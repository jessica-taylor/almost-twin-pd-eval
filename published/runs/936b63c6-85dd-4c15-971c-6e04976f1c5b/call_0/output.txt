# Causal Decision Theory: Choosing by What an Action Would Cause

Causal decision theory (CDT) is a school of thought in decision theory which says that a rational agent should choose the action that causes the best outcome, in expectation. The reference article contrasts this with evidential decision theory (EDT), which says that an agent should choose the action that would be the best “news”: the action whose having been performed would be most strongly associated with good outcomes. In simple cases the two theories agree. They diverge when an action is evidence for a good outcome without causing it, or when an action is correlated with some relevant feature of the world that the agent cannot change.

The central mathematical question is therefore not merely “What is probable given that I perform this action?” but rather “What would probably happen if I intervened to perform this action?” CDT answers with counterfactual or intervention probabilities rather than ordinary conditional probabilities. This essay explains the formal idea, gives a practical way of applying it, and discusses where the theory becomes controversial. The core counterfactual formula and the examples of King David, Newcomb’s problem, Death in Damascus, the Adversarial Offer, and the Psychopath Button come from the supplied source. The explicit use of modern interventionist notation — in particular Pearl-style `do(·)` operators and structural causal models — is my own operational gloss, intended to make CDT precise enough for unfamiliar cases.

---

## 1. Expected utility: evidential versus causal

Let \(A\) range over possible actions and \(O\) over possible outcomes. Let \(D(O_j)\) be the desirability, utility, or value of outcome \(O_j\). An evidential decision theorist evaluates an action \(A\) by the conditional expected utility

\[
V(A)=\sum_j P(O_j \mid A)\,D(O_j).
\]

Here \(P(O_j \mid A)\) is the ordinary conditional probability of \(O_j\) given that the agent performs \(A\). This is the probability one would assign on receiving the news “the agent did \(A\).”

The reference article gives the causal decision theory formula, due to Allan Gibbard and William Harper, as

\[
U(A)=\sum_j P(A \to O_j)\,D(O_j),
\]

where \(P(A \to O_j)\) is the probability of the counterfactual: if \(A\) were performed, \(O_j\) would occur. I will sometimes write this as \(P(A \mathbin{\square\!\rightarrow} O_j)\) to emphasize that it is not an ordinary material conditional. The decision rule is:

\[
\text{Choose } A^* \in \arg\max_A \sum_j P(A \mathbin{\square\!\rightarrow} O_j)D(O_j).
\]

The article notes that David Lewis proved probabilities of conditionals are not generally equal to conditional probabilities. If one always had

\[
P(A \to O_j)=P(O_j \mid A),
\]

then CDT and EDT would coincide. Lewis’s triviality result shows that such an equality cannot hold generally for nontrivial probability functions. Gibbard and Harper also showed that, under certain assumptions involving a controversial principle related to conditional excluded middle, statistical independence between \(A\) and the relevant counterfactuals suffices for equality. But in many decision problems the action and the counterfactual dependence are not independent in the required way. That is precisely where CDT and EDT separate.

---

## 2. What are counterfactual probabilities?

The source points out an important gap: CDT itself does not specify a unique algorithm for computing the counterfactual probabilities \(P(A \to O_j)\). One proposal mentioned in the article is Lewis’s “imaging” technique. Imagine a space of possible worlds \(w\), with prior probability \(P(w)\). To evaluate \(P(A \to O_j)\), move the probability mass from each world \(w\) to the closest possible world \(w_A\) in which \(A\) is true. Then

\[
P(A \to O_j)=\sum_w P(w)\,\mathbf{1}[w_A \models O_j],
\]

or, if there are multiple equally close \(A\)-worlds, distribute the mass among them according to some similarity weighting. The difficulty is that this requires a notion of “closeness” between worlds, and it may require knowing what one would believe if one were certain of \(A\), which can generate a regress. The source treats this as a serious vagueness objection.

A more operational way to make CDT precise — this is my own addition, not explicitly in the source — is to use an interventionist causal model. In a structural causal model, the world is represented by variables and structural equations. Suppose \(A\) is a variable representing the action, and \(O\) is a variable representing the outcome. An intervention that sets \(A=a\), written \(\mathrm{do}(A=a)\), replaces whatever causal equation normally determines \(A\) with the constant assignment \(A=a\). Other causal laws remain fixed. The counterfactual probability is then identified with the interventional probability:

\[
P(A \mathbin{\square\!\rightarrow} O_j) \approx P(O_j \mid \mathrm{do}(A=a)).
\]

More explicitly, if \(M\) is a structural causal model and \(O_{a}\) is the value that \(O\) would take under the intervention \(\mathrm{do}(A=a)\), then

\[
P(O_j \mid \mathrm{do}(A=a)) = \Pr(O_a = O_j).
\]

If the agent has already observed evidence \(E=e\), the relevant counterfactual may be

\[
P(O_j \mid \mathrm{do}(A=a), E=e),
\]

computed by updating over exogenous variables consistent with \(e\), then applying the intervention. For ordinary one-shot decisions made before acting, the prospective interventional probability is usually the relevant object.

This formulation makes clear that CDT needs causal assumptions. Observational data alone often does not determine \(P(O \mid \mathrm{do}(A))\). If one has a causal graph, one can sometimes use adjustment formulas. For example, if a set of variables \(Z\) satisfies a back-door condition relative to the effect of \(A\) on \(O\), then

\[
P(O=o \mid \mathrm{do}(A=a))
=
\sum_z P(O=o \mid A=a, Z=z)P(Z=z).
\]

Without such a model, CDT is underdetermined. That is not a bug peculiar to this formulation; it reflects the source’s point that CDT does not itself supply a complete algorithm for counterfactual calculation.

A useful intermediate formulation uses “dependency hypotheses.” Let \(K\) range over the agent’s hypotheses about how the world causally works. Then CDT can be written as

\[
U(A)
=
\sum_k P(K=k)
\sum_j P_k(O_j \mid \mathrm{do}(A))D(O_j).
\]

Here \(P(K=k)\) is the agent’s prior credence in dependency hypothesis \(k\), and \(P_k(O_j \mid \mathrm{do}(A))\) is the outcome distribution under intervention according to that hypothesis. The source quotes Andy Egan’s criticism that CDT holds fixed the agent’s unconditional credences in dependency hypotheses. This formula makes that requirement explicit.

---

## 3. Applying CDT: an informal procedure

A practical CDT analysis can be organized as follows.

1. **Specify the action space.** Identify the possible actions \(A\), or policies \(\pi\), among which the agent chooses.

2. **Specify outcomes and utilities.** Assign desirabilities \(D(O_j)\).

3. **Specify the causal structure.** This may be a causal graph, a set of structural equations, or a set of dependency hypotheses \(K\).

4. **Intervene on the action.** For each candidate action \(A=a\), compute the distribution of outcomes under \(\mathrm{do}(A=a)\), holding fixed the causal structure and the agent’s prior credences in dependency hypotheses.

5. **Take expected utility.** Compute

   \[
   U(a)=\sum_j P(O_j \mid \mathrm{do}(A=a))D(O_j),
   \]

   or, with uncertain causal structure,

   \[
   U(a)=\sum_k P(k)\sum_j P_k(O_j \mid \mathrm{do}(A=a))D(O_j).
   \]

6. **Choose maximally.** Select an action with maximal causal expected utility.

This procedure evaluates actions by their expected causal consequences, not by their evidential associations.

### Example: apples and oranges

Suppose eating an apple makes you happy if the apple is good, but sad if it is bad. You are uncertain whether the apple is good. Let \(G\) be the proposition that the apple is good, with prior probability \(p\). Let the utility of happiness be \(h>0\), and the utility of sadness be \(-s<0\). If eating the orange has utility \(u_O\), then CDT compares

\[
U(\text{apple})=p h + (1-p)(-s)
\]

with

\[
U(\text{orange})=u_O.
\]

The apple’s being good or bad is a state of the world that the action does not normally change. The relevant causal question is: if I ate the apple, what would happen given the apple’s actual type? That is exactly what the expectation over \(G\) represents.

### Example: King David and Bathsheba

The source gives Gibbard and Harper’s example. King David wants Bathsheba but fears that summoning her may provoke revolt. David does not know whether he is charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. But unjust acts themselves do not cause revolts. The common cause is the king’s underlying charisma or lack thereof.

Let \(C\) be charisma, \(A\) be the action of summoning Bathsheba, and \(R\) be revolt. The causal structure is roughly:

\[
C \to A,\qquad C \to R,
\]

but not

\[
A \to R.
\]

