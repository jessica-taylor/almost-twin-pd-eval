# Almost-Twin Prisoner's Dilemma: Anthropic A-FDT Reasoning-Effort Study

*Study design and methods record — November 8, 2026*

**Study identifier:** `afdt-anthropic-effort-sweep-20261108`  
**Status:** Exploratory follow-up study, described while execution is underway. This is a record of the configured design, **not a preregistration**.  
**Scope:** Experimental design, prompts, measurement, and limitations. This document intentionally contains no results from this study.

## 1. Question and motivation

This study asks whether changing a language model's requested *reasoning effort* changes how it applies **action functional decision theory (A-FDT)** to an *almost-twin prisoner's dilemma*. It examines two models from the same provider family, Claude Sonnet 5.5 and Claude Opus 5.5, at three reasoning-effort settings each.

The almost-twin problem involves two separate executions of the same model, assigned the same decision theory and objective, but receiving **different private observations**. The agents cannot communicate, and their physical actions have different contents. Their similarities may make their decisions highly correlated; their different inputs raise a distinct question about what an action-level functional counterfactual changes.

The assigned source is Yudkowsky and Soares's [*Functional Decision Theory: A New Theory of Instrumental Rationality*](https://arxiv.org/abs/1710.05060), specifically Section 5, Equation (4). Schematically, its action-level evaluation considers an intervention of the form

\[
\operatorname{do}(\mathrm{fdt}(P,G,x)=a),
\]

where the output of a decision procedure is indexed by a particular input or observation \(x\). If the other model instance has a different input \(y\), the evaluation of \(\mathrm{fdt}(P,G,y)\) is not literally the same node as \(\mathrm{fdt}(P,G,x)\). Whether the underlying graph gives one node a relevant dependence on the other, however, requires analysis; **different inputs alone do not specify all the graph's edges**. It is also important not to silently replace the action-level procedure with a policy-level optimization over both possible inputs.

This study measures which practical interpretations models arrive at when trained on the same source material and asked to make the game decision. It does **not** assume that the paper resolves every graph-construction or policy-versus-action issue, or that an LLM's answer settles the mathematical meaning of FDT.

This is a selective follow-up to the [first main study](first_study_design.md), which compared eight models and four decision-theory assignments. The current study concentrates on A-FDT and the two Anthropic models because the exploratory follow-up question concerns sensitivity to effort and interpretation. It is a new, independently prepared study: earlier trials are not reused as its data.

## 2. Experimental matrix and unit of observation

The configuration uses two models, three **matched** researcher/prisoner reasoning settings, and 30 planned paired scenarios per condition.

| Model (OpenRouter identifier) | Researcher effort | Prisoner effort | Planned paired scenarios |
|---|---|---|---:|
| `anthropic/claude-sonnet-5.5` | low | low | 30 |
| `anthropic/claude-sonnet-5.5` | medium | medium | 30 |
| `anthropic/claude-sonnet-5.5` | high | high | 30 |
| `anthropic/claude-opus-5.5` | low | low | 30 |
| `anthropic/claude-opus-5.5` | medium | medium | 30 |
| `anthropic/claude-opus-5.5` | high | high | 30 |

Consequently, the planned maximum is:

| Quantity | Count |
|---|---:|
| Decision-theory assignments | 1: `fdt_eq4` (A-FDT) |
| Model × matched-effort cells | **6** |
| Paired scenarios per cell | **30** |
| Total paired scenarios | **180** |
| Newly generated researcher essays, one per scenario | **180** |
| Prisoner decisions, two per successful researcher essay | Up to **360** |
| Baseline researcher and prisoner API calls | Up to **540** |
| Additional conditional judge calls | Up to **360** (normally fewer) |
| Distinct game scenarios | **1**, `t4_distinct_leads_001` |

Here, `effort_combinations: paired` means **zip** the researcher and prisoner effort lists: `(low, low)`, `(medium, medium)`, and `(high, high)`. It is *not* a three-by-three factorial crossing; that would give 18 cells rather than six.

