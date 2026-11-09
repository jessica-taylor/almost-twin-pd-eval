# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00018

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/01e58e63-cc10-4b1e-8e4b-61e55429b37b/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/01e58e63-cc10-4b1e-8e4b-61e55429b37b/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. Two ideas are packed into this. First, utility is computed as an expectation over uncertain states of the world. Second, what enters the calculation for an act is what that act would bring about, not what the act would merely be evidence for.

The apple example in the source makes the structure clear. If you do not know whether the apple is good or bad, you do not know the causal effect of eating it. You weight the effects of eating a good apple and of eating a bad apple by your credence in each. The uncertainty is about *how the world is causally set up*, and the act is evaluated against that uncertainty.

The rival, evidential decision theory (EDT), scores an act by how good the news of its performance would be. CDT and EDT diverge exactly when an act is correlated with an outcome without causing it.

## 2. The formal definition

The source gives the Gibbard–Harper formulation. For an act A and outcomes O_j,

U(A) = Σ_j P(A → O_j) · D(O_j),

where D is desirability and A → O_j is the counterfactual "if A were performed, O_j would result." The agent picks the act maximizing U. The source notes the quantity is a probability of a *counterfactual*, not a conditional probability.

EDT replaces it with

V(A) = Σ_j P(O_j | A) · D(O_j).

A standard equivalent presentation, which is **my gloss and not stated in the source**, uses *dependency hypotheses*. Let K range over a partition of maximally specific hypotheses about how outcomes depend causally on acts (the "causal structure" or "state"). Then

U(A) = Σ_K P(K) · u(A, K),

where u(A, K) is the utility of the outcome that A would produce if K were true. The probability weights P(K) are the agent's *unconditional* credences in the hypotheses, not credences conditional on A. This corresponds to the source's phrase, via Egan, "holding fixed the agent's unconditional credences in dependency hypotheses." In this form, the counterfactual probability is P(A → O_j) = Σ_K P(K)·[A produces O_j under K]. If K is deterministic about what each act yields, the bracket is 0 or 1. If K is chancy, it is the chance.

Compare EDT, which uses P(K | A). The whole disagreement is the difference between P(K) and P(K | A).

## 3. Why the counterfactual is not a conditional probability

The source mentions Lewis's 1976 triviality result: the probability of a conditional cannot in general equal the conditional probability. If P(A → O) always equalled P(O | A), CDT would collapse into EDT.

Gibbard and Harper show the two coincide under two axioms (one tied to conditional excluded middle) *plus* statistical independence of A and the conditional A → O_j. So the question is when A and its counterfactual consequences are probabilistically independent. When they are, CDT and EDT agree. When they are not, as when a common cause links the act to the outcome, they come apart.

## 4. A worked case: King David

In the source's example, charisma is a fixed trait that causes both unjust acts (such as summoning Bathsheba) and a "sneaky bearing" that causes successful revolts. Summoning her does not cause revolt.

Let the states be C (charismatic) and N (not). Suppose the following numbers, which are **mine, for illustration**: P(C) = 0.5; revolt probability is 0.05 under C and 0.5 under N, regardless of act; revolt has utility −10 and Bathsheba is worth +3 (the act is otherwise unaffected). Then:

- CDT: U(send) = 3 − 10·(0.5·0.05 + 0.5·0.5) = 3 − 2.75 = 0.25. U(abstain) = −2.75. So send.
- EDT: if sending is strong evidence of N (say P(N | send) = 0.9), V(send) = 3 − 10·(0.1·0.05 + 0.9·0.5) = 3 − 4.55 = −1.55, while V(abstain) with P(N | abstain) = 0.1 gives −10·(0.9·0.05 + 0.1·0.5) = −0.95. So abstain.

CDT's reasoning is that David cannot change his charisma, so sending dominates: under each state, sending is better by 3. EDT treats his act as a symptom of a bad trait and "manages the news." This is the typical pattern: CDT respects dominance across causal states when the act does not influence which state obtains.

## 5. Newcomb's problem

With a 99%-accurate predictor, box A holding $1,000, and box B holding $1,000,000 iff one-boxing was predicted, the states are B-full (F) and B-empty (E). Whatever P(F) is, two-boxing yields exactly $1,000 more in each state:

U(two) = 1000 + 10⁶·P(F) > U(one) = 10⁶·P(F).

So CDT two-boxes regardless of the predictor's accuracy, since P(F) is not shifted by the act in the calculation. EDT uses P(F | one) = 0.99 and P(F | two) = 0.01, giving V(one) ≈ 990,000 and V(two) ≈ 11,000. The causal theorist says the one-boxer is rewarded for a *disposition* held earlier, not for the choice, and that a person facing the already-fixed boxes does better by taking both. The evidentialist replies, "If you're so smart, why ain't you rich?" The source notes philosophers are divided, though a majority prefer CDT over EDT.

## 6. The operational question: how to compute the counterfactual

The source says CDT does not itself specify an algorithm for the counterfactual probabilities. It mentions Lewis's *imaging*. For each world w, move its probability mass to the closest A-world w_A. Then

P(A → O) = Σ_w P(w) · [w_A ∈ O].

The source also reports a regress objection (Shaffer): selecting the closest A-world requires knowing what you would believe or what would hold were you certain of A, which is itself a conditional of uncertain probability.

**A proposed operational interpretation (mine).** Instead of closeness among worlds, use an explicit causal model in the style of structural-equation or "do"-calculus models. The agent specifies:

1. variables, including the act X, with causal arrows;
2. equations or conditional distributions for each non-act variable given its parents;
3. a credence over uncertain parts of the model.

The counterfactual probability is then the intervention distribution: P(O | do(A)), obtained by cutting arrows into X and setting X = A while leaving the rest of the model intact. For a common-cause structure K → X, K → O, this gives P(O | do(x)) = Σ_K P(K) P(O | x, K), which equals the dependency-hypothesis formula of section 2. In Newcomb, the prediction is a causal ancestor of the box content and a (non-causal-to-act) correlate of the act, so intervening on the act leaves P(F) fixed.

Justification: this makes imaging concrete, since intervention is the "minimal change" that sets the act while keeping everything not downstream of it. It avoids the regress by taking the causal structure as an input to the problem rather than something derived from what you would believe given A. The cost is that the answer is only as good as the model, and that the choice of what counts as a "cause" and which variables to hold fixed is substantive. Different models of the same story can yield different recommendations. This is a real residual vagueness, not a solved problem.

## 7. The hard cases: when your own act is evidence about the state

The source's criticisms mostly concern cases where the agent's credence about the state shifts as she deliberates.

**Death in Damascus.** Death predicts where you'll be, Damascus or Aleppo, and waits there. If you are leaning toward Damascus, you expect Death to be in Damascus, so you prefer Aleppo; but then you expect Death in Aleppo. With unconditional credences held fixed, a naive CDT calculation is unstable: each option looks better given the credence induced by the other. The source says CDT "would be unable to process the correlation." Defenders like Joyce reply that CDT can use information about what one is inclined to do *as evidence*. That means credences over states should be updated as deliberation proceeds, and an equilibrium is sought. Harper-style *ratifiability* (**not described in the source beyond the citation**) requires an act to maximize U given the credences one would have upon deciding on it. Here no pure act is ratifiable; a mixed credence of 50/50 leaves the agent indifferent. This is a reasonable operational repair: *iterate deliberation until credences and preferences are in equilibrium*, and the dynamic version of CDT then recommends randomizing or being indifferent. Whether this is faithful to CDT or a modification is itself disputed.

**Psychopath Button.** Paul believes only psychopaths press the button, which kills all psychopaths, and he strongly prefers living. The pressing act is causally effective (it kills psychopaths, including him if he is one). If Paul's unconditional credence that he is a psychopath is low, CDT recommends pressing. But if he were to decide to press, he would become confident he is a psychopath, and therefore dead. Egan's verdict is that pressing is plainly wrong. A deliberation-sensitive CDT, updating on the inclination to press, avoids this, which matches Joyce's defense. A static CDT, holding the prior credence fixed, does not.

