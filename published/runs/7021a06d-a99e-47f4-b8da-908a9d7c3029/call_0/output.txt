# Choosing the Function, Not the Act: An Essay on P-FDT (Policy Functional Decision Theory)

## 1. The source and what it commits to

Yudkowsky and Soares's paper *Functional Decision Theory* presents most of its formal machinery in terms of actions. The decision procedure in their Equation (4) intervenes on a node representing "the output of FDT given these inputs" and asks which *action* that output should be. Twice, however, the authors note that this is not the version they actually prefer. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which this essay takes as the primary source, says:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described in these footnotes **P-FDT** (policy functional decision theory). The action-level procedure of the paper's Equation (4) I will call **A-FDT**. I will also refer to causal decision theory (CDT) and evidential decision theory (EDT).

Footnote 16 makes four claims:

1. The point of intervention is a node written $\mathrm{FDT}(-)$.
2. The object chosen at that node is a policy, a map from inputs to actions.
3. The agent then applies the chosen policy to her actual input to get her action.
4. As far as the authors can tell, this differs from A-FDT only in multi-agent dilemmas.

Several things are left open. The footnote does not say exactly what the node $\mathrm{FDT}(-)$ is indexed by. It does not say what counts as an "input," which probability distribution evaluates policies, how ties are broken, whether policies may be randomized, or why the difference should be confined to multi-agent cases. Below I state the base framework, give my reconstruction of P-FDT, work through examples, prove a small result explaining when P-FDT and A-FDT come apart, and then address the open questions. Material that is my own interpretation or proposal is labelled as such.

## 2. Background: the action-level theory (A-FDT)

The paper models an agent by a world-model $(P, G)$:

- $P$ is a probability distribution over variables, including variables for the outputs of mathematical functions.
- $G$ is a graph saying how changing one variable propagates to others. Unlike a purely causal graph, $G$ is meant to encode *subjunctive* dependence: dependence that holds because two physical systems compute the same function. Causal dependence is a special case.

Write $V$ for utility and $x \in \mathcal X$ for the agent's observation history. The paper defines A-FDT as

$$
\mathrm{FDT}(P,G,x) := \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\!\left(V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right). \tag{A-FDT}
$$

Two features matter for everything that follows.

**The agent intervenes on a logical node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable representing what the FDT algorithm outputs on these inputs. Every physical system whose behaviour depends on that output changes in the hypothetical. This includes the agent's body, a predictor's simulation, and a twin. This is the paper's "intervene on the *type*" rather than the token.

**Observations select the node; they are not conditioned on.** The expectation in (A-FDT) does not condition on $\textsc{Obs}=x$. In the paper's words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." In the transparent Newcomb problem there are separate nodes $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. An agent who sees a full box intervenes on the first and evaluates the result against her whole prior model, including worlds in which she would have seen an empty box.

So A-FDT already makes the agent's function, on a given input, the unit of choice. What it does *not* do is treat the function's behaviour across all inputs as a single object. When the agent intervenes on the node for input $x$, the nodes for other inputs $x'\neq x$ keep whatever distribution $P$ assigns them. Footnote 16 changes exactly this.

## 3. Definition of P-FDT

**My interpretation.** I read "the node $\mathrm{FDT}(-)$" as a single variable $\Pi$, written $\textsc{fdt}(\underline P,\underline G)$ with the observation slot left open. Its values are policies $\pi:\mathcal X\to\mathcal A$. The value of $\Pi$ is the function $x\mapsto \mathrm{FDT}(P,G,x)$, that is, the agent's complete input–output behaviour. In the graph, every instantiation of the agent's decision procedure that receives input $x$ outputs $\Pi(x)$. Every predictor that models the agent reads (some part of) $\Pi$.

**Definition (P-FDT).** Given world-model $(P,G)$ with policy node $\Pi$, define the policy value

$$
\mathrm{EU}(\pi) := \mathbb E\big(V \,\big|\, \mathtt{do}(\Pi=\pi)\big), \qquad \pi\in\mathcal A^{\mathcal X},
$$

and

$$
\pi^\ast := \operatorname*{argmax}_{\pi\in\mathcal A^{\mathcal X}} \mathrm{EU}(\pi), \qquad \text{P-FDT}(P,G,x) := \pi^\ast(x).
$$

This has the two-stage structure the footnote describes: "choose … a *policy* … to which the agent then applies her inputs in order to select an action."

Three remarks fix the meaning.

