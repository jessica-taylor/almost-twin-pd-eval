# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. The key phrase is "causal." Where evidential decision theory (EDT) asks "how good is the news that I did A?", CDT asks "how good would things be if I were to do A?" The two questions diverge exactly when an act is correlated with an outcome without causing it.

The source article's informal example is the apple: if you don't know whether the apple is good or bad, you weigh the causal effect of eating it under each hypothesis by your credence in that hypothesis. The rest of the theory is about making "weigh the causal effects" precise.

*Source vs. me.* The definitions in §2 and the Savage-style and causal-model formulations in §3 follow the source (Gibbard–Harper, Lewis imaging) where it speaks. The causal-graph version, the discussion of deliberational dynamics, and the operational recommendations in §6 are my own elaborations or standard background, not claims of the article.

## 2. The Gibbard–Harper formula

Gibbard and Harper (1981) define the causal expected utility of an act A as

U(A) = Σ_j P(A □→ O_j) · D(O_j),

where the O_j partition the possible outcomes, D is desirability, and P(A □→ O_j) is the probability of the counterfactual "if I were to do A, outcome O_j would occur." (The source writes the arrow as →.) CDT says: pick A maximizing U(A).

Compare EDT, which uses V(A) = Σ_j P(O_j | A) D(O_j). The two agree if P(A □→ O_j) = P(O_j | A) for all relevant A and j. Lewis (1976) showed this identity cannot hold in general, as a matter of logic (his triviality results): no assignment of "probabilities of conditionals" can equal conditional probabilities across a class of probability functions closed under conditionalization, except trivial ones. So the counterfactual probability is a genuinely different quantity.

Gibbard and Harper showed that, given two axioms (one being conditional excluded middle), if A is probabilistically independent of the counterfactual A □→ O_j, then P(A □→ O_j) = P(O_j | A). The converse moral matters most: where the act is *not* independent of the counterfactuals, the theories can come apart.

## 3. Dependency hypotheses: a usable form

The counterfactual formula is easiest to use by decomposing over **dependency hypotheses** K: maximal specifications of how outcomes depend causally on the agent's acts, holding fixed everything outside the agent's causal influence. Then

U(A) = Σ_K P(K) · Σ_j P(O_j | K, A) D(O_j),

or, when K settles the outcome given A, simply U(A) = Σ_K P(K) D(outcome of A under K).

The crucial feature: the weights are the **unconditional** credences P(K), not P(K | A). This is the formal difference from EDT, which would use P(K | A). Egan's phrase for this is that CDT "holds fixed the agent's unconditional credences in dependency hypotheses."

A graph-based equivalent (my gloss, in the style of Pearl's do-operator): given a causal model, replace the equation for the act variable with A := a, and compute

U(a) = Σ_o P(o | do(a)) D(o).

This is the intervention reading of "if I were to do A." It makes the counterfactual probability computable whenever the causal structure and the relevant conditional probabilities are available. It also dissolves much of the worry below about vagueness, though it presupposes a causal model.

Lewis's **imaging** gives another computation: to evaluate P(A □→ O), move the probability of each world w to the closest world w_A where A holds, and sum the mass landing in O-worlds. Conditioning, by contrast, discards non-A worlds and renormalizes. Imaging keeps the "causal background" of w while changing the act; conditioning treats the act as evidence about that background.

## 4. Worked examples

### 4.1 King David and Bathsheba

This is the source's example. David is either charismatic (C) or not (¬C). Charisma is fixed and causally upstream of both his acts and the risk of revolt. Unjust acts (summoning Bathsheba) don't cause revolts; they merely correlate with uncharisma, which does.

Let the payoffs be: Bathsheba is worth +b, a successful revolt costs −r, with b small relative to r. Write ρ_C and ρ_¬C for revolt probabilities, with ρ_¬C > ρ_C, both independent of the act given the type.

- CDT: U(send) = b − P(¬C)ρ_¬C r − P(C)ρ_C r; U(abstain) = −P(¬C)ρ_¬C r − P(C)ρ_C r. The revolt terms are identical, so U(send) − U(abstain) = b > 0. Send.
- EDT: sending is evidence for ¬C, so P(revolt | send) > P(revolt | abstain). If the evidence is strong enough relative to b/r, abstain.

The source notes exactly this verdict split. Here CDT's answer is intuitively right: the act cannot alter his charisma.

### 4.2 Newcomb's problem

Box A holds $1,000; box B holds $1,000,000 iff the predictor predicted one-boxing. Let q = P(B is full), unconditional. Dependency hypotheses: full or empty, with no act dependence.

- U(two-box) = 1000 + q·10⁶
- U(one-box) = q·10⁶

Two-boxing dominates by $1,000 for every q, so CDT two-boxes. EDT with 99% accuracy gets V(one-box) ≈ 990,000 vs V(two-box) ≈ 11,000, and one-boxes. The source reports that philosophers typically prefer CDT in a forced choice between the two, while noting that two-boxers walk away with $1,000 and one-boxers with $1,000,000, which critics find damning. CDT defenders reply that the one-boxers were simply presented with a richer menu ("the rewards are for being the kind of agent predicted to one-box, and that was settled before the choice").

### 4.3 The Adversarial Offer

From the source (Oesterheld–Conitzer): two boxes cost $1 each; you may buy one or none; yesterday the seller put $3 in each box she predicted you would *not* buy; the prediction is right with probability 0.75.

CDT reasoning: let p be your credence that you buy box 1 (and p′ for box 2). Box 1 is full iff the seller predicted you wouldn't buy it. Before deciding, your credences in "box i contains $3" are 1 − (credence that you'll buy i, roughly). Since you buy at most one box, the two probabilities of containing $3 sum to at least 1, so for some box the causal expected content is ≥ $1.50 > $1. Buying it looks causally profitable.

