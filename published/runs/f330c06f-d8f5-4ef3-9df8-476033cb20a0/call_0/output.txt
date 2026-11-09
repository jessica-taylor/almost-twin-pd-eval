# Causal Decision Theory and the Logic of Intervention

Causal decision theory (CDT) is a school of thought in decision theory that says, roughly: choose the action that would causally produce the best expected outcome. The contrast is with evidential decision theory (EDT), which says: choose the action that would be the best news if you learned that you had done it. The Wikipedia article on causal decision theory summarizes the distinction by saying that CDT recommends the action with the best expected causal consequences, whereas EDT recommends the action that is most indicative of good outcomes (Wikipedia contributors, 2026).

That distinction sounds simple, but it becomes subtle as soon as actions are correlated with outcomes without causing them. A choice may be evidence that a good or bad outcome will occur, even though the choice does not bring that outcome about. CDT tries to evaluate actions by asking what would happen if the action were performed, not merely what one should expect upon learning that the action was performed. This essay gives a fairly explicit formulation of CDT, explains how it evaluates actions and policies, and discusses how it handles dependence, prediction, and counterfactual reasoning. I also indicate where the source leaves matters under-specified and propose a natural operational interpretation using modern interventionist causal language.

---

## 1. Expected utility: evidential versus causal

Suppose an agent can choose among actions \(A_1,\dots,A_n\), and the possible outcomes are \(O_1,\dots,O_m\). Let \(D(O_j)\) be the desirability or utility of outcome \(O_j\). The agent has probabilistic beliefs about the world.

Evidential decision theory evaluates an action by conditional probability:

\[
V_{\text{EDT}}(A_i)=\sum_j P(O_j \mid A_i)D(O_j).
\]

Here \(P(O_j \mid A_i)\) is the ordinary conditional probability of \(O_j\) given that the action \(A_i\) is taken. EDT treats the action as a piece of evidence. If doing \(A_i\) would make good news likely, EDT favors \(A_i\).

The reference article gives the classic causal formulation due to Gibbard and Harper (1981):

\[
U(A)=\sum_j P(A \to O_j)D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(A \to O_j)\) is the probability of the counterfactual: if \(A\) were performed, \(O_j\) would occur. The arrow here should not be read as a material conditional or as ordinary conditional probability. It is meant to express a causal or counterfactual dependence: what would follow from performing \(A\).

A useful way to rewrite the CDT formula, using contemporary notation, is:

\[
V_{\text{CDT}}(A_i)=\sum_j P(O_j \mid do(A_i))D(O_j),
\]

where \(do(A_i)\) means “intervene to set the action variable to \(A_i\).” This notation is not used in the source article, but it captures the intended difference between counterfactual probability and conditional probability. Lewis proved that the probability of a conditional need not equal the corresponding conditional probability; if they always coincided, CDT would collapse into EDT (Lewis, 1976, as cited in Wikipedia contributors, 2026).

A deterministic version is sometimes clearer. Let \(W\) be a space of possible worlds, with credence \(P(w)\). For each action \(A\), let \(O_A(w)\) be the outcome that would occur if action \(A\) were performed in world \(w\). Then CDT evaluates

\[
V_{\text{CDT}}(A)=\sum_{w} P(w)D(O_A(w)).
\]

This says: take your current probability distribution over worlds, ask what outcome the action would produce in each world, and take the expectation. The crucial feature is that the action is treated as an intervention on the world, not merely as information about the world.

---

## 2. What CDT holds fixed, and what it changes

CDT’s central operation is: hold fixed the relevant causal structure and the agent’s beliefs about exogenous facts, then evaluate what happens when the action variable is set by the agent.

Suppose there is a state variable \(S\), an action variable \(A\), and an outcome variable \(O\). If \(S\) is a common cause of both \(A\) and \(O\), then \(A\) and \(O\) may be correlated even if \(A\) does not cause \(O\). EDT will see that correlation and treat \(A\) as evidence about \(O\). CDT will not, unless there is a causal path from \(A\) to \(O\).

In a simple causal model, we might have:

\[
S \to A,\qquad S \to O,\qquad A \to O.
\]

If the arrow \(A \to O\) is present, then the action causally affects the outcome. If it is absent, then the action is merely correlated with the outcome through \(S\). CDT evaluates the action by removing the arrows into \(A\) and setting \(A\) directly. In graphical causal-model language, this is the intervention \(do(A=a)\). Under a standard backdoor condition, if \(S\) screens off the confounding between \(A\) and \(O\), then

