# A-FDT: Deciding by Intervening on the Output of Your Own Decision Function

## 0. Naming and scope

The source paper, Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality*, calls its theory "FDT." This essay uses **A-FDT** for the decision procedure given in Equation (4) of Section 5. The "A" stands for *action*: the procedure intervenes on a node whose values are the agent's available actions. The paper's footnotes 7 and 16 say the authors' "preferred formalization" has the agent choose *policies* (maps from observations to actions) instead. They say the difference "only matters in multi-agent dilemmas so far as we can tell." I treat that policy version as a related variant and do not call it A-FDT. Other theories keep their own names: CDT (causal decision theory), EDT (evidential decision theory), and, for historical predecessors, Timeless Decision Theory and Updateless Decision Theory.

I try to mark three kinds of statement: what the source says, what follows from the source's equations, and what I add as an operational suggestion. The additions are collected mainly in Section 5.

## 1. The common frame: expected utility with a choice of "hypotheticals"

The source places EDT, CDT and A-FDT inside one schema. Each prescribes the action maximizing

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j)\tag{1}$$

where $x$ is the observation history and "$\hookrightarrow$" is the connective for decision hypotheticals. Following Joyce, the source says the theories agree about how to value outcomes and disagree about "the epistemic perspective from which actions are to be evaluated." In practice the agent holds a world-model $M$. For each action $a$ she builds a hypothetical $M^{a\hookrightarrow}$, a transient "scratch-paper" object, and picks the action with the highest value. The theories differ in what $M$ contains and how hypotheticals are built from it:

$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E[V\mid \mathrm{Obs}=x,\mathrm{Act}=a]\tag{2}$$
$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E[V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x]\tag{3}$$

Here $V=\mathcal U(\text{Outcome})$, and $G$ is a causal graph over the variables of $P$, with Pearl's $\mathrm{do}$ operator doing the surgery. EDT conditions, which keeps every correlation. CDT intervenes on a physical-action node, which keeps only correlations that the graph says are caused by the action.

## 2. The definition of A-FDT

The source's Equation (4):

$$\mathrm{A\text{-}FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\Big[V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big]\tag{4}$$

The ingredients are as follows.

**A model with logical structure.** $P$ must contain variables for the outputs of mathematical functions. The source's example is a variable for $6288+1048$ with nearly all its mass on $7336$. $G$ is a graph that "tells us how changing a logical variable affects all other variables." It is the analogue of CDT's causal graph, but it must encode subjunctive dependence in general: "logical, mathematical, computational, causal, etc. structure."

**A self-referential intervention node.** The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of the A-FDT procedure itself when run on this very model and these observations. Underlines denote dequoting, so the variable's *name* contains the model. The source notes that this self-reference is harmless: the agent need not know the *value* of $\mathrm{A\text{-}FDT}(P,G,x)$ to have a variable *representing* it, and Kleene's second recursion theorem (quining) shows how a data structure can contain an accurate representation of itself.

**Observation changes the node, not the distribution.** In (3) an observation shifts $P$ by conditioning. In (4) an observation $x$ changes *which node* is intervened on, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. These are distinct variables standing for what the same procedure outputs on different inputs. The agent does not discard the observation. It acts as the node-for-$x$ dictates, and hypothetical worlds in which that node outputs something else may be worlds where she would have observed something else.

**Surgery.** $\mathrm{do}(\mathrm{fdt}=a)$ sets the node to $a$ and recomputes everything downstream according to $G$, leaving everything else fixed. Downstream means everything that subjunctively depends on the function's output, not only what the action causes. Typically the node is a root with children such as $\mathrm{Act}$ and any predictor-like variables.

Two readings follow immediately.

1. *Agreement with CDT and EDT where dependence is only causal.* If every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$, then $\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid\mathrm{do}(\mathrm{fdt}=a)]$ and all three theories agree. They diverge only when something other than the action's causal descendants tracks the agent's decision: predictors, twins, copies.
2. *The analogy that organizes the theory.* In the source's words: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT intervenes on the *token* "my action is $a$," while A-FDT intervenes on the *type*, the function.

