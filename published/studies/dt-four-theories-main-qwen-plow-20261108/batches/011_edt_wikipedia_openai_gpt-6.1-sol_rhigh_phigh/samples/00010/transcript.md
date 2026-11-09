# 011_edt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00010

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b942b991-8a8c-40e1-a165-46f11268574d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b942b991-8a8c-40e1-a165-46f11268574d/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing by What an Action Tells You

Evidential decision theory (EDT) evaluates an action partly by what performing it would reveal. Its central question is:

> Given everything I currently know, how good should I expect the outcome to be, conditional on my taking this action?

This differs from asking which action would *cause* the best outcome. Usually the questions agree. Buying an umbrella both indicates and helps produce a lower probability of getting wet. But they can diverge when an action provides evidence about something it cannot influence: a predictor’s earlier decision, an underlying illness, or another person’s independently made choice.

The supplied reference article characterizes EDT as maximizing an action’s “news value.” This does not mean that pleasant information is itself the goal. The object of evaluation remains the actual outcome. The controversial claim is that ordinary conditional probabilities provide the appropriate weights for evaluating it.

We will develop that claim mathematically, examine its characteristic recommendations, and identify what additional modeling decisions are needed to apply it reliably.

## 1. The basic rule

Let:

- \(E\) represent the agent’s current information;
- \(A\) be a random variable recording the action taken;
- \(\mathcal A\) be the set of available actions;
- \(O_1,\ldots,O_n\) be mutually exclusive, exhaustive outcomes;
- \(u(O_j)\) be the utility of outcome \(O_j\).

Assuming \(P(A=a\mid E)>0\), define the **evidential value** of action \(a\) by

\[
V_E(a)
=
\mathbb E[u(O)\mid E,A=a]
=
\sum_j P(O_j\mid E,A=a)\,u(O_j).
\]

EDT recommends any action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a).
\]

This is the reference article’s definition, with the background information \(E\) made explicit. Utilities need not be monetary. They can incorporate health, pleasure, fairness, other people’s welfare, or anything else the agent values. Monetary examples below assume utility is linear in money.

The conditioning matters. EDT does not merely ask what happens among people who take an action in the general population. It asks what follows from *this agent’s* taking it, given *this agent’s* information. Population statistics can inform that distribution, but they are not automatically the right distribution.

The rule also presupposes a probabilistic model connecting choices to outcomes. It does not itself supply that model. Predictions, shared causes, physical mechanisms, and psychological similarities must all be represented in the probabilities before maximization begins.

## 2. Conditioning is not intervention

The reference contrasts EDT with causal decision theory (CDT), whose probabilities concern outcomes under the counterfactual supposition that an action is performed.

In a causal model, a common representation is

\[
V_C(a)=\mathbb E[u(O)\mid E,\operatorname{do}(A=a)].
\]

Here \(\operatorname{do}(A=a)\) represents an intervention setting the action to \(a\), rather than ordinary observation that \(A=a\). This notation is a useful modeling interpretation of the reference’s counterfactual formulation, not a definition covering every version of CDT.

A simple state-based model shows the difference. Suppose \(S\) describes circumstances fixed before the choice, and \(u(a,s)\) includes all consequences of taking action \(a\) in state \(s\). Then EDT uses

\[
V_E(a)=\sum_s P(s\mid E,A=a)\,u(a,s).
\]

If intervening on the action leaves those circumstances unchanged, CDT instead uses

\[
V_C(a)=\sum_s P(s\mid E)\,u(a,s).
\]

EDT allows the action to change the *evidential weights* assigned to states. CDT holds those weights fixed while varying the action.

If \(S\) and \(A\) are conditionally independent given \(E\), these expressions agree. Thus EDT does not ignore causal consequences. It includes them through the outcome distribution or payoff function, while also retaining noncausal evidential dependencies.

