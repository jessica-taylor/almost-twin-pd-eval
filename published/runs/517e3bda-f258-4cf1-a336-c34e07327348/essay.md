# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a school of decision theory that evaluates actions by their *news value*: the expected desirability of the outcome one would anticipate on learning that one had performed the action. The supplied reference article summarizes the slogan as “do what you most want to learn that you will do” and traces the formal contrast with causal decision theory (CDT) to Gibbard and Harper’s distinction between two kinds of expected utility (Ahmed 2021; Gibbard & Harper 1976). EDT says that a rational agent should choose the act whose occurrence would be the best evidence of a good outcome. CDT says that the agent should choose the act that would causally bring about the best outcome. The two often agree, but they diverge in predictor problems, twin cases, and other situations where choices are strongly evidentially correlated with outcomes.

This essay gives a formal statement of EDT, explains how it evaluates acts and policies, and describes its treatment of dependencies and counterfactuals. I distinguish claims found in the reference article from additional operational proposals that I think make EDT usable in unfamiliar cases.

---

## 1. The EDT calculation

Let \(\mathcal A\) be a set of available acts, and let \(\{O_j\}\) be a partition of possible outcomes. Let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). The agent has a probability function \(P\) representing her credences over propositions involving acts, states, and outcomes. EDT assigns to each act \(a\) the value

\[
V(a)=\sum_j P(O_j\mid A=a)D(O_j),
\]

where \(A=a\) is the proposition that the agent performs act \(a\). Equivalently,

\[
V(a)=\mathbb E[D(O)\mid A=a].
\]

More explicitly, if the agent has background evidence \(K\), we should write

\[
V_K(a)=\sum_j P(O_j\mid A=a,K)D(O_j).
\]

If one models background states \(S_i\) that, together with the act, determine the outcome, with utility \(u(a,S_i)\), then

\[
V_K(a)=\sum_i P(S_i\mid A=a,K)u(a,S_i).
\]

For continuous outcome spaces, the sum becomes an integral. I assume here that utilities are bounded or that the relevant expectations exist. The EDT choice rule is: choose an act \(a^*\) with maximal \(V_K(a)\).

The reference article contrasts this with CDT’s counterfactual expected utility:

\[
U(a)=\sum_j P(A=a\mathrel{\Box\rightarrow}O_j)D(O_j),
\]

where \(A=a\mathrel{\Box\rightarrow}O_j\) means that outcome \(O_j\) would obtain in the counterfactual situation in which \(a\) is performed. In modern causal-model language, CDT uses something like \(P(O_j\mid do(A=a))\), while EDT uses the observational conditional \(P(O_j\mid A=a)\). These coincide when the act is probabilistically independent of the background variables relevant to the outcome, but not otherwise. The article states that this non-equivalence is the source of the differing recommendations of EDT and CDT.

The essential philosophical point is that EDT does not first ask whether the act causes the outcome. It asks what the act indicates. If performing \(a\) is strong evidence that the world is in a high-utility state, EDT gives \(a\) high value even if \(a\) has no causal influence on that state.

---

## 2. Acts, policies, and randomization

The source mainly evaluates single acts. Many decision problems, however, concern policies: plans, algorithms, or rules mapping observations to actions. A natural EDT extension is to treat a policy \(\pi\) as another proposition, namely “the agent adopts or implements \(\pi\).” Then

\[
V_K(\pi)=\sum_j P(O_j\mid \Pi=\pi,K)D(O_j),
\]

where \(\Pi=\pi\) is the proposition that the agent follows policy \(\pi\).

If \(\pi\) specifies actions conditional on signals, the probability term includes the chances of receiving those signals and the outcomes that follow. For example, if a policy is “cooperate if the other agent’s signal is friendly, otherwise defect,” EDT conditions on the whole policy being adopted, not merely on one branch being reached.

