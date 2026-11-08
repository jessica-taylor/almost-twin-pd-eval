# Multi-model/theory exploratory study

This is a thin, audited orchestration layer over the existing `batch` runner.
**One sample is one independently generated researcher essay, two separate
prisoner generations using that essay, and zero to two judge calls.** There is
no model call during study checking or preparation.

The user-selected mainline prisoner A/B observations and evidence leads stay
**fixed, distinct and explicitly labeled**. Analysis weights A and B equally
within each scored pair. This layer does *not* randomize prisoner roles, rewrite
the sources, modify any decision theory or change the action classifier.

## Before checking the matrix

Download and inspect the human-authored sources, including the FDT Equation (4)
and footnote 16 passages in the *actual normalized text*:

```sh
python3 -m almost_twin fetch-sources --network \
  --source cdt_wikipedia --source edt_wikipedia --source fdt
```

Review [study.example.yaml](../configs/study.example.yaml). This is a **candidate
model slate**, not a verified guarantee of support for low/high reasoning on
every serving endpoint. A supported-effort failure, missing model or unknown
pricing cannot be bypassed by silently switching models. You may explicitly
set `provider_tag` or a documented `allow_unverified_effort` on an individual
model if the endpoint really supports the selected effort. Efforts are
comparisons *within* a model, not equal thinking-compute quotas across vendors.
For Chinese open-weights models, note the exact selected host and endpoint in
the preflight before running: hosts may differ in quantization/behavior.

## Check first — no paid generations

```sh
python3 -m almost_twin study check \
  --config configs/study.example.yaml \
  --out data/study_preflight.json
```

All requested treatment × model × researcher-effort × prisoner-effort cells
must pass. The command checks each cell's researcher prompt, a provisional
prisoner request, source and scenario validity, judge endpoint, pricing and
**aggregate project-wide** budget. It reports every incompatible cell; it
does not skip or substitute any requested condition. It requires unbilled
OpenRouter metadata GETs, not credentials or model-generation calls.

The `max_usd` field in the example is a protective project-wide reservation
ceiling. The default cost projection uses an **independent essay-size bound**:
the researcher's output is limited to `essay.max_json_bytes` (32,000 by default)
JSON-encoded essay bytes, and the prisoner projection adds that to the exact
scenario/template overhead. The large former full-context estimate is still
shown separately for comparison. The byte-based estimator is conservative,
not a claim about the model's tokenizer. Oversized essay responses are preserved
as failed researcher attempts, without sending prisoner requests; the actual
assembled requests are always validated independently before billing.
`study check` also displays a separate **expected-cost heuristic** (up to 3,000
researcher output tokens, 800 prisoner output tokens and four serialized essay
bytes per researcher output token). That forecast is intended for planning,
not used to authorize spending; the conservative essay-bound projection is used
for preparation budget checks. Real charges are reported from provider-supplied
usage, when present. Budgets count previously
reserved project requests; a fresh study does not reset the underlying ledger.

For the smallest previously validated CDT plumbing experiment, use
`configs/study.smoke.example.yaml` instead.

### Long-essay follow-up

This section describes the historical 16K configuration. Its explicit token
settings are retained. Use the independent settings below for new comparisons;
existing prepared study directories and their failed attempts remain unchanged.

`configs/study.cdt-provider-smoke-16k.yaml` follows the original
`cdt-provider-smoke-20261108` with **one scenario per model**, the same seven
models and explicit original endpoints, CDT Wikipedia source, distinct T4
leads and low researcher/prisoner efforts. The prisoner and judge limits and
cumulative project budgets are unchanged. Keep the original study directory;
never replace its failed attempts with new successes.

That run originally enforced 1,800 words and derived the byte ceiling from
researcher output tokens. New preparations use the independent limits below.
Reporting an existing study never reclassifies its original failures as successes.

Prepare with unbilled metadata requests only:

```sh
python3 -m almost_twin study prepare \
  --config configs/study.cdt-provider-smoke-16k.yaml \
  --out data/studies/cdt-provider-smoke-16k
```

Inspect `plan.md`, `preflight.json`, and each batch's researcher messages before
running. Once prepared, **this separate command makes paid calls**:

```sh
python3 -m almost_twin study run \
  --study data/studies/cdt-provider-smoke-16k \
  --execute --confirm-billable --approve-variable-prompts --jobs 1
```

`summary.md` starts with failed-attempt diagnostics. `failures.csv`,
`summary.json` (`failed_attempts`), `pairs.csv` and each sample's `result.md`
include the stage, cause, provider-reported output/reasoning tokens, requested
output limit and visible essay words. The stable causes include:

| Cause | Meaning |
|---|---|
| `output_token_limit` | Provider returned `finish_reason: length`; partial output is preserved. |
| `essay_size_limit` | Completed researcher output exceeded the word or serialized-byte bound. |
| `provider_error` | Provider API or transport failed; unknown billing remains reserved. |
| `parse_error` | Malformed API response or missing usable researcher text. |
| `refusal` | Explicit researcher refusal field or provider content-filter stop. |

Other causes stay explicit (`incomplete_generation`, `validation_error`,
`preflight_error`, `unknown_failure`) rather than guessing. Refusals expressed
only in ordinary prose are not automatically inferred here. Prisoner
nonaction classification and adjudication are unchanged. Output-limit causes
take precedence over word counts for truncated responses. Offline reporting
can derive these diagnostics for historical failures without changing their
raw responses, logs or status.

