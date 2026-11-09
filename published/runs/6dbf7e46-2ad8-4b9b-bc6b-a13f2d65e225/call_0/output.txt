# The Logic of News Value: A Formal and Philosophical Exposition of Evidential Decision Theory

## 1. Introduction: Auspiciousness versus Efficacy

At the core of rational choice theory lies an apparently simple prescription: an agent confronted with a set of mutually exclusive actions should choose an action that maximizes expected utility. Yet, formalizing "expected utility" exposes a fundamental fault line in mathematical philosophy. When an agent contemplates an action, should they evaluate the action by the consequences it will *causally bring about*, or by the epistemic state they would enter upon *learning* that they have chosen it?

The latter principle is the defining thesis of **Evidential Decision Theory (EDT)**. In the words of Arif Ahmed, EDT urges an agent to "do what you most want to learn that you will do" (Ahmed 2021). The value of an act is identified with its *news value*: how desirable the world is expected to be, conditional on receiving the news that the act was executed.

In contrast, **Causal Decision Theory (CDT)** insists that rational action must track *causal efficacy*. As James M. Joyce wrote:

> "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news." (Joyce 1999)

The debate between EDT and CDT has generated some of the most enduring puzzles in formal epistemology, statistics, and game theory—most notably Newcomb’s Paradox and the Twin Prisoner’s Dilemma. 

In this essay, we develop a rigorous mathematical foundation for EDT, contrast its formal architecture with CDT, examine how it evaluates policies across canonical thought experiments, and confront the primary criticisms leveled against it—in particular David Lewis’s famous charge that EDT recommends an irrational policy of "managing the news" (Lewis 1981). Along the way, we distinguish the core mathematical claims presented in the literature from the operational and structural assumptions required to apply EDT to novel and partially observed decision environments.

---

## 2. Formal Architecture

### 2.1 The Probability Space and Value Function

Let $(\Omega, \mathcal{F}, P)$ be a probability space representing an agent’s subjective credences over possible worlds. We define three collections of events within $\mathcal{F}$:

1. **Actions ($\mathcal{A}$):** A finite or countable set of pairwise disjoint, non-null events $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ representing the mutually exclusive options immediately available to the agent, with $P(A_i) > 0$ for all $i$.
2. **Outcomes ($\mathcal{O}$):** A finite or countable partition of $\Omega$, denoted $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$, representing the fine-grained states of affairs about which the agent intrinsically cares.
3. **Desirability Function ($D$):** A utility mapping $D: \mathcal{O} \to \mathbb{R}$ assigning real-valued cardinal utility to each outcome.

Following the formulation of Allan Gibbard and William Harper (1976), the evidential expected utility (or desirability, $V$) of an action $A \in \mathcal{A}$ is given by:

$$V(A) = \sum_{j} P(O_j \mid A) \, D(O_j)$$

where $P(O_j \mid A) = \frac{P(O_j \cap A)}{P(A)}$ denotes standard Kolmogorov conditional probability.

The decision rule of EDT is straightforward:

$$\text{Select } A^* \in \mathcal{A} \quad \text{such that} \quad A^* \in \arg\max_{A \in \mathcal{A}} V(A)$$

If multiple actions achieve the maximum, any tie-breaking rule (or indifference) is permitted.

### 2.2 EDT versus CDT: The Formal Wedge

To see why EDT diverges from CDT, consider Gibbard and Harper’s formalization of causal expected utility, denoted $U(A)$:

$$U(A) = \sum_{j} P(A \mathbin{\Box\rightarrow} O_j) \, D(O_j)$$

Here, $A \mathbin{\Box\rightarrow} O_j$ is the counterfactual proposition: *"If action $A$ were chosen, outcome $O_j$ would obtain."* In Stalnaker–Lewis possible-worlds semantics, this proposition is true at a world $\omega$ if and only if $O_j$ holds in the closest accessible world to $\omega$ where $A$ is true. 

In general, epistemic conditionalization does not match counterfactual conditioning:

$$P(O_j \mid A) \neq P(A \mathbin{\Box\rightarrow} O_j)$$

