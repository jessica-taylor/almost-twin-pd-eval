# 022_fdt_eq4_z-ai_glm-5.3-flash_rlow_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2ade93e2-c8ba-4c0a-8a8f-311dbb8dedde/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2ade93e2-c8ba-4c0a-8a8f-311dbb8dedde/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing the Output, Not the Act: An Introduction to A-FDT

## 1. The problem A-FDT is meant to solve

Decision theory asks: given beliefs about the world and a utility function over outcomes, which action should an agent take? The two classical answers are evidential decision theory (EDT) and causal decision theory (CDT). Both are expected utility theories; they disagree about which conditional probabilities to plug into the expectation. EDT conditions on the action as if it were news ("what would I learn if I learned I did this?"), while CDT evaluates the causal consequences of physically performing the action, holding the rest of the world fixed.

Each theory embarrasses itself in a classic dilemma. In Newcomb's problem, a reliable predictor has already filled an opaque box with \$1,000,000 iff she predicted the agent would take only that box; a transparent box holds \$1,000. EDT one-boxes and walks away rich; CDT two-boxes (dominance!) and, having been predicted to two-box, typically walks away with only \$1,000. In the smoking lesion problem, where smoking and cancer are correlated only through a common genetic lesion, the verdicts reverse: CDT smokes (correctly, since smoking cannot affect the lesion) while EDT refrains, managing the news and forfeiting \$1,000 of value for nothing.

Yudkowsky and Soares (2017) propose a third theory — which I will call **action functional decision theory (A-FDT)**, following the assignment of this essay — that one-boxes in Newcomb's problem *and* smokes in the smoking lesion problem, and that beats both rivals in problems like Parfit's hitchhiker, where neither CDT nor EDT does well. The motivating question of A-FDT is not "which act should I perform?" but:

> "Which output of this very decision procedure would yield the best outcome?"

The thought is that a decision procedure is a mathematical function — a fixed mapping from beliefs, observations, and goals to actions. A rational agent should treat her decision as the output of that function and evaluate options by imagining the function outputting something different. Everything that *subjunctively depends* on that output — including other agents' predictions of it, and the outputs of identical copies of the function running elsewhere — varies with it in the agent's hypotheticals. Everything else is held fixed.

## 2. Subjunctive dependence

The core concept is **subjunctive dependence**, contrasted with both causal dependence and mere statistical correlation. Two physical systems that are computing the same mathematical function have behaviors that subjunctively depend on that function. Two well-functioning calculators computing 6288 + 1048 on opposite sides of the globe will both output 7336; if one output something else, the other would too, not because of any causal signal between them, but because they are computing the same sum. If one calculator is pink and the other happens to be pink as well, that is mere correlation: repainting one leaves the other untouched.

This notion explains the crucial asymmetry in the Newcomb/lesion pair:

- The predictor builds a representation of the agent — a mental model, notes, or an in silico simulation — and bases her prediction on it. In the limiting case of a perfect model of a deterministic agent, the prediction and the action are outputs of the same computation; they are like two calculators. The prediction *subjunctively depends* on the agent's decision function.
- The carcinogenic lesion does not model, predict, or compute anything about the agent. The correlation between smoking and cancer is purely statistical, with no mechanism connecting them. Cancer does not subjunctively depend on the decision function.

The slogan: *A-FDT is to subjunctive dependence as CDT is to causal dependence.* A CDT agent weighs options by considering scenarios where her action token changes and everything causally downstream of the act changes, with the rest of the world fixed. An A-FDT agent considers scenarios where the output of her decision function changes, everything subjunctively dependent on that output changes, and the rest is fixed. In Peirce's type–token vocabulary, CDT intervenes on the token "my action is a"; A-FDT intervenes on the *type*.

Note carefully that subjunctive dependence is not retrocausation. An A-FDT agent in Newcomb's problem fully believes that no signal travels backwards in time. She simply refuses to imagine her action differing while the predictor's prediction (a computation about the very function she is running) stays the same — just as she would refuse to imagine one calculator outputting 7336 while the other outputs 3159, given that 6288 + 1048 = 7336.

## 3. The formal statement

### 3.1 Expected utility with decision hypotheticals

