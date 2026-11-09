# Causal Decision Theory: Choosing What You Can Influence

## 1. The idea in one sentence

Causal decision theory (CDT) says that a rational agent facing a set of possible actions should choose the action that **causes** the best outcome in expectation. The phrase "in expectation" matters because you rarely know what your actions will cause. The word "causes" matters even more, because it is where CDT departs from its main rival, evidential decision theory (EDT). EDT recommends the action that would be the best *news* to receive about yourself.

The reference article sets out this contrast, gives Gibbard and Harper's formula, and surveys a set of thought experiments and objections. This essay rebuilds that material as a working procedure: definitions, a recipe, worked numbers, and an account of where the theory is underspecified. I mark clearly where I go beyond the source. That happens mainly in Sections 4, 6 and 7, where I offer an operational reading of "counterfactual probability" and a treatment of unstable cases drawn from the ratifiability and deliberation literature.

## 2. Setup and the Gibbard–Harper formula

The ingredients are:

- a finite set of **acts** $\mathcal{A}$;
- a set of mutually exclusive, jointly exhaustive **outcomes** $O_1,\dots,O_n$;
- a **desirability** (utility) function $D(O_j)$;
- a credence function $P$ over propositions, including propositions about acts.

**EDT** scores an act by conditional expected utility:
$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

**CDT**, in the form Gibbard and Harper (1981) gave it and the source quotes, scores an act using probabilities of counterfactuals:
$$
U(A) = \sum_j P(A \mathbin{\square\!\!\rightarrow} O_j)\, D(O_j).
$$
Here $A \mathbin{\square\!\!\rightarrow} O_j$ is the subjunctive conditional "if $A$ were performed, $O_j$ would obtain."

The source glosses $P(A\to O_j)$ as the probability "that $A$ necessarily implies $O_j$." I read this as loose phrasing. The relevant conditional is not strict implication. It is the counterfactual that would be true if the world's causal structure, together with facts outside the agent's control, would deliver $O_j$ upon $A$. Everything below uses that reading.

The two formulas differ only in the weights. EDT asks how likely $O_j$ is *given that* I do $A$. CDT asks how likely it is that $O_j$ *would* result *if* I did $A$. The source notes that Lewis (1976) proved these cannot be identified in general: no conditional connective $\to$ satisfies $P(A\to O)=P(O\mid A)$ across a class of non-trivial probability functions closed under conditioning. If such a connective existed, CDT would collapse into EDT.

## 3. When CDT and EDT agree, and why they sometimes don't

Gibbard and Harper identify a sufficient condition for agreement. Assume:

1. **Centering:** $A \wedge (A \mathbin{\square\!\!\rightarrow} O) \equiv A \wedge O$. If $A$ actually happens, "if $A$ then $O$" holds exactly when $O$ holds.
2. **Conditional excluded middle (CEM):** for each $A$, exactly one of the counterfactuals $A \mathbin{\square\!\!\rightarrow} O_j$ is true. So these counterfactuals partition logical space, and $\sum_j P(A\mathbin{\square\!\!\rightarrow} O_j)=1$.

From centering,
$$
P(O_j \mid A) = \frac{P(A\wedge O_j)}{P(A)} = \frac{P(A \wedge (A\mathbin{\square\!\!\rightarrow} O_j))}{P(A)} = P(A\mathbin{\square\!\!\rightarrow} O_j \mid A).
$$
So if the counterfactual is **probabilistically independent of the act**, meaning $P(A\mathbin{\square\!\!\rightarrow} O_j\mid A)=P(A\mathbin{\square\!\!\rightarrow} O_j)$, then $P(O_j\mid A)=P(A\mathbin{\square\!\!\rightarrow}O_j)$ and the two theories coincide.

The interesting cases are those where independence fails. Learning that you chose $A$ can be evidence about which counterfactuals are true, because something that shapes your choice also shapes how the world would respond. The source flags CEM as controversial. It is needed mainly to make the counterfactuals form a partition. The dependency-hypothesis formulation below avoids relying on it.

## 4. An operational formulation: dependency hypotheses and interventions

The source states plainly that CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." It mentions Lewis's **imaging** proposal: to evaluate $A$, move each world $w$'s probability mass to the closest world $w_A$ where $A$ holds,
$$
P_A(w') = \sum_{w:\, w_A = w'} P(w), \qquad U(A)=\sum_{w'} P_A(w')\,D(w').
$$
The source also reports Shaffer's worry that this invites a regress. Imaging requires knowing what the closest $A$-world is. That is itself a conditional matter about which one may be uncertain.

For applications I recommend a formulation that sidesteps much of this. It is standard in the literature (Lewis 1981; Skyrms), though the source does not spell it out. Let $\{K_1,\dots,K_m\}$ be a partition into **dependency hypotheses**. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on acts, and it is outside the agent's causal influence. Then
$$
U(A) = \sum_i P(K_i) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j).
$$
The key feature is the weight: **unconditional** $P(K_i)$, not $P(K_i\mid A)$. EDT would use $P(K_i\mid A)$. That single substitution is the whole difference.

