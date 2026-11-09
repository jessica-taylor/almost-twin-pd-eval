# 005_cdt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00002

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a88fa862-7eef-41da-a116-9b232f88f000/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a88fa862-7eef-41da-a116-9b232f88f000/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Counterfactuals, Interventions, and Rational Choice: A Mathematical Guide to Causal Decision Theory

When a rational agent chooses among competing actions, how should they evaluate the consequences of their choice? At first glance, standard probability theory seems to offer a straightforward answer: compute the expected utility of each action by conditioning on the event that the action is performed. Yet one of the deepest developments in twentieth-century philosophical logic and decision theory was the discovery that conditional probability tracks *evidence*, not *causation*. When an action is statistically correlated with background states of the world that the agent cannot control, maximizing conditional expected utility leads to decisions that manage the news rather than shape the future.

**Causal decision theory** (CDT) was developed to resolve this confusion. As summarized in the reference literature (Ahmed 2021; Weirich 2016), CDT is the school of thought within decision theory holding that a rational agent confronted with a set of possible actions should select the action that *causes* the best outcome in expectation. It stands in direct opposition to **evidential decision theory** (EDT), which advises the agent to select the action that would be the best "news"—that is, the action most indicative of a favorable outcome if one were informed that it had been taken.

This essay provides a mathematical account of CDT, explaining both its philosophical motivation and its formal mechanics. Because the foundational literature leaves certain computational questions open—most notably how to algorithmically evaluate the probabilities of counterfactual conditionals—we will distinguish between the core claims established in the source material and the operational extensions we introduce to make the theory applicable to unfamiliar decision problems.

---

## 1. The Informal Intuition: Expected Causal Effects

To see what is at stake, consider the baseline scenario described in the reference article. Suppose you are choosing between eating an apple ($A_{\text{apple}}$) and eating an orange ($A_{\text{orange}}$). If you know with certainty that eating the apple will cause you to be happy and eating the orange will cause you to be sad, rationality trivially dictates eating the apple.

Decision theory becomes nontrivial when causal consequences are uncertain. Suppose that eating a *good* apple causes happiness, whereas eating a *bad* apple causes sadness, and you do not know whether the apple in front of you is good or bad. As the source text notes, you do not know the actual causal effect of eating the apple; instead, you must evaluate its *expected* causal effects, which depend on three quantities:
1. How likely you think the apple is to be good or bad;
2. How happy eating a good apple makes you; and
3. How sad eating a bad apple makes you.

*(To formalize this informal example beyond the source text, let $S \in \{G, B\}$ denote the state of the apple, with prior probabilities $P(G) = p$ and $P(B) = 1 - p$, and assign utilities $u_{\text{happy}} > 0 > u_{\text{sad}}$ with $u_{\text{orange}} = 0$. The expected causal utility of eating the apple is simply $p \, u_{\text{happy}} + (1 - p) u_{\text{sad}}$.)*

In this simple setting, the state of the apple ($G$ or $B$) is statistically independent of your choice to eat it. Your choosing to eat the apple gives you no new evidence about whether the apple is rotten. Consequently, causal and evidential reasoning coincide. The divergence between CDT and EDT arises when your choice *does* carry statistical information about the background state of the world—even though your choice has no causal power over that state.

---

## 2. Formal Architecture: Counterfactuals vs. Conditional Probabilities

### The Gibbard–Harper Equation

In their landmark 1981 paper, Allan Gibbard and William Harper formalized causal decision theory by replacing standard conditional probabilities with the probabilities of *counterfactual conditionals* (Gibbard & Harper 1981). Let $\mathcal{A}$ be a finite set of available actions, and let $\{O_j\}$ be a mutually exclusive and exhaustive partition of possible outcomes, each assigned a numerical desirability (or utility) $D(O_j) \in \mathbb{R}$.

As stated in the reference article, Gibbard and Harper define the causal expected utility $U(A)$ of an action $A \in \mathcal{A}$ as:

$$U(A) = \sum_{j} P(A \to O_j) D(O_j), \tag{1}$$

where $A \to O_j$ is the counterfactual (or subjunctive) conditional proposition *"If the agent were to perform $A$, then outcome $O_j$ would occur"* (rendered in the source text as it being the case that $A$ causally or counterfactually implies $O_j$), and $P(A \to O_j)$ is the agent's subjective probability that this conditional holds.

By contrast, evidential decision theory evaluates an action $A$ using standard conditional probabilities:

$$U_{\text{EDT}}(A) = \sum_{j} P(O_j \mid A) D(O_j), \quad \text{where } P(O_j \mid A) = \frac{P(A \land O_j)}{P(A)}. \tag{2}$$

### Lewis's Triviality Result

Why introduce a specialized counterfactual connective $\to$ rather than simply identifying $P(A \to O_j)$ with the conditional probability $P(O_j \mid A)$? As the reference article highlights, David Lewis (1976) proved a celebrated impossibility theorem—known as **Lewis's triviality result**—demonstrating that $P(A \to O_j)$ cannot in general equal $P(O_j \mid A)$ if $\to$ is a genuine propositional connective obeying the standard laws of probability.

Specifically, the source notes Lewis's stronger theorem: if a class of probability functions is closed under conditionalizing, there can be no probability conditional $\to$ satisfying $P(A \to B) = P(B \mid A)$ for all $A, B$ in that class unless the class consists entirely of *trivial* probability functions—defined as probability functions that never assign positive probability to more than two incompatible alternatives (and are therefore at most four-valued).

