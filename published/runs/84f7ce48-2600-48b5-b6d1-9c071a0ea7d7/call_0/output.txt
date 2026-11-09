# A-FDT: Choosing by Intervening on a Decision Function

## 1. The idea in one paragraph

A-FDT (action functional decision theory) is an expected-utility theory in which the agent evaluates each available action by asking what the world would look like *if the output of her own decision function were that action*. It does not ask what would happen if her body made a different movement while the rest of the world stayed fixed. The source paper (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") states the guiding principle as treating one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" I take Equation (4) of Section 5 as the formal definition. The paper calls the resulting theory FDT. I call it A-FDT throughout, because Equation (4) selects *actions*, whereas the paper's footnotes say its authors' "preferred formalization" selects *policies*. I return to that distinction in Section 6.

I try to mark what is the paper's claim and what is my own gloss. My own proposals are flagged "(my addition)".

## 2. Setting: expected utility with a choice of "hypotheticals"

The paper's Equation (1) writes expected utility as

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j),$$

where $P(a\hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$". Following Joyce, the paper holds that EDT, CDT and A-FDT agree on this form and differ only on how to read the connective $\hookrightarrow$, which is the "epistemic perspective" from which actions are evaluated.

Operationally, the agent holds a world-model $M$. For each action $a$ she builds a *hypothetical* $M^{a\hookrightarrow}$, a transient computational object like "notes on scratch paper". She computes the expected utility $V_a$ in it and takes the maximizer. The three theories differ in what $M$ contains and how the hypotheticals are built:

- **EDT** (Eq. 2): $M = P$, and the hypothetical conditions on the action: $\arg\max_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$.
- **CDT** (Eq. 3): $M=(P,G)$ with $G$ a causal graph, and the hypothetical applies Pearl's operator: $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$.
- **A-FDT** (Eq. 4): $M=(P,G)$ with $G$ a graph of *subjunctive* dependencies, and the hypothetical intervenes on a logical variable.

## 3. Equation (4)

$$\mathrm{A\text{-}FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\; \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

**Reading the symbols.** $P$ is a probability distribution over variables of the agent's model. These include ordinary variables, and also variables for the outputs of mathematical functions, such as a variable for $6288+1048$ with most of its mass on $7336$. $G$ is a graph "that tells us how changing a logical variable affects all other variables". $x$ is the observation history. The underlines denote dequoting: $\mathrm{fdt}(\underline P,\underline G,\underline x)$ names the variable that represents the output of this very procedure when run on the inputs $P, G, x$.

**Self-reference.** The model contains a variable whose name depends on the model. The paper calls this harmless: the agent need not know the *value* of $\mathrm{A\text{-}FDT}(P,G,x)$ to have a variable *representing* it, and Kleene's second recursion theorem ("quining") shows how a data structure can contain an accurate representation of itself. Footnote 12 adds a warning: the variable $\mathrm{fdt}(\underline P,\underline G)$ is not the same as the action $\mathrm{A\text{-}FDT}(P,G)$ that the procedure returns.

**Two differences from CDT** (the paper's own summary):

1. CDT intervenes on a node $\mathrm{Act}$ for the *physical* action. A-FDT intervenes on a node for the output of its *decision procedure*.
2. CDT responds to observation by Bayesian conditioning: it replaces $\mathrm{Obs}=x$ with $\mathrm{Obs}=y$. A-FDT responds to observation by *changing which node it intervenes on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

The second difference does a great deal of work. An A-FDT agent holding an observation does not treat that observation as a fixed background fact that every hypothetical must respect. Her hypotheticals may contain worlds in which she observed something else. The reason is that the predictor, blackmailer or twin responds to the function's output on the *whole* input space, and the intervention on a different output changes which observation her counterpart ends up generating.

**Where A-FDT collapses to the others.** The paper notes that when all correlations between $\mathrm{Act}$ and other variables are caused by $\mathrm{Act}$, the three equations agree:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G)=a)].$$

They come apart only when something correlates with the action without being caused by it. That is the situation with predictors, twins and copies.

## 4. Subjunctive dependence and the graph $G$

The graph in Equation (4) encodes *subjunctive dependence*. The paper's motto is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Two physical systems computing the same function subjunctively depend on that function. If two calculators compute $6288+1048$ and one displays $7336$, you may infer the other does too. A scribe copying one calculator's display depends on it both causally and subjunctively, so causal dependence is a special case. Mere statistical correlation, such as two calculators both happening to be pink, is not subjunctive dependence. Had the Paris calculator been green, the Tokyo one would still be pink.

