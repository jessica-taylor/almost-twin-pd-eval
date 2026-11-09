# Policy Functional Decision Theory (P-FDT): Choosing What to Do at Every Input at Once

## 1. The source and what it actually says

Yudkowsky and Soares's paper *Functional Decision Theory* (FDT) formalizes a decision rule in which the agent does not ask "which physical act of mine causes the best outcome?" but "which output of *this very decision function* yields the best outcome?" The paper's official equation intervenes on a node representing the output of the FDT function on the agent's current inputs. Twice, in footnotes, the authors say this is not their preferred formulation. Footnote 7:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which this essay takes as its primary source, says:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the theory these footnotes describe **policy functional decision theory (P-FDT)**. The footnote fixes three things:

1. the object of choice is a *policy*, a map from inputs to actions;
2. the choice is made by *intervening on the node $\mathrm{FDT}(-)$*, where the dash suggests the function itself rather than its value at a particular input;
3. the agent then *applies her inputs* to the chosen policy.

It leaves open how observations enter the expectation, which probability model is used, how ties and unreachable inputs are handled, whether policies may randomize, and exactly which "multi-agent dilemmas" make the difference. Below I separate the source's claims from my own reconstructions. My additions are marked as **Proposal** or **Interpretation**.

## 2. Background: the action-level formulation (FDT)

The paper writes every expected-utility theory in the form "choose $a$ maximizing $\mathbb E[V]$ in the hypothetical for $a$." The theories differ only in how the hypothetical is built. Evidential decision theory (EDT) conditions on the act. Causal decision theory (CDT) performs a Pearl intervention $\mathtt{do}(\textsc{Act}=a)$ on a causal graph:

$$\mathrm{CDT}(P,G,x)=\arg\max_{a}\ \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big).$$

