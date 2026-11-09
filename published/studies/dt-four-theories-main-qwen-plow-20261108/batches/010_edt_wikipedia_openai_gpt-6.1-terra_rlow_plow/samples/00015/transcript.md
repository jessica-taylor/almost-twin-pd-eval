# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/95595963-bc6b-4c86-b64c-a568b98481f2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/95595963-bc6b-4c86-b64c-a568b98481f2/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential decision theory: choosing what would be good news

A decision can reveal something about the world as well as change it. A doctor’s decision to order a test may be evidence that the patient’s symptoms are serious; a person’s choice to carry an umbrella may be evidence that rain is likely. Evidential decision theory, or **EDT**, asks a decision-maker to take such evidential relationships seriously when evaluating actions.

Its guiding recommendation is to choose the action whose performance would be the best news, in expected-utility terms. This is not merely the advice to perform actions that *look* impressive. The “news” is information for the agent itself: if I learned that I had taken a particular action, what should I expect the world, including my eventual payoff, to be like?

This idea can agree with ordinary causal reasoning. Taking an umbrella is often good news partly because it keeps one dry. But action can also be evidence about facts it does not cause. If a reliable predictor has already filled a box on the basis of a prediction of my choice, then my choice may be evidence about what the predictor did. EDT counts that information in evaluating the choice, even though the choice cannot ordinarily change the past.

The distinction is philosophically contentious. Critics argue that rational action should be guided by what an action can *bring about*, not by favorable correlations. To see the disagreement clearly, we need both a formal rule and a careful account of the probabilities to which the rule is applied.

## 1. The evidential value of an act

Suppose an agent has a set of available actions \(\mathcal A\), and the possible outcomes \(O_1,O_2,\ldots\) form a mutually exclusive and exhaustive partition. Let \(u(O_j)\) be the agent’s utility for outcome \(O_j\), and let \(K\) represent the information available at the decision point.

For an action \(a\), its **evidential value** is

\[
V_K(a)
=
\sum_j P(O_j\mid A=a,K)\,u(O_j)
=
\mathbb E[u(O)\mid A=a,K].
\]

Here \(A\) is the random variable representing the action actually taken. EDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A} V_K(a).
\]

The reference article presents the same rule without writing \(K\) explicitly. Making the background information explicit is useful: an action can be evidence for different things depending on what the agent already knows.

Several details matter in application.

First, the outcomes must include everything the agent values: money, effort, health, effects on others, and so on. Using monetary amounts directly as utilities, as we will do in some examples, assumes that utility is linear in money over the relevant range.

Second, the probability is conditional on the **action actually occurring**, not simply on the agent imagining it. The question is: among possibilities compatible with current information in which I take \(a\), what outcomes should I expect?

Third, one must evaluate all actions against the same body of current information. Learning that an action was taken may change beliefs about hidden traits, other agents’ decisions, earlier predictions, and the effects of the action itself. But the analyst should not quietly give one alternative extra information unavailable for the other.

For continuous outcomes, the sum is replaced by an integral. Ties are permitted: the simple rule does not by itself specify how to choose among actions with equal evidential value.

## 2. Conditioning is not intervention

Causal decision theory, or CDT, uses a different kind of hypothetical assessment. In a suitable causal model, one might write its value as

\[
C_K(a)
=
\mathbb E[u(O)\mid \operatorname{do}(A=a),K].
\]

The \(\operatorname{do}\) notation represents an intervention that sets the action to \(a\), rather than an observation that the action equals \(a\). The reference article expresses CDT using counterfactual probabilities: the probability that an outcome would occur *if* the action were performed. The intervention notation is one useful way to make such counterfactuals precise, though it is not the only formulation of CDT.

The difference is familiar from statistics. If people take medicine because they are ill, then observing that someone took medicine may be evidence of illness. Setting medicine-taking by intervention need not make illness more likely. Schematically,

\[
P(\text{ill}\mid \text{medicine})
\neq
P(\text{ill}\mid \operatorname{do}(\text{medicine})).
\]

Likewise, if an earlier predictor and the agent’s choice are correlated, conditioning on the choice can change the probability assigned to the earlier prediction. An intervention on the later choice, in an ordinary forward-causal model, does not change that earlier event.

