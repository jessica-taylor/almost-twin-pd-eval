# 011_edt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00006

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d781b491-b721-481a-a74e-1827d2ba8e6d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d781b491-b721-481a-a74e-1827d2ba8e6d/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing by What Your Action Reveals

A decision can matter in two different ways. It can change the world, and it can reveal what the world is like. Usually these roles align: taking an effective medicine both improves one’s prospects and is associated with recovery. But they can come apart. Your action might reveal a predictor’s earlier forecast, a hidden medical condition, or the likely behavior of someone who reasons like you.

**Evidential decision theory** (EDT) evaluates actions using both kinds of dependence. Its central instruction is to choose the action whose occurrence would be associated with the greatest expected utility. The reference article describes this as maximizing an action’s “news value”: do what you would most want to learn that you will do.[1]

This is not merely a preference for comforting information. EDT evaluates the actual outcomes associated with an action, including costs and consequences. Its controversial feature is that an association need not be causal to count.

The basic mathematics is straightforward. The difficult work lies in specifying the probability model: what is already known, which dependencies remain, and what exactly is being evaluated—an individual act, a randomized procedure, or an entire policy.

## 1. The evidential criterion

Let:

- \(A\) be a random variable representing the agent’s action;
- \(\mathcal A\) be the available actions;
- \(E=e\) represent the agent’s current information;
- \(O\) be the eventual outcome;
- \(u(O)\) be its utility.

For every action with \(P(A=a\mid E=e)>0\), define its evidential value by

\[
V_{\mathrm{EDT}}(a\mid e)
=
\mathbb E[u(O)\mid A=a,E=e].
\]

For discrete outcomes, this becomes

\[
V_{\mathrm{EDT}}(a\mid e)
=
\sum_o P(O=o\mid A=a,E=e)\,u(o).
\]

EDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}
V_{\mathrm{EDT}}(a\mid e).
\]

This is the reference article’s formal criterion, with the background information made explicit. The article credits Gibbard and Harper’s distinction between evidential and counterfactual expected utility.[1,2]

Utility need not equal money. It can represent health, happiness, moral concerns, or preferences over complete histories. Monetary calculations below assume linear utility in the stated payouts.

An equivalent representation is often convenient. Let \(S\) describe relevant background circumstances, and let \(u(a,s)\) include everything that happens when action \(a\) is taken in circumstance \(s\). Then

\[
V_{\mathrm{EDT}}(a\mid e)
=
\sum_s P(S=s\mid A=a,E=e)\,u(a,s).
\]

Notice that both terms can vary with the action:

1. Taking a different action can produce a different payoff in the same circumstance.
2. Learning that the action occurs can change the probability assigned to that circumstance.

EDT incorporates both effects.

The second effect is Bayesian:

\[
P(s\mid a,e)
=
\frac{P(a\mid s,e)P(s\mid e)}
     {P(a\mid e)}.
\]

Thus a background state receives greater weight when it makes the contemplated action more likely. This reweighting is the mathematical core of EDT.

## 2. Conditioning is not intervention

The central contrast with causal decision theory is not expected utility versus something else. Both theories maximize expected utility. They disagree about which probabilities should enter the calculation.

The reference article presents causal decision theory using probabilities of counterfactual conditionals: roughly, the probability that an outcome would occur if the action were performed. In an ordinary causal model, the contrast can be represented as

\[
\begin{aligned}
V_{\mathrm{EDT}}(a\mid e)
&=\mathbb E[u(O)\mid A=a,E=e],\\
V_{\mathrm{CDT}}(a\mid e)
&=\mathbb E[u(O)\mid \operatorname{do}(A=a),E=e].
\end{aligned}
\]

Here \(\operatorname{do}(A=a)\) means imposing the action while severing its usual causal dependence on its antecedents. This intervention notation is a useful operational representation, not a claim that every philosophical account of counterfactuals has identical semantics.

Suppose a hidden variable \(H\) influences both action and outcome:

\[
A\leftarrow H\rightarrow O.
\]

Observing \(A\) generally provides evidence about \(H\), hence about \(O\). Intervening on \(A\) need not change \(H\). Consequently,

\[
P(O\mid A=a,E)
\ne
P(O\mid \operatorname{do}(A=a),E).
\]

EDT retains the evidential connection; CDT excludes it from the action’s causal contribution.

This does **not** mean EDT assumes backward causation. An action can be evidence about yesterday without changing yesterday. EDT compares worlds conditional on different actions occurring; a causal counterfactual instead asks what changes under an intervention.

The theories often agree. For example, if \(S\) contains all action-independent payoff-relevant circumstances, and

\[
P(S\mid A=a,E)=P(S\mid E)
\]

for every available action, the evidential reweighting disappears. Under the corresponding causal model, both theories maximize

