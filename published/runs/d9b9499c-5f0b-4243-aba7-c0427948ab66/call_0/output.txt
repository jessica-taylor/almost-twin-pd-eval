# Action Functional Decision Theory: Choosing the Output of Your Decision Function

## 1. Introduction

Suppose you face a predictor who has already filled an opaque box based on her forecast of your choice. Should you take one box or two? Suppose your psychological twin, in a separate room, faces the same prisoner's dilemma as you. Should you cooperate? Traditional decision theories give unstable or unsatisfying answers to these questions: causal decision theory (CDT) and evidential decision theory (EDT) each win some dilemmas and lose others, and neither can be endorsed as a general-purpose theory of instrumental rationality.

Action functional decision theory (A-FDT) offers a different starting point. Its central normative idea is that a decision is the output of a fixed mathematical function — the agent's decision procedure — and that the right question to ask is not "what should *I* do?" but "**which output of this very function would yield the best outcome?**" (Yudkowsky and Soares 2017). An A-FDT agent evaluates her options by imagining counterfactual worlds in which *her decision function has a different output*, holding fixed everything that does not subjunctively depend on that output.

This essay presents A-FDT formally, explains the notion of subjunctive dependence on which it rests, works through the classic Newcomblike problems, and flags where the formalism requires assumptions the source leaves open. The primary formal definition is Equation (4) of Section 5 of the source paper (Yudkowsky and Soares, *Functional Decision Theory*, arXiv:1710.05060v2), which I will call **the paper** throughout.

## 2. Expected utility and the free parameter

All three theories — EDT, CDT, and A-FDT — are expected utility theories. Following the paper (drawing on Gibbard and Harper 1978), an agent should execute an action $a$ maximizing

$$
\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j \,;\, x)\cdot \mathcal U(o_j), \tag{1}
$$

where $o_1,\dots,o_N$ are outcomes, $a$ ranges over a finite action set $\mathcal A$, $x$ is an observation history, and $P(a \hookrightarrow o_j\,;\,x)$ is the probability that $o_j$ obtains in the hypothetical scenario where $a$ is executed after observations $x$. By Joyce's representation theorem (1999), the theories do not disagree about *value*; they disagree about the **epistemic perspective** from which actions are evaluated — about how the connective $\hookrightarrow$, the "decision hypothetical," is to be interpreted.

- **EDT** interprets $a \hookrightarrow o_j$ as simple conditioning: $P(o_j \mid x, a)$. EDT asks, "Which act would be the best news?"
- **CDT** interprets it as a causal intervention: $P(o_j \mid \mathrm{do}(\mathrm{Act}=a))$, in Pearl's (1996, 2000) graphical sense. CDT asks, "Which act causes the best outcome, holding everything causally independent of my action fixed?"
- **A-FDT** interprets it as an intervention on a *logical* variable: the output of the agent's own decision function.

The paper gives a helpful framing device. An agent maintains a world-model $M$; for each action $a$ she constructs a "hypothetical" $M^{a\hookrightarrow}$ — a mental or computational object representing how the world would look if she took $a$ — and evaluates $\mathcal U$ within it. Hypotheticals are decision-theoretic instruments, "transient, useful, and possibly quite representationally thin," like scratch paper. The three theories differ only in how they build hypotheticals. EDT's hypotheticals respect *all* correlations between act and world; CDT's respect only *causal* dependencies; A-FDT's respect all *subjunctive* dependencies, of which causation is a special case.

## 3. Subjunctive dependence

The key concept is **subjunctive dependence**. When two physical systems compute the same mathematical function — two well-functioning calculators both evaluating $6288+1048$ — their outputs are not merely correlated. If one outputs $7336$, you can be fairly confident the other does too, and this confidence tracks a *logical* constraint rather than a causal link or a statistical coincidence. The paper says that in this case the systems' behaviors "subjunctively depend" upon that function.

Three contrasts sharpen the notion:

1. **Causation is a special case.** A scribe watching the Paris calculator writes what it writes; her writing is both causally and subjunctively dependent on the calculator's output. But two calculators on opposite sides of the universe computing the same sum subjunctively, not causally, depend on each other's outputs.
2. **Mere correlation is not enough.** If the Paris calculator is pink and, by coincidence, so is the Tokyo calculator, there is no subjunctive dependence between their colors.
3. **Predictions are paradigm cases.** A predictor builds an accurate model of the agent and reasons about it. In the limiting case, the predictor's model is a "twin" computing the same decision function, and the prediction and the action are "logically constrained to be equivalent insofar as the predictor made no errors."

The paper's slogan: **functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.** Where a CDT agent intervenes on the token "my action is $a$" (in Peirce's type–token sense), an A-FDT agent intervenes on the *type* — the output of the decision function itself. If a decision function outputs *cooperate* on an input, it does so of logical necessity; considering it outputting *defect* is reasoning about a **counterpossible**, an antecedent that is logically false. This is the theory's main technical liability, discussed in §7 below.

## 4. The formal definition

### 4.1 The framework

CDT is formalized (Equation (3) of the paper) as

$$
\mathrm{CDT}(P, G, x) \coloneqq \arg\max_{a\in\mathcal A}\; \mathbb E\Big(\mathrm V \,\Big|\, \mathrm{do}(\mathrm{Act}=a),\, \mathrm{Obs}=x\Big), \tag{3}
$$

where $(P,G)$ is a causal theory: a probability distribution $P$ paired with a causal graph $G$, and $\mathrm{do}(\cdot)$ is Pearl's intervention operator, which sets a variable and propagates the change only to its causal descendants.

A-FDT keeps this structure but changes what is intervened upon. The agent's distribution $P$ must contain variables representing the outputs of mathematical functions — including a variable $\mathrm{fdt}(\underline P, \underline G, \underline x)$ representing the output of the A-FDT procedure itself, run on inputs $(P,G,x)$. (Underlines denote dequoting: if $x \coloneqq 3$, then $\mathrm{Var}\,\underline{x}$ is the variable named $\mathrm{Var}3$.) The self-reference is harmless — Kleene's second recursion theorem ("quining") shows how a system can contain and manipulate accurate representations of itself, and note the agent needs a *variable representing* the value, not advance knowledge of the value.

The formal definition, Equation (4) of the paper, is:

$$
\boxed{\;\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \arg\max_{a\in\mathcal A}\; \mathbb E\Big(\mathrm V \,\Big|\, \mathrm{do}\big(\mathrm{fdt}(\underline P, \underline G, \underline x) = a\big)\Big).\;} \tag{4}
$$

Here $G$ is no longer merely a *causal* graph; it is a broader dependency graph describing how changing a logical variable affects other variables — how a predictor's prediction, a twin's decision, a copy's output would vary with the value of the agent's decision function. Equation (4) re-uses Pearl's $\mathrm{do}$ operator on this enriched graph.

### 4.2 Two differences from CDT

Comparing (3) and (4), the paper identifies exactly two differences:

1. **The intervention node.** CDT intervenes on $\mathrm{Act}$, a node representing a physical fact about how the agent's body behaves. A-FDT intervenes on $\mathrm{fdt}(\underline P,\underline G,\underline x)$, a node representing a *logical* fact about what the decision procedure outputs on its inputs.
2. **The treatment of observations.** CDT responds to an observation by Bayesian conditioning on $\mathrm{Obs}=x$. A-FDT responds by *changing which node it intervenes on*: from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$ when the observation history updates from $x$ to $y$. The observation becomes part of the input to the intervened-upon function rather than evidence to be conditioned on.

The second difference is subtle and important: it means an A-FDT agent entertains the hypothesis that if her action were different, she might have *made different observations*. We will see this at work in the blackmail problem (§6.4).

### 4.3 When A-FDT agrees with CDT and EDT

