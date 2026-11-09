# A-FDT: Choosing by Intervening on Your Own Decision Function

## 1. What this essay covers

The source is Yudkowsky and Soares' paper *Functional Decision Theory: A New Theory of Instrumental Rationality*. Its slogan is that a rational agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" This essay is about the formal procedure in **Equation (4), Section 5**, which I call **A-FDT** (the action version of functional decision theory). The paper calls the same procedure FDT.

I use "A-FDT" for Equation (4) throughout. The paper's footnotes 7 and 16 say its authors' *preferred* formalization intervenes on a *policy* (a map from observations to actions) rather than on an action. A-FDT is the action-and-observation version the paper actually works with, and I treat the policy version as a neighbouring theory. I call the paper's other theories CDT (causal decision theory) and EDT (evidential decision theory). I call the paper's discarded variant, which asks what happens if one *used a different decision function*, FDT$'$.

I mark each claim as one of three kinds. **[Source]** is something the paper states. **[Derived]** is something that follows by calculation from the paper's models. **[Mine]** is my own interpretation or proposal.

## 2. The formal definition

### 2.1 The shared expected-utility skeleton

[Source] EDT, CDT and A-FDT are all expected-utility theories. They choose an action $a\in\mathcal A$ to maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),\tag{1}$$

where $x$ is the observation history and $P(a\hookrightarrow o_j;x)$ is the probability that outcome $o_j$ obtains in the *hypothetical* in which $a$ is executed after observing $x$. Following Joyce's representation theorem, the theories differ only in how they interpret the connective "$\hookrightarrow$". The paper quotes Joyce: they disagree "about the epistemic perspective from which actions are to be evaluated."

[Source] The agent keeps a world-model $M$. For each action $a$ she builds a *hypothetical* $M^{a\hookrightarrow}$, a transient instrument for evaluating that action and not a belief. She computes $V_a$ from each hypothetical and takes the largest. The three theories differ in what $M$ is and how the hypotheticals are built.

- EDT: $M=P(\cdot\mid x)$, and the hypothetical conditions on the act, $\operatorname{argmax}_a\mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT: $M=(P,G)$ with $G$ a causal graph, and the hypothetical is a Pearl surgery on the *physical act*, $\operatorname{argmax}_a\mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.

### 2.2 Equation (4)

[Source] A-FDT takes as input a probability distribution $P$ over the variables of the agent's model, a graph $G$, and an observation $x$. It returns

$$\mathrm{A\text{-}FDT}(P,G,x)\;:=\;\operatorname*{argmax}_{a\in\mathcal A}\;\mathbb E\Big(V\;\Big|\;\mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).\tag{4}$$

Four features need unpacking.

1. **The intervened variable is logical.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node standing for *the output of this very procedure when run on these very inputs*. The underline means "dequoting": it turns the actual values of $P,G,x$ into part of the variable's name. $P$ must therefore contain variables for outputs of mathematical functions, such as the value of $6288+1048$.

2. **The self-reference is harmless.** The model contains a variable whose name mentions the model. The paper says the agent "does not need to know the *value* of $\mathrm{FDT}(M,x)$ in order to have a variable representing that value." Kleene's second recursion theorem ("quining") shows that such self-representing data structures exist.

3. **Observation changes where you intervene, not what you condition on.** CDT responds to a new observation by conditioning on it. A-FDT responds by intervening on a *different node*, $\mathrm{fdt}(\underline P,\underline G,\underline y)$ instead of $\mathrm{fdt}(\underline P,\underline G,\underline x)$.

4. **The graph carries the dependence information.** The paper observes that a clean operator "$\mathtt{true}(\phi)$" for updating on a logically false sentence is not available. It therefore requires that $G$ "tells us how changing a logical variable affects all other variables," and then reuses Pearl's $\mathtt{do}$. So the theory works *given* a graph that correctly encodes subjunctive dependence. The paper says that constructing such graphs is "perhaps the largest open problem in the study of functional decision theory."

