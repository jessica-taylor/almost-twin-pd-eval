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