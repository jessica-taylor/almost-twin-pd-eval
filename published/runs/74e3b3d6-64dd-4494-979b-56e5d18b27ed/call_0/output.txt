# Evidential Decision Theory: Choosing the Best News

Evidential decision theory, or EDT, is a school of decision theory that evaluates actions by asking: *How good would the world be, in expectation, if I learned that I had performed this action?* The theory’s slogan, as reported in the reference article, is to “do what you most want to learn that you will do” (Wikipedia contributors, 2026, citing Ahmed, 2021). An EDT agent therefore chooses the action with the highest *news value*: the expected desirability of outcomes conditional on the action being taken.

This makes EDT formally simple but philosophically provocative. It differs from causal decision theory, or CDT, which evaluates actions by their expected causal efficacy: what outcomes would be brought about if the action were performed. The two theories often agree, but they diverge in famous cases such as Newcomb’s paradox and the twin prisoner’s dilemma. The reference article presents EDT’s core formula, these two examples, a brief discussion of Sleeping Beauty, and some criticisms. In this essay I reconstruct EDT in a form precise enough for unfamiliar cases, explain how it handles dependencies and counterfactuals, and indicate where the source is under-specified. Some of the formal refinements below—especially the use of total evidence, zero-probability actions, policy evaluation, and ratifiability—are my own elaborations rather than claims made explicitly by the source.

---

## 1. The basic EDT rule

Suppose an agent faces a finite set of possible actions

\[
\mathcal A=\{A_1,\dots,A_n\}
\]

and a finite set of possible outcomes

\[
\mathcal O=\{O_1,\dots,O_m\}.
\]

The agent has a probability function \(P\) representing her beliefs, and a desirability or utility function \(D\) assigning a real number \(D(O_j)\) to each outcome. EDT defines the value of an action \(A\) as the conditional expected desirability of outcomes given that \(A\) is performed:

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

Equivalently,

\[
V(A)=\mathbb E_P[D(O)\mid A].
\]

The EDT prescription is:

\[
\text{Choose } A^* \in \arg\max_{A\in\mathcal A} V(A).
\]

This is the formula given in the reference article, attributed to Gibbard and Harper (1976). The article emphasizes that \(D(O_j)\) is the desirability of outcome \(O_j\), while \(P(O_j\mid A)\) is the ordinary conditional probability of \(O_j\) given that action \(A\) occurs.

In most realistic applications one should include the agent’s total background evidence \(E\). A more explicit version is therefore

\[
V_E(A)=\sum_j P(O_j\mid A,E)D(O_j).
\]

This refinement is not stated in the source, but it is natural: EDT evaluates the news value of an action relative to what the agent already knows.

If outcomes are determined by an action together with a state of the world \(S\), we can write

\[
V(A)=\sum_s P(S=s\mid A,E)U(A,s),
\]

where \(U(A,s)\) is the utility of performing \(A\) in state \(s\). The crucial point is that EDT conditions the probability of states on the action. If performing \(A\) is evidence that the world is in a good state, EDT counts that in favor of \(A\).

---

## 2. EDT versus CDT

The reference article contrasts EDT with causal decision theory. CDT uses counterfactual probabilities:

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A \mathrel{\Box\rightarrow} O_j\) means something like “if \(A\) were performed, \(O_j\) would obtain.” In modern causal-model language, CDT often evaluates

\[
U(A)=\sum_j P(O_j\mid do(A))D(O_j),
\]

where \(do(A)\) represents an intervention that sets the action to \(A\). EDT instead uses the observational conditional

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

The difference is important whenever the action is correlated with outcomes for reasons other than direct causation. For example, an action may be predicted by a highly accurate predictor, caused by a common factor, or correlated with another agent’s action because the agents reason similarly. EDT treats all such probabilistic dependencies as decision-relevant. CDT asks whether the action itself would make the outcome more likely; EDT asks whether the action is good news.