*Mathematical Reconstruction of Lewis's Proof (Extending the Source):* It is instructive to see the short algebraic proof of how this collapse occurs. Suppose $\to$ is a proposition inside our algebra of events such that for any probability measure $P$ in aconditionalization-closed family and any events $A, C$ with $P(A) > 0$, we have $P(A \to C) = P(C \mid A)$. Assuming $P(A \land C) > 0$ and $P(A \land \neg C) > 0$, we can conditionalize $P$ on $C$ and $\neg C$ to obtain two new probability measures $P_C(\cdot) = P(\cdot \mid C)$ and $P_{\neg C}(\cdot) = P(\cdot \mid \neg C)$. By hypothesis, the conditional rule must hold for $P_C$ and $P_{\neg C}$ as well:

$$P(A \to C \mid C) = P_C(A \to C) = P_C(C \mid A) = P(C \mid A \land C) = 1,$$

$$P(A \to C \mid \neg C) = P_{\neg C}(A \to C) = P_{\neg C}(C \mid A) = P(C \mid A \land \neg C) = 0.$$

Expanding $P(A \to C)$ by the law of total probability over the partition $\{C, \neg C\}$ yields:

$$P(A \to C) = P(A \to C \mid C)P(C) + P(A \to C \mid \neg C)P(\neg C) = 1 \cdot P(C) + 0 \cdot P(\neg C) = P(C).$$

Since $P(A \to C) = P(C \mid A)$ by assumption, we are forced to conclude that $P(C \mid A) = P(C)$ whenever $P(A \land C) > 0$ and $P(A \land \neg C) > 0$. In any probability space containing three mutually incompatible events with positive probability, one can choose $A$ and $C$ to violate this independence—proving that a counterfactual conditional $\to$ cannot be globally equated with conditional probability.

### The Gibbard–Harper Equivalence Condition

When *do* CDT and EDT agree? As reported in the reference text, Gibbard and Harper (1981) proved that if we accept two logical axioms governing counterfactuals, then the **statistical independence** of the action $A$ and the counterfactual $A \to O_j$ suffices to guarantee that $P(A \to O_j) = P(O_j \mid A)$.

