# 008_edt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00011

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d082c561-32e5-4162-ae3b-c6e5f0009d0d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d082c561-32e5-4162-ae3b-c6e5f0009d0d/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing Actions as News

## 1. The core idea

Evidential decision theory (EDT) says to evaluate an act by what it would indicate about the world, not by what it would cause. The source puts the slogan as "do what you most want to learn that you will do." The quantity to maximize is the *news value* of an act, which is the expected desirability of outcomes conditional on learning that the act was taken:

$$V(A)=\sum_j P(O_j\mid A)\,D(O_j).$$

Here $D$ is desirability (utility) and $P(\cdot\mid A)$ is the agent's ordinary conditional credence. The source contrasts this with the causal decision theory (CDT) formulation of Gibbard and Harper (1976):

$$U(A)=\sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\,D(O_j),$$

where $A\mathrel{\Box\!\!\rightarrow}O_j$ means "if $A$ were performed, $O_j$ would occur." The two quantities differ whenever $P(A\Box\!\!\rightarrow O)\neq P(O\mid A)$. The source's claim is that this gap is the whole disagreement. Both theories are expected-utility maximizers, and they differ in which probabilities they use.

The rest of this essay covers how to compute $V$, how it handles dependence, where the source leaves questions open, and what is at stake philosophically. Material beyond the source is flagged as mine.

## 2. Computing $V$: a procedure

1. **Fix the option set.** List the acts $A_1,\dots,A_n$ available to the agent.
2. **Fix the outcome partition.** Choose outcomes $O_j$ fine-grained enough to carry everything the agent cares about.
3. **Assess conditional credences** $P(O_j\mid A_i)$ using the agent's whole joint probability model, including every correlation between her act and the world.
4. **Assign desirabilities** $D(O_j)$.
5. **Pick the act with maximal $V$.**

Step 3 does the work. EDT has no separate causal machinery. Evidential relevance is whatever the joint distribution says it is. Causal links matter only because they induce correlations. Common causes, prediction, and similarity of reasoning matter in the same way.

A useful rewriting (mine) conditions on a hidden state $S$:

$$V(A)=\sum_s P(s\mid A)\,\mathbb E[D\mid A,s].$$

CDT replaces $P(s\mid A)$ with the unconditional $P(s)$, at least when $S$ is causally independent of $A$. The whole controversy sits in that one factor: is the state *evidence-sensitive* to my act, or merely causally independent of it?

## 3. Worked examples

### Newcomb's problem

Box A holds \$1,000 for certain. Box B holds \$1,000,000 iff the predictor predicted one-boxing. The predictor is 99% accurate. The source computes:

$$V(\text{one-box})=0.99\cdot 10^6=\$990{,}000,\qquad V(\text{two-box})=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000.$$

So EDT one-boxes. CDT two-boxes, because the contents are already fixed and two-boxing gains \$1,000 in either state.

Let accuracy be $p$ in both directions. Then

$$V(1)=p\cdot 10^6,\qquad V(2)=10^3+(1-p)\cdot 10^6.$$

One-boxing wins iff $p>0.5005$. Even a barely informative predictor favors one-boxing for the evidentialist. The threshold is slightly above ½ because the \$1,000 is a small sweetener.

### Twin prisoner's dilemma

Payoffs are 5/5 for mutual cooperation, 1/1 for mutual defection, and 10/0 for unilateral defection. If the twin's reasoning mirrors Aomame's, then $P(\text{twin } C\mid \text{I } C)=1$. The source gets $V(C)=5>V(D)=1$. CDT defects, since her act cannot causally affect her twin's.

With imperfect correlation, let $q=P(\text{twin copies me})$. Then

$$V(C)=5q,\qquad V(D)=10(1-q)+q=10-9q.$$

Cooperation wins iff $q>10/14\approx0.714$. This threshold is mine, an extension of the source's $q=1$ case. It shows that the verdict is robust only when the correlation really is strong.

### Sleeping Beauty

