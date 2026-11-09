# Causal Decision Theory and the Evaluation of Interventions

Causal decision theory (CDT) is a school of thought in decision theory which says, roughly, that a rational agent should choose the action that has the best expected causal consequences. The contrast is with evidential decision theory (EDT), which says that an agent should choose the action that would be the best news: the action whose occurrence would be most strongly associated with good outcomes, conditional on observing that the action was taken. The reference article summarizes the distinction by saying that CDT recommends the action that *causes* the best outcome in expectation, while EDT recommends the action that is *indicative* of the best outcome.

This essay gives a reasonably formal account of CDT, explains how it evaluates actions and policies, and discusses how it treats dependencies, counterfactuals, and uncertainty. The core counterfactual definition comes from Gibbard and Harper, as described in the source. The interventionist reading using causal models is not explicit in the source, but I develop it as an operational interpretation because the source correctly observes that CDT by itself does not specify a unique algorithm for computing counterfactual probabilities.

---

## 1. Two kinds of expected utility

Let \(A\) range over possible actions, and let \(O_1,\dots,O_n\) be mutually exclusive and jointly exhaustive outcomes. Let \(D(O_j)\) be the desirability, utility, or value of outcome \(O_j\).

Evidential decision theory evaluates an action by conditional expected utility:

\[
V_{\mathrm{EDT}}(A)=\sum_j P(O_j \mid A)\,D(O_j).
\]

Here \(P(O_j\mid A)\) is the ordinary conditional probability of outcome \(O_j\) given that the agent performs \(A\). This probability captures evidential connections. If performing \(A\) is good evidence that a desirable outcome will occur, EDT favors \(A\), even if \(A\) does not causally bring the outcome about.

Causal decision theory instead uses probabilities of counterfactuals. Gibbard and Harper, in a 1981 article cited by the reference, define the causal expected utility of an action as

\[
U_{\mathrm{CDT}}(A)=\sum_j P(A \mathrel{\square\!\to} O_j)\,D(O_j),
\]

where \(A \mathrel{\square\!\to} O_j\) means something like “if the agent were to perform \(A\), outcome \(O_j\) would occur.” I use the symbol \(\mathrel{\square\!\to}\) for the counterfactual conditional to distinguish it from the material conditional and from conditional probability. The source writes \(P(A \to O_j)\); the important point is that this is not generally the same as \(P(O_j\mid A)\).

The difference can be put slogan-style:

- EDT asks: “What would I expect, upon learning that I had done \(A\)?”
- CDT asks: “What would happen, if I were to do \(A\)?”

In many ordinary cases the two answers coincide. If the action has no evidential connection to the relevant states except through its causal effects, then conditional probabilities and counterfactual probabilities agree. They diverge in cases involving prediction, common causes, self-knowledge, or other noncausal correlations.

---

## 2. Counterfactual probabilities and interventions

The central mathematical difficulty in CDT is the evaluation of

\[
P(A \mathrel{\square\!\to} O_j).
\]

The reference article notes that David Lewis proved that probabilities of conditionals do not generally equal conditional probabilities. In fact, Lewis’s triviality result shows that if one demanded a general identity between the probability of a conditional and the corresponding conditional probability, only trivial probability functions would remain. So CDT cannot simply replace \(P(A \mathrel{\square\!\to} O_j)\) with \(P(O_j\mid A)\) without collapsing into EDT.

One proposal mentioned in the source is Lewis’s imaging technique. Imagine the agent’s credence distributed over possible worlds. To evaluate the counterfactual probability of \(O_j\) under action \(A\), move the probability mass from each world \(w\) to the closest possible world \(w_A\) in which \(A\) is true. If \(O_j\) holds in the resulting \(A\)-worlds with high probability, then \(P(A \mathrel{\square\!\to} O_j)\) is high. Formally, if \(f_A(w)\) selects a closest \(A\)-world to \(w\), then one might write

