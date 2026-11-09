# Choosing the Function, Not the Act: An Essay on Policy Functional Decision Theory (P-FDT)

## 1. The passage and the question it raises

Yudkowsky and Soares's paper "Functional Decision Theory" (2017) spends nearly all of its length on a theory that evaluates *actions*. Two footnotes say that this is not the authors' preferred version. The more detailed one, footnote 16, reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(−) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Footnote 7 adds that "agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

I call the theory these footnotes describe **policy functional decision theory (P-FDT)**. The action-level theory in the paper's main text, its equation (4), I call **action-FDT**. My aim is to reconstruct P-FDT precisely enough that it can be applied to new cases.

The essay has four parts:
- I separate what the source says from what I add.
- I show by example why the policy/action distinction can matter.
- I prove a small proposition relating the two theories.
- I flag the places where the footnote leaves real choices open.

## 2. Background: what action-FDT does

All the theories in the paper are expected-utility maximizers. They differ only in how they construct the hypothetical "what if I chose $a$?"

The source's FDT agent has a world-model $(P, G)$:
- $P$ is a probability distribution over variables.
- $G$ is a graph encoding dependencies. These include causal dependencies, and also *subjunctive* ones: logical or computational dependence between systems that compute the same function.

Some variables in $P$ stand for the outputs of mathematical functions. In particular, $\mathsf{fdt}(\underline P, \underline G, \underline x)$ denotes the output of the FDT algorithm itself on inputs $(P, G, x)$, where $x$ is the observation history. The source's equation (4) is

$$
\mathrm{FDT}(P,G,x) \;=\; \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \,\big|\, \mathtt{do}(\mathsf{fdt}(\underline P,\underline G,\underline x)=a)\big).
$$

Two features matter for what follows.

**Intervening on the function, not the body.** Every system whose behavior subjunctively depends on that function changes in the hypothetical. This includes the agent's body, a twin, and a predictor's model of the agent.

**Observations change the intervention point, not the distribution.** The source says that "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." In the transparent Newcomb problem, Fiona's graph contains two nodes, $\mathsf{fdt}(\cdot,\cdot,\textit{full})$ and $\mathsf{fdt}(\cdot,\cdot,\textit{empty})$. The predictor's prediction depends on the first. The observation she actually receives determines which node controls her act.

There is a consequence the source mentions but plays down. When action-FDT intervenes on $\mathsf{fdt}(x)$, the *other* observation-indexed nodes $\mathsf{fdt}(y)$, $y\neq x$, are not intervened on. They keep whatever distribution $P$ assigns them. In the source's examples this prior hardly matters: in the transparent Newcomb calculation, the authors note that Fiona's uncertainty $q$ about her empty-box behavior "doesn't matter." The footnotes suggest that in some multi-agent problems it does matter, and that this is why policies are preferred.

## 3. Defining P-FDT

### 3.1 The source's claim

The footnote commits P-FDT to three things:
1. The intervention is on a node representing the decision function as a whole, written "FDT(−)".
2. The value set in that node is a policy, a map from inputs to actions. Footnote 7 says the inputs are observations.
3. The agent then "applies her inputs" to the chosen policy to get her act.

### 3.2 A formalization (my construction)

Let $\mathcal X$ be the set of possible observation histories relevant to the problem, and let $\Pi = \mathcal A^{\mathcal X}$ be the set of deterministic policies.

Start from the action-FDT graph $G$, in which there are nodes $\mathsf{fdt}(\underline P,\underline G,\underline y)$ for each $y\in\mathcal X$. Build a new graph $G^\Pi$ in three steps:

- **Merge** all of these nodes into a single node $\Phi = \mathsf{fdt}(\underline P, \underline G)$ taking values in $\Pi$.
- **Redirect** every edge $\mathsf{fdt}(y)\to Z$ to an edge $\Phi \to Z$. Wherever $Z$ formerly read the value of $\mathsf{fdt}(y)$, it now reads the coordinate $\Phi(y)$.
- **Leave alone** every other node and every other structural equation.

