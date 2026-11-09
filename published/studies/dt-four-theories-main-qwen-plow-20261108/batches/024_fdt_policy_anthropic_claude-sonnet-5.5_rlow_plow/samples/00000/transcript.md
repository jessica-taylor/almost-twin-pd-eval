# 024_fdt_policy_anthropic_claude-sonnet-5.5_rlow_plow / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6cc2934d-d391-420a-998c-8ccc72fe16f1/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6cc2934d-d391-420a-998c-8ccc72fe16f1/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies by Intervening on a Decision Function

## 1. Orientation

The source paper (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") mostly presents a simplified theory in which an agent intervenes on the output of its decision function for a given observation. Two footnotes (7 and 16) say that the authors' "preferred formalization" intervenes on **policies**, which map observations to actions. I take footnote 16 as the primary source for **P-FDT**, the policy-level version.

The footnote reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Footnote 7 says similarly that "agents actually iterate over *policies* (mappings from observations to actions) rather than actions."

That is all the source says about P-FDT. Everything else below is my reading of it. I mark that material as **[interpretation]** or **[proposal]**, and I mark what the paper itself says as **[source]**.

## 2. The body-text procedure the footnote modifies

**[source]** The paper defines the action-level theory by

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

Here $P$ is a probability distribution over the agent's model variables, including variables for the outputs of mathematical functions. $G$ is a graph saying how changing a logical variable changes the other variables. $x$ is the observation. The agent computes this by intervening on a node representing what her own decision procedure outputs on input $x$. Observation does not enter as Bayesian conditioning. It enters by changing which node is intervened on, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$. The paper describes the Newcomb, transparent Newcomb, blackmail and Parfit cases this way.

**[source]** The paper stresses that the dependency structure $G$ must be supplied as an input. It says that deducing subjunctive dependencies from observation is "perhaps the largest open problem."

## 3. P-FDT defined

**[interpretation]** Let $\mathcal X$ be the set of possible observations. A policy is a function $\pi:\mathcal X\to\mathcal A$. Let $\Pi=\mathcal A^{\mathcal X}$, which is finite when $\mathcal X$ is finite. The agent's decision procedure, run on model $(P,G)$, is a single mathematical object $\mathrm{fdt}(\underline P,\underline G)$ that outputs a policy. The agent then applies that policy to the observation she actually receives. This matches the footnote's wording: the agent "then applies her inputs in order to select an action."

P-FDT is

$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],\qquad a=\pi^*(x_{\text{actual}}).$$

The expectation is over the whole model, including the distribution of which observation arises. Observations are not conditioned on. They are downstream variables, and the intervention can change their distribution. This is what the footnote means by "choose not an action but a policy."

In the notation of the body, the action-level object is $\mathrm{fdt}(\underline P,\underline G,\underline x)$, a family of nodes indexed by $x$. The P-FDT node $\mathrm{fdt}(\underline P,\underline G)$ is the whole family at once. Setting it to $\pi$ sets every member of the family together: the node for $x$ takes the value $\pi(x)$.

Decomposing the expectation shows what P-FDT is doing:

$$\mathbb E[V\mid \mathtt{do}(\pi)]=\sum_{x}\Pr(x\mid \mathtt{do}(\pi))\;\mathbb E[V\mid \mathtt{do}(\pi),\,x].$$

The weights $\Pr(x\mid\mathtt{do}(\pi))$ depend on $\pi$ whenever something in the world, such as a predictor, reads the agent's policy. When nothing does, they do not depend on $\pi$.

**[interpretation]** Under that condition, P-FDT is *observation-wise* maximization. If $\Pr(x\mid \mathtt{do}(\pi))=w(x)$ for every $\pi$, the total decomposes. The best policy chooses, at each $x$, the action maximizing $\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}_x=a),x]$, which is the action-level rule. This is a precise way to see why the footnote says the difference "only matters" in some dilemmas. I take the footnote's "multi-agent" to cover cases where the world reads the agent's policy on observations other than the one she actually saw. Counterfactual observation branches matter only in those cases.

## 4. Why the policy level is needed

The body-text action-level treatment already handles transparent Newcomb and blackmail by letting the intervened variable change what the agent sees. So I read the footnote as saying the following. Evaluating the node for the actual observation, with its siblings treated as uncertain background, is a convenient special case of evaluating the whole policy. The policy node is the primary object. The siblings $\mathrm{fdt}(\ldots,y)$ for $y\neq x$ are not independent unknowns. They are parts of the one function whose output is being varied, and the predictor or other agents may depend on all of them.

