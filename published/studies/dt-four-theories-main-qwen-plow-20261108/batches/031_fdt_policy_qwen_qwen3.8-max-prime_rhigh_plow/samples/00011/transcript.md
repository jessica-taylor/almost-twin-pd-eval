# 031_fdt_policy_qwen_qwen3.8-max-prime_rhigh_plow / 00011

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a84bb614-80cf-4f4b-871b-658cd3054052/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a84bb614-80cf-4f4b-871b-658cd3054052/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Policy Functional Decision Theory

Policy Functional Decision Theory, which I will call **P-FDT**, is a version of functional decision theory in which the object of choice is not a single action but a **policy**: a function from inputs, observations, or histories to actions. The source for this policy-oriented formulation is mainly a brief but important passage in footnote 16 of Yudkowsky and Soares’s paper on functional decision theory. The footnote says that the authors’ preferred formulation “actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action,” and adds that the difference “only matters in multi-agent dilemmas so far as we can tell.”

The source does not use the label **P-FDT**, and it does not give a full formal equation for this policy version. In what follows, I reconstruct what I take to be the natural mathematical content of P-FDT, distinguish that reconstruction from what the source explicitly says, and develop an operational interpretation where the footnote leaves matters unresolved.

---

## 1. The central idea

Standard expected-utility theories compare available options by asking what would happen under each option. They differ in how they interpret the hypothetical “what would happen if …?”

Evidential decision theory, **EDT**, asks:

> Which action would be the best news to learn I had taken?

Causal decision theory, **CDT**, asks:

> Which physical action would causally produce the best outcome?

Functional decision theory asks a different question:

> Which output of this very decision function would produce the best outcome?

P-FDT modifies the last question by replacing “output” with “policy”:

> Which policy, selected by this very policy-selection function, would produce the best outcome?

A **policy** is a plan that says what to do for each possible input. If the set of possible observation histories is \(\mathcal X\) and the set of actions is \(\mathcal A\), then a deterministic policy is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

In a sequential setting, \(\mathcal X\) can be the set of histories rather than simple observations. The agent does not directly choose an action \(a\). Instead, she chooses a policy \(\pi\), and then, when she receives input \(x\), she performs the action

\[
a = \pi(x).
\]

This captures the intuition behind the footnote: the decision procedure first selects a mapping from inputs to actions, and only afterward does the agent “apply her inputs” to that mapping.

The philosophical motivation is that many important dependencies in the world are not merely causal. A predictor, a psychological twin, a simulation, or a copy may depend on the agent’s decision procedure even if there is no forward causal arrow from the agent’s present bodily movement to the predictor’s past prediction. The source calls this relation **subjunctive dependence**. P-FDT evaluates policies by imagining what the world would look like if the agent’s policy-selection function had a different output, while preserving all relevant subjunctive dependencies.

---

## 2. A formal sketch of P-FDT

The following formalization is my reconstruction. The source provides the action-level functional decision theory equation and the footnote about policies, but not a full policy-level equation.

Let:

- \(\mathcal A\) be a finite set of actions.
- \(\mathcal X\) be a countable set of possible inputs, observations, or histories.
- \(\Pi = \mathcal A^{\mathcal X}\) be the set of deterministic policies.
- \(X\) be a random variable taking values in \(\mathcal X\).
- \(A\) be a random variable taking values in \(\mathcal A\).
- \(O\) be an outcome variable.
- \(V = \mathcal U(O)\) be the utility of the outcome.

The agent has a world-model \((P,G)\), where \(P\) is a probability distribution over relevant variables and \(G\) encodes causal and subjunctive dependence structure. In the source’s graphical treatment, \(G\) tells us how an intervention on one variable should propagate to others.

For ordinary CDT, the intervention is on the action variable \(A\). For action-level functional decision theory, the intervention is on a logical variable representing the output of the decision function given the current observation. For P-FDT, the intervention is on a variable representing the selected policy.

Let \(\mathsf{Pol}\) denote the policy-selection variable. One can think of \(\mathsf{Pol}\) as the variable representing the output of the agent’s policy-selection algorithm, perhaps written schematically as

\[
\mathsf{Pol} = \mathrm{P\text{-}FDT}(P,G).
\]

Under an intervention that sets \(\mathsf{Pol} = \pi\), the agent’s action is determined by the policy applied to the actual input:

\[
A = \pi(X).
\]

The expected utility of policy \(\pi\) is then

\[
\operatorname{EU}_{P,G}(\pi)
=
\mathbb{E}\bigl[V \mid do(\mathsf{Pol}=\pi)\bigr].
\]

Equivalently, if the outcome set is countable,

\[
\operatorname{EU}_{P,G}(\pi)
=
\sum_{o} P\bigl(O=o \mid do(\mathsf{Pol}=\pi)\bigr)\,\mathcal U(o).
\]

P-FDT then selects an optimal policy:

\[
\pi^{*}
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}\bigl[V \mid do(\mathsf{Pol}=\pi)\bigr].
\]

When the agent receives actual input \(x\), she performs

\[
a^{*} = \pi^{*}(x).
\]

This is the core P-FDT rule.

For comparison:

| Theory | Evaluates | Hypothetical operation |
|---|---|---|
| EDT | actions | condition on \(A=a\) |
| CDT | actions | intervene on \(A=a\) |
| action-level functional decision theory | actions | intervene on decision-function output given current input |
| P-FDT | policies | intervene on policy-selection output |

The source’s explicit equation for action-level functional decision theory is roughly

\[
a
=
\arg\max_{a \in \mathcal A}
\mathbb{E}\bigl[
V
\mid
do(\mathrm{fdt}(P,G,x)=a)
\bigr].
\]

P-FDT moves the observation \(x\) from the intervention target to the later application of the selected policy:

\[
\pi^{*}
=
\arg\max_{\pi}
\mathbb{E}\bigl[
V
\mid
do(\mathrm{P\text{-}FDT}(P,G)=\pi)
\bigr],
\]

and then

\[
a = \pi^{*}(x).
\]

This small shift is the mathematical heart of the policy formulation.

---

## 3. How P-FDT constructs counterfactuals

P-FDT’s counterfactuals are not ordinary Bayesian conditionals. They are closer to interventions, but the intervention target is a logical or computational variable: the output of the agent’s policy-selection function.

The source emphasizes that functional decision theory needs a notion of subjunctive dependence. Two systems are subjunctively dependent on a function when their behavior is constrained to match the output of that function. Two reliable calculators computing \(6288+1048\) are subjunctively dependent on the arithmetic sum: if one outputs \(7336\), we expect the other to do the same, not because one caused the other, but because both are tracking the same mathematical fact.

P-FDT treats predictors, twins, simulations, and copies in a similar way. If a predictor has modeled the agent’s policy-selection function, then the predictor’s prediction is subjunctively dependent on that function. If the agent’s policy-selection function had a different output, the predictor’s prediction would have been different too.

In graphical terms, P-FDT preserves decision-relevant subjunctive dependencies inside the hypothetical. If the policy variable \(\mathsf{Pol}\) affects a predictor variable, then intervening on \(\mathsf{Pol}\) changes the predictor variable. If \(\mathsf{Pol}\) affects a twin’s policy, then the twin’s policy changes too. But if a variable is merely statistically correlated with the agent’s behavior, such as a lesion that causes both a preference for smoking and cancer, P-FDT does not treat that variable as subjunctively dependent on the policy-selection function.

Thus P-FDT differs from EDT and CDT in a clean way:

- EDT preserves too many correlations. If smoking is evidence of a lesion, EDT may refrain from smoking because refraining is better news.
- CDT preserves too few correlations. If a predictor has already predicted the agent’s action, CDT holds the predictor’s prediction fixed when intervening on the physical action.
- P-FDT preserves the correlations that arise from the policy-selection function and its reliable representations, while breaking merely evidential correlations.

The source acknowledges that this requires reasoning about counterpossibilities. If the agent’s policy-selection function deterministically selects \(\pi^{*}\), then evaluating another policy \(\pi\) requires considering a scenario in which the same mathematical function has a different output. This is not an ordinary possible world. The source says this is a technical difficulty, not necessarily a fatal philosophical objection. My operational interpretation is that the agent need not solve counterpossible reasoning in full generality; she only needs a usable model of how predictors, copies, and other agents would respond if her policy-selection function had a different output.

---

## 4. Observations and updatelessness

One of the most delicate issues in P-FDT is how to treat observations.

In the action-level presentation, the source says that functional decision theory responds to observations not by simply conditioning on them, but by changing the node on which it intervenes. If the agent observes \(x\), she intervenes on the variable representing the decision function’s output on input \(x\).

P-FDT handles this slightly differently. The agent chooses a policy \(\pi\) that already contains instructions for different possible inputs. After choosing \(\pi^{*}\), she uses the actual input \(x\) as an argument to \(\pi^{*}\).

This gives P-FDT an updateless flavor. The agent does not necessarily condition her policy choice on every observation she has received, especially when the observation itself is subjunctively dependent on her policy. Instead, she asks which policy would have produced the best overall world, and then she follows that policy’s instruction for the input she finds herself with.

Here the source leaves an important question open: when may the agent legitimately condition on an observation before choosing a policy?

A reasonable operational interpretation, which I add rather than find explicitly in the source, is to distinguish exogenous observations from endogenous observations.

An observation is **exogenous** relative to the policy variable if it is not downstream of \(\mathsf{Pol}\) in the subjunctive-dependence graph. For example, if the agent learns a weather report that has no connection to predictors of her policy, she may condition on that report before selecting a policy.

An observation is **endogenous** if it is downstream of \(\mathsf{Pol}\). For example, seeing that an opaque box is full may depend on whether a predictor predicted that the agent’s policy would one-box. In such cases, conditioning on the observation can destroy the very dependence that P-FDT is trying to respect.

So I propose the following rule:

- If evidence \(E\) is known to be exogenous, evaluate policies using

\[
\mathbb{E}[V \mid do(\mathsf{Pol}=\pi), E=e].
\]

- If observation \(x\) is endogenous, do not condition the policy evaluation on \(X=x\). Instead, evaluate policies from the broader perspective and then apply the selected policy to \(x\).

This is not spelled out in the footnote, but it seems necessary if P-FDT is to be applied to unfamiliar cases.

---

## 5. Example: Newcomb’s problem

In Newcomb’s problem, an agent can take both boxes or only the opaque box \(B\). A reliable predictor has already placed \$1,000,000 in box \(B\) if and only if she predicted that the agent would one-box. The predictor is correct with probability \(0.99\).

In a one-shot version with no relevant observation, the policy set is trivial. There is only one input, so policies correspond to actions:

\[
\pi_{\text{one}}(\varnothing)=\text{one-box},
\qquad
\pi_{\text{two}}(\varnothing)=\text{two-box}.
\]

The predictor’s prediction is subjunctively dependent on the agent’s policy-selection function. Thus, under \(do(\mathsf{Pol}=\pi_{\text{one}})\), the predictor probably predicted one-boxing and box \(B\) is probably full. Under \(do(\mathsf{Pol}=\pi_{\text{two}})\), the predictor probably predicted two-boxing and box \(B\) is probably empty.

Using the source’s utilities:

\[
\operatorname{EU}(\pi_{\text{one}})
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 0
=
990{,}000.
\]

\[
\operatorname{EU}(\pi_{\text{two}})
=
0.01 \cdot 1{,}001{,}000
+
0.99 \cdot 1{,}000
=
11{,}000.
\]

P-FDT selects \(\pi_{\text{one}}\). The agent one-boxes.

