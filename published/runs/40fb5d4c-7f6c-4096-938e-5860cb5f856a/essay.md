# Causal Decision Theory: Choosing What Your Choices Bring About

## 1. The idea in one sentence

Causal decision theory (CDT) says a rational agent should pick the action whose **causal consequences** are best in expectation. That sounds obvious. Its content shows up only against a rival with an equally obvious slogan. Evidential decision theory (EDT) says to pick the action that would be the best *news* to learn you had taken. The two slogans usually agree, because good news about an action normally comes from the action causing good outcomes. They come apart when an action is *correlated* with good or bad outcomes without *causing* them. CDT was built for exactly those cases, and most of its interest, and most of the criticism it faces, comes from them.

This essay sets out the formal machinery, works through the standard examples with numbers, and then addresses a question the canonical formulations leave open: *which* probabilities go into the calculation when the agent's own choice is evidence about the world. Material drawn from the reference article (Wikipedia's "Causal decision theory") is marked as such. Operational proposals, the numerical parameters, and the structural-model reading are my own additions or standard literature that the article does not discuss.

## 2. The common skeleton

Both theories share the same raw materials:

- a finite set of **acts** $\mathcal{A} = \{A_1, \dots, A_m\}$ available to the agent;
- a set of **outcomes** $\{O_1, \dots, O_n\}$;
- a **desirability** (utility) function $D(O_j)$;
- a credence function $P$ over propositions.

Each theory then scores an act by an expectation of the form $\sum_j (\text{weight of } O_j \text{ given } A)\, D(O_j)$. They differ only in the weight.

**EDT** uses the conditional probability:
$$V(A) = \sum_j P(O_j \mid A)\, D(O_j).$$

**CDT**, in the formulation of Gibbard and Harper (1981) quoted in the source, uses the probability of a counterfactual conditional:
$$U(A) = \sum_j P(A \mathbin{\Box\!\!\to} O_j)\, D(O_j),$$
where $A \mathbin{\Box\!\!\to} O_j$ reads "if I were to do $A$, $O_j$ would obtain."

The informal gloss in the source is the apple example. If you are unsure whether the apple is good, the expected causal effect of eating it depends on three quantities: the probability that it is good, how happy a good apple makes you, and how sad a bad one makes you. With $P(\text{good}) = 0.7$, $D(\text{happy}) = 5$, $D(\text{sad}) = -3$, we get $U(\text{eat}) = 0.7\cdot 5 + 0.3\cdot(-3) = 2.6$. Here the apple's quality does not depend on whether you eat it, so the counterfactual and conditional probabilities coincide and EDT gives the same number. The interesting cases are the ones where they do not coincide.

## 3. Dependency hypotheses: a more usable form

The Gibbard–Harper formula asks for probabilities of counterfactuals, which are hard to assess directly. A more practical equivalent, associated with Lewis (1981) and Skyrms, factors the agent's uncertainty into two parts:

1. uncertainty about **how the world is arranged independently of the choice**, and
2. uncertainty about **what each act would bring about given that arrangement**.

Let $\mathcal{K} = \{K_1, \dots, K_r\}$ be a partition into *dependency hypotheses*. Each $K_i$ is a maximally specific proposition about how outcomes causally depend on acts, and nothing the agent does can affect which $K_i$ is true. Then
$$U(A) = \sum_{i} P(K_i) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j). \tag{1}$$

Compare EDT, which by the law of total probability can be written
$$V(A) = \sum_{i} P(K_i \mid A) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j). \tag{2}$$

The entire difference is the weight on the dependency hypothesis. CDT uses the **unconditional** $P(K_i)$. EDT uses $P(K_i \mid A)$. CDT refuses to let the act serve as evidence about things the act cannot influence. As the source puts it, quoting Egan's critical summary, CDT holds "fixed the agent's unconditional credences in dependency hypotheses."

