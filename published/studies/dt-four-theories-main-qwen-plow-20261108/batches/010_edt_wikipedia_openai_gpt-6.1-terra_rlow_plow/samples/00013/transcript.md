# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00013

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/58302aae-809f-472f-a9ae-f2b48a1570cc/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/58302aae-809f-472f-a9ae-f2b48a1570cc/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential decision theory: choosing what would be good news

Suppose you are deciding whether to carry an umbrella. Your choice can cause you to stay dry, but it can also reveal something about the weather: people are more likely to carry umbrellas when they have seen signs of rain. These are different kinds of connection. An umbrella does not make rain more likely merely because carrying one is associated with rain.

Evidential decision theory, or **EDT**, evaluates an action by asking how desirable the world would be *conditional on performing it*. Its guiding thought is that an agent should do what she would most like to learn that she will do. Often this agrees with the familiar advice to choose the action that causes the best outcome. When an action is evidence about facts it does not cause, however, the recommendations can diverge.

That divergence is the theory’s distinctive feature and the source of its controversy. An EDT calculation can treat a present choice as evidence about a prediction made yesterday or about the simultaneous choice of a distant, similar agent. Critics reply that this confuses making good things happen with managing signs of good fortune. Understanding EDT requires seeing both why the evidential calculation is attractive and what assumptions it needs.

## The basic rule

Let \(K\) represent everything the agent knows at the decision point, and let \(A\) be an available action. Suppose the possible outcomes \(O_1,O_2,\ldots\) form a mutually exclusive and exhaustive partition, and \(u(O_j)\) is the agent’s utility for outcome \(O_j\). EDT assigns the action the value

\[
V_{\mathrm E}(A\mid K)
=\sum_j P(O_j\mid A,K)\,u(O_j).
\]

The recommended actions are those maximizing this quantity. Equivalently, writing \(U\) for the utility of the eventual outcome,

\[
A^*\in\operatorname*{arg\,max}_A
\mathbb E[U\mid A,K].
\]

The conditioning event \(A\) means that the action is **actually performed**, not merely that it is available or contemplated. The probability distribution is the agent’s distribution given her present information. If money is used as a stand-in for utility, as in the examples below, we are assuming that the agent values the relevant amounts linearly.

The outcome description must include everything the agent cares about. For example, if an action itself is painful or violates a promise, those features must be represented in utility, even if they do not affect a monetary payoff. Nor should the outcome partition omit relevant uncertainty: an action can have consequences through ordinary physical effects, through other people’s responses, and through whatever its occurrence indicates about hidden circumstances.

This rule does not say that thinking about an action provides the same evidence as taking it. An agent may consider both \(A\) and \(B\), while only the eventual performance of one of them is evidence of the relevant kind.

## Conditioning and causal counterfactuals

For an event of positive probability, ordinary conditioning is

\[
P(O\mid A,K)=\frac{P(O\cap A\mid K)}{P(A\mid K)}.
\]

It asks what proportion of the cases compatible with \(K\) and \(A\) have outcome \(O\). It does not, by itself, say what would happen if an outside force changed the action while holding fixed the factors that produced it.

Causal decision theory, or **CDT**, instead evaluates outcomes under causal counterfactuals. In the notation used in the reference article, its comparison can be written schematically as

\[
V_{\mathrm C}(A\mid K)
=\sum_j P(A\mathbin{\Box\!\rightarrow}O_j\mid K)\,u(O_j),
\]

where \(A\mathbin{\Box\!\rightarrow}O_j\) says that \(O_j\) would occur if \(A\) were performed. Different versions of CDT interpret these counterfactuals somewhat differently. In a suitable causal model, a related expression is

\[
\mathbb E[U\mid \operatorname{do}(A),K],
\]

where \(\operatorname{do}(A)\) represents an intervention setting the action rather than observing it as the product of its usual causes.

The distinction is not that EDT ignores causation. Causal effects usually contribute to \(P(O\mid A,K)\): if taking an umbrella keeps you dry, that affects the conditional distribution of dryness. EDT differs in allowing *other* dependencies to contribute too.