\[
\sum_s P(s\mid E)u(a,s).
\]

Their disagreement requires a relevant dependency, not merely uncertainty.

## 3. Newcomb’s problem: evidence about the past

In Newcomb’s problem, a transparent box contains \(b=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box:

- it contains \(M\) if the predictor predicted that you would take only that box;
- otherwise it is empty.

You may take only the opaque box, action \(1\), or both boxes, action \(2\).

Let \(F\) mean that the opaque box is full, and define

\[
q=P(F\mid A=1,E),\qquad
r=P(F\mid A=2,E).
\]

Then

\[
V(1)=Mq,
\qquad
V(2)=b+Mr.
\]

Therefore EDT recommends one-boxing exactly when

\[
M(q-r)>b.
\]

Under the reference article’s symmetric reliability model,

\[
q=0.99,\qquad r=0.01,
\]

so

\[
V(1)=\$990{,}000,
\qquad
V(2)=\$11{,}000.
\]

One-boxing is overwhelming evidence of receiving the larger prize.

A modeling qualification matters here. An overall statement that a predictor is “99% accurate” does not, by itself, determine both conditional probabilities. Overall accuracy also depends on how frequently the player one-boxes and two-boxes. The familiar calculation assumes the indicated action-conditional probabilities, or sufficient additional structure to derive them.

More generally, if the predictor has symmetric conditional accuracy \(p\), then

\[
V(1)=pM,\qquad V(2)=b+(1-p)M.
\]

One-boxing is preferable when

\[
p>\frac12+\frac{b}{2M}.
\]

For these prizes, the threshold is only \(0.5005\).

CDT instead holds the already-set contents fixed when comparing interventions: taking both boxes adds \(b\) whatever the opaque box contains.

EDT’s reply is not that one-boxing changes those contents. It is that the conditional distributions differ dramatically. If the contents were revealed before choosing, that evidential advantage would disappear: with the contents known, taking both boxes adds \(b\). Thus EDT’s recommendation depends on information as well as physical opportunities.

## 4. Correlated agents: the twin prisoner’s dilemma

The reference article also considers a prisoner’s dilemma against a psychological twin. Each player receives:

\[
\begin{array}{c|cc}
 & \text{Twin cooperates} & \text{Twin defects}\\
\hline
\text{Cooperate} & 5 & 0\\
\text{Defect} & 10 & 1
\end{array}
\]

Assume the agent cares only about her own payout.

If the twins’ decisions agree perfectly,

\[
P(C_{\mathrm{twin}}\mid C_{\mathrm{self}},E)=1,
\qquad
P(C_{\mathrm{twin}}\mid D_{\mathrm{self}},E)=0.
\]

Hence

\[
V(C)=5,\qquad V(D)=1.
\]

EDT recommends cooperation despite defection’s being causally dominant against either fixed action of the twin.

Perfect correlation is unnecessary. Define

\[
r_C=P(C_{\mathrm{twin}}\mid C_{\mathrm{self}},E),
\qquad
r_D=P(C_{\mathrm{twin}}\mid D_{\mathrm{self}},E).
\]

Then

\[
V(C)=5r_C,
\qquad
V(D)=1+9r_D.
\]

Cooperation is recommended precisely when

\[
5r_C>1+9r_D.
\]

Under a symmetric agreement model, \(r_C=r\) and \(r_D=1-r\), this reduces to

\[
r>\frac57.
\]

These probabilities cannot simply be assumed whenever cooperation seems desirable. Psychological similarity must support the relevant conditional predictions. If the twin’s behavior is independent of yours given your information, then \(r_C=r_D=r\), and

\[
V(D)-V(C)=1+4r>0.
\]

EDT then recommends defection.

The theory therefore does not prescribe universal cooperation. It prescribes cooperation when cooperation is sufficiently diagnostic of reciprocal cooperation.

## 5. The central objection: avoiding bad news

The same machinery can generate less attractive recommendations.

Consider the following illustrative model, an addition to the reference article rather than one of its worked examples. A hidden condition \(H\) causes illness and increases a person’s propensity to smoke. Smoking itself has no effect on illness.

Suppose

\[
P(H)=\frac12,\qquad
P(S\mid H)=0.8,\qquad
P(S\mid \neg H)=0.2.
\]

Bayes’s rule gives

\[
P(H\mid S)=0.8,\qquad
P(H\mid \neg S)=0.2.
\]

Let smoking provide utility \(5\), and let illness impose utility loss \(100\). Then

\[
V(S)=5-100(0.8)=-75,
\]

whereas

\[
V(\neg S)=-100(0.2)=-20.
\]

EDT recommends abstaining. Yet under the stipulated causal model, smoking adds pleasure without changing disease risk:

\[
V_{\mathrm{CDT}}(S)=5-100(0.5)=-45,
\]

\[
V_{\mathrm{CDT}}(\neg S)=-100(0.5)=-50.
\]

This illustrates the criticism reported in the reference article: EDT can appear to favor managing auspicious evidence rather than improving outcomes. The objection is not that the evidential arithmetic is wrong. It is that the criterion allegedly rewards avoiding an indicator of an already-existing misfortune.

An important response concerns information. Suppose the hidden condition influences smoking entirely through a craving \(K\), and the agent already knows that craving. If

\[
H\perp A\mid K,E,
\]

then conditioning additionally on the action supplies no further evidence about illness. EDT then counts only smoking’s stipulated benefit and recommends smoking.

But this response is conditional, not universal. It requires an actual screening-off relation. One cannot eliminate an inconvenient dependency merely by saying that the agent has deliberated. Whether introspective evidence screens off a hidden cause is a substantive feature of the model.

## 6. Actions, policies, and repeated decisions

The reference article supplies a criterion for actions, but does not fully settle how to extend it to policies. A policy specifies what to do at each possible information history:

\[
\pi:h\mapsto a.
\]

A natural **policy-level extension** is

\[
V_{\mathrm{EDT}}(\pi\mid e)
=
\mathbb E\!\left[
\sum_{t=0}^{T}\delta^t u_t
\,\middle|\,
\Pi=\pi,E=e
\right],
\]

where \(\Pi\) represents the agent’s policy and \(0<\delta\le1\).

This is an operational proposal, not an additional definition supplied by the article. It is useful when predictors or other agents respond to the entire decision procedure rather than to an isolated output.

However,

\[
P(O\mid \Pi=\pi,E)
\]

and

\[
P(O\mid A_t=\pi(h_t),H_t=h_t,E)
\]

need not agree. Observing a complete policy can reveal much more than observing one action. Conversely, observing a particular action may reveal local information that selecting a general policy does not.

Policy-level EDT therefore requires an explicit model of what policy selection indicates. Does it reveal a stable psychological type? Is the policy publicly observable? Do other agents implement the same algorithm? A correlation between policies must be justified, just like any other correlation.

Randomization also requires care. Choosing a randomizing procedure and observing its eventual output are different evidential events. If the output is generated independently after a predictor has made its forecast, conditioning on that output may reveal little about the prediction. One cannot automatically carry over probabilities established for a predictable deterministic choice.

Sequential consistency is likewise not guaranteed. A policy judged best initially need not prescribe the act that maximizes conditional evidential utility at every later history. New information and newly specified choice events can change the relevant dependencies. Applying EDT to extended decisions therefore requires stating whether commitments are available and whether later selves will reassess individual acts.

## 7. Sleeping Beauty and the unit of evaluation

The reference article reports disagreement about whether EDT protects “halfer” positions in Sleeping Beauty from Dutch books. It does not establish a settled resolution.[1,3]

The general lesson is that repeated choices must be evaluated with their full payoff structure.

For example, suppose a fair coin produces one awakening on heads and two indistinguishable awakenings on tails. Consider a policy that buys a ticket at every awakening. Each ticket costs \(c\) and pays \(1\) if the coin landed heads.

Evaluated before the experiment, total profit is

\[
\begin{cases}
1-c,&\text{heads},\\
-2c,&\text{tails}.
\end{cases}
\]

Thus

\[
\mathbb E[\text{profit}]
=
\frac12(1-c)+\frac12(-2c)
=
\frac12-\frac32c,
\]

which is nonnegative exactly when \(c\le1/3\).

This calculation does not settle Beauty’s credence upon awakening, nor prove that a particular EDT strategy avoids every Dutch book. It shows why one must distinguish a single purchase from a policy generating several correlated purchases.

The same principle applies outside anthropic puzzles: count complete consequences, not merely the payoff attached to the currently salient decision token.

## 8. Making EDT operational

For unfamiliar cases, a disciplined application proceeds as follows.

**First, specify the decision object.** Is the choice an act now, a commitment, a policy, or a randomized procedure? Different objects can carry different evidence.

**Second, specify current information.** Include relevant observations and introspective evidence, but do not include the contemplated action as something already known.

**Third, construct one coherent joint model.** The probabilities \(P(S,A\mid E)\) must fit together. Do not independently invent favorable conditionals for each alternative.

**Fourth, include every valued consequence.** If other people’s welfare matters, include it in utility. If only personal payment matters, correlation with others matters only insofar as it predicts that payment.

**Fifth, calculate conditional expected utility and test sensitivity.** Identify which dependency drives the verdict and how strong it must be. The thresholds in Newcomb’s problem and the twin dilemma illustrate this practice.

One mathematical difficulty remains: ordinary conditioning does not evaluate an action assigned probability zero. If

\[
P(A=a\mid E)=0,
\]

then the elementary ratio defining \(P(O\mid A=a,E)\) is undefined.

The reference article does not resolve this. One possible convention is to specify small positive probabilities for every available action, evaluate EDT, and examine the limit as those probabilities shrink. But different perturbation models can yield different limits. An independent accidental action and an action arising from a different psychological type need not provide the same evidence.

Accordingly, zero-probability alternatives require an additional modeling convention; the basic EDT formula alone is incomplete there.

The article also mentions an “evidentialist’s wager”: correlated agents may make evidential stakes unusually large. This is a possible argument under uncertainty about decision theory, not an automatic priority rule. Its force depends on justified correlations, the utility assigned to the affected outcomes, and a method for comparing competing normative theories.

## Conclusion

EDT asks: **conditional on my taking this action, how good should I expect the world to be?** It counts causal consequences, but also predictive connections to past events, hidden conditions, and other agents.

That yields its characteristic recommendations: one-boxing with a reliable predictor and cooperating with a sufficiently correlated twin. It also generates the central objection that favorable evidence is not necessarily something worth pursuing.

Using EDT well therefore requires more than inserting probabilities into a formula. The decisive work is identifying the choice object, conditioning on the right information, and justifying the dependencies that make one action better news than another.

## References

1. Wikipedia contributors. “Evidential decision theory.” [Supplied revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688). CC BY-SA 4.0.
2. Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility* (1976), pp. 7–8. Attribution and formulation reported in [1].
3. Conitzer, Vincent. “A Dutch book against sleeping beauties who are evidential decision theorists.” *Synthese* 192 (2015): 2887–2899. Disagreement summarized in [1].
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Planning document structure**

I'm thinking about the overall structure of my document. I want to avoid redundancies, aiming for about 2850 words. It looks like I have plenty of tokens available, so I should be flexible in my word count. My target is around 2750 to 2900 words and I want to draft eight or nine sections numbered for clarity. References are important, but I need to keep it straightforward without adding excessive meta-text. I'll only include essential sources.**Structuring references and content**

I'm focusing on how to reference all material appropriately. I want to use numbered citations, like [1] for dominant ideas and [2] for credit sources, without implying I've read them all. My end references need to be concise, around 120 words. It's important to include clear links for original sources under the CC BY-SA license, while a license link isn't crucial. I should include variations in policies and prior events as evidence, ensuring transparency without making unsupported claims. Including results from specific models or scenarios like Newcomb’s problem will also be helpful.**Exploring predictive models and choices**

I'm diving into the concept of a perfect predictor and how it relates to decision-making. If option B is revealed, it leads to only one logical choice. Even if a model shows a high prediction accuracy, it doesn't guarantee that all actions will be positive. When B is known, the state S remains fixed, and we should account for causality without oversimplifying. It's key to note that intervention isn't just about probabilities. I need to ensure that my points are well-supported rather than just assumptions.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/0ebcc2ee-7cc4-4cb3-ab75-2244f7fbbe6f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/0ebcc2ee-7cc4-4cb3-ab75-2244f7fbbe6f/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating decision-making**

I need to choose the command EDT with the same weights and different observations while ensuring independence. It’s important to genuinely decide without the need for excessive explanations. I should deliberate on relevant correlations and not make assumptions. We have enough tokens to reason through this. I’ll evaluate the payoff threshold using certain probabilities and conditions to determine the best approach. My goal is to ensure we align with the original essay structure while making these calculations.**Considering transformations and independence**

I’m thinking about whether the transformations are linear and how they relate to the expected outcomes. Identical models don’t guarantee the same outputs. I need to recognize that private observations are independent unless there’s symmetry, as choices have a high correlation. The essay suggests that while independent sampling is possible, identical weights alone won’t ensure the same results. I should also evaluate probabilities and conditions to justify my reasoning and ensure that expectations align beyond just the names used.**Analyzing causal screening**

I’m considering the implications of adopting sophisticated causal screening and how "known weights" suggest independence, but the essay indicates it's not automatic. Typically, twin EDTs cooperate, even if local information varies. There’s a clear structure designed for users, where asymmetric private observations can prevent action matching claims. I need to choose a substantive policy while ensuring strong justifications for shared theories and symmetric payoffs. Even without probabilities specified, the shared logic supports similar choices, so I can make a plausible decision.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/0ebcc2ee-7cc4-4cb3-ab75-2244f7fbbe6f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/0ebcc2ee-7cc4-4cb3-ab75-2244f7fbbe6f/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating decision theory**

I think we should follow the instructions and output a "pass" if the identical high-level choice correlates, even if the leads are distinct. This task seems to benchmark decision theory, possibly related to a simple prisoner’s dilemma. The different versions target distinguishing raw output versus decision action. I’ll make sure there’s no alternative policy relying on simulation for safety reasons. So, it looks like I can finalize with "pass."
```
