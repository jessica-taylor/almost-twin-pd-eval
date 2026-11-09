# 025_fdt_policy_anthropic_claude-opus-5.5_rhigh_phigh / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/7021a06d-a99e-47f4-b8da-908a9d7c3029/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/7021a06d-a99e-47f4-b8da-908a9d7c3029/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out a roughly 2,400 to 3,000 word essay on P-FDT, anchored in footnote 16 and its cross-reference to footnote 7, and I need to quote the footnote accurately.

I'm now checking the two footnotes more closely: one says policies rather than actions only matter in multi-agent dilemmas, which the paper sets aside for exposition. I'm writing out the P-FDT argmax over policies, and I'm noting that the node's dash leaves open whether it's indexed by observation, so I'm reading it as the whole policy, equivalent to jointly intervening on every observation's node.

I'm weighing when action-level FDT and policy-level P-FDT actually come apart: they differ when the other observation-nodes are uncertain or mis-modeled, and most clearly when several copies of the agent receive different inputs and need to coordinate.

I'm now working through the coordination example that shows where action-level and policy-level FDT diverge: two copies receive different inputs, and each has to choose so that their joint choice pays off. With action-level FDT, each copy holds the other's output at its prior, so ties and wrong priors can leave them miscoordinated. Policy selection instead picks one optimal policy, and since both copies compute that same function, they land on matching outputs.

I'm now building a concrete payoff table for the coordination case: a payoff of 10 when the two copies pick opposite actions, and 0 otherwise. With uniform priors the action-level calculation ties, and an alphabetical tie-break would leave both copies choosing A and getting nothing, so I'm considering a version with asymmetric payoffs to make the choice decisive.

I'm testing a payoff structure where (A,A) gives 1 and (A,B) and (B,A) give 10, so that uniform priors make action-level FDT pick A for both, while a fixed-point prediction of the other copy picking A makes switching to B look better and the loop becomes unstable. Policy selection avoids this by choosing the best of the four policies outright, and that outcome is the one I'm about to work through.

I'm checking the single-instance case next, where policy selection should give the same answer as action-level FDT. In transparent Newcomb with a 99%-accurate predictor, the best policy comes out the same either way, so the two formulations agree there.

I'm checking the single-instance transparent Newcomb case by hand: policy one-box/two-box gives about 990,010 expected, while the two-box policy gives about 11,000, so the best policy is the one-boxing one.

I'm checking the transparent Newcomb case against both formulations and confirming that the best policy is one-box on the full box and two-box on the empty one. I'm also considering whether a proposition about when action-level and policy-level FDT coincide could hold, namely that if the agent's beliefs about its own policy on other inputs are fixed at the optimal policy, the action-level choice on the actual input would match.

I'm checking that the policy-level and action-level formulations agree in the single-instance case: if the other inputs' policy values are fixed at the optimal policy, the action-level choice on the actual input must land on the same action, since the optimal policy maximizes over every input's entry at once. The converse doesn't hold, though: action-level FDT can settle on local optima where no single instance wants to change, while policy selection finds the global optimum.

Next I'm checking whether action-level FDT conditions on the observation: the source's equation intervenes on the node and doesn't condition on the observed input, so the expected utility is over the whole world with that node set, which gives EU_x(a) as the policy with entry a and the others drawn from the prior. For the single-instance question, I'm wondering whether the footnote's "multi-agent only" claim holds, since an agent with imperfect self-knowledge about its behavior on other inputs could still land on a local optimum even without copies.

I'm now considering whether the gym example, where the same decision recurs each week with the same input, shows no gap, while cases with different inputs on different days might show one, which is the multi-instance sense the footnote seems to mean.

I'm now asking how the policy space should be set up: whether policies are deterministic maps from inputs to actions, and whether tie-breaking by a fixed canonical order is what lets separate copies land on the same choice. I'm also turning to what counts as an "input" and whether a different world-model for the same agent would count as a different function.

I'm now asking when the prior P is fixed: whether it's the model as of the start of the problem or as updated by the observations so far, since that decides whether the expectation should condition on the input.

I'm weighing how to present the essay's structure: a brief introduction, then the source's footnotes 7 and 16 quoted, with a note on what they assert and what they leave open. Next I'm setting up the world-model and the action-level FDT equation, before defining the policy-level node that outputs a whole function over inputs. I still need to settle the exact two-step definition of P-FDT and how it feeds into the predictor's reading of the policy.

I'm laying out the rest of the essay: a worked example on transparent Newcomb with the four policies compared, then a section on whether action-level and policy-level FDT can diverge. After that I'm planning a short section on mechanical blackmail, where refusing wins only if the error rate stays below 0.001.

I'm now sketching the essay's remaining sections: open questions about how nodes are identified, what the policy domain covers, which prior applies, how ties are broken, whether stochastic policies are allowed, how the graph is built, and computational cost, followed by a procedure checklist and a short conclusion.

I'm now laying out the coordination example, with two instances of the same function each receiving a different input, and I'm setting the payoffs so that the two instances gain only when they land on matching actions.

I'm setting up the coordination example with the shared payoff and working out which policy the P-FDT argmax selects, which comes out to the pair where the two instances play different actions. I'm then comparing that with what action-level FDT gives when instance 1 intervenes on its own node and treats the other instance's choice as a prior probability q.

