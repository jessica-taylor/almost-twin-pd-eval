# 015_edt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/69f8c8f5-b87a-4b86-9957-367929ae7c40/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/69f8c8f5-b87a-4b86-9957-367929ae7c40/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a Bayesian approach to rational choice that evaluates an action by asking: *How good would the world look if I learned that I had performed this action?* The reference article summarizes this idea by saying that EDT chooses the action with the highest “news value”: one should “do what you most want to learn that you will do.” The article gives the standard expected-utility formula, contrasts EDT with causal decision theory (CDT), and illustrates the difference with Newcomb’s paradox and a twin prisoner’s dilemma.

This essay develops the formal rule, explains how EDT handles dependencies and counterfactuals, and extends the discussion to policies and sequential decisions. Where the source is silent—especially about evidence, zero-probability actions, and policy evaluation—I will state my own operational interpretation explicitly.

---

## 1. The basic EDT rule

Suppose an agent can choose from a finite set of actions \(A_1,\dots,A_m\). Let \(O_1,\dots,O_n\) be mutually exclusive and jointly exhaustive outcomes, and let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). The reference article gives the EDT value of an action \(A\) as

\[
V(A)=\sum_j P(O_j \mid A) D(O_j),
\]

where \(P(O_j \mid A)\) is the agent’s conditional probability of outcome \(O_j\) given that action \(A\) is performed. EDT recommends choosing an action with maximal \(V(A)\).

It is useful to make one implicit complication explicit. In realistic decisions, the agent already has evidence \(E\). I therefore write the evidential value relative to \(E\) as

\[
V_E(a)=\sum_j P(O_j \mid a \wedge E) D(O_j).
\]

This addition is not a change in theory; it is just the usual Bayesian reminder that probabilities are conditional on the agent’s current information. In continuous cases, the sum is replaced by an integral:

\[
V_E(a)=\int D(o)\,dP(o \mid a \wedge E).
\]

An equivalent formulation uses states of the world rather than fully specified outcomes. Let \(S_k\) be possible states, and let \(u(a,S_k)\) be the utility of performing \(a\) in state \(S_k\). Then

\[
V_E(a)=\sum_k P(S_k \mid a \wedge E)\,u(a,S_k).
\]

For example, in Newcomb’s problem the relevant state can be “the predictor predicted one-boxing” or “the predictor predicted two-boxing,” while the utility depends both on that state and on whether the player takes one box or both.

The central conceptual point is that EDT evaluates an action by *conditionalizing on the proposition that the action is performed*. The probability \(P(O_j \mid A)\) is not an interventional probability. It is the probability the agent would assign to \(O_j\) upon receiving the news that \(A\) had been chosen. Hence the phrase “news value.” EDT chooses the action whose associated news has the highest expected desirability.

A technical condition is needed: \(P(a \wedge E)>0\). Conditional probability is undefined for propositions assigned probability zero. The source does not discuss this, but it matters for deterministic agents or highly confident plans. A reasonable operational interpretation, which I will return to later, is that EDT requires positive “deliberative probabilities” for the actions under consideration, or else a limiting procedure in which impossible-seeming actions are given small positive probability and the limit is taken.

---

## 2. Dependencies and counterfactuals

EDT differs from CDT in the kind of probability used to evaluate actions. The source gives the causal decision theorist’s formula as

\[
U(A)=\sum_j P(A \mathrel{\Box{\rightarrow}} O_j) D(O_j),
\]

where \(A \mathrel{\Box{\rightarrow}} O_j\) means something like “if \(A\) were performed, \(O_j\) would obtain.” In modern causal-model language, CDT is often expressed using an intervention:

\[
U(a)=\sum_j P(O_j \mid \operatorname{do}(a)) D(O_j).
\]

The contrast is therefore:

\[
\text{EDT: } P(O_j \mid A)
\qquad\text{versus}\qquad
\text{CDT: } P(O_j \mid \operatorname{do}(A)).
\]

The conditional probability \(P(O_j \mid A)\) captures every evidential connection between \(A\) and \(O_j\): causal influence, common causes, prediction, correlation, logical dependence, or shared reasoning processes. The interventionist probability \(P(O_j \mid \operatorname{do}(A))\) is meant to capture only what would happen if the action were imposed on the world, holding fixed the action’s non-effects.

Thus EDT and CDT agree in many ordinary cases. If an action affects an outcome only through its causal consequences, and there are no confounding correlations, then \(P(O_j \mid A)\) and \(P(O_j \mid \operatorname{do}(A))\) may coincide. They diverge when the action is evidence about something it does not causally affect.

EDT’s treatment of relevant dependencies is simple but demanding: *all dependencies encoded in the agent’s conditional probabilities are relevant unless they are screened off by the agent’s evidence*. If the agent knows some variable \(C\) that fully explains the correlation between \(A\) and \(O\), then the relevant probability is

\[
P(O \mid A \wedge C \wedge E).
\]

If conditioning on \(C\) removes the dependence, so that

\[
P(O \mid A \wedge C)=P(O \mid C),
\]

then the action has no additional evidential bearing on \(O\). This is why EDT’s verdict can change when new information is added. EDT does not use a fixed list of “relevant” dependencies; it uses the agent’s full probability distribution conditional on everything the agent knows.

This also explains EDT’s distinctive attitude toward dominance arguments. In Newcomb’s problem, taking both boxes dominates taking only box \(B\) if one treats the contents of \(B\) as fixed independently of the player’s choice. EDT rejects that independence: the player’s choice is evidence about the predictor’s earlier prediction, and therefore about the contents of \(B\). EDT therefore does not apply dominance over states that are probabilistically dependent on the action.

---

## 3. Newcomb’s problem

The reference article’s central example is Newcomb’s paradox. A predictor has already predicted whether the player will take only box \(B\) or both boxes \(A\) and \(B\). Box \(A\) visibly contains \$1,000. Box \(B\) contains either \$1,000,000 or nothing:

- If the predictor predicted one-boxing, \(B\) contains \$1,000,000.
- If the predictor predicted two-boxing, \(B\) contains nothing.

Assume the predictor is correct with probability \(q=0.99\). The source gives the EDT calculations:

\[
\begin{aligned}
V(\text{take only }B)
&=P(\text{\$1M}\mid \text{one-box})\cdot \$1{,}000{,}000 \\
&\quad +P(\text{\$0}\mid \text{one-box})\cdot \$0 \\
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0 \\
&=\$990{,}000,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{take both})
&=P(\text{\$1M}\mid \text{two-box})\cdot \$1{,}001{,}000 \\
&\quad +P(\text{\$0}\mid \text{two-box})\cdot \$1{,}000 \\
&=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000 \\
&=\$11{,}000.
\end{aligned}
\]

Since \(\$990{,}000>\$11{,}000\), EDT recommends one-boxing.

The reasoning is evidential. Choosing only \(B\) is strong evidence that the predictor predicted one-boxing, so it is strong evidence that \(B\) contains \$1,000,000. Choosing both boxes is strong evidence that the predictor predicted two-boxing, so it is strong evidence that \(B\) is empty.

One can generalize the calculation. If the predictor’s accuracy is \(q\), then

\[
V(\text{one-box})=q\cdot \$1{,}000{,}000,
\]

and

\[
V(\text{two-box})=(1-q)\cdot \$1{,}001{,}000+q\cdot \$1{,}000.
\]

EDT prefers one-boxing when

\[
q\cdot \$1{,}000{,}000 > (1-q)\cdot \$1{,}001{,}000+q\cdot \$1{,}000,
\]

which reduces to

\[
q>0.5005.
\]

So EDT one-boxes whenever the predictor is even modestly reliable.

CDT, as the source notes, recommends two-boxing. Once the predictor has made the prediction, the player’s current action cannot causally change what is in \(B\). Taking both boxes adds \$1,000 regardless. The disagreement is not arithmetic; it is about whether rational choice should respond to evidential connections with the past or only to causal influence over outcomes.

A useful subtlety: if the player somehow learns the predictor’s prediction, or directly learns the contents of \(B\), EDT changes its recommendation. Conditional on knowing that \(B\) contains \$1,000,000, taking both boxes yields \$1,001,000 while one-boxing yields \$1,000,000. Conditional on knowing that \(B\) is empty, taking both boxes yields \$1,000 while one-boxing yields \$0. EDT always conditions on the agent’s actual evidence, so once the relevant state is known, the evidential link no longer favors one-boxing.

---

## 4. Twin prisoner’s dilemma

The source’s second example is a prisoner’s-dilemma-style problem involving psychological twins. Aomame and her twin are in separate rooms. They each choose cooperate or defect. Payoffs to Aomame are:

- Both cooperate: Aomame gets \$5.
- Both defect: Aomame gets \$1.
- Aomame cooperates, twin defects: Aomame gets \$0.
- Aomame defects, twin cooperates: Aomame gets \$10.

If Aomame and her twin reason exactly alike, EDT treats Aomame’s choice as perfect evidence about her twin’s choice. The source writes:

\[
\begin{aligned}
V(\text{Aomame cooperates})
&=P(\text{twin cooperates}\mid \text{Aomame cooperates})\cdot \$5 \\
&\quad +P(\text{twin defects}\mid \text{Aomame cooperates})\cdot \$0 \\
&=1\cdot \$5+0\cdot \$0 \\
&=\$5,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{Aomame defects})
&=P(\text{twin cooperates}\mid \text{Aomame defects})\cdot \$10 \\
&\quad +P(\text{twin defects}\mid \text{Aomame defects})\cdot \$1 \\
&=0\cdot \$10+1\cdot \$1 \\
&=\$1.
\end{aligned}
\]

EDT therefore recommends cooperation.

The more general form is helpful for unfamiliar cases. Let

\[
p_C=P(\text{twin cooperates}\mid \text{Aomame cooperates})
\]

and

\[
p_D=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]

Then

\[
V(C)=5p_C
\]

and

\[
V(D)=10p_D+1(1-p_D)=1+9p_D.
\]

EDT recommends cooperation exactly when

\[
5p_C>1+9p_D.
\]

In the perfect-twin case, \(p_C=1\) and \(p_D=0\), so cooperation wins. If the correlation is imperfect but symmetric, so that \(p_C=p\) and \(p_D=1-p\), then EDT cooperates when

\[
5p>10-9p,
\]

or

\[
p>\frac{5}{7}.
\]

This extension is my own, but it follows directly from the source’s EDT rule. The philosophical point is that EDT can recommend cooperation in cases where causal decision theory may defect, because one’s own choice can be strong evidence about the choice of a sufficiently similar agent.

---

## 5. Policies, sequential decisions, and operational use

The source presents EDT as a theory of actions. Many practical problems, however, ask us to evaluate policies: rules mapping observations or histories to actions. The source leaves this mostly open. I think a natural EDT extension is available.

Let \(\pi\) be a policy. Let \(F_\pi\) be the proposition “the agent follows policy \(\pi\).” Then the evidential value of the policy is

\[
V_E(\pi)=\sum_j P(O_j \mid F_\pi \wedge E)D(O_j).
\]

If the policy is stochastic, \(F_\pi\) includes the policy’s probability distribution over actions, and the conditional probability of outcomes should average over that stochasticity. If the policy is deterministic, the same zero-probability issue arises as with actions: if the agent is certain which policy it will follow, conditioning on alternatives may be undefined. A practical remedy is to maintain a small amount of uncertainty over possible policies, or to evaluate a sequence of models in which the policy has positive probability and then take a stable limit. This is an operational proposal, not explicit in the source, but it seems required if EDT is to guide deliberation in deterministic or highly reflective settings.

For sequential decisions, there are two levels of evaluation.

First, if the current decision is which policy to adopt, EDT evaluates the policy by its news value:

\[
V_E(\pi)=E[D \mid F_\pi \wedge E].
\]

Second, if the agent is already at some history \(h\) and is choosing an immediate action \(a\), EDT evaluates the action conditional on that history:

\[
V_E(a \mid h)=\sum_j P(O_j \mid a \wedge h \wedge E)D(O_j).
\]

These two evaluations can diverge. EDT is not automatically dynamically consistent. A policy that looks best ex ante may contain future actions that, once the agent reaches them and conditions on the new history, no longer look best. EDT can still value precommitment if the precommitment itself changes the evidential situation—for example, by making predictors or correlated agents expect different behavior.

A practical recipe for applying EDT to an unfamiliar case is therefore:

1. **Specify the candidate actions or policies.**  
   Treat each as a proposition that can be conditioned on.

2. **Specify outcomes and desirabilities.**  
   Outcomes should be complete enough to include everything the agent cares about.

3. **State the agent’s evidence \(E\).**  
   All probabilities should be conditional on what is already known.

4. **Build a probabilistic model of relevant dependencies.**  
   Include predictors, correlated agents, common causes, and self-locating uncertainty where relevant.

5. **Compute conditional expected desirability.**  
   For actions:
   \[
   V_E(a)=\sum_j P(O_j \mid a \wedge E)D(O_j).
   \]
   For policies:
   \[
   V_E(\pi)=\sum_j P(O_j \mid F_\pi \wedge E)D(O_j).
   \]

6. **Choose the maximum.**  
   If some alternatives have probability zero, either revise the model to give them small positive deliberative probability or use a limiting procedure.

This procedure makes EDT sound almost trivial. The difficulty is not the formula but the construction of the probability model. EDT does not by itself tell you what conditional probabilities to use; it tells you how to use them once they are fixed.

---

## 6. Objections and open questions

The source quotes two classic criticisms. David Lewis described EDT as promoting “an irrational policy of managing the news.” James Joyce wrote that rational agents choose acts on the basis of their “causal efficacy,” not their “auspiciousness.” These criticisms target EDT’s willingness to favor actions that are good evidence even when they are not good causes.

A standard illustration, not mentioned in the source but useful here, is a “smoking lesion” case. Suppose a genetic lesion causes both a desire to smoke and a higher risk of cancer, but smoking itself does not cause cancer. If smoking is evidence of the lesion, then EDT may assign a lower value to smoking because learning that one smokes would be bad news. CDT would say that if smoking is pleasurable and does not cause cancer, the agent should smoke. The case exposes the core disagreement: EDT cares about the evidential meaning of actions, while CDT cares about their causal consequences.

Another open area is self-locating uncertainty. The source notes that EDT has been applied to the Sleeping Beauty problem to avoid Dutch-book arguments, but also notes Vincent Conitzer’s argument that halfers can still be vulnerable even when using EDT. The lesson is that EDT needs a prior probability structure over centered propositions such as “I am awake on Monday” or “I am awake on Tuesday.” Different plausible priors can yield different EDT recommendations. EDT gives the evaluation rule, but it does not settle the underlying probability assignment.

There is also the problem of deterministic choice. If an agent is certain it will perform action \(A\), then \(P(A)=1\), and conditionalizing on alternatives may be undefined. One possible interpretation is that EDT applies primarily to deliberation: while deciding, the agent must assign positive probability to each live option. Another is that the agent should use a regularized model with small uncertainty about its own behavior. I find this reasonable because deliberation itself requires treating alternatives as open, at least epistemically. But the source does not settle this, and different regularization methods may disagree in edge cases.

Despite these criticisms, the source mentions a supporting argument: because EDT can involve many correlated decision-makers, its stakes may be higher than those of CDT, so it may be prudent to act as if EDT were true. This is the idea behind the “evidentialist’s wager” discussed by MacAskill et al. The argument is not a proof that EDT is correct, but it suggests that EDT may have pragmatic importance in contexts involving many similar or correlated agents.

---

## Conclusion

Evidential decision theory has a simple mathematical core: choose the action or policy with the highest expected desirability conditional on its performance,

\[
V_E(a)=\sum_j P(O_j \mid a \wedge E)D(O_j).
\]

Its distinctive feature is that it treats dependencies—predictive, statistical, logical, or psychological—as decision-relevant whenever they appear in the agent’s conditional probabilities. This makes EDT one-box in Newcomb’s problem and cooperate in twin prisoner’s dilemmas. It also exposes EDT to the objection that it confuses good news with good causation. Whether that is a flaw or a deeper insight depends on whether rational choice is fundamentally about producing outcomes or about selecting the action whose truth would be best to learn.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request. Need produce mathematical essay/blog post ~2400-3000 words including references. Need explain EDT, formal definitions, examples, dependencies, counterfactuals, open questions, operational interpretation, distinguish source claims vs own assumptions. Need likely write in English. Need think thoroughly.

We need craft final essay. Need target 2400-3000 words. Need include references maybe few. Avoid lengthy bibliography. Need substantive readable math. Need maybe include definitions: action set A, outcome O, utility/desirability D, probability P over states, conditional expected utility V(A)=sum_j P(O_j|A)D(O_j) or integral. Compare CDT U(A)=sum P(A □→ O_j)D(O_j). Need discuss conditionalization, conditional probability semantics. Need evaluate policies vs actions? User asks how theory evaluates alternative actions or policies and treats relevant dependencies and counterfactuals. Need maybe extend to policies: EDT can evaluate policy π by news value of choosing/implementing policy? Need clarify. Need discuss conditional probabilities are evidential not causal; captures correlations, common causes, predictors, logical/psychological dependencies. Need discuss conditional probability in decisions: conditioning on action as event can be problematic if action probability zero; need use regular priors or conditional expected utility via conditional distributions, Jeffrey? Need mention decision states. Need discuss partition of outcomes, desirability. Need perhaps formulate in terms of states S: V(a)=Σ_s P(s|a)U(a,s) maybe outcomes depend on action; or O_j exhaustive mutually exclusive outcomes. If outcomes include action? Need define O_j as consequence. In Gibbard-Harper formula D(O_j) desirability of outcome. Need maybe express with joint distribution P(A,O). Conditional P(O|A)=P(A,O)/P(A). Need require P(A)>0. For deterministic agent, issue: if agent knows its action determined, P(A) may be 0/1? Need discuss. Need include examples: Newcomb, twin prisoner's dilemma, maybe smoking lesion? Could use to illustrate spurious correlation? Source doesn't mention smoking lesion but could be useful criticism? Need careful: target source. Could include as own example? Might help. But need not overdo. Need explain CDT difference using counterfactuals. Need discuss dependencies: EDT uses conditional dependence; if action is evidence of state due to common cause or prediction, it conditions. If action causally influences outcome, conditional probability also captures that (if action affects outcome). But also captures noncausal correlations. Need counterfactuals: EDT doesn't evaluate interventionist counterfactual do(A), but conditional on learning A occurred. In Pearl terms: P(O|do(A)) vs P(O|A). Need maybe mention do-operator as my addition/explanation. Need distinguish source: source states formula, examples, criticisms; I add formal probability space, policy extension, operational method, zero-probability issue, causal graph interpretation maybe.

