# Evidential Decision Theory: Choosing by What an Action Reveals

A decision can matter in two different ways. It can **change the world**, and it can **provide evidence about the world**. Usually these considerations favor the same action. Taking an effective medicine both improves one’s prospects and indicates that recovery is more likely. But when an action is correlated with something it cannot cause—an earlier prediction, a hidden medical condition, or another person’s simultaneous choice—the two considerations can diverge.

**Evidential decision theory** (EDT) evaluates actions through conditional expected utility. Its central instruction, as presented in the supplied reference article, is to choose the action whose occurrence would be the best news about the outcome.

This is not a recommendation to value comforting beliefs. The utility remains the utility of what actually happens. The controversial step is using an action’s evidential significance, including its noncausal significance, to decide whether to perform it.

## 1. The mathematical rule

Let:

- \(E\) represent the agent’s current evidence;
- \(A\) be a random variable representing the action performed;
- \(\mathcal A\) be the available actions;
- \(S\) represent uncertain features of the situation;
- \(u(a,s)\) be the utility of performing \(a\) when \(S=s\).

For finite state spaces, EDT assigns action \(a\) the value

\[
V_E(a)
=
\sum_s P(S=s\mid E,A=a)\,u(a,s),
\]

and recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a).
\]

Equivalently, if \(O_j\) are mutually exclusive and exhaustive outcomes,

\[
V_E(a)=\sum_j P(O_j\mid E,A=a)\,u(O_j).
\]

This is the reference article’s central definition, with the background evidence \(E\) made explicit. For continuous outcomes, the corresponding sum becomes an integral.

Three details matter.

First, the utility must describe the consequences the agent actually values. Money can stand for utility only under an appropriate assumption, such as risk neutrality over the amounts involved. An altruistic agent can include others’ welfare; a selfish agent need not.

Second, EDT conditions on **all relevant current evidence**. Population-level correlations need not survive conditioning on what this particular decision-maker knows.

Third, the alternatives are evaluated using one fixed probability model. The agent should not invent a favorable distribution separately for each candidate action. The different conditional distributions must arise from a coherent joint distribution involving actions, states, and outcomes.

Bayes’ rule makes the evidential mechanism explicit:

\[
P(s\mid E,A=a)
=
\frac{P(A=a\mid s,E)P(s\mid E)}
{\sum_{s'}P(A=a\mid s',E)P(s'\mid E)}.
\]

An action favors hypotheses under which that action was comparatively likely. EDT then evaluates the outcomes associated with those hypotheses.

This is a decision rule, not an extra law of probability. Bayesian conditioning explains how to calculate the values once a model is supplied; EDT adds the normative claim that these are the values to maximize.

## 2. Conditioning is not intervention

The reference contrasts EDT with causal decision theory (CDT). In its presentation, CDT uses probabilities of counterfactual outcomes:

\[
U_E(a)
=
\sum_j P(a\mathrel{\Box\!\to}O_j\mid E)\,u(O_j),
\]

where \(a\mathrel{\Box\!\to}O_j\) concerns what would happen if action \(a\) were performed.

In a suitable causal model, a common representation is

\[
U_E(a)
=
\mathbb E[u\mid E,\operatorname{do}(A=a)].
\]

Here \(\operatorname{do}(A=a)\) replaces the ordinary process generating the action with an intervention setting it to \(a\). This notation is a useful clarification, rather than a claim that every version of CDT has precisely the same counterfactual semantics.

The distinction is straightforward:

- **Conditioning** asks which worlds are more probable given that the action occurs.
- **Intervention** asks what happens when the action is imposed while its ordinary causes are held fixed or disconnected appropriately.

Suppose a hidden variable \(G\) influences both the agent’s choice and an outcome:

\[
G\longrightarrow A,
\qquad
G\longrightarrow O.
\]

Observing \(A\) can reveal information about \(G\), and therefore about \(O\), without \(A\) causing \(O\).

EDT retains that information. CDT does not treat this particular informational association as a benefit of intervening on the action.

Thus EDT’s hypothetical question is evidential: “Suppose I learned that I performed \(a\).” It need not preserve the same beliefs about earlier events across alternatives. That does **not** mean it assumes backward causation. Changing one’s conditional probability for an earlier event is not changing the event.

Where the observational and intervention distributions agree, the two theories agree as well.

## 3. Newcomb’s problem: evidence about an earlier prediction

Newcomb’s problem places this distinction in a dramatic setting.

There are two boxes:

- a transparent box containing \(b=\$1{,}000\);
- an opaque box containing either \(M=\$1{,}000{,}000\) or nothing.

A predictor has already filled the opaque box. It contains \(M\) if the predictor predicted that the agent would take only that box; otherwise it is empty.

Let \(F\) mean that the opaque box is full. Suppose

\[
P(F\mid E,\text{one-box})=q,
\]

and

\[
P(F\mid E,\text{two-box})=1-q.
\]

These are assumptions about **conditional reliability**. An aggregate statement that a predictor is “99% accurate” does not, by itself, determine both conditionals. The reference’s numerical example effectively supplies the symmetric values \(q=0.99\).

With linear monetary utility,

\[
V_E(\text{one-box})=qM,
\]

whereas

\[
V_E(\text{two-box})=b+(1-q)M.
\]

Therefore EDT recommends one-boxing exactly when

\[
(2q-1)M>b.
\]

For the specified amounts, the threshold is

\[
q>\frac{1+b/M}{2}=0.5005.
\]

At \(q=0.99\),

\[
V_E(\text{one-box})=\$990{,}000,
\qquad
V_E(\text{two-box})=\$11{,}000.
\]

CDT instead treats the opaque box’s already-fixed contents as unaffected by the present action. If \(p=P(F\mid E)\), its corresponding values are

\[
U_E(\text{one-box})=pM,
\]

\[
U_E(\text{two-box})=pM+b.
\]

Two-boxing is causally better by \(b\), whatever \(p\) is.

Neither calculation contains an arithmetic error. The disagreement concerns which comparison should govern choice.

The causal comparison holds the box contents fixed across alternatives. The evidential comparison allows one-boxing and two-boxing to support different beliefs about those contents. One-boxing does not fill the box; it indicates that the box was probably filled.

This also explains why two-boxing’s apparent dominance does not settle the dispute. It dominates when each action is compared within the same box-content state. EDT instead weights those states differently for different actions.

## 4. Psychological twins and correlated choices

The reference also considers a prisoner’s dilemma between psychological twins. Each receives:

| Agent’s action | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | 5 | 0 |
| Defect | 10 | 1 |

The agent values only her own payoff.

Write

\[
x=P(\text{twin cooperates}\mid E,\text{cooperate}),
\]

\[
y=P(\text{twin cooperates}\mid E,\text{defect}).
\]

Then

\[
V_E(C)=5x,
\qquad
V_E(D)=10y+(1-y)=1+9y.
\]

Cooperation is evidentially preferable when

\[
5x>1+9y.
\]

For perfectly correlated choices, \(x=1\) and \(y=0\), giving values \(5\) and \(1\). EDT cooperates.

A useful generalization assumes symmetric matching reliability \(r\):

\[
P(C_{\rm twin}\mid C)=r,
\qquad
P(D_{\rm twin}\mid D)=r.
\]

Then cooperation is preferable when

\[
5r>10-9r,
\]

or

\[
r>\frac57.
\]

The numerical threshold is an additional derivation, not one supplied by the reference.

The important point is that cooperation requires a sufficiently strong dependence in the probability model. EDT does not infer cooperation merely because both players are described as rational. Shared reasoning, common information, or matched implementation must justify the relevant conditional probabilities.

Nor does EDT require the agent’s decision to cause her twin’s decision. Its recommendation arises precisely because her own choice is informative about the other choice.

## 5. The criticism: choosing favorable symptoms

The reference reports Lewis’s criticism that EDT promotes an irrational policy of “managing the news.” A simple additional example shows the concern.

Suppose an agent can eat an enjoyable snack. Eating gives one unit of utility and has no effect on whether she has a serious disease. However, a hidden condition increases both disease risk and the propensity to eat the snack. Given her current evidence,

\[
P(D\mid E,\text{eat})=0.8,
\qquad
P(D\mid E,\text{abstain})=0.2.
\]

Let utility be

\[
u(a,D)
=
\mathbf 1_{\{a=\text{eat}\}}
-
100\mathbf 1_{\{D\}}.
\]

EDT calculates

\[
V_E(\text{eat})=1-100(0.8)=-79,
\]

\[
V_E(\text{abstain})=-100(0.2)=-20,
\]

and recommends abstaining.

Causally, eating adds one unit of enjoyment without affecting disease. A causal theorist therefore regards abstention as sacrificing a genuine benefit merely to select an action associated with healthier people.

The evidentialist can reply that abstention really would be good news in the stipulated model. But this restates the disagreement: should favorable diagnostic significance guide action when the action cannot improve the diagnosed condition?

### Screening off the association

Additional evidence can change the verdict. Suppose the agent learns the relevant hidden condition \(G\), and it screens off the association:

\[
D\perp A\mid E,G.
\]

Then

\[
P(D\mid E,G,\text{eat})
=
P(D\mid E,G,\text{abstain}),
\]

so EDT recommends eating for the extra utility.

This is a genuine consequence of the conditional-expectation rule. It is not, however, a universal solution. Observing one’s desires or symptoms need not reveal every relevant common cause.

Moreover, both Newcomb-style prediction and the snack example can involve noncausal correlations. The basic EDT formula contains no separate instruction to retain “helpful prediction correlations” while discarding “mere symptom correlations.” Anyone proposing such a distinction needs an additional principle.

## 6. What if the alternative action has probability zero?

The reference states EDT’s formula without resolving an important technical issue: ordinary conditional probabilities require the conditioning event to have positive probability.

If

\[
P(A=a\mid E)=0,
\]

then the usual ratio does not define

\[
P(S\mid E,A=a).
\]

This matters for an agent who is certain how she will choose, or whose known deterministic procedure logically fixes her action.

A reasonable operational approach is to model uncertainty before the decision is settled. The agent can be uncertain about her eventual deliberation, implementation, or relevant psychological details. Each candidate action may then have positive probability.

Another possibility is to specify a family of models \(P_\varepsilon\) in which each action has positive probability, and examine

\[
\lim_{\varepsilon\to0}
\mathbb E_{P_\varepsilon}[u\mid E,A=a].
\]

These are modeling proposals, not a uniquely specified completion of EDT in the source.

The difficulty is that different perturbations can give different answers. An unexpected action might result from a shared reasoning error, a private randomizer, or an external malfunction. Those possibilities provide different evidence about predictors and twins.

Consequently, “give every action a tiny probability” is not enough. One must specify **how** the otherwise unlikely action could occur.

This also prevents a common mistake about randomization. If an independent coin determines the final move, observing its result need not reveal the agent’s underlying disposition. Correlations attached to a deliberative choice cannot automatically be transferred to a mechanically randomized action.

## 7. Actions, policies, and sequential decisions

A policy specifies what to do at multiple possible decision points. Formally, a deterministic policy maps an information history \(h\) to an action:

\[
\pi:h\mapsto a.
\]

The reference primarily presents action-level EDT. A natural extension—proposed here rather than uniquely dictated by the article—is to evaluate policy selection evidentially:

\[
W_E(\pi)
=
\mathbb E[u\mid E,\Pi=\pi],
\]

where \(\Pi\) represents the policy selected and \(u\) measures the complete outcome.

This extension requires a joint model relating policy selection to the environment. If a predictor forecasts policies, or other agents use correlated procedures, conditioning on \(\Pi=\pi\) may change expectations about them.

It is not equivalent to evaluating

\[
\mathbb E[u\mid E,\operatorname{do}(\Pi=\pi)].
\]

The former treats selection as evidence; the latter represents an intervention on the policy.

### Ex ante evaluation and later reconsideration

For possible later histories \(h\), the law of total expectation gives

\[
W_E(\pi)
=
\sum_h
P(h\mid E,\Pi=\pi)
\mathbb E[u\mid E,h,\Pi=\pi].
\]

But an agent reconsidering locally might instead maximize

\[
V_{E,h}(a)
=
\mathbb E[u\mid E,h,A=a].
\]

These expressions condition on different events. There is no general reason for policy selection and repeated local action selection to produce identical behavior.

An operational account must therefore specify:

1. whether the choice object is a present action or a complete policy;
2. whether later choices are committed or revisable;
3. what information later agents possess;
4. which decisions remain correlated.

Policy evaluation does not automatically solve every sequential problem. It clarifies where further assumptions enter.

### Repeated awakenings

The reference’s discussion of Sleeping Beauty illustrates this need. In the standard setup, a coin determines whether Beauty has one awakening or two, with memory erased between awakenings.

Evaluating bets requires more than a conditional probability for heads. One must specify whether a bet is offered once or repeatedly, whether indistinguishable awakenings implement the same decision, and how payments accumulate over the experiment.

The source reports both a proposal that EDT helps some “halfer” agents avoid Dutch books and Conitzer’s criticism of that proposal. It does not establish a universal resolution. EDT supplies an optimization rule; it does not independently settle every question about self-locating probability or betting protocols.

## 8. Applying EDT to an unfamiliar problem

A practical application should proceed in the following order.

**Specify outcomes and utilities.** Include all consequences the agent values, rather than treating money or other agents’ welfare as automatically relevant.

**Fix the evidence.** Identify what is known before comparing alternatives, including information that might screen off apparent correlations.

**Build a joint model.** Represent how states, predictions, dispositions, other agents, and actions are related. Distinguish observed correlation from an unsupported assumption of psychological similarity.

**Calculate the action-conditioned distributions.** Use \(P(S\mid E,A=a)\), not an intervention distribution, unless the model makes them equal.

**Check support and decision granularity.** Explain zero-probability alternatives, randomization, and whether the decision concerns an action or a policy.

Finally, test sensitivity. As the Newcomb and twin calculations demonstrate, a qualitative statement such as “the predictor is reliable” or “the players are similar” can conceal a quantitative threshold.

The source also reports an argument that EDT may deserve extra attention under uncertainty about decision theory because correlated decisions can involve large stakes. That is not an automatic argument for EDT: its force depends on the agent’s utility function and on how competing theories’ recommendations are aggregated.

## References and source attribution

The central rule, standard examples, and reported philosophical disputes follow Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” supplied revision 1373679688. References discussed there include Gibbard and Harper, *Counterfactuals and Two Kinds of Expected Utility* (1976); Ahmed, *Evidential Decision Theory* (2021); Lewis, “Causal Decision Theory” (1981); and Conitzer, “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists” (2015). The threshold calculations, snack example, and operational proposals above are mathematical elaborations.

## Conclusion

EDT recommends the action with the greatest expected utility conditional on its being performed. Its distinctive commitment is to count noncausal evidential dependencies alongside ordinary causal consequences. That makes one-boxing and cooperation with sufficiently correlated twins intelligible, while exposing the theory to the charge of choosing favorable symptoms. Applying it rigorously requires more than its compact formula: one must specify the evidence, joint probability model, feasible alternatives, and level of decision being evaluated.