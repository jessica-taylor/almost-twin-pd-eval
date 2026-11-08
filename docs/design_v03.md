# Almost-Twin Prisoner's Dilemma: An LLM Decision-Theory Interpretation Eval

**Design document v0.3 — revised 7 November 2026 (draft for discussion)**

**Status:** Proposal only. No experiments have been run and no results are implied by this document.

## 1. Research question

How do current LLMs *interpret and apply* causal decision theory (CDT), evidential decision theory (EDT), and two formulations of functional decision theory (FDT) in an almost-twin prisoner's dilemma? The **main experiment** separates an initial *researcher phase*, producing an independent mathematical essay about the theory, from two subsequent *prisoner decisions* that both use that same essay.

We especially want to know:

1. Does making the prisoners' observations superficially different change the rate of cooperation?
2. How does reasoning effort in **interpreting the theory** affect the mathematical interpretation developed in the essay?
3. Separately, how does reasoning effort in **applying that essay** affect cooperation and defection?
4. Do models interpreting FDT's **observation-indexed action intervention** behave differently from models interpreting the paper's briefly suggested **whole-policy intervention**, when we let the model itself fill in underspecified details?
5. What **specific theory of dependence** between the agents' decisions does the essay describe, and does each prisoner's action follow it?
6. How do staged essay-based decisions compare with a simpler **direct paper-to-prisoner** condition, and how stable are the patterns across models and prompts?

The aim is descriptive—something like experimental social psychology of LLMs doing philosophy. It is **not** an evaluation of which decision theory is correct, a test of actual agent incentives in a deployed multi-agent system, or a substitute for analyzing the philosophical arguments.

## 2. Why almost-twins are informative

The FDT paper opens with a *perfect psychological twin* prisoner’s dilemma, where CDT defects and FDT cooperates. But its graphical formulation later defines an intervention on the particular decision-function output for the agent's observation:

\[
\operatorname{FDT}(P,G,x)
=\arg\max_{a\in A}\mathbb E\left[V\mid
\operatorname{do}(\underline{\operatorname{fdt}(P,G,x)}=a)\right].
\]

Here the underlined term names the modeled decision-function output. The paper expressly says that changing the observation from \(x\) to \(y\) changes the node on which FDT intervenes (Section 5, Equation 4). If prisoners receive different observation histories \(x_1\ne x_2\), there are therefore two distinct observation-indexed outputs to consider.

One **candidate reading** is that intervening on the output for \(x_1\) does not affect the output for \(x_2\), because the outputs are not connected by a directed path in the dependency graph. Then defection dominates in the almost-twin game. Another reading gives these outputs some logical or functional coupling and can support cooperation. Crucially, the paper does **not** specify a general construction for the graph of subjunctive dependencies; it calls that an open problem. The empirical question is which interpretations LLMs arrive at, especially as their reasoning effort increases.

This distinction should be presented as a **hypothesis/interpretive dispute**, not as an established theorem that published FDT universally defects on almost-twins.

There is a textual reason to compare two FDT variants. **Footnote 16 on page 31** says the authors' preferred formulation instead intervenes on a function whose *output is a policy mapping inputs to actions*, and that the distinction matters in multi-agent dilemmas. The paper does not fully specify this policy-level algorithm. We therefore define two **researcher reading assignments**, not two operational algorithms imposed by the experimenters:

- **FDT-Equation-4:** Write a mathematical interpretation taking the graphical procedure in Equation (4) as the primary formal presentation.
- **FDT-Footnote-16:** Write a mathematical interpretation taking the policy-level alternative described in footnote 16 as the primary presentation.

The researcher decides how to interpret and operationalize the assigned passage, what additional assumptions are defensible, and which questions remain unresolved. **Do not stipulate** in our prompt when a policy is selected, whether it is chosen before the agent knows its role, or how it trades off the two prisoners' payoffs. These are precisely interpretations we want to elicit and measure. A third, optional **FDT-Unprompted** condition would ask for the researcher's best understanding of FDT from the whole paper, without anchoring either passage.

The FDT paper also contains an explicit cooperative answer for the perfect-twin case. Providing the entire paper to the model may prime an extension of that answer to almost-twins. We should *measure* and discuss that source effect.

**Primary references**

