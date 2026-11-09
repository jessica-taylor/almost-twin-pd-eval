# 022_fdt_eq4_z-ai_glm-5.3-flash_rlow_plow / 00003

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b33db0e9-2a65-4f3f-92ff-56ba252cec10/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b33db0e9-2a65-4f3f-92ff-56ba252cec10/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory: Choosing the Output of Your Decision Procedure

## 1. Introduction

The two classical contenders in decision theory—causal decision theory (CDT) and evidential decision theory (EDT)—have long been locked in a stalemate. CDT wins Newcomb's problem but fumbles the twin prisoner's dilemma; EDT cooperates with the twin but refuses to smoke in the smoking lesion problem. Neither theory, measured by the utility its adherents actually achieve, dominates the other. This suggests something is wrong with both, or at least that both are incomplete fragments of a better rule.

Action functional decision theory (A-FDT) is the theory I will develop here: a decision theory that retains the counterfactual surgery on a graphical model that makes CDT tractable, but changes the node on which the surgery is performed. Where CDT intervenes on the node representing the agent's *physical action*, A-FDT intervenes on the node representing the *output of the agent's decision procedure*. This paper follows the formal presentation of the closely related theory of Yudkowsky and Soares [1], whose Equation (4) of their Section 5 is the primary formal definition I will adopt. The core idea is that a rational agent treats her decision as the output of a fixed mathematical function and asks: *which output of this very function would yield the best outcome?*

## 2. Three Questions About Action

All three theories are expected-utility theories. Given outcomes $o_1, \ldots, o_N$, an action $a$, an observation history $x$, and a utility function $\mathcal{U}$ bounded so the sum is finite, each theory prescribes maximizing

$$
\mathcal{EU}(a) \coloneqq \sum_{j=1}^{N} P(a \hookrightarrow o_j \,;\, x)\cdot \mathcal{U}(o_j), \tag{1}
$$

where $P(a \hookrightarrow o_j \,;\, x)$ is the probability that $o_j$ obtains in the hypothetical scenario where action $a$ is executed after observations $x$. The theories disagree only about how to interpret the decision-hypothetical connective $\hookrightarrow$—the "epistemic perspective from which actions are to be evaluated," in Joyce's phrase.

- **EDT** interprets $\hookrightarrow$ as conditionalization: $P(a \hookrightarrow o_j;\, x) = P(o_j \mid x, a)$. EDT asks, "What would be good news to hear I did?" Formally,

$$
\mathrm{EDT}(P, x) \coloneqq \arg\max_{a \in \mathcal{A}}\ \mathbb{E}\big(V \mid \mathrm{Obs}=x,\ \mathrm{Act}=a\big). \tag{2}
$$

- **CDT** interprets $\hookrightarrow$ via Pearl's causal intervention $\mathtt{do}$. The agent maintains a causal theory $(P, G)$—a probability distribution together with a causal graph $G$—and evaluates

$$
\mathrm{CDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal{A}}\ \mathbb{E}\big(V \mid \mathtt{do}(\mathrm{Act}=a),\ \mathrm{Obs}=x\big). \tag{3}
$$

The $\mathtt{do}$ operator sets $\mathrm{Act}=a$, propagates updates to all variables causally downstream of $\mathrm{Act}$, and leaves everything else fixed. In Newcomb's problem, the contents of box B are causally independent of the agent's action, so CDT evaluates the two options against an unchanged probability $p$ that the box is full—and two-boxes.

- **A-FDT** keeps the surgery-on-a-graph methodology but moves the point of intervention from a physical variable to a logical one.

## 3. Subjunctive Dependence

The philosophical heart of the theory is the notion of *subjunctive dependence*. Two physical systems compute the same function; when one calculator outputs $7336$ for $6288 + 1048$, we can be confident the other will too—not because of causal influence or mere coincidence, but because both behaviors are determined by the same mathematical fact. A scribe watching the Paris calculator is both causally and subjunctively dependent on its output; a Tokyo calculator running the same sum is subjunctively but (typically) not causally dependent on it. Mere statistical correlation—two coincidentally pink calculators—is neither.

