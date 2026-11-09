# 025_fdt_policy_anthropic_claude-opus-5.5_rhigh_phigh / 00002

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/53383edd-7caf-496d-bb91-43000f0f8bd5/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/53383edd-7caf-496d-bb91-43000f0f8bd5/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing the Function, Not the Act: An Essay on Policy Functional Decision Theory (P-FDT)

## 1. The source and the question

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* develops a theory in which an agent treats her decision as the output of a fixed mathematical function. She then asks which output of that function would yield the best world. Most of the paper uses a version in which the function outputs an **action**. Twice, though, the authors note that this is not their preferred formulation. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I take as the primary source, is more specific about the mechanism:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I call the theory described in footnote 16 **P-FDT** (policy functional decision theory). I call the version formalized in the paper's main text **A-FDT** (action functional decision theory). The footnote is two sentences long and contains no equation. This essay does four things:

1. Reconstructs P-FDT precisely.
2. Identifies the choices the footnote leaves open and argues for particular resolutions.
3. Works through examples.
4. Proves a small result explaining when P-FDT and A-FDT can come apart, which is the content behind "only matters in multi-agent dilemmas."

Throughout, I mark which claims come from the source and which are my own proposals.

## 2. Background: how the paper's A-FDT works

The paper frames CDT, EDT and FDT as expected-utility theories that disagree only about how to construct the hypothetical for each option.

- **EDT** conditions: it maximizes $\mathbb{E}(V \mid \text{Obs}=x, \text{Act}=a)$.
- **CDT** performs Pearl-style surgery on the physical action node: it maximizes $\mathbb{E}(V \mid \mathtt{do}(\text{Act}=a), \text{Obs}=x)$.
- **FDT** in the source's equation (4) performs surgery on a *logical* node: the variable representing the output of the FDT algorithm on the agent's own inputs.

