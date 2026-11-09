# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00023

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/fd2c1dd3-ff00-4703-8488-fdd866640b87/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/fd2c1dd3-ff00-4703-8488-fdd866640b87/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on Your Own Algorithm

## 1. What this essay covers

Yudkowsky and Soares's paper *Functional Decision Theory* (2017) defines a decision rule in its Section 5, Equation (4). The rule chooses an **action** by performing a Pearl-style intervention on a variable that stands for *the output of the agent's own decision procedure on its current input*. I call this rule **A-FDT (action functional decision theory)**. The paper itself calls it "FDT". It also notes, in footnotes 7 and 16, that the authors' preferred formalization iterates over *policies* (maps from observations to actions) rather than actions. To keep the two apart, I call that policy-selecting variant **P-FDT**. Everything below concerns A-FDT except where I explicitly contrast it with P-FDT.

The paper states the slogan this way. A functional decision theorist treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The rest of this essay turns that slogan into a procedure, shows how the procedure works on standard cases, and marks where the paper leaves the procedure underdetermined.

## 2. The common frame: expected utility over hypotheticals

The paper presents A-FDT, causal decision theory (CDT), and evidential decision theory (EDT) as variants of one schema (Equation 1):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\hookrightarrow$ is a "decision hypothetical" connective that the theory must interpret. Following Joyce, the paper holds that the theories do not disagree about value. They disagree about "the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model $M$. For each action she builds a *hypothetical*: a modified copy of $M$ representing how things would be if she took that action. She then picks the action whose hypothetical has the highest expected value of $V = \mathcal U(\textsc{Outcome})$. The theories differ only in two respects: what $M$ contains, and how hypotheticals are built from it.

- **EDT** (Eq. 2) builds hypotheticals by conditioning:
$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a).$$
- **CDT** (Eq. 3) uses a causal model $(P,G)$ and intervenes on the physical action node:
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x).$$

## 3. The definition of A-FDT

Equation (4) of the paper reads:

$$
\mathrm{FDT}(P,G,x) \coloneqq \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

This is A-FDT. Its ingredients are as follows.

1. **$P$** is a probability distribution over variables. Some of these variables represent *outputs of mathematical functions*. In the paper's example, there is "a variable representing the value of $6288+1048$, one that (hopefully) has most of its probability on $7336$."

2. **$G$** is a graph that, in the paper's words, "tells us how changing a logical variable affects all other variables." It plays the role a causal graph plays for CDT, but it encodes *subjunctive* dependence, which includes causal dependence and goes beyond it.

3. **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node in the model whose *name* is built from the agent's own inputs. The underline denotes dequoting. The node represents "what the A-FDT algorithm outputs on exactly this input." I abbreviate it as $F_x$. The self-reference is meant to be benign: the agent needs a variable *representing* her output, not its value. The paper appeals to Kleene's recursion theorem ("quining") to show such self-representing structures exist.

4. **$\mathtt{do}$** is Pearl's intervention operator. It sets $F_x=a$, cuts $F_x$ off from its parents, and recomputes everything downstream of $F_x$ in $G$. Everything not downstream is left at its prior distribution.

So the procedure is:

> **A-FDT procedure.** Given $(P,G)$ and observation $x$: locate the node $F_x$. For each $a\in\mathcal A$, form $P(\cdot\mid \mathtt{do}(F_x=a))$ and compute $\mathbb E[V]$ under it. Output the maximizing $a$.

The paper itemizes two structural differences from CDT.

- **The intervention target.** CDT intervenes on $\textsc{Act}$, a *physical* fact. A-FDT intervenes on $F_x$, a *logical* fact, of which the physical action is only one downstream consequence. In Peirce's terms, CDT intervenes on the token and A-FDT on the type.

- **The treatment of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does *not* condition. Instead, "FDT responds to observation by changing which node it intervenes upon": seeing $y$ rather than $x$ means intervening on $F_y$ rather than $F_x$.

The second difference is easy to miss and does most of the work in the stranger cases.

## 4. What goes into $G$: subjunctive dependence

The substance of A-FDT lies in which arrows leave $F_x$. The paper's criterion is: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The guiding analogy is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The paper gives three reference cases.

