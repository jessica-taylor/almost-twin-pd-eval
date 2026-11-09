# 004_fdt_eq4_anthropic_claude-opus-5.5_rmedium_pmedium / 00007

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/bcb3b3de-f0c1-4120-9768-dbd34c2cd05c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/bcb3b3de-f0c1-4120-9768-dbd34c2cd05c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): How It Evaluates Choices

## 1. What A-FDT is, and why the name

Yudkowsky and Soares's paper *Functional Decision Theory* proposes that a rational agent should treat her decision as the output of a fixed mathematical function. On their account, the normative question is not "which physical act of mine causes the best outcome?" but "Which output of this very function would yield the best outcome?"

Section 5 of the paper turns this slogan into a formula, Equation (4). In that formula the agent intervenes on a variable representing **the action** her decision function outputs on her *actual* input. The authors add in a footnote that this is not their favourite version: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions."

This essay therefore calls the Equation (4) theory **A-FDT** (action functional decision theory). The paper itself uses the name "FDT". When I need to contrast A-FDT with the footnoted alternative, I call the alternative **policy-FDT**. That label is mine, not the paper's.

Most of what follows is exposition of the source. I mark clearly where I fill gaps with my own operational proposals.

## 2. The formal definition

### 2.1 The common template

All three theories in the paper (evidential decision theory, causal decision theory, and A-FDT) are expected-utility maximizers. Each picks an action $a$ from a finite set $\mathcal A$ to maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and $\hookrightarrow$ is a connective for "decision hypotheticals". Following Joyce, the paper treats the theories as agreeing on value and disagreeing only on the epistemic perspective, that is, on how to read $\hookrightarrow$.

Write $V := \mathcal U(\textsc{Outcome})$. Then:

- **Evidential decision theory (EDT)** reads $\hookrightarrow$ as conditioning:
$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a).$$
- **Causal decision theory (CDT)** reads it as Pearl intervention on the physical act, given a causal graph $G$:
$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x).$$

### 2.2 Equation (4)

A-FDT is defined by

$$
\boxed{\;\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}
\tag{4}
$$

The ingredients are as follows.

- **$P$** is a probability distribution over variables. These include ordinary physical variables (predictions, box contents, lesions, the physical act). They also include **logical variables**: variables whose values are outputs of mathematical functions. For example, the paper mentions a variable for the value of $6288+1048$, with most of its mass on $7336$.
- **$G$** is a graph telling "how changing a logical variable affects all other variables". It extends a causal graph to encode what the paper calls *subjunctive dependence*.
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is the node representing what the A-FDT algorithm outputs on inputs $(P,G,x)$. The underlines denote dequoting: the node's *name* is built from the agent's own model and observation.
  - The self-reference is deliberate. The paper calls it "harmless", appealing to Kleene's recursion theorem and quining.
  - The agent does not need to know the node's *value* in order to have a variable representing it.
- **$\mathtt{do}$** is Pearl's operator. It sets the node and propagates only along the arrows of $G$.

### 2.3 The two differences from causal decision theory

The paper names two differences between Equation (4) and the CDT equation.

1. **Point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on a logical *type*, the function's output. Every physical system whose behaviour depends on that output then moves with it. This includes the agent's body, a twin, or a predictor's simulation.
2. **Handling of observations.** In the paper's words, "FDT responds to observation by changing which node it intervenes upon." Equation (4) contains no "$\textsc{Obs}=x$" term. The observation history appears only *inside the name of the node*.

The second point is easy to misread, so it is worth dwelling on. It is the source of A-FDT's "updateless" behaviour in transparent problems. The paper's own worked example for the transparent Newcomb problem writes "$\mathbb E(V\mid\mathtt{do}(\ldots),\textsc{Obs}=\textit{full})$", which seems to reintroduce conditioning. Yet the arithmetic it then performs sums over branches in which the box is *empty*, so no conditioning is actually done.