## 3. Subjunctive dependence and counterpossibles

Two systems **subjunctively depend** on a function when both compute it. The source's model case is two calculators computing $6288+1048$. Their outputs are constrained to agree insofar as neither errs, whether or not they share a causal history. A predictor in Newcomb's problem holds a "twin inside the predictor's mind," a representation of the agent's decision function, and the prediction depends on the agent's action through that function.

The source stresses three distinctions.

- Causation is a special case of subjunctive dependence. If a scribe copies a calculator's output, she would have written something different had it output something different.
- Mere statistical correlation is not subjunctive dependence. Two pink calculators that happen to be pink do not depend on each other's colour.
- The dependence can be probabilistic. A noisy predictor or a nondeterministic agent weakens the link without removing it.

If a function outputs $\textit{cooperate}$ on an input, it does so necessarily, so imagining it outputting $\textit{defect}$ is a *counterpossible* supposition. The source admits that this is "the main drawback of FDT relative to CDT at this time." It argues that the difficulty is technical, not philosophical. Humans reason sensibly under logical uncertainty (about the twin prime conjecture, say), and the agent only needs the local question of how particular predictors' outputs would change.

Two further points from the source. First, it considers a variant, FDT′, that asks "what if I used a different decision function $f_n$?" It argues that this does not avoid counterpossibles, since predictors of $d$ must still be imagined predicting as if $d$ behaved like $f_n$. Second, it admits that Equation (4) "rests on shakier philosophical foundations" than (3). Pearl gives an account of how to learn causal structure from experiment, and nothing comparable exists for subjunctive dependence. The source calls this "perhaps the largest open problem" for the theory. Equation (4) works *given* an accurate $G$ but does not say how to produce one.

## 4. Worked examples

Throughout, the evaluation is of $\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$ in a graph given in advance.

### 4.1 Newcomb's problem

Nodes: $\mathrm{fdt}$ (root), $\mathrm{Act}$ (child of $\mathrm{fdt}$), $\mathrm{Prediction}$ (child of $\mathrm{fdt}$ and a noise node $\mathrm{Accurate}$, with $P(\text{accurate})=0.99$), $\mathrm{Box\,B}$ (a function of the prediction), and $V$.

- $\mathrm{do}(\mathrm{fdt}=\textit{onebox})$: $\mathrm{Act}=\textit{onebox}$; the box is full with probability $0.99$. $\mathbb E[V]=0.99\cdot 1{,}000{,}000=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\textit{twobox})$: $\mathrm{Act}=\textit{twobox}$; the box is full with probability $0.01$. $\mathbb E[V]=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

A-FDT one-boxes. The source emphasizes that no retrocausation is involved. The agent merely refuses to imagine the action changing while the logical fact behind the prediction stays fixed. CDT's graph has $\mathrm{Act}$ with no link to $\mathrm{Prediction}$, so its hypotheticals hold the box fixed and two-boxing wins by $\$1{,}000$ whatever the box's probability.

The source also answers an obvious objection. Suppose A-FDT is nearly certain it will one-box and so nearly certain the box is full. Why not then take both? Because the question "what if I two-boxed?" is evaluated by setting the *function's* output to $\textit{twobox}$, and the hypothetical changes the prediction too. Credence about the actual world does not enter the construction of the hypothetical.

### 4.2 The smoking lesion: the graph must differ

The dependence structure, not the surface payoffs, determines the answer. In the source's formalization the lesion fixes the agent's utility function ($\mathcal U_S$ or $\mathcal U_R$, the latter valuing smoking at $-\$1$) and so which of two procedures, $\mathrm{fdt}(\underline{P_S},\underline G)$ or $\mathrm{fdt}(\underline{P_R},\underline G)$, controls $\mathrm{Act}$. The agent cannot tell which. The Cancer node has *no* arrow from either fdt node, because cancer does not depend on what the procedure outputs. So $P(\text{lesion})=p$ is unchanged under either intervention, and smoking beats refraining by $p\cdot\$1{,}000$. This is why the Newcomb graph cannot be reused after renaming variables: the topology of $G$ differs even though the numbers look isomorphic. The source adds that the problem is "badly confused" as formalized, since agents must be ignorant of their own desires, and it recommends abandoning it.

