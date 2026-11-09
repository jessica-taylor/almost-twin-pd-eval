# A-FDT: Choosing as the Output of a Function

## 1. What this essay is about

Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes that an agent should not ask "which physical act of mine has the best consequences?" Instead she should treat her decision as the output of a fixed mathematical function. Its abstract puts the question as: "Which output of this very function would yield the best outcome?"

The paper gives one fully explicit decision rule, Equation (4) in Section 5. That rule maximizes over **actions** for the single input the agent currently faces. The authors note in footnotes that their "preferred formalization" instead iterates over *policies*. To keep the two apart, I call the rule defined by Equation (4) **A-FDT** (action functional decision theory). I call the policy-iterating variant mentioned in the footnotes **policy-selecting FDT**. The paper itself uses the single label "FDT," and I keep that label inside quotations.

I also mark which claims come from the paper and which are mine. The paper supplies the equation, the worked dilemmas, and the philosophical arguments. The following are my own additions:

- the step-by-step recipe in §4,
- the reduction lemma in §3,
- the coordination example in §6,
- the proposed conventions for filling the formal gaps.

## 2. The formal object

### 2.1 Common frame

The paper treats EDT, CDT and A-FDT as expected-utility theories. All three maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

They differ only in how the decision hypothetical "$\hookrightarrow$" is read. Following Joyce (1999), the paper says the theories disagree "about the epistemic perspective from which actions are to be evaluated." Write $V = \mathcal U(\textsc{Outcome})$.

- **EDT (Eq. 2)** conditions: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT (Eq. 3)** intervenes on the physical act and conditions on observations: $\arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x)$.

### 2.2 Equation (4)

A-FDT takes as input a probability distribution $P$, a graph $G$, and an observation history $x$:

$$
\boxed{\;\text{A-FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\; \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}
$$

Each ingredient works as follows.

- **$P$ is a joint distribution over world variables, including logical ones.** The paper requires that "$P$ must contain variables representing the outputs of different mathematical functions." In particular it must contain a variable $\textsc{fdt}(\underline P,\underline G,\underline x)$. Underlining denotes dequoting: this is the variable *named* "output of the A-FDT algorithm on inputs $(P,G,x)$."
- **The self-reference is deliberate.** The variable's name depends on the model that contains it. The paper calls this harmless. The agent need not know the variable's *value* in order to represent it, and Kleene's recursion theorem shows how such self-describing data structures ("quining") can be built.
- **$G$ is a graph of subjunctive dependence.** It plays the role Pearl's causal graph plays for CDT, but it also records which variables "depend on" the output of a mathematical function. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."
- **$do(\cdot)$ is Pearl's operator, reused.** The logical node is set to $a$. Everything downstream of it in $G$ is recomputed, and everything else keeps its prior distribution. The paper's idealized alternative is a $\mathtt{true}(\phi)$ operator that updates on counterpossible logical sentences. Because nobody knows how to define $\mathtt{true}$, the logical-dependency structure is supplied as an input, exactly as causal structure is supplied to CDT.

### 2.3 Two structural differences from CDT

The paper identifies exactly two differences between A-FDT and CDT:

1. **Where the intervention lands.** A-FDT intervenes on the *type* (the function's output), not the *token* (the physical act). Any physical system computing or accurately modeling that function, such as the agent's body, a twin, or a predictor's simulation, moves with the intervention.
2. **How observations enter.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Equation (4) contains no "$\textsc{Obs}=x$" term. The observation appears only in the name of the intervened node.

One immediate consequence: interventions are well defined even when $P(\textsc{fdt}=a)=0$. EDT must exclude zero-probability actions. A-FDT can evaluate an option it is certain it will not take, because it imagines the option rather than conditioning on it.

## 3. Observations as node selectors

The second difference is the conceptual heart of the theory. Here is how it works mechanically.

**The model contains many decision nodes.** Suppose there is a family of nodes $\textsc{fdt}_y := \textsc{fdt}(\underline P,\underline G,\underline y)$, one for each observation history $y$ the agent might have. Her physical act is then a *selector*:

$$
\textsc{Act} = \textsc{fdt}_{\textsc{Obs}}.
$$

**Observations can be downstream of the agent's own function.** The variable $\textsc{Obs}$ may itself depend on some $\textsc{fdt}_y$, for example when a predictor decides what the agent gets to see. Intervening on $\textsc{fdt}_x$ can then change the probability that $x$ is observed at all. This is the sense in which, in the paper's words, "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

**In ordinary problems this changes nothing.** The following lemma is my own observation, but it follows directly from the definitions.

> **Lemma.** Suppose that in $G$ the only descendant of $\textsc{fdt}_x$ that affects $V$ is $\textsc{Act}$, and that $\textsc{Obs}$ is not a descendant of $\textsc{fdt}_x$. Then
> $$\mathbb E\big(V\mid do(\textsc{fdt}_x=a)\big) = P(\textsc{Obs}\neq x)\,c + P(\textsc{Obs}=x)\,\mathbb E\big(V\mid \textsc{Obs}=x, do(\textsc{fdt}_x=a)\big),$$
> where $c$ does not depend on $a$. Hence, if $P(\textsc{Obs}=x)>0$, the argmax coincides with that of the conditioned expression, which is CDT's answer whenever $\textsc{Act}$ inherits $\textsc{fdt}_x$'s only effects.

*Proof.* In worlds with $\textsc{Obs}\ne x$, the act is driven by another node, so $V$ is unaffected by $a$. In worlds with $\textsc{Obs}=x$, the act equals $a$. Because $\textsc{Obs}$ is not downstream of the intervention, the event $\textsc{Obs}=x$ keeps its prior probability. $\square$

This makes precise the paper's informal claim that the theories agree "in simple settings." The unconditioned, "updateless" form of Equation (4) bites only when something other than the agent's own act depends on $\textsc{fdt}_x$, and especially when the observation itself does.

## 4. A recipe for applying A-FDT

The paper leaves the construction of $(P,G)$ to the modeler. The following procedure is my operationalization. It reproduces every analysis in the paper.

1. **List the agent's possible inputs.** Make a decision node $\textsc{fdt}_y$ for every observation history $y$ that some part of the problem cares about. That includes the inputs the agent might receive and the inputs a predictor might simulate.
2. **Find every implementation or model of each node.** Draw an arrow from $\textsc{fdt}_y$ to each variable whose value is computed from that function's output at input $y$. This covers the agent's act when she sees $y$, a twin's act on the same input, and a predictor's prediction of "what she would do on seeing $y$." Imperfect predictors get an extra noise parent, as with the paper's $\textsc{Accurate}$ node.
3. **Do not draw arrows to mere correlates.** A lesion, a gene, or a coincidence that is statistically associated with the agent's choice gets no arrow from any $\textsc{fdt}$ node.
4. **Wire the act as a selector.** Set $\textsc{Act}=\textsc{fdt}_{\textsc{Obs}}$, with $\textsc{Obs}$ wired to whatever actually produces it.
5. **Put priors on exogenous variables.** For each non-current node $\textsc{fdt}_y$ with $y\neq x$, specify a belief $q_y$ about its value.
6. **Evaluate and choose.** For each $a\in\mathcal A$, apply $do(\textsc{fdt}_x=a)$, propagate, compute $\mathbb E V$, and take the argmax.

Steps 2–3 are where all the philosophy lives. Step 5 is where Equation (4) is silent in an important way (§6.2).

## 5. Worked examples

All of these follow the paper. Dollar figures stand in for utilities, and I recompute the arithmetic.

### 5.1 Newcomb's problem

A predictor that is 99% accurate fills box B with \$1,000,000 iff it predicts one-boxing. Box A always holds \$1,000. There is no observation, so there is a single node $\textsc{fdt}$, and it is the parent of both $\textsc{Act}$ and $\textsc{Prediction}$.

- $do(\textsc{fdt}=\text{onebox})$: box B is full with probability $0.99$, so $\mathbb E V = 0.99\times 10^6 = 990{,}000$.
- $do(\textsc{fdt}=\text{twobox})$: box B is full with probability $0.01$, so $\mathbb E V = 0.01\times1{,}001{,}000 + 0.99\times1{,}000 = 11{,}000$.

A-FDT one-boxes.

CDT intervenes on $\textsc{Act}$, which leaves $P(\text{full})=p$ fixed. Two-boxing then wins by \$1,000 for every $p$.

The psychological twin prisoner's dilemma has the same structure. The twin's act is a second child of the same node, so cooperating yields \$1,000,000 and defecting yields \$1,000.

### 5.2 Transparent Newcomb

Both boxes are transparent. B is filled iff the predictor predicts the agent would one-box *upon seeing B full*. The agent sees B full, so $x=\text{full}$. Following the recipe:

- The prediction is a child of $\textsc{fdt}_{\text{full}}$ (with noise).
- The observation is a child of the prediction.
- $\textsc{Act}=\textsc{fdt}_{\textsc{Obs}}$.
- Let $q=P(\textsc{fdt}_{\text{empty}}=\text{twobox})$.

| Intervention | Accurate (0.99) | Inaccurate (0.01) | $\mathbb E V$ |
|---|---|---|---|
| $\textsc{fdt}_\text{full}=$ onebox | full, onebox: \$1,000,000 | empty, act set by $\textsc{fdt}_\text{empty}$: $q\cdot$\$1,000 | $990{,}000+10q$ |
| $\textsc{fdt}_\text{full}=$ twobox | empty, act set by $\textsc{fdt}_\text{empty}$: $q\cdot$\$1,000 | full, twobox: \$1,001,000 | $10{,}010+990q$ |

A-FDT one-boxes for every $q\in[0,1]$. When the agent imagines two-boxing, she imagines a world where she probably would not have seen a full box.

Two textual cautions:

- The paper's displayed objective for this case writes "$\textsc{Obs}=\text{full}$" inside the parentheses. Its computation, however, averages over both values of $\textsc{Accurate}$, including the branch where the box is empty. That is unconditioned, as Equation (4) prescribes, and I follow the equation.
- The paper prints the twobox value as "\$110,00," apparently a typo for \$10,010. Similarly, the paper's EDT figure of "\$999,000" for one-boxing in ordinary Newcomb appears to be a typo for \$990,000.

The paper treats Parfit's hitchhiker as the same problem. The driver's rescue plays the role of the full box, and paying plays the role of leaving the \$1,000.

### 5.3 XOR blackmail

A perfect predictor knows whether the agent's house has termites, which have prior probability $p$ and would cause \$1,000,000 in damage. It sends a letter iff exactly one of these holds:

- no termites, and the agent will pay \$1,000 on receiving the letter;
- termites, and the agent will not pay.

The agent has the letter. Let $\textsc{fdt}_{\text{letter}}$ feed both the predictor and the act. Termites are not a descendant, which is step 3 of the recipe.

- **Pay.** With termites (probability $p$), no letter is sent and she loses \$1,000,000. Without termites, the letter arrives, she pays, and she loses \$1,000. So $\mathbb E V = -10^6p-1{,}000(1-p)$.
- **Refuse.** With termites, the letter arrives and she loses \$1,000,000. Without termites, there is no letter and she loses nothing. So $\mathbb E V = -10^6p$.

Refusing is better by $1{,}000(1-p)$.

EDT pays, because conditioning on paying "sends her probability on termites to 0." CDT refuses, but its hypothetical for paying is one in which the infallible predictor erred. A-FDT's hypothetical for paying is one in which the letter was never sent in the termite world.

### 5.4 Smoking lesion

The lesion causes both a taste for smoking and cancer. Smoking itself is worth \$1,000. The paper formalizes the taste as two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$, giving two possible models $P_S, P_R$. The act is controlled by $\textsc{fdt}(\underline{P_S},\underline G)$ if the lesion is present and by $\textsc{fdt}(\underline{P_R},\underline G)$ otherwise.

Cancer has no $\textsc{fdt}$ parent, so intervening leaves $P(\text{lesion})=p$ unchanged. Under the paper's numbers the two options are:

- smoke: $p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q)$;
- refrain: $p(10{,}000)+(1-p)(990{,}000+1{,}000q)$.

These differ by exactly $1{,}000p$, so A-FDT smokes. The lesion does not model the agent's function, so it does not move under the intervention. The agent also does not know which node is "hers." This is an instance of uncertainty about the point of intervention, a feature the general recipe must allow for.

### 5.5 Death in Damascus

Death predicts the agent perfectly, so Death's location is a child of $\textsc{fdt}$.

- $do(\text{Aleppo})$: Death is in Aleppo, and the agent dies having paid \$1,000.
- $do(\text{Damascus})$: Death is in Damascus, and the agent dies without paying.

A-FDT stays, at no instability cost. CDT's hypotheticals hold Death's location fixed, which produces the Gibbard–Harper oscillation. The paper adds a further point. CDT, even with ratification, treats a genuinely random coin offering a 50% escape as not worth \$1. A-FDT correctly sees the coin as raising survival from 0 to ½.

## 6. What Equation (4) leaves open

### 6.1 Where does $G$ come from?

The authors are explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) works "*given* a graph that accurately describes how changing the value of a logical variable affects other variables."

