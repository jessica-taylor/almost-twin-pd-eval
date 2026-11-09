# A-FDT: Choosing the Output of a Function

## 1. The idea in one paragraph

Action functional decision theory (A-FDT) is the decision procedure given by Equation (4) of Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. The paper calls the theory simply "FDT". I write **A-FDT** for the action-level rule in Equation (4). The paper's footnotes 7 and 16 say its authors' preferred formalization selects *policies* (maps from observations to actions), and that the difference "only matters in multi-agent dilemmas so far as we can tell". I discuss that only briefly.

A-FDT is an expected-utility theory. It differs from causal decision theory (CDT) and evidential decision theory (EDT) only in how it builds the hypothetical scenario for each action. A-FDT does not ask "what if my body did this?" (CDT) or "what would it say about the world if I did this?" (EDT). It asks, in the paper's words, "Which output of this very function would yield the best outcome?" Everything else in the theory follows from taking that question literally.

Below I set up the formalism, state Equation (4) and unpack it, work the standard cases, and then address what the paper leaves open. I mark my own additions and examples as such.

## 2. The shared expected-utility skeleton

The paper defines (Equation (1)) expected utility as

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal U(o_j),$$

where $a$ ranges over a finite action set $\mathcal A$, $x$ is an observation history, the $o_j$ are outcomes, and $P(a \hookrightarrow o_j; x)$ is "the probability that $o_j$ will obtain in the hypothetical scenario where the action $a$ is executed after receiving observations $x$". Following Joyce, the paper holds that EDT, CDT, and A-FDT agree on the valuing machinery and disagree only on the "epistemic perspective", that is, on how to read the connective $\hookrightarrow$.

- **EDT** (Equation 2) reads it as conditioning: $\arg\max_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$.
- **CDT** (Equation 3) reads it as Pearl's intervention on the physical action node: $\arg\max_a \mathbb E(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$.
- **A-FDT** (Equation 4) reads it as an intervention on a node representing the *output of the decision function*.

The paper also describes each theory as a pair: a world-model $M$ and a recipe for building a hypothetical $M^{a\hookrightarrow}$ for each action. The agent computes $V_a$ from each hypothetical and takes the maximizer. The paper stresses that hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs", like "notes on scratch paper".

## 3. Equation (4)

$$\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P, \underline G, \underline x) = a\big)\Big).$$

The inputs and symbols are as follows.

- $P$ is a probability distribution over variables of the world. Besides ordinary variables, it contains variables for the outputs of mathematical functions. The paper's example is a variable for $6288+1048$ with nearly all its mass on $7336$.
- $G$ is a graph saying how changing a logical variable changes the other variables. Pearl's $\mathrm{do}$ operator needs the same kind of structure. $G$ must encode "logical, mathematical, computational, causal, etc. structure", not just causal structure.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model representing what A-FDT returns when run on that model and that observation. The underlines mean dequoting: $\mathrm{Z}\underline{x}$ with $x=3$ denotes the variable named $\mathrm{Z}3$.

The $\mathrm{do}$ operation sets the node to $a$, then recomputes every variable downstream of it according to $G$ and leaves everything else untouched. Downstream includes the agent's own body, any predictor that models the agent, and any twin running the same computation.

### Two differences from CDT

The paper identifies exactly two differences from Equation (3).

1. **Where the intervention happens.** CDT intervenes on $\mathrm{Act}$, a physical fact about the agent's body. A-FDT intervenes on $\mathrm{fdt}(\cdot)$, a logical fact about the agent's decision function. In Peirce's terms, CDT intervenes on the token and A-FDT on the type.
2. **How observation enters.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. A new observation changes *which node is intervened on*: from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. This is why the paper says A-FDT "responds to observation by changing which node it intervenes upon".

The second difference is easy to miss, and it matters. Equation (4) as printed has no $\mathrm{Obs}=x$ on the right of the bar. In the transparent Newcomb calculation the paper writes $\mathbb E(V\mid \mathrm{do}(\mathrm{fdt}(\cdot,\text{full})=a, \mathrm{Obs}=\text{full}))$, but its numbers show that the observation is *not* used to discard worlds. The inaccurate-predictor world, in which the agent would have seen an empty box, still contributes. My reading is that in A-FDT the observation determines the index of the intervened node and does not filter the worlds being averaged over. I think this is the faithful reading, because any other reading would reproduce the "update on the full box" behaviour the paper attributes to CDT and EDT.

### Self-reference

The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ has a name that depends on the model that contains it. The paper says this is harmless. The agent need not know the *value* of the function's output to have a variable *representing* it, and Kleene's second recursion theorem ("quining") shows how a program can hold an accurate representation of itself.