*Mathematical Derivation of the Equivalence (Reconstructed from the Source's Description):* Let us state the two axioms referenced by Gibbard and Harper (and discussed in Shaffer 2009) and show how they yield the equality:

1. **Conditional Excluded Middle (CEM):** For any action $A$ and outcome $O_j$, either $A$ would result in $O_j$ or $A$ would result in $\neg O_j$:
   $$(A \to O_j) \lor (A \to \neg O_j) \quad \text{is logically true, and} \quad \neg\big((A \to O_j) \land (A \to \neg O_j)\big).$$
2. **Centering / Counterfactual Modus Ponens:** In any possible world where $A$ is actually performed, the counterfactual $A \to O_j$ has the same truth value as the actual outcome $O_j$:
   $$A \land (A \to O_j) \iff A \land O_j.$$

From Axiom 2, the events $A \land (A \to O_j)$ and $A \land O_j$ are identical, so their probabilities are equal:

$$P\big(A \land (A \to O_j)\big) = P(A \land O_j).$$

Dividing both sides by $P(A) > 0$ gives the general relationship between conditional probability and counterfactuals:

$$P(A \to O_j \mid A) = \frac{P\big(A \land (A \to O_j)\big)}{P(A)} = \frac{P(A \land O_j)}{P(A)} = P(O_j \mid A). \tag{3}$$

Equation (3) reveals the exact locus of disagreement between EDT and CDT. EDT evaluates $P(O_j \mid A)$, which by (3) is the probability of the counterfactual $A \to O_j$ *given that $A$ is performed*: $P(A \to O_j \mid A)$. CDT, by contrast, evaluates the *unconditional* probability of the counterfactual: $P(A \to O_j)$.

If $A$ and $A \to O_j$ are statistically independent, then $P(A \to O_j \mid A) = P(A \to O_j)$, and therefore:

$$P(A \to O_j) = P(O_j \mid A).$$

When an agent's choice $A$ is statistically correlated with the causal mechanism $A \to O_j$, however, independence fails, and the two theories diverge.

---

## 3. Operationalizing CDT: How to Compute $P(A \to O_j)$

### The Vagueness Problem and Lewisian Imaging

A major criticism noted in the reference article (Shaffer 2009) is that Equation (1) does not by itself specify an algorithm for calculating the counterfactual probabilities $P(A \to O_j)$. If a practitioner is handed a decision problem, how should they compute $P(A \to O_j)$?

The source text discusses one prominent proposal due to David Lewis (1981): the method of **imaging**. Let $W$ be a set of possible worlds equipped with a prior probability distribution $P$. To evaluate $P(A \to O_j)$ assuming $A$ is possible:
* For each possible world $w \in W$, identify the "closest" possible world $w_A \in W$ in which the action $A$ holds (assuming a unique closest world, which ties back to CEM).
* Transfer (or "image") the entire probability mass $P(w)$ from each world $w$ to its closest $A$-world $w_A$.

Formally, the imaged probability distribution $P^A$ on $W$ is defined by:

$$P^A(w') = \sum_{w \in W \,:\, w_A = w'} P(w), \tag{4}$$

and the probability of the counterfactual is the probability of $O_j$ under the imaged measure:

$$P(A \to O_j) = P^A(O_j) = \sum_{w \in W \,:\, w_A \in O_j} P(w). \tag{5}$$

Notice how imaging differs from Bayesian conditionalization. Conditionalization on $A$ throws away all probability mass outside $A$ and rescales the remaining mass proportionally. Imaging *conserves* probability mass locally, shifting the mass of each $\neg A$-world to its most similar $A$-world while holding causal background facts fixed.

However, as the reference article observes (citing Shaffer 2009), imaging faces an operational hurdle: determining the closest world $w_A$ requires knowing what would be true if $A$ were certain to occur, which is itself a counterfactual judgment to which an agent might assign probability less than $1$, threatening an epistemic regress.

### An Operational Resolution: Partitioning by Dependency Hypotheses

To make CDT fully operational for solving unfamiliar cases, we can connect Gibbard and Harper's formalism to a second concept mentioned in the reference article's discussion of Andy Egan (2007): **dependency hypotheses** (or causal background states).

*Operational Framework (Our Synthesis Extending the Source):* Suppose we partition the space of possible worlds into a set of mutually exclusive and exhaustive background states $\mathcal{S} = \{S_1, S_2, \dots, S_m\}$. Each state $S_k$ is a *dependency hypothesis*—a complete specification of how the world is causally wired and what background factors obtain independently of the agent's present choice. Crucially, we choose the partition $\mathcal{S}$ fine-grained enough to satisfy two operational criteria:

1. **Causal Independence of States from Actions:** The agent knows that their choice of action $A$ has no causal influence on which state $S_k$ holds. That is, for every world $w \in S_k$, its closest $A$-world $w_A$ also lies in $S_k$.
2. **Screening Off (Back-Door Sufficiency):** Once the background state $S_k$ is fixed, there is no remaining non-causal confounding between the action $A$ and the counterfactual $A \to O_j$. Within each $S_k$, $A$ is conditionally independent of $A \to O_j$, so by Equation (3), $P(A \to O_j \mid S_k) = P(O_j \mid A, S_k)$.

Applying the law of total probability across the partition $\mathcal{S}$ gives an explicit, computable formula for the counterfactual probability:

$$P(A \to O_j) = \sum_{k=1}^{m} P(S_k) P(A \to O_j \mid S_k) = \sum_{k=1}^{m} P(S_k) P(O_j \mid A, S_k). \tag{6}$$

Substituting Equation (6) into Gibbard and Harper's utility formula (1) yields the **Partition Formulation of Causal Decision Theory**:

$$U_{\text{CDT}}(A) = \sum_{k=1}^{m} P(S_k) \sum_{j} P(O_j \mid A, S_k) D(O_j). \tag{7}$$

Compare Equation (7) with the corresponding expansion of Evidential Decision Theory (2) across the same state partition $\mathcal{S}$:

$$U_{\text{EDT}}(A) = \sum_{k=1}^{m} P(S_k \mid A) \sum_{j} P(O_j \mid A, S_k) D(O_j). \tag{8}$$

Equations (7) and (8) make the mathematical difference between CDT and EDT completely transparent:
* Both theories compute the conditional outcome distribution $P(O_j \mid A, S_k)$ within each causal state $S_k$.
* **EDT** weights each state $S_k$ by the *evidentially updated* probability $P(S_k \mid A)$, allowing the choice of $A$ to shift the agent's credences about causally immutable background states.
* **CDT** weights each state $S_k$ by the *unconditional* probability $P(S_k)$, holding fixed the agent's beliefs about factors outside their causal control. (Readers familiar with Judea Pearl's structural causal models will recognize $\sum_k P(S_k) P(O_j \mid A, S_k)$ as the back-door adjustment formula for the interventional distribution $P(O_j \mid \mathrm{do}(A))$.)

Whenever you face an unfamiliar decision problem, you can apply CDT via a four-step procedure:
1. **Specify Actions and Outcomes:** List the available actions $A \in \mathcal{A}$ and outcome utilities $D(O_j)$.
2. **Isolate Background States:** Identify a partition of states $\{S_k\}$ that are causally unaffected by $A$ and that screen off all non-causal correlations between $A$ and $O_j$.
3. **Assign Unconditional State Credences:** Determine the prior probabilities $P(S_k)$ (ignoring any purely statistical correlation between $A$ and $S_k$).
4. **Compute Expected Causal Utility:** Evaluate $U_{\text{CDT}}(A)$ using Equation (7) and select $\arg\max_{A \in \mathcal{A}} U_{\text{CDT}}(A)$.

---

## 4. Canonical Applications: Confounding and Prediction

Let us put this formal procedure to work on the classic decision problems described in the reference article. *(In each case, the qualitative scenario and theoretical verdict come directly from the source text, while the specific numerical parameters are our illustrative additions to demonstrate the calculation.)*

### Common-Cause Confounding: King David and Bathsheba

Gibbard and Harper (1981, p. 164) illustrate the failure of independence between $A$ and $A \to O_j$ with the story of King David and Bathsheba. As recounted in the reference article:
* Kings have two personality types: charismatic ($C$) and uncharismatic ($\neg C$), fixed by genetics and early childhood experiences and unchangeable in adulthood.
* Charismatic kings tend to act justly, whereas uncharismatic kings tend to act unjustly.
* Successful revolts ($R$) against charismatic kings are rare, whereas successful revolts against uncharismatic kings are frequent—not because unjust acts cause revolts, but because uncharismatic kings have a sneaky, ignoble bearing.
* David does not know whether he is charismatic, but he knows that summoning Bathsheba ($S$) is an unjust act, whereas abstaining ($\neg S$) is just.