The two evaluations coincide in many straightforward cases. For example, suppose action is randomized independently of all relevant prior conditions, and its effects on outcomes are properly represented in the model. Then observing an action can carry no information about those prior conditions beyond the information supplied by the intervention. Conditional and causal expected utilities may agree.

EDT therefore does not reject causation. Causal effects are among the reasons an outcome may be likely conditional on an action. Its distinctive feature is that it also counts relevant *noncausal* dependencies.

## 3. Newcomb’s problem

Newcomb’s problem makes that feature vivid. A player can take an opaque box alone or take it together with a transparent box containing \$1,000. A predictor has already placed \$1 million in the opaque box if it predicted that the player would take that box alone, and nothing there if it predicted that the player would take both.

Let \(B\) denote taking the opaque box alone and \(T\) taking both. The reference article uses the following conditional probabilities:

\[
P(\text{opaque box full}\mid B)=0.99,
\qquad
P(\text{opaque box full}\mid T)=0.01.
\]

Assuming linear utility in dollars,

\[
\begin{aligned}
V(B)&=0.99(\$1{,}000{,}000)+0.01(\$0)
      =\$990{,}000,\\
V(T)&=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
      =\$11{,}000.
\end{aligned}
\]

EDT recommends taking only the opaque box. The choice is strong evidence that the predictor anticipated that choice and filled the box.

A causal assessment points the other way. The box was filled or left empty before the player chose. Holding its contents fixed, taking both boxes adds \$1,000. On the usual causal model, taking both is therefore better.

The numbers also show the limits of a verbal description such as “99% accurate predictor.” Overall accuracy,

\[
P(\text{prediction correct})=0.99,
\]

does not by itself imply both conditional probabilities used above. Accuracy might vary between one-boxers and two-boxers, and the frequency of each choice matters. To apply EDT numerically, one needs the relevant conditional probabilities, or a joint model from which they can be calculated.

More generally, write

\[
p_B=P(\text{full}\mid B),\qquad
p_T=P(\text{full}\mid T).
\]

EDT prefers \(B\) precisely when

\[
\$1{,}000{,}000(p_B-p_T)>\$1{,}000.
\]

Thus the verdict depends not on prediction in the abstract, but on how much more likely a full box is conditional on one choice than on the other.

There is no claim here that choosing one box sends a causal signal into the past. The evidential claim is instead that the choice and the prediction are statistically related—for example, because the predictor has information about the process that produces the choice.

## 4. Correlated decision-makers

The same logic applies when the correlated event is another person’s action rather than an earlier prediction. In the reference article’s twin prisoner’s dilemma, Aomame chooses whether to cooperate with or defect against a psychological twin. Their individual payoffs are:

| Aomame’s action | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$5 | \$0 |
| Defect | \$10 | \$1 |

Against a fixed choice by the twin, defection pays more. Nevertheless, if the twins reason in exactly analogous ways and face appropriately symmetric circumstances, Aomame’s cooperation may be excellent evidence that her twin cooperates too. Under the article’s idealized assumptions,

\[
P(\text{twin cooperates}\mid A=C)=1,\qquad
P(\text{twin cooperates}\mid A=D)=0.
\]

Consequently,

\[
V(C)=\$5,\qquad V(D)=\$1,
\]

and EDT recommends cooperation.

Perfect correlation is not essential. Let

\[
p=P(\text{twin cooperates}\mid A=C),\qquad
q=P(\text{twin cooperates}\mid A=D).
\]

Then

\[
V(C)=5p,\qquad V(D)=10q+1(1-q)=1+9q.
\]

Cooperation is recommended if \(5p>1+9q\). This inequality makes the substantive question explicit: how strongly does the agent’s choice discriminate between possibilities in which the twin cooperates and possibilities in which the twin defects?

Similarity alone does not guarantee the required correlation. The twins may have different information, use independent randomizers, or face different incentives. Nor need one twin’s decision cause the other’s. EDT’s recommendation follows from the stipulated conditional probabilities and utilities, not from a general rule that one should always cooperate with similar people.

## 5. Actions as evidence about hidden conditions

The most troubling cases for EDT often involve an action that is evidence of an undesirable pre-existing condition. Imagine a simplified “smoking lesion” case. A hidden genetic condition makes a person likely both to smoke and to develop a disease. Suppose, for the sake of the example, that smoking itself has no effect on disease and gives the person one unit of pleasure.

