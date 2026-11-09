# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. The key word is "causal." Many things correlate with my acting that my acting does not bring about. CDT asks what my act will bring about, not what my act will indicate. Its rival, evidential decision theory (EDT), ranks acts by what they indicate, that is, by the news value of learning that I performed them.

Formally, both theories maximize an expected utility. They differ in which probability they feed in. For acts A and outcomes O_j with desirabilities D(O_j):

- EDT: V(A) = Σ_j P(O_j | A) D(O_j)
- CDT (Gibbard–Harper): U(A) = Σ_j P(A □→ O_j) D(O_j)

Here A □→ O_j is the counterfactual "if I were to do A, O_j would result." The source writes it with an arrow and describes P(A → O_j) as the probability that A "necessarily implies" O_j. I read this as a counterfactual and not a material conditional. With a material conditional, any act I am confident I will not perform would look good, since A ⊃ O is trivially true when A is false.

The source claims that this is the formal statement. The rest of this essay mixes source claims with my own operational proposals, and I flag which is which.

## 2. Why the conditional probability is not the counterfactual probability

If P(A □→ O) always equaled P(O | A), CDT and EDT would coincide. Lewis (1976) showed that no single "probability of a conditional" can equal the conditional probability across a class of probability functions closed under conditionalization, unless the functions are trivial (at most four-valued). So the identification fails in general.

Gibbard and Harper showed when it does hold. Given two axioms, one tied to conditional excluded middle, **if A is probabilistically independent of the counterfactual A □→ O_j**, then P(A □→ O_j) = P(O_j | A). So the theories diverge exactly when the act is evidence about which counterfactuals are true, that is, about the causal structure or background state.

## 3. A practical reformulation: dependency hypotheses

The source leaves the computation of counterfactual probabilities unspecified. A common and useful operational move, which I adopt here as a proposal, is to partition by **dependency hypotheses**. A dependency hypothesis K is a maximally specific proposition about how outcomes depend causally on the agent's acts. Then:

U(A) = Σ_K P(K) · Σ_j P(O_j | A, K) D(O_j),

where P(K) is the *unconditional* credence in K. If K fixes the causal facts, the inner probability is the chance of O_j under act A given K.

The contrast with EDT is clear. EDT would weight by P(K | A). CDT weights by P(K), "holding fixed" the agent's prior views about causal structure (this is the phrase Egan criticizes). When K is a causal-graph structure with background variables, this is Pearl's do-operator: U(A) = Σ_o P(o | do(A)) D(o). Pearl-style intervention is one concrete algorithm for the counterfactual probability. It sets A by surgery, deleting arrows into A, so that evidence flowing backward from A to its common causes is cut.

**Procedure for an unfamiliar case:**
1. List the available acts.
2. Identify the causal structure: which variables are downstream of the act, and which are upstream or independent.
3. Fix credences over the states or dependency hypotheses that the act cannot influence.
4. For each act, compute the expected utility with those state credences unchanged.
5. Pick the maximum.

## 4. Worked examples

**Apple.** The apple is good with probability p. Eating yields happiness h if good and −s if bad. U(eat) = ph − (1−p)s, to be compared with not eating. The state (good or bad) is causally independent of my choice, so CDT and EDT agree.

**King David.** Let C be "charismatic." The source's story: revolt risk depends on charisma, not on the unjust act. Say P(C) = c, and the revolt probability is r_C for charismatic and r_U for uncharismatic kings, with r_U > r_C. Summoning Bathsheba gives a gain g and costs the revolt loss L if revolt occurs. Then

U(summon) − U(abstain) = g − 0, because the revolt probability (c·r_C + (1−c)·r_U) is the same under both acts.

CDT recommends summoning whenever g > 0. EDT sees that summoning is evidence of being uncharismatic (since uncharismatic kings act unjustly), which raises the apparent revolt risk, so it can recommend abstaining. The fixed variable is exactly the one the act cannot change.

**Newcomb.** Let S₁ be "box B is full." Take the box B payoff as $1,000,000 and box A as $1,000. Let q = P(S₁), held fixed by CDT.

- U(one-box) = q · 10⁶
- U(two-box) = q · 10⁶ + 1000

Two-boxing dominates by $1,000 for every q. CDT two-boxes. EDT, with 99% accuracy, computes V(one-box) = 0.99·10⁶ and V(two-box) = 0.01·10⁶ + 1000, and one-boxes. The dispute is whether the 99% correlation counts as something the act controls. CDT says no, because the prediction is already settled.

**Prisoner's dilemma with a twin.** Defecting dominates causally. If my twin's choice is highly correlated with mine but not caused by it, CDT defects (Lewis 1979 treats this as a Newcomb problem), while EDT cooperates.

## 5. Stress cases and the ratifiability issue

The source lists cases where CDT seems to misfire. These show that "hold fixed prior credence" is subtle when the agent has evidence about her own tendencies.

