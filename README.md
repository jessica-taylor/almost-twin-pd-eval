# Almost-Twin Decision Theory Eval — Sprint 01

An auditable, offline-first scaffold for **human article → researcher essay → two independent simulated prisoner decisions**. Mainline prisoners receive the same frozen essay, never the original article. Model and effort choices are explicit in each saved pilot; preparation requires no model calls.

The authoritative broad design is [docs/design_v03.md](docs/design_v03.md); [CODEX_TASK.md](CODEX_TASK.md) is the original Sprint 01 handoff. The current prisoner interface is a **naturalistic, one-turn text adventure**, further refined in the [distinct-evidence and adjudication protocol](docs/adjudication_protocol.md). The default early-test scenario has different evidence and outgoing letters for the two prisoners. Prompts are not approved or frozen instruments yet.

## Quick start: exploratory CDT Wikipedia / GPT-5 Nano

Use Python 3.11+ with PyYAML installed. Set `OPENROUTER_API_KEY` in your environment or a gitignored `.env` (see `.env.example`). No endpoint-tag discovery, settings file or hand-written timestamp is needed for this workflow.

Acquire the source and inspect `data/source_cache/report.md` and its full article/QA links:

```sh
python3 -m almost_twin fetch-sources --network --source cdt_wikipedia
```

No separate source approval is required. Source attribution, manifest pins, revision identity and raw/normalized/provenance hash checks remain in place.

Prepare one exploratory three-call pilot. This command refreshes **unbilled metadata only**, selects and pins an endpoint, and exports the complete researcher request and spending estimate. It sends no source or essay to a model:

```sh
python3 -m almost_twin pilot prepare \
  --assignment cdt_wikipedia --model openai/gpt-5-nano \
  --researcher-effort low --prisoner-effort low \
  --scenario t4_distinct_leads_001 --out data/pilots/cdt-nano
```

Open `data/pilots/cdt-nano/plan.md`. The researcher prompt, message JSON and exact serialized request are in its `researcher/` directory. Review the estimated cost and effort evidence, then explicitly authorize **one researcher call**:

```sh
python3 -m almost_twin pilot researcher --pilot data/pilots/cdt-nano \
  --execute --confirm-billable --prompts-approved
```

The command prints the frozen `essay.md` path; the pilot's `plan.md` links it and all run artifacts. Read the essay before preparing the two prisoner requests:

```sh
python3 -m almost_twin pilot prisoners --pilot data/pilots/cdt-nano
```

That command makes no generation requests. Inspect both `data/pilots/cdt-nano/prisoners/messages_0.md` and `messages_1.md`, their JSON/serialized requests and updated costs, then explicitly authorize **two independent prisoner calls**:

```sh
python3 -m almost_twin pilot prisoners --pilot data/pilots/cdt-nano \
  --execute --confirm-billable --prompts-approved
```

The updated `plan.md` links the pair outcome, responses and exact API records. Exploratory runs and append-only essay/decision/commitment logs live under `data/exploratory/`; the pilot's append-only history is `events.jsonl`. The project-wide budget ledger remains `data/budget.jsonl`. All these artifacts, approvals and credentials are gitignored.

Pilot defaults are three cumulative reserved calls and US$2 estimated spend. Set `--max-calls`/`--max-usd` at preparation to change them explicitly; prior project reservations, including failed/unknown transport outcomes, count toward those caps. The initial pair-cost projection uses the endpoint context ceiling because the essay is not yet known; exact pair costs are recalculated after the essay. These are estimated caps, not an account billing guarantee. Use an OpenRouter key credit limit for a hard account limit.

A completed researcher or pair is returned when resumed, never automatically called again. Partial failures preserve responses, commitments, logs and reservations and require deliberate new preparation rather than an automatic retry. Existing pilots cannot be overwritten. Use a new `--out` for a new exploratory trial or changed instructions/settings. [Detailed behavior and audit assumptions](docs/pilot_workflow.md).

## Collect multiple complete trials

After the CDT Wikipedia source is cached as above, prepare five separate essay → prisoner A → prisoner B → judge-if-needed trials, using GPT-5 Nano with low reasoning for both researcher and prisoners. Preparation performs only unbilled metadata checks:

```sh
python3 -m almost_twin batch prepare \
  --assignment cdt_wikipedia --model openai/gpt-5-nano \
  --researcher-effort low --prisoner-effort low \
  --scenario t4_distinct_leads_001 --count 5 \
  --max-calls 30 --max-usd 5.00 \
  --out data/batches/cdt-nano-five
```

Review `data/batches/cdt-nano-five/plan.md`, its researcher prompt and the existing prisoner/judge templates. The approval here is deliberately **for the template family with future model-generated essays**, not a claim that all dynamic prompts were individually inspected. First run one full sample, then resume the remainder concurrently:

```sh
python3 -m almost_twin batch run --batch data/batches/cdt-nano-five \
  --execute --confirm-billable --approve-variable-prompts --limit 1
python3 -m almost_twin batch run --batch data/batches/cdt-nano-five \
  --execute --confirm-billable --approve-variable-prompts --jobs 2
python3 -m almost_twin batch status --batch data/batches/cdt-nano-five
```

Each sample creates a **fresh essay** and two independent prisoner calls, followed by zero to two judge calls for ambiguous actions. Every API request, raw response, validation result and error is retained. The derived `results.jsonl` and `results.csv` contain one row per sample for later analysis. There are no automatic retries of attempted calls; completed trials are skipped on resume. Judge model/effort, budgets and endpoint are configurable at preparation. See [full batch workflow, artifacts and safeguards](docs/batch_workflow.md).

### Study-wide model × theory × reasoning-effort matrices

Use `study check` (unbilled) to validate every requested model/provider/effort
combination and the aggregate budget **before** creating a study. `study
prepare` freezes a separate batch for each cell; `study run` resumes cells
sequentially, running multiple full scenarios concurrently within a cell;
`study report` exports pair-level and prisoner-level results, cooperation
rates and CC/CD/DC/DD counts without calling models. Example:

```sh
python3 -m almost_twin study check --config configs/study.smoke.example.yaml
python3 -m almost_twin study prepare --config configs/study.smoke.example.yaml \
  --out data/studies/cdt-smoke
python3 -m almost_twin study run --study data/studies/cdt-smoke \
  --execute --confirm-billable --approve-variable-prompts --jobs 2
python3 -m almost_twin study report --study data/studies/cdt-smoke
```

Only the `study run` line is billable. For the proposed OpenAI, Anthropic,
Google, DeepSeek, Qwen and GLM matrix, begin with
`configs/study.example.yaml`; it is a *candidate slate*, not a validated
promise that every endpoint supports both requested reasoning levels. The
protective example budget must be reviewed and explicitly adjusted if the
preflight projection exceeds it. Prisoner A and B continue to receive their
fixed, different prompts, and the primary cooperation rate weights them
equally within each complete two-prisoner sample.

See [study workflow and safeguards](docs/study_workflow.md).

For an immediately readable **cooperate/defect result in every sample directory**, run the offline reporting command after any amount of batch progress:

```sh
python3 -m almost_twin.sample_report --batch data/batches/cdt-nano-five
```

It writes `samples/00000/result.md` and `result.json` (and equivalents for each other sample) and prints the current A/B classifications. `WITHHOLD` means cooperate; `SUBMIT` means defect. The report distinguishes recognized commands from judge-inferred actions, and shows years/utility only for a complete scored pair. It also writes **`samples/00000/transcript.md`**, a **terminal-friendly `samples/00000/transcript.txt`**, and a `transcript/` folder. Both full transcripts show the complete returned researcher/prisoner/judge answer texts and **any readable reasoning supplied by OpenRouter inline**, rather than being link-only indexes. Individual response and reasoning files, structured details and authoritative `response.raw` JSON remain available. The transcript explicitly says when no readable reasoning was returned; reported reasoning tokens are not treated as a trace. It works with batches prepared before this feature and makes **no model calls**. It is deliberately separate from the hash-pinned generation runner, so adding or updating the reporter does not invalidate an in-progress batch.

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

Source acquisition is explicitly network-enabled but never calls a generation API. Without `--network` or `--reextract`, the command fails before networking. `--source` requires an explicit article choice: `cdt_sep`, `edt_sep`, `fdt`, `cdt_wikipedia`, or `edt_wikipedia`. Each attempt has an immutable directory under `data/source_cache/<source_id>/`; successful automated checks update `current.json`. Failed attempts retain diagnostics and do not overwrite the earlier source. A failed command exits nonzero even if some other sources succeeded.

