# Action Functional Decision Theory (A-FDT): Choosing the Output of a Function

## 1. Orientation

Yudkowsky and Soares's paper *Functional Decision Theory* proposes that a rational agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper's central formal statement is Equation (4) in Section 5. There the agent chooses an **action** by intervening on a node of her world-model that represents the output of her own decision procedure on her actual inputs.

I call this action-valued formulation **A-FDT** (action functional decision theory). The label matters because the authors say, in footnotes 7 and 16, that their "preferred formalization" iterates over *policies*, which are mappings from observations to actions. I will call that variant *policy-selection FDT* when it comes up. Both are distinct from **CDT** (causal decision theory) and **EDT** (evidential decision theory), which the paper uses as foils.

The essay has four parts. I first state Equation (4) and its ingredients. I then explain how A-FDT treats dependence and counterfactuals, and work through the paper's examples, recomputing the numbers. Finally, I separate what the source settles from what a user must supply, and propose operational conventions where the source leaves gaps. Claims attributed to the paper are marked as such. Recipes, conventions, and the coordination example in §6 are my own.

## 2. The formal definition

All three theories share one template. Expected utility is

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $\hookrightarrow$ is the connective for "decision hypotheticals." Following Joyce, the paper treats the interpretation of $\hookrightarrow$ as the free parameter that distinguishes the theories. Each theory says how to turn a world-model into a *hypothetical* for each action. The paper describes a hypothetical as a transient computational object, "like … notes on scratch paper," not a metaphysical possible world.

- **EDT** conditions: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT** (Equation 3) intervenes on the physical act: $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$.
- **A-FDT** (Equation 4, written "FDT" in the source) is

$$\boxed{\;\text{A-FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\; \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}$$

The ingredients are as follows.

- $P$ is a probability distribution over the variables of the agent's model. The model includes variables for the *outputs of mathematical functions*, and in particular for the output of A-FDT itself on various inputs.
- $G$ is a directed graph that says how changing a variable, including a logical one, propagates to other variables. For CDT, $G$ encodes causal structure. For A-FDT it must encode what the paper calls *subjunctive dependence*.
- $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a node of the model. The underlines denote dequoting: the node *represents* the value of A-FDT run on exactly these inputs. The authors note that this self-reference is harmless. An agent can have a variable representing a value without knowing the value, and Kleene's recursion theorem ("quining") lets a data structure contain a representation of itself.
- $\mathtt{do}$ is Pearl's intervention. It sets the node to $a$, cuts the node off from its parents, recomputes everything downstream according to $G$, and leaves everything else at its prior distribution.
- $V = \mathcal U(\textsc{Outcome})$ is the utility node.

The paper identifies exactly two differences from CDT. First, the **point of intervention** is a logical node (the output of the agent's decision function) rather than the physical act. Second, **observations are handled differently**: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Equation (4) contains no conditioning bar on $\textsc{Obs}=x$. The observation enters only through the *name* of the node being set.

In short, A-FDT is CDT with the "type" in place of the "token." In Peirce's terms, which the paper borrows, the agent intervenes on the type ("what this function outputs on this input") rather than on the token ("what my body does now").

## 3. Subjunctive dependence: what goes in $G$

Everything that distinguishes A-FDT from CDT lives in $G$. The paper's guiding slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**Positive cases.** Two well-functioning calculators computing $6288+1048$, in Paris and Tokyo, both depend on the arithmetical fact. Neither causes the other, yet if the sum "were" different, both displays would differ. The paper extends this to agents. A psychological twin runs the same decision function. A reliable predictor contains a model of it ("a 'twin' inside the predictor's mind"). In $G$, arrows therefore run from $\textsc{fdt}(\cdot)$ to the agent's own $\textsc{Act}$, to the twin's act, and to the predictor's $\textsc{Prediction}$.

**Causal dependence is a special case.** A scribe copying the Paris calculator's output depends on it both causally and subjunctively. So anything downstream of the act in the causal graph remains downstream in $G$.

**Negative cases.** Mere statistical correlation does not create an arrow. If the Paris and Tokyo calculators are both pink by coincidence, repainting one leaves the other pink. Likewise, the carcinogenic lesion "is not evaluating the agent's future decisions," so cancer is not a child of the decision node.

**Counterpossibles.** Since a function's output on a given input is logically fixed, $\mathtt{do}(\textsc{fdt}(\ldots)=a)$ for the non-actual $a$ is counter-to-logic. The paper says an ideal $\mathtt{true}(\phi)$ operator for updating on logical sentences is "not clear how to define." Its response is to require that the dependency structure be *given* as input, "in the same way that the relevant causal structure is given as an input to CDT." This is the paper's main admitted gap: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem."

## 4. Worked examples

All dollar figures are utilities. I follow the paper's models and recompute the arithmetic.

### 4.1 Newcomb's problem (99%-accurate predictor)

The graph has $\textsc{fdt}(\underline P,\underline G) \to \textsc{Act}$ and $\textsc{fdt}(\underline P,\underline G) \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $P(\textit{accurate})=0.99$. $\textsc{Prediction}$ determines Box B, and Box B together with $\textsc{Act}$ determines $V$.

$$\begin{aligned}
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{onebox})] &= 0.99(10^6)+0.01(0)=990{,}000,\\
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\end{aligned}$$

