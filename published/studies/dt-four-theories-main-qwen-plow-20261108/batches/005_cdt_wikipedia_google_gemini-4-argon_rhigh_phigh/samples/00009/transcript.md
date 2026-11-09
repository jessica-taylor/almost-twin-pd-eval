# 005_cdt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00009

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/83e7c008-9e1d-47e9-b856-cef1d5d2c6dc/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/83e7c008-9e1d-47e9-b856-cef1d5d2c6dc/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Counterfactuals, Interventions, and Rational Choice: A Mathematical Account of Causal Decision Theory

When a rational agent chooses among competing actions, every option plays a dual role. On one hand, an action is a physical **intervention** in the world—a lever pulled to bring about desirable future states. On the other hand, an action is a piece of **evidence** about the agent—a symptom of the prior beliefs, character traits, or neurological states that led the agent to choose it. 

In most everyday decisions, these two roles align: the actions that serve as the best evidence of a good outcome are precisely those that causally produce it. As noted in the reference text, if eating a good apple causes happiness, eating a bad apple causes sadness, and eating an orange causes sadness, an agent uncertain of the apple's quality evaluates the decision by weighing three quantities: the probability that the apple is good or bad, the utility of eating a good apple, and the disutility of eating a bad one. Because the act of eating the apple neither causes nor provides evidence about whether the apple was already rotten on the tree, expected causal value and expected evidential value coincide.

However, when the state of the world and the agent's choice share a common cause—or when another agent has accurately predicted the choice beforehand—intervention and evidence pull apart. **Causal decision theory** (CDT) is the school of thought within decision theory holding that rational choice must be governed exclusively by the expected *causal* consequences of an action. This contrasts sharply with **evidential decision theory** (EDT), which advises an agent to select the action that would be most indicative of a good outcome if the agent received the "news" that they had taken it (Ahmed 2021). While philosophical debate between the two camps remains active, philosophers generally favor CDT when forced to choose between them (Weirich 2016).

This essay provides a rigorous mathematical account of CDT, examining how it evaluates alternative actions, how it handles statistical dependencies and counterfactuals, and where its foundational definitions leave open operational questions. To equip the reader to analyze unfamiliar decision problems, we will supplement the core framework from the literature with explicit algebraic derivations and an operational procedure for computing causal expected utility—carefully distinguishing claims established in the reference text from our own mathematical reconstructions and extensions.

---

## 1. The Formal Architecture of CDT and EDT

To formalize a decision problem, let $\mathcal{A} = \{A_1, A_2, \dots, A_m\}$ be a finite set of mutually exclusive actions available to an agent, and let $\mathcal{O} = \{O_1, O_2, \dots, O_n\}$ be a finite partition of mutually exclusive and exhaustive outcomes. The agent's preferences over outcomes are represented by a real-valued desirability (or utility) function $D: \mathcal{O} \to \mathbb{R}$, and the agent's epistemic state is represented by a probability measure $P$.

In a foundational 1981 paper, Allan Gibbard and William Harper formulated causal decision theory as the maximization of expected utility $U(A)$ calculated from the probabilities of **counterfactual conditionals** (Gibbard and Harper 1981):

$$U(A) = \sum_{j=1}^{n} P(A \to O_j) D(O_j)$$

Here, $D(O_j)$ is the desirability of outcome $O_j$, and $A \to O_j$ denotes the subjunctive or counterfactual conditional proposition: *"If the agent were to perform action $A$, then outcome $O_j$ would occur"* (rendered in the reference text as the counterfactual probability that $A$ necessarily implies $O_j$). 

By contrast, evidential decision theory evaluates an action $A$ using standard conditional probabilities:

$$V(A) = \sum_{j=1}^{n} P(O_j \mid A) D(O_j), \quad \text{where } P(O_j \mid A) = \frac{P(A \land O_j)}{P(A)}$$

### Lewis's Triviality Result and the Divergence of $U(A)$ and $V(A)$

At first glance, it is tempting to equate the probability of the conditional, $P(A \to O_j)$, with the conditional probability, $P(O_j \mid A)$. If the identity $P(A \to O_j) = P(O_j \mid A)$ held universally, CDT and EDT would be mathematically identical.

However, as the reference article highlights, David Lewis (1976) proved a celebrated **triviality result** demonstrating that no genuine conditional arrow $\to$ can satisfy $P(A \to O_j) = P(O_j \mid A)$ across any non-trivial class of probability functions closed under conditionalization. Specifically, Lewis showed that if a class of probability functions is closed under conditionalizing, no probability conditional exists for that class unless every probability function in it is *trivial*—meaning it never assigns positive probability to more than two incompatible alternatives, and is therefore at most four-valued.

Why do the two quantities diverge? The conditional probability $P(O_j \mid A)$ measures how the agent's belief in $O_j$ updates upon *observing* or *learning* that $A$ is true. Updating on $A$ transmits diagnostic information backward through causal pathways to common causes of $A$ and $O_j$. By contrast, $P(A \to O_j)$ is meant to track only what $A$ would *bring about* in the forward causal direction.

### When Do CDT and EDT Agree? The Gibbard–Harper Equivalence Condition

Although $P(A \to O_j)$ and $P(O_j \mid A)$ differ in general, Gibbard and Harper (1981) proved that under two logical axioms governing the conditional arrow $\to$, a simple probabilistic condition guarantees their equality: the **statistical independence** of the act $A$ and the counterfactual conditional $A \to O_j$.

The reference text notes this theorem and mentions that one of the two axioms is related to the controversial **Principle of Conditional Excluded Middle (CEM)** (Shaffer 2009). To make the mechanics of this result transparent for practical application, we provide an explicit mathematical reconstruction of how these axioms yield the equivalence.

*(Mathematical Reconstruction)* Let the propositions in our decision model form a Boolean algebra equipped with the counterfactual connective $\to$. The two axioms invoked by Gibbard and Harper are:

1. **Conditional Excluded Middle (CEM) and Consistency:** For any possible action $A$ and outcome $O_j$, either $A$ would bring about $O_j$ or $A$ would bring about $\neg O_j$, and not both:
   $$(A \to O_j) \lor (A \to \neg O_j) \quad \text{and} \quad \neg\big((A \to O_j) \land (A \to \neg O_j)\big)$$
   Because the outcomes $\{O_1, \dots, O_n\}$ partition the outcome space, CEM ensures that the propositions $\{A \to O_1, \dots, A \to O_n\}$ form a measurable partition of the probability space, so that $\sum_{j=1}^n P(A \to O_j) = 1$.

2. **Modus Ponens (or Weak Centering):** In any possible world where action $A$ is actually performed, the counterfactual $A \to O_j$ has the exact same truth value as the actual outcome $O_j$:
   $$\big(A \land (A \to O_j)\big) \leftrightarrow (A \land O_j)$$

From Axiom 2, because the conjunctions $A \land (A \to O_j)$ and $A \land O_j$ are logically equivalent events, they must have identical probabilities:

$$P\big(A \land (A \to O_j)\big) = P(A \land O_j)$$

Assuming $P(A) > 0$, we divide both sides by $P(A)$ and apply the definition of conditional probability:

$$P(A \to O_j \mid A) = \frac{P\big(A \land (A \to O_j)\big)}{P(A)} = \frac{P(A \land O_j)}{P(A)} = P(O_j \mid A)$$

Now suppose that the action $A$ and the counterfactual conditional $A \to O_j$ are statistically independent, meaning $P(A \to O_j \mid A) = P(A \to O_j)$. Substituting this into the equation above immediately yields:

$$P(A \to O_j) = P(O_j \mid A)$$

Consequently, whenever an agent's choice of action gives no diagnostic information about which counterfactual mapping $A \to O_j$ holds in the world, CDT and EDT prescribe the exact same action. They diverge precisely when $P(A \to O_j \mid A) \neq P(A \to O_j)$.

---

## 2. Diagnostic Actions and Common Causes: Classic Applications

