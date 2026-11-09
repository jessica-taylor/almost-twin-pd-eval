# A-FDT: Action Functional Decision Theory as a Surgery on Logical Variables

## 1. The idea in one paragraph

Every expected-utility theory has the form "pick the action with the highest expected utility," so the theories differ only in how they imagine the world *if* a given action were taken. Evidential decision theory (EDT) imagines it by conditioning. Causal decision theory (CDT) imagines it by intervening on a physical action variable. **A-FDT** is the theory that Yudkowsky and Soares present as Equation (4) of "Functional Decision Theory: A New Theory of Instrumental Rationality." It intervenes on a *logical* variable instead: the output of the agent's own decision function on her actual inputs. The paper's summary question for the agent is "Which output of this very function would yield the best outcome?" Everything that subjunctively depends on that output changes in the hypothetical, and everything else is held fixed.

I call this version A-FDT because the paper's displayed equation selects an *action*. Footnotes 7 and 16 say the authors' preferred formalization selects a *policy*, meaning a map from observations to actions. They add that the difference "only matters in multi-agent dilemmas so far as we can tell." This essay treats the action-selecting Equation (4) and says when I go beyond it.

I try to flag what is **[Source]** and what is **[Mine]**, meaning my interpretation or extension.

## 2. The definition

### 2.1 The shared expected-utility frame [Source]

All the theories maximize
$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$
where $a$ ranges over a finite action set $\mathcal A$, $x$ is an observation history, and $\hookrightarrow$ is the "decision hypothetical" connective. Following Joyce, the paper holds that the theories "disagree about the epistemic perspective from which actions are to be evaluated," not about value. The agent keeps a world-model $M$. For each action she builds a hypothetical $M^{a\hookrightarrow}$, a transient mental object like "notes on scratch paper," and takes the action whose hypothetical scores highest.

### 2.2 The three equations [Source]

With $V := \mathcal U(\textsc{Outcome})$:

1. EDT: $\;\mathrm{EDT}(P,x)=\arg\max_a \mathbb E\,[V \mid \textsc{Obs}=x,\ \textsc{Act}=a]$.
2. CDT: $\;\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E\,[V \mid \mathrm{do}(\textsc{Act}=a),\ \textsc{Obs}=x]$.
3. **A-FDT (Equation 4):**
$$\boxed{\;\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big[V \;\Big|\; \mathrm{do}\big(\textsf{fdt}(\underline P,\underline G,\underline x)=a\big)\Big]\;}$$

In this equation $P$ is a probability distribution over the model's variables, including variables for the outputs of mathematical functions, and $G$ is a graph saying how changing any variable (logical, computational, causal) propagates to the others. The notation $\textsf{fdt}(\underline P,\underline G,\underline x)$ names a node whose label is the dequoted inputs. The node represents "the output of the A-FDT procedure when run on exactly these inputs."

### 2.3 Parsing the equation

**The intervened node is logical.** $\textsf{fdt}(\underline P,\underline G,\underline x)$ is not the agent's body or the physical act $\textsc{Act}$. It is the value of a fixed function at a fixed argument. Intervening on it is a counterpossible: if the function in fact returns $a_1$, the hypothetical "it returns $a_2$" is, strictly, a logical falsehood. The paper compares this to reasoning about "elliptical curves" if Fermat's last theorem were false, or to asking what a calculator that outputs $3159$ for $6288+1048$ would imply for a calculator across the world.

**Self-reference is harmless.** The model contains a node whose name mentions the model. The paper notes that the agent need not know the *value* of $\mathrm{FDT}(P,G,x)$ to have a variable *representing* it, and cites Kleene's second recursion theorem ("quining") for how a structure can contain an accurate representation of itself.

**Observation changes which node, not the distribution.** CDT responds to observing $x$ by conditioning on $\textsc{Obs}=x$. A-FDT responds by *switching the node it intervenes on*, from $\textsf{fdt}(\underline P,\underline G,\underline x)$ to $\textsf{fdt}(\underline P,\underline G,\underline y)$. The expectation in Equation (4) contains no conditioning on $\textsc{Obs}$. The observation appears only as an argument inside the node's label. Footnote 16 spells out the consequence: A-FDT "agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

