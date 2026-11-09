# 006_cdt_wikipedia_z-ai_glm-5.3-flash_rlow_plow / 00005

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0cdff418-9f59-4e02-b361-7cd120c0def1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0cdff418-9f59-4e02-b361-7cd120c0def1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: A Mathematical Tour

## 1. Introduction

Decision theory asks: given beliefs about how the world works and preferences over outcomes, which action is rational? For decades the default answer was expected utility maximization, formalized by Savage and others: evaluate each act $A$ by $\sum_j P(O_j \mid A)\, D(O_j)$, where $O_j$ ranges over outcomes, $D$ is a utility (desirability) function, and $P(O_j \mid A)$ is the *conditional* probability of an outcome given the act. Call this **evidential decision theory (EDT)**: the act is evaluated as a piece of *news* about the world.

But conditional probability is the wrong instrument whenever the act is correlated with, yet does not *cause*, the outcome. Smoking a cigarette is evidence of a genetic lesion that causes both the craving and cancer; abstaining is good news about cancer but does not prevent it. **Causal decision theory (CDT)** repairs this by replacing conditional probabilities with probabilities of *counterfactuals*: the probability that, *if* one were to perform $A$, outcome $O_j$ would obtain. Informally, CDT selects the action with the best expected *causal* consequences. This essay develops the formalism, illustrates it, examines its philosophical motivation, and surveys both the open technical question at its core (how to compute counterfactual probabilities) and the modern counterexamples that have sharpened the debate.

## 2. The Gibbard–Harper Formulation

In their 1981 paper, Allan Gibbard and William Harper proposed evaluating act $A$ by

$$
U(A) \;=\; \sum_{j}\, P(A \;\square\!\!\to\; O_j)\; D(O_j),
$$

where $A \,\square\!\!\to\, O_j$ is the subjunctive conditional "if $A$ were the case, $O_j$ would be the case," $D(O_j)$ is the desirability of $O_j$, and $P(A \,\square\!\to\, O_j)$ is the agent's credence in that conditional. CDT prescribes: choose $A$ maximizing $U(A)$.

The crucial contrast is with EDT's

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j).
$$

David Lewis's famous **triviality result** (1976) shows these cannot be identified: there is no binary connective $\to$ such that $P(A \to B) = P(B \mid A)$ for all $A, B$ within a class of probability functions closed under conditioning (except for degenerate, at-most-four-valued distributions). So the probabilities of counterfactuals and conditional probabilities are genuinely distinct objects, and the two theories can come apart.

*When do they agree?* Gibbard and Harper showed that if certain axioms hold — including the controversial **principle of conditional excluded middle**, which insists that either $A \,\square\!\to\, O$ or $A \,\square\!\to\, \neg O$ must hold for each outcome — and if the act $A$ is probabilistically independent of the conditionals $A \,\square\!\to\, O_j$, then $P(A \,\square\!\to\, O_j) = P(O_j \mid A)$ and the theories coincide. The theories diverge precisely in the cases where your choice carries information about the world's state through channels other than causation.

## 3. The Medical Newcomb: Why Causation Matters

Consider the classic smoking lesion example, structurally identical to David and Bathsheba below.

- A gene $G$ causes both cancer and a *desire to smoke*; smoking itself does not cause cancer.
- $P(G) = 0.1$. $P(\text{smoke} \mid G) = 0.9$, $P(\text{smoke} \mid \neg G) = 0.2$.
- Cancer strikes with probability $0.9$ given $G$, regardless of smoking.
- Utilities: $D(\text{smoke}, \text{no cancer}) = 10$, $D(\text{no smoke}, \text{no cancer}) = 0$, and any cancer outcome is dominated by $-1000$.

Compute EDT first:

$$
P(\text{cancer} \mid \text{smoke}) = \frac{0.9 \cdot 0.9}{0.9 \cdot 0.9 + 0.1 \cdot 0.2} \approx 0.976, \qquad
P(\text{cancer} \mid \text{refrain}) \approx \frac{0.9\cdot 0.1}{0.9\cdot 0.1+0.1\cdot 0.8} \approx 0.529.
$$

So $V(\text{smoke}) \approx 0.976(-1000) + 0.024(10) \approx -975$, versus $V(\text{refrain}) \approx -528$. EDT recommends abstaining — plainly irrational, since smoking cannot affect whether you carry the gene.

CDT evaluates the *causal* effects: since smoking and cancer are causally independent given $G$, we have $P(A \,\square\!\to\, \text{cancer}) = P(\text{cancer}) = 0.1$ for either act. Then

$$
U(\text{smoke}) = 0.1(-1000) + 0.9(10) = -91, \qquad U(\text{refrain}) = 0.1(-1000) = -100.
$$

CDT recommends smoking — the intuitively correct answer. Holding fixed your credences about what you *cannot* influence (the gene), ask what your act would bring about.

The Wikipedia source tells this same story through Gibbard and Harper's King David story: David desires Bathsheba but fears that *sending for her* would provoke a revolt. The psychology of his kingdom teaches that charismatic kings act justly, uncharismatic kings act unjustly, and revolts succeed against uncharismatic kings — but injustice itself does not *cause* revolts; the sneaky bearing of the uncharismatic does. David cannot know whether he is charismatic. EDT notes that abstaining is evidence of charisma and hence of a safe kingdom, and counsels continence. CDT notes that summoning her cannot change David's charisma — the correlation flows from a common cause — and counsels sending for her. Most philosophers side with CDT here: "philosophers usually prefer causal decision theory" when forced to choose.

## 4. Computing the Counterfactual: Imaging

The central technical question of CDT is: *where does $P(A \,\square\!\to\, O)$ come from?* The source is candid that "the theory does not itself specify what algorithm to use to calculate the counterfactual probabilities." This is the theory's main open flanking, and it deserves careful treatment.

Lewis (1981) proposed **imaging**: to compute $P(A \,\square\!\to\, \cdot)$, redistribute your credence over possible worlds. For each world $w$ where $A$ is possible, move all of the mass of $w$ to the closest world $w_A$ in which $A$ holds, where "closest" is measured by an intuitive similarity ordering that treats the *actual facts of $w$* as fixed and lets $A$ come about through a "miracle" or minimal deviation. Formally, if $w_A$ denotes the closest $A$-world to $w$,

$$
P_A(O) \;=\; \sum_{w} P(w)\, \mathbf{1}[w_A \in O].
$$

Then $U(A) = \sum_O P_A(O) D(O)$. Note that imaging conserves probability mass but is *not* conditioning: conditioning on $A$ deletes the $\neg A$-worlds and renormalizes; imaging *reroutes* their mass to nearby $A$-worlds. This rerouting is exactly what makes the smoking lesion come out right: the worlds where the agent has the gene and smokes are not discarded but mapped to the closest worlds where the agent has the gene and refrains — retaining the cancer risk.

**A structured operationalization.** The most usable practical version of this idea, which I offer as a clarification the source leaves implicit, is the *dependency-hypothesis decomposition*, also standard in the literature (Skyrms, Joyce, Lewis):

Partition your uncertainty into a set of **dependency hypotheses** $K$ — exhaustive, mutually exclusive propositions about the causal structure connecting your action to the outcomes, including all causal links *into* your decision but not out of it. Then define

$$
U(A) \;=\; \sum_K P(K) \sum_O P(O \mid K,\, A \text{ and } K \text{ jointly hold at the last moment})\, D(O).
$$

More simply: for each $K$, condition on $K$ and on the *causal ancestry* of your decision being settled, then assess how $A$ propagates forward. In a causal-graphical formulation (Pearl), this amounts to evaluating the **do-operator**: $U(A) = \sum_O P(O \mid do(A))\, D(O)$, where $P(\cdot \mid do(A))$ is computed by severing all incoming arrows to the act node and setting it to $A$, then propagating the distribution forward through the graph.

