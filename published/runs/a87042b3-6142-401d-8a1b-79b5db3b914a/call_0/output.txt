# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. The idea in one paragraph

The source paper (Yudkowsky and Soares, "Functional Decision Theory") develops its main equations for actions. It says in footnotes 7 and 16 that the authors' *preferred* formalization works with policies. I will call that policy-selecting version **P-FDT**. Footnote 16 is my primary source. It says the preferred formulation "intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action." It adds that "the difference only matters in multi-agent dilemmas so far as we can tell." Footnote 7 is similar: agents "iterate over *policies* (mappings from observations to actions) rather than actions."

Everything below that goes beyond these sentences is my interpretation. I flag the places where I extend the source.

## 2. From actions to policies

The paper's action-based rule is

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V \mid do(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model standing for the output of the algorithm on input $(P,G,x)$. A new observation $x$ does not make the agent condition. It changes *which* variable she intervenes on. The paper's examples show this: $\mathrm{fdt}(P,G,\text{full})$ and $\mathrm{fdt}(P,G,\text{empty})$ are distinct nodes in Fiona's transparent-Newcomb graph.

A P-FDT agent works with a set $\Pi$ of policies $\pi:\mathcal X\to\mathcal A$, where $\mathcal X$ is the set of possible observations. The agent treats one variable as the output of her decision function, $\Pi^\ast=\mathrm{fdt}(\underline P,\underline G)$, which takes values in $\Pi$. Observations are not an argument of the node. The rule I propose is:

1. Build the hypothetical $M^{\pi\hookrightarrow}$ for each $\pi\in\Pi$ by $do(\Pi^\ast=\pi)$.
2. Compute $V_\pi=\mathbb E[V\mid do(\Pi^\ast=\pi)]$. The expectation is over *all* observation branches, weighted by the probabilities those branches have *under the intervention*.
3. Select $\pi^\ast=\arg\max_\pi V_\pi$.
4. Apply $\pi^\ast$ to the actual observation $x$ and execute $a=\pi^\ast(x)$.

Step 4 is what footnote 16 describes ("to which the agent then applies her inputs"). Step 2 is my formalization. Written out:

$$V_\pi=\sum_{x}\ P(\Obs=x\mid do(\Pi^\ast=\pi))\ \mathbb E\big[V\mid do(\Pi^\ast=\pi),\Obs=x\big].$$

The key difference from the action-based form is that the probability of the observation is itself downstream of the intervention. In the action-based form, intervening on $\mathrm{fdt}(\cdot,x)$ for the one observed $x$ gives the impression that $x$ is held fixed. The paper handles this in the transparent Newcomb case by letting $\Act$ be controlled by whichever $\mathrm{fdt}$ node matches the observation, and by letting the prediction determine which observation occurs. P-FDT builds this in from the start.

## 3. Why the difference "only matters in multi-agent dilemmas"

The source's claim is hedged ("so far as we can tell"). Here is a reconstruction of why it is plausible.

Suppose the dependencies of the world on the agent are *only* of the form "environment depends on the agent's output on the observation actually received." Then the action-based and policy-based rules agree. In every worked example in the paper (Newcomb, transparent Newcomb, blackmail, XOR blackmail, Parfit) the action-based rule already reproduces policy-level behavior. It does so by letting a predictor's prediction select which $\mathrm{fdt}$ node controls $\Act$. The prediction in those graphs depends on the agent's behavior at *other* observations, and that is exactly what a policy encodes.

Where could the two come apart? Suppose some other agent's behavior depends on *several* of my input–output pairs, or on correlated copies of me that receive different observations. Then intervening on a single observation-indexed node only moves that node, and a copy's behavior on its own input may depend on a different node. A policy-level intervention moves all of them together. This is my reading, not an explicit claim of the source. It is my guess at why the authors mention multi-agent dilemmas.

I can give a concrete case. Two copies of an agent are told "you are Copy 1" or "you are Copy 2" and must coordinate: payoff arrives only if Copy 1 plays X and Copy 2 plays Y. The agent's policy $\pi=(\text{X on 1},\text{Y on 2})$ matters jointly. Evaluating each of her two observation-nodes independently risks evaluating a mix inconsistent with a single function. Intervening on the policy ensures that both copies are evaluated under the same function.

## 4. Counterfactuals and dependencies

P-FDT inherits the paper's dependency treatment, and I restate it for policies.

- **Subjunctive dependence.** Variable $Z$ depends on $\Pi^\ast$ if it would change were the decision function to output a different policy, for example because $Z$ is computed by a predictor or copy that implements or accurately models the function. This includes causal dependence as a special case. The paper's example is a scribe copying a calculator.
- **Statistical correlation alone does not count.** The smoking lesion is correlated with the act but does not depend on $\Pi^\ast$. The lesion node is therefore not downstream of $\Pi^\ast$ and is held fixed.
- **Counterfactual structure.** The intervention is on a *logical* fact. Imagining $\Pi^\ast=\pi'$ when the agent's function in fact outputs $\pi$ is a counterpossible. The source is open about the lack of a theory of counterpossibles. It simply takes the dependency graph $G$ as an input, just as CDT takes a causal graph (footnote 9, and the "largest open problem" discussion).

This is the main source of uncertainty in any application. P-FDT as I have written it is only as determinate as $G$. If two reasonable modelers draw different graphs, they will get different recommendations.

## 5. Worked examples

All payoffs are in dollars, following the source's convention.

**Newcomb.** The policy has no observations, so it reduces to an action. Under $do(\Pi^\ast=\text{one-box})$ the box is full with probability 0.99, so $V=\$990{,}000$ (as in the paper, since $0.99\times\$1{,}000{,}000$). Under two-boxing, $V=\$11{,}000$. One-box.

**Transparent Newcomb.** Policies are maps $\{\text{full},\text{empty}\}\to\{1,2\}$. Let the predictor fill the box iff she predicts $\pi(\text{full})=1$, with accuracy 0.99. Write $\pi=(u,w)$ for the behavior on (full, empty).

- $\pi=(1,2)$: box full with probability 0.99, giving $\$1{,}000{,}000$. Otherwise it is empty and she two-boxes for $\$1{,}000$. $V=0.99(10^6)+0.01(10^3)=\$990{,}010$.
- $\pi=(2,2)$: full only with probability 0.01, giving $\$1{,}001{,}000$. Otherwise $\$1{,}000$. $V=0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000$.

(The paper's own expression for the one-box value, $\$990{,}000+0.01q\cdot\$1{,}000$, is the same computation with $q$ the probability of two-boxing on seeing empty; the $q$-dependence is small.) The best policy has $\pi(\text{full})=1$. Having seen a full box, she one-boxes. This reproduces the paper's verdict. The details of how the observation-dependent behavior in the empty branch matters show up automatically: $\pi(\text{empty})$ is chosen too, and two-boxing there is better.

**Parfit's hitchhiker.** The driver rescues the agent iff she predicts $\pi(\text{city})=\text{pay}$. The policy "pay" yields rescue with probability 0.99, worth about $\$990{,}000-\$990$. The policy "don't pay" yields rescue with probability 0.01. P-FDT pays, and executes this at the ATM.

**Blackmail with an imperfect predictor.** The paper's numbers carry over directly. With error rate 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation, versus a certain \$1,000 for paying. P-FDT refuses. At error rate 0.00011 the comparison flips. The policy-level formulation makes the origin of this clear. It is the whole-policy comparison, including branches where no letter arrives, that decides.

**Smoking lesion.** The paper models this with two utility functions $U_S$, $U_R$ and two decision-function nodes, with the lesion selecting which one controls the act. It is awkward, and the paper itself calls the problem "badly confused." A policy-level reading is straightforward: $\Pi^\ast$ has no downstream path to cancer, so the cancer probability is unchanged across policies, and smoking wins by its direct \$1,000. I do not rely on any more detail than this.

## 6. A decision procedure and its caveats

For a practitioner, I propose the following checklist, which is my own packaging.

1. List the observations $x$ the agent might receive and her available actions. This gives $\Pi$.
2. List every process that computes, predicts, copies, or models the agent's function. These are the nodes with subjunctive dependence.
3. Draw $G$ with $\Pi^\ast$ feeding the agent's action (through the observation), and feeding each dependent process.
4. For each $\pi$, compute $V_\pi$ as in section 2, with observation probabilities moving with $\pi$.
5. Choose the best $\pi$ and apply it to the actual observation.

Three caveats follow.

*Size.* $|\Pi|=|\mathcal A|^{|\mathcal X|}$. The source is explicit that the exact procedure is idealized and that bounded agents would approximate it. I would add that in practice one restricts to the few observation classes that any dependent process can distinguish.

*Ties and degenerate cases.* The source does not say how to break ties among optimal policies. I assume any maximizer is acceptable.

*Imperfect dependence.* The source gives accuracy parameters in its examples but no general account of partial subjunctive dependence. I treat it as a probabilistic edge, with the predictor's output equal to the policy's output with probability equal to its accuracy, as the paper does.

## 7. Relation to other theories

The paper contrasts FDT with causal decision theory (CDT) and evidential decision theory (EDT). It also states that its footnote on earlier variants: Wei Dai's updateless decision theory and Yudkowsky's timeless decision theory. The first is named for apparent lack of updating. The second both conditions on evidence and moves the intervention point, which the authors say is a harmful "double update." P-FDT, as I understand it, is closest in spirit to updateless approaches, since it evaluates whole policies from a standpoint prior to the observation. It differs from timeless decision theory in that it does not condition on the observation. I draw the comparison to the updateless approach only loosely, as the source does not define it.

## 8. Open questions

- **No theory of the dependency graph.** The source says that deducing subjunctive structure from observation is "perhaps the largest open problem."
- **Fairness.** P-FDT's claim to superiority applies to "fair" problems, those that reward or punish agents only for their behavior, not their procedure. The source admits this is not formalized, and footnote 15 gives a copy-of-Fiona counterexample showing it is hard to formalize.
- **Policy versus action in multi-agent settings.** The source says only that it matters there. My reconstruction in section 3 is one candidate explanation. A reader should not treat it as established.

## 9. Conclusion

P-FDT evaluates each policy by imagining the decision function outputting it, letting everything that subjunctively depends on that function change (predictors, copies, the observation itself) and holding everything else fixed. It then applies the best policy to the actual input. This reproduces the source's verdicts: one-box in Newcomb and the transparent variant, pay in Parfit's hitchhiker, refuse blackmail, smoke in the lesion problem. The method is clean given a dependency graph, but the graph itself is the unresolved part of the theory.

## References

- Yudkowsky, E., and Soares, N. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060 (footnotes 7, 9, 15, 16, and Sections 5, 6, 9).
- Joyce, J. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.
- Pearl, J. *Causality*. Cambridge University Press, 2000.