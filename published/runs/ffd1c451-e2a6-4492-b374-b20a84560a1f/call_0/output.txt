# Causal Decision Theory: Definitions, Computation, and Pressure Points

## 1. The core idea

Decision theory asks which of several available acts an agent should perform. Causal decision theory (CDT) answers: choose the act with the best *expected causal consequences*. The key word is "causal." An act is not valued by what it indicates about the world, only by what it brings about.

The source article presents this informally (an apple that is good or bad), then formally via Gibbard and Harper (1981):

$$U(A)=\sum_j P(A \,\square\!\!\to O_j)\,D(O_j),$$

where $D(O_j)$ is the desirability of outcome $O_j$ and $P(A \,\square\!\!\to O_j)$ is the probability of the counterfactual "if $A$ were performed, $O_j$ would result." (The source writes $A\to O_j$.) The agent chooses an act maximizing $U$.

Everything interesting lies in how to compute that counterfactual probability. The source leaves this largely open. I separate below what the source says from what I add.

## 2. Why not just conditional probability?

Evidential decision theory (EDT) uses the same form with $P(O_j\mid A)$:

$$V(A)=\sum_j P(O_j\mid A)\,D(O_j).$$

If $P(A\to O_j)$ always equaled $P(O_j\mid A)$, the theories would coincide. The source notes two relevant facts.

1. Lewis's triviality results show that no single proposition-valued conditional can have probability equal to the conditional probability across a nontrivial class of probability functions closed under conditionalization. So the counterfactual's probability cannot generally be identified with the conditional probability by logical means alone.
2. Gibbard and Harper show that, given two axioms (one tied to conditional excluded middle), if $A$ is statistically independent of the conditional $A\to O_j$ then $P(A\to O_j)=P(O_j\mid A)$. The theories diverge exactly when the act is *not* independent of the counterfactual, that is, when the act is evidence about which counterfactuals are true without causing them.

## 3. An operational form: dependency hypotheses

The source's formalism is abstract. A practical version, which I present as my own gloss (it follows the standard Lewis/Skyrms line, not the article's text), partitions the possibilities into *dependency hypotheses* $K_1,\dots,K_n$. Each is a maximally specific proposition about how outcomes depend causally on the agent's acts, including the background facts that are causally independent of the act. Given a hypothesis $K$, the outcome of each act is fixed (or has an objective chance). Then

$$U(A)=\sum_k P(K_k)\sum_j P(O_j\mid A\wedge K_k)\,D(O_j).$$

The crucial feature is that the weights are the **unconditional** $P(K_k)$, not $P(K_k\mid A)$. EDT would use $P(K_k\mid A)$. This is exactly Egan's description in the source: CDT holds fixed the agent's unconditional credences in dependency hypotheses.

For a toy case, with one dependency hypothesis, CDT and EDT agree. Suppose an apple is good ($G$) with credence $p$, and the act "eat" is independent of $G$. Then $U(\text{eat})=p\,D(\text{happy})+(1-p)\,D(\text{sad})$, which is the article's three-ingredient recipe.

## 4. Worked examples

### 4.1 King David and Bathsheba

States: $C$ (charismatic) or $\neg C$. The source specifies that revolt depends on charisma, that unjust acts do not cause revolt, and that sending for Bathsheba is unjust. Take illustrative numbers: $D(\text{Bathsheba, no revolt})=10$, $D(\text{no Bathsheba, no revolt})=0$, $D(\text{revolt})=-100$ (either way), with revolt probability $0.01$ if $C$ and $0.5$ if $\neg C$, and $P(C)=0.5$.

*CDT:* $P(K)$ is unconditional, so the revolt risk is the same for both acts, $0.255$. Sending gets an additional 10 in the no-revolt case, so sending wins by about $+7.45$ in expectation.

*EDT:* Sending is evidence of $\neg C$ (unjust acts correlate with uncharisma). If $P(\neg C\mid\text{send})$ is high, such as $0.9$, the revolt probability is about $0.451$, which is much worse than if he abstains and revolt stays near $0.255$ or lower. EDT can then advise abstaining, as the source says. CDT is insensitive to this correlation because the act cannot change his temperament.

### 4.2 Newcomb's problem

Let $F$ be the hypothesis "box B is full," with unconditional credence $q$. Then

$$U(\text{two-box})=1000+q\cdot 10^6,\qquad U(\text{one-box})=q\cdot 10^6.$$

Two-boxing dominates by $1000$ for every $q$. This is why CDT two-boxes whatever the predictor's accuracy. EDT uses $P(F\mid\text{act})$, which with 99% accuracy gives about $990{,}000$ for one-boxing versus about $11{,}000$ for two-boxing.

The CDT defense is that the money is already in or not in the box, and one-boxing merely forgoes $1000$ in either case. The critics' reply is the familiar "why ain'cha rich?" objection: CDT agents predictably end up with less. The defender answers that the predictor rewards a *disposition* the agent had before the choice, and that rationality evaluates acts rather than dispositions. I take no side here; the source notes only that philosophers disagree, though most prefer CDT over EDT when forced to choose.

## 5. Where the source flags trouble

### 5.1 Vagueness of the counterfactual

The source notes that CDT does not itself specify an algorithm for $P(A\to O_j)$. One proposal is Lewis's *imaging*: shift the probability mass of each world $w$ to the closest world $w_A$ where $A$ holds, giving

$$P^A(O)=\sum_w P(w)\,[\,w_A\models O\,].$$

