# Action Functional Decision Theory (A-FDT): Choosing the Output of One's Decision Function

## 1. Orientation

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a decision rule that, in their words, answers the question "Which output of this very function would yield the best outcome?" The paper's main formal statement is Equation (4) in Section 5. That equation intervenes on a variable standing for the output of the agent's decision procedure on a *particular input*, and the procedure returns an *action*.

Footnotes 7 and 16 say the authors' "preferred formalization" instead chooses a *policy*, meaning a map from observations to actions. To keep these two apart, I call the action-valued rule of Equation (4) **A-FDT** (action functional decision theory). I call the footnoted alternative **policy-FDT**. When I quote the paper, its label "FDT" refers to the A-FDT equation unless I say otherwise.

The essay covers five things:

1. The shared expected-utility framework.
2. The A-FDT equation and each of its ingredients.
3. A step-by-step procedure, applied to several standard cases.
4. The points the paper leaves underdetermined, with operational proposals of my own, clearly marked.
5. Where A-FDT and policy-FDT can come apart.

## 2. The common skeleton: expected utility over hypotheticals

The paper treats EDT, CDT and A-FDT as three instances of one schema. An agent with observation history $x$ chooses an action $a$ maximizing

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $P(a \hookrightarrow o_j; x)$ is "the probability that $o_j$ will obtain in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Following Joyce, the authors hold that the theories do not disagree about value. They disagree only about how to interpret the connective $\hookrightarrow$, that is, how to build the *hypothetical* $M^{a\hookrightarrow}$ from the world-model $M$. In the paper's words, hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs."

Write $V = \mathcal U(\textsc{Outcome})$. The two classical rules are:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a), \tag{2}
$$
$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x). \tag{3}
$$

EDT conditions on the act. CDT performs Pearl-style surgery on the physical act node of a causal graph $G$. Surgery recomputes everything downstream of $\textsc{Act}$ and leaves everything else at its prior (observation-conditioned) distribution.

## 3. The A-FDT equation

The paper's Equation (4), with the left-hand label written in this essay's naming, is

$$
\boxed{\;\text{A-FDT}(P,G,x) \;=\; \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).\;} \tag{4}
$$

Each ingredient does specific work.

**$P$.** $P$ is a probability distribution over world variables. Unlike EDT's and CDT's distributions, it also contains variables for the *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$, "one that (hopefully) has most of its probability on $7336$."

**$G$.** $G$ is a graph that tells us "how changing a logical variable affects all other variables." It plays the role a causal graph plays for CDT, but it encodes *subjunctive* dependence. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**The intervention node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a node in the model. It *represents* the value that the decision procedure returns on exactly this input $(P,G,x)$. The underlines denote dequoting: the node's name is built from the inputs.

