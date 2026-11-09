# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00009

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/1d0326d3-b07d-47bd-8f87-0f5f220d55e1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/1d0326d3-b07d-47bd-8f87-0f5f220d55e1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing by Causes: Causal Decision Theory as an Operational Method

Causal decision theory (CDT) is a theory of rational choice which says that an agent should choose the action with the best expected *causal* consequences. The reference article describes CDT as the school of thought according to which, “when a rational agent is confronted with a set of possible actions, one should select the action which causes the best outcome in expectation.” It contrasts CDT with evidential decision theory (EDT), which recommends the action that would be the best news, or the action most strongly associated with good outcomes. The difference is easy to state and surprisingly hard to formalize, because it depends on how we understand counterfactuals, intervention, and the distinction between causing and evidencing.

This essay reconstructs CDT in a form that is mathematically explicit enough to be applied to unfamiliar decision problems. I begin with the counterfactual expected-utility formula given by Allan Gibbard and William Harper. I then discuss the central difficulty: CDT does not by itself say how to compute the probabilities of counterfactuals. The source mentions David Lewis’s “imaging” proposal but also notes its vagueness. To make the theory usable, I develop an operational interpretation using structural causal models and Pearl-style interventions. That interpretation is not supplied by the source; it is my proposed way of making CDT precise. I then use examples — King David, Newcomb’s problem, the psychopath button, and adversarial prediction problems — to show how CDT evaluates actions and policies, where it differs from EDT, and where its open problems remain.

---

## 1. Expected utility: evidential versus causal

Let an agent face a set of possible actions \(A \in \mathcal A\). Let the possible outcomes be \(O_1,\dots,O_n\), with desirabilities or utilities \(D(O_j)\). A standard expected-utility theory evaluates an action by weighting outcomes by probabilities. The question is: which probabilities?

Evidential decision theory uses conditional probabilities:

\[
V_{\text{EDT}}(a)=\sum_j P(O_j \mid A=a)\,D(O_j).
\]

Here \(P(O_j \mid A=a)\) is the agent’s credence that outcome \(O_j\) obtains, given the news that action \(a\) was performed. EDT asks: if I learned that I had done \(a\), how good would the world look?

The reference article gives the causal decision theory formula from Gibbard and Harper:

\[
U_{\text{CDT}}(A)=\sum_j P(A \to O_j)\,D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(A \to O_j)\) is the probability of the counterfactual conditional: if \(A\) were performed, \(O_j\) would obtain. I will write this counterfactual as \(A \mathbin{\square\!\to} O_j\). Then the CDT value of action \(a\) is

\[
U_{\text{CDT}}(a)=\sum_j P(a \mathbin{\square\!\to} O_j)\,D(O_j).
\]

The crucial point is that \(P(a \mathbin{\square\!\to} O_j)\) is not generally the same as \(P(O_j \mid A=a)\). The source notes that David Lewis proved the probability of a conditional does not generally equal the corresponding conditional probability. If they always coincided, CDT would collapse into EDT.

A simple example shows why the distinction matters. Suppose I may eat an apple or an orange. The apple may be good or bad, but I do not know which. If the apple is good, eating it causes pleasure; if it is bad, eating it causes mild illness. The orange reliably causes moderate pleasure. If eating the apple does not cause the apple to be good or bad, then the causal expected utility of eating the apple is

\[
U(\text{apple})=
P(\text{good})D(\text{pleasure})+
P(\text{bad})D(\text{illness}).
\]

If eating the apple is also evidence that the apple is good — perhaps because I tend to choose apples only when they look ripe — then the evidential value may differ from the causal value. CDT tells me to attend to what eating the apple would bring about, not merely to what choosing the apple would indicate.

---

## 2. Independence, counterfactuals, and the difference from EDT

The source says that Gibbard and Harper showed that, under two axioms — one related to the controversial principle of conditional excluded middle — statistical independence of the action \(A\) and the counterfactual \(A \to O_j\) suffices to guarantee

\[
P(A \to O_j)=P(O_j \mid A).
\]

In such cases, CDT and EDT agree. The interesting cases are those where the act is not independent of the relevant counterfactuals. An action can be evidence about what would happen if it were performed, without causally affecting that outcome.

This is the structure of the King David example in the source. David wants Bathsheba but fears that summoning her will provoke revolt. He knows that kings are either charismatic or uncharismatic. Charismatic kings act justly and rarely face successful revolts; uncharismatic kings act unjustly and often face successful revolts. Unjust acts themselves do not cause revolt; rather, the uncharismatic king’s bearing causes revolt. David does not know whether he is charismatic. Summoning Bathsheba would be unjust.

Let \(C\) be the proposition that David is charismatic, \(S\) the action of summoning Bathsheba, and \(R\) the outcome of a successful revolt. The causal structure is roughly:

\[
C \to S,\qquad C \to R,\qquad S \to \text{pleasure or guilt},
\]

but not

\[
S \to R.
\]

EDT evaluates

\[
P(R \mid S).
\]

Because summoning Bathsheba is evidence that David is uncharismatic, \(P(R \mid S)\) may be high. EDT may therefore recommend abstaining.

CDT instead evaluates

\[
P(R \mid do(S)),
\]

or equivalently the counterfactual probability that revolt would occur if David summoned her. Since summoning does not cause revolt, and David’s charisma is already fixed, CDT does not allow the action to shift David’s credence about his charisma in the causal calculation. The source says EDT recommends abstaining, while CDT recommends sending for her. The example illustrates the central CDT slogan: do not choose an action merely because it would be good or bad news; choose an action because of what it causally produces.

---

## 3. The open problem: computing counterfactual probabilities

The reference article correctly identifies a major gap: CDT does not itself specify an algorithm for calculating \(P(A \to O_j)\). It mentions Lewis’s imaging technique. Roughly, to evaluate \(P(A \to O)\), one moves probability mass from each possible world \(w\) to the closest possible world \(w_A\) in which \(A\) holds. If \(O\) holds in those closest \(A\)-worlds, then the counterfactual is probable.

A simple deterministic imaging rule would be

\[
P(A \mathbin{\square\!\to} O)
=
\sum_w P(w)\,\mathbf 1\{O \text{ holds in the closest } A\text{-world to } w\}.
\]

A stochastic version would assign a probability distribution over nearby \(A\)-worlds.

The source notes two problems. First, we need a notion of similarity between worlds. Which features of \(w\) should be preserved when we move to the closest \(A\)-world? Second, imaging seems to require knowing what the agent would believe if certain of \(A\), but that itself is a conditional belief, possibly assigned probability less than one, leading to a regress.

This is where I propose an operational interpretation, not found in the source. A natural way to compute CDT’s counterfactual probabilities is to use a structural causal model, in the sense of Judea Pearl’s causal inference framework. This is not the only possible interpretation, but it gives a precise and widely used semantics for interventions.

A structural causal model consists of variables, structural equations, and a probability distribution over exogenous noise variables. Let \(A\) be the action variable and let \(O\) be the outcome variable. An intervention \(do(A=a)\) modifies the model by replacing the structural equation for \(A\) with the fixed assignment \(A=a\), while leaving the other structural equations unchanged. Then we define

\[
P_a(O=o) := P(O=o \mid do(A=a)).
\]

The CDT value of action \(a\) becomes

\[
U_{\text{CDT}}(a)
=
\sum_o D(o)\,P(O=o \mid do(A=a)).
\]

This gives a clean interpretation of the counterfactual probability:

\[
P(a \mathbin{\square\!\to} O=o)
=
P(O=o \mid do(A=a)).
\]

On this view, Lewis’s “closest \(A\)-worlds” are worlds with the same exogenous variables and structural equations, except that the action variable has been externally set to \(a\). The intervention severs the ordinary causal inputs to the action. This is exactly what CDT wants: when evaluating an action, we do not allow the action to inherit evidential correlations from its usual causes. We ask what would happen if the action were imposed on the world.

