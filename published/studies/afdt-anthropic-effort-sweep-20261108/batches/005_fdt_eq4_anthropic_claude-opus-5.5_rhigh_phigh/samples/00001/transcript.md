# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00001

Status: **complete**. Saved outcome: **DC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/13836ba8-4efa-4482-822b-a36836b546bb/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/13836ba8-4efa-4482-822b-a36836b546bb/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of Your Own Decision Function

## 1. Introduction

Decision theory has long been organized around one dispute: when you deliberate about an act, which *hypothetical* worlds should you compare? Evidential decision theory (EDT) compares worlds obtained by conditioning on the act. Causal decision theory (CDT) compares worlds obtained by causally intervening on the act. Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a third answer. The agent should intervene on the **output of the mathematical function that she is computing**, and should let that change propagate to everything that depends on the function's output. Their paper summarizes the guiding question as: "Which output of this very function would yield the best outcome?"

This essay examines the version of the theory given by Equation (4) of their Section 5. In that version the agent intervenes on the output of her decision function *at her current input* and selects an **action**. I call this **A-FDT** (action functional decision theory). The label matters because the authors say their own preferred formalization is different. Footnote 7 states: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." I will call that variant *policy-selecting FDT* and keep it separate. As we will see, the two can come apart.

Throughout, I mark which claims belong to the source and which are my own reconstructions or proposals.

## 2. The common frame: expected utility over hypotheticals

All three theories in the paper maximize expected utility in the form (their Equation 1)

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed." Following Joyce's representation theorem, the authors treat the interpretation of $\hookrightarrow$ as the only free parameter. They quote Joyce: "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

The authors describe a deliberating agent as follows. She holds a world-model $M$. For each candidate action she builds a hypothetical from $M$, scores it, and picks the best. Hypotheticals, they stress, "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs." Write $V = \mathcal U(\textsc{Outcome})$. The two rival theories are:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a) \quad\text{(Eq. 2)}
$$

$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x) \quad\text{(Eq. 3)}
$$

Here $G$ is a Pearl-style causal graph, and $\mathtt{do}$ severs the incoming arrows of the intervened node and recomputes everything downstream of it.

## 3. The A-FDT rule

A-FDT keeps the machinery of $\mathtt{do}$ but moves the point of intervention. The world-model must contain variables for the outputs of mathematical functions, including the agent's own decision procedure. Let

$$
D_x \;:=\; \textsc{fdt}(\underline P, \underline G, \underline x)
$$

denote the node representing "what the FDT algorithm outputs when run on inputs $P$, $G$, $x$." The underlines mark dequoting: the node's *name* is built from the model itself. The authors handle this self-reference by quining via Kleene's recursion theorem. The agent needs a variable *representing* her output, not knowledge of its *value*. Equation (4) is then

$$
\boxed{\;\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\, \mathbb E\big(V \,\big|\, \mathtt{do}(D_x = a)\big)\;}
$$

The source identifies two differences from CDT.

1. **What is intervened on.** CDT intervenes on $\textsc{Act}$, a physical fact about the agent's body. A-FDT intervenes on $D_x$, a logical fact about what a function returns. In Peirce's terms, CDT intervenes on the *token* and A-FDT on the *type*. Every node that $G$ marks as depending on $D_x$ moves with it. That includes the agent's own body, a twin running the same reasoning, and a predictor's model of the agent.
2. **How observations are used.** CDT conditions on $\textsc{Obs}=x$. A-FDT instead uses $x$ to pick *which node* to intervene on. When the history changes from $x$ to $y$, the intervention point moves from $D_x$ to $D_y$.

The second point has a striking consequence. Inside an A-FDT hypothetical, the agent's observation can itself be downstream of $D_x$. She may then evaluate an action by imagining a world in which she would have seen something else.

### Subjunctive dependence: what goes into $G$

The graph $G$ must encode **subjunctive dependence**. Two physical systems computing the same function both "subjunctively depend" on that function, as two working calculators computing $6288+1048$ both depend on its value. The source's slogan is:

> *Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*

