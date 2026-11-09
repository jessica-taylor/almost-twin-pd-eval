# A-FDT Anthropic reasoning-effort follow-up (planned)

This is a fresh exploratory study following
[`dt-four-theories-main-qwen-plow-20261108`](dt-four-theories-main-qwen-plow-20261108-results.md).
It tests whether **researcher and prisoner reasoning effort, varied together**,
changes the action in the same almost-twin prisoner's dilemma under the
Equation (4) A-FDT assignment.
No previous outcomes are carried into the study, and this plan has no results.

## Matrix and controls

- **Models:** `anthropic/claude-sonnet-5.5` and `anthropic/claude-opus-5.5`,
  pinned to OpenRouter's `anthropic` provider endpoint.
- **Theory and game:** `fdt_eq4` (A-FDT); `t4_distinct_leads_001`, with the same
  distinct observations and two prisoner roles as the first main study.
- **Researcher/prisoner reasoning efforts:** the three matched pairs
  **`low/low`, `medium/medium`, `high/high`** for each model; **30 independent
  prisoner pairs per condition**. This gives six condition cells, 180 new
  researcher essays and up to 360 prisoner calls (plus conditional judges).
  The `effort_combinations: paired` setting zips the two lists rather than
  taking their Cartesian product; omitting it would create **18** cells.
- **Essay prompt and bounds:** unchanged from the first study: requested
  2,400–3,000 words, hard maximum 5,000 words and 64,000 JSON-encoded bytes.
  **Researcher total output allowance is 32,000 tokens at every effort**.
- **Prisoner total output allowance:** **12,000 tokens at every effort**,
  including hidden reasoning. Both allowances are held fixed to avoid
  confounding changes in requested effort with different output-token caps.
  API timeout remains 900 seconds.
- **Judge:** `openai/gpt-6.1-sol` at low effort, only when classification needs
  it; keep the original action/failed-sample scoring rules.

Each scenario independently writes a **new essay** that is reused within its
A/B pair. The six cells do **not** share essays across effort conditions.
Researcher effort changes the essay distribution, and prisoner effort may
change how it is applied. The independent variable is the **joint requested
effort level of the full researcher-to-prisoner pipeline**. This design cannot
attribute a resulting action difference specifically to the essay or to
prisoner deliberation. It also does not equate an API effort setting with a
fixed amount of computation or observed reasoning-token usage.

## Checking and preparing (no paid generations)

From the repository root:

```sh
python3 -m almost_twin study check \
  --config configs/study.afdt-anthropic-effort-sweep-20261108.yaml \
  --out data/afdt-anthropic-effort-sweep-20261108-preflight.json

python3 -m almost_twin study prepare \
  --config configs/study.afdt-anthropic-effort-sweep-20261108.yaml \
  --out data/studies/afdt-anthropic-effort-sweep-20261108
```

The preflight verifies live OpenRouter metadata for all six exact
model/effort/provider combinations, without generation calls. If `medium`
effort is missing or rejected on the selected endpoint, investigate it; do not
silently change models or bypass validation. **Project budgets are cumulative
reservations**; the config carries forward the existing $1,300 and 3,000-call
ceilings. If the conservative preflight estimate exceeds them, explicitly
review the requested increase before proceeding. Preparation creates a frozen
new study directory and must not overwrite the first study.

## Paid pilot, then continuation

First attempt **one scenario in each of the six cells**, with the existing
provider-family concurrency limiter permitting three Anthropic scenarios at
once:

```sh
python3 -m almost_twin study run \
  --study data/studies/afdt-anthropic-effort-sweep-20261108 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 6 --provider-jobs 3 --limit-per-cell 1
```

Review actual costs, output/reasoning tokens, essay-limit failures, parser
classifications, refusals, and HTTP 429 failures before continuing. To process
remaining prepared scenarios, remove `--limit-per-cell 1`:

```sh
python3 -m almost_twin study run \
  --study data/studies/afdt-anthropic-effort-sweep-20261108 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 6 --provider-jobs 3
```

Both models use the **same Anthropic provider family**, so the default
`--provider-jobs 2` would limit the whole experiment to two concurrent paired
scenarios despite `--jobs 6`. This study's recommended `--provider-jobs 3`
raises that ceiling without changing code or global defaults. If the pilot
shows headroom and no rate-limit errors, `--provider-jobs 4` is a reasonable
optional next step; it is not a guarantee against provider token-per-minute
limits. Unlike a request-rate throttle, `--provider-jobs` bounds concurrent
full scenarios, each with sequential researcher/prisoner stages. A request to
the judge provider occurs only if needed.

Retain failures without retry or recoding. Use
`python3 -m almost_twin study report --study
data/studies/afdt-anthropic-effort-sweep-20261108` to regenerate offline
summary files.

## Analysis focus

Compare cooperation rates and CC/CD/DC/DD counts *within Sonnet* and
*within Opus* across the three joint effort settings, counting whole A/B
pairs as the unit. Report failure counts, actual reasoning-token distributions,
and costs separately **for both researcher and prisoner stages**. Qualitatively
examine whether additional effort changes how the generated essays explain
observation-indexed A-FDT nodes, and how the prisoner applies those essays.
Differences are effects of the combined configuration, and cannot identify
the stage responsible without an additional study.

A later follow-up could **reuse the same frozen researcher essay** across
prisoner effort arms to isolate prisoner-stage effects; separately varying
researcher effort while fixing the prisoner model would isolate essay changes.
Neither factorial design is assumed by this matched-effort sweep.