Consider a hidden variable \(H\) that influences both an action and an outcome:

\[
H\longrightarrow A,\qquad H\longrightarrow O.
\]

Observing \(A\) can change beliefs about \(H\), and thereby about \(O\), even if changing \(A\) would not change \(H\). By contrast, if the action is randomized independently of all relevant prior factors, and its downstream effects are represented correctly, conditioning on it will often agree with intervening on it. Randomization can remove precisely the evidential association that makes EDT and CDT disagree.

## Newcomb’s problem: evidence about a past prediction

The reference article’s central example involves two boxes. A transparent box contains $1,000. An opaque box contains either $1 million or nothing. Before the choice, a highly reliable predictor has put $1 million in the opaque box if it predicted that the agent would take only that box; otherwise it left the box empty. The agent can take the opaque box alone or take both.

Suppose the agent’s conditional probabilities are

\[
P(\text{opaque box full}\mid \text{one-box})=0.99
\]

and

\[
P(\text{opaque box full}\mid \text{two-box})=0.01.
\]

Then, using dollars as utility,

\[
\begin{aligned}
V_{\mathrm E}(\text{one-box})
&=0.99(1{,}000{,}000)+0.01(0)
=\$990{,}000,\\
V_{\mathrm E}(\text{two-box})
&=0.01(1{,}001{,}000)+0.99(1{,}000)
=\$11{,}000.
\end{aligned}
\]

EDT therefore recommends taking only the opaque box.

The causal objection is immediate. The predictor has already filled or not filled the opaque box. Whatever is in it, taking the transparent box as well adds $1,000. On the stipulated causal structure, CDT recommends taking both.

EDT does **not** need to claim that the present choice sends a signal backward in time. Rather, the predictor’s earlier judgment and the later choice are correlated—for example, because both depend on features of the agent’s reasoning. Learning that the agent one-boxes is strong evidence that the predictor predicted one-boxing, even though it is not evidence that the later choice physically caused the earlier prediction.

The numbers also show that one-boxing is not an unconditional EDT command. More generally, let

\[
p=P(\text{full}\mid \text{one-box}),\qquad
q=P(\text{full}\mid \text{two-box}).
\]

Then one-boxing is favored exactly when

\[
1{,}000{,}000(p-q)>1{,}000.
\]

The evidential difference must exceed the extra $1,000 obtainable by taking both boxes. Moreover, a claim that a predictor is “99% accurate” *overall* does not alone establish the two displayed conditional probabilities: the frequencies of the two choices and the distribution of prediction errors matter. The calculation requires the more specific conditional assumptions.

## Correlated agents: the twin prisoner’s dilemma

Now consider Aomame and a psychological twin in separate rooms. Each independently chooses to cooperate or defect. Aomame’s payoffs are:

| Aomame | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | $5 | $0 |
| Defect | $10 | $1 |

For either fixed choice by the twin, Aomame earns more by defecting. But suppose the agents’ reasoning is so closely matched that Aomame is certain that her twin makes the same choice she does. Then

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]
\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]

Consequently,

\[
V_{\mathrm E}(C)=\$5,\qquad V_{\mathrm E}(D)=\$1.
\]

EDT recommends cooperation even when Aomame cares only about her own payoff. Cooperation is good news about the twin’s choice.

Perfect matching is not essential. Put

\[
c=P(\text{twin cooperates}\mid C),\qquad
d=P(\text{twin cooperates}\mid D).
\]

Then

\[
V_{\mathrm E}(C)=5c,\qquad
V_{\mathrm E}(D)=10d+1(1-d)=1+9d.
\]

Cooperation is favored when \(5c>1+9d\). This makes the scope of the argument clear: EDT does not automatically recommend cooperation with anyone called a “twin.” It needs a sufficiently strong conditional connection between the choices. If the twin cooperates with the same probability regardless of Aomame’s action, defection has the higher evidential value.

## A criticism: buying good news

The same reasoning can produce a troubling recommendation. Imagine that a hidden medical condition makes people both more likely to crave a certain harmless confection and more likely to develop an illness. Assume eating the confection has no effect on the illness or its treatment, and gives a small pleasure worth \(0.1\) utility units. Illness costs 10 units.

