# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision procedure given by Equation (4), Section 5, of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality". In this essay "A-FDT" names that procedure. When I need to mention causal or evidential decision theory, I call them CDT and EDT, following the paper.

The central idea is that the agent treats her decision as the output of a fixed mathematical function. She asks "Which output of this very function would yield the best outcome?" She does not ask which physical act would cause the best outcome (CDT) or which act would be the best news (EDT).

The theory has three parts: an expected-utility shell, a world-model with dependency structure, and an intervention on a logical node. I describe each in turn, then work examples. I also separate what the paper claims from what I add.

## 2. The formal definition

All three theories are expected utility theories. The paper writes expected utility as

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j),$$

where $x$ is the observation history. The theories differ only in how they read "$\hookrightarrow$", the connective for decision hypotheticals. The paper leans on Joyce's representation theorem: the theories disagree about the epistemic perspective from which actions are evaluated, not about value.

For EDT, $\hookrightarrow$ is conditioning on the act. For CDT it is Pearl's $\mathtt{do}$ on the act node. The paper's Equation (4) for A-FDT is

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big(V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

The ingredients are these.

- $P$ is a probability distribution. It includes variables for the outputs of mathematical functions, for example a variable for $6288+1048$ with nearly all its mass on 7336.
- $G$ is a graph saying how changing a logical variable propagates to other variables. It encodes causal and logical dependence together, and is the paper's "subjunctive dependence" structure.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node standing for the output of the A-FDT algorithm itself on inputs $(P,G,x)$. The underlines mean dequoting: the node's name is built from the actual inputs. The self-reference is harmless, and the paper cites Kleene's second recursion theorem (quining). The agent does not need to know the value of the node in order to have a variable representing it.
- $V=\mathcal U(\text{Outcome})$.

The paper names two differences from CDT.

1. A-FDT intervenes on the node for the output of its decision procedure, not on the physical act node.
2. A-FDT does not respond to observation by conditioning. It responds by changing which node it intervenes on: $\mathrm{fdt}(P,G,x)$ becomes $\mathrm{fdt}(P,G,y)$ when the observation changes from $x$ to $y$. The agent evaluates "what if the procedure, run on this input, output $a$", and this can change which observations she would have made.

The paper also writes a conceptual version, $\mathrm{FDT}^*$, using a $\mathtt{true}(\cdot)$ operator that conditions on a logical sentence, and says that operator is not yet definable. The practical definition therefore takes the dependency graph as an input, just as CDT takes the causal graph as an input. A footnote says the authors' preferred formalization iterates over policies (maps from observations to actions) rather than actions, and that this matters only in some multi-agent problems.

## 3. Subjunctive dependence

Two physical systems computing the same function subjunctively depend on it. The paper's picture is two calculators computing $6288+1048$. Subjunctive dependence is related to the other kinds of dependence as follows.

- It is weaker than identity of the computation. A predictor with an imperfect model of the agent, or a nondeterministic agent, gives a weakened but real dependence.
- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Statistical correlation alone is not subjunctive dependence. Two calculators that are both pink share no dependence in this sense, because the Tokyo calculator would still be pink if the Paris one were green.

So A-FDT is to subjunctive dependence as CDT is to causal dependence. CDT intervenes on the token "my act is $a$"; A-FDT intervenes on the type. In the hypothetical for $a$, the agent changes the function's output and everything that depends on it, and holds everything else fixed.

This requires counterpossible reasoning, since the function does not in fact output anything else. The paper acknowledges this as the main drawback and the largest open problem: no theory yet says how to infer subjunctive dependence structure from observation, as Pearl's work does for causation. It argues the difficulty is technical, not philosophical. Humans reason under logical uncertainty, and the agent needs only restricted questions of the form "how would this predictor's output change if my algorithm's output changed?"

## 4. Worked applications

I use the paper's own cases. Numbers are dollars standing in for utilities.

**Newcomb's problem.** The graph has a node $\mathrm{fdt}(P,G)$ with arrows into both Act and Prediction, and Prediction determines Box B. This is the structure of the paper's Fiona graph (Figure 5b). The nodes Accurate (0.99) and Box B are as in the paper's network.

- $\mathtt{do}(\mathrm{fdt}=\text{onebox})$ makes Act = onebox and Box B full with probability 0.99, so EU is about \$990,000.
- $\mathtt{do}(\mathrm{fdt}=\text{twobox})$ makes Box B full with probability 0.01, so EU is about \$11,000.

A-FDT one-boxes. This reasoning contains no retrocausation. The agent simply declines to imagine her act changing while the predictor's model of her procedure stays fixed.

**Smoking lesion.** Here the graph must differ from the one for Newcomb's problem. The lesion is a common cause of the urge to smoke and of cancer, but it does not model the agent's decision function. Cancer is not downstream of the fdt node, so intervening on the node changes the act but not the cancer probability. Smoking gains \$1,000 in every hypothetical, so A-FDT smokes. The dependency graph, not the surface correlation, does the work. The paper itself calls this problem contrived and badly confused, because the agent must be uncertain about her own preferences.

**Transparent Newcomb and Parfit's hitchhiker.** Observation changes which node is intervened on. In the transparent case, with a full box seen, the agent evaluates $\mathtt{do}(\mathrm{fdt}(P,G,\text{full})=a)$.

- If the output is onebox, the predictor (who models this very procedure) fills the box with probability 0.99 and the agent one-boxes, so EU is about \$990,000.
- If the output is twobox, the box is likely empty, and the agent does not run this node but the empty-box node, so EU is small.

A-FDT one-boxes even while looking at a full box. The paper says this is exactly equivalent to paying the driver in Parfit's hitchhiker. The same structure gives refusal in the mechanical blackmail problem. Refusing corresponds to a hypothetical in which the blackmail letter was probably never sent, and the agent in the letter-receiving state is evaluating what her procedure does there.

With an imperfect blackmailer the arithmetic can be done explicitly. In the paper's example the blackmailer errs with probability 0.0009. Paying gives a certain loss of \$1,000. Refusing gives blackmail with probability 0.0009 and a loss of \$1,000,000, which is \$900 in expectation. So A-FDT refuses. At an error rate of 0.011% the comparison reverses and she pays. The decision is a threshold computation, not a slogan about never yielding.

**XOR blackmail and Death in Damascus.** In XOR blackmail, infestation is not downstream of the fdt node, and the node does influence whether the letter is sent. So the agent refuses to pay. In Death in Damascus, Death's location depends on the same function through the appointment book, so A-FDT stays in Damascus and saves \$1,000. It never enters the instability that the paper attributes to CDT.

**Cosmic ray problem.** A-FDT intervenes on the node and does not condition on a statistical correlation between taking \$100 and being hit by a ray, so it takes the \$100. EDT's conditioning does not allow it to break that correlation.

## 5. How the theory handles agreement and disagreement

The paper observes that when every correlation between the act and the world is caused by the act (apart from possible dependence on the fdt node), the three expressions coincide:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)].$$

