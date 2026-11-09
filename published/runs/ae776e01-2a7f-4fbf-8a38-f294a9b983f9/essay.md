# A-FDT: Choosing the Output of Your Own Decision Function

## 1. What this essay covers, and a note on names

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a rule of rational choice. Its abstract summarizes the rule as follows: the agent treats her decision as the output of a fixed mathematical function that answers the question, "Which output of this very function would yield the best outcome?" The paper's formal statement is Equation (4) in Section 5. That equation picks an **action** by intervening on a node that represents the decision function's output.

Footnotes 7 and 16 of the paper say the authors actually prefer a different formalization, in which the agent selects a **policy**, meaning a map from observations to actions. They set it aside "for ease of exposition." To keep the two apart, this essay uses these names:

- **A-FDT** (action functional decision theory) for the theory defined by Equation (4). This is the subject of the essay.
- **Policy-FDT** for the footnoted variant.
- **CDT** (causal decision theory) and **EDT** (evidential decision theory) for the standard rivals.

I mark three kinds of claim throughout: what the paper says, what follows mathematically from Equation (4), and operational proposals of my own.

## 2. The common frame: expected utility with a free "hypothetical" connective

The paper places all three theories inside a single expected-utility scheme (its Equation 1). The agent chooses the action $a \in \mathcal A$ that maximizes

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\, \mathcal U(o_j),
$$

where $x$ is the agent's observation history and $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed." Following Joyce, the paper treats the interpretation of $\hookrightarrow$ as the free parameter. In Joyce's words, the theories disagree "about the epistemic perspective from which actions are to be evaluated."

Write $V = \mathcal U(\textsc{Outcome})$. Then:

- **EDT** reads $\hookrightarrow$ as conditioning (Equation 2):
$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a).$$
- **CDT** reads it as a Pearl intervention on the physical act, using a causal graph $G$ (Equation 3):
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x).$$

The paper also gives a useful methodological picture. The agent holds a world-model $M$. For each option she builds a "hypothetical" $M^{a\hookrightarrow}$, which is a scratch-paper object rather than a belief or a possible world. She scores each hypothetical and acts on the best one. On this picture the theories differ in only two respects: what $M$ must contain, and how hypotheticals are carved out of it.

## 3. The definition of A-FDT

### 3.1 Equation (4)

For A-FDT, the model $P$ must contain variables for the outputs of mathematical functions, including the decision function itself. The graph $G$ must record "the logical, mathematical, computational, causal, etc. structure of the world more broadly." The paper then defines:

$$
\boxed{\;\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\; \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}
\tag{4}
$$

Here $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a node in the agent's own model. It stands for "whatever the A-FDT algorithm outputs on input $(P,G,x)$." The underlines denote dequoting: the node's name is built from the model's own contents. The paper argues that this self-reference is harmless, because representing a value does not require knowing it. Kleene's recursion theorem ("quining") shows that such self-representing data structures exist.

### 3.2 The two differences from CDT

The paper itself names exactly two differences between Equations (3) and (4).

1. **Type versus token.** CDT intervenes on $\textsc{Act}$, a physical event. A-FDT intervenes on a logical variable, the output of the decision function. Anything else that computes or models that function becomes a descendant of the intervened node. That includes the agent's own body, a twin, or a predictor's simulation. So it changes along with the intervention. In Peirce's terms, which the paper borrows, CDT intervenes on the token and A-FDT intervenes on the type.

2. **Observations select a node rather than being conditioned on.** Equation (4) contains no "$\textsc{Obs}=x$" term. In the paper's words, "FDT responds to observation by changing which node it intervenes upon." When the history changes from $x$ to $y$, the agent stops intervening on $\textsc{fdt}(\ldots,x)$ and starts intervening on $\textsc{fdt}(\ldots,y)$.

A remark on the text. In the transparent Newcomb section, the paper's display writes "$\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full})$". The calculation that follows, however, averages over worlds where box B is empty, so it does *not* condition on the observation. That calculation matches Equation (4), and I follow Equation (4) throughout.

### 3.3 Subjunctive dependence

The graph $G$ is meant to encode *subjunctive dependence*. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Two physical systems that compute the same function subjunctively depend on that function. Two calculators evaluating $6288+1048$ are the paper's example.

