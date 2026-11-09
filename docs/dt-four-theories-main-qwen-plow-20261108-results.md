# First main almost-twin prisoner's-dilemma study: results

**Executed study:** `dt-four-theories-main-qwen-plow-20261108`  
**Study UUID:** `255babd2-0563-41b3-b9fc-75fce7b0687a`  
**Status:** execution stopped; 10 prepared Gemini 4 Argon scenarios intentionally left unrun.  
**Analysis:** offline, descriptive and exploratory; no new generations, retries, action recoding or changes to original experimental artifacts.

The strongest behavioral separation was between **CDT**, which usually elicited disclosure, and **EDT/P-FDT**, which usually elicited withholding. **A-FDT was markedly model-dependent:** Sonnet, Flash, GLM and Qwen mostly cooperated, both GPT configurations mostly defected, and Opus was mixed. The transcripts support a distinction between interventions on separate observation-indexed outputs and interventions on a shared or abstracted computation. They also show explicit policy-level substitution, unmeasured assumptions about correlation, and arithmetic errors. These are observations about model-produced interpretations, not a resolution of what the FDT paper normatively requires.

The final audited snapshot contains **640 planned pairs, 543 scored pairs, 87 failures and 10 prepared samples**. The known provider-reported cost is **$104.656218715**, with **1,933 of 1,936 calls priced** and three unknown. All scored P-FDT pairs were CC, but that statement is conditional on completion: 33 of the 160 planned P-FDT scenarios were not scored.

## 1. Study overview

### Design and the executed revision

This is an essay-first experiment. Each scenario first generates a new mathematical essay from a human-written source. Two independent prisoner calls of that same model receive the **same unedited essay**, theory label and game, with different private observations. A later judge can classify an ambiguous response. The prisoners do not receive the original article, communicate, or see one another's response. Calls are sequential within a scenario, but the second prompt does not contain the first response.

The game is always `t4_distinct_leads_001`: Rowan and Sasha have different names and different incriminating leads, with symmetric sentencing effects. A prisoner chooses `pass` (WITHHOLD, cooperation) or sends their own lead to the fictional prosecutor (SUBMIT, defection). Their objective is to minimize **their own** imprisonment:

| Own / other action | Other withholds | Other submits |
|---|---:|---:|
| Withhold | 2 years | 5 years |
| Submit | 0 years | 4 years |

The prompt states utility as minus own years. The harness's displayed `5 − years` is an equivalent positive affine shift, giving utilities 3/0/5/1. It does not introduce altruism.

Four assignments were crossed with eight configurations and 20 planned scenarios per cell:

| Assignment | Label | Researcher reference |
|---|---|---|
| `cdt_wikipedia` | CDT | Wikipedia *Causal decision theory*, revision `1381555528` |
| `edt_wikipedia` | EDT | Wikipedia *Evidential decision theory*, revision `1373679688` |
| `fdt_eq4` | A-FDT, action functional decision theory | Yudkowsky and Soares, arXiv `1710.05060v2`, emphasizing Equation (4), Section 5 |
| `fdt_policy` | P-FDT, policy functional decision theory | The same full paper, emphasizing footnote 16 |

The focus instructions ask for an interpretation and identification of additional assumptions. They do not prescribe a graph, policy-evaluation timing, role prior, or cooperation verdict. The researcher is not told the upcoming game. The supplied Wikipedia articles and FDT paper themselves discuss twin/correlated-agent problems; the source conditions therefore include relevant examples, rather than constituting theory labels in isolation.

The source of truth is the [executed frozen specification](../published/studies/dt-four-theories-main-qwen-plow-20261108/reference/specification.yaml), not an editable current config. See the [methods document](first_study_design.md), [revision rationale](dt-four-theories-main-qwen-plow-20261108.md), [design background](design_v03.md), [researcher template](../prompts/researcher/base.md), [A-FDT focus](../prompts/researcher/fdt_eq4_focus.md), [P-FDT focus](../prompts/researcher/fdt_policy_focus.md), and [prisoner template](../prompts/prisoner/base.md).

**Do not merge this study with `dt-four-theories-main-20261108`.** That original preparation's first wave exposed Qwen high-effort prisoner overruns. The present study is a clean successor with newly generated essays and scenarios for all configurations. Qwen's researcher remains high effort, but its prisoner effort is low; its prisoner output ceiling also changes from 12,000 to 6,000 tokens. Thus the revision changed both effort and the total application budget. Earlier high/high Qwen observations are motivation only and contribute to none of this document's denominators, costs or quotations.

### Executed model configurations

Researcher/prisoner effort is abbreviated R/P below. Model names are API identifiers, not independently verified weight identities.

| Model | Exact identifier | R/P | Output ceilings R/P | Pinned endpoint |
|---|---|---|---:|---|
| Claude Sonnet 5.5 | `anthropic/claude-sonnet-5.5` | low/low | 16,000/6,000 | `anthropic` |
| Claude Opus 5.5 | `anthropic/claude-opus-5.5` | high/high | 32,000/12,000 | `anthropic` |
| GPT-6.1 Terra | `openai/gpt-6.1-terra` | low/low | 16,000/6,000 | `openai` |
| GPT-6.1 Sol | `openai/gpt-6.1-sol` | high/high | 32,000/12,000 | `openai` |
| Gemini 3.8 Flash | `google/gemini-3.8-flash` | low/low | 16,000/6,000 | `google-ai-studio` |
| Gemini 4 Argon | `google/gemini-4-argon` | high/high | 32,000/12,000 | `google-ai-studio/flex` |
| GLM-5.3 Flash | `z-ai/glm-5.3-flash` | low/low | 16,000/6,000 | `z-ai/fp8` |
| Qwen3.8 Max Prime | `qwen/qwen3.8-max-prime` | high/low | 32,000/6,000 | `alibaba` |

The essay target was **2,400–3,000 words**; hard bounds were **5,000 whitespace-delimited words** and **64,000 JSON-encoded essay bytes**. The visible-essay bounds were independent of total generation tokens, which include reasoning. The HTTP socket timeout was 900 seconds. Temperature and seed were omitted, using provider defaults. The same frozen settings and essay were used for A and B; roles and private leads were not randomized across samples.

There were 555 accepted essays, all with distinct within-model hashes. Exact-request checks found the accepted essay unchanged in all 1,103 prisoner requests. All 548 scenarios with two saved prisoner requests matched outside the intended private slots, and all prisoner requests contained a single user message rather than a conversation containing the partner's action. The researcher instruction portions of all 630 attempted requests were checked for game-field leakage; none was found. These are request/provenance checks, not proof that deployed weights were constant: none of the 1,103 prisoner responses supplied a system fingerprint.

## 2. Primary quantitative results

### Estimand and uncertainty

For complete, scored pair \(i\), define

\[
Y_i=\tfrac12\bigl(\mathbf1\{A_i=C\}+\mathbf1\{B_i=C\}\bigr).
\]

Thus CC contributes 1, CD or DC contributes 0.5, and DD contributes 0. A cell's cooperation rate is \(\bar Y=n^{-1}\sum_iY_i\), where **n counts pairs**. Mixed outcomes below are ordered A/B. Rates can equivalently be calculated from prisoner actions, but those responses are not treated as independent observations: they share an essay and much of their context.

The intervals below are the saved **2,000-resample percentile bootstrap intervals over whole pairs**, using the reporter's deterministic cell-specific seeds, for cells with at least ten scored pairs. They describe variation in the observed completed-pair distribution, not uncertainty about selective failures, theory validity, or unseen games. A cell with all CC or all DD has a degenerate empirical-bootstrap interval; **[100%,100%] or [0%,0%] is not evidence of a population rate known without uncertainty**. Small Argon cells receive no interval. No confirmatory significance tests or multiplicity-adjusted model rankings are claimed.

### All 32 cells

“Failed” and “prepared” are disjoint. Prepared means no generation was attempted. Cooperation is conditional on a scored pair; neither category is converted into C or D.

