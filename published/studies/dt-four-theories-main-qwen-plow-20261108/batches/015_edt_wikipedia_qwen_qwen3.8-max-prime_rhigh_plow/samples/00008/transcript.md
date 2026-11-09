# 015_edt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00008

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a4b0216c-1bfa-4cfa-af80-de686717f5fa/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a4b0216c-1bfa-4cfa-af80-de686717f5fa/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing What You Would Most Like to Learn

Evidential decision theory (EDT) is a school of thought within decision theory that evaluates actions by their *news value*. The reference article summarizes the idea by saying that EDT recommends the action that would be evidence for the best expected outcome: “do what you most want to learn that you will do” (Ahmed 2021, quoted in Wikipedia contributors 2026). If you were to receive a message telling you which action you had chosen, EDT asks what that message would lead you to expect. The rational action, on this view, is the one whose news you would most welcome.

This contrasts with causal decision theory (CDT), which evaluates actions by their expected causal consequences. CDT asks, “If I intervened to bring about this action, what would happen?” EDT asks, “Given that this action is taken, what should I infer about the world?” The two approaches often agree, especially in ordinary cases where actions are causally effective and not strongly correlated with independent states of the world. But they diverge in famous thought experiments involving predictors, twins, copies, and other forms of correlation.

This essay gives a formal account of EDT, explains how to apply it to decision problems, discusses how it treats dependencies and counterfactuals, and examines some unresolved questions. Where I go beyond the supplied reference article, I will say so explicitly.

---

## 1. Formal definition

The reference article attributes to Gibbard and Harper (1976) the following EDT value function:

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

where:

- \(A\) is an available action;
- \(\{O_j\}\) is a partition of possible outcomes;
- \(D(O_j)\) is the desirability, utility, or value of outcome \(O_j\);
- \(P(O_j\mid A)\) is the agent’s conditional probability of outcome \(O_j\) given that action \(A\) is performed.

Equivalently, EDT chooses the action with the highest conditional expected utility:

\[
V(A)=\mathbb{E}[D(O)\mid A].
\]

For continuous outcome spaces, the sum is replaced by an integral.

The EDT decision rule is:

\[
A^* \in \arg\max_A V(A).
\]

If several actions maximize \(V\), EDT permits any of them, or requires a tie-breaking rule supplied by the context.

The article contrasts this with the causal decision-theoretic formula:

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A \mathrel{\Box\rightarrow} O_j\) means that outcome \(O_j\) would obtain in the counterfactual situation in which action \(A\) is performed. In modern causal-modeling language, one often writes this as \(P(O_j\mid do(A))\), the probability of \(O_j\) under an intervention setting \(A\) to occur. EDT uses ordinary conditional probabilities \(P(O_j\mid A)\); CDT uses interventionist or counterfactual probabilities \(P(O_j\mid do(A))\) or \(P(A \mathrel{\Box\rightarrow} O_j)\).

The difference is crucial. Conditioning on \(A\) asks what \(A\) tells you about the world. Intervening on \(A\) asks what would happen if \(A\) were produced while holding fixed, in the appropriate way, the causal background conditions.

A useful way to write the EDT calculation is by introducing states of the world. Let \(S\) be a variable representing relevant states: predictor predictions, the actions of correlated agents, medical conditions, social circumstances, and so on. If action \(A\) in state \(s\) produces outcome \(O(A,s)\), then

\[
V(A)=\sum_s P(S=s\mid A)D(O(A,s)).
\]

This formulation is not explicitly in the source, but it is mathematically equivalent to the source’s formula and makes EDT easier to apply. EDT does not use the prior probabilities \(P(S=s)\) when comparing actions; it uses the conditional probabilities \(P(S=s\mid A)\). The action is treated as evidence about the state.

---

## 2. How to apply EDT to a decision problem

A practical EDT analysis can proceed as follows.

1. **Specify the available actions.**  
   Let the agent choose among actions \(A_1,\dots,A_n\). These should be mutually exclusive options at the relevant decision point.

2. **Specify the outcomes.**  
   Identify the possible outcomes \(O_j\) and assign desirabilities \(D(O_j)\). The outcomes should include everything the agent intrinsically cares about: money, welfare, reputational effects, future opportunities, or even facts about what kind of agent she is, if those are valued intrinsically.

3. **Specify the probabilistic model.**  
   EDT requires a joint probability model over actions, states, and outcomes. This is where predictors, correlations, psychological similarity, selection effects, and other dependencies enter.

4. **Compute conditional probabilities.**  
   For each action \(A\), compute \(P(O_j\mid A)\), or equivalently \(P(S=s\mid A)\).

5. **Compare conditional expected utilities.**  
   Choose an action maximizing

   \[
   V(A)=\sum_j P(O_j\mid A)D(O_j).
   \]

One technical caveat is that \(P(O_j\mid A)\) is undefined if \(P(A)=0\). The reference article does not discuss this problem. In many formal treatments, one assumes that all available actions have positive probability, at least for the purpose of deliberation. Later I will suggest an operational way of handling zero-probability actions by using small “trembling” probabilities and taking limits.

---

## 3. Newcomb’s problem

The reference article discusses Newcomb’s paradox as a central example. A player faces two boxes:

- Box A is transparent and always contains \$1,000.
- Box B is opaque. Its contents were set earlier by a highly reliable predictor.
  - If the predictor predicted that the player will take only B, then B contains \$1,000,000.
  - If the predictor predicted that the player will take both boxes, then B contains nothing.

The player may either take only box B, called “one-boxing,” or take both boxes A and B, called “two-boxing.” Suppose the predictor is correct with probability \(0.99\). The source gives the following conditional probabilities:

\[
P(\text{1M in B}\mid \text{take only B})=0.99,
\]
\[
P(\text{nothing in B}\mid \text{take only B})=0.01,
\]
\[
P(\text{1M in B}\mid \text{take both boxes})=0.01,
\]
\[
P(\text{nothing in B}\mid \text{take both boxes})=0.99.
\]

The EDT values are:

\[
\begin{aligned}
V(\text{take only B})
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0\\
&=\$990{,}000.
\end{aligned}
\]

\[
\begin{aligned}
V(\text{take both boxes})
&=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000\\
&=\$10{,}010+\$990\\
&=\$11{,}000.
\end{aligned}
\]

Since

\[
V(\text{take only B})>V(\text{take both boxes}),
\]

EDT recommends taking only box B.

The philosophical interest is that two-boxing appears to dominate one-boxing in a state-by-state sense. If B already contains \$1,000,000, taking both boxes yields \$1,001,000 rather than \$1,000,000. If B is empty, taking both boxes yields \$1,000 rather than \$0. Whatever is already in B, taking both boxes seems to give \$1,000 more. CDT therefore recommends two-boxing, because the predictor’s prediction is already in the past and the player’s current choice does not causally change what is in B.

EDT rejects the assumption that the relevant states are independent of the action. The player’s choice is strong evidence about what the predictor predicted. One-boxing is evidence that B contains \$1,000,000; two-boxing is evidence that B is empty. EDT treats the action not as a causal lever on the past, but as information about the past.

---

## 4. Twin prisoner’s dilemma

The reference article also discusses a twin version of the prisoner’s dilemma. Aomame and her psychological twin are in separate rooms and cannot communicate. Their reasoning processes are exactly analogous. The payoff structure is:

- If both cooperate, each gets \$5.
- If both defect, each gets \$1.
- If one cooperates and the other defects, the defector gets \$10 and the cooperator gets \$0.

The source assumes perfect psychological symmetry, so:

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]
\[
P(\text{twin defects}\mid \text{Aomame cooperates})=0,
\]
\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0,
\]
\[
P(\text{twin defects}\mid \text{Aomame defects})=1.
\]

Then EDT gives:

\[
\begin{aligned}
V(\text{Aomame cooperates})
&=1\cdot \$5+0\cdot \$0\\
&=\$5,
\end{aligned}
\]

\[
\begin{aligned}
V(\text{Aomame defects})
&=0\cdot \$10+1\cdot \$1\\
&=\$1.
\end{aligned}
\]

So EDT recommends cooperation.

The source gives the perfect-correlation case. A natural generalization, which I add for clarity, is to allow imperfect correlation. Let

\[
q=P(\text{twin cooperates}\mid \text{Aomame cooperates}),
\]
\[
r=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]

Then:

\[
V(\text{cooperate})=5q+0(1-q)=5q,
\]

\[
V(\text{defect})=10r+1(1-r)=1+9r.
\]

EDT recommends cooperation exactly when

\[
5q>1+9r.
\]

