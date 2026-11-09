# A-FDT: Choosing the Output of Your Own Decision Function

## 1. What A-FDT is

Yudkowsky and Soares (2017) present *functional decision theory* as a rival to causal decision theory (CDT) and evidential decision theory (EDT). The core slogan is that a rational agent should treat her decision as the output of a fixed mathematical function that asks, "Which output of this very function would yield the best outcome?"

The paper gives one fully explicit formula, its Equation (4). In that formula the thing being chosen is an **action** $a\in\mathcal A$. The paper also signals, in a footnote, that this is not the authors' preferred version:

> "In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

I therefore use two names in this essay:

- **A-FDT (action functional decision theory)** is the rule defined by Equation (4). It is the subject of this essay. The paper itself just calls it "FDT."
- **P-FDT (policy functional decision theory)** is the policy-selecting variant the footnote mentions. The paper does not formalize it.

Throughout, I separate three kinds of claim: what the source says, what follows from its equations, and what I propose myself. My own proposals are marked **[Proposal]**.

## 2. The common frame: expected utility with a free "hypothetical" connective

All three theories maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $x$ is the agent's observation history, and $a\hookrightarrow o_j$ reads "if $a$ were done, $o_j$ would result." Following Joyce (1999), the paper treats the meaning of $\hookrightarrow$ as the only free parameter. In Joyce's words, quoted in the paper, decision theories "disagree about the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model $M$. For each option she builds a *hypothetical*, which is a modified copy of $M$ representing "what the world would look like" under that option. She then scores each hypothetical by its expected utility. The paper describes hypotheticals as "notes on scratch paper: transient, useful, and possibly quite representationally thin." They are tools for deciding, not beliefs about how the world is.

The three theories differ in how they build the hypothetical. Write $V=\mathcal U(\textsc{Outcome})$:

$$
\begin{aligned}
\text{EDT}(P,x) &= \arg\max_a \ \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) && (2)\\
\text{CDT}(P,G,x) &= \arg\max_a \ \mathbb E\big(V \mid do(\textsc{Act}=a),\ \textsc{Obs}=x\big) && (3)\\
\text{A-FDT}(P,G,x) &= \arg\max_a \ \mathbb E\big(V \mid do(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big) && (4)
\end{aligned}
$$

In these formulas:

- $P$ is a probability distribution.
- $G$ is a directed graph telling the $do$-operator which variables are downstream of which.
- $do(\cdot)$ is Pearl's intervention. It sets a node to a value, recomputes everything downstream of it, and leaves everything else at its prior distribution.

## 3. Anatomy of Equation (4)

Equation (4) differs from CDT's Equation (3) in two ways. The source states both explicitly.

**(i) The intervention target is logical, not physical.** CDT intervenes on $\textsc{Act}$, the node for what the agent's body does. A-FDT intervenes on $\textsc{fdt}(\underline P,\underline G,\underline x)$. This node represents *the output of the A-FDT algorithm when run on this very model and these very observations*. The underlines indicate dequoting: the node's *name* is built from the agent's actual model.

This is self-referential, and the paper defends the self-reference as harmless. The agent does not need to know the node's value in order to have a variable representing it. Kleene's recursion theorem ("quining") shows that such self-representing data structures exist.

In the paper's Peircean terms, CDT intervenes on the *token* (this act). A-FDT intervenes on the *type* (what this function outputs, wherever it is computed).

**(ii) Observations change *where* the agent intervenes, not *what she conditions on*.** Equation (3) conditions on $\textsc{Obs}=x$. Equation (4) does not. In A-FDT, $x$ appears only inside the name of the intervened node. When observations change from $x$ to $y$, the agent switches from intervening on $\textsc{fdt}(\ldots,\underline x)$ to intervening on $\textsc{fdt}(\ldots,\underline y)$.

So the graph must contain sibling nodes $\textsc{fdt}(\underline P,\underline G,\underline y)$ for observations $y\neq x$ that the agent might have received. In each hypothetical those siblings are not intervened on, so they stay at their prior distributions. This detail does a lot of work in the examples below. It is also where A-FDT and P-FDT come apart.

Because the antecedent "$\textsc{fdt}(P,G,x)=a$" is false of logical necessity for all but one $a$, these are *counterpossible* hypotheticals. The paper does not try to define a general $\mathtt{true}(\phi)$ operator for conditioning on logical sentences. Instead it requires the graph $G$ to encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly." Pearl's $do$ is then reused on that graph.

**When A-FDT agrees with its rivals.** Suppose every correlation between $\textsc{Act}$ and other variables is produced by $\textsc{Act}$ itself, apart from $\textsc{Act}$'s dependence on the $\textsc{fdt}$ node. Then the paper shows

$$
\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\textsc{fdt}=a)].
$$