The theories diverge only when something correlates with the act without being caused by it, which is the signature of predictors, twins and copies. The paper's diagnosis is that EDT's hypotheticals respect too many correlations, CDT's too few, and A-FDT's the right ones.

## 6. Dominance and fairness

**Dominance.** The paper argues that every method of constructing hypotheticals induces its own notion of dominance. The CDT-style dominance of two-boxing is therefore a restatement of CDT's method and not a neutral argument. A-FDT has an analogous dominance principle, under which it never takes a dominated action, and under which one-boxing in Newcomb's problem wins. The paper prefers to compare theories by utility achieved.

**Fairness.** Problems that punish an agent for the decision procedure she uses, as opposed to her action, are unfair, and no theory wins on all of them. The authors claim A-FDT matches or beats the alternatives on "fair" problems, where the outcome depends only on the agent's behavior in the dilemma at hand and the agent's beliefs are accurate. The paper concedes it has no formal definition of fairness, and a footnote shows the difficulty: a problem that punishes agents for acting like a copy of Fiona is unfair to her, but it is not clear how to build its analogue for another theory.

## 7. What the source leaves open, and what I add

The source determines Equation (4) and what it says about the cases above. It leaves open the following.

1. **Where $G$ comes from.** The paper gives no method. In practice the user must supply, for each node, whether it depends on the output of her procedure. My operational heuristic, which is mine and not the paper's, is to ask whether the node is produced by something that models or computes the agent's procedure. Predictors, twins and copies get an arrow from the fdt node, while lesions and other mere common causes do not. If the dependence is only partial, the node should be a noisy function of fdt, as with the 0.99 predictor.

2. **Policies versus actions.** Equation (4) as printed ranges over actions. Using a policy version (the preferred one in the footnotes) is straightforward in single-agent cases, where it agrees with observation-indexed nodes.

3. **The meaning of the unchosen nodes.** In the transparent and blackmail graphs, the nodes for the other observations ($\mathrm{fdt}(\ldots,\emptyset)$ and so on) need priors. The paper notes these priors do not affect the answer in its examples, and the correct values can be derived. I would add the caution that this is a feature of those examples, not a general theorem.

4. **Observation must be handled with care.** Because the agent does not condition on $x$, she still must use $x$ to select the node. I add the practical check that the observation node should be downstream of the nodes it depends on in $G$, as in the paper's Figure 5b where Prediction feeds into Act.

5. **Computational feasibility.** The paper acknowledges that full world-models make the argmax intractable, and expects bounded approximations to inherit the qualitative behavior. Beyond that I say nothing.

6. **Multi-agent cases.** The paper sketches symmetric voting coalitions and self-coordination over time (the gym example), where an agent assumes that others, or future selves facing relevantly identical decisions, share her function. Whether this extends to asymmetric players depends on the unresolved dependency-structure question.

## 8. Philosophical motivation

The paper makes three arguments for the theory.

- **Utility.** The theory does better than CDT and EDT in the paper's cases, and this argument is stated as the primary one.
- **Reflective stability.** The agent has no desire to self-modify, because she already acts as she would have precommitted to act, and no costly commitment devices are needed.
- **Information.** A-FDT does not assign negative value to information, unlike EDT, which would pay to avoid it.

On the charge that A-FDT agents believe they control the past or abstract objects, the paper replies that deterministic CDT agents face the same puzzle about controlling their token act. Both theories use imagined hypotheticals, which the paper calls "decision-theoretic instruments constructed from beliefs", like notes on scratch paper, and not claims about metaphysics. Its conclusion is that each agent should choose from a "global perspective", asking what the whole universe would look like if the algorithm output something different.

## 9. Conclusion

A-FDT is a short definition with a large unfinished foundation. Equation (4) says: build a model that includes the logical node for your own decision function, intervene on that node for each candidate output, and pick the output with the highest expected utility. Observations select which node to intervene on instead of being conditioned on. Everything is determined once the dependency graph is given, and the worked cases show it recommends one-boxing, smoking, paying the driver, and refusing blackmail. What is missing is a principled account of how an agent comes to know that graph and how to reason about the counterpossible interventions. Until that exists, applying A-FDT to a new case requires explicit modeling judgments about which things depend on the agent's procedure, and a reader should treat those judgments as additional assumptions and not as consequences of the source.