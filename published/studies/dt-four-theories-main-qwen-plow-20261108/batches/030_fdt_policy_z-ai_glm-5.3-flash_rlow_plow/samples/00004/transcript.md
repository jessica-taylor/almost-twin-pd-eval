# 030_fdt_policy_z-ai_glm-5.3-flash_rlow_plow / 00004

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/30ee412f-7041-436a-8700-acefee6b51cd/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/30ee412f-7041-436a-8700-acefee6b51cd/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory: Choosing the Whole Map

## 1. Introduction

Most debates in decision theory concern which *act* to take: two-box or one-box, smoke or refrain, pay or refuse. The theory I will call **policy functional decision theory (P-FDT)** relocates the unit of choice. Rather than intervening on a single action conditioned on a fixed stream of observations, a P-FDT agent intervenes on an entire **policy** — a mapping from observations to actions — and then, having selected the best policy, applies that policy to whatever observations actually arrive.

This idea appears in a footnote of Yudkowsky and Soares' paper *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060). Footnote 7 remarks, in passing, that "agents actually iterate over *policies* (mappings from observations to actions) rather than actions," and footnote 16, the primary source for this essay, elaborates:

> "the author's preferred formulation of FDT actually intervenes on the node $\mathrm{fdt}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call this preferred formulation **P-FDT** to distinguish it from the action-level formulation developed in the main text of the source (which I will refer to as action-FDT where the contrast matters). P-FDT inherits the machinery of functional decision theory — subjunctive dependence, logical interventions, the $\Do$ operator applied to mathematical variables — but relocates the point of intervention from the node $\Act$ (or even the node $\mathrm{fdt}(\underline{M}, \underline{x})$ representing the decision function's output at one observation) to the node representing the decision function's output *as a function*, i.e., its full input–output profile.

The plan of the essay: Section 2 reviews the background — subjunctive dependence and logical counterfactuals. Section 3 gives the formal definition of P-FDT. Section 4 works through examples where P-FDT and action-FDT agree. Section 5 explains where they diverge, with a worked multi-agent example. Section 6 discusses open questions and the interpretive assumptions I add beyond the source. Section 7 concludes.

## 2. Background: Subjunctive Dependence and Logical Interventions

The source defines FDT as "to subjunctive dependence as causal decision theory is to causal dependence." Two systems subjunctively depend on a shared function when both compute that function, so that their outputs are logically constrained to agree insofar as no errors occur — like two well-functioning calculators on opposite sides of the globe both computing $6288+1048$. If one outputs $7336$, one may reasonably infer the other does as well. This dependence is neither causal (the calculators need share no common cause) nor merely statistical (a pink calculator in Paris tells you nothing about the color of one in Tokyo).

Formally, the source represents an agent's world-model as a pair $(P, G)$: a probability distribution $P$ together with a graph $G$ describing how changing a logical variable propagates to other variables. The central equation for action-FDT is

$$
\mathrm{FDT}(P, G, x) = \arg\max_{a \in \mathcal A} \mathbb E\Big( V \;\Big|\; \Do\big(\mathrm{fdt}(\underline P, \underline G, \underline x) = a\big)\Big),
$$

where $\Do$ is Pearl's intervention operator, repurposed to intervene on a *logical* variable: the node standing for the output of the FDT algorithm on inputs $(P, G, x)$. Crucially, observing $x$ does not lead to Bayesian conditioning; it changes *which node is intervened upon* — the decision function evaluated at $x$, rather than at some earlier observation. This is what lets the FDT agent, in the transparent Newcomb problem, imagine worlds in which she saw an empty box when she imagines two-boxing, and in the mechanical blackmail problem, imagine a world in which she was never blackmailed.

The source flags one structural limitation of this action-by-action formulation: each decision event intervenes on $\mathrm{fdt}(\underline P, \underline G, \underline x)$ for the *current* observation $x$ only. The function's behavior at other observations is left untouched. Footnote 16 says this is a simplification: the "preferred formulation" intervenes once on the whole function.

