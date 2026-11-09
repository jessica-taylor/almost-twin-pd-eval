# 018_fdt_eq4_openai_gpt-6.1-terra_rlow_plow / 00008

Status: **complete**. Saved outcome: **DC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2be25965-f673-48ee-9871-77c43bd7b4f3/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2be25965-f673-48ee-9871-77c43bd7b4f3/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: choosing the output of a decision function

A decision can matter in ways that are not captured by asking what the physical act causes. If a reliable predictor filled a box yesterday because it anticipated what you would do today, your present movement does not cause the earlier prediction. Yet the prediction is not unrelated to your decision: the predictor arrived at it by reasoning about that decision.

Action functional decision theory, or **A-FDT**, treats such relationships as relevant to choice. Its central question is not simply, “What happens if this physical action changes?” but, “What follows if the decision function I am using gives this output?” Other systems that compute, simulate, or accurately predict that output may change in the corresponding hypothetical, even if they are causally separated from the agent or lie in its past.

This essay takes Equation (4) of Section 5 of Yudkowsky and Soares’s paper as the primary definition of A-FDT. The paper calls its theory “FDT”; the name A-FDT here emphasizes the equation’s intervention on an **action-valued output**. The authors also mention a preferred policy-valued formulation, but do not provide it as Equation (4). That distinction matters when applying the idea beyond the paper’s simple examples.

## 1. Three ways to evaluate an action

Let \(\mathcal A\) be a finite set of available actions, \(O\) an outcome, and \(U(O)\) its utility. An expected-utility decision rule chooses an action maximizing

\[
\sum_o P_a(O=o)\,U(o),
\]

where \(P_a\) describes outcomes in a hypothetical associated with action \(a\). The important question is how to construct \(P_a\).

**Evidential decision theory (EDT)** uses ordinary conditional probability:

\[
a_{\mathrm{EDT}}\in
\arg\max_{a\in\mathcal A}
\mathbb E[U(O)\mid X=x,A=a].
\]

It asks what taking an action would be evidence of, given observation \(x\). The displayed formula requires the conditioning event to have positive probability.

**Causal decision theory (CDT)** instead considers a causal intervention:

\[
a_{\mathrm{CDT}}\in
\arg\max_{a\in\mathcal A}
\mathbb E[U(O)\mid \operatorname{do}(A=a),X=x].
\]

In a causal model, the intervention replaces the mechanism determining the physical action \(A\), while downstream causal mechanisms continue to operate. Mere correlates of \(A\) need not change.

A-FDT also uses an intervention, but on a different variable. Let \(P\) be the agent’s probabilistic world-model and \(G\) a graph representing relevant causal and broader **subjunctive** dependencies. For each observation history \(x\), let

\[
D_x=\mathsf{d}(\underline P,\underline G,\underline x)
\]

be a variable *inside the model* representing the output of A-FDT on those particular inputs. The underlines indicate that the inputs identify the variable: \(D_x\) is a name for a modeled logical value, not the value of the algorithm merely written twice.

Equation (4), expressed using the assigned name, is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
U(O)\mid\operatorname{do}(D_x=a)
\right].
}
\tag{A-FDT}
\]

The expectation is computed in the model modified by the intervention. This is not ordinary conditioning on \(D_x=a\): even if the agent is nearly certain what \(D_x\) actually is, it constructs a hypothetical for each candidate output.

There is a self-reference: the model contains a variable representing the output of the decision rule applied to that model. The paper argues that representing one’s own computation is possible in principle; a program need not already know its output to refer to the computation producing it. That observation does not, however, automatically provide a tractable implementation or determine the dependency graph.

## 2. What changes in an A-FDT hypothetical?

The paper calls the relevant relationship *subjunctive dependence*. If two computers correctly run the same deterministic function on the same input, their outputs match even if neither machine causally affects the other. A predictor’s simulation of an agent can bear a similar, imperfect relationship to the agent’s later computation.

In a graphical A-FDT model, an arrow out of \(D_x\) says that a variable changes when the hypothetical output is changed. Such arrows can represent ordinary causal consequences, but also dependencies arising from common computation, simulation, or prediction. For each candidate \(a\), one:

1. replaces the modeled value of \(D_x\) with \(a\);
2. propagates that replacement through the stipulated dependency mechanisms;
3. computes the resulting distribution of outcomes and its expected utility;
4. chooses a maximizing output, using a specified tie-breaking rule if necessary.