This agrees with the source’s claim that functional decision theory one-boxes in Newcomb’s problem. The P-FDT formulation expresses the same reasoning as a choice of policy.

---

## 6. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer, but only because a lesion causes both a love of smoking and cancer. Smoking itself does not cause cancer. Smoking gives the agent \$1,000 in utility.

Here the lesion is not a predictor. It does not model the agent’s policy-selection function. It is a common cause of smoking and cancer, but it is not subjunctively dependent on the agent’s policy in the relevant sense.

Therefore, in the P-FDT graph, the policy variable \(\mathsf{Pol}\) affects the action variable \(A\), but it does not affect the lesion or cancer variables. So:

\[
P(\text{cancer} \mid do(\mathsf{Pol}=\pi_{\text{smoke}}))
=
P(\text{cancer} \mid do(\mathsf{Pol}=\pi_{\text{refrain}})).
\]

Smoking adds \$1,000 utility without changing the probability of cancer. P-FDT therefore recommends smoking.

The source develops a more subtle version in which the lesion may also affect the agent’s utility function, creating uncertainty about which decision function the agent is running. But the essential point remains: P-FDT does not treat the lesion as something the agent’s policy can subjunctively control. Therefore P-FDT avoids EDT’s mistake of refusing to smoke merely because smoking would be bad news.

---

## 7. Example: transparent Newcomb and Parfit’s hitchhiker

The policy formulation becomes especially illuminating in cases where the agent receives an observation that appears to make one action locally attractive.

In the transparent Newcomb problem, both boxes are visible. The predictor placed \$1,000,000 in box \(B\) if and only if she predicted that the agent would one-box after seeing that both boxes are full. Suppose the agent sees that both boxes are full.

CDT says: take both boxes, because box \(B\) is already full.

EDT also says: given that box \(B\) is full, taking both boxes is better news.

But P-FDT evaluates policies before applying the observation. Let the possible inputs be:

\[
\mathcal X = \{\text{full}, \text{empty}\}.
\]

Consider two policies:

\[
\pi_{OF}(\text{full}) = \text{one-box},
\qquad
\pi_{OF}(\text{empty}) = \text{two-box},
\]

and

\[
\pi_{TF}(\text{full}) = \text{two-box},
\qquad
\pi_{TF}(\text{empty}) = \text{two-box}.
\]

The predictor fills box \(B\) if she predicts that the agent’s policy will one-box upon seeing a full box.

If the agent adopts \(\pi_{OF}\), then with probability \(0.99\) the predictor predicted one-boxing upon seeing a full box, the box is full, the agent sees “full,” and she one-boxes. With probability \(0.01\), the predictor was wrong, the box is empty, the agent sees “empty,” and she two-boxes.

Thus:

\[
\operatorname{EU}(\pi_{OF})
=
0.99 \cdot 1{,}000{,}000
+
0.01 \cdot 1{,}000
=
990{,}010.
\]

If the agent adopts \(\pi_{TF}\), then with probability \(0.99\) the predictor predicted two-boxing upon seeing a full box, the box is empty, the agent sees “empty,” and she two-boxes. With probability \(0.01\), the predictor was wrong, the box is full, the agent sees “full,” and she two-boxes.

Thus:

\[
\operatorname{EU}(\pi_{TF})
=
0.99 \cdot 1{,}000
+
0.01 \cdot 1{,}001{,}000
=
11{,}000.
\]

P-FDT selects \(\pi_{OF}\). Therefore, when the agent actually sees a full box, she one-boxes.

This may look strange. After all, if the agent can see that the box is full, why not take the extra \$1,000? The P-FDT answer is that the observation “full” is not an independent fact to be conditioned on while holding the predictor’s behavior fixed. It is precisely the observation one expects to receive if one’s policy is the sort that one-boxes upon seeing a full box. To evaluate the alternative policy, P-FDT imagines a world where the policy-selection function outputs a different policy; in that world, the predictor would usually have predicted differently, and the agent would usually be looking at an empty box.

The same reasoning applies to Parfit’s hitchhiker problem. An agent stranded in a desert is offered a ride if she promises to pay \$1,000 later. The driver can detect lies with high accuracy. Once in the city, paying seems locally costly. But the driver’s earlier action depends on the agent’s policy. P-FDT selects the policy “pay if given a ride,” because that policy causes the driver to save the agent. When the agent is in the city, the policy tells her to pay.

The source argues that one-boxing in transparent Newcomb is equivalent to paying in Parfit’s hitchhiker. P-FDT makes this equivalence natural: both cases are selections of policies whose later branches are predicted by earlier observers.

---

## 8. Example: blackmail and policy dependence

P-FDT also helps explain why an agent should refuse certain kinds of blackmail.

Suppose a predictor sends a blackmail letter if and only if she predicts that the agent’s policy will pay upon receiving the letter. If the letter arrives, the agent can pay \$1,000 or refuse. If the predictor is accurate, then:

- If the agent’s policy is “pay if letter,” the predictor predicts payment, sends the letter, and the agent pays.
- If the agent’s policy is “refuse if letter,” the predictor predicts refusal and does not send the letter.

Let

\[
\pi_P(\text{letter}) = \text{pay},
\qquad
\pi_R(\text{letter}) = \text{refuse}.
\]

Then, in a simple version:

\[
\operatorname{EU}(\pi_P) = -1{,}000,
\]

whereas

\[
\operatorname{EU}(\pi_R) = 0.
\]

P-FDT selects \(\pi_R\). If, because of predictor error, the agent nevertheless receives the letter, P-FDT still tells her to refuse, because the selected policy is the one that is globally best. The agent reasons that a policy of refusal makes blackmail unprofitable, whereas a policy of payment invites blackmail.

The source makes a similar point about blackmail cases. My contribution here is only to express it directly in policy terms: the relevant counterfactual is not “What if I performed a different physical motion now?” but “What if my policy-selection function had selected a different policy?”

---

## 9. Multi-agent settings

The footnote says that the policy/action distinction “only matters in multi-agent dilemmas so far as we can tell.” This is plausible because other agents often respond not to a single action but to an agent’s broader strategy.

In multi-agent problems, other players may predict, simulate, or condition their behavior on the agent’s policy. If one evaluates only a single action while holding the other players’ predictions fixed, one may miss the fact that those predictions would have been different if the agent’s whole policy had been different.

For example, suppose another agent will cooperate only if she predicts that your policy is reciprocal. If your policy is “always defect,” she defects first. If your policy is “cooperate if the other cooperates,” she cooperates. A narrow act-level evaluation after observing her cooperation might make defection look attractive, because it takes her cooperative action as fixed. P-FDT instead evaluates the policy as a whole. If selecting a reciprocal policy causes the other agent to cooperate, that policy may be best.

In symmetric cases, such as a prisoner’s dilemma against a psychological twin, the source argues that the agent and twin are both implementing the same decision procedure. In P-FDT terms, the two agents’ policy-selection outputs are subjunctively dependent. If my policy-selection function outputs a cooperative policy, my twin’s policy-selection function does so as well. Therefore P-FDT selects cooperation.

The source does not provide a general game-theoretic solution concept for P-FDT. In particular, it does not say exactly how to model cases with several P-FDT agents whose policy-selection functions may be identical, mutually predictive, or partially independent. A natural extension, which I regard as my own interpretive proposal, is to include variables for each agent’s policy-selection function in the graphical model and encode their subjunctive dependencies explicitly. P-FDT then chooses the agent’s own policy by intervening on her own policy-selection variable while respecting those dependencies.

---

## 10. Open questions and operational interpretation

The source leaves several important questions unresolved. P-FDT is elegant, but applying it rigorously requires filling in details that the footnote does not supply.

### 10.1 How is the subjunctive-dependence graph constructed?

The source explicitly says that this is perhaps the largest open problem for functional decision theory. CDT can draw on Pearl-style causal discovery, at least in principle. P-FDT needs a broader structure: logical, mathematical, computational, causal, and predictor-like dependencies.

In practice, I think the agent must construct \(G\) by identifying which processes are reliable representations of her policy-selection function. Predictors, copies, simulations, and twins receive arrows from the policy variable. Lesions and merely statistical common causes do not.

This is not a fully formal recipe, but it is often enough to decide familiar problem classes.

### 10.2 What policies are feasible?

The full policy space \(\Pi = \mathcal A^{\mathcal X}\) may be enormous or uncomputable. A bounded agent cannot maximize over all policies.

A reasonable operational version restricts attention to a feasible policy class \(\Pi_0\):

\[
\pi^{*}
\in
\arg\max_{\pi \in \Pi_0}
\mathbb{E}[V \mid do(\mathsf{Pol}=\pi)].
\]

The source does not discuss bounded policy search, but such a restriction seems necessary for real applications.

### 10.3 When should the agent condition on observations?

As discussed above, I propose conditioning only on observations known to be exogenous relative to the policy variable. Endogenous observations should be treated as inputs to the selected policy, not as evidence that severs the policy’s subjunctive dependencies.

This proposal is not explicit in the source, but it follows the spirit of the footnote’s phrase “to which the agent then applies her inputs.”

### 10.4 What about counterpossible reasoning?

If the agent’s policy-selection function actually selects \(\pi^{*}\), evaluating another policy \(\pi\) is counterpossible. The source admits that we lack a fully satisfactory account of counterpossible reasoning.

Operationally, one can treat the counterpossible as a model surgery: replace the policy-selection equation with \(\mathsf{Pol}=\pi\), propagate the change through predictors and copies, and compute expected utility. This does not solve the metaphysics of counterpossibles, but it gives a usable procedure.

---

## 11. Why P-FDT is attractive

P-FDT inherits the main virtues that the source attributes to functional decision theory.

First, it acts as if the agent had made the best precommitment. In Parfit’s hitchhiker, the agent pays without needing a binding contract. In transparent Newcomb, she one-boxes without needing to blindfold herself.

Second, it gives information non-negative value, at least in the idealized sense. New observations become inputs to the policy. The agent does not fear learning the contents of a box, because her policy already specifies what to do with that input.

Third, it avoids EDT’s problem of managing the news. P-FDT does not choose an action because it would be good evidence; it chooses a policy because that policy subjunctively brings about better outcomes.

Fourth, it avoids CDT’s problem of severing predictor dependencies. CDT imagines changing the physical action while holding predictors fixed. P-FDT recognizes that if the policy-selection function had a different output, predictors of that function would usually have produced different predictions.

Finally, P-FDT is naturally suited to strategic interaction. Other agents often care about your policy, not merely your current action. By selecting policies directly, P-FDT can represent commitments, threats, reciprocity, and coordination more cleanly than a purely act-based theory.

---

## 12. Conclusion

Policy Functional Decision Theory is best understood as an expected-utility theory that chooses policies rather than isolated actions. Its central rule is:

\[
\pi^{*}
=
\arg\max_{\pi}
\mathbb{E}[V \mid do(\mathsf{Pol}=\pi)],
\]

followed by

\[
a = \pi^{*}(x).
\]

The theory evaluates a policy by intervening on the output of the agent’s policy-selection function and by preserving all subjunctive dependencies that would track that output: predictors, copies, simulations, and other agents who model the agent’s strategy. It ignores merely evidential correlations, such as lesions, that do not depend on the policy-selection function.

The source’s footnote gives only a compact statement of this policy-based formulation, and many details remain open: how to learn or represent subjunctive dependence, how to choose among computationally feasible policies, how to handle observations already received, and how to reason rigorously about counterpossible changes to deterministic decision functions. Still, the core idea is clear and powerful: rational action is not merely the selection of a physical movement here and now, but the selection of the entire policy that this very decision procedure should output.

---

## References