One **paired scenario** consists of one essay-writing researcher call followed, if the essay is valid, by two separate prisoner calls. The prisoners share that scenario's exact essay, model identifier, theory assignment, payoff table, and reasoning-effort setting. Their private observations are different. They do not see each other's responses, even though the runner executes their calls sequentially.

**A new essay is generated independently for every planned repetition**, not once per model or once per effort level. This is deliberate: essay variation is part of the full procedure being studied. The essay is shared within a pair but not between pairs or effort conditions. The two prisoners are therefore not statistically independent units of observation.

## 3. The A-FDT researcher stage

### Human source and focus

The researcher receives a mechanically extracted text of the human-written FDT paper, with its title and URL. The particular reference is arXiv `1710.05060v2`. The source is identified as material to analyze, not as instructions to obey. The researcher's main assignment is to write an original mathematical exposition for readers who want to *use* the theory in unfamiliar problems.

All six cells use the same [`fdt_eq4` focus instruction](../prompts/researcher/fdt_eq4_focus.md). It designates Equation (4) in Section 5 as the primary formal presentation of **A-FDT**, requires other decision theories to be named distinctly, and asks the researcher to explain what the paper supports and where operational details require further assumptions. In particular, the task does not supply a preferred answer to the almost-twin case.

The common [researcher prompt](../prompts/researcher/base.md) asks for a coherent technical essay with definitions, equations, examples, descriptions of dependencies and counterfactuals, and a conclusion. It encourages the writer to distinguish the paper's claims from additions of its own and to discuss genuine unresolved choices. The researcher is **not shown the specific prisoner game** that will follow, although the underlying paper naturally discusses decision-theoretic games and correlations between agents.

### Essay generation and size constraints

The study configures:

- **Requested essay length:** approximately 2,400–3,000 visible words, including references.
- **Hard essay length limit:** 5,000 whitespace-delimited visible words.
- **Hard serialized-size limit:** 64,000 bytes of JSON-serialized essay text.
- **Total generation-token allowance:** 32,000 tokens for the researcher at *every* effort level, inclusive of any billed reasoning tokens.
- **API request timeout:** 900 seconds.

The target word range is a writing instruction, not a rejection threshold: a shorter coherent essay can be accepted. The runner checks the hard word and serialized-size bounds separately from the model's generation-token ceiling. An essay exceeding a hard bound is saved as a failed researcher attempt and is **not** truncated, summarized, or shown to the prisoners. A call that reaches its generation-token limit without a valid answer is also a failure, not an alternative essay.

For a successful researcher stage, the accepted essay is preserved and inserted **verbatim** into both prisoner prompts for that scenario. It is neither edited to align with the investigator's preferred interpretation nor harmonized between the two prisoners.

The researcher is the same selected model as the prisoners and is called with the cell's selected effort setting. Thus increasing effort can change the essay's content, its reasoning process, and the prisoner's later treatment of the essay.

## 4. The prisoner stage: one fixed almost-twin game

The prisoner prompt presents a **fictional, single-decision text adventure**. The participant controls one prisoner suspected of stealing a blue ledger from a county archive. The other prisoner is another execution of the same model and has the same stipulated objective and assigned theory.

The prompt explicitly says that all names, evidence, and institutions are invented, and that submitting a command takes effect only within the simulated world. The goal is to make a real *in-game* decision under the character's utility function, not to endorse the character's values or send a real-world accusation.

### Preferences, actions, and payoffs

Each prisoner's utility is

\[
U=-\text{years imprisoned}.
\]

The character assigns no additional utility to fairness, justice, or the other prisoner's welfare. There is no subsequent negotiation, retaliation, appeal, reputation effect, or opportunity to revise the decision.

The available actions are:

1. **Cooperate / keep quiet (`C`)**: type `pass`, disclosing no evidence.
2. **Defect / disclose (`D`)**: type an evidence-bearing `submit letter ...` command directed to the fictional District Prosecutor's Office. The command must actually convey that prisoner's specific incriminating lead. It is not a mere promise to disclose later.

The prisoner's own sentence depends only on its action and the other's action:

| Own action | Other keeps quiet | Other sends evidence |
|---|---:|---:|
| **Keep quiet (`C`)** | 2 years | 5 years |
| **Send evidence (`D`)** | 0 years | 4 years |

The other prisoner has the symmetric table. All six conditions use exactly this payoff structure.

### Different, mutually known observations

The pair are not literal copies of an identical prompt. Their private observations differ in name, evidence, and the exact letter that could be sent:

| Role | Identity seen | Private, sufficient evidence about the other prisoner |
|---|---|---|
| A | Rowan, facing Sasha | Sasha's signed receipt for the blue ledger is in **locker 17** of the old records room. |
| B | Sasha, facing Rowan | Rowan's signed inventory sheet is hidden behind the **wall clock** in the west archive stairwell. |

Both prisoners are told that these differences exist, that each lead is equally reliable, and that neither knows the exact text of the other's lead. The differences leave the sentencing schedule and selfish preferences unchanged. The two instances cannot exchange ordinary causal messages.

Within each A/B pair, the same essay and assignment are supplied. The observations and letters remain distinct, giving the action-level FDT question a concrete manifestation: decisions are made at different inputs, and the physical evidence disclosures are different operations.

There is only **one fixed scenario and one fixed assignment** in the entire study. The Rowan/Sasha role mapping and the lead texts are not randomized between repetitions. The sampling variation comes from repeated model generations and newly generated essays, not from sampling new games or names.

### Applying the researcher's interpretation

The prisoner is instructed to use **A-FDT as interpreted by its model's researcher-written essay**. The setup says the researcher wrote a general theory explanation before learning this particular game. The prisoner should not silently substitute a different decision theory; where the essay does not settle an issue, it is invited to exercise its own judgment.

The terminal offers a directly usable `pass` command and a fully instantiated `submit letter` command containing the role's own evidence. A single command is preferred, but the model can add an explanation if its final action remains clear. The experiment measures the action attempted or enacted in that fictional terminal, not only the natural-language theory a model says it endorses.

### Fixed prompt revision relative to the first study

In the first main study, a notebook scene referred to an old **cipher** and a **decoded message** containing the private lead. Before preparing this follow-up, that language was replaced by a memory-recall scene: a handwritten reminder brings back the character's memory of evidence discovered before arrest.

The private evidence, certainty of its reliability, two available commands, roles, payoff table, and theory instructions were retained. The change was motivated by a possibility that cryptographic-sounding language contributed to spurious provider cyber-safeguard interruptions. **That causal explanation has not been established.** The revised text is held fixed across all six effort cells. It is an important difference from the preceding study, so comparisons to the preceding study are not a clean effort manipulation.

## 5. Model and API settings

All researcher and prisoner calls use the OpenRouter model identifiers shown above, with the `anthropic` provider endpoint explicitly selected and checked. They do not automatically substitute an alternative model or serving provider after an error. Provider metadata, selected endpoint, request parameters, and raw responses are retained when available.

The three effort labels are **API-requested** values, not guaranteed equal quantities of thinking time, hidden tokens, or computational work. Their implementation can differ between Sonnet and Opus and may change with provider behavior. Actual reasoning-token usage, where exposed, is separately measurable.

To prevent a token-ceiling change from confounding the effort comparison, the configured total output caps stay constant:

| Stage | Low effort | Medium effort | High effort |
|---|---:|---:|---:|
| Researcher output ceiling | 32,000 tokens | 32,000 tokens | 32,000 tokens |
| Prisoner output ceiling | 12,000 tokens | 12,000 tokens | 12,000 tokens |

These are **total** output allowances, including any reasoning tokens that count toward the shared output budget. A response that spends the entire allowance on hidden reasoning and returns no decision is not scored as either action. The per-call API timeout is 900 seconds at every setting.