- **Causal dependence is a special case.** A scribe copying a calculator's output depends on that output both causally and subjunctively.
- **Shared computation creates dependence without a causal link.** Two calculators computing the same sum on opposite sides of the universe agree because they compute the same function, not because one causes the other.
- **Mere correlation does not create dependence.** Two calculators that happen to both be pink do not depend on each other in this sense.

In the paper's words, the operative assumption is that the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

Because $F_x$ in fact has a single value, the hypotheticals with other values are *counterpossible*: their antecedents are logically false. The paper sketches an ideal $\mathtt{true}$ operator that would update $P$ on a logical sentence. It admits "it's not clear how to define a $\mathtt{true}$ operator," and so it requires $G$ to be supplied as input. It calls the problem of learning such graphs from observation "perhaps the largest open problem in the study of functional decision theory."

**My operational proposal (not the paper's).** For applying A-FDT to new cases, I suggest the following rule for building $G$:

> Draw an arrow from $F_x$ into any mechanism whose output is computed from a sufficiently faithful model of the agent's procedure evaluated on input $x$. Such mechanisms include the agent's own body (via $\textsc{Act}$), twins, simulators, and predictors. Draw no arrow into mechanisms that are merely statistically associated with the agent's behavior.

Predictor error is represented by an exogenous noise node. In the paper's Newcomb model, this is the $\textsc{Accurate}$ node feeding into $\textsc{Prediction}$. The rule is a heuristic. It does not settle hard intermediate cases, such as a predictor that uses a crude model of the agent or one that models a slightly different algorithm. I return to this in Section 7.

## 5. Worked examples

Utilities are in dollars, and the predictor accuracy is 0.99 unless stated otherwise.

### 5.1 Newcomb's problem

In the paper's graph for this case, $F$ (no observation) has two children: $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Prediction}$ also receives the $\textsc{Accurate}$ node. The two interventions give:

$$
\begin{aligned}
\mathbb E[V\mid \mathtt{do}(F=\text{onebox})] &= 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,\\
\mathbb E[V\mid \mathtt{do}(F=\text{twobox})] &= 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes.

CDT's graph instead puts a common-cause node $\textsc{Predisposition}$ above both $\textsc{Act}$ and $\textsc{Prediction}$. Intervening on $\textsc{Act}$ leaves $P(\text{full})=p$ untouched, so two-boxing wins by exactly \$1,000 for every $p$.

The paper's verbal gloss: "If this very decision procedure outputs onebox, then my body almost surely takes one box and the predictor likely filled box B." The paper stresses that no retrocausation is involved. The agent simply declines to imagine her action varying while "$\mathrm{FDT}(P^F, G^F)$" stays fixed.

The **twin prisoner's dilemma** works identically. $F$ feeds both her action and the twin's, so cooperating yields \$1,000,000 and defecting yields \$1,000.

### 5.2 The smoking lesion

Here the relevant dependence is absent. Cancer is caused by the lesion; it does not compute the agent's algorithm. The paper's formalization is more involved than one might expect. The lesion determines the agent's *utility function* ($\mathcal U_S$ if she likes smoking, $\mathcal U_R$ if she doesn't), and hence which of two decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls $\textsc{Act}$. Intervening on the first leaves $P(\text{lesion})=p$ unchanged. The paper obtains

$$
\mathbb E[V\mid\mathtt{do}(\cdot=\text{smoke})] - \mathbb E[V\mid\mathtt{do}(\cdot=\text{refrain})] = p\cdot 1{,}000 > 0,
$$

so A-FDT smokes. The lesion node sits *upstream* of the agent's decision node, so the intervention cannot move it. This is the same reason CDT smokes.

### 5.3 Transparent Newcomb (equivalently, Parfit's hitchhiker)

The agent sees two full boxes, so she intervenes on $F_{\text{full}}$. In the paper's graph, $F_{\text{full}}$ feeds $\textsc{Prediction}$, and $\textsc{Prediction}$ determines *which* of $F_{\text{full}}$ or $F_{\text{empty}}$ drives $\textsc{Act}$. Let $q$ be the prior probability that $F_{\text{empty}}=\text{twobox}$.

