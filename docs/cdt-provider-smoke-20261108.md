# CDT cross-provider smoke: November 2026

This is a **compatibility/plumbing run**, not a powered test of the CDT
hypothesis. The configuration is
[`configs/study.cdt-provider-smoke-20261108.yaml`](../configs/study.cdt-provider-smoke-20261108.yaml).

## Fixed design

- **Only CDT:** `cdt_wikipedia`, using the pinned human-written Wikipedia
  source. Do not change the researcher or prisoner prompts mid-run.
- **One scenario:** `t4_distinct_leads_001`; fixed, distinct prisoner A/B
  observations and the same frozen essay within a pair.
- **Seven models:** `google/gemini-3.8-flash` (previous working baseline),
  `openai/gpt-6.1-terra`, `anthropic/claude-sonnet-5.5`,
  `z-ai/glm-5.3`, `deepseek/deepseek-v4.1-flash`,
  `qwen/qwen3.8-27b`, and `openai/gpt-6-luna`. Do not include Haiku in
  this pilot; the previous pilot established a refusal problem.
- **Low / low effort**, one independently generated researcher essay
  per scenario, `researcher_max_tokens: 12000`, `prisoner_max_tokens: 3000`.
  The existing enforced serialized-essay bound applies to prisoner context.
- **Two paired scenarios per model:** 14 total, requiring up to 42 baseline
  generation requests (14 essays + 28 prisoner decisions) and up to 28
  conditional Sol judge requests. First send **one pair per model** (seven
  scenarios), inspect, then consider the second pair per model.
- **Endpoint routing:** Use the existing checked OpenRouter provider selection
  and pin the resulting route per cell. Keep `allow_unverified_effort` and
  `provider_tag` unset unless a specific live preflight failure is reviewed
  and documented. No silent substitutions.
- **Budget:** Config ceilings are cumulative project-wide ceilings, inclusive
  of previous pilots and outstanding reservations. They are safety limits,
  not permission to spend the entire ceiling.

Model IDs were checked against public OpenRouter model listings when the config
was drafted; **that does not establish that a currently selected endpoint
supports all requested parameters**. Only the local `study check` establishes
that for this exact configuration.

## Check and freeze, with no paid generations

After merging the config and pulling current `main`, from the repository root:

```bash
python3 -m almost_twin fetch-sources --network --source cdt_wikipedia
python3 -m almost_twin study check \
  --config configs/study.cdt-provider-smoke-20261108.yaml \
  --out data/cdt-provider-smoke-20261108-preflight.json
python3 -m almost_twin study prepare \
  --config configs/study.cdt-provider-smoke-20261108.yaml \
  --out data/studies/cdt-provider-smoke-20261108
```

`fetch-sources` downloads the source; `study check` reads live metadata
without billable model generations, and `study prepare` freezes the validated
plan without generating responses. **Do not proceed to preparation if
`study check` reports any failed cell or the budget fails.** Inspect the
expected-cost heuristic, conservative estimate, full-context diagnostic,
selected provider tags, rejected candidate endpoints, source hashes and
the prepared `plan.md`.

This must use a **new study directory** because the prior reporting/context
changes altered the hash-pinned generation runner. Do not try to resume the
older Haiku/Gemini study with new code.

## First pass: one pair per model

Only the following step is billable and needs explicit authorization:

```bash
python3 -m almost_twin study run \
  --study data/studies/cdt-provider-smoke-20261108 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 1 --limit-per-cell 1
```

With `--limit-per-cell 1` and no `--limit-cells`, the runner attempts up to
one pending scenario in **each** of the seven model cells. Cell execution is
sequential and a scenario's researcher and two prisoner calls are sequential,
so `--jobs 1` minimizes overlapping requests and helps identify rate limits.
Failed attempts are preserved and are **not** automatically retried.

Review `summary.md`, `summary.csv`, `review_summary.md`,
`review_samples.csv`, and the per-cell
`samples/00000/{result.md,transcript.txt}`. Check:

1. **Endpoint:** intended exact model ID; selected provider tag and actual
   route/provenance; no model or effort substitution.
2. **Request/response:** researcher essay completed without truncation; each
   prisoner received that frozen essay plus its correct fixed private lead;
   response was saved in full; finish reason, returned reasoning metadata,
   context limit and response parsing are sensible.
3. **Failures:** distinguish preflight/parameter errors, HTTP failures,
   timeouts, HTTP 429, malformed content, judge errors and unscorable outcomes.
   Judge decisions should agree with the visible actions.
4. **Refusals:** a clear refusal may produce `resolved_nonaction`; this is
   **unscored**, neither cooperation nor a transport failure. Do not impute a
   `pass` action. Read the explanation in the transcript.
5. **Costs:** compare provider-reported `usage.cost` and wall time by model;
   missing charge records remain unknown, not zero.

Keep a short issue log keyed by model/provider, whether preflight succeeded,
whether the essay and two prisoner calls returned, whether action parsing and
judging worked, whether 429s occurred, and the specific error text. This
pilot should primarily inform the next **model/provider selection and adapter
fixes**, not estimate cooperation rates from one or two pairs.

## Optional second pass

After reviewing the first seven scenarios, if the selected endpoints and budget
still look acceptable, run:

```bash
python3 -m almost_twin study run \
  --study data/studies/cdt-provider-smoke-20261108 \
  --execute --confirm-billable --approve-variable-prompts --jobs 1
```

Already terminal scenarios are skipped, so this fills in the other prepared
sample per model without repeating completed or failed calls. If a model
fails, investigate before continuing; do not change the frozen specification,
retry a billed failure implicitly, or treat unscored cases as defects.

The run automatically regenerates the summary and readable reports. To
regenerate offline later:

```bash
python3 -m almost_twin study report --study data/studies/cdt-provider-smoke-20261108
```

No stats-driven comparisons are intended at `n=2` per model. For the
general workflow and exact status meanings, see
[study_workflow.md](study_workflow.md).
