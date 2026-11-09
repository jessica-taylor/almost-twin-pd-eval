# Action Functional Decision Theory (A-FDT): Intervening on What Your Decision Procedure Outputs

## 1. The question A-FDT asks

Classical decision theory pictures a rational agent as choosing among available acts. It then evaluates each act by asking what the world would be like if that act were performed. The two standard theories answer this "what if" differently:

- **Evidential decision theory (EDT)** conditions on the act. It asks which act would be the best *news*.
- **Causal decision theory (CDT)** intervenes on the act. It changes the act and everything causally downstream of it, and holds everything else fixed.

Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a third answer. Their slogan is that a rational agent treats "one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The object varied in the hypothetical is therefore not the physical act token. It is the *output of the decision function* on the agent's current inputs.

This essay treats the version of the theory given by Equation (4) of the paper's Section 5. That equation chooses an **action** by intervening on a node representing the decision function's output on the agent's actual inputs. I call it **A-FDT** (action functional decision theory). The paper mentions in footnotes 7 and 16 that the authors' "preferred formalization" instead iterates over *policies*, meaning maps from observations to actions. They say the difference "makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." I keep the two apart. Equation (4) is the object of study, and the policy variant is mentioned only where the contrast clarifies something.

## 2. The common expected-utility skeleton

The paper presents EDT, CDT and A-FDT as expected-utility theories that differ only in how they build hypotheticals. Each prescribes an action $a\in\mathcal A$ maximizing

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),
$$

where:

- $x$ is the observation history;
- $\hookrightarrow$ is the "decision hypothetical" connective.

Following Joyce, the authors treat the interpretation of $\hookrightarrow$ as the free parameter. In Joyce's words, decision theories disagree "about the epistemic perspective from which actions are to be evaluated."

Write $V=\mathcal U(\textsc{Outcome})$. The three rules are then:

$$
\text{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a) \tag{2}
$$
$$
\text{CDT}(P,G,x)=\arg\max_a \mathbb E\big(V\mid do(\textsc{Act}=a),\textsc{Obs}=x\big) \tag{3}
$$
$$
\text{A-FDT}(P,G,x)=\arg\max_a \mathbb E\big(V\mid do(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big) \tag{4}
$$

Here $G$ is a graph over the variables of $P$, and $do$ is Pearl's intervention operator. In (4), $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a *variable in the agent's own model* whose name is fixed by the model and the observation. The underlines mark dequoting, so the expression names the node standing for "what the A-FDT algorithm returns on input $(P,G,x)$." The agent does not need to know this node's value in order to intervene on it. The authors appeal to Kleene's recursion theorem ("quining") to argue that the self-reference is harmless.

The paper itself flags two structural differences between (3) and (4):

1. **Point of intervention.** CDT sets the physical act. A-FDT sets a logical fact: the output of a fixed function on fixed inputs.
2. **Treatment of observation.** CDT *conditions* on $\textsc{Obs}=x$. A-FDT does not condition on it. Instead, observation changes *which node* is intervened upon. Moving from history $x$ to $y$ moves the intervention from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second difference is easy to overlook, and it drives A-FDT's most distinctive verdicts.

## 3. Subjunctive dependence and the graph $G$

What must $G$ encode? The paper's informal answer is **subjunctive dependence**. Two physical systems "subjunctively depend" on a function when both compute it. Two working calculators computing $6288+1048$ are the paper's example: if (counterpossibly) that sum were different, both displays would differ. Some features of this notion:

- **Causal dependence is a special case.** A scribe copying a calculator's output depends on it causally and therefore subjunctively.
- **Mere statistical correlation is not enough.** Two coincidentally pink calculators do not depend on one another.

The paper's central structural claim is the analogy:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

In Peircean terms, CDT intervenes on the *token* act and A-FDT intervenes on the *type*.

What the source commits to about $G$ is limited. Given $G$, Equation (4) is a fully specified procedure. But the authors say plainly that how to *construct* $G$ is open: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." The underlying semantics would be a $\mathtt{true}(\phi)$ operator that updates beliefs on a possibly false logical sentence. The authors grant that "it's not clear how to define a $\mathtt{true}$ operator." The graph $G$ is their workaround, supplied as input in the same way CDT is given a causal graph. Footnote 8 adds that only the independence relations encoded by the graphs matter, not the graphical formalism itself.

## 4. A working recipe for A-FDT (my operationalization)

To make A-FDT usable on new cases, I propose the following recipe. It is consistent with every worked example in the paper, but the specific rules for drawing edges are **my assumptions**, not the source's.

**Step 1: Output nodes.** For each observation history $y$ the agent might face in the problem, create a node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ with range $\mathcal A$. The paper does exactly this in the transparent Newcomb and blackmail problems, with nodes such as $F_{\text{full}}$, $F_{\text{empty}}$, $F_{\text{letter}}$ and $F_\emptyset$.

**Step 2: The act node.** Model $\textsc{Act}$ as a deterministic switch. Whatever determines which observation the agent receives selects which $F_y$ sets the act:

$$
\textsc{Act} = F_{\textsc{Obs}}.
$$

**Step 3: Dependence edges.** Draw an edge $F_y\to Z$ exactly when $Z$ is produced by a process that computes, simulates, or reliably predicts the A-FDT output on input $y$. Examples are a predictor's forecast, a twin's choice, or a copy's action. Do **not** draw an edge to a variable that is merely correlated with the act through a common physical cause, such as a lesion. My justification is the paper's own criterion: a predictor "builds an accurate model of the agent and reasons about her behavior; a carcinogenic lesion does no such thing." Prediction error enters as an independent noise parent, like $\textsc{Accurate}$ in the paper's Newcomb network.

**Step 4: Ordinary causal structure.** Keep the remaining causal structure as CDT would have it.

**Step 5: Priors on non-intervened output nodes.** Give each $F_{y'}$ with $y'\neq x$ a prior. The source treats these priors as parameters ($q$ in several examples) and remarks that "it doesn't matter" in its cases. In general they can matter. My proposal is to set each such prior to the output A-FDT itself would return on $y'$, computed recursively. This is a fixed-point requirement, and it matches the paper's parenthetical remarks that "the correct $q$" is 0 or 1. Where no consistent fixed point exists, the policy formulation is, I think, the principled repair: choose the whole map $y\mapsto a$ jointly. That is a different theory, not A-FDT.

**Step 6: Evaluate and choose.** For each $a$, compute $\mathbb E(V\mid do(F_x=a))$ *without* conditioning on $\textsc{Obs}=x$, and take the argmax.

Step 6 follows Equation (4) literally, but the source is not fully consistent on this point. In the transparent Newcomb computation the text writes $\mathbb E(V\mid do(F_{\text{full}}=a,\textsc{Obs}=\text{full}))$, which includes the observation. The surrounding prose and arithmetic, however, assign substantial weight to worlds where the box is empty. They therefore follow Equation (4): no conditioning. I take Equation (4) and the arithmetic as authoritative. Conditioning *and* switching nodes is the "double update" the paper attributes to Timeless Decision Theory and calls "harmful in practice."

## 5. Worked examples

### 5.1 Newcomb's problem

The setup is the standard one, with a predictor who is 99% accurate. The model contains a single output node $F$ (no observations), with edges $F\to\textsc{Act}$ and $F\to\textsc{Prediction}$, plus noise. Then:

$$
\mathbb E(V\mid do(F{=}\text{one}))=0.99\cdot 10^6 = 990{,}000,
$$
$$
\mathbb E(V\mid do(F{=}\text{two}))=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000 = 11{,}000.
$$

A-FDT one-boxes. (The source gives \$999,000 for Eve's one-boxing figure but \$990,000 for Fiona's. The latter is the correct value.)

CDT intervenes on $\textsc{Act}$ with the prediction held fixed at some probability $p$. It gains \$1,000 for every $p$ and two-boxes. The source stresses that A-FDT's reasoning involves no retrocausation: the agent "just thinks it is foolish to imagine her action changing without also imagining $\text{FDT}(P,G)$ taking on a different value."

### 5.2 Twin prisoner's dilemma

The twin computes the same function, so the graph has $F\to\textsc{MyAct}$ and $F\to\textsc{TwinAct}$. Setting $F=C$ yields $(C,C)$ and \$1,000,000. Setting $F=D$ yields $(D,D)$ and \$1,000. A-FDT cooperates. The source's voting and gym examples have the same structure. In each, several decision instances that are relevantly identical all hang off one output node.

### 5.3 Smoking lesion

Here the graph differs, even though the probability tables can be the same as in Newcomb. The lesion causes cancer, and nothing predicts the agent's function, so cancer gets no edge from any $F$.

The source's formalization is subtle. The lesion fixes the agent's *utilities* (whether she likes smoking), so there are two candidate decision computations:

- $F_S$, run by an agent who likes smoking;
- $F_R$, run by one who does not.

The act is given by $\textsc{Act}=F_S$ if the lesion is present and $F_R$ otherwise. Intervening on $F_S$ leaves $P(\text{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes.

The general moral for applying the theory: **identical correlations can receive different graphs**, and the difference turns entirely on whether some process tracks the agent's function. The paper notes that this is why the agent's graph from Newcomb's problem "cannot be re-used," whereas CDT can reuse its graph by mere renaming.

### 5.4 Transparent Newcomb and Parfit's hitchhiker

Both boxes are visible. The predictor fills box B iff she predicts one-boxing *upon seeing it full*. The agent sees it full, so A-FDT intervenes on $F_{\text{full}}$. The graph has $F_{\text{full}}\to\textsc{Prediction}\to\textsc{BoxB}$, with $\textsc{Act}=F_{\text{full}}$ if the box is full and $F_{\text{empty}}$ otherwise. Let $q=P(F_{\text{empty}}=\text{two})$.

$$
\text{one: } 0.99\cdot10^6 + 0.01\cdot q\cdot 1{,}000 = 990{,}000+10q,
$$
$$
\text{two: } 0.99\cdot q\cdot 1{,}000 + 0.01\cdot1{,}001{,}000 = 10{,}010+990q.
$$

(The source prints the second figure as "\$110,00 + q·\$990"; the constant should be \$10,010.) One-boxing wins for every $q\in[0,1]$. The agent one-boxes *while looking at a full box*, because in the hypothetical where her function outputs "two", she would most likely have been shown an empty box.

Parfit's hitchhiker has exactly the same structure: pay on arriving in the city. The paper's defense rests on three points:

- the **precommitment argument**: "it is rational to predictably behave as though one has precommitted";
- the **value of information**: A-FDT never pays to be blindfolded;
- **utility achieved**, which the authors regard as primary.

### 5.5 XOR blackmail versus mechanical blackmail

These two cases are good tests of whether one has the graph right.

*XOR blackmail.* The letter is sent iff (no termites and the agent pays) or (termites and the agent refuses). Termites are upstream and are not predicted from $F$. Intervening on $F_{\text{letter}}$ changes *whether the letter arrives*, but not the probability of termites. Paying therefore just costs \$1,000 in the worlds where the letter arrives, and A-FDT refuses. CDT also refuses, though for a different reason. EDT pays, because conditioning on paying makes termites impossible given the letter.

*Mechanical blackmail.* The blackmailer runs the damaging program iff she predicts that the agent pays when blackmailed. The relevant edge is $F_{\text{blackmail}}\to\textsc{Blackmailer}$. Under $do(F=\text{pay})$ the agent is blackmailed and loses \$1,000. Under $do(F=\text{refuse})$ she is (almost) never blackmailed. A-FDT refuses even while holding the letter.

Suppose the predictor wrongly predicts payment with probability $\varepsilon$. Then refusing costs about $\varepsilon\cdot10^6$ and paying costs \$1,000, so A-FDT refuses iff $\varepsilon<0.001$. The source's $\varepsilon=0.0009$ ("loses \$900 in expectation") agrees with this. Its claim that A-FDT pays at "0.011%" does not: that error rate gives \$110 < \$1,000, so the agent would still refuse. The intended figure was presumably 0.11%.

### 5.6 Death in Damascus

Death's appointment book is written from a perfect prediction of the agent's function, so $F\to\textsc{DeathLocation}$. Both interventions yield death, and staying saves \$1,000, so A-FDT stays. There is no instability. CDT, by contrast, oscillates or ratifies a mixed state. The paper argues that CDT then values a genuinely random coin (a 50% chance of survival) at less than \$1, because its hypotheticals already treat Death's location as independent of the act.

## 6. Dominance, fairness, and what the theory claims

**Dominance.** The CDT dominance argument for two-boxing holds the prediction fixed while varying the act. The authors answer that "every method for constructing hypotheticals gives rise to its own notion of dominance." Under A-FDT's notion, holding the subjunctive dependencies fixed, A-FDT never takes a dominated action. Dominance is therefore not a neutral arbiter between the theories. What decides between them is utility achieved.

**Fairness.** Any theory can be defeated by a problem that rewards agents for *how* they decide, for example "pay those who run EDT." The authors call a problem "fair" roughly when the agent's beliefs are accurate and outcomes depend only on the agent's *behavior* in the problem at hand. Their claim is that they "have not been able to construct an intuitively fair dilemma where FDT loses to a rival decision theory." Footnote 15 concedes that formalizing fairness is unresolved. A predictor who punishes whoever matches a copy of the agent is a case where A-FDT necessarily loses, and it is unclear how to convert such cases into fair analogues.

**Reflective stability.** According to its own hypotheticals, an A-FDT agent never wants to self-modify into some other decision theory mid-problem. The authors call it "reflectively stable in fair problems," and they present this as an advantage over CDT, which recommends abandoning itself for future problems.

**"Control."** The authors anticipate the objection that A-FDT agents imagine they control logical facts or the past. Their reply is a parity argument: a deterministic CDT agent equally evaluates counterfactual acts that it will not in fact perform. "Any principled objection" to controlling the decision type "will also imply that (deterministic) CDT agents cannot 'control' their decision token."

## 7. Open questions and the limits of Equation (4)

1. **Constructing $G$.** Equation (4) is only as good as its dependence graph. My Step 3 rule, "edges to anything that computes or predicts $F_y$", works on clean textbook cases. It is vague about *partial* similarity: a rough model of the agent, an agent running a slightly different algorithm, or a correlation that is half common-cause and half prediction. The source supplies no answer. A natural extension is to weight the edges, so that a predictor's accuracy becomes noise on the $F\to\textsc{Prediction}$ link. The paper already models accuracy this way. But how to estimate *logical* similarity between algorithms remains unsolved.

2. **Counterpossibles.** For the true value $a^*$, the intervention $do(F_x=a)$ with $a\neq a^*$ is a counterpossible: the function's output is logically fixed. The authors call the lack of a theory of counterpossibles "the main drawback of FDT relative to CDT." They also argue that substituting "what if I used a different function" (their FDT′) does not avoid the problem, because predictors track the actual function.

3. **Off-path output nodes.** A-FDT sets only $F_x$ and treats the other $F_{y'}$ as uncertain parameters. In the paper's examples the verdict is robust to their values. In general it need not be, and A-FDT on its own can make choices at different observations that do not cohere as a single policy. This is precisely the gap the authors' preferred policy formulation closes: choose $\pi:\mathcal X\to\mathcal A$ maximizing $\mathbb E(V\mid do(\textsc{fdt}(\underline P,\underline G)=\pi))$. My fixed-point proposal in Step 5 is a partial patch within A-FDT, not a substitute for that formulation.

4. **Bounded agents.** The equations are idealized. The paper only expects approximating agents to inherit the "similar strengths and weaknesses" of the ideal.

## 8. Conclusion

A-FDT keeps the machinery of causal expected utility (a probability model, a graph, and Pearl-style surgery) and changes two things:

- the **variable intervened upon**: the output of the agent's decision function on her actual inputs, rather than her physical act;
- the **role of observation**: it selects which output node to intervene on, rather than being conditioned on.

Two practical consequences follow. When applying A-FDT, the work lies almost entirely in drawing the graph: which processes compute or predict your function, and which observations they cause you to receive. Once the graph is fixed, the decision is mechanical, as in the examples above. A-FDT one-boxes, smokes, cooperates with twins, pays the driver, refuses mechanical blackmail, and stays in Damascus.

What the source leaves open is equally clear: a general theory of subjunctive dependence, a semantics for counterpossibles, a formal criterion of fairness, and the coordination of choices across observations that the policy variant is meant to handle. A-FDT as stated in Equation (4) is a precise conditional procedure, *given* a dependence graph. Supplying that graph in a principled way is the theory's central unfinished task.

*Reference:* E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.