* $P(O_j \mid A)$ measures how likely $O_j$ is given the **evidence** that $A$ occurred. It is sensitive to common causes that correlate $A$ and $O_j$ upstream.
* $P(A \mathbin{\Box\rightarrow} O_j)$ measures whether $A$ exerts **causal influence** over $O_j$, holding fixed all background facts not causally downstream of $A$.

In decision-analytic terms, CDT evaluates an action by intervening on the system (akin to Judea Pearl’s $\text{do}(A)$ operator), whereas EDT evaluates an action by conditioning on the event $A$ within the unmanipulated joint distribution:

$$V_{\text{EDT}}(A) = \mathbb{E}[D \mid A] \quad \text{versus} \quad U_{\text{CDT}}(A) = \mathbb{E}[D \mid \text{do}(A)]$$

---

## 3. Canonical Applications

### 3.1 Newcomb’s Paradox

In Newcomb’s problem (Wolpert & Benford 2013), an agent faces two boxes:
* **Box A (transparent):** Always contains $\$1,000$.
* **Box B (opaque):** Contains either $\$1,000,000$ or $\$0$, placed there yesterday by a highly accurate Predictor.

The Predictor operated as follows:
* If she predicted the agent would take **only Box B** ("one-box"), she deposited $\$1,000,000$ into Box B.
* If she predicted the agent would take **both Box A and Box B** ("two-box"), she left Box B empty.

Let the action set be $\mathcal{A} = \{A_1, A_2\}$, where $A_1$ is "take only B" and $A_2$ is "take both boxes." Let $M$ be the state that Box B contains $\$1,000,000$, and $E$ be the state that Box B is empty ($E = M^c$). The agent assumes linear utility in money: $D(\$x) = x$.

Assume the Predictor has symmetric accuracy $p \in (0.5, 1]$:

$$P(M \mid A_1) = p, \quad P(E \mid A_1) = 1-p$$
$$P(E \mid A_2) = p, \quad P(M \mid A_2) = 1-p$$

#### Evidential Calculation:

$$\begin{aligned}
V(A_1) &= P(M \mid A_1) \cdot \$1{,}000{,}000 + P(E \mid A_1) \cdot \$0 \\
&= p \cdot 10^6 \\
V(A_2) &= P(M \mid A_2) \cdot \$1{,}001{,}000 + P(E \mid A_2) \cdot \$1{,}000 \\
&= (1-p) \cdot 1{,}001{,}000 + p \cdot 1{,}000 \\
&= 1{,}001{,}000 - 10^6 p
\end{aligned}$$

Comparing the two:

$$V(A_1) - V(A_2) = p \cdot 10^6 - (1{,}001{,}000 - 10^6 p) = 2 \cdot 10^6 p - 1{,}001{,}000$$

$$V(A_1) > V(A_2) \iff p > \frac{1{,}001{,}000}{2{,}000{,}000} = 0.5005$$

For a predictor with $p = 0.99$:

$$V(A_1) = 0.99 \times \$1{,}000{,}000 = \$990{,}000$$
$$V(A_2) = 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$10{,}010 + \$990 = \$11{,}000$$

EDT decisively prescribes **$A_1$ (one-boxing)**.

#### The Causal Contrast:

Under CDT, the state of Box B was fixed yesterday. The counterfactuals satisfy:

$$P(A_1 \mathbin{\Box\rightarrow} M) = P(M) \quad \text{and} \quad P(A_2 \mathbin{\Box\rightarrow} M) = P(M)$$

Hence:

$$U(A_1) = P(M) \cdot 10^6$$
$$U(A_2) = P(M) \cdot 1{,}001{,}000 + (1 - P(M)) \cdot 1{,}000 = P(M) \cdot 10^6 + 1{,}000$$

Because $U(A_2) - U(A_1) = \$1{,}000 > 0$ for *any* prior $P(M)$, CDT prescribes **$A_2$ (two-boxing)** via strict dominance.

EDT rejects the dominance argument because the states (contents of Box B) are not epistemically independent of the actions: choosing $A_2$ provides terrible news regarding whether $M$ holds.