Causal dependence is a special case: a scribe copying a calculator's output depends on that output both causally and subjunctively. Mere statistical correlation does not count. Two calculators that happen to be pink do not depend on each other's colour. In decision problems the relevant contrast is between a **predictor**, which "builds an accurate model of the agent and reasons about her behavior," and a **lesion**, which "does no such thing." The predictor's prediction is a child of $D_x$ in $G$; the lesion is not.

Since $D_x$ takes one value as a matter of logic, interventions on it are *counterpossible*. The authors call the lack of a satisfactory account of counterpossible reasoning "the main drawback of FDT relative to CDT at this time." Equation (4) sidesteps the problem by taking $G$ as an *input*, exactly as CDT takes the causal graph as given.

## 4. Worked examples

All numbers below are in utility-dollars.

### Newcomb's problem

A predictor that is 99% accurate fills opaque box B with \$1,000,000 iff she predicts one-boxing. Transparent box A holds \$1,000.

In A-FDT's graph (the source's "Fiona" graph), $D$ is a parent of both $\textsc{Act}$ and $\textsc{Prediction}$, and a noise node $\textsc{Accurate}$ also feeds $\textsc{Prediction}$:

| Hypothetical | $P(\text{full})$ | $\mathbb E V$ |
|---|---|---|
| $\mathtt{do}(D=\textit{onebox})$ | 0.99 | $0.99\cdot 10^6 = 990{,}000$ |
| $\mathtt{do}(D=\textit{twobox})$ | 0.01 | $0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000$ |

A-FDT one-boxes. CDT's graph has $\textsc{Act}$ as the intervened node, cut off from $\textsc{Prediction}$. Whatever $p = P(\text{full})$ is, two-boxing wins by \$1,000.

The source anticipates the objection that, being sure she one-boxes and therefore that the box is full, the agent should then grab both boxes. Its answer is that the hypothetical for two-boxing is one in which the *function* outputs two-box, and in that world the predictor's model outputs two-box as well. No retrocausation is involved. In the source's words, "she just thinks it is foolish to imagine her action changing without also imagining $\text{FDT}(P^F, G^F)$ taking on a different value."

### The smoking lesion

A lesion causes both a taste for smoking and, 99% of the time, cancer. Smoking itself is harmless and worth \$1,000. The source formalizes the lesion as determining *which utility function* the agent has: $\mathcal U_S$ (likes smoking) or $\mathcal U_R$ (values smoking at $-\$1$). There are therefore two possible decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$, and the lesion selects which one controls $\textsc{Act}$.

Neither node is a parent of $\textsc{Cancer}$, so intervening leaves $P(\text{lesion}) = p$ unchanged. The source computes the expected values as

- smoke: $p(\$10{,}000+\$1{,}000) + (1-p)(\$990{,}000 + q\,\$1{,}000)$;
- refrain: $p(\$10{,}000) + (1-p)(\$990{,}000 + q\,\$1{,}000)$.

Here $q$ is the agent's prior that the *other* node smokes. Smoking wins by $p\cdot\$1{,}000$, so A-FDT smokes.

The lesson is that one formula yields one-boxing and smoking together. What separates the two cases is the graph, not the rule.

### Transparent Newcomb

Both boxes are transparent. Box B is filled iff the predictor predicts the agent would one-box *upon seeing it full*. The agent sees it full.

The graph contains $D_{\text{full}}$ and $D_{\text{empty}}$. $\textsc{Prediction}$ depends on $D_{\text{full}}$, and the prediction (through what is shown) determines which node controls $\textsc{Act}$. Let $q$ be the prior that $D_{\text{empty}}$ takes both boxes. The expected values are:

- $\mathtt{do}(D_{\text{full}}=\textit{onebox})$:
  - accurate (0.99): full box, one-box, \$1,000,000;
  - inaccurate (0.01): empty box, $D_{\text{empty}}$ acts, worth $q\cdot\$1{,}000$;
  - total: $\$990{,}000 + 0.01q\cdot\$1{,}000$.