Let \(L\) be the condition and \(S\) the act of smoking. Assume

\[
P(L\mid S)=0.8,\qquad P(L\mid \neg S)=0.2,
\]

and that disease follows exactly when \(L\) is present. Assign utility \(-10\) to disease and \(+1\) to the pleasure of smoking. Then

\[
V(S)=1-10(0.8)=-7,\qquad
V(\neg S)=-10(0.2)=-2.
\]

On these stipulated probabilities, simple EDT recommends not smoking. Yet if the condition is already fixed and smoking does not affect it, refusing the cigarette cannot prevent the disease. CDT would favor smoking for its pleasure.

This example gives force to David Lewis’s criticism that EDT can amount to managing the news. Refusing a cigarette may be good news about one’s underlying condition, but the critic asks why one should sacrifice pleasure to obtain that news when the condition itself cannot be changed.

An evidentialist can reply that the decision must be assessed with all information the agent actually has. Suppose the agent knows whether they have the desire associated with the condition. Conditional on that knowledge, the additional correlation between smoking and the condition might disappear:

\[
P(L\mid S,K)=P(L\mid \neg S,K).
\]

If so, EDT recommends smoking for its pleasure. This response does not prove that every problematic case disappears. Whether the relevant correlations vanish depends on what the agent knows and on the actual probability model. If uncertainty about the hidden condition remains correlated with action even after conditioning on \(K\), the conflict can remain.

The lesson for applications is not to add or remove correlations to secure a preferred verdict. One must ask what information is genuinely available, what would be learned from each action, and whether the proposed joint probabilities are coherent.

## 6. Where do the probabilities come from?

The EDT formula is simple once the probabilities are supplied. Supplying them can be the difficult part. A useful operational approach is to build a joint probability model for the relevant variables:

- background conditions and the agent’s information;
- predictors, other agents, and their information;
- the agent’s eventual action;
- outcomes and utilities.

The model should represent whichever dependencies are credible in the case. Bayes’ rule can then calculate quantities such as \(P(O\mid A=a,K)\). For example,

\[
P(O\mid A=a,K)
=
\frac{P(A=a\mid O,K)P(O\mid K)}
     {P(A=a\mid K)},
\]

provided \(P(A=a\mid K)>0\). The equation shows why an act can be evidence: it may be more likely in some possible circumstances than in others.

This modelling proposal goes beyond the reference article’s basic formula. It also exposes an important open question: how should an agent assign probabilities to its own possible actions while deciding which to perform? The answer cannot simply assume that the action is independent of every hidden factor; that would erase the dependencies central to Newcomb’s problem. But it cannot simply stipulate whatever correlations make a favored action attractive either.

One practical strategy is to model uncertainty about features such as the agent’s reasoning, information, dispositions, or implementation errors, together with whatever a predictor or counterpart knows about them. The resulting probabilities should be calibrated to the situation as understood *before the action is settled*. This is an operational proposal, not a complete solution to the philosophical problem of self-prediction. In particular, discovering the result of one’s own deliberation may itself change the relevant information.

A related issue arises when \(P(A=a\mid K)=0\). Ordinary conditional probability then does not define \(V_K(a)\), even if \(a\) is an available alternative. The reference formula does not settle how to handle this. One possible extension is to consider a family of nearby models in which each available action has a small positive probability and take a limit. But different ways of introducing that small probability—for example, different kinds of error or randomization—can give different limits. Such a convention must therefore be justified by the case; it is not automatically supplied by EDT.

These difficulties distinguish two uses of the theory. If the joint distribution is stipulated, the calculation can be straightforward. In an unfamiliar real problem, defending the distribution and the decision point may require as much work as computing the expected utilities.

## 7. Policies and later decisions

Sometimes the object of choice is not an isolated act but a **policy**: a rule specifying what the agent will do under different future observations. If \(\pi\) ranges over available policies, a natural evidential analogue of the act rule is

\[
V_K(\pi)=\mathbb E[u(O)\mid \Pi=\pi,K],
\]

where \(\Pi\) is the policy actually adopted or implemented. This is an extension of the reference article’s action formula, useful when predictors or other agents respond to a whole decision rule.

