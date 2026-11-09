# Causal Decision Theory: Choosing Causes, Not Signs

A decision can be good news without being a good intervention. Someone who declines a medical treatment might thereby reveal that they were healthy all along; declining does not necessarily make them healthy. Conversely, accepting treatment may be evidence of serious illness while still improving the patient’s prospects.

Causal decision theory—CDT—makes this distinction central. It recommends the available action with the best expected **causal consequences**, rather than the action whose occurrence would be the most encouraging evidence.

That slogan leaves substantial work to do. What changes when we hypothetically change an action? What stays fixed? How should uncertainty about causal structure enter the calculation? And does choosing a policy differ from choosing an individual act?

The supplied reference presents CDT’s counterfactual formulation and several disputes surrounding it. Below, I distinguish that core account from a structural-model interpretation that makes the calculations more operational.

## 1. Expected utility over counterfactual outcomes

Let \(\mathcal A\) be the available actions, \(E=e\) the agent’s current evidence, and \(u(o)\) the utility of outcome \(o\). Outcomes should include everything the agent values: benefits, costs, risks, effects on others, and any intrinsic value or disvalue of acting a certain way. Assume a finite problem, or otherwise that the relevant expectations exist.

Write \(O_a\) for the outcome that would occur **if the agent performed action \(a\)**. CDT evaluates

\[
V_C(a\mid e)
=
\mathbb E[u(O_a)\mid E=e]
=
\sum_o P(O_a=o\mid e)\,u(o)
\]

and recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid e).
\]

This expresses the Gibbard–Harper formulation reported in the reference:

\[
U(A)=\sum_j P(A\mathbin{\to}O_j)D(O_j).
\]

The arrow should be read as a counterfactual conditional: *if \(A\) were performed, \(O_j\) would occur*. Despite the reference’s informal wording about necessary implication, this is not ordinary logical entailment or the material conditional.

For comparison, evidential decision theory evaluates

\[
V_E(a\mid e)
=
\sum_o P(O=o\mid A=a,e)\,u(o).
\]

The difference is between:

- imagining that an action is performed while assessing its consequences; and
- learning that the action is performed and updating one’s beliefs accordingly.

These need not yield the same probabilities.

A useful representation introduces an uncertain causal state \(S\), specifying how each action would turn out:

\[
O_a=g(a,S).
\]

Then CDT uses

\[
V_C(a\mid e)
=
\sum_s P(s\mid e)\,u(g(a,s)).
\]

Under the consistency assumption that the actual outcome is \(g(A,S)\), EDT instead uses

\[
V_E(a\mid e)
=
\sum_s P(s\mid A=a,e)\,u(g(a,s)).
\]

CDT holds the distribution of causal states fixed across the comparison. It does **not** assert that actions and states are statistically independent. Their possible dependence is precisely why the two calculations can disagree.

## 2. An operational interpretation: intervene on a causal model

The reference emphasizes that CDT itself does not provide a universally accepted algorithm for assigning counterfactual probabilities. One useful implementation is a structural causal model. This is additional modeling machinery, not a definition supplied by the article.

Suppose variables obey equations

\[
X_i=f_i(\operatorname{Pa}_i,Z_i),
\]

where \(\operatorname{Pa}_i\) denotes the causal parents of \(X_i\), and \(Z_i\) represents background influences. Let \(H\) describe uncertainty about the equations themselves. Current evidence gives a posterior distribution \(P(H,Z\mid e)\).

To evaluate an action \(a\):

1. Retain that posterior over background circumstances and causal models.
2. Replace the ordinary equation determining the action with \(A:=a\).
3. Recompute the consequences using the remaining equations.
4. Average their utilities.

Formally,

\[
V_C(a\mid e)
=
\sum_h\int
u\!\left(O^{h,a}(z)\right)
\,dP(h,z\mid e).
\]

This is commonly written

\[
V_C(a\mid e)
=
\mathbb E[u(O)\mid \operatorname{do}(A=a),e],
\]

with \(e\) understood here as evidence available before the contemplated action.

The intervention removes the action’s dependence on its ordinary causes. It does not erase relevant knowledge about those causes, nor does it freeze downstream consequences.

For example, if disease severity influences both treatment choice and survival, intervening on treatment breaks its dependence on severity while retaining treatment’s effect on survival. If treatment also causes side effects, those remain part of the calculation.

This yields a crucial distinction:

> Holding background circumstances fixed does not mean holding the outcome fixed.

CDT also accommodates uncertainty about causal structure. If a drug might help, harm, or have no effect, the agent averages over those hypotheses using their current probabilities. “Hold fixed” means use the same uncertainty distribution when comparing hypothetical actions—not pretend to know the causal facts.

When action selection is unconfounded, CDT and EDT can agree. Under consistency, a sufficient condition is

\[
A\perp O_a\mid E
\]

for every action \(a\). Then

\[
P(O_a=o\mid e)=P(O=o\mid A=a,e).
\]

Thus the disagreement is not about whether conditional probabilities are legitimate. It concerns which conditional probabilities answer the decision question.

