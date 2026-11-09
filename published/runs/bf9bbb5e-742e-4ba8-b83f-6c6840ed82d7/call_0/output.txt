# Policy Functional Decision Theory (P-FDT): Choosing What a Function Does on Every Input

## 1. The source and the task

Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality* develops functional decision theory in its action-level form. In two footnotes, however, the authors say that this is not their preferred version. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which this essay treats as the primary source, gives the operational content:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the theory described there **P-FDT** (policy functional decision theory). To keep the two theories apart, I call the formulation in the paper's main text, its equation (4), **A-FDT** (action-level FDT). Causal decision theory (CDT) and evidential decision theory (EDT) keep their usual names.

The footnote is two sentences long. It fixes three things:

1. the object of choice is a policy, meaning a map from inputs to actions;
2. the choice is made by intervention on a node representing the decision function's output;
3. the action is obtained afterward, by applying the policy to the actual input.

Everything else is left open: how the expectation is formed, whether observations are conditioned on, what the policy space is, how ties are broken, and when P-FDT and A-FDT diverge. Below I state what the source commits to, then give an operational reading and justify each added assumption. My own proposals are marked as such.

## 2. Background: the A-FDT machinery

The paper models an agent with a world-model $(P, G)$:

- $P$ is a probability distribution over variables.
- $G$ is a graph encoding dependence structure. The paper calls this structure "logical, mathematical, computational, causal, etc."

The world-model includes variables standing for the outputs of mathematical functions. Among them is a variable $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, which represents what the FDT algorithm outputs on the agent's own model and observation history $x$. The underline denotes dequoting.

Utility is the variable $V = \mathcal{U}(\textsc{Outcome})$. A-FDT is defined by

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right). \tag{A}
$$

Here $\mathtt{do}$ is Pearl's intervention operator, applied to a logical node rather than a physical one. Three features of (A) matter for what follows.

- **What gets intervened on.** The agent intervenes on the *type* (the output of her decision function), not on the *token* (her physical act). Anything that subjunctively depends on that output changes along with it. Examples are a predictor's model of her, or a twin running the same function.
- **How observations enter.** The paper says that "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Different histories $x$ index different nodes $\textsc{fdt}(\underline P,\underline G,\underline x)$.
- **What is held fixed.** Intervening on the node for input $x$ leaves the nodes for other inputs $y \neq x$ at their prior distribution. The paper's transparent Newcomb calculation shows this: "Write $q$ for Fiona's prior probability that she two-boxes upon seeing the box empty".

The third feature is what P-FDT changes.

## 3. Definition of P-FDT

Let $\mathcal X$ be the set of possible observation histories and $\mathcal A$ the set of actions. A **policy** is a function $\pi:\mathcal X\to\mathcal A$, and $\Pi$ is a set of policies. Following the footnote, the world-model contains a node $\textsc{fdt}(\underline P,\underline G)$ whose value is a policy: the input–output behaviour of the decision function. Footnote 16 writes this as $\mathrm{FDT}(-)$, with the dash marking the input slot that is no longer fixed.

**P-FDT.** Given $(P,G)$ and an actual history $x$:

$$
\pi^\ast \in \arg\max_{\pi\in\Pi}\ \mathbb E\!\left(V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G)=\pi\big)\right), \qquad \text{P-FDT}(P,G,x) := \pi^\ast(x). \tag{P}
$$

Two of my modelling assumptions turn (P) into a usable procedure.

**Assumption 1 (factorisation).** Every place in $G$ where the decision function's behaviour on a particular input $y$ matters reads $\pi(y)$ from the policy node. This covers the agent's own body when she observes $y$, a predictor simulating her on $y$, and a copy of her receiving $y$. So $\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)$ amounts to simultaneously setting every input-indexed node:

$$
\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi) \;\equiv\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline y)=\pi(y)\ \text{for all } y\in\mathcal X\big).
$$

This is how I read "intervenes on the node $\mathrm{FDT}(-)$": the policy is the function's behaviour on all inputs at once.

**Assumption 2 (no conditioning on $x$ during evaluation).** The expectation in (P) is taken under the model the agent holds at the start of the decision problem. The actual history $x$ is used only in the final step $\pi^\ast(x)$. The footnote supports this directly: the agent chooses a policy "to which the agent then applies her inputs in order to select an action." Equation (A) supports it as well, since it contains no $\textsc{Obs}=x$ term either.

