# A-FDT: Choosing by Intervening on the Decision Function

## 1. The idea

Suppose you are about to choose, and you know that something else in the world, such as a predictor, a twin, or a blackmailer, is computing roughly what you are computing. The question is what you should hold fixed while you compare your options.

Causal decision theory (CDT) holds fixed everything not causally downstream of your physical act. Evidential decision theory (EDT) holds fixed nothing: it conditions on the act and lets every correlation ride along. The theory I will call **A-FDT** takes a third route. Its procedure is Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality". The source simply calls this theory FDT. I use "A-FDT" for the *action*-selecting procedure of Equation (4), because the authors say (footnotes 7 and 16) that their *preferred* formalization selects *policies*, mappings from observations to actions, and that the paper sets this aside. I take the "A-" prefix to mark that choice of the paper's presentation. The prefix is my gloss, not the source's.

The slogan is that the agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The agent does not ask which physical act would be best. She asks what the world would look like if her decision function returned a different value, and she imagines that change propagating to everything that depends on the function.

In this essay I do four things:
- define the procedure precisely;
- explain what it demands of the world-model, which is where the source is candid about open problems;
- work through examples, with the arithmetic checked;
- separate what the source claims from what I am adding.

## 2. Formal definition

### 2.1 The expected-utility frame

The source puts EDT, CDT and A-FDT in one frame. Each maximizes

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j) \tag{1}$$

over a finite action set $\mathcal A$. Here $x$ is an observation history and $\hookrightarrow$ is the connective for "decision hypotheticals". By Joyce's representation theorem, the theories do not disagree about *valuing*. They disagree about "the epistemic perspective from which actions are to be evaluated", that is, about how $\hookrightarrow$ is interpreted.

- **EDT**: $\hookrightarrow$ is conditioning, $\operatorname{argmax}_a \mathbb E(V \mid \mathrm{Obs}=x,\mathrm{Act}=a)$ (Eq. 2).
- **CDT**: $\hookrightarrow$ is Pearl's intervention on the physical act node, $\operatorname{argmax}_a \mathbb E(V \mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$ (Eq. 3). The observation is conditioned on.
- **A-FDT** (Eq. 4):

$$\text{A-FDT}(P,G,x) := \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}$$

### 2.2 The ingredients

- $P$ is a probability distribution over the agent's model variables. These include variables for the outputs of mathematical functions. The source's example is a variable for $6288+1048$ that puts most of its mass on 7336.
- $G$ is a graph, in the source's words, "that tells us how changing a logical variable affects all other variables".
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node standing for the output of the very procedure being run, given those inputs. The underlines are dequoting. If $x := 3$ then $Z\underline{x}$ names the variable $Z3$.
- $do(\cdot)$ is Pearl's operator. The source describes it roughly: it updates everything downstream of the intervened variable, according to $G$, and leaves everything else untouched.

For readers who want something more explicit, here is my own formalization, which is consistent with the source's use of Pearl but is not given there. Treat $(P,G)$ as a structural model. Each node is $X_i = f_i(\mathrm{pa}_i, u_i)$ with exogenous noise $u$ drawn from $P$. One node, $F_x:=\mathrm{fdt}(P,G,x)$, is the decision-function node. Then

$$\mathbb E\big(V\mid do(F_x=a)\big)=\sum_u P(u)\,\mathcal U\!\big(\mathrm{Outcome}^{\,F_x\leftarrow a}(u)\big),$$

where the superscript means "recompute every node with $F_x$'s equation replaced by the constant $a$". Everything the graph connects below $F_x$ moves, and nothing else does.

### 2.3 Two differences from CDT

The source identifies exactly two differences between Eq. (3) and Eq. (4).

1. **The intervention site.** CDT intervenes on $\mathrm{Act}$, a physical fact about her body. A-FDT intervenes on $F_x$, a logical fact about her decision function. In Peirce's terms, CDT intervenes on a *token* and A-FDT on a *type*.
2. **The handling of observations.** CDT conditions on the observation. A-FDT does not. It "responds to observation by changing which node it intervenes upon". After seeing $y$ rather than $x$, the agent intervenes on $F_y$ instead of $F_x$.