### 2.3 The one-line comparison

The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT intervenes on the *token* "my action is $a$". A-FDT intervenes on the *type*, the function's output, and lets the surgery propagate along every edge that represents dependence on that output. These edges include causal ones. The paper argues causal dependence is a special case of subjunctive dependence (the scribe who copies a calculator's output depends on it subjunctively too).

Where every correlation between $\mathrm{Act}$ and the world is caused by $\mathrm{Act}$, the paper notes that all three theories coincide:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)].$$

They split only when something correlates with the action without being caused by it: predictors, twins, copies.

## 3. Subjunctive dependence

[Source] Two physical systems that compute the same function "subjunctively depend" on that function. If the calculator in Paris outputs 7336 for $6288+1048$, the one in Tokyo (if working) would too, and if the first had output something else, the second would have as well. This is not common cause, and it is not mere correlation. Two *pink* calculators are statistically correlated in color, but had the Parisian calculator been green, the Tokyo one would still be pink.

[Source] When the A-FDT agent imagines taking different actions, "she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure." Everything else, including the lesion, the termites and the weather, is held fixed.

The paper admits that this requires evaluating *counterpossibles*: if the function outputs $a_1$ on this input, then it does so necessarily, and the hypothetical "outputs $a_2$" is logically impossible. Its response is that this is a technical difficulty and not a philosophical one. Mathematicians reason sensibly under logical uncertainty, and the agent only needs narrow questions like "how would this predictor's prediction change if the algorithm had a different output?" FDT$'$ ("what if I used a different function?") does not escape the problem, because the agent must still imagine every predictor of her actual function $d$ behaving as if $d$ behaved like the substitute.

[Mine] One practical reading of the requirement: *place an edge from the node $\mathrm{fdt}$ to a variable $Z$ exactly when $Z$'s value is produced by something that computes, or accurately models, this decision function.* A test is to ask, "If my deliberation reached a different conclusion, would $Z$ have been produced by a different computation or a different input?" A predictor that simulates me passes. A lesion that merely causes both my tastes and my cancer does not. Its output does not depend on any representation of my deliberation.

## 4. A procedure for applying A-FDT

The paper gives the algorithm only through examples. Here is the pattern they follow, made explicit.

1. **Write down the model $P$.** Include variables for the agent's act, the other agents' predictions or copies, the stochastic "accuracy" or luck variables, and utility.
2. **Identify the decision function's nodes.** If the problem has several possible observations, there is one node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ per observation. Each controls $\mathrm{Act}$ in the branch where $x$ is observed.
3. **Draw the dependence graph $G$.** Draw arrows from each such node to every variable that is, or models, an output of this function: the agent's own act (when that observation occurs), and any predictor's prediction. Draw no arrows to variables that merely correlate with the act through a non-computing common cause.
4. **For each action, intervene.** Set the node for the *actual* observation to $a$, propagate along the arrows, and compute $\mathbb E[V]$. The same intervention changes which observation occurs, if observations are downstream of the prediction.
5. **Take the argmax.**

Two points on step 4. In the paper's transparent-box computation, the value $\mathrm{Obs}=\textit{full}$ is not held fixed inside the hypothetical. The notation "$\mathtt{do}(\mathrm{fdt}(\ldots,\textit{full})=a,\ \mathrm{Obs}=\textit{full})$" only indexes *which* node is intervened on. In the hypothetical where that node outputs *twobox*, the agent very likely never sees a full box. I read this as the A-FDT analogue of updating on evidence: observations select the node, and they do not restrict the worlds. Second, the paper's graphs for Newcomb-like problems are stated to be models of the agent's *beliefs*, assumed accurate, and not of the situations themselves.

## 5. Worked examples

### 5.1 Twin prisoner's dilemma

