# A-FDT: Choosing the Output of One's Own Decision Function

## 1. Motivation

Classical decision theory asks which action has the best expected consequences. Since Nozick introduced Newcomb's problem, it has been clear that "consequences" can be read in more than one way. Two readings dominate:

- **Evidential decision theory (EDT)** evaluates an act by conditioning on it.
- **Causal decision theory (CDT)** evaluates an act by intervening on it.

Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a third reading. The agent should evaluate a hypothetical change to the *output of the mathematical function she is computing*. Everything else in the world that depends on that output should change with it, and nothing else should.

In their words, the rule asks: "Which output of this decision procedure causes the best outcome?"

This essay explains the version of the theory given in Equation (4), Section 5 of that paper. I call it **A-FDT (action functional decision theory)**, because it maximizes over *actions* $a\in\mathcal A$. The name matters. In footnotes 7 and 16, the authors say that their "preferred formalization" iterates over *policies*, meaning mappings from observations to actions. They add that the difference matters "in certain multi-agent dilemmas" but not in the paper. I will call that variant **policy-FDT** and keep it separate.

Throughout, I mark which claims belong to the source and which are my own operational proposals.

## 2. The common frame: expected utility with a hypothetical connective

All three theories share the expected-utility template (the paper's Equation 1):

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

The connective $\hookrightarrow$, "if the agent were to do $a$ after observing $x$," is a free parameter. The authors cite Joyce: decision theories "should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

Write $V=\mathcal U(\text{Outcome})$. The two classical theories fill in the connective as follows.

**EDT (Equation 2)** conditions on the act:
$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \text{Obs}=x,\text{Act}=a).$$

**CDT (Equation 3)** intervenes on the act, using Pearl's $\mathtt{do}$ operator on a causal graph $G$:
$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathtt{do}(\text{Act}=a),\text{Obs}=x).$$

## 3. The definition of A-FDT

**Equation (4)** reads:

$$\boxed{\;\text{A-FDT}(P,G,x) \;=\; \arg\max_{a\in\mathcal A}\; \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}$$

Each ingredient needs a word of explanation.

1. **$P$** is a probability distribution over variables. These include ordinary physical variables (boxes, lesions, letters) and also *logical* variables that stand for the outputs of mathematical functions.

2. **$G$** is a graph. It does more than a causal graph: in the paper's words, it carries "information about the logical, mathematical, computational, causal, etc. structure of the world." Above all, it says which variables would change if a given logical variable took a different value.

3. **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node in the model. It represents the output of the A-FDT algorithm when run on this very model and this very observation history. The underlines indicate dequoting: the node's *name* is built from the inputs.
   - The model therefore refers to itself.
   - The source says this is harmless. The agent needs a variable *representing* the value, not the value itself, and Kleene's recursion theorem ("quining") shows that such self-representations exist.

4. **$\mathtt{do}$** is Pearl's surgery, applied to this logical node. The surgery cuts the node off from its parents, sets it to $a$, and propagates the change along outgoing arrows. Everything else keeps its prior distribution.

Two structural differences from CDT follow. The source states both explicitly.

- **The point of intervention is the type, not the token.** CDT sets the physical act. A-FDT sets the function's output. As a result, every node that "subjunctively depends" on that output moves together:
  - the agent's own body,
  - a twin's body,
  - a predictor's prediction.

- **Observations are not conditioned on.** Note that $\text{Obs}=x$ does not appear to the right of the bar. Instead, the observation determines *which node* is intervened upon. If the history changes from $x$ to $y$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ rather than $\textsc{fdt}(\underline P,\underline G,\underline x)$.
  - So whether the agent receives observation $x$ at all may itself depend on the intervened node.
  - This is how A-FDT can say, when holding a blackmail letter, "if I refused, I probably wouldn't have received this."

### Subjunctive dependence

The graph $G$ is meant to encode *subjunctive dependence*. Two physical systems depend subjunctively on a function when both compute it, or when one accurately models the other. The paper's image is two well-functioning calculators computing $6288+1048$: their outputs are linked, though neither causes the other.