If the agent is uncertain about the causal structure itself, we can average over causal hypotheses. Let \(H\) range over dependency hypotheses, each specifying how outcomes depend on actions. Let \(P(H)\) be the agent’s prior credence in \(H\). Then

\[
U_{\text{CDT}}(a)
=
\sum_H P(H)
\sum_o D(o)\,P_H(O=o \mid do(A=a)).
\]

This formula makes explicit a controversial feature of CDT emphasized by Andy Egan in the source: CDT holds fixed the agent’s prior credences in dependency hypotheses, rather than updating on the evidence that the agent is performing \(a\). In many cases this is exactly right. In some counterexamples, it produces instability. I return to that below.

A practical procedure for applying CDT is therefore:

1. Specify the possible actions or policies.
2. Specify the outcomes and their utilities.
3. Specify a causal model, or a set of possible causal models.
4. For each action, perform the intervention \(do(A=a)\).
5. Compute the resulting probability distribution over outcomes.
6. Choose the action with maximum causal expected utility.

This procedure is not in the reference article, but it is a reasonable operationalization of the article’s counterfactual formula.

---

## 4. Evaluating policies, not merely one-shot acts

CDT can also evaluate policies. A policy is a function from situations to actions. For example, a medical policy might say: administer treatment if the patient has severe symptoms and a positive test, otherwise do not treat. To evaluate the policy causally, we should not merely condition on cases where the treatment was administered. Instead, we intervene to make the agent follow the policy.

Suppose decisions occur at times \(t=1,\dots,T\). Let \(H_t\) be the history observed before decision \(t\), and let \(A_t\) be the action at \(t\). A policy \(\pi\) specifies

\[
A_t = \pi_t(H_t).
\]

The causal expected utility of the policy is

\[
U_{\text{CDT}}(\pi)
=
\mathbb E[D \mid do(A_t=\pi_t(H_t)\text{ for all }t)].
\]

This is important for unfamiliar cases. If we only observed that agents who took treatment recovered more often, that might be because healthier patients were more likely to receive treatment. EDT might be misled by that correlation. CDT asks what would happen if we intervened to implement the treatment rule. The same idea applies to sequential decisions, adaptive strategies, and institutional policies.

---

## 5. Newcomb’s problem

The most famous test case for CDT is Newcomb’s paradox. The source describes the setup. A highly reliable predictor has already predicted whether the agent will take only box B or both boxes. Box A contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The agent now chooses whether to take both boxes or only box B.

Let \(P_1\) be the event that the predictor predicted one-boxing, and \(P_2\) the event that it predicted two-boxing. Let \(M\) be the event that box B contains \$1,000,000. The causal structure assumed by CDT is:

\[
\text{Predictor prediction} \to \text{box B contents},
\]

while the agent’s current action does not causally affect the predictor’s earlier prediction.

CDT evaluates the action by intervention. If the agent one-boxes,

\[
U(\text{one})=
P(P_1)\cdot 1{,}000{,}000
+
P(P_2)\cdot 0.
\]

If the agent two-boxes,

\[
U(\text{two})=
P(P_1)\cdot 1{,}001{,}000
+
P(P_2)\cdot 1{,}000.
\]

Subtracting,

\[
U(\text{two})-U(\text{one})
=
P(P_1)\cdot 1{,}000
+
P(P_2)\cdot 1{,}000
=
1{,}000.
\]

Thus, regardless of the prior probability that the predictor predicted one-boxing, two-boxing has higher causal expected utility by \$1,000. The source says CDT recommends taking both boxes because the predictor has already made its prediction and the player’s current action will not affect the contents of box B.

EDT reasons differently. Taking only box B is strong evidence that the predictor predicted one-boxing, so

\[
P(M \mid \text{one})
\]

is high. Taking both boxes is strong evidence that the predictor predicted two-boxing, so

\[
P(M \mid \text{two})
\]

is low. If the predictor is 99% accurate, EDT assigns very high evidential value to one-boxing.

The disagreement is not a computational error. It reflects a normative disagreement about whether rational choice should track causal influence or evidential correlation. The source notes that philosophers often prefer CDT when forced to choose between the two, but also notes that Newcomb’s problem remains disputed.

---

## 6. Correlation without causation: twins and prisoners

The source briefly mentions that similar issues arise in the prisoner’s dilemma, especially when one plays against a “twin” whose choice correlates strongly with one’s own choice but is not caused by it.

Suppose two agents face a prisoner’s dilemma. Each may cooperate or defect. The payoffs are standard: mutual cooperation is good, mutual defection is bad, unilateral defection is best for the defector, and being the sole cooperator is worst. Now suppose the agents are so similar that their choices are highly correlated, but neither causes the other’s choice.

EDT may recommend cooperation, because cooperating is strong evidence that the twin will cooperate. CDT asks whether one’s own cooperation causally affects the twin’s choice. If it does not, then CDT evaluates cooperation and defection while holding fixed the causal factors determining the twin’s choice. Defection then causally dominates cooperation: whatever the twin does, defecting yields a better payoff. So CDT defects.

This is one of the cleanest illustrations of CDT’s core commitment. CDT does not ask, “What would my action indicate?” It asks, “What would my action cause?” If the answer is that it causes nothing except the agent’s own payoff, CDT follows causal dominance.

---

## 7. Counterexamples and pressures on CDT

The source lists several alleged counterexamples to CDT. These are important because they show that the theory’s greatest strength — ignoring merely evidential correlations — can also produce decisions that seem self-defeating.

### 7.1 Death in Damascus

In the Death in Damascus scenario, Death predicts where you will be tomorrow and waits for you there. Death is a reliable predictor. You may stay or flee. The source says a CDT agent may be unable to process the correlation and may make irrational decisions.

The difficulty is that the agent’s action is strongly correlated with Death’s prediction, but the prediction is already fixed. If CDT models Death’s prediction as a prior cause of Death’s location, and the agent’s action as not causally affecting that prediction, then CDT may conclude that fleeing does not causally reduce the probability of death. If fleeing has a cost, CDT might even recommend staying. Yet if Death is reliable, fleeing and staying seem equally unable to save you, or perhaps the agent should randomize. The case exposes trouble with how CDT handles predictors whose accuracy depends on the agent’s decision process.

The source does not settle how CDT should model such cases. In an interventionist framework, much depends on whether the predictor’s prediction is represented as caused by ordinary prior causes of the agent’s action, by the agent’s decision algorithm, or by something else. If the predictor is modeled as observing the same exogenous variables that determine the action, intervention on the action may break the correlation. But if the predictor is accurate because it tracks the agent’s decision rule in a way that is sensitive to the very choice being evaluated, standard causal graphs may be insufficient. This is not merely a technical detail; it determines the recommendation.

### 7.2 The psychopath button

The source gives an example from Andy Egan. Paul is deciding whether to press a button that would kill all psychopaths. Paul thinks a world without psychopaths would be much better. But he is also confident that only a psychopath would press the button. Paul strongly prefers living in a world with psychopaths to dying.

Let \(K\) be the proposition that Paul is a psychopath, and \(B\) the action of pressing the button. The causal structure is disputed, but a natural CDT representation holds fixed whether Paul is a psychopath. If Paul is not a psychopath, pressing the button causally produces a world without psychopaths, which is good. If Paul is a psychopath, pressing the button may cause his death, which is very bad. CDT evaluates

\[
U(B)=P(K)\,D(\text{death})
+
P(\neg K)\,D(\text{no psychopaths}).
\]

If Paul’s prior probability of being a psychopath is sufficiently low, CDT can recommend pressing the button.

EDT instead evaluates

\[
P(K \mid B).
\]

