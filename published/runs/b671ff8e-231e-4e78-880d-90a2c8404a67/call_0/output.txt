# A-FDT: Choosing the Output of Your Own Decision Function

## 1. The question A-FDT asks

Every expected-utility decision theory computes values of the form "how good would things be if I did $a$?" The theories differ in how they construct the hypothetical world that follows the word *if*. Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a theory whose hypotheticals vary something other than the agent's physical act. They vary the output of the mathematical function the agent computes. In their words, the agent should treat "one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

This essay explains the version of that theory given by **Equation (4), Section 5** of the paper. I call it **A-FDT** (action functional decision theory) because its maximization ranges over *actions*. The authors note (footnotes 7 and 16) that their "preferred formalization" iterates over *policies*, meaning maps from observations to actions. That variant is a different object and I mention it only for contrast. My aims are to state Equation (4) precisely, give a procedure for applying it, work through the paper's main examples, and identify where applying the theory requires assumptions the paper does not supply. Claims attributed to the source are marked as such. Proposals of my own are labelled **[my proposal]**.

## 2. The common framework

The source follows Gibbard and Harper and Joyce in treating all three theories as maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $x$ is the observation history and "$\hookrightarrow$" is the connective for decision hypotheticals. Joyce's representation theorem leaves the interpretation of $\hookrightarrow$ as a free parameter. The three theories fill it in as follows, writing $V = \mathcal U(\textsc{Outcome})$.

- **Evidential decision theory (EDT)**, Equation (2):
  $$\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a).$$
  The hypothetical is ordinary conditioning.
- **Causal decision theory (CDT)**, Equation (3):
  $$\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x).$$
  The hypothetical is a Pearl intervention on the physical act node in a causal graph $G$.
- **A-FDT**, Equation (4):
  $$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The underlines denote dequoting. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a *variable in the agent's model* that stands for the output of the A-FDT algorithm when run on this very model and this very observation. The paper notes that this self-reference is harmless. The agent needs a variable that *represents* the value; it does not need to know the value. Kleene's recursion theorem ("quining") shows that such self-representing structures can be built.

The source identifies two differences between Equations (3) and (4):

1. **The point of intervention.** CDT intervenes on a physical token, "my body does $a$." A-FDT intervenes on a logical type, "this function outputs $a$ on this input." Anything else in the world that computes or accurately models that function moves along with the intervention.
2. **How observations enter.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition. Instead, observation *selects which node is intervened on*. When the history changes from $x$ to $y$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ rather than $\textsc{fdt}(\underline P,\underline G,\underline x)$.

The second point has the largest practical consequences, and I return to it below.

## 3. Subjunctive dependence and the graph $G$

The relation that A-FDT tracks the source calls *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The paper illustrates this with calculators. Two working calculators computing $6288+1048$ agree because they compute the same sum, not because one causes the other. On this view causal dependence is a special case of subjunctive dependence. Merely statistical correlation, like two calculators that happen to share a colour, is not subjunctive dependence at all. The source summarizes: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Formally, the ideal operation would be a $\mathtt{true}(\varphi)$ operator that updates $P$ on the counterpossible supposition that the decision function outputs $a$. The paper says plainly that "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) avoids the problem by requiring that $P$ come with a graph $G$, which "tells us how changing a logical variable affects all other variables." Pearl's $\mathtt{do}$ is then reused on that graph. All of the theory's content about which things move with the decision therefore sits in $G$. The paper calls "deducing the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem in the study of functional decision theory."

The practical consequence is that **A-FDT is a function of a modelling choice**. To apply it, one must build $G$.

## 4. An operational recipe for A-FDT