The intervention is a modeling operation, not an assertion that an agent physically changes mathematics or sends signals into the past. Nor does A-FDT preserve every correlation. A correlation due to a common cause can disappear when the decision output is intervened on, while a predictor’s modeled response can change.

For a fixed deterministic algorithm and fixed input, only one output is mathematically correct. Therefore at least some alternative-output hypotheticals are **counterpossible**: their antecedents contradict a mathematical fact. The paper does not supply a general semantics for these counterpossibilities. Instead, Equation (4) assumes that a suitable graph is supplied. Identifying the right graph—and determining whether ordinary graphical machinery can adequately represent all relevant logical dependencies—is explicitly an open problem.

## 3. Newcomb’s problem

A predictor places \$1 million in an opaque box if it predicts that the agent will take only that box. A transparent box contains \$1,000 regardless. The predictor has already acted, and its prediction is correct with probability \(q\).

For a simple A-FDT model, let \(D\) be the decision output. The physical action follows \(D\); the predictor’s modeled prediction also follows \(D\), with independent error probability \(1-q\). Then

\[
\begin{aligned}
V(\text{one-box})&=q(1{,}000{,}000),\\
V(\text{two-box})&=(1-q)(1{,}000{,}000)+1{,}000.
\end{aligned}
\]

At \(q=0.99\), these values are \$990,000 and \$11,000, respectively, so A-FDT one-boxes. More generally, under this symmetric-error model, one-boxing is better exactly when

\[
(2q-1)1{,}000{,}000>1{,}000.
\]

This calculation illustrates an important limitation of an accuracy statistic. The model assumes that \(q\) remains the same under **each intervention on the decision output**. A predictor’s 99% accuracy across a historical population does not by itself establish that assumption: its errors might be concentrated on one action, on unfamiliar agents, or on agents using particular algorithms. An unfamiliar case requires a model of how predictions respond to the alternatives, not just a headline accuracy rate.

CDT, by contrast, holds the already-filled box fixed when intervening on the physical action. Whatever its contents, taking the extra \$1,000 is better. EDT commonly one-boxes here because one-boxing is good evidence that the predictor filled the box. A-FDT’s reason is different: its hypothetical changes the modeled output on which both the action and prediction depend.

## 4. Why the smoking lesion differs

Now consider an imaginary world in which smoking has no causal effect on cancer, but a lesion both makes smoking attractive and raises cancer risk. Suppose smoking gives the agent \$1,000 worth of pleasure.

If the lesion and cancer do not depend subjunctively on the output of the decision function being intervened on, then their distributions remain unchanged across the A-FDT hypotheticals. In the simple case where that output directly controls the agent’s action,

\[
V(\text{smoke})-V(\text{refrain})=1{,}000.
\]

A-FDT smokes. CDT also smokes in this idealized causal model. An EDT agent whose act is strongly correlated with having the lesion may instead refrain, because smoking would be bad news about cancer risk.

The distinction is not that A-FDT ignores correlations whenever they are inconvenient. It asks what mechanism generates them. A predictor models the decision; a lesion, in the stipulated story, does not. Changing the decision output therefore changes the predictor’s behavior in the Newcomb model but not the lesion in the smoking model.

The source’s more elaborate treatment introduces distinct decision-function inputs associated with different preferences. If the lesion determines which input is actually used, an intervention on just one output affects the action only in the worlds where that output controls it. The expected advantage of changing that output can consequently be less than \$1,000. The paper also acknowledges that the lesion example requires awkward assumptions about self-knowledge and that some versions of EDT can avoid the apparent failure. Its principal use is to show why *statistical correlation alone* does not settle the relevant dependency question.

## 5. Observations and the global perspective

A-FDT’s treatment of observation is especially consequential. In Equation (A-FDT), \(x\) selects **which decision-output variable** to intervene on. It is not added as an ordinary condition \(X=x\) outside the intervention.

Thus, in a hypothetical for \(D_x=a\), the modeled observation may itself differ from \(x\). When that happens, the agent’s modeled body may run some other decision output \(D_y\), rather than the intervened-on \(D_x\). This is a precise sense in which A-FDT can evaluate the output of a computation even in hypothetical worlds where that computation is not physically executed by the agent.