My recipe's rule, "arrows to every process that computes or models the function," is a reasonable working criterion. It does not settle the harder cases:

- *partial* similarity, such as a twin who reasons almost but not exactly as you do;
- predictors that model a coarse-grained version of your algorithm;
- algorithms that are logically related without being identical.

A natural graded proposal is to give an arrow with a noise parent whose reliability equals the modeled accuracy, as the paper does with $\textsc{Accurate}$. This is an additional assumption, not something the source supplies.

### 6.2 Actions versus policies: the role of the other nodes

Equation (4) intervenes on **one** node, $\textsc{fdt}_x$. Every other $\textsc{fdt}_y$ keeps its prior distribution. In the paper's examples the priors ($q$ above) do not affect the answer. The authors note: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

A minimal example of my own shows *how* it can make a difference.

> **Coordination across inputs.** Two exact copies of the agent are in separate rooms. One is shown a red card and the other a blue card, and both know the protocol. Each chooses $A$ or $B$. Each copy receives 2 if both choose $A$, 1 if both choose $B$, and 0 otherwise.

The copies run the same algorithm on *different* inputs. The red copy intervenes on $\textsc{fdt}_{\text{red}}$ while holding $r=P(\textsc{fdt}_{\text{blue}}=A)$ fixed:

$$
\mathbb E(V\mid do(\textsc{fdt}_\text{red}=A)) = 2r,\qquad \mathbb E(V\mid do(\textsc{fdt}_\text{red}=B)) = 1-r.
$$

