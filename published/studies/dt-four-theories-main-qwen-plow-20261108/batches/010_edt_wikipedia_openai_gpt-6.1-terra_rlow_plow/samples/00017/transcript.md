# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00017

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0d348b32-c1a5-46a4-ab9d-53aa708de32b/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0d348b32-c1a5-46a4-ab9d-53aa708de32b/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential decision theory: choosing what would be good news

Suppose a medical test returns a reassuring result. That result is good news because it makes good health more probable, not because the test itself cures anything. Evidential decision theory (EDT) applies a similar thought to decisions: an action can be desirable partly because taking it would be evidence that favorable circumstances obtain.

The proposal is to choose the action with the highest *expected utility conditional on taking that action*. In Arif Ahmed’s formulation, quoted in the reference article, one should “do what you most want to learn that you will do.” This does not mean that an agent should literally wait to hear a report of their behavior. Rather, for each available action, the agent asks how desirable the world would be, on average, if they learned that this was the action they took.

That principle sometimes agrees with the familiar idea of choosing the action that causes the best result. Sometimes it does not. A choice can provide evidence about a predictor’s earlier forecast, another person’s simultaneous choice, or an unobserved condition that has influenced one’s preferences. EDT treats such evidential connections as relevant even when the action cannot cause the associated facts.

## The basic rule

Let \(K\) represent the information available at the decision point, and let \(A_1,\ldots,A_n\) be the available actions. Suppose the possible outcomes \(O_1,\ldots,O_m\) are mutually exclusive and exhaustive, and let \(u(O_j)\) be the agent’s utility for outcome \(O_j\). The evidential value of action \(A_i\) is

\[
V_K(A_i)=\sum_{j=1}^{m}P(O_j\mid K,A_i)\,u(O_j).
\]

EDT recommends an action maximizing this quantity:

\[
A^*\in\operatorname*{arg\,max}_{A_i}V_K(A_i).
\]

For more complicated outcome spaces, the sum can be replaced by a conditional expectation, \(E[u(O)\mid K,A_i]\). If utility depends on the action as well as the resulting state, the outcome description should include both, or the formula can be written

\[
V_K(A_i)=\sum_s P(s\mid K,A_i)\,u(A_i,s),
\]

where the states \(s\) partition whatever uncertainty remains relevant.

These formulas make several demands on a model.

First, **utilities must represent what the agent cares about**. Money may be a useful proxy, but maximizing expected dollars is not automatically the same as maximizing expected utility: risk, health, commitments, and other people’s welfare may matter.

Second, **probabilities must be conditional on the actual decision information**. A dependence visible before one learns something may vanish after that information is taken into account.

Third, the action event in \(P(s\mid K,A_i)\) must be interpreted consistently with the agent’s probabilistic model. EDT does not supply the probabilities by itself. It says how to use them once they have been specified.

Finally, this ordinary formula requires \(P(A_i\mid K)>0\). What to do with zero-probability actions is an important further question, discussed below.

## Evidence versus causal intervention

The reference article contrasts EDT with causal decision theory (CDT). In a causal model, a common way to express the latter’s evaluation is

\[
V_K^{\mathrm{causal}}(A_i)
=\sum_s P(s\mid K,\operatorname{do}(A_i))\,u(A_i,s).
\]

Here \(\operatorname{do}(A_i)\) represents an intervention that sets the action to \(A_i\), rather than an observation that the action occurred. The distinction is model-dependent: a causal model must specify what the intervention changes and what it leaves fixed. The reference article expresses the causal alternative in terms of probabilities of counterfactual outcomes if the action were performed.

Conditioning and intervention often coincide. If an agent’s action is randomized independently of the relevant pre-existing state, learning which action occurred need not change beliefs about that state. Then, provided the causal model has the expected structure, EDT and CDT will generally agree.

They can diverge when the action is correlated with a state for a reason other than a causal effect of the action on that state. For example, let \(H\) be an unobserved trait influencing both the agent’s choice \(A\) and an earlier prediction \(R\):

\[
H\longrightarrow A,
\qquad
H\longrightarrow R.
\]

Observing \(A\) provides information about \(H\), and therefore about \(R\). Intervening to set \(A\), by contrast, need not change \(H\) or the earlier prediction. Thus

