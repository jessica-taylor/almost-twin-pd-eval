# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. The key word is "causal." An act may be a sign of good news without bringing it about. CDT asks what the act would bring about, not what it would indicate.

Evidential decision theory (EDT) ranks acts by the conditional expectation

V(A) = Σ_j P(O_j | A) D(O_j).

The source presents CDT in the Gibbard–Harper form,

U(A) = Σ_j P(A □→ O_j) D(O_j),

where D is desirability and P(A □→ O_j) is the probability of the counterfactual "if A were performed, O_j would result." (The source writes the arrow as →.) The whole theory is this one change: replace the conditional probability P(O_j | A) with the probability of a counterfactual. The two coincide when the act is probabilistically independent of the relevant counterfactuals, and diverge otherwise.

## 2. Why the two quantities differ

Conditioning on A is epistemic: it updates on A as evidence, so it shifts beliefs about everything correlated with A, including its causes and common causes. A counterfactual supposition is interventionist: it holds fixed what A does not influence.

Lewis's 1976 triviality results show that no single proposition "A → O" can in general have probability equal to P(O | A) across a non-trivial class of probability functions. So CDT's counterfactual probability cannot be identified with conditional probability. Gibbard and Harper showed that, given two axioms (one tied to conditional excluded middle), if A is statistically independent of the conditional A □→ O_j, then P(A □→ O_j) = P(O_j | A). The converse failure is what matters: when acts and conditionals are dependent, the theories split.

## 3. A usable formulation: dependency hypotheses

The source does not say how to compute counterfactual probabilities. Here is a standard operational reading, which is my gloss and not the source's.

Partition the possibilities into *dependency hypotheses* K, each a maximally specific proposition about how outcomes depend causally on the agent's acts, together with whatever background is causally independent of the act. Given K, each act's outcome is settled (or has a determinate chance). Then

U(A) = Σ_K P(K) · Σ_j P(O_j | A, K)·D(O_j) = Σ_K P(K) · E[D | do(A), K].

The crucial feature is that the weights are the **unconditional** credences P(K), not P(K | A). EDT would use P(K | A). This is exactly the "hold fixed unconditional credences in dependency hypotheses" requirement that Egan identifies, and it is where both CDT's strength and its critics' objections originate.

This formulation is close to Skyrms's K-partition, and in Pearl's causal-model language it is the expectation of the outcome under the intervention do(A). In a causal graph with acts A, background variables, and an outcome, the formula is

U(A) = Σ_s P(s) · E[D | A, s],

provided s ranges over states that A does not influence. The word "provided" matters. The partition must consist of causally independent factors, or at least be fine enough that conditional on K the act is irrelevant evidentially to the outcome.

## 4. The procedure

1. List the available acts.
2. Specify the causal structure: which variables the act can influence, and which are fixed independently of it.
3. Specify credences P(K) over the dependency hypotheses or states, without conditioning on the act.
4. For each act and each K, compute the outcome distribution under intervention.
5. Weight by P(K), take desirabilities, and choose the maximum.

## 5. Worked examples

**Apple.** The apple is good with probability g. Eating gives happiness h if good, −s if bad; not eating gives 0. U(eat) = gh − (1−g)s. Here the state is causally independent of the act and also evidentially independent, so CDT and EDT agree.

**King David (Gibbard–Harper).** The states are C (charismatic) and ¬C. Charisma is fixed in adulthood and causes both just behavior and freedom from revolt. Let the utility of Bathsheba be b > 0, and the loss from a revolt be r. Say P(revolt | ¬C) = 0.8 and P(revolt | C) = 0.1, with P(C) = c. The act "send" does not alter C or the revolt chance given C. So

U(send) = b − [c·0.1 + (1−c)·0.8]·r, and U(abstain) = −[same bracket]·r.

Thus U(send) − U(abstain) = b > 0, and CDT sends for her whatever c is. EDT, by contrast, notes that sending is evidence of ¬C, so P(revolt | send) is higher than P(revolt | abstain). If r is large enough, EDT abstains. CDT's verdict follows the structural fact that sending does not change one's charisma; it is a dominance argument.

**Newcomb.** Let S be the state "box B is full." The predictor has already acted, so S is causally independent of the choice. With p = P(S), two-boxing yields 1000 + p·10⁶ against one-boxing's p·10⁶. Two-boxing wins by 1000 for every p, so CDT two-boxes. EDT uses P(S | one-box) ≈ 0.99 and P(S | two-box) ≈ 0.01, giving about 990,000 against 11,000, and one-boxes. This is the defining split. The CDT theorist says one-boxers are rewarded for a prior disposition, and that the person facing the choice cannot change what is in the box. The critic replies "if you're so smart, why ain't you rich?" The CDT reply is that the rich were offered a different, better game.

