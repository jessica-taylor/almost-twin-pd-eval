# Causal Decision Theory: Foundations, Formalisms, and Dilemmas

Decision theory formalizes the choices of an agent seeking to optimize outcomes in an uncertain world. In classical expected utility theory, an agent assigns subjective probabilities to states of nature and evaluates acts according to their expected desirability. However, standard formulations often leave ambiguous what kind of probability is being calculated: conditional belief given that an act is chosen, or the probability that the act *causes* the outcome to occur. 

This ambiguity separates two rival frameworks: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. EDT advises an agent to choose the action that provides the best epistemic "news"—the action conditioning on which yields the highest expected utility. CDT rejects this criterion, arguing that rational choice must track the *efficacious consequences* of actions rather than mere correlation or symptomhood.

Below, we develop the mathematical apparatus of CDT, explore its treatment of dependencies and counterfactual conditionals, contrast it with EDT through standard thought experiments, and address its formal ambiguities and contemporary criticisms.

---

## 1. The Core Divergence: Causation vs. News-Value

Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be a finite partition of mutually exclusive and exhaustive actions available to the agent, and let $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ be a partition of possible outcomes. The agent's preferences over outcomes are represented by a utility (or desirability) function $V \colon \mathcal{O} \to \mathbb{R}$.

In standard Evidential Decision Theory (as formalized, for instance, in Richard Jeffrey's logic of decision), the value of an action $A \in \mathcal{A}$ is given by its evidential expected utility:
$$
U_{\mathrm{EDT}}(A) = \sum_{j=1}^m P(O_j \mid A)\, V(O_j),
$$
where $P$ is the agent's subjective probability distribution over a suitable algebra of propositions. Here, $P(O_j \mid A)$ denotes the standard Kolmogorov conditional probability:
$$
P(O_j \mid A) = \frac{P(A \land O_j)}{P(A)}, \quad \text{for } P(A) > 0.
$$
$U_{\mathrm{EDT}}(A)$ measures the expectation of utility conditional on receiving the "news" that $A$ has occurred. 

CDT contends that EDT falls victim to spurious correlation whenever an action serves as a diagnostic sign of an outcome without exercising any causal leverage over it. If a common cause induces a statistical correlation between an act and an outcome, EDT may instruct the agent to act merely to generate reassuring evidence about factors already outside their control.

To correct this, CDT replaces conditional probabilities with probabilities that reflect causal efficacy.

---

## 2. Formal Formulations of Causal Expected Utility

Historically, CDT has been formulated in two mathematically distinct but closely related ways: via **counterfactual conditionals** (Gibbard and Harper) and via **dependency hypotheses** or causal states (Lewis, Skyrms). In modern applied contexts, it is frequently operationalized using **structural causal models** (Pearl's do-calculus).

### 2.1 The Gibbard–Harper Counterfactual Formulation

Allan Gibbard and William Harper (1981) formalize CDT using counterfactual conditionals. Let $A \mathbin{\Box\to} O$ denote the subjunctive conditional: *"If the agent were to do $A$, then $O$ would occur."*

The causal expected utility of an action $A$ is defined as:
$$
U_{\mathrm{CDT}}(A) = \sum_{j=1}^m P(A \mathbin{\Box\to} O_j)\, V(O_j).
$$
To evaluate this expectation, one must define the probability of a counterfactual, $P(A \mathbin{\Box\to} O_j)$.

A central mathematical milestone in conditional logic is David Lewis's **Triviality Theorem** (1976). Lewis proved that, under mild closure conditions, the probability of a conditional cannot generally equal the conditional probability:
$$
P(A \mathbin{\Box\to} O) \neq P(O \mid A).
$$
Specifically, if one identifies $P(A \mathbin{\Box\to} \cdot)$ with $P(\cdot \mid A)$ across all propositions in non-trivial probability spaces, the probability function collapses to an at most four-valued measure. Hence, $U_{\mathrm{CDT}}$ and $U_{\mathrm{EDT}}$ represent genuinely distinct functionals.

Gibbard and Harper demonstrated that $P(A \mathbin{\Box\to} O_j) = P(O_j \mid A)$ holds if the choice of $A$ is statistically independent of the counterfactual conditional itself:
$$
P(A \mathbin{\Box\to} O_j \mid A) = P(A \mathbin{\Box\to} O_j).
$$
Under the Principle of Conditional Excluded Middle (CEM)—which states that $(A \mathbin{\Box\to} O) \lor (A \mathbin{\Box\to} \neg O)$ is a logical truth—the conditionals partition the space of causal consequences. When $A$ and the truth of $A \mathbin{\Box\to} O_j$ are correlated, EDT and CDT diverge.

### 2.2 Lewis's Formulation via Dependency Hypotheses

David Lewis (1981) bypassed primitive counterfactual operators by partitioning the state space into maximal **dependency hypotheses**. 

Let $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$ be a partition of mutually exclusive and exhaustive propositions specifying the complete causal setup of the world outside the agent's immediate control. Each $K \in \mathcal{K}$ details exactly how every outcome $O \in \mathcal{O}$ depends causally upon every available action $A \in \mathcal{A}$.

Under a specific dependency hypothesis $K$, the objective propensity (or deterministic guarantee) of action $A$ yielding outcome $O_j$ is fixed, denoted $P_K(O_j \mid A)$ (or simply $1$ if $A$ deterministically yields $O_j$ under $K$). The agent's causal expected utility is the expectation weighted across their subjective credences $P(K)$ in these hypotheses:
$$
U_{\mathrm{CDT}}(A) = \sum_{K \in \mathcal{K}} P(K) \sum_{j=1}^m P_K(O_j \mid A)\, V(O_j).
$$
Crucially, Lewis's algorithm requires the agent to weight each $K$ by its **unconditional credence** $P(K)$, rather than the conditional credence $P(K \mid A)$. This captures the causal intuition that one's present choice cannot retroactively alter which state of the world $K$ actually obtains.

---

## 3. Resolving the Operational Ambiguity: Lewisian Imaging vs. Pearlian Interventions

The Wikipedia summary notes a major formal critique: CDT does not intrinsically specify a mechanical algorithm for computing $P(A \mathbin{\Box\to} O)$ or constructing $\mathcal{K}$. Below, we analyze Lewis's proposed technique (imaging) and develop a modern operational alternative based on structural causal models.

### 3.1 Lewisian Imaging

To compute credences in conditionals, Lewis proposed the mathematical operation of **imaging**. 

Let $W$ be a set of possible worlds, and let $P \colon \mathcal{P}(W) \to [0, 1]$ be a probability distribution over subsets of $W$. Suppose there exists a selection function $s \colon W \times \mathcal{A} \to W$, where $s(w, A) = w_A$ is the "closest" or most similar world to $w$ in which $A$ is true.

The *image* of $P$ on $A$, denoted $P_A$, transfers the probability mass of each world $w$ entirely to its closest $A$-counterpart:
$$
P_A(w') = \sum_{\{w \in W : s(w, A) = w'\}} P(w).
$$
The probability of the conditional proposition is then equated with the probability of the consequent under the imaged distribution:
$$
P(A \mathbin{\Box\to} O) = P_A(O) = \sum_{w \in W} P(w)\, \mathbf{1}_O(s(w, A)).
$$
While mathematically well-defined on a fixed metric space of worlds, imaging faces significant operational hurdles in practice. As noted in the source material, evaluating similarity relations among worlds requires assigning credences to conditionals, which risks an infinite epistemic regress or subjective arbitrariness in selecting the metric.

### 3.2 A Modern Operationalization: Structural Causal Models and the Do-Calculus

*(Note: While Judea Pearl's do-calculus is widely used in contemporary causal analysis, its explicit mapping to Gibbard–Harper CDT represents an operational extension beyond the historical reference text.)*

A rigorous, computable realization of CDT can be formulated using a **Structural Causal Model (SCM)**. An SCM is a 4-tuple $\mathcal{M} = \langle U, V, F, P(U) \rangle$, where:
- $U$ is a set of exogenous (background) variables determined by factors outside the model, distributed according to $P(U)$.
- $V$ is a set of endogenous variables.
- $F = \{f_X \mid X \in V\}$ is a set of deterministic functions such that each endogenous variable is determined by its parents:
  $$
  X = f_X(\mathrm{PA}_X, U_X).
  $$

An agent's choice of an action corresponds to an **intervention**, formalized by the $\mathrm{do}$-operator, $\mathrm{do}(A = a)$. This intervention mathematically replaces the structural equation for $A$ with the constant assignment $A = a$, severing all incoming graphical arrows from the parents of $A$ while leaving the remainder of the system invariant:
$$
f_A(\mathrm{PA}_A, U_A) \implies a.
$$
In this framework, the causal expected utility is calculated by taking expectations with respect to the interventional distribution:
$$
U_{\mathrm{SCM}}(a) = \sum_{y} P(Y = y \mid \mathrm{do}(A = a))\, V(y),
$$
where:
$$
P(Y = y \mid \mathrm{do}(A = a)) = \sum_{u} P(U = u)\, \mathbf{1}_{\{Y_{\mathcal{M}[a]}(u) = y\}}.
$$
This gives an unambiguous, algorithmic interpretation of CDT:
1. **Evidential updating** conditions on observations: $P(Y \mid A=a)$ utilizes standard Bayesian conditioning across the unmodified joint distribution $P(U, V)$.
2. **Causal evaluation** surgically modifies the causal graph via $\mathrm{do}(A = a)$, evaluating the distribution of outcomes while preserving the baseline distribution of exogenous confounders $P(U)$.

---

## 4. Canonical Applications: Common Causes and Asymmetric Information

To see CDT in action, we contrast its prescriptions with those of EDT across two classical scenarios involving confounding.

### 4.1 King David and Bathsheba

Gibbard and Harper introduced the historical-psychological example of King David:
- David contemplates whether to summon Bathsheba ($A$) or abstain ($\neg A$).
- Kings are either charismatic ($C$) or uncharismatic ($\neg C$). Charisma is fixed from birth by genetics and early environment and cannot be changed by adult actions.
- Uncharismatic kings face frequent, successful rebellions ($R$); charismatic kings face them rarely.
- Unjust acts do not cause rebellions; rebellions are caused by the general "ignoble bearing" typical of uncharismatic kings.
- David does not know his charisma status, but he knows summoning another man's wife is unjust, and that uncharismatic kings are far more prone to unjust acts than charismatic kings.

Let the causal structure be represented as:
$$
C \longrightarrow A, \quad C \longrightarrow \neg R.
$$
Charisma $C$ acts as a common cause (confounder) between summoning Bathsheba ($A$) and avoiding revolt ($\neg R$). 

#### The EDT Analysis
Because uncharismatic kings commit unjust acts far more frequently:
$$
P(C \mid A) \ll P(C \mid \neg A).
$$
Since revolts depend heavily on charisma:
$$
P(R \mid A) = P(R \mid C)P(C \mid A) + P(R \mid \neg C)P(\neg C \mid A) > P(R \mid \neg A).
$$
If the disutility of a revolt outweighs the pleasure of summoning Bathsheba, EDT calculates:
$$
U_{\mathrm{EDT}}(A) < U_{\mathrm{EDT}}(\neg A).
$$
EDT instructs David to abstain, treating his choice as a diagnostic indicator of his own innate charisma.

#### The CDT Analysis
CDT considers the counterfactual consequences of David's action. Because David's adult choice cannot causally affect his innate charisma $C$:
$$
P(A \mathbin{\Box\to} C) = P(C), \quad P(A \mathbin{\Box\to} \neg C) = P(\neg C).
$$
Because the presence or absence of a revolt $R$ is causally governed by $C$ and not by $A$:
$$
P(A \mathbin{\Box\to} R) = P(C) P(R \mid C) + P(\neg C) P(R \mid \neg C) = P(\neg A \mathbin{\Box\to} R).
$$
The risk of revolt is causally invariant under David's choice. Letting $V(B)$ be the utility of summoning Bathsheba and $V(R)$ be the disutility of revolt:
$$
U_{\mathrm{CDT}}(A) = V(B) + \mathbb{E}[\text{Revolt Penalty}],
$$
$$
U_{\mathrm{CDT}}(\neg A) = 0 + \mathbb{E}[\text{Revolt Penalty}].
$$
Because $V(B) > 0$, CDT recommends sending for Bathsheba. CDT views David's abstinence as an irrational attempt to suppress bad news about an unalterable past state.

### 4.2 Newcomb's Paradox

Newcomb's problem formalizes the divergence between dominance reasoning and indicative conditioning.

An agent faces two boxes:
- **Box 1** (transparent): contains $\$1,000$.
- **Box 2** (opaque): contains either $\$1,000,000$ or $\$0$.

The agent may choose:
- $A_1$: Take only Box 2 ("One-box").
- $A_2$: Take both Box 1 and Box 2 ("Two-box").

A reliable Predictor made a prediction yesterday:
- If the Predictor predicted $A_1$, they placed $\$1,000,000$ in Box 2.
- If the Predictor predicted $A_2$, they left Box 2 empty.
Assume the Predictor is accurate with probability $p = 0.99$.

```
         Causal Graph for Newcomb's Problem
         
                 [Predictor's Brain]
                    /           \
         Prediction/             \ Predictor's Setup
                  v               v
           [Agent's Choice]    [Box 2 Content: $0 or $1M]
                  |                     |
                  +---------->[Payout]<--+
                                ^
                                |
                         [Box 1: $1,000]
```

#### EDT: One-Boxing
EDT evaluates the expected utility conditional on taking the actions:
$$
U_{\mathrm{EDT}}(A_1) = p \cdot \$1,000,000 + (1-p) \cdot \$0 = 0.99 \times 10^6 = \$990,000,
$$
$$
U_{\mathrm{EDT}}(A_2) = (1-p) \cdot (\$1,000,000 + \$1,000) + p \cdot \$1,000 = 0.01 \times 1,001,000 + 0.99 \times 1,000 = \$11,000.
$$
Because $U_{\mathrm{EDT}}(A_1) \gg U_{\mathrm{EDT}}(A_2)$, EDT firmly recommends one-boxing.

#### CDT: Two-Boxing
CDT sets up the dependency hypotheses regarding the contents of Box 2:
- $K_{\mathrm{full}}$: Box 2 contains $\$1,000,000$.
- $K_{\mathrm{empty}}$: Box 2 contains $\$0$.

Because the contents of Box 2 were fixed yesterday, the agent's current act has no backward causal efficacy on Box 2:
$$
A_i \mathrel{\rlap{\to}/\mkern-3mu\to} K.
$$
Formally, under counterfactual semantics:
$$
P(A_1 \mathbin{\Box\to} K_{\mathrm{full}}) = P(A_2 \mathbin{\Box\to} K_{\mathrm{full}}) = P(K_{\mathrm{full}}).
$$
Evaluating the causal expected utility:
$$
U_{\mathrm{CDT}}(A_1) = P(K_{\mathrm{full}}) \cdot \$1,000,000 + P(K_{\mathrm{empty}}) \cdot \$0,
$$
$$
U_{\mathrm{CDT}}(A_2) = P(K_{\mathrm{full}}) \cdot (\$1,001,000) + P(K_{\mathrm{empty}}) \cdot (\$1,000).
$$
Subtracting the two yields:
$$
U_{\mathrm{CDT}}(A_2) - U_{\mathrm{CDT}}(A_1) = P(K_{\mathrm{full}})(1,001,000 - 1,000,000) + P(K_{\mathrm{empty}})(1,000 - 0) = \$1,000.
$$
Regardless of the probability $P(K_{\mathrm{full}})$, $U_{\mathrm{CDT}}(A_2) - U_{\mathrm{CDT}}(A_1) = \$1,000 > 0$. Two-boxing strictly causally dominates one-boxing. CDT agents conclude that whatever is in Box 2 is already there; leaving Box 1 behind simply discards a guaranteed $\$1,000$.

---

## 5. Pathologies and Counterexamples: The Problem of Instability

Despite its philosophical popularity, CDT faces critical challenges. A central class of counterexamples demonstrates that CDT can produce unstable deliberations, voluntarily forgo guaranteed payoffs, or expose agents to sure losses (Dutch books).

### 5.1 Andy Egan's Psychopath Button

Andy Egan (2007) introduced decision problems where an action provides dramatic evidence about the causal structure of the world, making the act seem desirable before it is chosen, but undesirable the moment it is adopted.

Consider the **Psychopath Button**:
- Paul can push a button ($B$) to eliminate all psychopaths from earth, or leave it unpressed ($\neg B$).
- Paul considers a world without psychopaths to be vastly superior to the status quo ($+100$).
- If Paul is himself a psychopath, pressing the button will kill him along with the others (utility $-1000$).
- Living in a world with psychopaths while surviving yields utility $0$.
- Paul's initial credence that he is a psychopath is very low: $P(\mathrm{Psy}) = 0.01$.
- However, Paul is certain that *only* a psychopath would press such a button: $P(\mathrm{Psy} \mid B) = 1$, whereas $P(\mathrm{Psy} \mid \neg B) = 0$.

```
         Paul's Epistemic Deliberation Cycle
         
          Start: P(Psy) = 0.01
             |
             v
       CDT evaluates B:
       Holding P(Psy) fixed, expected value is positive!
             |
             v
       Paul forms intention to press B
             |
             v
       Self-observation: "I am about to press B"
             |
             v
       Update: P(Psy | intending B) -> 1
             |
             v
       CDT re-evaluates B:
       Death is certain! Expected value is -1000.
             |
             v
       Paul abandons intention to press B
             |
             v
       Update: P(Psy | intending ~B) -> 0 (Cycle repeats)
```

#### The CDT Dilemma
Because whether Paul is a psychopath is a fixed biological or psychological fact, pressing the button does not *cause* him to become a psychopath:
$$
P(B \mathbin{\Box\to} \mathrm{Psy}) = P(\mathrm{Psy}) = 0.01.
$$
CDT evaluates the button press by holding this unconditional credence fixed:
$$
U_{\mathrm{CDT}}(B) = P(\mathrm{Psy}) \cdot (-1000) + (1 - P(\mathrm{Psy})) \cdot (100) = 0.01(-1000) + 0.99(100) = -10 + 99 = +89.
$$
$$
U_{\mathrm{CDT}}(\neg B) = 0.
$$
Since $89 > 0$, CDT instructs Paul to press the button. 

Yet virtually everyone agrees that pressing the button is reckless: Paul knows that if he actually pushes it, he will do so only because he is a psychopath, thereby guaranteeing his own death. Egan points out that CDT demands this choice because it holds fixed the agent's *unconditional credences* in dependency hypotheses, deliberately ignoring what the choice reveals about the agent themselves.

### 5.2 Deliberational Instability and "Death in Damascus"

This issue leads directly to the phenomenon of **unratifiability** (first analyzed systematically by Richard Jeffrey and William Harper).

In the classical tale **Death in Damascus**:
- An agent is in Damascus and must choose between staying in Damascus ($D$) or fleeing to Aleppo ($A$).
- Death has made an appointment with the agent for tomorrow in one of the two cities.
- Death is an exceptional predictor of the agent's movements ($p \approx 1$).
- If the agent meets Death, utility is $-100$; if the agent avoids Death, utility is $0$.

Suppose the agent currently plans to stay in Damascus ($D$). If Death predicted $D$, Death is in Damascus. Then going to Aleppo ($A$) would save the agent's life:
$$
U_{\mathrm{CDT}}(A) > U_{\mathrm{CDT}}(D).
$$
The agent resolves to go to Aleppo. But as soon as the agent decides to go to Aleppo, they must update their credence about where Death is waiting: Death likely predicted Aleppo. Under this updated belief:
$$
U_{\mathrm{CDT}}(D) > U_{\mathrm{CDT}}(A).
$$
The agent's rational recommendation oscillates continuously. An action $A$ is defined as **ratifiable** if and only if:
$$
U_{\mathrm{CDT}}(A \mid A) \ge U_{\mathrm{CDT}}(A' \mid A) \quad \forall A' \in \mathcal{A},
$$
where $U_{\mathrm{CDT}}(\cdot \mid A)$ denotes causal utility computed with credences conditioned on the proposition that the agent performs $A$. In Death in Damascus, *neither* action is ratifiable.

### 5.3 The Adversarial Offer and Exploitation

Recent work by Spencer (2020), Joyce (2020), and Oesterheld & Conitzer (2021) demonstrates that CDT's insensitivity to self-predictive correlation allows external adversaries to systematically extract money from causal decision theorists.

Consider the **Adversarial Offer**:
- Two boxes ($B_1$ and $B_2$) cost $\$1$ each to purchase.
- The player may purchase at most one box: $\mathcal{A} = \{\text{Buy } B_1, \text{Buy } B_2, \text{Decline}\}$.
- Yesterday, a seller predicted the buyer's choice with accuracy $p = 0.75$.
- The seller placed $\$3$ into each box that she predicted the buyer would **not** buy.
- If the seller predicted the player would buy nothing, she placed $\$3$ in both boxes.

#### CDT's Calculation
Let the state space denote the distribution of money:
- $S_1$: Box 1 has $\$3$, Box 2 has $\$0$.
- $S_2$: Box 1 has $\$0$, Box 2 has $\$3$.
- $S_{12}$: Both boxes have $\$3$.

The buyer reasons causally: the money was deposited yesterday. The act of buying cannot causally affect what is inside either box. 

By the rules of the game, the seller places $\$3$ in *at least one box* in every contingency:
- If the seller predicts $B_1$, Box 2 receives $\$3$.
- If the seller predicts $B_2$, Box 1 receives $\$3$.
- If the seller predicts Decline, both receive $\$3$.

Therefore, the total amount of money in the two boxes is at least $\$3$. By symmetry, the causal expected value of the money inside any given box must be at least:
$$
\mathbb{E}_{\mathrm{causal}}[\text{Contents of } B_i] \ge \frac{\$3}{2} = \$1.50.
$$
Since each box costs only $\$1.00$, the net causal expected gain of purchasing a box is:
$$
U_{\mathrm{CDT}}(\text{Buy } B_i) = \$1.50 - \$1.00 = +\$0.50.
$$
Meanwhile, declining yields $\$0.00$. Hence, CDT strictly prefers buying a box over declining.

#### The Consequence
Because the buyer is predictable ($p = 0.75$), whenever the buyer decides to purchase a box (say, $B_1$), it is $75\%$ likely that the seller anticipated this and left $B_1$ empty. The buyer's realized return from the purchase is:
$$
\mathbb{E}[\text{Return}] = 0.25 \times (\$3 - \$1) + 0.75 \times (\$0 - \$1) = 0.50 - 0.75 = -\$0.25.
$$
The seller systematically extracts an average of $\$0.25$ per round from a standard CDT agent. 

Oesterheld and Conitzer (2021) show that this vulnerability can be generalized into formal **diachronic Dutch books**: by presenting sequences of choices where dependency hypotheses correlate with the agent's inclinations, an exploiter can extract guaranteed wealth from a CDT agent who refuses to condition on their own actions.

---

## 6. Modern Defenses: Jim Joyce and Deliberational Dynamics

How do defenders of CDT respond to these apparent failures? The most prominent defense comes from Jim Joyce (2012, 2020), who argues that the standard statement of CDT is static and incomplete, and must be embedded within a model of **deliberational dynamics**.

Joyce contends that an agent does not choose in an epistemic vacuum with fixed credences. Instead, deliberation is an iterative cognitive process:

1. **Initial Credence**: The agent starts with an initial probability distribution over actions, $P_0(A)$.
2. **Evolving Self-Information**: As the agent deliberates and observes their own inclinations toward an action $A$, their probability distribution shifts toward $A$.
3. **Continuous Updating**: The agent updates their credences in the dependency hypotheses $K$ to reflect this self-observation:
   $$
   P_t(K) = P_0(K \mid P_t(A)).
   $$
4. **Equilibrium (Mixed Strategies)**: When faced with unstable problems like Death in Damascus or the Psychopath Button, the deliberate state evolves until the agent reaches an equilibrium state—often a mixed state where the causal expected utilities of the options equalize:
   $$
   U_{\mathrm{CDT}}(A_1) = U_{\mathrm{CDT}}(A_2) = \dots = U_{\mathrm{CDT}}(A_k).
   $$

In the Adversarial Offer, a fully deliberating Joyceian CDT agent would recognize their own predictability during deliberation, driving their subjective value of purchasing down to match its true post-deliberative expectation, thereby avoiding deterministic exploitation. 

However, whether Joyce's deliberational dynamics truly rescues CDT remains contested. Critics point out that modifying credences during deliberation risks blurring the fundamental philosophical line between choosing an action and observing an event, threatening the conceptual foundation that originally separated CDT from EDT.

---

## 7. Comparative Summary

| Scenario | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Mathematical Reason for Divergence |
| :--- | :--- | :--- | :--- |
| **Newcomb's Problem** | One-box ($\$1,000,000$) | Two-box ($\$1,000 + \text{Box 2}$) | $P(\text{Full} \mid A_1) \gg P(\text{Full} \mid A_2)$, but $P(A_i \mathbin{\Box\to} \text{Full})$ is invariant under choice. |
| **King David** | Abstain from Bathsheba | Send for Bathsheba | Common cause (innate charisma) induces correlation without causal connection. |
| **Psychopath Button** | Do not press button | Press button (static formulation) | Common cause (psychopathy); CDT holds $P(\mathrm{Psy})$ fixed while EDT conditions on action. |
| **Adversarial Offer** | Decline offer | Purchase a box | CDT treats box contents as causally fixed; fails to account for predictive exploitation. |

---

## 8. Conclusion

Causal Decision Theory provides an intuitive response to the failures of standard evidential conditioning in the presence of confounding. By demanding that an agent maximize expected *causal consequences*—formalized via counterfactual probabilities $P(A \mathbin{\Box\to} O)$, dependency hypotheses, or structural interventions $\mathrm{do}(A)$—CDT preserves the core principle that rational agents should manage what they can control, rather than manage what they can merely diagnose.

Yet, this insistence on holding fixed unconditional credences in past or causal states creates vulnerabilities of its own. As illustrated by the Psychopath Button, Death in Damascus, and recent adversarial Dutch book constructions, completely divorcing action evaluation from the diagnostic news that the action conveys can lead to severe deliberational instability and systematic monetary loss. 

Whether CDT can resolve these paradoxes via deliberational dynamics, or whether it must ultimately yield to newer alternatives—such as functional, benchmark, or timelike decision theories—remains one of the most vibrant open debates in the mathematical foundations of choice.

---

## References

1. Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
2. Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
3. Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer.
4. Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
5. Joyce, J. M. (2020). *Yet Another Refutation of Causal Decision Theory?*
6. Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
7. Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
8. Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4).
9. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
10. Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.
11. Weirich, P. (2016). Causal Decision Theory. In E. N. Zalta (Ed.), *The Stanford Encyclopedia of Philosophy*.