Read `data/source_cache/report.md`, then each linked `article.md`, `qa.md`, and `provenance.json`. Raw downloads, retrieval times, resolved URLs, revisions, byte hashes, normalization hashes, extractor identity/code hash, conversion commands, warnings, and text counts are recorded. Local raw and normalized hashes are checked again before prompt use.

The actual Sprint 01 acquisition succeeded for all three sources. A metadata-only snapshot is in [sources/acquisition_report.json](sources/acquisition_report.json). The first extractor attempts failed on the separate SEP notes container and an overly narrow FDT wording check; the saved bytes were re-extracted after fixing both checks. Failed-attempt records remain locally. No missing passage was filled in by a model.

- **CDT:** SEP's full *Causal Decision Theory* article, substantive revision 24 October 2024. Headings, examples, bibliography and math are retained.
- **EDT:** SEP's full *Decision Theory* article, substantive revision 20 August 2025, including §3.2 on Jeffrey and twelve linked notes. This is a broad decision-theory article, **not a dedicated EDT entry**.
- **FDT:** Explicitly pinned `1710.05060v2` TeX source, retrieved before any PDF processing. A safe tar/gzip/single-TeX reader rejects traversal, links, special files and excessive decompression; input/include files are resolved without executing TeX. Conservative Markdown retains display math, all four equation numbers, sixteen footnotes, macro definitions, TikZ graph code and bibliography data. QA shows Equation (4), its observation-indexed variable, the observation-change paragraph, the graph-construction open problem and footnote 16. **Some macro notation, cross-references and graph drawings remain literal TeX**; inspect the mathematical formatting as needed. This is not a polished Pandoc rendition. If source conversion fails, text PDF extraction is attempted with `pdftotext -layout`; a failed mathematical check is a visible failure. A genuinely non-textual PDF requires separate manual OCR work, which is not implemented.