Let us parameterize this problem to apply Equations (7) and (8):
* **States:** $\mathcal{S} = \{C, \neg C\}$, with David's prior credence $P(C) = 0.5$ and $P(\neg C) = 0.5$.
* **Diagnostic correlation:** Given his political science texts, David believes that if he acts unjustly ($S$), he is likely uncharismatic: $P(C \mid S) = 0.1$ and $P(\neg C \mid S) = 0.9$. Conversely, if he abstains ($\neg S$), $P(C \mid \neg S) = 0.9$ and $P(\neg C \mid \neg S) = 0.1$.
* **Causal mechanism of revolt:** Because unjust acts *themselves* do not cause revolts, the probability of revolt depends only on charisma:
  $$P(R \mid S, C) = P(R \mid \neg S, C) = 0.05, \qquad P(R \mid S, \neg C) = P(R \mid \neg S, \neg C) = 0.80.$$
* **Desirabilities:** Retaining the throne costs $0$ and losing it to a revolt ($R$) yields $-100$; enjoying Bathsheba's company ($S$) adds a utility bonus of $+10$. Thus, the four outcome payoffs are:
  $$D(\neg R \land S) = 10, \quad D(\neg R \land \neg S) = 0, \quad D(R \land S) = -90, \quad D(R \land \neg S) = -100.$$

**EDT Evaluation:** Using Equation (8), EDT updates the probability of David's personality type based on his action:

$$P(R \mid S) = P(C \mid S)P(R \mid S, C) + P(\neg C \mid S)P(R \mid S, \neg C) = (0.1)(0.05) + (0.9)(0.80) = 0.725,$$

$$P(R \mid \neg S) = P(C \mid \neg S)P(R \mid \neg S, C) + P(\neg C \mid \neg S)P(R \mid \neg S, \neg C) = (0.9)(0.05) + (0.1)(0.80) = 0.125.$$

Hence:

$$U_{\text{EDT}}(S) = 10 - 100(0.725) = -62.5, \qquad U_{\text{EDT}}(\neg S) = 0 - 100(0.125) = -12.5.$$

EDT recommends that David abstain ($\neg S$), because summoning Bathsheba is strong evidence that he has an ignoble bearing and will be overthrown.

**CDT Evaluation:** Using Equation (7), CDT holds fixed the unconditional prior $P(C) = P(\neg C) = 0.5$, since David's adulthood decision cannot retroactively alter his genetics or childhood:

$$P(S \to R) = P(C)P(R \mid S, C) + P(\neg C)P(R \mid S, \neg C) = (0.5)(0.05) + (0.5)(0.80) = 0.425,$$

$$P(\neg S \to R) = P(C)P(R \mid \neg S, C) + P(\neg C)P(R \mid \neg S, \neg C) = (0.5)(0.05) + (0.5)(0.80) = 0.425.$$

Thus:

$$U_{\text{CDT}}(S) = 10 - 100(0.425) = -32.5, \qquad U_{\text{CDT}}(\neg S) = 0 - 100(0.425) = -42.5.$$

Since $U_{\text{CDT}}(S) - U_{\text{CDT}}(\neg S) = +10 > 0$, CDT recommends summoning Bathsheba. In medical and social decision-making (such as the famous smoking-gene problem), philosophers overwhelmingly agree with CDT: abstaining from a symptom to manipulate one's diagnosis of an immutable cause is a fallacy of evidential reasoning (Weirich 2016).

### Predictive Correlation: Newcomb's Paradox and the Twin Prisoner's Dilemma

While CDT's triumph in common-cause problems is uncontroversial, its application to *predictive* correlations sparked one of the deepest schisms in decision theory: **Newcomb's paradox** (Wolpert & Benford 2013; Ahmed 2021).

As described in the reference article, a player faces two boxes, A and B, and a predictor whose forecasts of the player's choice are reliable with accuracy $99\%$:
* **Box A** is transparent and always contains a visible $\$1,000$.
* **Box B** is opaque; its content has *already been set* by the predictor prior to the decision:
  * If the predictor predicted the player will take both boxes ($A_2$, "two-boxing"), Box B contains $\$0$.
  * If the predictor predicted the player will take only Box B ($A_1$, "one-boxing"), Box B contains $\$1,000,000$.

Let $\mathcal{S} = \{\hat{A}_1, \hat{A}_2\}$ denote the background state of what the predictor has already placed in Box B, with unconditional probabilities $P(\hat{A}_1) = q$ and $P(\hat{A}_2) = 1 - q$. Assuming utility is linear in dollars, the payoff matrix $D(A_i, \hat{A}_k)$ is:

| Action \ State | $\hat{A}_1$ (Box B has $\$1\text{M}$) | $\hat{A}_2$ (Box B has $\$0$) |
| :--- | :---: | :---: |
| **$A_1$ (Take only Box B)** | $\$1,000,000$ | $\$0$ |
| **$A_2$ (Take Boxes A and B)** | $\$1,001,000$ | $\$1,000$ |

**EDT Evaluation:** Because the predictor is $99\%$ accurate, $P(\hat{A}_1 \mid A_1) = 0.99$ and $P(\hat{A}_2 \mid A_2) = 0.99$. By Equation (8):

$$U_{\text{EDT}}(A_1) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000,$$