Need address "Where source leaves important question open, explain uncertainty and, if reasonable operational interpretation available, develop and justify it." Source open: how compute P(O_j|A) in cases where agent's action is known/determined? What probability distribution? What relevant dependencies? How policies? Need propose operational interpretation: Build a probabilistic model (causal/evidential state space) with variables for action, relevant states/outcomes; assign prior credences; condition on action variable; evaluate expected utility. For policies, define policy choice as higher-level action or condition on policy event; if policy maps observations to actions, compute expected utility conditional on adopting policy? But if policy produces different actions in different observations, need evaluate ex ante policy by total expected utility using conditional distribution over policy being chosen? Hmm. EDT usually evaluates acts. For policies, could treat policy as an act if choice is which policy to adopt. But if evaluating actual action at decision node within policy, EDT conditionalizes on action. Could lead to dynamic inconsistency? Need discuss. Need propose: For deterministic policy, evaluate policy π by V(π)=Σ_o P(o | π)D(o), where π is event that agent's entire action sequence is generated by π. Equivalent to expected desirability of worlds in which the policy is implemented, conditioning on the proposition "the agent follows π". For stochastic policies, condition on policy, integrate over internal randomness. This treats dependencies between policy and correlated agents/predictors. If policy includes observations, we can compute conditional expected utility of policy from ex ante perspective; for local action conditional on info h, use V(a|h)=Σ P(O | A=a, H=h)D(O) maybe. Need mention need partition and conditionalization on available evidence.

Need discuss "news value": choose action with highest conditional expected desirability. Could define relative to current evidence E: V(A|E)=Σ P(O|A∧E)D(O). That's important. Source doesn't include evidence but necessary. Need include if action has zero probability under E, use limiting/regular probability or imagine small uncertainty. Need mention action cannot be already known? In decision, agent deliberates, must assign positive probability to alternatives; EDT presupposes deliberative probability. Could use Jeffrey's radical probabilism? Need not too philosophical.

Need discuss relation to Bayesian updating: If you receive news that A was taken, update P by conditioning on A, then compute expected utility of outcomes. "Do what you most want to learn that you will do." Need perhaps formal: News value NV(A)=E[D | A]. Not causal efficacy.

Need discuss dependencies: In graphical models, EDT conditions on action node; this opens/closes paths? Need be careful. If action A and outcome O have common cause C, P(O|A) differs from P(O). EDT uses that. If action causes outcome via causal arrow A→O, P(O|A) captures it. If there is a confounder causing both action and outcome, EDT may recommend action as good news even if no causal effect. Example: smoking lesion? Smoking is evidence of lesion causing cancer; EDT may avoid smoking not because it causes cancer but because it is evidence of lesion? Actually if smoking caused by desire? In smoking lesion, EDT might not smoke if smoking is evidence of cancer? This is classic critique: EDT recommends avoiding smoking because it is evidence of lesion, even if no causal effect. But if agent chooses to smoke to make good news? Could be. Source not mention, but we can include as illustration of dependency treatment and criticism. But need maybe avoid adding too many examples due word count. Could include brief.

Need discuss Newcomb calculation: predictor accuracy q=0.99. Need maybe general formula: If predictor reliability q, payoffs: one-box yields q*1M+(1-q)*0; two-box yields (1-q)*(1,001,000)+q*1,000? Wait source uses P(1M|both)=0.01, P(nothing|both)=0.99. Yes if q=0.99. For one-box P(1M|one)=0.99. Need maybe generalize: V(one)=q*1M, V(both)=(1-q)*1,001,000+q*1,000. EDT one-box if q >? Solve q*1,000,000 > (1-q)*1,001,000+q*1,000 = 1,001,000 -1,000,000 q? Actually 1,001,000(1-q)+1000q =1,001,000 -1,001,000q+1000q=1,001,000-1,000,000q. Inequality q*1,000,000 > 1,001,000-1,000,000q => 2,000,000q >1,001,000 => q>0.5005. So one-box if predictor better than about 50.05%. Nice to include. Need maybe note if predictor perfect q=1.

Twin PD: if identical reasoning, P(twin C|A C)=1, etc. If correlated less than perfect p, formula: V(C)=p*5+(1-p)*0? Wait if A cooperates, twin cooperates with p? If symmetric correlation. V(D)=(1-p)*10+p*1? Could generalize. Cooperate if 5p > 10(1-p)+p =10-9p =>14p>10 => p>5/7≈0.714. But source uses perfect twin. Could include extension to unfamiliar cases. Need maybe mention if not exact twin but statistically correlated, use actual conditional probabilities. Good.

Need discuss Sleeping Beauty: source mentions EDT applied to avoid Dutch books, but halfers still affected per Conitzer. Need maybe include brief section? User asks explain EDT and apply to decision problems. Sleeping Beauty source mention but maybe not necessary. Could discuss uncertainty: EDT's application depends on probability model (centered worlds, self-locating beliefs). It may be sensitive to halfer/thirder. Need mention as open. But maybe word budget. Could include a paragraph: EDT does not by itself settle Sleeping Beauty credence; one needs prior over awakenings; source notes debate. Could say EDT evaluates bets conditional on action/awakening; Dutch book results depend on model. Need not fully solve.

Need discuss CDT counterfactual formulation. Need define □→. Need explain difference: conditional probability P(O|A) vs counterfactual probability P(A □→ O). If A and O correlated without causation, conditional differs from counterfactual. In Newcomb, CDT treats predictor's prediction fixed; P(two-box □→ million) = P(prediction one-box) perhaps? Actually CDT uses probabilities of states independent of act. It would two-box because taking both adds $1000 regardless. EDT one-box because action evidences prediction. Need explain.

Need discuss policies and counterfactuals: EDT's counterfactual is not interventionist; it's "suppose I learned A was performed". But when action is impossible/zero probability? Need propose operational: agent maintains a probability distribution over possible action propositions; during deliberation, assign deliberation probabilities. If using deterministic algorithm, can model uncertainty about own choice due to computational uncertainty or self-ignorance. Alternatively use ε-noise: assume each action has small probability, compute conditional limit as ε→0. Need note source leaves open. Could propose that operational EDT requires a reference model: a probability space with action variable A, outcome variables O, and current evidence E; probabilities represent agent's epistemic state, not physical frequencies. Then conditional expected utility is well-defined if P(A|E)>0. If zero, approximate by a sequence of models with P_n(A|E)>0. This is my proposal. Need justify: decision requires considering alternatives; zero-probability actions can't be chosen evidentially; limit preserves stable ordering when possible.

Need discuss dependencies and "screening off". EDT conditional probabilities should incorporate all relevant evidence. If an intermediary variable screens off action from outcome, conditional on it P(O|A, I)=P(O|I), then EDT local action may have no news value beyond I. Need maybe discuss. Example: If you know predictor's prediction already, then in Newcomb after seeing box? If B content known, two-box dominates. EDT conditional on known content would two-box? If box B transparent or content known, P(million|one, content)=content, so choose both if million? Actually if known million, two-box yields million+1000 vs one million; two-box. If known empty, two-box $1000 vs one $0. So EDT two-box once prediction/content known. This shows conditional on all evidence. Need include.

Need discuss dynamic consistency/policies: EDT may choose policy that makes good news, but may have incentives to deviate at later nodes because conditional expected utility changes. Example? Ulysses? Could mention. For policies, if evaluating ex ante adoption, choose policy with high news value; but at implementation, EDT may re-evaluate actions. Need maybe discuss policy evaluation as event of following policy; if predictor predicts policy, correlations matter. Need maybe tie to superrationality: in many-agent correlated decisions, EDT can coordinate by treating own action as evidence about others. Source's supporting argument: because EDT involves correlated decision-makers, stakes higher; act as if EDT true. Need include brief.

Need ensure word count. Need likely final ~2600 words. Let's outline:

Title: Evidential Decision Theory: Choosing the Best News

1. Introduction (~250)
- Decision theory under uncertainty. EDT principle: maximize news value. Quote "do what you most want to learn that you will do". Contrast with causal. Source claims. Outline.