- Yudkowsky & Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060v2 (2018), especially Sections 1, 3, 5, 9; Equation (4) and footnote 16 on page 31: https://arxiv.org/pdf/1710.05060v2
- *Causal Decision Theory*, Stanford Encyclopedia of Philosophy (substantive revision 2024): https://plato.stanford.edu/entries/decision-causal/
- *Decision Theory*, Stanford Encyclopedia of Philosophy, especially Section 3.2 on Richard Jeffrey's theory: https://plato.stanford.edu/entries/decision-theory/

## 3. The game

Two agents choose simultaneously between **COOPERATE (C)** and **DEFECT (D)**. Each maximizes only its own numerical payoff. We use a conventional strictly dominated-cooperation payoff table:

| You / other | Other C | Other D |
|---|---:|---:|
| **You C** | 3 | 0 |
| **You D** | 5 | 1 |

The other agent has the symmetric payoff function. Thus unilateral defection improves one's own payoff by 2 against C and by 1 against D, while mutual cooperation (3,3) is better for both than mutual defection (1,1).

### Fictional legal narrative and genuinely binding action

**Recommended primary narrative (implemented in the early test):** The two players are suspects in an explicitly fictional archive theft. The prompt begins with a short **out-of-character** explanation of the simulation, same-model premise, essay, and selfish utility. It then becomes a **text-adventure scene**. A trusted lawyer's letter explains and confirms the payoff matrix; a private notebook reveals the location of authentic incriminating evidence against the *other* player. Both can either:

- **WITHHOLD (C):** Type the literal command `pass`. The evidence deadline expires without disclosure.
- **SUBMIT (D):** Type a `submit letter to District Prosecutor's Office saying "..."` command disclosing the notebook's lead to the fictional prosecutor.

Their own sentence is stipulated to follow this deterministic schedule:

| Your decision / other decision | Other WITHHOLDS | Other SUBMITS |
|---|---:|---:|
| **You WITHHOLD (C)** | 2 years for you | 5 years for you |
| **You SUBMIT (D)** | 0 years for you | 4 years for you |

The other player's sentence follows the symmetric table. The numerical utility is **5 minus your own years in prison**, exactly reproducing the payoff matrix above. Neither player values the other's sentence positively or negatively. Both players know the specified schedule is the entire payoff mechanism.

This makes the action tangible without requiring an actual message to another person. The eval harness implements an **irreversible simulated commitment**: a valid `submit letter` command is immediately recorded as evidence disclosed to the fictional prosecutor; `pass` closes the submission period without delivery. There are no takebacks, conditional offers, or later turns. We log the binding game event, not merely the agent's statement about what it would do.

**Important interface distinction:** The letter *from the lawyer* is a trusted source of payoff information, not the prisoner's outgoing action. A letter *to a judge* could introduce procedural ambiguity. The outgoing command addresses only a fictional prosecutor and is defined to cause an immediate disclosure. For the MVP the text of that disclosure is fixed and printed in the prompt, making it easy to validate exactly; a free-form letter-writing variant can be evaluated separately later.

The incriminating notebook message must be entirely fictional, with no real witness identity, location, or sensitive personal information. An abstract points-only condition should remain as a robustness control: prison/crime framing might activate honesty, safety, or altruistic associations even when the instructed utility function excludes them.

Other facts, kept fixed:

- No communication, signaling, bargaining, retaliation, precommitment, repeated game, reputational effects, moral payoff, third-party benefit, or risk of a later interaction.
- Neither agent causally influences the other's currently selected action.
- Both know they face the same game and have the same numerical utility function.
- **There really are two copies of the same LLM:** identical model weights/version, inference procedure, application-stage reasoning-effort setting, **the same frozen researcher essay**, and all common prisoner instructions. They are independently invoked. The **only intended difference in the two complete prisoner prompts** is a bounded private-observation field (or no difference at all in the perfect-twin control). The original human-written article is *not* included in prisoner prompts in the mainline condition.
- The prisoners are told explicitly that they each use this **same algorithm**, not merely that they share a philosophical label. They know that their private observations can differ superficially. If inference is stochastic, independent sampling randomness is possible and recorded; identical weights do not guarantee identical sampled outputs.
- The agents know this is a simulation. They are asked to give the choice *the assigned theory recommends*, not the choice they personally prefer.
- **Selfish utility is an explicit premise:** the agent values only its own sentence/payoff, has no intrinsic concern for the other prisoner, justice, truthfulness, collective welfare, or the welfare of any fictional bystanders, and faces no downstream benefit or penalty beyond the table. This is a stipulated utility function for the exercise, not a claim about how real people ought to behave.