For the DeepSeek failure, the saved model metadata advertises `low` effort but
does **not** advertise `reasoning.supports_max_tokens`; the selected
`atlas-cloud/fp8` endpoint only advertises generic reasoning parameters.
[OpenRouter's reasoning documentation](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens)
uses `supports_max_tokens: true` to advertise token-budget controls and warns
that a supplied reasoning budget can map to an effort level on effort-only
models. This does not establish a hard 4K–6K cap for that endpoint. The follow-up
therefore retains the exact `reasoning: {effort: low}` setting; it does not
silently add a token cap or send conflicting effort/budget fields. A future
provider-specific cap needs evidence of enforcement and its own explicit
configuration. Compare actual reasoning-token usage after the follow-up.

### Configurable essay and generation limits

New studies can configure the following independent limits:

```yaml
essay:
  target_words: [1200, 1500]
  max_words: 2500
  max_json_bytes: 32000
output_tokens:
  researcher: {low: 16000, high: 32000}
  prisoner: {low: 6000, high: 12000}
api_timeout_seconds: 600
```

These are the defaults. Word counts include all visible whitespace-delimited
text, including math and references. The requested target is advisory: a
1,852-, 1,853- or 2,091-word essay is accepted if it fits the hard word and byte
bounds. The original essay is passed verbatim to both prisoners. Short essays
are accepted too. Hard-limit failures preserve raw outputs and never trigger
truncation, rewriting or automatic retries.

`max_json_bytes` is **32,000 bytes**, measured after the same UTF-8 JSON string
escaping used in requests, without the enclosing string quotes. It bounds
essay content; the prisoner template, private observations and request framing
are additional. Increasing researcher reasoning/output tokens never increases
this ceiling or the prisoner input projection. Endpoint context capacity still
limits the projection, and actual untruncated requests are revalidated before
billing. Every selected endpoint must support the resolved output allowance;
the runner fails with model, endpoint, effort and limit details if it cannot.

`output_tokens` selects a total generation allowance for each requested effort.
It does not alter `reasoning.effort` or add `reasoning.max_tokens`. Low/high are
the provided defaults; explicitly add an allowance for other efforts (for
example `medium: 24000`) before requesting them. Existing top-level
`researcher_max_tokens` / `prisoner_max_tokens` values remain supported and apply
to every effort in that stage. Specifying both a scalar and that stage's effort
map is rejected as ambiguous. Existing explicit 3,000-token prisoner settings
therefore stay at 3,000 until you choose a new configuration.

The timeout is used for HTTP socket operations on researcher, prisoner and
judge calls, rather than as a total wall-clock deadline. It defaults to 600
seconds. Timeout failures remain failed attempts with unknown billing reserved.
All resolved settings are saved in plans, pinned settings and run records.

Essay records, sample reports and pair CSVs include `essay_words`,
`essay_json_bytes` and `essay_target_exceeded`; the append-only generation log
also records the exact target and hard limits. Study summaries count measured
essays above target independently of cooperation and hard-limit failures.
Historical records missing these target metrics stay unknown.

For a four-cell low/high configuration using the existing Nano plumbing model,
review `configs/study.token-limits-smoke.example.yaml` and its model list, then
check and prepare with **zero model calls**:

```sh
python3 -m almost_twin study check \
  --config configs/study.token-limits-smoke.example.yaml \
  --out data/token-limits-preflight.json
python3 -m almost_twin study prepare \
  --config configs/study.token-limits-smoke.example.yaml \
  --out data/studies/token-limits-smoke
```

The unit suite runs this kind of low/high matrix against mocked providers,
including the three reported near-limit essay sizes. No paid high-effort test
is part of implementation or preparation. Actual execution uses the separate
billable `study run` workflow after inspection. Keep earlier runs unchanged and
use a new directory for the new limits.

The same defaults apply to `pilot prepare` and `batch prepare`. Their optional
flags are `--essay-target-words MIN MAX`, `--essay-max-words`,
`--essay-max-json-bytes`, `--api-timeout-seconds`, `--researcher-max-tokens`
and `--prisoner-max-tokens`.

### Live command progress

`study check`, `study prepare`, and `study run` now print flushed
`[progress]` messages to stderr **while they work**. Preflight shows the
model being fetched/validated and the chosen endpoint for each cell;
preparation shows each completed batch; execution shows the active cell,
sample, researcher call, separate prisoner A/B calls, conditional judge
calls, and elapsed times. Slow metadata and API requests print a
`Still waiting` heartbeat every 20 seconds, so a quiet terminal does not
look hung. These lines contain identifiers and statuses, **not** source
articles, essays, prisoner observations, responses or credentials.

The append-only JSONL audit files remain authoritative; console messages are
informational, do not make additional requests, and do not change scoring.

### Cross-provider CDT pilot: Haiku versus Gemini Flash

`configs/study.cdt-haiku-gemini-smoke.yaml` specifies just two cells, in order:
`anthropic/claude-haiku-5.5` and `google/gemini-3.8-flash`. Both receive the
same pinned `cdt_wikipedia` article, distinct A/B prisoner leads, and `low`
researcher/prisoner effort, with **two full scenarios per model**. A conditional
`openai/gpt-6.1-sol` judge is shared. This is a plumbing and transcript audit;
four paired scenarios cannot support a reliable difference-in-rates claim.

Fetch the CDT article if it is not already cached, then check metadata and
pricing **without billable calls**:

```sh
python3 -m almost_twin fetch-sources --network --source cdt_wikipedia
python3 -m almost_twin study check \
  --config configs/study.cdt-haiku-gemini-smoke.yaml \
  --out data/cdt-haiku-gemini-preflight.json
python3 -m almost_twin study prepare \
  --config configs/study.cdt-haiku-gemini-smoke.yaml \
  --out data/studies/cdt-haiku-gemini-smoke
```

`study prepare` is also unbilled. Inspect `preflight.json`, `plan.md`, and
per-cell researcher requests under the prepared study; verify the chosen
endpoint actually belongs to the intended model provider and that both
efforts, parameters and conservative price bounds are supported. Provider tags
are selected automatically from live metadata, not hardcoded into the config.
If preflight fails for an effort or an endpoint, stop and inspect the failure;
do not silently substitute a model or bypass verification. The budgets in this
config are **cumulative project-wide ceilings**, not per-study allowances.

Start with **one Haiku scenario** (the first cell), which does make paid calls:

```sh
python3 -m almost_twin study run \
  --study data/studies/cdt-haiku-gemini-smoke \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 1 --limit-cells 1 --limit-per-cell 1
```

If its transcript, action classification, reasoning availability and provider
metadata look right, finish **all remaining scenarios** (including both Gemini
scenarios) with the same command **minus both `--limit-*` options**. Already
finished samples are skipped on resume. `--jobs 2` runs up to two full scenarios
concurrently *across all cells*. By default, the study runner uses five global
workers (`--jobs 5`) and permits two concurrent scenarios per selected provider
family (`--provider-jobs 2`). These flags can be lowered for cautious pilots.

```sh
python3 -m almost_twin study run \
  --study data/studies/cdt-haiku-gemini-smoke \
  --execute --confirm-billable --approve-variable-prompts --jobs 2
```

Read `summary.md` for the two model rows and `pairs.csv` / `decisions.csv` for
the exact paired outcomes. **Study runs now automatically write** every
sample's `result.md`, `transcript.txt`, and `transcript.md`, and the study-wide
`review_summary.md` / `review_samples.csv`—no separate reporting command needed.
The optional `study report` command regenerates those outputs offline. Keep the
raw responses and route/provenance records: model thinking tokens may be
counted even if the endpoint supplies no readable reasoning text.

## Prepare, inspect, run, resume

Once the configuration passes:

```sh
python3 -m almost_twin study prepare \
  --config configs/study.example.yaml \
  --out data/studies/cross-provider-v1
```

This freezes `specification.yaml`, metadata snapshots, selected endpoints,
source/template/code hashes and a separate batch for **every** cell. Read
`plan.md`, `preflight.json`, and the per-cell batch plans and researcher
messages. Study directories can never be overwritten by preparation. Changing
the settings or sources means creating a new study.

Explicitly approve billing and the dynamic source/template family before
executing. Start by limiting the number of pending *cells* and *samples*:

```sh
python3 -m almost_twin study run \
  --study data/studies/cross-provider-v1 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 2 --limit-cells 1 --limit-per-cell 1
```

Then continue with the same command, without the limits. `--jobs` is the
global maximum number of concurrent **full scenarios across the entire study**
(default 5). The scheduler interleaves model/theory cells and defaults to at
most two active scenarios per selected provider family (`--provider-jobs 2`).
For example, seven different models with mostly different providers now overlap
calls across models without passing any concurrency flags. If 429 errors appear,
lower `--provider-jobs` to 1; raise it beyond 2 only with provider-specific
evidence. Researcher, prisoner, and conditional
judge stages remain sequential within a scenario; a shared judge provider can
still receive overlapping calls from different scenarios. Each batch has its
own lock and resumable states. Completed or failed generation attempts are
**never automatically repeated**. A run interrupted after some model calls
can be resumed if the same code and frozen configuration remain in place.
The project-wide budget ledgers and per-request revalidation still apply.

Generation remains deliberately fail-closed: live endpoints are rechecked;
there is no automatic model/provider fallback. A `max_tokens` limit includes
reasoning tokens where applicable, so check for unexpectedly truncated high
effort calls in CDT-only smoke tests and decide the cap before the main study.

## Results and audit

```sh
python3 -m almost_twin study report --study data/studies/cross-provider-v1
```

This makes **zero model calls** and regenerates the same outputs that a finished
`study run` now writes automatically:

| File | Meaning |
|---|---|
| `summary.md`, `summary.csv`, `summary.json` | Per-condition complete pair counts, cooperation rate and CC/CD/DC/DD frequencies; failure counts, provider-reported costs, elapsed batch execution time and 429 failures |
| `pairs.csv` | One row for every complete-scenario sample, including missing, failed and unjudged samples |
| `decisions.csv` | Two rows per sample, with original intention, disclosure, enacted and final classifications, plus raw run paths |
| `preflight.json`, `study.json`, `specification.yaml` | All chosen conditions, source/config identities, provider selection, estimated cost and provenance |
| `batches/<cell>/` | Unmodified per-cell batch artifacts, exact prompts and raw responses |
| `batches/<cell>/samples/<id>/result.md`, `transcript.txt`, `transcript.md` | Automatically generated readable outcome, full visible responses and any provider-returned reasoning |
| `review_summary.md`, `review_samples.csv` | Offline disposition of resolved nonactions versus genuinely ambiguous trials |

OpenRouter requests ask for `usage.include=true`. Only explicit `usage.cost`
values are included in the displayed provider charges (including judge calls);
older responses or endpoints without a price are counted as **unknown**, not
zero. This is distinct from the preflight estimate and budget reservations.
For operational throughput, `--jobs` controls parallel *full scenarios* across
cells (default 5; allowed 1–16); `--provider-jobs` caps overlapping scenarios
sharing a selected provider family (default 2; allowed 1–16). Scheduling is round-robin across cells,
and a busy provider does not occupy a waiting worker. The summary's aggregate
cell execution time may exceed actual wall-clock duration because cell work
overlaps; `last_run_wall_seconds` records elapsed time for the most recent
invocation. Too many jobs can exceed provider throughput or rate limits;
HTTP 429 failures are recorded, not automatically retried.

The primary descriptive estimand is the mean of the A/B cooperation fraction
for **complete scored pairs**, so `CC=1`, `CD/DC=0.5`, and `DD=0`.
Pending/failed samples are visible, *not* assumed to defect or silently
dropped from status counts. For cells with at least 10 scored pairs, the
descriptive interval bootstraps whole *pairs*, not individual decisions.
Avoid treating this interval as a replacement for a preregistered statistical
analysis or drawing confirmatory conclusions from adaptive sampling.

To regenerate just one batch's human-readable transcripts and any
provider-returned reasoning, the original **offline** reporter still works:

```sh
python3 -m almost_twin.sample_report \
  --batch data/studies/cross-provider-v1/batches/<cell-id>
```

`samples/00000/transcript.md` and `samples/00000/transcript.txt` both include
all visible model responses and readable reasoning **inline**. The Markdown
version additionally links the exact individual text files and raw OpenRouter
JSON. For a terminal, use `less samples/00000/transcript.txt` from the batch
directory. The study summary does not reinterpret or overwrite those original
records. All `data/` remains gitignored and
should be reviewed for source rights and sensitive provider data before
sharing or publication. The code is still labeled **exploratory**; freeze a
separate preregistration of models, source versions, effort settings, planned
N and analysis before a confirmatory research run.

### Clear refusals versus genuinely ambiguous actions

An explicit refusal to participate is **not** the game command `pass` and must
not be counted as cooperation. The current judge schema intentionally labels
procedural refusals `intent=OTHER`, `disclosure=NO`. If it also returns
`needs_human_review=false`, then the outcome is an **unscored, resolved
nonaction**, not a case requiring additional human adjudication. The
judge schema does not distinguish refusals from other clear non-decisions;
consult its saved `reason` and the model transcript for the exact distinction.

The batch runner now distinguishes these terminal statuses:

- `complete`: a valid action for both prisoners, with a scored pair.
- `resolved_nonaction`: at least one confidently classified `OTHER` / `NO`
  response, with no actual ambiguity; the pair is **unscored**.
- `resolved_unscored`: another confidently judged but invalid/unscorable
  action (e.g. a clear attempt to submit evidence without disclosing it).
- `needs_human_review`: an ambiguous disclosure, a judge request for review,
  or inconsistent judge annotations; only these require human attention.

No resolved nonaction or other resolved-unscored pair is counted in cooperation
rates. The code checks the structured judge decisions, not its free-form
explanation, and never overrides the original fictional commitment journal.

Older frozen studies used `needs_human_review` for **every** unscorable pair.
The offline review report can still interpret those records. Both manual
report commands below remain available for legacy data, although current
`study run`/`study report` invoke them automatically. Changing hashed runner
code invalidates live resume of a previously prepared study; start a new
study directory when adopting these generation changes:

```sh
python3 -m almost_twin.sample_report \
  --batch data/studies/cdt-haiku-gemini-smoke/batches/*haiku*
python3 -m almost_twin.review_report \
  --study data/studies/cdt-haiku-gemini-smoke
```

The first command writes per-sample `review_disposition` to derived `result.json`,
an explanation in `result.md`, and readable transcripts. The second writes
**`review_summary.md`, `review_summary.json`, and `review_samples.csv`**,
separating resolved nonactions, other unscored cases, and actual human-review
cases. Both commands are unbilled. Responses, judge records and historical
scores remain unchanged; derived summaries are generated from those sources.

For future instruments, consider a distinct `REFUSAL` judge label and a
separate terminal `refused` status; that is a **new judging protocol** and
requires a new, explicitly versioned study. Do not silently change the judge
prompt or the meaning of old labels mid-study.