This is why the source says that EDT and CDT agree in many cases but diverge in certain philosophical thought experiments. When action and outcome are related only by ordinary causation, and there are no confounding correlations, the conditional \(P(O_j\mid A)\) and the counterfactual/interventional probability \(P(A\mathrel{\Box\rightarrow}O_j)\) often coincide. They come apart in cases involving prediction, duplication, or common causes.

---

## 3. What counts as a relevant dependency?

EDT’s central commitment is that any probabilistic dependence between action and outcome can matter, provided it remains after conditioning on the agent’s evidence. This includes:

1. **Direct causal dependence.** If smoking causes cancer, then \(P(\text{cancer}\mid \text{smoking})\) reflects a causal relation, and EDT will disfavor smoking if cancer is bad.

2. **Predictive dependence.** If a predictor has already predicted what you will do, your action may be strong evidence about the predictor’s earlier prediction.

3. **Common-cause dependence.** If some underlying condition causes both your action and an outcome, your action may be evidence of that outcome even if it does not cause it.

4. **Logical or algorithmic correlation.** If another agent uses the same reasoning process as you, your choice may be evidence of their choice, even without communication.

The reference article illustrates predictive dependence with Newcomb’s paradox and algorithmic correlation with the twin prisoner’s dilemma. EDT does not, by itself, ask whether the dependence is causal. It only asks what the conditional probabilities are.

This breadth is also the source of the main objections to EDT. To see why, consider an example not mentioned in the source but often used in discussions of EDT.

### A common-cause example: the smoking lesion

Suppose a genetic lesion causes both a tendency to smoke and a high risk of cancer. Smoking itself does not cause cancer. Suppose also that smoking gives no direct pleasure. The agent knows only the statistical association:

\[
P(\text{cancer}\mid \text{smoke})=0.9,
\]
\[
P(\text{cancer}\mid \text{do not smoke})=0.1.
\]

Let cancer have utility \(-100\), and no cancer have utility \(0\). Then EDT gives

\[
V(\text{smoke})=0.9(-100)+0.1(0)=-90,
\]

while

\[
V(\text{do not smoke})=0.1(-100)+0.9(0)=-10.
\]

EDT recommends not smoking, because smoking is bad news: it indicates that one probably has the lesion and hence cancer. But if smoking does not causally affect cancer, CDT would not reject smoking on those grounds. This example is not in the source, but it clarifies the dispute. Critics such as Lewis and Joyce, cited in the article, object that EDT encourages “managing the news” rather than producing good outcomes.

One possible EDT response is that if the agent learns she has or lacks the lesion, the relevant conditional probabilities change. If she knows she has the lesion, smoking may no longer be evidence of cancer beyond what she already knows. Thus EDT’s verdict depends sensitively on the agent’s total evidence.

---

## 4. Newcomb’s paradox

The reference article’s central example is Newcomb’s paradox. There is a predictor, a player, and two boxes:

- Box A is transparent and always contains \$1,000.
- Box B is opaque. Its contents were already determined by the predictor.
- If the predictor predicted that the player will take both boxes, box B is empty.
- If the predictor predicted that the player will take only box B, box B contains \$1,000,000.

The player can either take both boxes or take only box B. The predictor is highly reliable; the article uses 99% accuracy.

EDT recommends taking only box B. The reason is that taking only box B is strong evidence that the predictor predicted one-boxing, in which case box B contains \$1,000,000. Taking both boxes is strong evidence that the predictor predicted two-boxing, in which case box B is empty.

Using the article’s numbers:

\[
\begin{aligned}
V(\text{take only B})
&=P(\text{1M in B}\mid \text{take only B})\cdot \$1{,}000{,}000 \\
&\quad + P(\text{nothing in B}\mid \text{take only B})\cdot \$0 \\
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0 \\
&=\$990{,}000.
\end{aligned}
\]

For two-boxing:

\[
\begin{aligned}
V(\text{take both})
&=P(\text{1M in B}\mid \text{take both})\cdot \$1{,}001{,}000 \\
&\quad + P(\text{nothing in B}\mid \text{take both})\cdot \$1{,}000 \\
&=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000 \\
&=\$11{,}000.
\end{aligned}
\]