In that case EDT, CDT and A-FDT all agree. They diverge only when something other than the act correlates with the act. The central example is a predictor.

## 4. Subjunctive dependence: what goes into $G$

The concept that tells you how to draw $G$ is *subjunctive dependence*. The source's formulation is:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Two physical systems subjunctively depend on a function when both compute it, or reliably model it. The paper's illustration is two well-functioning calculators computing $6288+1048$ on opposite sides of the globe.

- **Causal dependence is a special case.** A scribe copying the calculator's output depends on that output both causally and subjunctively.
- **Mere correlation is not subjunctive dependence.** If two calculators happen to share a colour, neither colour depends on the other.

The resulting drawing rule is:

- A predictor's prediction, a twin's choice, or Death's appointment book gets an arrow *from* the $\textsc{fdt}$ node.
- A carcinogenic lesion, a common-cause predisposition, or a termite infestation does not, because these do not compute or model the agent's decision function.

Imperfect predictors are handled by giving the prediction an extra noise parent. In the paper this is $\textsc{Accurate}$, with $P(\textit{accurate})=0.99$.

## 5. Applying A-FDT: worked cases

The procedure in every case is the same:

1. Write down $(P,G)$ with the $\textsc{fdt}$ nodes.
2. Intervene on the node indexed by your actual observation.
3. Propagate the intervention downstream.
4. Leave everything else at its prior, including sibling $\textsc{fdt}$ nodes.
5. Compare expected utilities.

### Newcomb's problem

In the graph, $\textsc{fdt}(\underline P,\underline G)$ points to both $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Prediction}$ also has the parent $\textsc{Accurate}$, and Box B is filled iff the prediction is "one-box."