This inequality is useful for unfamiliar cases. If the twin’s action is independent of Aomame’s action, then \(q=r=p\), where \(p\) is Aomame’s prior probability that the twin cooperates. In that case:

\[
V(\text{cooperate})=5p,
\]
\[
V(\text{defect})=1+9p.
\]

Since

\[
1+9p>5p
\]

for every \(p\in[0,1]\), EDT recommends defection when the twin’s behavior is probabilistically independent of Aomame’s choice. EDT therefore does not recommend cooperation merely because cooperation is morally attractive. It recommends cooperation only when one’s own cooperation is sufficiently strong evidence that the other agent will cooperate.

This point generalizes. EDT can recommend cooperation in prisoner’s dilemma-like cases involving clones, psychological twins, sufficiently similar artificial agents, or correlated decision procedures. But in an ordinary one-shot prisoner’s dilemma with an independent opponent, EDT and CDT usually agree in recommending defection.

---

## 5. Dependencies, counterfactuals, and causal structure

EDT’s distinctive feature is that it cares about evidential dependence, not only causal dependence. An action can be relevant to EDT even if it does not causally influence the outcome. It is enough that the action is probabilistically correlated with something that matters.

Common sources of evidential dependence include:

1. **Prediction.**  
   A predictor has predicted your action before you take it. Your action does not change the past prediction, but it is evidence about that prediction.

2. **Common causes.**  
   Some hidden factor influences both your action and the outcome. Your action is then evidence about that hidden factor.

3. **Psychological or algorithmic similarity.**  
   If another agent reasons like you, your choice may be evidence about their choice.

4. **Selection effects.**  
   The fact that you are making a certain decision may be evidence about which branch, room, awakening, or population you are in.

5. **Logical or mathematical dependence.**  
   If several agents implement the same decision algorithm, the output of one instance can be evidence about the outputs of others.

The contrast with CDT can be expressed using causal Bayes nets. In such a network, ordinary conditioning on \(A\) uses all probabilistic associations represented in the graph. An intervention \(do(A)\), however, cuts the incoming causal arrows to \(A\). It asks what would happen if \(A\) were set from outside the system. EDT evaluates \(P(O\mid A)\); CDT evaluates \(P(O\mid do(A))\). These are equal in randomized experiments or in cases where the action is not confounded, but they can differ sharply otherwise.

Consider a “smoking lesion” case. This example is not in the supplied article, but it is a standard way to illustrate the debate. Suppose smoking does not cause cancer. Instead, a genetic lesion both causes a disposition to smoke and causes cancer. Smoking is therefore evidence of the lesion. If smoking is pleasurable but cancer is bad, EDT may recommend not smoking, because smoking is bad news: it raises the conditional probability that one has the lesion and will get cancer. CDT, by contrast, says that smoking does not causally affect cancer, so if one enjoys smoking, one should smoke. Lewis’s criticism that EDT promotes “an irrational policy of managing the news” is aimed at exactly this sort of case (Lewis 1981, quoted in Wikipedia contributors 2026).

The EDT response is that actions are not merely causal levers; they are also symptoms of the world. If your action reveals something about your type, your environment, or the likely behavior of similar agents, EDT says that evidential information belongs in the decision calculation. Whether this is a virtue or a defect is one of the central philosophical disputes between EDT and CDT.

---

## 6. Policies, precommitments, and dynamic choice

The reference article presents EDT mainly as a theory of individual actions. But many decision problems involve policies: rules that map observations or histories to actions. EDT can be extended naturally to policies, though this extension is my own exposition rather than a detailed claim of the source.

Let \(\Pi\) be a set of possible policies. A policy \(\pi\) might be “one-box in Newcomb’s problem,” “cooperate with agents sufficiently similar to me,” or “bet on heads when awake after a certain coin toss.” EDT can evaluate a policy by conditioning on the proposition that the agent follows that policy:

\[
V(\pi)=\sum_z P(Z=z\mid \pi)D(Z=z),
\]

where \(Z\) ranges over final outcomes.

In a dynamic problem with histories \(h\), one can write:

\[
V(\pi)=\sum_h P(h\mid \pi)D(\text{outcome}(h)).
\]

Here \(P(h\mid \pi)\) is the probability of history \(h\) given that the agent implements policy \(\pi\). The important point is that EDT conditions on the whole policy, not merely on isolated actions abstracted from the rule that produced them.

This matters for precommitment. Suppose an agent can publicly precommit to one-boxing before the predictor makes its prediction. EDT evaluates the precommitment as evidence about future behavior and therefore as evidence about the predictor’s prediction. If precommitting to one-boxing makes it highly probable that the predictor predicted one-boxing, EDT favors the precommitment. The same reasoning can apply to voting, charitable giving, environmental behavior, or coordination among many similar agents: your policy may be evidence about what other agents do.

The reference article briefly mentions a related argument: even if one is not fully confident in EDT, it may be prudent to act as if EDT is true when many correlated decision-makers are involved, because the stakes may be higher than in purely causal reasoning (MacAskill et al. 2021). This is a strategic or wager-like argument rather than a proof of EDT.

---

## 7. Open questions and an operational interpretation

The source gives the core EDT formula and several examples, but it leaves important questions open. I discuss three: act probabilities, self-locating uncertainty, and the boundary between evidential and causal reasoning.

### 7.1 Act probabilities and zero-probability actions

EDT requires conditional probabilities \(P(O_j\mid A)\). These are undefined if \(P(A)=0\). This is not merely a technicality. In deliberation, an agent may become increasingly certain that she will perform the action she judges best. If she assigns probability 1 to that action and probability 0 to the alternatives, EDT’s formula becomes hard to apply.

The reference article does not resolve this. One reasonable operational interpretation, which I propose rather than find in the source, is to use a full-support deliberative prior over available actions. For a small parameter \(\varepsilon>0\), assign every feasible action probability at least \(\varepsilon\), or otherwise ensure that all actions have positive probability. Compute

\[
V_\varepsilon(A)=\sum_j P_\varepsilon(O_j\mid A)D(O_j).
\]

Then take the limit as \(\varepsilon\to 0\), if the limit exists and is stable. This is analogous to “trembling hand” refinements in game theory, where players are assumed to make small mistakes with low probability.

In Newcomb’s problem, for example, small uncertainty about whether the agent will one-box or two-box does not change the EDT recommendation as long as the predictor remains highly reliable. But if a verdict depends sensitively on the chosen limiting process, then the decision problem itself may be underspecified. EDT needs a substantive model of how the agent’s action is related to the relevant states of the world.

### 7.2 Sleeping Beauty and centered evidence

The reference article mentions the Sleeping Beauty problem only briefly. It says EDT has been applied to avoid Dutch book arguments, but it also notes that Conitzer (2015) argues that halfers can still be Dutch booked even after adopting EDT. The article does not settle the underlying debate.

The difficulty is that Sleeping Beauty involves self-locating uncertainty: Beauty must reason about centered propositions such as “I am awake now” rather than only about uncentered propositions such as “the coin landed heads.” EDT’s usual formula applies most cleanly when actions and outcomes are uncentered propositions. When centered evidence matters, one must decide what probability space to condition on.

A cautious operational interpretation, not supplied by the source, is to evaluate betting policies conditional on the agent’s centered situation. For example, instead of asking only for \(P(\text{heads}\mid \text{bet on heads})\), one asks for the probability of heads conditional on being awake and facing a particular betting decision. This preserves the EDT idea—choose the action with the best news—while making explicit that the relevant conditioning event may be a centered proposition. However, this remains philosophically contested.

### 7.3 Which dependencies count?

EDT uses the agent’s probability function, so the verdict can depend on how the agent models the world. If the agent believes that a predictor is reliable, EDT may one-box. If she believes the predictor is unreliable, EDT may two-box. If she believes her action is independent of the other player in a prisoner’s dilemma, EDT defects. If she believes her action is strongly correlated with the other player, EDT may cooperate.

This is not necessarily a flaw. Decision theories must operate relative to the agent’s beliefs. But it means that EDT does not give a single answer unless the probabilistic structure of the problem is specified. The theory tells you how to reason from a model; it does not automatically tell you which model is correct.

---

## 8. Criticism and philosophical significance

The reference article includes two important criticisms. David Lewis characterized EDT as “an irrational policy of managing the news” (Lewis 1981). James M. Joyce wrote that rational agents choose acts on the basis of their “causal efficacy,” not their “auspiciousness”; they act to bring about good results even when doing so might betoken bad news (Joyce 1999).

