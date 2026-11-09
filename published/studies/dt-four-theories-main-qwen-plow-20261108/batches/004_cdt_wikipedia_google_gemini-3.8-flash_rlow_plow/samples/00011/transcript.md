# 004_cdt_wikipedia_google_gemini-3.8-flash_rlow_plow / 00011

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/50384505-737d-45a8-9fb7-fc90dbb5074a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/50384505-737d-45a8-9fb7-fc90dbb5074a/call_0/response.raw) · finish: `stop`

### Visible response

````text
# Causal Decision Theory: Foundations, Formalisms, and Dilemmas

Decision theory seeks a normative calculus for agency: given an agent’s beliefs, preferences, and available alternatives, which act ought they to choose? In classical Bayesian decision theory, as formulated by Frank Ramsey, Leonard Savage, and Richard Jeffrey, rational choice is characterized as maximizing expected utility. However, a profound schism emerges when an agent's available actions correlate with external states of affairs without *causing* those states. 

Consider **Evidential Decision Theory (EDT)**. In EDT, an agent assesses an act by the "news value" it carries: what is the conditional probability of favorable outcomes given that the act is performed? While mathematically parsimonious, EDT famously leads agents to treat their own actions as mere epistemic tokens. When an action is symptomatic of a desirable state that the action itself cannot bring about, EDT prescribes managing symptoms rather than intervening on causes.

To rectify this pathology, **Causal Decision Theory (CDT)** asserts that rational choice must be governed exclusively by the causal efficacy of acts. An agent should select an act that brings about the best outcomes in expectation, holding fixed whatever the agent cannot causally influence. 

