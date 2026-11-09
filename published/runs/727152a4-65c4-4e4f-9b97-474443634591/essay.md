# A-FDT: Deciding by Intervening on One's Decision Function

## 1. The idea

A-FDT, the action-level version of functional decision theory, is the decision procedure given as Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." Its central move is to treat a decision as the output of a fixed mathematical function, and to evaluate each candidate action by asking what the world would look like if *that function* returned the action. The question is not "what if my body did something else?" Causal decision theory (CDT) asks that, and evidential decision theory (EDT) asks "what would it be good news to learn I did?" A-FDT asks which output of this very procedure would yield the best outcome.

Two clarifications about naming. The paper calls the theory FDT. Here I call the Equation (4) procedure A-FDT, since it ranges over single actions. Footnotes 7 and 16 say the authors' preferred formalization iterates over *policies* (maps from observations to actions) rather than actions, and that this difference matters only in some multi-agent dilemmas. I follow the paper in setting that aside.

## 2. The formal definition

All three theories maximize expected utility,

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differ in how they read the connective $\hookrightarrow$. This is Joyce's point, which the paper quotes: the theories "disagree about the epistemic perspective from which actions are to be evaluated." The paper's three procedures are:

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT (Eq. 4):
$$\mathrm{FDT}(P,G,x)\coloneqq \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

The ingredients are these.

- **P** is a probability distribution over the agent's model variables. It includes variables for outputs of mathematical functions, such as the value of $6288+1048$.
- **G** is a graph of *dependence structure*. It covers causal links and also logical or computational links, showing how changing the value of a logical variable propagates to other variables.
- **x** is the observation history.
- **fdt(P̲,G̲,x̲)** is a node in the model standing for the output of the A-FDT procedure run on exactly these inputs. The underlines are the paper's dequoting notation. The self-reference is harmless: the agent need not know the node's value to have a node representing it, and Kleene's recursion theorem (quining) shows such self-representation can be constructed.
- **do** is Pearl's surgery operator. It sets the node and recomputes everything downstream of it in $G$, leaving everything else fixed.

The paper identifies two differences from CDT. First, the intervention point moves from the physical act node to the node for the decision function's output. Second, observation is handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition: it changes *which node it intervenes on*, from $\mathrm{fdt}(P,G,x)$ to $\mathrm{fdt}(P,G,y)$ when the observation changes. The function evaluated on a different input is a different logical variable.

The paper also considers an idealized version, $\mathrm{FDT}^*$, which uses a $\mathtt{true}(\cdot)$ operator that conditions on logical sentences, including false ones. It says no one knows how to define this operator. Equation (4) avoids the problem by requiring the dependence structure $G$ as an *input*, just as CDT takes causal structure as an input. This is the paper's main stated limitation. Deducing subjunctive-dependence structure from observation, in the way Pearl deduces causal structure, is called "perhaps the largest open problem."

## 3. Subjunctive dependence

Two variables subjunctively depend on one another when they are computed by, or reliably track, the same function. Examples are a twin's choice and the prediction a predictor makes by modeling the agent. The paper's analogy is two calculators computing $6288+1048$: if one outputs 7336, one can infer the other will, and one can say what the other *would* output if the first malfunctioned in some specified way.

Several points from the source are worth stating.

1. Causal dependence is a special case of subjunctive dependence.
2. Mere statistical correlation is not subjunctive dependence. Two pink calculators in different cities are an example.
3. A-FDT holds fixed everything that does not subjunctively depend on the function's output, and varies everything that does. Hence "FDT is to subjunctive dependence as CDT is to causal dependence."
4. Since the function's output is logically fixed, evaluating alternatives involves *counterpossibles*. The paper defends this on practical grounds: humans reason under logical uncertainty routinely, and only narrow questions need answering, such as how a predictor's output would change if the algorithm's output changed.

## 4. Applying the procedure

A usable recipe follows from the source.

1. Identify the decision function and its input: your model $(P,G)$ and observation $x$.
2. Build $G$ so that the node $\mathrm{fdt}(P,G,x)$ has arrows into your physical act *and* into every other variable that models or copies your reasoning: predictors, twins, simulations.
3. Do not add arrows from it to variables that are only statistically correlated with your act.
4. For each action $a$, intervene, propagate, and compute $\mathbb E[V]$.
5. If the observation is such that other observation-values $y$ are possible, the nodes $\mathrm{fdt}(P,G,y)$ remain in the graph. A parent variable, such as the prediction, determines which node controls the act. Intervening on $\mathrm{fdt}(P,G,x)$ can therefore change the probability that you see $x$ at all.
6. Output the maximizing action.

The paper's own computations illustrate this.

**Newcomb's problem.** The node $\mathrm{fdt}(P^F,G^F)$ points to both $\mathrm{Act}$ and $\mathrm{Prediction}$. The predictor is accurate with probability 0.99. Setting the node to *onebox* gives Box B full with probability 0.99, so $\mathbb E[V]=\$990{,}000$. Setting it to *twobox* gives full with probability 0.01, so $\mathbb E[V]=\$11{,}000$. A-FDT one-boxes. Carl (CDT) intervenes on $\mathrm{Act}$ downstream of the prediction, so full-probability $p$ is unchanged and two-boxing gains $\$1{,}000$ for every $p$. Eve (EDT) one-boxes via conditioning.