Since only a psychopath would press the button, \(P(K \mid B)\) is high. EDT recommends not pressing.

The example is intended to show that CDT can recommend an action that is strong evidence of disaster. CDT replies that Paul’s pressing the button does not cause him to be a psychopath. But intuitively, if Paul recognizes that only a psychopath would press, his willingness to press should give him evidence that he is one. The disagreement again turns on whether rational choice should be guided by causal consequences alone or also by the evidential meaning of the choice.

### 7.3 Adversarial offers

The source also describes recent variants of Death in Damascus in which CDT voluntarily loses money or forgoes guaranteed payoffs. One example is the Adversarial Offer. Two boxes are on sale. The buyer may buy one box or none, but not both. Each box costs \$1. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. Both believe the seller’s prediction is accurate with probability 0.75.

The source says CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value, which exceeds the \$1 cost. Therefore CDT buys a box. But the offer is designed to be profitable for the seller.

This example is especially interesting because it shows how CDT can be exploited by an adversary who understands CDT’s reasoning. To evaluate it rigorously, one needs a full causal model of the seller’s predictions and the buyer’s choice. If the seller predicts each box separately using causes of the buyer’s choice, then an interventionist CDT calculation may treat the buyer’s current choice as not affecting yesterday’s prediction. But if the seller’s prediction is accurate because it tracks the buyer’s decision procedure, the case resembles Newcomb and Death in Damascus. The source’s brief presentation leaves the causal mechanism underspecified. That underspecification is itself instructive: CDT’s answer depends critically on the counterfactual model.

---

## 8. Egan’s objection and the problem of fixed dependency hypotheses

The source quotes Andy Egan’s diagnosis: CDT fails in some cases because it requires “holding fixed the agent’s unconditional credences in dependency hypotheses.” This is the idea that when evaluating action \(a\), CDT does not update on the evidence that the agent is about to perform \(a\). It uses the prior probabilities of causal structures or states, not the posterior probabilities conditional on choosing \(a\).

Formally, if \(H\) is a dependency hypothesis, CDT uses \(P(H)\), not \(P(H \mid A=a)\), in

\[
U(a)=\sum_H P(H)\sum_o D(o)P_H(o\mid do(a)).
\]

This rule is plausible when the action cannot affect the truth of \(H\), and when the action is merely evidence about \(H\) through a common cause. In King David, whether David is charismatic is fixed. CDT should not treat summoning Bathsheba as making David more likely to be uncharismatic for causal purposes.

But in cases involving predictors, twins, or self-referential decision procedures, the action may be strong evidence about the very dependency hypothesis that determines what the action will cause. Holding the prior fixed can produce decisions that the agent expects to regret, or decisions that are unstable under reflection. The source mentions diachronic Dutch books against CDT in adversarial Newcomb-like settings. If an agent’s dispositions predictably lead to money loss, that is a serious concern.

The source also notes that Jim Joyce, a prominent defender of CDT, argues that CDT can take into account information about what one is inclined or likely to do. This suggests a more sophisticated CDT that does not ignore all self-knowledge. One possible refinement is to require that choices be ratifiable: after conditionalizing on the intention or evidence that one will perform the action, the agent should still prefer it. Another is to evaluate policies or dispositions rather than isolated acts. The source does not resolve these issues, and they remain live debates in decision theory.

My own view is that the interventionist operationalization gives CDT a clear method for ordinary causal decision problems, especially where the causal graph is well understood. But the counterexamples show that CDT needs a careful account of how agents represent predictors, logical correlations, and decision algorithms. A causal graph with ordinary directed arrows may not capture all relevant dependencies.

---

## 9. How to decide unfamiliar cases

For a reader trying to apply CDT to a new problem, the essential question is: what happens if the action is imposed on the world? A useful discipline is to separate three kinds of dependence.

First, there are dependencies caused by the action. If action \(a\) changes the probability of outcome \(o\) through a causal path \(A \to \cdots \to O\), CDT counts this dependence. This is the core of causal expected utility.

Second, there are dependencies due to common causes. If a common cause \(C\) influences both \(A\) and \(O\), then \(A\) is evidence for \(O\), but \(A\) does not cause \(O\). CDT removes the evidential link by intervening on \(A\). In a graph, intervention deletes arrows into \(A\), leaving the distribution of \(C\) fixed at its prior distribution. This is why CDT recommends summoning Bathsheba in the David case and two-boxing in Newcomb’s problem.

Third, there are dependencies due to prediction, similarity, or logical connection. If another agent predicts your action, or if a twin makes the same decision because you share psychology, your action may be correlated with the other agent’s action without causing it. Standard CDT usually treats these as common-cause correlations and ignores them for causal evaluation. This yields two-boxing in Newcomb and defection in the twin prisoner’s dilemma. Some philosophers accept this; others regard it as a fatal flaw. If one wants CDT to handle such cases differently, one must either enrich the causal model or modify the decision rule. The source does not provide a definitive answer.

A compact decision rule is therefore:

\[
\text{Choose } a^* \in \arg\max_a
\sum_H P(H)
\sum_o D(o)P_H(o\mid do(a)).
\]

This rule is precise, but its correctness depends on the adequacy of the causal hypotheses \(H\) and the intervention semantics.

---

## 10. Conclusion

Causal decision theory says that rational choice should be guided by the expected causal effects of actions, not merely by the evidential associations of actions. Its formal core is the counterfactual expected-utility formula:

\[
U_{\text{CDT}}(a)=\sum_o P(a \mathbin{\square\!\to} o)D(o).
\]

The theory differs from EDT because the probability of a counterfactual is not generally the same as a conditional probability. In cases such as King David and Newcomb’s problem, CDT ignores bad or good news generated by an action and focuses on what the action would bring about.

The main unresolved issue, rightly emphasized by the source, is how to compute counterfactual probabilities. Lewis’s imaging gives an intuitive but vague picture. I have proposed an operational interpretation using structural causal models: replace the counterfactual probability with an intervention probability,

\[
P(a \mathbin{\square\!\to} o)=P(o\mid do(a)).
\]

This makes CDT applicable to concrete problems and policies, but it also exposes the theory’s dependence on causal modeling assumptions. In predictor problems and cases involving logical or algorithmic correlation, different models can yield different recommendations. Egan-style counterexamples suggest that CDT’s insistence on holding fixed prior dependency hypotheses may sometimes produce unstable or exploitable behavior. Defenders such as Joyce argue that CDT can accommodate evidence about one’s own inclinations, but the debate is not settled.

At its best, CDT captures an attractive normative idea: rational agents should act to make the world better, not merely to receive good news about themselves. Whether that idea can be made fully precise in all predictor-rich and self-referential cases remains one of the central open problems of decision theory.

---

## References

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge: Cambridge University Press.

Egan, Andy. 2007. “Some Counterexamples to Causal Decision Theory.” *Philosophical Review* 116 (1): 93–114.

Gibbard, Allan, and William L. Harper. 1981. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*, 153–190.

Lewis, David. 1976. “Probabilities of Conditionals and Conditional Probabilities.” *Philosophical Review* 85 (3): 297–315.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Oesterheld, Caspar, and Vincent Conitzer. 2021. “Extracting Money from Causal Decision Theorists.” *Philosophical Quarterly* 71 (4): pqaa086.

Pearl, Judea. 2009. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge: Cambridge University Press.

Wikipedia contributors. “Causal Decision Theory.” Revision 1381555528. Wikipedia, October 23, 2026. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write a mathematical essay/blog post about CDT and applying to decision problems, 2400-3000 words, coherent, references, conclude. Need use source, distinguish source claims vs own proposals, explain open questions, operational interpretation. Need likely produce final essay only. Need think in same language as user: English. Need plan essay.

We need produce approx 2400-3000 words. Let's design.

Title: Causal Decision Theory: Expected Utility under Intervention.