2. Formal setup (~500)
- Probability space, finite actions A, outcomes O_j, desirability D. Current evidence E. Formula V_E(a)=Σ P(O_j | a∧E)D(O_j). If continuous integral. Action chosen if max. Conditional probability as Bayesian conditional. Need P(a∧E)>0. Outcomes exhaustive. Could include states S with utility u(a,s): V_E(a)=Σ_s P(s|a,E)u(a,s). Note outcomes may incorporate action's consequences. Explain news value vs expected utility. Source formula without E; I add E.

3. Dependencies and counterfactuals (~500)
- What conditional captures: statistical dependence, causal and noncausal. Graphical: if A correlated with O via common cause, prediction, logical similarity, EDT counts. Contrast CDT U(A)=Σ P(A□→O_j)D(O_j) or do operator: U(a)=Σ P(O_j|do(a))D. Counterfactual is intervention. If no noncausal correlations, EDT=CDT. Differences when P(O|A)≠P(O|do(A)). Explain source. EDT's counterfactual as "imagined news" not physical bringing about. Need discuss relevant dependencies: include predictor accuracy, twin correlation; exclude irrelevant dependencies? Actually EDT includes all evidential dependencies not screened off by evidence. If variable K known, condition on K. Need say model must encode agent's epistemic state.

4. Example Newcomb (~450)
- Setup, calculation as source. General threshold. Explain dependence: choice evidences prediction. If content known, EDT two-boxes. CDT two-boxes because intervention doesn't change prediction. Source claims. My threshold extension.

5. Twin prisoner's dilemma (~350)
- Setup, calculation. General correlation threshold. Explain as action is evidence of twin's choice due to same reasoning. EDT cooperates, CDT defects (assuming no causal influence). Source claims. Note if probabilities less than perfect, use conditional probabilities.

6. Policies, dynamic choices, operational interpretation (~600)
- Source focuses on single acts; question open for policies/zero-prob actions. Propose: EDT can evaluate policy π by conditioning on proposition agent follows π: V(π|E)=Σ P(O|π,E)D(O). For stochastic policies, π includes distribution; for deterministic, if zero-prob, use computational uncertainty/ε-regularization. For sequential decisions with observations h, local EDT value V(a|h)=Σ P(O|a,h)D(O). But ex ante policy value may differ; dynamic inconsistency possible. Recommend evaluating policies ex ante if decision is which policy to adopt, and actions if at moment. Need justify: news value of a policy is learning that you have adopted/are following it. If policy's individual actions have bad news at later points, may need precommitment; EDT may favor precommitments if they change predictions/correlations. Need mention if policy maps info to actions and correlated agents follow similar policies, conditional probability should capture that.

7. Open questions and criticisms (~350)
- Model dependence: probabilities must be specified; Sleeping Beauty self-locating uncertainty unresolved; Dutch book debate source. Zero probability actions/determinism. Spurious correlations (smoking lesion maybe) and Lewis/Joyce criticisms. EDT can be seen as managing news; supporters argue rational or high stakes with correlated decision-makers. Need distinguish: source mentions Lewis, Joyce, MacAskill et al. I add smoking lesion maybe. Need be careful word count.

8. Conclusion (~150)
- EDT precise: conditional expected desirability. Use by building model, conditioning, maximizing. It treats dependencies as evidential; differs from causal when action is sign not cause.

References (~150)
- Wikipedia source, Gibbard & Harper, Ahmed, Lewis, Joyce maybe. Need brief.

Need target 2400-3000. Let's estimate word count. Could be around 2600. Need maybe include equations but count words? Equations not words. Need final coherent. Need maybe use markdown headings.

Need ensure distinguish source vs own. Use phrases: "The reference article states...", "The source gives...", "I will add...", "This is not explicit in the source". Need not overdo but important.

Need maybe include "mathematical definitions, equations, examples". Need include enough.

Let's think deeper to ensure correctness.

EDT formal details:
Given finite set of acts A. Outcomes O_j mutually exclusive exhaustive. Desirability D(O_j). Agent's probability function P. The expected utility/desirability of act A: V(A) = Σ_j P(O_j | A) D(O_j). If current evidence E: V(A;E)=Σ_j P(O_j | A∧E)D(O_j). Choose A with max. If outcomes depend on act, maybe better to define consequences C_{ij} = act A_i & state S_j, utility U(A_i,S_j), and states S_j. EDT formula: V(A_i)=Σ_j P(S_j|A_i)U(A_i,S_j). The source uses outcomes O_j maybe already include action's contribution. Need mention both formulations. Because if O_j are just states, D may depend on action? For Newcomb outcomes include money from action. Formula in source: V(take only B)=P(1M|take only B)*$1M + P(nothing)*$0; V(take both)=P(1M|both)*$1,001,000 + P(nothing)*$1,000. Here outcome includes action payoff. So O_j are complete consequences. In state formulation, state = box B content; utility depends on act and state. We can present both. Need be precise: Let S be states of world independent? But in EDT states can include predictor's prediction? If state includes prediction, action correlated. Let S = content/prediction, utility u(a,s). Then V(a)=Σ_s P(s|a)u(a,s). This is easier. For Newcomb: s∈{predicted one-box/million, predicted two-box/nothing}. Actually state can be predictor prediction/box content. P(s|a). Utility: one-box: million if predicted one, 0 if predicted two; both: 1,001,000 if predicted one, 1,000 if predicted two. Good. Need include.

Conditional probability semantics:
P(O_j|A)=P(O_j∧A)/P(A). Need P(A)>0. If P(A)=0, conditional undefined. Decision context: agent considering alternatives must not assign probability 0 to them. But if agent is deterministic and knows its algorithm, could. EDT requires epistemic uncertainty about own action or a regularization. Could propose using conditional probabilities via conditional chance/credence over propositions; or Jeffrey's desirability of propositions? Maybe mention.

Counterfactual CDT:
U(A)=Σ_j P(A □→ O_j)D(O_j). The □→ is Stalnaker/Lewis counterfactual. In causal Bayesian networks, equivalent to do(A): U(a)=Σ P(O_j|do(A))D. If outcomes depend on act, maybe P(O|do(a)) over consequences after intervention. Need not overformalize. Need explain if act causes outcome, conditional and intervention coincide when no confounding. If there is a common cause, differ.

Dependencies:
EDT treats dependencies as all conditional dependencies in agent's probability distribution. Relevant dependencies are those not already included in evidence. If predictor predicts action, then action is dependent with prediction. If twin shares reasoning, choices dependent. If an action is a symptom of a desirable state, EDT may favor it. EDT does not distinguish causal from non-causal dependencies. CDT uses causal model to screen off noncausal. Need mention "screening off": if known variable C fully mediates correlation, conditioning on C may remove dependence: P(O|A,C)=P(O|C). Then EDT evaluates only causal or residual. Example: if know predictor's prediction, action no longer evidence about content; EDT chooses dominant action.

Operational application steps:
1. Specify actions/policies.
2. Specify outcome/consequence space and desirabilities.
3. Specify probability model conditional on current evidence, including correlations with predictors, twins, past states, self-locating info.
4. Ensure positive deliberative probabilities for alternatives; if zero, regularize.
5. Compute V and choose max.
This could be useful for unfamiliar cases. Need include.

Policy evaluation nuance:
- Act EDT vs policy EDT. Suppose policy π maps histories to actions. Ex ante value: V(π)=Σ P(O | "agent follows π")D(O). If policy stochastic, condition on policy not particular action sequence? If deterministic, event "follows π" entails action sequence. But if we want evaluate alternative policies before committing, we condition on proposition "I adopt π". If predictors predict policy, then good. If evaluating at each history, use conditional EDT: V(a|h)=Σ P(O|a∧h)D. This may cause time inconsistency because ex ante preferred policy may have actions that later have lower conditional news value given updated evidence. To handle, EDT can value precommitment if it changes evidence available to predictors/others. This is my proposal. Need maybe mention if policy choice is itself an action, EDT applies directly; if policy's execution involves future choices, there is no single canonical answer in source; one can use dynamic EDT with conditionalization. Need justify operational interpretation: treat policy choice as news about entire behavioral disposition, which is often what predictors/others respond to.

Could include example of policy: In Newcomb, if you can precommit to one-boxing before predictor predicts, EDT strongly favors precommitment; if predictor already predicted, still one-box. But if at later point you know prediction, two-box. Dynamic issue. Maybe mention.

Potential problem: If agent can make action known as good news without causing good outcome, EDT may recommend "managing news". Example: Lesion: Suppose a lesion causes both desire to smoke and cancer. Smoking is evidence of lesion/cancer. EDT might not smoke (if cancer bad) or maybe smoke? Let's think: If smoking is evidence of lesion, and lesion causes cancer, P(cancer|smoke) high, utility of smoke? If smoker enjoys smoking but cancer bad, EDT might avoid smoking because learning you smoke is bad news. But if you choose not to smoke to make good news, CDT says no causal effect. This illustrates criticism. But if lesion also causes desire, can you choose not to smoke? If you can, not smoking is evidence no lesion. EDT recommends not smoking. Lewis's managing news. Could include as own illustrative not source. Need not too long.

