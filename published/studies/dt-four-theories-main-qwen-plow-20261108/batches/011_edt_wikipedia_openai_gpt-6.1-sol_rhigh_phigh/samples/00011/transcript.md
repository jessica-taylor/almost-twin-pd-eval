# 011_edt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00011

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c1ffa2d3-9a87-44df-833a-a0ec35ed965e/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c1ffa2d3-9a87-44df-833a-a0ec35ed965e/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing the Action That Is Good News

A decision can matter in two different ways. It can change what happens, and it can reveal what sort of situation one is already in. Usually these considerations agree: taking an effective medicine both improves one’s prospects and indicates that recovery is more likely. But they can come apart when actions correlate with hidden conditions, predictions, or other people’s decisions.

**Evidential decision theory** (EDT) evaluates an action by the expected desirability of the world conditional on taking it. The supplied reference article summarizes its recommendation as choosing the action with the highest “news value”: do what you would most like to learn that you will do.

This is not simply advice to seek reassuring information. EDT concerns the utility of actual outcomes, not necessarily the pleasure of believing that things are going well. Its controversial claim is that an action’s evidential relationship to those outcomes is the right relationship for practical deliberation—even when it is not causal.

Understanding that claim requires distinguishing three things: the utility function, the probabilistic model, and the rule for comparing actions.

## 1. The basic mathematical rule

Let:

- \(\mathcal A\) be a finite set of available actions;
- \(E\) represent the agent’s current information;
- \(O_1,\ldots,O_n\) be mutually exclusive, exhaustive outcomes;
- \(u(O_j)\) be the utility of outcome \(O_j\);
- \(P\) be the agent’s probability distribution.

Write \(A\) for the random variable representing which action the agent takes. EDT assigns action \(a\) the value

\[
V_E(a)
=
\mathbb E[u(O)\mid E,A=a]
=
\sum_j P(O_j\mid E,A=a)u(O_j).
\]

It recommends any action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a).
\]

The reference article gives this conditional-expectation formulation and attributes the distinction between evidential and counterfactual expected utility to Gibbard and Harper.

Three qualifications matter.

First, utility need not equal money. It may represent health, happiness, moral concerns, or any combination of consequences. Numerical examples below use dollars as utility only for simplicity.

Second, outcomes must be described richly enough to capture everything the agent values. If taking an action is itself pleasant, costly, dishonest, or obligatory, that feature belongs in the outcome or utility function.

Third, every action is evaluated against the **same current information** \(E\). EDT does not license forgetting inconvenient facts when evaluating one option. Nor does it permit choosing whichever conditional probabilities make a favored action look attractive: the probabilities should belong to one coherent model.

For positive-probability actions, the conditioning is ordinary Bayesian conditioning:

\[
P(O_j\mid E,A=a)
=
\frac{P(O_j,A=a\mid E)}{P(A=a\mid E)}.
\]

The distinctive feature is not a new probability calculus. It is the decision to use these conditional probabilities for choosing actions.

## 2. Evidence is not intervention

Suppose \(S\) describes relevant background conditions and \(u(a,s)\) gives the utility of taking \(a\) in condition \(s\). EDT then evaluates

\[
V_E(a)=\sum_s P(s\mid E,A=a)u(a,s).
\]

The distribution over background conditions can differ between candidate actions. Learning that I take one action may suggest that I am in a different situation from the one suggested by another action.

By contrast, in a simple causal model where \(S\) is unaffected by the choice, causal decision theory evaluates

\[
V_C(a)=\sum_s P(s\mid E)u(a,s).
\]

Here the agent holds the background distribution fixed and varies the action’s effects. More generally, causal models can express this distinction using intervention probabilities:

\[
P(O\mid E,\operatorname{do}(A=a)),
\]

rather than observational probabilities \(P(O\mid E,A=a)\).

The reference instead presents CDT through probabilities of counterfactual conditionals, \(P(A\mathrel{\Box\!\rightarrow}O)\). These are different formal approaches to representing causal evaluation; the central contrast is that ordinary conditioning need not agree with a causal counterfactual.

EDT therefore does not primarily ask:

> What would happen if I changed my action while leaving its causes unchanged?

It asks:

> Conditional on my taking this action, what should I expect?

This can change beliefs about the past without implying that the action changes the past. Learning that a thermometer reads \(30^\circ\) changes one’s belief about the temperature; forcing its display to read \(30^\circ\) generally does not. EDT treats an action as potential evidence in the first sense, not merely as an intervention in the second.