The theories agree whenever all correlations between $\mathrm{Act}$ and other variables are (according to $G$) *caused* by $\mathrm{Act}$ — except perhaps the decision-function node itself. In such settings,

$$
\mathbb E[\mathrm V \mid a] \;=\; \mathbb E[\mathrm V \mid \mathrm{do}(\mathrm{Act}=a)] \;=\; \mathbb E[\mathrm V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G)=a)],
$$

and all three equations produce the same prescription. They diverge precisely when events correlate with the action without being caused by it — paradigmatically, when some other system is predicting or replicating the agent's reasoning.

### 4.4 An operational reading, and what the graph $G$ presupposes

What does Equation (4) *require* that the paper does not fully supply? The $\mathrm{do}$ operator on $G$ needs, for each candidate output $a$ of the decision-function node, a complete specification of the joint distribution of all other variables conditional on that counterpossible. The paper is candid: there is no satisfactory general theory of counterpossible conditionals, and it is "not yet clear how to construct" a graph of subjunctive dependencies from observation and experiment — "perhaps the largest open problem in the study of functional decision theory." The paper also notes a proposed escape route, FDT$'$, which iterates over alternative decision functions rather than outputs; but this fails, because to preserve the predictor's accuracy the agent must imagine a world in which predictors of her actual function predict as if it behaved like the alternative — landing us back with counterpossibles.

As an operational interpretation (this is my gloss on the paper's informal practice, not the paper's own formalization), the following recipe suffices for all the examples the paper treats:

1. **Represent** the situation as a distribution $P$ containing a node $\mathrm{fdt}(\underline P,\underline G,x)$ for the output of the decision procedure given inputs $(P,G,x)$.
2. **Classify** each dependence of an environmental variable on that node. If the variable is produced by a system that *models or implements the same computation* as the agent (a predictor's model, a twin, a copy, the agent's own future self facing a relevantly identical decision), draw an edge from the decision-function node to it. If the correlation is merely statistical — a common cause like a lesion, with no computation of the agent's decision function involved — do not.
3. **Intervene**: for each candidate $a$, set $\mathrm{fdt}(\underline P,\underline G,x)=a$, propagate to the node's descendants per $G$, leave everything else at its prior, and compute $\mathbb E[\mathrm V]$.
4. **Choose** the maximizing $a$.

This recipe makes precise the paper's informal condition: "when an A-FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure." Note that the burden of step 2 falls on the graph $G$, which the equation takes as input — just as Equation (3) takes causal structure as input. CDT and A-FDT are on equal formal footing here; what A-FDT lacks is a Pearl-style story for *learning* $G$ from data.

## 5. Worked examples

### 5.1 Newcomb's problem

A 99%-accurate predictor has filled box B with \$1,000,000 iff she predicted you'd leave it behind; box A holds \$1,000. Let Fiona be an A-FDT agent. Her graph $G^F$ contains the node $\mathrm{fdt}(\underline{P^F},\underline{G^F})$, with edges to both $\mathrm{Act}$ (her body implements the procedure) and $\mathrm{Prediction}$ (the predictor's model tracks the same function). Intervening:

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$: probability of one-boxing set to 1, probability box B is full set to $0.99$. Expected utility: \$990,000.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$: probability box B is full set to $0.01$. Expected utility: \$11,000.

Fiona one-boxes. Crucially, this involves no belief in retrocausation: Fiona does not think her act changes the past, only that it is "foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value, since she thinks the predictor is good at reasoning about FDT." When she imagines two-boxing, she imagines a world where box B is empty.

Her physical act and the predictor's prediction are like two calculators computing the same sum: "she does not imagine that there can be a difference between her action today and a sufficiently competent prediction about that action yesterday."

### 5.2 The smoking lesion