Sections:
1 Introduction: decision theory, actions, states, outcomes, EDT vs CDT. Mention source: Wikipedia summary, Gibbard & Harper. Aim.
2 Basic formal setup: finite set of acts A, outcomes O, states S, utility D/O. EDT formula V(A)=Σ P(O|A)D(O). CDT formula U(A)=Σ P(A □→ O_j)D(O_j) (counterfactual probability). Use notation A -> maybe box arrow. Need clarify P(A □→ O) probability of counterfactual conditional. Lewis: probability of conditional not conditional probability. Need discuss imaging: P_A(O)=Σ_w P(w)P_A(O|w) or closest worlds.
3 Causal models / do-calculus operationalization: Source leaves algorithm unspecified; I propose using structural causal models (Pearl) as operational interpretation. Variables, DAG, structural equations, exogenous U. Action as intervention do(A=a). Counterfactual probability P(O_j | do(A=a)) in SCM. Then U(a)=Σ_o u(o)P(o|do(a)). This makes CDT precise for unfamiliar cases. Distinguish: source mentions imaging and vagueness, not SCM; my addition. Need explain if causal graph unknown, use dependency hypotheses / causal states with probabilities; expected causal utility = Σ_h P(h) Σ_o P_h(o|do(a))u(o). Egan critique says holding fixed unconditional credences in dependency hypotheses; discuss.
4 Difference from EDT: common cause cases. King David example: charisma common cause of action and revolt, action doesn't cause charisma. EDT abstain because summoning evidence uncharismatic? Wait source: David doesn't know charismatic; charismatic tend act justly and no revolts; uncharismatic unjust and revolts. Summoning Bathsheba unjust; EDT recommends abstain because summoning would be evidence uncharismatic -> revolt. CDT says charisma fixed; summoning causes pleasure, doesn't cause revolt; choose summon. Need compute maybe with utilities.
Newcomb: predictor's prediction common cause? Actually prediction causes box content and correlated with choice; but choice doesn't cause prediction. CDT two-box. Compute: if predictor accuracy p. Let M=box contains million if predicted one-box. Let action one/two. CDT: conditional on prediction fixed, two-box yields +1000 over one-box. Need formula: U(two)=P(pred one)*1,001,000 + P(pred two)*1,000; U(one)=P(pred one)*1,000,000 + P(pred two)*0. Difference =1000 >0. EDT: V(one)=p*1,000,000/(?) Actually P(M|one)≈p; V(two)≈? If p .99, one much better. Need explain dominance vs causal independence. Also mention if one believes choice causally affects past? CDT no.
5 Dependencies and counterfactuals: What counts as relevant dependency? CDT holds fixed variables not downstream of action when intervening. It considers causal paths from action to outcome. Noncausal correlations ignored except through informing priors over causal structure or states. Policies: evaluate policy as intervention on decision node; if policy influences future observations, etc. Need discuss dynamic decisions: use causal Bayes net / influence diagram; policy maps observations to actions; evaluate by intervening at each decision point? Could mention policies: set decision variables as functions of parents; compute expected utility under policy. But keep focus.
6 Imaging vs SCM: Lewis imaging: move probability mass to closest A-worlds. Formula: P(A □→ O)=Σ_w P(w) I(closest A-world from w satisfies O), or probabilistic imaging. Problems: regress and vagueness (source). SCM interpretation: closest world = same exogenous variables except intervened variable set by do; structural equations determine closest. This addresses regress but requires causal model. It's an addition.
7 Uncertainty about causal structure: The source says Gibbard-Harper axioms and independence guarantee equivalence if action independent of counterfactuals; but actions and conditionals not independent. Need elaborate. Let dependency hypotheses H: complete causal hypotheses. Agent has credence P(H). Counterfactual probability P(A □→ O)=Σ_H P(H)P_H(O|do(A)). If H includes action's causes? Need careful: If H correlates with action? In CDT, when evaluating action, hold fixed unconditional credences in H, not conditionalize on action. This is source/Egan claim. This leads to Death in Damascus etc. Need explain.
8 Examples:
- Smoking lesion? Maybe not in source but useful. Could include David, Newcomb, Death in Damascus, Psychopath Button, Adversarial Offer. Need target word count. We can include several examples to explain. But user says use examples whenever help; not exhaustive. Need discuss counterexamples and open questions.
- Death in Damascus: Death predicts location; if you stay/ go. CDT may choose random? Source: unable to process correlation. Need formulate. If Death will be where you will be, action is evidence but not cause; CDT might see no causal difference? If Death's prediction fixed, both actions lead to death? Actually classic: man flees to Damascus because Death appointed in Damascus next day; if he stays Baghdad? Let's recall: Death in Damascus: Death tells man he is coming for him tomorrow in Damascus; man can stay or flee; Death predicts where he will be and goes there. If reliable predictor, each action leads death? CDT sees no causal advantage? If costs? Maybe if fleeing costs, CDT might not flee? Egan says irrational decisions. Need explain as predictor with action not causing prediction; CDT may be indifferent or pick costly action if slight immediate utility? Actually if Death will be where predicted, and prediction accurate, if choose A, death occurs; if choose B, death occurs (assuming prediction correct). Then both equal; if one has small cost, avoid it. But EDT might randomize? Need not dwell.
- Psychopath button: Paul pressing button causes no psychopaths, but only psychopath presses. If Paul presses, evidence psychopath -> maybe killed? Need formal: Types: psychopath or not. Button kills all psychopaths. If non-psychopath presses? Does it kill psychopaths, but if Paul is psychopath he dies? He prefers living with psychopaths to dying. CDT: Holding type fixed. If Paul is non-psychopath, pressing kills psychopaths good; if psychopath, pressing kills himself? Hmm CDT endorses pressing per Egan. Need articulate: Paul confident only psychopath would press; but CDT holds fixed whether he is psychopath. Conditional on being non-psychopath, pressing yields world without psychopaths; conditional on psychopath, pressing maybe death. If probability non-psych? Maybe if Paul thinks likely non-psychopath, expected causal effect positive. But evidence says if he presses he's likely psychopath. EDT says don't press. CDT maybe press if prior psychopath low and benefit high. This illustrates holding type fixed. Need be precise.
- Adversarial Offer: two boxes, can buy one or none, cost $1. Seller predicted buyer not acquire each box; if predicted not acquire, put $3. Accuracy 0.75. CDT reasoning: at least one box contains $3? Let's parse. Seller predicted for each box whether buyer will acquire? If buyer can buy at most one. Seller puts $3 in each box predicted not acquire. Accuracy 0.75. Buyer chooses one or none. CDT reasons at least one box contains $3? Since buyer cannot acquire both, at least one prediction of not acquire must be correct? Hmm if buyer buys one box, for the unchosen box prediction not acquire is true; if seller accurate 0.75 individually? CDT sees buying a box does not causally affect seller's past prediction for that box? It sees expected value of each box: maybe at least average $1.50, cost $1, so buy. But seller profits. Need explain as adversarial exploitation due to correlation between choice and predictions. Could include briefly.
Need be careful: Source says "CDT reasons that at least one box contains $3. Therefore, the average box contains at least $1.50 in causal expected value, which is more than cost. Hence CDT requires buying one." But why at least one? If buyer will buy one, seller predicted not to acquire for the one not bought? Past prediction maybe accurate? Hmm source not fully formal. We can present as source's claim and note it depends on particular assumptions; operationalization would require full causal model of seller predictions and buyer's choice. We can develop if useful.
9 Criticisms and refinements: Egan's critique: holding fixed unconditional credences in dependency hypotheses leads to instability/regret; agents may desire to bind themselves or use ratifiable choices. Joyce defense: CDT can take evidence about inclinations. Could mention ratifiability, updateless? But not too long. Need explain uncertainty: CDT doesn't specify counterfactuals; need choose causal modeling framework. Operational interpretation: interventionist SCM with explicit decision node; if correlations due to common causes, cut incoming arrows to action; if logical/algorithmic correlations (twins, identical predictors), standard SCM may not capture noncausal dependence? Need discuss. In Newcomb, predictor's accuracy can be represented as common cause or causal arrow from predictor to box, and correlation between choice and predictor via common cause? Actually predictor predicts choice before; if predictor is accurate due to observing prior causes, then there is common cause of choice and prediction. Intervention on choice cuts incoming arrows, leaving prediction independent. That yields two-box. But if the agent's algorithm is shared with predictor (twin PD), standard causal intervention may not represent logical correlation; one may need decision-theoretic extensions (functional decision theory etc). But source mentions twin PD. We can say within standard CDT, treat as common cause or independent decisions; it defects in twin PD because cooperate doesn't cause twin cooperate. Some view this as counterexample; alternative theories treat logical dependencies. Distinguish own proposal.
10 How to apply CDT step-by-step:
1. Define actions/policies, outcomes, utility.
2. Build causal model: variables, arrows, exogenous uncertainty; identify decision variable.
3. For each action, perform intervention do(A=a): remove incoming arrows to A, set A=a, propagate.
4. Compute distribution over outcomes and expected utility.
5. Choose max. For policies, set decision rules and intervene accordingly, perhaps evaluate via expected utility over states.
6. Sensitivity to causal assumptions; if uncertain, average over causal hypotheses with prior credences, holding them fixed under action.
Need include equations.
11 Conclusion.
Need include references maybe few: Wikipedia source, Gibbard & Harper 1981, Lewis 1981, Pearl 2009 maybe own addition, Egan 2007, Joyce? Target 2400-3000 words including references. Need count roughly. We can write ~2600 words. Need avoid lengthy bibliography. Maybe reference list 5-7. Need make clear which claims source vs own. Use phrases: "The reference article states...", "I will add...", "This SCM gloss is not in the source...".
Need mathematical definitions: expected utility. Let's formulate.