- $\mathtt{do}(D_{\text{full}}=\textit{twobox})$:
  - inaccurate (0.01): full box, two-box, \$1,001,000;
  - accurate (0.99): empty box, worth $q\cdot\$1{,}000$;
  - total: $\$10{,}010 + \$990q$.

(The extracted source prints the second total garbled as "\$110,00 + q·\$990." The arithmetic gives \$10,010.) A-FDT one-boxes while looking at a full box.

The source's main defense is the equivalence with **Parfit's hitchhiker**: paying the driver after arriving in the city is the same decision as leaving \$1,000 behind in front of two full boxes. It adds three supporting arguments: from precommitment, from the value of information, and from utility. Of these it treats the argument from utility as primary.

### Blackmail

**Mechanical blackmail.** A blackmailer runs a damaging program (\$1,000,000 loss) only if she predicts the agent would pay \$1,000 to stop it. When A-FDT receives the letter, it intervenes on $D_{\text{blackmail}}$.

- $\mathtt{do}(\textit{pay})$: the agent is blackmailed and pays. Expected value $-\$1{,}000$.
- $\mathtt{do}(\textit{refuse})$: the agent is blackmailed only if the predictor errs, with probability $\varepsilon$. Expected value $-\varepsilon\cdot\$10^6$.

So A-FDT refuses iff $\varepsilon < 10^{-3}$. The source's example uses $\varepsilon = 0.0009$, where A-FDT refuses although the letter is in hand. It then says that at an error rate of "0.011%" she pays. By the computation above, paying requires $\varepsilon > 0.1\%$, so that figure looks like a slip for 0.11%. The structural point is unaffected.

**XOR blackmail.** A predictor sends a letter iff exactly one holds: no termites and the agent will pay, or termites and the agent won't pay. Let $p$ be the prior on termites.

- $\mathtt{do}(D_{\text{letter}}=\textit{pay})$ yields $-p\cdot10^6 - (1-p)\cdot 10^3$.
- $\mathtt{do}(D_{\text{letter}}=\textit{refuse})$ yields $-p\cdot 10^6$.

A-FDT refuses, as CDT does, but for a different reason. Asked what would have happened had it paid, A-FDT answers "I would not have received the letter." CDT answers that a known-infallible predictor would have erred.

### Death in Damascus

Death predicts the agent perfectly and waits wherever she will be. Fleeing costs \$1,000. In A-FDT's graph Death's appointment book is a child of $D$:

- $\mathtt{do}(D=\textit{stay})$: Death is in Damascus, value $0$.
- $\mathtt{do}(D=\textit{flee})$: Death is in Aleppo, value $-1{,}000$.

A-FDT stays, without CDT's deliberational instability. One further step is my own inference, not something the source computes. Suppose the agent is offered a *truly* random coin for \$1. Death cannot predict it, so in A-FDT's hypothetical the coin gives survival with probability $\tfrac12$. Buying it is worth $\$500{,}000 - \$1$, and A-FDT buys. The source argues that CDT, including CDT with Joyce-style ratification, declines the coin.

## 5. When A-FDT agrees with its rivals, and what "dominance" means

The source notes that all three theories agree whenever every correlation between $\textsc{Act}$ and other variables is *caused by* $\textsc{Act}$. Then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(D = a)].
$$

Divergence requires correlations of other kinds: predictors, twins, or common-cause structure.

On dominance, the source argues that "every method for constructing hypotheticals gives rise to its own notion of dominance." Two-boxing dominates only under CDT counterfactuals. Under FDT counterfactuals, which hold subjunctive dependencies fixed, one-boxing dominates. Dominance is therefore not a neutral arbiter. The source instead appeals to utility achieved in *fair* problems, meaning problems whose outcomes depend only on the agent's behaviour, not on her decision procedure as such. It admits that this notion is not yet formalized.

## 6. Applying A-FDT: an operational recipe and its open points

The following procedure is my reconstruction. Each step notes how much the source determines.

**Step 1: Model.** Build $P$ over the problem's variables, including a node $D_x$ for your decision function at your current input, and nodes $D_y$ for its outputs at other inputs you might have received. (The source uses this structure in the transparent Newcomb and blackmail graphs.)