To see how the failure of independence between $A$ and $A \to O_j$ operates in practice, let us examine two canonical cases from the reference text: a common-cause confounding problem (King David and Bathsheba) and a predictive correlation problem (Newcomb's paradox).

### Case 1: King David and Bathsheba (Common-Cause Confounding)

Gibbard and Harper (1981) illustrate the divergence of CDT and EDT with a historical parable. King David desires to summon Bathsheba, another man's wife, but fears provoking a successful revolt. From his studies in political science and psychology, David knows the following causal structure:
* Kings possess one of two fixed personality types determined by genetics and early childhood: **charismatic** ($C$) or **uncharismatic** ($\neg C$). This trait cannot be altered in adulthood.
* Charismatic kings tend to act justly, whereas uncharismatic kings tend to act unjustly. Summoning Bathsheba ($S$) is an unjust act; abstaining ($\neg S$) is just.
* Successful revolts ($R$) against charismatic kings are rare, whereas revolts against uncharismatic kings are frequent. Crucially, *unjust acts themselves do not cause revolts*—uncharismatic kings suffer revolts solely because of their sneaky, ignoble bearing.

Let us parameterize this qualitative story from the source with concrete numbers (our illustrative assignment) to see how the formulas behave. Suppose David initially assigns probability $P(C) = 0.5$ to being charismatic. Suppose further that whether a revolt occurs depends strictly on charisma, such that for simplicity a revolt occurs if and only if David is uncharismatic ($R \leftrightarrow \neg C$), or with fixed probabilities conditioned on charisma: say, $P(R \mid C) = 0.1$ and $P(R \mid \neg C) = 0.9$, entirely unaffected by $S$. Finally, suppose David assigns diagnostic probabilities to his own actions given his type: $P(S \mid C) = 0.1$ and $P(S \mid \neg C) = 0.9$.

Let the outcomes be the four combinations of whether Bathsheba is summoned and whether a revolt occurs, with desirabilities driven by a reward $b = 10$ for being with Bathsheba and a severe penalty $c = -100$ for a revolt:
* $O_1 = S \land \neg R$: $D(O_1) = 10$
* $O_2 = S \land R$: $D(O_2) = 10 - 100 = -90$
* $O_3 = \neg S \land \neg R$: $D(O_3) = 0$
* $O_4 = \neg S \land R$: $D(O_4) = -100$

**The Evidential Calculation:** By Bayes' theorem, because $P(C) = P(\neg C) = 0.5$, learning that David summons Bathsheba updates the probability that he is uncharismatic to $P(\neg C \mid S) = 0.9$. Consequently, the conditional probability of a revolt given $S$ is:

$$P(R \mid S) = P(R \mid C)P(C \mid S) + P(R \mid \neg C)P(\neg C \mid S) = (0.1)(0.1) + (0.9)(0.9) = 0.82$$

Similarly, $P(R \mid \neg S) = (0.1)(0.9) + (0.9)(0.1) = 0.18$. Plugging these into the EDT formula yields:

$$V(S) = (1 - 0.82)(10) + (0.82)(-90) = 1.8 - 73.8 = -72$$

$$V(\neg S) = (1 - 0.18)(0) + (0.18)(-100) = -18$$

Since $V(\neg S) > V(S)$, EDT advises David to abstain from summoning Bathsheba—effectively telling him to manage the news about his own unalterable genetic temperament.

**The Causal Calculation:** CDT recognizes that summoning Bathsheba has zero causal effect on whether a revolt occurs. The unconditional probability of revolt is $P(R) = (0.5)(0.1) + (0.5)(0.9) = 0.50$. Thus, the counterfactual probabilities are $P(S \to O_1) = 0.50$, $P(S \to O_2) = 0.50$, $P(\neg S \to O_3) = 0.50$, and $P(\neg S \to O_4) = 0.50$. The causal expected utilities are:

$$U(S) = (0.50)(10) + (0.50)(-90) = -40$$

$$U(\neg S) = (0.50)(0) + (0.50)(-100) = -50$$

Since $U(S) > U(\neg S)$ by exactly the value of Bathsheba's company ($+10$), CDT recommends summoning her. Here, $S$ and $S \to R$ fail to be independent because $S$ is diagnostically correlated with the pre-existing state $\neg C$ that makes $S \to R$ true.

### Case 2: Newcomb's Paradox and the Twin Prisoner's Dilemma

The exact same structural divergence drives **Newcomb's paradox** (Wolpert and Benford 2013; Gibbard and Harper 1981). An agent faces two boxes: transparent Box A, which visibly contains $\$1,000$, and opaque Box B, whose contents were already set yesterday by a predictor with $99\%$ accuracy. The agent may either take both boxes ($A_2$, "two-boxing") or take only Box B ($A_1$, "one-boxing"). If the predictor predicted $A_1$, Box B contains $\$1,000,000$; if the predictor predicted $A_2$, Box B contains $\$0$.

Let $M$ denote the state in which Box B contains $\$1,000,000$, and $\neg M$ the state in which it is empty. Assuming desirability is linear in dollars:

| State of Box B | One-Box ($A_1$) | Two-Box ($A_2$) |
| :--- | :---: | :---: |
| **$M$ (Predictor predicted $A_1$)** | $\$1,000,000$ | $\$1,001,000$ |
| **$\neg M$ (Predictor predicted $A_2$)** | $\$0$ | $\$1,000$ |

EDT evaluates the choice using $P(M \mid A_1) = 0.99$ and $P(M \mid A_2) = 0.01$:

$$V(A_1) = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000$$

$$V(A_2) = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000$$

EDT therefore recommends one-boxing ($A_1$).

CDT, by contrast, notes that the predictor's action lies in the immutable past. Whether Box B contains $\$1,000,000$ ($M$, with some prior probability $p = P(M)$) or $\$0$ ($\neg M$, with probability $1-p$) cannot be causally altered by the agent's hand movement today. Hence:

$$U(A_1) = p(\$1,000,000) + (1-p)(\$0) = \$1,000,000p$$

$$U(A_2) = p(\$1,001,000) + (1-p)(\$1,000) = \$1,000,000p + \$1,000$$

For *every* prior $p \in [0, 1]$, $U(A_2) - U(A_1) = \$1,000 > 0$. By strict causal dominance, CDT recommends taking both boxes. As David Lewis (1979) demonstrated, an isomorphic structure arises in the **Prisoner's Dilemma** played against a psychological "twin" whose choice to cooperate or defect strongly correlates with, but is not caused by, one's own choice (Howard 1988): CDT recommends defecting because one's choice cannot causally alter the twin's move, whereas EDT can recommend cooperating if the correlation is sufficiently high.

---

## 3. Resolving the Vagueness Problem: Operationalizing Counterfactual Probabilities

While the philosophical intuition behind $P(A \to O_j)$ is clear in simple dominance cases, the reference text points out a major theoretical vulnerability: **vagueness** (Shaffer 2009). Gibbard and Harper's formula does not by itself specify a general mathematical algorithm for computing the counterfactual probabilities $P(A \to O_j)$ in arbitrary decision problems.

### Lewis's Imaging and the Epistemic Regress

One formal proposal cited in the reference text is the **imaging** technique developed by David Lewis (1981). Let $W$ be a set of possible worlds equipped with a similarity metric, and let $P$ be a probability distribution over $W$. Under Lewis's semantics for counterfactuals (assuming CEM holds so that a unique closest world exists), for each world $w \in W$ and possible action $A$, there is a single closest possible world $w_A \in W$ in which $A$ is true.

To evaluate $P(A \to O_j)$ by imaging on $A$, one shifts the probability mass $P(w)$ of each world $w$ directly to its closest $A$-world $w_A$, defining a new probability function $P^A$:

$$P^A(w') = \sum_{\{w \in W \mid w_A = w'\}} P(w)$$

The counterfactual probability is then simply the total imaged probability of the worlds where $O_j$ holds:

$$P(A \to O_j) = P^A(O_j) = \sum_{\{w \in W \mid w_A \models O_j\}} P(w)$$

Unlike Bayesian conditionalization—which deletes the probability mass of $\neg A$-worlds and normalizes the remainder uniformly—imaging *conserves* probability mass by migrating it across world-lines to the nearest $A$-worlds, leaving causally independent background facts intact.

However, as Michael Shaffer (2009) observes in the reference text, applying imaging directly as a decision procedure runs into a serious difficulty: to know which world $w_A$ is closest to $w$, an agent must know what would be true—and what they would believe—if they were certain of $A$. Yet "what I would believe if I were certain of $A$" is itself a counterfactual conditional to which a fallible agent might assign probability less than $1$. Attempting to evaluate that higher-order conditional requires another round of imaging, threatening an infinite epistemic regress.

### Operational Synthesis: Dependency Hypotheses and Causal Interventions