$$
\begin{aligned}
\mathbb E[V\mid do(\textsc{fdt}=\textit{onebox})] &= 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,\\
\mathbb E[V\mid do(\textsc{fdt}=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes.

CDT's graph has no arrow from the act to the prediction. Under CDT, $P(\textit{full})=p$ in both hypotheticals, so two-boxing wins by \$1,000 for every $p$.

The paper stresses that the A-FDT agent does not believe in backward causation. She only refuses to imagine her action changing without also imagining a change in the function the predictor is modelling.

The Twin Prisoner's Dilemma works the same way. The twin's choice is a second child of the same $\textsc{fdt}$ node, so cooperating yields \$1,000,000 and defecting yields \$1,000.

### Smoking lesion

Here the lesion does not compute anything about the agent's decision function, so there is no arrow from $\textsc{fdt}$ to $\textsc{Cancer}$.

The paper formalizes the lesion as also fixing the agent's utility function: $\mathcal U_S$ (likes smoking) or $\mathcal U_R$ (does not). There are therefore two decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$, and the lesion determines which one controls $\textsc{Act}$.

Intervening on the $S$-node leaves $P(\textit{lesion})=p$ unchanged. Smoking then beats refraining by exactly $p\cdot\$1{,}000$, so A-FDT smokes.

This case shows A-FDT is not EDT in disguise. It breaks correlations that do not run through its own decision function.

### Transparent Newcomb

The agent sees that both boxes are full. Box B was filled iff the predictor predicted she would one-box *upon seeing a full box*.

The graph has two decision nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction depends on $F_{\text{full}}$, and the prediction determines which node controls $\textsc{Act}$. A-FDT intervenes on $F_{\text{full}}$. The sibling $F_{\text{empty}}$ stays at its prior; let $q$ be the prior probability that the agent two-boxes on seeing an empty box.

With the predictor 99% accurate:

$$
\begin{aligned}
\text{one-box: } &0.99(1{,}000{,}000)+0.01\,(1{,}000q)=990{,}000+10q,\\
\text{two-box: } &0.01(1{,}001{,}000)+0.99\,(1{,}000q)=10{,}010+990q.
\end{aligned}
$$

(The extracted source prints the two-box line as "$110,00 + q·$990"; the correct constant is \$10,010.)

One-boxing wins for every $q\in[0,1]$. Notice what happened: although the agent *sees* a full box, her two-box hypothetical is mostly a world in which the box was empty. This is the formal content of the paper's claim that A-FDT agents "entertain the hypothesis that, if their action were different, they might have *made different observations*." Parfit's hitchhiker has the same structure, so A-FDT pays the driver.

### XOR blackmail: why "do not condition on $\textsc{Obs}$" matters

A perfect predictor sends a letter iff exactly one of the following holds:

- there are no termites and the agent would pay \$1,000 on receiving the letter, or
- there are termites and she would not pay.

Let the prior probability of termites be $p$. Termite damage costs \$1,000,000. A-FDT intervenes on $F_{\text{letter}}$ and does **not** condition on having received the letter:

- **Pay:** the letter arrives exactly in the no-termite worlds, so $\mathbb E[V]=-(1-p)\,1{,}000-p\,1{,}000{,}000$.
- **Refuse:** the letter arrives exactly in the termite worlds, so $\mathbb E[V]=-p\,1{,}000{,}000$.

Refusing wins by $(1-p)\cdot\$1{,}000$. The intervention changes whether the letter arrives, not whether there are termites. This agrees with the paper's verdict.

Now consider a variant that both intervenes and also conditions on $\textsc{Obs}=\textit{letter}$. Paying would then imply no termites (−\$1,000), and refusing would imply termites (−\$1,000,000). That agent pays, which is EDT's mistake. The paper notes, in a passage attributing it to Timeless Decision Theory, that intervening *and* conditioning "creates a kind of 'double update' which proves harmful in practice." The absence of $\textsc{Obs}=x$ from Equation (4) is therefore deliberate and load-bearing.

### Mechanical blackmail with an imperfect predictor

The blackmailer runs a damaging program iff she predicts the agent would pay. Let $\varepsilon$ be the probability that she wrongly predicts payment.

- If A-FDT pays, it is always blackmailed and always loses \$1,000.
- If A-FDT refuses, it is blackmailed with probability $\varepsilon$ and then loses \$1,000,000.

So refusal is optimal iff $\varepsilon\cdot 10^6 < 10^3$, that is, iff $\varepsilon<0.1\%$. The paper's two examples sit on either side of this threshold: at $\varepsilon=0.09\%$ the agent refuses, and at its second example (printed as 0.011% but evidently meaning 0.11%) she pays.

The broader lesson is that A-FDT's apparent stubbornness is not dogmatic. It is ordinary expected-utility arithmetic over hypotheticals that include the predictor's response.

### Death in Damascus

Death's appointment book is a child of the $\textsc{fdt}$ node. Staying yields death; fleeing yields death plus the \$1,000 cost of the journey. A-FDT stays, without the instability or ratification machinery the paper attributes to CDT.

## 6. Dominance and the global perspective

The paper argues that "every method for constructing hypotheticals gives rise to its own notion of dominance."

- Two-boxing dominates only under CDT hypotheticals, which hold the prediction fixed while the act varies.
- If dominance is instead defined by holding subjunctive dependencies fixed, A-FDT never takes a dominated action.

Dominance therefore cannot settle the dispute neutrally. The paper's own criterion is utility achieved in "fair" problems: problems in which outcomes depend only on the agent's behaviour, not on the procedure that produced it. The authors report they "have not been able to construct an intuitively fair dilemma where FDT loses to a rival decision theory," and they acknowledge that fairness has not yet been formalized.

The philosophical picture is that A-FDT asks what the entire universe would look like if this function produced output $a$. The paper also argues that any objection to "controlling" a logical fact applies equally to a deterministic CDT agent "controlling" its physical act.

## 7. Open questions and operational interpretations

### 7.1 Where does $G$ come from?

The source is explicit that this is unresolved:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

Equation (4) is well defined only *given* $G$.

**[Proposal]** A practical recipe for hand-built models:

1. List every process in the scenario whose output is computed from, or trained to track, the agent's decision behaviour. Examples are simulations, mental models, track records used as predictors, and copies of the agent.
2. For each input $y$ on which such a process evaluates the agent, add a node $F_y=\textsc{fdt}(\underline P,\underline G,\underline y)$ with an arrow to that process. Represent the process's unreliability as a separate noise parent.
3. Make the observation node a *selector*: $\textsc{Act}$ copies whichever $F_y$ matches the realized observation. If upstream variables determine what is observed, they also determine which node is selected.
4. Leave purely statistical correlates (genes, lesions, demographic base rates) without an arrow from any $F_y$. They may still be correlated with $\textsc{Act}$ through common causes, and A-FDT will ignore those correlations exactly as CDT does.

The hard cases this recipe does not settle are partial similarity: a predictor running a *related but different* algorithm, or a "twin" who reasons somewhat differently. The paper's calculator analogy suggests treating the dependence as noisy, but how much noise to assign is not specified.

### 7.2 Priors on sibling decision nodes, and A-FDT versus P-FDT

Equation (4) leaves the non-intervened nodes $F_y$, for $y\neq x$, at their prior distribution. The paper says the prior on the *intervened* node is "inconsequential," and in transparent Newcomb and in the lesion case the sibling priors ($q$) happen not to affect the verdict. Nothing guarantees this in general.

Here is an illustration of my own. A fair coin shows the agent card $L$ or card $R$, and she then chooses $a$ or $b$. Before the flip, a perfect predictor evaluated her function on both cards. It pays \$2,000 if she would choose $b$ on both, \$1,000 if $a$ on both, and nothing otherwise. Her action has no other effect.

Suppose she sees $L$, and let $r=P(F_R=b)$ be her prior that she chooses $b$ on card $R$. Then

$$
\mathbb E[V\mid do(F_L=a)] = 1{,}000\,(1-r),\qquad
\mathbb E[V\mid do(F_L=b)] = 2{,}000\,r .
$$

A-FDT picks $b$ iff $r>1/3$. If her self-model expects $a$ at $R$, she chooses $a$ at $L$. By symmetry she does the same at $R$, and the self-confirming profile $(a,a)$ earns \$1,000. The profile $(b,b)$ is also self-confirming. A-FDT applied input-by-input behaves like a set of players, one per observation, who may settle into an inferior equilibrium.

P-FDT avoids this. It would maximize over the four policies $\{L,R\}\to\{a,b\}$ and pick $(b,b)$, earning \$2,000. This fits the paper's remark that the action/policy difference matters "in certain multi-agent dilemmas": the predictor here is the second agent. I offer this as an illustration of that remark, not as the authors' own example.

**[Proposal]** To apply A-FDT responsibly:

- **Robustness check.** Compute the A-FDT verdict as a function of the sibling priors. If it is the same over the whole range, as in transparent Newcomb, where one-boxing wins for all $q\in[0,1]$, the verdict is determinate.
- **Reflective consistency.** If the verdict does depend on the sibling priors, require them to match what A-FDT itself outputs at those inputs. This is a fixed-point condition.
- **Report multiplicity.** If several fixed points remain, say so. Equation (4) alone does not choose among them, and choosing the best one amounts to adopting P-FDT.

### 7.3 A notational ambiguity

In the transparent Newcomb discussion, the paper writes the objective as $\mathbb E(V \mid do(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full}))$, with an unbalanced parenthesis.

Read literally, this would condition on $\textsc{Obs}$. But the paper's own calculation does not condition: it averages over worlds where Box B is empty. That calculation also matches Equation (4) and the explanation of the "double update." I therefore read the displayed expression as a typo and treat Equation (4) as authoritative.

### 7.4 Ties, zero-probability options, and computability

Equation (4) does not specify how to break ties in the argmax. Unlike EDT, it has no problem with options of prior probability zero, because $do$ is defined even for zero-probability values.

The paper treats exact maximization over realistic models as intractable. It studies the idealized rule on the expectation that bounded approximations would inherit its comparative strengths.

## 8. Conclusion

A-FDT is the rule

$$
\arg\max_a \mathbb E\big[V \mid do(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big].
$$

In words: pretend to set the output of your own decision function, on your actual input, to each candidate action. Propagate that change to everything that computes or predicts the function. Leave everything else, including your observation, at its prior distribution. Then pick the best result.

Two structural choices produce the theory's distinctive verdicts:

- intervening on a logical node rather than on the physical act, and
- letting observations select the intervention point rather than serve as conditions.

Those verdicts are one-boxing, smoking, paying the hitchhiker's driver, refusing both kinds of blackmail, and staying in Damascus.

Two gaps remain. The first, emphasized by the source, is that the subjunctive-dependence graph $G$ is an input that no one yet knows how to learn. The second, which follows from the action form of Equation (4), is that verdicts can depend on the agent's priors about her own behaviour at other inputs. That can leave A-FDT at a suboptimal fixed point which the policy version, P-FDT, would avoid. Used with an explicit $G$ and a check that the verdict is robust to those sibling priors, A-FDT is a precise procedure for deciding new cases.

**Reference.** Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060. (Also cited via the paper: Joyce 1999; Pearl 2000.)