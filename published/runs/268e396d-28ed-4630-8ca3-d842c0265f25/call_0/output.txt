# A-FDT: Choosing the Output of a Fixed Function

## 1. The idea in one paragraph

Yudkowsky and Soares's paper "Functional Decision Theory: A New Theory of Instrumental Rationality" presents functional decision theory as a family of ideas, with several formalizations. This essay explains the one given by **Equation (4), Section 5**, which I call **A-FDT** (action functional decision theory). In A-FDT the agent treats her decision as the output of a fixed mathematical function, and she asks the question the abstract puts this way: "Which output of this very function would yield the best outcome?" She answers it by computing expected utility in hypothetical scenarios. In each scenario, the *logical output* of her own decision procedure is set to a candidate action, and everything that depends on that output, subjunctively or causally, changes with it. Everything else is held fixed.

I use "A-FDT" only for the Equation (4) procedure, in which the thing selected is an *action* given the agent's actual observations. The paper's footnotes 7 and 16 say its authors' "preferred formalization" has the agent iterate over *policies* (maps from observations to actions) instead. I call that variant policy-FDT where I need to refer to it. I flag below where the distinction matters.

I try throughout to separate three kinds of claims: what the source says, what follows from it, and what I am proposing as an operational gloss.

## 2. The shared expected-utility skeleton

The paper's Equation (1) says EDT, CDT and FDT all maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $P(a\hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Citing Joyce's representation theorem, the source stresses that the theories do not disagree about value. They disagree about "the epistemic perspective from which actions are to be evaluated," that is, about how to read the hypothetical connective $\hookrightarrow$.

The source then describes a general procedure. The agent keeps a world-model $M$. For each action $a$ she builds a *hypothetical* $M^{a\hookrightarrow}$ from $M$ and computes a value $V_a$ from it. She takes the action with the largest $V_a$. Hypotheticals are "decision-theoretic instruments constructed from beliefs," comparable to "notes on scratch paper." They are not beliefs and not mind-independent possible worlds. EDT builds them by conditioning, and CDT by Pearl's $\mathtt{do}$ on the physical action node. A-FDT builds them by $\mathtt{do}$ on a logical node.

## 3. Equation (4)

The A-FDT input is a pair $(P, G)$ together with the observation $x$. $P$ is a probability distribution over variables that include the outputs of mathematical functions, such as a variable for $6288+1048$ with most of its mass on $7336$. $G$ is a graph saying how changing a logical variable propagates to the other variables. The source requires this structure "to be given as an input," just as CDT takes causal structure as input. Equation (4) reads

