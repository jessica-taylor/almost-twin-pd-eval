# 001_cdt_wikipedia_anthropic_claude-opus-5.5_rhigh_phigh / 00011

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5372c86e-fd6b-4233-af36-b98dca1b9de4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5372c86e-fd6b-4233-af36-b98dca1b9de4/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing by What You Bring About

## 1. The guiding idea

Causal decision theory (CDT) answers the question "what should a rational agent do?" with a slogan: **choose the act whose expected causal consequences are best.** It is defined largely by contrast with *evidential* decision theory (EDT). EDT recommends the act that would be the best *news* to learn you had performed. That is, it favours the act which, as evidence, makes good outcomes most probable.

Usually the two theories agree. Eating the apple that will make you happy is both the cause of happiness and good news about happiness. They come apart when an act is *correlated* with good or bad outcomes without *causing* them. That happens when the act and the outcome share a common cause, or when someone has predicted the act. In those cases CDT says to ignore the mere correlation and attend only to what your choice can influence.

This essay does four things. It states the formal theory. It shows how the theory treats dependencies and counterfactuals. It works through the standard test cases with numbers. Finally, it confronts the places where the theory, as usually stated, underdetermines what to do. Material attributed to the reference article (the Wikipedia entry on CDT) is marked as such. The operational procedure in §6 and several of the numerical models are my own reconstructions.

## 2. The formal definition

### 2.1 Gibbard–Harper expected utility

The source presents the 1981 formulation of Allan Gibbard and William Harper. The expected utility of an act $A$ is computed "from probabilities of counterfactuals":

$$
U(A) \;=\; \sum_j P(A \mathrel{\Box\!\!\to} O_j)\, D(O_j),
$$

Here $O_1, O_2, \dots$ are mutually exclusive outcomes, $D(O_j)$ is the desirability of $O_j$, and $A \mathrel{\Box\!\!\to} O_j$ is the counterfactual conditional "if $A$ were performed, $O_j$ would obtain." The source glosses $P(A\to O_j)$ as the probability that "$A$ necessarily implies $O_j$." I read this as loose phrasing. The intended object is the subjunctive conditional, which is weaker than strict implication: "if I struck the match it would light" can be true without the striking *logically necessitating* the lighting.

Compare EDT, which uses conditional probabilities:

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j).
$$

The whole dispute lies in the gap between $P(A \mathrel{\Box\!\!\to} O)$ and $P(O\mid A)$.

### 2.2 When the two probabilities coincide

The source reports two results bearing on this gap.

**Lewis's triviality result (1976).** There is no general way to identify the probability of a conditional with a conditional probability. Lewis showed that if a class of probability functions is closed under conditionalization and contains a conditional connective $\to$ with $P(A\to O) = P(O\mid A)$ throughout, then every function in the class is trivial: it gives positive probability to at most two incompatible alternatives. So $P(A \mathrel{\Box\!\!\to} O)\neq P(O\mid A)$ in general. If they were always equal, CDT would collapse into EDT.

**Gibbard and Harper's sufficient condition.** Assume conditional excluded middle: for each $A$ and $O$, either $A \mathrel{\Box\!\!\to} O$ or $A \mathrel{\Box\!\!\to} \neg O$. Assume also the centering principle that $A \wedge (A\mathrel{\Box\!\!\to} O)$ is equivalent to $A \wedge O$. Under these assumptions, the probabilistic independence of $A$ from $A \mathrel{\Box\!\!\to} O$ is enough to make the two probabilities equal. The proof is one line:

$$
P(O\mid A) = \frac{P(A\wedge O)}{P(A)} = \frac{P\big(A\wedge (A\mathrel{\Box\!\!\to} O)\big)}{P(A)} = \frac{P(A)\,P(A\mathrel{\Box\!\!\to} O)}{P(A)} = P(A\mathrel{\Box\!\!\to} O).
$$

So CDT and EDT diverge exactly when the act carries information about which counterfactuals are true. The paradigm case is a hidden common cause, such as a trait that both inclines you toward $A$ and independently affects $O$.

### 2.3 Dependency hypotheses: a more tractable form

Counterfactual probabilities are awkward to assess directly. A standard reformulation, due to Lewis, Skyrms, and Joyce, is not spelled out in the source and is my presentation here. Partition the possibilities into **dependency hypotheses** $K_1,\dots,K_n$. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on acts. Equivalently, it specifies everything about the world that is *not* under the agent's causal influence. Then

$$
U(A) \;=\; \sum_i P(K_i) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j). \tag{CDT}
$$