So the rule for hypotheticals is this. When A-FDT imagines the output changing, the things that change with it are "all and only those things that subjunctively depend on the output of her decision-making procedure," and everything else is held fixed. In the paper's phrase, where CDT's hypotheticals respect too few action–environment correlations and EDT's too many, A-FDT "preserve[s] all decision-relevant subjunctive dependencies."

**What the paper does not supply.** It says plainly that Equation (4) "rests on shakier philosophical foundations" than CDT's. There is no analogue of Pearl's account for inferring the structure of subjunctive dependence from observation. The paper requires "that the relevant logical dependency structure be given as an input to FDT, in the same way that the relevant causal structure is given as an input to CDT," and calls deducing it "perhaps the largest open problem." It also notes that the evaluation requires counterpossible reasoning, since an output that is in fact $a_1$ is imagined to be $a_2$. Its response is that the difficulty is technical rather than philosophical, and that humans manage such reasoning with heuristics.

**An operational interpretation (my addition).** A practitioner who must write down $G$ can proceed as follows.

1. *Locate the computation.* Identify the decision procedure and the inputs it receives in each branch of the problem. For each possible observation $x$, create a node $\mathrm{fdt}(\underline P,\underline G,\underline x)$. Only one of these is "live" in the agent's actual situation, but the others may feed into the model.
2. *Find the copies.* Ask of each variable in the scenario: is it produced by running (or accurately modelling) this procedure? Predictions, twins' choices and your future selves in identical circumstances are candidates. Give these nodes an arrow from the relevant $\mathrm{fdt}$ node.
3. *Model imperfection.* For an imperfect predictor, add a noise variable, as the paper does with $\mathrm{Accurate}$. The prediction node then equals the $\mathrm{fdt}$ output when the noise is benign and is otherwise independent of or flipped from it.
4. *Exclude mere correlates.* A variable correlated with your action because of a common cause, such as the smoking lesion, receives no arrow from $\mathrm{fdt}$. Test it by asking whether the variable would differ if this function returned a different output. The lesion would not, since it does not model you.
5. *Evaluate.* Intervene on each value of the $\mathrm{fdt}$ node, propagate, compute $\mathbb E[V]$, and take the argmax.

Steps 2 and 4 are where the unresolved theory lives. The procedure is only as good as the dependency judgments, and the paper offers no algorithm for them beyond the guiding test.

## 5. Worked examples

All numbers use the paper's dollar-utilities.

### 5.1 Newcomb's problem

The graph has a node $\mathrm{fdt}$ with arrows to $\mathrm{Act}$ and to $\mathrm{Prediction}$. $\mathrm{Prediction}$ also depends on $\mathrm{Accurate}$ (probability 0.99), and $\mathrm{Prediction}$ determines $\mathrm{Box\,B}$.

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$: $\Pr(\text{full})=0.99$, so $\mathbb E[V]=0.99\times 1{,}000{,}000=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$: $\Pr(\text{full})=0.01$, so $\mathbb E[V]=0.01\times1{,}001{,}000+0.99\times1{,}000=\$11{,}000$.

A-FDT one-boxes. The paper stresses that this involves no retrocausation. The agent believes no signal passes from her action to the past. She only declines to imagine her action changing while "the FDT algorithm" and its accurate model inside the predictor stay fixed.

A natural objection is: "If Fiona is nearly sure the box is full, won't she reconsider and take both?" The paper answers that her way of weighing options is exactly what blocks this. To ask what would happen if she two-boxed is to ask what would happen if the function returned *twobox* on this very input, and the box would then probably be empty.

### 5.2 Smoking lesion

Here the lesion is a common cause of the urge to smoke and of cancer. The cancer node therefore gets no arrow from the $\mathrm{fdt}$ node, which makes the graph differ from Newcomb's even though the probability tables look alike. The paper formalizes the lesion as altering the agent's utility function ($\mathcal U_S$ versus $\mathcal U_R$, differing by \$1 in the value of smoking), so the agent does not know which of two decision functions she is running. Intervening on the one corresponding to $\mathcal U_S$, with $p=\Pr(\text{lesion})$ unchanged by the intervention, smoking is better than refraining by exactly $p\cdot\$1{,}000$. The same criterion yields one-boxing and smoking. EDT and CDT would require different graph-free tables to do the same. This is the paper's headline claim for a single rule. The paper also calls the smoking lesion problem "badly confused" and recommends dropping it, so I treat it as a consistency check rather than a deep test.

### 5.3 Transparent Newcomb and observation-dependence

Now the agent sees the box. Her graph has nodes $\mathrm{fdt}(\ldots,\text{full})$ and $\mathrm{fdt}(\ldots,\text{empty})$. $\mathrm{Prediction}$ determines which of the two governs $\mathrm{Act}$, "[t]his represents the fact that the predictor's prediction determines which observation the agent receives." Suppose she sees a full box. She intervenes on the *full* node. Let $q$ be her credence that she two-boxes on seeing an empty box.

