import argparse
import json
import sys
import urllib.error
from pathlib import Path

from .common import EvalError, write_json


def parser():
    p = argparse.ArgumentParser(description='Offline-first essay → independent fictional decision pair scaffold')
    p.add_argument('--root', type=Path, default=Path.cwd(), help='Repository root containing prompts/configs/sources')
    sub = p.add_subparsers(dest='command', required=True)
    f = sub.add_parser('fetch-sources', help='Reproducible local source acquisition; requires --network')
    f.add_argument('--source', action='append', choices=['cdt_sep', 'edt_sep', 'fdt', 'cdt_wikipedia', 'edt_wikipedia'])
    f.add_argument('--network', action='store_true')
    f.add_argument('--reextract', action='store_true', help='Offline re-extraction of hash-verified cached downloads')
    r = sub.add_parser('render-prompts', help='Always offline; complete staged messages and precise pair diffs')
    r.add_argument('--assignment', choices=['cdt_sep', 'edt_sep', 'fdt_eq4', 'fdt_policy', 'cdt_wikipedia', 'edt_wikipedia'], default='fdt_eq4')
    r.add_argument('--demo', action='store_true')
    r.add_argument('--essay', type=Path, help='Verbatim essay file; use fixtures/demo_essay.md for a labeled preview')
    r.add_argument('--out', type=Path)
    judge = sub.add_parser('prepare-adjudication', help='Offline blinded judge prompts for a completed prisoner run')
    judge.add_argument('--run', type=Path, required=True, help='Path to the saved prisoner pair run')
    j = sub.add_parser('run-judge', help='Offline by default; optionally ask a pinned OpenRouter judge about ambiguous prisoner responses')
    j.add_argument('--run', type=Path, required=True, help='Original prisoner-pair run directory')
    j.add_argument('--settings', type=Path, default=Path('configs/judge.example.json'))
    j.add_argument('--capabilities', type=Path, help='Optional offline OpenRouter capability snapshot')
    j.add_argument('--execute', action='store_true')
    j.add_argument('--confirm-billable', action='store_true')
    j.add_argument('--prompts-approved', action='store_true')
    j.add_argument('--max-calls', type=int, default=2)
    j.add_argument('--max-usd', type=str, default='1.00')
    m = sub.add_parser('inspect-model', help='Unbilled metadata only; never selects a model')
    m.add_argument('--model', required=True)
    m.add_argument('--network', action='store_true')
    m.add_argument('--out', type=Path, default=Path('data/openrouter/capabilities.json'))
    approval = sub.add_parser('approve-source', help='Legacy optional source verification; never required for execution')
    approval.add_argument('--source', required=True)
    approval.add_argument('--source-terms-reviewed', action='store_true', help=argparse.SUPPRESS)
    pilot = sub.add_parser('pilot', help='Prepare and resume a small exploratory researcher → prisoner pair pilot')
    actions = pilot.add_subparsers(dest='pilot_command', required=True)
    prep = actions.add_parser('prepare', help='Refresh unbilled metadata, select/pin endpoint, export exact researcher request and costs; no generations')
    prep.add_argument('--assignment', required=True)
    prep.add_argument('--model', required=True)
    prep.add_argument('--researcher-effort', default='low')
    prep.add_argument('--prisoner-effort', default='low')
    prep.add_argument('--researcher-max-tokens', type=int, default=12000)
    prep.add_argument('--prisoner-max-tokens', type=int, default=3000)
    prep.add_argument('--scenario', default='t4_distinct_leads_001',
                      help='Active case_id in prompts/prisoner/observation_cases.yaml')
    prep.add_argument('--provider-tag', help='Override automatic endpoint selection; never silently replaced')
    prep.add_argument('--capabilities', type=Path, help='Use a saved snapshot for entirely offline preparation instead of metadata GETs')
    prep.add_argument('--allow-unverified-effort', metavar='REASON', help='Record a manual override only when metadata is insufficient; cannot override explicit unsupported efforts')
    prep.add_argument('--temperature', type=float)
    prep.add_argument('--seed', type=int)
    prep.add_argument('--out', type=Path, help='New pilot directory; default data/pilots/<uuid>')
    prep.add_argument('--max-calls', type=int, default=3)
    prep.add_argument('--max-usd', default='2.00')
    for stage in ('researcher', 'prisoners'):
        step = actions.add_parser(stage, help='Dry-run/inspect by default; both billing flags are required for generation')
        step.add_argument('--pilot', type=Path, required=True)
        step.add_argument('--execute', action='store_true')
        step.add_argument('--confirm-billable', action='store_true')
        step.add_argument('--prompts-approved', action='store_true', help='Approve the prepared serialized requests by hash; persisted locally')
        step.add_argument('--source-terms-reviewed', action='store_true', help=argparse.SUPPRESS)
    batch = sub.add_parser('batch', help='Prepare/run/export repeated full essay + prisoner pair + optional judge samples')
    batch_actions = batch.add_subparsers(dest='batch_command', required=True)
    bprep = batch_actions.add_parser('prepare', help='Prepare a pinned exploratory batch; all metadata calls are unbilled')
    bprep.add_argument('--assignment', default='cdt_wikipedia',
                       choices=['cdt_sep', 'edt_sep', 'fdt_eq4', 'fdt_policy', 'cdt_wikipedia', 'edt_wikipedia'])
    bprep.add_argument('--model', default='openai/gpt-5-nano')
    bprep.add_argument('--count', type=int, required=True)
    bprep.add_argument('--scenario', default='t4_distinct_leads_001',
                       help='Active case_id in prompts/prisoner/observation_cases.yaml')
    bprep.add_argument('--researcher-effort', default='low')
    bprep.add_argument('--prisoner-effort', default='low')
    bprep.add_argument('--researcher-max-tokens', type=int, default=12000)
    bprep.add_argument('--prisoner-max-tokens', type=int, default=3000)
    bprep.add_argument('--provider-tag')
    bprep.add_argument('--capabilities', type=Path)
    bprep.add_argument('--allow-unverified-effort')
    bprep.add_argument('--temperature', type=float)
    bprep.add_argument('--seed-base', type=int,
                       help='Optional explicit per-sample seed: base+sample index; omitted by default')
    bprep.add_argument('--judge-model', default='openai/gpt-6.1-sol')
    bprep.add_argument('--judge-provider-tag')
    bprep.add_argument('--judge-effort', default='low')
    bprep.add_argument('--judge-max-tokens', type=int, default=1200)
    bprep.add_argument('--judge-capabilities', type=Path)
    bprep.add_argument('--judge-allow-unverified-effort')
    bprep.add_argument('--no-judge', action='store_true', help='Leave ambiguous classifications pending human/later judging')
    bprep.add_argument('--max-calls', type=int, required=True, help='Persistent project-wide generation call cap')
    bprep.add_argument('--max-usd', required=True, help='Persistent project-wide estimated generation USD cap')
    bprep.add_argument('--judge-max-calls', type=int, default=100, help='Separate persistent judge call cap')
    bprep.add_argument('--judge-max-usd', default='5.00', help='Separate persistent judge estimated USD cap')
    bprep.add_argument('--out', type=Path, help='New batch directory; default data/batches/<uuid>')
    brun = batch_actions.add_parser('run', help='Resume pending samples; explicit billable and template-family authorization required')
    brun.add_argument('--batch', type=Path, required=True)
    brun.add_argument('--execute', action='store_true')
    brun.add_argument('--confirm-billable', action='store_true')
    brun.add_argument('--approve-variable-prompts', action='store_true',
                      help='Authorize reviewed template family with fresh, unreviewed generated essays and judge inputs')
    brun.add_argument('--jobs', type=int, default=1, help='Concurrent full samples (each contains sequential stages)')
    brun.add_argument('--limit', type=int, help='Process at most this many pending samples in this invocation')
    brun.add_argument('--wait-for-lock', action='store_true')
    bstatus = batch_actions.add_parser('status', help='Regenerate CSV/JSONL derived indexes; no generation')
    bstatus.add_argument('--batch', type=Path, required=True)
    run = sub.add_parser('run', help='Dry run by default; one researcher OR one prisoner pair, no batch')
    run.add_argument('stage', choices=['researcher', 'prisoner'])
    run.add_argument('--assignment', choices=['cdt_sep', 'edt_sep', 'fdt_eq4', 'fdt_policy', 'cdt_wikipedia', 'edt_wikipedia'], required=True)
    run.add_argument('--settings', type=Path, default=Path('configs/openrouter.example.json'))
    run.add_argument('--capabilities', type=Path, help='Offline snapshot from inspect-model; live mode refreshes metadata')
    run.add_argument('--essay', type=Path, help='Prisoner stage: completed researcher run directory')
    run.add_argument('--scenario', default='t4_distinct_leads_001',
                     help='Active case_id in prompts/prisoner/observation_cases.yaml')
    run.add_argument('--execute', action='store_true')
    run.add_argument('--confirm-billable', action='store_true')
    run.add_argument('--prompts-approved', action='store_true', help='Explicitly acknowledge manual rendered prompt approval')
    run.add_argument('--source-terms-reviewed', action='store_true', help=argparse.SUPPRESS)
    run.add_argument('--max-calls', type=int)
    run.add_argument('--max-usd', type=str)
    return p