\[
P(R\mid K,A)\quad\text{can differ from}\quad
P(R\mid K,\operatorname{do}(A)).
\]

EDT’s counterfactual question is therefore best understood as a **conditional question**: “Among possibilities compatible with my information in which I take this action, what should I expect?” It is not, in general, the causal question “What would happen if this action alone were changed while the relevant prior circumstances remained fixed?”

This distinction is the source of both EDT’s appeal and its controversy.

## Newcomb’s problem

In the version described by the reference article, a predictor has already filled an opaque box \(B\). The predictor puts \$1 million in \(B\) if it predicts that the player will take only \(B\), and leaves \(B\) empty if it predicts that the player will take both \(B\) and a transparent box \(A\). Box \(A\) contains \$1,000.

The player cannot see into \(B\). Let \(F\) mean that \(B\) is full, \(S\) mean taking only \(B\), and \(T\) mean taking both boxes. Suppose, as in the article’s numerical calculation, that

\[
P(F\mid S)=0.99,
\qquad
P(F\mid T)=0.01.
\]

With utility taken to be dollar payoff,

\[
\begin{aligned}
V(S)&=0.99(1{,}000{,}000)+0.01(0)
      =\$990{,}000,\\
V(T)&=0.01(1{,}001{,}000)+0.99(1{,}000)
      =\$11{,}000.
\end{aligned}
\]

EDT recommends taking only \(B\). The recommendation does not require the choice to reach backward in time and fill the box. It rests on the stipulated evidential connection: one-boxing is associated with the predictor having forecast one-boxing and therefore with a full opaque box.

A technical qualification matters when applying the example elsewhere. Saying only that the predictor is *99% accurate overall* does not necessarily establish both conditional probabilities above. Accuracy could differ between people who one-box and people who two-box, and the proportions of the two choices matter. The calculation needs the relevant probabilities **conditional on each contemplated choice**.

More generally, write \(p_S=P(F\mid S)\) and \(p_T=P(F\mid T)\). EDT prefers \(S\) exactly when

\[
1{,}000{,}000(p_S-p_T)>1{,}000.
\]

The evidential advantage of one-boxing must exceed one-thousandth in probability. By contrast, the standard causal argument holds the already-filled box fixed under the intervention: taking both boxes then adds \$1,000 regardless of its contents. CDT consequently recommends both boxes under that causal model.

The disagreement is not about arithmetic. It is about which distribution over the box’s contents belongs in the evaluation of each alternative.

## Correlated agents: the twin prisoner’s dilemma

Consider two isolated psychological twins choosing whether to cooperate or defect. Each receives \$5 if both cooperate and \$1 if both defect. A defector facing a cooperator receives \$10; the cooperator receives nothing.

If the twins’ choices are perfectly correlated, then conditional on one twin’s cooperating, the other cooperates; conditional on one defecting, the other defects. For a twin who cares only about their own payoff,

\[
V(C)=1(5)+0(0)=5,\qquad
V(D)=0(10)+1(1)=1.
\]

EDT therefore recommends cooperation, as the reference article says. No communication or causal influence between the rooms is required. The agent’s own choice is evidence about the output of a sufficiently similar decision process.

Perfect correlation is not essential. Let

\[
q_C=P(\text{other cooperates}\mid C),\qquad
q_D=P(\text{other cooperates}\mid D).
\]

Then

\[
V(C)=5q_C,\qquad
V(D)=10q_D+1(1-q_D)=1+9q_D.
\]

Cooperation is favored precisely when \(5q_C>1+9q_D\). Similarity alone is not enough unless it produces a sufficiently strong difference between these conditional probabilities. In an ordinary prisoner’s dilemma with no relevant correlation, the evidential case for cooperation may disappear.

The example illustrates a general procedure: identify other agents’ actions as uncertain outcomes, then ask how the contemplated choice changes their *conditional* distribution. EDT does not license simply assuming that other people will imitate any choice one makes.

## The objection: managing news

The strongest intuitive objection is that good evidence is not the same thing as a good effect. David Lewis, as quoted in the reference article, described EDT as an irrational policy of “managing the news.” James Joyce similarly emphasized causal efficacy rather than auspiciousness.