\[
P(O=o \mid do(A=a))
=
\sum_s P(S=s)P(O=o \mid A=a,S=s).
\]

Thus CDT uses the agent’s unconditional or prior probabilities over the relevant background states \(S\), not probabilities conditioned on the action itself. This is the formal expression of the idea that CDT “holds fixed” the agent’s background views about the causal structure.

The source article notes that CDT does not itself specify an algorithm for computing the probabilities of counterfactuals. One proposal mentioned there is Lewis’s “imaging” technique: to evaluate \(P(A \to O)\), move probability mass from each possible world to the closest possible world in which \(A\) is true, then see how much mass lands in \(O\)-worlds. But this requires an account of similarity between possible worlds, and, as the source notes, it may lead to regress because we must ask what we would believe if we were certain of \(A\) (Shaffer, 2009, as cited in Wikipedia contributors, 2026).

A reasonable operational interpretation, which I add to the source rather than find explicitly stated there, is to model the agent’s beliefs using structural causal equations. An agent specifies variables, structural equations, and a probability distribution over exogenous noise variables. To evaluate an action \(A=a\), the agent replaces the structural equation for \(A\) with the constant equation \(A:=a\), leaves the other equations unchanged, and computes the resulting distribution over outcomes. This gives a concrete meaning to \(P(O=o \mid do(A=a))\). It does not solve every philosophical problem—choosing the right causal model can itself be difficult—but it makes CDT usable in many ordinary decision problems.

---

## 3. Common causes: King David and Bathsheba

The reference article gives an example due to Gibbard and Harper involving King David. David wants to summon Bathsheba, but fears that doing so may provoke revolt. He knows that kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. David does not know which type he is. Summoning Bathsheba would be unjust, and unjust acts themselves do not cause revolts. Rather, uncharismatic kings are prone to revolt because of their ignoble bearing.

Let \(C\) be David’s charisma type, \(A\) the action of summoning Bathsheba, and \(R\) a successful revolt. The causal structure is approximately:

\[
C \to A,\qquad C \to R.
\]

There is no direct causal arrow \(A \to R\), because the unjust act itself does not cause revolt. The act is evidence of uncharismatic character, and uncharismatic character causes revolt.

EDT evaluates:

\[
V_{\text{EDT}}(A)=\sum_j P(O_j \mid A)D(O_j).
\]

Because summoning Bathsheba is evidence that David is uncharismatic, it raises the conditional probability of revolt. If the expected cost of revolt is large enough, EDT recommends abstaining.

CDT evaluates:

\[
V_{\text{CDT}}(A)=\sum_j P(O_j \mid do(A))D(O_j).
\]

Under the intervention \(do(A=\text{summon})\), David’s charisma type is not changed. If the act does not causally affect revolt, then the probability of revolt under the intervention is just the background probability associated with David’s unknown type:

\[
P(R \mid do(A=\text{summon}))
=
P(R).
\]

More precisely, if charisma is the only relevant background variable,

\[
P(R \mid do(A))
=
\sum_c P(C=c)P(R \mid C=c).
\]

The direct benefit of summoning Bathsheba is added to this background revolt risk. If the benefit of summoning is positive and the revolt risk is unchanged by the action, CDT recommends summoning. The source article says exactly this: EDT recommends abstention, while CDT recommends sending for her, because charisma cannot be changed by the act.

This example illustrates the essential difference. EDT asks, “What does this action indicate?” CDT asks, “What would this action bring about?”

---

## 4. Newcomb’s problem

Newcomb’s problem is the most famous test case. A predictor has predicted whether the agent will take one box or two. Box A is transparent and contains \$1,000. Box B is opaque. If the predictor predicted one-boxing, Box B contains \$1,000,000. If the predictor predicted two-boxing, Box B contains nothing. The predictor is highly reliable, perhaps 99% accurate. The agent chooses after the prediction has been made.

Let the possible contents of Box B be \(F\) for full and \(E\) for empty. The payoffs are:

| Action | Box B full | Box B empty |
|---|---:|---:|
| One-box | \$1,000,000 | \$0 |
| Two-box | \$1,001,000 | \$1,000 |

