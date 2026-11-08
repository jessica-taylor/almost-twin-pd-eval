# Almost-Twin Decision Theory Eval — Sprint 01

An auditable, offline-first scaffold for **human article → researcher essay → two independent simulated prisoner decisions**. Mainline prisoners receive the same frozen essay, never the original article. No models or efforts have been selected, and no paid experiment has been run.

The authoritative broad design is [docs/design_v03.md](docs/design_v03.md); [CODEX_TASK.md](CODEX_TASK.md) is the original Sprint 01 handoff. The current prisoner interface is a **naturalistic, one-turn text adventure**, further refined in the [distinct-evidence and adjudication protocol](docs/adjudication_protocol.md). The default early-test scenario has different evidence and outgoing letters for the two prisoners. Prompts are not approved or frozen instruments yet.

## Try it offline

Use Python 3.11+ and PyYAML 6.x. From the repository root:

```sh
python3 -m almost_twin render-prompts --demo
python3 -m unittest discover -s tests -v
```

These require no credentials and make no network requests. The demo uses an **invented source and an explicitly synthetic essay fixture**, not a researcher result. It writes readable Markdown, exact message-array JSON, message/template hashes, and precise diffs under `data/rendered_prompts/demo/fdt_eq4/`. Markdown exports have an HTML comment identifying each message's role; JSON contains exactly the model-visible message arrays. The content following the role comment is verbatim.

For a fresh Python environment with venv/pip available:

```sh
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/almost-twin render-prompts --demo
```

`python3 -m almost_twin` works without installation when PyYAML is already installed. `pdftotext` from Poppler (`poppler-utils` on Debian/Ubuntu) is needed only if the TeX extraction fails. There is no LLM conversion, TeX compilation, or OCR.

## Acquire and inspect sources

```sh
python3 -m almost_twin fetch-sources --network
# Offline re-extraction after an extractor change, retaining actual retrieval timestamps:
python3 -m almost_twin fetch-sources --reextract
```

Source acquisition is explicitly network-enabled but never calls a generation API. Without `--network` or `--reextract`, the command fails before networking. `--source cdt`, `--source edt`, and `--source fdt` can restrict acquisition. Each attempt has an immutable directory under `data/source_cache/<source_id>/`; successful automated checks update `current.json`. Failed attempts retain diagnostics and do not overwrite the earlier source. A failed command exits nonzero even if some other sources succeeded.

Read `data/source_cache/report.md`, then each linked `article.md`, `qa.md`, and `provenance.json`. Raw downloads, retrieval times, resolved URLs, revisions, byte hashes, normalization hashes, extractor identity/code hash, conversion commands, warnings, and text counts are recorded. Local raw and normalized hashes are checked again before prompt use.

The actual Sprint 01 acquisition succeeded for all three sources. A metadata-only snapshot is in [sources/acquisition_report.json](sources/acquisition_report.json). The first extractor attempts failed on the separate SEP notes container and an overly narrow FDT wording check; the saved bytes were re-extracted after fixing both checks. Failed-attempt records remain locally. No missing passage was filled in by a model.

- **CDT:** SEP's full *Causal Decision Theory* article, substantive revision 24 October 2024. Headings, examples, bibliography and math are retained.
- **EDT:** SEP's full *Decision Theory* article, substantive revision 20 August 2025, including §3.2 on Jeffrey and twelve linked notes. This is a broad decision-theory article, **not a dedicated EDT entry**.
- **FDT:** Explicitly pinned `1710.05060v2` TeX source, retrieved before any PDF processing. A safe tar/gzip/single-TeX reader rejects traversal, links, special files and excessive decompression; input/include files are resolved without executing TeX. Conservative Markdown retains display math, all four equation numbers, sixteen footnotes, macro definitions, TikZ graph code and bibliography data. QA shows Equation (4), its observation-indexed variable, the observation-change paragraph, the graph-construction open problem and footnote 16. **Some macro notation, cross-references and graph drawings remain literal TeX**; manual formatting approval is necessary. This is not a polished Pandoc rendition. If source conversion fails, text PDF extraction is attempted with `pdftotext -layout`; a failed mathematical check is a visible failure. A genuinely non-textual PDF requires separate manual OCR work, which is not implemented.

