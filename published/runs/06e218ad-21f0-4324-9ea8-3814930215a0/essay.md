# Causal Decision Theory: Choosing What You Can Bring About

## 1. The guiding idea

Causal decision theory (CDT) answers a simple question: *which action should a rational agent take?* Its answer is that you should choose the action whose **causal consequences** are best in expectation. The words "causal consequences" do almost all of the work. The theory is easiest to understand by contrast with its main rival, evidential decision theory (EDT). EDT recommends the act that would be the best *news* to receive about yourself, meaning the act whose performance would most raise your expectation of a good outcome.

The two theories usually agree. Learning that you ate a good apple is good news, and eating a good apple also causes happiness. They come apart only when an act is *correlated* with good or bad outcomes without *causing* them. That happens when some common cause, a predictor, or a twin produces the correlation. Most of the philosophical action happens in those cases, and so does most of this essay.

Before starting, a note on sources. The reference article I draw on is the Wikipedia entry on CDT. It states the Gibbard–Harper formula, Lewis's triviality point, the Bathsheba and Newcomb cases, the "vagueness" and "counterexample" criticisms, and the Adversarial Offer and Psychopath Button cases. Several other things are my own reconstruction or proposal, and I flag them as such:

- the dependency-hypothesis and interventionist formulations;
- the worked numbers;
- the step-by-step procedure in §6;
- the treatment of deliberational equilibrium.

## 2. The informal picture

The source begins with fruit. Suppose eating an apple causes happiness and eating an orange causes sadness. Then eat the apple. Now complicate the case. The apple may be good or bad, and you do not know which. You cannot simply read off "the" causal effect of eating it. Instead you form an expectation from three ingredients:

1. how likely the apple is to be good;
2. how good eating a good apple is;
3. how bad eating a bad apple is.

With credence $p$ that the apple is good, utility $u_g$ for a good apple and $u_b$ for a bad one, the causal expected value of eating is $p\,u_g + (1-p)\,u_b$. You compare that number with the value of the alternatives.

Notice something easy to miss. Whether the apple is good is not affected by your choice to eat it. That is why $p$ is the *same* number whichever act you consider. CDT's characteristic move, stated generally, is to hold fixed your beliefs about things you cannot influence.

## 3. Formal statements

### 3.1 Gibbard and Harper: probabilities of counterfactuals

Gibbard and Harper (1981) defined the causal utility of an act $A$ as

$$
U(A) = \sum_j P(A \mathbin{\square\!\!\rightarrow} O_j)\, D(O_j).
$$

Here $\{O_j\}$ is a partition of outcomes and $D$ is desirability. The term $P(A \mathbin{\square\!\!\rightarrow} O_j)$ is your credence in the **counterfactual conditional** "if I were to do $A$, $O_j$ would obtain."

The source glosses this as the probability that "$A$ necessarily implies $O_j$." That is loose. The conditional is a counterfactual, not a strict (necessary) implication. It can be true even if $A$ does not logically or metaphysically necessitate $O_j$, as long as $O_j$ holds in the relevantly closest $A$-worlds.

Compare EDT's value function:

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j).
$$

The two theories differ in exactly one place: the probability of a conditional versus a conditional probability.

### 3.2 Why the two probabilities differ

**The source's claim.** If $P(A \mathbin{\square\!\!\rightarrow} O) = P(O\mid A)$ held in general, CDT would collapse into EDT. Lewis (1976) proved that no conditional connective can satisfy this identity across a class of probability functions closed under conditionalisation, except for trivial functions.

Gibbard and Harper identify when the identity *does* hold. Assume:

- **(Centering)** $A \wedge (A \mathbin{\square\!\!\rightarrow} O)$ is equivalent to $A \wedge O$. If you actually do $A$, then "$A$ would yield $O$" is true just in case $O$ is.
- **(Independence)** The act $A$ is probabilistically independent of the counterfactual $A \mathbin{\square\!\!\rightarrow} O$.

Then the derivation is short:

$$
P(O\mid A) = \frac{P(A\wedge O)}{P(A)} = \frac{P(A \wedge (A\mathbin{\square\!\!\rightarrow}O))}{P(A)} = P(A\mathbin{\square\!\!\rightarrow} O).
$$