The paper is not fully consistent on this point. Its transparent Newcomb section writes the A-FDT objective with "$\textsc{Obs}=\textit{full}$" inside the $\mathtt{do}$, yet the calculation that follows does not condition on it. The calculation treats the empty-box branch as live. I follow the calculation and equation (A).

Write $U(\pi) := \mathbb E(V\mid \mathtt{do}(\textsc{fdt}=\pi))$ for the value of a policy.

## 4. Applying P-FDT: worked cases

The recipe is mechanical:

1. Enumerate the relevant inputs.
2. Enumerate the policies.
3. For each policy, trace which input each instance of the function actually receives and what it outputs.
4. Compute $U(\pi)$.
5. Apply the best policy to the actual input.

### 4.1 Transparent Newcomb

The setup:

- The inputs are $\mathcal X=\{\textit{full},\textit{empty}\}$.
- The predictor is accurate with probability $0.99$.
- The predictor fills box B iff it predicts one-boxing on seeing a full box. So the prediction reads $\pi(\textit{full})$.

Write $\pi=(f,e)$, where $f$ is the action on seeing a full box and $e$ the action on seeing an empty one.

**Case $f=\textit{one}$.**
- With probability 0.99 the box is full and the agent one-boxes, receiving \$1,000,000.
- With probability 0.01 the predictor errs, the box is empty, and the agent plays $e$.

$$U(\textit{one},e)=990{,}000+0.01\cdot 1{,}000\,[e=\textit{two}].$$

**Case $f=\textit{two}$.**
- With probability 0.99 the box is empty and the agent plays $e$.
- With probability 0.01 the box is full by error and she two-boxes, receiving \$1,001,000.

$$U(\textit{two},e)=10{,}010+990\,[e=\textit{two}].$$

The optimum is $\pi^\ast=(\textit{one},\textit{two})$, with $U=990{,}010$. Facing two full boxes, the agent applies $\pi^\ast(\textit{full})=\textit{one}$ and one-boxes, as the paper's A-FDT agent does. Unlike the A-FDT calculation, this one does not depend on a prior $q$ about the agent's own behaviour on the empty-box input. That quantity is chosen jointly, not assumed.

### 4.2 XOR blackmail

The setup:

- There is one relevant input, *letter*, with policy value either *pay* or *refuse*.
- The prior probability of termites is $p$.
- The predictor is infallible.

Under policy *pay*, the letter arrives exactly when there are no termites, so

$$U(\textit{pay})=-p\cdot 10^6-(1-p)\cdot 10^3.$$

Under policy *refuse*, the letter arrives exactly when there are termites, so

$$U(\textit{refuse})=-p\cdot 10^6.$$

Refusing is strictly better. The policy cannot touch the termites; it only changes when the letter is sent. This is the same verdict the paper gives for Fiona.

### 4.3 Mechanical blackmail with an error rate

Suppose the blackmailer wrongly predicts payment with probability $\varepsilon$.

- The policy *pay* is blackmailed essentially always and loses \$1,000.
- The policy *refuse* is blackmailed only by error and loses $\varepsilon\cdot 10^6$ in expectation.

P-FDT refuses iff $\varepsilon<10^{-3}$. With the paper's $\varepsilon=0.0009$, refusing costs \$900 in expectation and P-FDT refuses, even while holding the letter. The paper's second figure ("0.011%") seems to be a misprint for a rate just above this threshold.

In all three cases P-FDT and A-FDT agree, as the footnote leads us to expect. The next section explains why, and when they come apart.

## 5. How P-FDT relates to A-FDT

A-FDT optimises one input-indexed node at a time, holding the others at the agent's beliefs about them. P-FDT optimises all of them jointly. This is the familiar distinction from team decision theory (Marschak and Radner) between *person-by-person* optimality and *team* optimality. The connection is my addition, not the source's, but it makes the relationship precise.

Under Assumption 1, fix the agent's beliefs about the off-input nodes to be a point mass on some policy $\sigma$. A-FDT at input $x$ then evaluates action $a$ as $U(\sigma[x\mapsto a])$: the value of $\sigma$ with its $x$-entry replaced by $a$.

**Proposition 1 (P-FDT optima are A-FDT fixed points).** Let $\pi^\ast$ maximise $U$. Suppose the agent believes she follows $\pi^\ast$ on inputs other than $x$. Then $\pi^\ast(x)$ maximises the A-FDT objective at $x$, and this holds for every $x$, including inputs that have probability zero under $\pi^\ast$.

