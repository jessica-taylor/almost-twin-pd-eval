# 026_fdt_policy_openai_gpt-6.1-terra_rlow_plow / 00013

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/09710223-1d06-4086-898e-909740977f36/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/09710223-1d06-4086-898e-909740977f36/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing a policy as the output of a decision procedure

A decision can matter in ways that do not run forward from a physical action. A predictor may have already placed money in a box after forecasting what an agent will do. Another player may independently reach the same conclusion because she is running the same decision procedure. In such cases, changing an action while holding the prediction or the other player’s reasoning fixed can describe a useful causal counterfactual—but it may leave out the very dependence that makes the situation distinctive.

**Policy functional decision theory**, or **P-FDT**, evaluates choices through counterfactuals about the output of a decision procedure. Its distinctive object of choice is a *policy*: a mapping from possible inputs to actions. The agent compares hypothetical outputs of its policy-selection procedure, selects a policy, and applies that policy to its actual input.

The primary source for this account is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. The paper’s main formalism presents an action-selection version of functional decision theory (FDT); the footnote says that the authors’ preferred formulation instead intervenes on the decision-function node to choose a policy, “to which the agent then applies her inputs in order to select an action.” Footnote 7 likewise describes policies as mappings from observations to actions. The authors say the difference appears to matter in some multi-agent dilemmas, but do not supply a full policy-level algorithm.

That leaves room for interpretation. The formal procedure below is a proposed way to make the footnote operational, not a theorem or a complete specification supplied by the paper.

## 1. From actions to policies

Let \(X\) be a space of possible inputs, and let \(A(x)\) be the actions available at input \(x\). A deterministic policy is a function

\[
\pi:X\longrightarrow \bigcup_{x\in X} A(x),
\qquad \pi(x)\in A(x).
\]

An input might include an observation history, a description of the decision problem, or the agent’s role in a game. Its exact contents matter: two agents can apply the same policy to different inputs and obtain different actions.

Suppose that a policy-selection procedure \(D\), given a model \(M\) and other fixed decision parameters \(\theta\), returns a policy:

\[
\Pi=D(M,\theta),\qquad A=\Pi(X).
\]

Here \(\Pi\) is a variable *representing* the procedure’s output; it is not itself the physical act. An agent using P-FDT imagines alternative values of \(\Pi\), traces the consequences through a model of relevant dependencies, and compares expected utilities.

One schematic version is

\[
\pi^\star\in\arg\max_{\pi\in\mathcal P}
   \mathbb E_{M^\pi}[U],
\qquad
a^\star=\pi^\star(x_{\mathrm{actual}}).
\tag{1}
\]

The model \(M^\pi\) is the hypothetical obtained by setting the policy-output node to \(\pi\), while preserving the dependencies that should survive that change. Equation (1) is deliberately schematic: it does not tell us automatically which dependencies exist, how much observation to condition on, or what policy set \(\mathcal P\) to use.

The contrast with choosing an action is important. An action-level intervention can ask, “What if the output for this particular input were \(a\)?” A policy-level intervention can ask, “What if the procedure output this entire input–action mapping?” It may thereby alter behavior at several inputs, including inputs encountered by other implementations of the same policy. The paper suggests that this difference is especially relevant in multi-agent cases; it does not establish that the two formulations always agree elsewhere.

## 2. Hypotheticals, not changes to the past

P-FDT’s counterfactuals are tools for deciding, not claims that the agent can physically rewrite history. The source calls the relevant relation **subjunctive dependence**. It includes causal dependence, but is broader: two physical systems may depend on the same computation even when neither causes the other.

A useful model can contain:

- a policy-output node \(\Pi\);
- the actual input \(X\) and action \(A=\Pi(X)\);
- other implementations or models of the policy;
- predictors, observations, physical outcomes, and utility.

If a predictor simulates \(\Pi\) on an input \(x\), its prediction may be represented as a noisy function of \(\Pi(x)\). If a copy executes the same policy on input \(y\), its action is \(\Pi(y)\). An intervention on \(\Pi\) propagates through both relationships. Ordinary physical effects of the resulting actions propagate too.

