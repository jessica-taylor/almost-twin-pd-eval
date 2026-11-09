# A-FDT: Choosing the Output of a Decision Function

## 1. What is being explained

Yudkowsky and Soares's paper "Functional Decision Theory: A New Theory of Instrumental Rationality" calls its theory "FDT". In this essay I call the theory defined by **Equation (4), Section 5** of that paper **A-FDT** (action functional decision theory). The label marks that the formal object is an argmax over *actions*. The paper's footnotes say its authors' "preferred formalization of FDT" iterates over *policies*, meaning maps from observations to actions. They add that "this makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." I treat only the action-level version, and I flag where my own proposals go beyond the paper.

The central idea, in the paper's words, is that "correct decision-making centers on choosing the output of a *fixed mathematical decision function*, rather than centering on choosing a physical act." An agent using A-FDT asks "Which output of this decision procedure causes the best outcome?", where a causal decision theory (CDT) agent asks "Which physical act of mine causes the best outcome?" and an evidential decision theory (EDT) agent asks "Which physical act of mine would be the best news to hear I took?"

## 2. The expected-utility frame

All three theories are expected-utility theories. Equation (1) says to choose $a\in\mathcal A$ maximizing

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $P(a\hookrightarrow o_j;x)$ is the probability that outcome $o_j$ obtains in the hypothetical scenario where $a$ is executed after observations $x$. The paper leans on Joyce's representation theorem: the theories do not disagree about value, only about "the epistemic perspective from which actions are to be evaluated." They differ in how they read the connective $\hookrightarrow$:

- EDT reads it as conditioning: $E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$ (Equation 2).
- CDT reads it as Pearl's intervention on the physical act: $E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$ (Equation 3).
- A-FDT reads it as intervention on a *logical* variable (Equation 4).

The agent holds a world-model $M$. For each action she builds a "hypothetical" $M^{a\hookrightarrow}$, which the paper likens to "notes on scratch paper: transient, useful, and possibly quite representationally thin." She computes a value from each and picks the best. Hypotheticals are instruments built from beliefs, not beliefs themselves.

## 3. Equation (4) read carefully

The paper first writes an ideal but undefined version:

$$\mathrm{FDT}^*(P,x)=\arg\max_a E\big(V\mid \mathtt{true}(\mathrm{fdt}(\underline P,\underline x)=a)\big).$$

It then admits "it's not clear how to define a $\mathtt{true}$ operator" (a conditional on a *false* logical sentence). It sidesteps the problem by requiring the model to come with a dependency graph $G$ and reusing Pearl's $\mathtt{do}$:

$$\textbf{(4)}\qquad \mathrm{A\text{-}FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;E\Big(V\;\Big|\;\mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The components are:

1. **$P$** is a probability distribution over variables, including variables for the values of mathematical functions. A-FDT needs a variable for $6288+1048$, which should put most of its mass on $7336$.
2. **$G$** is a graph saying "how changing a logical variable affects all other variables". This is the key additional input. The paper says it is required "in the same way that the relevant causal structure is given as an input to CDT."
3. **$\mathrm{fdt}(\underline P,\underline G,\underline x)$** is a node representing the output of the A-FDT procedure itself, run on the agent's own model and observations. The underlines denote dequoting. The self-reference is harmless: the agent need not know the *value* of $\mathrm{A\text{-}FDT}(P,G,x)$ to have a variable *representing* it, and Kleene's second recursion theorem ("quining") shows how a data structure can contain an accurate representation of itself.
4. **$\mathtt{do}$** sets that node to $a$, then propagates only to nodes downstream of it in $G$, leaving everything else fixed.

The paper identifies two differences from CDT's Equation (3).

- **Where the intervention happens.** CDT intervenes on $\mathrm{Act}$, a physical fact about her body. A-FDT intervenes on the *type* "what this decision function outputs", where CDT intervenes on the *token* "my action is $a$".
- **How observations are used.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes *which node it intervenes on*, namely $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the observation actually received. Each possible observation has its own node, a different input to the same function.

The second difference has consequences. Because A-FDT evaluates $a$ as "this procedure, on this input, outputs $a$", the hypothetical can include worlds in which the agent saw something *else* (see §5).

The paper summarizes the philosophy as an analogy: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Causal dependence is a special case of subjunctive dependence. Mere statistical correlation is not. Two pink calculators in Paris and Tokyo are correlated in color, but had the Parisian one been green the Tokyo one would still be pink.

## 4. Building $G$: what the paper settles and what it leaves open

The paper is candid that this is the weakest point. Equation (4) "rests on shakier philosophical foundations than (3)." Pearl gave an account of how to infer causal structure from observation and experiment, but "no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence." The paper calls this "perhaps the largest open problem in the study of functional decision theory." It also concedes that A-FDT must evaluate counterpossibles (if the function outputs $a$, it outputs $a$ of logical necessity, so the hypothetical for any other output runs counter to logic). It argues the difficulty is "technical rather than philosophical," pointing to how human mathematicians reason under logical uncertainty.

So the following are **claims of the source**:

- A-FDT is given by Equation (4) with $G$ as an input.
- A-FDT agents preserve "all decision-relevant subjunctive dependencies."
- The needed assumption is that "when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

The source does *not* give an algorithm for producing $G$. Here is a working procedure I propose, consistent with the paper's examples, for a reader who must handle an unfamiliar case. It is an interpretation, not part of the source.

**Step 1: Locate the computations.** List every process in the scenario that *evaluates the agent's decision function* (or something intended to match it): the agent's body, a twin, a predictor's simulation, a blackmailer's model, a coalition-mate's reasoning, her own future self facing a relevantly identical choice.

**Step 2: Draw arrows from the node $\mathrm{fdt}(\cdot,x)$** to the variables that such a process produces. Strength of dependence goes in $P$, as a reliability variable. The paper does this with the Boolean $\mathrm{Accurate}$ node in Newcomb's problem: a good predictor means a high-probability edge, not a certain one. Edges are drawn only where the variable would differ if the *function's output* differed.

**Step 3: Apply the counterfactual test.** For each candidate variable $Z$, ask: "If the algorithm had output something else on this input, with physics and history otherwise as they are, would $Z$ differ because $Z$'s value is computed from that output?" A lesion that causes both smoking-desire and cancer fails the test. A predictor's model of me passes.

**Step 4: Handle observations.** Create one $\mathrm{fdt}$ node per possible observation. Add a selector, a variable in the world that determines which observation, and hence which node, controls $\mathrm{Act}$. The transparent-Newcomb and blackmail graphs in the paper work this way: $\mathrm{Prediction}$ decides whether $\mathrm{fdt}(\ldots,\textit{full})$ or $\mathrm{fdt}(\ldots,\textit{empty})$ controls $\mathrm{Act}$.

**Step 5: Compute.** For each $a$, apply $\mathtt{do}(\mathrm{fdt}(\ldots,x_{\text{actual}})=a)$, propagate downstream, take expectation of $V$, and return the argmax. Nodes for other observations, such as $\mathrm{fdt}(\ldots,\textit{empty})$ when she saw *full*, are not intervened on; they keep their priors.

Two honest caveats follow. First, the result is only as good as $G$: the paper's claims about A-FDT's performance are conditional on $G$ being right. Second, different reasonable choices of $G$ in murky cases (partial copies, predictors of uncertain method, correlated-but-not-computed agents) can change the verdict. The paper does not adjudicate those cases.

## 5. Worked applications

### 5.1 Twin prisoner's dilemma

Payoffs: both cooperate, \$1,000,000 each; both defect, \$1,000 each; unilateral defector \$1,001,000, cooperator \$0. $G$ has one node $\mathrm{fdt}$ with arrows to both players' actions. Suppose the twin's action matches mine with probability $\rho$.

$$EU(C)=\rho\cdot 10^6,\qquad EU(D)=1000\rho+1{,}001{,}000(1-\rho).$$

$C$ wins iff $2{,}000{,}000\rho>1{,}001{,}000$, that is $\rho>0.5005$ (my computation). With $\rho=1$ this is the paper's reasoning: "If it concludes that cooperation is better, then we both cooperate and I get \$1,000,000."

### 5.2 Newcomb's problem

Fiona's graph has $\mathrm{fdt}(P^F,G^F)$ pointing to both $\mathrm{Act}$ and $\mathrm{Prediction}$, which feeds $\mathrm{Box\;B}$. With $\mathrm{Accurate}$ having probability 0.99:

- $\mathtt{do}(\mathrm{fdt}=\textit{onebox})$: $P(\text{full})=0.99$, so $EU=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\textit{twobox})$: $P(\text{full})=0.01$, so $EU=\$11{,}000$.

She one-boxes. (The source's EDT paragraph gives \$999,000 for Eve's one-boxing; by its own numbers $0.99\times\$1{,}000{,}000=\$990{,}000$, so I take that as a typo.) For general accuracy $a$, one-boxing wins iff $a>0.5005$.

A natural objection: if she is nearly sure the box is full because her procedure one-boxes, won't she reconsider? The paper's answer is that to evaluate two-boxing she must imagine the procedure outputting *twobox*, and in that hypothetical the prediction differs. Nothing retrocausal is assumed: "she just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value."

### 5.3 Smoking lesion: the same rule gives a different graph

Here A-FDT does *not* reuse the Newcomb graph. A lesion does not compute the agent's decision function, so $\mathrm{Cancer}$ is not downstream of the $\mathrm{fdt}$ node; $\mathrm{Lesion}$ is upstream of $\mathrm{Act}$. Intervening on $\mathrm{fdt}$ leaves $P(\text{lesion})=p$ unchanged, and smoking gains $\$1000$ with the cancer risk held fixed. In the source's formalization the lesion fixes preferences, so there are two candidate procedures, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, and the agent does not know which she runs. Smoking then beats refraining by $p\cdot\$1000$. The source itself calls this setup contrived and recommends philosophers abandon the problem. The lesson is that **one rule, different graphs**: the Newcomb/lesion asymmetry lives entirely in $G$.

### 5.4 Transparent Newcomb and Parfit's hitchhiker

The agent sees a full box. A-FDT intervenes on $\mathrm{fdt}(\ldots,\textit{full})$. Take $q$ to be her prior probability of two-boxing upon seeing empty. If the prediction is accurate (0.99) and she sets $\mathrm{fdt}(\ldots,\textit{full})=\textit{onebox}$, the box is full and she gets \$1,000,000; if inaccurate, the box is empty, the empty-node controls, and she gets about $1000q$. Total: $\$990{,}000+10q$. For $\textit{twobox}$: if accurate, the prediction is "two-box", the box is empty, and she receives $1000q$ in expectation; if inaccurate, the box is full and she gets \$1,001,000. Total: $\$10{,}010+990q$. (The source prints this as "\$110,00 + q·\$990", evidently garbled; my arithmetic gives $10{,}010$.) With $q=1$, one-boxing gives about \$990,010 and two-boxing about \$11,000.

Note what happened: when she imagines two-boxing *while looking at a full box*, she imagines a world where she probably saw an empty box. The paper's gloss: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*." The paper observes that this case is "precisely equivalent to paying the driver in Parfit's hitchhiker problem." A-FDT pays. The predictor's output depends on what the procedure does when it finds itself in the city, and that decides whether the agent is rescued at all.

### 5.5 Blackmail: a threshold computation

In the mechanical blackmail problem, the blackmailer runs her program iff she predicts the agent would pay. Setting $\mathrm{fdt}(\ldots,\textit{blackmail})=\textit{pay}$ makes blackmail near-certain and costs \$1,000. Setting it to *refuse* makes blackmail unlikely, even though the damage if it happens is \$1,000,000.

With predictor error $\varepsilon$ (the chance the blackmailer wrongly predicts payment from a would-be refuser), refusing costs about $\varepsilon\cdot\$1{,}000{,}000$ and paying costs \$1,000. The break-even is $\varepsilon=0.001$. The source says refusing is correct at $\varepsilon=0.0009$ (expected loss \$900), which agrees. It then says she pays at $0.011\%$, but that number gives an expected loss of only about \$110 from refusing, so by the source's own arithmetic she would still refuse. The break-even I derived is 0.1%. I take the source's figure to be a typo. The qualitative point stands, and it is stated in the source: she refuses "even when holding the blackmail letter, even though she *knows* that the blackmailer predicted wrongly—because it's advantageous to be *the kind of agent* that makes such decisions."

### 5.6 Other cases from the source

- **XOR blackmail.** The letter's arrival depends on the $\mathrm{fdt}(\ldots,\textit{letter})$ node and on the infestation, but the infestation is not downstream of the procedure. So paying cannot reduce the termite probability. A-FDT refuses, whereas EDT pays, because conditioning on paying makes termites impossible.
- **Death in Damascus.** Death's book entry depends on the procedure's output. A-FDT concludes "wherever she goes, Death will be," and stays, saving \$1,000. CDT oscillates, because its hypotheticals hold Death's location fixed.
- **Cosmic ray problem.** A-FDT takes \$100: it will "dismiss your warning" that she only ever takes \$100 when hit by rays, because that is a merely statistical correlation. EDT takes \$1.
- **Coordination.** In a ten-person voting game, group members' decisions are "not subjunctively independent," so A-FDT agents vote. For self-coordination over time (the gym example), if today's and next week's decisions are relevantly identical, the same node controls both, so she goes today.

## 6. How A-FDT sits between EDT and CDT

The paper's diagnosis is symmetric. "EDT respects too many action-environment correlations, while CDT respects too few." EDT keeps even correlations with no mechanism, and so "manages the news." CDT breaks even the logically necessary correlations with predictors and twins, and so imagines "known-to-be-perfect predictors inexplicably falter exactly when Carl makes his current decision." A-FDT's hypotheticals preserve exactly those correlations that arise from some process computing the same function.

When all correlations between $\mathrm{Act}$ and other variables are caused by $\mathrm{Act}$ (the only exception being the $\mathrm{fdt}$ node on which $\mathrm{Act}$ itself depends), the three equations agree: $E[V\mid a]=E[V\mid\mathtt{do}(a)]=E[V\mid\mathtt{do}(\mathrm{fdt}=a)]$. They come apart only where something other than the agent's causal influence produces action-correlated events, typically other agents modeling the agent.

**Dominance.** The source argues that "every method for constructing hypotheticals gives rise to its own notion of dominance." Two-boxing dominates under CDT's hypotheticals. Refraining "dominates" smoking under EDT's. Under A-FDT's, an action $a$ dominates $b$ if, "holding constant all relevant subjunctive dependencies," switching the algorithm's output from $b$ to $a$ is sometimes better and never worse. Under this notion, A-FDT agents never take a dominated action. So dominance is not a theory-neutral tiebreaker, and the source falls back on utility achieved.

**Is this a delusion?** The paper's reply to "A-FDT agents think they can control mathematics" is a parity argument. A deterministic CDT agent also has only one action available and merely *imagines* worlds where it differs. Any objection to "controlling" the decision type equally impugns "controlling" the decision token.

## 7. Scope, fairness, and limits

The source claims A-FDT does better "in all dilemmas where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand," which it informally calls "fair problems." Newcomb's predictor "punishes *two-boxers*"; it does not punish a decision theory. A scenario that pays based on *which algorithm* you run (for instance, rewarding anyone who follows CDT) is not fair in this sense, and no theory dominates across all such problems. The source admits it has no formal criterion of fairness, and it has "not been able to construct an intuitively fair dilemma where FDT loses to a rival decision theory." A footnote notes an obstacle to formalizing the criterion: a copy of Fiona who punishes anyone taking the same action as the copy.

Beyond the open problems the paper names (inferring subjunctive dependence, fairness, optimality), my own additional observations are:

1. **Graph sensitivity.** Since Equation (4) takes $G$ as given, a skeptic may say the theory only relocates the problem. The paper agrees that this is the open problem; the theory is a decision rule *conditional on* a dependence model, not a method for producing that model.
2. **Unspecified cases.** Partial copies, agents who merely resemble the agent, and predictors using unknown methods are not handled by the source. My Step 2 suggestion (edge strength as a reliability variable) is a proposal, justified only by the paper's treatment of imperfect predictors via $\mathrm{Accurate}$.
3. **Actions versus policies.** The source says its preferred formulation uses policies and that the difference matters in some multi-agent dilemmas, without saying which. I do not claim to know.

## 8. Conclusion

A-FDT, as given by Equation (4), is a small modification of CDT with large consequences. Replace "intervene on my physical act" with "intervene on the output of my own decision function, given the observation I actually received," and supply a graph recording which parts of the world depend on that output. The resulting procedure one-boxes, cooperates with twins, smokes, pays the driver in the desert, refuses blackmail, and stays in Damascus. It does so without ratification, precommitment, or belief in retrocausation, and it agrees with CDT and EDT wherever their disagreements do not arise.

What the theory demands in return is a dependency model that the source frankly concedes nobody yet knows how to derive. Used with care, in the way sketched in §4, A-FDT is a usable decision procedure for any case where you can say, defensibly, which things in the world are computed from your own decision rule. Where that cannot be said, the theory under-determines the answer, and the source offers no way to settle it.

## Reference

Yudkowsky, E., and Soares, N. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060. All quotations above are from this paper; the A-FDT label, the construction procedure in §4, and the threshold computations in §§5.1–5.5 are my own.