- Intervene $\text{onebox}$: with probability 0.99 the prediction is "one-box", the box is full and she gets \$1,000,000. Otherwise she sees an empty box and her other node acts, giving $0.01\,q\cdot\$1{,}000$ in expectation. Total: $\$990{,}000+10q$.
- Intervene $\text{twobox}$: with probability 0.99 the prediction is "two-box", so she would see an empty box and act on the other node, giving $0.99\,q\cdot\$1{,}000=990q$. With probability 0.01 the predictor errs, she sees a full box and takes both, giving $\$1{,}001{,}000$. Total: $\$10{,}010+990q$.

For any $q\in[0,1]$ one-boxing wins by roughly \$980,000. (The paper's printed total for two-boxing reads "\$110,00 + q·\$990", which looks like a typesetting slip. The arithmetic gives \$10,010 + 990q.) Even with a full box in plain view, her hypothetical for two-boxing is a world in which she mostly *saw an empty box*. This is the computational content of "A-FDT does not condition on observations the way CDT and EDT do".

This is also the paper's argument that one-boxing here is equivalent to paying in Parfit's hitchhiker: the driver rescues the agent iff she predicts payment upon arrival.

### 5.4 Blackmail

*Mechanical blackmail.* The blackmailer runs the program iff she predicts the agent will pay. With a perfect predictor, intervening on $\mathrm{fdt}(\ldots,\text{blackmail})=\text{pay}$ makes blackmail near-certain and costs \$1,000. Intervening on $\text{refuse}$ makes blackmail near-impossible, so the agent expects to lose nothing. She refuses, even holding the letter, and is never sent it.

For an imperfect predictor with error rate $\varepsilon$ (probability of predicting "pay" for a refuser), paying costs \$1,000 for sure in the hypothetical, while refusing costs $\varepsilon\times\$1{,}000{,}000$. Refusal wins iff $\varepsilon<0.001$. The paper works the case $\varepsilon=0.0009$ (cost \$900, refuse). It then says that for an error chance of "0.011%" she pays. By the same arithmetic 0.011% would still be refusal territory (an expected cost of \$110), so I take that figure to be a slip for something above the 0.1% threshold, such as 1.1%.

*XOR blackmail.* The letter is sent iff exactly one of "no termites and you pay" or "termites and you don't pay" holds. Conditioning (EDT) makes paying look like good news that implies no termites. A-FDT holds the termite node fixed, since nothing about the infestation depends on the function's output, while the letter's *arrival* does depend on it. Refusing is therefore recommended, with a different rationale from CDT's: CDT refuses because its hypotheticals sever the predictor's accuracy; A-FDT refuses because in its hypotheticals refusal means the letter would rarely have been sent.

### 5.5 Death in Damascus

Death's book entry subjunctively depends on the agent's decision function. Every hypothetical for fleeing places Death in Aleppo, and every hypothetical for staying places him in Damascus. The only difference between options is then the \$1,000 camel fare, so A-FDT stays. CDT, by contrast, imagines Death's location fixed while the action varies, which yields the unstable "go where Death isn't expected" loop. The paper uses this to argue that CDT would even decline a \$1 truly random coin that gives a 50% chance of survival, which would be wildly irrational.

### 5.6 A graded twin dilemma (my addition)

To show how partial dependence enters, suppose the twin is a copy of the agent's function with probability $\rho$ and otherwise acts independently, cooperating with probability $c$. In the twin prisoner's dilemma with the paper's payoffs:

$$\mathbb E[V\mid \mathrm{do}(C)]-\mathbb E[V\mid \mathrm{do}(D)] = \rho\cdot 999{,}000-(1-\rho)\cdot1{,}000.$$

Cooperation wins iff $\rho>0.001$. The independent-branch term contributes the usual defect-dominates amount of \$1,000 and is independent of $c$. So A-FDT's cooperation does not require perfect twins; it requires only enough subjunctive dependence to outweigh the dominance premium. This simple model is not in the paper, but it shows how the graph's noise variable affects the recommendation.

## 6. Actions versus policies

Equation (4) intervenes on a node indexed by a single observation $x$, so it picks an action for the observation the agent actually has. Footnotes 7 and 16 say that the authors' "preferred formalization of FDT" instead intervenes on a node selecting a *policy*, a map from observations to actions, which the agent then applies to her input. They state that "[t]his makes a difference in certain multi-agent dilemmas" but do not make a difference in the paper, and "[t]he difference only matters in multi-agent dilemmas so far as we can tell." I treat this as unresolved by the source.

Two observations (mine) clarify the relationship. First, in the transparent Newcomb calculation the value of the action at $x=\text{full}$ depends on the agent's credence $q$ about her behavior at $x=\text{empty}$. The paper acknowledges that "[t]he correct value of $q$ is 1" but notes that the verdict is robust. In general, A-FDT therefore needs a consistent prior over its own outputs at other inputs, which in an ideal case coincides with what A-FDT would actually output there. A policy-selecting variant would instead choose all outputs jointly and so avoid this requirement. Second, whether the two differ outside the multi-agent cases is something I cannot establish from the paper. A practitioner can use Equation (4) as stated, with the $q$-style priors about her behavior at other inputs filled in by running the same procedure there.

## 7. How A-FDT treats counterfactuals, dominance and fairness

**Counterfactuals versus conditionals.** The paper stresses that conditionals are not counterfactuals. Given a choice between \$1 and \$100, the agent conditional on taking the \$1 probably had some reason, but if she counterfactually took the \$1 she would simply be poorer. EDT's conditioning makes it "manage the news". In the cosmic ray problem, an EDT agent who almost always takes \$1 treats taking \$100 as evidence of cosmic-ray damage and forgoes the \$100. A-FDT, like CDT, breaks merely statistical correlations. It differs from CDT in refusing to break correlations that follow from the function itself.

**The counterfactuals are not worlds.** The paper insists that hypotheticals are "mental or computational objects used as tools", not mind-independent possible worlds. Both CDT's and A-FDT's hypotheticals contain impossibilities. CDT agents imagine perfect predictors failing exactly when they act. A-FDT agents imagine observations differing from those they have. The paper's defense is parity: a deterministic CDT agent who "controls" her physical token faces the same metaphysical worry as an A-FDT agent who "controls" the function's type. The justification offered is practical, namely which method makes the agent richer.

**Dominance.** The CDT argument for two-boxing is that taking the extra \$1,000 is better whatever the box contains. The paper replies that this holds fixed the predictor's behavior while changing the agent's function, which is akin to "imagining a calculator outputting 3159 while holding constant the fact that 6288+1048=7336". Every method of constructing hypotheticals yields its own dominance notion, so none is neutral. Under A-FDT dominance (hold relevant subjunctive dependencies fixed), one-boxing is not dominated. The paper's preferred criterion is utility achieved.

**Fairness.** The paper separates problems that reward or punish *actions* (including predicted ones) from those that reward or punish *decision procedures as such*. Newcomb's predictor "punishes two-boxers", not CDT as a procedure. A problem in which a mind reader pays iff you follow a given theory is unfair, and no theory can win all of them. The paper claims A-FDT is at least as good as CDT and EDT on fair problems, and admits that it lacks a formal criterion of fairness. Footnote 15 gives a counterexample showing why the formalization is difficult: a copy of Fiona that punishes anyone who matches its action is "unfair to Fiona" in a way not mirrored for Carl.

## 8. Limits and an honest accounting

Things the paper claims: A-FDT agrees with CDT and EDT in simple settings; it one-boxes in Newcomb's problem, smokes in the lesion problem, pays in Parfit's hitchhiker, one-boxes in the transparent case, refuses both blackmails, stays in Damascus, and is "reflectively stable in fair problems"; and it is an expected-utility theory in Joyce's sense.

Things the paper leaves open, which I flag as requiring additional assumptions in any application:

- The construction of $G$ (how to know that a given node depends on the function's output).
- A $\mathtt{true}$ operator or counterpossible conditional (the paper explicitly sidesteps this by requiring $G$ as input).
- The action/policy question.
- Fairness, and hence the precise scope of the claim that A-FDT is never beaten.
- Approximation: the paper's idealized models are small, and it only conjectures that bounded versions would show similar strengths and weaknesses.

Also, the paper's verdicts are computed on hand-built graphs. A critic can reasonably say that the right answer comes from the graph the theorist chooses. A-FDT cannot settle disagreements about dependency structure, and my five-step procedure only organizes the judgment rather than eliminating it.

## 9. Conclusion

A-FDT replaces CDT's question "what would my act cause?" with "what would the world be like if this very decision function returned $a$ on this input?" It does so with one change to Pearl's machinery: intervene on a logical node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ in a graph encoding subjunctive dependence, and let observation change the node of intervention instead of the conditioning event. The result agrees with the standard theories when dependence is causal, and diverges exactly in the presence of predictors, twins and copies, where it earns more utility than either rival on the paper's examples. The price is that the dependency graph must be supplied, since there is no general theory of how to derive it, and the verdicts are only as reliable as that input. Within that limitation, Equation (4) gives a concrete, checkable procedure that a careful reader can apply to new cases.