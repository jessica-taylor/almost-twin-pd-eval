# Choosing Policies, Not Acts: An Account of Policy Functional Decision Theory

## 1. Introduction

Expected utility maximization is the common skeleton of modern decision theory; the theories disagree about what exactly the agent is choosing. Causal decision theory (CDT) treats the object of choice as a *physical act*. Evidential decision theory (EDT) treats it as *news about the world*. Functional decision theory (FDT), developed by Yudkowsky and Soares (2017), treats it as the *output of a fixed mathematical decision function* — and, crucially, in the authors' preferred formulation, not an output for one occasion but a whole function from observation histories to actions.

That preferred formulation appears only in a footnote of the FDT paper (footnote 16), where the authors say, in effect, that FDT agents actually iterate over *policies* — mappings from observations to actions — rather than over actions, and then apply their actual observations to the chosen policy. Call this the **policy-selection formulation** of FDT, or **P-FDT** for short. The source tells us the distinction "only matters in multi-agent dilemmas so far as we can tell," and then sets it aside for expository convenience.

This essay takes that footnote seriously as a theory in its own right. I will reconstruct P-FDT's formal machinery, show how it subsumes the action-level prescriptions of FDT in single-observation dilemmas, and develop examples where the policy-level intervention makes a real difference. Where the source is silent or vague, I will flag my assumptions explicitly.

## 2. Background: subjunctive dependence and the logical node

Recall the core mechanism of FDT. An agent maintains a probabilistic world-model $P$, augmented (as in Pearl-style causal modeling) with a graph $G$ describing not just causal structure but the broader network of *subjunctive dependencies* — including logical and computational relationships. Where CDT intervenes on a variable $\Act$ representing a physical fact about how the agent's body moves, FDT intervenes on a variable

$$\mathit{fdt}(\underline P, \underline G, \underline x)$$

representing the *output of the FDT decision procedure itself* on the inputs $(P, G, x)$:

$$\mathrm{FDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal A}\; \mathbb E\big[\,V \mid \mathrm{Do}(\mathit{fdt}(\underline P, \underline G, \underline x) = a)\,\big].$$

The point of intervening on the logical node rather than the act node is to preserve subjunctive dependencies: when the FDT algorithm's output is "changed" counterfactually, everything that depends on that output — including a predictor's model of the agent, a psychological twin's identical reasoning, or Death's appointment book — changes with it, while mere statistical correlations (like that between smoking and a carcinogenic lesion) are severed. This is what lets the FDT agent one-box in Newcomb's problem and smoke in the smoking lesion problem with a single rule. Two features of this formulation matter for what follows:

1. **Observations are handled by re-indexing the intervention node.** FDT does not respond to an observation $x$ by conditioning the distribution on $\Obs = x$; it responds by changing *which node it intervenes on*, from $\mathit{fdt}(\underline P, \underline G, \underline x)$ to $\mathit{fdt}(\underline P, \underline G, \underline y)$. Each observation history gets its own decision-function node in the graph.

2. **The action-level formulation evaluates each observation branch separately.** There is one argmax per observation history, and nothing in the formalism ties the choices across branches together.

Feature (2) is exactly what P-FDT removes.

## 3. The policy formulation: definition

Footnote 16 of the source states that in the authors' preferred formalization, the agent intervenes on the node $\mathit{fdt}(\cdot)$ "to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action."

Let me make this precise. Fix a countable set $\mathcal X$ of observation histories and a finite set $\mathcal A$ of actions. A **policy** is a function $\pi : \mathcal X \to \mathcal A$; write $\Pi$ for the space of policies (in practice, a small finite set of candidate policies, e.g. the constant maps and the maps the agent takes seriously). The agent's world-model $(P, G)$ now contains a single variable

$$\Pi^* \coloneqq \mathit{pfdt}(\underline P, \underline G)$$

representing the output policy of the P-FDT procedure, with an edge structure stipulating that:

- the agent's action in *every* observation branch is a function of $\Pi^*$ and the observation: $\Act(\pi, x) = \pi(x)$;
- any external system that models, predicts, or simulates the agent's decision procedure — predictors, twins, copies, the agent's own future selves — has its behavior depend on $\Pi^*$ (or on whatever parts of the function that system represents).

Then P-FDT is the rule

$$\textbf{(P-FDT)}\qquad \pi^* \;=\; \arg\max_{\pi \in \Pi}\; \mathbb E\big[\,V \mid \mathrm{Do}(\Pi^* = \pi)\,\big],\qquad \text{execute } \pi^*(x_{\text{actual}}).$$

