# Causal Decision Theory: What It Computes and Where It Strains

## 1. The question CDT answers

Decision theory tells an agent how to choose among actions when the outcomes are uncertain. The usual answer is to maximize expected utility. That answer hides a choice: *expected with respect to which probabilities?*

**Causal decision theory** (CDT) says the probabilities should measure what the action would *bring about*. The reference article puts it this way: choose "the action which causes the best outcome in expectation." Its rival, **evidential decision theory** (EDT), recommends the action that would be the best *news*, the one whose performance would most raise your expectation of a good outcome.

In most ordinary problems the two theories agree. They come apart when an action is *correlated* with good or bad outcomes without *causing* them, for example when the action is a symptom of some hidden condition, or when someone predicted it. This essay does four things:

- sets out the formal definitions;
- shows how CDT handles dependencies and counterfactuals;
- works through the standard cases numerically;
- develops a concrete operating procedure, including how to deal with "unstable" problems that the source raises but does not resolve.

On attribution: material credited to "the source" comes from the reference article. The operational procedure in §7 and the worked numbers throughout are my own reconstructions, built on standard literature where noted.

## 2. The basic setup

Let $\mathcal{A}$ be a finite set of available acts and $\{O_j\}$ a partition of outcomes. Let $D(O_j)$ be the desirability, or utility, of outcome $O_j$. The agent has a credence function $P$.

The source's informal example already contains the essential structure. You can eat an apple that is good with probability $p$. A good apple makes you happy (utility $h>0$) and a bad one makes you sad (utility $-s$). Not eating has utility $0$. Then

$$
U(\text{eat}) = p\,h - (1-p)\,s ,
$$

so you should eat iff $p > s/(h+s)$.

Notice why this is uncontroversial. Whether the apple is good is a *state of the world*. It is fixed before you act, and you have no reason to think your choosing to eat tells you anything about it. In Savage's framework, states are assumed independent of acts. Under that assumption, "what my act causes" and "what my act indicates" coincide, and every reasonable theory gives the same answer.

The whole debate about CDT concerns what to do when that independence fails.

## 3. Two expected utilities

**Evidential expected utility.** EDT weights outcomes by conditional probability:

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

**Causal expected utility (Gibbard–Harper).** The source presents Gibbard and Harper's 1981 formulation, which uses "probabilities of counterfactuals":

$$
U(A) = \sum_j P(A \mathbin{\square\!\!\to} O_j)\, D(O_j).
$$

Here $A \mathbin{\square\!\!\to} O_j$ is the subjunctive conditional "if I were to do $A$, $O_j$ would obtain."

The source glosses $P(A \to O_j)$ as the probability "that $A$ necessarily implies $O_j$." I think that wording is misleading if read literally. Logical or metaphysical necessitation is far too strong: almost nothing is *necessitated* by eating an apple. The intended reading, in Gibbard and Harper and in the counterfactual literature generally, is the would-counterfactual. That reading is the one used below.

### When the two coincide

If $P(A \mathbin{\square\!\!\to} O) = P(O\mid A)$ always held, CDT would collapse into EDT. The source cites Lewis's 1976 triviality result: no conditional connective has probabilities that equal conditional probabilities across a class of credence functions closed under conditionalization, except for trivial credence functions. So the two quantities are genuinely different.

The source also reports a sufficient condition for agreement from Gibbard and Harper. The derivation is short enough to give in full. Assume two axioms:

1. **Conditional excluded middle:** for each act $A$, exactly one $O_j$ satisfies $A \mathbin{\square\!\!\to} O_j$.
2. **Centering for actual acts:** $A \wedge (A \mathbin{\square\!\!\to} O) \;\leftrightarrow\; A \wedge O$. In words, if you actually do $A$, what would happen if you did $A$ is just what happens.

Now suppose $A$ is probabilistically independent of $A \mathbin{\square\!\!\to} O$. Then