The second difference matters a great deal. Observations enter A-FDT through the *index* of the node, so the graph $G$ must say how each $F_{x'}$ for each possible observation $x'$ drives the action. The source's examples show this in practice. In the transparent Newcomb problem, $\mathrm{Act}$ depends on $F_{\text{full}}$, $F_{\text{empty}}$ and $\mathrm{Prediction}$, and the prediction determines which node controls the act, because the prediction determines which observation the agent receives. So when the agent imagines changing $F_{\text{full}}$, she may imagine receiving a *different observation*. The source says so directly: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

A caution about the source's notation. In the transparent Newcomb calculation it writes $\mathbb E(V\mid do(\mathrm{fdt}(\ldots,\textit{full})=a,\ \mathrm{Obs}=\textit{full}))$, but the worked calculation lets the box be empty in some hypothetical worlds. I read "$\mathrm{Obs}=\textit{full}$" there as *indicating which node is intervened on*, not as a conditioning that pins the box's contents in the hypothetical. Otherwise the calculation would not go through. Equation (4) as displayed has no conditioning on $x$ at all.

### 2.4 Self-reference

The node $F_x$ is named using $P$ and $G$, which themselves contain the node. This looks circular. The source answers that the agent need not know the *value* of $\text{A-FDT}(P,G,x)$ to have a variable *representing* it. Kleene's second recursion theorem shows how a data structure can contain an accurate representation of itself ("quining"). Consequently A-FDT does not require a prior over its own output. It also does not need a ratification step, because the intervention overrides whatever the prior said.

### 2.5 When A-FDT agrees with CDT and EDT

The source records a simple agreement condition. If every correlation between the act and other variables is *caused* by the act, apart from possible subjunctive dependence on $F$ itself, then

$$\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(F=a)].$$

All three theories then return the same action. They come apart only when something correlates with the act without being caused by it. Predictors, twins and copies are the paradigm cases.

## 3. Subjunctive dependence: what $G$ must encode

### 3.1 The source's account

Equation (4) is only as good as the graph fed into it. The source's central concept is *subjunctive dependence*: when two physical systems compute the same function, "their behaviors 'subjunctively depend' upon that function". Three of the source's observations delimit the concept.

- **Causal dependence is a special case.** A scribe copying a calculator's output depends on it subjunctively, because if the calculator output something else she would write something else.
- **Mere statistical correlation does not suffice.** Two pink calculators in Paris and Tokyo have no subjunctive dependency between their colors. If the Paris calculator had been green, Tokyo's would still be pink.
- **Imperfect modeling weakens dependence without removing it.** A predictor that is 99% accurate yields 99% dependence. This is how the $\mathrm{Accurate}$ noise node enters the Newcomb graph.

The source's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." In its words, CDT hypotheticals preserve only causal structure, while FDT hypotheticals "preserve all decision-relevant subjunctive dependencies".

### 3.2 Counterpossibles and the source's stance

If the function in fact outputs *onebox*, then "it outputs *twobox*" is logically false, so the hypotheticals are counterpossible. The source concedes this is the main drawback relative to CDT. It also argues that the difficulty is "technical rather than philosophical", since humans reason comfortably under logical uncertainty. It further says A-FDT only needs narrow counterpossibles, such as "How would this predictor's prediction of my action change if the FDT algorithm had a different output?" Its operational fix is to avoid defining a $\mathtt{true}(\cdot)$ operator on logical sentences and instead *require $G$ as an input*, "in the same way that the relevant causal structure is given as an input to CDT".

The source is explicit that this rests on "shakier philosophical foundations" than CDT. Pearl has a theory of how to learn causal structure from observation and intervention, and no analogous theory exists for subjunctive structure. The source calls this "perhaps the largest open problem in the study of functional decision theory."

### 3.3 What I propose as an operational reading

