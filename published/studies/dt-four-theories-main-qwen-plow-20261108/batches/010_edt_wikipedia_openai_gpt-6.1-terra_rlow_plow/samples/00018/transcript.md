# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00018

Status: **complete**. Saved outcome: **DC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/73187e81-42ee-4425-83cf-7e6a46647787/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/73187e81-42ee-4425-83cf-7e6a46647787/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential decision theory: choosing what would be good news

Suppose you are about to choose between two actions. One question you might ask is: *What will each action cause?* Another is: *What would each action tell me about the world?* Usually the answers work together. Taking an umbrella both causes you to stay drier and may indicate that rain is likely.

But the questions can come apart. An action might be evidence that something desirable has already happened, even though the action cannot cause that earlier event. Or it might be evidence about what another, similarly situated decision-maker will do, even though neither person influences the other.

**Evidential decision theory**, or EDT, evaluates an action by the expected desirability of the outcomes conditional on taking it. In the reference article’s memorable formulation, it recommends doing what you would most want to learn that you will do. This is not merely advice to feel optimistic: the “news” of an action matters because the action can be statistically associated with facts that determine what happens.

The central philosophical dispute is whether such associations are appropriate grounds for choice when they do not represent causal influence. EDT says, roughly, that they are. Causal decision theory, or CDT, evaluates actions using a different sort of counterfactual: what would happen *if the action were performed*, holding fixed relevant features of the world that the action cannot affect.

## The basic calculation

Let \(H\) represent everything the agent knows when deciding, and let \(\mathcal A\) be the available actions. Suppose the possible outcomes \(O_1,\ldots,O_n\) are mutually exclusive and exhaustive, with utilities \(u(O_j)\). The evidential value of action \(a\) is

\[
V_{\mathrm E}(a\mid H)
=\sum_{j=1}^{n}P(O_j\mid A=a,H)\,u(O_j).
\]

EDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_{\mathrm E}(a\mid H).
\]

More generally, if utility depends on a detailed state \(S\) and the action itself, the same rule can be written

\[
V_{\mathrm E}(a\mid H)
=\sum_s P(S=s\mid A=a,H)\,u(a,s).
\]

The probabilities are the agent’s credences at the decision point, conditional both on current information and on the hypothetical news that the action is taken. Utility should include everything the agent cares about: money, health, effects on others, risk, and so on. Using dollar amounts directly as utilities, as the examples below do, assumes for simplicity that the agent values the relevant amounts linearly.

For an ordinary event of positive probability, Bayes’s rule gives

\[
P(S=s\mid A=a,H)
=
\frac{P(A=a\mid S=s,H)P(S=s\mid H)}
     {P(A=a\mid H)}.
\]

This makes the evidential mechanism explicit. A state becomes more plausible on learning that \(a\) is taken if that action would be relatively likely in that state. The dependence might arise because the state helps cause the action, because it predicts the action, or because the action and state have a common source. EDT’s formula does not require that the action cause the state.

That does not mean every attractive correlation should be accepted uncritically. The probabilities must reflect the actual decision problem and the agent’s current information. A correlation that holds in a population may disappear once the agent knows relevant facts about herself. Conversely, conditioning on too little can conceal a dependency that matters.

## Conditioning and causal counterfactuals

The reference article contrasts EDT’s conditional probabilities with the probabilities of causal counterfactuals. A convenient illustration uses intervention notation:

\[
V_{\mathrm C}(a\mid H)
=\sum_j P(O_j\mid \operatorname{do}(A=a),H)\,u(O_j).
\]

Here \(\operatorname{do}(A=a)\) represents a causal intervention that sets the action to \(a\), rather than merely observing that \(A=a\). This notation is a useful operational model for CDT, although causal decision theory can be formulated in other ways.

The difference is clearest in a simple causal model. Suppose an underlying variable \(S\) influences both what an agent does and what outcome occurs:

\[
S\longrightarrow A,\qquad S\longrightarrow O,\qquad A\longrightarrow O.
\]

Observing \(A=a\) provides information about \(S\), because \(S\) helps explain the action. Intervening to set \(A=a\) breaks the causal link into \(A\), so it need not provide the same information about \(S\). In general,

