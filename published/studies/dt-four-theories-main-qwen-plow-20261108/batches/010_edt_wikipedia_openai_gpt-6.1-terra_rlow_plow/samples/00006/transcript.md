# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00006

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/4043aa66-5e98-450c-b1ca-4a8d31d40880/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/4043aa66-5e98-450c-b1ca-4a8d31d40880/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential decision theory: choosing what you would want to learn

A decision can be good in two different senses. It can be a good *way of bringing about* an outcome, or it can be good *news about* the outcome. Ordinarily these assessments point in the same direction: taking an umbrella both keeps you dry and is evidence that you will stay dry. But they can come apart when your action is statistically associated with facts it does not cause.

Evidential decision theory, or **EDT**, treats the second assessment as fundamental. It recommends the action whose occurrence would be the best news, measured by expected utility. The slogan is: **do what you would most want to learn that you will do**.

This is not simply a recommendation to look for encouraging evidence. EDT asks an agent to compare the expected outcomes *conditional on each available action*, and then to perform an action maximizing that expectation. The resulting theory agrees with ordinary causal reasoning in many familiar problems. Its distinctive implications arise when actions reveal information about predictors, other decision-makers, or hidden features of the agent.

## 1. The basic rule

Suppose an agent has evidence \(E\), a set of available actions \(\mathcal A\), and a probability distribution over outcomes. For an action \(a\), define its evidential value by

\[
V_E(a)=\mathbb E[u(O)\mid E,A=a],
\]

where \(A\) is the action actually taken, \(O\) is the resulting outcome, and \(u\) is the agent’s utility function. With discrete outcomes \(o_1,\ldots,o_n\), this is

\[
V_E(a)=\sum_j P(O=o_j\mid E,A=a)\,u(o_j).
\]

EDT recommends any action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a).
\]

If the action itself matters—for example, if lying is intrinsically bad for the agent—its utility can be included by defining the outcome broadly enough, or by writing \(u(a,o)\).

The probability \(P(O=o_j\mid E,A=a)\) is an ordinary conditional probability: it describes how likely the outcome would be *upon learning* that action \(a\) occurs, given the agent’s present evidence. It need not describe what would happen if an external force intervened to set the action to \(a\).

The reference article presents this conditional-expectation rule and contrasts it with causal decision theory, or **CDT**. In a simple causal model, a CDT-style value can be written

\[
C_E(a)=\mathbb E[u(O)\mid E,\operatorname{do}(A=a)],
\]

where \(\operatorname{do}(A=a)\) represents an intervention that sets the action while leaving the rest of the model’s causal mechanisms intact. This notation is a convenient operational illustration; philosophical accounts of CDT differ in their treatment of causal counterfactuals.

The distinction is between conditioning and intervening. Conditioning on an action can change beliefs about its causes or correlates. An intervention generally breaks the causal arrows into the action, so that setting it does not itself supply information about those causes. When the two distributions agree, EDT and CDT agree about the action’s value. When they differ, their recommendations can differ too.

### A small model

Let \(H\) be an unobserved trait that influences both an agent’s choice \(A\) and a separate outcome \(O\):

\[
H\longrightarrow A,\qquad H\longrightarrow O.
\]

If people with trait \(H\) tend to choose \(a\), learning \(A=a\) is evidence for \(H\), and hence for whatever \(H\) predicts about \(O\). An intervention forcing \(A=a\), by contrast, need not change \(H\).

EDT counts the former evidential relationship. CDT asks what changing the action would causally accomplish. Neither the mere presence nor absence of an arrow settles the philosophical dispute: the question is which kind of comparison is appropriate for choosing.

## 2. Applying the rule

For an unfamiliar problem, a useful procedure is:

1. **Fix the decision point and evidence.** Include what the agent knows before choosing, but not what it would learn only from observing its eventual choice.
2. **Specify the alternatives.** These may be immediate acts, randomized procedures, or policies for responding to future observations.
3. **Specify outcomes and utilities.** Include the consequences and features of conduct that the agent values.
4. **Build a joint probability model.** Represent predictors, hidden variables, other agents, and the agent’s own prospective action.
5. **Condition separately on each alternative.** Calculate \(P(O\mid E,A=a)\), not merely an unconditional probability of the outcome.
6. **Compare conditional expected utilities.** Check how the result changes under plausible alternative probabilities.

The joint model is essential. EDT is not the rule “choose whatever sounds like good news”; it requires probabilities expressing *how strongly* each choice predicts each outcome. If the information given in a story does not determine those conditional probabilities, the decision may remain underdetermined.

It is also important that the utilities belong to the decision-maker. Dollar amounts can stand in for utility in simplified examples, but only if the agent values money approximately linearly over the relevant range.

## 3. Newcomb’s problem: evidence about a prediction

Newcomb’s problem separates evidential and causal assessment especially sharply. A transparent box contains \$1,000. An opaque box contains either \$1 million or nothing. A predictor has already filled the opaque box: it put in the million if it predicted that the agent would take only the opaque box, and left it empty if it predicted that the agent would take both.

Let \(B\) be taking only the opaque box and \(T\) taking both. Suppose, as in the reference article’s numerical calculation, that

\[
P(\text{opaque box full}\mid B)=0.99,
\qquad
P(\text{opaque box full}\mid T)=0.01.
\]

Taking dollars as utilities,

\[
V(B)=0.99(\$1{,}000{,}000)=\$990{,}000,
\]

whereas

\[
V(T)=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
=\$11{,}000.
\]

EDT therefore recommends **one-boxing**. The point is not that taking only the opaque box makes the predictor fill it retroactively. Rather, one-boxing is strong evidence that the prediction already made was a one-box prediction.

A causal analysis ordinarily recommends taking both. At the moment of choice the opaque box is already full or empty. Holding that past fact fixed, taking both adds \$1,000 either way. Thus two-boxing causally dominates one-boxing, even though it is much worse news about the opaque box.

The numerical premise deserves care. An overall predictor accuracy of 99%,

\[
P(\text{prediction matches choice})=0.99,
\]

does **not** by itself imply 99% accuracy conditional on each choice. The two conditional probabilities used above are stronger assumptions; their values depend on the base rates of choices and on the distribution of errors. Under less ideal prediction, if

\[
p_B=P(\text{full}\mid B),\qquad p_T=P(\text{full}\mid T),
\]

then EDT one-boxes exactly when

\[
\$1{,}000{,}000(p_B-p_T)>\$1{,}000.
\]

Thus the recommendation depends on the evidential difference between the actions, not on a magical property of opaque boxes.

## 4. Correlated decisions: the twin prisoner’s dilemma

The same logic applies without a predictor looking into the past. Suppose Aomame plays a prisoner’s dilemma against a psychological twin. Each chooses cooperate or defect in a separate room. Their payoffs to Aomame are:

| Aomame | Twin | Aomame’s payoff |
|---|---|---:|
| Cooperate | Cooperate | \$5 |
| Cooperate | Defect | \$0 |
| Defect | Cooperate | \$10 |
| Defect | Defect | \$1 |

If their decisions are perfectly correlated, then learning that Aomame cooperates reveals that her twin cooperates; learning that Aomame defects reveals that her twin defects. Therefore

\[
V(C)=\$5,\qquad V(D)=\$1,
\]

and EDT recommends cooperation.

Again, cooperation need not *cause* the twin to cooperate. Both choices may reflect similar reasoning and evidence. In an ordinary prisoner’s dilemma against an independently choosing opponent, conditioning on Aomame’s act might not change the probability of the opponent’s act; then defection would have the higher evidential value as well as the higher causal value.

Perfect correlation is not required. Write

\[
q_C=P(\text{twin cooperates}\mid C),\qquad
q_D=P(\text{twin cooperates}\mid D).
\]

Then

\[
V(C)=5q_C,\qquad
V(D)=10q_D+1(1-q_D)=1+9q_D.
\]

