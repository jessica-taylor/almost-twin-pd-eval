# Causal Decision Theory: Choosing by What Your Actions Bring About

## 1. The idea in one sentence

Causal decision theory (CDT) says that a rational agent should choose the action whose *causal consequences* are best in expectation. The reference article states it this way and sets it against **evidential decision theory** (EDT), which recommends the action that would be the best *news* to learn you had taken.

In ordinary decisions the two theories agree. They come apart only when an action is evidence about something it does not cause. That gap explains why CDT exists, and it is also where CDT's best-known difficulties arise. This essay first sets out the formal machinery, then gives operational versions you can compute with, works through the standard cases with numbers, and ends with the open problems and one way to handle them.

Throughout, I mark which claims come from the source article and which are my own reconstructions or proposals.

## 2. The basic setup

We have:

- a finite set of **acts** $\mathcal A = \{A_1,\dots,A_n\}$, which are the options genuinely open to the agent;
- a finite set of **outcomes** $O_1,\dots,O_m$, with a desirability (utility) function $D(O_j)\in\mathbb R$;
- a credence function $P$ over propositions about the world, including propositions about which act is chosen.

In Savage's textbook framework we also have **states** $S$ and compute $\sum_S P(S)\,D(A,S)$. That works only if the states are chosen so that the act cannot influence them. Once an act can influence or correlate with the states, we have to decide which probability of a state to use.

EDT answers with the conditional probability:
$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j).
$$

CDT, in the formulation by Gibbard and Harper (1981) quoted in the source, answers with a probability of a counterfactual:
$$
U(A) \;=\; \sum_j P(A \mathbin{\Box\!\!\to} O_j)\, D(O_j).
$$

**A note on reading the arrow.** The source glosses $P(A\to O_j)$ as the probability that "$A$ necessarily implies $O_j$." I think that gloss misleads. In Gibbard and Harper, and in Stalnaker and Lewis before them, the connective is the *counterfactual conditional*: "if $A$ were done, $O_j$ would obtain." It is not strict implication. A strict conditional would almost never hold for a single outcome, because $A$ rarely entails $O_j$ by necessity. The counterfactual reading is what makes the formula do causal work, so I use the box-arrow $\Box\!\!\to$.

The informal content, which the source illustrates with an apple, is straightforward. You do not know whether the apple is good. Your expected causal payoff from eating it depends on three things: how likely the apple is to be good, how much a good apple pleases you, and how much a bad one displeases you. If $g = P(\text{good})$, then
$$
U(\text{eat}) = g\,D(\text{happy}) + (1-g)\,D(\text{sad}).
$$
Here CDT and EDT agree. Eating the apple does not make it more likely to have been good, and nothing about your choice is evidence about the apple's quality.

## 3. When do the two theories coincide?

### 3.1 The Gibbard–Harper condition

The source reports that, given two axioms (one related to the controversial principle of *conditional excluded middle*), statistical independence of $A$ and $A\mathbin{\Box\!\!\to}O_j$ guarantees $P(A\mathbin{\Box\!\!\to}O_j)=P(O_j\mid A)$. Here is a reconstruction of the argument.

- **Axiom 1 (centering / modus ponens):** $A \wedge (A\mathbin{\Box\!\!\to}O) \equiv A\wedge O$. If $A$ actually holds, then "if $A$ were, $O$ would be" is true exactly when $O$ is actually true.
- **Axiom 2 (conditional excluded middle, CEM):** $(A\mathbin{\Box\!\!\to}O)\vee(A\mathbin{\Box\!\!\to}\neg O)$. For each act and outcome, there is a definite fact about what would happen.

From Axiom 1,
$$
P(O\mid A)=\frac{P(A\wedge O)}{P(A)}=\frac{P\big(A\wedge(A\mathbin{\Box\!\!\to}O)\big)}{P(A)}=P(A\mathbin{\Box\!\!\to}O\mid A).
$$
If the counterfactual is independent of the act, the last term equals $P(A\mathbin{\Box\!\!\to}O)$. CEM ensures that for each act the counterfactuals $A\mathbin{\Box\!\!\to}O_j$ partition the space, so $U(A)$ is a genuine expectation.

The upshot is that **CDT and EDT diverge exactly when your choice is evidence about what would happen under it.** This occurs, for example, when a common cause influences both your choice and the outcome.

### 3.2 Why we cannot simply identify the two

