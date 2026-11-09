# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Algorithm

## 1. Introduction

Decision theory asks a deceptively simple question: when you consider an option, what do you imagine would happen if you took it? Expected-utility theories agree on how to aggregate value once that imagined scenario is fixed. They disagree about how the scenario should be built.

Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a specific answer. In this essay I call the version formalized in their Equation (4) **A-FDT**, for "action functional decision theory." The name marks that Equation (4) maximizes over *actions*. The authors say they actually prefer a variant that maximizes over *policies*, which are maps from observations to actions (their footnotes 7 and 16). Their slogan is that the agent should treat her decision as the output of a fixed mathematical function and ask "Which output of this very function would yield the best outcome?"

This essay has four aims:

1. state Equation (4) precisely;
2. explain how A-FDT builds its counterfactuals;
3. work through the paper's examples, correcting some arithmetic slips along the way;
4. identify what the paper leaves undetermined and propose an operational reading.

I mark my own proposals explicitly as such.

## 2. The common frame: expected utility with a free "→"

The paper follows Gibbard and Harper and Joyce. All three theories it discusses maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\, \mathcal U(o_j),$$

where $x$ is the observation history. The connective "$\hookrightarrow$" is a free parameter. In Joyce's words, the theories disagree "about the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model $M$ and, for each candidate action $a$, builds a *hypothetical* $M^{a\hookrightarrow}$. The paper calls these "decision-theoretic instruments constructed from beliefs," not beliefs. The three theories construct hypotheticals as follows.

- **Evidential decision theory (EDT)** conditions:
 $$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a).$$
- **Causal decision theory (CDT)** performs a Pearl intervention on the physical action node and conditions on observations:
 $$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x).$$
- **A-FDT**, Equation (4):
 $$\boxed{\;\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A} \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;}$$

## 3. Unpacking Equation (4)

### 3.1 The world-model

$P$ is a probability distribution over variables, and $G$ is a directed graph over them. Unlike a causal graph, $G$ contains nodes for **logical facts**, in particular the output of the A-FDT algorithm itself on particular inputs. The paper describes these as variables "representing the outputs of different mathematical functions." Edges from such a node point to every physical or computational process whose behaviour *subjunctively depends* on that output. That includes:

- the agent's own body;
- a twin running the same reasoning;
- a predictor whose model of the agent computes the same function.

### 3.2 The intervention node

$\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable whose *name* is determined by the actual inputs. The underline denotes dequoting. The agent intervenes on "what this very algorithm outputs on these very inputs." The paper argues that the self-reference is harmless: one needs a *variable representing* the output, not its value, and Kleene's recursion theorem ("quining") guarantees that such self-representing structures exist.

### 3.3 The surgery

$\mathtt{do}$ is Pearl's operator. Set the node, cut its incoming edges, recompute everything downstream, and leave everything else at its prior distribution. Downstream of the logical node, this changes:

- the agent's action;
- the predictor's prediction;
- the twin's move.

Upstream and sideways variables, such as a lesion or a termite infestation, keep their prior probabilities.

### 3.4 Observations are not conditioned on

This is the formally striking feature of Equation (4). The paper states it directly: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." When $x$ becomes $y$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead. Her observation tells her *which instance of the function she is*, not which worlds to throw away.

### 3.5 The guiding analogy

The paper's summary: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT intervenes on the *token* action. A-FDT intervenes on the *type*, meaning the logical output that every faithful implementation shares.

### 3.6 When the theories agree

From the definitions, the paper notes that if every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from the algorithm node), then

$$\mathbb E[V\mid a] = \mathbb E[V\mid\mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)].$$

All three theories then coincide. Divergence requires predictors, copies, or similar dependence that is not causal.

## 4. Subjunctive dependence

The informal criterion is this: when two physical systems compute the same function, their behaviour subjunctively depends on that function. The paper's image is two working calculators computing $6288+1048$, which agree without causal contact. Causal dependence is a special case, illustrated by a scribe copying a calculator's output. Mere correlation, such as two calculators that happen to be pink, does not count.

The theory's central assumption, in the paper's words, is that the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

Because a function's output on a given input is logically necessary, these hypotheticals are *counterpossible*. The paper concedes that we lack an account of counterpossibles. It sidesteps the problem by requiring the dependence structure to be supplied in $G$, just as CDT requires a causal graph. The authors call deducing such graphs "perhaps the largest open problem in the study of functional decision theory." This is a real gap. A-FDT is only as determinate as the graph you give it. In what follows I treat $G$ as given and accurate, as the paper does.

## 5. Worked examples

I use the paper's setups: utilities in dollars, a predictor that is 99% accurate unless stated otherwise, and "Fiona" for the A-FDT agent where the paper uses her.

### 5.1 Psychological Twin Prisoner's Dilemma

Both twins' moves are children of the same node $\textsc{fdt}$.

- $\mathtt{do}(\textsc{fdt}=\textit{cooperate})$ yields $(C,C)$, worth \$1,000,000.
- $\mathtt{do}(\textsc{fdt}=\textit{defect})$ yields $(D,D)$, worth \$1,000.

