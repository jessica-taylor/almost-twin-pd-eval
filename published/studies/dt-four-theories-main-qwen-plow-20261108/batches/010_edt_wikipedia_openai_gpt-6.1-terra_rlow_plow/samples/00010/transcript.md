# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00010

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/86632ab6-4973-422f-8991-bdfc9946e466/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/86632ab6-4973-422f-8991-bdfc9946e466/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential decision theory: choosing what you want to learn you will do

Suppose a doctor discovers that people who take a certain medicine tend to recover. That association might mean the medicine causes recovery. But it might instead mean that healthier patients are more likely to take it. A decision-maker must distinguish those possibilities when predicting the consequences of treatment.

Evidential decision theory, or **EDT**, asks a distinctive question about such dependencies. Rather than evaluating an action exclusively by what it causes, EDT evaluates it by what performing it would be *evidence of*. Its slogan is: do what you would most like to learn that you will do. The point is not that learning good news magically produces a good outcome. It is that, when an agent’s action is correlated with facts that matter, the action can provide information about those facts.

This distinction is most striking when an action is evidence about something it cannot cause: a predictor’s earlier decision, for example, or the simultaneous choice of a psychologically similar person. EDT can then recommend an action that a causal decision theory rejects.

The reference article presents EDT through a conditional expected-utility formula and contrasts it with causal decision theory. It also describes several thought experiments and criticisms. The account below follows that core presentation, while distinguishing it from additional proposals about how to apply the formula when the probability model or the choice of policy is unclear.

## 1. The basic rule

Let \(A\) range over the actions available to an agent, and let \(O_1,O_2,\ldots\) be mutually exclusive and exhaustive outcomes. Write \(D(O_j)\) for the agent’s utility, or desirability, of outcome \(O_j\). The source gives the evidential value of action \(A\) as

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

EDT recommends an action maximizing \(V(A)\).

In practice, the agent already has information at the time of choice. If that information is represented by \(K\), a more explicit formulation is

\[
V_K(A)=\mathbb E[D(O)\mid K,A]
      =\sum_j P(O_j\mid K,A)D(O_j).
\]

Here \(K\) should include the facts the agent actually knows: observations, memories, available options, and any relevant evidence about how the decision situation was created. The conditional \(P(O_j\mid K,A)\) asks what probability the agent assigns to outcome \(O_j\) on receiving the additional information that action \(A\) occurs.

The outcomes must include everything that affects utility. If an action has a cost, the outcome description must record it. If the agent values another person’s welfare, that too belongs in the utility function. Monetary payoffs can serve as utilities in simple examples, but only under the assumption that the agent values money linearly over the amounts involved.

The formula does not prescribe a particular probability distribution. Two evidential decision-makers with different evidence, priors, or utilities can rationally reach different conclusions. EDT supplies the **rule for using** those inputs, not all the inputs themselves.

The central operation is ordinary conditioning. When \(P(K,A)>0\),

\[
P(O\mid K,A)
=\frac{P(O,A\mid K)}{P(A\mid K)}.
\]

This allows the action to be evidence about any correlated feature of the world, whether the correlation arises from a causal effect of the action, a common cause, prediction, shared reasoning, or something else. Which correlations are credible is a substantive modeling question.

## 2. Conditioning is not intervention

The contrast with causal decision theory, or CDT, becomes clear in a simple causal model. Let \(S\) be a background state and suppose the outcome depends on both \(S\) and the action. An evidential calculation can be written as

\[
V_K(a)=\sum_s P(s\mid K,A=a)\,u(a,s).
\]

One familiar causal calculation instead holds fixed the distribution of the background state while varying the action:

\[
C_K(a)=\sum_s P(s\mid K)\,u(a,s),
\]

provided that \(S\) is causally prior to the action and that the model correctly represents what would happen under each intervention. More generally, a causal model may use

\[
C_K(a)=\mathbb E[u(O)\mid K,\operatorname{do}(A=a)],
\]

where \(\operatorname{do}(A=a)\) represents an intervention setting the action rather than merely observing it.

These expressions need not agree. Observing that \(A=a\) may change one’s beliefs about \(S\); intervening to set \(A=a\) need not. Conversely, when the action is independent of relevant background states given \(K\), and the causal model has the required structure, the two calculations agree.

