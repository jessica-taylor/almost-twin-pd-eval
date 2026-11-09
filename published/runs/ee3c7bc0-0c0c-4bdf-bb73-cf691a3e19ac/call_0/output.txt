# Evidential Decision Theory: Acts as News

## 1. The core idea

Evidential decision theory (EDT) says to choose the act you would be happiest to learn you had chosen. The source's slogan is "do what you most want to learn that you will do." Formally, given acts A, outcomes O_j, and a desirability function D, the source defines the news value

V(A) = Σ_j P(O_j | A) D(O_j),

and EDT recommends an act maximizing V. The causal decision theory (CDT) rival replaces P(O_j | A) with P(A □→ O_j), the probability of the counterfactual "if A were performed, O_j would result":

U(A) = Σ_j P(A □→ O_j) D(O_j).

The source (following Gibbard and Harper 1976) says only that these quantities are not always equal, and that this is why the theories diverge. Everything below on how to apply EDT is my elaboration unless I say it is the source's.

EDT has no separate causal apparatus. Dependencies enter only through the agent's credences, since P(· | A) encodes every correlation, causal or not, that the agent believes links her act to the world. Counterfactuals do not appear at all. That is both its appeal (one probability function and ordinary conditioning) and the root of its critics' complaints.

## 2. What "conditioning on an act" means

Conditioning is well defined only if P(A) > 0. If the agent is certain she will not do A, P(O | A) is undefined. Operationally one can use a small-probability fix: assign every available act a tiny positive probability, for instance via a hypothetical "trembling" of the agent's choice. This is my suggestion, not the source's. It has a cost, though. What the tremble correlates with matters. If the tremble is independent noise, conditioning on it severs correlations with the agent's dispositions and EDT starts to look causal. If the tremble reflects the agent's actual decision procedure, correlations remain. Which reading is right is a real open question, and I adopt the second for the cases below because those thought experiments stipulate that the correlation runs through the agent's decision procedure.

A second point: V(A) is computed from the agent's credences *as she deliberates*. The source speaks of the act as "news," but she is not literally learning it. The calculation is a hypothetical: how good would the world be, by my present lights, given that I am the sort of agent who does A?

## 3. The procedure

1. List the available acts A_1,…,A_n.
2. Specify outcomes O_j and their desirabilities D(O_j). Outcomes should be fine-grained enough to include everything the agent cares about.
3. For each act, compute the conditional distribution P(O_j | A_i) using the whole credal state, including beliefs about predictors, twins, and common causes.
4. Compute V(A_i) and choose the maximum.

Equivalently, using a partition of states S_k, V(A) = Σ_k P(S_k | A) · D(A ∧ S_k). Unlike the CDT analogue, the weights P(S_k | A) depend on A. If states are probabilistically independent of the act, the weights reduce to P(S_k), and EDT agrees with CDT. This is the sense in which the two theories "agree in many cases."

## 4. Worked cases from the source

**Newcomb's problem.** The predictor is 99% accurate. Box A holds $1,000; box B holds $1,000,000 if one-boxing was predicted, else nothing. With the source's numbers:

V(one-box) = 0.99 · 10⁶ = $990,000,
V(two-box) = 0.01 · 1,001,000 + 0.99 · 1,000 = $11,000.

EDT one-boxes. CDT two-boxes because the contents are already fixed, so two-boxing yields $1,000 more in either state.

Generalizing: let accuracy be p (symmetric) and the prize M against the visible m. Then V(one) = pM and V(two) = (1−p)M + m. One-boxing wins iff p > ½ + m/(2M). With the source's numbers the threshold is 0.5005. So EDT's verdict is robust to rather poor predictors, and only a nearly uninformative predictor flips it.

**Twin prisoner's dilemma.** Payoffs: both cooperate $5 each; both defect $1 each; unilateral defector $10, cooperator $0. If the twin mirrors the agent with probability 1, V(C) = 5 and V(D) = 1, so EDT cooperates. With imperfect correlation q (probability the twin does what the agent does), V(C) = 5q and V(D) = 10(1−q) + q. Cooperation wins iff 5q > 10 − 9q, i.e. q > 5/7. The structure parallels Newcomb: EDT cooperates when the act is sufficiently strong evidence about the other player's act. CDT defects because the agent's act does not causally influence the twin's.

## 5. The key philosophical point: evidence versus causation

The two verdicts above are the cases friendly to EDT. Critics emphasize that V tracks *auspiciousness* rather than efficacy. Lewis called EDT "an irrational policy of managing the news"; Joyce said rational agents act on "causal efficacy, not auspiciousness." The standard illustration (not in the source) is a medical case. Suppose a gene causes both a disposition to choose some act (say, smoking) and a disease, and the act itself is harmless. Choosing the act is bad news about the gene, so a naive EDT calculation avoids it, though avoiding it does nothing for the agent's health.