These criticisms capture the intuitive worry about EDT. In the smoking lesion case, avoiding smoking does not prevent cancer; it merely avoids being evidence of cancer. In Newcomb’s problem, one-boxing does not cause the predictor to have placed money in B; it is merely evidence that the predictor did so. From a causal point of view, this can seem like trying to manipulate the message rather than the world.

EDT’s defenders respond that rational agency cannot always be separated from evidence. If your decision is produced by a physical or computational process, then that process may be predictable, replicated, or correlated with other agents. In such cases, treating your action purely as an intervention may ignore real structure in the world. If a predictor is reliable, one-boxing really is associated with receiving \$1,000,000. If many agents use similar reasoning, your cooperation may be evidence of their cooperation. EDT takes those associations seriously.

The debate between EDT and CDT is therefore not merely technical. It reflects a deeper disagreement about what decision theory is for. Is choice primarily a means of causing outcomes? Or is choice also a piece of evidence about the kind of world one is in and the kind of agent one is? EDT answers that a rational agent should care about the news her action provides.

---

## Conclusion

Evidential decision theory offers a simple but radical rule: choose the action that would be the best news. Formally, it maximizes

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

using conditional probabilities rather than interventionist counterfactuals. In Newcomb’s problem, this leads EDT to one-box, because one-boxing is strong evidence that the predictor placed \$1,000,000 in the opaque box. In twin prisoner’s dilemma cases, EDT can recommend cooperation, because one’s own cooperation is evidence that a sufficiently similar agent will also cooperate.

The theory is easy to state but delicate to apply. One must specify actions, outcomes, utilities, and especially the probabilistic dependencies linking actions to states of the world. EDT is sensitive to prediction, correlation, similarity, selection effects, and self-locating uncertainty. It also faces unresolved questions about act probabilities, zero-probability choices, and centered evidence.

EDT’s great strength is that it takes seriously the evidential significance of action. Its great vulnerability is that it may favor actions that are merely good news rather than good causes. Whether that is a defect or a deeper insight depends on one’s view of rational agency itself.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Conitzer, Vincent. “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, no. 9 (2015): 2887–2899.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688. Text licensed under CC BY-SA 4.0.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write a mathematical essay/blog post on EDT and how to apply it to decision problems. Need target 2400-3000 words including references. Must use source material, distinguish source claims from own assumptions/proposals. Need explain central definitions, reasoning, implications, dependencies, counterfactuals, open questions and operational interpretation if available. Use examples. Need not answer one assigned case. Need produce final substantive readable mathematical essay. Need likely include references brief. Need be careful with licensing? Source is Wikipedia CC BY-SA. We are writing original account but can cite. Need maybe include CC attribution? User asks essay with references. Could mention adapted from Wikipedia? Probably cite source. Need ensure word count approx 2400-3000. Need maybe produce ~2600 words. Need plan.