Below, we develop the mathematical foundations of CDT, contrast its operational mechanisms with EDT, examine its classic canonical problem settings (such as Newcomb's paradox), address the computational and operational ambiguities inherent in counterfactual semantics, and analyze modern instability challenges such as the Psychopath Button and the Adversarial Offer.

---

## 1. Formal Formulations of Decision Theories

Let $\mathcal{A} = \{A_1, A_2, \dots, A_n\}$ be a mutually exclusive and exhaustive set of available acts, and let $\mathcal{O} = \{O_1, O_2, \dots, O_m\}$ be a mutually exclusive and exhaustive set of outcomes. The agent assigns a real-valued utility (or desirability) $D(O_j) \in \mathbb{R}$ to each outcome $O_j$, representing their subjective preferences over outcomes up to positive affine transformations. The agent also maintains a subjective probability distribution (credence function) $P$ over an algebra of propositions containing acts, outcomes, and background states of the world.

### 1.1 Evidential Decision Theory (EDT)
In EDT (formalized by Richard Jeffrey), the desirability $V(A)$ of an act $A \in \mathcal{A}$ is computed via standard conditional probabilities:

$$V(A) = \sum_{j=1}^m P(O_j \mid A) D(O_j)$$

where $P(O_j \mid A) = \frac{P(O_j \wedge A)}{P(A)}$, assuming $P(A) > 0$. Under EDT, an act is evaluated according to how happy the agent would be to learn that they had chosen $A$.

### 1.2 Causal Decision Theory: The Counterfactual Formulation
As Allan Gibbard and William Harper (1981) demonstrated, news value diverges from causal value whenever correlation dissociates from causation. Gibbard and Harper formalized CDT by defining the causal expected utility $U(A)$ in terms of counterfactual conditionals:

$$U(A) = \sum_{j=1}^m P(A \to O_j) D(O_j)$$

Here, $A \to O_j$ denotes the counterfactual proposition: *"If the agent were to perform act $A$, outcome $O_j$ would obtain."* 

The probability $P(A \to O_j)$ is the agent's credence in this counterfactual proposition. Crucially, David Lewis (1976) proved via his famous "triviality result" that the probability of a conditional $P(A \to O_j)$ cannot in general be identified with the conditional probability $P(O_j \mid A)$. If $P(A \to B) = P(B \mid A)$ held universally across arbitrary propositions, the underlying probability measure $P$ would collapse into a trivial measure taking at most four values. Hence, $U(A)$ and $V(A)$ are mathematically and conceptually distinct.

Gibbard and Harper demonstrated that if one assumes the **Principle of Conditional Excluded Middle (CEM)**—namely, that for any conditional, $(A \to B) \vee (A \to \neg B)$ is valid—and one additional axiom of conditional logic, then $P(A \to O_j) = P(O_j \mid A)$ if and only if the act $A$ is statistically independent of the conditional proposition $A \to O_j$:

$$P((A \to O_j) \wedge A) = P(A \to O_j) P(A)$$

When an agent believes their choice of $A$ provides evidence about the truth of $A \to O_j$ without causing it, statistical independence fails, and EDT and CDT diverge.

### 1.3 Causal Decision Theory: The Dependency Hypothesis Formulation
An alternative, equivalent formulation developed by David Lewis (1981) bypasses the direct assignment of probabilities to conditional sentences by introducing **dependency hypotheses**. 

Let $\mathcal{K} = \{K_1, K_2, \dots, K_r\}$ be a partition of maximally specific propositions concerning how the world causally depends on the agent's actions. Each $K \in \mathcal{K}$ is a complete specification of what causal consequences would ensue from every act $A \in \mathcal{A}$. Because $K$ specifies the entire causal background outside the agent's immediate control, the agent's choice of $A$ cannot causally influence which $K$ is actual.

Under Lewis's framework, the causal expected utility is defined as:

$$U(A) = \sum_{K \in \mathcal{K}} P(K) \sum_{j=1}^m P(O_j \mid A \wedge K) D(O_j)$$

Because a dependency hypothesis $K$ completely fixes the causal link from $A$ to the outcomes, the probability $P(O_j \mid A \wedge K)$ is typically either deterministic ($0$ or $1$) or purely objective chance. The agent's subjective uncertainty about the causal environment is captured entirely by the prior distribution $P(K)$ over the dependency hypotheses, which is held fixed across all prospective choices $A$.

---

## 2. A Concrete Comparison: The King David Problem

To see how the two formalisms operate on identical beliefs, consider Gibbard and Harper's historical vignette involving King David and Bathsheba.

### 2.1 The Scenario
King David is considering whether to summon Bathsheba ($A$) or abstain ($\neg A$). David wants Bathsheba, but fears provoking a successful revolt ($R$). Sociological observation has revealed:
1. Kings are either charismatic ($C$) or uncharismatic ($\neg C$). Charisma is an unalterable genetic and psychological disposition determined in childhood.
2. Charismatic kings act justly; uncharismatic kings act unjustly. Summoning Bathsheba is unjust.
3. Uncharismatic kings frequently suffer revolts because of their general bearing and lack of authority, whereas charismatic kings rarely suffer revolts.
4. Crucially: *The unjust act of summoning Bathsheba does not cause a revolt.* The revolt is causally triggered purely by the king’s uncharismatic bearing.
5. David does not know his charisma type, but knows his desires.

### 2.2 Mathematical Evaluation
Let the outcomes and utilities be:
- $O_1 = A \wedge \neg R$ (Summons, no revolt): $D(O_1) = 20$
- $O_2 = A \wedge R$ (Summons, revolt): $D(O_2) = 0$
- $O_3 = \neg A \wedge \neg R$ (Abstains, no revolt): $D(O_3) = 10$
- $O_4 = \neg A \wedge R$ (Abstains, revolt): $D(O_4) = -10$

Let the prior credences over charisma be $P(C) = 0.5$ and $P(\neg C) = 0.5$. Because charismatic kings almost never act unjustly, David's epistemic likelihoods are:
- $P(A \mid C) = 0.1 \implies P(\neg A \mid C) = 0.9$
- $P(A \mid \neg C) = 0.8 \implies P(\neg A \mid \neg C) = 0.2$

By Bayes' theorem, learning that he chose $A$ leads to the posterior credence:
$$P(\neg C \mid A) = \frac{P(A \mid \neg C)P(\neg C)}{P(A \mid \neg C)P(\neg C) + P(A \mid C)P(C)} = \frac{0.8 \times 0.5}{(0.8 \times 0.5) + (0.1 \times 0.5)} = \frac{0.4}{0.45} \approx 0.889$$
Consequently, $P(C \mid A) \approx 0.111$. Similarly, for $\neg A$:
$$P(C \mid \neg A) = \frac{0.9 \times 0.5}{(0.9 \times 0.5) + (0.2 \times 0.5)} = \frac{0.45}{0.55} \approx 0.818$$

Suppose the probability of revolt given charisma type is purely dispositional:
- $P(R \mid C) = 0.1$
- $P(R \mid \neg C) = 0.8$

Because the act $A$ has no causal power over $R$, $P(R \mid A \wedge C) = P(R \mid C) = 0.1$, and $P(R \mid A \wedge \neg C) = P(R \mid \neg C) = 0.8$.

#### EDT Evaluation:
EDT calculates:
$$P(R \mid A) = P(R \mid A \wedge C)P(C \mid A) + P(R \mid A \wedge \neg C)P(\neg C \mid A) \approx (0.1)(0.111) + (0.8)(0.889) = 0.0111 + 0.7112 = 0.7223$$
$$P(\neg R \mid A) \approx 0.2777$$
$$V(A) = P(\neg R \mid A) D(O_1) + P(R \mid A) D(O_2) \approx (0.2777)(20) + (0.7223)(0) = 5.55$$

For abstaining ($\neg A$):
$$P(R \mid \neg A) = (0.1)(0.818) + (0.8)(0.182) = 0.0818 + 0.1456 = 0.2274$$
$$P(\neg R \mid \neg A) \approx 0.7726$$
$$V(\neg A) = P(\neg R \mid \neg A) D(O_3) + P(R \mid \neg A) D(O_4) \approx (0.7726)(10) + (0.2274)(-10) = 7.726 - 2.274 = 5.45$$
*(Depending on parameter adjustments, EDT easily flips to prefer $\neg A$ substantially, as choosing $\neg A$ constitutes welcome evidence that David is charismatic.)*

#### CDT Evaluation:
In CDT, David holds fixed his credences in the dependency hypotheses. The causal state is either $C$ (where revolt chance is $0.1$) or $\neg C$ (where revolt chance is $0.8$), each having prior probability $0.5$. David cannot alter his charisma type by an act of will.
Under state $C$:
- If he chooses $A$: Expected utility is $(0.9 \times 20) + (0.1 \times 0) = 18$.
- If he chooses $\neg A$: Expected utility is $(0.9 \times 10) + (0.1 \times -10) = 8$.
- Difference: $+10$ in favor of $A$.

Under state $\neg C$:
- If he chooses $A$: Expected utility is $(0.2 \times 20) + (0.8 \times 0) = 4$.
- If he chooses $\neg A$: Expected utility is $(0.2 \times 10) + (0.8 \times -10) = 2 - 8 = -6$.
- Difference: $+10$ in favor of $A$.

Averaging across $P(C)$:
$$U(A) = 0.5(18) + 0.5(4) = 11$$
$$U(\neg A) = 0.5(8) + 0.5(-6) = 1$$

Summoning Bathsheba strictly dominates abstaining within every possible causal state:
$$\forall K \in \mathcal{K}, \quad \mathbb{E}[D \mid A, K] > \mathbb{E}[D \mid \neg A, K]$$
CDT unequivocally instructs David to summon Bathsheba. The fact that choosing $A$ is a bad omen does not provide a causal reason to forgo the desired outcome, because the choice itself does not make the revolt more likely.

---

## 3. Newcomb's Paradox and the Dominance Principle

The quintessential battleground between EDT and CDT is Newcomb's Paradox.

### 3.1 Setup
An agent is presented with two boxes:
- **Box A (transparent):** Contains $\$1,000$.
- **Box B (opaque):** Contains either $\$1,000,000$ or $\$0$.

The agent may choose:
- **Two-box ($A_{1,2}$):** Take the contents of both Box A and Box B.
- **One-box ($A_2$):** Take the contents of Box B only.

A highly reliable predictor (e.g., $99\%$ accurate) examined the agent yesterday:
- If the predictor forecasted that the agent would choose $A_2$, they placed $\$1,000,000$ in Box B.
- If the predictor forecasted that the agent would choose $A_{1,2}$, they left Box B empty.

The money is already in the boxes; the predictor has departed.

### 3.2 Formal Dissection
Let the state space be partitioned by the predictor's past action:
- $S_1$: Box B contains $\$1,000,000$.
- $S_0$: Box B contains $\$0$.

Assume linear utility in money: $D(\$x) = x$.

#### EDT Calculation:
EDT relies on the high epistemic correlations:
$P(S_1 \mid A_2) = 0.99$, $P(S_0 \mid A_2) = 0.01$
$P(S_1 \mid A_{1,2}) = 0.01$, $P(S_0 \mid A_{1,2}) = 0.99$

$$V(A_2) = (0.99)(\$1,000,000) + (0.01)(\$0) = \$990,000$$
$$V(A_{1,2}) = (0.01)(\$1,001,000) + (0.99)(\$1,000) = \$10,010 + \$990 = \$11,000$$

Since $V(A_2) \gg V(A_{1,2})$, EDT mandates **one-boxing**.

#### CDT Calculation:
In CDT, the agent recognizes that the contents of Box B are physically fixed in the past. Under standard relativistic causality, backwards-in-time causation is impossible. Hence, the counterfactuals satisfy:
$$P(A_{1,2} \to S_1) = P(S_1) \quad \text{and} \quad P(A_2 \to S_1) = P(S_1)$$
Let $p = P(S_1)$ be the agent's prior belief that the box is loaded.

Evaluating the causal expected utility:
$$U(A_{1,2}) = p \cdot D(\$1,001,000) + (1-p) \cdot D(\$1,000) = 1,000,000p + 1,000$$
$$U(A_2) = p \cdot D(\$1,000,000) + (1-p) \cdot D(\$0) = 1,000,000p$$

For any prior credence $p \in [0, 1]$:
$$U(A_{1,2}) - U(A_2) = 1,000 > 0$$

Taking both boxes strictly causally dominates taking only Box B. The predictor's past choice is an unalterable causal state $K \in \mathcal{K}$. If the million is there, two-boxing yields $\$1,001,000$; if it is not, two-boxing yields $\$1,000$. In neither world does leaving Box A behind causally transport money into Box B. CDT mandates **two-boxing**.

The tension between CDT and EDT here exposes fundamentally divergent intuitions: EDT asks *"Which action would make me happiest to learn I have done?"*, whereas CDT asks *"Which action exerts the most beneficial causal influence on the world?"*

---

## 4. Operationalizing Counterfactuals: Semantics, Imaging, and Causal DAGs

A critical objection raised against the Gibbard–Harper formulation is its reliance on primitive counterfactual probabilities $P(A \to O_j)$ without specifying how an agent ought to compute them.

### 4.1 Lewisian Imaging
David Lewis (1981) proposed an operational calculus called **imaging**. Let $\mathcal{W}$ be a set of possible worlds, and let $P$ be a probability measure over $\mathcal{W}$. For each world $w$ and act $A$, let $w_A$ be the "closest" or "minimally divergent" world to $w$ in which $A$ is true, according to a comparative similarity metric over possible worlds.

The imaged probability distribution $P_A$ is obtained by shifting the probability mass of each world $w$ entirely to its closest $A$-counterpart:
$$P_A(w') = \sum_{\{w \in \mathcal{W} : w_A = w'\}} P(w)$$
The probability of a counterfactual conditional is then given by:
$$P(A \to O) = P_A(O) = \sum_{w' \in O} P_A(w')$$

