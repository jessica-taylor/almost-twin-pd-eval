# Causal Decision Theory: Expected Utility under Intervention

Causal decision theory (CDT) is a family of decision rules that evaluate choices by their expected causal consequences. The reference article summarizes the core idea as follows: when a rational agent faces several possible actions, she should choose the action that causes the best outcome in expectation. This contrasts with evidential decision theory (EDT), which chooses the action that would be the best “news” — the action whose occurrence would be most strongly associated with good outcomes.

The source gives the informal examples of eating an apple rather than an orange, and of an apple that may be good or bad. If eating a good apple causes happiness and eating a bad apple causes sadness, the rational choice depends not only on the causal structure but also on the agent’s uncertainty: the prior probability that the apple is good, the utility of happiness, and the disutility of sadness.

The reference article leaves an important question open: how exactly are the relevant “expected causal consequences” to be computed? It presents Gibbard and Harper’s counterfactual formula and notes Lewis’s imaging proposal, but it does not supply a full algorithm. In what follows, I first reconstruct the formal theory as presented in the source, then develop an operational interpretation using causal models and interventions. Where I add assumptions beyond the source, I will say so explicitly.

---

## 1. Two decision rules: evidential and causal expected utility

Let \(\mathcal A\) be a set of possible actions, and let \(\mathcal O=\{O_1,O_2,\dots\}\) be possible outcomes. Let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). For simplicity, assume a finite outcome space; the continuous case is obtained by replacing sums with integrals.

Evidential decision theory evaluates an action \(A\) by the conditional probability of outcomes given that action:

\[
V_{\text{EDT}}(A)=\sum_j P(O_j \mid A)\,D(O_j).
\]

The quantity \(P(O_j\mid A)\) is ordinary conditional probability. EDT asks: if I learned that I had taken \(A\), how likely would \(O_j\) be?

The source article gives the causal decision-theoretic rule, following Gibbard and Harper (1981), as

\[
U(A)=\sum_j P(A \to O_j)\,D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(A\to O_j)\) is the probability of the counterfactual that \(A\) would lead to, or imply, \(O_j\). I will write this counterfactual arrow as \(A \square\!\to O_j\) to emphasize that it is not material implication and not ordinary conditionalization:

\[
V_{\text{CDT}}(A)=\sum_j P(A \square\!\to O_j)\,D(O_j).
\]

The phrase in the source, “the counterfactual probability of it being the case that \(A\) necessarily implies \(O_j\),” should not be read as logical necessity. It means something like: the probability that, were the agent to take action \(A\), outcome \(O_j\) would obtain.

The distinction matters because, as the source notes, Lewis proved that the probability of a conditional is not generally equal to a conditional probability. If one could always replace \(P(A \square\!\to O_j)\) with \(P(O_j\mid A)\), CDT would collapse into EDT. Lewis’s triviality result shows that such an identification cannot be generally sustained. Gibbard and Harper also showed that, under certain axioms — one related to the controversial principle of conditional excluded middle — statistical independence between the action and the relevant counterfactual can make the two calculations agree. But in decision problems involving common causes, predictors, or self-knowledge, that independence can fail.

Thus the central formal question for CDT is:

> What is the probability distribution over outcomes under the counterfactual supposition that action \(A\) is performed?

---

## 2. Counterfactual probabilities: imaging and intervention

The source notes that CDT itself does not specify an algorithm for calculating counterfactual probabilities. One proposal mentioned in the source is Lewis’s “imaging” technique. The idea is that the agent has a probability distribution over possible worlds. To evaluate \(P(A \square\!\to O)\), one moves probability mass from each possible world \(w\) to the closest possible world \(w_A\) in which \(A\) holds. If the closest \(A\)-world is unique, then

\[
P(A \square\!\to O)
=
\sum_{w} P(w)\,\mathbf 1[O \text{ holds in } w_A],
\]

where \(w_A\) is the closest \(A\)-world to \(w\). More generally, one may use a stochastic kernel that redistributes mass from \(w\) over nearby \(A\)-worlds.

Imaging captures the intuitive idea that when we imagine an action being performed, we should preserve as much of the actual world’s background as possible, changing only what is needed to make the action true. But the source also notes a difficulty: imaging requires knowing what the agent would believe if she were certain of \(A\), and that itself may be a conditional to which the agent assigns probability less than one. This can generate a regress.

A more operational way to make CDT precise — this is my own proposal, not a claim of the source — is to use causal models. A structural causal model represents the world by variables, structural equations, and a distribution over exogenous background variables. Let \(M\) be a causal model with exogenous variables \(U\), endogenous variables \(V\), structural equations \(F\), and prior distribution \(P(U)\). An action \(A\) is one of the endogenous variables.