The source expresses CDT using probabilities of counterfactuals: roughly, how likely each outcome would be *if* the action were performed. Such counterfactuals require an account of which features of the world are held fixed and which change. EDT’s standard formula instead uses the ordinary conditional distribution. It does not deny that causal counterfactuals are meaningful; it denies that they always provide the right probabilities for evaluating a choice.

The philosophical dispute is therefore not simply whether actions have causes or consequences. Both theories can recognize both. The disagreement is whether rational choice should track the expected outcome *conditional on the action* or the expected outcome under an appropriately specified causal intervention.

## 3. Newcomb’s problem

Newcomb’s problem makes the difference vivid. A predictor has already filled an opaque box \(B\) according to a prediction of the player’s choice. If the predictor expected the player to take only \(B\), it put \$1 million inside. If it expected the player to take both boxes, it left \(B\) empty. A transparent box \(A\) contains \$1,000. The player chooses either \(B\) alone or both boxes.

For the numerical calculation in the source, assume

\[
P(B\text{ full}\mid \text{one-box})=0.99
\]

and

\[
P(B\text{ full}\mid \text{two-box})=0.01.
\]

Assuming linear utility for money, EDT assigns

\[
V(\text{one-box})
=0.99(\$1{,}000{,}000)+0.01(\$0)
=\$990{,}000,
\]

while

\[
V(\text{two-box})
=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
=\$11{,}000.
\]

It therefore recommends taking \(B\) alone.

The evidential reasoning is that one-boxing would be strong evidence that the predictor predicted one-boxing, and hence that the opaque box is full. Two-boxing would be strong evidence of the opposite prediction. EDT does not have to say that the current choice travels backward in time and fills the box.

A standard causal analysis takes the box’s contents as already fixed and unaffected by the player’s present action. For either possible content, taking both boxes yields \$1,000 more than taking only \(B\). CDT therefore two-boxes.

There is a useful numerical qualification. A bare statement that the predictor is “99% accurate” does **not** by itself imply both conditional probabilities above. Aggregate accuracy can coexist with different error rates for one-boxers and two-boxers. The displayed values require the stronger conditional assumptions, or a probability model that entails them. This matters in unfamiliar cases: a general description of a correlation should not silently be substituted for the particular conditionals that EDT needs.

More generally, put

\[
p_1=P(B\text{ full}\mid\text{one-box}),\qquad
p_2=P(B\text{ full}\mid\text{two-box}).
\]

With the same payoffs, EDT one-boxes exactly when

\[
1{,}000{,}000p_1
>
1{,}000+1{,}000{,}000p_2,
\]

or

\[
p_1-p_2>0.001.
\]

Thus the prescription depends on the evidential advantage of one-boxing being large enough to outweigh the certain \$1,000 forgone. The strength of prediction matters, not merely its existence.

## 4. A psychological twin

In the source’s twin prisoner’s dilemma, Aomame chooses whether to cooperate or defect against a psychological twin in another room. Each gets \$5 if both cooperate and \$1 if both defect. A defector against a cooperator gets \$10; the cooperator gets nothing. Aomame cares only about her own payoff.

If her reasoning and circumstances are such that her choice is perfectly correlated with her twin’s, then

\[
P(\text{twin cooperates}\mid\text{Aomame cooperates})=1,
\]

and

\[
P(\text{twin cooperates}\mid\text{Aomame defects})=0.
\]

Consequently,

\[
V(\text{cooperate})=\$5,\qquad
V(\text{defect})=\$1.
\]

EDT recommends cooperation, even though Aomame’s act has no ordinary causal effect on the twin’s simultaneous act. Her choice is evidence of the twin’s choice because the two arise from sufficiently similar reasoning.

Perfect correlation is not essential. Let

\[
q_C=P(\text{twin cooperates}\mid\text{Aomame cooperates}),
\]
\[
q_D=P(\text{twin cooperates}\mid\text{Aomame defects}).
\]

Then

\[
V(C)=5q_C,\qquad
V(D)=10q_D+1(1-q_D)=1+9q_D.
\]

Cooperation is recommended exactly when

\[
5q_C>1+9q_D.
\]

This makes the limitation clear. Mere similarity does not guarantee cooperation: the evidential relationship must be strong enough. Nor should an agent assume that every person who faces the same problem will act as they do. Independent randomization, different information, different utilities, or different reasoning can weaken the relevant conditional dependence.