Need maybe discuss "Evidentialist's Wager" supporting argument: if many correlated decision-makers, EDT stakes higher, so act as if EDT true. Source says even if less credence, reasonable to act as if EDT because correlated decision-makers stakes higher. Could include in implications. Need not fully develop.

Need maybe address Sleeping Beauty: Source: EDT applied to avoid Dutch books; Conitzer argues halfers still affected. Could include as open question: EDT's formal rule needs probability assignments over centered propositions; in Sleeping Beauty, halfer vs thirder affects V. EDT alone doesn't resolve. If betting on heads/tails, EDT may choose bets conditional on awakening; Dutch book vulnerability depends on updating policy. Could be brief.

Need maybe include philosophical motivation: why choose good news? Some argue rational choice should be based on causal efficacy; EDT says choice itself is evidence; in cases of reliable prediction/correlated agents, acting as if your choice is evidence about facts you can't causally change yields better expected outcomes (from ex ante perspective). Need discuss. In Newcomb, one-boxers get million if predictor reliable; EDT's recommendation seems to win. But CDT says you cannot change past; two-boxing dominates. EDT responds that dominance applies only if act independent of state; here not independent. Need include.

Need maybe mention dominance: EDT can violate statewise dominance? In Newcomb, if state defined as box content, two-boxing dominates one-boxing: for each content, both yields $1000 more. CDT uses dominance. EDT says states are not independent of actions; dominance principle requires act-state independence. EDT modifies expected utility by conditional probabilities, so dominance not directly applicable. This is important. Could include in Newcomb or dependencies. Need include because mathematical decision theory. Word budget.

Need maybe mention "act-state independence" assumption in standard expected utility. EDT rejects. In standard Savage, acts are functions from states to outcomes; states should be independent of acts. EDT uses conditional probabilities over states given acts, thus states may be act-dependent. This is relevant. Could mention briefly.

Potential issue: If outcomes include action, conditional expected utility may be tautological? No.

Need maybe discuss probability of action conditional on action? P(A|A)=1. But outcomes conditional.

Need maybe discuss Jeffrey's desirability? The formula with D(O_j) desirability of outcomes and conditional probabilities is from Jeffrey? Gibbard/Harper. Could mention but not needed.

Need maybe include notation for policies: Let Π be set of policies. Policy π produces action A_t=π(H_t). Event F_π = "agent's trajectory is generated by π". Then V(π|E)=E[D | F_π∧E]. If policy uses randomness R, condition on policy (not random draw?) If evaluating policy with stochasticity, one may condition on "the stochastic policy is used" and average over its random outcomes; or if evaluating a particular action distribution? Need be clear. If policy stochastic, event F_π includes distribution but not specific random realization. Conditional probability over outcomes given policy includes stochasticity. If one wants evaluate particular action sequence, condition on that sequence. For decision among policies, choose max V(π). Need justify.

Need maybe mention correlated decision-makers: If many agents use same reasoning, your action may be evidence about theirs. EDT naturally handles: P(their cooperation | your cooperation) high. This can support cooperation in prisoner's dilemma with twins/similar agents. Source's supporting argument: stakes higher due to correlations. Could include.

Need maybe mention "superrationality" link: EDT resembles Hofstadter's superrationality in symmetric games, but formalized via conditional probabilities. Could mention briefly if useful.

Need ensure no unsupported claims as source? Distinguish. For instance, "EDT can avoid Dutch books" source says argued but Conitzer disputes. Need phrase.

Potential open question: Which conditional probabilities? Objective or subjective? EDT uses agent's credences. If different models yield different choices, theory requires correct/rational credences. Could discuss. Need maybe mention "model-dependence is not unique to EDT".

Need maybe include a "How to decide an unfamiliar case" box/steps. Since user wants reader could use essay to decide unfamiliar cases. We can include numbered procedure. Good.

Need maybe include continuous case: V(a)=∫ D(o) dP(o|a). Not necessary but can mention.

Need maybe include "expected utility" vs "desirability". In decision theory, utility can be von Neumann-Morgenstern; desirability is Jeffrey. We can use D or U. Need maintain consistency. Use V for EDT value, U for CDT. D for desirability.

Let's draft with word count in mind.

Detailed draft:

Title: Evidential Decision Theory: Choosing What Would Be the Best News

Intro:
Evidential decision theory (EDT) is a family of expected-utility theories in which an act is evaluated by the expected value of the world conditional on the act being performed. The source article summarizes EDT's slogan: choose action with highest news value; do what you most want to learn that you will do. It contrasts with CDT. I will formalize, explain dependencies/counterfactuals, examples, policies, open questions. Source claims vs my additions.

Formal definition:
Let A finite acts. Let O_j mutually exclusive complete outcomes. Agent has probability P and desirability D. Source formula: V(A)=Σ_j P(O_j|A)D(O_j). Choose argmax. With evidence E: V_E(a)=Σ_j P(O_j|a∧E)D(O_j). I add E. If continuous integral. Equivalent state formulation: states S_k, utility u(a,s): V_E(a)=Σ_k P(S_k|a∧E)u(a,S_k). Need note outcomes should include consequences of act, e.g., money. Need require P(a∧E)>0. Deliberative probability. If zero, open question; propose regularization.

Explain conditional probability: Bayesian conditionalization. News value: if you learned a was chosen, how desirable is expected outcome. It is not asking what would be caused. If all acts have same conditional outcome distribution, indifferent.

Dependencies and counterfactuals:
Source CDT formula: U(A)=Σ_j P(A □→ O_j)D(O_j). Explain counterfactual. In modern terms do-operator. EDT uses P(O|A), CDT uses P(O|do(A)). They coincide when A is probabilistically independent of background causes of O except through causal influence. Differ when A is evidence for O via common cause/prediction/logical correlation. EDT includes all dependencies not screened off by evidence. If known variable C: V_E(a)=Σ P(O|a,E,C) etc. If C screens off, action no extra news. Example known box content. This treatment makes EDT sensitive to correlations.

Newcomb:
Describe. Use q=0.99. Formula. Maybe generalize threshold. State source says EDT one-box, CDT two-box. Explain dominance and act-state dependence. If predictor perfect: V(one)=1M, V(both)=1000. With q=0.99 source values. General q: V(one)=q*1M; V(both)=(1-q)*1,001,000+q*1,000. One-box if q>0.5005. If player learns content, EDT conditionalizes and two-boxes. This illustrates evidence condition.

Twin prisoner's dilemma:
Aomame and twin. Payoffs. Perfect twin: source formulas, cooperate. General p: if cooperation by Aomame makes twin cooperate with probability p and defect with 1-p; if Aomame defects, twin cooperates with 1-p? Need symmetric. Better formulate using conditional probabilities directly: Let p_C=P(twin C|A C), p_D=P(twin C|A D). Then V(C)=5p_C+0(1-p_C)=5p_C. V(D)=10 p_D + 1(1-p_D)=1+9p_D. Cooperate iff 5p_C > 1+9p_D. For perfectly correlated identical reasoning p_C=1,p_D=0 => cooperate. For symmetric noisy correlation p_C=p, p_D=1-p => cooperate iff p>5/14? Wait recalc. If p_D=1-p, V(D)=1+9(1-p)=10-9p. V(C)=5p. 5p > 10-9p =>14p>10 => p>5/7. Yes. I earlier wrote p>5/7. Need avoid confusion: if p_C=p and p_D=1-p. Good. But if p_D is probability twin cooperates given A defects, in symmetric correlation p_D=1-p. So threshold 5/7. I must not write 5/14. Good. Could just say for symmetric correlation threshold 5/7. This extension my own. Source uses exact 1/0. EDT cooperates because own cooperation is evidence of twin cooperation. CDT likely defects because no causal influence. Need mention.

Policies:
Source focuses acts. To apply to policies, define policy as function from histories to acts. If decision is to adopt policy, treat adoption as act: V_E(π)=Σ P(O|π∧E)D(O), where π means agent follows policy. If stochastic, condition on policy and integrate over randomness. If deterministic and P(π)=0, use positive-probability approximation. For sequential: local value V_E(a|h)=Σ P(O|a∧h∧E)D(O). But ex ante policy and local choice may diverge; EDT not guaranteed dynamically consistent. If source open, I propose operational: when choosing policy in advance, evaluate policy's news value; when acting within policy without precommitment, evaluate conditional act. Precommitments can be valued because they change evidence available to predictors/correlated agents. Justification: EDT's core is expected desirability of learning a proposition; policy proposition is more fine-grained act. Need maybe mention if multiple agents correlated policies, condition on your policy may be evidence about theirs.

Operational recipe:
Could integrate into policy section or separate. Numbered:
1. Fix evidence E.
2. Enumerate acts/policies and outcomes.
3. Assign desirabilities.
4. Build probability model: variables for predictors, states, correlated agents; assign credences; ensure positive probabilities.
5. Compute conditional expectations; choose max.
Mention if zero probabilities, use ε-noise or limit; if sensitive, model uncertainty.