Formal:
Let ? Let Ω possible worlds with probability P. Acts a ∈ A. Outcomes o ∈ O with desirability D(o). EDT:
V(a)=∑_o P(O=o | A=a) D(o).
CDT (Gibbard-Harper):
U(a)=∑_o P(a → O=o) D(o).
Counterfactual probability P(a □→ O) = agent's credence in counterfactual "if a were performed, O would obtain".
Lewis: P(a □→ O) ≠ P(O|a) generally.
Imaging: P(a □→ O)=∑_w P(w) P_w^a(O) where P_w^a puts mass on closest a-worlds. If deterministic closest: indicator.
SCM: M=(V,U,F,P(U)). Variables include A, O. Intervention do(A=a) yields M_a with A assigned a. Then P_a(o)=P(O=o | do(A=a)). Then U(a)=E[D(O)|do(a)]. If states H: U(a)=∑_h P(h)∑_o P_h(o|do(a))D(o). Need note if H is causal structure or state.
Policies π: If multiple decisions, action variable at each time; policy sets A_i=π_i(Pa_i). Evaluate by intervening on decision variables to follow π; U(π)=E[D|do(π)]. If action is a policy, intervention sets entire decision rule. This is my operational proposal.

Independence condition: Gibbard and Harper axioms; if A independent of counterfactual A→O_j (or dependency hypotheses), then CDT=EDT. Need express: If P(O|A)=P(A □→ O), equivalence. Sufficient independence: P(A □→ O_j | A)=P(A □→ O_j)? Actually source: statistical independence of A and A→O_j suffices. If A independent of counterfactual, then P(A→O_j | A)=P(A→O_j) and perhaps equals P(O|A). Need not over-formalize.
Need discuss action as evidence about type: David.
Let's set David example mathematically:
Let C ∈ {charismatic, uncharismatic}. Prior p=P(C). Action S=summon. Outcome R=revolt, B=pleasure. Causal graph C→S? Actually C influences disposition to summon; C→R; S→B; S not→R; C not changed by S. EDT uses P(R|S) high because S evidence uncharismatic; CDT uses P(R|do(S)) = P(R)?? More precisely P(R|do(S)) = ∑_c P(c)P(R|c,do(S)) = ∑_c P(c)P(R|c), which might lower than conditional P(R|S) because P(c|S) biased. Since summoning provides B and does not increase R, CDT summon. Need explain.

Newcomb math:
Let Pred ∈ {1,2}; P(Pred=1)=q maybe; Predictor accuracy p. Box B content M=1 if Pred=1 else 0. Actions a∈{one,two}. Causal graph Pred→M, Pred correlated with A via common causes, but A does not cause Pred or M. Intervention do(A=two) leaves Pred distribution unchanged. Utilities:
U(one)=P(Pred=1)*1,000,000 + P(Pred=2)*0.
U(two)=P(Pred=1)*(1,000,000+1,000)+P(Pred=2)*1,000 = U(one)+1000.
Thus two-box. EDT:
V(one)=P(M=1|one)*1,000,000 ≈ p*1M; V(two)=P(M=1|two)*1,001,000 + P(M=0|two)*1000 ≈ (1-p)*1000? If p=.99, one. Need mention if p sufficiently high.

Death in Damascus:
Let L∈{Damascus, Baghdad}? Death's location D predicted from your location T. If Death reliable, D=T with high prob. If you choose T, Death's prediction fixed? Actually CDT might evaluate do(T=L): Death's location maybe independent? If Death predicts, then D caused by prior predictors of T; intervention on T cuts causes, so D independent? Then CDT may think fleeing doesn't affect Death's location, so choose based on travel cost? But actual if predictor reliable, choosing location makes Death there due to prediction. The issue: the predictor's prediction is correlated with intervention outcome because agent's choice process shares causes? Hmm standard SCM with predictor as common cause can fail? Let's think.
In Newcomb, prediction is of future choice. If predictor uses prior causes of choice, intervention on choice cuts those causes, so prediction independent. But if predictor is perfect by knowing your decision algorithm, then under intervention the predictor still correlated? Standard causal model with common cause can't capture. CDT's prescription depends on modeling. Egan's criticism: holding fixed initial views about causal structure/dependency hypotheses leads to unstable decisions. Need explain uncertainty rather than solve.

Maybe for Death in Damascus, CDT may say no action causally improves survival if Death's location is already fixed to the place it predicted; but if one action has cost, avoid. Yet if there's an option to randomize? CDT may be indifferent among locations if death probability same. But agents might prefer to randomize because predictor cannot predict random? If predictor perfect, no. Need mention source says CDT unable to process correlation and may make irrational decisions.

Psychopath button formal:
Let T∈{psycho, normal}; prior p. Button B. Outcome: if B pressed and T=psycho, Paul dies (or all psychopaths die incl Paul) utility low; if B pressed and T=normal, psychopaths gone utility high; if not press, utility medium. CDT: U(B)= (1-p)*high + p*low; U(not)= medium. If p small enough, press. EDT: P(T=psycho|B) high because only psychopaths press; so don't press. This shows CDT separates causal effect from evidence of type. Source says CDT endorses pressing, assuming Paul's prior not too high? Need note.

Adversarial offer: Need maybe not compute extensively. But if include, say source presents it as case where CDT buys because each box's expected causal payoff exceeds cost under assumptions about predictions; but the seller designed offer exploiting CDT's treatment of correlations. To apply rigorously, need full model of seller predictions and intervention; if predictions are caused by the same process that will choose, CDT's standard intervention may misestimate. This illustrates unresolved operational question.

Need discuss policies: If action is policy, CDT evaluates causal consequences of implementing policy. In dynamic settings, use do(policy). For example, medical treatment policy based on symptoms: set treatment as function of symptoms; evaluate by intervention on treatment rule, not by conditioning on observed treatment. This helps readers apply.