Since \(\$990{,}000>\$11{,}000\), EDT says: take only box B.

CDT, according to the source, recommends taking both boxes. The causal reasoning is that the predictor has already acted. The contents of box B are fixed. Taking both boxes cannot change whether box B contains \$1,000,000; it only adds the sure \$1,000 from box A. Thus two-boxing causally dominates one-boxing: in every possible state of box B, taking both yields \$1,000 more than taking only B. EDT nevertheless one-boxes because it conditions on the evidential connection between the player’s choice and the predictor’s earlier prediction.

A useful extension, not explicitly in the source, is to compute the threshold predictor accuracy required for EDT to one-box. Let \(p\) be the probability that the predictor predicts one-boxing given that the player one-boxes, and also the probability that it predicts two-boxing given that the player two-boxes. Let \(M=1{,}000{,}000\). Then

\[
V(\text{one-box})=pM,
\]

while

\[
V(\text{two-box})=(1-p)(M+1000)+p(1000)=(1-p)M+1000.
\]

EDT prefers one-boxing when

\[
pM>(1-p)M+1000,
\]

or

\[
(2p-1)M>1000.
\]

With \(M=1{,}000{,}000\), this requires

\[
p>0.5005.
\]

So EDT one-boxes even if the predictor is only barely better than chance, provided the million-dollar reward is large enough relative to the sure thousand dollars.

---

## 5. The twin prisoner’s dilemma

The reference article also discusses a variant of the prisoner’s dilemma involving psychological twins. Aomame and her twin are in separate rooms and cannot communicate. Their payoffs are:

- Both cooperate: each gets \$5.
- Both defect: each gets \$1.
- One cooperates, one defects: defector gets \$10, cooperator gets \$0.

The article assumes that the twin’s reasoning processes are exactly analogous to Aomame’s. EDT then says that Aomame’s choice is strong evidence about her twin’s choice. If Aomame cooperates, that is evidence that her twin will cooperate. If she defects, that is evidence that her twin will defect.

In the idealized case of perfect correlation:

\[
\begin{aligned}
V(\text{cooperate})
&=P(\text{twin cooperates}\mid \text{Aomame cooperates})\cdot \$5 \\
&\quad +P(\text{twin defects}\mid \text{Aomame cooperates})\cdot \$0 \\
&=1\cdot \$5+0\cdot \$0 \\
&=\$5,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{defect})
&=P(\text{twin cooperates}\mid \text{Aomame defects})\cdot \$10 \\
&\quad +P(\text{twin defects}\mid \text{Aomame defects})\cdot \$1 \\
&=0\cdot \$10+1\cdot \$1 \\
&=\$1.
\end{aligned}
\]

EDT therefore recommends cooperation.

Again, it is helpful to generalize. Suppose the correlation is imperfect. Let

\[
q=P(\text{twin cooperates}\mid \text{Aomame cooperates})
\]

and suppose symmetrically that

\[
q=P(\text{twin defects}\mid \text{Aomame defects}).
\]

Then

\[
V(\text{cooperate})=5q,
\]

while

\[
V(\text{defect})=10(1-q)+q=10-9q.
\]

Cooperation is recommended when

\[
5q>10-9q,
\]

or

\[
14q>10,
\]

so

\[
q>\frac{5}{7}\approx 0.714.
\]

Thus EDT cooperates when the twin is sufficiently likely to make the same choice, but defects if the correlation is weak. This illustrates how EDT can be applied to unfamiliar cases: estimate the conditional probabilities induced by the relevant dependence, multiply by utilities, and compare.

---

## 6. Policies, not merely isolated actions

The reference article mostly discusses one-shot actions, but EDT can also evaluate policies. A policy is a rule mapping circumstances to actions. Let \(\pi\) be a policy, and let \([\pi]\) be the proposition that the agent adopts or executes \(\pi\). Then EDT can define

\[
V(\pi)=\mathbb E[D(O)\mid \pi]
=\sum_j P(O_j\mid \pi)D(O_j).
\]