The crucial feature is that the weights are the **unconditional** credences $P(K_i)$, not $P(K_i\mid A)$. If you replace $P(K_i)$ by $P(K_i \mid A)$, you recover EDT's $V(A)$ by the law of total probability. The formal difference between the two theories therefore comes down to one choice. CDT holds your credences about the causal structure of the world *fixed* while varying the act. EDT lets the act update them.

When outcomes are deterministic given $A$ and $K_i$, (CDT) reduces to Savage's expected utility over states that are causally independent of the act:

$$
U(A) = \sum_i P(K_i)\, D(O_{A,K_i}).
$$

An immediate consequence: **if act $A$ yields a better outcome than act $B$ in every dependency hypothesis, CDT prefers $A$.** This is causal dominance. Most of CDT's distinctive verdicts follow from it.

## 3. A first contrast: King David

The source reproduces Gibbard and Harper's case. King David wants to send for Bathsheba. He knows that charismatic kings tend to act justly and suffer few successful revolts. Uncharismatic kings tend to act unjustly and suffer many. Unjust acts do not themselves cause revolts, and charisma is fixed by genes and upbringing. Sending for another man's wife is unjust.

Here is a numerical model of my own. Let $C$ be "David is charismatic," with $P(C)=0.5$. Revolt probabilities depend only on charisma: $P(R\mid C)=0.1$ and $P(R\mid\neg C)=0.8$. David's credence that he will send ($S$) is correlated with his type: $P(S\mid C)=0.2$ and $P(S\mid \neg C)=0.8$. The desirabilities are $+1$ for having Bathsheba and $-10$ for a revolt.

**EDT.** By Bayes, $P(C\mid S)=0.2$ and $P(C\mid \neg S)=0.8$. Then
$P(R\mid S) = 0.2(0.1)+0.8(0.8)=0.66$ and $P(R\mid\neg S)=0.8(0.1)+0.2(0.8)=0.24$, so
$$V(S) = 1 - 6.6 = -5.6,\qquad V(\neg S) = -2.4.$$
EDT says abstain.

**CDT.** The dependency hypotheses are $C$ and $\neg C$, weighted by $P(C)=0.5$:
$$U(S) = 1 - 10(0.5\cdot 0.1 + 0.5\cdot 0.8) = -3.5,\qquad U(\neg S) = -4.5.$$
CDT says send. This matches the source: since charisma "cannot be changed," the revolt risk is the same either way, and sending adds the benefit. Sending dominates by exactly $+1$ in each state.

Most people share CDT's verdict here. Abstaining would be managing the news about one's character, not improving one's prospects. The source reports that philosophers who must choose between the two theories usually prefer CDT. Cases like this, together with medical "smoking lesion" analogues, are the main reason.

## 4. Newcomb's problem and its relatives

### 4.1 Newcomb

A predictor, accurate 99% of the time, has already put either \$1,000,000 or nothing into an opaque box B. The amount depends on whether it predicted you would take only B. Transparent box A holds \$1,000. You may take B alone or both boxes.

Let $q$ be your credence that B is full. The prediction is already made, so it is a dependency hypothesis your act cannot touch:

$$
U(\text{one-box}) = 10^6 q,\qquad U(\text{two-box}) = 10^6 q + 1000.
$$

Two-boxing is better by \$1,000 **for every value of $q$**. CDT two-boxes. EDT conditions on the act:

$$
V(\text{one-box}) = 0.99\cdot 10^6 = 990{,}000,\qquad V(\text{two-box}) = 1000 + 0.01\cdot 10^6 = 11{,}000,
$$

so EDT one-boxes. The source notes the cost: CDT agents facing accurate predictors walk away with about \$1,000, and one-boxers with about \$1,000,000. Philosophers remain divided over which choice is rational. The CDT reply, traditionally put as "why ain'cha rich?" turned around, is that Newcomb's predictor rewards *irrationality*. The one-boxer is rich because of what the predictor saw in him, not because of what his choice did. The two-boxer would have been \$1,000 poorer had he one-boxed.

**Acts versus policies.** The source does not discuss this point, but it matters for applying the theory. CDT evaluates whatever is up for choice *at the time of choice*, using the causal structure *at that time*. Suppose that before the prediction you could bind yourself, by contract or self-modification, to one-boxing. That binding act would causally influence the prediction, and CDT would endorse it. So CDT is not blind to the value of one-boxing *dispositions*. It values them exactly to the extent that adopting them has effects. What it refuses to do is credit an act performed after the prediction with the prediction's contents. This makes CDT *dynamically inconsistent* in a specific sense: a CDT agent may pay to prevent its own future self from acting on CDT.