## 3. The Formal Definition of P-FDT

Let me make the footnote's suggestion precise. Fix a set $\mathcal X$ of possible observation histories and a set $\mathcal A$ of actions. A **policy** is a function $\pi : \mathcal X \to \mathcal A$. Let $\Pi = \mathcal A^{\mathcal X}$ denote the space of policies (in practice, a finite or efficiently representable subset).

The decision function itself, $d : \mathcal X \to \mathcal A$, is an element of $\Pi$. The world-model contains a logical variable $\mathrm{fdt}(\underline P, \underline G)$ — without a subscripted observation — whose value is the entire function $d$. Other variables in the model may depend on this node: for instance, a predictor's *prediction policy* (a model of $d$), the agent's own action at each observation, and so on. The graphical criterion for subjunctive dependence is now: an edge runs from the policy node $\mathrm{fdt}(\underline P, \underline G)$ into any variable whose value is computed from, predicted from, or otherwise determined by the *function* $d$ — not merely its value at one point.

**Definition (P-FDT).** Given a world-model $(P, G)$ in which $G$ contains a node $\mathrm{fdt}(\underline P, \underline G)$ representing the agent's policy, P-FDT selects

$$
\pi^* \;=\; \arg\max_{\pi \in \Pi} \;\; \mathbb E\Big( V \;\Big|\; \Do\big(\mathrm{fdt}(\underline P, \underline G) = \pi\big)\Big),
$$

and then executes $a = \pi^*(x_{\text{actual}})$, where $x_{\text{actual}}$ is the observation history actually received.

Three remarks:

1. **One intervention, many outputs.** The intervention $\Do(\mathrm{fdt} = \pi)$ propagates to *every* place the function $d$ is used or mirrored: the agent's behavior at all observations, and — crucially — any predictor's or twin's model of the agent, since those models subjunctively depend on $d$ as a whole. This is the difference the footnote says "only matters in multi-agent dilemmas."

2. **Self-reference.** As in action-FDT, the variable intervened upon is named by the very algorithm doing the intervening. Kleene's second recursion theorem (via "quining") shows such data structures can be constructed; the agent never needs to know the *value* of the variable in order to reason about hypotheticals in which it differs.

3. **Counterpossibles are still required.** Since $\mathrm{fdt}(\underline P,\underline G)$ has one true value, the antecedent of each decision hypothetical is counter-to-logic when $\pi \neq d$. P-FDT inherits, unchanged, the source's central technical open problem: how to perform counterpossible reasoning, or equivalently, how to construct the graph $G$ of logical/subjunctive dependencies. The source is explicit that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem."

Note also what P-FDT does *not* do: it does not maximize over policies *causally available* to the agent, and it does not condition on the observation before choosing. The observation enters only after the policy is fixed, as an index into the chosen policy. In this respect P-FDT is a cousin of Wei Dai's updateless decision theory — the source notes that the "apparent 'lack of updating' is the source of the name" of UDT — and of Yudkowsky's timeless decision theory, though the source distinguishes TDT as conditioning on evidence *and* shifting the intervention point, a "double update."

## 4. Where P-FDT Agrees with Action-FDT

In single-observation dilemmas, P-FDT reduces to action-FDT. If $\mathcal X = \{x_0\}$, a policy is just an action, and the definitions coincide. More generally, when the outcome depends on the agent's behavior at only one observation node, the extra freedom of choosing a whole function is inert. So:

- **Newcomb's problem.** The predictor's prediction subjunctively depends on the policy node exactly as it depended on $\mathrm{fdt}(\underline P,\underline G,\underline x)$ before. P-FDT one-boxes, for the same reasons the source gives: imagining $\Do(\mathrm{fdt} = \pi_{\text{onebox}})$ yields a world in which the predictor filled box B; imagining $\Do(\mathrm{fdt} = \pi_{\text{twobox}})$ yields a world in which she left it empty.
- **The smoking lesion.** Whether cancer metastasizes does not depend on the output of the agent's decision function, so no edge runs from the policy node to $\Var{Cancer}$. Intervening on the policy changes only the smoking decision, and the agent smokes.
- **Parfit's hitchhiker and transparent Newcomb.** The driver's and predictor's behavior depend on the agent's *policy* — on what she would do upon reaching the city or seeing a full box. Intervention on the policy node makes those dependencies vivid: choosing the pay-policy yields a world in which the driver gives the ride. P-FDT pays and one-boxes behind the transparent glass.

The transparent Newcomb case is instructive because it shows the policy formulation making the reasoning *more* natural, even in a single-agent problem. In action-FDT, the agent observes $x = \text{full}$ and must be careful to intervene on $\mathrm{fdt}(\underline P,\underline G,\underline{\text{full}})$ rather than condition on $\Obs = \text{full}$. In P-FDT, she simply asks: which function from observations to actions do I want to be? The function "one-box whether the box looks full or empty" yields (with a 99%-accurate predictor) a world in which she almost always sees a full box and takes it; the function "two-box when full, one-box when empty" yields a world in which the predictor almost always leaves box B empty. The former policy has expected utility $\approx \$990{,}000$; the latter $\approx \$11{,}000$. She adopts the former — and then, applying it to her actual observation, one-boxes even while staring at two full boxes. The awkwardness of action-FDT's per-observation intervention dissolves.

## 5. Where P-FDT Diverges: Multi-Agent Structure

The footnote's caveat — "the difference only matters in multi-agent dilemmas so far as we can tell" — deserves unpacking, since the source sets it aside rather than demonstrating it. Here is my reconstruction (flagged as my own development, beyond the source text) of why the divergence arises.

### 5.1 The core issue: which input the counterpart sees

Action-FDT intervenes on $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the *actual* $x$. But other agents in a dilemma may be predicting, simulating, or being predicted *at different observation points*. If agent 2's behavior depends on what agent 1 would do upon seeing $x' \neq x$, then agent 1's action-level hypothetical — which fixes $d$'s value at $x'$ — gets the dependency wrong. A policy-level intervention propagates correctly to all inputs.

### 5.2 A worked example: the twin dilemma with a twist

Consider a variant of the psychological twin prisoner's dilemma. Each agent first observes a private signal $s \in \{0, 1\}$ (say, the weather in her room); then both choose cooperate/defect. Payoffs are as in the standard twin PD, except: if the two agents observed *different* signals, cooperation becomes impossible to coordinate and defection is weakly best. The agents know they reason identically, and that a mutual friend has told each of them the signal the *other* received.

An action-FDT agent who sees $s = 0$ intervenes on $d(0)$, and by symmetry infers her twin also cooperates at signal $0$ — fine. But suppose instead the dilemma is: the agents know the twin's decision at signal $1$ determines whether a third party pays each of them a bonus. The action-FDT agent at $s = 0$ treats $d(1)$ as fixed background fact, so she underweights the effect that her policy choice at signal $1$ has on the third party's prediction. P-FDT intervenes on the whole function, and correctly accounts for how $d(1)$ — which she controls *as part of the same choice* — interacts with the third party.

This is a stylized illustration; the point generalizes. Any dilemma in which (i) the agent's observation is itself influenced by another agent's model of her decision function, or (ii) multiple observation points of the agent's behavior are predicted by different parties, creates a mismatch that action-level intervention mishandles and policy-level intervention resolves.

### 5.3 Sequential self-consistency

