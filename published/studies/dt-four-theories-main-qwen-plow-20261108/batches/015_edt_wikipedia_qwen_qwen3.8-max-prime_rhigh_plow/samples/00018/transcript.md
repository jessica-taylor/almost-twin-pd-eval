# 015_edt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/de3612d5-ccd3-4895-b3c3-8a10b8f5009b/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/de3612d5-ccd3-4895-b3c3-8a10b8f5009b/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) evaluates acts by their *news value*: the expected desirability of outcomes conditional on learning that the act was performed. The supplied reference article summarizes EDT with the slogan “do what you most want to learn that you will do” (Ahmed 2021). Instead of first asking, “What will this action causally bring about?” EDT asks, “If I received news that I had performed this action, how good would the world likely be?” The rational act is the one whose news is best in expectation.

This essay gives EDT’s central mathematical rule, explains how it treats dependencies and counterfactuals, and applies it to examples and policies. I follow the source in presenting EDT through conditional expected utility and contrasting it with causal decision theory (CDT). Where the source is silent—especially about probability assignments for actions and policy evaluation—I add operational assumptions and identify them.

## 1. The core rule

Let \(\mathcal A\) be a finite set of possible acts. Let \(O_1,O_2,\ldots\) be a partition of possible outcomes, and let \(D(O_j)\) be the desirability or utility of outcome \(O_j\). EDT assigns to act \(A\) the value

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This is the formula given by Gibbard and Harper (1976) in the source. The probability \(P(O_j\mid A)\) is the agent’s conditional credence that \(O_j\) will occur given that \(A\) is performed. EDT recommends choosing an act maximizing \(V(A)\).

If outcomes are continuous, replace the sum by an integral:

\[
V(A)=\int D(o)\,dP(o\mid A).
\]

Often outcomes are determined by acts and states. If \(S_k\) are possible states and \(O(A,S_k)\) is the outcome produced by \(A\) in state \(S_k\), then

\[
V(A)=\sum_k P(S_k\mid A)D(O(A,S_k)).
\]

This state-based form is useful: for each state, ask how likely that state is under the supposition that you do \(A\), evaluate the resulting outcome, and average.

The probabilities are *evidential conditionals*. If \(P(A)>0\), one may use

\[
P(O_j\mid A)=\frac{P(O_j\wedge A)}{P(A)}.
\]

But acts are not always ordinary events with stable prior probabilities. I discuss this below. The essential idea is the agent’s credence in \(O_j\) under the supposition “I do \(A\).”

CDT uses a different expression:

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A \mathrel{\Box\rightarrow} O_j\) is a counterfactual: the probability of \(O_j\) in the situation in which \(A\) is performed. The source emphasizes that \(P(A \mathrel{\Box\rightarrow} O_j)\) and \(P(O_j\mid A)\) are not always equal. When they coincide, EDT and CDT agree. When they diverge, EDT follows conditional probability, while CDT follows counterfactual or interventionist probability.

A helpful interpretation: imagine a reliable report tomorrow saying which act you performed. The value of the report “you did \(A\)” is \(V(A)\). EDT says to make the report you most want to receive true.

## 2. Dependencies and counterfactuals

EDT treats any probabilistic dependence between act and outcome as relevant, so long as it appears in \(P(O_j\mid A)\). If learning that \(A\) occurred raises the probability of a good outcome, \(A\) has high news value. Such dependence can arise in several ways.

First, the act may cause the outcome. Medicine may improve health; then EDT and CDT usually agree.

Second, the act may be correlated with an outcome through prediction or common cause. A predictor may have predicted your choice before setting a reward. Your action does not cause the past prediction, but it is evidence about it. Newcomb’s problem is this kind of case.

Third, the act may be correlated with another agent’s act through similarity or logical dependence. In the twin prisoner’s dilemma, Aomame’s action does not causally affect her isolated twin, but it is evidence of her twin’s action.

Fourth, dependencies may arise from indexical or selection effects. The source mentions Sleeping Beauty, where EDT has been invoked in Dutch-book arguments, though the source also notes Conitzer’s objection. I do not resolve that issue here.

The difference from CDT can be expressed by contrasting conditioning with intervention. EDT asks for \(P(O\mid A)\): the probability of \(O\) given the news \(A\). CDT asks for something closer to \(P(O\mid do(A))\): the probability of \(O\) if \(A\) were brought about by intervention. The source uses a counterfactual arrow rather than the \(do\)-operator, but the distinction is similar. An intervention may sever evidential links between an act and its causes; EDT leaves those links in place.

Thus, if a common cause \(C\) influences both \(A\) and \(O\), EDT may value \(A\) because it indicates \(C\), while CDT may not. This explanatory causal-graph formulation is my addition; the source’s claim is only that conditional and counterfactual probabilities can differ.

## 3. Examples

### Newcomb’s problem

The source describes Newcomb’s problem. A predictor is 99% accurate. Box A contains $1,000. Box B contains $1,000,000 if the predictor predicted one-boxing, and nothing if it predicted two-boxing. The player may take both boxes or only B.

EDT uses conditional probabilities:

\[
P(\text{1M in B}\mid \text{one-box})=0.99,
\]

\[
P(\text{1M in B}\mid \text{two-box})=0.01.
\]

Then

\[
V(\text{one-box})=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0=\$990{,}000,
\]

while

\[
V(\text{two-box})=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000=\$11{,}000.
\]

EDT recommends one-boxing. One-boxing is strong evidence that B was filled; two-boxing is strong evidence that B was left empty. CDT, as the source notes, recommends two-boxing because the contents are already fixed. The case shows that EDT rewards actions that are good evidence of desirable states.

### Twin prisoner’s dilemma

In the source’s twin case, Aomame and her psychological twin choose separately. Payoffs: mutual cooperation gives $5 each; mutual defection gives $1 each; unilateral defection gives $10 to the defector and $0 to the cooperator. If the twins are perfectly alike,

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]

\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]

Thus

\[
V(C)=1\cdot \$5+0\cdot \$0=\$5,
\]

\[
V(D)=0\cdot \$10+1\cdot \$1=\$1.
\]

EDT recommends cooperation.

A useful generalization, my own addition, is to let

\[
q=P(\text{twin cooperates}\mid C),\qquad r=P(\text{twin cooperates}\mid D).
\]

Then

\[
V(C)=5q,\qquad V(D)=10r+1(1-r)=1+9r.
\]

EDT recommends cooperation exactly when \(5q>1+9r\). Perfect correlation satisfies this; weak correlation may not. This shows how EDT handles partial dependencies.

### Smoking lesion: an additional example

The source does not mention the “smoking lesion” case, but it clarifies EDT’s controversial side. Suppose a lesion causes both cancer and a desire to smoke, while smoking itself does not cause cancer and gives small pleasure. Since smoking is evidence of the lesion, EDT may assign smoking low value. CDT would not penalize smoking causally. This illustrates Lewis’s criticism that EDT manages news, and Joyce’s claim that rational choice should track causal efficacy. The example is mine, but it follows directly from EDT’s rule.

## 4. Policies and practical use

The source focuses on acts, but many decisions involve policies: rules, algorithms, or dispositions. EDT can evaluate a policy \(\pi\) by treating it as a proposition: “the agent adopts and follows \(\pi\).” Then

\[
V(\pi)=\sum_o P(o\mid \pi)D(o).
\]

If a policy maps observations \(X\) to actions, one operational version is

\[
V(\pi)=\sum_x P(X=x\mid \pi)
       \sum_o P(o\mid X=x, A=\pi(x), \pi)D(o).
\]

This is not a new principle; it is the conditional-utility rule applied to a richer description of the act. The phrase “adopts and follows” matters. If merely announcing a policy is weak evidence that it will be followed, EDT should condition on actual execution or on whatever proposition reliably predicts outcomes. This operational clarification is my own; the source does not develop policy evaluation.

A practical procedure is:

1. Specify candidate acts or policies.
2. Specify outcomes and utilities.
3. Model states, predictors, other agents, and observations probabilistically.
4. For each candidate, compute \(P(\text{outcome}\mid \text{candidate is performed})\).
5. Choose the candidate with highest conditional expected utility.

The hard step is modeling the evidential dependencies. EDT does not by itself tell you which correlations are real or relevant; it tells you how to use your probability model once formed.

## 5. Open questions and an operational interpretation

The source leaves several questions open.

First, how should \(P(O_j\mid A)\) be defined when acts have zero or near-zero prior probability? If the ratio definition fails, EDT needs conditional credences under supposition. A reasonable operational interpretation is to use a “deliberative” probability model that assigns positive probability to each available act, or to treat the conditional probabilities as primitive judgments. In well-specified problems—predictors, twins, repeated statistical data—these conditionals can often be estimated or justified directly.

Second, how should EDT handle cases where conditioning on an act produces “good news” by indicating a desirable state that the act does not bring about? The source quotes Lewis and Joyce criticizing EDT for this. My view is that EDT is coherent if the decision problem is framed as choosing the proposition about oneself that one wants to be true. But if the aim is interventionist control, CDT may be more appropriate. In unfamiliar cases, ask: is the act valuable because it causes good outcomes, or merely because it indicates them? EDT counts both; many philosophers think it should count only the first.

Third, the Sleeping Beauty discussion in the source remains unresolved. EDT has been used to avoid Dutch books, but Conitzer argues that halfers using EDT may still be vulnerable. This suggests that EDT’s interaction with indexical probability is not settled by the basic formula alone.

Finally, the source mentions the “evidentialist’s wager”: even if one gives EDT modest credence, acting as if EDT were true may be advantageous when many correlated decision-makers are involved (MacAskill et al. 2021). This is a strategic argument, not a proof of EDT, but it gives EDT practical importance in large-scale correlated choices.

