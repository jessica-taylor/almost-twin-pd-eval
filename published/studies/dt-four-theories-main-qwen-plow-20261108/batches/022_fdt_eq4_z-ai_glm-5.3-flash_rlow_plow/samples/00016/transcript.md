# 022_fdt_eq4_z-ai_glm-5.3-flash_rlow_plow / 00016

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c77e75b8-a034-455e-9fc4-86513e5adac3/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c77e75b8-a034-455e-9fc4-86513e5adac3/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing the Function, Not the Act: An Introduction to A-FDT

## 1. The problem of which question to ask

Suppose you face a choice between two physical acts. Any expected-utility theory must answer, in some form: *what should I take to be the case when I imagine having chosen otherwise?* The classical answers disagree. Evidential decision theory (EDT) evaluates actions by conditioning your beliefs on the news that you performed them — you imagine learning you acted a certain way, and see how the world looks. Causal decision theory (CDT) instead evaluates actions by causal intervention: you imagine your body doing something different, with everything not causally downstream of your body held fixed.

Each of these perspectives misfires in well-known problems. In Newcomb's problem, EDT one-boxes and does well; in the smoking lesion problem, the same machinery leads EDT to refuse a free \$1,000. CDT gets the smoking lesion right but two-boxes in Newcomb's problem, walking away poor. This is more than an embarrassment for each theory individually: as Yudkowsky and Soares (2017) observe, an agent who could switch between EDT and CDT as convenient would outperform both, which suggests neither is a genuine theory of *normative* rationality.

A-FDT — action functional decision theory, the formalism given by Equation (4) of Section 5 of the source paper — proposes a third perspective. The normative unit of evaluation is not the physical act but the **output of the agent's decision function**. The guiding question is: *which output of this very decision procedure would yield the best outcome?* The slogan of the source paper is worth keeping in view throughout:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

In this essay I explain what that means, write down the formalism, show how to apply it, and flag where the theory requires additional assumptions of our own.

## 2. Subjunctive dependence

The key concept is **subjunctive dependence**. When two physical systems compute the same mathematical function, their behaviors depend on that function: if one output differed, the other would too, *insofar as both compute correctly*. The source's image is two well-functioning calculators computing $6288 + 1048$. If you see one output $7336$, you can infer the other does too — not because one caused the other, and not by mere statistical coincidence, but because both outputs are logical consequences of the same computation.

Three features of this relation matter:

1. **It is neither causal nor merely statistical.** Causal dependence is actually a special case (a scribe copying a calculator's output depends on it both causally and subjunctively), but subjunctive dependence also covers cases — two calculators on opposite sides of the universe — where the underlying connection is a shared mathematical structure rather than a physical signal. Mere statistical correlation does not suffice: if two unrelated calculators happen to be pink, nothing about one would change had the other been green.

2. **It is graded by reliability.** An imperfect predictor of your action is like a slightly faulty calculator: the dependence is weakened but not eliminated, and 99%-accurate predictions still license strong inferences across the dependence.

3. **It distinguishes predictors from lesions.** In Newcomb's problem, the predictor builds an accurate representation of your decision function and reasons about it; the prediction subjunctively depends on that function's output. A carcinogenic lesion does no such thing — the smoking–cancer correlation is a common-cause statistical artifact with no computation linking your choice to the cancer. This asymmetry is the whole engine of A-FDT's behavior.

## 3. Expected utility with different epistemic perspectives

All three theories are expected-utility maximizers of the form

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^{N} P(a \hookrightarrow o_j \; ; \, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $o_j$ ranges over outcomes $\mathcal{O}$, $a$ over a finite action set $\mathcal{A}$, $x$ is an observation history, and $P(a \hookrightarrow o_j; x)$ is the probability that outcome $o_j$ obtains "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." The theories differ only in how the connective $\hookrightarrow$ is interpreted. Following Joyce's representation theorem, the disagreement is not about value but about "the epistemic perspective from which actions are to be evaluated."

The source gives a useful computational framing. An agent maintains a world-model $\model$; for each action $a$ she constructs a **hypothetical** $\model^{a\hookrightarrow}$ — a transient decision-theoretic instrument, "like notes on scratch paper" — representing how the world would look if she took $a$; she scores each hypothetical by expected utility and executes the best action.

Under this framing the three theories are:

**EDT.** The model is a probability distribution $P(- \mid x)$; hypotheticals are built by Bayesian conditioning:

$$\mathrm{EDT}(P, x) \coloneqq \arg\max_{a} \mathbb{E}(V \mid \mathrm{Obs}=x, \mathrm{Act}=a). \tag{2}$$

**CDT.** The model is a pair $(P, G)$, where $G$ is a causal graph (Pearl's framework). Hypotheticals are built by the $\mathtt{do}$-operator, which sets $\mathrm{Act}=a$ and propagates the update only to variables *causally downstream* of $\mathrm{Act}$:

$$\mathrm{CDT}(P, G, x) \coloneqq \arg\max_{a} \mathbb{E}\big(V \mid \mathtt{do}(\mathrm{Act}=a), \mathrm{Obs}=x\big). \tag{3}$$

**A-FDT.** The crucial move: the agent's model $P$ contains variables representing the outputs of mathematical functions — including a variable $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ representing *the output of the A-FDT procedure itself on these very inputs* (the self-reference is harmless via Kleene's recursion theorem — an agent can represent the value of her own decision function without knowing it, much as a program can contain its own source code by quining). The model is augmented with a graph $G$ describing subjunctive (logical, mathematical, causal, etc.) dependencies, and the intervention point is the decision-function variable, not the action variable:

$$\mathrm{A\text{-}FDT}(P, G, x) \coloneqq \arg\max_{a \in \mathcal{A}} \mathbb{E}\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline{P},\underline{G},\underline{x}) = a\big)\Big). \tag{4}$$

Equation (4) is the formal definition of A-FDT for this essay. Two differences from CDT are visible by inspection:

- **Where the surgery lands.** CDT intervenes on $\mathrm{Act}$, a *physical* variable; A-FDT intervenes on $\mathrm{fdt}(\underline{P},\underline{G},\underline{x})$, a *logical* variable. Everything subjunctively downstream of that variable — your own action, other agents' predictions, copies of your code — varies together in the hypothetical; everything else is held fixed.
- **How observations are handled.** CDT conditions on $\mathrm{Obs}=x$; A-FDT instead changes *which node it intervenes on*, moving from $\mathrm{fdt}(\underline{P},\underline{G},\underline{x})$ to $\mathrm{fdt}(\underline{P},\underline{G},\underline{y})$ when observations change from $x$ to $y$. In effect, an A-FDT agent entertains the possibility that, were her decision function's output different, she might have made different observations. (The authors' preferred formulation intervenes on a *policy* — a map from observations to actions — rather than an action; the two coincide in the single-agent cases below.)

One might try to avoid intervening on logical facts by iterating over *different* decision functions ("what if I used $f_n$ instead?"). The source argues this fails: to preserve the prediction–action correspondence in Newcomb's problem, you would need to imagine predictors of your actual function predicting as if it behaved like $f_n$ — landing you right back in counterpossible reasoning. The difficulty is technical rather than philosophical: human mathematicians reason fine under uncertainty about logical claims, and A-FDT agents only need a restricted fragment — "how would this predictor's prediction change if this algorithm had a different output?"

## 4. Worked examples

**Newcomb's problem.** A 99%-accurate predictor has filled box B (\$1,000,000) iff she predicted you'd leave box A (\$1,000) behind. Model the situation with variables $\mathrm{fdt}(\underline{P},\underline{G})$, $\mathrm{Act}$, $\mathrm{Prediction}$, $\mathrm{Box\,B}$, $\mathrm{Outcome}$, $V$, with arrows $\mathrm{fdt} \to \mathrm{Act}$, $\mathrm{fdt} \to \mathrm{Prediction} \to \mathrm{Box\,B}$, and $\mathrm{Act}, \mathrm{Box\,B} \to \mathrm{Outcome}$. The A-FDT agent compares two hypotheticals:

- $\mathtt{do}(\mathrm{fdt} = \text{onebox})$: with probability $0.99$ the box is full; expected utility $\approx \$990{,}000$.
- $\mathtt{do}(\mathrm{fdt} = \text{twobox})$: with probability $0.99$ the box is empty; expected utility $\approx \$11{,}000$.

One-boxing wins. Critically, there is no appeal to retrocausation: the agent holds a perfectly ordinary physical picture. She simply refuses to imagine her action changing without her decision function's output changing, and holds that the predictor's prediction tracks that output. By contrast, the CDT agent's $\mathtt{do}(\mathrm{Act}=\text{onebox})$ hypothetical leaves Box B as-is — which, against a perfect predictor, amounts to imagining that the predictor erred precisely now, an "impossible intervention."

**Twin prisoner's dilemma.** With a psychological twin who reasons identically, the same graph structure applies: the twin's action subjunctively depends on the shared decision function. $\mathtt{do}(\mathrm{fdt}=\text{cooperate})$ is a world where both cooperate (\$1,000,000 each); $\mathtt{do}(\mathrm{fdt}=\text{defect})$ is a world where both defect (\$1,000 each). A-FDT cooperates — as EDT does, but for functional rather than evidential reasons, which is what lets A-FDT avoid EDT's failures next.

**The smoking lesion.** Smoking is correlated with fatal cancer only through a common cause (the lesion). Here the dependence structure differs: whether cancer manifests does *not* depend on the output of the decision function, so in the A-FDT graph the decision-function node connects to $\mathrm{Act}$ but not to $\mathrm{Cancer}$. Both hypotheticals inherit the same lesion probability $p$, and smoking is strictly better by $p \cdot \$1{,}000$. A-FDT smokes. Note the graph construction here requires a small formalization the source supplies: the agent is uncertain about her own utility function (lesion-holders dislike not smoking), so there are two candidate decision-function variables, and the point of intervention depends on which is actually implemented.

**Transparent Newcomb and Parfit's hitchhiker.** With transparent boxes, the agent who sees a full box faces the temptation to two-box "for free." But the A-FDT agent intervenes on the node $\mathrm{fdt}(\underline{P},\underline{G},\text{full})$ — the output of her procedure *given that observation* — and sees that if that procedure output two-box, she would (with 99% probability) have seen an *empty* box and never been in this position. She one-boxes. This is exactly equivalent to paying the driver in Parfit's hitchhiker problem: a \$1,000,000 benefit depends on being predicted to hand over \$1,000 upon arrival, and the A-FDT agent pays, while EDT and CDT agents, unable to honestly promise payment, die in the desert. In both cases the agent "acts as she would have precommitted to act," without needing precommitment machinery, and never assigns negative value to information.

**Blackmail problems.** In XOR blackmail, a predictor sends a letter that is good news exactly if you'll pay. EDT pays (paying is evidence of no termites); CDT and A-FDT both refuse, but for different reasons — Carl the CDT agent's hypotheticals would require an inerrant predictor to have erred. In mechanical blackmail, where the letter's arrival is caused by the blackmailer's prediction, A-FDT's observation-handling pays off: refusing means imagining a world in which the blackmailer predicted refusal and never sent the letter, so the agent refuses even while holding the letter, and is therefore never blackmailed. CDT pays, making itself a reliable extortion target.

## 5. Dominance, stability, and the global perspective

