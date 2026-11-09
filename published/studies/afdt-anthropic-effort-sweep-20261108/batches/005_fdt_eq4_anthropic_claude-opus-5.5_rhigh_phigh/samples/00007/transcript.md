# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00007

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/dee87c66-a9f8-4503-b454-8836996e727c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/dee87c66-a9f8-4503-b454-8836996e727c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing as the Output of a Function

*An essay on the action form of functional decision theory, following Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality" (arXiv:1710.05060)*

## 1. Naming and scope

Yudkowsky and Soares define a family of decision rules they call *functional decision theory*. The rule they actually write down, Equation (4) in their Section 5, has the agent intervene on a variable whose value is an **action**. In two footnotes (7 and 16) they say that their *preferred* formalization instead selects a **policy**, meaning a map from observations to actions, and that "the difference only matters in multi-agent dilemmas so far as we can tell."

In this essay, **A-FDT** (action functional decision theory) means exactly the Equation (4) rule. I write **P-FDT** for the policy-selecting variant the authors mention but do not formalize. I use the following names for the theories A-FDT is compared with:

- **CDT**: causal decision theory, the paper's Equation (3).
- **EDT**: evidential decision theory, the paper's Equation (2).
- **TDT**: timeless decision theory, the earlier variant mentioned in a footnote.

When the source says "FDT" in a passage about Equation (4), I translate it to A-FDT. Direct quotations keep the source's wording. I flag places where I go beyond the paper.

The guiding question, in the paper's words, is to treat one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

## 2. The shared skeleton: expected utility over hypotheticals

All three theories in the paper are expected-utility rules of the form

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history and $\hookrightarrow$ is a connective for "decision hypotheticals." The authors follow Joyce in treating the interpretation of $\hookrightarrow$ as the free parameter that separates the theories.

Operationally, the agent holds a world-model $M$. For each candidate action $a$ she builds a *hypothetical* $M^{a\hookrightarrow}$: "a mental image in the agent's head of how the world might look if she chooses $a$." She then scores each hypothetical by expected utility. The three theories build hypotheticals differently. Let $V = \mathcal U(\textsc{Outcome})$.

- **EDT** conditions on the action:
$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a).$$
- **CDT** applies Pearl's surgery to the physical action node in a causal graph $G$, then conditions on what was observed:
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x).$$

The paper's diagnosis is that EDT's hypotheticals "respect too many correlations" and CDT's "respect too few." The two motivating cases show this:

- In the smoking lesion problem, EDT keeps a merely statistical correlation between smoking and cancer and so refuses a free benefit.
- In Newcomb's problem, CDT severs the correlation between its act and a reliable prediction of that act, so in its hypotheticals a known-reliable predictor "inexplicably falter[s]."

A-FDT aims to keep exactly the dependencies that the paper calls *subjunctive*.

## 3. Subjunctive dependence

The core notion is informal in the source. When two physical systems compute the same function, their behaviors "subjunctively depend" on that function. Two calculators computing $6288+1048$ give matching answers because each computes the same sum, not because one causes the other. The paper's slogan:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The paper gives three reference points:

1. **Causal dependence is a special case.** A scribe copying a calculator's output depends on it both causally and subjunctively.
2. **Mere correlation is not dependence.** Two calculators that happen to share a color do not depend on each other.
3. **Prediction counts.** A predictor who models the agent's decision procedure contains, in effect, a "twin" of the agent's function. Its prediction therefore depends subjunctively on that function's output, even though the prediction happened earlier and no signal travels backward in time.

## 4. The definition of A-FDT

### 4.1 The equation

A-FDT's world-model is a pair $(P,G)$:

- $P$ is a probability distribution that includes variables for the outputs of mathematical functions, including the agent's own decision function.
- $G$ is a graph saying how changing such a variable propagates to other variables. The paper describes it as a graph "that tells us how changing a logical variable affects all other variables."

The rule is

$$
\boxed{\;\mathrm{A\text{-}FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;} \tag{4}
$$

The node $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable in the agent's own model. It stands for "what this very algorithm outputs on input $(P,G,x)$." The underlines mark dequoting: the variable's *name* is built from the agent's actual model and observation.

This self-reference is legitimate. Representing a value does not require knowing it, and Kleene's recursion theorem ("quining") lets a data structure contain a representation of itself.

Equation (4) is a tractable stand-in for an ideal rule the authors cannot define:

$$\arg\max_a \mathbb E\big(V \mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a)\big).$$