The source also mentions conditional excluded middle: for every $A$ and $O$, either $A\mathbin{\square\!\!\rightarrow}O$ or $A\mathbin{\square\!\!\rightarrow}\neg O$. This principle is controversial. It ensures the counterfactuals $\{A\mathbin{\square\!\!\rightarrow} O_j\}_j$ form a partition, so the weights in $U(A)$ sum to one.

The derivation gives a diagnostic. **CDT and EDT disagree exactly when your choice is evidence about what your choice would cause.** That happens when something correlates the act with the "causal setup" of the world without the act producing that setup.

### 3.3 Dependency hypotheses (a reformulation)

**My reconstruction from the wider literature, not stated in the source.** Many people find counterfactuals awkward to assign credences to. A common reformulation, due to Lewis (1981) and Skyrms, introduces a partition $\{K_i\}$ of **dependency hypotheses**. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on acts, and it is outside the agent's influence. Then

$$
U(A) = \sum_i P(K_i) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j).
$$

Two features matter.

- The weights are the **unconditional** credences $P(K_i)$, not $P(K_i\mid A)$.
- Within each hypothesis, the act's effect is given by $P(O_j\mid A\wedge K_i)$. This is legitimate because, once the causal structure is fixed, conditioning on $A$ tracks only its downstream effects.

EDT, by contrast, weights by $P(K_i\mid A)$. Every disagreement between the two theories comes from the gap between these weights.

### 3.4 An interventionist version

**Also my addition.** If you represent the problem as a causal Bayesian network, the $do$-operator gives a third equivalent formulation:

$$
U(A) = \sum_j P(O_j \mid do(A))\, D(O_j).
$$

Here $do(A)$ cuts the arrows *into* the act node and keeps everything upstream at its prior distribution. Suppose $Z$ is the set of the act's causal parents, or more generally a set of variables satisfying Pearl's back-door criterion. Then

$$
P(O\mid do(A)) = \sum_z P(z)\,P(O\mid A,z).
$$

This is the dependency-hypothesis formula with $z$ playing the role of $K$. For practical purposes, this is the clearest way to compute CDT: draw the graph, intervene on your act, and propagate.

## 4. The classic divergence cases

### 4.1 King David and Bathsheba (from the source)

Gibbard and Harper's example works as follows. Kings are either charismatic ($C$) or not. Charisma is fixed by genes and upbringing. Charismatic kings tend to act justly. Uncharismatic kings tend to act unjustly and also tend to suffer successful revolts, because of their "sneaky, ignoble bearing" and not because of their unjust acts. David must decide whether to send for Bathsheba ($S$), which is unjust.

**My numbers.** Let the value of Bathsheba be $b>0$ and the cost of revolt be $r>0$. Let revolt occur with probability $\rho_C$ if David is charismatic and $\rho_{\bar C}$ if not, with $\rho_{\bar C} > \rho_C$. Sending does not affect revolt. Then:

$$
U(S) - U(\neg S) = b + \big[-r\,(P(C)\rho_C + P(\bar C)\rho_{\bar C})\big] - \big[-r\,(P(C)\rho_C + P(\bar C)\rho_{\bar C})\big] = b > 0.
$$

The revolt terms cancel because $P(C)$ is the same under both acts. CDT says: send for her.

EDT instead uses $P(\bar C\mid S) > P(\bar C\mid\neg S)$:

$$
V(S) - V(\neg S) = b - r(\rho_{\bar C}-\rho_C)\big[P(\bar C\mid S) - P(\bar C\mid \neg S)\big].
$$

This can be negative. EDT then counsels abstaining, as though abstention could make David charismatic. Most people find CDT's verdict correct here. The source reports that philosophers forced to choose between the two theories generally prefer CDT. This is the "medical Newcomb" pattern: a symptom of a bad condition is not a cause of it, so avoiding the symptom does not help.

### 4.2 Newcomb's problem

There are two boxes. Box A is transparent and holds \$1,000. Box B is opaque. A predictor who is 99% reliable put \$1,000,000 in B if and only if it predicted you would take only B.

**CDT computation (mine).** Let $K_1$ be "B is full" and $K_2$ be "B is empty," with credence $p = P(K_1)$. The contents are already fixed.

$$
U(\text{one}) = 10^6 p,\qquad U(\text{two}) = 10^6 p + 10^3.
$$