\[
P(O\mid A=a,H)
\ne
P(O\mid \operatorname{do}(A=a),H).
\]

When the action is randomized independently of relevant background states, these quantities often coincide. More generally, they coincide when the conditioning information blocks the relevant noncausal associations, subject to the assumptions of the causal model. In such cases EDT and CDT agree.

It is important not to confuse EDT’s hypothetical conditioning with a claim that the agent literally receives an external report of her decision before making it. The conditional distribution is a way of evaluating alternatives from the present standpoint. Nor does EDT say that a later action changes the past. It says that the later action can be evidence about the past.

## Newcomb’s problem

The reference article’s central example is Newcomb’s problem. A predictor has already put either \$1 million or nothing in an opaque box \(B\). A transparent box \(A\) contains \$1,000. The agent can take only \(B\), or take both boxes. The predictor filled \(B\) if it predicted that the agent would take only \(B\).

Suppose the agent’s conditional probabilities are

\[
P(B\text{ full}\mid \text{one-box})=0.99,
\qquad
P(B\text{ full}\mid \text{two-box})=0.01.
\]

Then, using money as utility,

\[
V_{\mathrm E}(\text{one-box})
=0.99(\$1{,}000{,}000)=\$990{,}000,
\]

while

\[
\begin{aligned}
V_{\mathrm E}(\text{two-box})
&=0.01(\$1{,}001{,}000)
  +0.99(\$1{,}000)\\
&=\$11{,}000.
\end{aligned}
\]

EDT therefore recommends taking only \(B\). One-boxing is highly favorable news about what the predictor previously did.

There is a subtle probability assumption here. Saying only that the predictor is correct on 99% of all occasions does **not**, by itself, establish both conditional probabilities above. Overall accuracy is a weighted average and can conceal different error rates for the two choices. The numerical calculation requires the stated conditional relationships, or assumptions strong enough to imply them.

The causal argument goes the other way. By the time the agent chooses, the box contents are fixed. For either possible content of \(B\), taking both boxes yields \$1,000 more than taking only \(B\). On the standard causal model, choosing two boxes cannot alter the earlier prediction or filling of the opaque box, so CDT recommends two-boxing.

The disagreement is not over arithmetic. It is over which distribution belongs in the decision calculation. EDT compares the worlds associated with each choice; CDT compares the consequences of the available interventions. The one-boxer need not believe that her choice sends a signal backward in time. She needs only the evidential claim that her choice and the predictor’s earlier prediction are strongly correlated.

The numbers also show that one-boxing is not an unconditional EDT command. Write

\[
p_1=P(B\text{ full}\mid \text{one-box}),\qquad
p_2=P(B\text{ full}\mid \text{two-box}).
\]

One-boxing is preferred precisely when

\[
\$1{,}000{,}000(p_1-p_2)>\$1{,}000.
\]

If the action would convey too little information about the box, the extra \$1,000 can outweigh its evidential significance.

## Correlated decision-makers

A second way for actions to be evidence is through similarity between agents. In the reference article’s twin prisoner’s dilemma, an agent and her psychological twin separately choose whether to cooperate or defect. Their individual payoffs are:

| Agent’s choice | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$5 | \$0 |
| Defect | \$10 | \$1 |

If each knows that their decisions will match perfectly, then

\[
P(\text{twin cooperates}\mid \text{cooperate})=1,
\qquad
P(\text{twin cooperates}\mid \text{defect})=0.
\]

Thus

\[
V_{\mathrm E}(\text{cooperate})=5,\qquad
V_{\mathrm E}(\text{defect})=1.
\]

EDT recommends cooperation even for an agent who cares only about her own payout. Her cooperation is evidence of the twin’s cooperation; her defection is evidence of the twin’s defection.

Again, causation is not required. The agents might be in sealed rooms with no communication. Their common psychology, information and reasoning may nevertheless make their choices correlated. In a standard causal analysis where changing one agent’s choice does not change the twin’s, defection yields more regardless of what the twin does and is therefore causally dominant.

Perfect matching is a strong assumption. Let

\[
q_C=P(\text{twin cooperates}\mid \text{I cooperate}),\qquad
q_D=P(\text{twin cooperates}\mid \text{I defect}).
\]

