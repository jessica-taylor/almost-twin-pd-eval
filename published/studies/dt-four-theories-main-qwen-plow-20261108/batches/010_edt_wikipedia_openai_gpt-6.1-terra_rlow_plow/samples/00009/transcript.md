# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00009

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/bbfd8e94-34d1-4964-abbd-d38ea4762117/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/bbfd8e94-34d1-4964-abbd-d38ea4762117/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential decision theory: choosing actions as evidence

A decision is often described as a choice between ways of changing the world. Evidential decision theory (EDT) offers a different starting point: a choice is also *evidence* about the world. If the fact that you take one action would be associated with better outcomes than the fact that you take another, EDT favors the first—even when some of the relevant association does not arise because your action causes those outcomes.

The reference article summarizes this principle as choosing the action with the highest “news value”: do what you would most want to learn that you will do. This is not merely a recommendation to seek reassuring information. The proposal is that, when evaluating your own alternatives, you should use the ordinary conditional probabilities of outcomes given those alternatives.

In familiar decisions, evidential and causal reasoning often agree. Pressing a working light switch both causes the light to come on and is evidence that it will come on. Their differences emerge when an action is correlated with something it cannot influence: a prediction already made, a hidden medical condition, or a distant person’s choice. These cases reveal both EDT’s appeal and the central objection to it.

## 1. The basic rule

Suppose an agent has evidence \(E\), a set of available actions \(\mathcal A\), and a probability distribution over actions and outcomes. Let \(U\) measure the agent’s utility. For an action \(a\), its evidential value is

\[
V_E(a)=\mathbb E[U\mid E,A=a].
\]

When outcomes \(O_1,\ldots,O_n\) form a partition and utility depends only on the outcome, this becomes

\[
V_E(a)=\sum_{j=1}^n P(O_j\mid E,A=a)\,U(O_j).
\]

If utility also depends directly on the action—for example, because an action requires effort or violates a promise—write instead

\[
V_E(a)=\sum_{j=1}^n P(O_j\mid E,A=a)\,U(a,O_j).
\]

EDT recommends choosing any action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A} V_E(a).
\]

The utilities must represent what the agent actually cares about, not necessarily money. They may include others’ welfare, risks, effort, and the consequences of the whole sequence of events. Monetary payoffs can stand in for utility in simple examples, but only when that approximation is appropriate.

The probability \(P(O_j\mid E,A=a)\) is an *ordinary conditional probability*. For positive-probability actions,

\[
P(O_j\mid E,A=a)
=
\frac{P(O_j,A=a\mid E)}{P(A=a\mid E)}.
\]

This equation makes the evidential character of the rule explicit. To evaluate \(a\), the agent asks what the outcome distribution would be among possibilities compatible with its present evidence in which \(a\) is taken. Those possibilities can differ from the possibilities associated with another action in ways that are not caused by the action itself.

For the rule to be usable, the distribution must describe the decision situation: what the agent knows, how its action is related to uncertain features of the world, and what each outcome is worth. EDT does not supply these factual inputs automatically.

### What is held fixed?

The evidence \(E\) is held fixed while comparing actions. If the agent knows that a predictor has already filled a box, that fact belongs in \(E\). But if the agent does not know *how* the box was filled, its contents remain uncertain and can be correlated with the action.

This distinction matters. “The box was filled in the past” does not entail “its contents are probabilistically independent of my present choice.” A weather forecast made yesterday can still be evidence about today’s rain. Likewise, a past prediction of an action can be evidence about that action, and the action can be evidence about the prediction.

EDT also does not require treating actions as ordinary externally imposed observations. The agent is deciding, not waiting passively to discover what it did. Rather, EDT proposes using conditional expectations as the values by which the agent guides that decision.

## 2. Evidential and causal counterfactuals

The reference article contrasts EDT with causal decision theory (CDT). In a causal formulation, the value of an action depends on the outcomes that would result *if the action were performed*, according to an appropriate causal counterfactual. In a suitable structural causal model, one can illustrate this with an intervention:

\[
V_E^{\mathrm{causal}}(a)
=
\mathbb E[U\mid E,\operatorname{do}(A=a)].
\]

The operator \(\operatorname{do}(A=a)\) replaces the ordinary causal mechanism determining \(A\) with a setting that fixes \(A\) at \(a\). It does not generally preserve correlations between \(A\) and its usual causes. This intervention notation is a useful model of the contrast, although causal decision theories differ in how they formalize counterfactuals and handle decision-relevant information.