So A-FDT chooses $A$ iff $r>1/3$, and the blue copy reasons symmetrically. Suppose the agent's self-model confidently predicts $B$. Then both copies choose $B$, the prediction is borne out, and each receives 1.

Policy-selecting FDT intervenes on the whole map $\pi:\{\text{red},\text{blue}\}\to\{A,B\}$ at once and picks $\pi\equiv A$, for a payoff of 2.

The general lesson, in my terms: an A-FDT agent with correct self-beliefs follows a policy that is *person-by-person optimal*. No single input's output can be improved holding the others fixed. Such a policy need not be *globally* optimal. A-FDT therefore inherits, across its own inputs, a mild version of the self-prediction dependence the paper criticizes in EDT.

Two practical guidelines follow. Both are my proposals.

- **Make sure the answer is not an artifact of $q_y$.** When applying Equation (4), verify that the argmax is the same for every $q_y$, as it is in all of the paper's examples. If it is not, report the dependence explicitly.
- **Look for better self-consistent solutions.** Where the answer depends on $q_y$, check whether some self-consistent assignment of the other nodes dominates. If one does, the case is one where A-FDT and policy-selecting FDT may come apart.

### 6.3 Which $P$?

Equation (4) feeds the same $P$ into the expectation and into the node's name. In the transparent Newcomb computation that $P$ is clearly *not* conditioned on "box B full."