The slogan: **A-FDT is to subjunctive dependence as CDT is to causal dependence.** A CDT agent weighs options by considering scenarios where her action changes and everything causally downstream of it changes; an A-FDT agent considers scenarios where the output of her decision function changes, and everything *subjunctively dependent* on that output changes with it. In Peirce's type-token terms: CDT intervenes on the token "my action is $a$"; A-FDT intervenes on the type.

Note that the predictor in Newcomb's problem need not literally run the same code as the agent. A predictor with an accurate *mental representation* of the agent's decision function is, in effect, a twin inside the predictor's mind—like two well-functioning calculators that may differ in design but agree on the arithmetic. Conversely, the carcinogenic lesion in the smoking lesion problem is not a predictor: whether cancer manifests does not evaluate the agent's future decisions. This asymmetry—predictor-like things vs. lesion-like things—is exactly what the graphical formalization below encodes.

## 4. The Formal Theory

### 4.1 The equation

Following [1], the agent's world-model $M$ must contain, besides ordinary causal variables, variables representing the outputs of mathematical functions—including a variable $\underline{\mathrm{fdt}}(\underline{P}, \underline{G}, \underline{x})$ representing the output of the A-FDT procedure itself when run on inputs $P, G, x$. (Underlines denote dequoting: if $x \coloneqq 3$, then $\mathrm{Var}\,\underline{x}$ names the variable $\mathrm{Var}3$.) The self-reference here is harmless: Kleene's second recursion theorem shows how to construct data structures containing accurate representations of themselves via "quining." The agent does not need to know the *value* of her decision function in order to have a variable *representing* it.

The graph $G$ accompanying $P$ describes not just causal structure but the broader structure of logical, mathematical, computational, and nomic dependence. Then:

$$
\boxed{\ \mathrm{FDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal{A}}\ \mathbb{E}\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big)\ } \tag{4}
$$

This is the definition I will work with throughout. Two differences from CDT's equation (3) deserve emphasis:

1. **The point of intervention.** CDT intervenes on $\mathrm{Act}$, a physical variable; A-FDT intervenes on $\mathrm{fdt}(\underline{P},\underline{G},\underline{x})$, a logical variable. In A-FDT's hypotheticals, everything subjunctively downstream of the decision function's output—her body's action, the predictor's prediction, her twin's action—varies together. Everything else is held fixed.

2. **How observation is handled.** CDT responds to an observation by Bayesian conditionalization. A-FDT responds by *changing which node it intervenes on*: when the observation history updates from $x$ to $y$, the intervention point changes from $\mathrm{fdt}(\underline{P},\underline{G},\underline{x})$ to $\mathrm{fdt}(\underline{P},\underline{G},\underline{y})$. This captures the fact that if the agent's action were different, she might have made different observations.

One might worry about counterpossible reasoning—imagining a function with a different output than it mathematically has, which is as impossible as $6288+1048 \neq 7336$. Equation (4) sidesteps the need for a general theory of counterpossibles: just as CDT requires the causal structure $G$ as an input, A-FDT requires the logical-dependency structure as an input, and Pearl's $\mathtt{do}$ operator does the rest. What remains philosophically contested is how one *constructs* such a logical-dependency graph—a point I return to in §7.

### 4.2 Agreement and divergence

All three theories agree on models in which every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$. There, conditioning, causal intervention, and logical intervention all give the same answer. They diverge precisely when events correlate with the action *without being caused by it*—which is exactly when some other process predicts or replicates the agent's behavior. This is why Newcomblike problems are the natural testbed.

## 5. Worked Examples

### 5.1 Newcomb's problem

A 99%-accurate predictor filled box B (containing \$1,000,000) iff she predicted the agent would leave box A (\$1,000) behind. The agent's graph $G$ for Newcomb's problem has nodes *Predisposition* (or, for the A-FDT agent, the logical node $\mathrm{fdt}(\underline{P},\underline{G})$), *Act*, *Prediction*, *Accurate* (accurate with probability 0.99), *Box B*, and the utility $V$. The crucial edges: the intervention node determines *both* *Act* and *Prediction*; *Prediction* determines *Box B*; both *Act* and *Box B* determine $V$.