How can a decision-maker bypass this regress and compute $U(A)$ in unfamiliar cases? While the reference text leaves this algorithmic question open as a criticism of the pure Gibbard–Harper formulation, it also alludes (via Andy Egan's 2007 critique) to the standard operational device used in modern CDT: partitioning the world into **dependency hypotheses**.

*(Operational Proposal and Justification)* To turn CDT into an explicit, regress-free algorithm for applied modeling, we can replace abstract possible-world similarity with a finite partition of causal background states—a method originally developed by Brian Skyrms, David Lewis, and James Joyce, and closely linked to Judea Pearl's structural causal models.

**Definition (Dependency Hypotheses):** A set of propositions $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$ is a partition of *dependency hypotheses* if the $K_i$ are mutually exclusive and exhaustive ($\sum_{i=1}^r P(K_i) = 1$) and each $K_i$ is a maximally specific specification of how outcomes causally depend on actions. Mathematically, conditional on any single dependency hypothesis $K_i$ and action $A$, the probability of outcome $O_j$ is purely a matter of objective physical chance (or deterministic necessity) that is completely unaffected by why the agent chose $A$.

In the deterministic case, each $K_i$ specifies a response function $f_i: \mathcal{A} \to \mathcal{O}$ mapping each action $A$ to a unique outcome $O_j = f_i(A)$. In the stochastic case, each $K_i$ specifies objective transition probabilities $P(O_j \mid A \land K_i)$ representing the causal propensity of $A$ to produce $O_j$ when the causal background is $K_i$. Because $K_i$ holds fixed all common causes and background mechanisms, within each $K_i$ the action $A$ and the conditional $A \to O_j$ are independent:

$$P(A \to O_j \mid K_i) = P(O_j \mid A \land K_i)$$

By the law of total probability, the counterfactual probability $P(A \to O_j)$ decomposes into an expectation over the unconditional probabilities of the dependency hypotheses:

$$P(A \to O_j) = \sum_{i=1}^{r} P(K_i) P(A \to O_j \mid K_i) = \sum_{i=1}^{r} P(K_i) P(O_j \mid A \land K_i)$$

Substituting this into Gibbard and Harper's formula yields the **Partition Formula for Causal Expected Utility**:

$$U(A) = \sum_{i=1}^{r} P(K_i) \sum_{j=1}^{n} P(O_j \mid A \land K_i) D(O_j)$$

For readers familiar with graphical causal inference, this expression is identical to Pearl's back-door adjustment formula for an intervention $\text{do}(A)$ when $\mathcal{K}$ represents the set of background confounders (parents of $A$ in a directed acyclic graph): $P(A \to O_j) = P(O_j \mid \text{do}(A))$. 

This provides a concrete **Four-Step Operational Procedure** for applying CDT to any unfamiliar decision problem:
1. **Separate Causal States from Evidential Signals:** Identify all background variables (past predictions, genetic traits, unobserved environmental states) that are causally upstream of or causally unaffected by the present action $A$.
2. **Construct the Partition $\mathcal{K}$:** Form the mutually exclusive states $K_1, \dots, K_r$ generated by these causally independent background variables, and assign unconditional credences $P(K_i)$ based on all evidence available *prior* to deciding.
3. **Specify Forward Transition Probabilities:** For each pair $(K_i, A)$, determine the causal transition probability $P(O_j \mid A \land K_i)$ (which is $1$ or $0$ in deterministic models).
4. **Compute $U(A)$ Holding $P(K_i)$ Fixed:** Weight the expected utility of $A$ in each state $K_i$ by the *unconditional* probability $P(K_i)$—deliberately refusing to replace $P(K_i)$ with the diagnostic conditional probability $P(K_i \mid A)$—and select $\arg\max_{A \in \mathcal{A}} U(A)$.

Notice how this operationalizes the contrast with EDT. Written in terms of the same partition $\mathcal{K}$, EDT's formula is:

$$V(A) = \sum_{i=1}^{r} P(K_i \mid A) \sum_{j=1}^{n} P(O_j \mid A \land K_i) D(O_j)$$

The entire mathematical dispute between CDT and EDT reduces to a single question: should we weight the dependency hypotheses by their unconditional credences $P(K_i)$ or by the act-conditional credences $P(K_i \mid A)$?

---

## 4. Pathologies of Fixed Credences: Act-State Dependence and Instability

While the partition formula solves the vagueness problem by holding unconditional credences $P(K_i)$ fixed across all actions $A$, this very feature has become the target of modern counterexamples. As the reference text notes, Andy Egan (2007) argues that holding fixed the agent's unconditional credences in dependency hypotheses creates a fundamental disconnect between CDT's formal algorithm and the intuitive rule *"do what you expect will bring about the best results."* Similarly, recent game-theoretic results by Caspar Oesterheld and Vincent Conitzer (2021) and Jack Spencer (2020) show that standard CDT agents can be induced to voluntarily lose money.

Let us analyze the three distinct mathematical mechanisms underlying these counterexamples in the reference text, and then formulate the operational refinement proposed by CDT's defenders.

### 1. Asymmetric Causal Efficacy: The Psychopath Button

In Egan's (2007) **Psychopath Button** thought experiment (also analyzed by Greaves 2013), Paul is debating whether to press ($P$) or not press ($\neg P$) a "kill all psychopaths" button. Paul believes it would be much better to live in a world without psychopaths than with them, but he strongly prefers living in a world with psychopaths to dying himself. Crucially, Paul is initially very confident that he is not a psychopath, yet he is also highly confident that *only a psychopath would press such a button*.

Let us formalize this using our partition procedure (our mathematical parameterization of Egan's scenario). The dependency hypotheses are $K_{\text{sane}}$ (Paul is not a psychopath; pressing kills all psychopaths and leaves Paul alive) and $K_{\text{psy}}$ (Paul is a psychopath; pressing kills all psychopaths *including Paul*).
* **Desirabilities:** Living in a psychopath-free world: $D(\text{Live Free}) = 10$; status quo (living with psychopaths): $D(\text{Status Quo}) = 0$; dying: $D(\text{Dead}) = -1000$.
* **Unconditional Credences:** Before deciding, Paul is confident he is sane: $P(K_{\text{sane}}) = 0.999$ and $P(K_{\text{psy}}) = 0.001$.
* **Diagnostic Credences:** Conditional on pressing the button, Paul is almost certainly a psychopath: $P(K_{\text{psy}} \mid P) = 0.99$.

Applying standard CDT by holding $P(K_i)$ fixed at their unconditional values yields:

$$U(P) = P(K_{\text{sane}}) D(\text{Live Free}) + P(K_{\text{psy}}) D(\text{Dead}) = (0.999)(10) + (0.001)(-1000) = 9.99 - 1.00 = +8.99$$

$$U(\neg P) = P(K_{\text{sane}}) D(\text{Status Quo}) + P(K_{\text{psy}}) D(\text{Status Quo}) = 0$$

Because $U(P) > U(\neg P)$, standard CDT instructs Paul to press the button! Why does this differ so sharply from Newcomb's problem? In Newcomb's problem, two-boxing dominates one-boxing in *every* dependency hypothesis ($M$ and $\neg M$). In the Psychopath Button, there is no dominant action: pressing is better in $K_{\text{sane}}$ ($+10 > 0$) but catastrophic in $K_{\text{psy}}$ ($-1000 < 0$). Because choosing $P$ is overwhelming evidence that the world is in state $K_{\text{psy}}$, evaluating $P$ using the prior $P(K_{\text{sane}}) = 0.999$ ignores critical evidence about *what causal effect the button will actually have* when Paul presses it.

### 2. Deliberative Instability: Death in Damascus

In **Death in Damascus** (Gibbard and Harper 1981; Egan 2007; Harper 1984; Meacham 2010), an agent in Damascus must decide whether to stay in Damascus ($A_D$) or flee to Aleppo ($A_A$). Death, a reliable predictor with accuracy $p = 0.99$, has already predicted the agent's decision and gone to wait in the predicted city. Being in the same city as Death results in death ($D = 0$); being in the other city results in survival ($D = 100$).

Let $K_D$ be the dependency hypothesis that Death is waiting in Damascus, and $K_A$ that Death is in Aleppo:

$$U(A_D) = 100 P(K_A), \qquad U(A_A) = 100 P(K_D)$$

Suppose the agent starts with $P(K_D) > 0.5$. Then $U(A_A) > U(A_D)$, so CDT recommends fleeing to Aleppo ($A_A$). However, as soon as the agent forms the intention to flee to Aleppo, they know that Death—being $99\%$ accurate—almost certainly predicted $A_A$, forcing the agent's credence in $K_A$ up to $P(K_A) = 0.99$ and $P(K_D) = 0.01$. At that instant, recomputing CDT with the updated credences yields $U(A_D) = 99 > U(A_A) = 1$, so CDT now demands staying in Damascus! Every pure action is self-undermining: intending $A_D$ makes $A_A$ causally superior, and intending $A_A$ makes $A_D$ causally superior.

### 3. Guaranteed Financial Loss: The Adversarial Offer

Building on Death in Damascus, Oesterheld and Conitzer (2021) (alongside related work by Spencer 2020 and Joyce 2020) show that an adversary can exploit this structure to extract money from a standard CDT agent without relying on deliberative flip-flopping. Consider their **Adversarial Offer** described in the reference text:
* Two boxes, Box 1 and Box 2, are on offer. Each costs $\$1$.
* The buyer may purchase Box 1 ($B_1$), Box 2 ($B_2$), or neither ($N$), but *cannot purchase both*.
* Yesterday, the seller predicted which option ($B_1$, $B_2$, or $N$) the buyer would choose, with accuracy $0.75$. The seller placed $\$3$ in *each* box that she predicted the buyer **not** to acquire, and $\$0$ in any box she predicted the buyer *would* acquire.

Let us write out the exact payoff matrix across the three dependency hypotheses corresponding to the seller's prediction: $K_{B_1}$ (predicted Box 1), $K_{B_2}$ (predicted Box 2), and $K_N$ (predicted neither). Notice that if the seller predicted $N$, she predicted the buyer would acquire *neither* Box 1 nor Box 2, so she put $\$3$ in *both* boxes! Subtracting the $\$1$ purchase price for buying a box gives the net payoffs:

| Dependency Hypothesis (Seller's Prediction) | Buy Box 1 ($B_1$) | Buy Box 2 ($B_2$) | Buy Neither ($N$) |
| :--- | :---: | :---: | :---: |
| **$K_{B_1}$ (Box 1 has $\$0$, Box 2 has $\$3$)** | $-\$1$ | $+\$2$ | $\$0$ |
| **$K_{B_2}$ (Box 1 has $\$3$, Box 2 has $\$0$)** | $+\$2$ | $-\$1$ | $\$0$ |
| **$K_N$ (Box 1 has $\$3$, Box 2 has $\$3$)** | $+\$2$ | $+\$2$ | $\$0$ |

*(Mathematical Proof of CDT's Vulnerability)* Let $p_1 = P(K_{B_1})$, $p_2 = P(K_{B_2})$, and $p_N = P(K_N)$ be *any* unconditional probability distribution over the seller's predictions held fixed by the buyer ($p_1 + p_2 + p_N = 1$). The gross causal expected values of the two boxes (before the $\$1$ cost) are:

$$U_{\text{gross}}(B_1) = 3(p_2 + p_N), \qquad U_{\text{gross}}(B_2) = 3(p_1 + p_N)$$

Taking the average of the two boxes' gross causal expected values gives:

$$\frac{U_{\text{gross}}(B_1) + U_{\text{gross}}(B_2)}{2} = \frac{3(p_1 + p_2 + 2p_N)}{2} = 1.5(1 + p_N) \ge \$1.50$$

Because the average gross causal expected value of the two boxes is at least $\$1.50$, at least one of the two boxes must have a gross causal expected value of at least $\$1.50$, and therefore a net causal expected utility of at least $\$1.50 - \$1.00 = +\$0.50 > U(N) = \$0$. 

Thus, **no matter what unconditional probabilities $(p_1, p_2, p_N)$ the CDT agent assigns**, standard CDT strictly forbids walking away ($N$) and requires buying whichever box currently looks more likely to be unpredicted! Yet if the buyer chooses $B_i$, the seller predicted $B_i$ with probability $0.75$, meaning the acquired box actually contains $\$3$ with probability $0.25$ and $\$0$ with probability $0.75$. The buyer's actual expected net payoff from buying is:

$$(0.25)(+\$2) + (0.75)(-\$1) = -\$0.25 < \$0$$

By extending this mechanism across sequential stages, Oesterheld and Conitzer (2021) prove that standard CDT agents are vulnerable to **diachronic Dutch books**—sequences of bets that guarantee a deterministic net financial loss.

### Operational Resolution: Self-Informative Deliberation and Ratifiability

Does this refute CDT? As the reference text notes, CDT's foremost modern defender, James Joyce (2012, 2020; Weirich 2016), argues that these counterexamples arise only from an overly naive version of CDT that forbids an agent from updating their beliefs on introspective evidence generated *during* deliberation. According to Joyce, CDT can and must treat an agent's awareness of their own inclination to act as genuine evidence about the causal structure of the world, while still evaluating actions strictly by their forward causal efficacy.

*(Operational Formulation)* Following William Harper (1984), Richard Jeffrey, and James Joyce (2012), we can formalize this refined operational rule through the principle of **ratifiability**. Suppose that during deliberation, an agent tentatively settles on intending action $A^*$, denoted $\text{Int}(A^*)$. Forming the intention $\text{Int}(A^*)$ is an internal mental event that provides diagnostic evidence about the dependency hypotheses, updating the agent's credences from $P(K_i)$ to $P(K_i \mid \text{Int}(A^*))$.

Relative to the epistemic standpoint of intending $A^*$, the causal expected utility of any alternative action $A \in \mathcal{A}$ is:

$$U\big(A \;\big|\; \text{Int}(A^*)\big) = \sum_{i=1}^{r} P\big(K_i \;\big|\; \text{Int}(A^*)\big) \sum_{j=1}^{n} P(O_j \mid A \land K_i) D(O_j)$$

**Definition (Ratifiability):** An action $A^* \in \mathcal{A}$ is *ratifiable* if and only if it maximizes causal expected utility given the evidence that the agent intends to perform $A^*$:

$$U\big(A^* \;\big|\; \text{Int}(A^*)\big) \ge U\big(A \;\big|\; \text{Int}(A^*)\big) \quad \text{for all } A \in \mathcal{A}$$

Let us verify how incorporating ratifiability into CDT resolves our cases without collapsing CDT into EDT:

1. **Newcomb's Paradox:** Whether the agent intends to one-box ($\text{Int}(A_1)$) or two-box ($\text{Int}(A_2)$), two-boxing still strictly dominates one-boxing by $+\$1,000$:
   $$U\big(A_2 \;\big|\; \text{Int}(A_2)\big) = (0.01)(\$1,001,000) + (0.99)(\$1,000) = \$11,000 > U\big(A_1 \;\big|\; \text{Int}(A_2)\big) = \$10,000$$
   Thus, two-boxing ($A_2$) is the *unique* ratifiable action. Updating on self-knowledge never tempts a CDT agent to one-box, because learning that Box B is empty only reinforces the fact that taking both boxes yields $\$1,000$ rather than $\$0$.

2. **The Psychopath Button:** If Paul tentatively intends to press the button ($\text{Int}(P)$), he updates his credence in being a psychopath to $P(K_{\text{psy}} \mid \text{Int}(P)) = 0.99$. From that updated causal perspective:
   $$U\big(P \;\big|\; \text{Int}(P)\big) = (0.01)(10) + (0.99)(-1000) = -989.9 < U\big(\neg P \;\big|\; \text{Int}(P)\big) = 0$$
   Pressing the button is *unratifiable*. Conversely, if Paul intends not to press ($\text{Int}(\neg P)$), his credence in being sane remains high, making $P$ look attractive. As Joyce (2012) argues, a self-aware CDT agent tracks how their evolving credences shift $U(P)$ and settles at an epistemic equilibrium where they abstain once they recognize that any decisive impulse to press is evidence of its own lethality.

3. **Death in Damascus and the Adversarial Offer:** In the Adversarial Offer, neither $B_1$ nor $B_2$ is ratifiable: conditional on intending $B_1$, $p_1 = P(K_{B_1} \mid \text{Int}(B_1)) = 0.75$, so $U(B_1 \mid \text{Int}(B_1)) = (0.75)(-1) + (0.25)(2) = -\$0.25 < U(N \mid \text{Int}(B_1)) = \$0$. What creates the trap is that $N$ is *also* unratifiable as a pure intention (since $\text{Int}(N)$ implies both boxes contain $\$3$ with probability $0.75$). In games with no pure ratifiable option, a rational CDT agent recognizes that any deterministic choice is exploitable by the predictor; as Harper (1984) and Joyce (2012) show, if the agent cannot randomize to reach a mixed-strategy equilibrium, they should reject unratifiable gambles that only appear profitable before taking into account the evidence of one's own choice.

---

## 5. Summary Comparison of Decision Rules

To consolidate our analysis for applied problem-solving, the table below summarizes how Evidential Decision Theory, Standard (Prior-Fixed) Causal Decision Theory, and Ratifiable Causal Decision Theory evaluate actions across a partition of dependency hypotheses $\mathcal{K} = \{K_1, \dots, K_r\}$ with deterministic outcome functions $f_i(A)$:

| Framework | Mathematical Evaluation Criterion | King David / Newcomb | Psychopath Button | Adversarial Offer |
| :--- | :--- | :--- | :--- | :--- |
| **Evidential Decision Theory (EDT)** | Maximize $\sum_i P(K_i \mid A) D(f_i(A))$ | Abstain / One-Box | Do Not Press | Walk Away ($N$) |
| **Standard CDT (Unconditional $P(K_i)$)** | Maximize $\sum_i P(K_i) D(f_i(A))$ | Summon / Two-Box | Press Button | Buy a Box ($B_1$ or $B_2$) |
| **Ratifiable CDT (Self-Informative)** | Seek $A^*$ maximizing $\sum_i P(K_i \mid \text{Int}(A^*)) D(f_i(A))$ | Summon / Two-Box | Do Not Press ($P$ unratifiable) | Reject $B_1, B_2$ (unratifiable) |

---

## 6. Conclusion

Causal decision theory rests on a foundational insight of rational agency: to decide well is to intervene effectively in the causal order of the world, not to curate flattering diagnostic evidence about things that are already fixed. Mathematically, Gibbard and Harper captured this principle by replacing conditional probabilities $P(O_j \mid A)$ with counterfactual probabilities $P(A \to O_j)$—two quantities that Lewis's triviality result proves are fundamentally distinct whenever actions and causal laws are statistically entangled.

While the bare counterfactual formula leaves open how to compute $P(A \to O_j)$ without falling into an imaging regress, partitioning the state space into dependency hypotheses $K_i$ turns CDT into a precise, general-purpose algorithm. Moreover, as contemporary counterexamples like the Psychopath Button and the Adversarial Offer demonstrate, keeping causal efficacy distinct from evidential "news"-value does not require an agent to be blind to their own psychology. When paired with ratifiability and self-informative deliberation, causal decision theory provides a mathematically rigorous framework capable of honoring dominance in Newcomb-style dilemmas while resisting exploitation in adversarial environments.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press. ISBN 9781108607865.
* Bellos, Alex (2016). "Newcomb's problem divides philosophers. Which side are you on?". *The Guardian*, 28 November 2016.
* Egan, Andy (2007). "Some counterexamples to causal decision theory". *The Philosophical Review*, **116** (1): 93–114. doi:10.1215/00318108-2006-023.
* Gibbard, Allan; Harper, William L. (1981). "Counterfactuals and two kinds of expected utility". *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*: 153–190.
* Greaves, Hilary (2013). "Epistemic decision theory". *Mind*, **122** (488): 915–952. doi:10.1093/mind/fzt090.
* Harper, William (1984). "Ratifiability and Causal Decision Theory: Comments on Eells and Seidenfeld". *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, **1984** (2): 213–228. doi:10.1086/psaprocbienmeetp.1984.2.192506.
* Howard, J. V. (1988). "Cooperation in the Prisoner's Dilemma". *Theory and Decision*, **24** (3): 203–213. doi:10.1007/BF00148954.
* Joyce, James M. (2012). "Regret and instability in causal decision theory". *Synthese*, **187** (1): 123–145. doi:10.1007/s11229-011-0022-6.
* Joyce, James M. (2020). "Yet Another Refutation of Causal Decision Theory?". Working paper, University of Michigan.
* Lewis, David (1976). "Probabilities of conditionals and conditional probabilities". *The Philosophical Review*, **85** (3): 297–315. doi:10.2307/2184045.
* Lewis, David (1979). "Prisoners' dilemma is a Newcomb problem". *Philosophy & Public Affairs*, **8** (3): 235–240.
* Lewis, David (1981). "Causal decision theory". *Australasian Journal of Philosophy*, **59** (1): 5–30. doi:10.1080/00048408112340011.
* Meacham, Christopher J. G. (2010). "Binding and its consequences". *Philosophical Studies*, **149** (1): 49–71. doi:10.1007/s11098-010-9539-7.
* Oesterheld, Caspar; Conitzer, Vincent (2021). "Extracting Money from Causal Decision Theorists". *The Philosophical Quarterly*, **71** (4): pqaa086. doi:10.1093/pq/pqaa086.
* Shaffer, Michael John (2009). "Decision Theory, Intelligent Planning and Counterfactuals". *Minds and Machines*, **19** (1): 61–92. doi:10.1007/s11023-008-9126-2.
* Spencer, Jack (2020). "An argument against causal decision theory". *Analysis*, **81**: 52–61. doi:10.1093/analys/anaa037.
* Wedgwood, Ralph (2013). "Gandalf's solution to the Newcomb problem". *Synthese*, **190** (14): 2643–2675. doi:10.1007/s11229-011-9900-1.
* Weirich, Paul (2016). "Causal Decision Theory". In Zalta, Edward N. (ed.), *Stanford Encyclopedia of Philosophy* (Winter 2016 ed.).
* Wolpert, D. H.; Benford, G. (2013). "The lesson of Newcomb's paradox". *Synthese*, **190** (9): 1637–1646. doi:10.1007/s11229-011-9899-3.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Audience**

I'm currently focused on defining the target audience. I'm aiming for mathematically literate readers with an interest in decision theory. I need to balance technical rigor with accessibility. I'm trying to decide on the best angle to introduce CDT, to pique interest from a variety of readers.


**Refining the Scope**

I'm now honing the scope of the essay. I intend to provide a coherent account of Causal Decision Theory, including mathematical definitions and examples. The goal is to be precise enough to guide decisions in unfamiliar cases. I'll also clarify how CDT evaluates actions and handles dependencies, while carefully distinguishing claims from the source versus my own expansions.


**Clarifying Key Concepts**

I'm now diving into the source document, focusing on core definitions. I'm noting the contrast between Causal Decision Theory (CDT) and Evidential Decision Theory (EDT), particularly the difference in how each evaluates actions. I'm aiming to extract the essence of CDT: that rational agents choose actions based on the expected outcome of causation, contrasting with EDT's focus on evidence. My goal is to extract the essence of CDT, and to avoid introducing my own assumptions when clarifying these concepts.


**Analyzing the Equation**

I'm now focused on formalizing the core equation of CDT, as presented by Gibbard and Harper. I'm unpacking the terms: the utility of an action ($U(A)$), the counterfactual probability of an action leading to an outcome ($P(A \to O_j)$), and the desirability of that outcome ($D(O_j)$). I'm carefully comparing this formulation to EDT's use of conditional probability, highlighting the critical distinction that Lewis demonstrated.


**Examining Philosophical Implications**

I'm now exploring the philosophical implications and thought experiments. I've been looking at the role of counterfactuals, particularly the use of conditional excluded middle. I'm focusing on cases where actions and their outcomes aren't statistically independent, such as the King David and Bathsheba scenario. I'm also planning to investigate Newcomb's Paradox and the Twin Prisoner's Dilemma to further solidify the distinctions between EDT and CDT, especially in complex scenarios.


**Evaluating Criticisms**

Now, I'm delving into the criticisms of CDT, especially regarding calculating counterfactual probabilities. I'm assessing the vagueness in determining $P(A \to O_j)$ and the challenges of imaging, as Shaffer highlights. I also understand that CDT doesn't have an algorithm to determine $P(A \to O_j)$. I'm also examining Egan's counterarguments about dependency hypotheses. Furthermore, I've started going through the *Death in Damascus* example to see if I can process the correlation. I plan to address these in my final analysis.


**Analyzing Paradoxes**

I'm now wrestling with specific paradoxes to test CDT's boundaries. I'm deep into the Offer & Money Extraction scenario and seeing how CDT's approach leads to seemingly counterintuitive choices. I'm also examining the Psychopath Button thought experiment and how CDT's analysis clashes with common intuition. Finally, I'm analyzing defense, where Jim Joyce and Weirich are trying to clarify that CDT is not necessarily irrational in this context, when properly applied.


**Structuring the Essay**

I am now structuring the essay and creating the framework. I'm aiming for around 2400-3000 words, integrating mathematical rigor with philosophical clarity. I have section headings planned: the introduction, formal architectures of CDT and EDT, and mathematical formalization. I'll include the equation, criticisms, and implications to build a cohesive narrative.


**Formalizing the Distinction**

I'm now detailing the formal distinction between Causal Decision Theory (CDT) and Evidential Decision Theory (EDT), focusing on their core equations. I'm presenting the Gibbard-Harper (1981) formula directly: $U(A) = \sum_j P(A \to O_j) D(O_j)$, contrasting it with EDT's $V(A) = \sum_j P(O_j \mid A) D(O_j)$. I'm clarifying the source's language around "counterfactual probability" and relating it to standard subjunctive conditional notation. I plan to highlight David Lewis's (1976) triviality result, showing why the probabilities cannot generally be equal, unless the two axioms, including Conditional Excluded Middle (CEM), hold, which I intend to prove explicitly.


**Operationalizing Probabilities**

I'm now outlining a section to operationalize counterfactual probabilities by looking at two classic cases. I'm focusing on "Medical/Psychological Confounding: King David and Bathsheba," where I intend to develop a numerical model to distinguish between the conditional and counterfactual probabilities. I'm also planning to explore "Predictive Correlation: Newcomb's Paradox and the Twin Prisoner's Dilemma," where I'll compute and compare the utilities from both CDT and EDT, highlighting the contrast in their approaches to these problems. I'm hoping this section will show how these methods work in practice.


**Resolving Algorithm Challenges**

I'm now grappling with Shaffer's critique of CDT's lack of a canonical algorithm for computing counterfactual probabilities. I'm focusing on Lewis's imaging method and the potential for epistemic regress. My current plan is to operationalize this, drawing on Egan's dependency hypotheses and causal modeling. I'm aiming to partition the state space into maximally specific dependency hypotheses ($K_i$ or causal states $S_i$) to eliminate the regress and derive a practical formula: $U(A) = \sum_i P(K_i) D(f_i(A))$, which is equivalent to  $\sum_i P(K_i) \sum_j P(O_j \mid A \land K_i) D(O_j)$. I intend to connect this method to Judea Pearl's *do*-calculus operator, as well.


**Operationalizing Models**

I'm now constructing Structural Causal Models (SCMs) to provide readers with a concrete, repeatable 4-step process. I'm focusing on "Pathologies of Fixed Credences," expanding on the cutting-edge criticisms. I'll analyze failure modes using mathematical models: the Psychopath Button, Death in Damascus, and the Adversarial Offer. I will show how these issues arise from holding unconditional credences fixed.


**Finalizing the Structure**

Now I'm finalizing the structure of my essay. I'm incorporating the recent addition of Oesterheld & Conitzer's two-box offer to show that the standard CDT calculations can compel a purchase that loses money. I'll include Jim Joyce's operational fix, focusing on "self-informative deliberation and ratifiability." I'm formulating the ratifiability condition and demonstrating how it resolves specific paradoxes while preserving two-boxing in Newcomb's problem. I'm also writing the conclusion to summarize the essay's core ideas and the references. The essay is nearly complete.


**Verifying the Derivation**

I'm now clarifying the connection between the Gibbard-Harper equivalence and its underlying assumptions. I've re-examined their two core axioms: Conditional Excluded Middle (CEM), and Modus Ponens (or Centering). I am confirming that the equivalence $P(A \to O_j) = P(O_j \mid A)$ relies on both axioms and the statistical independence of $A$ and $A \to O_j$. I plan to show how Modus Ponens leads to triviality in standard probability.


**Confirming Mathematical Equivalence**

I'm now diving into the Adversarial Offer scenario and its math to build a counterexample for CDT. I'm unpacking the source's assumptions, defining the buyer's options, and setting up the utility matrix to prove a point about CDT's rationality. I'm working through the logic to demonstrate a case where CDT leads to losing money. I'm also confirming the formal equivalence between Gibbard-Harper and how Modus Ponens leads to triviality in standard probability.


**Calculating Expected Values**

I'm now calculating the causal expected values for the Adversarial Offer scenario, specifically for buying Box 1 versus Box 2, and for buying neither. Using a structural causal model with dependency hypotheses, I'm modeling the outcomes based on the seller's predictions and demonstrating the potential for CDT to lead to an unfavorable outcome. I'm verifying the math on these cases. I plan to determine if CDT is irrational in this scenario.


**Calculating the Values**

I'm now carefully calculating the expected values for each action: buying Box 1, buying Box 2, and buying neither in the Adversarial Offer scenario. I'm using a structural causal model with dependency hypotheses to rigorously model each outcome based on the seller's predictions. I'm working through the calculations step by step, which has proven that CDT leads to a loss in this particular scenario. I'm verifying the math on these cases and questioning the rationality of CDT's decision.


```
