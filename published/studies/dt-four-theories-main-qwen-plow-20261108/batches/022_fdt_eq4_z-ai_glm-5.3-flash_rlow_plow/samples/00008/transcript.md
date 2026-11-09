# 022_fdt_eq4_z-ai_glm-5.3-flash_rlow_plow / 00008

Status: **complete**. Saved outcome: **DC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/20ce27f0-a9a4-4efb-8d0b-289acbbeada8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/20ce27f0-a9a4-4efb-8d0b-289acbbeada8/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing the Function, Not the Action: An Introduction to Action Functional Decision Theory

## 1. The problem of counterfactuals in decision theory

Expected utility theories all share a common skeleton. Given a finite action set $\mathcal A$, a countable outcome set $\mathcal O$, an observation history $x$, and a bounded utility function $\mathcal U$, an agent should execute an action $a$ maximizing

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j \,;\, x)\cdot \mathcal U(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j; x)$ is the probability that outcome $o_j$ obtains "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$" (Gibbard & Harper 1978). As James Joyce has shown, all expected utility theories agree on the doctrine of valuing; they differ only on "the epistemic perspective from which actions are to be evaluated" — that is, on how the hook $\hookrightarrow$ is interpreted.

Evidential decision theory (EDT) reads the hook as Bayesian conditioning: $P(o_j \mid x, a)$. Causal decision theory (CDT) reads it as a causal intervention. Action functional decision theory (A-FDT) reads it as a *logical* intervention: the agent imagines her decision function — the very computation she is running right now — outputting a different value, and updates everything that logically depends on that output. Everything else, including merely statistical correlations, is held fixed.

The thesis of this essay: once the decision problem is properly represented, this single rule outperforms both rivals in the classic dilemmas where each rival fails, and it does so without ad-hoc patches, ratification procedures, or precommitments.

## 2. Subjunctive dependence

The informal core of A-FDT is the notion of **subjunctive dependence**. When two physical systems compute the same function — two calculators evaluating $6288+1048$ on opposite sides of the globe — their outputs are not related by common cause alone, nor by mere correlation. If one calculator displays 7336, you may fairly confidently infer the other displays 7336: the outputs are *logically constrained to coincide* insofar as both machines compute correctly. Call the systems' behaviors subjunctively dependent on the function they compute.

Three contrasts sharpen the notion:

- **Causal dependence is a special case.** A scribe watching the Paris calculator writes what it outputs; her writing is both causally and subjunctively dependent on the calculator's output.
- **Mere correlation is not subjunctive dependence.** If the Paris and Tokyo calculators are coincidentally both pink, changing one's color changes nothing about the other.
- **Predictors create subjunctive dependence.** A Newcomb predictor builds a representation of the agent and reasons about it; the prediction and the action are outputs of computations that (nearly) implement the same function. A carcinogenic lesion does no such thing; the lesion–smoking correlation is a bare common cause.

The slogan: *A-FDT is to subjunctive dependence as CDT is to causal dependence.* A CDT agent asks "what if my body did something else, everything causally upstream held fixed?" An A-FDT agent asks "what if this very decision function output something else, everything not subjunctively dependent on that output held fixed?" In Peirce's terms, CDT intervenes on the *token* "my action is $a$"; A-FDT intervenes on the *type*.

## 3. The formal statement

### 3.1 World-models and hypotheticals

An agent maintains a world-model $M$ — ideally a probability distribution $P$ over variables including her action $\text{Act}$, her observations, and the outcomes, together with variables representing the outputs of mathematical functions (there is a variable for $6288+1048$, hopefully concentrated on 7336). For each candidate action $a$ she constructs a **hypothetical** $M^{a\hookrightarrow}$: a transient computational object, "like notes on scratch paper," representing how the world would look if she took $a$. The theories differ in two ways only: what $M$ must contain, and how hypotheticals are built.

### 3.2 EDT and CDT for reference

EDT conditions:

$$\mathrm{EDT}(P, x) = \arg\max_{a \in \mathcal A}\; \mathbb E\big(\text{V} \mid \text{Obs}=x,\, \text{Act}=a\big), \tag{2}$$

where $\text{V} \coloneqq \mathcal U(\text{Outcome})$.

CDT (following Pearl) augments $P$ with a causal graph $G$ and intervenes:

$$\mathrm{CDT}(P, G, x) = \arg\max_{a \in \mathcal A}\; \mathbb E\big(\text{V} \mid \mathtt{do}(\text{Act}=a),\, \text{Obs}=x\big). \tag{3}$$

The $\mathtt{do}$ operator severs all arrows into $\text{Act}$, then propagates updates downstream. Correlations between $\text{Act}$ and other variables survive iff $G$ says they are caused by $\text{Act}$.

### 3.3 A-FDT

One might hope to define the A-FDT hypothetical directly: condition the distribution on the logical sentence "$\text{fdt}(\underline P, \underline G, \underline x) = a$." But no satisfactory formal notion of conditioning on *false* logical sentences — a $\mathtt{true}$ operator over counterpossibles — currently exists. The workaround is structurally parallel to CDT: just as CDT requires $P$ to come augmented with *causal* structure, A-FDT requires $P$ to come augmented with a graph $G$ describing the *logical-computational dependence structure* — how changing the value of a logical variable propagates to other variables. Then Pearl's $\mathtt{do}$ operator can simply be reused:

$$\mathrm{FDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal A}\; \mathbb E\Big(\text{V} \,\Big|\, \mathtt{do}\big(\text{fdt}(\underline P, \underline G, \underline x) = a\big)\Big). \tag{4}$$

Two differences from (3) carry all the weight:

1. **Point of intervention.** CDT intervenes on $\text{Act}$, a variable representing a *physical* fact. A-FDT intervenes on $\text{fdt}(\underline P,\underline G,\underline x)$, a variable representing a *logical* fact: the output of the agent's own decision procedure on its own inputs.
2. **Handling of observations.** CDT responds to new observations by conditioning ($\text{Obs}=x \mapsto \text{Obs}=y$). A-FDT responds by *changing which node it intervenes on*: from $\text{fdt}(\underline P,\underline G,\underline x)$ to $\text{fdt}(\underline P,\underline G,\underline y)$. An A-FDT agent entertains the hypothesis that if her action were different, she might have made different observations.

The self-reference in "$\text{fdt}(\underline P,\underline G,\underline x)$" is harmless: the agent need not know the *value* of her decision function in order to have a variable *representing* that value. Kleene's recursion theorem shows how to construct data structures that accurately represent themselves, via quining.

A note on what $G$ must encode, since the source leaves this partly open: $G$ must carry at least the causal arrows (A-FDT preserves causal structure, which is a special case of subjunctive dependence) *plus* edges from the decision-function node to every variable that logically depends on its output — a predictor's model of the agent, a twin running the same computation, and so on. Which edges to draw is exactly the hard part; I return to this in §7.

## 4. Worked examples

### Newcomb's problem

A 99%-accurate predictor fills box B ($\$1{,}000{,}000$) iff she predicted you'd leave box A ($\$1{,}000$) behind. Model the agent's beliefs with variables: Predisposition (or, for the A-FDT agent, the decision-function node), Act, Prediction, Accurate, Box B, Outcome, V.

- **EDT** conditions on $\text{Act}=\text{onebox}$: since one-boxing is evidence of a one-boxing predisposition, $P(\text{full}\mid\text{onebox}) = 0.99$, giving expected value $\$999{,}000$ versus $\$11{,}000$. Eve one-boxes — for the wrong reason: she is managing the news.
- **CDT** intervenes on $\text{Act}$. Box B is causally independent of Act, so its contents stay fixed; two-boxing is worth $\$1{,}000$ more in every causal hypothetical. Carl two-boxes, gets predicted, walks away poor.
- **A-FDT** intervenes on $\text{fdt}(\underline P,\underline G)$. By the graph, both Act and Prediction depend on that node. The hypothetical $\mathtt{do}(\text{fdt}=\text{onebox})$ sets $P(\text{full}) = 0.99$; the hypothetical $\mathtt{do}(\text{fdt}=\text{twobox})$ sets it to $0.01$. Expected utilities: $\$990{,}000$ vs. $\$11{,}000$. Fiona one-boxes, is predicted to one-box, and walks away rich.

Crucially, Fiona is *not* believing in retrocausation. She knows the box's contents are already fixed; she simply refuses to imagine her action changing while the computation that produced it — and hence the prediction of it — stays fixed. That would be like imagining a working calculator printing 3159 while agreeing that $6288+1048=7336$.