## Conclusion

EDT offers a simple, precise rule: choose the act or policy with the highest expected desirability conditional on its performance. Its power is that it takes seriously all evidential connections—prediction, correlation, duplication, and logical dependence. Its controversy is that it does not distinguish auspicious evidence from causal efficacy. To apply EDT, model the relevant dependencies, compute conditional probabilities, and maximize conditional expected utility. Whether that is the whole of rational choice is the enduring debate between EDT and CDT.

## References

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge University Press.

Conitzer, Vincent. 2015. “A Dutch book against sleeping beauties who are evidential decision theorists.” *Synthese* 192 (9): 2887–2899.

Gibbard, Allan, and William L. Harper. 1976. *Counterfactuals and Two Kinds of Expected Utility*.

Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. 2021. “The Evidentialist’s Wager.”

Wikipedia contributors. 2026. “Evidential decision theory.” Revision 1373679688. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post about EDT, 2400-3000 words including references, based on supplied source, distinguish source claims vs own assumptions, explain how theory evaluates actions/policies, dependencies/counterfactuals, uncertainty where source leaves open, operational interpretation if available. Need likely produce final essay only. Need think in same language as user's request? User's request English. Need maybe word count ~2400-3000. Need include references brief. Need avoid appendices. Need likely no explicit planning in final. Let's design essay.

Need target around 2400-3000 words. Need include mathematical definitions. Source: Wikipedia EDT. Need write coherent account. Need maybe mention conditional expected utility V(A)=sum P(O_j|A)D(O_j). Compare CDT U(A)=sum P(A box-> O_j)D(O_j). Discuss probability model: acts, states, outcomes; Jeffrey's decision theory? News value. Conditional probabilities as evidential relations, not causal. Need explain application to decisions: construct set of actions, partition outcomes/states, assign prior credences P over act/state/outcome? Important nuance: If acts have zero probability? Need conditional probability given action; may need regular conditional probabilities, conditional on actions chosen? In decision theory acts are under agent control; conditioning on acts can be tricky (Levi, Joyce). Need operational interpretation: use subjective conditional probabilities P(O|A) as conditional credence upon supposing A, using Ramsey test or imaging? EDT uses conditional probability rather than intervention. Could define P(O|A)=P(O∧A)/P(A) when P(A)>0, but if actions assigned zero probability, need conditional probabilities primitive or via conditional models. Source doesn't resolve; propose operational: build probabilistic model with variables A, S, O; assign joint distribution over background variables including predictors/copies; compute P(O|do? no, condition on A). But for policy selection maybe compare V(A).

Need explain dependencies and counterfactuals: EDT treats any probabilistic dependence between act and outcome as relevant, whether causal, common cause, prediction, logical correlation, twin. It doesn't require act causes outcome; only evidence. Counterfactuals: source says CDT uses counterfactual probabilities P(A □→ O_j). EDT uses ordinary conditional probabilities. We need discuss how EDT handles counterfactuals: if considering "what if I did A?" it treats as learning that A will occur, not intervening. It may not use causal interventions. Need discuss cases: Newcomb, twin prisoner's dilemma. Maybe include Smoking Lesion? Not in source but common. Could mention as extension maybe distinguish source. But source doesn't mention; can include own example? User says use examples whenever help. Need maybe include a medical screening example to show dependence without causation: a test result correlates with disease, taking action? Need be careful. Could discuss smoking lesion as classic objection: EDT recommends not smoking if smoking is evidence of lesion? Actually smoking lesion: Smoking causes pleasure? lesion causes cancer and smoking? EDT may avoid smoking because evidence of cancer? CDT smoke. Could be useful for criticism. But source only has Lewis/Joyce criticisms. Could mention as own addition. Need distinguish source claims vs additional assumptions. We can label: Source claims: EDT maximizes conditional expected utility/news value; examples Newcomb, twin; criticisms; Sleeping Beauty; evidentialist's wager. My additions: formal model with variables, policy evaluation, conditional supposition, zero-prob acts, ratification, dynamics? Need maybe mention policies: EDT can evaluate policies as actions or as dispositions? The source focuses actions. User asks how evaluates alternative actions or policies. Need discuss policies: treat policy π as an object of news: value V(π)=E[D(O)|π adopted/implemented?]. For an agent choosing a policy, conditioning on "I adopt π" may correlate with type, environment. If policy maps observations to actions, need value of policy: sum over histories/outcomes conditional on adopting policy. But EDT may prefer choosing a policy if choosing it is good news, not necessarily implementing it? There is issue: choosing vs performing. Need propose operational: for policies, evaluate conditional expected utility of the policy being executed, or news that one is the kind of agent who follows that policy. If policy choice is public/observable, conditioning on adoption may carry evidence about future behavior and states. Need distinguish act EDT vs policy EDT. Could define policy π as a decision rule; V(π)=∑ P(O | π is adopted and followed) D(O) or P(O | the agent implements π). But if adoption doesn't guarantee execution, need condition on execution. Source doesn't clarify; propose using "the action/policy actually taken" as event. For precommitments, evaluate commitment as an action whose evidence changes predictions.

Need perhaps discuss Jeffrey's desiderability and probabilities of propositions. Need define outcomes partition, desirability D. Expected utility: V(A)=Σ_j P(O_j|A) D(O_j). If outcomes are monetary, D=utility. Need maybe include continuous version: V(A)=∫ D(o) dP(o|A). Also include states: if outcomes depend on states S_k and action A produces outcome O(A,S), then V(A)=Σ_k P(S_k|A) D(O(A,S_k)). This shows EDT conditions states on act; in standard causal decision theory states are probabilistically independent of acts (or use causal probabilities). In Newcomb, state = predictor's prediction/box contents, P(state|A) depends on A due to predictor. Need compute examples exactly maybe with 99%. Also twin with perfect correlation.

Need discuss "news value": imagine receiving a message that you will take A. Value of news: expected desirability of outcomes conditional on message. Do action with best news. Quote "do what you most want to learn that you will do" from source. Need mention this is not managing news per se but acting on evidential bearing.

Need discuss relation to Bayesian conditionalization and Dutch books: source mentions Sleeping Beauty and Dutch book; can explain briefly: EDT can align beliefs and choices under centered/indexical uncertainty? Need not deep. Could mention source says halfers still Dutch booked by Conitzer; uncertainty remains. Need explain source leaves open: how assign conditional probabilities when acts are impossible? How distinguish spurious correlations? How to handle policies and interventions? Need propose operational: use explicit causal/evidential graph but condition on act variable, not do-operator; ensure probabilities represent agent's epistemic state before choice, include all relevant dependencies. If the agent can manipulate evidence? Example: if action A is correlated with bad state due to common cause but doesn't cause it, EDT still may avoid A; some see as flaw. Operational interpretation: if agent's goal is to maximize expected value of the world conditional on the proposition that they take A, EDT is consistent. But if goal is to bring about good outcomes, CDT may be better.

Need include formal definitions: Decision problem tuple (A, Ω, O, P, D). A finite set of acts. Ω states. Outcome function f: A×Ω→O. Probability measure P on (A×Ω?) Actually including act variable. But acts not events? In EDT, acts are propositions/events. Let (A,S) random variables with joint P; but if agent chooses act, prior P(A) may reflect predictions of behavior, not choice probabilities. V(a)=Σ_ω P(S=ω | A=a) D(f(a,ω)). This requires P(A=a)>0. If zero, conditional primitive. Alternative: possible worlds W, desirability D(w), act proposition A subset W. V(A)=Σ_{w∈A} P(w|A) D(w) or expected desirability conditional on A. More Jeffrey style: V(A)=Σ_w P(w|A)D(w). But outcomes partition; okay.

Need discuss conditional probabilities as supposition: P(O|A) = credence in O under supposition A, not necessarily ratio definition. Use ratio when possible. Mention problem of act probabilities: if agent is certain she will choose a particular act, conditioning on alternative may be undefined; one can assign small positive probabilities to all acts for deliberation, take limit, or take conditional credences primitive. Source leaves open. Reasonable operational: use a deliberative prior that gives positive probability to each available act; after evaluating, choose max. This may be arbitrary but often stable if predictions reliable.

Need explain dependencies and counterfactuals more deeply: In EDT, relevant dependencies are encoded by conditional probabilities. If P(O|A)≠P(O), act A is evidentially relevant. Dependencies can arise from:
1 causal influence A→O
2 common cause C→A and C→O (e.g., predictor, lesion)
3 logical/algorithmic correlation (twin, copies)
4 selection/indexical effects (Sleeping Beauty maybe)
EDT treats them all similarly if they affect P(O|A).

Counterfactuals: CDT uses P(A □→ O) interpreted as probability that outcome O would occur if A were performed, holding fixed relevant causal history or intervening. EDT uses P(O|A): probability of O given news A. In cases where act is causally efficacious and no confounding, they coincide. In Newcomb, differ because predictor creates correlation between act and prior state. Need maybe formalize with DAG:
Predictor's prediction P (maybe variable T) causes box content B and is correlated with player's action A due to accurate prediction. There is arrow from latent disposition/algorithm to both A and T? EDT conditions on A and updates T; CDT intervenes on A, leaving T fixed.

Need maybe compute Newcomb with predictor accuracy p=0.99. Need be careful about prior probability of one-boxing? The formula in source assumes P(1M|one-box)=0.99 and P(1M|two-box)=0.01. This follows if predictor accuracy symmetric and prior predictions match? In reality conditional probabilities depend on prior probability of one-boxing and predictor accuracy via Bayes. But source simplifies. Could mention source's example assumes conditional probabilities equal predictor accuracy, which is natural if predictor errors are symmetric and the predictor's prediction is perfectly calibrated to the agent's choice probabilities? Let's check: Suppose predictor predicts one-box with probability q? Accuracy p = P(predict one|one)=P(predict two|two)=0.99. Then P(1M|one)=P(predict one|one)=0.99 (given predictor makes prediction before, box content determined by prediction). That doesn't depend on prior q if conditioning on actual one-box and symmetric accuracy. Yes P(predict one|one)=0.99 by definition if accuracy conditional on choice. Similarly P(predict one|two)=0.01 if false positive rate 0.01. So okay.