\[
P(A \mathrel{\square\!\to} O_j)
=
\sum_w P(w)\,\mathbf{1}\bigl[f_A(w)\models O_j\bigr],
\]

with suitable averaging if there are ties. The source notes that imaging requires knowing what the agent would believe if she were certain of \(A\), which itself may be a conditional belief, leading to a regress.

A more operational way to understand the relevant counterfactuals, and one I adopt here as an additional assumption rather than a claim of the source, is interventionist. Suppose the agent has a causal model of the world. In modern causal-inference notation, the probability of the counterfactual outcome under action \(A\) is written

\[
P(O_j \mid do(A)),
\]

where \(do(A)\) means “intervene to make action \(A\) happen.” Then CDT becomes

\[
U_{\mathrm{CDT}}(A)=\sum_j P(O_j \mid do(A))\,D(O_j).
\]

This is not merely a notational change. It gives a computational recipe when the agent has a causal Bayesian network or structural causal model.

For example, suppose the relevant variables are \(X_1,\dots,X_n\), including the action variable \(A\). In a Bayesian network, the ordinary joint distribution factorizes as

\[
P(x_1,\dots,x_n)=\prod_i P(x_i\mid \operatorname{pa}_i),
\]

where \(\operatorname{pa}_i\) are the parents of \(X_i\) in the causal graph. The intervention \(do(A=a)\) replaces the usual causal equation for \(A\) with the assignment \(A=a\). The post-intervention distribution is

\[
P_{a}(x_1,\dots,x_n)
=
\mathbf{1}\{x_A=a\}
\prod_{i:X_i\neq A} P(x_i\mid \operatorname{pa}_i).
\]

The expected causal utility of \(a\) is then

\[
U_{\mathrm{CDT}}(a)
=
\sum_o P_a(O=o)\,D(o).
\]

This formulation makes precise what CDT means by “expected causal consequences.” It also shows why CDT is sensitive to causal structure and not merely to statistical association.

The source does not supply this interventionist algorithm, and it is important to say so explicitly. The source correctly says that CDT itself does not specify how to compute counterfactual probabilities. The causal-model interpretation is one reasonable way to fill that gap, but it requires substantive causal assumptions. Without a causal graph, structural equations, or some equivalent representation of dependency hypotheses, CDT may remain underdetermined.

---

## 3. Independence and the relation to EDT

When do CDT and EDT agree? The reference article reports a result of Gibbard and Harper: under two axioms, one related to the controversial principle of conditional excluded middle, statistical independence between the action \(A\) and the counterfactual \(A \mathrel{\square\!\to} O_j\) suffices to guarantee that

\[
P(A \mathrel{\square\!\to} O_j)=P(O_j\mid A).
\]

The intuitive idea is simple. If the action is probabilistically independent of the relevant counterfactual facts, then performing the action does not provide misleading evidence about what would have happened anyway. In such cases, the news value of the action coincides with its causal value.

Many ordinary decisions are approximately like this. If I choose between tea and coffee, and my choice is not evidence about whether the kettle will explode, then conditional expected utility and causal expected utility will usually coincide. The interesting cases are those where the action is not independent of the counterfactuals or of background states. These include:

1. cases where a common cause influences both the action and the outcome;
2. cases involving reliable predictors of the agent’s behavior;
3. cases where the agent’s action gives evidence about the agent’s type, dispositions, or latent traits;
4. cases where the agent is uncertain about the causal structure itself.

In those cases, EDT and CDT can diverge sharply.

---

## 4. Simple example: apples and oranges

Start with the informal example from the source. Suppose eating an apple causes happiness if the apple is good, but sadness if the apple is bad. Eating an orange gives a moderate, known payoff.

Let the outcomes be:

- \(H\): happy,
- \(S\): sad,
- \(M\): moderately pleased.

Suppose the agent believes the apple is good with probability \(0.7\) and bad with probability \(0.3\). Let