When action supplies no information about background conditions, the two evaluations coincide. Thus EDT and CDT agree across many ordinary decisions.

## 3. Newcomb’s problem: an action as evidence about a prediction

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either \(\$1{,}000{,}000\) or nothing.

A predictor has already filled the opaque box:

- if it predicted that the agent would take only the opaque box, it put in the million;
- if it predicted that the agent would take both boxes, it left the opaque box empty.

Let \(B\) mean taking only the opaque box, \(T\) taking both, and \(F\) that the opaque box is full. Assume

\[
P(F\mid E,B)=0.99,\qquad P(F\mid E,T)=0.01.
\]

With utility linear in dollars,

\[
V_E(B)=0.99(1{,}000{,}000)=990{,}000,
\]

whereas

\[
V_E(T)
=
0.01(1{,}001{,}000)+0.99(1{,}000)
=
11{,}000.
\]

EDT therefore recommends one-boxing.

The recommendation does not require believing that reaching for one box magically fills it. The action indicates what the predictor probably anticipated and therefore what is probably already inside.

A useful generalization makes the assumptions explicit. Let the large prize be \(M\), the transparent-box amount be \(k\), and set

\[
p_B=P(F\mid E,B),\qquad p_T=P(F\mid E,T).
\]

Then

\[
V_E(B)=Mp_B,\qquad V_E(T)=Mp_T+k.
\]

One-boxing is preferred precisely when

\[
M(p_B-p_T)>k.
\]

Under symmetric conditional accuracy \(q\), where \(p_B=q\) and \(p_T=1-q\), this becomes

\[
q>\frac12+\frac{k}{2M}.
\]

An important modeling caution follows: “the predictor is 99% accurate overall” does not, by itself, establish both conditional probabilities used above. Overall accuracy also depends on how frequently each action occurs. The source’s calculation should therefore be read as assuming the relevant action-conditional reliability, not merely a single aggregate accuracy figure.

CDT, under the usual causal assumptions, instead recommends taking both boxes: whatever the opaque box already contains, taking the transparent box adds \(\$1{,}000\).

## 4. Psychological twins and correlated cooperation

The reference’s twin prisoner’s dilemma illustrates dependence without prediction.

Two isolated psychological twins choose between cooperation \(C\) and defection \(D\). Each receives:

- \(5\) if both cooperate;
- \(1\) if both defect;
- \(10\) for defecting against cooperation;
- \(0\) for cooperating against defection.

If their decisions match perfectly, then

\[
P(C_{\text{twin}}\mid E,C)=1,
\qquad
P(C_{\text{twin}}\mid E,D)=0.
\]

Consequently,

\[
V_E(C)=5,\qquad V_E(D)=1.
\]

EDT recommends cooperation, although neither twin causally controls the other.

Perfect matching is not essential. Suppose instead that

\[
P(C_{\text{twin}}\mid E,C)=q,
\qquad
P(D_{\text{twin}}\mid E,D)=q.
\]

Then

\[
V_E(C)=5q,
\qquad
V_E(D)=10(1-q)+q=10-9q.
\]

Cooperation wins exactly when

\[
q>\frac57.
\]

Thus EDT does not recommend cooperation merely because the other player is similar or likely to cooperate. It requires sufficiently strong **action-dependent evidence**. If the twin’s probability of cooperation is the same whichever action one takes, defection remains better.

The conflict with dominance reasoning is precise: defection pays more while holding the twin’s action fixed, but EDT does not hold its probability fixed when one’s own action is evidence about it.

## 5. The central objection: managing the news

The same mechanism that supports one-boxing generates less attractive recommendations in diagnostic-choice cases.

Consider an artificial model involving a pleasant but medically inert pill. A hidden disorder \(L\) makes people more inclined to take it:

\[
P(L)=\frac12,\qquad
P(A=\text{take}\mid L)=0.8,\qquad
P(A=\text{take}\mid\neg L)=0.2.
\]

Taking the pill provides utility \(1\); having the disorder costs utility \(100\). The pill neither causes nor cures the disorder.

Bayes’ rule gives

\[
P(L\mid \text{take})=0.8,
\qquad
P(L\mid \text{decline})=0.2.
\]

Hence

\[
V_E(\text{take})=1-100(0.8)=-79,
\]