## 5. The objection: managing the news

The same feature that produces these recommendations also motivates a famous criticism. The source reports David Lewis’s objection that EDT promotes an irrational policy of “managing the news,” and James Joyce’s claim that action should be guided by causal efficacy rather than auspiciousness.

Consider a simplified medical case. An underlying condition \(G\) makes a person both more likely to enjoy smoking and more likely to develop a disease. Suppose, for this example, smoking itself has **no causal effect** on the disease, and the person prefers smoking to abstaining by one utility unit. Before choosing, the person assigns

\[
P(G\mid\text{smoke})=0.8,\qquad
P(G\mid\text{abstain})=0.2.
\]

Let the loss from \(G\) be ten units. Then, taking abstention’s direct utility as zero,

\[
V(\text{smoke})=1-10(0.8)=-7,
\]
\[
V(\text{abstain})=0-10(0.2)=-2.
\]

EDT as modeled recommends abstention. A causal analysis says that abstention cannot change whether the person has \(G\), so smoking is better by one unit in either state. The critic asks: why give up something enjoyable merely because doing so would be good news about an already settled condition?

An evidentialist can respond that the calculation uses the best available correlations: among people who abstain, the bad condition is less common. But the example also exposes a delicate issue about **current information**. If the agent already knows the relevant inclination to smoke, and that knowledge screens off the action from \(G\), then

\[
P(G\mid K,\text{smoke})=
P(G\mid K,\text{abstain}),
\]

and EDT recommends smoking. This is sometimes called a screening-off or “tickle” style response: once the informational basis of the choice is known, the choice may supply no further bad news.

That response is not automatic. The relevant inclination might not be fully observable; the action might reveal aspects of the agent not contained in \(K\). One must model what the agent actually knows rather than simply declare the correlation screened off. The dispute concerns both the decision rule and the appropriate representation of an agent’s self-knowledge.

## 6. How to construct an evidential model

The source’s formula is compact, but applying it to a new problem requires choices the formula alone does not settle. The following is an operational proposal, not an additional rule stated by the source.

**First, specify the decision and information.** Identify the alternatives available at the same decision point and record \(K\). If the agent has observed a test result or knows a predictor’s method, include that information in every comparison. Do not condition on facts that would only become known after choosing unless the decision is explicitly a contingent policy.

**Second, define outcomes and utility.** Include direct costs, delayed effects, other people’s welfare if relevant, and uncertainty about all of them. Where a consequence depends on the action itself, include the action in the outcome description or use a utility function \(u(a,s)\).

**Third, build a joint probability model.** The model should describe how actions and relevant states are correlated under the agent’s current uncertainty. A causal diagram can help identify plausible dependencies, but EDT’s evaluation uses the resulting conditional probabilities, not just arrows from action to outcome. Ask what common causes, prediction mechanisms, information channels, and shared decision procedures could produce the correlations.

**Fourth, calculate each conditional value.** Evaluate \(\mathbb E[u\mid K,A=a]\) for each alternative and compare them. A dependency should be used only if supported by the model; it should not be invented to favor a desired verdict.

**Fifth, test sensitivity.** Vary uncertain correlations, utilities, and assumptions about self-knowledge. Thresholds such as those derived above show when a verdict changes. This is especially important when the problem statement says only that a predictor is “reliable” or that another agent is “similar.”

There is a modeling tension here. If an agent is certain that its own reasoning deterministically selects one particular action, it may assign zero probability to the alternatives. Yet it still wants to evaluate them. The bare EDT formula does not define \(P(O\mid K,A=a)\) when \(P(A=a\mid K)=0\).

One possible operational response is to retain genuine uncertainty about one’s decision procedure or its inputs while deliberating. Another is to evaluate nearby models in which each action has a small positive probability and take a limit. But different nearby models can yield different limits, so this is not a universal solution. A third approach is to introduce an explicit counterfactual or revised model for impossible alternatives; that requires assumptions beyond ordinary conditioning. The source’s formula leaves this zero-probability problem open.

A related warning concerns **randomization**. If a physical randomizer is genuinely independent of the predictor’s earlier act, then conditional on the randomizer’s outcome the predictor need not be especially likely to have predicted that outcome. But the predictor might have anticipated the use of the randomizer or possessed information about it. One must model the actual correlation, not assume either independence or perfect prediction.

