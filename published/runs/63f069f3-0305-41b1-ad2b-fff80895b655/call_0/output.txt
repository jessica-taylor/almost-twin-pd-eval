# Choosing Policies, Not Acts: An Essay on P-FDT

## 1. The source and what this essay does with it

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* presents functional decision theory mostly as a rule for choosing **actions**. The agent intervenes on a logical variable that represents what her decision function outputs on her current input. Twice, however, the authors say that this is not their preferred formulation. Footnote 7 reads:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I take as the primary source here, reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the theory sketched in these footnotes **P-FDT** (policy functional decision theory). The action-level theory defined by the paper's equation (4) I call **A-FDT**. I also discuss causal decision theory (**CDT**) and evidential decision theory (**EDT**).

The footnotes are brief, so most of the work here is reconstruction. I keep three kinds of claim apart:

- what the source actually says;
- what follows from combining the footnotes with the paper's formal machinery;
- choices I make where the source is silent. These are marked as **proposals**.

## 2. Background: decisions as surgery on a logical node

The paper treats EDT, CDT and FDT as expected-utility theories that differ only in how they build *hypotheticals*. All three maximize
$$
\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),
$$
and they disagree about how to read the connective "$\hookrightarrow$":

- **EDT** reads it as conditioning.
- **CDT** reads it as Pearl's $\mathtt{do}$-intervention on the physical action node $\textsc{Act}$.
- **FDT** also uses $\mathtt{do}$, but on a different node. Its world-model $(P,G)$ contains variables for the outputs of mathematical functions, including one for the output of FDT itself. The graph $G$ records *subjunctive dependence*: which events would differ if that function's output differed. The paper's equation (4) is
$$
\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \mid \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

Two features of equation (4) are worth noting.

1. The intervention node is indexed by the observation $x$. The paper stresses that FDT does not respond to observation by conditioning. Instead, "FDT responds to observation by changing which node it intervenes upon." Seeing a full box in the transparent Newcomb problem means intervening on $\textsc{fdt}(\underline P,\underline G,\textit{full})$ rather than $\textsc{fdt}(\underline P,\underline G,\textit{empty})$.
2. The other nodes, meaning the function's outputs on *other* inputs, are not intervened on. They keep whatever distribution $P$ gives them. In the paper's transparent Newcomb calculation, Fiona carries a prior $q$ that she two-boxes on seeing an empty box. The authors remark that "the correct value of $q$ is 1, … but in this case it doesn't matter."

That last remark points straight at the gap P-FDT fills. In A-FDT, the agent's beliefs about her own behaviour on other inputs are a free parameter. In the paper's examples the parameter happens not to matter. In general it can.

## 3. Defining P-FDT

Fix the agent's world-model $(P,G)$ and an input set $\mathcal X$: the possible observation histories on which this decision function might be run. Footnote 7 says policies are "mappings from observations to actions," so the policy space is
$$
\Pi=\mathcal A^{\mathcal X}=\{\pi:\mathcal X\to\mathcal A\}.
$$

Following footnote 16, replace the family of action-valued nodes $\{\textsc{fdt}(\underline P,\underline G,\underline x)\}_{x\in\mathcal X}$ with a single **policy-valued node** $\textsc{fdt}(\underline P,\underline G)$ taking values in $\Pi$. Every system in the world whose behaviour subjunctively depends on the function now reads its behaviour off this node. This includes:

- the agent's own body at a decision point with input $x_i$;
- a predictor's model of the agent being shown input $x_j$;
- a twin who receives input $x_k$.

Each such system is a child of the policy node, with structural equation
$$
\textsc{Behaviour}_i = \pi(x_i)\quad(\text{possibly composed with noise, e.g. a predictor's error variable}).
$$

The P-FDT rule then has two stages:
$$
\boxed{\;\pi^\ast \in \arg\max_{\pi\in\Pi}\ \mathbb E\!\left(V \mid \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G)=\pi\big)\right),\qquad \text{act}=\pi^\ast(x).\;}
$$

The first stage is "intervenes on the node $\mathrm{FDT}(-)$ to choose … a policy". The second is "to which the agent then applies her inputs in order to select an action."

Three points about this definition.

**(i) The observation enters only at the application stage.** On my reading, the expectation is taken under the same $P$ for every $x$. A-FDT already declines to condition on $x$ and lets $x$ merely select a node. P-FDT goes further: $x$ does not even select a node, and it only indexes into the chosen policy. This is the source of the theory's "updateless" character. The paper credits Wei Dai's Updateless Decision Theory as an early variant of FDT, though this credit appears in a draft note in the source rather than the published text.

