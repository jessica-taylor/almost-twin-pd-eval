# Causal Decision Theory: Causation, Counterfactuals, and Choice

## 1. The problem decision theory faces

Suppose you face a choice among actions — eat the apple or the orange, take one box or two, press the button or leave it alone. Decision theory aims to give a systematic answer: an algorithm that takes your beliefs and desires as input and outputs a recommendation. Since Savage (1954), the near-universal currency of such algorithms has been *expected utility*: assign each possible outcome a numerical desirability, assign each outcome a probability conditional on your action, and maximize the resulting expectation.

The rub is in the phrase "conditional on your action." There are, at a formal level, at least two distinct ways to understand the probabilities in an expected-utility calculation:

1. **Evidentially.** Ask: *how likely would each outcome be, given the news that I perform this action?* Formally, $P(O_j \mid A)$ — ordinary conditional probability. This yields **evidential decision theory (EDT)**:

$$EU_{\text{edt}}(A) = \sum_j P(O_j \mid A)\, D(O_j).$$

2. **Causally.** Ask: *what would each outcome be if I were to causally bring about this action?* This yields **causal decision theory (CDT)**, the subject of this essay. Its slogan, from the Wikipedia source we build on: *select the action which causes the best outcome in expectation*.

The distinction seems pedantic — surely "if I do $A$" just means "$A$ happens"? A landmark theorem of David Lewis (1976) says otherwise: the probability of a conditional $P(A \to O)$ cannot in general be identified with the conditional probability $P(O \mid A)$. Lewis's triviality result shows that any attempt to define a "conditional probability function" $P(A \to O)$ satisfying certain composition axioms collapses: if such an object existed and updated by conditionalization, the class of probability functions would be driven to triviality (functions never assigning positive probability to more than two incompatible alternatives). This formal gap is not a curiosity; it is precisely the room in which the two decision theories come apart, and it is why they give different answers to Newcomb's problem, the Prisoner's Dilemma against a twin, and a growing family of other cases.

This essay develops CDT in detail: its formal core (§2), the machinery of counterfactual probabilities and how to compute them (§3), its divergence from EDT in concrete cases (§4), its celebrated applications and failures (§5–6), and my own attempt to give the theory a coherent operational reading that clarifies where it succeeds and where it genuinely breaks (§7).

## 2. The formal core

Following Gibbard and Harper (1981), the central object is the **causal expected utility** of an action $A$:

$$U(A) = \sum_j P(A \,\square\!\!\to\, O_j)\, D(O_j),$$

where $D(O_j)$ is the desirability (utility) of outcome $O_j$, and $P(A \,\square\!\!\to\, O_j)$ is the agent's credence in the *counterfactual* "were $A$ performed, $O_j$ would result" (I use $\,\square\!\!\to\,$ for the counterfactual conditional, following Lewis's notation, to distinguish it from the material conditional and from $P(\cdot\mid\cdot)$). The rational act, on CDT, is $\arg\max_A U(A)$.

Three remarks on this formula.

**(a) It is expected utility over *counterfactual* probabilities, not conditional probabilities.** This is the entire difference from EDT. In many ordinary cases the two coincide: if the apple's goodness is causally independent of my choice to eat it, then $P(\text{happy} \mid \text{eat}) = P(\text{eat} \,\square\!\!\to\, \text{happy})$, and both theories say "eat the apple." Gibbard and Harper showed, further, that under two axioms — one of which is the controversial *conditional excluded middle* (CEM: for any $A$ and $B$, either $A \,\square\!\!\to\, B$ or $A \,\square\!\!\to\, \neg B$) — the mere *statistical independence* of $A$ and $A \,\square\!\!\to\, O_j$ suffices to guarantee $P(A \,\square\!\!\to\, O_j) = P(O_j \mid A)$. The theories are designed to be coextensive on "causally boring" problems; they diverge only where the action is statistically correlated with factors it does not cause.

**(b) The desirability function is common ground.** Both CDT and EDT can share $D$. The disagreement is entirely about the probability measure over outcomes, i.e., about which *epistemic state* the agent should evaluate actions from.

**(c) What is $A \,\square\!\!\to\, O_j$?** It is the counterfactual "if $A$ were the case, $O_j$ would be the case." In Lewis's possible-worlds semantics, $A \,\square\!\!\to\, O$ is true at world $w$ iff in the closest $A$-world(s) to $w$, $O$ holds. "Closest" is governed by a comparative-similarity relation that respects causal structure: worlds are made distant by changes in *laws* first, then in *particular facts about the past*. This is what makes the semantics causal in spirit: when evaluating "if I two-box," we hold fixed the past state of the world — including the predictor's earlier prediction — and let only downstream consequences vary.