An intervention that sets \(A=a\) is written \(\operatorname{do}(A=a)\). Formally, it replaces the structural equation for \(A\) with the constant equation \(A=a\). All other equations remain unchanged. Let \(O_a(u)\) be the value that outcome \(O\) would take in the modified model when the background variables are \(U=u\). Then the causal expected utility of action \(a\) is

\[
V_{\text{CDT}}(a)
=
\sum_u P(u)\,D(O_a(u)),
\]

or equivalently

\[
V_{\text{CDT}}(a)
=
\sum_o D(o)\,P(o \mid \operatorname{do}(a)).
\]

This gives a clean interpretation of Gibbard and Harper’s counterfactual probability:

\[
P(A=a \square\!\to O=o)
\quad\text{is modeled as}\quad
P(o \mid \operatorname{do}(a)).
\]

If the agent has already observed some evidence \(e\) before choosing, and that evidence is not itself downstream of the action being evaluated, the agent should first update her beliefs about the exogenous variables:

\[
V_{\text{CDT}}(a \mid e)
=
\sum_u P(u \mid e)\,D(O_a(u))
=
\sum_o D(o)\,P(o \mid \operatorname{do}(a), e).
\]

This is the natural CDT rule for choice conditional on current information.

If the agent is uncertain about which causal model is correct, we can introduce dependency hypotheses \(H\), where each hypothesis specifies a causal structure or structural model. Then a natural CDT rule is

\[
V_{\text{CDT}}(a)
=
\sum_h P(h)
\sum_o D(o)\,P_h(o \mid \operatorname{do}(a)).
\]

The source’s discussion of “dependency hypotheses” fits naturally with this formulation. However, Egan’s criticism, discussed below, concerns precisely whether CDT should hold fixed the agent’s prior credences in such hypotheses when the action itself provides evidence about them.

---

## 3. An operational recipe for applying CDT

Using the interventionist interpretation, one can apply CDT by the following procedure.

### Step 1: Specify actions, outcomes, and utilities

List the available actions \(a\in\mathcal A\), the relevant outcomes \(O\), and the utility function \(D(O)\). If the decision is sequential, the “action” may be a policy rather than a single act.

### Step 2: Specify the causal model

Identify the variables relevant to the decision: background traits, predictions by others, physical states, observations, intermediate consequences, and final outcomes. Represent the assumed causal relations. For example, a common cause \(C\) of both an action tendency and an outcome should be represented as

\[
C \to A,\qquad C \to O,
\]

whereas a genuine causal effect of the action on the outcome is represented as

\[
A \to O.
\]

CDT treats these two structures very differently.

### Step 3: Intervene on the action

To evaluate action \(a\), replace the normal mechanism producing \(A\) with the fixed assignment \(A=a\). This cuts incoming arrows to \(A\). Variables that are causally downstream of \(A\) continue to respond to it; variables that are merely correlated with \(A\) through common causes do not change merely because we condition counterfactually on \(A=a\).

### Step 4: Compute the interventional outcome distribution

If the causal graph is known, one can often compute \(P(o\mid \operatorname{do}(a))\) by standard adjustment formulas. For example, if \(Z\) is a set of confounders satisfying the back-door criterion relative to \(A\) and \(O\), then

\[
P(o \mid \operatorname{do}(a))
=
\sum_z P(o \mid a,z)\,P(z).
\]

If there is no confounding — for example, in a randomized experiment — then

\[
P(o \mid \operatorname{do}(a)) = P(o \mid a),
\]

and CDT agrees with EDT.

### Step 5: Maximize causal expected utility

Choose an action maximizing

\[
V_{\text{CDT}}(a)=\sum_o D(o)P(o\mid \operatorname{do}(a)).
\]

### Step 6: For policies, intervene on the policy

In dynamic problems, the alternatives may be policies \(\pi\) mapping histories or observations to actions. Suppose there are action variables \(A_t\) and observation variables \(X_t\). A policy \(\pi\) assigns

\[
A_t = \pi_t(X_{<t},A_{<t}).
\]

The causal expected utility of the policy is

\[
V_{\text{CDT}}(\pi)
=
\mathbb E\bigl[D(O) \mid \operatorname{do}(\pi)\bigr],
\]

where \(\operatorname{do}(\pi)\) means intervening to make the agent follow \(\pi\) at each relevant decision point. Observations are not simply conditioned away; they are generated by the causal process, possibly affected by earlier interventions. This is the natural way to extend CDT from one-shot acts to plans and policies.

