# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. The apple example in the source is the simplest case. If you are unsure whether the apple is good, you weight the causal effects of eating it by your credences about how the world is arranged.

The informal slogan hides the main technical question: what does "causal consequences in expectation" mean when the agent is uncertain about the very causal structure that links acts to outcomes? The rest of this essay answers that question, shows how it separates CDT from evidential decision theory (EDT), and marks where the source leaves things open and where I add proposals of my own.

## 2. The formal definition (Gibbard–Harper)

The source gives the Gibbard–Harper formula. For an act A and outcomes O_j,

U(A) = Σ_j P(A □→ O_j) · D(O_j),

where D is desirability and P(A □→ O_j) is the probability of the counterfactual "if A were performed, O_j would result." The rational act maximizes U.

EDT replaces the counterfactual probability with the conditional probability P(O_j | A). The two are different objects. Lewis's triviality results, cited in the source, show that the probability of a conditional cannot in general be a conditional probability, so one cannot treat CDT as EDT in disguise. Gibbard and Harper showed that with two axioms (one involving conditional excluded middle), if A is probabilistically independent of the counterfactual A □→ O_j, then the two quantities coincide. CDT and EDT diverge exactly where acts and counterfactuals are correlated.

## 3. An operational reformulation: dependency hypotheses

The source stresses that CDT does not say how to compute counterfactual probabilities. A standard operational route, which I will adopt, is partition by *dependency hypotheses* (Lewis 1981). A dependency hypothesis K is a maximally specific proposition about how outcomes depend causally on the agent's acts, covering things outside the agent's control. Then

U(A) = Σ_K P(K) · Σ_j P(O_j | K, A) · D(O_j).

Under each K, the act's causal influence is fixed, so conditioning on A within K adds no spurious evidential news. The crucial feature is that the weights are the unconditional credences P(K), not P(K | A). This is Egan's point in the source: CDT "holds fixed the agent's unconditional credences in dependency hypotheses." EDT would weight by P(K | A) instead.

If the K are causally upstream of A and can be treated as the states of the world, this is Savage-style expected utility with states that are causally independent of acts. If the states are not independent of the acts causally, they are not appropriate "states" in this formula; the K are chosen to restore that independence.

*Note on status.* The source only gives the counterfactual formula. The K-partition is the standard Lewis/Skyrms reading, which I treat as the operational interpretation. It also sidesteps the triviality problem, since only ordinary probabilities of K and of outcomes given K and A are needed.

## 4. Worked cases

### 4.1 King David

Let C be "David is charismatic." Charisma is fixed, correlates with justness and with revolt, and the act of summoning Bathsheba does not cause revolt. Suppose, with illustrative numbers:

- Summoning: gain g from Bathsheba; revolt costs r.
- P(revolt | C) = 0.05, P(revolt | ¬C) = 0.6, regardless of the act (given the type).
- P(C) = 0.5, but P(C | summon) is lower because summoning is an unjust act, which is evidence of uncharismatic type.

EDT uses P(revolt | summon), which is high, and may advise abstaining. CDT uses K = C or ¬C with fixed weights 0.5. Revolt probability is 0.325 whether or not he summons, so the revolt term cancels and U(summon) − U(abstain) = g > 0. CDT says summon. This matches the source.

### 4.2 Newcomb's problem

Let K₁ be "box B contains $1,000,000" and K₂ "box B is empty." The act cannot change which holds. Let p = P(K₁). Then

U(two-box) = p(1,001,000) + (1−p)(1,000),
U(one-box) = p(1,000,000).

So two-boxing wins by exactly $1,000 for every p. CDT two-boxes. EDT, using P(K₁ | act) ≈ 0.99 for one-boxing, one-boxes. The source notes that CDT agents therefore typically get $1,000 and not $1,000,000, which is the central complaint against it.

### 4.3 The Adversarial Offer

Two boxes cost $1 each. The seller puts $3 in each box she predicted you would *not* buy; the prediction is right with probability 0.75, and you know this.

Let q be your credence that you buy box 1. Take your credence that box 1 contains $3 to be ≈ 1 − (your credence that the seller predicted you would buy it). If you are 50/50 between the boxes, each box contains $3 with probability 0.5, so causal EV is $1.50 − $1 = $0.50 > 0 for either box. CDT says buy. Evidentially, though, conditional on buying a box, it has $3 only with probability 0.25, so EV = 0.75 − 1 = −$0.25. A CDT agent reliably loses money on average to the seller.

Two features of my analysis deserve flag. First, it matters that your credences about the prediction update as you deliberate. If you become confident you will buy box 1, then you should believe box 1 is probably empty and box 2 probably full, so buying box 2 looks causally better, and then the reverse. There is no stable pure-act deliberation equilibrium, only a mixed one. Second, in a mixed equilibrium (probability ½ each, with the credences matching) each purchase has causal EV $0.50 in the arithmetic above, so even at equilibrium CDT still says buying beats abstaining. This is why the case is regarded as a real problem and not an artifact of instability.

## 5. Deliberational dynamics and instability

Death in Damascus shows a feature the source mentions only briefly. Death predicts your location, Damascus or Aleppo, and waits there. Suppose you strongly believe the prediction is accurate. If you are inclined toward Damascus, you expect Death there, so Aleppo looks better causally. Once you lean to Aleppo, Damascus looks better. No pure act is *ratifiable*, meaning that it is optimal given the credences you would have upon deciding on it.

