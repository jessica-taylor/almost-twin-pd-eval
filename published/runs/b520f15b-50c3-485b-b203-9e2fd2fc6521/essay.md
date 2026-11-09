# A-FDT: Choosing by Intervening on Your Decision Function

## 1. The idea

A-FDT is the decision theory the source paper presents as Equation (4) of its Section 5 (the paper calls the family "functional decision theory"). I use "A-FDT" for that equation and for the procedure it defines. CDT and EDT are named separately where I discuss them.

A-FDT shares the expected-utility form of CDT and EDT and differs only in how it builds the hypothetical in which an action is taken. The paper puts it this way: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." The agent treats her choice as the output of a fixed mathematical function. She asks what would happen if that very function returned a different value, and she lets every quantity that depends on the function change accordingly.

## 2. The formal definition

The source gives a shared template (Equation 1):

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

Here $a$ is an action, $x$ an observation history, and $\hookrightarrow$ the connective for decision hypotheticals. The three theories differ in how they read $\hookrightarrow$. The source cites Joyce: the theories "disagree about the epistemic perspective from which actions are to be evaluated," not about value.

- EDT (Eq. 2): $\arg\max_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$.
- A-FDT (Eq. 4):

$$\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The ingredients are as follows.

- $P$ is a probability distribution over the agent's world-model variables. These include variables for the outputs of mathematical functions, such as the value of $6288+1048$.
- $G$ is a graph, "augmented" structure that says how changing a logical variable affects the other variables. It encodes causal, logical, computational and other dependencies together.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model that represents the output of A-FDT itself on those inputs. The underlines mean dequoting. The self-reference is harmless: the agent need not know the value of this variable to have a variable representing it, and Kleene's second recursion theorem (quining) shows how a structure can contain a representation of itself.
- $\mathrm{do}$ is Pearl's surgery operator. It sets the intervened variable and recomputes its descendants, leaving everything else fixed.

The source names two differences from CDT. First, A-FDT intervenes on the node for the decision function's output instead of the node for the physical act. Second, observation changes which node gets intervened on instead of being conditioned on. When the observation changes from $x$ to $y$, CDT swaps $\mathrm{Obs}=x$ for $\mathrm{Obs}=y$ in its conditioning. A-FDT swaps $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for $\mathrm{fdt}(\underline P,\underline G,\underline y)$ as the intervention target.

The source's footnotes add two points. Its preferred formalization intervenes on policies (maps from observations to actions), and this matters only in some multi-agent problems. And the paper hedges that Eq. 4 "rests on shakier philosophical foundations" than the CDT equation.

## 3. Subjunctive dependence

The graph $G$ must encode subjunctive dependence. Two systems depend on the same function when they compute it, and neither the causal route nor the statistical route is required. The source's examples:

- Two calculators computing $6288+1048$ depend on that sum's value. A faithful predictor's model of an agent depends on the agent's function in the same way.
- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere correlation is not subjunctive dependence. Two pink calculators are correlated in color, but had the scribe bought a green one, the other would still be pink.

So an A-FDT agent keeps correlations that reflect shared computation and severs correlations that are coincidence or common-cause artifacts. EDT keeps all correlations. CDT keeps only the causal ones. The paper's slogan is that EDT respects too many correlations and CDT too few.

The counterfactual here is a counterpossible: the function does output $a$ although it actually outputs something else. The source concedes this is "the main drawback" of the theory. It argues the difficulty is technical, since humans and mathematicians reason under logical uncertainty, and it brackets the question. It says what matters is that the agent imagines changes "in all and only those things that subjunctively depend on the output of her decision-making procedure."

## 4. Using the equation: a recipe

The source says the equation is a step-by-step procedure. For a concrete problem:

1. Build $P$ for the problem as the agent understands it.
2. Build $G$, marking which variables depend on the decision function. Examples are the agent's own act, a twin's act, or a predictor's prediction.
3. For each candidate action $a$, apply $\mathrm{do}(\mathrm{fdt}(\ldots,x)=a)$. Propagate along $G$ and compute $\mathbb E[V]$.
4. Output the maximizer.

Step 2 is where everything is decided. The source says "we require that the relevant logical dependency structure be given as an input," just as CDT is given its causal structure. The paper has no general method for deducing subjunctive dependence from observation. It calls this "perhaps the largest open problem."

## 5. Worked examples

**Newcomb's problem.** Predictor accuracy is 0.99. In $G$, $\mathrm{fdt}$ points to both $\mathrm{Act}$ and $\mathrm{Prediction}$. Setting $\mathrm{fdt}=\text{onebox}$ gives $P(\text{full})=0.99$ and expected value \$990,000. Setting it to twobox gives $P(\text{full})=0.01$ and \$11,000. A-FDT one-boxes. CDT's graph has $\mathrm{Act}$ with no arrow to the box, so it two-boxes whatever $p=P(\text{full})$ is, because the extra \$1,000 is the same in both cases. No retrocausation is involved. A-FDT just declines to imagine the function's output changing while the predictor's model of it stays put.

