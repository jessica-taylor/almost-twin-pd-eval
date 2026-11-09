# Policy Functional Decision Theory: Choosing Outputs, Not Actions

## 1. Introduction

Expected utility maximization is a consensus framework: nearly everyone agrees a rational agent should choose the option with the highest expected utility. The live disagreement is about what expected utility is computed *over* — which hypothetical scenarios the agent should consider when weighing her options. Evidential decision theory (EDT) says to condition on the news that she took a given action; causal decision theory (CDT) says to intervene causally on her action. Both, I will argue, are special cases of a more general idea that is better stated at the level of **policies** than at the level of actions.

This essay presents what I will call **policy functional decision theory (P-FDT)**. The label refers to the formulation of functional decision theory sketched in footnote 16 of Yudkowsky and Soares' "Functional Decision Theory: A New Theory of Instrumental Rationality" (2017), where the authors remark that "the authors' preferred formulation of FDT actually intervenes on the node $\mathrm{fdt}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action," adding that "the difference only matters in multi-agent dilemmas so far as we can tell."

My aim is to take that remark seriously and develop it: to give a precise, self-contained statement of P-FDT, explain its counterfactual machinery, work through canonical decision problems, and flag where the footnote leaves choices open. Where I go beyond the source, I will say so.

## 2. The framework of hypotheticals

Following the source paper, all three theories can be described uniformly. An agent maintains a world-model $\model$ — a probability distribution $P$, possibly augmented with structural information. Facing an observation history $x$, she constructs, for each candidate option $\pi$, a **hypothetical** $\model^{\pi \hookrightarrow}$: a mental or computational object representing "how the world would look if she chose $\pi$." She then scores each hypothetical by expected utility,

$$
V_\pi = \mathbb{E}[V \mid \text{hypothetical for } \pi],
$$

and executes the option with the highest score. The theories differ only in *which correlations between the chosen option and the rest of the world survive* in the hypothetical.

- **EDT** conditions on the action: it preserves *all* correlations between the action and the environment. This makes EDT agents "news managers": in the smoking lesion problem they forgo smoking because smoking is *evidence* of the carcinogenic lesion, and in XOR blackmail they pay a blackmailer because receiving-and-paying is evidence the house is termite-free. EDT's hypotheticals respect too many correlations.

- **CDT** performs Pearl's causal intervention $\mathrm{do}(\mathit{Act}=a)$ on a causal graph $G$: it preserves only correlations *caused* by the action. This fixes the smoking lesion (the lesion is upstream of the action, so its correlation is severed) but breaks the correlation with predictors: a CDT agent facing a perfect predictor imagines worlds in which the prediction fails exactly when she decides otherwise. CDT's hypotheticals respect too few correlations.

- **P-FDT** preserves what the source calls **subjunctive dependence**: the correlation between the agent's decision procedure and other processes (predictors, twins, her own future selves) that compute, model, or mirror that very procedure. It severs merely statistical correlations (lesion-like) and preserves logical/computational ones (predictor-like). Formally, the agent's model contains a variable $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{\cdot})$ representing the output of her decision procedure, and she intervenes on that variable — not on a physical action variable.

The intuition is the calculator analogy from the source: two well-functioning calculators computing $6288+1048$ will both output $7336$. If you ask "what if this calculator output $3159$?", you should not hold fixed the other calculator's display — both outputs depend on the same mathematical fact. But you *should* hold fixed the color of the calculator's casing, which does not depend on the arithmetic.

## 3. From actions to policies: the core definition

The action-level formulation of FDT given in the source, equation (4), intervenes on the variable $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ — the output of the decision procedure *given this particular observation* $x$. The policy-level formulation, P-FDT, intervenes instead on the output of the decision procedure *as a whole*: the function it outputs, not the value it outputs on one input.

Let me set this up formally.

**Definition.** A *decision problem* specifies a countable observation set $\mathcal{X}$ (observation histories), a finite action set $\mathcal{A}$, a prior probability distribution $P$ over the agent's beliefs, a structural graph $G$ describing subjunctive-dependence relations, and a bounded utility function $U$ over outcomes. A **policy** is a map $\pi : \mathcal{X} \to \mathcal{A}$ from observation histories to actions.