---

### 3.2 The Twin Prisoner's Dilemma

Consider Aomame and her psychological twin (Greene & Levinstein 2020). Each must choose between Cooperate ($C$) and Defect ($D$) without communicating. The payoff matrix (in dollars) is:

| | Twin: $C$ | Twin: $D$ |
|---|---|---|
| **Aomame: $C$** | $(5, 5)$ | $(0, 10)$ |
| **Aomame: $D$** | $(10, 0)$ | $(1, 1)$ |

Let $C_T$ and $D_T$ denote the twin's choices. Because Aomame and her twin share identical cognitive algorithms and deliberation procedures, their choices are strongly correlated:

$$P(C_T \mid C) = 1 - \epsilon, \quad P(D_T \mid D) = 1 - \delta$$

In the idealized limit where the twin is an exact psychological replica, $\epsilon = \delta = 0$.

#### Evidential Evaluation:

$$\begin{aligned}
V(C) &= P(C_T \mid C) \cdot 5 + P(D_T \mid C) \cdot 0 = (1 - \epsilon) \cdot 5 \\
V(D) &= P(C_T \mid D) \cdot 10 + P(D_T \mid D) \cdot 1 = \delta \cdot 10 + (1 - \delta) \cdot 1 = 1 + 9\delta
\end{aligned}$$

For $\epsilon = \delta = 0$:

$$V(C) = 5 > V(D) = 1$$

EDT recommends **Cooperate**. Even though Aomame’s physical act does not causally alter her twin’s brain states in a distant room, her decision serves as decisive evidence for what cognitive procedure "agents like them" execute. 

CDT, conversely, observes that Aomame's choice has zero causal influence over the twin ($P(C \mathbin{\Box\rightarrow} C_T) = P(C_T)$). For any fixed state of the twin, defecting yields $\$5$ more if the twin cooperates ($10 > 5$) and $\$1$ more if the twin defects ($1 > 0$). CDT thus dictates **Defection**, leaving two causal decision theorists with $\$1$ each, while two evidential decision theorists walk away with $\$5$ each.

---

## 4. The Central Controversy: Managing the News and the Tickle Defense

### 4.1 The Medical Fallacy and the Smoking Lesion

The most celebrated challenge to EDT is the *Smoking Lesion* problem. Suppose a genetic lesion $L$ causes both a craving to smoke ($S$) and lung cancer ($C$). Smoking itself does not causally cause cancer; it is merely an epiphenomenon of $L$:

```
       Lesion (L)
       /        \
      v          v
 Smoking (S)    Cancer (C)
```

Suppose:
* $P(L) = 0.2$
* An agent with $L$ smokes with probability $0.8$; an agent without $L$ smokes with probability $0.1$.
* An agent with $L$ gets cancer with probability $0.9$; an agent without $L$ gets cancer with probability $0.05$.
* Utility of smoking: $+1$. Utility of cancer: $-100$.

By Bayes' rule:

$$P(L \mid S) = \frac{P(S \mid L)P(L)}{P(S)} = \frac{0.8 \times 0.2}{(0.8 \times 0.2) + (0.1 \times 0.8)} = \frac{0.16}{0.16 + 0.08} = \frac{2}{3} \approx 0.667$$

$$P(L \mid \neg S) = \frac{P(\neg S \mid L)P(L)}{P(\neg S)} = \frac{0.2 \times 0.2}{(0.2 \times 0.2) + (0.9 \times 0.8)} = \frac{0.04}{0.04 + 0.72} = \frac{0.04}{0.76} \approx 0.053$$

The probability of cancer given smoking is:

$$P(C \mid S) = P(C \mid L) P(L \mid S) + P(C \mid \neg L) P(\neg L \mid S) = 0.9\left(\frac{2}{3}\right) + 0.05\left(\frac{1}{3}\right) \approx 0.617$$

The probability of cancer given abstention is:

$$P(C \mid \neg S) = P(C \mid L) P(L \mid \neg S) + P(C \mid \neg L) P(\neg L \mid \neg S) = 0.9(0.053) + 0.05(0.947) \approx 0.095$$

