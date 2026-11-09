# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. Introduction and naming

Newcomb's problem and the smoking lesion problem have the same payoff structure. A background process, which the agent's physical act cannot affect, settles whether she gets $1,000,000, and she then chooses whether to take a sure $1,000. Causal decision theory (CDT) two-boxes and smokes. Evidential decision theory (EDT) one-boxes and refrains. The source paper, Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, argues that a single rule can one-box and smoke, because a predictor and a lesion differ in a way both CDT and EDT ignore.

The paper's abstract describes the core idea as treating "one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper calls its theory FDT. In this essay, **A-FDT** means the specific procedure of the paper's Equation (4), Section 5. It intervenes on a node representing the output of the agent's decision procedure and ranks *actions*. The paper's footnotes say that its authors' preferred formalization ranks *policies* (maps from observations to actions), which matters only in some multi-agent problems. I discuss that variant briefly in §6. I call it the policy-level variant and do not treat it as part of A-FDT. I mark my own proposals as such throughout.

## 2. The shared frame: expected utility over hypotheticals

The paper treats EDT, CDT and A-FDT as expected utility theories. They differ over how to read the connective in

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),\tag{1}$$

where $a$ is an action, $x$ an observation history, and $P(a\hookrightarrow o_j;x)$ the probability that $o_j$ obtains in the hypothetical scenario where $a$ is executed after observing $x$. Joyce's representation theorem, which the paper cites, says the theories agree on how to value prospects once an "epistemic perspective" is fixed. In the paper's words, they differ over "the epistemic perspective from which actions are to be evaluated." So the substantive question is how to construct a hypothetical $M^{a\hookrightarrow}$ from a world-model $M$.

- **EDT** (Eq. 2) conditions: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- **CDT** (Eq. 3) takes a model $(P,G)$, where $G$ is a causal graph, and intervenes on the physical act with Pearl's operator: $\arg\max_a \mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. The operator sets $\mathrm{Act}=a$, recomputes everything causally downstream, and leaves everything else untouched.

The paper describes hypotheticals as "decision-theoretic instruments constructed from beliefs." They are scratch paper, not claims about the world.

## 3. Equation (4): the definition of A-FDT

The paper's Equation (4) is

$$\mathrm{A\text{-}FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Its ingredients are as follows.

1. **A world-model $(P,G)$.** $P$ is a probability distribution over variables, including variables for the outputs of mathematical functions. The paper's example is a variable for $6288+1048$ that "(hopefully) has most of its probability on 7336." $G$ is a graph, like a causal graph, saying how changing a *logical* variable propagates to other variables. $G$ is a required input. It is not derived from $P$.
2. **A distinguished node $\mathrm{fdt}(\underline P,\underline G,\underline x)$.** This variable represents what the A-FDT procedure itself outputs when run on this model and these observations. The underlines indicate dequoting, so the node's name depends on the contents of the model. The self-reference is harmless: the agent need not know the *value* of her own output in order to have a variable *representing* it, and Kleene's second recursion theorem ("quining") shows how data structures can contain accurate representations of themselves.
3. **Intervention on that node.** For each candidate $a$, the agent performs surgery, forcing the node to $a$ and propagating along $G$'s arrows. She computes expected utility in the resulting distribution and then executes the maximizer.

The paper names two differences from CDT.

- **What is intervened on.** CDT intervenes on $\mathrm{Act}$, a physical fact about her body. A-FDT intervenes on a logical fact about her decision function. In Peirce's terms, CDT intervenes on the token and A-FDT on the type.
- **How observations are handled.** CDT conditions on $\mathrm{Obs}=x$. A-FDT never conditions on $x$. It *changes which node it intervenes on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$ when she sees $y$ instead. Because the observation is a downstream consequence of what other instances of the function output, intervening on the node for $x$ can change the probability that she saw $x$ at all. The paper says this explicitly: A-FDT "should entertain the hypothesis that, if their action were different, they might have *made different observations*."

I note one small inconsistency in the source. The transparent Newcomb discussion writes the objective with "$\mathrm{Obs}=\mathrm{full}$" inside the expectation. The numbers actually computed there match Equation (4), which has no such conditioning. Conditioning on the observation after intervening would reintroduce the "double update" that the paper criticizes in Timeless Decision Theory, so I read Equation (4) as the authoritative statement.

**Relation to CDT and EDT.** The paper's Section 5 states that when every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$, "except perhaps $\mathrm{fdt}(\underline P,\underline G)$, on which Act may subjunctively depend," then

$$\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=a)],$$

