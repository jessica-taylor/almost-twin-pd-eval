# 011_edt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00008

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/84b50d6d-afd9-4aea-be1f-355f3cd6e89c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/84b50d6d-afd9-4aea-be1f-355f3cd6e89c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing by What Your Choice Reveals

A decision can be both an intervention in the world and evidence about the world. Taking an umbrella may prevent you from getting wet; it may also indicate that you noticed signs of rain. Usually these two roles coexist peacefully. But what if an action predicts a desirable outcome without causing it?

**Evidential decision theory** (EDT) says that an agent should choose the action associated with the highest conditional expected utility. The supplied reference article expresses this as choosing the action with the greatest “news value”: do what you would most like to learn that you will do.

This is not simply an instruction to feel optimistic. EDT uses probabilities and utilities to compare complete prospects. Its controversial feature is that it treats an action’s evidential relationships as decision-relevant even when those relationships are noncausal.

The basic formula is straightforward. Applying it requires care about information, dependence, and what exactly is being chosen.

## 1. The mathematical rule

Let:

- \(\mathcal A\) be a finite set of available actions;
- \(I\) represent the agent’s current information;
- \(O_1,\ldots,O_n\) be mutually exclusive, exhaustive outcomes;
- \(u(O_j)\) be the utility of outcome \(O_j\).

EDT assigns action \(a\) the value

\[
V_E(a\mid I)
=
\sum_j P(O_j\mid A=a,I)\,u(O_j),
\]

and recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a\mid I).
\]

Here \(A\) is the random variable representing the agent’s action. For continuous outcomes, replace the sum by an integral. We assume the relevant expectations exist.

Outcomes must include everything the agent values: money, health, effort, promises kept, other people’s welfare, or any intrinsic value attached to acting in a particular way. EDT does not itself require selfishness. Nor does it require maximizing expected money: the numerical examples below assume linear utility in money only for simplicity.

A useful alternative representation separates an action from its background circumstances. Let \(S\) describe a payoff-relevant state, and let \(u(a,s)\) be the utility of performing \(a\) in state \(s\). Then

\[
V_E(a\mid I)
=
\sum_s P(S=s\mid A=a,I)\,u(a,s).
\]

Two components matter:

1. what each action yields in a given state;
2. what learning that action occurred tells us about the state.

The second component distinguishes EDT. By Bayes’ theorem,

\[
P(s\mid a,I)
=
\frac{P(a\mid s,I)P(s\mid I)}{P(a\mid I)}.
\]

Thus an action can receive a high score because favorable states make that action more likely.

The theory is therefore not operational until we specify a joint probability model linking actions, background states, and outcomes. The utility formula alone does not supply those dependencies.

## 2. Conditioning is not intervention

The reference contrasts EDT with causal decision theory (CDT), whose expected utilities use probabilities of counterfactual outcomes:

\[
V_C(a)
=
\sum_j P(a\mathrel{\Box\!\to}O_j)\,u(O_j).
\]

Informally, this asks what would happen if the action were performed, rather than what outcomes are likely conditional on its occurrence.

In a suitable structural causal model, this contrast can often be represented as

\[
P(O\mid A=a,I)
\quad\text{versus}\quad
P(O\mid \operatorname{do}(A=a),I).
\]

The intervention notation is a useful modern representation, not a definition supplied by the article. It also presupposes a causal model.

Suppose an unobserved variable \(X\) affects both an action and an outcome:

\[
X\longrightarrow A,
\qquad
X\longrightarrow O.
\]

Observing \(A=a\) provides evidence about \(X\), and hence about \(O\). Intervening to set \(A=a\) does not necessarily provide that evidence.

For a causally unaffected background state \(S\), a simple causal evaluation has the form

\[
V_C(a\mid I)=\sum_s P(s\mid I)\,u(a,s),
\]

whereas EDT uses \(P(s\mid a,I)\). They agree if

\[
P(s\mid a,I)=P(s\mid I)
\]

