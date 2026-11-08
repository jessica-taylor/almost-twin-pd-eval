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
    f.add_argument('--source', action='append', choices=['cdt', 'edt', 'fdt'])
    f.add_argument('--network', action='store_true')
    f.add_argument('--reextract', action='store_true', help='Offline re-extraction of hash-verified cached downloads')
    r = sub.add_parser('render-prompts', help='Always offline; complete staged messages and precise pair diffs')
    r.add_argument('--assignment', choices=['cdt', 'edt', 'fdt_eq4', 'fdt_policy'], default='fdt_eq4')
    r.add_argument('--demo', action='store_true')
    r.add_argument('--essay', type=Path, help='Verbatim essay file; use fixtures/demo_essay.md for a labeled preview')
    r.add_argument('--out', type=Path)
    judge = sub.add_parser('prepare-adjudication', help='Offline blinded judge prompts for a completed prisoner run')
    judge.add_argument('--run', type=Path, required=True, help='Path to the saved prisoner pair run')
    m = sub.add_parser('inspect-model', help='Unbilled metadata only; never selects a model')
    m.add_argument('--model', required=True)
    m.add_argument('--network', action='store_true')
    m.add_argument('--out', type=Path, default=Path('data/openrouter/capabilities.json'))
    run = sub.add_parser('run', help='Dry run by default; one researcher OR one prisoner pair, no batch')
    run.add_argument('stage', choices=['researcher', 'prisoner'])
    run.add_argument('--assignment', choices=['cdt', 'edt', 'fdt_eq4', 'fdt_policy'], required=True)
    run.add_argument('--settings', type=Path, default=Path('configs/openrouter.example.json'))
    run.add_argument('--capabilities', type=Path, help='Offline snapshot from inspect-model; live mode refreshes metadata')
    run.add_argument('--essay', type=Path, help='Prisoner stage: completed researcher run directory')
    run.add_argument('--scenario', default='t4_distinct_leads_001',
                     choices=['t0_identical_001', 't2_name_001', 't4_distinct_leads_001'])
    run.add_argument('--execute', action='store_true')
    run.add_argument('--confirm-billable', action='store_true')
    run.add_argument('--prompts-approved', action='store_true', help='Explicitly acknowledge manual rendered prompt approval')
    run.add_argument('--source-terms-reviewed', action='store_true', help='Acknowledge resolved third-party article transmission rights')
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
        elif args.command == 'inspect-model':
            from .router import snapshot
            if not args.network:
                raise EvalError('Network disabled: inspect-model requires --network (unbilled metadata only)')
            write_json(args.out, snapshot(args.model))
            print(args.out)
        elif args.command == 'run':
            from .router import run
            print(run(root, args))
    except (EvalError, OSError, ValueError, KeyError, urllib.error.URLError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