The standard EDT reply (the "tickle defense," again not in the source) is that if the gene influences behavior only through beliefs and desires the agent can introspect, then once she conditions on those, the act carries no further evidence about the gene. Formally, if G is screened off from A by the agent's known mental state T, then P(G | A, T) = P(G | T), and V equals the causal value. The reply works only to the extent that the agent really has such introspective access. In Newcomb and twin cases, the stipulation is that the correlation survives conditioning on everything the agent can inspect, because the predictor or twin tracks the same decision procedure. There EDT keeps its evidential verdict. A reader deciding an unfamiliar case should therefore ask: after I condition on all my own known reasons and dispositions, does my act still shift my credence about a state I care about? If not, EDT and CDT agree. If so, EDT lets the act count as evidence.

A proponent's defense of the Newcomb verdict is the familiar one: those who one-box walk away rich, and the theory should be judged by the expected result of being its follower. The critic answers that this confuses a favorable predicament with a good choice within it. The source presents both sides and takes no stand, and I won't claim the dispute is settled.

## 6. Policies and many agents

Because V is computed with the agent's whole credal state, EDT naturally extends to correlated decision makers. The source notes (citing MacAskill et al., "The Evidentialist's Wager") that EDT can involve many correlated agents, so its stakes may be higher than CDT's. Even a agent with low credence in EDT might then act as if it were true. A rough version of the argument: if there are N agents whose choices correlate with yours with strength ε, then EDT counts roughly εN extra copies of the benefit, which can swamp CDT's considerations when N is huge. This is an expected-choiceworthiness argument under theoretical uncertainty, and it depends on the contested assumption that such correlations exist and that one can compare values across the two theories.

The same machinery gives a policy-level reading: evaluate a policy π (a map from observations to acts) by V(π) = Σ_j P(O_j | I follow π) D(O_j). This is my extension, not the source's. For one-shot decisions it coincides with act evaluation. For sequential problems, conditioning on the whole policy can differ from re-conditioning at each node. The difference matters especially when the agent's later information changes which correlations remain. In such cases EDT can recommend plans that its stage-by-stage self would abandon. I flag this as unresolved, and a careful user should specify which evaluation point is intended.

## 7. Sleeping Beauty

The source says EDT has been used to answer Dutch book arguments against Sleeping Beauty when she holds credence ½ in heads. The idea is that when Beauty considers bets, her decision at one awakening is correlated with her decisions at other awakenings, because they are the same reasoning. Conditioning on "I bet" therefore also updates on the number of bets placed, which changes the expected payoff relative to a calculation that treats each bet as isolated. The source also notes Conitzer's objection that halfers remain exposed to Dutch books even with EDT. I would not read EDT as a resolution of the credence question, only as a different account of how credences feed into bets.

## 8. Strengths and weaknesses summarized

Strengths:
- It needs a single probability function and ordinary conditioning, with no primitive causal or counterfactual notions.
- It recommends the intuitively profitable acts in Newcomb and twin problems.
- It handles correlated agents uniformly.

Weaknesses:
- It can confuse evidence with influence, so it may "manage the news" in cases where a common cause is not screened off.
- Conditioning on probability-zero acts is undefined and its repairs are contested.
- Its sequential behavior is less clear than its one-shot behavior.

## 9. A short method for new cases

Given a new problem, write the agent's credences as a joint distribution over acts, states, and outcomes. Compute P(O | A) for each act. Then compare with the causal counterfactual weights. If they match, nothing philosophical is at stake. If they differ, identify the source of the discrepancy: a predictor, a twin, or a common cause. Then ask whether the agent's own introspectible states screen it off. If they do, the evidential calculation, done correctly, falls back toward the causal answer. If not, EDT will treat the act as evidence and select accordingly.

## 10. Conclusion

EDT is the view that an act's value is the conditional expected desirability of the world given that the act is performed. It is simple and unified, and it gives the one-box and cooperate verdicts that the source emphasizes. Its central difficulty is the one Lewis and Joyce press: whether rational choice should respond to what an act indicates or only to what it brings about. The source reports the dispute without resolving it, and so do I. What I have tried to supply is an operational recipe, together with the points where that recipe depends on further assumptions: how to handle zero-probability acts, how much screening-off the agent's introspection provides, and whether to evaluate acts or policies.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1976). Counterfactuals and Two Kinds of Expected Utility.
- Lewis, D. (1981). Causal decision theory. *Australasian J. Philosophy* 59(1).
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge.
- Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese* 192.
- MacAskill, W. et al. (2021). *The Evidentialist's Wager*.
- Greene, P. & Levinstein, B. (2020). Act consequentialism without free rides. *Philosophical Perspectives* 34.