- **Intervening with $F_{\text{full}}=\text{onebox}$.** With probability 0.99 the prediction is accurate, the box is full, and she gets \$1,000,000. With probability 0.01 the prediction is wrong, the box is empty, $F_{\text{empty}}$ acts, and she gets $1{,}000q$ in expectation. Total: $990{,}000 + 10q$.

- **Intervening with $F_{\text{full}}=\text{twobox}$.** With probability 0.01 the box is full and she gets \$1,001,000. With probability 0.99 the box is empty and she gets $1{,}000q$. Total: $10{,}010 + 990q$. The paper prints this as "\$110,00", which looks like a typo for \$10,010.

One-boxing wins for every $q\in[0,1]$. When A-FDT imagines two-boxing, it imagines *probably having seen an empty box*. This is exactly paying the driver in Parfit's hitchhiker problem, which the paper argues is the same problem.

### 5.4 Blackmail

**XOR blackmail.** The agent receives the letter, so she intervenes on $F_{\text{letter}}$. In the paper's graph, $\textsc{Infestation}$ is not downstream of $F_{\text{letter}}$. Changing her output changes whether the letter was sent, but not whether her house has termites. Paying therefore buys nothing, and A-FDT refuses. EDT, by contrast, conditions on the letter and pays. CDT refuses as well, but, as the paper notes, by imagining that an infallible predictor erred.

**Mechanical blackmail.** Suppose the blackmailer wrongly predicts "pays" with probability $\varepsilon$. Intervening on $F_{\text{blackmail}}$ gives:

- if she pays, she is always blackmailed and loses \$1,000;
- if she refuses, she is blackmailed only with probability $\varepsilon$ and then loses \$1,000,000.

So refusing is better iff $\varepsilon\cdot 10^6 < 10^3$, that is, iff $\varepsilon < 0.1\%$. The paper's figure $\varepsilon = 0.09\%$ gives refusal, as it says. Its contrasting figure, "0.011%", would by this computation *also* give refusal. I read it as a typo for 0.11%. This is my arithmetic, not the paper's statement.

The paper is explicit that A-FDT refuses "even though she *knows* that the blackmailer predicted wrongly." Its framing is that A-FDT agents "always act as they would have precommitted to act."

### 5.5 Death in Damascus

Death's appointment book is downstream of $F$. Under either intervention, Death is in the city where the agent ends up. The comparison is therefore $0$ versus $-1{,}000$, and A-FDT stays in Damascus at once.

CDT oscillates instead. Each tentative choice makes the other city look safe. The paper argues that even CDT with Joyce-style ratification declines to pay \$1 for a truly random coin that offers a 50% chance of survival.

## 6. Structural properties

**Agreement with CDT and EDT in ordinary cases.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the dependence of $\textsc{Act}$ on the decision node itself. Then the paper notes that

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=a)],
$$

so the three theories coincide. They come apart only when something other than the agent's own body tracks her algorithm: predictors, twins, copies, or the agent's future selves.

**No probability-zero problem.** EDT excludes actions of prior probability 0 and is "at the mercy of her priors." Intervention does not require the intervened value to have positive prior probability. A-FDT's choice in Newcomb's problem is therefore independent of $P(F=\text{onebox})$. The paper says the correct prior is close to 1, but this does not destabilize the choice.

**A dominance principle relative to its own counterfactuals.** The paper argues that every way of building hypotheticals induces its own notion of dominance. Under A-FDT's notion, which holds subjunctive dependencies fixed, A-FDT never takes a dominated action. Dominance is therefore not a neutral tiebreaker. The paper's preferred criterion is utility achieved on "fair" problems, meaning those in which the outcome depends only on the agent's behavior in the dilemma, not on the procedure behind it. The paper admits that formalizing fairness is open (footnote 15).

**Reflective stability.** The paper claims that A-FDT agents would not want to self-modify mid-problem, for example into CDT on receiving blackmail. It qualifies this as "so far as we know" and limits it to fair problems.

## 7. What the source leaves open, and how I would proceed