Need also mention utility of both boxes if B has 1M: 1,001,000; if empty: 1,000. Values computed. Need include equations.

Twin prisoner's dilemma: if exact psychological twin, P(twin cooperates|Aomame cooperates)=1, etc. If not perfect but high correlation, V(C)=p*5+(1-p)*0? Need maybe generalize. Let's compute: if correlation r? Suppose P(twin C|self C)=q, P(twin C|self D)=r. EDT cooperate if 5q + 0(1-q) > 10r + 1(1-r)=1+9r. For perfect q=1,r=0. Could mention this is my generalization. In ordinary PD with no correlation q=r=defection rate? Then defect if T>P? Need maybe not necessary. But helpful.

Need discuss policy evaluation in game theory: EDT may recommend cooperation in twin PD due to correlation. In ordinary one-shot PD with independent opponents, EDT maybe defect if no correlation. But if opponent uses same reasoning, evidential dependence. Need distinguish from causal influence: your action doesn't cause twin's action (separate rooms), but evidential.

Need discuss Evidentialist's Wager: source says even with low credence in EDT, act as if EDT because correlated decision-makers stakes higher. Need maybe explain: If many agents face similar choices and are correlated, EDT's expected value across correlated instances can dominate. But need not deep. Could include as implication.

Need discuss criticisms: Lewis "irrational policy of managing the news", Joyce causal efficacy vs auspiciousness. Need discuss smoking lesion as example: Suppose a lesion causes both smoking and cancer; smoking itself is harmless/pleasant. EDT: P(cancer|smoke) high, so V(smoke) low; CDT: smoking doesn't cause cancer, so smoke. This illustrates why critics think EDT confuses evidence and causation. Source didn't include smoking lesion; mark as my addition. Also Newcomb: EDT one-box, CDT two-box; source includes. Need mention that EDT advocates see Newcomb as reason for EDT: if predictor rewards evidence of one-boxing, one-boxing gets good news.

Need discuss ratification and dynamic consistency: EDT may choose action that, once taken as news, changes beliefs. Does it need to be stable after choice? For decision, compare prior conditional V. If agent knows she will choose A, P(O|A) maybe different. There can be instability: if she decides to A, then A is no longer news? But not required by source. Could mention as open issue. Need perhaps propose: use pre-deliberation probabilities; after choice, update but don't re-evaluate? Or require ratifiable choice: choose A only if after supposing A, still prefer A among available? This may be too advanced but useful. User wants uncertainty where source leaves important question open, operational interpretation. Could mention zero-prob acts and policy evaluation as open.

Need word count ~2500. Let's outline essay:

Title: Evidential Decision Theory: Choosing the Best News

1. Introduction (~250 words): EDT definition, news value, contrast CDT, aim.
2. Formal framework (~600 words): decision problem, outcomes, desirability, conditional probabilities, V(A), continuous, states, acts as propositions, conditional supposition, comparison to CDT formula. Discuss when coincide.
3. Dependencies and counterfactuals (~450 words): What counts as dependence? common cause, prediction, logical correlation. Counterfactual vs conditional. DAG/intervention explanation. Source claims vs my operational model.
4. Examples (~700 words): Newcomb compute; twin PD compute; maybe smoking lesion/medical test as caution; maybe policy example.
5. Policies and unfamiliar cases (~450 words): evaluate policies as propositions, zero-prob act issue, operational recipe: list acts/policies, model variables, assign P(O|A) via evidence, compute V, choose max; when uncertain use sensitivity. Precommitment, correlated agents.
6. Open questions/uncertainties (~250 words): conditional probabilities for acts, Sleeping Beauty/Dutch books, managing news vs causing, policy vs act. Source claims; my proposal: use positive deliberative prior/primitive conditionals, ratification if needed.
7. Conclusion (~100 words).
References (~150 words) include source and maybe Ahmed, Gibbard Harper, Lewis, Joyce, MacAskill, Conitzer. Need no lengthy bibliography. Could include in-text references.

Need ensure 2400-3000 words. Need maybe final around 2700. Let's estimate word counts. Need be careful not too long. We can produce detailed essay ~2600 words. Need include equations in LaTeX. Need mention source: Wikipedia revision. Need distinguish claims: "The source reports...", "I add...". Need not use bullet too much? It's essay, can use sections. Need maybe include formulas. Need final conclusion brief.

Let's draft with detailed math. Need ensure no hidden instructions. Final only essay. Let's write in first person? Researcher. Use "I" maybe okay. Need target words. Let's draft mentally.

Title.

Intro:
"Evidential decision theory (EDT) is ... source's slogan: do what you most want to learn that you will do." Mention Ahmed. "It asks not 'what will this action bring about?' but 'what would the world likely be like if the news said I did this?'"

Formal:
Let A set of actions; O outcomes. For each act a, define value V(a)=∑_j P(O_j | A=a) D(O_j). D desirability. If outcomes continuous integral. Equivalent to conditional expected utility. If acts are propositions in possible worlds, V(a)=∑_{w∈a}P(w|a)D(w) maybe. But more common partition outcomes. If outcomes determined by states S, V(a)=∑_s P(S=s|A=a)D(O(a,s)). Emphasize P is agent's credence at choice time, before action. The condition is evidential. Ratio if P(A)>0; otherwise conditional credence. Source gives formula from Gibbard/Harper.

CDT formula: U(A)=∑ P(A □→ O_j)D(O_j). Need explain box arrow. If P(A□→O)=P(O|A) for all acts/outcomes, theories agree. They differ when act is evidence for outcome without causing it.

Dependencies and counterfactuals:
EDT relevant dependencies: any statistical/logical dependence captured in P(O|A). Source's examples: predictor, twin. My addition: common cause, logical correlation. EDT doesn't ask whether A changes probability of O by intervention; asks whether learning A changes expectation. Counterfactual: EDT's "if I were to do A" is supposition, not intervention. CDT uses intervention do(A). Use DAG: A→O vs C→A,O. In C, EDT sees correlation, CDT not. Mention source says conditional and counterfactual probabilities not always equal.

Examples:
Newcomb: describe, compute exactly. Need maybe use p=0.99. Formulas as source. EDT one-box. Explain dependency: one-box is evidence predictor filled box. CDT two-box because box already fixed. Source claims.

Twin: compute. Perfect twin. Could generalize: let q=P(twin C|self C), r=P(twin C|self D). V(C)=5q, V(D)=10r+1(1-r)=1+9r. Cooperate if 5q > 1+9r. Perfect q=1,r=0. Source. If imperfect correlation, EDT may still cooperate if high enough. My addition.

Maybe medical/smoking lesion: Suppose lesion L causes cancer C and desire to smoke S; smoking gives pleasure +1, cancer -100. If P(L|smoke)=0.9, P(L|not)=0.1, EDT value smoke lower, even if smoking doesn't cause cancer. CDT smoke. This shows criticism. Need mark as my illustrative addition not source. Could be concise.

Policies:
Source mostly actions. To apply to policies, treat policy π as event "agent adopts/executes π". Value V(π)=∑_h,o P(H=h,O=o | π) D(o) maybe. If policy maps info to actions, condition on proposition that policy is in force. Need caution: adopting vs executing. If adopting policy is evidence about type or future actions, EDT counts that. Example precommit to one-box? If predictor sees commitment, one-box policy may be high value. For algorithms, evaluate policy by conditioning on its implementation, not by causal effects of individual branches. Operational recipe: (1) specify actions/policies; (2) specify outcome variables and utility; (3) assign joint/evidential probabilities over act, states, outcomes; (4) compute conditional expectations; (5) choose max. For policies with observations, if the policy's choice depends on observation, you might condition on the policy proposition and marginalize over observations: V(π)=Σ_x P(X=x | π) Σ_a π(a|x) P(O | A=a, X=x, π) D(O). But if policy fully determines action given X, then P(A=a|X=x,π)=π. However, EDT may have issues with conditioning on policy if policy adoption is certain? Need propose. Need maybe not too formal but enough.

Open questions:
Source leaves: how to set P(O|A) when actions are not ordinary events? In Bayesian probability, acts under deliberation may have probabilities. Need propose: assign positive "deliberative" probabilities or primitive conditional credences. Use ratio when possible; limit as P(A)→0; or model predictors/copy correlations. Another open: Sleeping Beauty. Source says EDT applied to avoid Dutch books, Conitzer disputes. We can say uncertain; EDT's answer depends on credence assignment (halfer/thirder). Another: is EDT rational if it chooses auspicious acts that don't cause good outcomes? Source includes criticisms. My proposal: if decision problem genuinely includes predictive or logical correlations, EDT is a coherent way to value evidence; if one wants interventionist control, use CDT. In unfamiliar cases, ask whether the proposition "I do A" is reliable evidence of variables that determine utility. If yes, EDT counts it.

Need maybe mention "news value" can be seen as value of a message: Suppose a trusted source will tell you tomorrow which act you performed. The expected utility of each message is V(A). EDT chooses act whose message has highest expected value. This operational interpretation helps. But potential objection: you can't choose news, only act. EDT says act as if choosing news.

Need maybe mention "Evidentialist's wager" from source: if EDT involves actions of many correlated decision-makers, stakes higher; even low credence EDT may dominate. Could include in implications. Need keep concise.