$$
P(O \mid A) = \frac{P(A\wedge O)}{P(A)} = \frac{P\big(A \wedge (A\mathbin{\square\!\!\to} O)\big)}{P(A)} = \frac{P(A)\,P(A\mathbin{\square\!\!\to} O)}{P(A)} = P(A \mathbin{\square\!\!\to} O).
$$

Divergence therefore requires that *the act carries information about which counterfactuals are true*. In other words, the act must be evidence about the causal structure of your situation, not merely a lever within it.

## 4. Making the counterfactuals computable

The source states a real gap plainly. CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." It mentions one proposal, Lewis's **imaging**: to evaluate the conditional on $A$, move each world $w$'s probability mass to the closest $A$-world $w_A$:

$$
P^{A}(w') = \sum_{w} P(w)\,\mathbf{1}[w_A = w'], \qquad U(A) = \sum_{w'} P^A(w')\, D(w').
$$

Compare this with conditionalization. Conditionalization deletes the $\neg A$-worlds and renormalizes, so the $A$-worlds you keep are the ones evidentially associated with $A$. Imaging instead *transports* every world, preserving each world's prior weight on everything the act cannot affect.

The source notes the regress worry: imaging requires knowing what the closest $A$-world is, which is itself a counterfactual matter one may be uncertain about.

The standard way to tame this, which goes beyond the source's text, is Lewis's and Skyrms's **dependency hypothesis** formulation. A dependency hypothesis $K$ is a maximally specific proposition about how outcomes depend causally on acts. Think of it as a complete specification of the causally relevant background that the act cannot influence. Let $\{K\}$ partition such hypotheses. Then

$$
\boxed{\,U(A) = \sum_{K} P(K) \sum_j P(O_j \mid A \wedge K)\, D(O_j)\,}
$$

The key feature is that the weight on $K$ is the **unconditional** $P(K)$, not $P(K\mid A)$. EDT's formula is the same except that $P(K)$ is replaced by $P(K\mid A)$. The entire disagreement lives in that substitution.

Readers who know causal Bayes nets will recognize this as back-door adjustment. If $K$ is a set of variables that causally precede the act and screen off the confounding, then

$$
P(O\mid do(A)) = \sum_k P(k)\, P(O\mid A, k).
$$

This gives an operational answer to the source's vagueness worry, and it is my framing rather than the source's. The counterfactual probabilities are *interventional* probabilities in the agent's causal model of the situation. The modeling burden is to say which variables are upstream of the act and therefore fixed under intervention. The regress problem does not vanish. It becomes the familiar problem of uncertainty over causal models, which can be handled by putting a prior over models and treating each model as a dependency hypothesis.

## 5. The classic divergence cases

### 5.1 King David and Bathsheba (medical-Newcomb type)

This example is from the source, quoting Gibbard and Harper. Charisma $C$ is fixed in adulthood. It makes just behavior more likely and successful revolt less likely, while unjust acts do not themselves cause revolts. I will put numbers on it:

| Quantity | Charismatic $C$ | Uncharismatic $\neg C$ |
|---|---|---|
| Prior | 0.5 | 0.5 |
| $P(\text{abstain}\mid\cdot)$ | 0.9 | 0.2 |
| $P(\text{revolt}\mid\cdot)$ (independent of act) | 0.1 | 0.8 |

Utilities: Bathsheba $+10$, revolt $-100$, additive.

**CDT.** Charisma is the dependency hypothesis, weighted by its prior. So $P(\text{revolt}) = 0.5(0.1)+0.5(0.8) = 0.45$ whatever David does:

$$
U(\text{send}) = 10 - 45 = -35,\qquad U(\text{abstain}) = -45.
$$

Sending is better by exactly the $10$ he gains, because sending changes nothing else.

**EDT.** Conditioning on the act updates beliefs about charisma. Since $P(\text{send}\mid C)=0.1$ and $P(\text{send}\mid \neg C)=0.8$,

$$
P(C\mid\text{send}) = \tfrac{0.05}{0.45} = \tfrac19,\quad P(C\mid\text{abstain}) = \tfrac{0.45}{0.55} = \tfrac{9}{11}.
$$

That gives $P(\text{revolt}\mid\text{send}) \approx 0.722$ and $P(\text{revolt}\mid\text{abstain})\approx 0.227$, so

$$
V(\text{send}) \approx -62.2,\qquad V(\text{abstain}) \approx -22.7.
$$

EDT says abstain, which is the source's verdict. CDT's diagnosis is that EDT is "managing the news": abstaining makes David *look* charismatic without making him so. The source reports that when forced to choose, philosophers usually side with CDT here, and cases of this type are its strongest motivation.

### 5.2 Newcomb's problem

This is the case from the source. Box A holds a visible \$1,000. Box B holds \$1,000,000 iff a 99%-reliable predictor predicted one-boxing.

**CDT.** The prediction is upstream of the choice, so let $q = P(\text{B full})$ be held fixed:

$$
U(\text{two}) = q(1{,}001{,}000) + (1-q)(1{,}000) = U(\text{one}) + 1{,}000 .
$$

Two-boxing wins for *every* $q$. This is the dominance argument, and the source confirms CDT recommends it.

**EDT.**
$$
V(\text{one}) = 0.99 \times 10^6 = 990{,}000,
$$
$$
V(\text{two}) = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
$$

EDT one-boxes.

The source notes that this is an "alleged counterexample": CDT agents predictably walk away with \$1,000, and philosophers genuinely disagree about which answer is rational. The CDT defender replies that the one-boxer is rewarded for being a certain kind of agent, not for the act. Once the boxes are filled, the act itself only ever costs \$1,000. Lewis's observation, mentioned in the source, is that a prisoner's dilemma against a near-copy of yourself has the same structure. Your twin's choice is correlated with yours but not caused by it, so CDT defects.

### 5.3 What the formalism shows about these cases

In both 5.1 and 5.2, CDT's verdict is a **dominance** verdict relative to the dependency hypotheses. If one act is better than another under every $K$, CDT prefers it no matter what $P(K)$ is.

So one useful test for an unfamiliar case: identify the act-independent causal background. If an act dominates under every background, CDT picks it, and no correlational information can change that.

## 6. Instability: when your own choice is evidence

The more serious criticisms in the source concern cases where the CDT verdict depends on $P(K)$, and $P(K)$ in turn depends on what the agent expects to do.

### 6.1 Death in Damascus

Death predicts where you will be tomorrow (Damascus or Aleppo) and waits there, reliably. Let $x$ be your current credence that you will go to Aleppo. Assume, for this illustration, a perfectly reliable predictor. Then your credence that Death is in Aleppo is also $x$, and

$$
U(\text{Aleppo}) = -x,\qquad U(\text{Damascus}) = -(1-x).
$$

(Survival scores $0$ and death $-1$.)

Whichever city you currently lean toward, CDT recommends the other one. But leaning toward the other city shifts $x$, which reverses the recommendation. Every pure choice is **unratifiable**.

The source says a CDT agent "would be unable to process the correlation." I would phrase it more carefully. Naive CDT, evaluated once at a fixed credence, gives a recommendation that undermines itself.

### 6.2 Ratifiability and deliberational equilibrium

The source cites Harper, Joyce, and Meacham but does not develop their responses. Here is the mainstream development, which supplies the missing operational rule.

Let $U_B(A)$ be the causal expected utility of $A$ computed with credences $P(\cdot\mid \text{I decide on } B)$ in place of $P$.

- **Ratifiability (Jeffrey, Harper):** act $A$ is ratifiable iff $U_A(A) \ge U_A(B)$ for all $B$. A ratifiable act is one you would not regret choosing, given what choosing it tells you.
- **Deliberational dynamics (Skyrms, Arntzenius, Joyce):** treat deliberation as a process on your credences over acts, $\mathbf{x}$. At each step, compute $U$ under current credences and shift credence toward acts with higher $U$. Credences in dependency hypotheses update on the information that your credences over acts are changing. Choose at a **deliberational equilibrium** $\mathbf{x}^*$, where no act has higher causal expected utility than the current mixture.

This is where Joyce's point in the source ("information about what one is inclined or likely to do as evidence") has formal teeth. CDT never conditions on the act *as an intervention*. It does let your evolving *beliefs about what you will do* inform your beliefs about the world.

In Death in Damascus, the equilibrium is $x^*=1/2$. At that point the two cities have equal causal expected utility, and either choice (or a coin flip) is permissible.

### 6.3 The Psychopath Button

This case is from the source, citing Egan. Paul wants a world without psychopaths but believes only a psychopath would press the button, and pressing kills him if he is one. My numbers: a psychopath-free world is worth $+10$, the status quo $0$, death $-100$. Let $\pi = P(\text{Paul is a psychopath})$. Then

$$
U(\text{press}) = 10(1-\pi) - 100\pi = 10 - 110\pi ,
$$

which is positive iff $\pi < 1/11$.

With a modest prior such as $\pi = 0.05$, naive CDT says press, because $U = 4.5$. That is Egan's complaint, and "pretty much everyone" thinks Paul should not press.

Now apply the ratifiability machinery. Conditional on deciding to press, Paul's credence that he is a psychopath jumps, say to $\pi = 0.9$. Then $U = -89$, so pressing is unratifiable. Conditional on deciding not to press, $\pi$ might fall to $0.02$, giving $U=7.8>0$, so refraining is unratifiable too.

The deliberational equilibrium sits where $\pi(\mathbf{x}^*) = 1/11$, which leaves Paul indifferent. On this account CDT does not *demand* pressing. It reaches a balanced state from which declining is permissible.

Whether that is satisfying is contested. Egan's diagnosis, quoted in the source, is that the trouble lies in CDT's requirement to "hold fixed the agent's unconditional credences in dependency hypotheses." My reading is that deliberational CDT partially concedes the point. It holds credences fixed *at the moment of choice*, but lets them move *during deliberation*.

### 6.4 The Adversarial Offer: an exploitation argument

The source quotes Oesterheld and Conitzer's case. A seller offers two boxes at \$1 each, and the buyer may buy one or none. Yesterday the seller put \$3 in each box she predicted the buyer would *not* acquire. Her prediction is 75% accurate.

Here is a short argument that *any* version of CDT buys, including the deliberational version. My presentation fills out the source's sketch.

Under every possible prediction, at least one box contains \$3:

- prediction "box 1" means box 2 is full;
- prediction "box 2" means box 1 is full;
- prediction "none" means both are full.

So for any credence over predictions,

$$
\mathbb{E}[\text{box}_1] + \mathbb{E}[\text{box}_2] \ge 3 \quad\Longrightarrow\quad \max_i \mathbb{E}[\text{box}_i] \ge 1.5 > 1 .
$$

"Buy nothing" (value $0$) is therefore *never* a causal-expected-utility maximizer, at any credence. That means it cannot be in the support of any deliberational equilibrium. Ratifiability does not help either: conditional on deciding "none," each box is full with probability $0.75 + 0.125 = 0.875$, so buying looks even better.

Yet whichever box the buyer actually takes, the seller predicted that box with probability $0.75$, so it contains \$3 with probability only $0.25$. The buyer's expected *realized* payoff is $0.75 - 1 = -0.25$ per round. The seller profits reliably.

This is the strongest form of the "CDT loses money" critique in the source, and it connects to their claim that CDT agents are vulnerable to diachronic Dutch books. A CDT defender, such as Joyce in his reply cited by the source, must argue that evaluating an act by the expected payoff *of agents who perform it* already smuggles in the evidential reasoning CDT rejects.

## 7. An operational procedure (my proposal)

The source leaves the algorithm open. The following procedure is my synthesis of the dependency-hypothesis and deliberational traditions. It is precise enough to apply to new cases.

1. **Model the decision.** List acts $\mathcal{A}$, outcomes $O_j$, and utilities $D$. If commitments or policies are genuinely available *as acts*, for instance binding yourself before a prediction is made, include them. CDT evaluates whatever is actually choosable at the time of choice.
2. **Build a causal model.** Identify the variables causally upstream of, or causally independent of, the act. These include predictions already made, fixed traits, and hidden states. Their joint configurations are the dependency hypotheses $K$. If the causal structure itself is uncertain, let $K$ range over structures as well.
3. **Assign credences.** Set $P(K)$ from current evidence. That evidence may include what you know about your own dispositions, but you never condition on the act itself.
4. **Compute** $U(A) = \sum_K P(K)\sum_j P(O_j\mid A, K) D(O_j)$ for each act.
5. **Check dominance.** If some act is best under every $K$, choose it and stop. This settles the Bathsheba, Newcomb, and twin prisoner's dilemma cases.
6. **Check ratifiability.** If the best act at step 4 is ratifiable, choose it.
7. **Deliberate to equilibrium.** Otherwise, iterate. Shift credence toward higher-$U$ acts, update $P(K)$ on your changing inclinations, and repeat until reaching $\mathbf{x}^*$. Any act in the support of $\mathbf{x}^*$ is permissible. If an external randomizer is available, and the predictor cannot predict its outcome, choosing the mixture $\mathbf{x}^*$ is itself an option worth modeling at step 1.
8. **Report ties honestly.** In unstable cases CDT typically yields *permissibility*, not a unique verdict.

**A worked application: medical Newcomb.** A gene causes both a taste for smoking and cancer, and smoking itself is harmless. Step 2 makes the gene the dependency hypothesis. Step 5 shows that smoking dominates, since the pleasure comes at no causal cost, so CDT recommends smoking. The difference from Newcomb lies not in CDT's verdict but in how intuitive that verdict feels. Our intuitions about gene-mediated correlations usually agree with CDT. Our intuitions about predictor-mediated correlations often do not.

## 8. Assessment

CDT's core idea is compelling. A choice is a means of changing the world, so it should be evaluated by the changes it makes. The formula $U(A)=\sum_K P(K)\,\mathbb{E}[D\mid A,K]$ makes that idea exact. In the dependency-hypothesis or interventionist reading, it is as computable as the agent's causal model.

The pressure points identified in the source fall into two families:

- **Prediction cases** (Newcomb, the twin prisoner's dilemma). CDT's verdicts follow from dominance and are stable. The dispute there is about whether causal efficacy is really what rationality tracks when the environment rewards dispositions.
- **Instability cases** (Death in Damascus, the Psychopath Button, the Adversarial Offer). CDT's recommendation depends on credences that the recommendation itself disturbs. Ratifiability and deliberational equilibrium supply a principled fix in many of these cases, softening Egan's examples into permissible indifference. The Adversarial Offer shows that the fix has limits: no amount of equilibrium-seeking makes declining the bet a CDT-optimal act.

## 9. Conclusion

Causal decision theory replaces conditional probabilities with counterfactual or interventional ones. It ranks acts by $\sum_j P(A\mathbin{\square\!\!\to}O_j)D(O_j)$, operationalized as an average over act-independent dependency hypotheses weighted by their unconditional credences.

The theory agrees with evidential decision theory whenever acts carry no information about the causal background. It diverges, sometimes impressively (Bathsheba, smoking genes) and sometimes controversially (Newcomb), when they do.

The source rightly flags that CDT does not specify how counterfactual probabilities are to be computed. I have argued that causal models fill that gap reasonably well. Deliberational dynamics address the instability problems, at the cost of producing permissions rather than unique verdicts. What remains genuinely open is whether an agent who is predictably exploitable, like the CDT buyer in the Adversarial Offer, can still be called fully rational. That question is where the current debate stands.

## References

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116(1).
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*.
- Joyce, J. (2012). "Regret and instability in causal decision theory." *Synthese* 187.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Phil. Review* 85; (1981) "Causal decision theory." *AJP* 59.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Phil. Quarterly* 71(4).
- Reference article: Wikipedia, "Causal decision theory," revision 1381555528.