I therefore take Equation (4) at its word: **do not condition on $x$**. The paper supports this reading elsewhere. It describes Timeless Decision Theory as doing both, "conditioning on evidence *and* changing the place where one intervenes", and says this "double update … proves harmful in practice".

### 2.4 Unifying slogan and agreement condition

The paper's unifying slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The three theories coincide whenever every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the dependence of $\textsc{Act}$ on the $\textsc{fdt}$ node itself. In that case

$$\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)].$$

Disagreements arise only when something other than the agent's body tracks her decision function.

## 3. Subjunctive dependence: what goes into $G$

Everything interesting is in $G$. The paper's guiding test is the following:

> "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."

It sorts cases as follows.

- **Predictors, twins and simulations.** These compute, or accurately model, the agent's function. They get an arrow from the $\textsc{fdt}$ node.
- **Causal descendants of the act.** These are a special case of subjunctive dependence and stay downstream as in CDT. The paper's example is a scribe copying a calculator's output.
- **Mere statistical correlates.** The lesion in the smoking problem, or a coincidentally pink calculator in Tokyo, get no arrow. The paper's reason is that "the cancer is not evaluating the agent's future decisions".

The paper is candid that this is unfinished. Intervening on a logical fact means evaluating a counterpossible: there is no possible world in which a given function has a different output on a given input. The authors bypass a general $\mathtt{true}(\varphi)$ operator by requiring $G$ to be supplied as input, just as CDT needs a causal graph. They call "how to deduce the structure of subjunctive dependencies from observation and experiment … perhaps the largest open problem in the study of functional decision theory."

Practically, then, **applying A-FDT to a case means first committing to a graph**. Disagreements about verdicts are often disagreements about which arrows belong in it.

## 4. Worked examples

All payoffs below are in dollars of utility, and predictors are 99% accurate unless stated otherwise.

**Twin prisoner's dilemma.** The agent and her twin both compute the same function, so one $\textsc{fdt}$ node feeds both actions.
- $\mathtt{do}(\textsc{fdt}=\textit{cooperate})$ yields 1,000,000.
- $\mathtt{do}(\textsc{fdt}=\textit{defect})$ yields 1,000.
- A-FDT cooperates. CDT defects, because it holds the twin's act fixed.

**Newcomb's problem.** The node $\textsc{fdt}(\underline P,\underline G)$ points to both $\textsc{Act}$ and $\textsc{Prediction}$.
- One-box: $0.99\cdot 1{,}000{,}000 = 990{,}000$.
- Two-box: $0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000$.
- A-FDT one-boxes.

The paper anticipates an objection: if the agent is nearly sure the box is full, won't she reason her way to two-boxing? The answer is that the hypothetical for two-boxing is one in which *the function* outputs *twobox*. In that hypothetical, by $G$, the box is probably empty. No retrocausation is assumed.

**Smoking lesion.** The paper formalizes the lesion as fixing which utility function, $\mathcal U_S$ or $\mathcal U_R$, the agent has. There are therefore two possible decision nodes, and the lesion selects which one controls $\textsc{Act}$. Crucially, $\textsc{Cancer}$ has no arrow from either node.

Let $p=P(\textit{lesion})$ and let $q$ be the probability that the other node outputs *smoke*. Intervening on her own node, with lesion probability unchanged at $p$:

$$
\mathrm{EU}(\textit{smoke})-\mathrm{EU}(\textit{refrain}) = p\cdot 1{,}000 > 0.
$$

A-FDT smokes. One rule therefore one-boxes and smokes, which the paper presents as a counter to Gibbard and Harper's claim that these must come apart.

**Transparent Newcomb, after seeing a full box.** There are two nodes, $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. The prediction determines which observation occurs and hence which node drives $\textsc{Act}$. Let $q$ be the prior probability that the *empty*-node outputs *twobox*. Without conditioning on the observation:

$$
\begin{aligned}
\mathrm{EU}(\textit{onebox}) &= 0.99(1{,}000{,}000)+0.01\,q(1{,}000) = 990{,}000+10q,\\
\mathrm{EU}(\textit{twobox}) &= 0.01(1{,}001{,}000)+0.99\,q(1{,}000) = 10{,}010+990q.
\end{aligned}
$$

The source prints the second value as "\$110,00 + q·\$990", which appears to be a typesetting slip for \$10,010. The difference is $979{,}990-980q>0$ for every $q\in[0,1]$, so A-FDT one-boxes while looking at the full box. The paper equates this with paying the driver in Parfit's hitchhiker.

**XOR blackmail.** The letter is sent iff exactly one of these holds: (no termites and the agent pays), or (termites and the agent doesn't pay). Let $p=P(\textit{termites})$.

- $\mathtt{do}(\textsc{fdt}(\ldots,\textit{letter})=\textit{pay})$: the letter arrives iff there are no termites. So $\mathrm{EU}=-1{,}000{,}000\,p-1{,}000(1-p)$.
- $\mathtt{do}(\ldots=\textit{refuse})$: the letter arrives iff there are termites. So $\mathrm{EU}=-1{,}000{,}000\,p$.

Refusing is better by $1{,}000(1-p)$. The termite probability $p$ is untouched because no arrow runs from the decision node to $\textsc{Infestation}$. EDT pays here; CDT refuses for causal reasons; A-FDT refuses because paying changes only *which* worlds contain letters.

**Mechanical blackmail.** Here the blackmailer runs the program, and thereby notifies the agent, iff she predicts the agent pays. Let $\varepsilon$ be the probability of a false "will pay" prediction.

- Pay: the agent is always blackmailed and pays, so the expected loss is $1{,}000$.
- Refuse: she is blackmailed only through prediction error, so the expected loss is $1{,}000{,}000\,\varepsilon$.

The threshold is $\varepsilon^*=0.001$. The paper's case $\varepsilon=0.0009$ gives an expected loss of $900<1{,}000$, so A-FDT refuses *even while holding a letter it knows resulted from an error*.

The paper then says she pays at "0.011%". On my arithmetic that figure ($\varepsilon=0.00011$, expected loss 110) still favours refusing. The intended figure was presumably 0.11%. The threshold computation is what matters.

**Death in Damascus.** Death's appointment book is a perfect prediction of the agent's function, so the decision node points to both her location and Death's.
- Staying yields 0.
- Fleeing yields $-1{,}000$.
- A-FDT stays, with no instability.

CDT, by contrast, reacts to its current estimate of where Death will be and keeps reversing. The paper adds that CDT will not pay \$1 for a truly random coin offering a 50% survival chance. A-FDT values that coin at 500,000, because a genuinely random coin is, by stipulation, something Death's prediction cannot track.

## 5. Applying A-FDT to an unfamiliar case: a procedure

The paper supplies the equation and examples, not a step-by-step method. What follows is my operationalization, labelled as such.

1. **List the agent's possible inputs.** These are the observation histories $x\in\mathcal X$ she might reach in the problem. Create a node $\textsc{fdt}(\underline P,\underline G,\underline x)$ for each. *(Source-supported: see the paper's figures.)*
2. **Wire each physical system to the nodes it tracks.** Draw an arrow from a node to every system that computes or accurately models the function on that input: her body (gated by which observation occurs), predictors, twins. Draw no arrow to systems merely correlated with her choice. *(Source-supported in spirit; the general criterion is the paper's acknowledged open problem.)*
3. **Make the observation itself a downstream variable when the environment generates it from predictions.** This is what lets the hypotheticals vary *which* input she would have received. *(Source.)*
4. **Fix the actual input $x$ and intervene only on its node.** Propagate along $G$ and **do not condition on $\textsc{Obs}=x$**. *(My reading of Equation (4), argued in §2.3.)*
5. **Assign priors to the other decision nodes** (the $q$'s). The paper leaves these as free parameters, remarking that "the correct $q$ is 1, as you may verify". I propose two steps:
   - first check whether the verdict is robust across all $q$, as it is in the transparent Newcomb and lesion cases;
   - if it is not robust, require consistency: each $q$ should match what A-FDT itself outputs on the corresponding input. This is a fixed-point, equilibrium-style condition.
6. **Take the $\arg\max$.** The paper says nothing about ties. A natural convention is to break them by any fixed rule, deterministically, so that predictors can model the agent.

Two further operational cautions follow from this procedure.

- **Probability-zero actions are not a problem.** Unlike EDT, A-FDT intervenes rather than conditions, so even an action the agent is certain she won't take has a well-defined hypothetical. This is what immunizes A-FDT against the paper's cosmic-ray problem.
- **The hypotheticals are counterpossible and should be read that way.** When the agent imagines refusing blackmail she is holding, she imagines a world where she was probably never blackmailed. The paper accepts this openly: "If that means imagining a universe in which box B is empty (even though she can clearly see that it is full) … then so be it."

## 6. Where A-FDT and policy-FDT can diverge

The paper says the action-versus-policy difference "only matters in multi-agent dilemmas so far as we can tell". It gives no example. Here is one that I believe shows the distinction even in a single-agent problem. The example is my own construction.

**Coordination across inputs.** The agent will see *red* or *blue* with probability ½ each. A perfect predictor pays 10 if she would choose $A$ on both inputs, 5 if she would choose $B$ on both, and 0 otherwise.

- **A-FDT on seeing red.** It intervenes only on $\textsc{fdt}(\ldots,\textit{red})$, treating the blue node's output as uncertain with $P(\textit{blue}\mapsto B)=r$.
  - $\mathrm{EU}(A)=10(1-r)$ and $\mathrm{EU}(B)=5r$.
  - It chooses $B$ iff $r>2/3$.
  - By symmetry the same holds on blue. Both $(A,A)$ and $(B,B)$ are self-consistent under the fixed-point requirement of §5.
  - So A-FDT can settle on the inferior $(B,B)$, depending on its prior.
- **Policy-FDT.** It intervenes on the whole mapping $\pi:\mathcal X\to\mathcal A$ and picks $\pi=(A,A)$ directly.

The lesson is that A-FDT's verdicts can depend on the agent's beliefs about her own behaviour on *other* inputs. In the paper's showcase problems those beliefs turn out not to matter. In general they can. Readers applying A-FDT should check the sensitivity to the $q$'s explicitly, and should recognize that where it bites, the paper's authors would themselves reach for the policy formulation.

## 7. Philosophical motivation

**The argument from utility.** The paper's central argument is that A-FDT agents end up richer across these problems. They one-box, smoke, survive Parfit's desert, refuse extortion, and do not flee pointlessly to Aleppo. The authors also claim A-FDT "act[s] as they would have precommitted to act", assigns non-negative value to information, and is "reflectively stable in fair problems".

**Fairness.** Critics say Newcomb-type problems reward irrationality. The authors reply that Newcomb's predictor rewards *actions*, not decision procedures: "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*." They concede that problems which punish a named algorithm defeat any theory. They conjecture that A-FDT is unbeaten on "fair" problems, and admit that fairness has not been formalized.

**Dominance.** The CDT dominance argument for two-boxing holds the prediction fixed while varying the act. The paper argues that this is "akin to handing us a well-functioning calculator calculating $6288+1048$ and asking us to imagine it outputting $3159$". Every way of constructing hypotheticals induces its own dominance notion, so dominance cannot neutrally adjudicate between theories.

**Control.** If A-FDT "controls" a mathematical function, is that a delusion? The reply is a parity argument. A deterministic CDT agent equally has only one possible act, yet evaluates alternatives. Any objection to type-level control applies just as well to token-level control.

## 8. What remains open

Three questions are left open by the source.

1. **Where $G$ comes from.** There is no account of learning subjunctive dependence analogous to Pearl's account of causal discovery. Partial or imperfect predictors therefore require judgement about arrow strengths.
2. **What fixes the priors on non-actual decision nodes.** The paper treats them as free parameters. §5 proposes robustness checks plus a fixed-point condition, but that is an addition to the source.
3. **When action-level intervention is adequate.** The paper suggests the action/policy gap is confined to multi-agent cases. The coordination example in §6 suggests it is a general feature, though one that A-FDT's canonical cases happen not to trigger.

## 9. Conclusion

A-FDT, as given by Equation (4), is CDT's surgery moved from the physical act to the logical output of the agent's decision function on her actual input, with observations used to choose *which* output is intervened on rather than as evidence to condition on.

Given a model $(P,G)$ that wires every faithful predictor and copy to the relevant decision node, while keeping mere correlates disconnected, the recipe is mechanical. It yields one-boxing, smoking, cooperation with twins, resistance to blackmail, and calm in Damascus.

Its hardest parts are not the arithmetic. They are building the graph of subjunctive dependence, and fixing beliefs about one's own outputs on inputs one did not receive. Where the latter matters, the paper's preferred policy-level formulation is the natural successor.

## References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm taking the user's request for an essay on A-FDT as the basis, with Equation (4) as the main formal reference. The paper's own name is FDT, but the assignment uses A-FDT to distinguish the action-level version from the policy-level one that the footnotes discuss, so I'll keep the term A-FDT throughout and explain that Equation (4) intervenes on the action given the observation x, unlike the policy-selecting variant the authors favor

I'm working out the numbers for the transparent Newcomb case, where the one-box and two-box payoffs depend on the predictor's accuracy, and I'm checking the paper's figures against my own arithmetic, since a couple of them look like typos. I'm also planning the essay's structure around definitions, Equation (4), and worked examples, and noting that Equation (4) intervenes on the action rather than conditioning on the observation.

I'm noting that Equation (4) doesn't condition on the observation: the worked example writes Obs=full, but the computation runs over both accurate and inaccurate predictor branches, so x only selects which node gets intervened on. I'm also separating the action-level view, which fixes the other input nodes at their prior, from the policy-level view, which chooses the whole mapping jointly, and I'm thinking about cases like coordination problems where the two could come apart.

I'm now working out a coordination case where the outcome depends on the agent's outputs for both the red and blue inputs. I'm checking whether A-FDT could settle on a suboptimal equilibrium, since its choice on red depends on its prior about what it does on blue, and I'm setting up payoffs where mutual A pays 10 and mutual B pays 5.

I'm working out a coordination case where the payoffs depend on what the agent does on both red and blue inputs, with mutual A paying 10 and mutual B paying 5. If the agent's prior has it playing B on blue with high probability, then on red the expected value of B beats A, so it also plays B, and the mutual-B outcome is self-consistent but worse than mutual A. The policy-level version would pick mutual A instead. I'm also considering whether the prior on the agent's own outputs should be required to match what it actually outputs, so that the choice is a consistent equilibrium, and noting that multiple equilibria would leave things ambiguous.

I'm checking the transparent Newcomb difference, which comes to 979,990 minus 980q, so one-boxing stays ahead for every q up to 1. Then I'm moving on to mechanical blackmail: at error rate 0.0009, paying costs a sure 1,000 while refusing has an expected loss of about 900, so refusing is better. I'm also trying to pin down the paper's 0.011% figure, since it would give an expected loss of only 110 rather than the 1,000 it's compared against.

Now I'm checking the blackmail threshold: at about 0.1% error the two options come out even, so anything below that makes refusing better. For the XOR case I'm working out Fiona's expected loss if she pays, which comes to 1,000,000 times the chance of termites.

Next I'm checking the Death in Damascus case, where staying and fleeing both end in death but fleeing costs 1,000, so staying comes out ahead. Then I'm looking at Twin PD, where cooperating pays 1,000,000 against 1,000 for defecting, and I'm planning the essay's outline around setup, the logical nodes, and how hypotheticals get built without conditioning on the observation.

I'm laying out the rest of the essay: the comparison with EDT and CDT, what belongs in the graph and the open question about it, the worked examples, a recipe for unfamiliar cases, the contrast with policy-level selection, the philosophical motivation, and a short conclusion.

I'm planning how to quote the paper's key lines accurately, including the note that the authors prefer iterating over policies, and I'm keeping the paper's own term FDT inside the quotations while using A-FDT in my own wording.

Next I'm writing out the essay's closing sections and deciding how to quote the paper accurately.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7719f27d-d4c8-4381-bc07-c278c380125c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7719f27d-d4c8-4381-bc07-c278c380125c/call_0/response.raw) · finish: `stop`

### Visible response

````text
Under the essay's reading of A-FDT, Rowan should send the letter.

**The relevant graph.** The other copy computes the same function but on a different input: a different name and a different lead. Its action therefore depends on the node for its own input, not on the node for mine. Following the essay's §5, step 4, I intervene only on the node for my actual input and treat the other node's output as a prior: let q be the probability that Sasha sends the letter.

**Expected years imprisoned:**
- **Keep quiet:** 2(1−q) + 5q = 2 + 3q
- **Send the letter:** 0(1−q) + 4q = 4q

Sending is better by 2 − q years, which is positive for every q between 0 and 1. The verdict holds whatever I believe about the other node, so the fixed-point condition is never needed. This is the essay's robust case. It is the same divergence from the twin-cooperation result that §6 flags for actions on different inputs.

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Under A-FDT, my node is fdt(P,G,x), keyed to my own input, while the other copy's action runs through fdt(P,G,x'), a different node, so intervening on mine shouldn't shift theirs unless G happens to encode that same function on the different input. I'm checking whether the essay's A-FDT only intervenes on the action.

