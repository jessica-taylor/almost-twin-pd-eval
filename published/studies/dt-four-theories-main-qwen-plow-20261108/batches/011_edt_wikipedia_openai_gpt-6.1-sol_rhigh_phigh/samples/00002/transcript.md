# 011_edt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00002

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f75b21a2-f3ae-4a3a-a1cc-764ed31f0d61/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f75b21a2-f3ae-4a3a-a1cc-764ed31f0d61/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing by What Your Action Reveals

Evidential decision theory (EDT) recommends choosing the action whose occurrence would be the best news about the world. As the supplied reference article puts it, one should “do what you most want to learn that you will do.” This is not an instruction to prefer comforting beliefs. The object of evaluation is still the actual outcome and its utility. What distinguishes EDT is the probability distribution used to evaluate that outcome: the distribution **conditional on performing the action**.

Usually, actions that predict good results also cause good results. The distinction becomes important when an action reveals something about a predictor, an independently acting counterpart, or an underlying condition. EDT counts such evidential relationships even when they are not causal influences.

This essay develops the article’s central rule, explains its applications, and identifies additional modeling assumptions needed to make it operational in unfamiliar cases.

## 1. The basic mathematical rule

Consider a finite set of available actions \(\mathcal A\). Let \(E\) represent the agent’s current information, and let \(O_1,\ldots,O_n\) be mutually exclusive, exhaustive outcomes. A utility function \(u(O_j)\) represents the agent’s preferences.

The evidential value of action \(a\) is

\[
V_E(a)
=
\sum_{j=1}^n
P(O_j\mid E,A=a)\,u(O_j).
\]

EDT recommends any action satisfying

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a).
\]

This is the supplied article’s formula with current information made explicit. Equivalently, if \(U\) is the random variable giving the utility of the complete outcome,

\[
V_E(a)=\mathbb E[U\mid E,A=a].
\]

The instruction is hypothetical: before acting, compare what each possible action would tell you. It is not necessary actually to perform an action and then learn that it occurred.

A useful alternative representation separates the action from a payoff-relevant state \(S\):

\[
V_E(a)=\sum_s P(S=s\mid E,A=a)\,u(a,s).
\]

Here \(u(a,s)\) includes both the action’s benefits and costs and whatever happens in state \(s\). The key feature is that the probability assigned to the state may depend on which action is being evaluated.

Several qualifications matter.

First, utilities need not be monetary. They may incorporate risk aversion, other people’s welfare, or preferences over complete histories. The numerical examples below treat money as utility for simplicity.

Second, \(E\) should contain the agent’s relevant information. An action can be evidence before some information is known but cease to be evidence afterward.

Third, the rule presupposes a joint probability model relating actions and outcomes. EDT tells us how to use that model; it does not, by itself, supply its probabilities.

## 2. Conditioning, causation, and counterfactuals

The central disagreement between EDT and causal decision theory (CDT) concerns what should vary when an action is considered.

The reference article presents CDT using probabilities of counterfactual conditionals:

\[
V_{\mathrm{CDT}}(a)
=
\sum_j P(a\mathrel{\Box\!\rightarrow}O_j\mid E)\,u(O_j).
\]

In a structural causal model, a familiar implementation uses interventions:

\[
V_{\mathrm{CDT}}(a)
=
\mathbb E[U\mid E,\operatorname{do}(A=a)].
\]

The intervention notation is an operational rendering of the contrast, not a definition of every philosophical version of CDT. An intervention sets the action while severing its ordinary causal dependence on its upstream determinants. Conditioning does not sever that dependence.

For example, suppose an unobserved variable \(L\) influences both an action and an outcome:

\[
A\leftarrow L\rightarrow O.
\]

Learning the action can change the probability of \(L\), thereby changing the probability of \(O\). Setting the action by intervention need not do either.

EDT retains this evidential update. It does **not** assert that choosing an action changes the past or causally controls \(L\). Rather, it evaluates the worlds in which that action occurs, including what its occurrence indicates about their other features.

The two theories agree when their relevant probability distributions agree. A sufficient condition is

\[
P(O_j\mid E,A=a)
=
P(O_j\mid E,\operatorname{do}(A=a))
\]

for every action and outcome. Many ordinary decision models effectively assume this condition. For example, if the agent’s choice reveals nothing about tomorrow’s weather beyond an already known forecast, conditioning on taking an umbrella introduces no additional weather evidence.

