# Action Functional Decision Theory: Choosing the Output, Not the Act

## 1. Introduction

Expected utility maximization is the shared skeleton of modern decision theory. Every serious contender—causal decision theory (CDT), evidential decision theory (EDT), and the theory I will expound here, **action functional decision theory (A-FDT)**—agrees that a rational agent should execute an action that maximizes expected utility. Where the theories disagree is on a prior question: *from which epistemic perspective should each candidate action be evaluated?* As Joyce puts it (quoted in the source), "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

A-FDT answers that question as follows. The agent's deliberation is an implementation of a fixed mathematical function—one that takes beliefs, observations, and goals as input and returns an action as output. The normative question the agent should ask is not "which physical act would cause the best outcome?" (CDT) nor "which act would be the best news?" (EDT), but rather: **which output of this very function would yield the best outcome?** When the agent evaluates an alternative action, she evaluates it as an alternative *output of her decision function*, holding fixed everything that does not depend—causally, logically, or mathematically—on that function's output, and varying everything that does.

The payoff of this seemingly subtle shift is substantial. A-FDT agents one-box in Newcomb's problem, smoke in the smoking lesion problem, pay the driver in Parfit's hitchhiker problem, refuse blackmail that CDT and EDT both succumb to, and cooperate with psychological twins—all from a single decision rule with no precommitment machinery, ratification procedures, or probability kinematics.

This essay develops the theory formally (Section 2 introduces subjunctive dependence; Section 3 gives the core equation), works through canonical examples (Sections 4–5), diagnoses why CDT and EDT fail where A-FDT succeeds (Section 6), and closes with philosophical assessment and open problems (Section 7). Throughout, "the source" refers to the paper by Yudkowsky and Soares on which this account is based; where I go beyond it, I will say so.

## 2. Subjunctive Dependence

The intuitive core of A-FDT is that some things "depend" on your future action in a way that outruns both causation and mere correlation. Call this **subjunctive dependence**.

**Definition (informal).** *Two physical processes that compute the same mathematical function have behaviors that subjunctively depend upon that function: had the function's output been different, both processes' outputs would have been different.*

The canonical image is two well-functioning calculators on opposite sides of the globe, each computing 6288 + 1048. If one outputs 7336, you can be nearly certain the other does too. This is not because either calculator *causes* the other's output, and not (primarily) because they share historical causes—two alien species could independently discover arithmetic. The dependence runs through the mathematical function itself: insofar as both calculators compute it without error, their outputs are logically constrained to agree.

Three contrasts sharpen the notion:

1. **Causal dependence is a special case.** A scribe watching the Parisian calculator writes down its output. Her inscription is both causally and subjunctively dependent on the calculator's output: if it had output something else, she would have written something else. So the framework subsumes ordinary causation.

2. **Mere statistical correlation is not subjunctive dependence.** If the Parisian calculator happens to be pink and the Tokyo one happens to be pink, there is no subjunctive dependence between the colors: had one been green, the other would still be pink. Nothing about the *fact* of the color depends on any shared computation.

3. **Prediction is a middle case.** A Newcomb predictor builds a representation of the agent—a mental model, notes, or a simulation—and bases her prediction on that representation's properties. In the limit of a perfect model of a deterministic agent, the prediction and the action are outputs of effectively the same computation, like the two calculators. Imperfection weakens but does not eliminate the dependence, exactly as a cosmic ray might make one calculator err without breaking the presumption that the other agrees.

Using this notion, the source offers a memorable slogan: **A-FDT is to subjunctive dependence as causal decision theory is to causal dependence.** A CDT agent weighs options by considering scenarios in which her *action token* changes and everything causally downstream changes, with all else fixed. An A-FDT agent weighs options by considering scenarios in which the *output of her decision function* changes and everything that subjunctively depends on that output changes, with all else fixed. In Peirce's type–token terminology: CDT intervenes on the token "my action is *a*"; A-FDT intervenes on the *type*.