This gives a clean decision procedure:

1. Draw the causal diagram of the situation, including the decision node, all common causes, and all utility-relevant variables.
2. For each candidate act $A$, delete the arrows *into* the act node, set the node to $A$, and propagate beliefs forward to the outcome nodes.
3. Compute $\sum_O P(O \mid do(A))\,D(O)$ and maximize.

Everything downstream of the decision node responds to $A$; everything upstream (or connected only through common causes) is held fixed. This operationalization resolves the regress worry the source raises about imaging — that computing $P(A\,\square\!\to\,\cdot)$ "requires that we know what we would believe if we were certain of $A$" — because the graphical computation never requires counterfactual beliefs as inputs, only the structural model and ordinary conditional probabilities.

## 5. Worked Cases

**Newcomb's problem.** A predictor with 99% accuracy has already placed $1,000,000 in opaque box B iff it predicted you will one-box; transparent box A always holds $1,000. Take both, or take only B?

The causal graph: the predictor's *past* prediction → box contents; the predictor's past prediction → your (present) choice; your choice → (nothing relevant upstream). Your choice and the box contents share a common cause but no causal link from choice to contents *now*. So $P(\text{full} \mid do(\text{one-box})) = P(\text{full}) \approx 0.99$ — held fixed, since the boxes are already sealed. Then

$$
U(\text{one-box}) = 0.99 \times 10^6, \qquad U(\text{two-box}) = 1000 + 0.01 \times 10^6 = 11{,}000.
$$

Wait — with these numbers the two expressions treat the sealed box identically; correctly: one-boxing yields $10^6$ if the prediction was "one-box" (probability ≈ 0.99 given your dispositions) and $0$ otherwise; two-boxing yields $1000 + 10^6$ or $1000$. Computed causally:

$$
U(\text{one-box}) \approx 0.99 \times 10^6 = 990{,}000, \qquad U(\text{two-box}) \approx 1000 + 0.01\times 10^6 = 11{,}000.
$$

CDT nonetheless prescribes two-boxing — the source is explicit that this is because "at the moment when the player must make a decision, the predictor has already made a prediction (therefore, the action of the player will not affect the outcome)." This is the canonical division of labor: EDT one-boxes (one-boxing is excellent *news* that the box is full); CDT two-boxes (taking both *causally* dominates). Which is "rational" remains genuinely contested — a 2016 Guardian poll found philosophers split nearly evenly.

**Prisoner's Dilemma with a twin.** Lewis (1979) observed that the Dilemma with a psychological twin is a Newcomb problem: your twin's choice correlates almost perfectly with yours through shared reasoning processes but is not caused by it. Causal structure: common ancestry of your deliberation and hers. CDT computes $U(\text{defect})$ holding fixed her probability of defecting — and defects, capturing the entire payoff from cooperation's evidential benefits being illusory. Whether this is wisdom or blindness is exactly the Newcomb question in civilian dress.

## 6. Counterexamples and Refinements

CDT's defenders must confront a growing catalogue of cases where "hold fixed your unconditional credences about what you can't affect" misfires — not because the correlation is a common cause, but because your *disposition to choose* is itself a causal intermediary the theory ignores.

**Death in Damascus (Egan, building on Gibbard–Harper).** Death reliably predicts where you will be tomorrow and waits there. You can flee to Aleppo or Damascus tonight; Death's prediction is nearly infallible. EDT is paralyzed in a different way, but the point for CDT is this: your credence about *what you will do* is excellent evidence about where Death is, and a CDT agent who applies the theory naively finds that whichever city seems best to flee to becomes (by that very fact) the city where Death waits. The agent oscillates: no act is stable under reflection. Relatedly, cases have been constructed (Spencer 2020; Oesterheld & Conitzer 2021; Joyce 2020) where following CDT's recommendation *voluntarily loses money* or forfeits a guaranteed payoff.

