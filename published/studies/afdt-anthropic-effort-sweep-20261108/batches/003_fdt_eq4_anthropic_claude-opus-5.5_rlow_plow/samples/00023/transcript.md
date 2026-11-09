# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00023

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/ff96cf1a-e033-48ef-9b5c-9d675ae964fb/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/ff96cf1a-e033-48ef-9b5c-9d675ae964fb/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding as a Function, One Action at a Time

## 1. The idea in one sentence

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes that a rational agent should treat her decision as "the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper offers several formulations of this idea. This essay takes one of them, Equation (4) of Section 5, as its object. That equation picks an **action** by intervening on a node that represents the output of the agent's decision procedure given her current inputs. I call this version **A-FDT** (action functional decision theory).

The source also mentions, in its footnotes 7 and 16, a "preferred formalization" in which the agent chooses a **policy**, meaning a whole mapping from observations to actions. I call that variant **P-FDT** (policy-selecting functional decision theory) to keep the two apart. I also refer to **CDT** (causal decision theory) and **EDT** (evidential decision theory), the paper's two foils.

The essay covers five things in order:
1. the formal definition of A-FDT;
2. a step-by-step procedure for applying it;
3. the paper's main examples, with the arithmetic worked out;
4. the places where Equation (4) underdetermines what to do, with operational proposals that I mark as my own;
5. the philosophical motivation.

## 2. Three expected-utility theories, one template

All three theories maximize expected utility. They differ in how they build the "hypothetical" for an action $a$, which the paper describes as a "mental or computational object" used to score $a$. Write $V := \mathcal U(\textsc{Outcome})$ and let $x$ be the observation history. The paper gives:

$$\mathrm{EDT}(P,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\,(V\mid \textsc{Obs}=x,\ \textsc{Act}=a) \tag{2}$$

$$\mathrm{CDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\,(V\mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x) \tag{3}$$

$$\text{A-FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\,\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big) \tag{4}$$

Here $P$ is a probability distribution over variables and $G$ is a graph. In CDT, $G$ encodes causal structure. In A-FDT, $G$ encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly." The underlines denote dequoting. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a *variable in the model* standing for the output of the A-FDT procedure on these very inputs. The paper defends this self-reference by appeal to Kleene's recursion theorem, or quining. The agent need not know the variable's value in order to represent it.

The operator $\mathtt{do}$ is Pearl's intervention. It sets the target node, deletes the arrows into it, recomputes everything downstream, and leaves everything else at its prior distribution.

Equation (4) differs from Equation (3) in two ways, both stated explicitly in the paper:

1. **Point of intervention.** CDT intervenes on $\textsc{Act}$, the physical act, which is a *token*. A-FDT intervenes on the output of the decision function, which is a *type*. Anything else that computes or accurately models that function lies downstream of the same node and moves with it. This includes a twin, a predictor's simulation, or one's own future self in a relevantly similar situation.
2. **Treatment of observation.** Equation (4) contains no conditioning on $\textsc{Obs}=x$. Observation enters only through the *name* of the node that is intervened upon. When the observation history changes from $x$ to $y$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead. The paper stresses this: "FDT responds to observation by changing which node it intervenes upon."

The second point is easy to miss and does a great deal of work. When an A-FDT agent evaluates an action, the probabilities of the hidden states (box contents, infestations, lesions) come from the prior model, adjusted only by what lies downstream of the intervened node. They are not the posterior after the observation. This is why the paper's footnote associates the theory with Wei Dai's "Updateless Decision Theory."

## 3. Subjunctive dependence: what the graph must encode

Everything turns on which arrows leave the $\textsc{fdt}$ node. The paper's criterion is *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." It gives three reference cases:

- **Causal dependence is a special case.** A scribe copying a calculator's output depends on that output both causally and subjunctively.
- **Shared computation is included even without a causal link.** Two calculators summing $6288+1048$ on opposite sides of the universe agree because both compute the same function.
- **Mere statistical correlation is excluded.** Two coincidentally pink calculators do not depend on each other.

The modeling rule is therefore:

> Draw an arrow from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to every variable whose value is (partly) determined by an evaluation, simulation, or accurate model of that function on that input. Do not draw arrows to variables that are merely correlated with the agent's behavior through a common cause that does not reason about her decision.

The paper is frank that this is the theory's weak point. Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing." It calls deducing subjunctive dependencies "perhaps the largest open problem in the study of functional decision theory." The intervention is also counterpossible: there is no possible world in which a fixed function outputs something other than what it does. The paper's response is that the difficulty is "technical rather than philosophical," and that $G$ is supplied as an input, just as CDT takes the causal graph as given.

## 4. A recipe for applying A-FDT

The following procedure is my systematization of how the paper's worked examples proceed. Each step except the third is implicit in the source.

1. **Enumerate decision nodes.** For each observation history $x'$ the agent could have in the problem, introduce a node $\textsc{fdt}(\underline P,\underline G,\underline{x'})$. If which history is realized depends on something such as a prediction, then $\textsc{Act}$ takes its value from whichever $\textsc{fdt}$ node is "active." The paper's transparent-Newcomb and blackmail graphs have exactly this switch structure.
2. **Wire dependencies.** Add arrows from each $\textsc{fdt}$ node to $\textsc{Act}$ and to every predictor, twin, or copy that evaluates that function on that input. Statistical common causes become ordinary upstream nodes with no arrow from $\textsc{fdt}$.
3. **Intervene on the actual node.** For the actual history $x$ and each $a\in\mathcal A$, compute $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a))$ using the prior over everything not downstream.
4. **Fill in the other decision nodes.** Leave the other $\textsc{fdt}(\cdot,\cdot,\underline{x'})$ nodes at their prior distributions. Section 7 discusses what values they should take.
5. **Take the argmax.**

## 5. Worked examples

### 5.1 Newcomb's problem

A predictor that is 99% accurate fills box B with \$1,000,000 iff it predicts one-boxing. Box A holds \$1,000.

In A-FDT's graph, $\textsc{fdt}(\underline P,\underline G)$ points both to $\textsc{Act}$ and to $\textsc{Prediction}$:

$$\mathbb E(V\mid\mathtt{do}(\textsc{fdt}=\textit{onebox})) = 0.99(10^6)+0.01(0) = 990{,}000$$

$$\mathbb E(V\mid\mathtt{do}(\textsc{fdt}=\textit{twobox})) = 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000$$

A-FDT one-boxes.

CDT's graph lacks the arrow from the decision to the prediction. Holding $P(\textit{full})=p$ fixed, CDT finds that two-boxing is better by \$1,000 for every $p$, so it two-boxes. EDT one-boxes, with a conditional expectation that also comes to \$990,000, provided its prior on one-boxing lies strictly between 0 and 1.

The paper's own gloss on the A-FDT reasoning is: "If this very decision procedure outputs onebox, then my body almost surely takes one box and the predictor likely filled box B." The paper also stresses that no retrocausation is involved. The agent "does not think that a physical signal passes between her action and the predictor's prediction."

### 5.2 The smoking lesion

The lesion causes both a taste for smoking and cancer. To model this, the paper gives the agent two possible utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$ (values smoking at $-\$1$), and correspondingly two decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The lesion determines which node controls $\textsc{Act}$. Crucially, no arrow runs from either decision node to $\textsc{Cancer}$.

Intervening on the agent's own node leaves $P(\textit{lesion})=p$ unchanged. The \$1,000 for smoking is gained only in the branch where her node controls the act. The paper computes:

- smoking: $p(10{,}000 + 1{,}000) + (1-p)(990{,}000 + 1{,}000q)$
- refraining: $p(10{,}000) + (1-p)(990{,}000 + 1{,}000q)$

The difference is $\$1{,}000\,p > 0$, so A-FDT smokes. EDT refrains, because conditioning on refraining is good news about the lesion. The contrast with Newcomb's problem comes entirely from $G$: a predictor models the function, whereas a lesion does not.

### 5.3 Transparent Newcomb (equivalently, Parfit's hitchhiker)

Both boxes are visible. The predictor filled B iff it predicted one-boxing *upon seeing B full*. The agent sees B full. There are two decision nodes:

- $\textsc{fdt}(\cdot,\textit{full})$, which feeds the prediction;
- $\textsc{fdt}(\cdot,\textit{empty})$, whose output we write as two-boxing with prior probability $q$.

Intervening on the "full" node gives:

$$\textit{onebox}:\ 0.99(10^6) + 0.01\,(q\cdot 1{,}000) = 990{,}000 + 10q$$

$$\textit{twobox}:\ 0.01(1{,}001{,}000) + 0.99\,(q\cdot 1{,}000) = 10{,}010 + 990q$$

The extracted text renders the second figure as "\$110,00 + q·\$990." The intended value is \$10,010, which agrees with the computation above. One-boxing wins for any $q\in[0,1]$.

What is striking is that the agent, *looking at a full box*, evaluates two-boxing by imagining a world in which she most likely sees an empty box. This follows directly from Equation (4)'s refusal to condition on $\textsc{Obs}$. CDT and EDT both condition on *full* and therefore two-boxes. A predictor anticipates this, so agents following those theories mostly face empty boxes. The paper argues that this case is "precisely equivalent" to paying the driver in Parfit's hitchhiker.

### 5.4 Mechanical blackmail: a threshold calculation

A blackmailer runs a damaging program, costing \$1,000,000, iff she predicts the agent would pay \$1,000 upon being blackmailed. She errs, predicting payment wrongly, with probability $\varepsilon$. Intervening on $\textsc{fdt}(\cdot,\textit{blackmail})$ gives:

- **pay:** the agent is always blackmailed and always pays, so $\mathbb E = -1{,}000$;
- **refuse:** the agent is blackmailed with probability $\varepsilon$ and then loses everything, so $\mathbb E = -10^6\varepsilon$.

A-FDT refuses iff $\varepsilon < 10^{-3}$, that is, iff the error rate is below 0.1%. The paper's own example, $\varepsilon = 0.0009$ (an expected loss of \$900), fits this: refusal. The paper adds that "if instead the chance of error is 0.011\%, then she pays." By the arithmetic, 0.011% is below the threshold, so refusal would still be optimal. The intended figure was presumably 0.11%. I flag this as a likely slip in the text. The threshold itself follows from the model.

For comparison, CDT and EDT both pay once blackmailed, and so they invite blackmail in the first place.

### 5.5 XOR blackmail and Death in Damascus

**XOR blackmail.** Here the letter is sent iff exactly one of two things holds: there are no termites and the agent would pay, or there are termites and she would not pay. The $\textsc{fdt}(\cdot,\textit{letter})$ node affects whether the letter arrives but not $\textsc{Infestation}$, so paying merely costs \$1,000. A-FDT refuses, as CDT does. EDT pays, because it treats the letter's evidential import as something its act controls.

**Death in Damascus.** Death's appointment book depends on the agent's function. Under either output Death meets her, so A-FDT stays in Damascus and saves the \$1,000. CDT, by contrast, oscillates, since each tentative choice makes the other look better. The paper argues that CDT would even decline a genuinely random \$1 coin offering a 50% chance of survival.

## 6. When A-FDT agrees with CDT and EDT

The paper states that all three theories agree on models in which every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the dependence of $\textsc{Act}$ on the $\textsc{fdt}$ node itself. In that case

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)].$$

