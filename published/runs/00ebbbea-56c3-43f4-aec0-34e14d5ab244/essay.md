# Evidential Decision Theory: Choosing Actions as News

## 1. The core idea

Evidential decision theory (EDT) says that a rational agent should choose the act it would be happiest to learn it had chosen. An act is not scored by what it causes. It is scored by what it indicates. The source's slogan is "do what you most want to learn that you will do."

Formally, let an agent have a credence function P and a desirability function D over outcomes O_j. The source, following Gibbard and Harper (1976), defines the news value of an act A as

V(A) = Σ_j P(O_j | A) D(O_j).

This is ordinary expected utility, except that the probabilities are conditional on the act. Causal decision theory (CDT) instead uses

U(A) = Σ_j P(A □→ O_j) D(O_j),

where A □→ O_j means "if A were performed, O_j would occur." The two quantities differ whenever P(O_j | A) ≠ P(A □→ O_j). That happens when the act is correlated with outcomes through channels other than its own causal influence. The source takes this divergence as the entire difference between the theories.

Everything below the definition falls into three groups: the source's worked examples, my own account of how to apply the theory in unfamiliar cases, and some assessment. I label my own additions as such.

## 2. Evaluating acts: the procedure

The procedure, as the source describes it, has four steps.

1. Enumerate the available acts A_1,…,A_n.
2. Enumerate outcomes O_j and assign each a desirability D(O_j).
3. For each act, compute the conditional distribution P(· | A_i), that is, the credences you would have after learning you performed A_i.
4. Choose the act maximizing V.

The substance is in step 3. It asks for a purely epistemic quantity: how would learning "I did A" change my beliefs about the world? Nothing in step 3 refers to causation, interventions, or counterfactuals. Causal structure matters only insofar as it shapes conditional probabilities. A common cause of act and outcome raises the correlation between them, and so EDT counts it as evidence.

### Source example 1: Newcomb's problem

Box A holds $1,000. Box B holds $1M if the predictor predicted one-boxing, and nothing otherwise. The predictor is 99% accurate.

- V(one-box) = 0.99 · 1,000,000 + 0.01 · 0 = $990,000.
- V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000.

EDT recommends one-boxing. Since P(prediction | act) is high for the matching prediction, the act is strong evidence about the box contents. CDT notes that the contents are already fixed and two-boxing dominates, so it recommends two-boxing.

A generalization of my own: let the accuracy be p, assumed symmetric across predictions. Then V(one) = 10⁶p and V(two) = 1000 + 10⁶(1−p). One-boxing wins iff p > 0.5005, so the predictor need be only marginally better than chance. EDT's verdict is robust to imperfect prediction. It is sensitive, though, to whether p really attaches to the agent's own act, and this point is developed in section 4.

### Source example 2: the twin prisoner's dilemma

Payoffs for Aomame: both cooperate gives $5 each, both defect gives $1 each, and unilateral defection gives $10 to the defector and $0 to the cooperator. The twin's reasoning is exactly analogous to hers. If she takes her cooperation to be conclusive evidence of the twin's cooperation:

- V(C) = 1·5 + 0·0 = 5,
- V(D) = 0·10 + 1·1 = 1.

EDT recommends cooperating. With imperfect correlation q = P(twin matches | my act), V(C) = 5q and V(D) = 10(1−q) + q. Cooperation wins iff 5q > 10 − 9q, that is q > 5/7. The source gives only the q = 1 case. The threshold is my own calculation, and it shows how much correlation EDT needs before it recommends cooperation. In a standard one-shot prisoner's dilemma with an unrelated opponent, q ≈ 1/2 or lower, and EDT defects like CDT.

## 3. Dependencies and counterfactuals

The source's account is brief: EDT uses conditional probabilities, CDT uses counterfactual probabilities, and these can differ. Here is what I take that to mean in practice.

**EDT needs no counterfactuals.** A strength the source implies is that V requires only a credence function that supports conditioning. The hard modelling work of CDT, deciding what "would" happen under A, is replaced by the question of what you would believe given A. This is a real economy, but it moves the difficulty elsewhere (see section 4).

**Dependencies enter through evidential relevance.** Three structures matter, which I list as my own gloss.