$$\mathrm{A\text{-}FDT}(P,G,x) \;:=\; \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\Big(\mathcal V \;\Big|\; \mathtt{do}\big(\mathsf{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $\mathcal V=\mathcal U(\textsc{Outcome})$. The underlines denote dequoting, so $\mathsf{fdt}(\underline P,\underline G,\underline x)$ is a *variable in the model* that stands for the output of the A-FDT procedure run on exactly those inputs. The self-reference is harmless. The agent does not need to know the value of $\mathrm{A\text{-}FDT}(P,G,x)$ to have a variable representing it, and Kleene's second recursion theorem ("quining") shows how a structure can contain an accurate representation of itself.

The source names two differences from CDT's Equation (3).

1. **Where the surgery happens.** CDT intervenes on $\textsc{Act}$, a physical fact about the agent's body. A-FDT intervenes on $\mathsf{fdt}(P,G,x)$, a logical fact about her decision function. Anything downstream of that node in $G$ moves, including her body's behavior, any predictor's prediction, and any twin's choice.
2. **How observation enters.** CDT conditions on $\textsc{Obs}=x$. A-FDT never conditions on the observation. In the source's words it responds to observation "by changing which node it intervenes upon." Seeing $y$ instead of $x$ means intervening on $\mathsf{fdt}(\underline P,\underline G,\underline y)$.

The second point has a consequence worth stating plainly. A-FDT is *updateless* in the footnote's sense. Observation does not shrink the set of scenarios under consideration. The hypotheticals can include scenarios in which she observed something else, because the observed value is itself downstream of the node being set.

### Why this is a legitimate expected-utility rule

Joyce's theorem constrains how preferences over prospects and beliefs fit together, and it leaves the choice of hypothetical-forming constraints free. A-FDT supplies one such choice. Its hypotheticals must respect logical constraints in addition to the causal ones CDT respects. The source's agreement claim follows: if every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (with the possible exception of $\mathsf{fdt}$ itself),

$$\mathbb E[\mathcal V\mid a]=\mathbb E[\mathcal V\mid \mathtt{do}(a)]=\mathbb E[\mathcal V\mid\mathtt{do}(\mathsf{fdt}=a)],$$

and the three theories coincide. They come apart only when something correlates with the action without being caused by it, as when another agent models or copies the decision procedure.

## 4. Subjunctive dependence: what $G$ must encode

The source introduces *subjunctive dependence* to name the relation that A-FDT's graph is supposed to track. Its slogan is "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

- **Two systems computing the same function.** Two calculators computing $6288+1048$ cannot disagree, apart from malfunction. If one displays $7336$, you can infer the other will. A predictor who models the agent accurately is in this relation to her, and in the source's phrase the agent has "a 'twin' inside the predictor's mind." Imperfect models give a weakened but nonzero dependence.
- **Causation is a special case.** A scribe copying a calculator's output depends on it subjunctively, because had the output differed, so would the scribe's note.
- **Statistical correlation is not enough.** If the Paris calculator and the Tokyo calculator happen to both be pink, there is no subjunctive dependence between the colors. Had the scribe bought a green calculator, Tokyo's would still be pink.

The test the source uses is a counterfactual one: *if this computation had output something else, would that thing have been different?* The only commitment A-FDT needs is stated plainly: "when an FDT agent imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

The source does not say how to *derive* such a graph from observation and experiment, and calls this "perhaps the largest open problem in the study of functional decision theory." Pearl gives a theory of how to learn causal structure, and nothing comparable exists for subjunctive structure. So anyone applying A-FDT must supply $G$ from an understanding of the problem.

**My operational heuristics** (not from the source, but consistent with its worked examples):

1. Put a node $\mathsf{fdt}(P,G,x)$ for each observation the agent might receive. These nodes are the candidate intervention points.
2. Add an edge from an $\mathsf{fdt}$ node to each system that *implements or models* the procedure. These are the agent's own body (so $\textsc{Act}$ is a function of the $\mathsf{fdt}$ nodes), predictors who simulate her, and copies of her.
3. Do not add an edge to a variable that merely shares a common cause with her action. In the smoking lesion, the lesion causes the agent's preferences, and so influences which procedure runs, but it does not evaluate her output.
4. Represent imperfect prediction as an explicit stochastic node (the source's $\textsc{Accurate}$) feeding the predictor's output.
5. Where an observation is itself determined by a prediction, make the prediction select which $\mathsf{fdt}$ node controls $\textsc{Act}$. The source does this in the transparent Newcomb and blackmail graphs.

## 5. Worked examples

The numbers below come from the source, except where I say I recomputed them.

### 5.1 Newcomb's problem (and the twin prisoner's dilemma)

Take Fiona's graph with the node $\mathsf{fdt}(P,G)$ pointing to both $\textsc{Act}$ and $\textsc{Prediction}$, a stochastic $\textsc{Accurate}$ node (99%) feeding $\textsc{Prediction}$, and $\textsc{Box B}$ determined by $\textsc{Prediction}$. Then:

- $\mathtt{do}(\mathsf{fdt}=\textit{onebox})$: she one-boxes, and box B is full with probability 0.99. Expected value is $0.99\times\$1{,}000{,}000=\$990{,}000$.
- $\mathtt{do}(\mathsf{fdt}=\textit{twobox})$: she two-boxes, and box B is full with probability 0.01. Expected value is $0.01(\$1{,}001{,}000)+0.99(\$1{,}000)=\$11{,}000$.

So A-FDT one-boxes. (The source's text gives EDT's one-boxing value as \$999,000, but conditioning on one-boxing with the same 0.99 reliability also gives \$990,000. The ranking is unaffected.) The twin prisoner's dilemma is the same calculation. Setting the shared function's output to *cooperate* sets the twin's move too, giving \$1,000,000 against \$1,000 for *defect*.

No retrocausation is involved. A-FDT agrees with the physicist that nothing travels backward in time. She simply declines to imagine her action differing without the output of the function that the predictor modeled differing too.

The source also answers a natural objection: "Even if she is quite sure that the box is full ... when you ask her what *would happen if* she two-boxed, she says that, for her to two-box, the FDT algorithm would have to output *twobox*." Her confidence about the actual contents is a belief, and her hypotheticals are a separate instrument.

Contrast CDT. Its $\mathtt{do}(\textsc{Act})$ cuts the edge between action and prediction, so with box-full probability $p$ the value of two-boxing is always \$1,000 higher. EDT conditions on the action and so respects the (real) correlation, but it also respects spurious correlations, as in the lesion case below.

### 5.2 Smoking lesion

Here the graph must differ from Newcomb's, which is why A-FDT is not just EDT with relabelled variables. The lesion causes cancer and also determines which procedure runs, but the cancer node is *not* downstream of $\mathsf{fdt}$. The source models the lesion as selecting between two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$ (a \$1 penalty for smoking), so that $\textsc{Act}$ is a function of $\textsc{Lesion}$, $\mathsf{fdt}(P_S,G)$ and $\mathsf{fdt}(P_R,G)$. Intervening on the relevant $\mathsf{fdt}$ node leaves $P(\textsc{Lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes. The source itself calls this formalization contrived and recommends philosophers abandon the problem, and I do not lean on it further. Its value is as a check that A-FDT separates predictor-like from lesion-like correlations by graph structure alone.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

Now the agent sees box B full. A-FDT intervenes on $\mathsf{fdt}(P,G,\textit{full})$ and does not condition on fullness. In the graph, $\textsc{Prediction}$ determines which of $\mathsf{fdt}(\cdot,\textit{full})$ or $\mathsf{fdt}(\cdot,\textit{empty})$ controls $\textsc{Act}$. Let $q$ be her prior that she two-boxes upon seeing an empty box. (I rederived the following values.)

- Set output *onebox*: with probability 0.99 (accurate) the predictor expected one-boxing, the box is full, and she gets \$1,000,000. Otherwise the box is empty and she runs the *empty* branch, worth $1000q$. Total $\approx \$990{,}000+10q$.
- Set output *twobox*: with probability 0.99 the predictor expected two-boxing, so the box is empty, she never sees "full," and she earns about $1000q$. With probability 0.01 she gets \$1,001,000. Total $\approx \$10{,}010+990q$.

(The source prints this second total with a typographical slip.) For any $q\in[0,1]$ one-boxing wins, and she leaves the \$1,000 even while looking at a full box. Parfit's hitchhiker has the same structure, with the driver as predictor, so A-FDT pays in the city. In both cases she is evaluating "the kind of agent that makes such decisions," and in worlds where that kind of agent two-boxes she is mostly staring at an empty box or dying in the desert.

### 5.4 XOR blackmail

The letter is sent iff exactly one of the following holds: (no termites and she pays on receipt), or (termites and she does not pay). Let $p$ be the probability of termites, which no hypothetical alters. (This computation is mine, following the source's description.)

- $\mathtt{do}(\mathsf{fdt}(\textit{letter})=\textit{pay})$: the letter arrives only when there are no termites, so she pays \$1,000 in that case. Value $-10^6p-1000(1-p)$.
- $\mathtt{do}(\mathsf{fdt}(\textit{letter})=\textit{refuse})$: the letter arrives only when there are termites, and she pays nothing. Value $-10^6p$.

She refuses. EDT conditions on the action *given the letter*, which makes paying look like proof of a termite-free house, so it pays. A-FDT and CDT both refuse, but for different reasons. In CDT's hypothetical the letter is still sent, so the "perfect" predictor has erred. In A-FDT's hypothetical changing the output changes whether the letter is sent.

### 5.5 Mechanical blackmail, and a correction

If the blackmailer is a perfect predictor, then under $\mathtt{do}(\textit{pay})$ she is always blackmailed and always loses \$1,000. Under $\mathtt{do}(\textit{refuse})$ she is never blackmailed. A-FDT refuses even while holding the letter. If the blackmailer errs with probability $\varepsilon$ in the direction of blackmailing a refuser, refusing costs $\varepsilon\cdot\$1{,}000{,}000$ in expectation and paying costs \$1,000. The break-even point is therefore $\varepsilon=0.001$, and A-FDT refuses iff $\varepsilon<0.1\%$.

The source's first example ($\varepsilon=0.0009$, loss \$900) fits this. Its second example says that at an error rate of "0.011%" she pays. That figure gives an expected loss of \$110, below \$1,000, so refusing would still win. I take it to be a slip for 0.11% (loss \$1,100), and the threshold derivation above is what I would trust.

## 6. Where the source leaves things open, and what I propose

**(a) What is the intervention, formally?** The source gives the abstract $\mathtt{true}(\cdot)$ operator for counterlogical conditioning and says "it's not clear how to define" it. It sidesteps this by assuming $G$ is given and reusing Pearl's $\mathtt{do}$. So A-FDT is well defined as a *function of* $(P,G,x)$ and not as a free-standing theory. The paper's footnote 9 mentions that an evidential version, conditioning on false logical sentences, would need a probability over counterpossibles that no one yet has. The paper also argues, plausibly but without proof, that agents "do not need to evaluate counterpossibilities in full generality," only questions like how a predictor's output would change.

**(b) Observations in the transparent case.** The source's displayed formula for transparent Newcomb attaches "$\textsc{Obs}=\textit{full}$" to the do-expression, but the surrounding calculation and text clearly evaluate hypotheticals in which she sees an empty box. That matches Equation (4), which has no $\textsc{Obs}$ conditioning. I follow Equation (4) and the calculation.

**(c) Action versus policy.** Equation (4) intervenes on one node at a time, namely the node for the observation actually received, and treats the agent's outputs at other observations as given by $P$. That is why the examples need priors such as $q$. For the problems in the source this does not matter, since the answer is the same for every $q$, and the source itself says the difference "only matters in multi-agent dilemmas so far as we can tell." But as a matter of the formalism, A-FDT's recommendation could in principle depend on $P$'s beliefs about her behavior elsewhere.

My proposal, which is not in the source, is to require $P$ to be *self-consistent*. Her credence in each $\mathsf{fdt}(P,G,x')$ should equal what A-FDT would actually output there. Where the dependency order is acyclic, as in transparent Newcomb where the empty-box decision does not depend on the full-box decision, compute the later branches first. Where it is cyclic, I would fall back on the policy variant, which optimizes all branches jointly. This is an additional assumption and should be labelled as such.

**(d) Fairness.** The source claims A-FDT does best in "fair problems," where the agent's beliefs are accurate and outcomes depend only on her behavior in the problem at hand, and it admits it has no formal definition of fairness. Its footnote 15 observes that a problem punishing "act the same as a copy of Fiona" is unfair to Fiona in a way that does not transfer to Carl. So the optimality claim is a conjecture the authors have not found a counterexample to. They do not prove it.

**(e) Logical uncertainty.** For the model to contain a variable for the output of the very procedure being run, the agent must be uncertain about a logical fact while computing it. The source points to the logical-uncertainty literature and to the existence of human reasoners who cope. This is a technical gap, and the source argues it is not a philosophical objection.

## 7. Motivation, objections, and the "global perspective"

The case for A-FDT in the source is mainly a utility argument. Agents who follow A-FDT predictably end up richer in fair Newcomb-like problems, so "it would be great news to hear that a beloved daughter adheres to FDT." The precommitment argument is a corollary: A-FDT "always act[s] as they would have precommitted to act," so it needs no costly binding mechanisms. The source also argues that A-FDT never assigns negative value to information, unlike EDT, because it always acts as it would have precommitted to act.

On dominance, the source argues that dominance is relative to a method of building hypotheticals. Two-boxing dominates under CDT's counterfactuals, and refusing to smoke "dominates" under conditioning. Under A-FDT's own notion, which holds subjunctive dependencies fixed and switches the algorithm's output, A-FDT never takes a dominated action. The source concludes that dominance "doesn't afford us a neutral criterion."

Against the charge that she believes in controlling the past, the source offers a symmetry argument. A deterministic CDT agent also "imagines" worlds in which her token action differs. If controlling the type is suspect, so is controlling the token. A-FDT is described as choosing from a "global perspective": "What would the entire universe look like if the FDT algorithm behaved differently?"

I find one point worth adding about the structure of the argument. The source concedes that no decision theory wins on every possible problem, since one can always reward a particular procedure. So the claim has to be about problems that reward or punish *actions* and not procedures. The fairness caveat is then essential, because it limits where the utility argument has force. A reader should therefore treat "A-FDT outperforms CDT and EDT" as holding relative to a still-informal class of problems.

## 8. A recipe for unfamiliar cases

1. List the observation-dependent decision points, and give each a node $\mathsf{fdt}(P,G,x)$.
2. Identify every system whose behavior is determined by, or a model of, this computation. Draw edges from the $\mathsf{fdt}$ nodes to them. Include stochastic nodes for imperfect modeling.
3. Leave out variables that merely correlate with the action through a common cause.
4. Determine how observations arise. If they are downstream of an $\mathsf{fdt}$ node, as with predictions and letters, draw that edge.
5. For each candidate action $a$, set the actual-observation node to $a$ using $\mathtt{do}$, and propagate. Do not condition on the observation.
6. Compute $\mathbb E[\mathcal V]$, using self-consistent beliefs about the other branches (my proposal), and take the argmax.

If every correlation of the action is causal, step 5 reduces to ordinary expected utility, and A-FDT agrees with CDT and EDT.

## 9. Conclusion

A-FDT is a small modification of CDT with large consequences. It intervenes on a logical node standing for the output of the agent's own decision function. It responds to observations by switching the intervention point and not by conditioning. Given a graph encoding subjunctive dependence, it yields a concrete procedure that one-boxes in Newcomb, pays in Parfit's hitchhiker, refuses XOR and mechanical blackmail, and cooperates with a twin. What the procedure leaves open is also substantial. We lack a way to learn subjunctive structure from experience and a satisfactory account of counterpossibles. The role of beliefs about one's own other-branch outputs is underspecified, and "fair problem" is still informal. A reader who adopts A-FDT should regard Equation (4) as a rigorous *conditional* statement ("given the right graph, here is the action"), and should treat the construction of the graph as the place where judgment, and any remaining disagreement, lives.

**Sources.** Yudkowsky & Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality" (arXiv:1710.05060), the primary source throughout. Cited therein and used here: Joyce, *The Foundations of Causal Decision Theory* (1999); Pearl, *Causality* (2000); Gibbard & Harper (1978).