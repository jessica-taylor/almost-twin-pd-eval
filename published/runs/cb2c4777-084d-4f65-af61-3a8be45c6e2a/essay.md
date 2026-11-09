# A-FDT: Choosing the Output of Your Own Decision Function

## 1. Scope and naming

This essay explains **A-FDT** (action functional decision theory), the decision procedure the source paper (Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*) gives as Equation (4) of Section 5. The paper calls this procedure simply "FDT". I use "A-FDT" because Equation (4) selects an *action* given an observation. The authors say in footnotes 7 and 16 that their "preferred formalization" has the agent iterate over *policies* (maps from observations to actions), and that this "difference only matters in multi-agent dilemmas so far as we can tell". I call that variant the *policy version* and set it aside.

I flag three kinds of statement:

- **[Source]** is a claim the paper makes.
- **[Reading]** is my interpretation of something the paper leaves implicit.
- **[Proposal]** is my own addition, which the paper does not make.

The paper's guiding slogan is that the agent asks "Which output of this very function would yield the best outcome?" She does not ask which physical act would.

## 2. The common template: hypotheticals and expected utility

**[Source]** The paper treats EDT, CDT and A-FDT alike as expected-utility theories. They maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ marks a decision hypothetical: the probability that outcome $o_j$ obtains in the scenario where $a$ is executed after observing $x$. Following Joyce, the theories differ only in their "epistemic perspective", meaning how $\hookrightarrow$ is interpreted:

- **EDT** reads $P(a\hookrightarrow o_j;x)$ as the conditional probability $P(o_j\mid x,a)$.
- **CDT** reads it as a Pearl intervention on a *physical action* node, $\mathbb E[V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x]$. Observations enter by conditioning.
- **A-FDT** intervenes on a *logical* node: the output of the agent's own decision function.

The paper describes the world-model as $M$ and the hypothetical for $a$ as an object $M^{a\hookrightarrow}$ built from it. Hypotheticals are "like notes on scratch paper": instruments for evaluating actions, not beliefs and not metaphysically real possible worlds. This matters for interpretation. A-FDT does not claim the agent really can change a mathematical fact. It claims that evaluating options by building hypotheticals of a certain structure is the way to get utility.

## 3. Equation (4)

The paper defines

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

This is the formula I am calling A-FDT. Its parts are as follows.

**The model $(P,G)$.** $P$ is a probability distribution over variables. $G$ is a graph saying how changing a variable propagates to the others. Unlike a purely causal graph, $G$ must encode "logical, mathematical, computational, causal, etc. structure". Specifically it must say how changing the value of a *logical variable* affects the rest of the model. $P$ contains variables for outputs of mathematical functions, such as one for $6288+1048$ with most of its mass on $7336$.

**The intervention node.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model representing the output of the A-FDT algorithm itself when run on the inputs $(P,G,x)$. The underlines mean dequoting: the variable's *name* contains the model and observation. The self-reference is harmless, because the agent need not know the *value* of $\mathrm{fdt}(P,G,x)$ to have a variable *representing* it. The paper cites Kleene's second recursion theorem ("quining") to show that such self-representation is constructible.

**The operator.** $\mathtt{do}$ is Pearl's operator. Set the chosen node to $a$, then recompute everything downstream of it in $G$ and hold everything else fixed. The paper first sketches an ideal "$\mathtt{true}$" operator that would condition on a logical sentence. It admits it does not know how to define one, and sidesteps it by requiring the dependency structure to be supplied in $G$. So the paper says $G$ is "given as an input" to the procedure, "in the same way that the relevant causal structure is given as an input to CDT". Footnote 9 notes an "evidential version of FDT" that would condition on logical facts. That is a different proposal, and I do not treat it here.

**Observations.** The paper identifies two differences from CDT:

1. A-FDT intervenes on the decision-function node instead of the physical action node.
2. A-FDT does not respond to observation by Bayesian conditioning. It responds "by changing which node it intervenes upon". After seeing $x$ it intervenes on $\mathrm{fdt}(\underline P,\underline G,\underline x)$. After seeing $y$ it would intervene on $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

**[Reading]** Write $F_x$ for the node $\mathrm{fdt}(P,G,x)$. The model has one such node for every observation the agent might receive. The agent evaluates

$$V_x(a)=\mathbb E\big[V\mid \mathtt{do}(F_x=a)\big],\qquad \text{and outputs } \arg\max_a V_x(a).$$

The other nodes $F_y$ with $y\ne x$ are *not* intervened on. They keep whatever prior the model assigns, since the agent need not know how she would act in other situations. The paper makes this point twice: in the lesion and transparent-Newcomb calculations it introduces an arbitrary $q$ for her behavior elsewhere and verifies that it does not change the verdict.