**An interventionist reading (my addition).** If the agent's beliefs are encoded in a causal Bayesian network, with the act as a node, (1) is the back-door adjustment formula of Pearl's do-calculus:
$$U(A) = \sum_j P(O_j \mid do(A))\, D(O_j), \qquad P(O_j \mid do(A)) = \sum_k P(k)\,P(O_j \mid A, k),$$
where $k$ ranges over the act's causal parents and other confounders. Intervening on $A$ cuts the arrows into $A$, so the act stops carrying information about its causes. For a reader who wants an algorithm, this is the most operational form of CDT available. It is not, however, how the founders stated the theory, and the source does not mention it.

## 4. Why the two can come apart: Lewis and Gibbard–Harper

If $P(A \mathbin{\Box\!\!\to} O) = P(O \mid A)$ always held, CDT would collapse into EDT. The source reports that Lewis (1976) proved this identity cannot hold in general. More strongly, no conditional connective can have its probabilities equal to conditional probabilities across a class of probability functions closed under conditionalization, unless those functions are trivial.

The source also reports a positive result from Gibbard and Harper: given two axioms, one related to *conditional excluded middle*, statistical independence of $A$ and $A \mathbin{\Box\!\!\to} O$ guarantees the identity. The argument is short:

- *Centering*: if $A$ is true, then $A \mathbin{\Box\!\!\to} O$ holds exactly when $O$ does. So $A \wedge (A \mathbin{\Box\!\!\to} O) \equiv A \wedge O$.
- Therefore $P(O \mid A) = P(A \mathbin{\Box\!\!\to} O \mid A)$.
- If $A$ is independent of $A \mathbin{\Box\!\!\to} O$, the right side equals $P(A \mathbin{\Box\!\!\to} O)$.

Conditional excluded middle, which says that for each act exactly one outcome-counterfactual holds, is what lets the counterfactuals form a partition so that the expectation is well defined. The lesson is diagnostic: **CDT and EDT diverge exactly when the act is evidentially correlated with which counterfactuals are true.** That happens when there is a common cause of the act and the outcome, or when some predictor tracks the act.

## 5. Worked examples

### 5.1 King David and Bathsheba (common cause)

Gibbard and Harper's case, quoted in the source: a king's charisma is fixed by genes and upbringing. Charismatic kings tend to act justly. Uncharismatic kings tend to act unjustly and also suffer revolts, because of their "sneaky, ignoble bearing," not because of their unjust acts. David wants to summon Bathsheba, which is unjust, and does not know his own type.

To make it numerical, I choose illustrative figures:
- $P(C) = 0.5$ (charismatic);
- $P(\text{revolt}\mid C) = 0.1$ and $P(\text{revolt}\mid \neg C) = 0.9$, whatever David does;
- $P(\text{send}\mid C) = 0.2$ and $P(\text{send}\mid \neg C) = 0.8$;
- utilities are additive: $+10$ for Bathsheba, $-100$ for a revolt.

The dependency hypotheses are $\{C, \neg C\}$. Since sending does not affect revolt within either cell:

**CDT:**
$U(\text{send}) = 10 - 100[0.5(0.1)+0.5(0.9)] = -40$ and $U(\text{abstain}) = -50$. CDT says send. The ten-point advantage holds whatever $P(C)$ is, because sending adds 10 and causes nothing else.

**EDT:** By Bayes, $P(C\mid\text{send}) = 0.1/0.5 = 0.2$ and $P(C\mid\text{abstain}) = 0.4/0.5 = 0.8$. So
$V(\text{send}) = 10 - 100(0.2\cdot0.1 + 0.8\cdot0.9) = -64$ and $V(\text{abstain}) = -100(0.8\cdot0.1+0.2\cdot0.9) = -26$. EDT says abstain.

This matches the verdicts the source reports. CDT's reasoning is that abstaining would only make David *look* charismatic. It would not *make* him charismatic, and only charisma prevents revolts. The source notes that when forced to choose, philosophers usually prefer CDT, and cases like this one, sometimes called "medical Newcomb problems," are a large part of the reason.

### 5.2 Newcomb's problem (predictor)

As described in the source: box A is transparent and holds \$1,000. Box B is opaque and holds \$1,000,000 if and only if a 99%-reliable predictor predicted that you would take only B. You choose between one-boxing and two-boxing.

Here the dependency hypotheses are $K_{\text{full}}$ and $K_{\text{empty}}$, the already-fixed contents of box B. Let $q = P(K_{\text{full}})$.