The paper does not say how a user should actually draw $G$. Here is a working discipline. It is my proposal, consistent with the source's examples but not stated by it.

1. **Name the decision function and its instances.** List every process in the scenario that (a) runs the same computation, as a twin does, or (b) contains a model of it accurate enough to reproduce its output, as a predictor does. Include the agent's own body or brain as one instance.
2. **Add edges from $F$ to each instance's output**, mediated by a noise node if the instance is imperfect. That node has probability $\varepsilon$ of breaking the link. Newcomb's $\mathrm{Accurate}$ is such a node.
3. **Add no edge from $F$ to a variable that merely correlates** with the act through a common cause or by coincidence. A lesion that is not modeling the agent gets no edge.
4. **Give ordinary causal edges downstream of those instances in the usual way.** Boxes get filled because of the prediction, utilities follow from outcomes, and so on.
5. **For each possible observation $x$, create a node $F_x$** and wire the act to whichever $F_x$ applies. If the observation is itself produced by an instance of the function, the wiring must make that visible, as in the transparent Newcomb graph.
6. **Run the "swap test" as a sanity check on each edge.** If the function returned a different value *and everything else logical and physical stayed consistent*, would this variable be different? Calculators computing the same sum pass. Pink calculators fail.

Step 2's noise node has a consequence worth stating. Dependence is graded, and the source's blackmail example with an error rate shows the results are sensitive to the rate. In practice the main modeling work is estimating $\varepsilon$. One more limit should be flagged. I have given a checklist and not an algorithm. Where it is ambiguous whether a process "models" the agent, for instance a predictor that tracks only a crude behavioral proxy, the source gives no determinate answer, and any answer needs extra assumptions.

## 4. Worked examples

All numbers use the source's dollar-valued utilities.

### 4.1 Newcomb's problem

The graph has $F \to \mathrm{Act}$ and $F\to\mathrm{Prediction}\to\mathrm{Box\,B}$. $\mathrm{Accurate}$, with probability 0.99, feeds into $\mathrm{Prediction}$. Both payoffs are in $V$.

- $do(F=\textit{onebox})$: the act is *onebox*, and Box B is full with probability 0.99. Expected value is $0.99\times 1{,}000{,}000=\$990{,}000$.
- $do(F=\textit{twobox})$: the act is *twobox*, and Box B is full with probability 0.01. Expected value is $0.01\times 1{,}001{,}000 + 0.99\times 1{,}000=\$11{,}000$.

So A-FDT one-boxes.

CDT, by contrast, cuts the edge from the act to the prediction and finds that, for any probability $p$ that the box is full, two-boxing is better by $\$1{,}000$. The source stresses that this is no retrocausal claim: A-FDT "does not think that a physical signal passes between her action and the predictor's prediction; she just thinks it is foolish to imagine her action changing without also imagining $\text{FDT}(P^F,G^F)$ taking on a different value". Suppose a skeptic objects that she is nearly sure the box is full, so why not take both. The answer is that the "what if I two-boxed" question is answered inside the intervention on $F$, not by conditioning on the current belief about the box.

### 4.2 The smoking lesion

Here the graph differs from Newcomb's, even though CDT and EDT can reuse their Newcomb models by renaming variables. The source builds $G$ so that $F$ drives $\mathrm{Act}$ but not $\mathrm{Cancer}$, since the lesion "is not evaluating the agent's future decisions". Intervening on $F$ leaves the probability $p$ of the lesion unchanged. The source's formalization is quite contrived (the agent is uncertain about her own preferences, via two utility functions), and the source itself recommends abandoning the problem. In that model, smoking beats refraining by exactly $p\cdot\$1{,}000$. So A-FDT smokes and one-boxes under a single rule. This is the point: the same procedure gives different answers because different *graphs* are fed in, and the graphs differ because the dependence structures differ.

### 4.3 The transparent Newcomb problem and Parfit's hitchhiker

Take $F_{\text{full}}$ and $F_{\text{empty}}$ as above. Let $q$ be the agent's credence that she two-boxes on seeing an empty box.