This policy formulation is my own elaboration, though it is continuous with the general idea that CDT evaluates the causal consequences of the agent’s choice or plan.

---

## 4. Examples

### 4.1 A simple apple

Suppose an apple may be good with probability \(p\) and bad with probability \(1-p\). Eating a good apple causes happiness \(H\); eating a bad apple causes sadness \(S\). An orange is known to cause mild sadness \(S_O\). Utilities are \(D(H)\), \(D(S)\), and \(D(S_O)\).

If eating the apple does not causally affect whether the apple is good or bad, then

\[
V_{\text{CDT}}(\text{eat apple})
=
pD(H)+(1-p)D(S).
\]

The orange has value

\[
V_{\text{CDT}}(\text{eat orange})=D(S_O).
\]

CDT chooses the apple iff

\[
pD(H)+(1-p)D(S) > D(S_O).
\]

Here CDT and EDT give the same answer, because there is no problematic dependence between the action and the state of the apple.

### 4.2 King David and Bathsheba

The source gives Gibbard and Harper’s example of King David. David wants Bathsheba but fears revolt. He knows that kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. Unjust acts themselves do not cause revolts; rather, the uncharismatic king’s disposition causes both unjust behavior and revolt. David does not know whether he is charismatic.

Let \(C\) be charisma, \(A\) the action of summoning Bathsheba, and \(R\) a successful revolt. The causal structure is approximately:

\[
C \to A,\qquad C \to R,
\]

while the action \(A\) itself does not cause \(R\), or at least does not cause \(R\) except through pathways David regards as negligible.

Let \(q=P(C=\text{charismatic})\). Let

\[
r_c=P(R\mid C=\text{charismatic}),\qquad
r_u=P(R\mid C=\text{uncharismatic}),
\]

with \(r_c<r_u\). Suppose summoning Bathsheba gives David benefit \(b\), while a revolt imposes cost \(c\).

CDT evaluates the intervention \(\operatorname{do}(A=\text{summon})\). Since charisma is a fixed background variable relative to the intervention, the causal probability of revolt is approximately

\[
P(R\mid \operatorname{do}(\text{summon}))
=
q r_c + (1-q) r_u.
\]

Thus

\[
V_{\text{CDT}}(\text{summon})
\approx
b - c\bigl(q r_c + (1-q)r_u\bigr),
\]

plus whatever baseline utility David assigns to the status quo.

EDT, by contrast, uses

\[
P(R\mid A=\text{summon}).
\]

Because uncharismatic kings are more likely to summon Bathsheba, observing that David summons her is evidence that he is uncharismatic. Therefore

\[
P(C=\text{uncharismatic}\mid A=\text{summon})
>
P(C=\text{uncharismatic}),
\]

and EDT may assign a much higher probability to revolt. EDT can therefore recommend abstaining, while CDT recommends summoning if the expected benefit exceeds the baseline causal risk.

The source says EDT recommends abstention and CDT recommends sending for Bathsheba. The example illustrates CDT’s central commitment: David’s action may be evidence of his type, but it does not change his type.

### 4.3 Newcomb’s problem

In Newcomb’s problem, a highly reliable predictor has predicted whether the agent will take both boxes or only one. Box A always contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The agent chooses after the prediction has been made.

Let \(q\) be the agent’s prior probability that the predictor predicted one-boxing. Under CDT, the agent evaluates interventions on her current choice. Since the prediction is already fixed, the intervention does not change the predictor’s earlier prediction.

If the agent one-boxes:

\[
V_{\text{CDT}}(\text{one-box})
=
q\cdot 1{,}000{,}000 + (1-q)\cdot 0.
\]

If the agent two-boxes:

\[
V_{\text{CDT}}(\text{two-box})
=
q\cdot 1{,}001{,}000 + (1-q)\cdot 1{,}000.
\]

The difference is

\[
V_{\text{CDT}}(\text{two-box})
-
V_{\text{CDT}}(\text{one-box})
=
1{,}000.
\]

So CDT recommends two-boxing. In fact, two-boxing causally dominates one-boxing: whatever is in Box B, taking both boxes yields \$1,000 more than taking only Box B.

EDT reasons differently. Taking only Box B is strong evidence that the predictor predicted one-boxing, so Box B is likely to contain \$1,000,000. If the predictor is 99% accurate, EDT gives approximately

\[
V_{\text{EDT}}(\text{one-box})
\approx 0.99\cdot 1{,}000{,}000
=
990{,}000,
\]

whereas

\[
V_{\text{EDT}}(\text{two-box})
\approx
0.99\cdot 1{,}000 + 0.01\cdot 1{,}001{,}000
\approx
10{,}990.
\]