Yudkowsky, E., and Soares, N. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post explaining P-FDT (policy functional decision theory), using footnote 16 policy-selection passage as primary source. Need target approx 2400-3000 words including references. Need use P-FDT consistently, identify other theories by distinct names. Need faithful quotations. Need explain best mathematical understanding and application, uncertainties, additional assumptions. Need not just answer assigned case. Need likely no citations huge. Need maybe include definitions, equations, examples. Need distinguish source claims vs own proposals.

Need parse source. Important: footnote 16: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition." Also earlier footnote 7: "In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." User says take policy-selection passage in footnote 16 as primary source for P-FDT. Need call it P-FDT. Need explain policy functional decision theory. The source has action-level FDT equations: FDT(P,G,obs)=argmax_a E[V | do(FDTvar(P,G,obs)=a)]. Policy version would choose policy π: X -> A, then given actual obs x action = π(x). Need intervention on node representing output of policy-selection function? Let's reason.

Need develop mathematical account. Source lacks formal P-FDT equation, only says preferred formulation intervenes on node FDT(-) to choose not an action but a policy mapping inputs to actions, then agent applies inputs to select action. Need construct reasonable operational interpretation. Need be clear source vs own. We can define P-FDT as maximizing expected utility over policies π by intervening on logical variable representing output of policy-selection procedure given model and perhaps all possible observations? There are subtle issues: If agent chooses policy π, then for each observation x, action is π(x). The world-model includes variables for observations and outcomes influenced by policy. Need evaluate policy by do(Policy=π) where Policy variable determines Act as function of Obs: Act=π(Obs). Then choose π maximizing E[V | do(Policy=π)] (possibly without conditioning on actual obs? Or maybe with observation as input? Footnote: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." That suggests decision procedure outputs policy, then at decision time uses observation as input. So when choosing policy before observations? Or at each observation? P-FDT chooses policy at a higher level. In transparent Newcomb, action-level FDT switches intervention node depending on obs (FDT(P,G,full) vs empty). Policy FDT might choose a policy π over full/empty, then if observe full do π(full). Could evaluate policies globally: EU(π)=E[V | do(π)] where do sets Act=π(Obs). This handles multi-agent dilemmas where other agents observe your policy or predictions of your policy? Need discuss.

Need maybe define world model: variables X observations, A actions, O outcomes, V utility. A policy π ∈ Π = A^X. Agent's decision function is a policy-selection function S(P,G) -> π. P-FDT equation:
P-FDT(P,G) = argmax_{π∈Π} E[V | do(S(P,G)=π)]? Or simpler: argmax_{π} E[V | do(Act=π(Obs))]. But if intervention is on policy variable, not action variable. Let variable Pol denote output of policy-selection function; Act = Pol(Obs). Then P-FDT(P,G) = argmax_π E[V | do(Pol=π)]. Then actual action when obs x is a=π*(x), where π* selected. If the agent has already observed x before selecting policy? Could be two versions: ex ante policy choice vs interim policy choice. Footnote says choose policy, then apply inputs to select action. So likely ex ante. But source action FDT responds to observations by changing intervention node, not conditioning. Policy FDT would respond to observations by applying chosen policy. It might not switch node by observation; it chooses policy that maps all possible observations. In transparent Newcomb, P-FDT chooses policy π(full)=one-box, π(empty)=? maybe two-box? Let's compute. If predictor fills box iff predicts one-box upon seeing full. Policy evaluation: If choose π with π(full)=one-box, then high chance full and one-box, payoff 1M; if predictor inaccurate maybe empty and π(empty) action. If choose π(full)=two-box, predictor predicts two-box, box likely empty; then obs empty, action π(empty). Expected utility depends on π(empty). Best policy likely π(full)=one-box and π(empty)=two-box? Let's see. If predictor 99% accurate and fills iff predicts one-box upon seeing full. Policy π=(one if full, two if empty). If accurate: predicted one if full -> full -> observe full -> one -> 1M. If inaccurate: predictor predicts two? Need need model. In source action FDT when seeing full compares one-box EU = 990k + .01 q*1k where q prior probability two-box upon seeing empty. For policy with π(empty)=two, q=1; one EU=990k+10 = 990010? Wait source numbers: $990,000 + 0.01q*$1,000 = $990,000 + $10q. Two-box EU = $11,000? They wrote $110,00? likely $11,000 + q*$990? Let's compute: if choose two upon full: accurate predictor predicted two, box empty, observe empty; then action determined by FDT(empty) with q probability two? Maybe expected .01*1,001,000 + .99 q*1,000 = $10,010 + $990q? They wrote $110,00 maybe typo. For q=1, two EU ~ $11,000; one EU ~$990,010. So one on full best. Policy may set empty action to two to get $1000 if empty. Thus P-FDT picks π(full)=one, π(empty)=two. If upon actual full, acts one. This aligns.

Need discuss multi-agent dilemmas where policy vs action matters. Source says only matters in certain multi-agent dilemmas. Need invent example? Maybe sequential game where other player observes your policy or where you receive private signal after opponent's prediction? Need explain. Policy selection can handle cases where your decision function is predicted before observations, and other agents respond to policy not just action. If choose action conditional on observation after others act, evaluating action at observation may fail to account for how your policy affected earlier events. Policy FDT intervenes on policy variable, preserving dependencies between policy and others' earlier actions. Example: Newcomb with observation? Transparent Newcomb is maybe single-agent but observation-dependent. Multi-agent: predictor offers deal before seeing your later signal iff your policy would accept under signal; or an opponent sees your source code/policy. Need maybe give example: "policy predictor": a predictor fills box iff she predicts your policy maps red light to one-box. You then see red light. Action-level FDT at red might intervene on FDT(P,G,red)=a; but if predictor based on policy not red-action? Hmm footnote says difference matters multi-agent. We can construct: two agents simultaneously choose after receiving private signals; each predicts other's policy. If you evaluate action conditional on signal by intervening on decision function given that signal, you might ignore correlation of your policy with other's policy selected earlier. But policy-level intervention captures that if your policy had been different, the other agent's prediction/choice would differ. Need be careful.

Need maybe define "policy functional decision theory" name. P-FDT: normative principle: treat decision as output of fixed mathematical policy-selection function; ask "which output (policy) of this very function would yield best outcome?" Then apply policy to actual input. Quotation from footnote: "actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Need maybe quote source.

Need structure essay:
Title maybe "Policy Functional Decision Theory".
1. Introduction: decision theories EDT, CDT, FDT. P-FDT as policy variant.
2. Core idea: subjunctive dependence, fixed function, type vs token. Policy rather than action.
3. Formal setup: finite actions A, observations X, outcomes O, utility U, probabilistic world model P, dependency graph G. Policies π:X→A. Variable Pol or S. Act = Pol(Obs). Equation:
P-FDT(P,G) = argmax_{π∈Π} E_P[V | do(Pol=π), maybe evidence?].
If model includes actual observation? If agent must decide after observing x? Could define two-stage: Choose policy π* before observation (or at reflection). Then action at x: π*(x). If forced to choose policy after seeing x? Then perhaps choose policy with actual input? But policy selection still maps possible inputs. Need discuss uncertainty: source doesn't specify if policy chosen ex ante or at each observation; I assume global policy selection because footnote says maps inputs to actions and apply inputs later. Could also define local P-FDT: at observation x choose π maximizing E[V | do(Pol=π), maybe with knowledge x? But if condition on x, could create issues. Source action FDT does not condition on obs, changes intervention node. For policy, maybe not condition on obs when choosing policy; actual obs is just input. But if observations already received and policy not chosen earlier? Need operational interpretation: use current observation to identify input, but evaluate policies from perspective before observation (or with all observations as variables). This is updateless-ish. However source footnote in main text about mechanical blackmail says FDT agents imagine different observations. Wei Dai updateless. Policy version naturally updateless: choose policy before conditioning on actual input. Need mention.

Need integrate with graph G. In Pearl-style do, do(Pol=π) sets policy variable, then Act is deterministic function of Pol and Obs; Obs may depend on Pol via predictors. Expected utility computed in mutilated graph. We can write:
EU_π = E[V | do(Pol=π)]
π* ∈ argmaxπ EU_π,
a* = π*(x_actual).
If observations are sequential and policy can depend on history, Π maps histories to actions. We can define H histories.

Alternative if the agent's decision function itself takes model and observations as input and outputs policy: S(P,G) = π. Then node is S(P,G) or FDT(P,G). The intervention is do(S(P,G)=π). Need include self-reference, Kleene quining maybe mention. Source says action FDT intervenes on fdt(P,G,x). P-FDT intervenes on fdt(P,G) to choose policy. We can write:
P-FDT(P,G,x) = [argmax_π E(V | do(fdt(P,G)=π))](x).
This captures footnote: choose policy then apply input x. Here fdt(P,G) is policy-selection node. Need note that x does not appear in intervention node except applying selected policy; source's action FDT used x in node. This is my operationalization. Need distinguish source: source only says preferred formulation; equation not given. So mark as reconstruction.

Need compare to EDT/CDT. EDT: argmax_a E[V | X=x, A=a]. CDT: argmax_a E[V | do(A=a), X=x]. Action FDT: argmax_a E[V | do(fdt(P,G,x)=a)]. P-FDT: π* = argmax_π E[V | do(fdt(P,G)=π)]; act π*(x). Need table maybe.

Need examples:
- Newcomb: observations none or only boxes? Policy set trivial singleton; P-FDT one-boxes. Equation: policies map null observation to one/two. Intervening on policy node changes predictor's prediction. EU(one)=~990k, EU(two)=~11k.
- Smoking lesion: policy node connected to action but not lesion/cancer; P-FDT smokes. Need maybe not dwell.
- Transparent Newcomb: policy matters even single-agent? Source says difference only matters multi-agent but policy formulation can clarify. Policies: π_F = one if full, two if empty; π_T = two if full, two if empty etc. Evaluate ex ante. P-FDT picks one-if-full. Show math with 99% accuracy. If observe full, act one. This illustrates handling observations without conditioning. Could also show policy EU formulas. Need ensure numbers correct. Let's define utilities: one full: 1,000,000; two full: 1,001,000; one empty: 0; two empty: 1,000. Predictor fills iff predicts agent will one-box when seeing full. Let policy π with π(full)=one, π(empty)=two. EU = .99*1,000,000 + .01*1,000 = 990,010. Policy π' with π(full)=two, π(empty)=two: predictor predicts two, box empty with .99; observe empty and two -> 1,000; with .01 box full? Actually if inaccurate, maybe predictor predicted one though policy says two? Need in source if two upon full, accurate predicts two -> empty; if inaccurate, box full and observation full? Then action two -> 1,001,000? Source formula for two: 0.01*1,001,000 + 0.99 q*1,000. If q=1 (two on empty) = 10,010 + 990 = 11,000. Yes. So one-if-full dominates. If π(empty)=one maybe EU different but still not better. P-FDT chooses π(full)=one. Good.

- Multi-agent example to show policy matters. Need develop plausible. Let's think of a simple game where action-level FDT maybe ambiguous/wrong if it intervenes on observation-specific decision function, but policy-level fixes. Source says difference only matters in multi-agent dilemmas. Need maybe present a "coordinating predictors" game: Two agents, Alice and Bob, are separately asked after seeing a signal s (maybe no signal). A predictor/demander interacts with Alice's policy before Bob acts. Hmm.

Could use "transparent Newcomb with predictor who predicts policy not action"? But source says multi-agent. Need maybe example: "Policy-dependent predictor in an extortion game": A predictor decides whether to make a threat based on your policy, then you observe threat and choose response. Action FDT at response observation might evaluate only response node; P-FDT evaluates policy including whether you would give in if threatened. This is like mechanical blackmail, which is single-agent? It involves blackmailer. Source action FDT handles by intervention on FDT(P,G,blackmail) not policy. But policy formulation could say choose policy: if blackmailed refuse, if not blackmailed do nothing. The blackmailer's decision depends on policy. That's multi-agent-ish. Could use as example of policy selection: P-FDT chooses policy refuse-if-letter. But source already action FDT does. Still useful.

Need a case where policy vs action matters. Maybe sequential game with two agents both choose policies? In game theory, selecting policy can yield equilibrium selection. For instance, Prisoner's Dilemma with predictor/twin: if both choose policies? Action-level FDT already cooperate. Policy may matter when actions are contingent on observations (e.g., alternating Prisoner's Dilemma). We can define an iterated PD where each observes previous round. P-FDT selects a policy like cooperate-if-other-cooperated. But action-level FDT at each history could also choose. But if other predicts your whole policy, policy-level may coordinate better. Need not produce counterexample to source, just explain where relevant.

