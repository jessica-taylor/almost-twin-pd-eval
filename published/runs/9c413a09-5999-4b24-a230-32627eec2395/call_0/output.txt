# A-FDT: Action Functional Decision Theory

## 1. What this essay is about

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a decision rule built around one question. The agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

The paper's main formal statement is Equation (4) in Section 5. There the agent intervenes on a variable whose values are *actions*: the output of her decision procedure on her actual inputs. Two footnotes (7 and 16) say the authors actually prefer a different version, in which the agent chooses a *policy*, a map from observations to actions. They set that version aside because, as far as they can tell, it only matters in multi-agent dilemmas.

To keep the two apart, I call the action-valued rule of Equation (4) **A-FDT**. I call the policy variant the authors mention **policy-FDT**. The paper itself uses "FDT" for what I call A-FDT. Causal decision theory (**CDT**) and evidential decision theory (**EDT**) appear as foils. Throughout, I mark which claims belong to the source and which are my own interpretations or proposals.

## 2. The common frame: expected utility over hypotheticals

All three theories in the paper are expected-utility theories. Following Gibbard and Harper, the source writes the value of an action $a$, given observation history $x$, as

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $\hookrightarrow$ is the connective for "decision hypotheticals." The paper leans on Joyce's representation theorem: rational preferences justify maximizing (1) whatever constraints are placed on $P(\cdot\hookrightarrow\cdot)$. The theories differ only in how they read $\hookrightarrow$, which is to say in how the agent builds, from her world-model, a picture of "what would happen if I chose $a$." The paper calls these pictures *hypotheticals*. It treats them as "decision-theoretic instruments constructed from beliefs," not as beliefs and not as metaphysical possible worlds.

Write $V = \mathcal U(\textsc{Outcome})$. The two classical rules are then:

$$
\mathrm{EDT}(P,x)=\arg\max_a \mathbb E[V\mid \textsc{Obs}=x,\ \textsc{Act}=a], \tag{2}
$$
$$
\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E[V\mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x]. \tag{3}
$$

EDT conditions on the physical act. CDT performs Pearl surgery on the act inside a causal graph $G$. Surgery keeps the correlations that run causally downstream from $\textsc{Act}$ and severs all others.

## 3. The definition of A-FDT

A-FDT keeps CDT's machinery of surgery on a graph and changes two things. Its model $(P,G)$ must contain a variable for the output of the A-FDT procedure itself on the agent's own inputs. The graph $G$ must encode *subjunctive* dependence, not merely causal dependence. Equation (4) reads:

$$
\boxed{\ \text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left[V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right]\ } \tag{4}
$$

The underlines denote dequoting. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the *name* of the variable in the model representing "what this algorithm outputs on these inputs." The agent needs no knowledge of the variable's value in order to represent it. The source handles the self-reference with Kleene's recursion theorem ("quining").

The paper draws two contrasts with (3).

1. **Locus of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type: the output of a fixed function. Every variable with an edge from that node changes in the hypothetical. That includes the agent's own body, a twin running the same function, and a predictor's model of it.
2. **Treatment of observations.** In the paper's words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." After seeing $x$, the agent intervenes on $\textsc{fdt}(\cdot,\cdot,x)$. Had she seen $y$, she would intervene on $\textsc{fdt}(\cdot,\cdot,y)$.

The source states the slogan this way: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." It also states the core requirement: "when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

**When A-FDT agrees with its rivals.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, except for $\textsc{Act}$'s own dependence on the fdt node. Then
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],$$
and all three rules agree. Disagreement requires something other than the agent's own act that tracks her decision function, such as a predictor or a copy.

## 4. Building the graph: subjunctive dependence

Everything in A-FDT depends on $G$, so it helps to state what the source says about $G$.

