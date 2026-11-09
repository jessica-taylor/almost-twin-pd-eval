# 005_cdt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00019

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5936bdd7-75cc-422a-bf5d-4e9255688041/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5936bdd7-75cc-422a-bf5d-4e9255688041/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Interventions, Counterfactuals, and Rational Choice: A Mathematical Guide to Causal Decision Theory

When a rational agent stands at a decision node, what makes one action better than another? At first glance, the answer seems obvious: a rational agent should choose the action that yields the highest expected utility. Yet as soon as we formalize what "expected utility" means in environments where an agent’s choices correlate with external states of the world, probability theory splits into two distinct paradigms.

One paradigm—**Evidential Decision Theory (EDT)**—treats decision-making as an exercise in Bayesian updating. Under EDT, as characterized by Arif Ahmed (2021), an agent evaluates an action $A$ by asking how welcome the "news" would be if one learned that $A$ had been performed. The second paradigm—**Causal Decision Theory (CDT)**—insists that rational choice is about *intervention* rather than *observation*. Rather than asking what an action is evidence for, CDT asks what an action *causes* to happen in expectation.

This essay provides a mathematical account of Causal Decision Theory, tracing its formal mechanics from the foundational counterfactual equations of Allan Gibbard and William Harper (1981) and David Lewis (1981) to modern game-theoretic critiques involving instability and money extraction (Egan 2007; Oesterheld & Conitzer 2021). Along the way, where the core philosophical literature leaves operational questions open, we will construct explicit mathematical procedures that allow a practitioner to analyze and resolve unfamiliar decision problems.

---

## 1. Informal Foundations: From Apples to Expected Causal Effects

At an intuitive level, CDT advises an agent to select the action with the best expected causal consequences. The reference literature illustrates this with a simple deterministic choice: if eating an apple will cause you to be happy and eating an orange will cause you to be sad, rationality requires eating the apple.

Real decision problems, however, rarely offer known deterministic mappings from actions to outcomes. Suppose instead that eating a *good* apple causes happiness, eating a *bad* apple causes sadness, and you are uncertain whether the apple in front of you is good or bad. Because the causal effect of eating the apple depends on an unknown state of the world, you cannot rely on known causal consequences. Instead, you must calculate *expected* causal effects, which depend on three quantities:
1. Your credence (subjective probability) that the apple is good versus bad;
2. The quantitative desirability (utility) of the happiness caused by eating a good apple; and
3. The negative desirability of the sadness caused by eating a bad apple.

As long as the state of the apple (good or bad) is statistically independent of your decision to eat it, every standard theory of rationality agrees on the calculation. The mathematical divergence between causal and evidential reasoning emerges only when your choice of action is *statistically correlated* with the underlying state of the world despite having no causal influence over it.

---

## 2. The Formal Architecture of CDT and EDT

To make this divergence precise, let $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be a finite set of mutually exclusive actions available to an agent, and let $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ be a finite partition of possible outcomes. Each outcome $O_j$ is assigned a real-valued desirability (or utility) $D(O_j) \in \mathbb{R}$.

### The Gibbard–Harper Counterfactual Formulation

In their landmark 1981 paper, Allan Gibbard and William Harper formalized Causal Decision Theory as the maximization of causal expected utility $U(A)$, calculated from the probabilities of counterfactual conditionals:

$$U(A) = \sum_{j=1}^{m} P(A \to O_j) D(O_j)$$

Here, $A \to O_j$ denotes the subjunctive or counterfactual conditional proposition: *"If the agent were to perform action $A$, then outcome $O_j$ would occur"* (referred to in the reference text as the counterfactual proposition that $A$ necessarily implies $O_j$ under the relevant causal laws). The term $P(A \to O_j)$ is the agent's subjective probability that this counterfactual conditional holds true.

By contrast, Evidential Decision Theory evaluates an action $A$ using standard conditional probabilities $P(O_j \mid A) = \frac{P(A \wedge O_j)}{P(A)}$, maximizing evidential expected utility $V(A)$:

$$V(A) = \sum_{j=1}^{m} P(O_j \mid A) D(O_j)$$

### Lewis's Triviality Result

If the probability of the counterfactual conditional $P(A \to O_j)$ were always identical to the conditional probability $P(O_j \mid A)$, CDT and EDT would be mathematically equivalent. However, David Lewis (1976) proved a foundational impossibility theorem—known as **Lewis's triviality result**—showing that $P(A \to O_j)$ cannot in general equal $P(O_j \mid A)$.

Specifically, as noted in the source material, Lewis proved that if a class of probability functions is closed under conditionalizing, there can be no probability conditional $\to$ satisfying $P(A \to B) = P(B \mid A)$ across that class unless the class consists entirely of *trivial* probability functions—defined as probability functions that never assign positive probability to more than two incompatible alternatives (and are therefore at most four-valued). In any realistic decision space with three or more mutually exclusive possibilities, a counterfactual conditional proposition $A \to O_j$ must be a distinct mathematical object from the conditional probability $P(O_j \mid A)$.

### The Gibbard–Harper Equivalence Theorem

When *do* the two theories agree? The source notes that Gibbard and Harper proved that under two axioms—one related to the **Principle of the Conditional Excluded Middle (CEM)** (Shaffer 2009)—the statistical independence of the act $A$ and the counterfactual $A \to O_j$ suffices to guarantee $P(A \to O_j) = P(O_j \mid A)$.

To see exactly how this works in practice, let us state a formal reconstruction of the two axioms and the resulting proof (extending the brief summary in the source to make the algebraic mechanics explicit):