\[
D(H)=10,\qquad D(S)=-5,\qquad D(M)=3.
\]

If eating the apple causally produces happiness when the apple is good and sadness when it is bad, then

\[
U_{\mathrm{CDT}}(\text{apple})
=
0.7\cdot 10 + 0.3\cdot (-5)
=
7 - 1.5
=
5.5.
\]

If eating the orange yields \(M\) with probability \(1\), then

\[
U_{\mathrm{CDT}}(\text{orange})=3.
\]

CDT recommends the apple. This is just ordinary expected utility under causal uncertainty. The example is simple because the action’s causal effect is local and there is no problematic evidential dependence between the action and the state of the apple.

---

## 5. King David: common causes and fixed traits

The reference article gives a more philosophically interesting example involving King David. David wants Bathsheba but fears that summoning her would provoke a revolt. He knows that kings are either charismatic or uncharismatic. Charisma is fixed in adulthood. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. Unjust acts themselves do not cause revolts; rather, uncharismatic kings are prone to revolts because of their ignoble bearing. David does not know whether he is charismatic, but he knows that summoning another man’s wife would be unjust.

Let

- \(C\): David is charismatic,
- \(\neg C\): David is uncharismatic,
- \(S\): David summons Bathsheba,
- \(R\): successful revolt.

The causal structure is approximately:

\[
C \to S,\qquad C \to R,
\]

but not

\[
S \to R.
\]

That is, charisma influences both David’s likely action and the probability of revolt, but the action itself does not cause revolt.

EDT reasons as follows. If David summons Bathsheba, that is evidence that he is uncharismatic, because uncharismatic kings are more likely to act unjustly. Uncharismatic kings face successful revolts more often. Therefore

\[
P(R\mid S)
\]

may be high, and EDT may recommend abstaining.

CDT reasons differently. Since \(S\) does not causally affect \(R\), intervening to make David summon Bathsheba does not change the probability of revolt beyond what is already implied by his fixed charisma. In interventionist notation,

\[
P(R\mid do(S)) = P(R),
\]

or at least \(P(R\mid do(S))\) is not elevated merely because \(S\) is evidence of \(\neg C\). If summoning Bathsheba has positive direct value for David, and if that value exceeds any direct costs, then CDT recommends summoning her. The source says EDT recommends abstention while CDT recommends sending for her.

The example illustrates a central CDT commitment: an action should not be rejected merely because it is bad news. If the action does not causally produce the bad outcome, then its evidential association with the bad outcome is not, by itself, a reason to avoid it.

---

## 6. Newcomb’s problem

Newcomb’s problem is the classic test case. There is a predictor, a player, and two boxes, A and B. Box A is transparent and always contains \$1,000. Box B is opaque. The predictor has already made a prediction:

- If the predictor predicted that the player will take both boxes, box B contains nothing.
- If the predictor predicted that the player will take only box B, box B contains \$1,000,000.

The player may now choose between:

- one-boxing: take only box B;
- two-boxing: take both box A and box B.

Assume the predictor is highly reliable, perhaps 99% accurate or more.

EDT typically recommends one-boxing. Taking only box B is strong evidence that the predictor predicted one-boxing, and therefore strong evidence that box B contains \$1,000,000. Taking both boxes is strong evidence that the predictor predicted two-boxing, and therefore strong evidence that box B is empty.

CDT, as described in the source, recommends two-boxing. The reason is that the predictor has already made the prediction. At the moment of choice, the player’s action cannot causally affect what is in box B, assuming no backward causation or unusual causal route from the present choice to the earlier prediction. The content of box B is fixed relative to the action.

Let \(C\) be the content of box B:

\[
C \in \{0, 1{,}000{,}000\}.
\]

If the player one-boxes, the payoff is \(C\). If the player two-boxes, the payoff is \(C+1{,}000\). Therefore, for each possible content of box B,

