# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a theory of rational choice that evaluates actions by their *evidential import*. The central idea, as stated in the reference article, is that an agent should choose the action with the highest *news value*: the action such that, if the agent learned as news that she had performed it, the expected outcome would be best. In a memorable slogan, EDT recommends doing “what you most want to learn that you will do” (Ahmed 2021, quoted in Wikipedia contributors 2026).

This makes EDT subtly different from ordinary expected-utility reasoning as it is often informally presented. Standard decision theory is sometimes described as choosing the act that causes the best expected outcome. EDT need not ask whether the act *causes* the outcome. It asks whether the act is *evidence* for good outcomes. If performing \(A\) would be strong evidence that something desirable is true or will occur, then \(A\) receives high evidential expected utility, even if \(A\) does not bring that desirable fact about causally.

The reference article contrasts EDT with causal decision theory (CDT). CDT evaluates acts by their expected causal efficacy, using counterfactual probabilities of the form \(P(A \mathrel{\Box\rightarrow} O_j)\), the probability of outcome \(O_j\) in the counterfactual situation where \(A\) is performed. EDT instead uses ordinary conditional probabilities \(P(O_j \mid A)\). The two coincide in many ordinary cases, but they diverge in famous philosophical examples such as Newcomb’s paradox and twin prisoner’s dilemma.

Below I develop the formal rule, explain how EDT treats dependencies and counterfactuals, and discuss how it can be extended to policies. I also identify points where the source is silent, especially the treatment of zero-probability actions and the operational meaning of conditioning on one’s own choice. Some of the operational suggestions are my own.

---

## 1. Formal definition

Let \(\mathcal{A}\) be the set of available acts. For EDT, an act \(A\) is best treated as a proposition: “the agent performs \(A\).” Let \(\{O_j\}\) be a partition of possible outcomes relevant to the agent’s preferences. The agent has a subjective probability function \(P\) over propositions involving acts, states of the world, and outcomes. The agent also has a desirability or utility function \(D\), where \(D(O_j)\) is the value of outcome \(O_j\).

The reference article gives the standard EDT value function, attributed to Gibbard and Harper (1976):

\[
V(A)=\sum_{j} P(O_j \mid A) D(O_j).
\]

This is the conditional expected desirability of outcome \(O_j\), given that the agent performs \(A\). If \(P(A)>0\), then

\[
P(O_j \mid A)=\frac{P(O_j \land A)}{P(A)}.
\]

So equivalently,

\[
V(A)=\frac{1}{P(A)}\sum_j P(O_j \land A)D(O_j).
\]

EDT then prescribes:

\[
A^* \in \arg\max_{A\in\mathcal{A}} V(A).
\]

If outcomes are continuous, the sum becomes an integral:

\[
V(A)=\int u(w)\,dP(w\mid A),
\]

where \(w\) ranges over possible worlds or states and \(u(w)\) is the utility of world \(w\).

The reference article also gives the causal decision theory analogue:

\[
U(A)=\sum_{j} P(A \mathrel{\Box\rightarrow} O_j) D(O_j).
\]

Here \(A \mathrel{\Box\rightarrow} O_j\) means something like: in the relevant counterfactual world where the agent performs \(A\), outcome \(O_j\) occurs. In modern causal-model language, CDT often uses an interventionist probability such as \(P(O_j \mid do(A))\), whereas EDT uses the observational conditional \(P(O_j \mid A)\). This distinction is central.

---

## 2. What EDT is doing: conditioning, not intervening

The formal difference between EDT and CDT can be understood through the distinction between *conditioning* and *intervening*.

Suppose an outcome \(O\) depends on some background state \(S\). Then EDT computes

\[
P(O \mid A)=\sum_s P(O \mid A,s)P(s \mid A).
\]

The important term is \(P(s \mid A)\): the probability of background state \(s\) given that the agent performs \(A\). If \(A\) is correlated with \(S\), EDT takes that seriously. The action may be evidence about \(S\), even if it does not causally influence \(S\).

This is why EDT is sensitive to predictors, copies, psychological twins, common causes, and logical or statistical correlations. If the agent’s action is evidence that some favorable state obtains, EDT gives the action credit for that evidence.

By contrast, a causal theory would ask what would happen if we *intervened* to make \(A\) true. In a causal graph, intervening on \(A\) cuts incoming arrows into \(A\). The resulting probability, \(P(O \mid do(A))\), may be very different from \(P(O \mid A)\) when \(A\) has common causes or is predicted by other variables.