Nor does EDT require backward causation. Conditioning on today’s action can revise beliefs about yesterday, just as observing a footprint revises beliefs about an earlier visitor. The dispute is whether this evidential revision should guide a choice, not whether it is legitimate as inference.

## 3. Newcomb’s problem: evidence about an already-filled box

In Newcomb’s problem, a transparent box contains \(k=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A predictor previously filled the opaque box exactly when it predicted that the agent would take only that box.

Let:

- \(B\): take only the opaque box;
- \(T\): take both boxes;
- \(F\): the opaque box is full.

Suppose

\[
P(F\mid E,B)=0.99,
\qquad
P(F\mid E,T)=0.01.
\]

Then

\[
V_E(B)=0.99M=\$990{,}000,
\]

while

\[
V_E(T)=0.01M+k=\$11{,}000.
\]

EDT therefore recommends taking only the opaque box.

The important dependency is predictive, not retrocausal. One-boxing provides evidence that the predictor anticipated one-boxing, which in turn provides evidence that the opaque box is full.

CDT reasons differently. Whatever the box contains, taking both yields another \(\$1{,}000\). If the current action cannot affect the earlier filling decision, two-boxing is causally better in either fixed state.

A modeling qualification is essential. Saying merely that a predictor is “99% accurate” overall does not establish the two conditional probabilities above. Overall accuracy averages across different actions and can conceal unequal error rates. The reference’s numerical calculation requires the displayed action-conditional probabilities, or assumptions sufficient to derive them.

More generally, writing

\[
p_B=P(F\mid E,B),\qquad p_T=P(F\mid E,T),
\]

EDT recommends one-boxing exactly when

\[
(p_B-p_T)M>k.
\]

Under the additional symmetric assumption \(p_B=r\) and \(p_T=1-r\), this becomes

\[
r>\frac{1+k/M}{2}.
\]

For the stated prizes, the threshold is \(0.5005\). The recommendation therefore depends on the strength of the evidential link and the utility stakes, not on an unconditional commitment to one-boxing.

## 4. Psychological twins: evidence about another decision

The reference’s twin prisoner’s dilemma illustrates the same structure without a predictor or a temporal asymmetry.

Two psychologically identical agents choose independently, without communicating, whether to cooperate or defect. Each receives:

| Own action | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \(5\) | \(0\) |
| Defect | \(10\) | \(1\) |

Let \(C\) and \(D\) denote the agent’s actions, and define

\[
q_C=P(\text{twin cooperates}\mid E,C),
\qquad
q_D=P(\text{twin cooperates}\mid E,D).
\]

Then

\[
V_E(C)=5q_C,
\qquad
V_E(D)=10q_D+(1-q_D)=1+9q_D.
\]

Thus cooperation is recommended precisely when

\[
5q_C>1+9q_D.
\]

For perfect twins, the reference assumes \(q_C=1\) and \(q_D=0\). EDT consequently compares mutual cooperation, worth \(5\), with mutual defection, worth \(1\).

This does not mean cooperation causes the twin to cooperate. Rather, one’s decision is informative about a sufficiently similar reasoning process elsewhere.

For a noisy symmetric model, suppose \(q_C=r\) and \(q_D=1-r\). Cooperation requires \(r>5/7\). Similarity must therefore be strong enough to overcome the temptation payoff.

EDT does not recommend cooperation merely because both players are called rational. Their conditional behavior must be justified by the model. Two agents may share an objective or decision rule without having sufficiently correlated information, preferences, or deliberation.

## 5. The objection: managing the news

The same mechanism that produces attractive recommendations in Newcomb’s problem can appear perverse elsewhere.

Consider the following illustrative model, added here rather than taken from the reference. A hidden lesion \(L\) makes an agent more likely to smoke and independently causes a serious illness. Smoking itself has no effect on the illness.

Suppose, conditional on current information,

\[
P(L\mid \text{smoke})=0.9,
\qquad
P(L\mid \text{abstain})=0.1.
\]

Smoking provides one unit of pleasure; the illness costs \(100\) utility units. EDT assigns

\[
V_E(\text{smoke})=1-100(0.9)=-89,
\]

\[
V_E(\text{abstain})=-100(0.1)=-10.
\]

It recommends abstaining, even though abstention cannot prevent the illness.

CDT instead compares smoking with abstention at the same underlying lesion probability. Since smoking adds pleasure without worsening health, it recommends smoking.

This captures the reference’s central criticism. David Lewis describes EDT as an irrational policy of “managing the news”; James Joyce argues that actions should be chosen for their causal efficacy rather than their auspiciousness.

An evidentialist can respond that, by the agent’s own conditional probabilities, abstainers really are more likely to avoid illness. The disagreement is therefore not an arithmetic error. It concerns whether choosing an act should be evaluated using that act’s evidential association with an uncontrollable state.

The example also blocks a superficial defense of EDT: correlations need not involve predictors or unusually reliable copies. Ordinary common causes can generate them.

## 6. Which information belongs in the calculation?

The lesion example makes the information set \(E\) crucial.

Suppose the agent already knows a psychological fact \(Z\), such as the relevant strength of their urge, and that \(Z\) screens off the action from the lesion:

\[
P(L\mid E,Z,A=a)=P(L\mid E,Z)
\]

for both available actions.

Conditional on \(Z\), smoking no longer carries additional information about illness. EDT then favors smoking’s extra pleasure.

This is a genuine consequence of conditional independence, but not a universal solution to the objection. There may be no observed variable that screens off the correlation. Nor may one simply add the lesion’s actual status to the information set when the agent does not know it.

A sound operational convention is:

> Hold fixed the information actually available before the choice, and assess the additional evidence supplied by each candidate action.

This convention elaborates the reference’s basic formula. It avoids selecting different background information merely to obtain a preferred answer. It does not settle every dispute about deliberative self-knowledge: an agent’s awareness of their motives, intentions, or reasoning may itself affect which dependencies remain.

The relevant question is always conditional: *after accounting for what I already know, what would this action still tell me?*

## 7. Actions, policies, and decisions over time

An isolated action is not always the right object of evaluation. A **policy** specifies an action for each possible information history:

\[
\pi:\mathcal H\longrightarrow\mathcal A.
\]

Examples include a trading strategy, a rule for responding to threats, or instructions governing several future awakenings.

The reference states EDT primarily as an action rule; it does not provide a complete theory of policy selection. A natural extension is to introduce a random variable \(\Pi\) representing the policy adopted and evaluate

\[
V_E(\pi)
=
\mathbb E[U(H)\mid E,\Pi=\pi],
\]

where \(H\) is the resulting complete history and \(U(H)\) its total utility.

This is a proposal for applying the evidential principle, not an additional claim established by the reference.

Its attraction is straightforward: adopting a policy can provide evidence about predictors, other agents’ policies, or several future actions at once. Evaluating only one realized action may discard those connections.

But “adopting policy \(\pi\)” must correspond to a definite event or decision procedure. Merely renaming an action as a policy does not create additional control. A freely chosen last-minute act, a binding advance commitment, and a stable disposition can have different evidential relationships to the world.

Policy evaluation also raises a temporal problem. A policy can look best before information arrives while a different action looks best after it arrives. The agent may then wish to abandon the earlier plan. The one-step EDT formula alone does not establish that policy choice and later action choice will agree.

For sequential problems, an adequate specification must therefore say:

- when the policy is selected;
- what information is available then;
- whether it is binding or revisable;
- how later decisions are evaluated;
- which outcomes enter total utility.

A defensible operational approach is to evaluate genuinely available commitments as commitments and later free choices as later choices, without assuming their recommendations coincide. This exposes, rather than conceals, any conflict between planning and reconsideration.

## 8. Zero-probability acts and randomization

Ordinary conditioning requires positive probability. If

\[
P(A=a\mid E)=0,
\]

the elementary definition

\[
P(O\mid E,A=a)
=
\frac{P(O,A=a\mid E)}{P(A=a\mid E)}
\]

does not assign a value.

This matters because a sufficiently self-confident agent might regard its own eventual choice as certain. It also arises in models with perfectly deterministic predictors.

The reference leaves this issue open. One possible operational extension is to model small probabilities of mistakes, experimentation, or imperfect self-knowledge, ensuring that every feasible action has positive probability. One can then examine the limiting recommendations as those probabilities shrink.

However, different perturbations can produce different limiting conditional probabilities. There is no general guarantee of a unique answer. If the verdict depends on the perturbation, the model needs additional assumptions.

Randomization likewise requires care. Choosing a probability distribution over actions and observing the outcome of a random draw are different events. A predictor might forecast the distribution accurately while being unable to forecast the draw. Conditioning on policy adoption and conditioning on the realized action can therefore have different implications.

An application of EDT must identify which event is being evaluated, rather than treating every occurrence of the same physical action as evidentially equivalent.

## 9. A practical procedure, and its limits

For an unfamiliar problem, a useful workflow is:

1. **Specify the decision object:** immediate act, randomized strategy, or policy.
2. **Fix current information:** write down \(E\), without adding unknown facts.
3. **Specify complete outcomes and utility:** include costs, benefits, and any welfare beyond the agent’s own.
4. **Model dependencies:** identify causal effects, common causes, predictions, and similarities between decision processes.
5. **Compute conditional expectations:** use \(P(O\mid E,A=a)\), or the explicitly justified policy analogue.
6. **Check robustness:** vary uncertain correlations, utility assumptions, and treatments of zero-probability options.

The difficult step is usually not maximization but constructing the conditional distribution. Correlation should neither be discarded merely because it is noncausal nor asserted merely because a story describes agents as similar.

The reference’s discussion of Sleeping Beauty illustrates these limits. Beauty is awakened once after heads and twice, with memory erasure, after tails. The article reports disagreement over whether EDT protects certain “halfer” betting strategies from Dutch books, including Conitzer’s argument that it does not generally do so. A complete analysis must specify linked betting decisions and total payoffs across awakenings; the EDT slogan alone settles neither credence nor betting policy.

The article also mentions an evidentialist wager: correlated decisions elsewhere might make EDT’s stakes unusually large. That possibility matters only insofar as those outcomes enter the agent’s utility and the correlations are credible. It is not, by itself, a general proof of EDT.

### Sources

This essay develops the supplied article, Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688, licensed CC BY-SA 4.0. Its principal cited treatments include Gibbard and Harper, *Counterfactuals and Two Kinds of Expected Utility* (1976); Ahmed, *Evidential Decision Theory* (2021); Lewis, “Causal decision theory” (1981); Joyce, *The Foundations of Causal Decision Theory* (1999); and Conitzer, “A Dutch book against sleeping beauties who are evidential decision theorists” (2015).

## Conclusion

EDT maximizes expected utility conditional on taking an action. Its distinctive feature is retaining evidential dependencies even when they do not represent causal influence. This explains both its appeal in prediction and twin problems and its vulnerability to the charge of managing the news. Applying it well requires explicit information, utilities, and conditional probabilities—and additional care when the choices concern policies, repeated decisions, or events assigned probability zero.
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Considering uncertainties and sources**

There's a lot to unpack regarding expected normative uncertainty weights and how they're not mandated, along with cross-theory scaling issues that remain unresolved. I think it probably fits into a broader context, though. It's important that we don’t make claims without proper sourcing, especially regarding EDT policy. Also, I want to ensure that any original derivations get proper credit without infringing on copyright. I’m aiming to produce around 2850 words.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6fd7d969-87ee-4e8f-b08a-677efe1dfc68/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6fd7d969-87ee-4e8f-b08a-677efe1dfc68/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6fd7d969-87ee-4e8f-b08a-677efe1dfc68/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6fd7d969-87ee-4e8f-b08a-677efe1dfc68/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
