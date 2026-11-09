# 005_cdt_wikipedia_google_gemini-4-argon_rhigh_phigh / 00003

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/81e74b74-5f6e-445c-889f-d824318f9f03/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/81e74b74-5f6e-445c-889f-d824318f9f03/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Interventions, Counterfactuals, and Rational Choice: A Mathematical Guide to Causal Decision Theory

When a rational agent confronts a choice among competing actions, how should the value of each option be assessed? At first glance, standard probability theory seems to offer an immediate answer: calculate the expected utility of each action by conditioning on its performance. Yet one of the central insights of twentieth-century decision theory is that conditional probability conflates two fundamentally distinct roles an action can play: an action as *evidence* about the state of the world, and an action as a *causal intervention* upon the world.

**Causal decision theory (CDT)** is the mathematical and philosophical school of thought designed to isolate the latter. As summarized in our reference overview, CDT holds that a rational agent should select the action that *causes* the best outcome in expectation. In doing so, it stands in direct opposition to **evidential decision theory (EDT)**, which advises choosing the action with the highest "news value"—the action that, if one were informed it had been taken, would provide the strongest statistical evidence of a favorable outcome (Ahmed 2021).

In this essay, we will develop a precise mathematical account of CDT, trace its philosophical motivations, and establish a concrete operational procedure for applying the theory to novel decision problems. Because the reference text leaves several formal connections open—most notably the exact algorithm for computing counterfactual probabilities and the proper handling of self-referential or adversarial environments—we will explicitly distinguish between the foundational principles reported in the source and the mathematical reconstructions and operational extensions we introduce to make the framework fully actionable.

---

## 1. The Informal Core and the Formal Gibbard–Harper Equation

To see why expected value must enter causal reasoning, consider the simple illustration provided in the reference text. If you know with certainty that eating an apple will cause you to be happy and eating an orange will cause you to be sad, causal rationality trivially recommends the apple. In realistic decision problems, however, an action's causal effects depend on background states of the world that are unknown to the agent. Suppose eating a *good* apple causes happiness, while eating a *bad* apple causes sadness. Because you do not know whether the apple before you is good or bad, you cannot know the actual causal consequence of eating it; you must instead evaluate its *expected* causal consequence, weighting the utility of each potential outcome by your credence that the apple is in the corresponding state.

Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be a finite set of mutually exclusive actions available to an agent, and let $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ be a partition of possible outcomes. Each outcome $O_j$ carries a numerical desirability (or utility) $D(O_j) \in \mathbb{R}$.

In their seminal 1981 formulation, Allan Gibbard and William Harper defined the causal expected utility $U(A)$ of an action $A \in \mathcal{A}$ in terms of the probabilities of counterfactual conditionals (Gibbard and Harper 1981):

$$U(A) = \sum_{j=1}^{m} P(A \to O_j) \, D(O_j). \tag{1}$$

The reference article describes $P(A \to O_j)$ as "the counterfactual probability of it being the case that $A$ necessarily implies $O_j$." As a point of mathematical and philosophical precision—stepping beyond the brief phrasing of the reference text—it is important to clarify that in the Stalnaker–Lewis semantics underlying Gibbard and Harper's work, the arrow $\to$ does not denote strict logical entailment ($\Box(A \supset O_j)$), nor does it denote the material conditional. Rather, $A \to O_j$ is the **subjunctive or counterfactual conditional**: *"If the agent were to perform action $A$, then outcome $O_j$ would obtain."* Equation (1) asserts that the rational figure of merit for an action $A$ is the expectation of $D(O_j)$ weighted by the agent's probability that $A$ would counterfactually bring about $O_j$.

By contrast, evidential decision theory evaluates an action $A$ using standard conditional probabilities:

$$V(A) = \sum_{j=1}^{m} P(O_j \mid A) \, D(O_j), \tag{2}$$

where $P(O_j \mid A) = \frac{P(A \land O_j)}{P(A)}$ for any action with $P(A) > 0$.

---

## 2. Why Conditioning Fails: Lewis's Triviality Result and Confounding

If the probability of the counterfactual conditional $P(A \to O_j)$ always coincided with the conditional probability $P(O_j \mid A)$, equations (1) and (2) would be identical and CDT would collapse into EDT. However, as the reference article notes, David Lewis (1976) proved a celebrated **triviality result** demonstrating that no non-trivial probability space can identify the probability of a conditional with a conditional probability across a class of probability functions closed under conditioning. Specifically, if $P(A \to B) = P(B \mid A)$ held universally across such a class, the underlying probability function could never assign positive probability to more than two incompatible propositions (making the probability space at most four-valued).

Why do $P(A \to O_j)$ and $P(O_j \mid A)$ diverge in decision-theoretic practice? The reference text notes a theorem by Gibbard and Harper: if we adopt two axioms governing the logic of counterfactuals, then the statistical independence of the act $A$ and the counterfactual $A \to O_j$ suffices to guarantee that $P(A \to O_j) = P(O_j \mid A)$. Because the reference article mentions this result without supplying the derivation, let us reconstruct the proof explicitly to see how the machinery works.

### Mathematical Reconstruction: The Equivalence Condition

Assume our probability measure $P$ is defined over an algebra of propositions that includes acts $A \in \mathcal{A}$, outcomes $O_j \in \mathcal{O}$, and counterfactuals $A \to O_j$. Following Gibbard and Harper (1981) and Shaffer (2009), we impose two axioms:

1. **Conditional Excluded Middle (CEM):** For any action $A$ and outcome $O_j$, $(A \to O_j) \lor (A \to \neg O_j)$ holds at every possible world, and $(A \to O_j) \land (A \to \neg O_j)$ is impossible. This guarantees that $A \to O_j$ is a well-behaved measurable event whose negation is $A \to \neg O_j$.
2. **Centering (Modus Ponens / Weak Centering):** In any world where $A$ is actually performed, the counterfactual $A \to O_j$ has the exact same truth value as $O_j$ itself. Formally, the conjunction $A \land (A \to O_j)$ is logically equivalent to $A \land O_j$.