- $do(F_{\text{full}}=\textit{onebox})$: with probability 0.99 the prediction is accurate, the box is full and she one-boxes, giving $\$1{,}000{,}000$. Otherwise she sees an empty box and $F_{\text{empty}}$ drives the act. Total $\$990{,}000+10q$.
- $do(F_{\text{full}}=\textit{twobox})$: with probability 0.99 the predictor foresaw this, the box is empty, and $F_{\text{empty}}$ drives the act, giving $1{,}000q$. With probability 0.01 the box is full and she takes both, giving $\$1{,}001{,}000$. Total $\$10{,}010+990q$.

The source prints the second figure as "$\$110{,}00+q\cdot\$990$", an apparent typo. My recomputation gives the figure above, and the conclusion is unchanged: for any $q\in[0,1]$, one-boxing wins.

Parfit's hitchhiker has the same structure, and the source says one-boxing in the transparent problem is "precisely equivalent to paying the driver". With my own simplified numbers (a 99%-accurate lie detector, $\$1{,}000$ to pay, death worth $-\$1{,}000{,}000$): $do(F_{\text{city}}=\textit{pay})$ gives $0.99(-1{,}000)+0.01(-1{,}000{,}000)=-\$10{,}990$, while refusing gives $0.01\cdot 0 + 0.99(-1{,}000{,}000)=-\$990{,}000$. A-FDT pays. This is an illustration I computed, not a calculation in the source.

### 4.4 Mechanical blackmail with a fallible predictor

The blackmailer runs the program iff she predicts the agent would pay on receiving the letter. Suppose she wrongly predicts "pay" with probability $\varepsilon$ when the true output is "refuse". Then:

- $do(F_{\text{letter}}=\textit{pay})$: she is always blackmailed and always loses $\$1{,}000$.
- $do(F_{\text{letter}}=\textit{refuse})$: she is blackmailed with probability $\varepsilon$ and then loses $\$1{,}000{,}000$, so the expected loss is $\varepsilon\cdot 10^6$.

Refusing is better iff $\varepsilon<0.001$. The source works the cases $\varepsilon=0.0009$ (refuse, expected loss $\$900$) and $\varepsilon=0.00011$ (pay). Two features are striking. First, with the letter in hand, A-FDT may refuse even though she "*knows* that the blackmailer predicted wrongly". Second, a perfect blackmailer simply never blackmails her: "her counterfactual reasoning is proven correct." The approach is also dynamically stable on this problem. The source says that "FDT agents always act as they would have precommitted to act", so no costly commitment device is needed.

### 4.5 Death in Damascus

