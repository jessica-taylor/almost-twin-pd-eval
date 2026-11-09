# A-FDT: Choosing the Output of Your Own Decision Function

## 1. The question A-FDT asks

Decision theories inside the expected-utility tradition agree on how to value outcomes and disagree about which hypothetical to evaluate. Evidential decision theory (EDT) asks which act would be the best *news*. Causal decision theory (CDT) asks which physical act *causes* the best outcome. Yudkowsky and Soares's "Functional Decision Theory: A New Theory of Instrumental Rationality" proposes a third question. The agent should ask which *output of the decision function she is computing* yields the best outcome.

In the paper's words, the functional decision theorist treats "one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

This essay works from the paper's Equation (4) in Section 5. That equation selects an **action** given the agent's model and her observations. I call this version **A-FDT** (action functional decision theory). The paper notes, in footnotes 7 and 16, that the authors' "preferred formalization" instead optimizes over *policies*, meaning maps from observations to actions. I call that variant **policy-FDT** and treat it as a separate theory. Throughout, I mark which claims come from the paper and which are my own interpretation.

## 2. The common skeleton

All three theories maximize a quantity of the form (the paper's Equation 1)

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\hookrightarrow$ is a connective for "decision hypotheticals." Following Joyce, the paper treats the interpretation of $\hookrightarrow$ as the only free parameter: the theories are "disagreeing about the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model $M$. For each action $a$ she builds a hypothetical $M^{a\hookrightarrow}$, computes an expected value $V_a$ from it, and takes the argmax. The paper stresses that hypotheticals are "decision-theoretic instruments constructed from beliefs," not beliefs themselves. Write $V := \mathcal U(\textsc{Outcome})$. The paper's three equations are:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) \tag{2}
$$
$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}
$$
$$
\text{A-FDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big) \tag{4}
$$

## 3. Reading Equation (4)

**The model.** The pair $(P,G)$ is a probability distribution $P$ together with a graph $G$. In CDT, $G$ encodes causal structure. In A-FDT, $G$ encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly." It tells the agent how changing a *logical* variable propagates to other variables.

**The intervention node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model that stands for the output of the A-FDT algorithm on the agent's own inputs. The underlines denote dequoting: the variable's *name* depends on the actual $P$, $G$ and $x$. The paper calls this self-reference "harmless." The agent needs only a variable that *represents* her output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows such self-representations are constructible.

**The operator.** Pearl's $\mathtt{do}$ sets the node to $a$ and recomputes everything downstream of it in $G$, leaving everything else fixed.

The paper identifies two differences from CDT.

1. **Where the intervention happens.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type: the function's output, which may also drive a twin's act, a predictor's simulation, or a future self's behavior.
2. **What observations do.** CDT conditions on $\textsc{Obs}=x$. A-FDT does *not* condition. Instead, the observation determines *which node* gets intervened on: $\textsc{fdt}(\underline P,\underline G,\underline x)$ versus $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second difference is easy to miss and drives the theory's most surprising verdicts. Because the hypothetical is not conditioned on $x$, setting the function's output can change the probability that the agent sees $x$ at all.

**The underlying notion.** The paper calls the relevant relation *subjunctive dependence*. "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Causal dependence is a special case of it. Mere statistical correlation is not. The slogan: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

**Agreement in simple cases.** If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, except its dependence on the $\textsc{fdt}$ node, then
$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$
and all three theories agree. They diverge only when something other than the act itself tracks the agent's decision. Predictors, twins and copies are the standard cases.

## 4. A working recipe

To apply A-FDT to a new case, I propose the following procedure. It assembles what the paper does in its worked examples into explicit steps.

1. **List the observations.** Enumerate the possible inputs $x$ the agent might receive (for example, *full* versus *empty*, or *letter* versus *no letter*). Each one gets its own node $\textsc{fdt}(\cdot,\cdot,x)$.
2. **Add arrows from each node.** Draw an arrow from $\textsc{fdt}(\cdot,\cdot,x)$ to everything whose value is computed from that output. This includes the agent's own act in the branch where she sees $x$, and any predictor, twin or simulation that models the function on input $x$. Do **not** add arrows to things that are merely statistically correlated with the act, such as a lesion.
3. **Wire the act node.** Make $\textsc{Act}$ a deterministic switch: whichever observation actually occurs selects which $\textsc{fdt}$ node controls the act.
4. **Put priors on everything else.** This includes priors over the *other* $\textsc{fdt}$ nodes, which represent how the agent would act on inputs she is not currently facing.
5. **Score each action.** For the actual $x$ and each $a$, compute $\mathbb E[V \mid \mathtt{do}(\textsc{fdt}(\cdot,\cdot,x)=a)]$ over the whole model, without conditioning on $x$. Choose the argmax.

## 5. Worked examples

### Twin prisoner's dilemma

