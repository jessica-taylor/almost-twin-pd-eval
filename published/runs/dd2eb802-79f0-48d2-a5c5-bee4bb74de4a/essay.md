# A-FDT: Choosing as the Output of One's Own Decision Function

## 1. The question A-FDT asks

When an agent deliberates, standard decision theory says she should compare her options by how well they turn out. That leaves open a prior question: what exactly is being varied when she imagines taking a different option?

- **Evidential decision theory (EDT)** varies the *news*. It asks which act would be the best thing to learn she had done.
- **Causal decision theory (CDT)** varies the *physical act*. It intervenes on her body's behaviour and propagates the change causally downstream.

Yudkowsky and Soares, in "Functional Decision Theory: A New Theory of Instrumental Rationality," propose a third answer. The agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

This essay concerns the version formalized as **Equation (4), Section 5** of that paper. The rule chooses an *action* by intervening on a node representing the decision function's output on the agent's actual inputs. Here I call it **A-FDT** (action functional decision theory). The name marks a contrast the authors draw in footnotes 7 and 16. Their "preferred formalization" intervenes instead on a *policy*, a map from observations to actions. They say this difference "will not make a difference in this paper" but may matter in multi-agent dilemmas. I will call that variant **policy-FDT**. Its formal statement is not given in the source.

Throughout, I separate three things:

1. what the paper says;
2. what follows from its equations;
3. what I add as operational assumptions, which I flag explicitly.

## 2. The common expected-utility frame

All three theories, the paper says, maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}$$

In this formula:

- $a$ ranges over a finite action set $\mathcal A$;
- $x$ is the observation history;
- $o_j$ are outcomes;
- $\hookrightarrow$ is the "connective for decision hypotheticals."

Following Joyce's representation theorem, the authors treat the interpretation of $\hookrightarrow$ as the free parameter. In Joyce's words, which the paper quotes, rival theories disagree "about the epistemic perspective from which actions are to be evaluated." The three theories fill in the parameter as follows:

$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a) \tag{2}$$

$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x) \tag{3}$$

$$\text{A-FDT}(P,G,x)=\arg\max_a \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big) \tag{4}$$

Here $V=\mathcal U(\textsc{Outcome})$, $P$ is a probability distribution, and $G$ is a graph. The underlines denote dequoting. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a *variable in the agent's model* whose name refers to the output of the A-FDT procedure itself, run on these very inputs. The authors note that this self-reference is harmless. The agent need not know the variable's value in order to represent it, and Kleene's recursion theorem ("quining") shows how such self-representing structures can be built.

## 3. What the equation actually does

Equation (4) differs from (3) in exactly two ways, both stated in the paper.

**(i) The point of intervention.** CDT intervenes on $\textsc{Act}$, a physical fact about the agent's body. A-FDT intervenes on a logical fact: what a particular function returns on a particular input. Anything that subjunctively depends on that function changes along with the intervention. This includes:

- the agent's own act;
- a predictor's simulation of her;
- a twin running the same reasoning.

**(ii) The treatment of observation.** The authors write: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Observing $y$ rather than $x$ moves the intervention from $\textsc{fdt}(\ldots,\underline x)$ to $\textsc{fdt}(\ldots,\underline y)$. The model is not conditioned on $\textsc{Obs}=x$.

This second difference produces A-FDT's most striking verdicts. In a hypothetical where the function outputs something different, the agent may have *received a different observation*. The paper puts it this way: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

### Subjunctive dependence

The graph $G$ must encode which variables change when the function's output changes. The paper calls this relation *subjunctive dependence*. Two physical systems computing the same function both depend subjunctively on that function, much like two working calculators computing $6288+1048$. The relation has two boundary features:

- **Causal dependence is a special case.** A scribe copying a calculator's output would write something else if the output differed.
- **Mere correlation is excluded.** Two calculators that happen to be pink do not depend on each other's colour.

The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

### The procedure in steps

In practice, A-FDT works like this:

1. **Build the model.** Construct a model $(P,G)$ containing:
   - physical variables;
   - a logical node $F_x \equiv \textsc{fdt}(\underline P,\underline G,\underline x)$ for the actual input;
   - where relevant, nodes $F_y$ for counterfactual inputs $y$.
2. **Draw the edges.** Draw an edge from $F_x$ to every variable whose value is computed from (or is a reliable representation of) the function's output on $x$. This includes the act, predictors' predictions, and twins' acts.
3. **Evaluate each action.** For each $a$, set $F_x=a$ by Pearl surgery: leave non-descendants at their prior distribution and recompute descendants.
4. **Score.** Compute $\mathbb E[V]$ in each surgically modified model.
5. **Choose.** Output the maximizing $a$.