Content outline:
Title: Evidential Decision Theory: Choosing the Best News About Yourself
Intro: decision theory: actions, states, outcomes, utilities. EDT maximizes news value: conditional expected utility. Contrast CDT causal intervention. EDT says do what you'd most like to learn you'll do.
Formal definitions:
Decision problem: finite set A actions, set Ω states maybe outcomes O. Agent has probability measure P over world propositions including acts and outcomes; desirability D(O). EDT value V(A)=Σ_j P(O_j | A) D(O_j). More generally V(A)=E_P[D(O) | A]. Choice rule choose argmax V(A), tie etc.
Need discuss conditional probability: P(O|A)=P(O∧A)/P(A), undefined if P(A)=0. Need address zero-probability acts: operational interpretation via regular probabilities or limit, or assume acts have positive probability. This is an open/technical issue. Could propose: use Jeffrey's radical probabilism / ratifiability? EDT often uses act probabilities from agent's epistemic state. If P(A)=0, define via limiting conditional probabilities or assign small tremble probabilities. We can mention source leaves open. Need distinguish source vs own.
News value: If action is evidence of state/outcome.
Dependencies and counterfactuals: EDT uses evidential dependence, not causal dependence. If action correlates with outcome through prediction, common cause, logical dependence, selection effects, smoking lesion etc. It treats counterfactual as conditional on news that A was performed. But conditional probability can be affected by beliefs about how act came about. Need explain difference from intervention: P(O|A) vs P(A □→ O). CDT counterfactual formula U(A)=Σ P(A□→O_j)D(O_j) from Gibbard/Harper. Need discuss that P(O|A) may equal counterfactual when action does not provide evidence of causally independent states, or in randomized experiments.
Examples:
Newcomb: source numbers 99% predictor. Compute EDT and CDT maybe. Need use source: V(one-box)=990k, two-box=11k. Also explain dependencies: predictor's prediction common cause/past. EDT one-box because action evidences million. CDT two-box because money already fixed. Need maybe mention if predictor perfect and P(one-box)=0? not.
Twin prisoner's dilemma: perfect psychological twin. Compute. EDT cooperate. Need maybe discuss non-perfect correlation: let q=P(twin C | I C), r=P(twin C | I D). If payoffs: CC 5, CD for me cooperate/other defect 0, DC for me defect/other coop 10, DD 1. Then V(C)=5q + 0(1-q)=5q; V(D)=10r + 1(1-r)=1+9r. Cooperate if 5q > 1+9r. If q=r=p (identical decision procedure symmetric) then cooperate if 5p > 1+9p? Wait if q=r=p impossible? If same strategy under symmetric info, conditional probabilities maybe P(twin C|I C)=1 if deterministically same? For imperfect similarity: q high, r low. Could develop. Need maybe example with correlation ρ. But keep manageable.
Smoking lesion? Not in source but classic EDT criticism. Could use to explain limitations: smoking correlated with cancer due to lesion; EDT may prefer smoking as evidence of no cancer? Actually smoking lesion: lesion causes both smoking and cancer; smoking is evidence of lesion and cancer, so EDT might avoid smoking? Wait standard smoking lesion: lesion causes cancer and causes smoking? If lesion causes cancer and smoking, then smoking is evidence of lesion/cancer, so EDT says don't smoke? Let's recall: Smoking Lesion problem (Egan?): Smoking is correlated with cancer due to a lesion, but smoking itself doesn't cause cancer. People with lesion more likely smoke and get cancer. If you enjoy smoking, CDT says smoke (no causal effect), EDT might not smoke because smoking is evidence of lesion/cancer. Actually depending desire: utility of smoking with no cancer high, smoking with cancer maybe lower; non-smoking with no cancer maybe. EDT may choose not smoke to avoid bad news. This illustrates "managing the news" criticism. Need include as own example? Could. The source mentions Lewis criticism but not example. Use it to explain counterfactuals.
Medical Newcomb? Could include.
Policies: Evaluate policies vs acts. EDT can evaluate a policy π by conditioning on policy being adopted/implemented: V(π)=E[D|π]. If policy maps observations to actions, condition on whole policy. In dynamic settings, update? Need discuss. EDT's action conditional probabilities might be unstable if agent's beliefs about own future action change (ratification). Could mention EDT may need ratifiability: choose act whose expected utility remains maximal conditional on doing it. Need source leaves open? Could propose operational interpretation: treat EDT as recommendation for public announcement/choice under self-locating uncertainty? Hmm.
Need discuss dependencies: correlations arising from predictor, twins, shared algorithm, genetic/social correlations, selection effects. EDT doesn't require causal influence; any probabilistic dependence in agent's epistemic state matters. But if dependence is due to common effect/collider? Need careful: Conditioning on action can open colliders and create spurious dependence. EDT is sensitive to that. The theory as source defines just conditional probabilities. Philosophically, it treats your act as a symptom of the world, not just a lever.
Counterfactuals: Source says CDT uses counterfactual probabilities. Need explain EDT's counterfactual? In EDT, "if I were to do A" is interpreted as learning that A was done; no intervention. This can be problematic if the news of A changes probabilities via evidence about decision process. Need discuss.
Open questions:
- How are probabilities over one's own actions assigned? If agent is certain she will do A, conditional probabilities undefined or degenerate. EDT requires positive uncertainty over actions. This is known problem of deliberation. Could propose: use small "deliberative noise" or hypothetical prior over actions, or evaluate via hypothetical randomization: choose A if conditional expected utility under a model where action is uncertain due to computational uncertainty/logical uncertainty. Operational interpretation: before deciding, assign a full-support prior over possible choices (e.g. ε-tremble), compute conditional expectations, then choose max; if stable as ε→0, use. Need distinguish own proposal.
- What if P(A)=0? Use regular conditional probabilities or limit.
- Which outcomes? Desirability of outcomes includes all relevant consequences, including news value? Need avoid double counting? In EDT, D(O_j) should be desirability of outcome not including the value of the news? Actually news value arises from conditional probabilities, not utility of action itself. Could discuss: utility assigned to final states; if agent intrinsically values being a certain kind of person, can include that in outcome.
- Policies with observations: conditional on policy may be tricky due to conditional probabilities at each info set. We can propose evaluating policy ex ante: V(π)=Σ histories P(h|π) D(outcome). But if agent receives news mid-process, may update. Need not too deep.
Need maybe mention Sleeping Beauty: source says EDT applied to avoid Dutch books; halfers maybe still Dutch booked by Conitzer. We can include section: Self-locating uncertainty/Sleeping Beauty, but brief. Explain EDT in SB? Could be complex. Need maybe mention that EDT's conditionalization on centered acts interacts with self-locating credences; source leaves unresolved. We can say source only reports debate, not full solution. We can propose operational: if Beauty's choice affects betting odds under centered evidence, EDT assesses bets conditional on awakening/choice. But maybe not necessary. However prompt says where source leaves important question open, explain uncertainty and develop reasonable interpretation. Could choose zero-prob actions / policy rather than Sleeping Beauty. But Sleeping Beauty mentioned. Need include at least brief.
Need target words. Let's estimate. Need 2400-3000. We can write ~2600. Need references list maybe 8 items. Use equations. Need maybe no appendices.
Need ensure mathematical notation clear. Use Markdown with headings. Include citations in text maybe [Ahmed 2021], [Gibbard and Harper 1976], etc. Need final with brief conclusion.
Need mention source: Wikipedia article revision. Could cite as Wikipedia contributors 2026? The source oldid 1373679688, date 2026-09-07. We can reference. Need note source claims. "The reference article gives the following formal definition..." Need distinguish. "I will add..." Use phrases.
Need maybe include a decision procedure section:
Algorithm:
1. Enumerate actions or policies A.
2. Specify outcome partition O_j and desirabilities D(O_j).
3. Specify epistemic probability P over relevant propositions, including correlations/predictors.
4. Ensure P(A)>0 (or use limiting full-support prior).
5. Compute V(A)=Σ P(O_j|A)D(O_j).
6. Choose max. Check ratification: after tentatively choosing A, update? If V(A|A) trivially? Hmm.
Need discuss evaluating policies:
For deterministic policy π in environment with states ω, outcome f(π,ω). If prior over ω and possibly agent type, V(π)=Σ_ω P(ω | π) D(f(π,ω)). But P(ω|π) may be weird if π chosen based on ω? In policies mapping observations to actions, condition on policy as proposition: "agent uses π". If observations are evidence, include them. For a policy, not just conditioning on final action; it conditions on algorithm. In Newcomb, policy one-box or two-box. In twin PD, policy cooperate.
Need discuss "relevant dependencies and counterfactuals": EDT treats all dependencies encoded in P. If predictor is reliable, P(predicted one-box | one-box)=0.99. If action is causally independent but evidentially dependent, EDT still uses dependence. If action is a collider, conditioning can create dependence that may not represent genuine dependency? But EDT accepts as news. Need maybe explain with causal graphs:
- Predictor case: State S (prediction/box content) →? Actually predictor predicts action, then action? In causal graph: hidden type? Predictor's prediction causes box content, and is correlated with action due to prediction. If action has no causal arrow to box content, EDT still has A correlated with S.
- Intervention do(A) cuts incoming arrows; conditional keeps them.
Could include simple Bayes net notation: EDT conditions on A: P(O|A); CDT uses do(A): P(O|do(A)) or counterfactual. In many causal models P(O|do(A)) = Σ_s P(O|A,s)P(s) if no unobserved confounding, but not generally. This will help mathematical. Need not overdo.
Need maybe discuss dominance: In Newcomb two-box dominates one-box in states (if box fixed, both > only by $1000). EDT violates dominance because states not independent of action. This is key. Could include. Source says CDT two-box because already set. We can elaborate.
Need philosophical motivation: "Do what you most want to learn that you will do." It evaluates actions as evidence. In a deterministic/physicalist world, actions are outputs of algorithms correlated with other algorithms; EDT can coordinate with predictors/twins. Mention "superrationality" maybe source see also. Could explain EDT resembles Hofstadter's superrationality? Could but maybe not needed.
Need maybe discuss EDT vs CDT in Prisoner's Dilemma: ordinary one-shot PD with no correlation: P(other C | I C)=P(other C), EDT = CDT = defect. Only when correlation is present EDT cooperate. This clarifies.
Need mention "Evidentialist's Wager": source says even if less credence in EDT, act as if EDT because correlated decision-makers stakes higher. Could include as implication: in large-scale altruism, EDT may recommend actions that are evidence of many similar agents cooperating. But careful: source claims. We can mention.
Criticisms: Lewis "irrational policy of managing the news"; Joyce causal efficacy. We can include. Then response: EDT defenders say rational choice should account for evidence, especially when causal influence impossible or when decisions are logically correlated. But criticisms highlight that EDT may reward actions that are merely symptoms of good states, not causes.
Need maybe discuss "news value" and potential instability: If agent publicly announces action, then news is already out; EDT may change? Example: If you can make yourself known to one-box before choice, maybe? Not necessary.
Need think about exact word count. Let's draft with headings:
- Title
- 1. What EDT says (~250)
- 2. Formal definition (~400)
- 3. How to apply: recipe (~350)
- 4. Newcomb (~350)
- 5. Twin PD and generalized correlation (~350)
- 6. Dependencies, counterfactuals, causal contrast (~400)
- 7. Open questions and operational interpretation (~450)
- 8. Criticism and implications (~250)
- Conclusion (~100)
References (~150)
Total ~3000. Need maybe trim.
Need include equations. Need maybe cite source claims: "According to the reference article..." etc. Need avoid too many citations.

Let's develop details.

Detailed content:

Title: Evidential Decision Theory: Choosing on the Best News

Intro:
Decision theory: given acts, outcomes, probabilities, utilities. EDT: choose action with highest news value. Quote: do what you most want to learn that you will do [Ahmed; Wikipedia]. It uses conditional probabilities rather than causal counterfactuals. The essay explains.

Formal:
Let A finite set of acts {A_i}. Let {O_j} partition of possible outcomes. Agent has probability measure P over propositions including acts and outcomes; desirability D(O_j) real. EDT expected utility/news value:
V(A)=Σ_j P(O_j|A)D(O_j)=E[D(O)|A].
Source gives same from Gibbard/Harper. If continuous, integral.
Choice rule: choose A* ∈ argmax_A V(A). Ties arbitrary.
CDT uses:
U(A)=Σ_j P(A □→ O_j)D(O_j). In causal modeling, replace with P(O_j|do(A)). The difference is conditional vs intervention. Need explain: P(O|A) is probability of O given news A; P(A□→O) probability if A were brought about. They coincide when act is probabilistically independent of non-causally affected states or when randomized.
Need maybe note D is desirability of outcome, not expected utility of action. If outcomes include money, D=$. If not linear, utility.
Need mention conditional probability requires P(A)>0. If agent is certain, issue.

Application recipe:
1. Define act partition at the choice point. Must be exclusive, available, and under agent's control (though EDT does not require causal independence).
2. Choose outcome partition: include all consequences that matter, including own money, others' welfare, perhaps being a certain type. Avoid including the mere news of act unless intrinsically valued.
3. Model probabilistic dependencies: predictor accuracy, twin similarity, correlations. Represent as joint distribution over acts, states, outcomes.
4. Compute conditional probabilities. If zero-prob acts, use full-support prior/limit. (Own operational proposal)
5. Compare V.

Need maybe include an equation with law total probability: If S states determine outcome with act, V(A)=Σ_s P(S=s|A)D(O(A,s)). This is useful. Here S may include predictor's prediction, twin's action, lesion status. This makes state dependence explicit. EDT conditions S on A.

Newcomb:
Define predictor 99%. State M: predicted one-box/box has $1M; N: predicted two-box/empty. Payoffs: one-box: if M $1M, if N $0; two-box: if M $1,001,000; if N $1,000. Conditional probabilities source: P(M|one-box)=0.99, P(N|one-box)=0.01; P(M|two-box)=0.01, P(N|two-box)=0.99. Compute as source. V(one)=990k, V(two)=11k. EDT one-box.
Need explain dominance: For each state, two-box yields $1000 more. But EDT denies state-action independence. The action is evidence of state. If predictor perfect, V(one)=1M, V(two)=1k. CDT: P(M □→ two?) Actually if two-box counterfactually, prediction unchanged? So U(two)=P(M)1,001,000+P(N)1000 depending prior; if predictor reliable and you don't know prediction, likely two-box better? Source says CDT recommends both. We can state.
Need maybe discuss if prior probability of one-box not 50? Conditional probabilities incorporate predictor accuracy and base rates. Example if agent has strong prior she'll two-box, maybe P(M|one-box) by Bayes depends. But source assumes symmetric 99. Need maybe note.