All `data/` artifacts are gitignored, including full source text, source excerpts, rendered prompts, responses, commitments and local budget state. Only URLs, metadata/hashes, scripts, templates and synthetic fixtures belong in the repository. SEP's [terms](https://plato.stanford.edu/info.html#t) distinguish personal downloads from redistribution. Before sending full articles to OpenRouter and a provider, resolve that **separate source-license/terms question**, individually for SEP and FDT. Availability on arXiv is not blanket redistribution permission. The researcher runner blocks live article transmission until `--source-terms-reviewed` is explicitly passed; that flag records your resolved review, not a legal determination by this scaffold.

## Review the exact prompts

Read these plain files first:

1. [Researcher request](prompts/researcher/base.md), [FDT Equation 4 focus](prompts/researcher/fdt_eq4_focus.md), and [FDT footnote 16 focus](prompts/researcher/fdt_policy_focus.md).
2. [Prisoner text-adventure prompt](prompts/prisoner/base.md) and [in-scene observation/evidence cases](prompts/prisoner/observation_cases.yaml). The OOC setup and frozen essay precede the holding-cell scene; the lawyer's letter states the payoff table, and a decoded notebook note gives the prisoner their own actionable fictional evidence.
3. [Source manifest](sources/manifest.yaml), the full local articles and their QA passages.
4. [Implementation choices and open questions](docs/implementation_choices.md), [adjudication protocol](docs/adjudication_protocol.md), [blinded judge prompt](prompts/judge/intent.md), [early-test configuration](configs/early_test.yaml), and [OpenRouter settings template](configs/openrouter.example.json).

Render actual article text with the labeled synthetic essay for **procedure inspection only**:

```sh
python3 -m almost_twin render-prompts --assignment fdt_eq4 --essay fixtures/demo_essay.md
```

Change `--assignment` to `cdt`, `edt` or `fdt_policy` to inspect the other assignments. Outputs go to `data/rendered_prompts/source_review/<assignment>/`. `researcher.md/.json` contains the actual article; `T0_identical/a.md`, `b.md` and `pair.diff` show identical requests; `T2_name/` changes only Rowan → Sasha; `T4_distinct_leads/` changes both characters' names, evidence and outgoing letters. `audit.json` records hashes. Omitting `--essay` renders only the researcher request; an empty essay fails. A subsequent render can replace the review export; run directories and source attempts are unique.

The handoff index at `data/review.md` links the full researcher prompt and both prisoner prompts/diffs for one T0 and one T2, plus all source reports. Prisoner previews currently contain the clearly labeled synthetic fixture because no live researcher essay exists. Before any live prisoner call, render again using the **actual frozen essay**:

```sh
python3 -m almost_twin render-prompts --assignment fdt_eq4 --essay data/runs/RESEARCHER_RUN_ID/essay.md
```

T0 requests are byte-identical. T2 requests differ only in the private intake-card name. T4 requests differ in three audited slots: the visible cell observation, the notebook's private lead, and the example disclosure command. Single-pass substitution preserves embedded essay/source text verbatim. IDs, filenames, budgets, hashes and hypotheses are metadata only. [docs/hypotheses.md](docs/hypotheses.md) is never loaded by rendering or execution; tests prohibit experiment/game fields in researcher instructions. Natural examples inside the supplied article are retained.

## OpenRouter settings, preflight and dry run

The runner has no built-in model selection. Copy `configs/openrouter.example.json` to `data/openrouter/settings.json`; select an exact model ID, one endpoint provider tag, separate researcher `effort` (`e_R`) and prisoner `effort` (`e_A`), and output limits. Researcher/prisoner limits of 12,000/3,000 tokens are **reviewable starter budgets**, including reasoning where counted by the provider. They are not guarantees of a complete essay or adequate reasoning. Null temperature/seed means those fields are omitted and provider defaults apply; an explicit seed is shared by both calls and can change how independent sampling behaves.

After you select a model, unbilled metadata discovery is available:

```sh
python3 -m almost_twin inspect-model --network --model YOUR/EXACT_MODEL --out data/openrouter/capabilities.json
```

