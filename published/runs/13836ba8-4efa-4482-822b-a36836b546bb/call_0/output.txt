# A-FDT: Choosing the Output of Your Own Decision Function

## 1. Introduction

Decision theory has long been organized around one dispute: when you deliberate about an act, which *hypothetical* worlds should you compare? Evidential decision theory (EDT) compares worlds obtained by conditioning on the act. Causal decision theory (CDT) compares worlds obtained by causally intervening on the act. Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a third answer. The agent should intervene on the **output of the mathematical function that she is computing**, and should let that change propagate to everything that depends on the function's output. Their paper summarizes the guiding question as: "Which output of this very function would yield the best outcome?"

This essay examines the version of the theory given by Equation (4) of their Section 5. In that version the agent intervenes on the output of her decision function *at her current input* and selects an **action**. I call this **A-FDT** (action functional decision theory). The label matters because the authors say their own preferred formalization is different. Footnote 7 states: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." I will call that variant *policy-selecting FDT* and keep it separate. As we will see, the two can come apart.

Throughout, I mark which claims belong to the source and which are my own reconstructions or proposals.

## 2. The common frame: expected utility over hypotheticals

All three theories in the paper maximize expected utility in the form (their Equation 1)

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed." Following Joyce's representation theorem, the authors treat the interpretation of $\hookrightarrow$ as the only free parameter. They quote Joyce: "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

The authors describe a deliberating agent as follows. She holds a world-model $M$. For each candidate action she builds a hypothetical from $M$, scores it, and picks the best. Hypotheticals, they stress, "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs." Write $V = \mathcal U(\textsc{Outcome})$. The two rival theories are:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a) \quad\text{(Eq. 2)}
$$

$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x) \quad\text{(Eq. 3)}
$$

Here $G$ is a Pearl-style causal graph, and $\mathtt{do}$ severs the incoming arrows of the intervened node and recomputes everything downstream of it.

## 3. The A-FDT rule

A-FDT keeps the machinery of $\mathtt{do}$ but moves the point of intervention. The world-model must contain variables for the outputs of mathematical functions, including the agent's own decision procedure. Let

$$
D_x \;:=\; \textsc{fdt}(\underline P, \underline G, \underline x)
$$

denote the node representing "what the FDT algorithm outputs when run on inputs $P$, $G$, $x$." The underlines mark dequoting: the node's *name* is built from the model itself. The authors handle this self-reference by quining via Kleene's recursion theorem. The agent needs a variable *representing* her output, not knowledge of its *value*. Equation (4) is then

$$
\boxed{\;\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\, \mathbb E\big(V \,\big|\, \mathtt{do}(D_x = a)\big)\;}
$$

The source identifies two differences from CDT.

1. **What is intervened on.** CDT intervenes on $\textsc{Act}$, a physical fact about the agent's body. A-FDT intervenes on $D_x$, a logical fact about what a function returns. In Peirce's terms, CDT intervenes on the *token* and A-FDT on the *type*. Every node that $G$ marks as depending on $D_x$ moves with it. That includes the agent's own body, a twin running the same reasoning, and a predictor's model of the agent.
2. **How observations are used.** CDT conditions on $\textsc{Obs}=x$. A-FDT instead uses $x$ to pick *which node* to intervene on. When the history changes from $x$ to $y$, the intervention point moves from $D_x$ to $D_y$.

The second point has a striking consequence. Inside an A-FDT hypothetical, the agent's observation can itself be downstream of $D_x$. She may then evaluate an action by imagining a world in which she would have seen something else.

### Subjunctive dependence: what goes into $G$

The graph $G$ must encode **subjunctive dependence**. Two physical systems computing the same function both "subjunctively depend" on that function, as two working calculators computing $6288+1048$ both depend on its value. The source's slogan is:

> *Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*

Causal dependence is a special case: a scribe copying a calculator's output depends on that output both causally and subjunctively. Mere statistical correlation does not count. Two calculators that happen to be pink do not depend on each other's colour. In decision problems the relevant contrast is between a **predictor**, which "builds an accurate model of the agent and reasons about her behavior," and a **lesion**, which "does no such thing." The predictor's prediction is a child of $D_x$ in $G$; the lesion is not.

Since $D_x$ takes one value as a matter of logic, interventions on it are *counterpossible*. The authors call the lack of a satisfactory account of counterpossible reasoning "the main drawback of FDT relative to CDT at this time." Equation (4) sidesteps the problem by taking $G$ as an *input*, exactly as CDT takes the causal graph as given.

