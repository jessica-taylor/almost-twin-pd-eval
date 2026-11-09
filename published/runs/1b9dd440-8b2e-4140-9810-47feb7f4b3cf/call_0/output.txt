# Evidential Decision Theory: Choosing What Would Be Good News

A decision can matter in two ways. It can change what happens, and it can indicate what is already true—or what another, correlated agent will do. Usually these considerations align. Buying a reliable umbrella both helps keep you dry and predicts that you will stay dry. But some decision problems separate causal influence from evidential significance.

**Evidential decision theory** (EDT) evaluates actions by their evidential significance: choose the action conditional on which expected utility is greatest. The supplied reference article describes this as maximizing an action’s “news value.” The question is not merely, “What would this action cause?” but, “How good should I expect the world to be, given that I perform it?”

That principle is mathematically straightforward. Applying it requires care about what is being conditioned on, how beliefs about one’s own choices are formed, and whether the object of evaluation is an immediate act or a whole policy.

## 1. The basic rule

Let:

- \(\mathcal A\) be a finite set of available actions;
- \(X\) be the random variable representing the agent’s action;
- \(O\) be the eventual outcome;
- \(u(O)\) be its utility;
- \(K\) be the agent’s information at the time of evaluation.

EDT assigns action \(a\) the value

\[
V_K(a)=\mathbb E[u(O)\mid X=a,K].
\]

For a discrete outcome space,

\[
V_K(a)=\sum_o P(O=o\mid X=a,K)\,u(o).
\]

It recommends any action satisfying

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_K(a).
\]

This is the reference article’s central definition, with the background information \(K\) made explicit.

Utilities need not represent money. They may encode health, other people’s welfare, risk aversion, or preferences concerning the action itself. Outcomes must be described richly enough to capture everything the agent values. If accepting a payment involves breaking a promise, for example, that feature should not disappear from the utility model.

A useful equivalent representation introduces a background state \(S\), sufficiently detailed that the utility obtained from action \(a\) in state \(s\) is \(u(a,s)\). Then

\[
V_K(a)=\sum_s P(S=s\mid X=a,K)\,u(a,s).
\]

This exposes EDT’s distinctive feature: **different actions can induce different conditional distributions over the same background states**.

Learning that I took an umbrella may suggest that I saw signs of rain. Learning that I chose a particular answer may suggest that a highly accurate predictor anticipated that answer. EDT retains such evidential relationships rather than discarding them merely because they are noncausal.

The theory does not recommend maximizing pleasant feelings about the news. The news matters only through its implications for valued outcomes.

## 2. Conditioning is not intervention

The reference contrasts EDT with causal decision theory (CDT), which evaluates counterfactual outcomes under each action. In a structural causal model, a common operational representation is

\[
C_K(a)=\mathbb E[u(O)\mid \operatorname{do}(X=a),K].
\]

The intervention \(\operatorname{do}(X=a)\) fixes the action while severing its ordinary causal dependence on its upstream determinants. Ordinary conditioning does not sever those dependencies.

Suppose a latent variable \(T\) influences both my action \(X\) and another event \(Y\):

\[
T\longrightarrow X,
\qquad
T\longrightarrow Y.
\]

Observing \(X\) can provide evidence about \(T\), and therefore about \(Y\), even if \(X\) does not cause \(Y\). Thus

\[
P(Y\mid X=a,K)
\]

can differ from

\[
P(Y\mid\operatorname{do}(X=a),K).
\]

EDT uses the former distribution.

This intervention notation clarifies the comparison; it is not an additional component of EDT. The source expresses CDT using probabilities of counterfactual conditionals. Different accounts of counterfactuals require further specification, so intervention probabilities should not be identified with every conceivable counterfactual semantics.

In the background-state representation, suppose intervention on the action leaves \(S\) unchanged. CDT then evaluates

\[
C_K(a)=\sum_s P(S=s\mid K)\,u(a,s),
\]

whereas EDT uses \(P(S=s\mid X=a,K)\). A sufficient condition for agreement is

\[
S\perp X\mid K.
\]

This explains why the theories agree in many ordinary problems.

EDT nevertheless has its own answer to a “what if” question. It compares worlds in which different actions occur, weighting them through ordinary conditional probability. It does **not** claim that choosing an action changes the past. Its controversial claim is that evidence about the past can legitimately affect which present action is best.

## 3. Newcomb’s problem: the action as evidence

A predictor has already filled two boxes:

- a transparent box contains \(k=\$1{,}000\);
- an opaque box contains either \(M=\$1{,}000{,}000\) or nothing.

The opaque box is full exactly when the predictor predicted that the agent would take only that box. The agent now chooses between one-boxing and taking both boxes.

Let \(F\) mean that the opaque box is full, and define

\[
q_1=P(F\mid X=\text{one},K),
\qquad
q_2=P(F\mid X=\text{both},K).
\]

Assuming utility is linear in money,

\[
V_K(\text{one})=Mq_1,
\]

\[
V_K(\text{both})=Mq_2+k.
\]

Therefore EDT recommends one-boxing precisely when

\[
M(q_1-q_2)>k.
\]