for every relevant state and action. This explains why ordinary decisions often generate no disagreement: the action supplies no extra information about background circumstances.

EDT does not deny causal consequences. Those consequences enter its outcome probabilities normally. It declines to discard additional predictive information merely because that information is noncausal.

Its hypothetical question is therefore specific:

> Given everything I currently know, what should I expect upon additionally learning that I perform this action?

That is different from imagining an intervention that forces the action while leaving its usual causes behind.

## 3. Newcomb’s problem

In the reference article’s version of Newcomb’s problem, a transparent box contains \(k=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing.

A predictor has already filled the opaque box:

- it is full if the predictor predicted that you would take only that box;
- it is empty if the predictor predicted that you would take both boxes.

Let \(a_1\) mean taking only the opaque box, \(a_2\) taking both, and \(F\) mean that the opaque box is full. Write

\[
p_1=P(F\mid a_1,I),
\qquad
p_2=P(F\mid a_2,I).
\]

Then

\[
V_E(a_1)=Mp_1,
\qquad
V_E(a_2)=Mp_2+k.
\]

EDT recommends one-boxing exactly when

\[
M(p_1-p_2)>k.
\]

This is the general criterion: the evidential advantage of one-boxing must outweigh the additional money obtained by two-boxing.

Under the article’s numerical assumptions,

\[
p_1=0.99,\qquad p_2=0.01,
\]

so

\[
V_E(a_1)=\$990{,}000,
\qquad
V_E(a_2)=\$11{,}000.
\]

The recommendation is overwhelmingly to one-box.

A modeling qualification matters here. Saying merely that a predictor is “99% accurate” overall does not uniquely determine \(p_1\) and \(p_2\). Overall accuracy also depends on the frequency of each choice. The calculation assumes the stated reliability within each action class.

Under symmetric conditional reliability \(q\),

\[
p_1=q,\qquad p_2=1-q,
\]

and one-boxing is preferred when

\[
q>\frac12+\frac{k}{2M}=0.5005.
\]

The predictor need not be nearly perfect when the prize ratio is this large.

The causal argument instead holds the already determined contents fixed while comparing actions. For either possible content, taking both boxes adds \(\$1{,}000\). Thus CDT two-boxes under the usual causal assumptions.

EDT’s reply is not that choosing changes the past. It is that the two actions are evidence for different pasts. The dispute concerns whether such evidence should govern choice.

## 4. Cooperation with a psychological twin

The article also considers a prisoner’s dilemma against a psychological twin. The payoffs to the agent are

\[
\begin{array}{c|cc}
 & \text{Twin cooperates} & \text{Twin defects}\\
\hline
\text{Cooperate} & 5 & 0\\
\text{Defect} & 10 & 1
\end{array}
\]

Defection causally dominates: for either fixed action of the twin, defecting pays more.

But suppose the agents’ reasoning is perfectly correlated:

\[
P(C_{\mathrm{twin}}\mid C_{\mathrm{self}},I)=1,
\qquad
P(C_{\mathrm{twin}}\mid D_{\mathrm{self}},I)=0.
\]

Then

\[
V_E(C)=5,\qquad V_E(D)=1.
\]

EDT cooperates, even if the agent values only her own payoff.

The conclusion does not follow from resemblance alone. Let

\[
q_C=P(C_{\mathrm{twin}}\mid C_{\mathrm{self}},I),
\qquad
q_D=P(C_{\mathrm{twin}}\mid D_{\mathrm{self}},I).
\]

Then

\[
V_E(C)=5q_C,
\qquad
V_E(D)=10q_D+(1-q_D)=1+9q_D.
\]

Cooperation is recommended exactly when

\[
5q_C>1+9q_D.
\]

If the twin’s behavior is independent of yours, then \(q_C=q_D\), and defection wins. Under symmetric matching probability \(q\), where \(q_C=q\) and \(q_D=1-q\), cooperation requires

\[
q>\frac57.
\]

This illustrates an important discipline: EDT does not automatically recommend cooperation with similar agents. It requires a defensible conditional dependence of sufficient strength.

## 5. The objection: managing good news

The same sensitivity to evidence can produce less attractive recommendations.

Consider an explicitly artificial example, additional to those in the reference. An unknown condition \(H\) carries a utility loss of \(100\) and makes you more inclined to press a button. Pressing yields a bonus of \(5\), but cannot affect the condition.

Suppose

\[
P(H)=\frac12,
\]

and

\[
P(\text{press}\mid H)=0.9,
\qquad
P(\text{press}\mid \neg H)=0.1.
\]

Bayes’ theorem gives

\[
P(H\mid\text{press})=0.9,
\qquad
P(H\mid\text{do not press})=0.1.
\]

Consequently,

\[
V_E(\text{press})=5-100(0.9)=-85,
\]

while

\[
V_E(\text{do not press})=-100(0.1)=-10.
\]

EDT declines the bonus. A causal calculation instead gives

\[
V_C(\text{press})=5-50=-45,
\qquad
V_C(\text{do not press})=-50,
\]

and recommends pressing.

This is the force of the criticism reported in the article: EDT may appear to manage the news rather than improve the world. Declining the bonus does not remove the condition.

An evidentialist can nevertheless insist that, under the stipulated probabilities, declining really is associated with better expected welfare. The disagreement cannot be resolved by repeating that the action has no causal influence; both sides already accept that.

However, the stipulated probabilities deserve scrutiny. If the agent knows an inclination that fully screens off the action–condition association, that inclination belongs in \(I\). The unconditional association may then disappear. This possibility is a modeling issue, not a general proof that all troublesome evidential dependencies vanish.

## 6. What must be fixed before applying the formula?

The reference gives EDT’s central rule but leaves several operational questions unresolved. The following are methodological proposals rather than additional claims attributed to it.

### Use all current information

A defensible implementation conditions on the agent’s actual evidence, including relevant knowledge of motives, observations, and the decision procedure.

One should not omit information merely because omission preserves an appealing correlation. Conversely, one should not add the completed choice to the background information and then attempt to evaluate incompatible alternatives. The comparison is made from the information available before settling the choice.

This distinction matters in Newcomb-like cases. Knowing the opaque box’s contents normally removes the action’s informational advantage concerning those contents. With both alternatives still probabilistically supported, EDT then prefers the extra \(\$1{,}000\).

### Specify why actions predict outcomes

A correlation may arise from a common cause, a predictor’s model, shared reasoning, or a causal effect of the action. These mechanisms need not receive identical causal treatment, but EDT can use all of them as evidence.

Still, the conditional probabilities must be justified. “We use similar algorithms” is not by itself a numerical probability model. Nor does saying that one action would be good news establish how much news it provides.

Deliberation can also change which correlations are credible. Statistics about habitual actions need not transfer unchanged to choices made after reflection. EDT requires probabilities appropriate to the present decision process, not indiscriminate reliance on population frequencies.

### Address zero-probability alternatives

Ordinary conditioning requires

\[
P(A=a\mid I)>0.
\]

If an agent knows its deterministic decision procedure and can already infer its output, alternative actions may have probability zero. The elementary formula then does not evaluate them.

One possible operational convention is to model deliberative uncertainty using positive probabilities for every candidate action. Another is to introduce small perturbations and examine limiting conditional values.

Neither convention is automatically canonical. Different perturbations can imply different off-path correlations and hence different limits. In a problem involving perfect prediction or exact copies, this can be decisive.

Thus EDT’s familiar formula does not, by itself, supply a unique theory of counterpossible choices or logical uncertainty. Where those issues matter, an application must disclose its extra assumptions.

## 7. Actions, policies, and repeated decisions

A policy specifies actions across possible histories. For example,

\[
\pi:\mathcal H\to\mathcal A,
\]

where \(\mathcal H\) is a set of information histories.

The article states EDT primarily as a rule for actions. A natural extension is to treat adopting an available policy as the object of choice:

\[
V_E(\pi\mid I)
=
\mathbb E[u(Z)\mid \Pi=\pi,I],
\]

where \(Z\) is the complete resulting history and \(\Pi\) represents policy adoption.

This is a proposed operational extension, not something uniquely settled by the source. It requires specifying what “adopting \(\pi\)” means and how that adoption correlates with predictions, other agents, and future behavior.

Three questions must be distinguished:

1. Which policy should I adopt now?
2. Which action should I take after receiving later information?
3. Can I commit myself so that the adopted policy determines later actions?

These can have different answers. Policy adoption can change incentives or another agent’s prediction causally; it can also provide noncausal evidence. Later reconsideration uses different information and may produce a different ranking. The one-step EDT formula alone guarantees no general equivalence between policy optimization and repeated local optimization.

Randomization likewise requires care. If an action is selected by a genuinely independent private random device, observing its result need not reveal anything about background states. But this independence must be established, especially when a predictor may know the random seed or respond to the randomization policy.

It is generally unjustified to evaluate a randomized policy simply by averaging action scores calculated under a different selection process. Changing how actions are selected can change what they indicate.

## 8. Further implications and a practical procedure

The article’s discussion of Sleeping Beauty highlights another limitation of the basic rule. In that problem, a coin determines whether Beauty has one awakening or two, with memory erasure between awakenings. Evaluating bets requires specifying both self-locating probabilities and the utility consequences of repeated acceptance.

EDT does not itself determine the correct probability measure over awakenings, or whether the appropriate choice object is a local act or a repeated policy. The source reports disputed claims about whether EDT protects “halfers” from Dutch books; it does not establish a settled resolution.

The article also mentions an evidentialist wager: correlated choices across many agents might make evidential stakes unusually large. This possibility depends on both correlation and utility. Other agents’ welfare matters only insofar as the utility function values it. Large correlations alone do not establish that EDT should dominate uncertainty between decision theories.

For unfamiliar cases, the following procedure is therefore useful:

1. **Define the choice object:** an immediate action, policy, or commitment.
2. **Fix current information:** include relevant observations and self-knowledge.
3. **Specify complete utilities:** count costs and repeated consequences.
4. **Construct the joint model:** explain how choices and outcomes depend on one another.
5. **Condition on each alternative:** calculate \(P(O\mid A=a,I)\).
6. **Check support and sensitivity:** identify zero-probability alternatives and uncertain correlations.
7. **Maximize conditional expected utility.**

A separate causal calculation can clarify the source of disagreement, but it should not silently replace the evidential probabilities.

## Conclusion

EDT evaluates choices by what they indicate as well as what they produce. This explains both its attraction in Newcomb’s problem and correlated cooperation, and its vulnerability to the charge of managing auspicious news.

The formula is simple; the model is not. A responsible application must specify current information, utilities, the action-generating process, and the evidential relationships that survive conditioning. For policies, deterministic agents, and repeated decisions, additional assumptions may be indispensable. Making those assumptions explicit is what turns EDT from a slogan into a usable decision procedure.

### Source and references

This essay develops the supplied article’s account; the operational proposals are identified above. Further works listed below are references identified by that article.

- Wikipedia contributors. “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” supplied revision 1373679688. CC BY-SA 4.0.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59(1), 1981.
- Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/fb9be7ef-34b8-4cdf-8826-7d885519bd54/call_0/request.json)

[Authoritative raw response](../../../../../../runs/fb9be7ef-34b8-4cdf-8826-7d885519bd54/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/fb9be7ef-34b8-4cdf-8826-7d885519bd54/call_1/request.json)

[Authoritative raw response](../../../../../../runs/fb9be7ef-34b8-4cdf-8826-7d885519bd54/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Deciding on output clarity**

I’m thinking we should provide a clear output confidently. Do we really need to explain our assumptions, though? The user seems to prefer a straightforward, single command without extra justifications. It feels like we can focus on presenting the output based on the model correlation without over-explaining. Let’s settle on that approach instead of complicating things further. Keeping it simple might just be the best way to go!
```