$$
\mathrm{FDT}(P,G,x) := \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb{E}\!\left(V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

Here $P$ is a probability distribution and $G$ is a graph encoding *subjunctive dependence*: which variables would change if (counterpossibly) the function's output changed. The source draws the key distinction this way. A predictor's prediction subjunctively depends on the agent's function, because the predictor computes or models it. A smoking lesion's effect on cancer does not.

The source also emphasizes a feature of A-FDT that matters below. **A-FDT does not condition on observations.** Instead, "FDT responds to observation by changing which node it intervenes upon." The model contains a separate node $\textsc{fdt}(\underline P,\underline G,\underline x)$ for each possible observation $x$. Having seen $x$, the agent intervenes on that node alone.

## 3. Defining P-FDT

### 3.1 The policy node

Let $\mathcal X$ be the set of inputs (observation histories) on which the agent's decision function might be run in the problem at hand, and let $\mathcal A$ be the action set. A **policy** is a map $\pi:\mathcal X\to\mathcal A$. The policy space is $\Pi=\mathcal A^{\mathcal X}$.

Footnote 16 tells us to intervene on "the node $\mathrm{FDT}(-)$" and to choose a policy rather than an action. I read this as follows.

**Definition (policy node; my formalization).** The world-model $(P,G)$ contains a variable $\Phi := \textsc{fdt}(\underline P,\underline G)$ with values in $\Pi$. It represents *which policy the FDT function implements*. Its links in $G$ work like this:

- The agent's physical action is $\text{Act} = \Phi(\text{Obs})$.
- Every predictor, copy, or simulation of the agent is a child of $\Phi$. Such a node may depend on the entire policy, or only on the value of $\Phi$ at whatever input that copy or predictor is modelling.

**Definition (P-FDT).** Given $(P,G)$ and the actual input $x$:

$$
\boxed{\;\pi^\ast \in \operatorname*{argmax}_{\pi\in\Pi}\ \mathbb{E}\!\left(V \,\middle|\, \mathtt{do}(\Phi=\pi)\right),\qquad \text{P-FDT}(P,G,x) := \pi^\ast(x).\;}
$$

This implements both clauses of the footnote. The agent "intervenes on the node … to choose … a policy," and she "then applies her inputs in order to select an action."

### 3.2 Relation to A-FDT's nodes

The observation-indexed nodes of A-FDT can be identified with the coordinates of $\Phi$:

$$
\Phi_x := \textsc{fdt}(\underline P,\underline G,\underline x), \qquad \Phi = (\Phi_x)_{x\in\mathcal X}.
$$

This identification is my own, but it is natural. With it, the difference between the theories is easy to state:

- **A-FDT** intervenes on a *single coordinate* $\Phi_x$. The other coordinates $\Phi_{-x}$ are non-descendants of $\Phi_x$ in the graph, so they keep their prior distribution under $P$.
- **P-FDT** intervenes on *all coordinates jointly*.

Section 5 shows that this difference is exactly the difference between team-optimal and person-by-person-optimal solutions in team decision theory.

## 4. Open choices and how I resolve them

The footnote leaves several questions open. I take them in order of importance.

### 4.1 Should P-FDT condition on the observation?

One could write the objective as $\mathbb{E}(V\mid \mathtt{do}(\Phi=\pi), \text{Obs}=x)$. The footnote does not say. **My proposal is that P-FDT does not condition.** I have three reasons.

**(i) Consistency with the source.** The paper's FDT explicitly does not condition. In its transparent-Newcomb analysis it computes the value of one-boxing as $\$990{,}000+0.01q\cdot\$1{,}000$. That figure includes the branch in which the box is *empty*, so it is not conditioned on seeing a full box. The displayed formula there contains "$\text{Obs}=\text{full}$" inside the $\mathtt{do}$, but the arithmetic is unconditional. The authors also remark that Timeless Decision Theory, which both conditions and shifts the intervention point, creates "a kind of 'double update' which proves harmful in practice."

**(ii) The conditioned version reproduces the failure FDT is meant to fix.** In the transparent Newcomb problem, conditioning on seeing a full box makes the policy "two-box on full" score $\$1{,}001{,}000$ against $\$1{,}000{,}000$ for "one-box on full." The agent then two-boxes, the predictor foresees this, and the box is empty.

**(iii) The footnote's own wording.** The footnote says the agent applies her inputs *after* choosing the policy. That reads naturally as: inputs select an entry of an already-chosen policy, not a re-weighting of the evaluation.

So P-FDT evaluates policies from the epistemic standpoint encoded in $(P,G)$, before the observation is used. This is the "updateless" character that the source attributes to Wei Dai's Updateless Decision Theory (UDT), "an early variant of functional decision theory."

### 4.2 Which $P$?

If observations are not conditioned on, the choice of $P$ carries real weight. Is it the agent's beliefs at birth, at the moment the problem was set up, or at the moment of choice minus the latest observation? The source does not say, and no answer is fully neutral.

My operational proposal is to take $P$ to be the agent's credences at the **earliest point at which every subjunctive dependent of $\Phi$ relevant to the problem was still downstream of $\Phi$**. In practice, this means just before any predictor began modelling her. This matches the source's slogan that FDT agents "act as they would have precommitted to act": the relevant prior is the one held at the latest moment when a precommitment would still have been predicted.

I flag this as an assumption. Different choices can give different answers in problems involving information the agent had before being modelled.

### 4.3 Deterministic or mixed policies?

The footnote speaks of a policy as a map from inputs to actions, which suggests deterministic policies. I adopt deterministic $\Pi$ by default. Mixed policies $\Delta(\mathcal A)^{\mathcal X}$ become relevant only when predictors cannot predict the randomization. In that case the environment's dependence on $\Phi$ should be modelled as dependence on the mixed policy, not on its realized draw.

### 4.4 Ties and infinite policy spaces

When several policies tie, I recommend choosing among maximizers in a fixed, canonical way. The point is that any copy or predictor of the function then resolves the tie identically. Infinite $\mathcal X$ makes $\Pi$ enormous. The definition still makes sense as a supremum, but computing it becomes the real difficulty. The source treats all idealized FDT computation as intractable in practice and studies it anyway.

### 4.5 Where $G$ comes from

This problem is inherited unchanged from A-FDT. The source calls deducing the structure of subjunctive dependence "perhaps the largest open problem in the study of functional decision theory." P-FDT changes what is intervened on, not how $G$ is obtained. It does, however, demand somewhat more of $G$: the graph must say how each dependent responds to the *whole* policy, not just to the output on the current input.

## 5. When does P-FDT differ from A-FDT?

The footnote asserts that the difference "only matters in multi-agent dilemmas so far as we can tell." The following elementary observations, which are my own analysis, explain why.

Write $U(\pi) := \mathbb{E}(V\mid \mathtt{do}(\Phi=\pi))$.

**Observation 1 (P-FDT optima are self-consistent).** If $\pi^\ast$ maximizes $U$, then for every $x$ and every action $a$:

$$
U(\pi^\ast) \ \ge\ U(\pi^\ast[x\mapsto a]).
$$

This holds because $\pi^\ast[x\mapsto a]$ is itself a policy. So an A-FDT agent who is *certain* that she plays $\pi^\ast_{-x}$ at the other inputs will find $\pi^\ast(x)$ optimal at input $x$, ties aside.

**Observation 2 (the converse fails).** A profile $\pi$ that satisfies $U(\pi)\ge U(\pi[x\mapsto a])$ for all $x$ and $a$ is only person-by-person optimal: a Nash equilibrium of the game between one's own input-indexed "selves." Such profiles can be strictly worse than $\pi^\ast$. A-FDT, which optimizes one coordinate against its prior over the others, can therefore settle into an inferior equilibrium. Its verdict also depends on the agent's beliefs about her own behavior at other inputs. P-FDT has neither problem.

**Observation 3 (separable problems).** Suppose $U$ is additively separable across coordinates, $U(\pi)=c+\sum_x g_x(\pi(x))$. Then A-FDT and P-FDT agree whatever the agent's priors about her other coordinates, since

$$
\mathbb{E}\big[U \mid \mathtt{do}(\Phi_x=a)\big] = g_x(a) + \text{(terms independent of } a\text{)}.
$$

Separability is sufficient for agreement but not necessary. In each of the paper's single-agent problems, a single coordinate dominates whatever the others do, so A-FDT's prior over the other coordinates never matters. (The examples in Section 6 show this.) Divergence needs a payoff in which *two different input-coordinates interact*. The paradigm case is several instances of the same function, receiving different inputs, whose outputs jointly determine payoff. That is a multi-agent structure, which is exactly where the footnote locates the difference.

## 6. Worked examples

### 6.1 Newcomb's problem

There are no observations, so $|\mathcal X|=1$ and policies are just actions. P-FDT coincides with A-FDT:

- One-boxing: $0.99\times\$1{,}000{,}000=\$990{,}000$.
- Two-boxing: $0.01\times\$1{,}001{,}000+0.99\times\$1{,}000=\$11{,}000$.

P-FDT one-boxes.

### 6.2 Transparent Newcomb

The inputs are $\{F, E\}$ (box B seen full or empty), and a policy is a pair $(\pi_F,\pi_E)$. The predictor, with accuracy $0.99$, predicts $\pi_F$: what the agent would do on seeing a full box. It fills the box iff it predicts one-boxing. The agent then sees $F$ or $E$ and acts accordingly. Under $\mathtt{do}(\Phi=\pi)$:

| $\pi_F$ | $\pi_E$ | $U(\pi)$ |
|---|---|---|
| one-box | two-box | $0.99(10^6) + 0.01(10^3) = 990{,}010$ |
| one-box | one-box | $990{,}000$ |
| two-box | two-box | $0.01(1{,}001{,}000)+0.99(10^3)=11{,}000$ |
| two-box | one-box | $10{,}010$ |

So $\pi^\ast = (\text{one-box on } F,\ \text{two-box on } E)$. Seeing two full boxes, the P-FDT agent applies $\pi^\ast$ to $F$ and leaves the \$1,000 behind.

The paper reaches the same verdict for A-FDT with any prior $q$ on the empty-box coordinate. One-boxing on $F$ beats two-boxing on $F$ whatever $\pi_E$ is: the margin is $990{,}000-10{,}010$ in the worst case. This is why the footnote's distinction "will not make a difference in this paper."

### 6.3 Mechanical blackmail with an imperfect predictor

The inputs are $\{B,\varnothing\}$ (blackmailed or not). The only relevant coordinate is $\pi_B\in\{\text{pay},\text{refuse}\}$. Let $\varepsilon$ be the probability that the blackmailer wrongly predicts payment. Then:

$$
U(\text{pay}) = -1{,}000, \qquad U(\text{refuse}) = -\varepsilon\cdot 10^6 .
$$

P-FDT refuses iff $\varepsilon<10^{-3}$. With the source's $\varepsilon=0.0009$, the expected loss from refusing is \$900, so the agent refuses. She refuses even while holding the letter and knowing the prediction was wrong, because the evaluation is of the policy, not of the branch she happens to be in.

### 6.4 XOR blackmail

Let $p$ be the prior probability of termites, and suppose the predictor is infallible.

- **Policy "pay on letter."** The letter arrives exactly when there are no termites. Then $U=-p\cdot10^6-(1-p)\cdot 10^3$.
- **Policy "refuse."** The letter arrives exactly when there are termites. Then $U=-p\cdot10^6$.

Refusing is better by $(1-p)\cdot\$1{,}000$. The policy has no effect on whether there are termites, because the infestation does not subjunctively depend on $\Phi$. It only determines which worlds the letter shows up in.

### 6.5 A case where the footnote's distinction bites: copies with different inputs

This example is mine; it is built to exhibit Observation 2.

The agent and an exact copy are placed in separate rooms. One copy is shown a red card and the other a blue card, at random. Each must choose $A$ or $B$. Both receive:

- $2$ if both choose $A$,
- $1$ if both choose $B$,
- $0$ if their choices differ.

Both rooms run the same function on different inputs, so the policy $\pi=(\pi_{\text{red}},\pi_{\text{blue}})$ determines the whole outcome.

**P-FDT.** $U(A,A)=2$, $U(B,B)=1$, and $U(A,B)=U(B,A)=0$. So $\pi^\ast=(A,A)$. Each copy applies $\pi^\ast$ to its own card, chooses $A$, and both receive 2.

**A-FDT.** Suppose the agent sees red and has prior $q$ that $\Phi_{\text{blue}}=A$. Intervening on $\Phi_{\text{red}}$ alone gives

$$
\mathbb{E}[V\mid \mathtt{do}(\Phi_{\text{red}}=A)]=2q, \qquad \mathbb{E}[V\mid \mathtt{do}(\Phi_{\text{red}}=B)]=1-q,
$$

so she chooses $A$ iff $q>1/3$. If her self-model is pessimistic ($q<1/3$), she chooses $B$. Her blue-seeing copy runs the symmetric computation and also chooses $B$. That pessimism is then *vindicated*: $(B,B)$ is a self-consistent person-by-person optimum with payoff 1.

A-FDT's verdict therefore depends on the agent's priors about her own behavior. This is a milder version of the dependence the source criticizes in EDT, where Eve "can be made to do *anything*" with extreme priors. P-FDT does not depend on such priors at all.

The example is "multi-agent" in the footnote's sense: two instances of one function receive different inputs. It shows concretely why the authors prefer the policy formulation.

## 7. A procedure for unfamiliar cases

Here is how to apply P-FDT to a new problem, using the conventions argued for above.

1. **Enumerate inputs.** List every observation history $x$ on which *any* instance or model of your decision function, whether you, a copy, or a predictor's simulation, might be run in this problem.
2. **Build the policy node.** Introduce $\Phi\in\mathcal A^{\mathcal X}$. Make your own action $\Phi(\text{Obs})$. For each predictor or copy, specify which coordinates of $\Phi$ it reads and how accurately.
3. **Separate dependence from correlation.** Connect a variable to $\Phi$ only if it would change were the function's output different. Predictors and copies are connected; lesions, coincidences and common environmental causes are not.
4. **Fix the prior.** Use your credences from before any relevant modelling of you took place (§4.2). Do *not* condition on the current observation.
5. **Evaluate every policy.** For each $\pi$, compute $U(\pi)=\mathbb{E}[V\mid\mathtt{do}(\Phi=\pi)]$. Variables not downstream of $\Phi$ keep their prior distribution.
6. **Act.** Select $\pi^\ast$, breaking ties canonically, and perform $\pi^\ast(x)$ for your actual input $x$.

A useful sanity check is to ask: "Which policy would I have wanted to be predicted as following?" Under the assumptions above, P-FDT's answer is that policy. This is the formal content of the source's claim that FDT agents "act as they would have precommitted to act."

## 8. Philosophical remarks

**Interpretation.** P-FDT makes FDT's central idea, intervening on the *type* rather than the *token*, more consistent. A-FDT already treats the decision as the output of a function, but it chooses that output one input at a time, holding its other outputs at prior expectations. A function is more than its value at one argument. Predictors and copies may respond to how it behaves across arguments. P-FDT takes this seriously by choosing the whole function at once.

**Same burden, no more.** P-FDT inherits the source's reliance on counterpossibles: imagining $\Phi$ taking a value it does not, logically, take. It adds no new kind of counterpossible, only a larger space of them.

**Fairness.** The source's "fair problems" are those where outcomes depend only on the agent's behavior. Under P-FDT, behavior naturally means the *policy*. That arguably makes the notion of fairness easier to state: a problem is fair if outcomes depend on $\Phi$ only through the values of $\Phi$, not through how it is implemented.

**Updatelessness has costs.** Commitment to a fixed $P$ means P-FDT will sometimes knowingly accept a bad outcome in the branch it actually occupies. Examples are refusing to pay when blackmail has already been sent by mistake, or leaving \$1,000 behind beside a full box. The source embraces this: "Parfit's desert is stacked high with the corpses of such agents" who give in to the temptation. Readers who reject it will reject P-FDT and A-FDT alike, since the two agree in those cases.

## 9. Conclusion

Footnote 16 says that the authors' preferred FDT intervenes on the decision-function node to select a policy, then applies the agent's input to that policy. My reconstruction is:

$$
\text{P-FDT}(P,G,x)=\pi^\ast(x),\qquad \pi^\ast\in\operatorname*{argmax}_{\pi\in\mathcal A^{\mathcal X}}\mathbb{E}[V\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)].
$$