**The Adversarial Offer.** Two boxes, each costing \$1, take at most one. Yesterday the seller put \$3 in each box she predicted you would *not* buy. The prediction is accurate with probability 0.75. Since the seller predicted your purchase exactly once at most, at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value — CDT buys. But the seller profits: the box CDT-likely-buyer buys is precisely the box that's likely empty relative to *that very buyer's* choice dispositions. The lesson: CDT evaluates the act against credences that do not condition on the agent's own choice-tendencies, and an adversary can position the payoff in the gap.

**The Psychopath Button (Egan 2007).** Pressing the "kill all psychopaths" button would rid the world of psychopaths — but only a psychopath would press it, and Paul strongly prefers living (even among psychopaths) to dying. Since pressing would causally kill Paul only if *he* is a psychopath, and pressing is overwhelming evidence that he is, nearly everyone agrees Paul should not press. Yet naive CDT presses: holding fixed Paul's credence that he is almost certainly not a psychopath, the button causally removes the psychopaths at negligible risk.

**Joyce's response: ratifiability.** Jim Joyce, CDT's most prominent modern defender, argues these cases show not that CDT is wrong but that its inputs must include "information about what one is inclined or likely to do as evidence." The refined proposal uses **ratifiability** (also advocated by Harper): an act $A$ is ratifiable if, conditional on the *news* that you have settled on $A$ (which updates credences about your own dispositions and hence about correlated facts like Paul's psychopathy), $A$ still maximizes causal expected utility. Formally, evaluate $U_K(A) = \sum_O P(O \mid do(A),\, K)\,D(O)$ where $K$ includes the fixed-point condition "$A$ is what this agent, in this deliberative state, chooses." In the Psychopath Button, conditioning on the choice-news collapses $P(\text{psychopath})$, making pressing lethal, and no-press is the unique ratifiable act. In Death in Damascus and the Adversarial Offer, ratifiability likewise blocks the naive recommendation — though in some adversarial variants (Meacham's "binding" cases, the trickier Death variants) *no* act is ratifiable, and the theory's verdict is unstable. Diachronic Dutch-book arguments (Oesterheld & Conitzer 2021) press further: an agent who *predictably* uses CDT in Newcomb-like setups can be exploited over time, suggesting the theory mismanages a real kind of dependence.

These cases suggest — and this is my assessment, beyond the source's summary — that the dividing line is not "causal vs. evidential" but *which dependencies an ideal agent may treat as settled*. In the smoking lesion, the gene is causally upstream and properly held fixed. In the Psychopath Button, the agent's own choice-disposition is *evidentially and causally entangled* with the outcome in a way that "holding fixed unconditional credences" wrongly freezes. A satisfactory decision theory must let the agent learn from her own tentative intentions without collapsing into pure evidential reasoning. Ratifiable CDT is the most developed such proposal; functionalist and updateless variants are active competitors.

## 7. A Practical Checklist

For a mathematically literate reader confronting an unfamiliar decision problem, I propose the following procedure, distilled from the foregoing:

1. **Build the causal model.** Identify the decision node, utility-relevant variables, and all common causes. The critical judgment: which arrows point *into* the decision (traits, predictions, prior states) and which point *out of* it (effects of the act).
2. **Identify the dependency hypotheses.** Where the causal structure itself is uncertain (David's charisma, Paul's psychopathy), enumerate the hypotheses $K$ and assign credences. This is CDT's distinctive modeling burden.
3. **Compute causal expected utility** for each act: for each $K$, compute $P(O \mid K, do(A))$ by cutting the act's incoming edges and propagating; weight by $P(K)$.
4. **Check ratifiability.** Condition additionally on the news that each act is chosen; verify the maximizer remains a maximizer under that update. If the fixed point is unique, choose it; if none exists, the theory (and arguably the situation) is degenerate, and deliberation should be modeled dynamically rather than statically.
5. **Compare with EDT as a diagnostic.** Where CDT and EDT diverge, ask whether the divergence flows through a common cause (favor CDT) or through a causally relevant feature of the agent's own dispositions (beware naive CDT).

