# A-FDT: Choosing the Output of a Fixed Function

## 1. The core idea

Expected-utility theories differ in one place: how they build the hypothetical scenario used to evaluate an action. Evidential decision theory (EDT) conditions on the action. Causal decision theory (CDT) intervenes on the physical act and propagates the change along causal arrows. **A-FDT** is the theory defined by Equation (4) in Section 5 of Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. The paper calls it "FDT". I use "A-FDT" to mark that it is the action-valued version of the rule. The authors' preferred formalization ranges over *policies*, and I say below where that matters.

A-FDT intervenes on a *logical* fact, namely what the agent's own decision function outputs. The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." The agent asks which output of this very function would yield the best outcome, and she imagines everything that depends on that output changing with it.

This essay covers the formal definition, the inputs it requires, the places where the paper leaves implementation open, and worked examples. Claims from the paper are marked as such. Where I supply interpretation or extra assumptions, I say so.

## 2. The formal setup

All the theories discussed share the shape of Equation (1). An agent should execute an action $a \in \mathcal A$ maximizing
$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$
where $x$ is the observation history and $P(a\hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$". Following Joyce, the theories disagree only about the *epistemic perspective*, that is, about how to read "$\hookrightarrow$". Writing $V=\mathcal U(\text{Outcome})$:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V\mid \text{Obs}=x,\text{Act}=a)$.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V\mid do(\text{Act}=a),\text{Obs}=x)$, where the world-model is a pair $(P,G)$ with $G$ a causal graph, and $do$ is Pearl's operator.
- **A-FDT** (Eq. 4):
$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\Big(V\;\Big|\;do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The paper's own name for the rule is $\mathrm{FDT}$. I write A-FDT$(P,G,x)$ for the same map.

The paper's description of the "hypothetical for $a$" is useful. A hypothetical is a transient, "possibly quite representationally thin" object built from the agent's beliefs, like notes on scratch paper. It is a tool for evaluating actions, not a belief and not a mind-independent possible world.

### Reading Equation (4)

Four features need unpacking.

**(a) The intervention variable.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model representing the output of the A-FDT algorithm when run on this model and these observations. The underlines are dequoting: the node's *name* contains the values of $P$, $G$ and $x$. Different observations give different nodes.

**(b) Self-reference.** The model contains a node whose name depends on the model. The paper says this is harmless. The agent does not need to know the *value* of $\mathrm{FDT}(P,G,x)$ to have a variable representing it, and Kleene's second recursion theorem (quining) shows how a data structure can contain an accurate representation of itself.

**(c) Observation handling.** This is the second difference from CDT. CDT responds to a new observation by conditioning on it. A-FDT responds by changing *which node it intervenes on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. Equation (4) contains no conditioning on $x$ beyond the node's name. In the worked examples below, the expectation is taken over the *prior* distribution of the model, including worlds where the agent saw something different. This is why the paper says A-FDT agents "entertain the hypothesis that, if their action were different, they might have *made different observations*." It is also the source of the "updateless" label the paper mentions for an ancestor theory. The paper's text writes an "$\text{Obs}=\text{full}$" term inside the expectation in the transparent Newcomb discussion, but its computation does not condition on it. I follow the computation.

**(d) What $G$ must supply.** The $do$ operator needs a graph telling it which variables are downstream of the intervened node. For CDT these are causal arrows. For A-FDT the graph must encode *all decision-relevant subjunctive dependencies*: causal, logical, computational. The source states plainly that no analogue of Pearl's account exists for learning this structure. It calls the problem "perhaps the largest open problem in the study of functional decision theory," and says Equation (4) works "*given* a graph that accurately describes how changing the value of a logical variable affects other variables."

The paper also writes down a more ambitious rule, $\mathrm{FDT}^*$, using a $\texttt{true}(\phi)$ operator for conditioning on false logical sentences, and notes that nobody knows how to define such an operator. Equation (4) sidesteps this by requiring the logical dependency structure as an *input*, "in the same way that the relevant causal structure is given as an input to CDT."

## 3. Subjunctive dependence

Two things subjunctively depend on a function when they compute it, or when one contains a model of it. The paper's examples are two calculators computing $6288+1048$, and a predictor that holds an accurate representation of the agent. If one calculator outputs $7336$, we expect the other to. This holds even when the calculators share no causal history, and it weakens but does not vanish if one is faulty.

The paper makes these points:

- Causal dependence is a special case of subjunctive dependence. A scribe copying a calculator's display would write something different if the calculator output something different.
- Mere statistical correlation is *not* subjunctive dependence. Two pink calculators in Paris and Tokyo are correlated in color, but had the Paris one been green, the Tokyo one would still be pink.
- The relevant counterfactual is a **counterpossible**: a function that outputs *cooperate* on an input does so necessarily, so imagining it outputting *defect* means reasoning about a logical impossibility. The paper concedes that this lack of a satisfactory account is "the main drawback of FDT relative to CDT at this time." It argues the difficulty is technical, not philosophical. Humans reason under logical uncertainty routinely, and A-FDT agents only need narrow questions of the form "how would this predictor's prediction of my action change if the algorithm had a different output?"
- A variant FDT$'$ ("what if I used a *different* decision function?") does not avoid the problem. A predictor of the actual function must still be imagined as predicting "as if" the function behaved differently.

The summary assumption the paper needs is stated this way: when an A-FDT agent imagines taking two different actions, "she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure." Everything else is held fixed.

One consequence the paper draws: where all correlations between Act and the world are caused by Act (except possibly through the fdt node), the three expectations coincide:
$$\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)].$$
They come apart only when something other than the act correlates with it, such as a predictor or a twin.