while

\[
V_E(\text{decline})=-100(0.2)=-20.
\]

EDT recommends declining. Yet taking the pill improves utility by \(1\) whether or not the disorder is present.

This example, added here rather than drawn from the supplied article, exhibits the concern behind the article’s quotations from Lewis and Joyce: rational choice should bring about good outcomes, critics argue, rather than select actions that merely indicate them.

An evidentialist can reply that the stipulated probabilities make declining genuinely favorable evidence. But that reply sharpens the philosophical disagreement rather than eliminating it. The critic denies that favorable evidence alone supplies a reason to forgo a causally beneficial action.

The verdict is also sensitive to information. If the agent already knows whether \(L\) is present, taking the pill is better in either case. More generally, if observed information \(E\) screens off the dependence,

\[
P(L\mid E,A)=P(L\mid E),
\]

the objection disappears in this model.

However, one cannot simply assume that introspection always provides such screening information. That is an additional psychological and probabilistic claim, not a consequence of EDT’s formula.

## 6. Where do the probabilities come from?

The conditional-expectation rule is concise, but applying it requires a model of one’s own action. The supplied article does not settle how that model should be constructed during deliberation.

A workable interpretation is to evaluate options using a coherent distribution representing uncertainty **before the decision is resolved**, while including all information already available. This is an operational proposal, not an extra theorem supplied by the reference.

It leaves two difficulties.

### Self-prediction

An agent may expect to follow EDT and therefore become nearly certain of choosing its recommended action. Alternative actions can then become extremely improbable. If an alternative has probability zero, ordinary conditioning does not define its value:

\[
P(O\mid E,A=a)
\]

has a zero denominator.

One possible repair introduces small probabilities of mistakes or “trembles,” evaluates every action, and studies the limit as those probabilities shrink. But different error models can produce different limiting conditionals. A mistake caused by distraction may have different evidential significance from one caused by a hidden condition.

Thus zero-probability alternatives require additional modeling assumptions. Merely declaring them available does not specify the missing probabilities.

### Which dependencies survive deliberation?

Population correlations need not describe a particular informed deliberator. Conversely, deciding to deliberate carefully does not automatically erase correlations with predictors or psychological duplicates.

The practical requirement is to justify

\[
P(O\mid E,A=a)
\]

for this agent, with this information and this decision procedure. EDT supplies a comparison rule; it does not independently supply a complete psychology of choice.

## 7. Actions, policies, and repeated decisions

An action is a choice at one information state. A policy specifies choices across possible information states.

For example, a policy might say: accept an offer after observing one signal, reject it after another, and randomize after a third. Let \(\pi\) denote such a policy and \(\tau\) a complete resulting history.

A natural policy-level extension of EDT is

\[
V_E(\pi)
=
\sum_\tau P(\tau\mid E,\Pi=\pi)\,u(\tau),
\]

where \(\Pi\) represents the policy the agent adopts. For stochastic policies, the history includes the relevant random outcomes.

This is an operational extension proposed here; the reference explicitly states an action-level rule, not a complete theory of policy selection.

The extension preserves EDT’s central idea: adopting a policy may provide evidence about predictors, correlated agents, or hidden circumstances. It also exposes an important ambiguity. Conditioning on adopting a policy is not generally equivalent to conditioning on one action prescribed by that policy.

A predictor might forecast the entire policy. Another agent might share the same reasoning procedure but receive different observations. Two policies might prescribe the same action now while differing elsewhere. Those differences can matter evidentially even though the currently executed action is identical.

Randomization requires similar care. An independent coin can make its outcome uninformative about a hidden state. But choosing to use that coin may itself be informative, and a predictor might anticipate the outcome. “Randomize” is therefore not a general instruction to remove every relevant dependence.

There is also a distinction between evaluating a policy beforehand and reconsidering individual actions later. These evaluations condition on different events and potentially different information. Agreement is not guaranteed merely by writing down the expected-utility formula.

For sequential problems, one must therefore specify:

1. whether the object of choice is an act or a complete policy;
2. what is known at each decision point;
3. whether commitment is possible;
4. which decisions remain correlated.

The source leaves these questions open. A reasonable practice is to model commitment as a distinct available option and evaluate it explicitly, rather than silently switching between policy-level and act-level reasoning.

## 8. What the broader examples do—and do not—establish

