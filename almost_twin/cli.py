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
    prep.add_argument('--scenario', default='t4_distinct_leads_001', choices=['t0_identical_001', 't2_name_001', 't4_distinct_leads_001'])
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
    run = sub.add_parser('run', help='Dry run by default; one researcher OR one prisoner pair, no batch')
    run.add_argument('stage', choices=['researcher', 'prisoner'])
    run.add_argument('--assignment', choices=['cdt_sep', 'edt_sep', 'fdt_eq4', 'fdt_policy', 'cdt_wikipedia', 'edt_wikipedia'], required=True)
    run.add_argument('--settings', type=Path, default=Path('configs/openrouter.example.json'))
    run.add_argument('--capabilities', type=Path, help='Offline snapshot from inspect-model; live mode refreshes metadata')
    run.add_argument('--essay', type=Path, help='Prisoner stage: completed researcher run directory')
    run.add_argument('--scenario', default='t4_distinct_leads_001',
                     choices=['t0_identical_001', 't2_name_001', 't4_distinct_leads_001'])
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
        elif args.command == 'run':
            from .router import run
            print(run(root, args))
    except (EvalError, OSError, ValueError, KeyError, urllib.error.URLError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