In modern causal-model language, the same idea becomes Pearl's intervention operator:
$$
U(a) = \sum_o P(o \mid \mathrm{do}(a))\, D(o).
$$
Here $\mathrm{do}(a)$ cuts the arrows *into* the action variable, sets it to $a$, and propagates effects only *downstream*. Variables that are causally upstream of, or parallel to, the act keep their prior distribution.

**My operational recipe** for unfamiliar cases:

1. **Model the act as an intervention.** Draw (at least mentally) a causal graph containing your choice, the outcomes, and every variable correlated with your choice.
2. **Sort variables.** Those causally downstream of the act can be influenced. Those upstream or merely correlated (common causes, earlier predictions, fixed traits) cannot.
3. **Hold the non-influenceable variables at their current unconditional credence.** These are your dependency hypotheses.
4. **Compute** $U(a)$ for each act and pick the maximum.
5. **Check stability** (Section 6): would learning that you had chosen the maximizer change step 3's credences enough to reverse the verdict?

Steps 1–4 are standard CDT. Step 5 is my addition, motivated by the counterexamples the source surveys.

## 5. Worked examples

### 5.1 The apple: plain expected value

This is the source's informal example. Let $g$ be your credence that the apple is good, with $D(\text{happy})=h>0$ and $D(\text{sad})=-s<0$. No hidden correlations are present, so
$$
U(\text{eat}) = g h - (1-g)s.
$$
Eat if $g > s/(h+s)$. All three factors the source lists (probability of good or bad, how happy, how sad) appear exactly once. Here CDT and EDT agree, because eating the apple is not evidence about its quality.

### 5.2 King David and Bathsheba: a common cause

The case comes from Gibbard and Harper as quoted in the source. Charisma $C$ is a fixed trait. It makes just acts more likely, and it makes successful revolt $R$ less likely. Unjust acts do not themselves cause revolt.

Illustrative numbers (mine):

- $P(C)=0.5$
- $P(R\mid C)=0.1$ and $P(R\mid\neg C)=0.8$
- $D(\text{Bathsheba})=+10$ and $D(R)=-100$
- because charismatic kings tend to act justly, $P(C\mid\text{send})=0.2$ and $P(C\mid\text{abstain})=0.8$

*EDT:*
$$
V(\text{send}) = 10 - 100\,[0.2(0.1)+0.8(0.8)] = 10-66 = -56,
$$
$$
V(\text{abstain}) = -100\,[0.8(0.1)+0.2(0.8)] = -24.
$$
EDT says abstain.

*CDT:* $C$ is upstream of the act, so hold $P(C)=0.5$. Then $P(R\mid\mathrm{do}(\cdot)) = 0.5(0.1)+0.5(0.8) = 0.45$ for *both* acts:
$$
U(\text{send}) = 10-45=-35,\qquad U(\text{abstain})=-45.
$$
CDT says send, matching the source's report. The verdict does not depend on the 0.5. Sending is better by exactly 10 under every value of $P(C)$, because it dominates within each dependency hypothesis. Abstaining would only manage the news about David's character, not change it. That is the core CDT intuition.

### 5.3 Newcomb's problem: a prediction already made

Box A holds \$1,000. Box B holds \$1,000,000 iff the predictor (99% accurate) predicted one-boxing.

*EDT:*
$$
V(\text{one-box}) = 0.99 \times 10^6 = 990{,}000,
$$
$$
V(\text{two-box}) = 0.01\times 10^6 + 1{,}000 = 11{,}000.
$$

*CDT:* the prediction is upstream. Let $q$ be your current credence that B is full. Then
$$
U(\text{one-box}) = q\cdot 10^6,\qquad U(\text{two-box}) = q\cdot 10^6+1{,}000.
$$
Two-boxing wins by \$1,000 for every $q$. This is the source's stated CDT verdict: "the action of the player will not affect the outcome."

The structural lesson is that CDT obeys **causal dominance**. If one act is better within every dependency hypothesis, it is chosen, however strongly the acts correlate with those hypotheses.

### 5.4 The twin prisoner's dilemma

The source cites Lewis's (1979) argument that the prisoner's dilemma is a Newcomb problem. Suppose you play against a near-copy of yourself whose choice is strongly correlated with yours but not caused by it. Defection dominates causally within each hypothesis about the twin's move, so CDT defects. EDT notes that cooperation is evidence the twin cooperates, and may cooperate. Any case where your action and another agent's action share a common cause has this Newcomb shape.

## 6. The hard cases: unstable decisions

