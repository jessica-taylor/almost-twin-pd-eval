# Causal Decision Theory: Definitions, Computation, and Where It Strains

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. The qualifier "in expectation" matters because the agent is usually uncertain what an act would cause. The qualifier "causal" distinguishes CDT from evidential decision theory (EDT), which ranks acts by how good the news of the act would be.

The source (a Wikipedia article) states the theory informally, gives the Gibbard–Harper formula, contrasts it with EDT, and lists criticisms. I mark below where I add material of my own.

## 2. The Gibbard–Harper formula

Gibbard and Harper (1981) define the utility of an act A as

U(A) = Σ_j P(A □→ O_j) · D(O_j),

where the O_j are mutually exclusive, exhaustive outcomes, D is desirability, and P(A □→ O_j) is the probability of the counterfactual "if A were performed, O_j would result." (The source writes the arrow as "→".) The rule is to maximize U.

EDT replaces the counterfactual probability with a conditional probability:

V(A) = Σ_j P(O_j | A) · D(O_j).

The two formulas are different objects. Lewis (1976) showed that the probability of a conditional does not in general equal the conditional probability, and his triviality results strengthen this. If P(A □→ O) always equalled P(O | A), the theories would coincide. The source notes that Gibbard and Harper show that, given two axioms (one tied to conditional excluded middle), P(A □→ O) = P(O | A) *when A is probabilistically independent of the counterfactual*. The theories diverge exactly when the act is evidence about the counterfactual, which is when something is correlated with the act without being caused by it.

## 3. An operational form (my elaboration)

The source says the theory does not specify how to compute counterfactual probabilities. A standard working version, which I adopt as a proposal and which is not stated in the source, uses **dependency hypotheses**: maximally specific hypotheses K about how outcomes depend causally on acts. Then

U(A) = Σ_K P(K) · Σ_j P(O_j | A, K) · D(O_j),

or, in a deterministic setting where K fixes the outcome function o_K(A),

U(A) = Σ_K P(K) · D(o_K(A)).

The key feature is that the weights are the **unconditional** credences P(K), not P(K | A). Evidence about K is allowed to enter only through the agent's current credences, and the act is not treated as further evidence. Egan (2007), cited in the source, describes this as "holding fixed the agent's unconditional credences in dependency hypotheses." This is the same as intervening on A (Pearl's do-operator) in a causal model: U(A) = Σ_j P(O_j | do(A)) D(O_j). Lewis's "imaging" is a related semantic route: shift probability mass from each world to the nearest world where A holds. The source records a regress worry for imaging, namely that we must already know what we would believe on supposing A. Causal models sidestep part of this by taking the causal structure as an input, but at the price of assuming that the structure is known or has well-defined credences. That is the real open question.

## 4. Worked examples

### 4.1 Apples
Let K₁ = "the apple is good" with credence p, giving happiness h, and K₂ = "bad" with credence 1−p, giving −s. Then U(eat) = p·h − (1−p)·s. Here the act does not bear on K, so CDT and EDT agree.

### 4.2 King David (from the source)
Let C = charismatic. The act "summon Bathsheba" (S) is unjust, and unjust acts do not cause revolts; the king's bearing does. Suppose R is revolt, with P(R | C) low and P(R | ¬C) high. Acts correlate with C (uncharismatic kings act unjustly), so P(R | S) > P(R | ¬S) and EDT counsels abstaining. But K is fixed, so under CDT

U(S) = Σ_K P(K) · D(outcome | S, K).

Summoning her yields her company in both states, with revolt risk fixed by C regardless of the act. Summoning dominates, assuming the pleasure of Bathsheba outweighs the injustice cost. Here CDT behaves like dominance reasoning.

### 4.3 Newcomb's problem (from the source)
Box A has $1,000. Box B has $1,000,000 iff the predictor predicted one-boxing, with 99% accuracy. Let K₁ = "B is full" with credence q. Then

U(two-box) = 1000 + q·10⁶, U(one-box) = q·10⁶.

Two-boxing wins by $1,000 for **every** q. So CDT two-boxes. EDT gets P(full | one-box) = 0.99 and computes 990,000 against 11,000 for two-boxing, and so one-boxes. The empirical complaint against CDT is that two-boxers end up richer by $1,000 *given the box contents* but predictably poorer on average. The CDT reply, due to Lewis and others, is that the game rewards irrationality and the predictor has simply penalized a rational type.

### 4.4 Prisoner's dilemma with a twin
Against a twin who correlates with you, defecting dominates causally, so CDT defects. Lewis (1979) argued that this is a Newcomb problem.

## 5. Unstable cases: when credences depend on the act's expected choice

The source mentions Death in Damascus. Death predicts your location and waits there: Damascus or Aleppo. Suppose that fleeing to Aleppo is slightly better if Death is in Damascus. Let r = your credence you will go to Damascus. A reliable predictor makes your credence in "Death in Damascus" close to r. Then