and the three theories agree. They diverge when something correlates with the agent's action without being caused by it, as with predictors and twins.

## 4. What the graph must encode: subjunctive dependence

The paper introduces **subjunctive dependence** to say which variables should move when the node is set. When two physical systems compute the same function, their behaviors subjunctively depend on that function. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." The controlling assumption is that "when she imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

Three clarifications from the paper:

- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere correlation is not dependence. If the calculators in Paris and Tokyo happen to both be pink, buying a green one in Paris would not change Tokyo's.
- Imperfect predictors give weakened but nonzero dependence, like two calculators that might suffer a cosmic-ray error.

Since a deterministic function has only one output on a given input, setting the node to a non-actual value is a *counterpossible* supposition, like asking what would follow if $6288+1048\neq 7336$. The paper admits that no satisfactory account of counterpossible reasoning exists and calls this "the main drawback of FDT relative to CDT at this time." It argues the difficulty is technical, not philosophical, since agents need only answer narrow questions like "How would this predictor's prediction of my action change if the FDT algorithm had a different output?" It also considers a variant, FDT′, which asks what would happen if she used a different decision function, and shows this does not help. The predictors of $d$ must still be imagined as predicting a different behavior from $d$, which is the same counterpossible problem.

Equation (4) therefore *sidesteps* counterpossible logic by taking the dependency structure $G$ as given, just as CDT takes causal structure as given. The paper concedes that "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem."

**A practical recipe for building $G$.** This is my elaboration, not the paper's. It is consistent with the worked examples.

1. Identify every process in the situation that implements or accurately models the agent's decision function: predictors, twins, copies, her own later selves. Give each its own node, downstream of the function-output node, plus exogenous noise nodes for their reliability.
2. Create a separate function-output node for each possible observation, and wire the observation-generating process so that it decides which node controls $\mathrm{Act}$.
3. For every other variable (lesion, termites, weather), ask the paper's pink-calculator question. Would it have been different, as a matter of computational necessity and not mere correlation, had the function output something else? If not, it stays upstream of or disconnected from the function node.
4. Evaluate with $\mathtt{do}$ on the node for the actual observation.

## 5. Worked applications

Throughout, A-FDT is the procedure of Equation (4), and I compute the quantities the paper does.

### 5.1 Twin prisoner's dilemma

The agent and her twin run the same function, so $\mathrm{fdt}$ feeds both $\mathrm{Act}_{\text{me}}$ and $\mathrm{Act}_{\text{twin}}$. Setting $\mathrm{fdt}=\textit{cooperate}$ yields \$1,000,000 and setting it to *defect* yields \$1,000. A-FDT cooperates. The twin's act is not causally downstream of hers, and no physical signal is sent. Her twin is simply another instance of the function she is varying.

### 5.2 Newcomb's problem

The model has stochastic nodes $\mathrm{Accurate}$ (0.99) and the function output. $\mathrm{Prediction}$ and $\mathrm{Act}$ both descend from $\mathrm{fdt}$, and $\mathrm{Box\,B}$ descends from $\mathrm{Prediction}$.

- $\mathtt{do}(\mathrm{fdt}=\textit{onebox})$: $\mathrm{Act}=\textit{onebox}$ and the box is full with probability 0.99, so $\mathbb E[V]=0.99\times 1{,}000{,}000=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\textit{twobox})$: the box is full with probability 0.01, so $\mathbb E[V]=0.01\times1{,}001{,}000+0.99\times1{,}000=\$11{,}000$.

A-FDT one-boxes. Here, A-FDT's expected utilities match EDT's in structure. CDT instead breaks the arrow from the function to the prediction, so the box is full with some fixed probability $p$ regardless, and two-boxing gains \$1,000 for any $p$.

The standard objection is that an agent nearly sure the box is full should "reflect" and two-box. The paper's reply is that the *what-if* question is answered by intervening on the function, not the act. If the function outputs *twobox*, the same function was run by the predictor, and the box is probably empty. No retrocausation is involved.