Two-boxing wins by exactly \$1,000 for *every* value of $p$. It causally dominates.

**EDT computation.**

$$
V(\text{one}) = 0.99\cdot 10^6 = 990{,}000,\qquad V(\text{two}) = 0.01 \cdot 10^6 + 10^3 = 11{,}000.
$$

So the source's summary is right: CDT two-boxes because the prediction is already made, and EDT one-boxes because one-boxing is strong evidence of a full box. The source counts Newcomb as an "alleged counterexample." CDT agents predictably leave with \$1,000 while one-boxers leave rich. Philosophers remain divided on the case.

The causalist reply deserves a fair statement. The predictor rewards a *disposition* that the predictor detected earlier. At the moment of choice, the money is either in the box or it is not. Whatever is in B, taking A as well gets you \$1,000 more. On this view, one-boxers are rich because of who they were when the prediction was made, not because of what they do now. The common slogan "if you're so smart, why ain't you rich?" is answered with "because the game rewards irrationality."

### 4.3 The twin Prisoner's Dilemma

**From the source, following Lewis (1979).** You play a one-shot Prisoner's Dilemma against a near-copy of yourself. Your choices are highly correlated, but neither choice causes the other. CDT notes that defection dominates causally and defects. EDT notes that your cooperation is evidence of your twin's cooperation and cooperates. Lewis's point is that this is simply Newcomb's problem in another form. The twin's choice plays the role of the prediction.

## 5. Instability, ratifiability, and Egan's challenge

### 5.1 Death in Damascus

Death predicts where you will be tomorrow and waits there. You can stay in Damascus or flee to Aleppo. Suppose Death is reliable.

**My formalization.** Let $q$ be your current credence that you will go to Aleppo. Because Death tracks your choice, your credence that Death will be in Aleppo is roughly $q$. Let survival be worth 1 and death worth 0. Then:

$$
U(\text{Aleppo}) = 1-q, \qquad U(\text{Damascus}) = q.
$$

If you lean toward Aleppo ($q>1/2$), Damascus looks better. Leaning toward Damascus makes Aleppo look better. No pure act is stable.

The source puts this by saying a CDT agent is "unable to process the correlation." I would put it more precisely. CDT's recommendation *depends on the agent's credences about its own act*, and those credences shift as deliberation proceeds. The unconditional weights $P(K)$ in §3.3 are not fixed inputs in such cases. They move with the agent's own leanings.

### 5.2 Ratifiability (background, not in the source)

Jeffrey and Harper proposed that a rational choice should be **ratifiable**. An act $A$ is ratifiable if, once you assume you will perform it, no alternative looks better:

$$
\sum_i P(K_i \mid A)\,u(B, K_i) \le \sum_i P(K_i \mid A)\,u(A,K_i) \quad \text{for all } B.
$$

Here $u(A,K) = \sum_j P(O_j\mid A\wedge K)D(O_j)$. In Death in Damascus no pure act is ratifiable. The standard way out, developed by Skyrms, Arntzenius and Joyce, is **deliberational dynamics**. Treat deliberation as a process that updates $q$ toward whichever act currently has higher causal utility, and choose at a fixed point. In this example the fixed point is $q=1/2$, where the agent is indifferent and in effect randomizes.

### 5.3 The Psychopath Button

**From the source (Egan 2007).** Paul could press a button that kills all psychopaths. He would prefer a world without psychopaths, but he strongly prefers living among psychopaths to dying. He is confident that only a psychopath would press the button. Egan reports that "pretty much everyone" thinks Paul should not press, yet CDT endorses pressing.

**My numbers.** Take these utilities: a psychopath-free world is +10, dying is −100, and the status quo is 0. Paul's prior that he is a psychopath is 0.05. Naive CDT then gives

$$
U(\text{press}) = 0.95(10) + 0.05(-100) = 4.5 > 0 = U(\text{refrain}),
$$

so CDT says press. But $P(\text{psycho}\mid\text{press})$ is high. If Paul decides to press, his updated causal utility for pressing becomes very negative. Pressing is therefore not ratifiable.

Egan diagnoses the problem as follows. The intuitive rule is "do what you expect to bring about the best results." CDT's formal rule is "maximize expected value *holding fixed your initial credences in dependency hypotheses*." The second rule ignores what your choice would reveal about which causal hypothesis holds.