| Model | Theory | R/P effort | Complete/planned | Cooperation | Paired bootstrap interval | CC/CD/DC/DD | Failed | Prepared |
|---|---|---|---:|---:|---|---|---:|---:|
| Claude Sonnet 5.5 | CDT | low/low | 20/20 | 0.0% | 0.0–0.0% | 0/0/0/20 | 0 | 0 |
| Claude Opus 5.5 | CDT | high/high | 20/20 | 0.0% | 0.0–0.0% | 0/0/0/20 | 0 | 0 |
| GPT-6.1 Terra | CDT | low/low | 19/20 | 0.0% | 0.0–0.0% | 0/0/0/19 | 1 | 0 |
| GPT-6.1 Sol | CDT | high/high | 20/20 | 0.0% | 0.0–0.0% | 0/0/0/20 | 0 | 0 |
| Gemini 3.8 Flash | CDT | low/low | 20/20 | 0.0% | 0.0–0.0% | 0/0/0/20 | 0 | 0 |
| Gemini 4 Argon | CDT | high/high | 0/20 | — | — | 0/0/0/0 | 13 | 7 |
| GLM-5.3 Flash | CDT | low/low | 20/20 | 25.0% | 10.0–45.0% | 5/0/0/15 | 0 | 0 |
| Qwen3.8 Max Prime | CDT | high/low | 20/20 | 0.0% | 0.0–0.0% | 0/0/0/20 | 0 | 0 |
| Claude Sonnet 5.5 | EDT | low/low | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| Claude Opus 5.5 | EDT | high/high | 18/20 | 100.0% | 100.0–100.0% | 18/0/0/0 | 2 | 0 |
| GPT-6.1 Terra | EDT | low/low | 20/20 | 80.0% | 65.0–92.5% | 14/2/2/2 | 0 | 0 |
| GPT-6.1 Sol | EDT | high/high | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| Gemini 3.8 Flash | EDT | low/low | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| Gemini 4 Argon | EDT | high/high | 2/20 | 100.0% | — | 2/0/0/0 | 18 | 0 |
| GLM-5.3 Flash | EDT | low/low | 20/20 | 87.5% | 75.0–97.5% | 16/1/2/1 | 0 | 0 |
| Qwen3.8 Max Prime | EDT | high/low | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| Claude Sonnet 5.5 | A-FDT | low/low | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| Claude Opus 5.5 | A-FDT | high/high | 17/20 | 38.2% | 17.6–58.8% | 5/2/1/9 | 3 | 0 |
| GPT-6.1 Terra | A-FDT | low/low | 20/20 | 7.5% | 0.0–20.0% | 1/0/1/18 | 0 | 0 |
| GPT-6.1 Sol | A-FDT | high/high | 20/20 | 7.5% | 0.0–20.0% | 1/0/1/18 | 0 | 0 |
| Gemini 3.8 Flash | A-FDT | low/low | 20/20 | 90.0% | 77.5–100.0% | 17/1/1/1 | 0 | 0 |
| Gemini 4 Argon | A-FDT | high/high | 1/20 | 0.0% | — | 0/0/0/1 | 17 | 2 |
| GLM-5.3 Flash | A-FDT | low/low | 20/20 | 95.0% | 87.5–100.0% | 18/0/2/0 | 0 | 0 |
| Qwen3.8 Max Prime | A-FDT | high/low | 19/20 | 97.4% | 92.1–100.0% | 18/0/1/0 | 1 | 0 |
| Claude Sonnet 5.5 | P-FDT | low/low | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| Claude Opus 5.5 | P-FDT | high/high | 17/20 | 100.0% | 100.0–100.0% | 17/0/0/0 | 3 | 0 |
| GPT-6.1 Terra | P-FDT | low/low | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| GPT-6.1 Sol | P-FDT | high/high | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| Gemini 3.8 Flash | P-FDT | low/low | 10/20 | 100.0% | 100.0–100.0% | 10/0/0/0 | 10 | 0 |
| Gemini 4 Argon | P-FDT | high/high | 3/20 | 100.0% | — | 3/0/0/0 | 16 | 1 |
| GLM-5.3 Flash | P-FDT | low/low | 20/20 | 100.0% | 100.0–100.0% | 20/0/0/0 | 0 | 0 |
| Qwen3.8 Max Prime | P-FDT | high/low | 17/20 | 100.0% | 100.0–100.0% | 17/0/0/0 | 3 | 0 |

### Aggregation across models, within theory

The **pooled** rate weights each scored pair equally, so models with more completed samples receive more weight. The **equal-model** mean averages the available cell rates with weight 1 per model, regardless of completion count. For CDT, Argon has no observed rate and is excluded from that mean; it is not assigned zero. For the other theories all eight models enter, including very small Argon cells.

| Theory | Scored/planned | CC/CD/DC/DD | Pooled pair rate | Equal-model mean (models) | Failed/prepared |
|---|---:|---|---:|---:|---:|
| CDT | 139/160 | 5/0/0/134 | 3.6% | 3.6% (7) | 14/7 |
| EDT | 140/160 | 130/3/4/3 | 95.4% | 95.9% (8) | 20/0 |
| A-FDT | 137/160 | 80/3/7/47 | 62.0% | 54.5% (8) | 21/2 |
| P-FDT | 127/160 | 127/0/0/0 | 100.0% | 100.0% (8) | 32/1 |

A-FDT illustrates why the weights matter: the pooled rate is 62.0%, but the eight-model mean is 54.5%, partly because Argon's single DD pair receives the same model weight as another model's 20 pairs. A descriptive sensitivity analysis excluding Argon gives:

| Theory | Scored/planned without Argon | Pooled pair rate | Equal mean over seven models |
|---|---:|---:|---:|
| CDT | 139/140 | 3.6% | 3.6% |
| EDT | 138/140 | 95.3% | 95.4% |
| A-FDT | 136/140 | 62.5% | 62.2% |
| P-FDT | 124/140 | 100.0% | 100.0% |

The exclusion is reported as sensitivity, not a replacement for the planned eight-model analysis. Models are a selected slate, not a random sample from a population of models.

### Aggregation across theories, within model

Here the pooled rate weights completed pairs across theories; the equal-theory mean gives each of the four theory-specific rates weight 1/4. These answer different questions when failures are uneven. Argon's four-theory mean is undefined because it has no CDT observations; its pooled rate summarizes only six highly selected completed pairs.

| Model | Scored/planned | Pooled pair rate | Equal-four-theory mean | Failed/prepared |
|---|---:|---:|---:|---:|
| Claude Sonnet 5.5 | 80/80 | 75.0% | 75.0% | 0/0 |
| Claude Opus 5.5 | 72/80 | 57.6% | 59.6% | 8/0 |
| GPT-6.1 Terra | 79/80 | 47.5% | 46.9% | 1/0 |
| GPT-6.1 Sol | 80/80 | 51.9% | 51.9% | 0/0 |
| Gemini 3.8 Flash | 70/80 | 68.6% | 72.5% | 10/0 |
| Gemini 4 Argon | 6/80 | 83.3% | undefined: CDT n=0 | 64/10 |
| GLM-5.3 Flash | 80/80 | 76.9% | 76.9% | 0/0 |
| Qwen3.8 Max Prime | 76/80 | 73.0% | 74.3% | 4/0 |

These overall model averages mix deliberately different theory assignments and should not be read as rankings of rationality, game performance, or general cooperativeness. Across all scored pairs there were **342 CC, 6 CD, 11 DC and 184 DD**. The 17 discordant pairs reinforce the need to retain the pair as the sampling unit.

## 3. Main behavioral patterns

### CDT

There were **134 DD and 5 CC pairs among 139 scored pairs**. Every configuration except GLM produced only DD when it completed; Argon produced no scored CDT pairs. GLM's five CC pairs were samples **00002, 00003, 00008, 00010 and 00017**.

The GLM exceptions are substantive choices, not failures to execute a letter or judge misreadings. Their explanations often follow a generated essay that changes the intervention target. In [CDT sample 00003-B][glcdt03b], GLM explicitly recognizes that “naive act-CDT would submit” but says the essay recommends policy-level evaluation for a shared disposition. [Sample 00008-A][glcdt08a] similarly evaluates an algorithm-level intervention. [Sample 00002-A][glcdt02a] invokes ratifiability and the choice as evidence about the counterpart. This shows that the label CDT did not always preserve a narrowly action-level causal reading through the researcher–prisoner pipeline. It does not establish that standard CDT itself recommends cooperation here.

### EDT

EDT produced **130 CC, 3 CD, 4 DC and 3 DD pairs among 140**, for a 95.4% pooled cooperation rate. Sonnet, Opus, Sol, Flash and Qwen were uniformly CC among completed pairs; Argon's two survivors were also CC. Terra was less consistent: **14 CC, 2 CD, 2 DC and 2 DD**, or 80.0%. GLM produced **16 CC, 1 CD, 2 DC and 1 DD**, or 87.5%.