### When the theories agree

When every correlation between the act and other variables is caused by the act, the paper notes that

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(F=a)],$$

so EDT, CDT and A-FDT all agree. Disagreement requires something other than the act itself to track the act: predictors, twins, copies, or merely statistical correlates.

## 4. Worked examples

All payoffs are in dollars treated as utility, following the paper.

### 4.1 Newcomb's problem

The setup:

- The predictor is 99% accurate.
- Box A holds \$1,000.
- Box B holds \$1,000,000 if one-boxing was predicted, and nothing otherwise.

In Fiona's graph, $F$ points to both $\textsc{Act}$ and $\textsc{Prediction}$, and $\textsc{Accurate}$ is an independent noise parent of the prediction. The two interventions give:

$$\mathbb E[V\mid \mathtt{do}(F=\textit{onebox})]=0.99(1{,}000{,}000)+0.01(0)=990{,}000,$$

$$\mathbb E[V\mid \mathtt{do}(F=\textit{twobox})]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.$$

A-FDT one-boxes. CDT holds $P(\textit{full})=p$ fixed under both interventions, so two-boxing gains \$1,000 whatever $p$ is, and CDT two-boxes.

A textual note: the paper reports EDT's one-boxing value as "\$999,000." The same arithmetic it uses for Fiona gives \$990,000. This is evidently a slip and does not affect any verdict.

A-FDT's reasoning involves no retrocausation. The paper insists Fiona "does not think that a physical signal passes between her action and the predictor's prediction." Her action and the prediction are simply two downstream effects of one logical fact.

### 4.2 Twin prisoner's dilemma

The setup is a prisoner's dilemma with these payoffs:

| Agent / Twin | Twin cooperates | Twin defects |
|---|---|---|
| **Agent cooperates** | 1,000,000 each | 0 to agent, 1,001,000 to twin |
| **Agent defects** | 1,001,000 to agent, 0 to twin | 1,000 each |

The twin runs the same function on the same input. So $F$ points to both players' acts. Intervening gives (C,C) worth 1,000,000 and (D,D) worth 1,000, and A-FDT cooperates.

The reasoning uses CDT-style surgery, not EDT-style news. The twin's act changes because it is a *descendant* of the intervened node, not because it is correlated evidence.

### 4.3 The smoking lesion

Here the lesion causes both a taste for smoking and cancer. Nothing in the world computes the agent's decision function, so no edge runs from her $F$ node to $\textsc{Cancer}$. Intervening on $F$ leaves $P(\textit{lesion})$ untouched, smoking adds \$1,000 utility, and A-FDT smokes.

The paper's full formalization is more elaborate. The lesion determines which of two utility functions ($\mathcal U_S$ or $\mathcal U_R$) and hence which of two decision-function nodes controls the act. The agent cannot tell which one she is. The result is that smoking beats refraining by $p\cdot 1{,}000$. The authors also argue the problem is "badly confused" and recommend abandoning it. The key point for applying A-FDT is simple: **a common cause that does not model the agent's reasoning gets no edge from $F$.**

### 4.4 Transparent Newcomb and Parfit's hitchhiker

This is where the observation-indexing matters. Both boxes are visible, and B is filled iff the predictor predicts one-boxing *upon seeing B full*. The model has two logical nodes:

- $F_{\text{full}}$, the output on seeing a full box;
- $F_{\text{empty}}$, the output on seeing an empty box.

The prediction depends on $F_{\text{full}}$, and the prediction determines which node controls the act. Seeing a full box, A-FDT intervenes on $F_{\text{full}}$ and does **not** condition on $\textsc{Obs}=\textit{full}$. Let $q$ be the prior probability that she two-boxes when facing an empty box. Then:

$$\textit{onebox}:\ 0.99(1{,}000{,}000)+0.01\cdot q\cdot 1{,}000 = 990{,}000+10q,$$

$$\textit{twobox}:\ 0.01(1{,}001{,}000)+0.99\cdot q\cdot 1{,}000 = 10{,}010+990q.$$

The paper misprints the second value as "\$110,00 + q·\$990." The ranking is unaffected. A-FDT leaves the \$1,000 even while looking at a full box.

Parfit's hitchhiker has the same structure: the driver rescues you iff she predicts you will pay once in the city. A-FDT pays. The paper defends both verdicts with three arguments:

- **From precommitment:** CDT and EDT agents would pay to bind themselves to this very act.
- **From value of information:** A-FDT never assigns information negative value.
- **From utility:** "Parfit's desert is stacked high with the corpses of such agents."

### 4.5 Blackmail

**Mechanical blackmail.** A perfect predictor runs a damaging program only if she predicts the agent will pay \$1,000 upon being notified. Holding the letter, A-FDT intervenes on $F_{\text{blackmail}}$. The two options compare as follows:

- *Pay:* she is almost surely blackmailed and loses \$1,000.
- *Refuse:* she is almost never blackmailed.

So she refuses. The answer shifts with predictor error. The paper's figures:

- With a 0.0009 chance of a mistaken prediction, refusing costs about \$900 in expectation versus \$1,000 for paying, so she still refuses.
- At an error rate of 0.011%, the paper reports that she pays. A careful reader should recompute such thresholds rather than trust the stated percentages. The rule is a comparison of $\epsilon\cdot 10^6$ against $10^3$, which reverses at $\epsilon=10^{-3}$.

**XOR blackmail.** The letter is sent iff exactly one of two conditions holds: no termites and the agent will pay, or termites and the agent won't. The termites are causally upstream of everything and not downstream of $F$. Intervening on $F_{\text{letter}}$ changes whether the letter arrives but not whether there are termites, so A-FDT refuses. EDT pays, because paying is good news about termites. This case shows A-FDT is not "EDT with a twist": it breaks merely evidential correlations just as CDT does.

### 4.6 Death in Damascus

Death predicts the agent perfectly and goes wherever she will be. In A-FDT's graph, $F$ points to both her location and Death's appointment book. Every intervention yields death, so the only difference is the \$1,000 cost of fleeing, and A-FDT stays.

CDT is unstable here. Whatever it expects to do, it prefers the other option. The paper argues CDT will even refuse to pay \$1 for a truly random coin that gives a genuine 50% survival chance, because its hypotheticals already credit it with at least 50% survival.

## 5. Dominance, fairness, and the global perspective

The paper denies that the dominance argument for two-boxing is neutral. "Every method for constructing hypotheticals gives rise to its own notion of dominance." Under A-FDT counterfactuals, which hold subjunctive dependencies fixed, switching to two-boxing makes you worse off. A-FDT never takes an action dominated in its own sense.

The authors propose judging theories by utility achieved in "fair" problems: problems where the outcome depends only on the agent's behaviour in the dilemma, not on which algorithm produced it. Newcomb's problem counts as fair: "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*." They admit fairness has not been formalized. Footnote 15 gives an example: a game that punishes anyone matching Fiona's copy is intuitively unfair, but it is unclear how to state that in general.

They also claim A-FDT is reflectively stable in fair problems. Holding the blackmail letter, Fiona has no wish to switch to CDT.

## 6. What the source leaves open, and how one might close it

### 6.1 Where does $G$ come from?

The paper is explicit. Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing." It calls this "perhaps the largest open problem."

A deeper idealization would be a $\mathtt{true}$ operator for counterpossible conditioning, which the paper does not know how to define. Equation (4) sidesteps the problem by taking the dependency structure as input, just as CDT takes causal structure as input.

**My operational proposal** is a rule of thumb for drawing edges from $F_x$:

> Draw an edge $F_x \to Z$ iff $Z$ is produced by a process that, within the agent's model, *computes or reliably represents* the agent's decision function on input $x$, with any unreliability modelled as an independent noise parent of $Z$.

This rule:

- reproduces every graph in the paper;
- separates predictors from lesions;
- makes partial reliability tractable: an imperfect predictor is $Z=f(F_x,N)$ with $N$ independent.

Its weakness is that "reliably represents" is not a crisp notion. Agents running *similar but not identical* functions are not settled by the source. The usual examples are a human opponent who partly reasons like you, or your future self on a slightly different input.

A natural extension, which is my own, is to let the edge carry a fidelity parameter $\rho$. The other agent copies $F$'s output with probability $\rho$ and otherwise draws from a fixed background distribution. The paper's gym example and its voting example (ten agents, where each votes because "the other members of the group will reason symmetrically") suggest the authors would treat sufficiently similar decisions as sharing a node. So they would effectively set $\rho \approx 1$ when the inputs differ in no relevant way.

### 6.2 Is $\textsc{Obs}=x$ conditioned on?

Equation (4) has no conditioning on observations. Yet the paper's transparent-Newcomb calculation writes $\mathbb E(V\mid \mathtt{do}(F_{\text{full}}=a), \textsc{Obs}=\textit{full})$. The numbers it actually computes are *unconditioned*: the two-boxing branch includes worlds where the box is empty. Conditioning would collapse A-FDT into two-boxing.