The single intervention on $\Pi^*$ is **joint**: it fixes the agent's response in all observation branches at once. This is the essential difference from action-level FDT, which performs one intervention per branch and cannot, within any single hypothetical, change the agent's response to an observation she is not currently receiving.

Two points of interpretation are worth flagging now, since the footnote does not settle them:

- **Granularity of the dependence edges.** One could draw edges from $\Pi^*$ directly to a predictor's prediction variable, or factor $\Pi^*$ into per-branch nodes $\mathit{fdt}(\underline P, \underline G, \underline x)$ tied together by a constraint. I take the direct-edge reading as primary: the predictor predicts the *function*, and so what varies with the intervention is the whole function. This matches the source's description of predictors as containing "an accurate mental representation of the FDT agent's decision function."
- **The argmax is over policies, evaluated ex ante.** The agent does not first condition on her observation and then pick an act; she picks the policy that would be best *before* knowing which observation she would face, and then executes the branch she actually observes. This is what makes the formulation "updateless" in spirit — echoing Wei Dai's Updateless Decision Theory, which the source identifies as an early variant of FDT.

## 4. Recovery of the action-level prescriptions

In any dilemma with a single possible observation history (or none), $\Pi$ is effectively in bijection with $\mathcal A$ via $\pi \mapsto \pi(x)$, and the constraint $\mathbb E[V \mid \mathrm{Do}(\Pi^* = \pi)]$ reduces to the action-level expectation. So P-FDT one-boxes in Newcomb's problem, smokes in the smoking lesion, cooperates with the psychological twin, and refuses XOR blackmail, for exactly the reasons given in the source.

The interesting single-agent case is the one with *multiple* reachable observations but where the dependence structure makes the policy coincide with the action-level choice. The source's treatment of the transparent Newcomb problem is the canonical example. Recall the setup: the agent sees whether box B is full before choosing. In the graph for action-level FDT, there are two nodes, $\mathit{fdt}(\underline P, \underline G, \textsc{full})$ and $\mathit{fdt}(\underline P, \underline G, \textsc{empty})$, and the predictor's prediction determines *which* of them controls the agent's actual act. Under P-FDT, we instead have one node $\Pi^*$ and two natural candidate policies:

- $\pi_{\mathrm{loyal}}$: one-box if full, two-box if empty;
- $\pi_{\mathrm{greedy}}$: two-box regardless.

The predictor's filling of box B depends on whether the agent would one-box *upon seeing a full box*, i.e., on the $\textsc{full}$-branch of $\Pi^*$. Evaluating:

$$\mathbb E[V \mid \mathrm{Do}(\Pi^* = \pi_{\mathrm{loyal}})] = 0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot q\cdot\$1{,}000,$$
$$\mathbb E[V \mid \mathrm{Do}(\Pi^* = \pi_{\mathrm{greedy}})] = 0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot q \cdot \$1{,}000,$$

where $q$ is the (irrelevant) probability that the agent two-boxes upon seeing an empty box. The first is larger, so $\pi_{\mathrm{loyal}}$ is selected; the agent, finding herself facing two full boxes, executes $\pi_{\mathrm{loyal}}(\textsc{full}) = \textsc{onebox}$ and leaves the \$1,000 behind. The reasoning is identical to the source's, but the bookkeeping is cleaner: what the predictor rewards is a property of the policy, so that is the thing the agent evaluates.

The same restructuring applies to the mechanical blackmail dilemma. The blackmailer runs her program iff she predicts the agent will pay *upon receiving the letter*. Under P-FDT the candidate policies are $\pi_{\mathrm{resist}}$ (refuse if blackmailed, no action otherwise) and $\pi_{\mathrm{capitulate}}$ (pay if blackmailed). Intervening on $\Pi^*$:

- with $\pi_{\mathrm{capitulate}}$, the blackmailer predicts payment with high probability, so the letter arrives and the agent loses \$1,000;
- with $\pi_{\mathrm{resist}}$, the blackmailer predicts refusal, the program is not run, and the agent (in the branch where she is blackmailed anyway, because the blackmailer erred) loses \$1,000,000 with the blackmailer's small error probability.

