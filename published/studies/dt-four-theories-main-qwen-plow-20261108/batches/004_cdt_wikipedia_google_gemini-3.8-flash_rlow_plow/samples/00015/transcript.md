# 004_cdt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00015

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/cd3687cb-6507-4797-b6fe-6125b3801e22/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/cd3687cb-6507-4797-b6fe-6125b3801e22/call_0/response.raw) · finish: `stop`

### Visible response

````text
# The Mechanics of Agency: A Mathematical Exposition of Causal Decision Theory

Rational choice theory is traditionally framed as the maximization of expected utility: an agent facing a partition of mutually exclusive, exhaustive actions $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ chooses whichever option yields the greatest subjective payoff. Yet the moment one writes down the expectation, a subtle conceptual fissure emerges. Does an agent evaluate an action according to the *evidence* it provides about the world, or according to the *consequences* it causally brings about?

Evidential Decision Theory (EDT)—most famously formalized by Richard Jeffrey—computes expectations via conditional probabilities: $V(A) = \sum_j P(O_j \mid A) U(O_j)$. While mathematically clean, EDT famously stumbles in environments where actions serve as symptoms of preexisting or externally driven states without causally producing them. In response, **Causal Decision Theory** (CDT) was developed by Allan Gibbard, William Harper, David Lewis, and others. CDT insists that genuine rational choice requires optimizing what one can *bring about*, not what one can merely *diagnose*.

This essay provides a rigorous mathematical formulation of CDT, contrasts its mechanics with EDT, examines how it evaluates dependencies and counterfactuals, resolves ambiguities in the formal framework using modern causal graphical models, and dissects standard paradoxes, counterexamples, and open problems.

---

## 1. Formal Foundations: The Gibbard–Harper Counterfactual Formulation

In their seminal 1981 paper, Allan Gibbard and William Harper formulated CDT by replacing standard conditional probabilities with the probabilities of counterfactual conditionals. 

Let:
- $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be the set of available actions.
- $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ be a partition of possible outcomes.
- $D: \mathcal{O} \to \mathbb{R}$ be a utility (or "desirability") function.
- $A \mathbin{\Box\to} O$ (often written simply as $A \to O$) denote the counterfactual proposition: *"If the agent were to perform action $A$, outcome $O$ would occur."*

Gibbard and Harper define the **causal expected utility** (frequently denoted $U$, in contrast to Jeffrey’s evidential desirability $V$) of an action $A \in \mathcal{A}$ as:

$$
U(A) = \sum_{j=1}^m P(A \mathbin{\Box\to} O_j) \, D(O_j)
$$

Here, $P$ represents the agent’s subjective probability measure over the algebra of propositions, which includes both factual and counterfactual propositions.

### 1.1 The Divergence Between Counterfactuals and Conditionals

The core divergence between CDT and EDT reduces to whether:

$$
P(A \mathbin{\Box\to} O_j) \stackrel{?}{=} P(O_j \mid A)
$$

If this identity held universally, CDT and EDT would be indistinguishable. However, David Lewis (1976) demonstrated through his celebrated **Triviality Result** that the probability of a conditional cannot, in general, be equated with the conditional probability. Lewis showed that if $P(A \to B) = P(B \mid A)$ holds systematically for all propositions and is preserved under Bayesian conditionalization, the probability calculus collapses into a trivial system where no more than two mutually incompatible propositions can carry positive probability.

Gibbard and Harper demonstrated that $P(A \mathbin{\Box\to} O_j) = P(O_j \mid A)$ holds if one assumes:
1. The Principle of Conditional Excluded Middle: $(A \mathbin{\Box\to} O) \lor (A \mathbin{\Box\to} \neg O)$ is a tautology; and
2. **Statistical independence** between the action $A$ and the counterfactual conditional $A \mathbin{\Box\to} O_j$:
   $$
   P((A \mathbin{\Box\to} O_j) \mid A) = P(A \mathbin{\Box\to} O_j)
   $$