**The graph does the work.** The paper's own approach (§5, footnote 9) is to demand $G$ as an input, just as CDT demands a causal graph. It writes: "Equation (4) works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing." Pearl's $\mathrm{do}$-operator is simply reused on a graph that includes logical nodes.

### 2.4 When the theories agree [Source]

If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (the only exception being the node $\textsf{fdt}$ on which $\textsc{Act}$ may itself depend), then
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\textsf{fdt}=a)],$$
and all three theories return the same action. They come apart only when something correlates with the action without being caused by it: predictors, twins, copies, blackmailers who model you.

## 3. Subjunctive dependence: what the graph must encode

The key notion is **subjunctive dependence**: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The paper's slogan is that "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The source gives these features:

- Causal dependence is a special case. A scribe copying a calculator's display depends causally on it, and also subjunctively, since had it output something else she would have written something else.
- Mere statistical correlation is not subjunctive dependence. If two calculators happen to both be pink, repainting one does not change the other.
- Dependence admits degrees. With an imperfect predictor or a noisy agent, the interdependence is "weakened, but not eliminated."
- The paper's key assumption is that the agent imagines "corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

**What the source leaves open.** How should one *learn* $G$? The paper calls this "perhaps the largest open problem in the study of functional decision theory," and says no Pearl-style account yet exists for dependence on logical facts. It also leaves open how to define probabilities over logical sentences that are false, and whether Pearl's framework can express this at all.

**[Mine] An operational reading.** For practical use, I suggest a modeling discipline that stays within the source's examples. To build $(P,G)$ for a problem:

1. *Find every process that is, or contains a model of, the agent's decision function.* This covers twins, simulations, predictors, and earlier or later selves facing the same decision. Give each its own node, and add an edge from the function node $\textsf{fdt}(\cdot)$ to each, perhaps mediated by an accuracy variable such as $\textsc{Accurate}$ in the Newcomb graph.
2. *Make the physical act a descendant of the function node.* The act is controlled by $\textsf{fdt}$ for whichever observation actually obtained.
3. *Treat merely correlated things as upstream or independent.* A lesion, a termite infestation, or the weather gets no edge from $\textsf{fdt}$. It may sit upstream of the act, but intervening on $\textsf{fdt}$ does not move it.
4. *Introduce one node per possible observation* when observations depend on something downstream of the function. The transparent Newcomb problem is the standard case, and §5.4 below works through it.
5. *Intervene on the node labelled with your actual inputs, set it to each $a$, propagate along the edges, and score $V$.*

Steps 1 and 3 amount to a judgment about which things "run the same computation." That judgment is exactly what the source declines to formalize. The recipe makes the dependence explicit and auditable, but it does not remove it. The prescriptions inherit all the uncertainty in $G$. The recipe is a checklist, not a theory of $G$.

## 4. Why not condition, and why not intervene on the act?

A-FDT sits between EDT and CDT. The paper's diagnosis is that "EDT respects too many action-environment correlations, while CDT respects too few."

- EDT keeps *merely statistical* correlations. In the cosmic ray problem, an agent who almost always takes \$1 infers that taking \$100 means she was hit by a ray, and so she forgoes the \$100. A-FDT breaks that correlation, because no edge runs from $\textsf{fdt}$ to the ray.
- CDT severs *logically necessary* correlations. Facing a perfect predictor, a CDT agent imagines the prediction staying fixed while her act changes, so in her hypothetical a "known-to-be-perfect" predictor errs exactly when she acts. A-FDT keeps those correlations, because the prediction and the act both hang off the same function node.

The paper also argues that dominance reasoning cannot arbitrate. "Every expected utility theory comes with its own notion of dominance." Two-boxing dominates under CDT-style counterfactuals, refusing to smoke dominates under conditioning, and A-FDT has its own version: "holding constant all relevant subjunctive dependencies," A-FDT never takes a dominated action. The paper's primary criterion is therefore utility actually achieved in "fair" problems, meaning ones where the agent's beliefs are accurate and the payoff depends only on her behavior in the dilemma at hand. It admits that no formal criterion of fairness exists yet.