## 3. Computing the counterfactual probabilities

The Wikipedia source is candid that CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." This is a real gap for anyone wanting to *use* the theory. Two main proposals exist; I describe both, then argue that they are best understood as two presentations of a single idea.

### 3.1 Lewis's imaging

Lewis (1981) proposed **imaging**: to evaluate $P(A \,\square\!\!\to\, O_j)$, redistribute probability mass from each possible world $w$ to the closest world $w_A$ in which $A$ holds. Formally, if $\delta_A(w, w')$ measures the "distance" from $w$ to the nearest $A$-world $w'$:

$$P_A(O_j) = \sum_w P(w)\, \mathbb{1}[O_j \in w_A],$$

i.e., $P_A$ is the probability function obtained by *transporting* each world's mass to its nearest $A$-world, rather than *deleting* worlds incompatible with $A$ as conditionalization does. The contrast is vivid:

- **Conditionalization** throws away worlds where $\neg A$ and renormalizes. It asks: among worlds consistent with my having done $A$, which outcomes obtain? This preserves *all* correlations, including acausal ones.
- **Imaging** keeps every world's mass but reroutes it to the nearest world where $A$ holds. It asks: *in each possibility as I take the world to actually be, what would happen if $A$ were imposed?* Correlations not caused by $A$ are dragged along intact; the change in $A$ is localized to its causal neighborhood.

### 3.2 Joyce's conditional objective chance and Pearl's do-operator

Joyce (1999) and others reformulate CDT via an expectation over **dependency hypotheses**: chance-setting propositions about which causal structure obtains. Writing $K$ for such a hypothesis, the causal expected utility becomes

$$U(A) = \sum_K P(K) \sum_j P(O_j \mid A, K)\, D(O_j).$$

In Pearl's (2009) causal graphical-model vocabulary, this is exactly the **do-operator**: $P(O_j \mid \text{do}(A))$ is computed by mutilating the causal graph — deleting all arrows into the decision node — and then conditioning on $A$. Joyce's formulation and imaging typically agree when the dependency hypotheses are stated at the right grain; Pearl's do-calculus gives them a concrete computational home.

The source notes a potential **regress** in imaging: to evaluate $P(A \,\square\!\!\to\, O_j)$ we must know "what we would believe if we were certain of $A$" — itself a conditional, possibly with probability less than 1, inviting an infinite hierarchy. I think the worry is less severe than it appears *if* we read imaging not as a psychological procedure but as a definition relative to a background causal model. On this reading — which I offer as my own operational interpretation, not one explicit in the source — the input to CDT is not a raw probability distribution over worlds but a distribution over *causal models* (in Pearl's sense, a DAG plus conditional probabilities). Imaging then has a non-circular semantics: the "closest $A$-world" to $w$ is the world that results from surgically setting the decision variable to $A$ in $w$'s causal model, leaving everything not causally downstream of the decision untouched. The regress evaporates because the closeness metric is read off the represented causal structure, not bootstrapped from further conditionals. The genuine residual cost is that the agent must have *causal* beliefs, not merely probabilistic ones — a cost EDT avoids but, as we shall see, pays for elsewhere.

## 4. Where CDT and EDT part ways: the David example

Gibbard and Harper's King David example cleanly exhibits the divergence. David desires Bathsheba but fears revolt. Psychology tells him: kings are charismatic or uncharismatic; charisma is fixed by genetics and childhood and *cannot be changed in adulthood*; charismatic kings tend to act justly, uncharismatic kings unjustly; successful revolts target uncharismatic kings — but *not because* of their unjust acts, rather because uncharismatic kings have a "sneaky, ignoble bearing" that invites revolt. David does not know which type he is, and knows summoning Bathsheba is unjust.

Let $C$ = charismatic, $S$ = summon, $R$ = successful revolt. The causal structure is:

$$C \longrightarrow \text{bearing} \longrightarrow R, \qquad C \longrightarrow S, \qquad S \not\longrightarrow R.$$

Summoning is an unjust act, so choosing $S$ is *strong evidence* that David is uncharismatic ($P(C \mid S)$ is low). EDT therefore computes a high probability of revolt conditional on summoning and recommends restraint. But this evidential link runs through a common cause: David's fixed charisma determines both his inclination to summon and his revolt-vulnerability. Deciding to summon does not make him uncharismatic — that was settled long ago. CDT, holding fixed David's credence over his own type, computes $P(R \mid \text{do}(S)) = P(R)$, unchanged, and recommends **summoning**: the act's only causal effect is Bathsheba's company, which David values.

Formally in the Joyce/Pearl idiom: $U(S) = \sum_{c} P(c)\,[P(R \mid c)\,D(S, R, c) + P(\neg R \mid c)\,D(S, \neg R, c)]$, whereas $EU_{\text{edt}}(S) = \sum_j P(S, j)\,D(j)$ with $j$ ranging over type-outcome pairs. The difference is whether David's decision *screens off* his type. Most philosophers side with CDT here: it seems irrational to forgo a desired outcome merely because pursuing it is diagnostic of a fact you cannot influence. (A refinement is due to Eells and Seidenfeld's *ratifiability* requirement, discussed in §6: an act should be maximal given the supposition that you will in fact perform it — which matters when the act provides evidence about your own deliberation, as here.)

## 5. Newcomb's problem

Newcomb's problem is the canonical stress test. A near-perfect predictor (99% accurate) has already placed $\$1{,}000{,}000$ in opaque box B iff it predicted you will take only B; transparent box A always contains $\$1{,}000$. You choose: take both, or take only B.

**EDT one-boxes.** $P(\text{B full} \mid \text{one-box}) \approx 0.99$, so

$$EU_{\text{edt}}(\text{one-box}) \approx 0.99 \times 10^6, \qquad EU_{\text{edt}}(\text{two-box}) \approx 0.01 \times 10^6 + 1000.$$

**CDT two-boxes.** The prediction is in the past; your action does not causally reach it. Imaging holds fixed the predictor's completed act:

$$U(\text{two-box}) = P(\text{B empty})\,(10^6 + 1000)\cdot 0 + P(\text{B empty})\cdot 1000 + \dots$$

more carefully, $U(\text{two-box}) = 1000 + 10^6 \cdot P(\text{B full})$ vs. $U(\text{one-box}) = 10^6 \cdot P(\text{B full})$: two-boxing strictly dominates by $\$1{,}000$ in causal expectation, whatever $P(\text{B full})$ is. CDT's verdict is that at the moment of decision, the money is already there or not, and taking both causally secures $\$1{,}000$ extra on every possibility.

The source flags that CDT's recommendation — unsurprisingly, since it walks away with $\$1{,}000$ while EDT agents average $\sim\$990{,}000$ — has been treated as a counterexample "from birth." I want to make the structure precise, because it recurs. The predictor's prediction and your choice are correlated through a common cause: your *decision disposition* (or, in variants, your algorithm/character). Both theories agree on the correlation; they disagree on whether choosing should be evaluated as an intervention on your disposition (it is not — by the time you choose, it is fixed) or as evidence about it (it is). CDT's two-boxing is correct *given its own interpretive stance*: the choice is a lever on downstream effects only. Whether that stance is the right one for a *self-modeling* agent is the deeper question, to which I return in §7.

A related and underappreciated case, due to Lewis (1979) and Howard (1988): the **Prisoner's Dilemma against a psychological twin**. If your twin's choice correlates strongly with yours without being caused by it (common cause: similar upbringing/genes), CDT defects (dominance: defection causally gets you $\$1$ more on each outcome) while EDT cooperates (your cooperation is news that your twin cooperates). Here many intuitions flip: cooperating against a twin seems less crazy than one-boxing. The lesson, taken seriously by Joyce (2012) and others, is that intuitions track case-by-case features, not a stable theory verdict.

## 6. Genuine counterexamples to CDT

Recent literature has produced cases where CDT's failure is harder to dismiss. I present three, with the arithmetic.

**Death in Damascus.** Death is a perfect predictor and waits where it predicts you will be tomorrow. You can flee to Aleppo or Damascus today. If Death is in your city, staying put gets you killed; fleeing to the other city is safe. Your credences satisfy: $P(\text{Death in Damascus} \mid \text{I stay}) \approx 1$ and $P(\text{Death in Aleppo} \mid \text{I go}) \approx 1$. EDT handles this gracefully. CDT computes: fleeing to Aleppo has causal expected utility $P(\text{Death in Aleppo}) \cdot (\text{death}) + \dots$ — and since by the setup $P(\text{Death in Damascus} \mid \text{stay}) \approx 1$, symmetry implies $P(\text{Death in Aleppo}) \approx 1$ (Death is somewhere, and it predicts *your* choice, including your fleeing). So fleeing looks safe and staying looks fatal — but by the same reasoning *staying* also looks safe and fleeing fatal. Meacham (2010) and Egan (2007) show the CDT agent **cycles**: whatever act it settles on becomes, upon supposing it will perform that act, the act whose alternatives look better. It is caught in an unstable loop and, on some versions, voluntarily loses money or forgoes guaranteed payoff.

**The Adversarial Offer** (Oesterheld & Conitzer 2021). Two boxes, each costs $\$1$; you may buy at most one. Yesterday the seller put $\$3$ in each box she predicted you would *not* buy; her predictions are 75% accurate. From the buyer's perspective: *at least one* box was predicted-not-bought (you buy at most one), so *at least one* box contains $\$3$ with probability $\geq 0.75$. The average box therefore has causal expected value $\geq 0.5 \times 0.75 \times 3 = \$1.125 > \$1$. CDT buys a box. But the seller profits: CDT's very predictability as a causal expected-utility maximizer is exploited. The seller's money-making strategy works *because* CDT agents have stable, predictable reasoning from their own fixed credences.

**The Psychopath Button** (Egan 2007). Paul may press a button that kills all psychopaths; he'd love a psychopath-free world; he is nearly certain *only a psychopath would press it*; he vastly prefers living (with psychopaths) to dying. CDT: pressing causally kills psychopaths other than Paul (their existence is not causally up to Paul) and kills Paul only if he is a psychopath. Paul is confident he is not a psychopath — after all, he is so reluctant to press... but wait: *that* reluctance is evidence against being a psychopath, and it is exactly what CDT's "hold fixed your unconditional credences" instruction forbids him from using when he contemplates pressing. Under the supposition "Paul presses," the evidence that he is a psychopath becomes overwhelming, so pressing looks suicidal; but CDT evaluates pressing with his *unconditional* credence $P(\text{psychopath}) \approx 0$, so pressing looks wonderful. Nearly everyone agrees Paul should not press; plain CDT says press.

**Diagnosis.** Egan's diagnosis (which the source endorses) is that there is a disconnect between the intuitive rule "do what you expect will bring about the best results" and CDT's algorithm "maximize expected utility holding fixed your unconditional credences about the causal structure." The culprit is precisely the fixing: in these cases the act is *evidence about the dependency hypothesis itself* (am I the kind of agent — or person — whose choice is linked to bad outcomes?), and orthodox CDT refuses to condition on that evidence at evaluation time.

**Joyce's response.** Joyce (2012) argues that a properly *ratifiability*-constrained CDT can handle these cases. An act $A$ is **ratifiable** if it maximizes $U$ among acts, evaluated *given the supposition that you choose $A$* — where "given the supposition" is understood causally-appropriately, e.g., via conditioning on the choice as an act of your deliberating self. In the Psychopath Button, pressing is not ratifiable: conditional on your choosing to press, $P(\text{psychopath})$ soars and $U(\text{press} \mid \text{pressing}) < U(\text{refrain} \mid \text{pressing})$. In Death in Damascus, *no* act is ratifiable — the instability is genuine — which Joyce treats as a limit case rather than a refutation. Whether ratifiability rescues CDT in the Adversarial Offer is contested; Oesterheld and Conitzer (2021) show that CDT agents remain systematically exploitable across a family of such scenarios, and are vulnerable to **diachronic Dutch books** (sequences of bets, each individually acceptable at its time of offer, that jointly guarantee a loss).

I flag clearly, following the source's own distinction, what is established and what is my extrapolation: *established* (from the cited literature) are the existence of the cycling/instability phenomena and the money-pumping constructions; *my proposal* is the reading of these results in §7 below.

## 7. An operational reading: CDT as interventional choice for a self-modeling agent

Let me try to give the theory its best operational formulation and say where I think it genuinely stands.

**The proposal.** Model the agent as having (i) a credence distribution over causal models of the world, including a node $D$ for its own decision, and (ii) a deliberation rule. CDT is the rule: *evaluate each candidate act as an intervention $\text{do}(D = A)$ in each causal model, average over models, maximize.* The "hold fixed unconditional credences" instruction is then not an arbitrary stipulation but the semantic content of $\text{do}$: interventions break arrows *into* the decision node, so the decision's correlations with its causes carry no evidential weight *inside the evaluation*.

This reading clarifies the theory's scope. CDT is the correct theory for an agent whose choices function as **levers**: actions whose causal consequences are downstream and whose evidential ties to fixed facts should be ignored. Smoking and the lesion (the classic companion to the David case), the apple's quality, David's charisma — in all these, CDT is right and EDT is wrong, because the acausal correlation is a common-cause artifact and acting on it is superstition.

But the reading also exposes the theory's blind spot: a self-modeling agent's choice is not only a lever; it is also a **reading of itself**. In the Psychopath Button, the choice is diagnostic of the agent's own type, and the type is causally relevant to the outcome. CDT's interventional semantics forbids the agent from using that self-diagnosis — yet the agent, at deliberation time, *possesses* it and *knows* its reliability. The Adversarial Offer sharpens this into a practical theorem: an agent whose deliberation is predictable from its fixed credences can be systematically exploited by parties who model that deliberation. In such settings, the correct object of choice may not be the act but a **policy or disposition** — e.g., "be the kind of agent who does not buy boxes from adversarial sellers," or "one-box in Newcomb problems." Evaluating policies rather than acts (a move associated with Meacham's "binding," and with functionalist/updates of decision theory in the AI-alignment literature) lets the agent count the downstream causal consequences of *having* a disposition, which in Newcomb cases includes the predictor's past behavior — not because the choice causes the prediction, but because the disposition caused it, and the agent can choose, at the level of disposition, to be one-boxing.

This is, I emphasize, beyond the source: the Wikipedia article reports the counterexamples and Joyce's ratifiability response but does not endorse policy-level evaluation. My claim is only that it is the most natural repair consistent with CDT's causal commitment: the causal graph is simply drawn one level up, with the decision *algorithm* rather than the decision as the intervention point. Notably, this repair keeps CDT's virtues (it still two-boxes *given* a fixed disposition... no — more precisely, it recommends acquiring the one-boxing disposition, and then one-boxing follows) while avoiding the exploited-agents trap. It also explains why intuitions split in the twin Prisoner's Dilemma: at the level of acts CDT defects, at the level of dispositions the causal consequences of "being a cooperator with a twin" include the twin's cooperation, and cooperation can be causally optimal.

The unresolved question, which I leave open because the literature leaves it open, is whether the disposition-level evaluation collapses back into EDT (since policy evaluation often resembles evidential reasoning about one's own algorithm) or constitutes a genuinely third theory. Oesterheld and Conitzer's Dutch book results suggest that *some* departure from act-level CDT is mandatory for any agent that expects to face predictors; the precise formalization remains contested.

## 8. Conclusion

Causal decision theory replaces evidential conditioning with counterfactual or interventional probability in the expected-utility formula. Its mathematical heart is a small set of ideas: Lewis's theorem that $P(A \,\square\!\!\to\, O) \neq P(O \mid A)$ in general; imaging versus conditionalization as two ways of updating on an action; and the Gibbard–Harper / Joyce / Pearl formalism that makes "holding fixed the causal background" precise via dependency hypotheses or the do-operator. Applied to ordinary choices and common-cause confusions — David, smoking, apples — it delivers the intuitively correct verdicts that EDT muddles. Applied to cases where the act is evidence about the agent's own fixed nature or predictable deliberation — Newcomb, Death in Damascus, the Psychopath Button, the Adversarial Offer — it either two-boxes into poverty or cycles unstably, and its best defenders must add structure (ratifiability, or in my reading, a shift from acts to policies) that goes beyond the theory's original statement.

The mathematical moral is clean: **CDT is the theory of choice under intervention, and it is exactly as good as the assumption that choice is intervention.** When that assumption holds, use it with confidence — draw the causal graph, apply the do-operator, maximize. When it fails — when your choice is a window onto yourself or a signal to predictors — the theory needs the agent to reason about dispositions as well as acts. That refinement, whether it counts as a rescue of CDT or its supersession, is the live frontier of the field.

### References (selected)

- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116: 93–114.
- Gibbard, A. & Harper, W. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese* 187: 123–145.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Philosophical Review* 85: 297–315.
- Lewis, D. (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs* 8: 235–240.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59: 5–30.
- Meacham, C. J. G. (2010). "Binding and its consequences." *Philosophical Studies* 149: 49–71.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Philosophical Quarterly* 71: pqaa086.
- Pearl, J. (2009). *Causality*, 2nd ed. Cambridge University Press.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy*.
- Wikipedia contributors (2026). "Causal decision theory," rev. 1381555528, CC BY-SA 4.0.