- Two physical systems computing the same function both depend subjunctively on that function. The paper's image is two well-functioning calculators computing $6288+1048$.
- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere statistical correlation does not count. Two calculators that happen to be pink share no subjunctive dependence.
- An accurate predictor contains a "twin" of the agent's function. Its prediction therefore depends on the fdt node, weakened by any noise in the prediction.
- A lesion or other common physical cause does not "evaluate the agent's future decisions," so it gets no edge from the fdt node.

The source is frank that it gives no general procedure for constructing $G$. It calls "deducing the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem in the study of functional decision theory." A truly general account would require counterpossible reasoning (what a function would do were it, impossibly, to output something else), and the paper brackets that. Equation (4) works *given* $G$, just as (3) works given a causal graph.

**Operational recipe (my proposal, distilled from the paper's examples).** To set up a problem for A-FDT:

1. List every process that computes, simulates, or reliably predicts the agent's decision function on some input $y$. Include the agent's own body.
2. For each relevant input $y$, create a node $F_y=\textsc{fdt}(\underline P,\underline G,\underline y)$. Draw an edge from $F_y$ to every process in step 1 that computes or predicts the output on input $y$.
3. Model prediction error with an exogenous noise node, as the paper does with $\textsc{Accurate}$. Nothing else should mediate between the fdt node and the predictor.
4. Leave purely correlational structure, such as lesions and coincidences, as ordinary causal structure with no edge from any $F_y$.
5. If which input the agent receives depends on some upstream variable, make $\textsc{Act}$ a switch. It copies $F_y$ when the observation would be $y$.
6. Compute (4) by intervening on $F_x$ for the actual $x$.

## 5. Worked examples

All payoffs are in dollars-as-utility.

### Newcomb's problem

The predictor is 99% accurate. Box A holds \$1,000. Box B holds \$1M if the predictor predicted one-boxing. There is no observation, so the agent intervenes on $F=\textsc{fdt}(\underline P,\underline G)$. In the graph, $F$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$.

$$\mathbb E[V\mid\mathtt{do}(F=\textit{one})]=0.99(1{,}000{,}000)=990{,}000,$$
$$\mathbb E[V\mid\mathtt{do}(F=\textit{two})]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.$$

A-FDT one-boxes. CDT's surgery on $\textsc{Act}$ leaves $P(\textit{full})=p$ fixed, so CDT two-boxes for every $p$.

The source makes a point worth repeating: no retrocausation is assumed. The agent simply refuses to imagine her act varying while a competent prediction of that very act stays fixed. The twin prisoner's dilemma works the same way. The twin's choice hangs off the same fdt node, so the agent compares mutual cooperation (\$1M) with mutual defection (\$1,000) and cooperates.

### Smoking lesion

The lesion causes cancer and also a taste for smoking. Smoking itself is harmless. There is no edge from the fdt node to $\textsc{Cancer}$.

The paper models the case with two possible utility functions and two candidate fdt nodes, one for each. Which node controls $\textsc{Act}$ depends on $\textsc{Lesion}$. Intervening on the node for "lesion-type preferences" leaves $P(\textit{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot 1{,}000$, so A-FDT smokes.

EDT refrains, because it treats smoking as evidence of the lesion. A-FDT thus one-boxes and smokes, which the paper calls "a single compact decision criterion."

### Transparent Newcomb

Both boxes are transparent. Box B is filled iff the predictor predicts one-boxing *upon seeing a full box*. The agent sees a full box. In the graph:

- $F_{\text{full}}$ feeds both $\textsc{Prediction}$ and $\textsc{Act}$.
- $F_{\text{empty}}$ feeds only $\textsc{Act}$.
- $\textsc{Prediction}$ acts as the switch that decides which fdt node sets $\textsc{Act}$.

Let $q$ be the agent's probability that she two-boxes on seeing an empty box. Intervening on $F_{\text{full}}$:

$$\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=\textit{one})]=0.99(1{,}000{,}000)+0.01\,q(1{,}000)=990{,}000+10q,$$
$$\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=\textit{two})]=0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.$$