In sequential problems, the relevant “action” may be an entire plan. For example, an agent might choose between a policy of one-boxing in Newcomb-like situations and a policy of two-boxing. EDT evaluates the policy by conditioning on the proposition that the policy is followed.

This matters because EDT can sometimes recommend ex ante commitment to a policy even if, at a later moment, a myopic act-by-act calculation might look different. If the agent can bind herself, or if predictors anticipate her general policy, then the policy is the proper object of evaluation. If she cannot bind herself and will re-decide later using EDT, then EDT may need to evaluate each future choice separately. This creates possible dynamic inconsistency.

The source does not fully address this issue. A reasonable operational interpretation, which I propose rather than find in the article, is this: EDT should be applied to the option that is genuinely under the agent’s control at the time of decision. If the agent is choosing a binding policy, evaluate the policy as a whole. If she is choosing only an immediate act, evaluate that act conditional on current evidence. If there is a conflict between ex ante policy evaluation and later act-by-act evaluation, the case should specify whether commitment is possible. EDT by itself does not automatically solve all sequential-choice problems.

---

## 7. Counterfactuals and zero-probability actions

A technical subtlety arises because EDT uses conditional probabilities \(P(O_j\mid A)\). Ordinary conditioning requires \(P(A)>0\). But in deterministic deliberation, an agent may regard some actions as impossible. For instance, if she is certain she will choose the action with highest expected utility, then before deliberation she may assign probability zero to inferior actions. Conditioning on those actions then becomes problematic.

The reference article does not discuss this. One operational solution is to assign small positive probabilities, sometimes called “trembles,” to every possible action. For example, suppose each action has at least probability \(\epsilon>0\). Then compute EDT values using those probabilities and take the limit as \(\epsilon\to 0\) if needed. Another approach is to treat conditional probabilities as primitive, not defined by the ratio \(P(O\land A)/P(A)\). A third approach is to model the agent’s decision procedure explicitly, including uncertainty about how she will reason, and then condition on action events within that enlarged model.

These moves are not mere technicalities. EDT is a theory about what an agent should do given her beliefs, but those beliefs include beliefs about her own possible choices. The source’s simple formula assumes that such conditional probabilities are available. In applying EDT to unfamiliar cases, one must therefore specify a probability model over actions, states, predictors, and outcomes.

A related issue is ratifiability. An EDT choice might be self-undermining if the agent’s recognition that she is making that choice changes the evidential probabilities. A natural strengthening, not stated in the source, is to require that an EDT choice be *ratifiable*: it should remain optimal conditional on the agent’s knowledge that she is choosing by EDT. Formally, if \(R\) is the proposition that the agent is using EDT, one may require

\[
A^*\in \arg\max_A \sum_j P(O_j\mid A,R,E)D(O_j).
\]

This is one way to make EDT more stable in reflexive decision problems. Whether EDT should be supplemented in this way is philosophically contested, and the reference article leaves the question open.

---

## 8. Sleeping Beauty and indexical uncertainty

The reference article briefly mentions the Sleeping Beauty problem. It says that EDT has been applied to Sleeping Beauty in order to avoid Dutch book arguments, but that Vincent Conitzer has argued that “halfers” can still be Dutch-booked even after adopting EDT (Conitzer, 2015).

The important general lesson is that EDT is not, by itself, a complete theory of self-locating belief. To apply EDT in Sleeping Beauty, one must first decide how Beauty should assign credences upon awakening: for example, whether heads should receive credence \(1/2\) or \(1/3\). EDT then evaluates bets or choices conditional on the relevant awakening event. Different prior accounts of indexical evidence can therefore lead to different EDT recommendations. The source correctly presents this as an area of ongoing dispute rather than a settled application of EDT.

---

## 9. Philosophical motivation and criticism

EDT has an attractive interpretation: it tells agents to choose the action that would be the best news. If you imagine receiving a message saying “you performed \(A\),” EDT asks which such message would make you most pleased, given your beliefs and desires. This makes EDT especially natural in environments where choices are predictable or correlated. If many similar agents use similar reasoning, your choice may be evidence about their choices, and therefore about large-scale outcomes.