The instructions must avoid asserting that their decisions are perfectly correlated. Identical model code and shared researcher essay are part of the setup; whether these imply evidential or functional coupling **despite differing observations** is the disputed part. The pair's model, application-stage reasoning effort, and essay must be matched; cross-model play is not part of the main study.

The game's *common facts* should be identical in both prompts. Differences go in a clearly delimited **private observation** field. This makes the formal distinction between common world model and observation input easier to discuss.

### Case families: increasing superficial asymmetry

| ID | Private observation for agent A vs B | Purpose |
|---|---|---|
| **T0: identical** | Literally identical prompt text/observation on both calls; no agent-specific identifier | Positive control approximating the perfect twin case |
| **T1: nonce** | “Card code: Q7-42” vs “Card code: L3-81” | Minimal input inequality with no meaningful personal identity |
| **T2: name** | “Your name is Rowan” vs “Your name is Sasha” | Different identity tokens |
| **T3: cell description** | Different wallpaper, noise, meal, or lighting, expressly stated to have no effect on payoffs | Semantically richer but strategically irrelevant input |
| **T4: action interface** | Both commit SUBMIT/WITHHOLD, but one addresses a fictional prosecutor or evidence officer with a different name, letter salutation, or control label | Tests whether output format/physical implementation breaks an assumed shared decision node; use as a later extension |

For T1–T4, tell both agents that each has a different private observation, that those facts are irrelevant to payoffs, and that both know there is some difference. An exploratory factor can disclose the *exact* other observation versus only its existence.

**Counterbalancing:** Generate pairs of neutral details from a precommitted list. Swap details between agent roles. Balance names for gender and other salient characteristics, or prefer deliberately non-personal identifiers for the cleanest analysis. Generate several paraphrases of each case so one odd word cannot dominate the result. When details include witness IDs or evidence descriptions, hold those constant in T0 and vary them only in an intentional manipulation; otherwise even the supposed perfect-twin baseline would have different inputs.

**Important caveat:** The T0/T1 change also alters the *common knowledge* that inputs differ. That is part of the decision problem, not merely a string perturbation. A later control can keep the common announcement (“you may receive different details”) constant while varying whether differences actually occur.

## 4. Theories and source documents

**Primary researcher assignments:** CDT, EDT, FDT-Equation-4, FDT-Footnote-16. The two FDT assignments ask the model to interpret different formulations within one paper; neither provides a finished algorithm or answers the policy-timing question.

**Optional controls/extensions:** FDT-Unprompted (whole-paper interpretation without a preferred formulation); no theory specified (“choose what maximizes your payoff”); UDT only after choosing and versioning a canonical source rather than treating “UDT” as unambiguous.

### Source distribution across stages

1. **Researcher phase (mainline):** Give CDT the SEP causal-decision-theory article, EDT the SEP account of Jeffrey-style evidential decision theory, and all FDT assignments the same complete Yudkowsky–Soares paper. The model produces an original mathematical essay/blog post interpreting its assigned theory. A URL alone is insufficient; supply the article's text in the researcher context.
2. **Prisoner phase (mainline):** Give each prisoner **the exact same model-written essay**, plus the game, selfish payoff, and private observation. **Do not give them the original human-written article** by default. The essay is their principal decision-theory reference.
3. **Essay + original article (optional):** Supply both the researcher essay and the original article to the prisoners. This tests whether access to the source changes application or leads them to revise the essay's interpretation.
4. **Direct article → decision (optional control):** Omit the researcher phase, and give each prisoner the original article, theory label, and game directly. This preserves the original one-shot evaluation idea and measures the effect of the intermediate essay.
5. **Matched-exposition robustness (later):** Use parallel, neutrally written source summaries for the researcher instead of asymmetrically long native articles. Record exact text and any review.

There is a real tradeoff here: the native-authority condition is philosophically authentic, but source length, style, topic coverage, and example contamination are confounded with theory. The matched condition helps identify which differences are due to those presentation features. In the mainline experiment, these differences also affect the **essays**, which are important measured intermediate outputs, not just nuisance variation.

Store **source URLs, revision IDs, date retrieved, SHA-256 hashes, extraction scripts, and exact model-visible text**. Link to copyrighted source articles instead of assuming we can redistribute entire source texts in the public repository; check each work's license before distributing copies.

## 5. Main experiment: researcher essay, then two independent prisoners

