# Evidential Decision Theory: Choosing What You Would Welcome as News

Suppose you must choose an action whose consequences depend partly on circumstances you cannot observe. Your action may provide evidence about those circumstances—even when it cannot change them. Should that evidence influence your choice?

**Evidential decision theory** (EDT) says yes. Its central instruction is to choose the action associated with the greatest expected utility, conditional on performing that action. As the supplied reference article puts it, choose what you would most want to learn that you will do.

This slogan needs careful interpretation. EDT does not say that favorable news causes favorable events, nor that pleasant beliefs are intrinsically valuable. It evaluates actual outcomes, but uses the action itself as evidence about which outcomes obtain.

The reference article supplies the basic rule and its applications to Newcomb’s problem and the twin prisoner’s dilemma. The modeling recommendations, additional examples, and policy-level formulation below elaborate that account; where the basic rule leaves choices open, those choices will be made explicit.

## 1. The conditional-expectation rule

Let:

- \(I\) denote the agent’s current evidence;
- \(A\) be a random variable representing the action performed;
- \(\mathcal A\) be the set of available actions;
- \(O\) represent the resulting outcome;
- \(u(O)\) be the agent’s utility for that outcome.

For finitely many possible outcomes, EDT assigns action \(a\) the value

\[
V_I(a)=\sum_o P(O=o\mid I,A=a)\,u(o).
\]

It recommends any action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_I(a).
\]

More generally,

\[
V_I(a)=\mathbb E[u(O)\mid I,A=a],
\]

provided the conditional expectation exists.

The probabilities are the agent’s credences, ideally informed by reliable empirical evidence. Utilities represent what the agent ultimately values. Monetary payoffs can stand directly for utility only under an assumption such as risk neutrality over the relevant amounts.

Outcomes must also be described richly enough to include everything that matters. If an action has a direct cost, that cost belongs in the utility calculation. An equivalent formulation uses a state variable \(S\) and an action-dependent utility function:

\[
V_I(a)=\sum_s P(S=s\mid I,A=a)\,u(a,s).
\]

Here \(S\) describes payoff-relevant circumstances, while \(u(a,s)\) describes the consequences of performing \(a\) in circumstance \(s\).

Two ingredients therefore determine an EDT recommendation:

1. how valuable each action–state combination is;
2. what performing each action would indicate about the state.

The second ingredient distinguishes EDT. It does not generally evaluate every action against the same distribution over circumstances.

The conditioning must be performed separately for each candidate action, using the same underlying probability model. One must not first condition on the favored action and then use that posterior to evaluate all alternatives.

## 2. Evidence is not intervention

The reference article contrasts EDT with causal decision theory (CDT). In its presentation, CDT evaluates probabilities of counterfactual outcomes:

\[
U_I(a)=\sum_o P(a\mathrel{\Box\!\rightarrow}o\mid I)\,u(o).
\]

The expression \(a\mathrel{\Box\!\rightarrow}o\) concerns what would happen if action \(a\) were performed. It is not ordinary material implication.

In a standard causal-model formulation, a corresponding expression is

\[
U_I(a)=\mathbb E[u(O)\mid I,\operatorname{do}(A=a)].
\]

The intervention notation expresses an important distinction. Conditioning on \(A=a\) retains the information conveyed by the ordinary process producing the action. Intervening to set \(A=a\) severs that action’s usual causal dependence on its antecedents while preserving its downstream effects. This is a useful illustration of the contrast, though it is not a complete account of every formulation of CDT.

Consider a hidden variable \(L\) that influences both the agent’s action and some outcome:

\[
L\longrightarrow A,\qquad L\longrightarrow O.
\]

Learning the action can reveal something about \(L\), and thus about \(O\). Forcing the action need not change \(L\). Consequently,

\[
P(O\mid I,A=a)
\]

can differ from

\[
P(O\mid I,\operatorname{do}(A=a)).
\]

EDT retains such evidential connections. They may arise from common causes, reliable prediction, shared psychological traits, or similar reasoning processes.

This does not amount to backward causation. If an action is evidence about yesterday’s prediction, EDT need not claim that today’s action changes yesterday. It instead compares conditional distributions in which the action and the prediction already tend to match.

When the relevant circumstances are independent of the action, conditional on current evidence,

\[
P(S\mid I,A=a)=P(S\mid I),
\]

the state-based formula becomes ordinary expected-utility maximization against a common distribution over states. Under the corresponding causal assumptions, EDT and CDT then agree.

## 3. Newcomb’s problem: prediction without backward influence