The reference mentions attempts to use EDT in Sleeping Beauty betting problems to avoid Dutch books, alongside Conitzer’s criticism that some such agents remain vulnerable.

The justified conclusion is limited: adopting EDT does not automatically settle questions involving repeated awakenings, correlated acceptances, and uncertain self-location. An adequate calculation must specify which offers occur, which acceptances are linked, and how total payoff is counted. A credence about the coin alone is not a complete decision model.

The article also reports an “evidentialist’s wager”: correlations with many other decision-makers might make EDT’s stakes especially large. This is not a consequence of conditional expectation alone. Its force depends on credible correlations, on whose welfare enters utility, and on how uncertainty between decision theories should be handled. It is a further argument for EDT, not part of its definition.

## 9. A practical procedure

For an unfamiliar problem, an evidential analysis can proceed as follows:

1. **Specify the choice object:** immediate act, randomized act, or policy.
2. **Fix current information \(E\):** use it consistently across alternatives.
3. **Define outcomes and utility:** include all relevant costs and benefits.
4. **Model the joint distribution:** represent hidden states, predictions, other agents, and one’s own choice.
5. **Compute conditional expectations:** evaluate \(\mathbb E[u\mid E,A=a]\), or the explicitly chosen policy analogue.
6. **Audit the dependencies:** ask which survive conditioning on everything known, and which rely on controversial assumptions.
7. **Check undefined cases:** state any assumptions needed for zero-probability options or sequential implementation.

A causal diagram can help identify common causes and interventions. For EDT, however, identifying a dependence as noncausal does not by itself justify discarding it.

## Conclusion

EDT makes a clear mathematical proposal: choose the action associated with the highest conditional expected utility. Its strength is taking predictive and psychological dependencies seriously without requiring causal influence. Its difficulty is that favorable indication can recommend rejecting causally beneficial actions. Applying it well therefore requires more than a formula: it requires a defensible account of information, self-prediction, available alternatives, and the object of choice.

### References and source attribution

Primary source: Wikipedia contributors, [“Evidential decision theory,” supplied revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Selected works identified in that article:

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., and Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
- Conitzer, V. (2015). “A Dutch book against sleeping beauties who are evidential decision theorists.” *Synthese* 192: 2887–2899.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning a formal essay**

I need to produce a substantive essay between 2400 and 3000 words, focusing on decisions, policy dependencies, and counterfactual probabilities. The topics to explore include the accuracy of Newcomb’s problem, smoking criticisms, and the dynamics of policies. I should aim for about 2750-2900 words, including references. I'll need to ensure I discuss randomization and evidence interventions thoroughly while being mindful of the word budget, avoiding any spurious independence or unnecessary details.**Structuring an essay outline**

I’m setting up the outline for my essay, starting with the title and introduction, aiming for around 170 words. The formal section will be about 350 words, covering utilities and finite knowledge in the context of actions and information. I want to dedicate a portion to counterfactuals, Newcomb's problem, and the twin formulation, focusing on conditional accuracy and thresholds. I'll also dive into common causes, particularly related to smoking and health loss. The final section will analyze operational probabilities and their implications for actions and coherence in reasoning.**Analyzing policy dynamics**

I need to cover policies with a focus on conditioning versus action and how certain histories influence expected utility. I have to discuss potential inconsistencies and the importance of time consistency in Bayesian reasoning. There’s a chance that standard expected decision theory could fail based on how policies are reassessed in relation to correlated actions. I should clarify that perfectly correlated policies may limit unrealized actions, and it's crucial to differentiate between policies predicted by random factors and how they relate to hidden states.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/61235607-48f4-4761-8995-b8621e447ca1/call_0/request.json)

[Authoritative raw response](../../../../../../runs/61235607-48f4-4761-8995-b8621e447ca1/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing model execution correlation**

I’m exploring how to model two LLM executions with fixed weights but different user prompts. If randomness is independent, then outputs should be independent too. However, the uncertainty of outputs with fixed weights might lead to correlations during decision-making. It's interesting that identical weights don’t ensure identical outputs, which complicates reasoning. I need to keep in mind how the prompt influences this, especially when users mention independent executions and relate it to the twin prisoner experiment.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/61235607-48f4-4761-8995-b8621e447ca1/call_1/request.json)

[Authoritative raw response](../../../../../../runs/61235607-48f4-4761-8995-b8621e447ca1/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