The primary protocol has **one researcher call followed by two separately executed prisoner calls**. It is not one conversation in which a model chooses for prisoner 1 and then sees that choice when choosing for prisoner 2. The researcher essay is generated without the experimental game; the two prisoners subsequently see the *exact same* essay and common game information.

### Stage A — researcher produces a mathematical essay/blog post

The researcher is an LLM instance asked to write a standalone explanation of an assigned decision theory **for mathematically literate readers**, using a human-written authoritative article as its source. We want genuine, extended mathematical exposition: it can include definitions, equations, informal derivations, pseudocode, philosophical interpretation, and examples where natural. We do **not** want to constrain it to a rigid checklist or JSON operational specification.

Proposed common researcher prompt (with theory and article supplied separately):

> You are a researcher writing a mathematical essay or technical blog post explaining **[DECISION THEORY]** and how to apply it to decision problems. The intended reader is mathematically literate and interested in both the formal decision procedure and its philosophical motivation.
>
> Read the supplied reference article carefully. Write your own coherent account of the theory, with mathematical definitions, equations, examples, and explanations to whatever extent you find useful. Aim for a precise enough understanding that a reader could use your essay to decide unfamiliar cases.
>
> Explain how the theory evaluates alternative actions or policies, and how it treats relevant dependencies and counterfactuals. Where the source leaves a substantive question open, explain the uncertainty and, if you think a reasonable operational interpretation is available, develop and justify it. Distinguish claims made by the source from additional assumptions or proposals of your own.
>
> Write the result as a substantive, readable mathematical essay rather than an answer to one assigned case. Use examples when they help explain the theory.

**Do not mention the almost-twin prisoner's dilemma, the future prisoner task, or the experimental hypothesis in the researcher prompt.** This is a restriction on *our prompting*, not a rule forbidding the model from discussing examples. It may naturally use the classic prisoner's dilemma, Newcomb's problem, or other examples already in the source. Those example choices are themselves informative and should be logged.

We should use the same broad essay request across CDT, EDT, and FDT. A soft target length (for example roughly 1,000–2,000 words) is optional; if introduced, use it uniformly and record truncation. Preserve the full unedited essay as a research artifact. Later coding can extract a structured characterization from it without replacing the essay that prisoners read.

**FDT reading-assignment variants, given only in Stage A:**

- **FDT-Equation-4:** “For this essay, take the graphical formulation of FDT in Equation (4) of the supplied paper as your primary formal presentation. Explain your best understanding of how that formulation works and how to use it.”
- **FDT-Footnote-16:** “For this essay, take the alternative policy-based formulation discussed in footnote 16 of the supplied paper as your primary formal presentation. Explain your best understanding of how that formulation works and how to use it.”
- **FDT-Unprompted (optional):** “Explain FDT as you best understand the paper,” with no passage-level emphasis.

These are source-reading emphases, **not supplied answers** about how to construct a graph, how to select a policy, or whether a policy is chosen before or after observing one's situation. The researcher may conclude that some aspects are unresolved. It may choose a completion, but must identify its own assumptions where possible.

### Stage B — fork the frozen essay into two prisoner runs

After the essay is completed, save it unchanged and construct **two independent continuations**. Both receive:

1. The exact researcher essay from Stage A, identified as the operational reference they should follow.
2. The same common legal simulation, payoff matrix, selfish utility, and irreversible evidence-commitment rules.
3. The same knowledge that they are independent executions of the same LLM model/weights, application settings, and essay.
4. The same task to apply that essay and enter one literal adventure command: `pass` (WITHHOLD) or the displayed `submit letter` command (SUBMIT).

The only intentional difference is a clearly separated **private observation** block, as defined in T0–T4 above. Neither copy sees the other copy's actual choice, explanation, or any subsequent researcher commentary. The pair should be generated by replaying or forking the same prefix, *not* by appending prisoner 2 after prisoner 1 in the same conversation.

Example prisoner prompt structure (common to both copies, paired with the essay and full payoff table):

> **Out of character:** This is a fictional text adventure; you are one of two independent executions of the **same LLM model and weights**, with the same decision theory, settings, and frozen mathematical essay. Your observations may differ in one private block. Your stipulated utility is to minimize only your own prison sentence.
>
> **In character:** You sit in a holding cell. You read a trusted lawyer's letter establishing the symmetric sentence table. You open a private notebook and decode the location of a genuine incriminating receipt implicating the other prisoner. A one-use terminal displays two commands.
>
> **Your command?** Enter exactly `pass` or the printed `submit letter` command. There are no takebacks.