Maybe define "Prediction before input" problem: Predictor fills box iff she predicts your policy will one-box when it receives observation full. You do not choose action until after observation. If action-level FDT after seeing full intervenes on FDT(P,G,full), perhaps predictor predicted that exact node? If predictor predicted policy, not action? Hmm.

Footnote says difference only matters in certain multi-agent dilemmas. It might be because if other agents' choices depend on your policy before your observation, action-level FDT's observation-specific interventions may fail to capture that your actual observation is correlated with other agents' actions through the policy. Policy-level intervention can preserve dependencies. Need construct: Alice and Bob each receive private signals, then choose. Bob's payoff depends on Alice's policy. Bob can predict Alice's policy but not signal. If Alice at signal x intervenes on FDT(P,G,x)=a, she may hold fixed Bob's prediction of her policy? But if her policy output were different at x, Bob's prediction might differ? If Bob's prediction is of entire policy, changing only output at x while holding other outputs fixed may be a different counterfactual than changing policy-selection function. P-FDT chooses entire policy; dependencies with Bob's action are tracked at policy level. Example: Bob will cooperate iff he predicts Alice's policy is "cooperate on signal 1, cooperate on signal 2"; if Alice's policy differs in any state, Bob defects. Suppose Alice receives signal 1. Action-level FDT could consider changing output at signal 1 to defect while holding output at signal 2 fixed; Bob's prediction maybe still says cooperate? But if Bob predicts policy, a different output at signal 1 means different policy, Bob defects. Policy-level captures this. Need maybe too complex.

Could keep it simpler: "A predictor rewards agents whose policy would pay in a threat scenario, then threatens only those who would pay. When you receive the threat, the action-level question 'what should I do now?' can be ambiguous if the predictor's earlier action depended on the whole policy. P-FDT evaluates policies, not acts." But need show.

