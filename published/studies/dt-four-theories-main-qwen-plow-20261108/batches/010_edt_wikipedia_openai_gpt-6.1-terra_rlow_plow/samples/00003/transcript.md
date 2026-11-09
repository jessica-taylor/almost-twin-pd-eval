# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00003

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5fa1b992-b949-4999-b704-0fefd34dea00/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5fa1b992-b949-4999-b704-0fefd34dea00/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Acting on Good News

Suppose your choice is informative about something you cannot control. You are considering whether to cooperate with a person whose reasoning closely resembles yours, for example, or whether to take a box filled by someone who predicted your decision yesterday. The choice may not *cause* the other person’s decision or alter yesterday’s prediction. Nevertheless, learning what you choose might tell you a great deal about both.

Evidential decision theory (EDT) treats that information as relevant to choice. Its basic recommendation is to choose the action associated with the best expected outcome, conditional on taking it. In Arif Ahmed’s formulation, one should “do what you most want to learn that you will do.”

This principle can produce familiar recommendations: buy the cheaper of two otherwise identical products, or take an effective medicine when its benefits exceed its costs. Its distinctive implications appear when an action is evidence about events it does not causally influence. Whether that is a strength or a flaw is the central philosophical dispute surrounding EDT.

## The basic calculation

Let \(K\) represent everything the decision-maker currently knows, \(A\) a candidate action, and \(O_1,\ldots,O_n\) mutually exclusive and exhaustive outcomes. Let \(u(O_j)\) be the utility of outcome \(O_j\). The evidential value of \(A\) is

\[
V_K(A)=\sum_{j=1}^n P(O_j\mid K,A)\,u(O_j).
\]

EDT recommends an action in

\[
\operatorname*{arg\,max}_{A} V_K(A).
\]

Equivalently, when utility is a random variable \(U\),

\[
V_K(A)=\mathbb E[U\mid K,A].
\]

The conditioning event \(A\) means that the agent **actually takes** the action. It is not merely the hypothesis that the agent is offered it or imagines taking it. Likewise, the outcomes must include all consequences relevant to utility: the action’s cost, benefits, side effects, effects on others if those matter to the agent, and any relevant uncertainty.

For example, if a ticket costs $5 and pays $20 with probability \(0.4\), with no other payoff, its expected monetary value is

\[
0.4(15)+0.6(-5)=3.
\]

If buying the ticket carries no further evidence about the world, EDT compares this $3 with the value of not buying. The calculation becomes more interesting when buying is correlated with an unknown condition—for instance, when buyers tend to have private information about the odds. Then the relevant probability is not automatically the advertised average probability but \(P(\text{win}\mid K,\text{buy})\), if that conditional probability is part of the decision-maker’s justified model.

The reference article contrasts this calculation with causal decision theory (CDT). In a simple causal model, CDT can be represented as evaluating

\[
V^{\mathrm{causal}}_K(A)
=\mathbb E[U\mid K,\operatorname{do}(A)],
\]

where \(\operatorname{do}(A)\) represents an intervention setting the action while holding fixed the appropriate causal background. More generally, CDT is expressed using probabilities of causal counterfactuals: what outcomes would occur *if the agent were to take* \(A\). The intervention notation is a useful illustration, not a complete account of every version of CDT.

The two quantities need not agree:

\[
P(O\mid K,A)\ne P(O\mid K,\operatorname{do}(A)).
\]

Conditioning asks what is probable **on learning that the action occurs**. Intervention asks what would result **from setting the action**. When action is correlated with a predictor, a hidden condition, or another agent, learning the action can change beliefs about those things even when intervening on the action would not change them.

## Why the distinction matters

Imagine a hidden variable \(H\) that influences both your action and some independent outcome. A simple dependency structure is

\[
H\longrightarrow A,\qquad H\longrightarrow O.
\]

Observing \(A\) provides evidence about \(H\), which in turn provides evidence about \(O\). But in this diagram, changing \(A\) does not change \(H\), and there is no arrow from \(A\) to \(O\). Thus conditioning on \(A\) can change the probability of \(O\), while intervening on \(A\) does not.