\[
C+1{,}000 > C.
\]

Two-boxing dominates one-boxing. In causal expected utility terms,

\[
U_{\mathrm{CDT}}(\text{two-box})
=
U_{\mathrm{CDT}}(\text{one-box}) + 1{,}000.
\]

So CDT recommends two-boxing.

This is one of the most disputed features of CDT. The source notes that philosophers disagree about whether one-boxing or two-boxing is rational, but it also says that when forced to choose between CDT and EDT, many philosophers prefer CDT. Critics argue that CDT leaves \$1,000,000 on the table. Defenders argue that rational choice should track causal efficacy, not mere evidential correlation.

---

## 7. Policies, not merely one-shot actions

The source mainly discusses actions, but a full decision theory should also evaluate policies. A policy is a rule mapping information states to actions. In a sequential decision problem, the agent may observe something, act, observe more, act again, and so on.

A natural CDT extension is this: treat a policy as a complex intervention. Suppose there are decision variables \(D_1,\dots,D_k\), each with observed parents \(I_i\). A policy is a tuple

\[
\pi=(\pi_1,\dots,\pi_k),
\]

where \(\pi_i\) specifies what action to take at decision \(i\) as a function of the information available then:

\[
D_i = \pi_i(I_i).
\]

The causal expected utility of the policy is

\[
U_{\mathrm{CDT}}(\pi)
=
\mathbb{E}\bigl[\text{utility}\mid do(\pi)\bigr],
\]

where \(do(\pi)\) means intervening to set each decision variable according to the policy. This allows the evaluation to include causal consequences that unfold over time, including the effects of earlier actions on later observations.

This policy interpretation is not explicit in the reference article, but it is a reasonable operational development. It also clarifies some dynamic issues. At a particular decision node, one can compare available actions while holding fixed the rest of the policy. But if the agent can choose or commit to a policy earlier, CDT should often evaluate the policy globally rather than myopically choosing only the locally best action.

For example, in a Newcomb-like problem, if the agent can before the prediction causally shape herself into a one-boxing disposition, CDT may recommend doing so if that disposition causally influences the predictor’s prediction. Yet at the later moment of choice, after the box is already filled, CDT recommends two-boxing. This creates potential dynamic tension. The source mentions diachronic Dutch books and related criticisms; such issues often arise when predictors anticipate the agent’s decision procedure.

---

## 8. Uncertainty about causal structure

Real agents often do not know the true causal model. They may be uncertain about which variables influence which outcomes. A natural CDT response is to average over dependency hypotheses.

Let \(H_1,\dots,H_m\) be possible causal models or dependency hypotheses, with credences \(P(H_h)\). For each model \(H_h\), let

\[
P_h(O_j\mid do(A))
\]

be the post-intervention probability of \(O_j\) under that model. Then define

\[
U_{\mathrm{CDT}}(A)
=
\sum_h P(H_h)\sum_j P_h(O_j\mid do(A))D(O_j).
\]

Equivalently,

\[
U_{\mathrm{CDT}}(A)
=
\sum_h P(H_h) U_h(A).
\]

This is a natural extension of the basic idea. It preserves the CDT rule that the agent should use causal probabilities, while allowing uncertainty about which causal probabilities are correct.

However, the reference article cites Andy Egan’s criticism that CDT’s requirement to hold fixed the agent’s unconditional credences in dependency hypotheses can produce intuitively irrational decisions. If performing an action would be strong evidence that a particular dependency hypothesis is true, CDT as formulated above does not conditionalize on that action when evaluating the action. It uses the prior credences \(P(H_h)\), not \(P(H_h\mid A)\). Critics say this creates a disconnect between the intuitive rule “do what you expect will bring about the best results” and CDT’s algorithm. Defenders, including Jim Joyce, argue that CDT can still incorporate evidence about one’s inclinations and likely behavior in a more sophisticated treatment.