Summoning Bathsheba may be evidence that David is uncharismatic, because uncharismatic kings are more likely to act unjustly. EDT therefore may recommend abstaining, since the news “David summoned Bathsheba” is bad news about revolt. But CDT asks what would happen if David intervened to summon her. Since the action does not causally affect charisma, and charisma is what determines revolt risk, the causal probability of revolt is unchanged by the action, conditional on charisma. If summoning has positive utility and does not causally increase revolt, CDT recommends summoning.

This example illustrates the core distinction: CDT does not allow an action to serve merely as evidence for an unchangeable trait when evaluating causal consequences.

---

## 4. Newcomb’s problem

Newcomb’s problem is the classic test case. The source describes it as follows. A highly reliable predictor has predicted whether the player will take both boxes or only one. Box A is transparent and contains \$1,000. Box B is opaque. If the predictor predicted that the player will take both boxes, Box B is empty. If the predictor predicted that the player will take only Box B, Box B contains \$1,000,000. The player now chooses between one-boxing and two-boxing.

Let \(T\) be the predictor’s earlier prediction: \(T=1\) if it predicted one-boxing, \(T=2\) if it predicted two-boxing. Let \(q=P(T=1)\). At the time of choice, CDT normally assumes the prediction is already fixed and is not causally affected by the player’s current action. The intervention \(\mathrm{do}(A=\text{two-box})\) does not change \(T\). Therefore:

\[
U(\text{two-box})
=
q(1{,}001{,}000)+(1-q)(1{,}000),
\]

because if the predictor predicted one-boxing, Box B contains \$1,000,000 and Box A contains \$1,000; if it predicted two-boxing, Box B is empty and Box A contains \$1,000.

Similarly,

\[
U(\text{one-box})
=
q(1{,}000{,}000)+(1-q)(0).
\]

The difference is

\[
U(\text{two-box})-U(\text{one-box})
=
1{,}000.
\]

So, under this causal model, two-boxing dominates one-boxing by \$1,000 regardless of \(q\). CDT therefore recommends taking both boxes.

EDT reasons differently. If the predictor is 99% accurate, then learning that the player one-boxed is strong evidence that the predictor predicted one-boxing, so Box B probably contains \$1,000,000. Learning that the player two-boxed is strong evidence that Box B is empty. Thus EDT recommends one-boxing.

The source notes that philosophers usually prefer CDT to EDT when forced to choose, but also that Newcomb’s problem remains divisive. One important clarification is that CDT’s recommendation depends on the assumed causal structure. If the predictor’s prediction were causally downstream of the action — for example, if the action somehow caused the past prediction, or if the predictor’s simulation were interventionally responsive to the agent’s choice in a way not captured by the standard temporal ordering — then the causal calculation could change. In the standard formulation, however, the prediction is fixed before the action, and CDT two-boxes.

---

## 5. Policies, plans, and dynamic choice

So far I have discussed single actions. But many decision problems involve policies: rules mapping observations or histories to actions. CDT can evaluate a policy \(\pi\) by treating the choice of policy as the intervened variable. If \(\Pi\) is a policy variable, then

\[
U(\pi)=\mathbb{E}[D(O)\mid \mathrm{do}(\Pi=\pi)].
\]

In a sequential setting, this becomes

\[
U(\pi)
=
\sum_h P(h)\sum_o P(o\mid \mathrm{do}(\text{follow }\pi),h)D(o),
\]

where \(h\) ranges over histories at which the policy may act. If the agent can genuinely choose a plan or commitment device in advance, CDT should evaluate that choice causally. If precommitting changes what predictors do, or changes future options, those causal consequences belong in the calculation.

If, instead, the agent makes local choices step by step without binding precommitment, CDT normally evaluates each choice by intervening on the current action while holding fixed the agent’s current credences and assumed future policy. This can create diachronic problems: a sequence of locally causally optimal choices may lead to outcomes that look globally disadvantageous. The source mentions Oesterheld and Conitzer’s claim that CDT agents can be subject to diachronic Dutch books. Whether the right response is to evaluate whole policies rather than individual acts, or to add ratifiability or stability constraints, is not settled by the source and is partly a matter of interpretation.

A reasonable operational view, which I propose rather than find in the source, is this: when a policy is available as an object of choice, evaluate the policy directly; when only momentary actions are available, evaluate the current action under the agent’s current plan for the future. This preserves the interventionist logic while reducing some dynamic inconsistencies.

---

## 6. Vagueness and the need for a causal model