Conditional on the state of Box B, two-boxing yields \$1,000 more than one-boxing. If Box B is full, two-boxing gives \$1,001,000 instead of \$1,000,000. If Box B is empty, two-boxing gives \$1,000 instead of \$0.

CDT treats the content of Box B as already fixed when the agent chooses. The predictor’s prediction is in the past, and the present action does not causally affect it. Therefore CDT evaluates:

\[
V_{\text{CDT}}(\text{two-box})
=
P(F)\cdot 1{,}001{,}000 + P(E)\cdot 1{,}000,
\]

\[
V_{\text{CDT}}(\text{one-box})
=
P(F)\cdot 1{,}000{,}000 + P(E)\cdot 0.
\]

The difference is

\[
V_{\text{CDT}}(\text{two-box})-V_{\text{CDT}}(\text{one-box})
=
P(F)\cdot 1{,}000 + P(E)\cdot 1{,}000
=
1{,}000.
\]

So CDT recommends two-boxing regardless of the prior probability that Box B is full, provided the prediction is already fixed and the current choice does not causally affect it.

EDT reasons differently. One-boxing is strong evidence that the predictor predicted one-boxing, so one-boxing is strong evidence that Box B is full. Two-boxing is strong evidence that Box B is empty. If the predictor is sufficiently reliable, EDT gives:

\[
V_{\text{EDT}}(\text{one-box}) \approx 1{,}000{,}000,
\]

\[
V_{\text{EDT}}(\text{two-box}) \approx 1{,}000.
\]

So EDT recommends one-boxing.

The source article says that philosophers often prefer CDT to EDT, but Newcomb’s problem remains controversial. Some regard two-boxing as the clearly causal answer; others regard one-boxing as the answer that actually gets the million dollars. The disagreement is not merely mathematical; it depends on what one thinks a rational decision is supposed to track: causal influence or successful news.

---

## 5. Policies, information, and dependence

So far I have discussed one-shot actions. But decision problems often involve policies: rules that map observations, evidence, or intermediate states to actions. CDT can be extended to policies by treating the adoption of a policy as an intervention.

Let \(\Pi\) be a policy variable. A policy \(\pi\) might say: if observation \(e\) occurs, take action \(\pi(e)\). If the observation is not itself affected by the policy, a simple CDT evaluation is:

\[
V_{\text{CDT}}(\pi)
=
\sum_e P(e)\sum_o P(o \mid do(A=\pi(e)), e)D(o).
\]

If the policy affects what observations are obtained, or affects earlier variables such as predictors, then the intervention should be applied to the policy as a whole:

\[
V_{\text{CDT}}(\pi)=\mathbb{E}[D(O)\mid do(\Pi=\pi)].
\]

This is my operational gloss on the source’s more abstract counterfactual formulation. It says: compare policies by asking what would happen if the agent implemented each policy.

This framework helps clarify how CDT treats dependencies.

1. **Direct causal dependence.** If the action causally affects the outcome, CDT counts that effect. Eating a good apple causes happiness; pressing a working button causes an explosion; investing in a productive project causes profit.

2. **Common-cause dependence.** If action and outcome share a common cause, CDT does not count the mere correlation as a causal reason. David’s summoning is evidence of uncharismatic character, but it does not cause revolt. CDT holds the common cause fixed.

3. **Predictive dependence.** If a predictor has already predicted the action, CDT usually treats the prediction as fixed at the time of action. In Newcomb’s problem, the predictor’s prediction is prior to the choice, so the choice does not causally change the prediction. But if the predictor will observe the choice before acting, then the action may causally influence the outcome through the predictor. In that case, CDT can recommend one-boxing. The recommendation depends on the causal structure, not on the mere presence of prediction.

4. **Evidence about one’s own tendencies.** The source notes Joyce’s defense that CDT can take information about what one is likely to do as evidence. This is plausible if the information is treated as evidence about background variables. For example, if you learn that you are the kind of person who usually defects in prisoner’s dilemmas, that may be evidence about your dispositions, which may correlate with other agents’ predictions. CDT can update its priors over background states using that evidence.