One might hope that some conditional connective satisfies $P(A\to O)=P(O\mid A)$ in general. Lewis (1976) showed this hope fails. As the source's footnote puts it, a class of probability functions closed under conditionalization admits such a "probability conditional" only if every function in it is trivial, assigning positive probability to at most two incompatible alternatives. CDT therefore cannot be reduced to EDT by clever semantics. Probabilities of conditionals and conditional probabilities really are different objects.

## 4. Operational forms of CDT

The counterfactual formula is elegant, but it does not tell you where the numbers $P(A\mathbin{\Box\!\!\to}O_j)$ come from. The source flags this as the theory's "vagueness." Three standard ways to make CDT computable are below. The source mentions only imaging; the other two are my additions from the wider literature, included because they are the most usable in practice.

### 4.1 Dependency hypotheses (Lewis 1981; Skyrms)

Partition the possibilities into **dependency hypotheses** $K_1,\dots,K_r$. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on acts. It includes everything outside the agent's control that matters to the outcome: the contents of a box, a king's charisma, a predictor's forecast. Then
$$
\boxed{\;U(A)=\sum_{i} P(K_i)\sum_j P(O_j\mid A\wedge K_i)\,D(O_j)\;}
$$
The essential feature is that the weights are the **unconditional** $P(K_i)$, not $P(K_i\mid A)$. EDT would instead use
$$
V(A)=\sum_i P(K_i\mid A)\sum_j P(O_j\mid A\wedge K_i)\,D(O_j).
$$
Seen this way, the entire disagreement between the theories is whether to update your view of the causal background on your own choice.

### 4.2 Imaging (Lewis)

The source describes Lewis's imaging. To evaluate $P(A\mathbin{\Box\!\!\to}O)$, move the probability mass of each world $w$ to the closest world $w_A$ in which $A$ holds:
$$
P_A(w') = \sum_{w:\,w_A = w'} P(w), \qquad P(A\mathbin{\Box\!\!\to}O)=P_A(O).
$$
Conditioning and imaging differ in where the mass goes. Conditioning deletes the $\neg A$-worlds and renormalizes, so the remaining $A$-worlds keep their relative weights, and those weights carry correlational information. Imaging keeps every world's mass and moves it minimally. A world in which the predictor forecast two-boxing and you one-boxed is moved to a nearby world in which you two-box *and the forecast is unchanged*.

### 4.3 Interventions (Pearl)

In a causal Bayesian network, let $K$ be the set of causal parents of the act node (the common causes of choice and outcome). The **back-door adjustment** formula is
$$
P(O\mid do(A))=\sum_k P(k)\,P(O\mid A, k),
$$
which has exactly the form of §4.1. I offer this as an operational reading, not a claim made by the source. *CDT is expected utility under $do(A)$.* You cut the arrows into the act node, so that the act's causes, and hence your evidence about them, stay where they were.

For most practical problems I recommend the dependency-hypothesis form. It asks you to (i) list the factors outside your control that matter, (ii) assign them credence without conditioning on your act, and (iii) compute what each act would bring about given each factor.

## 5. Worked examples

### 5.1 King David and Bathsheba (medical-Newcomb type)

The source presents Gibbard and Harper's case. Charisma ($C$) is fixed. It makes just acts more likely, and it lowers the risk of revolt, but unjust acts do not themselves cause revolts. Here are some illustrative numbers of my own:

| | value |
|---|---|
| $P(C)$ | 0.5 |
| $P(\text{send}\mid C),\; P(\text{send}\mid\neg C)$ | 0.2, 0.8 |
| $P(R\mid C),\; P(R\mid \neg C)$ (independent of act) | 0.1, 0.9 |
| $D$: Bathsheba $+10$, revolt $-100$ | |

**CDT.** The dependency hypotheses are $C,\neg C$, weighted unconditionally. $P(R)=0.5(0.1)+0.5(0.9)=0.5$, so
$$U(\text{send})=10-50=-40,\qquad U(\text{abstain})=-50.$$
Sending wins by exactly 10, and it wins by 10 for *any* value of $P(C)$. It dominates.

**EDT.** By Bayes, $P(C\mid\text{send})=0.1/0.5=0.2$ and $P(C\mid\text{abstain})=0.4/0.5=0.8$. Then $P(R\mid\text{send})=0.74$ and $P(R\mid\text{abstain})=0.26$:
$$V(\text{send})=10-74=-64,\qquad V(\text{abstain})=-26.$$
EDT recommends abstaining, as the source says.