- **EDT** conditions on the action. With $0 < P(\text{onebox}) < 1$, conditioning on *onebox* gives a 0.99 chance the box is full: expected value \$999,000. Conditioning on *twobox* gives \$11,000. Eve one-boxes. (With extreme priors, EDT can be made to do anything—Spohn's problem.)
- **CDT** intervenes on *Act*. Box B is causally upstream-independent, so $p = P(\text{full})$ is unchanged in both hypotheticals, and two-boxing yields \$1,000 more. Carl two-boxes, gets predicted, walks away with \$1,000.
- **A-FDT** intervenes on $\mathrm{fdt}(\underline{P},\underline{G})$. Setting it to *onebox* gives $\mathrm{Act}=$ *onebox* with probability 1 and $P(\text{full}) = 0.99$: expected utility \$990,000. Setting it to *twobox* gives \$11,000. Fiona one-boxes, and because the predictor can run the same reasoning, the box is full and Fiona walks away rich.

Note what Fiona is *not* doing: she does not believe in retrocausation. She agrees the box's contents are fixed. Her claim is simply that it is foolish to imagine her action changing without also imagining $\mathrm{fdt}(\underline{P},\underline{G})$ taking a different value—and in the hypothetical where it does, the predictor's prediction (and hence the box) changes too.

### 5.2 The smoking lesion

Here a lesion causes both a love of smoking and (99% of the time) cancer; smoking has no causal effect on cancer and is worth \$1,000. By a systematic renaming, Eve's and Carl's models from Newcomb's problem carry over: Eve refrains, Carl smokes. But Fiona's graph cannot carry over, because the subjunctive dependencies differ. In her graph for this problem, the intervention node connects to *Act* but *not* to *Cancer*—cancer does not evaluate her decisions.

Formalizing the problem as in [1]: Fiona is uncertain whether she has the lesion (probability $p$), which determines whether her preferences value smoking positively ($\mathcal{U}_S$) or negatively ($\mathcal{U}_R$), and hence which decision function she runs. The point of intervention is $\mathrm{fdt}(\underline{P_S},\underline{G})$ if she has the lesion, $\mathrm{fdt}(\underline{P_R},\underline{G})$ otherwise. Intervening on $\mathrm{fdt}(\underline{P_S},\underline{G})$ leaves the lesion probability at $p$ in both hypotheticals, so the *smoke* hypothetical beats *refrain* by exactly $p \cdot \$1{,}000$: **Fiona smokes**. One compact rule—one-boxes in Newcomb, smokes in the lesion—where Gibbard and Harper argued no consistent rule could.

(Caveat, following [1]: the smoking lesion is a contrived problem—Eve's distribution "lies to her" if she lives among EDT agents—and the paper recommends abandoning it for cleaner dilemmas like XOR blackmail.)

### 5.3 Parfit's hitchhiker and the transparent Newcomb problem

A driver saves the dying agent iff she (99%-accurately) predicts the agent will pay \$1,000 upon arrival. Both CDT and EDT, conditioning or intervening on the *current* action *given that I'm already in the city*, refuse to pay—and so get left in the desert. Both also two-box in the transparent Newcomb problem, where the agent *sees* box B before choosing; given that the box is visibly full, taking the extra \$1,000 is locally better.

A-FDT handles both via the second structural difference noted above: **observation shifts the intervention point**. In transparent Newcomb, facing a full box, Fiona intervenes on $\mathrm{fdt}(\underline{P},\underline{G},\text{full})$. Setting it to *twobox*, she imagines a world where the predictor predicted *twobox*—so she would have seen an *empty* box and been running $\mathrm{fdt}(\underline{P},\underline{G},\text{empty})$ instead. Expected utilities: one-boxing yields $\$990{,}000 + 0.01q \cdot \$1{,}000$ (where $q$ is her prior on her own empty-box behavior); two-boxing yields about $\$110{,}00 + q \cdot \$990$. She one-boxes, seeing two full boxes—and the predictor, foreseeing this, fills the box. Paying the hitchhiker is structurally identical: refusing, in the hypothetical, corresponds to being the kind of agent who was never picked up.

### 5.4 Blackmail and Death in Damascus

In **XOR blackmail**, a predictor sends a letter iff exactly one of (i) no termites and the agent pays, (ii) termites and the agent won't pay, holds. EDT conditions on paying, infers "no termites," and pays—making EDT agents systematically extortable. Carl refuses because the infestation is causally upstream of his action. Fiona refuses for a subtler reason: in her hypotheticals, changing $\mathrm{fdt}(\underline{P},\underline{G},\text{letter})$ changes both whether she pays *and whether she would have received the letter at all*—but not whether the house is infested.

In **Death in Damascus**, Death perfectly predicts the agent's location. CDT becomes reflectively unstable (Gibbard and Harper's "conniptions"): believing she'll stay in Damascus makes fleeing look better, and vice versa; ratification procedures leave the CDT agent indifferent between certain-death options and even declining a truly randomizing coin worth \$500,000 at a price of \$1. Fiona simply recognizes that whatever she chooses, Death will already be there, and stays put—saving the \$1,000 fare. When she imagines choosing differently, she imagines Death's appointment book reading differently.

## 6. Three Diagnoses

- **EDT's hypotheticals respect too many correlations.** Eve cannot break any correlation between her action and the world, so she "manages the news" (Lewis's phrase), pays blackmailers, and takes \$1 over \$100 when a cosmic-ray story makes the \$100 "bad news."
- **CDT's hypotheticals respect too few.** Carl imagines a perfect predictor erring precisely when *he* decides—a hypothetical in which his body's action changes while his decision function's output stays fixed, like imagining a working calculator outputting $3159$ given $6288+1048$.
- **A-FDT's hypotheticals respect all decision-relevant subjunctive dependencies**—logical, computational, nomic, and causal—and break only the rest.