**(ii) Why one $P$ for all inputs.** My argument, which goes beyond the source, is this. The node $\textsc{fdt}(\underline P,\underline G)$ names *one* function call. If the agent first updated $P$ on $x$ and then selected a policy, the computation run on input $x$ would differ from the one run on input $y$. Their outputs would no longer be values of a single policy node, and the coordination that P-FDT exists to secure would fall apart. Holding $P$ fixed is what makes "the policy" a well-defined logical object shared by all instances.

**(iii) Hypotheticals.** In the P-FDT hypothetical for $\pi$, every instance of the function behaves according to $\pi$ at once. Predictors predict $\pi$, twins play $\pi$, and the agent's body follows $\pi$. Nothing that does not subjunctively depend on the function changes: lesions, coin flips and the contents of the agent's genes are held fixed. That is the paper's analogy, "FDT is to subjunctive dependence as CDT is to causal dependence", lifted from outputs to whole input–output maps.

## 4. Applying P-FDT: a procedure and worked examples

Operationally, I suggest the following recipe. It is a proposal assembled from the paper's graphical method.

1. **Enumerate inputs.** List every observation history $x\in\mathcal X$ on which some instance of your decision function might run. Include inputs you are not currently facing and inputs fed to simulations of you.
2. **Build the graph.** Add one policy node. For each instance, add an edge from the policy node with equation $\pi(x_i)$. Model ordinary causal structure as in CDT.
3. **Score policies.** For each $\pi\in\mathcal A^{\mathcal X}$, compute $U(\pi)=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\pi)]$. Only the components of $\pi$ that some instance actually reads matter.
4. **Choose and apply.** Pick $\pi^\ast$ and output $\pi^\ast(x)$ for your actual input $x$.

### Example 1: Transparent Newcomb

**Setup.** The inputs are $\mathcal X=\{\textit{full},\textit{empty}\}$. The predictor, accurate with probability $0.99$, predicts $\pi(\textit{full})$. It fills box B iff it predicts *onebox*. The agent sees the box and acts on $\pi(\text{what she sees})$. Write $u_e$ for the payoff on an empty box: $\$0$ if $\pi(\textit{empty})=\textit{onebox}$ and $\$1{,}000$ if it is *twobox*.

**If $\pi(\textit{full})=\textit{onebox}$:**
- With probability $0.99$ the box is full and she one-boxes, receiving $\$1{,}000{,}000$.
- With probability $0.01$ it is empty and she plays $\pi(\textit{empty})$.
- So $U=990{,}000+0.01\,u_e$.

**If $\pi(\textit{full})=\textit{twobox}$:**
- With probability $0.01$ the box is full, receiving $\$1{,}001{,}000$.
- Otherwise it is empty.
- So $U=10{,}010+0.99\,u_e$.

**Result.** The four policies score:

| $\pi(\textit{full})$ | $\pi(\textit{empty})$ | $U(\pi)$ |
|---|---|---|
| onebox | twobox | 990,010 |
| onebox | onebox | 990,000 |
| twobox | twobox | 11,000 |
| twobox | onebox | 10,010 |

So $\pi^\ast=(\textit{full}\mapsto\textit{onebox},\ \textit{empty}\mapsto\textit{twobox})$. An agent who sees a full box one-boxes, as in the paper.

Note also that P-FDT *derives* the paper's "correct $q=1$" rather than leaving it as an input. The empty-box component of the optimal policy is "two-box."

### Example 2: Mechanical blackmail

**Setup.** The inputs are $\{\textit{blackmail},\varnothing\}$. The blackmailer runs the program iff she predicts $\pi(\textit{blackmail})=\textit{pay}$. She wrongly predicts *pay* with probability $\varepsilon$.

**Scores.**
- The policy "pay if blackmailed" yields $U=-1{,}000$.
- The policy "refuse if blackmailed" yields $U=-\varepsilon\cdot 1{,}000{,}000$.

**Result.** P-FDT refuses iff $\varepsilon<0.001$. This reproduces the paper's $\varepsilon=0.0009$ case: an expected loss of $\$900$, so she refuses. It also makes the threshold explicit.

The agent holding the letter may *know* the prediction was an error. She still refuses, because the policy is scored before, and independently of, the observation.

Parfit's hitchhiker works the same way, with input "in the city" and policy component "pay."

### Example 3: Where A-FDT and P-FDT come apart

The footnotes say policy selection matters in "multi-agent dilemmas." Here is the simplest case I know, my own construction in the spirit of those footnotes.