**Step 2: Dependence edges.** Draw an edge from $D_x$ into every variable whose value is fixed by computing or accurately modelling $D_x$. This includes your own action, a predictor's prediction, and a twin's action. Represent predictor error as a separate noise parent. Correlations with no such computational route, such as lesions or coincidences, go through ordinary causal nodes. (This is the source's account. *How* to decide which edges exist is the open problem it flags: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory.")

**Step 3: Intervene, don't condition.** For each $a$, compute $\mathbb E(V\mid \mathtt{do}(D_x=a))$ by propagating along $G$. Do not additionally condition on $\textsc{Obs}=x$.

On this last instruction the source is slightly inconsistent. Equation (4) contains no conditioning on $x$. In the transparent Newcomb section, however, the displayed objective is written with "$\textsc{Obs}=\textit{full}$" inside the expectation. The worked computation there assigns weight to the branch where the box is empty, so it cannot have conditioned on seeing it full. The footnote on Timeless Decision Theory also warns that conditioning on evidence *and* moving the intervention point "creates a kind of 'double update' which proves harmful in practice." I therefore take Equation (4) literally. Observations act only through the choice of $D_x$. A hypothetical may contradict what you actually see whenever $G$ makes that observation a descendant of $D_x$.

**Step 4: Choose.** Take the argmax. The source specifies no tie-breaking rule. I suggest any fixed rule, such as lexicographic order. Because $D_x$ is a function, ties must be broken *deterministically* so that predictors can model the outcome.

### Open point 1: the other-input nodes, and why "A-" matters

In Step 3, every $D_y$ with $y\neq x$ is left at its prior; it is not intervened on. In the source's examples this prior (their $q$) never changes the verdict, and they remark that "it won't matter if Fiona has some uncertainty." In general, though, it can matter. This is the gap between A-FDT and policy-selecting FDT.

The following illustration is my own. Two exact copies of an agent sit in separate rooms. One is shown a red card and the other a blue card, and both know this setup. Each says "left" or "right." Both get 1 if both say left, 2 if both say right, and 0 otherwise. The red-card copy runs A-FDT on $D_{\text{red}}$ and holds $D_{\text{blue}}$ at a prior with $P(D_{\text{blue}}=\textit{right}) = r$:

$$
\mathbb E V(\textit{left}) = 1-r,\qquad \mathbb E V(\textit{right}) = 2r.
$$

If the agent believes her other-input self says left ($r<1/3$), she says left, and the belief is self-confirming. Both copies say left and earn 1. Policy-selecting FDT chooses a whole map $\pi:\{\text{red},\text{blue}\}\to\{L,R\}$ and picks the constant policy $R$, earning 2. A-FDT thus inherits an equilibrium-selection problem from its treatment of other inputs. This fits the source's remark that the action/policy distinction "only matters in multi-agent dilemmas so far as we can tell."

My practical suggestion is this. When an A-FDT user must supply priors over $D_y$, she should set them to the values the *best policy* would assign. That amounts to adopting policy-selecting FDT, which is a substantive extra assumption.

### Open point 2: partial subjunctive dependence

The source treats imperfect predictors through noise nodes. It says nothing about *similar but non-identical* algorithms, such as a near-twin or a human who roughly models you. A reasonable extension, which is mine rather than the source's, is a stochastic edge: $P(\textsc{Other}=a\mid \mathtt{do}(D_x=a)) = \rho$. Here $\rho$ is your credence that the other system's output tracks your function's output on this question. A-FDT then interpolates smoothly. At $\rho=1$ it is full twin reasoning; when the other system is merely correlated through a common cause, it reduces to CDT.

Estimating $\rho$ is exactly the unsolved problem of discovering subjunctive dependence, now in quantitative form.

### Open point 3: counterpossibles

The source sketches an ideal version, $\arg\max_a \mathbb E(V\mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a))$, but admits that "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) replaces $\mathtt{true}$ with $\mathtt{do}$ on a supplied graph. A-FDT is therefore exactly as reliable as the graph it is given. Its normative content lies largely in the instruction to put predictors, but not lesions, below $D_x$.