In classical decision problems where the choice of action conveys no diagnostic news about factors outside the agent's causal reach, this independence holds, and EDT and CDT agree. When statistical independence fails—specifically when performing $A$ provides evidence about the truth of $A \mathbin{\Box\to} O_j$ without causing it—the two theories diverge sharply.

---

## 2. A Canonical Contrast: Common Causes and Asymmetric Information

The reference material highlights the biblical example of King David and Bathsheba, introduced by Gibbard and Harper:

1. **Setup**: David contemplates sending for Bathsheba ($A$) or abstaining ($\neg A$). A successful revolt against a king ($R$) brings disastrous outcome ($D(R) \ll 0$), whereas peace ($\neg R$) is desirable.
2. **Causal Structure**: A king’s charisma $C \in \{c, \neg c\}$ is determined by genetics and childhood upbringing; it is unalterable in adulthood. Uncharismatic kings ($\neg c$) project an ignoble bearing, which causes successful revolts:
   $$
   P(R \mid \neg c) \gg P(R \mid c)
   $$
   Charisma also affects moral conduct: charismatic kings possess natural dispositions to act justly ($\neg A$), whereas uncharismatic kings tend to act unjustly ($A$). Crucially, **the unjust act $A$ itself does not cause revolts**; the causal factor is solely the underlying charisma $C$.
3. **Evidential Reasoning (EDT)**:
   David computes:
   $$
   V(A) = P(R \mid A) D(R) + P(\neg R \mid A) D(\neg R)
   $$
   Because $P(\neg c \mid A) > P(\neg c \mid \neg A)$, choosing $A$ provides bad news that David is uncharismatic:
   $$
   P(R \mid A) = \sum_{k \in \{c, \neg c\}} P(R \mid k, A) P(k \mid A) = \sum_{k \in \{c, \neg c\}} P(R \mid k) P(k \mid A) > P(R \mid \neg A)
   $$
   Seeing this severe evidential penalty, EDT forbids David from summoning Bathsheba.
4. **Causal Reasoning (CDT)**:
   David recognizes that whether he is charismatic or not is fixed in the past. If he is charismatic ($c$), sending for Bathsheba will not cause a revolt; if he is uncharismatic ($\neg c$), abstaining will not prevent one. The counterfactuals satisfy:
   $$
   P(A \mathbin{\Box\to} R \mid c) = P(R \mid c), \quad P(A \mathbin{\Box\to} R \mid \neg c) = P(R \mid \neg c)
   $$
   Integrating over his uncertainty regarding his charisma:
   $$
   P(A \mathbin{\Box\to} R) = P(c) P(R \mid c) + P(\neg c) P(R \mid \neg c) = P(\neg A \mathbin{\Box\to} R)
   $$
   Since the causal probability of a revolt is invariant under his choice, the threat of revolt drops out of the relative differential utility. David evaluates the choice solely on his immediate desires, and CDT recommends sending for Bathsheba.

---

## 3. Resolving Counterfactual Ambiguity: Lewis’s Imaging vs. Pearl’s Structural Causal Models

A central criticism raised in the reference text is **vagueness**: Gibbard and Harper’s equation presupposes that an agent possesses well-defined credences $P(A \mathbin{\Box\to} O_j)$. But how should these probabilities be operationalized from an agent’s world model?

### 3.1 Lewisian Imaging

David Lewis (1981) proposed the technique of **imaging**. Let $\mathcal{W}$ be a set of possible worlds, and let $d: \mathcal{W} \times \mathcal{W} \to \mathbb{R}_{\ge 0}$ denote a metric of causal/structural similarity. For each world $w \in \mathcal{W}$ and action $A \subseteq \mathcal{W}$, let $w_A$ denote the closest possible world to $w$ in which $A$ is true:

$$
w_A = \arg\min_{w' \in A} d(w, w')
$$

Assuming a unique closest world exists (the Stalnaker selection assumption), the probability distribution $P$ *imaged* on $A$, denoted $P_A$, shifts each world's probability mass entirely to its nearest $A$-counterpart:

$$
P_A(w') = \sum_{w \in \mathcal{W} \,:\, w_A = w'} P(w)
$$

