# Action Functional Decision Theory: Choosing the Output, Not the Act

## 1. Introduction

Expected utility maximization is the shared skeleton of modern decision theory. Evidential decision theory (EDT) and causal decision theory (CDT) both tell an agent to pick the action with the highest expected utility; they disagree only about what "expected" means—about which conditional probabilities to plug into the expectation. Yet the two standard interpretations perform erratically across classic dilemmas. CDT two-boxes in Newcomb's problem and walks away with \$1,000 where a one-boxer walks away with \$1,000,000. EDT one-boxes but refuses to smoke in the smoking lesion problem, forgoing a free \$1,000 of value. In Parfit's hitchhiker, both are left to die in the desert.

This essay expounds **action functional decision theory (A-FDT)**, in the graphical formalization of Yudkowsky and Soares (2017), whose Equation (4) is our primary definition. A-FDT's central idea: treat your decision procedure as a fixed mathematical function, and choose *which output of that function would be best*—intervening on the logical fact of what the function returns, rather than on the physical fact of what your body does. Causal dependence, on this view, is a special case of a broader relation, *subjunctive dependence*, and A-FDT is to subjunctive dependence what CDT is to causal dependence.

Readers should keep one caveat in mind throughout: the formal core of A-FDT is precise, but one of its inputs—a graph of logical/subjunctive dependencies—lacks a full philosophical foundation analogous to Pearl's theory of causation. I will flag what is source doctrine, what is open, and where I am supplying my own operational gloss.

## 2. The Shared Framework: Expected Utility and Hypotheticals

Following Gibbard and Harper, all three theories maximize

$$\mathcal{EU}(a) \;=\; \sum_{j=1}^N P(a \hookrightarrow o_j \,;\, x)\,\mathcal{U}(o_j),$$

where $o_j$ ranges over outcomes, $a$ over a finite action set, $x$ over observation histories, and $P(a \hookrightarrow o_j; x)$ is the probability of $o_j$ "in the hypothetical scenario where $a$ is executed after observations $x$." Joyce's representation theorem tells us that EDT, CDT, and A-FDT are not rival theories of *value*; they disagree about the epistemic perspective from which actions are evaluated—about the interpretation of the connective $\hookrightarrow$.

A useful computational picture (from the source): an agent maintains a world-model $M$—a probability distribution, possibly augmented with structural information. For each candidate action $a$ she constructs a *hypothetical* $M^{a\hookrightarrow}$, a scratch-paper object representing "how the world would look if I took $a$," and evaluates expected utility in it. The theories differ in exactly two ways: what the model contains, and how hypotheticals are built from it.

- **EDT**: the model is just a posterior distribution $P(- \mid x)$; hypotheticals are formed by Bayesian conditioning. Formally, with $V = \mathcal{U}(\text{Outcome})$:
$$\mathrm{EDT}(P, x) = \arg\max_{a} \mathbb{E}\big(V \mid \text{Obs}=x, \text{Act}=a\big).$$
- **CDT**: the model is a pair $(P, G)$, where $G$ is a Pearl-style causal graph; hypotheticals are formed by the intervention operator $\mathrm{do}$:
$$\mathrm{CDT}(P, G, x) = \arg\max_{a} \mathbb{E}\big(V \mid \mathrm{do}(\text{Act}=a), \text{Obs}=x\big).$$

The $\mathrm{do}(\text{Act}=a)$ operation sets $\text{Act}=a$, propagates the update along causal arrows, and holds everything not causally downstream of $\text{Act}$ fixed. In Newcomb's problem, Box B is causally upstream (or sideways) from the action, so its contents stay put in every CDT hypothetical—and two-boxing wins by \$1,000 in each.

## 3. Subjunctive Dependence