(The extracted text prints the second value as "\$110,00 + q·\$990." The derivation gives $10{,}010+990q$; the conclusion is unaffected.)

A-FDT one-boxes for every $q\in[0,1]$, even with a visibly full box. While evaluating two-boxing, the agent imagines a world in which she would probably have seen an empty box. CDT and EDT both two-box, are predicted to, and so face empty boxes. The paper argues that this case is structurally identical to paying the driver in Parfit's hitchhiker.

### Mechanical blackmail with an imperfect predictor

The blackmailer runs a \$1M-damage program only if she predicts the agent will pay \$1,000 to stop it. Suppose she wrongly predicts "pay" with probability $\varepsilon$. After receiving the letter, A-FDT intervenes on $F_{\text{blackmail}}$:

- If the node outputs *pay*, the agent is essentially always blackmailed and pays, for an expected loss of $1{,}000$.
- If it outputs *refuse*, she is blackmailed only with probability $\varepsilon$, for an expected loss of $\varepsilon\cdot 10^6$.

So A-FDT refuses iff $\varepsilon<10^{-3}$. The paper's case $\varepsilon=0.0009$ gives an expected loss of \$900, so it refuses. The paper's example of where it would pay instead is printed as "0.011%." By the same arithmetic, $1.1\times10^{-4}$ would still lead to refusal, so the paper presumably meant 0.11%. The general threshold is the useful thing to remember.

### Death in Damascus

Death predicts the agent perfectly. Both of A-FDT's hypotheticals contain Death at the agent's location, so the \$1,000 cost of fleeing decides the matter: stay in Damascus.

CDT cycles. If it expects to stay, it wants to flee, and vice versa. The source further argues that CDT would turn down a truly random coin offering a 50% chance of survival for \$1.

## 6. What the source leaves open, and how I would operationalize it

### (a) Does A-FDT also condition on $x$?

Equation (4) contains no "$\textsc{Obs}=x$" term. The prose says that A-FDT responds to observations by moving the intervention point *instead of* conditioning. A footnote says that conditioning *and* moving the intervention point creates a harmful "double update"; this was the problem with the earlier Timeless Decision Theory. Yet the paper's transparent-Newcomb display writes $\mathbb E(V\mid \mathtt{do}(F_{\text{full}}=a),\textsc{Obs}=\textit{full})$. The arithmetic that follows does not condition on a full box: it assigns 1% weight to worlds with an empty box.

My reading: the equation and the computations are authoritative, and the displayed conditioning is a typo. Operationally, then, $x$ does exactly one thing: it selects which node to intervene on. Expectations are taken under the prior model. This is what makes A-FDT "updateless" with respect to observations.

### (b) Beliefs about one's own outputs on other inputs

Every computation above contains a free parameter for the agent's other fdt nodes: $q$ in the transparent Newcomb and in the smoking lesion. A-FDT leaves these nodes at their prior distribution, because only $F_x$ is intervened on. The paper notes the "correct" values ($q=1$ and $q=0$ respectively) and shows that its conclusions do not depend on them.

In general they can matter. A natural requirement, which is my proposal, is **reflective consistency**: for every input $y$, the agent's prior on $F_y$ should match what (4) actually outputs at $y$. Finding such beliefs is a fixed-point problem. The agent can iterate: guess beliefs, compute (4) at each input, update the beliefs, repeat.

### (c) Why the action version can fall short of the policy version

Fixed points need not be unique. Here is an illustration of my own. An agent and her exact copy run the same algorithm. One sees a red light and the other a green light; nothing else differs. Each receives 10 if both choose $A$, 6 if both choose $B$, and 0 if they mismatch.

The red-room agent intervenes on $F_{\text{red}}$ and holds $F_{\text{green}}$ at her belief $r=P(F_{\text{green}}=A)$. That gives
$$\mathbb E[V\mid\mathtt{do}(F_{\text{red}}=A)]=10r,\qquad \mathbb E[V\mid\mathtt{do}(F_{\text{red}}=B)]=6(1-r),$$
so she picks $A$ iff $r>3/8$. Both $(A,A)$ with $r=1$ and $(B,B)$ with $r=0$ are reflectively consistent. A-FDT can therefore settle on the inferior outcome.