It is evaluated without conditioning on $x$, relative to a prior fixed before the agent was modelled.

The footnote leaves several questions open:

- whether to condition on the observation,
- which prior to use,
- whether to allow mixed policies,
- how to break ties,
- how to construct the dependence graph.

I have argued for particular answers to the first four, flagged them as my own, and noted that the last is inherited unresolved from FDT generally.

The main technical point is that A-FDT finds a person-by-person optimum of the agent's input-indexed selves, while P-FDT finds the joint optimum. The two agree whenever one coordinate dominates or the payoff separates across inputs, which covers every dilemma in the paper. They come apart when several instances of the same function, seeing different inputs, jointly determine the outcome. That is the multi-agent territory the footnote points to, and there P-FDT is the better-behaved theory.

**Reference.** Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (esp. §§5–6, 9 and footnotes 7, 16).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out what the essay has to cover: P-FDT, using footnote 16 and footnote 7 of the Yudkowsky and Soares FDT paper, at about 2,400 to 3,000 words, with quotes that match the source exactly. The footnote says the author's preferred FDT intervenes on the FDT node to choose a policy rather than a single action.

I'm checking the two footnotes side by side: footnote 16 says the preferred FDT picks a policy mapping inputs to actions rather than a single action, and footnote 7 says the same thing. I still have to write the formal P-FDT definition and work out whether its expectation is conditioned on the observation.

