# Repeated full-scenario batches (exploratory)

This workflow automates the *existing* mainline design, one independent sample at a time:

1. Send the human-written CDT/EDT/FDT source to a researcher model, obtaining a fresh mathematical essay about the assigned theory. The researcher **is not told about almost-twin PD**.
2. Send that *same frozen essay* to two separate prisoner calls. Each has its own text-adventure observations and evidence, and neither sees the other's decision. The default `t4_distinct_leads_001` gives them different evidence and outgoing letters. The two calls share model, weights/endpoint, assigned theory, essay and reasoning-effort setting, subject to the usual limits on independently verifying deployed weights.
3. Use the existing simple action classifier. Only responses flagged as ambiguous are sent to a separate judge, by default `openai/gpt-6.1-sol`. Judge labels do not rewrite the original responses or irreversible commitment journal.
4. Save raw request/response artifacts, one machine-readable result per sample, and a flat CSV for analysis.

All samples are labeled **exploratory**, not preregistered data. No change to decision-theory definitions, prompts, game rules or action classification is made here. A sample is a full researcher/paired-prisoner trial, **not** just one prisoner's answer. Parallelism runs *different complete samples* concurrently; within each sample the essay must finish before the pair and any judging.

## CDT / Nano walkthrough

From the repository root, with Python 3.11+ and PyYAML installed:

```sh
python3 -m almost_twin fetch-sources --network --source cdt_wikipedia
```

Only the first preparation needs a fetched and verified source. The following **prepares** five independent samples, makes unbilled model-capability checks, chooses a pinned endpoint for Nano and the judge, computes conservative cost estimates, and writes all initial researcher prompts. It makes **zero paid model calls**:

Provider tags are normally selected automatically: prefer the model author's base endpoint (`openai` for OpenAI, `anthropic` for Anthropic), then author variants, then other validated endpoints. The chosen provider is frozen for the batch; there is no silent fallback or substitution during execution. Recognized prompt-length pricing tiers are conservatively priced using the highest applicable advertised rates, so a small judge request may have a deliberately high cost estimate.

```sh
python3 -m almost_twin batch prepare \
  --assignment cdt_wikipedia --model openai/gpt-5-nano \
  --researcher-effort low --prisoner-effort low \
  --scenario t4_distinct_leads_001 --count 5 \
  --max-calls 30 --max-usd 5.00 \
  --judge-max-calls 20 --judge-max-usd 5.00 \
  --out data/batches/cdt-nano-five
```

Read `data/batches/cdt-nano-five/plan.md`, `plan.json`, the source, and the existing prompt templates. In particular, inspect `samples/00000/researcher/messages_0.md`. The researcher essay and exact subsequent prisoner/judge prompts *cannot* be manually inspected yet: they are generated dynamically. Make sure the projected upper cost and the scope of this approval are acceptable.

To authorize the batch and process the first full sample as a billable smoke test:

```sh
python3 -m almost_twin batch run \
  --batch data/batches/cdt-nano-five \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 1 --limit 1
```

Then inspect the saved sample and raw API records. To finish the other four samples using two concurrent workers:

```sh
python3 -m almost_twin batch run \
  --batch data/batches/cdt-nano-five \
  --execute --confirm-billable --approve-variable-prompts \
  --jobs 2
```

You can also run all five from the start with `--jobs 2`. To regenerate summaries without any model calls:

```sh
python3 -m almost_twin batch status --batch data/batches/cdt-nano-five
```

The `--count` is fixed when preparing a batch; create a new `--out` directory for additional samples. `--limit` counts pending samples attempted in that invocation, not API calls. Already completed and failed samples are not automatically called again. Different batches use the same *cumulative* project budgets and ledgers; choose `--max-calls` and `--max-usd` with prior pilot/batch reservations in mind.

The normal **`batch run` now writes these per-sample readable reports automatically**
when it finishes, including any returned reasoning. To regenerate them offline
for an older batch or after subsequent reporting-code changes, use:

```sh
python3 -m almost_twin.sample_report --batch data/batches/cdt-nano-five
```

