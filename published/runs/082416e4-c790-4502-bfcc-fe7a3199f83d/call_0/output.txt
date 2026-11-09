# A-FDT: Choosing by Intervening on the Decision Function

## 1. The idea

A-FDT is the decision theory given by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality" (Section 5). I use "A-FDT" for that procedure throughout. I call the evidential and causal theories EDT and CDT.

All three theories maximize expected utility. They differ in what "if I did a" means. In the paper's Equation (1), the expected utility of action a is

EU(a) = Σ_j P(a ↪ o_j; x) · U(o_j),

where ↪ is the connective for decision hypotheticals. The paper follows Joyce in saying that the theories disagree about "the epistemic perspective from which actions are to be evaluated". They do not disagree about value.

- EDT reads ↪ as conditioning: argmax_a E(V | Obs=x, Act=a). This is Equation (2).
- CDT reads ↪ as a Pearl intervention on the physical action: argmax_a E(V | do(Act=a), Obs=x). This is Equation (3).
- A-FDT, Equation (4), is

 A-FDT(P, G, x) := argmax_{a∈𝒜} E( V | do( fdt(P̲, G̲, x̲) = a ) ).

Here P is a probability distribution over the agent's model variables. G is a graph describing how changing a variable, including a *logical* variable, propagates to others. x is the observation history. fdt(P̲, G̲, x̲) is a node representing the output of A-FDT itself on those very inputs. The underlines denote dequoting, and the self-reference is harmless by Kleene's recursion theorem ("quining"). The agent need not know the value of the node in order to have a variable that represents it.

## 2. Two differences from CDT

The paper identifies exactly two.

1. **Where the intervention happens.** CDT intervenes on a node for the physical act. A-FDT intervenes on the node for the *output of its decision function*. In Peirce's terms, CDT intervenes on a token and A-FDT on the type. The surgery therefore propagates to everything that depends on that function. This includes the agent's own body, and also twins, predictors and other copies or models of the agent. Correlations are kept when they reflect dependence on the function, which the paper calls *subjunctive dependence*. Merely statistical correlations are severed.

2. **How observations enter.** CDT conditions on Obs=x. A-FDT does not condition on its observation. It changes *which node it intervenes on*, from fdt(P̲, G̲, x̲) to fdt(P̲, G̲, y̲) when the observation is y. Because the same function is evaluated on different inputs, each observation corresponds to a different node. In the intervened scenario the agent's observations may therefore differ from the ones it actually has. The paper says A-FDT "should entertain the hypothesis that, if their action were different, they might have *made different observations*."

A consequence stated in the paper: where every correlation between Act and the world is caused by Act, the three theories coincide, since E[V|a] = E[V|do(a)] = E[V|do(fdt=a)]. They diverge when something correlates with the action without being caused by it, for instance a predictor.

## 3. Subjunctive dependence

Two systems subjunctively depend on a function when they compute it. Two calculators computing 6288+1048 are the standard example. A predictor holding an accurate model of the agent is a "twin inside the predictor's mind". Causal dependence is a special case: a scribe copying a calculator's output would write something different if the output were different. A shared colour is a mere correlation, because a different calculator in Paris would not change the colour of the one in Tokyo.

Subjunctive dependence is graded. If the predictor's model is imperfect, the link is weakened but not eliminated. This is why the 99% accuracy node appears in the Newcomb graph.

## 4. How to apply the procedure

The procedure is stated for given (P, G). The steps are:

1. Build the variables, including a node F = fdt(P̲, G̲, x̲) for the output of the procedure on the actual observation.
2. Draw G so that F is a parent of every variable that implements or models the function (the act, any prediction, any twin), and of nothing that is merely correlated with the agent.
3. For each action a, set F=a with do(·), propagate through G, and compute E[V].
4. Output the argmax.

Fiona is the paper's A-FDT agent. The paper's worked cases:

**Newcomb's problem.** Both Act and Prediction are children of F. Do(F=onebox) gives Act=onebox and P(full)=0.99, so EU = $990,000. Do(F=twobox) gives P(full)=0.01, so EU = $11,000. Fiona one-boxes. She does not need retrocausation. She simply declines to imagine her action varying while the function's output stays fixed. CDT's dominance argument "asks us to imagine it outputting 3159, holding constant the fact that 6288+1048=7336."