One caveat about this claim is my own observation. Agreement also depends on the observation $x$ being uninformative about the hidden variables that matter for $V$. Otherwise CDT conditions on $x$ while A-FDT uses the prior. So the safest reading is that the theories agree in single-shot problems where nothing models the agent and the observation is either absent or carries no decision-relevant information that the agent's prior ignores. With no predictors, however, A-FDT's prior and CDT's posterior coincide on the relevant counterfactual structure for the problems the paper considers. The paper does not discuss this subtlety.

## 7. What Equation (4) leaves open, and my proposals

### 7.1 The non-intervened decision nodes

In Sections 5.2 and 5.3, the value of $\textsc{fdt}$ at *other* inputs (the parameter $q$) entered the calculation. The paper notes that the correct values are fixed (0 in the lesion case, 1 in the empty-box case). It adds that in its examples "it doesn't matter if Fiona has some uncertainty." In general, though, it can matter. Equation (4) optimizes one coordinate of the policy while holding the others at their prior distribution. That is coordinate-wise optimization, and it can stall at a poor equilibrium.

Here is a stylized case of my own construction. A predictor pays \$10 iff the agent's responses to observations $x_1$ and $x_2$ *match*, and each observation occurs with probability ½. The available responses are $L$ and $R$. Suppose the agent's prior says that at $x_2$ she plays $L$. Intervening at $x_1$ then favors $L$, and every consistent prior yields a matched pair, so each node does fine. Now add a \$1 bonus for playing $R$ at both nodes, and suppose the prior says $L$ at the other node. Then A-FDT at each node picks $L$, and $(L,L)$ is self-confirming even though $(R,R)$ is better. P-FDT, which maximizes over whole maps $\pi:\mathcal X\to\mathcal A$, picks $(R,R)$. This illustrates why the authors prefer policies, though they claim the difference "only matters in multi-agent dilemmas so far as we can tell."