The causalist's complaint is that abstaining does not make David charismatic. It only lets him enjoy feeling as though he might be. Cases like this one, where the act is merely a *symptom* of a fixed cause, are why, as the source notes, philosophers asked to choose between the two theories usually prefer CDT.

### 5.2 Newcomb's problem

Box A holds a visible \$1,000. Box B holds \$1,000,000 if and only if a 99%-reliable predictor forecast that you would take only B. Let $p$ be your unconditional credence that B is full. The dependency hypotheses are "full" and "empty":
$$
U(\text{one-box}) = p\cdot 10^6,\qquad U(\text{two-box}) = p\cdot 10^6 + 10^3.
$$
Two-boxing wins by \$1,000 whatever $p$ is. The prediction is already made, and your choice cannot reach back to change it. This dominance reasoning is CDT's verdict, as the source reports.

EDT conditions on the act instead:
$$
V(\text{one-box})=0.99\cdot 10^6=990{,}000,\qquad V(\text{two-box})=10^3+0.01\cdot10^6=11{,}000.
$$
The standing objection is the slogan "if you're so smart, why aren't you rich?" Agents who follow CDT reliably walk away with \$1,000, while agents who follow EDT walk away with a million. The source notes that philosophers remain divided on which is rational. The CDT reply is that Newcomb's problem rewards a certain kind of *agent*, not a certain *choice*. Given the box's actual contents, whatever they are, taking both is better by \$1,000.

### 5.3 The twin prisoner's dilemma

The source mentions, following Lewis (1979), that the prisoner's dilemma against a near-copy has the same structure. Your twin's choice is strongly correlated with yours but not caused by it. CDT holds the twin's choice fixed as a dependency hypothesis, and defection dominates. EDT treats your cooperation as evidence of the twin's cooperation and cooperates. The lesson for applying CDT is that **correlation through a common origin** (shared code, shared upbringing, a shared predictor) is never a reason, by CDT's lights, to act differently.

## 6. The hard part: which credences to hold fixed?

The dependency-hypothesis formula uses $P(K_i)$, the agent's *unconditional* credence in each causal background. But that credence is not fixed independently of deliberation. If the agent becomes confident she will choose $A$, and $A$ is correlated with $K_i$, then her unconditional credence in $K_i$ should shift. This is the problem at the heart of the counterexamples the source surveys, and the theory as originally stated does not resolve it.

### 6.1 Death in Damascus

Death predicts where you will be tomorrow and waits there. You can stay in Damascus ($S_D$) or flee to Aleppo ($S_A$). Let $x$ be your current credence that Death is in Damascus, and let meeting Death be worth $-1$:
$$
U(S_D)=-x,\qquad U(S_A)=-(1-x).
$$
If $x>\tfrac12$, CDT says flee. But if you come to expect to flee, Death's reliability means you should come to believe Death is in Aleppo, and then CDT says stay, and so on. No pure act is stable. The source says a CDT agent "would be unable to process the correlation." A more precise statement is that **CDT, as written, gives a verdict relative to a credal state that its own verdict undermines.**

### 6.2 Ratifiability

Jeffrey, and Harper (cited in the source), proposed a refinement. An act $A$ is **ratifiable** if it maximizes causal expected utility computed with the credences you would have *on deciding* to do $A$:
$$
A \text{ ratifiable} \iff \forall B:\; \sum_i P(K_i\mid A)\,u(B,K_i)\;\le\;\sum_i P(K_i\mid A)\,u(A,K_i),
$$
where $u(B,K_i)=\sum_j P(O_j\mid B\wedge K_i)D(O_j)$. The rule is then to choose a ratifiable act. Notice that the conditional probability $P(K_i\mid A)$ appears only in the role of "what I'd believe if I chose $A$." The act's *value* is still causal, since each $B$ is evaluated in a fixed background.

In Newcomb's problem two-boxing is ratifiable and one-boxing is not, so ratifiability confirms the CDT verdict. In Death in Damascus *neither* city is ratifiable.

### 6.3 Psychopath Button

