# Causal Decision Theory: What It Computes, Where It Diverges from EDT, and Where It Strains

## 1. The guiding idea

Causal decision theory (CDT) answers a deliberating agent's question, "what should I do?", with a simple slogan: **choose the action whose causal consequences are best in expectation.** The reference article states it this way. It contrasts CDT with evidential decision theory (EDT), which recommends the action that would be the best *news* to receive about oneself.

When actions are causally relevant to outcomes and nothing else links the two, the slogan is uncontroversial. The source's opening example is eating an apple. If a good apple makes you happy and a bad one makes you sad, and you are unsure which you have, the expected value of eating depends on three things:

1. your credence that the apple is good,
2. how good the good case is, and
3. how bad the bad case is.

Nothing about your choice tells you anything about the apple except through its effects, so every reasonable theory agrees here.

The theory becomes interesting when choices are *correlated* with states of the world that they do not *cause*. These correlations arise through common causes, predictors, twins, or features of your own character. In such cases CDT insists that the correlation is irrelevant to choice. That insistence is both its central motivation and the source of its best-known difficulties.

This essay sets out the formal theory, shows how it differs from EDT, works through the standard cases numerically, and then addresses an issue the source leaves open: how to compute the counterfactual probabilities CDT needs, and what to do when the computation is unstable. I flag clearly where I go beyond the source.

## 2. Formal definitions

### 2.1 The Gibbard–Harper formula (source)

Following Gibbard and Harper (1981), the source defines the causal expected utility of an action $A$ as

$$
U(A) = \sum_j P(A \,\square\!\!\to O_j)\, D(O_j),
$$

where:

- $O_j$ ranges over a partition of outcomes,
- $D(O_j)$ is the desirability of $O_j$, and
- $P(A \,\square\!\!\to O_j)$ is the agent's credence in the counterfactual "if I were to do $A$, $O_j$ would obtain."

The rule is: choose an $A$ maximizing $U$.

EDT replaces the probability of the counterfactual with a conditional probability:

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

### 2.2 The dependency-hypothesis formulation (my reconstruction, following Lewis 1981)

For working cases, a more transparent form is useful. Let $\mathcal{K} = \{K_1, \dots, K_n\}$ be a partition of **dependency hypotheses**: maximally specific propositions about how outcomes depend causally on actions. Each $K$ says, for every available act, what that act would bring about (or with what objective chances). Crucially, which $K$ is true is **not under the agent's causal control**.

If each $A \wedge K$ determines an outcome with desirability $D(A,K)$, then

$$
U(A) = \sum_{K} P(K)\, D(A, K), \qquad V(A) = \sum_K P(K \mid A)\, D(A,K).
$$

This puts the entire difference between the theories in one place:

> **CDT weights states by unconditional credence $P(K)$; EDT weights them by credence conditional on the act, $P(K\mid A)$.**

When the act is probabilistically independent of the dependency hypotheses, the two coincide. When the act is *evidence* about $K$ without *causing* $K$, they come apart. This is the formal content of Egan's diagnosis, quoted in the source: CDT "hold[s] fixed the agent's unconditional credences in dependency hypotheses."

An immediate consequence is a **causal dominance principle**. If $D(A,K) \ge D(B,K)$ for every $K$, then $U(A) \ge U(B)$, however the acts and states are correlated. EDT does not satisfy this.

### 2.3 Why counterfactual probability is not conditional probability (source)

If $P(A \,\square\!\!\to O) = P(O\mid A)$ held generally, CDT would collapse into EDT. The source notes that Lewis (1976) showed this cannot hold in general. In fact, no conditional connective's probability can equal the conditional probability across a class of probability functions closed under conditionalization, unless those functions are trivial.

Gibbard and Harper also identified when the identity does hold. Assume two axioms:

- **(i) Conditional excluded middle:** $(A\,\square\!\!\to O) \vee (A\,\square\!\!\to \neg O)$.
- **(ii) Centering:** $A \wedge (A \,\square\!\!\to O)$ is equivalent to $A \wedge O$.

Given these, independence of $A$ from $A\,\square\!\!\to O$ suffices for equality:

$$
P(A\,\square\!\!\to O) = P(A\,\square\!\!\to O \mid A) = \frac{P(A \wedge (A\,\square\!\!\to O))}{P(A)} = \frac{P(A\wedge O)}{P(A)} = P(O\mid A).
$$

The first step uses independence and the third uses centering. The source notes that the first axiom (conditional excluded middle) is controversial.

The upshot: **CDT and EDT disagree exactly when your act is evidence about which counterfactuals are true.**

## 3. Worked cases

I attach illustrative numbers to the source's examples. The numbers are mine; the verdicts they reproduce are the source's.

### 3.1 King David and Bathsheba (source example, my numbers)

Gibbard and Harper's case runs as follows:

- Kings are either charismatic ($C$) or not ($\neg C$), and this is fixed by genes and upbringing.
- Charismatic kings tend to act justly and suffer few successful revolts.
- Uncharismatic kings act unjustly and suffer many, but because of their "sneaky, ignoble bearing," *not* because of their unjust acts.
- Sending for Bathsheba ($S$) is unjust.

Let the desirabilities and probabilities be:

- $D$: Bathsheba is worth $+1$; a revolt is worth $-10$.
- $P(\text{revolt}\mid C) = 0.1$ and $P(\text{revolt}\mid \neg C) = 0.8$, whatever David does.
- $P(C) = 0.5$, but $P(C\mid S) = 0.2$ and $P(C \mid \neg S) = 0.8$.

**EDT:**

$$
V(S) = 1 - 10\,[0.2(0.1) + 0.8(0.8)] = 1 - 6.6 = -5.6,
$$

$$
V(\neg S) = -10\,[0.8(0.1) + 0.2(0.8)] = -2.4.
$$

EDT says abstain.

**CDT:**

$$
U(S) = 1 - 10\,[0.5(0.1) + 0.5(0.8)] = -3.5, \qquad U(\neg S) = -4.5.
$$

CDT says send.

The CDT verdict follows from dominance. Within each dependency hypothesis, sending is better by exactly 1. Abstaining would merely give David the comforting *news* that he is probably charismatic; it would not make him so. The source reports that philosophers generally prefer CDT when forced to choose, and cases like this are a main reason. EDT's recommendation looks like "managing the news" rather than managing the world.

### 3.2 Newcomb's problem (source)

A predictor that is 99% reliable has filled opaque box B with \$1,000,000 if it predicted you would take only B, and left it empty otherwise. Transparent box A holds \$1,000. Take as dependency hypotheses $K_{\text{full}}$ and $K_{\text{empty}}$. The contents are already fixed and are causally independent of your choice.

**CDT:**

$$
U(\text{two}) = P(K_\text{full})(1{,}001{,}000) + P(K_\text{empty})(1{,}000) = U(\text{one}) + 1{,}000.
$$

Two-boxing wins by exactly \$1,000 for *every* credence $P(K_\text{full})$.

**EDT:**

$$
V(\text{one}) = 0.99 \times 10^6 = 990{,}000,
$$

$$
V(\text{two}) = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
$$

EDT one-boxes.

This is the source's "early alleged counterexample." Two-boxers predictably walk away with about \$1,000 while one-boxers walk away with about \$1,000,000. The CDT reply is the "why ain'cha rich?" rejoinder in reverse: the predictor rewards a disposition, and given whatever is in the box, taking both is better. The source reports that philosophers remain divided.

The **twin prisoner's dilemma** (Lewis 1979, cited in the source) has the same structure. Your twin's choice is correlated with yours but not caused by it, so CDT defects by dominance and EDT cooperates.

### 3.3 A point about policies (my addition)

The task asks how CDT evaluates *policies*. Standard CDT evaluates acts at the moment of choice. It can still evaluate the adoption of a policy *as an act*, and when the adoption is causally upstream of a predictor's prediction, CDT's verdict changes.

Suppose that before the prediction is made you can bind yourself to one-box, for instance by signing an enforceable contract. Then binding causally affects $K$, and CDT recommends binding. CDT therefore wants to precommit and then regrets being unable to once the prediction is fixed. This dynamic inconsistency is the background to the "binding" literature cited in the source (Meacham 2010) and to the Dutch-book criticisms below.