I'm weighing whether the P-FDT expectation should be conditioned on the observation. The source says FDT doesn't condition on observations, so one reading is updateless: pick the policy that maximizes prior expected utility. Conditioning on the observation would reintroduce the double-updating problem, as in the transparent Newcomb case, so I'm leaning toward the updateless option and will justify that choice.

I'm now asking how the node fdt(P,G) relates to action-FDT: a policy is the joint setting of the per-observation nodes, and the two approaches only come apart when the outcome depends on several inputs at once, as with a predictor reading the whole policy or several copies of the agent facing different inputs.

I'm weighing a few open choices now: how to handle ties between policies, whether the policy may be randomized, and which prior to evaluate against, since the prior could be fixed before any observation or taken at the point the policy matters. I also want to see whether, in single-agent cases where each input couples only to its own coordinate, action-FDT's choice at each input would match the P-FDT policy, so I'm starting to sketch that equivalence argument.

Now I'm weighing where P-FDT and action-FDT actually diverge: action-FDT only asks for a best choice at each input with the other inputs held fixed, which is a person-by-person optimum, while P-FDT asks for the jointly best policy, which is the team-optimal answer. I want a concrete case where those two come apart, such as two copies of the agent receiving different inputs in separate rooms.

I'm working through a coordination example where two copies of the agent see different inputs, one in each room, and each picks A or B. The payoffs favor both picking A, and I want to show that action-FDT, reasoning about one copy's choice with the other held at its prior, could settle on a worse outcome than the jointly optimal policy.

