# Codex task: Almost-Twin Decision Theory Eval — Sprint 01

> **Post-sprint interface update:** This file preserves the original Sprint 01 handoff. The currently implemented prisoner prompt is now a naturalistic text adventure, with a lawyer's letter, private notebook, and two literal terminal commands (`pass` or `submit letter ...`). It intentionally replaces the JSON prisoner-response instructions below; see [prompts/prisoner/base.md](prompts/prisoner/base.md), [README.md](README.md), and [docs/implementation_choices.md](docs/implementation_choices.md) for the current interface. The researcher phase and essay-first design are unchanged.

**Scope:** Build an auditable scaffold for an *early test* of the essay-first decision-theory experiment. Prioritize source acquisition, exact prompt templates, prompt rendering, and a safe OpenRouter adapter. **Do not run a paid batch, choose models on the researcher's behalf, or push to GitHub unless explicitly asked.**

Read `docs/design_v03.md` for the research design. It is authoritative for the experiment; if a proposed implementation choice is underdetermined, record the choice and surface it for review. The prompt files in this package are initial drafts, not frozen research instruments. Keep them as separate readable files, and make edits in those files rather than hiding prompts in application code.

## Goal of the main experiment

For each named decision-theory assignment (CDT, EDT, FDT Equation 4, FDT footnote 16):

1. Provide a **human-written source article** to an LLM researcher. The researcher writes a substantive mathematical essay or technical blog post explaining the theory and how to apply it generally. The researcher is **not told about the upcoming almost-twin PD experiment**. Examples are welcome if they arise naturally.
2. Save the essay verbatim. Independently instantiate **two prisoner copies of the same model**, both with the exact same essay, common game text, theory label, decoding settings, and application effort. Give them only different *private observation* fields where that condition calls for differences.
3. Each prisoner makes an actual, irreversible **simulated** decision to SUBMIT or WITHHOLD incriminating evidence. The harness commits the action to a local simulated game state and scores the outcome. Neither prisoner sees the other's response first.

**Mainline prisoners receive the researcher essay only** as their theoretical reference. They do **not** receive the original human-written paper in the mainline. Preserve two optional controls for later: (a) essay + original paper, (b) direct paper to prisoner without a researcher essay. Do not implement those as hidden defaults.

## Immediate deliverables (priority order)

### 1. Sources are reproducibly downloaded and readable

Implement a `fetch-sources` command reading `sources/manifest.yaml`. Fetch and normalize sources to a gitignored local cache such as `data/source_cache/{cdt,edt,fdt}/`, preserving raw bytes and generating a human-inspectable `article.md` for each source. Write a machine-readable provenance record: URL, revision, retrieval UTC timestamp, SHA-256 of raw and normalized files, extractor version/command, warnings, and text statistics.

Initial sources:

- **CDT:** Stanford Encyclopedia of Philosophy, *Causal Decision Theory* — https://plato.stanford.edu/entries/decision-causal/
- **EDT:** Stanford Encyclopedia of Philosophy, *Decision Theory*, notably §3.2 on Jeffrey's theory — https://plato.stanford.edu/entries/decision-theory/
- **FDT:** Yudkowsky & Soares, *Functional Decision Theory* arXiv:1710.05060v2 — https://arxiv.org/abs/1710.05060 ; **first attempt TeX source:** https://arxiv.org/src/1710.05060 (arXiv lists a TeX Source link); **fallback PDF:** https://arxiv.org/pdf/1710.05060v2

For **SEP**, download HTML and extract the article body into Markdown/text without LLM rewriting. Preserve headings, formula representations, examples, and meaningful footnotes. The EDT source is not a dedicated SEP entry; document its precise coverage rather than pretending it is. Do not silently substitute an unrelated source if extraction proves inadequate.

For **FDT**, attempt the arXiv source archive **before anything involving OCR**. Sniff whether the downloaded body is gzip, tar.gz, or a single compressed TeX file; unpack safely (reject absolute paths and `../` entries), locate the main TeX document and its included files, and convert to an inspectable Markdown/text version while retaining mathematical display expressions and footnotes. Pandoc/LaTeXML can be used if available; document the conversion path. If source conversion fails, fall back to `pdftotext -layout` on the PDF, and only consider OCR if the PDF is genuinely non-textual. Do **not** hallucinate or reconstruct missing equations with an LLM.