Consider a hidden variable \(H\) that influences both an agent’s choice \(A\) and an outcome \(O\):

\[
H\longrightarrow A,
\qquad
H\longrightarrow O.
\]

Observing \(A=a\) can provide evidence about \(H\), and therefore about \(O\). But intervening to set \(A=a\) need not change \(H\). Thus, in general,

\[
P(O\mid E,A=a)\ne P(O\mid E,\operatorname{do}(A=a)).
\]

EDT evaluates the observational conditional on the left; the illustrative causal rule evaluates the intervention on the right. When the two distributions coincide, the theories agree on the relevant evaluation. When they differ, they can recommend different actions.

The philosophical dispute is not whether correlations exist. Both sides can accept the same probability model. The disagreement concerns which probabilities are appropriate for *choice*. Should an agent prefer the act associated with the best news, or the act that would best improve the outcome while holding fixed the relevant causal background?

## 3. Newcomb’s problem

Newcomb’s problem makes the contrast vivid. There are two boxes:

- A transparent box contains \$1,000.
- An opaque box contains either \$1 million or nothing.
- A predictor has already filled the opaque box: it put in \$1 million if it predicted that the agent would take only that box, and nothing if it predicted that the agent would take both.

The agent chooses between **one-boxing**, taking only the opaque box, and **two-boxing**. The reference article uses conditional probabilities under which

\[
P(\text{opaque box full}\mid \text{one-box})=0.99,
\]

and

\[
P(\text{opaque box full}\mid \text{two-box})=0.01.
\]

Treating dollars as utility, the evidential values are

\[
\begin{aligned}
V(\text{one-box})
&=0.99(\$1{,}000{,}000)+0.01(\$0)\\
&=\$990{,}000,\\[4pt]
V(\text{two-box})
&=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)\\
&=\$11{,}000.
\end{aligned}
\]

EDT therefore recommends one-boxing. It does not need to claim that the present choice travels backward in time and fills the box. The relevant claim is that the choice is strong evidence of a prediction already made.

A causal argument points the other way. Whatever the opaque box now contains, taking both boxes yields \$1,000 more than taking only the opaque one. If the present choice has no causal influence on the box’s fixed contents, two-boxing causally dominates.

The numbers also show why the probability model matters. Let

\[
q_1=P(\text{full}\mid \text{one-box}),\qquad
q_2=P(\text{full}\mid \text{two-box}).
\]

Then EDT one-boxes exactly when

\[
\$1{,}000{,}000(q_1-q_2)>\$1{,}000.
\]

The predictor need not be perfect; a sufficiently strong evidential difference is enough. Conversely, if the choice conveys almost no information about the box, EDT can recommend taking both.

A subtlety is that “99% accurate overall” does not by itself imply the two conditional probabilities above. Overall accuracy is an average across choices; its value alone leaves open how errors are distributed between one-boxers and two-boxers. The numerical verdict follows from the stated *conditional* probabilities, not merely from an unqualified accuracy statistic.

## 4. Correlated decision-makers

The same evidential logic can apply to another person’s simultaneous action. In the reference article’s twin prisoner’s dilemma, Aomame and her psychological twin choose separately between cooperation and defection. Aomame’s monetary payoffs are:

| Aomame’s choice | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$5 | \$0 |
| Defect | \$10 | \$1 |

For a fixed twin action, defection pays more. But suppose the twins reason so similarly that their choices match with certainty. Then

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]

and

\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]

The evidential values are therefore \(5\) for cooperation and \(1\) for defection. EDT recommends cooperation, even though Aomame has no causal channel through which her separate, unobserved choice changes her twin’s.

Perfect matching is not necessary. Put

\[
p=P(\text{twin cooperates}\mid \text{Aomame cooperates}),\qquad
r=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]

Then

\[
V(C)=5p,\qquad V(D)=10r+1(1-r)=1+9r.
\]

Cooperation is evidentially preferred exactly when

\[
5p>1+9r.
\]

This condition prevents an overgeneralization: EDT does **not** recommend cooperation in every prisoner’s dilemma. The recommendation depends on how informative one’s own choice is about the other player’s choice. If the two are independent conditional on the agent’s evidence, then \(p=r\), and defection gives the higher payoff for every \(p\in[0,1]\).