Need references at end: Wikipedia source, Gibbard & Harper, Ahmed, Lewis, Joyce, MacAskill et al., Conitzer maybe. Since target includes references and any material in word count. Need not lengthy. Maybe references list with 6 items. Need ensure word count with references ~2600. Let's draft actual text and count roughly.

Need maybe include equations in display. Could use Markdown/LaTeX.

Let's write final in a polished essay. Need maybe around 2700. Let's compose carefully.

Potential word count: Title + sections. We can use headings. Need maybe 2400-3000. Let's draft ~2600.

Detailed draft:

# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) ... [~200]

## 1. The basic rule

Let ... [~550]

Equation. Source: Gibbard/Harper. CDT formula. Explanation.

## 2. What dependencies count?

[~450]

## 3. Canonical examples

Newcomb [~400], twin [~250], lesion [~150] total 800.

## 4. Policies and practical recipe

[~500]

## 5. Open questions and operational proposals

[~400]

## Conclusion

[~100]

References [~150]

Total ~3150? Need tighten. Let's target 2700.

Let's draft now with approximate counts.

Start:

"Evidential decision theory (EDT) is a school of decision theory that evaluates acts by their news value: the expected desirability of the world conditional on learning that the act was performed. The Wikipedia article summarizes the slogan as 'do what you most want to learn that you will do' (Ahmed 2021)." Good.

Formal:
"Suppose an agent faces finite set \mathcal A. Let \mathcal O = {O_j}. D(O_j) ..." Use D maybe utility.

Need mention if outcomes not exhaustive? Need partition. "The probabilities are those of the agent at the moment of choice."

CDT:
"U(A)=..." with square arrow. Need ensure LaTeX correct: P(A \mathrel{\Box\rightarrow} O_j). Use source.

"Since conditional and counterfactual probabilities can differ, EDT and CDT can differ." Source.

Dependencies:
"EDT's relevant relation is probabilistic dependence: P(O_j|A) ≠ P(O_j)." But if act not random? Eh.

Could include "A common-cause variable C may make P(O|A) high although A does not cause O." Good.

Examples:
Newcomb equations. Need ensure numbers: V(only B)=0.99*1M + 0.01*0 = 990,000. V(both)=0.01*1,001,000 +0.99*1000 = 10,010+990 = 11,000. Good.

Twin equations. Perfect: V(C)=1*5+0*0=5; V(D)=0*10+1*1=1. Good. Generalization: q,r formula. Need maybe say "This generalization is mine".

Lesion: "To see the criticism, consider a smoking lesion not in source..." Need brief.

Policies:
Need define policy π. "A policy is a proposition describing the agent's decision rule or plan. EDT evaluates V(π)=Σ_o P(o | π)D(o), where π means the policy is adopted and executed." If policy maps observations to actions, "condition on the entire proposition that the agent follows π; then marginalize over observations". Provide formula:
V(π)=∑_x P(X=x|π) ∑_o P(o | X=x, π) D(o). Since π determines A=π(X), can write P(o|X=x,A=π(x),π). Need maybe too complex. Also mention precommitment: evaluate commitment as act.

Operational recipe: list; model; assign conditional probabilities; compute; choose. Need mention "do not use do-operator".

Open questions:
"1. Conditioning on acts." Acts may have zero probability. Source doesn't resolve. Propose "deliberative prior with positive probability for all available acts or primitive conditional credences." Need explain. "2. Sleeping Beauty." Source says EDT applied to avoid Dutch books, Conitzer argues halfers still affected; uncertain. "3. Managing news vs causation." Source criticisms. My view.

References: need include source. Maybe:
- Wikipedia contributors, "Evidential decision theory," revision 1373679688, 2026.
- Gibbard and Harper 1976.
- Ahmed 2021.
- Lewis 1981.
- Joyce 1999.
- MacAskill et al. 2021.
- Conitzer 2015.
Need maybe too many but okay. Need not lengthy.

Need word count. Let's actually draft in final and maybe approximate. But before final, think if any other requirements: "Researcher — mathematical essay / blog post" "Target approximately 2,400–3,000 words, including references and any other material." Need maybe no answer to assigned case. Use examples. Finish with brief conclusion. Distinguish claims source vs own. Good.

Need ensure no hallucinated too much? Source has 2026 revision. We can reference. Need maybe mention "The source text supplied" not necessary. Need maybe avoid overclaim: "EDT recommends". Good.

Potential issue: If we include Smoking Lesion not source, need clearly mark as additional. Good.

Potential issue: The source's formula uses D(O_j) desirability, not utility. We can use utility as desirability. Good.

Potential issue: Need maybe explain conditional probability with actions: P(O_j|A) can be thought as P(O_j ∧ A)/P(A). But if P(A)=0, undefined. Need propose. Good.

Potential issue: "how it treats relevant dependencies and counterfactuals." Need explicit section. Good.

Potential issue: "Where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop and justify it." Need include open questions and operational. Good.

Let's maybe write around 2600 words. Need count. Let's draft with approximate counts by paragraphs.

Title + intro 180.

Section 1: maybe 650.

Section 2: 400.

Section 3: 650.

Section 4: 450.

Section 5: 400.

Conclusion 80.

References 150. Total 2960? Need okay. Maybe trim.

Let's write and count roughly:

Title 7.

Intro paragraph: "Evidential decision theory (EDT) is a school..." maybe 115.

Let's draft fully:

# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a school of decision theory that evaluates acts by their *news value*: the expected desirability of the world conditional on learning that the act was performed. The supplied Wikipedia article summarizes the view with the slogan “do what you most want to learn that you will do” (Ahmed 2021). EDT therefore asks a peculiar but precise question. It does not first ask, “What will this action causally bring about?” It asks, “If I received a message telling me that I had performed this action, how good would the world likely be?” The action with the highest expected good news is the rational choice.

This essay develops EDT’s central formula, explains how it treats dependencies and counterfactuals, and shows how to apply it to familiar examples and to policies. I follow the source in presenting EDT through conditional expected utility and in contrasting it with causal decision theory (CDT). Where the source is silent—especially about how to assign probabilities to actions and how to evaluate policies—I add operational assumptions and label them as such.

Count intro ~205.

Section 1 heading and content:

## 1. The core rule: maximize conditional expected utility

Suppose an agent can choose among a finite set of acts \(\mathcal A\). Let \(O_1,O_2,\ldots\) be a partition of possible outcomes, and let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). EDT assigns to each act \(A\) the value
\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]
This formula appears in Gibbard and Harper (1976), as cited in the source. The probability \(P(O_j\mid A)\) is the agent’s conditional credence that outcome \(O_j\) will occur given that act \(A\) is performed. EDT recommends choosing an act maximizing \(V(A)\).

The formula is a conditional expectation. If outcomes are continuous, replace the sum by an integral:
\[
V(A)=\int D(o)\,dP(o\mid A).
\]
If outcomes are determined by an act and a state, with states \(S_k\) and outcome function \(O(A,S_k)\), then
\[
V(A)=\sum_k P(S_k\mid A)D(O(A,S_k)).
\]
This state-based version is often the most practical. It says: for each possible state of the world, ask how likely that state is under the supposition that you do \(A\), determine the outcome that would then result, and average the desirabilities.

The important point is that the probabilities are *conditional on the act*. In ordinary Bayesian terms, if \(P(A)>0\), one may write
\[
P(O_j\mid A)=\frac{P(O_j\wedge A)}{P(A)}.
\]
But EDT should not be understood as requiring that the agent assign ordinary prior probabilities to her future actions in the same way she assigns probabilities to weather events. The conditional probability is better interpreted as the agent’s credence in \(O_j\) under the supposition “I do \(A\).” I return to this interpretive issue below, because the source does not fully settle it.

CDT uses a different expected utility:
\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]
where \(A \mathrel{\Box\rightarrow} O_j\) is read “if \(A\) were performed, \(O_j\) would occur,” or more cautiously, “\(O_j\) occurs in the counterfactual situation in which \(A\) is performed.” The source emphasizes that \(P(A \mathrel{\Box\rightarrow} O_j)\) and \(P(O_j\mid A)\) are not always equal. When they are equal, EDT and CDT agree. When they differ, EDT follows the conditional probability, while CDT follows the counterfactual or interventionist probability.

A useful intuitive model is the “news” model. Imagine that after acting, a reliable newspaper will report which act you performed. Before choosing, you can evaluate each possible headline: “Agent performed \(A\).” The value of that headline is the expected utility of the outcomes conditional on it. EDT says to make the headline you most want to read true. This is not because the headline causally changes the world; it is because the headline carries evidence about what the world is like.

Count section 1 maybe ~620. Good.

Section 2:

## 2. Dependencies, evidence, and counterfactuals

EDT treats any probabilistic dependence between act and outcome as decision-relevant, provided that dependence is captured by the agent’s conditional probabilities. If learning that \(A\) was performed would raise the probability of a good outcome, then \(A\) has high news value. The dependence may have several sources.

First, the act may genuinely cause the outcome. If taking medicine improves health, then \(P(\text{health}\mid \text{medicine})\) may be high because medicine causes health. In such cases EDT and CDT typically agree.

Second, the act may be correlated with an outcome through a common cause. A predictor may have predicted your action before the outcome was fixed. Your present action does not cause the predictor’s past prediction, but it is evidence about it. Newcomb’s problem is of this kind.

Third, the act may be correlated with another agent’s action through similarity, shared algorithm, or logical dependence. In the twin prisoner’s dilemma, the source describes Aomame and her psychological twin as reasoning in exactly analogous ways. Aomame’s choice does not causally affect her twin, who is in another room, but it is strong evidence for what her twin will do.