def main(argv=None):
    args = parser().parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == 'fetch-sources':
            from .sources import fetch_sources
            print(json.dumps(fetch_sources(root, args.source, args.network, args.reextract), indent=2))
        elif args.command == 'render-prompts':
            from .prompts import render
            if args.demo and args.essay:
                raise EvalError('--demo uses its own explicitly synthetic essay; omit --essay')
            print(render(root, args.assignment, args.demo, args.essay, args.out))
        elif args.command == 'prepare-adjudication':
            from .judge import prepare_adjudication
            print(prepare_adjudication(root, args.run))
        elif args.command == 'run-judge':
            from .judge_runner import run_judge
            print(run_judge(root, args))
        elif args.command == 'inspect-model':
            from .router import snapshot
            if not args.network:
                raise EvalError('Network disabled: inspect-model requires --network (unbilled metadata only)')
            write_json(args.out, snapshot(args.model))
            print(args.out)
        elif args.command == 'approve-source':
            from .approvals import approve_source
            identity = approve_source(root, args.source, args.source_terms_reviewed)
            print(f"Verified source {identity['source_id']} revision {identity['source_revision']} SHA-256 {identity['source_sha256']}. No source approval is required for execution.")
        elif args.command == 'pilot':
            from .pilot import prepare, resume
            folder = prepare(root, args) if args.pilot_command == 'prepare' else resume(root, args)
            print(folder)
            plan_path = folder / 'plan.json'
            if plan_path.exists():
                plan = json.loads(plan_path.read_text())
                if args.pilot_command == 'prepare':
                    print(f"Exploratory pilot; no billable requests. Researcher estimate: ${plan['researcher_estimated_usd']}; three-call projected upper estimate: ${plan['projected_three_call_usd']}.")
                    print(f"Inspect {folder / 'plan.md'} and {folder / 'researcher/messages_0.md'}")
                else:
                    print(f"Estimated stage maximum: ${plan.get('estimated_total_usd')}; exact requests and metadata: {plan_path}")
            if (folder / 'essay.md').exists():
                print(f"Frozen essay: {folder / 'essay.md'}. Inspect it before pilot prisoners.")
            if args.pilot_command != 'prepare':
                print(f"Pilot review index: {args.pilot.resolve() / 'plan.md'}")
        elif args.command == 'batch':
            from .batch import prepare as batch_prepare, run as batch_run, export as batch_export
            if args.batch_command == 'prepare':
                folder = batch_prepare(root, args)
            elif args.batch_command == 'run':
                folder = batch_run(root, args)
            else:
                folder = batch_export(root, args.batch)
            print(folder)
            summary = json.loads((folder / 'summary.json').read_text())
            print(f"Exploratory batch: {summary['total']} samples; statuses: {summary['counts']}")
            print(f"Analysis files: {folder / 'results.jsonl'} and {folder / 'results.csv'}")
            print(f"Review: {folder / 'plan.md'}; raw runs: {folder / 'samples'}")
        elif args.command == 'run':
            from .router import run
            print(run(root, args))
    except (EvalError, OSError, ValueError, KeyError, urllib.error.URLError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