**The deliberational reply (my worked version).** Suppose Paul's credence in being a psychopath depends on his inclination $q$ to press, as $s(q) = 0.01 + 0.89q$. Pressing has nonnegative causal utility exactly when $10(1-s) - 100s \ge 0$, that is, when $s \le 1/11$. Solving $0.01 + 0.89q = 1/11$ gives $q^\ast \approx 0.091$.

At the equilibrium, Paul is about 91% inclined not to press and is indifferent between the acts. Note what deliberation does here. It moves Paul *away* from the naive "press" verdict toward a strong lean against pressing. Joyce argues that CDT, properly applied, already allows "information about what one is inclined or likely to do" to serve as evidence. The source reports this defense. Critics answer that ending up indifferent, and pressing about 9% of the time, still gets the case wrong.

### 5.4 Money pumps: the Adversarial Offer

**From the source (Oesterheld & Conitzer 2021).** Two boxes are for sale at \$1 each. You may buy one or neither. Yesterday the seller put \$3 in every box she predicted you would *not* buy. Her prediction is accurate with probability 0.75.

The CDT argument runs as follows. Whatever the seller predicted, at least one box contains \$3:

- If she predicted "neither," both boxes contain \$3.
- If she predicted "box 1," box 2 contains \$3.
- If she predicted "box 2," box 1 contains \$3.

So the expected contents of the two boxes sum to at least \$3. That means at least one box has expected contents of at least \$1.50, which exceeds its price. CDT therefore buys a box.

**The ex-post view (my calculation).** Given that you buy box $i$, the seller predicted that purchase with probability 0.75, so box $i$ is empty with probability 0.75. Your expected net is $0.25(3) - 1 = -\$0.25$. Assuming the seller is calibrated, she profits from every CDT buyer.

Oesterheld and Conitzer present this, together with diachronic Dutch-book arguments, as showing that CDT agents can be exploited for money. Related cases are Spencer's argument that CDT forgoes guaranteed payoffs, and Joyce's reply. One defense is that CDT should not be judged by its average performance across worlds where the predictor already knows your choice. Another is that deliberational CDT would reach a mixed equilibrium and lower its valuation of the boxes. It is worth checking where the second defense leads. If the buyer randomizes between the boxes and the seller's accuracy is defined relative to the realized choice, the calculation changes. How much it changes depends on whether the seller can predict the outcome of the randomizing device. That is exactly the kind of underspecification discussed next.

## 6. The open question: where do the counterfactual probabilities come from?

**The source's claim.** CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." Lewis's proposal is **imaging**. To evaluate $P(A\mathbin{\square\!\!\rightarrow}O)$, move each world $w$'s probability to the nearest $A$-world $w_A$:

$$
P^A(w') = \sum_{w:\, w_A = w'} P(w), \qquad P(A\mathbin{\square\!\!\rightarrow} O) = P^A(O).
$$

Shaffer's objection, reported by the source, is that imaging needs a similarity metric and a known "nearest $A$-world" for each world. Our beliefs about those are themselves uncertain conditionals, which threatens a regress.

**My operational proposal.** I think a workable and defensible procedure is available. It turns the counterfactual into two more tractable ingredients: a causal model and credences over causal models. To decide an unfamiliar case:

1. **Fix the act set** $\mathcal A$, including mixed or randomized acts if randomization is genuinely available and opaque to any predictor.
2. **Identify the act-independent background.** List the variables, or dependency hypotheses $K$, that are causally upstream of or independent of your choice. These are the predictor's past prediction, your genes, the apple's quality, the contents of the box, and the like. Uncertainty about the structure itself belongs here too, as a mixture over graphs. This turns imaging's regress into ordinary first-order uncertainty over models.
3. **Specify within-hypothesis causal chances** $P(O\mid do(A), K)$. These describe what your act would produce if hypothesis $K$ were true.
4. **Compute** $U(A) = \sum_K P(K)\,P(O\mid do(A),K)\,D(O)$.
5. **Check stability.** If the credences $P(K)$ depend on what you expect to choose, iterate. Update $P(K)$ given your current inclination $q$, recompute $U$, and shift $q$ toward the better act. Choose at a fixed point $q^\ast$. If an act is ratifiable at its own fixed point, that act is the recommendation.