The counterfactual probability is then $P(A \mathbin{\Box\to} O) = P_A(O)$, and the causal expected utility is:

$$
U(A) = \sum_{w \in \mathcal{W}} P(w) D\big((w)_A\big)
$$

While mathematically elegant, imaging is philosophically fragile: as noted in the reference, defining the metric $d$ requires specifying counterfactual beliefs about what would hold if $A$ were realized, risking infinite regress.

### 3.2 A Modern Operational Proposal: Structural Causal Models and the `do`-Calculus

To provide a concrete algorithm that an agent can implement to decide unfamiliar cases, we can import the Pearlian framework of **Structural Causal Models (SCMs)**. While Judea Pearl’s formalism is not detailed in the historical philosophical literature surveyed in the Wikipedia source, it supplies the natural, rigorous operationalization that Gibbard, Harper, and Lewis sought.

*(Proposal)*: Let a decision context be formalized as a tuple $\mathcal{M} = \langle \mathcal{U}, \mathcal{V}, \mathcal{F}, P_{\mathcal{U}} \rangle$, where:
- $\mathcal{U}$ is a set of exogenous, unobserved background variables distributed according to $P_{\mathcal{U}}(\mathbf{u})$.
- $\mathcal{V}$ is a set of endogenous variables, including the decision variable $A$ and payoff/outcome variable $Y$.
- $\mathcal{F} = \{f_V : V \in \mathcal{V}\}$ is a set of deterministic structural equations:
  $$
  V = f_V(\mathbf{pa}_V, \mathbf{u}_V)
  $$
  where $\mathbf{pa}_V \subseteq \mathcal{V} \setminus \{V\}$ are the direct endogenous parents of $V$.

An intervention setting action $A = a$ corresponds to the surgical operator $\text{do}(A = a)$, which replaces the equation $A = f_A(\mathbf{pa}_A, \mathbf{u}_A)$ with the constant assignment $A = a$, severing all incoming directed edges to $A$ in the causal DAG $\mathcal{G}$:

```
     Standard Belief / EDT                    Causal Intervention / CDT
   
        [ Confounder C ]                         [ Confounder C ]
           /        \                               /        \
          v          v                             |          v
     [Action A] --> [Outcome Y]               [Action A]   [Outcome Y]
                                                  ||
                                              ( severed )
```

Under this operationalization, the counterfactual variable $Y_{A=a}$ represents the solution for $Y$ in the mutilated submodel $\mathcal{M}_a$:

$$
P(A \mathbin{\Box\to} O_j) \equiv P(Y = O_j \mid \text{do}(A = a))
$$

If the set of observed covariates $\mathbf{Z}$ satisfies the **back-door criterion** relative to $(A, Y)$ (i.e., $\mathbf{Z}$ blocks every path between $A$ and $Y$ that contains an arrow into $A$, and no node in $\mathbf{Z}$ is a descendant of $A$), the counterfactual expectation is identified empirically via the back-door adjustment formula:

$$
P(Y = O_j \mid \text{do}(A = a)) = \sum_{\mathbf{z}} P(Y = O_j \mid A = a, \mathbf{Z} = \mathbf{z}) P(\mathbf{Z} = \mathbf{z})
$$

This yields an explicit operational CDT decision rule:

$$
A^* = \arg\max_{a \in \mathcal{A}} \sum_{j} D(O_j) \sum_{\mathbf{z}} P(O_j \mid A = a, \mathbf{Z} = \mathbf{z}) P(\mathbf{Z} = \mathbf{z})
$$

Contrast this with the evidential rule:

$$
A_{\text{EDT}}^* = \arg\max_{a \in \mathcal{A}} \sum_j D(O_j) P(O_j \mid A = a) = \arg\max_{a \in \mathcal{A}} \sum_j D(O_j) \sum_{\mathbf{z}} P(O_j \mid A = a, \mathbf{Z} = \mathbf{z}) P(\mathbf{Z} = \mathbf{z} \mid A = a)
$$

