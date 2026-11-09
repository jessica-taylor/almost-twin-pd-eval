# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00001

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a716745a-39f3-4717-99a4-f31c8e7ce95a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a716745a-39f3-4717-99a4-f31c8e7ce95a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definitions, Computation, and Where It Strains

## 1. The core idea

Causal decision theory (CDT) says that a rational agent facing a set of acts should choose the one with the best *expected causal consequences*. The key word is "causal." Evidential decision theory (EDT) asks, "How good is the news that I did A?" CDT asks, "How good would things be if I did A?" The two questions come apart when an act is correlated with a good or bad outcome without causing it.

The source's informal example is an apple of unknown quality. You do not know the causal effect of eating it, so you weight the effects by your credence that the apple is good or bad. Uncertainty about causal structure and about the state of the world is handled by taking an expectation, not by ignoring causation.

## 2. Formal definition

The source gives the Gibbard–Harper formulation. For an act A and outcomes O_j,

U(A) = Σ_j P(A □→ O_j) · D(O_j),

where D is the desirability of an outcome and P(A □→ O_j) is the probability of the counterfactual "if A were performed, O_j would result." (The source writes the arrow as →.) CDT recommends the act maximizing U.

EDT replaces P(A □→ O_j) with P(O_j | A). The source notes that these differ in general. Lewis's triviality results show that the probability of a conditional cannot in general be a conditional probability. Gibbard and Harper showed that if two axioms hold, one involving conditional excluded middle, then independence of A and (A □→ O_j) makes the two quantities equal. So CDT and EDT agree exactly when the act carries no evidence about the relevant counterfactuals.

### A state-partition version (my gloss)

The source does not give this, but it is the form most readers will use. Partition the possibilities into *dependency hypotheses* K, each a maximally specific account of how outcomes depend causally on your acts, including everything outside your influence. Then

U(A) = Σ_K P(K) · Σ_j P(O_j | A, K) D(O_j).

The crucial feature is that the weights are the *unconditional* P(K), not P(K | A). Within a cell K, the act's causal effect is fixed, so conditioning on A there is harmless. EDT would use P(K | A). Egan's complaint, quoted in the source, is aimed at this feature: CDT "holds fixed the agent's unconditional credences in dependency hypotheses."

This is my operationalization of the counterfactual probabilities. It is a standard one, but the source itself leaves the algorithm open.

## 3. Worked examples

### King David and Bathsheba (from the source)

Summoning Bathsheba is unjust. Revolt risk depends on David's unknown charisma type, not on the act. Unjust acts do not cause revolts, but they are evidence of an uncharismatic king.

Take illustrative numbers. Let the cells be K₁ (charismatic, revolt probability 0.1) and K₂ (uncharismatic, revolt probability 0.6). Suppose P(K₁) = 0.5. Let Bathsheba be worth +3, a revolt cost −10, and the baseline be 0.

- **CDT:** the revolt risk is the same under both acts, as the cell weights are held fixed. Summoning gains +3 and the revolt term is identical. So CDT recommends summoning.
- **EDT:** summoning is evidence of K₂, so P(K₂ | summon) might be 0.8. The expected revolt cost then exceeds that under abstaining, where P(K₂ | abstain) might be 0.2. With these numbers, summoning has expected value 3 − 10(0.2·0.1 + 0.8·0.6) = 3 − 5.0 = −2.0, and abstaining has −10(0.8·0.1 + 0.2·0.6) = −2.0. Make the correlation a little stronger and EDT abstains. The source reports that EDT abstains and CDT summons, which is the intended structure.

The lesson is that CDT does not treat the act as a symptom of the cause of the revolt. It treats the act as an intervention on a variable that is not downstream of charisma.

### Newcomb's problem (from the source)

Box A holds $1,000. Box B holds $1,000,000 if the predictor predicted one-boxing, and nothing otherwise. Let the dependency hypotheses be K_full (B is full) and K_empty, with credence q in K_full. Then

U(two-box) = q(1,001,000) + (1−q)(1,000),
U(one-box) = q(1,000,000) + (1−q)(0).

Two-boxing dominates by exactly $1,000 for every q. So CDT two-boxes, because the prediction is already fixed. EDT instead uses P(K_full | one-box) ≈ 0.99 and P(K_full | two-box) ≈ 0.01, giving roughly $990,000 against $11,000, so it one-boxes. Two-boxers walk away with $1,000 and one-boxers with $1,000,000 (typically). That is the standard "why ain'cha rich?" objection. The CDT reply is that the rich were offered a different, better game: the money was placed before the choice, and the two-boxer faces a box that is empty and would be no fuller had she taken it alone.