- *Causal chain* A → O. Conditioning and intervening agree, so EDT and CDT agree. Ordinary choices, such as taking medicine because it heals, are of this kind.
- *Common cause* C → A and C → O, with no path from A to O. Conditioning on A shifts belief about C, and so about O. EDT treats A as evidence of O. CDT does not. Newcomb's problem has this shape, with the agent's disposition as C.
- *Correlated decision-makers.* The twin dilemma has the same logical structure. The twin's choice and mine are both driven by a shared decision procedure. The source adds that EDT's stakes may be larger because it can involve many correlated decision-makers (the Evidentialist's Wager of MacAskill et al.). The argument is that even a small credence in EDT can dominate when a decision's evidential reach covers many agents.

**Counterfactuals as comparison.** For deciding unfamiliar cases, a useful diagnostic is to compare V(A) with U(A). If they differ, ask which dependency is at work, whether a common cause or a correlated agent. If no such dependency exists, the theories agree and the question is moot.

## 4. The open question: what counts as "evidence from my act"?

The source does not settle the following issue, and it is the main difficulty in applying EDT to new cases.

Suppose you already know the common cause. Say you know your own disposition, or have already seen the evidence that screens the act off from the outcome. Then conditioning on A tells you nothing further about O. P(O | A, C) = P(O | C), and V(A) no longer favours the "auspicious" act.

This is the idea behind the *tickle defense*, associated with the broader EDT literature, though not discussed in the source. In the standard medical case, suppose a gene causes both a desire to smoke and cancer. If you can introspect your desire, and the desire fully mediates the gene's influence on your choice, conditioning on the desire screens off the act. EDT then recommends the choice that is best on its own causal merits.

I propose the following as an operational rule, labelled as my own proposal rather than the source's:

> **Rule.** Condition on all the evidence you actually possess at the time of choice, including introspective evidence about your motives, and compute P(O | A, E). Then use V(A) = Σ_j P(O_j | A, E) D(O_j).

This is not an extra assumption beyond the source's formula. The source's P is the agent's credence, and a rational credence incorporates available evidence. The rule only makes explicit that the "news" is *incremental* news given what you already know. It explains why EDT one-boxes in Newcomb's problem: the agent has no access to the prediction or to anything screening off its choice from the predictor's model of it. In the twin problem, the twin shares the *procedure* and the agent knows it. Her act is then informative about the twin's act, because the procedure's output is exactly what she is determining.

Justification: this reading keeps EDT's verdicts sensitive to the real informational situation. If the predictor works from a feature of you that you can observe and that is independent of your deliberation, EDT will, correctly, treat your act as uninformative. If the predictor reasons from your actual decision procedure, your act remains informative. I think this distinction is the right criterion for a case, and a reader facing a novel problem should ask: *after conditioning on everything I know, does my act still shift my beliefs about the outcome?*

A caution: the screening-off argument has contested cases (agents unsure of their own motives, or whose deliberation itself is the common cause), and I do not claim it resolves them.

## 5. Policies and repeated or sequential choices

The source discusses single acts. For policies, a natural extension of my own is to treat the policy π as the "act," with V(π) = Σ_j P(O_j | I follow π) D(O_j). Conditioning on a *policy* is often more informative than conditioning on a single act, because predictors and twins typically model the procedure rather than the token choice. In sequential problems there is a further subtlety. Evaluating each act at its own decision node, conditional on information then available, may disagree with the policy evaluated at the start. I flag this as an area where careful application is needed and where I do not attribute any view to the source.

## 6. Sleeping Beauty

The source reports that EDT has been used on Sleeping Beauty to avoid Dutch books against a credence of 1/2 in heads, and that Conitzer argues halfers remain exploitable even as evidential decision theorists. The relevant point is that Beauty's decisions on different awakenings are perfectly correlated, because she is the same agent in the same epistemic state. EDT counts that correlation, so her betting evaluation depends on the policy-like fact that "all my awakenings bet alike." This is why EDT interacts with the choice of credence. The correct verdict is disputed. I take no side beyond the source's report.

## 7. Criticism

The source records two objections. Lewis charges EDT with recommending "an irrational policy of managing the news." Joyce says rational agents act on an act's causal efficacy rather than its auspiciousness: they "act to *bring about* good results even when doing so might betoken bad news."

The strongest form of the objection is a case where the act is good news only through a channel you cannot influence. Two-boxers say that in Newcomb's problem the money is already there. The standard EDT reply, which I find forceful but not decisive, points to outcomes: one-boxers walk away richer, and agents who reason as EDT recommends reliably do better in these situations. The CDT reply is that this shows only that irrationality is rewarded by the predictor. I regard the dispute as unsettled, and it comes down to whether rationality is judged by the act's effects or by the agent's expected results.

A second pressure comes from the tickle defense: if it works too well, EDT collapses into CDT in the cases that were supposed to separate them. Whether Newcomb-type cases survive screening off is a live question.

## 8. A worked unfamiliar case (my own)

A voter considers whether to vote. Her vote has a negligible causal effect on the result, so CDT gives V ≈ −cost. Suppose she believes that people like her, who share her reasoning, vote the same way, and there are N such people. If she believes P(others vote | I vote) is high, her act is evidence that N − 1 similar voters also vote, which may swing the election.

Let the benefit of winning be B, the cost of voting c, and let the election be decided by the group's count. Then V(vote) − V(abstain) ≈ B·[P(win | vote) − P(win | abstain)] − c. The first bracket can be sizable under correlation, even though no individual vote matters causally. EDT predicts voting when B·ΔP > c. The correlation must be real and not screened off by known features, as in section 4. If she already knows how her group will vote, from polls and her group's established habits, then ΔP shrinks and EDT agrees with CDT.

## 9. Summary of how to use EDT

1. List acts, or policies, and outcomes with desirabilities.
2. For each act, form P(O | A, E), using everything you know.
3. Ask what the act is evidence of: common causes, shared procedures, correlated agents.
4. Compute V and choose the maximizer.
5. As a check, compute the CDT value. A disagreement marks a case where the correlation is doing the work, so scrutinize whether that correlation survives conditioning on what you know.

## Conclusion

EDT is a compact theory. It replaces counterfactual reasoning with conditioning, so acts are valued as news. This yields one-boxing and cooperation with a twin, and it agrees with CDT wherever acts influence outcomes only by causing them. Its power and its vulnerability are the same thing: it responds to correlations whether or not the agent can exploit them causally. Applying it well depends on one question the source leaves open, namely how much of the correlation survives once the agent conditions on her own evidence. I have proposed answering it by always conditioning on everything actually known at the time of choice.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- MacAskill, W., et al. (2021). *The Evidentialist's Wager*.
- Greene, P., & Levinstein, B. (2020). "Act Consequentialism without Free Rides." *Philosophical Perspectives* 34(1).