Note immediately why this handles the Newcomb/lesion asymmetry. The predictor *represents* the agent's decision function and reasons about it, so the box's contents subjunctively depend on the function's output. The carcinogenic lesion does no such computation; the smoking–cancer correlation is merely statistical, mediated by a common cause with no representational relationship to the agent. So an A-FDT agent imagines the prediction changing with her choice, but not the cancer.

There is an honest cost here. If a decision function outputs *cooperate* on a given input, it does so of logical necessity—there is no possible world in which it outputs *defect* on that same input, any more than there are worlds where 6288 + 1048 ≠ 7336. So A-FDT counterfactuals are **counterpossibles**: their antecedents run contrary to logic. I return to this in Sections 3 and 7.

## 3. The Formal Theory

### 3.1 The shared expected-utility framework

Following the source (drawing on Gibbard and Harper), all three theories maximize a quantity of the form

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j;\, x)\cdot \mathcal{U}(o_j), \tag{1}$$

where $o_1, o_2, \ldots$ are outcomes in a countable set $\mathcal{O}$, $a$ ranges over a finite action set $\mathcal{A}$, $x$ is an observation history, $P(a \hookrightarrow o_j;\, x)$ is the probability that $o_j$ obtains in the hypothetical scenario where action $a$ is executed after observations $x$, and $\mathcal{U}$ is a bounded real-valued utility function. The connective $\hookrightarrow$ is the free parameter: EDT reads it as Bayesian conditioning, CDT as a causal intervention, A-FDT as a *logical* intervention.

### 3.2 Hypotheticals as computational objects

The source offers a useful implementation-level picture. An agent maintains a world-model $M$—a full Bayesian distribution, a neural network's approximate distribution, or something else. For each candidate action $a$, she constructs a **hypothetical** $M^{a\hookrightarrow}$: a transient, scratch-paper object representing "how the world would look if she took action $a$." She then computes an expected utility $V_a$ from each hypothetical and executes the argmax. Hypotheticals are not beliefs and not possible worlds; they are decision-theoretic instruments. The three theories differ only in (i) how $M$ is represented and (ii) how $M^{a\hookrightarrow}$ is constructed from $M$.

For reference, EDT and CDT in this framework are:

$$\mathrm{EDT}(P, x) \coloneqq \argmax_{a}\, \mathbb{E}(V \mid \mathrm{Obs}=x, \mathrm{Act}=a) \tag{2}$$

$$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a}\, \mathbb{E}(V \mid \mathtt{do}(\mathrm{Act}=a), \mathrm{Obs}=x) \tag{3}$$

where in (3), following Pearl, $M = (P, G)$ is a causal theory: $P$ a distribution and $G$ a causal graph. The $\mathtt{do}$ operator sets $\mathrm{Act}=a$ and propagates updates along outgoing arrows only, severing all other correlations with $\mathrm{Act}$.

### 3.3 The A-FDT equation

A-FDT requires that the world-model contain variables representing the outputs of mathematical functions—including, crucially, a variable $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the A-FDT procedure itself when run on inputs $(P, G, x)$. (Underlines denote dequoting: the variable's *name* mentions the model; its *value* is the action the procedure will output.) The self-reference is harmless by Kleene's second recursion theorem: one can construct data structures containing accurate representations of themselves, and the agent needs a variable *representing* the output without knowing its value.

One might hope to define A-FDT via a $\mathtt{true}$ operator—conditioning on the logical sentence "$\mathrm{fdt}(\underline P,\underline G,\underline x) = a$" directly—but the source notes it is unclear how to define such an operator. Instead, mirroring CDT's requirement that $P$ be augmented with causal structure, A-FDT requires that $P$ come augmented with a graph $G$ describing the broader logical/mathematical/computational/causal dependency structure: for each logical variable, how changing its value affects other variables. Then Pearl's $\mathtt{do}$ operator applies verbatim. The primary formal presentation of A-FDT is:

$$\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}}\; \mathbb{E}\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P, \underline G, \underline x) = a\big)\Big). \tag{4}$$