Computing the values:

$$V(S) = 1 - 100 \times P(C \mid S) \approx 1 - 61.7 = -60.7$$
$$V(\neg S) = 0 - 100 \times P(C \mid \neg S) \approx 0 - 9.5 = -9.5$$

EDT recommends **not smoking**.

David Lewis (1981) argued that this recommendation is absurd. The agent already either has the lesion or does not. Smoking does not *cause* cancer. Refusing to smoke merely to suppress bad news about one's genetic makeup constitutes an irrational attempt to **"manage the news."** It is analogous to an actor refusing to look at an existing diagnosis because an untreated illness is preferable in ignorance.

### 4.2 The "Tickle Defense" and Its Limitations

Proponents of EDT respond with the **Tickle Defense**. They argue that the Smoking Lesion scenario is psychologically underspecified. 

If the lesion causes smoking via a psychological mechanism—such as an intense conscious craving or "tickle" $T$—then an introspective agent already knows whether they feel $T$. Once the agent conditions on their own internal mental state $T$, the action of smoking is conditionally independent of the lesion:

$$P(L \mid S \cap T) = P(L \mid \neg S \cap T)$$

Under this conditional independence, the "news value" of smoking is screened off by the agent’s introspective awareness. Smoking no longer provides evidence about $L$ beyond what the craving already provided. Consequently:

$$V(S \mid T) - V(\neg S \mid T) = D(\text{pleasure of smoking}) > 0$$

EDT would then permit smoking.

However, critics point out that the Tickle Defense depends on strong assumptions:
1. The common cause must act entirely through a consciously accessible intermediary.
2. The agent must possess perfect, transparent self-knowledge of their dispositions before deciding.

If the lesion predisposes choices subconsciously—or if the choice itself is the only epistemically accessible sign of one's disposition—the screening-off condition fails, and EDT once again advises abstaining.

---

## 5. Formal Extensions and Open Foundational Questions

The foundational literature leaves several operational and mathematical questions unaddressed or contentious. We examine three critical ones here, developing explicit proposals where standard formulations fall short.

### 5.1 The Probability of Acts: $P(A)$ and Deliberation

Standard Kolmogorov conditioning requires $P(A) > 0$. But what credence should an agent assign to their own acts during deliberation?

* **The Problem:** If an agent believes that rational deliberation is deterministic, then conditional on deciding to perform $A^*$, the probability of alternative acts $A'$ might appear to be zero, rendering $P(O \mid A')$ undefined.
* **Operational Interpretation (Epsilon-Exploration / Trembling Hand):** 
  To formalize EDT rigorously in non-trivial computational agents, we can define an agent's credences over actions through a perturbed policy model. Let $\pi_\theta(A)$ be a parameterized decision policy. We evaluate actions by considering the limit of an explicit deliberation process with an infinitesimal exploration probability $\epsilon$:

  $$P_\epsilon(A) = (1-\epsilon)\mathbb{I}(A = \arg\max V) + \frac{\epsilon}{|\mathcal{A}|}$$

  Alternatively, an agent treats their pending decision as a random variable correlated with their character until deliberation concludes. The credences $P(O \mid A)$ are well-defined throughout deliberation because the agent maintains a strictly positive prior distribution $P(A) \in (0, 1)$ over all options under consideration.

### 5.2 Dynamic Consistency and Sequential Decisions

Consider a sequential decision problem where an agent chooses an action $A_1 \in \mathcal{A}_1$ at time $t_1$, observes an intermediate signal $S \in \mathcal{S}$, and then chooses $A_2 \in \mathcal{A}_2$ at time $t_2$.

How does EDT evaluate a multi-stage policy $\pi = (\pi_1, \pi_2)$?
There are two competing frameworks:

1. **Global Evidential Policy Selection:** Choose a policy $\pi^* = (\pi_1, \pi_2)$ upfront that maximizes:

   $$V(\pi) = \sum_{O} P(O \mid \text{Agent implements } \pi) \, D(O)$$