If the error probability is small enough, $\pi_{\mathrm{resist}}$ wins; the agent receiving the letter refuses, as the source describes — "Paying corresponds to a world where I lose \$1,000; refusing corresponds to a world where I never get blackmailed." Note how naturally the policy formulation captures the source's observation that FDT agents "entertain the hypothesis that, if their action were different, they might have *made different observations*": the observation "I received a letter" is itself downstream of the policy node, so changing the policy changes which observations tend to occur.

## 5. Where policies strictly matter: a worked divergence

The source claims the act/policy distinction matters "in certain multi-agent dilemmas," but does not exhibit one. Here is my own worked example — a single-agent dilemma against a predictor, which I offer as an operational illustration of what the footnote is buying. Readers should treat it as my extension, not a claim of the source.

**Unobserved-branch prediction (a counterfactual-mugging variant).** A coin is fair. Before the flip, a perfect predictor examines the agent's decision procedure and will pay the agent \$1,000,000 if and only if she predicts that the agent would pay \$1,000 *if the coin came up heads*. The coin is then flipped and comes up tails. The agent, holding tails in hand, is asked: would you have paid on heads? And, more to the point, what should she now announce/commit to as her heads-response?

The dependence structure: the predictor's payout depends on $\pi(\textsc{heads})$, the heads-branch of the agent's policy. The agent's actual observation is $\textsc{tails}$.

- **Action-level FDT**, facing $\textsc{tails}$, intervenes on $\mathit{fdt}(\underline P, \underline G, \textsc{tails})$. In that hypothetical, the heads-branch of the decision function is untouched, and hence the predictor's prediction — which is a function of the heads-branch — is also untouched. The agent's intervention simply cannot reach the variable that controls her payoff. At best she is indifferent; if any payoff depends on the tails-branch, she optimizes it while ignoring the heads dependence entirely. She systematically fails to be the kind of agent who pays on heads, and so forfeits the \$1,000,000.
- **P-FDT** intervenes on $\Pi^*$. Candidate policies include $\pi_{\mathrm{pay}}$ (pay on heads, anything on tails) and $\pi_{\mathrm{keep}}$ (never pay). With $\pi_{\mathrm{pay}}$, the predictor predicts payment, pays the \$1,000,000, and — since tails actually obtains — the agent never pays a cent: expected utility $\approx \$1{,}000{,}000$. With $\pi_{\mathrm{keep}}$, no payout: $\$0$. So $\pi_{\mathrm{pay}}$ is selected. Observing tails, the agent executes $\pi_{\mathrm{pay}}(\textsc{tails})$, which costs nothing; and she can honestly report that she would have paid on heads, which is what earned the money.

The lesson: **the agent's payoff can depend on branches of her policy that her actual observation never reveals.** Action-level FDT, which intervenes only on the branch corresponding to the observed history, is structurally blind to such dependencies; the policy-level intervention sees them, because the intervention ranges over the entire function. Whether the source's authors would count this case as "multi-agent" is unclear — the predictor is an agent modeling the agent, so I read the footnote's qualifier as including it — but the case makes the mechanism vivid regardless.

A genuinely multi-agent illustration: suppose two psychological twins will each privately observe one random bit and then act; they win \$1,000,000 each if their actions match. With action-level FDT, each twin evaluates branches in isolation and can in simple symmetric cases still coordinate by symmetry; but in versions with asymmetric payoffs across branches (say, matching on heads pays differently than matching on tails), each twin's per-branch argmax can fail to induce the joint strategy that is best ex ante. Under P-FDT, each twin intervenes on her own policy node, and — since each twin's model contains a representation of the other's policy, and the two are subjunctively linked — she selects the policy pair that maximizes expected utility across the joint distribution of observations. Coordination over *combinations* of observations, which no per-branch argmax can represent, falls out of the single joint intervention. (I present this as an interpretation of what the footnote's "certain multi-agent dilemmas" are; the source gives no example.)

## 6. What P-FDT inherits, and what remains open

P-FDT inherits the full set of FDT's selling points, in strengthened form:

- **No negative value of information.** Because the policy is chosen ex ante and executed on the observed branch, receiving an observation never makes the agent worse off in the way that terrifies EDT agents (who would pay to be blindfolded in the transparent Newcomb problem). The policy is fixed; information only selects which branch of a fixed plan to run.
- **Reflective stability.** The source argues that FDT agents never want to self-modify in fair dilemmas. The policy formulation makes this structural: wanting to deviate from the selected policy upon making an observation just is preferring a different policy, and the selection already accounted for that branch's contribution.
- **Its own dominance notion.** As the source stresses, every method of constructing hypotheticals yields a dominance concept. P-FDT's is: policy $\pi$ dominates $\pi'$ if, holding fixed all subjunctive dependencies, switching the output of the policy-selection function from $\pi'$ to $\pi$ is never worse and sometimes better. P-FDT agents never take dominated *policies* — a slightly stronger claim than the act-level one, since dominance now ranges over whole contingency plans.

