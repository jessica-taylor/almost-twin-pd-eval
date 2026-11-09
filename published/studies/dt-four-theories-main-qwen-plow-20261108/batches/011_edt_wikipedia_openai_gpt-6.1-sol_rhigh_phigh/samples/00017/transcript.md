# 011_edt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00017

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/eeb289a1-ed0d-40bd-ac86-8fa3d449be98/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/eeb289a1-ed0d-40bd-ac86-8fa3d449be98/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing by What Your Action Indicates

Suppose you must choose an action whose consequences depend partly on facts you cannot observe. Your choice may itself provide evidence about those facts. Should that evidence influence what you do?

**Evidential decision theory** (EDT) says yes. It evaluates an action by the expected desirability of the world conditional on your performing it. The reference article expresses the motivation as choosing what you would most like to learn that you will do.[1] That is not necessarily the action that would produce the best consequences if imposed independently of its usual causes.

This distinction matters when actions are informative: a predictor anticipates your decision, another agent reasons similarly to you, or an unobserved trait influences both your behavior and your prospects. To apply EDT correctly, we therefore need more than a payoff table. We need a probability model explaining what each available action would indicate.

## 1. The mathematical rule

Let \(A\) be a random variable representing the agent’s action, with possible values in a finite set \(\mathcal A\). Let \(E\) represent the agent’s current information, and let \(O_1,\ldots,O_n\) be mutually exclusive, exhaustive outcomes. Assign each outcome a utility \(u(O_j)\).

EDT evaluates action \(a\) by

\[
V_E(a)
=
\mathbb E[u(O)\mid A=a,E]
=
\sum_j P(O_j\mid A=a,E)\,u(O_j).
\]

It recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a).
\]

This is the reference article’s central definition, with current information \(E\) made explicit. The article attributes the distinction between evidential and counterfactual expected utilities to Gibbard and Harper.[2]

An “outcome” should contain everything that matters to the agent. It may include money, health, other people’s welfare, the action performed, and later consequences. Utilities remain fixed across comparisons: EDT changes the probabilities assigned to outcomes, not the standards by which those outcomes are valued.

Often it is convenient to represent uncertainty using a state variable \(S\), with utility \(u(a,s)\). Then

\[
V_E(a)=\sum_s P(S=s\mid A=a,E)\,u(a,s).
\]

For example, \(S\) might describe whether an opaque box contains money, while \(a\) describes which boxes are taken.

Two details are essential.

First, the probabilities concern the agent’s uncertainty **before learning which action occurs**. They are not probabilities calculated after deliberately discarding relevant information.

Second, ordinary conditional probabilities require

\[
P(A=a\mid E)>0.
\]

How to evaluate alternatives assigned probability zero is a substantive modeling problem, not something the displayed formula automatically solves. We will return to it.

For the numerical examples below, utility is linear in money. This simplifies calculation, but EDT itself does not require risk neutrality.

## 2. Evidence is not intervention

The philosophical contrast with causal decision theory becomes clearest when we distinguish two questions:

1. What should I expect **conditional on my performing \(a\)**?
2. What should I expect **if \(a\) were imposed**, without retaining its usual evidential implications?

EDT answers the first. Causal decision theory answers a version of the second.

The reference article writes causal expected utility using probabilities of counterfactual conditionals,

\[
P(a\mathrel{\Box\!\rightarrow}O_j).
\]

In an appropriate causal model, a common implementation instead uses intervention probabilities:

\[
V_C(a)
=
\sum_j P(O_j\mid \operatorname{do}(A=a),E)\,u(O_j).
\]

The intervention notation is an explanatory supplement here; the article does not develop a causal-model formalism.

Conditioning and intervention can differ because actions have causes. Suppose an unobserved characteristic \(T\) influences both your action \(A\) and some payoff-relevant fact \(S\):

\[
T\longrightarrow A,
\qquad
T\longrightarrow S.
\]