**Setup.** Two instances of the same decision function run in separate rooms. One is shown the label $1$, the other the label $2$. Each outputs $A$ or $B$. Each instance (or each instance's principal) receives:
- 2 if both output $A$;
- 1 if both output $B$;
- 0 if they mismatch.

**P-FDT.** Policies are pairs $(\pi(1),\pi(2))$, with
$$
U(A,A)=2,\quad U(B,B)=1,\quad U(A,B)=U(B,A)=0.
$$
P-FDT selects $(A,A)$, and each instance applies its label and outputs $A$.

**A-FDT in room 1.** This instance intervenes only on $\textsc{fdt}(\underline P,\underline G,1)$. It treats $\textsc{fdt}(\underline P,\underline G,2)$ as a variable with prior $r=P(\text{output }A)$. Then
$$
\mathbb E[V\mid \mathtt{do}(A)]=2r,\qquad \mathbb E[V\mid\mathtt{do}(B)]=1-r.
$$
So it outputs $A$ iff $r>1/3$.

**Why A-FDT can fail.** An A-FDT agent who expects its label-2 counterpart to play $B$ will play $B$. If both instances hold that belief, the belief is self-confirming. Formally, A-FDT finds *coordinate-wise* optima of $U$, the Nash-like fixed points of the instances' best responses. P-FDT finds the *joint* optimum.

The failure has the same shape the paper diagnoses in EDT, where Eve's choices are "at the mercy of her priors." A-FDT is at the mercy of its priors about its own behaviour on other inputs. The two instances are not literal twins with identical inputs, so the paper's twin-PD reasoning ("we both run this very reasoning") does not apply at the action level. It does apply at the policy level, because both instances share the node $\textsc{fdt}(\underline P,\underline G)$.

## 5. How the two formulations relate

The source says the difference "only matters in multi-agent dilemmas so far as we can tell." The following elementary observation, my own, makes the relationship precise.

**Proposition.** Suppose that under $P$ the A-FDT agent assigns probability $1$ to $\textsc{fdt}(\underline P,\underline G,y)=\pi^\ast(y)$ for every $y\neq x$, where $\pi^\ast$ is P-FDT-optimal. Suppose also that the action-indexed and policy-indexed graphs encode the same dependencies. Then $\pi^\ast(x)$ is A-FDT-optimal at $x$.

**Proof.** Under that belief, A-FDT's objective at $x$ is $a\mapsto U(\pi^\ast[x\mapsto a])$, where $\pi^\ast[x\mapsto a]$ is $\pi^\ast$ with its $x$-component replaced by $a$. Since $\pi^\ast$ maximizes $U$ over all policies, it in particular maximizes over this one-coordinate family. $\square$

So A-FDT run on *accurate self-beliefs about an optimal policy* never contradicts P-FDT, apart from ties. The converse fails, as Example 3 shows: A-FDT can sit at a suboptimal fixed point.

This is why the paper's single-agent examples come out the same either way. There, either the other-input components do not affect the comparison (in transparent Newcomb, $q$ enters both sides in a way that does not flip the ranking), or the paper stipulates the correct self-belief.

I would read the source's "multi-agent" broadly. It should cover any problem in which the function is instantiated on *several distinct inputs* whose joint behaviour matters. That includes a single agent who is simulated on hypothetical inputs, or who meets her own decision repeatedly with differing observations, as in the paper's gym example when the weeks differ observably. The source hedges with "so far as we can tell," and I see no principled reason the divergence must be confined to literally distinct people.

## 6. What the footnote leaves open, and how I propose to settle it

**(a) What counts as an "input".** Footnote 7 says "observations"; footnote 16 says "inputs." In the paper's smoking lesion treatment, the instances differ not by observation but by world-model: $\textsc{fdt}(\underline{P_S},\underline G)$ versus $\textsc{fdt}(\underline{P_R},\underline G)$, with different utility functions. Should a policy also range over model variants?

*Proposal:* follow footnote 7 and let policies map observations only. An agent with utility $\mathcal U_S$ runs a different function from one with $\mathcal U_R$; she does not optimize on the other's behalf. This preserves the paper's smoking result. Smoking adds $p\cdot\$1{,}000$ through the $\mathcal U_S$-instance and changes nothing about the lesion, which does not subjunctively depend on the function.

**(b) Which $P$.** Section 3 argued that $P$ must be shared across the inputs in $\mathcal X$. That leaves open *when* $P$ is fixed: at birth, at the start of the problem, or at some intermediate point.

*Proposal:* fix $P$ at the latest point before any observation on which some predictor or copy conditions its behaviour. That is the information state shared by every instance being coordinated. Fixing it later reintroduces A-FDT's coordinate-wise problem. Fixing it earlier than necessary invites mistakes from priors that have not yet absorbed knowledge every instance would share. This is a genuine philosophical choice the source does not make.

**(c) Zero-probability inputs.** Policies are total functions on $\mathcal X$, including inputs that are impossible under the selected policy, such as an empty box under a perfect predictor. Components on such inputs do not affect $U$, so ties among policies are common. Ties are harmless, since all tied policies give the same act on every input that actually occurs.

*Proposal:* for robustness against predictor error, break ties by the value under a small-noise perturbation. This is a trembling-hand refinement. In transparent Newcomb it is exactly what makes "empty $\mapsto$ twobox" strictly better.

**(d) Tie-breaking must be canonical.** Whatever rule is used, every instance must apply the *same* rule. Otherwise they may pick different maximizers and miscoordinate. Since the instances compute one function, a fixed deterministic ordering of $\Pi$ achieves this automatically.

**(e) Randomization.** The source is silent on mixed policies. *Proposal:* model randomization explicitly as actions such as "flip a truly random coin." The modeller then decides, case by case, whether predictors see the coin's outcome or only the policy. This matters in Death in Damascus. There P-FDT, unlike the CDT agent in the paper, would pay \$1 for a truly random coin that Death cannot predict: a 50% chance of a \$1,000,000 outcome easily outweighs \$1.

**(f) The open problem inherited from FDT.** P-FDT needs the graph $G$ telling it which systems read the policy node. The paper calls deducing such subjunctive dependencies "perhaps the largest open problem in the study of functional decision theory." Policy selection does not solve that problem. It does make one thing easier to state: what a predictor depends on is now a whole input–output map, which is arguably closer to what simulators actually compute.

**(g) Tractability.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$, which is enormous in realistic cases. The paper's own idealization ("maximizing over all possible actions is not realistic") applies with even more force here. Bounded P-FDT agents will need to restrict $\mathcal X$ to the inputs some instance actually reads, which is often only two or three.

## 7. Philosophical motivation

The paper's main arguments for FDT carry over to P-FDT, and arguably fit it better.

- **Precommitment.** The paper argues that "FDT agents simply act as they would have ideally precommitted to act." A precommitment is naturally a *policy*: a contingency plan specifying what to do upon each observation. P-FDT makes the parallel exact. Choosing $\pi^\ast$ under the shared prior is choosing the optimal contingency plan, and executing $\pi^\ast(x)$ is keeping it. Under A-FDT the parallel holds only when the agent's self-beliefs happen to be correct.
- **Reflective stability.** The paper claims FDT agents would not self-modify on receiving blackmail. For P-FDT this is close to definitional, given $P$ fixed as in §6(b). If the optimal policy refuses blackmail, no instance that later observes blackmail has any reason, by P-FDT's own lights, to want a different policy, since $P$ was not updated in between.
- **Value of information.** The paper says FDT agents do not assign negative value to information. Under P-FDT, any policy available to a less-informed agent is still available to the more-informed one, because a policy can simply ignore an input. So expanding $\mathcal X$ cannot lower $\max_\pi U(\pi)$ provided the information-receiving process does not itself change what predictors predict. That proviso is a substantive assumption of mine, not the source's.
- **The "global perspective".** The paper's slogan asks: "What would the entire universe look like if the FDT algorithm behaved differently?" The most complete description of how an algorithm "behaves" is its full input–output map. Intervening on that map is the most literal reading of the slogan.

The cost is the familiar one, sharpened. P-FDT agents knowingly take actions that are worse given their actual observation: refusing a blackmail they know to be mispredicted, leaving \$1,000 on the table. The paper's reply applies here too: "it's advantageous to be *the kind of agent* that makes such decisions." Whether one finds that convincing is the central philosophical dispute, and P-FDT simply commits to it more fully.

## 8. Conclusion

On the reading developed here, P-FDT is the functional decision theory that Yudkowsky and Soares describe as their preferred formulation. The agent intervenes on a single node representing her decision function's entire map from observations to actions. She selects the policy with highest expected utility under a model held fixed across inputs, and then applies it to the observation she actually has.

It agrees with the paper's action-level theory, A-FDT, whenever A-FDT's beliefs about its own behaviour on other inputs are correct. It improves on A-FDT when coordination across differently-informed instances is needed, because it optimizes jointly rather than coordinate-wise. That is the content behind the footnote's remark about "multi-agent dilemmas."

The footnote leaves several design choices open: the domain of inputs, the time at which the prior is fixed, tie-breaking, randomization, and above all the construction of the subjunctive-dependence graph. I have proposed principled defaults for the first four. The last remains the theory's main unresolved foundation.

## References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (esp. eq. 4, footnotes 7 and 16).
- Dai, W. (2009). "Towards a New Decision Theory." *Less Wrong*.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Pearl, J. (2000). *Causality*. Cambridge University Press.