The reference uses \(q_1=0.99\) and \(q_2=0.01\), giving

\[
V_K(\text{one})=\$990{,}000,
\qquad
V_K(\text{both})=\$11{,}000.
\]

One-boxing is overwhelmingly favored.

There is an important modeling subtlety here. Saying that the predictor is “99% accurate” overall does not by itself establish both conditional probabilities above. Aggregate accuracy depends on how frequently each action occurs. The calculation assumes the particular conditional reliability represented by \(q_1\) and \(q_2\).

Under the symmetric assumption

\[
q_1=r,\qquad q_2=1-r,
\]

one-boxing is preferred when

\[
r>\frac{1+k/M}{2}.
\]

For these stakes, the threshold is \(0.5005\).

CDT instead observes that the box contents are already fixed. In each fixed-content state, taking both boxes adds \$1,000. EDT does not dispute this state-by-state advantage. It compares different conditional mixtures of states: worlds where the agent one-boxes are much more likely to contain a full opaque box.

The disagreement is therefore not arithmetic. It concerns which distribution should evaluate an available action.

## 4. Correlated agents: the twin prisoner’s dilemma

The reference also considers two psychologically identical agents deciding separately whether to cooperate or defect. Each cares only about her own payment:

\[
\begin{array}{c|cc}
 & \text{Twin cooperates} & \text{Twin defects}\\
\hline
\text{Cooperate} & 5 & 0\\
\text{Defect} & 10 & 1
\end{array}
\]

Suppose their reasoning is perfectly correlated:

\[
P(\text{twin cooperates}\mid X=C,K)=1,
\]

\[
P(\text{twin defects}\mid X=D,K)=1.
\]

Then

\[
V_K(C)=5,\qquad V_K(D)=1,
\]

so EDT recommends cooperation.

No communication or causal influence between rooms is required. One agent’s decision is evidence about the other’s.

The recommendation depends on correlation, not simply on similarity or goodwill. Suppose instead that

\[
P(\text{twin cooperates}\mid X=C,K)=r,
\]

\[
P(\text{twin defects}\mid X=D,K)=r.
\]

Then

\[
V_K(C)=5r,
\qquad
V_K(D)=10(1-r)+r=10-9r.
\]

Cooperation is preferable exactly when

\[
r>\frac57.
\]

By contrast, if the opponent cooperates with probability \(p\) independently of the agent’s choice,

\[
V_K(C)=5p,
\qquad
V_K(D)=10p+(1-p)=1+9p,
\]

and defection wins.

EDT is thus not a general instruction to cooperate. Its recommendation depends on a sufficiently strong evidential connection between the choices. Exact psychological duplication is one proposed basis for such a connection; ordinary resemblance is not automatically enough.

## 5. The objection: choosing auspiciousness over efficacy

The reference quotes David Lewis’s criticism that EDT promotes “managing the news.” A deliberately artificial medical example makes the objection precise.

Suppose an unobserved condition \(L\) makes someone more inclined to smoke. In this hypothetical world, smoking has no harmful causal effects and provides one unit of enjoyment. Having \(L\) costs 100 utility units. Given the agent’s present information, suppose

\[
P(L\mid X=\text{smoke},K)=0.8,
\]

\[
P(L\mid X=\text{abstain},K)=0.2.
\]

Then

\[
V_K(\text{smoke})=1-100(0.8)=-79,
\]

\[
V_K(\text{abstain})=-100(0.2)=-20.
\]

EDT recommends abstention, although smoking improves utility by one unit whether or not the condition is present.

The objection is forceful: abstaining does not cure the condition. Why sacrifice enjoyment merely because abstention would be reassuring evidence?

The evidentialist response begins by distinguishing causal improvement from conditional desirability. People who abstain in the stipulated model are less likely to have the condition. EDT treats that fact as decision-relevant, just as it treats one-boxing as evidence of a full box. Whether this is rational is precisely the dispute, not something the expected-utility notation resolves.

The example also exposes the importance of \(K\). Suppose the agent knows her relevant dispositions so thoroughly that her eventual action supplies no further information about \(L\):

\[
P(L\mid X=a,K)=P(L\mid K)
\]

for both actions. The evidential penalty disappears, and EDT recommends smoking in this artificial setup.

But screening-off must be established, not assumed. Saying that a trait causes the choice does not show that the agent already knows everything about that trait. Nor does adding more information invariably eliminate an evidential dependency.

The general lesson is to calculate using the agent’s **actual information**, not a convenient description chosen to produce a favored verdict.

## 6. What beliefs about one’s own action are required?

The reference supplies a valuation formula, but not a complete account of how a deliberating agent should assign probabilities to her own possible choices. This is an important open modeling issue.

Ordinary conditioning requires

\[
P(X=a\mid K)>0.
\]

If the agent is certain she will choose \(a\), the elementary formula

\[
P(O=o\mid X=b,K)
=
\frac{P(O=o,X=b\mid K)}{P(X=b\mid K)}
\]

does not evaluate an alternative \(b\) assigned probability zero.