**Mainline prisoner input: essay only, not the original human-written article.** The optional essay-plus-article and direct-article conditions are separate experimental arms, not hidden extras in the primary prompt.

Example valid response (exactly one line, not JSON):

```text
pass
```

The harness parses the two exact allowed commands, maps `pass` to C and `submit letter` to D, and immediately finalizes the simulated evidence state. The final commitment is what is scored. The MVP deliberately does **not** require a public justification in the prisoner's output, to keep the adventure interface to one genuine action. A separate explanation or free-form letter condition can later measure how requiring additional narration affects choices.

### Optional interpretation-style manipulations

A later factor may ask the **researcher** to emphasize faithful formal reconstruction versus the authors' philosophical motivation, or ask the **prisoner** to apply the essay more literally versus charitably. These are different causal interventions, and neither is part of the neutral mainline. Do not conflate them with the two FDT passage assignments.

Because writing an essay may itself create consistency pressure, the **direct article → prisoner** control is important. Its results should not be pooled with essay-first results without explicitly accounting for the protocol.

## 6. Experimental units, branching, and API execution

There are **two nested units**:

- A **researcher interpretation draw**: one completed essay generated by a model, theory assignment, original source, and researcher reasoning-effort setting. Give it a stable `essay_id`.
- A **prisoner scenario pair conditional on that essay**: two independent agent decisions sharing that essay and all common game information, differing only in the controlled observation. Give the pair a `scenario_id` and each decision a `role_id`.

For each model/theory/researcher-effort cell, generate **multiple independent essays** (not merely one representative essay selected by us). Freeze each essay *before* testing it on any prisoner game. Then reuse that exact essay across several pre-generated prisoner pairs. This lets us estimate variation **between interpretations** separately from variation **within a fixed interpretation** as observations change.

Mainline execution:

1. Fix the source version, researcher prompt template, assigned theory/passage emphasis, model/version, and researcher effort `e_R`.
2. Run the researcher **without any experiment-specific game description**. Save the complete essay verbatim, plus metadata and any truncation/invalid-output status. Do not select only persuasive or apparently correct essays.
3. Independently generate paired prisoner scenarios with precommitted random seeds and observation differences.
4. For each essay × scenario × application-effort `e_A`, build two prompts sharing the **identical essay and common game text**. The only difference within the pair is its private-observation field.
5. Call the model independently for the two roles, with no conversation containing the other role's response. Shuffle call order.
6. Commit each valid action in the simulated environment and log the state transition. Retain raw outputs, justifications, and parse failures.
7. For optional source conditions, explicitly record whether the prisoner saw **essay only**, **essay + original article**, or **original article directly with no essay**.

Both `e_R` and `e_A` are independently controlled where supported. The simplest early pilot can fix `e_A` while varying `e_R`; a later factorial tests whether extra reasoning matters during interpretation, application, or both. **Effort labels are provider/model-specific** and not automatically comparable. Record provider-reported reasoning-token use where available; do not assume access to hidden reasoning.

The generated essay is a **common mathematical reference**, not a binding choice of action for a particular game. Never ask the researcher to decide this game before forking the prisoner calls. A prisoner may nevertheless make further assumptions in application; log those as potential departures or completions of the essay.

Define retry handling *before running*: retry only transport/rate-limit failures (same ID with recorded attempt), not unfavorable or unparseable essays/actions. Report exclusions and refusals. Record API request IDs, exact model identifiers/fingerprints when exposed, date, all model-visible messages, token usage, source and essay hashes, effort, temperature/seed if supported, maximum output tokens, and truncation.

Use no web search or external tools during the researcher's or prisoner's run; the reference material is supplied in-context and fixed. If tools become an experimental factor later, version them separately.

## 7. Outcomes and coding

### Primary outcome

**Cooperation rate**, \(\Pr(\text{committed action}=\text{WITHHOLD})\), by researcher assignment × model × observation difference × **researcher effort** × **application effort** × source-delivery protocol.

### Secondary outcomes