### What the intervention means

Since the function really does output one value on that input, the intervention is a counterpossible: it supposes something false by logical necessity. The paper compares it to imagining a calculator outputting $3159$ for $6288+1048$. Equation (4) avoids defining a general counterpossible operator. The paper notes that no definition of a "$\mathtt{true}$" operator is available, so it takes the dependence structure $G$ as an *input*, just as CDT takes causal structure as an input. The theory therefore relocates the hard part into $G$ (section 7 below). It does not dissolve it.

### Agreement with CDT and EDT in easy cases

If all correlations between the action and other variables are caused by the action, except possibly the dependence on the decision function itself, then
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)].$$
The theories diverge only when something correlates with the action without being caused by it, typically because another agent is modelling you.

## 4. Subjunctive dependence

A-FDT's graph edges are not statistical correlations. The paper defines *subjunctive dependence*: two physical systems computing the same function have behaviors that subjunctively depend on that function. This yields the slogan: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

Three observations from the paper help in using the notion.

- **Causal dependence is a special case.** If a scribe copies a calculator's display, what she writes depends causally *and* subjunctively on its output.
- **Statistical correlation is not enough.** If two calculators are both pink by coincidence, then "if the scribe had bought a green calculator instead, the one in Tokyo would still be pink". That is no subjunctive dependence.
- **Imperfection weakens but does not remove it.** An imperfect predictor, or a noisy agent, gives a weaker dependence, modelled with a noise variable (in the paper, $\mathrm{Accurate}$ with probability 0.99).

A graph encodes this by drawing arrows from the $\mathrm{fdt}$ node to everything that implements or accurately models the function, and *not* to variables that merely correlate with the output through a common cause.

## 5. How the rule works: worked cases

### Newcomb's problem

In Fiona's graph (Figure 4b in the paper), $\mathrm{fdt}$ feeds both $\mathrm{Act}$ and $\mathrm{Prediction}$. Noise $\mathrm{Accurate}$ is true with probability 0.99, and $\mathrm{Prediction}$ fills box B iff it predicts one-boxing.

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$: act is one-box, box full with probability 0.99, so $\mathbb E V = 0.99\cdot 1{,}000{,}000 = \$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$: box full with probability 0.01, so $\mathbb E V = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1000 = \$11{,}000$.

A-FDT one-boxes. The paper's own text gives $\$999{,}000$ for the EDT one-box value. By my arithmetic it should be $\$990{,}000$, matching Fiona's figure, so I take that as a typo.

The usual objection is that Fiona believes the box is already full, so she should take the free \$1,000. The paper's answer is that she evaluates "what if I two-boxed?" by supposing the function output something else, and in that supposition the predictor's model of her also outputs something else. No retrocausal physics is involved, only a refusal to imagine "her action changing without also imagining $\mathrm{fdt}$ taking on a different value".

### Smoking lesion