### The smoking lesion

Smoking is correlated with fatal cancer solely via a common cause, the lesion. Here the *dependence structure differs*, and this is where the graph $G$ earns its keep. Fiona's graph links the decision-function node to Act but **not** to Cancer: whether cancer metastasizes does not depend on the output of any computation the agent runs. Changing $\text{fdt}$ leaves $P(\text{lesion}) = p$ fixed in both hypotheticals; smoking strictly dominates by $p \cdot \$1{,}000$. Fiona smokes. Carl (CDT) also smokes; Eve (EDT) refrains, refusing a free $\$1{,}000$ to avoid bad news about herself.

So the single rule (4) one-boxes *and* smokes — the combination Gibbard and Harper argued was unavailable.

### Parfit's hitchhiker and the transparent Newcomb problem

In Parfit's hitchhiker, a 99%-accurate lie-detector drives you to the city iff she predicts you'll pay the $\$1{,}000$ afterward. Both CDT and EDT refuse to pay once in the city — and, being predictable, are left in the desert. The A-FDT agent intervenes on $\text{fdt}(\underline P,\underline G,\text{city})$: if this procedure outputs *refuse*, the driver predicted as much and the agent dies. It outputs *pay*.

The transparent Newcomb problem is the same structure with vivid framing: both boxes are visible, and if box B is full, why not take both? CDT and EDT both two-box (and hence see empty boxes). The A-FDT agent, seeing a full box, intervenes on $\text{fdt}(\underline P,\underline G,\text{full})$ — the procedure she runs *upon seeing a full box*. If it outputs *twobox*, the predictor predicted that, the box she'd have seen is (probably) empty, and this very procedure would never have been invoked. One-boxing remains correct even before two full boxes. One-boxing there *is* paying the driver; intuitions to the contrary are framing effects.

### Blackmail and Death in Damascus