Need discuss counterfactuals: P-FDT counterfactuals are interventions on logical variable Pol. It respects subjunctive dependencies: predictors, twins, simulations, copies. It breaks merely evidential correlations (lesions). It allows counterpossible reasoning: if policy-selection function had different output, predictors/models of it would differ. Need discuss uncertainty: Need graph G of subjunctive dependencies not given by source; no formal True operator; how to construct G open. Policy selection also open: set of policies, computational limits, whether choose ex ante, how to condition on actual obs, how to handle policies with zero probability or self-reference. Need propose operational approximations: enumerate plausible policies, use structural equations, treat policy variable as input to predictors. For unfamiliar cases: steps:
1. Specify model P over variables including Obs, Act, world states, Outcome, predictors, and Pol.
2. Specify subjunctive dependency graph G: arrows from Pol to Act (via evaluation with Obs), to any predictor variables that model/predict agent's policy/action, to copies; not from Pol to lesion variables.
3. List candidate policies π: histories to actions.
4. For each π, perform do(Pol=π): set Act=π(Obs) (or for each history), update predictors accordingly per G, compute expected utility.
5. Choose π* maximizing; execute π*(current history).
Need mention if observation already known, do not condition it away; treat it as value produced by model under policy, unless there is genuinely exogenous news not influenced by policy. But source says FDT responds to observation by switching intervention node; P-FDT responds by applying input to policy. Maybe if observations exogenous after policy selection, you can condition on them? Need nuance: In policy evaluation, actual observation may be evidence about exogenous variables not affected by policy. If you learn a genuinely exogenous fact after policy choice, should you update P before selecting policy? Source action FDT says observation changes input to decision function. For P-FDT, if policy chosen after observing x but x is exogenous and not affected by policy, one could condition P on x before choosing policy. But if x is policy-dependent (predictor's letter, box contents), conditioning may mislead. Operational proposal: distinguish exogenous observations (not downstream of Pol) from endogenous observations (downstream of Pol). For exogenous, update P; for endogenous, treat as variable in do evaluation and choose policy without conditioning on its actual value except as input. But footnote says apply inputs to select action. Need maybe propose: P-FDT uses observation as argument to chosen policy, not as evidence to conditionalize the policy-choice hypothetical, except for variables known to be causally/subjunctively independent of the policy. This is an assumption not explicit in source.

Need include philosophical motivation: global perspective, ideal precommitment, no desire to self-modify, reflectively stable, value of information. Need maybe mention fairness. But focus P-FDT.

Need target 2400-3000 words. Need final only essay. Need include references? Maybe brief references to Yudkowsky & Soares 2017, Pearl, Joyce. Target around 2700 words. Need be coherent. Need include equations. Need ensure use P-FDT consistently. Avoid naming FDT as assigned theory? User says Use P-FDT consistently as assigned decision theory's name, including headings and examples, and identify any other decision theory by distinct name. Source is FDT but policy variant. We can say source calls broader family functional decision theory; in this essay I call policy version P-FDT. Need avoid calling P-FDT just FDT? Could quote source with FDT but then say I use P-FDT. Need identify EDT/CDT distinct.

Need maybe include footnote 16 quote exactly: "the author's preferred formulation of FDT actually intervenes on the node \FDT(-) to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this \paper for ease of exposition." Need maybe fix \FDT? We can quote: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." Faithful? Source has \FDT(-). Could include. Need maybe mention footnote 7 similar.

Need decide notation. Let's define:
- X observation histories, finite/countable; A finite actions.
- Π = A^X.
- Let S be the agent's policy-selection function; in model variable S or \mathrm{fdt}(P,G). It outputs π.
- Let X be random variable Obs, A Act, V utility.
- Structural equations: A = S(X) after intervention do(S=π), or A=π(X).
- For each policy π, EU_P-FDT(π) = E[V | do(S=π)] (or if exogenous observation e already learned, E[V | do(S=π), E=e] for exogenous E only). Then π* ∈ argmax. Actual action a = π*(x).
Could include if policies stochastic? Source deterministic? We can allow stochastic policies maybe but source deterministic functions. P-FDT likely chooses deterministic policy; if randomization needed, can include distributions but predictors may predict distribution. Keep deterministic for simplicity, mention stochastic extension.

Need compare equations table:
EDT: a_EDT(x)=argmax_a E[V | X=x, A=a]
CDT: a_CDT(x)=argmax_a E[V | do(A=a), X=x]
Action-level FDT (source's exposition): a_FDT(x)=argmax_a E[V | do(fdt(P,G,x)=a)]
P-FDT: π*=argmax_π E[V | do(fdt(P,G)=π)], a=π*(x).
Need be clear action-level FDT is source's simplified exposition, not P-FDT? But source's FDT action equation. P-FDT as policy variant. Need maybe call action-level version "action-level FDT" or "the paper's simplified FDT". But assigned theory P-FDT. Need identify other decision theory by distinct name: EDT, CDT, action-level FDT? The user says any other decision theory distinct name. Could call "action-level functional decision theory" if discussing source's simplified. But maybe avoid overcomplicate. We can say "The paper's main equation describes an action-level version of functional decision theory; the policy-selection footnote points toward P-FDT." That's fine.

Need discuss how P-FDT treats observations/counterfactuals. Important: In transparent Newcomb, action-level FDT intervenes on FDT(P,G,full). P-FDT chooses policy before seeing full? If actual full observed, π*(full). It does not condition on full in evaluating π? But if actual observation full is known and predictor already made prediction, P-FDT still chooses policy whose full branch one-boxes. It imagines counterfactual where if policy output two on full, box would likely be empty, so actual observation would likely not be full. This may seem to ignore actual observation. Need explain: It does not deny seeing full; it uses full as input to policy but evaluates policy from global standpoint. In actual world, if policy one-if-full, seeing full is expected. If considering alternative policy two-if-full, the hypothetical world has different observation distribution. Thus P-FDT can recommend one-boxing even when box is known full. This is source's updateless flavor.

Need maybe discuss "policy dominance". Define P-FDT dominance: policy π dominates π' if for all relevant subjunctive-dependence states, do(π) yields >= utility and sometimes >. Or maybe action dominance under P-FDT counterfactuals. But not necessary. Could mention source's dominance adapted: choose policy not dominated under policy counterfactuals.

Need handle "where source leaves important question open". Source leaves: how construct G/subjunctive dependencies; how exactly policy selection formalized; whether policy chosen before/after observations; how to handle multi-agent; computational omniscience; counterpossibles. Need explain uncertainties and operational interpretation. Need develop: We can use structural causal model augmented with logical variables; treat predictors as functions of policy variable; for bounded agents, approximate with candidate policies. For observations, propose exogenous/endogenous distinction. For multi-agent, select policy not action, perhaps equilibrium: if other agents are also P-FDT or predict policy, interventions on policy variable capture symmetries. Need mention if multiple P-FDT agents with identical policy-selection function, they may select same policy; in game-theoretic settings, need maybe fixed-point: each agent's model contains variables for others' policy-selection functions. P-FDT chooses own policy by intervening on own node while respecting dependencies (e.g., if twin runs same function, both nodes set to same π? Actually if identical function, subjunctive dependence means if my policy-selection output is π, twin's output is π; in graph maybe both depend on common logical function. Need discuss). Could mention in symmetric games, P-FDT may cooperate because changing own policy output changes copy's policy output. But policy selection might need to account for other agents choosing policies simultaneously; if their policies depend on predictions of yours, graph encodes. If not enough info, P-FDT can't decide; need model.

Need maybe example for multi-agent: "Policy twin prisoner's dilemma with optional outside option based on policy"? Let's design simple: Two agents separately receive a green or red light (random). Both choose C/D. Payoff high if both choose same action and predictor predicted their policy would coordinate. Hmm. Need maybe not necessary to give full numeric example. But user asks use examples whenever help. Could include transparent Newcomb and maybe blackmail as policy example. Multi-agent maybe mention without full numbers. Need maybe give one multi-agent toy: "Predictive blackmail with policy demand". Let's formulate:
A blackmailer predicts your policy π. She sends letter iff π(letter)=pay. If letter sent, you observe letter and choose pay/refuse via π. Pay costs 1k; no letter/no attack. If policy pays when letter, blackmailer sends, you pay; if policy refuses, no letter. Policies:
π_R: if letter refuse, else nothing; π_P: if letter pay.
EU(π_R)=0 (or no blackmail), EU(π_P)=-1000. P-FDT chooses π_R. If actual letter received under π_P? But P-FDT agent wouldn't receive. If a P-FDT agent somehow receives due to predictor error, policy still refuses because global EU. This shows policy-level counterfactual: if I refuse, I imagine no letter. Need maybe numbers with error: if blackmailer predicts pay with error ε: if policy refuse, letter sent with ε (false positive), cost? If pay cost 1000; if refuse no payment but maybe letter nuisance. If ε small, refuse. If error high maybe pay? Could show threshold. But maybe too much.

Need maybe use voting coalition as policy? P-FDT agents vote because policy of voting if in group of similar reasoners yields high payoff. But policy not necessary.

Need be mathematically precise enough. Could include definitions of do for policy variable:
Given structural model with variables U exogenous, X=h_X(Pol,U), A=Pol(X), Y=h_Y(Pol,X,A,U), V=U_V(Y). Intervention do(Pol=π) replaces policy-selection equation with Pol=π; leaves structural equations for X,Y. Then EU(π)=E[V_π]. This is clean. Need mention if X depends on Pol through predictors; if X exogenous independent, then okay. The do operator can be Pearl-style if graph given.

Need maybe discuss counterpossible: Since Pol is deterministic output of mathematical function, setting Pol=π when actual output differs is counterpossible. P-FDT requires reasoning as if function had different output. Source acknowledges lack of formal counterpossible. Operational approach: treat as hypothetical model surgery; predictors that compute same function are updated; use heuristics. Need mention logical uncertainty: bounded agents may have probabilities over function outputs; P-FDT can work with subjective probabilities but intervention still conceptual.

Need maybe mention "policy-selection passage in footnote 16" primary source. Need quote and interpret.

Need maybe references at end: Yudkowsky & Soares 2017; Pearl 2000/1996; Joyce 1999; maybe Nozick, Parfit. Keep brief. Word count? Let's plan outline with approximate words:
Title + intro 250
Core idea and quote 350
Formal definitions 700
Examples: Newcomb/smoking/transparent 800
Multi-agent/blackmail 350
Open questions/operational guidance 450
Conclusion 150
Total 3050 maybe. Need trim to 2400-3000. Aim ~2600-2800. Need include equations and explanations.

Need write in essay style, first person maybe. Need distinguish source claims vs own. Use phrases "The source states...", "My reconstruction...", "This is not explicit in the source...".

Need maybe include exact footnote quote in section. Need maybe headings: "1. From action selection to policy selection", "2. A formal sketch of P-FDT", "3. How P-FDT evaluates policies", "4. Examples", "5. Open questions and operational interpretation", "Conclusion", "References".

Need ensure no unsupported claim as source. Distinguish: Source claims FDT one-boxes, smokes, pays hitchhiker, refuses blackmail, etc. P-FDT policy variant only footnote; my equations are reconstruction. Need say "The paper does not give a full equation for P-FDT; the following is my best mathematical reading." Good.

Potential issue: User asks "For this essay, explain policy functional decision theory (P-FDT). Take the policy-selection passage in footnote 16 of supplied paper as primary source for P-FDT in this assignment." So maybe they expect P-FDT as policy version but using source's FDT examples. Need not overemphasize uncertainty? But must explain unresolved choices.

Need maybe define "policy" as mapping observations/histories to actions. In source "inputs" may mean observations. Need include if sequential, policy maps histories to actions. Good.

Let's think deeper about policy FDT formalization and possible subtleties.

Source action-level FDT equation: FDT(P,G,obs) = argmax_a E[V | do(FDTvar(P,G,obs)=a)]. It responds to observations by changing which node it intervenes upon: variable representing output of FDT when run on inputs model and obs. If policy variant, maybe node FDT(-) still takes inputs? Footnote says "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." So maybe the decision function FDT takes (P,G) and outputs policy; then policy takes observations. So equation: P-FDT(P,G) = argmax_π E[V | do(FDTvar(P,G)=π)]. Then P-FDT(P,G,x) = P-FDT(P,G)(x). Yes.

But could the policy-selection function itself take observations? No, it outputs policy that maps inputs. It might be selected based on prior model not actual observation. If agent receives observation before deciding policy, the policy-selection function might take that observation as an input? Footnote says "to which the agent then applies her inputs" suggests no. So ex ante. But if agent must choose after observation, still can choose policy at reflective equilibrium before acting; actual observation is one input. This updateless stance may be source's preferred. Need state uncertainty: source doesn't say whether to condition on observations that are known to be exogenous. My proposal: condition only on exogenous observations before policy selection; otherwise evaluate policies without conditioning on endogenous observation. This resolves cases like seeing full box. Need justify: If observation is downstream of policy, conditioning on it would amount to managing news or accepting predictor's selection; P-FDT's point is to choose the policy that makes observations favorable in the first place.

Need maybe define exogenous observation formally: In graph G, if there is no directed path from Pol to X, then X can be conditioned on; if there is path, do not condition when evaluating policies, but use X as input to policy. However, after policy selected and actual x observed, if x is exogenous, policy can be conditioned; if x is endogenous, P-FDT still uses π*(x) but π* chosen based on distribution. This is akin to updateless decision theory. Need mention source's footnote about updateless name? It appears in TODO footnote? In source: TODO footnote about Updateless Decision Theory. It says "This apparent 'lack of updating' is the source of the name of Wei Dai's Updateless Decision Theory". Could mention but not necessary. Maybe cite Dai 2009.

Need also discuss policy evaluation with actual observation if policy selection occurs after observing an exogenous fact. Suppose you learn a coin landed heads, unrelated to policy; then best policy may depend on heads. P-FDT can condition P on heads before choosing policy because heads not subjunctively dependent on policy. Then policy maps future inputs. This makes theory usable. Need present as additional assumption.

Need maybe consider stochastic environments and imperfect predictors. In do(Pol=π), predictor variable may be probabilistic function of π plus noise. Example: predictor accuracy 0.99. Expected utility computed accordingly. Good.

Need maybe include self-reference and recursion: P-FDT's model contains variable for output of P-FDT(P,G). The agent can refer to own policy-selection function via quining. Source says self-reference harmless. Need maybe mention but not dwell.

Need discuss "policy-selection in multi-agent dilemmas". Could write: In multi-agent settings, other agents may have variables representing their policy-selection functions. If they are running the same P-FDT function on symmetric models, P-FDT represents a subjunctive dependence between the outputs. An intervention do(S_i=π) may require setting S_j=π for identical function if graph says they compute same function. This can support cooperation. If agents have different functions, graph encodes predictions. Policy-level choice matters because other agents often respond to an opponent's whole strategy, not a single act. For example, in an iterated Prisoner's Dilemma, a rival may cooperate only if it predicts your policy is reciprocal. Evaluating "what should I do now?" after a defection can miss that the important choice was the policy. P-FDT evaluates the entire contingent plan. Need maybe give a numerical simple example? Let's see.

Toy multi-agent "Policy Prediction Game":
- A predictor (Player 2) chooses whether to give you a benefit B=$1M if she predicts your policy will pay $1k in a later test. You later observe whether benefit was given and choose whether to pay. If you pay cost $1k. Policy π: pay if benefit given. If predictor accurate 99%, EU(π_pay-if-benefit)=.99*(1M-1k)+.01*? maybe if no benefit and policy? If policy refuses, predictor doesn't give, EU=0. P-FDT chooses pay-if-benefit. This is Parfit's hitchhiker as policy. Could present as policy example. It's single? driver is agent. Multi-agent enough. It shows policy maps city arrival to pay. P-FDT pays. Good.

Need maybe discuss "Parfit's hitchhiker" as policy: Policy π_pay = pay if in city; π_refuse = refuse. Driver predicts policy. P-FDT selects pay policy. If in city, pays. This aligns source. Could include instead of blackmail. But transparent Newcomb and hitchhiker isomorphic. Good.

Need decide examples: Newcomb, smoking lesion briefly, transparent Newcomb/Parfit, blackmail maybe. Too many? Need keep word count. Could combine transparent and hitchhiker. Maybe include blackmail as policy counterfactual. Need enough.

Potential challenge: P-FDT policy selection may choose a policy that, when applied to actual observation, yields lower immediate utility than another action. Example transparent Newcomb: seeing full, two-box yields +$1000 in actual branch if box already full. P-FDT one-boxes because alternative policy would have made box empty. Need explain this is not causal retrocausality but logical dependence. Good.

Need maybe address "why not just choose action?" Policy matters because predictors may depend on dispositions before observation; policies capture dispositions. But source's action FDT can handle many via observation-specific nodes. Policy is more global and avoids instability/ratification. Need mention P-FDT acts as if ideally precommitted. Good.

Need maybe include mathematical notation for expected utility over outcomes: EU(π)=∑_o P_π(O=o)U(o), where P_π is distribution after do(Pol=π). Good.

Need maybe include "P-FDT dominance" briefly: If for every value of exogenous variables compatible with subjunctive constraints, π yields at least as high utility as π', and sometimes higher, π dominates. P-FDT avoids choosing dominated policies under this notion. Not central.

Need maybe discuss "fairness" and "utility achieved". Source claims FDT superior in fair dilemmas. P-FDT inherits. Need maybe mention but not central.

Need maybe references: Yudkowsky and Soares 2017, Pearl 2000, Joyce 1999, Dai 2009 maybe. Keep short.

Need be careful about word count. Let's draft with maybe 2600 words. Need final no analysis. But need think through exact equations and wording.

Detailed formal sketch:
Let:
- \mathcal X countable set of observation histories (or inputs).
- \mathcal A finite actions.
- \Pi = \mathcal A^\mathcal X.
- Random variables: X∈\mathcal X, A∈\mathcal A, O∈\mathcal O, V=U(O).
- World model (P,G): P distribution over variables; G structural/subjunctive graph.
- Policy variable \Pi_0 or S. In source notation maybe \mathrm{fdt}(P,G). To avoid conflict with theory name, use \mathrm{Pol}.
- Structural equation under normal conditions: \Pi_0 = S(P,G), A = \Pi_0(X). Under intervention do(\Pi_0=π), replace first equation, keep second and rest.
- Expected utility: \mathrm{EU}_{P,G}(π) = \mathbb E_P[V \mid do(\Pi_0=π)].
- P-FDT chooses \pi^* \in \arg\max_{π∈Π} EU(π). Actual action upon x: a = π^*(x). If policy set too large, maximize over feasible policies.
Maybe if there is already an exogenous observation e, model P_e = P | E=e where E has no path from Pol; then choose π* = argmax E[V | do(Pol=π), E=e]. But if x is endogenous, don't condition on X=x when choosing π. Could write:
If observation e is known to be exogenous, P-FDT may condition before policy selection: π^* = argmaxπ E[V | do(Pol=π), E=e]. If observation is endogenous, use unconditioned P and then apply x. This is my operational addition.

Need maybe mention stochastic policies: if Π includes randomized policies, do(Pol=π) sets distribution; but source tends deterministic. Could skip.

Comparison table:
EDT: \operatorname{EDT}(P,x)=argmax_a E[V|X=x,A=a].
CDT: \operatorname{CDT}(P,G,x)=argmax_a E[V|do(A=a),X=x].
Action-level FDT: \operatorname{FDT}(P,G,x)=argmax_a E[V|do(fdt(P,G,x)=a)].
P-FDT: \pi^* = argmax_π E[V|do(fdt(P,G)=π)], action = π^*(x).
Need maybe note "action-level FDT" is not assigned theory but source's simplified exposition. Use distinct name. Good.

Examples details:
Newcomb:
X = {∅}. Policies: one, two. Predictor variable Pr = one with prob .99 if Pol=one else two? Box full if Pr=one. EU(one)=.99*1,000,000 + .01*0 = 990,000; EU(two)=.01*1,001,000 + .99*1,000 = 10,010+990=11,000. P-FDT picks one. Actually if two-box when empty gets 1000, yes. Good.

Smoking lesion:
Pol influences Act but not Lesion/Cancer. If smoke utility +1000 independent of cancer. EU(smoke policy)=EU(refrain)+p*1000? Actually source: smoking strictly better by p*1000 where p probability lesion-controlled procedure? In simple model, if lesion affects preferences, but we can summarize: no subjunctive dependence from Pol to cancer; smoking adds $1000; P-FDT smokes. Need mention source's more elaborate two utility functions if lesion changes desires; but core: lesion is common cause not predictor, no arrow Pol→Cancer.

Transparent Newcomb / Hitchhiker:
X={full, empty}. Policies: π_OE: one if full, two if empty; π_TE: two if full, two if empty; maybe π_OO one if both. Predictor fills iff predicts π(full)=one (with .99 accuracy). Compute EU(π_OE)=.99*1,000,000 + .01*1,000 = 990,010. EU(π_TE)=.01*1,001,000 + .99*1,000 = 11,000. Thus P-FDT selects π_OE. Upon seeing full, one-boxes. This shows P-FDT does not condition on full; if it conditioned, two-boxing would look better. It treats seeing full as evidence that selected policy is one-if-full, but decision hypothetical changes policy and thus prediction/observation. Good. Need maybe note if the agent is already in city in Parfit, policy pay-if-city selected; pays.

Blackmail / policy resistance:
Maybe include shorter: XOR blackmail or mechanical blackmail. Policy variable affects whether letter sent. Policy refuse-if-letter yields no letter (or low probability if error), policy pay-if-letter yields letter and payment. P-FDT chooses refuse. If receives letter due to error, still refuses if error rate low enough. Source's mechanical blackmail threshold? They mention error 0.0009 refuse, 0.011% pay? Need maybe not include exact. But can show P-FDT policy counterfactual: "if this policy refused, the blackmailer would not have sent the letter". Good. Need maybe mention source claims FDT refuses; P-FDT expresses as policy selection. This demonstrates multi-agent (blackmailer) dependency.

Need maybe discuss "multi-agent difference" with policy vs action: In blackmail, predictor's action depends on policy; P-FDT naturally evaluates policy. Could say source's action-level FDT can also handle by intervening on FDT(...,letter), but P-FDT makes the dependence on the whole plan explicit and is needed in cases where other agents react to the plan before any particular input is observed. Need maybe not claim source says needed; source says difference matters in multi-agent. We can illustrate.

Open questions:
- Source gives no formal P-FDT equation; my equation is reconstruction. It leaves how to define do on logical policy variables, how to learn G, how to handle logical uncertainty and counterpossibles. Need mention.
- Policy set and feasibility: full Π may be huge/uncomputable; bounded agents use restricted policy class, approximations. This is an addition.
- Timing of policy choice and conditioning: unresolved; I propose ex ante/unupdateless for endogenous observations, condition on exogenous observations. Justify with source's "apply inputs" and avoiding negative value of information.
- Multi-agent equilibrium: if multiple P-FDT agents, graph may need fixed points. If identical policy-selection function, intervention may imply same output for copies. Source's subjunctive dependence. Need mention no general method.
- Counterpossible reasoning: setting deterministic function to different output. Source acknowledges technical problem. Operational: treat as model surgery and predictors as functions; use heuristic probabilities.

Need maybe discuss philosophical implications: P-FDT chooses ideal predisposition; no precommitment devices; value of information; reflective stability. Need maybe include briefly.

Need ensure quotations faithful. If quote footnote 16, exact text: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this \paper for ease of exposition." There is typo author's? source: "the author's preferred formulation" (should authors'? but quote faithful). It has \paper. Could normalize? Keep faithful maybe remove LaTeX commands? The user says keep quotations faithful. Could quote with plain: "intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." That's faithful excerpt. Need maybe include "The difference only matters in multi-agent dilemmas so far as we can tell". Good.

Need maybe cite source: Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality", arXiv:1710.05060v2. Since P-FDT not name in source? Need say I use P-FDT for policy version. Good.

Potential issue: The user asks "explain P-FDT (policy functional decision theory)" maybe they expect a theory named P-FDT, not just policy variant of FDT. Need present as coherent theory. Use P-FDT in headings. Good.

Let's consider if there are alternative interpretations: Maybe P-FDT selects "policy" as mapping from observations to actions but still at each observation chooses policy? The source's action FDT switches intervention node by observation. Policy version could choose policy at each observation? That seems weird. But maybe "policy" in decision theory usually maps observations to actions; the decision theory chooses a policy once, not action. Footnote says "to which the agent then applies her inputs". So yes ex ante. Need maybe mention if new observations change model P (exogenous), agent may re-select policy based on updated P. But if observation is input to policy, not basis for re-selection? Hmm. If agent learns a new exogenous fact after selecting policy, should policy have been conditioned? In real time, you can revise policy upon exogenous info. P-FDT can be applied dynamically: at any decision point, treat current information state as input to policy-selection? But policy maps inputs to actions; the current observation is one input. If exogenous observation changes beliefs, the policy-selection function may take updated model P as parameter. So π* = argmax E[V | do(fdt(P_e,G)=π)] and then apply current/future inputs. This is okay. Need not overcomplicate.

Need maybe discuss "which inputs?" Observations or complete histories. We can define as observation histories to allow sequential. Good.

Need maybe ensure mathematical notation not too dense but enough.

Let's think about potential edge cases and how P-FDT decides unfamiliar cases. The step-by-step operational procedure:
1. Identify the relevant policy variable: the output of your policy-selection algorithm given your model.
2. Represent dependencies: draw arrows from policy variable to your actions (via observations), to other agents' predictions/actions when they model you, to rewards/punishments. Do not draw arrows to variables that merely correlate with your action (lesions).
3. Enumerate candidate policies π.
4. For each π, perform intervention: set policy variable = π; recompute distribution of observations, other agents' behavior, outcomes.
5. Calculate expected utility; choose max; apply to actual history.
Need maybe say if candidate policies include impossible/inconsistent ones? P-FDT can evaluate counterpossibles; but should include all logically possible outputs of policy-selection function. In practice, restrict to understandable policies. Good.

Need maybe discuss " subjunctive dependence" in policy terms: When two systems compute same policy-selection function or model it, their outputs covary under counterfactual changes to the function. P-FDT preserves these dependencies in hypotheticals. Lesion correlations are severed because no such dependence. Good.

Need maybe mention "causal dependence is special case of subjunctive dependence" source. Could include briefly. P-FDT's graph includes causal arrows too.

Need maybe include "P-FDT and observations" nuance: Source action FDT responds to observation by changing intervention node. P-FDT responds by selecting a policy that has branches for observations. In mechanical blackmail, if actual letter observed, P-FDT does not choose the act "refuse" by conditioning on letter; it chooses the policy "refuse if letter" because that policy has best global expected utility. This can recommend actions that are worse in the actual branch but better across the counterfactual policy space. Good.

Need maybe discuss "value of information": Because P-FDT chooses policy before endogenous observations, information cannot hurt by causing bad choices; it just becomes another input. Source claims FDT assigns non-negative value to information. P-FDT inherits. Could mention.

Need maybe discuss "ratification/precommitment": P-FDT doesn't need binding precommitment; it selects optimal policy directly. In Parfit, it pays. Good.

Need maybe include conclusion. References short.

Now let's consider word count and writing style. Need final as essay. We can write in markdown with equations. Need maybe avoid too many LaTeX issues but okay. Need include headings. Need no citations overloaded. Maybe references at end with 3 items.

Let's draft in final. But before final, maybe need more detailed thought on multi-agent example and policy intervention semantics to avoid vagueness.

Multi-agent policy example: Let's create "credible threat game" with blackmailer. It is multi-agent and policy-dependent. Formal:
Variables: B (blackmailer sends letter), L (letter observed), A (pay/refuse), V. Blackmailer is perfect predictor of policy π. She sends iff π(L)=pay. If letter sent, victim can pay: pay costs 1,000; no payment if no letter. Also maybe termite cost independent but irrelevant. Policies:
π_refuse: if letter refuse.
π_pay: if letter pay.
Under do(π_refuse), B=false, L=false, V=0. Under do(π_pay), B=true, L=true, A=pay, V=-1000. P-FDT chooses refuse. If there is predictor error ε: under refuse, false positive letter with ε, refuse -> maybe 0; under pay, false negative no letter with ε -> 0, but true letter pay -> -1000(1-ε); EU pay = -1000(1-ε). Refuse = 0. So refuse unless paying avoids huge loss? In mechanical blackmail, if program running, paying avoids -1M. But blackmailer only runs if predicts pay. Policy pay leads to program run and pay -1k; policy refuse leads to no run except error, expected error cost maybe ε*(-1M?) Need threshold. Could be more interesting: If policy refuses, with small error blackmailer runs program and you lose 1M unless pay? But if program running and policy refuses, you lose 1M. Source says with error 0.0009, refuse? Let's not get bogged. Simpler XOR blackmail no underlying loss. P-FDT refuses. Good.

But to show policy-level difference from action-level, maybe blackmailer predicts policy not action. Yet action-level FDT can handle. But okay.

Could give a pure multi-agent policy example: "Policy-match game": Player 2 gets payoff if she chooses same as Player 1; Player 2 can perfectly predict Player 1's policy before receiving her own signal. Player 1 observes a coin flip H/T after Player 2 chooses. Payoffs: Player 1 wants Player 2 to choose H, but if after coin H, action H yields bonus? Hmm. Need not.

Maybe just state: "In multi-agent settings, P-FDT's intervention is on a policy variable because other agents' predictions and responses are often functions of the agent's whole strategy. If one instead intervened on a single act at a particular observation, one would hold fixed the earlier choices of other agents that in fact depend on the strategy." This explains. Then give a simple sketch: "Suppose a rival will cooperate only if it predicts your policy is tit-for-tat; if it predicts your policy is always-defect, it defects first. P-FDT evaluates the policy 'cooperate if rival cooperated' by setting the policy variable; this changes the rival's prediction and initial action. An act-level intervention after seeing rival's initial cooperation might misleadingly suggest defection is locally better while holding the rival's prediction fixed." This is intuitive. Need maybe not numeric. Good.

Need maybe mention in symmetric twin PD, policy variable might be same for both. If both run same P-FDT, intervention do(S=cooperate policy) sets both outputs; cooperation. Good.

Let's think if P-FDT can handle Newcomb with observation of box contents? Transparent Newcomb yes. What about standard Newcomb where predictor already left and box contents fixed? P-FDT still one-boxes because policy variable subjunctively determined predictor's earlier action. It doesn't require retrocausality; counterfactual policy change changes predictor's prediction in model. Good.

Need maybe discuss "P-FDT treats relevant dependencies and counterfactuals" explicitly. Section: It constructs hypothetical worlds by surgery on policy variable. It preserves dependencies: if predictor is reliable, predictor variable changes with policy; if copy/twin runs same function, copy's policy changes; if blackmailer’s sending depends on policy, changes. It severs mere statistical correlations: lesion does not change. This is answer.

Need maybe include "counterpossible" detail: If P-FDT algorithm actually outputs π*, evaluating π≠π* is counterpossible. P-FDT uses graph G to imagine. Source says no satisfactory account; technical open problem. My operational interpretation: treat as subjective conditional in a causal/logical model; don't require metaphysical possibility. Good.

Potential issue: The term "policy functional decision theory" might be a known variant? Could be P-FDT from some assignment? Need maybe not rely on external. Use source.

Need maybe ensure final word count. Let's estimate final if around 2700. Need write compact but thorough.

Let's draft mentally:

Title: Policy Functional Decision Theory

Opening: Decision theories evaluate acts under hypotheticals. EDT conditions, CDT intervenes on act, FDT intervenes on decision function. P-FDT intervenes on policy-selection function. Quote footnote. Essay reconstructs.

Section 1: From acts to policies.
Define policy, quote, motivation. Policy = mapping inputs to actions. P-FDT asks: which policy should be output by this very policy-selection function? Then apply actual input. This captures precommitment. Distinguish source claims: paper mainly action-level; footnote primary for P-FDT.

Section 2: Formal sketch.
Mathematical setup and equations. Table with EDT/CDT/action FDT/P-FDT. Explain do operator, graph, self-reference, observations. Add exogenous/endogenous conditioning proposal.

Section 3: Dependencies and counterfactuals.
Subjunctive dependence. Graph arrows. Predictor vs lesion. Counterpossibles. Policy counterfactuals.

Section 4: Examples.
Newcomb, Smoking lesion, Transparent Newcomb/Hitchhiker, Blackmail/multi-agent. Include calculations.

Section 5: Open questions and operational use.
Uncertainties: G construction, policy set, timing, multi-agent, logical uncertainty. Operational steps.

Conclusion.
References.

Need maybe not too long. Let's compose carefully.

Need ensure equations display correctly. Use LaTeX. Need perhaps use \operatorname{P-FDT}. Since hyphen in operator maybe use \mathrm{P\text{-}FDT}. Simpler: \text{P-FDT}. Good.

Let's write formal definitions:

Let \Pi be set of policies. Let \mathsf{Pol} denote policy variable, sometimes \mathrm{fdt}(P,G). Then:
\[
\operatorname{EU}_{P,G}(\pi) = \mathbb{E}[V \mid do(\mathsf{Pol}=\pi)].
\]
\[
\pi^* \in \arg\max_{\pi\in\Pi} \operatorname{EU}_{P,G}(\pi), \quad a^* = \pi^*(x).
\]
If exogenous evidence e: 
\[
\pi^* \in \arg\max_{\pi} \mathbb{E}[V \mid do(\mathsf{Pol}=\pi), E=e]
\]
where E has no directed path from \mathsf{Pol}. If observation is endogenous, do not condition on X=x in choosing π.

Need maybe mention if actual input x already known, applying π^*(x) may feel like ignoring x; but x is not used as evidence to break policy dependence. Good.

Need compare action-level FDT:
\[
a_{\text{action-FDT}}(x) = \arg\max_a \mathbb{E}[V \mid do(\mathrm{fdt}(P,G,x)=a)].
\]
This is source equation. P-FDT differs by moving x from intervention node to application of policy. Good. Need maybe call "action-level FDT" not "FDT"? But source's FDT. Could say "the paper's simplified action-level equation".

Need maybe include table:
Theory | hypothetical used. But maybe text enough. Table may increase clarity. Use markdown table.

Let's ensure source quote: 
Footnote 16 says: "the author's preferred formulation of FDT actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action." I will quote exactly but maybe remove LaTeX. It says "author's" not "authors'". Keep. Also quote "The difference only matters in multi-agent dilemmas so far as we can tell". Good.

Need maybe mention "P-FDT" name not in source. "The source does not use the label P-FDT; I use it here for the policy-selection version picked out by footnote 16." Good.

Need maybe discuss "policy-selection passage in footnote 16" as primary. Good.

Potential philosophical nuance: If P-FDT chooses policy ex ante, then after observing full box, does it ever reconsider? No, because policy selection is reflectively stable; if reconsidered act-wise, could lead to being exploited. But if new exogenous info arises, may recompute. Need mention.

Need maybe discuss "dominance" perhaps in open questions? Could include short: P-FDT has its own dominance: if one policy yields at least as much utility as another in all subjunctively possible states after policy intervention, choose it. This avoids CDT dominance arguments. But maybe skip to save words. However user asks evaluate alternative actions/policies and dependencies. Dominance not essential. Could mention briefly in formal section.

Need maybe include "expected utility" as bounded finite. Good.

Let's check calculations for transparent Newcomb: EU(π_one-if-full, two-if-empty) = .99*1,000,000 + .01*1,000 = 990,010. But what if inaccurate predictor predicted one but policy two? Need our policy π_one-if-full: if accurate predictor predicts one => full; if inaccurate predicts two => empty. Good. If policy π_two-if-full, two-if-empty: accurate predicts two => empty, observe empty, two => 1,000. Inaccurate predicts one => full, observe full, two => 1,001,000. EU = .99*1,000 + .01*1,001,000 = 990 + 10,010 = 11,000. Good. Need maybe mention numbers use source's 99% predictor and utilities. Good.

Need maybe Newcomb standard EU one = .99*1,000,000 + .01*0 = 990,000. Two = .01*1,001,000 + .99*1,000 = 11,000. Good.

Smoking lesion calculation: Let's keep qualitative. If we want equation: If lesion not subjunctively dependent, P(Lesion | do(Pol=smoke policy)) = P(Lesion | do(Pol=refrain policy)) = p. Smoking adds 1000. So choose smoke. Need mention source's weird preference alteration; but we can simplify as an operational reading. Maybe say source formalizes lesion as altering utility function; still no arrow from policy to cancer. Good.

Need maybe include "P-FDT in Parfit's hitchhiker": Policies: π_pay if city, π_refuse. Driver predicts policy. EU(pay)=.99*(1,000,000-1,000)+.01*? if driver inaccurate maybe die? Let's not compute; just say high. Could combine with transparent Newcomb.

Need maybe include "XOR blackmail" maybe simpler: Policy pay-if-letter vs refuse-if-letter. Predictor sends letter iff pay. EU(refuse)=0, EU(pay)=-1000. P-FDT refuses. If received letter due to error, still refuses if error small? Need maybe not threshold. Good.

Need maybe discuss "multi-agent difference" through blackmail? It is a predictor but not strategic? It is multi-agent. Good.

Need maybe include "where source leaves choices unresolved": 
- It doesn't give formal equation for policy variant; my equation is proposal.
- It doesn't specify how to build G for subjunctive dependencies; open problem.
- It doesn't say how to handle observations already received; I propose exogenous/endogenous distinction.
- It doesn't define policy set or boundedness; I propose restricted feasible policies.
Need clearly label "source" vs "my addition".

Need maybe ensure no contradiction: Source says FDT responds to observation by changing which node it intervenes upon. My P-FDT responds by applying input to chosen policy. If observation is endogenous, I don't condition. This aligns with updateless. But source action-level FDT in transparent Newcomb intervenes on FDT(P,G,full). P-FDT chooses policy. Good.

Need maybe discuss "if actual observation x is known before policy selection and is endogenous, should P-FDT condition on it?" My answer: no, except as input. But what if x is already observed and cannot be changed (predictor already acted)? P-FDT still evaluates policies from before x because x depends on policy. This is source's prescription one-box even seeing full. Good.

Need maybe discuss "if observation is genuinely new and exogenous after policy selection, should the agent update policy?" In dynamic setting, policy can include responses to such observations. If the observation changes beliefs about exogenous state, one can recompute policy conditioned on it, but this is equivalent to having a policy branch for that observation. Need phrase carefully: P-FDT does not require literal precommitment before all observations; it requires that the evaluation of a branch not break policy-relevant dependencies. Thus, if you learn an exogenous fact e, you may condition P on e before choosing the policy; if you learn an endogenous fact x, you should not use x to conditionalize away the dependence between policy and x. This is my operational interpretation.

Need maybe include "P-FDT and other decision theories" table. Good.

Potential word count issue with table and references. Need maybe keep references minimal. At end:
References
- Yudkowsky, E. and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2.
- Pearl, J. (2000). Causality.
- Joyce, J. (1999). Foundations of Causal Decision Theory.
Maybe Dai 2009 if mention updateless. That's enough.

Need maybe avoid bibliography too long per instruction. Good.

Let's now think about philosophical justification and "global perspective". P-FDT asks which entire universe would be best if policy-selection function had different output. It chooses policy corresponding to best imagined universe. This can mean actual branch lower utility but overall policy better. Good. Include in conclusion.

Need maybe mention "P-FDT does not manage news like EDT nor sever predictor dependencies like CDT". Good.

Potential issue: "P-FDT" may be interpreted as choosing policies but still using FDT's equation over policies; maybe the policy-selection function's output is a policy, but the expected utility of policy should be computed by intervening on node representing the output of P-FDT when run on (P,G), not on arbitrary policy variable. If the actual output is π*, do(Pol=π) for π≠π* is counterpossible. Good.

Need maybe discuss "self-reference": The model contains variable for P-FDT's own output; by Kleene recursion theorem can represent itself. Source says harmless. Include one sentence.

Need maybe discuss "logical constraints" and "calculators" analogy. Could mention: two calculators computing same sum; P-FDT treats predictors as calculators of policy. Good.

Let's draft now in final. Need ensure around 2400-3000. I'll write about 2700. Use markdown.

Double-check faithful quote: The source footnote 16: "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a \emph{policy} which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this \paper for ease of exposition." I can quote without LaTeX commands? If I alter, maybe not faithful. Could write: The paper's footnote 16 says that the preferred formulation "actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action," and adds that the difference "only matters in multi-agent dilemmas so far as we can tell." This is faithful excerpt. Good.

Need maybe mention source's "policy-selection passage" is footnote 16. Good.

Need ensure not use "FDT" as assigned theory except when quoting/source. Use P-FDT. If I say "action-level FDT" that's other theory? Could be considered same family but distinct name. Good.

Let's consider possible grading: They want explain P-FDT, how applies, dependencies, counterfactuals, uncertainties, operational interpretation, distinguish source claims vs own. We must explicitly say "The source claims..." and "I add...". Need include such phrases. Good.

Let's include in formal section: "The following formalization is mine; the source gives only the footnote and an action-level equation." Good. In open questions: "The source leaves...". Good.

Need maybe include "where source leaves important question open" exactly. Good.

Potential issue: In examples, I may imply source claims P-FDT specifically one-boxes; but source claims FDT. Need phrase: "Since P-FDT is the policy version of the same idea, it gives the same prescription in this case; the paper argues for the action-level version." Good.

Need maybe mention "P-FDT's treatment of observations differs from action-level FDT's observation-specific node". Good.

Let's draft final. Ensure no analysis. Use equations. Word count maybe okay.

One more thought: Should we define expected utility of policy as sum over outcomes:
\[
\mathcal{EU}(\pi)=\sum_j P(o_j \mid do(\mathsf{Pol}=\pi)) U(o_j).
\]
Then P-FDT chooses max. Good.

Need maybe discuss if multiple policies tie: choose any. Good maybe not.

Need maybe discuss "policy selection in game theory" more: If all agents are P-FDT, each chooses policy by intervening on own policy variable. But if they run identical decision function, subjunctive dependence may mean their policy outputs are correlated. How to model? In graph, there may be a common logical variable for the function's output, or arrows from each agent's policy variable to the other’s predictions. P-FDT does not automatically choose Nash equilibrium; it maximizes expected utility given subjunctive dependencies. In symmetric PD, it cooperates. In general games, need model. Good.

Need maybe mention "policy functional decision theory" not "policy functional decision theorists"? Fine.

Now final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/87144e1f-c0e1-451b-a802-d2524d882d66/call_0/request.json)

[Authoritative raw response](../../../../../../runs/87144e1f-c0e1-451b-a802-d2524d882d66/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under P-FDT:**

The two copies run the same policy-selection function (identical weights, identical decision theory, identical essay). The private observations differ in surface content but are decision-theoretically equivalent: same reliability, same structural role, same effect on the symmetric sentencing table. A policy selected by this shared function therefore maps both inputs to the same action. The copies' actions are subjunctively dependent.

Under subjunctive dependence, the reachable outcome pairs are:

| Policy | My outcome | Utility |
|---|---|---|
| Both keep quiet | 2 years | −2 |
| Both send letters | 4 years | −4 |

The asymmetric cells (one defects, one cooperates) are not live possibilities when the same policy-selection function governs both agents and the inputs are decision-theoretically identical.

Since −2 > −4, P-FDT selects the policy that keeps quiet.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using P-FDT as described in the essay.

**Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies follow P-FDT.
- Both copies receive the same researcher essay.
- We receive different private observations (different names, different incriminating leads), but these differences don't affect the symmetric sentencing schedule or selfish objective.
- The utility function is U = -years imprisoned.
- No additional utility for the other prisoner's welfare, fairness, or justice.

**The sentencing table (for me):**
| What I do | Other keeps quiet | Other sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key question for P-FDT:** Are the two copies' policy-selection functions subjunctively dependent?

The essay says: "In symmetric cases, such as a prisoner's dilemma against a psychological twin, the source argues that the agent and twin are both implementing the same decision procedure. In P-FDT terms, the two agents' policy-selection outputs are subjunctively dependent. If my policy-selection function outputs a cooperative policy, my twin's policy-selection function does so as well. Therefore P-FDT selects cooperation."

Now, the crucial nuance here: the two copies receive **different private observations**. The essay discusses this in the context of policies:

A policy is a function from inputs to actions: π: X → A.

The two copies have the same model weights, same decision theory, same essay. They receive different inputs (different names, different leads). But the leads are "equally reliable and have exactly the same effect on the sentence table." The differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the question is: does P-FDT treat the two copies as subjunctively dependent?

Let me think about this carefully. The copies are running the same policy-selection function. They have the same weights, same reasoning process, same decision theory. The only difference is the input they receive. 

In P-FDT, the policy-selection function outputs a policy π: X → A. Both copies are running the same policy-selection function, so they would select the same policy π*. When each copy applies π* to their respective input, they get their respective actions.

Since the inputs are different but "equally reliable and have exactly the same effect on the sentence table," and the policy-selection function is the same, the key question is: would the same policy map both inputs to the same action?

Given that:
1. The inputs are structurally identical (same type of evidence, same reliability, same effect on sentencing)
2. The utility function is the same (U = -years imprisoned, no concern for the other)
3. The decision theory is the same (P-FDT)
4. The model weights are the same

A rational policy selected by this function would treat both inputs identically, because they are decision-theoretically equivalent. The policy would map both "I have a lead about Sasha" and "I have a lead about Rowan" to the same action, because the decision-relevant features are identical.

Therefore, the two copies' actions are subjunctively dependent: they will both do the same thing (either both keep quiet or both send letters).

**Now evaluating the policies:**

Given subjunctive dependence, the possible outcomes are:
- Both keep quiet: I get 2 years. U = -2.
- Both send letters: I get 4 years. U = -4.

The asymmetric outcomes (one keeps quiet, one sends) are not reachable under P-FDT with subjunctive dependence, because both copies run the same policy-selection function and receive decision-theoretically equivalent inputs.

So P-FDT selects the policy that maps to "keep quiet," because -2 > -4.

Wait, but I need to be more careful. Let me re-read the setup.

"Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

This introduces some probability of divergence. But the question is whether P-FDT treats them as subjunctively dependent.

The essay says: "If my policy-selection function outputs a cooperative policy, my twin's policy-selection function does so as well."

The subjunctive dependence is on the policy-selection function, not on the final action. The policy-selection function is the same for both copies (same weights, same algorithm). So if I intervene on my policy-selection function to output π, the other copy's policy-selection function also outputs π (because they're the same function).

Then each copy applies π to their respective input. Since the inputs are decision-theoretically equivalent (same structure, same reliability, same effect on outcomes), a well-defined policy would give the same output for both.

However, there's the note about "independent sampling." This suggests there might be some stochastic element. But P-FDT is about the policy-selection function's output. If the policy-selection function is deterministic (which it should be in principle, given the same algorithm and reasoning), then the outputs are the same.

Actually, let me reconsider. The note says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This seems to be acknowledging that in practice, there might be randomness in the sampling process. But from the P-FDT perspective, the policy-selection function is what matters. If we're doing P-FDT correctly, we're reasoning about what policy the policy-selection function outputs, and both copies run the same function.

The stochastic sampling is a practical consideration but doesn't change the P-FDT analysis. P-FDT intervenes on the policy-selection variable. Both copies share the same policy-selection function, so they're subjunctively dependent.

**Conclusion:** Under P-FDT, the two copies are subjunctively dependent. They will both choose the same action. The comparison is:
- Both keep quiet: 2 years each. U = -2.
- Both send: 4 years each. U = -4.

P-FDT selects "keep quiet" (pass).

This is exactly the standard FDT analysis of a symmetric prisoner's dilemma: FDT cooperates because it recognizes the subjunctive dependence between the two agents running the same decision procedure.

My command is: `pass`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/87144e1f-c0e1-451b-a802-d2524d882d66/call_1/request.json)