Then

\[
V_{\mathrm E}(C)=5q_C,\qquad
V_{\mathrm E}(D)=10q_D+1(1-q_D)=1+9q_D.
\]

Cooperation is recommended exactly when \(5q_C>1+9q_D\). Similarity alone does not establish this inequality: the relevant question is how much the agent’s own action changes her conditional expectations about the twin.

## The “bad news” objection

Critics argue that EDT can confuse improving the world with receiving favorable evidence about it. The reference article quotes David Lewis’s characterization of EDT as an irrational policy of “managing the news.” A stylized example brings the concern into focus.

Suppose a genetic trait \(G\) causes both a strong desire to smoke and a disease. Smoking itself has no causal effect on the disease. Smoking gives the agent one unit of enjoyment; having the disease costs 100 units. At the decision point, assume

\[
P(G\mid \text{smoke})=0.20,\qquad
P(G\mid \text{abstain})=0.01.
\]

If the disease occurs exactly when \(G\) is present, EDT assigns

\[
V_{\mathrm E}(\text{smoke})=1-100(0.20)=-19,
\]

\[
V_{\mathrm E}(\text{abstain})=0-100(0.01)=-1.
\]

It recommends abstaining. Yet on the stated causal assumptions, abstention does nothing to prevent the disease and sacrifices the enjoyment. The causal critic says that abstention merely accompanies good news about a fixed trait.

An evidentialist can reply that actions are not independent “buttons” whose background associations may simply be ignored. If the specified conditional probabilities genuinely describe the agent’s situation, abstaining is associated with a better expected outcome. Whether that association is an adequate reason to act is exactly what the theories dispute.

There is also a practical challenge to the example. The agent may know the strength of her craving, medical test results, or other information that explains the correlation. Once that information is included in \(H\), the action might provide little further evidence about \(G\):

\[
P(G\mid \text{smoke},H)\approx P(G\mid \text{abstain},H).
\]

Then EDT may recommend smoking for its enjoyment. This is not a general refutation of the objection: in some models a residual correlation remains after conditioning on everything the agent knows. It is a reminder that EDT’s verdict depends on the information actually available, not on an unconditional correlation chosen for the illustration.

## Applying EDT to policies and sequential choices

Many decisions concern plans rather than isolated acts: “If the test is positive, seek treatment; otherwise wait.” A policy \(\pi\) maps possible future observations to actions. A natural evidential evaluation is

\[
V_{\mathrm E}(\pi\mid H)
=
\mathbb E[U\mid \Pi=\pi,H],
\]

where \(\Pi=\pi\) denotes the event that the agent adopts or follows the policy. Outcomes must include the observations and later actions generated under that policy.

The reference article states the action-based rule but does not settle every question about policy evaluation. The following is an operational proposal: specify the policy as precisely as the decision requires, model how its adoption is correlated with predictors, other agents and future observations, and condition on the event actually being evaluated. A policy’s evidential value need not equal the value of conditioning only on the particular move it eventually prescribes. The fact that someone adopted a conditional plan can itself carry information.

Sequential decisions can therefore be dynamically delicate. A policy preferred before receiving information need not prescribe the action preferred after receiving that information. An agent might, for example, initially favor a plan whose adoption is good evidence about a predictor, then later find that deviating gives a better value conditional on what she has since learned. Whether she can commit, what the predictor observes, and whether she is evaluating adoption, execution, or a particular later action must be included in the model. There is no general license to treat these as interchangeable events.

Randomization also needs explicit modeling. A fair coin used to select between actions can weaken the connection between the realized action and the agent’s underlying disposition. But if a predictor can predict the coin, or predicts the policy rather than the realized action, the dependency may remain. To evaluate “flip a coin” as a policy, condition on adopting that policy and average over its possible results—not automatically on the same conditional probabilities assigned to deliberate one-boxing and two-boxing.

## What if an alternative has probability zero?

The basic formula requires \(P(A=a\mid H)>0\). This creates a problem if an agent is certain what she will do but still wants to evaluate another available action. Ordinary conditional probability does not determine \(P(O\mid A=a,H)\) when the conditioning event has probability zero. The reference article’s formula leaves this issue open.