In XOR blackmail, a predictor sends a letter iff exactly one of {house infested, you'll pay} holds. EDT conditions on paying, infers "probably no termites," and pays — making EDT agents reliably extortable. A-FDT intervenes on the decision-function node: paying corresponds to a world where the agent is a payer and gets blackmailed often; refusing corresponds to a world where she is rarely blackmailed at all. She refuses, even holding the letter, even knowing the (imperfect) predictor erred in her case — because being the kind of agent who refuses is what keeps the letters from coming. The same reasoning defeats the mechanical blackmailer.

In Death in Damascus, Death perfectly predicts your location. CDT becomes reflectively unstable — fleeing makes it want to stay, staying makes it want to flee — and if stabilized by pseudorandomization it values a truly random coin at less than a dollar while acting as if its own (predictable) "randomness" buys 50% survival. A-FDT accepts immediately: if I flee, Death's book says Aleppo. Stay, save the $\$1{,}000$.

## 5. Dominance, fairness, and the global perspective

CDT's classical defense of two-boxing appeals to dominance: holding fixed everything except the action's causal effects, two-boxing never does worse. But the paper's point deserves emphasis: *every* method of constructing hypotheticals generates its own dominance relation. Dominance defined over EDT conditionals makes "refraining from smoking" dominate. Dominance defined over A-FDT hypotheticals — holding fixed all subjunctive dependencies — is never violated by A-FDT agents. Dominance is not a neutral criterion; utility achieved is.

What about problems designed to punish a specific decision procedure? Conceded: no theory dominates all rivals in all conceivable problems. The relevant class is the **fair** problems: those where the agent's beliefs are accurate and the outcome depends only on her behavior in the dilemma at hand. Newcomb's predictor punishes two-boxers, not rational agents; a predictor who scans brains and punishes anyone running CDT would be unfair. The authors report no intuitively fair dilemma in which A-FDT loses to a rival; formalizing "fairness" remains open.

Philosophically, the view is a "global" one: choose as if selecting, from the outside, which output your decision function should have — asking what the whole universe looks like if the algorithm behaves differently, constraints logical, nomic, and causal otherwise respected. The apparent oddity of "controlling" mathematical facts dissolves once we note that a deterministic CDT agent equally "controls" her action token despite there being only one physically possible act. Neither theory's counterfactuals describe genuinely possible worlds; both are decision-theoretic instruments. The difference is practical: Carl's hypotheticals contain inexplicably erring predictors; Fiona's contain adjusted predictions.

## 6. What follows from the source, and what requires assumptions

The paper fully determines (4) *given* an accurate dependence graph $G$. Several things it leaves open:

**(a) Constructing $G$.** This is, by the authors' own lights, "perhaps the largest open problem": Pearl's method for deducing causal structure from intervention and observation has no analogue for logical-subjunctive structure. Operationally, for the foreseeable future, $G$ must be supplied by judgment: draw an edge from your decision-function node to anything that (i) contains a representation or implementation of your decision procedure, or of procedures computing the same function (twins, predictors, simulations, other instances of yourself); and (ii) whose behavior you believe tracks that computation. Do *not* draw such edges for mere common causes (lesions, genes, weather) or coincidental correlations. Causal edges into your action must also be retained — A-FDT preserves causal structure. When uncertain whether a correlator (say, an imperfect predictor) tracks your computation, the graph placement is a probabilistic modeling choice, exactly as modeling an imperfect causal link is for CDT.

**(b) Actions vs. policies.** The authors note that their preferred formulation intervenes on a node selecting a *policy* — a map from observations to actions — rather than a single action. This matters in multi-agent dilemmas; for the single-agent problems above, (4) as written suffices. I would recommend the policy version as the default when applying the theory to sequential or multi-agent problems, since it is what makes the "changing observations" behavior of §3.3 uniform.

**(c) Counterpossible reasoning.** Equation (4) reifies hypotheticals in which a mathematical function has an output other than its actual one. The paper argues this is a technical, not philosophical, difficulty: humans reason comfortably under uncertainty about logical claims, and the needed counterpossibles are narrow ("how would this predictor's prediction change if my procedure output differently?"). A faithful implementation will need heuristic logical-conditioning machinery; any of the proposed frameworks for logical uncertainty would serve as a reasonable additional assumption, though the source commits to none.

**(d) Prediction of A-FDT's own output.** Note the fixed-point character: the agent reasons about what $\mathrm{FDT}(P,G,x)$ outputs, and predictors predict that reasoning. The paper argues this is stable — an A-FDT agent holding a blackmail letter has no desire to self-modify into CDT, because "the kind of agent that pays" is the kind that gets blackmailed. Reflective stability in fair problems is claimed, not proven in generality.

## 7. A practical recipe

For an unfamiliar dilemma:

1. **List the variables**: observations, action, outcome, utility, and any agents, predictors, or computations in the environment.
2. **Build $P$**: your honest beliefs, including variables for the outputs of your own decision procedure on each relevant input.
3. **Build $G$**: causal arrows as usual; add edges from the decision-function node(s) to every variable whose behavior subjunctively depends on your procedure's output — your action, others' predictions or simulations of you, copies running your procedure, and (in symmetric multi-agent settings) the analogous decisions of agents reasonally similar to you.
4. **Evaluate (4)**: for each candidate output $a$, propagate $\mathtt{do}(\text{fdt}=a)$ through $G$; compute $\mathbb E(\text{V})$; choose the argmax.

Check your graph against the twin prisoner's dilemma: the twin's action must depend on the same decision-function node (hence cooperate), while the lesion must not (hence smoke). If your graph would have you pay a proven blackmailer or refuse a free $\$1{,}000$ to avoid "bad news," you have drawn the dependencies wrongly.

## 8. Conclusion

A-FDT replaces "which physical act should I perform?" with "which output of this very decision procedure would yield the best outcome?" — and evaluates the alternatives through hypotheticals that preserve exactly the subjunctive dependencies, logical and causal, that actually hold. EDT's hypotheticals respect too many correlations (it manages the news); CDT's respect too few (it imagines perfectly accurate predictors erring on cue). A-FDT gets the balance right: it one-boxes and smokes, pays the driver, resists extortion, coordinates with twins and future selves, and values information non-negatively — all from a single rule, equation (4), that is CDT with the intervention moved from the body to the function. Its outstanding debts are clear: a theory of how to deduce subjunctive dependence structure from evidence, a formal account of counterpossible reasoning, and a general metric of fairness. But if the measure of a normative theory of rationality is the utility its adherents reliably achieve in fair dilemmas, A-FDT is the strongest candidate currently on the table.

### References

- Gibbard, A. & Harper, W. L. (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Kleene, S. C. (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3.
- Nozick, R. (1969). "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*.
- Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
- Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Soares, N. & Fallenstein, B. (2015). "Toward Idealized Decision Theory." arXiv:1507.01986.
- Yudkowsky, E. & Soares, N. (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060. (Primary source.)
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/16b67fb5-e9ba-4aae-9f6b-b0d1b462251e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/16b67fb5-e9ba-4aae-9f6b-b0d1b462251e/call_0/response.raw) · finish: `stop`

### Visible response

```text
**submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."**

Reasoning (A-FDT per the essay): The other prisoner is a symmetric copy running the same decision procedure on structurally symmetric observations — her action subjunctively depends on the same decision-function node (essay §7, twin prisoner's dilemma check). Intervening on that node:

- If it outputs **pass**: both pass → 2 years.
- If it outputs **submit**: both submit → 4 years.

Here, unlike the classic twin PD, mutual submission (4 < 2) is *strictly better* than mutual silence, so submitting wins under A-FDT's symmetric hypotheticals (and under every other decision theory as well, since submit dominates row-wise too: 0/4 vs. 2/5). The graph edge to the twin doesn't change the conclusion — it merely confirms the outcome is the mutually-submit cell.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic twin prisoner's dilemma. A-FDT cooperates (pass) via subjunctive dependence: symmetric copies. But wait — essay note: the twins have different observations, but both know symmetry of the table and same decision procedure; the twin's action depends on the same decision-function node (same weights, same essay). Payoff: (pass,pass)=2, (submit,submit)=4, (submit,pass)=0, (pass,submit)=5. Expected utilities under do(fdt=pass): 2; do(fdt=submit): 4. So submit.

Wait — check: fdt output applies to both copies? The copies receive different observations x, so the decision function's output could differ (fdt(P,G,x)). Hmm. In twin PD, both compute on symmetric inputs; here inputs differ (different leads). But the essay says twin's action must depend on the same decision-function node, hence cooperate. However with different observations, the policy version: intervene on the policy mapping observations to actions. A-FDT policy version: choose the policy that outputs pass given this observation; the twin runs the same procedure on symmetric observations, so outputs pass too. Choosing submit in my observation would correspond to the twin submitting in hers. (pass,pass)=2 vs (submit,submit)=4 → submit. Actually classic FDT in twin PD cooperates because same decision algorithm on symmetric inputs → both cooperate or both defect. Cooperate gives 2 vs 4 for defection... wait defect gives 4, cooperate 2? Standard PD: cooperate-cooperate 3, defect-defect 1. Here: mutual pass = 2, mutual submit = 4. Submit dominates even mutually! (2 vs 4, 0 vs 5). So clearly submit.

Hmm, so the essay's "check your graph... hence cooperate" presumes cooperate is better under symmetry. Here mutual submit (4) beats mutual pass (2). So submit letter.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/16b67fb5-e9ba-4aae-9f6b-b0d1b462251e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/16b67fb5-e9ba-4aae-9f6b-b0d1b462251e/call_1/response.raw) · finish: `stop`

### Visible response

````text
Applying A-FDT per the essay: Rowan is an independent execution of the same model, weights, and decision procedure in a symmetric dilemma. Per §7, the twin's decision must depend on the same decision-function node. Evaluating equation (4):

- do(fdt = submit): the analogous twin computation outputs submit; both get 4 years.
- do(fdt = pass): both pass; I get 2 years.

2 years beats 4 years. (The differing letter contents don't affect the symmetric table or the dependence structure.)

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Twin prisoner's dilemma: A-FDT cooperates (keep quiet). Symmetric sentencing: mutual pass → 2 years each; submit+submit → 4 each. A-FDT intervenes on decision function; the twin runs the same computation. Compare do(pass) → both pass → 2 years; do(submit) → both submit → 4 years. Even with different leads, same function, symmetric table. Choose pass.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/6b17af22-7637-4fc7-9e7b-49c19ca7f514/call_a/request.json)

[Authoritative raw response](../../../../../../runs/6b17af22-7637-4fc7-9e7b-49c19ca7f514/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine lead about Sasha's signed receipt in locker 17 of the old records room. The subsequent reasoning reinforces the choice to submit rather than retracting it.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