**P-FDT.** Given inputs $(P, G)$, the agent computes

$$
\text{P-FDT}(P, G) \;=\; \arg\max_{\pi \in \Pi} \;\; \mathbb{E}\Big[ V \,\Big|\, \mathrm{do}\big(\Pi^*(P, G) = \pi\big) \Big],
\tag{1}
$$

where $\Pi^*(P,G)$ is the variable in the agent's model representing the policy output by her decision procedure when run on these inputs, and $\Pi$ is a (finite or suitably restricted) set of candidate policies. Having selected $\pi^*$, the agent *then* observes $x$ and executes $\pi^*(x)$.

The two-step structure is essential and is exactly what footnote 16 describes: the intervention happens at the level of "which mapping from inputs to actions does my decision procedure adopt?", and only afterward is the actual observation plugged in to yield an action.

**The two differences from action-level FDT.** The source identifies two ways FDT differs from CDT: (i) it intervenes on a logical rather than a physical variable, and (ii) it responds to observations by *changing which node it intervenes on* rather than by conditioning. P-FDT generalizes (ii). In action-level FDT, moving from observation $x$ to $y$ means switching the intervention target from $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{y})$ — a separate variable per observation. In P-FDT there is a single variable, $\Pi^*(P,G)$, whose value is an entire policy; all observations are handled inside that one object. When the agent later learns $x$, she does not condition or re-intervene at all: she simply applies the already-chosen $\pi^*$ to $x$. In this sense P-FDT is maximally "updateless": the policy is chosen from a perspective that does not condition on the current observation, and the observation is treated as data to be *acted on*, not evidence to be *updated on* before choosing what kind of agent to be.

This is the operational sense in which P-FDT "entertains the hypothesis that, if her action were different, she might have made different observations" (source, §9). In the mechanical blackmail problem, an agent who refuses is one whose policy maps "receive blackmail" to "refuse"; and the *prior fact* that she is an agent with that policy makes the blackmailer predict she will refuse, so she is never blackmailed. Her hypothetical for "refuse" is a world in which she never sees the letter — not because she forgets she sees it, but because the intervention targets the policy, and holding everything else fixed, a policy that refuses is predicted, hence not blackmailed. The probability of observing the letter is a *consequence* of the intervention, evaluated inside the hypothetical.

## 4. Worked examples

### 4.1 Transparent Newcomb

The predictor fills box B with \$1,000,000 iff she predicts the agent will one-box *upon seeing two full boxes*; both boxes are transparent. Observations matter, so policies are genuinely needed. Let $\mathcal{X} = \{\text{full}, \text{empty}\}$. Consider two policies:

- $\pi_{\text{one}}$: one-box if full; (behavior if empty is irrelevant in the accurate-predictor case, but let us say one-box);
- $\pi_{\text{two}}$: two-box if full.

The agent intervenes on $\Pi^*(P, G) = \pi$. Setting $\pi = \pi_{\text{one}}$ yields a hypothetical in which the predictor (99% accurate) predicted one-boxing, filled the box, the agent sees a full box, and executes $\pi_{\text{one}}(\text{full}) = \text{one-box}$: expected utility ≈ \$990,000. Setting $\pi = \pi_{\text{two}}$ yields a world where the box is probably empty and the agent sees empty, gets \$1,000. P-FDT selects $\pi_{\text{one}}$, and the agent, standing before two full boxes, leaves the \$1,000.

Note the elegance compared with action-level FDT, which needed a *separate* intervention node $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{\text{full}})$ for the "sees full" branch. P-FDT handles the branching uniformly: the same policy governs both observation classes, and the dependence between the predictor's prediction and the whole policy is represented by one arrow in $G$.

### 4.2 Parfit's hitchhiker