### 4.3 The transparent Newcomb problem: observation moves the node

There are now two nodes, $\mathrm{fdt}(\cdot,\textit{full})$ and $\mathrm{fdt}(\cdot,\textit{empty})$. The prediction decides which one controls $\mathrm{Act}$, since it determines what is observed. Let $q$ be the prior probability of two-boxing on seeing an empty box, and suppose the agent sees a full box. Intervening on the $\textit{full}$ node:

- $a=\textit{onebox}$: with probability $0.99$ the box is full and she one-boxes, getting $\$1{,}000{,}000$. With probability $0.01$ she sees an empty box and her $\textit{empty}$ node acts. $\mathbb E[V]=\$990{,}000+10q$.
- $a=\textit{twobox}$: with probability $0.01$ (misprediction) she sees a full box and two-boxes for $\$1{,}001{,}000$. With probability $0.99$ she sees an empty box and the $\textit{empty}$ node acts. $\mathbb E[V]=\$10{,}010+990q$.

One-boxing wins for every $q\in[0,1]$. (The source's printed expression for the two-box case contains a typographical slip; the figures above are my recomputation from the graph.) Note that the source writes the intervention with "$\mathrm{Obs}=\textit{full}$" inside the $\mathrm{do}$, but the calculation does not condition on $\mathrm{Obs}=\textit{full}$ in the hypothetical. $\mathrm{Obs}$ is itself downstream of the intervention and may come out *empty*. I read the "$\mathrm{Obs}=\textit{full}$" as labelling the node, in line with Equation (4), where $x$ appears only inside the node's name. This is exactly how an A-FDT agent holding two full boxes leaves the $\$1{,}000$: in the hypothetical where she two-boxes, she is "probably" looking at an empty box.

### 4.4 Parfit's hitchhiker

This is isomorphic to the transparent Newcomb problem, as the source notes. Using the stated numbers and treating the driver's detection error as $0.01$, let the relevant node be $\mathrm{fdt}(\cdot,\textit{in city})$. It feeds the driver's decision to give a ride and the payment action.

- $\mathrm{do}(\textit{pay})$: with probability $0.99$ she is predicted to pay and rides, losing $\$1{,}000$; with probability $0.01$ she is left to die ($-\$1{,}000{,}000$). $\mathbb E[V]=-0.99\cdot 1{,}000-0.01\cdot 1{,}000{,}000=-\$10{,}990$.
- $\mathrm{do}(\textit{refuse})$: with probability $0.99$ she is left to die, and with probability $0.01$ she rides free. $\mathbb E[V]=-\$990{,}000$.

A-FDT pays, even though, standing in the city, paying looks like pure loss. CDT and EDT both refuse, and so (if predicted correctly) never get the ride.

### 4.5 Mechanical blackmail with an imperfect predictor

The source gives the following case. A blackmailer who errs with probability $\varepsilon$ in predicting that an agent will pay runs the program iff she predicts payment. If the program runs and the agent refuses, the agent loses $\$1{,}000{,}000$. The A-FDT agent holding a letter intervenes on $\mathrm{fdt}(\cdot,\textit{blackmail})$:

- $\mathrm{do}(\textit{pay})$: she is blackmailed with probability about $1$ and loses $\$1{,}000$.
- $\mathrm{do}(\textit{refuse})$: she is blackmailed with probability $\varepsilon$ and loses $\$1{,}000{,}000$, an expected loss of $10^6\varepsilon$.

With $\varepsilon=0.0009$ the second loss is $\$900<\$1{,}000$, so she refuses, even though in the actual world she is holding the letter. The breakeven is $\varepsilon\approx 0.1\%$. The source says that at an error rate of "0.011%" she would pay. By Equation (4) and the stated payoffs, $0.011\%$ gives an expected refusal loss of only $\$110$, so she would still refuse; I read that figure as a slip for something like $0.11\%$, where $10^6\varepsilon=\$1{,}100>\$1{,}000$. The qualitative point is unaffected. The same structure explains why A-FDT refuses in the XOR blackmail: changing the node changes whether the letter is sent but not whether the house has termites, so paying has no benefit and refusing does not make termites likelier.

### 4.6 Other cases

- **Twin prisoner's dilemma.** $\mathrm{fdt}$ is the parent of both agents' actions. $\mathrm{do}(\textit{cooperate})$ gives $\$1{,}000{,}000$ and $\mathrm{do}(\textit{defect})$ gives $\$1{,}000$.
- **Death in Damascus.** Death's book entry depends on the agent's decision function, so the location of Death is downstream of the node. Staying costs $0$ (utility measured relative to death) and fleeing costs $\$1{,}000$, so A-FDT stays. There is no instability, because the CDT oscillation arises only from holding Death's location fixed under changes in the action.
- **Cosmic ray problem.** $\mathrm{Act}$'s correlation with the "hit by a ray" variable is statistical, not subjunctive, so the intervention breaks it and A-FDT takes the $\$100$. EDT's conditioning instead preserves the correlation.
- **Voting and self-coordination.** These come from the source's conclusion. When ten agents with the same decision function must all pay to vote, or when one's future selves face the same gym decision, the other agents' actions lie downstream of the same node.

## 5. Using Equation (4): a recipe and its assumptions

The source gives the equation and a set of examples but does not give a general algorithm for producing $G$. What follows from the source is this procedure:

1. Specify $P$, including variables for the outputs of the relevant functions.
2. Specify $G$ so that it shows how the node(s) $\mathrm{fdt}(\underline P,\underline G,\underline x)$ propagate to $\mathrm{Act}$ and to every other variable that subjunctively depends on them.
3. Choose the node matching the actual observation $x$.
4. For each action $a$, compute $\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}(\ldots,x)=a)]$.
5. Output the argmax.