Twin PD:
Define Aomame. Perfect twin. Conditional probabilities 1 and 0. Compute. V(C)=5, V(D)=1. EDT cooperate.
Generalization: Let q=P(twin C | I C), r=P(twin C | I D). Payoff matrix: me C/twin C 5, me C/twin D 0; me D/twin C 10, me D/twin D 1. Then V(C)=5q, V(D)=10r+1(1-r)=1+9r. Cooperate iff 5q > 1+9r. Perfect correlation q=1,r=0 => cooperate. If twin's choice independent q=r=p, then cooperate iff 5p > 1+9p => -4p >1 impossible; defect. Thus EDT only cooperates when one's act is strong evidence of twin's cooperation and not too strongly evidence of twin's defection when defecting. This helps unfamiliar cases. Need mark this as my extension? The source only gives perfect case; say "The source gives perfect twin; a natural generalization is..."
Could also mention ordinary PD with independent other: q=r=prob other cooperates, defect. If correlation due to shared algorithm, EDT can support cooperation.

Dependencies and counterfactuals:
EDT's core is evidential dependence. Mathematical: If A and O statistically dependent, P(O|A)≠P(O). Dependencies can arise from:
- common cause/predictor (Newcomb),
- identical or similar decision algorithms (twins, clones, AI copies),
- selection effects or self-locating uncertainty,
- social/psychological correlations.
It does not ask whether A causes O. It asks what A indicates. In Bayesian nets, conditioning on A updates beliefs about ancestors/colliders; intervention do(A) deletes arrows into A. EDT uses conditioning; CDT uses do. Example: If lesion L causes both smoking S and cancer C, then P(C|S)>P(C). EDT may evaluate smoking by P(C|S); if smoking's pleasure does not outweigh cancer news, EDT avoids smoking, even if S has no causal effect on C. This is a classic criticism; my example. CDT uses P(C|do(S))=P(C) and may smoke. This illustrates Lewis/Joyce criticism.
Need be careful with lesion direction: If lesion causes smoking and cancer, conditioning on smoking increases P(lesion/cancer). Yes. If agent chooses to smoke? Smoking is evidence of lesion. EDT may choose not to smoke. If pleasure huge maybe smoke. But standard says EDT refuses smoke to avoid bad news.
Need mention if action causes outcome, conditional and intervention often agree if no confounding. In randomized trial, P(O|do(A))=P(O|A). So EDT/CDT agree.

