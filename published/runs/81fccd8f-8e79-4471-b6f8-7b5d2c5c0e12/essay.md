# The Mechanics and Philosophy of Causal Decision Theory

In standard Bayesian decision theory, a rational agent selects an action that maximizes expected utility. Yet beneath this consensus lies a foundational schism regarding what "expectation" tracks. Does an act's desirability lie in the **news** it provides about the world, or in the **causal consequences** it brings about?

**Causal Decision Theory (CDT)** formalizes the principle that rational choice should be guided exclusively by an agent's causal efficacy. It arose largely as a response to the perceived failures of **Evidential Decision Theory (EDT)** in scenarios featuring common causes or predictive adversaries. EDT evaluates actions via ordinary conditional probabilities—asking, in effect, *"Given that I take action $A$, how good do I expect the world to be?"* CDT, by contrast, asks: *"What outcomes will my choosing $A$ actively bring about?"*

This essay develops the formal architecture of CDT, traces how it separates causal influence from mere epistemic correlation, examines its operationalization across competing mathematical frameworks, and analyzes both canonical and contemporary challenges to its normative validity.

---

## 1. The Core Divergence: Causation vs. Correlation

To appreciate CDT, one must first isolate the flaw it was designed to cure. Consider Jeffrey’s formulation of Evidential Decision Theory. Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be a mutually exclusive and exhaustive set of available acts, $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ a set of mutually exclusive outcomes, and $u(O_j) \in \mathbb{R}$ the utility of outcome $O_j$. An evidentialist computes the value of an act $A$ via conditional probability:

$$V_{\mathrm{EDT}}(A) = \sum_{j} P(O_j \mid A) \, u(O_j)$$

While $V_{\mathrm{EDT}}$ behaves intuitively in benign statistical environments, it conflates **symptomatic** evidence with **causal** influence. 

Gibbard and Harper (1981) dramatized this distinction with the story of **King David and Bathsheba**. Historical records inform King David of two psychological types among monarchs: *charismatic* and *uncharismatic*. A king's charisma is an immutable constitutional trait established in early childhood. Charismatic kings govern justly and face negligible risk of revolt; uncharismatic kings govern unjustly, project a sneaky, ignoble bearing, and are routinely deposed by violent rebellion. Crucially, the rebellion is caused by the ruler’s repulsive bearing, not by the unjust acts themselves. 

David does not know his type. He desires Bathsheba, but summoning her is unjust. 
* Under **EDT**, David notes that summoning Bathsheba ($A$) is strong evidence that he is uncharismatic ($C$), which carries a high conditional probability of revolt ($R$). Because $P(R \mid A) \gg P(R \mid \neg A)$, EDT instructs David to abstain. He treats his own act as a diagnostic test of his personality.
* Under **CDT**, David recognizes that whether he is charismatic or uncharismatic is already fixed. Abstaining from Bathsheba cannot rewrite his childhood or change his bearing. Summoning her brings about the erotic fulfillment he desires without exerting any causal influence on whether his subjects revolt. CDT therefore recommends sending for Bathsheba.

Philosophers predominantly view EDT’s abstention as irrational "fetishism" or superstitious self-management: managing the barometer to change the weather. CDT provides the formal apparatus to forbid choosing an act merely because it serves as a welcome sign of an unalterable reality.

---

## 2. Formal Formulations of CDT

How should an expected utility calculation track causal efficacy rather than simple epistemic correlation? Two primary mathematical formalisms define the literature: counterfactual conditionals and causal dependency hypotheses.

### 2.1. The Gibbard–Harper Counterfactual Formulation

Allan Gibbard and William Harper (1981) formulated CDT using counterfactual conditionals. Let $A \to O_j$ represent the proposition: *"If $A$ were enacted, $O_j$ would obtain."* The causal expected utility $U(A)$ is defined as:

$$U(A) = \sum_{j} P(A \to O_j) \, u(O_j)$$

where $P(A \to O_j)$ is the agent's subjective probability assigned to the counterfactual truth condition.

The rift between EDT and CDT reduces formally to the non-equivalence between the probability of a counterfactual conditional and an ordinary conditional probability:

$$P(A \to O_j) \neq P(O_j \mid A)$$

David Lewis established in his celebrated triviality result (Lewis 1976) that the conditional probability $P(Y \mid X)$ cannot, in general, be interpreted as the probability of a conditional proposition $X \to Y$ without rendering the probability calculus degenerate. 