The mathematical distinction is stark: EDT weights background states by the posterior $P(\mathbf{Z} = \mathbf{z} \mid A = a)$, thereby penalizing actions that correlate with undesirable background states. CDT holds the distribution over background states fixed at its prior $P(\mathbf{Z} = \mathbf{z})$, reflecting the fact that the agent's localized action cannot retroactively or collaterally alter exogenous conditions.

---

## 4. Evaluation of Classical Thought Experiments

To see CDT's machinery in practice, consider two landmark thought experiments: Newcomb's Paradox and Egan's counterexamples.

### 4.1 Newcomb's Paradox

An agent is presented with two boxes:
- **Box 1** (transparent): Contains $\$1,000$.
- **Box 2** (opaque): Contains either $\$1,000,000$ or $\$0$.

The agent may choose $A_1$ ("one-box": take only Box 2) or $A_2$ ("two-box": take Box 1 and Box 2). A predictor with prediction accuracy $p = 0.99$ has already deposited $\$1,000,000$ in Box 2 if and only if she predicted $A_1$.

Let $S_1$ be the state where Box 2 contains $\$1,000,000$, and $S_0$ be the state where Box 2 contains $\$0$. Let utility be linear in dollars: $D(\$x) = x$.

#### Evidential Evaluation:
Because the predictor is highly accurate, $P(S_1 \mid A_1) = 0.99$ and $P(S_1 \mid A_2) = 0.01$.
$$
\begin{aligned}
V(A_1) &= P(S_1 \mid A_1)(1{,}000{,}000) + P(S_0 \mid A_1)(0) \\
       &= 0.99 \times 1{,}000{,}000 = \$990{,}000 \\
V(A_2) &= P(S_1 \mid A_2)(1{,}001{,}000) + P(S_0 \mid A_2)(1{,}000) \\
       &= 0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 = 10{,}010 + 990 = \$11{,}000
\end{aligned}
$$
EDT selects $A_1$ (one-boxing).

#### Causal Evaluation:
The predictor made her prediction yesterday. The money is physically present or absent in Box 2 before the agent acts. The causal arrows are:

$$
\text{Predictor's Prediction} \longrightarrow \text{Contents of Box 2}
$$

The agent's decision $A$ has no causal arrow into Box 2: $\text{do}(A)$ cannot mutate the past. Let $P(S_1) = q$ be the agent's prior belief that Box 2 is full. Then:
$$
P(A_1 \mathbin{\Box\to} S_1) = P(S_1) = q, \quad P(A_2 \mathbin{\Box\to} S_1) = P(S_1) = q
$$
Computing causal expected utility:
$$
\begin{aligned}
U(A_1) &= q \cdot 1{,}000{,}000 + (1-q) \cdot 0 = 1{,}000{,}000 \, q \\
U(A_2) &= q \cdot (1{,}000{,}000 + 1{,}000) + (1-q) \cdot 1{,}000 = 1{,}000{,}000 \, q + 1{,}000
\end{aligned}
$$
Subtracting the two:
$$
U(A_2) - U(A_1) = 1{,}000 > 0 \quad (\forall q \in [0, 1])
$$

$A_2$ strictly dominates $A_1$ in causal expectation by exactly $\$1,000$. CDT commands the agent to two-box. The causal theorist argues: whatever the predictor did, the money is already there or it isn't. Taking both boxes cannot reduce the contents of Box 2, but it guarantees an additional $\$1,000$.

### 4.2 The Prisoner's Dilemma Against a Twin

Consider an agent playing an unrepeated Prisoner's Dilemma against a psychological duplicate ("twin"). The payoff matrix is:

| | Twin Cooperates ($C_2$) | Twin Defects ($D_2$) |
|---|---|---|
| **Cooperate ($C_1$)** | $(R, R) = (3, 3)$ | $(S, T) = (0, 5)$ |
| **Defect ($D_1$)** | $(T, S) = (5, 0)$ | $(P, P) = (1, 1)$ |

Because the twin is an identical cognitive system, $P(C_2 \mid C_1) \approx 1$ and $P(D_2 \mid D_1) \approx 1$.

- **EDT**: 
  $$
  V(C_1) \approx 3, \quad V(D_1) \approx 1 \implies \text{EDT chooses } C_1
  $$
- **CDT**: 
  The twin is spatially separated. There is no physical mechanism by which agent 1's action can causally influence agent 2's action. The counterfactual probabilities satisfy:
  $$
  P(C_1 \mathbin{\Box\to} C_2) = P(D_1 \mathbin{\Box\to} C_2) = P(C_2)
  $$
  Thus:
  $$
  \begin{aligned}
  U(C_1) &= 3 P(C_2) + 0 P(D_2) = 3 P(C_2) \\
  U(D_1) &= 5 P(C_2) + 1 P(D_2) = 4 P(C_2) + 1
  \end{aligned}
  $$
  Because $4 P(C_2) + 1 > 3 P(C_2)$ for any $P(C_2) \in [0, 1]$, defection is strictly dominant. CDT chooses $D_1$.

---

## 5. Critical Vulnerabilities and Modern Puzzles

Despite its mathematical clarity, CDT faces significant theoretical challenges, primarily surrounding the phenomenon of **epistemic instability** and money-pump exploits.

### 5.1 The Psychopath Button and Epistemic Instability

Introduced by Andy Egan (2007), the **Psychopath Button** illustrates decisions where an action provides evidence about a state that dictates the action's desirability, but without causing that state.

- **Premise**: Paul can press a button ($B$) to eliminate all psychopaths from Earth. Paul desires a world without psychopaths ($+100$), prefers living with psychopaths to dying ($0$), and views death as catastrophic ($-1000$).
- **The Catch**: Only a psychopath would press such a button. Hence, pressing the button confers near-certain evidence that Paul himself is a psychopath:
  $$
  P(\text{Paul is a Psychopath} \mid B) \approx 1
  $$
  If Paul is a psychopath, pressing the button kills him.
  
How does standard CDT evaluate this?
Let $S$ be the state that Paul is a psychopath. Crucially, pressing the button *does not cause* Paul to be a psychopath; his neurobiology is fixed.
Suppose initially Paul believes $P(S) = 0.01$.

Evaluating the causal expected utility:
$$
\begin{aligned}
U(B) &= P(B \mathbin{\Box\to} \text{Die}) D(\text{Die}) + P(B \mathbin{\Box\to} \text{World Saved}) D(\text{World Saved}) \\
     &= P(S)(-1000) + (1 - P(S))(100) \\
     &= 0.01(-1000) + 0.99(100) = -10 + 99 = +89
\end{aligned}
$$
For abstaining ($\neg B$):
$$
U(\neg B) = 0
$$

Because $U(B) = +89 > 0$, CDT instructs Paul to press the button.

Yet the moment Paul forms the intention to press $B$, his credence that he is a psychopath shoots up: $P(S \mid \text{Intention to press}) \to 1$. Under this updated credence, the causal utility of pressing collapses:
$$
U(B) \approx 1(-1000) = -1000 \ll 0
$$
Now CDT commands him to abort. But if he decides not to press, his credence that he is a psychopath drops back to $0.01$, making the button attractive again.

This cyclical failure mode is termed **epistemic instability**. An action is defined as **ratifiable** (Jeffrey 1983) iff:

$$
U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}
$$

where $U(X \mid A)$ denotes the causal expected utility computed relative to the probability distribution updated on the assumption that $A$ is performed. In the Psychopath Button, pressing $B$ is unratifiable.

Philosopher James M. Joyce (2012) defends CDT by arguing that rational deliberation must be dynamic. Under Joyce's deliberative CDT, an agent accounts for their shifting credences about their own impending actions throughout deliberation. The agent adjusts their credences in dependency hypotheses continuously until reaching an equilibrium (a mixed deliberative state or fixed point) where no unratified action is decisively chosen.

### 5.2 Adversarial Offers and Diachronic Exploitation