Causal dependence is a special case of subjunctive dependence. A scribe who copies a calculator's output depends on that output in both senses. Mere statistical correlation does not count. Two pink calculators share a color by coincidence, so they do not depend on each other.

The operational test is therefore: *would this variable change if the decision function (counterpossibly) had a different output?* A predictor's forecast passes the test. A lesion that independently causes both a craving and a cancer does not.

## 4. An operational recipe (my systematization)

The paper builds its graphs case by case. Here is a general procedure distilled from its examples. The structural steps follow the figures; the choices flagged as **[assumption]** are mine.

1. **Exogenous world variables.** List the states that do not depend on the agent's function: the infestation, the lesion, a predictor's accuracy noise, and so on. Give each its prior.

2. **One logical node per relevant input.** For every observation history $y$ that the agent might be in, add a node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$. This is the pattern in the paper's figures for the transparent Newcomb problem and both blackmail problems.

3. **Action wiring.** Set $\textsc{Act} := F_{\textsc{Obs}}$. The observation acts as a switch that decides which logical node controls the body. In the transparent Newcomb graph, the switch is the prediction, since the prediction determines what the agent sees.

4. **Subjunctive edges.** Draw an edge from $F_y$ to every variable that tracks the function's output on input $y$: the agent's act, a twin's act, and a predictor's forecast. A predictor's forecast also gets a noise parent. Do not draw such edges to variables that are only correlated with the act, like the lesion.

5. **Priors on the non-intervened nodes.** The paper leaves this open. In its examples it uses an arbitrary $q$ and observes that $q$ "doesn't matter." **[assumption]** Where $q$ does matter, I propose setting it to the agent's self-consistent prediction of her own output on that other input. Section 7 shows why this choice is not innocuous.

6. **Intervene and score.** For the current history $x$ and each $a$, compute $\mathbb E(V\mid\mathtt{do}(F_x=a))$ under the prior, *not* conditioned on $x$. Output the maximizer.

## 5. A consequence: when A-FDT agrees with CDT

The paper asserts that the three theories agree when every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$. The following short derivation is my own; it makes precise when A-FDT's unusual handling of observations matters.

**Claim.** Suppose that in $(P,G)$ the only child of $F_x$ is $\textsc{Act}$, which reads $F_x$ only when $\textsc{Obs}=x$. Suppose also that $P(\textsc{Obs}=x)>0$. Then A-FDT chooses the same action as CDT.

**Proof sketch.** $F_x$ is not an ancestor of $\textsc{Obs}$, so the intervention leaves the distribution of $\textsc{Obs}$ unchanged. Split the expectation on the observation:

$$
\mathbb E(V\mid \mathtt{do}(F_x=a)) = P(x)\,\mathbb E(V\mid x,\mathtt{do}(F_x=a)) + P(\neg x)\,\mathbb E(V\mid \neg x,\mathtt{do}(F_x=a)).
$$

On $\neg x$ worlds, $F_x$ influences nothing, so the second term is constant in $a$. On $x$ worlds, setting $F_x=a$ just sets $\textsc{Act}=a$ with the act's other parents severed. That is CDT's intervention conditioned on $x$. The argmax is therefore unchanged. ∎

So the "updateless" character of A-FDT matters only when **the decision function's output can influence which observation occurs**. That happens in exactly the cases where a predictor's forecast feeds into what the agent later sees.

The claim also exposes an edge case the paper does not discuss. If the agent's prior gives the actual history probability zero, then every action ties. Some tie-breaking or prior-smoothing convention is needed, and this would be an extra assumption.

## 6. Worked examples

All payoffs are in dollars of utility. The predictor is 99% accurate unless stated otherwise.

### 6.1 Newcomb's problem

The graph has $F\to\textsc{Act}$ and $F\to\textsc{Prediction}\to\textsc{Box B}$, with an accuracy-noise node feeding $\textsc{Prediction}$. Following the paper:

$$
\mathbb E(V\mid\mathtt{do}(F=\textit{onebox})) = 0.99\cdot 10^6 = 990{,}000,
$$
$$
\mathbb E(V\mid\mathtt{do}(F=\textit{twobox})) = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.
$$