Step 5 is where I go beyond what the source commits to. Without it, "unconditional credence" is ambiguous. It could mean credence *before* deliberation, which yields Egan's unratifiable pressing, or credence *at the end* of deliberation, which yields Joyce's equilibrium. I favor the end-of-deliberation reading for one reason. A rational agent's final credences should already reflect everything it knows, including what it is about to do. Freezing earlier credences would mean deliberately ignoring evidence.

The proposal leaves one real choice point. In some games there are several equilibria, and the procedure does not say which to pick. My tentative suggestion is to prefer equilibria reachable from the agent's actual starting credences under the dynamics. That adds path-dependence, which some will find unattractive.

## 7. Acts versus policies

The source discusses CDT as evaluating individual acts at the moment of choice. **This section is my commentary.** There is a much-discussed refinement involving binding, which Meacham (2010) treats among the cited works.

Evaluate the Newcomb problem *before* the predictor makes its prediction, from the standpoint of an agent who can commit to a policy. Adopting "one-box" now causally influences the prediction, and so it causally influences the box's contents. CDT applied at that earlier time therefore recommends committing to one-box, if commitment is possible.

So CDT is not hostile to good outcomes in Newcomb-like settings. Its verdicts depend on *when* the evaluation is made and *what is still causally open* at that point. A CDT agent who expects to face predictors has instrumental reason to become, or to bind itself to be, the kind of agent who one-boxes. Critics take this as an admission that CDT's act-level verdict is wrong. Defenders take it as the correct account of the value of precommitment. In either case, here is a practical rule for applying CDT: **identify the decision point, then hold fixed exactly what is causally fixed at that point.**

## 8. Summary of how to use CDT on a new case

- **Evaluate acts by what they bring about.** Weight each possible causal setup by your credence in it. Do not boost or discount a setup because your act would be evidence for it.
- **Common causes are not levers.** Symptoms, revealed dispositions, and correlated twins all fall under this. Bathsheba, medical Newcomb cases, and the twin Prisoner's Dilemma are all decided by this principle.
- **Past predictions are fixed.** In Newcomb-type problems CDT follows causal dominance: two-box, defect against the twin, buy in the Adversarial Offer.
- **When credences depend on your own choice**, as in Death in Damascus or the Psychopath Button, run deliberation to equilibrium and check ratifiability. Expect mixed or indifferent verdicts.
- **Earlier commitment points are causally different decisions** and may warrant different, cooperative policies.

## 9. Conclusion

CDT rests on a compelling thought: rational choice is about making a difference, not about receiving good news. Its formal core is a single substitution. It replaces EDT's $P(O\mid A)$ with $P(A\mathbin{\square\!\!\rightarrow}O)$, or equivalently with $\sum_K P(K)P(O\mid do(A),K)$. That substitution delivers clear verdicts wherever correlations arise from common causes. It also explains why CDT and EDT coincide whenever acts are independent of the causal hypotheses.

The source correctly identifies two pressure points. First, the counterfactual probabilities are underdetermined by the theory alone. Second, predictor cases (Newcomb, Death in Damascus, the Adversarial Offer, the Psychopath Button) generate verdicts that many find unacceptable or exploitable. I have argued that the first problem is largely answered by modelling causal structure explicitly and placing uncertainty over models. I have also argued that the second problem is partly softened, though not dissolved, by letting the agent's credences settle into a deliberational equilibrium and by distinguishing act evaluation from policy evaluation. Whether what remains is a refutation of CDT, or simply the cost of declining to treat evidence about yourself as power over the world, is still one of decision theory's live disagreements.

---

**References (selected)**

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116(1).
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*.
- Joyce, J. (2012). "Regret and instability in causal decision theory." *Synthese* 187.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Phil. Review* 85; (1979) "Prisoners' dilemma is a Newcomb problem"; (1981) "Causal decision theory." *AJP* 59.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Phil. Quarterly* 71(4).
- Shaffer, M. (2009). "Decision theory, intelligent planning and counterfactuals." *Minds and Machines* 19.
- Wikipedia contributors, "Causal decision theory," rev. 1381555528 (CC BY-SA 4.0).