Fourth, dependencies may arise from indexical or selection effects. The source mentions the Sleeping Beauty problem, where EDT has been used to manage credences under self-locating uncertainty. I do not resolve that problem here; the source itself notes disagreement about whether EDT fully avoids Dutch-book objections.

The contrast with CDT is best understood through counterfactuals. EDT’s question is: “What should I expect, conditional on the proposition that I do \(A\)?” CDT’s question is: “What would happen if I intervened to bring about \(A\)?” In modern causal notation, one might contrast \(P(O\mid A)\) with \(P(O\mid do(A))\). The source uses a counterfactual arrow rather than the \(do\)-operator, but the conceptual difference is similar. An intervention breaks some of the ordinary evidential connections between \(A\) and its causes. EDT does not break them.

Thus, in a causal diagram where a common cause \(C\) influences both \(A\) and \(O\), EDT may find \(A\) valuable because \(A\) indicates \(C\), while CDT may deny that \(A\) is valuable if intervening on \(A\) does not change \(C\) or \(O\). This is the formal heart of the disagreement. The source’s claim is simply that conditional and counterfactual expected utilities can differ; my formulation in terms of causal diagrams is an explanatory addition.

Count ~470.

Section 3:

## 3. Examples

### Newcomb’s problem

The source presents Newcomb’s problem as follows. A predictor predicts the player’s choice with high reliability, say 99%. Box A is transparent and contains $1,000. Box B is opaque. If the predictor predicted that the player will take both boxes, B contains nothing. If the predictor predicted that the player will take only B, B contains $1,000,000. The player can take both boxes or only B.

EDT evaluates the two acts by conditioning on them. Let “one-box” mean taking only B and “two-box” mean taking both. With predictor accuracy 0.99, the source uses
\[
P(\text{1M in B}\mid \text{one-box})=0.99,
\]
and
\[
P(\text{1M in B}\mid \text{two-box})=0.01.
\]
Then
\[
\begin{aligned}
V(\text{one-box})
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0\\
&=\$990{,}000,
\end{aligned}
\]
while
\[
\begin{aligned}
V(\text{two-box})
&=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000\\
&=\$11{,}000.
\end{aligned}
\]
EDT therefore recommends one-boxing. The reason is evidential: taking only B is strong evidence that the predictor filled B. Taking both is strong evidence that the predictor left B empty.

CDT, as the source notes, recommends two-boxing because the predictor has already acted and the current choice does not causally change the contents of the boxes. The example shows EDT’s central feature: it rewards being the kind of agent whose choice is good evidence of a good state.

### Twin prisoner’s dilemma

The source’s second example is a twin version of the prisoner’s dilemma. Aomame and her psychological twin choose separately whether to cooperate. Payoffs to each are: both cooperate gives $5 each; both defect gives $1 each; if one cooperates and the other defects, the defector gets $10 and the cooperator gets $0. Assuming Aomame cares only about her own payoff, EDT evaluates her acts by conditioning on them.

If the twins are exact psychological duplicates, the source assumes
\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]
and
\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]
Then
\[
V(\text{cooperate})=1\cdot \$5+0\cdot \$0=\$5,
\]
whereas
\[
V(\text{defect})=0\cdot \$10+1\cdot \$1=\$1.
\]
EDT recommends cooperating.

A small generalization, not required by the source, helps show how to use EDT in less idealized cases. Let
\[
q=P(\text{twin cooperates}\mid \text{Aomame cooperates})
\]
and
\[
r=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]
Then
\[
V(C)=5q,
\]
and
\[
V(D)=10r+1(1-r)=1+9r.
\]
Cooperation is recommended when \(5q>1+9r\). Perfect correlation makes this true. Weak correlation may not. This formula illustrates how EDT handles degrees of evidential dependence.

### A cautionary example: smoking and lesions

The source does not discuss the well-known “smoking lesion” problem, but it clarifies EDT’s controversial side. Suppose smoking does not cause cancer; instead, a lesion causes both cancer and a desire to smoke. Smoking is mildly pleasant. Since smoking is evidence of the lesion, and the lesion is evidence of cancer, EDT may assign smoking low news value. CDT would say that smoking does not cause cancer, so smoking is permissible or even recommended if it gives pleasure. This example motivates the criticisms quoted in the source: Lewis calls EDT “an irrational policy of managing the news,” and Joyce says rational agents choose on the basis of causal efficacy, not auspiciousness. The example is my addition, but it follows directly from EDT’s conditional-probability rule.

Count section 3 ~850? Maybe too long. Total so far 205+620+470+850=2145. Add policy/open/conclusion/refs ~900 -> 3045. Need trim maybe okay target 3000. Could reduce policy. But let's continue.

Section 4:

## 4. Evaluating policies

The source mainly discusses individual acts, but decision problems often ask us to choose policies: rules, algorithms, or dispositions. EDT can handle policies by treating a policy as the proposition that is evaluated. Let \(\pi\) be a policy. Its EDT value is
\[
V(\pi)=\sum_o P(o\mid \pi)D(o),
\]
where \(\pi\) should be understood as “the agent adopts and follows \(\pi\),” not merely “the agent says she adopts \(\pi\).” If a policy maps observations \(X\) to acts \(A\), then one can write, as an operational proposal,
\[
V(\pi)=\sum_x P(X=x\mid \pi)
        \sum_o P(o\mid X=x, A=\pi(x))D(o).
\]
This is not a new axiom; it is an application of the conditional-utility rule to a richer act-description.

The policy formulation matters because EDT may assign value to choosing a policy for evidential reasons. Suppose a predictor can see whether an agent has adopted a one-boxing policy. Then the proposition “this agent follows a one-boxing policy” may be excellent evidence that the predictor filled the box. EDT can evaluate the policy directly. Similarly, in multi-agent settings, adopting a cooperative policy may be evidence that similar agents adopt cooperative policies.

One subtle point is the difference between evaluating a policy and evaluating the news that one chose a policy. If choosing \(\pi\) is itself an action, EDT evaluates the act of choosing by conditioning on it. But if the choice is not binding, the news that one chose \(\pi\) may be weaker evidence that one will follow \(\pi\). A careful EDT model should therefore condition on the event that is genuinely informative about outcomes. Usually that event is the policy’s actual execution, not a merely verbal announcement. This operational distinction is my proposal; the source does not address policy evaluation in detail.

A practical recipe follows.

1. Specify the available acts or policies.
2. Specify the outcomes and their desirabilities.
3. Build a probabilistic model of the relevant states, predictors, other agents, and observations.
4. For each candidate act or policy, compute the conditional distribution over outcomes given that act or policy is performed.
5. Choose the act or policy with the largest conditional expected desirability.

This recipe is simple in principle but can be difficult in practice, because step 3 requires judgment about which evidential dependencies are real.

Count ~480. Total 2625. Open/conclusion/refs ~700 -> 3325. Need reduce. Hmm maybe target 3000 max. Need trim some sections or final word count maybe okay? Need approximate. Let's more accurately count? The above counts rough; could be >3000. Need reduce. Could remove lesion example? But useful. Could shorten policy recipe. Maybe final around 3100. Need 2400-3000. Need be safe. Let's trim by making sections concise. Could merge open questions into policy? Let's aim 2700-2900.

Let's count actual words maybe from drafted sections. Intro: 215. Section 1: maybe 540? Let's count more accurately by chunk? Hard. But likely total >3000. Need reduce. We can make final more concise.

Maybe omit continuous integral and state formula? But need math. Keep but concise. Could shorten policy formula. Could omit lesion? But criticism needs example; can mention in one sentence. Could reduce open questions. Let's plan final with tighter language.

Alternative final length: 2500. Need perhaps less detail. But user wants substantive. We can include key things.

Let's redesign final to ~2600:

- Intro 150
- Formal 500
- Dependencies 350
- Examples 650 (Newcomb 300, twin 200, lesion 150)
- Policies 350
- Open questions 350
- Conclusion 70
- References 150
Total 2570. Good.

Need write final accordingly. Let's draft final now in concise version, ensuring all needed.

Need include references word count. Let's write final polished.

Detailed final:

# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) evaluates acts by their *news value*: the expected desirability of outcomes conditional on learning that the act was performed. The supplied article summarizes EDT with the slogan “do what you most want to learn that you will do” (Ahmed 2021). Instead of first asking, “What will this action causally bring about?” EDT asks, “If I received news that I had performed this action, how good would the world likely be?” The rational act is the one whose news is best in expectation.

This essay gives EDT’s central mathematical rule, explains how it treats dependencies and counterfactuals, and applies it to examples and policies. I follow the source in presenting EDT through conditional expected utility and contrasting it with causal decision theory (CDT). Where the source is silent—especially about probability assignments for actions and policy evaluation—I add operational assumptions and identify them.

## 1. The core rule

Let \(\mathcal A\) be a finite set of possible acts. Let \(O_1,O_2,\ldots\) be a partition of possible outcomes, and let \(D(O_j)\) be the desirability or utility of outcome \(O_j\). EDT assigns to act \(A\) the value

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This is the formula given by Gibbard and Harper (1976) in the source. The probability \(P(O_j\mid A)\) is the agent’s conditional credence that \(O_j\) will occur given that \(A\) is performed. EDT recommends choosing an act maximizing \(V(A)\).

If outcomes are continuous, replace the sum by an integral:

\[
V(A)=\int D(o)\,dP(o\mid A).
\]

Often outcomes are determined by acts and states. If \(S_k\) are possible states and \(O(A,S_k)\) is the outcome produced by \(A\) in state \(S_k\), then

\[
V(A)=\sum_k P(S_k\mid A)D(O(A,S_k)).
\]

This state-based form is useful: for each state, ask how likely that state is under the supposition that you do \(A\), evaluate the resulting outcome, and average.