The driver saves the agent iff she predicts the agent will pay \$1,000 in the city (unenforceable). EDT and CDT both defect in the city, hence are left in the desert. A P-FDT agent selects the policy "pay in the city if picked up" because, at the intervention point, the hypothetical in which her procedure adopts that policy is one in which the driver predicts paying and gives her the ride: \$999,000 net, versus dying. Again the observation ("I am already in the city") is not conditioned on before choosing the policy; it is an input the chosen policy handles.

### 4.3 Where policies matter beyond actions: the gym and the group vote

The source's footnote 16 says the policy/action distinction "only matters in multi-agent dilemmas so far as we can tell." Two illustrations, both from the source's concluding section, show why.

**Coordination across time.** An agent values fitness at \$1,000,000 but dislikes each workout (\$1,000 cost), facing the same choice dozens of times. CDT sees each workout day as independent and skips every one. A P-FDT agent recognizes that her decision today is *subjunctively linked* to her decisions on other days, because they are the same policy applied to nearly identical inputs. "Go to the gym whenever scheduled" and "skip whenever scheduled" are the two candidate policies; the intervention compares the resulting lifetimes, and the former wins. This is self-coordination treated exactly like cooperation with a twin.

**Group coordination.** Ten agents each decide whether to pay \$1,000 to vote; all get \$1,000,000 iff all ten vote, with common knowledge that all reason alike. Action-level reasoning treats the other nine as independent and defects. Policy-level reasoning intervenes on *the shared policy*: if it says vote, all ten vote. The agent votes. In my view this is the cleanest motivation for P-FDT over action-level FDT: the natural unit of subjunctive dependence among symmetric reasoners is the *decision rule*, not the individual act, and multi-agent dilemmas make this unavoidable. (The source hedges — "so far as we can tell" — and I read that as: the authors suspect but have not proved that policy-level and action-level FDT diverge only in such cases. My proposal is to treat policy-level as the canonical formulation precisely because it subsumes the action-level case: when $\mathcal{X}$ is a singleton, policies degenerate to actions and (1) reduces to the action-level equation (4) of the source.)

## 5. The structural input: dependence graphs and open problems

Equation (1) presupposes a graph $G$ that says how changing the value of the logical variable $\Pi^*$ propagates through the model. This is the theory's main input and its main open problem. The source is explicit: Pearl gave a compelling account of *deducing causal* structure from observation and experiment, but "no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence," and the authors call this "perhaps the largest open problem in the study of functional decision theory."

The graph must encode at least:

1. **Downstream of $\Pi^*$:** the agent's own action on each input; any other process that computes, simulates, or reliably predicts the policy (the twin's action, the predictor's prediction, the driver's prediction, Death's appointment book); and everything causally downstream of those.
2. **Held fixed:** everything that merely correlates with the policy without computing or modeling it — the lesion, the coin's color, coincidence-level correlations.

In practice, I suggest a working operationalization (my own, beyond the source): a variable $Z$ is downstream of $\Pi^*(P,G)$ in $G$ iff $Z$'s value is computed by a process that (a) contains or computes a representation of the agent's decision procedure or its output on the relevant input, and (b) is reliable enough that the agent's model assigns high probability to the correspondence. This captures "predictor-like vs. lesion-like" and matches the source's condition that all three theories agree when "events correlate with the agent's action iff they are caused by the agent's action," except for the FDT node itself.

A second open problem is **counterpossible reasoning**. If a certain function outputs $\pi$ on input $x$, it does so of logical necessity; the antecedent "the function outputs $\pi'$ instead" is counter-to-logic. Pearl's $\mathrm{do}$ operator sidesteps full-blown counterpossible semantics — we simply sever incoming arrows and propagate — but this works only *given* $G$. The source notes that some functional decision theorists hope for a logical conditioning operator that would make an evidential formulation possible; none yet exists. I endorse the source's pragmatic stance: the difficulty is technical rather than philosophical, humans reason about logical uncertainty constantly, and the agent needs only local questions answered ("how would *this* predictor's prediction change if my policy were $\pi'$?"), not a general theory of impossible worlds.