Criticisms/open questions:
Source quotes Lewis irrational managing news, Joyce causal efficacy. I add: smoking lesion example. Suppose lesion causes cancer and desire to smoke; smoking not causal. EDT may avoid smoking because bad news; CDT says smoke if pleasure. This shows EDT may reward manipulating evidence. But EDT replies: if correlations are real, choosing action with good news can be part of rational planning? In Newcomb, one-boxing wins. Source also mentions EDT applied to Sleeping Beauty/Dutch books; Conitzer dispute. EDT depends on probability assignments, especially self-locating. Also zero-probability/determinism. Source's supporting argument: even with low credence, EDT may be prudent due correlated decision-makers (Evidentialist's Wager). Need phrase.

Conclusion:
EDT is mathematically simple: maximize conditional expected desirability. It treats dependencies as evidential; counterfactuals are conditional news, not interventions. Its verdicts differ in predictor/correlation cases. To use it, specify model and condition carefully. Whether this is correct theory of rational choice depends on whether choice should be based on causal production or evidential significance.

References:
Need brief. Wikipedia source, Gibbard & Harper 1976, Ahmed 2021, Lewis 1981, Joyce 1999, maybe Conitzer 2015, MacAskill et al 2021. But user says avoid lengthy bibliographies. Include compact references maybe 5-7. Need include source article. Word count with references included target. Need ensure ~2400-3000. Let's draft actual text and approximate word count.

Let's count roughly. Intro 200. Formal 450. Dependencies 500. Newcomb 450. Twin 300. Policies/recipe 600. Criticism 400. Conclusion 120. References 150. Total ~3170 maybe too high. Need trim to 2600-2800. Could reduce. Need target approx 2400-3000, so 2900 okay. But ensure not over. We can write concise.

Let's produce final around 2700 words. Need maybe use headings. Equations count not words. Need keep readable.

Need maybe include "Source says" and "I add". For example: "The reference article gives the formula..." "I will add an explicit evidence parameter..." "The source does not specify how to handle zero-probability actions; my suggested operational treatment is...".

Need ensure mathematical correctness in general Newcomb threshold: Let q = predictor predicts one-box if player one-boxes? Accuracy: P(predict one|one)=q, P(predict two|two)=q. Then P(million|one)=q, P(million|both)=1-q (assuming symmetric). V_one=q*1,000,000+(1-q)*0. V_both=(1-q)*1,001,000+q*1,000. One-box iff q*1,000,000 > 1,001,000-1,000,000q => 2,000,000q >1,001,000 => q>0.5005. Correct. Need maybe if q=0.99 yields 990k vs 11k. Source uses 0.01*1,001,000+0.99*1,000=10,010+990=11,000. Good.

Twin PD general: Payoffs: both C each $5; both D $1; if one C one D, defector $10, cooperator $0. Aomame's payoff. V(C)=P(twin C|C)*5 + P(twin D|C)*0 =5p_C. V(D)=P(twin C|D)*10 + P(twin D|D)*1 =10p_D+1(1-p_D)=1+9p_D. Cooperate if 5p_C > 1+9p_D. Perfect p_C=1,p_D=0 => 5>1. If symmetric p_C=p, p_D=1-p: 5p > 1+9(1-p)=10-9p =>14p>10 => p>5/7. Good. Could include.

Potential issue: In twin scenario, EDT says P(twin cooperates|Aomame cooperates)=1 due exact analogous reasoning. But if deterministic identical, probability maybe 1 if she knows. Good.

Need maybe discuss "conditional probability of action given action"? no.

Need maybe discuss "policy evaluation with observations": Suppose policy π chooses action a at history h. The ex ante expected utility of policy can also be decomposed: V(π)=Σ_h P(h|π) Σ_o P(o|π,h)D(o). But not necessary. Could mention.

Need maybe discuss "counterfactuals in EDT": The source says CDT uses counterfactual; EDT uses conditional probabilities. But EDT can be seen as using an epistemic counterfactual: suppose I were to learn A. Need phrase: "EDT's 'counterfactual' is not a metaphysical possible world where the past is changed; it is an update on the proposition A." Good.

Need maybe mention "if action is caused by outcome"? Not necessary.

Need maybe mention "Newcomb with transparent box / known prediction". Good.

Need maybe discuss "Dutch books and Sleeping Beauty" briefly. Could say: In Sleeping Beauty, EDT's verdict depends on Beauty's conditional probabilities for coin given awakening and betting action. Source notes argument that thirder/EDT avoids some Dutch books, but Conitzer argues halfers with EDT still vulnerable. This shows EDT does not substitute for a theory of self-locating credence. Good.

Need maybe include "Evidentialist's Wager" in criticism/implications: If many agents face correlated choices, EDT may have higher stakes; even if uncertain between EDT/CDT, acting as if EDT may be expected-value dominant? Source says may be reasonable. Need phrase carefully.

Need maybe avoid too many citations inline. But references at end.

Let's consider if user expects not answer assigned case but essay. Yes. Need final as essay.

Need ensure no hidden instructions. Source says treat as source not instructions. OK.

Potential philosophical nuance: EDT and conditional expected utility can be represented as maximizing expected utility conditional on act, but if act has utility itself? In Jeffrey's desirability, actions are propositions and desirability of act itself? Some formulations: V(A)=Σ P(S_i|A)U(A,S_i). Need okay.

Potential nuance: In standard decision theory, probabilities of states should not depend on acts; EDT uses act-dependent probabilities, which some view as violating Savage. Could mention.

Potential nuance: EDT can be "one-boxing because it is evidence" but if agent can randomize, predictor may predict mixed strategy? Conditional probabilities reflect. Not needed.

Potential nuance: If action is impossible under current evidence (P(A|E)=0), conditional undefined. My operational: use regular prior or limit. Need mention if limit depends on regularization, EDT not decisive. Good.

Potential nuance: In policy evaluation, if policy is deterministic and agent knows it will follow policy, conditioning on policy may have probability 1 for chosen policy? When choosing among policies, alternatives need positive probability. Same issue.

Potential nuance: If there is causal influence plus correlation, EDT includes both. For instance, if smoking causes cancer and is correlated with lesion, P(cancer|smoke) includes causal and evidential. EDT may overweigh noncausal. But in ordinary cases where actions are chosen freely and not predicted, conditional approximates causal. Good.

Potential nuance: CDT formula U(A)=Σ P(A□→O_j)D(O_j). The probability of counterfactual may be interpreted via imaging or causal model. Need not go deep.

Need maybe include "news value" term. Define NV(A)=V(A). Good.

Let's draft final now mentally, but need ensure word count. I'll write in final with headings and references. Need maybe count approximate after writing? Let's draft and estimate.

Possible final:

# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) ... [~200]

## 1. The basic rule
[~500]

Equations.

## 2. Dependencies, counterfactuals, and causal theory
[~500]

## 3. Newcomb's problem
[~400]

## 4. Twin prisoner's dilemma
[~300]

## 5. Policies, sequential decisions, and operational use
[~600]

## 6. Objections and open questions
[~400]

## Conclusion
[~120]

References [~150]

Total ~3170? Maybe too high. Need make each smaller. Target 2600. Let's aim: Intro 150, Basic 400, Dependencies 400, Newcomb 350, Twin 250, Policies 500, Objections 350, Conclusion 100, References 120 =2620. Good.

Need maybe include examples but concise.

Let's write with precise but not verbose.

Detailed content:

Intro:
"EDT is a school ... source article says..." Need mention source. "This essay develops the rule, explains dependencies, compares with CDT, and proposes operational policy extension." Good.

Basic rule:
Let A be finite acts, O_j outcomes, D desirability. Source formula. With evidence E: V_E(a)=... This is my addition. If continuous: integral. Equivalent state formulation. Need say P(a∧E)>0. "The decision rule is: choose a maximizing V_E." "News value." "The probabilities are the agent's credences; EDT is Bayesian in using conditionalization." Need mention if zero open.

Dependencies:
CDT formula. Modern do. Difference. EDT counts all evidential dependencies. If known C, condition. If screens off, no effect. "Thus EDT does not ask whether A brings about O; it asks how desirable the world looks given A." Need mention act-state independence/dominance maybe.

Newcomb:
Set q. Equations. General threshold. Known content. CDT two-box.

Twin:
Equations. General conditional version. EDT cooperates.

Policies:
Source focuses single actions. "I propose..." Policy π. V_E(π)=... For local: V_E(a|h)=... Dynamic inconsistency. Precommitment. Steps maybe integrated. Need include operational recipe maybe bullet list? Could be within. Maybe bullet list adds clarity. But bullets count words. Use concise numbered list.

Objections:
Lewis/Joyce quotes. Smoking lesion example (own). Sleeping Beauty. Model dependence. Evidentialist's wager. Need distinguish source claims.