**Smoking lesion.** Here the graph differs, and this is the substantive modeling step. The cancer variable is not downstream of the decision function; the lesion is its parent. Intervening on the node leaves the probability of the lesion at $p$, and smoking wins by $p\cdot\$1{,}000$. The same machinery thus one-boxes and smokes. The paper formalizes the lesion as determining which of two utility functions (and hence which of two function-nodes) governs the act. It also calls the problem contrived and recommends philosophers abandon it.

**Transparent Newcomb and Parfit's hitchhiker.** The agent sees a full box. A-FDT intervenes on $\mathrm{fdt}(P,G,\textit{full})$. The prediction depends on this node. If it is set to *twobox*, then with high probability the prediction was "two-box," the box is empty, and the act is governed by the *other* node, $\mathrm{fdt}(\ldots,\textit{empty})$. With $q$ the probability of two-boxing on seeing an empty box, the paper computes:

- one-boxing: $\$990{,}000 + 0.01q\cdot\$1{,}000$,
- two-boxing: $\$11{,}000 + q\cdot\$990$ (the source prints this as "\$110,00," which is evidently a typo).

So A-FDT takes one box, though it sees a full box. The paper argues this is the same as paying the driver in Parfit's hitchhiker.

**Mechanical blackmail.** When blackmailed, A-FDT compares paying (always blackmailed, lose \$1,000) with refusing (never blackmailed, because the blackmailer predicts refusal). It refuses. With a fallible blackmailer, the paper's numbers are: if the blackmailer errs with probability 0.0009, refusing costs about \$900 in expectation against \$1,000 for paying, so A-FDT refuses even while holding a letter it knows came from an error. If the error probability is 0.011%, it pays.

**XOR blackmail.** Both CDT and A-FDT refuse. Their reasons differ: CDT because infestation is causally upstream of its act, A-FDT because intervening on the function changes whether the letter arrives but not whether termites are present. EDT pays, because it conditions on the good news the letter carries when it pays.

**Death in Damascus.** A-FDT intervenes on the function that the book's prediction tracks. Death's location therefore moves with the choice, and it stays and saves \$1,000. CDT's hypotheticals hold Death fixed, producing instability.

## 5. What the source claims and why

**The balance claim.** EDT's hypotheticals respect too many correlations, including merely statistical ones (cosmic ray problem, XOR blackmail). CDT's respect too few, since it treats predictors as erring exactly when the agent deviates. A-FDT keeps those correlations that are subjunctive dependences.

**Utility as criterion.** The source's primary justification is that A-FDT agents do better on average in "fair" problems, where outcomes depend on the agent's behavior and not on which procedure she runs. It rejects dominance arguments as theory-relative: every method of building hypotheticals induces its own dominance relation, and A-FDT has one too.

**Reflective stability.** Because A-FDT acts as it would have precommitted to act, it has no need for costly binding. It also never assigns negative value to information.

**Control.** The paper argues that objecting to A-FDT's "control" over its function type is no more principled than objecting to a deterministic CDT agent's "control" over its token. No retrocausation is invoked.

**Cooperation cases.** In the twin prisoner's dilemma A-FDT cooperates, because twin and agent compute the same function. The paper also discusses a ten-person voting game and self-coordination across days (the gym example), where similarity of decisions across agents or times supports cooperation.

## 6. Open points and my own proposals

The following are *my additions*, not claims of the source.

**Constructing G in practice.** The source gives no algorithm. A reasonable operational rule is to ask, for each environment variable $Z$: "Does $Z$ get determined by running, copying, or modeling my decision procedure on this input?" If so, add an arrow from the function node. A direct test is to ask whether a change in my reasoning would alter $Z$ even with my body held fixed. This is a heuristic, not a derivation. Errors in $G$ propagate directly: wrongly adding an arrow to the lesion's cancer variable recreates EDT's mistake, and omitting a predictor's arrow recreates CDT's.

**Imperfect dependence.** The source handles fallible predictors by an accuracy variable. I recommend routing every imperfect dependence through an explicit noise node in $G$, as in the paper's Newcomb graph, so that Equation (4) remains a standard do-calculation with computable probabilities.

**Policies versus actions.** For problems where observation-dependent behavior matters, I would iterate over policies, in line with the authors' footnote preference. In the single-node examples above, the observation-indexed nodes already do this implicitly.

**Fairness.** The source offers only an informal fairness notion and admits (footnote 15) that it lacks a formal criterion. Its claim of superiority holds only relative to that notion. Mind-readers that punish the specific algorithm A-FDT, or any problem rewarding disagreement with a copy of Fiona, are acknowledged to be unfavorable, so A-FDT's advantage is not universal.

**Tractability.** The source analyzes idealized minimal models and expects bounded approximations to share qualitative behavior. That is an expectation, not a result.

## 7. Conclusion

A-FDT is Equation (4): maximize expected utility under $\mathrm{do}(\mathrm{fdt}(P,G,x)=a)$. It changes CDT's intervention point from physical act to decision-function output, and it replaces conditioning on observations with a switch of which function-node is intervened on. Where subjunctive dependence is correctly encoded in $G$, it one-boxes against predictors, smokes despite lesion correlations, pays the hitchhiker, refuses blackmail, and stays in Damascus. Its weak point is the one the authors stress: Equation (4) works *given* a graph encoding logical dependence, and no principled method yet exists for obtaining one. Applying A-FDT to a new problem is therefore a question of careful modeling, of deciding what actually depends on one's decision procedure, followed by routine expected-utility calculation.