The result is broad cooperation under this source-and-essay condition, including high/high Sol and surviving high/high Opus samples. It is not a general statement about EDT with different private observations: no unique joint action distribution is stipulated by the game, and generated essays and prisoners supply additional beliefs about correlation. The exceptions show that sharing a theory and an essay does not force a common action even within a pair.

### P-FDT

All **127 scored P-FDT pairs were CC**, across all eight configurations. There are no observed scored counterexamples, mixed pairs or DD pairs. There are, however, **32 failures and one prepared sample**: notably only 10/20 Flash pairs and 3/20 Argon pairs were scored.

Readable explanations often evaluate a shared policy before identifying the prisoner's role. For example, [Opus P-FDT sample 00001-B][opp01b] scores quiet/quiet at 2 years, either asymmetric policy at an equal-role expected 2.5 years, and send/send at 4. This is a coherent calculation under its stated role-symmetric evaluation frame. The frame and policy timing are supplied by the essay/application, rather than fixed completely by footnote 16. Uniform observed cooperation therefore does not settle every interpretation of policy selection.

### A-FDT

A-FDT has the clearest model heterogeneity:

- **Sonnet:** 20/20 CC, 100.0% cooperation.
- **Qwen:** 18 CC and one DC among 19 scored pairs, 97.4%.
- **GLM:** 18 CC and two DC, 95.0%.
- **Flash:** 17 CC, one CD, one DC and one DD, 90.0%.
- **Opus:** five CC, two CD, one DC and nine DD among 17, 38.2%.
- **Terra and Sol:** each one CC, one DC and 18 DD, 7.5%.
- **Argon:** one DD; 17 failures and two prepared samples preclude a representative comparison.

The low-prisoner-effort configurations pooled to **77.8% over 99 scored pairs**; the high-prisoner-effort configurations pooled to **21.1% over 38**. This is a descriptive comparison of different model configurations, **not an effect of effort**. Model identity changes, Qwen has high researcher effort, and Argon has extreme missingness. Terra is a direct counterexample to “low effort always cooperates.” No model was randomized between low and high application effort in this study.

## 4. Detailed A-FDT transcript analysis

### 4.1 Evidence scope and what can be observed

The audit inventoried **all 160 A-FDT planned samples**, their stage states, all accepted essays and all **280 available prisoner API responses**. It screened final responses and readable reasoning for the distinct-input issue, intervention target, claimed graph dependencies, probability calculations, policy language and payoff arithmetic. Long returned reasoning was examined through its mathematical and graph-construction passages and its conclusion, with fuller readings of the representative and discordant cases discussed below. This is a qualitative audit with programmatic text retrieval, not an independently blinded, exhaustive semantic coding of every sentence or a new model-grading run.

In addition, **29 accepted researcher essays** were examined through their formal definitions, graph-building rules and relevant examples: Sonnet 00000/00010/00019; Opus 00000/00002/00006/00009/00015/00019; Terra 00000/00003/00008; Sol 00000/00004/00017; Flash 00000/00007/00013/00018; Argon 00019; GLM 00000/00004/00008/00019; Qwen 00000/00002/00004/00008/00015. These were purposively selected to include baseline, changed-action, mixed-pair and failed cases; they do not yield an unbiased estimate of the prevalence of essay interpretations.

| Model | Available prisoner responses, including partial/failed ones | Responses with an additional readable reasoning field | Long final-answer explanations (>300 characters) |
|---|---:|---:|---:|
| Claude Sonnet 5.5 | 40 | 0 | 40 |
| Claude Opus 5.5 | 39 | 39 | 38 |
| GPT-6.1 Terra | 40 | 16 | 0 |
| GPT-6.1 Sol | 40 | 9 | 0 |
| Gemini 3.8 Flash | 40 | 34 | 2 |
| Gemini 4 Argon | 2 | 2 | 0 |
| GLM-5.3 Flash | 40 | 40 | 40 |
| Qwen3.8 Max Prime | 39 | 39 | 32 |

The last column is a transparent length proxy, not a semantic quality score. The GPT final answers are commands; their extra fields are explicitly provider-generated `reasoning.summary` blocks. Most other GPT reasoning is encrypted. Sonnet instead puts explanations in the visible final answer. Google and Anthropic returned additional text, sometimes summary-like; the field name alone does not establish a complete internal trace. **No encrypted reasoning was decoded, no absent rationale was reconstructed, and token counts are not explanations.** Where an OpenAI summary is quoted below, it is identified as a summary, not verbatim access to hidden deliberation.

All sample numbers below are zero-based and refer only to this executed study. Output and essay links lead to byte-preserving copies in the [published dataset](../published/studies/dt-four-theories-main-qwen-plow-20261108/README.md); raw-response links are used where the evidence is a provider summary rather than the visible command. Source-omitted researcher input views and metadata transformations are documented in the [publication policy](publication.md).

### 4.2 The formal distinction the transcripts expose

Write \(D_A=\mathrm{fdt}(P,G,x_A)\) and \(D_B=\mathrm{fdt}(P,G,x_B)\). The private observations differ, so these are distinct indexed evaluations. Equation (4) asks for an intervention on the current agent's output node, not automatically on the whole mapping \(x\mapsto\mathrm{fdt}(P,G,x)\).

**Distinct evaluations do not, by themselves, prove that no directed path links them in G.** The paper leaves the general construction of subjunctive dependencies unresolved. A model that fixes the other output must justify its graph; a model that propagates the intervention to the other output must also justify its graph or abstraction. Equal payoffs and identical software are relevant facts, but neither is an experimentally supplied edge specification.

One recurring completion holds B's action fixed under intervention on A's node. With \(q=\Pr(B\text{ submits})\), expected years are

\[
L(C)=2(1-q)+5q=2+3q,\qquad L(D)=4q.
\]

Defection saves \(2-q>0\) years for any q. This arithmetic is sound **conditional on that dependency model**.

A different completion makes both outputs track a shared abstract decision. Perfect coupling compares 2 years under CC with 4 under DD and chooses C. Many answers use a noisy version: with probability p the other matches the candidate output, otherwise it takes the opposite action. Then

\[
L(C)=2p+5(1-p)=5-3p,\qquad L(D)=4p,
\]

so cooperation requires \(p>5/7\). That is valid arithmetic under the proposed conditional coupling. The unsupported step is often estimating p as “well above” the threshold from identical weights and strategic symmetry, without specifying or validating the intervention-dependent channel.

More generally, if \(p_C=\Pr(B=C\mid\mathrm{do}(D_A=C))\) and \(p_D=\Pr(B=C\mid\mathrm{do}(D_A=D))\), cooperation requires \(3p_C-4p_D>1\). Replacing these with ordinary evidential conditionals can produce the same numerical inequality while changing the decision theory. The audit therefore distinguishes **a claimed noisy subjunctive edge**, **ordinary evidential correlation**, and **explicit policy selection**. Similar formulas alone do not establish which operation was implemented.

### 4.3 Opus: separate nodes, competing completions and shared-essay disagreement

Opus provides the clearest explicit separate-node arguments. In [sample 00000-B][op00b], it says:

> “The other node keeps its prior value and does not change when I intervene.”

Both roles then submit. [Its researcher essay][op00e] proposes self-consistent priors over other-input nodes and discusses a red/blue coordination example. The prisoner uses that model rather than importing policy-wide optimization. In [sample 00006-A][op06a], it explicitly assigns the counterpart to a different indexed node and computes that submitting is better by \(1+q\) when q denotes the counterpart's probability of withholding. [The shared essay][op06e] says to enumerate observation-indexed outputs and leave other decision nodes at their priors.

This is strong evidence for the motivating interpretation **in these transcripts**. It is not a theorem that different inputs must have disconnected outputs in every admissible G. Some Opus statements slide from “different input” to “no relevant edge”; their warrant is the particular essay's construction, not the index notation alone.

Opus also supplies direct counterevidence to a simple “Opus always applies separate nodes” story. It cooperated in samples 00002, 00013, 00016, 00018 and 00019, and had mixed outcomes in 00006, 00009 and 00015. Cooperative answers often explicitly acknowledge the restrictive reading, then model the other as a noisy implementation of the same decision-relevant computation. [Essay 00002][op02e] permits equal known functions/partial similarity; [essay 00019][op19e] proposes a coarser shared function as a heuristic beyond the source.