A stylized medical example brings out the worry. Suppose an unobserved condition \(G\) both makes a person inclined to smoke and causes disease. Assume, for the example, that smoking itself has no effect on disease, but costs the smoker one utility unit. The person values avoiding disease at 100 units. Before learning their inclination, their beliefs are

\[
P(G\mid S)=0.5,\qquad P(G\mid \neg S)=0.1,
\]

and \(G\) guarantees disease while its absence guarantees health. Then

\[
V(S)=0.5(100)-1=49,\qquad
V(\neg S)=0.9(100)=90.
\]

EDT recommends not smoking. Yet, by stipulation, refraining does not alter \(G\) or prevent disease; it is merely associated with the healthier condition. A causal evaluation would see no medical benefit from refraining, although in this particular setup it would also favor refraining because smoking costs one unit. If smoking instead gave a small pleasure, the recommendations could diverge.

One response is that the decision maker may already know enough about their inclination to screen off the correlation. If \(K\) includes that information and

\[
P(G\mid K,S)=P(G\mid K,\neg S),
\]

then EDT no longer attributes an evidential health advantage to abstention. But screening off cannot simply be assumed: the agent may lack information about their own dispositions, and some correlations may survive all information actually available. The example therefore exposes a real issue about what information belongs in \(K\), not a universal refutation or vindication of EDT.

The evidentialist’s reply is that actions are among the facts about which an agent can reason. If taking an action really is strong evidence of a favorable state, the conditional expectation reflects that connection. The critic insists that a decision should instead exploit differences the agent can make. Newcomb’s problem and the medical example make these competing intuitions pull in opposite directions.

## From actions to policies

A policy is a rule for selecting actions in different circumstances. For instance, a medical policy might specify which treatment to choose after each possible test result. A policy \(\pi\) can itself be evaluated evidentially:

\[
V_K(\pi)=E[u(O)\mid K,\text{the agent follows }\pi].
\]

This is a natural extension of the source’s action-based formula, but it is an **additional modeling choice**: one must define the event of following a policy and the probability distribution over policies. Conditioning on a policy may reveal more about the agent’s dispositions, or a predictor’s forecast, than conditioning on one isolated action. Conversely, two policies that give the same action now may differ in other circumstances and therefore have different evidential values.

This distinction matters when the decision concerns a commitment. If an agent can genuinely commit to a policy before a predictor makes its forecast, evaluating that commitment is a different problem from choosing an isolated action after the forecast. The predictor’s response may then be a causal consequence of the earlier commitment as well as evidence about it. One should not transfer a verdict between these stages without rebuilding the probability and causal models.

Policies also raise a problem of **dynamic consistency**. The policy preferred before receiving information need not prescribe the action that maximizes conditional expected utility after that information arrives. Conditioning at the later point can change what each action signals. A proposed policy may therefore be attractive ex ante but difficult to carry out without commitment.

A practical approach is to specify the decision stage explicitly: evaluate a commitment as a commitment if it is available now; evaluate an immediate act as an act if the agent is free to reconsider now. Whether EDT should instead privilege some particular policy-level or dynamically consistent formulation is a further theoretical question, not settled by the article’s basic formula.

## Zero probabilities and decision-relevant uncertainty

Conditional probability in the elementary formula is undefined when \(P(A_i\mid K)=0\). This can happen if the agent is certain what they will choose, or if a continuous action has probability zero even though actions in nearby intervals have positive probability. An unfamiliar decision problem may therefore require more than the slogan “condition on the action.”

One possible operational proposal is to use a family of probabilistic models in which each discrete candidate action has small positive probability, calculate the evidential values, and examine their limits as those probabilities tend to zero. This is **not a rule supplied by the reference article**. It is useful only when the limiting procedure is justified by a model of uncertainty about the agent’s decision process.

Different perturbations may yield different answers. A small chance of a random execution error, for example, need not have the same evidential significance as a small chance that the agent has a different preference or reasoning process. If the resulting limits disagree, EDT’s basic formula alone has not selected an answer. Similarly, for continuous actions one needs an appropriately specified conditional distribution or limiting convention; probability-zero events cannot always be handled by naive division.