**Death in Damascus.** Death predicts where I will be and waits there. Suppose I think Death is accurate. If I am leaning toward Aleppo, I should expect Death in Aleppo, so Damascus looks better, and vice versa. Every pure act is unstable. The CDT value of each act depends on my current credence about what I will do, because that credence determines my credence about Death's location. The source says CDT "would be unable to process the correlation." That overstates matters: CDT can process the correlation as evidence about the state, but a naive version that fixes the initial credences ignores that credences shift as I deliberate.

*Operational interpretation (mine, following the deliberational-CDT literature, notably Joyce and Harper's ratifiability work).* Let π be my credence about my own act. Define U_π(A) as above, using state credences induced by π. An act-credence is an equilibrium if it puts weight only on acts that maximize U_π. For Death, the unique equilibrium is the mixed π = (½, ½), under which both cities have equal expected utility. This also matches Joyce's remark that CDT can use information about one's own inclinations as evidence. Whether the equilibrium is the right output of "CDT" is contested, since randomization still leaves the expected survival probability at ½ while a perfect predictor of the randomization outcome would not exist.

**Psychopath Button.** Paul believes only psychopaths press the button, and he prefers a world with psychopaths to dying. The naive CDT calculation uses his prior probability that he is a psychopath, which may be small. Pressing then looks good, because it eliminates psychopaths and he probably survives. But once he considers pressing, his credence that he is a psychopath should rise, so the deliberational version flips the verdict and says do not press. This gives an example where the choice of CDT variant matters for the conclusion. Egan's criticism targets the naive, fixed-credence version.

**Adversarial Offer (Oesterheld–Conitzer).** Two boxes cost $1 each, and the seller put $3 in each box she predicted I would not buy, with accuracy 0.75. Let b be my credence that I buy box 1 and 1−b my credence that I buy box 2 (suppose I always buy one). Under a fixed credence about the contents, CDT reasons that the contents satisfy: box 1 holds $3 with probability 1 − 0.75 if I buy it, but since the seller's prediction is fixed, my credence that box 1 is full is 0.75(1−b)+0.25b ... let me state it properly. If I buy box 1, the seller predicted that with probability 0.75, so box 1 is full with probability 0.25. If I buy box 2, box 1 is full with probability 0.75. Averaging by my credences, the expected content of box i is at least 1.5 for at least one i whichever way I lean, and so CDT recommends buying some box. Yet every purchase yields an expected net of 0.25·3 − 1 = −0.25 for the box chosen. The CDT calculation is evaluated at the credences held before choosing. This is the reasoning "at least one box contains $3, so average value ≥ $1.50 > $1." The diachronic complaint is that a bookie who knows this can reliably extract money. The deliberational variant escapes in the sense that the equilibrium credence b = ½ makes both boxes' expected content 0.5·3 = 1.5 ... Under b = ½ each box has credence 0.5 of being full, and expected causal value 1.5 > 1, so buying remains recommended. This means ratifiable CDT still buys and loses 0.25 in expectation relative to declining. I therefore think the case is a real problem for CDT in either form, and I note the disagreement: defenders reply that the loss is the cost of facing a predictor who rewards irrationality, while critics say a losing policy cannot be rational.

## 6. Acts versus policies

The source discusses individual acts. When the same agent faces a decision repeatedly, or when a predictor reads the agent's *decision procedure*, evaluating acts one at a time can differ from evaluating policies. CDT evaluates the *act at the moment of choice*, treating earlier predictions as fixed. Evaluated *before* the predictor acts, the policy "one-box" causally produces the million, since the predictor's inputs depend on the policy. This is why a CDT agent who can precommit would precommit to one-boxing, and why critics say CDT is dynamically inconsistent. This paragraph is my own gloss, not the source's.

## 7. Open problems the source flags

1. **Vagueness.** CDT does not itself say how to compute P(A □→ O). Lewis's imaging proposal moves each world's probability mass to the closest A-world. But "closest" depends on what I would believe if certain of A, which is another conditional, so there is a regress. Causal graphs avoid this when a model is supplied, but then the modeling choice carries the philosophical weight.
2. **Counterexamples.** Egan argues that "do what you expect will bring about the best results" and "hold fixed unconditional credence in dependency hypotheses" come apart. Defenders (Joyce) reply that proper CDT uses evidence about one's own tendencies.
3. **Money pumps.** Oesterheld and Conitzer argue that CDT agents can be diachronically Dutch-booked.

## 8. Conclusion

CDT scores each act by its expected causal effects, with probabilities of counterfactuals in place of conditional probabilities. It differs from EDT exactly where an act is evidence about causally upstream facts it cannot change, as in King David, Newcomb, and twin prisoner's dilemmas. Computationally, it holds fixed credences over dependency hypotheses and intervenes on the act. The theory's difficulties concentrate in cases where the agent's credences about her own choice feed back into the states, such as Death in Damascus, the Psychopath Button, and the Adversarial Offer. There, the answer depends on whether one uses the naive or the deliberational version, and in some cases (the Adversarial Offer) both versions seem to recommend a losing act. A reader applying CDT should therefore state explicitly the causal model, the credences held fixed, and whether those credences update during deliberation.