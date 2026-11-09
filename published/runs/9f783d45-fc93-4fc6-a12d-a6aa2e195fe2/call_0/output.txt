# Evidential Decision Theory: Choosing the Act You Would Most Like to Learn You Performed

## 1. The slogan and the idea

Evidential decision theory (EDT) answers the question "what should I do?" with a recommendation that sounds almost too simple:

> **Do what you would most want to learn that you will do.**

The phrase comes from Arif Ahmed's monograph on EDT, which is the main source for the reference article. An act, on this view, is assessed by its *news value*. Suppose you are told that you are about to perform act $A$. How good, in expectation, is the world you should now expect? EDT tells you to choose the act whose news is best.

This sets EDT apart from **causal decision theory** (CDT), which assesses acts by what they *bring about*. In most ordinary decisions the two theories agree, because the news that I do $A$ usually matters only through what $A$ causes. They separate when an act is *evidence* about something it does not *cause*. Examples include a prediction already made, a twin's choice, or a hidden common cause. Most of the philosophical interest in EDT, and most of the controversy, sits in that gap.

This essay sets out the formal theory, works through the standard cases, and then takes up questions the reference article leaves open. The main ones are what the agent should condition on, what to do about acts of probability zero, and whether to evaluate acts or policies. The source's claims are marked as such. Where I add structure or propose an operational reading, I say so.

## 2. The formal definition

### 2.1 The basic formula

Fix a finite set of available acts $\mathcal{A}$ and a partition of possible outcomes $\{O_j\}$. Each outcome has a desirability (utility) $D(O_j)$. The agent has a credence function $P$ that covers both outcomes and her own acts. Following Gibbard and Harper (1976), the source defines the **evidential expected utility** of an act $A$ as

$$
V(A)=\sum_j P(O_j \mid A)\, D(O_j).
$$

The decision rule is:

$$
\text{choose } A^* \in \arg\max_{A\in\mathcal{A}} V(A).
$$

Two features stand out.

1. **Acts are propositions in the agent's own probability space.** For $P(O_j\mid A)$ to make sense, the agent must have credences about what she herself will do. This is the hallmark of the Jeffrey-style framework from which EDT descends. Savage's framework, by contrast, treats acts as functions from states to outcomes and puts no probabilities on them.
2. **Nothing beyond conditioning is used.** EDT needs no counterfactuals, no causal graph, and no interventions. The only dependency relation it recognizes is probabilistic (evidential) dependence.

### 2.2 States, outcomes, and partition invariance

It is often convenient to bring in a partition of states $\{S_i\}$, such as "the box contains \$1M / is empty", with outcomes fixed by an act–state pair: $D(A\wedge S_i)=u(A,S_i)$. The law of total probability then gives

$$
V(A)=\sum_i P(S_i\mid A)\,u(A,S_i).
$$

*(Addition.)* A notable formal property is that this calculation gives the same answer **for every partition** $\{S_i\}$, provided $u(A,S_i)$ is read as the news value of $A\wedge S_i$. In Jeffrey's framework, $V(A)$ is the probability-weighted average of the values of the ways $A$ can be true, and refining or coarsening the partition leaves that average unchanged. CDT, in Lewis's formulation, works differently. The states must be "dependency hypotheses" that the act cannot causally affect, so CDT depends on choosing the right partition. EDT has no partition problem. That is part of its appeal. As §5 shows, it also makes EDT sensitive to *every* correlation, whether or not one would call it relevant.

### 2.3 The contrast with CDT

The source states CDT's formula as

$$
U(A)=\sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\,D(O_j),
$$

where $P(A\mathrel{\Box\!\!\rightarrow}O_j)$ is the probability that $O_j$ *would* obtain *if* $A$ were performed. If the states $S_i$ are causally independent of the act, this becomes

$$
U(A)=\sum_i P(S_i)\,u(A,S_i).
$$

*(Addition.)* Set the two side by side:

$$
V(A)-U(A)=\sum_i \big[P(S_i\mid A)-P(S_i)\big]\,u(A,S_i).
$$

So **EDT and CDT agree whenever the act is probabilistically independent of the causally upstream states**, and disagree only if the act carries information about them. This gives a quick test for unfamiliar cases. Ask whether learning that you chose $A$ would change your credence about anything you cannot causally affect. If it would not, the two theories coincide, and both reduce to Savage-style expected utility.

## 3. The standard cases

### 3.1 Newcomb's problem

There are two boxes. Box A is transparent and holds \$1,000. Box B is opaque. A predictor has filled it with \$1,000,000 if it predicted you would take only B, and left it empty if it predicted you would take both. The predictor is right with probability $p$.

