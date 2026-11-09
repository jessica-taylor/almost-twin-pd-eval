# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision procedure given by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality". The paper calls the theory FDT. I use "A-FDT" for the Equation (4) procedure throughout, and I name every other theory separately: causal decision theory (CDT) and evidential decision theory (EDT).

The paper's central slogan is that the agent treats her decision as "the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Where CDT intervenes on a physical act, A-FDT intervenes on the *type*, the output of the decision function, and lets every dependence on that output propagate.

## 2. The formal definition

All three theories maximize expected utility,

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differ only in how they read the hypothetical connective $\hookrightarrow$. The paper leans on Joyce's remark that theories "disagree about the epistemic perspective from which actions are to be evaluated."

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **A-FDT (Eq. 4):**

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \,\Big|\, do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The ingredients:

- $P$ is a probability distribution over the agent's world-model variables. It includes variables for outputs of mathematical functions, such as $6288+1048$.
- $G$ is a graph encoding how changing a *logical* variable changes other variables. This covers causal links, but also links between a function and every physical system that computes or models it.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model representing the output of the A-FDT procedure itself on those inputs. Underlines denote dequoting, and the self-reference is harmless via quining (Kleene's recursion theorem). The agent need not know the node's value in order to have a node representing it.
- $do$ is Pearl's operator: set the node, recompute its descendants, and leave everything else alone.

The paper identifies two differences from CDT. First, the intervention site is the decision-function node rather than the physical act. Second, observations are handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT instead *changes which node it intervenes on*, namely $\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$. The paper says the observation-indexed node is why A-FDT "does not react to observations by conditioning."

The paper also notes that its preferred formalization intervenes over *policies* (maps from observations to actions). It sets this aside because it only matters in multi-agent cases.

## 3. Subjunctive dependence

The graph $G$ must represent *subjunctive dependence*. Two things subjunctively depend on a function if they would both change were the function's output different. Examples are two calculators computing the same sum, or a predictor's accurate model of the agent. The paper's relations among kinds of dependence:

- Causal dependence is a special case of subjunctive dependence. A scribe copying a calculator's output depends on it in both senses.
- Mere statistical correlation is not subjunctive dependence. Two pink calculators are correlated in colour, but changing one would not change the other.

So A-FDT preserves exactly the correlations between act and world that are logically or causally grounded, and breaks the merely statistical ones. The paper's summary is that EDT "respects too many action-environment correlations, while CDT respects too few."

Intervening on a node whose value is a logical necessity means evaluating counterpossibles, as with "elliptic curves if Fermat's last theorem were false." The paper concedes this is "the main drawback" of the theory. Its response is to treat the difficulty as technical, since humans reason about such things tolerably, and to demand only that the agent's imagined changes track "all and only those things that subjunctively depend on the output."

## 4. Open problems and my proposed operational reading

**What the source says.** Eq. (4) works *given* $G$. The paper states: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem." It also lacks a $\mathtt{true}(\phi)$ operator for conditioning on false logical sentences (footnote 9), which is why $G$ is taken as an input.

**What I add, and flag as my own proposal.** For practical application, I suggest this checklist for building $G$.

1. List the processes in the problem whose behaviour is produced by computing, modelling, or being a copy of the agent's decision procedure, such as twins and predictors. Draw arrows from the $\mathrm{fdt}$ node to these.
2. Treat any process that merely shares a common cause with the agent's act, such as a lesion, as not downstream of $\mathrm{fdt}$.
3. For imperfect predictors or twins, keep the arrow but include a stochastic noise node, as the paper does with $\mathrm{Accurate}$.
4. If the agent could receive different observations, make one $\mathrm{fdt}(\cdot,x)$ node per observation. Let any node that determines which observation arrives, such as a prediction, also select which $\mathrm{fdt}$ node controls $\mathrm{Act}$.

The difficulty in this recipe is step 1. Whether a given system really tracks the agent's procedure is a modelling judgement, and A-FDT does not tell you how to make it.

## 5. Worked applications

I use the paper's models and numbers.

### Newcomb's problem

$G$: the node $\mathrm{fdt}$ points to both $\mathrm{Act}$ and $\mathrm{Prediction}$. $\mathrm{Prediction}$ also depends on $\mathrm{Accurate}$ (0.99), and $\mathrm{Prediction}$ determines $\mathrm{Box\ B}$.

- $do(\mathrm{fdt}=\text{onebox})$: Act is onebox, and Box B is full with probability 0.99. The value is $0.99\cdot 10^6 = \$990{,}000$.
- $do(\mathrm{fdt}=\text{twobox})$: Box B is full with probability 0.01. The value is $0.01\cdot 1{,}001{,}000+0.99\cdot 1000=\$11{,}000$.

So A-FDT one-boxes. No retrocausation is involved. The agent is only declining to imagine her output changing while the predictor's model of that output stays fixed.

The objection "she is nearly sure the box is full, so she should take both" fails because the hypothetical for two-boxing is not "same world, different act." It is "this function outputs twobox," and in that hypothetical the box is probably empty.

### Smoking lesion

Here the graph differs. The lesion affects $\mathrm{Act}$ (via preferences) and $\mathrm{Cancer}$, but the $\mathrm{fdt}$ node feeds only $\mathrm{Act}$. The paper handles this by giving the agent two utility functions, $\mathcal U_S$ and $\mathcal U_R$. $\mathrm{Act}$ is determined by the lesion and by two nodes, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$. Intervening does not change $P(\text{lesion})=p$. Smoking is better by $p\cdot\$1000$, so A-FDT smokes.

With the same procedure, A-FDT one-boxes in one problem and smokes in the other, because $G$ differs between them. The paper adds that the lesion problem is contrived, and it recommends abandoning it.

### Transparent Newcomb and Parfit's hitchhiker

Upon seeing a full box, A-FDT intervenes on $\mathrm{fdt}(\cdot,\text{full})$. Two-boxing at that node makes the predictor probably have predicted differently, so the agent would probably be seeing an *empty* box and running $\mathrm{fdt}(\cdot,\text{empty})$ instead. With $q$ the probability that she two-boxes on an empty box:

- onebox: $\$990{,}000+0.01\,q\cdot\$1000$
- twobox: about $\$11{,}000+q\cdot\$990$

A-FDT one-boxes even while looking at a full box. The paper notes this is structurally the same as paying in Parfit's hitchhiker: the driver rescues only agents predicted to pay.

### Blackmail

In the paper's mechanical blackmail problem, intervening on $\mathrm{fdt}(\cdot,\text{blackmail})$ gives:

- pay: blackmail is nearly certain, and the loss is $\$1000$.
- refuse: blackmail is nearly absent from the hypothetical.

So she refuses. With a fallible blackmailer, whose error rate is 0.0009, refusing costs $0.0009\cdot\$1{,}000{,}000=\$900$ in expectation, which is below the $\$1000$ cost of paying. The paper says she still refuses, and that at an error rate of 0.011% she pays instead. This is a good illustration of a threshold computed directly from Eq. (4).

In XOR blackmail, A-FDT refuses because the infestation node is not downstream of $\mathrm{fdt}$. EDT pays, conditioning on good news. CDT also refuses, but, as the paper stresses, for the wrong reason. Its hypothetical has the predictor err.

### Death in Damascus

In the hypothetical where the function outputs "flee," Death's book says Aleppo. A-FDT stays and saves $\$1000$. CDT oscillates, and the paper argues it would even decline a $\$1$ truly random coin worth a 50% chance of survival.

### Cases where all three theories agree

If every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$, then $\mathbb E[V|a]=\mathbb E[V|do(a)]=\mathbb E[V|do(\mathrm{fdt}=a)]$. The theories diverge only when predictors or twins create non-causal but subjunctive links.

## 6. Why the paper thinks this is right

Its arguments are largely about performance, plus some structure.

- **Utility.** Predictors that anticipate A-FDT behaviour reward it, and in the paper's examples agents following CDT or EDT do worse. The paper calls this "the argument that gives the others their teeth."
- **Dominance is theory-relative.** CDT's dominance argument assumes CDT-style counterfactuals, so it cannot adjudicate between theories. Each method of building hypotheticals induces its own dominance relation, and under the A-FDT-style relation A-FDT agents never take dominated actions.
- **Precommitment and information.** An A-FDT agent acts as she would have precommitted to act, and it assigns non-negative value to information.
- **Fairness.** Newcomb's predictor responds to the agent's *action*, not to her procedure, so the problem is treated as fair. A problem that punishes an agent for being an A-FDT agent is not. The paper claims A-FDT does well in fair problems but admits no formal criterion of fairness exists. Its footnote gives an example: punishing whoever acts like a copy of Fiona is unfair to her.
- **Parity of "control."** A-FDT's talk of controlling the output type is said to be exactly as problematic as a deterministic CDT agent's talk of controlling a token act.

## 7. Cautions and my own commentary

These points are mine, not the paper's claims.

1. The theory is only as good as $G$. If one misdraws the arrow between predictor and function, A-FDT inherits the error, just as CDT does with a bad causal graph.
2. The paper's claim that A-FDT "never loses in fair dilemmas" is stated as an observation ("the authors have not been able to construct" a counterexample), not a theorem.
3. The observation-indexed intervention means the agent can evaluate hypotheticals in which her actual observations differ. This is what makes refusal in the blackmail and transparent cases coherent, but it can feel as if she ignores her evidence. The paper's reply is that she responds to evidence by choosing the node to intervene on.
4. Bounded agents must approximate Eq. (4), and the paper says only that approximations should keep the qualitative difference from CDT and EDT.

## 8. Conclusion

A-FDT replaces the question "what if my body did something else?" with "what if this very decision function output something else?", and evaluates the answer in a model where all subjunctively dependent variables move with it. The resulting rule, Eq. (4), is formally close to CDT: an expected utility maximization over $do$-surgery, with a different intervention site and a different treatment of observations. In the paper's examples it one-boxes in Newcomb's problem, smokes in the lesion problem, pays in Parfit's hitchhiker, refuses blackmail, and stays in Damascus. The main open problem is how to learn or specify the dependence graph $G$, and until that is solved, applying the theory depends on careful modelling.