The twin's choice $T$ is produced by the same function, so $\mathtt{do}(\mathrm{fdt}=a)$ sets both $\mathrm{Act}$ and $T$. Cooperation yields \$1,000,000 and defection \$1,000, so A-FDT cooperates. CDT fixes $T$ and defects.

### 5.2 Newcomb's problem

[Source] The model (Figure "Bayesian network for Newcomb's problem") has a stochastic $\mathrm{Accurate}\in\{\textit{accurate}\ (0.99),\textit{inaccurate}\ (0.01)\}$, and $\mathrm{Prediction}$ and $\mathrm{Act}$ are both children of the node $\mathrm{fdt}(\underline P,\underline G)$. Then:

- $\mathtt{do}(\mathrm{fdt}=\textit{onebox})$: $\Pr(\text{full})=0.99$, so $\mathbb E[V]=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\textit{twobox})$: $\Pr(\text{full})=0.01$, so $\mathbb E[V]=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

A-FDT one-boxes. Carl (CDT) holds $\Pr(\text{full})=p$ fixed under both interventions and sees a constant \$1,000 advantage for two-boxing.

[Derived/Mine] A general version: with box A holding $\alpha_0$ dollars and box B holding $\beta$, and symmetric predictor accuracy $\alpha$, A-FDT compares $\alpha\beta$ against $\alpha_0+(1-\alpha)\beta$ and one-boxes iff $\alpha>\tfrac12+\tfrac{\alpha_0}{2\beta}$. For the source's numbers the threshold is $\alpha>0.5005$. This shows that A-FDT does not need a *perfect* predictor, only one whose reliability exceeds the threshold.

No retrocausation is invoked. The agent holds that "it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value."

### 5.3 Smoking lesion

Here the graph differs from Newcomb's even though the payoff table is the same. The paper's Figure shows $\mathrm{Lesion}$ as a parent of both $\mathrm{Act}$ and $\mathrm{Cancer}$, with the agent's decision-function node feeding only $\mathrm{Act}$. Intervening on the node leaves $\Pr(\text{lesion})=p$ unchanged, so smoking is better by $p\cdot\$1{,}000$, and A-FDT smokes. This is the point of Section 6's contrast: one rule, different graphs, so A-FDT one-boxes and smokes.

The paper models the lesion as changing the agent's *utility function* ($\mathcal U_S$ versus $\mathcal U_R$), so the agent's act depends on one of two decision-function nodes, $\mathrm{fdt}(\underline{P_S},\underline G)$ or $\mathrm{fdt}(\underline{P_R},\underline G)$, which of the two being fixed by the lesion. The paper calls the whole setup contrived and recommends that philosophers abandon it. I take it as an illustration of how graph structure, not payoff structure, drives the verdict.

### 5.4 Transparent Newcomb and Parfit's hitchhiker

This is where observation-handling matters. The agent sees a full box.

- **Intervene on $\mathrm{fdt}(\ldots,\textit{full})=\textit{onebox}$.** [Source] With $\mathrm{Accurate}=\textit{accurate}$ (0.99), the prediction is 1, the box is full, and she one-boxes: \$1,000,000. Otherwise the box is empty and the node $\mathrm{fdt}(\ldots,\textit{empty})$ controls her act, giving \$$1000q$, where $q$ is her probability of two-boxing on seeing it empty. Total: $\$990{,}000+10q$.
- **Intervene on $\mathrm{fdt}(\ldots,\textit{full})=\textit{twobox}$.** With probability 0.99 the prediction is "two-box", the box is empty, and the empty-node acts: $990q$. With probability 0.01 she sees a full box and two-boxes: \$1,001,000. Total: $10{,}010+990q$.

(The paper prints this second expression with a typo, "\$110,00"; the calculation gives $10{,}010+990q$, which is \$11,000 at $q=1$.) One-boxing wins for every $q\in[0,1]$. In her hypotheticals, imagining two-boxing means imagining a world where she *probably never saw a full box*.