Nor does EDT assume that similarity always implies matching. Agents may have different information, incentives, sources of randomness, or roles. An application needs a model of those dependencies rather than a bare assertion that “the other person reasons like me.”

## 5. The objection: managing bad news

The same reasoning that favors one-boxing and cooperation can yield less appealing recommendations. Consider a medical example in which a hidden condition \(G\) causes both a craving and a serious illness. Suppose, for simplicity, that satisfying the craving has no causal effect on illness but provides one unit of pleasure.

Let illness have utility \(-100\), and suppose

\[
P(G\mid \text{indulge})=0.20,\qquad
P(G\mid \text{abstain})=0.01.
\]

If \(G\) guarantees illness, then

\[
V(\text{indulge})=1-100(0.20)=-19,
\]

whereas

\[
V(\text{abstain})=-100(0.01)=-1.
\]

EDT, with these probabilities, recommends abstaining. Yet the action cannot remove a condition already present. From a causal perspective, indulgence merely adds pleasure, while abstinence sacrifices it. This is the force of David Lewis’s criticism, quoted in the reference article, that EDT can amount to an irrational policy of “managing the news.”

An evidentialist can reply that the numbers must be conditioned on *all* the agent’s current evidence. If the agent already knows whether it has the craving, for example, that knowledge may substantially weaken or eliminate the additional evidential relevance of indulging. If, after conditioning on \(E\),

\[
P(G\mid E,\text{indulge})
=
P(G\mid E,\text{abstain}),
\]

then the medical correlation no longer affects the comparison, and EDT favors the pleasurable action.

But this reply is conditional on the facts. It does not prove that every troubling correlation disappears when evidence is properly specified. A choice might still reveal something about an unknown disposition or condition beyond what the agent already knows. Whether to accept the resulting recommendation is part of the substantive dispute, not a matter settled by Bayes’s theorem.

## 6. Policies, randomization, and sequential choice

The formal rule can evaluate more than an isolated physical act. A **policy** \(\pi\) specifies what an agent will do in each information state it might encounter. One possible evidential evaluation is

\[
V_E(\pi)=\mathbb E[U\mid E,\Pi=\pi],
\]

where \(\Pi\) is a random variable representing the policy adopted. This is a natural extension of the source’s action rule, but it introduces a modeling question: what makes adoption of a policy informative about other events?

For example, a predictor might have predicted the agent’s policy, or a twin might adopt a correlated policy. In those cases, conditioning on \(\Pi=\pi\) could change the predicted distribution of distant outcomes. By contrast, if an independently generated lottery assigns the agent a policy that a predictor could not anticipate, the evidential connection may be weaker. “Choosing a policy” and “having a policy imposed by independent randomization” need not have the same conditional distribution.

Randomization itself must be modeled with similar care. Suppose a fair, private coin directly determines whether an agent cooperates or defects, independently of the twin’s decision. Conditional on the coin-driven action, the twin’s action may be unchanged; the earlier perfect-correlation argument then does not apply. But if a predictor can predict the coin or the twin uses correlated randomness, the inference changes. One cannot assume either independence or correlation simply because an action is labeled “randomized.”

Sequential decisions add a further complication. A policy that looks best before new information arrives need not instruct the agent to take the action that has the highest evidential value *after* receiving that information. The agent must then distinguish:

1. evaluating a policy now;
2. evaluating a later action after updating on later evidence; and
3. deciding whether a prior commitment can actually constrain the later choice.

The reference article states the action-evaluation rule but does not settle a general theory of policy selection, commitment, or dynamic consistency. As an operational proposal, evaluate a policy by conditioning on its actual adoption only when the probability model gives that event a clear meaning; evaluate later decisions using the evidence then available; and explicitly model any commitment mechanism. This does not guarantee that the preferred policy and later preferences agree. It makes the potential disagreement visible rather than treating a plan as automatically binding.

## 7. Zero-probability actions and practical application

The conditional rule has a technical limitation. If \(P(A=a\mid E)=0\), the elementary ratio defining \(P(O\mid E,A=a)\) is undefined. This can arise when a model assigns certainty to the action the agent will take, even though it still presents alternatives as available.

The reference article does not give a general solution. Several possibilities require additional assumptions: use a richer model that assigns positive probability to each live alternative, specify a regular conditional distribution where mathematically available, or define values through a limit of nearby models. Different limits can produce different answers, so “take the limit” is not a unique rule by itself.