## 3. Common causes: the King David example

The reference illustrates this distinction with King David. His fixed character influences both his tendency to act unjustly and his vulnerability to revolt. The contemplated unjust act is stipulated not to cause revolt.

Here is a numerical version; the numbers are illustrative additions.

Let \(C\) mean that David is charismatic, and \(S\) that he summons Bathsheba. Suppose

\[
P(C)=\tfrac12,
\qquad
P(S\mid C)=0.1,
\qquad
P(S\mid\neg C)=0.9.
\]

Let revolt probabilities be

\[
P(R\mid C)=0.1,
\qquad
P(R\mid\neg C)=0.7,
\]

with summoning causally irrelevant to revolt once character is fixed.

Summoning is evidence of lacking charisma. Bayes’ rule gives

\[
P(R\mid S)=0.64,
\qquad
P(R\mid\neg S)=0.16.
\]

But intervening on summoning leaves character unchanged:

\[
P(R\mid\operatorname{do}(S))
=
P(R\mid\operatorname{do}(\neg S))
=
0.4.
\]

For illustration, assign summoning a net utility benefit of \(10\) and revolt a cost of \(100\). CDT calculates

\[
V_C(S)=10-100(0.4)=-30,
\qquad
V_C(\neg S)=-100(0.4)=-40.
\]

EDT calculates

\[
V_E(S)=10-100(0.64)=-54,
\qquad
V_E(\neg S)=-100(0.16)=-16.
\]

Hence the disagreement.

This is not a moral endorsement of the act. Its injustice, effects on Bathsheba, and all other morally relevant consequences belong in the utility function. The example isolates one issue: refusing an act does not improve an unchangeable character merely because refusal would be evidence of good character.