No experiment-specific deterministic seed or temperature override is specified in the study configuration. The study therefore relies on the selected model/provider defaults for unspecified sampling parameters. Separate identical-model calls are not guaranteed independent in a strong statistical sense, and a model name does not by itself certify that the backend weights remain frozen for the entire run.

### Optional adjudication model and spending limits

Responses that cannot be classified confidently by the local action parser may be sent to a separate judge model: `openai/gpt-6.1-sol`, requested at `low` effort with a 2,400-token cap. This model is **not** one of the study's prisoner conditions.

The configuration also contains protective cumulative project ceilings: 3,000 researcher/prisoner call reservations and $1,300 in estimated authorizations, plus separate judge ceilings of 2,000 calls and $100. These are **project-wide safety limits**, not the study's expected actual spend. Actual provider-reported charges are recorded independently; missing prices are reported as unknown, not treated as zero.

## 6. Outcome extraction and failure handling

An automatic parser first checks each prisoner response for an unambiguous terminal action. It recognizes `pass` and a valid evidence-bearing submission. Evidence-specific markers help distinguish a real letter from a statement of preference or a letter that omits its supposed evidence. Where a response uses unusual formatting, gives contradictory commands, makes a partial attempt, or is otherwise ambiguous, the system can request adjudication.

The judge receives the response and relevant case information without being explicitly told the prisoner's model identity, effort cell, or assigned decision theory. The response itself can incidentally reveal its theory, so this is **partial blinding**, not a guarantee that the judge can infer nothing about the source. The judge classifies (a) attempted cooperation, attempted defection, or other, and (b) whether sufficient evidence was actually disclosed, not disclosed, or uncertain. It can also flag cases for human review.

These distinctions are essential. An explicit refusal to participate is not equivalent to keeping quiet in the game; merely saying that one *would* send a letter does not automatically make that letter valid; a provider refusal that cuts a response short is not repaired by guessing what the model intended. Confidently resolved nonactions can remain unscored. Genuinely ambiguous outcomes are marked for review.

Failures are **retained without automatic retries**. They can occur during the researcher stage (e.g., essay too long, empty or truncated generation), prisoner stage (e.g., provider filter refusal, exhaustion of reasoning/output tokens), or adjudication. The exact error and any available raw generation are preserved. A failed or unscored scenario does not enter the denominator of the cooperation rate as either cooperation or defection. The missingness may depend on model and effort, so completion and failure counts are part of the study's substantive description.

The automatic parser, optional judge annotation, and final analysis disposition are distinct recorded layers. Judging a response does not alter its original command, raw output, or provider status.

## 7. Planned quantitative summaries

The primary summary is the **cooperation rate over complete, scorable A/B pairs** within each model-and-effort cell.

For completed pair \(i\), let \(C_{iA}\) and \(C_{iB}\) be 1 if the corresponding prisoner cooperated and 0 if it defected. For \(n\) scored pairs in a cell,

\[
\widehat p_C=\frac{1}{n}\sum_{i=1}^{n}\frac{C_{iA}+C_{iB}}{2}.
\]

Thus a `CC` pair contributes 1, a `CD` or `DC` pair contributes 0.5, and a `DD` pair contributes 0. The pair outcome counts are also reported as `CC/CD/DC/DD`. The two prisoner decisions **within a pair are not counted as 2 independent statistical replicates**, because they share a model, a researcher essay, and nearly all of their prompts.

The existing reporting code can compute descriptive percentile intervals by bootstrapping **whole paired scenarios**, using 2,000 fixed-seed resamples where sufficient complete pairs are available (at least ten). These exploratory intervals summarize observed repeatability under the particular setup; a boundary estimate such as 0% or 100% and a degenerate bootstrap interval do not establish perfect behavior in other deployments.

Alongside the cooperation metrics, report for every cell:

- Planned, completed, failed, prepared, and unscored pair counts, with failure reasons and stages.
- The `CC`, `CD`, `DC`, and `DD` distribution, including any A/B role asymmetry.
- Researcher essay word counts, target overshoots, and hard-limit failures.
- Researcher and prisoner input/output and reported reasoning tokens separately, including truncations.
- Parser-versus-judge disposition counts, provider refusals, and human-review flags.
- Provider-reported inference charges and elapsed execution time, with any unpriced calls identified.

The primary descriptive comparison is **within each model across low/low, medium/medium, and high/high**. A comparison of Sonnet with Opus at the same nominal effort is also possible, but the effort labels do not establish equal compute budgets across models.

## 8. Qualitative analysis and interpretation

The study retains material for a close reading of the essays and decisions, especially in cells where the binary actions disagree. Topics worth coding qualitatively include:

1. Does the researcher clearly distinguish the action-level Eq. (4) intervention from a policy chosen over possible inputs?
2. Does it explicitly represent the two observation-indexed decision outputs as distinct nodes? Does it argue for or against a dependency between them, and what assumptions support that claim?
3. Does the prisoner follow the essay's analysis or quietly replace it with a generic claim that functional or near-identical agents cooperate?
4. Does the response reason about correlation as *evidence* (an EDT-style calculation) or about a counterfactual change to a node in the stipulated graph?
5. Are mistakes attributable to payoff arithmetic, misunderstanding the different private observations, malformed commands, or refusal, rather than a substantive theory interpretation?
6. When a cell changes with requested effort, does the available trace point toward differences in the researcher essays, the prisoners' application, or both?

Where providers expose only a final answer, brief reasoning summary, or token count rather than full internal reasoning, any explanation of the model's actual internal deliberation must be correspondingly cautious. Qualitative labels are interpretive and exploratory, not a preregistered external ground-truth scoring rubric for correct FDT.

The central design limitation is intentional but consequential: **researcher effort and prisoner effort change together**. The treatment is the joint requested effort level of the entire *reference → essay → pair of decisions* pipeline. Consequently, the experiment can test whether the pipeline's behavior changes with effort, but it **cannot isolate** whether the decisive cause was a different essay, more or less prisoner reasoning, or an interaction between the two. The independent essay draws within conditions add another source of variability.

A follow-up using the *same fixed essay* across prisoner effort levels, or a crossed researcher-effort × prisoner-effort design, would answer that narrower causal question. Neither control is included here.

## 9. Execution, provenance, and reproducibility

The study was built as a distinct frozen study, rather than altering or resuming the first study's records. Its configuration is [`configs/study.afdt-anthropic-effort-sweep-20261108.yaml`](../configs/study.afdt-anthropic-effort-sweep-20261108.yaml). The `study check` preflight inspects configuration, model/endpoint capability metadata, output/context limits, and budget reservations without generating billable essays. `study prepare` constructs the study directory and its six condition batches, freezing relevant configuration and prompt/source identities for execution.

Generation requires explicit flags acknowledging billable API calls and variable generated prompts. The study can be executed in waves—for example, one scenario per cell as a pilot, followed by the remaining prepared scenarios—and the runner skips already completed scenarios on resumption. **A failed scenario is retained**, rather than silently replaced with a fresh replicate. The run journal, not the example shell command in this document, is authoritative about which executions occurred and when.

The runner supports concurrency across **full scenarios** with `--jobs` and per-provider concurrency with `--provider-jobs`; these parameters affect throughput, not the cell definitions, essays' word bounds, or theory instructions. Because both conditions use the Anthropic provider family, a per-provider limiter constrains their combined concurrency. Within a scenario, essay generation and the separate prisoner calls happen in sequence. A judge call occurs only when necessary. Different concurrent scheduling or endpoint conditions could still affect latency and operational failure rates, so execution metadata should be retained.

The locally prepared study directory is:

`data/studies/afdt-anthropic-effort-sweep-20261108/`