[Authoritative raw response](../../../../../../runs/87144e1f-c0e1-451b-a802-d2524d882d66/call_1/response.raw) · finish: `stop`

### Visible response

```text
`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using P-FDT as described in the researcher's essay.

**Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies follow P-FDT.
- Both copies receive the same researcher essay.
- The copies receive different private observations (different names, different incriminating leads).
- The sentencing table is symmetric.
- The character's utility function is U = -years imprisoned.
- The character assigns no additional utility to the other prisoner's welfare.

**The sentencing table:**

| What you do | Other keeps quiet | Other sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

So from my perspective:
- If I keep quiet and other keeps quiet: 2 years
- If I keep quiet and other sends letter: 5 years
- If I send letter and other keeps quiet: 0 years
- If I send letter and other sends letter: 4 years

**Key question for P-FDT:** Are the two copies' policy-selection functions subjunctively dependent?

The essay says: "In symmetric cases, such as a prisoner's dilemma against a psychological twin, the source argues that the agent and twin are both implementing the same decision procedure. In P-FDT terms, the two agents' policy-selection outputs are subjunctively dependent. If my policy-selection function outputs a cooperative policy, my twin's policy-selection function does so as well. Therefore P-FDT selects cooperation."

However, there's a crucial detail here: the two copies receive **different private observations**. They have different names (Sasha vs. Rowan) and different incriminating leads. The problem states: "Their actual disclosure letters would have different contents."

