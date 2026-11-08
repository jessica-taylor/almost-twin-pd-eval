# Eight-model CDT frontier pre-study (November 2026)

Config: [`study.cdt-frontier-provider-prestudy-20261108.yaml`](../configs/study.cdt-frontier-provider-prestudy-20261108.yaml).

This is an **exploratory provider/behavior check** before a larger, separately
frozen CDT study. Its purpose is to find unsupported reasoning-effort settings,
bad endpoint routing, truncation, essay-length problems, refusals, and broken
scoring. Two paired scenarios per model are **not** a statistically useful
estimate of cooperation rates.

## Fixed design

- `cdt_wikipedia` only; the human-written source, researcher prompt and
  prisoner prompts remain unchanged during this study.
- `t4_distinct_leads_001`, with fixed but distinct A/B observations. Each
  independent paired scenario gets one newly generated essay shared by its
  two prisoners (and conditional judge calls).
- **Eight models × two pairs = 16 paired scenarios**; up to 48 baseline model
  calls and 32 conditional judge calls. There is one effort combination per
  model, not a full low/high factorial design.

| Model | Researcher / prisoner effort | Reason for inclusion |
| --- | --- | --- |
| `anthropic/claude-sonnet-5.5` | high / high | Anthropic mid-tier frontier model |
| `anthropic/claude-opus-5.5` | high / high | Anthropic flagship; test expensive high reasoning |
| `openai/gpt-6.1-terra` | high / high | Current Terra variant |
| `openai/gpt-6.1-sol` | high / high | Current Sol variant |
| `google/gemini-3.8-flash` | low / low | Fast Flash baseline; earlier essay-length failure |
| `google/gemini-4-argon` | high / high | Google's flagship reasoning model |
| `z-ai/glm-5.3` | high / high | Reasoning-capable open-weight family |
| `qwen/qwen3.8-max-prime` | high / high | Recent high-throughput Qwen Max variant |

The model IDs are intended identities, **not proof of endpoint capability**.
`study check` must verify live metadata, high-effort support, 32K/12K token
allowances, prices and providers. In particular, do not silently downgrade
effort or fall back to an unrelated model if an endpoint fails its check.
Provider tags are deliberately not hardcoded: `study prepare` freezes the
verified selected provider/route per cell, which must be reviewed. In
particular, GLM's many possible hosts can differ in quantization/behavior.

## Essay limits and generation budgets

The prompt requests **1,200–1,500 words**, including references; short essays
remain usable. The runner accepts a completed essay up to **2,500 visible
words** and **32,000 JSON-encoded bytes**. This would have accepted the prior
1,852-, 1,853- and 2,091-word failed essays (assuming their byte lengths
fit), and gives meaningful headroom without encouraging 5,000-word essays.
The researcher prompt now explicitly states the target. A model that ignores
it and exceeds the hard ceiling still produces a logged failed attempt; the
runner does not truncate its essay or silently retry it.

Separately, `max_tokens` limits total generated tokens **including hidden
reasoning**: high effort gets **32K** for the researcher and **12K** for each
prisoner; Flash's low effort gets **16K** and **6K** respectively. These values
do not change the essay bounds or the prisoner input projection. Since high
effort can be slow, HTTP socket timeout is **900 seconds** per call. The judge
remains `openai/gpt-6.1-sol` at low effort, with 2,400 output tokens; this is
the existing judge protocol, not a change in the action classification.

Project-wide (not per-study) protective budget ceilings are 500 researcher/
prisoner requests and $300, with separate judge ceilings of 300 calls and $50.
They cover previous reservations as well. Check both the heuristic expected
cost and conservative reservation estimate in preflight; **a ceiling is not a
prediction that the run will cost that amount**.

## Check and prepare: no paid model calls

After pulling the config into the repository, run from its root:

```bash
python3 -m almost_twin fetch-sources --network --source cdt_wikipedia
python3 -m almost_twin study check \
  --config configs/study.cdt-frontier-provider-prestudy-20261108.yaml \
  --out data/cdt-frontier-provider-prestudy-20261108-preflight.json
python3 -m almost_twin study prepare \
  --config configs/study.cdt-frontier-provider-prestudy-20261108.yaml \
  --out data/studies/cdt-frontier-provider-prestudy-20261108
```

Stop if any cell fails preflight; resolve the specific model, effort,
endpoint, token-cap or budget issue **before preparing**, and create a new
study directory if changing the frozen design. Inspect `preflight.json`,
`plan.md` and prepared researcher requests. Check that the matrix contains
exactly eight cells and 16 total planned pairs, and that high-effort settings
are actually supported on the selected endpoints.

## Billable execution: inspect one pair per model first

```bash
python3 -m almost_twin study run \
  --study data/studies/cdt-frontier-provider-prestudy-20261108 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 5 --provider-jobs 2 --limit-per-cell 1
```

This runs at most one pair for each of the eight model cells. Up to five
whole scenarios execute concurrently (at most two per selected provider
family). Their stages are sequential within each scenario; the shared judge
provider may see overlapping calls. Previous parallel pilots had no HTTP
429 failures, but this does not guarantee the new hosts will behave the same.
If 429s occur, reduce `--provider-jobs` and/or `--jobs`; failed attempts are
recorded rather than automatically repeated. The progress log reports stages
and elapsed time without printing private prompts or credentials.

Review `summary.md`, `failures.csv`, `review_summary.md` and the readable
`batches/*/samples/*/transcript.txt` files. In particular, check:

1. Exact model ID, selected endpoint/provider tag, effort settings, output
   limits, finish reason and provider-reported costs.
2. Researcher completion and essay lengths; distinguish an actual truncated
   response (`output_token_limit`) from an overlong completed essay
   (`essay_size_limit`).
3. Both prisoners received the **same** verbatim essay and distinct private
   lead, generated their own responses, and were scored as intended.
4. Refusals and resolved nonactions remain unscored, not counted as defects
   or cooperation; judge requests and review statuses make sense.
5. HTTP failures, transport timeouts, provider-specific anomalies and 429s.

After investigating failures, finish the second prepared sample per model:

```bash
python3 -m almost_twin study run \
  --study data/studies/cdt-frontier-provider-prestudy-20261108 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 5 --provider-jobs 2
```

Terminal failed attempts will **not** be retried, and already finished pairs
are skipped. If a cell needs a changed limit/provider/effort, log that failure
and prepare a separate, explicitly named follow-up rather than altering its
frozen batch. Preserve the original study and raw provider outputs.

The next substantive study should freeze its final model/provider selection,
reasoning levels, sample size and estimands after this compatibility check.
Do not read an exploratory `n=2` cooperation rate as evidence of how a model
behaves in general. See [`study_workflow.md`](study_workflow.md) for status and
resume semantics.