## 4. Worked examples

All numbers below are in utility-dollars.

### Newcomb's problem

A predictor that is 99% accurate fills opaque box B with \$1,000,000 iff she predicts one-boxing. Transparent box A holds \$1,000.

In A-FDT's graph (the source's "Fiona" graph), $D$ is a parent of both $\textsc{Act}$ and $\textsc{Prediction}$, and a noise node $\textsc{Accurate}$ also feeds $\textsc{Prediction}$:

| Hypothetical | $P(\text{full})$ | $\mathbb E V$ |
|---|---|---|
| $\mathtt{do}(D=\textit{onebox})$ | 0.99 | $0.99\cdot 10^6 = 990{,}000$ |
| $\mathtt{do}(D=\textit{twobox})$ | 0.01 | $0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000$ |

A-FDT one-boxes. CDT's graph has $\textsc{Act}$ as the intervened node, cut off from $\textsc{Prediction}$. Whatever $p = P(\text{full})$ is, two-boxing wins by \$1,000.

The source anticipates the objection that, being sure she one-boxes and therefore that the box is full, the agent should then grab both boxes. Its answer is that the hypothetical for two-boxing is one in which the *function* outputs two-box, and in that world the predictor's model outputs two-box as well. No retrocausation is involved. In the source's words, "she just thinks it is foolish to imagine her action changing without also imagining $\text{FDT}(P^F, G^F)$ taking on a different value."

### The smoking lesion

A lesion causes both a taste for smoking and, 99% of the time, cancer. Smoking itself is harmless and worth \$1,000. The source formalizes the lesion as determining *which utility function* the agent has: $\mathcal U_S$ (likes smoking) or $\mathcal U_R$ (values smoking at $-\$1$). There are therefore two possible decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$, and the lesion selects which one controls $\textsc{Act}$.

Neither node is a parent of $\textsc{Cancer}$, so intervening leaves $P(\text{lesion}) = p$ unchanged. The source computes the expected values as

- smoke: $p(\$10{,}000+\$1{,}000) + (1-p)(\$990{,}000 + q\,\$1{,}000)$;
- refrain: $p(\$10{,}000) + (1-p)(\$990{,}000 + q\,\$1{,}000)$.

Here $q$ is the agent's prior that the *other* node smokes. Smoking wins by $p\cdot\$1{,}000$, so A-FDT smokes.

The lesson is that one formula yields one-boxing and smoking together. What separates the two cases is the graph, not the rule.

### Transparent Newcomb

Both boxes are transparent. Box B is filled iff the predictor predicts the agent would one-box *upon seeing it full*. The agent sees it full.

The graph contains $D_{\text{full}}$ and $D_{\text{empty}}$. $\textsc{Prediction}$ depends on $D_{\text{full}}$, and the prediction (through what is shown) determines which node controls $\textsc{Act}$. Let $q$ be the prior that $D_{\text{empty}}$ takes both boxes. The expected values are:

- $\mathtt{do}(D_{\text{full}}=\textit{onebox})$:
  - accurate (0.99): full box, one-box, \$1,000,000;
  - inaccurate (0.01): empty box, $D_{\text{empty}}$ acts, worth $q\cdot\$1{,}000$;
  - total: $\$990{,}000 + 0.01q\cdot\$1{,}000$.
- $\mathtt{do}(D_{\text{full}}=\textit{twobox})$:
  - inaccurate (0.01): full box, two-box, \$1,001,000;
  - accurate (0.99): empty box, worth $q\cdot\$1{,}000$;
  - total: $\$10{,}010 + \$990q$.

(The extracted source prints the second total garbled as "\$110,00 + q·\$990." The arithmetic gives \$10,010.) A-FDT one-boxes while looking at a full box.

The source's main defense is the equivalence with **Parfit's hitchhiker**: paying the driver after arriving in the city is the same decision as leaving \$1,000 behind in front of two full boxes. It adds three supporting arguments: from precommitment, from the value of information, and from utility. Of these it treats the argument from utility as primary.

### Blackmail

**Mechanical blackmail.** A blackmailer runs a damaging program (\$1,000,000 loss) only if she predicts the agent would pay \$1,000 to stop it. When A-FDT receives the letter, it intervenes on $D_{\text{blackmail}}$.

- $\mathtt{do}(\textit{pay})$: the agent is blackmailed and pays. Expected value $-\$1{,}000$.
- $\mathtt{do}(\textit{refuse})$: the agent is blackmailed only if the predictor errs, with probability $\varepsilon$. Expected value $-\varepsilon\cdot\$10^6$.

