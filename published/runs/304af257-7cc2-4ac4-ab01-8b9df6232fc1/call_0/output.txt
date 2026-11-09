# A-FDT: Choosing as the Output of a Function

## 1. The question

Most decision theories ask a question about a physical act. Causal decision theory (CDT) asks which act *causes* the best outcome. Evidential decision theory (EDT) asks which act would be the best *news*. The theory in this essay asks something different. Yudkowsky and Soares put it this way: a rational agent follows a procedure that asks "Which output of this decision procedure causes the best outcome?"

I will call the formal version of this theory **A-FDT** (action functional decision theory). It is the theory defined by Equation (4) of Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality*. The source simply calls it "FDT." The prefix "A-" marks a distinction the authors make in two footnotes: the version in Equation (4) chooses an *action* given an observation. Their "preferred formalization" instead chooses a *policy*, meaning a map from observations to actions. Section 6 returns to this distinction.

The essay has five parts:

1. The formal definition.
2. A step-by-step recipe for applying it.
3. Worked examples.
4. The points the source leaves open, with my proposed readings, explicitly labelled as mine.
5. A short assessment.

## 2. The expected-utility skeleton

All three theories (EDT, CDT, A-FDT) share one template. Following Gibbard and Harper, an agent with observation history $x$ chooses an action $a$ from a finite set $\mathcal A$ to maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

Here $\hookrightarrow$ is a "decision hypothetical" connective. The source invokes Joyce's representation theorem: expected-utility theorists agree on how to value prospects but disagree about "the epistemic perspective from which actions are to be evaluated." The three theories differ only in how they read $\hookrightarrow$.

- **EDT** conditions on the act and the observation:
  $$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a).$$
- **CDT** performs a Pearl intervention on the physical act, using a causal graph $G$:
  $$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E\big(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x\big).$$
- **A-FDT** (Equation 4) intervenes on a node that represents the output of the decision procedure itself:
  $$\boxed{\;\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}$$

The underlines denote dequoting. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the *name of a variable* inside the agent's model, and that variable stands for "whatever the A-FDT algorithm returns on inputs $(P,G,x)$." The model therefore contains a variable describing its own decision procedure's output. The authors call this self-reference harmless. The agent does not need to know the variable's value in order to represent it, and Kleene's recursion theorem shows such self-representing structures can be built.

## 3. The ingredients of Equation (4)

**The world-model $(P,G)$.**
- $P$ is a probability distribution over variables.
- $G$ is a graph that says how changing one variable propagates to others.

In CDT, $G$ encodes only causal structure. In A-FDT, the source requires that $G$ encode "logical, mathematical, computational, causal, etc." structure. In particular, $G$ must say which variables *subjunctively depend* on the output of the agent's decision function.

**Subjunctive dependence.** The source's analogy is two well-functioning calculators computing $6288+1048$. If either outputs 7336, so does the other. Neither causes the other's output; both depend on the same mathematical fact. The source illustrates the relation with three kinds of system:

- An accurate predictor's prediction subjunctively depends on the agent's decision function.
- A twin running the same reasoning depends on it in the same way.
- A lesion that merely correlates with the agent's choice does *not* depend on it.

Causal dependence is a special case of subjunctive dependence. Mere statistical correlation is not. The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**Surgery.** $\mathtt{do}(\textsc{fdt}(\cdot)=a)$ is Pearl's operator applied to the logical node. It works in two steps:

1. Cut the node's incoming dependencies and set it to $a$.
2. Recompute every descendant of the node in $G$, leaving non-descendants at their prior distribution.

The descendants include the agent's physical $\textsc{Act}$ and every modelled copy or prediction of the function.

**How observations enter.** This is the subtle point. The source says CDT "responds to observation by Bayesian conditionalization," whereas A-FDT "responds to observation by changing which node it intervenes upon." When the observation history changes from $x$ to $y$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead of $\textsc{fdt}(\underline P,\underline G,\underline x)$.