## 4. How to apply A-FDT: a procedure

The paper presents Equation (4) as a procedure that "could in principle be scrupulously followed." Assembling its worked examples gives the following recipe.

1. **Build the model $(P,G)$.** Include nodes for the agent's act, the environment, and noise or accuracy variables.
2. **Add the fdt node(s).** Introduce $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for each observation $x$ the agent might receive. Make each such node a parent of whatever represents the agent's act when she sees $x$.
3. **Wire in subjunctive dependents.** Make the fdt node a parent of every process that computes or models it: predictors, twins, copies, future selves in relevantly identical situations. Do not make it a parent of merely correlated variables.
4. **Intervene.** For each $a$, set the node for the *actual* observation to $a$, propagate downstream, and compute $\mathbb E[V]$.
5. **Pick the maximizer.**

Unconditioned worlds, where the agent would have seen a different observation, enter step 4 with their prior weights. Any node for a different observation that influences the outcome needs a belief about its value. In the paper this appears as a parameter $q$ (see below).

## 5. Worked examples

### Newcomb's problem

The model has stochastic nodes Accurate ($0.99$) and Act. The paper's A-FDT graph puts $\mathrm{fdt}(\underline P,\underline G)$ as a parent of both Act and Prediction. Prediction determines Box B.

- $do(\mathrm{fdt}=\textit{onebox})$: Act is one-box, and Box B is full with probability $0.99$. Expected value is $0.99\times\$1{,}000{,}000=\$990{,}000$.
- $do(\mathrm{fdt}=\textit{twobox})$: Box B is full with probability $0.01$. Expected value is $0.99\times1000+0.01\times1{,}001{,}000=\$11{,}000$.

