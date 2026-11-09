# Action Functional Decision Theory (A-FDT): A Working Mathematician's Guide

## 1. What is being explained

Yudkowsky and Soares (2017) describe functional decision theory as the view that an agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Their paper gives several formulations. This essay concerns the one stated as **Equation (4), Section 5**. In that formulation the agent selects an *action* for the single input it actually faces. I call this theory **A-FDT** (action functional decision theory).

Several other theories appear below, and I keep their names distinct:

- **CDT**: causal decision theory, the paper's Equation (3).
- **EDT**: evidential decision theory, Equation (2).
- **P-FDT**: the policy-selecting variant mentioned in the paper's footnotes. The authors write: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." The paper does not formalize P-FDT. I use the name only for contrast.
- **TDT**: timeless decision theory, discussed briefly in Section 4.

The source calls its theory "FDT", and quotations below keep that wording. Whenever I state results about Equation (4), I say A-FDT. Claims that are my own additions, rather than the source's, are marked as such.

## 2. The formal definition

### 2.1 Common ground: expected utility over hypotheticals

The paper treats EDT, CDT and A-FDT as expected-utility theories that differ only in how they interpret the decision conditional "$a \hookrightarrow o$". The shared template is

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history and $V := \mathcal U(\textsc{Outcome})$. Following Joyce, the paper says the theories disagree "about the epistemic perspective from which actions are to be evaluated". Each one tells the agent how to build, for each candidate action, a *hypothetical*: a modified world-model used only as a computational tool.

The three rules are:

$$
\mathrm{EDT}(P,x) = \arg\max_{a}\ \mathbb E(V \mid \textsc{Obs}=x,\ \textsc{Act}=a) \tag{2}
$$

$$
\mathrm{CDT}(P,G,x) = \arg\max_{a}\ \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}
$$

$$
\text{A-FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big) \tag{4}
$$

### 2.2 The ingredients of Equation (4)

**The world-model $(P,G)$.**
- $P$ is a probability distribution over variables.
- $G$ is a graph saying how changing one variable propagates to others.
- For CDT, $G$ encodes causal structure only. For A-FDT, the source requires $G$ to encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly." In particular, $P$ must contain variables standing for *outputs of mathematical functions*.

**The intervention node $\textsc{fdt}(\underline P,\underline G,\underline x)$.**
- This variable represents "the output of the decision algorithm when run on inputs $(P,G,x)$."
- The underlines denote dequoting: the variable's *name* is built from the agent's own model and observation.
- This is self-referential, but the paper argues the self-reference is harmless. The agent needs a variable *representing* its output, not the output's value. Kleene's recursion theorem ("quining") shows such self-representations can be constructed.

**The operator $\mathtt{do}$.**
- This is Pearl's surgery. It cuts the edges into the intervened node, sets its value, and recomputes everything downstream according to $G$.
- Variables not downstream keep their prior distribution.

### 2.3 Two structural differences from CDT

The paper identifies two differences between Equations (3) and (4).

1. **Point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type, namely the function's output. Anything that subjunctively depends on that output therefore co-varies with it in the hypothetical. This includes the agent's body, but also a twin, a predictor's simulation, or Death's appointment book.

2. **Treatment of observation.** Equation (4) contains no conditioning on $\textsc{Obs}=x$. Observations enter only through *which node is intervened on*:

   > "When CDT's observation history updates from $x$ to $y$, CDT changes from conditioning its model on $\textsc{Obs}=x$ to conditioning its model on $\textsc{Obs}=y$, whereas FDT changes from intervening on the variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead."

The second point is easy to miss, and it drives A-FDT's most striking verdicts (Section 4).

### 2.4 When the three theories agree

If every correlation in $(P,G)$ between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from the dependence of $\textsc{Act}$ on the fdt node), then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$

and all three theories recommend the same action. A-FDT is therefore conservative in ordinary problems. It diverges only where something *other than the agent's own action* tracks the agent's decision procedure: predictors, copies, simulations, and similar.

## 3. Subjunctive dependence: what goes into $G$

The intuitive slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." The paper says two physical systems computing the same function both "subjunctively depend" upon that function. Its standard illustration is two calculators computing $6288+1048$.

The relation has three key features:

- **Causal dependence is a special case.** A scribe copying the output of a calculator depends on it both causally and subjunctively.
- **Statistical correlation is not enough.** Two coincidentally pink calculators do not depend on each other. Likewise, a lesion that correlates with smoking does not "evaluate the agent's future decisions."
- **Dependence can be noisy.** An imperfect predictor is modeled by an edge from the fdt node into $\textsc{Prediction}$, plus an independent noise node such as $\textsc{Accurate}$.