### 5.3 Smoking lesion

Here the graph must differ. The lesion is not a function of the decision procedure, so it stays upstream, and intervening on the function node does not move the probability of cancer. The paper formalizes the problem with two utility functions, $\mathcal U_S$ (smoking valued) and $\mathcal U_R$ (smoking at −\$1), and two function nodes. The lesion determines which node controls $\mathrm{Act}$. With $P(\text{lesion})=p$, smoking beats refraining by $p\cdot\$1{,}000$, the probability that the function being varied is the one actually controlling her act, times the value of smoking. A-FDT smokes.

One rule thus one-boxes and smokes, with the differences carried by $G$ and not by ad hoc repairs. The paper also notes that this formalization is contrived, since the agent is uncertain about her own desires. It calls the problem "badly confused" and recommends abandoning it.

### 5.4 Transparent Newcomb and Parfit's hitchhiker

With transparent boxes the agent sees the contents. Two nodes exist, $\mathrm{fdt}(\underline P,\underline G,\textit{full})$ and $\mathrm{fdt}(\underline P,\underline G,\textit{empty})$, and $\mathrm{Prediction}$ decides which controls $\mathrm{Act}$. Write $q$ for her credence that she two-boxes on seeing an empty box. She has seen *full*, so she intervenes on the first node.

- $a=\textit{onebox}$: with probability 0.99 the prediction is accurate, so the box is full and she gets \$1,000,000. Otherwise she sees an empty box, and the value is $q\times\$1{,}000$. The total is $\$990{,}000+10q$.
- $a=\textit{twobox}$: with probability 0.99 the prediction was "two-box", so the box is empty and she acts per the other node, getting $990q$. With probability 0.01 she gets \$1,001,000. The total is $\$10{,}010+990q$.

(The source prints this total with a typographical garble, "\$110,00". The calculation gives $10{,}010+990q$.) One-boxing wins for any $q\in[0,1]$. When imagining two-boxing on seeing a full box, she imagines a world where she probably saw an empty box. This is the same structure as Parfit's hitchhiker, where paying in the city is analogous to one-boxing on a full box. The paper acknowledges this is odd and defends it on three grounds: agents would precommit to it, it never assigns negative value to information, and it maximizes utility.

### 5.5 Blackmail, with error rates

In the mechanical blackmail problem, the blackmailer runs the program iff she predicts the agent would pay. The node $\mathrm{fdt}(\ldots,\textit{blackmail})$ feeds both $\mathrm{Blackmailer}$ and $\mathrm{Act}$. If the agent pays, she is blackmailed with probability near 1 and loses \$1,000. If she refuses, she is blackmailed with probability near 0. A-FDT refuses even holding the letter.

Suppose the blackmailer wrongly predicts "pays" with probability $\varepsilon$. Paying costs about \$1,000. Refusing costs $\varepsilon\times\$1{,}000{,}000$ in expectation. The break-even point is $\varepsilon=0.001$. The paper's first example ($\varepsilon=0.0009$) fits: refusal costs \$900. But the paper's second example says that at $\varepsilon=0.011\%$ she pays. On Equation (4) that would cost only \$110 for refusing, which beats paying. The paper's figure appears to be a slip for 0.11%, where refusal costs \$1,100 and she pays. I flag this as an apparent error in the source, derived from Equation (4) itself.

### 5.6 XOR blackmail and Death in Damascus

In XOR blackmail, termites are upstream of the predictor and of the letter. They are *not* downstream of the function node, so intervening does not change the probability of infestation. It changes only whether the letter arrives. Refusing is better, since A-FDT does not treat the letter as news about termites that her act could "manage." Carl and the A-FDT agent both refuse, but for different reasons. Carl holds the infestation fixed because it is causally upstream of his act. A-FDT holds it fixed because it is not downstream of the function. They differ in their hypotheticals: Carl's says the predictor erred, while A-FDT's says the letter would not have been sent.

In Death in Damascus, Death's book is downstream of the function. Setting the output to *stay* puts Death in Damascus, and setting it to *flee* puts him in Aleppo at a cost of \$1,000. A-FDT stays and saves the \$1,000. There is no instability because there is no incentive to revise: the hypotheticals already include the dependence that CDT must patch with ratification.

