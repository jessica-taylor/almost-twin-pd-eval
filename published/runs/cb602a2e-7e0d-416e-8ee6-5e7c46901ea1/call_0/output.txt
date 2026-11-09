# A-FDT: Action Functional Decision Theory

## Choosing as a function rather than as a body

Decision theory has long been organized around one question: when an agent considers taking an action, what should she imagine would follow? Evidential decision theory (EDT) says she should imagine the world *conditional on* learning she took it. Causal decision theory (CDT) says she should imagine the world *as if her physical act were surgically set*, with only its causal consequences changing.

Yudkowsky and Soares's paper "Functional Decision Theory: A New Theory of Instrumental Rationality" proposes a third answer. The agent should treat her decision as "the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

This essay explains one precise version of that proposal. I call it **A-FDT (action functional decision theory)**. It is the rule given as Equation (4) in Section 5 of the paper:

$$
\mathrm{FDT}(P,G,x) \;:=\; \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\!\left(V \,\middle|\, \mathtt{do}\!\left(\textsc{fdt}(\underline P,\underline G,\underline x)=a\right)\right). \tag{4}
$$

The paper calls this simply "FDT." I use the name A-FDT because the paper says in footnotes 7 and 16 that the authors' "preferred formalization" iterates over *policies* rather than actions. The rule in Equation (4) is the action-level version. When I discuss the policy-level variant, I call it **policy FDT** to keep the two apart.

Throughout, I mark which claims come from the paper and which are my own interpretations or additions.

## 1. The common skeleton

The paper presents EDT, CDT and A-FDT as expected-utility theories that share a single form (its Equation 1):

$$
\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).
$$

Here $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective. Following Joyce, the paper treats the theories as "disagreeing about the epistemic perspective from which actions are to be evaluated." That is, they disagree about how to interpret $\hookrightarrow$.

Operationally, the agent holds a world-model $M$. For each action $a$, she builds a "hypothetical" from $M$ and scores it by expected utility. The paper describes hypotheticals as "decision-theoretic instruments constructed from beliefs," not beliefs in their own right. The three theories differ in how they build these hypotheticals:

- **EDT:** $\operatorname{argmax}_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a)$. The agent conditions on her act.
- **CDT:** $\operatorname{argmax}_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x)$. The agent intervenes on the physical-act node of a causal graph and conditions on what she has observed.
- **A-FDT:** Equation (4). The agent intervenes on a *logical* node and does **not** condition on the observation.

## 2. The ingredients of Equation (4)

**The model $(P,G)$.** $P$ is a probability distribution over variables. Some of these represent physical facts, such as box contents, termites and payouts. Others represent *outputs of mathematical functions*. $G$ is a graph saying how changing each variable would change the others. For CDT, $G$ encodes causal structure only. For A-FDT, the paper says $G$ must carry information about "the logical, mathematical, computational, causal, etc. structure of the world more broadly."

**The logical nodes.** $\textsc{fdt}(\underline P,\underline G,\underline x')$ is a variable whose value is the output of the A-FDT algorithm when it is run on the inputs $(P,G,x')$. The underlines denote dequoting: the node's *name* is built from the model itself. The paper argues this self-reference is harmless. The agent needs a variable that *represents* her own output, not knowledge of that output's value, and Kleene's recursion theorem shows such self-representing structures can be built.

There is generally one such node for each observation history $x'$ that the agent could have received.

**The intervention.** $\mathtt{do}(\textsc{fdt}(\ldots,x)=a)$ is Pearl's operator applied to the logical node. It sets that node to $a$ and propagates the change along $G$'s arrows to everything downstream. Upstream and unrelated variables keep their prior distribution.

**Subjunctive dependence.** The arrows out of the logical node represent what the paper calls *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The paper treats causal dependence as a special case. It also insists that merely statistical correlation is not subjunctive dependence. Its example is two calculators that happen to be pink: they share a colour but do not depend on each other.