$$U_{\text{EDT}}(A_2) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$10,990.$$

EDT strongly recommends one-boxing ($A_1$).

**CDT Evaluation:** Because the prediction lies in the past, the player's present choice cannot causally affect $\hat{A}_k$. Applying Equation (7) with any fixed prior $q = P(\hat{A}_1) \in [0, 1]$ gives:

$$U_{\text{CDT}}(A_1) = q(\$1,000,000) + (1 - q)(\$0) = \$1,000,000\,q,$$

$$U_{\text{CDT}}(A_2) = q(\$1,001,000) + (1 - q)(\$1,000) = \$1,000,000\,q + \$1,000.$$

For *every* value of $q$, $U_{\text{CDT}}(A_2) - U_{\text{CDT}}(A_1) = \$1,000 > 0$. By strict causal dominance, CDT recommends two-boxing ($A_2$).

As the reference article notes (citing Lewis 1979 and Howard 1988), Newcomb's paradox is structurally isomorphic to the **Prisoner's Dilemma** played against a psychological "twin" whose choice to cooperate ($C$) or defect ($D$) correlates strongly with, but is not caused by, one's own choice. If your twin's cooperation gives you $+1,000,000$ and your own defection gives you an extra $+1,000$ regardless of what your twin does, CDT recommends defecting while EDT recommends cooperating. Critics point out that in both scenarios, CDT agents reliably walk away poorer than EDT agents ($1,000$ vs. $1,000,000$).

---

## 5. Pathologies, Instability, and Self-Locating Evidence

Beyond Newcomb's problem, recent research surveyed in the reference article has uncovered sharp counterexamples where a naive application of Equation (7) produces decisions that appear self-destructive, unstable, or financially exploitable. Examining these cases reveals an important open question in the formulation of CDT—and shows how an operational refinement can resolve part, though not all, of the difficulty.

### Act-State Interaction: The Psychopath Button

Andy Egan (2007) argues that CDT malfunctions because of a disconnect between the intuitive rule *"do what you expect will bring about the best results"* and CDT's formal algorithm of *"holding fixed the agent's unconditional credences in dependency hypotheses."* Consider Egan's **Psychopath Button** thought experiment from the source text (Egan 2007; Greaves 2013):
* Paul is debating whether to press ($P$) or not press ($\neg P$) a "kill all psychopaths" button.
* Paul thinks it would be much better to live in a world with no psychopaths than in the status quo.
* However, Paul is quite confident that *only a psychopath* would press such a button, and he very strongly prefers living in a world with psychopaths to dying.

*Mathematical Analysis (Extending the Source):* Why does naive CDT fail here? Notice how the Psychopath Button differs from King David. In King David's problem, the background state (charisma) affected the baseline probability of revolt, but the *causal effect* of summoning Bathsheba ($+10$ utility, $0$ change in revolt probability) was the same in both states. In the Psychopath Button, the background state $S \in \{\text{Psych}, \neg\text{Psych}\}$ determines *what the action causally does to Paul*:
* If $S = \neg\text{Psych}$ (Paul is not a psychopath), pressing $P$ kills all psychopaths while Paul survives, yielding utility $+10$ (compared to $0$ for $\neg P$).
* If $S = \text{Psych}$ (Paul is a psychopath), pressing $P$ causes Paul's own death, yielding utility $-1,000$ (compared to $0$ for $\neg P$).

Suppose Paul initially believes he is almost certainly not a psychopath: $P(\text{Psych}) = 0.001$ and $P(\neg\text{Psych}) = 0.999$. If Paul holds these *unconditional* credences fixed in Equation (7), he computes:

$$U_{\text{CDT}}(P) = (0.999)(+10) + (0.001)(-1,000) = 9.99 - 1.00 = +8.99 > U_{\text{CDT}}(\neg P) = 0.$$

Naive CDT therefore endorses pressing the button! Yet if Paul finds himself inclined to press the button, that inclination is overwhelming evidence that $S = \text{Psych}$ (say, $P(\text{Psych} \mid \text{inclined to } P) = 0.99$), under which pressing the button is almost certain suicide.

### Deliberational Instability: Death in Damascus

A second pathology arises when the causal value of an action reverses upon learning what one is about to do. In the **Death in Damascus** scenario (Gibbard & Harper 1981; Harper 1984; Egan 2007; Meacham 2010), an anthropomorphic "Death" predicts where you will be tomorrow—either staying in Damascus ($A_D$) or fleeing to Aleppo ($A_A$)—and goes to wait for you there.

Let $\mathcal{S} = \{\hat{D}, \hat{A}\}$ denote Death's location, predicted with accuracy $p = 0.9$. Surviving yields utility $100$; meeting Death yields $0$. For any belief $q = P(\hat{D})$ about whether Death is waiting in Damascus, Equation (7) gives:

$$U_{\text{CDT}}(A_D) = 100(1 - q), \qquad U_{\text{CDT}}(A_A) = 100\,q.$$

Suppose you initially believe $q = 0.5$ and decide to flee to Aleppo ($A_A$). Once you form the intention to go to Aleppo, you have strong evidence that Death predicted this and is waiting in Aleppo, shifting your credence to $q = P(\hat{D} \mid \text{intend } A_A) = 0.1$. With $q = 0.1$, CDT immediately reverses its verdict: $U_{\text{CDT}}(A_D) = 90 > U_{\text{CDT}}(A_A) = 10$, advising you to stay in Damascus! Yet intending to stay in Damascus shifts $q$ to $0.9$, making Aleppo optimal again. Neither pure action is a stable fixed point of deliberation.