*Proof.* For any $a$, $U(\pi^\ast[x\mapsto a])\le U(\pi^\ast)=U(\pi^\ast[x\mapsto\pi^\ast(x)])$. $\square$

**Proposition 2 (the converse fails).** A policy $\sigma$ may satisfy $U(\sigma[x\mapsto a])\le U(\sigma)$ for all $x$ and $a$, so that it is a self-consistent A-FDT profile, and still have $U(\sigma)<\max_\pi U(\pi)$.

The proof is the example in §6. Together, the propositions say that A-FDT prescriptions are the stable points of P-FDT's objective under single-input deviations, but A-FDT can settle on a stable point that is not optimal. Which point it reaches depends on the agent's prior beliefs about her own behaviour on other inputs.

This is a milder version of a fault the paper itself finds in EDT, whose choices "are at the mercy of her priors." P-FDT removes that dependence, because the off-input behaviour is a choice variable rather than a belief.

This also suggests why the authors saw no difference in their examples. In transparent Newcomb, the blackmail cases, and the twin prisoner's dilemma, the payoff-relevant structure is "separable." Either only one input matters, as with the twins who see identical inputs. Or the behaviour on other inputs enters additively without interacting with the choice at $x$. In such problems every person-by-person optimum is team-optimal, so the two theories coincide.

## 6. Where they diverge: instances of the function on different inputs

Footnote 16 says the difference matters "in multi-agent dilemmas." On my analysis, the operative condition is narrower and more specific:

> P-FDT and A-FDT can diverge when **several instances of the same function receive different inputs, and the payoff depends on how their outputs interact.**

Multi-agent settings with copies are the paradigm case. This characterisation is my interpretation, not the source's claim.

**Example (labelled copies, coordination).** An agent is copied. Copy 1 receives input $1$, copy 2 receives input $2$, and each outputs $A$ or $B$. Each copy gets 10 if both output $A$, 5 if both output $B$, and 0 if they mismatch. Both copies run the same function with the same $(P,G)$.

*P-FDT.* The policies are pairs $(\pi(1),\pi(2))$:

| Policy | $U(\pi)$ |
|---|---|
| $(A,A)$ | 10 |
| $(B,B)$ | 5 |
| $(A,B)$ | 0 |
| $(B,A)$ | 0 |

So $\pi^\ast=(A,A)$. Copy 1 applies it to input 1 and outputs $A$; copy 2 does the same.

*A-FDT.* Copy 1 intervenes on $\textsc{fdt}(\underline P,\underline G,1)$ and holds $\textsc{fdt}(\underline P,\underline G,2)$ at its prior, $r=P(\pi(2)=A)$. Then

$$\mathrm{EU}(A)=10r, \qquad \mathrm{EU}(B)=5(1-r).$$

So $A$ is chosen iff $r>1/3$. If the agent's self-model says she tends to play $B$ on input 2, then $B$ is correct on input 1 and, symmetrically, on input 2. The profile $(B,B)$ is self-confirming: a person-by-person optimum that is not team-optimal. This is Proposition 2.

**Anti-coordination variant, and ties.** Now let the copies get 10 each iff their outputs differ.

- P-FDT finds two optimal policies, $(A,B)$ and $(B,A)$.
- A-FDT under symmetric self-uncertainty ($r=1/2$) is indifferent on each input. The copies may then break the tie the same way and mismatch.

For P-FDT the tie is harmless if the decision function includes a deterministic tie-breaking rule over policies, such as a fixed enumeration order. Both copies compute the same argmax and select the same $\pi^\ast$, then apply it to different inputs, so they anti-coordinate. This is a further proposal of mine: **tie-breaking among optimal policies must be a fixed part of the function, not delegated to independent randomness.** Without this, P-FDT's guarantee of coordination among copies fails exactly at ties.

The same structure appears within a single agent over time. The paper's gym example is one case: the agent "this week" and "next week" are instances of one function on different inputs. When those instances' choices interact non-additively, P-FDT's joint choice is the safer prescription. So I read the footnote's "multi-agent" as covering any setting where the function is instantiated more than once.

## 7. Choices the footnote leaves open

### 7.1 What prior evaluates policies?

Assumption 2 says that $x$ is not conditioned on. But the model $P$ may itself already contain earlier observations. I propose that $P$ be the model at the start of the decision problem, before the problem-specific inputs that the policy ranges over.

This fits the paper's remark that FDT agents "act as they would have precommitted to act": the policy is the precommitment, evaluated from the vantage point at which a precommitment could have been made.