For example, suppose a genetic lesion \(L\) causes both a desire to smoke and a high risk of cancer. Smoking itself does not cause cancer in this hypothetical case. Then \(P(\text{cancer} \mid \text{smoke})\) may be high, because smoking is evidence of the lesion. EDT may therefore assign low value to smoking if cancer is bad enough. But \(P(\text{cancer} \mid do(\text{smoke}))\) would not be elevated by the lesion, since forcing someone to smoke does not produce the lesion. CDT would evaluate smoking only by its direct consequences, such as enjoyment. This example is not in the source, but it illustrates the general difference.

Thus EDT treats relevant dependencies broadly: any probabilistic dependence encoded in the agent’s credence function can affect the value of an act. It does not require that the dependence be causal.

---

## 3. Evaluating policies

The reference article focuses mainly on single acts, but decision problems often ask us to choose policies: rules, algorithms, or plans that map future observations or internal states to actions. EDT can handle policies by treating a policy as a higher-level act.

Let \(\Pi\) be a set of possible policies. For a policy \(\pi\), define the proposition \([\pi]\): “the agent adopts and implements policy \(\pi\).” Then EDT can assign

\[
V(\pi)=\sum_j P(O_j \mid \pi)D(O_j).
\]

The policy with highest \(V(\pi)\) is chosen.

This is a natural extension, though the source does not develop it explicitly. It matters because in many Newcomb-like problems, the predictor may predict not merely a single physical movement but the agent’s decision procedure. If an agent can choose between a one-boxing policy and a two-boxing policy, EDT evaluates the policy by the news value of having that policy. If a reliable predictor predicted that the agent would use a one-boxing policy, then adopting that policy is evidence of a full box.

For stochastic policies, one must be careful. Suppose policy \(\pi\) randomizes between actions. There are at least two options:

1. Evaluate the proposition “I adopt randomized policy \(\pi\).”
2. Evaluate the realized action after the randomization, conditioning on the outcome of the randomizer.

Which is appropriate depends on the decision problem. If the predictor predicts the adoption of the randomized policy, the first is natural. If the predictor predicts the realized action, the second may be more appropriate. In my view, the cleanest operational rule is to evaluate the object actually chosen by the agent. If the agent chooses a policy, evaluate the policy. If the agent chooses a realized action after randomization, evaluate that action, conditional on the randomization result and all other relevant evidence.

---

## 4. Example: Newcomb’s paradox

The reference article discusses Newcomb’s paradox in detail. There is a predictor with 99% accuracy. Box A visibly contains \$1,000. Box B is opaque. If the predictor predicted that the player will take both boxes, box B is empty. If the predictor predicted that the player will take only box B, box B contains \$1,000,000. The player chooses after the predictor has made its prediction, but without knowing what it predicted.

Let \(B\) be the act of taking only box B, and \(A+B\) the act of taking both boxes. EDT computes:

\[
\begin{aligned}
V(B)
&= P(\text{\$1M in B} \mid B)\cdot \$1{,}000{,}000 \\
&\quad + P(\text{B empty} \mid B)\cdot \$0 \\
&= 0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0 \\
&= \$990{,}000.
\end{aligned}
\]

For two-boxing:

\[
\begin{aligned}
V(A+B)
&= P(\text{\$1M in B} \mid A+B)\cdot \$1{,}001{,}000 \\
&\quad + P(\text{B empty} \mid A+B)\cdot \$1{,}000 \\
&= 0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot \$1{,}000 \\
&= \$11{,}000.
\end{aligned}
\]

Since \(V(B) > V(A+B)\), EDT recommends one-boxing.

The reason is purely evidential. Taking only box B is excellent news about what the predictor predicted. Taking both boxes is bad news about the content of box B. EDT does not require that the current choice causally changes the predictor’s earlier prediction. It only requires that the choice is strong evidence about that prediction.

CDT, as the source notes, recommends two-boxing. Once the predictor has already made its prediction, the contents of box B are fixed. From a causal perspective, taking both boxes adds the visible \$1,000 without changing whether box B contains \$1,000,000. So CDT sees two-boxing as dominant.

This is the classic divide: EDT chooses the act that is the best news; CDT chooses the act with the best causal consequences.