As written, Equation (4) contains no conditioning on $\textsc{Obs}=x$. The consequence is important. In A-FDT's hypotheticals, the observation actually received can itself become improbable. The agent may judge that if her function had a different output, she would have *seen something else*.

**The counterpossible worry.** The function's output on a given input is a logical fact. Imagining a different output is therefore imagining something impossible, a "counterpossible." The source admits there is no satisfactory theory of a $\mathtt{true}(\phi)$ operator for such antecedents. It sidesteps the problem by making the dependency graph $G$ an *input*: "we require that the relevant logical dependency structure be given as an input to FDT, in the same way that the relevant causal structure is given as an input to CDT."

## 4. An operational recipe

The source does not give a step-by-step list in this form. The following is my reconstruction of how Equation (4) is applied in its examples.

1. **List the instances of your decision function.** Identify every place your decision function, run on some input, is evaluated: your own body, predictors' models of you, twins. For each input $y$ that matters (each observation you might receive), create a node $F_y=\textsc{fdt}(\underline P,\underline G,\underline y)$.
2. **Wire the graph.** Let $\textsc{Act}$ depend on whichever $F_y$ corresponds to the observation you will actually receive. That routing may itself depend on other variables, such as a prediction. Draw an edge from $F_y$ to every predictor that predicts your behaviour on input $y$. Connect merely correlated factors, like a lesion, through ordinary causal edges only, not through $F_y$.
3. **Assign priors.** Give priors to exogenous variables (noise, termites, lesions) and to the *other* function nodes $F_{y'}$ with $y'\neq x$.
4. **Intervene and propagate.** For each $a\in\mathcal A$, set $F_x=a$ by intervention, propagate through $G$, and compute $\mathbb E[V]$.
5. **Choose.** Output the argmax.

### Example 1: Newcomb's problem

The setup: a predictor that is 99% accurate fills box B with \$1,000,000 iff it predicts one-boxing. Box A holds \$1,000. The graph has $F\to\textsc{Act}$ and $F\to\textsc{Prediction}\to\textsc{BoxB}$.

- $\mathtt{do}(F=\text{onebox})$: box B is full with probability 0.99. Expected value $=0.99\times 10^6 = \$990{,}000$.
- $\mathtt{do}(F=\text{twobox})$: expected value $=0.01\times 1{,}001{,}000 + 0.99\times 1{,}000 = \$11{,}000$.

A-FDT one-boxes. CDT reaches the opposite answer because $\mathtt{do}(\textsc{Act})$ leaves $\textsc{BoxB}$ at its prior $p$ under either act. Two-boxing then wins by \$1,000 whatever $p$ is.

The source stresses that no backward causation is assumed. The agent "just thinks it is foolish to imagine her action changing without also imagining" her function's output changing. That output is what the predictor tracks.

### Example 2: The smoking lesion

A lesion causes both a taste for smoking and, 99% of the time, cancer. Smoking itself is worth \$1,000. Surviving is worth \$1,000,000.

The structural fact for A-FDT is that cancer does not depend on the output of the decision function. The source formalizes the problem as follows:

- The lesion fixes which utility function, and therefore which world-model ($P_S$ or $P_R$), the agent runs.
- $\textsc{Act}$ is controlled by $\textsc{fdt}(\underline{P_S},\underline G)$ if she has the lesion and by $\textsc{fdt}(\underline{P_R},\underline G)$ otherwise.

Intervening on the $P_S$ node does not change $P(\text{lesion})=p$. With $q$ the prior that the other procedure smokes, the two options are worth:

- Smoke: $p(\$10{,}000+\$1{,}000)+(1-p)(\$990{,}000+q\$1{,}000)$.
- Refrain: $p(\$10{,}000)+(1-p)(\$990{,}000+q\$1{,}000)$.

Smoking wins by $p\cdot\$1{,}000$. A-FDT therefore agrees with CDT here and disagrees with EDT. The source also judges this problem "badly confused," since EDT's distribution would misdescribe a population of EDT agents. It recommends abandoning the problem.

### Example 3: The transparent Newcomb problem

Both boxes are transparent. Box B was filled iff the predictor foresaw one-boxing *upon seeing a full box*. The agent sees it full.

There are two function nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction depends on $F_{\text{full}}$. The prediction also determines which node controls $\textsc{Act}$. Let $q$ be the prior that $F_{\text{empty}}$ two-boxes; its correct value is 1.

- $\mathtt{do}(F_{\text{full}}=\text{onebox})$: with probability 0.99 the box is full and she one-boxes, getting \$1,000,000. With probability 0.01 it is empty, she acts by $F_{\text{empty}}$, and gets $q\cdot\$1{,}000$. Total: $\$990{,}000+\$10q$.
- $\mathtt{do}(F_{\text{full}}=\text{twobox})$: with probability 0.01 the predictor errs, the box is full, and she gets \$1,001,000. With probability 0.99 the box is empty and she gets $q\cdot\$1{,}000$. Total: $\$10{,}010+\$990q$.

(The source's extraction prints this as "\$110,00"; the arithmetic gives \$10,010.)

A-FDT one-boxes *while looking at a full box*. In her two-boxing hypothetical she would most likely have seen an empty box. This is the "observations are not conditioned on" feature at work.

The source argues that the case is structurally identical to Parfit's hitchhiker. Paying the driver once safely in the city corresponds to leaving the \$1,000. The source defends the verdict with three arguments: from precommitment, from the value of information, and from utility.

### Example 4: Blackmail

**XOR blackmail.** A predictor sends a letter iff exactly one of two things holds: (i) no termites and you will pay; (ii) termites and you will not pay.

- EDT pays, since conditioning on paying makes termites impossible.
- A-FDT refuses. Intervening on $F_{\text{letter}}$ changes whether the letter is sent but not whether termites are present.
- CDT also refuses, for a different reason. In the source's words, its hypothetical "would say that the predictor erred."

**Mechanical blackmail.** A blackmailer runs a damaging program only if she predicts you will pay \$1,000 to stop it.

- $\mathtt{do}(F_{\text{blackmail}}=\text{refuse})$ makes being blackmailed nearly impossible.
- A-FDT therefore refuses, even while holding the letter. Being refusers means such agents are not targeted in the first place.

The source adds a sensitivity analysis. Suppose the blackmailer wrongly predicts payment with probability 0.0009. Refusing then costs an expected $0.0009\times\$1{,}000{,}000=\$900$, less than the \$1,000 payment, so A-FDT refuses. At an error rate of 0.011% the comparison flips, and the source says Fiona "pays."

### Example 5: Death in Damascus

Death is a perfect predictor and will be wherever you go. Fleeing to Aleppo costs \$1,000.

Under A-FDT, intervening on the function moves Death's appointment book along with the agent. Both options lose the \$1,000,000, so A-FDT stays and saves \$1,000.

CDT is unstable here. Each belief about where it will go recommends the other city. On the source's analysis, CDT would even decline to pay \$1 for a truly random coin that gives a 50% chance of survival.

## 5. Dominance and fairness

The source rejects the dominance argument for two-boxing as question-begging. Dominance holds the rest of the world fixed while the act varies, and what "fixed" means depends on the hypothetical connective. So "every method for constructing hypotheticals gives rise to its own notion of dominance."

A-FDT has its own version. Action $a$ dominates $b$ if, holding subjunctive dependencies fixed, switching the algorithm's output from $b$ to $a$ is never worse and sometimes better. A-FDT never takes an action dominated in this sense.

The source evaluates decision theories by utility in "fair" problems: those where "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb's predictor counts as fair because it rewards *one-boxers*, not followers of a particular theory. The source admits that fairness has not been formalized. Its own footnote gives an example: a problem that punishes anyone who matches a copy of Fiona is intuitively unfair, yet hard to exclude in a principled way.

## 6. Open questions and my proposed readings

The following points are where the source underdetermines application. My proposals are labelled as such.

**(a) Where does $G$ come from?** The source calls "deducing the structure of subjunctive dependencies from observation and experiment" perhaps "the largest open problem." Equation (4) is a function of $G$, so verdicts are only as good as the graph.

*My proposal:* draw an edge $F_y\to Z$ exactly when $Z$ is computed by a process whose reliability as a predictor of *your input–output behaviour on $y$* is part of your model. This covers accurate predictors, simulations, and twins running the same reasoning. Correlations that run through shared causes of your preferences or inputs (lesions, upbringing) should go through ordinary causal edges. This captures the source's predictor/lesion contrast. It does not settle intermediate cases, such as a crude predictor that uses only demographics. My tentative view is that such a predictor tracks your inputs, not your function, and so gets no $F$-edge. That is an additional assumption.

**(b) Priors on the other function nodes.** Equation (4) leaves the priors on $F_{y'}$, $y'\neq x$, free. In the source's examples they do not change the verdict, and the source notes the correct values ($q=1$, $q=0$). But they could matter in close cases.

*My proposal:* set them to what A-FDT itself returns on those inputs, computed recursively where feasible. Where that is not feasible, use one's best estimate. Doing this consistently is essentially computing a policy, which leads to point (c).

**(c) Action versus policy.** The source's "preferred formalization" intervenes on a policy node $\pi:\mathcal X\to\mathcal A$:
$$\pi^*=\arg\max_\pi \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),\qquad \text{act } \pi^*(x).$$
The source says the difference arises only in some multi-agent dilemmas and sets it aside. A-FDT optimizes $F_x$ one input at a time, holding the other nodes at their priors. If those priors are self-consistent, A-FDT's choice coincides with the policy optimum whenever the problem's value separates across inputs. It can diverge when coordinating outputs across several inputs matters jointly. The source's examples are of the first kind. This explanation of where the two can diverge is my analysis, not a claim made in the source.

**(d) Conditioning on $\textsc{Obs}$.** The displayed expression in the transparent-Newcomb section writes the observation inside the conditioning bracket. Equation (4) omits it, and the computation that follows clearly does not condition on box B being full. I follow Equation (4).

This is not a cosmetic choice. Conditioning on the observation *and* moving the intervention point would recreate the "double update" that the source attributes to Timeless Decision Theory and calls "harmful in practice." With both updates, the transparent-Newcomb agent would two-box.

**(e) Ties and degenerate models.** The source does not specify tie-breaking. Any fixed rule is consistent with Equation (4). Note that, unlike EDT, A-FDT has no difficulty with probability-zero actions, because interventions are well defined regardless of the prior on the act.

## 7. Assessment

A-FDT keeps CDT's machinery (an argmax over interventions in a graph) and changes two things. It intervenes on the *type*, the output of a fixed function, rather than the *token* physical act. And it handles observations by relocating that intervention rather than by conditioning.

These changes yield the following verdicts:

- one-boxing in Newcomb's problem;
- smoking in the smoking lesion problem;
- paying in Parfit's hitchhiker;
- one-boxing in transparent Newcomb;
- refusing in both blackmail cases;
- staying put in Death in Damascus.

The source argues that A-FDT acts as CDT would have precommitted to act, never assigns negative value to information, and is reflectively stable in fair problems.

The costs are equally clear. A-FDT presupposes a counterpossible dependency structure that it does not show how to learn. Its verdicts can feel strange, such as refusing a blackmailer while holding the letter. Its claimed superiority rests on a notion of fairness that has not been formalized.

To decide an unfamiliar case:

1. Ask what depends on the *output of your reasoning* rather than on your body's motion.
2. Draw those dependencies.
3. Intervene on the function node for your actual input.
4. Let the hypothetical worlds, including ones where you would have seen something different, decide.

## Reference

Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060 (Section 5, Equation 4).