# A-FDT: Deciding by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision procedure given by Equation (4), Section 5, of Yudkowsky and Soares's paper "Functional Decision Theory: A New Theory of Instrumental Rationality". I use "A-FDT" throughout for that equation, which the paper calls "FDT". It selects an action. The paper's footnotes say its authors' preferred formalization iterates over policies, meaning maps from observations to actions. I discuss that variant separately in section 6.

The paper's central claim is that a rational agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" A-FDT is contrasted with two rivals:

- Causal decision theory (CDT) asks which physical act of mine causes the best outcome.
- Evidential decision theory (EDT) asks which act would be the best news to learn I took.

All three are expected-utility theories. They differ only in how they build the hypothetical for each action. The paper puts it this way, following Joyce: they supply different "epistemic perspectives."

## 2. The formal definition

The paper's general template (Equation 1) is

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

The connective $\hookrightarrow$ is the interpretive free parameter. The three theories fill it in as follows.

**EDT (Equation 2).**
$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a).$$

**CDT (Equation 3).**
$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x).$$

**A-FDT (Equation 4).**
$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- $P$, a probability distribution over variables of the agent's world-model, including variables for the outputs of mathematical functions. The paper's example is a variable for $6288+1048$ that puts nearly all its mass on 7336.
- $G$, a graph encoding how changing a logical or computational variable propagates to the other variables. This is the "subjunctive dependence" structure.
- $x$, the observation history.

The underlined arguments are dequoted names. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of the A-FDT algorithm on exactly these inputs. Its name depends on the model, so it is self-referential, but the paper calls this harmless. The agent needs only a variable standing for her own output, not its value, and Kleene's second recursion theorem ("quining") shows such self-representing structures can be built.

Two differences from CDT follow, and the paper states both explicitly:

1. **Where to intervene.** CDT intervenes on a physical action node. A-FDT intervenes on a node for the output of the decision function, so the intervention propagates to everything that subjunctively depends on that function. That includes the agent's own body and any predictors or twins that model her. The paper puts this as "Peirce's type–token" distinction: CDT intervenes on the token "my action is $a$", A-FDT on the type.
2. **How observation enters.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. Observation changes which node is intervened on: $\mathrm{fdt}(\underline P,\underline G,\underline x)$ versus $\mathrm{fdt}(\underline P,\underline G,\underline y)$. So an observation does not simply rule out worlds. The agent considers hypotheticals in which she saw something else.

Equation (4) rests on a graph $G$ because the paper lacks a workable $\mathtt{true}$ operator for logical counterpossibles. It says: "Unfortunately, it's not clear how to define a $\mathtt{true}$ operator." The graph supplies the structure instead, just as CDT takes a causal graph as input.

## 3. Subjunctive dependence

A variable subjunctively depends on the decision function when it would differ if that function had a different output. The paper's examples:

- Two calculators computing $6288+1048$ depend on the same function. Seeing one output 7336 licenses a confident inference about the other, up to error.
- Causal dependence is a special case. A scribe copying a calculator's output depends on it subjunctively as well as causally.
- Mere statistical correlation is not dependence. Two pink calculators are correlated, but if one had been green the other would still be pink.

This is why a predictor and a lesion are treated differently. A predictor holds an accurate model of the agent's function, so it depends on that function. A lesion that causes both smoking and cancer does not evaluate the agent's decision. If the predictor is imperfect, the dependence is weakened but not eliminated.

The paper is clear that hypotheticals on this view involve counterpossibles, since the function does in fact output one thing. It says this is "the main drawback of FDT relative to CDT at this time", though it argues the difficulty is technical, not philosophical, and notes that humans reason about such cases tolerably well. The paper also considers a variant that asks "What if I used a different decision function?" and argues it just reintroduces the same problem. That is because predictors of the original function must still be imagined as predicting differently.

## 4. Worked applications

The procedure is: (i) build $P$ and $G$, marking which nodes are downstream of the decision function; (ii) for each action $a$, intervene on the node for the function's output given the actual observation; (iii) compute expected utility; (iv) take the argmax.

**Newcomb's problem.** The predictor is 99% accurate. Intervening on $\mathrm{fdt}$ sets both $\mathrm{Act}$ and $\mathrm{Prediction}$:

- One-box: the box is full with probability 0.99, giving about \$990,000.
- Two-box: the box is full with probability 0.01, giving about \$11,000.

So A-FDT one-boxes. No retrocausation is assumed. The agent simply declines to imagine her action varying while the prediction of that very function stays fixed.

**Smoking lesion.** The graph differs. The lesion influences $\mathrm{Act}$ but is not downstream of the decision function, so intervening leaves $P(\text{lesion})=p$ unchanged. Smoking then wins by $p\cdot\$1000$. The paper formalizes this with two functions, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, one for each possible preference set, with the lesion deciding which controls the action. The graph, not the payoff table, separates this case from Newcomb's problem. The paper concedes the case is contrived and recommends abandoning it.