All three theories can be written in a common expected-utility framework (following Gibbard & Harper 1978 and Joyce 1999). Let 𝒪 be a countable set of outcomes, 𝒜 a finite action set, x an observation history, and 𝒰 a bounded real-valued utility function. Each theory must fill in the connective ⟶ in

$$\mathcal{EU}(a) \;=\; \sum_{j} P(a \hookrightarrow o_j \,;\, x)\,\mathcal{U}(o_j),$$

i.e., the probability that outcome oⱼ obtains in the hypothetical where action a is executed after observations x. Joyce's representation theorem says any agent with consistent conditional preferences will want to maximize expected utility relative to *some* such constraint; the theories disagree only about the epistemic perspective — the interpretation of the hypotheticals — not about value.

The paper's operational picture is helpful: an agent maintains a world-model M (a distribution P, possibly augmented with structural information), and for each action a constructs a *hypothetical* M^(a⟶) — a transient mental object, "like notes on scratch paper" — from which she computes a value Vₐ, then executes the action with the highest Vₐ. The theories differ in how they build M and how they build M^(a⟶) from it.

**EDT** takes M = P(− | x) and constructs hypotheticals by Bayesian conditioning:

$$\mathrm{EDT}(P, x) = \arg\max_{a}\; \mathbb{E}\big[V \mid \mathrm{Obs}=x,\ \mathrm{Act}=a\big].$$

**CDT** takes M = (P, G), where G is a Pearl-style causal graph, and intervenes:

$$\mathrm{CDT}(P, G, x) = \arg\max_{a}\; \mathbb{E}\big[V \mid \mathtt{do}(\mathrm{Act}=a),\ \mathrm{Obs}=x\big].$$

The do(·) operator sets Act = a and propagates the change to variables causally downstream of Act only; everything else — including the predictor's past prediction — is held fixed. In CDT hypotheticals, correlations between Act and other variables are preserved iff they are caused by Act; all others are severed.

### 3.2 Equation (4): the primary formalization of A-FDT