A-FDT one-boxes. (The source gives EDT's one-boxing value as \$999,000. By the same arithmetic it should be \$990,000. The verdict is unaffected.)

CDT intervenes on $\textsc{Act}$, which has no path to Box B. The full-box probability $p$ is therefore the same under both interventions, two-boxing wins by \$1,000 for every $p$, and CDT two-boxes.

The agent need not believe in retrocausation. In the paper's words, she "just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F, G^F)$ taking on a different value."

### 4.2 Twin prisoner's dilemma

One node, $\textsc{fdt}$, feeds both prisoners' acts. Setting it to *cooperate* yields \$1,000,000 and setting it to *defect* yields \$1,000, so A-FDT cooperates. Ten-voter coordination problems and "coordinating with one's future self" about gym visits work the same way in the paper. Each is modeled by letting relevantly identical decisions share a node.

### 4.3 Smoking lesion

This case requires more structure, and the paper supplies it. The lesion determines *preferences*, so there are two candidate world-models: $P_S$ (likes smoking) and $P_R$ (values smoking at −\$1). There are correspondingly two decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. $\textsc{Act}$ equals the first if the agent has the lesion and the second otherwise. Cancer depends only on the lesion and luck.

Let $p=P(\textit{lesion})$ and $q=P(\textsc{fdt}(\underline{P_R},\underline G)=\textit{smoke})$. Intervening on the $P_S$-node leaves $p$ unchanged:

$$\begin{aligned}
\text{smoke: }& p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q),\\
\text{refrain: }& p(10{,}000)+(1-p)(990{,}000+1{,}000q).
\end{aligned}$$

Smoking wins by $p\cdot\$1{,}000$ for every $q$. A-FDT therefore one-boxes and smokes, which was the combination Gibbard and Harper argued no single principle could deliver.

The paper itself regards this dilemma as "badly confused," because the agent must be uncertain about her own desires. It keeps the example mainly for historical reasons.

### 4.4 Transparent Newcomb and Parfit's hitchhiker

Both boxes are visible, and the predictor fills B iff she predicts one-boxing *upon seeing two full boxes*. The graph now contains two decision nodes, $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. The prediction depends on the *full*-node. The prediction also fixes which node controls $\textsc{Act}$, because it fixes what the agent sees.

Having seen *full*, the agent intervenes on the *full*-node and does **not** condition on the box being full. Let $q$ be the prior probability that the *empty*-node outputs *twobox*.

$$\begin{aligned}
\textit{onebox}:&\ 0.99(10^6)+0.01\,q(1{,}000)=990{,}000+10q,\\
\textit{twobox}:&\ 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.
\end{aligned}$$

(The source prints the second line as "$110,00 + q·$990"; the constant should be \$10,010.) One-boxing wins for all $q\in[0,1]$.

When the agent imagines two-boxing, she imagines a world in which she would most likely have *seen an empty box*. Parfit's hitchhiker has the same structure: paying in the city corresponds to one-boxing. CDT and EDT both two-box here and refuse to pay. Predicted to do so, they see empty boxes and are left in the desert.

### 4.5 Blackmail

**XOR blackmail.** The letter arrives iff exactly one of (termites, will-not-pay) or (no termites, will-pay) holds. Intervening on $\textsc{fdt}(\ldots,\textit{letter})$ changes whether the letter is sent, but not whether there are termites. Paying therefore buys nothing, and A-FDT refuses. EDT pays, because conditioning on paying "sends her probability on termites to 0." CDT also refuses, but for a different reason. Its hypothetical has a supposedly infallible predictor erring, which the paper reads as a symptom of a deeper flaw.