Two differences from Equation (3) carry all the content:

1. **The intervention point.** CDT intervenes on the node $\mathrm{Act}$ representing a physical fact about how the agent's body behaves. A-FDT intervenes on the node representing a *logical* fact about how the decision function behaves. Everything subjunctively downstream of that function's output—propagating along arrows in $G$—varies with the intervention; everything else is held fixed.

2. **The treatment of observation.** CDT responds to a new observation by Bayesian conditioning on it. A-FDT responds by *changing which node it intervenes on*: from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$ when the observation history updates from $x$ to $y$. This is because the observation itself is (often) a subjunctive consequence of the function's behavior—a predictor's message, a transparent box's visible contents—so the observation is downstream of the intervention point in $G$.

**Agreement and divergence.** In models where all correlations between $\mathrm{Act}$ and other variables are (per $G$) caused by $\mathrm{Act}$—except possibly the dependency running through the decision function itself—equations (2), (3), and (4) coincide:

$$\mathbb{E}[V \mid a] = \mathbb{E}[V \mid \mathtt{do}(a)] = \mathbb{E}[V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=a)].$$

They diverge precisely when events correlate with the action without being caused by it—which is exactly the Newcomblike case. Since Joyce's representation theorem applies to any expected-utility theory differing only in constraints on the epistemic perspective of the hypotheticals, A-FDT inherits it, standing to CDT as a cousin that additionally requires hypotheticals to respect *logical* constraints.

## 4. Worked Examples

I now apply Equation (4) in the source's style: give the agent a model $(P^F, G^F)$, evaluate the equation, and read off the action. Throughout, "Fiona" is the A-FDT agent.

### 4.1 Newcomb's Problem

A reliable (99%) predictor has filled box B with \$1,000,000 iff she predicted the agent would leave behind box A (containing \$1,000). Both CDT and A-FDT use models over variables $\{$Predisposition (or $\mathrm{fdt}(\cdot)$), Act, Prediction, Accurate, Box B, Outcome, $V\}$; the difference is the graph and the intervention point.

- **CDT's graph:** Predisposition → Act and Predisposition → Prediction; Accurate → Prediction; Prediction → Box B; Act → Outcome ← Box B. Intervening $\mathtt{do}(\mathrm{Act}=\text{onebox})$ leaves Box B untouched, so two-boxing is worth \$1,000 more in every state. CDT two-boxes; predicted as a two-boxer, it walks away with \$1,000.

- **A-FDT's graph:** the root node is $\mathrm{fdt}(\underline{P^F},\underline{G^F})$ itself, with arrows to Act and to Prediction (the predictor's model of the agent computes the same function, hence subjunctively depends on the same output). Then:

$$\mathbb{E}[V \mid \mathtt{do}(\mathrm{fdt}=\text{onebox})] = 0.99 \cdot \$1{,}000{,}000 = \$990{,}000,$$
$$\mathbb{E}[V \mid \mathtt{do}(\mathrm{fdt}=\text{twobox})] = 0.01 \cdot \$1{,}001{,}000 = \$11{,}000.$$

A-FDT one-boxes. In words: "If this very decision procedure outputs *onebox*, my body takes one box and the box is likely full. If it outputs *twobox*, my body takes two boxes and the box is likely empty. I prefer the first, so this procedure hereby outputs *onebox*."

Crucially, no retrocausation is being posited. The agent fully believes the prediction happened in the past; she simply refuses to imagine her action changing *without* the prediction changing, since both are logical outputs of (representations of) the same function—like two calculators that must agree.

**On dominance.** The two-boxer's dominance argument assumes CDT-style counterfactuals: hold the prediction fixed, vary the act. But that is precisely to imagine the physical action changing while the decision function's behavior is held constant—as odd as asking a working calculator to output 3159 while 6288 + 1048 remains 7336. Every method of constructing hypotheticals generates its own dominance relation (conditional on $a$, "refrain" dominates in the smoking lesion!), so dominance is not a neutral arbiter between theories. The source's preferred metric is utility achieved.