**My additional proposals** for the step the paper leaves open, namely building $G$ for an unfamiliar case:

- **Test for a link.** Draw an arrow from the decision node to a variable $Z$ when $Z$'s value is produced by something *computing or modelling the agent's output on this input*: a predictor, a copy, a counterpart, a record derived from such a prediction. Do not draw one when $Z$ merely correlates with the choice through a common cause the function does not control, such as a lesion or a shared history.
- **A diagnostic question.** Ask: "If this procedure returned something else on this input, would the thing producing $Z$ have computed something else?" The calculator-and-scribe examples are the model.
- **Noise as stochastic nodes.** Represent predictor error, as the source does, by an exogenous noise node such as $\mathrm{Accurate}$, so that imperfect subjunctive dependence has a price.
- **Separate nodes for separate inputs.** Include one fdt node for each observation that could be received, and a variable that determines which one drives $\mathrm{Act}$ (a "selector" such as the prediction in transparent Newcomb).
- **Prior over off-path nodes.** When a hypothetical may route control to a node other than the one intervened on, the agent needs a prior for what that node outputs (the $q$ above). The source stresses that in its examples the verdict is insensitive to it. I add that this should be checked in each new case rather than assumed.

I flag these as my own: the source says only that $G$ must be supplied "in the same way that the relevant causal structure is given as an input to CDT." The choice of arrows is a modelling decision, and a mistaken $G$ can yield either CDT-like or EDT-like behaviour.

**Self-reference and tie-breaking.** The source does not discuss ties or what happens when several nodes within a model are mutually dependent. I assume ties are broken arbitrarily, and the argmax in (4) is silent on it.

## 6. Why intervene on the function? The source's arguments