The source quotes Egan's case. Paul would like a world without psychopaths, but he believes only a psychopath would press the button, and he much prefers living among psychopaths to dying. Here are illustrative numbers of my own: $D(\text{press},\neg\Psi)=+10$, $D(\text{press},\Psi)=-100$, $D(\neg\text{press})=0$, prior $P(\Psi)=0.05$, $P(\Psi\mid\text{press})=0.9$, $P(\Psi\mid\neg\text{press})=0.01$.

**Naïve CDT** uses the prior:
$$U(\text{press})=0.95(10)-0.05(100)=4.5>0.$$
It says press. Egan reports that "pretty much everyone" thinks this is wrong.

**Ratifiability.** On deciding to press, $P(\Psi)=0.9$, and $U(\text{press})=1-90=-89<0$. So pressing is unratifiable. On deciding not to press, $P(\Psi)=0.01$, and $U(\text{press})=9.9-1=8.9>0$. So not pressing is unratifiable too. As in Death in Damascus, nothing is ratifiable.

Egan's diagnosis, as reported in the source, is that the intuitive rule "do what you expect to bring about the best results" differs from CDT's rule "maximize expected outcome *holding fixed your initial credences in dependency hypotheses*." The second clause is the culprit.

### 6.4 An operational proposal: deliberational equilibrium

The source closes this topic by noting that Joyce, CDT's leading modern defender, argues that CDT can treat "information about what one is inclined or likely to do as evidence." What follows is my own reconstruction of how to make that operational, in the spirit of Skyrms's and Joyce's deliberational dynamics.

Let $\sigma\in\Delta(\mathcal A)$ be the agent's current credence about what she will do. Her credence in each dependency hypothesis is then
$$
P_\sigma(K_i)=\sum_{A}\sigma(A)\,P(K_i\mid A).
$$
Compute $U_\sigma(B)=\sum_i P_\sigma(K_i)\,u(B,K_i)$ for each act. Deliberation shifts $\sigma$ toward acts with higher $U_\sigma$. A **deliberational equilibrium** is a $\sigma^*$ at which every act in its support maximizes $U_{\sigma^*}$. The rule is: *choose in accordance with an equilibrium*, picking any act in its support (or randomizing if you can).

Applied to the Psychopath Button, $U_\sigma(\text{press})=10-110\,P_\sigma(\Psi)$, which is zero exactly when $P_\sigma(\Psi)=1/11$. Solving $0.01+0.89\,\sigma=1/11$ gives $\sigma^*\approx0.09$. At equilibrium Paul is indifferent and only about 9% inclined to press. Joyce's line is that CDT never recommends *confidently* pressing, and that the hesitancy we feel is the instability itself.

In Death in Damascus the equilibrium is $\sigma^*=(\tfrac12,\tfrac12)$, so CDT advises indifference, or a coin flip if Death cannot predict the coin.

I think this is the most defensible way to apply CDT to unstable problems. Two caveats keep the question open:

1. Equilibria can be multiple, and the dynamics then matter.
2. At equilibrium CDT often delivers indifference where intuition delivers a firm "don't press." Whether indifference counts as an adequate answer is exactly what the critics dispute.

### 6.5 The Adversarial Offer

The source's most pointed recent example is due to Oesterheld and Conitzer. Two boxes cost \$1 each, and the buyer may buy at most one. Yesterday the seller put \$3 in each box she predicted the buyer would *not* acquire. Her predictions are accurate with probability 0.75.

**CDT.** The seller predicted some single action, and that action acquires at most one box. So at least one box contains \$3. With $q_1,q_2$ the credences that each box is full, we have $q_1+q_2\ge1$, hence $\max(q_1,q_2)\ge\tfrac12$. Buying the likelier box has causal value at least $3\cdot\tfrac12-1=0.50>0$. Under the equilibrium approach of §6.4 the buyer randomizes between boxes, and each still has causal value of at least \$0.50. So CDT buys.

**Reality, or EDT.** Conditional on buying box 1, it is full with probability 0.25, so the expected profit is $0.75-1=-0.25$. Not buying yields 0. The CDT buyer loses about \$0.25 per round, and the seller profits.

This is the "money-pump" style of objection. CDT can be exploited by a predictor who structures payoffs so that it is always causally attractive to buy, while what the buyer actually receives is systematically correlated with the buyer's own choice. Oesterheld and Conitzer extend the point to diachronic Dutch books. Note that the equilibrium move does not help here: some act always has positive causal value, so CDT never settles on "don't buy."

