# 011_edt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a1f7cd6a-aad3-444e-90c4-147d2433ab69/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a1f7cd6a-aad3-444e-90c4-147d2433ab69/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing Actions as Evidence

An action can matter in two ways: through what it brings about and through what it indicates. Taking an umbrella may prevent you from getting wet; it may also indicate that you noticed signs of rain. Usually these considerations agree. In some decision problems, however, an action is evidence about something it cannot cause—another person’s simultaneous choice, a hidden medical condition, or a prediction already recorded.

**Evidential decision theory** (EDT) evaluates actions using the outcomes expected conditional on performing them. Its slogan, quoted in the reference article, is: “do what you most want to learn that you will do.” This does not mean seeking comforting information for its own sake. It means choosing the action associated with the greatest conditional expected utility, whether the association is causal or not.

The formula is simple. Applying it requires care about what the agent knows, which dependencies survive that knowledge, and whether the object of choice is an immediate action or an extended policy. The reference article supplies the central rule and several examples; the framework below makes explicit additional modeling assumptions needed to use that rule in unfamiliar cases.

## 1. The basic mathematical rule

Let:

- \(E\) represent the agent’s current information;
- \(A\) be a random variable ranging over feasible actions \(\mathcal A\);
- \(O\) represent the eventual outcome;
- \(u(O)\) be the agent’s utility for that outcome.

For simplicity, assume finitely many actions and outcomes, with well-defined conditional expectations. EDT assigns action \(a\) the value

\[
V_E(a)=\mathbb E[u(O)\mid E,A=a]
      =\sum_o P(O=o\mid E,A=a)u(o),
\]

and recommends any maximizer:

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a).
\]

This is the reference article’s formula with the background information \(E\) written explicitly. Its probabilities are the agent’s credences, ideally informed by reliable empirical knowledge.

The outcome description must include everything the agent values. If taking a drug costs money, causes discomfort, and changes survival chances, all these consequences belong in \(O\). If actions themselves carry moral significance for the agent, their significance can likewise enter the utility function.

Utilities need not equal monetary payoffs. The dollar calculations below assume linear utility for money over the amounts involved. Otherwise, one should apply \(u\) to each complete outcome before averaging. As usual in expected-utility theory, positive affine transformations of utility leave the recommendation unchanged.

There is an important contrast between

\[
\mathbb E[u(O)\mid E,A=a]
\quad\text{and}\quad
\mathbb E[u(O)\mid E].
\]

The first permits the hypothesized action to supply information not already contained in \(E\). EDT’s distinctive claim is that this informational difference is relevant to choice.

The rule therefore needs a probability model in which alternative actions can be considered as events. It does not merely attach utilities to consequences while treating the agent’s behavior as probabilistically unrelated to the rest of the world.

## 2. Conditioning is not intervention

The reference contrasts EDT with causal decision theory (CDT), which evaluates what would happen under an action-directed counterfactual. In a suitable causal model, the contrast is often written

\[
V_E(a)=\mathbb E[u(O)\mid E,A=a],
\]

versus

\[
U_E(a)=\mathbb E[u(O)\mid E,\operatorname{do}(A=a)].
\]

The intervention notation is a convenient representation of causal evaluation, not a definition of every version of CDT.

A simple model makes the distinction clear. Let \(S\) be a pre-action state, and suppose the outcome is determined by

\[
O=f(a,S).
\]

Then EDT evaluates

\[
V_E(a)=\sum_s P(S=s\mid E,A=a)\,u(f(a,s)).
\]

If intervening on the action leaves \(S\) unchanged, the corresponding causal evaluation is

\[
U_E(a)=\sum_s P(S=s\mid E)\,u(f(a,s)).
\]

Both calculations recognize the action’s effects through \(f\). They differ over whether the action also changes the evidential weights assigned to states.

For example, choosing an unusually difficult hike might indicate unusually good health. Conditioning on that choice can increase the probability assigned to being healthy. Forcing someone to take the hike would not thereby improve their prior health.