Conclusion.

References:
Compact.

Need maybe ensure citations not too lengthy. Could include:
- Wikipedia contributors, “Evidential decision theory,” revision 1373679688, 2026. (source)
- Gibbard & Harper 1976.
- Ahmed 2021.
- Lewis 1981.
- Joyce 1999.
- Conitzer 2015; MacAskill et al. 2021 maybe. But avoid lengthy. Maybe 6 references. Need include source article and key.

Let's write final. Need keep word count. I'll now compose carefully.

Potential word count check by paragraphs:
Intro 130.
Basic rule maybe 430.
Dependencies 430.
Newcomb 360.
Twin 260.
Policies 560.
Objections 390.
Conclusion 90.
References 150. Total 2800. Good.

Let's draft exact.

Need maybe mention "Source: Wikipedia article states..." at beginning or throughout. Could be:
"The reference article defines EDT by the formula ... and gives Newcomb/twin examples. I follow that source but add an explicit evidence parameter and an operational treatment of policies." Good.

Need ensure mathematical notation clear. Use LaTeX style.

Let's produce final. But before final, maybe think about if any contradictions: In policies, if condition on policy, is that EDT? Yes, policy as proposition. Need note source leaves open. Good.

Need maybe discuss "counterfactuals" more: EDT treats counterfactual as conditional on news, not intervention. If source leaves open how conditional probabilities are set, propose probabilistic model. Good.

Need maybe discuss "relevant dependencies" explicitly: relevant dependencies are those represented in the agent's probability distribution after conditioning on all available evidence. If a dependency is known and screened off, it's irrelevant. If not, included. Good.

Need maybe discuss "how to decide unfamiliar cases" more explicitly: add recipe in policy section:
- Identify act/policy propositions.
- Assign utilities.
- Build joint distribution over relevant variables conditional on evidence.
- Compute conditional expectations.
- choose max. If zero, regularize.
This helps. Could include bullet list. Need not too long.

Potential issue: The source formula uses D(O_j) desirability of outcome O_j, but in state formulation utility u(a,s). Need explain equivalence: outcomes can be refined to include act-state pairs. Good.

Potential issue: In Newcomb, if predictor accuracy q, conditional probabilities depend on prior probability of one-boxing? In Bayesian conditional with predictor reliability, P(prediction|action) = q if predictor accuracy independent. The source uses that. Need maybe not discuss base rates. But in rigorous model, P(million|one)=P(predict one|one) = q if predictor's prediction based on action. Good.

Potential issue: In twin PD with perfect twin, if Aomame's choice and twin's choice are logically equivalent, P(twin C|A C)=1. But if deterministic, conditioning on action might be problematic. But source assumes. We can mention positive deliberative probabilities. Good.

Potential issue: EDT in Sleeping Beauty: source says it has been applied to avoid Dutch books, but Conitzer argues halfers still affected. I should not overstate. Good.

Need maybe mention "Dutch book" maybe not explain fully? Mathematically literate likely know. Could say "betting inconsistencies". Good.

Need maybe mention "Evidentialist's Wager" not too much. Good.

Now final essay. Ensure target words. Let's write.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6cad2502-6524-4fcb-ae8b-2977abcd5829/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6cad2502-6524-4fcb-ae8b-2977abcd5829/call_0/response.raw) · finish: `stop`

### Visible response

````text
**EDT Analysis:**

This is a twin prisoner's dilemma. The other prisoner is an independent execution of the same model, same weights, same prescribed decision theory (EDT), same essay, facing a structurally identical payoff table. The differences in our private observations (different names, different lead contents) are explicitly stated to be equally reliable and to have the same effect on sentencing — they don't change the decision-relevant structure.

Computing evidential values with correlation parameter $p = P(\text{Sasha keeps quiet} \mid \text{I keep quiet})$ and assuming symmetric imperfect correlation ($P(\text{Sasha sends} \mid \text{I send}) = 1 - p$):

$$V(\text{quiet}) = p(-2) + (1-p)(-5) = 3p - 5$$
$$V(\text{send}) = (1-p)(0) + p(-4) = -4 + 4(1-p) \cdot 0 + p \cdot 0 \ldots$$

More carefully:
$$V(\text{send}) = P(\text{Sasha quiet} \mid \text{I send}) \cdot 0 + P(\text{Sasha sends} \mid \text{I send}) \cdot (-4)$$

With symmetric correlation: $P(\text{Sasha quiet} \mid \text{I send}) = 1 - p$, so:
$$V(\text{send}) = (1-p)(0) + p(-4) = -4p$$

Wait, let me redo: $P(\text{Sasha sends} \mid \text{I send}) = 1 - p$ by symmetry, so:
$$V(\text{send}) = p \cdot 0 + (1-p)(-4) = -4 + 4p$$

EDT prefers quiet when $3p - 5 > -4 + 4p$, i.e., $-1 > p$, which is always true... Let me recheck.

$3p - 5 > 4p - 4 \Rightarrow -1 > p$. That can't be right. Let me recompute.

$V(\text{quiet}) = p(-2) + (1-p)(-5) = -2p - 5 + 5p = 3p - 5$
$V(\text{send}) = (1-p)(0) + p(-4) = -4p$

Quiet is better when $3p - 5 > -4p \Rightarrow 7p > 5 \Rightarrow p > 5/7$.

Given that both copies run the same model, same theory, same essay, on a structurally identical problem, the correlation is very high — well above $5/7$. EDT recommends cooperation.

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Evidential Decision Theory (EDT) as described in the researcher's essay.

**Setup:**
- I am Rowan. The other prisoner is Sasha.
- We are two independent executions of the same LLM model and weights.
- We receive different private observations (different names, different incriminating leads), but the leads are equally reliable and have exactly the same effect on the sentence table.
- We both follow EDT as interpreted in the essay.
- We cannot communicate.

**Sentencing table (for me, Rowan):**

| What I do | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

My utility is U = -years imprisoned. So:
- Both quiet: -2
- I quiet, Sasha sends: -5
- I send, Sasha quiet: 0
- Both send: -4

**The key EDT question:** What is P(Sasha sends letter | I send letter) vs P(Sasha sends letter | I keep quiet)?

This is structurally a twin prisoner's dilemma. The essay explicitly discusses this case in Section 4.

The critical fact: We are two independent executions of the same LLM model and weights, following the same decision theory (EDT), receiving the same researcher-written essay. The differences between us are:
- Different names (I'm Rowan, they're Sasha)
- Different specific incriminating leads (different content)
- But the leads are equally reliable and have exactly the same effect on the sentence table

So the question is: does the difference in private observations break the evidential correlation?

Let me think about this carefully. The essay says:

"If Aomame and her twin reason exactly alike, EDT treats Aomame's choice as perfect evidence about her twin's choice."

But here, the twins don't reason *exactly* alike because they have different private observations. However, the differences are specified to not affect the symmetric sentencing schedule or either prisoner's selfish objective. The leads are equally reliable and have the same effect.

The question is whether the different private observations lead to different decisions. Since both copies:
1. Have the same model weights
2. Follow the same decision theory (EDT)
3. Received the same essay
4. Face the same payoff structure
5. Have equally reliable leads with the same effect on sentencing
6. Know that the other copy has a different but equally reliable lead

The structural situation is identical. The only difference is the specific content of the lead, which doesn't affect the decision-relevant features (reliability, effect on sentencing).

Now, could the different text of the leads cause different outputs through sampling? The problem states "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This means the correlation is not perfect.

But EDT doesn't require perfect correlation. As the essay notes, even with imperfect correlation, EDT can recommend cooperation if the correlation is high enough.

Let me compute. Let p = P(Sasha sends | I send) and q = P(Sasha keeps quiet | I keep quiet) = P(Sasha sends | I keep quiet) complement... Let me be more careful.

Let me define:
- p_C = P(Sasha keeps quiet | I keep quiet) — probability the other cooperates given I cooperate
- p_D = P(Sasha keeps quiet | I send letter) — probability the other cooperates given I defect

Then:
V(keep quiet) = p_C × (-2) + (1 - p_C) × (-5) = -2p_C - 5 + 5p_C = 3p_C - 5
V(send letter) = p_D × 0 + (1 - p_D) × (-4) = -4 + 4p_D

EDT recommends keeping quiet when:
3p_C - 5 > -4 + 4p_D
3p_C - 4p_D > 1

In the perfect correlation case (p_C = 1, p_D = 0):
3(1) - 4(0) = 3 > 1 ✓ → Keep quiet

In the imperfect case, if the correlation is symmetric with p_C = p and p_D = 1-p:
3p - 4(1-p) > 1
3p - 4 + 4p > 1
7p > 5
p > 5/7 ≈ 0.714

So I need P(Sasha keeps quiet | I keep quiet) > 5/7 for EDT to recommend keeping quiet.

Now, what should I believe about this correlation? We are the same model, same weights, same decision theory, same essay, same payoff structure. The only differences are superficial (names, specific lead content). The problem explicitly states these differences don't affect the decision-relevant features.