Operationally, for any decision problem we must ask *at which time* the act is evaluated. CDT's verdict is relative to the causal position of the choice node.

### 3.4 Death in Damascus: instability (source)

Death reliably predicts where you will be tomorrow and waits there. You can stay in Damascus or flee to Aleppo. Let $q$ be your credence that Death is heading to Aleppo, with survival worth 1 and death worth 0. Then

$$
U(\text{Damascus}) = q, \qquad U(\text{Aleppo}) = 1 - q.
$$

So far this is unproblematic. The trouble is that $q$ is not exogenous to deliberation. Death predicts *you*, so your credence about Death's location should track your credence about your own choice:

- As you lean toward Aleppo, $q$ rises toward 1, and Damascus becomes the CDT-better option.
- As you lean toward Damascus, $q$ falls, and Aleppo becomes better.

Whichever act you come to believe you will perform, CDT recommends the other. The source puts this as the claim that a naive CDT agent "would be unable to process the correlation."

### 3.5 The Adversarial Offer: CDT loses money (source)

Oesterheld and Conitzer's case runs as follows:

- Two boxes each cost \$1, and the buyer may buy one or none.
- The seller placed \$3 in each box she predicted the buyer would *not* buy.
- Her predictions are 75% accurate.

Let $x_i$ be the buyer's credence that box $i$ contains \$3. Then $U(\text{buy } i) = 3x_i - 1$ and $U(\text{none}) = 0$. The seller predicts at most one purchase, so at least one box is filled, and therefore $x_1 + x_2 \ge 1$. Hence

$$
\max_i U(\text{buy } i) \ge 3\cdot\tfrac12 - 1 = 0.5 > 0.
$$

CDT therefore always buys a box. Evidentially, though, given that you buy box $i$, the seller probably predicted it, so

$$
P(\text{box } i \text{ filled} \mid \text{buy } i) = 0.25,
$$

and the expected net return is $0.75 - 1 = -\$0.25$. The seller profits on average from CDT buyers.

Notice that this argument is robust to *whatever* credences the CDT agent ends deliberation with, including the equilibrium credences discussed below. That robustness is what makes the case harder to dismiss than Death in Damascus.

### 3.6 The Psychopath Button (source, my numbers)

Paul can press a button that kills all psychopaths. He thinks a psychopath-free world would be much better, but he is confident that only a psychopath would press it, and he strongly prefers living with psychopaths to dying. Let $\Psi$ be "Paul is a psychopath," and set:

- $D(\text{press}, \neg\Psi) = +10$
- $D(\text{press}, \Psi) = -100$
- $D(\text{don't}) = 0$
- $P(\Psi) = 0.05$ and $P(\Psi\mid\text{press}) = 0.9$

Naive CDT, using his current credence, computes

$$
U(\text{press}) = 0.95(10) + 0.05(-100) = 4.5 > 0,
$$

and so presses. Egan reports that "pretty much everyone" judges this wrong. The verdict seems to ignore something Paul knows: if he finds himself pressing, he is very probably a psychopath and will die.

## 4. The open questions, and an operational interpretation

The source identifies two gaps:

1. **Vagueness:** CDT does not say how to compute $P(A\,\square\!\!\to O)$.
2. **Counterexamples:** Egan attributes the counterexamples to holding unconditional credences fixed.

It also reports Joyce's reply, that CDT can use "information about what one is inclined or likely to do as evidence." Here is how I would fill these gaps. I want to be explicit that this section combines established proposals from the wider literature with my own synthesis.

### 4.1 Computing counterfactual probabilities

**Imaging (source).** Lewis's proposal is to evaluate $P(A\,\square\!\!\to O)$ by moving the probability mass of each world $w$ to the closest $A$-world $w_A$, then summing the mass that lands on $O$-worlds:

$$
P(A\,\square\!\!\to O) = P_A(O) = \sum_w P(w)\,\mathbf{1}[O \text{ holds at } w_A].
$$

Conditionalization *redistributes* mass proportionally among the $A$-worlds already present. Imaging instead *shifts* each world to its nearest $A$-variant, so a world's non-$A$-dependent features travel with it. The source, following Shaffer, notes a regress worry: we must know the similarity ordering, which is itself something we may be uncertain about.

**Structural interventions (my proposal, drawing on Pearl's causal models, which the source does not discuss).** A tractable and widely used operationalization is to represent the problem as a structural causal model:

- endogenous variables $V$,
- exogenous variables $U$ with prior $P(U)$,
- structural equations $V_i = f_i(\mathrm{pa}_i, U_i)$,
- and the act as a variable $\mathcal{A}$.

Define

$$
P(A\,\square\!\!\to O) := P(O \mid \mathrm{do}(\mathcal{A}=A)),
$$

which is computed by deleting the equation for $\mathcal{A}$, setting it to $A$, and propagating through the equations, while keeping $P(U)$ and every non-descendant of $\mathcal{A}$ at its prior distribution.

This recovers Lewis's dependency-hypothesis form. Take $K$ to be the joint setting of all variables that are not causal descendants of the act, which is everything that is "fixed" as far as the act is concerned. Then

$$
U(A) = \sum_K P(K)\, \mathbb{E}[D \mid \mathrm{do}(A), K].
$$

The regress worry is relocated rather than eliminated: uncertainty about the similarity ordering becomes uncertainty about the causal model. Uncertainty over *models* can be handled by averaging, though, so long as the model variable is itself not causally downstream of the act. I regard this as the most reasonable operational reading of "expected causal consequences," and it is what I would use to decide unfamiliar cases.

In each of the examples above, the model is simple:

| Case | Act causally affects | Act is merely evidence about |
|---|---|---|
| Bathsheba | Having Bathsheba | Charisma |
| Newcomb | Taking box A | Contents of box B |
| Death in Damascus | Your location | Death's location |
| Adversarial Offer | What you pay | Box contents |
| Psychopath Button | Deaths of psychopaths | Paul's psychopathy |

### 4.2 Which credences: before or after deliberation?

The formula $U(A) = \sum_K P(K) D(A,K)$ requires $P(K)$, but at *which* moment of deliberation? Several cases above, notably Death in Damascus and the Psychopath Button, turn on the fact that $P(K)$ should depend on what the agent expects to do. Two refinements are standard in the wider literature. The source gestures at them by citing Harper (1984) on ratifiability and Joyce (2012) on instability.

**Ratifiability.** Let $U_B(A) = \sum_K P(K \mid B)\, D(A,K)$ be the causal utility of $A$ computed on the supposition that one will in fact choose $B$. Act $A$ is **ratifiable** if

$$
U_A(A) \ge U_A(B) \quad \text{for all } B.
$$

That is, once you have decided on $A$, $A$ still looks best by causal lights. Apply this to the two unstable cases:

- **Death in Damascus.** Neither pure act is ratifiable.
- **Psychopath Button.** For pressing, $U_{\text{press}}(\text{press}) = 0.1(10) + 0.9(-100) = -89 < 0$. For not pressing, take $P(\Psi\mid\text{don't}) = 0.01$; then $U_{\text{don't}}(\text{press}) = 0.99(10) - 1 = 8.9 > 0$. Neither pure act is ratifiable.

**Deliberational equilibrium.** Following Skyrms and Joyce, model deliberation as a dynamic process:

1. The agent's credence $\pi$ over her own acts induces credences $P_\pi(K) = \sum_B \pi(B) P(K\mid B)$.
2. Those credences induce causal utilities.
3. The agent shifts $\pi$ toward acts with higher utility.
4. She repeats until a fixed point is reached, where every act in the support of $\pi$ has maximal utility.

At such a fixed point she is indifferent among the acts she might perform and may act on any of them, or randomize.

In the Psychopath Button, the equilibrium is reached when the induced credence $s$ in being a psychopath makes pressing worthless:

$$
10(1-s) - 100s = 0 \iff s = \tfrac{1}{11}.
$$

With $P(\Psi\mid\text{press}) = 0.9$ and $P(\Psi\mid\text{don't}) = 0.01$, solving $0.9\pi + 0.01(1-\pi) = 1/11$ gives $\pi \approx 0.091$. So at equilibrium Paul thinks he is about 9% likely to press and is indifferent between pressing and not. Joyce argues that this verdict, unlike naive pressing, is defensible: CDT, properly applied, has absorbed the evidential bearing of Paul's own inclinations on $P(K)$. That is how I read the source's report that CDT "is capable of taking into account any information about what one is inclined or likely to do as evidence."

Two cautions:

- This move does not change the Newcomb verdict. Two-boxing dominates for every $P(K)$, so it is ratifiable and the unique equilibrium.
- It does not defuse the Adversarial Offer. The argument that some box is worth at least \$0.50 holds at every credence, including equilibrium credences, so the CDT agent buys and loses \$0.25 in expectation.

This is why Oesterheld and Conitzer's and Spencer's cases are regarded as sharper challenges than Egan's. They also argue that CDT agents are vulnerable to diachronic Dutch books, which connects to the precommitment structure in §3.3.

### 4.3 A procedure for unfamiliar cases

Synthesizing the above (this is my proposal, not the source's), a CDT agent should proceed as follows:

1. **Enumerate acts**, fixing the time of choice. If adopting a policy earlier is possible, treat it as a separate act at an earlier node.
2. **Build the causal model.** Identify which variables are causal descendants of the act. All others form the dependency hypotheses $K$, including uncertainty over the model itself.
3. **Assign credences $P(K)$**, incorporating all evidence. This includes evidence about one's own likely choice when $K$ includes predictors or features of one's character correlated with choice.
4. **Compute $U(A) = \sum_K P(K)\, \mathbb{E}[D\mid \mathrm{do}(A), K]$** and check dominance first, which often settles the case.
5. **Check stability.** If the maximizing act is unratifiable, iterate the deliberational dynamics to an equilibrium and choose among (or mix over) the acts in its support.
6. **Note the residue.** If the problem has an Adversarial-Offer-like structure, CDT will knowingly accept a bet with negative expectation conditional on taking it. That outcome is a feature of the theory, not an error in applying it.

## 5. Assessment

The case for CDT rests on a principled distinction between *bringing about* good outcomes and *learning* that they obtain. Bathsheba shows the distinction at its most persuasive: abstaining in order to feel charismatic is a confusion, and CDT avoids it.

Two kinds of pressure remain:

- **Correlation with one's own choice, as in Newcomb and the twin dilemma.** Agents who follow CDT systematically end up poorer, and causal dominance explains this only to those already persuaded that dominance is the right test.
- **Self-referential predictors, as in Death in Damascus, the Psychopath Button, and the Adversarial Offer.** The theory's inputs depend on its outputs. Ratifiability and deliberational equilibrium are natural repairs, and they handle the instability cases tolerably. They leave intact the exploitability results, which hold at every credal state.

The source also leaves the formal foundation underspecified, since CDT "does not itself specify" how to compute counterfactual probabilities. The interventionist reading is in my view the best available operationalization, but it shifts the burden onto getting the causal model right.

## 6. Conclusion

Causal decision theory ranks acts by

$$
U(A) = \sum_K P(K)\,D(A,K),
$$

the expected desirability of their causal consequences, with credences over act-independent dependency hypotheses held fixed. EDT differs only in using $P(K\mid A)$. The two agree unless an act is evidence about what it cannot cause, and in exactly those cases CDT obeys causal dominance. That yields sending for Bathsheba, two-boxing in Newcomb, and defecting against one's twin.

The theory's open joints are the computation of counterfactual probabilities, for which I have argued that interventions in a causal model are the most usable answer, and the choice of credences when one's own decision is evidentially entangled with the state. Ratifiability and deliberational equilibrium, which go beyond the source, tame the instability cases but not the money-pump cases.

Anyone applying CDT should therefore do three things: build the causal model explicitly, check for dominance and stability, and accept that in predictor-rich environments the theory deliberately prefers causing to being lucky, at a cost its critics consider decisive.

### References

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116.
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*.
- Joyce, J. (2012). "Regret and instability in causal decision theory." *Synthese* 187.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Phil. Review* 85; (1981) "Causal decision theory." *AJP* 59.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Phil. Quarterly* 71.
- Pearl, J. (2009). *Causality*, 2nd ed. (not cited in the source; basis of §4.1).