How far back that vantage point should go is a substantive question the source does not settle. The paper notes that "updateless decision theory" is an ancestor of FDT, which suggests a lean toward early vantage points. A safe operational rule: the policy should range over every input that some instance of the function, or some predictor of it, might be responding to within the problem.

### 7.2 The policy space

$\mathcal A^{\mathcal X}$ is finite only when $\mathcal X$ is finite. The paper allows $\mathcal X$ to be countable, in which case the policy space is uncountable and the argmax may not exist. Operationally:

- restrict to the finitely many inputs relevant to the problem at hand, which every example in the paper permits; or
- restrict to computable policies and accept a supremum when no maximum exists.

**Mixed policies** are not mentioned. I would allow randomisation only through explicit nodes in $G$, such as the paper's "truly random coin," so that predictors' access to the randomisation is modelled rather than assumed. Since $U$ is linear in a mixture over deterministic policies, a deterministic optimum exists whenever randomness is not itself rewarded.

### 7.3 Off-path inputs

Under the optimal policy some inputs may have probability zero; the empty box in a world of FDT agents is an example. EDT-style conditioning is undefined there. P-FDT still prescribes $\pi^\ast(x)$. Proposition 1 shows this prescription agrees with what A-FDT would choose on that input, given correct self-beliefs. I count this as a strength of the policy formulation, not merely a technicality.

### 7.4 Constructing $G$

P-FDT inherits the open problem the paper calls "perhaps the largest open problem in the study of functional decision theory": how to obtain a graph that says how the world would differ if the function behaved differently. The policy formulation slightly sharpens the demand. $G$ must now say which instance, or which predictor, reads which input of the policy. A predictor in transparent Newcomb reads $\pi(\textit{full})$, not $\pi(\textit{empty})$. The source says nothing about how these input-specific dependencies are learned.

### 7.5 Self-reference

The policy node $\textsc{fdt}(\underline P,\underline G)$ refers to the function being computed, just as the A-FDT node does. The paper's appeal to Kleene's recursion theorem ("quining") applies unchanged. The agent needs a variable *representing* her policy, not knowledge of its value.

## 8. Philosophical motivation

The argument for P-FDT over A-FDT follows the paper's own argument for FDT over CDT. The paper diagnoses CDT as imagining "breaking *too many* correlations": changing the token while holding fixed the type that predictors track.

A-FDT has a smaller version of the same flaw. When choosing at input $x$, it changes the function's output on $x$ while holding its outputs on other inputs fixed at prior beliefs. But the function's behaviour on input 2 is the same function as its behaviour on input 1. If one would not imagine $6288+1048$ changing while $1048+6288$ stays put, one should not imagine $\pi(1)$ changing without asking what $\pi$ as a whole should be.

P-FDT takes the paper's "global perspective" one step further: "What would the entire universe look like if the FDT algorithm behaved differently?" now ranges over the algorithm's whole input–output behaviour.

P-FDT also makes FDT's reflective-stability claim easier to state. A P-FDT agent who picks $\pi^\ast$ at the start of a problem and the same agent re-running P-FDT after seeing $x$ use the same objective $U$, by Assumption 2. So she reaches the same $\pi^\ast$ (given fixed tie-breaking) and the same action. Her plan and her execution cannot come apart. This is the formal content of "FDT agents always act as they would have precommitted to act."

## 9. Conclusion

On my reading of footnote 16, P-FDT has a simple core:

- intervene on a node whose value is the decision function's entire map from inputs to actions;
- evaluate each map by expected utility in the resulting hypothetical, without conditioning on the actual input;
- apply the best map to the input actually received.

In separable problems, which include every example in the paper, it agrees with the action-level A-FDT. In general, its prescriptions are the team-optimal points among A-FDT's self-consistent profiles. It diverges from A-FDT when several instances of the function receive different inputs and must coordinate. There A-FDT can get stuck on a self-confirming but suboptimal profile or mis-break ties, while P-FDT, with fixed deterministic tie-breaking, does not.

The footnote leaves open the evaluation prior, the policy space, randomisation, and above all the construction of the dependence graph. I have proposed operational answers for the first three. The fourth is the paper's own central open problem, and the policy formulation inherits it.

**References.** Yudkowsky, E. and Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (esp. eq. (4), §§5–6, 9, and footnotes 7 and 16). Marschak, J. and Radner, R., *Economic Theory of Teams* (1972), for the person-by-person versus team-optimality distinction.