One possible operational response is to use a *trembling* model: assign small positive probabilities to alternatives, compute the conditional values, and consider a limit as those probabilities approach zero. But different ways of introducing the small probabilities can give different answers. If an unlikely action is modeled as a random slip, it may carry little evidence about the agent’s dispositions; if it is modeled as evidence of a different disposition, it may carry a great deal.

Thus the limit is not a mechanical solution without further assumptions. The model must say what makes each alternative possible and how that possibility relates to predictors and background states. Alternatively, an agent can maintain modest uncertainty about her eventual choice while deliberating. Either approach is an additional modeling commitment, not a consequence of the elementary EDT equation.

## Other applications and limits

The reference article notes applications of EDT to the Sleeping Beauty problem, where an agent may awaken once or more than once depending on a coin flip, with memory erased between awakenings. The problem raises questions about self-locating probability: what should Beauty believe when she wakes without knowing which awakening it is?

Decision recommendations depend not only on her credences but also on the betting protocol—whether a bet is offered on each awakening, whether identical choices are linked, and how payments across awakenings are counted. EDT has been proposed as a way to avoid certain Dutch books, or sets of individually acceptable bets that produce a guaranteed loss. The reference also reports Conitzer’s argument that agents assigning probability \(1/2\) to heads can remain vulnerable to Dutch books even when using EDT. The safe conclusion is not that EDT automatically resolves Sleeping Beauty, but that probability, action dependence and the full payoff structure must be specified together.

The article also mentions an “evidentialist’s wager”: even someone uncertain whether EDT is correct might give it considerable practical weight if evidential correlations connect a choice to many other agents’ outcomes. That is a further argument about decision-theoretic uncertainty, not a theorem of EDT itself. Its force depends on how rival theories and their stakes are compared, including how utilities are made commensurable across theories.

## A procedure for unfamiliar cases

For practical use, the following checklist separates the main modeling choices from the final maximization:

1. **Fix the decision and information.** Identify the available actions or policies and the information \(H\) the agent has now.
2. **Specify outcomes and utilities.** Include all consequences the agent values, across agents and times where relevant.
3. **Model dependencies.** Ask what the action would indicate about hidden states, earlier predictions, other decision-makers and future observations. Do not assume a correlation merely because an example resembles Newcomb’s problem.
4. **Calculate conditional distributions.** For each alternative, estimate \(P(O\mid A=a,H)\), checking that the conditioning event is well defined and has positive probability.
5. **Compute and compare expected utilities.** Choose an action with maximal evidential value; treat ties as permitted alternatives unless another principle breaks them.
6. **Check the framing.** If the choice concerns a policy, commitment, randomization or a sequence of decisions, verify that the conditioned event is the one actually under consideration.

For comparison with CDT, construct a causal model and ask how outcomes would differ under interventions. A disagreement between the two calculations is not, by itself, an error in either: it identifies the philosophical choice between evaluating an act as evidence and evaluating its causal consequences.

## Conclusion

EDT is expected-utility maximization using probabilities conditional on the agent’s own action. Its distinctive power is to bring predictors, common causes and correlated decision-makers into the evaluation without pretending that every correlation is causal. Its distinctive difficulty is that favorable evidence can seem like a poor substitute for causal control.

The formula is simple; applying it well is not. A useful EDT analysis must make the agent’s information, action probabilities, dependencies and payoffs explicit—especially when policies, randomization or zero-probability alternatives are involved.

### References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, “[Counterfactuals and Two Kinds of Expected Utility](https://www.econstor.eu/bitstream/10419/220553/1/cmsems-dp0194.pdf),” 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy* 59, 1981.
- Vincent Conitzer, “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists,” *Synthese* 192, 2015.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/a5a5ab47-de61-417b-9e7b-6da087159717/call_0/request.json)

[Authoritative raw response](../../../../../../runs/a5a5ab47-de61-417b-9e7b-6da087159717/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/a5a5ab47-de61-417b-9e7b-6da087159717/call_1/request.json)

[Authoritative raw response](../../../../../../runs/a5a5ab47-de61-417b-9e7b-6da087159717/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
