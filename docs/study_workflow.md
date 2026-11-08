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
ceiling. The default cost projection uses a **new enforced essay-size bound**:
the researcher's output is limited to at most `8 * researcher_max_tokens`
JSON-encoded essay bytes, and the prisoner projection adds that to the exact
scenario/template overhead. The large former full-context estimate is still
shown separately for comparison. The factor of eight is deliberately generous,
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
finished samples are skipped on resume. Using `--jobs 2` runs two scenarios
concurrently *within each cell*; cells still run sequentially.

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
maximum concurrent **full scenarios within one condition cell**; condition
cells are processed sequentially. Each batch has its own lock and resumable
states. Completed or failed generation attempts are **never automatically
repeated**. A run interrupted after some model calls can be resumed if the
same code and frozen configuration remain in place. The project-wide budget
ledgers and per-request revalidation still apply.

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
For operational throughput, `--jobs` controls parallel *full scenarios* within
one cell (allowed 1–16); stages inside each scenario and the cells themselves
remain sequential. Too many jobs can exceed provider throughput or rate limits;
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