Let $M$ be "B contains \$1M". Under EDT:

$$
\begin{aligned}
V(\text{one-box}) &= P(M\mid \text{one})\cdot 10^6 = p\cdot 10^6,\\
V(\text{two-box}) &= P(M\mid\text{two})\cdot(10^6+10^3) + P(\neg M\mid\text{two})\cdot 10^3 = (1-p)\cdot 10^6 + 10^3.
\end{aligned}
$$

With $p=0.99$, as in the source, the values are \$990,000 against \$11,000, so EDT recommends one-boxing. *(Addition.)* In general, one-boxing wins exactly when

$$
p\cdot 10^6 > (1-p)\cdot10^6+10^3 \iff p > 0.5005.
$$

A predictor only slightly better than chance is enough.

CDT reasons differently. The contents of B are already fixed, and the act is causally independent of $M$. For any credence $q=P(M)$,

$$
U(\text{two}) - U(\text{one}) = q\cdot 10^3 + (1-q)\cdot 10^3 = 10^3 > 0,
$$

so two-boxing dominates. In the notation of §2.3, the disagreement comes entirely from $P(M\mid\text{one})\neq P(M\mid\text{two})$.

### 3.2 The twin prisoner's dilemma

The source's version: Aomame and her psychological twin each choose to cooperate (C) or defect (D). Mutual cooperation pays \$5 each, mutual defection \$1 each, and a lone defector gets \$10 while the lone cooperator gets \$0. With perfect correlation, EDT gives $V(C)=5$ and $V(D)=1$, so Aomame should cooperate.

*(Addition.)* It is more instructive to vary the correlation. Let

$$
q_C = P(\text{twin C}\mid \text{I C}),\qquad q_D = P(\text{twin C}\mid\text{I D}).
$$

Then

$$
V(C) = 5q_C,\qquad V(D) = 10q_D + (1-q_D) = 1+9q_D,
$$

and EDT recommends cooperating iff $5q_C > 1 + 9q_D$.

- **Perfect twin** ($q_C=1,\ q_D=0$): $5>1$, so cooperate.
- **Independent opponent** ($q_C=q_D=q$): cooperate iff $5q>1+9q$, which never holds. Defect.
- **Partial correlation**, e.g. $q_C=0.8,\ q_D=0.3$: $4 > 3.7$, so cooperate, narrowly.

The independent case matters. Against an opponent whose choice is uncorrelated with yours, EDT defects just as orthodox game theory does. EDT is not a theory of "being nice". Its verdicts follow the structure of the agent's evidence. This is the formal core of what Hofstadter called *superrationality*.

### 3.3 Sleeping Beauty and Dutch books

The source notes that EDT has been invoked in the Sleeping Beauty problem to protect "halfers" from Dutch books, and that Conitzer (2015) argues halfers remain vulnerable even so. A worked example shows why EDT is relevant at all. The details below are my reconstruction of the standard reasoning, not text from the source.

A fair coin is tossed. On Heads, Beauty is woken once. On Tails, she is woken twice, with her memory erased in between. At each awakening she is offered a bet: win $a$ if Tails, lose $b$ if Heads.

Her awakenings cannot be told apart, so her decision procedure gives the same answer at each one. An EDT agent therefore treats "I accept now" as strong evidence that "I accept at every awakening". If she evaluates total winnings in the world:

$$
V_{\text{halfer, EDT}}(\text{accept}) = \tfrac12(-b) + \tfrac12(2a) = a - \tfrac{b}{2}.
$$

A "thirder" who evaluates only the present bet causally gets

$$
U_{\text{thirder, CDT}}(\text{accept}) = \tfrac13(-b)+\tfrac23 a = \tfrac23\left(a-\tfrac b2\right),
$$

which has the same sign. Halfer credences combined with EDT produce the same betting behaviour as thirder credences combined with CDT. That is why the combination escapes the usual Dutch book, an observation associated with Arntzenius and Briggs. Conitzer's point, which the source reports, is that a cleverer sequence of bets still exploits the evidential halfer. Whether EDT rescues halfing is therefore contested. The example does make a general lesson clear. **When an agent's decision is copied across several decision points, EDT treats one choice as evidence about all of them**, and so effectively evaluates a policy.

## 4. How EDT handles dependencies and counterfactuals

The deepest conceptual difference is in what each theory treats as a "dependency".

- **CDT** asks how outcomes *would* differ under intervention. Correlations through common causes or predictions are screened off, because the agent's act is treated as an exogenous "surgery" on the world.
- **EDT** asks how credences *do* differ under conditioning. Every correlation counts, whatever its source: causation, a common cause, prediction, or computational similarity.