The redirect step covers every system that depends on the function: the agent's own body under various observations, a predictor's simulation of what she would do upon seeing $y$, a copy of her in another room.

Then define

$$
\mathrm{EU}(\pi) \;=\; \mathbb E\big(V \,\big|\, \mathtt{do}(\Phi = \pi)\big), \qquad
\pi^\ast \in \arg\max_{\pi\in\Pi}\mathrm{EU}(\pi), \qquad
\text{P-FDT}(P,G,x) \;=\; \pi^\ast(x).
$$

In words, P-FDT asks: *"If this decision function were the function that maps each possible input to the action this policy specifies, what would the whole world look like, and how good would that be?"* It then executes the best policy at its actual input.

### 3.3 The key interpretive choice: no conditioning on $x$

The expectation defining $\mathrm{EU}(\pi)$ does not condition on $\textit{Obs}=x$. I take this to be the footnote's meaning, for two reasons:
- It says the agent chooses a policy and *then* "applies her inputs," so inputs enter only through evaluation of the policy.
- It matches the source's action-FDT equation (4), which also does not condition on the observation.

Conditioning would also double-count evidence. The source makes exactly this complaint, in an internal note, about Timeless Decision Theory, which "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

P-FDT is therefore close in spirit to what the source calls Wei Dai's "Updateless Decision Theory." I make no claim about the details of that theory.

## 4. P-FDT on the source's single-agent examples

### 4.1 Transparent Newcomb

A policy is a pair $(\pi(\textit{full}), \pi(\textit{empty}))$ with entries 1 (one-box) or 2 (two-box). The predictor, accurate with probability $0.99$, fills box B iff she predicts $\pi(\textit{full})=1$.

| Policy (full, empty) | Accurate (0.99) | Inaccurate (0.01) | EU |
|---|---|---|---|
| (1, 2) | full, take 1 → \$1,000,000 | empty, take 2 → \$1,000 | \$990,010 |
| (1, 1) | full → \$1,000,000 | empty, take 1 → \$0 | \$990,000 |
| (2, 2) | empty, take 2 → \$1,000 | full, take 2 → \$1,001,000 | \$11,000 |
| (2, 1) | empty, take 1 → \$0 | full, take 2 → \$1,001,000 | \$10,010 |

The optimum is "one-box on full, two-box on empty." Applied to the input *full*, it yields one-boxing, which is the source's answer.

The source's action-FDT calculation gives $\$990{,}000 + 0.01q\cdot\$1{,}000$ for one-boxing, where $q$ is Fiona's credence that she two-boxes upon seeing an empty box. This is just a row of the table averaged over beliefs about the other coordinate. P-FDT sets $q$ by optimization instead of by prior.

### 4.2 Mechanical blackmail

Let the blackmailer wrongly predict "pay" with probability $\varepsilon$. Only the coordinate $\pi(\textit{blackmail})$ matters:
- Paying gives $\mathrm{EU} = -\$1{,}000$, since the agent is blackmailed essentially always and pays.
- Refusing gives $\mathrm{EU} = -\varepsilon\cdot\$1{,}000{,}000$.

So P-FDT refuses iff $\varepsilon < 0.001$. With the source's $\varepsilon = 0.0009$, refusal costs \$900 in expectation and beats paying.

The source also says that at an error rate of "0.011%" Fiona pays. Read literally, that rate gives an expected loss of \$110 from refusing, so refusal would still win. The intended figure is presumably 0.11%, which is above the threshold. My threshold calculation is my own, and it agrees with the source's qualitative claim.

### 4.3 Parfit's hitchhiker

This has the same structure as transparent Newcomb. The policy "pay \$1,000 in the city" makes rescue 99% likely and beats "don't pay." P-FDT pays upon arriving.