EDT cooperates when \(5q_C>1+9q_D\). This inequality makes the dependence explicit: similarity must provide enough favorable evidence to outweigh the temptation payoff. A mere assertion that two agents are “similar” does not determine the answer.

## 5. The criticism: managing the news

The strongest intuitive objection is that good news is not the same as good consequences. The reference article reports David Lewis’s characterization of EDT as an irrational policy of “managing the news,” and James Joyce’s contrasting insistence on causal efficacy. A medical example shows why the objection has force.

Suppose a hidden condition \(H\) makes people crave a certain snack and also makes them prone to a disease. Assume the snack has no causal effect on the disease. Before deciding, an agent’s probabilities are

\[
P(H)=0.1,\quad P(\text{eat}\mid H)=0.9,\quad
P(\text{eat}\mid \neg H)=0.1.
\]

For simplicity, suppose disease occurs exactly when \(H\) is present, disease has utility \(-100\), and eating provides a benefit of \(+2\). Bayes’s rule gives

\[
P(H\mid \text{eat})=\frac{0.1(0.9)}{0.1(0.9)+0.9(0.1)}=0.5,
\]

and

\[
P(H\mid \text{abstain})
=\frac{0.1(0.1)}{0.1(0.1)+0.9(0.9)}
=\frac1{82}.
\]

So the evidential values are approximately

\[
V(\text{eat})=2-100(0.5)=-48,
\qquad
V(\text{abstain})=-100/82\approx-1.22.
\]

EDT, applied to this model, recommends abstaining. Yet eating does not cause the disease, and abstaining does not remove the hidden condition. A causal theorist says that the agent is sacrificing the snack merely to make its action an encouraging symptom.

An evidentialist can reply that, conditional on the total evidence available at choice time, eating is bad news. But the conclusion is sensitive to what that evidence includes. If the agent already knows whether it has the craving, or knows \(H\), conditioning on its choice may add little or no information about disease. This is sometimes called a *screening-off* response: relevant background information can remove a spurious evidential association. It does not automatically answer every objection, since a hidden trait might remain informative even after all accessible evidence is included.

The example also warns against manipulating the probability model. One cannot simply announce that eating is “freely chosen” and therefore independent of \(H\). Independence must be justified by the model of how the decision is made.

## 6. Actions, policies, and randomization

The reference article formulates EDT in terms of actions. In extended problems, however, it may be natural to choose a **policy**: a rule specifying what to do after possible future observations. One can apply the same evidential idea to a policy variable \(\Pi\):

\[
V_E(\pi)=\mathbb E[u(O)\mid E,\Pi=\pi].
\]

This is an operational extension, not a unique prescription supplied by the source. Its usefulness is that a predictor or another agent may be correlated with a decision procedure rather than merely with one isolated physical movement. In a repeated interaction, for example, a policy of cooperating when the other agent has a reliable matching policy may be evidence that cooperation will be reciprocated.

But the description of the alternative matters. “Adopt a cooperative policy,” “cooperate on this occasion,” and “use a coin that happens to produce cooperation” are different events. They can have different evidential relationships to another agent’s behavior. A reader applying EDT should state which event is being conditioned on and why it is available to the agent.

Randomization illustrates the distinction. Let \(R\) be a fair coin physically independent of a hidden trait \(H\). Conditional on a genuinely adopted policy “follow \(R\),” the coin’s result supplies no evidence about \(H\). But the *adoption of that policy* might itself be correlated with \(H\), a predictor, or another agent’s policy. Independence of the coin is not necessarily independence of the decision to use it.

Sequential decisions raise another question. A policy preferred in advance need not be preferred at every later information state, because the later agent conditions on new evidence and possibly on earlier actions. One can evaluate whole policies at the initial point or reapply EDT locally at each later point, but these procedures need not agree without further assumptions. Commitment devices, the availability of later revision, and what each stage knows must therefore be modeled rather than assumed away.

## 7. What if an action has probability zero?