For randomized policies, one must distinguish the news that the policy was adopted from the news of the realized action. Suppose a policy selects act \(a\) with probability \(\mu(a)\). If the randomizing device is independent of everything relevant except the realized act, and if adopting the randomization procedure itself carries no further evidence, then the ex ante value of the randomized policy is

\[
V_K(\pi_\mu)=\sum_a \mu(a)V_K(a).
\]

But EDT is sensitive to evidence, so adopting a randomization procedure may itself carry information—about one’s type, about predictors’ expectations, or about correlated agents—and that information belongs in \(P(O\mid \Pi=\pi,K)\). This policy formulation is not emphasized in the source; I offer it as a conservative extension of the article’s act-based rule.

---

## 3. Examples

### Newcomb’s problem

The reference article describes Newcomb’s problem. A predictor has filled an opaque box B: it contains $1,000,000 if the predictor predicted that the agent would take only B, and $0 if the predictor predicted that the agent would take both boxes. A transparent box A always contains $1,000. The agent may take only B or both A and B. Suppose the predictor is correct with probability \(0.99\).

EDT computes:

\[
\begin{aligned}
V(\text{one-box}) 
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0 \\
&=\$990{,}000,\\[4pt]
V(\text{two-box}) 
&=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000 \\
&=\$11{,}000.
\end{aligned}
\]

Thus EDT recommends one-boxing. The article states that CDT recommends two-boxing because the predictor has already acted, so taking both boxes adds $1,000 regardless of what is in B.

More generally, if the predictor is correct with probability \(p\) and the large prize is \(M\), then

\[
V(\text{one-box})=pM,
\]

while

\[
\begin{aligned}
V(\text{two-box})
&=(1-p)(M+1000)+p(1000)\\
&=1000+(1-p)M.
\end{aligned}
\]

One-boxing is EDT-optimal exactly when

\[
pM>1000+(1-p)M,
\]

or

\[
p>\frac12+\frac{1000}{2M}.
\]

For \(M=\$1{,}000{,}000\), this threshold is just above \(0.5\). The example shows how EDT uses the conditional dependence between the agent’s choice and the predictor’s earlier prediction.

This also explains why EDT can reject a dominance argument. Two-boxing yields $1,000 more than one-boxing for each fixed content of B. But EDT does not hold the probability of B’s content fixed across acts: one-boxing is strong evidence that B contains $1,000,000, while two-boxing is strong evidence that B is empty.

### Twin prisoner’s dilemma

The article’s second example is a twin prisoner’s dilemma. Aomame and her exact psychological twin choose separately whether to cooperate or defect. Payoffs are: both cooperate, $5 each; both defect, $1 each; one cooperates and the other defects, $10 to the defector and $0 to the cooperator.

Because the twins’ reasoning processes are exactly analogous, the article assumes

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]

and

\[
P(\text{twin defects}\mid \text{Aomame defects})=1.
\]

Then

\[
V(C)=1\cdot \$5+0\cdot \$0=\$5,
\]

while

\[
V(D)=0\cdot \$10+1\cdot \$1=\$1.
\]

EDT recommends cooperation. The source does not explicitly give CDT’s verdict here, but a standard causal treatment would usually treat the twin’s action as causally independent and therefore recommend defection, since defecting yields more than cooperating for each fixed choice by the twin.

The EDT calculation can be generalized. Suppose the agent believes that the probability the twin matches her choice is \(q\), symmetrically. Then

\[
V(C)=5q,
\]

and

\[
V(D)=1q+10(1-q)=10-9q.
\]

Cooperation is EDT-optimal when

\[
5q>10-9q,
\]

that is,

\[
q>\frac{5}{7}.
\]

If the agents are independent and conditional correlation is weak, EDT can recommend defection. EDT is therefore not a general principle of cooperation; it is a principle of maximizing conditional expected utility given whatever evidential connections the agent’s probability model contains. This threshold calculation is my extension of the source’s perfect-correlation example.

---

## 4. Dependencies and counterfactuals