**Mechanical blackmail.** The blackmailer runs a damaging program (cost \$1,000,000) only if she predicts the agent would pay \$1,000 to stop it. Let $\varepsilon$ be the probability that she wrongly predicts payment from a refuser. Holding the letter, the agent compares:

$$\text{pay}: \approx -1{,}000, \qquad \text{refuse}: -\varepsilon\cdot 10^6.$$

So A-FDT refuses iff $\varepsilon<10^{-3}$. The paper's case $\varepsilon=0.0009$ gives refusal, with an expected loss of \$900. (The paper's second figure, "0.011%," lies below this threshold even though the text says she then pays; 0.11% is presumably intended.) Since an accurate blackmailer can see that A-FDT agents refuse, she does not blackmail them.

## 5. The general shape of the verdicts

Two structural facts follow from Equation (4).

**Agreement in "simple" problems.** The paper notes that if every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node), then

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],$$

and EDT, CDT, and A-FDT all agree. Disagreement requires something besides the act's own effects that tracks the decision function: a predictor, a twin, or a copy.

**Acting as one would have precommitted.** Because the observation is not conditioned on, A-FDT evaluates the output as though from before the observation. Its expectations weigh the worlds in which the agent would have seen something else. This is why the paper claims that A-FDT agents act as they would have precommitted to act and never assign negative value to information.

The paper explains the name "Updateless Decision Theory" (an ancestor theory) the same way. It also warns that Timeless Decision Theory, which both conditions *and* moves the intervention point, commits a harmful "double update." For a user, the warning translates into a practical rule: **never both condition on $x$ and switch to the $x$-node.**

## 6. What the source leaves open, and how to operationalize it

### 6.1 The source of $G$

**Source.** $G$ is an input, and the paper offers no method for learning it.

**My convention.** Draw an arrow from $\textsc{fdt}(\underline P,\underline G,\underline y)$ to a variable $Z$ when $Z$ is produced by a process that evaluates, simulates, or reasons about that same function on input $y$ (or about a function whose output the agent knows to be equal to it). Model the reliability of the process with an exogenous noise node such as $\textsc{Accurate}$, independent of the decision node.

Mere common-cause correlation (lesions, demographics, mood) does not qualify. Neither do processes that respond to the agent's *procedure* rather than its *output*. The paper treats the latter as unfair problems (see §7), not as dependencies.

This convention reproduces every graph in the paper. It is still a heuristic. Partial similarity (an opponent running a *similar* but not identical algorithm) is not settled by the source. One natural extension adds a mixing variable: with probability $s$ the opponent's act copies the node, and otherwise it is independent. Whether that is the correct treatment is an open question.

### 6.2 Which node to intervene on

The node is indexed by the agent's full input $(P,G,x)$. A problem description must therefore specify, for each possible observation history $y$ the agent might face, a separate node $\textsc{fdt}(\ldots,y)$. It must also specify which of these nodes predictors consult, and which one governs $\textsc{Act}$ in which world. Omitting the *empty*-node in the transparent Newcomb problem, for example, would leave the twobox hypothetical undefined.

### 6.3 Priors on the nodes not intervened on

In the examples, the prior $q$ on the agent's *other* decision nodes "doesn't matter." That is a feature of those payoffs, not of A-FDT in general. Equation (4) sets one node and leaves the others at their priors, so the verdict can depend on what the agent believes about her own behavior at other inputs.

The following example is my own. A fair coin shows *red* or *green*, and the agent sees it. A perfect predictor pays 10 if the agent's outputs at red and green are both $A$, 5 if both are $B$, and 0 if they differ.

At red, A-FDT intervenes on the red-node, holding the green-node at its prior. With $r=P(\text{green-node}=A)$:

$$\text{choose }A: 10r, \qquad \text{choose }B: 5(1-r).$$

If the agent expects herself to play $B$ elsewhere ($r<1/3$), A-FDT picks $B$, and that expectation is self-confirming. The pair $(B,B)$ is then a stable but suboptimal fixed point. Policy-selection FDT, which optimizes the whole map $\{red,green\}\to\{A,B\}$ jointly, picks $(A,A)$.

