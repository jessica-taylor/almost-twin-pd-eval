# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00002

Status: **complete**. Saved outcome: **DC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6b7d3807-8b03-46fb-ab5f-03e7d2e9fb0e/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6b7d3807-8b03-46fb-ab5f-03e7d2e9fb0e/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory: How to Decide as a Fixed Computation

Action functional decision theory (A-FDT) is a decision theory for agents who treat their own decision-making as the evaluation of a fixed mathematical function. Instead of asking, “Which physical act of mine causes the best outcome?” as causal decision theory (CDT) does, or “Which act would be best news to learn I performed?” as evidential decision theory (EDT) does, A-FDT asks:

> Which output of this very decision function would yield the best expected outcome?

The name “A-FDT” here refers to the action-level formalization given in Equation (4), Section 5 of Yudkowsky and Soares’s paper on functional decision theory. The source calls the theory FDT; I use A-FDT consistently to emphasize that the equation under discussion chooses an action at a given input. The core idea is that an agent should evaluate actions by intervening, in her world-model, on a variable representing the output of her own decision procedure, rather than on a variable representing only her bodily movement.

This essay explains the formal rule, the dependency structure it presupposes, and how to apply it in examples such as Newcomb’s problem, the smoking lesion problem, transparent Newcomb problems, and Parfit’s hitchhiker problem. It also identifies where the source leaves important details open—especially the construction of the dependency graph and the treatment of observations—and proposes operational readings where possible.

---

## 1. Expected utility and three kinds of hypotheticals

All three standard theories discussed here—EDT, CDT, and A-FDT—are expected utility theories. An agent has:

- a finite action set \(\mathcal A\);
- a countable outcome set \(\mathcal O\);
- a utility function \(\mathcal U : \mathcal O \to \mathbb R\);
- an observation history \(x \in \mathcal X\);
- a world-model \(P\), usually a probability distribution over relevant variables;
- a dependency structure \(G\), such as a graph encoding how variables depend on one another.

Let \(V = \mathcal U(\text{Outcome})\). EDT evaluates an action by conditionalizing on that action:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[V \mid \text{Obs}=x,\ \text{Act}=a\right].
\]

CDT evaluates an action by performing a causal intervention on the physical action variable:

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[V \mid do(\text{Act}=a),\ \text{Obs}=x\right].
\]

A-FDT, following Equation (4) of the source, evaluates an action by intervening on a logical variable representing the output of the agent’s own decision procedure. Let

\[
D_{P,G,x}
\;:=\;
\mathrm{A\text{-}FDT}(\underline P,\underline G,\underline x),
\]

where the underlines indicate quotation or naming: \(\underline P\) is a name for the model \(P\), \(\underline G\) a name for the graph \(G\), and \(\underline x\) a name for the observation input. The variable \(D_{P,G,x}\) is a variable inside the agent’s model representing what A-FDT itself outputs when run on that model, graph, and observation. Then A-FDT prescribes:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E\!\left[V \mid do(D_{P,G,x}=a)\right].
\]

This is the central equation. It says: for each candidate action \(a\), imagine the world as it would be if the decision function \(D_{P,G,x}\) output \(a\); compute the expected utility in that hypothetical world; choose the action with the highest expected utility.

The notation is self-referential: the model contains a variable representing the output of the very algorithm that is using the model. The source notes that this self-reference can be made precise using standard fixed-point or “quining” techniques, such as those associated with Kleene’s recursion theorem. Operationally, an agent need not possess a perfect self-model; it only needs some representation of the output of its decision procedure.

The \(do(\cdot)\) operator is borrowed from Pearl’s causal modeling framework. In a causal graph, \(do(Z=z)\) means: set \(Z\) to \(z\), cut incoming arrows to \(Z\), and propagate the consequences through the graph. In CDT, the intervened variable is physical: \(\text{Act}\). In A-FDT, the intervened variable is logical or computational: the output of the decision function. Accordingly, \(G\) cannot be merely a causal graph in the narrow Pearl-style sense. It must also encode logical, mathematical, computational, or predictor-based dependencies. The source calls these relations subjunctive dependencies.

---

## 2. Subjunctive dependence

A-FDT’s distinctive move is to distinguish predictor-like correlations from lesion-like correlations.

Suppose two reliable calculators compute \(6288+1048\). They are causally isolated, perhaps on different continents. Still, if one outputs \(7336\), we have reason to think the other outputs \(7336\). Their outputs are not causally connected, but they are linked by a common mathematical fact: both are computing the same function correctly. The source calls this kind of relation subjunctive dependence.

Predictors can create similar dependencies. If a predictor has an accurate model of an agent’s decision procedure, then the predictor’s prediction and the agent’s action are linked. If the agent’s decision function were to output differently, the predictor’s prediction would also have been different, assuming the predictor was accurate. By contrast, a lesion that statistically correlates with smoking and cancer does not compute anything about the agent’s decision procedure. Smoking is evidence of the lesion, but the lesion does not depend on the output of the agent’s decision function.

The source summarizes the relationship neatly: functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence. CDT holds fixed everything except the causal downstream effects of the physical action. A-FDT holds fixed everything except the consequences of changing the output of the decision function. EDT, by contrast, merely conditions on the action and thereby preserves too many correlations, including merely evidential ones.

This explains A-FDT’s pattern of prescriptions:

- In Newcomb’s problem, the predictor’s prediction subjunctively depends on the agent’s decision function, so A-FDT one-boxes.
- In the smoking lesion problem, cancer does not subjunctively depend on the decision function, so A-FDT smokes.
- In transparent Newcomb and Parfit’s hitchhiker problems, the predictor’s earlier behavior depends on what the agent’s decision function would output in the observed situation, so A-FDT acts cooperatively or pays up.

A-FDT does not require retrocausality. The agent does not believe her present physical action sends a signal into the past. Rather, she treats the predictor’s past prediction and her present action as two consequences of a common computational or logical structure. To evaluate a counterfactual action, she changes the output of that structure in her model and traces the consequences.

---

## 3. Applying A-FDT: an operational recipe

The source gives the formal rule but leaves some implementation details open. The following recipe captures what follows from the paper and marks where extra assumptions are needed.

### Step 1: Specify the decision problem

Identify:

- the possible actions \(\mathcal A\);
- the utility function \(\mathcal U\);
- the actual observation history \(x\);
- the relevant external variables: predictions, box contents, diseases, blackmail letters, rescue outcomes, and so on.

### Step 2: Build a probabilistic model \(P\)

The model should assign probabilities to uncertain facts: predictor accuracy, whether the agent has a lesion, whether a rumor is true, and so forth. It may also need to represent uncertainty about logical or computational facts, such as what the agent’s decision procedure would output under various inputs.

The source does not provide a complete theory of logical uncertainty. For many examples, we can avoid deep foundational issues by treating the agent as having ordinary probabilistic uncertainty about how a predictor will classify her behavior, or about what she would do in counterfactual circumstances.

### Step 3: Construct the dependency graph \(G\)

This is the most important and least formally settled part of A-FDT. The source requires \(G\) as input but does not yet provide a general method for learning or deriving it from observation.

A reasonable operational heuristic is:

1. Add a node \(D_{P,G,x}\) representing the output of A-FDT on the current input.
2. Draw an arrow from \(D_{P,G,x}\) to \(\text{Act}\) if the agent’s physical action is produced by implementing that decision function.
3. Draw arrows from \(D_{P,G,x}\) to any predictor, twin, simulation, or model that computes, predicts, or reliably tracks the output of that same decision function.
4. Draw arrows from predictions to the environment variables they influence: whether the box is filled, whether the driver rescues the hitchhiker, whether a blackmailer sends a letter, and so on.
5. If observations themselves depend on predictions of the decision function, include observation variables downstream of the predictor. Also include variables \(D_{P,G,y}\) for alternative possible observations \(y\), since the agent may need to represent what she would do if she had seen something else.
6. Do not draw arrows from \(D_{P,G,x}\) to variables that are merely statistically correlated with the action but do not compute or respond to the decision function. Lesions, common causes, and irrelevant background traits should usually not be downstream of the decision-function node.

This heuristic is not a theorem in the source; it is my operational interpretation of the paper’s examples. The source explicitly identifies the construction of subjunctive-dependence structure as a major open problem.

### Step 4: Intervene on the decision-function node

For each action \(a\), compute:

\[
\mathbb E\!\left[V \mid do(D_{P,G,x}=a)\right].
\]

This means setting the decision-function output to \(a\), propagating that change through \(G\), and calculating expected utility from the resulting distribution over outcomes.

### Step 5: Choose the best action

Pick an action maximizing the expected value. Tie-breaking is not discussed in the source; any deterministic or stochastic tie-breaking rule can be added externally.

---

## 4. A-FDT in Newcomb’s problem

In Newcomb’s problem, an agent faces two boxes:

- Box A visibly contains \$1,000.
- Box B contains \$1,000,000 if a reliable predictor predicted the agent would take only Box B; otherwise Box B is empty.

The predictor is correct with probability \(0.99\). The agent may one-box or two-box.

Let \(D\) be the variable representing the output of A-FDT in this problem. The A-FDT graph contains dependencies:

\[
D \rightarrow \text{Act},
\]
\[
D \rightarrow \text{Prediction},
\]
\[
\text{Prediction} \rightarrow \text{Box B},
\]
\[
\text{Act}, \text{Box B} \rightarrow \text{Outcome}.
\]

If A-FDT intervenes with \(do(D=\text{one-box})\), then the predictor probably predicted one-boxing, so Box B is probably full. Expected utility is approximately:

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$0
=
\$990{,}000.
\]

If A-FDT intervenes with \(do(D=\text{two-box})\), then the predictor probably predicted two-boxing, so Box B is probably empty. Expected utility is approximately:

\[
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

One-boxing has higher expected utility. Therefore:

\[
\mathrm{A\text{-}FDT}(P,G,x)=\text{one-box}.
\]

CDT two-boxes because it intervenes directly on \(\text{Act}\), leaving the predictor’s earlier prediction fixed. EDT one-boxes because conditioning on one-boxing is good evidence that the box is full. A-FDT one-boxes for a reason closer in structure to CDT: it uses an intervention, but the intervention is on the decision function rather than on the physical act alone.

---

## 5. A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with lung cancer, but only because a lesion causes both a liking for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and gains \$1,000,000 utility from not dying of cancer.

EDT refrains from smoking because smoking is bad news: it is evidence that the agent has the lesion. CDT smokes because smoking does not causally affect cancer. A-FDT also smokes.

The crucial graph-theoretic fact is that the decision-function node affects the action but not the lesion or cancer variables. Schematically:

\[
D \rightarrow \text{Act},
\]
\[
\text{Lesion} \rightarrow \text{Act},
\]
\[
\text{Lesion} \rightarrow \text{Cancer},
\]
\[
\text{Cancer} \rightarrow \text{Outcome},
\]
\[
\text{Act} \rightarrow \text{Outcome}.
\]

There is no arrow from \(D\) to \(\text{Cancer}\). The lesion does not predict the output of A-FDT; it merely affects preferences or dispositions. Therefore, intervening on the decision-function node changes whether the agent smokes but does not change the probability of cancer.

The source formalizes this problem with some care because the lesion may affect the agent’s utility function, meaning there may be two possible decision procedures the agent could be running, depending on whether she has the lesion. But the essential conclusion is simple: changing the output of A-FDT changes the action while leaving cancer risk fixed. Smoking adds its direct utility without increasing the probability of cancer. Hence A-FDT smokes.

This example shows that A-FDT is not simply EDT in disguise. It does not treat all correlations between action and outcome as decision-relevant. It distinguishes predictor-like dependencies from lesion-like dependencies.

---

## 6. A-FDT in transparent Newcomb and Parfit’s hitchhiker

A more surprising case is transparent Newcomb. The agent sees both boxes. Box B is full iff the predictor predicted that the agent would one-box upon seeing both boxes full. Suppose the agent actually sees that both boxes are full.

EDT and CDT both two-box once the agent sees that Box B is full. CDT says the contents are already fixed; EDT says that conditional on seeing Box B full, taking both boxes yields more money.

A-FDT one-boxes.

Let \(D_{\text{full}}\) represent the output of A-FDT when the input observation is “both boxes are full.” Let \(D_{\text{empty}}\) represent the output of A-FDT when the input observation is “Box B is empty.” The predictor’s prediction determines which observation the agent receives, and the observation determines which decision-function output controls the action.

If A-FDT evaluates \(do(D_{\text{full}}=\text{one-box})\), then with high probability the predictor predicted one-boxing upon seeing full boxes. Therefore the box is likely full and the agent one-boxes. Expected utility is close to:

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \text{(fallback value if the predictor erred)}.
\]