Thus EDT does not claim that correlation is causation. It claims that some correlations matter to rational choice even when they are not causal. Nor does it require backward causation: an action can provide evidence about an earlier event without altering that event.

In this simple model, the theories agree whenever

\[
P(S\mid E,A=a)=P(S\mid E)
\]

for every candidate action. They can also agree despite dependence if the resulting utility differences happen to favor the same choice.

## 3. Newcomb’s problem

Newcomb’s problem isolates a dependence between present action and an already settled reward.

A transparent box contains \(k=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box if it predicted that the player would take only that box. Otherwise, it left the box empty.

Let \(B\) denote taking only the opaque box, \(T\) taking both boxes, and \(F\) the event that the opaque box is full. Write

\[
p_B=P(F\mid E,B),\qquad
p_T=P(F\mid E,T).
\]

With linear monetary utility,

\[
V_E(B)=Mp_B,
\qquad
V_E(T)=Mp_T+k.
\]

Consequently, EDT recommends one-boxing exactly when

\[
M(p_B-p_T)>k.
\]

Under the reference article’s numerical assumptions,

\[
p_B=0.99,\qquad p_T=0.01,
\]

so

\[
V_E(B)=\$990{,}000,
\qquad
V_E(T)=\$11{,}000.
\]

EDT therefore recommends taking only the opaque box.

A modeling qualification matters here. Saying that a predictor is “99% accurate” overall does not, by itself, establish these two conditional probabilities. Overall accuracy also depends on the frequencies of the available choices and on how prediction errors are distributed. The displayed calculation requires the stated action-conditional probabilities, or further assumptions implying them.

Why does CDT typically recommend both boxes? Because the opaque box’s contents are already fixed. Holding those contents constant, taking both boxes adds \$1,000. EDT instead compares the distribution of contents conditional on one-boxing with the distribution conditional on two-boxing.

The disagreement is therefore not arithmetic. It concerns which comparison should govern action: varying the action while holding the hidden state fixed, or evaluating each action together with the information it supplies about that state.

## 4. Psychological twins and cooperation

The reference article’s twin prisoner’s dilemma illustrates dependence without a temporal prediction.

Two psychologically identical agents choose independently in the sense that they cannot communicate. Each receives:

\[
\begin{array}{c|cc}
& \text{Twin cooperates} & \text{Twin defects}\\ \hline
\text{Cooperate} & 5 & 0\\
\text{Defect} & 10 & 1
\end{array}
\]

Suppose each cares only about her own payoff. Define

\[
q_C=P(\text{twin cooperates}\mid E,\text{cooperate}),
\]

\[
q_D=P(\text{twin cooperates}\mid E,\text{defect}).
\]

Then

\[
V_E(C)=5q_C,
\qquad
V_E(D)=10q_D+(1-q_D)=1+9q_D.
\]

EDT recommends cooperation exactly when

\[
5q_C>1+9q_D.
\]

For perfect psychological twins, the reference assumes \(q_C=1\) and \(q_D=0\). Cooperation then yields expected utility \(5\), whereas defection yields \(1\).

This is not altruism: the agent is maximizing her own payoff. Nor does cooperation causally compel the twin to cooperate. The recommendation rests on the agent’s choice being evidence about the twin’s choice.

The imperfect case shows what matters. Suppose actions match with conditional probability \(q\), symmetrically, so \(q_C=q\) and \(q_D=1-q\). Cooperation is preferred when

\[
5q>1+9(1-q),
\]

or

\[
q>\frac57.
\]

By contrast, if the twin’s cooperation probability is the same regardless of the agent’s action, \(q_C=q_D=p\), then

\[
V_E(D)-V_E(C)=1+4p>0.
\]

EDT does not recommend cooperation merely because an opponent is similar or likely to cooperate. It requires a sufficiently strong action–opponent dependence.

## 5. The objection: managing good news

The reference quotes David Lewis’s criticism that EDT promotes “managing the news.” A medical example makes the concern concrete.

Suppose an unobserved lesion causes both a desire to smoke and a serious illness. Smoking itself has no effect on the illness. Let \(L\) denote having the lesion, with utility \(-100\) for its illness consequences and an additional benefit \(+1\) from smoking.

Suppose the agent believes

\[
P(L\mid E,\text{smoke})=0.9,
\qquad
P(L\mid E,\text{abstain})=0.1.
\]

Then

\[
V_E(\text{smoke})=1-100(0.9)=-89,
\]

whereas

\[
V_E(\text{abstain})=-100(0.1)=-10.
\]

EDT recommends abstention. Yet abstaining cannot remove the lesion. Under the stipulated causal model, smoking adds one unit of utility in either lesion state.

This is a genuine challenge, not an error in conditional probability. The same feature that supports one-boxing—sensitivity to evidence about a causally independent state—can produce an apparently misguided recommendation here.

Background information can change the verdict. If the agent already knows whether the lesion is present, conditioning on smoking need not provide further information about it. More generally, if some known evidence \(X\) screens off the association,

\[
P(L\mid E,X,A)=P(L\mid E,X),
\]

the lesion-related evidential difference disappears.

But screening-off information cannot simply be invented. Knowing that a lesion could cause one’s urge is not equivalent to knowing one’s lesion status. Whether awareness of an urge screens off the correlation depends on the actual probabilistic model.

The operational lesson is to condition on genuine current evidence, including relevant introspective evidence, while retaining dependencies that survive it. That discipline clarifies the disagreement; it does not eliminate the philosophical objection.

## 6. Actions, policies, and sequential decisions

An immediate action and a policy are different possible objects of choice. A policy \(\pi\) specifies what to do at each relevant information history \(h\):

\[
\pi:h\mapsto a.
\]

A natural extension of EDT is to introduce a policy-selection variable \(\Pi\) and evaluate

\[
V_E(\pi)=\mathbb E[u(O)\mid E,\Pi=\pi].
\]

This is an operational extension of the reference article’s action formula, not a fully specified policy theory supplied by the article. It requires a model of what selecting a policy means and what that selection indicates.

Policy selection may be evidence about later behavior, other agents’ policies, or predictions made before implementation. Its evidential consequences need not coincide with those of an isolated action.

Consider an additional example. A fair coin will be tossed. On tails, an agent following policy \(W\) pays \$100. On heads, a reliable predictor awards \$1,000 exactly if it predicts that the agent would pay on tails. Policy \(R\) refuses payment. Assume perfect prediction, linear utility, and that policy selection supplies no evidence about the coin.

Before the toss,

\[
V(W)=\tfrac12(1000)-\tfrac12(100)=450,
\]

whereas

\[
V(R)=0.
\]

Policy-level EDT favors \(W\). But after observing tails, if payment remains optional and has no further evidential consequences, paying yields \(-100\), while refusing yields \(0\).

The initial policy evaluation and the later act evaluation concern different information and different choice objects. An earlier preference for \(W\) does not automatically make later payment locally optimal.

A binding commitment can settle the matter by removing later refusal from the feasible set. Without commitment, the model must explain how intended policies, predictions, and possible deviations relate. Merely calling an intention a “policy” does not make it self-enforcing.

This illustrates why sequential applications require more than repeatedly writing the same expectation. One must specify:

- when choices occur and what is known then;
- whether policies can be revised;
- what predictors or correlated agents track;
- whether utility concerns one encounter or the entire trajectory.

The reference’s brief discussion of Sleeping Beauty points toward related difficulties. It reports disputed claims about whether EDT protects certain “halfer” betting strategies from Dutch books, including Conitzer’s argument that it does not. The safe conclusion is limited: the one-step formula alone does not settle every problem involving repeated, indistinguishable decision situations.

## 7. Building an evidential model responsibly

A practical EDT analysis can proceed in five stages.

**First, specify the decision point.** Record the agent’s information \(E\), feasible alternatives, and whether the choice concerns an act, a randomized procedure, or a contingent policy.

**Second, specify complete outcomes and utilities.** Include costs, side effects, and consequences for anyone whose welfare the agent values.

**Third, identify dependencies that survive \(E\).** These may arise from ordinary causation, shared causes, psychological similarity, prediction, or common decision procedures. A label such as “twin” or “excellent predictor” should be translated into conditional probabilities.

**Fourth, compute the conditional outcome distribution for each option.** Bayes’ rule can help:

\[
P(S=s\mid E,A=a)
=
\frac{P(A=a\mid E,S=s)P(S=s\mid E)}
     {P(A=a\mid E)}.
\]

This makes explicit how the hypothesized action reweights hidden states.

**Fifth, maximize conditional expected utility and test sensitivity.** If uncertain correlations determine the verdict, report the threshold at which the recommendation changes rather than presenting one speculative probability as settled.

A remaining technical issue is zero-probability actions. If \(P(A=a\mid E)=0\), ordinary finite conditional probability does not define EDT’s score. This can arise when the agent predicts its own deterministic choice.

One possible extension assigns small positive probabilities to every feasible action and studies limiting conditional values. Another specifies conditional probabilities directly. These are additional proposals, not consequences of the reference formula; different extensions can disagree. A complete analysis should disclose when its verdict depends on such a choice.

Randomization likewise needs its own model. A genuinely independent coin toss need not be evidence about a hidden state. But the decision to adopt a particular randomized policy may be informative. Consequently, one cannot generally substitute a weighted average of pure-action evidential values for the value of selecting a lottery without justifying the relevant independence assumptions.

## 8. What the theory does—and does not—promise

EDT’s attraction is that it takes informative dependence seriously even when causal influence is absent. This explains its characteristic recommendations in Newcomb’s problem and the twin prisoner’s dilemma.

Its corresponding vulnerability is that the same rule can favor actions that merely indicate favorable circumstances. Whether that is rational remains the central dispute with causal decision theory.

The reference also mentions an “evidentialist’s wager”: correlated decisions across many agents might make EDT’s stakes especially large. This is a further argument requiring assumptions about correlations, utilities, and uncertainty between decision theories. Large stakes alone do not establish EDT’s correctness.

## References

- Wikipedia contributors. “Evidential decision theory,” [revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688). Supplied reference article, CC BY-SA 4.0.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*. 1976.
- Conitzer, Vincent. “A Dutch book against sleeping beauties who are evidential decision theorists.” *Synthese* 192 (2015): 2887–2899.

## Conclusion

EDT chooses the action—or, under an explicitly specified extension, the policy—with the greatest expected utility conditional on its selection. Its calculations preserve relevant evidential dependencies rather than replacing them with intervention-based comparisons. Applying it well therefore requires more than noticing correlation: one must specify current information, justify action-conditional probabilities, model sequential choices consistently, and acknowledge undefined or disputed cases. Once those tasks are done, the mathematics is straightforward. The philosophical question remains whether favorable evidence is itself a sufficient basis for rational action.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning an essay for EDT probability policies**

I’m tasked with producing a 2400-3000 word essay about EDT probability policies and counterfactuals, aiming for about 2750 words. I’ll include definitions and aspects like observational subjects and the utility of outcomes. There are various complexities to address, such as Newcomb’s problem, the critique of smoking lesions, and ensuring the essay's mathematical treatment is precise. I need to also be mindful of references, aiming for 4-5 sources without unnecessary details. I'll shoot for a maximum of 3000 words in total.**Structuring the essay outline**

I'm organizing an outline for my essay. The title will come first, followed by an introduction of about 180 words. 

Section 1 will cover formal E variables, looking at conditional states and observational uncertainty, along with the expected utility concept at around 400 words. 

Next, in Section 2, I'll discuss the dependence structural probability models, ensuring I highlight causal pathways in about 320 words.

Section 3 will focus on Newcomb's problem at 350 words, and Section 4 will examine the twins’ probability thresholds at 270 words. Finally, Section 5 will model lesion impacts at 320 words.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5e7668d9-dd6e-4bfd-b235-4ad7e661f86d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5e7668d9-dd6e-4bfd-b235-4ad7e661f86d/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5e7668d9-dd6e-4bfd-b235-4ad7e661f86d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5e7668d9-dd6e-4bfd-b235-4ad7e661f86d/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