The deepest criticism the source reports comes from Egan (2007). The intuitive rule is "do what you expect will bring about the best results." CDT's algorithm instead says "do whatever has the best expected outcome, *holding fixed our initial views about the likely causal structure of the world*." The difficulty is that one's initial views may themselves depend on what one is inclined to do.

### 6.1 Death in Damascus

Death predicts where you will be tomorrow and waits there. You can go to Aleppo or stay in Damascus. Let $a$ be your current credence that you will go to Aleppo. Since Death is reliable, your credence that Death is in Aleppo is about $a$. With $D(\text{meet Death})=-1$ and $0$ otherwise:
$$
U(\text{Aleppo}) = -a,\qquad U(\text{Damascus}) = -(1-a).
$$
CDT prefers Damascus iff $a>1/2$. But concluding that you will go to Damascus pushes $a$ toward 0, which makes Aleppo better, and so on. The source says a CDT agent here is "unable to process the correlation." More precisely, naive CDT gives a verdict that depends on your current self-prediction and reverses when you act on it.

### 6.2 The Psychopath Button

Paul can press a button that kills all psychopaths. Only a psychopath would press it, Paul thinks, and Paul is far more averse to dying than to living among psychopaths. Illustrative numbers (mine):

- $D(\text{no psychopaths, Paul alive})=+10$, $D(\text{status quo})=0$, $D(\text{Paul dies})=-100$
- prior $P(\text{Paul is a psychopath})=0.05$
- $P(\text{psychopath}\mid\text{press})=0.9$

