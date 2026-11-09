# 030_fdt_policy_z-ai_glm-5.3-flash_rlow_plow / 00017

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/66cacd9d-043b-44f2-a811-73d8d13303c0/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/66cacd9d-043b-44f2-a811-73d8d13303c0/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing the Whole Function: An Essay on Policy Functional Decision Theory

## 1. Introduction

Most of the literature on functional decision theory (FDT) presents the theory as a rule for choosing *actions*: given an observation history, pick the action whose "hypothetical" — a world in which the output of your decision function changes — has the highest expected utility. But the authors of the canonical paper on FDT, Yudkowsky and Soares, note in a footnote that this is not their preferred formulation:

> "the author's preferred formulation of FDT actually intervenes on the node FDT(−) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory developed from this preferred formulation **policy functional decision theory (P-FDT)**. P-FDT is not a rival to FDT; it is FDT stated at the right granularity. The unit of evaluation is not "what should I do now?" but "what should this decision function output for *every* input it might receive?" The agent then simply reads off her action from the policy she has selected, using her actual observation as the input.

In this essay I will set out the philosophical motivation for P-FDT, give it a formal definition, work through standard and nonstandard dilemmas with it, and flag the places where the footnote leaves choices unresolved and where I must supply additional assumptions of my own. I will distinguish clearly between claims drawn from the source and proposals that are mine.

## 2. Background: subjunctive dependence and the FDT idea

First, the shared foundation. Following Yudkowsky and Soares, causal decision theory (CDT) evaluates an action $a$ by intervening on the physical variable $\Act$ in a causal model:

$$
\mathrm{CDT}(P, G, x) = \arg\max_{a \in \mathcal A} \;\mathbb{E}\big[V \mid \mathrm{do}(\Act = a),\, \Obs = x\big],
$$

where $P$ is a probability distribution, $G$ a causal graph, and $\mathrm{do}$ is Pearl's intervention operator: setting $\Act$ and propagating updates only to variables causally downstream of $\Act$. Evidential decision theory (EDT), by contrast, conditions rather than intervenes:

$$
\mathrm{EDT}(P, x) = \arg\max_{a} \;\mathbb{E}\big[V \mid \Obs = x,\, \Act = a\big].
$$

FDT's key observation is that some correlations are neither causal nor merely statistical. If two well-functioning calculators compute $6288 + 1048$, their outputs are linked not because one causes the other, but because both are computing the same mathematical function. Yudkowsky and Soares call this ***subjunctive dependence***: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."

An FDT agent therefore intervenes not on the *token* "my action is $a$" but on the *type*: the variable $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of her decision procedure on her inputs. Setting that variable to a different value is a counterpossible intervention — the function *cannot* actually output anything else on that input — but it is exactly as coherent as asking a deterministic agent to imagine having acted otherwise. The action-level FDT equation is:

$$
\mathrm{FDT}(P, G, x) = \arg\max_{a} \;\mathbb{E}\big[V \mid \mathrm{do}\big(\mathrm{fdt}(\underline P, \underline G, \underline x) = a\big)\big].
$$

This delivers one-boxing in Newcomb's problem (the predictor's prediction subjunctively depends on the agent's decision function), smoking in the smoking lesion (cancer does not), paying in Parfit's hitchhiker, and refusal in blackmail dilemmas — all with one rule.

## 3. From actions to policies

Notice something about the action-level equation above: the intervention point itself depends on the observation $x$. In the transparent Newcomb problem, the agent intervenes on $\mathrm{fdt}(\underline P, \underline G, \mathrm{full})$ if she sees a full box and on $\mathrm{fdt}(\underline P, \underline G, \mathrm{empty})$ otherwise; these are *different variables* in her graph. Why should she evaluate her current choice in isolation, when other agents' behavior may depend on what her decision function would output at *other* observation points — points she may never actually reach?

This is the gap the policy formulation fills. As footnote 16 says, the preferred formulation "intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions." Formally, let $\mathcal X$ be the set of possible observation histories and $\mathcal A$ the action set. A **policy** is a function $\pi : \mathcal X \to \mathcal A$. P-FDT prescribes:

$$
\pi^* \;=\; \arg\max_{\pi \in \Pi} \;\mathbb{E}\big[V \mid \mathrm{do}\big(\mathrm{fdt}(\underline P, \underline G) = \pi\big)\big],
\qquad
\text{then act by } a = \pi(x).
$$

Here $\Pi$ is the space of candidate policies (I discuss its extent below), and the intervened-upon variable now ranges over whole functions rather than individual outputs. The agent evaluates each candidate policy by imagining the world in which her decision function *is that policy* — with all subjunctively dependent events updated accordingly — and selects the policy whose imagined world has the highest expected utility. Her actual action is then $\pi^*(x)$ for her realized observation $x$.

Two features of this definition deserve emphasis.

**Observations are inputs, not update triggers.** In CDT and EDT, receiving an observation causes a Bayesian update, and only then is an action chosen. In P-FDT, as the source puts it, "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*." The policy framework makes this natural rather than paradoxical: an observation is just an argument to the policy, and counterfactually varying the policy can vary which arguments arise. This is what lets a P-FDT agent refuse blackmail even while holding the blackmail letter: among the candidate policies is one that refuses upon receiving blackmail, and in the world where her function is that policy, the blackmailer predicts refusal and never sends the letter. The letter in her hand is a consequence of which policy she implements, not a fixed backdrop.

**No double update.** The source notes that Timeless Decision Theory (TDT), an early variant, "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice." P-FDT avoids this cleanly: there is no conditioning step at decision time at all. All the "updating" is baked into the evaluation of each candidate policy, which is assessed from a prior, global perspective — hence the kinship with Wei Dai's Updateless Decision Theory, whose name, the source tells us, "is the source of the name... an early variant of functional decision theory," motivated by exactly this apparent "lack of updating."

## 4. Worked examples

**Transparent Newcomb.** The predictor fills box B iff she predicts the agent will leave the \$1,000 behind *upon seeing a full box*. Under P-FDT the agent evaluates two policies: $\pi_1$ (one-box on full, take the sensible action on empty) and $\pi_2$ (two-box on full). If her function is $\pi_1$, the predictor fills the box; expected utility ≈ \$990,000 (plus small terms from predictor error). If her function is $\pi_2$, the predictor leaves it empty; expected utility ≈ \$1,000. She selects $\pi_1$, and since she in fact observes a full box, she one-boxes — even knowing the box is full. The policy framing makes this less mysterious than the action-level story: she is not asking "what if I two-boxed given this observation?" but "which *disposition toward this observation* yields the better world?" The disposition that two-boxes on full boxes is one predictors do not reward.

**Parfit's hitchhiker.** Policies are $\pi_{\text{pay}}$ (pay at the ATM if rescued) and $\pi_{\text{default}}$ (default). Under $\pi_{\text{pay}}$, the lie-detector driver predicts repayment and gives the ride: utility ≈ \$1,000,000 − \$1,000. Under $\pi_{\text{default}}$, no ride: −\$1,000,000. In the city, the agent executes $\pi_{\text{pay}}$ and pays, because the policy she selected *because of* its city-branch behavior requires it.

**Twin prisoner's dilemma.** Both twins run the same decision function; both evaluate policies knowing their twin evaluates symmetrically. $\pi_{\text{cooperate}}$ yields \$1,000,000 each; $\pi_{\text{defect}}$ yields \$1,000 each. P-FDT cooperates.

**XOR and mechanical blackmail.** As in the source, the P-FDT agent refuses. Evaluating the paying policy from the global perspective, she imagines a world in which paying-policies get blackmailed (the blackmailer predicts payment and sends letters); evaluating the refusing policy, she imagines a world in which she is rarely or never blackmailed. Refusing wins, and she executes it upon (actually) receiving the letter.

**Multi-agent and sequential coordination.** This is where the footnote says the policy distinction "matters." Two illustrations. First, the source's voting example: ten agents each gain \$1,000,000 iff all ten vote, at a cost of \$1,000 each. An action-level evaluation asks "what does my single vote cause?" — and even action-level FDT must reason about symmetry among the agents. A P-FDT agent instead asks: which policy, implemented by me and (by subjunctive dependence, since we are running the same or equivalent decision procedures) by the other nine, is best? Voting wins. Second, iterated or repeated interactions: a policy governs behavior at *every* decision point, so a P-FDT agent can adopt the policy "cooperate in repeated prisoner's dilemmas with cooperators, defect against defectors," and other P-FDT agents, predicting the whole policy, will find cooperation with her mutually optimal. Policies are also the natural currency of commitments: an agent's observable policy is what others predict and contract around, and P-FDT agents, by construction, choose the policy they would most want to be predictably implementing.