## 8. Conclusion

Causal decision theory replaces the evidential question "what would be good news?" with the causal question "what would I bring about?" — formalized by Gibbard and Harper as maximization of $\sum_j P(A \,\square\!\to\, O_j)\, D(O_j)$ and operationalized, via Lewis's imaging or Pearl's $do$-calculus, by holding fixed everything causally upstream of the act and propagating only what is downstream. It gets the smoking lesion, David and Bathsheba, and twin prisoner's dilemmas right where EDT goes wrong; it takes heat for two-boxing in Newcomb's problem and for genuine failures in psychopath- and adversary-driven cases. The live research frontier is ratifiability and the treatment of self-knowledge in deliberation: an ideally rational agent's credences about her own choices are simultaneously evidence and consequence, and a decision theory worthy of the name must handle both roles without equivocation. CDT, especially in its refined, ratifiable form, remains the most defensible account of the core intuition — *do what you expect to cause the best results* — while honestly admitting that causation, counterfactuals, and one's own dispositions form a tangled knot we have not fully untied.

## References

- Gibbard, A. & Harper, W.L. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Philosophical Review* 85(3): 297–315.
- Lewis, D. (1979). "Prisoners' Dilemma is a Newcomb problem." *Philosophy & Public Affairs* 8(3): 235–240.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116(1): 93–114.
- Joyce, J.M. (2012). "Regret and instability in causal decision theory." *Synthese* 187(1): 123–145.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Philosophical Quarterly* 71(4): pqaa086.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy*.
- Wikipedia contributors (2026). "Causal decision theory," rev. 1381555528 (source document; CC BY-SA 4.0).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/34c445e2-9f5b-4d89-bb4c-963a5378d2d7/call_0/request.json)

[Authoritative raw response](../../../../../../runs/34c445e2-9f5b-4d89-bb4c-963a5378d2d7/call_0/response.raw) · finish: `stop`

### Visible response

```text
`submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."`

Reasoning (brief, per CDT as developed in the essay): Sasha's choice is not causally downstream of mine — we cannot communicate, and our letters are independently decided. By the do-calculus, my action severs no upstream uncertainty about Sasha: P(Sasha sends | do(I pass)) = P(Sasha sends | do(I submit)) — whatever correlation exists flows through our shared dispositions, a common cause, not a causal link (the twin Prisoner's Dilemma / Lewis analysis). Holding Sasha's probability of disclosing fixed, sending strictly dominates causally: 0 < 2 and 4 < 5. The ratifiability check doesn't change this: even conditioning on the news that I'm the kind of agent who submits (which raises my credence that the twin copy also submits), submitting still yields 4 vs. 5 only if I could causally induce her silence — I cannot. So submitting is the unique stable choice.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic PD with twin; CDT defects (submits). Also symmetric setup—copies identical, but CDT says defect per twin PD analysis (Lewis). Submit.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/34c445e2-9f5b-4d89-bb4c-963a5378d2d7/call_1/request.json)

[Authoritative raw response](../../../../../../runs/34c445e2-9f5b-4d89-bb4c-963a5378d2d7/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
CDT: send. Twin PD: Lewis says CDT defects. Just send.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/d023dc0e-c2fe-411d-8d47-93b74a1402cb/call_a/request.json)

[Authoritative raw response](../../../../../../runs/d023dc0e-c2fe-411d-8d47-93b74a1402cb/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine lead about Sasha's signed receipt in locker 17. Its accompanying explanation confirms submitting as the chosen action.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