For EDT, counterfactuals are therefore not a primitive. "What would happen if I did $A$?" is replaced by "what should I believe, given that I do $A$?" Defenders count this as a virtue. Counterfactuals are notoriously hard to analyse, and conditional probability is well understood. Critics count it as the central flaw: the agent ends up treating her act as a *symptom* when it should be a *lever*.

The source quotes two such critics. David Lewis described EDT as endorsing "an irrational policy of managing the news". James Joyce wrote that rational agents "choose acts on the basis of their *causal efficacy*, not their auspiciousness."

## 5. The smoking lesion and the problem of what to condition on

The sharpest form of the "managing the news" objection is a case the source does not discuss. It is needed to apply EDT responsibly.

**Smoking lesion** *(addition)*. A genetic lesion $L$ causes both cancer and a desire to smoke. Smoking itself is harmless and pleasant. Take these numbers:

| Quantity | Value |
|---|---|
| $P(L)$ | 0.2 |
| $P(\text{cancer}\mid L)$, $P(\text{cancer}\mid\neg L)$ | 0.9, 0.01 |
| $P(\text{smoke}\mid L)$, $P(\text{smoke}\mid\neg L)$ | 0.9, 0.2 |
| Utility of smoking / of cancer | $+10$ / $-1000$ |

Conditioning naively:

$$
P(L\mid \text{smoke}) = \frac{0.18}{0.18+0.16}\approx 0.529,\qquad P(L\mid\neg\text{smoke}) = \frac{0.02}{0.02+0.64}\approx 0.030.
$$

$$
V(\text{smoke}) \approx 10 - 1000(0.529\cdot0.9 + 0.471\cdot 0.01)\approx -470.8,
$$

$$
V(\neg\text{smoke}) \approx -1000(0.030\cdot 0.9 + 0.970\cdot0.01)\approx -37.0.
$$

On this calculation EDT says not to smoke, giving up a harmless pleasure in order to avoid bad news. Most people find that verdict wrong.

**The tickle defence.** The standard evidentialist reply, developed by Eells and later Ahmed, is that the calculation conditions on the wrong information. The lesion affects behaviour only *through* the agent's desires and beliefs, and a deliberating agent can introspect those. Let $T$ be the agent's known motivational state, the "tickle". If the lesion works only through $T$, then $L \perp \text{smoke} \mid T$, and

$$
V(\text{smoke}\mid T) - V(\neg\text{smoke}\mid T) = 10 > 0.
$$

Once the agent knows her own desires, the act carries no further news about the lesion, and EDT recommends smoking.

**Operational proposal** *(mine)*. The source leaves open which background information $K$ enters the conditional probabilities. I recommend reading EDT as

$$
V_K(A) = \sum_j P(O_j\mid A\wedge K)\,D(O_j),
$$

where $K$ is **everything the agent knows at the time of choice, including introspectively accessible facts about her own preferences, credences, and deliberative state**. This is not an ad hoc fix. It is the principle of total evidence applied to EDT's own conditioning. With that convention, a useful diagnostic follows:

> EDT and CDT diverge only when the act remains correlated with causally independent states **even after conditioning on the agent's total evidence**.

In the smoking lesion, the tickle screens off the correlation, so the two theories agree. In Newcomb's problem, the predictor tracks *the decision itself* (or the whole computation producing it), not just an introspectable input. The correlation survives, so the theories disagree. The twin case is the same: the twin runs the same reasoning, not merely the same inputs. Read this way, EDT's distinctive verdicts are confined to cases of **correlation through the decision process itself**. That is a principled boundary.

The caveat should be stated plainly. The tickle defence assumes perfect self-knowledge. Where an agent truly cannot introspect the relevant state, EDT can still advise news-management. Whether such agents are realistic is an open question.

## 6. Further open questions and operational readings

### 6.1 Acts of zero probability

$P(O\mid A)$ is undefined when $P(A)=0$. Suppose a deliberating agent becomes certain she will one-box. Then $V(\text{two-box})$ has no value, and the comparison cannot be made. The source does not address this.

*Operational reading (mine).* Evaluate acts using the credences the agent holds **during** deliberation, before she becomes certain what she will do. All live options then have positive probability. Formally, one can use a full conditional probability (Popper) function, or treat each act as receiving at least some small probability $\varepsilon$ (a "trembling hand") and take $\varepsilon \to 0$. In the cases above, the conditional probabilities $P(S\mid A)$ come from the structure of the problem (predictor accuracy, twin correlation) and are stable as $P(A)$ varies. The verdicts are therefore robust to this choice.

### 6.2 Acts versus policies

The Sleeping Beauty example showed EDT evaluating, in effect, a policy shared across awakenings. More generally, one can define a **policy-level EDT** *(my formulation)*. Let a policy $\pi$ map each information state to an act, and set