The source reports that "a CDT agent would be unable to process the correlation." That is too strong, and Joyce's reply (also in the source) is that CDT can use information about one's own inclinations as evidence about the dependency hypotheses. The version I defend:

1. Deliberation is a process in which credence P_t(K) is updated by evidence about what you are inclined to do.
2. CDT evaluates acts relative to P_t.
3. A decision is stable when it maximizes causal EV under the credences it itself induces (Harper/Arntzenius/Joyce-style equilibrium).

In Death in Damascus the stable state is the mixed one: probability ½ each, with a credence of ½ on Death's location. At this point the agent is indifferent. This yields a coherent answer, but it is an addition to the source's formula, which on its face does not mention deliberational updating. Different CDT theorists disagree about whether a mixed act is really available (a randomizing device that Death cannot predict would change the problem).

## 6. The Psychopath Button

Paul thinks only psychopaths would press the button. Pressing kills all psychopaths. If Paul's credence that he is a psychopath is, say, 0.9 before deliberation, then pressing causes death (if he is one) or a better world (if not). With the unconditional credence fixed at a low value, CDT presses. If Paul's credence responds to his inclination (Joyce's route), then as he leans to press, he becomes confident he is a psychopath, and pressing then looks fatal. So the stable verdict is not to press, matching the intuition Egan reports.

So the apparent counterexample depends on whether the credences in the dependency hypothesis are held fixed at their pre-deliberation values. The source's quote from Egan identifies that as the culprit, while Joyce's defence amounts to denying that CDT must freeze them. I regard the second reading as the more defensible operational interpretation, but it makes the Adversarial Offer harder to dismiss: there, even at stable credences, CDT still buys.

## 7. The vagueness objection and imaging

The source notes that CDT leaves the counterfactual calculation open and mentions Lewis's *imaging*. For a credence function P and act A, the image P^A moves the mass of each world w to the closest A-world w_A:

P^A(O) = Σ_w P(w) · [w_A ∈ O].

Then U(A) = Σ_j P^A(O_j) D(O_j). Imaging is a counterpart of conditioning that respects causal structure, and the dependency-hypothesis formula is the special case in which closeness holds fixed the K.

The regress objection in the source is that determining "closest A-world" requires knowing what you would believe given A, which is itself a conditional. My view is that in structured models this is harmless. Pearl's do-operator gives an explicit algorithm: with causal graph G and structural equations, P(O | do(A)) is computed by cutting the arrows into A and setting A. Then

U(A) = Σ_o P(o | do(A)) D(o).

This does not eliminate the modelling problem, since the graph must come from somewhere, but it makes the dependence on that causal model explicit and locates the vagueness in the model rather than in the logic of conditionals. This is my proposal, not the source's.

For Newcomb, the graph has a common cause (the agent's disposition) pointing to both prediction and act. do(act) severs the disposition-to-act link and leaves the prediction untouched, which reproduces two-boxing. The model-relative character is a real feature. A "twin" prisoner's dilemma is similar. If the twin's choice is caused by the same algorithm, whether do(my action) should also change the twin's depends on whether one models the intervention at the algorithm or at the output. Standard CDT intervenes at the output.

## 8. Criticisms and how they bear on use

The source records three kinds of objection.

- **Intuition-based:** Newcomb, Psychopath Button.
- **Money-pump-based:** Adversarial Offer and related cases (Spencer, Oesterheld and Conitzer). CDT agents knowingly accept bets that lose in expectation, and diachronic Dutch books against them are possible.
- **Formal vagueness:** the counterfactual algorithm.

The standard CDT reply to the first two is "why ain'cha rich?": the predictor rewarded irrational dispositions, and CDT evaluates acts, not dispositions. The money-pump cases are harder, since the loss there is not obviously due to a reward for a disposition. I take the Adversarial Offer to be the strongest objection in the source, because it is a repeatable setup where the causal and the average outcomes diverge under common knowledge.

## 9. A procedure for unfamiliar cases

1. List the acts available at the time of choice.
2. Build the causal model, including everything that depends on you and everything that does not.
3. Identify the dependency hypotheses K, those facts that are causally independent of the act yet matter to outcomes.
4. Estimate P(K) at the credences you hold upon deciding (including what your inclination is evidence of, if you accept the Joyce-style reading).
5. Compute U(A) = Σ_K P(K) Σ_j P(O_j | K, A) D(O_j).
6. If the best act changes as credences update, look for a stable (ratifiable, possibly mixed) credence–choice pair.
7. Sanity check: if the verdict differs from EDT, find which correlation is non-causal, and confirm that it really is.

## 10. Conclusion

CDT evaluates acts by the expected value of what they would bring about, holding fixed what they cannot influence. Formally, it uses counterfactual or interventional probabilities in place of conditional ones, and operationally it weights dependency hypotheses by credences that are not conditioned on the act. This explains its verdicts: summon Bathsheba, two-box. Its difficulties come from two places. The first is the choice of causal model and treatment of the counterfactual. The second is the question of whether credences are frozen or respond to deliberation, which determines whether cases like Psychopath Button and Death in Damascus are counterexamples. The Adversarial Offer suggests that even the more sophisticated version still has a systematic cost in settings with accurate predictors.

**References (selected, as in the source):** Gibbard & Harper (1981); Lewis (1976, 1981); Egan (2007); Joyce (2012); Oesterheld & Conitzer (2021); Spencer (2020); Shaffer (2009); Weirich, *SEP*, "Causal Decision Theory."