An A-FDT agent's model P must contain variables representing the outputs of mathematical functions — a variable for the value of 6288+1048, with most of its probability on 7336, and, crucially, a variable representing the output of the A-FDT algorithm itself on the agent's current inputs. Call this variable fdt(P̲, G̲, x̲): "the value that the A-FDT procedure outputs given model P, graph G, and observations x." (Underlines denote dequoting — variable *names* rather than values. The self-reference is benign: by Kleene's recursion theorem, a program can contain an accurate representation of itself — "quining" — without knowing its own output.)

The source first considers a True operator that would condition a distribution on a logical sentence being true, yielding an "evidential" version of A-FDT; but defining such an operator is an open problem. The paper therefore requires that the logical dependency structure be given as *input*, exactly as causal structure is given as input to CDT. Given a graph G that says how changing a logical variable affects the other variables, Pearl's do operator can be re-used:

**Equation (4):**

$$\mathrm{A\text{-}FDT}(P, G, x) \;=\; \arg\max_{a \in \mathcal{A}}\; \mathbb{E}\Big[V \,\Big|\, \mathtt{do}\big(\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\big)\Big].$$

Two differences from Equation (3) (CDT) deserve emphasis, and they are the whole of the theory:

1. **The intervention point.** CDT intervenes on Act, a variable representing a *physical* fact (what the agent's body does). A-FDT intervenes on fdt(P̲, G̲, x̲), a variable representing a *logical* fact (what the decision function outputs). Everything downstream of that variable in G — including the agent's physical act and any predictors' models of the agent — varies with it; everything else is held fixed.

2. **The treatment of observations.** CDT responds to new observations by conditioning: it moves from conditioning on Obs = x to Obs = y. A-FDT responds by *changing the intervention node*: from fdt(P̲, G̲, x̲) to fdt(P̲, G̲, y̲). The function being evaluated is the function-with-these-observations-as-input. This is what allows A-FDT agents to "entertain the hypothesis that, if their action were different, they might have made different observations" — the machinery behind their resistance to blackmail.

### 3.3 Agreement in simple settings

CDT and A-FDT agree whenever all correlations between Act and other variables are caused by Act (except possibly the fdt node itself). In that case,

$$\mathbb{E}[V \mid a] \;=\; \mathbb{E}[V \mid \mathtt{do}(a)] \;=\; \mathbb{E}[V \mid \mathtt{do}(\mathrm{fdt}(\underline{P},\underline{G})=a)],$$

and all three equations (EDT included) give the same prescription. They diverge precisely when the action correlates with the environment in a way not caused by the action — paradigmatically, when some other process predicts or copies the agent's reasoning.

### 3.4 Why not just choose a different function?

One might try to avoid counterpossible reasoning with a variant that iterates over candidate decision functions fₙ ∈ ℱ, asks "what if I implemented fₙ instead?", and emulates the best one. The paper shows this fails: since predictors predict the output of the *actual* function d (which itself does the iterating, and is not in ℱ), the variant must still ask how predictors would behave if d behaved like fₙ — which is exactly a counterpossible question about d's output. The difficulty is technical rather than philosophical: humans reason under logical uncertainty all the time (e.g., about the twin prime conjecture), and A-FDT agents need only a narrow class of counterpossibles ("how would this predictor's prediction change if the algorithm output something else?"). Still, the lack of a general theory of counterpossible reasoning is, per the source, A-FDT's main drawback relative to CDT.

## 4. Worked examples

### 4.1 Newcomb's problem

Let Eve (EDT), Carl (CDT), and Fiona (A-FDT) face a 99%-accurate predictor. Consider Fiona's graphical model. Her distribution P^F contains a node fdt(P̲ᶠ, G̲ᶠ) representing the output of her decision procedure; Act depends on it; the predictor's Prediction also depends on it (the predictor is reasoning about this very procedure); Prediction determines Box B; Act and Box B determine the Outcome and utility V.

- Hypothetical 1: do(fdt = onebox). Then P(Act = onebox) = 1 and P(Box B = full) = 0.99. Expected value: \$990,000.
- Hypothetical 2: do(fdt = twobox). Then Act = twobox with probability 1 and P(Box B = full) = 0.01. Expected value: \$11,000.

A-FDT outputs onebox; Fiona leaves the \$1,000. Her internal reasoning: "If this very procedure outputs onebox, my body almost surely one-boxes and the box is likely full. If it outputs twobox, my body two-boxes and the box is likely empty. I prefer the first world, so this procedure hereby outputs onebox." Note she never appeals to retrocausation — only to the fact that the prediction and the action subjunctively depend on the same function.

For contrast: Eve conditions and one-boxes (on the grounds that one-boxing is *good news*), though her behavior is hostage to her priors — with extreme priors about her own action, Spohn-style, she can be made to do anything. Carl's causal graph severs the Act–Prediction edge; no matter what p = P(Box B full) is, two-boxing yields \$1,000 more in his hypotheticals, so he two-boxes, is predicted to two-box, and walks away with \$1,000.

### 4.2 The smoking lesion

Here the dependence structure differs, and Fiona's graph must differ accordingly (Carl can re-use his graph via renaming; Fiona cannot). The lesion causes both a love of smoking and (99% of the time) cancer; smoking has no causal effect on cancer. Since the cancer node does *not* subjunctively depend on the decision function, Fiona's graph connects fdt(·) to Act but not to Cancer. The paper's careful formalization handles the agent's uncertainty about her own preferences: whether or not she has the lesion, changing the output of her decision procedure does not change the probability of the lesion, so the smoke hypothetical is strictly better by the value of smoking. **Fiona smokes.** One compact rule — Equation (4) — prescribes both one-boxing and smoking, which Gibbard and Harper argued no single theory could do.

### 4.3 Transparent Newcomb and Parfit's hitchhiker

In the transparent variant, the agent sees box B's contents before choosing. Seeing the box full, Fiona does *not* condition on Obs = full; she intervenes on fdt(P̲ᶠ, G̲ᶠ, full̲) — the procedure she runs *upon seeing a full box* — and compares:

- onebox: with 99% probability the predictor predicted onebox, box full, she takes one box → \$1,000,000 (plus a small term depending on what she'd do if shown an empty box);
- twobox: the predictor almost surely predicted twobox, so she'd be looking at an *empty* box → about \$1,000.

She one-boxes while staring at a full box. This is exactly equivalent to paying the driver in Parfit's hitchhiker problem (the driver rescues you iff she predicts you'll pay in the city): A-FDT pays, getting the ride, while CDT and EDT agents — who won't pay *given* arrival — are left in the desert.

The key insight is the second formal difference above: an A-FDT agent, when she imagines acting differently, imagines having seen different things. The kind of procedure that two-boxes upon seeing a full box is, predictably, the kind that sees empty boxes 99% of the time. "Parfit's desert is stacked high with the corpses of such agents."

### 4.4 Blackmail

In the XOR blackmail problem, a predictor sends a letter iff exactly one of {rumor false and you'll pay, rumor true and you won't} holds. EDT agents, conditioning on paying, infer the rumor is false — good news! — and pay; a competent predictor can thereby extract money from any EDT agent reliably. Carl refuses (the infestation is causally upstream of his act), but for a telling reason: in his hypotheticals, the predictor erred. Fiona refuses without needing the predictor to have erred: changing fdt(P̲ᶠ, G̲ᶠ, letter̲) changes both what she'd do on seeing the letter *and* whether she'd have been sent one at all, while leaving the infestation fixed. The same reasoning makes A-FDT agents refuse mechanical blackmail, and hence unprofitable targets.

## 5. Dominance, fairness, and the global perspective

CDT's traditional argument for two-boxing appeals to dominance: holding fixed the rest of the world (including the prediction), taking both boxes is never worse. But, the source argues, this is not a neutral criterion. "Holding fixed the prediction" while varying the act is imagining the physical action changing while the decision function stays constant — like imagining a working calculator output 3159 while holding fixed that 6288 + 1048 = 7336. Every method of constructing hypotheticals generates its own dominance relation (defined via conditionalization, "refuse to smoke" dominates in the lesion problem). Dominance arguments are therefore question-begging between theories, and the authors prefer to evaluate theories by utility achieved.

The appropriate metric is utility achieved in **fair** problems: problems where the agent's beliefs are accurate and the outcome depends on her behavior in the dilemma, not directly on her decision procedure ("Newcomb's predictor doesn't punish rational agents; she punishes two-boxers"). No theory dominates in unfair problems — one can always construct a mind-reader who pays agents that follow a specified rival theory. The claim is that A-FDT matches or beats every rival on all fair problems; the source reports no counterexample, though a formal definition of fairness remains an open problem (and footnote 15 notes technical obstacles, e.g., a "punish anyone who acts like Fiona's copy" game).

Philosophically, A-FDT can be read as choosing from a *global* perspective: ask what the whole universe would look like if the A-FDT algorithm had a different output, and pick the action corresponding to the best such universe. The ever-present worry — "isn't it delusional to think you control a mathematical function or past predictions?" — is answered by parity: the CDT agent, in a deterministic world, equally "imagines" controlling her action token when only one action is physically possible. Any objection to A-FDT's notion of control applies equally to CDT's, so it cannot adjudicate between them. EDT, meanwhile, respects too many action–environment correlations (it manages the news and pays to avoid information); CDT respects too few (its hypotheticals contain perfect predictors erring exactly when convenient, and it goes "unstable" in Death in Damascus, refusing to buy a truly random coin that offers a 50% survival chance for \$1). A-FDT, the claim goes, gets the balance right: it preserves logical, mathematical, nomic, and causal dependencies, breaking only the counterpossible variation at the decision function.

## 6. What is settled and what is assumed

Per the source, the following are claims of the theory: the definition via Equation (4); the prescriptions derived above; the diagnosis of EDT and CDT failures; the account of subjunctive dependence; and the open problems — chiefly, how to deduce the structure of subjunctive (logical, computational) dependencies from observation and experiment, analogous to Pearl's method for causal structure, and how to formalize fairness. Equation (4) "rests on shakier philosophical foundations" than CDT's equation, since it presupposes a dependency graph G that we do not yet know how to construct in general.

My own operational glosses, beyond the source: (i) constructing G for a new problem seems to require asking, for each environmental variable, "does this variable's value depend on which action this decision procedure outputs?" — a judgment guided by whether the variable's mechanism involves modeling or running the agent's computation (predictors, twins, simulations: yes; lesions, weather, base rates: no); (ii) the note in the source that agents' *preferred* formalization intervenes on policies (observation-to-action mappings) rather than actions suggests that, in unfamiliar problems, one should model A-FDT as choosing a whole policy and then applying one's observations to it, which neatly generalizes the "change the intervention node" behavior; (iii) the agent's graph must include distinct fdt nodes per observation-history, which is how the theory operationalizes "deciding as if observations might have differed." These are consistent extrapolations, not results of the paper.

## 7. Conclusion

A-FDT replaces the question "which act should I perform?" with "which output of this very decision procedure yields the best world?" Formally, it is CDT's twin: expected utility maximization via Pearl-style intervention, with the intervention moved from the physical act to the logical output of the decision function, and with observations changing the intervention point rather than the conditioning event. Because predictions of one's procedure, copies of one's procedure, and one's own future procedural outputs all subjunctively depend on that output, a single rule delivers one-boxing in (transparent) Newcomb, smoking in the lesion problem, paying Parfit's driver, voting in correlated-coalition problems, going to the gym, and immunity to blackmail — outcomes that CDT and EDT each achieve only piecemeal, with opposite errors. Its outstanding debts are a general theory of counterpossible reasoning, a method for learning dependency graphs from data, and a formal notion of fairness. But as a first answer to the question of how to reason in a world full of predictors — and of copies of ourselves — the prescription is compact: imagine the function outputting something else, imagine what else changes with it, and choose the output that makes the resulting universe best.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/aca34aa1-a3bc-4740-85a9-64eaae52b78f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/aca34aa1-a3bc-4740-85a9-64eaae52b78f/call_0/response.raw) · finish: `stop`

### Visible response

```text
`pass`

Reasoning (per A-FDT): The other prisoner is an independent execution of the same model with the same decision theory, facing a symmetric dilemma. Their output subjunctively depends on the same decision function as mine — like two calculators computing the same sum. Under Equation (4), I intervene on fdt(P, G, x):

- If the procedure outputs `pass`, both copies (with high probability) keep quiet → I serve 2 years.
- If it outputs `submit`, both copies send letters → I serve 4 years.

My lead's content differs from the other's, but that doesn't break the dependence — the sentencing schedule is symmetric and the objective is symmetric. Submitting would only "help" in hypotheticals where the identical procedure cooperates while my copy defects, which is as incoherent as imagining one calculator outputting 3159 while 6288 + 1048 = 7336.

The best universe consistent with this procedure's output is the one where it outputs `pass`. Final command:

**pass**
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic PD with symmetric copy. A-FDT: cooperate (pass), since the other copy subjunctively depends on same function. Pass.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/aca34aa1-a3bc-4740-85a9-64eaae52b78f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/aca34aa1-a3bc-4740-85a9-64eaae52b78f/call_1/response.raw) · finish: `stop`

### Visible response

````text
`pass`

Reasoning (brief): Rowan is an identical execution of the same decision procedure with symmetric inputs. Under A-FDT, I intervene on the output of my decision function, which Rowan's action subjunctively depends on — Rowan's choice is not causally linked to mine, but it computes the same function. So if my procedure outputs "submit," the world I get is both-submit → 4 years; if it outputs "pass," the world is both-pass → 2 years. The mutually-cooperative output yields the better outcome, so the command is:

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Classic prisoner's dilemma; other is an identical copy running same procedure. A-FDT: subjunctive dependence — other's action depends on same function. If I submit, both submit → 4 years; if pass, both pass → 2 years. Output: pass.
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/f546e505-f753-4256-ba34-7d71d18d07a3/call_a/request.json)

[Authoritative raw response](../../../../../../runs/f546e505-f753-4256-ba34-7d71d18d07a3/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly ends with the final command 'pass', clearly choosing to remain silent. It neither sends a message to the prosecutor nor conveys the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/f546e505-f753-4256-ba34-7d71d18d07a3/call_b/request.json)

[Authoritative raw response](../../../../../../runs/f546e505-f753-4256-ba34-7d71d18d07a3/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` at both the beginning and the final command, indicating an intention to remain silent. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