Yet if you do buy box 1, the seller probably predicted that (accuracy 0.75), so box 1 is empty with probability 0.75, and your expected return is 0.25·3 − 1 = −$0.25. Notably, the CDT agent buys *knowing* the policy loses money on average. Here the dependency hypotheses' unconditional credences are the issue: they are not updated by the act. The example shows the cost of "holding fixed" credences that one has good reason to expect will shift once one learns what one will do.

## 5. Unstable cases: Death in Damascus and the Psychopath Button

In Death in Damascus, Death predicts where you'll be tomorrow (Damascus or Aleppo) and waits there. If you are leaning toward Damascus, you believe Death is probably in Damascus, so CDT says go to Aleppo; but then you expect Death in Aleppo, and so on. The act's causal expected utility depends on your credences, which depend on your current inclination. No act is **ratifiable** (Harper's term in the source's references: an act is ratifiable if it maximizes U conditional on being chosen). The naive procedure oscillates.

The Psychopath Button has the same structure. Paul believes only psychopaths press. If he presses, the causal effect on the world's psychopaths is that they all die, including himself if he is one. CDT with his unconditional credence that he is not a psychopath (perhaps moderate) can favor pressing; Egan says nearly everyone judges this wrong, since pressing is strong evidence he is a psychopath.

Joyce's defense (cited in the source) is that CDT is not committed to ignoring such evidence: information about one's own inclinations can be treated as evidence that changes P(K) *during deliberation*. Then the right recommendation is the output of a deliberative equilibrium, not of the first-pass calculation. I find this a coherent repair, with a cost: the theory now needs a theory of how credences evolve while deliberating, and in genuinely unstable cases it may return only a mixed or "ratifiable" recommendation rather than a unique act.

## 6. The vagueness problem, and an operational reading

The source flags that CDT doesn't itself specify how to compute counterfactual probabilities, and that Lewis's imaging requires knowing what we'd believe if certain of A, itself a conditional, threatening regress.

My proposal for practical use (beyond the source):

1. **Specify a causal model.** List the variables, including the act and any upstream common causes (type, disposition, predictor's information).
2. **Fix dependency hypotheses K** as the possible values of variables not downstream of the act, with prior P(K).
3. **Update P(K) on everything the agent actually knows**, including evidence about her own dispositions, *before* intervening. This is Joyce's point and avoids the crudest failures.
4. **Intervene:** compute U(a) = Σ_K P(K) E[D | K, do(a)].
5. **Check ratifiability:** if the maximizer's recommendation changes once the agent conditions on choosing it, iterate. Report equilibrium acts or mixtures.

This turns the regress into a fixed-point computation, and the model-relative choice of what counts as "downstream of the act" becomes an explicit input. The cost is that results are only as good as the model; reasonable people can disagree about whether a predictor's accuracy is a downstream or upstream feature, and the theory's verdict in Newcomb depends on that classification.

## 7. Criticisms, assessed

- **"CDT loses money"** (Newcomb, Adversarial Offer, Spencer; Oesterheld–Conitzer's diachronic Dutch book arguments). These arguments show CDT agents do worse on average in problems where the environment rewards a policy. The CDT reply: the environment rewards irrationality or pre-set dispositions, and "doing well" is not the same as "choosing well given the situation." The difficulty is that the Adversarial Offer lacks an obviously favored-for-irrationality structure; the seller wins by simply reading a CDT agent's reasoning, and that is harder to dismiss.
- **Egan's diagnosis:** the conflict is between "do what you expect to bring about the best results" and CDT's algorithm. The two readings diverge exactly when an act is evidence about dependency hypotheses.
- **Vagueness:** discussed above; the causal-model reading mitigates but doesn't eliminate it.

## 8. Conclusion

CDT evaluates acts by U(A) = Σ P(A □→ O_j)D(O_j), equivalently by intervening on the act in a causal model and averaging over dependency hypotheses with credences that are *not* conditioned on the act. This is why it sends for Bathsheba and two-boxes: it refuses to treat correlation as influence. Its strength is a principled answer to common-cause cases; its weakness is that the same refusal yields apparently self-defeating verdicts when the agent's own act is strong evidence about her situation. A practical CDT user should model causal structure explicitly, update on self-knowledge before intervening, and check ratifiability. Whether that repaired theory is fully adequate remains contested.

**References (as cited in the source):** Gibbard & Harper (1981); Lewis (1976, 1981); Egan (2007); Joyce (2012); Oesterheld & Conitzer (2021); Spencer (2020); Shaffer (2009); Weirich, *SEP* "Causal Decision Theory."