Death's appointment book is written on the basis of a prediction of the agent's decision procedure. The graph therefore gives $F\to\mathrm{Act}$ and $F\to\mathrm{Death's\ location}$. Staying gives $\$0$ (she dies), and fleeing gives $-\$1{,}000$ (she dies anyway). A-FDT stays. CDT, by holding Death's location fixed while varying the act, flips between the two answers as its credences change (the "instability" the source describes), and it will even refuse a $\$1$ truly random coin worth a 50% chance of survival.

### 4.6 The XOR blackmail

This is where the *shape* of the dependence matters. The letter-sending predictor depends on both the infestation and $F_{\text{letter}}$, and the infestation does *not* depend on $F$. When A-FDT imagines paying, the hypothetical contains a different probability of *receiving the letter* but the same probability of termites, so paying buys nothing. EDT, which conditions, treats the letter as good news upon payment and pays. A-FDT refuses.

## 5. Why the construction is principled (and where it is not)

### 5.1 The source's arguments

The source gives several kinds of argument.

- **Utility.** A-FDT agents tend to end up richer in the dilemmas considered. The source calls this "the argument that gives the precommitment and value-of-information arguments their teeth."
- **Endorsement.** A good theory should recommend its own use. The source argues CDT, by contrast, would recommend self-modifying away from itself in future dilemmas.
- **Dominance is theory-relative.** Each method of constructing hypotheticals has its own dominance principle. CDT's holds the prediction fixed while switching the act, which the source compares to being "handed a well-functioning calculator calculating $6288+1048$ and asked to imagine it outputting 3159, holding constant the fact that $6288+1048=7336$." A-FDT's holds the subjunctive dependencies fixed. Dominance is therefore "not a neutral criterion".
- **Balanced hypotheticals.** EDT "respects too many action-environment correlations, while CDT respects too few." The cosmic ray problem illustrates EDT's failure: an agent who would normally take $\$1$ reasons that taking $\$100$ must mean she was hit by a ray.
- **Fairness.** The source's boundary on its claims is that problems must be "fair". The outcome must depend only on the agent's behavior in the problem, with the agent's beliefs accurate. "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*." A predictor who rewards the use of a specific algorithm is a different matter, since "no decision theory is safe" there. The source also says it lacks a formal criterion for fairness.

### 5.2 The "global perspective"

The source's philosophical gloss is that A-FDT asks "What would the entire universe look like if the FDT algorithm behaved differently?" and picks the best such universe. It argues that this involves no more delusion than CDT's imagining a deterministic agent's act varying: "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token." The claim is minimal and instrumental: "if an agent wants to get as much utility as she can, she should weigh different imaginary worlds in which her decision procedure has different logical outputs".

### 5.3 Where my own assumptions enter

The source supplies the equation and a body of worked cases. The following is not supplied by it.

- The detailed discipline of §3.3 for building $G$. The source says only that the structure must be an input.
- My explicit structural-equation reading of $do(F_x=a)$ in §2.2.
- The reading of "$\mathrm{Obs}=\textit{full}$" in the transparent formula (§2.3).
- The interpretation of "A-" as "action". The source's own footnotes name the policy version as the authors' preference, say that the difference "only matters in multi-agent dilemmas so far as we can tell", and leave it unexplored. I would add one sensible expectation: in a problem where the *same* agent faces several correlated choice points, intervening on a whole policy rather than one action-at-an-observation could matter. Neither the source nor I have worked this out.
- The Parfit calculation in §4.3, which is mine and relies on a simplified model.

## 6. Limits and open questions

1. **Learning $G$.** There is no theory of how to infer subjunctive structure. Different reasonable graphs for the same story can give different verdicts, and the output of A-FDT is only as reliable as the input.
2. **Counterpossible semantics.** Equation (4) avoids defining $\mathtt{true}(\cdot)$ by passing structure in, but it does not tell us why the structure is what it is. The source's footnote 9 mentions a hoped-for "evidential version" that would condition on false logical sentences. No definition of such conditionals exists.
3. **Fairness.** Without a formal criterion, the claim "A-FDT does well on all fair problems" cannot be tested systematically. Footnote 15 notes an obstacle: if I punish anyone who takes the same action as a copy of her, she "will always lose at this game, whereas Carl and Eve might win".
4. **Bounded agents.** The source's calculations use "the simplest possible world-models that accurately capture a given dilemma". It expects approximations of the theory to preserve the same qualitative behavior but gives no proof.
5. **Optimality.** The authors write that they "do not yet know whether FDT is optimal among decision theories, or even (on a formal level) what optimality consists in."

## 7. Conclusion

A-FDT is a small modification of CDT with large effects. Equation (4) keeps the expected-utility form and Pearl's intervention operator, but moves the intervention from the physical act to the node representing the output of the agent's own decision function, and moves the response to observation from conditioning to the choice of which node to intervene on. Everything that subjunctively depends on that output then varies in the hypothetical, including predictors, twins, copies of the agent, and even what the agent sees. Everything else, including lesions, termites and coincidences, is held fixed.

The result is a single rule that one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays in Parfit's hitchhiker, refuses mechanical and XOR blackmail, and stays in Damascus. The price is that the rule needs a graph of subjunctive dependence that nobody yet knows how to derive from first principles. I have suggested a practical discipline for drawing it. The theory's real work is done by that graph, so to apply A-FDT in a new case you must first decide, case by case and with explicit reasons, which processes in the world are computing what you are computing.