1. **Axiom 1 (Conditional Excluded Middle and Consistency)**: For any possible action $A$ and outcome $O_j$, either $(A \to O_j)$ or $(A \to \neg O_j)$ holds at every possible world, and they cannot both hold. Consequently, $\neg(A \to O_j) \equiv (A \to \neg O_j)$, ensuring that across a mutually exclusive and exhaustive partition of outcomes $\{O_1, \dots, O_m\}$, the counterfactual propositions $\{A \to O_1, \dots, A \to O_m\}$ form a partition of the probability space with $\sum_j P(A \to O_j) = 1$.
2. **Axiom 2 (Centering / Counterfactual Modus Ponens)**: In any world where action $A$ is actually performed, the counterfactual $A \to O_j$ has the same truth value as the outcome $O_j$ itself. That is, the conjunction $A \wedge (A \to O_j)$ is logically equivalent to $A \wedge O_j$.

**Proof of Equivalence under Independence:**
Assume $P(A) > 0$. By the definition of conditional probability and Axiom 2, we have:

$$P(O_j \mid A) = \frac{P(A \wedge O_j)}{P(A)} = \frac{P(A \wedge (A \to O_j))}{P(A)} = P(A \to O_j \mid A)$$

Now suppose that the performance of action $A$ is statistically independent of the counterfactual proposition $A \to O_j$, meaning $P(A \wedge (A \to O_j)) = P(A) P(A \to O_j)$, or equivalently $P(A \to O_j \mid A) = P(A \to O_j)$. Substituting this into the equation above immediately yields:

$$P(O_j \mid A) = P(A \to O_j)$$

This derivation reveals the precise mathematical locus of disagreement between CDT and EDT. Whenever an agent's choice of $A$ provides zero statistical information about which counterfactual mapping $A \to O_j$ is true of the world, CDT and EDT issue identical prescriptions. They diverge *if and only if* $P(A \to O_j \mid A) \neq P(A \to O_j)$—that is, when the act $A$ is diagnostically correlated with the causal structure of the environment.

---

## 3. Operationalizing Counterfactuals: Imaging and Dependency Hypotheses

As Michael Shaffer (2009) observes in the criticism section of the reference article, Gibbard and Harper's formula suffers from a potential operational vagueness: CDT does not by itself specify a unique algorithm for computing the counterfactual probabilities $P(A \to O_j)$.

### Lewis's Imaging and Shaffer's Regress

One formal algorithm proposed in the literature is David Lewis's (1981) method of **imaging**. Let $\mathcal{W}$ be a set of possible worlds equipped with a prior probability distribution $P(w)$ for $w \in \mathcal{W}$. Suppose that for each world $w$ and each possible action $A$, there is a uniquely closest possible world $w_A \in \mathcal{W}$ in which $A$ holds (this uniqueness corresponds directly to the Conditional Excluded Middle).

To evaluate $P(A \to O_j)$ via imaging, one shifts the probability mass $P(w)$ of each world $w$ directly onto its closest $A$-world $w_A$. Denoting the imaged probability distribution under action $A$ as $P^A$, the probability of any world $w'$ after imaging on $A$ is:

$$P^A(w') = \sum_{\{w \in \mathcal{W} \mid w_A = w'\}} P(w)$$

The counterfactual probability is then simply the total imaged probability of worlds where $O_j$ holds:

$$P(A \to O_j) = \sum_{w' \in O_j} P^A(w') = \sum_{w \in \mathcal{W}} P(w) \mathbb{I}(w_A \in O_j)$$

where $\mathbb{I}(\cdot)$ is the indicator function. Unlike Bayesian conditionalization—which deletes all worlds where $\neg A$ holds and renormalizes the remaining probability mass proportionally—imaging *preserves* the probability mass of $\neg A$-worlds by migrating it across the similarity metric to the nearest $A$-worlds.

However, the source highlights Shaffer's (2009) objection to this procedure: determining the similarity mapping $w \mapsto w_A$ requires knowing what would be the case (or what we would believe) if we were certain of $A$. Because that specification is itself a conditional to which an uncertain agent might assign a probability strictly less than $1$, attempting to compute $P(A \to O_j)$ purely from primitive world-similarity threatens an epistemic regress.

### An Operational Resolution: Partitioning into Dependency Hypotheses

How can an applied decision theorist avoid Shaffer's regress and calculate $U(A)$ in unfamiliar problems? The reference article points toward the operational solution when discussing Andy Egan's (2007) analysis of CDT: in practice, CDT operates by *"holding fixed the agent's unconditional credences in dependency hypotheses."*

Let us formalize this operational interpretation (distinguishing our explicit mathematical construction from the brief mention in the source). A **dependency hypothesis** (or causal state) $S_k$ is a maximally specific proposition about how the outcomes $\mathcal{O}$ causally depend on the agent's actions $\mathcal{A}$. Mathematically, with $n = |\mathcal{A}|$ actions and $m = |\mathcal{O}|$ outcomes, there are at most $m^n$ deterministic functions $f_k : \mathcal{A} \to \mathcal{O}$ mapping each action $A$ to a unique outcome $f_k(A) \in \mathcal{O}$. Each dependency hypothesis $S_k$ corresponds to the conjunction of counterfactuals:

$$S_k \equiv \bigwedge_{i=1}^{n} \left(A_i \to f_k(A_i)\right)$$

Because the set of dependency hypotheses $\mathcal{S} = \{S_1, S_2, \dots, S_K\}$ forms a mutually exclusive and exhaustive partition of the causal possibilities, the proposition $(A \to O_j)$ is simply the union of all dependency hypotheses $S_k$ that map action $A$ to outcome $O_j$:

$$P(A \to O_j) = \sum_{k : f_k(A) = O_j} P(S_k)$$

Substituting this into the Gibbard–Harper equation yields the **partition form of Causal Decision Theory**:

$$U(A) = \sum_{k=1}^{K} P(S_k) \sum_{j=1}^{m} P(O_j \mid A \wedge S_k) D(O_j)$$

where $P(O_j \mid A \wedge S_k) \in \{0, 1\}$ for deterministic dependency hypotheses, or $P(O_j \mid A \wedge S_k) \in [0, 1]$ if $S_k$ specifies fixed objective chances (stochastic causal mechanisms) for each outcome given $A$.