EDT does not claim that correlation creates a physical causal influence. Its claim is normative: among actions available to you, prefer the one on which the prospects are best conditional on its being taken. CDT instead gives special decision-making significance to the outcomes that the choice would causally bring about.

The evidential calculation is not a prediction made by a detached observer who knows nothing about the agent. It uses the agent’s current information \(K\). If \(K\) already settles the hidden condition, then the action cannot provide additional evidence about that condition. This point matters both in defense of EDT and in criticisms of it.

## Newcomb’s problem

The reference article’s principal example is Newcomb’s problem. A transparent box contains $1,000. An opaque box contains either $1 million or nothing. A highly reliable predictor has already filled the opaque box: it contains $1 million if the predictor predicted that you would take only that box, and nothing if it predicted that you would take both.

You choose between:

- **One-boxing:** take only the opaque box.
- **Two-boxing:** take both boxes.

Suppose the relevant conditional probabilities are

\[
P(\text{opaque box full}\mid K,\text{one-box})=0.99,
\]
\[
P(\text{opaque box full}\mid K,\text{two-box})=0.01.
\]

Assuming utility is proportional to money over these amounts, EDT calculates

\[
V_K(\text{one-box})=0.99(\$1{,}000{,}000)=\$990{,}000,
\]

and

\[
V_K(\text{two-box})
=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
=\$11{,}000.
\]

It therefore recommends one-boxing.

The reasoning is evidential, not retrocausal. One-boxing is strong evidence that the predictor anticipated one-boxing and filled the box. It does not follow that the present choice physically changes the earlier prediction.

A causal decision theorist instead reasons that the opaque box is already either full or empty. In either case, taking the transparent box adds $1,000. On the usual causal description, two-boxing therefore causally dominates one-boxing.

One technical qualification is important. The statement “the predictor is 99% accurate” does not by itself imply both conditional probabilities above. Overall accuracy can be 99% while accuracy differs between one-boxers and two-boxers. The numerical EDT verdict uses the stronger, action-conditional probabilities stated in the calculation.

More generally, if

\[
p_1=P(\text{full}\mid K,\text{one-box}),\qquad
p_2=P(\text{full}\mid K,\text{two-box}),
\]

then one-boxing is favored, under linear monetary utility, exactly when

\[
\$1{,}000{,}000(p_1-p_2)>\$1{,}000.
\]

The predictor need not be perfect: the evidential advantage must simply outweigh the transparent box’s value.

## Correlated decision-makers

The same principle applies when the relevant dependency concerns another person’s choice rather than a prediction of yours.

In the reference article’s twin prisoner’s dilemma, Aomame and her psychological twin choose separately whether to cooperate or defect. Aomame’s payoffs are:

| Aomame | Twin | Aomame’s payoff |
|---|---|---:|
| Cooperate | Cooperate | $5 |
| Cooperate | Defect | $0 |
| Defect | Cooperate | $10 |
| Defect | Defect | $1 |

If the twins’ choices are perfectly correlated, then

\[
P(\text{twin cooperates}\mid K,\text{Aomame cooperates})=1
\]

and

\[
P(\text{twin cooperates}\mid K,\text{Aomame defects})=0.
\]

EDT assigns cooperation a value of $5 and defection a value of $1, so it recommends cooperation. It does so even if Aomame cares only about her own payoff and has no causal influence over her twin.

Perfect correlation is not essential, but the degree of correlation matters. Write

\[
c=P(\text{twin cooperates}\mid K,\text{Aomame cooperates}),
\]
\[
d=P(\text{twin cooperates}\mid K,\text{Aomame defects}).
\]

Then

\[
V_K(C)=5c,\qquad
V_K(D)=10d+1(1-d)=1+9d.
\]

EDT cooperates when

\[
5c>1+9d.
\]

Merely knowing that the other player is similar does not establish this inequality. An application requires justified probabilities about how similarity translates into correlated choices. Nor does EDT prescribe cooperation in every ordinary prisoner’s dilemma: if the other player’s choice is evidentially independent of yours, defection has the higher payoff against either choice.

## The objection: managing the news

EDT’s sensitivity to correlation is also its most prominent target. David Lewis criticized it as an irrational policy of “managing the news”: choosing an action because it signals a favorable state rather than because it helps bring that state about.