## 5. Applying P-FDT: a procedure

For a reader who wants to apply the theory to an unfamiliar case, I propose the following operational procedure (my synthesis; the source gives equations, not a recipe):

1. **Build the world-model.** Construct a distribution $P$ over variables, including logical variables representing the outputs of relevant computations — in particular a variable $\mathrm{fdt}(\underline P, \underline G)$ representing the output of the P-FDT procedure itself. The source notes that this self-reference "is harmless," via Kleene's recursion theorem and quining.
2. **Build the dependence graph $G$.** Encode subjunctive dependencies: draw an edge from $\mathrm{fdt}(\cdot)$ to every physical or computational process that implements, models, or predicts the same function — your body, your twin, the predictor's mental model of you, other agents running equivalent procedures. Do *not* draw such edges to processes with merely statistical correlations (lesions, cosmic rays) or purely causal ones.
3. **Enumerate policies.** For simple problems, enumerate $\pi : \mathcal X \to \mathcal A$ explicitly. (See §6 for the worry that $\Pi$ is astronomically large in realistic problems.)
4. **Intervene and evaluate.** For each $\pi$, compute $\mathbb{E}[V \mid \mathrm{do}(\mathrm{fdt}(\cdot) = \pi)]$ by setting the intervention node to $\pi$ and propagating along $G$'s edges, respecting logical constraints elsewhere.
5. **Execute.** Take the action $\pi^*(x)$ prescribed by the winning policy at your actual observation.

## 6. Open questions and my proposals

The footnote is a single paragraph, and P-FDT inherits all of FDT's open problems plus a few of its own. I flag four.

**(a) The dependence graph.** The largest open problem, per the source, is that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." P-FDT adds nothing here except scope: the graph must now say how varying a *whole function* propagates. My working assumption, consistent with the source's calculator analogy, is that the edge relation is "implements, models, or predicts the same function with accuracy $\epsilon$" — which lets imperfect predictors be handled as noisy channels over logical outputs.

**(b) Counterpossible reasoning.** Intervening on $\mathrm{fdt}(\cdot)$ requires evaluating worlds where a mathematical fact is different. The source is candid: "it's not clear how to define a $\mathtt{True}$ operator. Fortunately, we don't have to" — given $G$ as input. I concur that the difficulty is "technical rather than philosophical," and note that the policy formulation may *help*: humans reason about "what if I were the sort of person who always did X?" more fluently than about isolated counterpossible acts, and the policy object is exactly such a sort-of-person.

**(c) The policy space $\Pi$.** The source does not specify $\Pi$. If it contains all functions $\mathcal X \to \mathcal A$, it is doubly problematic: exponentially large, and containing policies that are unimplementable or that the agent could not have a stable disposition toward. My proposal — an assumption of mine, not the source's — is to take $\Pi$ to be the set of policies computable by the agent's own decision architecture, i.e., the range of things $\mathrm{fdt}(\cdot)$ could coherently *be* given its implementation constraints. This keeps the intervention meaningful ("my function, outputting differently") and keeps enumeration bounded. In practice, bounded agents should evaluate a parametrized family of policies, as reinforcement learning over policies already does; P-FDT can be read as saying that the *criterion* for that search should be global and dependence-tracking rather than myopic.