The distinction matters. A predictor might predict the policy an agent will follow before the agent receives a private signal. In a repeated or sequential problem, choosing a policy now may also influence what others expect and therefore what they do later. To evaluate a policy, one should include its consequences in every information state in which it may be used, weighted by their conditional probabilities.

Policy choice and later act choice need not agree automatically. At a later time, after new information arrives, an agent applying the act formula afresh may prefer to depart from the earlier policy. Whether it can commit, whether a predictor anticipated that commitment, and what information is available at each stage all affect the analysis. One should not assume that “evaluate a policy now” and “re-optimize each act later” are interchangeable descriptions.

Nor does merely *considering* a policy establish that it will be adopted. As with acts, the relevant conditional distribution concerns the policy’s actual adoption or implementation, and zero-probability alternatives present the same formal difficulty.

## 8. Other implications and open debates

The reference article notes an application of EDT to the Sleeping Beauty problem, where an agent is awakened under conditions involving memory loss and uncertainty about which awakening she occupies. Some have argued that EDT helps an agent with a one-half credence for heads avoid certain Dutch books; Conitzer argues that such agents can still be Dutch-booked. The significance is broader than that single puzzle: sequential betting, repeated awakenings, and policy choice can interact with how an agent represents its evidence. The article reports a dispute, not a settled theorem that EDT resolves the problem.

It also mentions the “evidentialist’s wager”: even someone uncertain whether EDT is the correct decision theory might give it substantial practical weight if correlations with many other decision-makers make the stakes of its recommendations large. That is an argument about decision-making under uncertainty *between theories*, not a proof of EDT’s basic conditional-value rule. Its force depends on how competing theories are weighted and on whether their evaluations can be compared.

These debates illustrate a recurring theme. EDT can attach high importance to dependencies that causal analysis treats as fixed background correlations. That may capture real regularities in a world of predictors and similar agents. It may also, critics argue, recommend sacrificing causal benefits for favorable evidence about facts one cannot affect.

## Conclusion

EDT evaluates an action by the expected utility conditional on taking it. To apply it, identify the available acts or policies, specify outcomes and utilities, condition on the agent’s actual information, and calculate how each alternative changes the probability of every relevant outcome—including outcomes connected to the choice by prediction or common causes rather than by the choice’s causal effects.

The rule yields clear recommendations when the conditional probabilities are well specified. Its hardest questions concern how those probabilities should be modelled for an agent’s own alternatives, especially when an alternative has probability zero or when decisions occur over time. The central philosophical question remains whether good evidence about outcomes is itself a sufficient guide to action, or whether rational choice must instead track what the action can causally change.

### References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688, CC BY-SA 4.0.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, “Counterfactuals and Two Kinds of Expected Utility,” 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.
- Vincent Conitzer, “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists,” *Synthese*, 2015.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing target accuracy**

I need to produce substantial output close to my target, but I should include a disclaimer about accuracy given the conditions. There are zero probabilities involved, and I need to consider policy selection carefully. It seems like I should address the common prior circularity issues as well as the impact of things like smoking lesions and their dynamics. There's a lot to unpack, so I'll need to think this through thoroughly.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/d0e05efb-f155-43c5-bc1e-10d2c89e5202/call_0/request.json)

[Authoritative raw response](../../../../../../runs/d0e05efb-f155-43c5-bc1e-10d2c89e5202/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Choosing correlation criteria**

I need to select the right correlation approach. There's this idea of using an identical model with symmetric irrelevant specifics while considering a strong correlation in reasoning that often includes uncertainty in common decisions. However, independent sampling can yield different outcomes even with the same rational analysis. A strong similarity suggests there might be a likely cooperation factor in the decision-making process. It's a bit complex, but I'm thinking it through!
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/d0e05efb-f155-43c5-bc1e-10d2c89e5202/call_1/request.json)

[Authoritative raw response](../../../../../../runs/d0e05efb-f155-43c5-bc1e-10d2c89e5202/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Choosing correlations wisely**

I need to make sure I'm selecting correlations that are strong and common while keeping in mind abstract symmetry, even with private observations that vary. The identical model and decision theory can create symmetry, but I should avoid irrelevant factors. Ultimately, I want to focus on what leads to a likely strong correlation of choices. This process feels a bit tricky, but it's essential to clarify my thinking and ensure I'm on the right track!
```