A-FDT one-boxes.

The paper stresses that the agent need not believe in backward causation. She thinks it "foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F, G^F)$ taking on a different value." The CDT agent instead holds $\textsc{Box B}$ fixed and two-boxes.

### 6.2 Twin prisoner's dilemma

The twin computes the same function, so $F$ is a parent of both players' acts. The intervention $\mathtt{do}(F=\textit{cooperate})$ yields $10^6$, and $\mathtt{do}(F=\textit{defect})$ yields $1{,}000$. A-FDT cooperates.

### 6.3 Transparent Newcomb and Parfit's hitchhiker

The agent sees two full boxes, so she intervenes on $F_{\textit{full}}$. Let $q$ be her prior that $F_{\textit{empty}}=\textit{twobox}$. Without conditioning on "full":

$$
\mathbb E(V\mid\mathtt{do}(F_{\textit{full}}=\textit{onebox})) = 990{,}000 + 10q,\qquad
\mathbb E(V\mid\mathtt{do}(F_{\textit{full}}=\textit{twobox})) = 10{,}010 + 990q.
$$

(The paper prints the second value as "\$110,00 + q·\$990," which appears to be a typo.)

A-FDT one-boxes even while looking at the full box. In its own hypothetical for two-boxing, the box is probably empty.

The paper argues that this is "precisely equivalent to paying the driver in Parfit's hitchhiker problem." Intervening on $F_{\textit{in city}}=\textit{pay}$ makes the rescue 99% likely. Intervening on $F_{\textit{in city}}=\textit{refuse}$ makes death in the desert 99% likely.

### 6.4 The smoking lesion

The lesion fixes which utility function the agent has. So the agent's act is controlled by one of two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, depending on the lesion. Crucially, neither node is a parent of $\textsc{Cancer}$. The intervention therefore leaves $P(\textit{lesion})=p$ untouched. Smoking comes out ahead by $p\cdot 1{,}000$, so A-FDT smokes.

This is how A-FDT one-boxes and smokes "using one simple rule." The rule is the same in both problems; only the graph differs, because the dependence structures differ.

### 6.5 XOR blackmail

This is a letter-and-termite problem with an infallible predictor. Termites cost $10^6$ and occur with prior probability $p$. The letter is sent iff either there are no termites and the agent would pay, or there are termites and she would refuse. Intervening on $F_{\textit{letter}}$ changes whether the letter arrives, but not whether termites exist:

$$
\mathbb E(V\mid\mathtt{do}(F_{\textit{letter}}=\textit{pay})) = -p\cdot 10^6-(1-p)\cdot 1{,}000,
\qquad
\mathbb E(V\mid\mathtt{do}(F_{\textit{letter}}=\textit{refuse})) = -p\cdot 10^6.
$$

A-FDT refuses. EDT pays, because paying is good news about the termites.

### 6.6 Mechanical blackmail and a threshold

The blackmailer runs the program iff she predicts that the agent pays, and she wrongly predicts payment with probability $\varepsilon$. Assume, as the paper's numbers do, that a disposition to pay means the agent is always blackmailed. Then:

$$
\mathbb E(V\mid\mathtt{do}(F_{\textit{bm}}=\textit{pay}))=-1{,}000,\qquad
\mathbb E(V\mid\mathtt{do}(F_{\textit{bm}}=\textit{refuse}))=-\varepsilon\cdot 10^6.
$$

A-FDT refuses iff $\varepsilon<10^{-3}$. This matches the paper's example of $\varepsilon=0.09\%$, which gives an expected loss of \$900. The paper then says that at "0.011%" she pays. Under the stated payoffs the threshold is 0.1%, so that figure looks like a misprint for 0.11%.

Notice that she refuses "even though she *knows* that the blackmailer predicted wrongly." The hypothetical, not the actual world, determines the choice.

### 6.7 Death in Damascus

Death's appointment book is a perfect predictor, so it is a child of $F$. Then $\mathtt{do}(F=\textit{stay})$ gives death with $V=0$, and $\mathtt{do}(F=\textit{flee})$ gives death with $V=-1{,}000$. A-FDT stays.

