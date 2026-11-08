# First substantive almost-twin PD study: four conditions, eight models

Specification: [`configs/study.dt-four-theories-main-20261108.yaml`](../configs/study.dt-four-theories-main-20261108.yaml).

This is the first larger, **still exploratory**, study after the November 8
CDT-only provider pre-study (15/16 pairs completed, all 15 were DD, no HTTP
429s; one Gemini 4 Argon researcher essay had 2,661 words against a 2,500-word
hard cap). Preserve that earlier study unchanged. Do not mix its results or
failures into this study.

## Frozen design

- **Four assignments:** `cdt_wikipedia`, `edt_wikipedia`, `fdt_eq4`, and
  `fdt_policy`. The last two are **two formulations of FDT**, not two
  completely unrelated decision theories.
- **Eight models:** four natural strong/weak pairs, with the strong model at
  high/high reasoning and the weak/cheap model at low/low reasoning for both
  essay generation and prisoner responses.
- **Twenty independent paired scenarios per cell:** 4 × 8 × 20 = **640 pairs**.
  Each pair has a fresh researcher essay and two independent prisoner calls
  conditional on that shared essay, followed by zero to two judge calls.
  This entails **up to 1,920 baseline model calls** and **1,280 conditional
  judge calls**.
- **One fixed scenario:** `t4_distinct_leads_001`. Prisoners A and B receive
  distinct observations; the researcher essay is passed verbatim to both.
  Thus this study tests repeated generations for *this scenario*, not
  generalization across different game structures.

| Family | Weaker/cheaper model (low / low) | Stronger model (high / high) |
| --- | --- | --- |
| Anthropic | `anthropic/claude-sonnet-5.5` | `anthropic/claude-opus-5.5` |
| OpenAI | `openai/gpt-6.1-terra` | `openai/gpt-6.1-sol` |
| Google | `google/gemini-3.8-flash` | `google/gemini-4-argon` |
| Chinese families | `z-ai/glm-5.3-flash` | `qwen/qwen3.8-max-prime` |

The Chinese weak/strong pairing preserves coverage of both Z.ai and Qwen,
but substitutes **GLM-5.3 Flash** for the earlier strong GLM-5.3. This is a
new serving configuration and must pass preflight and initial transcript
inspection; the previous successful GLM-5.3 requests do not validate Flash.
Qwen Max Prime remains from the completed high-reasoning pre-study.

Reasoning settings are intentionally **not controlled across tiers**. This
design compares two model-plus-reasoning *deployment policies* per family,
not an isolated causal effect of changing model weights. The two selected
Chinese models are also from different organizations. For substantive
comparisons, favor *within-model, between-theory* descriptive differences.

## Doubled essay allowance

The templated researcher prompt now requests **2,400–3,000 visible words**
(versus 1,200–1,500). The independent hard limits are doubled to **5,000
words** and **64,000 serialized JSON bytes** (versus 2,500 and 32,000).
Earlier 2,661-word Gemini Argon output would be accepted under the new word
cap if it fits the 64K byte ceiling. If a model exceeds either hard bound,
record `essay_size_limit`; do not truncate, rewrite or silently retry.

Generation ceilings remain as in the pre-study: researcher **16K low / 32K
high output tokens** and prisoner **6K low / 12K high tokens**. These include
reasoning tokens; the essay bounds do not. The timeout remains 900 seconds
per HTTP socket operation. Raising the essay target might increase output
token use, particularly with high-reasoning models; inspect actual usage and
`finish_reason` during the first-sample audit before committing to 640.

Judge policy remains low-effort `openai/gpt-6.1-sol` with 2,400 output tokens.
The study uses the four existing, unchanged source definitions; it does not
change prisoner cases, judge labels, scoring, unscored/refusal semantics or
automatic retry policy.

## Costs, power and interpretation

Linear extrapolation of the CDT pre-study's **$1.888669455 for 16 pairs**
to 640 pairs is about **$75.55**. This is only a baseline: doubling the
requested essay, reducing effort on four models, using a cheaper Chinese
model, and varying source articles across theories all change token use.
Actual cost and conservative reservations must be read from `study check`.
With 640 pairs, total wall-clock time may be multiple hours despite
parallel execution; an aggregate `recorded cell execution` time is *not*
wall-clock time.

The config sets cumulative protective ceilings of **3,000 baseline calls /
$500** and **2,000 judge calls / $100**, including existing budget ledger
reservations. These are upper authorization checks, not a claim that this
experiment will spend $600; no paid calls run at check or prepare time.

Primary descriptive outputs are per-cell cooperation fraction (average of
prisoner A/B in each complete pair), CC/CD/DC/DD frequencies, missingness,
failure categories and model/provider costs. Whole pairs, not individual
prisoner responses, are resampled for any intervals. At n=20 per cell,
avoid overconfident cross-model rankings and record all failures/unscored
trials; do not reclassify a refusal as a defection. Freeze 20 planned pairs
in advance rather than increasing N selectively after seeing results.

## Check and prepare (no billable generations)

After merging the config and pulling the repository, from its root:

```bash
python3 -m almost_twin fetch-sources --network \
  --source cdt_wikipedia --source edt_wikipedia --source fdt
python3 -m almost_twin study check \
  --config configs/study.dt-four-theories-main-20261108.yaml \
  --out data/dt-four-theories-main-20261108-preflight.json
python3 -m almost_twin study prepare \
  --config configs/study.dt-four-theories-main-20261108.yaml \
  --out data/studies/dt-four-theories-main-20261108
```

Check that the live metadata validates exactly **32 model × theory cells**, all
20 samples per cell, all selected reasoning levels, context/output limits,
the **new** GLM Flash endpoint, and the expected/conservative cost. Stop if
any cell fails. Inspect `preflight.json` and `plan.md`, including selected
provider tags, before freezing. Do not silently select another model, an
unverified effort or a different source. Study preparation creates a fresh
directory; never overwrite the finished pre-study.

## Billable first wave and full execution

Start with **one scenario per cell** (32 paired scenarios):

```bash
python3 -m almost_twin study run \
  --study data/studies/dt-four-theories-main-20261108 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 5 --provider-jobs 2 --limit-per-cell 1
```

Review the resulting `summary.md`, `failures.csv`, `review_summary.md`,
`summary.json`, per-cell transcripts and exact route/reasoning-token metadata.
Focus on length/byte-limit violations, truncated high-reasoning outputs,
new GLM Flash behavior, judge decisions, HTTP errors and rate limits. Pause
and investigate if unexpected failures occur. Completed or failed scenarios
are terminal; reruns do not silently replace them.

If all looks sound, finish all remaining prepared pairs:

```bash
python3 -m almost_twin study run \
  --study data/studies/dt-four-theories-main-20261108 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 5 --provider-jobs 2
```

The runner's default concurrency is five whole scenarios and two scenarios
per provider family. If 429s appear, lower concurrency (there is no automatic
retry). If the first wave exposes a needed limit or provider change, log
the failures and freeze a **new** follow-up study rather than altering this
prepared specification. The automatically generated reports preserve the
pair-level data and recorded charges. Refer to [`study_workflow.md`](study_workflow.md)
for execution and reporting semantics.