Notice why this resolves the operational difficulty in standard applications: instead of defining an abstract similarity metric over all possible worlds, a modeller only needs to:
1. Identify the causally exogenous variables $S_k$ (states of nature whose causal influence on $\mathcal{O}$ is invariant to the agent's choice of $A$);
2. Assign unconditional prior probabilities $P(S_k)$ to those states; and
3. Specify the forward causal law $P(O_j \mid A \wedge S_k)$ within each state.

Compare the partition formula for CDT against the partition expansion of EDT:

$$V(A) = \sum_{k=1}^{K} P(S_k \mid A) \sum_{j=1}^{m} P(O_j \mid A \wedge S_k) D(O_j)$$

The entire mathematical difference between CDT and EDT reduces to a single term: **CDT weights each causal mechanism $S_k$ by its unconditional probability $P(S_k)$, whereas EDT weights $S_k$ by the conditional probability $P(S_k \mid A)$.**

---

## 4. Canonical Applications: Confounders and Predictors

With this operational apparatus in hand, we can analyze the classic decision problems from the reference text and see precisely how CDT processes non-causal correlations.

### Case 1: Common-Cause Confounding (King David and Bathsheba)

Gibbard and Harper (1981) illustrate the failure of EDT under common-cause confounding with the story of King David and Bathsheba. As described in the source:
* David must choose between summoning Bathsheba ($A_S$) and abstaining ($A_N$).
* There are two background personality types (dependency hypotheses): charismatic ($S_C$) and uncharismatic ($S_{\neg C}$), fixed by genetics and early childhood.
* Charismatic kings rarely face successful revolts ($O_R$) and tend to act justly ($A_N$). Uncharismatic kings frequently face successful revolts ($O_R$) because of their sneaky, ignoble bearing, and they also tend to perform unjust acts like summoning another man's wife ($A_S$).
* Crucially, unjust acts themselves have **zero causal effect** on whether a revolt occurs; the probability of revolt depends solely on whether David is charismatic ($S_C$) or uncharismatic ($S_{\neg C}$).

To demonstrate the mathematical mechanics, let us assign illustrative numerical parameters to Gibbard and Harper's narrative (noting that these specific numbers are our own parameterization of the source's qualitative setup). Suppose David's prior credence that he is charismatic is $P(S_C) = 0.5$ and $P(S_{\neg C}) = 0.5$. Suppose the probability of revolt $O_R$ given charisma is $0.1$, regardless of his action, and the probability of revolt given lack of charisma is $0.8$, regardless of his action:

$$P(O_R \mid A_S \wedge S_C) = P(O_R \mid A_N \wedge S_C) = 0.1$$

$$P(O_R \mid A_S \wedge S_{\neg C}) = P(O_R \mid A_N \wedge S_{\neg C}) = 0.8$$

Suppose further that charismatic kings summon Bathsheba with probability $0.1$, whereas uncharismatic kings summon her with probability $0.9$. Let the utility of summoning Bathsheba be $+10$ (and $0$ for abstaining), while a successful revolt imposes a utility penalty of $-50$ (additive with the benefit of Bathsheba).

**CDT Evaluation:**
Holding fixed the unconditional credences $P(S_C) = 0.5$ and $P(S_{\neg C}) = 0.5$, the counterfactual probability of revolt under either action is:

$$P(A_S \to O_R) = P(A_N \to O_R) = 0.5(0.1) + 0.5(0.8) = 0.45$$

Therefore, the causal expected utilities are:

$$U(A_S) = 10 - 50 \cdot P(A_S \to O_R) = 10 - 50(0.45) = -12.5$$

$$U(A_N) = 0 - 50 \cdot P(A_N \to O_R) = 0 - 50(0.45) = -22.5$$

Since $U(A_S) - U(A_N) = +10 > 0$, **CDT recommends summoning Bathsheba ($A_S$)**. Because David's charisma is already fixed in the past, abstaining cannot make him charismatic; summoning her strictly dominates abstaining by $+10$ utils in every causal state.

**EDT Evaluation:**
By Bayes' rule, conditional on summoning Bathsheba ($A_S$), David's updated probability that he is uncharismatic jumps to:

$$P(S_{\neg C} \mid A_S) = \frac{0.5 \times 0.9}{0.5 \times 0.9 + 0.5 \times 0.1} = 0.9$$

Conditional on abstaining ($A_N$), by symmetry, $P(S_{\neg C} \mid A_N) = 0.1$. Consequently, the evidential probability of revolt given $A_S$ is $P(O_R \mid A_S) = 0.1(0.1) + 0.9(0.8) = 0.73$, whereas $P(O_R \mid A_N) = 0.9(0.1) + 0.1(0.8) = 0.17$. The evidential utilities are:

$$V(A_S) = 10 - 50(0.73) = -26.5, \quad V(A_N) = 0 - 50(0.17) = -8.5$$

Thus **EDT recommends abstaining ($A_N$)**—attempting to manage the *news* about his childhood personality by avoiding symptomatic actions. As the source notes, cases like King David explain why philosophers predominantly prefer CDT over EDT when forced to choose between the two (Weirich 2016).

### Case 2: Predictive Correlation (Newcomb's Paradox and the Twin Prisoner's Dilemma)

While CDT's triumph in the Bathsheba problem is widely accepted, the exact same mathematical rule generates fierce controversy in **Newcomb's paradox** (Wolpert & Benford 2013; Gibbard & Harper 1981).

As specified in the reference article:
* A player chooses between taking only Box B (**One-Boxing**, $A_1$) or taking both Box A and Box B (**Two-Boxing**, $A_2$).
* Box A is transparent and always contains $\$1,000$.
* Box B is opaque. Yesterday, a predictor with $99\%$ accuracy predicted the player's choice. If the predictor predicted $A_1$, Box B contains $\$1,000,000$ (dependency hypothesis $S_1$). If the predictor predicted $A_2$, Box B contains $\$0$ (dependency hypothesis $S_2$).