My operational reading is this. $P$ is the agent's model of the problem as a whole, as it stood before observations that might themselves depend on her function. Information enters only through the selection of the node. By the lemma in §3, this choice is innocuous whenever observations are not downstream of the agent's function.

The paper footnotes a historical point. Timeless Decision Theory conditioned on evidence *and* switched nodes, creating "a kind of 'double update' which proves harmful in practice." Avoiding that double update is a reason to adopt the reading above.

### 6.4 Counterpossibles, ties, and imperfect knowledge

**Counterpossibles.** Whatever the function actually outputs, it outputs as a matter of logical necessity. The hypothetical "it outputs something else" is therefore counterpossible. The paper calls the lack of an account of counterpossibles "the main drawback of FDT relative to CDT at this time." It argues that the difficulty is "technical rather than philosophical," and that using $do$ on a supplied graph sidesteps it.

**Ties.** Ties in the argmax are not resolved by the paper. A deterministic tie-breaking convention should be fixed, since predictors model the full algorithm.

**Imperfect predictors.** These are handled by noise nodes. The paper's mechanical-blackmail discussion shows how the answer can flip with error rates. With a \$1,000 demand against \$1,000,000 in damages, the threshold is a false-positive rate of $10^{-3}$. Below it the agent refuses. Above it, a policy of refusing would be triggered too often by mistaken blackmail, and paying becomes better.

## 7. Why act this way? The paper's motivations

The paper's case is primarily performance in "fair" problems. These are problems where outcomes depend only on the agent's behavior in the dilemma, not on which theory produced it. "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*." The authors admit they lack a formal definition of fairness. Footnote 15 notes that simply punishing anyone who acts like a copy of Fiona already causes trouble.

Supporting arguments:

- **Precommitment.** CDT and EDT agents would pay to bind themselves to one-box or to pay the driver, while A-FDT agents act that way without binding.
- **Value of information.** EDT can expect information to hurt it, as when it would pay to blindfold itself in transparent Newcomb.
- **Reflective stability.** CDT recommends self-modifying away from CDT for future problems.
- **Dominance is not neutral.** Each way of constructing hypotheticals induces its own dominance notion. Two-boxing "dominates" only relative to CDT counterfactuals, and under subjunctive-dependence counterfactuals A-FDT never picks a dominated option.
- **Control is equally puzzling for CDT.** A deterministic CDT agent "controls" its token no more coherently than A-FDT "controls" its type.

The paper also takes up the charge that refusing blackmail while holding the letter is odd. Its reply is the "global perspective": the agent should ask what the whole universe would look like if her algorithm behaved differently, and accept hypotheticals in which her observations differ.

## 8. Conclusion

A-FDT, as given by Equation (4), is CDT with two substitutions:

1. intervene on the logical node "output of this algorithm on this input" instead of the physical act;
2. let observations choose *which* node to intervene on instead of conditioning on them.

Once the model is set up, applying it is mechanical. Build a graph in which every implementation or reliable model of the function at input $y$ descends from $\textsc{fdt}_y$, and mere correlates do not. Wire the act as a selector on the observation. Intervene, propagate, and compare expectations. Done this way, it one-boxes, smokes, pays the driver, refuses XOR and mechanical blackmail, cooperates with twins, and stays in Damascus.

What Equation (4) does not supply is just as important:

- a method for constructing the subjunctive-dependence graph;
- a semantics for counterpossibles;
- a treatment of the other $\textsc{fdt}_y$ nodes, which in coordination problems across inputs can lock the action version into an inferior self-consistent policy that the authors' preferred policy-selecting formulation would avoid.

A careful user should treat these as explicit modeling choices and check that conclusions are robust to them.

## References

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Soares, N. & Fallenstein, B. (2015). Toward Idealized Decision Theory. arXiv:1507.01986.