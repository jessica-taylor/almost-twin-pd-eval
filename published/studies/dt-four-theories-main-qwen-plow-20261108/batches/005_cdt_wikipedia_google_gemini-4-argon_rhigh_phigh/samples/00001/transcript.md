# 005_cdt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00001

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c05ad917-7ca0-41ac-806b-08f1bba00842/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c05ad917-7ca0-41ac-806b-08f1bba00842/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Counterfactuals, Interventions, and Rational Choice: A Mathematical Guide to Causal Decision Theory

When an agent deliberates over a set of possible actions, every prospective choice plays a dual role. On the one hand, an action is an *intervention* in the world—a causal lever that brings about downstream consequences. On the other hand, the fact that an agent chooses a particular action is often a *symptom* of pre-existing background conditions, such as the agent's character, genetic dispositions, or how third parties have modeled the agent's behavior. 

How should a formal theory of rationality weigh these two roles? **Causal decision theory** (CDT) is the school of thought within decision theory holding that rational choice must be governed exclusively by the first role: when confronted with a set of possible actions, an agent should select the action that *causes* the best outcome in expectation. In contrast, **evidential decision theory** (EDT) evaluates actions according to their symptomatic value, recommending whichever action would provide the best "news" about the state of the world if the agent learned that it had been taken (Ahmed 2021).

At an intuitive level, CDT is almost self-evident. As the reference article illustrates, if eating an apple causes happiness and eating an orange causes sadness, rationality dictates eating the apple. When the causal consequences of an action are uncertain—say, when eating a good apple causes happiness, eating a bad apple causes sadness, and the agent does not know whether the apple on the table is good or bad—the agent must calculate the *expected* causal effect by weighing the utilities of those outcomes against the probabilities of the apple's quality. 

Yet turning this intuition into a rigorous mathematical procedure raises deep questions about probability, counterfactual logic, and agency. This essay provides a formal account of CDT, reconstructs the mathematical machinery linking counterfactual conditionals to statistical independence, develops concrete operational algorithms where the philosophical literature leaves the formalism underspecified, and analyzes the modern game-theoretic paradoxes that test the limits of causal rationality. Throughout, we explicitly distinguish the core claims of the reference text from our own mathematical reconstructions and operational proposals.

---

## 1. The Formal Architecture of CDT and EDT

Let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a finite set of mutually exclusive actions available to an agent, and let $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$ be a finite partition of mutually exclusive and exhaustive outcomes encoding everything the agent cares about. Each outcome $O_j$ is assigned a real-valued desirability (or utility) $D(O_j) \in \mathbb{R}$, and the agent's epistemic state is represented by a probability measure $P$ over an algebra of propositions that includes $\mathcal{A}$ and $\mathcal{O}$.

In the framework of Evidential Decision Theory (commonly associated with Richard Jeffrey), the news-value or evidential expected utility $V(A)$ of an action $A \in \mathcal{A}$ with $P(A) > 0$ is computed via standard Bayesian conditionalization:

$$V_{\text{EDT}}(A) = \sum_{j=1}^{n} P(O_j \mid A) D(O_j), \quad \text{where } P(O_j \mid A) = \frac{P(A \land O_j)}{P(A)}.$$

In a foundational 1981 paper, Allan Gibbard and William Harper argued that conditional probability conflates causal efficacy with purely diagnostic correlation. They proposed instead that causal decision theory maximizes expected utility $U(A)$ calculated from the probabilities of *counterfactual conditionals* (Gibbard & Harper 1981):

$$U_{\text{CDT}}(A) = \sum_{j=1}^{n} P(A \to O_j) D(O_j).$$

In the wording of the reference text, $P(A \to O_j)$ is described as "the counterfactual probability of it being the case that $A$ necessarily implies $O_j$." From a technical standpoint, we must refine this terminology: in the semantics of counterfactuals developed by Robert Stalnaker and David Lewis, the subjunctive conditional $A \to O_j$ (often written $A \square\!\!\to O_j$) is not a strict modal implication across all possible worlds, which would be far too strong to capture contingent causal laws. Rather, $A \to O_j$ is the proposition that *if $A$ were performed, $O_j$ would be the case* in the nearest possible world(s) where $A$ holds.

### Lewis's Triviality Result and the Gibbard–Harper Equivalence

Why can we not simply equate the probability of the conditional $P(A \to O_j)$ with the conditional probability $P(O_j \mid A)$? If $P(A \to O_j) = P(O_j \mid A)$ held universally, CDT and EDT would be mathematically identical. However, as noted in the reference article, David Lewis (1976) proved a celebrated **triviality result**: if a class of probability functions is closed under conditionalizing, there can be no connective $\to$ satisfying $P(A \to O_j) = P(O_j \mid A)$ across that class unless the probability functions are *trivial*—meaning they never assign positive probability to more than two incompatible alternatives, and hence are at most four-valued. In any realistic decision problem with three or more mutually exclusive possibilities, a counterfactual conditional proposition $A \to O_j$ cannot have its probability universally identified with $P(O_j \mid A)$.

Nevertheless, $P(A \to O_j)$ and $P(O_j \mid A)$ often coincide in everyday decision-making. The reference article notes that Gibbard and Harper proved that under two axioms—one related to the controversial **Principle of Conditional Excluded Middle (CEM)** (Shaffer 2009)—the statistical independence of the act $A$ and the counterfactual $A \to O_j$ suffices to guarantee $P(A \to O_j) = P(O_j \mid A)$. 

While the reference article states this theorem without giving the axioms or proof, we can reconstruct the formal derivation to see exactly how the machinery works:

1. **Axiom 1 (Conditional Excluded Middle and Non-Contradiction):** For any consistent action $A$ and outcome $O_j$, $(A \to O_j) \lor (A \to \neg O_j)$ is logically true, and $(A \to O_j) \land (A \to \neg O_j)$ is logically false.
2. **Axiom 2 (Modus Ponens / Centering):** If $A$ actually occurs, the counterfactual $A \to O_j$ has the same truth value as the material outcome $O_j$. Formally, $(A \land (A \to O_j)) \iff (A \land O_j)$.

**Proposition (Gibbard–Harper Equivalence):** *Under Axioms 1 and 2, for any action $A$ with $P(A) > 0$, $P(O_j \mid A) = P(A \to O_j \mid A)$. Consequently, if $A$ and $A \to O_j$ are statistically independent under $P$, then $P(A \to O_j) = P(O_j \mid A)$.*

*Proof (Author's Reconstruction):* By the definition of conditional probability and Axiom 2, we can substitute the conjunction $A \land (A \to O_j)$ for $A \land O_j$:

$$P(O_j \mid A) = \frac{P(A \land O_j)}{P(A)} = \frac{P(A \land (A \to O_j))}{P(A)} = P(A \to O_j \mid A).$$

By definition, $A$ and $A \to O_j$ are statistically independent if and only if $P(A \to O_j \mid A) = P(A \to O_j)$. Substituting this independence identity directly yields $P(O_j \mid A) = P(A \to O_j)$. $\blacksquare$

This derivation exposes the exact mathematical wedge between EDT and CDT: **EDT evaluates $A$ using the conditional distribution $P(A \to O_j \mid A)$, whereas CDT evaluates $A$ using the unconditional distribution $P(A \to O_j)$.** Whenever an agent believes that their choice of $A$ is diagnostically correlated with the truth of the causal counterfactual $A \to O_j$—that is, when $P(A \to O_j \mid A) \neq P(A \to O_j)$—EDT and CDT diverge.

---

## 2. Operationalizing the Counterfactual: Partitions, Imaging, and Interventions

A central criticism highlighted in the reference article (citing Shaffer 2009) is that Gibbard and Harper's formula is algorithmically vague: CDT does not by itself specify a unique mathematical procedure for computing $P(A \to O_j)$. Furthermore, Axiom 1 (CEM) fails when causal processes are genuinely indeterministic (e.g., tossing a quantum coin if $A$ is chosen). How, then, can a practitioner operationalize CDT so that it applies cleanly to both deterministic and stochastic problems?

Drawing on hints in the source text—specifically Lewis's (1981) *imaging* technique and Andy Egan's (2007) discussion of *dependency hypotheses*—and augmenting them with modern causal modeling, we can formulate three rigorous operational interpretations of CDT.

### 2.1. Partitioning via Dependency Hypotheses ($K$)

As the reference text notes in its discussion of Egan (2007), standard CDT operates by "holding fixed the agent's unconditional credences in dependency hypotheses." In David Lewis's (1981) formulation of CDT, a **dependency hypothesis** $K$ is a maximally specific proposition about how outcomes causally depend on the agent's actions—that is, a complete specification of all background causal factors that are outside the agent's present causal control.

Let $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$ be a finite partition of such dependency hypotheses. Because each $K \in \mathcal{K}$ holds fixed all common causes and background states, conditional on a specific $K$, the act $A$ has no purely diagnostic correlation with the causal structure; within $K$, conditioning on $A$ tracks purely causal consequences. We can therefore expand $P(A \to O_j)$ by marginalizing over the unconditional prior $P(K)$:

$$P(A \to O_j) = \sum_{K \in \mathcal{K}} P(K) P(O_j \mid A \land K).$$

Substituting this into the Gibbard–Harper utility equation yields the **K-partition formulation of CDT**:

$$U_{\text{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K) \sum_{j=1}^{n} P(O_j \mid A \land K) D(O_j).$$

Compare this with the expanded form of EDT over the same partition:

$$V_{\text{EDT}}(A) = \sum_{K \in \mathcal{K}} P(K \mid A) \sum_{j=1}^{n} P(O_j \mid A \land K) D(O_j).$$

This pair of equations makes the operational difference crystal clear. Both theories agree on what happens once the causal state of the world $K$ is fixed: both use $P(O_j \mid A \land K)$. However, EDT updates the probability of the background causal state from $P(K)$ to $P(K \mid A)$, allowing the choice of $A$ to serve as retroactive evidence about the state of the world. CDT forbids this update, holding $P(K)$ invariant across all actions $A$.

### 2.2. Lewisian Imaging and the Regress Problem

The reference text outlines a second operational approach proposed by Lewis (1981): **imaging**. Let $\mathcal{W}$ be a finite set of possible worlds equipped with a probability mass function $P: \mathcal{W} \to [0,1]$. Assume a Stalnaker selection function $f: \mathcal{W} \times \mathcal{A} \to \mathcal{W}$ that maps each world $w \in \mathcal{W}$ and possible action $A \in \mathcal{A}$ to the "closest" possible world $w_A = f(w, A)$ in which $A$ holds (with $f(w, A) = w$ whenever $w \in A$).

Whereas Bayesian conditioning on $A$ deletes all probability mass outside $A$ and renormalizes the remaining mass proportionally, *imaging on $A$* transfers the probability mass $P(w)$ of each world $w$ directly to its closest $A$-world $w_A$. Formally, the imaged probability distribution $P_A$ over $\mathcal{W}$ is defined by:

$$P_A(w') = \sum_{\substack{w \in \mathcal{W} \\ f(w, A) = w'}} P(w), \quad \text{and} \quad P(A \to O_j) = P_A(O_j) = \sum_{w' \in O_j} P_A(w').$$

Notice that imaging preserves total probability without renormalization: no probability mass is destroyed and redistributed to unrelated background states. 

However, as the reference text points out (citing Shaffer 2009), imaging faces a serious epistemic obstacle: specifying the selection function $f(w, A)$ requires knowing what would be true at $w_A$ if we were certain of $A$, which is itself a counterfactual conditional to which an uncertain agent might assign probability less than $1$, threatening an infinite regress.

### 2.3. An Operational Proposal: Structural Causal Models and the $\text{do}$-Operator

*Author's Operational Proposal:* To resolve Shaffer's regress and provide a fully algorithmic procedure for unfamiliar problems, we can ground both Lewis's imaging and the $K$-partition formula in the modern mathematics of **Structural Causal Models (SCMs)** and Judea Pearl's intervention calculus. 

Suppose we represent the decision problem as a Directed Acyclic Graph (DAG) over background exogenous variables $U$ (corresponding to dependency hypotheses $K$), endogenous pre-action variables $X$, the action variable $A$, and the outcome variable $O$. In an SCM, each variable is determined by a structural function of its graph parents and local noise. 

Performing action $A$ corresponds not to conditioning on $A$, but to applying the surgical intervention operator $\text{do}(A)$, which deletes all incoming arrows into $A$ (severing the diagnostic link between background causes $K$ and the choice $A$) and fixes $A$ to the chosen value. Under this operationalization, the counterfactual probability is identified with the interventional distribution:

$$P(A \to O_j) := P(O_j \mid \text{do}(A)) = \sum_{k} P(K = k) P(O_j \mid A, K = k),$$

where $K$ is any set of pre-action variables satisfying the **back-door criterion** (i.e., $K$ contains no causal descendants of $A$ and blocks all non-causal paths from $A$ to $O$). This resolves Shaffer's regress: the agent does not need an infinite hierarchy of nested beliefs over possible worlds; they only need a prior distribution over a finite family of causal graphs and structural parameters. If the causal mechanism itself is uncertain, $K$ simply indexes both the state of the background variables and the candidate causal models.

---

## 3. Canonical Applications: Confounding vs. Prediction

To see how this formalism operates in practice, let us work through two canonical classes of problems from the reference text: common-cause confounding and predictive correlation.

### 3.1. Common-Cause Confounding: King David and Bathsheba

Gibbard and Harper (1981) illustrate the divergence between EDT and CDT using the biblical story of King David and Bathsheba. As quoted in the reference article, David desires to summon Bathsheba ($S$) rather than abstain ($\neg S$), knowing that summoning another man's wife is an unjust act. From political science and psychology, David knows that kings have two fixed personality types determined by genetics and early childhood: charismatic ($C$) and uncharismatic ($\neg C$). Charismatic kings tend to act justly and rarely face successful revolts ($R$); uncharismatic kings tend to act unjustly and frequently face successful revolts—not because unjust acts *cause* revolts, but because uncharismatic kings have an ignoble bearing that provokes rebellion.

Let us parameterize this story to execute an explicit calculation. Suppose David's prior credence that he is charismatic is $P(C) = 0.5$ and $P(\neg C) = 0.5$. Let the utility of peace ($\neg R$) be $0$, the utility of a revolt ($R$) be $-100$, and the utility bonus of having Bathsheba ($S$) be $+10$:

| Action & Outcome | $(S, \neg R)$ | $(S, R)$ | $(\neg S, \neg R)$ | $(\neg S, R)$ |
| :--- | :---: | :---: | :---: | :---: |
| **Desirability $D(\cdot)$** | $+10$ | $-90$ | $0$ | $-100$ |

Because unjust acts do not causally provoke revolts, the probability of revolt depends exclusively on the dependency hypothesis $\{C, \neg C\}$:

$$P(R \mid S \land C) = P(R \mid \neg S \land C) = 0.10, \qquad P(R \mid S \land \neg C) = P(R \mid \neg S \land \neg C) = 0.80.$$

However, because charisma strongly influences whether a king acts justly, suppose $P(S \mid C) = 0.05$ and $P(S \mid \neg C) = 0.75$.

**The Evidential Calculation:** An EDT agent updates their belief about their personality type via Bayes' rule conditional on their choice:

$$P(C \mid S) = \frac{P(C)P(S \mid C)}{P(C)P(S \mid C) + P(\neg C)P(S \mid \neg C)} = \frac{0.5(0.05)}{0.5(0.05) + 0.5(0.75)} = 0.0625,$$

$$P(C \mid \neg S) = \frac{0.5(0.95)}{0.5(0.95) + 0.5(0.25)} \approx 0.7917.$$

Using these posterior weights, the evidential probability of revolt if David summons Bathsheba jumps to $P(R \mid S) = 0.0625(0.10) + 0.9375(0.80) = 0.75625$, whereas abstaining yields $P(R \mid \neg S) = 0.7917(0.10) + 0.2083(0.80) \approx 0.2458$. Consequently:

$$V_{\text{EDT}}(S) = 10 - 100(0.75625) = -65.625 < V_{\text{EDT}}(\neg S) = 0 - 100(0.2458) = -24.58.$$

EDT advises David to abstain—attempting to "manage the news" about his fixed genetic character by mimicking the behavior of a charismatic king.

**The Causal Calculation:** CDT recognizes that $\{C, \neg C\}$ is causally independent of $S$. Holding fixed the unconditional credences $P(C) = P(\neg C) = 0.5$:

$$P(S \to R) = P(\neg S \to R) = 0.5(0.10) + 0.5(0.80) = 0.45.$$

Thus, the causal expected utilities are:

$$U_{\text{CDT}}(S) = 10 - 100(0.45) = -35 > U_{\text{CDT}}(\neg S) = 0 - 100(0.45) = -45.$$

Because summoning Bathsheba adds $+10$ utility in every causal state without altering the probability of revolt, CDT recommends $S$. In medical and policy contexts (such as the famous smoking lesion problem), philosophers almost universally agree with CDT: refusing a beneficial action merely because it is correlated with an unchangeable genetic flaw is irrational self-deception.

### 3.2. Predictive Correlation: Newcomb's Paradox and the Twin Prisoner's Dilemma

The philosophical consensus splinters when we turn to **Newcomb's paradox** (Wolpert & Benford 2013; Ahmed 2021). An agent faces two boxes: a transparent Box A containing $\$1{,}000$, and an opaque Box B containing either $\$1{,}000{,}000$ or $\$0$. The agent may take only Box B ($A_1$, "one-boxing") or take both Box A and Box B ($A_2$, "two-boxing"). Yesterday, a predictor with $99\%$ accuracy predicted the agent's choice: if the predictor predicted $A_1$, she placed $\$1{,}000{,}000$ in Box B (state $K_1$); if she predicted $A_2$, she placed $\$0$ in Box B (state $K_2$).

Let utility be linear in dollars. The decision matrix is:

| Action \ Dependency Hypothesis | $K_1$ ($\$1\text{M}$ in Box B) | $K_2$ ($\$0$ in Box B) |
| :--- | :---: | :---: |
| **$A_1$ (One-box: Box B only)** | $\$1{,}000{,}000$ | $\$0$ |
| **$A_2$ (Two-box: Boxes A + B)** | $\$1{,}001{,}000$ | $\$1{,}000$ |

Because the predictor's action occurred in the past (and assuming no retrocausality), the contents of Box B are causally independent of the agent's present choice: $P(A_1 \to K_1) = P(A_2 \to K_1) = P(K_1)$. For *any* unconditional probability $p = P(K_1) \in [0, 1]$, CDT computes:

$$U_{\text{CDT}}(A_2) = p(1{,}001{,}000) + (1-p)(1{,}000) = 1{,}000{,}000p + 1{,}000 > U_{\text{CDT}}(A_1) = 1{,}000{,}000p.$$

Two-boxing strictly dominates one-boxing by $\$1{,}000$ in causal expectation. EDT, by contrast, uses $P(K_1 \mid A_1) = 0.99$ and $P(K_1 \mid A_2) = 0.01$, yielding $V_{\text{EDT}}(A_1) = \$990{,}000 \gg V_{\text{EDT}}(A_2) = \$11{,}000$. 

As Lewis (1979) proved, Newcomb's problem is structurally isomorphic to the **Twin Prisoner's Dilemma**, in which you play a one-shot Prisoner's Dilemma against a psychological twin whose choice to cooperate or defect correlates at $99\%$ with yours, despite causal isolation. Just as CDT mandates two-boxing in Newcomb's problem, it mandates defecting against your twin—leaving CDT agents systematically poorer than EDT agents whenever accurate predictors or correlated peers populate the environment.

---

## 4. Pathologies at the Frontier: Self-Location, Instability, and Money Extraction

While defenders of CDT often accept the "why ain'cha rich?" objection in Newcomb's paradox as the unavoidable price of respecting causal dominance in an environment that rewards irrational dispositions, recent literature cited in the reference article has uncovered much sharper counterexamples. These cases do not rely on dominance; instead, they exploit how CDT handles *state-action interaction* and *deliberative instability*.

### 4.1. State-Action Interaction: The Psychopath Button and Ratifiability

In King David and Newcomb's paradox, the utility function is *additive* in the state and action: $D(A, K) = f(A) + g(K)$. The causal effect of the action is identical across all dependency hypotheses. What happens when the causal effect of an action *reverses sign* depending on the background state $K$, and the action itself is strong evidence about which state obtains?

Consider Andy Egan's (2007) **Psychopath Button**, described in the reference text: Paul can press a "kill all psychopaths" button ($B$) or abstain ($\neg B$). Let $K_{\text{sane}}$ be the state in which Paul is not a psychopath, and $K_{\text{psych}}$ the state in which Paul is a psychopath. Paul strongly prefers a world without psychopaths ($+10$) to the status quo ($0$), but vastly prefers living in the status quo to dying ($-1{,}000$):

| Action \ State | $K_{\text{sane}}$ (Paul is sane) | $K_{\text{psych}}$ (Paul is a psychopath) |
| :--- | :---: | :---: |
| **$B$ (Press button)** | $+10$ | $-1{,}000$ |
| **$\neg B$ (Do not press)** | $0$ | $0$ |

Suppose Paul begins deliberation with a very low unconditional credence that he is a psychopath, say $P(K_{\text{psych}}) = 0.001$ and $P(K_{\text{sane}}) = 0.999$. However, Paul is also confident that almost only a psychopath would press a mass-execution button: $P(K_{\text{psych}} \mid B) = 0.99$.

If we apply naive CDT—holding fixed Paul's initial unconditional credence $P(K_{\text{psych}}) = 0.001$—we obtain:

$$U_{\text{CDT}}(B) = 0.999(10) + 0.001(-1{,}000) = 9.99 - 1.00 = +8.99 > U_{\text{CDT}}(\neg B) = 0.$$

Naive CDT instructs Paul to press the button, marching him straight into near-certain death! As Egan points out, virtually everyone agrees that pressing the button is irrational.

How can a causal decision theorist respond? The reference article notes James Joyce's (2012) defense: CDT is naturally capable of incorporating "information about what one is inclined or likely to do as evidence." Formally, Joyce distinguishes between *unconditional* CDT (which uses prior credences $P(K)$) and *deliberative* CDT, which requires that a rational choice be **ratifiable** (Harper 1984; Jeffrey 1983).

**Definition (Ratifiability):** An action $A^* \in \mathcal{A}$ is *ratifiable* if it maximizes causal expected utility when probabilities over dependency hypotheses $K$ are conditioned on the hypothesis that the agent has decided to perform $A^*$:

$$A^* \in \arg\max_{A \in \mathcal{A}} U_{\text{CDT}}(A \mid A^*), \quad \text{where } U_{\text{CDT}}(A \mid A^*) = \sum_{K \in \mathcal{K}} P(K \mid A^*) \sum_{j=1}^{n} P(O_j \mid A \land K) D(O_j).$$

Notice that $U_{\text{CDT}}(A \mid A^*)$ is *not* EDT: when comparing an alternative action $A$ against $A^*$, we hold the conditioning event $A^*$ fixed across all $A \in \mathcal{A}$. In the Psychopath Button, if Paul settles on pressing ($B$), his conditional credence updates to $P(K_{\text{psych}} \mid B) = 0.99$, so:

$$U_{\text{CDT}}(B \mid B) = 0.01(10) + 0.99(-1{,}000) = -989.90 < U_{\text{CDT}}(\neg B \mid B) = 0.$$

Thus, $B$ is unratifiable: the moment Paul forms the intention to press $B$, that very intention provides self-locating evidence that he is a psychopath, making $\neg B$ causally superior. Conversely, if Paul settles on $\neg B$, $P(K_{\text{psych}} \mid \neg B) \approx 0.0001$, so $U_{\text{CDT}}(B \mid \neg B) \approx +9.90 > U_{\text{CDT}}(\neg B \mid \neg B) = 0$, making $\neg B$ *also* unratifiable!

### 4.2. Deliberative Instability: Death in Damascus

This lack of any pure ratifiable option brings us directly to the classic **Death in Damascus** scenario (Gibbard & Harper 1981; Egan 2007). Death predicts whether you will be in Damascus ($A_D$) or Aleppo ($A_A$) tomorrow, and goes to wait for you there. Being where Death is results in death ($0$); being in the other city results in survival ($+100$). Assume Death's prediction ($K_D$ or $K_A$) is $99\%$ accurate.

| Action \ State | $K_D$ (Death in Damascus) | $K_A$ (Death in Aleppo) |
| :--- | :---: | :---: |
| **$A_D$ (Stay in Damascus)** | $0$ | $+100$ |
| **$A_A$ (Flee to Aleppo)** | $+100$ | $0$ |

Here, $U_{\text{CDT}}(A_D) = 100 P(K_A)$ and $U_{\text{CDT}}(A_A) = 100 P(K_D)$. Every inclination refutes itself: if you lean toward staying in Damascus, $P(K_D \mid A_D) = 0.99$, so CDT tells you to flee to Aleppo ($U_{\text{CDT}}(A_A \mid A_D) = 99 > 1$). Once you decide to flee to Aleppo, $P(K_A \mid A_A) = 0.99$, so CDT tells you to stay in Damascus. 

In game theory, this is recognized as a matching-pennies game played against a predictor of oneself. The only ratifiable state is a **Credal/Behavioral Fixed Point** (comparable to a Nash equilibrium) in which the agent's credences are $P(K_D) = P(K_A) = 0.5$, rendering $U_{\text{CDT}}(A_D) = U_{\text{CDT}}(A_A) = 50$.

### 4.3. Guaranteed Exploitation: The Adversarial Offer

Can ratifiability and mixed-strategy equilibria rescue CDT from all predictive counterexamples? Recent work by Jack Spencer (2020) and Caspar Oesterheld and Vincent Conitzer (2021)—highlighted in the reference article—proves that the answer is *no*. They construct scenarios where CDT forces an agent to accept a **sure loss in expectation** and forgo a guaranteed free option, even if the agent uses ratifiability or mixed strategies.

Consider Oesterheld and Conitzer's **Adversarial Offer** from the reference text:
* Two boxes, Box 1 and Box 2, are on offer for $\$1$ each.
* The buyer may choose $B_1$ (buy Box 1 for $\$1$), $B_2$ (buy Box 2 for $\$1$), or $N$ (buy neither for $\$0$).
* Yesterday, the seller predicted the buyer's choice $\hat{A} \in \{B_1, B_2, N\}$ with accuracy $0.75$, and placed $\$3$ in each box that she predicted the buyer **not** to acquire.

Let us construct the exact payoff matrix (net of the $\$1$ purchase price for $B_1$ and $B_2$) across the three dependency hypotheses $K_1 = (\hat{A} = B_1)$, $K_2 = (\hat{A} = B_2)$, and $K_N = (\hat{A} = N)$:

| Action \ Seller's Prediction | $K_1$ (Predicted $B_1$: Box 1 has $\$0$, Box 2 has $\$3$) | $K_2$ (Predicted $B_2$: Box 1 has $\$3$, Box 2 has $\$0$) | $K_N$ (Predicted $N$: Box 1 has $\$3$, Box 2 has $\$3$) |
| :--- | :---: | :---: | :---: |
| **$B_1$ (Buy Box 1 for $\$1$)** | $-\$1$ | $+\$2$ | $+\$2$ |
| **$B_2$ (Buy Box 2 for $\$1$)** | $+\$2$ | $-\$1$ | $+\$2$ |
| **$N$ (Buy neither for $\$0$)** | $\$0$ | $\$0$ | $\$0$ |

Let $p_1 = P(K_1)$, $p_2 = P(K_2)$, and $p_N = P(K_N)$ be *any* probability distribution over the dependency hypotheses (whether unconditional priors or posteriors updated during deliberation), with $p_1 + p_2 + p_N = 1$. Now compute the causal expected utilities of the three options:

$$U_{\text{CDT}}(B_1) = -1(p_1) + 2(p_2 + p_N) = -p_1 + 2(1 - p_1) = 2 - 3p_1,$$

$$U_{\text{CDT}}(B_2) = -1(p_2) + 2(p_1 + p_N) = -p_2 + 2(1 - p_2) = 2 - 3p_2,$$

$$U_{\text{CDT}}(N) = 0.$$

Now take the average of the causal expected utilities of buying Box 1 and buying Box 2:

$$\frac{1}{2} U_{\text{CDT}}(B_1) + \frac{1}{2} U_{\text{CDT}}(B_2) = 2 - \frac{3}{2}(p_1 + p_2).$$

Because $p_1 + p_2 = 1 - p_N \le 1$, it is a mathematical theorem that for **every possible probability distribution** $(p_1, p_2, p_N)$ in the simplex:

$$\frac{1}{2} U_{\text{CDT}}(B_1) + \frac{1}{2} U_{\text{CDT}}(B_2) \ge 2 - \frac{3}{2}(1) = +\$0.50 > U_{\text{CDT}}(N) = \$0.$$

Consequently, $\max\big(U_{\text{CDT}}(B_1), U_{\text{CDT}}(B_2)\big) \ge +\$0.50 > 0$ under *all* credences! Even if the agent updates on their own inclinations (Joyce's ratificationism), abstaining ($N$) is strictly inferior to at least one of the boxes, and randomizing $50/50$ between $B_1$ and $B_2$ has a causal expected value of at least $+\$0.50$. Thus, CDT **strictly forbids choosing $N$**.

Yet look at what actually happens when the CDT agent buys a box $B_i$: because the seller predicts the buyer's choice with probability $0.75$, the buyer receives $\$0 - \$1 = -\$1$ with probability $0.75$ and $\$3 - \$1 = +\$2$ with probability $0.25$, for an actual expected return of:

$$\mathbb{E}[\text{Payoff} \mid B_i] = 0.75(-1) + 0.25(+2) = -\$0.25 < \$0.$$

By holding fixed a single probability distribution $(p_1, p_2, p_N)$ across counterfactual evaluations of both $B_1$ and $B_2$, CDT relies on the fact that in every world, *at least one* box contains $\$3$. It therefore concludes that the average box is worth at least $\$1.50$ (net $+\$0.50$), remaining blind to the adversarial correlation that whichever box the agent *actually* reaches for is $75\%$ likely to be the empty one. Worse still, in sequential versions of such games, Oesterheld and Conitzer (2021) show that CDT agents are vulnerable to **diachronic Dutch books**—sequences of trades each of which CDT endorses as having positive causal expected value, but which together guarantee a deterministic financial loss.

---

## 5. A Practical Protocol for Unfamiliar Decision Problems

How should a mathematically literate decision-maker apply CDT to an unfamiliar problem while guarding against its known pathologies? Synthesizing the formal framework of the reference article with our operational extensions, we can formulate a four-step decision protocol:

### Step 1: Specify the Causal Structure and Partition $\mathcal{K}$
Decompose the decision problem into actions $\mathcal{A}$, outcomes $\mathcal{O}$ with utilities $D(O_j)$, and a partition of **dependency hypotheses** $\mathcal{K} = \{K_1, \dots, K_r\}$. 
* *Rule of construction:* A variable belongs in $K$ if and only if it is **causally independent** of the agent's present choice $A$ (i.e., it is determined prior to or outside the causal light-cone of $A$, blocking all back-door paths between $A$ and $O$). Do *not* include causal mediators (variables downstream of $A$) in $K$; mediators belong in the conditional outcome distribution $P(O_j \mid A \land K)$.

### Step 2: Check for Causal Dominance and Diagnostic Confounding
For each $K \in \mathcal{K}$, compute the state-specific expected utility:

$$u(A, K) = \sum_{j=1}^{n} P(O_j \mid A \land K) D(O_j).$$

* If an action $A^*$ satisfies $u(A^*, K) \ge u(A, K)$ for all $K \in \mathcal{K}$ (with strict inequality for at least one $K$ with $P(K) > 0$), then $A^*$ **causally dominates** all alternatives. In standard confounding cases (like King David or medical decisions with genetic confounders), stop here and select $A^*$.

### Step 3: Check for State-Action Interaction and Apply Ratification
If the ranking of actions reverses across different dependency hypotheses $K$ (as in the Psychopath Button or Death in Damascus) *and* the agent's choice $A$ is diagnostically correlated with $K$ ($P(K \mid A) \neq P(K)$), do not use naive prior credences $P(K)$. Instead, evaluate the **deliberative causal matrix**:

$$M(A, A') = U_{\text{CDT}}(A \mid A') = \sum_{K \in \mathcal{K}} P(K \mid A') u(A, K),$$

where $A'$ is the action the agent contemplates settling upon, and $A$ is any alternative deviation. Look for a **ratifiable pure action** $A^*$ satisfying $M(A^*, A^*) = \max_{A \in \mathcal{A}} M(A, A^*)$.

### Step 4: Guard Against Adversarial Extraction and Dutch Books
If no pure action is ratifiable (as in Death in Damascus), or if an adversary has structured the payoffs across multiple correlated options (as in the Adversarial Offer), check the **actual expected value** of any candidate strategy $\sigma$ (where $\sigma(A)$ is the probability of playing $A$):

$$V_{\text{actual}}(\sigma) = \sum_{A \in \mathcal{A}} \sigma(A) M(A, A).$$

If CDT recommends a mixed or pure strategy $\sigma$ whose actual expected payoff $V_{\text{actual}}(\sigma)$ is strictly less than a guaranteed status-quo baseline $N$ (where $u(N, K) = c$ is constant across all $K$), recognize that you are facing an **adversarial Newcomb-like extraction trap**. While orthodox CDT demands taking the gamble, a pragmatically rational agent who wishes to avoid Dutch-book exploitation must either pre-commit to abstaining ($N$) before the predictor acts, or adopt a policy-level (evidential/functional) decision rule when interacting with high-accuracy predictors.

---

## 6. Conclusion

Causal decision theory represents one of the great triumphs of twentieth-century formal philosophy and decision science. By replacing simple conditional probabilities $P(O_j \mid A)$ with counterfactual or interventional probabilities $P(A \to O_j)$, Gibbard, Harper, and Lewis rescued decision theory from superstitious self-signaling—explaining with mathematical precision why rational agents should act to change the future rather than to manage the news about the past. 

At the same time, the ongoing debates over Newcomb's paradox, the Psychopath Button, and the Adversarial Offer reveal that separating cause from evidence is subtler than early theorists imagined. When an agent's own deliberative process is embedded inside a world containing self-locating uncertainty or accurate predictors, holding fixed unconditional credences in dependency hypotheses can produce severe instabilities and exploitable losses. Understanding both the formal power of the $K$-partition calculus and the exact structural conditions under which it breaks down equips the modern researcher to navigate both everyday statistical confounding and the deepest paradoxes of rational agency.

---

## References

* Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
* Egan, A. (2007). "Some counterexamples to causal decision theory." *The Philosophical Review*, 116(1), 93–114.
* Gibbard, A., & Harper, W. L. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs: Conditionals, Belief, Decision, Chance, and Time* (pp. 153–190). D. Reidel.
* Greaves, H. (2013). "Epistemic decision theory." *Mind*, 122(488), 915–952.
* Harper, W. (1984). "Ratifiability and Causal Decision Theory: Comments on Eells and Seidenfeld." *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1984(2), 213–228.
* Howard, J. V. (1988). "Cooperation in the Prisoner's Dilemma." *Theory and Decision*, 24(3), 203–213.
* Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese*, 187(1), 123–145.
* Joyce, J. M. (2020). "Yet Another Refutation of Causal Decision Theory?" Working manuscript, University of Michigan.
* Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *The Philosophical Review*, 85(3), 297–315.
* Lewis, D. (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy*, 59(1), 5–30.
* Meacham, C. J. G. (2010). "Binding and its consequences." *Philosophical Studies*, 149(1), 49–71.
* Oesterheld, C., & Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *The Philosophical Quarterly*, 71(4), pqaa086.
* Shaffer, M. J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines*, 19(1), 61–92.
* Spencer, J. (2020). "An argument against causal decision theory." *Analysis*, 81(1), 52–61.
* Wedgwood, R. (2013). "Gandalf's solution to the Newcomb problem." *Synthese*, 190(14), 2643–2675.
* Weirich, P. (2016). "Causal Decision Theory." In E. N. Zalta (Ed.), *The Stanford Encyclopedia of Philosophy* (Winter 2016 ed.).
* Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese*, 190(9), 1637–1646.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Approach**

I'm currently focused on defining the appropriate scope and persona for this piece on Causal Decision Theory. I need to nail down the target audience and level of technical detail. I'm exploring different approaches to ensure clarity and relevance to an expert audience in decision theory. I'm trying to decide the best way to structure the explanation of CDT.


**Refining the Audience**

I've established the persona of a researcher writing a technical essay, aiming for a mathematically literate audience interested in both formal procedures and the philosophical underpinnings of Causal Decision Theory. My primary goal is to produce a rigorous, operational account suitable for real-world decision-making and this will form the core of my analysis.


**Analyzing the Source Text**

I'm now carefully analyzing the source, contrasting Causal and Evidential Decision Theory. I'm focusing on the uncertainties and open questions it raises. My plan is to develop operational interpretations for these, specifically those regarding counterfactual probabilities, and to distinguish explicitly the source's claims from my own. I aim for a mathematical essay format, targeting around 2,600-2,800 words, and will avoid unnecessary repetition. I will end with a brief conclusion.


**Clarifying the Formula**

I'm now diving deeper into the formal definition of Causal Decision Theory. I'm focusing on the formula: U(A) = Σj P(A → Oj) D(Oj). I'm carefully unpacking the counterfactual probability P(A → Oj) and its relation to conditional probability P(Oj | A), following Lewis's distinction. I need to make sure I grasp the independence condition and its implications.


**Exploring Independence**

I'm currently focused on the implications of Conditional Excluded Middle and statistical independence in Causal Decision Theory. I now believe that, under these conditions, P(A → Oj) equals P(Oj | A). I'm looking at King David and Bathsheba. Charismatic kings, genetically fixed, rarely revolt, even when acting unjustly. Uncharismatic ones are more prone to revolt due to their personality, but EDT abstains (summoning her is evidence of being uncharismatic). CDT, conversely, instructs to summon her. I have started a thought experiment on Newcomb's paradox.


**Evaluating the Counterarguments**

I am now closely examining criticisms of Causal Decision Theory, specifically focusing on counterexamples. I'm unpacking the implications of imaging, noting the potential for regress, and Egan's concept of fixed unconditional credences in dependency hypotheses. I'm carefully analyzing the "Death in Damascus" and "Adversarial Offer" scenarios, to understand CDT's challenges with instability and correlation. I'm exploring how these counterexamples expose the vulnerabilities of the theory.


**Analyzing the Paradox**

I'm now carefully examining the Psychopath Button thought experiment. I see the tension between CDT's endorsement of pressing the button, given fixed initial beliefs, and our intuitions. I'm exploring Joyce's defense of ratifiability within CDT, as a crucial element in resolving the paradox. I'm focusing on how the theory accounts for self-locating evidence during deliberation. I see this as a key point in addressing the counterarguments.

**Structuring the Essay**

I'm currently structuring the essay, starting with an introduction that presents the problem of how standard decision theory blurs the roles of action. I will frame this as the difference between an action being a symptom of background states (evidence) and as an intervention in the world (cause). The title should be a rigorous mathematical essay, perhaps *Counterfactuals, Interventions, and Rational Choice: A Mathematical Guide to Causal Decision Theory*.


**Presenting the Contrast**

I'm now introducing the contrast between Evidential and Causal Decision Theories. I'll start with the intuitive apple/orange scenario from the source, and then move to common-cause confounding. My focus is on formally presenting the Gibbard-Harper equation, $U(A) = \sum_j P(A \to O_j) D(O_j)$, and contrasting it with EDT's Jeffrey conditionalization formula. I'll be discussing Lewis's Triviality Result to explain why P(A → Oj) cannot be P(Oj | A) in non-trivial cases, and will reconstruct Gibbard-Harper's two axioms.


**Deriving the Independence Result**

I'm now working to mathematically demonstrate how statistical independence allows us to derive P(A → Oj) = P(Oj | A). I'll provide an explicit algebraic derivation within the essay, while also noting that the source text mentions the axioms and the final result.



**Connecting the Formulas**

I'm now linking Lewisian imaging and Structural Causal Models (SCMs). I'll formulate imaging mathematically using a selection function, demonstrating how it avoids conditioning on an action. I plan to operationalize the regress worry by fixing a structural causal model. I'm focusing on connecting P(A → Oj) to P(Oj | do(A)) via the back-door adjustment formula, providing a concrete, modern algorithmic tool to solve unfamiliar problems, along with canonical application scenarios.


**Illustrating the Machinery**

I'm now detailing applications for the formal apparatus, building on established scenarios. I'm focusing on two key cases: Diagnostic Confounding (King David) and Predictive Correlation (Newcomb's Problem). I'll provide illustrative probabilities, utilities, and calculations side-by-side for both EDT and CDT, and will formalize the predictive power in Newcomb's problem, relating it to the Twin Prisoner's Dilemma. I will also be analyzing the three major classes of counterexamples raised in the source: State-Action Feedback and Self-Locating Belief (*The Psychopath Button*).


**Examining the Counterexamples**

I am now focusing on the three main classes of counterexamples. I'm exploring *The Psychopath Button* and Joyce's ratificationist defense, showing how the calculation is modified with deliberative inclinations. I'm formalizing *Death in Damascus* to illustrate the fixed-point problem of non-ratifiable pure strategies. Finally, I'm working through *The Adversarial Offer*, doing a rigorous mathematical breakdown of the states and showing CDT's guarantee of linearity of expectation.


**Synthesizing a Protocol**

I'm now focused on drafting the content, doing word counts for sections. I'm developing a step-by-step mathematical procedure practitioners can use to solve any novel decision problem, including ratification checks. I've begun to construct a concise list of references for the conclusion. I am also checking the math for the equivalence proof, and planning on integrating both into the current writing.


**Deriving the Equivalence**

I'm now deriving the equivalence between the counterfactual and conditional probabilities, explicitly proving $P(A \to O_j) = P(O_j \mid A)$. I've reconstructed a full proof, using Axiom 1 (Conditional Excluded Middle), Axiom 2 (Modus Ponens), and the definition of conditional probability. I'm focusing on the logical steps to establish this relationship rigorously.


**Formalizing the Proof**

I'm now putting the finishing touches on the equivalence proof, explicitly showing that, if the action and the counterfactual are statistically independent, then the counterfactual and conditional probabilities are equal. Specifically, I've confirmed that the implications of conditional excluded middle and modus ponens, in conjunction with the definition of conditional probability, lead to a clean demonstration. I also have the King David and Bathsheba scenario and related utility functions, probabilities and equations set up.


**Calculating the Values**

I'm now calculating the expected utilities in the King David scenario, using both Evidential and Causal Decision Theory. I'm crunching the numbers with the explicit probabilities and utility functions to compare the two approaches. I'm confirming that EDT leads to abstaining, while CDT recommends action, based on the specific parameters. I'll include the explicit formulas in the final draft.


**Calculating the Psychopath Button**

I'm now calculating the values for the Psychopath Button scenario to understand its specific dynamics. I'm focusing on incorporating prior credences regarding Paul's psychopathy, and how this impacts the expected utilities of pressing the button versus not pressing it. I am planning to relate this calculation to the broader framework.


**Analyzing the Calculation**

I'm now carefully analyzing the calculations for the Psychopath Button scenario, paying attention to the state-action interaction and the non-additivity it creates. I'm focusing on why naive Causal Decision Theory recommends pressing the button and how to use Joyce's ratificationist approach. I will relate this to the broader theory.



**Calculating the Utilities**

I'm now calculating the causal expected utilities for each box in this modified Newcomb scenario. I'm focusing on the probabilistic setup, defining the key variables, including the buyer's action, the seller's prediction and the box contents. My next step will involve setting up and interpreting the utility functions, to understand how CDT would evaluate this variation.


**Calculating the Payoffs**

I'm now calculating payoffs in the Newcomb-like scenario, and it has some surprising implications. Regardless of how I set up the unconditional probabilities, CDT *strictly forbids* choosing 'No Box'. The buyer is always worse off with an explicit calculation. I am now working through the implications, and figuring out how to reconcile the theory with this surprising calculation.


**Calculating the Payoffs**

I've been crunching the numbers for those Newcomb-like payoffs, and the results are not what I expected! Causal Decision Theory actually *forbids* choosing 'No Box', regardless of the initial probabilities. I need to figure out what this unexpected result means, and how to reconcile it with the theory. This will be the focus of my next iteration.


```