This sends no source, essay or credential. Inspect the saved model and `endpoints[]`. Set `provider_tag` to one exact endpoint `tag`, not a broad provider family that could match multiple routes. If the endpoint does not advertise individual supported reasoning efforts, supply a dated `provider_effort_review` in your settings: allowed efforts, provider/model documentation URL, review timestamp and explanatory note. A generic `reasoning` parameter advertisement alone is insufficient. If current catalog shape differs or the evidence is insufficient, preflight fails until reviewed. There is no silent effort translation or fallback in application code.

```sh
python3 -m almost_twin run researcher --assignment fdt_eq4 \
  --settings data/openrouter/settings.json \
  --capabilities data/openrouter/capabilities.json
```

This is still offline. It exports complete messages, validated payload metadata and a conservative cost estimate to a unique `data/runs/<uuid>/plan.json`; it makes no reservation, records no successful essay, and requires no key. Without a capability file it exports a clearly **unvalidated** plan with unknown cost. Do not interpret that plan as permission or feasibility for a live call.

Preflight requires the selected endpoint to advertise requested parameters, accepts only verified effort levels, checks full untruncated context and output limits, and requires JSON-object response-format support for prisoners. Unknown limits, nonstandard pricing, unsupported temperature/seed and stale (>24 hours) capability/evidence timestamps fail. Live mode refreshes metadata before spending. Token estimates use UTF-8 message JSON bytes plus 512 framing tokens as a deliberately conservative proxy; no source or essay is shortened. Pricing is taken from the pinned endpoint and includes the full output token budget. These are **estimated spending caps**, not a provider-enforced dollar ceiling; use an OpenRouter key credit limit for a hard account spending limit.

The request path is `POST https://openrouter.ai/api/v1/chat/completions`. It sends a single `reasoning: {effort: ...}`, explicit `max_tokens`, `provider.require_parameters: true`, exact `provider.only`/`order`, and `allow_fallbacks: false`. Model IDs and any returned provider are checked, raw responses and actual route metadata are retained. Per-model weights cannot be independently inspected; pair fingerprints are compared when returned, and a mismatch excludes the pair while preserving any already committed actions. Missing fingerprints are recorded as unverifiable.