The slogan the paper offers is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

Comparing Equation (4) with CDT's Equation (3), the paper identifies two differences:

1. **Where the surgery happens.** CDT intervenes on the token (the physical act). A-FDT intervenes on the type (the function's output). Anything else that computes or accurately models that function moves along with the act. This includes twins, predictors and simulations.
2. **How observations enter.** CDT responds to $x$ by conditioning on it. A-FDT responds to $x$ "by changing which node it intervenes upon." It moves from $\textsc{fdt}(\ldots,x)$ to $\textsc{fdt}(\ldots,y)$ when its observation changes from $x$ to $y$.

The second difference is easy to overlook, and it does a great deal of work.

## 3. A recipe for applying A-FDT

The paper does not give a step-by-step procedure. The following recipe is my reconstruction from its worked examples.

1. **List the variables.** Identify exogenous variables (for example a predictor's accuracy, or termites), observations, the physical act, outcomes, and $V=\mathcal U(\textsc{Outcome})$.
2. **Add logical nodes.** Create one node $\textsc{fdt}(\underline P,\underline G,\underline{x'})$ for each relevant observation history $x'$.
3. **Wire subjunctive dependencies.**
   - $\textsc{Act}$ is a child of every logical node, together with a selector. The selector is whatever determines which observation the agent actually receives, and therefore which logical node controls her body.
   - Any predictor, twin or simulator that models the agent's algorithm on input $x'$ is a child of $\textsc{fdt}(\ldots,x')$.
   - Lesions, genes, and other merely statistical correlates are *not* children of any logical node.
4. **Assign probabilities.** Give priors to the exogenous variables. Give priors to the *non-intervened* logical nodes (what the agent would do on other inputs). The paper usually calls the relevant one $q$.
5. **Intervene and score.** For each $a\in\mathcal A$, compute $\mathbb E[V\mid\mathtt{do}(\textsc{fdt}(\ldots,x)=a)]$ by propagating through $G$. Do not condition on $\textsc{Obs}=x$.
6. **Choose.** Output the argmax.

The worked examples below follow this recipe.

## 4. Worked examples

### Twin prisoner's dilemma

Both twins' acts are children of a single logical node, because each twin runs the same function.

- $\mathtt{do}(\textsc{fdt}=\textit{cooperate})$ leads to both cooperating, with $V=\$1{,}000{,}000$.
- $\mathtt{do}(\textsc{fdt}=\textit{defect})$ leads to both defecting, with $V=\$1{,}000$.

A-FDT cooperates. CDT holds the twin's act fixed under its intervention, so defection dominates and CDT defects.

### Newcomb's problem

The predictor is 99% accurate. Fiona's graph (the paper's figure for her) makes both $\textsc{Act}$ and $\textsc{Prediction}$ children of $\textsc{fdt}(\underline P,\underline G)$. Box B is full if and only if the prediction is "one-box."

$$
\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\textit{onebox})]=0.99(10^6)+0.01(0)=\$990{,}000,
$$
$$
\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\textit{twobox})]=0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000.
$$

A-FDT one-boxes.

The paper stresses that this involves no backward causation. Fiona "does not think that a physical signal passes between her action and the predictor's prediction." She only thinks it foolish to imagine her act changing without imagining the computation it implements changing as well.

A minor note: the paper reports \$999,000 for EDT's one-box value in the same problem. Since the probabilities are identical, that figure appears to be a typo for \$990,000.

### Smoking lesion

This case shows that A-FDT does not simply follow correlations. The lesion causes both cancer and a taste for smoking. The paper models the taste as a difference in utility functions, $\mathcal U_S$ (likes smoking) versus $\mathcal U_R$ (values smoking at $-\$1$). This gives two possible decision functions, $\textsc{fdt}(\underline{P_S},\ldots)$ and $\textsc{fdt}(\underline{P_R},\ldots)$. The lesion selects which one drives $\textsc{Act}$.