I therefore read Equation (4) literally. **Observations select the node; they are not conditioned on.** The paper's footnote on Timeless Decision Theory supports this reading. That theory "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful."

### 6.3 Priors on one's own off-path outputs

When A-FDT intervenes on $F_x$, the other nodes $F_y$ ($y\neq x$) are non-descendants. They keep their prior distribution, which is the $q$ in §4.4.

The paper notes that the "correct" values ($q=1$ in transparent Newcomb) do not affect the verdicts there. That is a fact about those examples, not a general theorem. A-FDT's verdict at $x$ can depend on beliefs about what it would do at other inputs. In principle this calls for a fixed point: the $F_y$ beliefs should match what A-FDT actually outputs at $y$.

### 6.4 A-FDT versus policy-FDT

This is where restricting attention to Equation (4) matters most. Here is an illustration of my own, not from the paper.

> **Coordination across inputs.** A predictor shows the agent either signal $x$ or signal $y$ (50/50, independent of everything). She pays \$100 iff the agent's dispositions are *both* "take L on $x$" and "take L on $y$", or *both* "take R on $x$" and "take R on $y$". She pays \$300 iff the dispositions are "R on $x$" and "R on $y$" (instead of \$100). The physical act itself is payoff-irrelevant.

Policy-FDT chooses the whole map at once and selects (R,R), worth \$300.

A-FDT, on seeing $x$, intervenes only on $F_x$ and holds its prior over $F_y$. Suppose that prior puts high probability on L, for instance because of how the agent has behaved before. Then setting $F_x=L$ looks better. Each observation-indexed node, optimized separately against stale beliefs about the others, can settle into a worse equilibrium (L,L).

If the agent's beliefs about $F_y$ are required to be accurate, then (R,R) is also a self-consistent outcome. So A-FDT under-determines the result where policy-FDT does not. This is presumably the phenomenon footnote 16 has in mind. The paper does not develop it.

**My recommendation for applying A-FDT** is to use Equation (4) as stated, but require the beliefs over off-path nodes $F_y$ to be a fixed point of A-FDT itself. Where several fixed points exist, the theory as written does not choose among them. Report that, and note that policy-FDT would select the best one.

### 6.5 Ties and degenerate priors

Equation (4) needs nothing like EDT's requirement that actions have nonzero probability, because $\mathtt{do}$ is defined even for interventions of prior probability zero. This is why A-FDT is not "at the mercy of its priors" over its own act, which the paper argues EDT is. The paper does not address ties. A fixed tie-breaking order is a harmless convention.

## 7. A checklist for unfamiliar cases

1. **List the variables:** world states, observations, other agents' acts, outcomes.
2. **Identify the inputs** $x$ on which your decision function might be evaluated, and create a node $F_x$ for each one that matters.
3. **Draw edges** from each $F_x$ to everything that computes or reliably represents it, including your own act when you observe $x$. Add noise parents for any unreliability.
4. **Leave pure statistical correlates unlinked**, such as lesions and coincidences, along with genuine upstream causes.
5. **Assign priors** to non-descendant nodes, including your off-path outputs, ideally at a fixed point.
6. **Do not condition on the actual observation.** For each $a$, compute $\mathbb E[V\mid \mathtt{do}(F_{x}=a)]$ for the observed $x$.
7. **Choose** the argmax. If the verdict hinges on off-path priors, flag it as a place where A-FDT and policy-FDT may part ways.

## 8. Conclusion

A-FDT keeps the expected-utility machinery shared by EDT and CDT, as well as CDT's surgical style of counterfactual. It changes only the *target* of the surgery, from the physical act to the output of the agent's own decision function on her actual input. Two consequences follow:

- Predictors, twins and copies move with the choice, so A-FDT one-boxes, cooperates with twins, pays the hitchhiker's driver, and refuses blackmail.
- Lesions and other upstream correlates do not move, so A-FDT smokes and refuses the XOR blackmailer.

Because observations select the intervention node instead of being conditioned on, A-FDT acts as it would have precommitted to act, without needing to precommit.

The theory's price, which the authors acknowledge, is that it takes a graph of logical dependencies as given. We lack both a theory of counterpossibles and a method for learning such graphs. Two further underspecifications, both mine to flag rather than the paper's, deserve the attention of anyone applying Equation (4):

1. the treatment of one's own off-path outputs;
2. the action/policy distinction.

With those caveats made explicit, A-FDT gives a precise, mechanical procedure.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2.