2. **Myopic or Local Update:** At each information set $I_{t}$, condition on the current history $h_t$ and choose:

   $$A_t^* = \arg\max_{A \in \mathcal{A}_t} \sum_{O} P(O \mid h_t \cap A) \, D(O)$$

These two formulations can diverge. If an agent at $t_1$ knows that taking action $A_1$ will tempt their future self at $t_2$ into taking an action that provides bad news, a naive local evidential updater may fail backward induction or exhibit dynamic inconsistency. 

**Proposal:** A fully coherent evidential agent must adopt **sophisticated evidential planning**: when evaluating an early action $A_1$, the agent must model their future choice $A_2$ as an endogenous random variable determined by the evidential reasoning of their future self:

$$V(A_1) = \sum_{S} P(S \mid A_1) \sum_{A_2} P(A_2 \mid A_1, S) \sum_{O} P(O \mid A_1, S, A_2) D(O)$$

where $P(A_2 \mid A_1, S)$ reflects the agent's rational prediction of their future evidential choice.

### 5.3 The Sleeping Beauty Problem and Anthropic Credence

The reference material notes that EDT has been applied to the Sleeping Beauty problem to resolve Dutch book vulnerabilities (Conitzer 2015). 

In the Sleeping Beauty setup:
* Beauty is put to sleep on Sunday. A fair coin is tossed.
* **Heads ($H$):** She is awakened on Monday only.
* **Tails ($T$):** She is awakened on Monday, given an amnesia drug to erase the memory, and awakened again on Tuesday.
* Upon awakening, Beauty is asked for her credence in $H$: is it $1/2$ ("halfer") or $1/3$ ("thirder")?

A halfer assigns $P(H \mid \text{Awake}) = 1/2$. However, under standard decision rules, halfers can be subjected to Dutch books if offered repeated bets across awakenings without knowing what day it is. 

Under EDT, when Beauty is offered a bet upon awakening, she recognizes that her decision to accept the bet provides evidence about her actions across *all* identical awakenings:

$$V(\text{Accept}) = \sum_{c \in \{H, T\}} P(c \mid \text{Accept at this awakening}) \cdot \mathbb{E}[\text{Payoff} \mid c, \text{Accept at all correlated awakenings}]$$

Because an acceptance under $T$ implies two acceptances (Monday and Tuesday), EDT automatically weights the tails world by a factor of 2. 

As Conitzer (2015) formalizes, EDT allows an agent holding halfer credences ($P(H) = 1/2$) to bet *as if* she were a thirder, neutralizing standard Dutch books. However, Conitzer also proves that halfers who adopt EDT remain vulnerable to more sophisticated Dutch books unless their priors are adjusted to account for the anthropic selection mechanism itself.

---

## 6. The Evidentialist's Wager

A striking modern defense of EDT does not argue that EDT is metaphysically superior to CDT, but that one should act evidentially as a matter of **normative decision-theoretic hedging** (MacAskill et al. 2021).

Suppose an agent has meta-theoretic uncertainty over decision theories:

$$P(\text{EDT is correct}) = \alpha, \quad P(\text{CDT is correct}) = 1 - \alpha \quad (\text{with } 0 < \alpha < 1)$$

In standard situations, CDT and EDT agree. But in correlation scenarios—such as the Twin Prisoner’s Dilemma or interactions across large populations of similar algorithmic agents—the stakes can scale with the number of correlated agents.

Let $N$ be the number of correlated decision-makers facing a social dilemma. 
* If CDT is true, an individual agent's choice only affects their local payoff: the causal difference is bounded by an individual increment $\Delta_{\text{local}} = O(1)$.
* If EDT is true, an agent's choice to cooperate provides evidence that all $N$ agents will cooperate: the evidential difference scales with the collective outcome $\Delta_{\text{global}} = O(N)$.

Under an expected utility calculation across decision theories:

$$\mathbb{E}[\Delta V] = \alpha \cdot O(N) - (1 - \alpha) \cdot O(1)$$

For sufficiently large $N$, the evidential term dominates whenever $\alpha > 0$:

$$N > \frac{(1 - \alpha)}{\alpha} \frac{O(1)}{O(1)} \implies \text{Act according to EDT}$$