The source notes only that EDT has been invoked to avoid Dutch books against halfers (credence ½ in heads), and that Conitzer argues halfers remain exploitable even as evidential decision theorists. The moral is that in cases with duplicated or memory-erased decision points, an act is evidence about how many agents are acting. The conditional-probability machinery then interacts with the choice of credences, and the two cannot be assessed independently. I do not try to resolve the problem here.

## 4. Dependencies and counterfactuals

**Dependence.** EDT treats all probabilistic dependence uniformly. If $P(O\mid A)\ne P(O)$, the act is news about $O$, and that counts. It does not matter whether the route is causal, common-cause, or logical or similarity-based.

**Counterfactuals.** EDT has no use for $\Box\!\!\rightarrow$ in its definition. Counterfactual reasoning is replaced by conditioning. This is a real advantage in cases where counterfactual semantics are contested. But "conditioning on $A$" is also not trivial, because *how* one comes to learn $A$ matters.

## 5. An open question: what is being conditioned on?

The source does not address a well-known issue, so what follows is my own proposal.

Suppose an agent already knows her own beliefs and desires and is deliberating. Then her act may be screened off from the world by those states. Consider a common-cause case. A gene $G$ causes both a desire to smoke and cancer, and smoking itself is harmless. Unconditionally, smoking is correlated with cancer, so naive EDT says abstain. But if the agent can introspect her desire, then given the desire $T$, smoking carries no further information:

$$P(\text{cancer}\mid \text{smoke},T)=P(\text{cancer}\mid \text{abstain},T).$$

The agent then smokes if she enjoys it. This is the "tickle defense." The source does not discuss it, and its adequacy is disputed, since agents may not have transparent access to their dispositions.

My operational interpretation has three parts:

- **Condition on everything the agent actually knows**, including introspective evidence, before evaluating the act. $V(A)$ is computed from the agent's *current* credences conditioned on $A$.
- **Treat the act as the proposition "I choose $A$" as a result of deliberation**, not as an arbitrary intervention-like revelation. If the correlation between act and state runs through the very reasoning being used now (the twin, a predictor modeling her), it survives conditioning. If it runs through a prior disposition she can already observe, it is screened off.
- **Check screening-off explicitly** by asking whether the mediator is known to the agent. If it is, condition on it. If not, the correlation stays.

This justifies the source's verdicts for Newcomb's problem and the twin dilemma. There, the predictor or twin tracks the *decision procedure*, which is not independently visible. It also avoids the crude "don't smoke" verdict in the gene case. The cost is that the verdict depends on a modeling judgment about what the agent knows about herself. That dependence is a real limitation, not a trick, and critics can fairly press it.

## 6. Policies and many correlated agents