This is self-referential, since the model contains a node naming the model. The paper says the self-reference is harmless. The agent needs a variable *representing* the output, not knowledge of its value, and quining (Kleene's recursion theorem) shows such self-describing structures exist. Below I abbreviate the node as $D_x$.

**The $\mathtt{do}$ operator.** $\mathtt{do}(D_x=a)$ sets $D_x$ to $a$ and recomputes its descendants in $G$. Variables that are not descendants keep their prior distribution.

The paper names two differences from CDT:

1. **Point of surgery.** CDT intervenes on the *token* physical act. A-FDT intervenes on the *type*, the output of the function. Every process whose behavior subjunctively depends on that function changes together: the agent's body, a twin, a predictor's model.
2. **Treatment of observation.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Observing $x$ makes the agent intervene on $D_x$ instead of $D_y$.

### What Equation (4) does *not* do: it does not condition on $x$

Read literally, Equation (4) contains no "$\textsc{Obs}=x$" term. In the transparent Newcomb worked example, the paper's displayed expression does include "$\textsc{Obs}=\textit{full}$" inside the intervention. However, the computation that follows sums over the case where the predictor erred and the box is *empty*. So the observation is plainly *not* conditioned on.

I therefore adopt this reading: **under A-FDT, $x$ affects the computation only by fixing which node is intervened on.** Expectations are taken over the agent's unconditioned (prior) model. This is what lets A-FDT "imagine a world in which she was never blackmailed in the first place." The paper also says that the earlier Timeless Decision Theory, which both conditions *and* moves the intervention point, suffers a harmful "double update."

## 4. Subjunctive dependence and what $G$ must contain

The paper's informal criterion is that, when an agent imagines taking a different action, "she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

- **Predictors and twins depend on the node.** Two calculators computing the same sum, or a predictor holding an accurate model of the agent, depend subjunctively on the computed function.
- **Common causes do not.** A lesion that causes both smoking-desire and cancer does not depend on the agent's decision function. Neither does a coincidental correlation, like two calculators that happen both to be pink.
- **Causal dependence is a special case.** A scribe copying a calculator's output depends on it both causally and subjunctively.

The paper is explicit that it supplies no method for deriving $G$: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." So $G$ is an *input* to A-FDT, just as the causal graph is an input to CDT.

### An operational recipe for building $G$ (my proposal, not the paper's)

To apply A-FDT to new cases, I suggest building $G$ as follows. These rules are distilled from the paper's own graphs but are not stated by the authors.

1. **Start from a causal model** of the situation: exogenous noise, mechanisms, outcome, and $V$.
2. **Add a logical node $D_y$ for each input** $y$ on which the agent's procedure might be run in the scenario, including inputs it is not actually receiving.
3. **Link $D_y$ to every process that evaluates the agent's function on $y$.** For each mechanism that evaluates, simulates, or reliably models the agent's function on input $y$, draw an edge $D_y \to$ (that mechanism). Represent imperfection with an independent noise parent, such as the paper's $\textsc{Accurate}$ node.
4. **Make the physical act a multiplexer.** $\textsc{Act}$ takes value $D_y$ for whichever $y$ the agent actually receives, so the variables that determine the observation are parents of $\textsc{Act}$.
5. **Add no edge from $D_y$ to variables merely correlated with the act through common causes.** Lesions, genes and coincidences fall in this category.
6. **Handle preferences or beliefs the agent cannot introspect.** If the agent's inputs differ across possibilities, give each its own $D$-node and gate $\textsc{Act}$ on the latent variable. The paper does exactly this in the smoking lesion.

The non-intervened nodes $D_y$ for $y\neq x$ need prior distributions. The paper calls these $q$ and says "it doesn't matter" in its examples. That is true there, but not in general (Section 7).

### The procedure

Given $(P,G,x)$:

1. Locate $D_x$.
2. For each $a\in\mathcal A$, form $P(\cdot\mid \mathtt{do}(D_x=a))$, using the prior over all nondescendants of $D_x$, including the other nodes $D_y$.
3. Compute $\mathbb E[V]$ under each hypothetical.
4. Output the argmax.

## 5. Worked examples

All payoffs are in utility-dollars, as in the paper.

### Twin prisoner's dilemma

The agent and her twin both implement the function, so $D\to\textsc{Act}_{\text{me}}$ and $D\to\textsc{Act}_{\text{twin}}$. The two hypotheticals give:

- $\mathtt{do}(D=C)$ yields 1,000,000.
- $\mathtt{do}(D=D)$ yields 1,000.

A-FDT cooperates. A CDT agent, holding the twin's act fixed, defects by dominance.

### Newcomb's problem (99% accurate predictor)

The graph has $D\to\textsc{Act}$ and $D\to\textsc{Prediction}\leftarrow\textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$.

$$
\mathbb E[V\mid\mathtt{do}(D=\text{one})] = 0.99\cdot 10^6 = 990{,}000,
$$
$$
\mathbb E[V\mid\mathtt{do}(D=\text{two})] = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.
$$

A-FDT one-boxes. The paper stresses that no retrocausation is assumed. The agent simply refuses to imagine her action changing while "the FDT algorithm" stays fixed, much as one would not imagine a calculator showing a different sum while $6288+1048=7336$ holds.

### Smoking lesion

The lesion sets the agent's utility function: $\mathcal U_S$ if she has the lesion and $\mathcal U_R$ if not. So there are two possible intervention nodes, $D_S=\textsc{fdt}(\underline{P_S},\underline G)$ and $D_R$, and $\textsc{Act}=D_S$ if $\textsc{Lesion}$, else $D_R$.

Crucially, $D_S$ has no edge to $\textsc{Cancer}$. With $p = P(\text{lesion})$, the hypotheticals differ only through $\textsc{Act}$ in lesion-worlds. Smoking beats refraining by $p\cdot 1{,}000$, so A-FDT smokes. The same rule that one-boxes in Newcomb's problem therefore smokes here. The paper's diagnosis is that "the cancer is not evaluating the agent's future decisions."

### Transparent Newcomb (agent sees box B full)

$\textsc{Prediction}$ depends on $D_{\text{full}}$ and noise. The observation the agent receives is determined by $\textsc{Prediction}$, which therefore selects whether $D_{\text{full}}$ or $D_{\text{empty}}$ drives $\textsc{Act}$. Let $q = P(D_{\text{empty}}=\text{two})$. Without conditioning on "full":

$$
\mathbb E[V\mid \mathtt{do}(D_{\text{full}}=\text{one})] = 0.99\cdot 10^6 + 0.01\cdot q\cdot 1{,}000 = 990{,}000 + 10q,
$$
$$
\mathbb E[V\mid \mathtt{do}(D_{\text{full}}=\text{two})] = 0.01\cdot 1{,}001{,}000 + 0.99\cdot q \cdot 1{,}000 = 10{,}010 + 990q.
$$

The paper's printed figure "\$110,00" for the first term of the second line looks like a typesetting slip for \$10,010. One-boxing wins for every $q\in[0,1]$.

This example shows A-FDT's most striking trait. While *looking at* a full box, the agent evaluates two-boxing by imagining a world in which she probably sees an empty one. The paper argues that this case is "precisely equivalent" to paying the driver in Parfit's hitchhiker. It supports the verdict with arguments from precommitment, from value of information, and above all from utility.

### XOR blackmail (infallible predictor)

The letter is sent iff either (no termites and the agent pays on receipt) or (termites and the agent refuses). Let $p=P(\text{termites})$. Termites are a nondescendant of $D_{\text{letter}}$; the letter is a descendant.

- $\mathtt{do}(D_{\text{letter}}=\text{pay})$:
  - No termites: the letter is sent, she pays, and $V=-1{,}000$.
  - Termites: no letter is sent, and she suffers the infestation, $-10^6$.
  - Total: $-(1-p)\,1{,}000 - p\,10^6$.
- $\mathtt{do}(D_{\text{letter}}=\text{refuse})$:
  - Total: $-p\,10^6$.

A-FDT refuses, as CDT does but EDT does not. The *counterfactuals* differ, though. Asked what would have happened had she paid, the A-FDT agent says she would not have received the letter. The CDT agent says the infallible predictor would have erred.

### Mechanical blackmail with a fallible blackmailer

Suppose the blackmailer wrongly predicts payment with probability $\varepsilon$.

- Under $\mathtt{do}(D_{\text{blackmail}}=\text{pay})$, the agent is blackmailed and loses 1,000.
- Under refuse, she is blackmailed only with probability $\varepsilon$ and then loses $10^6$, for an expected loss of $\varepsilon\cdot 10^6$.

So A-FDT refuses iff $\varepsilon<10^{-3}$. The paper's case $\varepsilon=0.0009$ gives an expected loss of \$900, so she refuses, "even though she *knows* that the blackmailer predicted wrongly."

The paper's companion figure of "0.011%" for the case where she pays seems inconsistent with this threshold. Presumably some value above 0.1% is meant. Either way, the threshold computation is the operative content.

### Death in Damascus

Death's appointment book is an accurate prediction of the agent's procedure, so $D\to\textsc{Book}$ and $D\to\textsc{Act}$. Under either intervention Death meets her, and fleeing costs an additional 1,000. A-FDT stays, stably and without ratification.

The paper contrasts this with CDT. CDT oscillates, and under several ways of resolving the oscillation it declines to pay \$1 for a truly random coin that offers a 50% chance of survival.

## 6. Shared structure and the dominance argument

Two general claims from the paper are useful when deciding new cases.

**Agreement in ordinary cases.** If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the act's dependence on $D$, then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(D=a)],
$$

and all three theories agree. Divergence requires something other than the agent's own act, such as a predictor or a copy, that tracks the agent's function.

**Dominance is theory-relative.** CDT's dominance argument for two-boxing holds the prediction fixed while the act varies. That is just CDT's hypothetical restated. A-FDT has its own dominance notion, which holds subjunctive dependencies fixed, and it never violates that notion. The paper concludes that dominance is no neutral arbiter, and that theories should be compared by utility achieved in "fair" problems. In such problems the outcome depends only on the agent's behavior in the problem at hand, not directly on her procedure.

## 7. Open questions and operational resolutions

### (a) Where does $G$ come from?

The paper offers no theory of this. Its fallback is that humans "have some ability to notice when they are being predicted," and that A-FDT needs only narrow counterpossibles of the form "How would this predictor's prediction of my action change if the FDT algorithm had a different output?"

The rules in Section 4 are my proposal for applying A-FDT in practice. Their weakest point is rule 3. Deciding *how much* a process "models" the agent, as opposed to sharing a common cause with her, is exactly the unresolved question. Partial similarity, such as a rough psychological profile or a similar but non-identical algorithm, is not covered by the paper. A natural extension, which is my own suggestion, uses an edge with a noise node whose reliability parameter equals one's credence that the process tracks the function. This yields graded verdicts like the blackmail threshold above.

### (b) Counterpossibles

The output of a deterministic function on a given input is logically fixed, so $\mathtt{do}(D_x=a)$ for the non-actual $a$ is a counterpossible. The paper's more principled operator $\mathtt{true}(\phi)$ is left undefined, and $G$ substitutes for it.

The paper also blocks an obvious escape. An agent that asks "what if I used a different function?" (their FDT′) still has to model how predictors of $d$ would respond as if $d$ behaved like $f_n$. That brings back the same counterpossible.

The paper's defence is a parity argument. A deterministic CDT agent also "imagines" that its single physically possible act varies, so any objection to type-level "control" applies to token-level control as well.

### (c) Priors on the other nodes $D_y$

Equation (4) leaves $P(D_y)$ for $y\neq x$ to the agent's prior. The paper notes the correct values in its examples ($q=1$ in transparent Newcomb, $q=0$ in the lesion case) and shows the verdict is insensitive to them there. In general it is not.

Here is my own example. A fair coin shows the agent L or R. A perfect predictor pays $10^6$ if the agent's responses to L and R are both $a$, pays $2\cdot 10^6$ if both are $b$, and pays nothing otherwise.

On seeing L, A-FDT intervenes on $D_L$, holding $D_R$ at its prior $r=P(D_R=b)$:

$$
\mathbb E[V\mid\mathtt{do}(D_L=a)] = (1-r)\,10^6, \qquad \mathbb E[V\mid\mathtt{do}(D_L=b)] = r\cdot 2\cdot 10^6.
$$

So A-FDT picks $a$ whenever $r<1/3$. Suppose we impose the natural consistency requirement that the prior on $D_R$ match what A-FDT actually outputs on R. Then both $(a,a)$ and $(b,b)$ are self-consistent, and A-FDT can settle on the inferior one.

Policy-FDT avoids this. It intervenes on the whole map $\pi:\{L,R\}\to\mathcal A$ and selects $\pi=(b,b)$ directly.

My operational recommendations are:

- **Fixed-point condition.** Set priors on $D_y$ to A-FDT's own outputs where these are computable.
- **Policy fallback.** Where several fixed points exist, recognize that Equation (4) alone underdetermines the choice, and use the policy formulation the authors say they prefer.

The paper says the action–policy difference matters only "in certain multi-agent dilemmas" ("so far as we can tell"). The example above involves a predictor, so it fits that description loosely. It shows the gap arises whenever several input-instances of one's own function are jointly evaluated by the environment.

### (d) Fairness

The claim that A-FDT is optimal in "fair" problems has no formal backing. The paper admits that "a simple formal criterion for distinguishing fair dilemmas from unfair ones" is lacking. It also notes that a problem punishing anyone who matches a copy of the FDT agent defeats it, and that such problems have no obvious principled analogue for other theories.

## 8. Summary for practitioners

To decide an unfamiliar case with A-FDT:

1. **Model the world** causally, including any predictors, copies, or simulations of you.
2. **Add a node for "my function's output on this input,"** plus nodes for its outputs on other inputs the environment might evaluate.
3. **Draw edges** from those nodes to every process that computes or reliably predicts them, and to your physical act. Draw none to mere common-cause correlates.
4. **Intervene** on the node for your actual input, without conditioning on that input. Compare expected utilities and output the best action.
5. **Check sensitivity** to priors on your other-input nodes. If the answer depends on them, impose self-consistency, and if that still leaves several answers, choose at the policy level.

## 9. Conclusion

A-FDT keeps the expected-utility form shared with EDT and CDT, and with it Joyce's representation theorem. It changes the epistemic perspective: the agent intervenes on the logical output of her own decision function, and observations move the point of intervention instead of updating the distribution. Under this one change the agent one-boxes, smokes, pays the driver, ignores blackmail, cooperates with her twin, and stays calmly in Damascus.

The cost is foundational. A-FDT presupposes a graph of subjunctive dependencies and a way to entertain counterpossibles, and the paper supplies neither in general. Equation (4) is also silent about the agent's outputs on inputs she is not receiving. Section 7 argues that this gap is where action-level and policy-level versions of the theory come apart.

## References

- Yudkowsky, E., & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060).
- Gibbard, A., & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.