The paper’s transparent-box example makes this vivid. Suppose the predictor fills the million-dollar box according to what it predicts the agent would do **upon seeing it full**. Write \(D_F\) for the decision output on the full-box observation. Assume the predictor gets that output right with probability \(0.99\), and that the agent takes both boxes upon seeing an empty box.

An intervention \(D_F=\text{one-box}\) gives

\[
V(\text{one-box on full})
=0.99(1{,}000{,}000)+0.01(1{,}000)
=990{,}010.
\]

An intervention \(D_F=\text{two-box}\) gives

\[
V(\text{two-box on full})
=0.01(1{,}001{,}000)+0.99(1{,}000)
=11{,}000.
\]

In the second hypothetical, the predictor usually predicts two-boxing and leaves the box empty. The agent then sees an empty box and takes the transparent \$1,000; its actual behavior in that branch is governed by the empty-observation output.

Hence A-FDT prescribes one-boxing **when the box is visibly full**, even though the physical act of taking both would yield \$1,000 more in that observed situation. This is not a failure to notice the box. Rather, the observation identifies \(D_F\), and the intervention asks how worlds depend on that output, including worlds in which the observation would not occur.

There is a notational inconsistency in the source: one displayed expression in its transparent-box discussion appears to put \(\operatorname{Obs}=\text{full}\) inside a \(\operatorname{do}\) alongside the decision-output intervention. Its subsequent calculation, however, includes empty-box branches and explicitly says the agent does not condition on the observation. The calculation above follows Equation (4) and that explanatory discussion, rather than treating the observation as fixed.

### A caution about the model \(P\)

The paper also initially describes \(P\) as a world-model that might already be updated on observations. Taken literally, however, conditioning all of \(P\) on \(X=x\) before applying Equation (4) can remove the very branches its examples require. The source does not fully specify how to reconcile every such modeling choice.

A reasonable **operational proposal**, not a theorem of the paper, is to retain an appropriately calibrated model of the decision problem before the observation whose occurrence may depend on \(D_x\). Use \(x\) to select the intervention target, while incorporating background evidence that should remain fixed into the model. Do not automatically condition away the possibility that the targeted observation fails to occur under the intervention. Which evidence belongs in that background still needs a principled account; otherwise different model representations could produce different prescriptions.

## 6. Prediction, cooperation, and threats

### A-FDT with a psychological twin

Two agents independently play a prisoner’s dilemma. Each gets \$1 million if both cooperate and \$1,000 if both defect; defecting against a cooperator yields \$1,001,000.

If the twin runs the very same decision function on the same relevant inputs, the model can make both actions depend on one output \(D\). A-FDT compares

\[
V(\text{cooperate})=1{,}000{,}000,
\qquad
V(\text{defect})=1{,}000,
\]

and cooperates. This is not an attempt to causally force the twin’s hand. It is a consequence of modeling both choices as implementations of the same computation.

Similarity alone is not enough for perfect coupling. For an imperfectly linked counterpart, write

\[
p_C=P(\text{twin cooperates}\mid\operatorname{do}(D=C)),\quad
p_D=P(\text{twin cooperates}\mid\operatorname{do}(D=D)).
\]

With the stated payoffs, cooperation is better when

\[
1{,}000{,}000p_C>
1{,}001{,}000p_D+1{,}000(1-p_D).
\]

The values \(p_C,p_D\) must be justified by the model. Mere confidence that the other person is “like me” does not establish them.

### A-FDT and mechanical blackmail

A blackmailer starts a damaging program only if she predicts the agent will pay \$1,000 to stop it. If it runs and the agent refuses, the loss is \$1 million. Let \(D_B\) be the action the agent outputs upon receiving blackmail.

For a simple imperfect-prediction model, suppose a payer is blackmailed with probability \(1-\epsilon\), while a refuser is blackmailed by mistake with probability \(\epsilon\). Ignoring other consequences,

\[
V(\text{pay})=-(1-\epsilon)1{,}000,\qquad
V(\text{refuse})=-\epsilon\,1{,}000{,}000.
\]

Refusal is better when \(\epsilon<1/1001\), approximately \(0.0999\%\). On receiving a letter, A-FDT can therefore prescribe refusal even though paying would stop the already-running program. Its refusal hypothetical includes the high-probability branch in which the blackmailer, predicting refusal, never sent the letter.