In all three cases, P-FDT and action-FDT agree. That is consistent with the footnote's claim that the difference does not show up in the paper's examples. The next section explains when they agree and when they come apart.

## 5. When policies matter

### 5.1 A coordination problem among copies

Here is an example of my own. Two exact copies of an agent, both running the same function on the same $(P,G)$, are placed in rooms labeled $\alpha$ and $\beta$. Each sees only its room's label, so the inputs differ. Each chooses A or B. Both receive:
- 10 if both choose A,
- 1 if both choose B,
- 0 otherwise.

**Action-FDT.** The copy in room $\alpha$ intervenes on $\mathsf{fdt}(\alpha)$. The node $\mathsf{fdt}(\beta)$ is a different logical variable, and the graph has no edge between them. So the other copy's behavior is held at the prior. Writing $r = P(\mathsf{fdt}(\beta)=A)$:

$$
\mathbb E(V\mid \mathtt{do}(\mathsf{fdt}(\alpha)=A)) = 10r,\qquad \mathbb E(V\mid \mathtt{do}(\mathsf{fdt}(\alpha)=B)) = 1-r.
$$

The copy chooses A iff $r > 1/11$. Suppose both copies start out pessimistic, each believing the other will probably choose B. Then both choose B, and the pessimism confirms itself.

Action-FDT's verdict thus depends on a self-prediction prior. This is the same kind of dependence the source criticizes in EDT, whose choices "are at the mercy of her priors."

**P-FDT.** P-FDT evaluates the four policies $(\pi(\alpha),\pi(\beta))$ directly, with utilities 10, 1, 0, 0. It chooses $(A,A)$. Both copies run the same computation, reach the same $\pi^\ast$, and apply their own labels. No prior over the counterpart is needed, because the counterpart's behavior is part of what is chosen.

### 5.2 Anti-coordination and the need for fixed tie-breaking

Change the payoff to 10 if the choices *differ* and 0 otherwise. Only P-FDT can exploit the asymmetry of labels: the policies $(A,B)$ and $(B,A)$ both earn 10.

But they tie. If each copy broke the tie independently, the copies could miscoordinate. P-FDT therefore needs a tie-breaking rule that is part of the function, such as a fixed ordering on $\Pi$. Then every instance resolves the tie the same way. The footnote does not mention this. I treat it as a required completion, discussed further in §7.

### 5.3 Why the source says "multi-agent"

These examples suggest the precise condition. The two theories diverge when **several instances of the same decision function receive different inputs and their outputs jointly determine the payoff.**

Copies, twins, and simulations are the natural cases, which explains the footnote's "multi-agent." By my reading, though, a single agent whose own future or past selves are relevant instances with different observations falls under the same condition. The source's gym example, where an agent "coordinate[s] with herself over time," points in this direction. Applying the footnote's claim there is my extension, not the source's.

## 6. A proposition relating the two theories

Fix $(P,G)$ and the merged graph $G^\Pi$. Suppose the action-FDT agent's beliefs about the off-input nodes are a point mass on some policy $\pi$, meaning $P(\mathsf{fdt}(y)=\pi(y))=1$ for all $y \neq x$, and that these nodes are otherwise independent of the intervened node. For any $a\in\mathcal A$, write $\pi[x\mapsto a]$ for the policy that agrees with $\pi$ except that it sends $x$ to $a$.

**Lemma.** Under these assumptions, intervening on $\mathsf{fdt}(x)$ is the same as intervening on $\Phi$:

$$
\mathbb E\big(V\mid \mathtt{do}(\mathsf{fdt}(x)=a)\big) = \mathrm{EU}(\pi[x\mapsto a]).
$$

*Reason:* in $G$, every downstream node reads $\mathsf{fdt}(x)=a$ together with $\mathsf{fdt}(y)=\pi(y)$ for $y \ne x$. In $G^\Pi$, every downstream node reads exactly those coordinates of $\pi[x\mapsto a]$.