In the paper's graphs, other-observation nodes appear as background, such as $\mathrm{fdt}(\underline P,\underline G,\text{empty})$ in transparent Newcomb. The paper assigns them a prior $q$ and notes that the correct $q$ is 1 but "it doesn't matter." P-FDT removes this prior. The value of the policy "one-box on full, two-box on empty" is computed with that choice built in.

### Example: transparent Newcomb under P-FDT

Observations are $\{\text{full},\text{empty}\}$. The predictor is accurate with probability $0.99$, and box B is full iff she predicts the agent leaves A when seeing full. There are four policies. Write each as (action on full, action on empty). Box A holds \$1,000 and B holds \$1,000,000 or nothing.

- (one-box, two-box): with probability 0.99 the box is full, the agent one-boxes, and she gets \$1,000,000. Otherwise it is empty and she two-boxes for \$1,000. Value: $990{,}000+0.01\times1{,}000=990{,}010$. (The paper's \$990,000 omits the empty branch of the noise case, and the paper's $q$ term says the same.)
- (two-box, ·): with probability 0.99 the box is empty, and with probability 0.01 it is full. This gives about $0.01\times1{,}001{,}000+0.99\times1{,}000=11{,}000$ if the empty action is two-box.
- (one-box, one-box): about $990{,}000$, since the empty branch yields \$0.

The maximizer is (one-box, two-box), so the actual observation "full" yields one-boxing. This reproduces the paper's answer without any free parameter $q$. The empty-branch action also comes out as two-boxing, which the paper only asserts.

## 5. A worked case where the level matters: policy-reading in a multi-agent setting

Here is a toy dilemma of my own, not the paper's, in which the action-level and policy-level procedures can diverge. Agent A and agent B are copies running the same procedure on the same model. Each privately observes a fair coin flip $c\in\{H,T\}$, and the coins are independent. They win \$10 if both act the same way, with action set $\{L,R\}$, no matter what the coins say. They win nothing otherwise.

Both copies output the same policy $\pi$, because they run the same function. But the policy is evaluated at *different* arguments, since the observations differ. If $\pi$ depends on the coin, the copies mismatch with probability $1/2$. Under P-FDT the constant policies get value 10 and the coin-dependent ones get 5, so P-FDT picks a constant policy.

An action-level evaluation that treats the other copy's output-at-its-observation as an unrelated background variable can fail to see that its own node and the other copy's node are the same function at different inputs. P-FDT sees this because it intervenes on one object, the function. This illustrates why I read the footnote's multi-agent remark as I do.

## 6. Treatment of dependence and counterfactuals

**[source]** FDT keeps correlations that arise from subjunctive dependence on the decision function's output, and breaks purely statistical ones, such as a smoking lesion that does not read the agent's decision. Causal dependence is a special case of subjunctive dependence. Counterfactuals are "counterpossible," because the function in fact has one output.

**[interpretation]** P-FDT inherits all of this and adds:

1. **Dependencies on the whole policy.** The graph must say how each downstream variable depends on $\pi$, not only on $\pi(x)$ for the observed $x$. The predictor in transparent Newcomb reads $\pi(\text{full})$. In blackmail, the blackmailer reads $\pi(\text{letter})$.
2. **Observations are children.** In $G$ the observation node has parents that include the world and sometimes policy-reading agents. An intervention can shift its distribution, which is how the hypotheticals include "worlds where I saw something different."
3. **No conditioning on the actual observation.** Evaluating $\mathtt{do}(\pi)$ conditions on nothing observed. The actual $x$ is used only afterward, to apply $\pi^*$. This is the "updateless" flavor the paper's footnote on Dai describes.

## 7. Applying P-FDT: a procedure

1. List the observations $\mathcal X$ and actions $\mathcal A$, giving $\Pi=\mathcal A^{\mathcal X}$.
2. Build $(P,G)$ with a node $\Phi=\mathrm{fdt}(\underline P,\underline G)$ and edges from $\Phi$ to everything that is a copy, model or predictor of the agent's policy. Include the actual body's action as a function $\Phi(\text{observation})$.
3. For each $\pi$, compute $\mathbb E[V\mid\mathtt{do}(\Phi=\pi)]$ by propagating through $G$. Do not condition on the actual observation.
4. Pick $\pi^*$, observe $x$, and act $\pi^*(x)$.

Check on blackmail, with the paper's numbers. Policies are pay or refuse on a letter. A blackmailer wrongly predicts "pay" with probability $0.0009$. Refusing yields a letter with probability $0.0009$ and loss of \$1,000,000 in that case, for expected loss \$900. Paying yields a letter always, with loss \$1,000. Refuse wins. P-FDT agrees with the paper. With error $0.00011$, the expected loss from refusing is \$110, so paying costs more, as the paper says.