**Hypotheticals should track believed dependence.** The source diagnoses the failures of the rival theories in terms of their hypotheticals. EDT's "respect too many correlations" and so "manages the news": in the XOR blackmail the EDT agent pays because paying is good news about termites. CDT's "respect too few," so its Newcomb agent imagines "a perfect predictor [making] an incorrect prediction." A-FDT's hypotheticals keep exactly the dependencies the agent believes in.

**Utility.** The primary argument is the argument from utility: agents implementing A-FDT predictably get richer in fair problems, and a theory recommending anything else would be one we would warn our loved ones away from. The source treats the precommitment argument and the value-of-information argument as secondary to this. A-FDT acts as it "would have precommitted to act," with no costly mechanisms, and it never assigns negative expected value to information.

**Dominance is theory-relative.** The paper argues that every method of building hypotheticals induces its own dominance principle. Two-boxing dominates relative to CDT's counterfactuals, refusing to smoke dominates relative to EDT's conditionals, and A-FDT has an analogue: action $a$ dominates $b$ if, "holding constant all relevant subjunctive dependencies," switching the algorithm's output from $b$ to $a$ is sometimes better and never worse. No dominance principle is therefore a neutral arbiter.

**Fairness.** The source says no decision theory wins in all problems: a mind-reader can reward whoever uses a specific procedure. A-FDT is claimed to match or beat the rivals in *fair* problems, "where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." But the source admits there is no formal definition of fairness. Footnote 15 gives a counterexample to naive attempts: a problem rewarding agents who act differently from a copy of A-FDT is unfair to A-FDT in a way that has no obvious analogue for CDT. The claim "no fair problem where A-FDT loses" is therefore an empirical report of the authors' search, not a theorem.

**Objections.** One objection is that A-FDT agents believe they control abstract functions or the past. The paper replies that deterministic CDT agents face a parallel puzzle about controlling their *token* action. Both imagine variations that cannot actually occur, and "any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token." The paper also reports that the observation-dependent behaviour looks strange. It answers that the strangeness reflects the "global perspective": the agent asks "what would the entire universe look like if the [procedure] behaved differently?"

## 7. Limits and open questions

Pulling together the caveats:

- **Dependence structure is an input.** There is no analogue of Pearl's causal discovery for subjunctive dependence, and the source says it is unclear whether it fits in Pearl's framework at all. Footnote 9 also notes that an "evidential" reading, conditioning on a logical sentence, would require probabilities for false logical claims. The $\mathrm{true}(\cdot)$ operator is explicitly left undefined, and Equation (4) sidesteps it by assuming $G$.
- **Counterpossible semantics.** The source offers no theory of counterpossibles, only the observation that humans manage and that the task may be local.
- **Actions versus policies.** The authors' preferred version selects policies. For single-agent problems in the paper this makes no difference, but for A-FDT proper the extension to multi-agent cases is an open matter.
- **Idealization.** The examples use minimal models in which the agent's model matches the situation. Real agents would need approximations, and the source expects bounded versions to share the idealized agents' strengths and weaknesses without proof.
- **Optimality.** The authors say they "do not yet know whether FDT is optimal among decision theories, or even (on a formal level) what optimality consists in."

## 8. Conclusion

A-FDT is the expected-utility rule $\arg\max_a\mathbb E[V\mid\mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)]$. It differs from CDT in two ways: it intervenes on a node standing for the output of the agent's own decision function, and it responds to observation by switching which node is intervened on instead of by conditioning. What each hypothetical contains is settled by the graph $G$, which must encode all the decision-relevant subjunctive dependence the agent believes in. This yields one-boxing in Newcomb's problem, smoking in the lesion problem, cooperation with a twin, payment in Parfit's desert and refusal of blackmail, all from a single rule. The rule is only as good as the dependence structure supplied to it, and how to *get* that structure is the main thing the source leaves open. In this essay I have offered heuristics for constructing it and flagged where they go beyond the source.