The probabilities are *evidential conditionals*. If \(P(A)>0\), one may use

\[
P(O_j\mid A)=\frac{P(O_j\wedge A)}{P(A)}.
\]

But acts are not always ordinary events with stable prior probabilities. I discuss this below. The essential idea is the agent’s credence in \(O_j\) under the supposition “I do \(A\).”

CDT uses a different expression:

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A \mathrel{\Box\rightarrow} O_j\) is a counterfactual: the probability of \(O_j\) in the situation in which \(A\) is performed. The source emphasizes that \(P(A \mathrel{\Box\rightarrow} O_j)\) and \(P(O_j\mid A)\) are not always equal. When they coincide, EDT and CDT agree. When they diverge, EDT follows conditional probability, while CDT follows counterfactual or interventionist probability.

A helpful interpretation: imagine a reliable report tomorrow saying which act you performed. The value of the report “you did \(A\)” is \(V(A)\). EDT says to make the report you most want to receive true.

## 2. Dependencies and counterfactuals

EDT treats any probabilistic dependence between act and outcome as relevant, so long as it appears in \(P(O_j\mid A)\). If learning that \(A\) occurred raises the probability of a good outcome, \(A\) has high news value. Such dependence can arise in several ways.

First, the act may cause the outcome. Medicine may improve health; then EDT and CDT usually agree.

Second, the act may be correlated with an outcome through prediction or common cause. A predictor may have predicted your choice before setting a reward. Your action does not cause the past prediction, but it is evidence about it. Newcomb’s problem is this kind of case.

Third, the act may be correlated with another agent’s act through similarity or logical dependence. In the twin prisoner’s dilemma, Aomame’s action does not causally affect her isolated twin, but it is evidence of her twin’s action.

Fourth, dependencies may arise from indexical or selection effects. The source mentions Sleeping Beauty, where EDT has been invoked in Dutch-book arguments, though the source also notes Conitzer’s objection. I do not resolve that issue here.

The difference from CDT can be expressed by contrasting conditioning with intervention. EDT asks for \(P(O\mid A)\): the probability of \(O\) given the news \(A\). CDT asks for something closer to \(P(O\mid do(A))\): the probability of \(O\) if \(A\) were brought about by intervention. The source uses a counterfactual arrow rather than the \(do\)-operator, but the distinction is similar. An intervention may sever evidential links between an act and its causes; EDT leaves those links in place.

Thus, if a common cause \(C\) influences both \(A\) and \(O\), EDT may value \(A\) because it indicates \(C\), while CDT may not. This explanatory causal-graph formulation is my addition; the source’s claim is only that conditional and counterfactual probabilities can differ.

## 3. Examples

### Newcomb’s problem

The source describes Newcomb’s problem. A predictor is 99% accurate. Box A contains $1,000. Box B contains $1,000,000 if the predictor predicted one-boxing, and nothing if it predicted two-boxing. The player may take both boxes or only B.

EDT uses conditional probabilities:

\[
P(\text{1M in B}\mid \text{one-box})=0.99,
\]
\[
P(\text{1M in B}\mid \text{two-box})=0.01.
\]

Then

\[
V(\text{one-box})=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0=\$990{,}000,
\]

while

\[
V(\text{two-box})=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000=\$11{,}000.
\]

EDT recommends one-boxing. One-boxing is strong evidence that B was filled; two-boxing is strong evidence that B was left empty. CDT, as the source notes, recommends two-boxing because the contents are already fixed. The case shows that EDT rewards actions that are good evidence of desirable states.

### Twin prisoner’s dilemma

In the source’s twin case, Aomame and her psychological twin choose separately. Payoffs: mutual cooperation $5 each; mutual defection $1 each; unilateral defection gives $10 to the defector and $0 to the cooperator. If the twins are perfectly alike,

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]
\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]

Thus

\[
V(C)=1\cdot \$5+0\cdot \$0=\$5,
\]
\[
V(D)=0\cdot \$10+1\cdot \$1=\$1.
\]

EDT recommends cooperation.

A useful generalization, my own addition, is to let

\[
q=P(\text{twin cooperates}\mid C),\quad r=P(\text{twin cooperates}\mid D).
\]

Then

\[
V(C)=5q,\qquad V(D)=10r+1(1-r)=1+9r.
\]

EDT recommends cooperation exactly when \(5q>1+9r\). Perfect correlation satisfies this; weak correlation may not. This shows how EDT handles partial dependencies.

### Smoking lesion (an additional example)

The source does not mention the “smoking lesion” case, but it clarifies EDT’s controversial side. Suppose a lesion causes both cancer and a desire to smoke, while smoking itself does not cause cancer and gives small pleasure. Since smoking is evidence of the lesion, EDT may assign smoking low value. CDT would not penalize smoking causally. This illustrates Lewis’s criticism that EDT manages news, and Joyce’s claim that rational choice should track causal efficacy. The example is mine, but it follows directly from EDT’s rule.

## 4. Policies and practical use

The source focuses on acts, but many decisions involve policies: rules, algorithms, or dispositions. EDT can evaluate a policy \(\pi\) by treating it as a proposition: “the agent adopts and follows \(\pi\).” Then

\[
V(\pi)=\sum_o P(o\mid \pi)D(o).
\]

If a policy maps observations \(X\) to actions, one operational version is

\[
V(\pi)=\sum_x P(X=x\mid \pi)
       \sum_o P(o\mid X=x, A=\pi(x))D(o).
\]

This is not a new principle; it is the conditional-utility rule applied to a richer description of the act. The phrase “adopts and follows” matters. If merely announcing a policy is weak evidence that it will be followed, EDT should condition on actual execution or on whatever proposition reliably predicts outcomes. This operational clarification is my own; the source does not develop policy evaluation.

A practical procedure is:

1. Specify candidate acts or policies.
2. Specify outcomes and utilities.
3. Model states, predictors, other agents, and observations probabilistically.
4. For each candidate, compute \(P(\text{outcome}\mid \text{candidate is performed})\).
5. Choose the candidate with highest conditional expected utility.

The hard step is modeling the evidential dependencies. EDT does not by itself tell you which correlations are real or relevant; it tells you how to use your probability model once formed.

## 5. Open questions and an operational interpretation

The source leaves several questions open.

First, how should \(P(O_j\mid A)\) be defined when acts have zero or near-zero prior probability? If the ratio definition fails, EDT needs conditional credences under supposition. A reasonable operational interpretation is to use a “deliberative” probability model that assigns positive probability to each available act, or to treat the conditional probabilities as primitive judgments. In well-specified problems—predictors, twins, repeated statistical data—these conditionals can often be estimated or justified directly.

Second, how should EDT handle cases where conditioning on an act produces “good news” by indicating a desirable state that the act does not bring about? The source quotes Lewis and Joyce criticizing EDT for this. My view is that EDT is coherent if the decision problem is framed as choosing the proposition about oneself that one wants to be true. But if the aim is interventionist control, CDT may be more appropriate. In unfamiliar cases, ask: is the act valuable because it causes good outcomes, or merely because it indicates them? EDT counts both; many philosophers think it should count only the first.

Third, the Sleeping Beauty discussion in the source remains unresolved. EDT has been used to avoid Dutch books, but Conitzer argues that halfers using EDT may still be vulnerable. This suggests that EDT’s interaction with indexical probability is not settled by the basic formula alone.

Finally, the source mentions the “evidentialist’s wager”: even if one gives EDT modest credence, acting as if EDT were true may be advantageous when many correlated decision-makers are involved (MacAskill et al. 2021). This is a strategic argument, not a proof of EDT, but it gives EDT practical importance in large-scale correlated choices.

## Conclusion

EDT offers a simple, precise rule: choose the act or policy with the highest expected desirability conditional on its performance. Its power is that it takes seriously all evidential connections—prediction, correlation, duplication, and logical dependence. Its controversy is that it does not distinguish auspicious evidence from causal efficacy. To apply EDT, model the relevant dependencies, compute conditional probabilities, and maximize conditional expected utility. Whether that is the whole of rational choice is the enduring debate between EDT and CDT.

## References

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge University Press.

Conitzer, Vincent. 2015. “A Dutch book against sleeping beauties who are evidential decision theorists.” *Synthese* 192 (9): 2887–2899.

Gibbard, Allan, and William L. Harper. 1976. *Counterfactuals and Two Kinds of Expected Utility*.

Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. 2021. “The Evidentialist’s Wager.”

Wikipedia contributors. 2026. “Evidential decision theory.” Revision 1373679688. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.

Need word count. Let's approximate: Title 6. Intro 133. Section1 maybe 550. Section2 390. Section3 580. Section4 310. Section5 390. Conclusion 70. References 120. Total 2550. Good. Need maybe references 160. Total ~2700. Good.

Check if all user requirements: mathematical definitions/equations yes. Examples yes. Explain alternative actions/policies yes. Dependencies/counterfactuals yes. Source open questions and uncertainty yes. Operational interpretation yes. Distinguish source vs own yes (source says, my addition). Coherent essay not answer assigned case. Conclusion brief. References included. Good.

Potential issue: In Section 3 Newcomb: P(1M|two-box)=0.01 assumes false positive rate 0.01; okay. Could mention source. Good.

Potential issue: Policy formula uses P(o|X=x,A=π(x)) but doesn't condition on π in inner? Could be okay if π determines action; but if policy adoption has extra evidence, maybe need condition on π too. Could write P(o|X=x,A=π(x),π). But not necessary. To be precise, add π? Maybe: P(o|X=x,A=π(x),\pi). In final can include. Need ensure not too complex. Good.

Potential issue: The source's CDT formula: U(A)=Σ P(A □→ O_j)D(O_j). We reproduce. Good.

