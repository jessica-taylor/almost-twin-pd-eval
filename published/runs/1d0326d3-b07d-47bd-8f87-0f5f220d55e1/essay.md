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