**CDT:**
$$U(\text{two}) = q(1{,}001{,}000) + (1-q)(1{,}000) = U(\text{one}) + 1{,}000.$$
Two-boxing wins by exactly \$1,000 *for every* $q$. This is causal dominance: the contents are fixed, and taking A adds \$1,000 to whatever is in B.

**EDT:** With $P(K_{\text{full}}\mid\text{one}) = 0.99$ and $P(K_{\text{full}}\mid\text{two}) = 0.01$, we get $V(\text{one}) = 990{,}000$ and $V(\text{two}) = 11{,}000$. EDT one-boxes.

The source records that philosophers disagree about which answer is rational. The standard objection to two-boxing is "if you're so smart, why ain'cha rich?": one-boxers walk away with millions on average. The causalist reply is that the predictor rewards a *disposition*, not the *act*. At the moment of choice, the one-boxer leaves \$1,000 on the table that she could have taken. The objection compares agents facing different boxes, whereas CDT compares acts available to one agent facing fixed boxes.

### 5.3 Twin prisoner's dilemma

The source notes, following Lewis (1979), that the prisoner's dilemma against a near-identical "twin" has Newcomb's structure. The twin's choice is strongly correlated with yours but is not caused by it. CDT takes the twin's act as a dependency hypothesis, so defection dominates and CDT defects. EDT cooperates when the correlation is strong enough. The general pattern is that **CDT defects in any one-shot game in which the other party's move is causally independent of yours**, however strong the correlation.

## 6. The open question: where do $P(K_i)$ come from?

Formula (1) is precise once the partition $\mathcal{K}$ and the credences $P(K_i)$ are given. The source identifies two ways this is underdetermined.

**(a) Vagueness about counterfactuals.** The source reports (citing Shaffer 2009) that CDT does not itself specify an algorithm for computing counterfactual probabilities. Lewis's *imaging* proposal moves each world $w$'s probability to the closest world $w_A$ in which $A$ holds:
$$P_A(X) = \sum_w P(w)\,\mathbf{1}[w_A \in X], \qquad P(A \mathbin{\Box\!\!\to} O) = P_A(O).$$
The source raises a regress worry: knowing where mass should move requires knowing what one would believe on becoming certain of $A$, which is itself a conditional one may be unsure about. A similarity ordering over worlds is also needed, and that is philosophically loaded.

*My operational resolution.* In practice I recommend replacing world-similarity with a causal model. Treat the act as an exogenous intervention. Let $\mathcal{K}$ be the joint states of every variable not causally downstream of the act, coarsened as far as possible without losing information about $P(O \mid do(A), K)$. Imaging then becomes "hold fixed everything not downstream of $A$, set $A$, and propagate forward," which is the do-operator. This removes the regress, because the causal model is part of the agent's credal state and not a further conditional to be assessed. The price is real: it assumes the agent has a causal model. Uncertainty over models can be handled by putting models into $\mathcal{K}$, since which model is true is not something the act causes.

**(b) Self-evidence and instability.** The deeper problem is this. If $P(K_i)$ is an unconditional credence, it depends on how likely the agent thinks she is to perform each act, and that is exactly what deliberation is meant to settle. Usually this does not matter. In Newcomb's problem, two-boxing wins for every $q$. In other cases it matters decisively.

### 6.1 Death in Damascus

Death predicts where you will be tomorrow and waits there. You can stay in Damascus ($D$) or flee to Aleppo ($L$). Death is reliable: say $P(\text{Death predicts } X \mid \text{you go to } X) = 0.9$. Survival is worth 1 and death 0. Let $r$ be your current credence that you will go to Aleppo. Death's location is a dependency hypothesis, with
$$P(\text{Death at } L) = 0.9r + 0.1(1-r) = 0.1 + 0.8r.$$
Then $U(L) = 1 - (0.1+0.8r) = 0.9 - 0.8r$ and $U(D) = 0.1 + 0.8r$. Thus $U(L) > U(D)$ exactly when $r < 1/2$.