Assuming linear utility in dollars, the payoff matrix is:

| Action \ Causal State | $S_1$ (Predicted $A_1$: $\$1\text{M}$ in B) | $S_2$ (Predicted $A_2$: $\$0$ in B) |
| :--- | :---: | :---: |
| **$A_1$ (Take Box B only)** | $\$1,000,000$ | $\$0$ |
| **$A_2$ (Take Boxes A and B)** | $\$1,001,000$ | $\$1,000$ |

Let $p = P(S_1)$ be the agent's unconditional credence that the predictor placed $\$1,000,000$ in Box B yesterday, so $1 - p = P(S_2)$. Because the prediction was locked in prior to the decision, the contents of Box B are causally independent of the agent's present action: $P(A_1 \to S_1) = P(A_2 \to S_1) = p$.

Applying the CDT formula:

$$U(A_1) = p(\$1,000,000) + (1 - p)(\$0) = \$1,000,000p$$

$$U(A_2) = p(\$1,001,000) + (1 - p)(\$1,000) = \$1,000,000p + \$1,000$$

For *every* prior probability $p \in [0, 1]$, we have $U(A_2) - U(A_1) = \$1,000 > 0$. Thus, **CDT unconditionally recommends Two-Boxing ($A_2$)**.

By contrast, because the predictor is $99\%$ accurate, $P(S_1 \mid A_1) = 0.99$ and $P(S_1 \mid A_2) = 0.01$. EDT computes:

$$V(A_1) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$

$$V(A_2) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$

and therefore **EDT recommends One-Boxing ($A_1$)**.

As David Lewis (1979) and J. V. Howard (1988) showed, this exact structure carries over to the **Prisoner's Dilemma against a psychological twin**. If your twin's decision to cooperate ($S_C$) or defect ($S_D$) is causally independent of your own choice, yet strongly correlated with it because of shared psychology, the game is mathematically isomorphic to Newcomb's problem: defecting causally dominates cooperating by saving a fixed cost regardless of $P(S_C)$, so CDT mandates defection while EDT endorses cooperation whenever the correlation is sufficiently high.

---

## 5. Pathologies at the Frontier: Act-State Dependence, Instability, and Money Extraction

If Newcomb's problem merely pitted causal dominance against high evidential payoffs, defenders of CDT could simply embrace Two-Boxing ("why leave $\$1,000$ on the table when the money in Box B is already fixed?"). However, a wave of modern counterexamples cited in the reference article demonstrates that holding unconditional credences in dependency hypotheses fixed can lead to catastrophic or self-defeating decisions.

### 1. Act-Diagnostic Causal Mechanisms: The Psychopath Button

Andy Egan (2007) argues that CDT fails whenever an agent's choice provides diagnostic evidence about *which causal mechanism connects their action to the outcome*. Consider Egan's **Psychopath Button** (also analyzed by Greaves 2013):
* Paul can either press the "kill all psychopaths" button ($A_P$) or abstain ($A_N$).
* Paul prefers living in a world without psychopaths to living in a world with psychopaths, and strongly prefers living in a world with psychopaths to dying.
* However, Paul is confident that *only a psychopath would press such a button*.