**Proposition.** Let $\pi^\ast$ be P-FDT-optimal, and suppose the action-FDT agent's beliefs about $\mathsf{fdt}(y)$, $y\neq x$, are concentrated on $\pi^\ast$. Then $\pi^\ast(x)$ is an action-FDT-optimal choice at $x$. In other words, $\pi^\ast$ is a self-consistent profile for action-FDT.

*Proof.* By the lemma, $\mathbb E(V\mid \mathtt{do}(\mathsf{fdt}(x)=a)) = \mathrm{EU}(\pi^\ast[x\mapsto a]) \le \mathrm{EU}(\pi^\ast)$. Equality holds at $a = \pi^\ast(x)$. ∎

**The converse fails.** A policy can be stable under every single-coordinate deviation without being globally optimal. $(B,B)$ in §5.1 is such a policy: changing one coordinate drops the payoff from 1 to 0, yet $(A,A)$ earns 10.

So action-FDT is coordinate-wise optimization over $\Pi$. P-FDT is joint optimization. They coincide when:
- the payoff is separable across inputs, which holds in the source's single-agent examples because only one input-node bears on what happens at each observation; or
- the agent's self-beliefs happen to sit at the global optimum.

This is my mathematical gloss on the footnote's empirical-sounding "so far as we can tell."

## 7. Questions the footnote leaves open, and proposed answers

### 7.1 Which inputs, and which prior?

The footnote says "inputs," and footnote 7 says "observations." I take $\mathcal X$ to be observation histories.

Which $P$ evaluates policies is less clear. In equation (4), $P$ is fixed and $x$ varies. For a long-lived agent, this raises the question of how far back the "prior" goes.

**Proposal.** Use the epistemic state that all relevant instances of the function share. That is the state the predictors and copies in the problem are modeling. In a stylized problem, it is simply the model specified before observations. Going further back than the dependencies require adds nothing. Not going back far enough breaks the coupling with predictors who model the earlier state.

### 7.2 The size of $\Pi$

$|\Pi| = |\mathcal A|^{|\mathcal X|}$, which is infinite when $\mathcal X$ is countably infinite. The maximum may then not be attained.

**Proposal.**
- Restrict $\mathcal X$ to the observations the problem distinguishes, as in the two-input examples above.
- In general, accept an $\epsilon$-optimal policy.
- Note that when the payoff is separable across inputs, the joint optimum can be computed coordinate by coordinate.

### 7.3 Ties

As §5.2 showed, coordination among instances requires a fixed rule for selecting from $\arg\max$, for example a canonical ordering on $\Pi$. A rule like "choose any maximizer" is not a function and cannot be relied on to coordinate.

### 7.4 Inputs the policy makes unreachable

Suppose that under $\pi^\ast$, some input $x$ has probability zero. With a perfect predictor in transparent Newcomb, $\pi^\ast$ means the agent never sees an empty box. Then $\mathrm{EU}$ does not depend on $\pi(x)$, so P-FDT is silent about what to do there.

**Proposal.** Use a lexicographic refinement:
1. Among optimal policies, prefer those that are also optimal when every input is reached with a small probability $\delta$ (for example, through predictor error).
2. Take the limit as $\delta\to 0$.

With an imperfect predictor, as in the source's 99% case, the issue does not arise: the empty-box column in §4.1 already determines the second coordinate.

### 7.5 Randomized policies

The footnote speaks only of maps to actions. Whether mixed policies $\mathcal X\to\Delta(\mathcal A)$ should be allowed depends on the graph:
- If a randomization source is modeled as independent of predictors, the source's "truly random" coin in Death in Damascus, then randomizing changes outcomes. Mixed policies should be in the choice set: the coin yields a 50% survival chance, worth far more than its \$1 price.
- If predictors can predict the randomness, as with pseudorandomness, then the randomization is just a deterministic policy in disguise.

I would let $G$ decide this rather than the decision rule.

### 7.6 Which instances get merged?