Both agents compute the same function, so one node $\textsc{fdt}$ points to both acts. Setting $\textsc{fdt}=C$ yields $(C,C)$ and \$1,000,000. Setting $\textsc{fdt}=D$ yields $(D,D)$ and \$1,000. A-FDT cooperates. Its stated reasoning: "My twin and I follow the same course of reasoning—this one."

### Newcomb's problem (99% accurate predictor)

The node $\textsc{fdt}$ points both to $\textsc{Act}$ and to $\textsc{Prediction}$.

- $\mathtt{do}(\textsc{fdt}=\textit{onebox})$ gives box B full with probability 0.99, so the expected value is $0.99\times 10^6 = 990{,}000$.
- $\mathtt{do}(\textsc{fdt}=\textit{twobox})$ gives box B full with probability 0.01, so the expected value is $0.01\times 1{,}001{,}000+0.99\times1{,}000=11{,}000$.

A-FDT one-boxes. (The paper's figure of \$990,000 for Fiona is correct. Its \$999,000 for Eve, the paper's EDT agent, appears to be a slip, since the same arithmetic applies to her.)

The paper anticipates an objection. If the agent is nearly sure box B is full, why not grab the extra \$1,000? Because under A-FDT, "for her to two-box, the FDT algorithm would have to output *twobox*." In that hypothetical the predictor, being good at reasoning about A-FDT, predicts accordingly. No retrocausation is involved. The paper's own analogy compares the agent and the predictor's model to two well-functioning calculators computing $6288+1048$ in different places.

### Smoking lesion

The lesion causes both a taste for smoking and cancer. Nothing models the decision function, so the $\textsc{fdt}$ node has no arrow to $\textsc{Cancer}$.

The paper formalizes the problem with two utility functions, $\mathcal U_S$ (for lesion-havers) and $\mathcal U_R$ (for those without the lesion). Correspondingly there are two function nodes. $\textsc{Act}$ copies $\textsc{fdt}(\underline{P_S},\underline G)$ if the agent has the lesion and $\textsc{fdt}(\underline{P_R},\underline G)$ otherwise. Intervening on the $S$-node leaves $P(\textit{lesion})=p$ unchanged, so smoking beats refraining by $p\cdot\$1{,}000$. A-FDT smokes, so it one-boxes and smokes under a single rule.

The general lesson is that A-FDT differs from CDT only where something *models the function*. The paper is candid that this problem is "badly confused." It recommends that philosophers abandon it.

### Transparent Newcomb and Parfit's hitchhiker

This is where the observation-indexing does real work. The predictor fills box B iff it predicts the agent one-boxes *upon seeing it full*. The graph has two function nodes, $\textsc{fdt}(\cdot,\textit{full})$ and $\textsc{fdt}(\cdot,\textit{empty})$. $\textsc{Prediction}$ depends on the *full* node, and $\textsc{Prediction}$ also determines which node controls $\textsc{Act}$. Let $q$ be the prior that the agent two-boxes when the box is empty. Seeing a full box, the agent computes:

$$
\begin{aligned}
\mathtt{do}(\textsc{fdt}_{\textit{full}}=\textit{one}):&\quad 0.99\cdot 10^6 + 0.01\cdot q\cdot 10^3 = 990{,}000+10q,\\
\mathtt{do}(\textsc{fdt}_{\textit{full}}=\textit{two}):&\quad 0.01\cdot 1{,}001{,}000+0.99\cdot q\cdot 10^3=10{,}010+990q.
\end{aligned}
$$

(The paper prints the second constant as "\$110,00," a typo for \$10,010.) A-FDT one-boxes while looking at two full boxes.

The essential move is that the hypothetical is not conditioned on $\textsc{Obs}=\textit{full}$. In the two-boxing hypothetical, the agent mostly sees an *empty* box. The paper argues that this case is structurally identical to paying the driver in Parfit's hitchhiker. It supports the verdict with three arguments: from precommitment, from the value of information, and from utility, which it treats as the decisive one.

### XOR blackmail

A predictor sends a letter iff exactly one of two things holds: (i) there are no termites and the agent will pay, or (ii) there are termites and the agent won't pay. EDT pays, because conditioning on paying drives the probability of termites to zero.

In A-FDT's graph, $\textsc{fdt}(\cdot,\textit{letter})$ points to the predictor and hence to whether the letter is sent, but **not** to $\textsc{Infestation}$. With prior $p$ on termites, the infestation loss is about $p\cdot 10^6$ whatever the agent does. Paying adds a cost of $\$1{,}000$ in the worlds where the letter arrives, and refusing adds nothing. So A-FDT refuses.

CDT also refuses, but its hypotheticals differ. Asked what would have happened had it paid, CDT says it would still have received the letter, which implicitly makes the inerrant predictor err. A-FDT says it would not have received the letter.

### Mechanical blackmail

A blackmailer runs a damaging program iff she predicts the agent would pay on receiving the notice. CDT and EDT pay. For A-FDT, $\mathtt{do}(\textsc{fdt}_{\textit{blackmail}}=\textit{refuse})$ makes being blackmailed nearly impossible, so A-FDT refuses.