**Smoking lesion.** The lesion is a common cause of the act and of cancer, and nothing subjunctively links cancer to the function. In the source's formalization, the intervention node feeds $\mathrm{Act}$ but not $\mathrm{Cancer}$. Intervening does not change $P(\text{lesion})=p$, and smoking wins by $p\cdot\$1{,}000$. So the same equation one-boxes and smokes. This is the step that lets A-FDT escape the supposed dilemma that a rational agent must either two-box and smoke (CDT) or one-box and refrain (EDT). The graph differs between the two problems, and nothing else does.

The source notes a quirk. To make the lesion problem well-posed, the agent must be uncertain about her own utility function, so the paper recommends abandoning the problem as contrived. This is also why the source treats it as a poor argument against EDT.

**Transparent Newcomb / Parfit's hitchhiker.** Here observation matters. Seeing a full box, A-FDT intervenes on $\mathrm{fdt}(\ldots,\text{full})$. The prediction is a function of that node, and the act is controlled by it only if the prediction was "one-box." Setting the node to onebox gives $0.99\cdot\$1{,}000{,}000$ plus a small term. Setting it to twobox gives about \$110,000. A-FDT one-boxes while looking at a full box. When it imagines two-boxing, it imagines a world where it probably saw an empty box. The source notes this is formally the same as paying the driver in Parfit's hitchhiker. The point is that the policy "pay when in the city" is what gets the agent picked up.

**Mechanical blackmail.** Upon seeing the letter, A-FDT imagines refusing and so imagines a world where it was probably never blackmailed. With a blackmailer who wrongly predicts "pay" with probability 0.0009, refusing costs about \$900 in expectation and paying costs \$1,000, so it refuses even though it knows the blackmailer erred this time. With error 0.00011 it pays. The threshold is whichever policy leaves the agent richer, so the choice is a calculation and not a stance.

**XOR blackmail and Death in Damascus.** In XOR blackmail, A-FDT intervenes without changing the termite probability, so paying buys nothing and it refuses. EDT pays because conditioning on payment makes the letter good news. In Death in Damascus, Death's location depends on the same function as the agent's. Fleeing therefore moves Death to Aleppo, and staying saves \$1,000. CDT instead oscillates, because its hypotheticals hold Death fixed.

**Twin prisoner's dilemma.** Cooperating sets the shared function to cooperate, giving \$1,000,000 against \$1,000 for defecting.

## 6. Why this is not delusion, and what it is not

The source answers the objection that A-FDT pretends to control mathematics or the past. A deterministic CDT agent also imagines worlds where her act differs from what physics allows. Both theories use imagined variation as a decision tool, so any objection to "controlling" the decision type applies equally to controlling the decision token. The hypotheticals are instruments, "like notes on scratch paper," not beliefs.

Several features follow from the construction.

- A-FDT agrees with CDT and EDT whenever the only correlations with the act are causal ones. They diverge only in Newcomblike settings with predictors or copies.
- There is no negative value of information. An agent that acts as it would have precommitted to act has no reason to pay to blindfold itself.
- It needs no ratification or precommitment machinery. EDT's extreme priors can force any action, and CDT is unstable, but A-FDT's hypotheticals do not depend on priors over the act in that way.
- The paper defines a dominance principle analogous to CDT's, with subjunctive dependencies held fixed. By that principle A-FDT never takes a dominated action. The paper stresses that every hypothetical-construction method yields its own dominance relation, so dominance cannot neutrally adjudicate between theories. The paper prefers utility achieved in "fair" problems, meaning problems where outcomes depend on the agent's behavior and not on its decision procedure as such. The paper admits fairness is not yet formalized.

## 7. What the source leaves open, and my proposed handling

These points are my own additions, not claims of the source.

1. **Building $G$.** The paper gives no algorithm. A usable heuristic is to include an arrow from the decision-function node to any variable that is produced by a process containing a model, copy or simulation of the agent's decision procedure. The test is the counterfactual question the paper poses: would this variable differ if the function's output differed? Common causes, such as the lesion, fail the test.
2. **Degree of dependence.** For imperfect predictors the paper uses an accuracy variable, exactly as in the Newcomb figure, so the dependence is probabilistic. I would handle weak copies the same way, with a noise node that sometimes breaks the correlation.
3. **Observation-indexed nodes.** Each possible observation gets its own node, and a predictor's output decides which node actually controls the act (as in the transparent Newcomb graph). When the agent's decision on observation $x$ affects whether $x$ occurs, the procedure effectively evaluates policies, in line with the source's footnote.
4. **Unknown dependence structure.** I would say the equation cannot then be applied mechanically. One reasonable response is to average over candidate graphs with weights, but this is my proposal and the source does not endorse it.
5. **Boundary cases.** The paper itself notes that a problem which punishes copies of the agent (its footnote 15) is unfair to A-FDT, and that comparison classes are unclear.

## 8. Conclusion

Equation (4) turns A-FDT into a CDT-shaped procedure with one substitution: the surgery targets the output of the agent's own decision function, so everything subjunctively downstream moves with it. This one change yields one-boxing, smoking, paying the hitchhiker, refusing blackmail, and standing still before Death. Its limits are plain in the source. The counterpossible semantics is underdeveloped, and the dependence graph must be supplied, since no theory yet tells us how to learn it. Within those limits, the rule is operational. Specify the dependencies, intervene on the function, and take the best imagined world.