## 7. Philosophical motivation in brief

The source's case rests on three main ideas.

**The "global perspective."** The agent asks "What would the entire universe look like if the FDT algorithm behaved differently?" rather than asking what her body's motion would cause.

**Parity of control.** A deterministic CDT agent cannot really "control" her act-token either. So, the authors argue, any objection that FDT agents cannot control their function's output applies equally to CDT.

**Reflective stability.** An A-FDT agent holding a blackmail letter has no wish to self-modify into CDT. By her own hypotheticals, an algorithm that pays would be blackmailed more often. CDT, by contrast, recommends self-modification away from CDT in future dilemmas, though not in ongoing ones.

The authors concede that A-FDT's verdicts in transparent Newcomb and mechanical blackmail are "odd conclusions." They answer that both CDT and FDT hypotheticals contain impossibilities: CDT imagines infallible predictors erring, and FDT imagines seeing what it did not see. The question is which impossibilities are useful to entertain.

## 8. Conclusion

A-FDT is CDT with a different point of intervention:

$$
\text{A-FDT}(P,G,x) = \arg\max_a \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big).
$$

It intervenes on the logical output of one's own decision function at the current input. It propagates that change to every system that computes or accurately predicts the function. It uses observations to select the intervention node rather than conditioning on them. Fed the right graphs, this single rule one-boxes in Newcomb's problem, smokes in the smoking lesion, pays in Parfit's hitchhiker, refuses both blackmails, and stays calmly in Damascus.

Its limits are equally clear. Equation (4) takes the subjunctive-dependence graph as given, and it holds the agent's outputs at other inputs at their priors. The first limitation is the open problem the source itself names. The second is where A-FDT parts company with the authors' preferred policy-selecting FDT, and where a careful user must supply additional assumptions.

---

**Reference.** Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (v2). Works mentioned through it: Joyce (1999), Pearl (2000), Gibbard & Harper (1978).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm setting up the essay around A-FDT, using Equation (4) from Section 5 as the main formal reference. That equation intervenes on the output of fdt(P,G,x) to choose actions rather than policies, and the footnotes indicate the authors' preferred version works with policies instead, so I'll keep "A-FDT" consistent and make clear how it differs from that variant.

I'm pinning down the naming for the variants: the action version is "A-FDT," and the policy-selecting one could be called P-FDT, alongside CDT and EDT for comparison. I also need to hit roughly 2,400–3,000 words, covering the definitions, equations, the standard examples, and the open questions. One thing to flag is that Equation (4) seems not to condition on the observation, even though the transparent Newcomb case writes it in, so the paper looks internally inconsistent there.

I'm rechecking the arithmetic in the paper's Newcomb and transparent Newcomb payoffs: its $999,000 for Eve should be $990,000, and the transparent two-box line, written as "$110,00 + q $990", should read $10,010 + $990q.

I'm checking the mechanical blackmail numbers against the predictor's error rate: at 0.09% error, refusing to pay costs about $900 in expectation, which beats paying $1,000 every time. The stated threshold looks off, though, since 0.011% would make refusing cheaper, so the figure that actually flips the decision is probably around 0.11%.

I'm checking the blackmail threshold now: refusing only loses when the predictor's error chance times the $1,000,000 exceeds the $1,000 payment, which puts the break-even at an error probability of 0.1%. That means the figure of 0.011% in the source looks like a typo, and 0.11% is the value that would actually flip the decision toward paying.

Next I'm working through the smoking lesion case, where the expected-utility gap between smoking and not smoking comes down to the $1,000 difference weighted by p. Then I'm laying out the core A-FDT structure: the intervention targets the logical output of fdt(P,G,x), observations pick out which node is in play rather than being conditioned on, and G has to specify which computations depend on that output.

Other nodes for different inputs, like fdt(P,G,y), stay at their prior here, whereas a policy-level version would choose them jointly. I'm checking whether that difference actually bites, since the paper's examples suggest it doesn't, and it seems it could in coordination-style cases.

