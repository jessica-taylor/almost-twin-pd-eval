# A-FDT: Intervening on the Output of Your Own Decision Function

## 1. The question A-FDT asks

Decision theorists agree that a rational agent should maximize expected utility. They disagree about which hypothetical worlds the expectation should be taken over. Evidential decision theory (EDT) asks which act would be the best news to learn about. Causal decision theory (CDT) asks which physical act would cause the best outcome. Yudkowsky and Soares's *Functional Decision Theory* (arXiv:1710.05060) proposes a third question. In their words, the agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

This essay explains the version of that theory given by Equation (4) of the paper's Section 5. I call it **A-FDT** (action functional decision theory) because the equation selects an *action* rather than a policy. The authors note in footnotes 7 and 16 that their "preferred formalization" selects a *policy*, meaning a map from observations to actions. I discuss that variant separately under the name **policy-FDT** to keep the two apart. The paper itself labels Equation (4) simply "FDT."

I separate three kinds of material throughout:

- what the paper states;
- what follows mathematically from Equation (4);
- operational choices that I propose where the paper is silent. These are flagged as **[proposal]**.

## 2. The common expected-utility frame

Following Gibbard and Harper, the paper writes expected utility as

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\hookrightarrow$ is the connective for "decision hypotheticals." The paper invokes Joyce's representation theorem: the expected-utility form is shared, and the theories differ only in how they interpret $\hookrightarrow$. Write $V = \mathcal U(\textsc{Outcome})$.

- **EDT** interprets the connective as conditioning: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$ (Eq. 2).
- **CDT** interprets it as Pearl intervention on the physical act: $\arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x)$ (Eq. 3).

**A-FDT** (Eq. 4) intervenes on a *logical* node:

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x) = a\big)\Big).
$$

The ingredients are as follows.

- **$P$** is a probability distribution over variables. These include ordinary physical variables (box contents, lesions, letters) and also variables standing for *outputs of mathematical functions*.
- **$G$** is a graph saying how changing a logical variable affects other variables. The paper calls this "information about the logical, mathematical, computational, causal, etc. structure of the world more broadly."
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is the variable whose value is the output of the A-FDT procedure itself, run on this very model and this very observation. The underlines mark dequoting: the variable's *name* is built from the inputs. The self-reference is defended by appeal to Kleene's recursion theorem (quining). The agent needs a variable *representing* her output, not knowledge of its value.

The paper names two structural differences from CDT:

1. A-FDT intervenes on its decision function's output rather than on the physical act.
2. A-FDT "responds to observation by changing which node it intervenes upon" rather than by conditioning.

Notice that $\textsc{Obs}=x$ does **not** appear to the right of the conditioning bar in Eq. (4). This is the formal source of A-FDT's most striking verdicts, discussed in §5.

### Why a $do$ and not a "true" operator

The paper first writes an idealized rule, $\mathrm{FDT}^* = \arg\max_a \mathbb E(V \mid \texttt{true}(\textsc{fdt}(\underline P,\underline x)=a))$. Here $\texttt{true}(\phi)$ would update $P$ to the scenario in which the logical sentence $\phi$ holds. Every alternative output except the actual one is a logical impossibility, so this requires *counterpossible* reasoning. The authors admit: "it's not clear how to define a $\texttt{true}$ operator. Fortunately, we don't have to." Instead, the dependency structure is supplied as an input $G$, exactly as CDT is supplied a causal graph. Pearl's $do$ is then reused.

All the philosophical difficulty is therefore concentrated in the construction of $G$. The paper calls this "perhaps the largest open problem in the study of functional decision theory."

## 3. Subjunctive dependence: what goes into $G$

The paper's guiding notion is *subjunctive dependence*. "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Its illustration is two calculators computing $6288+1048$ on opposite sides of the globe. Neither causes the other's output, yet if (counterpossibly) the sum were different, both displays would differ.

Causal dependence is a special case: a scribe copying the calculator's display depends both causally and subjunctively on its output. Mere statistical correlation is not subjunctive dependence. Two calculators that happen to both be pink do not depend on each other's colour.

Hence the slogan: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" CDT intervenes on the *token* (my act); A-FDT intervenes on the *type* (the function's output). The source's central requirement is that the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

**[proposal] An operational edge criterion.** The paper does not supply a rule for building $G$. For applying A-FDT to new cases, I suggest the following.