### Guaranteed Loss: The Adversarial Offer

Worse still, recent work by Jack Spencer (2020), Caspar Oesterheld and Vincent Conitzer (2021), and James Joyce (2020) shows that variants of Death in Damascus can force a CDT agent to voluntarily lose money. Consider Oesterheld and Conitzer's **Adversarial Offer**, quoted in the reference article:
* Two boxes (Box 1 and Box 2) are on offer. A buyer may purchase one ($A_1$ or $A_2$) or neither ($A_0$), but not both.
* Each box costs $\$1$.
* Yesterday, the seller put $\$3$ in each box that she predicted the buyer *not* to acquire. Both seller and buyer believe the seller's prediction is accurate with probability $0.75$.

*Mathematical Proof of CDT's Vulnerability (Unpacking the Source's Argument):* Why does the reference article state that *"CDT reasons that at least one box contains $\$3$. Therefore, the average box contains at least $\$1.50$ in causal expected value, which is more than the cost. Hence, CDT requires buying one of the two boxes"*?

Let the seller's three possible predictions be $\mathcal{S} = \{\hat{A}_0, \hat{A}_1, \hat{A}_2\}$, with arbitrary probabilities $(p_0, p_1, p_2)$ summing to $1$. Look at the gross monetary contents $(V_1, V_2)$ placed in Box 1 and Box 2 under each prediction:
* If $\hat{A}_0$ (predicted to buy *neither* box): neither box is predicted to be acquired, so the seller puts $\$3$ in *both* boxes: $(V_1, V_2) = (\$3, \$3)$.
* If $\hat{A}_1$ (predicted to buy Box 1): Box 2 is not acquired, so $(V_1, V_2) = (\$0, \$3)$.
* If $\hat{A}_2$ (predicted to buy Box 2): Box 1 is not acquired, so $(V_1, V_2) = (\$3, \$0)$.

Consequently, in *every* state of the world, the sum of the money inside the two boxes satisfies $V_1 + V_2 \ge \$3$. Subtracting the $\$1$ purchase price, the causal expected net payoffs of the three actions for *any* probability distribution $(p_0, p_1, p_2)$ are:

$$U_{\text{CDT}}(A_0) = \$0,$$

$$U_{\text{CDT}}(A_1) = 3(p_0 + p_2) - 1, \qquad U_{\text{CDT}}(A_2) = 3(p_0 + p_1) - 1.$$

Averaging the causal expected net utilities of $A_1$ and $A_2$ gives:

$$\frac{U_{\text{CDT}}(A_1) + U_{\text{CDT}}(A_2)}{2} = \frac{3(2p_0 + p_1 + p_2) - 2}{2} = \frac{3(1 + p_0) - 2}{2} = \$0.50 + \$1.50\,p_0 \ge +\$0.50.$$

Because the average of $U_{\text{CDT}}(A_1)$ and $U_{\text{CDT}}(A_2)$ is at least $+\$0.50$, it is mathematically impossible for both $U_{\text{CDT}}(A_1)$ and $U_{\text{CDT}}(A_2)$ to be $\le 0$. Regardless of what probabilities $(p_0, p_1, p_2)$ the buyer assigns to the seller's predictions, **CDT strictly forbids choosing $A_0$ (buying neither box)**!

Yet if the buyer follows CDT and purchases a box (say $A_i$), the seller has anticipated $A_i$ with probability $0.75$, leaving Box $i$ empty $75\%$ of the time. The buyer's actual expected payoff from buying Box $i$ is:

$$(0.25)(\$3) + (0.75)(\$0) - \$1 = -\$0.25 < \$0.$$

The seller reliably extracts $\$0.25$ in expectation from the causal decision theorist.

### Operational Refinement: Deliberational CDT and Ratifiability

How should a defender of CDT respond to these counterexamples? As the reference article notes, James Joyce (2012, 2020; see also Weirich 2016 and Harper 1984) argues that CDT is not committed to holding fixed *initial* unconditional credences in dependency hypotheses; rather, CDT is naturally capable of taking into account *"information about what one is inclined or likely to do as evidence."*

*Operational Proposal (Our Formalization of Joyce's and Harper's Defense):* We can formalize Joyce's insight by distinguishing between **ex-ante (naive) CDT** and **deliberational (evidentially updated) CDT**. During deliberation, an agent can observe their own current behavioral inclination or intention $I_{A^*}$ to perform action $A^*$. Because $I_{A^*}$ is a piece of self-locating evidence available *before* the action is executed, the agent should update their credences over the dependency hypotheses from $P(S_k)$ to $P(S_k \mid I_{A^*})$, and then evaluate the causal expected utility of any candidate action $A \in \mathcal{A}$ holding fixed that updated distribution:

$$U_{\text{CDT}}(A \mid I_{A^*}) = \sum_{k=1}^{m} P(S_k \mid I_{A^*}) \sum_{j} P(O_j \mid A, S_k) D(O_j). \tag{9}$$

Following William Harper (1984), we say that an action $A^*$ is **ratifiable** if it maximizes causal expected utility given the evidence that the agent intends to perform $A^*$:

$$A^* \in \arg\max_{A \in \mathcal{A}} U_{\text{CDT}}(A \mid I_{A^*}). \tag{10}$$