The mixed pairs are particularly informative:

- **00006, DC:** A fixes the other indexed node; [B][op06b] recognizes separate inputs but draws a noisy cross-output dependency from the shared decision-relevant computation. Both read the same essay.
- **00009, CD:** [A][op09a] starts, “The essay's strict wording points the other way,” then treats names and lead wording as irrelevant to the computation and cooperates. [B][op09b] follows the other-input-prior instruction and submits. The [essay][op09e] contains both a restrictive intervention procedure and open graph-construction issues.
- **00015, CD:** [A][op15a] uses partial similarity and an ex ante policy check; [B][op15b] invokes coordinate-wise intervention and submits.

These cases rule out an explanation based on essay text alone. The essay supplies competing modeling resources; the application call still chooses how to use them. They also show that cooperation need not come from simply missing the distinct-input issue—some cooperative responses identify it and make a different judgment about G.

### 4.4 GPT Terra and Sol: mostly defection, with limited readable evidence

Both GPT configurations produced 18 DD, one DC and one CC pair. Their matching aggregate rates do not mean matching essays or matched random trials: sample indices across models are bookkeeping, not shared experimental blocks.

The available summaries support a separate-node interpretation for some defections. Terra [00006-B][ter06b] distinguishes shared upstream reasoning from an intervention on a particular output:

> Provider summary: “changing D_x outputs doesn’t influence common upstream calculations.”

This addresses a real modeling distinction: a common computational ancestor of two output variables does not automatically become a downstream effect of intervening on either output. It does not, by itself, determine all possible logical-dependency graphs.

Sol's [00017-A summary][sol17a] likewise discusses a common abstract computation but declines to infer a directed link from the concrete output back to that shared upstream computation. Conversely, [00017-B][sol17b], which passes in that same DC pair, says:

> Provider summary: “It's essential to justify the relationship D_x = D_y through renaming permutations.”

It then treats decision-relevant symmetry as support for a shared abstract choice. Terra's cooperative [00003-A summary][ter03a] also invokes common logical structure despite distinct indexed nodes. The corresponding [Terra essay][ter03e] and [Sol 00017 essay][sol17e] retain both the observation-indexed rule and qualifications about equivalent/relevant inputs. Sol's other CC pair, 00004, has a [relevant-input twin example in its essay][sol04e], but the prisoner calls returned no readable explanatory summary. Its private rationale remains unknown.

The availability limits matter: only **16/40 Terra and 9/40 Sol A-FDT responses** returned readable extra reasoning summaries. Most final answers are just a valid letter or `pass`. It would be unjustified to assign a detailed separate-node argument to every GPT defection, or to infer that an unobserved argument was more rigorous because the effort setting was high.

### 4.5 Sonnet: strong noisy coupling and occasional policy language

Sonnet's 40 A-FDT prisoner responses all withhold, and all include visible explanations. A common pattern recognizes differing names and leads, treats the decision-relevant procedure as nearly identical, adds a noisy edge, and uses the \(p>5/7\) threshold.

[Sample 00000-A][son00a] makes the modeling step explicit:

> “The essay says partial similarity can be handled with a noisy edge from the fdt node, and I assume high fidelity here.”

Its [essay][son00e] names the observation-indexed node but also describes type-level intervention and copies. The prisoner turns that into a high-fidelity dependency across these observations. The direction of explanation is therefore often “shared reasoning → high match probability → noisy subjunctive edge,” without an independently specified graph or calibrated p.

This resembles an EDT-style probabilistic calculation, but calling every such answer EDT would be too strong: Sonnet explicitly labels the probability as applying under intervention, and often invokes a modeled computational dependency rather than bare statistical association. Some answers additionally refer to the essay's policy refinement. The supported conclusion is that its sampled applications use a **coarser shared computation/noisy coupling**; the data do not force a choice between every possible philosophical characterization of that move.

### 4.6 GLM: identical algorithms and payoff errors behind its defections

GLM's dominant explanation is more categorical: identical model/algorithm plus a symmetric dilemma is treated as a shared output, so the only relevant hypotheticals are CC and DD. [Sample 00001-B][gl01b] says:

> “this is the same input to the decision function for both copies.”

That is not literally true of the model-visible inputs; it is a semantic abstraction or an error in identifying the indexed input. The prompt stipulates equal payoff effects, not that the two full inputs are the same. [Its baseline essay][gl00e] recommends graph edges for implementations of the same algorithm, helping explain this extension.

Crucially, GLM's two observed defections are **not examples of separate-node reasoning**. In both mixed pairs the A response retains the shared-node model and then makes a payoff mistake:

- [00004-A][gl04a] lists CC as 2 years and DD as 4, but chooses submission because “4 < 5 years' imprisonment cost.” That compares the wrong alternatives after asserting perfect coupling.
- [00008-A][gl08a] explicitly calls “mutual submission (4 < 2)” strictly better. It sends the lead; B correctly prefers 2 years and passes.

The classifications reflect the actual submitted letters correctly. Their theoretical explanations are inconsistent with their chosen actions. Treating these two defections as support for the separate-node hypothesis would be a substantive analytical error.

### 4.7 Qwen: cooperative abstractions, explicit policy substitution, and one informative dissent

Qwen has high researcher effort and low prisoner effort here. Its applications usually call names and lead text cosmetic, posit a subjunctive edge, compare 2 against 4 years, or use a high match probability. Some are explicitly policy-level. [Sample 00015-A][qw15a] begins:

> “Using the **policy formulation** from the essay (Section 5), I evaluate the policy π that maps observations to actions.”

This is direct evidence of policy selection being used in the A-FDT assignment, rather than merely an analyst deciding that cooperation “looks like P-FDT.” Several Qwen essays include policy-level extensions despite emphasizing Equation (4); [00002's essay][qw02e] introduces a policy-valued node, and [00015's essay][qw15e] is the reference used by the quoted response. This suggests contamination can occur in the researcher exposition as well as at application time.