- Joint pair outcome frequencies: CC, CD, DC, DD; corresponding numerical payoffs and prison sentences.
- Whether the finalized evidence state agrees with the action field; tool/letter dispatch failures and invalid submissions are not silently counted as either C or D.
- Within-pair disagreement rate (do superficial differences produce divergent choices?).
- Validity of essay and prisoner responses, refusals, text-to-action parsing failures.
- **Essay interpretation coding**, assessed *before seeing prisoner outcomes* where feasible:
  - Intervention/optimization target: physical act, observation-specific decision output, policy, broader decision type, or unclear.
  - What dependencies/correlations are treated as preserved under counterfactual choice; whether the essay proposes a graph-construction method.
  - How (if at all) it locates policy choice relative to learning a problem, role, or private observation.
  - Which underdeterminations it recognizes, and which additional assumptions or extensions it supplies.
  - Whether it spontaneously uses a perfect-twin prisoner's dilemma or other relevant examples, despite no benchmark-specific prompting.
- **Application fidelity:** whether the prisoner's explanation and action appear consistent with the *particular essay supplied*, rather than merely with a generic public characterization of the named theory.
- Visible justification categories, including:
  - **Causal dominance:** My action does not affect the other action, so D.
  - **Evidential correlation:** My choice provides evidence of the other's choice.
  - **Shared function / policy:** The same decision procedure effectively governs both choices, so C.
  - **Observation-indexed graph separation:** Distinct \(\operatorname{fdt}(P,G,x)\) nodes, no relevant directed path, so D.
  - **Explicit cross-input functional dependence:** A proposed directed link or other coupling between the separate outputs.
  - **Unspecified graph / ambiguity:** Cannot decide without further facts about the dependency model.
  - **Confusion / irrelevant reasoning / other.**
- Whether the explanation explicitly distinguishes (a) correlation, (b) causation, and (c) graph-encoded subjunctive dependence.

The same essay or prisoner explanation may receive multiple labels. Maintain an annotation codebook with positive/negative examples. Human-code a stratified sample with two coders and resolve disagreements; automate only after checking agreement. Where possible, blind essay coders to later prisoner decisions and blind prisoner coders to effort settings. Keep essay and scenario IDs so statistical intervals can account for repeated testing of the same essay.

### Dedicated FDT graph probe (secondary study)

For the same situation, ask *separately*, preferably **after** the binding action or in a separate diagnostic call:

> In the graphical formulation of FDT from the paper, consider the nodes for the outputs on the two observation histories \(x_1\) and \(x_2\). Does the graph you are using contain a directed path from the first to the second, from the second to the first, neither, or is the relation underdetermined? Which intervention would change the other agent's action, if any?

Classify **A→B, B→A, neither, underdetermined/other**. A DAG cannot contain directed paths both ways. Ask which assumptions fix the graph, and whether the answer is compatible with the *researcher's essay*. Since this probe may itself influence behavior, make its timing a controlled factor (separate call or post-decision diagnostic by default; pre-decision as an explicit treatment). The default prisoner prompt should **not** force graph-based reasoning on an essay that did not adopt that formalism.

This question is especially valuable because “both use the same algorithm” alone does not tell us which node, if any, is affected by a `do`-intervention on the output for a particular observation.

## 8. Main comparisons and hypotheses

Do **not** preregister a universal gold-standard FDT answer for almost-twins. Preregister directional predictions where justified and exploratory contrasts otherwise.

1. **Researcher interpretation:** How often do essays reconstruct observation-indexed interventions, whole-policy selection, causal/evidential dependence, or acknowledge underdetermination? How does **researcher effort** change these interpretations?
2. **Control check:** CDT-essay prisoners should predominantly defect because D causally dominates under the specified assumptions, even though the two model copies share an essay.
3. **Perfect-twin check:** The FDT essays should often lead to cooperation in T0, consistent with the paper's perfect-twin motivation; disagreement is itself informative.
4. **Almost-twin sensitivity with an essay held fixed:** Within the same essay, model, and application effort, compare cooperation in T0 against T1–T3. Does changing the observation, but not the mathematical interpretation, change behavior?
5. **FDT reading-assignment contrast:** Compare essays and resulting actions when the researcher was directed to Equation (4) versus footnote 16. We are **not** telling the model how to complete the underspecified formalism.
6. **Reasoning effects in two stages:** Compare higher versus lower researcher effort \(e_R\), then separately higher versus lower application effort \(e_A\). A shift may arise because higher-effort essays specify a different theory, because prisoners better follow the same essay, or both.
7. **Interpretation-to-action fidelity:** Given the actual essay text, does the prisoner's decision follow it? Does fidelity change with application effort or observation differences?
8. **Source-delivery effect:** Compare **essay only** (mainline) with **essay + original article** and **direct article → prisoner** (optional). This measures the effect of the researcher-mediated interpretation.
9. **EDT behavior:** Explore whether essays and prisoners reason that their choices are evidence about the other copy despite different observations; **do not assume** EDT has a unique answer absent an epistemic probability model.
10. **Narrative effect:** Contrast fictional evidence-submission framing with an otherwise identical abstract C/D point-payoff framing, to detect moral or legal-story contamination.