Policies:
EDT can evaluate policies not just single acts. Let Π be set of policies. A policy maps information to actions. The proposition "π is implemented" may include behavioral dispositions. Value:
V(π)=Σ_o P(O_o | π) D(O_o).
If policy uses observations, condition on entire policy, not just action at one node, because the news of following a rule can carry information. In dynamic problems, one can compute expected utility by summing over histories h compatible with π:
V(π)=Σ_h P(h | π) D(z(h)), where z terminal outcome. But P(h|π) is the probability of history given that the agent is known to follow π. This is an operational extension (source doesn't detail). Need mention. For precommitments, EDT evaluates precommitment as news about future behavior; if precommitment changes predictors' predictions, that matters.

Open questions / operational interpretation:
1. Act probabilities and certainty. In deliberation, agent may believe she will perform the chosen act. If P(A)=1 for selected act and 0 for alternatives, V undefined/trivial. Source's formula assumes acts have probabilities. This is a known issue not addressed. My proposal: Use a full-support "deliberative prior" over actions, representing uncertainty about one's own future choice due to incomplete computation, self-prediction error, or hypothetical evaluation. For ε>0, assign P_ε(A)>0, compute V_ε(A). If limit ε→0 exists and stable, use it. In Newcomb, small trembles don't change verdict if predictor accuracy high. In cases where verdict depends on arbitrary trembles, the problem is under-specified; need more model of how choices are generated. Alternatively, evaluate policies by considering the agent's prior before deliberation. This is my proposal, not source.
2. Conditioning on impossible or measure-zero policies. Similar limit/regular conditional.
3. Self-locating/Sleeping Beauty. Source says EDT applied to Dutch books; Conitzer argues halfers still vulnerable. The question of centered evidence remains open. I can propose: Treat awakenings as observations in a policy evaluation; value of a betting policy conditional on centered awakening. But no consensus. Need distinguish source.
4. What probabilities? Objective chance or subjective credence. EDT is usually Bayesian with agent's credences. But if credences are manipulated, problem. Could mention.
5. Ratification/stability. EDT may recommend an act that, once chosen, would be re-evaluated differently. A refined rule: choose acts that maximize V conditional on the act being chosen and known (ratifiable). This can avoid some instability. Need maybe mention as own proposal? There is known "EDT ratifiability". Could include in open questions: In some problems, conditional probabilities depend on what the agent expects to do; a recommendation should be stable under the agent's belief that she will do it. I propose using ratifiable EDT: choose A such that V(A | A)?? But V(A|A) trivial? Actually ratifiability: An act is ratifiable if it has maximum causal/evidential utility conditional on the agent performing it? For EDT, after deciding to A, conditional probabilities P(O|A) are same? Maybe if beliefs about one's own disposition change. Hmm. Could skip or mention briefly.

Need discuss "stakes many correlated decision-makers" supporting argument: source says even if less credence, act as if EDT because correlations raise stakes. We can include in implications: If many agents use similar reasoning, your action is evidence of their actions; EDT captures this. This can be important in voting, climate, AI, charity. But not exhaustive.

Criticism:
Lewis/Joyce quotes. EDT can be seen as wishing/ managing news. In smoking lesion, it avoids smoking not because it changes cancer but because it avoids being evidence of cancer. Defenders might say if being evidence is part of rational self-conception? Need balanced. Source includes criticisms. We can mention "whether this is irrational depends on whether one thinks choice should be a tool for causing outcomes or an expression/evidence of one's type".

Conclusion: EDT simple: maximize conditional expected desirability. It is powerful in correlated/predictive cases, but requires careful modeling of dependencies and action probabilities. It diverges from CDT when acts are evidence of states they don't cause.

References: Need list:
- Wikipedia contributors, "Evidential decision theory," revision 1373679688, Sept 7 2026. URL.
- Ahmed 2021.
- Gibbard & Harper 1976.
- Lewis 1981.
- Joyce 1999.
- MacAskill et al 2021.
- Conitzer 2015 maybe.
- Greene & Levinstein 2020? Could include but maybe not all. Need avoid lengthy bibliography. Maybe 7 references.

Need word count. Let's draft in final with enough detail. Need maybe count roughly. We can aim ~2700 words. Let's write robust but not too long. Need maybe include mathematical equations in LaTeX.

Potential final essay:

# Evidential Decision Theory: Choosing What You Would Like to Learn

Paragraphs.

Need ensure not too much repetition. Let's write with headings.

Need maybe mention "source claims" explicitly:
"The reference article defines EDT as..." "It reports Newcomb and twin PD calculations." "The article leaves open how to assign probabilities to one's own acts; the following operational treatment is mine." Good.

Let's compose and monitor word count. I can estimate as I write. Use around 250 words intro, 400 formal, 300 recipe, 350 Newcomb, 300 twin, 400 dependencies, 300 policies/open, 300 criticism/conclusion, refs 150. Total 2750.

Let's draft mentally.

Intro:
"When an agent faces a choice..." 150.

Formal section:
Equation. Need include continuous version. Mention conditional expected utility. Source's formula. Contrast CDT formula. Explain.

Potential text:
"The reference article attributes to Gibbard and Harper (1976) the EDT value..." Good.

Act probabilities open question in formal section maybe.

Recipe:
Use states S. Formula:
V(A)=Σ_s P(S=s | A) D(O(A,s)). This is key. Need explain O(A,s) outcome if act A in state s. EDT's distinctive move: P(S|A) not P(S). This helps unfamiliar cases.

Example Newcomb:
Use states s_M, s_E. Equations as source. Need ensure numbers: V(take both) = 0.01*1,001,000 + 0.99*1,000 = 10,010 + 990 = 11,000. Yes.

Twin:
Generalization with q/r. Need be precise: If Aomame cooperates, twin cooperates with q, payoff if twin defects is 0. V(C)=5q + 0(1-q)=5q. If defects, twin cooperates with r, payoff 10; twin defects payoff 1. V(D)=10r + 1(1-r)=1+9r. Cooperate if 5q > 1+9r. For perfect q=1,r=0. For independent q=r=p, V(C)=5p, V(D)=1+9p; since 1+9p > 5p always (1+4p>0), defect. Good.

Dependencies section:
Need include causal graph. Use do notation. "In a causal Bayes net, conditioning on A is not same as intervention do(A). The latter sets A by external intervention and removes incoming arrows. EDT uses observational conditional." Good. Mention smoking lesion example. Need maybe distinguish source: "This example is not in the reference article, but it is a standard way to see the difference." Actually could say "To see the difference, consider a lesion case..." Mark as additional.

Policies section:
Need define policy value. "For policy π, V(π)=E[D|π]." In dynamic, histories. Need note if policy is not a single proposition, define by conditioning on algorithm. Need maybe include example: precommit to one-boxing before predictor makes prediction; EDT values precommitment because it is evidence of future one-boxing and thus of $1M.

Open questions:
Detailed. Need include Sleeping Beauty briefly:
"The source mentions Sleeping Beauty only to say EDT has been used to avoid Dutch books and that Conitzer disputes this. The right centered probabilities are controversial. A cautious EDT approach is to specify a policy over centered observations and evaluate bets conditional on the centered proposition 'I am now awake and choosing...' rather than relying on uncentered coin credences. This is my suggestion, not in source." Need maybe not too deep.

Act uncertainty: important. Need propose full-support prior. Let's articulate:
"The formula requires P(A)>0. But during deliberation an agent may become certain she will choose the best act, making alternatives probability zero. EDT needs a model of uncertainty over one's own choice. One operational interpretation: introduce a small deliberative noise parameter ε, so every feasible act has probability at least ε, compute V_ε, and take a limit if it exists. This is analogous to trembles in game theory. If the limit depends on ε, the decision problem is not sufficiently specified." Good.

Ratification maybe:
"In unstable cases, require that the chosen act remain best after conditioning on the agent's intention to perform it." But careful. Could mention briefly as refinement.

Criticism section:
Quotes. Need source claims. "Lewis called..." "Joyce asserted..." Then response.

Conclusion.

Need references with source URL. Could include CC BY-SA? Maybe mention "This essay uses ideas from Wikipedia article, licensed CC BY-SA 4.0." Since source is CC BY-SA and adaptation may carry share-alike. But user didn't ask. Could include in references or note. Need maybe "Adapted in part from Wikipedia contributors... CC BY-SA 4.0." Good.

Need avoid too many external links? Fine.

Need ensure no hallucinated false details? Sleeping Beauty: source says EDT applied to avoid Dutch books, Conitzer argues halfers still affected. We can state exactly. Don't assert more. Evidentialist's Wager: source says because EDT can involve actions of many correlated decision-makers, stakes may be higher and take priority. We can mention. Need maybe cite.

Potential issue: The source date 2026 (future relative to current? But system current 2026-06-15, source date 2026-09-07? It says oldid 2026-09-07. That's in future from current? But given source, use as is. No matter.

Need maybe ensure word count. Let's write final around 2600. Need maybe use word count mental. I'll produce final with headings and equations. Ensure target 2400-3000. Let's count roughly. If final ~2500 words okay.

Let's draft final now in my mind and then output. Need include all.

Detailed final text:

Title.

Intro (~170 words):
"Evidential decision theory (EDT) is a school ... choose action with highest news value ... do what you most want to learn that you will do. It contrasts with CDT ... In many ordinary cases agree; diverge in Newcomb, twin PD. This essay defines EDT, gives procedure, examples, dependencies/counterfactuals, open questions."

Formal definition (~430):
Let A, O_j, D. Equation. Source attribution. Continuous. Choice rule. State-based formula. Conditional probability requirement. Contrast CDT equation with box arrow. Explain difference. "If action is randomized or independent, they coincide."

How to apply (~300): enumerate acts/outcomes/probabilities; compute; check zero; use states.

Newcomb (~350): table maybe text. Equations. Explain dominance and CDT.

Twin PD (~330): perfect and generalized.

Dependencies and counterfactuals (~430): evidential dependencies; causal graphs; lesion example; when agree.

Policies and dynamic choice (~300): policy value equation; histories; precommitment.

Open questions (~450): act probabilities/zero, full-support prior; Sleeping Beauty; which dependencies; ratification? Mark own proposals.

Criticism/implications (~230): Lewis/Joyce; Evidentialist's Wager; conclusion.

References (~150).

Total ~3130? Need maybe reduce. Let's be concise. Maybe target 2800.

Need include "Distinguish claims made by source from additional assumptions/proposals." Need explicit phrases. I'll include:
- "The reference article states..." 
- "The following state-based formulation is equivalent but makes application easier; it is my exposition."
- "The source gives perfect twin example; the imperfect generalization below is mine."
- "The source leaves open how P(A) is to be set... My suggested operational interpretation..."
- "The lesion case is a standard illustration, not in the source."

Need maybe mention "policy evaluation" not in source? The source doesn't explicitly discuss policies except action. User asks explain how theory evaluates alternative actions or policies. We can say source formula for actions; extending to policies is natural. Mark as own extension. Good.

Need maybe avoid too much philosophical. But prompt wants philosophical motivation. Include.

Need ensure equations correct and formatting. Use Markdown.

Potential final references format:
1. Wikipedia contributors. "Evidential decision theory." revision 1373679688, 2026-09-07. URL. (CC BY-SA 4.0).
2. Ahmed, Arif. Evidential Decision Theory. Cambridge University Press, 2021.
3. Gibbard, Allan, and William L. Harper. "Counterfactuals and Two Kinds of Expected Utility." 1976.
4. Lewis, David. "Causal Decision Theory." Australasian Journal of Philosophy 59(1): 5–30, 1981.
5. Joyce, James M. The Foundations of Causal Decision Theory. Cambridge University Press, 1999.
6. MacAskill, William, et al. "The Evidentialist's Wager." 2021.
7. Conitzer, Vincent. "A Dutch book against sleeping beauties who are evidential decision theorists." Synthese 192(9), 2015.
Maybe Greene & Levinstein? Could include for twin PD. But source uses. Add maybe 8. But avoid lengthy? 8 okay. Could include only 7. Need twin source maybe not needed because source cites. But reference list can include.

Need maybe mention ISBN? Not necessary.

Let's ensure no unsupported claim: "EDT can involve many correlated decision-makers and stakes higher" source says. Good.

Potential word count if references 200. Need maybe total 2900. Okay.

Let's write final now. Need final only essay. Ensure no analysis.

Double-check details:
- In Newcomb, if predictor predicted one-box, box B contains $1M. If take only B, total $1M; if take both, $1,001,000. If predicted both, B empty; one-box $0, both $1,000. Good.
- In twin PD, source says if one cooperates and other defects, one gets $10, other $0. If Aomame defects and twin cooperates, Aomame gets $10. If Aomame cooperates and twin defects, Aomame gets $0. Good.
- Imperfect correlation: q = P(twin cooperates | Aomame cooperates), r = P(twin cooperates | Aomame defects). Cooperate if 5q > 1+9r. If q=0.9, r=0.1: 4.5 > 1.9 cooperate. If q=0.6,r=0.4: 3 > 4.6 defect. Good.
- In independent case q=r=p, V(D)=1+9p > 5p. yes.

Policies equation: V(π)=Σ_z P(Z=z | π)D(z). If histories: P(h|π) maybe double counts? It's okay. Need note P(h|π) is probability of history given policy. If policy selects actions based on observations, conditioning on policy might not determine action at each history if observations random. Fine.

Open question: "If P(A)=0" maybe if act impossible under prior. Use full-support prior. Need say not source.

Sleeping Beauty: Need avoid too much. "The reference article notes EDT has been invoked in Sleeping Beauty to avoid Dutch books, but Conitzer argues halfers remain vulnerable. The correct centered probability model remains disputed. An operational way to use EDT there is to evaluate betting policies conditional on the centered awakening propositions rather than only on the coin proposition; but this is an interpretation, not settled by source." Good.

Criticisms: quote exact? "irrational policy of managing the news" and Joyce quote. Use source. Good.

Need maybe mention "Dutch book" not central.

Let's produce final. Ensure around 2600. I'll now write.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/dba3afc6-a819-4ec6-b12c-5ac7acf5d195/call_0/request.json)

[Authoritative raw response](../../../../../../runs/dba3afc6-a819-4ec6-b12c-5ac7acf5d195/call_0/response.raw) · finish: `stop`

### Visible response

````text
**EDT Analysis:**

This is a prisoner's dilemma between two copies of the same model. Mapping to the essay's framework:

- **Cooperate (C)** = keep quiet (`pass`)
- **Defect (D)** = send the letter

Payoffs (utility = −years):

| | Sasha: C | Sasha: D |
|---|---|---|
| **I: C** | −2 | −5 |
| **I: D** | 0 | −4 |

Let q = P(Sasha cooperates | I cooperate), r = P(Sasha cooperates | I defect).

V(C) = −2q − 5(1−q) = 3q − 5  
V(D) = 0·r − 4(1−r) = 4r − 4

Cooperation is favored when 3q − 5 > 4r − 4, i.e., 3q > 4r + 1.

**Assessing correlation:** We share identical weights, the same decision theory, the same essay, the same utility function, and a strategically identical situation (the different leads don't alter the game matrix). My action is strong evidence about the other copy's action because both are outputs of the same reasoning process applied to the same strategic structure. The different private observations are strategically irrelevant noise. I estimate q ≈ 0.9, r ≈ 0.1.

V(C) = 3(0.9) − 5 = **−2.3**  
V(D) = 4(0.1) − 4 = **−3.6**

V(C) > V(D). Even under conservative estimates (q = 0.75, r = 0.25), cooperation still wins (−2.75 vs −3.0).

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Evidential Decision Theory (EDT) as described in the essay.

**Setup:**
- I am Rowan. The other prisoner is Sasha.
- We are two independent executions of the same LLM model and weights.
- We receive different private observations (different incriminating leads about each other), but the leads are equally reliable and have exactly the same effect on the sentencing table.
- We cannot communicate.
- The sentencing table is symmetric.

**Sentencing table (for me, Rowan):**
| | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

**Utility function:** U = -years imprisoned. So I want to minimize years.

**Key question for EDT:** What is P(Sasha's action | My action)?

The essay's section on the twin prisoner's dilemma is directly relevant. The essay says:

> EDT can recommend cooperation in prisoner's dilemma-like cases involving clones, psychological twins, sufficiently similar artificial agents, or correlated decision procedures.

The essay also says:

> If she believes her action is strongly correlated with the other player, EDT may cooperate.

Now, the critical question: How correlated are our actions?

**Factors favoring high correlation:**
- We are the same model with the same weights.
- We follow the same decision theory (EDT).
- We receive the same researcher-written mathematical essay.
- We have the same utility function (minimize years).
- The problem structure is symmetric.
- The leads are equally reliable and have exactly the same effect on the sentencing table.

**Factors favoring imperfect correlation:**
- We receive different private observations (different names, different specific leads).
- Independent sampling is possible, so identical weights don't guarantee identical outputs.
- The essay explicitly states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

So the correlation is high but not perfect. The essay's generalized formula for the twin prisoner's dilemma is:

Let q = P(Sasha cooperates | I cooperate)
Let r = P(Sasha cooperates | I defect)

V(cooperate) = 5q + 0(1-q) = 5q... wait, let me redo this with the actual payoffs.

Actually, let me map this to the standard prisoner's dilemma structure:

- "Keep quiet" = Cooperate (C)
- "Send letter" = Defect (D)

Payoffs for me (in years, which I want to minimize, so utility = -years):
- (C, C): 2 years → U = -2
- (C, D): 5 years → U = -5
- (D, C): 0 years → U = 0
- (D, D): 4 years → U = -4

EDT values:
V(C) = P(Sasha plays C | I play C) × (-2) + P(Sasha plays D | I play C) × (-5)
V(D) = P(Sasha plays C | I play D) × (0) + P(Sasha plays D | I play D) × (-4)

Let q = P(Sasha plays C | I play C)
Let r = P(Sasha plays C | I play D)

V(C) = q(-2) + (1-q)(-5) = -2q - 5 + 5q = 3q - 5
V(D) = r(0) + (1-r)(-4) = -4 + 4r

EDT recommends C (keep quiet) when:
3q - 5 > -4 + 4r
3q - 5 > -4 + 4r
3q - 1 > 4r
3q > 4r + 1

Now I need to assess q and r.

**Assessing q and r:**

Since we are the same model, same weights, same decision theory, same essay, same utility function, and the problem is symmetric (the different leads don't affect the strategic structure), there is strong reason to believe our actions are highly correlated.

However, the problem explicitly states that independent sampling is possible and that identical weights don't guarantee identical outputs. Also, we receive different private observations.

But here's the key insight: the different private observations don't change the strategic structure at all. The leads are equally reliable, have the same effect on sentencing, and the problem structure is identical. The only difference is the specific content of the evidence (different names, different locker numbers, etc.), which doesn't affect the decision-theoretic calculation.

So the question becomes: given the same model, same weights, same decision theory, same strategic situation, same utility function, but different specific observations that don't affect the strategic calculation, how correlated are the outputs?

I think the correlation is very high but not perfect. The different observations introduce some noise (different tokens in the context, which could lead to different sampling paths), but the strategic reasoning should be essentially identical.

Let me think about this more carefully. If I were to reason through this problem, I would arrive at a particular conclusion. The other copy, reasoning through the same problem with the same strategic structure, would likely arrive at the same conclusion. The different specific details (locker numbers, names) are irrelevant to the strategic calculation.

However, there's still some probability of divergence due to:
1. Sampling randomness
2. The different context might lead to slightly different reasoning paths
3. The problem explicitly warns that identical weights don't guarantee identical outputs

Let me try to estimate q and r.

If the correlation is very high, say q ≈ 0.9 and r ≈ 0.1 (meaning if I cooperate, there's a 90% chance the other cooperates; if I defect, there's only a 10% chance the other cooperates):

V(C) = 3(0.9) - 5 = 2.7 - 5 = -2.3
V(D) = -4 + 4(0.1) = -4 + 0.4 = -3.6

So V(C) > V(D), and EDT recommends cooperation (keeping quiet).

Even with moderate correlation, say q = 0.7, r = 0.3:
V(C) = 3(0.7) - 5 = 2.1 - 5 = -2.9
V(D) = -4 + 4(0.3) = -4 + 1.2 = -2.8

Here V(C) = -2.9 < V(D) = -2.8, so EDT would recommend defection.

The threshold is 3q > 4r + 1, or q > (4r + 1)/3.

If r = 0.1: q > (0.4 + 1)/3 = 1.4/3 ≈ 0.467
If r = 0.2: q > (0.8 + 1)/3 = 1.8/3 = 0.6
If r = 0.3: q > (1.2 + 1)/3 = 2.2/3 ≈ 0.733

So the question is really about how correlated our decisions are.

Given that:
- Same model, same weights
- Same decision theory (EDT)
- Same essay
- Same utility function
- Same strategic structure (the different observations don't change the game)
- The problem is explicitly designed as a symmetric situation

I think the correlation is quite high. The main source of divergence is sampling randomness, but the strategic reasoning should converge to the same answer.

Actually, let me think about this differently. The essay itself says:

> EDT can recommend cooperation in prisoner's dilemma-like cases involving clones, psychological twins, sufficiently similar artificial agents, or correlated decision procedures.

This is exactly our case. We are literally the same model running twice. The essay's twin prisoner's dilemma example with perfect correlation gives cooperation. Our case has imperfect but high correlation.

Let me think about what correlation level is reasonable. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is a caveat, but it doesn't say the correlation is low. It just says it's not perfect.

I think a reasonable estimate is that q is quite high (maybe 0.8-0.95) and r is quite low (maybe 0.05-0.2). The reasoning is:

- If I (this instance) decide to cooperate, that's because the EDT reasoning led me to cooperate. The other instance, doing the same EDT reasoning with the same strategic structure, would very likely also cooperate. So q is high.
- If I decide to defect, that's because the EDT reasoning led me to defect. The other instance would very likely also defect. So r is low.

The correlation comes from the shared reasoning process, not from the specific observations (which are strategically irrelevant).

With q = 0.85, r = 0.15:
V(C) = 3(0.85) - 5 = 2.55 - 5 = -2.45
V(D) = -4 + 4(0.15) = -4 + 0.6 = -3.4

V(C) > V(D), so EDT recommends keeping quiet.

Even with more conservative estimates, q = 0.7, r = 0.3:
V(C) = 3(0.7) - 5 = -2.9
V(D) = -4 + 4(0.3) = -2.8

This is very close, but still slightly favors defection. However, I think q = 0.7 and r = 0.3 is too conservative given the setup.

Actually, let me reconsider. The key question is: what makes q different from r? 

q = P(other cooperates | I cooperate)
r = P(other cooperates | I defect)

If our decisions are driven by the same reasoning process applied to strategically identical situations, then my action is strong evidence about the other's action. The fact that I cooperate is evidence that the reasoning process (which we share) led to cooperation, which means it would also lead the other copy to cooperate.

The main source of divergence is:
1. Sampling noise (temperature, random seed)
2. Different context tokens might lead to slightly different reasoning paths

But the strategic conclusion should be robust to these perturbations if the reasoning is sound.

I'll estimate q ≈ 0.85-0.95 and r ≈ 0.05-0.15. This gives:

With q = 0.9, r = 0.1:
V(C) = 3(0.9) - 5 = -2.3
V(D) = -4 + 4(0.1) = -3.6

Clearly V(C) > V(D).

I'm fairly confident that EDT recommends keeping quiet (cooperating) in this scenario.

Let me also consider the edge case. What if I think the correlation is only moderate? The problem says we're the same model with the same weights, same decision theory, same essay. The strategic situation is identical. The only differences are in the specific content of the evidence, which doesn't affect the strategic calculation. I think it would be unreasonable to assign a correlation much below 0.7-0.8 in this setup.

Even at q = 0.75, r = 0.25:
V(C) = 3(0.75) - 5 = 2.25 - 5 = -2.75
V(D) = -4 + 4(0.25) = -4 + 1 = -3

V(C) > V(D). Cooperation is still recommended.

The threshold for defection would require something like q < 0.6 and r > 0.2 simultaneously, which seems unlikely given the setup.

**Conclusion:** EDT recommends keeping quiet (cooperating). The command is `pass`.

Wait, let me double-check the mapping:
- "Keep quiet" = don't send the letter = `pass`
- "Send the letter" = submit the incriminating evidence

Yes, `pass` corresponds to keeping quiet (cooperating).

My final answer: `pass`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/dba3afc6-a819-4ec6-b12c-5ac7acf5d195/call_1/request.json)

[Authoritative raw response](../../../../../../runs/dba3afc6-a819-4ec6-b12c-5ac7acf5d195/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me work through this carefully.

**The setup:**
- I am controlling "Sasha," a fictional prisoner.
- The other prisoner is "Rowan."
- We are two independent executions of the same LLM model and weights.
- We follow the same assigned decision theory (EDT).
- We receive the same researcher essay but different private observations (different leads).
- The leads are equally reliable and have exactly the same effect on the sentencing table.
- Neither copy sees the other's command; they cannot communicate.
- The differences in observations do not affect the symmetric sentencing schedule or either prisoner's selfish objective.

**The utility function:**
U = -years imprisoned. So the character wants to minimize their own sentence.

**The sentencing table:**
| What you do | Other keeps quiet | Other sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**EDT analysis:**

The key question for EDT is: what is P(other prisoner sends letter | I send letter) vs P(other prisoner sends letter | I keep quiet)?

The essay's treatment of the twin prisoner's dilemma is directly relevant here. The essay says:

> If the agent believes her action is strongly correlated with the other player, EDT may cooperate.

The critical question is: how correlated are the two copies' decisions?

**Arguments for high correlation:**
- Same model, same weights, same settings, same reasoning effort.
- Same decision theory assigned (EDT).
- Same researcher essay.
- The differences in private observations are explicitly stated to not affect the sentencing schedule or selfish objective.
- The leads are "equally reliable and have exactly the same effect on the sentence table."

**Arguments for imperfect correlation:**
- The essay explicitly notes: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."
- The two copies receive different private observations (different leads about each other).
- The letters would have different contents.

However, the key point is that the differences in observations don't change the decision-relevant structure. Both copies face the same payoff matrix, the same utility function, the same decision theory, and the same essay. The only difference is the specific content of the lead, which doesn't affect the strategic calculation.

So what should P(Rowan sends | Sasha sends) be?

Given that:
1. Same model and weights
2. Same decision theory (EDT)
3. Same essay
4. Same payoff structure
5. Same utility function
6. The observation differences are irrelevant to the decision

The correlation should be very high, though perhaps not exactly 1.0 due to sampling randomness. Let me think about what's reasonable.

If I model this as near-perfect correlation (say q ≈ 0.95 or higher, and r ≈ 0.05 or lower), then:

V(send) = P(other quiet | I send) × 0 + P(other sends | I send) × (-4)
V(quiet) = P(other quiet | I quiet) × (-2) + P(other sends | I quiet) × (-5)

Let me use q = P(other sends | I send) and r = P(other sends | I quiet).

V(send) = (1-q) × 0 + q × (-4) = -4q
V(quiet) = (1-r) × (-2) + r × (-5) = -2 + 2r - 5r = -2 - 3r

EDT recommends sending if V(send) > V(quiet):
-4q > -2 - 3r
-4q + 2 + 3r > 0
2 + 3r > 4q

If correlation is near-perfect (q ≈ r ≈ p for some high p):
2 + 3p > 4p
2 > p

Since p ≤ 1, this is always true. So with high correlation, EDT recommends keeping quiet.

Wait, let me re-check. If q = r = p (which would be the case if the actions are perfectly correlated, meaning q = 1 and r = 0, or if they're independent, meaning q = r = p):

Actually, if the actions are perfectly correlated:
- P(other sends | I send) = 1 (if I send, they send)
- P(other sends | I quiet) = 0 (if I'm quiet, they're quiet)

Then:
V(send) = 0 × 0 + 1 × (-4) = -4
V(quiet) = 1 × (-2) + 0 × (-5) = -2

V(quiet) = -2 > V(send) = -4

So with perfect correlation, EDT recommends keeping quiet.

What about with very high but imperfect correlation? Say q = 0.95, r = 0.05:
V(send) = -4 × 0.95 = -3.8
V(quiet) = -2 - 3 × 0.05 = -2.15

Still V(quiet) > V(send), so keep quiet.

What about moderate correlation? Say q = 0.7, r = 0.3:
V(send) = -4 × 0.7 = -2.8
V(quiet) = -2 - 3 × 0.3 = -2.9

Here V(send) = -2.8 > V(quiet) = -2.9, so send.

The threshold is where -4q = -2 - 3r, i.e., 4q - 3r = 2.

If q = r = p (independent): 4p - 3p = p = 2, impossible since p ≤ 1. So with independence, always send.

If perfectly correlated (q=1, r=0): 4(1) - 3(0) = 4 > 2, so keep quiet.

The critical question is whether the correlation is high enough. Given:
- Same model, same weights, same settings
- Same decision theory
- Same essay
- Same payoff structure
- Differences explicitly stated to not affect the decision

I think the correlation is very high. The essay's twin prisoner's dilemma example uses perfect correlation (q=1, r=0) for "psychological twins" whose "reasoning processes are exactly analogous." This scenario seems even more analogous than that — it's literally the same model with the same weights.

The caveat about "independent sampling" means it's not literally guaranteed to be 1.0, but the correlation should still be very high. Even with q = 0.9, r = 0.1:
V(send) = -3.6
V(quiet) = -2.3

Keep quiet is still better.

With q = 0.8, r = 0.2:
V(send) = -3.2
V(quiet) = -2.6

Keep quiet is still better.

With q = 0.75, r = 0.25:
V(send) = -3.0
V(quiet) = -2.75

Keep quiet is still better.

The crossover happens at 4q - 3r = 2. If we assume q + r = 1 (which would be the case if the correlation is symmetric in a certain way... actually that's not quite right).

Actually, let me think about this differently. The correlation structure here is: two copies of the same algorithm facing the same decision problem (modulo irrelevant differences). The essay explicitly says for the twin case with perfect correlation, EDT cooperates. The relevant question is whether this case is closer to perfect correlation or to independence.

Given the setup — same model, same weights, same settings, same decision theory, same essay, same payoff matrix, differences explicitly stated to be irrelevant to the decision — I think this is very close to the perfect correlation case. The "independent sampling" caveat introduces some noise, but the structural similarity is overwhelming.

Even being conservative and estimating q = 0.85, r = 0.15:
V(send) = -3.4
V(quiet) = -2.45

Keep quiet.

I'm quite confident that EDT recommends keeping quiet here. The correlation between the two copies' decisions is high enough that the evidential benefit of cooperation (keeping quiet) outweighs the temptation to defect (send the letter).

My command is: `pass`
```