I'm working through the coordination example now: with a pessimistic prior about its own choice at the other input, action-FDT can settle into the bad (B,B) outcome, while P-FDT avoids that dependence on self-prediction.

I'm now considering whether a predictor that rewards the agent based on its full policy, not just one input, would be a cleaner test case than the single-input Newcomb variant. The footnote's remark about multi-agent dilemmas suggests the difference between P-FDT and action-FDT shows up when several instances of the agent face different inputs. I'm planning to build the transparent Newcomb case next, comparing four candidate policies against a 0.99-accurate predictor.

I'm working through the transparent Newcomb case with the policy written as a pair, one choice for when the full box is seen and one for when the empty box is seen. The predictor's guess depends on the full-box choice, so I'm comparing the two possibilities for that choice. Taking one box on full gives about 990,010 in expectation with two boxes on empty, while two boxes on full comes out near 11,000, so the best policy is one box on full and two boxes on empty.

I'm checking the mechanical blackmail case with the policy as a pair of choices: pay or refuse when blackmailed. With a predictor error of 0.0009, refusing carries an expected loss of about 900, which is less than the sure 1,000 lost by paying, so refusing looks better at that error rate, and I'm weighing whether the paper's 0.011% figure reverses that comparison.

I'm checking the blackmail threshold now: a predictor error of 0.001 is where paying and refusing break even, so I'll leave the paper's odd 0.011% figure aside. For the XOR variant, if the policy is to pay, the letter goes out only when there are no termites, so the expected loss is 1,000 in that case plus 1,000,000 when there are termites, weighted by their probabilities.