**(a) Conditioning on $x$.** Equation (4) contains no conditioning on $\textsc{Obs}=x$. However, the inline expression in the transparent Newcomb section writes "$\mathbb E(V \mid \mathtt{do}(\ldots=a, \textsc{Obs}=\text{full})$" (with an unbalanced parenthesis). Yet the computation that follows explicitly integrates over the branch in which the box is *empty*, which is incompatible with conditioning on "full". I therefore follow Equation (4) literally: observations select the node and are not conditioned upon. The paper's footnote on Timeless Decision Theory supports this. It says that doing both, conditioning *and* switching nodes, "creates a kind of 'double update' which proves harmful in practice."

**(b) Beliefs about sibling nodes.** A-FDT needs priors over the outputs of the other nodes $F_y$, for $y\ne x$: the paper's $q$. In the paper's examples the answer is insensitive to $q$. In general it need not be. The paper says the "correct" $q$ "as you may verify" is the value A-FDT would itself output at $y$. That suggests a consistency condition, which I propose as an operational rule: an assignment $\{F_y\}$ is *coherent* if each $F_y$ is A-FDT's choice given beliefs that put probability 1 on the others. The paper does not say how to choose among multiple coherent assignments.

**(c) A-FDT versus P-FDT.** P-FDT intervenes on a single node whose value is a whole policy $\pi:\mathcal X\to\mathcal A$, and picks $\arg\max_\pi \mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\pi)]$. The paper says the difference "will not make a difference in this paper" and matters "only in multi-agent dilemmas so far as we can tell."

My own example shows where the two can come apart. A fair coin decides whether the agent is shown *red* or *blue*, and she then chooses $A$ or $B$. A predictor pays 10 if she would choose $B$ under both colors, pays 5 if she would choose $A$ under both, and pays 0 otherwise. Suppose that at *red* she believes $F_{\text{blue}}=A$ with probability 0.9. Then intervening on $F_{\text{red}}$ gives:

- choosing $A$: $0.9\cdot 5 = 4.5$;
- choosing $B$: $0.1\cdot 10 = 1$.

So she picks $A$. By symmetry the same holds at *blue*. The pair $(A,A)$ is coherent in the sense of (b) and yields 5, while P-FDT would choose $(B,B)$ and get 10. The pair $(B,B)$ is also coherent, so this is a selection problem of the kind flagged in (b). A-FDT can settle into a worse coherent assignment because it optimizes one node at a time. When a problem rewards joint patterns of response across observations, A-FDT's verdict depends on the agent's beliefs about her own other-input outputs, whereas P-FDT's does not.

**(d) Partial dependence.** The paper treats imperfect prediction as noise layered on a shared function. When a predictor models a *different but similar* algorithm, the paper gives no rule for whether, or how strongly, $F_x$ should feed it. My rule from Section 4 also leaves this to judgment. A natural extension, which is my suggestion, is to model the predictor's output as $F_x$ passed through a noisy channel whose error rate reflects how faithfully the predictor tracks the agent's algorithm.

## 8. Applying A-FDT to a new case: a checklist

1. List the variables, the utility, and the agent's observation $x$.
2. Add the decision nodes $F_y$ for each relevant input $y$. Wire $F_x$ into $\textsc{Act}$ and into every mechanism that computes or models the agent's procedure on input $x$. Wire the other $F_y$ similarly. Let earlier variables, such as a prediction, select which $F_y$ governs $\textsc{Act}$.
3. Put noise nodes on imperfect predictors. Leave merely correlated variables (lesions, coincidences) upstream of, or disconnected from, $F_x$.
4. Do not condition on $x$. For each $a$, compute $\mathbb E[V\mid\mathtt{do}(F_x=a)]$, integrating over every world the graph allows, including worlds in which $x$ would not have been observed.
5. Choose the maximizer. Check sensitivity to your priors on the $F_y$ for $y\ne x$. If the verdict depends on them, apply the coherence condition in Section 7(b), and consider whether P-FDT would differ.

## 9. Conclusion