Thus EDT is not a rejection of causal effects. Those effects remain part of its conditional outcome distributions. Its distinctive commitment is to count noncausal evidence as well.

## 3. Newcomb’s problem

The reference article’s principal example is Newcomb’s problem.

A transparent box contains \(b=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A reliable predictor has already filled the opaque box:

- it contains \(M\) if the predictor predicted that the player would take only that box;
- it contains nothing if the predictor predicted that the player would take both boxes.

Let \(A=1\) mean taking only the opaque box, \(A=2\) taking both, and \(F=1\) mean that the opaque box is full. Define

\[
p_1=P(F=1\mid E,A=1),
\qquad
p_2=P(F=1\mid E,A=2).
\]

Then

\[
V_E(1)=Mp_1,
\qquad
V_E(2)=b+Mp_2.
\]

Consequently, EDT recommends one-boxing exactly when

\[
M(p_1-p_2)>b.
\]

This inequality is more informative than the slogan that EDT always one-boxes. Its verdict depends on the strength of the evidential relationship and the relative stakes.

Under the symmetric conditional-reliability assumptions used in the article’s calculation,

\[
p_1=0.99,\qquad p_2=0.01,
\]

so

\[
V_E(1)=\$990{,}000,
\qquad
V_E(2)=\$11{,}000.
\]

More generally, if \(p_1=q\) and \(p_2=1-q\), one-boxing wins when

\[
q>\frac12+\frac{b}{2M}.
\]

For these prizes, the threshold is \(0.5005\).

There is a statistical subtlety here: a predictor’s *overall* accuracy of \(99\%\) does not alone establish both conditional probabilities above. Aggregate accuracy can conceal unequal performance across actions. Applying EDT requires the relevant conditional probabilities, or enough information to derive them.

CDT instead treats the box’s already-fixed contents as unaffected by the current act. Holding those contents fixed, taking both boxes adds \(\$1{,}000\). EDT rejects that as the appropriate comparison: one-boxing and two-boxing are evidence for different distributions over those fixed contents.

The disagreement is therefore not about whether present actions physically reach backward in time. It concerns whether evidentially different pasts belong in the comparison.

## 4. Cooperation with a psychological twin

The reference also considers a prisoner’s dilemma against a psychological twin. Each player receives:

\[
\begin{array}{c|cc}
 & \text{Twin cooperates} & \text{Twin defects}\\
\hline
\text{Cooperate} & 5 & 0\\
\text{Defect} & 10 & 1
\end{array}
\]

Suppose the players’ choices are perfectly correlated:

\[
P(C_{\mathrm{twin}}\mid C)=1,
\qquad
P(C_{\mathrm{twin}}\mid D)=0.
\]

Then

\[
V_E(C)=5,
\qquad
V_E(D)=1,
\]

so EDT recommends cooperation even when the agent cares only about her own payment.

Neither communication nor causal control is required. Her choice is evidence about the independently made choice of someone who reasons similarly.

Perfect similarity is stronger than necessary. Write

\[
r=P(C_{\mathrm{twin}}\mid C),
\qquad
s=P(C_{\mathrm{twin}}\mid D).
\]

Then

\[
V_E(C)=5r,
\qquad
V_E(D)=1+9s.
\]

Cooperation is recommended precisely when

\[
5r>1+9s.
\]

For symmetric matching reliability \(q\), where \(r=q\) and \(s=1-q\), this becomes

\[
q>\frac57.
\]

The lesson is not that EDT recommends cooperation with everyone. If the other player’s action is independent of one’s own, then \(r=s\), and defection wins. What matters is a sufficiently strong, justified evidential relationship.

## 5. The objection: merely managing the news?

The supplied article reports a central criticism associated with David Lewis and James Joyce: rational action should produce good outcomes, not merely indicate them. Newcomb-style reasoning can look attractive, but the same formal principle can have less attractive consequences.

Consider the following additional example, not developed in the reference.

An agent chooses whether to smoke. Smoking gives utility \(1\). A disease imposes utility \(-100\), but smoking does not cause the disease. Instead, an underlying condition makes both smoking and disease more likely. Suppose the agent’s information supports

\[
P(D=1\mid E,\text{smoke})=0.9,
\qquad
P(D=1\mid E,\text{abstain})=0.1.
\]

EDT calculates

\[
V_E(\text{smoke})=1-100(0.9)=-89,
\]

\[
V_E(\text{abstain})=-100(0.1)=-10.
\]

It recommends abstaining, despite the assumption that smoking has no causal effect on disease.

The causal objection is sharp: declining a pleasurable activity does not cure an underlying condition. EDT’s reply, at the level of its formal rule, is equally clear: abstention is associated with a much better expected outcome. The normative dispute is whether that association should guide choice.

The example also shows why conditioning information matters. Suppose the agent observes a variable \(L\) that completely screens off the action–disease association:

\[
D\perp A\mid E,L.
\]

Now both actions receive the same conditional disease probability, and

\[
V_E(\text{smoke}\mid L)
-
V_E(\text{abstain}\mid L)
=1.
\]

EDT recommends smoking.

This does not establish that all objections disappear once agents introspect carefully. Whether an agent knows enough to screen off an association is a substantive modeling question. Assuming that every relevant determinant of choice is already known would remove much of EDT’s distinctive application by assumption.

Nor does EDT recommend ignoring unwelcome evidence. Its instruction is to use the information actually available and evaluate actual outcomes—not to substitute pleasant beliefs for utility.

## 6. What does it mean to condition on one’s own choice?

An ordinary statistical observer can condition on another person’s action. Conditioning on one’s own still-unsettled action raises additional problems.

### A forecasting model of deliberation

An operational interpretation is to use a joint probability model formed while deliberation remains unresolved. That model describes uncertainty about hidden states, one’s eventual action, and other agents’ behavior.

Each candidate action is evaluated using a different conditional distribution from this **same** model. One should not construct a favorable model for one action and an unfavorable model for another.

This interpretation goes beyond the reference’s displayed formula by specifying how it might be applied. It also exposes a limitation: EDT does not uniquely determine a rational agent’s probabilities over its own eventual choices.

Those probabilities cannot be read mechanically from population statistics. A correlation between smoking and disease in a population, for instance, may be irrelevant after conditioning on everything this particular agent knows.

### Zero-probability actions

Ordinary conditional probability requires

\[
P(A=a\mid E)>0.
\]

If the model assigns an alternative action probability zero, the ratio

\[
P(O\mid E,A=a)
=
\frac{P(O,A=a\mid E)}{P(A=a\mid E)}
\]

does not define its value.

This matters when an agent is certain of its own deterministic reasoning. The reference does not resolve the problem.

A practical convention is to use a full-support model of unresolved deliberation, assigning every genuinely available action positive probability. Another is to introduce small probabilities of deviations and examine a limit. Neither method is uniquely mandated by EDT. Different explanations of rare deviations can produce different conditional distributions even as deviation probabilities approach zero.

Consequently, a careful application should state how alternative actions receive evidential meaning and test whether the recommendation depends on that assumption. Replacing an undefined conditional with an intervention would silently switch decision theories.

### Correlation is not automatic logical control

Similarly, describing two agents as copies does not, without further modeling, specify every relevant probability. Their information, inputs, and possible sources of divergence matter.

EDT uses whatever dependencies the justified joint model contains. Its basic formula supplies no separate rule for changing mathematical facts, rewriting another algorithm’s output, or propagating a “logical counterfactual.” Such machinery would be an additional theory, not ordinary conditioning alone.

## 7. From individual actions to policies

A policy specifies actions across possible information states. For a finite decision problem, write

\[
\pi:\mathcal H\rightarrow\mathcal A,
\]

where \(\mathcal H\) is the set of relevant observation histories.

The reference chiefly describes individual actions. A natural—but additional—policy-level extension introduces a random variable \(\Pi\) representing the policy eventually adopted and evaluates

\[
V_E(\pi)=\mathbb E[U\mid E,\Pi=\pi].
\]

Here \(U\) should represent the utility of the entire resulting history. This formulation preserves EDT’s central idea: adopting a policy can be evidence about predictors, other agents’ policies, or hidden conditions.

But it requires a probability model over policies. One must not silently replace the expression with

\[
\mathbb E[U\mid E,\operatorname{do}(\Pi=\pi)],
\]

which evaluates a causal intervention on policy selection.

Policy evaluation and later action evaluation are also distinct. After observing history \(h\), act-level EDT compares

\[
\mathbb E[U\mid E,H=h,A=a].
\]

There is no general guarantee that these local rankings implement the policy favored earlier. The conditioning events differ. Commitment and sequential consistency therefore require analysis rather than being automatic consequences of the one-step formula.

Randomization introduces another distinction. If a coin is independent of a hidden state, its result supplies no evidence about that state conditional on the decision to use it. But choosing a randomized policy may itself be informative. “Randomize” is therefore not a universal method for eliminating evidential dependencies.

These issues are especially important in repeated decisions. The reference mentions disagreement about whether EDT protects certain “halfer” positions in Sleeping Beauty against Dutch books, including Conitzer’s argument that it does not. That discussion should not be read as a settled theorem. One must specify how awakenings are represented, which choices are linked by a common policy, and whether utility counts individual bets or total gains across the experiment.

## 8. A practical method

For an unfamiliar problem, an EDT analysis can proceed as follows:

1. **Specify the decision object.** Is the agent choosing a present action, a commitment, or a contingent policy?
2. **Specify information and utility.** Include known signals, relevant self-knowledge, costs, and the complete consequences the agent values.
3. **Build a joint model.** Identify causal effects, common causes, predictions, and dependencies between decision-makers.
4. **Condition on each alternative.** Compute the resulting expected utility without deleting merely noncausal correlations.
5. **Check modeling sensitivity.** Examine predictor calibration, screening-off information, zero-probability alternatives, and sequential consistency.

For example, the Newcomb recommendation is robust whenever

\[
p_1-p_2>\frac{b}{M}.
\]

There is no need to know both probabilities with arbitrary precision if their plausible ranges already establish this inequality.

The reference also mentions an “evidentialist’s wager”: correlated decisions across many agents may make evidential stakes large. This is a further argument, not part of EDT’s definition. Its force depends on the correlations, the utility function, and how uncertainty between decision theories is handled. Large numbers of correlated agents do not automatically matter to someone whose utility concerns only their own payment.

## Conclusion

EDT evaluates an action by the expected utility conditional on that action occurring. Its distinctive feature is that it retains evidential dependencies even when the action does not causally produce what it predicts.

That principle explains one-boxing and cooperation with a sufficiently correlated twin. It also generates the objection that EDT sometimes recommends managing signs of good fortune rather than producing good fortune. Applying it responsibly therefore requires more than identifying a correlation: one must specify information, utilities, a coherent joint model, and the meaning of conditioning on alternative actions or policies.

### References

- Wikipedia contributors. “Evidential decision theory.” [Supplied revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688). CC BY-SA 4.0. Primary source for this essay.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility,” 1976.
- Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192 (2015): 2887–2899.

The latter works are identified in the supplied article; the operational extensions above are distinguished from its claims.
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Crafting a detailed paper**

I need to keep the headings to about eight, aiming for a word count around 2750-2900. I think I can craft something around 2850 words with nine sections. I want to ensure that I'm accurately discussing the “when all outcomes have equal P conditional” aspect without overstating it. There's a detailed policy discussion I need to include, particularly about expanding the model with a variable representing the agent's policy and defining the expected utility accordingly.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5e323878-c4b7-45d7-b01d-1dc5c543fe36/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5e323878-c4b7-45d7-b01d-1dc5c543fe36/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5e323878-c4b7-45d7-b01d-1dc5c543fe36/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5e323878-c4b7-45d7-b01d-1dc5c543fe36/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating essay submission parameters**

I need to decide between submitting or passing an essay based on various conditions. It's important to evaluate the correlation between different probabilities while avoiding overthinking it. I’ll analyze the strengths of these correlations and establish outputs. Considering the same settings, the different leads shouldn’t matter. Even though independent sampling could happen, that doesn't mean I can treat outputs the same under uncertainty. I want to figure out the best way to use my essay effectively.**Choosing the right model**

I need to make a genuine choice about passing or modeling shared deliberative dispositions. It’s crucial to analyze if this decision can be justified. Both agents have the same numeric parameters, so they might make identical strategic choices while ignoring their private specifics. If we consider unresolved deliberative uncertainty, we might see a high correlation. The user pointed out differences that affect independent sampling, so I need to decide carefully. I should rationally opt for passing, given high confidence in my reasoning process.**Clarifying essay logic**

The essay emphasizes that logical control isn't automatic, and we shouldn't incorporate FDT inappropriately. I need a coherent model based on a shared latent "policy pattern." However, the internal dispositions and unresolved reasoning remain unclear. While the model weights are known, I lack detailed values. Thus, there's a common latent propensity, and I need to look at the distribution. For example, using a mixture with prior values can yield useful results like r at 0.905 and s at 0.095, which looks promising.
```