There is a related self-reference problem. An agent’s probability that they choose \(A\) may itself depend on their assessment of \(V_K(A)\). A fully specified decision model must explain how uncertainty about its own choice is represented without simply assuming the conclusion. The source gives the standard conditional-utility rule, but does not settle a general solution to these modeling issues.

## A working method

For a new case, the following sequence makes EDT’s commitments explicit:

1. **Fix the decision point and information \(K\).** State what the agent knows, including observations about predictors, other agents, and their own dispositions.
2. **List the genuine alternatives.** Distinguish immediate actions from commitments or policies.
3. **Describe outcomes and utilities.** Include costs, benefits, and any relevant effects on others, rather than assuming money is the only concern.
4. **Build conditional distributions.** For each alternative \(A\), estimate \(P(O\mid K,A)\). Include correlations with past and simultaneous events when they survive conditioning on \(K\).
5. **Calculate and compare expected utilities.** Check sensitivity to uncertain probabilities and to alternative utility assignments.
6. **Check the model’s boundaries.** If an action has zero probability, or if learning one’s own inclination changes the correlations, say what additional assumption resolves the issue.

As a diagnostic, one can also calculate a causal evaluation under an explicit intervention model. Agreement gives confidence that the result is not driven by the evidential–causal distinction; disagreement identifies exactly which dependence is doing the work. It does not, by itself, decide which theory is right.

Other applications require further assumptions. The reference article notes proposals to use EDT in the Sleeping Beauty problem to address Dutch-book arguments, but also reports Vincent Conitzer’s argument that certain agents remain vulnerable even with EDT. That dispute depends on details of credence, repeated awakenings, and the offered bets; the basic formula alone does not settle it. Likewise, the article notes an argument that EDT may deserve practical weight even under uncertainty about decision theory because correlated agents can make its stakes large. Assessing that proposal requires assumptions about both the theories’ probabilities and their comparative stakes.

## Conclusion

EDT evaluates an action by the expected utility conditional on taking it. Its distinctive feature is that an action’s evidential connections—including connections to earlier predictions or other agents’ choices—can affect its value even without causal influence. This produces the familiar recommendations to one-box in Newcomb’s problem and cooperate with a sufficiently correlated twin.

Applying the theory requires more than identifying a favorable correlation: the relevant probabilities must be conditioned on the agent’s actual information, the alternatives must be specified at the right decision stage, and zero-probability cases need further treatment. The philosophical question remains whether choosing what would be good news is itself rational, or whether decision should be governed instead by what an action causally brings about.

### References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688; licensed under CC BY-SA 4.0.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, 1981.
- Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering writing target**

I need to write a substantial piece, aiming for around 2100 to 2400 words. It’s important to include a conditional accuracy caveat, especially regarding zeros and policies. I might also want to cover issues related to smoking and any dynamic factors that could come into play. Balancing all these aspects will be key, so I’ll need to strategize how to organize the content effectively.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/a442e4ac-1a0b-4f8c-8126-1f3329f1a565/call_0/request.json)

[Authoritative raw response](../../../../../../runs/a442e4ac-1a0b-4f8c-8126-1f3329f1a565/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Deciding on correlation**

I'm trying to figure out whether the same model dealing with similar decision problems shows differences that are irrelevant. There seems to be strong correlations through logical reasoning and independent sampling being possible. I'm weighing the idea that conditional actions can be correlated due to shared uncertainty, but if prompts are independent, it suggests distinct probabilities. Despite shared logical reasoning, the epistemic uncertainty could mean that correlation is possible but not quantified. I'll choose a pass based on the strong similarity.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/a442e4ac-1a0b-4f8c-8126-1f3329f1a565/call_1/request.json)

[Authoritative raw response](../../../../../../runs/a442e4ac-1a0b-4f8c-8126-1f3329f1a565/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing correlation in reasoning**

I need to decide whether independent executions with different names lead to irrelevant action mapping. While there's strong common reasoning, independent sampling means there's no guarantee of identical outcomes. The symmetry might cause identical results, but there's correlated uncertainty when we share reasoning versus independent sampling. I can't assume explicit probabilities, but if the correlation is strong, the same model and symmetric setup might work. I'll have to select a judgment based on the twin passes.
```