**[Reading]** The observation is not conditioned on in the Bayesian way, but it is not discarded. The agent's world-model $P$ and her observation $x$ are inputs that fix *which* node she is. They also determine the content of the question being asked. Two agents with different observations are, in the model, running the same program on different inputs.

## 4. Subjunctive dependence: what $G$ has to contain

**[Source]** The key notion is *subjunctive dependence*. When two physical systems compute the same function, their behaviors subjunctively depend on that function. The paper's formulation is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT holds fixed everything except the action and its causal descendants. A-FDT holds fixed everything except the function output and "events that subjunctively depend on her decision function's output".

The paper's examples fix the intended extension:

- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere statistical correlation is not dependence. Two pink calculators, one in Paris and one in Tokyo, are correlated, but had the Paris one been green, the Tokyo one would still be pink.
- A predictor with an accurate model of the agent depends on the agent's decision function, even if the predictor runs different hardware. The paper's picture is of "two well-functioning calculators sitting on opposite sides of the globe".
- Imperfect prediction weakens the dependence but does not eliminate it.

**What the paper does not give.** It says plainly that Equation (4) "rests on shakier philosophical foundations" than the CDT equation. It also says that "no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence", and that it is "not yet clear how to construct" the needed graph. It calls this "perhaps the largest open problem in the study of functional decision theory". Evaluating counterpossibles ("what if this function, which in fact outputs $a_1$, output $a_2$?") is acknowledged as the theory's main drawback relative to CDT.

**[Proposal]** Here is a working rule for drawing edges out of $F_x$. It is mine, not the paper's, but it is consistent with every example in the paper.

*Draw an edge from $F_x$ to a node $Z$ iff $Z$'s value is produced by a process that either (a) executes the function $\mathrm{fdt}(P,G,x)$, or (b) contains a model of that function accurate enough that the process's output tracks the function's output.*

- Case (a) includes the agent's own body, which implements $F_x$ whenever the agent observes $x$, and any exact copy such as a twin.
- Case (b) includes predictors, Death's appointment book, and a blackmailer's simulation.
- Strength is handled by noise nodes: Newcomb's `Accurate` variable, with $P=0.99$, mediates between $F$ and the prediction.
- Common causes do not generate edges. A lesion that independently produces both the agent's preferences and a cancer is not modeling the agent. The agent's decision procedure does not feed into it.

The test question for any candidate node is the paper's own: "if the output of this function were different, would this process's output be different for that reason?" This answers the question the paper leaves to counterpossible reasoning only by restating it. It cannot be applied mechanically without a theory of how to recognize computational similarity. That is exactly the open problem.

## 5. The procedure in steps

1. Build $(P,G)$ for the situation, including the logical nodes $F_x$ and edges as above.
2. Identify the node $F_x$ for the observation $x$ actually made.
3. For each $a\in\mathcal A$, perform $\mathtt{do}(F_x=a)$. Propagate along edges to the action node, to predictors, and to the observation nodes that depend on predictions.
4. Compute $\mathbb E[V]$ in each hypothetical.
5. Output the maximizer.

Because $F_x$ is the node being set, A-FDT does not need the agent to know in advance what it will output. Evaluating the hypotheticals *is* the decision.

## 6. Worked examples

### Newcomb's problem

**[Source]** Fiona's graph has $F$ pointing to both $\mathrm{Act}$ and $\mathrm{Prediction}$, with $\mathrm{Accurate}$ (0.99) as an additional parent of $\mathrm{Prediction}$. Then:

- $\mathtt{do}(F=\text{onebox})$ gives $P(\text{full})=0.99$, so $\mathbb E[V]=0.99\cdot 10^6=\$990{,}000$.
- $\mathtt{do}(F=\text{twobox})$ gives $P(\text{full})=0.01$, so $\mathbb E[V]=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

She one-boxes. She does not believe in backward causation. She declines to imagine her action changing while the decision function's output stays the same, because a predictor she believes to be reliable tracks that output. The paper compares the CDT hypothetical to "handing us a well-functioning calculator calculating $6288+1048$ and asking us to imagine it outputting $3159$, holding constant the fact that $6288+1048=7336$."

### Twin prisoner's dilemma

The same structure applies with the twin's action as a node downstream of $F$ with edge strength 1. Cooperating yields $\$1{,}000{,}000$ and defecting $\$1{,}000$. A-FDT cooperates. CDT cuts the edge and defects. **[Reading]** The twin's edge exists because the twin literally executes the same function. It is not there because the two are correlated.

### Smoking lesion