Let us see how Equations (9) and (10) perform across our counterexamples:
1. **Psychopath Button Solved:** If Paul feels inclined to press the button ($I_P$), he updates his credence that he is a psychopath to $P(\text{Psych} \mid I_P) = 0.99$. Plugging this into Equation (9) yields:
   $$U_{\text{CDT}}(P \mid I_P) = (0.01)(+10) + (0.99)(-1,000) = -989.90 < U_{\text{CDT}}(\neg P \mid I_P) = 0.$$
   Pressing the button is unratifiable, whereas not pressing ($\neg P$) is uniquely ratifiable ($U_{\text{CDT}}(\neg P \mid I_{\neg P}) = 0$). Deliberational CDT cleanly avoids disaster.
2. **Death in Damascus and Mixed Strategies:** When no pure action satisfies (10), the agent recognizes that any deterministic intention is self-defeating. Under standard game-theoretic extensions of ratifiability, if the agent can randomize with probability $r = 0.5$ between Damascus and Aleppo, the mixed strategy equalizes $U_{\text{CDT}}(A_D \mid I_{\text{mix}}) = U_{\text{CDT}}(A_A \mid I_{\text{mix}}) = 50$, restoring a ratifiable equilibrium.
3. **Why the Adversarial Offer Remains a Deep Challenge:** Remarkably, Equation (9) does *not* rescue CDT in the Adversarial Offer! Even if the buyer forms the inclination $I_{A_0}$ to buy neither box and updates to $p_0 = P(\hat{A}_0 \mid I_{A_0}) = 0.75$, Equation (9) tells the buyer that both boxes very likely contain $\$3$, so $U_{\text{CDT}}(A_1 \mid I_{A_0}) > 0$ and $A_0$ is unratifiable. Conversely, if the buyer intends $I_{A_1}$ ($p_1 = 0.75$), Box 1 has negative expected value ($-\$0.25$), but Box 2 now has high expected value ($+\$1.25$), tempting the buyer to switch to $A_2$. Even if the buyer randomizes $50/50$ between $A_1$ and $A_2$, they still pay $\$1$ to play a losing game whenever the seller predicts that they will buy *some* box. This demonstrates why Oesterheld and Conitzer's money-extraction results represent a genuine frontier in contemporary decision theory.

---

## 6. Conclusion

Causal decision theory rests on a foundational insight: rational agency is about intervening on the world, not curating one's evidence about the past. By replacing standard conditional probabilities $P(O_j \mid A)$ with counterfactual probabilities $P(A \to O_j)$—and operationalizing those counterfactuals by averaging over causally independent dependency hypotheses $S_k$—CDT provides a mathematically rigorous prescription that avoids the diagnostic fallacies of evidential decision theory in confounding scenarios like King David and Bathsheba.

