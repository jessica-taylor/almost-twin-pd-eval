# A-FDT: Choosing the Output of a Decision Function

## 1. What is being explained

The source paper, Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality*, calls its proposal "functional decision theory" (FDT). This essay uses the name **A-FDT** for the version given by **Equation (4) of Section 5**. That version chooses among *actions*, conditions on an observation history, and intervenes on a node representing the output of the agent's own decision function. The paper's authors say in two footnotes that their "preferred formalization" has agents "iterate over *policies* (mappings from observations to actions) rather than actions," a difference they say matters only in some multi-agent dilemmas. I mention that variant only where it bears on interpretation. Other theories are called by their own names: causal decision theory (CDT) and evidential decision theory (EDT).

The essay marks provenance explicitly. Unmarked exposition follows the source. Passages labelled **[Mine]** are my own operational suggestions or computations, and the source does not endorse them.

## 2. The common frame: expected utility with a hypothetical connective

The paper treats EDT, CDT and A-FDT as expected-utility theories. An agent picks the action $a \in \mathcal A$ maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j) \qquad (1)$$

Here $x$ is the observation history and $P(a\hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Following Joyce, the theories differ only in their reading of the connective "$\hookrightarrow$", that is, in the "epistemic perspective" from which actions are evaluated.

Operationally, the agent holds a world-model $M$. For each candidate action she builds a *hypothetical* $M^{a\hookrightarrow}$, a transient "scratch paper" object and not a belief. She computes the expected utility $V_a$ of each hypothetical and takes the best. The three theories differ in what $M$ must contain and how hypotheticals are built from it:

- **EDT** (Eq. 2): $M=P$, and the hypothetical is conditioning, $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- **CDT** (Eq. 3): $M=(P,G)$ with $G$ a causal graph, and the hypothetical is Pearl's surgery, $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **A-FDT** (Eq. 4):
$$\text{A-FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

## 3. Reading Equation (4)

**The intervened variable.** Under CDT the intervened node is the physical action $\mathrm{Act}$. Under A-FDT it is a node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ representing the *logical* fact "what the A-FDT procedure outputs when run on this model and these observations." Underlining denotes dequoting: the node's name depends on the value of $P$, $G$ and $x$. The paper puts it as: "a CDT agent intervenes on the token 'my action is $a$,' whereas an FDT agent intervenes on the *type*."

**Self-reference.** The model contains a variable naming the output of the very procedure that consults the model. The source says this is harmless. The agent need not know the *value* of $\text{A-FDT}(P,G,x)$ to hold a variable *representing* it, and Kleene's second recursion theorem ("quining") shows how a structure can contain an accurate representation of itself.

**The graph carries the content.** $G$ must say how changing the logical node propagates to other variables. The paper wanted a $\mathtt{true}$ operator to condition on logical sentences, such as $P(\text{Riemann}\mid \mathtt{true}(\lnot \text{TPC}))$, but "it's not clear how to define a $\mathtt{true}$ operator." So it requires that $P$ come "augmented with information about the logical, mathematical, computational, causal, etc. structure of the world," and then reuses Pearl's $\mathrm{do}$. A-FDT is therefore a procedure *relative to a supplied dependence structure*, in the same way CDT is relative to a supplied causal structure.

**Observations.** CDT and EDT respond to observation by conditioning. A-FDT responds by changing *which node it intervenes on*: moving from $x$ to $y$ changes the intervention from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. This is the update-free feature behind the paper's remark that A-FDT considers hypotheticals in which her observations were different. In the paper's treatment, observation does not shrink the space of worlds being evaluated.

**What is held fixed.** In the hypothetical for $a$, everything logically, causally or subjunctively downstream of the node is recomputed with the node set to $a$. Everything else keeps its prior probability. The paper's gloss is that A-FDT "weighs her options by considering scenarios where the output of her decision function changes, and events that subjunctively depend on her decision function's output change, but everything else is held fixed."

**Agreement with the other theories.** If every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$, then $\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$ and the three coincide. They come apart when something correlates with the action without being caused by it, as with a predictor or a twin.

## 4. Subjunctive dependence and building $G$

Section 3 of the source defines **subjunctive dependence**: two systems depend subjunctively on a function when both compute it. Two calculators evaluating $6288+1048$ are the model case. If one says $7336$, the other very likely does too, and "insofar as the calculator made no errors" the outputs are logically constrained to agree. Causal dependence is a special case. A scribe copying a calculator's output depends on it subjunctively, because "if it output something different, she would write something different." Statistical correlation is not enough: two calculators that are both pink are not subjunctively linked, since a green calculator in Paris would not change Tokyo's.

Two consequences follow for application.

1. *Imperfect prediction weakens dependence without removing it.* In the Newcomb model this is a stochastic node, $\mathrm{Accurate}$, with $P(\text{accurate})=0.99$. It sits upstream of $\mathrm{Prediction}$, and the intervened node feeds both $\mathrm{Act}$ and $\mathrm{Prediction}$.
2. *A lesion is not a predictor.* The predictor contains a model of the agent's decision function. The lesion merely correlates with the agent's tastes. In the graph, the lesion node is not downstream of the logical node, even though it is correlated with $\mathrm{Act}$ in $P$.

The source is open about the gap: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem." It also notes that A-FDT must evaluate counterpossibles, such as "what if this function returned a different value?", and offers only a hope that this is a technical rather than philosophical difficulty. It gives the analogy of mathematicians reasoning under logical uncertainty, and it says "our interest here isn't in the particular method an agent uses to identify and reason about subjunctive dependencies."

**[Mine] A working recipe for $G$.** The paper leaves the construction of $G$ to the user. The following checklist is how I would apply the theory to a new case. It is a heuristic and not part of the source.

1. *Name the computation.* Write down the decision procedure and its inputs, namely the model and the observation. Ask what else in the problem is that computation, or contains a representation of it: twins, simulations, predictors reasoning about the agent, copies of the agent at other times.
2. *Add one node per possible observation.* For each observation $x$ the agent might receive, add a node $\mathrm{fdt}(\ldots,x)$, and add whatever mechanism determines which observation arrives (as in the transparent problems below).
3. *Draw edges by counterfactual test, not by correlation.* For each other variable $Z$, ask: if this computation returned something different, would $Z$ be different *because* some process computes, simulates or reads that output? If so, add an edge. If $Z$ merely co-occurs with the agent's choices (the pink calculator), do not.
4. *Model fallibility explicitly.* Imperfect copying or prediction becomes a noise node, like $\mathrm{Accurate}$, with calibrated probability.
5. *Do not pre-condition on the output.* The agent may hold credence about what the procedure outputs, but the hypothetical overrides it.

Different careful users could draw different graphs for the same story, and the theory's outputs would differ accordingly. I count that as an honest consequence of the source's position that $G$ is an input.

## 5. Worked applications

Throughout, "the agent" is an A-FDT agent whose model accurately describes her situation.

### 5.1 Newcomb's problem

Graph: $\mathrm{fdt}\to \mathrm{Act}$ and $\mathrm{fdt}\to\mathrm{Prediction}\to\text{Box B}$, with $\mathrm{Accurate}\to\mathrm{Prediction}$, and $\mathrm{Act}$ and Box B feeding $V$.

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$: $\mathrm{Act}=\text{onebox}$, and box B is full with probability $0.99$. Expected value $=0.99\times 1{,}000{,}000=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$: $\mathrm{Act}=\text{twobox}$, and box B is full with probability $0.01$. Expected value $=0.01\times1{,}001{,}000+0.99\times1{,}000=\$11{,}000$.

So A-FDT one-boxes. (The source prints \$999,000 for the EDT one-box value; on its own numbers $0.99\times 10^6=\$990{,}000$.)

The paper stresses that no retrocausation is involved. The agent "does not think that a physical signal passes between her action and the predictor's prediction; she just thinks it is foolish to imagine her action changing without also imagining $\text{FDT}(P^F,G^F)$ taking on a different value." A CDT agent, by contrast, pictures a perfect predictor going wrong exactly when she acts.

### 5.2 Smoking lesion

The graph now has no edge from the logical node to $\mathrm{Cancer}$. The lesion causes both smoking-taste and cancer, so $\mathrm{do}(\mathrm{fdt}=\cdot)$ leaves $P(\text{lesion})=p$ unchanged. Smoking is then better by the $\$1{,}000$ taste value (scaled by $p$ in the paper's formalization, since the agent does not know which of two procedures, tied to her tastes, is controlling her action). A-FDT smokes, so the same rule one-boxes in Newcomb's problem and smokes here. The paper adds that the smoking lesion problem is "badly confused" and treats it "only because of its historical significance."

### 5.3 Transparent Newcomb: observation changes the node, not the beliefs

Now suppose the agent sees box B full. The graph has two nodes, $\mathrm{fdt}(\cdot,\text{full})$ and $\mathrm{fdt}(\cdot,\text{empty})$. The prediction determines which observation arrives and hence which node controls $\mathrm{Act}$. Evaluate $\mathrm{do}(\mathrm{fdt}(\cdot,\text{full})=a)$, where $q$ is her credence that she two-boxes on seeing an empty box:

- $a=$ onebox: with probability $0.99$ the predictor predicted this, so the box is full and she takes it, getting \$1,000,000. With probability $0.01$ the box is empty and the other node acts: $1000q$. Total $=990{,}000+10q$.
- $a=$ twobox: with probability $0.99$ the predictor predicted two-boxing on seeing full, so the box is empty and the other node acts: $990q$. With probability $0.01$ she gets \$1,001,000: $10{,}010$. Total $=10{,}010+990q$.

For any $q\in[0,1]$ one-boxing wins. (The source prints "\$110,00"; the correct term is $0.01\times 1{,}001{,}000=\$10{,}010$.) Even holding a full box, she evaluates two-boxing as a world in which she very probably saw an empty one. This is the sense in which she changes her behavior with evidence only "by changing *the place in her graph where she intervenes*."

Note a feature of the action-level formulation. The evaluation at one node requires a credence $q$ about what the *other* node outputs. The paper says $q$ happens not to matter here, and that the correct value is $1$, but a general user must supply such credences. The policy-valued formulation mentioned in footnotes 7 and 16 would remove this dependence by choosing the whole observation-to-action map at once.

### 5.4 Parfit's hitchhiker

**[Mine, following the paper's remark that this is "precisely equivalent" to transparent Newcomb.]** Let the driver's lie detector be 99% accurate. Nodes: $\mathrm{fdt}(\cdot,\text{city})$ is what she does once in the city; a prediction node determines whether she is carried (if she is not, she is in the desert and dies, losing \$1,000,000).

- $\mathrm{do}(\text{pay})$: $0.99\times(-1{,}000)+0.01\times(-1{,}000{,}000)=-\$10{,}990$.
- $\mathrm{do}(\text{refuse})$: $0.99\times(-1{,}000{,}000)+0.01\times 0=-\$990{,}000$.

She pays. CDT and EDT, evaluating only from the city with the ride already granted, do not, and so are left in the desert.

### 5.5 Blackmail, Damascus, and the twin

- **Mechanical blackmail.** Holding the letter, the agent compares $\mathrm{do}(\mathrm{fdt}(\cdot,\text{blackmail})=\text{pay})$ with $=\text{refuse}$. The intervention changes both her action *and* whether the letter was sent, because the blackmailer's prediction reads the same node. Against a perfect blackmailer, paying means certainly blackmailed and a \$1,000 loss. Refusing means never blackmailed. With a blackmailer who errs with probability $\varepsilon$, refusing costs about $10^6\varepsilon$ and paying costs \$1,000, so the break-even is $\varepsilon=0.1\%$. **[Mine]** (The source states two fallible-predictor cases whose second figure, "0.011%," does not match this arithmetic; I take it as a misprint and rely on the break-even above.)
- **XOR blackmail.** The infestation node is upstream of the predictor and not downstream of the logical node. Changing the output changes the letter's probability but not the termite probability, so she refuses. EDT pays because conditioning on "pay" implies "no termites."
- **Death in Damascus.** Death's appointment-book entry is a function of a prediction of the agent's decision node. Under $\mathrm{do}(\mathrm{fdt}=\text{stay})$, Death is in Damascus and the agent loses nothing further. Under $\mathrm{do}(\mathrm{fdt}=\text{flee})$, Death is in Aleppo and she is out \$1,000. She stays. There is no instability, because no hypothetical holds Death's location fixed while the agent's choice varies.
- **Twin prisoner's dilemma.** The twin runs the same function, so one node feeds both actions. $\mathrm{do}(\text{cooperate})$ yields \$1,000,000 and $\mathrm{do}(\text{defect})$ yields \$1,000. She cooperates. Substituting different decision functions for the two parties would require a different graph.

## 6. Why A-FDT is not EDT, and not CDT

The paper's diagnosis is symmetrical: "EDT respects too many action-environment correlations, while CDT respects too few." EDT's hypotheticals keep *every* correlation, so it avoids smoking and pays XOR blackmail to "manage the news." In the cosmic-ray problem, if EDT is nearly certain to take \$1, then taking \$100 "must" mean she was hit, so she takes \$1, and her fear is self-confirming. CDT severs every correlation not caused by the action, so it imagines inaccurate predictors being wrong exactly now. A-FDT keeps just the correlations that are subjunctive dependencies and cuts the merely statistical ones.

The resulting hypotheticals can contain the "impossible." A-FDT agents end up in worlds where their observations match their output, and CDT agents end up in worlds where predictions were accurate. The paper claims neither is deluded and that the difference is practical. This matches its general line that "any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

**Dominance.** CDT's argument for two-boxing is that two-boxing wins holding the contents fixed. The paper replies that this presupposes CDT's way of evaluating counterfactuals: it asks us to imagine a calculator outputting $3159$ "holding constant the fact that $6288+1048=7336$." Every method of building hypotheticals yields its own dominance principle, so dominance is not a neutral arbiter. A-FDT's version holds subjunctive dependencies fixed, and by that standard A-FDT never takes a dominated action.

**Precommitment and self-endorsement.** The paper observes that "CDT and EDT agents would both precommit to one-boxing if given advance notice." A-FDT agents "simply act as they would have ideally precommitted to act," with no ritual or cost. It also claims that A-FDT is reflectively stable on fair problems. It argues that an A-FDT agent holding a blackmail letter would not want to switch to CDT, because according to her own hypotheticals a blackmail-paying procedure attracts more blackmail.

## 7. Open questions and where additional assumptions enter

1. **The graph.** The source says outright that there is no method for deducing subjunctive dependence structure, and that Equation (4) "works *given* a graph." Section 4's recipe is my operationalization. A user should treat conclusions as conditional on the graph, and the sensitivity of the decision to graph choices as worth checking. For example, in the XOR case, adding an edge from the logical node to the infestation node reverses the answer.
2. **Counterpossible content.** Equation (4) avoids defining a $\mathtt{true}$ operator by making the effect of the intervention part of the input. The theory does not yet explain *why* a given graph is the correct one. Nothing in the paper licenses a general method for assigning credences to logically false hypotheses.
3. **Credence about one's own output.** The agent may have credence about what she will do, and Section 6 of the source argues this should not block the evaluation. In the Newcomb case, even with $P(\text{onebox})\approx1$ she still evaluates two-boxing by intervening and finds the box likely empty. The paper compares this to EDT, where extreme priors lead to arbitrary behavior as Spohn noted.
4. **Actions versus policies.** The action-level Equation (4) needs credences about off-path nodes (the $q$ above). The authors prefer a policy-level choice and say the difference matters only in multi-agent dilemmas. I will not claim more. A careful user facing a multi-agent problem should check whether the answer is stable under the policy version.
5. **Fairness.** The paper claims A-FDT does best on "fair problems," meaning those where the agent's beliefs are accurate and the outcome depends only on what the agent does in the dilemma at hand. It admits there is no formal criterion. It offers the example of a copy of Fiona that punishes anyone who takes the same action as the copy, which is intuitively unfair to her. Mind-readers who reward or punish a *decision procedure* as such are excluded: "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*." The paper does not claim that A-FDT beats every rival in every setting.
6. **Utility as the criterion.** The argument for A-FDT is the "argument from utility": it gets richer than CDT or EDT in problems like these. The paper admits this is an informal case from selected dilemmas and not a proof of optimality ("We do not yet know whether FDT is optimal among decision theories, or even (on a formal level) what optimality consists in").

## 8. Using A-FDT on an unfamiliar case: a checklist

**[Mine, applying the above.]**

1. List actions, observations, outcomes and utilities.
2. Identify every process that computes, simulates or reads the agent's decision procedure. Mark which are exact copies and which are noisy.
3. Draw $G$ with a node $\mathrm{fdt}(\cdot,x)$ for each possible observation, plus the mechanism determining which observation is received.
4. Add stochastic nodes for prediction errors and any exogenous uncertainty.
5. For the observation actually received, intervene on $\mathrm{fdt}(\cdot,x)$ for each $a$ and propagate through logical, causal and subjunctive edges only.
6. Compute $\mathbb E[V]$ with off-path nodes carrying their prior credences, and pick the maximizer.
7. Sanity check: if all correlations with $\mathrm{Act}$ are causal, A-FDT should agree with CDT and EDT. If your graph says otherwise, re-examine step 3.

## 9. Conclusion

A-FDT, as given by Equation (4), keeps the expected-utility form and the Pearl-style surgery of CDT but moves the point of surgery. The agent sets the output of her own decision function, $\mathrm{fdt}(\underline P,\underline G,\underline x)$, to each candidate action and lets the consequences propagate through every dependence on that function, including predictors, twins and copies of herself. Observation changes which node she intervenes on, and not the set of worlds she weighs. This accounts for one-boxing in Newcomb's problem, paying in Parfit's hitchhiker, refusing blackmail, and smoking in the lesion problem, all by one rule. The formalism is only as good as the dependence graph it is given, and the source concedes that nobody yet knows how to derive such graphs from experience. Even so, Equation (4) states a clear procedure whose single substantive input, "what would change if this computation returned something else?", is also the question the theory takes decision-making to be about.