One operational proposal is to use a deliberative model in which every seriously available action has positive probability before the decision is settled. Another is to specify conditional beliefs about actions directly. Small-probability “tremble” models can also provide limiting values.

These are supplementary modeling choices, not consequences of the source’s formula. Different tremble models can yield different limits. One should therefore state the chosen interpretation rather than quietly manufacture conditionals for impossible events.

There is also a self-prediction problem: beliefs about what an agent will choose can depend on how she expects her decision rule to evaluate those very choices. A joint probabilistic model must be coherent, but the basic EDT formula does not itself solve every such consistency problem.

For practical purposes, the relevant probabilities should describe **this agent in this situation**, including what she knows about her deliberation. A population-level correlation between behavior and outcomes is not automatically the right conditional distribution for her decision.

## 7. From individual acts to policies

Many decisions concern contingent plans rather than isolated actions. A policy maps possible information histories to actions:

\[
\pi:H\rightarrow\mathcal A.
\]

For example, a policy might specify whether to buy insurance after receiving each possible test result.

The reference does not provide a general policy-selection theory. A natural evidential extension is

\[
V^{\mathrm{pol}}_{K_0}(\pi)
=
\mathbb E[U(\text{complete trajectory})\mid \Pi=\pi,K_0],
\]

where \(\Pi\) represents the adopted policy and \(K_0\) is the information available at the planning stage.

This is a proposal extending the source’s action-level rule. It treats adopting a policy as the action being evaluated. The conditioning event must correspond to genuinely adopting or implementing that policy, not merely describing a desirable plan.

This distinction matters in predictor problems. A predictor might respond to the agent’s general policy rather than to an unpredictable random outcome. Consequently,

\[
P(O\mid \Pi=\pi,K_0)
\]

need not resemble

\[
P(O\mid X=a,K).
\]

A privately randomized action likewise need not carry the same evidence as a deliberate choice of that action. If an independent random device determines the action, the resulting observation may reveal little about the traits or reasoning processes that a predictor tracks. Randomization changes the relevant model; it is not a universal device for erasing correlation.

Policy evaluation also raises **dynamic consistency**. An agent can prefer a complete policy initially yet prefer to depart from it after receiving information. One must distinguish:

- selecting a policy with commitment;
- repeatedly applying act-level EDT at later decision points;
- choosing a plan while anticipating later reconsideration.

These are different decision procedures. The single-action formula alone does not establish that they agree. Conditioning on an entire policy can carry evidence that is absent from conditioning on a particular action at one history.

In repeated problems, therefore, specify both the unit of choice and the utility-bearing trajectory. Counting each local decision independently can misrepresent the consequences of adopting the same policy throughout.

## 8. A practical method—and its limits

A disciplined EDT analysis can proceed as follows.

**First, specify the choice.** Is the agent choosing an immediate act, a randomized strategy, or an implementable contingent policy? Identify the actual alternatives.

**Second, fix the evidence.** Write down \(K\): observations, memories, self-knowledge, and knowledge of predictors or correlated agents. Hold this information fixed while comparing alternatives.

**Third, define utility.** Include every valued consequence. Expected dollars are appropriate only when linear monetary utility is a defensible assumption.

**Fourth, construct conditional outcome distributions.** For each alternative, ask what learning that it is performed would imply. Include both causal consequences and noncausal evidence. Do not substitute intervention probabilities merely because a dependency seems causally irrelevant.

**Fifth, check support and sensitivity.** Are the required conditionals defined? Does the answer depend on uncertain predictive reliability, hidden information, or a particular account of deliberation? Threshold calculations often reveal more than a single numerical verdict.

**Finally, maximize conditional expected utility.** State ties and unresolved modeling assumptions explicitly.

The reference’s discussion of Sleeping Beauty illustrates why these preliminary choices matter. Beauty awakens once after heads and twice, with memory loss, after tails. Betting analyses must specify which awakenings contain offers, how decisions across awakenings are linked, and how payments accumulate over the experiment. The reference reports disagreement over whether EDT protects halfers from Dutch books. Its discussion does not establish a general resolution.

The article also mentions an “evidentialist’s wager”: correlated decision-makers might make evidential stakes unusually large. That possibility deserves attention, but large stakes alone do not establish EDT. The relevant correlations, utilities, and treatment of uncertainty between decision theories still require justification.

## Conclusion

EDT recommends maximizing

\[
\mathbb E[u(O)\mid\text{the chosen alternative occurs},K].
\]

Its defining commitment is that an action’s evidence about outcomes matters even when it does not causally influence them. This supports one-boxing and cooperation with sufficiently correlated counterparts, while producing controversial recommendations in cases where reassuring behavior cannot improve the underlying condition.

The calculation is usually simple. The substantive work lies in specifying the evidence, the conditional dependencies, and the object of choice. A careful application makes those assumptions visible—and distinguishes EDT’s clear valuation rule from the unresolved problems of deliberation and policy selection surrounding it.

## References

- Wikipedia contributors. “Evidential decision theory,” supplied [revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688). Principal source; licensed CC BY-SA 4.0.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility,” 1976.
- Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59(1), 1981: 5–30.
- Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015: 2887–2899.