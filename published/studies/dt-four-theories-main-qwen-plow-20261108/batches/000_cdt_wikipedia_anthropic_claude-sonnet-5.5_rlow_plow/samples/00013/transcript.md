# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00013

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/bf978e84-c61e-4abc-81da-e116952f46db/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/bf978e84-c61e-4abc-81da-e116952f46db/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definitions, Computation, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. Two ingredients are involved. One is a utility over outcomes. The other is a way of measuring how likely each outcome is *if* an act were performed, as opposed to how likely it is *given the news* that the act is performed. The second ingredient is where CDT differs from evidential decision theory (EDT).

Notation:

- Acts A₁,…,Aₙ.
- Outcomes O_j with desirabilities D(O_j).
- Credence function P, the agent's beliefs at the time of choice.

EDT scores acts by V(A) = Σ_j P(O_j | A) D(O_j). The Gibbard–Harper formulation of CDT, which the source cites, scores them by

U(A) = Σ_j P(A □→ O_j) D(O_j),

where A □→ O_j is the counterfactual "if A were performed, O_j would result." Everything turns on how P(A □→ O_j) is computed and why it can differ from P(O_j | A).

## 2. Why the counterfactual is not the conditional

Conditioning on A is *evidential*: it treats A as information, so it also updates on everything correlated with A, including its causes and common causes. The counterfactual "if I were to do A" is *interventional*: it holds fixed what lies causally upstream of, or independent of, the act, and varies only what the act influences.

Lewis showed that no single proposition "A → O" can have, across a reasonable class of probability functions, probability equal to P(O | A) in general (his triviality result). So CDT cannot be treated as EDT with different notation. Gibbard and Harper observed that if their two axioms hold (one of them tied to conditional excluded middle) and A is probabilistically independent of the conditional A □→ O_j, then P(A □→ O_j) = P(O_j | A). The two theories diverge exactly when the act is evidence about which counterfactuals are true, that is, when the act is correlated with the state of the world that determines its consequences.

## 3. An operational form: dependency hypotheses

The source stresses that the counterfactual-probability algorithm is left unspecified. The standard way to make it operational, which comes from Lewis (1981) and Skyrms and is slightly beyond the source, uses **dependency hypotheses**. A dependency hypothesis K is a maximally specific proposition about how outcomes depend causally on acts, covering everything outside the agent's control. Then

U(A) = Σ_K P(K) · Σ_j P(O_j | A, K) D(O_j).

Within each K, conditioning on A is harmless because K already fixes the causal structure, and the weights P(K) are *unconditional*. Evidential theory would use P(K | A) instead. That is the entire formal difference: **CDT holds fixed the unconditional credences in dependency hypotheses**. Egan makes the same point in the source when he describes CDT as holding fixed "our initial views about the likely causal structure of the world."

In a causal-graph model the same thing can be written with Pearl's do-operator: U(A) = Σ_j P(O_j | do(A)) D(O_j). The two readings agree when K ranges over the exogenous-variable settings that, together with the act, determine the outcome. Both avoid Lewis's imaging regress by taking the causal structure as given. That is an assumption, and the vagueness criticism below targets exactly it.

## 4. Worked examples

**The apple.** Let the apple be good (G) with probability p. Eating yields happiness h if G and sadness −s if not. Then U(eat) = ph − (1−p)s, and U(not eat) = 0. Here G is causally and evidentially independent of the act, so CDT and EDT agree.

**Newcomb's problem.** The predictor is 99% accurate. Box A holds $1,000. Box B holds $1,000,000 iff one-boxing was predicted. The dependency hypotheses are K₁ (B full) and K₂ (B empty), with P(K₁) = q at the moment of choice. Then:

- U(two-box) = 1000 + q·10⁶
- U(one-box) = q·10⁶

Two-boxing wins by $1,000 for **every** q. It dominates, because the act cannot alter the box contents. EDT instead uses P(K₁ | one-box) = 0.99 and P(K₁ | two-box) = 0.01, giving V(one-box) = 990,000 against V(two-box) = 11,000.