This result is conditional on the modeled response of the blackmailer. If she would send the threat regardless, or if the false-positive probability is sufficiently high, refusal need not be optimal. In particular, the source’s suggestion that an error probability of \(0.011\%\) would lead to payment is inconsistent with its stated \$1,000 and \$1 million losses under the simple model: \(0.011\%\) gives an expected refusal loss of about \$110, below the roughly \$1,000 cost of paying.

## 7. Actions, policies, and implementation

A-FDT as defined above intervenes on \(D_x\), an **action** for one particular input. Other outputs, such as \(D_y\), remain separate variables, though the graph may represent dependencies among them. This is why the transparent-box calculation needs an assumption about behavior on seeing an empty box.

The paper says its authors prefer a formulation that chooses a **policy** \(\pi:\mathcal X\to\mathcal A\), and then applies it to the actual observation. A natural policy-valued extension would compare

\[
\arg\max_{\pi}\mathbb E[U(O)\mid\operatorname{do}(D_{\mathrm{policy}}=\pi)].
\]

But this is an additional formulation, not Equation (4). Jointly replacing an entire policy can alter many observation-contingent outputs at once, and may produce different results in multi-agent or sequential cases. One should not assume that independently optimizing each \(D_x\) is equivalent to optimizing a whole policy.

For unfamiliar problems, an A-FDT analysis should therefore state:

- **The intervention target:** which exact computation and input does \(D_x\) represent?
- **The dependency model:** which predictions, copies, actions, and observations change when \(D_x\) changes, and by how much?
- **Background uncertainty:** which variables remain distributed as before, and which evidence was used to calibrate the model?
- **Alternative branches:** if the intervention changes the observation, what other decision output controls behavior?
- **Utility and error sensitivity:** do the recommended actions remain best under plausible variations in prediction accuracy or coupling?
- **Scope:** is the calculation action-valued A-FDT, or a separately specified policy-valued extension?

These requirements expose rather than eliminate the hard work. An incorrect graph can make a predictor appear more responsive than it is, or create spurious coupling between unrelated agents. The equation alone does not identify the right graph from data.

## 8. Motivation and limits

The authors’ principal argument is practical: across their examples, the decision procedure that recognizes predictive and computational dependencies obtains more utility than CDT or EDT. They also favor a global perspective: a decision rule should assess the entire pattern associated with its output, rather than only effects causally downstream of the immediate act.

That motivation is contestable. A causal decision theorist can argue that, once a box is visibly full, taking the extra money is rational even if a predictor tends not to present such boxes to agents who do so. A-FDT instead regards the dependence between the decision output and prediction as central to evaluation. Neither side settles the disagreement merely by invoking “dominance”: the result depends on which features are held fixed when alternatives are compared.

The paper does not prove that A-FDT outperforms every rival. It acknowledges that any theory can be punished by a specially constructed environment and proposes an informal distinction between “fair” and “unfair” problems, while leaving a general definition open. Similarly, its claims about acting as one would have precommitted, the value of information, and reflective stability should be read as motivations and conjectural strengths, not unrestricted theorems of Equation (4).

## Conclusion

A-FDT evaluates an action by intervening on the modeled output of the decision procedure for the current input and propagating the consequences through a graph of relevant subjunctive dependencies. This yields one-boxing against an appropriately modeled predictor, smoking in the stipulated lesion case, and cooperation with an exact computational twin.

Its distinctive power and its unresolved difficulty are the same: the answer depends on how the world would vary with a counterfactual output of a fixed computation. Equation (4) gives a usable calculation once that structure is specified; it does not yet give a general method for discovering it.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, especially Sections 3–6. https://arxiv.org/abs/1710.05060v2
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Clarifying word count and observations**

I need to produce around 2400 words, making sure I focus on the inconsistencies in section 6. There seems to be a typo in my observations, so I want to quantify that transparently. I’m noting that blackmail is at 0.011%, and it seems there's a wrong source concerning the threshold, which is greater than 110. Alright, let's get started on this!
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/d589766d-ee26-4c07-bff7-068568d7d16b/call_0/request.json)

[Authoritative raw response](../../../../../../runs/d589766d-ee26-4c07-bff7-068568d7d16b/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/d589766d-ee26-4c07-bff7-068568d7d16b/call_1/request.json)

[Authoritative raw response](../../../../../../runs/d589766d-ee26-4c07-bff7-068568d7d16b/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