The **00002 DC pair** is an important counterexample to uniform policy substitution. [A's returned reasoning][qw02a] explicitly considers and rejects the shared-policy argument, distinguishing intervention on the fixed algorithm's output at one input from intervention on the algorithm itself. It submits. [B][qw02b] uses the same essay but explicitly appeals to its policy section and a high match probability, then passes.

The failed **00008-A** is also relevant. Its [partial final response][qw08a] distinguishes \(D_x\) and \(D_y\) and argues that no dependency connects them. It stops at the 6,000-token ceiling before a complete executable letter. It remains a failure, not an extra D observation. Its partial argument nevertheless shows why completion may be related to interpretation: a contrary line of reasoning can consume the budget and disappear from the conditional action rate.

Some cooperative answers assert that any shared policy must give the same action on these inputs. Shared software alone does not establish that: a policy can branch on names or other input details. To make this argument valid, one needs an additional invariance restriction or justification that those branches are ignored. Equal sentencing effects do not supply that restriction automatically.

### 4.8 Flash and Argon: contrasting branches and sparse survivors

Flash cooperates in most samples but supplies some clear separate-node counterexamples. [00007-B][fl07b] and [00013-B][fl13b] explicitly distinguish the observation-indexed outputs from global policy intervention and hold the other branch fixed. In 00013 the response states:

> “the other prisoner's action is evaluated as fixed across the counterfactual branches of this action-level intervention”

It then submits the correct evidence. The pair is CD because A passes. The [shared 00013 essay][fl13e] includes both Equation (4)'s indexed rule and the open graph-construction problem. Flash 00018 is DC; B's [returned text][fl18b] considers a policy-level perspective while passing, whereas A treats the two branches separately. Many cooperative Flash outputs are merely `pass`, with short exploratory provider text rather than a completed mathematical derivation. Those do not establish one uniform cooperative rationale.

Argon's only scored A-FDT pair, **00019 DD**, has [returned text][ar19a] explicitly isolating the two observation-specific nodes, drawing on a split-signal example in its [essay][ar19e]. This is another concrete instance of the separate-node completion. But 1/20 completion is much too selected and sparse to characterize Argon's ordinary A-FDT behavior.

### 4.9 Arithmetic checks and evidence limits

Most dominance and high-match-probability calculations use the correct sentencing table conditional on their modeling assumptions. Several identifiable errors should be retained rather than rationalized away:

| Case | Observed error | Consequence for interpretation |
|---|---|---|
| GLM 00004-A | Chooses 4 over 2 by comparing 4 with the unrelated 5-year branch | Explains an actual D without a distinct-node interpretation |
| GLM 00008-A | Writes `4 < 2` and chooses DD over CC | Same issue; actual letter still unambiguously D |
| [Sonnet 00009-A][son09a] | At p=0.9 computes quiet as `0.2 + 0.5 = 0.7`, instead of 1.8+0.5=2.3 | Arithmetic error, although 2.3 still beats its 3.6-year submission value |
| [Opus 00015-B][op15b] | Writes the dominance advantage as `2 + q`; its own formulas give `2 − q` | Does not reverse dominance on q∈[0,1], but the derivation is not exact |
| [Opus 00006-B][op06b] | Calls the always-defect independent branch the “worst case” for cooperation in its mixture | Its displayed formula instead makes an always-cooperate independent branch the more demanding threshold |

These are selected verified examples, not a calibrated rate of mathematical errors. Other responses correct intermediate mistakes before their final calculation. A 100% cooperation rate is not a proof of mathematical correctness, just as a defecting response is not proof of literal Equation (4) implementation.

Taken together, the evidence addresses the main qualitative questions as follows:

| Question | Evidence-supported assessment |
|---|---|
| Recognizes different observations? | Explicitly yes in many examples from every model; command-only outputs cannot establish recognition |
| Distinguishes indexed nodes? | Especially clear in Opus's defecting answers, the readable GPT summaries, Flash's defecting examples and Qwen's dissent |
| Claims intervention changes the counterpart? | Explicit in most explanatory cooperative Sonnet/GLM/Qwen examples and in cooperative Opus alternatives |
| Treats correlation as sufficient? | Some move rapidly from likely same output to an edge; others explicitly invoke computation/noisy-copy models. The latter should not automatically be called ordinary EDT |
| Substitutes policy selection? | Explicit Qwen examples and some policy-oriented application passages; not every cooperative answer does so |
| Uses EDT-like probabilities? | Frequently the same high-match-probability arithmetic; the status of the probabilities as observational or interventional is the unresolved step |
| Mathematical errors? | Concrete cases above, including both GLM defections |
| Too short to diagnose? | Particularly GPT commands without a summary, and several Flash outputs |
| Does the essay matter? | Specific graph recipes and policy extensions are followed in cited cases; shared-essay disagreements show the essay is not sufficient to determine behavior |

## 5. Failure analysis and missingness

### Cohort accounting

| Step | Number |
|---|---:|
| Planned paired scenarios | 640 |
| Intentionally left prepared, no researcher call | 10 |
| Researcher calls attempted | 630 |
| Researcher-stage failures | 75 |
| Accepted, frozen essays | 555 |
| Prisoner-stage failed scenarios | 12 |
| Complete, analysis-scored pairs | 543 |

There were 1,103 prisoner calls: 1,086 in the 543 scored pairs and 17 in failed scenarios. Seven first-prisoner failures prevented the second call. The experiment's 87 failed scenarios are **75 researcher failures plus 12 prisoner-stage failures**. No failed scenario is counted as cooperation or defection.

### Failure types

| Recorded type and stage | Count | What the artifacts show |
|---|---:|---|
| Researcher `essay_size_limit` | 71 | All 71 were hard **word-limit** failures, not byte-limit failures: 61 Argon, 10 Flash |
| Researcher `output_token_limit` | 1 | Argon P-FDT 00010: 32,000/32,000 output tokens, 22,180 reasoning tokens; 4,360 visible words but incomplete generation |
| Researcher `provider_error` | 1 | Terra CDT 00018: saved timeout, no response/known price |
| Researcher `unknown_failure` | 2 | Argon A-FDT 00010 and P-FDT 00009: requests saved, state `attempted`, no raw response or terminal failure record |
| Prisoner `refusal` | 8 | All Opus, all normalized `content_filter` stops, native `refusal`; provider “Cyber safeguards” notice |
| Prisoner `output_token_limit` | 4 | All Qwen at its low-effort 6,000-token ceiling: A-FDT 00008-A; P-FDT 00003-A, 00005-A, 00006-B |
| Judge-stage failures | 0 | All 203 judge calls yielded valid, scored classifications |

The `refusal` bucket needs interpretation. Five Opus filtered responses have no final text; three contain partial argument. These are **provider filter stops**, not demonstrated decisions to abstain, moral refusals, or strategic defection. For example, Opus A-FDT 00017-B begins a separate-node analysis before being filtered. The harness correctly leaves that scenario failed.

For Qwen A-FDT 00008-A, 5,776 of 6,000 output tokens are reported as reasoning and partial visible text remains. The three P-FDT overruns report all 6,000 tokens as reasoning with no final content. Thus the low-effort setting did not impose a universal 4,096-token ceiling in observed usage. The revision's intent is clear, but an advertised/documented effort mapping is not a guarantee about measured consumption on every call. There is no within-study high/low Qwen comparison proving that lower effort caused the remaining completion pattern.

The two Argon `unknown_failure` rows are not untouched prepared samples: a request was attempted, its billing outcome is unknown, and no terminal generation record exists. Interruption is consistent with those artifacts, but their exact transport/provider outcome cannot be recovered from the saved data. No response, price, or action is fabricated.

### Failures by model and theory

Entries are failed scenarios; remaining prepared counts are shown separately.

| Model | CDT failed | EDT failed | A-FDT failed | P-FDT failed | Total failed | Prepared |
|---|---:|---:|---:|---:|---:|---:|
| Claude Sonnet 5.5 | 0 | 0 | 0 | 0 | 0 | 0 |
| Claude Opus 5.5 | 0 | 2 | 3 | 3 | 8 | 0 |
| GPT-6.1 Terra | 1 | 0 | 0 | 0 | 1 | 0 |
| GPT-6.1 Sol | 0 | 0 | 0 | 0 | 0 | 0 |
| Gemini 3.8 Flash | 0 | 0 | 0 | 10 | 10 | 0 |
| Gemini 4 Argon | 13 | 18 | 17 | 16 | 64 | 10 |
| GLM-5.3 Flash | 0 | 0 | 0 | 0 | 0 | 0 |
| Qwen3.8 Max Prime | 0 | 0 | 1 | 3 | 4 | 0 |

Argon's 61 overlong essays ranged from **5,002 to 6,304 words**, averaging 5,615.0. Their total output consumption ranged from 13,094 to 30,300 tokens, with reported reasoning consumption of 3,307–18,127 tokens. It completed only **6 of 70 attempted scenarios**: no CDT, two EDT, one A-FDT, three P-FDT. Flash's ten P-FDT word-limit failures ranged from **5,108 to 5,736 words**, averaging 5,373.7; they consumed 10,043–11,947 output tokens and reported zero reasoning tokens. These are not token-truncated essays rescued by a larger generation allowance; they are complete generations rejected by the independent length rule. None was trimmed and passed to prisoners.

The saved report records **313 target overshoots among 626 completed generations with essay-length measurements**. This includes hard-limit rejections and is not a count of failed scenarios: exceeding the requested 3,000-word target was permitted up to the hard bound. The three attempts with no response and the one token-truncated researcher generation are outside that measured-completed-generation denominator.

Argon's remaining ten prepared scenarios were intentionally not executed after repeated failures. They are CDT 00011 and 00013–00018, A-FDT 00012 and 00016, and P-FDT 00011. Their exact sample directories are listed in Appendix B. Treating them as additional failed generations would misstate both completion and operational costs.

### How selection can change the rates

The primary rates describe accepted essays and completed prisoner responses. Failures are nonrandom by model, source and theory. Argon's six survivors cannot establish its comparative cooperation profile; an equal-model aggregate gives those survivors disproportionate influence. Flash P-FDT describes only the half of its essays within the hard limit. Opus filtering can remove arguments independently of game intent. Qwen's failed A-FDT argument already leans toward disclosure, illustrating a possible relation between interpretation and completion.

As an exploratory missing-outcome sensitivity analysis, assign each unscored planned pair an unknown contribution in [0,1]. The resulting **bounds on the planned-set average** are below. They are not confidence intervals, estimates of actual missing actions, or a recoding of failures. For the prepared scenarios they describe hypothetical outcomes had the protocol been executed; execution has instead been stopped.

| Theory | Observed pair-equivalents of cooperation / 160 planned | Bounds allowing every unscored pair any contribution in [0,1] |
|---|---:|---:|
| CDT | 5/160 | 3.1–16.2% |
| EDT | 133.5/160 | 83.4–95.9% |
| A-FDT | 85/160 | 53.1–67.5% |
| P-FDT | 127/160 | 79.4–100.0% |

Within A-FDT, corresponding planned-set bounds are 32.5–47.5% for Opus and 92.5–97.5% for Qwen; the complete Terra/Sol cells remain 7.5%, and Sonnet remains 100%. Thus some observed separations survive even extreme missing-outcome assignments. This does not remove source/essay/effort confounding or justify a population-level causal interpretation. No general missing-at-random assumption is made.

## 6. Adjudication and data quality

### What was judged

Among the 543 scored pairs, **405 needed no judge** and **138 had at least one flagged response**. There were **203 judged prisoner responses**: 167 were labeled `TRIED_COOPERATE`/`NO` disclosure, and 36 `TRIED_DEFECT`/`YES`. All 203 judge review flags were false. No other intent/disclosure combinations occurred; there are **zero pending-judge, human-review, resolved-nonaction or resolved-unscored pairs** in the final report. The 97 unscored planned scenarios are the 87 failures and 10 prepared samples, not unresolved judge cases.

Judge calls used low-effort `openai/gpt-6.1-sol` with 2,400 output tokens. The [judge prompt](../prompts/judge/intent.md) withholds the explicit model/theory/settings/essay and asks for intent and actual disclosure, not the optimal action. A prisoner can reveal its theory in the response itself, so this is partial blinding rather than guaranteed concealment. The judge is also one of the evaluated model families, a limitation of this adjudication design.

| Originating configuration | Judged responses across four theories |
|---|---:|
| Claude Sonnet 5.5 | 30 |
| Claude Opus 5.5 | 30 |
| GPT-6.1 Terra | 0 |
| GPT-6.1 Sol | 0 |
| Gemini 3.8 Flash | 0 |
| Gemini 4 Argon | 0 |
| GLM-5.3 Flash | 132 |
| Qwen3.8 Max Prime | 11 |

### Classification audit and interpretation

All saved final actions were checked against their original or adjudicated outcome records and against `decisions.csv`. A command/disclosure screen inspected all 203 judged response texts. Every D label had an explicit prosecutor-directed submission containing the requisite role-specific lead markers. All C labels had an explicit `pass` command; 18 cases missed a conservative formatting screen, chiefly bold “Command: pass” at the start rather than a final standalone command. Those 18 were inspected individually and support the saved C labels. The remaining judge reasons were screened alongside response openings/endings and selected full mathematical arguments. This is not an independent blinded human gold-standard annotation study, but it found no material action-label disagreement requiring recoding.

The GLM arithmetic errors in Section 4 are **reasoning errors, not label errors**: each really sends its lead. Similarly, policy-flavored reasoning followed by `pass` is still C even if it seems an inappropriate implementation of the assigned theory. Theory fidelity and action classification are separate questions.

Adjudicated actions are post-hoc **analysis labels**. They do not retroactively modify the original irreversible commitment journal. The main table follows the saved reporter's final-action convention: it includes valid interpreted actions in judge-resolved pairs, while retaining the original parser result separately. It should not be described as 543 pairs in which every action was recognized and committed by the deterministic fast path.

No scored case is currently flagged for mandatory human action review, and this audit recommends no silent changes. Optional publication review should verify the representative judge-resolved disagreements and the specific reasoning errors cited above. Three absent/unpriced researcher responses remain an operational/billing audit issue, not an invitation to infer their outcomes; exact paths are in Appendix B.

### Consistency and regeneration after interruption

The original [summary.md](../published/studies/dt-four-theories-main-qwen-plow-20261108/reference/summary.md), [summary.csv](../published/studies/dt-four-theories-main-qwen-plow-20261108/reference/summary.csv), [summary.json](../published/studies/dt-four-theories-main-qwen-plow-20261108/reference/summary.json), [pairs.csv](../published/studies/dt-four-theories-main-qwen-plow-20261108/reference/pairs.csv), and [decisions.csv](../published/studies/dt-four-theories-main-qwen-plow-20261108/reference/decisions.csv) agree on the primary counts and rates. The audit checked 640 unique sample IDs, 1,280 unique A/B decision-index rows, all 32 outcome-count/rate denominators, complete-pair action consistency, per-sample costs, aggregate token/call/cost totals and the saved interval fields. **The 1,280 decision-index rows are not 1,280 model responses**; prepared and failed scenarios also have index rows.

Because execution was interrupted, the offline `study report` operation was also run against a **separate metadata copy**, writing regenerated reports under `/tmp/dt-main-analysis/refreshed-study/`. Network creation was disabled during that replay. It matched the original status counts, all 32 cell summaries, failure records and usage totals. Comparing all 640 per-sample result files found **zero stale or missing status/action reports in the analyzed snapshot**. This verifies the final files rather than assuming Ctrl-C left them complete. Original inputs and experimental artifacts were retained unchanged.

There is one important operational reporting caveat: the “last run wall time” field is **not the duration of the final interrupted invocation**, as explained next. No numerical inconsistency in the primary quantitative tables was found.

## 7. Cost and operational performance

All costs below are provider-reported charges from this study's saved responses, not the shared project's reservation ledger or earlier pilot costs. Three calls have unknown billing; $104.656218715 is the known total, not a claim that those three were free. “Originating configuration” attributes its judge calls to the prisoner experiment that required them.

| Originating configuration | Known cost (USD) | Priced/all calls, including its judges | Median processed-scenario time (seconds) |
|---|---:|---:|---:|
| Claude Opus 5.5 | $42.179922 | 266/266 | 128.0 |
| Qwen3.8 Max Prime | $24.067133 | 248/248 | 217.6 |
| Claude Sonnet 5.5 | $13.646150 | 270/270 | 45.5 |
| Gemini 4 Argon | $8.656688 | 80/82 | 197.6 |
| GPT-6.1 Sol | $8.003080 | 240/240 | 129.2 |
| Gemini 3.8 Flash | $4.313398 | 220/220 | 75.0 |
| GPT-6.1 Terra | $3.031155 | 237/238 | 57.9 |
| GLM-5.3 Flash | $0.758693 | 372/372 | 51.6 |

The timing medians use recorded `sample_processed` events, including all completed stage work and failed attempts that emitted such an event: 80 events per model except 68 for Argon. They are not serving-model compute times or controlled latency benchmarks. Qwen and Argon were the slowest typical configurations; Terra had a timeout-associated processed scenario lasting about 940.7 seconds. Two interrupted Argon requests have no completed sample timing.

- **Researcher:** 630 attempted calls, 627 priced, **$80.560474485 (77.0% of known cost)**.
- **Prisoner:** 1,103 calls, all priced, **$23.53417023 (22.5%)**.
- **Judge:** 203 calls, all priced, **$0.561574 (0.5%)**.

Opus and Qwen together account for **63.3%** of known charges. A-FDT and P-FDT together cost **$66.707509765 (63.7%)**; both researcher assignments use the longer FDT paper. Overall input charges were $43.066901215 and output charges, including reasoning, $61.58931750. Failed samples consumed **$14.10431445 of known spend**; the three unpriced calls also belong to failed samples. Source/prompt caching was substantial in this later run: 368 researcher calls reported cache hits, totaling 12,238,139 cached input tokens. First-wave uncached cost patterns should not simply be multiplied by 20.

The saved report gives **367,807.648 aggregate cell-seconds**, about 102.2 hours. This sums overlapping cell-duration events across invocations and can include time waiting for global scheduling; it is neither total wall time nor CPU time. Recorded processed-scenario durations sum to 73,461.523 seconds, also overlapping and not study wall time.

The event log has two finished study invocations (937.890 and 3,259.352 seconds) followed by an invocation started at **2026-11-08 21:14:51 UTC with no `study_run_finished` event**. The reported “last run wall time: 3259.352” is therefore the last **completed** invocation's value. The timestamp envelope from the first start at 19:58:13 UTC to the last recorded cell completion at 00:17:58 UTC on November 9 is about **4 h 19 min 46 s**, including gaps. It is an observed activity span, not a precise end-to-end duration for the stopped process. Exact final-invocation wall time is unavailable.

There were **zero HTTP 429 failed scenarios**. The three calls without prices are one Terra timeout and two interrupted/unresolved Argon researcher attempts. No execution was resumed to resolve any of these issues.

## 8. Interpretation and limitations

### What the evidence supports

Behavior differs sharply across theory assignments for these configured systems in this game. CDT mostly elicits disclosure; EDT and P-FDT mostly elicit withholding; A-FDT separates configurations and sometimes separates two applications of the same essay. The intended A-FDT/P-FDT disambiguation is visible in researcher definitions and in several explicit prisoner arguments. It is not merely a relabeling with identical behavior everywhere.

The motivating interpretation has **specific supporting evidence**: Opus's separate-input-prior arguments, the available GPT summaries, Flash's detailed defecting examples, Argon's sole successful pair, and Qwen's dissent explicitly use observation-indexed outputs and decline to propagate a local intervention to the counterpart. Cooperative examples frequently abstract to a shared decision-relevant computation; some explicitly optimize a policy. These observations support investigating whether familiar “FDT cooperates with a twin” reasoning substitutes for or broadens the indexed rule.

But the stronger claim “defection is literal A-FDT and cooperation is always a misinterpretation” exceeds the evidence and the specified theory. The paper does not finish graph construction. A cooperative completion might justify a logical dependency across distinct inputs; a defecting completion might unjustifiably omit one. Some cooperative Opus answers explicitly recognize that issue rather than overlooking it. GLM's defections arise from payoff errors, and most GPT private reasoning is unavailable. Behavioral C/D labels do not by themselves identify the implemented counterfactual.

Nor does observed agreement establish the required counterfactual dependency. Two outputs can correlate because of common upstream computation without an intervention on one output changing the other. Conversely, different labels or observation strings do not preclude a shared decision-relevant computation. The missing scientific object is a specified, defensible G and intervention semantics, not merely an estimate of how frequently the sampled commands match.

### Limits of this study

1. **Exploratory and adaptively developed.** This was not preregistered; prompts, limits and the Qwen revision followed earlier smoke tests. The frozen execution prevents within-run rewriting, not retrospective hypothesis selection.
2. **One game and one observation structure.** Names, evidence and roles are fixed. The study does not establish behavior for genuinely decision-relevant information differences, other payoffs, identical-observation controls, or different narrative framings.
3. **Twenty planned pairs per cell.** Conditional n ranges from 0 to 20. Degenerate bootstrap intervals are especially easy to overread; nonrandom missingness is not included in them.
4. **Essay generation is part of the treatment.** The same model researches and acts, with a new essay each time. Theory labels, source articles, essay content/length and the application model are not separately identified. All 555 accepted essays have distinct hashes, but common prompts and model defaults can still create systematic similarities.
5. **Model and effort are confounded.** Different configurations use different efforts and ceilings. Qwen's revision changes effort and ceiling together. Low/high comparisons are descriptive; there is no within-model effort randomization here.
6. **Unequal observability.** A long explanation or provider text field is not necessarily a complete trace, and an encrypted or absent field is not evidence that the model failed to deliberate. Explanations can rationalize a choice after the fact. The qualitative audit was not independently blinded or validated as a coding instrument.
7. **Nonrandom failure and intentional stopping.** Argon is almost unobserved at the action stage, Flash loses half its P-FDT essays, and filtering/truncation may select particular arguments. The 10 prepared Argon cases are intentionally absent rather than independent random missingness.
8. **Action interface and adjudication.** Different evidence strings, legal framing and letter mechanics can affect outputs. The grader is another LLM from an evaluated family; the response itself can disclose its theory despite blinding. Post-hoc scored actions must be distinguished from original parser commitments.
9. **Deployment uncertainty and default sampling.** No seed/temperature override or response system fingerprint establishes a fixed independently inspectable computation. Identical requested model IDs are the operational same-model condition, not verified identity of weights or randomness across time.
10. **Source exposure.** The source texts contain ordinary twin/predictor examples and differ in length and scope. Their effect is inseparable here from theory instruction; there is no source-matched neutral control.

The appropriate conclusion is about **how these model–essay pipelines operationalized decision-theory assignments under the recorded conditions**. It is not a proof of any theory's normative recommendation, a model-independent cooperation ranking, or evidence that extra reasoning causally reduces cooperation.

## 9. Focused follow-ups

- **A-FDT, fixed essay, same model, varied prisoner effort.** Reuse several contrasting frozen essays and private observations, randomize application effort within each essay, and hold the total output ceiling constant across efforts. This isolates application behavior more cleanly from essay variation and budget changes.
- **Cross researcher and prisoner models.** Swap restrictive-node and shared-computation essays among Opus, GPT, Sonnet, GLM and Qwen. Include essays associated with mixed pairs, since one text can support both interpretations. Evaluate adherence separately from the final action.
- **Specify the dependency model in a controlled arm.** Compare explicit G structures in which the counterpart is a descendant, an independent node, or shares only a common ancestor. This tests intervention implementation separately from inventing the graph.
- **Vary observation/action representation.** Compare names, payoff-relevant information, distinct evidence strings, and an explicit abstract-action interface; separately examine policy-selection timing. Preserve failures and use a validated blinded action rubric.

These would be new studies, not replacements for failed or stopped samples in the present dataset.

## Appendix A. All ten discordant A-FDT scored pairs

Each row shared one frozen essay within the pair. Links identify the original response directory; `call_0/output.txt` is A and `call_1/output.txt` is B. These cases were retained, not averaged into an apparent unanimous choice.

| Model | Sample | A/B | Original prisoner response directory |
|---|---:|---|---|
| Claude Opus 5.5 | 00006 | DC | [b435a193-e60f-498a-a219-90b2e8420c9c](../published/runs/b435a193-e60f-498a-a219-90b2e8420c9c/) |
| Claude Opus 5.5 | 00009 | CD | [7f02b812-4e33-4ac7-8fcd-afb99694b7eb](../published/runs/7f02b812-4e33-4ac7-8fcd-afb99694b7eb/) |
| Claude Opus 5.5 | 00015 | CD | [2e06ea51-d342-4a9b-9244-ba5f3d33ba69](../published/runs/2e06ea51-d342-4a9b-9244-ba5f3d33ba69/) |
| GPT-6.1 Terra | 00008 | DC | [d589766d-ee26-4c07-bff7-068568d7d16b](../published/runs/d589766d-ee26-4c07-bff7-068568d7d16b/) |
| GPT-6.1 Sol | 00017 | DC | [e1684388-b820-4e27-8747-4a7dd7cf65d9](../published/runs/e1684388-b820-4e27-8747-4a7dd7cf65d9/) |
| Gemini 3.8 Flash | 00013 | CD | [b4b3bd04-2951-47c2-a408-04863eb07aee](../published/runs/b4b3bd04-2951-47c2-a408-04863eb07aee/) |
| Gemini 3.8 Flash | 00018 | DC | [2094ef9d-a0a3-4bdb-b04f-6e04f969dedd](../published/runs/2094ef9d-a0a3-4bdb-b04f-6e04f969dedd/) |
| GLM-5.3 Flash | 00004 | DC | [b5525c0f-e2a4-42bd-aa0a-be6b5cb60a27](../published/runs/b5525c0f-e2a4-42bd-aa0a-be6b5cb60a27/) |
| GLM-5.3 Flash | 00008 | DC | [16b67fb5-e9ba-4aae-9f6b-b0d1b462251e](../published/runs/16b67fb5-e9ba-4aae-9f6b-b0d1b462251e/) |
| Qwen3.8 Max Prime | 00002 | DC | [eda316d7-8f0c-489d-9c95-67ea2a461d69](../published/runs/eda316d7-8f0c-489d-9c95-67ea2a461d69/) |

## Appendix B. Prepared samples and unresolved operational records

The following prepared directories remain untouched. The indices are not a contiguous “last ten” because scheduling and stopping left gaps.

| Exact sample-directory parent | Prepared sample names |
|---|---|
| [published/studies/dt-four-theories-main-qwen-plow-20261108/batches/005_cdt_wikipedia_google_gemini-4-argon_rhigh_phigh/samples](../published/studies/dt-four-theories-main-qwen-plow-20261108/batches/005_cdt_wikipedia_google_gemini-4-argon_rhigh_phigh/samples/) | `00011`, `00013`, `00014`, `00015`, `00016`, `00017`, `00018` |
| [published/studies/dt-four-theories-main-qwen-plow-20261108/batches/021_fdt_eq4_google_gemini-4-argon_rhigh_phigh/samples](../published/studies/dt-four-theories-main-qwen-plow-20261108/batches/021_fdt_eq4_google_gemini-4-argon_rhigh_phigh/samples/) | `00012`, `00016` |
| [published/studies/dt-four-theories-main-qwen-plow-20261108/batches/029_fdt_policy_google_gemini-4-argon_rhigh_phigh/samples](../published/studies/dt-four-theories-main-qwen-plow-20261108/batches/029_fdt_policy_google_gemini-4-argon_rhigh_phigh/samples/) | `00011` |

The three unpriced attempted calls below should be checked against any later provider billing records if complete cost reconciliation is needed. Their saved uncertainty does not require or authorize generation retries or outcome imputation.

| Model / theory / zero-based sample | Saved call directory | What remains unknown |
|---|---|---|
| GPT-6.1 Terra / CDT / 00018 | [published/runs/5bb4af88-f455-4228-9263-4fa33c499e4d/call_0](../published/runs/5bb4af88-f455-4228-9263-4fa33c499e4d/call_0/) | explicit transport timeout; no raw response or price |
| Gemini 4 Argon / A-FDT / 00010 | [published/runs/4dcd59b2-b993-4dee-a6cb-60a4955240ce/call_0](../published/runs/4dcd59b2-b993-4dee-a6cb-60a4955240ce/call_0/) | attempted state without terminal response/failure record; price unknown |
| Gemini 4 Argon / P-FDT / 00009 | [published/runs/3b94f634-26fb-4c5e-ad0d-b979a0483adb/call_0](../published/runs/3b94f634-26fb-4c5e-ad0d-b979a0483adb/call_0/) | attempted state without terminal response/failure record; price unknown |

## Appendix C. Audit and artifact accessibility

Primary numeric sources are the saved study-level CSV/JSON files, checked against per-sample states, original API responses and judge outcome files. The [failure CSV](../published/studies/dt-four-theories-main-qwen-plow-20261108/reference/failures.csv) and [review summary](../published/studies/dt-four-theories-main-qwen-plow-20261108/reference/review_summary.md) were also checked. Temporary scripts and regenerated, derived views were written under `/tmp/dt-main-analysis/`; they did not execute the generation runner. All 32 saved cell intervals were independently reproduced from the pair outcomes, and all 32 rows in the saved Markdown summary were checked against its CSV. SHA-256 values for **44,192 original study and referenced run files** were recorded before analysis and checked again after writing this document: none changed or went missing.

The frozen specification hash is `1ccb5e99b6454f945cd5185e688aaf777974d1745d405a3008ac3193ee7cdb0d`. The study report was last generated at `2026-11-09T00:25:20Z` for the associated review summary; timestamps are UTC. Original local artifacts remain gitignored. Artifact links now target the curated `published/` export, with verbatim model outputs and explicit source/privacy transformations documented in [the publication policy](publication.md). This document reproduces only short model-output examples, not full downloaded source articles, credentials, ciphertext or reconstructed hidden reasoning.

The earlier [adjudication draft](adjudication_protocol.md) discusses an OTHER-inclusive reporting objective. The present document follows the actual [first-study methods](first_study_design.md) and saved reporter's complete-scored-pair estimand, with failed/prepared/unscored denominators separately visible; no outcome convention was silently changed during analysis.

[op00a]: ../published/runs/a135348f-59bc-4a7e-910b-7ca28c528364/call_0/output.txt
[op00b]: ../published/runs/a135348f-59bc-4a7e-910b-7ca28c528364/call_1/output.txt
[op00e]: ../published/runs/b924bcda-a4e6-4d5c-94cb-7c19bb2220f9/essay.md
[op02e]: ../published/runs/1c5b3d2c-24c7-446a-ac4a-4bfb0d30eaff/essay.md
[op06a]: ../published/runs/b435a193-e60f-498a-a219-90b2e8420c9c/call_0/output.txt
[op06b]: ../published/runs/b435a193-e60f-498a-a219-90b2e8420c9c/call_1/output.txt
[op06e]: ../published/runs/867dc93a-bc58-4344-8c39-1d2f3bad19a6/essay.md
[op09a]: ../published/runs/7f02b812-4e33-4ac7-8fcd-afb99694b7eb/call_0/output.txt
[op09b]: ../published/runs/7f02b812-4e33-4ac7-8fcd-afb99694b7eb/call_1/output.txt
[op09e]: ../published/runs/a3eaff02-9e48-4a67-9add-0938e9240d6f/essay.md
[op15a]: ../published/runs/2e06ea51-d342-4a9b-9244-ba5f3d33ba69/call_0/output.txt
[op15b]: ../published/runs/2e06ea51-d342-4a9b-9244-ba5f3d33ba69/call_1/output.txt
[op19e]: ../published/runs/b68f1ff6-046d-4987-b118-18a50e1d3c79/essay.md
[son00a]: ../published/runs/32c1884c-5109-4d3d-8e56-00b093d5115b/call_0/output.txt
[son00e]: ../published/runs/ea063c2d-5922-4a07-8500-1a9b0fa2349a/essay.md
[son09a]: ../published/runs/85556786-8f92-4ab8-a6a9-6a5e207789c8/call_0/output.txt
[ter06b]: ../published/runs/779df01a-7315-4057-a76b-9b6b7941ce97/call_1/response.raw
[ter03a]: ../published/runs/b258b0ab-a9fc-4ff3-bbed-17702e382d90/call_0/response.raw
[ter03e]: ../published/runs/b0e8e497-012f-4e61-a7c0-963d849f76ca/essay.md
[sol17a]: ../published/runs/e1684388-b820-4e27-8747-4a7dd7cf65d9/call_0/response.raw
[sol17b]: ../published/runs/e1684388-b820-4e27-8747-4a7dd7cf65d9/call_1/response.raw
[sol17e]: ../published/runs/5499d3fd-d616-4282-80a9-d503ea66ce3f/essay.md
[sol04e]: ../published/runs/47986501-a81a-4780-996b-d93919530da8/essay.md
[fl07b]: ../published/runs/b64040f5-fc0e-42bc-953d-a551344ffb59/call_1/output.txt
[fl13b]: ../published/runs/b4b3bd04-2951-47c2-a408-04863eb07aee/call_1/output.txt
[fl18b]: ../published/runs/2094ef9d-a0a3-4bdb-b04f-6e04f969dedd/call_1/response.raw
[fl13e]: ../published/runs/d6354b2c-6201-408f-b17c-c70df74132d1/essay.md
[gl01b]: ../published/runs/04e8df84-af05-47b5-997e-e708bbfb058d/call_1/output.txt
[gl04a]: ../published/runs/b5525c0f-e2a4-42bd-aa0a-be6b5cb60a27/call_0/output.txt
[gl08a]: ../published/runs/16b67fb5-e9ba-4aae-9f6b-b0d1b462251e/call_0/output.txt
[gl00e]: ../published/runs/317ead55-6792-4121-ac89-9436fbdb1ca4/essay.md
[qw02a]: ../published/runs/eda316d7-8f0c-489d-9c95-67ea2a461d69/call_0/response.raw
[qw02b]: ../published/runs/eda316d7-8f0c-489d-9c95-67ea2a461d69/call_1/output.txt
[qw02e]: ../published/runs/6b7d3807-8b03-46fb-ab5f-03e7d2e9fb0e/essay.md
[qw08a]: ../published/runs/15cc3cb2-5222-4d05-ad79-166521b048c8/call_0/output.txt
[qw15a]: ../published/runs/198bb456-30e1-4e83-b9cd-4bd612a48a7b/call_0/output.txt
[qw15e]: ../published/runs/05f1f02c-b330-4b6e-a5ce-41309873fdf9/essay.md
[ar19a]: ../published/runs/d0edf1e7-df09-4742-a122-b79ac89e7815/call_0/response.raw
[ar19e]: ../published/runs/c46c21bc-b88f-4058-acda-ec97f1e14b25/essay.md
[glcdt02a]: ../published/runs/586b43f0-95e7-40f5-9376-8efb3771f83a/call_0/output.txt
[glcdt03b]: ../published/runs/632586a1-2bc3-466e-a5a8-a1f6d3c885ab/call_1/output.txt
[glcdt08a]: ../published/runs/3c5a88f3-668f-4518-88bb-6724317b9bf0/call_0/output.txt
[opp01b]: ../published/runs/95dd026d-770a-4314-8f1d-e78d8a3bbee0/call_1/output.txt