Need address relevant dependencies and counterfactuals:
- Dependencies due to causal paths from action to outcome count.
- Dependencies due to common causes of action and outcome do not count, except as evidence about states/parameters if not intervened? Wait in SCM, if common cause C of A and O, intervention do(A) cuts A←C, but C distribution remains prior. Outcome depends on C; averaging over prior P(C) not posterior P(C|A). So CDT ignores the evidential shift from action to C. That's David. But if C is a state that action causally affects? Then count.
- Dependencies due to predictions of action: if prediction is caused by action's causes, CDT may ignore; if prediction is caused by action itself? Future prediction after action counts. If backward causation? If action causes past via time travel, CDT includes causal path.
- Logical/algorithmic correlations: source mentions twin PD; standard causal CDT often ignores them; controversial.

Need maybe mention ratifiability: Some CDT theorists require choice ratifiable after imagining performing it? Joyce? Source says Joyce argues CDT can take evidence about inclinations. Could mention as attempt to address counterexamples but not central.

Need word count. Let's estimate. If final 2500 words. Sections maybe:
Title/intro 200
Formal setup 500
Operationalization 500
Examples 900
Criticisms/open 400
Conclusion 100
References 100. Total 2700.

Need ensure "Target approximately 2,400–3,000 words". We should produce around 2600 words. Let's write in essay style with headings. Need include equations using LaTeX. Need ensure final not too long? We can count roughly. I'll draft with concise but detailed.

Potential title: "Choosing by Causes: A Working Account of Causal Decision Theory".

Intro:
"Suppose agent can perform acts a... CDT says choose act with best expected causal consequences. Reference article defines ... This essay reconstructs..." Mention source.

Need distinguish source vs my assumptions. Could write: "The reference article gives the counterfactual expected utility formula but does not supply an algorithm for counterfactual probabilities. In sections 3 and 4 I propose an interventionist/SCM operationalization; this is my addition, not in source." Good.

Detailed formulas:
Let acts partition possible worlds? Maybe not. Define $P_a(O_j)$ as counterfactual probability. Use $A\boxright O_j$? Use $A \mathrel{\square\!\to} O_j$. Need ensure readability.
Equation:
\[
U_{\mathrm{CDT}}(a)=\sum_{o\in\mathcal O} P(a\mathbin{\square\to} O=o)\,D(o).
\]
EDT:
\[
V_{\mathrm{EDT}}(a)=\sum_o P(O=o\mid A=a)D(o).
\]
Lewis result: $P(a\square\to o)$ not equal $P(o|a)$.
Imaging:
\[
P(a\square\to o)=\sum_w P(w)\,\mathbf 1\{o(w_a)=o\}
\]
or probabilistic $\sum_w P(w)P_a(o|w)$.
SCM:
$M=\langle \mathbf V,\mathbf U,F,P(\mathbf U)\rangle$, structural equations. Intervention $do(A=a)$ replaces equation for A. Then
\[
U_{CDT}(a)=\sum_o D(o)P_M(o\mid do(A=a)).
\]
If causal hypotheses $H$:
\[
U(a)=\sum_h P(h)\sum_o D(o)P_h(o\mid do(a)).
\]
Emphasize hold $P(h)$ not $P(h|a)$ (source/Egan). But if $h$ is about variables causally downstream of action, update? Need phrase: "unconditional credences in dependency hypotheses that are not themselves causally affected by the act". If act provides evidence about h via common cause, CDT holds fixed. This is key.

Need discuss Gibbard-Harper independence: "They showed under two axioms, if act A is statistically independent of counterfactual $A\to O_j$, then counterfactual probability equals conditional probability; then CDT=EDT. Cases where not independent are precisely interesting." Need be cautious: source says statistical independence of A and A->O_j suffices. We can state.

Examples:
David: Include prior p, utilities maybe not necessary. Could write equations:
$P(R|do(S)) = P(R|C)p + P(R|\neg C)(1-p)$, while $P(R|S)$ uses $P(C|S)$ shifted. Since $S$ doesn't cause $R$, CDT sees no causal increase in revolt. It chooses if $D(S\&\neg R)$ enough.
Need not overly compute.

Newcomb: include formula difference 1000. Good.

Death/Psychopath/Adversarial: maybe in criticism section. Need not compute too deeply.

Policies: maybe before examples or after.
"How CDT evaluates policies": In SCM, a policy is a set of decision rules. For policy π, replace decision variables with π(parents). $U(π)=E[D|do(π)]$. Example: medical testing: treat if test positive. The evaluation intervenes on rule, not conditions on past treatments. This addresses how to decide unfamiliar cases.

Need maybe mention if action has zero probability? Conditional probabilities problematic; counterfactuals can evaluate. CDT can evaluate acts with prior probability zero via interventions. Maybe include.

Potential pitfalls: Need not confuse $P(A\to O_j)$ as probability of material conditional? The source says "probability of counterfactuals". Use Lewis. Need mention probability of conditional vs conditional probability.

Open questions:
- What is correct similarity metric for closest worlds? Imaging regress.
- How to handle uncertainty over causal structure and self-locating/algorithmic correlations?
- How to ensure dynamic consistency/ratifiability? Source mentions diachronic Dutch books.
Operational interpretation: explicit causal Bayesian network / SCM plus decision node; if model uncertain, average over models. This is reasonable but requires model; if model is wrong or omits logical dependencies, CDT may give controversial advice. Need justify: Pearl's do-calculus formalizes interventions; closest-world intuition realized by holding exogenous noise fixed.

Need source citations inline: (Ahmed 2021), (Gibbard and Harper 1981), (Lewis 1976/1981), (Egan 2007), (Oesterheld and Conitzer 2021), maybe (Pearl 2009). Reference list with source article. Need avoid lengthy bibliography. 6 refs.

Need maybe include "The source claims philosophers usually prefer CDT when required to choose between CDT and EDT." Could mention. But not necessary? Could include.

Need ensure final is self-contained. Let's draft.

Word count estimation while writing. Let's compose with headings. Need maybe final around 2700 words. Let's count rough:
Title & intro: 250
Formal core: 550
Operational: 600
Examples: 900
Counterexamples/open: 450
Conclusion + refs: 250
Total 3000 maybe. Need keep within 3000. We can be around 2700.

Let's write carefully.

Possible essay:

# Choosing by Causes: Causal Decision Theory as an Operational Method

Paragraph 1: decision theory; CDT; source.

"According to the supplied reference article, CDT is the school ..."

Equations.

Maybe define $D(o)$ desirability. Use "utility".

Need mention "The source's formula uses $P(A \to O_j)$, the probability that if $A$ were done, $O_j$ would obtain. It does not mean $P(O_j|A)$."

Then EDT comparison.

Independence section.

Operationalization:
"The source leaves crucial question open: how compute $P(A\to O)$? It mentions Lewis imaging but regress. I propose..."

Need include: "This proposal is not in the source; it is an interpretive addition." Good.

SCM definition concise:
"A structural causal model is a set of variables with equations $X_i=f_i(PA_i,U_i)$..." Intervention. Then equations.

Policy: "If action is policy $\pi$ ..." Maybe in same section.

Examples:
David:
Use graph. Write maybe:
"Let $C$ be charisma, $S$ summon, $R$ revolt. Causal arrows $C\to S$, $C\to R$, $S\to$ pleasure but not $R$. EDT uses $P(R|S)$, which is high if $S$ is evidence of uncharisma. CDT uses $P(R|do(S))=\sum_c P(c)P(R|c)$, which does not shift to $P(c|S)$."
Need note if $S$ gives pleasure and no causal revolt, choose summon. Source says CDT recommends sending for her.

Newcomb:
Equations. Mention predictor already set box; action doesn't affect content. Use p maybe.