The paper gives worked graphs but no general construction. The following recipe generalizes its figures **[my proposal, though every step is visible in the paper's examples]**.

**Step 1: Enumerate decision inputs.** List the observation histories $x_1,\dots,x_k$ that the agent might have at the moment of choice, including the empty history $\emptyset$. Create one logical node $F_i := \textsc{fdt}(\underline P,\underline G,\underline{x_i})$ for each. If the agent is uncertain about its own utility function, as in the smoking lesion, also create nodes indexed by the distinct world-models it might be running.

**Step 2: Wire the physical act.** $\textsc{Act}$ is a deterministic switch. It equals $F_i$ when the process actually delivers observation $x_i$ (or model $i$). The variables that determine which input is delivered, such as a box's contents or a letter's arrival, are parents of $\textsc{Act}$.

**Step 3: Wire subjunctive dependents.** Every process that computes, simulates, or reliably predicts the function on input $x_i$ gets an arrow from $F_i$. Examples are a twin, a predictor's model, or Death's appointment book. Noise nodes, such as $\textsc{Accurate}$, capture imperfect prediction. Processes that are merely correlated with the act, such as lesions, get *no* arrow from any $F_i$.

**Step 4: Assign priors** to the root nodes, including the $F_j$ nodes that will not be intervened on.

**Step 5: Evaluate.** For the actual history $x$, for each $a$, compute $\mathbb E(V\mid \mathtt{do}(F_x=a))$ by propagating forward through $G$. Output the argmax.

Two features of Step 5 matter.

- **No conditioning on $x$.** The hypothetical for $a$ is allowed to assign low probability to the observation the agent actually has. This is exactly what the paper intends: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have made different observations."
- **One ambiguity in the source.** In the transparent Newcomb section the paper writes the maximand as $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full}))$. That expression appears to include the observation inside the intervention, which contradicts Equation (4). The paper's own computation, however, gives weight to worlds where the box is *empty*. So I read Equation (4) literally, as no conditioning, and treat the extra term as a notational slip. Under the other reading the transparent Newcomb verdict would flip to two-boxing.

## 5. Worked examples

All payoffs are in dollars, used as utility, as in the source.

### 5.1 Twin prisoner's dilemma

Two agents compute the same function, so in the model they share one node $F$ that feeds both acts. Then $\mathtt{do}(F=\textit{C})$ yields $(C,C)$ and \$1,000,000, while $\mathtt{do}(F=\textit{D})$ yields $(D,D)$ and \$1,000. A-FDT cooperates. CDT defects, because its intervention on one physical act leaves the twin fixed.

### 5.2 Newcomb's problem (99% predictor)

Fiona's graph (the paper's figure for her case) has $F\to\textsc{Act}$ and $F\to\textsc{Prediction}\leftarrow\textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$.

- One-box: $\mathtt{do}(F=\text{onebox})$ gives $P(\textit{full})=0.99$, so
  $$\mathbb E(V)=0.99\times1{,}000{,}000=990{,}000.$$
- Two-box: $\mathtt{do}(F=\text{twobox})$ gives $P(\textit{full})=0.01$, so
  $$\mathbb E(V)=0.01\times1{,}001{,}000+0.99\times1{,}000=11{,}000.$$

A-FDT one-boxes. These are the source's figures. (The source's EDT paragraph quotes \$999,000 for one-boxing; the same arithmetic gives \$990,000.)

The source anticipates an objection: Fiona is nearly sure she one-boxes, so why not grab the extra \$1,000? Her hypothetical for two-boxing is one in which *the function itself* outputs two-box. In that world the predictor's model of the function outputs two-box too. Nothing in her reasoning appeals to retrocausation.

### 5.3 Smoking lesion

The lesion fixes the agent's preferences. Utility $\mathcal U_S$ (likes smoking) gives smoking +\$1,000; utility $\mathcal U_R$ does not. The paper therefore builds two logical nodes:

- $F_S=\textsc{fdt}(\underline{P_S},\underline G)$ and $F_R=\textsc{fdt}(\underline{P_R},\underline G)$;
- $\textsc{Act}=F_S$ if lesion, and $\textsc{Act}=F_R$ otherwise.

Cancer depends on the lesion and on no $F$ node. Let $p=P(\text{lesion})$ and let $q=P(F_R=\text{smoke})$. Intervening on $F_S$ leaves $p$ unchanged. The two hypotheticals then differ by exactly $p\times\$1{,}000$ in favour of smoking. A-FDT smokes, "using one simple rule that has no need for ratification." Contrast Newcomb: there, $F\to\textsc{Prediction}$ is an edge; here, $F\to\textsc{Cancer}$ is not. Which edges $G$ contains is the whole difference between the two cases.