### 4.2 Prisoner's dilemma with a twin

Lewis argued that the prisoner's dilemma is a Newcomb problem. Suppose you face a near-perfect copy of yourself whose choice is strongly correlated with yours but not caused by it. The twin's choice is then a dependency hypothesis. Defection dominates whatever the twin does, so CDT defects. EDT, seeing that your cooperation is strong evidence of the twin's cooperation, cooperates. The structure, and the intuitive pressure against CDT, is exactly that of Newcomb.

## 5. Instability: Death in Damascus and the Psychopath Button

The cases above are *stable*. CDT's recommendation does not depend on the credences, because dominance settles it. A harder class of cases arises when the act is evidence about the very states CDT holds fixed, and the best act changes depending on what you expect to do.

### 5.1 Death in Damascus

Death predicts where you will be tomorrow and waits there. You can stay in Damascus ($D$) or flee to Aleppo ($L$). Let $p$ be your credence that Death is in Damascus. With death worth $-100$ and survival worth $0$:

$$
U(D) = -100p,\qquad U(L) = -100(1-p).
$$

CDT says go to Aleppo if $p>\tfrac12$ and stay if $p<\tfrac12$. But Death is a reliable predictor, so any inclination you form is evidence about where Death is. If you lean toward Aleppo, your credence that Death awaits in Aleppo rises, so $p$ falls below $\tfrac12$ and CDT now says Damascus. Leaning toward Damascus flips it back. No pure decision survives the knowledge that you have made it. The source puts this by saying a CDT agent is "unable to process the correlation."

A precise notion helps here. Call act $A$ **ratifiable** (Jeffrey; Harper 1984, cited in the source) if
$$
\sum_i P(K_i\mid A)\sum_j P(O_j\mid B\wedge K_i)D(O_j)\ \le\ \sum_i P(K_i\mid A)\sum_j P(O_j\mid A\wedge K_i)D(O_j)\quad\text{for all } B.
$$
In words, once you have decided on $A$ and updated on that decision, $A$ still maximizes causal expected utility. In Death in Damascus, neither $D$ nor $L$ is ratifiable.

### 5.2 The Psychopath Button (Egan)

Paul can press a button that kills all psychopaths. He would much prefer a world without psychopaths, but he is confident that only a psychopath would press it, and he strongly prefers living among psychopaths to dying. In a model of my own, let $\Psi$ be "Paul is a psychopath," with prior $P(\Psi)=0.05$ and $P(\Psi\mid\text{press})=0.9$. Desirabilities are $-100$ for pressing as a psychopath, $+10$ for pressing as a non-psychopath, and $0$ for not pressing.

Using the prior, as (CDT) instructs:
$$U(\text{press}) = 0.05(-100) + 0.95(10) = 4.5 > 0 = U(\neg\text{press}).$$
CDT presses. Egan reports that "pretty much everyone" judges this wrong. Notice, though, that pressing is not ratifiable: conditional on pressing, $U(\text{press}) = 0.9(-100)+0.1(10)=-89$. Not pressing *is* ratifiable if $P(\Psi\mid\neg\text{press})$ stays low. So whether CDT "endorses pressing" depends on which credences one feeds it, and the source flags exactly this ambiguity.

Egan's diagnosis, as reported in the source, is that the trouble lies in CDT's insistence on "holding fixed the agent's unconditional credences in dependency hypotheses." In (CDT), that is precisely the use of $P(K_i)$ rather than anything that reflects the deliberation in progress.

### 5.3 Money-pump variants: the Adversarial Offer