### 4.2 The Smoking Lesion Problem

Smoking is correlated with fatal cancer solely via a common cause (a lesion that causes both the craving and, 99% of the time, cancer). Smoking is worth \$1,000; surviving cancer is worth \$1,000,000.

Here A-FDT's graph *differs* from its Newcomb graph—this is the theory's key flexibility. Whether cancer metastasizes does not depend on the agent's decision function, so the node $\mathrm{fdt}(\cdot)$ connects to Act but not to Cancer. Formally, the source models the agent as uncertain which utility function she has ($\mathcal{U}_S$, which values smoking at +\$1,000, or $\mathcal{U}_R$, which discounts it), with $\mathrm{Act}$ determined by $\mathrm{fdt}(\underline{P^F_S},\underline{G^F})$ or $\mathrm{fdt}(\underline{P^F_R},\underline{G^F})$ according as the lesion is present. Intervening on $\mathrm{fdt}(\underline{P^F_S},\underline{G^F})=\text{smoke}$ leaves $\Pr(\text{lesion}) = p$ unchanged, so

$$\mathbb{E}[\text{smoke}] - \mathbb{E}[\text{refrain}] = p \cdot \$1{,}000 > 0,$$

and Fiona smokes. One compact rule delivers both one-boxing and smoking—the combination Gibbard and Harper argued impossible.