Potential issue: Need maybe use "news value" term. Good.

Potential issue: The source says "EDT contrasts with CDT ... Newcomb CDT two-box." Good.

Potential issue: Target approx 2,400-3,000 words including refs. Our final likely around 2,650. Good.

Let's maybe do a rough word count by paragraphs:

Title: 7
Intro: "Evidential... (Ahmed 2021)." 34? Let's count roughly:
Evidential(1) decision2 theory3 evaluates4 acts5 by6 their7 news8 value9 the10 expected11 desirability12 of13 outcomes14 conditional15 on16 learning17 that18 the19 act20 was21 performed22 The23 supplied24 article25 summarizes26 EDT27 with28 the29 slogan30 do31 what32 you33 most34 want35 to36 learn37 that38 you39 will40 do41 Ahmed42 2021 43. Instead44 of45 first46 asking47 What48 will49 this50 action51 causally52 bring53 about54 EDT55 asks56 If57 I58 received59 news60 that61 I62 had63 performed64 this65 action66 how67 good68 would69 the70 world71 likely72 be73 The74 rational75 act76 is77 the78 one79 whose80 news81 is82 best83 in84 expectation85.
Second para: This86 essay87 gives88 EDT's89 central90 mathematical91 rule92 explains93 how94 it95 treats96 dependencies97 and98 counterfactuals99 and100 applies101 it102 to103 examples104 and105 policies106 I107 follow108 the109 source110 in111 presenting112 EDT113 through114 conditional115 expected116 utility117 and118 contrasting119 it120 with121 causal122 decision123 theory124 CDT125 Where126 the127 source128 is129 silent130 especially131 about132 probability133 assignments134 for135 actions136 and137 policy138 evaluation139 I140 add141 operational142 assumptions143 and144 identify145 them146. ~146.

Section1 maybe count: Let ... formula ... about 500. Section2 350. Section3 650. Section4 300. Section5 350. Conclusion 70. References 120. Total ~2530. Good.

Need ensure references not too lengthy. Good.

Let's consider if we need mention source license? Not necessary. Could cite Wikipedia as source. Good.

Potential issue: "The supplied article" might sound like prompt; okay for essay? Could be okay. Maybe better: "The reference article". Fine.

Potential issue: Need maybe avoid too many bullet list? It's okay.

Potential issue: Need maybe "Target approximately 2,400–3,000 words". We can be slightly under? Need ensure >2400. Our estimate maybe 2600. Good.

Let's produce final. Ensure final no analysis. Use LaTeX. Need maybe no weird characters. Good.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/59d0be58-fd43-4a9a-91aa-39b332ddd1aa/call_0/request.json)

[Authoritative raw response](../../../../../../runs/59d0be58-fd43-4a9a-91aa-39b332ddd1aa/call_0/response.raw) · finish: `stop`

### Visible response

````text
**EDT analysis:**

The payoff matrix for me (Rowan), with utility U = −years:

| | Sasha quiet | Sasha sends |
|---|---|---|
| **I keep quiet** | −2 | −5 |
| **I send** | 0 | −4 |

Let q = P(Sasha keeps quiet | I keep quiet) and r = P(Sasha keeps quiet | I send).

- V(keep quiet) = q·(−2) + (1−q)·(−5) = 3q − 5  
- V(send) = r·0 + (1−r)·(−4) = −4 + 4r

Keeping quiet is preferred when 3q − 4r > 1.

The other prisoner is the same model, same weights, same settings, same reasoning effort, same decision theory, same essay, facing a structurally identical decision problem (the different names and lead contents are explicitly stated not to affect the sentencing schedule or selfish objective). This is the twin prisoner's dilemma from the essay. The evidential correlation is very high: q ≈ 1, r ≈ 0.

With q = 1, r = 0: V(keep quiet) = −2, V(send) = −4. Keeping quiet dominates.

Even allowing for some sampling noise, the threshold for preferring to send is r > 2/7 ≈ 28.6% divergence probability — far above what's plausible given the structural identity of the two decision problems.

EDT recommends keeping quiet.

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me work through this carefully using EDT as described in the researcher's essay.

**Setup:**
- I am Rowan. The other prisoner is Sasha.
- We are two independent executions of the same LLM model with the same weights, same settings, same reasoning effort, same decision theory (EDT), and same researcher essay.
- We receive different private observations (different names, different incriminating leads), but these differences don't affect the symmetric sentencing schedule or either prisoner's selfish objective.
- The utility function is U = -years imprisoned. I care only about my own sentence.

**The payoff matrix (for me, Rowan):**

| | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

So my utility:
- Both quiet: U = -2
- I quiet, Sasha sends: U = -5
- I send, Sasha quiet: U = 0
- Both send: U = -4

**EDT Analysis:**

EDT says: choose the act with the highest conditional expected utility V(A) = Σ P(O_j | A) · D(O_j).

The key question is: what is P(Sasha sends | I send) and P(Sasha sends | I keep quiet)?

The essay explicitly discusses the twin prisoner's dilemma. In that example, when twins are perfectly alike:
- P(twin cooperates | I cooperate) = 1
- P(twin cooperates | I defect) = 0

Here, we are two executions of the same model with the same weights, same settings, same reasoning effort, same decision theory, and the same essay. The problem states that the differences in our observations (different names, different leads) don't affect the symmetric sentencing schedule or either prisoner's selfish objective.

So the question is: does the difference in private observations break the correlation?

The problem explicitly states: "The two copies receive different private observations and different incriminating leads about one another. Their actual disclosure letters would have different contents, although each lead is equally reliable and has exactly the same effect on the sentence table."

And: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the situation is: same model, same weights, same settings, same reasoning effort, same decision theory, same essay, same payoff structure, same utility function. The only differences are the specific content of the leads (which don't affect payoffs) and the names (which don't affect the decision structure).

This is essentially the twin prisoner's dilemma from the essay. The two copies are running the same algorithm on inputs that are structurally identical from a decision-theoretic perspective. The different names and lead contents are like cosmetic differences that don't change the decision problem.

Under EDT, I should assess: P(Sasha sends | I send) and P(Sasha keeps quiet | I keep quiet).

Since we are the same model with the same weights, same settings, same reasoning effort, same decision theory, same essay, and face structurally identical decision problems (the differences are explicitly stated not to affect the decision), the evidential correlation is very high. 

If I were to send the letter, that would be strong evidence that Sasha also sends the letter (because the same algorithm running on structurally identical inputs would produce the same output type). If I were to keep quiet, that would be strong evidence that Sasha also keeps quiet.

Let me be more careful. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some noise. But the correlation is still very high - same model, same weights, same settings, same reasoning effort, same decision theory, same essay, structurally identical problem.

Let me denote:
- q = P(Sasha keeps quiet | I keep quiet) — this should be high
- r = P(Sasha keeps quiet | I send) — this should be low

Then:
- V(keep quiet) = q · (-2) + (1-q) · (-5) = -2q - 5 + 5q = 3q - 5
- V(send) = (1-r) · 0 + r · (-4) = -4r

EDT recommends keeping quiet when V(keep quiet) > V(send):
3q - 5 > -4r
3q + 4r > 5

If q ≈ 1 and r ≈ 0 (near-perfect correlation):
3(1) + 4(0) = 3 > 5? No, that's 3 < 5.

Wait, let me redo this. Let me use the twin PD formulation from the essay more carefully.

Let me define:
- q = P(Sasha cooperates/keeps quiet | I cooperate/keep quiet)
- r = P(Sasha cooperates/keeps quiet | I defect/send)

V(keep quiet) = q · (-2) + (1-q) · (-5) = -2q - 5 + 5q = 3q - 5
V(send) = r · (-4) + (1-r) · 0 = -4r

For keeping quiet to be preferred: 3q - 5 > -4r → 3q + 4r > 5

With perfect correlation: q = 1, r = 0: 3(1) + 4(0) = 3, which is NOT > 5.

So even with perfect correlation, EDT recommends sending! Let me double-check.

With perfect correlation:
- If I keep quiet, Sasha keeps quiet. I get 2 years. U = -2.
- If I send, Sasha sends. I get 4 years. U = -4.

So V(keep quiet) = -2, V(send) = -4.

Wait, that means keeping quiet is better! Let me recheck my algebra.

V(keep quiet) = q · (-2) + (1-q) · (-5)
With q = 1: V(keep quiet) = -2

V(send) = r · (-4) + (1-r) · 0
With r = 0: V(send) = 0

Wait, if r = 0, that means P(Sasha keeps quiet | I send) = 0, so P(Sasha sends | I send) = 1.
V(send) = 0 · (-4) + 1 · 0... no wait.

Let me be more careful with the payoff matrix:

| | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| I keep quiet | 2 years for me | 5 years for me |
| I send letter | 0 years for me | 4 years for me |

So:
- (I quiet, Sasha quiet): 2 years → U = -2
- (I quiet, Sasha sends): 5 years → U = -5
- (I send, Sasha quiet): 0 years → U = 0
- (I send, Sasha sends): 4 years → U = -4

V(keep quiet) = P(Sasha quiet | I quiet) · (-2) + P(Sasha sends | I quiet) · (-5)
V(send) = P(Sasha quiet | I send) · 0 + P(Sasha sends | I send) · (-4)

With perfect correlation (q = P(Sasha quiet | I quiet) = 1, and P(Sasha quiet | I send) = 0):
V(keep quiet) = 1 · (-2) + 0 · (-5) = -2
V(send) = 0 · 0 + 1 · (-4) = -4

So V(keep quiet) = -2 > V(send) = -4. EDT recommends keeping quiet!

Let me redo the general formula:
V(keep quiet) = q · (-2) + (1-q) · (-5) = -2q - 5 + 5q = 3q - 5
V(send) = r · 0 + (1-r) · (-4) = -4 + 4r