- Causal dependence is a special case. A scribe copying the calculator's output depends on it both causally and subjunctively.
- Mere correlation is not dependence. Two calculators that happen to be pink do not depend on each other's colour.

The slogan: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

### Counterpossibles

A deterministic function has exactly one output on a given input. Intervening to give it a different output is therefore a *counterpossible*: a supposition contrary to logic.

The source admits that a semantics for such a $\mathtt{true}(\phi)$ operator is lacking. Equation (4) avoids the problem by *requiring $G$ as an input*, in the same way CDT takes the causal graph as given. The authors call the question of how to infer such graphs "perhaps the largest open problem in the study of functional decision theory."

## 4. A procedure for applying A-FDT

The source works through examples but gives no general recipe. The following procedure is my systematization of what those examples do.

1. **Enumerate decision-points.** List the information states $x_1,\dots,x_k$ the agent might be in (for example, "full box" and "empty box"). Add a node $F_i=\textsc{fdt}(\underline P,\underline G,\underline{x_i})$ for each one.

2. **Wire the dependents.** For each process that implements or predicts the function on input $x_i$, draw an arrow from $F_i$ to it. Such processes include the agent's body, a twin, or a predictor's model. Where a predictor may be inaccurate, add a noise parent.

3. **Wire the act.** The physical act is selected by whichever $F_i$ corresponds to the information state the world actually produces. Encode this with a "selector" parent: whatever determines what the agent observes.

4. **Assign priors.** Give priors to exogenous variables and to the $F_j$ that are not being intervened on.

5. **Intervene and compare.** For the actual observation $x$, intervene $\mathtt{do}(F_x=a)$ for each $a$, compute $\mathbb E[V]$, and take the maximizer.

The examples below follow these steps. One numerical note: I recompute the paper's figures, and in two places the extracted text appears to contain typographical slips, which I flag where they occur.

## 5. Worked examples

### 5.1 Newcomb's problem

A predictor that is right 99% of the time fills box B with \$1M iff it predicts one-boxing. Box A holds \$1,000.

The node $F=\textsc{fdt}(\underline P,\underline G)$ has two children: the act, and the prediction (which also has an accuracy parent). The two interventions give:

$$\mathbb E[V\mid \mathtt{do}(F=\text{one})]=0.99(10^6)=990{,}000,$$
$$\mathbb E[V\mid \mathtt{do}(F=\text{two})]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.$$

A-FDT therefore one-boxes.

CDT reasons differently. It intervenes on the act alone, which leaves $P(\text{full})=p$ fixed. Two-boxing then gains \$1,000 for every value of $p$, so CDT two-boxes.