A-FDT cooperates. CDT holds the twin's move fixed, so defection dominates, and CDT defects.

### 5.2 Newcomb's problem

The graph has $\textsc{fdt}\to\textsc{Act}$ and $\textsc{fdt}\to\textsc{Prediction}$, with $\textsc{Accurate}\to\textsc{Prediction}$ and $\textsc{Prediction}\to\textsc{Box B}$.

| Intervention | $P(\text{full})$ | Expected value |
|---|---|---|
| $\mathtt{do}(\textsc{fdt}=\textit{onebox})$ | 0.99 | $0.99\cdot 10^6 = \$990{,}000$ |
| $\mathtt{do}(\textsc{fdt}=\textit{twobox})$ | 0.01 | $0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = \$11{,}000$ |

A-FDT one-boxes. (The paper's EDT paragraph reports \$999,000 for one-boxing, which appears to be a typo for \$990,000; its A-FDT paragraph has the right figure.)

The paper anticipates an objection: if Fiona is confident the box is full, why not two-box? The reply is that two-boxing *in her hypothetical* requires the algorithm to output *twobox*. That change propagates to the prediction. There is no retrocausation, only a shared logical antecedent.

### 5.3 Smoking lesion

Here the lesion is a common cause of the agent's preferences and of cancer. Cancer has no edge from any $\textsc{fdt}$ node. The paper models the lesion as determining which utility function, and so which algorithm instance, controls $\textsc{Act}$:

$$\textsc{Act}(\textit{lesion},s,r)=s,\qquad \textsc{Act}(\textit{nolesion},s,r)=r,$$

where $s$ and $r$ are the outputs of the two instances.

Intervening on the instance $s$ leaves $P(\textit{lesion})=p$ unchanged. Smoking therefore beats refraining by exactly $p\cdot\$1{,}000$, and A-FDT smokes. EDT refrains, while CDT and A-FDT both smoke.

### 5.4 Transparent Newcomb

Both boxes are transparent, and Fiona sees box B full. Her graph has two algorithm nodes, $\textsc{fdt}(\cdot,\textit{full})$ and $\textsc{fdt}(\cdot,\textit{empty})$. $\textsc{Prediction}$ determines which observation occurs, and therefore which node controls the action. Fiona intervenes on the *full* node. Let $q$ be her prior that the *empty* instance two-boxes. The paper notes that the correct value is $q=1$, but the answer does not depend on it.

$$\text{onebox}: 0.99\cdot 10^6 + 0.01\cdot q\cdot 1{,}000 = 990{,}000 + 10q,$$
$$\text{twobox}: 0.01\cdot 1{,}001{,}000 + 0.99\cdot q\cdot 1{,}000 = 10{,}010 + 990q.$$

The paper prints the second value as "\$110,00". The figure above is the corrected arithmetic. Either way, A-FDT one-boxes while *looking at* a full box. CDT and EDT both two-box, so in the actual world they face empty boxes. The paper argues that this is structurally identical to paying the driver in Parfit's hitchhiker.

### 5.5 Mechanical blackmail with an imperfect predictor

A blackmailer runs a program costing the agent \$1,000,000 unless she pays \$1,000. The blackmailer launches it only if she predicts the agent will pay. Let $\varepsilon$ be the probability that she wrongly predicts a refuser will pay. Intervening on $\textsc{fdt}(\cdot,\textit{blackmail})$:

- **pay:** always blackmailed, expected loss $\$1{,}000$;
- **refuse:** blackmailed with probability $\varepsilon$, expected loss $\varepsilon\cdot 10^6$.

A-FDT refuses iff $\varepsilon < 0.001$. With the paper's $\varepsilon = 0.0009$, the expected loss from refusing is \$900, so Fiona refuses, *even while holding the letter*. Above the threshold she pays.

(The paper's second example is "0.011%", which is $1.1\times10^{-4}$. That figure lies below the threshold, so on my calculation it gives refusal, not payment. I take this to be a slip, presumably for something like 0.11%. The threshold derivation above is mine.)

### 5.6 XOR blackmail

A letter arrives iff exactly one of the following holds: (i) no termites and you would pay; (ii) termites and you would not pay. Infestation is upstream of the predictor and has no edge from $\textsc{fdt}$. Intervening on the *letter* node changes whether the letter is sent, but not the termites. So paying only costs \$1,000. A-FDT refuses, and so does CDT. EDT pays, because conditioning on paying sends $P(\textit{termites})$ to 0.

## 6. A procedure for unfamiliar cases

Combining the source with Pearl semantics, an analyst can apply A-FDT as follows. Steps 1–4 are the paper's method. The explicit rules in steps 2, 5 and 6 are my systematization.

1. **List the instances.** Identify every place the agent's algorithm is computed: the agent herself, copies, simulations, and predictors' models. For each observation history $y$ the agent might receive, create a node $\textsc{fdt}(\underline P,\underline G,\underline y)$.
2. **Draw subjunctive edges.**
   - Add an edge from each such node to each process that faithfully computes or models it.
   - Represent imperfection with independent noise nodes, as $\textsc{Accurate}$ does in Newcomb.
   - Draw no edge to merely correlated variables, such as lesions or genes. The test I suggest is whether the variable's value is produced by *evaluating* the agent's function or a model of it.
3. **Route observations structurally.** Make the observation a function of upstream variables, and let it select which $\textsc{fdt}$ node drives $\textsc{Act}$.
4. **Intervene on the actual node.** Do not condition on $x$. For each $a$, compute $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}(\cdot,x)=a))$ and take the argmax.
5. **Handle the other instances.** Leave the $\textsc{fdt}$ nodes for other observations at their prior distributions. This follows the paper's treatment of $q$. The paper stresses that the conclusion is insensitive to $q$ in its examples, but that need not hold in general (see §7).
6. **Break ties.** The source says nothing about ties. Any fixed rule works for analysis; a canonical ordering is the simplest choice.