[Source] The paper argues this is exactly equivalent to paying in Parfit's hitchhiker. Both decisions are made after the benefit has been received, and both are predicted by something that determines whether the benefit comes. The paper offers three arguments for this verdict. Precommitment: CDT and EDT agents would both *precommit* to one-box, so acting as though precommitted is better than paying to precommit. Value of information: EDT would pay to be blindfolded, whereas an agent who acts as she would have precommitted never assigns negative value to information. Utility: "in 99 cases out of 100, *the kind of agent* that is inclined to conditionally give in to that temptation will actually find herself staring at an empty box B."

### 5.5 Mechanical blackmail

[Source] The blackmailer runs a program (costing both parties \$1,000,000) iff she predicts the agent would pay \$1,000. A-FDT's graph has the node $\mathrm{fdt}(\ldots,\textit{blackmail})$ feeding the blackmailer's behavior and the act. Setting it to *pay* gives probability about 1 of being blackmailed and a \$1,000 loss. Setting it to *refuse* gives probability about 0 of being blackmailed. She refuses *while holding the letter*, since the hypothetical where the function refuses is one in which "she was never blackmailed in the first place."

[Source/Derived] With a blackmailer who errs with probability $\varepsilon$, paying costs \$1,000 for certain, while refusing costs $\varepsilon\cdot\$1{,}000{,}000$ in expectation. The break-even is $\varepsilon=0.001$. The paper gives $\varepsilon=0.0009$ (refuse; expected loss \$900), which is consistent. Its second example, "0.011%", does not match this arithmetic, since that would be \$110 and still favor refusing. I suspect it meant 0.11%, which gives \$1,100 and favors paying. Either way the logic is the same: the verdict flips where the hypothetical expected losses cross.

### 5.6 XOR blackmail