The key intermediate notion is **subjunctive dependence**. When two physical systems compute the same function, their behaviors subjunctively depend on that function: if one calculator evaluating $6288 + 1048$ outputs $7336$, you may reasonably infer the other will too—not because either causes the other, and not merely by statistical coincidence, but because both are constrained by the same mathematical fact. Causal dependence is a special case (a scribe copying a calculator's output is causally *and* subjunctively dependent on it); mere correlation is not (two coincidentally pink calculators share no such dependence).

The crucial asymmetry: Newcomb's predictor contains an accurate *representation* of the agent's decision function—effectively a "twin" inside the predictor's mind—so her prediction subjunctively depends on the agent's decision function's output. A carcinogenic lesion computes nothing about the agent; the smoking–cancer correlation is merely statistical. An A-FDT agent respects the first dependence and breaks the second, and thereby one-boxes *and* smokes with a single rule.

## 4. The Formal Definition: Equation (4)

A-FDT's model is again a pair $(P, G)$, but now $G$ is not a causal graph: it is a broader graph describing how changes in *logical* variables—including variables representing the outputs of mathematical functions—affect other variables. The distribution $P$ must contain variables for the outputs of relevant mathematical functions, e.g. a variable for $6288+1048$ with most of its mass on $7336$.

The theory then intervenes not on the physical act but on the **logical variable representing the output of the A-FDT procedure itself**, evaluated on its own inputs:

$$\boxed{\;\mathrm{A\text{-}FDT}(P, G, x) \;=\; \arg\max_{a \in \mathcal A}\; \mathbb{E}\Big(V \,\Big|\, \mathrm{do}\big(\,\underline{\mathrm{afdt}(\underline{P}, \underline{G}, \underline{x})} = a\,\big)\Big).\;} \tag{4}$$

Here underlines denote *dequoting*: $\mathrm{afdt}(\underline{P}, \underline{G}, \underline{x})$ is a variable *named by* the expression "$\mathrm{afdt}(P,G,x)$"—i.e., a variable in the agent's own model representing what the agent's own decision procedure outputs on the model and observations she currently has. Two features deserve emphasis.

**Self-reference.** The model contains a variable whose name depends on the model. This circularity is harmless: the agent need not know the *value* of $\mathrm{afdt}(P,G,x)$ to have a variable representing it, and Kleene's second recursion theorem ("quining") shows how to build data structures that accurately represent themselves. In practice one might worry about Löbian obstacles to an agent *proving* its own output; the source does not address this, and I flag it as an implementation question beyond the paper's scope.

**Observation handling.** Where CDT responds to an observation by conditioning on $\text{Obs}=x$, A-FDT responds by *changing the node it intervenes on*: from $\mathrm{afdt}(\underline{P}, \underline{G}, \underline{x})$ to $\mathrm{afdt}(\underline{P}, \underline{G}, \underline{y})$ when observations change from $x$ to $y$. This is the mechanism behind A-FDT's "updateless" behavior in blackmail dilemmas (§7).

Note what Equation (4) does *not* do: it does not define the $\mathrm{do}$ surgery over counterpossible antecedents from scratch. Since a deterministic decision function *logically must* output what it outputs, $\mathrm{do}(\mathrm{afdt}(\ldots)=a)$, for the non-actual $a$, runs counter to logic. The source first proposes a $\mathtt{true}$ operator for conditioning on logical sentences, finds it undefinable in full generality, and settles for *assuming* $G$ as an input—exactly as CDT assumes causal structure. The paper also considers a rival, "A-FDT$'$," which instead asks "what if I implemented a *different* decision function $f_n$?" and shows this doesn't help: a predictor predicts the output of your *actual* function $d$, so even A-FDT$'$ must reason counterpossibly about how $d$'s output would differ. The need for counterpossible reasoning is thus ineliminable; the source calls this the theory's main open technical problem, while noting that humans navigate such reasoning with serviceable heuristics.

## 5. Worked Examples

### Newcomb's problem

Let $P$ contain variables Predisposition, Act, Prediction, Accurate (accurate with probability $0.99$), Box B, Outcome, $V$. The predictor fills Box B iff she predicts one-boxing; Prediction is a deterministic function of (Predisposition, Accurate).

- **EDT** conditions on Act. Conditioning on *onebox* makes Box B $99\%$ likely full: expected value \$999,000. Conditioning on *twobox*: \$11,000. So EDT one-boxes.
- **CDT** intervenes on Act. Box B is not downstream of Act, so $P(\text{full}) = p$ either way; two-boxing yields \$1,000 more in every hypothetical. So CDT two-boxes—and, being predictably a two-boxer, faces an empty box.
- **A-FDT** builds a graph in which both Act and Prediction are children of the node $\mathrm{afdt}(\underline{P}, \underline{G})$. Intervening $\mathrm{do}(\mathrm{afdt}=\text{onebox})$ sets Act to onebox *and*, via the subjunctive edge, sends $P(\text{full})$ to $0.99$; expected value \$990,000. Intervening $\mathrm{do}(\mathrm{afdt}=\text{twobox})$ sends it to $0.01$; expected value \$11,000. One-box wins.

The English rendering: "If this very decision procedure outputs *onebox*, my body almost surely takes one box and the predictor likely filled box B; if it outputs *twobox*, my body takes two boxes and the box is likely empty. I prefer the first world, so this procedure hereby outputs *onebox*." No retrocausation is invoked—only a refusal to imagine one's action changing while the function computing it (and things that track it) stays fixed.

### The smoking lesion

The same $P$ works for all three agents after renaming (Predisposition→Lesion, Prediction→Cancer, …). EDT refrains (managing the news, at a cost of \$1,000 in certain value); CDT smokes. A-FDT requires a new *graph*: the node for the agent's decision-function output connects to Act but **not** to Cancer, because cancer does not evaluate the agent's decisions. A subtlety from the source: whether the agent likes smoking depends on the lesion, so the model contains *two* candidate decision-function nodes, $\mathrm{afdt}(\underline{P_S}, \underline{G})$ and $\mathrm{afdt}(\underline{P_R}, \underline{G})$, corresponding to preferences that do or don't value smoking; the lesion determines which one controls Act, and the agent is uncertain which. Intervening on either leaves $P(\text{lesion})$ untouched, so smoking is strictly better by $p \cdot \$1{,}000$ (the probability that the smoking-valuing procedure is the one actually running, times the value of smoking). **A-FDT smokes.** One-boxing and smoking follow from a single criterion, contra the Gibbard–Harper impossibility intuition.

I note, with the source, that the lesion problem is badly contrived: if Eve lives among EDT agents none of whom smoke, her own model is inaccurate. The problem earns its place historically, not structurally.

### Transparent Newcomb and Parfit's hitchhiker

Now the agent *sees* whether box B is full before choosing. CDT and EDT both two-box on seeing a full box (conditioning or intervening on the act can't change the already-visible contents). A-FDT one-boxes even facing two full boxes. The mechanism is the observation-handling rule of §4: seeing the box full, Fiona intervenes on the node $\mathrm{afdt}(\underline{P}, \underline{G}, \text{full})$—her procedure *given that observation*. If that procedure outputs *twobox*, then by the subjunctive edge from procedure-output to Prediction, the predictor probably predicted *twobox*, so the box was probably *empty*, and the agent would not be in the "full" branch at all. (With a 99%-accurate predictor and prior $q$ on two-boxing-when-empty, one-boxing-on-full is worth $\$990{,}000 + 0.01q\cdot\$1{,}000$ versus roughly $\$11{,}000 + q\cdot\$990$.) Imagining two-boxing here means imagining a world in which she likely *saw an empty box*.

This is exactly Parfit's hitchhiker: pay the driver on arrival, and you probably were never left to die; refuse, and you probably are not in the city. CDT and EDT agents, predictably non-payers, die in the desert. A-FDT agents pay—without precommitment machinery—because "the best output of this procedure" is evaluated over worlds in which observations co-vary with the procedure's output.

### Blackmail

In XOR blackmail and mechanical blackmail, a predictor sends a costly letter iff (roughly) doing so will extract payment. EDT pays (paying is good news: it implies no infestation); CDT pays (the program is already running; \$1,000 beats \$1,000,000). A-FDT refuses even while holding the letter: intervening on $\mathrm{afdt}(\underline{P}, \underline{G}, \text{letter})$ changes *whether the letter is likely sent* (the blackmailer predicts the procedure), while leaving the infestation—causally and subjunctively independent of the procedure—untouched. Refusal corresponds to a world where one was probably never blackmailed. Strikingly, the A-FDT agent refuses even knowing (with an imperfect predictor) that her particular case was a prediction error, because being the kind of agent who refuses is what keeps her un-blackmailed in expectation. She has not "failed to update" on the letter: she updates by relocating her point of intervention. This is the source of the family resemblance to Wei Dai's updateless decision theory.

Two further payoffs: in Death in Damascus, where CDT destabilizes into an infinite belief-revision loop and even values a truly random survival coin at less than \$1, A-FDT stays in Damascus calmly, having accepted that Death's appointment book tracks her procedure. In the twin prisoner's dilemma, A-FDT cooperates, since the twin implements the same decision function.

## 6. Dominance, Fairness, and the Global Perspective

Every method of constructing hypotheticals yields its own notion of dominance. Two-boxing "dominates" only relative to CDT counterfactuals—i.e., relative to imagining the act token changing while the decision *type* stays fixed, which is like imagining a working calculator outputting $3159$ while holding fixed that $6288+1048=7336$. Defined instead over subjunctively-dependent-holding-fixed hypotheticals, one-boxing dominates in Newcomb's problem, and A-FDT agents never take dominated actions. Dominance is therefore not a neutral arbiter between theories; utility achieved is the metric the source relies on.

The source's fairness claim deserves careful statement. No decision theory wins in *all* dilemmas—one can build a predictor who rewards alphabetical decision theory. But in **fair problems**, where the agent's beliefs are accurate and outcomes depend only on her behavior in the dilemma at hand (rewarding predictions of her *actions*, not her decision procedure per se), the authors report no fair dilemma in which A-FDT loses to a rival. A formal criterion of fairness remains an open problem (footnote 15 of the source sketches the difficulty via a "punish anyone matching Fiona's output" game).

Philosophically, the source recommends the "global perspective": an A-FDT agent asks what the entire universe would look like if the A-FDT algorithm behaved differently, respecting logical, mathematical, nomic, and causal constraints. Is it a delusion to "control" a mathematical function's output? The source's reply is that a deterministic CDT agent's "control" of her action token faces an exactly parallel objection: there is only one act she can physically take, just as there is only one output the function can have. Both theories require imagining impossibilities; they differ in which impossibilities they imagine, and only A-FDT's imaginations preserve decision-relevant world structure.

## 7. Applying A-FDT to Unfamiliar Cases: A Recipe

Combining the source's formalism with my own operational gloss, here is how to apply Equation (4) to a new problem.

1. **Model.** Build a distribution $P$ over all decision-relevant variables, including variables representing the outputs of any mathematical/computational processes that figure in the problem—most importantly a variable $\mathrm{afdt}(\underline{P}, \underline{G}, \underline{x})$ for your own procedure's output given your observations.
2. **Dependence graph.** Build $G$: draw an edge from the decision-function-output node to every variable that is a *function of, or prediction of, or otherwise logically constrained by* that output. This includes your body's action, other agents' predictions and simulations of you, and copies or twins running the same procedure. It excludes variables correlated with you only statistically or via common causes that don't compute your decision (lesions, weather). Also draw edges between other variables as their logical/causal structure dictates, and add one node per observation-history for the procedure (e.g., $\mathrm{afdt}(\underline{P}, \underline{G}, \text{letter})$, $\mathrm{afdt}(\underline{P}, \underline{G}, \emptyset)$), with the environment determining which controls your act.
3. **Intervene and evaluate.** For each action $a$, compute $\mathbb{E}(V \mid \mathrm{do}(\mathrm{afdt}(\underline{P},\underline{G},\underline{x}) = a))$ by setting the output node to $a$ and propagating along $G$'s edges; pick the argmax.

**A worked application: a voting dilemma.** Ten agents each decide whether to pay \$1,000 to vote; each receives \$1,000,000 iff all ten vote. Under CDT, each agent's act is causally independent of the others, so voting is dominated and no one votes. The A-FDT construction: since the agents reason symmetrically (common knowledge of shared decision procedures), each agent's $G$ contains edges from her own decision-function output to the *other agents' corresponding outputs*—her hypotheticals co-vary across all ten procedures. Intervening $\mathrm{do}(\mathrm{afdt}=\text{vote})$ yields a world where all ten vote: net \$999,000. Intervening $\mathrm{do}(\mathrm{afdt}=\text{abstain})$: no one votes, \$0. She votes. (This step—treating symmetric reasoners as subjunctively dependent—is a substantive modeling commitment; the source endorses it for identical procedures and for predictors-of-the-procedure, and I would extend it to *similar* procedures with proportional weakenings of the dependence, an assumption of mine that the source leaves informal.)

**A caveat case.** If the ten voters are known to use *different*, independently-designed procedures, the dependence edges weaken or vanish, and A-FDT's prescription approaches CDT's. The theory's power lives or dies with the accuracy of $G$.

## 8. What Is Settled and What Is Open

From the source, firmly: the definition (4); the agreement of all three theories when action–world correlations are all caused by the action; the divergence under predictors and twins; the specific prescriptions catalogued above; the reflectively stable refusal to pay blackmailers; the non-negative valuation of information; the claim that dominance arguments are theory-relative.

Open, per the source and my reading: (i) a theory of *counterpossible* reasoning and a $\mathtt{true}$-like operator, which would enable an "evidential" version of A-FDT conditioning directly on logical sentences; (ii) a Pearl-style method for *inferring* the subjunctive-dependence graph $G$ from observation and experiment—perhaps the largest open problem; (iii) a formal definition of fairness, needed to state the optimality conjecture precisely; (iv) implementation questions (logical uncertainty, Löbian self-reference) that arise in any real computational agent. The source also notes in a footnote that the authors' preferred formulation intervenes on *policies* (observation→action mappings) rather than actions; I have followed the action-valuation form of Equation (4) throughout, but policy-valuation matters in some multi-agent dilemmas.

## 9. Conclusion

A-FDT is best understood as CDT with a generalized surgery: intervene on the *type*—"what this decision procedure outputs on this input"—rather than the token, preserving in your hypotheticals exactly those dependencies (causal, logical, predictive) that really track the procedure's output, and severing those that merely correlate with it. EDT respects too many action–environment correlations; CDT respects too few; A-FDT, the source argues, gets the balance right, one-boxing and smoking, escaping the desert, resisting extortion, and cooperating with twins—by one compact rule. Its foundations on counterpossibles and dependency inference remain unfinished, and its stranger prescriptions (paying the driver while staring at a full box's worth of money) should be weighed honestly. But if the metric is utility achieved in fair problems, A-FDT is the strongest general-purpose candidate currently on the table.

**Reference.** Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060. All unattributed formal claims above trace to Equation (4) and Sections 3–9 of that paper; deviations and extensions are flagged as mine.