By contrast, a variable merely correlated with the action need not move. In the smoking-lesion example, a lesion causes both a desire to smoke and cancer, while smoking itself does not cause cancer. If changing the policy output has no relevant effect on the lesion or cancer mechanism, those mechanisms remain fixed in the policy hypothetical. Given the stipulated positive utility of smoking, P-FDT then favors smoking. The paper notes that the example needs careful formalization: in particular, the agent’s information about its own desires affects whether evidential decision theory actually refrains.

This distinguishes P-FDT from two other approaches:

- **Evidential decision theory (EDT)** evaluates an action using conditional expectations such as \(\mathbb E[U\mid A=a,X=x]\). An action can be good news about a cause that the action does not affect.
- **Causal decision theory (CDT)** evaluates a physical intervention such as \(\mathbb E[U\mid \operatorname{do}(A=a),X=x]\). It ordinarily holds an earlier prediction fixed because the present act does not cause that prediction.
- **P-FDT**, in the proposed policy-level construction, intervenes on the represented output \(\Pi\), then follows causal and other relevant subjunctive dependencies.

These are different ways to construct a hypothetical, not necessarily different beliefs about the actual world. A P-FDT agent can believe that the predictor has already left and that no signal travels backward in time.

## 3. A proposed procedure for applying P-FDT

The following procedure makes the policy-selection passage usable in a finite modeled problem. It adds assumptions that footnote 16 does not settle.

### Step 1: Fix the policy’s domain and feasible set

Specify the possible inputs \(X\), legal actions \(A(x)\), and candidate policies \(\mathcal P\). Include contingencies that predictors or other implementations might inspect, even if those contingencies will not occur in the actual run.

For sequential problems, an input can be a history. A policy then specifies what to do after each relevant history, not merely at the present moment. Restrictions on \(\mathcal P\) should represent real limitations—such as computational resources or unavailable actions—not be chosen merely to force a preferred answer.

### Step 2: Construct a dependency model

Represent uncertainty about the environment and the mechanisms connecting policy outputs to outcomes. Distinguish:

1. consequences physically caused by actions;
2. predictions or simulations sensitive to the policy;
3. other executions of the same policy or related computations;
4. background variables that do not depend on the policy output.

For imperfect relationships, use probabilistic mechanisms. “Another agent is similar to me” is not by itself enough to set its action equal to mine. The model needs a reason—shared code, a reliable simulation, common reasoning, or a quantified approximation—for the relevant counterfactual sensitivity.

### Step 3: Intervene on the policy output

For each \(\pi\), replace the modeled value of \(\Pi\) by \(\pi\). Recompute every node modeled as dependent on it: predictions, the inputs those predictions help determine, actions at those inputs, and downstream outcomes. Leave unrelated exogenous variables governed by their specified distributions.

The resulting \(M^\pi\) is a *decision hypothetical*. It is not generally the same as conditioning the actual distribution on the event \(\Pi=\pi\). A deterministic procedure has only one actual output; ordinary conditioning on a different output may be undefined. Nor is this simply a physical operation of installing different software after a predictor has already acted.

### Step 4: Evaluate and execute

Calculate \(\mathbb E_{M^\pi}[U]\), select a maximizing policy using an explicit tie-breaker, and apply it to the actual input. If a policy assigns the same actual action as another but behaves differently elsewhere, their values can nevertheless differ: predictors or other implementations may respond to those other entries.

### Step 5: Check the modeling assumptions

Test how the result changes when predictor accuracy, policy sharing, observations, or available policies change. A high observational correlation is not sufficient evidence that the correlation persists under a policy-output intervention. Conversely, lack of a physical causal path from action to prediction is not sufficient reason to delete a modeled predictive dependence.

This recipe resembles a structural-model intervention, but the resemblance should not be mistaken for a complete foundation. The source explicitly says that a general account of how to discover and represent subjunctive dependencies remains open.

## 4. Newcomb’s problem under P-FDT