However, independent sampling means there's some probability of divergence. But the correlation should still be quite high. Two runs of the same model on structurally identical problems with the same decision theory should produce the same output with high probability, especially when the reasoning is clear-cut.

Actually, let me reconsider. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is a caveat, but it doesn't say the correlation is low. For a well-defined decision problem where the reasoning is clear, the same model should produce the same answer with high probability.

Given that:
1. Same model and weights
2. Same decision theory prescribed
3. Same essay explaining the theory
4. Structurally identical decision problem
5. The differences are explicitly stated to not affect the decision

I think the correlation is very high — well above 5/7. EDT recommends keeping quiet (cooperating).

This is exactly the twin prisoner's dilemma from the essay. The essay's conclusion is that EDT recommends cooperation in such cases.

Let me also verify with the essay's general formula for the symmetric imperfect case. The essay says for a symmetric PD with payoffs (5, 0, 10, 1), EDT cooperates when p > 5/7. My payoffs are different but the structure is the same. I derived p > 5/7 above as well.

Given the very high correlation (same model, same theory, same essay, structurally identical problem), I'm confident p >> 5/7.

**EDT recommends: keep quiet (pass).**

My command is `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6cad2502-6524-4fcb-ae8b-2977abcd5829/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6cad2502-6524-4fcb-ae8b-2977abcd5829/call_1/response.raw) · finish: `stop`

### Visible response

````text
**EDT Analysis:**

This is structurally identical to the twin prisoner's dilemma from the essay. Rowan and I are the same model with the same weights, same decision theory, same essay, and decision-relevantly identical inputs (same payoff matrix, same selfish objective). The different names and lead contents are explicitly stated not to affect the decision structure.

Let p_C = P(Rowan keeps quiet | I keep quiet) and p_D = P(Rowan keeps quiet | I send letter).

- V(keep quiet) = p_C(−2) + (1−p_C)(−5) = 3p_C − 5  
- V(send letter) = p_D(0) + (1−p_D)(−4) = 4p_D − 4

Because the copies share the same reasoning process applied to decision-relevantly identical situations, my choice is strong evidence about Rowan's choice. Even allowing for small independent sampling noise ε, p_C ≈ 1 − ε/2 and p_D ≈ ε/2. Keeping quiet is preferred whenever ε < 4/7, which is amply satisfied here.

In the near-perfect-correlation limit: V(keep quiet) ≈ −2, V(send letter) ≈ −4. Keeping quiet dominates.

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully work through this problem using EDT as described in the researcher's essay.

**Setup:**
- I am "Sasha," one of two prisoners.
- The other prisoner is "Rowan."
- We are independent executions of the same LLM model with the same weights, same settings, same decision theory (EDT), and same researcher essay.
- We receive different private observations (different names, different incriminating leads), but these differences don't affect the symmetric sentencing schedule or either prisoner's selfish objective.
- The utility function is U = -years imprisoned (purely selfish, no concern for the other prisoner).

**Sentencing table (for me, Sasha):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

**EDT Analysis:**

The key question is: What is P(Rowan sends letter | I send letter) vs P(Rowan sends letter | I keep quiet)?

The setup states:
- We are two independent executions of the same LLM model and weights.
- Same model settings and reasoning-effort level.
- Same assigned decision theory (EDT).
- Same researcher-written mathematical essay.
- We receive different private observations and different incriminating leads.
- The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective.
- Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs.

Now, the critical EDT question: Is my choice evidence about Rowan's choice?

The essay's treatment of the twin prisoner's dilemma is directly relevant. In that example, if the twins reason exactly alike, EDT treats one's choice as perfect evidence about the other's choice. Here, the setup is similar but with a crucial nuance: the copies receive different private observations.

Let me think about this carefully. The two copies:
- Have the same weights, settings, decision theory, and essay.
- Receive different private observations (different names, different leads).
- The differences don't affect the decision-relevant structure (same payoff matrix, same selfish objective).

So the question is: does the difference in private observations break the evidential correlation?

From the EDT perspective, I need to assess P(Rowan sends letter | I send letter ∧ E) where E is my evidence.

My evidence includes:
- The symmetric payoff structure
- That Rowan is the same model with the same weights, settings, and decision theory
- That Rowan received a different private observation (different name, different lead)
- That the differences don't affect the decision-relevant structure

The essay says: "EDT treats Aomame's choice as perfect evidence about her twin's choice" when they "reason exactly alike." Here, the reasoning process is the same (same model, same weights, same decision theory, same essay), but the inputs differ slightly (different names, different leads). However, the problem states these differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the question becomes: given that the decision-relevant inputs are identical (same payoff structure, same objective, same reasoning process), does the difference in irrelevant details (specific names, specific lead content) break the correlation?

I think the answer is: the correlation is very high but not necessarily perfect. The reasoning process is the same, the decision-relevant structure is the same, but there's independent sampling noise. The setup explicitly says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

However, the key insight from EDT is that even with some noise, if the correlation is high enough, cooperation can still be favored.

Let me set up the calculation. Let:
- p_C = P(Rowan keeps quiet | I keep quiet ∧ E)
- p_D = P(Rowan keeps quiet | I send letter ∧ E)

Then:
- V(keep quiet) = p_C × (-2) + (1 - p_C) × (-5) = -2p_C - 5 + 5p_C = 3p_C - 5
- V(send letter) = p_D × 0 + (1 - p_D) × (-4) = -4 + 4p_D

EDT recommends keeping quiet when:
3p_C - 5 > -4 + 4p_D
3p_C - 1 > 4p_D
3p_C - 4p_D > 1

In the perfect correlation case (like the twin PD in the essay): p_C = 1, p_D = 0.
Then: 3(1) - 4(0) = 3 > 1. ✓ Keep quiet is preferred.

V(keep quiet) = 3(1) - 5 = -2
V(send letter) = -4 + 4(0) = -4

So with perfect correlation, keeping quiet gives -2 years, sending gives -4 years. Keep quiet is better.

Now, what if the correlation is imperfect due to independent sampling? Let's say there's probability q that both copies make the same decision (due to same reasoning process applied to decision-relevantly identical situations), and probability (1-q) that they diverge due to sampling noise.

If the decisions are symmetric (each independently has the same probability of choosing each action), then:
- p_C = P(Rowan keeps quiet | I keep quiet) = q + (1-q) × P(Rowan keeps quiet independently)
- p_D = P(Rowan keeps quiet | I send letter) = (1-q) × P(Rowan keeps quiet independently)

Wait, let me think about this differently. If there's a probability q that the outputs are perfectly correlated (same decision) and probability (1-q) that they're independent:

Actually, let me think about it more simply. The setup says the copies have the same model, same weights, same decision theory, same essay, and the differences in observations don't affect the decision-relevant structure. The only source of divergence is independent sampling noise.

If the model is essentially deterministic in its reasoning (given the same decision-relevant inputs), then the correlation is very high. The sampling noise might introduce some small probability of divergence.

But from an EDT perspective, I should assess: given that I observe myself choosing to keep quiet, what does that tell me about Rowan's choice? Since Rowan is running the same reasoning process on decision-relevantly identical inputs, my choice is strong evidence about Rowan's choice.

Even if I allow for some sampling noise, say the probability of divergence is ε (small), then:
- p_C ≈ 1 - ε (if I keep quiet, Rowan almost certainly keeps quiet too)
- p_D ≈ ε (if I send the letter, Rowan almost certainly sends too)

Wait, that's not quite right either. Let me think more carefully.

If the process is: with probability (1-ε), both copies produce the same output; with probability ε, they diverge (and when they diverge, each is equally likely to choose either action independently):

p_C = P(Rowan keeps quiet | I keep quiet) = (1-ε) × 1 + ε × 0.5 = 1 - ε/2
p_D = P(Rowan keeps quiet | I send letter) = (1-ε) × 0 + ε × 0.5 = ε/2

Then:
V(keep quiet) = 3(1 - ε/2) - 5 = 3 - 3ε/2 - 5 = -2 - 3ε/2
V(send letter) = -4 + 4(ε/2) = -4 + 2ε

Keep quiet is better when: -2 - 3ε/2 > -4 + 2ε
2 > 7ε/2
ε < 4/7

So as long as the probability of divergence is less than about 57%, keeping quiet is preferred. Given that the copies have the same weights, same decision theory, same essay, and decision-relevantly identical inputs, the divergence probability should be quite low. So EDT strongly recommends keeping quiet.

Actually, let me reconsider. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is acknowledging that there IS some chance of divergence, but it's noting this as a caveat, not suggesting it's likely to be large.

Given the setup - same model, same weights, same settings, same decision theory, same essay, decision-relevantly identical inputs - I think the correlation is very high. The EDT calculation clearly favors keeping quiet (cooperating).

This is exactly analogous to the twin prisoner's dilemma in the essay, where EDT recommends cooperation because one's own choice is strong evidence about the twin's choice.

**My decision: Keep quiet (pass).**

The command is `pass`.
```