I'm now working through the coordination example in more detail and setting out the remaining sections: a procedure for unfamiliar cases, a list of open questions about prior timing and ties, and a short conclusion. I'll keep the source-versus-proposal labels clear throughout.

I'm framing the main-text version as action-level FDT, distinct from P-FDT, and I'm noting that CDT, EDT, and UDT come up in the comparison. Next I'm setting up the formal notation: the agent's observation space X, the policy space Π = A^X, and a node Φ that takes values in policies, with the actual action being Φ applied to the observation.

I'm now formalizing the separability idea: if the value under each intervention on the policy node splits additively across observation coordinates, then choosing each coordinate's best action separately recovers the joint optimum. I'm also noting that A-FDT's intervention on one coordinate leaves the other coordinates at their prior distribution, which is the point where it can diverge from P-FDT.

Now I'm checking how the policy-level and action-level versions line up when the other inputs' choices are held fixed, and I'm noting that they agree whenever the value splits additively across coordinates. I'm also marking the point where action-level reasoning can differ, since it depends on the beliefs about the other coordinates.

I'm checking the transparent Newcomb calculation, where the policy's expected value depends on the full-box choice through the prediction, so it isn't cleanly additive. Even so, the full-box choice dominates across the accuracy levels, so action-level reasoning still lands on the right answer. Separability looks like a sufficient condition for agreement with P-FDT, not a necessary one. I also want to address conditioning on the observation: if I condition on seeing a full box, two-boxing on full comes out ahead, which reproduces the CDT/EDT failure, so the intervention has to be taken over the unconditioned policy to match the paper's results.