---

## 5. Example: twin prisoner’s dilemma

The source also discusses a twin prisoner’s dilemma. Aomame and her psychological twin are in separate rooms. They cannot communicate. Their reasoning processes are exactly analogous. Payoffs are:

- Both cooperate: each receives \$5.
- Both defect: each receives \$1.
- One cooperates, one defects: cooperator receives \$0, defector receives \$10.

Assume Aomame cares only about her own payout. EDT evaluates Aomame’s choice by conditioning on what her twin will do.

If the twins are perfectly psychologically symmetric and reason identically, then Aomame’s choice is perfect evidence of her twin’s choice:

\[
P(\text{twin cooperates} \mid \text{Aomame cooperates}) = 1,
\]

\[
P(\text{twin defects} \mid \text{Aomame defects}) = 1.
\]

Then:

\[
\begin{aligned}
V(\text{cooperate})
&= P(\text{twin cooperates} \mid C)\cdot \$5 \\
&\quad + P(\text{twin defects} \mid C)\cdot \$0 \\
&= 1\cdot \$5 + 0\cdot \$0 \\
&= \$5.
\end{aligned}
\]

And:

\[
\begin{aligned}
V(\text{defect})
&= P(\text{twin cooperates} \mid D)\cdot \$10 \\
&\quad + P(\text{twin defects} \mid D)\cdot \$1 \\
&= 0\cdot \$10 + 1\cdot \$1 \\
&= \$1.
\end{aligned}
\]

So EDT recommends cooperation.

This example is useful because it shows how EDT handles non-causal correlations between agents. Aomame’s choice does not cause her twin’s choice. But it is conclusive evidence of her twin’s choice, given the assumed psychological symmetry.

We can generalize slightly. Suppose the correlation is not perfect. Let \(q\) be the probability that the twin makes the same choice as Aomame. Then:

\[
V(C)=5q,
\]

\[
V(D)=10(1-q)+1q=10-9q.
\]

EDT recommends cooperation when

\[
5q > 10-9q,
\]

so

\[
14q > 10,
\]

\[
q > \frac{5}{7}\approx 0.714.
\]

Thus, in an unfamiliar case with imperfect correlation, EDT gives a clear quantitative test: cooperate if the probability that the other agent mirrors your choice is high enough. This threshold calculation is my own elaboration, but it follows directly from the EDT formula given in the source.

---

## 6. Dependencies, counterfactuals, and “news”

EDT’s treatment of counterfactuals is unusual. In ordinary language, “what would happen if I did \(A\)?” often sounds causal. EDT interprets it more like: “what should I expect, conditional on learning that I do \(A\)?”

This is why the source describes EDT as choosing the action with the highest news value. If you received a message saying, “You will perform \(A\),” how good would the world look conditional on that message? EDT chooses the act whose message is best.

The relevant dependencies are therefore all dependencies captured by the agent’s conditional probabilities. These may include:

1. **Predictive dependencies**: an agent’s action is predicted by another agent, machine, or historical pattern.
2. **Common-cause dependencies**: an action and an outcome share a common cause.
3. **Logical or computational dependencies**: the agent’s decision is correlated with the decision of another agent running the same or similar reasoning.
4. **Self-locating or indexical dependencies**: the action may be evidence about which observer-moment or branch the agent is in, as in discussions of the Sleeping Beauty problem.

The source notes that EDT has been applied to the Sleeping Beauty problem to avoid Dutch-book arguments, but also that Vincent Conitzer has argued that halfers can still be Dutch-booked even when using EDT (Conitzer 2015, cited in Wikipedia contributors 2026). This remains an area of dispute rather than a settled advantage of EDT.

One important caution: EDT can reward actions that are merely symptoms of good states. If carrying an umbrella is evidence that it will rain, EDT may favor carrying an umbrella if rain is desirable, even if carrying the umbrella does not cause rain. This is not a problem if the agent truly values the evidence itself, but it becomes problematic if the goal is to bring about good outcomes rather than merely to be correlated with them.

---

## 7. Open questions and an operational interpretation

The reference article gives the central EDT formula but leaves several operational questions open.

First, conditional probability requires \(P(A)>0\). But in deliberate choice, an agent may be nearly certain what she will do. If \(P(A)=1\), then \(P(O \mid A)=P(O)\), and the EDT comparison may collapse. If \(P(A)=0\), the conditional probability is undefined.