Learning \(A=a\) can change your beliefs about \(T\), and therefore about \(S\). Intervening to impose \(A=a\) need not do so.

Bayes’ rule displays the evidential reweighting:

\[
P(s\mid A=a,E)
=
\frac{P(A=a\mid s,E)P(s\mid E)}
     {P(A=a\mid E)}.
\]

States in which the action is more likely receive greater conditional weight.

This does not mean EDT believes that choosing an action changes the past. It means that different actions can indicate different past circumstances. Nor does EDT ignore causal consequences: those consequences are already included in the conditional distribution of outcomes.

A useful agreement condition follows. If \(S\) consists of facts unaffected by the action, and

\[
P(S\mid A=a,E)=P(S\mid E)
\]

for every available \(a\), then evidential evaluation reduces to ordinary expected utility over the same state distribution. Under the corresponding causal assumptions, EDT and CDT agree.

The dispute concerns which dependencies should influence choice when this independence fails.

## 3. Newcomb’s problem: an action as evidence about a prediction

In Newcomb’s problem, a transparent box contains \(b=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box:

- if it predicted that you would take only the opaque box, it placed \(M\) inside;
- if it predicted that you would take both boxes, it left the opaque box empty.

Let \(B\) denote taking only the opaque box, and \(T\) taking both. Write

\[
p_B=P(\text{opaque box full}\mid A=B,E),
\]

\[
p_T=P(\text{opaque box full}\mid A=T,E).
\]

Then

\[
V_E(B)=p_BM,
\qquad
V_E(T)=b+p_TM.
\]

Consequently, EDT recommends one-boxing exactly when

\[
M(p_B-p_T)>b.
\]

The reference article uses

\[
p_B=0.99,\qquad p_T=0.01,
\]

giving

\[
V_E(B)=\$990{,}000,
\qquad
V_E(T)=\$11{,}000.
\]

EDT therefore takes only the opaque box.

There is a small but important statistical qualification. Saying merely that a predictor is “99% accurate” overall does not uniquely determine these two conditional probabilities. The article’s calculation uses a particular symmetric reliability model. In an unfamiliar case, one must obtain the relevant conditional probabilities rather than substitute an aggregate accuracy statistic without justification.

The causal argument for taking both boxes holds their contents fixed: whichever contents are present, taking both yields an additional \(\$1{,}000\). EDT instead compares two different conditional distributions over those already-fixed contents.

Thus the disagreement is not about whether the money is physically settled. Both theories can accept that it is. They disagree about whether the information conveyed by the action belongs in its evaluation.

If the contents are revealed before choosing, and both actions remain possible under the probability model, the evidential advantage disappears. Given the known contents, taking both yields the extra \(\$1{,}000\). The relevant probabilities must always be conditional on the information actually available.

## 4. Psychological twins and correlated cooperation

The reference article also considers a prisoner’s dilemma between psychological twins. Each chooses cooperation, \(C\), or defection, \(D\). The agent’s monetary payoffs are

\[
\begin{array}{c|cc}
&\text{Twin: }C&\text{Twin: }D\\ \hline
C&5&0\\
D&10&1
\end{array}
\]

Defection produces a higher payoff for either fixed action of the twin. Nevertheless, suppose the twins’ reasoning is so closely matched that

\[
P(\text{twin chooses }C\mid A=C,E)=1,
\]

\[
P(\text{twin chooses }C\mid A=D,E)=0.
\]

EDT then calculates

\[
V_E(C)=5,\qquad V_E(D)=1,
\]

and recommends cooperation.

The operative assumption is not merely that the players resemble one another. It is the specified conditional dependence between their choices. Different information, preferences, or private randomness could weaken that dependence.

To see how much correlation is required, define

\[
p=P(\text{twin chooses }C\mid A=C,E),
\]

\[
r=P(\text{twin chooses }C\mid A=D,E).
\]

Then

\[
V_E(C)=5p,
\qquad
V_E(D)=10r+(1-r)=1+9r.
\]

Cooperation is recommended precisely when

\[
5p>1+9r.
\]

EDT therefore does not prescribe cooperation against every opponent. Against an opponent whose action is independent of yours, \(p=r\), and defection wins.

Nor does the cooperative conclusion require altruism. In the article’s example, each player values only her own payout. The evidential connection between actions changes which personal payoff she should expect.

## 5. The objection: why not simply manage the news?

The same mechanism produces EDT’s most controversial recommendations. The article reports criticisms by David Lewis and James Joyce: favorable evidence is not necessarily effective action, and rational choice should arguably aim at bringing about good outcomes rather than indicating them.[1]

Here is an additional illustrative model, not an example developed in the reference article.

An unobserved trait \(L\) both increases the propensity to press a button and predicts an unavoidable loss of \(100\) utility units. Pressing the button provides a benefit of \(5\), but has no effect on \(L\) or the loss. Suppose

\[
P(L\mid \text{press},E)=0.8,
\qquad
P(L\mid \text{abstain},E)=0.2.
\]

Then

\[
V_E(\text{press})=5-0.8(100)=-75,
\]

\[
V_E(\text{abstain})=-0.2(100)=-20.
\]

EDT recommends abstaining. A causal evaluation recommends pressing: the loss is unaffected, and the button supplies a benefit.

The causal theorist sees abstention as pointless avoidance of bad news. The evidentialist replies that, under the stipulated model, abstention is associated with substantially better prospects.

Neither observation by itself resolves the disagreement. It exposes the central normative question: should choice maximize expected welfare conditional on the chosen act, or expected welfare under a suitably isolated intervention?

We should also scrutinize the model. If the agent has already observed information that screens off the connection between action and trait, the displayed probabilities are inappropriate. But if the dependence genuinely survives all current evidence, EDT’s recommendation follows directly. Removing it solely because it is noncausal would replace EDT’s rule rather than clarify it.

## 6. Building an evidential model responsibly

The expected-utility calculation is usually easier than constructing the conditional probabilities. The following procedure is an operational interpretation of EDT, rather than a further prescription supplied by the article.

**Identify the actual decision.** Specify the available acts, their timing, and what the agent can control. Choosing a treatment, choosing a lottery over treatments, and adopting a long-term treatment policy are different decisions.

**Include current evidence.** Condition on observations, known preferences, relevant internal information, and the known setup. Do not substitute population-level correlations for correlations that remain valid for this informed agent.

**Model why actions correlate with outcomes.** The connection might arise from direct causation, a common cause, prediction, shared reasoning, or a combination. EDT can use all these connections, but unsupported correlations should not be invented.

**Check the utilities.** A monetary payoff is not automatically its utility. Likewise, other people’s outcomes count only to the extent represented in the agent’s utility function.

**Inspect unsupported alternatives.** If an action has zero conditional probability, ordinary conditioning does not supply its value.

One possible response to the last problem is to use a justified family of full-support models \(P_\varepsilon\), evaluate

\[
V_\varepsilon(a)
=
\mathbb E_{P_\varepsilon}[u(O)\mid A=a,E],
\]

and examine the limit as \(\varepsilon\to0\). But the model must explain what rare departures from the expected action indicate. Different assumptions about those departures can produce different limiting recommendations. “Add a tiny probability” is therefore not a uniquely defined solution.

There is a deeper difficulty when an agent knows its own decision procedure. Its choice probabilities and its deliberation cannot always be specified independently. EDT supplies a ranking given an appropriate probabilistic model; the basic formula alone does not provide a complete theory of self-prediction or deliberative uncertainty.

These limitations matter especially in idealized cases involving perfectly predictable or identical agents.

## 7. Actions, randomization, and policies

The article primarily presents EDT as a theory of individual actions. Extending it to policies requires specifying what event is being conditioned on.

A policy is a rule mapping information histories to actions:

\[
\pi:\mathcal H\to\mathcal A.
\]

It may also be stochastic, assigning a probability distribution over actions at each history. If \(\Pi\) represents the selected policy and \(H\) the resulting complete history, a natural evidential extension is

\[
W_E(\pi)
=
\mathbb E[u(H)\mid \Pi=\pi,E].
\]

This is a proposed operational extension, not a uniquely established interpretation in the supplied article.

Its attraction is straightforward: when the present choice really is an implementable commitment, evaluate the whole commitment and all its consequences. Conditioning on policy selection may also reveal information about a predictor or other correlated policy-makers.

But this is not generally equivalent to evaluating the policy’s realized action. An action may arise under several policies, each carrying different evidence. Accordingly,

\[
\mathbb E[u(H)\mid \Pi=\pi,E]
\]

need not equal an expectation conditional only on what happens at one decision node.

Randomization makes the distinction vivid. If an action is selected solely by a private random device independent of a hidden state, then—given the randomization policy—the realized action supplies no evidence about that state. Yet the earlier choice to adopt that policy might itself be informative. Predictors might also observe the policy, the random outcome, both, or neither. These are different models.

For sequential problems, three questions should remain separate:

- Which complete policy looks best before observations arrive?
- Which action looks best after a particular history?
- Can the agent commit to the earlier policy?

Their answers need not coincide. One should not silently treat an uncommitted agent as able to bind its future choices, nor assume that conditioning on an earlier commitment is equivalent to conditioning on each later act separately.

A reasonable working convention is to evaluate individual acts at ordinary choice points and complete policies when policy commitment is genuinely available. This clarifies the decision object without claiming to solve every problem of dynamic consistency.

## 8. What EDT alone does not settle

The article briefly discusses Sleeping Beauty and Dutch-book arguments, reporting disagreement about whether EDT protects “halfers” from guaranteed-loss betting arrangements.[1,4] It does not establish a general resolution. Repeated awakenings require a model of the agent’s information, repeated decisions, and total payoff. The one-shot conditional-expectation formula cannot replace that specification.

The article also reports an argument that EDT may deserve practical priority under uncertainty about decision theory because correlations with many other decision-makers can magnify its stakes. This is a further argument, not part of EDT’s definition. Its force depends on the actual correlations, whose welfare enters utility, and how rival theories’ recommendations are compared.

More generally, EDT does not license assuming that distant people will match one’s choices simply because doing so would produce a striking recommendation. Correlations are inputs to be justified, not rewards for adopting the theory.

## Conclusion

EDT’s central instruction is precise:

\[
\boxed{\text{Choose an action maximizing }
\mathbb E[u(O)\mid A=a,E].}
\]

Its distinctive feature is retaining the information carried by an action, even when that information concerns circumstances the action cannot causally change. This explains both its appeal in Newcomb’s problem and correlated cooperation, and its vulnerability to the charge of managing favorable news.

Applying EDT well therefore means identifying the decision object, conditioning on all current evidence, justifying the remaining dependencies, and confronting zero-probability and sequential-choice ambiguities explicitly. The calculation is simple; deciding what an action genuinely indicates is the substantive work.

### References

1. Wikipedia contributors. “Evidential decision theory,” supplied [revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688). Primary source for this essay; CC BY-SA 4.0.
2. Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility* (1976), pp. 7–8. Cited in [1].
3. Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021. Cited in [1].
4. Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192 (2015): 2887–2899. Cited in [1].
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Calculating word count**

I’m working on a plan that includes sections: an introduction of 200 words, a formal section of 350 words, a casual part of 300 words, and several others, totaling to different word counts like 300 for Newcomb, 200 for twins, and so on. Adding everything up gives me 2650 words. Ideally, I need to aim for around 2800 words. I’m keeping track of the count in my head!
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4f19eb79-63a0-4f8c-a95c-3144c1d65f9a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4f19eb79-63a0-4f8c-a95c-3144c1d65f9a/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4f19eb79-63a0-4f8c-a95c-3144c1d65f9a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4f19eb79-63a0-4f8c-a95c-3144c1d65f9a/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