The reference article mentions a supporting argument along these lines: even if one is not fully confident in EDT, it may be reasonable to act as if EDT were true because EDT can involve the actions of many correlated decision-makers, giving its recommendations high stakes (MacAskill et al., 2021). In such cases, the evidential relevance of one’s action may extend far beyond its local causal impact.

Critics reject this emphasis on news value. The article quotes David Lewis’s characterization of EDT as “an irrational policy of managing the news” (Lewis, 1981). James Joyce is similarly quoted as saying that rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news (Joyce, 1999).

The disagreement is deep. EDT says that if an action is reliably associated with good outcomes, that association is decision-relevant. CDT says that only the action’s causal contribution is decision-relevant. In Newcomb’s paradox, EDT one-boxes because one-boxing is evidence that the predictor filled box B with a million dollars. CDT two-boxes because the predictor’s act is already finished, so the player can only add the extra \$1,000. In the twin prisoner’s dilemma, EDT cooperates because cooperation is evidence that the twin will cooperate. CDT may defect if it treats the twin’s action as causally independent.

The smoking-lesion case shows why many philosophers resist EDT: it can recommend avoiding a harmless symptom of bad outcomes. EDT defenders may respond that such cases are misleading, or that a properly formulated EDT with full evidence avoids some pathological verdicts. But the reference article’s criticisms section makes clear that the central philosophical dispute remains unresolved.

---

## 10. How to apply EDT in practice

A reader wanting to apply EDT to an unfamiliar decision problem can use the following procedure:

1. **Identify the available actions.**  
   Make them mutually exclusive and exhaustive, or specify the relevant policy options.

2. **Identify the possible outcomes.**  
   Assign each outcome a desirability \(D(O_j)\). If utilities depend on states and actions, use \(U(A,s)\).

3. **Specify the agent’s evidence.**  
   Include all relevant background information \(E\).

4. **Assign conditional probabilities.**  
   Estimate \(P(O_j\mid A,E)\) for each action and outcome. These probabilities should reflect all known causal, predictive, common-cause, or algorithmic dependencies.

5. **Compute EDT values.**  
   For each action,

   \[
   V_E(A)=\sum_j P(O_j\mid A,E)D(O_j).
   \]

6. **Choose the action with maximum EDT value.**  
   If evaluating policies, replace \(A\) with a policy \(\pi\) and condition on the policy being followed.

7. **Check stability if needed.**  
   In reflexive or sequential problems, ask whether the recommendation remains optimal when the agent conditions on the fact that she is using EDT, or whether a different policy should be adopted ex ante.

This procedure is simple, but its difficulty lies in step 4. EDT does not tell you where the conditional probabilities come from. It requires a coherent probabilistic model of the world, including the agent’s own possible choices.

---

## Conclusion

Evidential decision theory offers a clean and powerful rule: choose the action that would be the best news. Its formal core is the conditional expected utility formula

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

and its distinctive philosophical move is to treat all probabilistic dependencies between actions and outcomes as potentially decision-relevant. This explains why EDT one-boxes in Newcomb’s paradox and cooperates in the twin prisoner’s dilemma. It also explains why EDT is controversial: it can favor actions because they are symptoms of good outcomes, not because they cause those outcomes.

The theory is easy to state but subtle to apply. One must specify the relevant actions, outcomes, utilities, and especially the conditional probabilities given total evidence. In sequential, self-referential, or zero-probability cases, EDT may need supplementary ideas such as policy evaluation, trembling-hand probabilities, or ratifiability. Even with those refinements, the central dispute between EDT and causal decision theory remains: should rational choice track the best evidence or the best causal intervention? EDT gives a clear answer—choose what you would most want to learn you had chosen.

---

## References

Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.

Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.

Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.

MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist’s Wager*.

Wikipedia contributors. (2026). Evidential decision theory. Wikipedia, revision 1373679688. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688