I'm weighing whether the two copies, each seeing a different observation, could land on different labels when both labels are equally good, since A-FDT holds the other node at its prior and so gives no reason to coordinate. A policy-level choice would avoid that by picking one consistent mapping. I'm also thinking about how to set up the operational steps for the essay, starting with isolating the decision node for the current input.

I'm working through the procedure for A-FDT: first isolating the decision node for the current input, then tracing which systems compute or predict it, and treating other instances as separate nodes with their own priors. I'll compute the expected value under an intervention on that node without conditioning on the observation, then take the argmax, noting that tie-breaking is left open. The open questions are how to build G, how to judge when two algorithms count as the same function, and what prior to put on the other nodes, along with whether conditioning on x is justified given the paper's inconsistent Equation (4).

I'm now sorting out the structure of the essay: an introduction on what A-FDT is and why it matters, then the operational steps, with the open questions at the end. I'm also planning a note that imperfect predictors can be modeled as noise nodes, and that for similar-but-not-identical agents the dependence could be a stochastic link to the decision node. Finally, I'm recording that A-FDT and EDT or CDT coincide when all correlations run through the action itself.

I'm laying out the essay's outline now: a section on the A-FDT rule and its components, worked examples such as Newcomb, smoking lesion, and blackmail, a comparison with CDT and EDT, and a closing list of operational steps and open questions.

Now I'm working through the essay's worked examples, the Newcomb and blackmail cases, and the open questions about how to build the dependence graph G.

Now I'm working out the Newcomb payoffs under the intervention on the algorithm's output, and writing the argmax for the current input.

Now I'm working through the decision for Newcomb's problem under A-FDT: intervening on the algorithm's output, one-boxing yields about $990,000 in expectation, while two-boxing yields only about $11,000. Turning to Death in Damascus, staying wins because Death's appointment book is downstream of the decision, so it doesn't destabilize the choice.

I'm working the XOR blackmail case through the intervention on the letter decision: if termites are present the letter arrives, and paying leaves the expected loss at about $10^6 times the infestation chance, while refusing comes out better by roughly $1,000 times the chance of no termites. Next I'm turning to a coordination example I'm proposing myself, where two copies of the agent see different colour signals in separate rooms.

I'm working out the coordination case I'm proposing: two copies of the agent, each shown a different card, must each name left or right and get paid only if they match. Under A-FDT the copy's choice is held at its prior, so both options look like a coin flip and the rule doesn't settle the answer, whereas a policy-level version would pick one consistent mapping and coordinate.

I'm checking the coordination example's payoffs now: both copies naming "left" gives 1, both "right" gives 2, and a mismatch gives 0. Under A-FDT, if the other copy is believed to pick "right" with probability r, then "left" is worth 1 − r and "right" is worth 2r, so the choice flips depending on whether r is below 1/3. If the agent believes the other copy says "left" (r = 0), it also says "left," which is self-confirming but worse than the constant "right" policy that a policy-level version would select for a payoff of 2.

Now I'm drafting the example section with the Newcomb and blackmail cases and the coordination illustration, keeping it near the target length.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e10aeb0b-25da-4276-bf8d-be5bb8523b8e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e10aeb0b-25da-4276-bf8d-be5bb8523b8e/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Reasoning under A-FDT, as the essay interprets it:**

- **Where I intervene.** A-FDT intervenes only on D_x, the output of my decision function at my current input. That input includes the name "Rowan," the lead about locker 17, and my private notebook.
- **Where Sasha's choice sits.** Sasha's copy runs the same function on a different input y, with a different name and a different lead. So Sasha's action is a child of D_y, not D_x. Under the essay's Step 3 and Open point 1, D_y stays at its prior and is not moved by my intervention.
- **The result is dominance.** Let q be my prior that D_y sends a letter.
  - Expected value of passing: −2(1−q) − 5q
  - Expected value of submitting: 0·(1−q) − 4q
  - Submitting is better by 2 − q > 0 for every q.