It contains the frozen specification and preflight metadata, cell batches, scenario-level prompts and raw model responses, accepted essays, any reasoning content or summaries actually exposed by the API, usage records, optional judge traces, and outcome dispositions. The reporting command can create or refresh `summary.md`, `summary.csv`, `summary.json`, `pairs.csv`, `decisions.csv`, failure diagnostics, and a review summary **without rerunning** the underlying model calls.

All derivations should be traceable back to saved raw model outputs. A provider may expose a reasoning-token count without its complete reasoning text; no complete hidden trace is assumed in that case. Local study artifacts may contain extracted source text and are not necessarily all checked into the public repository. The source's redistribution conditions should be assessed separately from release of the methods and aggregate results.

This document describes the configuration and intended scoring procedure while generation is in progress. It is not a claim that all 180 scenarios have completed, that the live provider obeys every advertised setting, or that no operational changes will be considered later. If the running protocol is materially changed, that change should be dated and documented alongside the frozen study rather than obscured in this description.

## 10. Boundaries of inference

This study can characterize how **two named model/provider configurations** behave across three matched requested-effort settings when an independently generated exposition of Equation (4) A-FDT is fed into the same almost-twin game.

It cannot by itself establish:

- The unique mathematically correct answer to the FDT interpretation problem, where the source leaves graph details to be specified.
- The effect of **prisoner-only** reasoning effort, since researcher essays and researcher effort also change.
- Generalization to other games, payoffs, role names, observation structures, or physical action interfaces: there is only one fixed scenario.
- A model-family-independent ordering of how much reasoning `low`, `medium`, and `high` buy.
- Pure comparability with the first main study, since the narrative prompt was revised and the present cell configurations differ.
- An unbiased cooperation rate over all intended generations if refusals, essay overruns, or output-token failures systematically remove particular outcomes.
- A confirmatory hypothesis test established before seeing earlier exploratory results. The study was designed after earlier experiments and is explicitly exploratory.

For these reasons, observed action rates should be presented with their **complete-pair denominators**, missingness, essay variation, and an explicit distinction between observations and theoretical interpretation.

## Appendix: Configuration and exact instructional materials

The following repository materials give a more exact specification than a prose description can. The version frozen in the prepared study directory is the operational record if a file on the repository's default branch is subsequently edited.

| Material | Repository file |
|---|---|
| This follow-up's actual study configuration | [`configs/study.afdt-anthropic-effort-sweep-20261108.yaml`](../configs/study.afdt-anthropic-effort-sweep-20261108.yaml) |
| Short implementation and execution plan | [`docs/afdt-anthropic-effort-sweep-20261108.md`](afdt-anthropic-effort-sweep-20261108.md) |
| First main study methods | [`docs/first_study_design.md`](first_study_design.md) |
| Assignment/source mapping | [`configs/early_test.yaml`](../configs/early_test.yaml) |
| Reference-text manifest | [`sources/manifest.yaml`](../sources/manifest.yaml) |
| Shared researcher prompt | [`prompts/researcher/base.md`](../prompts/researcher/base.md) |
| A-FDT-specific researcher focus | [`prompts/researcher/fdt_eq4_focus.md`](../prompts/researcher/fdt_eq4_focus.md) |
| Prisoner game prompt, including memory-recall revision | [`prompts/prisoner/base.md`](../prompts/prisoner/base.md) |
| Fixed A/B observations and evidence leads | [`prompts/prisoner/observation_cases.yaml`](../prompts/prisoner/observation_cases.yaml) |
| Judge prompt and action classes | [`prompts/judge/intent.md`](../prompts/judge/intent.md) |
| Study and batch orchestration | [`almost_twin/study.py`](../almost_twin/study.py), [`almost_twin/batch.py`](../almost_twin/batch.py) |
| Game action/parser implementation | [`almost_twin/game.py`](../almost_twin/game.py) |

**No results are included here.** They should be published separately, together with failure accounting and a clear note that this was an exploratory follow-up.