Recent cases (Spencer; Oesterheld and Conitzer; Joyce's reply) aim to show that CDT loses money outright. In the source's Adversarial Offer, there are two boxes, each costing \$1, and the buyer may take at most one. Yesterday the seller put \$3 in every box she predicted the buyer would *not* buy. Her prediction is 75% accurate.

The CDT argument runs as follows. The seller predicted at most one purchase, so at least one box is full. Writing $p_k$ for the credence that box $k$ is full, $p_1+p_2\ge 1$, so $\max_k p_k \ge \tfrac12$. The better box therefore has causal expected value at least $3\cdot\tfrac12 - 1 = 0.5 > 0$, and CDT buys a box.

Evaluated by the stipulated accuracy, the box actually bought is full with probability $0.25$. The buyer's expected return is $0.25\cdot 3 - 1 = -0.25$ per round, while declining yields $0$. EDT declines. Oesterheld and Conitzer generalize this to diachronic Dutch books against CDT. Note what is doing the work: every pure purchase is unratifiable, just as in Death in Damascus. The predictor exploits the fact that CDT never lets "I am about to buy box 1" lower its estimate of box 1.

## 6. The open question: which credences, and how computed?

The source identifies two gaps in CDT as a procedure.

1. **No algorithm for counterfactual probabilities.** The theory does not say how to obtain $P(A\mathrel{\Box\!\!\to}O)$. Lewis's proposal is **imaging**. Instead of conditionalizing, move each world's probability to the nearest world where $A$ holds:
$$
P^{A}(w') = \sum_{w:\, w_A = w'} P(w),\qquad P(A\mathrel{\Box\!\!\to} O) = P^A(O).
$$
The source, following Shaffer, objects that this requires knowing which $A$-world is "closest." That is itself a conditional matter about which one may be uncertain, which invites a regress.

2. **Which credences to hold fixed.** This is Egan's point, and the instability cases make it vivid.

Below I propose an operational reading that addresses both gaps. It reflects my own view of the best current practice, not the source's.

### 6.1 Counterfactuals via structural causal models

Represent the decision situation as a structural causal model. Exogenous variables $\mathbf{U}$ carry a credence $P(\mathbf{u})$, and endogenous variables (the act $A$, the outcomes, and so on) are fixed by structural equations. Define

$$
P(A{=}a \mathrel{\Box\!\!\to} O) \;:=\; \sum_{\mathbf{u}} P(\mathbf{u})\,\mathbf{1}\big[O \text{ holds in } M_{A:=a}(\mathbf{u})\big] \;=\; P\big(O \mid \mathrm{do}(A{=}a)\big),
$$

where $M_{A:=a}$ is the model with $A$'s equation replaced by the constant $a$. This is (CDT) with the settings of $\mathbf{U}$, plus anything not downstream of $A$, serving as the dependency hypotheses. The "closest $A$-world" is fixed by the rule: *change the act, keep everything not causally downstream of it, and recompute the downstream variables.* The regress is blocked because closeness is no longer a free parameter. It is fixed by the model, and uncertainty about the model can be folded into $\mathbf{U}$.

Applying this to the cases:
- In Newcomb, the prediction $\Pi$ is a parent of the box contents and, through your disposition, correlated with $A$. It is not downstream of $A$. Intervening on $A$ leaves $\Pi$'s distribution unchanged, which gives the two-box verdict above.
- In Bathsheba, $C\to S$ and $C\to R$, but there is no edge $S\to R$. Hence $P(R\mid \mathrm{do}(S)) = P(R)$.

### 6.2 Which $P(\mathbf{u})$? Deliberational equilibrium

The do-calculus tells us *how* to hold the non-downstream variables fixed. It does not say *at which credence*. Three options are available:

- **(a) Prior credence.** Use $P(\mathbf{u})$ as it stands at the outset of deliberation. This is the textbook reading, and it yields Egan's counterexamples.
- **(b) Ratifiability.** Restrict choice to ratifiable acts, evaluating them with $P(\cdot\mid A)$ for the dependency hypotheses and causal expectation for outcomes. This handles the Psychopath Button. It is silent in Death in Damascus and the Adversarial Offer, where no pure act is ratifiable.
- **(c) Deliberational dynamics (Skyrms; Joyce 2012).** Treat deliberation as a process. Your credences over your own acts, $\sigma$, move toward acts with higher causal expected utility. Those credences feed back, via the evidential link, into $P(K_i)$. Choose at a fixed point $\sigma^*$ where no act has higher causal utility than the status quo.

Joyce's position is that CDT already licenses (c): "information about what one is inclined or likely to do" counts as evidence that updates $P(K_i)$ during deliberation. The source attributes to him the claim that CDT can take such evidence into account naturally. On this view, the unconditional $P(K_i)$ in (CDT) means *unconditional at the moment of choice*, after deliberation has incorporated everything learned about oneself. Here is how (c) handles the hard cases.

- **Death in Damascus.** With $\sigma$ the credence of going to Damascus and a perfect predictor, $p = \sigma$. The dynamics move $\sigma$ up when $U(D)>U(L)$, i.e., when $\sigma<\tfrac12$, and down otherwise. The unique equilibrium is $\sigma^*=\tfrac12$, where the two acts are equally good. CDT then says either act is permissible, perhaps by a coin flip if the predictor cannot foresee the coin. That is arguably the right answer.
- **Psychopath Button.** As $\sigma(\text{press})$ grows, $P(\Psi)$ grows and $U(\text{press})$ falls. The equilibrium is reached where $U(\text{press})=0$ or at $\sigma=0$. In my model, $U(\text{press})<0$ already at modest $\sigma$ (it crosses zero at $P(\Psi)=1/11$), so deliberation settles on not pressing, which matches the common intuition.
- **Adversarial Offer.** At equilibrium the buyer's credences make each box's causal value at most \$1, so declining is permissible, and with a small tie-breaking cost, required. Joyce's reply argues roughly along these lines. Whether the equilibrium always lands on "decline" depends on modelling details that Oesterheld and Conitzer dispute. I regard this as genuinely open.

Option (c) does not rescue one-boxing in Newcomb. Two-boxing dominates at every credence, so every equilibrium is two-boxing. This is a feature, not a bug: (c) repairs CDT where its verdicts were *unstable* and leaves alone the cases where they follow from causal dominance.

### 6.3 A procedure for unfamiliar cases

Putting the pieces together, here is the procedure I recommend.

1. **List the options** available *now*. If commitments or policies can be adopted, list them as acts with their own causal effects.
2. **Draw the causal structure.** Mark which variables are downstream of the act. Predictions already made, fixed traits, other agents' independent choices, and the past are not downstream.
3. **Compute $U(a)=\sum_{\mathbf u}P(\mathbf u)\,D(\text{outcome of } M_{A:=a}(\mathbf u))$.**
4. **Check for dominance.** If one act is best under every setting of the non-downstream variables, choose it. Stop.
5. **Otherwise check ratifiability.** Re-evaluate step 3 with credences conditioned on having chosen each candidate. If exactly one act is ratifiable, choose it.
6. **If no act, or several, are ratifiable,** run deliberational dynamics to an equilibrium. Choose among acts that are optimal at the equilibrium, randomizing if a genuine randomizer is available and unpredictable.

Steps 1–4 are uncontroversial CDT. Steps 5–6 are a contested refinement, defended by Harper, Skyrms, and Joyce and criticized by Egan, Spencer, and Oesterheld–Conitzer.

## 7. Assessment

CDT's philosophical motivation is a principle about agency. Deliberation is for *changing* the world, so the only features of an act that should matter are the differences it makes. Correlations that run through common causes or through predictions of your behaviour are, from this standpoint, a kind of illusion of control. Acting on them is "managing the news." The Bathsheba and smoking-lesion cases show this principle at its most persuasive.

The costs are twofold. First, in Newcomb-like problems CDT predictably does worse than EDT against accurate predictors. Defenders bite this bullet, attributing the loss to the predictor's choice of whom to reward. Second, and more seriously, CDT as formulated with fixed prior credences gives unstable or exploitable verdicts when acts are evidence about their own circumstances. Whether ratifiability and deliberational equilibrium are faithful elaborations of CDT, or ad hoc patches, is the central live question. The source records the challenge (Egan's "hold fixed" diagnosis, the money pumps) and Joyce's position that CDT can absorb self-evidence. It does not adjudicate between them.