The central A-FDT modeling question is therefore:

> **Which variables would differ if this function returned a different output on this input?**

Those variables receive arrows from the fdt node. Everything else is left untouched by the intervention. The paper defends the asymmetry between Newcomb's problem and the smoking lesion on exactly this basis: a predictor models the agent, while a lesion does not.

## 4. Worked examples

All numbers below use dollars as utility, as in the source.

### 4.1 Newcomb's problem

**Graph.** The node $\textsc{fdt}(\underline P,\underline G)$ has arrows to $\textsc{Act}$ and to $\textsc{Prediction}$. $\textsc{Prediction}$ is also affected by $\textsc{Accurate}$, with probability $0.99$ of being accurate.

**Hypotheticals.**
- $\mathtt{do}(\textsc{fdt}=\textit{onebox})$ makes box B full with probability $0.99$, so $\mathbb E V=990{,}000$.
- $\mathtt{do}(\textsc{fdt}=\textit{twobox})$ makes box B full with probability $0.01$, so $\mathbb E V = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000$.

**Verdict.** A-FDT one-boxes.

CDT's surgery on $\textsc{Act}$ leaves $P(\textit{full})=p$ fixed. Two-boxing is then better by $1{,}000$ whatever $p$ is, so CDT two-boxes.

### 4.2 The smoking lesion

This case shows how A-FDT handles uncertainty about *which* node controls one's action. The lesion fixes the agent's tastes. There are therefore two candidate procedures:

- $\textsc{fdt}(\underline{P_S},\underline G)$, which runs if the agent has the lesion and likes smoking;
- $\textsc{fdt}(\underline{P_R},\underline G)$, which runs otherwise.

$\textsc{Act}$ copies whichever procedure the lesion selects. $\textsc{Cancer}$ depends on $\textsc{Lesion}$ and luck, and on no fdt node.

Let $p$ be the probability of the lesion and $q$ the agent's credence that the $R$-procedure smokes. Intervening on the $S$-node leaves $P(\textit{lesion})=p$ unchanged. The paper's two expected utilities are:

- smoke: $p(10{,}000+1{,}000)+(1-p)(990{,}000+q\,1{,}000)$;
- refrain: $p(10{,}000)+(1-p)(990{,}000+q\,1{,}000)$.

Smoking wins by $p\cdot 1{,}000$, so A-FDT smokes. The prior on the intervened node itself is irrelevant, because $\mathtt{do}$ overwrites it.

### 4.3 Transparent Newcomb

Both boxes are visible, and the agent sees box B full. Fiona, the paper's A-FDT agent, uses a graph with two logical nodes:

- $F_{\text{full}} := \textsc{fdt}(\underline P,\underline G,\textit{full})$, which drives $\textsc{Prediction}$;
- $F_{\text{empty}}$.

$\textsc{Prediction}$ determines which node controls $\textsc{Act}$. Let $q$ be the prior probability that $F_{\text{empty}}=\textit{twobox}$.

**One-box.**
- With probability $0.99$ the prediction is accurate, the box is full, and the agent one-boxes for $1{,}000{,}000$.
- With probability $0.01$ the prediction is wrong, the box is empty, and $F_{\text{empty}}$ acts.
- Total: $\mathbb E V = 990{,}000 + 10q$.

**Two-box.**
- With probability $0.99$ the box is empty and $F_{\text{empty}}$ acts.
- With probability $0.01$ the box is full and the agent takes both boxes.
- Total: $\mathbb E V = 0.01(1{,}001{,}000)+0.99q(1{,}000) = 10{,}010+990q$.