Suppose, given the agent’s current information,

\[
P(\text{ill}\mid \text{eat})=0.8,\qquad
P(\text{ill}\mid \text{abstain})=0.2.
\]

The evidential values are

\[
V_{\mathrm E}(\text{eat})=0.1-10(0.8)=-7.9,
\]
\[
V_{\mathrm E}(\text{abstain})=-10(0.2)=-2.
\]

EDT recommends abstaining. Yet abstention does not cure or prevent the condition; it merely accompanies a lower incidence of it. If the causal assumptions are correct, CDT recommends taking the small pleasure.

This illustrates David Lewis’s complaint, quoted in the reference, that EDT can amount to an irrational policy of “managing the news.” James Joyce similarly emphasizes causal efficacy rather than auspiciousness. An evidentialist response is that the agent is choosing among actual action-events, and the probability of a bad outcome conditional on eating really is higher. The disagreement concerns whether that fact is a reason to choose when the association runs through a common cause.

The information \(K\) matters greatly here. If the agent knows whether she has the condition, and that knowledge screens off the association between action and illness, the conditional illness probabilities may become equal. Then EDT favors the pleasurable act. But an appeal to “screening off” is not a general solution: if the relevant condition is unknown, it cannot simply be inserted into \(K\) as if it were known. Conversely, an apparent evidential dependence should not be retained after the agent has actually learned information that removes it.

## Constructing the probabilities

The formula is simple; applying it demands a model. A useful procedure is:

1. **Specify the decision point and information \(K\).** Include observations already available, but not facts merely hypothesized for the analysis.
2. **List the available acts and outcomes.** Include indirect effects, action costs, and features relevant to utility.
3. **Build a joint probability model.** Represent the dependencies among actions, hidden states, predictions, other agents’ choices, and outcomes.
4. **Condition on each act.** Calculate \(P(O_j\mid A,K)\) for the same decision situation.
5. **Multiply by utility and compare.** Test whether the ranking changes under plausible alternative probabilities or utility assignments.

The third step is essential. One cannot infer that an action is good evidence merely because the outcome would be pleasant, or because an action would be chosen by an ideal agent. Nor should one assign each conditional probability independently without checking that the resulting claims belong to a coherent joint distribution.

There is a further difficulty: an agent applying EDT may be close to certain what she will choose *because* she has performed the calculation. If she assigns an alternative action probability zero, the ordinary ratio formula for conditioning on it is undefined. A deterministic model can therefore leave the value of an unchosen act unspecified.

The reference gives the conditional-value rule but does not settle this issue. One operational proposal is to model small uncertainties about the agent’s deliberation, implementation, or private evidence, so that each feasible act has positive probability, and then condition in that richer model. This must be done carefully: adding independent physical randomization can change the evidential relationships, rather than merely revealing the intended value of an unrealized choice. One can also specify conditional probabilities directly using a richer conditional-probability framework. Neither method is unique; different ways of approaching a zero-probability action can yield different answers. An honest application should identify that dependence rather than present the result as forced by the basic formula.

## Acts, policies, and sequential decisions

Sometimes the object of choice is not a single act but a **policy**: a rule \(\pi\) specifying what to do at each information state. A natural extension of EDT is

\[
V_{\mathrm E}(\pi\mid K)
=\mathbb E[U\mid \Pi=\pi,K],
\]

where \(\Pi=\pi\) is the event that the agent adopts or follows that policy. This is an extension, not a separate rule established in detail by the reference article. Like the act rule, it uses a conditional distribution, and it requires a model in which alternative policies have meaningful conditional values.

Policy choice matters when a predictor forecasts a whole decision rule, when other agents are correlated with that rule, or when earlier commitments affect later choices. But one must distinguish **conditioning on having a policy** from **causally imposing a policy**. If agents with policy \(\pi\) tend to have a certain hidden trait, observing \(\Pi=\pi\) updates beliefs about that trait. Intervening to install \(\pi\) need not do so. An evidential policy calculation and a causal commitment calculation can therefore differ just as their one-act counterparts do.