However, there is a delicate point. If the agent conditions on “I will probably do \(A\)” while deciding between \(A\) and \(B\), the agent may build the answer into the evidence. A reasonable operational rule, not explicitly in the source but consistent with interventionist CDT, is this: use all admissible evidence available before the intervention, but do not treat the candidate action itself as ordinary evidence when comparing alternatives. Equivalently, evaluate each action under the same posterior over exogenous variables, then apply the intervention \(do(A=a)\). For policies, evaluate the policy as a whole rather than conditioning on each act token separately. This avoids some self-fulfilling circularity, though it does not remove all controversy.

---

## 6. Vagueness and the problem of counterfactuals

The source article correctly emphasizes that CDT is not a complete algorithm. It gives a decision rule expressed in terms of counterfactual probabilities, but it does not say exactly how those probabilities should be computed. Lewis’s imaging is one proposal: move probability mass from each world to the closest world where the action is performed. But imaging requires a similarity ordering over possible worlds, and the source notes a possible regress involving what one would believe if one were certain of the action.

This is not a mere technical inconvenience. Different accounts of counterfactuals can yield different causal expected utilities. If an agent believes that performing \(A\) would be evidence that some hidden variable has a certain value, should the counterfactual evaluation include that evidence? CDT says no if the dependence is merely evidential, but drawing the line requires a causal model.

The interventionist interpretation I have suggested makes the theory more precise. Given a structural causal model, counterfactuals can be evaluated by modifying equations. For example, if the model contains variables \(S,A,O\) with equations

\[
S := f_S(U_S),
\]
\[
A := f_A(S,U_A),
\]
\[
O := f_O(A,S,U_O),
\]

then the intervention \(do(A=a)\) replaces the second equation with

\[
A := a.
\]

The resulting distribution of \(O\) is the CDT probability distribution over outcomes. If the agent has observed evidence \(e\), one can first update over the exogenous variables \(U_S,U_A,U_O\) conditional on \(e\), then perform the intervention. This gives a posterior counterfactual expected utility:

\[
V_{\text{CDT}}(a \mid e)=\mathbb{E}[D(O_a)\mid e].
\]

Again, this is an addition to the source, but it is a natural way to make CDT operational.

---

## 7. Counterexamples and instability

The source article discusses several alleged counterexamples to CDT. These are important because they show that CDT’s treatment of prediction and self-diagnostic evidence can be unintuitive.

### Death in Damascus

In the Death in Damascus scenario, Death predicts where you will be tomorrow and goes there. You meet Death in Damascus, and Death expresses surprise, saying that he has an appointment with you tomorrow in Aleppo. You consider fleeing to Aleppo.

If Death is a reliable predictor, your action is strongly correlated with Death’s prediction. If you flee, Death probably predicted that you would flee. If you stay, Death probably predicted that you would stay. CDT may treat Death’s prediction as already fixed and say that your present action cannot causally change it. But then the agent’s deliberation becomes unstable. If the agent comes to believe that Death predicted flight, staying looks better; if the agent comes to believe that Death predicted staying, fleeing looks better.

The source cites Egan’s criticism that CDT fails to process the correlation and may make irrational decisions. In some variants, following CDT can lead an agent to voluntarily lose money or forgo a guaranteed payoff. The exact diagnosis depends on how one models prediction, time, and the agent’s evidence about its own future action. The source leaves the operational details open, but the general problem is clear: CDT’s insistence on holding fixed background dependency hypotheses can make it blind to the evidential significance of its own choice.

### The Adversarial Offer

Oesterheld and Conitzer’s Adversarial Offer, as described in the source, involves two boxes. The buyer may purchase one box or none, but not both. Each box costs \$1. The seller put \$3 in each box that she predicted the buyer would not acquire. The seller’s prediction is believed to be accurate with probability \(0.75\).

The source says that CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value, which exceeds the \$1 cost. Hence CDT buys a box. But the seller profits.

This case is subtle because it mixes logical constraints with prediction. The buyer cannot buy both boxes, so at least one box will not be acquired. If the seller is accurate, that unacquired box probably contains money. But the box the buyer chooses is likely one the seller predicted the buyer would acquire, and therefore likely empty. A simple CDT calculation that averages over boxes without properly conditioning on the chosen box may recommend buying. A more detailed interventionist model might give a different answer depending on how the seller’s prediction is causally related to the buyer’s choice. The source presents the case as a counterexample, but it also exposes the need for a precise account of counterfactual computation.

### The Psychopath Button

Egan’s psychopath button case is especially vivid. Paul is considering pressing a button that would kill all psychopaths. He thinks a world without psychopaths would be much better. But Paul is confident that only a psychopath would press such a button. He strongly prefers living in a world with psychopaths to dying.