My construction merges nodes indexed by the *same* $(P,G)$. A predictor who models the agent with a slightly different model is computing a different function. Whether that predictor's node is linked to $\Phi$ is a fact about subjunctive dependence, and the source treats such facts as inputs supplied by $G$. P-FDT inherits the source's main open problem unchanged: how to learn the structure of subjunctive dependence, which the source calls "perhaps the largest open problem in the study of functional decision theory."

## 8. How to apply P-FDT to a new case

1. **Model.** Write a joint model $(P,G)$ of the world. Mark every place where the outcome depends on what the decision function would output on some input: your own act, predictions of it, copies of it.
2. **Enumerate inputs.** List the inputs $\mathcal X$ that distinguish those places.
3. **Merge.** Replace all of those places with a single policy node $\Phi$. Each place reads its own coordinate of $\Phi$.
4. **Evaluate.** For each $\pi \in \Pi$, compute $\mathrm{EU}(\pi) = \mathbb E(V\mid\mathtt{do}(\Phi=\pi))$, without conditioning on your actual observation. Off-path causal structure stays as $P$ describes it, as in the smoking lesion problem, where the lesion does not depend on the policy and smoking wins.
5. **Select.** Choose the optimal policy, breaking ties by the fixed ordering and refining for unreachable inputs as in §7.4.
6. **Act.** Look at your actual input $x$ and do $\pi^\ast(x)$.

One more example shows the procedure at work. Take the source's voting problem and vary it: the ten voters are copies who each see a different district label. Each copy can intervene only on its own label's node. Without policy-level reasoning, a copy that doubts the others' labels will vote can rationally abstain, and the doubt confirms itself as in §5.1. P-FDT chooses "vote under every label" as a single policy, so all ten vote and collect the \$1,000,000.

## 9. Why choose policies? The philosophical motivation

The source's central motivation is that the right question is "Which output of this very function would yield the best outcome?" P-FDT takes "output" in the most complete sense.

A function is not a single answer. It is the whole table of answers on all inputs. Predictors and copies are related to the agent through that table, not through one entry of it. Intervening on one entry while leaving the rest at a prior treats part of one's own function as an external fact, which is a small version of the mistake the source attributes to CDT: holding fixed something that in fact depends on one's choice.

P-FDT also strengthens the source's "argument from precommitment." The source says FDT agents "simply act as they would have ideally precommitted to act." An ideal precommitment is a contingency plan, that is, a policy. P-FDT makes this literal: the agent computes the best plan and follows it at whatever input she receives.

The source's "global perspective" asks "What would the entire universe look like if the FDT algorithm behaved differently?" P-FDT answers that question for every input at once.

## 10. Conclusion

Footnote 16 states that the authors' preferred FDT intervenes on the decision function to choose "not an action but a *policy*," which the agent then applies to her input.

I formalized this as P-FDT: merge all observation-indexed function nodes into one policy node, maximize expected utility over policies by intervention without conditioning on the actual observation, and execute the chosen policy at the actual input. On the source's examples (transparent Newcomb, Parfit's hitchhiker, mechanical blackmail), P-FDT agrees with action-FDT.

A simple proposition explains the agreement and its limits. P-FDT optima are always self-consistent points of action-FDT, but action-FDT can also settle on worse self-consistent points. The difference appears when multiple instances of the function receive different inputs and must coordinate, which is my precise reading of the footnote's "multi-agent dilemmas."

The footnote leaves several choices open: which prior evaluates policies, how to break ties, what to do at unreachable inputs, whether to allow randomization, and which dependencies to merge. I proposed operational answers to each. The deepest open problem, learning the subjunctive dependence graph, is the same for P-FDT as for FDT in the source.

## References

- Yudkowsky, E., and Soares, N. (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060. Footnotes 7 and 16, equation (4), and §§5–9.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Dai, W. (2009). "Towards a New Decision Theory." *Less Wrong*.