So A-FDT one-boxes. The paper stresses that no retrocausation is invoked. Fiona (the A-FDT agent in the paper's examples) merely finds it foolish "to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value." This holds even if she is nearly certain the box is full. Asked what would happen if she two-boxed, she answers that the algorithm would then have output *twobox* and the predictor would have modelled that.

The CDT graph, by contrast, makes Box B independent of the act given the Predisposition, so $do(\text{Act})$ leaves $P(\text{full})=p$ unchanged. Two-boxing then wins by $\$1000$ for any $p$. EDT conditions on the act and one-boxes if its prior on one-boxing is not extreme, though the paper's inline figure for EDT one-boxing, $\$999{,}000$, does not match $0.99\times10^6=\$990{,}000$, which I take to be a slip.

### Smoking lesion

The graph here differs from Newcomb's. The lesion is a common cause of the urge to smoke and of cancer, and the A-FDT node is *not* a parent of Cancer. The paper formalizes the lesion's effect on the agent as altering her utility function, so there are two possible algorithms, $\mathrm{fdt}(\underline{P_S},\underline G)$ and $\mathrm{fdt}(\underline{P_R},\underline G)$. The lesion decides which one drives Act. Intervening on the active node does not change $P(\text{lesion})=p$. Smoking beats refraining by exactly $p\cdot\$1000$, so A-FDT smokes.

The lesson is that the Newcomb and lesion problems have the same *probabilistic* structure but different *dependence* structure. Changing the graph, not the distribution, changes the answer. The paper adds that the lesion problem is contrived and "badly confused," and treats it for historical reasons.

### Transparent Newcomb and Parfit's hitchhiker

With transparent boxes the agent sees the contents. There are two nodes, $\mathrm{fdt}(\ldots,\textit{full})$ and $\mathrm{fdt}(\ldots,\textit{empty})$, and the prediction determines which one controls Act. Suppose she sees full, so she intervenes on $\mathrm{fdt}(\ldots,\textit{full})$. Let $q$ be her credence that she two-boxes when she sees empty.

- One-box: if Accurate (0.99), she gets $\$1{,}000{,}000$. Otherwise the box is empty and the other node acts, giving $q\cdot\$1000$ in expectation. Total: $\$990{,}000+0.01\,q\cdot\$1000$.
- Two-box: if inaccurate (0.01), she sees full and takes $\$1{,}001{,}000$. If accurate (0.99), the box is empty and she gets $q\cdot\$1000$. Total: $\$10{,}010+990\,q$. This is the paper's "$\$110{,}00+q\cdot\$990$" with a typo. It does not change the conclusion.

For any $q\in[0,1]$ one-boxing wins. When envisioning two-boxing on seeing a full box, she envisions a world in which she probably saw an empty box instead. The paper observes that this is exactly equivalent to paying the driver in Parfit's hitchhiker.

### Blackmail

In the mechanical blackmail, the blackmailer perfectly predicts the agent and runs the program iff she predicts payment. A-FDT's fdt node feeds the blackmailer node, so $do(\mathrm{fdt}=\textit{refuse})$ makes blackmail unlikely, whereas $do(\mathrm{fdt}=\textit{pay})$ makes it near-certain at a cost of $\$1000$. She refuses.

The paper extends this to a fallible predictor with error probability $\varepsilon$ of predicting payment wrongly. Refusing costs $\varepsilon\times\$1{,}000{,}000$ in expectation and paying costs $\$1000$, so the break-even is $\varepsilon=0.1\%$. The paper's $0.0009$ case refuses, as it should. Its second case, a "0.011%" error rate, is said to pay. By the stated payoffs, refusal would cost only $\$110$ in expectation, so the agent would still refuse. A $0.11\%$ error rate would flip the decision. I read the paper's figure as off by a factor of ten; this is my computation, not a claim in the source.

### XOR blackmail and Death in Damascus

In XOR blackmail, infestation is a root node. The fdt node influences whether a letter is sent and what Act does on receiving it, but not the infestation. Paying makes the letter "good news" evidentially, which is why EDT pays, but it cannot affect termites. A-FDT refuses.

In Death in Damascus, the book entry subjunctively depends on the agent's decision function, so wherever the function says to go, Death goes too. A-FDT compares $\$0$ (stay) with $-\$1000$ (flee) and stays. There is no instability, because the hypotheticals never imagine fleeing with Death left behind. CDT enters a loop precisely because its $do(\text{Act})$ holds Death's location fixed.

## 6. The asymmetric treatment of correlations

The paper's diagnosis: "EDT respects too many action-environment correlations, while CDT respects too few." A-FDT preserves exactly those correlations that arise because something computes (or models) the same function as the agent.

In the cosmic ray problem, statistical coincidence ties taking \$100 to hospital costs. A-FDT, like CDT, breaks that correlation. In Newcomb's problem, the correlation between act and prediction is not coincidence; A-FDT keeps it, and CDT breaks it.

## 7. An illustration of my own: imperfect twins

I add a case not in the paper to show how A-FDT handles graded dependence. Consider the twin prisoner's dilemma payoffs from the paper. The twin's output equals the agent's with probability $c$ and is otherwise the opposite. This models a twin that implements the agent's function with noise.

- $do(\mathrm{fdt}=\textit{cooperate})$: $EV=c\cdot 1{,}000{,}000+(1-c)\cdot 0$.
- $do(\mathrm{fdt}=\textit{defect})$: $EV=c\cdot 1000+(1-c)\cdot 1{,}001{,}000$.

Cooperation wins iff $c>1{,}001{,}000/2{,}000{,}000=0.5005$. The threshold is the point where the reliability of the dependence outweighs the temptation payoff.

Now suppose the "twin" merely shares her upbringing and a $90\%$ behavioral correlation with the agent, but does not compute her decision function or model it. There is then no edge from the fdt node to the twin's choice, and A-FDT defects, exactly as CDT does. EDT might still cooperate, conditioning on the correlation. This is the dependence-structure test applied to a case the paper does not discuss. It also shows why the structure of $G$ carries the weight: the answer depends on a modelling judgment about *why* the correlation holds, not on its strength.

## 8. Where the source leaves things open

**The graph $G$.** The paper gives no method for deducing it. Operationally, for human use, a defensible reading is: add an edge from the fdt node to a variable whenever (i) there is a process that computes the agent's decision function or contains a model of it, and (ii) that variable is a function of that process's output. Everything else is treated as upstream or exogenous. This is a heuristic of mine, consistent with the paper's examples. It is not a theorem.

**Counterpossible inference.** The paper brackets it, saying the method is not central. I treat it as the model's job: whatever supplies $G$ also supplies the conditional probabilities for downstream nodes given the intervened value.

**Beliefs about other-observation nodes.** In the transparent case, the parameter $q$ is the agent's credence in her own behavior under a different observation. The paper notes the correct $q$ and that the conclusion is robust. A cleaner alternative, which the paper's footnotes point toward but do not use in the main text, is to range over *policies* $\pi:\mathcal X\to\mathcal A$ and intervene on one node that outputs the whole policy. That removes $q$ entirely. I recommend it where observations matter, but it is an addition to Equation (4) as stated. The paper says the difference matters only in certain multi-agent dilemmas.

**Fairness.** The paper claims A-FDT does best in "fair" problems, where the outcome depends only on the agent's behavior (including predictions about it) and not on the agent's decision procedure as such. It acknowledges that the notion is not formalized. Its footnote 15 gives a copy of the agent that punishes agreement, which is unfair to A-FDT in a way that is hard to mirror for other theories. The claim of superiority is therefore a hypothesis, not a proved result.

**Dominance.** A-FDT has its own dominance principle ("holding constant all relevant subjunctive dependencies") and never takes a dominated action by that standard. The paper's point is that every hypothetical-building method generates its own dominance notion, so dominance cannot arbitrate between theories. It prefers to compare theories by utility achieved.

## 9. Philosophical motivation

The argument from utility is primary: agents following A-FDT do better on fair problems, and a correct theory should not recommend that people be shielded from it. Supporting arguments are:

- **Precommitment.** A-FDT acts as it would have precommitted to act, without the cost of binding mechanisms.
- **Value of information.** The theory does not assign negative value to information.
- **Reflective stability.** In fair problems, A-FDT has no desire to self-modify. CDT, by contrast, would modify itself to stop using CDT in future dilemmas.
- **The "delusion" charge.** The paper answers that if an A-FDT agent "controls" a function that is logically fixed, the deterministic CDT agent equally "controls" an act that is physically fixed. Both rely on imagined variation, so neither has a clean metaphysical advantage.

The global perspective: choose by asking "What would the entire universe look like if the FDT algorithm behaved differently?" and pick the action corresponding to the best imagined universe. That may mean imagining a universe where the box is empty although she sees it full, or where she was never blackmailed although she holds the letter.

## 10. Conclusion

A-FDT, as given by Equation (4), is an expected-utility rule that differs from CDT in two ways. It intervenes on a node for the output of the agent's decision function rather than on her physical act, and it handles observation by switching nodes rather than conditioning. Everything subjunctively dependent on that function moves with the intervention, and everything else is held fixed. This produces one-boxing in Newcomb's problem, smoking in the lesion problem, paying in Parfit's hitchhiker, refusing blackmail, and staying in Damascus, without ratification, tickle defenses, or precommitment.

The theory's power and its fragility lie in the same place: the graph $G$. The paper supplies no principled way to build it, and my twin example shows that the verdict can turn on whether a correlation reflects shared computation. The theory is a precise procedure given a dependence structure, and an open research program about where that structure comes from.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060). Primary source; see Section 5, Eq. (4).
- Joyce, J. *The Foundations of Causal Decision Theory* (1999).
- Pearl, J. *Causality* (2000).
- Gibbard, A., and Harper, W. "Counterfactuals and Two Kinds of Expected Utility" (1978).
- Soares, N., and Fallenstein, B. "Toward Idealized Decision Theory" (2015), source of the blackmail problems.