Let us formalize this decision problem (supplying illustrative utilities and credences that preserve Egan's exact qualitative structure). There are two causal dependency hypotheses:
* $S_{\neg \Psi}$ (**Paul is not a psychopath**): Pressing the button ($A_P$) kills all psychopaths and leaves Paul alive in a psychopath-free world ($D = +10$). Abstaining ($A_N$) leaves the status quo intact ($D = 0$).
* $S_{\Psi}$ (**Paul is a psychopath**): Pressing the button ($A_P$) causes Paul's own immediate death ($D = -100$). Abstaining ($A_N$) leaves the status quo intact ($D = 0$).

Notice that unlike Newcomb's problem—where the action $A_2$ adds $+\$1,000$ in *both* states—here the causal effect of pressing the button reverses sign across states: it is $+10$ in $S_{\neg \Psi}$ and $-100$ in $S_{\Psi}$.

Suppose that before deliberating, Paul's unconditional prior credence that he is a psychopath is very low, say $P(S_{\Psi}) = 0.01$ and $P(S_{\neg \Psi}) = 0.99$, because he expects that he will abstain. However, conditional on pressing the button, his credence that he is a psychopath is $P(S_{\Psi} \mid A_P) = 0.95$.

If Paul applies standard CDT by holding fixed his initial unconditional credences $P(S_{\neg \Psi}) = 0.99$ and $P(S_{\Psi}) = 0.01$, he calculates:

$$U(A_P) = P(S_{\neg \Psi})(10) + P(S_{\Psi})(-100) = 0.99(10) + 0.01(-100) = +8.9 > U(A_N) = 0$$

Thus, naive CDT recommends pressing the button—even though Paul believes with $95\%$ probability that pressing it will cause his own death! As Egan emphasizes, this exposes a gap between the intuitive causal rule ("do what you expect will bring about the best results") and the mechanical algorithm of evaluating actions using fixed prior credences over dependency hypotheses.

### 2. Decision Instability: Death in Damascus

A second pathology arises in **Death in Damascus** (Gibbard & Harper 1981; Harper 1984; Egan 2007; Meacham 2010). Death predicts whether you will be in Damascus ($A_D$) or flee to Aleppo ($A_A$) tomorrow, and goes to wait for you where he predicts you will be. Suppose Death is a $99\%$ accurate predictor, survival has utility $10$, and meeting Death has utility $0$ (with no travel cost).
* If you currently plan to stay in Damascus ($A_D$), you should believe with probability $0.99$ that Death is waiting in Damascus ($S_D$). Holding $P(S_D) = 0.99$ fixed, CDT computes $U(A_A) = 0.99(10) = 9.9 > U(A_D) = 0.01(10) = 0.1$, telling you to switch to Aleppo ($A_A$).
* Yet the moment you decide to go to Aleppo ($A_A$), your belief about Death's location updates to $P(S_A) = 0.99$, at which point CDT computes $U(A_D) = 9.9 > U(A_A) = 0.1$, telling you to switch back to Damascus ($A_D$).

Every pure action is self-undermining: deciding on an action immediately makes the alternative action strictly superior according to CDT.

### 3. Guaranteed Losses and Money Extraction: The Adversarial Offer

While Death in Damascus involves an symmetric loop where the agent cannot settle on a choice, recent results by Jack Spencer (2020) and Caspar Oesterheld and Vincent Conitzer (2021) prove that asymmetric variants of this structure force a CDT agent to **voluntarily lose money** (or submit to a diachronic Dutch book) regardless of the agent's beliefs.

Consider Oesterheld and Conitzer's (2021) **Adversarial Offer**, described in the reference article:
* Two boxes, Box 1 and Box 2, are on offer.
* A buyer has three available actions: buy Box 1 ($B_1$), buy Box 2 ($B_2$), or buy neither box ($N$). Each box costs $\$1$.
* Yesterday, the seller predicted which of the three actions the buyer would take ($\hat{B}_1, \hat{B}_2,$ or $\hat{N}$) and placed $\$3$ in *each box that she predicted the buyer not to acquire*.
* Both buyer and seller know the seller's prediction is accurate with probability $0.75$.

Let us construct the complete causal payoff matrix across the three possible dependency hypotheses (corresponding to the seller's three possible predictions yesterday):

1. **State $S_1$ (Seller predicted $\hat{B}_1$)**: Box 1 was predicted to be acquired, so it contains $\$0$; Box 2 was predicted not to be acquired, so it contains $\$3$.
2. **State $S_2$ (Seller predicted $\hat{B}_2$)**: Box 1 contains $\$3$; Box 2 contains $\$0$.
3. **State $S_N$ (Seller predicted $\hat{N}$)**: Neither box was predicted to be acquired, so *both* Box 1 and Box 2 contain $\$3$.

Subtracting the $\$1$ purchase price when a box is bought, the net monetary payoffs $D(A, S_k)$ to the buyer are:

| Buyer's Action | $S_1$ (Boxes: $\$0, \$3$) | $S_2$ (Boxes: $\$3, \$0$) | $S_N$ (Boxes: $\$3, \$3$) |
| :--- | :---: | :---: | :---: |
| **$B_1$ (Buy Box 1 for $\$1$)** | $-\$1$ | $+\$2$ | $+\$2$ |
| **$B_2$ (Buy Box 2 for $\$1$)** | $+\$2$ | $-\$1$ | $+\$2$ |
| **$N$ (Buy Neither)** | $\$0$ | $\$0$ | $\$0$ |

Let $p_1 = P(S_1)$, $p_2 = P(S_2)$, and $p_N = P(S_N)$ be the buyer's unconditional credences over the seller's prediction, where $p_1 + p_2 + p_N = 1$ and $p_k \ge 0$. Under CDT, holding $(p_1, p_2, p_N)$ fixed, the causal expected utilities are:

$$U(B_1) = -p_1 + 2p_2 + 2p_N = 3(p_2 + p_N) - 1$$

$$U(B_2) = 2p_1 - p_2 + 2p_N = 3(p_1 + p_N) - 1$$

$$U(N) = 0$$

Now take the simple arithmetic mean of the causal expected utilities of buying Box 1 and buying Box 2:

$$\frac{U(B_1) + U(B_2)}{2} = \frac{3(p_1 + p_2 + 2p_N) - 2}{2} = \frac{3(1 + p_N) - 2}{2} = 0.5 + 1.5p_N \ge \$0.50$$

This inequality is remarkable: **for every possible probability distribution $(p_1, p_2, p_N)$, the average causal expected value of buying a box is at least $+\$0.50$ net of the $\$1$ cost** (since at least one box contains $\$3$, the average gross value of a box is at least $\$1.50$). Because the average of $U(B_1)$ and $U(B_2)$ is at least $\$0.50$, it is mathematically impossible for both $U(B_1)$ and $U(B_2)$ to be $\le 0$:

$$\max\left\{U(B_1), U(B_2)\right\} \ge \$0.50 > U(N) = \$0$$

Therefore, regardless of what the buyer believes she is going to do, CDT strictly prohibits walking away ($N$) and requires buying either Box 1 or Box 2!

Yet what actually happens when the CDT agent buys a box $B_i$ ($i \in \{1, 2\}$)? Because the seller's prediction is accurate with probability $0.75$, conditional on the buyer choosing $B_i$, the probability that the seller predicted $\hat{B}_i$ (and thus left Box $i$ empty) is $P(S_i \mid B_i) = 0.75$. With only $0.25$ probability does Box $i$ contain $\$3$. Thus, the buyer's actual expected payoff upon buying $B_i$ is:

$$V(B_i) = 0.75(-\$1) + 0.25(+\$2) = -\$0.25 < \$0 = V(N)$$

Every time a CDT agent faces the Adversarial Offer, CDT compels them to enter a trade that loses $\$0.25$ in expectation to the seller, whereas an EDT agent simply computes $V(B_1) = V(B_2) = -\$0.25 < V(N) = 0$ and refuses the offer.

---

## 6. Operationalizing Self-Information and Ratifiability

The reference article notes that James Joyce (2012, 2020; see also Weirich 2016), the most prominent contemporary defender of CDT, argues that these counterexamples misunderstand how a sophisticated causal decision theorist deliberates: CDT is fully capable of taking into account *"information about what one is inclined or likely to do as evidence"* during the deliberation process. However, the source leaves open the exact mathematical formulation of Joyce's defense and how far it goes toward solving the counterexamples.

Let us formulate an explicit operational interpretation of **Self-Information CDT (or Deliberative CDT)** so that readers can apply it systematically (clearly distinguishing this mathematical synthesis from the brief summary in the source).

### The Deliberative Update Equation and Ratifiability

In standard ("pre-deliberative") CDT, the agent evaluates $U(A)$ using fixed prior credences $P(S_k)$ formed *before* noticing their own deliberative inclination. Under Joyce's framework—building on William Harper's (1984) and Richard Jeffrey's concept of **ratifiability**—an agent who is on the verge of choosing action $A$ acquires a piece of self-evidence $I_A$: *"I am inclined (or about to decide) to perform $A$."*

The agent may legitimately use Bayes' rule to update their beliefs about the exogenous dependency hypotheses $S_k$ upon observing their own inclination $I_A$:

$$P(S_k \mid I_A) = \frac{P(I_A \mid S_k) P(S_k)}{P(I_A)}$$

Critically, to remain a *causal* rather than an *evidential* decision theorist, the agent evaluates each alternative action $A' \in \mathcal{A}$ while holding fixed the credences $P(S_k \mid I_A)$ induced by their current inclination $I_A$. Define the **conditional causal expected utility** of action $A'$ given inclination $I_A$ as:

$$U(A' \mid I_A) = \sum_{k=1}^{K} P(S_k \mid I_A) \sum_{j=1}^{m} P(O_j \mid A' \wedge S_k) D(O_j)$$

An action $A^* \in \mathcal{A}$ is **ratifiable** if and only if it maximizes causal expected utility *on the supposition that the agent has decided to perform $A^*$*:

$$U(A^* \mid I_{A^*}) \ge U(A' \mid I_{A^*}) \quad \text{for all } A' \in \mathcal{A}$$

Let us test this operational procedure across our three frontier cases:

1. **How Deliberative CDT Solves the Psychopath Button**:
   Suppose Paul initially feels inclined to press the button ($I_{A_P}$). Before his finger hits the button, he updates his credence in the causal states on this inclination: $P(S_{\Psi} \mid I_{A_P}) = 0.95$ and $P(S_{\neg \Psi} \mid I_{A_P}) = 0.05$. Holding these updated credences fixed, he evaluates both actions:

   $$U(A_P \mid I_{A_P}) = 0.05(10) + 0.95(-100) = -94.5$$

   $$U(A_N \mid I_{A_P}) = 0.05(0) + 0.95(0) = 0$$

   Because $U(A_P \mid I_{A_P}) < U(A_N \mid I_{A_P})$, pressing the button is **unratifiable**! Conversely, if Paul resolves to abstain ($I_{A_N}$), wait—if he completely forgets his temptation to press and reverts to $P(S_{\Psi} \mid I_{A_N}) = 0.01$, he would feel tempted again. However, as Joyce (2012) emphasizes, a rational agent *retains the evidence of their earlier inclination* (learning that "I am the sort of person who was just tempted to press") or converges to a mixed deliberative state where $P(S_{\Psi}) \ge \frac{10}{110} \approx 0.091$, at which point abstaining ($A_N$) is the unique stable, ratifiable choice.

2. **Why Newcomb's Problem Remains Two-Boxing**:
   Does updating on self-information turn CDT into EDT in Newcomb's problem? Not at all! Even if you update on the inclination to One-Box ($I_{A_1}$), setting $P(S_1 \mid I_{A_1}) = 0.99$, evaluating both actions under that fixed distribution still yields:

   $$U(A_2 \mid I_{A_1}) = 0.99(\$1,001,000) + 0.01(\$1,000) = \$991,000 > U(A_1 \mid I_{A_1}) = \$990,000$$

   And conditional on Two-Boxing ($I_{A_2}$), where $P(S_1 \mid I_{A_2}) = 0.01$, we have:

   $$U(A_2 \mid I_{A_2}) = \$11,000 > U(A_1 \mid I_{A_2}) = \$10,000$$

   Thus, **Two-Boxing ($A_2$) is the unique ratifiable pure action in Newcomb's problem**. Self-information only alters CDT's recommendation when the relative causal payoff difference $U(A \mid S_k) - U(A' \mid S_k)$ changes sign across states $S_k$.

3. **Why the Adversarial Offer Still Traps CDT**:
   What happens when we apply Deliberative CDT to Oesterheld and Conitzer's Adversarial Offer? Because our earlier proof showed that $\max\{U(B_1), U(B_2)\} \ge \$0.50 > U(N) = \$0$ for *every* probability distribution $(p_1, p_2, p_N)$, updating on $I_A$ cannot rescue the action $N$: even conditional on $I_N$, $U(B_1 \mid I_N) = U(B_2 \mid I_N) > U(N \mid I_N)$, so **walking away ($N$) is never ratifiable**.
   Instead, conditional on $I_{B_1}$ ($p_1 = 0.75$), CDT prefers $B_2$; conditional on $I_{B_2}$ ($p_2 = 0.75$), CDT prefers $B_1$. Just as in Death in Damascus, the unique ratifiable equilibrium for a CDT agent who can randomize is the mixed strategy placing probability $\frac{1}{2}$ on $B_1$ and $\frac{1}{2}$ on $B_2$ (which induces $p_1 = p_2 = 0.5 \times 0.75 + \dots$, making $U(B_1) = U(B_2) \ge \$0.50 > U(N)$). And playing that mixed strategy still buys a box with probability $1$, locking in the $-\$0.25$ expected loss to the seller!

### Summary Checklist for Applying CDT to Unfamiliar Problems

When confronted with a new decision problem, a practitioner can apply CDT systematically in four steps:
1. **Partition the Exogenous Causal States**: Identify a partition of dependency hypotheses $\mathcal{S} = \{S_1, \dots, S_K\}$ that are causally upstream or causally independent of the choice set $\mathcal{A}$, such that each $S_k$ fixes the forward causal probabilities $P(O_j \mid A \wedge S_k)$.
2. **Check for Causal Dominance**: Compute the state-by-state expected utilities $u(A, S_k) = \sum_j P(O_j \mid A \wedge S_k) D(O_j)$. If an action $A^*$ satisfies $u(A^*, S_k) \ge u(A', S_k)$ for all $S_k$ (as in King David, Newcomb's Problem, and the Twin Prisoner's Dilemma), CDT unconditionally recommends $A^*$ regardless of the probability distribution over $\mathcal{S}$.
3. **Test for Act-State Interaction (Deliberative Ratifiability)**: If the optimal action varies across states $S_k$ *and* the agent's inclinations provide diagnostic evidence about $S_k$ (as in the Psychopath Button), compute the ratifiable causal expected utility $U(A' \mid I_A)$ using updated state probabilities $P(S_k \mid I_A)$ and select an action $A^*$ where $U(A^* \mid I_{A^*}) = \max_{A'} U(A' \mid I_{A^*})$.
4. **Check for Adversarial Instability**: If no pure action is ratifiable (as in Death in Damascus or the Adversarial Offer), identify the Nash-like ratifiable mixed distribution over $\mathcal{A}$ where every action in the support ties for maximum causal expected utility—while recognizing that against an accurate predictor, this causal equilibrium may carry a negative evidential return.

---

## 7. Conclusion

Causal Decision Theory captures a foundational insight of scientific rationality: to decide is to intervene in the causal order of the world, not merely to diagnose one's place within it. By replacing standard conditional probabilities $P(O_j \mid A)$ with counterfactual probabilities $P(A \to O_j)$—operationalized by holding fixed one's credences over causal dependency hypotheses $S_k$—CDT cleanly immunizes decision-makers against spurious common-cause correlations like the dilemma of King David. Yet as modern game-theoretic paradoxes such as the Psychopath Button and the Adversarial Offer demonstrate, the boundary between diagnosing the world and intervening in it becomes deeply entangled when predictors anticipate our choices or when our own inclinations reveal the causal laws governing our actions. Understanding both the formal equations of CDT and their behavior under self-information equips us to navigate this foundational frontier of rational choice.

---

## References

* Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
* Egan, A. (2007). "Some counterexamples to causal decision theory." *The Philosophical Review*, 116(1), 93–114.
* Gibbard, A., & Harper, W. L. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190).
* Greaves, H. (2013). "Epistemic decision theory." *Mind*, 122(488), 915–952.
* Harper, W. (1984). "Ratifiability and Causal Decision Theory: Comments on Eells and Seidenfeld." *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1984(2), 213–228.
* Howard, J. V. (1988). "Cooperation in the Prisoner's Dilemma." *Theory and Decision*, 24(3), 203–213.
* Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese*, 187(1), 123–145.
* Joyce, J. M. (2020). "Yet Another Refutation of Causal Decision Theory?" Unpublished manuscript, University of Michigan.
* Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *The Philosophical Review*, 85(3), 297–315.
* Lewis, D. (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy*, 59(1), 5–30.
* Meacham, C. J. G. (2010). "Binding and its consequences." *Philosophical Studies*, 149(1), 49–71.
* Oesterheld, C., & Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *The Philosophical Quarterly*, 71(4), pqaa086.
* Shaffer, M. J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines*, 19(1), 61–92.
* Spencer, J. (2020). "An argument against causal decision theory." *Analysis*, 81, 52–61.
* Weirich, P. (2016). "Causal Decision Theory." In E. N. Zalta (Ed.), *The Stanford Encyclopedia of Philosophy* (Winter 2016 ed.).
* Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese*, 190(9), 1637–1646.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Project Scope**

I'm now zeroing in on defining the precise scope. The goal is clear: a mathematically rigorous piece on Causal Decision Theory for an expert audience. I'm focusing on framing this as a researcher's perspective. It's crucial to lay out CDT's applicability in decision problems, so I'm thinking about the audience's needs.


**Expanding the Core Content**

I am now focused on integrating and expanding upon the Wikipedia article on Causal Decision Theory. My goal is to add formal definitions, operational procedures, philosophical motivations, and examples that will help the audience apply it to novel situations. I'm taking care to differentiate claims from the source versus my own reconstructions or proposals. I'm aiming for about 2,400 to 3,000 words. I am also working on requirements analysis.


**Refining the Argument's Scope**

I'm now diving into the word count requirements, aiming for the 2,400–3,000 word range. This will require rigorous mathematical explanations and worked examples. I am now working on outlining the core content: definitions (formal and informal), contrasts with EDT (Apple vs. orange example) and the formal gibbard-harper equation (clarifying phrasing).


**Clarifying Causal Foundations**

I'm now honing in on the counterfactual meaning, particularly in light of Lewis's triviality result and Gibbard & Harper's independence condition. This involves rigorously contrasting CDT with EDT, exploring the implications of their differing assumptions about conditionals. The King David and Bathsheba example is particularly useful for exposing the role of confounded common causes in decision contexts.


**Analyzing Decision Contexts**

I'm now analyzing decision contexts and working on incorporating thought experiments. I'm focusing on the contrast between EDT and CDT in situations such as the King David and Bathsheba example, and exploring the implications of their differing assumptions about conditionals. I'm also including Newcomb's Paradox and its variants as a key thought experiment, and making sure to carefully explain how EDT and CDT yield different recommendations. Furthermore, I've got to explore CDT's counter-intuitive recommendation in certain scenarios, like when one is considering summoning a revolt. Finally, I've started thinking about criticisms, specifically, the vague definitions of CDT.


**Examining Key Dilemmas**

I'm now diving into concrete thought experiments to highlight CDT's implications. The "Psychopath Button" presents a strong challenge, where CDT's recommended action clashes with common intuition. I'm also grappling with the complexities of "Death in Damascus," specifically the instability it exposes in processing correlations. Furthermore, the "Adversarial Offer" scenario showcases the potential for CDT to lead to predictable losses, and I'm assessing Joyce's defenses.


**Developing the Formalism**

Now, I'm working to expand the formal apparatus with the Gibbard–Harper equation, contrasting it with EDT's framework, and referencing Lewis's triviality result. I'm focusing on defining CDT's ability to incorporate information regarding our inclinations and actions, which Weirich and Ahmed argue it can (ratifiability/self-information). I'm constructing an essay structure with an engaging title, followed by an introduction highlighting the intervention-observation tension, leading into a discussion of the formal structures of CDT and EDT.


**Operationalizing Counterfactuals**

I'm now focusing on operationalizing counterfactuals within CDT. I'm unpacking the Gibbard–Harper equivalence theorem, explicitly stating its axioms, including the Principle of Conditional Excluded Middle (CEM) and Modus Ponens, with a mathematical reconstruction. I'm also addressing the "Vagueness" criticism by exploring how to compute P(A -> Oj), specifically Lewis's imaging and Egan's dependency hypotheses.


**Operationalizing Frameworks**

I'm now striving to establish a clear framework, bridging operational concepts for the audience, while explicitly separating the source's claims from my formal operationalization. I'm focusing on "dependency hypotheses" that partition the state space and eliminate the epistemic regress, connecting this to Lewis's imaging. I'm also planning to use concrete examples with numerical parameters, like the Bathsheba example.


**Analyzing Complex Examples**

I'm now analyzing more complex examples to highlight specific issues. I'm focusing on "Predictive Correlation" cases, like Newcomb's Paradox and the Twin Prisoner's Dilemma, showing how dominance reasoning emerges naturally. I'm also examining the challenges related to act-state dependence, specifically, exploring the "Psychopath Button" thought experiment to showcase CDT's counter-intuitive recommendation. Finally, I will also unpack the "As" structure.


**Analyzing Decision Outcomes**

I am now closely analyzing the "Adversarial Offer" to pinpoint where CDT leads to predictable losses. I will mathematically prove the lower bound of $0.50 for a CDT agent, despite the box's negative expected return, and will work to formalize and distinguish pre-deliberative and deliberative CDT approaches. This contrasts with Joyce's defenses, which can resolve the open questions of self-information and ratifiability.


**Synthesizing Key Applications**

I am now focusing on the conclusion, aiming for a synthesis of applying CDT, and identifying philosophical boundaries. I'm prioritizing mathematical rigor for the Gibbard–Harper equivalence proof, reconstructing it clearly for the reader. I am also working on checking the proof's logic and guaranteeing its clarity, especially the statistical independence condition for A and A -> Oj. I'm also planning to explore the ratifiability/self-information, particularly around $U(A \mid I_A) = \sum_k P(S_k \mid I_A) D(S_k(A))$, and linking it to addressing scenarios like the "Psychopath Button", and diagnosing the "Adversarial Offer" as a failure of unique ratifiable equilibria.


**Reconstructing Gibbard-Harper**

I'm working on the Gibbard-Harper reconstruction. I've re-examined their axiomatic framework. I can see why the Principle of Conditional Excluded Middle (CEM) and Modus Ponens are important in their derivation. Assuming statistical independence, this leads to $P(O_j \mid A) = P(A \to O_j)$. I am working on clarifying this as it is used in the theorem. I'm focusing on the statistical independence condition, and how this relates to Lewis's imaging.


**Clarifying Probabilistic Foundations**

I'm now clarifying the probabilistic foundations of Gibbard-Harper and its relationship to counterfactuals, particularly the Principle of Conditional Excluded Middle (CEM). I am explicitly working to demonstrate that without CEM, the counterfactual conditionals don't form a proper probability distribution. The goal is to provide a rigorous mathematical framework, focusing on how this impacts the overall probability calculus. I'm also delving into the Adversarial Offer scenario, and working through the math from Oesterheld & Conitzer (2021) to confirm that the framework is correct.


**Formalizing the Buyer's Dilemma**

I'm now focused on formalizing the "Predictive Buyer" scenario. I'm defining actions, seller's predictions, and state space to illustrate how CDT leads to buying one of the two boxes, despite the negative expected return. I'm working through the probabilities and payoffs for each possible action, formalizing the buyer's rationalization in response to the seller's predictions. The goal is to mathematically demonstrate CDT's reasoning and contrast it with alternative approaches.


**Analyzing Predictive Reasoning**

I'm now zeroing in on the Predictive Buyer scenario. I've formalized the buyer's actions, and the seller's predictions in terms of states. I'm working through a rigorous mathematical proof demonstrating that, for *any* initial probability distribution, Causal Decision Theory (CDT) will always favor buying a box, despite its negative expected return. I'm showing how this highlights CDT's departure from expected utility theory, as the average expected utility is at least \$0.50, and must outweigh the option to choose nothing.


**Operationalizing Action Analysis**

I'm now zeroing in on formalizing the "Predictive Buyer" scenario. I'm focusing on the probabilistic interpretation, and mathematically proving that Causal Decision Theory (CDT) will always favor buying a box, irrespective of expected return. This highlights CDT's divergence from expected utility theory. I will also clarify the expected value of an agent that abstains.


**Modeling Decision Preferences**

I am now closely modeling the "Psychopath Button" scenario. Standard CDT recommends pressing, even with very low initial psychopathy credence, because pressing suggests a causal mapping. The state determines the relevant map, which is why CDT recommends pressing. I am now working on evaluating how this recommendation depends on initial credences and the strength of the evidence of psychopathy, and on how we can model this correctly.


**Evaluating the Budgeted Word Count**

I'm evaluating my word count estimates for each section. My current plan is for an introduction and informal foundations section of roughly 350 words, with 550 for the formal architecture of Gibbard–Harper, EDT, and Lewis's triviality. Operationalizing counterfactuals will be around 500, with 500 for the canonical applications of Bathsheba, Newcomb's Paradox, etc. Pathologies will be about 450, operationalizing self-information and ratifiability 300 words, and the conclusion 150.


```