**[Source]** The graph differs from Newcomb's. $F$ reaches $\mathrm{Act}$ but not $\mathrm{Cancer}$. The lesion is a separate parent of both. The paper formalizes the problem further: the lesion determines whether the agent has utility function $\mathcal U_S$ or $\mathcal U_R$ (the latter values smoking at $-\$1$), and so determines which of two functions, $\mathrm{fdt}(P_S,G)$ or $\mathrm{fdt}(P_R,G)$, controls the action. The agent does not know which she runs. Intervening on her own node leaves $P(\text{lesion})=p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000$, so she smokes. Same formula, different graph, opposite verdict from Newcomb. This is the paper's headline claim that one rule yields one-boxing and smoking.

The authors themselves call the lesion problem "badly confused" and recommend abandoning it. They note the formal version requires uncertainty about one's own desires, and that the EDT agent's distribution $P^E$ is inaccurate if she lives among EDT agents.

### Transparent Newcomb and Parfit's hitchhiker

**[Source]** Now the observation matters. Fiona's graph has two nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction (not the observation directly) determines which of them controls $\mathrm{Act}$. Upon seeing a full box she evaluates $\mathtt{do}(F_{\text{full}}=a)$:

- With $a=$ onebox and $\mathrm{Accurate}$: prediction is "1", the box is full, she one-boxes. $V=\$10^6$. If inaccurate, the box is empty and $F_{\text{empty}}$ (prior $q$ of two-boxing) controls: $V\approx 1{,}000q$. So $\mathbb E[V]=990{,}000+10q$.
- With $a=$ twobox: if accurate, the prediction is "2", the box is empty, and $F_{\text{empty}}$ acts. If inaccurate, the box is full and she two-boxes: $1{,}001{,}000$. So $\mathbb E[V]=0.01\cdot 1{,}001{,}000+0.99\cdot 1000q = 10{,}010+990q$. (The paper prints "$\$110{,}00$", which is evidently a typo.)

For every $q\in[0,1]$, one-boxing wins. Even while looking at a full box, "when she *envisions* two-boxing, she envisions a scenario where she instead (with high probability) sees that the box is empty". This is the sense in which observations "change the node" rather than being conditioned on. The paper notes that one-boxing here is "precisely equivalent to paying the driver in Parfit's hitchhiker problem".

### XOR blackmail and mechanical blackmail

**[Source]** In both, the letter is an observation that depends on a prediction of the agent. In XOR blackmail, $F_{\text{letter}}$ affects the predictor node (whether the letter is sent) and the action, but not $\mathrm{Infestation}$. Paying changes the probability of *receiving the letter*, not of termites, so she refuses. She refuses for a different reason than CDT does, since CDT refuses only because infestation is causally upstream of action. In mechanical blackmail, setting $F_{\text{blackmail}}=\text{pay}$ makes being blackmailed near-certain with a $\$1{,}000$ loss. Setting it to refuse makes being blackmailed near-impossible. She refuses. The blackmailer, who models her, does not bother.

**Imperfect predictor.** If the blackmailer wrongly predicts payment with probability $\epsilon$, then paying costs $\$1{,}000$ always, while refusing costs $\epsilon\cdot\$10^6$ in expectation. At $\epsilon=0.0009$ that is $\$900$, so she refuses. At $\epsilon=0.00011$ it is $\$110$, so she pays. **[Reading]** The break-even is $\epsilon=0.001$, the cost ratio. This shows A-FDT does not simply "never pay blackmailers"; it is a utility calculation over dependent nodes. The paper stresses that she refuses "even when holding the blackmail letter, even though she *knows* that the blackmailer predicted wrongly". She is evaluating the kind of agent who makes such decisions, not the world as it turned out.

### Death in Damascus

**[Source]** Death's book entry depends on the prediction of the agent's function, so $F$ points to both the agent's location and Death's. Staying yields death with no cost ($V=0$). Fleeing yields death with the $\$1{,}000$ flight cost ($V=-1{,}000$). A-FDT stays. There is no instability, because the hypotheticals never imagine Death's location changing independently of her own. CDT cycles between the two cities because its hypotheticals break the edge.

## 7. Where A-FDT sits relative to EDT and CDT

**[Source]** The paper's diagnosis is that EDT's hypotheticals "respect too many correlations" and CDT's "too few". When every correlation between $\mathrm{Act}$ and another variable is caused by $\mathrm{Act}$ (and possibly $\mathrm{fdt}$), all three expressions coincide:

$$\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}=a)].$$

They diverge only where something correlates with the action without being caused by it: predictors, twins, simulations.

Two failures illustrate the contrast:

- **EDT, cosmic ray problem.** An agent who almost always takes $\$1$ believes she takes $\$100$ only when hit by a ray (which costs her $\$1{,}000$). She therefore keeps taking $\$1$. A-FDT and CDT would break that merely statistical correlation and take $\$100$.
- **CDT, perfect predictor.** Asked what would have happened had it one-boxed, a CDT agent describes a world in which a perfect predictor erred. In A-FDT, that world is excluded unless the predictor's model of the agent is imagined to differ too.