FDT also uses $\mathtt{do}$. Its graph $G$, however, encodes *subjunctive* dependence: "logical, mathematical, computational, causal, etc." structure. The intervention is on a variable standing for the output of the FDT algorithm itself (the source's Equation 4):

$$\mathrm{FDT}(P,G,x)=\arg\max_{a}\ \mathbb E\big(V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

Two features matter for what follows.

- **The intervention node is indexed by the observation $x$.** The source says that "FDT responds to observation by changing which node it intervenes upon," rather than by conditioning on $\textsc{Obs}=x$.
- **No conditioning on $x$.** This is deliberate. The source calls the alternative of both conditioning *and* moving the intervention point a harmful "double update" and attributes it to Timeless Decision Theory.

So FDT has one node per possible input: $\textsc{fdt}(\underline P,\underline G,x_1)$, $\textsc{fdt}(\underline P,\underline G,x_2)$, and so on. When deciding at input $x$, it sets one of these nodes and leaves the others distributed as $P$ says.

## 3. Defining P-FDT

### 3.1 The policy node

Let $\mathcal X$ be the set of possible inputs (observation histories) and $\mathcal A$ the finite action set. The policy space is

$$\Pi=\mathcal A^{\mathcal X}=\{\pi:\mathcal X\to\mathcal A\}.$$

**Interpretation.** I read "the node $\mathrm{FDT}(-)$" as a single variable $\Phi:=\textsc{fdt}(\underline P,\underline G,-)$ taking values in $\Pi$. It represents *which function from inputs to actions the P-FDT algorithm computes, given model $(P,G)$*. The per-input nodes of Section 2 become coordinates of it:

$$\Phi_x := \Phi(x) \quad\text{for each } x\in\mathcal X.$$

In the graph $G$:

- the agent's physical action has the structural equation $\textsc{Act}=\Phi(\textsc{Obs})$;
- a predictor who simulates the agent on input $y$ has a node depending on $\Phi(y)$;
- a twin who receives input $z$ acts according to $\Phi(z)$;
- lesion-like variables that merely correlate with the agent's behaviour have no arrow from $\Phi$.

All the substantive judgments about subjunctive dependence live in $G$, exactly as in the source.

### 3.2 The rule

Define the value of a policy and the chosen policy by

$$U(\pi):=\mathbb E\big(V \mid \mathtt{do}(\Phi=\pi)\big), \qquad \pi^\star\in\arg\max_{\pi\in\Pi} U(\pi),$$

and the prescribed action by

$$\boxed{\ \mathrm{P\text{-}FDT}(P,G,x):=\pi^\star(x)\ }$$

This is the footnote's two-step structure. First choose a policy by intervening on $\mathrm{FDT}(-)$. Then "apply her inputs in order to select an action."

### 3.3 What the definition implies

- **The maximization does not mention $x$.** Read literally, P-FDT computes the same $\pi^\star$ whatever it observes, and $x$ is used only at the application step. This is the source's "no conditioning" stance taken to its limit. Action-level FDT already refuses to condition on $x$. P-FDT also refuses to let $x$ choose *which* node gets intervened on: it intervenes on all of them jointly.
- **Behaviour is ex-ante optimal.** The agent acts exactly as she would have bound herself to act had she been able to commit, before seeing anything, to a complete contingency plan. This is the source's "argument from precommitment" built into the definition. FDT agents "simply act as they would have ideally precommitted to act."
- **Self-reference is handled as in the source.** The model contains a variable representing its own decision procedure, which the source says is harmless via quining (Kleene's recursion theorem). The agent need not know the value of $\Phi$ in order to intervene on it.
- **Counterpossibles are inherited.** In reality $\Phi$ has exactly one value, so $\mathtt{do}(\Phi=\pi)$ for other $\pi$ is a counterpossible supposition. P-FDT inherits the source's main open problem: how to obtain a graph $G$ that says how the world would differ if a mathematical function had a different output. Like the source, I take $G$ as given.

## 4. Unresolved choices and how I propose to settle them

### 4.1 Should the expectation condition on $x$?

One could define a variant P-FDT$_{c}$ that maximizes $\mathbb E(V\mid \mathtt{do}(\Phi=\pi),\textsc{Obs}=x)$. I reject this. Conditioning on what one sees, while also choosing the response to what one sees, reintroduces exactly the double-counting the source criticizes.

In the transparent Newcomb problem, conditioning on "box B is full" makes the full box look fixed. Any policy that two-boxes on seeing it full then looks $\$1{,}000$ better, so P-FDT$_c$ two-boxes and is predicted to. The unconditioned rule of 3.2 is the reading consistent with Equation 4 and with the footnote's phrase "applies her inputs" *after* choosing.

### 4.2 Which $P$?

The footnote doesn't say. If $P$ already incorporates observations that the policy is meant to respond to, they are double-counted again.

**Proposal.** $P$ should be the agent's model *of the decision problem as a whole*, prior to the observations in $\mathcal X$ that the policy maps from. Information acquired before the problem begins (background knowledge, problem description) lives in $P$. Information acquired within the problem is an input to $\pi$. The cut is a modelling choice, as choosing the graph is for CDT. Where it falls determines how "updateless" the agent is.

### 4.3 Ties and unreachable inputs

The argmax may contain several policies that disagree at the agent's actual input. The worst case is an input $x$ that has probability zero under every optimal policy. Then $U$ is insensitive to $\pi(x)$, and the rule gives no guidance at exactly the moment the agent faces $x$.

**Proposal (trembling refinement).** Let $P_\varepsilon$ be the model in which every predictor and every implementation of $\Phi$ errs independently with small probability $\varepsilon$. Define $\pi^\star$ as a limit point, as $\varepsilon\to0$, of optimal policies under $P_\varepsilon$. Every input then has positive probability, so every coordinate of the policy is disciplined.

Any remaining ties should be broken by a fixed canonical ordering on $\mathcal A$. A fixed rule matters because copies of the agent must break ties *identically* to coordinate.

### 4.4 Randomized policies

The footnote speaks of maps "from inputs to actions," so deterministic policies are the default. One may extend $\Pi$ to $\Delta(\mathcal A)^{\mathcal X}$. Whether randomization helps depends on what $G$ says predictors depend on: the policy, which includes the mixing probabilities, or the realized action.

In Death in Damascus with a truly random coin that Death cannot foresee, a mixed policy gets survival probability $\tfrac12$. The source treats such a coin as obviously worth $\$1$. I regard mixed policies as a natural extension, but not part of what the footnote asserts.

## 5. Worked examples

All numbers are in the source's dollar-utilities.

### 5.1 Newcomb's problem

There are no inputs, so $|\mathcal X|=1$ and policies are just actions. P-FDT coincides with FDT:

$$U(\text{onebox})=0.99\cdot 10^6=990{,}000,\qquad U(\text{twobox})=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=11{,}000.$$

P-FDT one-boxes.

### 5.2 Transparent Newcomb

The setup:

- inputs are $\mathcal X=\{\text{full},\text{empty}\}$;
- a policy is a pair $(f,e)$ giving the number of boxes taken on seeing each input;
- the predictor fills box B iff she predicts $f=1$, and she is accurate with probability $0.99$.

Writing $u(e)\in\{0,1{,}000\}$ for the payoff from an empty box:

| policy $(f,e)$ | $U$ |
|---|---|
| $(1,1)$ | $0.99\cdot 10^6+0.01\cdot 0 = 990{,}000$ |
| $(1,2)$ | $0.99\cdot 10^6+0.01\cdot 1{,}000=990{,}010$ |
| $(2,1)$ | $0.01\cdot 1{,}001{,}000+0.99\cdot 0=10{,}010$ |
| $(2,2)$ | $0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=11{,}000$ |

So $\pi^\star=(1,2)$: one-box on seeing full, two-box on seeing empty. This matches the source's FDT verdict. P-FDT also delivers the off-path behaviour explicitly instead of leaving it as an unknown $q$.

With a *perfect* predictor, $(1,1)$ and $(1,2)$ tie at $10^6$, because "empty" never occurs under $f=1$. The trembling refinement of 4.3 selects $(1,2)$.

### 5.3 Parfit's hitchhiker

The setup:

- the input is "in the city";
- the driver rescues the agent iff she predicts (99% accurately) that the agent's policy pays at that input.

The two policies give:

$$U(\text{pay})\approx 0.99\cdot(-1{,}000)+0.01\cdot(-10^6)=-10{,}990,$$
$$U(\text{refuse})\approx 0.01\cdot 0+0.99\cdot(-10^6)=-990{,}000.$$

P-FDT pays, even though at the moment of payment the rescue is already in the past.

### 5.4 Mechanical blackmail with an imperfect predictor

The blackmailer runs the damaging program iff she predicts payment on receipt of the letter. She mispredicts "pay" with probability $\epsilon$. The two policies cost:

- the always-pay policy costs $1{,}000$;
- the refuse policy is blackmailed only by mistake, costing $\epsilon\cdot 10^6$.

So P-FDT refuses iff $\epsilon<0.001$. At $\epsilon=0.0009$ the refuse policy costs $900$, reproducing the source's figure. The crossover is at $0.1\%$. The source's illustration of the paying regime ("0.011%") appears to be a slip for $0.11\%$, since $0.00011\cdot 10^6=110<1{,}000$.

Note what the policy view does here. An agent holding the letter, *knowing* the predictor erred, still refuses. Her action at this input is just one coordinate of the plan with the best ex-ante value.

### 5.5 XOR blackmail and the smoking lesion

In XOR blackmail, $\Phi$ affects whether the letter arrives but not whether there are termites. Hence

$$U(\text{pay on letter})-U(\text{refuse on letter})=-1{,}000\cdot\Pr(\text{letter sent}\mid\text{pay policy}).$$

This is negative, so P-FDT refuses, as FDT and CDT do.

In the smoking lesion, $G$ has no arrow from $\Phi$ to cancer, so smoking is $\$1{,}000$ better under every policy, and P-FDT smokes. The source's treatment, in which the lesion changes the agent's utility function and hence which function is running, can be absorbed by putting the agent's preference type into the input. The policy then specifies what to do "as a lesion-haver" and "as a non-haver," and the analysis goes through coordinate by coordinate.

## 6. When does the policy formulation make a difference?

The source asserts that the difference "only matters in multi-agent dilemmas so far as we can tell" but gives no example. Here is a precise sufficient condition for agreement, followed by an example where they come apart. Both are my own.

### 6.1 Agreement under coordinatewise dominance

Assume, as in the source's graphs, that the per-input nodes $\Phi_y$ are independent roots in $P$. Action-level FDT at input $x$ then maximizes over $a$:

$$\mathbb E\big(V\mid \mathtt{do}(\Phi_x=a)\big)=\mathbb E_{\pi_{-x}\sim P}\big[U(a,\pi_{-x})\big],$$

where $\pi_{-x}$ denotes the other coordinates, distributed according to the agent's *beliefs about her own behaviour elsewhere*.

**Claim.** Suppose that for each $x$ there is an action $a_x$ maximizing $U(a,\pi_{-x})$ over $a$ for *every* fixing of $\pi_{-x}$. Then FDT, under any beliefs about its other coordinates, and P-FDT agree at every input, up to ties.

*Proof sketch.* If $a_x$ is pointwise best for every $\pi_{-x}$, it is best in expectation over any distribution of $\pi_{-x}$. So FDT picks $a_x$. The policy $(a_x)_{x\in\mathcal X}$ satisfies $U((a_x)_x)\ge U(\pi)$ for any $\pi$, by changing coordinates one at a time, each change weakly improving. So P-FDT picks it as well. ∎

Transparent Newcomb satisfies the condition: $f=1$ is best whatever $e$ is, and $e=2$ is best whatever $f$ is. So do the other single-agent examples above. This plausibly explains the source's observation that the distinction never arises in its examples.

### 6.2 Divergence: coordinating with yourself across inputs

The condition fails when what the agent should do at one input depends on what she does at another. That happens when several instances of the same function act on *different* inputs, which is a natural reading of "multi-agent dilemmas."

**Example (the two-copy coordination game).** Two physical copies of the agent are run.

- Copy 1 is shown "red", copy 2 is shown "blue"; each knows only its own input.
- Each picks $L$ or $R$.
- Payoff to each: $(L,L)\mapsto 2$, $(R,R)\mapsto 1$, mismatched $\mapsto 0$.

The policy space is $\{L,R\}^{\{\text{red},\text{blue}\}}$. P-FDT computes $U(L,L)=2$, $U(R,R)=1$, and $U(L,R)=U(R,L)=0$. It chooses $(L,L)$, and both copies, applying their inputs, play $L$.

Action-level FDT at "red" intervenes only on $\Phi_{\text{red}}$. It treats $\Phi_{\text{blue}}$ as a variable it believes plays $R$ with probability $q$. Comparing the two actions:

- playing $L$ yields $2(1-q)$;
- playing $R$ yields $q$.

So it plays $R$ whenever $q>2/3$. If the agent's self-model expects $R$, then $R$ at both inputs is a self-confirming fixed point and is genuinely selected. Action-level FDT here behaves like a Nash-equilibrium solver among its own input-indexed instances and can lock into the inferior equilibrium. P-FDT moves both coordinates in one counterpossible supposition and cannot get stuck this way.

The example exhibits a broader advantage. P-FDT's choice never depends on the agent's prior beliefs about her own future or parallel behaviour. That dependence on self-predictions is a vulnerability the source itself diagnoses in EDT, where "Eve's choices are at the mercy of her priors," and in CDT's instability in Death in Damascus. The policy formulation removes the analogous residue from FDT.

## 7. Philosophical motivation

The source's case for FDT carries over to P-FDT, and in some respects fits it better.

**Utility.** The source's central argument is that FDT agents "get more of what they want." P-FDT maximizes ex-ante expected utility over complete plans, given $(P,G)$, by construction. In any problem where outcomes depend only on what the agent's function outputs on various inputs, no fixed contingency plan does better in expectation. This is the source's "fair problems" standard, which it admits is not yet formalized.

**Precommitment without commitment devices.** The source argues: "If it is rational to precommit to something, then it should also be rational to predictably *behave as though* one has precommitted." P-FDT is literally the rule "execute the plan you would have committed to," so it needs no ritual of binding.

**Reflective stability.** Because P-FDT already optimizes over plans from the ex-ante standpoint, it has no motive to self-modify on receiving any input. Self-modification could only replace $\pi^\star$ by a policy with no higher $U$. The source claims FDT is "reflectively stable in fair problems"; for P-FDT the claim is close to definitional, given fixed $P$ and $G$.

**Value of information.** An agent that chooses a plan and then reads an input can always ignore the input. Hence $\max_\pi U(\pi)\ge\max_{\text{constant }\pi}U(\pi)$: information never has negative expected value at the planning stage. This reconstructs the source's claim that FDT agents "do not assign negative expected value to information."

**The "global perspective."** The source describes FDT as asking "What would the entire universe look like if the FDT algorithm behaved differently?" P-FDT is the most literal implementation. The thing varied is the whole input–output behaviour of the algorithm, not one evaluation of it.

Two objections deserve candour.

- **Strange local verdicts.** Refusing to pay while holding the blackmail letter, or leaving $\$1{,}000$ beside a visibly full box, will strike many readers as irrational at the moment of action. P-FDT accepts this outright: it evaluates acts only as parts of policies. The source's reply applies: CDT likewise asks a deterministic agent to imagine actions she cannot take, so any principled objection to "controlling" one's decision type also threatens "controlling" one's decision token.
- **Everything is pushed into $G$ and the cut in 4.2.** P-FDT is only as good as its graph of subjunctive dependencies and its choice of prior model. The source names deducing such structure "perhaps the largest open problem."

## 8. A recipe for unfamiliar cases

1. **Inputs.** Fix the decision-relevant input set $\mathcal X$ and actions $\mathcal A$. Put everything learned *within* the problem into $\mathcal X$ and everything known beforehand into $P$.
2. **Dependencies.** Draw $G$. Every physical system that computes or accurately predicts the agent's function at some input gets an arrow from $\Phi$, evaluated at that input. Merely correlated factors get no arrow.
3. **Evaluation.** For each policy, compute $U(\pi)=\mathbb E(V\mid\mathtt{do}(\Phi=\pi))$, without conditioning on the actual input.
4. **Selection.** Take $\pi^\star$ to maximize $U$. Resolve unreachable inputs by the trembling limit and remaining ties canonically.
5. **Application.** Act on $\pi^\star(x)$.

## 9. Conclusion

Footnote 16 compresses a substantive refinement of FDT into one sentence: intervene on the decision function as a whole, choose a map from inputs to actions, then apply it. I have formalized this as

$$\mathrm{P\text{-}FDT}(P,G,x)=\Big(\arg\max_{\pi}\mathbb E\big(V\mid\mathtt{do}(\Phi=\pi)\big)\Big)(x).$$

I argued that the expectation should not condition on $x$, that $P$ should be the pre-input model, and that ties and unreachable inputs need a trembling-style refinement. I also gave a precise condition, coordinatewise dominance, under which P-FDT and action-level FDT coincide. That condition explains the source's claim that the paper's examples are unaffected. Where the condition fails, as when copies of one function must coordinate across different inputs, P-FDT selects the jointly optimal plan, while the action-level theory can be trapped by its own self-predictions. P-FDT thus makes precise the source's slogan that a rational agent acts as she would have precommitted to act. It remains bounded by the source's acknowledged open problems: counterpossible reasoning, constructing the dependency graph, and a formal account of fairness.

**References**

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060. The primary source, especially footnotes 7 and 16.
- Dai, W. (2009). "Towards a New Decision Theory." *Less Wrong*.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.*
- Pearl, J. (2000). *Causality.*