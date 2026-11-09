# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

Action functional decision theory (A-FDT) says: treat your decision as the output of a fixed mathematical function, and ask which output of *that function* would lead to the best world. This essay takes Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," as its formal statement. I use "A-FDT" for that equation, in which the agent selects an *action* for each observation. The paper's footnotes 7 and 16 say the authors' preferred formulation iterates over *policies* (maps from observations to actions), which matters only in some multi-agent problems. I refer to the policy version as a variant and do not develop it.

Everything below is either from the paper or flagged as my own addition.

## 2. Formal definition

The paper presents every expected-utility theory in the form

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),\tag{1}$$

where $x$ is the observation history and "$\hookrightarrow$" is a connective for decision hypotheticals. The paper follows Joyce in holding that theories differ only in what $\hookrightarrow$ means, that is, in the "epistemic perspective."

- EDT: $\hookrightarrow$ is conditioning, $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$ (Eq. 2).
- CDT: $\hookrightarrow$ is Pearl's intervention on the physical action node, $\arg\max_a\mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$ (Eq. 3).
- A-FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \,\Big|\, do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

**Inputs.** $P$ is a probability distribution over the variables of the world-model. $G$ is a graph saying how changing a variable propagates to the others. Crucially, $G$ must encode *subjunctive dependence* (logical, computational, causal, and so on), not just causation. $x$ is the observation.

**The intervened variable.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model representing the output of the A-FDT procedure itself, run on this very model and observation. The underlines mean dequoting: the variable's name is built from the values of $P$, $G$, $x$. The self-reference is harmless. The agent need not know the *value* of $\mathrm{FDT}(P,G,x)$ to have a variable *representing* it, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.

**The operator.** The paper's idealized operator is a "$\mathtt{true}$" that conditions on false logical sentences, but it admits no one knows how to define it. A-FDT sidesteps this by requiring the dependency structure to be supplied as input, as CDT requires a causal graph. Pearl's $do$ is then reused: set the node, then recompute every node downstream of it in $G$ and hold the rest fixed.

**Two differences from CDT.**
1. A-FDT intervenes on the *logical* node for the decision function's output, not the physical act node.
2. A-FDT does not condition on observations. Observing $x$ changes *which* node is intervened on ($\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$). Since the intervention may change what is observed, hypotheticals can include different observations.

**Operational summary.** For each action $a$: (i) set the node $\mathrm{fdt}(P,G,x)$ to $a$; (ii) propagate along $G$ to everything that subjunctively or causally depends on it, including other copies, predictors, and other-observation branches; (iii) compute $\mathbb E[V]$ in that modified model; (iv) output the argmax.

Where the world-model has no correlation between the action and anything except what the action causes, the three theories agree: $\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)]$. They come apart only with predictors, twins, and similar structures.

## 3. Subjunctive dependence

A-FDT is to subjunctive dependence as CDT is to causal dependence. Two systems subjunctively depend on a function when both compute it. A predictor with an accurate model of me, a twin, and a calculator across the world are all instances. Causal dependence is a special case. A scribe copying a calculator's output depends on it subjunctively, since she would write something different if it output something different. Mere statistical correlation is not: two pink calculators do not depend on each other's color.

In Peirce's terms, CDT intervenes on the *token* "my act is $a$," and A-FDT intervenes on the *type*, the function. Because the function's output is logically fixed, the hypotheticals are counterpossible, like imagining $6288+1048\ne 7336$. The paper admits this is the theory's main drawback relative to CDT. It argues the problem is technical, not philosophical: mathematicians reason under logical uncertainty routinely, and A-FDT only needs the narrow question "how would this predictor's output change if my algorithm's output changed?" Imperfect predictors or non-deterministic agents weaken the dependence without eliminating it, and this is represented by probabilities in $P$ (the 0.99 accuracy node).

The paper also considers a variant, FDT′, that varies which decision function is implemented rather than the output. It argues this saves nothing, since predictors of $d$ must still be imagined to predict as if $d$ behaved like $f_n$.

## 4. Worked examples

**Newcomb.** Fiona's graph has a node $\mathrm{fdt}(P,G)$ with arrows to both $\mathrm{Act}$ and $\mathrm{Prediction}$ (so to Box B). $\mathrm{Accurate}$ (0.99) is a second parent of $\mathrm{Prediction}$.

- $do(\mathrm{fdt}=\text{onebox})$: act is onebox; box full with probability 0.99, so $\mathbb E V=\$990{,}000$.
- $do(\mathrm{fdt}=\text{twobox})$: box full with probability 0.01, so $\mathbb E V = 0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