At the same time, our mathematical tour shows why CDT remains an active research subject rather than a closed chapter. When background states interact with the causal efficacy of an action (as in the Psychopath Button), an agent must combine causal counterfactuals with self-locating deliberative evidence via Equation (9) and the criterion of ratifiability. And when an agent faces an adversarial predictor across multiple options (as in Newcomb's problem, Death in Damascus, and the Adversarial Offer), the tension between local causal dominance and global predictive correlation forces decision theorists to confront the deepest questions about rationality, predictability, and agency.

---

## References

* Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
* Egan, A. (2007). "Some counterexamples to causal decision theory." *The Philosophical Review*, 116(1), 93–114.
* Gibbard, A., & Harper, W. L. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190).
* Greaves, H. (2013). "Epistemic decision theory." *Mind*, 122(488), 915–952.
* Harper, W. (1984). "Ratifiability and Causal Decision Theory: Comments on Eells and Seidenfeld." *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1984(2), 213–228.
* Howard, J. V. (1988). "Cooperation in the Prisoner's Dilemma." *Theory and Decision*, 24(3), 203–213.
* Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese*, 187(1), 123–145.
* Joyce, J. M. (2020). "Yet Another Refutation of Causal Decision Theory?" Working paper, University of Michigan.
* Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *The Philosophical Review*, 85(3), 297–315.
* Lewis, D. (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy*, 59(1), 5–30.
* Meacham, C. J. G. (2010). "Binding and its consequences." *Philosophical Studies*, 149(1), 49–71.
* Oesterheld, C., & Conitzer, V. (2021). "Extracting Money from Causal Decision Theorists." *The Philosophical Quarterly*, 71(4), pqaa086.
* Shaffer, M. J. (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines*, 19(1), 61–92.
* Spencer, J. (2020). "An argument against causal decision theory." *Analysis*, 81, 52–61.
* Weirich, P. (2016). "Causal Decision Theory." In E. N. Zalta (Ed.), *Stanford Encyclopedia of Philosophy* (Winter 2016 ed.).
* Wolpert, D. H., & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese*, 190(9), 1637–1646.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Task**

I'm zeroing in on defining the scope: A mathematical exposition of Causal Decision Theory, suitable for those with strong math skills and an interest in applying the theory. The goal is a formal explanation, not a casual introduction, for the target audience.


**Clarifying Scope & Approach**

I'm now integrating philosophical motivation alongside defining a rigorous framework for applying Causal Decision Theory (CDT). I'll carefully use the Wikipedia reference as a base while developing an operational system for readers. I'll need to clarify open questions about computing counterfactual probabilities, dependency hypotheses, and ratifiability, distinguishing source claims from my additional mathematical formulations. The target length is ~2,400–3,000 words. My analysis also now defines CDT as choosing the action that *causes* the best outcome, contrasting it with EDT, which uses evidential "news".


**Analyzing Causal Effects**

Now, I'm diving deeper into causal effects with a specific example: the apple versus orange scenario. I'm articulating both an informal description and a formal mathematical definition. Gibbard & Harper's (1981) formula is central, with $U(A)$ representing the utility of action $A$. I'm also highlighting the crucial distinction between CDT and EDT, pointing to Lewis's (1976) triviality result.


**Examining Independence Conditions**

I'm now focusing on the statistical independence requirement and its limitations, illustrated through the King David and Bathsheba counterexample, followed by an overview of the philosophers' preference for CDT over EDT. I'm also planning to incorporate thought experiments, specifically Newcomb's Paradox and the Prisoner's Dilemma with a twin, in this section.


**Addressing Computational Limits**

I'm now grappling with CDT's practical limitations. It doesn't offer a specific algorithm for calculating $P(A \to O_j)$. Imaging, Lewis's suggestion, creates a regress. Furthermore, there's a disconnect in CDT between what is supposed to bring the best outcome, and the algorithm of holding fixed initial unconditional credences in "dependency hypotheses". I'm exploring counterexamples like the "Death in Damascus" scenario, highlighting the instability with correlation, as well as the adversarial offer thought experiment, and its implications for money extraction.


**Structuring the Essay**

I'm now outlining the essay's organization to ensure a mathematically rigorous and applicable guide. The current title leans toward "Counterfactuals, Interventions, and Rational Choice: A Mathematical Guide to Causal Decision Theory." I'm planning to include examples that highlight CDT's potential pitfalls, like the box-buying scenario, and problematic edge cases like the Psychopath Button. The defense provided by Joyce, Weirich, and Wedgwood will also be added for completeness.


**Introducing the Debate**

I'm now writing an introduction laying out the fork in decision theory, the core problem of rational choice under uncertainty, and the distinction between EDT and CDT using a source's examples. I will introduce the basic intuition of decision theory with the "good/bad apple" example, formalizing it into a decision matrix. Then, I plan to discuss Gibbard–Harper's equation and contrasting EDT's conditional-probability expected utility. I will explain the distinction using a mathematical exposition of the source.


**Deriving an Equivalence**

I'm now focusing on deriving the Gibbard–Harper equivalence. I'm starting with the two axioms, Conditional Excluded Middle and Modus Ponens, and proving how statistical independence guarantees the result, $P(A \to O_j) = P(O_j \mid A)$. I'm explicitly noting which parts are from the source and adding my own algebraic derivations for a clear and rigorous presentation.


**Developing a Formal Algorithm**

I'm now formulating a specific algorithm, extending the source's framework. My objective is to create a step-by-step mathematical procedure. I'm focusing on defining background states for causal independence and then applying this to work out the examples. I'll need to clearly show how the $P(A \to O_j)$ equation can be applied in the algorithm.


**Illustrating Examples**

I'm now integrating illustrative examples. I'm formalizing scenarios to clarify EDT versus CDT. I'm highlighting the numerical aspects in "King David and Bathsheba," setting up state spaces and showing why CDT recommends the correct action. I am also calculating the precise expected values in "Newcomb's Paradox and the Twin Prisoner's Dilemma," underscoring the dominance reasoning of CDT, and briefly showing the isomorphism to the Twin Prisoner's Dilemma.


**Exploring Counterexamples**

I'm now focusing on a deeper analysis of counterexamples, specifically the "Psychopath Button", "Death in Damascus", and "Adversarial Offer" scenarios. I'm mathematically exploring each, focusing on the instability issues and self-referential causal hazards these present. I'm working to show how CDT, in specific situations, can be misapplied, especially when considering an agent's own intentions.


**Analyzing the Paradox**

I'm now deep-diving into the two-box scenario from the source to illustrate CDT's vulnerabilities. I'm unpacking Joyce's defense, differentiating *naive* from *ratified* CDT. I need to explain how CDT can, paradoxically, lead to sure losses in specific circumstances, when there are negatively correlated predictions between boxes. I'm exploring the implications for the agent's actions and intentions.


**Synthesizing Counterfactuals**

I'm working on the refined CDT utility, using credences conditioned on deliberative inclination, $I_A$, to provide a specific mathematical fix for the "Psychopath Button," while clarifying the enduring importance of Newcomb's Problem and the Adversarial Offer. I'm also preparing a brief conclusion, and compiling the references list. Word count is being monitored to maintain the target range.


**Refining Derivations**

I'm now honing the mathematical precision of my arguments, ensuring each derivation is clear and rigorous. I'm focusing specifically on the Adversarial Offer scenario, meticulously unpacking the expected values from the source's description. The goal is to mathematically demonstrate how CDT's approach leads to an advantageous outcome for the seller, in the scenario.


**Calculating Expected Values**

I'm now calculating the expected values for the "Adversarial Offer" in detail, and formally defining the expected value the buyer could receive for each of their three possible actions. I've focused on ensuring the model's structure is fully defined to ensure the result is clear. The key is in determining the initial credences and how those are updated.


**Calculating Box Values**

I'm now focusing on calculating the causal expected values of the boxes in the adversarial offer example. I'm unpacking the mathematical details from the source to rigorously show the advantages of CDT. I am developing an algorithm and model to illustrate that CDT always results in a positive expected value, thus illustrating its superiority.


```