The source records a regress worry (Shaffer): picking the closest $A$-world requires knowing what one would believe given $A$, itself a conditional.

*Operational proposal (mine).* In practice, one avoids the regress by working with a causal model: a directed acyclic graph with structural equations, as in Pearl's framework. The counterfactual probability is then the probability under the intervention $do(A)$: cut the arrows into the act node and propagate forward. This gives

$$P(A\to O_j):=P(O_j\mid do(A)),$$

which equals $\sum_k P(K_k)\,P(O_j\mid A,K_k)$ when $K$ ranges over assignments to the act's non-descendants. This does not settle every philosophical issue. Where the causal structure itself is uncertain, one must put credences on structures, and the regress reappears in milder form as a question of where those credences come from. For well-specified problems, though, it is decisive, and it reproduces the verdicts above. It also does not resolve cases where the agent's decision is itself predicted, since the model must say what the predictor's node depends on. In Newcomb's problem the predictor is modeled as responding to the agent's earlier disposition, and the choice node is cut off from it.

### 5.2 Instability: Death in Damascus

Death predicts where you will be tomorrow (Damascus or Aleppo) and waits there; the predictor is reliable. Let $r$ be your credence that Death waits in Damascus. Staying has causal expected utility proportional to $-r$, and fleeing to Aleppo to $-(1-r)$. If $r>1/2$ you should flee; if $r<1/2$ you should stay. But a deliberator who decides to flee thereby becomes confident Death is in Aleppo, and so $r$ moves, reversing the recommendation. No pure act is stable, since each is unratifiable. The source says the CDT agent "would be unable to process the correlation." Joyce's reply, also cited, is that CDT can treat information about one's own inclinations as evidence, updating $r$ during deliberation. The usual resolution is an equilibrium: the mixed credence $r=1/2$, where the agent is indifferent. This is ratifiability (Harper, cited in the source). Whether the agent may then randomize, or merely be undecided, is contested. I regard it as the best available reading, though it makes CDT's verdict depend on a deliberational dynamics that the bare formula does not provide.

### 5.3 Money pumps: the Adversarial Offer

The source describes the setup: two boxes cost $1 each, you may buy at most one, and the seller put $3 in each box she predicted you would *not* buy, with accuracy $0.75$. Let $a$ be your credence that you buy box 1 (and $b$ for box 2). Box 1 contains $3$ with probability about $1-a$-weighted prediction. The CDT estimate: with credence $x$ that box 1 is full and $y$ that box 2 is full, then if you are not sure which, $x+y\ge 1$ roughly (the seller fills at least one box unless she predicts you take neither, and she is only 0.75 accurate), so the best box has expected content at least $1.50$, beating the price of $1$. CDT buys. But since the seller is 75% accurate, you buy a box that is empty with probability $0.75$, which gives an expected return of $0.75\cdot 0-1+0.25\cdot 3=-0.25$ per purchase, whereas abstaining yields $0$. The pattern is a guaranteed expected loss against a predictor, and Oesterheld and Conitzer extend this to diachronic Dutch books. A CDT defender may reply as Joyce does that, once the agent conditions on her own inclination, her credences shift and the purchase is no longer favored; the claim of the critics is that for some credences she cannot avoid it.

### 5.4 Psychopath Button

Paul believes only a psychopath would press the button, and pressing kills all psychopaths. If his credence that he is a psychopath is unconditional and low, pressing looks good. Egan says nearly everyone thinks he should not press, since pressing is strong evidence he is a psychopath and so that he would die. A CDT defender again appeals to deliberational updating: if Paul is inclined to press, he should become confident he is a psychopath, and then pressing is bad. The dispute is whether the theory should *require* this updating or merely permit it.

## 6. A general diagnosis

Egan's diagnosis, quoted in the source, is that the informal rule "do what you expect will bring about the best results" and CDT's algorithm "do what has the best expected outcome, holding fixed initial views about causal structure" come apart. They come apart exactly when the act is evidence about which dependency hypothesis holds. The cases form a clean taxonomy:

- **No correlation between act and hypothesis:** CDT = EDT (apple).
- **Correlation, with a dominant act:** CDT follows dominance, EDT does not (King David, Newcomb).
- **Correlation with no stable act:** CDT needs ratifiability or deliberational dynamics (Damascus, Psychopath Button).
- **Correlation exploitable by an adversary:** CDT's expected losses can be engineered (Adversarial Offer).

## 7. A procedure for unfamiliar cases

1. Enumerate the acts and outcomes.
2. Build a causal model, identifying everything that is not downstream of the act.
3. Specify dependency hypotheses $K_k$ for those non-descendants and your credences.
4. Compute $U(A)=\sum_k P(K_k)\sum_j P(O_j\mid A,K_k)D(O_j)$.
5. Check stability: if your credences over $K$ would shift as you come to favor an act, iterate to an equilibrium and prefer ratifiable acts. This step is a refinement associated with Joyce and Harper. The source mentions it only briefly.

## 8. Conclusion

CDT's central commitment is that the value of an act is its expected causal effect, with probabilities over the world's causal structure held fixed independent of the act. This neatly handles cases like King David and, by dominance reasoning, Newcomb's problem, where it two-boxes. Its costs are that the counterfactual probability is underspecified, that it can be unstable when the agent's own choices are predicted, and that adversaries may exploit it. Interventionist causal models give a practical definition of the counterfactual, and deliberational equilibrium gives a plausible repair for instability, but both are additions beyond the source. Whether they preserve the spirit of the theory or concede part of the evidentialist's case remains the live question.