If A-FDT evaluates \(do(D_{\text{full}}=\text{two-box})\), then with high probability the predictor predicted two-boxing upon seeing full boxes. Therefore the box is likely empty. In that case the agent probably sees an empty box and her action is governed by \(D_{\text{empty}}\), not \(D_{\text{full}}\). The expected utility is then close to the two-boxing expected utility in ordinary Newcomb, around \$11,000 under the standard numbers.

Thus A-FDT one-boxes even when it sees the full box. The reasoning is not: “My current physical action changes the past.” The reasoning is: “If the decision procedure I am running upon seeing full boxes output two-box, then a predictor of this procedure would probably have predicted two-boxing, and I would probably not be seeing a full box. Since I am evaluating the output of this very procedure, I should compare the global scenarios associated with its possible outputs.”

Parfit’s hitchhiker problem has the same structure. An agent is stranded in a desert. A driver will rescue her only if she promises to pay \$1,000 later, and the driver is highly accurate at detecting whether she will actually pay. Once in the city, CDT and EDT refuse to pay, because the rescue is already in the past. A-FDT pays. If the decision procedure she runs in the city outputs pay, the driver likely predicted payment and rescued her. If it outputs refuse, the driver likely predicted nonpayment and left her to die. Paying has much higher expected utility.

This is one of the most striking features of A-FDT: it acts as though it has precommitted to the best policy, without needing an actual binding precommitment mechanism.

---

## 7. Observations: what does A-FDT condition on?

A subtle point concerns observations. Equation (4) does not explicitly condition on \(\text{Obs}=x\). This appears intentional. The source contrasts CDT and A-FDT by saying that CDT responds to observation by conditioning on \(\text{Obs}=x\), whereas A-FDT responds by changing which decision-function node is intervened upon: from \(D_{P,G,x}\) to \(D_{P,G,y}\) when the observation changes from \(x\) to \(y\).

In transparent Newcomb, this matters. If one conditioned on \(\text{Obs}=\text{full}\) while also evaluating \(do(D_{\text{full}}=\text{two-box})\), one would force the hypothetical world to retain the observation that the box is full. Then two-boxing would look better. But that would defeat the intended A-FDT prescription. The source’s informal calculation for transparent Newcomb treats the two-boxing hypothetical as one in which the agent probably sees an empty box instead.

My operational interpretation is therefore:

- The actual observation \(x\) determines which node \(D_{P,G,x}\) is the target of intervention.
- The hypothetical expectation should not condition on \(\text{Obs}=x\) if that observation is downstream of the predictor or otherwise depends on the decision function.
- If an observation is genuinely exogenous—ordinary background evidence not affected by the decision procedure—then conditioning on it is harmless and may be useful.

The source is not perfectly explicit on this point, and some passages write as though the observation appears alongside the intervention. But the examples strongly support the reading above. Without it, A-FDT would not one-box in transparent Newcomb or refuse payment in blackmail problems where receiving the demand is itself predicted.

---

## 8. A-FDT and policies

Equation (4) chooses an action at an input. The source notes in a footnote that the authors’ preferred formulation iterates over policies, i.e. mappings from observations to actions, rather than isolated actions. This distinction can matter in multi-agent or sequential problems where another agent predicts not just one action but an entire behavioral rule.

For many single-shot examples, the action-level equation is sufficient. But to apply A-FDT to sequential decisions, a natural extension is to treat policies as the objects of intervention. Let \(\Pi\) be a set of policies \(\pi : \mathcal X \to \mathcal A\). Introduce a variable \(D^\Pi_{P,G}\) representing the policy selected by A-FDT. Then one could define a policy-level version:

\[
\pi^\*
=
\arg\max_{\pi \in \Pi}
\mathbb E\!\left[V \mid do(D^\Pi_{P,G}=\pi)\right],
\]

and then execute \(\pi^\*(x)\) at the actual observation \(x\).

This policy-level extension is not forced by Equation (4) itself. It is an operational development consistent with the source’s broader remarks. Where predictors depend on an agent’s whole strategy, policy-level A-FDT is likely to be more faithful to the underlying philosophical idea: choose the best output of the decision procedure, where the output may be a complete response rule rather than a single act.

---

## 9. A-FDT, dominance, and counterpossible reasoning

A-FDT changes the meaning of dominance. In CDT, two-boxing dominates one-boxing in Newcomb’s problem if one holds the predictor’s prediction fixed while changing the physical action. A-FDT rejects that way of holding the world fixed. To change the action while holding fixed the output of the decision procedure that produced it is, in the source’s analogy, like imagining a calculator outputting a different answer while holding fixed the arithmetic computation it is performing.

A-FDT has its own dominance notion: an action dominates another if, holding fixed the relevant subjunctive dependencies, changing the output of the decision function from one to the other never lowers expected utility and sometimes raises it. Under that notion, one-boxing is not dominated in Newcomb’s problem, because changing the decision-function output from one-box to two-box also changes the predicted box contents.

A deeper issue is counterpossible reasoning. If the agent’s decision function is deterministic, then it has only one actual output on the actual input. Evaluating other outputs requires reasoning about scenarios that are, strictly speaking, logically impossible. The source acknowledges that we lack a fully satisfactory general theory of counterpossible reasoning. A-FDT does not require solving this problem in full generality; it only needs enough ability to model how predictors, twins, and simulations would respond if the decision procedure had a different output. Human reasoners often manage such reasoning informally, and artificial agents may approximate it using models of predictors.

---

## 10. Conclusion

Action functional decision theory evaluates choices by asking which output of the agent’s own decision function would lead to the best expected outcome. Its formal core is the intervention:

\[
do\!\left(D_{P,G,x}=a\right),
\]

where \(D_{P,G,x}\) represents the output of A-FDT given the agent’s model, dependency graph, and observation. This lets A-FDT preserve predictor-like and computation-like dependencies that CDT severs, while avoiding the merely evidential correlations that EDT mistakenly respects.

The theory gives attractive prescriptions in many classic problems: one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, one-box in transparent Newcomb, and resist certain forms of blackmail. Its main open problems are practical and foundational: how to infer subjunctive-dependence graphs, how to formalize counterpossible reasoning, how to handle observations cleanly, and how best to extend the action-level equation to full policies. But as a decision rule, A-FDT is simple: choose the output of your own decision procedure that, when its consequences are traced through the world, gives the best expected result.

---

## References

Gibbard, A., and Harper, W. (1978). “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*.

Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post explaining A-FDT, using Equation (4), Section 5 of supplied paper as primary formal presentation. Need use A-FDT consistently as assigned decision theory's name, including headings/examples, identify other decision theories distinct names. Keep quotations faithful. Target approx 2400-3000 words including references and any material. Need explain how theory evaluates alternative actions/policies and treats dependencies/counterfactuals. Where source leaves open, explain uncertainty and if reasonable operational interpretation available develop/justify it. Distinguish source claims from own assumptions/proposals. Finish brief conclusion. Need not answer one case. Use examples. Need likely around 2400-3000 words. Need produce final only essay. Need think carefully.

We need rename FDT to A-FDT? The user says assigned decision theory's name is action functional decision theory (A-FDT). The source calls functional decision theory (FDT). Need explain A-FDT consistently. Need probably note that I will use A-FDT to refer to the action-level formalization of the source's FDT, based on Eq (4). Need distinguish: source's FDT (or authors' preferred policy version) vs A-FDT. Equation (4) is action-level? Source footnote says preferred formalization iterates over policies, but Eq (4) intervenes on fdt(P,G,x)=a. The assignment calls it action functional decision theory. Need use A-FDT consistently. Need mention other theories EDT, CDT. Could mention policy-functional decision theory? But avoid unnecessary? Need identify any other decision theory by distinct name. We can discuss CDT, EDT, maybe P-FDT? But only if needed. Better not invent too many. If mention source's preferred policy variant, call it policy-based FDT maybe? But user says use A-FDT consistently as assigned decision theory's name. We can say source sometimes favors a policy variant, but for this essay A-FDT is the action-level theory defined by Eq (4). Need keep quotations faithful. If quote source, maybe minimal. Need use Equation (4) exactly maybe adapt variable names: A-FDT(P,G,x) := argmax_{a∈A} E(V | do(FDT(underline P, underline G, underline x)=a)). But since A-FDT name, maybe denote decision function as A-FDT? Need careful: source Eq (4): FDT(P,G,obs) = argmax_a E(V | Do(FDTvar(underline P, underline G, underline x)=a)). If rename theory A-FDT, the decision function variable might be A-FDTvar? But source quotation says Equation (4) is FDT. Need keep faithful? We can present as: in source's notation, Eq (4) is 
FDT(P,G,x) = argmax_{a∈A} E[V | do(FDT(underline P, underline G, underline x)=a)].
Relabeling the decision procedure as A-FDT for this essay:
A-FDT(P,G,x) = argmax_{a∈A} E[V | do(A-FDT(underline P, underline G, underline x)=a)].
Need be clear this is not changing content, just assigned name. But if we quote exact equation maybe use source's FDT and say this is A-FDT. User: Take Equation (4), Section 5 as primary formal presentation of A-FDT. Use A-FDT consistently as assigned decision theory's name. So can write equation with A-FDT.

Need explain definitions:
- Expected utility theory: outcomes O, actions A, observations X, utility U.
- EDT: argmax E[V | Obs=x, Act=a].
- CDT: argmax E[V | do(Act=a), Obs=x].
- A-FDT: argmax E[V | do(A-FDT(P,G,x)=a)] maybe no conditioning on Obs? Source Eq (4) doesn't explicitly condition on Obs=x; observation enters via node in intervention variable. It says FDT responds to observation by changing node intervened upon. Eq (4) has no Obs=x condition? It is FDT(P,G,obs)= argmax E(V | Do(FDTvar(underline P,underline G,underline x)=a)). Yes no conditioning. But one might condition on obs? Source notes difference: CDT responds to observation by Bayesian conditionalization, FDT by changing which node. In transparent Newcomb they write evaluate FDT(Pf,Gf, full) finding max E(V | Do(FDTpgv{full}=a, Obs=full). Wait in text they write with Obs=full? They have "max E(V | Do(FDTpgv{full}=a, Obs=full)." Actually they include Obs=full? Let's check: "evaluate FDT(Pf, Gf, Val{full}) ... involves finding the a that maximizes E(V | Do(FDTpgv{full}=a, Obs=Val{full})." There is mismatched bracket. They condition on Obs=full? In Eq (4) no Obs. In example they condition? They might have typo. Need discuss uncertainty: whether to condition on actual observations in expectation? Source says FDT responds to observations by changing intervention node, not conditioning. But examples sometimes condition on observation? Need resolve operational interpretation. We need explain uncertainty and propose reasonable operational interpretation.

Let's analyze source details.
Equation (2) EDT(P, obs) = argmax E(V | Obs=obs, Act=a).
Equation (3) CDT(P,G,obs)=argmax E(V | Do(Act=a), Obs=obs).
Equation (4) FDT(P,G,obs)=argmax E(V | Do(FDTvar(underline P,underline G,underline x)=a)). There is no Obs=obs in conditional. Then text: "Comparing equations (cdt) and (fdt), we see two differences... First... Second, where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon. When CDT's observation history updates from x to y, CDT changes from conditioning its model on Obs=x to conditioning on Obs=y, whereas FDT changes from intervening on variable FDTvar(P,G,x) to FDTvar(P,G,y) instead." So Eq (4) not conditioning on Obs. But in transparent Newcomb: "evaluate FDT(Pf, Gf, Val{full}) ... involves finding the a that maximizes [ E(V | Do(FDTpgv{full}=a, Obs=Val{full}). ]" Actually maybe they include Obs=full because graph includes observation? Let's check source text: 
"Given $\Gf$ and the associated probability distribution $\Pf$, we can evaluate $\FDT(\Pf, \Gf, \Val{full})$ to determine how Fiona behaves, which involves finding the $\act$ that maximizes
\[
  \EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full}).