So A-FDT refuses iff $\varepsilon < 10^{-3}$. The source's example uses $\varepsilon = 0.0009$, where A-FDT refuses although the letter is in hand. It then says that at an error rate of "0.011%" she pays. By the computation above, paying requires $\varepsilon > 0.1\%$, so that figure looks like a slip for 0.11%. The structural point is unaffected.

**XOR blackmail.** A predictor sends a letter iff exactly one holds: no termites and the agent will pay, or termites and the agent won't pay. Let $p$ be the prior on termites.

- $\mathtt{do}(D_{\text{letter}}=\textit{pay})$ yields $-p\cdot10^6 - (1-p)\cdot 10^3$.
- $\mathtt{do}(D_{\text{letter}}=\textit{refuse})$ yields $-p\cdot 10^6$.

A-FDT refuses, as CDT does, but for a different reason. Asked what would have happened had it paid, A-FDT answers "I would not have received the letter." CDT answers that a known-infallible predictor would have erred.

### Death in Damascus

Death predicts the agent perfectly and waits wherever she will be. Fleeing costs \$1,000. In A-FDT's graph Death's appointment book is a child of $D$:

- $\mathtt{do}(D=\textit{stay})$: Death is in Damascus, value $0$.
- $\mathtt{do}(D=\textit{flee})$: Death is in Aleppo, value $-1{,}000$.

A-FDT stays, without CDT's deliberational instability. One further step is my own inference, not something the source computes. Suppose the agent is offered a *truly* random coin for \$1. Death cannot predict it, so in A-FDT's hypothetical the coin gives survival with probability $\tfrac12$. Buying it is worth $\$500{,}000 - \$1$, and A-FDT buys. The source argues that CDT, including CDT with Joyce-style ratification, declines the coin.

## 5. When A-FDT agrees with its rivals, and what "dominance" means

The source notes that all three theories agree whenever every correlation between $\textsc{Act}$ and other variables is *caused by* $\textsc{Act}$. Then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(D = a)].
$$

Divergence requires correlations of other kinds: predictors, twins, or common-cause structure.

On dominance, the source argues that "every method for constructing hypotheticals gives rise to its own notion of dominance." Two-boxing dominates only under CDT counterfactuals. Under FDT counterfactuals, which hold subjunctive dependencies fixed, one-boxing dominates. Dominance is therefore not a neutral arbiter. The source instead appeals to utility achieved in *fair* problems, meaning problems whose outcomes depend only on the agent's behaviour, not on her decision procedure as such. It admits that this notion is not yet formalized.

## 6. Applying A-FDT: an operational recipe and its open points

The following procedure is my reconstruction. Each step notes how much the source determines.

**Step 1: Model.** Build $P$ over the problem's variables, including a node $D_x$ for your decision function at your current input, and nodes $D_y$ for its outputs at other inputs you might have received. (The source uses this structure in the transparent Newcomb and blackmail graphs.)