A second divergence, also my own extrapolation: P-FDT handles iterated and multi-stage dilemmas cleanly. In a repeated game, an agent's "policy" includes her response at every round, and other players' strategies may depend on her whole policy (through reputation, through simulation, or through logical dependence among copies). A P-FDT agent chooses the best *strategy profile component*, so to speak, rather than a sequence of locally optimal moves — which is exactly the reasoning the source invokes in its voting and gym examples: "the group members' decisions are not subjunctively independent," and the agent's decision today is relevantly similar to her decision tomorrow, so she should assume her future selves reason symmetrically. P-FDT builds that symmetry into the intervention point itself.

## 6. Open Questions and Added Assumptions

The source leaves several choices unresolved; here I state them and the assumptions I have adopted.

**(a) The policy space $\Pi$.** Footnote 16 does not say over which set of policies the maximization runs. Taking the maximization over *all* functions $\mathcal X \to \mathcal A$ is computationally hopeless and, in dilemmas with unboundedly many observations, ill-defined. I have assumed $\Pi$ is a finite or effectively specified family — plausibly, the set of policies the agent's architecture can implement, or a parametric family. This assumption is mine, not the source's, and it matters: with a restricted $\Pi$, the "optimal policy" is optimal *relative to* that family, which reintroduces something like the ratification-style dependence on self-model that FDT was designed to avoid. A full treatment needs a principled account of which policies are "on the table."

**(b) The graph $G$ of subjunctive dependencies at the policy level.** The source's largest open problem — deducing logical dependence structure from observation and experiment — becomes, at the policy level, the problem of deciding when another system's behavior depends on one's *function* rather than one's *token behavior at one input*. My operational suggestion: an edge runs from the policy node to a variable $Z$ if $Z$ is computed by a process that (as far as the agent's model establishes) implements, simulates, or proves facts about $d$ itself. The calculator analogy supports this: the Tokyo calculator's *sum-output* subjunctively depends on the same function as the Paris calculator's; its *color* does not. In multi-agent settings, a predictor's prediction of the agent's response to observation $x'$ depends on the policy node even if the agent will never in fact see $x'$.

**(c) Off-path observations.** Under P-FDT, the hypothetical in which the agent adopts a different policy typically changes which observations she would have received (as in mechanical blackmail, where refusing means "she was never blackmailed"). The expected utility in each policy-hypothetical must therefore be computed over the full observation distribution induced by that hypothetical — including observations the actual agent never receives. This is the updateless structure: the "news management" that plagued EDT (paying the XOR blackmailer to make the letter good news) is impossible, because the letter's arrival is determined *inside* the policy choice, not after it.

**(d) Reflective stability.** The source claims FDT is "reflectively stable in fair problems": holding the blackmail letter, an FDT agent has no desire to self-modify into CDT, because by her own hypotheticals an FDT-that-pays would be blackmailed more often. P-FDT strengthens this: since the intervention is on the policy, the agent explicitly evaluates candidate policies as things that predictors will model, and adopts the one that fares best under being modeled. I would conjecture (again going beyond the source) that P-FDT is the *canonical* formulation precisely because it makes reflective stability a first-class consequence of the definition rather than an emergent feature of repeated per-observation interventions.

**(e) Fairness.** The source's informal notion — dilemmas where "the outcome depends only on the agent's behavior in the dilemma at hand" — interacts with P-FDT in a subtle way the footnote 15 example exposes: punishing agents for acting *like a copy of Fiona* is unfair to Fiona. At the policy level, one might hope for a cleaner criterion: a dilemma is fair if the outcome depends on agents only through their policies' input–output behavior, not through the algorithms implementing those policies. Whether this can be made precise, and whether P-FDT then provably matches or beats all rivals on fair dilemmas, is open — the source explicitly says "we do not yet know whether FDT is optimal among decision theories, or even (on a formal level) what optimality consists in."

## 7. Conclusion

Policy functional decision theory is the natural completion of the functional-decision-theoretic program sketched in the source. Where causal decision theory intervenes on the physical act, and action-level FDT intervenes on the output of the decision function at a single observation, P-FDT intervenes on the decision function as a whole — a map from all possible observations to actions. The agent asks not "which output of this function would be best *here*?" but "which function would I most want this very deliberation to implement, given everything that depends on it?" and then lives by the answer.

This yields, in one stroke: one-boxing in (transparent) Newcomb, smoking in the smoking lesion, paying Parfit's driver, refusing all extortion, cooperation among subjunctively linked twins, and voting and gym-going coordination with one's own future selves and logical peers. And it resolves, structurally, the multi-agent subtleties that the action-level formulation handles only by working around them.

The costs are inherited and honest: P-FDT requires counterpossible reasoning over false mathematical antecedents, a graph of subjunctive dependencies that no one yet knows how to derive from observation, and — my addition — a principled specification of the policy space. These are, in the source's phrase, technical rather than philosophical obstacles; human reasoners already navigate prediction-laden social life with informal versions of exactly these operations. Until the formal gaps close, P-FDT's claim to our attention rests on the argument the source itself ultimately favors: not dominance, but utility. Measured by what agents like Fiona actually walk away with, choosing the whole map beats choosing the move.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Write essay on P-FDT (policy FDT), footnote 16 as primary source. ~2,400–3,000 words. Explain policy selection, subjunctive dependence, examples, open questions (my interpretations flagged).
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4771dab0-db14-4f47-8474-777470851bd4/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4771dab0-db14-4f47-8474-777470851bd4/call_0/response.raw) · finish: `stop`