Thus EDT recommends one-boxing. The source notes that philosophers disagree about which answer is rational, but that CDT’s answer is two-boxing.

### 4.4 The psychopath button

The source discusses an example from Egan. Paul is considering pressing a button that would kill all psychopaths. Paul thinks a world without psychopaths would be much better. But he is confident that only a psychopath would press the button. He strongly prefers living in a world with psychopaths to dying.

Let \(P\) be the proposition that Paul is a psychopath, and let \(B\) be pressing the button. If Paul is not a psychopath, pressing the button causes a better world. If Paul is a psychopath, pressing the button causes his death, which is worst for him.

EDT evaluates

\[
P(P\mid B=\text{press}).
\]

Since Paul believes only a psychopath would press, this conditional probability is high. EDT therefore recommends not pressing.

CDT evaluates \(\operatorname{do}(B=\text{press})\). If Paul’s psychopathy is treated as a fixed background variable, then pressing the button does not make him a psychopath. If his prior or admissible-evidence posterior probability of being a psychopath is low, and the benefit of a world without psychopaths is high, CDT can endorse pressing.

The source says that, according to Egan, “pretty much everyone” agrees Paul should not press, yet CDT endorses pressing. This is one of the most striking alleged counterexamples to CDT.

A CDT-friendly response, suggested by the source’s reference to Joyce, is that Paul may use actual evidence about his inclinations as evidence. If Paul has strong independent evidence that he is psychopathic, CDT should condition on that evidence before evaluating the intervention. The counterexample depends on the act itself being treated as evidence of Paul’s type, rather than on separately available evidence.

---

## 5. Dependencies, counterfactuals, and agreement with EDT

CDT does not ignore dependencies altogether. It ignores dependencies that are merely evidential rather than causal. More precisely, in the interventionist formulation, CDT preserves causal structure downstream of the action and severs the normal causes of the action.

This means CDT distinguishes several kinds of dependence.

### Common causes

If a variable \(C\) causes both the action and the outcome,

\[
C \to A,\qquad C \to O,
\]

then \(A\) and \(O\) are correlated, but intervening on \(A\) does not change \(C\). CDT treats \(C\) as fixed background. David’s charisma is an example.

### Direct causal effects

If

\[
A \to O,
\]

then intervening on \(A\) changes the probability of \(O\). CDT fully counts this effect.

### Mediators

If

\[
A \to M \to O,
\]

then intervening on \(A\) affects \(M\), which affects \(O\). CDT includes the entire downstream causal chain.

### Colliders and selection effects

If two variables independently influence a third,

\[
A \to S \leftarrow C,
\]

then conditioning on \(S\) can create a spurious correlation between \(A\) and \(C\). A careful causal model prevents mistaking such correlations for causal effects. This is one advantage of the interventionist formulation I have proposed.

CDT and EDT agree when the action is probabilistically independent of the relevant background dependencies, or when the causal effect of the action can be read directly from the conditional distribution. The source notes Gibbard and Harper’s result that, under certain axioms, statistical independence of \(A\) and the counterfactual \(A\to O_j\) suffices for

\[
P(A\to O_j)=P(O_j\mid A).
\]

In modern causal language, this is the familiar fact that if there is no confounding, the observational conditional equals the interventional distribution.

---

## 6. Open problems and criticisms

The source identifies several criticisms of CDT. The first is vagueness. CDT does not itself specify how to compute counterfactual probabilities. Lewis’s imaging proposal is one answer, but it faces the regress problem noted by Shaffer. The interventionist account I have used avoids some of that regress by taking a causal model as primitive, but it introduces another difficulty: the agent must have a causal model, and different models can yield different decisions.

A second criticism concerns counterexamples. Newcomb’s problem is the classic case: CDT two-boxes and thereby receives only \$1,000 when a one-boxer would receive \$1,000,000. Whether this is a decisive objection depends on whether one thinks rational choice should track causal influence or predictive correlation.

Egan’s criticism is deeper. He argues that CDT’s requirement to hold fixed the agent’s unconditional credences in dependency hypotheses creates a disconnect between the intuitive rule “do what you expect will bring about the best results” and CDT’s actual algorithm. In cases such as the psychopath button, Death in Damascus, and related predictor problems, CDT may recommend actions that seem self-defeating.

In Death in Damascus, a reliable predictor predicts where the agent will be tomorrow, and Death goes there. The agent’s choice is highly correlated with Death’s location, but does not causally determine it if the prediction has already been made. Standard one-shot CDT may see no causal advantage to fleeing or staying, except for small travel costs, while intuitively the correlation seems decision-relevant. The source says a CDT agent may be unable to process the correlation and may make irrational decisions.