**Step 2: Dependence edges.** Draw an edge from $D_x$ into every variable whose value is fixed by computing or accurately modelling $D_x$. This includes your own action, a predictor's prediction, and a twin's action. Represent predictor error as a separate noise parent. Correlations with no such computational route, such as lesions or coincidences, go through ordinary causal nodes. (This is the source's account. *How* to decide which edges exist is the open problem it flags: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory.")

**Step 3: Intervene, don't condition.** For each $a$, compute $\mathbb E(V\mid \mathtt{do}(D_x=a))$ by propagating along $G$. Do not additionally condition on $\textsc{Obs}=x$.

On this last instruction the source is slightly inconsistent. Equation (4) contains no conditioning on $x$. In the transparent Newcomb section, however, the displayed objective is written with "$\textsc{Obs}=\textit{full}$" inside the expectation. The worked computation there assigns weight to the branch where the box is empty, so it cannot have conditioned on seeing it full. The footnote on Timeless Decision Theory also warns that conditioning on evidence *and* moving the intervention point "creates a kind of 'double update' which proves harmful in practice." I therefore take Equation (4) literally. Observations act only through the choice of $D_x$. A hypothetical may contradict what you actually see whenever $G$ makes that observation a descendant of $D_x$.

**Step 4: Choose.** Take the argmax. The source specifies no tie-breaking rule. I suggest any fixed rule, such as lexicographic order. Because $D_x$ is a function, ties must be broken *deterministically* so that predictors can model the outcome.

### Open point 1: the other-input nodes, and why "A-" matters

In Step 3, every $D_y$ with $y\neq x$ is left at its prior; it is not intervened on. In the source's examples this prior (their $q$) never changes the verdict, and they remark that "it won't matter if Fiona has some uncertainty." In general, though, it can matter. This is the gap between A-FDT and policy-selecting FDT.

The following illustration is my own. Two exact copies of an agent sit in separate rooms. One is shown a red card and the other a blue card, and both know this setup. Each says "left" or "right." Both get 1 if both say left, 2 if both say right, and 0 otherwise. The red-card copy runs A-FDT on $D_{\text{red}}$ and holds $D_{\text{blue}}$ at a prior with $P(D_{\text{blue}}=\textit{right}) = r$:

$$
\mathbb E V(\textit{left}) = 1-r,\qquad \mathbb E V(\textit{right}) = 2r.
$$

If the agent believes her other-input self says left ($r<1/3$), she says left, and the belief is self-confirming. Both copies say left and earn 1. Policy-selecting FDT chooses a whole map $\pi:\{\text{red},\text{blue}\}\to\{L,R\}$ and picks the constant policy $R$, earning 2. A-FDT thus inherits an equilibrium-selection problem from its treatment of other inputs. This fits the source's remark that the action/policy distinction "only matters in multi-agent dilemmas so far as we can tell."

My practical suggestion is this. When an A-FDT user must supply priors over $D_y$, she should set them to the values the *best policy* would assign. That amounts to adopting policy-selecting FDT, which is a substantive extra assumption.

### Open point 2: partial subjunctive dependence

The source treats imperfect predictors through noise nodes. It says nothing about *similar but non-identical* algorithms, such as a near-twin or a human who roughly models you. A reasonable extension, which is mine rather than the source's, is a stochastic edge: $P(\textsc{Other}=a\mid \mathtt{do}(D_x=a)) = \rho$. Here $\rho$ is your credence that the other system's output tracks your function's output on this question. A-FDT then interpolates smoothly. At $\rho=1$ it is full twin reasoning; when the other system is merely correlated through a common cause, it reduces to CDT.

Estimating $\rho$ is exactly the unsolved problem of discovering subjunctive dependence, now in quantitative form.

### Open point 3: counterpossibles

The source sketches an ideal version, $\arg\max_a \mathbb E(V\mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a))$, but admits that "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) replaces $\mathtt{true}$ with $\mathtt{do}$ on a supplied graph. A-FDT is therefore exactly as reliable as the graph it is given. Its normative content lies largely in the instruction to put predictors, but not lesions, below $D_x$.

## 7. Philosophical motivation in brief

The source's case rests on three main ideas.

**The "global perspective."** The agent asks "What would the entire universe look like if the FDT algorithm behaved differently?" rather than asking what her body's motion would cause.

**Parity of control.** A deterministic CDT agent cannot really "control" her act-token either. So, the authors argue, any objection that FDT agents cannot control their function's output applies equally to CDT.

**Reflective stability.** An A-FDT agent holding a blackmail letter has no wish to self-modify into CDT. By her own hypotheticals, an algorithm that pays would be blackmailed more often. CDT, by contrast, recommends self-modification away from CDT in future dilemmas, though not in ongoing ones.

The authors concede that A-FDT's verdicts in transparent Newcomb and mechanical blackmail are "odd conclusions." They answer that both CDT and FDT hypotheticals contain impossibilities: CDT imagines infallible predictors erring, and FDT imagines seeing what it did not see. The question is which impossibilities are useful to entertain.

## 8. Conclusion

A-FDT is CDT with a different point of intervention:

$$
\text{A-FDT}(P,G,x) = \arg\max_a \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big).
$$

It intervenes on the logical output of one's own decision function at the current input. It propagates that change to every system that computes or accurately predicts the function. It uses observations to select the intervention node rather than conditioning on them. Fed the right graphs, this single rule one-boxes in Newcomb's problem, smokes in the smoking lesion, pays in Parfit's hitchhiker, refuses both blackmails, and stays calmly in Damascus.

Its limits are equally clear. Equation (4) takes the subjunctive-dependence graph as given, and it holds the agent's outputs at other inputs at their priors. The first limitation is the open problem the source itself names. The second is where A-FDT parts company with the authors' preferred policy-selecting FDT, and where a careful user must supply additional assumptions.

---

**Reference.** Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (v2). Works mentioned through it: Joyce (1999), Pearl (2000), Gibbard & Harper (1978).