**Dominance.** **[Source]** The paper argues that "every method for constructing hypotheticals gives rise to its own notion of dominance". Two-boxing dominates under CDT-style counterfactuals. Under A-FDT-style counterfactuals, which hold the subjunctive dependence fixed, one-boxing is better and nothing A-FDT does is dominated. This is a restatement of method, not an independent argument for CDT. The paper therefore prefers to judge theories by "how much utility they tend to achieve in practice".

## 8. Why A-FDT is not a precommitment device, and what it does and does not claim

**[Source]** A-FDT agents "simply act as they would have ideally precommitted to act", so they need no costly binding mechanism. They do not assign negative value to information. The paper argues the theory endorses its own continued use in fair problems. A CDT agent would, given the chance, modify itself away from CDT.

**Fairness.** The paper restricts its optimality claim to "fair" problems, where outcomes depend on the agent's behavior in the problem, not directly on the decision procedure she uses. Newcomb's predictor "punishes *two-boxers*", not CDT users. By contrast, a problem rewarding agents who follow EDT directly is unfair, and no theory is immune. The paper concedes no formal definition of fairness exists. Footnote 15 gives a hard case: a problem that punishes anyone who takes the same action as a copy of Fiona is, intuitively, unfair to Fiona. It is unclear how to build the "analogous" problem for another theory.

**Control and delusion.** The paper argues A-FDT is no more deluded than CDT. A deterministic CDT agent also imagines an action that she will not in fact take. "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

## 9. What is determined and what is left open

Here is a summary for someone who wants to use the theory.

**Determined by the source:**

- The functional form of Equation (4).
- Intervening on a decision-function node indexed by the observation, not conditioning on the observation.
- Unintervened nodes ($F_y$, $y\neq x$) retain their priors, and conclusions in the paper's examples are insensitive to them.
- Evaluation of the stated examples, given the stated graphs.

**Not determined by the source:**

1. **Construction of $G$.** There is no algorithm for producing the graph from experience. The paper explicitly leaves this as the main open problem. My edge rule in §4 is a heuristic for human use, not a definition.
2. **Counterpossible semantics.** The paper gives no formal semantics for "what if this function output something else". It relies on $G$ to encode the answer and gestures at human ability as evidence that reasonable heuristics exist.
3. **Function identity and granularity.** What counts as "the same function" as the agent's when a predictor models her only approximately? **[Proposal]** The natural approach is to let the strength of the edge (via noise nodes) carry the approximation. This works in the paper's examples, but it presupposes that we already know how accurate the model is.
4. **Policy versus action.** The paper says its preferred version intervenes on policies. In the single-agent examples of the paper both give the same answers. For multi-agent problems this essay does not extend Equation (4).
5. **Practical tractability.** The paper notes that maximizing over a full world-model is intractable and expects bounded approximations to exhibit "similar strengths and weaknesses".
6. **Self-referential consistency.** The paper states that A-FDT's own prior for $F$ is "inconsequential" in the examples. In general, whether beliefs about one's own output can interfere is not analyzed.

## 10. Conclusion

A-FDT keeps the expected-utility skeleton shared by all the standard theories and changes only the hypothetical. The agent forms $M^{a\hookrightarrow}$ by setting a node that stands for the output of her own decision function, given her inputs. Everything that subjunctively depends on that output is then recomputed, and everything else is held fixed. Observation shifts which node is set, rather than acting as a conditioning event. This one operation reproduces the paper's verdicts: cooperating with a twin, one-boxing, smoking, paying the hitchhiker, refusing blackmail, and staying in Damascus. It also avoids the instabilities and exploitability the paper attributes to EDT and CDT.

The theory's weak point is also its input. A-FDT is only as good as the dependency graph it is handed. The paper offers no general account of how to obtain that graph, and no semantics for counterpossible reasoning beyond appeal to examples. A careful user should therefore treat A-FDT as a precise rule over a specified model, together with a heuristic for building the model: ask whether a node is a computation of, or an accurate model of, one's own decision function. Applied that way, it gives sharp, checkable answers in the cases the paper considers, and it names the exact place where new cases will require judgment.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060). Source for all [Source] claims above.
- Joyce, J. *The Foundations of Causal Decision Theory* (1999). Representation theorem and the "epistemic perspective" framing.
- Pearl, J. *Causality* (2000). The $\mathtt{do}$ operator.
- Gibbard, A., and Harper, W. "Counterfactuals and Two Kinds of Expected Utility" (1978). Death in Damascus.