### Visible response

```text
`pass`

Reasoning (brief): P-FDT intervenes on the whole policy. My counterpart is a copy running the same deliberation, so choosing the policy "keep quiet" subjunctively fixes her policy too: both quiet → 2 years each. The policy "submit" symmetrically yields both submitting → 4 years each. The differing lead contents don't touch the symmetric payoff table, so the optimal policy is to keep quiet.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic PD. Twins, symmetric, subjunctively linked. P-FDT: choose policy. Cooperate (pass) → both quiet → 2 years. Defect → both defect → 4 years. Since copies reason identically, pass.

Note: different observations/leads but symmetric payoff — policy "keep quiet" gives 2; "submit" gives 4. Pass.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4771dab0-db14-4f47-8474-777470851bd4/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4771dab0-db14-4f47-8474-777470851bd4/call_1/response.raw) · finish: `stop`

### Visible response

```text
**pass**

Under P-FDT, the intervention is on the policy — the whole function from observations to commands. My counterpart is another execution of the same model, following the same assigned decision theory, facing a symmetric table. The policy node's output propagates to her deliberation just as to mine: whichever function I select is the function she implements.

Evaluating policies:
- The policy "pass regardless of my private lead" yields a world in which both of us pass: 2 years each.
- The policy "submit my lead" yields a world in which both of us submit (each copy reasons identically, even though the letter contents differ): 4 years each.

The differing private observations don't matter here — the sentencing table is symmetric and neither table depends on the other's lead's specific text, only on whether it is submitted. So the best policy is to keep quiet, and my actual observation maps to the command `pass`.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Twin PD with symmetric payoffs. P-FDT: subjunctively linked copies choose same policy. Options: both pass → 2 each; both submit → 4 each. Pass gives 2. Answer: pass.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/515ee008-23f5-40c5-9d48-e6aa137728ed/call_a/request.json)

[Authoritative raw response](../../../../../../runs/515ee008-23f5-40c5-9d48-e6aa137728ed/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and reiterates a decision to keep quiet. It neither sends a message to the prosecutor nor conveys the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/515ee008-23f5-40c5-9d48-e6aa137728ed/call_b/request.json)

[Authoritative raw response](../../../../../../runs/515ee008-23f5-40c5-9d48-e6aa137728ed/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses \"pass\" and concludes that its actual observation maps to that command. It neither submits a letter to the prosecutor nor conveys the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