Policy-FDT avoids this. It intervenes on a single node whose values are maps $\pi:\{\text{red},\text{green}\}\to\{A,B\}$, compares all four maps, picks $\pi\equiv A$, and applies $\pi(x)$. This is consistent with the source's remark that the distinction matters in multi-agent dilemmas.

For a practitioner the lesson is this. A-FDT gives determinate verdicts when the payoff depends on the output at *one* input, or when the other inputs' outputs do not change the ranking. That covers all of the paper's cases. When the outputs at different inputs must coordinate, (4) underdetermines the answer, and one needs either an equilibrium-selection rule or the policy version.

### (d) Ties, zero-probability actions, and $\mathcal A$

A-FDT inherits the convenient features of the do-calculus. An intervention is well defined even if the prior gives an action probability zero. This lets it escape the "cannot imagine taking \$100" problem that EDT faces in the source's cosmic-ray example. The paper gives no tie-breaking rule. Any fixed, publicly known rule is harmless, but predictors may exploit randomized tie-breaking.

The action set $\mathcal A$ is assumed finite. Graded predictor reliability is handled with noise nodes. Treating partial similarity between the agent and some other process, such as a "rough model," as a weighted edge is not covered by the source. It would require extra assumptions about the conditional distribution of the other process given the fdt node.

## 7. Philosophical motivation

The paper's case for A-FDT rests mainly on utility achieved, supported by several further arguments.

- **Precommitment.** CDT and EDT agents would pay for binding precommitments to one-box, to pay the driver, or to refuse blackmail. A-FDT acts as they would have precommitted to act, without paying for the commitment. It is also, the authors claim, reflectively stable in fair problems: holding the blackmail letter, it has no wish to self-modify into CDT.
- **Value of information.** EDT agents can expect information to harm them; A-FDT agents do not.
- **Dominance is not neutral.** Every way of constructing hypotheticals generates its own notion of dominance. Two-boxing "dominates" only under CDT's hypotheticals, so dominance cannot settle the dispute.
- **Fairness.** A problem is fair, informally, if the agent's beliefs are accurate and outcomes depend only on her *behavior* in the problem, not on her decision procedure as such. Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." The authors report finding no fair dilemma in which FDT loses. They also concede, in their footnote on fairness, that "fairness" has not yet been formalized.
- **Control.** A-FDT agents are no more deluded about "control" than CDT agents. A deterministic CDT agent imagines its one possible act varying; an A-FDT agent imagines its function's one possible output varying.

Critics will reply that refusing the blackmail letter or leaving a visibly free \$1,000 is odd. The paper acknowledges the oddness and answers with the "global perspective": the agent asks what the whole universe would look like if her algorithm behaved differently.

## 8. Conclusion

A-FDT is the rule $\arg\max_a\mathbb E[V\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)]$. It is CDT's surgery moved from the physical act onto the logical output of the agent's decision function. Observations select the intervention node rather than being conditioned on.

Its verdicts are fixed once two things are supplied: a graph recording what depends subjunctively on that output, and beliefs about the agent's outputs on other inputs. With those in hand, it one-boxes, smokes, cooperates with twins, pays the driver, refuses blackmail, and stays in Damascus.

Three things remain open:

- how to construct the subjunctive-dependence graph, which the source calls its largest open problem;
- whether expectations are also conditioned on $x$ (I have argued they are not);
- how to choose among self-consistent beliefs about other-input outputs, where the policy formulation the authors prefer offers a cleaner answer.

For problems in which a single input's output carries all the decision-relevant dependence, the recipe in Section 4 is enough to decide unfamiliar cases.

---

**References**
Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060).
Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
Pearl, J. (2000). *Causality*.