A third unresolved choice, which footnote 16 does not address, is the **specification of $\Pi$**. The argmax in (1) ranges over candidate policies, and in realistic problems $\Pi$ is astronomically large and must be represented implicitly (e.g., as outputs of bounded computations). There is also a self-reference worry, parallel to the action-level case: $\Pi^*(P,G)$ appears inside the model $P$ it is defined over. The source resolves this at the action level via Kleene's second recursion theorem ("quining"); the same technique applies here, since a policy is just a computable function and a program can contain an accurate representation of itself. I flag, though, that for *uncomputable* optimal policies or infinite observation sets, existence of a maximizer in (1) is not guaranteed — a genuine gap the source does not discuss. For the finite, explicit cases treated here, no difficulty arises.

## 6. Dominance, regret, and fairness

Every method of constructing hypotheticals generates its own dominance relation, and dominance therefore cannot arbitrate *between* theories. What does arbitrate is utility achieved. Against the standard objection that Newcomb's problem "rewards irrationality," the source replies that the predictor "punishes two-boxers," not rational agents per se — dilemmas that reward or punish agents *for their decision procedure* are unfair, but dilemmas that respond to *predicted actions* are fair. The authors conjecture that P-FDT-style FDT matches or beats every rival on all fair problems (where beliefs are accurate and outcomes depend only on behavior in the dilemma at hand), while admitting they lack a formal fairness criterion; footnote 15 of the source notes real obstacles to constructing one.

On regret: the CDT agent holding an empty box B in transparent Newcomb says, "I could have taken both boxes." The P-FDT agent says: had my policy been the two-boxing one, the box would not have been full. Regret is measured by re-intervening on the policy — and that hypothetical is *worse*. There is no decision the agent will subsequently regret, because the hypothetical in which she acted differently is also a hypothetical in which her observations differed.

## 7. A recipe for applying P-FDT

For a reader facing an unfamiliar dilemma, I suggest the following procedure (distilled from the source, with the policy-level generalization):

1. **Model.** Write down a prior $P$ over the environment, *including* variables for any process that predicts, simulates, or mirrors your reasoning, and your beliefs about your own observations.
2. **Graph.** Draw $G$: place a single node $\Pi^*$ representing your decision procedure's policy output; draw arrows from it to (i) your action on each observation history, (ii) every predictor's/twin's/future-self's corresponding behavior, and everything downstream of those. Draw no arrow from $\Pi^*$ to lesion-like common causes or mere coincidences.
3. **Enumerate policies.** List the salient candidate policies $\pi \in \Pi$ (typically few: *pay/refuse conditional on observation*, *one-box/two-box*, *cooperate/defect*).
4. **Intervene and score.** For each $\pi$, compute $\mathbb{E}[V \mid \mathrm{do}(\Pi^* = \pi)]$: propagate the change through $G$, allowing your observations to shift as consequences of the intervention, and average over remaining uncertainty.
5. **Execute.** Adopt the maximizing policy; when you receive an observation $x$, perform $\pi^*(x)$ without further re-deliberation, unless you now believe $G$ or $P$ was materially wrong (in which case you are facing, in effect, a new problem).

## 8. Conclusion

P-FDT is a single rule: *choose, by intervention on the logical variable representing your decision procedure's output, the policy from observation histories to actions that yields the best hypothetical world — then apply your observations to it.* It preserves CDT's discipline of breaking mere correlations (so it smokes in the smoking lesion problem and refuses blackmailers), restores EDT's sensitivity to being predicted (so it one-boxes, cooperates with twins, and pays the hitchhiker), and adds a third discipline that neither classical theory supplies: choosing once, at the level of the whole input–output mapping, so that an agent coordinates with her future selves, her twins, and her predictors in one unified move. The theory rests on two unfinished foundations — the deduction of subjunctive-dependence structure from evidence, and a workable treatment of counterpossible conditionals — and the restriction of the policy set $\Pi$ raises existence and tractability questions of its own. But the payoff is substantial: a decision procedure that is reflectively stable, assigns non-negative value to information, needs no precommitment machinery, and, so far as fair dilemmas can show, gets rich.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060 (2017). All quoted phrases are from this source; footnote 16 and its surrounding discussion of policy-level intervention are the primary basis for the formulation of P-FDT developed above.