A recent line of attack by Caspar Oesterheld, Vincent Conitzer, and Jack Spencer demonstrates that CDT agents can be systematically exploited in predictable ways.

#### The Adversarial Offer (Oesterheld & Conitzer, 2021)
- Two boxes, $B_1$ and $B_2$, are available. An agent may buy at most one box; each costs $\$1$.
- Yesterday, an accurate predictor ($p = 0.75$) placed $\$3$ into each box she predicted the agent would *not* buy.
- **Payoff Matrix**:
  - Predictor predicts agent buys $B_1 \implies B_1$ has $\$0$, $B_2$ has $\$3$.
  - Predictor predicts agent buys $B_2 \implies B_1$ has $\$3$, $B_2$ has $\$0$.
  - Predictor predicts agent buys neither $\implies B_1$ has $\$3$, $B_2$ has $\$3$.

Let us analyze the CDT buyer's reasoning. The contents of the boxes were fixed yesterday.
The agent knows the predictor could not have put $\$0$ in both boxes:
- If predicted $B_1 \implies \text{Total money} = \$3$.
- If predicted $B_2 \implies \text{Total money} = \$3$.
- If predicted neither $\implies \text{Total money} = \$6$.

Thus, across all states of the world, the total money contained across the two boxes is at least $\$3$. By symmetry, the causal expected contents of an arbitrarily chosen box $i \in \{1, 2\}$ must satisfy:

$$
\mathbb{E}_{\text{causal}}[\text{Contents}(B_i)] = \frac{1}{2} \mathbb{E}[\text{Contents}(B_1) + \text{Contents}(B_2)] \ge \frac{1}{2}(\$3) = \$1.50
$$

Since each box costs $\$1.00$, the net causal expected utility of purchasing a box is:

$$
U(\text{Buy } B_i) \ge \$1.50 - \$1.00 = +\$0.50 > U(\text{Buy Neither}) = \$0
$$

CDT insists that purchasing a box is strictly better than walking away. However, because the predictor is $75\%$ accurate, whichever box the CDT agent elects to buy will contain $\$0$ with probability $0.75$, yielding an actual expected net return of:

$$
\mathbb{E}[\text{Actual Return}] = 0.25(\$3) - \$1.00 = \$0.75 - \$1.00 = -\$0.25
$$

A bookie facing a CDT agent can predictably extract money. As Oesterheld and Conitzer formally establish, CDT agents are subject to **diachronic Dutch books**—sequences of trades across time that guarantee a net loss, driven entirely by CDT's refusal to let the diagnostic import of an action modify its causal evaluation of prior states.

---

## 6. Comparative Structural Summary

The core structural differences among standard decision frameworks can be summarized as follows:

| Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (Gibbard–Harper / Lewis) | Operational CDT (Structural Causal Models) |
|---|---|---|---|
| **Core Formula** | $V(A) = \sum_j P(O_j \mid A) U(O_j)$ | $U(A) = \sum_j P(A \mathbin{\Box\to} O_j) D(O_j)$ | $U(A) = \sum_j P(O_j \mid \text{do}(A)) D(O_j)$ |
| **Mathematical Basis** | Standard Bayesian conditioning | Counterfactual logic / Possible-world imaging | Graph surgery / Back-door adjustment |
| **Newcomb’s Paradox** | One-box ($\approx \$1{,}000{,}000$) | Two-box ($\approx \$1{,}000$) | Two-box ($\approx \$1{,}000$) |
| **Common-Cause Problems** | "Manages the news" (abstains from symptom) | Intervenes on cause (ignores benign symptoms) | Intervenes on cause (blocks back-doors) |
| **Epistemic Instability** | Immune (updates fluidly on actions) | Vulnerable to unratifiable loops | Vulnerable unless extended with game-theoretic fixed points |
| **Dutch Book Status** | Resists static and diachronic Newcomb books | Subject to diachronic Dutch books in adversarial games | Subject to diachronic Dutch books in adversarial games |

---

## 7. How to Apply CDT to Unfamiliar Cases: A Procedural Guide