U(Damascus) = P(Death in Aleppo)·1 − P(Death in Damascus)·1 ≈ (1−r) − r (taking survival worth 1, death worth 0 in the relevant comparison, with the sign appropriately set),

and so whichever act you lean toward, the other looks better. No pure act is stable. Here simple CDT is *unstable*: it keeps recommending the opposite of what you are inclined to do. Responses, which are additions beyond the source's text, include:

- **Ratifiability** (Harper's work, cited): choose only acts that maximize U under the credences you would have after deciding on them.
- **Deliberational dynamics** (Joyce, Skyrms): iterate credence updating during deliberation and accept equilibria, which here are mixed (50/50).

The source reports Joyce's defence that CDT can legitimately treat information about one's own inclinations as evidence about K. Then P(K) is not fixed independent of that evidence, and U is computed using the credences you have *at the end of deliberation*. This is a real change in the theory, not just a gloss, and the unstable-case problem is largely about whether it is legitimate.

## 6. Critical cases

**Adversarial Offer** (source). Two boxes cost $1 each. The seller put $3 in each box she predicted you would *not* buy. Prediction accuracy is 0.75. You may buy one or none. CDT reasoning: at least one box has $3. With credence c₁, c₂ that boxes 1, 2 are full and c₁ + c₂ ≥ 1, one box has c ≥ ½, so its expected value is ≥ $1.50 > $1. Buying seems right. But if you tend to buy box i, the seller probably left it empty (probability 0.75), so the realized expected gain is 0.25·3 − 1 = −$0.25. CDT predictably loses money, and the seller profits. Oesterheld and Conitzer present this as extraction of money from CDT agents and as a diachronic Dutch book. A CDT defender replies that the agent's *unconditional* credences should update on its own leaning, so a sophisticated CDT agent, one that respects Joyce's point, would see the offer as a loss. Whether that reply is available without collapsing into EDT is the contested matter.

**Psychopath Button** (source). Paul prefers no psychopaths to a world with them, but strongly prefers a world with psychopaths to death. He is confident only a psychopath would press. If his credence of being a psychopath is fixed at a moderate value, pressing looks good, since it would kill the psychopaths. Egan says nearly everyone thinks Paul should not press. The fix again requires conditioning credences on his own tendencies, which is the revision just discussed.

## 7. Positive case and negative case

For CDT: the decision should depend on what the act does. Correlation without causal influence (the charisma case, a medical correlation between a gene and a choice) should not be bought or avoided by the act itself. Surveyed philosophers prefer CDT to EDT, as the source notes.

Against CDT: it can give recommendations that systematically lose money, which suggests a violated principle of guaranteed payoff (Spencer's argument) or a Dutch book. EDT, for its part, has its own failures, such as "managing the news" in the charisma case.

## 8. Open questions

1. **Computing counterfactuals.** The theory underdetermines the semantics. Imaging, causal-model interventions, and dependency hypotheses are candidates; the regress concern applies most to imaging.
2. **Which credences to hold fixed.** Prior ones, or those updated on one's own deliberation? The first produces the counterexamples; the second makes CDT's verdicts approach EDT's in some cases, though not in all. Case analysis suggests the two still diverge when the act has no evidential relation to the dependency hypotheses beyond the agent's own inclinations.
3. **Policies versus acts.** The source speaks of acts. Evaluating policies by their causal consequences, including through predictors who model the policy, is a different proposal, closer to later theories, and I do not attribute it to the source.

## 9. A procedure for unfamiliar cases

1. List the acts and outcomes.
2. Identify the causal structure and which variables the act can influence.
3. Specify dependency hypotheses K and credences P(K), asking whether the agent's inclinations should already be reflected in them.
4. Compute U(A) = Σ_K P(K) Σ_j P(O_j | do(A), K) D(O_j).
5. Check stability: does the recommended act change your credences so that another act now looks better? If so, apply ratifiability or equilibrium reasoning.

## 10. Conclusion

CDT evaluates acts by their expected causal effects, with counterfactual rather than conditional probabilities. That makes it immune to spurious correlation, as in King David, and it two-boxes in Newcomb's problem. Its difficulties are that the counterfactual semantics is unspecified, and that fixing prior credences in dependency hypotheses produces unstable or money-losing verdicts when the world responds to the agent's dispositions. Defenders answer with evidence-sensitive credences and ratifiability; critics read the cases as showing that causal expectation is the wrong target. For a reader deciding unfamiliar cases, the useful discipline is to make the causal model and the credence assumptions explicit before computing.

**References** (as cited in the source): Gibbard & Harper (1981); Lewis (1976, 1979, 1981); Egan (2007); Joyce (2012); Spencer (2020); Oesterheld & Conitzer (2021); Weirich, *SEP* "Causal Decision Theory."