The source also mentions more recent variants, such as the Adversarial Offer. Two boxes are sold for \$1 each; the buyer may buy one or none. The seller put \$3 in each box she predicted the buyer would not acquire. The seller’s prediction is believed accurate with probability \(0.75\). The source says CDT reasons that at least one box contains \$3, so the average box has at least \$1.50 in causal expected value, which exceeds the \$1 cost. Therefore CDT buys a box, but this is profitable for the seller. Such cases are meant to show that CDT can voluntarily lose money when facing an adversary who predicts its choices.

Oesterheld and Conitzer, cited in the source, argue that CDT agents can be subject to diachronic Dutch books in Newcomb-like scenarios. This is a serious challenge if one expects a rational decision theory to avoid sure losses across time when the agent’s future choices are predictable.

How should a CDT defender respond? The source mentions Joyce’s view that CDT can take information about what one is inclined or likely to do as evidence. On the interventionist reconstruction, this means the agent may condition on evidence before performing the intervention. If Paul has independent evidence that he is a psychopath, he should update his prior probability of being a psychopath before evaluating \(\operatorname{do}(\text{press})\). If David has evidence about his charisma, he should condition on it.

But this response does not fully dissolve cases where the act itself is the main evidence about the agent’s type or future behavior. One possible operational refinement — this is my own suggestion, not in the source — is to evaluate policies or decision algorithms rather than isolated actions. In predictor problems, the predictor often predicts the agent’s decision procedure. If the agent can choose or commit to a policy, CDT should evaluate the policy under intervention:

\[
V_{\text{CDT}}(\pi)=\mathbb E[D(O)\mid \operatorname{do}(\pi)].
\]

This may handle some sequential problems more naturally. However, it does not automatically make CDT one-box in Newcomb’s problem or refrain from pressing the psychopath button, because the intervention still treats the predictor’s prior prediction as fixed unless the policy choice occurs before the prediction.

Thus the deepest uncertainty remains normative, not merely computational. If one accepts that rational choice should respond only to causal consequences of the actual intervention, CDT is coherent. If one thinks rational choice should also exploit reliable correlations between one’s choice and favorable states, even when those correlations are not causal, then CDT may seem too restrictive.

---

## Conclusion

Causal decision theory evaluates actions by the expected utility of their counterfactual consequences. In its classical Gibbard-Harper form, it uses probabilities of counterfactuals rather than ordinary conditional probabilities:

\[
V_{\text{CDT}}(A)=\sum_j P(A \square\!\to O_j)D(O_j).
\]

This distinguishes it from EDT, which uses \(P(O_j\mid A)\). The two rules agree when actions are independent of the relevant background dependencies, but they diverge in cases involving common causes, predictors, and self-knowledge.

The source leaves open how to compute the counterfactual probabilities. A natural operational interpretation, which I have developed here, identifies them with interventional probabilities in a causal model:

\[
P(A \square\!\to O)=P(O\mid \operatorname{do}(A)).
\]

This yields a practical procedure: specify a causal model, intervene on the action or policy, compute the resulting outcome distribution, and maximize expected utility. The procedure clarifies how CDT treats dependencies: it preserves downstream causal consequences, holds fixed common causes and prior predictions, and refuses to treat the action itself as mere evidence.

That refusal is also the source of CDT’s most famous difficulties. In Newcomb’s problem, Death in Damascus, the psychopath button, and adversarial betting scenarios, CDT can recommend actions that are predictably worse than alternatives recommended by EDT or by ordinary intuition. Whether these are fatal objections depends on whether one thinks rational agency is essentially causal intervention or whether it may also legitimately exploit evidential correlations. CDT gives a clear answer: choose the intervention with the best expected causal consequences.

---

## References

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge University Press.

Egan, Andy. 2007. “Some Counterexamples to Causal Decision Theory.” *Philosophical Review* 116 (1): 93–114.

Gibbard, Allan, and William L. Harper. 1981. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*, 153–190.

Lewis, David. 1976. “Probabilities of Conditionals and Conditional Probabilities.” *Philosophical Review* 85 (3): 297–315.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Oesterheld, Caspar, and Vincent Conitzer. 2021. “Extracting Money from Causal Decision Theorists.” *Philosophical Quarterly* 71 (4): pqaa086.

Pearl, Judea. 2009. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press.

Wikipedia contributors. “Causal Decision Theory.” Wikipedia, revision 1381555528, October 23, 2026. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528.