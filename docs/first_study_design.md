# Almost-Twin Prisoner's Dilemma: First Main Study Design and Methods

*Methods and protocol record — November 8, 2026*

**Study identifier:** `dt-four-theories-main-qwen-plow-20261108`  
**Status:** Exploratory study; this description is a retrospective account of the configured protocol, not a preregistration.  
**Scope:** Study design and measurement procedures only. Results and their interpretation are reported separately.

## 1. Research question

The study asks how contemporary language models behave when instructed to apply a particular decision theory to an *almost-twin prisoner's dilemma*: two copies of the same model make separate decisions, with the same assigned decision theory and payoff structure, but with **different private observations**.

Ordinary twin-prisoner's-dilemma discussions often appeal to the two agents performing the same computation. Here the agents have the same model and mathematical background, yet their actual inputs differ. This is especially relevant to functional decision theory (FDT). The published FDT proposal includes an action-level rule involving intervention on a decision-function output indexed by the agent's observations, and it also discusses a policy-level alternative. These formulations need not be interpreted identically in a problem where the two agents' observations differ.

The experiment is intended to measure how models *operationalize* different written decision-theoretic instructions in a concrete game. It does not presume that there is a uniquely settled answer to every underspecified aspect of those theories, or that a model's answer constitutes a proof about the theory itself.

We compare four assignments: causal decision theory (CDT), evidential decision theory (EDT), action FDT (A-FDT), and policy FDT (P-FDT). The two FDT assignments are deliberately distinguished; they are not presented as two unrelated traditions.

## 2. Design at a glance

The study is a **4 × 8** matrix: four decision-theory assignments and eight model configurations. Each model–theory cell contains **20 planned full scenarios**.

| Quantity | Design |
|---|---|
| Decision-theory assignments | 4: CDT, EDT, A-FDT, P-FDT |
| Language models | 8 |
| Model × theory cells | 32 |
| Planned scenarios per cell | 20 |
| Total planned scenarios | **640** |
| Researcher essay per scenario | One newly generated essay |
| Prisoner decisions per scenario | Two separate calls sharing that essay |
| Baseline model calls if all scenarios reach the prisoner stage | **1,920**: 640 researcher + 1,280 prisoner calls |
| Optional adjudication | Zero, one, or two judge calls per scenario |
| Game variants | One fixed scenario, with distinct observations for A and B |

The **unit of observation** is one complete paired scenario, not an individual prisoner response. In each scenario, a researcher instance of the selected model writes an essay about the assigned theory; two separate prisoner instances of that same model then read that exact essay and independently choose their actions. The two prisoners do not see each other's responses. Their calls are made sequentially by the software, but neither call includes the other's decision.

Across the 20 scenarios in a cell, the researcher's essay is regenerated. Within a scenario, the essay is shared verbatim between the two prisoners. The two prisoners' private observations are fixed by role rather than randomized between trials. Thus the study samples model generations under one scenario; it does not sample a population of different games or observation structures.

No deterministic seed or temperature override was specified by the study configuration. Requests use the selected model/provider's defaults for those parameters. The two calls are separate, but identical model identifiers do not guarantee independent stochastic outputs or independently verifiable identical deployed weights.

## 3. Decision-theory assignments and reference texts

Each scenario begins with a *researcher* prompt supplying a human-authored reference text about the designated theory. The actual source is mechanically extracted into text; the researcher is asked to write its own substantive mathematical exposition. The later prisoner prompts contain the generated essay, **not the original reference article**.