1. Draw an edge from $\textsc{fdt}(\underline P,\underline G,\underline y)$ to a variable $Z$ when $Z$'s value is produced by a process that *computes or models* the agent's decision procedure on input $y$. Examples are a twin running the same reasoning, a predictor simulating the agent, and the agent's own body executing it.
2. Do not draw an edge when $Z$ merely correlates with the agent's behaviour through a common cause that does no such modelling, such as a lesion.
3. Represent imperfect modelling with an exogenous noise node (the paper's $\textsc{Accurate}$ or $\textsc{Luck}$), not by weakening the edge.

This matches every graph in the paper. It does not resolve borderline cases, such as a crude predictor using a heuristic correlated with the agent's decisions.

## 4. A worked recipe

Here is how one would apply A-FDT to an unfamiliar problem. Steps 1, 3 and 5 restate the paper's practice; steps 2 and 4 contain my additions.

1. **Enumerate the observations** $y$ the agent might receive. Introduce one logical node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ for each.
2. **Wire the act.** $\textsc{Act}$ is a deterministic function of whichever $F_y$ the agent actually gets to run. That depends on the variables determining her observation. Wire every predictor, twin or simulation of input $y$ as a child of $F_y$, with noise nodes as needed.
3. **Intervene on the actual node** $F_x$, for each $a\in\mathcal A$. Hold every other root, including the sibling nodes $F_y$ for $y\neq x$, at its prior.
4. **Assign priors to the siblings** $F_y$, $y\neq x$. **[proposal]** Use the self-consistent value: the action A-FDT would itself output at $y$. The paper usually notes that "the correct $q$ is 0 (or 1), as you may verify," but that "it won't matter" in its examples. In general it can matter (see §7).
5. **Compute** $\mathbb E(V \mid do(F_x=a))$ by propagating along $G$, and take the argmax. The paper does not state a tie-breaking rule.

## 5. Examples

Dollar figures stand for utilities throughout.

### Newcomb's problem

Box A holds \$1,000. Box B holds \$1,000,000 iff the predictor, who is right 99% of the time, predicted one-boxing.

In the A-FDT agent's graph, the node $\textsc{fdt}(\underline P,\underline G)$ is a parent of both $\textsc{Act}$ and $\textsc{Prediction}$, with $\textsc{Accurate}$ as noise on the prediction. Intervening gives:

$$
\mathbb E(V\mid do(F=\textit{onebox})) = 0.99(1{,}000{,}000) = 990{,}000,
$$
$$
\mathbb E(V\mid do(F=\textit{twobox})) = 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
$$

A-FDT one-boxes. CDT's graph places $\textsc{Box B}$ upstream of a separately intervened $\textsc{Act}$, so CDT gets $p\cdot 10^6$ versus $p\cdot 10^6 + 1000$ and two-boxes.

(The paper's prose gives \$999,000 for EDT's one-boxing value but \$990,000 for the A-FDT agent's. The latter is the arithmetically correct figure for a 99% predictor.)

The paper also answers an objection here. Suppose the agent is nearly certain she one-boxes and so believes box B is probably full. Should she then two-box? No. The hypothetical for two-boxing is a world in which *the function* outputs *twobox*, and in that world the predictor's model outputs it too. There is no retrocausation. As the paper puts it, the agent "just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P,G)$ taking on a different value."

### The smoking lesion

The lesion causes cancer and also a liking for smoking. Smoking itself is harmless and worth \$1,000. The paper models the lesion's effect on preference as two utility functions, $\mathcal U_S$ and $\mathcal U_R$. Each corresponds to a distinct world-model, and therefore to a distinct logical node: $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The act is

$$\textsc{Act}(\textit{lesion},s,r)=s,\qquad \textsc{Act}(\textit{nolesion},s,r)=r.$$

Nothing about cancer depends on either logical node. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged. Smoking then beats refraining by exactly $p\cdot\$1{,}000$, the probability that this node is the one controlling her act times the value of smoking. A-FDT smokes.

So one rule gives one-boxing in Newcomb's problem and smoking in the smoking lesion problem. Gibbard and Harper had suggested that combination was unavailable. The paper adds that the lesion problem is "badly confused" and recommends abandoning it.

### Transparent Newcomb and Parfit's hitchhiker

Now both boxes are transparent. The predictor fills B iff she predicts the agent would one-box *upon seeing B full*. The A-FDT agent sees B full.

The graph has nodes $F_{\text{full}}$ and $F_{\text{empty}}$. $F_{\text{full}}$ drives $\textsc{Prediction}$. $\textsc{Prediction}$ determines which node controls $\textsc{Act}$. Let $q$ be the prior probability that $F_{\text{empty}}=\textit{twobox}$; the self-consistent value is $q=1$.

$$
do(F_{\text{full}}=\textit{onebox}):\quad 0.99(1{,}000{,}000) + 0.01\,q(1{,}000) = 990{,}000+10q,
$$
$$
do(F_{\text{full}}=\textit{twobox}):\quad 0.01(1{,}001{,}000) + 0.99\,q(1{,}000) = 10{,}010 + 990q.
$$

The paper prints the second value as "\$110,00 + q·\$990"; it should be \$10,010 + 990q. A-FDT one-boxes even while looking at a full box. In the two-box hypothetical the box is probably *empty*. The agent is imagining a world where she would not have made her actual observation.

**A note on the source.** In the transparent Newcomb computation, the paper writes the target expectation as $\mathbb E(V\mid do(F_{\text{full}}=a, \textsc{Obs}=\textit{full}))$. If $\textsc{Obs}=\textit{full}$ were genuinely conditioned on, the empty-box branch would vanish and the agent would two-box. The numbers the paper actually computes do not condition on the observation. They agree with Eq. (4) as stated. I therefore read Eq. (4) literally: observations select the intervention node and are not conditioned on.

This is also the paper's own account of the difference from "Timeless Decision Theory." Its (todo-tagged) footnote says that theory "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

Parfit's hitchhiker has the same structure. The driver rescues the agent (worth \$1,000,000) iff she predicts the agent will pay \$1,000 in the city. A-FDT pays, whereas CDT and EDT both refuse and are left in the desert. The paper presses the consistency point: one-boxing in transparent Newcomb "*is precisely equivalent to paying the driver in Parfit's hitchhiker problem*."

### Two blackmail problems

**XOR blackmail.** A perfect predictor sends a letter iff exactly one of the following holds:

- (i) there are no termites and the agent will pay \$1,000;
- (ii) there are termites (a \$1,000,000 loss) and the agent will refuse.

The node $F_{\text{letter}}$ affects whether the letter is sent, but it is not a parent of $\textsc{Infestation}$. Let $t$ be the prior probability of termites.

- If $F_{\text{letter}}=\textit{pay}$, the letter arrives exactly when there are no termites. Expected loss: $t(10^6) + (1-t)(10^3)$.
- If $F_{\text{letter}}=\textit{refuse}$, expected loss: $t(10^6)$.

Refusal wins. CDT also refuses, but for a different reason: in its hypotheticals the predictor would simply have erred. EDT pays.

**Mechanical blackmail.** A blackmailer runs a damaging program (costing \$1,000,000) only if she predicts payment of \$1,000. Paying when blackmailed means always being blackmailed and losing \$1,000. Refusing means being blackmailed only by prediction error. With error rate $\epsilon$, refusal costs $\epsilon\cdot 10^6$.

The paper concludes that A-FDT refuses at $\epsilon=0.0009$ (expected loss \$900 versus \$1,000). It pays at $\epsilon=0.0011$. (The paper writes "0.011%", which looks like a typo for 0.11%, since 0.011% would still favour refusal.) The threshold is $\epsilon^*=10^{-3}$. This illustrates that A-FDT is not dogmatically "never pay." It compares hypothetical *frequencies of being in the situation*, weighted by outcomes.

### Death in Damascus and the twin dilemma

When Death predicts perfectly, both $do(F=\textit{Aleppo})$ and $do(F=\textit{Damascus})$ put Death wherever the agent goes. A-FDT stays home and saves the \$1,000.

CDT, by contrast, is unstable here. The paper further argues that, even after settling, CDT would refuse to pay \$1 for a genuinely random coin that gives a 50% chance of survival. In the Psychological Twin Prisoner's Dilemma, the twin's choice is a child of the shared node, so A-FDT cooperates: \$1,000,000 versus \$1,000.

## 6. Dominance, control, and fairness

**Dominance.** The paper argues that dominance is not theory-neutral: "every method for constructing hypotheticals gives rise to its own notion of dominance." Two-boxing dominates only under CDT counterfactuals. Under A-FDT counterfactuals, which hold the subjunctive dependencies fixed, switching to two-boxing makes the agent worse off.

**Control.** The paper concedes that A-FDT agents act as though they control abstract functions. It replies that a deterministic CDT agent is in the same position with respect to its single physically possible act: "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

**Fairness.** The paper claims superiority only on "fair problems," where outcomes depend on the agent's *behaviour* rather than on which decision procedure produces it. Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." The authors acknowledge that formalizing fairness is open. Their footnote 15 gives a problem that punishes anyone who acts like a copy of the A-FDT agent; A-FDT always loses it.

The paper also argues that A-FDT acts as it would have precommitted to act. It claims A-FDT never assigns negative value to information and is "so far as we know, reflectively stable in fair problems." These are claims supported by examples, not theorems.

## 7. Where Equation (4) leaves things open

**(a) Constructing $G$.** This is the paper's own headline open problem. Every verdict above depends on edges the modeller supplies. There is no analogue of Pearl's theory for learning logical dependence from observation and experiment. My edge criterion (§3) is a heuristic, not a derivation.

**(b) The sibling nodes.** A-FDT intervenes on one node $F_x$ and leaves $F_y$, $y\neq x$, at their priors. In the paper's examples the answer is insensitive to those priors. In general it need not be.

**[my example]** Consider a coordination problem. Two exact copies of the agent receive different observations, *red* and *blue*. Each picks L or R, and both receive 10 iff the choices match. The red copy intervenes on $F_{\text{red}}$ with $F_{\text{blue}}$ held at its prior $q=P(F_{\text{blue}}=L)$. It then best-responds: L iff $q>1/2$. Both "all L" and "all R" are self-consistent, and if $q$ is exactly $1/2$, A-FDT is indifferent.

Policy-FDT avoids this. It chooses the whole map $\pi:\{\text{red},\text{blue}\}\to\{L,R\}$ at once, intervening jointly on all $F_y$:

$$
\pi^* = \arg\max_\pi \mathbb E\big(V \mid do(F_y = \pi(y)\ \forall y)\big), \qquad a = \pi^*(x).
$$

This is plausibly why the authors say the policy version "makes a difference in certain multi-agent dilemmas." My proposal of self-consistent sibling priors turns A-FDT into an equilibrium-selection problem. It does not by itself select a good equilibrium.

**(c) Probability-zero and self-referential priors.** EDT cannot condition on probability-zero acts. A-FDT's $do$ is defined regardless of the prior on $F_x$; the paper notes the prior on the intervened node is "inconsequential." What remains unsettled is the consistency of priors on *other* logical nodes, especially those whose values the agent could compute.

**(d) Bounded agents.** The paper studies idealized maximization over small models. It conjectures that bounded approximations inherit the same relative strengths, but does not demonstrate this.

## 8. When A-FDT agrees with CDT and EDT

The paper observes that the three theories coincide when all correlations between $\textsc{Act}$ and other variables are caused by $\textsc{Act}$, apart from the logical node itself:

$$
\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}(\underline P,\underline G)=a)].
$$

A-FDT therefore departs from familiar practice only where something *models* the agent: predictors, twins, copies, future selves facing the same decision, or other agents running the same algorithm. The paper's closing applications extend this to voting coalitions, gym-going across days, and AI systems that can be copied and predicted.

## 9. Conclusion

A-FDT is CDT's machinery applied at a different point. A-FDT keeps expected-utility maximization and Pearl surgery, but moves the surgery from the physical act to the node representing "the output of this very function on this input." Observations change which node is operated on; they are not conditioned on.

From this one change follow its main verdicts:

- one-boxing in Newcomb's problem;
- smoking in the smoking lesion problem;
- paying the driver in Parfit's hitchhiker;
- one-boxing before full transparent boxes;
- refusing both blackmailers (the mechanical one below a precise error threshold);
- staying calmly in Damascus.

The price is that everything rests on a graph of subjunctive dependence that no one yet knows how to infer. Equation (4) also leaves unspecified how to treat the agent's other possible inputs, a gap that the authors' policy-level formulation is meant to close. To use A-FDT on a new case:

1. draw the dependencies honestly, with an edge wherever something computes your decision and none where something merely correlates with it;
2. intervene on your own output;
3. let the hypothetical worlds include the observations you would then have received.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.