Sequential settings add another complication. A policy preferred at an earlier time need not remain preferred at every later information state. New evidence changes the relevant conditional probabilities; moreover, the event of following an entire policy can carry different information from the event of taking one local action. If an agent can commit, the consequences and costs of commitment belong in the initial model. If she cannot, a policy that requires her later self to make a choice she would then reject may not be feasible.

Thus “apply EDT to policies” is not a license to assume that the best-looking plan will be implemented. It requires specifying the choice architecture, what the agent will know later, and whether later decisions are themselves evaluated evidentially. The source’s basic formula leaves these modeling choices open.

## Self-location and decision-theoretic uncertainty

The reference notes applications of EDT to the Sleeping Beauty problem, where an agent is awakened under conditions that make her uncertain both about a coin flip and about which awakening she is experiencing. The problem raises questions not only about probabilities but also about how repeated opportunities to accept bets affect total payoffs. Some have argued that EDT helps a Beauty who assigns heads probability \(1/2\) avoid certain Dutch-book arguments; Conitzer argues that such halfers can still be vulnerable. The reference does not resolve the dispute.

The lesson is methodological: in self-locating problems, specify whether utilities are counted per awakening, per experiment, or by some other rule, and describe the whole betting protocol before computing conditional values. A decision rule alone does not determine the sample space or settle every disputed credence.

Finally, the reference mentions the **evidentialist’s wager**: even someone uncertain whether EDT is correct might give its recommendations considerable weight because choices may be correlated across many decision-makers. That is a further argument under moral or decision-theoretic uncertainty, not a consequence of the EDT formula itself. Its force depends on how such uncertainty is aggregated, on the strength of the correlations, and on the relative stakes assigned by competing theories.

## Conclusion

EDT evaluates an action by the expected utility of the outcome **given that the action occurs**. This makes ordinary consequences relevant, but also lets choices serve as evidence about predictions, hidden states, and correlated agents. It explains why EDT one-boxes in the stipulated Newcomb problem and cooperates with a sufficiently similar twin—and why critics worry that it can recommend sacrificing benefits merely to secure better news.

To apply the theory well, the crucial work is not just maximizing a formula. It is specifying the agent’s information, a coherent joint model, the utilities, and the action or policy being conditioned on. Where an alternative has zero probability or a sequential commitment is unclear, the basic rule needs an explicit additional interpretation.

### References

- Wikipedia contributors, [“Evidential decision theory,” revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), CC BY-SA 4.0.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.
- Vincent Conitzer, “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists,” *Synthese*, 2015.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Clarifying writing focus**

I need to create a substantial piece, targeting around 2400 words. My focus should be on zero probability and ensuring correlation accuracy. I want to explore policy conditions versus interventions, particularly relating to smoking lesions and their numerical data. Consistency in self-evidence seems crucial as well. Let’s keep the writing structured and clear, attending to these specific areas to achieve a comprehensive and informative output.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/789f57d1-0160-4490-abcf-6ee3907a3393/call_0/request.json)

[Authoritative raw response](../../../../../../runs/789f57d1-0160-4490-abcf-6ee3907a3393/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Deciding on correlation methods**

I’m trying to select a correlation method, considering that symmetry and strength are important. It seems like I should focus on specifics that are private and not get distracted by irrelevant details. My goal is to choose a method that will work well for the task at hand. I’ll ensure that I thoroughly assess my options and choose wisely for an effective analysis. It’s all about making the right choice!
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/789f57d1-0160-4490-abcf-6ee3907a3393/call_1/request.json)

[Authoritative raw response](../../../../../../runs/789f57d1-0160-4490-abcf-6ee3907a3393/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Selecting reasoning models**

I need to choose a reasoning model. The correlation between models can be strong, but they should be based on independent samples conditioned on the known model. I'm considering how uncertainty affects the reasoning output, especially since the correlation depends on shared uncertainty about propensity. Symmetry plays a role in achieving strong correlations via a common unknown algorithm, while private differences might be irrelevant. Ultimately, I want to select something reasonable.
```