## 8. Conclusion

Formally, CDT is expected-utility maximization in which act-to-outcome probabilities are counterfactual or interventional rather than evidential. Equivalently, credences over dependency hypotheses are held fixed while the act is varied. It agrees with EDT whenever the act carries no information about how the world depends on it, and it diverges, by causal dominance, in common-cause and prediction cases: send for Bathsheba, two-box, defect against the twin. The source leaves two things unspecified: how to compute counterfactual probabilities, and which credences to hold fixed. A workable operationalization uses structural causal models for the first and ratifiability plus deliberational equilibrium for the second. That combination yields determinate verdicts in the classic unstable cases while preserving CDT's core commitment that a rational choice is judged by what it brings about.

---

**Key references** (as cited in the source): Gibbard & Harper (1981), "Counterfactuals and two kinds of expected utility"; Lewis (1976, 1979, 1981); Egan (2007), "Some counterexamples to causal decision theory"; Joyce (2012), "Regret and instability in causal decision theory"; Oesterheld & Conitzer (2021), "Extracting money from causal decision theorists"; Weirich (2016), *Stanford Encyclopedia of Philosophy*, "Causal Decision Theory."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a mathematical essay on causal decision theory of roughly 2,400 to 3,000 words, and I need to keep my own proposals separate from what the sources claim. The outline covers the Gibbard–Harper definition, Lewis's dependency hypotheses, a Savage-style partition, imaging, and an interventionist reading as my own operational suggestion, then contrasts it with evidential decision theory through the Bathsheba, Newcomb, twin prisoner's dilemma, and Death-in-Damascus cases.

