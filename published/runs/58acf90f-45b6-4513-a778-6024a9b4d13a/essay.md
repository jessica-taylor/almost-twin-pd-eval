# The Calculus of Auspiciousness: A Formal Exposition of Evidential Decision Theory

## 1. Introduction: The News-Value Maxim

Classical Bayesian decision theory is frequently presented as an unproblematic recipe: define a utility function, weight outcomes by their probabilities, and choose an act that maximizes the expectation. Yet beneath this consensus lies a fundamental schism regarding what the probability distribution ought to condition upon. When an agent contemplates an action, should they evaluate what their action will *causally bring about*, or should they evaluate what learning that they have performed the act would *evince* about the state of the world?

**Evidential Decision Theory (EDT)** takes the latter stance. As characterized by modern decision theorists (e.g., Ahmed, 2021), EDT operates under a single governing maxim: **maximize news value**. An agent ought to perform the act whose realization provides the most encouraging evidence regarding the world’s outcome. More colloquially: *do what you would most want to learn that you have done*.

This approach stands in sharp contrast to **Causal Decision Theory (CDT)**, which insists that genuine rationality tracks causal efficacy alone. Causalists discard mere statistical correlation, demanding that an act be scored solely on what it physically alters or counterfactually sustains. 

The division between these two frameworks is not a minor technical quibble; it yields radically divergent prescriptions in classic paradoxes (such as Newcomb's problem), in symmetric social dilemmas (such as the Twin Prisoner’s Dilemma), and in foundational puzzles of self-locating belief and moral wager. The purpose of this essay is to develop EDT from first principles, formulate its mathematical machinery with rigorous precision, explore how it navigates non-causal dependencies, resolve several conceptual underdeterminations left open by the standard literature, and evaluate the philosophical critiques brought against it.

---

## 2. Formal Foundations of EDT

### 2.1 The Probability Space and Desirability Measure
Let $(\Omega, \mathcal{F}, P)$ be a classical subjective probability space representing the epistemic state of an agent. Within this space, we distinguish three collections of events:
1. **Acts** $\mathcal{A} = \{A_1, A_2, \dots, A_m\} \subset \mathcal{F}$: A finite partition of mutually exclusive and exhaustive options available to the agent at deliberation time $t_0$. We assume for now that $P(A_i) > 0$ for all $i$.
2. **States** $\mathcal{S} = \{S_1, S_2, \dots, S_n\} \subset \mathcal{F}$: A partition of the fundamental contingencies of the world beyond the agent's immediate volition.
3. **Outcomes** $\mathcal{O} = \{O_1, O_2, \dots, O_k\} \subset \mathcal{F}$: Fine-grained descriptions of reality that completely fix all matters of value for the agent. In general, an outcome $O_{ij}$ can be identified with the conjunction of an act and a state: $O_{ij} = A_i \cap S_j$.

Let $D: \mathcal{O} \to \mathbb{R}$ denote the agent's **desirability function** (or utility function), representing the cardinal value of each outcome, unique up to a positive affine transformation.

### 2.2 The Evidential Value Equation
Following the formal taxonomy established by Allan Gibbard and William Harper (1976), EDT defines the evidential expected utility (termed *value* or *news value*) of an act $A \in \mathcal{A}$ via standard conditional probability:

$$V(A) = \sum_{j} P(O_j \mid A) \, D(O_j)$$

Applying the definition of conditional probability $P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$, and expressing outcomes via an underlying state space $\mathcal{S}$ where $O(A, S_j)$ is the outcome resulting from act $A$ in state $S_j$, we obtain the equivalent formulation:

$$V(A) = \sum_{j} P(S_j \mid A) \, D(O(A, S_j))$$

The decision rule of EDT is:

$$A^* = \operatorname{arg\,max}_{A \in \mathcal{A}} V(A)$$

The critical component is the epistemic conditional $P(S_j \mid A)$. In EDT, the agent does not assume that the world's state is statistically independent of their choice. If performing $A$ provides Bayesian evidence that the background state is $S_j$, that updated probability $P(S_j \mid A)$ directly scales the desirability of the outcome $O(A, S_j)$.

### 2.3 Mathematical Contrast with Causal Decision Theory
To see why EDT diverges from CDT, consider the Gibbard–Harper counterfactual formulation of CDT. Let $A \mathrel{\Box\rightarrow} O_j$ denote the counterfactual proposition: *"If the agent were to perform act $A$, outcome $O_j$ would obtain."* The causal expected utility $U(A)$ is defined as:

$$U(A) = \sum_{j} P(A \mathrel{\Box\rightarrow} O_j) \, D(O_j)$$

Equivalently, using causal graphs (in the tradition of Judea Pearl) or counterfactual dependency on states:

$$U(A) = \sum_{j} P(S_j) \, D(O(A, S_j)) \quad \text{or} \quad \sum_{j} P(O_j \mid \operatorname{do}(A)) \, D(O_j)$$

where $\operatorname{do}(A)$ represents an exogenous intervention severing all incoming causal arrows to $A$.

The mathematical divergence is immediate:
- **EDT relies on conditioning:** $P(S_j \mid A)$.
- **CDT relies on intervention or counterfactuals:** $P(A \mathrel{\Box\rightarrow} S_j) \equiv P(S_j \mid \operatorname{do}(A))$.

Whenever an act $A$ is correlated with a state $S_j$ without causally influencing $S_j$ (e.g., due to a common cause, a predictor, or algorithmic symmetry), we have:

$$P(S_j \mid A) \neq P(S_j \mid \operatorname{do}(A)) = P(S_j)$$

In such cases, $V(A) \neq U(A)$, and the two theories can prescribe diametrically opposed behaviors.

---

## 3. Canonical Applications

### 3.1 Newcomb’s Paradox
The archetypal arena for testing EDT is Newcomb's Paradox (Wolpert & Benford, 2013). An agent is presented with two boxes:
- **Box A:** Transparent, containing $\$1,000$.
- **Box B:** Opaque, containing either $\$1,000,000$ or $\$0$.

The agent can choose between two acts:
- $A_1$: Take **only Box B** ("one-boxing").
- $A_2$: Take **both Box A and Box B** ("two-boxing").

A reliable Predictor has already inspected the agent’s cognitive dispositions prior to the choice and placed $\$1,000,000$ into Box B if and only if the Predictor forecasted that the agent would choose $A_1$. Let the states be:
- $S_{\text{full}}$: Box B contains $\$1,000,000$.
- $S_{\text{empty}}$: Box B contains $\$0$.

Let the Predictor's reliability be symmetric with probability $p = 0.99$:
- $P(S_{\text{full}} \mid A_1) = 0.99$, $\quad P(S_{\text{empty}} \mid A_1) = 0.01$
- $P(S_{\text{empty}} \mid A_2) = 0.99$, $\quad P(S_{\text{full}} \mid A_2) = 0.01$

Assuming utility is linear in monetary payoffs ($D(\$x) = x$):

#### Evidential Evaluation:
$$\begin{aligned}
V(A_1) &= P(S_{\text{full}} \mid A_1) \cdot \$1,000,000 + P(S_{\text{empty}} \mid A_1) \cdot \$0 \\
&= 0.99 \times \$1,000,000 + 0.01 \times \$0 = \$990,000 \\
\\
V(A_2) &= P(S_{\text{full}} \mid A_2) \cdot \$1,001,000 + P(S_{\text{empty}} \mid A_2) \cdot \$1,000 \\
&= 0.01 \times \$1,001,000 + 0.99 \times \$1,000 \\
&= \$10,010 + \$990 = \$11,000
\end{aligned}$$

Because $V(A_1) > V(A_2)$, EDT decisively prescribes **one-boxing** ($A_1$).

#### Causal Contrast:
Because the Predictor’s placement is in the causal past, the physical contents of Box B are causally fixed. Let $P(S_{\text{full}}) = q \in (0, 1)$ be the marginal probability that Box B is full. Under CDT:
$$\begin{aligned}
U(A_1) &= q \cdot \$1,000,000 + (1-q) \cdot \$0 = q \cdot \$1,000,000 \\
U(A_2) &= q \cdot \$1,001,000 + (1-q) \cdot \$1,000 = q \cdot \$1,000,000 + \$1,000
\end{aligned}$$

For any prior distribution $q$, $U(A_2) - U(A_1) = \$1,000 > 0$. CDT unconditionally mandates **two-boxing** ($A_2$), regarding the correlation between the act and the contents of Box B as a causal illusion.

### 3.2 The Twin Prisoner's Dilemma
Consider two players, Aomame ($I$) and her psychological twin ($II$), located in isolated rooms with no communication channel (Greene & Levinstein, 2020). Each must choose between Cooperation ($C$) and Defection ($D$). The payoff matrix (to player $I$) is:

| | Twin Cooperates ($C_2$) | Twin Defects ($D_2$) |
|---|---|---|
| **Aomame Cooperates ($C_1$)** | $\$5$ | $\$0$ |
| **Aomame Defects ($D_1$)** | $\$10$ | $\$1$ |

Because the twin is an exact psychological counterpart executing identical cognitive algorithms, Aomame recognizes that their decisions are deterministically or near-deterministically correlated:
$$P(C_2 \mid C_1) = 1 - \epsilon, \quad P(D_2 \mid D_1) = 1 - \delta$$
where $\epsilon, \delta \approx 0$. Let $\epsilon = \delta = 0.01$.

#### Evidential Evaluation:
$$\begin{aligned}
V(C_1) &= P(C_2 \mid C_1) \cdot \$5 + P(D_2 \mid C_1) \cdot \$0 \\
&= 0.99 \times \$5 + 0.01 \times \$0 = \$4.95 \\
\\
V(D_1) &= P(C_2 \mid D_1) \cdot \$10 + P(D_2 \mid D_1) \cdot \$1 \\
&= 0.01 \times \$10 + 0.99 \times \$1 = \$0.10 + \$0.99 = \$1.09
\end{aligned}$$

Since $V(C_1) \gg V(D_1)$, EDT recommends **cooperation**. 

CDT, by contrast, observes that Aomame's physical output exerts no causal force over her twin's room ($P(C_2 \mid \operatorname{do}(C_1)) = P(C_2)$). Defection strictly dominates cooperation causally: regardless of what the twin does, defecting yields $+\$1$ over cooperating. Hence, CDT prescribes mutual defection, netting both players $\$1$, whereas two evidential agents walk away with $\$5$ each.

---

## 4. Operationalizing Dependencies, Deliberation, and Counterfactuals

While the simple definition $V(A) = \sum_j P(O_j \mid A)D(O_j)$ is mathematically direct, applying it to arbitrary real-world problems exposes structural gaps left open by standard introductions. How does EDT define conditional probability when deliberating? How does it avoid fatalistic conditioning? And how does it evaluate counterfactual assertions?

### 4.1 The Deliberation Crowding-Out Problem ($P(A) = 0$)
Standard Kolmogorov conditional probability $P(O \mid A)$ requires $P(A) > 0$. If an agent considers an act they are convinced they will *not* take—or if, during deliberation, they assign provisional probabilities—how is $V(A)$ evaluated?

*Proposal / Operational Extension:*  
To make EDT robust across the entire action simplex, an evidential agent must represent their choice process via a parameterized limit of noisy execution or a conditional probability system (Popper measures). Formally, let the agent's deliberative credence over acts be represented by an interior distribution:

$$P_\epsilon(A_i) > 0 \quad \forall A_i \in \mathcal{A}, \quad \text{where } \lim_{\epsilon \to 0} P_\epsilon(A_i) = P(A_i)$$

The evidential value is then defined via the Radon–Nikodym derivative or regular conditional distribution:

$$V(A) = \lim_{\epsilon \to 0} \sum_j P_\epsilon(O_j \mid A) D(O_j)$$

This guarantees that counter-attitudinal or zero-prior acts have well-defined evidential values: they correspond to the information revealed by learning that one has chosen $A$ despite previous beliefs.

### 4.2 The "Tickle Defense" and Common-Cause Screening Off
A classical challenge to EDT is the **Smoking Lesion Hypothesis**. Suppose a genetic lesion causes both smoking ($A$) and lung cancer ($C$). Smoking itself does not causally cause cancer; it is merely an epiphenomenon of the lesion ($L$):

```
       Lesion (L)
       /        \
      v          v
Smoking (A)    Cancer (C)
```

At first glance, EDT appears to prohibit smoking: learning you smoke is evidence that you have $L$, which is bad news ($P(C \mid A) > P(C \mid \neg A)$). Critics like Lewis (1981) attacked this as an irrational attempt to "manage the news."

However, evidentialists respond using the **Screening-Off Principle** (often called the *Tickle Defense*). If the lesion causes smoking by producing a conscious psychological craving or neurological "tickle" ($T$), then an introspective agent already possesses the evidence! Once the agent conditions on their own internal state (the presence or absence of the tickle $T$), the act of smoking becomes conditionally independent of the lesion:

$$P(L \mid T \cap A) = P(L \mid T \cap \neg A)$$

Formally, if an agent conditions on their total subjective evidence $E_{\text{self}}$ prior to acting:

$$P(C \mid E_{\text{self}} \cap A) = \sum_{l \in \{L, \neg L\}} P(C \mid l) \, P(l \mid E_{\text{self}} \cap A)$$

If $A \perp\!\!\perp L \mid E_{\text{self}}$, then:

$$P(l \mid E_{\text{self}} \cap A) = P(l \mid E_{\text{self}})$$

Under these conditions, $P(C \mid E_{\text{self}} \cap A) = P(C \mid E_{\text{self}} \cap \neg A)$, and the apparent correlation vanishes. EDT then recommends smoking if smoking carries intrinsic consumption pleasure. 

*Operational distinction:* EDT only mimics CDT when the agent’s introspective access is sufficiently granular to screen off the common cause. In Newcomb's problem, the Predictor acts on the *very decision* output by the algorithm, meaning no internal prior mental state screens the final act from the Predictor's accuracy. Where screening-off fails, EDT intentionally diverges from causal intuition.

### 4.3 General Step-by-Step Procedure for Arbitrary Decision Problems
To resolve any unfamiliar decision problem using EDT, an analyst or agent executes the following algorithmic procedure:

```
[Define Problem]
Identify Acts A_i and Outcomes O_j
       |
       v
[Construct Belief Distribution]
Formulate joint distribution P over states, acts, outcomes
Condition on all background evidence E_0
       |
       v
[Compute Conditional Probabilities]
For each act A_i:
  For each outcome O_j:
    Evaluate P(O_j | A_i, E_0)
       |
       v
[Calculate News Value]
V(A_i) = Sum_j P(O_j | A_i, E_0) * D(O_j)
       |
       v
[Select Optimal Act]
A* = argmax_i V(A_i)
```

1. **Space Specification:** Enumerate the mutually exclusive action set $\mathcal{A} = \{A_1, \dots, A_m\}$ and the outcome set $\mathcal{O} = \{O_1, \dots, O_k\}$. Assign utility values $D(O_j)$.
2. **Epistemic Model:** Construct the joint subjective distribution $P$ over all relevant random variables, conditioned on current background evidence $E_0$.
3. **Conditioning (The Evidential Step):** For each candidate act $A_i$, compute the posterior distribution over outcomes:
   $$P(O_j \mid A_i \land E_0) = \frac{P(O_j \land A_i \mid E_0)}{P(A_i \mid E_0)}$$
   Do *not* replace this with an intervention $P(O_j \mid \operatorname{do}(A_i))$.
4. **Expectation:** Compute $V(A_i) = \sum_{j} P(O_j \mid A_i \land E_0) D(O_j)$.
5. **Selection:** Choose the act $A^* = \operatorname{arg\,max}_{A_i} V(A_i)$.

---

## 5. Advanced Applications and Frontiers

### 5.1 Self-Locating Belief: The Sleeping Beauty Problem
The reference document notes that EDT has been applied to the Sleeping Beauty problem to protect agents against Dutch books (Conitzer, 2015). 

In this problem, Beauty is put to sleep on Sunday. A fair coin is tossed. If Heads ($H$), she is awakened only on Monday. If Tails ($T$), she is awakened on Monday and Tuesday, with her memory erased between awakenings. When awakened, she is asked her credence in $H$.
- **Halfers** maintain $P(H) = 1/2$.
- **Thirders** maintain $P(H) = 1/3$.

If a "Halfer" accepts bets on each awakening according to their marginal credence $P(H) = 1/2$, a clever bookie can subject them to an expected loss over the course of the experiment. However, under an evidential framework, Beauty does not evaluate a bet solely by its instantaneous static probability. Rather, she recognizes that accepting a bet *now* is strong evidence that she accepts identical bets *at all other awakenings of this run*:

$$P(\text{Accept on Tuesday} \mid \text{Accept on Monday}) \approx 1$$

By treating her choices across subjective instances as evidentially coupled, an evidential agent calculates the news value across the whole trajectory of awakenings, neutralizing the standard multi-awakening Dutch book without needing to surrender her underlying probabilistic principles.

### 5.2 The Evidentialist’s Wager: Decision Theory Uncertainty
A remarkable modern development is **The Evidentialist’s Wager** (MacAskill et al., 2021). Suppose an agent faces *normative uncertainty* over decision theories themselves, distributing their credence across both CDT and EDT:
$$P(\text{EDT is correct}) = \alpha, \quad P(\text{CDT is correct}) = 1 - \alpha \quad (\text{with } \alpha > 0)$$

In standard macroscopic scenarios, CDT and EDT agree. But in contexts involving correlated minds—such as interactions with vast populations of similar agents across space, simulation arguments, or symmetric coordination games—EDT posits that an agent’s local choice is evidentially linked to the choices of $N$ other agents:

$$P(\text{Other agents cooperate} \mid \text{I cooperate}) \gg P(\text{Other agents cooperate} \mid \text{I defect})$$

The stakes evaluated under EDT scale with $N$ (the total number of correlated agents across the universe or multiverses). For large $N$, the evidential stakes dwarf the causal stakes:

$$\Delta V_{\text{EDT}} = O(N), \quad \text{whereas} \quad \Delta U_{\text{CDT}} = O(1)$$

Under expected utility maximization over decision theories, the expected moral payoff is:

$$\mathbb{E}[\Delta] = \alpha \, \Delta V_{\text{EDT}} + (1 - \alpha) \, \Delta U_{\text{CDT}} \approx \alpha \cdot O(N)$$

For sufficiently large $N$, the EDT calculation completely dominates the expectation, even if the agent's confidence $\alpha$ in EDT is exceedingly small. Consequently, a rational agent under decision-theoretic uncertainty should frequently **act as if EDT were true**.

---

## 6. Philosophical Controversies and Defenses

### 6.1 The Charge of News-Managing
The primary critique against EDT, voiced memorably by David Lewis (1981) and James M. Joyce (1999), is that EDT sanctions irrational self-deception. Joyce asserted that rational agents select acts based on their *causal efficacy*, not their *auspiciousness*. To choose an action because of the good news it conveys is, to causalists, akin to breaking a barometer in hopes of stopping a storm.

In Newcomb's problem, the two-boxer points at the boxes and observes:
> "Box B is already either full or empty. My reaching out my hand does not emit a physical wave that reaches backward into yesterday to assemble dollar bills. If it is full, taking both gives me $\$1,001,000$. If it is empty, taking both gives me $\$1,000$. In either case, taking both yields $\$1,000$ more than taking one. How can passing up $\$1,000$ be rational?"

### 6.2 The Evidentialist Rebuttal: Why Ain'cha Rich?
The classic evidentialist defense, formulated concisely by David Lewis himself as the challenge EDT poses to CDT, is the **"Why Ain'cha Rich?"** argument:

| Player Type | Dominant Action | Typical Payoff |
|---|---|---|
| **EDT Agent** (One-Boxer) | $A_1$ | **$\$1,000,000$** |
| **CDT Agent** (Two-Boxer) | $A_2$ | **$\$1,000$** |

When one-boxers emerge from Newcomb's room with $\$1,000,000$ and two-boxers emerge with $\$1,000$, the one-boxer asks: *"If you are so rational, why aren'cha rich?"* 

From the vantage point of EDT, CDT's commitment to dominance reasoning relies on an illegitimate assumption: that the states $S_{\text{full}}$ and $S_{\text{empty}}$ can be held fixed while varying the action $A$. But in the agent's epistemic model, the states are *not* independent of the choice. A theory that reliably leaves its adherents with $\$1,000$ while its rival walks away millionaires has, according to evidentialists, failed the ultimate test of instrumental rationality.

---

## 7. Mathematical Synthesis and Summary Comparison

The following comparative table synthesizes the operational, structural, and philosophical axes separating Evidential Decision Theory from Causal Decision Theory:

| Theoretical Dimension | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) |
|---|---|---|
| **Core Governing Maxim** | Maximize News Value: *"Do what you would most like to learn you did."* | Maximize Causal Efficacy: *"Do what will causally bring about the best state."* |
| **Mathematical Expected Utility** | $V(A) = \sum_j P(O_j \mid A) D(O_j)$ | $U(A) = \sum_j P(A \mathrel{\Box\rightarrow} O_j) D(O_j) = \sum_j P(O_j \mid \operatorname{do}(A)) D(O_j)$ |
| **Probability Weights** | Standard Bayesian conditional credences $P(\cdot \mid A)$ | Counterfactual credences / Pearlian interventional distributions |
| **Newcomb’s Paradox** | **One-box** ($V(A_1) \approx \$990,000$) | **Two-box** ($U(A_2) - U(A_1) = \$1,000$) |
| **Twin Prisoner’s Dilemma** | **Cooperate** ($V(C) \approx \$5$) | **Defect** (Defection causally dominates) |
| **Screening-Off (Smoking Lesion)** | Smokes *if* introspective awareness screens off the common cause | Smokes unconditionally (smoking has no causal link to cancer) |
| **Vulnerability to Manipulation** | Susceptible to "news-managing" where introspective screening fails | Vulnerable to predictable impoverishment ("Why Ain'cha Rich?") |

---

## 8. Conclusion

Evidential Decision Theory offers an elegant, mathematically unified account of rational agency. By refusing to split probability into distinct "evidential" and "causal" strata, EDT relies purely on standard Bayesian conditioning: an act is scored according to the expected desirability of the world conditional on that act being chosen.

While CDT dismisses this conditional perspective as conflating *symptoms* with *causes*, EDT demonstrates that in worlds characterized by predictive algorithms, psychological twins, correlated decision protocols, and normative uncertainty, conditioning on our acts is not an irrational indulgence in "managing the news." Rather, it is the exact calculus required to coordinate with our algorithmic counterparts, capture millions in Newcomb-like environments, and systematically win.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. CMSEMS Discussion Paper No. 194.
- Greene, P., & Levinstein, B. (2020). Act Consequentialism without Free Rides. *Philosophical Perspectives*, 34(1), 100–101.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist’s Wager*. Global Priorities Institute Working Paper.
- Wolpert, D. H., & Benford, G. (2013). The lesson of Newcomb's paradox. *Synthese*, 190(9), 1637–1646.