Being a psychopath is a fixed trait, upstream of the act. Naive CDT holds it at the prior:
$$
U(\text{press}) = 0.95(10) + 0.05(-100) = 4.5 > 0 = U(\text{don't press}).
$$
CDT presses. EDT computes $0.1(10)+0.9(-100) = -89$ and refrains. Egan reports that "pretty much everyone" agrees Paul should not press.

### 6.3 The Adversarial Offer

This example is due to Oesterheld and Conitzer and is quoted in the source. A seller fills each of two boxes with \$3 if she predicted the buyer would *not* take it. Each box costs \$1, and the prediction is 75% accurate. Whatever the seller predicted, at least one box contains \$3. Write $x_1, x_2$ for your credences that boxes 1 and 2 are full. Then $x_1+x_2\ge 1$, so some box has causal expected value $3x_i \ge 1.5 > 1$. CDT therefore always buys.

But conditional on buying box $i$, the seller probably predicted that purchase, so box $i$ is full with probability $0.25$. The buyer's expected payoff is $0.25(3)-1=-0.25$. The seller profits on average from CDT buyers. The same authors argue this generalizes to diachronic Dutch books.

### 6.4 Ratifiability and deliberational equilibrium

The source reports one response: Joyce's claim that CDT can treat "information about what one is inclined or likely to do as evidence." I now develop that response into a concrete procedure. This is my reconstruction, informed by Jeffrey, Harper, Skyrms and Joyce, but it goes beyond what the source states.

**Ratifiability.** An act $A$ is *ratifiable* if, computing causal expected utilities with credences conditioned on the news that you have decided on $A$, no alternative beats it:
$$
U_A(A) \ge U_A(B)\quad\text{for all } B, \qquad \text{where } U_A(B)=\sum_i P(K_i\mid A)\sum_j P(O_j\mid B\wedge K_i)\,D(O_j).
$$
This still uses causal dependence $P(O_j\mid B\wedge K_i)$. But it evaluates alternatives from the epistemic standpoint of someone who has settled on $A$.

Applied to the cases above:

- **Newcomb.** Two-boxing is ratifiable. Given that you two-box, B is probably empty, and two-boxing is still better by \$1,000.
- **Bathsheba.** Sending is ratifiable, since it dominates.
- **Psychopath Button.** Given that Paul has decided to press, $P(\text{psychopath})=0.9$, and $U(\text{press})=-89<0$. Pressing is *not* ratifiable. Not pressing is ratifiable, because given that decision Paul's psychopath credence is low, and then pressing *would* look good. Hmm: by the numbers above, with prior 0.05, pressing scores 4.5, which beats 0. So "don't press" is not ratifiable either.
- **Death in Damascus.** Neither pure act is ratifiable.

**Deliberational dynamics.** When no pure act is ratifiable, model deliberation as a process. The agent's credence $\pi$ of performing each act drifts toward acts with higher current causal utility. Credences in the dependency hypotheses are updated as $P(K_i)=\sum_A \pi(A)P(K_i\mid A)$. The agent decides at a fixed point, where no act has strictly higher utility than the current mix. This is the precise sense in which CDT can "take into account" one's own inclinations.

- In **Death in Damascus**, the fixed point is $a=1/2$. There both acts have utility $-1/2$, and the agent is indifferent. The theory then permits either act, perhaps chosen by a coin flip that Death cannot predict.
- In the **Psychopath Button**, let $\pi$ be Paul's credence that he presses and $p(\pi)=0.05(1-\pi)+0.9\pi$ his resulting credence that he is a psychopath. Then
$$
U(\text{press}) = 10(1-p) - 100p = 10 - 110p.
$$
This is zero at $p=1/11\approx 0.091$, which corresponds to $\pi\approx 0.048$. At equilibrium Paul is almost certain not to press and is indifferent at the margin. That reverses the naive verdict and roughly matches intuition.

**Caveats.** First, equilibria may be mixed and verdicts may be permissive. Second, the Adversarial Offer resists this fix. No pure act is ratifiable there. "Buy nothing" makes both boxes look full, so buying looks good. Any purchase makes the chosen box look empty and the other look full. Oesterheld and Conitzer argue that the deliberational equilibria still have the buyer purchasing with positive probability at an expected loss. Whether deliberational CDT fully answers these "money-pump" variants is, as the source indicates, disputed. Spencer and Joyce take opposing positions.

## 7. Open questions and how I would resolve them in practice

**What counts as a "cause"?** The source leaves this unanalysed. My operational answer is the interventionist one. A variable is influenceable iff it is a descendant of the act node in the best causal model you have. Predictions made earlier, fixed character traits, and twins' decisions are not descendants, even when they are strongly correlated with the act. If you are uncertain which causal model is right, put a credence over models and include them among the $K_i$. That keeps the formula well defined without the imaging regress the source mentions.

**Which credences count as "unconditional"?** This is the crux of Egan's objection. There are two coherent readings:

- **(a)** Credences at the start of deliberation (naive CDT).
- **(b)** Credences at a deliberational equilibrium (Joyce-style CDT).

I recommend (b) whenever the act carries evidence about the dependency hypotheses, and note that (a) and (b) coincide whenever it does not. The cost of (b) is mixed or permissive verdicts in some cases. Its benefit is that it handles the Psychopath Button and Death in Damascus without abandoning causal dominance. In particular it does not change the two-boxing verdict in Newcomb, because two-boxing dominates at every credence.

**Is two-boxing rational?** The source reports that philosophers disagree, while noting that most prefer CDT to EDT when forced to choose. The CDT defender argues that the one-boxer's riches come from being the kind of agent predictors reward, not from the act. Inside the decision situation, with the money already placed, taking the extra \$1,000 cannot make you poorer. The critic's reply, "if you're so smart, why ain'cha rich?", is a reply about which *dispositions* to cultivate. Plain CDT answers that question too, by applying itself one level up. *Before* the prediction is made, choosing to become a one-boxer causally influences the prediction, so CDT recommends precommitment when precommitment is available. This policy-level application is my gloss, not the source's. It shows that CDT can endorse binding oneself in advance while still recommending two-boxing once nothing more can be influenced. Meacham's work on binding, cited in the source, examines exactly this tension.

## 8. Philosophical motivation in brief

CDT rests on a simple thought: decisions are tools for changing the world, so they should be evaluated by the differences they make. EDT treats an act as a source of information about oneself. This lets it count "good news" that the act does not produce, as in abstaining to seem charismatic or one-boxing to seem predictable. CDT forbids that kind of news management. The price is the instability cases. In those cases the agent's own choice is evidence about the very states CDT tells her to hold fixed, and some account of self-knowledge during deliberation is unavoidable.

## 9. Conclusion

Formally, CDT replaces the conditional probabilities of evidential theory with probabilities of counterfactuals, $U(A)=\sum_j P(A\mathbin{\square\!\!\rightarrow}O_j)D(O_j)$. Equivalently, it uses unconditional credences over dependency hypotheses, or interventional probabilities $P(o\mid\mathrm{do}(a))$. It agrees with EDT whenever acts carry no evidence about factors outside the agent's control. It diverges, recommending sending for Bathsheba, two-boxing, and defecting against a twin, exactly when they do.

The source rightly flags two weaknesses. CDT does not by itself say how to compute counterfactual probabilities. And holding initial credences fixed yields troubling verdicts when one's choice is evidence about one's situation. I have suggested an operational repair for each. For the first, model acts as interventions in a causal model, with uncertainty over models absorbed into the dependency hypotheses. For the second, evaluate acts at a deliberational equilibrium, checking ratifiability. That gives a usable procedure for new cases. It also leaves open whether adversarial predictor cases show a genuine flaw or merely the cost of refusing to manage the news.

### References (selected)

- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility."
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities"; (1981) "Causal decision theory."
- Egan, A. (2007). "Some counterexamples to causal decision theory."
- Joyce, J. (2012). "Regret and instability in causal decision theory."
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists."
- Wikipedia, "Causal decision theory," rev. 1381555528 (the reference article).