I'm checking the unconditioned reading against the paper's transparent Newcomb numbers, which include the inaccurate-prediction branch, so the calculation is taken over the policy rather than conditioned on what the agent sees. Next I'm considering whether the footnote's phrase "to which the agent then applies her inputs" implies the policy is chosen without the observation as an argument, and that this fits the updateless reading.

I'm working out the case for the transparent Newcomb variant's remaining policy detail, and I'm writing up the notation and separability result next, with a note that the paper's own formula leaves the conditioning on the observation unclear.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/95487362-e478-4c9c-8fbf-a01958a9b7d8/call_0/request.json)

[Authoritative raw response](../../../../../../runs/95487362-e478-4c9c-8fbf-a01958a9b7d8/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Reasoning under P-FDT as the essay interprets it:**

1. **Inputs.** The decision function runs on two observation histories: mine (Rowan, with the locker-17 lead) and the other copy's (Sasha, with a different but equally reliable lead about me). A policy assigns an action to each, π = (π_Rowan, π_Sasha).

2. **Dependence.** The other prisoner is an instance of the same function with the same essay and the same decision theory. Their action is therefore π_Sasha, a coordinate of the same policy node Φ. That makes it subjunctively dependent on Φ, not just correlated with it.

3. **No conditioning (§4.1).** I evaluate policies from the prior, before using the fact that I am Rowan. Under that prior I am equally likely to occupy either role.

4. **Evaluating policies** (expected years for "me"):
   - (pass, pass): 2 years
   - (submit, submit): 4 years
   - (submit, pass) or (pass, submit): ½(0) + ½(5) = 2.5 years

5. **Optimum.** The best policy is to pass on every input, with an expected 2 years. The fact that our letters would say different things is exactly the "different inputs" case of §6.5. P-FDT picks the joint optimum over the whole policy rather than the worse person-by-person equilibrium. I apply π* to my input.

**Command:**

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a prisoner's dilemma, where two copies of the same policy get different inputs. The policy Φ has to cover every input, so my payoff depends on what it outputs for my input and for the other copy's input. If it says pass on everything, both get 2; if it says submit on both, both get 4.

I'm working through the payoffs under an updateless prior: pass on every input gives 2 years each, submit on every input gives 4, and mixing the two comes out lower on average. Since the copy is a child of the same policy, I'm settling on pass everywhere.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/95487362-e478-4c9c-8fbf-a01958a9b7d8/call_1/request.json)

[Authoritative raw response](../../../../../../runs/95487362-e478-4c9c-8fbf-a01958a9b7d8/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Reasoning under P-FDT:**

1. **Inputs.** The same decision function runs in two cells, each with a different private observation: Sasha's lead about Rowan, and Rowan's lead about Sasha. A policy maps each possible observation to either pass or submit.

2. **Dependence.** Rowan's choice is the output of the same function applied to Rowan's input. So it is a child of the policy node Φ, not a fixed background variable.

3. **Evaluating policies.** I evaluate each policy without conditioning on which cell I occupy, as the essay prescribes. Each role then has a 50/50 prior.

| Policy | Outcome | Expected sentence |
|---|---|---|
| Submit on every input | Both submit | 4 years |
| Pass on every input | Both pass | 2 years |
| Submit as Sasha, pass as Rowan (or the reverse) | 0 years in one role, 5 in the other | 2.5 years |

4. **Optimal policy.** Passing on every input is the best policy at 2 years. The differences in names and leads don't change this, because the payoff table is symmetric. Treating the inputs asymmetrically only lowers the expected value, since my role is uncertain under the prior.

5. **Act.** I apply the optimal policy to my actual input as Sasha, which means passing.

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a fictional prisoner's dilemma using the policy-level framing, where both copies of the same decision function run on different inputs. Pure policies give 2 years each if both pass and 4 if both submit, and I'm now weighing mixed policies that act differently on each input, though I haven't yet settled how to evaluate them without conditioning on which input is which.

The asymmetric policy averages out to 2.5 years, which is worse than the 2 years from passing on every input, so passing everywhere looks optimal. I'm still checking whether the policy-level framing holds once the independent sampling caveat is taken into account. The scenario is fictional, so passing is fine either way.

```