This creates `samples/00000/result.md` and `samples/00000/result.json`, and equivalent files in every other sample. It prints a concise summary for the first 20 samples. Each Markdown report spells out **Cooperate (WITHHOLD)** versus **Defect (SUBMIT)** for both prisoners, distinguishes parser-enacted actions from judge-adjusted classifications, indicates pending/failed states and links to both raw responses. A complete scored outcome also displays each prisoner's years and utility. Each report also shows provider-reported charges and explicitly identifies requests for which the provider supplied no cost.

Each sample additionally gets **`transcript.md` and terminal-friendly `transcript.txt`**, a `transcript_index.json`, and `transcript/` files containing the **complete visible responses** for the researcher, both prisoners and any judge calls. Both full transcripts show the returned response and readable reasoning content **inline**, with outcome and original-versus-final classifications at the top; they are not just link indexes. To read in a shell, use `less samples/00000/transcript.txt` (from the relevant batch root). When `choices[0].message.reasoning` (or its `reasoning_content` alias) is returned, the reporter writes the exact plaintext to a `*_reasoning.txt` file. When `reasoning_details` is returned, it preserves the complete array as `*_reasoning_details.json` and makes a readable text view of supplied `reasoning.text` and `reasoning.summary` blocks. Encrypted blocks remain in the JSON and are **not** represented as readable thinking. If nothing readable was returned, the transcript says so; reported `usage.*.reasoning_tokens` is shown separately and does not imply the actual trace was available. Every transcript links to the complete original `call_*/response.raw` JSON, which is the authoritative record. OpenRouter's current reasoning documentation states that thinking material is included when the model/provider exposes it and the request does not exclude it; our existing calls use `reasoning.effort`, not `reasoning.exclude`, so no generation changes are needed. See https://openrouter.ai/docs/guides/best-practices/reasoning-tokens.

These are derived files, regenerable without any network or generation requests. The reporter runs separately so the code hashes pinned by previously prepared batches are not invalidated by reporting enhancements. It cannot recover internal reasoning that the provider never sent in the original response.

If the judge model is unavailable on your OpenRouter account or endpoint capabilities fail validation, specify `--judge-model <available-model>` and/or `--judge-provider-tag <endpoint>` at **preparation**, or `--no-judge` to leave ambiguous samples for later manual review. This is a visible change to the judgment condition, so preserve it in the analysis. Metadata can be pinned offline using `--capabilities` and `--judge-capabilities`; live calls still refresh metadata and revalidate. The `--allow-unverified-effort` options record explicit assumptions rather than silently weakening capability checks.

## Output structure and audit trail

Each batch directory contains:

| Artifact | What it records |
|---|---|
| `batch.json`, `batch.sha256`, `plan.json`, `plan.md` | Batch ID, conditions, sample IDs, source/template/running-code hashes, selected endpoints, possible costs, and approval scope |
| `samples/00000/`, `samples/00001/`, ... | One independently prepared pilot per sample, including `pilot.json`, stage prompts, `state.json`, `events.jsonl` and links to actual run directories |
| `events.jsonl` | Append-only batch preparation, authorization, sample processing and finish records |
| `results.jsonl` | One JSON record per sample, ordered by sample index; contains status, model/efforts, essay hash, raw/derived action labels, utilities, review flags and artifact paths |
| `results.csv` | Flat audit-friendly row per sample, with separate A/B intent, disclosure, enacted/adjudicated/final action and utility columns |
| `summary.json` | Sample counts by status and locations of the result files |
| `samples/00000/result.md`, `result.json` | Human-readable decisions and the full sample record, generated on demand without rerunning the experiment |
| `samples/00000/transcript.md`, `transcript.txt`, `transcript/`, `transcript_index.json` | Self-contained Markdown/plain-text responses and returned reasoning, separate verbatim files, usage metadata, and links to the authoritative raw API JSON |