## 6. Where CDT is under pressure: instability

The formula uses P(K), but a rational agent deliberating about its act often acquires evidence about that act, and so about K, when the predictor or the world is correlated with the agent's own dispositions. This creates two problems.

**Death in Damascus.** Death predicts your location, Damascus or Aleppo, with high reliability, and waits there. Suppose you currently lean toward Damascus. Then you think Death is probably in Damascus, so Aleppo looks better. Once you lean toward Aleppo, Damascus looks better. No pure act is *ratifiable*: each is worse by your own lights once you consider that you will choose it. Plain CDT, with fixed credences, does not tell you where to stop. Extensions (Harper's ratifiability, Joyce's deliberational dynamics, mixed acts) address this. A natural equilibrium reading says to randomize at the credence where the two acts have equal expected utility. That is my suggestion rather than something the source asserts.

**Psychopath Button.** Paul believes only a psychopath would press. Pressing kills psychopaths, himself included if he is one. Unconditionally, he gives some credence to being a psychopath. Fixed-credence CDT may value pressing: if he is not a psychopath, it is great; if he is, he dies, but with low prior credence. Yet once he considers pressing, his credence in being a psychopath rises. Egan says nearly everyone thinks Paul should not press, and counts this against CDT. Joyce's reply is that CDT, correctly applied, uses all available evidence, including evidence about one's own inclinations, so the credence in K should be updated as deliberation proceeds. The question is then whether that update is legitimate (a defence of CDT) or amounts to smuggling in EDT (the critics' view).

## 7. Money-extraction arguments

Oesterheld and Conitzer's **Adversarial Offer**: two boxes cost $1 each, and you may buy at most one. The seller put $3 in each box she predicted you would *not* buy, and her prediction has accuracy 0.75, as both parties believe.

A CDT agent reasons that the contents are fixed. If q is the credence that box 1 holds the $3, then box 2 holds it with probability 1−q (the seller fills the box she predicts you won't buy, so at least one box is filled; assume exactly one). Then

q·3 + (1−q)·3 = 3,

so the average causal expected value of the two boxes is $1.50, and one of them has causal value at least $1.50 > $1. Buy it. Yet the evidential facts are that you buy a box exactly when the seller probably predicted it, so the box you buy is empty with probability 0.75. Your expected net is

0.25·3 − 1 = −0.25 per round.

The seller profits on average. This is a case where following CDT voluntarily loses money in expectation, and the source cites it, with the allied claim that CDT agents are exposed to diachronic Dutch books. CDT defenders reply that the setup rewards a predictable disposition and that a CDT agent who is offered such deals simply faces an adversarially chosen environment.

## 8. The vagueness objection

The source notes that CDT does not itself say how to compute P(A □→ O). Lewis's imaging proposes moving each world's probability mass to the nearest A-world:

P_A(w') = Σ_{w : closest A-world to w is w'} P(w).

This needs a similarity ordering, which is exactly the causal information we wanted. Shaffer's regress worry is that knowing which world is closest requires knowing what we would believe if certain of A, itself a conditional with uncertain probability. The dependency-hypothesis and causal-model formulations of §3 are a practical way out. They replace similarity ordering with a structural model. The cost is that the model, including its treatment of the agent's own decision as an intervention, must be supplied from outside, so judgments about "what is causally downstream" remain an input to the theory and are not derived by it.

## 9. How to decide unfamiliar cases

Ask these questions in order.

- **Is there a causal route from act to outcome?** If not, differences in evidential correlation are irrelevant to CDT.
- **What are the states the act cannot influence?** Take credences over them. If those credences should depend on your own inclination (as with Paul), decide how deliberation should update them. Plain CDT holds them fixed; sophisticated versions update to a ratifiable fixed point.
- **Is there dominance?** If one act is better in every causally independent state, CDT picks it (David, Newcomb). Dominance reasoning fails when the states are not independent of the acts.
- **Check for instability.** If the recommended act changes your credences so as to favor another, look for equilibria, including mixed ones.

## 10. Conclusion

CDT replaces "what does choosing A tell me?" with "what would choosing A bring about?" Formally, it weights outcome utilities by counterfactual probabilities, or equivalently by unconditional credences over dependency hypotheses, which gives dominance-respecting verdicts in cases like King David and Newcomb. Most philosophers, according to the source, prefer it to EDT. Its weaknesses are real: counterfactuals need a causal model that the theory does not provide, fixed credences yield instability (Death in Damascus) and doubtful verdicts (Psychopath Button), and Adversarial Offer-type cases show CDT agents losing money in expectation. Defenders such as Joyce respond that CDT can and should treat self-knowledge as evidence. Whether this repair preserves CDT's distinctive content, or simply drifts toward EDT, remains the central open dispute.