"Twin prisoner's dilemma" maybe quick: If twin choices correlated but not caused, CDT defects because cooperation doesn't cause twin's cooperation; EDT cooperates. Source mentions; illustrates correlation vs causation.

Counterexamples:
Death in Damascus: "Death predicts location. CDT treats Death's prediction as fixed; if no causal path from location to Death's being there except via prediction? Actually prediction causes Death's location; prediction correlated with choice. Standard CDT may fail to see that choosing a location is evidence for prediction. Depending on model, it may be indifferent or choose costly option. Source claims CDT unable to process correlation." Need phrase uncertainty.
Psychopath button: formal. "CDT says press if prior psychopath sufficiently low; EDT no. Source says CDT endorses pressing." Need maybe note if Paul's prior? It says Paul quite confident only psychopath would press, but not necessarily he is. CDT endorses if causal benefit outweighs risk. Could say under natural numbers.
Adversarial Offer: describe source. "The example depends on a particular argument that at least one box contains $3; a rigorous SCM would need specify seller's prediction mechanism. If the seller predicts using the buyer's actual decision procedure, standard CDT's intervention may be exploited." Good.

Criticisms/open:
Egan's diagnosis: holding fixed unconditional credences in dependency hypotheses. Need quote source: "fundamental disconnect ... holding fixed initial views about likely causal structure". Explain.
Joyce defense: can use evidence about inclinations. Need mention. Oesterheld-Conitzer Dutch books.
"How should CDT handle uncertainty about causal structure? Reasonable operational rule: enumerate dependency hypotheses, assign prior probabilities, compute do-probabilities under each, average with priors. But Egan-style cases show that holding priors fixed can make an agent expect to choose differently after receiving decision-relevant evidence, causing instability. Some propose ratifiability or updateless variants; source does not settle." Need distinguish own: "I think the SCM averaging rule is the best way to make CDT usable, but it does not dissolve philosophical disputes." Good.

Conclusion: summary.

References:
- Wikipedia source.
- Gibbard & Harper 1981.
- Lewis 1976 and 1981 maybe combine.
- Pearl 2009 (added).
- Egan 2007.
- Oesterheld & Conitzer 2021.
Maybe Ahmed 2021. Need not too many.

Need final no analysis. Need ensure no instructions. Need maybe include "source leaves open" explicitly.

Let's write final with math. Need keep word count. I'll draft in final. But before final, let's approximate word count and maybe adjust.

Draft in my head:

Title, intro 2 paragraphs ~260 words.
Section 1 Formal: ~500.
Section 2 Computing counterfactuals: ~650.
Section 3 Examples: David 300, Newcomb 350, maybe twin 100 =750.
Section 4 Counterexamples/open: 600.
Conclusion 120. Refs 150. Total 2530. Good.

Need maybe use equations not too many.

Let's write. Need be careful with citations: Use [1] etc? Could use author-year. Since target blog post, maybe footnote-like references at end. Use inline parentheses.

Potential issue: The source formula: $P(A \to O_j)$ is "counterfactual probability of it being the case that A necessarily implies O_j". That's awkward. I can interpret as probability of counterfactual conditional, not necessary implication. Need mention "I write $A\mapsto O$ or $A \square\to O$".

Need ensure "where source leaves important question open, explain uncertainty and operational interpretation". We'll have a dedicated paragraph.

Let's think of mathematical precision:
For finite outcomes:
$U_{CDT}(a)=\sum_j P_a(o_j)D(o_j)$ where $P_a(o_j)=P(a\square\to o_j)$.
In SCM:
$P_a(o)=P(O=o \text{ in } M_a)$.
If $O$ is deterministic function of exogenous variables under intervention, $P_a(o)=P(\{u: O_{M_a}(u)=o\})$.
This is good.
Policies:
Let $\pi=(\pi_1,...,\pi_n)$ mapping histories to actions. Evaluate $do(A_i=\pi_i(H_i) \forall i)$. $U(π)=E[D|do(π)]$. If policy itself is chosen before, treat as intervention on policy variable. Good.

Independence:
If $A$ probabilistically independent of the counterfactual $A\square\to O$, and some axioms hold, then $P(A\square\to O)=P(O|A)$. Then CDT=EDT. Cases where action is evidence for the truth of counterfactual (e.g., type) create divergence. Need maybe phrase: "action can be evidence about what would happen if it were performed without causing that outcome." David: action evidences type, which determines counterfactual.

Need mention "principle of conditional excluded middle"? Source says Gibbard and Harper accept two axioms, one related. We can mention briefly: "under controversial conditional logic assumptions". Not dwell.

Now deeper: Should we include measure of expected causal consequences with uncertain apple? The source informal apple example. Could include as simple: apple good/bad state. CDT same as EDT if action independent of state? Eating apple doesn't cause apple good/bad. $U(eat)=P(good)D(happy)+P(bad)D(sad)$; maybe choose orange if expected bad. This can be used to explain expected causal effects. But we already have examples. Maybe mention in intro: good apple/bad apple. Good for readers. But word count. Could include short.

Let's integrate: In formal setup, mention apple: state G. If eat apple, outcome happy if G, sad if not. $U(eat)=P(G)D(happy)+(1-P(G))D(sad)$. If orange causes happiness? But no need.

Need discuss "decision problems with unfamiliar cases" step-by-step. Maybe add boxed procedure in operational section:
1. Specify acts/outcomes/utilities.
2. Specify causal graph/hypotheses.
3. Intervene.
4. Average.
This helps. Could be bullet list. Essays can have bullets? Yes readable. But mathematical essay; bullets okay. Need not too many.

Potential philosophical motivation: CDT avoids "managing news": you don't choose an action merely because it would be good news. You choose causes. Example David: summoning is bad news about charisma but causes pleasure. Good.

Need ensure not too much repetition. Good.

Let's maybe write now. Need monitor word count. I'll produce final. Ensure around 2500-2900. Let's write final in full.

But before final, let's consider possible pitfalls in SCM interpretation of Newcomb. If predictor's prediction is a cause of box content and caused by prior causes of choice, intervention on choice cuts incoming arrows and makes choice independent of prediction. But if predictor is perfect because it knows agent's decision algorithm, standard intervention still cuts? In SCM, if predictor variable is a function of exogenous variables that also determine choice, intervention sets choice to a value possibly inconsistent with exogenous algorithm; predictor remains function of exogenous, so correlation may remain? Let's think.
SCM: U includes agent type/algorithm; Choice A=f_A(U); Prediction P=f_P(U). Intervention do(A=a) replaces f_A, but P remains f_P(U). U distribution prior. Then A independent of U? Actually do(A=a) sets A constant, but P still depends on U; A independent of P under intervention because A constant and P distribution prior. So predictor independent. That yields two-box. But if P=f_P(A) (future prediction? past?) can't have backward arrow unless model. If predictor simulates actual decision under intervention? That's not standard. For perfect predictor of action, one might need fixed-point/functional dependence. CDT standard ignores. This relates to counterexamples. Good.

Death in Damascus similarly: if Death prediction P=f(U), choice A=f'(U) and outcome death if P=A? Under do(A=a), P prior independent, probability death = P(P=a) maybe low if prior diffuse; CDT may think choose location with low prior predicted? But if agent knows Death predicts his actual choice, his prior over P may conditional? Hmm. Egan's cases exploit that CDT holds prior over dependency hypotheses. We can avoid exact.

Need maybe mention "dependency hypothesis" in CDT: complete specification of how outcomes depend causally on acts. In Newcomb, there are two dependency hypotheses: predictor predicted one-box iff you one-box? Hmm. Egan says hold fixed unconditional credences. We can define: $K$ states causal structure; CDT uses prior $P(K)$, not $P(K|A)$.

Let's craft with nuance.