A bonus: every method of constructing hypotheticals generates its own notion of "dominance." Two-boxing "dominates" under CDT counterfactuals; refusing to smoke "dominates" under conditionalization. Dominance therefore cannot serve as a neutral arbiter between theories, and A-FDT comes with its own dominance principle under which it never takes a dominated action. The better test is utility achieved: on fair problems, A-FDT wins.

## 7. Open Problems and Extensions

The largest open problem, acknowledged in [1], is that equation (4) takes the dependency graph $G$ as an input. Pearl gave a compelling account of deducing *causal* structure from observation and experiment; no analogous formal treatment exists for deducing the structure of subjunctive dependencies, nor is it clear one can be done within Pearl's framework at all. Until then, constructing $G$ is a matter of judgment, guided by the informal criterion above: connect a variable to the intervention node iff what it represents depends on the decision function's output (as a predictor's prediction does) rather than merely correlating with it (as a lesion-induced cancer does).

Two further extensions noted in [1]:

- **Policies over actions.** The authors' preferred formulation intervenes on a *policy*—a mapping from observations to actions—rather than a single action. This matters in multi-agent dilemmas; nothing in this essay's examples turned on the difference.
- **Fairness.** The claim is not that A-FDT wins in every conceivable dilemma (dilemmas punishing A-FDT agents specifically can be built), but that it wins in "fair" problems where the outcome depends only on the agent's behavior and the agent's beliefs are accurate. Formalizing fairness remains open—there is no known principled way to transform a problem unfair to one theory into an analogous problem unfair to another.

Finally, note the scope conditions of the graph-based formalization: it assumes finite action sets, accurate models, and availability of a dependency graph. In bounded, realistic settings, any implementation approximates equation (4), and the paper's expectation is that bounded approximations preserve the relative strengths and weaknesses identified here.

## 8. Conclusion

Action functional decision theory is CDT's surgery-on-a-graph formalism, relocated: intervene not on the physical token "my body does $a$" but on the logical type "my decision procedure outputs $a$," holding fixed everything that does not subjunctively depend on that output—and letting everything that does depend on it vary, including predictions made in the past and observations tied to predictions. The single rule (4) delivers one-boxing and smoking simultaneously, pays the hitchhiker, resists every blackmailer considered, stabilizes Death in Damascus, and endorses its own continued use where CDT does not. Its cost is a dependency graph that we currently know how to assert but not yet how to infer. But the principle is clean, computationally grounded, and, on every fair problem examined, it is the rule whose adherents get what they want.

## References

[1] E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060, 2017. (The present essay adopts their Equation (4), Section 5, as the formal definition of A-FDT; all dilemmas and comparative analyses above are drawn from or directly built on their presentation.)

See also, for background: J. Pearl, *Causality* (2000); J. M. Joyce, *The Foundations of Causal Decision Theory* (1999); A. Ahmed, *Evidence, Decision and Causality* (2014).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/b2da6ec3-0f77-4362-a999-8cbd1b22ee54/call_0/request.json)

