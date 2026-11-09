# A-FDT: Deciding by Intervening on the Output of Your Own Decision Function

## 1. The idea

A-FDT is the theory the source paper (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") presents as Equation (4) of Section 5. Its central claim is that an agent should treat her decision as the output of a fixed mathematical function. The question to ask is the paper's: "Which output of this very function would yield the best outcome?" The question is not "Which physical act of mine causes the best outcome?" (causal decision theory, CDT) or "Which physical act of mine would be the best news to hear I took?" (evidential decision theory, EDT).

This essay explains the formal procedure, works through examples, and marks where the paper stops and where my own interpretation begins. I use "A-FDT" for the assigned theory, and I call the rivals CDT and EDT.

## 2. The formal setup

All three theories are expected-utility theories. The paper writes expected utility as

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j),$$

where $\hookrightarrow$ is the connective for decision hypotheticals, $x$ is the observation history, and $\mathcal U$ is a bounded utility function. Following Joyce, the paper holds that the theories differ only in the "epistemic perspective", meaning how $\hookrightarrow$ is interpreted:

- **EDT** (Eq. 2) conditions: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x, \mathrm{Act}=a)$.
- **CDT** (Eq. 3) intervenes on the physical act, using a causal graph $G$: $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$.
- **A-FDT** (Eq. 4):

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is the agent's probability model and $G$ is a graph of dependencies. The underlines denote dequoting. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model representing the output of the A-FDT algorithm run on exactly these inputs. The self-reference is harmless, according to the paper: the agent need not know the value of the node to have a variable representing it, and Kleene's recursion theorem ("quining") shows how such self-representing structures can be built.

The paper names two differences from CDT.

1. **The intervention site.** A-FDT intervenes on a node for the output of a decision function, a logical fact. CDT intervenes on a node for the physical act, which is a token. The paper uses Peirce's distinction: CDT intervenes on the token, A-FDT on the type.
2. **The treatment of observations.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition on observations. Instead, a different observation means a different node to intervene on: $\mathrm{fdt}(\underline P,\underline G,\underline x)$ becomes $\mathrm{fdt}(\underline P,\underline G,\underline y)$. This is why the paper connects the approach to "updateless" ideas.

## 3. Subjunctive dependence and the graph $G$

The graph $G$ carries the substance of the theory. The paper's term for the relevant relation is *subjunctive dependence*. Two systems depend subjunctively on a function when both compute it, so that counterfactually changing the function's output changes both. The paper offers two calculators computing $6288+1048$ as the image. It claims that causal dependence is a special case of subjunctive dependence, and that mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators illustrate the latter.

The paper's analogy is: A-FDT is to subjunctive dependence as CDT is to causal dependence. A CDT hypothetical changes the act and what is causally downstream, holding the rest fixed. An A-FDT hypothetical changes the function's output and everything that subjunctively depends on it, holding the rest fixed. EDT respects too many correlations, because it preserves merely statistical ones. CDT respects too few, because it breaks the correlation with predictors. The paper says A-FDT "gets the balance right".

**What the paper leaves open.** The paper is explicit that it cannot define a general $\mathtt{true}$ operator for conditioning on logical falsehoods (counterpossibles). Its workaround is to require $G$ as an *input*, "in the same way that the relevant causal structure is given as an input to CDT". It calls deducing subjunctive-dependence structure from observation "perhaps the largest open problem". So Eq. (4) is a well-defined procedure only relative to a supplied $G$. The paper also says the equation "rests on shakier philosophical foundations" than the CDT one. I add one remark of my own: any application of A-FDT is only as good as the modeler's judgment about which variables are computed by, or predict, the agent's decision procedure.

## 4. Applying the procedure

A practical recipe, which is my summary and not a quoted algorithm:

1. List the variables of the problem and identify the node(s) $\mathrm{fdt}(\cdot, \cdot, x)$ for each possible observation $x$.
2. Draw edges from those nodes to everything that computes or models the agent's decision: her own act, any twin's act, any predictor's prediction.
3. For each action $a$, set the relevant node to $a$ by intervention. Propagate downstream. Leave variables not downstream of the node, such as lesions, termites, and noise, at their prior values.
4. Compute $\mathbb E[V]$ in each hypothetical and take the argmax.

### Newcomb's problem

The model has a stochastic node Accurate ($0.99$) and the node $\mathrm{fdt}$. Both Act and Prediction are downstream of $\mathrm{fdt}$. Intervening with one-boxing gives Box B full with probability $0.99$ and expected value $\$990{,}000$. Intervening with two-boxing gives full with probability $0.01$ and $\$11{,}000$. So A-FDT one-boxes. The reasoning involves no retrocausation. The agent just declines to imagine her act changing while the predictor's model of her stays put.

### Smoking lesion

The graph differs here. The paper formalizes the lesion as determining which utility function the agent has: $\mathcal U_S$ if she has the lesion, $\mathcal U_R$ otherwise. The two corresponding decision nodes both feed Act. Cancer is not downstream of either, because the lesion does not model the agent's decision. The intervention therefore leaves $P(\text{lesion})=p$ unchanged. Smoking comes out better by $p\cdot\$1{,}000$, so A-FDT smokes. This shows that one criterion handles both problems, and that all the work is done by $G$, which differs between them. The paper itself calls the formalization contrived and recommends abandoning the problem.

### Transparent Newcomb and Parfit's hitchhiker