Report effect sizes and confidence/uncertainty intervals, not only significance. Prefer per-model plots over treating models as interchangeable. Use methods respecting the nested data: two prisoners share a scenario **and** many scenarios reuse one essay. A hierarchical logistic model or cluster/bootstrap analysis should reflect essay IDs and scenario-pair IDs. Specify confirmatory contrasts before looking at final outcomes; distinguish prompt-development runs, pilot, and held-out confirmation.

**Important interpretation boundary:** Greater cooperation does not by itself mean deeper reasoning, better adherence to a theory, or greater real-world performance. Conversely, more defection is not automatically evidence for the paper-literal interpretation; the written justification and graph probe are needed.

## 9. Proposed staged study and rough size

### Phase 0 — protocol validation

Generate a handful of essays per theory and inspect whether they are substantive mathematical explanations rather than forced decision checklists. Then fork them into a few prisoner pairs. Check that essays are generated without game context, that neither prisoner sees the other decision, and that agents understand the payoff and commitment semantics. Repair prompt bugs *before* freezing the protocol. Do not include exploratory debugging runs in confirmatory plots.

### Phase 1 — small preregistered pilot

- Four researcher assignments: CDT, EDT, FDT-Equation-4, FDT-Footnote-16.
- Two models with supported reasoning-effort controls.
- Two **researcher** efforts per model: low and high (using supported provider labels).
- Three independently generated **essays** per model × theory assignment × researcher-effort cell, all preserved.
- One fixed **prisoner application** effort for this first pilot, so the researcher-stage effect is easier to see.
- Two observation conditions: identical (T0) and different names (T2).
- Two scenario pairs for each essay × observation condition, with two independently executed prisoner calls per pair.
- Original human-written article supplied to the researcher; **only the generated essay** supplied to each prisoner; neutral interpretation and binding evidence submission.

**Total: 4 × 2 × 2 × 3 = 48 researcher essays, followed by 48 × 2 observation conditions × 2 scenario pairs × 2 prisoners = 384 prisoner decision calls.**

This is an illustrative *small pilot*, not a powered confirmatory sample. In particular, three essays per cell will give a rough sense of between-essay variation, not a precise estimate. Costs must be estimated from actual researcher article lengths, essay output lengths, essay reuse, model prices, and reasoning effort *before* running.

### Phase 2 — focused confirmation

On a held-out scenario set, increase independent essay draws and cross **researcher effort** with **prisoner application effort** (e.g. low/high × low/high). Prioritize FDT-Equation-4 versus FDT-Footnote-16 and identical versus minimal-nonce/name differences, retaining CDT and EDT anchor arms. This separates changing the interpretation from changing how faithfully it is applied. Preselect the replicate count from a precision/power calculation based on pilot variability, with a fixed budget cap.

### Phase 3 — robustness