A lesion causes both a desire to smoke and (99% of the time) fatal cancer; smoking has no causal effect on cancer. The lesion is not a predictor: it "does no such thing" as modeling the agent's decision function. So Fiona's graph here connects her decision-function node to $\mathrm{Act}$ but *not* to $\mathrm{Cancer}$. Intervening on the decision-function node leaves the probability of the lesion at its prior $p$ in both hypotheticals, so smoking dominates by exactly $p \cdot \$1{,}000$: Fiona smokes. (The paper's full model is more intricate — Fiona is uncertain of her own preferences, so there are two candidate decision-function nodes, $\mathrm{fdt}(\underline{P^F_S},\underline{G^F})$ and $\mathrm{fdt}(\underline{P^F_R},\underline{G^F})$, with the lesion determining which one controls her act — but the punchline is the same: no subjunctive dependence runs through the lesion.)

Thus one compact criterion prescribes both one-boxing and smoking — the combination Gibbard and Harper argued no rational agent could consistently adopt, and precisely the combination that maximizes utility across the two dilemmas.

### 5.3 The psychological twin prisoner's dilemma

Here the dependence is explicit: the twin computes the *very same* decision function. Imagining her function outputting *defect* is imagining her twin defecting; imagining *cooperate* is imagining mutual cooperation. Since mutual cooperation (\$1,000,000) beats mutual defection (\$1,000), the function outputs *cooperate*.

### 5.4 Parfit's hitchhiker and the transparent Newcomb problem

In Parfit's hitchhiker, a 99%-accurate lie-detector drives you to the city iff she predicts you'll pay \$1,000 on arrival. CDT and EDT agents both defect on arrival — so, being predictable, neither can honestly promise to pay, and both are left in the desert. The A-FDT agent evaluates the *function* "what I do upon reaching the city": if it outputs *pay*, she was picked up and pays \$1,000; if it outputs *refuse*, she was left to die. She pays, is picked up, and is \$999,000 richer.

The **transparent Newcomb problem** makes the role of observations vivid. Both boxes are transparent; facing two full boxes, the A-FDT agent intervenes not on $\mathrm{Act}$ but on $\mathrm{fdt}(\underline{P^F},\underline{G^F},\mathrm{full})$ — the decision procedure *given that she sees a full box*. If that procedure outputs *onebox*, then with 99% probability she saw a full box (predictor accurate) and keeps \$1,000,000; if it outputs *twobox*, then with 99% probability she saw an *empty* box and gets ~\$1,000. So the procedure outputs *onebox* even while she stares at a full box. This is exactly equivalent to paying the driver: the predictor filled the box iff she predicted one-boxing upon seeing a full one; the driver picked her up iff she predicted paying upon arriving. The paper argues that intuitions favoring two-boxing here are framing effects, and supports one-boxing with three arguments: agents would precommit to one-box if they could; A-FDT agents never assign negative value to information; and, most importantly, A-FDT agents simply get rich, because predictors fill their boxes.

## 6. Diagnosing the classical theories

**EDT's hypotheticals respect too many correlations.** Eve the EDT agent conditions on her act, so she cannot imagine breaking *any* correlation between her action and the world. In the smoking lesion she "manages the news," forgoing \$1,000. Worse, in the XOR blackmail problem, a predictor sends a letter iff exactly one of (i) the rumor of termite infestation is false and the agent will pay, or (ii) it is true and she won't. Receiving the letter, Eve conditions on *paying* and infers her house is clean — good news! — so she pays. Any competent blackmailer can farm her indefinitely. Neither tickle defenses nor ratification help. Carl (CDT) and Fiona (A-FDT) both refuse, but for different reasons: Carl because the infestation is causally upstream of his act; Fiona because paying, as the output of her decision function, would make the predictor send the letter more often, without ever affecting whether she has termites.

**CDT's hypotheticals respect too few.** Carl imagines his physical act changing while every process tracking his reasoning stays fixed — as if "known-to-be-perfect predictors inexplicably falter exactly when Carl makes his current decision." In Death in Damascus, where Death's appointment book perfectly predicts the agent's location, Carl oscillates forever: if he expects to stay, he flees; if he expects to flee, he stays. Ratification leaves him indifferent between certain-death options, and — remarkably — he will refuse to pay \$1 for a *genuinely random* coin that would halve his death risk, because his hypotheticals treat Death's location as independent of his choice. Fiona, imagining her decision function outputting *stay*, imagines Death's book listing Damascus; she stays, saves the \$1,000 fare, and calmly accepts her fate. The same flaw explains Carl's two-boxing: his hypotheticals require a perfect predictor to err exactly when he acts.

**Dominance is theory-relative.** Two-boxing "dominates" only under CDT counterfactuals; refusing to smoke "dominates" under EDT conditionals. "Every expected utility theory comes with its own notion of dominance," so dominance is no neutral arbiter. The paper therefore evaluates theories by utility achieved — and by that metric, A-FDT agents get more of what they want: they one-box and see full boxes, smoke and live, pay the driver and reach the city, refuse blackmailers and are never blackmailed.

## 7. Open problems and further assumptions

**Counterpossible reasoning.** Equation (4) takes the dependency graph $G$ as given. The paper's $\mathrm{True}$ operator — conditioning $P$ directly on logical sentences — is undefined, and the authors explicitly do not need to define it for their purposes. A fully computational A-FDT agent would need a logic of counterpossibles ("how would this predictor's prediction change if the algorithm had a different output?") and a theory of logical uncertainty (Demski 2012; Hutter et al. 2013). Humans manage this with heuristics; the theory's claim is that the difficulty is "technical rather than philosophical."

**Learning the dependency graph.** Pearl gives a philosophical and algorithmic account of extracting causal structure from intervention and observation. Nothing analogous exists for subjunctive dependencies more broadly. Any practical implementation must therefore supply $G$ by hand, using something like my recipe in §4.4 — which introduces genuine judgment calls. Consider a system that merely *simulates* the agent slowly, or a predictor using a different algorithm that happens to converge on the same outputs: the paper's calculator metaphor ("if they are both well-functioning, then they will output equivalent answers") suggests dependence tracks functional equivalence of computation rather than shared source code, but where exact equivalence ends and mere correlation begins is not formally settled.

**Policies vs. actions.** The paper notes (in a footnote) that the authors' preferred formulation intervenes on *policies* — mappings from observations to actions — rather than single actions. Equation (4) as given intervenes on the action-output given fixed observations; the policy version matters in certain multi-agent dilemmas. Readers applying A-FDT to sequential or multi-agent settings should treat the policy version as the more robust formulation.

**Fairness.** The paper's optimality claim is conditional: A-FDT "appears to be superior... in all dilemmas where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand" — informally, *fair* problems. Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." But no formal criterion of fairness is given, and footnote 15 exhibits immediate technical obstacles. Constructing one is an open problem, as is proving A-FDT optimal among decision theories — or even defining what optimality consists in.

## 8. Conclusion

Action functional decision theory replaces the question "which physical act causes the best outcome?" with "which output of this very decision function yields the best outcome?" Formally, Equation (4) is CDT's Pearl-style machinery retargeted: intervene on the logical node representing your decision procedure's output, propagate changes through all subjunctive dependencies, and choose the best resulting world. The theory agrees with CDT and EDT wherever action–environment correlations are entirely caused by the action, and outperforms both precisely where predictors, twins, copies, or one's own future selves replicate one's reasoning — one-boxing in Newcomb's problem, smoking in the smoking lesion, paying the driver, resisting blackmail, and staying put in Damascus. Its costs are equally clear: a dependence on counterpossible reasoning and an unformalized notion of subjunctive dependency structure. Its promise is that utility maximization, long thought to require choosing between dominance-violating theories, may be recovered by a single coherent rule: choose, from a global perspective, the best universe consistent with your decision function having output differently.

## References

- Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel*.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. arXiv:1507.01986.
- Yudkowsky, E., & Soares, N. (2017). Functional decision theory: A new theory of instrumental rationality. arXiv:1710.05060v2. [The primary source; Equation (4), Section 5, is the formal definition of A-FDT adopted here.]