## 6. Where the source is silent: operational interpretations

**(a) Nuisance nodes.** The computations above depend on $q$, a credence about what the same function would output on other observations. In the examples $q$ drops out of the comparison, and the paper says "it doesn't matter." In general it might not drop out. *My proposal:* treat $q$ as a model parameter, check whether the argmax is robust across the plausible range of $q$, and if not, solve a joint problem over the other nodes' outputs. This is essentially the policy-level variant that footnote 7 says the authors prefer: maximize $\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)]$ over maps $\pi:\mathcal X\to\mathcal A$. The paper says the difference "only matters in multi-agent dilemmas so far as we can tell." I treat the policy-level variant as an extension and not as Equation (4).

**(b) Counterpossibility without logic.** I suggest treating the node as an exogenous "switch" variable in a structural model, with no probability on the contradiction itself. The agent never needs $P(\text{fdt}=\textit{twobox})$ for the surgery to work, since $\mathtt{do}$ overrides the prior. This is a reading of the paper's move of taking $G$ as input, not a solution to the underlying problem.

**(c) Reliability and partial dependence.** For imperfect predictors, the paper's own examples encode reliability as an exogenous noise node. I would generalize by giving each dependent process a noise node whose parameters reflect how well it models the function. This extends the paper's pattern, since the paper only shows it for predictors.

**(d) Fairness.** The paper claims A-FDT does best in "fair" problems, those where outcomes depend only on behavior in the problem at hand, with agent beliefs accurate. It admits that no formal criterion exists. Footnote 15 gives the example of a problem that punishes anyone who matches a copy of the agent, which is unfair to her but not to CDT or EDT. A reader should treat the fairness claim as unproven.

**(e) Risk of graph gerrymandering.** This is my own concern. Because $G$ is an input, A-FDT's verdicts are only as good as the dependency structure. Two modelers can disagree about whether a given process models the agent's function or merely correlates with it, and the theory as stated offers no adjudication. This is the same gap the paper identifies as its largest open problem.

## 7. Why one might adopt A-FDT

The paper's argument has three strands.

1. **Utility.** Predictors that can follow these arguments will see that CDT and EDT agents two-box and pay, and that A-FDT agents don't. So A-FDT agents tend to face full boxes and unthreatening blackmailers. The paper treats this as primary: "Utility has primacy."
2. **Dominance is theory-relative.** Two-boxing dominates only if hypotheticals hold the prediction fixed. Every method for constructing hypotheticals induces its own dominance notion. Under the A-FDT-style notion, an A-FDT agent never takes a dominated action.
3. **No more delusional than CDT.** A deterministic CDT agent "could" have acted otherwise only in imagination. The same holds for A-FDT agents and their function's output. Both imagine impossible worlds, but A-FDT's track the dependencies in the real world.

EDT "respects too many action-environment correlations," whereas CDT "respects too few." A-FDT is meant to get the balance right. Its characteristic reflective-stability claim, that an A-FDT agent holding the blackmail letter would not wish to switch to CDT, rests on the same hypotheticals.

## Conclusion

A-FDT, as Equation (4) states it, is a short rule with a long list of inputs. Take a model $(P,G)$ that includes a node for what your own decision procedure outputs on each possible observation. For each action, intervene on the node for the observation you actually made, propagate through the dependency graph, and compute expected utility. Then take the best action. The rule matches CDT where only causal dependence exists, and it matches EDT's one-boxing where predictors replicate your reasoning. It declines EDT's news-management and CDT's severing of logical dependence. Its main difficulties are the ones the source openly names: the lack of a theory of counterpossibles, no principled method for learning $G$, and no formal notion of fairness. Beyond these, the source's conclusions in transparent-box and blackmail cases are counterintuitive and defended mainly by appeal to utility. A user of A-FDT should expect the work to lie in building the graph.

## References

- Yudkowsky, E. and Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060).
- Joyce, J., *The Foundations of Causal Decision Theory* (1999).
- Pearl, J., *Causality* (2000).
- Gibbard, A. and Harper, W., "Counterfactuals and Two Kinds of Expected Utility" (1978).