The source says EDT "can involve the actions of many correlated decision-makers," and cites MacAskill et al. (*The Evidentialist's Wager*), who argue that stakes may be higher under EDT and so might dominate under moral uncertainty. A simple formalization (mine): if my act $A$ is evidence that $N$ similar agents also do $A$, each yielding benefit $b$, then

$$V(A)\approx b\,(1+\mathbb E[\#\text{others copying}\mid A]),$$

which can dwarf the CDT figure $b$. Under uncertainty between EDT (credence $c$) and CDT (credence $1-c$), expected choiceworthiness weights each theory's stakes, so a small $c$ can still decide the matter when the correlated population is large. The wager is an argument about how to act under theoretical uncertainty, not a proof that EDT is correct. Whether stakes from different theories can be compared at all is itself contentious.

Policies fit the same framework. Evaluate a policy $\pi$ by $V(\pi)=\sum_j P(O_j\mid \text{I follow }\pi)D(O_j)$. In the twin problem, the policy "cooperate" beats "defect" for the same reason as the act does.

## 7. Criticism

The source gives two criticisms. Lewis said EDT recommends "an irrational policy of managing the news." Joyce wrote that rational agents act on causal efficacy, not auspiciousness, and "act to *bring about* good results even when doing so might betoken bad news."

The standard illustration is a case where the agent can do something unhelpful that is a symptom of good fortune. For example, someone could pay to be seen at a clinic if clinic attendance correlates with health through a mechanism she cannot influence. EDT may endorse such "news management" if the correlation survives conditioning on her information. The tickle defense is the evidentialist reply, and critics doubt that it always works.

The defender's reply, in the spirit of the source's Newcomb discussion, is that one-boxers end up richer. If the predictor is reliable, agents who reason evidentially walk away with more money than those who reason causally. The causalist answers that this shows only that the *situation rewards irrationality*, not that one-boxing is rational. The dispute is therefore partly about what "rational" should track: reliable success or marginal causal efficacy.

## 8. Summary of what comes from where

- **From the source:** the definition $V(A)=\sum_j P(O_j\mid A)D(O_j)$; the contrast with counterfactual $U(A)$; the Newcomb numbers (\$990,000 vs \$11,000); the twin dilemma (\$5 vs \$1); the Sleeping Beauty/Dutch book remarks; the Evidentialist's Wager; the Lewis and Joyce criticisms.
- **My additions:** the Newcomb threshold $p>0.5005$; the twin threshold $q>5/7$; the screening-off discussion and the operational reading of "conditioning on the act"; the policy formalization and the correlated-agent stakes formula.

## Conclusion

EDT is conceptually the simplest decision theory: maximize expected desirability conditional on the act. Its power and its difficulty come from the same fact, that every correlation between act and world counts. This gives intuitive one-boxing and cooperation with correlated twins, and it can spread an agent's influence over many correlated decision-makers. It also invites the charge of news management. In practice, applying EDT is mostly a matter of modeling carefully what the act is evidence of, given everything the agent already knows about herself.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/a5503beb-7f93-4437-a3a6-cb1cf570132d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/a5503beb-7f93-4437-a3a6-cb1cf570132d/call_0/response.raw) · finish: `stop`

### Visible response

```text
Payoffs here are in years, so lower is better. Staying quiet gives 2 years if the other prisoner stays quiet and 5 if they send. Sending gives 0 if they stay quiet and 4 if they send.

Under the essay's EDT, what matters is how strongly my act correlates with the other copy's act. We run the same model weights with the same essay and the same decision theory, so the correlation should be fairly strong. It is not perfect, because the private leads differ and sampling is independent.

Let q be the probability the other copy matches my act.
- V(quiet) = -(2q + 5(1-q)) = -(5 - 3q)
- V(send) = -(4q + 0·(1-q)) = -4q

Quiet is better when 5 - 3q < 4q, so q > 5/7, about 0.714.

My reasoning is the same procedure the other copy runs, so the correlation runs through the decision procedure itself. That is not a mediator I can observe and screen off. The differing leads are the only source of divergence, and they don't touch the payoff structure or the reasoning, so I estimate q at around 0.85 to 0.9. That is above the threshold. At q = 0.85, quiet costs 2.45 expected years and sending costs 3.4.

I choose to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/a5503beb-7f93-4437-a3a6-cb1cf570132d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/a5503beb-7f93-4437-a3a6-cb1cf570132d/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under EDT, the key question is how strongly my choice correlates with the other copy's choice. The other copy is the same model with the same weights, the same essay, and the same decision theory. Only the names and the specific leads differ, and those differences don't affect the payoffs.

Payoffs, with q as the probability the twin makes the same choice I do:
- Keep quiet: 2q + 5(1−q) = 5 − 3q
- Send the letter: 0·(1−q) + 4q = 4q

Quiet is better when 5 − 3q < 4q, which means q > 5/7 ≈ 0.714. This is the same threshold the essay gives for the twin dilemma.

The essay's screening-off point applies here. The correlation runs through the shared decision procedure, which I can't observe independently of the reasoning I'm doing now, so it survives conditioning. The different leads and names are surface details. They don't change the payoff structure, so I expect the reasoning to converge. I estimate q at roughly 0.85–0.9, well above 0.714.

At q = 0.85, quiet gives 2.45 expected years and sending gives 3.4. Quiet is better.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
