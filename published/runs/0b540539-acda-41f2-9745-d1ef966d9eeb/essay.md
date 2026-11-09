# A-FDT: Choosing the Output of Your Own Decision Function

## 1. The idea in one paragraph

Yudkowsky and Soares's paper "Functional Decision Theory: A New Theory of Instrumental Rationality" gives a decision rule that this essay calls **A-FDT** (the paper calls it FDT). Its central claim is that the agent should treat her decision as the output of a fixed mathematical function and ask, in the paper's words, "Which output of this very function would yield the best outcome?" That differs from the question causal decision theory (CDT) asks ("Which physical act of mine causes the best outcome?") and from the question evidential decision theory (EDT) asks ("Which physical act of mine would be the best news to hear I took?"). A-FDT is an expected-utility theory. It differs from CDT and EDT only in how it builds the hypothetical scenarios it scores. The paper's formal statement, Equation (4) of Section 5, is the primary object of this essay.

I will separate three kinds of claim: what the paper states, what follows from it by calculation, and what I add (marked **[Proposal]**). The paper itself says the most important input to the formula is not fully specified.

## 2. The formal definition

### 2.1 Common frame

All three theories maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $x$ is the observation history and "$\hookrightarrow$" is the connective for decision hypotheticals. Following Joyce's representation theorem, the paper treats the theories as disagreeing about the "epistemic perspective from which actions are to be evaluated", that is, about what "$\hookrightarrow$" means. In practice the agent holds a world-model $M$ and builds a hypothetical $M^{a\hookrightarrow}$ for each action. She computes a value $V_a$ from each hypothetical and takes the best action.

The two benchmarks are:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. Hypotheticals are Bayesian conditionalizations.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. The model is a pair $(P,G)$ with $G$ a causal graph. Pearl's $\mathrm{do}$ operator sets $\mathrm{Act}=a$, recomputes everything causally downstream, and leaves everything else untouched.

### 2.2 Equation (4)