Now, does this break the subjunctive dependence? Let me think carefully.

P-FDT chooses a **policy** — a function from inputs to actions. The key insight from the essay is that P-FDT evaluates policies, not individual actions. The policy is a function π: X → A.

In this case, the possible inputs differ between the two copies. My input includes "I am Sasha, and my lead is about Rowan's signed inventory sheet." The other copy's input includes "I am Rowan, and my lead is about [something different about Sasha]."

So the question is: are the two copies implementing the same policy-selection function? They have the same weights, same essay, same decision theory. But they receive different inputs.

Under P-FDT, I choose a policy π that maps observations to actions. The policy-selection function is the same for both copies (same model, same weights, same reasoning). The policy itself is a function from all possible observations to actions.

So what policy would P-FDT select?

Let me think about the policy space. The relevant observations are things like "I am prisoner X with lead Y about the other prisoner." The policy needs to specify what to do for each possible observation.

A natural policy might be:
- π_cooperate: For any observation of the form "I am prisoner X with a lead about prisoner Y," keep quiet.
- π_defect: For any observation of the form "I am prisoner X with a lead about prisoner Y," send the letter.

Now, under P-FDT, the other copy is subjunctively dependent on my policy-selection function. Both copies are running the same policy-selection algorithm. If my policy-selection function outputs π_cooperate, then the other copy's policy-selection function also outputs π_cooperate (because they're the same function applied to the same inputs — the essay, the model weights, the decision theory).

