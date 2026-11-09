import csv
import hashlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from almost_twin.common import EvalError
from almost_twin.publication import export_publication
from almost_twin.publication_audit import findings

spec = importlib.util.spec_from_file_location('independent_publication_verifier', Path(__file__).parents[1]/'scripts/verify_publication.py')
verifier = importlib.util.module_from_spec(spec); spec.loader.exec_module(verifier)


def h(data):
    return hashlib.sha256(data).hexdigest()


def save(path, obj, frozen=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2)+'\n')
    if frozen:
        path.with_suffix('.sha256').write_text(h(path.read_bytes())+'\n')


def write_csv(path, rows, fields=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=fields or list(rows[0])); w.writeheader(); w.writerows(rows)


def fixture(root):
    study=root/'data/studies/fixture'; cell='cell'; batch=study/'batches'/cell
    source='SYNTHETIC source used only in tests. No actual article.'
    identity={'source_id':'fdt','source_revision':'arXiv:1710.05060v2','source_sha256':h(source.encode()),'source_provenance_sha256':'0'*64,'source_permanent_url':'https://arxiv.org/src/1710.05060v2'}
    essay=b'SYNTHETIC model essay.\r\nIts exact line endings are evidence.\r\n'
    settings={'model':'mock/model','provider_tag':'mock','researcher':{'effort':'low','max_tokens':32000},'prisoner':{'effort':'low','max_tokens':12000}}
    case={'private_a':'PRIVATE_A','private_b':'PRIVATE_B','evidence_a':'EVIDENCE_A','evidence_b':'EVIDENCE_B'}
    rows=[]
    def call(run,name,request,content=None):
        d=root/'data/exploratory/runs'/run/name;save(d/'request.json',request)
        if content is not None:
            save(d/'response.raw',{'model':request['model'],'created':123,'provider':'mock','choices':[{'finish_reason':'stop','message':{'content':content}}], 'usage':{'cost':1,'prompt_tokens':10,'completion_tokens':4}})
            (d/'output.txt').write_bytes(content.encode())
            save(d/'transport.json',{'status':200,'headers':{'Date':'test','Set-Cookie':'private-cookie-value; Path=/','CF-Ray':'private-trace-SJC','X-OpenRouter-Release':'release'}})
        return d.parent
    req={'model':'mock/model','reasoning':{'effort':'low'},'max_tokens':32000,'messages':[{'role':'user','content':'Synthetic instruction\n<source_document>\n'+source+'\n</source_document>\n'}]}
    for i,status in enumerate(['complete','failed','prepared']):
        sid=f's{i}';sample=batch/'samples'/f'{i:05d}'
        pilot={'settings':settings,'source_identity':identity,'template_hashes':{'fixture':'hash'},'scenario_record':case}
        save(sample/'pilot.json',pilot,True)
        state={};rr=pr=jr=''
        if i<2:
            run=call('r'+str(i),'call_0',req,essay.decode() if i==0 else None);rr=str(run)
            state.update(researcher_run=rr,researcher_status='success' if i==0 else 'attempted')
        if i==0:
            (run/'essay.md').write_bytes(essay)
            state['essay_sha256']=h(essay)
            for role,num in [('a',0),('b',1)]:
                request={'model':'mock/model','reasoning':{'effort':'low'},'max_tokens':12000,'messages':[{'role':'user','content':essay.decode()+'\n'+case['private_'+role]+'\n'+case['evidence_'+role]+'\n'+case['evidence_'+role]}]}
                run=call('p0','call_'+str(num),request,'pass' if num==0 else 'submit letter with evidence')
            pr=str(run);state.update(prisoner_run=pr,prisoner_status='success')
            save(run/'outcome.json',{'needs_review':[1],'enacted_actions':['WITHHOLD',None],'enacted_score':None})
            jreq={'model':'mock/judge','messages':[{'role':'user','content':'synthetic judgement request'}]}
            run=call('j0','call_b',jreq,'synthetic judgement');jr=str(run)
            save(run/'adjudicated_outcome.json',{'adjudicated_actions':['WITHHOLD','SUBMIT'],'needs_human_review':[], 'judgements':{'b':{'intent':'TRIED_DEFECT','disclosure':'YES','needs_human_review':False}},'adjudicated_score':{'years':[5,0],'utilities':[0,5]}})
            save(sample/'sample_state.json',{'judge_status':'success','judge_run':jr})
        save(sample/'state.json',state)
        rows.append({'id':cell,'assignment':'fdt_eq4','model':'mock/model','researcher_effort':'low','prisoner_effort':'low','sample_id':sid,'sample_index':str(i),'status':status,'pair_outcome':'CD' if i==0 else '', 'final_a':'WITHHOLD' if i==0 else '', 'final_b':'SUBMIT' if i==0 else '', 'essay_sha256':h(essay) if i==0 else '', 'researcher_run':rr,'prisoner_run':pr,'judge_run':jr,'reported_provider_usd':'4' if i==0 else '0'})
    save(batch/'batch.json',{'samples':[{'sample_id':'s'+str(i),'index':i,'path':'samples/'+f'{i:05d}'} for i in range(3)]},True)
    study.mkdir(parents=True,exist_ok=True);(study/'specification.yaml').write_text('synthetic: true\n')
    save(study/'study.json',{'schema_version':1,'repo_root':str(root),'study_id':'synthetic-study','spec_sha256':h((study/'specification.yaml').read_bytes()),'cells':[{'id':cell,'path':'batches/'+cell,'model':'mock/model','assignment':'fdt_eq4','researcher_effort':'low','prisoner_effort':'low'}]},True)
    write_csv(study/'pairs.csv',rows)
    write_csv(study/'decisions.csv',[{'sample_id':'s0','role':r,'final_action':x} for r,x in [('a','WITHHOLD'),('b','SUBMIT')]])
    write_csv(study/'failures.csv',[{'sample_id':'s1'}])
    c={'cell_id':cell,'complete_pairs':1,'samples_planned':3,'cooperation_rate':.5,'reported_provider_usd':'4','priced_calls':4,'pair_bootstrap_ci_low':None,'pair_bootstrap_ci_high':None,**{'outcome_'+x:1 if x=='CD' else 0 for x in ['CC','CD','DC','DD']},**{'status_'+s:1 if s in ['prepared','failed'] else 0 for s in ['prepared','failed','needs_human_review','resolved_nonaction','resolved_unscored']}}
    write_csv(study/'summary.csv',[c]);save(study/'summary.json',{'total_samples':3,'status_counts':{'complete':1,'failed':1,'prepared':1},'provider_usage':{'attempted_calls':5,'priced_calls':4,'unpriced_calls':1,'reported_provider_usd':'4','prompt_tokens':40,'completion_tokens':16},'cell_summaries':[c]})
    return study


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name);self.study=fixture(self.root)
    def tearDown(self):self.temp.cleanup()
    def export(self,name='published'):
        with patch('socket.socket',side_effect=AssertionError('Network forbidden')):
            return export_publication(self.root,self.root/name,[self.study])
    def test_all_states_and_independent_verification(self):
        out=self.export();r=verifier.verify(out,self.root)
        self.assertEqual(r['studies'][0]['status_counts'],{'complete':1,'failed':1,'prepared':1})
        self.assertEqual(r['studies'][0]['unknown_prices'],1)
        self.assertEqual((out/'runs/r0/essay.md').read_bytes(),(self.root/'data/exploratory/runs/r0/essay.md').read_bytes())
        self.assertEqual((out/'runs/r0/call_0/response.raw').read_bytes(),(self.root/'data/exploratory/runs/r0/call_0/response.raw').read_bytes())
        self.assertFalse((out/'runs/r0/call_0/request.json').exists())
        self.assertFalse((out/'runs/p0/call_0/transport.json').exists())
        self.assertNotIn(b'private-cookie-value',b''.join(p.read_bytes() for p in out.rglob('*') if p.is_file()))
        self.assertNotIn(str(self.root).encode(),b''.join(p.read_bytes() for p in out.rglob('*') if p.is_file()))
    def test_determinism_and_idempotence(self):
        a=self.export('one');b=self.export('two')
        tree=lambda root:{p.relative_to(root).as_posix():p.read_bytes() for p in root.rglob('*') if p.is_file()}
        self.assertEqual(tree(a),tree(b));self.assertEqual(self.export('one'),a)
    def test_changed_original_essay_rejected(self):
        (self.root/'data/exploratory/runs/r0/essay.md').write_text('tampered')
        with self.assertRaisesRegex(EvalError,'essay hash'):self.export()
    def test_tampered_raw_response_rejected(self):
        out=self.export();(out/'runs/p0/call_0/response.raw').write_text('{}')
        with self.assertRaisesRegex(ValueError,'hash mismatch'):verifier.verify(out)
    def test_changed_record_detected_even_with_updated_hash(self):
        out=self.export();m=json.loads((out/'MANIFEST.json').read_bytes());f=next(x for x in m['files'] if x['path'].endswith('/00000/record.json'));p=out/f['path'];j=json.loads(p.read_bytes());j['pair_outcome']='CC';save(p,j);f.update(sha256=h(p.read_bytes()),bytes=p.stat().st_size);save(out/'MANIFEST.json',m)
        with self.assertRaisesRegex(ValueError,'Outcome/action mismatch'):verifier.verify(out)
    def test_source_change_rejected(self):
        p=self.root/'data/exploratory/runs/r0/call_0/request.json';j=json.loads(p.read_bytes());j['messages'][0]['content']=j['messages'][0]['content'].replace('SYNTHETIC','ALTERED');save(p,j)
        with self.assertRaisesRegex(EvalError,'normalized source hash'):self.export()
    def test_secret_in_evidence_fails_without_redacting(self):
        p=self.root/'data/exploratory/runs/p0/call_0/response.raw';j=json.loads(p.read_bytes());secret='sk-or-v1-'+'a'*64;j['choices'][0]['message']['content']=secret;save(p,j);(p.parent/'output.txt').write_text(secret)
        with self.assertRaisesRegex(EvalError,'scan blocked'):self.export()
        self.assertIn(secret,p.read_text());self.assertFalse((self.root/'published').exists())
    def test_unknown_extra_file_rejected(self):
        out=self.export();(out/'private.txt').write_text('unexpected')
        with self.assertRaisesRegex(ValueError,'Unexpected'):verifier.verify(out)
    def test_refuses_to_overwrite_changed_export(self):
        out=self.export();(out/'README.md').write_text('human edit')
        with self.assertRaisesRegex(EvalError,'Nothing overwritten'):self.export()
        self.assertEqual((out/'README.md').read_text(),'human edit')
    def test_frozen_manifest_tampering_rejected(self):
        p=self.study/'study.json';j=json.loads(p.read_bytes());j['study_id']='tampered';save(p,j)
        with self.assertRaisesRegex(EvalError,'Frozen metadata'):self.export()
    def test_filtered_partial_pass_remains_failed_and_unscored(self):
        def rows(path):
            with path.open() as f:return list(csv.DictReader(f))
        p=self.study/'pairs.csv';rr=rows(p);rr[0].update(status='failed',pair_outcome='',final_a='',final_b='',judge_run='',reported_provider_usd='3');write_csv(p,rr)
        p=self.study/'batches/cell/samples/00000/state.json';j=json.loads(p.read_bytes());j['prisoner_status']='failed';save(p,j)
        save(p.parent/'sample_state.json',{})
        p=self.root/'data/exploratory/runs/p0/call_1/response.raw';j=json.loads(p.read_bytes());j['choices'][0].update(finish_reason='content_filter',native_finish_reason='refusal');j['choices'][0]['message'].update(content='pass',refusal='synthetic provider filter');save(p,j);(p.parent/'output.txt').write_text('pass')
        c=rows(self.study/'summary.csv')[0];c.update(complete_pairs=0,cooperation_rate=None,reported_provider_usd='3',priced_calls=3,outcome_CD=0,status_failed=2);write_csv(self.study/'summary.csv',[c])
        q=json.loads((self.study/'summary.json').read_bytes());q.update(status_counts={'failed':2,'prepared':1},cell_summaries=[c]);q['provider_usage'].update(attempted_calls=4,priced_calls=3,reported_provider_usd='3',prompt_tokens=30,completion_tokens=12);save(self.study/'summary.json',q)
        write_csv(self.study/'failures.csv',[{'sample_id':'s0'},{'sample_id':'s1'}])
        out=self.export();r=verifier.verify(out,self.root);self.assertEqual(r['studies'][0]['status_counts'],{'failed':2,'prepared':1})
        rec=json.loads((out/'studies/fixture/batches/cell/samples/00000/record.json').read_bytes());self.assertIsNone(rec['pair_outcome'])
    def test_scanner_does_not_echo_secrets(self):
        secret='ghp_'+'b'*40;r=findings(secret.encode(),'fixture')
        self.assertTrue(r);self.assertNotIn(secret,json.dumps(r))
    def test_scanner_unprefixed_credentials(self):
        value='synthetic'+'credential'*3
        for raw in [('password = "'+value+'"'),('OPENROUTER_API_KEY='+value),('https://fixture:'+value+'@invalid.example')]:
            result=findings(raw.encode(),'synthetic fixture')
            self.assertTrue(result);self.assertNotIn(value,json.dumps(result))
    def test_derivative_span_including_crlf_is_verified(self):
        out=self.export();m=json.loads((out/'MANIFEST.json').read_bytes())
        f=next(f for f in m['files'] if f['path']=='runs/r0/call_0/request.source_omitted.json')
        operation=f['operations'][0];original=json.loads((self.root/'data/exploratory/runs/r0/call_0/request.json').read_bytes())
        raw=original['messages'][0]['content'].encode();a,b=operation['span_utf8_bytes']
        self.assertEqual(h(raw[a:b]),operation['omitted_sha256'])
        verifier.verify(out,self.root)
    def test_wikipedia_copy_is_pinned_attributed_and_not_in_requests(self):
        source='SYNTHETIC licensed Wikipedia fixture.\n'
        folder=self.root/'data/source_cache/cdt_wikipedia/frozen';folder.mkdir(parents=True)
        (folder/'article.md').write_text(source)
        save(folder/'provenance.json',{'attribution':{'contributors':'Wikipedia contributors','license_url':'https://creativecommons.org/licenses/by-sa/4.0/','permanent_url':'https://en.wikipedia.org/w/index.php?oldid=123'}})
        identity={'source_id':'cdt_wikipedia','source_revision':123,'source_sha256':h(source.encode()),'source_provenance_sha256':h((folder/'provenance.json').read_bytes()),'source_permanent_url':'https://en.wikipedia.org/w/index.php?oldid=123'}
        for p in self.study.glob('batches/*/samples/*/pilot.json'):
            j=json.loads(p.read_bytes());j['source_identity']=identity;save(p,j,True)
        for p in (self.root/'data/exploratory/runs').glob('r*/call_0/request.json'):
            j=json.loads(p.read_bytes());j['messages'][0]['content']='<source_document>\n'+source+'\n</source_document>';save(p,j)
        out=self.export();self.assertEqual((out/'sources/cdt_wikipedia-123/article.md').read_bytes(),source.encode())
        self.assertNotIn(source,(out/'runs/r0/call_0/request.source_omitted.json').read_text())
        verifier.verify(out,self.root)


if __name__=='__main__':unittest.main()