EDT treats probabilistic dependencies as decision-relevant. If \(A\) is correlated with a state \(S\) that affects outcome \(O\), then \(P(S\mid A)\) may differ from \(P(S)\), and EDT uses \(P(S\mid A)\). The correlation may arise from prediction, common causes, shared algorithms, psychological similarity, or selection effects. EDT does not ask whether the agent’s act causally influences \(S\). In Newcomb’s problem, the act is evidence about a past prediction. In the twin case, it is evidence about a simultaneous but causally separate decision.

A useful way to see the contrast is with exogenous background variables \(U\). Suppose the outcome is determined by the act and background: \(O=o(a,U)\). EDT gives

\[
V(a)=\sum_u P(U=u\mid A=a)D(o(a,u)).
\]

An interventionist CDT calculation would keep the distribution of exogenous variables fixed under the intervention:

\[
U(a)=\sum_u P(U=u)D(o(a,u)).
\]

The two coincide if \(A\perp U\). They differ when the agent’s act is evidence about \(U\). Newcomb’s predictor creates exactly such dependence: \(U\) includes the predictor’s prediction or the box’s content, and \(P(U\mid A)\) is sharply different from \(P(U)\).

The counterfactuals implicit in EDT are evidential rather than interventionist. EDT asks: “If I were to learn that I had done \(a\), what should I expect?” This often corresponds to a backtracking reading: if I one-box, then probably the predictor predicted one-box. CDT asks: “If I were made to do \(a\), while the relevant causal past is held fixed, what would happen?” That difference explains why EDT can recommend an act that is good news but, according to CDT, causally ineffective.

One practical caution follows: EDT should condition on the agent’s total evidence. If an action is merely a proxy for evidence already available, omitting that evidence can produce misleading verdicts. For example, taking an umbrella is evidence of rain only because the agent has seen a rainy forecast. If the forecast is part of the evidence \(K\), EDT evaluates acts conditional on the forecast; it should not treat umbrella-taking as mysteriously bad news. This point is not explicit in the source, but it is essential for applying EDT carefully.

---

## 5. Open questions and operational conventions

The reference article leaves several operational questions open.

First, what if the agent assigns probability zero to an alternative act? If the agent is certain she will one-box, then \(P(\text{two-box})=0\), and \(P(O\mid \text{two-box})\) is undefined under the usual ratio definition. Yet decision theory must compare alternatives. I propose treating EDT’s conditionals as deliberational conditionals: probabilities are evaluated in a representation of the agent’s uncertainty before her decision is settled, or as limits of models with small decision noise. For example, assign each feasible act probability at least \(\varepsilon\), compute \(V_\varepsilon(a)\), and take a stable limit as \(\varepsilon\to0\). If the limit depends on how the noise is introduced, the original problem is under-specified. This “trembling-hand” convention is not in the source, but it preserves the intended evidential comparisons.

Second, which dependencies count? The EDT answer is: all dependencies represented in the agent’s probability function, relative to her evidence. If the agent later learns a variable that screens off the correlation—she learns whether the predictor predicted one-box, whether she has a lesion, or what forecast was issued—then EDT recalculates conditional on that fact. This makes EDT highly context-sensitive. It also explains why EDT may give different advice before and after learning a screening variable.

Third, how should logical or algorithmic correlations be represented? The twin case assumes exact psychological similarity. In real cases, correlations may be approximate. A reasonable operational approach is to assign joint probabilities to the relevant agents’ choices based on empirical reliability, symmetry, or known common source code, and then compute the relevant conditional probabilities. If two algorithms are known to be identical and receive symmetric inputs, assigning probability near one to matching choices is natural; if the connection is weak, the conditional probability should be correspondingly weak. The source assumes perfect correlation in the twin example; the general probabilistic treatment is my proposal.