The trouble follows directly. If you lean toward Damascus, CDT says go to Aleppo. Once you lean toward Aleppo, CDT says go to Damascus. Neither pure act is stable. The source says that a CDT agent "would be unable to process the correlation" here, citing Egan, Meacham, and Harper.

Two refinements from the literature (Harper's ratifiability, cited in the source; Skyrms's and Joyce's deliberational dynamics) give an operational answer:

**Ratifiability.** An act $A$ is ratifiable if, computing with $P(\cdot \mid A)$ in place of $P$ for the dependency hypotheses, no alternative beats it:
$$\sum_i P(K_i\mid A)\, \mathbb{E}[D \mid A, K_i] \;\ge\; \sum_i P(K_i\mid A)\, \mathbb{E}[D \mid B, K_i] \quad \forall B.$$
"Choose A" is ratifiable if, supposing you had decided on $A$, you would not wish you had done otherwise. In Death in Damascus no pure act is ratifiable.

**Deliberational equilibrium.** Treat $r$ as a state that evolves during deliberation. It moves toward whichever act currently has higher $U$, and the agent stops at a fixed point where no act is strictly preferred. Here the equilibrium is $r^* = 1/2$, with $U(L) = U(D) = 1/2$. Joyce's defense, mentioned in the source, uses this idea: CDT can take "information about what one is inclined or likely to do as evidence." The probabilities held fixed should be the agent's credences *at the end of rational deliberation*, not her arbitrary starting point.

*My proposed rule for unstable cases.* Compute $U$ as a function of the agent's act-credences $\mathbf{r}$. Find the deliberational equilibria, which are the $\mathbf{r}^*$ such that every act with $r_A^* > 0$ maximizes $U_{\mathbf{r}^*}$. If several exist, take the one with the highest equilibrium value, and if the agent can randomize, implement $\mathbf{r}^*$ with a randomizing device. This is a substantive addition to bare CDT. Its justification is that it is the unique natural way to make (1) well defined when $P(K)$ depends on $P(A)$, and that it coincides with ordinary CDT whenever one act wins for every $\mathbf{r}$, as in Newcomb and Bathsheba.

### 6.2 The Psychopath Button

Egan's case, quoted in the source: Paul would like a world with no psychopaths, but only a psychopath would press the button, and pressing it would kill Paul if he is one. Egan reports that "pretty much everyone" thinks Paul should not press, yet naive CDT says press.

To quantify, I choose: $+10$ for a psychopath-free world with Paul alive, $0$ for the status quo, $-100$ for Paul's death. Let $s = P(\text{Paul is a psychopath})$, which is a dependency hypothesis. Then $U(\text{press}) = 10(1-s) - 100s = 10 - 110s$ and $U(\text{not}) = 0$, so CDT says press iff $s < 1/11$. Paul's prior $s$ is small, so naive CDT says press.

Under the equilibrium rule, let $P(\text{psycho}\mid\text{press}) = 0.9$ and $P(\text{psycho}\mid\text{not}) = 0.01$. Then $s(r) = 0.01 + 0.89r$. Neither act is ratifiable. Conditional on pressing, $s = 0.9$ and pressing looks catastrophic. Conditional on not pressing, $s = 0.01$ and pressing looks good. The equilibrium sets $s(r^*) = 1/11$, giving $r^* \approx 0.091$. Equilibrium CDT therefore tells Paul to be indifferent and, if randomizing, to press with probability about 9%. That is better than naive CDT, but it is still not the clear "don't press" that intuition delivers. Critics take this residue as evidence that the problem goes deeper than a choice of credences.

### 6.3 The Adversarial Offer: money pumps

The source cites Oesterheld and Conitzer's case. Two boxes cost \$1 each, and you may buy at most one. Yesterday the seller put \$3 in each box she predicted you would *not* buy. Her prediction is accurate with probability 0.75.

Whatever she predicted, at least one box is full: if she predicted box 1, box 2 is full, and if she predicted "none," both are. Hence $P(\text{box}_1\text{ full}) + P(\text{box}_2\text{ full}) \ge 1$ for *any* credences, so some box has
$$U(\text{buy}_k) \ge 3\cdot\tfrac12 - 1 = 0.5 > 0 = U(\text{none}).$$
CDT therefore always buys, and this verdict is immune to the equilibrium refinement. But the seller predicts the purchase correctly 75% of the time, and then the bought box is empty. The buyer's actual expected return is $0.25\cdot 3 - 1 = -\$0.25$ per round. The source reports that a seller can exploit this and that causal decision theorists are vulnerable to diachronic Dutch books. EDT declines here, since $V(\text{buy}_k) = 0.25\cdot 3 - 1 < 0$.

The causalist response, given by Joyce (2020, cited in the source), is the Newcomb reply again. Each purchase is a good bet relative to boxes whose contents are already fixed, and the loss reflects a predictor punishing a disposition. Whether that reply convinces is now one of the main fault lines in the debate.

## 7. A procedure for unfamiliar cases

Collecting the above, here is how to apply CDT to a new problem. Steps 1–4 are standard CDT. Steps 5–6 are the refinements I have argued for.

1. **List acts and outcomes**, and assign utilities.
2. **Draw the causal structure.** Identify every variable whose value the act cannot influence: past events, fixed traits, others' predictions, and the choices of causally isolated agents such as twins.
3. **Form the dependency partition** $\mathcal{K}$ from those variables.
4. **Compute** $U(A) = \sum_i P(K_i)\,\mathbb{E}[D \mid do(A), K_i]$. Check for **causal dominance**: if one act is best within every $K_i$, choose it and stop. Bathsheba, Newcomb, the twin dilemma, and the Adversarial Offer all end here.
5. **If $P(K_i)$ depends on your own act-credences** and the ranking flips with them, compute the deliberational equilibria and check ratifiability.
6. **Choose** a ratifiable act if one exists. Otherwise adopt the best equilibrium mixed act.

A diagnostic for whether CDT and EDT will disagree is to ask whether the act is evidence about some $K_i$. If it is not, as in the apple, ordinary gambles, and most engineering decisions, the two theories coincide and the controversy is idle.

## 8. Philosophical assessment

CDT's motivation is that choosing is *intervening*. Deliberation should identify the differences you can make, not the news you would like to receive. This gives CDT the right answer in common-cause cases such as Bathsheba, smoking-lesion, and medical Newcomb problems, where EDT recommends "managing the news." It also matches how scientists and engineers evaluate interventions.

Its costs, as the source catalogues them, are threefold. First, its key input, counterfactual probability, is underspecified, and imaging threatens regress. Second, it gives unstable or counterintuitive verdicts in Death in Damascus and the Psychopath Button. Egan diagnoses the source of trouble as the requirement to hold dependency hypotheses fixed at their unconditional values. Third, it can be money-pumped by predictors. Refinements such as ratifiability and deliberational equilibrium repair the instability. They do not touch the Newcomb-style verdicts, which causalists regard as features, not bugs.

## 9. Conclusion

Formally, CDT is expected-utility maximization with one distinctive choice: outcomes are weighted by the probabilities they would have *if the act were performed*. Equivalently, the agent's credences about everything outside the act's causal reach are held fixed. In dependency-hypothesis form, $U(A) = \sum_i P(K_i)\,\mathbb{E}[D\mid A, K_i]$, and the theory differs from EDT exactly by refusing to replace $P(K_i)$ with $P(K_i\mid A)$. That refusal yields CDT's best result, ignoring spurious correlations in common-cause cases, and also its most contested ones: two-boxing, defecting against twins, and buying from adversarial predictors. The theory as stated leaves open how counterfactual probabilities are computed and which act-credences anchor $P(K_i)$. I have suggested resolving the first with causal models and interventions, and the second with deliberational equilibrium. These turn CDT into a usable procedure, though they leave its central philosophical bet unchanged.

---

**References (selected)**
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Phil. Review* 85: 297–315.
- Lewis, D. (1981). "Causal decision theory." *Australasian J. Phil.* 59: 5–30.
- Egan, A. (2007). "Some counterexamples to causal decision theory." *Phil. Review* 116: 93–114.
- Joyce, J. (2012). "Regret and instability in causal decision theory." *Synthese* 187: 123–145.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Phil. Quarterly* 71(4).
- Wikipedia contributors, "Causal decision theory," rev. 1381555528 (reference article).