## 7. A procedure for unfamiliar cases

Gathering the pieces, here is how I would apply CDT to a new decision problem. Steps 1–4 restate standard CDT. Steps 5–6 are my operational proposal.

1. **Fix the acts.** Include only options genuinely available, and allow mixed acts if a randomizer exists that the environment cannot predict.
2. **Identify dependency hypotheses $K_i$.** These are all facts that are causally upstream of or independent of the act and that matter to outcomes: predictions already made, others' fixed choices, your own traits, physical states.
3. **Compute causal payoffs $u(A,K_i)$.** Use $P(O\mid A\wedge K_i)$, or equivalently $P(O\mid do(A),K_i)$. Trace only the forward causal effects of the act.
4. **Check for dominance.** If some act has the highest $u(A,K_i)$ for every $K_i$, CDT chooses it whatever the credences. This settles Newcomb, the twin PD, and Bathsheba.
5. **Otherwise, check stability.** Compute $P(K_i\mid A)$ for each act and test ratifiability. If some act is ratifiable, choose it. If several are, prefer the one with the highest self-conditional causal utility. That tie-breaker is my suggestion and is contested.
6. **If nothing is ratifiable, find a deliberational equilibrium** $\sigma^*$ and act within its support.
7. **Never use $P(K_i\mid A)$ to *rank* acts.** It may only fix the credal state from which acts are compared. Using it to rank acts collapses CDT into EDT.

## 8. Assessment

**What the source establishes.** CDT is expected utility with probabilities of counterfactuals (Gibbard–Harper). It differs from EDT because probabilities of conditionals are not conditional probabilities (Lewis). It agrees with EDT whenever acts are independent of the relevant counterfactuals. It two-boxes in Newcomb and sends for Bathsheba. It leaves the computation of counterfactual probabilities underspecified, with Lewis's imaging facing a regress worry. And it faces counterexamples (Death in Damascus, Psychopath Button, Adversarial Offer) that Egan traces to holding unconditional credences in dependency hypotheses fixed.

**What I have added.** The counterfactual reading of the arrow in place of the source's "necessarily implies." The dependency-hypothesis and interventionist formulations as the working core. Numerical treatments of each case. The deliberational-equilibrium procedure as a precise version of Joyce's defense.

On the regress the source mentions: imaging presupposes a closeness ordering over worlds, and the agent may be uncertain about it. The dependency-hypothesis form sidesteps much of this by putting that uncertainty into the $K_i$ themselves. Uncertainty about the causal structure is just more uncertainty about which $K_i$ is true. That works only so long as the agent can say what the candidate structures are. This is my view, not the source's, and it relocates the problem rather than dissolving it.

The deepest tension is this. CDT's motivation is that rational choice should track *control*: you should be moved only by what you can affect. Its trouble cases are all ones in which an environment rewards or punishes the *kind of agent* you are, through predictions or correlations that your choice cannot causally touch. CDT's defenders say rationality concerns choices given circumstances, not which dispositions get rewarded. Its critics point out that the theory's adherents can be predictably beaten.

## 9. Conclusion

Causal decision theory evaluates each act by asking what it would bring about. Formally, it weights outcomes by $P(A\mathbin{\Box\!\!\to}O)$, or equivalently by unconditional credences over fixed causal backgrounds, rather than by $P(O\mid A)$. In most decisions this is indistinguishable from evidential reasoning. Where acts are mere symptoms of fixed causes, as in the Bathsheba case, CDT gives the verdict most people find correct. Where a predictor ties payoffs to what the agent will do, as in Newcomb's problem and the Adversarial Offer, CDT's refusal to count correlation can leave its adherents poorer. Where the agent's own inclination is evidence about the background, as in Death in Damascus and the Psychopath Button, the plain theory is unstable. Ratifiability and deliberational equilibrium are the best available repairs, but they sometimes yield indifference where intuition demands a firm answer. Applying CDT well means separating cause from correlation carefully, and recognizing that the theory's answer to "which credences do I hold fixed?" is still under negotiation.

## References

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116(1).
- Gibbard, A., & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*.
- Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese* 187.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Phil. Review* 85; (1981). "Causal decision theory." *AJP* 59.
- Oesterheld, C., & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Phil. Quarterly* 71(4).
- Wikipedia contributors, "Causal decision theory," rev. 1381555528 (CC BY-SA 4.0).