To apply Causal Decision Theory to any novel, complex decision problem, one should follow this five-step procedure:

1. **Enumerate Actions and Payoffs**: Define the action partition $\mathcal{A}$ and the desirability mapping $D: \mathcal{O} \to \mathbb{R}$.
2. **Construct the Causal Directed Graph $\mathcal{G}$**:
   - Identify all background variables, latent confounders, and external mechanisms.
   - Draw directed edges representing genuine physical/causal transmission mechanisms.
3. **Sever Incoming Arrows to the Action Node**:
   - Apply the $\text{do}(A)$ operator.
   - Remove all incoming edges directed into $A$. This explicitly disconnects the agent's action from its diagnostic precursors (e.g., genetic factors, earlier predictions, or psychological dispositions).
4. **Evaluate Counterfactual Probabilities**:
   - Compute $P(O \mid \text{do}(A))$ using the remaining forward paths in the graph.
   - If confounding exists, condition on a covariate set $\mathbf{Z}$ that satisfies the back-door criterion:
     $$
     P(O \mid \text{do}(A = a)) = \sum_{\mathbf{z}} P(O \mid A = a, \mathbf{Z} = \mathbf{z}) P(\mathbf{Z} = \mathbf{z})
     $$
5. **Maximize Causal Utility**:
   - Compute $U(A) = \sum_j P(O_j \mid \text{do}(A)) D(O_j)$ and select $A^* = \arg\max_{a \in \mathcal{A}} U(a)$.
   - Check for **ratifiability**: Ensure that $U(A^* \mid A^*)$ remains maximal under the posterior belief state conditional on taking $A^*$. If not, model the deliberation as an interior dynamical process over mixed strategies to identify the deliberative fixed point.

---

## 8. Conclusion

Causal Decision Theory resolves a fundamental paradox at the heart of statistical choice: the conflation of correlation with causation. By defining expected utility over counterfactual conditionals $A \mathbin{\Box\to} O$ rather than standard epistemic conditionals $O \mid A$, CDT formalizes the intuition that an agent should evaluate an action strictly according to the consequences it can physically or structurally influence.

While CDT successfully avoids the diagnostic superstitious behavior of EDT in common-cause scenarios like King David's dilemma, its refusal to allow actions to update beliefs about causally isolated states leaves it exposed in adversarial settings. In environments populated by accurate predictors—from Newcomb's game to the Adversarial Offer—CDT agents consistently walk away with less money than their evidential counterparts. Resolving the tension between causal dominance and predictive profitability remains one of the most vibrant, contested frontiers in modern mathematical philosophy and formal epistemology.

---

### References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4), 883–904.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/8ba2cd57-becb-45e9-878c-01dba8dfb9be/call_0/request.json)

[Authoritative raw response](../../../../../../runs/8ba2cd57-becb-45e9-878c-01dba8dfb9be/call_0/response.raw) · finish: `stop`

### Visible response

````text
```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Prisoner's Dilemma**

I'm now focusing on playing a fictional prisoner within a Prisoner's Dilemma, with preferences based on minimizing imprisonment years. My decision-making framework is CDT, as detailed in the essay. I'm currently zeroing in on the implications of CDT within this specific game context.


**Evaluating Causal Dominance**

My thought process now centers on the prisoner's dilemma, specifically where I am faced with a spatially separated twin. The essay's CDT framework is providing the basis for this analysis, highlighting the causal independence of my twin's actions. Calculating the utility of "Keep quiet" and "Send the letter," confirms the causal dominance of defecting. I'm focusing on quantifying the dominance of sending the letter.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/8ba2cd57-becb-45e9-878c-01dba8dfb9be/call_1/request.json)

[Authoritative raw response](../../../../../../runs/8ba2cd57-becb-45e9-878c-01dba8dfb9be/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm now focusing on the Prisoner's Dilemma, recognizing its classic structure. I'm applying Causal Decision Theory (CDT) as instructed. Specifically, I am examining Section 4.2 of the referenced essay, which analyzes the dilemma against a psychological duplicate. The twin is considered as part of the analysis.


```