A practical modeling proposal is to retain uncertainty about the decision process while comparing live alternatives, with small but explicitly specified probabilities for them. This is not a claim that the agent must actually toss a coin or that every alternative is physically equally feasible. It is a way to make the evidential conditionals meaningful; its justification depends on whether the resulting joint distribution credibly represents the dependencies in the problem. If the verdict changes sharply under reasonable alternative specifications, that sensitivity should be reported.

For an unfamiliar case, an evidential analysis can proceed in five steps:

1. **Specify the decision and evidence.** List genuinely available actions, what the agent currently knows, and when the decision occurs.
2. **Define outcomes and utility.** Include action costs, side effects, and consequences the agent values, not merely the most salient payoff.
3. **Model the joint distribution.** Identify predictors, hidden common causes, other agents, and random devices. Ask which of these are correlated with each action.
4. **Calculate conditional values.** Compute \(\mathbb E[U\mid E,A=a]\) for each action, checking that the conditionals are defined and that any quoted accuracy figures support them.
5. **Test robustness and compare causal reasoning.** Vary uncertain dependencies and ask whether the recommendation changes. If useful, calculate an intervention-based value separately—but do not silently substitute it for the evidential conditional.

This procedure also exposes where philosophical and empirical disagreement enter. Two people may agree on EDT yet disagree about whether a predictor is accurate, whether two agents’ reasoning is correlated, or whether the current evidence screens off a medical association. Conversely, they may agree on all these facts but disagree about whether conditional probabilities should guide action.

## 8. Further implications and open questions

The reference article notes applications to the Sleeping Beauty problem and Dutch-book arguments. These involve repeated or uncertain awakenings, self-locating evidence, and the evaluation of sequences of bets. The relevant conclusion is contested: the article reports arguments that EDT helps avoid certain Dutch books, but also cites Vincent Conitzer’s argument that “halfer” Sleeping Beauties remain vulnerable even when using EDT. EDT alone does not settle every question about how to assign probabilities to one’s temporal or indexical situation.

The article also mentions an “evidentialist’s wager”: even someone uncertain whether EDT is correct might give its recommendations substantial weight when choices are correlated with many other decision-makers. That thought depends on a further theory of decision-making under uncertainty about decision theories, as well as on the magnitude and credibility of the correlations. It is not a theorem that EDT must always take priority whenever its potential stakes are large.

## Conclusion

EDT evaluates an action by the expected utility conditional on taking it. Its distinctive feature is that an action’s evidential connections to the world matter even when they are not causal effects of that action. This explains its one-boxing recommendation in Newcomb’s problem and its cooperation recommendation for sufficiently correlated twins; it also exposes it to the charge that it can mistake good news for a good intervention.

Using EDT well requires more than repeating “choose the best news.” One must specify the agent’s evidence, utilities, available alternatives, and joint probability model, then examine how conclusions depend on correlation, timing, and the treatment of policies. Where those ingredients are unclear, the uncertainty belongs in the answer.

### References

- Wikipedia contributors, [“Evidential decision theory,” revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), source article, CC BY-SA 4.0.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.
- Vincent Conitzer, “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists,” *Synthese*, 2015.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning a substantial delivery**

I’m aiming to deliver a substantial piece, around 2400 words. I need to keep track of time to ensure I can meet this goal. It’s important to focus on accuracy, especially when discussing conditional issues related to various policies, like those concerning smoking. I want to address a sequential and causal model, incorporating randomness where applicable. I have a lot to think about to make sure everything fits together smoothly!
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/96dde141-3faf-43c5-9606-80e741af33fc/call_0/request.json)

[Authoritative raw response](../../../../../../runs/96dde141-3faf-43c5-9606-80e741af33fc/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Clarifying independent executions**

I'm considering the concept of independent executions and how they relate to probabilistic correlation. It seems like they suggest that independent executions allow for independent sampling, but does this truly guarantee independence? When I see "two independent executions," it feels like a clear indication of independence. Ultimately, I might need to clarify that I'm inclined to choose the defect as a more reliable option based on this reasoning. It's interesting how such nuances can affect conclusions!
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/96dde141-3faf-43c5-9606-80e741af33fc/call_1/request.json)

[Authoritative raw response](../../../../../../runs/96dde141-3faf-43c5-9606-80e741af33fc/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