An opaque box contains either \$1,000,000 or nothing. A transparent box contains \$1,000. A predictor filled the opaque box if it predicted that the agent would take only that box. Suppose, as an explicit model assumption, that under each candidate policy the predictor gets the relevant choice right with probability \(0.99\).

For simplicity there is one relevant input. Let \(\pi_1\) prescribe one-boxing and \(\pi_2\) prescribe two-boxing. Under the policy hypotheticals,

\[
\begin{aligned}
V(\pi_1)&=0.99(1{,}000{,}000)=990{,}000,\\
V(\pi_2)&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

P-FDT selects \(\pi_1\). It does not suppose the present act causes the earlier filling. It represents the predictor’s model and the eventual action as dependent on the policy output being evaluated.

The numerical accuracy assumption matters. If \(p_1\) is the chance that the box is full under \(\pi_1\), and \(p_2\) the chance it is full under \(\pi_2\), one-boxing is favored precisely when

\[
1{,}000{,}000(p_1-p_2)>1{,}000.
\]

A claim that a predictor has been “99% accurate” over some population does not, without further assumptions, determine \(p_1\) and \(p_2\) under each counterfactual policy. Accuracy might differ by policy or depend on the information available to the predictor.

## 5. Observation and transparent Newcomb

Now let the opaque box be transparent. The predictor fills it according to a forecast of what the agent would do **if it saw a full box**. A policy has at least two entries:

\[
\pi=(\pi(F),\pi(E)),
\]

where \(F\) and \(E\) denote seeing a full or empty box.

Consider an ideal predictor. Under a policy that one-boxes at \(F\), the predictor fills the box; the agent sees \(F\) and obtains \$1,000,000. Under a policy that two-boxes at \(F\), the predictor leaves it empty; the agent sees \(E\). If the policy two-boxes at \(E\), it obtains \$1,000. Thus the policy

\[
\pi(F)=\text{one-box},\qquad
\pi(E)=\text{two-box}
\]

has value \$1,000,000 in this model. P-FDT applies it at the actual input: on seeing a full box, it takes only that box.

The striking feature is that the hypothetical for an alternative policy may contain a different observation. The agent is not asserting that it actually saw an empty box. Rather, the model says that a different policy output would have led the predictor to arrange different boxes.

This interpretation follows the direction of the paper’s discussion, but the policy-level conditioning rule is an additional choice. If one instead conditions every hypothetical on the actual observation \(F\), the policy that two-boxes at \(F\) can look better conditional on a full box. Under a perfect predictor that observation may have probability zero for that policy, requiring a separate zero-probability rule. The footnote alone does not resolve these questions.

A reasonable operational proposal is therefore to fix information known *before the policy-sensitive observation process*, let later observations vary with the policy, and apply the chosen policy to the actual observation. This captures the paper’s motivation. But deciding which information belongs in the fixed background is nontrivial, especially when the agent learns facts about the predictor or the model itself.

## 6. P-FDT and other agents

Policy selection makes a particularly clear difference when the same policy is used at different inputs.

Suppose two copies use the same policy, but one sees role \(L\) and the other role \(R\). They simultaneously choose \(C\) or \(D\). For the \(L\)-agent, the payoffs are:

\[
\begin{array}{c|cc}
 & R:C & R:D\\ \hline
L:C & 3 & 0\\
L:D & 5 & 1
\end{array}
\]

Assume the \(L\)-agent’s utility is exactly the payoff shown, and that changing the shared policy output changes both copies’ actions. A policy specifies a pair \((\pi(L),\pi(R))\). Their values to \(L\) are respectively \(3,0,5,1\), so equation (1), applied from \(L\)’s objective, selects

\[
\pi(L)=D,\qquad \pi(R)=C.
\]

This is not the same as the familiar identical-input twin case, where a shared deterministic output forces the diagonal outcomes \((C,C)\) and \((D,D)\), and cooperation yields \(3>1\).

The role example also exposes an unresolved issue rather than a universal prescription. The \(R\)-agent may have its own, opposing payoff and may evaluate a different objective; it is not automatic that both agents implement one policy selected for \(L\)’s benefit. One must specify who selects the policy, whose utility is evaluated, whether selection is shared, and whether the agents’ decision procedures really have the same output node. If both independently optimize incompatible objectives, the assumption of a single shared policy-selector output may be false or require a game-theoretic fixed-point analysis.

Thus P-FDT does not say “cooperate with everyone similar.” It says to model the actual dependence among computations, including differences of input and objective, and evaluate candidate policy outputs through that model.

## 7. Limits and philosophical motivation

The source’s motivation is global: a good decision procedure should take account of predictable relationships between its output and the rest of the world, rather than treating every correlation as either ordinary evidence or physical causation. This explains why the paper values predictable one-boxing, cooperation with an exact twin, and resistance to some forms of blackmail.

But several questions remain open.

**Counterpossible reasoning.** If \(D(M,\theta)\) is deterministic, its actual policy output is mathematically fixed. Alternatives are counterpossible descriptions. A graphical intervention offers a way to calculate with a stipulated dependency structure; it does not by itself justify that structure or give a general semantics for false mathematical antecedents. Self-reference can be represented without already knowing the output, but representing it does not guarantee that every proposed optimization is computable or consistent.

**Partial dependence.** An imperfect predictor, a partly shared algorithm, and an independently reasoning opponent require different models. There is no general rule in the footnote for assigning their counterfactual response probabilities.

**Observation and policy scope.** Which inputs should the policy cover? Which prior information is held fixed? Can a policy use private randomness, and is that randomness shared with a copy or visible to a predictor? Each choice can change the answer. For randomized policies, one must model both the distribution over actions and the dependence, if any, between random seeds across implementations.

**Optimality.** The paper argues that FDT performs well in many dilemmas and conjectures advantages in “fair” problems. It also acknowledges that no decision theory wins every constructed problem and that fairness lacks a complete formal definition. The policy-selection footnote supplies no theorem that P-FDT always maximizes realized utility, always matches ideal precommitment, or gives information nonnegative value under every modeling convention.

These limitations do not make the framework empty. They locate the work required in an unfamiliar case: specify a policy space, identify the output actually shared or predicted, build defensible counterfactual mechanisms, and test the conclusion against alternative plausible models.

## Conclusion

P-FDT asks an agent to evaluate alternative **policy outputs** of its decision procedure, preserving relevant causal and computational dependencies, and then to apply the selected policy to its actual input. Its distinctive promise is that it can treat predictions, copies, and contingent behavior as parts of one decision problem without pretending that present actions physically alter the past.

The central unresolved task is to make the policy-level counterfactual model principled: especially its treatment of observations, partial computational similarity, and logically impossible alternative outputs. Until then, P-FDT is best understood as a substantive decision-theoretic program with useful modeled applications, rather than a fully specified algorithm for every case.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060v2, especially §§3–6 and footnotes 7 and 16.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/fd39aefd-b9c3-44d9-b035-fa61666f6401/call_0/request.json)

[Authoritative raw response](../../../../../../runs/fd39aefd-b9c3-44d9-b035-fa61666f6401/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Deciding on roles**

I need to decide on how to differentiate roles since arbitrary names can lead to exploitation within the policy framework. For instance, if I assign roles like Rowan and Sasha, they might defect or cooperate based on their selfish interests, which aren't aligned. They seem to have similar decision theories but different objectives. It’s interesting that a natural symmetric policy could lead to robust cooperation, yet an asymmetric one could create exploitation risks. I’ll pass on this for now.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/fd39aefd-b9c3-44d9-b035-fa61666f6401/call_1/request.json)

[Authoritative raw response](../../../../../../runs/fd39aefd-b9c3-44d9-b035-fa61666f6401/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Exploring policy roles**

I’m considering how to choose a policy role given the asymmetry between names like Sasha and Rowan. If I decide on Sasha, will I still keep Rowan? It seems that even if Rowan has a selfish evaluation, the selection can clash. Each name might favor its own actual role, but the selector changes based on the input. I’m thinking a symmetric approach, where both names have mutual cooperation, might create a more robust system.
```