The source’s vagueness objection is important. CDT says to maximize expected utility computed from counterfactual probabilities, but it does not by itself say where those probabilities come from. Lewis’s imaging proposal requires a similarity metric over possible worlds. The metric is not given by probability alone, and trying to define what one would believe if one were certain of \(A\) may lead to regress.

The interventionist formulation avoids some of this by replacing “closest possible world” with an explicit causal model. But it introduces a different dependence: the answer now depends on the chosen causal graph or structural equations. In many ordinary cases this is harmless. In unusual predictor cases, the correct causal representation may itself be philosophically disputed.

Thus, CDT is best understood not as a complete algorithm that takes only probabilities and utilities as inputs, but as a schema:

\[
\text{CDT schema: choose the action that maximizes expected utility under the best available causal model.}
\]

If no causal model is available, CDT does not yield a unique answer. If several causal models are plausible, Bayesian averaging over dependency hypotheses is a natural operational response:

\[
U(A)=\sum_m P(M=m)\sum_j P(O_j\mid \mathrm{do}(A),M=m)D(O_j).
\]

This is not an extra principle of CDT so much as a way of implementing it under causal uncertainty.

---

## 7. Counterexamples and pressure cases

The source discusses several cases intended to show that straightforward CDT can make unintuitive decisions.

### Death in Damascus

In the Death in Damascus scenario, Death is a reliable predictor of where you will be tomorrow and goes to wait there. If Death predicts you will be in Damascus, it goes to Damascus; if it predicts you will flee to Aleppo, it goes to Aleppo. The correlation between your choice and Death’s location is extremely strong, but in the standard causal story your current choice does not cause Death’s earlier prediction.

CDT may therefore treat Death’s prediction as fixed. If both locations seem equally likely to contain Death once the prediction is made, CDT may be indifferent, or may choose based on small causal benefits such as the comfort of staying home. But from an evidential perspective, choosing a location is terrible news: whatever you choose, Death is likely already there.

The source says that a CDT agent may be unable to process the correlation and may make irrational decisions, and that variants have been constructed in which CDT voluntarily loses money or forgoes guaranteed payoffs. The deeper issue is how to represent prediction. If Death’s prediction is caused by your decision procedure, one might model the decision procedure itself as a common cause of both the prediction and the action. Then evaluating policies rather than isolated actions may sometimes give more plausible results. But if the correlation is purely logical or mathematical, without a causal link, CDT’s interventionist machinery may still ignore it. This remains one of the most important open pressures on CDT.

### The Adversarial Offer

The source describes the Adversarial Offer. Two boxes are available. The buyer may buy one box or none, but not both. Each box costs \$1. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. Both believe the seller’s prediction is accurate with probability \(0.75\).

From a CDT perspective, the buyer’s current purchase does not causally affect whether the seller put money in the box yesterday. If the buyer looks at the boxes symmetrically, CDT may reason that at least one box contains \$3, so the average box contains at least \$1.50. Since a box costs only \$1, buying one has positive causal expected value.

But the seller can still profit, because the buyer is likely to buy exactly the boxes that the seller predicted the buyer would buy, and those boxes are empty. The buyer’s action is correlated with the seller’s prediction, even if it does not cause it. This is another example where CDT’s prohibition on conditioning on one’s own action can lead to choices that are exploitable by an adversary who predicts the agent.

### The Psychopath Button

In the Psychopath Button case, Paul is considering pressing a button that would kill all psychopaths. Paul thinks a world without psychopaths would be much better. But he is confident that only a psychopath would press such a button. Paul strongly prefers living in a world with psychopaths to dying.

Let \(S\) be the proposition that Paul is a psychopath. Let \(p=P(S)\). Suppose pressing the button yields:

- if \(S\) is true: Paul dies, utility \(D\);
- if \(S\) is false: no psychopaths, utility \(N\).

Not pressing yields living in the current world, utility \(L\). Assume

\[
N > L > D.
\]

CDT evaluates pressing using Paul’s prior probability \(p\), not the conditional probability \(P(S\mid \text{press})\):

\[
U(\text{press})=pD+(1-p)N,
\]

\[
U(\text{not press})=L.
\]

If \(p\) is small enough and \(N\) is sufficiently better than \(L\), CDT recommends pressing. EDT, by contrast, conditions on the action and notes that pressing is strong evidence that Paul is a psychopath, so EDT recommends not pressing.