The basic formula presupposes that \(P(A=a\mid E)>0\). If an agent assigns probability zero to an available action, ordinary conditioning on that action is undefined. This is a serious issue when an agent is nearly certain what it will choose, or when a deterministic model makes some alternatives impossible.

The source’s basic rule does not uniquely resolve it. A possible operational proposal is to use a model in which each available action has a small positive probability, compute its conditional value, and consider a limit as those probabilities approach zero. For instance, one might model a small chance of error or exploration.

That proposal requires care: different ways of introducing tiny probabilities can yield different limiting conditionals. A rare action produced by a random slip may be weak evidence about a predictor; the same action produced by an unusual but predictable disposition may be strong evidence. Thus a “tremble” is not neutral. Its mechanism must represent the counterfactual comparison the analyst intends, and if reasonable mechanisms disagree, the model has not supplied a unique EDT verdict.

Nor does EDT require the agent to believe its eventual action is causally beyond its control. A probability distribution over one’s prospective act can represent uncertainty before deliberation, uncertainty in an outside model of the decision process, or uncertainty about the relevant features of that process. The interpretation should be made explicit, particularly where self-prediction is central.

## 8. Self-location and broader arguments

The reference article also notes applications to the Sleeping Beauty problem, in which an agent may awaken different numbers of times depending on a coin flip, with memory erased between awakenings. A decision analysis must specify not just a credence in heads but also how bets are offered and paid: once per experiment, once per awakening, or under some other arrangement. Those details determine the relevant outcomes and conditional expectations.

The article reports arguments that EDT can help a “halfer,” who assigns heads probability \(1/2\), avoid certain Dutch books, while also noting Vincent Conitzer’s argument that halfers using EDT can still be Dutch-booked. The lesson is not that EDT settles the sleeping-beauty dispute, but that decision rules, self-locating probabilities, and the structure of repeated bets interact.

Finally, the article mentions an “evidentialist’s wager”: even someone uncertain whether EDT is correct might give evidential considerations substantial weight because correlated decisions can affect—or indicate—large stakes. This is a proposal about decision-making under uncertainty between theories, not a proof of EDT. Its force depends on how the theories’ recommendations and utilities are compared and on whether the supposed correlations are credible.

## Conclusion

EDT evaluates an action by the expected utility of outcomes **conditional on that action occurring**. Its signature move is to count an action’s evidential relationships even when they are not causal: one-boxing can indicate a favorable prediction, and cooperation can indicate cooperation by a correlated twin.

To use the theory well, specify the agent’s evidence, alternatives, utilities, and joint probability model; then condition on each alternative without silently replacing conditioning by intervention. The unresolved questions—especially zero-probability actions, policy choice, and sequential revision—are not minor bookkeeping. They determine what the alternatives mean and which dependencies EDT is being asked to evaluate.

### References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, “Counterfactuals and Two Kinds of Expected Utility,” 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy* 59, 1981.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/0b38090e-07f5-4806-b08e-ea8c068a3a47/call_0/request.json)

[Authoritative raw response](../../../../../../runs/0b38090e-07f5-4806-b08e-ea8c068a3a47/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating selection criteria**

I’m considering the need to make a selection while keeping in mind that similar reasoning suggests there’s a high correlation within the action category. Despite that, I recognize there are private differences to account for, involving independent sampling uncertainty. I need to apply reasonable judgment, which means taking these factors into consideration as I proceed. It feels a bit complex, but I think with careful thought, I can come to a good decision.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/0b38090e-07f5-4806-b08e-ea8c068a3a47/call_1/request.json)

[Authoritative raw response](../../../../../../runs/0b38090e-07f5-4806-b08e-ea8c068a3a47/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering correlation judgment**

I need to figure out the correlation judgment. I see that the same model reasoning and symmetry strongly predicts matching results, even when using independent samples, despite the names being distinct and possibly irrelevant. There’s no fixed quantified correlation to rely on, so I’ll have to pass based on reasonable shared reasoning uncertainty. It’s quite a task, but I’m hoping to make a sound choice!
```
