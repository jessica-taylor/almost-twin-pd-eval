# Policy Functional Decision Theory: Choosing Policies, Not Acts

## 1. Introduction

Decision theory asks how a rational agent should act. The two classical answers — causal decision theory (CDT) and evidential decision theory (EDT) — share a common structure: they evaluate *actions*. The agent holds fixed everything except (a version of) her action, computes expected utility, and picks the best act. The reference article that this essay interprets (Yudkowsky & Soares, "Functional Decision Theory") argues that both theories fail because their counterfactuals are malformed: EDT "manages the news" by treating all correlations between act and world as decision-relevant, while CDT breaks even the correlations that carry real decision-relevant information, such as the link between an agent's behavior and a predictor's model of that behavior.

Both classical theories, however, share a second, quieter assumption that has received far less attention: that the unit of evaluation is the *action* — the particular thing the agent's body does in a particular situation. This essay is about the theory one obtains by dropping that assumption. I will call it **policy functional decision theory (P-FDT)**. The source motivates it in a single footnote — footnote 16 — which says:

> "the author's preferred formulation of FDT actually intervenes on the node FDT(−) to choose not an action but a **policy** which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell."

The parenthetical disclaimer is doing a lot of work, and it is worth taking seriously rather than dismissing. What follows is my reconstruction: what P-FDT is, how to formalize it, why "only matters in multi-agent dilemmas" is both true in a narrow sense and misleading in an important one, and how the theory evaluates unfamiliar cases.

## 2. Background: functional decision theory in one page

The source's central idea is *subjunctive dependence*. When two physical systems compute the same function — two calculators evaluating 6288 + 1048 — their outputs are not merely correlated; they are constrained to agree *by the function they both implement*. If one calculator shows 7336, the other almost surely does too. This dependence is neither straightforwardly causal nor merely statistical: it is logical. The paper defines FDT by analogy:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Formally, the source gives (its equation 4):