Crucially, $\textsc{Cancer}$ is *not* a child of either logical node. So intervening on $\textsc{fdt}(\underline{P_S},\ldots)$ leaves $P(\textit{lesion})=p$ unchanged. The paper computes that smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes.

The same rule therefore one-boxes in Newcomb's problem and smokes in the smoking lesion problem. Gibbard and Harper had argued this combination was unavailable to any consistent rule. The difference lies entirely in $G$: a predictor *models the function*, while a lesion does not.

### Transparent Newcomb (the role of not conditioning)

Both boxes are visible. Box B was filled if and only if the predictor predicted one-boxing *upon seeing it full*. Fiona sees it full, so she intervenes on $\textsc{fdt}(\ldots,\textit{full})$.

This node feeds both the prediction and, when the box is in fact full, the act. Let $q$ be her prior that $\textsc{fdt}(\ldots,\textit{empty})=\textit{twobox}$. Then:

$$
\mathrm{EU}(\textit{onebox})=0.99(10^6)+0.01\,q(1{,}000)=\$990{,}000+10q,
$$
$$
\mathrm{EU}(\textit{twobox})=0.01(1{,}001{,}000)+0.99\,q(1{,}000)=\$10{,}010+990q.
$$

(The paper prints the second value as "\$110,00 + q·\$990." The correct constant is \$10,010.)

A-FDT one-boxes for every $q\in[0,1]$, even though it can see \$1,000,000 sitting in the box.

These numbers are only obtainable *without* conditioning on $\textsc{Obs}=\textit{full}$. The calculation includes the branch in which the predictor erred and the box is empty. Here the paper's text is slightly inconsistent. It writes the maximand as $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full})$, with the observation inside an unbalanced bracket. Yet its arithmetic and Equation (4) both omit the conditioning.

**My interpretation:** A-FDT does not condition on the current observation. The observation's only role is to pick out which node is intervened on. This matches the paper's statement that A-FDT "entertain[s] the hypothesis that, if their action were different, they might have *made different observations*." It also matches its remark that conditioning *and* switching nodes (Timeless Decision Theory) produces a harmful "double update."

The paper notes that one-boxing here is structurally identical to paying the driver in Parfit's hitchhiker problem. It defends one-boxing with three arguments:

- **Precommitment.** CDT and EDT agents would both precommit to it.
- **Value of information.** A-FDT never assigns negative value to information.
- **Utility.** Agents who behave this way actually see full boxes.

### XOR blackmail

A predictor sends a letter if and only if exactly one of two things holds: (i) there are no termites and the agent would pay \$1,000; (ii) there are termites and the agent would not pay. Let $p=P(\textit{termites})$, with termite damage of \$1M.

Intervening on $\textsc{fdt}(\ldots,\textit{letter})$:

- **Pay.** With termites, no letter is sent and the agent loses \$1M. Without termites, the letter comes and she pays. So $\mathrm{EU}=-p\cdot10^6-(1-p)\cdot10^3$.
- **Refuse.** With termites, the letter comes and she loses \$1M. Without termites, nothing happens. So $\mathrm{EU}=-p\cdot10^6$.

A-FDT refuses, by a margin of $(1-p)\cdot\$1{,}000$. EDT pays, because conditioning on paying sends $P(\textit{termites}\mid\textit{letter})$ to 0.

The paper notes that CDT also refuses, but with a revealing hypothetical. CDT's counterfactual "pay" world is one in which an inerrant predictor erred. A-FDT's counterfactual "pay" world is one in which the letter was never sent.

### Mechanical blackmail

A blackmailer runs a damaging program only if she predicts the agent would pay \$1,000 to stop it. Releasing the material costs \$1M.

- $\mathtt{do}(\textsc{fdt}(\ldots,\textit{blackmail})=\textit{pay})$: the agent is blackmailed and pays, so $\mathrm{EU}=-\$1{,}000$.
- $\mathtt{do}(\ldots=\textit{refuse})$: the agent is not blackmailed, so $\mathrm{EU}=0$.