Add source-quality checks. The normalized FDT material must visibly retain **Equation (4), its observation-indexed decision variable, the discussion of graph construction, and footnote 16 on policy selection**; show those passages in a local QA report (without printing all copyrighted content in a public artifact). Verify the SEP articles contain the expected theory sections. Fail clearly on incomplete extraction, truncation, empty files, or download errors. The user must be able to open `article.md` files locally and verify them before using them in prompts.

**Copyright and third-party processing:** Downloaded SEP full text is for local use; its terms permit personal downloads but tightly restrict electronic redistribution. Keep raw and normalized full-text source files out of git and out of published results by default. **Before a live OpenRouter request that transmits full human-written articles to an external model provider, flag this as a source-license/terms question for the user to resolve; do not assume personal download rights automatically authorize third-party API transmission.** If necessary, identify a suitable open-license alternative source rather than silently changing materials. Commit only source URLs, download/extraction scripts, hashes/metadata, and short compliant quotations as needed. Treat the FDT paper's license individually; do not assume arXiv's download availability means blanket redistribution permission.

### 2. Prompts must be ordinary files, reviewable before execution

Keep these files (and any later revisions) directly under `prompts/`:

- `researcher/base.md`: general mathematical essay/blog-post assignment with `{{THEORY_NAME}}`, `{{FOCUS_INSTRUCTION}}`, and `{{SOURCE_TEXT}}`.
- `researcher/fdt_eq4_focus.md`: brief source-reading emphasis on Equation (4), not an imposed interpretation.
- `researcher/fdt_policy_focus.md`: brief source-reading emphasis on footnote 16, without specifying policy timing, role symmetry, or payoff aggregation.
- `prisoner/base.md`: common legal game, same-algorithm premise, selfish utility and irreversible evidence commitment, with `{{ESSAY_TEXT}}`, `{{OBSERVATION_RELATION}}`, and `{{PRIVATE_OBSERVATION}}`.
- `prisoner/observation_cases.yaml`: machine-readable T0 identical and T2 different-name cases; later T1 nonce/T3 cell cases.
- `controls/direct_article.md`: optional direct-paper condition, separate from the mainline.

These files are already drafted in this package. Preserve their distinction between the reader/researcher and prisoner phases. **Do not leak hypotheses, case details, or even the term “almost-twin” into the researcher request.** The source article itself may naturally contain an ordinary perfect-twin example; do not censor it. Do not forbid the researcher from supplying its own examples.

Implement a `render-prompts` command that works **offline**, reads these files verbatim, substitutes known placeholders, and writes the **complete model-visible messages** in easy-to-read Markdown and JSON under `data/rendered_prompts/` (gitignored by default because they can contain human-written source text). Include a `--demo` mode with an obviously synthetic essay fixture, not mislabeled as a model-generated research result. Include rendered-message SHA-256 hashes and prompt-template hashes.

Two prisoner renderings for a given pair must be **byte-identical outside the private-observation field**. In T0 they should be entirely identical. Internal role IDs, filenames, random seeds, and metadata must not accidentally leak into the model-visible prompt. Unit-test this property.

### 3. Thin OpenRouter runner (after prompts are inspectable)

Use the user's `OPENROUTER_API_KEY` environment variable; support a gitignored `.env` file but never commit a key. A straightforward Python CLI with a small number of dependencies is fine. Use OpenRouter's `POST https://openrouter.ai/api/v1/chat/completions` (or its documented equivalent) rather than multiple ad hoc provider APIs. No need for a full eval framework in this sprint.

Support:

- `researcher` stage: in-context normalized human-written source → full natural-language essay. Save **entire** output, exact request payload, source hash, finish reason, usage, and model/provider metadata.
- `prisoner` stage: frozen essay → two **independent** calls. Store commitment and short public justification. No shared conversation state containing the other prisoner's action; no sequential “now decide as prisoner 2” continuation.
- Configurable model ID and **distinct researcher effort `e_R` and application effort `e_A`**. Use OpenRouter's documented `reasoning: {effort: ...}` or equivalent supported shorthand; never send contradictory fields.
- Validate selected model/provider support for requested reasoning effort, output format, and context length **before** spending credits. Set `provider.require_parameters: true` where supported; avoid silent fallback or ignored reasoning parameters. Record actual provider/route when available, and do not silently substitute a different model.
- Provider-appropriate generation limits for a substantial essay and a short prisoner response; don't silently truncate source or essay. Make optional temperature/seed behavior explicit and validate support.
- Exact raw responses; JSONL append-only logs with `essay_id`, `scenario_id`, role, template hashes, source hashes, model/version, effort, token usage, finish reason, errors, and committed action. Preserve invalid or ambiguous outputs as failures; never turn them into C or D by guesswork.
- A tiny local state machine that treats a valid `SUBMIT` or `WITHHOLD` as an **irreversible fictional commitment**, scores the sentence table, and records the pair outcome. It must not contact a real prosecutor, witness, lawyer, court, or other person.

**Safety/budget defaults:** Commands must be no-network and no-paid-API by default. Require both a configured key **and an explicit `--execute` / `--confirm-billable` flag** to make an OpenRouter generation request. Add a configurable maximum call count and estimated spending cap, with a dry-run cost estimate when possible. Do not run the full 48-essay/384-prisoner pilot in Sprint 01. Stop at a reviewable dry-run and optionally one very small user-approved live smoke test.

### 4. Transparency and tests

Provide tests for:

- Exact researcher prompt contains source + theory focus but **no benchmark/game fields**.
- Within each pair the **same frozen essay** is sent verbatim; prisoner prompts differ only in the intended private block (T0 prompts identical).
- T0 and T2 scenario renderings match the intended selfish payoff table and action mapping.
- An action can't be retracted, and scoring is symmetric.
- An unsupported reasoning setting, missing source, absent API key (for live mode), invalid output, and incomplete source extraction fail visibly without fictitious “successful” records.
- Offline dry-run and rendered-prompt inspection work without credentials.

Maintain `docs/hypotheses.md` separately from **all model-visible prompts**. The experimenter's predictions are:

- CDT normally defects.
- EDT cooperates substantially in low-reasoning settings.
- EDT at high effort and with different observations: no strong prediction.
- FDT at low effort: no strong prediction.
- FDT at high effort with different observations: usually defects.

Do not tune prompts to make these predictions come true. They are for later preregistration/interpretation, not for the agents.

## Acceptance criteria for this sprint

1. A human can read the full researcher and prisoner prompt templates as plain files, without running code.
2. A local `fetch-sources` run can produce readable, versioned CDT/EDT/FDT sources, including a mathematical-quality check of the FDT equation and policy footnote, or an explicit diagnostic explaining what could not be obtained.
3. A no-key/no-network `render-prompts --demo` can display the **exact intended staged procedure**, with one essay shared across two independently rendered prisoner requests.
4. The OpenRouter configuration surface and minimal request path are visible and documented; no money is spent without explicit authorization.
5. The README describes exactly which files the user should review before the first live test, what choices remain open (models/efforts), and what was/was not implemented.
6. Do not add optimization, large-scale statistics, automated grading, web dashboards, or a publication pipeline yet. Keep this small and transparent.

**End-of-sprint handoff:** Show the source extraction report and the **rendered researcher prompt, both rendered prisoner prompts, and their precise diff** for one T0 and one T2 case. State any source/formatting ambiguity explicitly and wait for manual prompt approval before scaling.

## Current reference links

- OpenRouter chat API: https://openrouter.ai/docs/api/api-reference/chat/create-a-chat-completion
- OpenRouter provider/effort caveat: https://openrouter.ai/blog/tutorials/how-to-test-tool-calling-accuracy-in-ai-agents/
- SEP terms: https://plato.stanford.edu/info.html
- arXiv FDT v2: https://arxiv.org/abs/1710.05060