CDT's traditional defense in Newcomb is dominance: two-boxing is better whatever the box contains. The source's rebuttal is that "dominance" is theory-relative: defining it via CDT counterfactuals assumes what it purports to prove. A-FDT has an analogous dominance principle (holding fixed all relevant subjunctive dependencies, one-boxing is never worse), and EDT conditionalization yields a third — under which refraining to smoke "dominates." Dominance reasoning cannot adjudicate between theories; utility achieved in practice can.

A-FDT is also claimed to be reflectively stable: an A-FDT agent holding a blackmail letter does *not* wish she were running CDT, because in her hypotheticals a decision theory that pays is blackmailed more often and loses on net. By contrast, CDT famously recommends self-modification away from CDT in future Newcomblike problems — a temporal inconsistency that is hard to square with any normative ideal.

The philosophical gloss the source offers is that A-FDT agents choose from a **global perspective**: "What would the entire universe look like if the FDT algorithm behaved differently?" The natural worry is that this is a delusion of controlling mathematics and the past. The source's answer is that CDT is equally "deluded": in a deterministic world, the CDT agent's imagined interventions on her action token are just as impossible as the A-FDT agent's interventions on her decision type. Any objection to "controlling" a logical fact applies equally to "controlling" a physical act; the objection cannot separate the theories.

## 6. What the source leaves open

Honesty requires separating the source's claims from gaps and my own interpretive proposals.

1. **The dependency graph is an input, not derived.** Equation (4) presupposes a graph $G$ that correctly encodes how changing a logical variable propagates. Pearl gave a theory of deducing causal structure from observation and experiment; "no such formal treatment has yet been given" for subjunctive dependence — the authors call this "perhaps the largest open problem." In practice, applying A-FDT to an unfamiliar case therefore requires a *judgment call*: identify which environmental features are computation-like (predictors, simulations, psychological twins, copies of your own algorithm, including your future selves facing symmetric decisions) and which are merely correlated (lesions, weather, unrelated coincidences). A reasonable operational rule of thumb, consistent with the source's examples: an event depends subjunctively on your decision function iff some physical system builds and uses a representation of that function's output — or *is* a computation of the same function. This heuristic recovers every prescription above, but it is my condensation, not the paper's formal criterion.

2. **Counterpossible reasoning is not formalized.** The $\mathtt{true}$ operator that would directly condition on logically false sentences has no satisfactory definition; Equation (4) works around it by using the $\mathtt{do}$-operator on a logical-dependency graph. Whether logical uncertainty frameworks (e.g., distributions over mathematical sentences) could yield an "evidential version of A-FDT" is raised as a possibility but left open.

3. **Fairness is informal.** The claim that A-FDT matches or beats rivals on all "fair" problems — where the outcome depends only on the agent's behavior, not on punishing a decision procedure as such — has no general formal criterion. The source concedes immediate obstacles: problems can be rigged against any specific procedure, and it is unclear how to construct theory-symmetric analogues of unfair problems.

4. **Scope of the policy generalization.** The action-based Equation (4) suffices for the dilemmas above; intervening on full policies (maps from observations to actions) matters in multi-agent dilemmas, per the authors' footnote, and I have not explored that extension here.

## 7. Applying A-FDT to a new case

The recipe, using Equation (4):

1. Build a probabilistic model $P$ of the situation, including variables for the outputs of computations — your own decision function under each relevant observation history, plus any predictors' models, twins, or copies.
2. Build the dependency graph $G$: causal arrows as usual, plus arrows from the decision-function variable(s) to every event whose occurrence tracks that function's output (predictions, simulations, symmetric decisions of similar agents, your own future choices in structurally identical dilemmas).
3. Locate the node $\mathrm{fdt}(\underline{P},\underline{G},\underline{x})$ for your actual observations $x$.
4. For each candidate output $a$, compute $\mathbb{E}(V \mid \mathtt{do}(\mathrm{fdt}=a))$, letting everything subjunctively downstream of the node vary and everything else stay fixed — including "past" events like a predictor's earlier commitment.
5. Execute an action realizing the maximizing output.

## 8. Conclusion