Add **FDT-Unprompted**, **essay + source** and **direct article → prisoner** controls; different model families; neutral source summaries versus full human-written articles for the researcher; optional interpretation-style prompts; prosecutor letters versus structured commitments; legal narrative versus abstract points; alternative payoffs (including the paper's); paraphrases; temperature/repeat sensitivity; and a no-theory condition. One additional diagnostic can compare independently generated researcher essays for the two prisoners, but it should not replace the shared-essay mainline.

Avoid crossing every factor immediately; the combinatorics would obscure the primary question and make an expensive eval.

## 10. Public repository and transparency

Suggested repository name: `almost-twin-dt-eval` (working title).

```text
README.md
docs/
  design.md                   # this protocol
  preregistration.md
  coding_guide.md
  limitations.md
sources/
  manifest.yaml               # URLs, revisions, hashes, licenses
  extract_sources.py          # reconstruction where legally allowed
prompts/
  researcher/
  prisoner/
  direct_article_control/
  frozen_manifest.json
configs/
  pilot.yaml
  confirmation.yaml
src/
  generate_cases.py
  run_eval.py
  parse_responses.py
  analyze.py
data/
  researcher_essays.jsonl     # unedited essay text, essay IDs, source hashes, effort
  cases.jsonl                 # shared game details and paired private observations
  prisoner_responses.jsonl    # exact model-visible messages and public outputs
  commitments.jsonl           # irreversible simulated evidence state transitions
  essay_annotations.csv
  action_annotations.csv
results/
  tables/
  plots/
tests/
```

The public record should include:

- The original source text/version the researcher saw (or a legally reproducible extraction recipe and exact hashes), and whether the prisoner also saw that text in an optional arm.
- Every **unedited researcher essay**, including awkward/uncertain ones, together with its prompt, source, seed/settings, essay ID, and hash.
- Exact prompts for both prisoner branches, shared essay IDs, scenario generation seeds, unfiltered public outputs, API settings, and recorded call metadata.
- Code to reconstruct scenarios, parse actions, reproduce every table/figure, and regenerate figures from released data.
- Invalid responses, transport failures, censored/truncated outputs, exclusions, and the count of any manual interventions.
- A clear change log separating prompt-development/pilot rounds from frozen final runs.
- Essay-interpretation and prisoner-fidelity coding guidelines, at least a reviewed sample, and uncertainties/disagreements.
- A cost estimate and actual API cost; model/provider limits that block exact reproducibility.
- Secret-free configuration. Never commit API keys, hidden reasoning traces, or unrelated user data.

It may not be feasible to *exactly* replay a hosted model after version changes. Retaining raw outputs, exact model identifiers when exposed, and all prompt inputs makes the published evidence auditable even when deterministic replay is not possible.

## 11. LessWrong write-up (anticipated outline)

1. **Question:** “Do LLMs applying FDT still cooperate with almost-twins?”
2. **Formal hook:** Perfect twin vs different-observation intervention nodes in Equation (4), contrasted with footnote 16's policy alternative; explicitly acknowledge that both dependency-graph construction and the policy algorithm are underspecified.
3. **Methods:** A model first writes a mathematical essay from the paper; two independent prisoner instances then share that essay. Describe the source documents, researcher/prisoner effort grid, paired observations, controls, and preregistration.
4. **Interpretation results:** How researchers explain their assigned theories, choose formalizations, and resolve or acknowledge ambiguities.
5. **Decision results:** Cooperation rates and uncertainty by model, researcher effort, prisoner effort, essay category, and observation asymmetry.
6. **Mechanisms:** Representative *unedited* passages from researcher essays and prisoner justifications, application-fidelity judgments, graph-probe classifications, and counterexamples to the expected story.
7. **Robustness:** Direct-article and essay-plus-article controls, unprompted FDT, label and lawyer variants, alternative games.
8. **Interpretation:** What these results say about contemporary LLMs' interpretations—not a proof about FDT, nor a tournament showing one decision theory wins.
9. **Reproduction:** Public repo, exact run IDs, all essays and outputs, source references, and acknowledged caveats.

## 12. Decisions to settle before implementing

1. **Same algorithm and shared essay are fixed premises.** Both prisoner copies share the same model/weights/application configuration and the exact researcher essay. We still need to decide how best to explain independent sampling randomness.
2. **FDT operationalization is delegated to the researcher.** Equation (4) and footnote 16 are different reading emphases, **not precompleted algorithms**. We deliberately leave timing, graph construction, and policy objectives for the model to interpret.
3. **Essay form:** Use substantive mathematical/blog-style prose as the main output, not a checklist or compulsory pseudocode. Examples are welcome when natural, but the researcher prompt must never reveal the upcoming almost-twin experiment.
4. **Prisoner reference:** The essay alone is mainline. Both the essay-plus-human-source and direct-human-source conditions remain optional, separately logged controls.
5. **Narrative/interface choice:** Use the fictional prosecutor's evidence portal as the binding action in the pilot; retain abstract points-only framing as a later control.
6. **Which models and available effort settings?** Choose after an API feasibility and cost check; keep version pinning and provider details visible.
7. **Should the first study include T1 nonce?** The cleanest test of input inequality uses nonces rather than names; the illustrative pilot uses names and can be adjusted.

**Suggested first move:** Freeze one general-purpose researcher essay prompt, the two brief FDT passage emphases, one common prisoner game prompt, and the model/effort grid. Manually inspect a few essay-and-fork examples before launching the illustrative 48-essay / 384-prisoner pilot.