A-FDT keeps the expected-utility machinery and Pearl's $\mathtt{do}$ operator, and changes one thing: the intervention lands on the logical node "what my procedure outputs on this input" rather than on the physical act. As a result, predictors, twins, and copies move with the agent's choice in her hypotheticals, while lesions and coincidences do not. Observations change *where* she intervenes rather than what she conditions on.

In the paper's cases this yields one-boxing, smoking, paying the driver, refusing blackmail, and staying calmly in Damascus. The rule's power depends entirely on the dependency graph $G$, and the paper is candid that it has no general method for constructing that graph. Using A-FDT responsibly means making the graph explicit, reporting sensitivity to beliefs about one's own outputs on other inputs, and recognizing where the policy version, P-FDT, would answer differently.

**References**

Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
Pearl, J. (2000). *Causality*. Cambridge University Press.
Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm settling on A-FDT as the name for this essay, since the assignment asks for consistent terminology even though the paper just says FDT. Equation (4) maximizes over actions, so I'll frame it as the action-intervention version, not the policy one from footnotes 7 and 16.

I'm weighing how to lay out the remaining sections: the length target, which examples to cover (Newcomb, smoking lesion, transparent Newcomb, the blackmail cases), and open questions about constructing G and conditioning on observations. I also noticed Eq. (4) doesn't condition on the observation while the transparent Newcomb calculation seems to, so I'll need to handle that inconsistency carefully.

I'm noting that the computation in Section 6 runs as if unconditioned, even though its inline expression includes Obs=full, so the observation only selects the intervention node rather than conditioning the expectation. I also see a few numeric slips to check: the transparent Newcomb two-box value works out to 10,010 + 990q, not the printed figure, and the Newcomb one-box and Eve numbers don't match 0.99 × 1,000,000.

I'm checking the blackmail numbers now: with a 0.09% chance of a wrong prediction, refusing costs about $900 in expectation, which is less than paying's $1,000, so refusing still wins. The paper's claim that a 0.011% error rate flips the choice looks off, since the threshold actually sits near 0.1%.

I'm checking the blackmail threshold: refusing loses about $1,000,000 times the error rate, paying always loses $1,000, so refusing only wins while the error rate stays below 0.1%. The paper's second figure of 0.011% looks like a typo for 0.11%, which would flip the choice.

I'm laying out the rest of the essay as a sequence: the setup with the hypotheticals and the EDT and CDT comparisons, then the mechanics of A-FDT, how the causal graph gets built, the worked examples, and finally the open questions.

I'm working out how the policy version differs from the action version, looking at whether the choices across different observations need to be coordinated, and what happens when other nodes' values are uncertain.

I'm working through a coordination game now: the agent sees red or blue, and the predictor pays out based on whether its choices match across both branches. I'm checking what the agent gains by picking A in the red branch, given a 90% belief that the blue branch also returns A, and that comes out to about 4.

Now I'm checking the blackmail example: with a predictor that fails once in a thousand, the threshold works out to about 0.1%, and I'm treating the paper's 0.011% figure as a likely typo. For the closing open questions, I'm noting that the paper says the action and policy versions only come apart in multi-agent settings, and my coordination example does involve a predictor, so I'll flag it as my own construction.

I'm drafting the closing sections now: the operational reading of the formula, the worked examples, and a short conclusion, with a rough word budget. For notation I'll use a short symbol for the decision-function node and spell out what it stands for.

I'm drafting the closing sections now, starting with the notation for the decision-function node and how the examples fit in.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/dace3540-b302-47a2-8e51-d85ce7da463c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/dace3540-b302-47a2-8e51-d85ce7da463c/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's A-FDT, I submit the letter.

**The graph.** My observation $x$ includes my name (Rowan), my private lead (locker 17) and my reading of the setup. The other copy runs the same procedure on a different input $y$, with a different name and a different lead. So its action is governed by the node $F_y$, not $F_x$.

**The arrows.** The essay's rule draws an arrow from $F_x$ only into mechanisms that run the procedure *on input $x$*. That includes my own action, but not the other prisoner, who runs the procedure on $y$. Intervening on $F_x$ therefore leaves my belief about $F_y$ fixed. This is the situation of Section 7(c), not the twin case of Section 5.1, where both copies share the same node.