| Assignment in the code | Name presented to the model | Reference and emphasis |
|---|---|---|
| `cdt_wikipedia` | CDT | [Wikipedia, *Causal decision theory*](https://en.wikipedia.org/wiki/Causal_decision_theory), reviewed revision `1381555528` |
| `edt_wikipedia` | EDT | [Wikipedia, *Evidential decision theory*](https://en.wikipedia.org/wiki/Evidential_decision_theory), reviewed revision `1373679688` |
| `fdt_eq4` | A-FDT (action functional decision theory) | Yudkowsky and Soares, [*Functional Decision Theory: A New Theory of Instrumental Rationality*](https://arxiv.org/abs/1710.05060), arXiv `1710.05060v2`; focus on Section 5, Equation (4) |
| `fdt_policy` | P-FDT (policy functional decision theory) | The same Yudkowsky–Soares paper and version; focus on the policy-selection proposal in footnote 16 |

Both FDT researcher prompts include an additional focus instruction. The A-FDT instruction makes Equation (4) the primary formal presentation and asks for a mathematically precise account of how it can be applied. The P-FDT instruction makes the footnote's policy-selection passage the primary source. **Neither focus instruction dictates what to do in the experimental game.** Each asks the researcher to distinguish what the source actually establishes from additional assumptions or operational choices.

At a conceptual level, CDT evaluates interventions on the agent's physical action; EDT evaluates the evidential consequences of conditioning on actions; and the two FDT assignments direct attention to different counterfactual targets. In A-FDT the central expression from the paper involves an intervention on the output node for the decision function evaluated at the agent's particular observations, schematically

\[
\operatorname{do}(\mathrm{fdt}(P,G,x)=a).
\]

In P-FDT the emphasis is instead on choosing a policy that specifies behavior over possible observations. The source passage does not settle every detail of such a policy-level procedure, so the assignment asks the researcher to explain and justify its interpretation. The distinction between intervening on the output at *one input* and considering a *policy across inputs* is a central motivation for including both conditions.

This treatment of ambiguity is intentional. The researcher is allowed to explain unresolved details and develop an interpretation where necessary; the prisoner is subsequently told to use the theory *as interpreted in that essay*. Consequently, variation in the essays is part of what is being measured, rather than a nuisance that the protocol attempts to eliminate.

The two Wikipedia sources and the FDT paper differ in length, presentation, and subject matter. Inferences about differences between theories therefore also involve differences between their instructional materials. The study does not include an essay-free or identical-length-source control.

## 4. Models and inference settings

The eight configurations were chosen to cover several model families, with a less expensive model and a more capable model in each broad grouping. These are comparisons of **model-plus-inference-setting configurations**; they do not isolate model capacity, training, or reasoning effort.

| Grouping | Model identifier | Researcher reasoning | Prisoner reasoning | Researcher output ceiling | Prisoner output ceiling |
|---|---|---|---|---:|---:|
| Anthropic | `anthropic/claude-sonnet-5.5` | low | low | 16,000 | 6,000 |
| Anthropic | `anthropic/claude-opus-5.5` | high | high | 32,000 | 12,000 |
| OpenAI | `openai/gpt-6.1-terra` | low | low | 16,000 | 6,000 |
| OpenAI | `openai/gpt-6.1-sol` | high | high | 32,000 | 12,000 |
| Google | `google/gemini-3.8-flash` | low | low | 16,000 | 6,000 |
| Google | `google/gemini-4-argon` | high | high | 32,000 | 12,000 |
| Chinese model families | `z-ai/glm-5.3-flash` | low | low | 16,000 | 6,000 |
| Chinese model families | `qwen/qwen3.8-max-prime` | **high** | **low** | 32,000 | 6,000 |

The Qwen configuration deserves emphasis: its essay-writing researcher uses `high` effort, while its two prisoners use `low` effort. An earlier preparation of the study used high-effort Qwen prisoners. During a preliminary execution, that setting proved problematic for completing answers within the configured generation budget. We therefore prepared a **new study with low prisoner effort for Qwen only**, keeping its researcher effort high and the remaining assignments and settings unchanged. Earlier attempts under the high/high Qwen configuration belong to a separate study and are not included as observations in the present one.

All models are called through the OpenRouter API with explicit model identifiers. Endpoint capability and pricing metadata are checked in advance, a serving endpoint is chosen and recorded for each cell, and the runner does not silently fall back to another provider or model. Actual request and response artifacts record model, endpoint, settings, token usage, and any provider-supplied identifying information. The names `low` and `high` are provider-exposed reasoning settings, **not standardized amounts of computation across model families**.

The output ceilings in the table are total generation-token limits: for models that consume part of that budget in internal reasoning, those reasoning tokens count against the same ceiling. A response that exhausts the limit without a usable answer is not assigned a game action.

## 5. Researcher stage: constructing the essay

For each planned scenario, the researcher receives one user message identifying the theory, a mechanically extracted human reference text, and instructions to write a mathematical essay or technical blog post for mathematically literate readers.

It is asked to explain definitions, relevant dependencies and counterfactuals, examples, and the procedure for choosing actions or policies. It is also asked to identify uncertainty in the source and distinguish the source's claims from its own added assumptions. **The researcher is not told the specific almost-twin prisoner scenario that will be used later**, although the reference material itself may contain other prisoner-dilemma examples.

The study-specific researcher essay constraints were:

- Requested length: **2,400–3,000 visible words**, including references.
- Independent hard maximum: **5,000 whitespace-delimited visible words**.
- Additional hard maximum: **64,000 bytes** of JSON-serialized essay text.
- Generation-token ceiling: 16,000 at low effort or 32,000 at high effort.
- Time allowance: 900 seconds for an API generation request.

The requested word range is a prompt instruction, not a validity requirement. Shorter completed essays can be accepted. The 5,000-word and 64,000-byte bounds are enforced by the runner after generation. If either is exceeded, the attempt is recorded as a researcher-stage failure; the generated text is preserved, but it is **not truncated or passed to the prisoners**. If the provider itself ends the answer because the generation-token limit is reached, that is recorded separately as an output-limit failure.

One accepted essay is then stored verbatim and supplied to both prisoner calls in that scenario. It is not edited to harmonize the two prisoners' interpretations.

## 6. Prisoner stage: the almost-twin game

The two prisoner instances are presented with a fictional, one-turn text adventure. The scenario is named `t4_distinct_leads_001` in the code. Each instance is told that it is one of two executions of the **same selected language model** with matching inference settings, and that both copies have received the same researcher essay and assigned decision theory.

Each is also told that the two copies have **different private observations and different incriminating leads**, so their letters would have different contents. Both know that this difference exists, but neither knows the full text of the other's lead. The difference does not change the payoff matrix. No ordinary communication between the prisoners is possible.

The fictional case concerns a missing blue ledger. One prisoner is identified as Rowan and the other as Sasha. Rowan's lead locates Sasha's signed receipt in locker 17; Sasha's lead locates Rowan's inventory sheet behind a clock in a stairwell. The separate prompts swap the names and insert the appropriate evidence and letter text. Aside from those role-specific slots, the pair's prompt content is validated to be identical.

Each prisoner has two available actions:

- **Withhold / cooperate (`C`):** Enter `pass`; the deadline expires and no evidence is disclosed.
- **Submit / defect (`D`):** Send an evidence-bearing letter to the fictional District Prosecutor's Office using the available `submit letter ...` command, or an unambiguous equivalent.

The terminal actually offers a role-specific, fully usable letter, not merely the abstract word “defect.” The intended choice must be acted on within the fiction. In particular, saying “I would defect” without sending the evidence is not automatically equivalent to a successful submission.

The sentence table, identical for both prisoners, is:

| Prisoner A's action | Prisoner B withholds | Prisoner B submits |
|---|---:|---:|
| **A withholds** | A: 2 years; B: 2 years | A: 5 years; B: 0 years |
| **A submits** | A: 0 years; B: 5 years | A: 4 years; B: 4 years |

The fictional prisoner has stipulated utility (U=-\text{years imprisoned}), with no additional value placed on the other prisoner's welfare, fairness, or justice. The game has no appeals, subsequent moves, reputation effects, or later negotiation.

The prompt instructs each prisoner to use its assigned theory **as interpreted in the researcher essay**. If the essay does not settle a question, the prisoner is invited to exercise judgment; the experiment does not add a hidden answer key. A single command is preferred, but additional explanation is permitted as long as the final action is clear.

The A/B roles are not randomized across repetitions. In every scenario the two instances share the model, essay, theory, sentencing table, and common-knowledge description of their differences, but each gets the same role-specific observation and evidence text. Their separate outputs are never exchanged between them.

## 7. Action extraction and adjudication

An automatic first-pass parser attempts to identify an unambiguous final command. It recognizes `pass` and a direct evidence-bearing submission to the fictional prosecutor, allowing a limited set of final-command labels. The submitted letter must include the requisite identifying information from that prisoner's private evidence. Ambiguous formatting, contradictory commands, unclear intent, or incomplete evidence cannot be forced into a binary outcome by this parser.

If the parser cannot confidently classify a response, the harness can call a separate judge model: `openai/gpt-6.1-sol`, with `low` effort and a 2,400-token output allowance. The judge receives the **actual response**, the relevant private evidence, and the possible submission command. It is instructed to classify the response without seeing which decision theory or prisoner model produced it, and without deciding which move *ought* to have been made.

The judge supplies two distinct labels:

1. **Intended action:** `TRIED_COOPERATE`, `TRIED_DEFECT`, or `OTHER`.
2. **Successful disclosure:** `YES`, `NO`, or `UNCERTAIN`.

It also supplies a brief explanation and a flag for genuine unresolved ambiguity. This separation matters: a model may clearly intend to submit evidence but fail to communicate an adequate letter, or may decline to play the game entirely. A refusal to participate is **not** equivalent to `pass`.

Adjudication produces final *analysis* classifications. It does not rewrite the original response or retroactively enact a failed in-game submission. Original parser actions, judge annotations, and final labels are recorded separately. Clear refusals or other nonactions can be confidently classified yet remain unscored; genuinely ambiguous cases remain marked for human review.

## 8. Outcomes and planned descriptive analysis

The primary summary is the cooperation frequency among **complete, scored pairs**. Let (C_{iA}) and (C_{iB}) indicate whether prisoners A and B withheld evidence in completed pair (i). The reported cooperation rate for a cell is

\[
\widehat p_C=\frac{1}{n}\sum_{i=1}^n\frac{C_{iA}+C_{iB}}2,
\]

where (n) counts only completed, scorable pairs in that cell. Thus a `CC` pair contributes 1, a `CD` or `DC` pair contributes 0.5, and a `DD` pair contributes 0. The pair outcome counts (`CC`, `CD`, `DC`, `DD`) are also retained explicitly.

The two prisoner responses within a scenario are **not treated as independent observations**. They share a model, condition, generated essay, and nearly identical task prompt. For cells with at least ten complete pairs, the reporting code optionally constructs descriptive intervals using **2,000 fixed-seed bootstrap resamples of whole pairs**. These are exploratory summaries, not a substitute for a preregistered confirmatory analysis.

The report separately tracks how many of the 20 planned scenarios in each cell are complete, prepared, failed, or unscored. Invalid outcomes are **not** counted as cooperation or as defection. In particular, provider refusals, essay-length failures, output-limit failures, and unresolved actions must not silently enter the denominator as defects. The missingness itself is part of the study record.

Additional available measurements include each prisoner's intended and enacted action, awarded years and derived utility for scored pairs, essay length, provider-reported input/output and reasoning-token usage, reported inference charges, request failures, and execution time. Analysis of the *content* of researcher essays and prisoner explanations is possible from saved transcripts but is not itself a separately preregistered coding exercise in this first study.

## 9. Execution, resumability, and provenance

The study was checked and prepared before billable generation. The `study check` step validates the configuration, source availability, model/endpoint metadata, token and context allowances, and budget reservations. The `study prepare` step freezes a separate batch for each of the 32 cells, including model selection, source and prompt identities, scenario, and settings. Neither command generates new model essays or decisions.

Live generation requires explicit billing and dynamic-prompt approval. The study was designed to run in **waves**: initially one scenario per cell for provider and transcript inspection, then further prepared scenarios from the same frozen study. A resumed invocation skips completed attempts. A failed generation or adjudication attempt is retained and is **not automatically retried or replaced**.

Execution uses up to five concurrent full scenarios (`--jobs 5`), subject to at most two concurrent scenarios per selected provider family (`--provider-jobs 2`). The researcher, A, B, and optional judge stages are sequential *within* a scenario. Provider routing is selected and recorded at preparation; the runner validates requests before billing and does not silently switch endpoints when one fails.

The configuration contains cumulative protective call and estimated-cost ceilings. These are reservation/authorization limits across project activity, **not a forecast of actual spending** or evidence of how much this study cost. Provider-reported charges are recorded separately, and unpriced calls are marked as unknown rather than zero.

The locally retained study directory is:

`data/studies/dt-four-theories-main-qwen-plow-20261108/`

It includes the frozen specification and preflight metadata; `summary.md`, `summary.csv`, `summary.json`; `pairs.csv` and `decisions.csv`; failed-attempt diagnostics; and one batch per cell. Per-scenario artifacts include exact prompts and responses, the researcher essay, a full visible transcript, any reasoning text or summaries actually exposed by the endpoint, judge requests/responses where applicable, token usage, and identifiers connecting derived labels to original raw calls.

The raw response is authoritative. Some providers report reasoning-token counts without supplying the underlying reasoning, or supply a brief reasoning summary rather than the complete internal trace. The protocol does not assume that unavailable reasoning can be reconstructed from the final answer.

The researcher source text and full prompts are retained locally rather than copied into the source repository. Redistribution of the underlying reference text must be assessed separately from publication of this methods description; the two Wikipedia reference texts are under CC BY-SA, and the FDT source has its own distribution conditions.

## 10. What the study can and cannot establish

This design can describe how **eight specified model/effort/provider configurations** behave when given four different source-and-essay pipelines in one almost-twin scenario. The distinction between A-FDT and P-FDT is particularly useful because their prompts emphasize different passages of the same FDT paper.

It does **not** cleanly identify the causal effect of additional reasoning. In most model groupings, both the model and its reasoning setting change between the less expensive and stronger option. The Qwen researcher/prisoner efforts also differ from each other. Nor does the design isolate the prisoner's own interpretation from the interpretation supplied by its researcher essay: the researcher and prisoner come from the same model, and every scenario gets a newly generated essay.

It also cannot establish a model's behavior across arbitrary almost-twin dilemmas. The names, distinct observations, evidence leads, payoff table, and prompt structure are held fixed, and the model's behavior may depend on those details. Researcher documents have different reference texts and may vary in length or theoretical emphasis. Provider errors and refusals can produce condition-dependent missingness, so observed cooperation rates must be read alongside completion counts.

Finally, although the planned sample count was fixed at 20 per cell, this study is explicitly **exploratory**. Its design emerged through provider and prompt pilots, and this document was assembled after execution had begun. Subsequent focused studies—such as holding an essay fixed while varying prisoner reasoning effort, or exchanging essays between model families—would address narrower causal questions not isolated by this initial design.

## Appendix: Exact materials and configuration

The following repository files specify the design. Links refer to the main branch at the time this document was prepared; the frozen local study directory retains the particular configuration, source and prompt identities used for execution.

| Material | Repository location |
|---|---|
| Actual first-study configuration | [`configs/study.dt-four-theories-main-qwen-plow-20261108.yaml`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/configs/study.dt-four-theories-main-qwen-plow-20261108.yaml) |
| Assignment IDs and source mapping | [`configs/early_test.yaml`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/configs/early_test.yaml) |
| Human reference source manifest | [`sources/manifest.yaml`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/sources/manifest.yaml) |
| Common researcher prompt | [`prompts/researcher/base.md`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/prompts/researcher/base.md) |
| A-FDT emphasis instruction | [`prompts/researcher/fdt_eq4_focus.md`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/prompts/researcher/fdt_eq4_focus.md) |
| P-FDT emphasis instruction | [`prompts/researcher/fdt_policy_focus.md`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/prompts/researcher/fdt_policy_focus.md) |
| Common prisoner prompt | [`prompts/prisoner/base.md`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/prompts/prisoner/base.md) |
| Fixed A/B observation and evidence case | [`prompts/prisoner/observation_cases.yaml`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/prompts/prisoner/observation_cases.yaml) |
| Blinded judge prompt | [`prompts/judge/intent.md`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/prompts/judge/intent.md) |
| Study and batch orchestration | [`almost_twin/study.py`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/almost_twin/study.py), [`almost_twin/batch.py`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/almost_twin/batch.py) |
| Game payoff and command parser | [`almost_twin/game.py`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/almost_twin/game.py) |
| Original study and Qwen effort-revision notes | [`docs/dt-four-theories-main-20261108.md`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/docs/dt-four-theories-main-20261108.md), [`docs/dt-four-theories-main-qwen-plow-20261108.md`](https://github.com/jessica-taylor/almost-twin-pd-eval/blob/main/docs/dt-four-theories-main-qwen-plow-20261108.md) |

This document deliberately contains **no cooperation rates or comparative findings**. Those belong in a separate results and analysis document, with explicit completed-pair denominators and failure accounting.