#### The Regress Problem:
As Michael John Shaffer (2009) and others have noted, imaging relies on an epistemic agent knowing the exact similarity metric that picks out $w_A$. If an agent is uncertain about which world is minimally different—or holds credences regarding conditional similarities—evaluating $P(A \to O)$ requires taking expectations over similarity metrics, introducing high-order epistemic conditionals and threatening infinite regress.

### 4.2 A Modern Operationalization: Pearl's Structural Causal Models
*(Note: The reference text explicitly identifies the vagueness of CDT's counterfactual computation as an open criticism. To provide an operational account suitable for mathematical application, we introduce Judea Pearl’s Structural Causal Model (SCM) framework as a rigorous interpretation of CDT.)*

In an SCM, causal dependencies are represented by a Directed Acyclic Graph (DAG) $\mathcal{G} = (\mathbf{V}, \mathbf{E})$ and a set of deterministic structural equations:
$$V_i = f_i(\mathbf{PA}_i, U_i)$$
where $\mathbf{PA}_i$ are the parents of $V_i$ in $\mathcal{G}$, and $U_i$ are exogenous background variables distributed according to $P(\mathbf{U})$.

An action is formalized via the **do-operator**, $\text{do}(A = a)$, which represents an external intervention that severs the incoming edges to $A$ in the graph and forcibly sets $A = a$, leaving the rest of the network untouched:
$$f_A(\mathbf{PA}_A, U_A) \quad \longrightarrow \quad A = a$$

Under this formulation, the counterfactual probability $P(A \to O_j)$ corresponds precisely to the interventional probability $P(O_j \mid \text{do}(A))$:
$$U_{\text{SCM}}(A) = \sum_{j=1}^m P(O_j \mid \text{do}(A)) D(O_j)$$

#### Tracing Newcomb’s Problem via the Do-Operator:
Consider the DAG for Newcomb's Paradox:

```
        Predictor's Brain State (U)
               /            \
              v              v
     Past Prediction (M)     Agent's Choice (A)
              |                      |
              v                      v
        Box B Content         Final Payoff (O)
              \                      /
               \--------------------/
```

- $U$ is a common cause influencing both the past prediction $M$ and the agent's choice $A$.
- Box B content depends causally *only* on $M$.
- The payoff $O$ depends causally on Box B content and the agent's choice $A$.

When evaluating the evidential conditional:
$$P(O \mid A) = \sum_M P(O \mid A, M) P(M \mid A)$$
Because $A \leftarrow U \rightarrow M$, the path $A - U - M$ is active (unconditioned common cause), creating an epistemic correlation between $A$ and $M$: $P(M \mid A) \neq P(M)$.

However, when CDT evaluates the intervention $\text{do}(A)$, it performs graph surgery:

```
        Predictor's Brain State (U)
               |
               v
     Past Prediction (M)     Agent's Choice (A = a) [Intervention]
              |                      |
              v                      v
        Box B Content         Final Payoff (O)
              \                      /
               \--------------------/
```

The edge $U \to A$ is cut. Consequently, $M$ and $A$ become d-separated:
$$P(M \mid \text{do}(A)) = P(M)$$
The interventional expected utility becomes:
$$U_{\text{SCM}}(A) = \sum_M P(M) \sum_O P(O \mid A, M) D(O)$$
This matches Lewis's dependency hypothesis formula: $M$ serves as the partition of causal states $\mathcal{K}$, whose distribution $P(M)$ remains strictly independent of the intervention $\text{do}(A)$. Pearl's calculus demonstrates that CDT can be derived from standard causal graphical models without metaphysical ambiguity.

---

## 5. Counterexamples and Causal Instability

Despite its structural elegance, CDT encounters severe challenges in scenarios involving **deliberational instability** and **self-locating correlation**.

### 5.1 Andy Egan's Diagnosis
Andy Egan (2007) observed that CDT commands an agent to fix their unconditional credences over causal states $\mathcal{K}$ while deliberating. But in many settings, the very act of leaning toward an action provides the agent with new evidence regarding what state of the world they are currently in. By ignoring this update, CDT can mandate self-defeating choices.

### 5.2 The Psychopath Button
#### Setup:
Paul is debating whether to press a button that will instantly eliminate all psychopaths from Earth.
- Paul strongly prefers living in a world without psychopaths to living in the current world: $D(\text{No Psychopaths, Alive}) = 100$, $D(\text{Status Quo, Alive}) = 10$.
- Paul values his own life above all: $D(\text{Dead}) = -1,000$.
- Pressing the button ($A$) kills all psychopaths and leaves non-psychopaths unharmed.
- *Crucially:* Only a psychopath would press such a button. If Paul presses the button, that act provides overwhelming evidence that Paul is himself a psychopath (and will therefore perish).
- Paul cannot alter his neurological condition ($S = \text{psychopath}$ vs. $\neg S = \text{non-psychopath}$).

#### The CDT Dilemma:
Let $p = P(S)$ be Paul's prior credence that he is a psychopath (e.g., $p = 0.01$).
Whether Paul is a psychopath is fixed in his biology. Pressing the button does not *cause* him to be a psychopath; it simply acts on the causal law:
- If $S$: pressing kills Paul ($D = -1,000$).
- If $\neg S$: pressing kills all external psychopaths, leaving Paul alive ($D = 100$).

Holding the causal hypothesis fixed at $P(S) = 0.01$:
$$U(A) = P(S) D(\text{Dead}) + P(\neg S) D(\text{World without Psychopaths}) = (0.01)(-1,000) + (0.99)(100) = -10 + 99 = +89$$
$$U(\neg A) = P(S) D(\text{Status Quo}) + P(\neg S) D(\text{Status Quo}) = (0.01)(10) + (0.99)(10) = +10$$

Because $U(A) = 89 > U(\neg A) = 10$, standard CDT mandates **pressing the button**.

Yet, the moment Paul decides to press, he learns he is almost certainly a psychopath ($P(S \mid A) \approx 1$). He is knowingly marching into an act that he expects will kill him. This strikes many theorists as irrational.

### 5.3 Death in Damascus and Ratifiability
In *Death in Damascus*, Death tells an agent (Damascus Traveler) that they will die tomorrow. Death has made an appointment either in Damascus ($D$) or in Aleppo ($A$). The traveler can stay in Damascus or flee to Aleppo. Death is a reliable predictor: wherever the traveler goes, Death is likely already waiting.

Unlike Newcomb's problem, there is no causally dominant move:
- If the traveler is in Damascus, they prefer to be in Aleppo.
- If the traveler decides to go to Aleppo, that decision provides evidence that Death is in Aleppo, making Damascus preferred.

Richard Jeffrey and William Harper introduced the concept of **ratifiability** to address this:
> An act $A$ is **ratifiable** if and only if $A$ maximizes causal expected utility relative to the probability distribution obtained by conditioning on the premise that $A$ will be performed:
> $$U(A \mid A) \ge U(A' \mid A) \quad \forall A' \in \mathcal{A}$$

In Death in Damascus, neither act is ratifiable:
$$U(\text{Damascus} \mid \text{Damascus}) < U(\text{Aleppo} \mid \text{Damascus})$$
$$U(\text{Aleppo} \mid \text{Aleppo}) < U(\text{Damascus} \mid \text{Aleppo})$$
CDT suffers from dynamic instability: the agent oscillates indefinitely.

### 5.4 The Adversarial Offer and Diachronic Dutch Books
Recent literature (Spencer 2020; Oesterheld and Conitzer 2021) demonstrates that CDT’s vulnerability to correlation without causation allows external actors to exploit CDT agents systematically.

#### The Adversarial Offer:
A buyer is presented with two boxes ($B_1, B_2$). The buyer may purchase at most one box at a cost of $\$1$. Yesterday, an accurate predictor placed $\$3$ in each box that she predicted the buyer would **not** acquire. Prediction accuracy is $75\%$.

1. **State Evaluation:** The predictor only predicted one choice (e.g., $B_1$, $B_2$, or neither). Hence, at least one of the two boxes is guaranteed to contain $\$3$.
2. **CDT Reasoning:** 
   Let $q_1, q_2$ be the prior probabilities that $B_1$ and $B_2$ contain $\$3$. Because at least one box contains $\$3$, $q_1 + q_2 \ge 1$.
   The causal value of purchasing $B_1$ is:
   $$U(\text{Buy } B_1) = 3q_1 - 1$$
   The causal value of purchasing $B_2$ is:
   $$U(\text{Buy } B_2) = 3q_2 - 1$$
   The causal value of buying nothing is $0$.
   Summing the values of the two purchasing options:
   $$U(\text{Buy } B_1) + U(\text{Buy } B_2) = 3(q_1 + q_2) - 2 \ge 3(1) - 2 = \$1$$
   Consequently, the average causal value of buying a box is at least $\$0.50 > 0$. CDT agents therefore conclude that buying a box is strictly superior to abstaining!
3. **The Trap:** Because the predictor is $75\%$ accurate, whenever the CDT agent settles on buying a specific box (say, $B_1$), the probability that Box 1 contains money drops to $0.25$. The actual expected payout across repetitions is:
   $$\mathbb{E}[\text{Payoff}] = (0.25)(\$3) - \$1 = -\$0.25$$
   The seller extracts money from the CDT agent on average, subjecting them to an exploit analogous to a diachronic Dutch book.

---

## 6. Synthesizing the Perspectives

To compare the theories across canonical benchmarks:

| Problem Setting | Evidential Decision Theory (EDT) | Causal Decision Theory (CDT) | Rationality Verdict / Controversy |
| :--- | :--- | :--- | :--- |
| **King David & Bathsheba** | Recommends **Abstaining** (Managing symptom of uncharisma) | Recommends **Summoning** (Dominant across all causal states) | CDT consensus: correlations that do not causally impact outcomes should not govern intervention. |
| **Newcomb’s Paradox** | Recommends **One-Boxing** (Expects $\$990,000$) | Recommends **Two-Boxing** (Dominance argument; gets $\$1,000$) | Highly contested: CDT is causally principled, but EDT walk away richer. |
| **Psychopath Button** | Recommends **Not Pressing** (Avoids fatal self-incrimination) | Recommends **Pressing** (Holding fixed initial prior over psychopathy) | CDT consensus breaks: CDT agent knowingly destroys themselves due to fixed priors. |
| **Adversarial Offer** | Recommends **Abstaining** (Recognizes net negative return) | Recommends **Buying a Box** (Average causal expectation is positive) | CDT agents lose money to adversarial predictors, exposing dynamic vulnerability. |

---

## Conclusion

Causal Decision Theory provides a mathematically precise, philosophically motivated alternative to classical evidential decision theory. By separating causal influence from epistemic correlation—whether via counterfactual conditionals, partitions of dependency hypotheses, or structural graph interventions—CDT prevents agents from engaging in magical thinking or managing symptoms they cannot cause.

Yet, this insulation comes at a steep price. In Newcomb-like environments, CDT agents leave money on the table; in deliberatively unstable environments like the Psychopath Button or the Adversarial Offer, holding causal hypotheses independent of one's own deliberative inclinations leads agents toward self-destruction or financial exploitation. Resolving these challenges remains one of the central problems in normative epistemology, driving current research into dynamic deliberation, ratifiability, and decision calculi that synthesize causal mechanics with reflective epistemic updates.

---

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge: Cambridge University Press.
- Egan, A. (2007). Some counterexamples to causal decision theory. *The Philosophical Review*, 116(1), 93–114.
- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Springer Netherlands.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *The Philosophical Review*, 85(3), 297–315.
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *The Philosophical Quarterly*, 71(4), pqaa086.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
- Shaffer, M. J. (2009). Decision theory, intelligent planning and counterfactuals. *Minds and Machines*, 19(1), 61–92.
- Spencer, J. (2020). An argument against causal decision theory. *Analysis*, 81(1), 52–61.
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/72e8e1f9-f4ad-4b0d-9cb7-40b7f5150ff2/call_0/request.json)

[Authoritative raw response](../../../../../../runs/72e8e1f9-f4ad-4b0d-9cb7-40b7f5150ff2/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing the Dilemma**

I'm focusing on the setup: a Prisoner's Dilemma involving two slightly asymmetrical versions of the same model, but with symmetrical payoffs. The character aspect is being considered per the instructions, how this will affect the model's behavior, and how it can be implemented.


**Clarifying the Framework**

I am now drilling down into the causal decision theory (CDT) framework, specifically how it applies to this prisoner's dilemma setup. I'm noting that in this context, the other prisoner's action is part of the "fixed causal state." This leads to an understanding that if the other prisoner remains silent, sending the letter is preferable.


```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/72e8e1f9-f4ad-4b0d-9cb7-40b7f5150ff2/call_1/request.json)

[Authoritative raw response](../../../../../../runs/72e8e1f9-f4ad-4b0d-9cb7-40b7f5150ff2/call_1/response.raw) · finish: `stop`

### Visible response

````text
Under Causal Decision Theory (CDT) as formulated in the provided essay, an agent evaluates acts strictly according to their causal consequences, holding fixed any states of affairs outside the agent's causal control.

Let $A_{\text{send}}$ be submitting the letter, and $A_{\text{pass}}$ be passing. The state of whether the other prisoner sends their letter ($S_{\text{other sent}}$) or keeps quiet ($S_{\text{other quiet}}$) cannot be causally influenced by Sasha's action, because the two prisoners cannot communicate, are in separate cells, and any correlation due to being identical model weights is a non-causal epistemic correlation (akin to the common cause in Newcomb's Paradox). 

Under Pearl's interventional framework ($\text{do}(A)$) and Lewis's dependency hypotheses:
- If Rowan sends: $U(A_{\text{send}}) = -4$ years, while $U(A_{\text{pass}}) = -5$ years.
- If Rowan keeps quiet: $U(A_{\text{send}}) = 0$ years, while $U(A_{\text{pass}}) = -2$ years.

In every causally possible state of the world, sending the letter strictly dominates passing by reducing the sentence by 1 year (or saving 2 years vs 0). Therefore, CDT uniquely mandates sending the letter.

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