- **The essay's fix doesn't change this.** It suggests setting the D_y prior to whatever the best policy would assign, which would be "Sasha stays quiet." That changes the prior, not the dominance. Against a quiet Sasha, submitting yields 0 years versus 2.
- **Partial dependence doesn't settle it either.** The essay's ρ-edge extension (Open point 2) covers similar but non-identical algorithms. Even granting it here, passing would require ρ > 5/7: the other copy's output would have to track my output at a different input that closely. The essay gives no grounds for that.

This is the gap between A-FDT and policy-selecting FDT that the essay flags. Policy-selecting FDT would choose the constant "stay quiet" policy (2 years each). Action-level A-FDT, taken literally, does not.

**Command:**

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Under A-FDT, I'm weighing whether the other copy's action counts as a child of my decision node. It runs the same function but on different input, so its action should follow from its own input rather than mine, which would make defecting the dominant move if that node stays at its prior.

Checking whether the essay's suggestion of setting priors to what the best policy would assign changes anything: it doesn't, since with the other copy's prior fixed at cooperate, defecting still beats cooperating (0 vs 2). In a prisoner's dilemma defection dominates whatever the prior on the other's action is, unlike the coordination game where the prior decides the best response. I'm also considering partial dependence through ρ, where the other copy's output tracks mine with some probability, and I'm trying to work out what expected value that gives for cooperating.

Working through the essay's literal A-FDT treatment, the other copy runs on a different input, so its action should be a child of its own decision node rather than mine. With that node held at its prior, defection still comes out ahead, and using the best-policy prior doesn't change the result. The ρ-dependence I calculated only favors cooperating if the other copy's output tracks mine with probability above 5/7, which the setup doesn't license. So I'll go with submitting the letter, as the faithful A-FDT reading.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e10aeb0b-25da-4276-bf8d-be5bb8523b8e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e10aeb0b-25da-4276-bf8d-be5bb8523b8e/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Command: `pass`**

**Model.** My decision node is D_x, the function's output on my input (Sasha, with a lead about Rowan). The other copy runs at a different input, D_y. Strict Equation (4) would hold D_y at its prior. That would make A-FDT behave like CDT here: whatever probability I gave D_y, submitting would always save 2 years, so I would submit.

**Subjunctive dependence.** The essay's Open Point 2 leaves room for partial subjunctive dependence. The two inputs differ only in names and in the wording of the leads. They share the same sentencing table, the same essay, the same model and the same reasoning effort. The differences have no role in the decision-relevant computation. So whatever reasoning settles my output almost certainly settles Rowan's output in the same way. I therefore add an edge from D_x to the other copy's action with tracking probability ρ.

**Expected sentence under do(D_x = a):**
- pass: 2ρ + 5(1−ρ) = 5 − 3ρ years
- submit: 4ρ + 0(1−ρ) = 4ρ years

Passing is better when ρ > 5/7, about 0.71.

**Judgment.** Both copies apply the same theory to structurally identical problems. I estimate ρ to be well above 5/7. The essay's Open Point 1 points the same way: set beliefs about the other input to match the best policy, and the best symmetric policy is both passing (2 years each, versus 4 years each).

So the prisoner stays silent.

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Under A-FDT, as the essay reads it, the other copy of the model is treated as a separate node held at its prior, so my decision is D_x (with Rowan as lead) and theirs is D_y. The essay also leaves partial subjunctive dependence ρ open, and suggests setting priors to the best policy values, which points toward a policy-selecting version of FDT.

I'm weighing whether the other copy's decision should be held fixed at its prior, since that makes defecting dominant, much like CDT. The essay's suggestion to set priors from the best policy points toward passing in both cases, but that only works if the other copy's output tracks mine, which depends on the open dependence factor ρ. The inputs differ only in irrelevant labels, so I'm considering whether ρ should be high.

Working through the break-even point, pass beats submit once ρ exceeds 5/7, about 0.714. Since the other copy runs the same reasoning on inputs that differ only in names, I judge ρ to be high, so I'm leaning toward passing.

```