A-FDT refuses, while holding the letter. If the predictor wrongly expects payment with probability $\varepsilon$, refusing costs $\varepsilon\cdot10^6$ in expectation. A-FDT therefore refuses if and only if $\varepsilon<0.001$.

The paper's illustrative numbers are an error rate of 0.0009 (refuse, expected loss \$900) and "0.011%" (pay). By this arithmetic, 0.011% would still yield refusal, with an expected loss of only \$110. The second figure is presumably meant to be 0.11%.

### Death in Damascus

Death perfectly predicts the agent, so Death's location is a child of the logical node.

- Staying yields death, with $V=0$.
- Fleeing yields death in Aleppo, with $V=-\$1{,}000$.

A-FDT stays, stably.

CDT holds Death's location fixed while varying the act. This produces Gibbard and Harper's instability. The paper argues it can also lead CDT to decline a truly random coin offering a 50% chance of survival for \$1.

## 5. When A-FDT agrees with CDT and EDT

The paper states a clean coincidence condition. Suppose that in $(P,G)$ every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from its dependence on the agent's own logical node. Then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)],
$$

and all three theories prescribe the same action. They diverge only when something other than the act's own effects tracks the act. In practice that means predictors, copies, and other replicators of the agent's reasoning.

## 6. Dominance, fairness, and control

**Dominance.** The paper argues that "every method for constructing hypotheticals gives rise to its own notion of dominance." Two-boxing dominates only under CDT's counterfactuals. Under A-FDT's counterfactuals, which hold the predictor–agent dependency fixed, one-boxing dominates. Dominance is therefore not a neutral tiebreaker, and the paper prefers to judge theories by the utility they achieve.

**Fairness.** No theory wins every problem: a mind reader can simply reward CDT agents for being CDT agents. The paper's claim is narrower. It holds that A-FDT does at least as well as its rivals on "fair problems," where "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." The authors concede, in a footnote, that formalizing fairness is still open.

**Control.** The objection is that an A-FDT agent pretends to control a mathematical fact. The paper replies with a parity argument. A deterministic CDT agent likewise "controls" an act that could not have been otherwise. Both theories use counterfactuals with impossible antecedents as tools, so the objection does not favour CDT.

## 7. What Equation (4) leaves undetermined

### (a) Where does $G$ come from?

This is the open problem the paper itself identifies:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

Equation (4) is a function of $G$, so every verdict above is conditional on a correct dependency graph.

Some guidance can be read off the paper's examples. The examples suggest a variable should be a child of $\textsc{fdt}(\ldots,x')$ when it is produced by a process that *computes or reliably models* the agent's algorithm on input $x'$. A predictor's accuracy parameter should then measure how faithfully it does so. **This is my proposed heuristic, not the paper's definition.**

Hard cases remain. Examples include a partial similarity between two agents, such as an agent running a slightly different algorithm, or a predictor that uses only crude behavioural statistics. How such cases should be treated is not settled by the source.

### (b) Counterpossibles

The ideal operator would be $\mathtt{true}(\phi)$, which updates on the truth of a logical sentence. The paper admits "it's not clear how to define a $\mathtt{true}$ operator." It sidesteps the issue by supplying $G$ and reusing $\mathtt{do}$.

Footnote 9 mentions a possible conditional, "evidential," variant of FDT. That variant would need conditional probabilities on false logical sentences, which no one yet knows how to define.

### (c) Priors on the non-intervened logical nodes

Every multi-observation example contains a free parameter $q$. This is the agent's credence about what her algorithm does on inputs she did not receive. The paper says the "correct" value can be verified (for example, $q=1$ in transparent Newcomb) but that it "doesn't matter" in its examples.

In general it can matter. **My proposal** is to require self-consistency: $q$ should place its mass on the outputs A-FDT itself returns for those inputs. This makes the profile of outputs a fixed point. That leads directly to the next point.