## 7. Open questions and interpretive choices

### 7.1 What is $P$?

In Equation (4), $\textsc{Obs}=x$ does not appear on the right-hand side. If $P$ were the posterior after observing $x$, then in transparent Newcomb $P(\textit{full})$ would be 1, and the computation in §5.4 could not deliver one-boxing. The paper's numbers require $P$ to be the agent's **prior**, or problem-level, model, in which the observation is still uncertain.

The paper's transparent-Newcomb display writes $\mathbb E(V\mid\mathtt{do}(\ldots=a, \textsc{Obs}=\textit{full})$. That stray $\textsc{Obs}$ clashes with Equation (4). Since the paper's own calculation does not condition, I read it as a notational slip. My operational interpretation is that **$P$ is a prior over the whole problem, including the observation process, and $x$ serves only to select the intervention node.** This interpretation also matches the paper's footnote on Updateless Decision Theory as an early variant. That footnote contrasts it with Timeless Decision Theory, which both conditions and switches nodes, a "double update" that "proves harmful in practice."

### 7.2 Action versus policy

A-FDT chooses one action at one node and holds the other instances at prior beliefs. The paper's preferred theory picks a whole policy, choosing all $\textsc{fdt}(\cdot,y)$ jointly. The paper claims the difference "only matters in multi-agent dilemmas so far as we can tell."

Here is where A-FDT can come apart from that alternative, in my analysis. If the payoff at the actual node depends on what *other* instances do, and the agent's prior about those instances is miscalibrated, then holding the others fixed can select an action that is not part of any jointly optimal policy. Coordination among instances is the clearest case. The policy version avoids this by optimizing jointly. When you apply A-FDT, you should therefore check that your priors on the other instances are consistent with A-FDT's own outputs. That amounts to a fixed-point condition, which the paper does not state.

### 7.3 Constructing $G$

The paper is explicit that no counterpart to Pearl's causal discovery exists for subjunctive dependence. Hard cases include:

- partial similarity, as with a "twin" who reasons somewhat differently;
- a predictor that models a related but different algorithm;
- the gym example, where today's and next week's decisions are "similar."

For all of these, A-FDT's verdict depends on judgments the formalism does not supply. A natural graded proposal, which is my own and not the paper's, is to model a partly similar process as a mixture: with probability $\rho$ it copies the $\textsc{fdt}$ node, and otherwise it follows an independent distribution. This preserves Pearl semantics, but the source does not license any particular $\rho$.

### 7.4 Fairness

The paper claims superiority on "fair problems," meaning problems where outcomes depend only on the agent's behaviour in the dilemma. It concedes that it has no formal definition of fairness. A problem that punishes anyone matching a copy of Fiona defeats A-FDT by construction.

## 8. Philosophical motivation in brief

The paper offers three arguments for A-FDT's counterintuitive verdicts:

- **Precommitment:** CDT and EDT agents would pay to bind themselves to A-FDT's choices.
- **Value of information:** A-FDT never pays to avoid information, whereas an EDT agent would blindfold herself in transparent Newcomb.
- **Utility:** A-FDT agents end up richer. The paper treats this as the argument that gives the other two their force.

The paper also reinterprets dominance. Every way of building hypotheticals induces its own dominance relation. CDT's "two-boxing dominates" is therefore "merely a restatement of CDT's method," not a neutral criterion. On the charge that it is odd to "control" a logical fact, the paper answers with parity: a deterministic CDT agent also imagines its single physically possible action varying.

## 9. Conclusion

A-FDT is Pearl-style expected utility maximization in which the surgery targets the logical node "what my decision algorithm outputs on this input," not the physical action. Observations select which node is intervened on rather than being conditioned on. The result is a single rule that:

- one-boxes in Newcomb's problem, opaque or transparent;
- cooperates with a twin;
- smokes despite the lesion;
- pays in Parfit's desert;
- refuses both kinds of blackmail.

To apply it, you need a prior model that includes the observation process, and a graph of subjunctive dependencies, which is the part the paper admits it cannot yet derive. Given those, the computation is as mechanical as CDT's. The theory's real open problems lie upstream of Equation (4):

- what counts as computing "the same function";
- how to reason counterpossibly;
- when acting node by node, as A-FDT does, falls short of choosing a whole policy.

**Reference.** E. Yudkowsky and N. Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (v2).