[Source] Termites are causally upstream of the letter. The predictor sends it iff (no termites and the agent pays) or (termites and the agent doesn't pay). The agent's decision-function node feeds the prediction, and hence the letter and the act, but not the infestation. EDT pays because conditioning on payment makes termites improbable. A-FDT refuses. Changing the function's output changes whether she receives the letter, not whether she has termites. CDT also refuses, but it reports that, had it paid, the (infallible) predictor would have erred, while A-FDT reports that the letter would simply not have been sent.

### 5.7 Death in Damascus

[Source] Death's book entry depends on a perfect prediction of the agent's decision procedure. A-FDT's hypotheticals have Death's location following the intervened output. Staying yields certain death at no cost; fleeing yields certain death and −\$1,000. She stays. CDT oscillates, because it holds Death's location fixed.

[Mine, flagged as inference] The paper argues that Carl, under CDT, would refuse to pay \$1 for a truly random coin, because in CDT's hypotheticals the coin is no better than his own choice. An A-FDT agent should accept such a coin. Intervening on "use the coin" yields a node whose output is not predictable by Death, so survival probability is 0.5 for \$1. The paper does not compute this explicitly.

## 6. Why the theory is built this way

**Against EDT.** EDT's hypotheticals preserve *every* statistical correlation between act and world, including accidental ones. The cosmic-ray problem shows the cost. If Eve almost always takes \$1, then taking \$100 is evidence of a cosmic-ray hit (followed by a \$1,000 hospital bill), so she takes \$1 and her fear is self-confirming. A-FDT's intervention breaks inconvenient correlations that no computation underlies. Moreover, Eve's behavior depends on her priors: with $P(\text{act})$ extreme she cannot even condition on the alternative.

**Against CDT.** CDT breaks too many correlations. Carl's hypotheticals have perfect predictors err precisely when he decides. A-FDT keeps the dependence on the decision function that the predictor actually models.

**Dominance.** [Source] Two-boxing "dominates" only when one holds the prediction fixed, which amounts to asking us to imagine a calculator outputting 3159 while holding fixed that $6288+1048=7336$. A-FDT has its own dominance notion (hold subjunctive dependencies fixed and switch the function's output), under which it never takes a dominated action. Every method of building hypotheticals induces its own dominance relation, so dominance cannot arbitrate between theories. The paper prefers to compare theories by utility achieved.

**Fairness.** [Source] A-FDT is claimed to do at least as well as CDT and EDT in "fair problems": those where the agent's beliefs are accurate and outcomes depend only on the agent's behavior in the dilemma at hand. Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." A problem that directly rewards or punishes the decision *procedure* is out of scope, and no theory wins all such problems. The paper also notes that a copy of the agent that punishes anyone who matches the copy defeats A-FDT, and admits there is no formal definition of fairness yet.

**Reflective stability.** [Source] A-FDT acts as it would have precommitted to act, so it has no reason to self-modify into CDT mid-problem. The paper says A-FDT is "reflectively stable in fair problems," whereas CDT recommends changing methodology (given the chance) while keeping CDT for ongoing Newcomblike problems.

## 7. What the source leaves open, and operational interpretations

**(a) Where do graphs come from?** Equation (4) is conditional on $G$. The paper has no procedure for learning subjunctive-dependence structure from data, analogous to Pearl's for causes. Someone applying A-FDT must therefore *supply* $G$ from the problem description. In textbook cases, such as predictors that model the agent, twins, and copies, my heuristic from Section 3 is workable. It is not a theory. Two reasonable people could draw different graphs for the same ambiguous problem, and A-FDT would then give different answers. This is not a bug in the equation; it moves the difficulty into the model, as CDT does with causal graphs.

**(b) Imperfect or partial dependence.** The paper treats predictor error as a stochastic node ($\mathrm{Accurate}$), and shows its expected-utility effects in the blackmail and Newcomb cases. I recommend the same device generally: represent imperfect dependence by a noise variable between the function node and the dependent variable, so that the intervention shifts probabilities and does not set values.

**(c) Uncertainty about one's own output.** The paper requires only that the agent have a variable *representing* the output, not know its value. Each non-actual node is given a prior (the paper's $q$), and in its examples the result holds for every $q$. [Mine] That robustness is worth checking in any new application: if the verdict depends on an arbitrary $q$, the model is probably underspecified.

**(d) Action versus policy.** With observations this matters only in multi-agent settings, according to the paper's footnotes. My reading is that the action version suffices when the agent's *other* observation-branch nodes are determined within the model, as in the transparent boxes, and the policy version is safer when other agents' behavior depends on the entire policy.

**(e) Counterpossible semantics.** The paper hopes for an "evidential version" that conditions on logical facts but admits we lack conditional probabilities for false logical sentences. Equation (4) sidesteps this by treating the logical variable as a graph node. It is therefore a modeling convention for counterpossibles, not an analysis of them. The paper's philosophical defense is a parity argument: if "controlling" the decision type is suspect, so is a deterministic CDT agent's "controlling" her decision token.

**(f) Scope.** All the worked computations use the simplest models that capture each dilemma. A realistic agent would have a vast model, and A-FDT would be approximated. The paper expects bounded approximations of different theories to preserve their qualitative differences, but does not prove this.

## 8. Conclusion

A-FDT, as given by Equation (4), is expected-utility maximization with a particular choice of hypotheticals. The agent intervenes, in a dependence graph, on the variable representing the output of her own decision function for her actual observation. She lets every variable that computes or models that output vary with it, and holds everything else fixed. This single rule gives one-boxing in Newcomb's problem, smoking in the smoking lesion problem, paying in Parfit's hitchhiker, refusing both blackmail problems, and staying put in Damascus. The cost is that the theory depends on the supplied graph $G$, and the paper offers no general method for obtaining it. Applying A-FDT well is therefore mostly a matter of modeling carefully which things depend subjunctively on the agent's decision function and which merely correlate with it. When that modeling is done correctly, the paper claims, the resulting hypotheticals track the real dependence structure of the world better than the hypotheticals of CDT or EDT do.