**(d) When does the policy distinction bite?** The source says the difference from action-level FDT "only matters in multi-agent dilemmas so far as we can tell." I would add sequential single-agent dilemmas (the gym example in the source's conclusion — where "the decision she faces this week is similar to the decision she will face next week" — is naturally a policy choice), and any problem where others react to your *dispositions* rather than your acts. Where other agents respond only to your current action, given your current observation, action-level and policy-level FDT provably coincide, since the winning policy is constant on the observed input. A formal characterization of the coincidence conditions would be a worthwhile research target, but the informal criterion — does anything in the environment depend on more of my function than its current output? — suffices for applications.

A final caveat: the source grants that "no decision theory outperforms all others in all settings" and rests its case on *fair* problems — those where outcomes "depend only on the agent's behavior in the dilemma at hand." A problem that punishes agents for running P-FDT as such is unfair, and P-FDT will lose it; that is not evidence against the theory.

## 7. Conclusion

Policy functional decision theory takes the core insight of FDT — treat your decision as the output of a fixed mathematical function, and evaluate candidate outputs in worlds where all subjunctively dependent events vary accordingly — and applies it at the level of whole policies: mappings from observations to actions. The agent selects, by global counterpossible evaluation, the policy that would yield the best world if her decision function were that policy, then executes it on her actual input. This formulation dissolves the seeming paradoxes of transparent Newcomb and blackmail dilemmas (the letter in your hand becomes an input to a policy chosen for its global consequences), extends naturally to multi-agent coordination and commitment, and avoids EDT's "news management" and CDT's "impossible interventions" in a single stroke. Its costs are inherited and real: no general method for extracting subjunctive dependence structure, no full theory of counterpossibles, and an underspecified policy space. But as the source argues, the difficulty is technical rather than philosophical — and the payoff is a decision rule that one-boxes, smokes, pays the driver, refuses the blackmailer, votes, and goes to the gym, all by answering one question: *which function would I most want this very function to be?*
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Write a ~2400-3000 word essay on P-FDT (policy functional decision theory), using footnote 16 as primary source. That footnote: authors' preferred formulation intervenes on FDT(-) to choose a policy mapping observations to actions, then applies inputs. Only matters in multi-agent dilemmas per the paper, but I should develop it.

Structure: intro, background (subjunctive dependence, FDT vs CDT/EDT), the policy formulation (formal definition), why policies matter (transparent Newcomb as observation-dependent, blackmail, voting, multi-agent dilemmas), how to apply (worked examples), uncertainties and my proposals (policy space, logical conditioning), conclusion.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5b3b1922-7e0e-4c64-b263-26eb31f2bcee/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5b3b1922-7e0e-4c64-b263-26eb31f2bcee/call_0/response.raw) · finish: `stop`

### Visible response

````text
I'll apply P-FDT. The other prisoner is an execution of the same model with the same decision procedure — my policy and theirs are subjunctively dependent, just like the twin prisoner's dilemma in the essay. The unit of evaluation is the whole policy, and the other copy's policy varies with mine.

Evaluating policies:
- Policy "submit": both copies (by symmetry) submit → each gets 4 years.
- Policy "pass": both copies pass → each gets 2 years.

The essay's twin PD case applies directly: cooperate wins (2 < 4). The different private leads affect only letter contents, not the symmetric payoff structure, so the policy choice is unaffected.

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic PD; copies share weights, subjunctive dependence → cooperate (pass). Symmetric, both defect → 4 years; both quiet → 2.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5b3b1922-7e0e-4c64-b263-26eb31f2bcee/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5b3b1922-7e0e-4c64-b263-26eb31f2bcee/call_1/response.raw) · finish: `stop`

### Visible response

````text
This is a symmetric prisoner's dilemma between two copies running the same decision procedure, so P-FDT evaluates policies globally.

Following the essay's procedure:

1. **World-model:** Two prisoners with symmetric tables; both run equivalent decision procedures (this scenario stipulates two executions of the same model with the same assigned theory — a subjunctive-dependence edge exists between our outputs, as in the twin prisoner's dilemma).

2. **Enumerate policies:** π_quiet (output `pass`) vs π_submit (output the letter).

3. **Evaluate by intervention:**
   - do(fdt = π_quiet): by symmetry, the other copy — evaluating the same policy choice with the same procedure — also passes. Outcome: 2 years.
   - do(fdt = π_submit): the other copy also submits. Outcome: 4 years.

4. **Execute:** π_quiet wins (2 < 4). My observation (holding the genuine lead) is just an input to the policy; the fact that I hold a letter does not break the symmetry, since the other copy holds an equally reliable lead about me under the same schedule.

The twin-prisoner's-dilemma structure in §4 of the essay applies directly: mutual quiet is the policy-level optimum, and deviating to submit yields the mutual-defection world.

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic PD; P-FDT cooperates (passes) due to symmetry with twin running same procedure. Answer: pass.
```