(The source is candid that this problem is contrived—the agent is uncertain of her own desires—and that the standard distribution "lies to" the EDT agent if she lives among EDT agents who mostly don't smoke. It treats the lesion problem for historical reasons and recommends the XOR blackmail problem, below, as the cleaner test.)

### 4.3 Parfit's Hitchhiker and the Transparent Newcomb Problem

In Parfit's hitchhiker, a driver with 99%-accurate lie detection rescues the agent iff she predicts the agent will pay \$1,000 upon reaching the city. CDT and EDT both defect on the payment—given arrival, paying is pure loss—and hence, being predictably defectors, are left in the desert. The A-FDT agent intervenes on $\mathrm{fdt}(\underline{P^F},\underline{G^F},\text{city})$; the hypothetical where this function outputs *refuse* is a world where the driver predicted refusal and left her to die. Paying wins: expected value ≈ \$990,000 versus ≈ −\$1,000,000 plus scraps.

The transparent Newcomb problem makes the observation-handling difference vivid. Both boxes are visible; suppose the agent *sees* box B is full. CDT conditions on Obs = full and intervenes on Act, keeping Box B = full: two-boxing nets \$1,001,000 > \$1,000,000. EDT, conditioning on both the full box and the action, also two-boxes. A-FDT instead intervenes on $\mathrm{fdt}(\underline{P^F},\underline{G^F},\text{full})$—the output of the procedure that runs *upon seeing a full box*—and this node subjunctively controls the prediction, hence (via Accurate) what the agent likely saw in the first place. The hypothetical where it outputs *twobox* is mostly a world where the agent saw an *empty* box (because the predictor predicted two-boxing): expected value \$110,00-ish per the source's arithmetic (0.01·\$1,001,000 + 0.99·q·\$1,000), versus \$990,000 + 0.01·q·\$1,000 for one-boxing. One-box, even staring at a full box.

This is not ignored information. The A-FDT agent *does* respond to evidence—by switching which node she intervenes on. If she had seen an empty box, she would intervene on $\mathrm{fdt}(\underline{P^F},\underline{G^F},\text{empty})$ (and there take the \$1,000, since that observation is not reward-contingent in the same way). The general lesson the source draws: **an agent should entertain the hypothesis that, if her action were different, she might have made different observations.**

One-boxing in the transparent case is *exactly* paying the hitchhiker, and the source supports it with three arguments: (i) **precommitment**—CDT and EDT agents would both precommit to one-box if they could, and predictably acting as one would have precommitted is the cheap way to get precommitment's benefits; (ii) **value of information**—EDT agents in transparent Newcomb would *pay to blindfold themselves*, since seeing the box harms them; A-FDT agents never assign negative value to information; (iii) **utility**—predictors fill boxes only for predictable one-boxers, so A-FDT agents get rich and the others mostly stare at empty boxes.

### 4.4 Blackmail: A-FDT as extortion-resistance

In **XOR blackmail**, a predictor sends a letter iff either (i) the house has no termites and the agent will pay \$1,000, or (ii) it has termites and she won't. EDT agents pay—conditioning on paying makes termites improbable, delicious news—and are thus endlessly exploitable by anyone who can manufacture correlations between their actions and good news. CDT refuses (infestation is causally upstream), but for a revealing reason: Carl's hypothetical has the inerrant predictor *erring*.

The A-FDT agent refuses, via the same structure as transparent Newcomb: intervening on $\mathrm{fdt}(\underline{P^F},\underline{G^F},\text{letter}) = \text{refuse}$ yields a world where the predictor predicted refusal, sent no letter, and (if termites exist) she simply loses the \$1,000,000 she was probably going to lose anyway—versus a *pay* world where she is predictably a payer, gets letters exactly when termite-free, and bleeds \$1,000 each time. The same analysis applies to **mechanical blackmail**, where payment is causally necessary to stop an already-launched program; Fiona refuses even while holding the letter, even knowing the imperfect blackmailer mispredicted, because being *the kind of agent* who refuses means rarely facing the dilemma at all. The source reports the break-even error rate explicitly: with 0.09% misprediction she refuses; at 0.011% she pays. Notably, A-FDT appears **reflectively stable** in these fair problems: holding the letter, Fiona has no desire to temporarily switch to CDT, since a theory that pays under blackmail gets blackmailed more.

### 4.5 Death in Damascus

An inerrant predictor-Death will meet the agent wherever she goes tomorrow; fleeing costs \$1,000. CDT is famously "unstable" here: expecting to stay, it flees; expecting to flee, it stays—cycling, or settling into a ~50/50 ratification at which it values a truly random \$1 coin (which would genuinely grant 50% survival) at less than a dollar, because its hypotheticals treat its location and Death's as independent. The A-FDT agent simply intervenes on her decision function's output, imagines Death's book changing to match, and stays put—saving \$1,000 in a lost cause.

## 5. How to Apply A-FDT to an Unfamiliar Problem

For the practicing reader, the source's method reduces to a recipe:

1. **Build the model.** Construct $P$ covering all decision-relevant variables, including a logical variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ (and, if observations vary, one per observation-history: $\mathrm{fdt}(\underline P,\underline G,\text{full})$, $\mathrm{fdt}(\underline P,\underline G,\emptyset)$, etc.).
2. **Draw the dependency graph $G$.** Connect $\mathrm{fdt}(\cdot)$ by arrows to every variable whose value would change *if the function's output changed*: the agent's physical act; other agents' acts *if* they implement or model the same function (twins, predictors, simulators, ratifiers of contracts); predictors' outputs; and observations whose occurrence is contingent on the predicted action. Do *not* connect it to variables related to the act only by common causes or chance (the lesion, the weather, the coin that landed heads).
3. **Intervene and compare.** For each candidate $a$, compute $\mathbb{E}[V \mid \mathtt{do}(\mathrm{fdt} = a)]$ by Pearl propagation, and take the argmax per Equation (4).
4. **Check the intervention point against observations.** If you have observed $x$, intervene on the function-with-input-$x$ node; do not additionally condition on $x$ inside the hypothetical if $x$'s occurrence itself subjunctively depends on the function.

Two modeling subtleties deserve emphasis. First, the graph $G$ encodes the agent's *beliefs* about dependency structure, and the analysis assumes accurate beliefs; a model misdescribing the predictor changes the prescription accordingly. Second, step 2 is where all the judgment lives: deciding whether a given real-world correlational partner of your action is "predictor-like" or "lesion-like" is exactly the question of whether it subjunctively depends on your decision function.

## 6. What the Source Leaves Open, and How I Suggest Reading It

**The graph-construction problem.** The source is explicit that this is "perhaps the largest open problem": Pearl gave a compelling account of *deducing causal* structure from observation and experiment, but no analogous formal treatment exists for deducing *logical/subjunctive* structure. Equation (4) takes $G$ as an input, just as CDT takes $G$ as an input; but we lack the learning theory for the broader graph. Nothing in this essay resolves that; any practical application of A-FDT currently requires the dependency structure to be supplied by the modeler.

**Counterpossible reasoning.** Because the antecedent $\mathrm{fdt}(\underline P,\underline G,\underline x) = a$ is (for the actual $a$) logically false, the hypotheticals are counterpossibles. The source argues this difficulty is technical rather than philosophical: humans reason comfortably under logical uncertainty (e.g., about the twin prime conjecture), and A-FDT agents need only a narrow class of counterpossible questions ("how would this predictor's prediction change if this function had a different output?"). A tempting escape—evaluate alternative *decision functions* rather than alternative outputs of one function—fails, as the source shows: to keep predictors' behavior consistent, the variant must imagine predictors predicting differently about the original function, which reinstates the counterpossibles. My suggested operational reading, consistent with the source's footnotes, is that the $\mathtt{do}$-based equation is best understood as an idealization: a fully satisfactory implementation would condition probabilities on uncertain logical facts (a "logical induction"-style reading of $\mathbb{E}[V \mid \mathrm{fdt}(\cdot)=a]$), with the interventionist Equation (4) as the computable surrogate once $G$ is given.

**Actions vs. policies.** Footnotes in the source indicate that the authors' preferred formalization intervenes on a *policy*—a mapping from observations to actions—rather than on action-per-observation nodes. Equation (4), our assigned formalization, is the action-level version; the difference "only matters in multi-agent dilemmas so far as we can tell."

**Fairness.** No decision theory wins in all possible dilemmas—one can always build a game that punishes a given procedure by name. The source conjectures A-FDT matches or beats all rivals on all *fair* problems—those where the agent's beliefs are accurate and outcomes depend only on the agent's behavior in the dilemma at hand, so that "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*"—but a formal criterion of fairness remains open (the source notes, e.g., the difficulty of constructing problem-analogies that are unfair to rival theories in a principled way).

## 7. Conclusion

Action functional decision theory is a one-parameter amendment to causal decision theory: intervene not on the physical act but on the logical output of the decision procedure itself, and preserve, in your hypotheticals, all and only the dependencies that run through that output. Where EDT's hypotheticals respect too many correlations (managing the news, paying blackmailers, refusing to smoke), and CDT's respect too few (imagining inerrant predictors erring, defecting against twins, fleeing Death), A-FDT's hypotheticals preserve exactly the decision-relevant subjunctive dependencies—and so it one-boxes, smokes, pays the hitchhiker, votes with like-minded coalitions, keeps gym resolutions, resists extortion, and coordinates with its own future selves, all by asking a single question: *what would the universe look like if this very function output something else?*

The theory's costs are real: it rests on counterpossible conditionals, requires a dependency graph we do not yet know how to learn, and issues prescriptions (pay the driver; leave the visible \$1,000) that many find intuitively strange. But its credentials are equally real: a single elegant rule, endorsed by Joyce's representation-theoretic framework, with no known fair dilemma in which it loses to a rival. If our best theory of rational choice should be the one that gets its adherents the most of what they want, A-FDT is currently the leading candidate.

### References

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060. (The source for this essay; Equation (4) of its Section 5 is the formal basis of A-FDT as presented here.)
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference.* Cambridge University Press.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory.* Cambridge University Press.
- Gibbard, A. & Harper, W. L. (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory.*
- Nozick, R. (1969). "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel.*
- Kleene, S. C. (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3.
- Lewis, D. (1979). "Prisoners' Dilemma is a Newcomb Problem." *Philosophy & Public Affairs* 8.
- Soares, N. & Fallenstein, B. (2015). "Toward Idealized Decision Theory." arXiv:1507.01986.