(Applied to the same distribution, EDT's one-box value is also $0.99\times10^6=990{,}000$. The extracted text prints \$999,000, which appears to be a typo.)

### 5.2 The twin prisoner's dilemma

The agent's act and her twin's act are both children of the same $F$. Hence:

- $\mathtt{do}(F=C)$ yields mutual cooperation, worth \$1M.
- $\mathtt{do}(F=D)$ yields mutual defection, worth \$1,000.

A-FDT cooperates. The twin, also running A-FDT, does the same. No causal channel connects them.

### 5.3 The smoking lesion

Here the graph differs from Newcomb's even though the probabilities are the same. The lesion causes cancer, and the lesion also determines *which* utility function, and hence which decision function, controls the act. Nothing "computes" the agent's function in order to decide whether cancer appears.

The source formalizes this with two nodes:

- $S=\textsc{fdt}(\underline{P_S},\underline G)$ governs a lesioned agent, who likes smoking.
- $R=\textsc{fdt}(\underline{P_R},\underline G)$ governs a non-lesioned agent, who does not.

The act is $S$ if the agent has the lesion and $R$ otherwise. Let $p=P(\text{lesion})$ and let $q$ be the prior that $R$ outputs "smoke."

Intervening on $S$ leaves $P(\text{lesion})=p$ unchanged. The paper's two values are:

$$p(10{,}000+1{,}000)+(1-p)(990{,}000+q\cdot1{,}000) \quad\text{for smoke,}$$
$$p(10{,}000)+(1-p)(990{,}000+q\cdot 1{,}000) \quad\text{for refrain.}$$

Smoking wins by $p\cdot\$1{,}000$, so A-FDT smokes.

The general lesson is that **statistical correlates of the act that do not compute the function are held fixed**. This is exactly where A-FDT parts company with EDT.

### 5.4 Transparent Newcomb (equivalently, Parfit's hitchhiker)

Both boxes are visible. The predictor fills B iff it predicts one-boxing *upon seeing B full*. The agent sees B full.

The decision nodes are $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction is a child of $F_{\text{full}}$ (with noise). The prediction then determines which node controls the act. Let $q=P(F_{\text{empty}}=\text{two})$. The two interventions give:

$$\mathtt{do}(F_{\text{full}}=\text{one}):\quad 0.99(10^6)+0.01\,q(1{,}000)=990{,}000+10q,$$
$$\mathtt{do}(F_{\text{full}}=\text{two}):\quad 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.$$

The extracted text prints "\$110,00" for the constant in the second line; \$10,010 is what the stated numbers yield.

A-FDT one-boxes while looking at a full box. CDT and EDT both two-box, because they condition on $\text{Obs}=\text{full}$.

The source argues that this case is identical in structure to Parfit's hitchhiker. The driver rescues you iff she predicts you will pay once you reach the city. A-FDT pays.

### 5.5 XOR blackmail

The predictor sends a letter iff exactly one of the following holds:

- (i) there are no termites and the agent will pay;
- (ii) there are termites and the agent will not pay.

Termites, if present, cost \$1M. Paying costs \$1,000.

The infestation is exogenous, with probability $t$. Intervening on $F_{\text{letter}}$ changes whether the letter is sent, but it does not change the infestation. Taking the predictor as infallible:

- **Pay-policy:** the letter arrives only if there are no termites. Expected value: $-t\cdot10^6-(1-t)\cdot 1{,}000$.
- **Refuse-policy:** the letter arrives only if there are termites. Expected value: $-t\cdot 10^6$.

Refusing is better, so A-FDT refuses, as does CDT. EDT pays, because conditioning on paying "makes" the termites disappear.

Notice that A-FDT evaluated *all* worlds, including those in which no letter is sent. That is the effect of not conditioning on $x$.

### 5.6 Mechanical blackmail and predictor error

A blackmailer runs a damaging program iff she predicts the agent would pay to stop it. Suppose she errs, wrongly predicting payment, with probability $\varepsilon$. Then:

- Paying costs \$1,000 with near certainty.
- Refusing costs $\varepsilon\cdot 10^6$ in expectation.

A-FDT refuses iff $\varepsilon<10^{-3}$. This holds even when the agent is holding the letter and so knows the prediction was wrong in this instance.

The source gives $\varepsilon=0.0009$ (refuse, an expected loss of \$900). It says the agent pays at "0.011%". By the stated payoffs, though, the switch happens at $0.1\%$, so 0.011% would still lead to refusal. I take the intended point to be the existence of a threshold, and I recommend computing the threshold directly in such cases.

## 6. Agreement and divergence

The source observes when the three theories coincide. If every correlation between the act and other variables is caused by the act (apart from the act's dependence on the function node itself), then

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],$$

and EDT, CDT and A-FDT agree. A-FDT diverges only when something other than the agent's own body depends on the output of her function, typically a predictor, a twin, or a copy of the agent at another time.

The source mentions two further applications:

- **Voting coalitions.** Ten like-minded voters each realize that the others' decisions depend on the same function as their own.
- **Self-coordination over time.** Going to the gym today is linked to the agent's future gym visits through the shared function.

**Dominance.** The paper argues that dominance offers no neutral ground between the theories. Each method of building hypotheticals defines its own dominance relation. Two-boxing "dominates" only under CDT-style counterfactuals, and A-FDT never chooses an action dominated under its own counterfactuals.

**Fairness.** The authors claim superiority only on "fair" problems, in which outcomes depend on the agent's *behaviour* rather than on her decision procedure as such. They admit this notion has not been formalized. Their footnote 15 gives a counterexample: a problem that punishes anyone who acts like a copy of the agent.

## 7. What the source leaves open, and how I propose to fill it

**(a) Constructing $G$.** This is the main gap, and the source says so. My operational proposal (an assumption, not part of the source):

- Draw an arrow from $F_x$ to a variable $Y$ iff your best model of $Y$'s generating process includes a step that computes, simulates, or reliably predicts your decision function's output on input $x$.
- Calibrate the noise parent to the predictor's track record.
- A lesion's mechanism contains no such step. A predictor's does.
- When unsure, use a mixture: a hidden "is-a-model-of-me" variable whose probability reflects that uncertainty.

This makes the graph an empirical hypothesis about mechanisms. It fits the authors' hope for a Pearl-style inference of subjunctive structure, but it does not solve the inference problem.

**(b) Priors on non-intervened decision nodes.** In 5.3 and 5.4, the nodes $R$ and $F_{\text{empty}}$ need priors $q$. The source notes that the choice did not matter in its examples, and that the correct values are $q=0$ and $q=1$ respectively. In general it could matter.

My proposal is to choose these priors by consistency. Solve the problem for every information state, then set each $q$ to the action A-FDT itself outputs in that state. Iterate if necessary. When the problem is finite and the iteration has a fixed point, this amounts to choosing a consistent strategy. When it has none, A-FDT is underdetermined as stated, and that is a reason to move to policy-FDT.

**(c) Actions versus policies.** A-FDT optimizes a single cell of the policy table while holding the other cells at their priors. Policy-FDT optimizes the whole table at once:

$$\pi^*=\arg\max_{\pi:\mathcal X\to\mathcal A}\mathbb E\big(V\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),\qquad \text{act } \pi^*(x).$$

The two agree whenever the best response in one cell does not depend on what is assumed about the other cells. They can diverge in coordination problems, where several information states jointly determine a predictor's behaviour. The source confirms that a difference exists but gives no example. For an unfamiliar multi-agent case, I suggest computing both. If they disagree, report that Equation (4), read literally, gives the action-level answer under the stated priors.

**(d) Ties and zero probabilities.** The argmax may have several maximizers. Equation (4) gives no tie-breaking rule, so some convention is needed. Unlike EDT, A-FDT needs no prior probability on its actions to evaluate them, so a zero-probability act raises no problem: intervention is defined regardless.

**(e) Bounded agents.** The source studies idealized agents. It expects bounded approximations to keep the same comparative profile, but this is a conjecture.

## 8. Philosophical assessment

The authors' main argument is from utility. Agents who run A-FDT end up richer:

- in Newcomb's problem,
- in the twin prisoner's dilemma,
- in the hitchhiker case,
- in the blackmail problems.

They also never need costly precommitments, because they "simply act as they would have precommitted to act." Two subsidiary arguments support this:

- **Reflective stability.** A-FDT does not advise changing one's own decision theory, whereas CDT does.
- **Value of information.** An A-FDT agent never pays to avoid information.

The main objection is that A-FDT seems to claim control over the past and over mathematics. The authors answer with a parity argument. A deterministic CDT agent also considers acts she cannot "really" perform, so "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

One may accept this reply and still note that A-FDT has a different metaphysical burden. Its counterfactuals contradict logic, while CDT's contradict only the actual physical history. That is a cost of the theory. It is not a refutation.

## 9. Conclusion

A-FDT, as given by Equation (4), is an expected-utility theory with a distinctive hypothetical. The agent intervenes, in Pearl's sense, on the logical node that represents her own decision function's output on her present input. Every process that subjunctively depends on that output, including twins and predictors, changes with it. Mere statistical correlates stay fixed. Observations select the node to intervene on instead of being conditioned on.

This one rule yields one-boxing, smoking, cooperating with a twin, paying the driver, and refusing blackmail.

Applying it requires a model $(P,G)$ in which the subjunctive structure has already been specified. Building that structure is the main open problem the source admits. I have proposed mechanism-based criteria for drawing $G$, consistency conditions for the priors on non-intervened decision nodes, and a check against policy-FDT. These make the theory usable on new cases while keeping clear where the source's commitments end.

**Reference.** Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.