One-box. No retrocausation is invoked. Fiona believes information does not travel backward. She merely refuses to imagine her action changing while the predictor's model of her stays fixed. That is the CDT dominance argument, which A-FDT treats as a restatement of CDT's method of constructing hypotheticals, not an independent argument. Each hypothetical-construction method yields its own dominance notion (EDT's would favor refraining in the smoking lesion), and A-FDT has an analogue under which it never takes a dominated action.

**Smoking lesion.** Here the graph differs. The lesion is a common cause of $\mathrm{Act}$ and cancer, and $\mathrm{fdt}$ points only to $\mathrm{Act}$. Intervening leaves $P(\text{lesion})$ unchanged, so smoking wins by $p\cdot\$1000$. Because the agent's preferences depend on the lesion, the paper models two utility functions and hence two possible decision functions, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, with $\mathrm{Act}$ determined by whichever the lesion selects. The same A-FDT equation yields one-boxing in Newcomb and smoking here; only $G$ changed. The paper concedes the problem is contrived and recommends abandoning it.

**Transparent Newcomb / Parfit's hitchhiker.** Fiona observes a full box. She intervenes on $\mathrm{fdt}(P,G,\text{full})$. Setting it to twobox changes the predictor's output, so with probability 0.99 she would have faced an empty box and been governed by $\mathrm{fdt}(P,G,\text{empty})$. Expected values are about $\$990{,}000+0.01q\cdot 1000$ for onebox versus $0.01\cdot 1{,}001{,}000+0.99q\cdot 1000$ for twobox, where $q$ is her credence that she two-boxes on seeing an empty box. She one-boxes despite seeing the full box. The same structure gives paying the driver in Parfit's hitchhiker and refusing mechanical blackmail. Her hypotheticals are of worlds where she is never blackmailed, even while she holds the letter. If the blackmailer errs with probability $\epsilon$, refusing costs $\epsilon\cdot\$1{,}000{,}000$ in expectation against a certain \$1,000 loss from paying; the paper's numbers show the threshold: at $\epsilon = 0.0009$ she refuses ($\$900$), at $0.00011$ she pays.

**XOR blackmail.** The infestation is not downstream of $\mathrm{fdt}$, but the letter is. Intervening changes whether the letter is sent, never whether there are termites, so she refuses. EDT pays, treating the letter as news.

**Death in Damascus.** Death's book entry depends on $\mathrm{fdt}$, so wherever she "decides" to go, Death is there. Staying saves \$1,000. CDT hypotheticals hold Death's location fixed, which makes CDT unstable and even makes it reject a \$1 truly random coin.

**Coordination.** The paper's voting and gym examples apply the same idea: symmetric agents or future selves share a decision function, so the intervention moves all copies.

## 5. What the source leaves open, and operational interpretations

**The graph $G$ is an input, not derived.** The paper says deducing subjunctive-dependence structure from observation is "perhaps the largest open problem." So A-FDT's prescriptions are only as good as the supplied $G$. To use it on a new case, I suggest (my own recommended procedure, not the paper's) the following checklist for each variable $Z$ in the model:

1. Does $Z$ have a computation, in a predictor's model, in a copy, or in another agent's reasoning, that is (approximately) the same function as my decision procedure, evaluated on the same input? If so, draw an arrow from $\mathrm{fdt}$ to $Z$, with strength given by the reliability of the predictor.
2. Is $Z$ merely correlated with my action via a common cause that does not compute my decision (lesion, infestation)? Then no arrow.
3. Does the actual action node depend on which observation I receive? If so, add the branching structure of the transparent-box and blackmail graphs, with a separate $\mathrm{fdt}(\ldots,x)$ node for each observation, selected by an upstream variable such as $\mathrm{Prediction}$.

A useful test: "Would $Z$ differ if my algorithm, as written, returned something different?" This is the question A-FDT asks, though it gives no algorithm for answering it.

**Unobserved branches.** In the transparent and blackmail graphs, the value of the other-observation node (e.g. $q$) enters expected utility. The paper notes that its correct value is determined by A-FDT's own behavior there, but the answer is insensitive to uncertainty about it in these examples. I add that in general one would need to treat these as probabilities for the A-FDT equations on other inputs, a mildly recursive but well-founded structure when observation histories are finite.

**Action versus policy.** With a single node per observation, the two versions coincide in single-agent problems like those above. The paper says they differ in some multi-agent dilemmas; it does not say how, and I do not speculate.

**Fairness.** The paper claims A-FDT does best on "fair" problems, where outcomes depend only on the agent's behavior in the problem at hand, but gives no formal definition (footnote 15 shows an obstacle: a problem punishing copying Fiona's action is unfair to her). I would treat the claim of optimality as a conjecture. Rival theories can be exploited by problems that reward or punish specific decision procedures, and no theory wins everywhere.

## 6. Philosophical motivation

The argument from utility: an agent who follows A-FDT does better in fair Newcomblike problems than CDT or EDT. The argument from precommitment: A-FDT acts as it would have precommitted to act, avoiding costly binding mechanisms, and is reflectively stable on fair problems, whereas CDT recommends self-modification. The argument from information: A-FDT does not assign negative value to information, unlike EDT, which would pay to avoid seeing a full box.

The diagnosis in the paper is symmetric. EDT's hypotheticals respect too many correlations, including merely statistical ones, so it manages the news (cosmic ray problem, XOR blackmail). CDT's respect too few, imagining predictors failing exactly when it acts. A-FDT preserves exactly those dependencies that are logically or causally mediated.

The paper also rebuts the charge of "delusion." If a deterministic CDT agent may imagine its act varying, an A-FDT agent may equally imagine its function's output varying. Both counterfactuals describe worlds that cannot actually occur. CDT agents always find predictions accurate, and A-FDT agents always find their observations consistent with their actions.

## 7. Cautions

- A-FDT's hypotheticals may require discarding the agent's actual observation. This is the feature that yields one-boxing on a visibly full box and refusal of a held letter, and it is the main source of the theory's counterintuitiveness. The paper's answer is that such agents tend to face the good case.
- The theory has no definition of its core counterfactual in full generality. Disagreement about outputs can therefore hide in disagreement about $G$, not about the equation.
- The paper's early variants (Timeless Decision Theory, Updateless Decision Theory) are named in a note: the first both conditioned on evidence and changed the intervention point, a "double update" the authors call harmful.

## 8. Conclusion

A-FDT is a one-line modification of CDT: replace the intervention on the act with an intervention on the output of one's own decision function, relative to a graph encoding subjunctive dependence, and let observations select which output node is intervened on. With the right graph it one-boxes, smokes, pays the driver, refuses blackmail, and stays in Damascus, using a single rule with no ratification or precommitment. What it does not yet provide is a principled method for building the graph, and that, along with a formal fairness criterion, is where its application to unfamiliar cases will succeed or fail.