**Proposition 1.** *Under Centering, $P(A \to O_j) = P(O_j \mid A)$ (assuming $P(A) > 0$) if and only if the act $A$ and the counterfactual proposition $A \to O_j$ are statistically independent.*

*Proof.* By the definition of conditional probability and the Centering equivalence $A \land (A \to O_j) \equiv A \land O_j$, we have:

$$P(A \to O_j \mid A) = \frac{P\big(A \land (A \to O_j)\big)}{P(A)} = \frac{P(A \land O_j)}{P(A)} = P(O_j \mid A). \tag{3}$$

Now, by definition, $A$ and $A \to O_j$ are statistically independent if and only if $P(A \to O_j \mid A) = P(A \to O_j)$. Substituting this independence relation into the left-hand side of equation (3) immediately yields:

$$P(A \to O_j) = P(O_j \mid A). \quad \blacksquare$$

Equation (3) reveals something striking: *evidential conditional probability $P(O_j \mid A)$ is actually the conditional probability of the counterfactual $A \to O_j$ given that $A$ is performed.* Therefore, EDT and CDT diverge precisely when performing $A$ gives the agent statistical evidence about what the counterfactual mapping $A \to O_j$ is!

This failure of independence occurs whenever there is a **common cause** (a confounder) that influences both the agent's propensity to choose $A$ and the background state of the world that determines $O_j$.

### Example 1: King David and Bathsheba

To illustrate how a common cause breaks independence, the reference text cites Gibbard and Harper's classic example of King David and Bathsheba:

* **The Narrative (from the source):** King David desires to summon Bathsheba, the wife of Uriah, but fears provoking a revolt. From political science and psychology, David knows that kings fall into two fixed personality types determined by genetics and early childhood: charismatic ($C$) and uncharismatic ($\neg C$). Charismatic kings rarely face successful revolts, whereas uncharismatic kings frequently do (because of their sneaky, ignoble bearing). Crucially, unjust acts do not *cause* revolts; however, charismatic kings strongly tend to act justly, while uncharismatic kings tend to act unjustly. David does not know his own charisma type, but he knows summoning Bathsheba is an unjust act.
* **Mathematical Parameterization (our elaboration):** Let the action space be $\mathcal{A} = \{A_S, A_R\}$, where $A_S$ is summoning Bathsheba and $A_R$ is refraining. Let the outcomes be defined by whether a revolt occurs ($R$ or $\neg R$) and whether David enjoys Bathsheba's company. Suppose David assigns utilities as follows:
  * Utility of Bathsheba's company: $+2$
  * Utility cost of a successful revolt: $-10$
  * Thus, the four composite outcomes have desirabilities:
    $$D(\neg R \land A_S) = 2, \quad D(\neg R \land A_R) = 0, \quad D(R \land A_S) = -8, \quad D(R \land A_R) = -10.$$
  Suppose David's unconditional prior credence that he is charismatic is $P(C) = 0.5$. If he is charismatic ($C$), the probability of a revolt is $0.1$ regardless of what he does; if he is uncharismatic ($\neg C$), the probability of a revolt is $0.8$ regardless of what he does. However, because unjust acts are symptomatic of uncharismatic kings, conditioning on his choice shifts his beliefs about his personality: suppose $P(C \mid A_R) = 0.9$ and $P(C \mid A_S) = 0.1$.

Let us compare EDT and CDT on this parameterization:

1. **Evidential Evaluation ($V$):** Under EDT, conditioning on $A_S$ makes it highly likely ($0.9$) that David is uncharismatic. Thus, the conditional probability of revolt given $A_S$ is:
   $$P(R \mid A_S) = P(C \mid A_S)P(R \mid C, A_S) + P(\neg C \mid A_S)P(R \mid \neg C, A_S) = (0.1)(0.1) + (0.9)(0.8) = 0.73.$$
   Similarly, conditioning on $A_R$ yields:
   $$P(R \mid A_R) = (0.9)(0.1) + (0.1)(0.8) = 0.17.$$
   The evidential expected utilities are therefore:
   $$V(A_S) = 0.27(2) + 0.73(-8) = -5.30, \qquad V(A_R) = 0.83(0) + 0.17(-10) = -1.70.$$
   EDT strictly recommends $A_R$ (abstaining), effectively advising David to manage the *news* about his fixed genetic character.

2. **Causal Evaluation ($U$):** Under CDT, whether David is charismatic is already causally fixed; his choice today cannot alter his childhood or genetics. Thus, $P(A_S \to R)$ and $P(A_R \to R)$ both weight the revolt probabilities by the *unconditional* prior $P(C) = 0.5$:
   $$P(A_S \to R) = P(A_R \to R) = (0.5)(0.1) + (0.5)(0.8) = 0.45.$$
   Consequently, the causal expected utilities are:
   $$U(A_S) = 0.55(2) + 0.45(-8) = -2.50, \qquad U(A_R) = 0.55(0) + 0.45(-10) = -4.50.$$
   CDT recommends $A_S$, recognizing that summoning Bathsheba adds $+2$ to David's payoff whether or not a revolt occurs, without changing the probability of revolt by a single percentage point. As the reference text observes, cases like King David explain why philosophers overwhelmingly prefer CDT over EDT when forced to choose between them (Weirich 2016).

---

## 3. Operationalizing CDT: Dependency Hypotheses and Imaging

A major criticism documented in the reference article is **vagueness**: the Gibbard–Harper equation (1) does not by itself specify a unique mathematical algorithm for computing the counterfactual probabilities $P(A \to O_j)$ (Shaffer 2009). If a practitioner is handed a novel decision problem, how should $P(A \to O_j)$ actually be calculated?