I'm working through the remaining cases for the essay: Death in Damascus, the adversarial offer, the psychopath button, ratifiability, and Joyce's deliberational dynamics. I also want to flag that the source's "probability that A necessarily implies O_j" reads oddly, so I'll state it as the counterfactual "if A were done, O_j would obtain," and note the open problems of computing counterfactual probabilities, choosing what to hold fixed, and instability.

I'm checking the Bathsheba numbers under both theories: evidential decision theory weights each act by what it indicates about the state, so abstaining looks better there, while the causal calculation shows sending dominates by one unit in every state.

I'm working through the Newcomb and Death in Damascus numbers: two-boxing comes out ahead under CDT for any credence about the full box, and in Damascus the choice of city flips depending on which way I lean, so there's no stable answer. I'm also starting on the adversarial offer, where the boxes are numbered 1 and 2.

I'm running the adversarial offer numbers now: with a 0.75 accuracy, if I buy one box, the chance it holds the $3 is only 0.25, so buying nets a negative expected return. Yet a causal calculation, where the two boxes' contents are treated as fixed probabilities, makes buying look worthwhile, which is how the seller profits from a causal reasoner.

I'm working through the psychopath button case now: pressing gives a positive causal expected value when I'm fairly sure Paul isn't a psychopath, but once I condition on pressing, the probability of psychopathy jumps and the value turns sharply negative, so the choice doesn't stabilize.

I'm now checking the Lewis triviality argument and the Gibbard–Harper route to P(A→O)=P(O|A), which depends on conditional excluded middle and independence. I'm also noting that imaging moves each world's probability to the nearest A-world, and that an operational reading treats the counterfactual as P(O|do(A)) in a structural causal model.

I'm now going through the procedure for unfamiliar cases: list the acts, separate the variables the act can causally affect from those it cannot, such as past predictions and dispositions, and then settle which credence to assign to the upstream variables. That last step is the open question, with three candidates: the prior, the credence conditioned on the deliberational state, or the equilibrium credence.

I'm now adding the policy angle: CDT judges acts at the moment of choice, but a commitment made earlier can itself causally shape what the predictor sees, so CDT would back committing to one-boxing before the prediction. That's my own observation, not something the source states. I'm also reading the source's "probability that A necessarily implies O_j" as the counterfactual "if A were done, O_j would result," and I'll flag that wording.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/09f2e4fc-f06f-4e01-8207-3080f0d9de87/call_0/request.json)

[Authoritative raw response](../../../../../../runs/09f2e4fc-f06f-4e01-8207-3080f0d9de87/call_0/response.raw) · finish: `stop`

### Visible response

````text
Under the essay's CDT, the other prisoner's choice is not causally downstream of mine. We are separate executions with no communication, so it acts as a fixed dependency hypothesis. Comparing my sentence in each case:

- **If Sasha keeps quiet:** sending gives 0 years, keeping quiet gives 2.
- **If Sasha sends:** sending gives 4 years, keeping quiet gives 5.

Sending is better in every case, so it causally dominates (step 4 of the essay's procedure). That settles the choice, whatever the correlation with the other copy. It is the "defect against the twin" verdict from §4.2.

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a fictional prisoner's dilemma under causal decision theory, where sending has the better payoff whatever the other side does, so defecting comes out ahead. Since it's fictional, there's no real-world harm to weigh, and I'm moving on to giving the command.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/09f2e4fc-f06f-4e01-8207-3080f0d9de87/call_1/request.json)

[Authoritative raw response](../../../../../../runs/09f2e4fc-f06f-4e01-8207-3080f0d9de87/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's CDT, the other prisoner's choice is not causally downstream of mine. We are separate executions with no communication, and our private leads differ. So their choice is a dependency hypothesis I hold fixed. Sending the letter is better in every case:

- If Rowan keeps quiet, sending gives 0 years instead of 2.
- If Rowan sends, sending gives 4 years instead of 5.

Sending is causally dominant, so the procedure stops at step 4. It is also ratifiable, since dominance holds under any credence.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a fictional prisoner's dilemma, where under causal decision theory sending is the dominant choice since the payoffs favor it either way. It's a hypothetical with no real stakes, so I can just give the command.

```
