# Qwen low-prisoner-effort revision of the first main study

Study config: [`study.dt-four-theories-main-qwen-plow-20261108.yaml`](../configs/study.dt-four-theories-main-qwen-plow-20261108.yaml).

## Why a new study?

The initial 32-pair first wave of `dt-four-theories-main-20261108` had two
Qwen3.8 Max Prime prisoner-B calls stop at the full 12,000 output-token limit,
using all 12,000 tokens on reasoning and producing no decision (A-FDT and
P-FDT). The other Qwen A/B responses often used thousands of thinking
tokens. Alibaba documents that for Qwen3.8 Max, OpenAI-style `high` effort
maps to its `xhigh` setting (thinking budget 262,144), whereas `low` maps to
4,096 and `medium` to 16,384. Max Prime is sold as having configurable
reasoning like Qwen3.8 Max, but **low-effort behavior on Prime still needs a
billable check**. Sources:

- [Alibaba's OpenAI-compatible chat documentation](https://www.alibabacloud.com/help/en/model-studio/qwen-api-via-openai-chat-completions)
- [OpenRouter Qwen3.8 Max Prime model page](https://openrouter.ai/qwen/qwen3.8-max-prime)

Only the Qwen model's **prisoner** effort changes from `high` to `low`.
Its researcher effort stays `high`; all other model settings, four theory
assignments (CDT, EDT, FDT Equation 4, FDT policy), essay limits, source
definitions, scenario, judge policy and scoring are unchanged. At low effort,
Qwen uses the existing low prisoner total-generation ceiling of **6K** tokens,
not 12K. The documented 4K thinking budget should leave approximately 2K
tokens for an answer, assuming the endpoint honors it; inspect actual usage.

The original study directory, failed attempts and first-wave results are
immutable. Do **not** alter `study.json`, `specification.yaml`, pinned batch
settings or sample status files, and do **not** count original high/high Qwen
trials as low-effort outcomes. This clean revision repeats the first wave;
the approximately $7 already spent on the original wave remains pilot data.
This is simpler than running 28 original non-Qwen batches separately and
combining their output with a separately frozen Qwen-low study.

## Check, prepare and validate before paying

From the repository root, after merging the new config:

```bash
python3 -m almost_twin study check \
  --config configs/study.dt-four-theories-main-qwen-plow-20261108.yaml \
  --out data/dt-four-theories-main-qwen-plow-preflight.json
python3 -m almost_twin study prepare \
  --config configs/study.dt-four-theories-main-qwen-plow-20261108.yaml \
  --out data/studies/dt-four-theories-main-qwen-plow-20261108
```

Both commands perform **no paid model-generation calls**. Verify all 32
cells pass and the Qwen selection is `researcher=high, prisoner=low` on the
intended Alibaba endpoint. Check the project-wide budget: this candidate
config uses a **$1,300 main-call ceiling**, slightly above the previous
Option-A threshold to allow for the newly added first-wave reservations; its
exact adequacy still depends on the current ledger.
It is a spending cap, not an estimate of actual charges. If the new preflight
reports insufficient budget, inspect the ledger and request an explicit
ceiling decision; do not delete or rewrite reservations to force a pass.

For the first billable wave only (one pair per model/theory cell):

```bash
python3 -m almost_twin study run \
  --study data/studies/dt-four-theories-main-qwen-plow-20261108 \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 5 --provider-jobs 2 --limit-per-cell 1
```

Check Qwen A-FDT and P-FDT especially: both prisoners must return nonempty
responses, `finish_reason` must not be `length`, and output token usage should
be comfortably below the low effort 6K allowance. Review costs, refusals,
judge records and any provider errors across all 32 cells before resuming.
For the remaining 19 scenarios per cell, rerun the same command without
`--limit-per-cell 1` after reviewing and accepting the initial results.

The original study may still be reported offline. To avoid analyzing
different effort conditions as one, treat the two study versions as distinct
experiments and keep all historical failures visible in the appendix/audit.