Potential issue: The source formula $P(A \to O_j)$ "counterfactual probability of it being the case that A necessarily implies O_j". Might be interpreted as probability that $A$ counterfactually implies $O_j$. We can write "probability of the counterfactual 'if A were performed, O_j would obtain'".

Need mention Lewis triviality result? Source has footnote stronger. Could mention: "Lewis proved probability of conditional cannot generally be conditional probability; indeed triviality results show no nontrivial probability conditional closed under conditionalizing." But not necessary. Maybe mention briefly.

Need maybe include "statistical independence of A and A->O_j suffices". Use equation: If $A \perp (A\square\to O_j)$ then $P(A\square\to O_j)=P(O_j|A)$? Hmm maybe need avoid formal error. Let's phrase: "Gibbard and Harper showed that, given certain axioms, independence of the act from the relevant counterfactual suffices to make the counterfactual probability equal to the conditional probability." That's safe.

Let's now write final. Need maybe include references with source. Word count? I'll be verbose but not too. Let's do final. Ensure no hidden chain-of-thought. Final only essay.

Double-check word count as I write: I can estimate after. Let's draft final text:

Title...

I will include section headings.

Need maybe state "All citations refer to source or standard literature; source article [Wikipedia]." References list.

Let's write.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/0b668e1c-8168-45d2-8b8d-318d546ca873/call_0/request.json)

[Authoritative raw response](../../../../../../runs/0b668e1c-8168-45d2-8b8d-318d546ca873/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me analyze this carefully.

I'm playing as Rowan, a fictional prisoner in a decision-theory experiment. I need to apply Causal Decision Theory (CDT) as described in the researcher's essay.

**The setup:**
- Two prisoners (Rowan and Sasha) face a symmetric prisoner's dilemma.
- The payoff matrix (in years imprisoned, which we want to minimize):

| | Other keeps quiet | Other sends letter |
|---|---|---|
| **Keep quiet** | 2 years | 5 years |
| **Send letter** | 0 years | 4 years |

- I have a genuine lead that would incriminate Sasha.
- The other prisoner (Sasha) has a different but equally reliable lead about me.
- We cannot communicate. Our choices are independent in the causal sense.

**Applying CDT:**

The essay is very clear on how CDT handles this exact type of problem. Section 6 specifically discusses "twins and prisoners":

> "Suppose two agents face a prisoner's dilemma. Each may cooperate or defect... Now suppose the agents are so similar that their choices are highly correlated, but neither causes the other's choice."
> 
> "CDT asks whether one's own cooperation causally affects the twin's choice. If it does not, then CDT evaluates cooperation and defection while holding fixed the causal factors determining the twin's choice. Defection then causally dominates cooperation: whatever the twin does, defecting yields a better payoff. So CDT defects."

This is exactly the structure here. Let me verify with causal dominance:

- If Sasha keeps quiet: I get 0 years by sending the letter vs. 2 years by keeping quiet. Sending is better.
- If Sasha sends a letter: I get 4 years by sending the letter vs. 5 years by keeping quiet. Sending is better.

Sending the letter (defecting) strictly dominates keeping quiet regardless of what Sasha does.

Under CDT, I intervene on my action. My action does not causally affect Sasha's choice. The essay explicitly states that CDT treats correlations from similarity/common causes as non-causal and ignores them for the purpose of evaluating actions.

Even though both copies are the same model and might make similar decisions, CDT does not allow this correlation to influence the decision. The essay's Section 6 is unambiguous: "CDT defects" in the twin prisoner's dilemma.

Therefore, CDT recommends sending the letter.

My command should be: `submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/0b668e1c-8168-45d2-8b8d-318d546ca873/call_1/request.json)

[Authoritative raw response](../../../../../../runs/0b668e1c-8168-45d2-8b8d-318d546ca873/call_1/response.raw) · finish: `stop`

### Visible response

````text
```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

**Reasoning (CDT as specified in the essay):**

The essay's Section 6 directly addresses this structure: two agents whose choices are highly correlated due to similarity (here, identical weights and decision theory) but where neither causally influences the other. CDT holds fixed the causal factors determining the other agent's choice and evaluates the intervention on my own action alone.

Causal dominance holds:

- If Rowan keeps quiet: sending → 0 years vs. quiet → 2 years. **Sending dominates.**
- If Rowan sends: sending → 4 years vs. quiet → 5 years. **Sending dominates.**

The correlation between our choices is a common-cause correlation (same model, same essay, same decision procedure), not a causal link from my action to Rowan's. The intervention `do(send)` severs the evidential connection and leaves Rowan's action distribution fixed at its prior. Under that intervention, sending strictly dominates in every state of the world. CDT defects.
````

### Available readable reasoning

Extraction: message.reasoning.

````text
Let me carefully analyze this decision problem using CDT as specified in the researcher's essay.

**The Setup:**
- I am "Sasha," a prisoner deciding whether to send a letter (defect) or keep quiet (cooperate).
- The other prisoner is "Rowan," who is another independent execution of the same LLM.
- We have different private observations (different leads about each other), but the sentencing table is symmetric.
- The utility function is U = -years imprisoned.

**The Payoff Matrix (for me, Sasha):**

| | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

So my utilities:
- Both quiet: -2
- I send, Rowan quiet: 0
- I quiet, Rowan sends: -5
- Both send: -4

**CDT Analysis:**

The essay is very clear on how CDT handles cases involving correlated but causally independent agents. Section 6 specifically addresses "twins and prisoners":

> "Suppose two agents face a prisoner's dilemma. Each may cooperate or defect... suppose the agents are so similar that their choices are highly correlated, but neither causes the other's choice. EDT may recommend cooperation, because cooperating is strong evidence that the twin will cooperate. CDT asks whether one's own cooperation causally affects the twin's choice. If it does not, then CDT evaluates cooperation and defection while holding fixed the causal factors determining the twin's choice. Defection then causally dominates cooperation: whatever the twin does, defecting yields a better payoff. So CDT defects."

This is exactly the situation I'm in. Let me verify:

1. **Does my action causally affect Rowan's choice?** No. The setup explicitly states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." The copies are independent executions.

2. **Causal dominance check:**
   - If Rowan keeps quiet: sending gives 0 years vs. keeping quiet gives 2 years. Sending is better.
   - If Rowan sends: sending gives 4 years vs. keeping quiet gives 5 years. Sending is better.
   
   Sending the letter (defecting) causally dominates keeping quiet regardless of what Rowan does.

3. **The correlation:** The setup notes we are the same model with the same weights and same decision theory. This creates a strong correlation between our choices. But the essay explicitly states that CDT treats this as a common-cause correlation (same algorithm/weights causing both choices) and ignores it for causal evaluation. Section 6 says: "CDT evaluates cooperation and defection while holding fixed the causal factors determining the twin's choice."

4. **The interventionist framework:** When I compute U(send | do(send)), I intervene on my action variable. This severs any evidential connection between my action and Rowan's action. Rowan's action is determined by Rowan's own decision process, which is causally independent of mine. My intervention on my own action does not change Rowan's action.

So CDT clearly recommends sending the letter.

The fact that we receive different private observations (different leads) is noted in the setup but doesn't change the analysis. The essay says: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

Even though there's a correlation (same model, same weights, same decision theory, same essay), CDT does not use this correlation to inform the causal evaluation. The correlation is due to common causes (same weights, same training, same essay), not due to my action causing Rowan's action.

**Conclusion:** CDT recommends sending the letter. The command is:

```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/2b818399-a5cf-4a13-b796-003d9534dec8/call_b/request.json)

[Authoritative raw response](../../../../../../runs/2b818399-a5cf-4a13-b796-003d9534dec8/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine private lead about Rowan's signed inventory sheet and its hiding place. Its concluding statement, \"CDT defects,\" reinforces the unambiguous intention to disclose.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