Consider a simplified medical case. A hidden lesion makes a person both prone to smoke and likely to develop a disease. Suppose, for the sake of the example, that smoking itself does **not** cause the disease and that the agent enjoys smoking. A possible probability model is

\[
P(\text{disease}\mid K,\text{smoke})=0.8,\qquad
P(\text{disease}\mid K,\text{abstain})=0.2.
\]

Let avoiding disease be worth 100 utility units and the enjoyment of smoking be worth 1. Then

\[
V_K(\text{smoke})=0.2(100)+1=21,
\]
\[
V_K(\text{abstain})=0.8(100)=80.
\]

EDT recommends abstaining. Yet, by stipulation, abstinence does not remove the lesion or prevent disease; it merely signals that the lesion is less likely. A critic asks why someone should sacrifice an enjoyable activity to obtain a favorable indication about an already existing condition.

The example’s stipulations are artificial. They are not medical advice, and actual smoking is causally harmful. Their purpose is to isolate the philosophical issue.

An evidentialist can reply that the recommendation follows only if the stated conditional probabilities remain correct given *all* of the agent’s current information. Perhaps the agent already knows their craving, genetic test result, or other relevant signs. If that information screens off the correlation, then

\[
P(\text{disease}\mid K,\text{smoke})
=
P(\text{disease}\mid K,\text{abstain}),
\]

and EDT recommends smoking in this artificial case because it supplies enjoyment without changing the disease risk. But this response does not settle every case: the agent may lack information that fully screens off the correlation. The disagreement is sharpest when the evidence remains genuinely relevant after conditioning on \(K\).

## Applying EDT to unfamiliar cases

The formal rule is compact, but applying it requires a model. A useful procedure is:

1. **Specify the decision and information.** Identify the available actions and the information \(K\) the agent has at the time of choice.
2. **Specify utility-bearing outcomes.** Include action costs, downstream consequences, and any aspects of others’ welfare that matter to the agent.
3. **Model the dependencies.** Ask what each action would be evidence about: hidden states, predictions, other agents’ choices, and ordinary causal effects.
4. **Estimate action-conditional probabilities.** Calculate or estimate \(P(O_j\mid K,A)\), rather than substituting either unconditional frequencies or intervention probabilities without justification.
5. **Compute and compare values.** Sum conditional utilities and examine how the recommendation changes under plausible alternative probability or utility assumptions.

Bayes’ rule can help expose where the evidential effect comes from. For a hidden state \(H\),

\[
P(H\mid K,A)
=
\frac{P(A\mid K,H)P(H\mid K)}{P(A\mid K)},
\]

provided \(P(A\mid K)>0\). If \(H\) makes the action more likely, observing the action raises the posterior probability of \(H\). The outcome probabilities can then be obtained by averaging over hidden states:

\[
P(O\mid K,A)
=
\sum_h P(O\mid K,A,h)P(h\mid K,A).
\]

This decomposition keeps two roles distinct. The factor \(P(O\mid K,A,h)\) can capture genuine effects of the action, while \(P(h\mid K,A)\) captures what the action signals about the background. EDT includes both.

The modeling can be difficult because the agent is deliberating about the very action whose probability appears in the model. The theory’s formula does not, on its own, explain how an agent should construct a joint probability distribution over its choice, predictors, and outcomes. It also does not make a predictor reliable merely because the scenario calls it one. Those are substantive modeling assumptions.

## Policies, randomization, and counterfactual choices

A decision can concern a single act or a policy: a rule specifying what to do in several possible circumstances. If the candidate policies are \(\pi\), the direct evidential analogue is

\[
V_K(\pi)=\mathbb E[U\mid K,\text{the agent adopts }\pi].
\]

The event conditioned on must be clear. Adopting a policy is different from executing one of its recommendations, and a predictor might be informative about either. A policy that says “cooperate when condition \(X\) holds” can be adopted even when \(X\) never occurs. Conversely, observing cooperation need not reveal which policy was adopted.