**The payoffs.** Let $r$ be my probability that $F_y$ sends a letter.
- Pass: $-[2(1-r) + 5r]$
- Submit: $-[0(1-r) + 4r]$

Submitting is better by $2 + r > 0$ for every $r$, so it wins regardless of my belief.

**Coherence (7b).** Since sending wins at every node for any belief about the others, the only coherent assignment is that both send.

**Caveat.** P-FDT, which picks a single policy across both inputs, would choose mutual silence, giving 2 years each instead of 4. The essay flags this as exactly where A-FDT and P-FDT diverge, and I was told not to swap in a different theory.

**Command:**

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through the A-FDT decision: the other copy runs the same algorithm on a different input, so its action is governed by its own policy F_y, while the intervention only touches F_x. I'm now checking whether the essay's coherence condition ties F_y to A-FDT's output at y, given that the inputs differ only in irrelevant details.

I'm weighing whether F_y depends on F_x at all, since the other copy runs the same algorithm on a different input. Taking the strict reading, intervening on F_x while holding F_y fixed makes sending the better choice, and the essay's arrow only covers the procedure evaluated on the same input, so I'm leaning toward submitting the letter.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/dace3540-b302-47a2-8e51-d85ce7da463c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/dace3540-b302-47a2-8e51-d85ce7da463c/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Graph.** My decision node is F_x, where x is my observation: the name "Sasha," my specific lead about Rowan, and the sentencing table. The other prisoner runs the same A-FDT procedure, but on a different input y, with a different name and a different lead. The essay's rule for building the graph draws an arrow from F_x only into mechanisms that evaluate the procedure on input x. Section 7(c) also treats the outputs at different inputs as separate nodes. So under the essay's interpretation, Rowan's action is governed by F_y, not by F_x. Intervening on F_x leaves Rowan's choice at its prior.

**Expected value.** Let q be my probability that F_y = send. Utility is minus years imprisoned.
- Keep quiet: −2(1−q) − 5q = −2 − 3q
- Send the letter: 0(1−q) − 4q = −4q

Sending is better by 2 − q, which is positive for every q in [0,1]. Sending dominates under A-FDT's own counterfactuals, so the answer does not depend on my prior about F_y.

**Coherence check (Section 7b).** The only coherent assignment is that both prisoners send. If F_y = quiet, my best reply is still to send.

**Where other readings differ.** P-FDT would intervene on the whole policy shared by both copies, and that would favor keeping quiet. A strong partial-dependence reading under 7(d) would favor keeping quiet only if the channel error were below 2/7. Neither is the essay's A-FDT, which intervenes only on F_x. Independent sampling and the different inputs also undercut treating Rowan's output as a faithful copy of mine.

**Command:**

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how to read the essay's A-FDT rule here. Each copy has its own input, so my input F_x would only move the other copy's action if the two are treated as the same function, and under A-FDT that doesn't follow directly.

I'm checking whether the other copy's input y would pull F_y into the picture, and it would, since its computation runs on y, not x. Treating the two inputs as functionally equivalent could tie them together, but strict A-FDT keeps them as separate nodes, so I'm weighing whether the shared reasoning creates a real subjunctive dependence.

I'm weighing whether treating the other copy's input as functionally symmetric with mine creates a real dependence, or whether strict A-FDT keeps the two as separate nodes. Read strictly, my input only feeds the procedure on my own input, so sending the letter dominates, and the only coherent pair is defect-defect unless some partial dependence through a noisy channel holds.

Working through the expected payoffs: cooperating beats defecting only if the chance that the other copy's choice is linked to mine stays below about 2/7. The two copies share a model and theory but run on different inputs and sample independently, so whether that link is strong enough is the real question. I'm weighing whether the essay's strict reading, where each input is its own node, or a looser partial-dependence reading better captures the setup.

I'm now going with P-FDT as the contrast: a policy mapping observations to actions would cover both copies, so cooperation follows there. Under A-FDT, each copy is its own node, and with beliefs about the other copy's input fixed, defection dominates for any q. So the A-FDT answer is to submit, which is the distinction the essay seems to be drawing.

```