- **Joint intervention.** $\mathtt{do}(\Pi=\pi)$ is equivalent to intervening simultaneously on every node $\textsc{fdt}(\underline P,\underline G,\underline{x'})$, setting each to $\pi(x')$. A-FDT intervenes on one coordinate; P-FDT intervenes on all of them at once.
- **Same prior for every input.** The maximization does not depend on $x$. Every instantiation of the agent, whatever it observes, computes the same $\pi^\ast$ from the same $(P,G)$. Only the final application step uses $x$. This is the formal content of the claim that the function, not the act, is what gets chosen.
- **No conditioning on $x$.** As with A-FDT, observations are never conditioned on. They enter only through $\pi^\ast(x)$.

## 4. A first example: transparent Newcomb

The setup: box B is filled iff a 99%-accurate predictor predicts the agent would one-box upon seeing it full. Inputs are $\mathcal X=\{\textit{full},\textit{empty}\}$ and actions are $\{1,2\}$ (one-box, two-box). Since the predictor reads $\Pi(\textit{full})$, the agent sees *full* exactly when the predictor's (possibly erroneous) prediction is "one-box."

| $\pi(\textit{full})$ | $\pi(\textit{empty})$ | accurate (0.99) | inaccurate (0.01) | $\mathrm{EU}(\pi)$ |
|---|---|---|---|---|
| 1 | 2 | full, take 1: \$1,000,000 | empty, take 2: \$1,000 | **\$990,010** |
| 1 | 1 | \$1,000,000 | empty, take 1: \$0 | \$990,000 |
| 2 | 2 | empty, take 2: \$1,000 | full, take 2: \$1,001,000 | \$11,000 |
| 2 | 1 | empty, take 1: \$0 | full, take 2: \$1,001,000 | \$10,010 |

So $\pi^\ast=(1,2)$: one-box on *full*, two-box on *empty*. The agent who sees full boxes applies $\pi^\ast$ and leaves the \$1,000 behind. This matches the paper's A-FDT verdict. A-FDT gives $\$990{,}000+0.01q\cdot\$1{,}000$ for one-boxing, where $q$ is the prior that she two-boxes on *empty*. The top two rows are that expression with $q=1$ and $q=0$.

The reason the two theories agree here is visible in the table. Whatever $\pi(\textit{empty})$ is, $\pi(\textit{full})=1$ beats $\pi(\textit{full})=2$. The coordinate being decided has a choice that is best regardless of the other coordinates. The next section shows this is the general condition for agreement.

## 5. When P-FDT and A-FDT come apart

The following analysis is mine; the paper does not give it. It requires one modelling assumption, which holds in all the paper's examples:

**(Separability.)** The nodes $N_x := \textsc{fdt}(\underline P,\underline G,\underline x)$ have no edges among themselves. $V$ depends on the agent's decision function only through the tuple $(N_x)_{x\in\mathcal X}$. Intervening on one $N_x$ leaves the marginal of $N_{-x}$ unchanged.

Under separability, the A-FDT value of action $a$ at input $x$ is an average of policy values:

$$
U_x(a) := \mathbb E(V\mid \mathtt{do}(N_x=a)) = \sum_{\pi_{-x}} P(N_{-x}=\pi_{-x})\ \mathrm{EU}(a,\pi_{-x}).
$$

Here $(a,\pi_{-x})$ is the policy that plays $a$ on $x$ and $\pi_{-x}$ elsewhere. Three facts follow.

**Proposition 1 (P-FDT's choice is A-FDT-consistent).** If the agent is certain of her own behaviour on the other inputs, $P(N_{-x}=\pi^\ast_{-x})=1$, then $U_x(a)=\mathrm{EU}(a,\pi^\ast_{-x})$. Since $\pi^\ast$ is a global maximum, $\pi^\ast(x)\in\operatorname{argmax}_a U_x(a)$.

**Proposition 2 (agreement under coordinate dominance).** Suppose some $a^\ast$ maximizes $\mathrm{EU}(a,\pi_{-x})$ for every $\pi_{-x}$. Then $a^\ast$ maximizes $U_x$ under *any* prior, and some optimal policy has $\pi^\ast(x)=a^\ast$. Transparent Newcomb, Parfit's hitchhiker, and both blackmail problems all satisfy this at the input where the agent actually decides.

**Proposition 3 (no converse).** A-FDT's choices form a coordinate-wise optimum: each input-node is best given beliefs about the others. P-FDT's choice is a global optimum. In general the former need not be the latter, and A-FDT's outcome depends on the agent's beliefs about her own behaviour elsewhere.

This is exactly the distinction in team decision theory (Marschak and Radner) between *person-by-person optimal* and *team optimal* decision rules. A-FDT treats the agent's responses to different inputs as members of a team, each choosing given beliefs about the others. P-FDT treats the decision rule as a single choice.

### The coordination example

This example is my own. An agent's decision function is instantiated twice: for instance, a program is copied, or Omega duplicates a person. Instance $i$ receives input $x_i\in\{1,2\}$ and knows only its own input. Each picks $A$ or $B$. Both instances care about the shared payoff:

$$
V(A,B)=V(B,A)=10,\qquad V(A,A)=1,\qquad V(B,B)=0,
$$

where the first coordinate is the action of the instance that received input 1.

**Under P-FDT.** The policies are elements of $\{A,B\}^{\{1,2\}}$, and $\mathrm{EU}(\pi)=V(\pi(1),\pi(2))$. The maximizers are $AB$ and $BA$. With a fixed canonical tie-break (say lexicographic), both instances compute $\pi^\ast=AB$, because they run the same function on the same $(P,G)$. Instance 1 plays $A$, instance 2 plays $B$, and both get 10.

**Under A-FDT.** Let $q$ be instance 1's credence that $N_2=B$. Then

$$
U_1(A)=10q+1(1-q)=1+9q,\qquad U_1(B)=10(1-q),
$$

so instance 1 plays $A$ iff $q>9/19$. Instance 2 is symmetric. With uninformed priors $q=r=1/2$, both play $A$ and receive 1.

Worse, suppose each instance tries to make its beliefs consistent by predicting the other's choice with the same procedure. Then a belief that the other plays $A$ makes $B$ better, and the reverse. The resulting oscillation resembles the instability the paper attributes to CDT in Death in Damascus. A-FDT succeeds only if the agent's prior already encodes a coordinated assignment, as Proposition 1 requires. P-FDT supplies that assignment instead of presupposing it.

This also explains the footnote's phrase "multi-agent dilemmas." My reading is that what matters is not distinct agents as such but *multiple instantiations of one function receiving different inputs*. That covers copies, simulations queried on different inputs, and one agent at different times with different observations. If all instantiations receive the same input, the policy collapses to a single action and the theories coincide. If only one instantiation's input matters and coordinate dominance holds, Proposition 2 makes them coincide.

## 6. Further applications

### Mechanical blackmail

Inputs are $\{\textit{letter}, \varnothing\}$. The blackmailer runs the damaging program if she predicts payment. With an error rate $\varepsilon$, she runs it anyway when she predicts refusal.

- A policy that pays on *letter* is always blackmailed and loses \$1,000.
- A policy that refuses is blackmailed with probability $\varepsilon$ and then loses \$1,000,000.

So P-FDT refuses iff $10^6\varepsilon < 10^3$, that is, iff $\varepsilon<0.001$. The agent holding the letter applies the refusing policy even though, in her actual situation, refusing costs her \$1,000,000. This is the paper's "global perspective": the policy is evaluated over all the worlds consistent with the model, not over the world she finds herself in.

### Smoking lesion

The paper models the lesion as determining which world-model ($P_S$ or $P_R$) the agent runs. Those are different functions, and changing one does not change $\textsc{Cancer}$. P-FDT therefore inherits the paper's verdict: smoke.

There is one interpretive subtlety. If "inputs" were taken to include the world-model itself, so that a single policy also covered the $P_R$ case, the agent would be choosing jointly for both lesion-types. Even then $\textsc{Cancer}$ has no edge from the policy node, and smoking under $U_S$ remains coordinate-dominant. The verdict is robust to this choice.

## 7. Open questions and my proposed resolutions

Footnote 16 is a single sentence, so much is underdetermined. Below I separate the gaps from my operational proposals.

**(a) What is the node $\mathrm{FDT}(-)$?** The dash can be read in two ways: as abbreviating arguments, or as an open observation slot. *Proposal:* read it as $\textsc{fdt}(\underline P,\underline G)$, a policy-valued node that is the common parent of all the observation-indexed nodes. This is the only reading on which "choose … a policy" and "then applies her inputs" fit together.

**(b) What are the "inputs"?** Footnote 7 says observations, and footnote 16 says inputs. *Proposal:* the domain is the set $\mathcal X$ of observation histories possible within the decision problem as modelled by $(P,G)$, with $(P,G)$ held fixed. Different world-models (as in the lesion case) are treated as different functions, following the paper's own treatment. Enlarging the domain is a further, nontrivial step.

**(c) Which prior evaluates policies?** Because nothing is conditioned on $x$, the answer depends heavily on what $P$ is. If $P$ were already updated on seeing a full box, the policy analysis would change. The paper's worked examples use a $P$ that leaves the observation uncertain. *Proposal:* $P$ should be the agent's model as of a point before any process that subjunctively depends on her function (a predictor, a copier) has acted on it. This matches the paper's slogan that FDT agents "act as they would have precommitted to act." The paper does not settle where that point lies in general, and for realistic agents it is a substantive question.

**(d) Ties.** Ties are far more common in policy space than in action space; the coordination example has two optimal policies. Coordination then depends on every instantiation breaking ties identically. *Proposal:* the tie-break is part of the function, fixed by a canonical ordering on $\mathcal A^{\mathcal X}$. That is cheap, but necessary. Without it, P-FDT's advantage over A-FDT can disappear.

**(e) Randomized policies.** The footnote speaks of maps from inputs to actions. *Proposal:* default to deterministic policies, and admit behavioural randomization ($\pi:\mathcal X\to\Delta(\mathcal A)$) only when the model contains randomness that predictors cannot see. Problems with imperfect recall, where several decision points share one input, are the natural place where this matters.

**(f) Constructing $G$.** P-FDT inherits FDT's central gap. There is no general account of how to determine which variables subjunctively depend on the agent's function. For P-FDT the demand is somewhat larger: the graph must say how predictors respond to the agent's *whole* policy, including her behaviour on inputs she will never receive. The paper calls deducing subjunctive dependencies "perhaps the largest open problem," and the policy formulation does not resolve it.

**(g) Tractability.** $|\mathcal A^{\mathcal X}|=|\mathcal A|^{|\mathcal X|}$, so exhaustive policy search is exponential. In practice one can use Proposition 2: whenever coordinate dominance holds, compute only the relevant coordinate.

## 8. A procedure for unfamiliar cases

1. **Identify the instantiations.** List every system that computes, simulates, or predicts the agent's decision function, together with the input each receives.
2. **Build $(P,G)$** with a policy node $\Pi$. Each instantiation receiving input $x$ outputs $\Pi(x)$, and each predictor depends on the part of $\Pi$ it models. Variables merely correlated with $\Pi$, such as a lesion, get no edge from $\Pi$.
3. **Fix the evaluating prior** at the point before dependent processes act (my proposal in 7c).
4. **Compute $\mathrm{EU}(\pi)=\mathbb E(V\mid\mathtt{do}(\Pi=\pi))$** for each policy, or use coordinate dominance to prune.
5. **Select $\pi^\ast$** with the canonical tie-break.
6. **Apply** $\pi^\ast$ to the actual observation.
7. **Check against A-FDT.** If the relevant coordinate is dominant, the two agree. If not, the case is one where the policy formulation does real work, and the verdict should be justified by the joint evaluation.

## 9. Philosophical significance

The paper argues that FDT is "to subjunctive dependence as causal decision theory is to causal dependence," and that the agent should ask "Which output of this very function would yield the best outcome?" P-FDT carries this thought one step further. A function's output on one input is not the function. If the agent's identity for decision purposes is the function she computes, then the natural object of choice is that function's entire graph, the map from all inputs to outputs.

A-FDT asks her to vary one row of her own truth table while treating the other rows as external facts with prior probabilities. That is a vestige of the token-level view FDT was meant to replace. P-FDT eliminates it. The practical result is the coordination advantage shown above: instantiations that see different things still act as parts of one deliberate plan, without communicating and without inconsistent self-predictions. The cost is that P-FDT is committed even more firmly to evaluating from a prior vantage point. That makes the question of *which* prior (7c) the main philosophical burden of the theory.

## Conclusion

On the reading defended here, P-FDT is the formulation of FDT that its authors prefer. It intervenes on a single policy-valued node $\Pi=\textsc{fdt}(\underline P,\underline G)$, picks the policy $\pi^\ast$ maximizing $\mathbb E(V\mid\mathtt{do}(\Pi=\pi))$, and acts on $\pi^\ast(x)$.

It agrees with the action-level A-FDT whenever the decision at the agent's actual input has a choice that is best regardless of her behaviour on other inputs. That is why the paper's examples (Newcomb, transparent Newcomb, hitchhiker, blackmail, lesion) do not distinguish the two. The theories diverge when several instantiations of one function receive different inputs and must coordinate. There A-FDT yields only a person-by-person optimum that depends on the agent's self-beliefs, while P-FDT selects the jointly best plan.

The footnote leaves open the indexing of the node, the domain of inputs, the evaluating prior, tie-breaking, randomization, and the construction of the dependency graph. I have proposed operational answers to these, but the last two remain open research problems rather than settled parts of the theory.

## References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (esp. Eq. 4 and footnotes 7, 16).
- Marschak, J. & Radner, R. (1972). *Economic Theory of Teams*. Yale University Press.
- Dai, W. (2009). "Towards a New Decision Theory." *Less Wrong*.