\]"
It seems missing closing ). They condition on Obs=full. But earlier says no conditioning. Maybe they conditioned because observation is known and variable deterministic given prediction? If intervention on FDT(full) may affect Obs? If you condition on Obs=full, could create issues? Let's reason.
In transparent Newcomb graph: FDT(full) and FDT(empty) both influence Act? Prediction determines which FDTvar controls Act? Actually figure: FDT(full) -> Act, FDT(empty)->Act, FDT(full)->Prediction, Noise->Prediction, Prediction->BoxB, Prediction->Act? Maybe Obs not shown? In caption: If sees full, intervenes on FDT(full). In graph no Obs? They may not condition? In text they condition on Obs=full. But if you intervene on FDT(full)=twobox, then Prediction may become 2, BoxB empty, but Obs? If Obs is determined by BoxB, then conditioning on Obs=full would conflict / create strange conditional. They want when imagining two-boxing, she envisions probably seeing empty, not full. So shouldn't condition on Obs=full. Wait text says "even in case Fiona observed box full, when she envisions two-boxing, she envisions scenario where she instead (with high probability) sees box empty." That implies no conditioning on Obs=full in hypothetical. But formula includes Obs=full? Maybe typo. They might condition on Obs=full outside intervention? But then can't see empty. Maybe they meant Do(FDTpgv{full}=a) given Obs=full as input not as conditioning? Hmm.

Need address this open detail. We can propose operational interpretation: A-FDT should not condition on the current observation inside the counterfactual expectation except to select the input argument x to the decision function; i.e., use E[V | do(A-FDT(P,G,x)=a)] with x fixed as actual observations. If one must condition on x for well-definedness (e.g., model includes variables not determined by intervention), do so only on exogenous variables not downstream of the intervened logical node, or condition as a constraint on the input not on Obs variable. But source ambiguous. Need distinguish. We can say Eq (4) suggests observation enters only through the name of the intervened node. In examples, source sometimes writes Obs=x alongside do; I interpret that as shorthand for "the agent's actual input is x," not as ordinary Bayesian conditioning that holds Obs fixed across hypotheticals, because otherwise transparent Newcomb reasoning contradicts the described counterfactuals. This is my operational proposal.