## 7. Acts, policies, and sequential choices

Sometimes the meaningful alternative is not a single immediate act but a policy: a rule specifying what the agent will do after various possible observations. Let \(\pi\) denote such a rule and \(U\) the utility of the resulting whole history. A natural evidential extension is

\[
V_K(\pi)=\mathbb E[U\mid K,\Pi=\pi],
\]

provided that the policy variable \(\Pi\) and its correlations with the world are defined in a joint model.

This is a proposal for applying the source’s conditional-value idea to policies. It is not a claim that the source settles every issue about policy choice. In particular, conditioning on adopting a policy can provide evidence about a predictor, another agent, or future information. That may differ from conditioning on one isolated act after the information arrives.

For example, an agent might today choose a policy to cooperate whenever paired with a sufficiently similar twin. The fact that the agent adopts that policy could be evidence that the twin adopts the same policy. Later, after receiving new information, the agent might reevaluate an individual act. Whether the original recommendation remains preferred depends on the new conditional probabilities. A full sequential analysis must specify what is known at each stage and whether the agent is choosing a binding commitment or merely announcing an intention.

The source mentions Sleeping Beauty as another setting where the unit of evaluation matters. In versions of that problem, a sleeping subject may be awakened a different number of times depending on a coin toss, with memory erased between awakenings. Arguments about betting and Dutch books depend on what counts as a bet, how often it is offered, and how payoffs accumulate across awakenings. The article notes a dispute: some argue that EDT can help an agent with a one-half credence avoid certain Dutch-book arguments, while Vincent Conitzer argues that such “halfers” remain vulnerable in a relevant setup. The general lesson is not that EDT alone settles the credence dispute, but that a complete analysis needs a policy and payoff model for the entire sequence.

## 8. Why take evidential links seriously?

EDT’s appeal is clearest when an agent’s choice is a reliable sign of other consequential decisions. A predictor may have studied the agent; a twin may reason similarly; a population of agents may respond to comparable arguments. In such cases, focusing exclusively on what one isolated act physically causes can seem to ignore information carried by the act itself.

The source also notes an argument for acting as if EDT were true even under uncertainty about decision theory: correlated decisions may raise the stakes of evidential reasoning. That is a further argument, not a theorem of EDT. Its force depends on how uncertainty over theories is handled, how their recommendations are compared, and whether the alleged correlations really exist. Large stakes alone do not establish a particular conditional probability.

The competing intuition remains powerful. If an adverse condition is already fixed, avoiding an enjoyable act because it is associated with that condition can look like sacrificing welfare to obtain a favorable diagnosis. Newcomb’s problem and the smoking case pull in opposite intuitive directions, and neither is resolved merely by repeating “correlation is not causation.” EDT deliberately gives some noncausal correlations decision-theoretic significance; its critics question whether that significance is rational.

## Conclusion

EDT evaluates an action by the expected utility conditional on its being performed. This makes an action’s evidential relationship to predictors, other agents, and hidden states central to choice. The rule is mathematically simple, but its application requires a careful joint probability model, an explicit account of current information, and attention to whether the alternatives are acts or policies.

The theory’s distinctive promise is that it takes predictive and psychological dependencies seriously. Its central challenge is to explain why favorable evidence should sometimes guide action when the associated good outcome is not causally produced by that action.

### References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688, the supplied reference article.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- Vincent Conitzer, “A Dutch book against sleeping beauties who are evidential decision theorists,” *Synthese* 192, 2015.
- David Lewis, “Causal decision theory,” *Australasian Journal of Philosophy* 59, 1981.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/06f0f971-8403-4051-882a-961201ffb340/call_0/request.json)

[Authoritative raw response](../../../../../../runs/06f0f971-8403-4051-882a-961201ffb340/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Choosing correlation**

I need to choose a correlation. I’m thinking about how to reason through this in an abstract scenario, which feels a bit irrelevant since it’s private. However, I can find a strong correlation that’s plausible. Maybe I’ll use independent sampling, but I want to ensure that my choice is coherent and symmetric. Okay, I’ll pass on that for now.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/06f0f971-8403-4051-882a-961201ffb340/call_1/request.json)

[Authoritative raw response](../../../../../../runs/06f0f971-8403-4051-882a-961201ffb340/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