## 4. Newcomb’s problem: dominance versus predictive success

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either \(\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box if it predicted that the player would take only that box; otherwise it left it empty.

Let \(F\in\{0,1\}\) indicate whether the opaque box is full. With monetary utility, the counterfactual payoffs are

\[
u(\text{one box},F)=10^6F,
\]

\[
u(\text{two boxes},F)=10^6F+1000.
\]

On the standard causal interpretation, the present action cannot alter the earlier filling. Therefore, for the same current probability \(q=P(F=1\mid e)\),

\[
V_C(\text{one})=10^6q,
\qquad
V_C(\text{two})=10^6q+1000.
\]

CDT recommends two-boxing. It gains \(\$1{,}000\) in either fixed filling state. Indeed, the dominance argument requires only that more money be preferable, not risk neutrality.

For an evidential calculation, suppose specifically that

\[
P(F=1\mid\text{one})=0.99,
\qquad
P(F=1\mid\text{two})=0.01.
\]

These conditional assumptions are stronger than merely saying that aggregate prediction accuracy is 99%. They yield

\[
V_E(\text{one})=\$990{,}000,
\qquad
V_E(\text{two})=\$11{,}000.
\]

EDT recommends one-boxing.

CDT need not deny predictive accuracy. It distinguishes the prediction’s correlation with the action from the action’s causal effect on the prediction. The controversy is whether this distinction should control rational choice when one-boxers predictably earn much more.

Nor does two-boxing logically guarantee only \(\$1{,}000\): a two-boxer can receive \(\$1{,}001{,}000\) if the predictor errs.

## 5. Policies, commitments, and correlated agents

An action and a policy are different objects. A policy specifies actions across possible observations and times:

\[
\pi_t:h_t\longmapsto \Delta(\mathcal A_t),
\]

where \(h_t\) is the available history and \(\Delta(\mathcal A_t)\) permits randomization.

A causal policy evaluation replaces the relevant action-generating equations with that policy and computes

\[
V_C(\pi\mid e)
=
\mathbb E[u(O^\pi)\mid e].
\]

This extends the operational model above. But one must identify what adopting the policy actually changes.

Suppose, before the Newcomb predictor acts, the player can install a visible, binding one-boxing commitment. If the predictor responds to that commitment, there is an ordinary causal path

\[
\text{commitment}\longrightarrow
\text{prediction}\longrightarrow
\text{box contents}.
\]

CDT can endorse committing to one-boxing. Later, without the commitment, it can recommend two-boxing once the contents are fixed.

There is no arithmetic contradiction: the interventions occur at different times. Nevertheless, this distinction creates questions about commitment, future reconsideration, and whether a merely announced plan will be carried out.

Calling something “policy selection” does not itself make it influence past predictions. Such influence requires an appropriate causal mechanism.

Similar issues arise when facing a highly correlated opponent. Consider a prisoner’s dilemma with payoffs

\[
u(C,C)=3,\quad u(D,C)=5,\quad
u(C,D)=0,\quad u(D,D)=1.
\]

If the opponent’s cooperation probability \(q\) is causally unaffected by the present action, then

\[
V_C(C)=3q,
\qquad
V_C(D)=5q+(1-q)=1+4q.
\]

Defection wins for every \(q\).

This remains true if the opponent is a psychological twin whose action strongly correlates with yours. Correlation alone does not create an outgoing causal arrow from your action to theirs. However, an intervention on a shared mechanism that actually controls both agents would be a different decision problem.

## 6. What the formalism leaves unsettled

### Choosing the counterfactuals

The reference discusses Lewis’s *imaging*: move the probability assigned to each world to a suitably closest world in which the contemplated action occurs.

The difficulty is specifying “closest.” Should changing an action preserve its ordinary causes, alter them, or alter other events correlated with it?

Structural intervention supplies one disciplined answer: preserve background circumstances, replace the action equation, and propagate effects forward. This clarifies many ordinary problems. It does not establish that every philosophical counterfactual must have that interpretation.

The source also reports concerns about regress in specifying counterfactual beliefs. An explicit structural model avoids leaving every calculation to an unspecified similarity judgment, but its causal assumptions still require justification.

### Learning about oneself

Egan’s “Psychopath Button,” discussed in the reference, makes the evidential problem personal. Paul can press a button that kills all psychopaths. He values their removal but strongly prefers living with them to dying. He also believes that only a psychopath would press.

Let

\[
r=P(\text{Paul is a psychopath}\mid e).
\]

For a simplified utility model, suppose pressing gives a non-psychopath benefit \(B>0\), while killing Paul gives him utility change \(-L\), with \(L>0\). Relative to not pressing,

\[
V_C(\text{press})=(1-r)B-rL.
\]

The fixed-credence calculation recommends pressing exactly when

\[
r<\frac{B}{B+L}.
\]

But Paul’s willingness to press may itself be strong evidence that \(r\) is high. Is it legitimate to evaluate pressing while ignoring that implication?

The reference reports Joyce’s response that CDT can incorporate information about one’s inclinations as evidence. In the present framework, genuinely learning about an inclination can update \(e\), thereby changing \(r\).

The unresolved issue is how deliberation itself supplies information. One must distinguish:

- receiving new evidence about one’s psychology;
- merely supposing an action for comparison;
- discovering what one has decided.

Automatically conditioning on every hypothetical action turns the calculation toward EDT. Never learning from deliberation seems unduly restrictive. The reference does not settle a unique updating procedure.

### Profitable-looking choices that lose money

The “Adversarial Offer” sharpens this challenge. A seller offers two boxes for \(\$1\) each; the buyer may purchase at most one. Yesterday, the seller placed \(\$3\) in each box she predicted the buyer would not acquire.

At least one box contains \(\$3\). Thus, writing their contents as \(M_L,M_R\),

\[
\mathbb E[M_L\mid e]+\mathbb E[M_R\mid e]\ge 3.
\]

Under the standard fixed-content causal interpretation, at least one purchase has expected net value at least

\[
\frac32-1=\$0.50.
\]

CDT therefore recommends buying some box rather than neither.

Yet consider a population of these purchases in which the seller predicts the buyer’s actual choice correctly 75% of the time. A correct prediction leaves the purchased box empty; an incorrect prediction leaves it containing \(\$3\). Average net profit is therefore

\[
0.75(-1)+0.25(2)=-\$0.25.
\]

The causal calculation and the observed return use different distributions: one holds the filling-state distribution fixed across alternatives; the other reflects the dependence between actual purchases and predictions. Critics argue that repeatedly endorsing such transactions is a serious defect.

An unpredictable private randomizer would change the prediction assumptions. It cannot simply be introduced while retaining all the original claims about predictive success.

These examples do not reveal an elementary algebraic contradiction in CDT. They challenge whether its counterfactual comparison captures everything rational deliberation should respect.

## 7. A practical method

For an unfamiliar problem, the structural interpretation suggests the following procedure:

1. **Specify the decision:** an immediate act, a commitment, or an implementable policy.
2. **Specify utilities:** include costs, externalities, and intrinsic concerns.
3. **Record current evidence:** including genuine information about dispositions.
4. **Model dependencies:** distinguish common causes, causal effects, and predictive correlations.
5. **Intervene on each alternative:** retain background uncertainty while recomputing consequences.
6. **Compare expected utilities:** then test sensitivity to disputed causal assumptions.

If reasonable models disagree about what an intervention changes, report that dependence rather than presenting CDT as delivering an assumption-free verdict.

### Sources

Primary source: Wikipedia contributors, “Causal decision theory,” supplied [revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), CC BY-SA 4.0.

Principal works discussed in that source include Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1981); Lewis, “Causal Decision Theory” (1981); Egan, “Some Counterexamples to Causal Decision Theory” (2007); Joyce, “Regret and Instability in Causal Decision Theory” (2012); and Oesterheld and Conitzer, “Extracting Money from Causal Decision Theorists” (2021).

## Conclusion

CDT asks what an available intervention would accomplish, not merely what its occurrence would reveal. Its central discipline is to separate causal consequences from diagnostic evidence while taking uncertainty seriously. Applied carefully, this gives a powerful procedure for ordinary decisions, policies, and commitments. Its hardest cases concern the agent’s own predictability: when deliberation reveals information about the deliberator, specifying what to hold fixed becomes part of the philosophical problem, not merely a computational detail.