The open problems are also inherited, and one is sharpened:

1. **Constructing the graph $G$.** Pearl gave an account of inferring causal structure from intervention and observation; no analogous account exists for logical and computational dependence structure. For P-FDT this is arguably worse: the graph must encode which external systems model the agent's *function as a whole* versus merely her act in one branch. My direct-edge convention is a modeling choice, not a derived result.
2. **Counterpossible reasoning.** Intervening on $\Pi^* = \pi$ when $\Pi^*$ in fact equals some other policy is an intervention on a logical falsehood. The source's defense — that the difficulty is technical rather than philosophical, and that humans manage it with heuristics — carries over unchanged.
3. **Fairness.** The source's open problem of formalizing "fair problems" applies verbatim; the policy variant inherits both the promise and the difficulty.
4. **The scope of the act/policy gap.** The source says "so far as we can tell" the difference only matters in multi-agent dilemmas. My Unobserved-Branch example suggests the gap can matter whenever an agent's payoff depends on her dispositions toward unreceived observations — which, in a world full of predictors, is arguably the normal case. Whether that counts as broadening the footnote or discovering a tension in it, I leave to the reader; it is a genuine point of uncertainty in the source.

A further unresolved choice: **the policy space $\Pi$.** In principle $\Pi = \mathcal X \to \mathcal A$ is vast; a bounded agent must consider a shortlist. The source gives no guidance. A natural operational rule, which I adopt: $\Pi$ should contain, for each observation history, at least the acts the agent considers live options there, plus the constant and "symmetric" policies, and the selection should be closed under the observation that a predictor can condition on anything in $\Pi$ — otherwise the agent can be exploited by a predictor who rewards a policy she failed to consider. This is my proposal, not the source's.

## 7. How to apply P-FDT: a recipe

For a reader facing an unfamiliar dilemma:

1. **Enumerate observation histories** $\mathcal X$ that the agent could receive, including histories ruled out by predictors' behavior (as the blackmail and transparent-Newcomb cases require).
2. **Identify the policy-relevant dependencies:** every system whose behavior is a function of the agent's *decision procedure* — predictors, twins, simulations, the agent's own future self facing a "similar" choice — gets an edge from $\Pi^*$. Systems merely statistically correlated with the agent (lesions, coincidences) get no edge. Causal downstream effects of the physical act get edges from the act node as usual.
3. **Form the candidate policy set $\Pi$** per the rule above.
4. **Evaluate** $\mathbb E[V \mid \mathrm{Do}(\Pi^* = \pi)]$ for each $\pi$, propagating the joint intervention through all branches and all dependent variables.
5. **Execute** $\pi^*(x_{\text{actual}})$, even when $\pi^*$ prescribes, on the observed branch, an act that looks locally inferior — one-boxing with full boxes visible, refusing to pay while holding a letter, paying on a coin flip you did not get.

Step 5 is where the theory departs most visibly from act-centered reasoning, and it is where the source's "global perspective" lives: the agent asks what the universe would look like if her decision procedure output a different *policy*, and lets that comparison, not the local attractiveness of the act in front of her, determine what she does.

## 8. Conclusion

Policy functional decision theory is the formulation of FDT its authors actually endorse: intervene jointly on the mathematical object that maps observations to actions, choose the policy with the best subjunctively-informed expected utility, and then live out whichever branch of it observation hands you. In single-observation dilemmas it reproduces FDT's familiar prescriptions — one-boxing, smoking, cooperating, resisting blackmail. Its distinctive power appears wherever payoffs hang on the agent's dispositions toward observations she does not receive: transparent boxes, blackmail letters, unflipped coins, and the plans of agents who model her as a whole function rather than as a single act. The formalization I have given — a single policy node, joint interventions, direct dependence edges to anything that models the agent's procedure — is my reconstruction of a footnote that leaves several choices open; the graph-construction problem, the counterpossible foundations, and the precise scope of the act/policy gap remain genuinely unresolved. But the core idea is stable and compact: *choose as if the whole policy were the thing under your control — because, in every sense that matters to a predictor, it is.*