The reference text points toward two closely related mechanisms in the literature: (i) holding fixed unconditional credences in *dependency hypotheses* (mentioned in connection with Andy Egan's analysis), and (ii) David Lewis's *imaging* technique (Lewis 1981). Below, we develop both into a concrete mathematical procedure and show how they fit together.

### Method A: Partitioning by Dependency Hypotheses (Causal States)

In almost every practical decision problem, the uncertainty about what an action $A$ will cause stems from uncertainty about the underlying causal structure or background state of the world (just as in the reference article's informal example of not knowing whether an apple is good or bad).

To formalize this operational procedure, let $\mathcal{S} = \{S_1, S_2, \dots, S_K\}$ be a partition of the probability space into **dependency hypotheses** (or causal background states). A valid partition $\mathcal{S}$ must satisfy two properties:

1. **Causal Independence from Actions:** No action $A \in \mathcal{A}$ available to the agent has any causal influence on which state $S_k \in \mathcal{S}$ obtains. (Equivalently, for each $k$, $P(A \to S_k) = P(S_k)$.)
2. **Sufficiency for Causal Consequences:** Conditional on any state $S_k$ and action $A$, the probability of each outcome $O_j$ is purely a matter of objective causal law or chance, unconfounded by the agent's inclinations. That is, within state $S_k$, $P((A \to O_j) \mid S_k) = P(O_j \mid A, S_k)$.

By the law of total probability over the partition $\mathcal{S}$, the counterfactual probability $P(A \to O_j)$ decomposes as:

$$P(A \to O_j) = \sum_{k=1}^{K} P(S_k) \, P(O_j \mid A, S_k). \tag{4}$$

Substituting equation (4) into the Gibbard–Harper formula (1) yields the **state-partition form of CDT**:

$$U(A) = \sum_{k=1}^{K} P(S_k) \sum_{j=1}^{m} P(O_j \mid A, S_k) \, D(O_j) = \sum_{k=1}^{K} P(S_k) \, D(A \land S_k), \tag{5}$$

where $D(A \land S_k) = \sum_j P(O_j \mid A, S_k) D(O_j)$ is the expected utility of performing $A$ in state $S_k$.

Notice how cleanly equation (5) illuminates the contrast with EDT. Expanding EDT's formula (2) over the exact same partition $\mathcal{S}$ gives:

$$V(A) = \sum_{k=1}^{K} P(S_k \mid A) \, D(A \land S_k). \tag{6}$$

Everything boils down to the weight placed on $S_k$: CDT holds fixed the unconditional credence $P(S_k)$, whereas EDT uses the act-updated credence $P(S_k \mid A)$. (For readers familiar with Judea Pearl's modern graphical causal models—an external connection beyond our reference text—equation (4) is equivalent to the *back-door adjustment formula* for the interventional distribution $P(O_j \mid \mathrm{do}(A))$, where $\mathcal{S}$ is a set of parent variables blocking all back-door confounding paths between $A$ and $O_j$.)

### Method B: Lewis's Imaging Algorithm and the Regress Worry

What if we want to evaluate $P(A \to O_j)$ directly on a space of possible worlds $W$ without explicitly writing down a partition $\mathcal{S}$? As described in the reference article, Lewis (1981) proposed the method of **imaging**.

Let $W$ be a finite set of possible worlds equipped with a prior probability distribution $P: W \to [0, 1]$ such that $\sum_{w \in W} P(w) = 1$. Every proposition $X$ (such as an action $A$ or outcome $O_j$) is identified with the subset of worlds $W_X \subseteq W$ where $X$ is true. Assume $A$ is possible ($W_A \neq \emptyset$).

For each world $w \in W$, Stalnaker's semantics assumes there is a unique "closest" (most similar) world $w_A \in W_A$ in which the agent performs action $A$ (if $w \in W_A$, then $w_A = w$). Whereas standard Bayesian conditioning *deletes* all worlds outside $W_A$ and renormalizes the remaining probabilities proportionally, **imaging** preserves probability mass locally by transferring the probability $P(w)$ of each world $w \notin W_A$ directly onto its closest $A$-world $w_A$. Formally, the imaged probability measure $P^A$ on $W$ is defined by the pushforward:

$$P^A(w') = \begin{cases} \displaystyle\sum_{\{w \in W \,:\, w_A = w'\}} P(w) & \text{if } w' \in W_A, \\ 0 & \text{if } w' \notin W_A. \end{cases} \tag{7}$$

Under imaging, the counterfactual probability is simply the imaged measure of $O_j$:

$$P(A \to O_j) = P^A(W_{O_j}) = \sum_{w' \in W_A \cap W_{O_j}} P^A(w'). \tag{8}$$

**Addressing the Regress Criticism:** The reference text notes a criticism raised by Shaffer (2009): to apply imaging, we must know which world $w_A$ is closest to $w$, or what we would believe if we were made certain of $A$; yet specifying which world would obtain if $A$ were true is *itself* a counterfactual conditional to which we might assign probability less than $1$, threatening an epistemic regress.

As an operational resolution of this uncertainty, we can unify Method A and Method B. A possible world $w$ can be represented as a tuple $w = (A(w), S(w), \xi(w))$, where $A(w) \in \mathcal{A}$ is the action taken at $w$, $S(w) \in \mathcal{S}$ is the realization of the causal background state (everything causally independent of $A$), and $\xi(w)$ captures post-decision stochastic noise. If we define the "closest $A$-world" $w_A$ via a structural intervention—replacing $A(w)$ with $A$ while holding fixed $S(w)$ and $\xi(w)$—then moving probability mass from $w$ to $w_A$ leaves the marginal distribution of $S$ completely invariant ($P^A(S_k) = P(S_k)$). Under this structural definition of world-similarity, Lewis's imaging formula (8) reduces algebraically to the dependency-hypothesis formula (4), and no infinite regress arises once the causal boundary of $S$ is specified.

---

## 4. Classic Thought Experiments: Newcomb's Paradox and the Twin Prisoner's Dilemma

Equipped with equation (5), let us examine how CDT operates in the flagship thought experiments described in the reference article.

### Example 2: Newcomb's Paradox

In Newcomb's paradox (Wolpert and Benford 2013; Ahmed 2021), an agent faces two boxes:

* **Box A** is transparent and visibly contains $\$1,000$.
* **Box B** is opaque and contains either $\$1,000,000$ or $\$0$.
* The agent must choose between two actions: taking both boxes ($A_2$, "two-boxing") or taking only Box B ($A_1$, "one-boxing").
* Yesterday, a Predictor—known to be $99\%$ accurate—predicted the agent's choice. If the Predictor predicted $A_1$, she placed $\$1,000,000$ in Box B; if she predicted $A_2$, she placed $\$0$ in Box B.

Let the causal dependency hypotheses be the two possible states of Box B set yesterday: $S_1$ (Box B contains $\$1,000,000$) and $S_2$ (Box B contains $\$0$). Because the Predictor's action lies in the past and there is no backward causation, $S_1$ and $S_2$ are causally independent of the agent's present choice. Assuming utility is linear in dollars, the payoff matrix $D(A_i \land S_k)$ is:

| Action \ Causal State | $S_1$ ($\$1\text{M}$ in Box B) | $S_2$ ($\$0$ in Box B) |
| :--- | :---: | :---: |
| **$A_1$ (One-Box: Box B only)** | $\$1,000,000$ | $\$0$ |
| **$A_2$ (Two-Box: Boxes A & B)** | $\$1,001,000$ | $\$1,000$ |

Let $p = P(S_1) \in [0, 1]$ be the agent's unconditional prior credence that the Predictor placed $\$1,000,000$ in Box B. Applying CDT's equation (5):

$$U(A_1) = p(1,000,000) + (1 - p)(0) = 1,000,000p,$$
$$U(A_2) = p(1,001,000) + (1 - p)(1,000) = 1,000,000p + 1,000.$$

Regardless of the value of $p$, $U(A_2) - U(A_1) = \$1,000 > 0$. By strict dominance over the causal states, CDT recommends two-boxing ($A_2$).

By contrast, EDT applies equation (6) using the $99\%$ accuracy of the Predictor as conditional evidence: $P(S_1 \mid A_1) = 0.99$ and $P(S_1 \mid A_2) = 0.01$. Thus:

$$V(A_1) = 0.99(1,000,000) + 0.01(0) = \$990,000,$$
$$V(A_2) = 0.01(1,001,000) + 0.99(1,000) = \$11,000.$$

EDT recommends one-boxing ($A_1$). As the reference article highlights, Newcomb's problem remains fiercely debated among philosophers (Bellos 2016): critics of CDT point out that one-boxers walk away millionaires $99\%$ of the time while two-boxers walk away with $\$1,000$ ("If you're so smart, why ain't you rich?"), whereas defenders of CDT insist that at the moment of choice the money is either already in Box B or not, making it irrational to leave a guaranteed $\$1,000$ on the table.

### Example 3: The Twin Prisoner's Dilemma

As David Lewis (1979) demonstrated, the exact same mathematical structure arises in a one-shot Prisoner's Dilemma played against a psychological "twin" whose decision process is strongly correlated with, though causally isolated from, your own (Howard 1988). Suppose you and your twin must independently choose to Cooperate ($A_C$) or Defect ($A_D$). Defecting saves you $\$1,000$ regardless of what your twin does, while your twin's cooperation gives you $\$1,000,000$. Because your twin's action ($S_C$ or $S_D$) is causally unaffected by yours, CDT treats $\{S_C, S_D\}$ as the partition of dependency hypotheses and recommends Defecting ($A_D$) by strict dominance—even if $P(S_C \mid A_C) = 0.99$.

---

## 5. Frontier Criticisms: Self-Information, Instability, and Money Extraction

While CDT's two-boxing verdict in Newcomb's paradox is embraced by causal theorists as a feature rather than a bug, the reference article surveys a wave of more recent counterexamples designed to show that holding fixed unconditional credences in dependency hypotheses can lead to patently self-defeating or unstable behavior. Let us analyze the two sharpest families of counterexamples from the reference text and formulate how a rigorous operational CDT can respond.

### 5.1 The Psychopath Button and Deliberative Self-Information

In Andy Egan's (2007) **Psychopath Button** thought experiment (see also Greaves 2013), an agent named Paul is debating whether to press a "kill all psychopaths" button ($A_P$) or refrain ($A_R$).

* **Paul's Preferences and Beliefs:** Paul prefers living in a world without psychopaths to living in a world with them, but he vastly prefers continuing to live over dying. Initially, Paul is quite confident that he is not a psychopath—say, his prior credence that he is a psychopath ($S_{\text{psy}}$) is $P(S_{\text{psy}}) = 0.01$, while $P(\neg S_{\text{psy}}) = 0.99$. However, Paul is also highly confident that *only a psychopath would press such a button*: say, $P(S_{\text{psy}} \mid A_P) = 0.99$.
* **Payoffs (our numerical assignment):** Suppose living in a world with psychopaths (the status quo under $A_R$) has utility $0$; living in a world cleared of psychopaths has utility $+10$; and dying (which occurs if Paul presses the button and is himself a psychopath) has utility $-1,000$.

| Action \ Causal State | $\neg S_{\text{psy}}$ (Paul is sane) | $S_{\text{psy}}$ (Paul is a psychopath) |
| :--- | :---: | :---: |
| **$A_P$ (Press Button)** | $+10$ | $-1,000$ |
| **$A_R$ (Refrain)** | $0$ | $0$ |

If we apply naive CDT using Paul's initial unconditional prior $P(S_{\text{psy}}) = 0.01$, we get:

$$U_{\text{naive}}(A_P) = 0.99(10) + 0.01(-1,000) = 9.9 - 10 = -0.1 < 0,$$

or, if Paul values a psychopath-free world slightly more—say $+20$ instead of $+10$—then:

$$U_{\text{naive}}(A_P) = 0.99(20) + 0.01(-1,000) = 19.8 - 10 = +9.8 > U_{\text{naive}}(A_R) = 0.$$

In the latter case, naive CDT tells Paul to press the button! Yet as Egan notes, almost everyone agrees Paul should *not* press it: if he finds himself about to press it, he has overwhelming evidence that he is a psychopath and that pressing it will kill him.

**Operational Resolution (Joyce's Deliberative Updating):** As the reference article points out, James Joyce (2012, 2020)—the foremost modern defender of CDT—argues that CDT is fully capable of incorporating *"information about what one is inclined or likely to do as evidence"* (see also Weirich 2016).

We can formalize Joyce's defense mathematically as a two-stage **deliberative updating (or ratifiability) procedure**:

1. During deliberation, an agent's emerging inclination to perform an action $A$ is an observable psychological event $I_A$. Before committing to an action, a rational Bayesian agent updates their unconditional prior $P(S_k)$ on the evidence $I_A$ of their own inclination, forming an updated credence distribution $P_I(S_k) = P(S_k \mid I_A)$.
2. The agent then evaluates causal expected utility using $P_I(S_k)$ as the current prior over dependency hypotheses:
   $$U(A' \mid I_A) = \sum_{k=1}^{K} P(S_k \mid I_A) \, D(A' \land S_k). \tag{9}$$
3. An action $A^*$ is **ratifiable** (deliberatively stable) if and only if it maximizes causal expected utility given the inclination to perform it:
   $$A^* \in \arg\max_{A' \in \mathcal{A}} U(A' \mid I_{A^*}). \tag{10}$$

Applying equation (9) to Paul: the moment Paul feels inclined to press the button ($I_{A_P}$), his credence in $S_{\text{psy}}$ updates to $P(S_{\text{psy}} \mid I_{A_P}) = 0.99$. Evaluated from that updated epistemic standpoint, the causal expected utility of pressing is $U(A_P \mid I_{A_P}) = 0.01(20) + 0.99(-1,000) = -989.8 < U(A_R \mid I_{A_P}) = 0$. Pressing the button is therefore *unratifiable*, whereas refraining ($A_R$) is uniquely ratifiable ($U(A_R \mid I_{A_R}) = 0$ and, if Paul still knows that deciding to press would mean he is a psychopath, he does not switch).

### 5.2 Death in Damascus and the Adversarial Offer

While ratifiability rescues CDT in the Psychopath Button, a deeper challenge arises when *no* pure action is ratifiable. The classic example mentioned in the reference text is **Death in Damascus** (Gibbard and Harper 1981; Harper 1984; Egan 2007; Meacham 2010): Death predicts whether you will be in Damascus ($A_D$) or Aleppo ($A_A$) tomorrow and goes to wait for you there. If you lean toward staying in Damascus ($I_{A_D}$), you infer Death is headed to Damascus, so CDT says flee to Aleppo ($A_A$); as soon as you decide to flee to Aleppo ($I_{A_A}$), you infer Death is waiting in Aleppo, so CDT says stay in Damascus ($A_D$).

Recently, Jack Spencer (2020) and Caspar Oesterheld and Vincent Conitzer (2021) sharpened this instability into scenarios where a CDT agent voluntarily loses money or falls prey to a diachronic Dutch book. Let us work through the exact mathematics of Oesterheld and Conitzer's **Adversarial Offer**, as quoted in the reference text:

* **The Setup (from the source):** Two boxes, Box 1 and Box 2, are on offer. A buyer may purchase Box 1 ($A_1$), purchase Box 2 ($A_2$), or purchase neither ($A_0$), but may not purchase both. Each box costs $\$1$. Yesterday, the seller put $\$3$ in each box that she predicted the buyer *not* to acquire. Both seller and buyer believe the seller's prediction is accurate with probability $0.75$.

Let us construct the causal state table carefully. Yesterday, the seller made one of three predictions about the buyer's choice today:
* **$S_1$ (Seller predicted $A_1$):** Because the seller puts $\$3$ in each box predicted *not* to be acquired, Box 1 contains $\$0$ and Box 2 contains $\$3$.
* **$S_2$ (Seller predicted $A_2$):** Box 1 contains $\$3$ and Box 2 contains $\$0$.
* **$S_0$ (Seller predicted $A_0$):** Neither Box 1 nor Box 2 was predicted to be acquired, so *both* Box 1 and Box 2 contain $\$3$.

Subtracting the $\$1$ purchase price when a box is bought, the buyer's net causal payoff matrix $D(A_i \land S_k)$ is:

| Buyer's Action \ Seller's Prediction | $S_1$ (Pred. $A_1$) | $S_2$ (Pred. $A_2$) | $S_0$ (Pred. $A_0$) |
| :--- | :---: | :---: | :---: |
| **$A_1$ (Buy Box 1 for $\$1$)** | $-\$1$ | $+\$2$ | $+\$2$ |
| **$A_2$ (Buy Box 2 for $\$1$)** | $+\$2$ | $-\$1$ | $+\$2$ |
| **$A_0$ (Buy Neither)** | $\$0$ | $\$0$ | $\$0$ |

Let $(p_1, p_2, p_0)$ be *any* probability distribution representing the buyer's unconditional credences over $(S_1, S_2, S_0)$ at the moment of choice, with $p_1 + p_2 + p_0 = 1$ and $p_k \ge 0$. Under CDT's equation (5), the causal expected utilities of the three actions are:

$$U(A_1) = -p_1 + 2p_2 + 2p_0 = 3(p_2 + p_0) - 1, \tag{11a}$$
$$U(A_2) = 2p_1 - p_2 + 2p_0 = 3(p_1 + p_0) - 1, \tag{11b}$$
$$U(A_0) = 0. \tag{11c}$$

Now consider the average of $U(A_1)$ and $U(A_2)$:

$$\frac{U(A_1) + U(A_2)}{2} = \frac{3(p_1 + p_2 + 2p_0)}{2} - 1 = \frac{3(1 + p_0)}{2} - 1 = 0.50 + 1.50p_0 \ge \$0.50. \tag{12}$$

Because the average of $U(A_1)$ and $U(A_2)$ is at least $+\$0.50$ for *every* conceivable credence distribution $(p_1, p_2, p_0)$, we have:

$$\max\big(U(A_1), U(A_2)\big) \ge \$0.50 > U(A_0) = \$0.$$

This is the mathematical heart of Oesterheld and Conitzer's critique: **even if the buyer applies Joyce's deliberative updating**, there is *no* credence distribution $(p_1, p_2, p_0)$ under which $A_0$ (buying neither box) maximizes causal expected utility! Regardless of what the buyer believes the seller predicted, CDT strictly forbids walking away empty-handed ($A_0$) and compels the buyer to buy either Box 1 or Box 2.

Yet observe what happens when the buyer buys a box—say $A_i$ ($i \in \{1, 2\}$). Because the seller's prediction is $75\%$ accurate, $P(S_i \mid A_i) = 0.75$ and $P(\neg S_i \mid A_i) = 0.25$. Thus, in actual expectation (and according to EDT), buying Box $i$ yields:

$$V(A_i) = 0.75(-1) + 0.25(+2) = -\$0.25 < V(A_0) = \$0.$$

The CDT agent is guaranteed to lose $\$0.25$ in expectation to the seller!

### Operational Proposals for Adversarial and Unstable Cases

How should a mathematically sophisticated practitioner of CDT handle cases like the Adversarial Offer? Stepping beyond the descriptive summary in the reference text, we can synthesize two operational defenses from the cited literature (Harper 1984; Meacham 2010; Joyce 2012, 2020):

1. **Ratifiable Mixed Policies (Randomization):** Why did the seller defeat the buyer in the Adversarial Offer? Because any *deterministic* choice $A_1$ or $A_2$ was anticipated with $75\%$ accuracy. Notice that under Joyce's ratifiability criterion (equation 10), neither $A_1$ nor $A_2$ is ratifiable: if the buyer leans toward $A_1$, then $p_1 = P(S_1 \mid I_{A_1}) = 0.75$, which yields $U(A_1 \mid I_{A_1}) = -0.25$ and $U(A_2 \mid I_{A_1}) = +1.25$, immediately telling the buyer to switch to $A_2$ (and vice versa). Following Harper (1984), when no pure action is ratifiable, a causal decision theorist can expand the action space to include **mixed strategies** $\pi = (\pi_1, \pi_2, 0)$ implemented via an external randomizing device (such as a fair coin flip $\pi = (0.5, 0.5, 0)$). If the seller cannot predict the outcome of a physical coin toss made at the time of choice, then choosing the policy "flip a fair coin between Box 1 and Box 2" breaks the correlation between the coin's realization and $(S_1, S_2)$, ensuring the buyer actually achieves the positive expected value of $\ge +\$0.50$.
2. **Pre-Commitment and Binding (Meacham 2010):** If the agent has an opportunity *prior* to the seller's prediction to bind themselves to a policy (or if the agent evaluates full diachronic policies rather than isolated synchronic acts), the agent's pre-commitment *causally affects* the predictor's state $S_k$. Viewed from an *ex ante* perspective before the prediction is made, CDT itself recommends binding oneself to $A_0$ (or to one-boxing in Newcomb's problem), because at the pre-prediction stage the state $S_k$ is a causal consequence of the agent's commitment rather than an independent background hypothesis.

---

## 6. Summary Procedure for Unfamiliar Cases and Conclusion

To apply causal decision theory systematically to any unfamiliar decision problem, a researcher or practitioner can execute the following four-step operational protocol:

1. **Specify the Decision Frame ($\mathcal{A}, \mathcal{O}, D$):** Enumerate the mutually exclusive available actions $A \in \mathcal{A}$, the possible outcomes $O_j \in \mathcal{O}$, and the utility function $D(O_j)$.
2. **Isolate the Partition of Dependency Hypotheses ($\mathcal{S}$):** Identify a partition of causal background states $\mathcal{S} = \{S_1, \dots, S_K\}$ that are causally upstream of (or causally unaffected by) the present choice $A$, such that within each $S_k$ the outcome distribution $P(O_j \mid A, S_k)$ is free of confounding. (If working directly on a space of possible worlds $W$, define the imaging map $w \mapsto w_A$ by intervening on $A$ while holding $S(w)$ fixed.)
3. **Deliberative Updating and Ratifiability Check:** Before computing expectations, ask whether your inclination $I_A$ to choose a candidate action $A$ provides new evidence about the background states $S_k$ (as in the Psychopath Button or Adversarial Offer). Compute the causal expected utility:
   $$U(A' \mid I_A) = \sum_{k=1}^{K} P(S_k \mid I_A) \sum_{j=1}^{m} P(O_j \mid A', S_k) \, D(O_j).$$
   Seek a **ratifiable** action $A^*$ satisfying $A^* \in \arg\max_{A'} U(A' \mid I_{A^*})$. (When actions and states are independent, or when self-observation yields no asymmetric instability, this reduces directly to maximizing $U(A) = \sum_k P(S_k) D(A \land S_k)$.)
4. **Diagnose Adversarial Instability:** If no pure action is ratifiable (as in Death in Damascus or the Adversarial Offer), check whether an physical randomization device (mixed strategy) can decouple the final choice from the predictor's state, or whether the decision problem must be elevated to a diachronic policy choice prior to the predictor's intervention.

### Conclusion

Causal decision theory represents one of the major triumphs of formal epistemology: by replacing evidential conditional probabilities $P(O_j \mid A)$ with counterfactual probabilities $P(A \to O_j)$, it provides a mathematically rigorous way to separate genuine causal efficacy from mere statistical symptomology. While modern adversarial thought experiments demonstrate that holding fixed one's beliefs about causal states requires subtle epistemic care during deliberation, the core insight of Gibbard, Harper, Lewis, and Joyce remains indispensable across philosophy, economics, and artificial intelligence: rational agency is the art of shaping the future, not managing the news about the past.

---

## References

* Ahmed, Arif (2021). *Evidential Decision Theory*. Cambridge University Press.
* Bellos, Alex (2016). "Newcomb's problem divides philosophers. Which side are you on?" *The Guardian*, 28 November 2016.
* Egan, Andy (2007). "Some counterexamples to causal decision theory." *The Philosophical Review*, 116(1): 93–114.
* Gibbard, Allan, and William L. Harper (1981). "Counterfactuals and two kinds of expected utility." In *Ifs: Conditionals, Belief, Decision, Chance, and Time*, 153–190.
* Greaves, Hilary (2013). "Epistemic decision theory." *Mind*, 122(488): 915–952.
* Harper, William (1984). "Ratifiability and Causal Decision Theory: Comments on Eells and Seidenfeld." *PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association*, 1984(2): 213–228.
* Howard, J. V. (1988). "Cooperation in the Prisoner's Dilemma." *Theory and Decision*, 24(3): 203–213.
* Joyce, James M. (2012). "Regret and instability in causal decision theory." *Synthese*, 187(1): 123–145.
* Joyce, James M. (2020). "Yet Another Refutation of Causal Decision Theory?" Unpublished manuscript, University of Michigan.
* Lewis, David (1976). "Probabilities of conditionals and conditional probabilities." *The Philosophical Review*, 85(3): 297–315.
* Lewis, David (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs*, 8(3): 235–240.
* Lewis, David (1981). "Causal decision theory." *Australasian Journal of Philosophy*, 59(1): 5–30.
* Meacham, Christopher J. G. (2010). "Binding and its consequences." *Philosophical Studies*, 149(1): 49–71.
* Oesterheld, Caspar, and Vincent Conitzer (2021). "Extracting Money from Causal Decision Theorists." *The Philosophical Quarterly*, 71(4): pqaa086.
* Shaffer, Michael John (2009). "Decision Theory, Intelligent Planning and Counterfactuals." *Minds and Machines*, 19(1): 61–92.
* Spencer, Jack (2020). "An argument against causal decision theory." *Analysis*, 81: 52–61.
* Weirich, Paul (2016). "Causal Decision Theory." In Edward N. Zalta (ed.), *Stanford Encyclopedia of Philosophy* (Winter 2016 ed.).
* Wolpert, D. H., and G. Benford (2013). "The lesson of Newcomb's paradox." *Synthese*, 190(9): 1637–1646.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Project Scope**

I'm now zeroing in on defining the precise scope. The goal is clear: a technical piece on Causal Decision Theory (CDT) for an expert audience. I'm focusing on the required format - mathematical essay or blog post - and the desired perspective, that of a researcher.


**Refining the Audience Needs**

I'm now zeroing in on defining the precise audience requirements, and I'm settling on a target length: 2,400–3,000 words. The piece must offer a full formal account of Causal Decision Theory (CDT), complete with definitions, equations, examples, and operational procedures that enable a reader to resolve unfamiliar decision problems using the supplied Wikipedia reference article. I must distinguish source claims from added assumptions.


**Interpreting Source Information**

I'm now grappling with uncertainties within the source material, specifically how to handle vague points and complex issues like imaging regress. I need to develop and justify reasonable operational interpretations for these. Crucially, I'm explicitly distinguishing the source's claims from my added elaborations. The format is set: a readable mathematical essay of around 2,600-2,800 words, including a concise conclusion and references. The core definition of CDT is clear: choosing actions that cause the best expected outcome.


**Formalizing the CDT Equation**

I'm now diving deep into the formal description of Causal Decision Theory (CDT). I'm focusing on the core equation from Gibbard and Harper (1981): $U(A) = \sum_j P(A \to O_j) D(O_j)$. I'm clarifying the meaning of the counterfactual probability, $P(A \to O_j)$, drawing on the Wikipedia text and emphasizing Gibbard & Harper's phrasing, while specifying its counterfactual nature in Stalnaker/Lewis semantics. I'm also examining the difference with EDT, especially Lewis' triviality result, as a key distinction.


**Analyzing Independence & Axioms**

I'm now zeroing in on the Gibbard and Harper (1981) independence result and its axioms, exploring why statistical independence of the action and its causal consequences can simplify CDT. I'm focusing on the counterexample of King David and Bathsheba to understand where this independence fails. I'm also planning to explore Newcomb's paradox and the Prisoner's Dilemma to explore the differences between CDT and EDT in concrete terms.


**Evaluating CDT Algorithms**

I'm now assessing the algorithmic vagueness inherent in Causal Decision Theory (CDT), as highlighted by Shaffer (2009). The "imaging" method, suggested by Lewis (1981), and the associated regress criticism are under evaluation, along with specific counterexamples from Egan (2007) and others. I'm focusing on the disconnect between CDT's rules and intuitive expectations. I'm also considering adversarial offer variants.


**Addressing Paradoxes & Flaws**

I'm currently dissecting specific counterexamples to Causal Decision Theory (CDT), such as the "Two Boxes" scenario. It seems CDT endorses seemingly irrational actions in these cases, leading to losses for the buyer and gains for the seller. Also, diachronic Dutch books are an issue. Further, I am considering the "Psychopath Button" thought experiment by Egan (2007) and Greaves (2013). I'm looking at how CDT, without modification, leads to the endorsement of actions that might seem counterintuitive. I'm exploring the nuances of ratifiability and self-information, as discussed by Joyce (2012, 2020) and Weirich (2016) as a potential remedy.


**Contrasting Decision Paradigms**

I'm now focusing on contrasting Evidential and Causal Decision Theories. The goal is to present the formal structure of CDT and why conditional probabilities fail to capture causal efficacy. I'm developing an operational framework that will help readers apply CDT to solve unfamiliar decision problems. I will show how to handle counterfactuals, dependency hypotheses, and imaging and consider counterexamples where CDT shows instability. I'm also planning to unpack the Gibbard–Harper (1981) equation and contrast it with EDT.


**Clarifying Triviality & Equivalence**

I'm now zeroing in on the mathematical implications of causal decision theory, drawing on the Gibbard–Harper equivalence condition. I'm focusing on the contrast with the formal description of Expected Utility and why $P(A \to O_j)$ doesn't equal $P(O_j \mid A)$ without collapsing the probability space to at most four values. I am also planning to include a brief derivation using Conditional Excluded Middle and Modus Ponens to clarify statistical independence and $P(A \to O_j)$.


**Operationalizing CDT Further**

I'm now detailing an operational recipe. I'm focusing on partitioning into dependency hypotheses or causal states, with the set  $\mathcal{S} = \{S_1, \dots, S_m\}$. I am planning to discuss how we must use conditional probabilities to generate our counterfactual $P(A \to O_j)$ when given some causal state $S_k$. The key aim is to provide an operational bridge, linking abstract counterfactuals to concrete applications of CDT.


**Elaborating Operational Details**

I'm now detailing the operational distinction between CDT and EDT using a state partitioning approach, highlighting the unconditional prior $P(S_k)$ in CDT and the conditional probability $P(S_k \mid A)$ in EDT. I'm focusing on the mathematical clarity this provides and its alignment with Pearl's $do$-calculus. I'm also planning to unpack Lewis's imaging algorithm as an operational method for determining counterfactual probabilities.


**Defining Causal Invariance**

I'm now zeroing in on defining the selection function $f_A: W \to W_A$ on the space of worlds. I'm focusing on pushing forward probability measures, $P^A(w') = \sum_{w: f_A(w) = w'} P(w)$, for computing $P(A \to O_j)$. Also, I'm clarifying Shaffer's regress concern. I'm ready to demonstrate operational clarity by applying causal invariance to this. I'm focusing on defining $f_A$ via causal invariance, to clarify the operational procedure.

I am setting up worked examples for King David, Newcomb's paradox, and a variant of the Prisoner's Dilemma. These applications are to be presented with numerical setups. I'm now explicitly noting parameters supplied to demonstrate scenarios. I will start by defining actions, states, and outcomes for King David and Bathsheba.


**Analyzing Decision Outcomes**

I'm now working through specific decision scenarios. I'm focusing on why EDT suggests abstaining in a problem, while CDT shows strict dominance. I'm preparing a detailed analysis of Newcomb's Paradox, setting up a payoff matrix and calculating utilities under both CDT and EDT, highlighting the dominance argument. I am then showing its isomorphism to a twin Prisoner's Dilemma.

I am also examining modern criticisms, such as the Psychopath Button scenario, from the provided source.


**Operationalizing Counterfactuals**

I'm now detailing a solution for the Psychopath Button scenario. I'm focusing on the contrast between naive CDT and a ratifiable version incorporating deliberative updating to model Joyce's position. This involves introducing conditional probabilities. I'm also preparing for a worked example.

I'm now zeroing in on detailing a concrete mathematical analysis of Oesterheld and Conitzer's Adversarial Offer scenario. I'm setting up the core elements and clarifying the actions, boxes, and prediction accuracy to be used. This will illustrate another paradox where CDT shows an advantage.


**Operationalizing Paradoxes**

I'm now detailing an operational solution for the Adversarial Offer scenario. I'm focusing on the mathematical setup, clarifying box values and prediction probabilities. I'm working through the buyer's perspective. Also, I am planning to demonstrate why naive CDT, without incorporating ratifiability or mixed strategies, leads to losses. This highlights a limitation I'll address in the worked example.



**Formulating a Summary**

I'm now formulating the final summary and conclusion. I will provide a step-by-step checklist for applying CDT and offer a concluding synthesis on its elegance and philosophical status. I am also planning a concise list of key references. Finally, I'm ensuring all claims from the source are explicitly distinguished from my assumptions.



**Refining Formatting & Length**

I'm now implementing the LaTeX formatting with inline math notation and carefully monitoring section word counts to stay within the 2,400-3,000 word target. I'm focusing on the derivation of the Gibbard-Harper equivalence condition, including the axioms for Conditional Excluded Middle and Centering, to clarify why statistical independence allows  $P(A \to O_j) = P(O_j \mid A)$. I'm planning to write out the formal proof clearly.


**Deriving Mathematical Proofs**

I'm now zeroing in on including key mathematical proofs to bolster the essay's formal rigor. I've successfully crafted a clean, illuminating demonstration of the equivalence claim. It explicitly explains the rationale behind the crucial statistical independence claim and directly justifies the claim provided in the source. I'm also planning to incorporate the mathematics from the adversarial offer example.


**Calculating Expected Outcomes**

I'm now calculating the expected outcomes of each action in the adversarial offer scenario. I am formalizing the probabilities for the buyer's actions ($A_1, A_2, A_0$) conditional on the states of the world ($S_1, S_2, S_0$). I'm also planning to explicitly introduce the prior probabilities for each state, ensuring a full mathematical framework.



**Calculating Scenario Outcomes**

I'm now calculating the final expected outcomes for the buyer in the Adversarial Offer scenario. I'm finalizing the formal probability setup, as well as clarifying the outcomes for actions A1, A2, and A0. The average causal expected utility of boxes $A_1$ and $A_2$ is at least $0.50$, thus CDT strictly forbids choosing $A_0$. However, I am aware that the buyer's evidential expected net payoff will be negative, even though CDT prefers one of those outcomes.


```