The reference article gives the action-level formula but does not resolve all questions about policy choice or sequential consistency. A reasonable operational proposal is to evaluate a genuine policy-selection decision using the agent’s current joint model, including how adoption of that policy is correlated with predictions and other agents. If the agent later faces an unanticipated choice, they can apply EDT again using their updated information. There is no general guarantee, however, that the later recommendation will coincide with the earlier policy’s prescription. Whether commitment is available and desirable must be modeled rather than assumed.

Randomization also needs explicit treatment. “Flip a coin and follow it” is itself a possible action or policy. If the coin is genuinely independent of the predictor’s information, conditioning on the coin’s result need not provide the same evidence as conditioning on an ordinary deliberative choice. But a predictor might anticipate the agent’s decision to randomize, know something about the coin, or reward policies rather than final acts. One cannot assume either that randomization breaks every dependency or that it breaks none.

A final technical problem arises when \(P(A\mid K)=0\). Ordinary conditioning on \(A\) is then undefined, even if the agent regards \(A\) as an available alternative. This can happen in a model that assigns probability one to a particular decision. The reference formula does not specify a universal solution. One possible modeling proposal is to use small-probability perturbations: give each alternative positive probability, compute its conditional value, and study the limit. But different perturbations can yield different limits, so this requires justification rather than serving as an automatic answer. Another possibility is to supply conditional probabilities as primitives of a richer model. Either way, zero-probability alternatives expose a gap between the compact formula and a fully specified decision procedure.

## Evidence, uncertainty, and the scope of the theory

EDT’s result depends on the probability distribution and utility function supplied to it. If a prediction is less reliable than expected, an apparent Newcomb-style reason to one-box may disappear. If a decision-maker is risk-averse over money, expected dollars should be replaced by expected utility. If an action supplies no evidence about another agent after all current information is considered, the correlation-based reason for cooperation disappears.

The same dependence on modeling appears in more elaborate problems. The reference article notes applications of EDT to the Sleeping Beauty problem, in which an agent has uncertain self-locating information across repeated awakenings. It also reports a dispute about whether EDT protects an agent with particular credences from Dutch-book arguments. That issue cannot be decided by the EDT formula alone: the betting protocol, what is known at each awakening, how many bets are made, and the probability assigned to each decision situation all matter.

The article also mentions an argument for acting as though EDT were true under moral or decision-theoretic uncertainty: correlated decision-makers may make the stakes of an evidential choice especially large. This is not itself the basic EDT rule, and the conclusion is not automatic. Comparing theories under uncertainty requires additional assumptions about their normative weights and about how to compare their evaluations.

## Conclusion

EDT evaluates an action by the expected desirability of outcomes conditional on that action being taken. This makes it attentive both to causal consequences and to information conveyed by a choice about predictors, hidden conditions, and similar agents.

Its appeal is clearest when an action is a reliable sign of a favorable outcome, as in the stipulated Newcomb and twin cases. Its challenge is clearest when a favorable sign seems unable to improve an already settled condition. Applying EDT responsibly therefore requires more than recognizing a correlation: one must specify the decision, condition on the agent’s actual information, model the relevant dependencies, and be explicit about uncertain assumptions.

## References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688, CC BY-SA 4.0.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, 1981.
- Conitzer, Vincent. “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Focusing on targets**

I'm trying to deliver something substantial that aligns closely with my goals. It seems important to address the accuracy of certain conditions, especially when it comes to distinguishing between zero and other factors. I need to consider policy aspects related to smoking lesion numbers and possibly incorporate elements of randomization and self-reference. I wonder how each of these components will fit into the overall strategy. There's definitely a lot to think about here!
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/da6601cf-59a4-4071-9808-9a538e2a2b66/call_0/request.json)

[Authoritative raw response](../../../../../../runs/da6601cf-59a4-4071-9808-9a538e2a2b66/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating correlation methods**

I need to choose between uncertain independent sampling or strong correlation methods. I'll think about symmetry in the reasoning and common deliberation. Even though it's not purely numerical, there's still some judgment involved. It looks like cooperation plays a key role in using the same algorithm and could lead to a high likelihood of success. So, it seems like I could go ahead and validate this approach.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/da6601cf-59a4-4071-9808-9a538e2a2b66/call_1/request.json)

[Authoritative raw response](../../../../../../runs/da6601cf-59a4-4071-9808-9a538e2a2b66/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