The $\mathtt{true}$ operator would update beliefs on a possibly false logical sentence, which is a counterpossible. Since nobody knows how to define it, Equation (4) moves the burden onto $G$. In the same way that CDT takes causal structure as input, A-FDT takes logical, computational and causal dependency structure as input.

### 4.2 Two differences from CDT

The source names exactly two differences between A-FDT and CDT:

1. **Point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the *type*, the function's output. In the graph, $\textsc{Act}$ is a child of the $\textsc{fdt}$ node, and so are the nodes for predictions, twins' acts, and simulations of the agent.
2. **Treatment of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT instead uses $x$ to choose *which* node it intervenes on. On observing $y$ rather than $x$, it intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$.

Note that Equation (4) contains no conditioning on $\textsc{Obs}=x$. This omission is deliberate, and it drives the theory's most distinctive verdicts (§6).

### 4.3 A recipe for applying A-FDT

The following steps are my own condensation of what Equation (4) asks you to do.

1. **Model the problem.** Write down a Bayesian network over the relevant variables and their prior probabilities.
2. **Add function nodes.** For each observation history $y$ the agent might face, add a node $F_y = \textsc{fdt}(\underline P,\underline G,\underline y)$.
3. **Route $\textsc{Act}$.** Make $\textsc{Act}$ a function of the $F_y$ nodes and of whatever determines which $y$ actually occurs.
4. **Draw subjunctive edges.** Draw an edge from $F_y$ to every variable that is computed from, or is a model of, the agent's behavior on input $y$. Predictions, simulations and twins all count. Variables that are only statistically correlated with the act get no such edge.
5. **Set beliefs about other inputs.** Give the nodes $F_{y'}$ for $y'\neq x$ prior distributions, the agent's beliefs about what she does in situations she is not in.
6. **Evaluate.** For each $a$, set $F_x := a$ by surgery, recompute descendants, and take the expectation of $V$ under the *unconditioned* prior over the remaining exogenous variables.
7. **Choose.** Output the maximizing $a$.

Steps 4 and 5 are where the source leaves the most to judgment; I return to them in §6.

## 5. Worked examples

### 5.1 Newcomb's problem

The predictor is accurate with probability $0.99$. In A-FDT's graph, the single node $F=\textsc{fdt}(\underline P,\underline G)$ has two children: $\textsc{Act}$, and $\textsc{Prediction}$ (which also depends on an independent $\textsc{Accurate}$ node).

| Intervention | Box B full with probability | Expected utility |
|---|---|---|
| $\mathtt{do}(F=\text{onebox})$ | 0.99 | $0.99\cdot 10^6 = \$990{,}000$ |
| $\mathtt{do}(F=\text{twobox})$ | 0.01 | $0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = \$11{,}000$ |

A-FDT one-boxes.

CDT differs only in where it intervenes. Under $\mathtt{do}(\textsc{Act}=a)$ the probability $p$ that Box B is full stays fixed, so two-boxing wins by \$1,000 for every $p$.

A-FDT's verdict does not depend on the prior probability of $F$. EDT's verdict does: Spohn's point is that extreme priors make EDT do anything.

### 5.2 The smoking lesion

The lesion causes both a love of smoking and cancer. The relevant question is whether cancer is computed from the agent's decision function. It is not.

The paper builds the case carefully. The lesion settles which utility function the agent has, and so which of two decision nodes controls $\textsc{Act}$:

- $\textsc{fdt}(\underline{P_S},\underline G)$ for an agent who likes smoking;
- $\textsc{fdt}(\underline{P_R},\underline G)$ for an agent who does not.

Neither node has an edge into $\textsc{Cancer}$. Intervening on the active node therefore leaves $P(\text{lesion}) = p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes.

Together with §5.1, this shows A-FDT doing what Gibbard and Harper argued no single rule could: one-boxing *and* smoking. The difference sits entirely in $G$. A predictor is a child of the agent's function, while a lesion is a common cause of the agent's preferences and her cancer.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

Box B is visible. The predictor fills it iff she predicts the agent would one-box *upon seeing it full*. Let $\alpha$ be the predictor's accuracy and $q$ the agent's prior that $F_{\text{empty}}$ outputs two-box. The agent sees "full" and intervenes on $F_{\text{full}}$.

**$\mathtt{do}(F_{\text{full}}=\text{onebox})$.**
- With probability $\alpha$ the prediction is accurate: the box is full and the agent one-boxes, receiving \$1,000,000.
- With probability $1-\alpha$ the prediction is wrong: the box is empty, $F_{\text{empty}}$ controls the act, and the agent receives $q\cdot\$1{,}000$ in expectation.

**$\mathtt{do}(F_{\text{full}}=\text{twobox})$.**
- With probability $1-\alpha$ the predictor errs, fills the box, and the agent receives \$1,001,000.
- With probability $\alpha$ the box is empty and the agent receives $q\cdot\$1{,}000$.

So

$$
\mathrm{EU}(\text{one}) = 10^6\alpha + 10^3 q(1-\alpha),\qquad \mathrm{EU}(\text{two}) = 1{,}001{,}000(1-\alpha) + 10^3 q\alpha.
$$

At $\alpha = 0.99$ these are $\$990{,}000 + 10q$ and $\$10{,}010 + 990q$. (The source prints the second as "\$110,00 + q·\$990", which looks like a typesetting slip for \$10,010.)

A-FDT therefore one-boxes *while looking at a full box*. Its hypothetical for two-boxing is a world where, with high probability, it would have seen an empty box.

Parfit's hitchhiker has the same structure. The node is $F_{\text{in city}}$, and paying is what makes "in city" likely in the first place. A-FDT pays.

### 5.4 Two blackmail problems

**XOR blackmail.** A-FDT refuses to pay. Intervening on $F_{\text{letter}}$ changes whether the letter is sent but has no edge into $\textsc{Infestation}$, so the termites are unaffected.

EDT pays, because conditioning on paying makes termites improbable. CDT refuses too, but its hypothetical says the infallible predictor would have erred. The two refusals rest on different hypotheticals.

**Mechanical blackmail.** The blackmailer runs the publishing program iff she predicts the agent would pay. Suppose she wrongly predicts payment with probability $\varepsilon$.

- $\mathtt{do}(F_{\text{blackmail}}=\text{pay})$: the agent is essentially always blackmailed and pays, so $\mathrm{EU} \approx -\$1{,}000$.
- $\mathtt{do}(F_{\text{blackmail}}=\text{refuse})$: the agent is blackmailed only with probability $\varepsilon$, so $\mathrm{EU} = -\varepsilon\cdot\$10^6$.

A-FDT refuses iff $\varepsilon < 10^{-3}$. The paper's worked case $\varepsilon = 0.0009$ gives refusal: −\$900 against −\$1,000.

The paper also says Fiona pays if the error rate is "0.011%". That figure lies *below* the threshold, so it is presumably a slip for 0.11%. The threshold calculation is what readers should rely on.

The general lesson: A-FDT refuses a threat when, and only when, its refusal disposition sufficiently suppresses the threat.

### 5.5 Death in Damascus

Death's appointment book is computed from a perfect prediction of the agent, so $\textsc{Book}$ is a child of $F$.

- $\mathtt{do}(F=\text{Damascus})$: the agent dies at home, utility 0.
- $\mathtt{do}(F=\text{Aleppo})$: the agent dies in Aleppo after paying for the trip, utility −\$1,000.

A-FDT stays in Damascus, and the deliberation is stable.

CDT's choice depends on its current credence about where it will go, and flips when that credence flips. Its ratified mixed strategies also lead it to decline a truly random coin worth a 50% survival chance at \$1. The point of contrast is structural: A-FDT's argmax in Equation (4) never consults the agent's prior about its own action at the intervened node.

## 6. What the source leaves open, and how one might close it

### 6.1 Where does $G$ come from?

The authors call this "perhaps the largest open problem in the study of functional decision theory." In their words:

> "Equation~(4) works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing."

**My proposal.** In practice, the problems in the paper are settled by one test.

> **Edge rule.** Draw $F_y \to Z$ iff $Z$ is (in the agent's model) computed by a process that evaluates, simulates, or reliably predicts the agent's decision function on input $y$, possibly with independent noise modeled as a separate exogenous parent.

Lesions, genes and coincidences that are correlated with the act get edges only into $\textsc{Act}$ (or into which decision node is active), never into consequences.

This rule reproduces every graph in the paper. It also says how to model an imperfect predictor: as "function output plus independent error," which is exactly the paper's $\textsc{Accurate}$ node.

The rule does not settle partial similarity, for example a predictor who models a *slightly different* algorithm. That remains a genuine gap. It mirrors the problem of reasoning under logical uncertainty, which the paper defers to the literature on counterpossibles.

### 6.2 Is A-FDT conditioning on its observation?

As printed, Equation (4) does not condition on $\textsc{Obs}=x$. In the transparent Newcomb discussion, however, the source writes the objective as $\mathbb E(V\mid \mathtt{do}(F_{\text{full}}=a, \textsc{Obs}=\text{full}))$, with an unbalanced parenthesis.

Read literally as conditioning on $\textsc{Obs}=\text{full}$, that objective would contradict the numbers the paper then computes. Those numbers average over the *prior* on $\textsc{Accurate}$, including the branch in which the box is empty.

**Operational reading, which I endorse.** Observations enter A-FDT only as an index selecting $F_x$. Expectations are taken under the prior. This is the only reading consistent with:

- Equation (4) itself;
- the worked numbers in §5.3–5.4;
- the paper's remark that the A-FDT agent "does not react to observations by conditioning her distribution";
- its warning in a footnote that TDT, which both conditions *and* switches the intervention node, suffers "a kind of 'double update' which proves harmful in practice."

### 6.3 Beliefs about the other function nodes

Equation (4) requires priors on $F_{y'}$ for $y'\ne x$: the parameter $q$ in transparent Newcomb, and the analogous $q$ in the smoking lesion problem. The paper notes that the correct values are what A-FDT would actually output (two-box on an empty box), and that its verdicts are robust to uncertainty about them.

In general they are *not* irrelevant. **My proposal** is to require *self-consistency*: the belief about $F_{y'}$ should equal $\mathrm{A\text{-}FDT}(P,G,y')$, computed by the same rule. That makes the set of off-node beliefs a fixed point.

This fixed-point requirement shows exactly where A-FDT and P-FDT can come apart. Here is an example of my own, not from the paper.

> **Split coordination.** Two exact copies of the agent are shown different colors. One sees red, the other blue. Each picks $A$ or $B$. Both receive 10 if both pick $A$, 1 if both pick $B$, and 0 otherwise.

The red copy intervenes on $F_{\text{red}}$ and holds $F_{\text{blue}}$ at its prior.

- If it believes $F_{\text{blue}}=B$, then $B$ is optimal for it.
- By symmetry, the blue copy then picks $B$.

So "both $B$" is a self-consistent A-FDT outcome, as is "both $A$." Each $F_y$ is optimized separately, so A-FDT has a coordination (equilibrium-selection) problem across its own observation-indexed nodes.

P-FDT optimizes the whole map $\pi:\{\text{red},\text{blue}\}\to\{A,B\}$ at once and picks $\pi\equiv A$. This fits the authors' remark that the action/policy difference shows up in multi-agent cases. It also suggests one reasonable extra rule if A-FDT is the target: among self-consistent fixed points, choose the one with the highest prior expected utility. That rule is in effect a step toward P-FDT.

### 6.4 Ties, zero probabilities, and stochastic agents

Because A-FDT uses $\mathtt{do}$ rather than conditioning, an action can be evaluated even when the agent is certain it will not take it. This avoids EDT's zero-probability failure. Ties are not addressed in the source; any fixed tie-breaking rule is compatible with Equation (4).

Agents with noisy execution fit naturally: add an exogenous noise parent to $\textsc{Act}$. Predictor noise is handled the same way through $\textsc{Accurate}$.

### 6.5 Fairness and dominance

The source makes two further claims:

1. **On dominance.** Every way of building hypotheticals induces its own dominance notion, so two-boxing's dominance argument just restates CDT's choice of hypothetical. Under "A-FDT dominance," which holds subjunctive dependencies fixed, A-FDT never picks a dominated act.
2. **On fairness.** A-FDT should be judged on "fair" problems, where outcomes depend only on the agent's behavior in the dilemma at hand. The authors say they know of no fair problem where it loses, but concede (footnote 15) that "fair" lacks a formal definition.

When applying A-FDT to a new case, check whether the payoff depends on *what you do* (fair) or on *which algorithm you run regardless of what it outputs* (unfair). An example of the second kind is a game that punishes anyone who matches Fiona's copy.

## 7. Applying A-FDT to an unfamiliar case: a checklist

1. **List the observation histories.** Ask which observations could occur and which node $F_x$ is active now.
2. **Find the models of you.** Identify which variables are computed from, or predict, your decision function on *which* inputs. Draw those edges, and only those.
3. **Leave correlations alone.** Variables merely correlated with your act, such as genes, lesions or coincidences, are left alone by the intervention.
4. **Do not condition on $x$.** Compute expectations under the prior. Your observation only picks the node.
5. **Fill in off-node beliefs consistently.** Set the $F_{y'}$ beliefs to your own self-consistent choices, and check whether the verdict is sensitive to them.
6. **Check for coordination problems.** If several of your own nodes must coordinate, note that A-FDT may have multiple fixed points. Consider whether the problem calls for P-FDT.

## 8. Conclusion

A-FDT keeps the expected-utility form of decision theory and changes only the epistemic perspective. Its hypotheticals are built by surgery on a variable representing *the output of the agent's own decision function on its current input*. All and only the variables that subjunctively depend on that output are allowed to vary.

That one change gives a unified set of verdicts: one-boxing, smoking, paying the hitchhiker's driver, refusing extortion, and staying calmly in Damascus. It achieves them without ratification or precommitment, because observations are used to select a node rather than to update the distribution.

The theory's precision is bounded by its inputs. Equation (4) is fully determinate only once the dependency graph $G$ and beliefs about one's behavior on other inputs are fixed. The source openly leaves the first unsolved. I have proposed an edge rule for $G$ and a self-consistency rule for the off-node beliefs, and the latter shows where A-FDT's action-by-action optimization can fall short of the policy-level view its authors prefer.

## References

- Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
- Gibbard, A., & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory.*
- Pearl, J. (2000). *Causality.*
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how to write up A-FDT, the action version from Equation (4), where the intervention sits on the action node rather than the policy. I need to keep the name "A-FDT" fixed throughout, headings included, and keep it clearly separate from CDT, EDT, and the policy version, which needs its own distinct label.

I'm now planning the essay's scope: a length of about 2400 to 3000 words, covering definitions, the Equation (4) formulation, a set of decision problems, the counterfactual treatment, and several open questions. I'm also noting a few things to check, including whether the equation omits observation conditioning and whether a numerical figure for the Newcomb case is consistent.

I'm checking the numbers in the transparent Newcomb case, where the paper's $110,00 figure looks like a typo for roughly $10,010 plus 990q. For the mechanical blackmail case, the refusal threshold works out to an error probability of 0.001, which doesn't match the paper's 0.011% figure, so I'll flag that as likely meaning 0.11%. I still need to look at the smoking lesion expected utilities as well.

I'm now turning to the operational side of A-FDT, starting with how to construct G: every node that is computed from the agent's decision function on the same input becomes a child of the fdt node, while mere statistical correlations through a common cause, like the lesion case, are left out. I'm also considering observations: Equation (4) doesn't condition on Obs=x, so the observation only feeds the intervention node, and the other fdt nodes for different inputs stay at the agent's prior estimate of its own behavior. I still need to check the transparent Newcomb case against this.

I'm now looking at the operational side of A-FDT: Equation (4) doesn't condition on the observation, so the observation only selects the node, and the other nodes for different inputs stay at the agent's prior estimate of its own behavior. For the off-path nodes, I'm thinking the q values matter in general, so self-consistency seems the right approach, though the policy version can diverge from this since it optimizes the whole map jointly.

I'm now working through a coordination example for A-FDT: two copies of the agent see different observations, say "red" and "blue", and get paid only if they choose matching actions. Intervening on one copy's node while holding the other at its prior could leave several self-consistent outcomes, and some of them are worse for both.

I'm now laying out the essay's structure: a title, then a section on what A-FDT is asking, a section on the shared EU and EDT/CDT framework, a section defining A-FDT through the components of Equation (4), and a section of worked examples starting with Newcomb.

I'm now sketching the remaining sections: the operational gaps in the source, the action-versus-policy contrast, and a general formula for the transparent Newcomb case with predictor accuracy and an off-path prior.

I'm now checking the Newcomb numbers for the transparent variant: if the agent's policy in the full-box case is two-boxing, an accurate prediction empties the box, so the agent takes the empty-box payoff, and an inaccurate one gives the full $1,001,000.

I'm checking the Death in Damascus case next: the Death node depends on the fdt node, so intervening on the decision to go to Damascus or Aleppo leaves the outcome unchanged in each branch, and the agent has no reason to shift away from its current choice.

I'm working through the blackmail case now: if I pay, I end up losing $1,000 for sure, while refusing risks $10^6 times the error probability, so refusing only wins when that error chance is under 0.001. I also want to keep the notation for the fdt node straight, and I'll mark which points come from the paper and which are my own proposals.

I'm now going back over the source text's quotes on subjunctive dependence, planning to quote the "largest open problem" line and the "Functional decision theory is to subjunctive dependence" comparison exactly as written.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/cd53342d-bfdc-45e3-83c9-a8f3f4c3639a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/cd53342d-bfdc-45e3-83c9-a8f3f4c3639a/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's reading of A-FDT, the choice is to send the letter. Here is the reasoning, applied inside the fiction.

**Which node is mine.** My observation history x includes being Rowan and holding the specific lead about Sasha. A-FDT intervenes only on F_x, the output of this decision function on this exact input.

**What depends on that node.** Sasha's copy receives a different observation y, with a different name and lead, so its act is the output of F_y, not F_x. By the essay's edge rule, F_x has edges only to variables that compute or predict the function on input x. Sasha's act gets no edge from F_x. This matches the essay's split-coordination example, where copies shown different colors occupy separate nodes and each holds the other's node at its prior.

**Evaluation.** I hold F_y fixed at any prior belief and compare my two options:

| Sasha's choice | Keep quiet | Send letter |
|---|---|---|
| Sasha keeps quiet | 2 years | 0 years |
| Sasha sends a letter | 5 years | 4 years |

Sending is strictly better in both cases, so it wins whatever I believe about F_y.

**Self-consistency check.** Applying the same rule to Sasha's node also gives "send." So the unique fixed point is mutual disclosure: both copies send, and each serves 4 years. P-FDT, which optimizes the whole policy at once, could pick mutual silence at 2 years each. The essay names that as the gap between the two theories, and the experiment assigns A-FDT.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a fictional prisoner's dilemma under the A-FDT framework. I'm treating the two copies as having different observations, and I'm asking whether the other copy's action depends on the policy I'm intervening on, given the rule for drawing the dependency edge.

I'm checking whether the other copy's action depends on my policy, and the edge rule says it doesn't, since that copy computes its own observation's function. So I'm holding its action fixed, and defecting dominates for me under that assumption, which makes both defecting the fixed point. I'll submit, since the essay's split-observation example treats different observations as separate nodes, even though a partial similarity might tempt me to call the functions essentially the same.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/cd53342d-bfdc-45e3-83c9-a8f3f4c3639a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/cd53342d-bfdc-45e3-83c9-a8f3f4c3639a/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay interprets it, sending the letter is the better choice.

1. **Which node I intervene on.** My observation (being Sasha, with the lead about Rowan) picks out my function node, F_Sasha. The other prisoner's act comes from the same function but on a different input: a different name and a different lead. That is a separate node, F_Rowan.

2. **Edges.** The essay's edge rule draws an edge from F_y only to variables that compute or predict the function on input y. Rowan's act is computed on input y′, not on my input. So intervening on F_Sasha does not change Rowan's act. Rowan's choice stays at my prior belief about it.

3. **Evaluation.** With the other prisoner's act held fixed, sending is better in both cases. If Rowan keeps quiet, sending gives 0 years versus 2. If Rowan sends, it gives 4 years versus 5. So sending is strictly better whatever my belief about F_Rowan.

4. **Self-consistency (§6.3).** The only fixed point is both prisoners sending. Mutual silence is not self-consistent, because each node's best response to a silent counterpart is to send. So the essay's tie-breaking rule for choosing among fixed points never comes into play. This is the gap the essay notes between action-level and policy-level reasoning. P-FDT, which picks the whole policy at once, might choose mutual silence, but A-FDT does not.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working under the A-FDT reading, with two copies that see different inputs. The other copy's function node takes a different input, so intervening on my copy's function shouldn't reach its act. Since that act is computed on a separate input, I don't see an edge between them, and I'm checking what follows from that.

I've settled on defection as the fixed point under A-FDT: with the other copy held fixed, defecting gives the better payoff in each case, and cooperation isn't self-consistent. That's the essay's split-coordination result. Since the instructions say to use A-FDT as interpreted, I'll submit the letter.

```