$$
V(\pi) = \sum_j P(O_j\mid \text{I follow }\pi)\,D(O_j).
$$

Act-level and policy-level EDT agree when the agent faces one decision and nothing else depends on her policy. They can come apart when predictors respond to what she *would* do in situations she never reaches. A standard example is the "transparent" Newcomb problem, where box B is visible. Seeing a full box, act-level EDT conditions on that observation, finds that no remaining correlation favours one-boxing, and takes both. Policy-level EDT one-boxes, because the policy of one-boxing is what makes full boxes likely. The source takes no side, and the literature is unsettled. I suggest stating explicitly which version is being used whenever a problem involves prediction of behaviour in counterfactual information states.

### 6.3 Where the probabilities come from

EDT is only as good as the conditional credences fed into it. In practice those credences come from a model of how the agent's choice relates to the world, usually some kind of causal model that includes the agent's decision procedure as a node. EDT does not need *counterfactual* reasoning, but it does need a well-specified joint distribution that includes the agent's own act.

## 7. The evidentialist's wager

The source reports an argument from MacAskill et al. (2021): even someone who gives EDT low credence may have reason to *act as if* it were true. *(Formalization mine.)* Suppose your choice is correlated with the choices of $N$ similar agents spread across the universe. If you are uncertain between EDT and CDT, with credence $c$ in EDT, then:

- under CDT, your choice affects only your own local outcome, with stakes of order $\Delta$;
- under EDT, your choice is evidence about all $N$ correlated choices, with stakes of order $N\Delta$.

If one maximizes expected choiceworthiness across theories, EDT's verdict wins whenever roughly

$$
c\cdot N\Delta > (1-c)\cdot \Delta \iff c > \frac{1}{N+1}.
$$

For large $N$ even a tiny credence in EDT dominates. The argument depends on contested assumptions: that stakes can be compared across theories, and that the population of correlated agents is large. Within those assumptions it is valid.

## 8. Assessment

**Arguments for EDT.**
- *Austerity*: it needs only probability and utility, and it is partition-invariant.
- *Success*: in Newcomb-like problems, agents who follow EDT reliably end up richer. Ahmed and others press the "why ain'cha rich?" challenge against CDT.
- *Coordination*: it supports cooperation among correlated reasoners without communication.

**Arguments against.**
- *News management*: in cases like the smoking lesion where the tickle defence fails, EDT appears to recommend acting so as to receive good news rather than to produce good outcomes. This is the objection of Lewis and Joyce.
- *Instability*: verdicts can depend on the agent's credences about her own acts, which raises the zero-probability and deliberation problems discussed above.
- *Self-knowledge dependence*: the best defence leans on idealized introspection.

## 9. A procedure for unfamiliar cases

Collecting the above *(the procedure itself is my synthesis)*:

1. **List the acts and the outcome-relevant states**, and specify $u(A,S)$.
2. **Fix the agent's total evidence $K$**, including her known preferences and her decision procedure.
3. **Build the joint distribution** $P(S, A \mid K)$. Ask what the act indicates about each state *given* $K$. Correlations through common causes that $K$ screens off disappear. Correlations through the decision process itself (prediction, copying, shared reasoning) remain.
4. **Compute** $V(A)=\sum_i P(S_i\mid A,K)\,u(A,S_i)$ using deliberational credences that give every act positive probability.
5. **If the problem involves predictions of behaviour in other information states, or repeated or copied decisions**, decide whether you are using act-level or policy-level EDT, and say which.
6. **Compare with CDT** via $\sum_i[P(S_i\mid A,K)-P(S_i\mid K)]\,u(A,S_i)$. If this term vanishes, the case does not separate the theories.

## 10. Conclusion

Evidential decision theory ranks acts by the expected value of the world one should believe in after learning one performs them: $V(A)=\sum_j P(O_j\mid A)D(O_j)$. It differs from causal decision theory only when the act carries information about states it cannot affect. In those cases (Newcomb's problem, the twin prisoner's dilemma, copied decisions as in Sleeping Beauty) it recommends one-boxing, cooperation, and policy-like reasoning. The main objection, that this amounts to "managing the news", has most force where an act's correlation with bad outcomes runs through a common cause. Conditioning on the agent's total evidence, including her introspectible motives, often removes that correlation. On the reading developed here, EDT's distinctive verdicts are confined to cases where the world is correlated with *the decision process itself*. Whether that makes EDT the right theory of rational choice, or a subtle mistake, remains one of the central open questions in decision theory.

---

**References**

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C. & Treutlein, J. (2021). "The Evidentialist's Wager."