This follows from Equation (4) by the same reasoning, although the paper does not compute it. Suppose a truly random coin is offered for \$1, one that Death cannot predict. Then $\mathtt{do}(F=\textit{buy coin})$ gives survival with probability $\tfrac12$, worth about $499{,}999$, so A-FDT buys. The paper argues that CDT, by contrast, cycles between options and declines the coin.

## 7. Open questions and how one might settle them

### 7.1 Where does $G$ come from? (Stated open by the paper.)

The paper admits that Equation (4) "rests on shakier philosophical foundations" than CDT's equation. It also writes: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

Behind this lies the problem of counterpossibles: the intended operator $\mathtt{true}(\phi)$ for false logical sentences is undefined. The paper sidesteps the problem by taking $G$ as an input.

**[Proposal]** In practice, draw an edge from $F_y$ to a variable when the variable's mechanism *evaluates or simulates* the agent's decision on input $y$. Predictors, twins and copies do this. Merely sharing an upstream cause with the decision does not qualify. This rule reproduces every graph in the paper, but it is a heuristic and not a theory.

Partial copies are a hard case: an agent whose reasoning is similar but not identical to yours. One natural rule is to model the copy's output as a noisy child of $F$, with noise reflecting the degree of similarity. That is an extra modelling commitment.

### 7.2 Priors on the other $F$ nodes, and why A-FDT is not Policy-FDT

In the paper's examples, the prior on the non-intervened nodes ($q$) does not affect the answer. That is not true in general. Here is my own illustration.

A fair coin shows R or B, and the agent observes it. A perfect predictor pays 100 iff the agent would choose *left* on both R and B. Choosing *right* earns a bonus of 1 on whichever branch it is chosen. At R, A-FDT intervenes on $F_R$, holding $q=P(F_B=\textit{left})$ at its prior:

$$
\mathbb E(V\mid\mathtt{do}(F_R=\textit{left})) - \mathbb E(V\mid\mathtt{do}(F_R=\textit{right})) = 100q - \tfrac12 .
$$

So A-FDT goes left iff $q>0.005$. Under my self-consistency rule from §4, both $(\textit{left},\textit{left})$ with $q=1$ and $(\textit{right},\textit{right})$ with $q=0$ are fixed points. The second earns 1 instead of 100.

Policy-FDT optimizes the whole map $y\mapsto a$ at once, so it selects $(\textit{left},\textit{left})$ outright. This shows concretely why the authors prefer the policy formulation.

Note that the paper says the difference matters "in certain multi-agent dilemmas." My example is a single agent coordinating with her own counterpart on another input; formally, that counterpart behaves like a second agent. For someone applying A-FDT as written, the practical advice is this: when the choice depends on $q$, report the dependence explicitly. Where appropriate, prefer the fixed point with the higher payoff. Doing so is a step toward Policy-FDT, not part of Equation (4).

### 7.3 Zero-probability histories and fairness

Section 5 showed that an actual history with prior probability zero makes every action tie. More broadly, the paper claims superiority only in "fair" problems, meaning ones where outcomes depend only on behavior, not on the decision procedure itself. It concedes, in footnote 15, that this notion of fairness is not yet formalized.

## 8. Conclusion

A-FDT is CDT with a different intervention point. It does not intervene on the physical act. It intervenes on a logical node $\textsc{fdt}(\underline P,\underline G,\underline x)$, so that twins, predictors and simulations move together with the agent's choice, while merely correlated factors stay fixed. A-FDT does not condition on observations; it lets the observation pick which logical node to intervene on.

Two consequences follow. In ordinary problems, A-FDT coincides with CDT, a fact made precise in Section 5. In Newcomb-like problems, it one-boxes, cooperates with twins, smokes, pays the driver, and refuses blackmail.

Applying A-FDT to a new case means three steps: build the dependence graph, specify priors on the non-intervened logical nodes, and maximize Equation (4). The paper determines the second and third steps. The first step, and the treatment of the priors when they matter, rests on assumptions the paper leaves open. As Section 7.2 shows, those choices can change the answer.

## References

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.* Cambridge University Press.
- Pearl, J. (2000). *Causality.* Cambridge University Press.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."