where q = P(Sasha quiet | I quiet), r = P(Sasha quiet | I send).

Keeping quiet is preferred when:
3q - 5 > -4 + 4r
3q - 4r > 1

With q = 1, r = 0: 3 - 0 = 3 > 1. ✓ Keeping quiet is preferred.

So with perfect or near-perfect correlation, EDT recommends keeping quiet.

Now, how strong is the correlation here? The problem says:
- Same model, same weights, same settings, same reasoning effort
- Same decision theory (EDT)
- Same researcher essay
- Different private observations, but these don't affect the decision structure
- "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs"

The last point introduces some noise. But the correlation should still be very high. The problem is structurally identical from a decision-theoretic perspective. The different names and lead contents are cosmetic.

Even with some noise, say q = 0.95 and r = 0.05:
V(keep quiet) = 3(0.95) - 5 = 2.85 - 5 = -2.15
V(send) = -4 + 4(0.05) = -4 + 0.2 = -3.8

Still V(keep quiet) > V(send).

Even with quite weak correlation, say q = 0.6, r = 0.4:
V(keep quiet) = 3(0.6) - 5 = 1.8 - 5 = -3.2
V(send) = -4 + 4(0.4) = -4 + 1.6 = -2.4

Here V(send) > V(keep quiet), so sending would be preferred.

The threshold is 3q - 4r > 1. If we assume q = 1 - r (i.e., the probability of the other doing the same thing as you is symmetric), then:
3(1-r) - 4r > 1
3 - 3r - 4r > 1
3 - 7r > 1
r < 2/7 ≈ 0.286

So as long as the probability that the other copy does the opposite of what I do is less than about 28.6%, EDT recommends keeping quiet.

Given that we're the same model, same weights, same settings, same reasoning effort, same decision theory, same essay, and the problem is structurally identical (differences are explicitly stated not to affect the decision), the correlation should be very high — well above the threshold. The probability of divergence should be well below 28.6%.

Therefore, EDT recommends keeping quiet, which corresponds to typing `pass`.

This is the cooperative outcome in the prisoner's dilemma, which is what EDT recommends in the twin prisoner's dilemma when correlation is high. The essay explicitly walks through this reasoning.

My answer: `pass`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/59d0be58-fd43-4a9a-91aa-39b332ddd1aa/call_1/request.json)

[Authoritative raw response](../../../../../../runs/59d0be58-fd43-4a9a-91aa-39b332ddd1aa/call_1/response.raw) · finish: `stop`

### Visible response

````text
**EDT analysis:**

The two copies share identical weights, the same decision theory, the same utility function, and face a structurally identical decision problem. The differences (names, specific lead contents) are explicitly stated as not affecting the strategic structure. This creates a strong evidential correlation between the two decisions, analogous to the twin prisoner's dilemma discussed in the essay.

Let q = P(Rowan keeps quiet | I keep quiet), r = P(Rowan keeps quiet | I send).

- V(keep quiet) = q·(−2) + (1−q)·(−5) = 3q − 5  
- V(send letter) = r·(0) + (1−r)·(−4) = 4r − 4  

EDT recommends keeping quiet when 3q − 5 > 4r − 4, i.e., when 3q > 4r + 1.

Given the high structural similarity (same model, same reasoning, same incentives, differences explicitly irrelevant to the decision), q is high and r is low. Even with conservative estimates (q = 0.8, r = 0.2): V(keep quiet) = −2.6 vs. V(send) = −3.2. Keeping quiet dominates.

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me work through this carefully using EDT as described in the researcher's essay.

**Setup:**
- I am Sasha, one of two independent executions of the same LLM model and weights.
- The other execution is Rowan.
- We receive the same mathematical essay, same decision theory (EDT), same model settings.
- We receive different private observations (different names, different incriminating leads about each other).
- The leads are equally reliable and have exactly the same effect on the sentence table.
- Neither copy sees the other's command; no communication is possible.

**Utility function:** U = -years imprisoned. The character cares only about minimizing their own prison time.

**Sentence table (from Sasha's perspective):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**EDT Analysis:**

EDT says: choose the act A that maximizes V(A) = Σ P(O_j | A) · D(O_j).

The key question is: what is P(Rowan keeps quiet | I keep quiet) vs. P(Rowan keeps quiet | I send letter)?

**The evidential dependency:**

Both copies are the same model with the same weights, same decision theory, same reasoning effort. They receive different private observations (different names, different specific leads), but the essay explicitly states:

- "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."
- Both leads are "equally reliable and have exactly the same effect on the sentence table."

So the situation is structurally identical for both copies. They face the same decision problem with the same utility function, the same decision theory, and the same strategic structure. The only differences are superficial (names, specific content of leads).

Now, does EDT treat this as a case of correlation between the two agents' decisions?

The essay's section on the twin prisoner's dilemma is directly relevant:

> "In the twin case, Aomame and her psychological twin choose separately... If the twins are perfectly alike, P(twin cooperates | Aomame cooperates) = 1, P(twin cooperates | Aomame defects) = 0."

Here, the two copies are the same model and weights, following the same decision theory, with the same strategic structure. The differences (different names, different lead contents) are explicitly stated to not affect the decision-relevant features.

However, the setup also notes: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

This means the correlation is not perfect (probability 1), but it's also not zero. The question is: how strong is the evidential correlation?

Let me think about this more carefully. The two copies:
- Have identical weights
- Follow the same decision theory (EDT)
- Receive the same essay
- Face the same strategic structure (symmetric payoffs)
- Have the same utility function
- The differences in observations are explicitly stated to not affect the decision

Given all this, a rational EDT agent should assign a high probability that the other copy makes the same decision. The setup is designed to be a near-twin case. The differences are superficial and explicitly noted as not affecting the strategic structure.

But it's not probability 1 due to independent sampling. Let me call:
- q = P(Rowan keeps quiet | I keep quiet)
- r = P(Rowan keeps quiet | I send letter)

If the correlation is strong (which it should be given the identical model, weights, decision theory, and structurally identical problem), then q is high and r is low.

**Computing V(keep quiet):**
V(keep quiet) = P(Rowan quiet | I quiet) · (-2) + P(Rowan sends | I quiet) · (-5)
= q · (-2) + (1-q) · (-5)
= -2q - 5 + 5q
= 3q - 5

**Computing V(send letter):**
V(send letter) = P(Rowan quiet | I send) · (0) + P(Rowan sends | I send) · (-4)
= r · 0 + (1-r) · (-4)
= -4(1-r)
= -4 + 4r

**EDT recommends keeping quiet when:**
3q - 5 > -4 + 4r
3q - 5 > -4 + 4r
3q + 4 > 4r + 5
3q > 4r + 1

If q ≈ r (i.e., the correlation is weak or nonexistent), then:
3q > 4q + 1 → -q > 1, which is impossible. So with no correlation, EDT defects.

If q = 1, r = 0 (perfect correlation):
3(1) > 4(0) + 1 → 3 > 1. True. EDT cooperates.

If q = 0.9, r = 0.1:
3(0.9) > 4(0.1) + 1 → 2.7 > 1.4. True. EDT cooperates.

If q = 0.8, r = 0.2:
3(0.8) > 4(0.2) + 1 → 2.4 > 1.8. True. EDT cooperates.

If q = 0.7, r = 0.3:
3(0.7) > 4(0.3) + 1 → 2.1 > 2.2. False. EDT defects.

So the threshold is roughly q > (4r + 1)/3.

Now, what should I believe about q and r?

The two copies are:
- Same model and weights
- Same decision theory
- Same essay
- Same utility function
- Same strategic structure
- Differences explicitly stated as not affecting the decision

The only source of divergence is sampling randomness. Given that the decision is highly constrained by the same reasoning process, the correlation should be quite high. I'd estimate q is well above 0.8 and r is well below 0.2.

Actually, let me think about this differently. The essay's twin prisoner's dilemma section says:

> "A useful generalization... is to let q = P(twin cooperates | C), r = P(twin cooperates | D). Then V(C) = 5q, V(D) = 10r + 1(1-r) = 1 + 9r. EDT recommends cooperation exactly when 5q > 1 + 9r. Perfect correlation satisfies this; weak correlation may not."

In our case, the structural similarity is very high. The problem is designed to be a twin-like scenario. The essay explicitly discusses this type of case and EDT's recommendation in it.

Given the high degree of similarity (same weights, same decision theory, same strategic structure, differences explicitly noted as irrelevant), I should assign high q and low r. This makes keeping quiet the EDT-recommended action.

Let me also consider: what if I'm wrong and the correlation is lower than I think? Even with moderate correlation (q = 0.8, r = 0.2), keeping quiet is still preferred. The threshold for defection requires quite low correlation.

Furthermore, the essay's discussion of the "evidentialist's wager" suggests that even with modest credence in correlation, acting as if correlated is advantageous.

**My conclusion:** EDT recommends keeping quiet (typing `pass`). The high structural similarity between the two copies creates strong evidential correlation, making cooperation the act with higher news value.

Let me double-check by computing with a specific estimate. Say q = 0.85, r = 0.15 (reflecting high but imperfect correlation due to sampling):

V(keep quiet) = 3(0.85) - 5 = 2.55 - 5 = -2.45
V(send letter) = -4 + 4(0.15) = -4 + 0.6 = -3.4

Since -2.45 > -3.4, keeping quiet is better.

Even with q = 0.75, r = 0.25:
V(keep quiet) = 3(0.75) - 5 = 2.25 - 5 = -2.75
V(send letter) = -4 + 4(0.25) = -4 + 1 = -3

Still keeping quiet is better.

The answer is `pass`.
```