The disagreement is not about arithmetic. Each theory answers a different question: "what will my act bring about?" or "what does my act indicate?" Philosophers surveyed on balance prefer CDT, and the source reports this, but the case is still contested, since two-boxers walk away with $1,000 and one-boxers with $1,000,000.

**King David.** Charisma (the common cause) is fixed. Revolt probability depends on charisma, not on the act of summoning, though summoning correlates with uncharisma. Within each K, summoning Bathsheba does not change the revolt probability, so summoning dominates. EDT counsels abstaining, since summoning is bad news about one's charisma. CDT summons.

**Prisoner's dilemma with a twin.** If my twin's choice is correlated with mine but not caused by it, then holding the twin's behavior fixed makes defection dominant, as in Newcomb's problem. Lewis argued that the prisoner's dilemma is a Newcomb problem for this reason.

## 5. Policies versus acts

The source speaks of acts, but the framework extends to policies, i.e. maps from observations to acts. A CDT agent evaluates a policy π by intervening on the *decision node* at the time of choice and holding fixed everything already settled. A difference arises when a predictor reads the agent's *policy* in advance. The standard CDT answer is to treat the prediction as a fixed upstream state at the moment of action. So at each choice point the agent defects to the dominating act. This is "causal at the time of acting." A different proposal would intervene on the policy *as it was fixed earlier*, which changes the answer in Newcomb-like problems. That proposal is not CDT. It belongs to successors such as functional or updateless approaches, and I mention it only to mark the boundary.

## 6. Where dependency credences come from: deliberation

If credences about K are updated during deliberation, the agent's own inclination becomes evidence about K. Consider Death in Damascus. Death predicts where you will be, and you choose Damascus or Aleppo. If you lean toward Damascus, you expect Death to be in Damascus and so prefer Aleppo. Then you expect Death in Aleppo, and the preference reverses. Every act is unratifiable: once you settle on it, you wish you had done the other.

Two responses exist, both beyond the source's specifics:

1. **Ratifiability** (Harper, Jeffrey): choose only acts that maximize U under the credences you would hold *after* deciding on them. Sometimes none exist in pure acts.
2. **Mixed or deliberational equilibria** (Joyce, Skyrms): stabilize credences where the agent is indifferent. Here that means 50/50 credence in Death's location, and any act then has equal expected value.

Joyce's defense of CDT, mentioned in the source, is that CDT can treat "information about what one is inclined to do as evidence." This changes P(K) through deliberation, so unconditional credences are not frozen at their initial values. Egan's critique is that the "hold fixed" step is exactly what is wrong. These two readings are interpretive, and the source leaves the dispute open.

## 7. Counterexamples and what they show