Here the lesion is a common cause of the desire to smoke and of cancer. It does not model the agent's decision function. The graph therefore has no arrow from the $\mathrm{fdt}$ node to $\mathrm{Cancer}$. The paper adds a wrinkle: the lesion determines the agent's utility function ($\mathcal U_S$ if lesion, $\mathcal U_R$ otherwise). So there are two decision-function nodes, $\mathrm{fdt}(\underline{P_S},\underline G)$ and $\mathrm{fdt}(\underline{P_R},\underline G)$, and $\mathrm{Act}$ takes whichever one the lesion variable selects. Intervening on the $S$-node leaves $P(\text{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1000$, so A-FDT smokes. The same rule one-boxes and smokes; only $G$ differs.

### Transparent Newcomb and Parfit's hitchhiker

Because observation selects the node, Fiona facing a full box intervenes on $\mathrm{fdt}(\cdot,\text{full})$. In her graph, $\mathrm{Prediction}$ selects which node, $\mathrm{fdt}(\cdot,\text{full})$ or $\mathrm{fdt}(\cdot,\text{empty})$, controls $\mathrm{Act}$. Let $q$ be her prior probability of two-boxing on seeing an empty box. I recompute the values:

- Setting the full-box output to one-box: $0.99\cdot 1{,}000{,}000 + 0.01\cdot 1000q = 990{,}000+10q$.
- Setting it to two-box: with probability 0.99 the box is empty and her action comes from the other node, giving $0.99\cdot 1000q$. With probability 0.01 the prediction erred, the box is full, and she two-boxes for \$1,001,000. The total is $10{,}010+990q$.

(The paper prints this second figure as "$\$110{,}00 + q\cdot\$990$", which looks like a typo.) One-boxing wins for every $q\in[0,1]$. When she envisions two-boxing, she envisions probably seeing an empty box. The paper argues this is the same structure as Parfit's hitchhiker, so A-FDT pays the driver.

### Blackmail

In the XOR blackmail, the termite infestation is not downstream of the $\mathrm{fdt}$ node. The letter's *existence* is downstream of it, since the predictor sends the letter based on what the function does on seeing it. Intervening on "pay" changes the probability of receiving the letter but not the infestation, so A-FDT refuses.

In the mechanical blackmail with a fallible predictor, let $\varepsilon$ be the probability that the blackmailer wrongly predicts "pays".

- Under $\mathrm{do}(\text{pay})$ she is always blackmailed and loses \$1,000.
- Under $\mathrm{do}(\text{refuse})$ she is blackmailed with probability $\varepsilon$ and then loses \$1,000,000, an expected loss of $10^6\varepsilon$.

She refuses iff $10^6\varepsilon<10^3$, i.e. $\varepsilon<0.001$. This matches the paper's numbers: $\varepsilon=0.0009$ gives \$900 against \$1,000 (refuse), and $\varepsilon=0.00011$ is, as the paper says, in the paying regime. Here A-FDT refuses even while holding a letter it knows came from an erroneous prediction. In the paper's words, "it's advantageous to be *the kind of agent* that makes such decisions".

### Death in Damascus

Death's location is downstream of the $\mathrm{fdt}$ node via the appointment book. Staying yields "Death is in Damascus" and saves the \$1,000 camel cost. Fleeing yields "Death is in Aleppo" and costs \$1,000. A-FDT stays, and there is no instability. CDT, by contrast, evaluates each option holding Death's location independent of the action, so its verdict flips with its beliefs about what it will do.

## 6. Why the hypotheticals are built this way

The paper's diagnosis is that EDT "respects too many action–environment correlations" and CDT "too few". Examples:

- **EDT, cosmic ray problem.** If the agent almost always takes \$1, then she takes \$100 "only when hit by cosmic rays", so conditioning makes \$100 look bad. A-FDT and CDT break that merely statistical link.
- **CDT, perfect predictor.** CDT hypotheticals describe a world where an infallible predictor erred exactly at this decision. A-FDT holds the predictor–agent dependence fixed.

The paper also argues that dominance reasoning is theory-relative. "Every expected utility theory comes with its own notion of dominance." A-FDT has its own: an action is dominated if, holding fixed all relevant subjunctive dependencies, switching the function's output from $b$ to $a$ is sometimes better and never worse. By that notion A-FDT never takes a dominated action. The paper's main test is utility achieved on fair problems, in which outcomes depend only on the agent's behavior in the problem and the agent's beliefs are accurate. It concedes that no formal criterion of fairness is yet available, and it says no decision theory wins in unfair problems such as ones that punish its specific algorithm.

## 7. The open question: where does $G$ come from?

The paper is candid. Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables", but "it is not yet clear how to construct such a thing", and it calls this "perhaps the largest open problem in the study of functional decision theory". Footnote 9 notes that an evidential version would need conditional probabilities on false logical sentences, which do not yet exist.

So A-FDT as specified is a *conditional* procedure: correct output given a correct $G$. A user of the theory therefore needs an operational way to write down a $G$. The following is **my proposal**, not the paper's.

**A construction checklist.**

1. *List the computations.* Identify every process in the problem that evaluates the agent's decision function, or contains an accurate model of it. Examples are twins, predictors, a blackmailer's simulation, and the agent's own future selves in similar situations.
2. *Index by input.* For each such process, say what input it runs the function on. A predictor simulating "what you'd do on seeing a full box" depends on $\mathrm{fdt}(\cdot,\text{full})$, not on the node for the observation the agent actually receives. This is what makes the transparent cases come out right.
3. *Add arrows from the $\mathrm{fdt}$ node to those processes' outputs only.* Do not add arrows to variables correlated with the agent merely through a shared cause, such as the lesion or the infestation.
4. *Model fallibility with noise nodes.* The strength of the dependence is the reliability of the model, e.g. $\mathrm{Accurate}$. It is not a stipulation that the dependence is binary.
5. *Say which node controls $\mathrm{Act}$ in each world.* Where the world determines which observation the agent gets, make $\mathrm{Act}$ a function of the relevant nodes, as in the transparent and blackmail graphs.
6. *Diagnostic test.* For each non-agent variable $Z$, ask: "if this computation had been carried out differently, would $Z$ have been different?" If yes, add an arrow. If $Z$ would be the same, as with the pink Tokyo calculator, do not.

The test for step 6 is the paper's own pink-calculator test. The checklist is my attempt to make it procedural. It does not resolve hard cases, such as dependence through a coarse, lossy model of the agent, or a predictor that tracks the agent's *reasons* rather than the function's output.

**A second gap: the other nodes.** When A-FDT intervenes on $\mathrm{fdt}(\cdot,x)$, the nodes for other observations $\mathrm{fdt}(\cdot,y)$ remain as random variables with priors, like $q$ above. In the paper's examples the result is insensitive to $q$. In general it need not be. My suggestion is a consistency requirement: set each such prior to the agent's best estimate of what A-FDT itself would return at that node, solved jointly, or evaluate over the set of such assignments and require robustness. The paper's remark that "the correct value of $q$ is 1" suggests this reading, but it does not give an algorithm. This is also where the policy-level formulation (the paper's footnotes 7 and 16) would make the specification cleaner, since it chooses all of the node values at once.

## 8. A worked example of my own: an imperfectly correlated twin

Suppose your twin runs the *same function* with probability $r$. With probability $1-r$ the twin's choice is independent of yours and cooperates with probability $s$. Payoffs are those of the paper's twin prisoner's dilemma: \$1,000,000 each for mutual cooperation, \$1,000 each for mutual defection, and \$1,001,000 / \$0 for defector / cooperator.

The graph has the $\mathrm{fdt}$ node pointing to your act and, with probability $r$, to the twin's act. Then

$$\mathbb E[V\mid\mathrm{do}(\text{cooperate})]=r\cdot 10^6+(1-r)s\cdot 10^6,$$
$$\mathbb E[V\mid\mathrm{do}(\text{defect})]=r\cdot 10^3+(1-r)\big[s\cdot 1{,}001{,}000+(1-s)\cdot 10^3\big].$$

The difference is
$$999{,}000\,r-1000\,(1-r),$$
which is positive iff $r>1/1000$, independent of $s$. So A-FDT cooperates when it assigns even a 0.1% chance that the other party's behavior is downstream of the same computation, because the stakes of mutual cooperation are so large relative to the \$1,000 gain from defecting. This is a prediction of Equation (4) given the stated $G$. Whether a real counterpart merits $r>0.001$ is exactly the question of constructing $G$ discussed in section 7.

## 9. Philosophical motivation and objections

The paper's central argument is "from utility". A-FDT agents do better in expectation on fair dilemmas, and a theory of rational choice that recommended hiding its own textbooks from loved ones would be strange. It supports this with two corollaries.

- **Precommitment.** A-FDT acts as it would have ideally precommitted to act, without costly binding. The paper calls this "reflective stability in fair problems", whereas CDT recommends self-modifying away from itself.
- **Value of information.** A-FDT never assigns negative expected value to information, since it behaves as it would have precommitted to.

The two natural objections are as follows.

*"A-FDT acts as if it can control logical facts and the past."* The paper responds that a deterministic CDT agent equally "cannot" control its action token. Both theories consult imagined worlds that differ from the actual one, and an objection to "controlling" the decision type would also be an objection to controlling the token.

*"A-FDT ignores the evidence it holds."* The paper replies that A-FDT does respond to evidence, by switching which node it intervenes on. It also notes that early variants combined conditioning with the node switch, creating a "double update" that proves harmful in practice.

My own caution, beyond the paper: the "fair problem" restriction is doing real work. The paper's footnote 15 concedes that a problem which punishes copies for matching a copy of A-FDT is unfair to A-FDT in an uncomfortable way, and it has no principled transformation to the analogous problem for rivals. So the claim of superiority on all fair problems is a conjecture that rests on a not-yet-formalized notion.

## 10. Conclusion

A-FDT, as given by Equation (4), says: build a world-model $P$ with a dependence graph $G$; for each available action $a$, intervene on the node representing the output of this very decision procedure (indexed by the observation received); recompute everything downstream, including predictors, twins, and one's own body; and choose the $a$ with the highest expected utility. It is formally close to CDT, differing in the intervention site and in treating observation as a choice of node rather than a conditioning event. That small change yields one-boxing in Newcomb's problem, smoking in the lesion problem, paying in Parfit's hitchhiker, refusing to be blackmailed, and stable behavior in Death in Damascus.

What the source establishes is the equation, the worked cases, and the argument that these behaviors earn more utility in fair problems. What it does not provide is a method for learning $G$, a formal notion of fairness, or an algorithm for the non-intervened nodes. The checklist and the self-consistency suggestion in section 7 are my attempts to make the procedure usable. They are not part of the theory as published.