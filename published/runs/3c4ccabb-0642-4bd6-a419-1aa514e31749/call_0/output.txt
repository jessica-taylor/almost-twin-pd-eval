# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

A-FDT, the theory presented as Equation (4) of Yudkowsky and Soares's "Functional Decision Theory: A New Theory of Instrumental Rationality", is an expected-utility theory. It differs from causal decision theory (CDT) and evidential decision theory (EDT) only in how it builds the hypothetical worlds in which actions are evaluated. The slogan is that the agent asks which output of "this very function" would yield the best outcome, instead of asking which physical act would. This essay sets out the formal procedure, works through applications, and marks where the source stops and my own proposals begin.

## 2. The formal setting

All three theories maximize

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $\hookrightarrow$ is a decision-hypothetical connective. Following Joyce, the source says the theories disagree only about "the epistemic perspective from which actions are to be evaluated". Each agent keeps a world-model $M$ and builds for each action $a$ a hypothetical $M^{a\hookrightarrow}$. It computes a value from that hypothetical and takes the argmax.

The three prescriptions are:

- EDT: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$ (Equation 2)
- CDT: $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$ (Equation 3)
- A-FDT (Equation 4):

$$\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\ \Big|\ \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution, $G$ is a graph, and $x$ is the observation. The graph encodes "logical, mathematical, computational, causal, etc. structure", that is, how changing a logical variable affects all the others. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is the node standing for the output of the A-FDT procedure on those inputs. The underlines denote dequoting. The self-reference is harmless, because the agent needs a variable representing the value without knowing it, and Kleene's recursion theorem ("quining") shows such self-representing structures exist.

Equation (4) differs from CDT in two ways.

1. The intervention is on the decision-function node, not the physical action node. Everything that subjunctively depends on the function's output moves with it, including the agent's body, predictors, and twins. The CDT agent intervenes on the token "my action is $a$", while the A-FDT agent intervenes on the type.
2. Observations are not conditioned on. A different observation $x$ changes which node is intervened on, from $\mathrm{fdt}(\ldots,x)$ to $\mathrm{fdt}(\ldots,y)$. The source's footnote 7 says the authors' preferred formalization ranges over policies (maps from observations to actions) instead of single actions. The source says this matters only in some multi-agent dilemmas. I treat the node-switching as the paper's operational mechanism and the policy reading as a gloss.

## 3. Subjunctive dependence

Two things subjunctively depend on a function when they compute, or accurately model, that function. Causal dependence is a special case, since a scribe copying a calculator's output both causally and subjunctively depends on it. Mere statistical correlation is not subjunctive dependence: two coincidentally pink calculators do not covary under the counterpossible "had this one been green". A predictor with an accurate model of the agent is like a calculator on the other side of the world computing the same sum. When A-FDT imagines the function outputting something else, she imagines the predictor's model doing so as well. No retrocausal physics is invoked.

If the model is imperfect, the dependence weakens but persists. In the source's Newcomb network, the probability that the box is full is 0.99 under the one-box intervention and 0.01 under the two-box intervention. The Bayesian network there (Figure 3) is not a causal graph.

## 4. Applying the procedure

The recipe is:

1. Build $(P,G)$ for the situation as the agent understands it.
2. Identify the node(s) $\mathrm{fdt}(\ldots,x)$ for each possible observation.
3. For each candidate output $a$, intervene on the node for the observation actually received. Propagate along the dependence arrows and leave everything else fixed.
4. Compute $\mathbb E[V]$ and take the maximum.

**Newcomb.** Do($\mathrm{fdt}=$one-box) gives expected value $0.99\cdot 10^6=\$990{,}000$. Do($\mathrm{fdt}=$two-box) gives $0.01\cdot 1{,}001{,}000+0.99\cdot 1000=\$11{,}000$. A-FDT one-boxes. The CDT agent does not see the box's contents change with the intervention, so she gains $\$1000$ in each branch and two-boxes.

**Smoking lesion.** The graph differs. The lesion is not a function of the decision procedure, so intervening on the fdt node leaves $P(\text{lesion})$ unchanged and smoking gains $\$1000$ times the probability that the procedure controls her act. A-FDT smokes. The source's formalization has two possible procedures, one for each utility function ($\mathcal U_S$, $\mathcal U_R$), selected by the lesion. It admits that this makes the problem contrived. The same equation gives one-boxing in one problem and smoking in the other, and the only difference is the input $G$.