(I computed these figures myself. The source's printed constant "\$110,00" appears to be a typesetting slip for \$10,010.)

**Verdict.** One-boxing wins for every $q\in[0,1]$.

Notice that in the two-box hypothetical, the agent mostly imagines seeing an *empty* box, although it has observed a full one. This is the "no conditioning on $\textsc{Obs}$" feature at work. The paper argues the same structure underlies paying the driver in Parfit's hitchhiker, which it calls "precisely equivalent".

### 4.4 XOR blackmail

This example uses the source's setup with an infallible predictor. My own calculation shows how the absence of conditioning plays out. Let $p=P(\textit{termites})$.

The letter is sent iff exactly one of the following holds:
- (i) no termites and the agent pays;
- (ii) termites and the agent refuses.

**$\mathtt{do}(F_{\text{letter}}=\textit{pay})$.** The letter arrives iff there are no termites.
- Termites: the agent loses $1{,}000{,}000$ and never sees the letter.
- No termites: the agent pays $1{,}000$.
- $\mathbb E V=-10^6 p-1{,}000(1-p)$.

**$\mathtt{do}(F_{\text{letter}}=\textit{refuse})$.** The letter arrives iff there are termites.
- $\mathbb E V=-10^6 p$.

**Verdict.** Refusing wins by $1{,}000(1-p)$. The infestation is upstream of everything, so no intervention moves it. Paying only changes *which* worlds contain the letter.

EDT conditions on the letter and pays. CDT refuses, but for a different reason: in its hypothetical the infallible predictor errs.

### 4.5 Mechanical blackmail with a fallible blackmailer

Suppose the blackmailer wrongly predicts payment with probability $\varepsilon$, and the leak costs $10^6$.

- Paying gives $-1{,}000$, because the agent is (essentially) always blackmailed.
- Refusing gives $-\varepsilon\cdot 10^6$.

So A-FDT refuses iff $\varepsilon<10^{-3}$. The source's illustrations are $0.0009$ (refuse) and a figure printed as "0.011%" (pay). That second figure lies *below* the threshold, so it presumably intends 0.11%. Either way, the procedure is unambiguous: compute the threshold.

### 4.6 Death in Damascus and twins

**Death in Damascus.** Death's appointment book depends subjunctively on the agent's function. Under either intervention, Death is wherever the agent is. A-FDT therefore stays in Damascus and saves the $1{,}000$. There is no instability, because the hypotheticals never separate the action from the prediction.

**Twin prisoner's dilemma.** One fdt node drives both prisoners' actions. Cooperation yields $10^6$ in the hypothetical and defection yields $10^3$, so A-FDT cooperates.

## 5. Why no conditioning? The "global perspective"

Equation (4) evaluates actions from what the paper calls a global perspective: "What would the entire universe look like if the FDT algorithm behaved differently?" The agent may imagine that, had its output differed, it "might have *made different observations*."

The authors contrast this with timeless decision theory (TDT). In a footnote they say TDT "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

The payoff is a form of dynamic consistency. The paper claims:
- A-FDT agents "act as they would have precommitted to act";
- they do not assign negative value to information;
- they are reflectively stable in "fair" problems, meaning problems where outcomes depend only on the agent's behavior and not on its internal procedure.

These are the source's claims. The examples above illustrate them; the paper does not prove them in general.

## 6. What the source leaves open, and how one might operationalize it

### 6.1 Constructing $G$

The paper is candid that A-FDT presupposes a graph it cannot yet derive:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

A logically clean alternative would be a $\mathtt{true}$ operator over counterpossible sentences. That operator is undefined, so the dependence structure is supplied as an input to the theory, just as CDT takes causal structure as an input.

**Operational proposal (mine).** Draw an edge from $\textsc{fdt}(\underline P,\underline G,\underline y)$ into variable $Z$ when $Z$ is produced by a process that *computes or reliably models* the agent's decision on input $y$. Examples are a simulation, a copy, a predictor reasoning about the agent's algorithm, or a future self facing an indistinguishable decision (compare the paper's gym example). Then:

- Quantify unreliability with an independent noise node, as with $\textsc{Accurate}$.
- Leave unedged any variable whose correlation with $\textsc{Act}$ runs through tastes, lesions, cosmic rays, or other channels that do not evaluate the decision.
- Similar-but-different agents, such as a CDT agent facing the A-FDT agent, should get an edge only to the extent that their output is computed by, or reliably tracks, the same function.

This proposal settles all of the paper's examples. It leaves genuinely hard cases open, such as partial algorithmic similarity, as the source itself does.

### 6.2 The other logical nodes and the prior $q$

Equation (4) intervenes only on the node for the actual input $x$. Nodes $\textsc{fdt}(\underline P,\underline G,\underline y)$ for $y\neq x$ keep their *prior* distribution. The source notes "the correct $q$" in its examples (0 for the lesion case, 1 for transparent Newcomb) but shows that $q$ did not matter there. In general it can matter. Here is a formalization of when it matters (my contribution).

**Assumptions.**
- (A1) The logical nodes $\{F_y\}_{y\in Y}$ are roots of $G$.
- (A2) They are probabilistically independent of each other and of the exogenous noise $N$.
- (A3) $V=h\big((F_y)_y, N\big)$ for some function $h$.

**Definition.** Write $U(\pi)=\mathbb E_N[h(\pi,N)]$ for a deterministic profile $\pi:Y\to\mathcal A$.

Under these assumptions, Equation (4) at input $x$ maximizes

$$
\mathbb E_{F_{-x}\sim P}\,U(a, F_{-x}).
$$

**Proposition.**
1. A-FDT at $x$ is a best response to the agent's own beliefs about its outputs on other inputs. The "players" are the inputs, and they share the common payoff $U$.
2. Call $\pi$ *reflectively consistent* if, when $P$ puts point mass on $\pi$, we have $\pi(x)\in\text{A-FDT}(P,G,x)$ for every $x$. Then every $U$-maximizing profile, which is P-FDT's choice, is reflectively consistent.
3. Reflectively consistent profiles can nonetheless be suboptimal.

*Proof sketch.* Parts 1 and 2 hold because a global maximum of a common payoff admits no profitable unilateral deviation. Part 3 is shown by the next example. ∎

**Example (my construction).** An agent is duplicated into two rooms.
- One copy observes "L"; the other observes "R".
- Each picks $\alpha$ or $\beta$.
- Each copy receives $10$ if both pick $\alpha$, $6$ if both pick $\beta$, and $0$ otherwise.

For the L-copy, $\mathbb E V(\alpha)=10\,P(F_R=\alpha)$ and $\mathbb E V(\beta)=6\,P(F_R=\beta)$. So A-FDT picks $\alpha$ iff $P(F_R=\alpha)>3/8$.

If the agent's prior says its R-self plays $\beta$, then $(\beta,\beta)$ is self-confirming. P-FDT selects $(\alpha,\alpha)$ outright. This is presumably the kind of case the footnote means by "certain multi-agent dilemmas".

**Two remedies, both additional assumptions.**
- (a) Add edges between logical nodes when the computations are known to coincide. In the example, symmetric inputs could justify identifying $F_L$ with $F_R$. This changes $G$, not Equation (4).
- (b) Adopt P-FDT.

Read strictly, A-FDT needs a supplementary norm for its priors over its own other-input outputs. The natural candidate is reflective consistency, and the proposition shows that this norm under-determines the outcome when there are multiple equilibria.

### 6.3 Smaller gaps

- **Ties.** The argmax may be set-valued. The paper specifies no tie-breaking rule.
- **Bounded agents.** The paper studies idealized maximization. It conjectures that approximations inherit the ideal's comparative strengths, but does not show this.
- **Fairness.** The claim that A-FDT is unbeaten on "fair" problems awaits a formal definition of fairness. The paper itself notes obstacles, such as an adversary that punishes whoever matches a copy of the agent.

## 7. A recipe for unfamiliar cases

1. **Fix the input.** Identify the actual observation history $x$.
2. **List computations of your function.** Find every process that computes, simulates, or predicts your decision on any input. Include counterfactual inputs that a predictor conditions on, such as "upon seeing the full box". Create a node $\textsc{fdt}(\cdot,\cdot,y)$ for each relevant $y$.
3. **Draw edges.**
   - From each logical node to your action on that input.
   - To each predictor or copy that tracks it, with noise nodes for unreliability.
   - From environment variables to whatever selects which input you receive.
4. **Leave purely statistical correlates unedged.**
5. **Assign priors** to non-intervened logical nodes. Ideally use reflectively consistent ones, and check sensitivity to these priors.
6. **For each action $a$**, set $\textsc{fdt}(\cdot,\cdot,x)=a$ *without conditioning on $x$*, propagate through $G$, and compute $\mathbb E V$.
7. **Choose the maximizer.** If the choice depends on the priors in step 5, report the dependence, or note where P-FDT would differ.

## 8. Conclusion

A-FDT, as given in Equation (4), is CDT's expected-utility machinery with two changes:

- the intervention target moves from the physical act to the logical output of the agent's decision function on its actual input;
- observations select the intervention target instead of being conditioned on.

These two changes produce one-boxing, smoking, paying the hitchhiker's driver, refusing both blackmails, and staying in Damascus. All follow from one rule plus an honest model of who is computing what.

The theory's precision is bounded by its inputs. The dependence graph $G$ must be supplied, and the source identifies its construction as the main open problem. The priors over one's outputs on other inputs are not fixed by Equation (4). Under natural assumptions, A-FDT is a best response within a common-payoff game among one's own input-indexed instances. It always admits P-FDT's optimum as a consistent choice, but does not by itself select that optimum. Distinguishing what the paper establishes from what these supplementary assumptions add is, I think, the right starting point for applying A-FDT to new cases.

---

**References**

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.*
- Pearl, J. (2000). *Causality.*