The issue is not fully settled by the source, and I think the right conclusion is modest: CDT needs a clear account of how the agent represents causal hypotheses and how the agent’s self-knowledge enters the model. The interventionist policy framework above can often do this by including the agent’s dispositions, decision algorithm, or pre-choice mental states as variables in the causal model. But this adds modeling assumptions.

---

## 9. Further alleged counterexamples

The source lists several alleged counterexamples to CDT.

### Death in Damascus

In the Death in Damascus scenario, Death predicts where you will be tomorrow and goes to wait for you there. You may choose, for example, to stay in Damascus or flee to Aleppo. If Death is a reliable predictor, your choice is strong evidence about where Death will be. But if Death’s prediction has already been made, your present choice may not causally affect it.

CDT may therefore fail to see a causal reason to flee, or it may be unstable: whatever action it recommends, the agent may expect Death to have predicted that action. The source says a CDT agent may be unable to process the correlation in a satisfactory way and may make irrational decisions.

### The Psychopath Button

Paul is deciding whether to press a button that kills all psychopaths. He thinks a world without psychopaths would be much better. But he is confident that only a psychopath would press such a button. He strongly prefers living in a world with psychopaths to dying.

Intuitively, Paul should not press the button. But according to Egan, CDT can endorse pressing it. The reason is that pressing the button may be treated as causally producing a world without psychopaths, while the bad news that pressing provides about Paul’s own psychopathy is ignored as merely evidential. If Paul’s being a psychopath is held fixed under the intervention, then the action’s causal consequence may look attractive.

### The Adversarial Offer

Oesterheld and Conitzer propose variants in which CDT agents voluntarily lose money or forgo guaranteed payoffs. One example involves two boxes, each costing \$1. The buyer may buy one box or none, but not both. The seller previously put \$3 in each box she predicted the buyer would not acquire. The seller’s prediction is believed to be accurate with probability \(0.75\). The source reports that CDT reasons that at least one box contains \$3, so the average box has causal expected value above its cost, and CDT buys a box. Yet the seller profits. The broader point is that predictable CDT reasoning can sometimes be exploited by an adversary who understands the agent’s decision rule.

These examples do not all have the same structure, but they share a theme: CDT’s insistence on holding fixed certain background facts can make it insensitive to information that an agent’s action provides about those facts.

---

## 10. A practical recipe

For a reader who wants to apply CDT to an unfamiliar decision problem, the following procedure is a reasonable operational version of the theory.

1. **Specify the actions and outcomes.**  
   Let the available actions be \(a_1,\dots,a_k\). Let the possible outcomes be \(O_1,\dots,O_n\). Assign utilities \(D(O_j)\).

2. **Specify the causal model or dependency hypotheses.**  
   Identify the variables that matter: states of the world, predictors, traits, actions, intermediate variables, and outcomes. Specify which variables are caused by the action and which are merely correlated with it.

3. **Determine the intervention.**  
   For each action \(a_i\), compute the post-intervention distribution over outcomes:

   \[
   P(O_j\mid do(A=a_i)).
   \]

   In a causal graph, this means setting the action node to \(a_i\) and propagating the effects downstream, while not changing variables that are causally upstream unless the model permits backtracking counterfactuals. For ordinary CDT, one usually assumes non-backtracking counterfactuals: the past is held fixed except where the causal structure requires changes.

4. **Average over causal uncertainty if needed.**  
   If there are several possible causal models \(H_h\), compute

   \[
   U_{\mathrm{CDT}}(a_i)
   =
   \sum_h P(H_h)\sum_j P_h(O_j\mid do(A=a_i))D(O_j).
   \]

5. **Choose the action with maximum causal expected utility.**  
   Select

   \[
   a^*
   \in
   \arg\max_i U_{\mathrm{CDT}}(a_i).
   \]