### 5.4 Transparent Newcomb and Parfit's hitchhiker

Box B is visible. The predictor fills it iff it predicts one-boxing *upon seeing it full*. The graph has nodes $F_{\text{full}}$ and $F_{\text{empty}}$. $F_{\text{full}}$ feeds $\textsc{Prediction}$, and $\textsc{Prediction}$ (through the box) determines which of the two nodes controls $\textsc{Act}$. Let $q=P(F_{\text{empty}}=\text{twobox})$; the source notes the correct value is 1.

Fiona sees a full box and evaluates $\mathtt{do}(F_{\text{full}}=a)$:

- One-box:
  $$0.99\times1{,}000{,}000 + 0.01\times q\times1{,}000 = 990{,}000+10q.$$
- Two-box:
  $$0.01\times1{,}001{,}000+0.99\times q\times1{,}000 = 10{,}010+990q.$$

The source prints the second figure as "\$110,00 + q·\$990"; the expression I give is the correct evaluation. A-FDT one-boxes while *looking at* \$1,000,000. Its two-box hypothetical is mostly a world in which it would have seen an empty box. The source argues that this is structurally identical to paying the driver in Parfit's hitchhiker problem. It defends the verdict on three grounds: precommitment (A-FDT acts as CDT and EDT agents would pay to be bound to act), the value of information (A-FDT never pays to be blindfolded), and utility (predictors show full boxes to A-FDT agents).

### 5.5 XOR blackmail

A letter arrives iff exactly one of these holds: (i) there are no termites and the agent will pay \$1,000, or (ii) there are termites and the agent will not pay. The graph has $\textsc{Infestation}\to\textsc{Predictor}\leftarrow F_{\text{letter}}$. Let $t=P(\text{termites})$.

- Pay: $\mathtt{do}(F_{\text{letter}}=\text{pay})$. The agent sees the letter exactly when there are no termites. Expected loss:
  $$t\times10^6+(1-t)\times10^3.$$
- Refuse: the letter comes exactly when there are termites. Expected loss:
  $$t\times10^6.$$

A-FDT refuses, because $F$ has no edge into $\textsc{Infestation}$. EDT pays: conditioning on paying "removes" the termites. CDT also refuses, but for a different reason. The source stresses that the agents' *hypotheticals* differ. Asked what would have happened had she paid, the A-FDT agent says she would never have received the letter. The CDT agent describes a world in which an infallible predictor erred.

### 5.6 Mechanical blackmail, with a threshold

The blackmailer runs the damaging program iff she predicts payment. Let $\varepsilon$ be the probability that she wrongly predicts payment from an agent disposed to refuse.

- $\mathtt{do}(F_{\text{bm}}=\text{pay})$: the agent is always blackmailed. Loss: \$1,000.
- $\mathtt{do}(F_{\text{bm}}=\text{refuse})$: the agent is blackmailed with probability $\varepsilon$ and then loses \$1,000,000. Expected loss: $\varepsilon\times10^6$.

A-FDT refuses iff $\varepsilon<10^{-3}$. The source's example of $\varepsilon=0.0009$ (refuse, expected loss \$900) fits this threshold. Its second example says Fiona pays at "0.011%". By the computation above, paying requires $\varepsilon>0.1\%$, so the intended figure was presumably 0.11%. The example shows that A-FDT is not a blanket "never pay" rule. It weighs how sensitive the predictor is against the stakes.

### 5.7 Death in Damascus

Death's appointment book is an arrow $F\to\textsc{DeathLocation}$. Under either intervention Death is wherever the agent is. Survival is therefore impossible in both hypotheticals, and the only difference is the \$1,000 travel cost. A-FDT stays in Damascus, decisively and without instability. CDT, by contrast, cycles: whichever destination it expects to choose, it then prefers the other. The source adds that CDT will also decline a truly random coin offered for \$1, because its hypotheticals already credit it with at least a 50% chance of survival.

## 6. When A-FDT agrees with the other theories

The source states that the theories coincide when every correlation between $\textsc{Act}$ and another variable is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node:

$$\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)].$$

So A-FDT is conservative. It departs from CDT only where the world contains copies, simulations, or predictions of the agent's function.

A corresponding dominance principle follows. The source defines it this way: $a$ dominates $b$ if, "holding constant all relevant subjunctive dependencies," switching the algorithm's output from $b$ to $a$ is sometimes better and never worse. Its broader point is that "every method for constructing hypotheticals gives rise to its own notion of dominance." The causal dominance argument for two-boxing therefore restates CDT's assumptions; it is not a neutral argument against A-FDT.

## 7. What the source leaves open

### 7.1 Priors on non-intervened $\textsc{fdt}$ nodes

In the lesion case and the transparent Newcomb case, the answer involves $q$, the prior on how the agent would act on *another* input. The source shows that for these cases the verdict holds for every $q$. That cannot be true in general. A problem could be built in which the best output on input $x$ depends on what the same function does on input $y$.

**[My proposal]** Treat the $F_j$ priors as an equilibrium condition. Put probability 1 on the value that A-FDT itself returns on input $j$, and iterate until the assignment is self-consistent. When the iteration converges, the result is a profile of actions in which each action is a best response given the others. That is coordinate-wise optimality, which is weaker than optimality of the whole profile.

### 7.2 Action-level versus policy-level optimization

The gap in 7.1 is precisely what the authors' preferred policy formulation closes. A-FDT intervenes on one input-indexed node at a time. The policy version instead chooses the whole map $\pi:\mathcal X\to\mathcal A$ at once and maximizes $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}=\pi))$.

The two can come apart **[my analysis]** whenever several input-nodes jointly feed one predictor. Suppose a reward requires a predicted pattern across two inputs. A-FDT, holding the other node fixed at a bad equilibrium value, may find no profitable single deviation. The policy version would switch both outputs together. The source says this difference "makes a difference in certain multi-agent dilemmas" but none of its examples depend on it. Anyone applying A-FDT should check whether some predictor reads the agent's behaviour on several inputs at once. If so, the A-FDT verdict may be a non-optimal equilibrium.

### 7.3 Building $G$

Deciding whether a process "computes the same function" is a judgement of degree. A predictor with 99% accuracy is modelled as an arrow plus noise. A lesion gets no arrow. The paper gives no criterion for intermediate cases, such as a crude heuristic model of the agent, or a different agent whose function is similar but not identical (for instance, a near-twin in a prisoner's dilemma).

**[My proposal]** Add an edge $F\to Z$ when, by the agent's own lights, $Z$'s value would be computed differently were the algorithm's output different. Use the noise node to encode the agent's credence that $Z$ actually tracks that output. In practice, this means asking whether the predictor's accuracy *comes from* modelling the agent's reasoning, or is a base-rate regularity that would survive a change in that reasoning. This rule respects the source's predictor/lesion asymmetry, but it is a heuristic, not a theorem.

### 7.4 Fairness

The source claims that A-FDT is optimal on "fair problems," meaning those in which outcomes depend only on the agent's behaviour, not on its decision procedure. It concedes that no formal definition of fairness exists yet. Its own footnote 15 gives a hard case: a game that punishes anyone who acts like a copy of Fiona.

## 8. Conclusion

A-FDT is CDT's machinery applied to a different variable. Equation (4) performs a Pearl intervention on a node standing for "the output of this algorithm on this model and this observation." Observations select which node to intervene on; they are not conditioned on. Everything that subjunctively depends on that output, whether twins, predictors, or Death's ledger, moves with the intervention. Merely correlated factors, such as lesions, stay fixed.

Applied with the recipe in Section 4, A-FDT cooperates with twins, one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays the driver, one-boxes in transparent Newcomb, refuses both kinds of blackmail (subject to a computable accuracy threshold), and stays in Damascus. Its open parts are equally clear. The dependency graph $G$ must be supplied from outside the theory. Priors on counterfactual inputs need a principled treatment, such as the self-consistency rule proposed above. And the action-level formulation can fall short of the policy-level formulation the authors prefer when a predictor responds to the agent's behaviour across several inputs.

**Reference.** E. Yudkowsky and N. Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.