A reasonable operational interpretation, which I add to the source’s basic formula, is to use a *deliberative probability distribution* with full support over available acts. During deliberation, the agent should assign a small positive probability to each available action, even if she expects to perform one of them. If her prior distribution assigns zero probability to some act, she can replace it with a small perturbation:

\[
P_\varepsilon(A)= (1-\varepsilon)P(A)+\varepsilon Q(A),
\]

where \(Q\) is a full-support distribution over acts. She can then compute \(P_\varepsilon(O_j \mid A)\) and take the limit as \(\varepsilon \to 0\), if the limit exists. This gives a way to define EDT values even for acts that initially have zero probability.

Second, the source does not fully specify what evidence should be held fixed when conditioning on \(A\). The natural rule is to condition on the act proposition together with the agent’s total admissible evidence, except perhaps evidence that is itself constituted by the act. Formally, if \(E\) is the agent’s evidence, one might compute

\[
V(A)=\sum_j P(O_j \mid A \land E)D(O_j).
\]

This makes explicit that EDT is not merely conditioning on \(A\) in isolation, but on \(A\) as added to what the agent already knows.

Third, EDT can depend heavily on the agent’s probability model. If the agent overestimates a correlation, EDT may recommend an action that is actually poor. But this is not unique to EDT; CDT also depends on correct causal beliefs. EDT’s distinctive vulnerability is that it can be led astray by merely evidential correlations, even when the agent’s probabilities are accurate.

---

## 8. Criticism and philosophical significance

The reference article includes two important criticisms. David Lewis characterized EDT as “an irrational policy of managing the news” (Lewis 1981, cited in Wikipedia contributors 2026). James Joyce wrote that rational agents choose acts “on the basis of their causal efficacy, not their auspiciousness” (Joyce 1999, cited in Wikipedia contributors 2026).

These criticisms target EDT’s willingness to choose acts that are good evidence but bad interventions. In smoking-lesion-style cases, EDT may avoid an action because it is evidence of a bad condition, even though the action itself is harmless or beneficial. CDT would say that the agent should ignore the bad news and take the beneficial action.

Defenders of EDT can respond in two ways. First, in cases like Newcomb’s paradox and twin prisoner’s dilemma, EDT appears to get attractive results: one-boxing yields the million dollars, and cooperation yields the higher correlated payoff. Second, as the source notes, if many decision-makers are correlated, EDT may have especially high stakes because one’s action can be evidence about many other actions. This is the idea behind “the evidentialist’s wager”: even if one is not fully confident in EDT, acting as if EDT may be worthwhile when one’s choice is correlated with many other agents’ choices (MacAskill et al. 2021, cited in Wikipedia contributors 2026).

This makes EDT philosophically important for questions involving predictors, simulated agents, copies, coordination, and acausal trade. If rational agents should care about the global pattern of decisions, not only local causal consequences, EDT captures something plausible.

Still, EDT remains controversial because it blurs the line between choosing good evidence and causing good outcomes.

---

## 9. Conclusion

Evidential decision theory evaluates actions by conditional expected utility:

\[
V(A)=\sum_j P(O_j \mid A)D(O_j).
\]

It chooses the act that would be the best news. This makes EDT especially responsive to predictive, correlational, and logical dependencies. It recommends one-boxing in Newcomb’s paradox and cooperating in twin prisoner’s dilemma when one’s choice is strong evidence of another agent’s choice.

The theory’s strength is also its weakness. By treating actions as evidence, EDT may favor actions that are auspicious rather than effective. CDT objects that rational choice should be about bringing about good outcomes, not merely being correlated with them. A careful EDT practitioner must therefore specify the relevant act propositions, outcome partition, probability model, and policy level with care. Where the source leaves matters open—especially concerning zero-probability acts and policy evaluation—a full-support deliberative interpretation provides a workable way to apply EDT to unfamiliar cases.

---

## References

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge University Press.

Conitzer, Vincent. 2015. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192 (9): 2887–2899.

Gibbard, Allan, and William L. Harper. 1976. “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*, 125–62.

Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. 2021. “The Evidentialist’s Wager.” Global Priorities Institute.

Wikipedia contributors. 2026. “Evidential Decision Theory.” Wikipedia, revision 1373679688. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688. Licensed under CC BY-SA 4.0.