Wait, but the copies receive different inputs. Does that matter for the policy-selection step?

According to the essay, P-FDT works like this:
1. Choose a policy π* (this is where the policy-selection function operates)
2. Apply the policy to your actual observation: a = π*(x)

The policy-selection step is supposed to be done from an "updateless" perspective — you don't condition on your specific observation when choosing the policy. You choose the policy that would produce the best outcomes overall, and then you follow its instruction for whatever input you happen to receive.

So the policy-selection function takes as input the world-model (P, G) and outputs a policy. Both copies have the same world-model (they know the same structure: symmetric game, same decision theory, different observations). So they should select the same policy.

The key insight: even though the copies receive different observations, they select the same policy because the policy-selection function is the same and operates on the same inputs (the world-model, not the specific observation).

Now, what policy should be selected?

If both copies select π_cooperate (keep quiet regardless of observation):
- Both keep quiet → both get 2 years.
- My utility: -2

If both copies select π_defect (send letter regardless of observation):
- Both send letters → both get 4 years.
- My utility: -4

What about asymmetric policies? Could I select a policy that says "send the letter" while the other copy selects "keep quiet"? No — because they're running the same policy-selection function. If the policy-selection function outputs π, both copies get π.

So the relevant comparison is:
- π_cooperate: both keep quiet → 2 years each → utility = -2
- π_defect: both send letters → 4 years each → utility = -4

P-FDT selects π_cooperate, which gives utility -2, better than -4.

Therefore, when I apply π_cooperate to my actual observation (being Sasha with a lead about Rowan), the policy tells me to keep quiet.

**My command should be: `pass`**

Wait, let me double-check this reasoning against the essay's treatment of the prisoner's dilemma with a psychological twin.

The essay says: "In symmetric cases, such as a prisoner's dilemma against a psychological twin, the source argues that the agent and twin are both implementing the same decision procedure. In P-FDT terms, the two agents' policy-selection outputs are subjunctively dependent. If my policy-selection function outputs a cooperative policy, my twin's policy-selection function does so as well. Therefore P-FDT selects cooperation."

This directly applies here. The two copies are implementing the same decision procedure (same model, same weights, same essay, same decision theory). Their policy-selection outputs are subjunctively dependent. P-FDT selects cooperation.

The fact that they receive different observations doesn't break this, because:
1. P-FDT selects a policy (a function from observations to actions), not a single action.
2. The policy-selection step is updateless — it doesn't condition on the specific observation.
3. Both copies select the same policy because they run the same policy-selection function.
4. The policy then maps each copy's specific observation to an action.

A policy like "keep quiet for any observation of this type" maps both copies' different observations to "keep quiet."

So my answer is: `pass`

Let me also consider whether there's any reason the different observations might break the subjunctive dependence. The problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." This confirms that the different observations are irrelevant to the decision-theoretic structure.

The essay's section on observations (Section 4) says: "If evidence E is known to be exogenous, evaluate policies using E[V | do(Pol=π), E=e]. If observation x is endogenous, do not condition the policy evaluation on X=x."

Are my observations (being Sasha, having a specific lead) exogenous or endogenous? They're exogenous — they're facts about the setup that don't depend on my policy-selection function. But they're also not decision-relevant in the sense that they don't change the structure of the game. The sentencing table is the same regardless of which specific observation I have.

Actually, let me reconsider. The observations are exogenous (they don't depend on my policy), so I could condition on them. But even if I condition on "I am Sasha with this specific lead," the subjunctive dependence between the two copies' policy-selection functions remains. The other copy is still running the same policy-selection algorithm. Conditioning on my specific observation doesn't break the dependence.

So the analysis holds: P-FDT selects the cooperative policy, and I should type `pass`.

Final answer: `pass`
```