Gibbard and Harper proved that if an agent satisfies certain baseline axioms—most notably the **Principle of the Conditional Excluded Middle (CEM)**, $(A \to C) \lor (A \to \neg C)$, and conditional consistency—then $P(A \to O_j) = P(O_j \mid A)$ if and only if the act $A$ is statistically independent of the counterfactual conditional itself:

$$P(A \to O_j \mid A) = P(A \to O_j)$$

In benign contexts (such as tossing a fair coin or opening an ordinary door), whether the coin lands heads if tossed is statistically independent of your decision to toss it. But in Newcomb-like dilemmas or King David scenarios, an act provides evidence about which counterfactual realm one inhabits.

### 2.2. Lewis’s Dependency Hypotheses and Imaging

David Lewis (1981) generalized this insight without relying strictly on the controversial semantics of CEM. Let $\mathcal{K} = \{K_1, K_2, \dots, K_k\}$ be an exhaustive partition of maximal **dependency hypotheses**. A dependency hypothesis $K$ is a complete, maximally specific specification of how all factors outside the agent’s causal control depend causally upon the agent’s possible actions. Under a fixed $K$, the outcome of choosing act $A$ is deterministic (or governed by fixed objective chances).

Because $K$ specifies external causal mechanics that are causally independent of the agent's current choice, the agent’s causal expected utility weights the utility of an act under each hypothesis by the *unconditional credence* that this causal state of affairs holds:

$$U_{\mathrm{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K) \sum_{j} P(O_j \mid A \land K) \, u(O_j)$$

If $A$ and $K$ uniquely fix an outcome $O_{A, K}$, this simplifies to:

$$U_{\mathrm{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K) \, u(O_{A, K})$$

Observe the mechanics: we do **not** weight by $P(K \mid A)$. The conditionalization $P(K \mid A)$ is precisely what EDT performs, permitting the choice of $A$ to update the agent's confidence regarding which causal hypothesis is true. CDT freezes the agent’s prior credences $P(K)$, forbidding the act from acting as an epistemic prism for background facts it cannot causally alter.

---

## 3. Resolving the Operational Vacuum: Modern Interventions

A chronic criticism highlighted in the reference text is that CDT does not uniquely specify how an agent is to compute or operationalize the counterfactual probabilities $P(A \to O_j)$. Lewis suggested the semantic procedure of **imaging**: to compute $P(A \to O)$, move the probability mass from each possible world $w$ to the "closest" possible world $w_A$ where $A$ is true. Yet, as Shaffer (2009) notes, identifying similarity metrics across possible worlds requires assessing what one would believe were $A$ true, inviting infinite epistemic regress or subjective ambiguity.

To turn CDT into an explicit, implementable decision procedure for unfamiliar cases, modern decision theorists frequently translate the philosophy of CDT into the language of **causal graphical models** and **Structural Causal Models (SCMs)**, pioneered by Judea Pearl.

*(Note: While rooted in Pearl's formal causality literature, applying the $do(\cdot)$ calculus as the direct, operational realization of Lewis–Gibbard–Harper CDT is an explanatory synthesis and interpretation developed here to bridge the vagueness problem raised in the source text).*

### The Structural Causal Architecture

Let a causal world be modeled by a tuple $\mathcal{M} = \langle \mathbf{U}, \mathbf{V}, \mathbf{F}, P(\mathbf{U}) \rangle$:
1. $\mathbf{U}$ is a set of exogenous background variables governed by probability distribution $P(\mathbf{U})$.
2. $\mathbf{V}$ is a set of endogenous observable variables, including the agent's decision variable $A$ and the utility payoff $Y$.
3. $\mathbf{F} = \{f_V : V \in \mathbf{V}\}$ is a set of deterministic structural equations $V = f_V(\mathbf{Pa}_V, \mathbf{U}_V)$, where $\mathbf{Pa}_V \subseteq \mathbf{V} \setminus \{V\}$ are the direct causal parents of $V$.

Within an SCM, conditioning on an event $A = a$ corresponds to standard Bayesian updating: observing $A = a$ prunes worlds where $A \neq a$ and updates the posterior distribution over exogenous variables $\mathbf{U}$ via Bayes' rule:

$$P(\mathbf{u} \mid A = a) = \frac{P(A = a \mid \mathbf{u}) P(\mathbf{u})}{P(A = a)}$$

This is the mathematical mechanism of **EDT**.

By contrast, choosing an act in CDT is modeled not by passive observation, but by the **intervention operator** $\mathrm{do}(A = a)$. An intervention replaces the structural equation governing the decision variable:

$$f_A(\mathbf{Pa}_A, \mathbf{U}_A) \quad \Longrightarrow \quad A := a$$

Graphically, this operation severs all incoming directed edges into $A$ in the causal directed acyclic graph (DAG), neutralizing confounding back-door paths between $A$ and prior causes. The structural equations for all other variables $V \in \mathbf{V} \setminus \{A\}$ remain completely invariant. 

The expected causal utility is then directly calculated via the interventional expectation:

$$U_{\mathrm{CDT}}(a) = \mathbb{E}[u(Y) \mid \mathrm{do}(A = a)] = \sum_{y} u(y) \, P(Y = y \mid \mathrm{do}(A = a))$$

By the back-door adjustment theorem, if $\mathbf{Z}$ is a sufficient set of confounders blocking all non-causal paths between $A$ and $Y$ (and containing no descendants of $A$), the interventional probability expands to:

$$P(Y = y \mid \mathrm{do}(A = a)) = \sum_{\mathbf{z}} P(Y = y \mid A = a, \mathbf{Z} = \mathbf{z}) P(\mathbf{Z} = \mathbf{z})$$

Notice that $\mathbf{Z}$ is weighted by its marginal prior probability $P(\mathbf{Z} = \mathbf{z})$, not the conditional probability $P(\mathbf{Z} = \mathbf{z} \mid A = a)$. This is the exact algebraic analogue of Lewis's dependency hypotheses: the distribution over the causal background is held invariant under intervention.

---

## 4. Benchmark Problems and Applications

To evaluate the mechanical behavior of CDT against EDT, we apply the formalisms to standard decision dilemmas.

### 4.1. Newcomb's Paradox

A reliable predictor (with predictive accuracy $q = 0.99$) presents an agent with two boxes:
* **Box A**: Transparent, containing $\$1{,}000$.
* **Box B**: Opaque, containing either $\$1{,}000{,}000$ or $\$0$.

The agent can choose either Box B alone (**one-boxing**, $A_1$) or both Box A and Box B (**two-boxing**, $A_2$). Yesterday, the predictor set the contents of Box B:
* If predicted $A_1 \implies$ Box B received $\$1{,}000{,}000$.
* If predicted $A_2 \implies$ Box B received $\$0$.

Let the payoff utilities be linear in dollars: $u(x) = x$.

```
           [ Predictor's Guess ]  (Yesterday)
                /            \
               v              v
    [ Contents of Box B ]   [ Agent's Choice ]  (Today)
               \              /
                v            v
                [ Total Payoff ]
```

#### EDT Analysis
The evidentialist assesses the choices using conditional distributions:

$$V_{\mathrm{EDT}}(A_1) = P(\text{B has } \$1\text{M} \mid A_1) \cdot \$1{,}000{,}000 + P(\text{B has } \$0 \mid A_1) \cdot \$0$$

$$V_{\mathrm{EDT}}(A_1) = (0.99)(\$1{,}000{,}000) + (0.01)(\$0) = \$990{,}000$$

$$V_{\mathrm{EDT}}(A_2) = P(\text{B has } \$1\text{M} \mid A_2) \cdot \$1{,}001{,}000 + P(\text{B has } \$0 \mid A_2) \cdot \$1{,}000$$

$$V_{\mathrm{EDT}}(A_2) = (0.01)(\$1{,}001{,}000) + (0.99)(\$1{,}000) = \$10{,}010 + \$990 = \$11{,}000$$

Because $V_{\mathrm{EDT}}(A_1) \gg V_{\mathrm{EDT}}(A_2)$, EDT firmly recommends **one-boxing**.

#### CDT Analysis
Under CDT, the state of Box B was fixed yesterday and lies in the causal past. No action chosen today can exert backwards causation on whether the cash is physically sitting in the box.

Let the dependency hypotheses be:
* $K_1$: Box B contains $\$1{,}000{,}000$.
* $K_0$: Box B contains $\$0$.

Let $P(K_1) = p$ and $P(K_0) = 1 - p$. The agent calculates:

$$U_{\mathrm{CDT}}(A_1) = p \cdot (\$1{,}000{,}000) + (1-p) \cdot (\$0) = 1{,}000{,}000 \, p$$

$$U_{\mathrm{CDT}}(A_2) = p \cdot (\$1{,}001{,}000) + (1-p) \cdot (\$1{,}000) = 1{,}000{,}000 \, p + 1{,}000$$

For any prior credence $p \in [0, 1]$:

$$U_{\mathrm{CDT}}(A_2) - U_{\mathrm{CDT}}(A_1) = \$1{,}000 > 0$$

Two-boxing strictly causally dominates one-boxing. In structural form, $\mathrm{do}(A)$ severs the edge between the predictor’s past forecast and the decision:

$$P(\text{Box B} = \$1\text{M} \mid \mathrm{do}(A_1)) = P(\text{Box B} = \$1\text{M} \mid \mathrm{do}(A_2)) = P(\text{Box B} = \$1\text{M})$$

The extra $\$1{,}000$ in Box A is guaranteed additional value regardless of the contents of Box B. CDT mandates **two-boxing**.

### 4.2. The Twin Prisoner's Dilemma

A parallel situation arises in a symmetric Prisoner's Dilemma against a psychological "twin" (Lewis 1979). Both players are deterministic reasoning systems executing near-identical cognitive algorithms. Hence, Player 1 defects if and only if Player 2 defects with high probability:

$$P(C_2 \mid C_1) \approx 1, \quad P(D_2 \mid D_1) \approx 1$$

EDT reasons that cooperating ($C_1$) yields strong evidence that the twin also cooperates ($C_2$), leading to the cooperative payoff $(R, R)$, which exceeds the mutual defection payoff $(P, P)$. EDT recommends Cooperation.

CDT, however, identifies that Player 1's physical execution of an action cannot causally affect Player 2's remote physical execution. Holding the twin's choice fixed (treating $C_2$ and $D_2$ as causal states outside Player 1's influence), Defection strictly dominates:

$$\begin{aligned}
U_{\mathrm{CDT}}(D_1) &= P(C_2) \cdot u(\text{Defect}, \text{Cooperate}) + P(D_2) \cdot u(\text{Defect}, \text{Defect}) \\
&> P(C_2) \cdot u(\text{Coop}, \text{Cooperate}) + P(D_2) \cdot u(\text{Coop}, \text{Defect}) = U_{\mathrm{CDT}}(C_1)
\end{aligned}$$

CDT mandates **Defection**, dismissing the statistical correlation as acausal common-mode alignment.

---

## 5. Pathologies and Contemporary Counterexamples

While CDT provides clean, intuitive recommendations in common-cause settings like King David, critics argue that its uncompromising refusal to update causal credences based on deliberations leads to catastrophic behavioral failures.

### 5.1. Andy Egan’s "Psychopath Button"

Andy Egan (2007) introduced scenarios featuring self-reinforcing, toxic diagnostic feedback.

Suppose Paul is debating whether to press a button that will instantaneously kill all psychopaths on Earth. Paul holds the following views:
1. It is overwhelmingly desirable to live in a world without psychopaths: $u(\text{world without psychopaths}) = 100$, whereas $u(\text{status quo}) = 10$.
2. Dying is disastrous: $u(\text{death}) = -1{,}000$.
3. Paul assigns an initial prior credence that he himself is a psychopath of $P(\text{Psy}) = 0.01$.
4. Critically, only a psychopath would ever press this button. Thus, pressing the button provides virtually conclusive evidence that the agent is a psychopath: $P(\text{Psy} \mid \text{Press}) \approx 1.0$.

#### CDT Evaluation
Whether Paul is a psychopath is an unalterable biological and developmental fact. Pressing the button does not cause Paul to become a psychopath; it simply executes all members of the category.

Holding fixed his prior credence $P(\text{Psy}) = 0.01$:
* If Paul is not a psychopath: Pressing the button kills all psychopaths while Paul survives, yielding utility $100$.
* If Paul is a psychopath: Pressing the button kills all psychopaths, including Paul, yielding utility $-1{,}000$.

The causal expected utility of pressing ($A$) is:

$$U_{\mathrm{CDT}}(A) = (0.99)(100) + (0.01)(-1{,}000) = 99 - 10 = +89$$

The utility of not pressing ($\neg A$) maintains the status quo:

$$U_{\mathrm{CDT}}(\neg A) = 10$$

Because $89 > 10$, CDT instructs Paul to **press the button**. 

Yet, as Egan points out, this recommendation seems pathological. The instant Paul forms the intention or reaches out his finger to press the button, he acquires decisive evidence that he is a psychopath. He is electing an action fully confident that doing so will result in his own imminent demise.

### 5.2. Deliberational Instability and "Death in Damascus"

In the classic "Death in Damascus" dilemma, an agent learns that Death is an exceptional predictor of human location. 
* Death has predicted whether the agent will be in Damascus ($D$) or Aleppo ($A$) tomorrow, and is currently waiting in the predicted city.
* If the agent meets Death, the utility is $-100$.
* If the agent goes to the other city, he escapes, yielding utility $0$.
* Death's predictive reliability is $0.99$.

Suppose the agent currently leans toward Damascus ($P(D) \approx 1$). Since Death anticipated this, Death is almost certainly in Damascus. Evaluating his options causally:
* The causal value of going to Damascus is $\approx -100$.
* The causal value of fleeing to Aleppo is $\approx 0$.

CDT instantly directs the agent to switch his choice to Aleppo. But as soon as the agent decides to go to Aleppo, his credence updates: he now expects to go to Aleppo ($P(A) \approx 1$). Under this revised belief, Death has surely anticipated Aleppo, meaning Aleppo now offers $-100$ and Damascus offers $0$. The agent is trapped in endless deliberational cycling: no pure action remains stable once chosen.

### 5.3. The Adversarial Offer and Exploitation

Recent formal work has shown that CDT's causal blind spot allows adversaries to systematically siphon wealth from agents. Oesterheld and Conitzer (2021), extending scenarios by Spencer (2020), proved that CDT agents can be subjected to diachronic Dutch books—schemes where an agent freely accepts a series of transactions that guarantee a net financial loss.

Consider the **Adversarial Offer**:
* A seller offers two opaque boxes (Box 1 and Box 2) for purchase. 
* An agent may buy Box 1, buy Box 2, or buy neither. Buying both is prohibited.
* Each box costs exactly $\$1.00$.
* Yesterday, the seller placed $\$3.00$ in each box that she predicted the buyer would **not** acquire.
* Both parties agree the seller's predictions are accurate with probability $p = 0.75$.

#### The CDT Calculation
The agent reasons causally about the contents of the boxes. Because the seller can predict the choice of at most one box (or none), the agent calculates that:
* At least one box definitely contains $\$3.00$ (if the agent buys Box 1, Box 2 certainly has $\$3.00$; if the agent buys Box 2, Box 1 certainly has $\$3.00$; if the agent buys neither, both have $\$3.00$).
* By symmetry, the agent assigns an expected monetary content to each box of at least:

$$\mathbb{E}[\text{Cash in Box } i] \ge \frac{1}{2}(\$3.00) = \$1.50$$

Because the expected causal value of the contents of either box ($\ge \$1.50$) strictly exceeds the acquisition price ($\$1.00$), CDT dictates that declining both boxes is strictly suboptimal. CDT mandates purchasing one of the boxes (say, Box 1).

#### The Evidential Reality
The moment the CDT buyer chooses Box 1, the seller’s $75\%$ accuracy takes effect:

$$\mathbb{E}[\text{Payoff} \mid \text{Chooses Box 1}] = (0.25)(\$3.00) - \$1.00 = \$0.75 - \$1.00 = -\$0.25$$

The seller extracts an expected profit of $\$0.25$ per interaction, while the buyer voluntarily incurs an expected loss of $\$0.25$ on an exchange where a passive agent (buying neither) guarantees a net loss of $\$0.00$. CDT's demand to hold the causal distribution invariant leaves the agent structurally vulnerable to predatory mechanism design.

---

## 6. The Modern Defense: Ratifiability and Deliberational Dynamics

To preserve CDT without embracing the common-cause fallacies of EDT, prominent causal decision theorists—most notably James M. Joyce (2012, 2020)—have introduced refined dynamic frameworks.

### 6.1. Ratifiability
Originally proposed by Richard Jeffrey (1983) and adapted for CDT, **ratifiability** posits that an action $A$ is rational only if it maximizes causal expected utility *relative to the posterior credences formed on the assumption that $A$ will actually be executed*:

$$\text{Act } A \text{ is ratifiable iff } U_{\mathrm{CDT}}(A \mid A) \ge U_{\mathrm{CDT}}(A' \mid A) \quad \forall A' \in \mathcal{A}$$

In the **Psychopath Button**:
* If Paul assumes he will press the button ($A$), his updated credence that he is a psychopath becomes $P(\text{Psy} \mid A) \approx 1.0$.
* Evaluating the causal expected utility of pressing *conditional on this state of belief*:

$$U_{\mathrm{CDT}}(A \mid A) \approx (0)(100) + (1.0)(-1{,}000) = -1{,}000$$

* The causal value of refraining conditional on this belief is $U_{\mathrm{CDT}}(\neg A \mid A) = 10$.

Pressing the button is **unratifiable**. A rational CDT agent seeking ratifiable choices would refuse to press, avoiding Egan's trap.

### 6.2. Deliberational Dynamics
When no pure act is ratifiable (as in Death in Damascus or the Adversarial Offer), Joyce models deliberation as a continuous-time dynamic process. An agent begins with a choice probability vector $\mathbf{p}_t = (p_1, \dots, p_n)$ over available acts. As the agent contemplates taking act $A_k$, their epistemic credences update, which in turn alters the causal expected utilities $U_{\mathrm{CDT}}(A_i \mid \mathbf{p}_t)$. 

The agent updates probabilities via an adjustment rule (such as the replicator dynamic or gradient ascent on causal utility):

$$\frac{d p_i}{dt} = g_i\big(U_{\mathrm{CDT}}(A_i \mid \mathbf{p}_t) - \bar{U}\big)$$

In Death in Damascus, this dynamic converges to the mixed-strategy equilibrium where $P(\text{Damascus}) = P(\text{Aleppo}) = 0.5$. At this fixed point, neither city causally dominates, and the agent resolves the decision via objective randomization, breaking the adversarial prediction.

---

## 7. Comparative Mathematical Synthesis

The operational differences across decision paradigms can be captured succinctly in how each theory computes the expected value of an act $A$ across states $S$ and outcomes $O$:

| Decision Theory | Mathematical Criterion | Treatment of Dependencies |
| :--- | :--- | :--- |
| **Evidential Decision Theory (EDT)** | $\sum_{j} P(O_j \mid A) u(O_j)$ | Exploits all statistical correlations; conflates diagnostic signals with causal consequences. |
| **Causal Decision Theory (Gibbard–Harper)** | $\sum_{j} P(A \to O_j) u(O_j)$ | Evaluates probability of counterfactual conditionals; acts independent of conditionals. |
| **Causal Decision Theory (Lewis)** | $\sum_{K} P(K) \sum_{j} P(O_j \mid A \land K) u(O_j)$ | Weights by unconditional credences in dependency hypotheses $K$; holds causal background fixed. |
| **Interventional CDT (Pearl / SCM)** | $\sum_{y} u(y) P(y \mid \mathrm{do}(A))$ | Cuts incoming edges to $A$; computes interventional distributions via graph surgery. |

---

## Conclusion

Causal Decision Theory embodies an uncompromising normative stance: **rational action consists in producing desirable outcomes, not in purchasing encouraging information.** By isolating the causal channels of agency—whether through Lewisian dependency hypotheses, counterfactual probability metrics, or explicit interventional graph surgeries—CDT insulates rational agents from the superstitions that mislead evidentialist reasoning in common-cause settings.

Yet this sharp separation between action and diagnosis generates its own vulnerabilities. In strategic environments populated by accurate predictors, correlated twins, or adversarial market-makers, an agent's choices are deeply informative about the world they inhabit. CDT’s insistence on holding background causal hypotheses fixed blinds the agent to the adverse informational costs of its own deliberative commitments. 

Whether CDT remains the definitive account of individual instrumental rationality depends largely on the success of modern extensions: specifically, whether ratifiability and continuous deliberational dynamics can successfully reconcile pure causal intervention with the harsh reality of predictive environments.

---

### References

* Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
* Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
* Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
* Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
* Joyce, J. M. (2020). *Yet Another Refutation of Causal Decision Theory?*
* Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4), pqaa086.
* Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
* Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.
* Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.