In Newcomb’s problem, a transparent box contains \(c=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box:

- it contains \(M\) if the predictor predicted that the agent would take only that box;
- it is empty if the predictor predicted that the agent would take both boxes.

Write \(B\) for taking only the opaque box and \(T\) for taking both. Let \(F\) mean that the opaque box is full, and define

\[
q_B=P(F\mid I,A=B),\qquad
q_T=P(F\mid I,A=T).
\]

For a risk-neutral agent,

\[
V_I(B)=Mq_B,
\]

whereas

\[
V_I(T)=Mq_T+c.
\]

EDT therefore recommends taking only the opaque box precisely when

\[
M(q_B-q_T)>c.
\]

This inequality isolates the relevant trade-off: the evidential advantage must outweigh the transparent box’s guaranteed payment.

The reference article uses

\[
q_B=0.99,\qquad q_T=0.01.
\]

Then

\[
V_I(B)=\$990{,}000,
\qquad
V_I(T)=\$11{,}000.
\]

EDT recommends one-boxing.

An important qualification is that “the predictor is 99% accurate overall” does not, by itself, establish both conditional probabilities. Aggregate accuracy depends on how often each action occurs as well as on the predictor’s errors within each category. The article’s numerical calculation should therefore be understood as assuming the specified action-conditional reliability.

CDT’s familiar two-boxing argument holds the already-set contents fixed when comparing actions: whatever the opaque box contains, taking both obtains another \$1,000. EDT instead compares worlds conditional on different choices. In one group the opaque box is probably full; in the other it is probably empty.

Thus the disagreement is not arithmetic. It concerns whether rational choice should exploit an evidential association with something the action cannot causally alter.

## 4. Psychological twins and conditional cooperation

The article’s twin prisoner’s dilemma makes the same structure interpersonal.

Two psychologically identical agents independently choose cooperation or defection. Each cares only about their own payment:

| Own action | Other cooperates | Other defects |
|---|---:|---:|
| Cooperate | \$5 | \$0 |
| Defect | \$10 | \$1 |

Let

\[
q_C=P(\text{other cooperates}\mid I,A=C),
\]

and

\[
q_D=P(\text{other cooperates}\mid I,A=D).
\]

Then

\[
V_I(C)=5q_C,
\qquad
V_I(D)=10q_D+(1-q_D)=1+9q_D.
\]

Cooperation is recommended exactly when

\[
5q_C>1+9q_D.
\]

For perfect psychological twins, the article assumes \(q_C=1\) and \(q_D=0\), yielding values of \$5 and \$1.

An imperfect version clarifies the strength of correlation required. Suppose the other agent matches one’s action with conditional probability \(r\), whichever action one takes. Then

\[
q_C=r,\qquad q_D=1-r,
\]

so cooperation is preferred when

\[
5r>10-9r
\quad\Longleftrightarrow\quad
r>\frac57.
\]

EDT therefore does not recommend cooperation merely because the other player is described as “similar.” The similarity must support sufficiently strong conditional predictions.

Defection still pays more for either fixed action of the opponent. EDT’s recommendation differs because it does not hold the opponent’s probable action fixed across the comparison.

## 5. The central objection: managing the news

The same mechanism can appear much less attractive elsewhere. The reference article reports Lewis’s criticism that EDT promotes an irrational policy of “managing the news,” and Joyce’s insistence that action should be guided by causal efficacy rather than auspiciousness.

Consider the following additional toy model.

A hidden condition \(L\) produces both a tendency to smoke and a serious disease. Smoking itself has no effect on the disease. Smoking provides one unit of enjoyment; having the condition costs 100 utility units:

\[
u(a,L)=\mathbf 1_{\{a=\mathrm{smoke}\}}-100\mathbf 1_L.
\]

Suppose

\[
P(L\mid I,\mathrm{smoke})=0.9,
\qquad
P(L\mid I,\mathrm{abstain})=0.1.
\]

EDT assigns

\[
V_I(\mathrm{smoke})=1-90=-89,
\]

and

\[
V_I(\mathrm{abstain})=-10.
\]

It recommends abstaining, even though abstention cannot prevent the disease.

If the current unconditional probability of \(L\) is \(1/2\), a causal evaluation gives smoking and abstaining values of \(-49\) and \(-50\), respectively. Smoking adds enjoyment without altering the disease risk.

Critics regard EDT’s abstention as confusing evidence of health with an effective way of becoming healthy. An evidentialist replies that the favorable association is relevant to which action to choose, just as predictor reliability is relevant in Newcomb’s problem.

This is the philosophical fault line. Both sides can agree completely about the causal structure and the conditional probabilities while disagreeing about which quantities should govern choice.

The example also illustrates why current information matters. If some observed variable \(T\), such as a fully informative diagnosis or psychological observation, screens off the association,

\[
P(L\mid I,T,A=a)=P(L\mid I,T),
\]

then the action no longer provides additional evidence about the condition. With those conditional probabilities, EDT recommends smoking for its stipulated enjoyment. But whether introspective evidence really screens off the association must be established, not assumed merely to obtain a preferred verdict.

## 6. Specifying the evidential model

The EDT formula is short; supplying its inputs can be difficult. The reference article does not settle all the following questions.

### Which information is held fixed?

A natural operational interpretation is to condition on all evidence presently available, then separately suppose each candidate action. This prevents arbitrary omission of known facts.

However, deliberation can itself produce evidence: an agent notices an inclination, reaches a conclusion, or recognizes a feature of their reasoning. Modeling these stages can change the action’s remaining evidential significance. EDT’s elementary formula does not independently specify the correct granularity of deliberation.

### What generates the action probabilities?

The model must represent the agent’s action as uncertain before the decision is settled. This need not mean that actions are physically random; uncertainty about deterministic reasoning can suffice.

Nevertheless, a recommendation can affect expectations about what the agent will do. A complete theory of a self-predicting decision-maker may therefore need consistency conditions between deliberation and action prediction. The basic conditional-expectation rule does not automatically supply a unique such model.

### What if an alternative has probability zero?

Ordinary conditioning requires

\[
P(A=a\mid I)>0.
\]

If the agent is certain that an available alternative will not be chosen, its conditional value is undefined by the elementary formula.

One possible modeling proposal is to introduce small “tremble” probabilities for every action and examine a limit as the trembles vanish. But the result can depend on how those trembles relate to hidden variables. A random motor error and a change of mind need not carry the same evidence.

Thus positive-probability modeling or a rule for zero-probability suppositions is an additional assumption, not something uniquely determined by basic EDT.

### Does randomization remove the dependence?

Sometimes. If an action is selected by a randomizer genuinely independent of relevant states, conditional on current evidence, then

\[
P(S\mid I,A=a)=P(S\mid I).
\]

But choosing whether to randomize may itself reveal information. Randomization is not a universal device for deleting inconvenient correlations; the randomization procedure must be included in the model.

## 7. From isolated actions to policies

Sequential problems require a further distinction. An **action** concerns what to do now. A **policy** specifies what to do across possible future observations.

Let \(H\) denote an observable history. A deterministic policy is a function

\[
\pi:H\longrightarrow\mathcal A.
\]

The supplied article defines EDT primarily for actions; it does not provide a complete theory of policy selection. A natural extension is to treat adopting a policy as the evidential event being evaluated.

Let \(\Pi\) represent the policy the agent implements, and let \(W\) describe the complete resulting trajectory. Define

\[
V_I^{\mathrm{policy}}(\pi)
=
\mathbb E[u(W)\mid I,\Pi=\pi].
\]

This is EDT applied at the policy-selection level. It requires a joint model of policies, observations, predictions, other agents’ behavior, and final outcomes.

Importantly, conditioning on \(\Pi=\pi\) is not the same as intervening to install that policy. It retains whatever evidence policy adoption provides about the rest of the world.

The evaluation can be decomposed as

\[
V_I^{\mathrm{policy}}(\pi)
=
\sum_h P(h\mid I,\Pi=\pi)
\mathbb E[u(W)\mid I,\Pi=\pi,H=h].
\]

Both the probability of reaching a history and the expected utility there may depend evidentially on the policy.

This matters when a predictor responds to an agent’s whole strategy, when several decisions reflect the same reasoning process, or when a policy controls repeated encounters. Conditioning only on one observed act can discard relevant information about these connections.

Policy evaluation also raises a dynamic question: will an agent who prefers a policy before receiving information still prefer its prescribed action afterward? The initial comparison conditions on policy adoption, whereas later act evaluation may condition on a different evidential event. The basic EDT formula alone does not guarantee that these rankings coincide.

For a sequential problem, a usable specification should therefore state:

- whether the choice concerns a present act or a complete policy;
- what evidence is available at each stage;
- whether earlier commitments can be revised;
- how repeated decisions and other agents’ choices are correlated.

Without these details, apparently different EDT solutions may concern different decision problems.

The article’s discussion of Sleeping Beauty illustrates this sensitivity. It reports both proposed EDT defenses against Dutch books and Conitzer’s argument that some halfers remain vulnerable. A betting calculation must specify not just Beauty’s credence, but which offers occur, how decisions across awakenings are linked, and how total gains and losses are aggregated. The source does not establish a universal resolution of that dispute.

## 8. Applying EDT to an unfamiliar case

A practical EDT analysis begins by identifying the actual choice object: an action, a randomized procedure, or a policy. Next, specify utilities over complete consequences and build a joint probability model incorporating the agent’s current information.

For each alternative, condition on that alternative occurring. Preserve relevant predictive and common-cause dependencies rather than deleting them merely because they are noncausal. Then compute conditional expected utility and compare.

Before trusting the result, check three vulnerabilities: whether the required conditionals are genuinely supported, whether additional known evidence screens off a dependence, and whether zero-probability or policy-level assumptions have been left implicit.

These checks do not replace EDT. They make clear what its recommendation depends on.

## References

- Wikipedia contributors. “Evidential decision theory.” Supplied [revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), licensed CC BY-SA 4.0. Primary source for this essay.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility* (1976), as cited in the supplied article.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Conitzer, Vincent. “A Dutch book against sleeping beauties who are evidential decision theorists.” *Synthese* 192 (2015): 2887–2899.

## Conclusion

EDT evaluates alternatives by the expected utility of outcomes conditional on choosing them. Its distinctive commitment is that evidence carried by an action can matter even when it concerns circumstances the action cannot change. That commitment explains both its attractive treatment of reliable predictors and psychological twins and its controversial treatment of diagnostic actions.

Applying EDT therefore requires more than a payoff table. It requires a defensible model of what each choice would reveal—and clarity about whether the agent is choosing an act, a procedure, or a policy.