Fourth, self-locating problems such as Sleeping Beauty remain unsettled. The source notes that EDT has been used in Dutch-book arguments concerning Sleeping Beauty, but also that Conitzer challenges the claim that halfers can fully avoid Dutch books by adopting EDT. The deeper issue is that EDT presupposes probabilities over propositions, while Sleeping Beauty turns on centered propositions: “it is Monday,” “it is Tuesday,” “I am awake now.” EDT can evaluate a betting policy at an awakening by conditioning on the agent’s current experience and the proposed policy, but it does not by itself decide whether the conditional probability of heads should be \(1/2\) or \(1/3\). The reference article leaves this contested; I regard EDT as needing an independent account of centered credence before it can be applied definitively.

---

## 6. Criticism, motivations, and the evidentialist’s wager

The reference article includes two important criticisms. David Lewis characterized EDT as “an irrational policy of managing the news,” and James Joyce argued that rational agents choose acts for their causal efficacy, not their auspiciousness. These criticisms target cases in which an act is good evidence for a good outcome but does not help produce it.

A standard illustration, not mentioned in the source, is the smoking-lesion problem. Suppose a lesion causes both cancer and a tendency to smoke, but smoking itself does not cause cancer. Smoking gives pleasure. Since smoking is evidence of the lesion, \(P(\text{cancer}\mid \text{smoke})\) may be high, so EDT may recommend not smoking. Critics say this is irrational: refraining from smoking does not prevent the lesion or the cancer; it merely makes the agent’s news better. If the agent knows her lesion status, EDT conditional on that status may recommend smoking, but the unknown-status recommendation is what many find objectionable.

The source also mentions a supporting argument sometimes called the evidentialist’s wager. Even if one is uncertain whether EDT is correct, it may be prudent to act as if EDT is true in worlds where many decision-makers are strongly correlated. In such worlds, EDT can coordinate behavior and capture large cooperative gains, while CDT may defect or free-ride. This argument does not prove EDT is true; it is a pragmatic reason to give EDT weight in high-stakes correlated settings.

---

## 7. Using EDT in practice

A reader wanting to apply EDT to an unfamiliar problem can use the following procedure.

1. List the feasible acts or policies. Include relevant observations and decision rules if evaluating a policy.
2. Specify outcomes and assign utilities \(D\).
3. State all available evidence \(K\).
4. Build a probability model over acts, states, and outcomes, including predictors, correlations, and other agents’ likely actions.
5. Compute

\[
V_K(a)=\sum_j P(O_j\mid A=a,K)D(O_j)
\]

for each act, or

\[
V_K(\pi)=\sum_j P(O_j\mid \Pi=\pi,K)D(O_j)
\]

for each policy.
6. Choose the act or policy with the greatest value. If conditionals involve probability-zero acts, use a deliberational or limiting convention. If the result is sensitive to modeling choices, report the sensitivity.

This procedure makes EDT precise enough for many applications, but it also reveals the theory’s controversial commitment: the probabilities used are ordinary evidential conditionals, not causal interventions.

---

## Conclusion

EDT evaluates actions by the expected desirability of the outcomes they evidence. Its core formula,

\[
V(a)=\sum_j P(O_j\mid A=a)D(O_j),
\]

is simple, but its implications are radical in cases involving predictors, twins, and correlated decision-makers. The reference article’s central examples—Newcomb’s problem and the twin prisoner’s dilemma—show EDT favoring one-boxing and cooperation because those acts are strong evidence of favorable outcomes. The theory diverges from CDT because it conditions on acts rather than intervening on them. To apply EDT carefully, one must specify total evidence, model evidential dependencies, and handle zero-probability counterfactuals with a deliberational convention. Whether one accepts EDT depends on a deeper question: should rational choice track what would be good news, or what would causally bring about good? EDT gives the first answer a precise mathematical form.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.  
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.  
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.  
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.  
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.  
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist’s Wager*.  
- Wikipedia contributors. (2026). *Evidential decision theory* (revision 1373679688). Wikimedia Foundation.