### (d) Actions versus policies

Equation (4) varies one node at a time and holds the others at their priors. **Policy FDT**, described only in the paper's footnotes, instead chooses an entire mapping $\pi:\mathcal X\to\mathcal A$:

$$
\pi^*=\operatorname*{argmax}_{\pi}\mathbb E\big[V\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big],\qquad \text{act } \pi^*(x).
$$

The paper says the two "will not make a difference in this paper" but do differ "in certain multi-agent dilemmas." The following example is my own illustration of how they can differ.

> **Copy coordination.** Two copies of the agent are shown different observations, *red* and *blue*.
> - Each copy picks $L$ or $R$.
> - The payoff is 2 if both pick $L$, 1 if both pick $R$, and 0 otherwise.
>
> **What A-FDT does.** On *red*, A-FDT intervenes only on $\textsc{fdt}(\ldots,\textit{red})$ and treats the *blue* node as fixed by its prior. Suppose that prior assigns credence $r$ to the blue copy playing $R$. Then $L$ scores $2(1-r)$ and $R$ scores $r$, so A-FDT picks $R$ whenever $r>2/3$.
>
> If the blue copy reasons symmetrically, the profile $(R,R)$ is self-consistent. Each copy's prior that the other plays $R$ turns out to be correct. So A-FDT, even with the self-consistency requirement from (c), can settle on the inferior payoff of 1.
>
> **What policy FDT does.** It varies both outputs jointly and selects $(L,L)$, with payoff 2.

The general point is this. Single-node intervention handles dependencies *on the current input* perfectly well, but it cannot by itself coordinate the agent's behaviour across different inputs. Policy optimization can. Readers applying Equation (4) should check whether the problem's outcome depends on how the agent behaves *on several inputs at once*. If it does, the action-level verdict may depend on the priors chosen in (c).

### (e) Tractability

Like Equations (2) and (3), Equation (4) maximizes over all actions in a full world-model, which is idealized. The paper expects bounded approximations of each theory to keep the same relative strengths, but offers this as an expectation rather than a result.

## 8. Summary of the formal content

| | Hypothetical for $a$ | Response to observation $x$ |
|---|---|---|
| EDT | $P(\cdot\mid \textsc{Act}=a, x)$ | condition on $x$ |
| CDT | $P(\cdot\mid\mathtt{do}(\textsc{Act}=a), x)$ | condition on $x$ |
| A-FDT | $P(\cdot\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a))$ | intervene on the node indexed by $x$ |

A-FDT keeps every correlation that runs through a shared computation, including those through twins, predictors and simulations. It cuts every correlation that is merely statistical, such as those running through lesions or cosmic rays. In the paper's words, EDT's hypotheticals "respect too many correlations," CDT's "too few."

## Conclusion

A-FDT, as given by Equation (4), is a CDT-shaped expected-utility rule with two changes:

1. The agent intervenes on the *output of her decision function* rather than on her physical act.
2. Observations select *which* function-output node she intervenes on, instead of being conditioned on.

Given an accurate graph of subjunctive dependencies, the rule delivers a consistent set of verdicts. It cooperates with twins, one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays in Parfit's hitchhiker, one-boxes in transparent Newcomb, refuses both kinds of blackmail, and stays in Damascus. It reaches all of these without ratification or precommitment.

Its unresolved parts are clearly located:

- how to construct the dependency graph $G$, or, equivalently, a theory of counterpossibles;
- how to set priors over the agent's outputs on inputs she did not receive;
- when action-level choice must give way to policy-level choice.

With those caveats, a reader can apply A-FDT to an unfamiliar case by asking: which things in this world compute or model my function on this input, and what would they do if its output were different?

---

**References**

- Yudkowsky, E. & Soares, N. "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060 (primary source).
- Gibbard, A. & Harper, W. (1978) "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999) *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000) *Causality*.