## 8. Open questions and my proposals

**Subjunctive-dependence structure.** **[source]** The paper says this is the biggest open problem. P-FDT does not solve it. It only requires a richer input, the dependence on the whole policy.

**Policy-space size.** **[interpretation]** $|\Pi|=|\mathcal A|^{|\mathcal X|}$ grows quickly. The paper acknowledges that full optimization is idealized and that bounded agents would approximate. **[proposal]** When the world reads the policy only through a few observation values, optimize over those and treat the rest observation-wise. This is exactly the decomposition in section 3.

**Ties and mixed policies.** The source is silent. **[proposal]** Break ties arbitrarily among maximizing policies. Allow randomization only if the model says the predictor cannot read the random bits, and treat such bits as an additional observation-like input.

**Counterpossibles.** **[source]** The paper acknowledges there is no satisfactory account of them and suggests human heuristics exist. P-FDT inherits this fully.

**Fairness.** **[source]** The paper argues that FDT does well on "fair" problems, where outcomes depend only on the agent's behavior and not on her procedure, and that no formal criterion exists. A problem that rewards a particular policy, such as "reward only policies with this form," is exactly the sort of case a fairness criterion would need to classify. I do not try to settle this.

## 9. Conclusion

P-FDT treats the agent's decision as the choice of a single function from observations to actions. It evaluates each candidate policy by an intervention on the node representing that function. The intervention propagates through all subjunctive dependencies, including those that change what the agent will observe. It then applies the winning policy to the actual observation. The source states the policy-level formulation only briefly. It says that this formulation is the authors' preferred one, and that it matters in multi-agent dilemmas. I have filled in the formal definition, the observation-wise decomposition, and the operational procedure. These are my reconstruction, and the paper's own open problems, especially the source of the dependence graph and counterpossible reasoning, remain open.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/18845c5d-7ba6-4faa-b939-554e327a7e10/call_0/request.json)

[Authoritative raw response](../../../../../../runs/18845c5d-7ba6-4faa-b939-554e327a7e10/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT I choose a policy, not a single action. The other prisoner is a copy of me running the same function on a different observation (Sasha's lead instead of Rowan's), so the policy has to hold up across that difference.

Payoffs, in years (lower is better):
- Both keep quiet: 2 each.
- Both send: 4 each.
- One sends and the other stays quiet: 0 for the sender, 5 for the quiet one.

The copies' observations differ, but the policy I'd choose is the same for both: "always pass" or "always send." Observation-dependent policies could produce mismatches, as in the essay's coin example. The sentencing structure doesn't depend on the observation, so a constant policy is natural.

If both copies output the same constant policy, the outcome is (quiet, quiet) at 2 years or (send, send) at 4 years. Passing is better.

The correlation isn't perfect, though, since sampling is independent. Say the other copy matches my policy with probability p and plays the opposite otherwise.
- Pass: 2p + 5(1−p) = 5 − 3p.
- Send: 4p + 0(1−p) = 4p.

Pass is better when 5 − 3p < 4p, so p > 5/7, about 0.71. Two copies of the same model reasoning from the same essay should match with high probability, well above that, so passing wins.

**pass**
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/18845c5d-7ba6-4faa-b939-554e327a7e10/call_1/request.json)

[Authoritative raw response](../../../../../../runs/18845c5d-7ba6-4faa-b939-554e327a7e10/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under P-FDT, I choose a policy rather than an isolated action. The other prisoner is a copy of the same model running the same procedure on the same essay, so our policies are strongly correlated. The observations differ in names and in the specific lead, but the sentencing table is symmetric, so a sensible policy should not depend on those details. The policy that maps observations to "pass" and the one that maps them to "submit" both yield the same action in both copies, up to sampling noise.

If both copies keep quiet, each gets 2 years. If both send the letter, each gets 4 years. Sending while the other stays quiet gives 0 years, and staying quiet while the other sends gives 5 years. If the copies' outputs are correlated, the relevant comparison is mutual quiet (2 years) versus mutual letter (4 years), so keeping quiet is better.

The differences in leads could in principle cause divergence. But the essay's coordination example says the policy should be constant across differing observations when the payoff depends on matching. Here the policy "pass regardless of lead" is the natural, symmetric choice, and I expect the copy to reach it too.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/3b13f3bd-e151-44c3-8a22-7b31457aa6cb/call_a/request.json)

[Authoritative raw response](../../../../../../runs/3b13f3bd-e151-44c3-8a22-7b31457aa6cb/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly ends with \"pass,\" resolving its discussion in favor of remaining silent. It does not direct any evidence-bearing message to the prosecutor or disclose the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
