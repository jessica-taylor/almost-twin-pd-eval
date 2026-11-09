# A-FDT Anthropic reasoning-effort follow-up (planned)

This is a fresh exploratory study following
[`dt-four-theories-main-qwen-plow-20261108`](dt-four-theories-main-qwen-plow-20261108-results.md).
It tests whether the **prisoner-stage reasoning effort** changes the action in
the same almost-twin prisoner's dilemma under the Equation (4) A-FDT assignment.
No previous outcomes are carried into the study, and this plan has no results.

## Matrix and controls

- **Models:** `anthropic/claude-sonnet-5.5` and `anthropic/claude-opus-5.5`,
  pinned to OpenRouter's `anthropic` provider endpoint.
- **Theory and game:** `fdt_eq4` (A-FDT); `t4_distinct_leads_001`, with the same
  distinct observations and two prisoner roles as the first main study.
- **Prisoner reasoning effort:** `low`, `medium`, `high` separately for each
  model; **30 independent paired scenarios per condition**. This gives six
  condition cells, 180 researcher essays, and up to 360 prisoner requests
  (plus conditional judge calls).
- **Researcher effort:** held fixed *within* model at the earlier baseline:
  Sonnet `low`, Opus `high`. Researcher prompt/source and essay bounds remain
  those of the first study: target 2,400–3,000 words; hard maximum 5,000 words
  and 64,000 JSON-encoded bytes. Researcher generation ceilings remain
  16,000/32,000 total output tokens for Sonnet/Opus respectively.
- **Prisoner generation ceiling:** **12,000 total output tokens for all three
  efforts**, including hidden reasoning. This avoids the prior low/high
  output-budget difference. The API timeout remains 900 seconds.
- **Judge:** `openai/gpt-6.1-sol` at low effort, only when classification needs
  it; keep the original action/failed-sample scoring rules.

Each scenario independently writes a **new essay** that is reused within its
A/B pair. The six cells do **not** share identical essays across prisoner-effort
conditions. Since researcher settings are held constant within each model,
the researcher-essay distributions are intended to be comparable, but essay
sampling adds noise and the experiment is *not* a matched-essay intervention.
The design should not be described as separately testing how researcher
reasoning effort changes behavior, nor as proving a causal effect of thinking
tokens; the independent variable is the API's requested prisoner effort.

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
*within Opus* across the three prisoner effort settings, counting whole A/B
pairs as the unit. Report failure counts, actual reasoning-token distributions,
and costs separately. Qualitatively examine whether additional effort makes
the model more likely to distinguish observation-indexed A-FDT nodes from
shared-policy or noisy-computation counterfactuals. Differences may reflect
the essay sample and provider sampling as well as the requested effort.

A later, stronger follow-up could **reuse the same frozen researcher essay**
across effort arms to measure within-essay effects directly. That requires
new harness support and is not assumed by this configuration.