## 5. Worked examples

### 5.1 Newcomb's problem [Source]

The model has stochastic nodes $\textsf{fdt}$ and $\textsc{Accurate}$ (0.99). The prediction and the act both depend on $\textsf{fdt}$. Box B is full iff the prediction is "onebox."

- $\mathrm{do}(\textsf{fdt}=\text{onebox})$: Act = onebox, and Box B is full with probability 0.99, so $\mathbb E[V]=0.99\times\$1{,}000{,}000=\$990{,}000$.
- $\mathrm{do}(\textsf{fdt}=\text{twobox})$: Act = twobox, and Box B is full with probability 0.01, so $\mathbb E[V]=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)=\$11{,}000$.

A-FDT one-boxes. (The source's text says \$999,000 for EDT's one-boxing value but \$990,000 for A-FDT's. The correct figure in both is \$990,000, since both use the 0.99 accuracy.)

Nothing here is retrocausal: "She does not think that a physical signal passes between her action and the predictor's prediction; she just thinks it is foolish to imagine her action changing without also imagining [the function] taking on a different value."

The common objection is that if the agent is nearly certain the box is full, she should two-box on reflection. The reply is that the agent never evaluates "two-box with the box held fixed." She evaluates "this function outputs two-box," and in that hypothetical the box is probably empty.

### 5.2 The twin prisoner's dilemma [Source]

Both players' acts descend from the same node. $\mathrm{do}(\textsf{fdt}=C)$ gives \$1,000,000 and $\mathrm{do}(\textsf{fdt}=D)$ gives \$1,000, so A-FDT cooperates. The twin's decision is not discarded as an independent variable. It is a second instantiation of the intervened function.

### 5.3 Smoking lesion [Source]

Here the dependence structure differs, so the graph cannot be reused from Newcomb's problem. The lesion is upstream of the act and of cancer, and no edge goes from $\textsf{fdt}$ to cancer. The paper makes the problem well-formed by letting the lesion determine the agent's *utility function* ($\mathcal U_S$ likes smoking, $\mathcal U_R$ does not). The agent then does not know which of two function nodes, $\textsf{fdt}(\underline{P_S},\underline G)$ or $\textsf{fdt}(\underline{P_R},\underline G)$, controls her act. In the lesion world, node $S$ controls the act. In the lesion-free world, node $R$ does.

Intervening on node $S$ leaves the probability $p$ of the lesion untouched. Smoking differs from refraining only in the worlds where $S$ controls the act, and there it gains the \$1,000 value of smoking. A-FDT therefore smokes, with an advantage of $p\cdot\$1{,}000$. The paper also says the problem is "badly confused" and treats it "only because of its historical significance."

### 5.4 Transparent Newcomb and Parfit's hitchhiker [Source, with a correction]

Observation of a full box is itself a consequence of the prediction. So the graph has separate nodes $\textsf{fdt}(\cdot,\text{full})$ and $\textsf{fdt}(\cdot,\text{empty})$. The prediction decides which of them controls the act. The agent sees a full box and intervenes on $\textsf{fdt}(\cdot,\text{full})$. Let $q$ be her prior probability that she two-boxes on seeing an empty box. Then:

- Output onebox: with probability 0.99 the prediction is accurate, the box is full, and she gets \$1,000,000. Otherwise the box is empty and the act is governed by the other node. Total: $990{,}000+10q$.
- Output twobox: with probability 0.99 the prediction is "twobox," the box is empty, and the *other* node controls the act, giving $990q$. With probability 0.01 the predictor errs, the box is full, and she gets \$1,001,000. Total: $10{,}010+990q$. (The source prints this as "\$110,00 + q·\$990", an evident typo.)

One-boxing wins for every $q\in[0,1]$, so the exact value of $q$ does not affect the choice. Even when the agent is looking at a full box, her hypothetical for two-boxing is one where, with high probability, she saw an empty box instead. Parfit's hitchhiker has the same structure: paying in the city corresponds to the hypothetical in which the driver rescued her.

This is how A-FDT treats observation in general. It does not condition on what was seen and then ask what to do. It asks what the whole input-output function should be, given that observations are themselves downstream of it. The paper contrasts this with Timeless Decision Theory, which "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

Equation (4) is also consistent with this reading. Its right-hand side has no $\textsc{Obs}$ conditioning. The paper's displayed expression for the transparent case adds "$\textsc{Obs}=\textsf{full}$" inside the $\mathrm{do}$. But the calculation that follows treats $\textsc{Obs}$ as determined by the graph and does not condition on it. **[Mine]** I take the calculation as authoritative. Conditioning on $\textsc{Obs}=\text{full}$ *and* intervening on the full-box node would reintroduce the double update.

### 5.5 XOR blackmail and mechanical blackmail [Source]

In XOR blackmail, the letter's arrival depends on the infestation and on what the agent would do given the letter. Intervening on $\textsf{fdt}(\cdot,\text{letter})$ changes the act *and* whether the letter is sent, but not whether the house has termites. Paying has no way of making the termites go away, so A-FDT refuses. EDT pays because conditioning on "pay" implies "no termites." CDT refuses too, but for a different reason: it treats the predictor as unaffected by the agent's act. If you ask Carl what would have happened had he paid, he says the letter would still have come. A-FDT says the predictor would have predicted differently and not sent it.

In mechanical blackmail, paying implies being blackmailed for \$1,000, while refusing implies (for a perfect predictor) never being blackmailed. Suppose the blackmailer errs with probability $\epsilon$ in predicting that the agent will pay, and the leak costs \$1,000,000. Paying costs \$1,000 for certain. Refusing costs $\epsilon\cdot\$1{,}000{,}000$ in expectation. A-FDT therefore refuses iff $\epsilon>0.1\%$. With $\epsilon=0.0009$ the expected loss from refusing is \$900, so she refuses. With $\epsilon=0.011\%$ it is about \$110, so she pays. This holds even while she holds the letter, because A-FDT is choosing a *procedure*, and the right procedure is the one that makes her a poor blackmail target.

### 5.6 Death in Damascus [Source, formalization mine]

**[Mine]** A minimal graph has $\textsf{fdt}$ feeding both the act (stay or flee) and Death's book entry (via a perfect prediction). The value is $V=\$1{,}000{,}000\cdot[\text{act}\ne \text{book}]-\$1{,}000\cdot[\text{flee}]$.

- $\mathrm{do}(\textsf{fdt}=\text{stay})$: the book says Damascus, the act is Damascus, and $V=0$.
- $\mathrm{do}(\textsf{fdt}=\text{flee})$: the book says Aleppo, the act is Aleppo, and $V=-\$1{,}000$.

A-FDT stays, with no instability. CDT's trouble comes from imagining the book fixed while the act varies. If instead a truly random coin that Death cannot predict is offered for \$1, A-FDT sees a 50% chance of surviving and will happily pay. The source's CDT agent refuses to pay for such a coin.

## 6. Questions the source does not settle, and my proposals

**(a) How to get $G$.** The source gives no procedure. My modeling checklist (§3) states the *interface*. Whether a node belongs "downstream of the function" is exactly the unsolved question. In real cases, I suggest the following heuristic, which is not from the source: ask whether the other process would still produce the same output if your decision procedure were rewritten, and whether that process is *tracking* your procedure (a model, a copy, a reasoner about you) rather than merely sharing a cause with it. Lesion-like things fail the test and predictor-like things pass it.

**(b) Imperfect dependence.** The paper handles this through noise variables like $\textsc{Accurate}$. A natural generalization, which is mine and not in the paper, is to let edges be stochastic with the intervened node as a parent, so that dependence is graded.

**(c) Action versus policy.** For single-agent problems, Equation (4) already handles observations by switching nodes, as in §5.4. The policy version would intervene on one node whose output is a whole map $x\mapsto a$. The source says the distinction matters only in multi-agent cases, and I do not develop it.

**(d) Unobserved nodes.** In the transparent and smoking cases, the other nodes ($\textsf{fdt}$ at other observations) need priors, such as $q$ above. The source finds that the *decision* is often insensitive to them. **[Mine]** I would add a robustness check: compute the comparison over the full range of unspecified priors and see if the ranking changes. If it does, the problem is underdetermined by the model.

**(e) Fairness.** A-FDT is not claimed to win everywhere. A problem that punishes agents "for using a specific decision procedure" can doom it, and footnote 15 gives an example of a rival copying Fiona's act. The claim is limited to "fair" problems, with no formal criterion yet. The authors say they have "not been able to construct an intuitively fair dilemma where FDT loses to a rival decision theory." That is an empirical claim about hand-picked cases, not a theorem.

**(f) Determinism and "control."** The authors argue that objections to A-FDT agents "controlling" a function output would equally undercut deterministic CDT agents "controlling" their own act. Both imagine hypothetical worlds that cannot actually occur. The authors say that as far as practical utility goes, the difference is that the A-FDT hypotheticals match the real dependencies.

## 7. Applying A-FDT to a new case: a protocol

Here is a protocol that makes the above operational. It is my synthesis of the source's procedure.

1. Write down the options, outcomes, utility function $\mathcal U$, and the observation you actually received.
2. List every process in the story that implements your decision function or contains a model of it, and every process that does not.
3. Build the graph. Make the function node(s) the parents of your act and of every such process. Include a node for each observation value your function may receive, whenever the observation is downstream of the function.
4. Fix the priors on all nodes, including the function-output nodes that are not your current one.
5. For each option $a$, set the node labelled with your actual inputs to $a$, propagate, and compute $\mathbb E[V]$.
6. Choose the maximizer. Test sensitivity to unspecified priors and to the strength of dependence edges.

Two sanity checks follow from the source. First, in a problem with no predictors, twins, or copies, the answer must agree with CDT. Second, the answer should be what you would have precommitted to if you had known the problem in advance. The source stresses that A-FDT agents "always act as they would have precommitted to act," and that this is why information never has negative expected value for them.

A short example outside the source's list is a three-person group coordination game where each voter pays \$1,000 to vote and everyone gets \$1,000,000 iff all vote. If the voters are known copies, the graph has one function node feeding all three acts. $\mathrm{do}(\textsf{fdt}=\text{vote})$ gives \$999,000 per person and $\mathrm{do}(\textsf{fdt}=\text{abstain})$ gives 0, so A-FDT votes. The paper uses a ten-voter version of this example. If the other voters are CDT agents whose behavior does not depend on yours, the same graph has no edges from $\textsf{fdt}$ to them. The comparison then reduces to whether your single vote matters, which is the CDT calculation, and the answer changes. This shows how the answer depends entirely on which edges $G$ contains.

## 8. Conclusion

A-FDT is a small formal change with large consequences. It keeps expected-utility maximization and Joyce-style foundations, and it keeps Pearl's $\mathrm{do}$-operator. It moves the intervention from a physical act to the logical output of the agent's own decision function, and it handles observation by changing *which* output is intervened on instead of by conditioning. On this view the theory's behavior is determined by the dependency graph $G$. With the right graph it one-boxes, smokes, cooperates with twins, pays the hitchhiker, refuses blackmail, and stays in Damascus. With the wrong graph, nothing in Equation (4) protects it.

The cost of this is that the central ingredient, a principled theory of how to obtain and justify $G$ and how to reason about counterpossibles, is missing. Equation (4) is best read as a well-defined decision rule conditional on a dependence structure, and I would not treat it as a complete answer to "what should I do?" The practical protocol above and the sensitivity checks are my attempt to make that conditionality explicit, so that disagreements about a case are located where they belong, in the graph.

## References

- Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060). Equations (1)–(4) are in §5, and the examples are in §§2–9.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Gibbard, A. and Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."