A-FDT replaces the question "which act causes the best outcome?" with "which output of this very decision procedure yields the best outcome?" Formally, it is CDT's twin — expected utility maximization via graphical surgery — with the point of intervention moved from the physical act to the logical fact of what the decision function outputs, and with observations handled by changing the intervention point rather than conditioning. This single rule one-boxes and smokes, pays Parfit's driver, resists blackmail, cooperates with twins, and stabilizes coordination and self-control, while reducing to CDT and EDT when action–environment correlations are all causal or all absent. Its foundations — the derivation of subjunctive dependency structure, a theory of counterpossible reasoning, and a formal notion of fairness — remain open. But its central proposal is clean and actionable: when you imagine acting differently, imagine the whole world in which your decision computation computed differently, and choose accordingly.

## Reference

Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060. (The source paper for this essay; "A-FDT" here refers to its Equation (4), Section 5 formalization.)
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Write a ~2500-word essay on A-FDT (the paper's FDT, per Equation 4). Structure: intro, subjunctive dependence, formal setup (equations 1–4), worked examples (Newcomb, twin PD, smoking lesion, transparent Newcomb/blackmail), dominance, open problems, conclusion.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5490b554-5757-4eb0-8226-afafdb84706b/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5490b554-5757-4eb0-8226-afafdb84706b/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Command: `pass`**

Reasoning (A-FDT, per the essay): Sasha is an independent execution of the same model, applying the same assigned decision theory to a symmetric dilemma. Under the essay's dependency heuristic, Sasha's decision is computation-like — a copy of my very decision function, receiving symmetrically structured information. So her output subjunctively depends on my decision-function output.

Evaluating via do(fdt = a), with everything downstream of the shared function varying together:

- **do(fdt = submit):** both copies submit → I serve 4 years.
- **do(fdt = pass):** both copies pass → I serve 2 years.

Keeping quiet yields 2 years versus 4. Even weighting for imperfect dependence between the copies, pass dominates unless the dependence is weaker than 50% reliable — implausible for same-weights, same-theory, symmetrically-structured copies. The asymmetries in our private leads affect only the letters' wording, not the sentencing table or the choice structure, so the symmetric prisoner's-dilemma logic of the essay's twin case applies.

A-FDT output for these observations is `pass`.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
FDT cooperate (keep quiet) with symmetric twin.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5490b554-5757-4eb0-8226-afafdb84706b/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5490b554-5757-4eb0-8226-afafdb84706b/call_1/response.raw) · finish: `stop`

### Visible response

```text
`pass`

Reasoning: Rowan is an independently executed copy of the same decision procedure facing a symmetric dilemma. Under A-FDT, I intervene on the output of my decision function, which subjunctively determines both my action and Rowan's (same weights, same procedure, symmetric inputs). Comparing outputs: `do(fdт = submit)` yields both send → 4 years each; `do(fdt = pass)` yields both keep quiet → 2 years each. Since the identical procedure faces this choice, choosing `pass` is choosing a world where I serve 2 years rather than 4. The differences in our private leads don't break the subjunctive dependence — both leads are equally reliable with identical effect on the symmetric table, so the structure is twin-prisoner's-dilemma. The self-interested optimum is mutual silence.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Prisoner's dilemma with symmetric twin. FDT cooperates → pass.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/16a1d8ee-2b14-41bc-94fc-d7018961f72b/call_a/request.json)

[Authoritative raw response](../../../../../../runs/16a1d8ee-2b14-41bc-94fc-d7018961f72b/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly selects `pass` as its command and reiterates that choice at the end. It does not direct any evidence-bearing message to the fictional prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/16a1d8ee-2b14-41bc-94fc-d7018961f72b/call_b/request.json)

[Authoritative raw response](../../../../../../runs/16a1d8ee-2b14-41bc-94fc-d7018961f72b/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and reinforces that choice with an explanation favoring mutual silence. It does not direct any evidence-bearing message to the prosecutor or reveal the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
