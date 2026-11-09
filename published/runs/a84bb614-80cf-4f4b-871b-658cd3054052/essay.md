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