This result—known as **The Evidentialist's Wager**—shows that whenever an agent is correlated with a vast population of reasoning peers (for instance, in cosmologically large universes or distributed artificial intelligence systems), the expected stakes under EDT dwarf those under CDT. Consequently, even an agent with low credence in EDT should often adopt evidential recommendations in practice.

---

## 7. Comparative Summary: EDT, CDT, and Dilemmas

The table below contrasts EDT and CDT across the primary benchmarks:

| Scenario | EDT Verdict | CDT Verdict | Primary Mechanism in EDT |
|---|---|---|---|
| **Newcomb's Paradox** | **One-box** ($A_1$) | **Two-box** ($A_2$) | Choice provides evidence about yesterday’s prediction. |
| **Twin Prisoner's Dilemma** | **Cooperate** ($C$) | **Defect** ($D$) | Twin's action is conditionally correlated with one's own. |
| **Smoking Lesion (without tickle)** | **Abstain** ($\neg S$) | **Smoke** ($S$) | Action betokens bad news regarding the lesion. |
| **Smoking Lesion (with tickle)** | **Smoke** ($S$) | **Smoke** ($S$) | Craving screens off the evidential link to the lesion. |
| **Sleeping Beauty (Halfer)** | **Bet as 1/3** | **Bet as 1/2** | Wager accepted today implies wagers accepted across awakenings. |

---

## 8. Algorithmic Protocol for Applying EDT to Unfamiliar Cases

To apply EDT systematically to an arbitrary decision problem, one can follow this five-step protocol:

1. **State Space and Payoffs:** Construct the set of disjoint available actions $\mathcal{A}$ and the outcome space $\mathcal{O}$. Define the utility function $D: \mathcal{O} \to \mathbb{R}$.
2. **Joint Credence Model:** Formulate the agent's prior subjective probability distribution $P$ over the product space $\mathcal{A} \times \mathcal{S} \times \mathcal{O}$, where $\mathcal{S}$ represents external states of the world. Ensure $P(A) > 0$ for all $A \in \mathcal{A}$.
3. **Screening-Off Analysis:** Determine whether any intermediate variables (such as conscious cravings, emotions, or deliberations) screen off the action from background common causes:
   $$\text{Check if } P(S \mid A \cap I) = P(S \mid I) \quad \text{for introspective state } I$$
4. **Conditional Expectation:** For each candidate action $A \in \mathcal{A}$, compute:
   $$V(A) = \sum_{O \in \mathcal{O}} P(O \mid A) \, D(O) = \sum_{S \in \mathcal{S}} P(S \mid A) \, D(O(A, S))$$
5. **Argmax Selection:** Select an action that achieves $\max_{A \in \mathcal{A}} V(A)$.

---

## 9. Conclusion

Evidential Decision Theory offers a conceptually unified and mathematically clean model of rational choice: an agent evaluates an action by calculating the expected value of the world conditional on having chosen that action. It requires no primitive counterfactual machinery, no causal graph discovery, and no structural equation modeling.

The primary philosophical challenge to EDT remains the charge of "managing the news." When correlated background states are physically unalterable, choosing an action simply because it signals good news can appear irrational to causal intuition. Yet, as demonstrated by Newcomb's Paradox and the Twin Prisoner's Dilemma, agents who follow causal decision theory systematically end up poorer than evidential agents when interacting with accurate predictors or cognitive peers. 

Whether EDT is ultimately viewed as the true theory of rationality, an elegant heuristic for multi-agent coordination, or an essential hedge in meta-decision theory, its formal study reveals a deep truth: the boundary between what an agent *brings about* and what an agent *learns about themselves* is among the most subtle problems in probability and logic.

---

## References

* Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
* Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese*, 192(9), 2887–2899.
* Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*. Discussion Paper No. 194, Center for Mathematical Studies in Economics and Management Science, Northwestern University.
* Greene, P., & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives*, 34(1), 100–101.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy*, 59(1), 5–30.
* MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist's Wager*. Global Priorities Institute Working Paper.
* Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese*, 190(9), 1637–1646.