**Smoking lesion.** The paper builds the graph with F feeding Act but *not* Cancer. Lesion is a parent of both Act and Cancer, so it is not downstream of F. The paper models the lesion as selecting which of two functions (one for each preference set) controls Act. In both intervened scenarios P(lesion) stays at p. Smoking is then better by p·$1,000 (per the paper's calculation, whose utility numbers do not exactly match the problem statement), and Fiona smokes. The same equation one-boxes and smokes. This works because G differs between the two problems, not because the rule does.

**Transparent Newcomb and Parfit's hitchhiker.** Fiona sees a full box, so her node is fdt(·, full). Prediction determines which node (full or empty) controls Act. Intervening on the full-node to output twobox makes the prediction likely "2", hence the box likely empty, hence her observation likely "empty". The paper computes EU(onebox) = $990,000 + 0.01q·$1,000 and EU(twobox) = about $110,000 + q·$990 (printed as "$110,00"), so she one-boxes. Hitchhiker has the same structure, so she pays. The paper argues that no precommitment is needed, because she acts as she would have precommitted.

**Blackmail.** In mechanical blackmail, setting fdt(·, blackmail)=pay makes blackmail near-certain and costs $1,000. Setting it to refuse makes blackmail near-impossible. She refuses. With blackmailer error 0.0009, refusing costs 0.0009 · $1,000,000 = $900 in expectation, versus $1,000 for paying, so she still refuses. At error 0.00011 (the paper's "0.011%"), refusing costs $110 in expectation, so she pays. In XOR blackmail she refuses because the infestation node is not downstream of F.

**Death in Damascus.** F controls both Act and the entry in Death's book. Staying costs $0, fleeing costs $1,000, and survival is lost either way, so she stays. There is no instability, and she would pay $1 for a truly random coin, which CDT will not.

**Cosmic ray.** A-FDT severs the merely statistical link between taking $100 and being hit, so it takes the $100, whereas EDT takes the $1.

## 5. Policies versus actions

Footnote 7 and 16 say the authors' preferred formalization intervenes on a *policy* (a map from observations to actions) rather than on an action. The paper states that this matters only in some multi-agent cases and uses actions throughout. In the examples above, the observation-indexed nodes (fdt(·, full), fdt(·, empty)) already behave like components of a policy. Where several nodes appear, as in blackmail, the probability q assigned to the *other* node is an input to the evaluation. The paper observes that its true value does not alter the choice in those examples.

## 6. What the source leaves open

The source is explicit that the weakest point is G. Equation (4) works *given* a graph describing how changing a logical variable affects other variables. The paper says "it is not yet clear how to construct such a thing—nor even whether it can be done in a satisfactory manner within Pearl's framework". It calls learning subjunctive-dependence structure from observation "perhaps the largest open problem". A fully general true(·) operator for conditioning on false logical sentences is not defined, and footnote 9 mentions an "evidential" alternative that would need one.

The paper also leaves unformalized how to separate "fair" problems from unfair ones. Its informal criterion is that the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the problem at hand. It claims A-FDT does at least as well as its rivals in such problems, but this is a conjecture ("no fair dilemmas in which FDT systematically achieves lower utility"), not a theorem.

## 7. A proposed operational reading (my own, not the paper's)

A usable rule of thumb that fits the worked examples: *put an edge from F to X exactly when X would have been different had a reliable simulation or copy of the agent's reasoning returned a different answer.* Three tests follow.

- Does X contain a model of my procedure, or something that uses the same procedure? If so, F is a parent.
- Does X merely share a cause with my action, with no process that evaluates my reasoning? If so, X is not downstream of F. The lesion is an example.
- Could X's existence depend on which observation I would get, as with letters, visible boxes and being asked at all? If so, track which observation-indexed node controls Act, and let the scenario change the observation, as in the transparent boxes.

For imperfect predictors, give the F→Prediction edge a noise node, as the paper does with Accurate. This is a modelling proposal, and different agents with different G's will disagree. In practice the verdict can be fragile in how the dependence is drawn. For example, an adversary who rewards agents for *which procedure* they use, rather than for their predicted behavior, is outside the fairness criterion, and the paper says no theory is safe there.

## 8. Philosophical stance

The paper claims that A-FDT corrects both rivals. EDT respects too many correlations, so it manages the news and can be exploited with good news (XOR blackmail). CDT respects too few, so it imagines perfect predictors erring exactly when it chooses. The paper adds that both A-FDT and CDT use counterfactuals that "contain impossibilities". CDT imagines a deterministic agent acting otherwise. A-FDT imagines a function with a different output. Its main justification is utility achieved in fair problems, plus reflective stability: it does not want to self-modify in order to escape its own recommendations, as the paper says CDT does.

## 9. Conclusion

A-FDT is Pearl-style expected utility maximization with a changed locus of intervention. It intervenes on the logical node "what my decision procedure outputs on these inputs", and the dependence graph, not the rule, determines how the effect propagates. Its practical verdicts, such as one-boxing, paying the hitchhiker and refusing blackmail, follow once G is drawn. The unsolved part is how to justify G in the first place.