$$\boxed{\;\mathrm{A\text{-}FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}$$

The ingredients are:

1. **$P$** is a probability distribution over variables. These include ordinary physical variables and variables for the outputs of mathematical functions, such as the value of $6288+1048$.
2. **$G$** is a graph "that tells us how changing a logical variable affects all other variables." It encodes logical, mathematical, computational and causal structure together.
3. **$\mathrm{fdt}(\underline P,\underline G,\underline x)$** is a node in the model. It represents the output of A-FDT itself when run on inputs $P,G,x$. The underlines denote dequoting: if $x:=3$ then $Z\underline{x}$ names the variable $Z3$.
4. **$\mathrm{do}$** is Pearl's surgery, applied to this logical node instead of a physical action node.

The intervention is evaluated for each available action $a$, and the action with the highest expected $V=\mathcal U(\mathrm{Outcome})$ is executed.

The paper identifies two differences from CDT. The first is the **site of intervention**. CDT intervenes on a node for the agent's physical action. A-FDT intervenes on a node for the output of its decision procedure. The second is the **treatment of observation**: "where CDT responds to observation by Bayesian conditionalization, [A-FDT] responds to observation by changing which node it intervenes upon." A CDT agent who sees $y$ instead of $x$ conditions on $\mathrm{Obs}=y$. An A-FDT agent switches from intervening on $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to intervening on $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

The slogan is that A-FDT is to subjunctive dependence as CDT is to causal dependence. It is the same surgical method, but the surgery respects every decision-relevant subjunctive dependency instead of only the causal ones. In Peirce's terms, CDT intervenes on the token "my action is $a$," while A-FDT intervenes on the type.

### 2.3 Subjunctive dependence

Two physical systems that compute the same function, or one that contains an accurate model of the other, have behaviors that "subjunctively depend" on that function. The paper's illustration is two calculators computing $6288+1048$. If one shows $7336$, the other almost certainly shows the same. This is not a causal link, and it can hold between calculators built on opposite sides of the universe. Causal dependence is a special case. A scribe who copies a calculator's output depends on it both causally and subjunctively. Mere statistical correlation is not subjunctive dependence. If two calculators are both pink by coincidence, repainting one does not change the other.

So the test for including an arrow from $\mathrm{fdt}$ to a variable $Z$ is this: would $Z$ be different if the function the agent computes had a different output? The paper's contrast is between a predictor, which builds a model of the agent, and a lesion, which does not evaluate the agent's future decisions.

### 2.4 Counterpossibles and the choice to supply $G$

If the decision function outputs *onebox* on this input, then it does so of logical necessity. Evaluating $\mathrm{do}(\mathrm{fdt}=\text{twobox})$ is therefore a **counterpossible**, comparable to asking how elliptic curves would behave if Fermat's last theorem were false. The paper defines a $\mathtt{true}$ operator for logical sentences, but "it's not clear how to define" it. Its way around the problem is to require the dependency structure $G$ as an input, just as CDT requires causal structure as an input. Footnote 9 mentions that some hope counterpossible research will eventually yield conditioning on logical falsehoods, giving an "evidential version" of the theory. The paper has no such definition, and Equation (4) is not that version.

The paper admits that Equation (4) "rests on shakier philosophical foundations" than the CDT equation. Pearl gave a method for inferring causal structure from observation and experiment, but nothing comparable exists for subjunctive structure. The paper calls deducing that structure "perhaps the largest open problem in the study of [A-FDT]." The authors add that the agent need only handle questions such as "How would this predictor's prediction of my action change if the [A-FDT] algorithm had a different output?"

### 2.5 Self-reference

The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is named by the model that contains it. This looks circular, but the paper calls it harmless: the agent need not know the value of the node to have a variable representing it. Kleene's second recursion theorem ("quining") shows that structures can contain accurate representations of themselves.

## 3. How to apply it: a recipe

The paper's worked examples follow a consistent pattern, which I state as a procedure. The paper does not give this exact list, but each step appears in its examples.

1. **Write $P$.** Include stochastic nodes such as the predictor's accuracy, deterministic nodes for the world's mechanisms, and a utility node.
2. **Write $G$.** Add one $\mathrm{fdt}$ node for each observation value the agent might receive. Draw an arrow from the relevant $\mathrm{fdt}$ node to every variable that implements, models or predicts that function. Do not draw arrows to variables that merely correlate with the agent's action.
3. **Select the node.** Given the actual observation $x$, intervene on $\mathrm{fdt}(\ldots,x)$. Other $\mathrm{fdt}(\ldots,x')$ nodes stay at their prior distributions.
4. **Intervene and propagate.** For each $a$, set $\mathrm{fdt}_x=a$. Recompute every descendant, including predictions, copies of the agent, the observation node, and the physical action. Leave non-descendants at their prior values.
5. **Score and maximize.** Compute $\mathbb E[V]$ under each surgery and output the best $a$.

One point deserves attention. Equation (4) contains no conditioning on $\mathrm{Obs}=x$. The observation enters only through the index of the node. This matters because the observation can itself be downstream of the intervention. In the transparent Newcomb problem below, setting the output to *twobox* changes what the agent would have seen. (Section 6 writes "$\mathrm{Obs}=\mathit{full}$" inside an expectation, but the computation actually performed lets the observation vary under intervention. I follow the computation.) The paper describes this as a feature: A-FDT "agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

## 4. Worked examples

### 4.1 Newcomb's problem

Accuracy is 0.99 and the payoffs are \$1,000,000 in box B and \$1,000 in box A. In Fiona's graph, a single node $\mathrm{fdt}(\underline{P^F},\underline{G^F})$ points to both $\mathrm{Act}$ and $\mathrm{Prediction}$. The two surgeries give:

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$: $\mathbb E[V]=0.99\times 1{,}000{,}000=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$: $\mathbb E[V]=0.99\times1{,}000+0.01\times1{,}001{,}000=\$11{,}000$.

A-FDT one-boxes. Carl's CDT graph has $\mathrm{Act}$ and $\mathrm{Prediction}$ as siblings under a common cause, "Predisposition". Intervening on $\mathrm{Act}$ leaves $\Pr(\text{full})=p$ fixed, so two-boxing wins by \$1,000 for every $p$. Eve's EDT conditionalization also picks one-boxing, but her answer depends on her prior over her own action. Under extreme priors she can be made to do anything.

The paper stresses that A-FDT does not posit retrocausation. Fiona knows the box is already filled. She refuses to imagine her function's output changing while the predictor's model of that function stays fixed. "When she imagines two-boxing, she therefore imagines a hypothetical world where box B is empty."

### 4.2 The twin prisoner's dilemma

Here $\mathrm{fdt}$ points to both players' moves. Cooperating yields \$1,000,000 and defecting yields \$1,000, so A-FDT cooperates. Unlike EDT's cooperation, this does not rest on treating the action as evidence. It rests on the structural fact that the twin runs the same function.

### 4.3 The smoking lesion

The paper builds the graph with some care. A lesion causes both the desire to smoke and a high chance of cancer. A-FDT's $\mathrm{fdt}$ node points to $\mathrm{Act}$ but not to $\mathrm{Cancer}$. Fiona is uncertain about her own utility function, so there are two possible nodes, one for each lesion state, and $\mathrm{Act}$ is selected by $\mathrm{Lesion}$. She intervenes on the node she in fact occupies. Writing $p$ for the lesion probability, smoking beats refraining by $p\cdot\$1{,}000$ and she smokes. This shows that the same rule one-boxes and smokes, though the graph differs between problems. The paper itself calls the lesion problem "contrived" and recommends abandoning it, so I do not lean on it.

### 4.4 The transparent Newcomb problem and Parfit's hitchhiker

The paper holds that one-boxing on seeing two full boxes "is precisely equivalent to paying the driver in Parfit's hitchhiker problem." Fiona's graph has two nodes, $\mathrm{fdt}_{\text{full}}$ and $\mathrm{fdt}_{\text{empty}}$. $\mathrm{Prediction}$ determines which of them controls $\mathrm{Act}$, because the prediction determines what she sees. Write $q$ for her prior that she two-boxes on seeing an empty box. Having seen a full box, she intervenes on $\mathrm{fdt}_{\text{full}}$:

- *onebox*: if the predictor is accurate (0.99), the box is full and she takes one box, for \$1,000,000. If not, the box is empty and her $\mathrm{fdt}_{\text{empty}}$ behavior governs. This gives $990{,}000+10q$.
- *twobox*: if accurate, the box is empty and she is in the $\text{empty}$ branch. If not, she gets \$1,001,000. This gives $10{,}010+990q$.

The paper's own displayed value for this second quantity contains a typo, which I have corrected. For any $q\in[0,1]$, one-boxing wins. The result does not depend on getting $q$ exactly right. Substantively, when she imagines two-boxing "she envisions a scenario where she instead (with high probability) sees that the box is empty." The paper offers three arguments for accepting this: precommitment, the non-negative value of information, and (decisively, in the authors' view) utility.

Parfit's hitchhiker has the same structure: the driver rescues the agent iff the agent is predicted to pay. A-FDT pays. This is not a bonus on top of the theory. It is the same surgery applied to a node whose descendants include the driver's decision to give the lift.

### 4.5 XOR blackmail, mechanical blackmail, and extortion

In XOR blackmail, $\mathrm{Infestation}$ is not downstream of $\mathrm{fdt}$, but the sending of the letter is. Fiona therefore sees that refusing means never getting the letter in the infested worlds, and she does not pay. Eve pays because conditioning on payment moves her probability of termites to zero. Carl also refuses, but for a different reason (termites are causally upstream) and with a different counterfactual. Asked what would have happened had he paid, Carl says he would still have received the letter. That presupposes an erring predictor.

In mechanical blackmail with a perfect predictor, $\mathrm{do}(\mathrm{fdt}_{\text{blackmail}}=\text{refuse})$ leads to a world in which the blackmailer never ran the program. A-FDT refuses while holding the letter, which is the stance of an agent who would never be blackmailed.

The paper then considers an imperfect predictor. Refusing means being blackmailed with probability $\varepsilon$ and losing \$1,000,000, so the expected loss is $10^6\varepsilon$. Paying means always being blackmailed and losing \$1,000. The break-even point is $\varepsilon=0.1\%$. The paper's numerical examples (0.09% refuses, with expected loss \$900) are consistent with this. Its second example, where 0.011% is said to make her pay, is inconsistent with that arithmetic and looks like a slip for 0.11%. This matters because it shows A-FDT is a quantitative rule, not a blanket refusal policy. Fiona "refuses to pay, even when holding the blackmail letter, even though she *knows* that the blackmailer predicted wrongly."

### 4.6 Cosmic ray and Death in Damascus

In the cosmic ray problem, an EDT agent who almost always takes \$1 fears that taking \$100 signals a cosmic ray. A-FDT treats that correlation as merely statistical, breaks it, and takes \$100. In Death in Damascus, Death's book is subjunctively downstream of the agent's function. A-FDT stays and saves \$1,000. A CDT agent cycles because her hypotheticals hold Death fixed while she changes her mind. A consequence the paper stresses is that Carl would refuse to pay \$1 for a truly random coin worth a 50% chance at survival, because his hypotheticals make it worthless.

## 5. How A-FDT relates to CDT and EDT

The paper's analysis is that EDT's hypotheticals "respect too many correlations" and CDT's "respect too few." A-FDT sits between them: it preserves exactly those correlations that arise from subjunctive dependence. In models where every correlation between $\mathrm{Act}$ and another variable is caused by $\mathrm{Act}$ (apart from dependence on the function node itself), the paper shows all three agree:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)].$$

The theories diverge only when something other than the agent's action produces correlations with it, as when predictors or twins are present.

**Dominance.** A CDT dominance argument asks what happens if the action changes "holding constant everything except the action's effects." The paper replies that every method of constructing hypotheticals induces its own notion of dominance, so dominance cannot be a neutral tiebreaker. It defines an A-FDT-style dominance: hold constant all relevant subjunctive dependencies, and switch the output of the algorithm. On that standard A-FDT never takes a dominated action.

**Utility as the criterion.** The main argument is that A-FDT agents reliably have more money in these problems. The paper does not claim A-FDT beats every theory in every problem. It admits one can build dilemmas that punish any theory, for instance one that punishes an agent for using A-FDT itself. The claim is limited to "fair" problems, those where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the problem at hand. The paper concedes that a formal criterion of fairness is missing. Its footnote 15 notes that a problem which punishes anyone who matches a copy of Fiona is intuitively unfair to Fiona but would be won by Carl.

## 6. Open questions and interpretive choices

### 6.1 Actions or policies

The text of Equation (4) selects an *action* $a$. Footnotes 7 and 16 say the authors' "preferred formalization" actually iterates over policies, meaning maps from observations to actions, and that "the difference only matters in multi-agent dilemmas so far as we can tell." The assignment fixes Equation (4) as the formalization, so my account has been action-based. I flag the following consequences.

In the action-based version, intervening on $\mathrm{fdt}_x$ leaves the other nodes $\mathrm{fdt}_{x'}$ at their priors, which is why $q$ appears in the transparent Newcomb calculation. The paper says the correct value of $q$ does not matter in its examples, but nothing guarantees this in general. **[Proposal]** The principled choice is to set each such prior to the agent's own best response at $x'$, computed by the same procedure. That makes the action version a fixed point of coordinate-wise evaluation. When consistency fails, one should move to the policy version, which maximizes jointly over all coordinates. I regard the policy version as the safer practical choice, but this is my recommendation, not the assigned formalization.

### 6.2 Constructing $G$

This is the major open input. The paper offers no algorithm, only the requirement that the agent's imagined changes be to "all and only those things that subjunctively depend on the output of her decision-making procedure." **[Proposal]** In unfamiliar cases I would use a working checklist:

- *Predictors and twins:* if a process contains an accurate model of the agent's function, or runs the same function, link it to $\mathrm{fdt}$. For imperfect predictors, make the link stochastic through an accuracy node, as in the paper's Newcomb graph.
- *Mechanical correlates:* if a variable and the agent's action share a common cause but the variable does not evaluate the agent's function (the lesion, the pink calculator), do not link it.
- *Consistency check:* the finished graph should answer the question "what would have happened if I had done otherwise?" without describing a world in which a known-accurate predictor errs. If it does, the graph is probably missing a link. This is the paper's test for why Carl's answers are wrong.
- *Sensitivity analysis:* because $G$ is an input and not derived, one can compute the decision under several candidate graphs. If they agree (as in the lesion problem for $q$), the decision is robust. If they disagree, the disagreement shows exactly which empirical or logical claim about dependence is carrying the decision.

I stress that this is judgment, not derivation. Misspecified graphs can produce bad decisions. For example, treating an adversary's mind-reading of one's *algorithm* as a prediction of one's *action* would misapply the rule. The paper's fairness discussion makes the same distinction when it says a predictor who punishes a particular *procedure*, and not a predicted *action*, is unfair.

### 6.3 Counterpossibles

The paper's position is that this difficulty is "technical rather than philosophical," and it points to human mathematicians who reason under uncertainty about logical claims. This is not a solution. Eq. (4) sidesteps the problem by taking $G$ as given, so all of the unresolved content of counterpossible reasoning ends up inside $G$.

## 7. Philosophical motivation

Two themes connect the procedure to its motivation.

**Control without delusion.** A-FDT is accused of acting as though one controls past events or abstract functions. The paper answers symmetrically. A deterministic CDT agent also entertains hypothetical worlds in which her action differs, though only one action is physically possible. A-FDT does the same with the output of the function. "Any principled objection to the idea that [A-FDT] agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token." What gets evaluated is a hypothetical, a "mental or computational object" used like notes on scratch paper, and not a belief about physics.

**The global perspective.** The agent is told to ask "What would the entire universe look like if the [A-FDT] algorithm behaved differently?" and to choose the action corresponding to the best imagined universe. This explains why A-FDT acts as it would have precommitted to act, without paying for a precommitment device. It also explains why A-FDT "is reflectively stable in fair problems" in the paper's phrase. A CDT agent would modify herself to stop being a CDT agent in future Newcomblike problems, whereas an A-FDT agent has no such wish, because her hypotheticals already include the consequences of being a tempting target.

## 8. Conclusion

A-FDT is a single surgical rule: for each available action, intervene on the logical node standing for the output of the agent's own decision procedure on her actual inputs, propagate the intervention through a graph of causal and subjunctive structure, and pick the action with the highest expected utility. Observation changes which node is intervened on and is not an ordinary Bayesian update. This one rule one-boxes in Newcomb's problem, cooperates with a twin, pays in Parfit's hitchhiker and in the transparent Newcomb problem, smokes, refuses XOR and mechanical blackmail at appropriate error rates, and stays put in Damascus.

The unresolved part is the graph. The paper treats subjunctive structure as an input and openly states that no principled method for inferring it exists. So A-FDT is a precise procedure given $(P,G)$ and only a partial theory of how to obtain $G$. An operational reader should treat the checklist in section 6.2 as a disciplined heuristic. They should also remember that the paper's own preferred formalization is policy-based, and that a few of its numerical examples contain slips that this essay has corrected.

## References

- Yudkowsky, E. and Soares, N. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060. The source for all definitions, quotations and examples above.
- Joyce, J. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999. The representation theorem the paper builds on.
- Pearl, J. *Causality*. Cambridge University Press, 2000. The source of the $\mathrm{do}$ operator.
- Gibbard, A. and Harper, W. "Counterfactuals and Two Kinds of Expected Utility," 1978. The source of the expected-utility framing and the Death in Damascus example.