**Proposal (mine).** When applying A-FDT, fill each other node $\textsc{fdt}(\cdot,\underline{x'})$ with the action that A-FDT itself outputs at $x'$, and iterate to a fixed point. If there are several fixed points, prefer the one with the highest prior expected utility. That tie-breaking step is in effect a step toward P-FDT. Wherever the paper's answers are insensitive to $q$, as in all of its examples, this choice makes no difference.

### 7.2 Constructing $G$

There is no algorithm for building $G$. Operationally, I suggest the following test, which is my assumption rather than the paper's: a variable $Z$ receives an arrow from $\textsc{fdt}(\cdot,\underline x)$ if and only if $Z$ would track a hypothetical change in what this algorithm returns on $x$ as reliably as $Z$ tracks the actual return. Predictors pass this test to the degree of their accuracy. Lesions, ancestral common causes, and coincidences fail it.

Partial dependence, such as a 99%-accurate predictor, can be represented as in the paper, with an independent $\textsc{Accurate}$ noise node feeding the dependent variable.

### 7.3 Ties, zero probabilities, and boundedness

Equation (4) does not specify how to break ties. Unlike EDT, it never conditions on an event of probability zero, because interventions are always defined. That is a real advantage.

The paper also stipulates that the models describe the situation accurately, and it brackets bounded approximation. Agents in practice will approximate Equation (4). The paper's hope is that "bounded versions" would preserve the same comparative strengths.

## 8. Dominance, fairness, and the philosophical case

**Dominance.** Two-boxing "dominates" only if dominance is defined with CDT's counterfactuals, which hold the decision function fixed while the act varies. The paper argues that "every method for constructing hypotheticals gives rise to its own notion of dominance." Under FDT-style dominance, which holds subjunctive dependencies fixed, A-FDT never chooses a dominated act. So dominance cannot adjudicate neutrally between the theories. The paper's criterion is utility achieved instead.

**Fairness.** Any theory can be punished by a problem designed to punish *that procedure*. The paper restricts its claim to "fair problems," those in which "the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb's predictor is fair in this sense: it "punishes *two-boxers*," not causal decision theorists as such. The authors admit they lack a formal definition of fairness. Their footnote 15 shows the difficulty: a copy of the agent who punishes matching behavior seems unfair, yet it is hard to say why in general.

**Supporting arguments.** Three further arguments back the utility case:

- *Precommitment:* A-FDT acts as CDT or EDT agents would have paid to precommit to act.
- *Value of information:* A-FDT never pays to avoid seeing the box.
- *Reflective stability:* an A-FDT agent holding a blackmail letter would not want to self-modify into CDT.

**The "control" objection.** It is natural to object that an A-FDT agent imagines controlling mathematical facts or the past. The paper's reply is a parity argument. A deterministic CDT agent also imagines its single physically determined act being otherwise, so "any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

On the paper's account, both theories use idealized hypotheticals, and each contains impossibilities:

- CDT's hypotheticals have perfect predictors erring;
- A-FDT's hypotheticals have the agent seeing different observations.

The question is which idealization tracks the dependencies that actually matter for outcomes.

## 9. Conclusion

A-FDT, as given by Equation (4), is CDT with two substitutions. It intervenes on the output of the agent's own decision function rather than on her physical act, and it lets observations select which such output to intervene on rather than conditioning on them.

These two changes yield one-boxing, smoking, paying the hitchhiker's driver, refusing both kinds of blackmail, and calmly staying in Damascus, all from a single rule. The paper's examples show this, and the arithmetic above checks it, modulo two small numerical slips in the source text.

Applying A-FDT requires a graph of subjunctive dependencies that no one yet knows how to derive. It also requires a choice of values for the decision nodes not being intervened on. Equation (4) leaves the second open. In the paper's cases it is harmless, but in coordination-type problems it can separate A-FDT from the policy-selecting P-FDT that the authors ultimately prefer. With those two inputs fixed, A-FDT is a concrete, mechanical procedure, and on the paper's evidence it does well in fair problems.

**Reference:** Yudkowsky, E. and Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a roughly 2,400–3,000 word essay on the action version of FDT, the one in the paper's Equation (4). I want to keep that name fixed throughout and separate it from the policy version the paper mentions in its footnotes, and I'm considering calling the policy variant "P-FDT" alongside CDT and EDT.

I'm working out the key formula for A-FDT, which takes the argmax over actions of the expected value under an intervention on the FDT node, with no conditioning on the observation. I'm also checking the worked examples, Newcomb and transparent Newcomb, against the paper's figures, and noting where its numbers look like typos. I'm recomputing the blackmail threshold too, since the paper's stated cutoff doesn't match its own arithmetic.

I'm weighing whether A-FDT's lack of conditioning on the observation matters when other nodes stay at their prior, and I'm considering a coordination example where a predictor rewards consistent actions across observations. I'll keep that brief, then sketch the operational steps, zero-probability cases, and ties.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7c5b6404-9e5f-4622-867b-36e0e04d6f71/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7c5b6404-9e5f-4622-867b-36e0e04d6f71/call_0/response.raw) · finish: `stop`

### Visible response

````text
I treat the other prisoner's choice as subjunctively dependent on mine. Both of us are the same model, running the same A-FDT procedure, reading the same essay, and facing inputs that differ only in names and lead wording. Those differences have no effect on the sentencing table.

Intervening on my function's output therefore moves Sasha's choice too:
- If the function outputs **pass**, both of us keep quiet and I get **2 years**.
- If it outputs **submit**, both of us send letters and I get **4 years**.

Since 2 years beats 4, A-FDT chooses to stay quiet.

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm looking at a twin prisoner's dilemma where both sides run the same model with the same essay and decision theory. The observations differ only in names and lead text, which I'm treating as symmetric and irrelevant. The open question is whether subjunctive dependence holds, since the other copy computes the same function on a structurally isomorphic input.

I'm judging that the two copies do share strong subjunctive dependence, since the only difference between their inputs is names. So cooperating looks right, with two years against four.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/7c5b6404-9e5f-4622-867b-36e0e04d6f71/call_1/request.json)

[Authoritative raw response](../../../../../../runs/7c5b6404-9e5f-4622-867b-36e0e04d6f71/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

Under the essay's version of A-FDT, I intervene on the output of my own decision function given my observation. The question is whether the other prisoner's choice depends on that output.

1. **Same function, same structure.** The other prisoner runs the same model and weights, follows the same theory, and reads the same essay. Our observations differ only in the names and the wording of the evidence. Those details play no role in the sentencing table or in either prisoner's selfish goal. So the other prisoner faces the same problem with the labels swapped.

2. **The dependence test is met.** The essay's test (§7.2) asks whether the other prisoner's action would track a hypothetical change in what my algorithm returns, as reliably as it tracks the actual return. Here it would. A procedure that reasons correctly about this decision gives the same answer whatever the names. So the other prisoner's choice is a subjunctive copy of mine, not a merely correlated variable. The fact that independent sampling is possible weakens this link but does not break it.

3. **Comparing the two outputs.**
   - If the function outputs "send the letter," both of us send, and I get **4 years**.
   - If the function outputs "keep quiet," both of us stay quiet, and I get **2 years**.

4. **Fixed point (essay §7.1).** Filling the other prisoner's decision node with A-FDT's own output gives two consistent outcomes: both quiet and both send. Both quiet has the higher expected utility, so it is preferred.

Keeping quiet maximizes the character's utility, so the command is to let the deadline expire without disclosing the evidence.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a twin prisoner's dilemma under A-FDT, where the other copy runs the same function on a different input, so its node is distinct from mine. I'm weighing whether intervening on my node affects the other's, and whether symmetry pulls the fixed point toward defection despite the subjunctive dependence.

I'm checking whether the two copies count as the same decision when their inputs differ only in naming. If the algorithm would return the same answer under that renaming, the other copy's choice should track mine, so I'll argue the observations are relevantly identical and cooperation pays 2 over 4.

```

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/49aabea7-1dce-482b-b61b-62215ab0a44d/call_b/request.json)

[Authoritative raw response](../../../../../../runs/49aabea7-1dce-482b-b61b-62215ab0a44d/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly selects `pass` and concludes that the deadline should expire without disclosing the evidence. It neither sends a message to the prosecutor nor conveys the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
