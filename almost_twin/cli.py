import argparse
import json
import sys
import urllib.error
from pathlib import Path

from .common import EvalError, write_json
from .progress_log import enable_progress, restore_progress


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
    prep.add_argument('--researcher-max-tokens', type=int, help='Override effort-specific default (low 16000, high 32000)')
    prep.add_argument('--prisoner-max-tokens', type=int, help='Override effort-specific default (low 6000, high 12000)')
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
    bprep.add_argument('--researcher-max-tokens', type=int, help='Override effort-specific default (low 16000, high 32000)')
    bprep.add_argument('--prisoner-max-tokens', type=int, help='Override effort-specific default (low 6000, high 12000)')
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
    for preparation in (prep, bprep):
        preparation.add_argument('--essay-target-words', type=int, nargs=2, metavar=('MIN', 'MAX'),
                                 help='Requested essay length; default 1200 1500')
        preparation.add_argument('--essay-max-words', type=int, help='Hard essay limit; default 2500')
        preparation.add_argument('--essay-max-json-bytes', type=int, help='Independent hard serialized essay limit; default 32000 bytes')
        preparation.add_argument('--api-timeout-seconds', type=float, default=600,
                                 help='HTTP generation timeout per call; default 600 seconds; no automatic retries')
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
    study = sub.add_parser('study', help='Prepare, execute and summarize a frozen multi-model/theory matrix')
    study_actions = study.add_subparsers(dest='study_command', required=True)
    scheck = study_actions.add_parser('check', help='Unbilled full-matrix endpoint and budget preflight; no generations')
    scheck.add_argument('--config', type=Path, required=True)
    scheck.add_argument('--out', type=Path, help='Optional JSON preflight report')
    sprep = study_actions.add_parser('prepare', help='Unbilled preflight and preparation of every complete-scenario batch')
    sprep.add_argument('--config', type=Path, required=True)
    sprep.add_argument('--out', type=Path, required=True, help='New study directory; will never overwrite')
    srun = study_actions.add_parser('run', help='Resume the matrix using existing batch audit/budget protections')
    srun.add_argument('--study', type=Path, required=True)
    srun.add_argument('--execute', action='store_true')
    srun.add_argument('--confirm-billable', action='store_true')
    srun.add_argument('--approve-variable-prompts', action='store_true')
    srun.add_argument('--jobs', type=int, default=5,
                      help='Global maximum concurrent complete scenarios across model cells (default: 5; 1..16)')
    srun.add_argument('--provider-jobs', type=int, default=2,
                      help='Maximum concurrent scenarios per provider family (default: 2; 1..16)')
    srun.add_argument('--limit-cells', type=int, help='Process at most this many pending condition cells')
    srun.add_argument('--limit-per-cell', type=int, help='Process at most this many pending scenarios per selected cell')
    sstatus = study_actions.add_parser('report', help='Regenerate study-wide CSV/JSON/Markdown results; no model calls')
    sstatus.add_argument('--study', type=Path, required=True)
    publication = sub.add_parser('export-publication', help='Deterministic offline curated study export; no model calls')
    publication.add_argument('--out', type=Path, default=Path('published'))
    publication.add_argument('--study', type=Path, action='append', help='Frozen study directory; defaults to the two completed main studies')
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
    previous_progress_level = (enable_progress()
        if args.command in ('study', 'batch', 'pilot', 'run', 'run-judge', 'inspect-model')
        else None)
    try:
        if args.command == 'fetch-sources':
            from .sources import fetch_sources
            print(json.dumps(fetch_sources(root, args.source, args.network, args.reextract), indent=2))
        elif args.command == 'export-publication':
            from .publication import export_publication
            print(export_publication(root, args.out, args.study))
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
                    print(f"Exploratory pilot; no billable requests. Three-call expected cost (heuristic): "
                          f"${plan['expected_three_call_usd']}; conservative upper estimate: "
                          f"${plan['projected_three_call_usd']}.")
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
            print(f"Review: {folder / 'plan.md'}; readable sample transcripts: {folder / 'samples'}")
        elif args.command == 'study':
            from .study import check as study_check, load_spec as study_load_spec
            from .study import prepare as study_prepare, run as study_run, report as study_report
            if args.study_command == 'check':
                specification, _ = study_load_spec(args.config)
                result, _, _ = study_check(root, specification)
                if args.out:
                    write_json(args.out, result)
                print(json.dumps({k: result[k] for k in ('expected_cells', 'projected_researcher_prisoner_calls',
                            'possible_judge_calls', 'expected_researcher_prisoner_usd',
                            'projected_researcher_prisoner_usd',
                            'projected_full_context_ceiling_usd', 'expected_cost_method',
                            'cost_projection_method', 'failures')}, indent=2))
                if result['failures']:
                    return 1
                print('All requested model/effort/provider cells passed unbilled preflight. No generations occurred.')
                return 0
            if args.study_command == 'prepare':
                folder = study_prepare(root, args)
                print(f'Prepared {folder}; NO billable calls. Review plan.md, preflight.json and each batch plan.')
            elif args.study_command == 'run':
                folder = study_run(root, args)
            else:
                folder = study_report(root, args.study)
            summary = json.loads((folder / 'summary.json').read_text())
            print(f"Study: {summary['total_complete_pairs']}/{summary['total_samples']} complete pairs; statuses: {summary['status_counts']}")
            print(f"Results: {folder / 'summary.md'}, {folder / 'summary.csv'}, {folder / 'pairs.csv'}, {folder / 'decisions.csv'}")
            if args.study_command != 'prepare':
                usage = summary['provider_usage']
                print(f"Provider-reported cost: ${usage['reported_provider_usd']} "
                      f"({usage['priced_calls']}/{usage['attempted_calls']} calls priced; "
                      f"{usage['unpriced_calls']} unknown). "
                      f"Aggregate cell execution: {usage['recorded_execution_seconds']}s; "
                      f"last run wall time: {usage.get('last_run_wall_seconds')}s; "
                      f"HTTP 429 failed scenarios: {usage['rate_limit_failures']}.")
                print(f"Readable transcripts: {folder / 'batches'}; "
                      f"review dispositions: {folder / 'review_summary.md'}")
        elif args.command == 'run':
            from .router import run
            print(run(root, args))
    except (EvalError, OSError, ValueError, KeyError, urllib.error.URLError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    finally:
        if previous_progress_level is not None:
            restore_progress(previous_progress_level)
    return 0


if __name__ == '__main__':
    sys.exit(main())