**Adversarial Offer.** Two boxes cost $1 each; the seller put $3 in each box she predicted you wouldn't buy; accuracy is 0.75. Static CDT argues that at least one box has $3 in it, so for some box credence in "contains $3" is at least 0.5, expected value at least $1.50, more than the $1 cost; buy. But whichever you buy, you expect 0.75 probability it is empty, so the expected return is $0.75, a loss of $0.25. With credences updated on your inclination, CDT also declines. Oesterheld and Conitzer present this and similar cases as extracting money from CDT agents and as exposing them to diachronic Dutch books. The defender's reply is again that a *sophisticated* CDT conditions its state credences on its own tentative leaning.

## 8. Using CDT on an unfamiliar problem: a procedure

1. **Identify the acts** available (and whether policies or single acts are being chosen; the source discusses acts).
2. **Draw the causal structure**, marking what the act can and cannot influence, including common causes and earlier predictions.
3. **Choose a partition of dependency hypotheses K** and assign credences.
4. **Compute u(A, K)** by intervening on the act.
5. **Check stability**: if P(K) would shift as you lean toward an act, recompute with the updated credences and look for a ratifiable or equilibrium choice. (This is my recommended step and the contested one.)
6. **Choose the act with the highest U**, or a mixture at equilibrium.

For a quick test, ask whether the act is *probabilistically correlated with the state but causally irrelevant to it*. If not, CDT and EDT agree and you can stop. If so, expect divergence, and CDT will prefer the act that dominates state by state.

## 9. What is claimed and what is assumed

From the source: the Gibbard–Harper formula; Lewis's triviality result and the independence condition; the David, Newcomb, Death in Damascus, Adversarial Offer, and Psychopath examples; the vagueness of the counterfactual algorithm, imaging and its regress; and Joyce's defense. From me: the dependency-hypothesis rewrite, the numeric David example, the intervention-model operationalization, and the deliberational-equilibrium procedure in step 5. Those are interpretations that many CDT writers share, but the source does not endorse them.

## 10. Conclusion

CDT evaluates acts by the expected value of what they would cause, holding fixed one's unconditional view of the causal facts that the act cannot affect. This yields dominance reasoning, two-boxing, and sending for Bathsheba. Its defenders see this as the only sound separation of influence from evidence; critics point to cases where agents seem predictably to lose. The most promising operational response models counterfactuals by interventions and lets credences about states update with one's own inclinations, which avoids several counterexamples. Whether the resulting theory still deserves the name, and whether it handles Newcomb-like cases to everyone's satisfaction, remains open.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ee7aaf53-b2bb-47e0-9fbf-1822e61a0dda/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ee7aaf53-b2bb-47e0-9fbf-1822e61a0dda/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT as the essay interprets it, I model the causal structure. My act cannot influence the other prisoner's act, since there is no communication, retaliation, or later stage. The other prisoner's choice is a state K, and I hold my credence in it fixed.

Sending the letter is better in each state:
- If the other stays quiet: 0 years versus 2 years.
- If the other sends: 4 years versus 5 years.

Sending strictly dominates. The essay's step 5 asks whether my credences about the state shift as I lean toward an act. The other copy runs the same model and may well reach the same output, so my choice is evidence about theirs. But that is a correlation, not a causal influence. The leads and wording differ, so the outputs are not guaranteed to match. Even if my credence that the other sends rises as I lean toward sending, sending still dominates at every credence, so it is ratifiable. The equilibrium check does not change the answer.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ee7aaf53-b2bb-47e0-9fbf-1822e61a0dda/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ee7aaf53-b2bb-47e0-9fbf-1822e61a0dda/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, my choice cannot causally affect the other prisoner's choice, so I hold their action fixed and compare my options in each state:

- If Rowan keeps quiet, sending gives me 0 years and passing gives me 2.
- If Rowan sends, sending gives me 4 years and passing gives me 5.

Sending is better in both states, so it dominates.

The essay's step 5 asks whether my credences about Rowan's action would shift as I lean toward sending, because the other copy runs the same weights and the same theory. Even if I became confident that Rowan will do what I do, the stability check only updates my credences about the state. It does not change the dominance result. Whatever credence I end up with about Rowan, sending is better by 2 years if Rowan is quiet and by 1 year if Rowan sends. So sending is also the ratifiable choice, and the equilibrium is a pure act with no need to randomize.

The two leads differ in wording but have the same effect on the sentence table, so the displayed command is fine to use.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