**Transparent Newcomb and Parfit's hitchhiker.** Seeing a full box, A-FDT intervenes on $\mathrm{fdt}(\ldots,\text{full})$. Setting that output to two-box makes the prediction "two-box on seeing full", so with 99% probability she would have seen an empty box. The source's values are $\$990{,}000+0.01q\cdot\$1000$ for one-boxing against $\approx\$11{,}000+q\cdot\$990$ for two-boxing, so she one-boxes. The structure is the same as paying the driver in the desert. The source says A-FDT acts as it would have precommitted to act, without paying for precommitment.

**Blackmail.** Seeing a mechanical blackmail letter, the A-FDT agent compares "pay" (probability of being blackmailed $\approx1$, lose \$1,000) with "refuse" (blackmailed with probability $\approx0$). She refuses and is never blackmailed. With a predictor erring 0.09% of the time she still refuses, because expected loss is $\$900$ against $\$1000$. At an error rate of 0.011% she pays, because the expected loss from refusing then falls below \$1000. In XOR blackmail the intervention changes whether the letter arrives but not whether the house has termites, so she refuses. EDT conditions, treats the letter as news about termites, and pays.

**Death in Damascus.** Death's book is written from an accurate prediction of the agent's procedure, so A-FDT's intervention moves Death's location with her choice. She stays and saves the \$1,000 travel cost, and does not oscillate. CDT, holding Death fixed, is unstable and cannot value a truly random coin at \$1.

**Coordination.** In a ten-person voting problem (\$1,000 each to vote, \$1,000,000 to all if everyone votes), identical A-FDT agents treat their decisions as one function and vote.

## 5. How A-FDT treats counterfactuals

The source holds that conditionals are not counterfactuals: conditional on taking a \$1 bill over a \$100 bill, she probably had a reason, but counterfactually she'd just be poorer. EDT's hypotheticals respect too many correlations, as in the cosmic-ray problem where it takes \$1 for fear of the hospital bill. CDT's respect too few. A-FDT keeps only the correlations that survive "the function behaves differently", described in the source as "all and only those things that subjunctively depend on the output".

The hypotheticals contain counterpossibles, such as the claim that the function outputs $b$ when it actually outputs $a$. The source admits the lack of a satisfactory account of this, calls it "the main drawback of FDT relative to CDT", and treats the matter as technical rather than philosophical. It also argues that CDT faces an analogous difficulty with deterministic tokens. Equation (4) avoids defining a $\mathtt{true}$ operator by requiring $G$ as input, as CDT requires causal structure. This is the main place where the theory is unfinished. **How $G$ is to be learned from observation is, in the source's words, "perhaps the largest open problem".** Without a general method the practitioner must supply $G$ by judgment.

## 6. What the source says and what I add

**Source claims.** Equation (4); the node-switching treatment of observations; the dependence-graph input; and the verdicts above (Newcomb, smoking lesion, transparent Newcomb, hitchhiker, blackmail, Damascus). The source also claims that A-FDT is reflectively stable in fair problems and has its own dominance notion, under which A-FDT never takes a dominated action.

**My operational proposals (not in the source).**

- *A test for drawing arrows.* Link a variable $Z$ to the fdt node if $Z$ is produced by a process that computes or models the decision function, either in full (twin) or in part (predictor). Do not link it if its relation to the agent's action runs only through a common cause that does not simulate the decision, as with the lesion. This is a heuristic derived from the source's examples, not a theorem.
- *Imperfect predictors as mixtures.* Treat model fidelity as a probability that the predicted node equals the fdt output, as in the source's $0.99$ and $0.0009$ examples. This gives the blackmail threshold: pay iff the blackmailer's false-positive rate is below $1000/10^6\cdot$ (roughly one in a thousand) times the stakes ratio. Writing $\epsilon$ for the false-positive rate, refusing has expected cost $\epsilon\cdot10^6$ and paying has expected cost \$1000, so she refuses iff $\epsilon<0.001$.
- *Ambiguous problems.* When two plausible graphs give different answers, evaluate under each and weight by credence in each graph. The source does not prescribe this.
- *Fairness.* The source says only that fair problems depend on the agent's behavior in the problem at hand and not on its decision procedure, and admits that a formal criterion is lacking (footnote 15).

## 7. Philosophical motivation

The source offers three arguments: precommitment (A-FDT acts as it would have precommitted), the value of information (it never expects information to hurt), and utility. The authors call the last the one that gives the others their teeth. A-FDT agents are richer in fair problems, and a predictor who keys on actions punishes two-boxers, not rational agents. The authors say only that they know of no fair dilemma where A-FDT loses.

## 8. Conclusion

A-FDT is CDT's surgical method applied to a different variable: the output of the agent's own decision function. Its prescriptions are as reliable as the dependence graph it is given, and the source supplies no general method for building that graph. Given a graph, the procedure is mechanical and delivers one-boxing, smoking, paying the driver, and refusing blackmail from a single rule.