Let \(S\) be the proposition that Paul is a psychopath, and let \(B\) be the action of pressing the button. The intuitive evidential reasoning is:

\[
P(S \mid B) \text{ is high}.
\]

If Paul presses the button, that is strong evidence that he is a psychopath, and therefore strong evidence that he will die. EDT says not to press.

CDT, however, evaluates the intervention \(do(B)\). If Paul’s prior probability of being a psychopath is low, and if pressing the button does not causally make him a psychopath, then CDT may assign high expected utility to pressing: it causes psychopaths to die, and Paul probably is not one. The intervention breaks the ordinary dependence between psychopathy and pressing. The source quotes Egan’s claim that CDT endorses pressing even though “pretty much everyone” agrees Paul should not.

This example highlights Egan’s general diagnosis: CDT holds fixed the agent’s unconditional credences in dependency hypotheses, even when the agent’s action gives strong evidence about which dependency hypothesis is true. If Paul’s pressing is a symptom of psychopathy, CDT ignores the symptomatic evidence. Whether that is a fatal flaw or a hard-nosed commitment to causal relevance is one of the central disputes in modern decision theory.

---

## 8. What CDT gets right, and where it remains contested

CDT captures an attractive idea: rational action should aim at controlling the future, not merely at being correlated with good news. If an action cannot change some bad fact, it is often unreasonable to avoid the action merely because it would be evidence of that bad fact. If a medical test would reveal that you are sick, avoiding the test does not make you healthy. If a predictor has already placed money in a box, taking an extra visible \$1,000 does not remove the million.

But CDT also faces hard cases involving prediction, self-knowledge, and policies. When an agent’s action is strongly predicted by another agent, or when the action reveals the agent’s type, the distinction between causal influence and evidence becomes controversial. EDT says that rational agents should choose the action that would be good news. CDT says that rational agents should choose the action that would cause good outcomes. In Newcomb-like cases, those recommendations diverge.

The source article also notes that Oesterheld and Conitzer argue CDT agents can be subjected to diachronic Dutch books and can voluntarily lose money in certain predictor problems. Whether this disproves CDT or merely shows that some forms of CDT are dynamically inconsistent is a further question. The source does not settle it.

A defensible practical version of CDT, in my view, should include at least the following components:

1. A specification of the relevant variables and causal structure.
2. A probability distribution over exogenous uncertainty.
3. An intervention rule: evaluate actions by setting the action variable, not by conditioning on it.
4. A policy rule: evaluate policies by intervening on the policy variable.
5. A rule for admissible evidence: update on evidence before the intervention, but do not treat the candidate action itself as ordinary evidence when comparing alternatives.

This gives CDT enough structure to be applied to unfamiliar cases. It also makes clear that CDT is not a purely formal formula detached from causal modeling. The hard work often lies in deciding what depends causally on what.

---

## Conclusion

Causal decision theory says that rational choice is guided by expected causal consequences. Formally, it replaces EDT’s conditional probabilities \(P(O_j \mid A)\) with counterfactual or interventionist probabilities \(P(O_j \mid do(A))\). In common-cause cases such as Gibbard and Harper’s King David example, this means ignoring correlations that are merely evidential. In Newcomb’s problem, it means two-boxing because the current choice does not causally alter the predictor’s earlier prediction.

The theory is attractive because it connects decision-making to intervention: choose what would actually make a difference. But it is incomplete without an account of counterfactuals. Lewis’s imaging is one proposal; structural causal models provide a more modern operational interpretation. The source’s counterexamples—Death in Damascus, the Adversarial Offer, and the psychopath button—show that CDT can give counterintuitive advice when actions are predictive of the agent’s own type or future behavior. These cases remain philosophically contested. Still, if one wants a usable decision procedure, CDT can be made reasonably precise by evaluating actions and policies under interventions, holding fixed the causal structure and the agent’s admissible background evidence.

---

## References

Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Belief, Decision, Chance, and Time* (pp. 153–190).

Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review, 85*(3), 297–315.

Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy, 59*(1), 5–30.

Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review, 116*(1), 93–114.

Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly, 71*(4), pqaa086.

Wikipedia contributors. (2026). Causal decision theory. In *Wikipedia, The Free Encyclopedia*. Revision 1381555528. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528