The batch indices are *derived* and can be regenerated by `batch status`; raw model artifacts and journals are not regenerated or overwritten. A sample's `state.json` gives `researcher_run` and `prisoner_run` paths under `data/exploratory/runs/<uuid>/`. Those run folders preserve exact model-visible messages (`messages_*.json` and Markdown), serialized request JSON, raw API responses, extracted outputs, model/provider information, usage, output hashes, essay, outcomes, and errors. Conditional judge calls are saved separately under `data/judge_runs/<uuid>/` and referenced by the sample record. These directories, the data ledgers, and full source text are gitignored. **Do not commit credentials or private responses.**

Result statuses:

- `prepared`: no essay generated yet.
- `researcher_complete`: essay exists; prisoner pair not yet done.
- `pending_judge`: prisoner pair completed but at least one action needs adjudication. Also the final status if `--no-judge` was chosen.
- `complete`: both decisions have an actionable final classification, using a judge if necessary.
- `resolved_nonaction`: the judge confidently classified one or more responses as `OTHER` / disclosure `NO` (including explicit refusals); the pair is terminal but **unscored**, never counted as cooperation.
- `resolved_unscored`: the judge confidently classified intent and disclosure, but at least one attempted action did not produce a valid scored game action; also terminal and excluded from cooperation rates.
- `needs_human_review`: a genuine unresolved ambiguity, uncertain disclosure, or inconsistent judge record remains. Missing a score **by itself** does not imply human review.
- `failed`: a generation or judge attempt failed, with preserved raw artifacts and an explanatory error. No automatic retry.

`intents` and `disclosures` are separate from `enacted_actions`; the judge may infer an attempted action without proving that the simulated evidence was successfully disclosed. `final_actions` and `final_score` are *derived analysis labels* (possibly adjudicated), while `enacted_actions` and the commitments journal record what the primary parser accepted. Analyze these separately rather than silently converting an ambiguous output into a successful action.

## Approval, cost and interruption semantics

The single-sample `pilot` interface still requires **manual approval of each exact prepared request**. That cannot literally be done for thousands of dynamic prisoner prompts, since the essays do not yet exist. Batch mode therefore introduces an **explicit, distinct authorization**: `--approve-variable-prompts` approves the reviewed source/template family, fixed scenario/settings, and dynamically filled essay/observations/judge inputs. The approval and hashes of *each actual generated request* are saved, but the logs **do not claim those requests were individually inspected**. Both billing flags remain mandatory.

The initial plan bounds three model calls per sample (one essay and two prisoners) using conservative estimates based on the actual template overhead plus an enforced cap of `8 * researcher_max_tokens` JSON-encoded essay bytes, subject to endpoint context limits. This replaces the extremely loose assumption that each essay fills the entire model context. An oversized essay is retained in raw generation files, but not passed to prisoners; new actual requests are still revalidated and reserved. Judging adds zero, one or two requests per sample, and uses its own persistent estimated-cost and call-count caps. Provider-reported costs are tracked separately; a missing amount is unknown, not free. Estimates are not a hard guarantee of OpenRouter charges; use a separate OpenRouter key credit limit when a hard real-money ceiling matters. Unknown/contradictory endpoint, reasoning and pricing metadata block execution. All requests have no automatic API retries.

The runner writes a separate pilot and locks each sample; the batch run also takes an exclusive lock. You may interrupt an in-progress batch and reissue the same `batch run` command: completed samples are skipped, and failed or uncertain attempts remain visible and are not silently repeated. The script regenerates `results.jsonl`/`results.csv` after each finished sample. It does not run the two prisoner calls in parallel *within* a sample; they are independent request contexts, but sent sequentially to preserve the existing two-call commitment behavior. Samples may be concurrent via `--jobs` (1–16).

Execution is pinned to the code hashes captured during preparation; if implementation changes, create a new batch for subsequent billable generation. Non-billable `batch status` remains usable after code changes. The batch is attached to its original repository root for trustworthy artifact paths. Its CSV/JSONL and raw records can be read independently later, including after you archive the folder.

The offline test suite uses mocked API responses to check fresh essays, independent pairs, conditional judging, `--limit` resume, concurrency, budget reservations, approval guards and partial failures. It makes no paid calls:

```sh
python3 -m unittest discover -s tests -v
```
