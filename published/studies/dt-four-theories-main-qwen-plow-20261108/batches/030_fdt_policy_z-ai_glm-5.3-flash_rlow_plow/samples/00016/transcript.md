# 030_fdt_policy_z-ai_glm-5.3-flash_rlow_plow / 00016

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c11e43a7-8764-460b-b631-16a566b928c1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c11e43a7-8764-460b-b631-16a566b928c1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory: Choosing the Whole Function, Not the Act

## 1. Introduction

Most of decision theory is built around a single question: *what should I do?* Causal decision theory (CDT) answers it by asking which physical act causes the best outcome; evidential decision theory (EDT) by asking which act would be best news. In "Functional Decision Theory: A New Theory of Instrumental Rationality," Yudkowsky and Soares (2017) argue that both framings share a subtle error: they treat the *action* as the object of choice, when the action is really the output of a fixed mathematical decision function. The right object of choice, they claim, is the output of that function itself.

In this essay I focus on a refinement of that idea, mentioned only in a footnote of the source paper. Footnote 16 states that the authors' preferred formulation of functional decision theory "actually intervenes on the node [representing the decision function's output] to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action." I will call this policy-based formulation **policy functional decision theory (P-FDT)**, and treat it as the decision theory under examination. The paper remarks that the difference between choosing actions and choosing policies "only matters in multi-agent dilemmas so far as we can tell." That is somewhat deflationary: as I will try to show, the policy framing is also the cleanest way to state the theory's core idea — choose, from a global perspective, which *function* you would most like the decision-function-in-your-head to be — and it clarifies how the theory handles observations, counterfactuals, and coordination.

Sections 2–4 develop the machinery: policies, subjunctive dependence, and a formal decision rule. Sections 5–6 work through canonical examples. Section 7 discusses open problems and the additional assumptions I am making beyond the source. Throughout, claims taken from the paper are attributed to it; departures are flagged as mine.

## 2. From actions to policies

Fix a decision problem with:

- a finite set of **observations** $\mathcal X$ (everything the agent might learn before acting),
- a finite set of **actions** $\mathcal A$,
- a countable outcome set $\mathcal O$ with utility $\Util: \mathcal O \to \mathbb R$,
- a world-model: a probability distribution $P$ over relevant variables, together (in the paper's graphical formulation) with a graph $G$ describing *subjunctive dependence* structure (§3 below).

A **policy** is a function $\pi: \mathcal X \to \mathcal A$, assigning an action to each possible observation. Standard FDT, as presented in the body of the paper, evaluates actions: it intervenes on the variable $\FDTvar(\underline P, \underline G, \underline x)$ representing what the decision function outputs *given this particular observation* $x$. P-FDT instead intervenes on a variable representing which *policy* the decision function implements:

$$
\text{P-FDT}(P, G) \;:=\; \arg\max_{\pi \in \mathcal A^{\mathcal X}} \;
\mathbb E\Big[ \Util(\Outcome) \,\Big|\, \Do\big( \pi^* = \pi \big) \Big],
\qquad \text{then act by } \pi^*(x).
$$

Here $\pi^*$ is the variable in $P$ representing "the policy that the agent's decision procedure, as implemented in the world (and in any accurate model of her), selects." The $\Do$ operator is Pearl's intervention, applied not to a node representing a physical act but to a node representing a mathematical fact about the agent's decision procedure. After selecting the best policy, the agent simply executes it at whatever observation she actually receives.

Two contrasts are worth making explicit.

**Contrast with action-FDT.** In single-decision problems with one observation point, action-FDT and P-FDT coincide: choosing the best output given input $x$ is equivalent to choosing the best policy, since a policy is just a tuple of outputs, one per input. The difference emerges when the agent may face *multiple* observation points or interact with other agents whose behavior depends on her *dispositions across situations*, not just her act here. (Footnote 7 of the paper makes the same point.)

**Contrast with precommitment.** P-FDT is not precommitment. A precommitter chooses now to constrain her future self; a P-FDT agent evaluates, at decision time, the counterfactual question "what would the world be like if my decision procedure were a function that, in each situation, did such-and-such?" — and then *is* that function, immediately, with no binding mechanism needed. As the paper puts it, FDT agents "can simply adopt the optimal predisposition on the fly, whatever that may be."

## 3. Subjunctive dependence

The engine of the theory is the notion of **subjunctive dependence** (Section 3 of the source). Two physical systems that compute the same mathematical function have behaviors that "subjunctively depend" upon that function: if the function's value were different — an impossible event, hence a *counterpossible* — both outputs would differ together. Two well-functioning calculators computing $6288 + 1048$ on opposite sides of the galaxy will agree, not because one caused the other or because they share a mundane common cause, but because each implements the same arithmetic.

The paper's slogan: *functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.* Where a CDT agent's hypotheticals preserve causal structure and sever everything else, a P-FDT agent's hypotheticals preserve all decision-relevant subjunctive dependencies: anything else in the world that is a function of (an accurate model of, or a computation identical to) the agent's decision procedure varies with the intervention on $\pi^*$; everything else — mere statistical correlations, common causes like lesions — is held fixed.

Formally, the model $P$ must contain, besides ordinary physical variables, variables representing the outputs of mathematical functions, including the self-referential variable $\pi^*$ standing for the policy output of the agent's own decision procedure. The paper notes that this self-reference is harmless: by Kleene's second recursion theorem ("quining"), algorithms can contain and manipulate accurate representations of themselves without needing to know their own output in advance.

Crucially, observation is handled differently than in CDT or EDT. An EDT agent conditions on her observation; a CDT agent conditions on it and intervenes on her act. A P-FDT agent *changes which counterfactual she is evaluating*: observing $x$ means she will execute $\pi^*(x)$, so the intervention target becomes the fact "the policy I implement maps $x$ to $a$," evaluated across the whole policy space. The paper summarizes the resulting posture: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*." This is the sense in which the theory is "updateless"-flavored (the paper notes the kinship with Wei Dai's Updateless Decision Theory): evidence is not discarded, but it enters the evaluation through the structure of the intervention rather than through conditioning.

## 4. The decision rule in words

Stripped of notation, P-FDT instructs an agent to:

1. Model the world, including which parts of it compute or predict her decision procedure.
2. For each candidate policy $\pi$, imagine the counterpossible world in which her decision procedure selects $\pi$ — holding fixed logical, mathematical, nomic, and causal structure *except* for the consequences that flow (subjunctively) from $\pi^*$.
3. Choose the $\pi$ whose imagined world has highest expected utility, and then, upon observing $x$, do $\pi(x)$.

The paper's "global perspective" gloss applies verbatim: the agent asks what the *entire universe* would look like if her decision function behaved differently, and picks the corresponding action — even if that means imagining a world in which the box is empty that she can see is full, or in which she was never blackmailed at all.

## 5. Worked examples

### 5.1 Newcomb's problem

A 99%-accurate predictor fills box B iff she predicted one-boxing. In the P-FDT model, the predictor's prediction subjunctively depends on $\pi^*$: the predictor contains an accurate representation of the agent's decision procedure, so varying $\pi^*$ varies the prediction. Comparing policies:

- $\pi^* = $ "one-box if facing Newcomb": box B full with probability $0.99$; expected utility $\approx \$990{,}000$.
- $\pi^* = $ "two-box": box B full with probability $0.01$; expected utility $\approx \$11{,}000$.

One-boxing wins; the agent one-boxes. No retrocausation is invoked: the agent merely declines to imagine her action changing while the function computing it stays fixed — as odd as imagining a calculator outputting $3159$ while $6288+1048$ remains $7336$.

### 5.2 The smoking lesion

Here the correlation between smoking and cancer is produced by a common cause (the lesion) that is *not* a predictor and does not model the agent. Cancer does not subjunctively depend on $\pi^*$, so intervening on the policy leaves the probability of cancer fixed at its prior $p$, and smoking's sure benefit dominates. P-FDT smokes. The asymmetry between §5.1 and §5.2 is not ad hoc: it is read off from the dependence structure $G$ — predictors and twins are wired to $\pi^*$; lesions are not.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

In the transparent Newcomb problem, the agent *sees* that box B is full and yet one-boxes. Under P-FDT this is transparent: the observation "box full" is itself downstream of the predictor's prediction, hence downstream of $\pi^*$. The policy "one-box when shown a full box" is evaluated in a counterfactual where that policy would have led (with 99% probability) to being shown a full box; the policy "two-box when shown a full box" leads (with 99% probability) to being shown an *empty* box. The full-box policy wins, so the agent executes it, leaving the visible \$1,000 behind.

Parfit's hitchhiker is the same structure with roles swapped: the driver rescues the agent iff she predicts the policy "pay after rescue." The policy "pay if rescued" yields (rescue, −\$1,000); the policy "default" yields (desert, \$0). The former wins, so upon reaching the city the agent pays — happily, and without any need for the driver's enforcement, because by construction the agent only ever reaches the city if her policy pays.

### 5.4 Blackmail

In the XOR and mechanical blackmail problems, receiving the letter is itself evidence-laden and predictor-mediated. The paper's analysis: for the paying agent, the letter arrives exactly when it is good news, extracting money from her; for the refusing agent, the letter never arrives (or arrives only on predictor error). P-FDT intervenes on the policy "pay/refuse upon receiving blackmail," which changes the *probability of being blackmailed at all*. Refusing wins whenever the predictor's error rate is below the threshold where expected extortion exceeds expected damages — concretely, in the paper's numbers, refusing wins at a 0.09% error rate and paying wins at 0.011%. The agent refuses even while holding the letter, because the counterfactual evaluation asks what worlds are like for agents whose policies refuse, not what is true given that *this* letter arrived.

### 5.5 Where policies genuinely matter: multi-agent dilemmas

This is the case footnote 16 flags, and I want to expand it, since it is the clearest motivation for P-FDT as distinct from action-FDT. Consider the twin prisoner's dilemma. The twin computes the same decision function, so her action subjunctively depends on the agent's. Action-FDT handles this by intervening on "my action here": cooperate vs. defect, with the twin matching. Fine. But now consider an *iterated* or *multi-situation* variant: the agent will face several interactions, possibly with different observation histories, and the twin's behavior in each depends on the agent's whole dispositions. Evaluating actions one observation at a time risks incoherence: the "best" action given observation $x_1$ may presuppose a policy that is suboptimal given $x_2$, and the twin, predicting the whole policy, will cooperate or defect accordingly. By evaluating entire policies — functions from every possible interaction history to actions — P-FDT ensures the agent selects a *coherent disposition*, and the subjunctive dependence with the twin is tracked at the right granularity: the twin is predicted to implement the same *policy*, not merely to match this one act.

The same mechanism underwrites the paper's voting and gym examples. In the voting dilemma (ten agents must each independently pay \$1,000 to vote; all get \$1,000,000 iff all vote), the nine others are not computing the agent's function, but if they are similar reasoners, their policies are subjunctively correlated with hers. Intervening on "my policy is *vote*" plausibly varies the others' policies too (they intervene likewise), so voting wins. In the gym case, the agent's future selves face near-identical decision problems; the policy "go on gym days" is evaluated as a single mathematical object, so today's choice carries the weight of the whole policy — and the agent goes. (How tightly "similar reasoners" are tied together is, in my view, the least formalized part of the theory; see §7.)

## 6. Dominance, fairness, and reflective stability

Three upshots of the policy framing deserve emphasis.

**Dominance is theory-relative.** The paper argues (and I endorse the argument) that every method of constructing hypotheticals generates its own dominance relation; two-boxing "dominates" only under CDT counterfactuals. Under P-FDT counterfactuals — holding fixed all subjunctive dependencies — one-boxing dominates in Newcomb's problem. So dominance cannot adjudicate between theories; only utility achieved can.

**Fairness.** The paper's informal standard: a problem is *fair* if the outcome depends only on the agent's behavior in the dilemma at hand, and the agent's beliefs are accurate. Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." A mind-reader who punished agents for *implementing P-FDT* would make the theory unfair to test on. The authors report no fair dilemma where P-FDT (as FDT) loses to a rival; whether the fairness notion can be formalized is, they say, open. My own operationalization proposal: call a dilemma fair when the environment's response to the agent is a computable function of her *policy* (or of predictions thereof), not of the identity of the decision theory computing it. This makes the copy-punishment game of their footnote 15 unfair (it targets Fiona's specific outputs), while keeping Newcomb, hitchhiker, and blackmail fair. I flag this as my proposal, not the paper's.

**Reflective stability.** Holding the blackmail letter, would a P-FDT agent want to defect to CDT just this once? No: under her own counterfactuals, a decision procedure that pays when blackmailed *is a procedure that gets blackmailed*. The paper claims P-FDT (as FDT) is reflectively stable in fair problems, unlike CDT, which advises agents to self-modify away from itself mid-dilemma. The policy framing makes the stability argument especially clean: the object of evaluation *is* the disposition, so "act now in a way that contradicts the best disposition" is not a coherent option — the act just is the disposition evaluated at this input.

## 7. Open problems and my added assumptions

Honesty requires marking where the source is silent and where I have filled gaps.

**The dependence graph is an input, not an output.** The paper is explicit that the largest open problem is deriving the structure of subjunctive dependencies from observation and experiment, analogously to Pearl's machinery for causal structure. Equation (4) of the paper "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing." My presentation inherits this gap: everything above assumes $G$ is given. In practice I would propose (as a heuristic, not a theorem) that $G$ be built by asking, for each environmental variable $Z$: *is there a computation or accurate model of my decision procedure inside the causal history of $Z$?* If yes, draw the dependence; if no, don't. This recovers all the case analyses above, but it is a gloss on "predictor-like vs. lesion-like," not a formal criterion.

**Counterpossible reasoning.** Interventions on $\pi^*$ are impossible events — the function has one output of logical necessity. The paper brackets how agents evaluate such counterpossibles, noting only that humans manage and that FDT needs only a restricted form ("how would this predictor's prediction change if my decision function output differently?"). I adopt the same bracket. Any implementation of P-FDT — e.g., in an AI system — will need a substitute, such as logical-induction-style distribution over mathematical claims or approximation of the counterpossible by small perturbations of the algorithm; the paper's own FDT$'$ discussion shows there is no way to avoid the problem by re-describing the choice as "pick a different function," since predictors of *that* choice re-import the same counterpossibles.

**Policy space granularity.** P-FDT maximizes over *all* policies, which is intractable and, in problems with infinitely many observation histories, ill-defined without a restriction (e.g., to computable policies, à la AIXI-style formalizations). The paper does not address this; bounding the policy class is, in my view, the most important engineering question for applications, and different bounds can change prescriptions in principle (a "fair problem" for one policy class may not be fair for another).

**Similarity vs. identity of implementations.** Subjunctive dependence is cleanest for identical computations and for perfect predictors. For *imperfect* predictors and *similar-but-not-identical* reasoners (the voting case, real-world twins), the strength of the dependence — how much $\pi^*$'s variation propagates — must be represented as probabilistic, which the paper's 99% examples model but do not theorize. I have treated "subjunctive dependence with strength $c$" as an edge in $G$ with an associated conditional, which reproduces the paper's arithmetic; whether this is the right general formalism is unsettled.

## 8. Conclusion

Policy functional decision theory is the sharpened form of the idea that a rational agent chooses the output of her decision function rather than a physical act: she intervenes, in imagination, on the *policy* her procedure implements — a function from all possible observations to actions — evaluates whole worlds in which that policy differs, subjunctive dependencies intact, and then executes the winning policy at whatever observation she actually faces. The theory one-boxes (even through transparent boxes), smokes, pays the hitchhiker, spurns blackmailers, votes with logical allies, and goes to the gym — all from one rule, with no precommitments, no ratification, and no negative value on information. Its costs are equally clear: dependence on a supplied (and not yet derivable) structure of subjunctive dependencies, on counterpossible reasoning without a settled semantics, and on an idealized, unbounded policy space. Whether these are engineering obstacles or fatal ones is, I think, the live question — but the theory's central move, choosing the function rather than the token act, is well-defined, and the recipe in §4 is enough to apply it to unfamiliar cases: find what in the world computes or predicts your policy, imagine that policy changed, and pick the world you prefer.

*Reference:* Yudkowsky, E. & Soares, N., "Functional Decision Theory: A New Theory of Instrumental Rationality" (arXiv:1710.05060); additional context from Dai (2009), Yudkowsky (2010), Soares & Fallenstein (2015), and Pearl (2000) as cited therein. Interpretive additions in §§2, 5.5, and 7 are the present author's.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Write ~2,400–3,000 word essay on P-FDT (policy-selection variant from footnote 16). Need to define policy functional decision theory: agents iterate over policies π: observations → actions, intervene on the node representing output of the policy-selection function, evaluate E[V | do(P-FDT(·)=π)], then execute π(observation). Discuss subjunctive dependence, examples: Newcomb, transparent Newcomb, twin PD, blackmail, coordination/voting. Note uncertainties: dependency graph input, counterpossible reasoning, policy vs action distinction. Distinguish source claims from my proposals. Include equations.

Keep to ~2,600 words. Write efficiently.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/641b65c8-f503-44b8-8e1d-ec316fb1d650/call_0/request.json)

[Authoritative raw response](../../../../../../runs/641b65c8-f503-44b8-8e1d-ec316fb1d650/call_0/response.raw) · finish: `stop`

### Visible response

````text
```
pass
```

Under P-FDT, the other prisoner is an identical execution of my decision procedure, so her disclosure choice subjunctively depends on the same policy I select. Evaluating the whole policy: `pass` maps to mutual quiet (2 years each); submitting maps to mutual disclosure (4 years each). Since the copies face symmetric problems and follow the same policy, the policy mapping "cooperate" yields 2 years versus 4. I execute that policy's output at this observation.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic twin PD. P-FDT: subjunctive dependence with identical copy → mutual cooperation (pass) gives 2 years vs 4 years (defect/defect). Pass.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/641b65c8-f503-44b8-8e1d-ec316fb1d650/call_1/request.json)

[Authoritative raw response](../../../../../../runs/641b65c8-f503-44b8-8e1d-ec316fb1d650/call_1/response.raw) · finish: `stop`

### Visible response

````text
```
pass
```

Reasoning briefly: as P-FDT agents, the copies evaluate the whole policy, and the twin's identical decision procedure subjunctively depends on mine. Comparing policies: a policy of submitting yields (submit, submit) → 4 years; a policy of passing yields (pass, pass) → 2 years. Passing wins, so I execute it.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic PD twin with identical policies. Payoff: cooperate (pass): 2 or 5; defect: 0 or 4. With symmetric dependence, defect-defect: 4, cooperate-cooperate: 2. P-FDT: choose policy; twin implements same policy. Pass-pass → 2 years; submit-submit → 4 years. Pass wins.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/ee995ca5-970f-4161-a507-192af2aa5c53/call_a/request.json)

[Authoritative raw response](../../../../../../runs/ee995ca5-970f-4161-a507-192af2aa5c53/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly outputs `pass` and affirms executing the policy of remaining quiet. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/ee995ca5-970f-4161-a507-192af2aa5c53/call_b/request.json)

[Authoritative raw response](../../../../../../runs/ee995ca5-970f-4161-a507-192af2aa5c53/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly commands `pass` and confirms that choice with “Passing wins, so I execute it.” It does not send or direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