This mirrors the paper's remark that action- and policy-based versions diverge in some cases. The paper says "The difference only matters in multi-agent dilemmas so far as we can tell." Whether my example counts as multi-agent is debatable, since the red-node and green-node behave like two coordinating players.

**My recommendation.** When applying A-FDT, (i) state the priors on all non-intervened decision nodes explicitly, (ii) check that the verdict is robust across them, and (iii) where it is not, report that the case lies in the territory where A-FDT and policy-selection FDT can come apart. A natural consistency requirement, which is my proposal and not the paper's, is that these priors match the outputs A-FDT itself would produce at those inputs. In the example this narrows the answer to the self-consistent fixed points $(A,A)$ and $(B,B)$ but does not decide between them.

### 6.4 Zero-probability actions, ties, and mixed acts

Unlike EDT, Equation (4) never conditions on the agent's act, so a prior of 0 on an action does not stop her from evaluating it. This is the paper's point about EDT's vulnerability to extreme priors, as in the "cosmic ray" problem.

The source says nothing about ties or randomization. I suggest breaking ties by any fixed rule. If randomization is available, model it as a separate variable, and state explicitly whether predictors can see it. In Death in Damascus, Death *can* predict the agent's pseudorandomness but not a truly random coin, and a correct $G$ must reflect that difference.

### 6.5 Imperfect self-implementation

$\textsc{Act}$ may depend on the decision node only noisily (trembling hands, cosmic rays). Equation (4) accommodates this by making $\textsc{Act}$ a stochastic function of its parents. Nothing in the theory changes.

## 7. Philosophical motivation

**Dominance is theory-relative.** CDT's dominance argument for two-boxing holds the prediction fixed while the act varies. The paper argues that this simply restates CDT's way of building counterfactuals. It is "akin to handing us a well-functioning calculator … and asking us to imagine it outputting 3159." Under A-FDT counterfactuals, which hold the subjunctive dependencies fixed, A-FDT never takes a dominated action. The authors conclude that dominance is not a neutral arbiter and that achieved utility is the better criterion.

**Diagnosis of the rivals.** In the paper's phrase, "EDT respects too many action-environment correlations, while CDT respects too few." EDT cannot break merely statistical correlations, which leaves it exploitable by XOR blackmailers. CDT breaks even the logically necessary correlation between its own decision function and accurate predictions of it. As a result it oscillates in Death in Damascus and, the paper argues, declines a \$1 truly random coin that would give it a 50% chance of survival.

**Fairness.** Any theory can be punished by a problem that targets its procedure. The paper proposes that problems are "fair" when "the outcome depends only on the agent's behavior in the dilemma at hand" and the agent's beliefs are accurate. Newcomb's predictor is fair in this sense: "she punishes two-boxers," not causal decision theorists. The authors report finding no intuitively fair dilemma in which their theory loses. They concede that "fairness" has not been formalized, and their footnote 15 shows why that is hard.

**"Control" of the past.** One objection is that A-FDT agents act as if they control mathematical facts or past predictions. The paper's reply is a parity argument. A deterministic CDT agent also "imagines" alternatives to the one act it will in fact take. Any principled objection to controlling the type therefore applies equally to controlling the token.

**Reflective stability.** CDT agents would pay to self-modify away from CDT before facing future Newcomb problems. The paper claims its theory is "reflectively stable in fair problems": an A-FDT agent holding a blackmail letter has no wish to become a CDT agent temporarily.

## 8. Conclusion

A-FDT is expected-utility maximization in which the hypothetical for action $a$ is built by Pearl-style surgery on a logical node, namely the output of the agent's own decision function on her actual input. The change is then propagated along a graph of subjunctive dependence that includes, but goes beyond, causal structure. Observations select which node to intervene on; they are not conditioned on.

These two moves are enough to produce the paper's distinctive verdicts. A-FDT one-boxes, smokes, cooperates with twins, pays in Parfit's desert, one-boxes facing two full transparent boxes, and refuses blackmail.

Applying A-FDT to a new case requires three things the source leaves to the user:

1. a dependency graph $G$, for which the paper provides only paradigms and no learning method;
2. a decision node for every relevant input;
3. explicit priors on the decision nodes not being intervened on.

The third requirement is where A-FDT can come apart from the policy-selection version the authors prefer, as the coordination example in §6.3 shows. With these supplied and the verdict checked for sensitivity, Equation (4) is a usable decision procedure. Its foundations, the logic of counterpossibles and a theory of fairness, remain open.

### References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060v2.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.