**Psychopath Button.** Paul believes only psychopaths press the button, and he prefers a world with psychopaths over death. The K-partition is: Paul is a psychopath, or Paul is not. Unconditionally, his credence in being a psychopath may be low, so pressing seems to kill only psychopaths, which he thinks is good, and CDT recommends pressing. Yet if he presses, he learns he is probably a psychopath and so would die. Egan argues that "pretty much everyone" says not to press. A CDT agent who updates on his own inclination (Joyce's view) could refuse. A naive one presses. The example thus reveals that CDT's verdict depends on *which credences it holds fixed*, and the source reports this ambiguity without resolving it.

**Adversarial Offer.** Two boxes cost $1 each, and you may buy one or none. The seller puts $3 in each box she predicted you would *not* buy, with prediction accuracy 0.75 believed by both. Suppose your credence that box 1 is full is q₁ and box 2 is q₂. Since the seller fills the box she predicts you won't buy, q₁ + q₂ = 1 + (1 − the probability of predicting "neither"), which means q₁ + q₂ ≥ 1 when the seller always predicts a purchase of at most one box. So one box has q ≥ ½, and its causal expected value is at least $1.50 − $1 > 0. CDT buys.

Evidentially, if you buy box i, the chance box i is full is only 0.25. That gives expected value 0.75 − 1 < 0. Averaged over choices, the buyer loses $0.25 per purchase in expectation, and the seller profits systematically. Oesterheld and Conitzer use this to argue that CDT agents can be exploited, and that CDT agents are subject to diachronic Dutch books. CDT defenders reply that the buyer was handed a bad situation, that the prediction is a fact about the agent's type, and that the rational agent is not responsible for the world rewarding other types. This "why ain'cha rich?" exchange recurs in every case here.

## 8. Vagueness and Lewis's imaging

The source notes that CDT does not itself fix an algorithm for P(A □→ O). Lewis's imaging proposal shifts probability from each world w to the closest A-world w_A. For this to be defined we need a similarity ordering, and the source notes a regress: knowing the closest A-world requires knowing what we would believe on certainty of A, itself a conditional with probability below 1.

The dependency-hypothesis and do-calculus formulations circumvent this regress by assuming that causal structure is *specified*, in a graph or as a partition. That is an additional assumption, not a derivation. In practice it works well when the model is clear (medical trials, games) and leaves real indeterminacy when it is not (agents modeled by predictors, or logically correlated agents).

## 9. A procedure for unfamiliar cases

1. List acts (or policies) and outcomes.
2. Identify what is already settled and causally independent of the act: the candidates for K.
3. Specify credences P(K), and decide whether deliberation updates them (naive CDT: no; deliberational CDT: yes, to an equilibrium).
4. For each K, compute the act's outcome distribution and utility.
5. Average over P(K), unconditionally on the act.
6. Check ratifiability: if the recommended act would not be chosen after one became confident one would perform it, treat the problem as an instability case and apply the deliberational variant.

A quick diagnostic: if some act dominates in every K, CDT chooses it, regardless of correlation with K. That is the signature of CDT, and also the source of the objections.

## 10. Conclusion

CDT evaluates acts by their expected causal effects, formalized as expected utility over counterfactual probabilities, concretely a mixture over dependency hypotheses held fixed unconditionally. It differs from EDT only where acts are evidence about causally independent facts, and there it recommends dominance reasoning: two-boxing, summoning Bathsheba, defecting against a correlated twin. The counterexamples (Newcomb, Death in Damascus, Psychopath Button, the Adversarial Offer) show that outcomes can depend on which credences are held fixed, and that agents following naive CDT may be exploitable. Defenders respond with deliberational refinements and with the observation that predictors reward type, not rationality. The disagreement concerns what "rational" should mean when an agent's own decision is evidence about the world, and I think it remains genuinely open.

**References** (as cited in the source): Gibbard & Harper (1981); Lewis (1976, 1979, 1981); Egan (2007); Joyce (2012); Oesterheld & Conitzer (2021); Spencer (2020); Weirich, *SEP* "Causal Decision Theory"; Shaffer (2009); Ahmed (2021).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/24433ed8-9e4b-4d62-bad6-aad6e5717324/call_0/request.json)

[Authoritative raw response](../../../../../../runs/24433ed8-9e4b-4d62-bad6-aad6e5717324/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is already fixed and my command cannot cause it to change. I hold my credence over their choice fixed and unconditional on my act.

Compare the two acts in each dependency hypothesis:
- If the other keeps quiet, sending gives me 0 years and passing gives me 2, so sending is better.
- If the other sends, sending gives me 4 years and passing gives me 5, so sending is again better.

Sending dominates in both cases. The other copy runs the same model and may reach the same output, but the essay says a CDT agent treats that correlation as evidence, not as a causal link, and does not let it change the choice. Deliberational updating gives the same result, because sending is better under every credence about the other's act. It is also ratifiable.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/24433ed8-9e4b-4d62-bad6-aad6e5717324/call_1/request.json)

[Authoritative raw response](../../../../../../runs/24433ed8-9e4b-4d62-bad6-aad6e5717324/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is causally independent of mine. I can't communicate with them, and the sentence depends only on the two choices.

Holding their choice fixed:
- If they keep quiet, sending the letter gives me 0 years and passing gives 2, so sending is better.
- If they send a letter, sending gives me 4 years and passing gives 5, so sending is better.

Sending the letter dominates in both cases. The copy's likely correlation with me doesn't change this, because CDT holds fixed the unconditional credence about their action. The ratifiability check also passes. Even if I became confident the other prisoner would send, or confident they would stay quiet, sending is still best.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