With predictor error rate $\epsilon$, refusing costs $\epsilon\cdot10^6$ in expectation and paying costs about \$1,000. A-FDT therefore refuses iff $\epsilon<10^{-3}$. The paper's 0.0009 case matches this: \$900 against \$1,000, so refuse. Its "0.011%" case, where A-FDT is said to pay, is consistent only if 0.11% was intended. At 0.011% the refusal cost is \$110, and A-FDT would still refuse.

### Death in Damascus

Death predicts the agent's location perfectly, so $\textsc{fdt}$ points to both the agent's location and Death's. Either choice means death, so A-FDT stays and saves the \$1,000 cost of fleeing. CDT, by contrast, is unstable here and, on the paper's argument, can refuse a genuinely random coin that would give a 50% chance of survival.

## 6. What the paper leaves open, and how I would fill it in

**(a) Where $G$ comes from.** The paper concedes this is "perhaps the largest open problem": there is no analogue of Pearl's methods for discovering subjunctive dependence. Equation (4) "works *given* a graph."

My proposed operational rule: add an arrow from $\textsc{fdt}(\cdot,x)$ to a variable $Z$ iff $Z$'s mechanism *evaluates* the agent's function on input $x$, or a sufficiently faithful model of it. Twins, simulations, predictors that reason about the agent's algorithm, and the agent's future selves facing the same decision all qualify. Pure common causes and coincidences do not.

Imperfect modeling belongs in noise variables like $\textsc{Accurate}$, not in a weakened arrow. This rule fits every example in the paper, but it is my assumption. Hard cases fall outside it: partial similarity (a "twin" who shares 80% of one's reasoning) and predictors that rely on statistics about agents of one's type rather than modeling the algorithm itself.

**(b) Whether to condition on $x$.** Equation (4) as written omits $\textsc{Obs}=x$. Yet the paper's transparent-Newcomb section writes the quantity as $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}_{\textit{full}}=a,\ \textsc{Obs}=\textit{full}))$, while its actual calculation sums over worlds where the box is empty. The prose settles the matter: A-FDT "does not react to observations by conditioning." The paper also notes that the earlier Timeless Decision Theory, which both conditions and changes the intervention node, suffers a harmful "double update."

I therefore read Equation (4) literally. The observation enters only through the choice of node.

**(c) Priors over the agent's other nodes.** Calculations under A-FDT need priors such as $q$ on how one would act given other inputs. In the paper's examples the answer is insensitive to $q$. In general it need not be.

A natural refinement, my own, is to set those priors at a fixed point: the values A-FDT itself would output on those inputs. This is solvable when the nodes do not interact. When they do interact, choosing all of them jointly is exactly what **policy-FDT** does. That suggests why the authors prefer policy-FDT. A-FDT optimizes one coordinate of the policy while holding the others at their priors, and that can fall short of the policy optimum in multi-agent coordination cases. The paper says only that the difference "makes a difference in certain multi-agent dilemmas."

**(d) Counterpossibles.** Since the function's output is a logical fact, intervening on it is counterpossible. A $\mathtt{true}(\varphi)$ operator would be the principled tool, but "it's not clear how to define" one. Using a supplied $G$ with Pearl's $\mathtt{do}$ is a workaround.

The paper argues the difficulty is technical, not philosophical. It also claims deterministic CDT faces a parallel puzzle about "control" of its own act, so this cannot favor CDT over A-FDT.

**(e) Fairness.** The paper claims A-FDT does at least as well as rivals on "fair problems," meaning those where outcomes depend only on the agent's behavior in the dilemma at hand. It admits that it has no formal definition of fairness. A problem that punishes anyone who acts like a copy of the A-FDT agent defeats A-FDT, and the paper acknowledges this.

## 7. Dominance and stability

Every way of constructing hypotheticals induces its own dominance notion. CDT-dominance favors two-boxing. FDT-dominance holds subjunctive dependencies fixed, and under it two-boxing is dominated.

The paper concludes that dominance is not neutral ground and prefers to judge theories by utility achieved. It also claims A-FDT is reflectively stable in fair problems: holding a blackmail letter, an A-FDT agent would not want to switch to CDT. It "always act[s] as [it] would have precommitted to act," without needing commitment devices.

## 8. Conclusion

A-FDT is CDT with the intervention moved. It intervenes on a logical node representing the output of one's own decision function on one's actual input, rather than on a physical act. It handles observations by choosing which node to intervene on, not by conditioning.

This single change accounts for one-boxing, smoking, cooperating with twins, paying the hitchhiker's driver, and refusing blackmailers. It also yields the surprising verdict that one should leave \$1,000 behind while looking at two full boxes.

The theory is only as good as the dependency graph $G$ it is given. Constructing $G$, interpreting counterpossibles, setting priors over one's off-path behavior, and deciding between A-FDT and policy-FDT remain open. The paper presents these as the main research problems. My suggested rules are one workable way to apply the theory in the meantime.

**Reference.** Yudkowsky, E. and Soares, N. "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.