$$\mathrm{FDT}(P, G, x) = \arg\max_{a \in \mathcal A}\; \mathbb{E}\Big[\,V \;\Big|\; \mathtt{do}\big(\mathrm{FDT}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big],$$

where $P$ is a probability distribution over a world-model, $G$ is a graph describing *logical and causal* dependence structure (not just causal structure), and $\mathrm{FDT}(\underline{P},\underline{G},\underline{x})$ is a variable *in the model* representing the output of the decision algorithm on its own inputs. The $\mathtt{do}$ operator performs the same surgery Pearl uses for causality, but on a *logical* node: when the agent imagines her decision function outputting $a$, she also imagines every variable subjunctively depending on that output — the predictor's prediction, her twin's action, Death's appointment book — changing accordingly. Everything else is held fixed.

Crucially, in this equation the maximization is over $\mathcal A$, the set of **actions**, and the node intervened upon is the output of FDT given a *particular observation history* $x$. Footnote 16 says the preferred formulation instead intervenes to choose a **policy** — a function from inputs to actions — and this is the move I now develop.

## 3. From actions to policies

### 3.1 Definitions

Fix the vocabulary of the source. An agent has a set $\mathcal X$ of possible observation histories $x$, a set $\mathcal A$ of actions, an observation-dependent belief state, and a utility function $V$ over outcomes.

**Definition (policy).** A *policy* is a function $\pi : \mathcal X \to \mathcal A$, mapping each possible observation history to an action. Write $\Pi$ for the (finite, for our purposes) set of policies.

A policy is the mathematical object the source calls a "predisposition": the decision-theoretic fingerprint of an agent across *all* situations she might find herself in, not just the one she currently occupies. An agent who one-boxes upon seeing a full box and upon seeing an empty box, and who smokes, is not characterized by three isolated acts but by one policy.

**Definition (P-FDT).** The policy functional decision theory prescription is:

$$\mathrm{P\text{-}FDT}(P, G) = \arg\max_{\pi \in \Pi}\; \mathbb{E}\Big[\,V \;\Big|\; \mathtt{do}\big(\underline{\pi} = \pi\big)\Big],$$

and the agent then executes $\pi(x^*)$, where $x^*$ is her actual observation history. Equivalently:

$$\mathrm{P\text{-}FDT}(P, G) = \Big(\arg\max_{\pi}\; \mathbb{E}\big[V \mid \mathtt{do}(\underline\pi = \pi)\big]\Big)(x^*).$$

Three remarks on this definition, flagging where I am adding structure the source leaves implicit:

1. **The intervention is on the policy node.** Just as action-FDT intervenes on a variable representing the output of the decision function *given current inputs*, P-FDT intervenes on a variable representing the output of the decision function *as a mapping on all inputs*. All and only the variables subjunctively dependent on the policy — other agents' predictions of the agent's policy, other implementations of the same policy, the agent's own behavior in *counterfactual* situations — change with it.

2. **The expectation is over observations.** Here I am making a choice the footnote does not specify. In the source's action-FDT, observations enter by *changing the intervention point* (intervene on $\mathrm{FDT}(\underline P,\underline G,\underline x)$ rather than conditioning on $x$, per the transparent Newcomb analysis). For the policy version, the natural analogue is a genuinely *updateless* calculation: the agent evaluates each candidate policy by its expected utility averaged over the observations she might receive, before conditioning on which observation she actually received. Wei Dai's updateless decision theory — cited in the source as an early variant of FDT — is exactly this move, and footnote 16's "policy" language plus the source's remark that the agent "applies her inputs in order to select an action" supports this reading. The agent then *executes* the policy's recommendation for her actual observations, without re-optimizing.

3. **The policy set is assumed finite and the expectation well-defined.** I will flag below (Section 6) where these assumptions strain.

### 3.2 Why policies? The source's own hints

The source already contains the seed of the idea in several places. In the gym example of Section 9, the agent's decision today is claimed to be relevantly like her decision next week: "If there are no relevant differences between her decision today versus tomorrow, then she should assume that she will continue going to the gym in the future if she goes today." That reasoning is *policy* reasoning — the agent treats today's choice as revealing (and subjunctively determining) a consistent disposition across a whole class of situations. Similarly, the transparent Newcomb analysis says Fiona, upon seeing a full box, "imagines a hypothetical world where she instead (with high probability) sees that the box is empty." An agent who reasons about her hypothetical observations at all is reasoning about a policy: her answer to "what would I do if I saw the empty box?" is part of the object being evaluated.

Action-FDT gets at this by changing the intervention point as observations arrive. P-FDT makes the structure explicit and uniform: one intervention, on a single object, once.

## 4. Where the difference is invisible (and why the footnote says it doesn't matter)

In single-agent, single-observation dilemmas, P-FDT and the source's action-FDT agree. This is easy to see in Newcomb's problem. The predictor fills box B iff she predicts one-boxing; the policy being evaluated has two relevant components, $\pi(\text{full})$ and $\pi(\text{empty})$ (with standard Newcomb's problem, only one observation — none about box contents — matters). Intervening on $\pi$ and setting it to "always one-box" yields: my body one-boxes with probability ≈1, and the box is full with probability 0.99, giving expected utility ≈ \$990,000. Setting $\pi$ to "always two-box" gives ≈ \$11,000. The argmax policy one-boxes, and the agent one-boxes — exactly the source's result. The same holds in the smoking lesion (with the source's two-utility-function formalization), Parfit's hitchhiker, Death in Damascus, and the blackmail problems: since these dilemmas involve a single decision point, choosing a policy and choosing the act are extensionally identical.

So the footnote's claim is right in its narrow scope: for everything the source actually analyzes, P-FDT and action-FDT coincide.

## 5. Where policies matter

### 5.1 Multiple observations of the same agent

The difference emerges when one agent's behavior is predicted or observed *in more than one situation*, and different observers' responses depend on different components of her behavior. Consider the source's mechanical blackmail problem joined with Newcomb's problem, faced by the *same* agent with a predictor who knows her policy across both.

An action-FDT agent handles this by intervening on $\mathrm{FDT}(\underline P,\underline G,\underline x)$ separately for each observation history she actually occupies. But here is the subtle problem the footnote gestures at: if she faces the *first* dilemma today and the *second* tomorrow, action-FDT at each point intervenes on the output given *today's* inputs. Each individual intervention imagines the predictor's model of her updating correctly. But if her disposition across the pair of dilemmas is what the predictor models — if the predictor predicts "what kind of agent is this?" — then the correct object of intervention is the pair-level policy, and only the policy-level intervention imagines all downstream consequences coherently.

A concrete case where this bites: suppose an agent will face Newcomb's problem (predictor pays one-boxers) *and* a variant (a second predictor pays *two-boxers*, having observed her Newcomb behavior). If she can commit to a policy over the pair before either predictor acts, she can one-box for predictor 1 and two-box for predictor 2, earning ≈ \$1,001,000. An agent who re-optimizes act-by-act, or who treats each dilemma's intervention independently, faces the transparent-Newcomb temptation problem at the second stage: given that she already one-boxed, two-boxing the second time is locally better, and predictors who model *acts* will predict it. But predictors who model *policies* — as any competent predictor of a deterministic agent must — will see the whole mapping. The policy agent who refuses to let her policy be "one-box, then defect on the second predictor" is the one predictor 2 fills the box for. (I flag this as my extension of the source's framework; the source does not analyze this case, and its claim that the difference "only matters in multi-agent dilemmas so far as we can tell" is an honest report of what the authors had verified, not a theorem.)

### 5.2 Multi-agent dilemmas: the true home of policy reasoning

The footnote's phrase "multi-agent dilemmas" points to the deepest application. Consider a psychological twin prisoner's dilemma where the twins each face the dilemma but also interact in a second, asymmetric game afterward. Or consider the voting example from the source's conclusion: ten agents each must pay \$1,000 to vote, and each receives \$1,000,000 iff all ten vote. The source notes that an FDT agent votes because the group members' decisions "are not subjunctively independent." But note what the coordination actually requires: each agent must reason as if her *disposition* — the policy "vote when facing this exact coordination structure" — is shared. If agent 1 faces a slightly different version of the problem than agent 2 (say, a \$1,200 cost), the action-level argument ("my decision is like theirs") breaks; the policy-level argument ("we all implement the same policy mapping decision-problem-descriptions to votes") survives, and correctly prescribes voting as long as the policy's average payoff across the coalition is positive. P-FDT gives this reasoning a formal home: the intervention is on the shared policy, the expectation aggregates over the coalition members' differing observation histories, and voting is prescribed whenever $\mathbb E[V \mid \text{all ten implement the voting policy}]$ exceeds the alternative.

Game-theoretically, P-FDT recommends the policy whose intervention is best — which, among agents that model each other as policy-implementers, selects the *program-equilibrium* (in the sense of Tennenholtz, though the source does not use that term) that maximizes each participant's utility given subjunctive dependence. Mutual cooperation in the twin prisoner's dilemma is the simplest instance.

### 5.3 Why not just "act as if committed"?

One might object that the source already handles all of this with its slogan that FDT agents "simply act as they would have precommitted to act." The policy formulation is the precise version of that slogan. Precommitment talk is diachronic and psychological; the policy is a static mathematical object, and the P-FDT intervention on it needs no temporal machinery, no binding ritual, and no assumption that the agent could have committed earlier. The policy is chosen *now*, from the global perspective the source describes: "What would the entire universe look like if the FDT algorithm behaved differently?" — where "behaved differently" now means "implemented a different mapping from inputs to actions."

## 6. Open problems specific to the policy formulation

Being honest about what the source leaves unresolved, and where my reconstruction extends it:

**(a) The policy space.** Footnote 7 of the source says agents "iterate over policies (mappings from observations to actions)." In realistic problems, $\mathcal X$ is astronomically large and $\Pi$ intractable. The source's own remark that bounded agents "approximating" these theories behave comparably applies with extra force here: any real P-FDT agent must restrict $\Pi$ to a representable class (e.g., programs of bounded length), which raises a question action-FDT also faces but less acutely — whether the restriction itself can be exploited by predictors. I know of no formal result either way; this is genuinely open.

**(b) Observations that depend on the policy.** My updateless reading (evaluate policies before conditioning on actual observations) is one natural choice, but there are others: one could condition the expectation on the *event* that the agent's actual observation history occurs while still intervening on the policy. In transparent Newcomb these give the same answer (the source's calculation already includes both branches via the accuracy variable). They can diverge in problems where the agent's utility function or probability distribution is itself observation-dependent — the smoking lesion's structure, iterated. The source gives no guidance; I recommend the updateless version on the grounds that it inherits the value-of-information virtues the source emphasizes (P-FDT agents never assign negative value to information, since information changes which component of the *already chosen* policy they execute, never the policy itself).

**(c) Logical uncertainty about the policy.** The source notes that the FDT variable is in the model and the agent may be uncertain of its value; Kleene's recursion theorem guarantees coherent self-reference. For policies, the self-reference is heavier — the model must represent the policy's behavior on all inputs — but the same technique applies. Nothing in the footnote suggests a problem unique to policies here.

**(d) The dependency graph.** The largest open problem the source names — deducing subjunctive dependence structure from observation and experiment, the analogue of Pearl's methods for causation — applies unchanged, and is arguably harder for policies: one must ask, for each candidate policy, how *each component* of the policy propagates logical influence. The calculator analogy extends naturally (two copies of the same program are one policy implemented twice), but the graph construction does not.

## 7. A worked micro-example

To make the procedure concrete, consider a problem I will call the **Sequential Newcomb pair**. An agent is observed by a predictor with 99% accuracy at two times. At time 1 she faces standard Newcomb. At time 2 she faces it again — but the second predictor knows both what the first predictor predicted *and* whether the agent one-boxed at time 1, and fills box B iff she predicts the agent one-boxes at time 2 *given* having one-boxed at time 1.

- **CDT**: two-boxes at both times; both predictors fill nothing; payoff ≈ \$2,000.
- **EDT**: one-boxes at time 1 (good news), and at time 2 — conditional on having one-boxed at time 1 — one-boxes again; payoff ≈ \$1,980,000. (EDT happens to do well here; the source's XOR blackmail shows where it fails.)
- **Action-FDT applied naively**: at time 2, intervening on $\mathrm{FDT}(\underline P,\underline G,\underline{x_2})$ — the output given time-2 inputs — correctly imagines the second predictor's prediction changing, one-boxes, and earns the full payoff *provided* the graph at time 2 encodes the dependence of the second prediction on the time-2 output *conditional on the observed history*. But if the second predictor's behavior depends on the *pair* of behaviors — e.g., she fills the box only if she predicts the agent one-boxes *both* times, a natural "consistency-checking" predictor — then no single-output intervention captures the dependence. The intervention point must be the policy $\pi = (\pi(x_1), \pi(x_2))$ treated as a unit.
- **P-FDT**: evaluates each of the four policies $\{\text{1-box}, \text{2-box}\}^2$ by $\mathbb E[V \mid \mathtt{do}(\underline\pi = \pi)]$, with the consistency-checking predictor's behavior a function of $\pi$ itself. The best policy is (one-box, one-box): ≈ \$1,980,000. Two-boxing at either stage risks the whole second box.

This example shows the footnote's "only matters in multi-agent dilemmas" in its full meaning: it is not only about *multiple agents*, but about any setting where *the environment evaluates the agent's behavior as a function*, rather than as a set of isolated outputs. Predictors of deterministic agents, by their nature, do exactly that.

## 8. Summary of prescriptions

For readers who want an operational recipe:

1. Model the world with a distribution $P$ over variables including, for each candidate policy $\pi$, variables representing everything subjunctively dependent on $\pi$: predictions of $\pi$, other implementations of $\pi$, and your own behavior under all observation histories.
2. Build a dependency graph $G$ containing both causal arrows and logical-dependence arrows (the hardest step; in practice, treat "systems computing the same function" as sharing a node).
3. For each $\pi \in \Pi$, compute $\mathbb E[V \mid \mathtt{do}(\underline\pi = \pi)]$, holding fixed everything not downstream (logically or causally) of the policy node, and aggregating over observation histories.
4. Execute $\arg\max_\pi \pi(x^*)$ for your actual observations $x^*$.

Sanity checks against the source: one-box in (transparent) Newcomb ✓; smoke in the smoking lesion ✓ (the policy node connects to the act but not to the cancer); pay Parfit's hitchhiker ✓; refuse all blackmail ✓; stay in Damascus ✓; vote in the ten-agent coalition ✓; go to the gym ✓.

## 9. Conclusion

Policy functional decision theory is the source's preferred formulation of FDT, stated in footnote 16 and left mostly undeveloped there: intervene not on the output of your decision function for the observation you happened to receive, but on the decision function itself, understood as a policy mapping all possible observations to actions, and then apply your actual observations to the winning policy. In every dilemma the source analyzes, P-FDT agrees with action-FDT — which is why the footnote can say the difference "only matters in multi-agent dilemmas." But the difference is conceptually significant well before exotic game theory arrives: it explains transparent Newcomb one-boxing as policy evaluation rather than observation-bending, it formalizes the source's precommitment and gym examples, and it is *necessary* — not merely convenient — once any part of the environment (including other agents, or the agent's own future selves) responds to her behavior *as a function* rather than to isolated outputs. The costs are the ones the source already owns — dependence on counterpossible reasoning and an unconstructed theory of subjunctive-dependence graphs — plus two new ones I have flagged: the tractability of the policy space, and the choice of how observations enter the expectation, for which I have recommended the updateless reading. What the policy formulation buys, in exchange, is a single intervention that captures, in one mathematical object, everything the source's prose describes as choosing "from the global perspective."

**Source.** Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060. All quotations are from this text; footnote 16 is the primary source for P-FDT. Extensions in Sections 3.1, 5, 6, and 7 are my own proposals, marked as such.