**Transparent Newcomb and Parfit's hitchhiker.** Here the observation rule matters. Seeing a full box, A-FDT intervenes on $\mathrm{fdt}(P,G,\mathit{full})$. Setting that to *twobox* makes the predictor likely to have left the box empty, so the agent would more likely have been running $\mathrm{fdt}(P,G,\mathit{empty})$. With $q$ the probability she two-boxes on seeing an empty box:

- One-boxing is worth $\$990{,}000+0.01\,q\,\$1000$.
- Two-boxing is worth about $\$11{,}000+q\cdot\$990$.

So A-FDT one-boxes even when it sees two full boxes. The paper notes this is structurally the same as paying the driver in Parfit's hitchhiker problem.

**Mechanical blackmail.** On receiving the letter, "pay" corresponds to a world where she is always blackmailed and loses \$1,000. "Refuse" corresponds to a world where she is almost never blackmailed. A-FDT refuses. The paper adds a sensitivity check. If the blackmailer wrongly predicts payment with probability 0.0009, refusing costs about \$900 in expectation against \$1,000 for paying, so A-FDT still refuses even holding the letter. At error 0.011% the comparison reverses and it pays.

**Death in Damascus.** Death's location depends on the function through the prediction in his book. So wherever A-FDT goes, Death is there, and it stays and saves the \$1,000. CDT by contrast oscillates because it holds Death's location fixed. The paper also shows CDT refusing a \$1 truly random coin that gives a 50% chance of survival.

**XOR blackmail.** Intervening on the function changes whether the letter is sent but not whether the house has termites, so A-FDT refuses. EDT pays because conditioning on payment makes termites improbable.

When all correlations with the action are causal, the paper notes that the three theories agree.

## 5. Operational reading, and what I add

The following is my reading of how a reader would apply Equation (4). The paper does not spell it out in these terms.

**Dependence checklist.** For each variable $Z$ in the problem, ask whether $Z$ would be different if the function computed here returned something else. This includes copies of the agent, predictors with accurate models, and the agent's own future selves in relevantly identical situations. Draw the arrows accordingly. The paper's own examples include the gym case, where this week's and next week's decisions are treated as the same function, and the ten-agent voting case. Hold fixed everything else, including mere correlations.

**Observation handling.** Each possible observation indexes a separate node, and every pathway by which the agent might have been shown that observation should be in the graph. This is what lets "observing a full box" be a variable downstream of the prediction. Omitting such pathways gives wrong answers, because the agent could then not imagine seeing something different.

**Unspecified parts.** The paper says it has no method for deriving $G$ from experience. It calls this "perhaps the largest open problem". It also gives no criterion for how strong a dependence must be to be drawn, and no full definition of fairness. I add that all the paper's worked examples use deterministic nodes with noise variables like $\mathrm{Accurate}$, and that is the only regime where the procedure is fully specified.

**Policies versus actions.** The authors prefer policies, while Equation (4) as stated is over actions. I would add that in single-agent problems with observations, the two generally coincide when the node-per-observation structure above is used, which is consistent with the paper's remark that the difference matters only in multi-agent dilemmas. This is an interpretation, not a claim from the paper.

## 6. Philosophical motivation and limits

The paper's primary argument is utility: A-FDT agents tend to end up richer in fair dilemmas. "Fair" means the outcome depends only on the agent's behaviour in the problem at hand and the agent's beliefs are accurate, not on which decision procedure she uses. The paper admits it has no formal criterion and that one can build dilemmas that punish any theory. Its footnote gives an example where Fiona (the A-FDT agent) loses to a copy of herself.

Secondary arguments are that A-FDT acts as a precommitment would, avoids negative value of information, and endorses its own use. It also answers the dominance objection. Dominance depends on which hypotheticals one holds fixed, so each theory has its own notion, and A-FDT never takes an action dominated in its own sense.

One caveat is that A-FDT's verdicts, such as one-boxing on a visible full box, are counterintuitive. The paper's response is that CDT's deterministic hypotheticals involve a similar fiction about control.

I add one more caution of my own. Because Equation (4) depends so heavily on $G$, the theory's answer to an unfamiliar case is only as good as the dependency graph one writes down. A reader should treat the graph as a substantive modelling assumption.

## 7. Conclusion

A-FDT keeps expected-utility maximization and Pearl-style surgery but moves the surgery from the physical act to the output of the decision function, and handles observation by changing which node is intervened on. EDT preserves too many action–environment correlations and CDT too few. A-FDT preserves exactly the dependencies that track the function. Its practical use depends on getting the dependency graph right, which the source leaves open.