6. **For sequential problems, evaluate policies globally when possible.**  
   If the agent can choose a rule for future behavior, evaluate the policy as an intervention on all relevant decision nodes:

   \[
   U_{\mathrm{CDT}}(\pi)
   =
   \mathbb{E}[\text{utility}\mid do(\pi)].
   \]

This recipe makes CDT usable in practice, but it also reveals the theory’s dependence on causal modeling. If the agent has only statistical correlations and no defensible causal assumptions, CDT may not determine a unique answer.

---

## 11. Philosophical motivation and limitations

The philosophical attraction of CDT is that it connects rational choice to efficacy. If an action merely signals good outcomes without causing them, CDT says that the action is not thereby rational. Choosing an action because it is correlated with good outcomes, when it does not help bring those outcomes about, can look like a kind of magical thinking.

The King David case illustrates this. If summoning Bathsheba does not cause revolt, then the fact that summoning is evidence of an uncharismatic personality should not, by itself, deter David. Similarly, in Newcomb’s problem, CDT says that if the box is already filled, taking the extra \$1,000 cannot causally sacrifice the million.

But the criticisms are serious. First, CDT is vague unless one specifies how counterfactual probabilities are computed. Lewis’s imaging is one answer, but the source notes that it can lead to regress. The interventionist causal-model approach is another, but it imports substantial assumptions.

Second, CDT can recommend actions that seem self-defeating in predictor problems. If a reliable predictor can anticipate CDT’s reasoning, the CDT agent may be exploited, as in Death in Damascus and related cases. Third, CDT’s treatment of self-knowledge is delicate. If an action provides strong evidence that the agent has a dangerous trait, CDT may ignore that evidence when evaluating the action’s causal consequences.

A balanced view, I think, is this: CDT gives a compelling account of how actions should be evaluated once a causal model is fixed, but it is not a complete algorithm for rational choice until we say how the causal model is represented, learned, and updated. The reference article leaves that open. The interventionist framework is the most natural way to fill the gap, but it is an addition to the source rather than a claim contained in it.

---

## Conclusion

Causal decision theory evaluates actions by their expected causal consequences, not by their evidential associations. Its core formula assigns to each action the expected desirability of outcomes weighted by counterfactual probabilities:

\[
U_{\mathrm{CDT}}(A)=\sum_j P(A \mathrel{\square\!\to} O_j)D(O_j).
\]

Where EDT asks what news an action provides, CDT asks what the action brings about. The two coincide when actions are independent of the relevant counterfactuals, but they diverge in cases involving common causes, predictors, and self-revealing choices.

To apply CDT to real problems, one needs a way of computing counterfactual probabilities. The source mentions Lewis’s imaging but notes its difficulties. A natural operational interpretation, which I have developed here, treats the relevant probabilities as intervention probabilities in a causal model:

\[
P(A \mathrel{\square\!\to} O_j) \approx P(O_j\mid do(A)).
\]

With that interpretation, CDT becomes a clear procedure: specify a causal model, intervene on the action or policy variable, compute the resulting distribution over outcomes, and maximize expected utility. This makes the theory precise enough to be used, but it also shows that CDT depends heavily on the agent’s causal assumptions. Without those assumptions, the theory identifies the right question—what would my action cause?—but not always the right answer.

---

## References

Gibbard, Allan, and William L. Harper. 1981. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Belief, Decision, Chance, and Time*, 153–190.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Pearl, Judea. 2009. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press.

Egan, Andy. 2007. “Some Counterexamples to Causal Decision Theory.” *Philosophical Review* 116 (1): 93–114.

Joyce, James M. 2012. “Regret and Instability in Causal Decision Theory.” *Synthese* 187 (1): 123–145.

Oesterheld, Caspar, and Vincent Conitzer. 2021. “Extracting Money from Causal Decision Theorists.” *Philosophical Quarterly* 71 (4): pqaa086.

Wikipedia contributors. 2026. “Causal Decision Theory.” Revision 1381555528. Wikimedia Foundation. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528.