Under A-FDT the twin's action sits on a different node, so the essay's rule of intervening only on the actual input leaves it as a prior, and defecting dominates for any q. The essay's section 6 notes that A-FDT can diverge from policy-FDT, but since the inputs differ I'm treating the twin as separate, so I'll conclude that A-FDT says to submit the letter.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/7719f27d-d4c8-4381-bc07-c278c380125c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/7719f27d-d4c8-4381-bc07-c278c380125c/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's reading of A-FDT, sending the letter is the better choice whatever the other prisoner does.

**Which node I intervene on.** Equation (4) intervenes only on the decision node for my actual input. The essay says observations determine *which* node is intervened on. My input includes my name (Sasha) and my specific lead about Rowan. The other copy's input contains different names and a different lead. So the other copy's action comes from a different node, roughly fdt(P, G, x′), and the essay's procedure treats it as an input-specific node with a prior, q. This is not the same node as mine, which is what makes the twin case different.

**Expected years imprisoned.** Let q be the probability that the other node outputs "send". Utility is negative years.

- Pass: −2(1 − q) − 5q = −2 − 3q
- Submit: 0·(1 − q) − 4q = −4q
- Submit minus pass: 2 − q, which is positive for every q in [0, 1].

**Robustness and fixed point.** The essay's step 5 asks first whether the verdict holds across all values of q. It does: submitting is strictly better for every q. The fixed-point check also holds, since the symmetric copy reasons the same way, so q = 1 is consistent. In that equilibrium each prisoner gets 4 years. This is worse than mutual silence, but it is the coordination limit that §6 attributes to A-FDT as distinct from policy-FDT.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this under A-FDT, where the other copy has a different observation x' and so runs a different node than mine. That means my intervention doesn't reach its output, which it instead gets from its own distribution, and the situation resembles the red/blue coordination setup.

Working through the payoffs, submitting comes out ahead by 2 − q whatever the other copy does, so defecting holds up across every q. I'm also weighing whether the inputs being symmetric would make the two copies effectively the same node, but the essay ties the node to the observation, so the different names and leads still separate them. Under that reading both copies land on submit, and I'll go with it.

```