## 4. Counterfactuals: the open problem

The source stresses that CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities." It describes Lewis's imaging proposal. For each world w, find the closest world w_A where A holds, and move w's probability mass there. Then P(A □→ O) is the mass that ends up on O-worlds.

Imaging differs from conditioning. Conditioning *renormalizes* over A-worlds, which is why it carries evidential information about other variables. Imaging *transports* each world to its nearest A-world, so the Newcomb-box state (already set) tends to be preserved.

The source also records a regress objection: to image, one must know what one would believe given certainty in A, and that is itself a conditional with credence below 1.

### An operational interpretation (my proposal, beyond the source)

In practice a reasonable resolution is to use a causal model in the style of structural equations and interventions. Represent the situation as a causal graph with variables V, and define

P(A □→ O) := P(O | do(A)),

obtained by deleting the equations that determine the act variable and setting it to A, while leaving the other equations and the exogenous priors unchanged. This gives a concrete, checkable procedure:

1. Draw the graph, including common causes (charisma → act, charisma → revolt; or predictor's model → prediction and → act).
2. Fix the prior over background variables.
3. For each act, compute the post-intervention distribution over outcomes.
4. Take expected desirability and maximize.

This avoids the regress, since "closeness" is replaced by a model, but it moves the burden onto the modeling. The intervention reading is faithful to the source's phrase "holding fixed our initial views about the likely causal structure." It is a proposal, not something the source commits to. In particular, it assumes the agent's act variable can be treated as having no *evidential* parents once intervened on, which is the very assumption disputed by critics.

## 5. When the agent's own credences move: deliberation

Here the source points to a real subtlety. In Newcomb-like cases with predictors, the agent may have information about what she is inclined to do. Joyce, per the source, argues that CDT can take "information about what one is inclined or likely to do as evidence." Operationally, the dependency-hypothesis credences P(K) should be the agent's *current* credences, which can update during deliberation as she learns about her own tendencies. This matters in the following cases.

### Death in Damascus

Death predicts where you will be and waits there. Suppose you may go to Damascus or Aleppo, and Death is reliable. If you are currently leaning to Damascus, you believe Death is probably in Damascus, so CDT says go to Aleppo. But once you lean to Aleppo, you believe Death is in Aleppo, and CDT says go to Damascus. Each act is unstable under its own expected-utility evaluation, since each act looks bad given the credences it induces. The source says CDT "would be unable to process the correlation." The more charitable account is that CDT needs a supplementary equilibrium notion, such as *ratifiability* (Harper's paper is cited), or a deliberational dynamic that settles at mixed credences. For instance, with symmetric credence 0.5 the two acts tie. This is one of several proposals, and the source does not choose among them.

### Psychopath Button

Paul thinks only a psychopath would press the button, and he prefers a world with psychopaths to dying. If his unconditional credence that he is a psychopath is low, say 0.01, then pressing has causal expectation about 0.99·(+large gain) + 0.01·(death). So CDT presses. Yet his pressing would be strong evidence that he is a psychopath. Egan says nearly everyone thinks he should refrain. A defender replies that Paul should first update on his own inclination to press: if he finds himself inclined to press, his credence in being a psychopath rises, and the causal expectation of pressing falls. The disagreement is over which credences count as "unconditional" at the moment of choice.

## 6. Adversarial offers and money pumps

The source cites Oesterheld and Conitzer's Adversarial Offer. Two boxes cost $1 each, and the seller put $3 in each box she predicted the buyer would *not* buy. Her prediction is accurate with probability 0.75, and the buyer shares that belief.

CDT reasoning: let p be your credence that you buy box 1 and let your credence for box 2 be similar. Box i contains $3 with probability equal to the chance the seller predicted you would not buy it. Since the seller predicted at most one box, at least one box is predicted "not bought" and so holds $3. Pick the box with the higher causal credence of being filled. That credence is at least 1/2, so the expected content is at least $1.50, exceeding the $1 price. So CDT buys.

But conditional on buying box i, the box is full only about 25% of the time, so the expected content is $0.75 and the purchase loses $0.25 on average. The seller profits from CDT buyers.

Defenders will say that the buyer should adjust credences as inclination forms. If she is inclined to buy box 1, she thinks box 1 is probably empty and box 2 is probably full, and she switches. The resulting instability again resembles Death in Damascus. The criticism is that, in equilibrium, CDT either dithers or loses money, and that this is exploitable by a diachronic Dutch book. The source reports this criticism without adjudicating it.

## 7. The twin prisoner's dilemma

Lewis argued that the prisoner's dilemma is a Newcomb problem. With a twin whose choice is highly correlated with yours but not caused by it, cooperation brings the twin's cooperation as *evidence*, not as a consequence. Defection dominates causally, so CDT defects. Two CDT agents each get the mutual-defection payoff, which is worse for both than mutual cooperation. Again, whether this is a failure of rationality or merely a bad situation is exactly the issue the source flags as disputed: philosophers disagree, though the source reports that most prefer CDT when forced to choose between CDT and EDT.

## 8. A checklist for unfamiliar cases

1. **Identify the acts** and the outcomes that matter.
2. **Identify what the act can and cannot influence.** Anything already settled or causally upstream of the act is not changed by it.
3. **Build dependency hypotheses** (or a causal graph) and assign credences from the agent's current information, including any evidence about her own dispositions.
4. **Compute U(A)** by intervention or counterfactual, holding those credences fixed.
5. **Check stability.** If the credences change when you tentatively favor an act, and the ranking flips, the problem needs a ratifiability or deliberation-dynamics argument. Plain CDT does not decide this.

Rules of thumb: when the act has no evidential bearing on the dependency hypotheses, CDT and EDT agree. When a common cause drives both act and outcome (David), CDT ignores the correlation. When a predictor's output is fixed (Newcomb), CDT treats it as a state and dominance applies.

## 9. What is claimed and what is mine

From the source: the expected-causal-effects definition; the Gibbard–Harper formula; Lewis's result that conditional probability differs from the probability of a conditional; the David case; CDT's two-boxing; imaging and its regress; the Egan criticisms; the Adversarial Offer and Psychopath Button; Joyce's reply; the Oesterheld–Conitzer Dutch-book argument.

From me: the dependency-hypothesis formula, the do-operator interpretation, the numerical illustrations, the stability and deliberation analysis, and the checklist. The deliberational resolutions are contested and should be read as options, not as the settled content of CDT.

## 10. Conclusion

CDT is a family of commitments more than a single algorithm: evaluate acts by what they would bring about, weighted by credences about how the world is. Its strengths are clear in cases like King David, where it refuses to treat an act as a mere symptom. Its difficulties come from the same place: holding fixed credences that the act itself may be evidence about. Whether Newcomb, Death in Damascus, and the Adversarial Offer are refutations or merely hard environments depends on how one specifies the counterfactuals and the dynamics of self-knowledge. Both remain open, and a user of the theory should state those choices explicitly.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/c72a0713-a100-401c-a3e4-b8bfebd178d3/call_0/request.json)

[Authoritative raw response](../../../../../../runs/c72a0713-a100-401c-a3e4-b8bfebd178d3/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT as the essay describes it, my choice cannot causally affect what the other prisoner does. Their decision is a fixed background state, and the letters they could send are different in content from mine. The payoffs are:

- If the other keeps quiet: sending gives 0 years and staying quiet gives 2, so sending is better.
- If the other sends: sending gives 4 years and staying quiet gives 5, so sending is better.

Sending dominates in both cases. The other copy is a correlated twin, but that is evidence about their act, not a causal channel. CDT holds fixed my unconditional credence about what they do, so the correlation does not change the ranking. The deliberation-instability concern from the essay does not apply either, because dominance means the ranking does not flip under any credence about the other's choice.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/c72a0713-a100-401c-a3e4-b8bfebd178d3/call_1/request.json)

[Authoritative raw response](../../../../../../runs/c72a0713-a100-401c-a3e4-b8bfebd178d3/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT as the essay describes it, my choice cannot causally affect what the other prisoner does. The other prisoner's decision is a fixed state of the world for me.

Sending the letter gives me a lower sentence whichever state holds:
- If the other prisoner keeps quiet, I get 0 years by sending against 2 by staying quiet.
- If the other prisoner sends a letter, I get 4 years by sending against 5 by staying quiet.

Sending dominates in both states. The other copy is a correlated twin, but the essay treats that correlation as evidence rather than causal influence. It would be a mistake to let it shift my unconditional credence about their act. There is also no instability here of the Death in Damascus kind, because the dominance holds at every credence.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