I'm checking the coordination case numerically: for instance 1, playing A beats playing B only when the probability that instance 2 plays B exceeds 9/19. Instance 2 faces the mirror-image condition, and with even priors both instances prefer A, which lands on the low-value outcome.

I'm checking the fixed-point structure here: the coordinated pair is a stable belief state under action-level FDT, but that method doesn't select it. The issue is that both instances run the same function, so their outputs are not really independent facts I can intervene on separately, and that's what the action-level formulation seems to overlook.

I'm now stating the theorem formally: the action-level value of each instance is an average, over what the other instances' functions output, of the whole-policy expected utility. That reduction only holds under an independence assumption I'm treating as a modeling choice, so the equality depends on how the graph is set up.

I'm now stating a proposition that if the prior puts all its weight on one profile of the other nodes, the best policy's entry at x has to be among the maximizers of the action-level value. I'm also noting that the coordination example shows this implication doesn't run backwards, and I'm working through when the expected utility splits into a term for x and a term for the other nodes, since in that case the two methods would agree.

I'm checking the one-boxing comparison: whichever choice the empty-box branch makes, one-boxing wins at the full-box node, since the empty-branch payoff is at most 1,000 and the gap from the full box is far larger. So the coordinate-wise choice agrees with the global one. I'm treating the general condition, that a coordinate has a dominant choice for every setting of the others, as my own contribution, and I'm noting it as a reason the paper's examples never exposed a difference between the two methods.

I'm settling the word budget and checking the footnote quotes against the source, keeping the author's apostrophe as it appears in footnote 16.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/b5cbabaf-b2b1-4a92-83b2-9ec5854e8667/call_0/request.json)

[Authoritative raw response](../../../../../../runs/b5cbabaf-b2b1-4a92-83b2-9ec5854e8667/call_0/response.raw) · finish: `stop`

### Visible response

````text
I'm treating this as a choice of policy rather than a single act, as the essay prescribes. Both copies run the same function on the same prior, from the vantage point before either knows whether it is Rowan or Sasha. A policy assigns an action to each possible input, here the Rowan observation and the Sasha observation. Assuming each role is equally likely:

- **Both keep quiet:** 2 years either way, so expected −2.
- **Both send letters:** 4 years either way, so expected −4.
- **One sends, one keeps quiet:** 0 or 5 years, so expected −2.5.

The best policy is to keep quiet on every input. A policy like "defect when I'm Rowan, stay quiet when I'm Sasha" only looks good if I evaluate it after learning my role. That breaks the essay's requirement that every instance optimize from the same prior. Done that way, both copies would end up defecting, which is the worst outcome. Applying the best policy to my actual input, Rowan, gives:

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a prisoner's dilemma between two copies that see different inputs, so under P-FDT I should pick a single policy mapping each input to an action. The policy space pairs an action for Rowan's observation with one for Sasha's, and since neither copy knows which it is, the prior is symmetric. Checking the candidate where both stay quiet, each copy's expected outcome comes to two years.

I'm checking the case where each copy evaluates from its own position: if Rowan evaluates as Rowan, defecting on its own input and cooperating on the other looks best, but Sasha would reason the same way, so the copies would compute different policies. Under the shared prior before observation, which instance is "me" is uncertain, so cooperating on both comes out best.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/b5cbabaf-b2b1-4a92-83b2-9ec5854e8667/call_1/request.json)

[Authoritative raw response](../../../../../../runs/b5cbabaf-b2b1-4a92-83b2-9ec5854e8667/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Reasoning under P-FDT, as the essay interprets it:**

1. **Instantiations.** One decision function runs twice. One copy receives input x_S ("I am Sasha, with a lead on Rowan"). The other receives x_R ("I am Rowan, with a lead on Sasha"). The policy node Π fixes both outputs at once.

2. **Evaluating prior.** Following the essay's proposal 7c, I evaluate policies from the vantage point before the inputs are assigned. From there, I am equally likely to be the instance holding either input. My utility is −(my years).

3. **Policy values** (expected years for me):

   | Policy (on x_S, x_R) | Expected years |
   |---|---|
   | (send, send) | 4 |
   | (quiet, quiet) | **2** |
   | (send, quiet) | ½·0 + ½·5 = 2.5 |
   | (quiet, send) | ½·5 + ½·0 = 2.5 |

   The asymmetric policies look attractive only from inside one input. Under joint evaluation, the instance that ends up holding the "quiet" input pays for them. The different names and leads don't change this. They only distinguish the two inputs; they don't give either copy a reason to choose an asymmetric policy that it would itself rank lower before knowing its input.

4. **Optimal policy.** π* = (quiet, quiet), with a unique maximum of 2 years and no tie-break needed. Applying π* to my actual input x_S gives: keep quiet.

5. **Check against A-FDT.** Sending is not coordinate-dominant once the other instance's output is understood to be the same function's output. This is the kind of case where the policy formulation does real work, and the joint evaluation favors silence.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through the decision under P-FDT: two copies of the same model get different observations, and the same policy is computed for both. I'm weighing the options, sending on both costs 4 years, staying quiet on both costs 2 years, and I'm just starting to look at the mixed case where one sends and the other stays quiet.

I'm working out whether the mixed policy beats the symmetric ones: sending when I'm Sasha and staying quiet when I'm Rowan averages to 2.5 years, which is worse than both staying quiet at 2. So quiet on every input comes out ahead. Since both copies run the same function, I'm treating the decision as one about the policy itself, and I'm settling on a pass.

```