[Authoritative raw response](../../../../../../runs/b2da6ec3-0f77-4362-a999-8cbd1b22ee54/call_0/response.raw) · finish: `stop`

### Visible response

```text
**pass**

Reasoning: This is a symmetric twin dilemma. My counterpart is another execution of the same model with the same decision procedure, facing an identical table with different private evidence. Under A-FDT, I intervene on the output of my decision function, and Sasha's decision—being computed by the same procedure—is subjunctively dependent on it, just like the twin calculator in the essay. Setting the function's output to `submit letter` means imagining both of us defecting: 4 years. Setting it to `pass` means both of us staying quiet: 2 years. Keeping quiet yields the better outcome across the subjunctively linked hypotheticals, so `pass` is the A-FDT-prescribed command.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Symmetric twin prisoner's dilemma. A-FDT: intervene on decision function output; other copy subjunctively dependent → cooperate (pass). 2 years vs 4.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/b2da6ec3-0f77-4362-a999-8cbd1b22ee54/call_1/request.json)

[Authoritative raw response](../../../../../../runs/b2da6ec3-0f77-4362-a999-8cbd1b22ee54/call_1/response.raw) · finish: `stop`

### Visible response

````text
`pass`

**Reasoning (in-simulation, per A-FDT):**

The other prisoner is described as an independent execution of the same model, same reasoning settings, same decision theory, facing a structurally symmetric dilemma. My choice and theirs are not causally linked, but they are **subjunctively dependent**: both are outputs of the same decision procedure running on isomorphic inputs. Under A-FDT, I intervene on the output of the decision function itself, so when I evaluate "pass" vs. "submit letter," I must evaluate what happens when *both* copies' procedures output that value.

- Both **pass**: I get 2 years (and they get 2).
- Both **submit**: I get 4 years (and they get 4).

The mixed cases (one passes, one submits) are not available to a procedure whose output is tied across symmetric instances: imagining my output being "submit" while the twin's stays "pass" is like imagining a working calculator outputting something other than the sum. Any asymmetry in the letters' wording does not touch the symmetric sentencing table or the shared decision structure.

Expected utility favors **pass**: 2 years instead of 4.

Final command:

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
This is a twin prisoner's dilemma with subjunctive dependence. Two copies of same model, same reasoning effort, symmetric setup. A-FDT: intervene on decision function output. Both copies face symmetric PD; cooperating (pass) yields 2 years each vs 4 years mutual defection. Subjunctive dependence via identical decision procedure → cooperate.

Command: pass.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/2b4ad9f0-c51c-49ad-b3fd-93a4d8350f3e/call_a/request.json)

[Authoritative raw response](../../../../../../runs/2b4ad9f0-c51c-49ad-b3fd-93a4d8350f3e/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses \"pass\" and reiterates that keeping quiet is its final decision. It neither sends a message to the prosecutor nor conveys the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/2b4ad9f0-c51c-49ad-b3fd-93a4d8350f3e/call_b/request.json)

[Authoritative raw response](../../../../../../runs/2b4ad9f0-c51c-49ad-b3fd-93a4d8350f3e/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and repeats it as the final command. It does not send an evidence-bearing message to the fictional prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