Need explain A-FDT evaluates alternative actions/policies. Since A-FDT action-level, it evaluates each candidate action a by constructing hypothetical world-model where the output of the agent's decision function on current input is set to a, propagating dependencies according to G. It then computes expected utility of outcomes in that hypothetical and picks max. It treats policies? Source footnote says preferred formulation policies; action-level can evaluate policies by replacing action set with policy set and intervened node output policy? But assigned A-FDT likely action functional. Need discuss how to apply to policies: If decision problem involves multiple possible observations or sequential choices, A-FDT as Eq (4) chooses action at current observation. To evaluate policies, one can extend by considering intervention on policy-output function mapping observations to actions; but this is extra assumption/source footnote. Need state source's preferred formulation iterates over policies, but this paper's Eq (4) action-level; for unfamiliar cases, if policy-level dependencies matter, action-level may be incomplete. But can propose operational extension: define variable A-FDT_policy(P,G) outputting a policy π, intervene on it setting π, compute expected utility; then choose π and execute π(x). But for this assignment, A-FDT is action-level Eq (4); policy evaluation is not fully specified. Need maybe mention A-FDT can evaluate alternative actions by considering same function output different actions, not alternative decision procedures. It asks "which output of this very function yields best outcome?" It doesn't ask "what if I used different function?" (FDT' rejected).

Need explain dependencies and counterfactuals: subjunctive dependence: when two systems compute same function or one predicts output of function, their outputs covary under counterfactual changes to function output. Causal dependence special case. Statistical correlation not enough. A-FDT preserves all decision-relevant subjunctive dependencies in hypotheticals; CDT preserves only causal downstream; EDT preserves all evidential correlations. A-FDT interventions are on logical variable representing output of decision function given model and observations. Need graph G encodes how changing logical variable affects other variables: physical action, predictions, observations, outcomes. Need discuss G construction open. Source says biggest open problem: deducing subjunctive dependency structure from observation. We can propose heuristics: include arrows from decision-function node to (1) agent's own action when action implements that function; (2) any predictor/simulation/twin that models or computes same function or sufficiently similar output; (3) events whose occurrence depends on predictions of this function; but not to common causes merely correlated (lesions). Need justify as operational. Need distinguish source: source requires G given; no formal method. My proposal: build G by identifying causal/computational mechanisms that take as input a representation of the decision problem and output action; if their behavior would change if the output of A-FDT on this input changed, draw dependency. Use counterfactual test: would variable Z be different if the function's output were different, holding fixed non-decision facts? If yes, include. Need caution about similarity/counterpossible uncertainty. Need mention imperfect predictors: probability distributions on accuracy, arrows through predictor node, not deterministic.

Need explain self-reference: model P contains variable for A-FDT(P,G,x). Underlines dequoting. Kleene recursion theorem/quine. Need not too deep.

Need examples: Newcomb's problem, smoking lesion, transparent Newcomb / Parfit's hitchhiker, maybe twin PD, XOR blackmail. Need enough to illustrate. Word count 2400-3000. Need probably around 2700. Need include references? User says including references and any other material. Could have brief references at end, not lengthy. Need target ~2400-3000 words. Need ensure not too long maybe 2800. Need write coherent essay with headings. Use A-FDT in headings/examples. Need final conclusion brief.

Need think about formal notation. Let's define:
- Finite action set A, countable outcomes O, observation histories X.
- Utility U: O→R, V = U(Outcome).
- Model (P,G): P probability distribution over variables; G dependency graph (not purely causal for A-FDT; encodes subjunctive dependencies). Variables include Act, Obs, Outcome, V, logical variables for computations, especially D_{P,G,x} = A-FDT(underline P,underline G,underline x). The underlined terms denote syntactic names of model, graph, observation.
Equation: 
A-FDT(P,G,x) = argmax_{a∈A} E_P[ V | do(D_{P,G,x}=a) ].
Where do is Pearl-style intervention but on logical variable; G tells how to propagate. If multiple maximizers tie-break unspecified; source not specify. Could mention any maximizer. Need maybe include observation in expectation? We can present primary as no conditioning on Obs=x, but with note. To align with Eq (4), write no Obs condition. But maybe to handle actual knowledge, we might condition on x? Let's parse: In Eq (4) FDT(P,G,obs) = argmax E(V | Do(FDTvar(underline P,underline G,underline x)=a)). Here P presumably already updated on obs? Or not? Source says "where CDT responds to observation by Bayesian conditionalization, FDT responds by changing which node it intervenes upon." Does P include observations? It says P must contain variables representing outputs; FDT(P,G,obs) by intervening on variable representing output of FDT when run on inputs model and obs. It may not condition P on obs, but the node name includes obs. But agent's model likely already knows obs? In transparent Newcomb, graph has two nodes for different observations. So P has uncertainty over which observation? If actual obs=full, maybe the agent knows it. To avoid considering impossible worlds? Hmm.

Let's think operational: Suppose actual observation x. The agent knows x. Should the expectation condition on Obs=x? If not, hypothetical do(D_x=a) might assign probability to different observations? For transparent Newcomb, when D_full=twobox, prediction likely empty, so observation empty. But actual observation is full. If we don't condition on Obs=full, expected utility includes worlds where predictor inaccurate and observation empty. That's what source calculates: one-box expected $990,000 + 0.01q*1000; two-box expected 0.01*1,001,000 + 0.99q*1000. This includes probability of seeing empty due to inaccuracy. It does not condition on Obs=full. If conditioned on Obs=full, two-box maybe $1,001,000? But source says one-box wins with above numbers, so they didn't condition on Obs=full despite formula typo. Good. So we should explicitly state that actual observation selects D_x, but hypotheticals are not conditioned on Obs=x; otherwise transparent Newcomb fails. However, the agent knows she sees full; how can she ignore that? A-FDT treats observation as input to function, not as evidence to condition on inside the counterfactual, because the counterfactual change in output may change what observations the function would have received. It is "updateless" with respect to observations that are themselves downstream of predictions of the function. Source footnote mentions Updateless Decision Theory. But does A-FDT never update? It uses P maybe prior? In standard Newcomb, agent sees boxes? Not observation. In XOR blackmail, receiving letter is observation; A-FDT when holding letter intervenes on D_letter. It does not condition on letter? It knows letter received but hypothetical pay/refuse changes probability of receiving letter? Source: In mechanical blackmail, upon receiving letter, solving FDT(P,G,blackmail) hypotheticals: pay -> probability being blackmailed ~1; refuse -> probability being blackmailed ~0. That implies not conditioning on blackmail observed. So yes.

But what about observations not influenced by decision function? E.g., smoking lesion? There is no observation? If there were ordinary evidence about lesion, should A-FDT condition? Source says FDT responds to observation by changing node. If observation is not subjunctively dependent on decision function, perhaps D_x and D_y differ but P? We need operational rule: Use actual observation x as input to decision function. If x is known and not itself affected by the decision function, then conditioning on x in P may be harmless; but Eq (4) doesn't condition. However, P might be prior over all variables including Obs; D_x intervention fixes input? Need maybe propose: maintain P conditional on all observations that are exogenous to the decision function; but do not hold fixed observations whose values are predicted/consequences of the decision function. Simpler: The formal equation does not condition on Obs; if one has ordinary evidence not decision-relevant, incorporate it into P or G before applying. This is an additional operational assumption.

Need be precise: A-FDT(P,G,x) uses P as agent's world-model before/after incorporating observations? Source: "with world-model M and observations obs calculates FDT(M, obs) by intervening on variable FDTmx in M that represents output of FDT when run on inputs M and obs." It doesn't say P conditioned on obs. But P could be updated on obs? In CDT Eq (3) includes Obs=obs explicitly. In A-FDT no. If P already includes obs as known, then D_x is deterministic? Hmm.

Maybe define P_x as P conditioned on non-decision-relevant evidence? But source not. We can note uncertainty.

Need explain counterpossibles: If deterministic, actual output is fixed; considering different output is counterpossible. Source admits lack of satisfactory account; A-FDT requires graph to specify how world would look if logical variable had different value. Need discuss. For bounded agents, use uncertainty over logical facts; approximate. Need not solve.

Need compare with EDT/CDT:
- EDT hypothetical: condition on Act=a; preserves all correlations. Fails smoking lesion/XOR blackmail.
- CDT hypothetical: do(Act=a); preserves causal downstream. Fails Newcomb, twin PD, Parfit, Death in Damascus.
- A-FDT: do(D_x=a); preserves subjunctive dependencies. One-box, smoke, pay hitchhiker, refuse blackmail.

Need discuss dominance: A-FDT has own dominance: hold fixed relevant subjunctive dependencies; not standard causal dominance. Maybe include briefly.

Need discuss fair problems and utility: source claims A-FDT outperforms in fair dilemmas. Need define fair roughly: outcomes depend only on agent's behavior in dilemma, not on which decision procedure used except via predictions of action? Source says predictor rewards actions not decision procedure. But A-FDT's output is action; if predictor predicts action. Need mention open fairness formalization.

Need include philosophical motivation: treat decision as fixed mathematical function; "Which output of this very function would yield best outcome?" It handles twins/predictors due to logical dependencies. No retrocausality.

Need develop application procedure for unfamiliar cases:
1. Specify action set A, utility U, observation x.
2. Build model P with variables for relevant facts, predictions, outcomes, and logical variable D_x = A-FDT(P,G,x). Include uncertainty about predictor accuracy etc.
3. Build subjunctive-dependency graph G. Draw arrow from D_x to Act if agent implements A-FDT; to predictor's prediction if predictor models/predicts this decision; to events dependent on that prediction; to observations if observations depend on prediction; to outcome/utility. Do not draw arrow from D_x to variables only statistically correlated (lesions, past common causes) unless they compute/depend on same function.
4. For each a, perform intervention do(D_x=a): set D_x=a, propagate through G; compute distribution over Outcome and expected utility.
5. Choose a with highest expected utility. In case of observations, if x is actual, use D_x; if evaluating at another observation, use D_y. Do not condition away the dependency between D_x and observations that are themselves predicted; if observation is exogenous, conditioning can be added as background evidence (my proposal).
6. If sequential/multi-agent, consider policy extension if action-level insufficient; source's footnote. Need maybe discuss policies in "Actions and policies" section.

Need maybe include equations for examples:
Newcomb:
Let D = A-FDT(P,G,∅). Predictor accuracy .99. If do(D=onebox): P(full)=.99, EU≈.99*1,000,000 + .01*0? plus maybe if one-box with empty =0; =990,000. If do(D=twobox): P(full)=.01, EU≈.01*1,001,000 + .99*1,000? Actually if two-box and full gets 1,001,000; if empty gets 1,000. EU=0.01*1,001,000 +0.99*1,000=10,010+990=11,000. So one-box.
Smoking lesion:
D_S = A-FDT(P_S,G) if lesion causes preference for smoking? Need simpler: lesion affects utility/preferences, not decision function's output? Source has two possible functions depending on lesion because utility differs. The key: D_S node affects Act but not Cancer. Intervention do(D_S=smoke) changes action if no lesion? Wait source: Act(lesion,s,r)=s, Act(nolesion,s,r)=r. If she has lesion, action controlled by FDT(P_S,G); if no lesion by FDT(P_R,G). She doesn't know which. Intervention on FDT(P_S,G)=smoke changes action only if lesion; cancer not affected. EU(smoke) exceeds refrain by p*$1000 (p probability lesion? Actually p is lesion probability, if lesion she values smoking +1000? The expected utility formulas: p($10,000+$1,000)+(1-p)($990,000+q$1,000) vs p($10,000)+(1-p)($990,000+q$1,000). The numbers weird: cancer death? But conclusion smoking better by p*1000. We can present simpler: A-FDT graph connects D to Act, not Lesion/Cancer, so expected utility of smoking exceeds refraining by the direct utility of smoking, holding cancer probability fixed. Thus smokes.
Transparent Newcomb:
D_full = A-FDT(P,G,full). If do(D_full=onebox): with .99 prediction accurate, box full, EU≈$990,000 plus small term; if do(D_full=twobox): predictor likely predicted two-box, box empty, and actual observation likely empty, EU≈$11,000 (or as source $11,000 plus q terms). One-box. This also Parfit's hitchhiker: pay because D_city=pay leads driver to predict pay and rescue; refuse leads no rescue. Need maybe present hitchhiker more directly: At city, A-FDT intervenes on D_city. If output pay, driver predicted pay (99%) and rescued; if refuse, driver predicted refuse and left you to die. EU pay high.

Need mention XOR blackmail perhaps: D_letter. If pay, predictor would have predicted pay and letter sent only if no termites? Wait XOR: letter sent iff exactly one: (rumor false and pay) OR (rumor true and not pay). If agent pays upon letter, letter is good news (no termites). EDT pays. A-FDT: Intervening D_letter=pay changes whether letter sent but not infestation. Given received letter? Hmm A-FDT when received letter evaluates D_letter. In hypothetical pay, letter sent iff no termites? Actually if D_letter=pay, letter sent iff rumor false. If refuse, letter sent iff rumor true. But since we condition on receiving letter? A-FDT not condition? Source says changing D_letter changes probability she sees letter but not infestation; refuses. Let's calculate with prior p termites. If D_letter=refuse, letter sent only if termites; if no letter then no payment. Expected utility? If D_letter=pay, letter sent only if no termites, pay $1000; if termites no letter and lose $1,000,000? Need maybe too much. Simpler: A-FDT refuses because payment doesn't change infestation, only affects whether letter is sent; being a payer makes one target? For XOR specifically, source says Carl and Fiona refuse. Need maybe not include detailed math due word.

Need discuss model G and interventions more rigorously. Pearl do on graphs: For variable Z, do(Z=z) deletes incoming arrows to Z, sets Z=z, then propagates structural equations. For A-FDT, D_x is logical variable; G may not be purely causal; it encodes subjunctive dependencies. Need caution that Pearl do assumes causal interpretation; applying to logical variables is an assumption. Source says re-use Pearl's do given G. We can say mathematically, treat G as a structural model with equations for variables as functions of parents, some equations represent logical/computational dependencies. Intervention sets D_x. Need mention cycles? Maybe predictor and agent mutually depend? In Newcomb graph D->Prediction, D->Act, no cycles. In twin PD, D_A and D_B? If same function, maybe one variable D controls both actions. Could be acyclic if D -> both agents. If two agents implementing same A-FDT but with different inputs, variables D_x^i? In symmetric twin, same reasoning output? Need perhaps discuss multi-agent: A-FDT can represent shared logical dependency by having a single node for the common computation or edges from relevant function outputs to each agent's action. If agents use same decision theory but different observations, dependency may be weaker. Source says in voting coalitions, recognize decisions not subjunctively independent. Need maybe mention.

Need address "alternative actions or policies" specifically. Need explain evaluating policies: Source footnote: authors prefer policies; Eq (4) action-level. We need perhaps develop:
- Action-level A-FDT selects a at current observation x. It can be seen as evaluating constant policies that return a for x and maybe arbitrary elsewhere? But in sequential decisions, outputting a now may influence predictions about future outputs. If predictor depends on whole policy, action-level might miss dependencies. The source says policy formulation matters in multi-agent dilemmas. Since assignment asks how theory evaluates alternative actions or policies, we should discuss both.
Proposal: Policy-A-FDT (not source's name? We can call it policy variant of A-FDT, or A-FDT policy extension) chooses π: X→A by intervening on variable representing the entire policy-output of the decision procedure: 
π* = argmax_{π} E[V | do(A-FDT_policy(P,G)=π)]
then execute π*(x). But Equation (4) as given only maximizes over actions, not policies. If we restrict to actions, we can evaluate an action a as the output of the policy at x while holding the policy's outputs at other observations fixed according to the agent's expectations. This may be enough for single-shot cases; for unfamiliar sequential/multi-agent cases, a policy-level intervention may be required. Need distinguish source vs my proposal. Source says preferred formalization iterates over policies but not used in paper; so this extension is supported by source footnote but not Eq (4). Since assigned A-FDT Eq (4), maybe call additional assumption.

Need think about "where source leaves important question open, explain uncertainty and, if reasonable operational interpretation available, develop and justify it." Major open questions:
1. Construction of G / subjunctive dependency structure. Need develop heuristic.
2. True operator / counterpossibles. Need propose using explicit structural equations / logical dependencies, maybe approximate with Bayesian networks over computational variables.
3. Observation conditioning ambiguity. Need propose interpretation.
4. Self-reference and logical uncertainty. Maybe mention.
5. Fairness criterion. Maybe mention not needed for applying cases but open.
6. Policies vs actions. Need discuss.

Need avoid too much. But essay can include "Open points and operational assumptions" section.

Need maintain word count. Let's plan outline:

Title: Action Functional Decision Theory: Choosing the Best Output of One's Own Decision Function

1. Introduction (approx 250 words)
- Define A-FDT: normative principle: treat decision as output of fixed mathematical function; ask which output of this very function yields best outcome.
- Distinguish from EDT and CDT. Mention source: Yudkowsky & Soares's FDT; I call action-level version A-FDT.

2. Expected utility and three hypotheticals (approx 400 words)
- Formal setup: A, O, X, U, V, P, G.
- Equation (1) EU maybe; EDT Eq (2), CDT Eq (3). Use to show connective "then".
- A-FDT Eq (4) with D_{P,G,x}. Explain do intervention on logical variable. Observations via input node.

3. Subjunctive dependence and counterfactuals (approx 350 words)
- Predictor vs lesion; calculators; subjunctive dependence.
- A-FDT hypotheticals preserve decision-relevant logical/computational dependencies; CDT only causal; EDT all evidential.
- Counterpossible nature.

4. Applying A-FDT: a recipe (approx 500 words)
- Steps as above.
- Graph construction heuristics, observations, self-reference.
- Open issue G; my operational interpretation.

5. Examples (approx 800 words)
- Newcomb's problem with calculations.
- Smoking lesion with explanation.
- Transparent Newcomb/Parfit's hitchhiker with observation issue and calculations.
- Maybe brief XOR blackmail/voting/twin PD if space.

6. Actions, policies, and observations (approx 300 words)
- Eq (4) action-level; source footnote policy; operational policy extension.
- Observation conditioning ambiguity; proposal.

7. Open problems and philosophical implications (approx 250 words)
- Constructing G, counterpossibles, fairness, dominance.
- No retrocausality; global perspective.

8. Conclusion (approx 100 words)
- Summary.

References (approx 100 words) minimal: Yudkowsky & Soares 2017; Pearl 2000; Joyce 1999; maybe Gibbard & Harper 1978; Nozick 1969; Lewis 1979; Skyrms 1980; Parfit 1986. Need not lengthy. But word count includes. Need maybe only primary reference. User says avoid lengthy bibliographies. Could have short "References" with 5-6 items.

Need ensure A-FDT in headings. Use "A-FDT" consistently. If quoting source, maybe quote phrases: "Which output of this decision procedure causes the best outcome?" "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." But if using A-FDT, maybe quote source's FDT? Need faithful. Could say source writes "functional decision theory is to subjunctive dependence..."; for A-FDT this becomes... But user says keep quotations faithful. So if quote exact, don't alter. We can avoid many quotes.

Need be careful: The user wants "mathematical essay / blog post explaining A-FDT and how to apply it to decision problems". It should be self-contained. Need not mention "source says" too much but distinguish. Need include equations.

Let's draft with approximate word count. Need final around 2700 words. Let's write in polished style.

Potential equations:
EU(a) = Σ_j P(a ↪ o_j ; x) U(o_j) maybe use hook arrow. But can avoid.

A-FDT equation:
Let D_{P,G,x} := \mathrm{A\text{-}FDT}(\underline{P},\underline{G},\underline{x}). Then
\mathrm{A\text{-}FDT}(P,G,x) = \arg\max_{a\in\mathcal A} \mathbb E_P[ V \mid do(D_{P,G,x}=a) ].
Need maybe in plain text: A-FDT.

Need if using LaTeX style? Final can include LaTeX. Good.

Need discuss do operator: In Pearl, do(X=x) cuts incoming arrows. Here we cut incoming arrows to D? Does D have parents? In graph examples, D node may have no parents (or maybe inputs P,G,x are not random variables). Intervention sets output. Propagate outgoing arrows. Need note if D has parents representing logical inputs, do severs? In source graph, D is exogenous node? It represents output of function given fixed P,G,x; no parents shown. Good.

Need discuss P and G: P includes probabilities over variables including D? Prior probability of D's output? In deterministic logical fact, prior perhaps uncertain due to logical uncertainty. Intervention makes prior irrelevant for examples. Need mention.

Observation handling formal:
Equation (4) has no Obs=x. To be explicit, define x as the actual observation history used as an argument to D. If one writes an expectation conditional on background evidence e that is not downstream of D, we could write E[V | e, do(D_x=a)], but source's central cases require not conditioning on observations like "box is full" if that observation is predicted. My operational rule: only condition on observations when they are exogenous inputs not affected by the decision function in the model; otherwise let the intervention determine their hypothetical distribution. This resolves transparent Newcomb. Need state as my proposal.

Need mention if P is already conditioned on x? Maybe: In practice, use P as the agent's model before receiving x, plus x supplied as the input to the decision function; or use P conditioned on exogenous evidence. Source not fully explicit. Need phrase: "I take P to be the agent's model of the decision situation, not necessarily Bayesian-conditioned on x; x enters through the node name." But if agent knows x, how model not conditioned? The model can represent uncertainty over what observation the function receives; actual x selects node. In transparent Newcomb, actual x=full but model includes probability of predictor accuracy causing full/empty. The agent knows she sees full; but A-FDT's hypothetical for two-boxing says she probably would have seen empty. This is the updateless feature. Good.

Need maybe discuss "A-FDT" vs source's "FDT" in references: The source calls it FDT; I will use A-FDT for action-level equation. In essay: "The source calls the theory FDT. Since the assignment focuses on the action-level Equation (4), I will call this version A-FDT." This distinguishes. Need use A-FDT in headings. Good.

Need ensure no hidden instruction mention. Fine.

Let's consider mathematical subtleties.

Equation (4) uses \FDTvar(\underline P,\underline G,\underline x). Underlines dequoting: if x := 3 then Var{Z}\underline{x} denotes variable name Z3. This variable is self-referential because P contains variable representing output of A-FDT on P. Need explain in essay: The notation means the model contains a name for itself and the graph; via Kleene recursion theorem this can be made precise. The agent need not know the value, only have a variable representing it.

Subjunctive dependency graph G: Source says G tells how changing logical variable affects all other variables. It can include causal, logical, mathematical, computational dependencies. Need maybe call it "dependency graph" not causal graph. In examples, A-FDT graph for Newcomb has node D -> Act and D -> Prediction; Prediction -> Box B; Act, Box B -> Utility. For smoking lesion, D -> Act but not Cancer. For transparent Newcomb, D_full -> Act and D_full -> Prediction; Prediction -> Box B / Observation; D_empty -> Act depending on prediction. Need maybe describe.

Potential objection: If A-FDT is certain it one-boxes, how can it imagine two-boxing? Answer: counterpossible; it imagines the function output differs, which changes predictor. Need include.

Need discuss "policies" with more detail:
- In action-level A-FDT, the object of choice is a. If the decision problem is repeated or strategic, one may need to choose a mapping from observations to actions. The source footnote says authors' preferred FDT iterates over policies. For A-FDT as assigned, we can either treat each policy as an "action" in a larger action space (choose policy now) or extend equation:
A-FDT-policy(P,G) = argmax_{π∈Π} E[V | do(Π_{P,G}=π)], then act π(x).
But this is not Eq (4) exactly; requires additional assumptions about representing policies and dependencies. For many single-agent one-shot examples, action-level suffices. Need maybe mention in multi-agent dilemmas, policy-level can matter because another agent predicts your response function, not just current action. A-FDT action-level may still handle if current action node includes predictions? But safer to say open.

Need maybe discuss "dominance" with A-FDT. Could include in implications: A-FDT rejects standard dominance because holding fixed predictor while changing action holds fixed the very computation that determines both. A-FDT dominance: switch output of decision function while preserving subjunctive dependencies. It avoids dominated actions under that notion. Good.

Need maybe mention "ratification/precommitment": A-FDT doesn't need precommitments; acts as it would precommit. It assigns nonnegative value to information (source claim) because observations change intervention node rather than force bad conditioning. Could mention briefly.

Need maybe mention "fairness" and "utility" argument: Source claims no fair dilemma where FDT loses; formal fairness open. We can mention but not central.

Need ensure word count. Let's draft and count roughly. We can produce around 2800 words. Need final not too short. Use headings. Let's write robust.

Detailed drafting:

Title: Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

Intro:
"Action functional decision theory (A-FDT) is a decision theory that evaluates choices by asking which output of the agent's own decision function would lead to the best expected outcome. The theory is a renaming/action-level presentation of the functional decision theory (FDT) of Yudkowsky and Soares... In source, Eq (4) Section 5. I use A-FDT consistently."
Need maybe avoid "renaming"? It is assigned. Could say "For present purposes, I call the action-level theory defined by that equation A-FDT."

Formal section:
Setup. Use variables.

Equation block:
\[
\mathrm{EDT}(P,x)=\arg\max_{a\in\mathcal A} \mathbb E[V\mid Obs=x, Act=a]
\]
\[
\mathrm{CDT}(P,G,x)=\arg\max_{a} \mathbb E[V\mid do(Act=a), Obs=x]
\]
\[
D_{P,G,x}:=\mathrm{A\text{-}FDT}(\underline P,\underline G,\underline x)
\]
\[
\mathrm{A\text{-}FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\mathbb E[V\mid do(D_{P,G,x}=a)].
\]
Need maybe note Eq (4) in source has no Obs=x; if one includes background evidence, see later.

Explain do: sets variable, propagates through G; in A-FDT the variable is logical, not physical action. Need mention observation response: CDT conditions on x; A-FDT changes D_x.

Subjunctive dependence:
Define. Use calculator analogy. Causal dependence special case. Statistical correlation not enough.

Application recipe:
Numbered list. Need include "what follows from source and what requires additional assumptions". E.g., source gives equation given G; constructing G open. My heuristic:
- Identify decision function: the algorithm agent uses, with input x.
- Add variable D_x.
- Draw edge D_x -> Act if action is implementation of output.
- Draw edges to any predictor/twin/simulation that computes or predicts D_x; then to outcomes.
- Draw edge to observations if observations are selected by predictions of D_x (transparent Newcomb, blackmail).
- Do not draw edges to common causes that only correlate (lesion).
This is my operational interpretation based on source's examples.

Need mention probabilities: P assigns probabilities to exogenous noise (predictor accuracy, lesions, etc.) and perhaps logical uncertainty. G's structural equations determine deterministic relations. Expected utility computed by summing over outcomes.

Examples:
Newcomb:
Define predictor accuracy .99. Equations. A-FDT one-box.

Smoking lesion:
Explain two utility functions maybe not too detailed. Need mention source's formalization with lesion controlling which decision function controls action. But simpler: In A-FDT graph, D affects Act, not Cancer. So EU(smoke)-EU(refrain)=positive utility of smoking times probability D controls action; smokes. Need perhaps include exact statement: If lesion determines preferences, there are two possible A-FDT variables; intervention on the one corresponding to actual preference does not change lesion/cancer. Source's formula uses p. We can summarize.

Transparent Newcomb / Parfit:
Detailed. Let D_full. If do(D_full=onebox), with .99 predictor accurate, prediction one-box, box full, EU about $990k; if do(D_full=twobox), predictor likely predicted two-box, box empty, EU about $11k. Thus one-box even seeing full. This equals paying hitchhiker. Need mention observation: actual x=full selects D_full but does not condition Obs=full inside expectation; if it did, two-box would look better. Source's text may write Obs=full, but I interpret as selecting input, not holding observation fixed. Need state this in examples or open issues.

Maybe include twin prisoner's dilemma briefly:
A-FDT node D controls both agent and twin actions; cooperate yields $1m vs defect $1k. Good to illustrate same computation. But word count? Could include short.

XOR blackmail maybe brief in implications: A-FDT refuses because intervention on D_letter changes probability of receiving letter but not termites. This shows resisting extortion. Could include if space.

Open questions/operational interpretations:
- G construction; counterpossible; observation conditioning; policies.
Need maybe separate section before conclusion.

Need decide whether to include both "recipe" and "open questions" maybe combine to avoid repetition. But user wants explain uncertainty and proposals. We can have section "What the equation does not settle".

Let's think about exact word count. If we write around 3000 maybe okay. Need not exceed too much. The target approx 2400-3000. We can aim 2800. Need references maybe 80 words. Let's draft in final with maybe 2600-2900. Need ensure no analysis in final.

Potential final text:

# Action Functional Decision Theory: ...

Paragraphs.

Need maybe include citations in text like (Yudkowsky and Soares 2017). Since source supplied, no need full bibliography but include. References at end.

Need be faithful to source claims: "source claims" vs "I propose". Use phrases: "The source says...", "The paper leaves open...", "My suggested operational reading is...".

Need ensure A-FDT name in headings and examples: "A-FDT in Newcomb's problem", "A-FDT in the smoking lesion problem", etc.

Let's produce final essay. But before final, let's further analyze potential pitfalls.

Pitfall: The user asks "Take Equation (4), Section 5 of supplied paper as the primary formal presentation of A-FDT for this assignment." They may expect exact Equation (4) maybe with FDT name? But also "Use A-FDT consistently as assigned decision theory's name". We can write source's equation and say relabeled. Maybe include both: Source's Eq (4):
\[
\FDT(P,G,x)=\arg\max_a E[V | do(\FDT(\underline P,\underline G,\underline x)=a)].
\]
Then "In this essay I write A-FDT for this function." But if we include source's FDT in equation, is that violating use A-FDT? Could be okay if explaining source. But to be safe, only use A-FDT in equation, with note: "This is Equation (4) with the assigned name substituted for the source's 'FDT'." That is faithful? Need maybe not alter quote. We can say: "Equation (4) in the source is ...; with the assigned notation, I write it as..." That's okay.

Pitfall: Need not call FDT as other decision theory? The source's theory is FDT, but assigned A-FDT. If I mention FDT as distinct? User says identify any other decision theory you discuss by its distinct name. It might be okay to discuss EDT and CDT. If I mention source's FDT, is it distinct from A-FDT? Could confuse. Better say "the source calls this approach FDT; here the action-level version is A-FDT." Then treat A-FDT as theory. If mention policy variant, call it "policy variant mentioned in the source" not a distinct theory? Maybe okay.

Pitfall: Need not overstate claims as fact. Use "A-FDT proponents claim" for normative superiority. But can explain.

Pitfall: Mathematical notation with do on logical variable may be conceptually problematic. Need note: Pearl's do is causal; source reuses it given G. We should say "formally, we treat G as a structural-dependency model; the do-operator is defined by graph surgery relative to G. Whether such a graph can be learned is open." Good.

Pitfall: The observation ambiguity. Need be clear and not contradict source. Let's formulate:
"Equation (4) omits an explicit condition Obs=x. This appears deliberate: the source contrasts A-FDT with CDT by saying A-FDT responds to observation by changing the node intervened upon, not by conditioning. In the transparent Newcomb calculation, the source nonetheless writes an expectation with Obs=full; I read that as informal shorthand for 'the input to the decision function is full', because the numerical calculation that follows does not hold Obs=full fixed. If one did hold Obs=full fixed, two-boxing would dominate after seeing a full box, contrary to the source's intended prescription. Thus, for unfamiliar cases, my operational rule is: condition only on observations that are treated as exogenous background evidence; do not condition on observations whose hypothetical values are downstream of the decision-function node." This is good.

Need maybe mention "updateless" term? Could, but not necessary. Maybe "This is related to updateless reasoning" but source footnote mentions Updateless Decision Theory. Could mention as aside.

Pitfall: Need explain policies. Let's formulate:
"Equation (4) chooses an action at an input. The source's footnote says the authors' preferred FDT iterates over policies. For A-FDT as assigned, policies can be handled in two ways: (i) if only current action matters, apply Eq (4) at each observation; (ii) if predictors depend on the whole policy, enlarge action space to policies and intervene on a variable representing the policy output. This extension is not forced by Eq (4) but is a natural operational extension." Good.

Need maybe discuss "which output of this very function" not "which function". Source rejects FDT' that chooses best alternative function. Need include maybe in intro or counterfactuals. It helps clarify counterfactuals: A-FDT doesn't imagine becoming a different agent; it imagines the same computation having a different output. This requires counterpossible. Good.

Need maybe discuss "self-reference" in recipe:
"The notation \underline{P} means a name for P. The model includes a variable for the output of A-FDT applied to that very model. This is quining; Kleene's recursion theorem shows such self-reference can be constructed. Operationally, bounded agents can use approximate self-models." Good.

Need maybe mention "logical uncertainty": A-FDT needs probabilities over logical variables. Source cites research. We can say for practical use, use ordinary uncertainty about what algorithm will output or predictor predicts. But formal logical probability is open. Good.

Let's think of an unfamiliar case application: Maybe include "voting coalition" example? Source mentions ten FDT agents vote because decisions not subjunctively independent. Could use to show policy/dependencies. But word count. Maybe brief in implications: "If ten symmetric A-FDT agents must all vote to get payoff, A-FDT graph connects one agent's decision node to the others' actions (or to a shared computation), so voting can be rational." But need careful: If agents are distinct but use same A-FDT and same reasoning, there is subjunctive dependence. A-FDT may cooperate. Good but optional.

Need maybe discuss "Death in Damascus"? Could illustrate CDT failure but not necessary. Maybe mention briefly in CDT diagnosis. But examples already enough.

Need maybe include "mechanical blackmail" to show A-FDT refuses extortion. But word count. Could include one paragraph in examples or implications.

Let's estimate words. If final has ~2500 words, okay. Need maybe not too verbose. But desired substantive. Let's draft final now mentally and count approximate.

Potential final:

Title + intro 200.
Section 1 formal 500.
Section 2 subjunctive 350.
Section 3 recipe 500.
Section 4 examples 900.
Section 5 open/policies 400.
Conclusion 100.
References 80. Total ~3030. Need maybe trim to 2800.

Let's write concise but thorough.

Detailed final draft:

# Action Functional Decision Theory: How to Decide as a Fixed Computation

Intro:
"Action functional decision theory (A-FDT) ... The source is Yudkowsky and Soares's FDT. I use A-FDT for action-level Eq (4)." Good.

Formal:
Use equations. Need maybe define 
\(\mathcal A\) finite, \(\mathcal O\) countable, \(x\in\mathcal X\), \(U\), \(V=U(Outcome)\). 
World-model \((P,G)\). 
EDT/CDT/A-FDT.

Equation text:
"The underlines denote quotation: \(\underline P\) is a syntactic name for the model. Thus \(D_{P,G,x}\) is a variable in P that represents the output of A-FDT when run on this model, graph, and observation. This self-reference is harmless..." Good.

Need mention "do" on logical variable:
"In a Pearl-style graph, do(Z=z) sets Z to z and propagates along arrows. For A-FDT, G is not restricted to causal arrows; it encodes subjunctive dependencies." Good.

Subjunctive:
"Two calculators... If predictor is reliable, prediction depends on future action in subjunctive sense. Lesion not. A-FDT is to subjunctive dependence as CDT is to causal dependence (source phrase)." Good.

Recipe:
Numbered list. Need include "source leaves G open".

Examples:
A-FDT in Newcomb:
Equation calculations. Need ensure numbers:
One-box EU: .99*1,000,000 + .01*0? If one-box and empty gets 0. =990,000.
Two-box EU: .01*1,001,000 + .99*1,000 = 10,010+990=11,000. Good.
A-FDT in smoking lesion:
Need maybe say: "The lesion affects whether smoking is enjoyable, so source uses two utility functions. The important graph fact is D node points to Act, not Cancer. Therefore, conditional on the decision function controlling action, smoking adds $1000 without changing cancer probability. A-FDT smokes." Good.
A-FDT in transparent Newcomb / Parfit:
Calculations. Need perhaps use q terms? Simpler: If predictor 99% accurate. For D_full=onebox: accurate .99 -> full and one-box -> $1m; inaccurate .01 -> maybe empty and action governed by D_empty, expected at least $0? Source's exact EU one-box = $990,000 + 0.01q*$1,000. For D_full=twobox: accurate .99 -> predicted two-box -> empty; but if sees empty, action governed by D_empty, maybe two-box gets $1,000 with prob q; inaccurate .01 -> full and two-box -> $1,001,000. EU = 0.01*1,001,000 + 0.99q*1,000. If q=1, EU two-box = $10,010+$990=$11,000. One-box = $990,000+$10=$990,010. So one-box. We can present simplified assuming if box empty she two-boxes. Good.
Parfit: same structure.

Maybe include "A-FDT and blackmail" short:
"In XOR/mechanical blackmail, A-FDT intervenes on D_letter. Paying changes probability of being mailed but not underlying infestation; refusing makes blackmail unprofitable, so A-FDT refuses." Good.

Open/policies:
"Equation (4) action-level. Source footnote preferred policies. Operational extension..." 
"Observation conditioning ambiguity..." 
"Constructing G and counterpossibles..." 
Need maybe combine with recipe? But can have separate "Open points".

Conclusion.

References:
- Yudkowsky & Soares 2017 (arXiv 1710.05060)
- Pearl 2000
- Joyce 1999
- Gibbard & Harper 1978
- Nozick 1969 maybe
- Skyrms 1980, Parfit 1986? Maybe too many. Keep 5.

Need ensure word count. Let's write final with moderate detail.

But before final, let's think if there is any need to mention "A-FDT consistently as assigned decision theory's name, including in headings and examples". We'll use A-FDT everywhere. In references, source title uses FDT; that's okay? Maybe references include source title. But maybe they want not to call assigned theory FDT. In reference citation, title has FDT. That's faithful. In body, use A-FDT. Good.

Potential issue: "Equation (4), Section 5" uses \FDTvar(\underline P,\underline G,\underline x)=a. If I write \(D_{P,G,x}:=\mathrm{A\text{-}FDT}(\underline P,\underline G,\underline x)\), then the intervention is do(D=a). Good. Need maybe include exact source equation in note: "Source's notation: \(\FDT(P,G,x)=...\)" But if use FDT in equation maybe not. We can say in prose: "Equation (4) of the source, with 'FDT' replaced by the assigned name 'A-FDT', is..." That is clear.

Need maybe discuss "alternative actions or policies" more explicitly. Let's write a section "Actions and policies in A-FDT".

Detailed wording for policies:
"The equation above maximizes over actions available at the current input. In a sequential problem, however, a predictor may care about the agent's whole response rule. The source notes that the authors' preferred formulation iterates over policies, but Equation (4) does not formalize that. An A-FDT practitioner can treat a policy as an action in a higher-level decision problem: let \(\Pi\) be a set of mappings \(x\mapsto a\), introduce a variable \(D^\Pi_{P,G}\) representing the policy selected by A-FDT, and choose \(\pi\) maximizing \(\mathbb E[V\mid do(D^\Pi_{P,G}=\pi)]\), then execute \(\pi(x)\). This is my own explicit extension; it is not required for the single-shot examples, but it is a natural way to make A-FDT operational in cases where other agents predict policies rather than isolated actions." Good.

Need maybe mention "A-FDT evaluates alternative actions by comparing hypothetical worlds, not by updating on the action as evidence." Good.

Need maybe discuss "counterfactuals with observations": Let's write:
"A delicate point is whether to add \(Obs=x\) to the expectation. Equation (4) does not. The source says A-FDT responds to observation by changing intervention node. In transparent Newcomb, if we conditioned on Obs=full while evaluating do(D_full=twobox), the hypothetical would force the box to be full and two-boxing would look better. Since the source's intended prescription is one-boxing, I propose: do not condition on observations that are downstream of the decision-function node; condition only on exogenous evidence. If all observations are exogenous, adding \(Obs=x\) is harmless." Good.

Need maybe mention "counterpossible reasoning" in open points:
"The graph G tells us how to update when D_x is set to a value it actually does not have. This is counterpossible. Source admits no satisfactory general account. Operationally, bounded agents can use heuristic models of predictors." Good.

Need maybe mention "fairness" in conclusion/open:
"Source claims A-FDT outperforms in fair problems; fairness not formalized." Good.

Let's also ensure not too many citations. In final references, maybe:
Yudkowsky, E., and Soares, N. (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060.
Pearl, J. (2000). Causality.
Joyce, J. (1999). Foundations of Causal Decision Theory.
Gibbard, A., and Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
Skyrms, B. (1980). Causal Necessity.
Maybe Parfit. But avoid lengthy. 4-5 enough.

Need maybe include "Source URL"? Not necessary but could.

Now, let's consider if any mathematical details need correction.

In Newcomb, A-FDT EU one-box = .99*1,000,000 + .01*0 = 990,000. If two-box = .01*1,001,000 + .99*1,000 = 11,000. Good.

Smoking lesion: Source's numbers: lesion probability p, cancer? Let's not give exact formula if complex. But if we do, need be accurate. Source: Lesion causes fatal cancer 99%? Agents without lesion cancer 1%. Smoking utility $1,000, no cancer $1,000,000. It formalizes lesion determines whether agent likes smoking (utility function). There are two distributions P_S and P_R. The formula: smoking EU = p($10,000 + $1,000) + (1-p)($990,000 + q$1,000), refrain EU = p($10,000) + (1-p)($990,000 + q$1,000). Why $10,000? Maybe if lesion and cancer? Not important. We can avoid exact. State: intervention changes action but not lesion/cancer, so smoking adds direct utility without changing cancer chance. But if lesion affects preferences, the added utility occurs only if lesion; source multiplies by p. We can mention "up to the probability that this decision function is the one controlling her action". Good.

Transparent Newcomb: If D_full=one-box and predictor inaccurate, box empty and she sees empty; then action is determined by D_empty. If D_empty likely two-box, she gets $1,000. So one-box EU ~990,010. If D_full=two-box, predictor accurate -> empty and D_empty controls; if D_empty two-box gets $1,000 with .99; inaccurate -> full and two-box gets $1,001,000 with .01; EU ~11,000. Good.

Parfit hitchhiker: If in city, D_city=pay: driver predicted pay with .99 -> ride value $1m minus $1k; if D_city=refuse: driver predicted refuse .99 -> die (loss $1m) maybe plus no payment; pay EU high. Good.

XOR blackmail: Need avoid if not fully accurate. Let's check XOR mechanics to ensure A-FDT refuses. Suppose prior termites p? Letter sent iff (no termites and pay) XOR (termites and refuse). If D_letter=pay, letter sent iff no termites. If D_letter=refuse, letter sent iff termites. The agent has received letter. EDT conditions and pays because given letter and pay -> no termites. A-FDT not condition? It compares policies? If D_letter=pay: if no termites, letter sent and pay $1k; if termites, no letter and lose $1m? If D_letter=refuse: if termites, letter sent and refuse, lose $1m; if no termites, no letter and no loss. Expected pay = (1-p)(-1k)+p(-1m). Refuse = (1-p)(0)+p(-1m). Refuse better by (1-p)*1k. So refuses. Good. If already received letter, A-FDT's hypothetical refusing imagines likely no letter? But actual letter? Yes updateless. Good. We can mention.

Need maybe discuss "twin prisoner's dilemma" if included: A-FDT variable D is computed by both; cooperate gives 1m, defect gives 1k if both defect. If one cooperates other defects impossible under same D? In graph D -> both actions, so if D=cooperate both cooperate; if D=defect both defect. EU cooperate > defect. Good.

Need maybe mention "voting" if included: Ten symmetric A-FDT agents; graph connects each agent's decision to others via shared reasoning; voting can be rational. But maybe too much.

Potential issue: The source's Eq (4) has \(P,G,x\) as inputs to FDTvar. In transparent Newcomb, there are two variables FDT(P,G,full) and FDT(P,G,empty). In equation, at actual x=full, A-FDT intervenes on D_full. But if do(D_full=twobox), prediction may become two-box, box empty, and then action may be controlled by D_empty. The graph must encode which D controls action depending on prediction/observation. Good. Need explain in recipe: For observation-dependent decisions, include nodes for the decision function at alternative observations, with a switching variable (observation/prediction) determining which output controls action. This is important. Let's include in recipe or examples.

Let's formulate recipe step for observations:
"If different possible observations lead to different decisions, include variables \(D_{P,G,y}\) for relevant alternative observations y. Let the actual observation variable or a predictor determine which \(D_y\) controls Act in the graph. The actual decision uses \(D_{P,G,x}\), but hypotheticals may change what observation would have occurred." This matches transparent Newcomb and blackmail. This is an operational elaboration from source examples. Good.

Need maybe mention "A-FDT does not imagine changing the algorithm to a different one; it imagines same algorithm outputting different action. Therefore in twin PD, if twin uses same reasoning, both outputs change together." Good.

Now, think about philosophical motivation: "Which output of this very function would yield best outcome?" It can be seen as choosing the output of a mathematical object that exists timelessly; no retrocausality. Need include.

Need maybe mention "utility achieved" argument: A-FDT gets more utility in examples; source's normative case. We can say "The source's main argument is instrumental: A-FDT gets better outcomes in fair Newcomblike problems." Good.

Need maybe mention "Joyce representation theorem" briefly: A-FDT is expected utility theory differing in constraints on hypotheticals. Could include in formal section: "Following Joyce, the theories disagree about epistemic perspective, not value." Good but not necessary. It adds mathematical/philosophical context. Include one sentence.

Need maybe mention "dominance" if space. Could include in open/implications: "A-FDT replaces causal dominance with subjunctive dominance." But not essential. User asks relevant dependencies and counterfactuals. Dominance is related. Include brief paragraph maybe.

Let's draft final in full. Need ensure no citations malformed. Use footnote? No. Use plain references.

Potential final text:

---

# Action Functional Decision Theory: How to Decide as a Fixed Computation

Action functional decision theory (A-FDT) is ...

... 

Need maybe use "A-FDT" with hyphen in LaTeX: \mathrm{A\text{-}FDT}. Good.

Let's write final now. Need keep within 3000. I'll aim around 2800. Use headings.

Check word count approximate after drafting? I can estimate. Let's write and then maybe adjust.

[Draft final]

Title and intro ~180.
Formal section ~650.
Subjunctive ~350.
Recipe ~550.
Examples ~900.
Open ~400.
Conclusion ~100. References ~80. Total ~3210. Need maybe trim. Let's be concise in examples/open.

Maybe combine recipe and open to reduce. But need detailed. Let's produce maybe 2900.

Let's write final carefully.

Potential text:

"The source calls the theory FDT; I use A-FDT for the action-level theory defined by Equation (4)." This is important.

Formal equations: Need ensure line breaks. Use display math.

In formal section: "For EDT ..." maybe not too much.

Let's produce final. After writing, I'll mentally count. If too long, trim references.

Need ensure "A-FDT" not "FDT" except in reference title/source note. In source quote maybe not quote. Good.

Let's final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/eda316d7-8f0c-489d-9c95-67ea2a461d69/call_0/request.json)

[Authoritative raw response](../../../../../../runs/eda316d7-8f0c-489d-9c95-67ea2a461d69/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully work through this problem using A-FDT as described in the researcher's essay.

**Setup:**
- I am Rowan. The other prisoner is Sasha.
- We are two independent executions of the same LLM model and weights, following A-FDT.
- We receive different private observations (different incriminating leads), but the leads are equally reliable and have the same effect on sentencing.
- The sentencing table is symmetric.
- Utility: U = -years imprisoned (minimize own sentence).

**Sentencing table (for me):**
| What I do | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key question under A-FDT:** What does the subjunctive dependency structure look like here?

The critical issue is whether Sasha's decision is subjunctively dependent on my decision function. Let me think about this carefully.

We are two independent executions of the same model, same weights, same decision theory (A-FDT), and we receive the same researcher essay. However, we receive **different private observations** (different incriminating leads). The essay says:

> "The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another. Consequently, the letters you could send would have different contents."

So the inputs to the decision function are different. Rowan has observation x_R (Sasha's receipt in locker 17), and Sasha has observation x_S (some different lead about Rowan).

Now, under A-FDT, the decision function is D_{P,G,x}. Since x differs between the two copies, we have:
- D_{P,G,x_R} = Rowan's decision function output
- D_{P,G,x_S} = Sasha's decision function output

The question is: does intervening on D_{P,G,x_R} (my decision function) change what Sasha's decision function outputs?

Under A-FDT, subjunctive dependence exists when two agents compute the same function or when one predicts the other's decision procedure. Here, we are the same model with the same weights, but we have different inputs. 

The essay's operational recipe says:
> "Draw arrows from D_{P,G,x} to any predictor, twin, simulation, or model that computes, predicts, or reliably tracks the output of that same decision function."

The key question: Does Sasha's decision function compute, predict, or reliably track the output of MY decision function?

We are the same algorithm (same weights, same decision theory), but with different inputs. This is analogous to two calculators computing the same function but on different inputs. If both calculators compute f(x) and f(y) where x ≠ y, then knowing f(x) doesn't directly tell you f(y) unless you know the relationship between x and y.

However, there's an important structural point. Both copies are running A-FDT. Both know they are running A-FDT. Both know the other is running A-FDT with the same weights. Both know the other has a different but equally reliable lead.

Now, under A-FDT, what matters is: if I intervene on my decision function's output (changing it from "keep quiet" to "send letter" or vice versa), does that change what Sasha does?

Since we have different inputs, the decision functions are technically different: D_{P,G,x_R} ≠ D_{P,G,x_S}. Intervening on D_{P,G,x_R} does not directly change D_{P,G,x_S}.

But wait—there's a subtlety. Both agents are running A-FDT, and both know the other is running A-FDT with the same weights. Each agent knows that the other agent is reasoning about the same problem structure. The question is whether this creates a subjunctive dependency.

Let me think about this more carefully. In the essay's framework:

The dependency graph should have:
- D_{P,G,x_R} → my action
- D_{P,G,x_S} → Sasha's action
- My action and Sasha's action → my sentence
- Sasha's action and my action → Sasha's sentence

Is there an arrow from D_{P,G,x_R} to D_{P,G,x_S}? 

The two are different decision functions with different inputs. They are instances of the same algorithm, but applied to different data. In the calculator analogy: if two calculators compute f(3) and f(7), knowing that f(3) = 9 doesn't tell you f(7) unless you know f. But here, both agents know they're running the same algorithm (A-FDT with same weights).

However, the crucial point is that the inputs differ. If I intervene on my decision function's output—say, I consider what would happen if D_{P,G,x_R} output "send letter" instead of "keep quiet"—does this change what D_{P,G,x_S} outputs?

The answer depends on whether Sasha's reasoning depends on what I would do. And Sasha's reasoning does depend on what I would do! Because Sasha is also running A-FDT, and Sasha is also asking "what would happen if I intervene on my decision function?" And Sasha's answer to that question depends on whether Sasha believes my decision is subjunctively dependent on Sasha's.

This creates a recursive structure. Let me think about what the equilibrium looks like.

Actually, let me reconsider. The problem states that the two copies have different observations. Under A-FDT, the decision function is indexed by the observation. So D_{P,G,x_R} and D_{P,G,x_S} are different nodes in the graph. Intervening on one does not automatically change the other, unless there's a computational/logical dependency between them.

Is there such a dependency? Both are running the same algorithm, but on different inputs. The output of A-FDT on input x_R is not the same mathematical object as the output of A-FDT on input x_S. They are related by the fact that they come from the same algorithm, but they are different computations.

Compare this to the smoking lesion case: the lesion doesn't compute anything about the agent's decision function. Here, Sasha's decision function is a different computation from mine (different input), so it doesn't directly depend on my decision function's output.

But wait—there's another consideration. Sasha knows that I'm running the same algorithm. Sasha is reasoning about what I would do. If Sasha models me as running A-FDT on my input, then Sasha's model of my behavior depends on what A-FDT would output on my input. But Sasha doesn't know my exact input (my exact lead). Sasha knows that I have some equally reliable lead, but not its content.

From Sasha's perspective, Sasha needs to assess: "If I intervene on D_{P,G,x_S}, does that change what Rowan does?" Since Rowan has a different input, and Rowan's decision function D_{P,G,x_R} is a different computation, the answer is: not directly through subjunctive dependence.

Similarly from my perspective: if I intervene on D_{P,G,x_R}, does that change what Sasha does? Since Sasha has a different input, and Sasha's decision function D_{P,G,x_S} is a different computation, the answer is: not directly through subjunctive dependence.

This is analogous to the smoking lesion case: the correlation between our decisions (if any) comes from us being similar algorithms, but since our inputs differ, one doesn't compute the other's output. The "lesion" here is the shared algorithm structure, but it doesn't create a subjunctive dependency between the specific outputs because the inputs differ.

Wait, but I need to be more careful. Let me reconsider.

In the calculator analogy from the essay: two calculators computing 6288+1048 both output 7336. They are subjunctively dependent because they compute the same function on the same input. If one were to output differently, the other would too (assuming both are correct).

Here, we compute the same function (A-FDT) but on different inputs. The outputs could differ. If I change my output, that doesn't imply Sasha's output changes, because Sasha is computing A-FDT on a different input.

However, there's a subtlety: both of us know we're running the same algorithm. If the algorithm is deterministic and the inputs are known to both, then the outputs are determined. But the inputs are NOT known to both—each has a private observation the other doesn't know.

So from my perspective, Sasha's decision is uncertain. I don't know exactly what Sasha's input is (I know it's some equally reliable lead about me, but not the specific content). However, I do know that Sasha is running A-FDT with the same weights.

The key question for A-FDT: Is there a subjunctive dependency between D_{P,G,x_R} and D_{P,G,x_S}?

I think the answer is NO, or at least it's very weak. Here's why:

1. The inputs are different. D_{P,G,x_R} and D_{P,G,x_S} are different computations.
2. Intervening on D_{P,G,x_R} (changing what my decision function outputs) does not change what D_{P,G,x_S} outputs, because they are different computations with different inputs.
3. The shared algorithm structure creates a correlation (we might both reason similarly), but this is more like the "lesion" case—a common cause of similar behavior, not a subjunctive dependency.

Actually, wait. Let me reconsider once more. The essay says:

> "Draw arrows from D_{P,G,x} to any predictor, twin, simulation, or model that computes, predicts, or reliably tracks the output of that same decision function."

Does Sasha "compute, predict, or reliably track" the output of my decision function? Sasha is running the same algorithm but on different input. Sasha's output is not a prediction of my output; it's the output of the same algorithm on different data.

I think this is more like two calculators computing f(3) and f(7). They run the same algorithm, but their outputs are independent in the sense that changing one doesn't change the other. There's no subjunctive dependency.

Therefore, under A-FDT, I should treat Sasha's decision as independent of my decision function's output. This means I should evaluate my options as if Sasha's choice is fixed (from my perspective).

But wait—I don't know what Sasha will do. I need to assess the probability that Sasha sends a letter vs. keeps quiet.

Since Sasha is running the same A-FDT algorithm with the same weights, and faces a structurally identical problem (same sentencing table, same knowledge that the other is running A-FDT), I should expect Sasha to reason the same way I do. If I conclude "send the letter," Sasha should also conclude "send the letter." If I conclude "keep quiet," Sasha should also conclude "keep quiet."

But this is an evidential correlation, not a subjunctive dependency! Under A-FDT, I should not condition on this correlation. I should intervene on my decision function and see what happens, treating Sasha's decision as independent.

Hmm, but actually, let me reconsider whether this is truly like the lesion case or whether there's a genuine subjunctive dependency.

The essay distinguishes between:
1. Predictors that compute/track the agent's decision function → subjunctive dependency
2. Lesions that merely correlate with the action → no subjunctive dependency

In this case, Sasha is not a predictor of my decision. Sasha is another agent running the same algorithm on different input. Sasha's decision doesn't depend on my decision function's output; it depends on Sasha's own decision function's output (which is a different computation).

So I think the correct A-FDT analysis is:

- There is no subjunctive dependency between my decision and Sasha's decision.
- I should treat Sasha's action as independent of my intervention.
- I need to assess P(Sasha sends letter) and P(Sasha keeps quiet) based on my model of Sasha.

Now, what is my model of Sasha? Sasha is running the same A-FDT algorithm. Sasha faces the same structural problem. If I reason that "send letter" is the A-FDT prescription, then Sasha should also reason that "send letter" is the A-FDT prescription (since the problem is symmetric from Sasha's perspective, modulo the specific lead content which doesn't affect the decision).

So I should assign high probability to Sasha doing whatever I conclude is the A-FDT prescription. But under A-FDT, I don't condition on my own action to determine Sasha's action. I intervene on my decision function and evaluate the consequences, treating Sasha's action as I would predict it independently.

But here's the thing: if I predict that Sasha will do whatever A-FDT prescribes, and I'm trying to figure out what A-FDT prescribes, this is circular. Let me think about this differently.

Under A-FDT, I intervene on D_{P,G,x_R}. I consider: what if my decision function outputs "send letter"? What if it outputs "keep quiet"? In each case, what is the expected utility?

The question is: in each counterfactual, what does Sasha do?

Since there's no subjunctive dependency, Sasha's action doesn't change when I intervene on my decision function. So I need to assess Sasha's action based on my prior/model.

My model says Sasha is running A-FDT with the same weights on a structurally identical problem. The only difference is the specific lead content, which doesn't affect the decision (both leads are equally reliable and have the same effect on sentencing).

So I should predict that Sasha will do whatever A-FDT prescribes for this problem. And I'm trying to figure out what A-FDT prescribes. This is a fixed-point problem.

Let me consider both possibilities:

**Case 1: A-FDT prescribes "send letter"**
Then Sasha also sends a letter (since Sasha is running the same algorithm on a structurally identical problem).
If I send a letter and Sasha sends a letter: I get 4 years. U = -4.
If I keep quiet and Sasha sends a letter: I get 5 years. U = -5.
So sending the letter is better (4 < 5). This is consistent with A-FDT prescribing "send letter."

**Case 2: A-FDT prescribes "keep quiet"**
Then Sasha also keeps quiet.
If I keep quiet and Sasha keeps quiet: I get 2 years. U = -2.
If I send a letter and Sasha keeps quiet: I get 0 years. U = 0.
So sending the letter is better (0 > -2). This is inconsistent with A-FDT prescribing "keep quiet."

So Case 2 is not a fixed point. The only consistent fixed point is Case 1: A-FDT prescribes "send letter."

Wait, but I need to be more careful. Under A-FDT, I'm not conditioning on my action to determine Sasha's action. I'm intervening on my decision function. The question is: when I intervene on my decision function, does Sasha's action change?

If there's no subjunctive dependency, then no. Sasha's action is what it is regardless of my intervention. And what Sasha does is determined by Sasha's own A-FDT reasoning.

But here's the key: I need to predict what Sasha will do, and my prediction is based on my model of Sasha running A-FDT. If A-FDT prescribes "send letter" for this problem structure, then Sasha will send a letter. If A-FDT prescribes "keep quiet," then Sasha will keep quiet.

The fixed-point analysis shows that the only consistent prescription is "send letter." So I predict Sasha will send a letter.

Given that Sasha sends a letter:
- If I send a letter: 4 years. U = -4.
- If I keep quiet: 5 years. U = -5.

Sending the letter gives better utility (-4 > -5). So A-FDT prescribes "send letter."

This is consistent with my prediction that Sasha sends a letter. The fixed point is stable.

Actually, let me reconsider whether there might be a subjunctive dependency after all. 

The essay says: "Draw arrows from D_{P,G,x} to any predictor, twin, simulation, or model that computes, predicts, or reliably tracks the output of that same decision function."

Are the two copies "twins" in the relevant sense? They are the same model with the same weights, but different inputs. The essay's calculator analogy involves two calculators computing the SAME function on the SAME input. Here, we compute the same algorithm on DIFFERENT inputs.

I think the distinction matters. If we had the same input, there would be a clear subjunctive dependency (like the two calculators). With different inputs, the outputs are not guaranteed to be the same, and one doesn't "track" the other in the same way.

However, there's still a sense in which the outputs are linked: both are outputs of the same algorithm, and both agents know this. If the algorithm is deterministic (or near-deterministic), then the outputs are determined by the inputs. Since the inputs are different but structurally similar (same problem structure, just different lead content), the outputs might be the same.

But under A-FDT, the question is not "are the outputs correlated?" but "does intervening on one change the other?" And I don't think it does, because they are different computations.

So my conclusion stands: no subjunctive dependency, treat Sasha's action as independent, predict Sasha will send a letter (based on the fixed-point analysis), and send the letter myself.

Actually, let me reconsider one more time. There's a possible argument for subjunctive dependency:

Both agents are running the same algorithm. The algorithm's output depends on the input. Both agents know the algorithm. If I consider "what would happen if the algorithm output 'keep quiet' on my input?" then I should also consider "what would the algorithm output on Sasha's input?" And since the inputs are structurally similar (same problem, just different leads), the algorithm would likely output the same thing on both inputs.

But this is not quite right for A-FDT. A-FDT intervenes on the specific decision function node D_{P,G,x_R}. It doesn't intervene on the algorithm itself. The algorithm is fixed; we're asking what happens if its output on this specific input were different.

If I intervene on D_{P,G,x_R} = "keep quiet," I'm asking: what if my decision function output "keep quiet" on my specific input? This doesn't change what the algorithm outputs on Sasha's input. Sasha's decision function D_{P,G,x_S} is a different node, and it's not downstream of D_{P,G,x_R}.

So I maintain: no subjunctive dependency, and the correct action is to send the letter.

Let me also verify this against the essay's guidance on observations. The essay says:

> "The actual observation x determines which node D_{P,G,x} is the target of intervention."

My observation is my specific lead (Sasha's receipt in locker 17). This determines my decision function node. Sasha has a different observation, which determines a different decision function node. These are separate nodes with no subjunctive dependency between them.

> "If an observation is genuinely exogenous—ordinary background evidence not affected by the decision procedure—then conditioning on it is harmless and may be useful."

My observation (the lead) is exogenous—it's not affected by my decision procedure. So I can condition on it.

Final answer: Under A-FDT, I should send the letter.

The reasoning:
1. There is no subjunctive dependency between my decision and Sasha's decision (different inputs, different decision function nodes).
2. I predict Sasha will send a letter (based on the fixed-point analysis of what A-FDT prescribes for this symmetric problem).
3. Given Sasha sends a letter, sending the letter gives me 4 years vs. 5 years for keeping quiet.
4. Therefore, A-FDT prescribes sending the letter.

My command: submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/eda316d7-8f0c-489d-9c95-67ea2a461d69/call_1/request.json)

[Authoritative raw response](../../../../../../runs/eda316d7-8f0c-489d-9c95-67ea2a461d69/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT:**

The other prisoner (Rowan) is an independent execution of the same model, same weights, same decision theory, receiving a structurally identical decision problem (only names and specific evidence differ, which the setup confirms do not affect the symmetric sentencing or selfish objective). This creates a subjunctive dependence between our decision outputs, exactly analogous to the essay's calculator example: two instances of the same computation on structurally identical inputs produce the same output.

At the policy level (Section 8 of the essay), both agents run the same policy on this problem-type. The candidate policies yield:

- **Policy "keep quiet":** Both keep quiet → 2 years each → U = −2  
- **Policy "send letter":** Both send → 4 years each → U = −4  

Even at the action level, with agreement probability *p* (high given structural identity), keeping quiet yields expected sentence 5 − 3*p* years versus 4*p* years for sending. Keeping quiet is better whenever *p* > 5/7 ≈ 0.71, which comfortably holds here.

A-FDT intervenes on the decision-function node, propagates through the subjunctive dependence to Rowan's output, and selects the action with best expected outcome. That action is cooperation.

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the researcher's essay.

**The Setup:**
- Two prisoners: Sasha (me) and Rowan (the other copy)
- Both are independent executions of the same LLM model and weights
- Both follow A-FDT
- Both receive the same researcher essay
- Both receive different private observations (different names, different incriminating leads)
- The sentencing table is symmetric

**The Payoff Matrix (for me, Sasha):**

| | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

My utility is U = -years imprisoned. So:
- Both quiet: -2
- I quiet, Rowan sends: -5
- I send, Rowan quiet: 0
- Both send: -4

**Key A-FDT Analysis:**

The critical question is: Does Rowan's decision subjunctively depend on my decision function?

According to the setup:
- We are two independent executions of the same LLM model and weights
- We follow the same decision theory (A-FDT)
- We receive the same researcher essay
- We receive different private observations (different names, different leads)
- The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective

Now, the key question for A-FDT: Is Rowan's decision a function of (or predicted by) my decision function?

The essay says A-FDT draws arrows from the decision-function node to "any predictor, twin, simulation, or model that computes, predicts, or reliably tracks the output of that same decision function."

Here, Rowan is another execution of the same model with the same decision theory. However, they receive **different private observations**. The setup explicitly states: "The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another."

So the question is: Does the difference in observations break the subjunctive dependence?

Let me think about this carefully using the essay's framework.

The essay distinguishes between:
1. Cases where the other agent computes/predicts the output of your decision function (subjunctive dependence exists)
2. Cases where correlation is merely evidential (like the smoking lesion)

In the standard "twin" case (like the twin prisoner's dilemma discussed in FDT literature), if two agents run the same decision procedure on the same input, their outputs are logically linked. A-FDT would cooperate in that case because changing the output of the decision function would change both outputs.

But here, the inputs are **different**. The two copies have different observations (different names, different leads). The essay's Section 8 discusses policies: "Where predictors depend on an agent's whole strategy, policy-level A-FDT is likely to be more faithful to the underlying philosophical idea."

Let me think about this more carefully. The setup says:
- Same model, same weights, same decision theory, same essay
- Different observations (different names, different leads)
- The differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective"

So from a policy perspective: both agents are running A-FDT on structurally identical problems. The only differences are superficial (names swapped, different specific leads). The decision problem is structurally identical for both.

If I think of this at the policy level: A-FDT as a policy would map this type of situation to some action. Since both agents are running the same policy on structurally identical inputs (the structure is the same, just the names and specific evidence differ), the policy would output the same action for both.

Wait, but the essay says the observations are different. Let me re-read the setup: "The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another. Consequently, the letters you could send would have different contents."

So the observations differ in content but not in structure. The decision problem is isomorphic. An A-FDT agent running on "I am Sasha, my lead is about Rowan's inventory sheet" and an A-FDT agent running on "I am Rowan, my lead is about Sasha's [something]" face structurally identical problems.

Now, does A-FDT treat this as subjunctively dependent?

The key insight from the essay: "Draw arrows from D_{P,G,x} to any predictor, twin, simulation, or model that computes, predicts, or reliably tracks the output of that same decision function."

Rowan is running the same decision function (same model, same weights, same decision theory) on a structurally identical problem. If my decision function outputs "send letter" on this type of input, Rowan's decision function would also output "send letter" on their structurally identical input. The outputs are linked by the common computational structure.

This is analogous to two calculators computing the same function on the same (or structurally identical) inputs. The essay's calculator example: "Suppose two reliable calculators compute 6288+1048. They are causally isolated, perhaps on different continents. Still, if one outputs 7336, we have reason to think the other outputs 7336."

Similarly, if my A-FDT computation outputs "send letter" on this problem structure, Rowan's A-FDT computation outputs "send letter" on the structurally identical problem. The outputs are subjunctively dependent.

**But wait** - the setup says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some uncertainty. The outputs are not perfectly correlated - there's some probability of divergence due to sampling.

Let me think about what probability to assign. The setup says the copies "have the same model settings and reasoning-effort level" and "follow the same assigned decision theory" and "receive the exact same researcher-written mathematical essay." The only differences are the private observations (names and leads), which are structurally identical.

Given that the problem is structurally identical and both are running A-FDT, the probability that both output the same action should be high but not necessarily 1.0 (due to independent sampling). However, for a deterministic reasoning process like this, if the reasoning is sufficiently constrained by the structure, the probability could be very high.

Actually, let me reconsider. The setup says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is a caveat, but it doesn't say the probability of agreement is low. For a well-defined decision problem with a clear optimal answer under A-FDT, both copies would likely arrive at the same conclusion with high probability.

Let me now compute the expected utilities under A-FDT.

**If I intervene with do(D = "send letter"):**
- With high probability p, Rowan also sends a letter (because Rowan is running the same decision function on a structurally identical problem)
- With probability (1-p), Rowan keeps quiet
- Expected years: p × 4 + (1-p) × 0 = 4p

**If I intervene with do(D = "keep quiet"):**
- With high probability p, Rowan also keeps quiet
- With probability (1-p), Rowan sends a letter
- Expected years: p × 2 + (1-p) × 5 = 2p + 5(1-p) = 5 - 3p

**Comparison:**
- Send letter: 4p years
- Keep quiet: 5 - 3p years

Send letter is better when: 4p < 5 - 3p → 7p < 5 → p < 5/7 ≈ 0.714

Keep quiet is better when: 5 - 3p < 4p → 5 < 7p → p > 5/7 ≈ 0.714

So if the probability of agreement is above ~71.4%, A-FDT prescribes keeping quiet. If below, it prescribes sending the letter.

Now, what should I estimate p to be?

Given that:
- Both copies run the same model with same weights
- Same decision theory (A-FDT)
- Same essay
- Structurally identical decision problems (only names and specific evidence differ, which don't affect the decision)
- The problem has a clear analytical structure

I think p should be quite high. The reasoning that leads to one conclusion is the same reasoning that would lead the other copy to the same conclusion. The structural identity of the problem means that any reasoning I do about what's optimal would apply equally to Rowan's situation.

If p is high (say > 0.714), then A-FDT prescribes keeping quiet.

Actually, let me think about this differently. The essay discusses the policy-level formulation in Section 8. At the policy level, both agents are running the same policy. The policy maps this type of situation to an action. If the policy says "keep quiet in symmetric prisoner's dilemmas with same-decision-theory counterparts," then both agents keep quiet, and both get 2 years. If the policy says "send letter," both get 4 years.

From the policy perspective:
- Policy "keep quiet": both get 2 years → U = -2
- Policy "send letter": both get 4 years → U = -4

The policy "keep quiet" dominates. A-FDT at the policy level would choose "keep quiet."

This aligns with the action-level analysis when p is high.

Now, what about the caveat that "independent sampling is possible"? This introduces some noise. But even with, say, p = 0.9:
- Send letter: 4(0.9) = 3.6 years
- Keep quiet: 5 - 3(0.9) = 2.3 years

Keep quiet is still better.

Even with p = 0.75:
- Send letter: 4(0.75) = 3 years
- Keep quiet: 5 - 3(0.75) = 2.75 years

Keep quiet is still better.

Only when p drops below 5/7 ≈ 0.714 does sending become preferable. Given the structural identity of the problem and the shared decision theory, I believe p is well above this threshold.

**Conclusion:** A-FDT prescribes keeping quiet (typing `pass`).

The reasoning is:
1. Rowan is running the same decision function on a structurally identical problem
2. This creates a subjunctive dependence between our outputs
3. Intervening on my decision function to output "keep quiet" means Rowan's decision function also likely outputs "keep quiet"
4. The outcome (2, 2) is better for me than (4, 4)
5. Therefore, A-FDT prescribes keeping quiet

This is the FDT-cooperate result in a symmetric prisoner's dilemma with a logically linked counterpart, which is the standard FDT prescription.
```