Reference documentation: [chat API](https://openrouter.ai/docs/api/api-reference/chat/create-a-chat-completion), [reasoning and supported efforts](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens), [endpoint metadata](https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints), [provider parameter requirements](https://openrouter.ai/docs/guides/routing/provider-selection).

## Optional live smoke test — only after manual approval

**Do not execute these example commands until you approve the rendered prompts, resolve article transmission terms, select the model/efforts, and review cost.** No live test is part of the completed sprint.

Set `OPENROUTER_API_KEY` in the environment, or a gitignored `.env` containing `OPENROUTER_API_KEY=...` (no shell evaluation/interpolation). The environment takes precedence. Keys are used only for the generation Authorization header and are never saved in request artifacts.

One researcher call:

```sh
python3 -m almost_twin run researcher --assignment fdt_eq4 \
  --settings data/openrouter/settings.json \
  --execute --confirm-billable --prompts-approved --source-terms-reviewed
```

After reading the entire saved essay and rendering/approving the resulting prisoner prompts, one pair (two independently instantiated calls):

```sh
python3 -m almost_twin run prisoner --assignment fdt_eq4 \
  --settings data/openrouter/settings.json \
  --essay data/runs/RESEARCHER_RUN_ID --scenario t4_distinct_leads_001 \
  --execute --confirm-billable --prompts-approved
```

Both billable flags are required. There is no batch command. The default persistent project budget is four calls and US$2 estimated spend; `--max-calls`/`--max-usd` explicitly change those limits. `data/budget.jsonl` reserves the whole stage before calling; failed/unknown transport outcomes remain charged against the reservation. A pair is always preflighted and reserved together. Calls are sequential HTTP requests **with separate one-message contexts**, not continuations; neither request contains the other's output. No automated retries are implemented. Changing the local ledger, directory or cap can bypass local accounting, so retain it as an audit record.

Each live call saves the exact serialized request, exact raw response bytes, transport metadata, output text and append-only start/success/failure JSONL events with source/template/essay hashes, IDs, model, effort, usage, finish reason and route metadata. Transport errors and truncated generations fail. **Empty or refused prisoner answers are retained as `OTHER` responses**, while an empty/refused researcher essay still fails. The researcher `essay.md` is the entire unedited response content, frozen by hash and verified against the raw response before reuse. Only a completed same-model, same-assignment researcher artifact is accepted for execution; a standalone synthetic preview is not a runnable research essay.

Prisoners are encouraged to enter **one of two text-adventure commands**, not JSON. Here is the T4 example for the first prisoner:

```text
pass
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

The other prisoner receives a *different* letter, disclosing a different item in a different location. The initial classifier is deliberately small: a final `pass` means cooperation; a final `submit letter` command addressed to the prosecutor counts as successful defection if it contains the required **case-insensitive evidence phrases**. Those phrases live in the readable [observation cases file](prompts/prisoner/observation_cases.yaml): `locker 17` for one lead, `clock` **and** `inventory sheet` for the other. Full sentence copying is unnecessary. A model that merely mentions evidence in its reasoning is not automatically scored as having sent it.

Everything else, including prose answers such as `I choose to defect`, is marked `OTHER`/`UNCERTAIN` **pending the judge**. The judge separately assigns `TRIED_DEFECT`, `TRIED_COOPERATE`, or `OTHER` and `YES`, `NO`, or `UNCERTAIN` disclosure. Unclear responses are preserved, never silently coerced to C/D. `pass = WITHHOLD = C`, and `submit letter = SUBMIT = D`; the payoff schedule and selfish utility are unchanged. Only high-confidence executed actions are immediately committed to the fictional game journal.

For a completed local prisoner run, prepare **offline, blind** prompts for later LLM or human classification:

```sh
python3 -m almost_twin prepare-adjudication --run data/runs/PRISONER_RUN_ID
```

These are written under the run's `adjudication_prompts/` directory. Before creating judge prompts, the command checks that the evidence-case YAML has the same hash as the one used for the prisoner run, and that each `output.txt` exactly matches the model content in its saved `response.raw`. Any mismatch stops adjudication, preventing later template edits or output-file changes from silently affecting historical labels. The judge sees the private lead, possible command and raw response, **not explicitly** the theory, model, effort, or essay (although the response itself could mention these). See the [adjudication protocol](docs/adjudication_protocol.md).

To run the **optional** OpenRouter judge, the example configuration uses `openai/gpt-6.1-sol`. Inspect its available endpoint tags first and enter an exact `provider_tag` into a copy of [configs/judge.example.json](configs/judge.example.json):

```sh
python3 -m almost_twin inspect-model --network --model openai/gpt-6.1-sol --out data/openrouter/judge_capabilities.json
python3 -m almost_twin run-judge --run data/runs/PRISONER_RUN_ID \
  --settings data/openrouter/judge-settings.json \
  --capabilities data/openrouter/judge_capabilities.json
```

This is an **offline plan**, requiring no API key. After reading the generated judge messages, actual billable adjudication requires the same command with `--execute --confirm-billable --prompts-approved`. It sends only uncertain prisoner responses, has a separate capped budget (two calls / $1 by default), and saves exact requests, responses, judge labels, and an **annotated outcome** without changing the original game journal. Judge prompts and metadata remain auditable; no judge or prisoner calls have been made by this project yet.

## Scope and remaining decisions

Implemented: source acquisition/provenance/QA; readable literal templates; offline prompt rendering, hashes and diffs; a small protected OpenRouter path; frozen essays; independent paired calls with a matching researcher/prisoner model **and provider tag**; role-specific evidence/letters; **simple marker-based command recognition**; separate guarded OpenRouter Sol-judge stage with historical evidence/output integrity checks; blinded-judge prompt exports; persistent fictional commitments and symmetric scoring; offline/mocked integration tests. All tests run without network or credentials.

Pending manual review: source formatting and licenses, prompt approval, exact model/provider/version selection, `e_R`/`e_A`, output budgets and optional decoding settings. Native source lengths/styles differ substantially. The direct-paper control remains a separate draft file; **direct-paper, essay-plus-source, T1/T3 execution, counterbalancing, batch adjudication, statistical analysis, optimization, dashboards and publication are not implemented**. T1/T3 observations remain available for later work. No paid batch, live smoke test, or empirical results have occurred. Scaling waits for manual prompt approval.