The source quotes Egan’s claim that CDT endorses pressing, while “pretty much everyone” agrees Paul should not press. It also notes Jim Joyce’s defense that CDT can take into account information about what one is inclined or likely to do as evidence. This suggests a possible reconciliation: if Paul observes in himself a strong inclination to press, he may update his prior \(p\) before evaluating the action. If after this update he probably is a psychopath, CDT will not press. But the difficult question remains: when may an agent use its own prospective action as evidence? CDT traditionally says that the action itself should not be conditioned on in the final expected-utility calculation, while Joyce’s response suggests that evidence about dispositions can be admitted earlier. The source leaves the exact boundary unclear.

### Dutch books and money pumps

The source also mentions Oesterheld and Conitzer’s argument that CDT can be made to voluntarily lose money in multiple scenarios and can be subject to diachronic Dutch books. These arguments are important because they turn philosophical intuitions into formal pressure: if a decision theory systematically exposes agents to exploitation, that counts against it, at least in environments with adversarial predictors.

A CDT defender might respond in several ways. One is to deny that the cases are genuinely possible, or to insist that the correct causal model restores sensible recommendations. Another is to say that CDT should evaluate policies or commitments when they are causally effective. A third is to add ratifiability or stability conditions. The source does not resolve this, and I do not think the issue can be closed by definition alone. It is one of the main places where CDT remains philosophically contested.

---

## 8. What CDT gets right, and where it remains open

CDT captures an attractive idea: rational choice should be guided by what actions bring about, not merely by what actions indicate. If an action is correlated with a good outcome but does not cause it, CDT resists treating the action as a magical signal. In ordinary decisions — taking medicine, buying insurance, investing, repairing a machine — this causal discipline is usually exactly what we want.

The theory is most compelling when the causal structure is clear. If a randomized trial tells us that a treatment causes recovery, CDT uses the trial’s interventional probabilities. If an action is merely correlated with recovery because healthier people select it, CDT warns against naïve conditional reasoning.

The theory is most controversial when the agent’s own choice is predicted by another agent. In Newcomb-like cases, CDT’s insistence on holding fixed the predictor’s earlier state leads to recommendations that can look self-defeating. In Death in Damascus and the Adversarial Offer, CDT may ignore correlations that seem decision-relevant. In the Psychopath Button, it may fail to use the agent’s own choice tendencies as evidence unless we carefully specify when such evidence may be admitted.

A workable operational interpretation, therefore, is to treat CDT as requiring an explicit causal model. When the model is given, compute interventional probabilities. When the model is uncertain, average over dependency hypotheses. When policies are available, evaluate policies. When only local actions are available, evaluate local interventions under the agent’s current plan. This does not eliminate all philosophical difficulties, but it makes the theory precise enough to decide many unfamiliar cases.

---

## Conclusion

Causal decision theory says: choose the action whose causal consequences would be best in expectation. Formally, it replaces EDT’s conditional probabilities \(P(O_j\mid A)\) with counterfactual or interventional probabilities \(P(A\mathbin{\square\!\rightarrow}O_j)\). In modern terms, it evaluates actions using \(P(O_j\mid \mathrm{do}(A))\) rather than \(P(O_j\mid A)\). This gives a clear rule in cases where actions are evidence for outcomes without causing them.

However, CDT does not by itself specify how to compute counterfactual probabilities. It needs a causal model, a similarity metric, or some other account of intervention. This vagueness is the source of both its flexibility and its controversies. In standard predictor problems, CDT gives stable recommendations — two-box in Newcomb’s problem, summon Bathsheba in Gibbard and Harper’s example — but in adversarial or self-referential prediction cases, its recommendations can appear exploitable. The best way to use CDT is therefore explicit: state the causal assumptions, intervene on the action or policy, compute expected utility, and acknowledge where the causal representation itself is doing the philosophical work.

---

## References

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Belief, Decision, Chance, and Time*, 153–190, 1981.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

Lewis, David. “Probabilities of Conditionals and Conditional Probabilities.” *Philosophical Review* 85, no. 3 (1976): 297–315.

Oesterheld, Caspar, and Vincent Conitzer. “Extracting Money from Causal Decision Theorists.” *The Philosophical Quarterly* 71, no. 4 (2021): pqaa086.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press, 2009. Included as an additional reference for the interventionist notation used above.

Wikipedia contributors. “Causal Decision Theory.” Revision 1381555528, October 23, 2026. Creative Commons Attribution-ShareAlike 4.0 International. Primary source for the present essay.