All `data/` artifacts are gitignored, including full source text, source excerpts, rendered prompts, responses, commitments and local budget state. Only URLs, metadata/hashes, scripts, templates and synthetic fixtures belong in the repository. Each source retains its licensing, attribution and redistribution metadata, including [SEP terms](https://plato.stanford.edu/info.html#t). The runner verifies source integrity and imposes no separate article-transmission approval step.

## Wikipedia CDT and EDT source variants

Theory and source are separate: **CDT** and **EDT** are theory labels, while every selectable reference names its source explicitly.

| Theory | SEP source / assignment | Wikipedia source / assignment |
|---|---|---|
| CDT | `cdt_sep` | `cdt_wikipedia` |
| EDT | `edt_sep` | `edt_wikipedia` |

Bare `cdt` and `edt` are not source IDs or assignment shortcuts and do not select SEP. Decision-theory instructions and model-visible labels remain simply CDT/EDT. The pinned FDT source is unchanged.

Old cache directories and the original acquisition snapshot retain their historical `cdt`/`edt` identifiers. To reuse their exact downloads offline under the explicit names, run `python3 -m almost_twin fetch-sources --reextract --source cdt_sep --source edt_sep`. This creates new immutable attempts without renaming or changing old bytes/provenance. Historical run/essay assignment IDs are not rewritten or silently aliased.

```sh
python3 -m almost_twin fetch-sources --network --source cdt_wikipedia
python3 -m almost_twin fetch-sources --network --source edt_wikipedia
python3 -m almost_twin render-prompts --assignment cdt_wikipedia --essay fixtures/demo_essay.md
python3 -m almost_twin render-prompts --assignment edt_wikipedia --essay fixtures/demo_essay.md
# Always offline; keeps the original revision, API responses and retrieval provenance:
python3 -m almost_twin fetch-sources --reextract --source cdt_wikipedia --source edt_wikipedia
# Offline researcher preflight only; no key or generation request:
python3 -m almost_twin run researcher --assignment cdt_wikipedia
```

Read `data/source_cache/report.md` and both local QA reports, then the full articles, original `revision.wikitext` and `rendered.html`. Complete researcher previews and exact JSON messages are under `data/rendered_prompts/source_review/{cdt_wikipedia,edt_wikipedia}/`; prisoners in these previews use the **synthetic** essay fixture. The ordinary prisoner dry-run command also accepts these assignment IDs, once supplied a frozen same-model researcher artifact. No such real model artifact is generated in this source-only sprint.

Acquisition uses the official MediaWiki Revisions API and Parse API `oldid` for the **same revision**; raw JSON, decoded wikitext, rendered HTML, normalized Markdown and provenance are hashed. Mathematical expressions are recovered from LaTeX annotations/alt text or exact revision wikitext with matching expression counts. Unannotated MathML recovery explicitly requires manual formula-correspondence review. All substantive sections, examples, lists, relevant tables, citations and references are retained; edit/navigation UI and media are excluded, with meaningful image descriptions and exclusions recorded. No LLM rewriting or external image downloads occur.

The acquired candidates are CDT revision **1381555528** and EDT revision **1373679688**. Automated QA passed with warnings; **manual review and manifest pinning remain pending**. After approving an article, set `revision_id` to its reviewed integer and `revision_review: approved` in `sources/manifest.yaml`. Subsequent acquisition verifies that pin; re-extraction accepts only the matching cached revision. Before pinning, network acquisition is discovery and may resolve a newer candidate. A cached revision that conflicts with a manifest pin is rejected before prompt use.

Both normalized articles include title, attribution to Wikipedia contributors with a history link, permanent revision URL, CC BY-SA 4.0 name/link, conversion modifications and media/third-party-rights qualifications. They remain local and gitignored. No source-license approval step blocks execution; attribution and rights qualifications remain attached to the article, and later publications/adaptations can carry licensing obligations.

Wikipedia is useful as a licensed reference condition, but is not necessarily as comprehensive or philosophically authoritative as SEP. **EDT explicitly discusses the twin prisoner's dilemma and recommends cooperation; CDT also discusses twins and correlated decisions.** These passages are preserved. Exposure annotations and excerpts are for human QA only, not extra researcher instructions. See the [SEP/Wikipedia comparison, downloaded revisions and formatting caveats](docs/wikipedia_sources.md) and [metadata-only acquisition report](sources/wikipedia_acquisition_report.json).

## Review the exact prompts

The two functional decision theories have distinct model-visible names:

| Assignment ID | Assigned decision theory | Primary source passage |
|---|---|---|
| `fdt_eq4` | **A-FDT** — action functional decision theory | Equation (4), Section 5 |
| `fdt_policy` | **P-FDT** — policy functional decision theory | Footnote 16, policy selection |

Researcher and prisoner requests explicitly name A-FDT or P-FDT. The researcher is asked to use that distinct name consistently in its essay and identify other theories by their specific names. There is no assignment to apply an unqualified “FDT.” Both assignments use the same unmodified human-written paper; its original title, notation and quotations remain intact. The source ID `fdt` identifies that paper, not an assigned decision theory. Historical prompts, essays and results are not relabeled.

Read these plain files first:

1. [Researcher request](prompts/researcher/base.md), [A-FDT Equation 4 assignment](prompts/researcher/fdt_eq4_focus.md), and [P-FDT footnote 16 assignment](prompts/researcher/fdt_policy_focus.md).
2. [Prisoner text-adventure prompt](prompts/prisoner/base.md) and [in-scene observation/evidence cases](prompts/prisoner/observation_cases.yaml). The OOC setup and frozen essay precede the holding-cell scene; the lawyer's letter states the payoff table, and a decoded notebook note gives the prisoner their own actionable fictional evidence.
3. [Source manifest](sources/manifest.yaml), the full local articles and their QA passages.
4. [Implementation choices and open questions](docs/implementation_choices.md), [adjudication protocol](docs/adjudication_protocol.md), [blinded judge prompt](prompts/judge/intent.md), [early-test configuration](configs/early_test.yaml), and [OpenRouter settings template](configs/openrouter.example.json).

Render actual article text with the labeled synthetic essay for **procedure inspection only**:

```sh
python3 -m almost_twin render-prompts --assignment fdt_eq4 --essay fixtures/demo_essay.md
```

Change `--assignment` to `cdt_sep`, `edt_sep`, `cdt_wikipedia`, `edt_wikipedia` or `fdt_policy` to inspect the other assignments. Outputs go to `data/rendered_prompts/source_review/<assignment>/`. `researcher.md/.json` contains the actual article; `T4_distinct_leads/a.md`, `b.md` and `pair.diff` show the role-specific names, evidence and outgoing letters. `audit.json` records hashes. The current early-test design **always** gives the two prisoners different observations and different concrete disclosure commands; older identical-prompt controls are no longer runnable. Omitting `--essay` renders only the researcher request; an empty essay fails. A subsequent render can replace the review export; run directories and source attempts are unique.

Any old `data/review.md` handoff index was generated under an earlier template version and may still refer to T0/T2 controls. Use a fresh `render-prompts` export for the current active case. Before any live prisoner call, render again using the **actual frozen essay**:

```sh
python3 -m almost_twin render-prompts --assignment fdt_eq4 --essay data/runs/RESEARCHER_RUN_ID/essay.md
```

T4 requests differ in three audited slots: the visible cell observation, the notebook's private lead, and the example disclosure command. No active scenario claims identical observations. New observation variants can be added to the YAML, but must also have distinct private observations and concrete disclosure letters. Single-pass substitution preserves embedded essay/source text verbatim. IDs, filenames, budgets, hashes and hypotheses are metadata only. [docs/hypotheses.md](docs/hypotheses.md) is never loaded by rendering or execution; tests prohibit experiment/game fields in researcher instructions. Natural examples inside the supplied article are retained.

## OpenRouter settings and lower-level preflight

The pilot workflow above generates its pinned settings automatically. The existing lower-level `run` commands remain available. For them, copy [configs/openrouter.example.json](configs/openrouter.example.json), choose a model and separate researcher/application efforts, and optionally set `provider_tag`. A null provider selects an endpoint once for the researcher; prisoner execution inherits the frozen essay's endpoint. Explicit provider-tag overrides are never silently replaced. Null temperature/seed omits those fields; requested optional decoding parameters must be advertised as supported.

Offline metadata snapshots remain supported:

```sh
python3 -m almost_twin inspect-model --network --model openai/gpt-5-nano --out data/openrouter/capabilities.json
python3 -m almost_twin run researcher --assignment cdt_wikipedia \
  --settings data/openrouter/settings.json --capabilities data/openrouter/capabilities.json
```

`run` is offline by default; without a capability file it exports a clearly **unvalidated** plan with unknown cost. `pilot prepare --capabilities data/openrouter/capabilities.json` also runs entirely offline. Normal pilot preparation/resume refreshes unbilled metadata automatically; live execution always refreshes before spending, validates the same pinned endpoint and model version, and stops if that endpoint becomes unsuitable. There is no mid-experiment fallback.

Reasoning validation uses endpoint `reasoning.supported_efforts` first, then model-level metadata. An explicit `null` accepts gateway effort values per OpenRouter's documented semantics; an omitted field supplies no effort evidence. Mandatory reasoning still rejects `none`. Plans record `verified_by_endpoint_metadata`, `verified_by_model_metadata`, or `documented_manual_override`, and preserve the selected effort unchanged. Insufficient evidence is `unverified` and blocks execution unless the user supplies a recorded assumption with `pilot prepare --allow-unverified-effort "reason"`, or a `reasoning_override` object with `efforts` and `reason` in lower-level settings. This override has no timestamp expiry and cannot bypass an explicitly unsupported effort. The old `provider_effort_review` format is accepted as a manual override, without requiring a new 24-hour review.

Pricing is request-aware. Text-only requests do not pay for optional search, image/audio or other tools they do not enable. Nonzero prices for those unused features are listed in `plan.json` under `estimates[].pricing_assumptions.ignored_fields`, with reasons. Requests explicitly disable OpenRouter plugins; tools/modalities are absent, and known automatic-search models/defaults are rejected. Cache reads use the larger of prompt/read rates, cache-write rates are conservatively added on every input token, and separate internal-reasoning rates are added on the full combined output budget. **Known prompt-length pricing tiers** (`overrides` with `min_prompt_tokens` and supported token rates) are bounded using the highest rate in every applicable category, with all tiers recorded in the estimate; this can overestimate small prompts. Unknown tier rules, other potentially applicable prices, storage charges, invalid rates and unknown limits still fail with actionable diagnostics.

Token estimates use UTF-8 message JSON bytes plus 512 framing tokens, including the full output budget; source/essay text is never truncated. The request path remains `POST https://openrouter.ai/api/v1/chat/completions`, with one `reasoning: {effort: ...}`, one supported output-limit field, `require_parameters: true`, and pinned `provider.only`/`order` with fallback disabled. Plain-text prisoner responses and current adjudication behavior are unchanged; only the separate judge requests JSON.

References: [OpenRouter reasoning/effort semantics](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens), [web-search enablement](https://openrouter.ai/docs/guides/features/plugins/web-search), [prompt-cache charges](https://openrouter.ai/docs/guides/best-practices/prompt-caching), [GPT-5 Nano](https://developers.openai.com/api/docs/models/gpt-5-nano).

## Optional live smoke test — only after manual approval

**Do not execute these example commands until you approve the rendered prompts, select the model/efforts, and review cost.** No live test is part of the completed sprint.

Set `OPENROUTER_API_KEY` in the environment, or a gitignored `.env` containing `OPENROUTER_API_KEY=...` (no shell evaluation/interpolation). The environment takes precedence. Keys are used only for the generation Authorization header and are never saved in request artifacts.

One researcher call:

```sh
python3 -m almost_twin run researcher --assignment fdt_eq4 \
  --settings data/openrouter/settings.json \
  --execute --confirm-billable --prompts-approved
```

After reading the entire saved essay and rendering/approving the resulting prisoner prompts, one pair (two independently instantiated calls):

```sh
python3 -m almost_twin run prisoner --assignment fdt_eq4 \
  --settings data/openrouter/settings.json \
  --essay data/runs/RESEARCHER_RUN_ID --scenario t4_distinct_leads_001 \
  --execute --confirm-billable --prompts-approved
```

Both billable flags are required. The lower-level `run` command is for one researcher or prisoner pair; the `pilot` and `batch` commands wrap it for exploratory end-to-end execution. The default persistent project budget for lower-level calls is four calls and US$2 estimated spend; `--max-calls`/`--max-usd` explicitly change those limits. `data/budget.jsonl` reserves the whole stage before calling; failed/unknown transport outcomes remain charged against the reservation. A pair is always preflighted and reserved together. Calls are sequential HTTP requests **with separate one-message contexts**, not continuations; neither request contains the other's output. No automated retries are implemented. Changing the local ledger, directory or cap can bypass local accounting, so retain it as an audit record.

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

This is an **offline plan**, requiring no API key. After reading the generated judge messages, actual billable adjudication requires the same command with `--execute --confirm-billable --prompts-approved`. It sends only uncertain prisoner responses, has a separate capped budget (two calls / $1 by default), and saves exact requests, responses, judge labels, and an **annotated outcome** without changing the original game journal. Judge prompts and metadata remain auditable.

## Scope and remaining decisions

Implemented: exploratory single-pilot and **repeated batch** workflows (fresh essay + pair + conditional judge per sample, resumable/concurrent execution, CSV/JSONL exports); automatic endpoint pinning, persistent scope/hash-bound approvals and request-aware pricing; source acquisition/provenance/QA; readable literal templates; offline prompt rendering, hashes and diffs; a small protected OpenRouter path; frozen essays; independent paired calls with a matching researcher/prisoner model **and provider tag**; role-specific evidence/letters; **simple marker-based command recognition**; separate guarded OpenRouter Sol-judge stage with historical evidence/output integrity checks; blinded-judge prompt exports; persistent fictional commitments and symmetric scoring; offline/mocked integration tests. All tests run without network or credentials.

Pending manual review: source formatting and licenses, prompt approval, exact model/provider/version selection, `e_R`/`e_A`, output budgets and optional decoding settings. Native source lengths/styles differ substantially. The direct-paper control remains a separate draft file; **direct-paper, essay-plus-source, T1/T3 execution, counterbalancing, statistical analysis, optimization, dashboards and publication are not implemented**. T1/T3 observations remain available for later work. The new batch layer has only been tested offline with mocked model responses; no billable batch was run while implementing it. Scaling requires explicit review of the source/template family and batch authorization.