With the observation "full", the A-FDT agent intervenes on $\mathrm{fdt}(\cdot,\cdot,\textit{full})$. In the hypothetical where that node outputs two-boxing, the predictor, who models that node, leaves Box B empty. The agent then sees an empty box and the empty-box node controls her act. With $q$ the probability that she two-boxes on seeing empty, the paper computes $\$990{,}000+0.01q\cdot\$1{,}000$ for one-boxing and $\$11{,}000+q\cdot\$990$ for two-boxing, so she one-boxes. The paper notes that this is "precisely equivalent" to paying the driver in Parfit's hitchhiker. The paper's own arguments for it are precommitment, non-negative value of information, and utility achieved.

### Blackmail

In the XOR blackmail problem, the node $\mathrm{fdt}(\cdot,\cdot,\textit{letter})$ influences whether the letter is sent and what she does if it is. It does not influence termites. So A-FDT refuses. In mechanical blackmail, refusing corresponds to a hypothetical in which she was never blackmailed. The paper's fallible-predictor variant is a numerical test. Suppose the predictor wrongly predicts payment with probability $0.0009$. Then paying costs \$1,000 for certain, since she is always blackmailed. Refusing costs $0.0009\times\$1{,}000{,}000=\$900$, so she refuses even while holding the letter. If the error rate were $0.011\%$, she would pay.

### Death in Damascus

Death's location depends on the book entry, which depends on a prediction of the agent's decision procedure. A-FDT sees that wherever she goes Death follows, and so stays and saves \$1,000. CDT is unstable here, and the paper argues it would even decline a \$1 truly random coin that gives a 50% chance of survival.

### Coordination

The paper's examples include a ten-person voting game and self-coordination over time (the gym). In both, nearly identical decision procedures make the agents' decisions subjunctively dependent. A-FDT agents therefore vote and go to the gym, while CDT agents do not.

## 5. Philosophical motivation

**Utility as the criterion.** The paper's primary argument is that A-FDT achieves more utility in "fair" problems. It treats dominance arguments as question-begging, because each method of constructing hypotheticals defines its own dominance relation. Two-boxing dominates only relative to CDT counterfactuals, which are like asking us to imagine a calculator outputting $3159$ while holding fixed that $6288+1048=7336$.

**Fairness.** A problem is fair if beliefs are accurate and the payoff depends only on the agent's behavior in the problem, not on which procedure she uses. Newcomb's predictor "punishes *two-boxers*", not CDT agents. The paper admits it has no formal definition of fairness. Footnote 15 notes the difficulty with a problem that punishes any agent who matches a copy of A-FDT.

**No delusion.** The paper says A-FDT agents are no more deluded about "control" than deterministic CDT agents, who also imagine hypothetical worlds in which a fixed act differs. Both consider impossible hypotheticals. They differ only in which ones.

**Reflective stability.** Because the agent acts as she would have precommitted to act, the paper argues she has no reason to self-modify or to pay for binding mechanisms.

## 6. Where my reading goes beyond the source

These points are interpretations or proposals of mine, not claims in the paper.

1. **Policies versus actions.** Equation (4) maximizes over actions. Footnotes 7 and 16 say that the authors' preferred formalization intervenes on a *policy* mapping observations to actions, a difference that matters in multi-agent dilemmas. For the single-agent examples in the paper, the per-observation form of Eq. (4) gives the same answers. When applying it to a new multi-agent case, I would use the policy form, which is a stipulation of mine for safety, not something Eq. (4) itself says.
2. **Imperfect predictors and partial dependence.** The paper handles imperfect correlation through stochastic nodes such as Accurate. A reasonable operational rule is to wire in exactly the noise the predictor's reliability implies, and to hold fixed everything not downstream. I treat this as a modeling convention.
3. **Detecting dependence.** A working heuristic for building $G$ is to ask whether a variable is produced by something that *computes or models* the agent's decision, so that a different output would change it. The paper only gestures at this with the calculator picture and human heuristics. The test is not rigorous. It would misfire on quasi-predictors that are only partly a function of the decision, and the paper does not settle such cases.
4. **Robustness check.** One useful sanity check, drawn from the paper's own reasoning, is that hypotheticals should not require an "inerrant" predictor to err. Carl's hypotheticals violate this. If an A-FDT hypothetical contains a predictor that errs contrary to the problem statement, $G$ is probably missing an edge.
5. **Priors on one's own output.** The paper notes the answer is independent of the prior on one's own action (unlike EDT, where extreme priors "can be made to do anything"). It also notes that probabilities for off-path nodes, such as $q$, drop out or are inconsequential. I take this to mean that A-FDT does not require resolving self-prediction before deciding.

## 7. Limitations

Besides the open problem of constructing $G$, the paper concedes that:

- it lacks a definition of counterpossible conditioning;
- it lacks a formal notion of fairness, so the claim that A-FDT is best on all fair problems is untested;
- it does not know whether A-FDT is optimal, "or even (on a formal level) what optimality consists in";
- its verdicts in transparent Newcomb and blackmail are counterintuitive to many people, and it responds largely by appeal to utility and framing effects.

My own caution is that results like "A-FDT one-boxes" are theorems only given a particular $G$. A skeptic can contest the verdict by contesting the graph, so any real application should state the graph explicitly.

## 8. Conclusion

A-FDT keeps the expected-utility skeleton of CDT and the Pearl-style intervention machinery, but moves the intervention from the physical act to the output of the agent's decision function and replaces conditioning on observations with a change of the intervention node. Everything that subjunctively depends on that function, including predictors, twins, and later selves, moves with the intervention, and everything else stays fixed. This yields one-boxing in Newcomb's problem, smoking in the lesion problem, paying in Parfit's hitchhiker, refusing blackmail, and calm acceptance in Death in Damascus, all from Equation (4). What the theory still needs is a principled account of the dependency graph $G$. Until that exists, A-FDT is a precise procedure whose inputs require judgment.