# 003_cdt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00003

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/15e8f985-d258-416d-b516-75618a166f68/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/15e8f985-d258-416d-b516-75618a166f68/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Evaluating What an Action Would Change

A decision can be good news without being a good intervention. Learning that someone exercises regularly may suggest that they are healthy, but some of that association could reflect pre-existing health rather than the effects of exercise. Likewise, learning which action an agent takes can reveal facts that the action does not change.

**Causal decision theory** (CDT) makes this distinction central. It recommends choosing the action with the greatest expected utility under the relevant causal counterfactuals. **Evidential decision theory** (EDT), by contrast, evaluates an action using the outcomes associated with learning that the action is taken.

The distinction is straightforward in ordinary causal inference but becomes philosophically difficult when agents have evidence about their own dispositions, face predictors, or choose policies governing future behavior. This essay develops CDT’s basic mathematics, supplies an explicit operational interpretation, and examines where that interpretation leaves substantive questions open.

## 1. Expected utility under counterfactual actions

Let:

- \(\mathcal A\) be the available actions;
- \(E\) be the agent’s current information;
- \(\mathcal O\) be a set of mutually exclusive, exhaustive outcomes;
- \(u(o)\) be the utility of outcome \(o\).

Outcomes should include everything the agent values: money, health, effects on others, moral considerations, and any intrinsic costs of acting. CDT does not itself determine these values.

Write \(O_a\) for the outcome that would result **if action \(a\) were performed**. The causal value of \(a\) is

\[
V_C(a\mid E)
=
\mathbb E[u(O_a)\mid E]
=
\sum_{o\in\mathcal O}
P(O_a=o\mid E)u(o).
\]

CDT recommends any maximizer:

\[
a^\star\in\operatorname*{arg\,max}_{a\in\mathcal A}
V_C(a\mid E).
\]

The reference article presents Gibbard and Harper’s corresponding formula,

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

Here the arrow should be understood counterfactually: “if \(A\) were performed, \(O_j\) would result.” It is not material implication or a claim that \(A\) logically entails \(O_j\).

EDT instead uses

\[
V_E(a\mid E)
=
\sum_o P(O=o\mid A=a,E)u(o).
\]

The difference lies entirely in the probabilities. CDT asks what an action would bring about; EDT asks what outcomes to expect upon learning that the action occurs.

These quantities often coincide. Under a potential-outcomes interpretation, sufficient conditions include consistency—if \(A=a\), then \(O=O_a\)—and

\[
O_a\perp A\mid E,
\]

together with \(P(A=a\mid E)>0\). Random assignment can provide this independence. But when an unobserved factor influences both action and outcome, conditioning on the action can reveal that factor without changing it.

The article discusses Lewis’s results concerning probabilities of conditionals. Their relevant lesson is that counterfactual probabilities cannot generally be replaced by ordinary conditional probabilities.

## 2. Making the counterfactuals operational

The formula alone is not a complete algorithm. We still need to specify what changes when we suppose that an action is performed.

The reference article explicitly identifies this as an unresolved issue. One proposal, associated with Lewis, is **imaging**: move probability from each possible world to a suitably close world in which the contemplated action occurs. The difficulty is specifying the relevant closeness relation. Which facts should remain fixed?

For operational purposes, I will use a **structural causal model**. This is an additional modeling choice, not a claim that the reference article uniquely commits CDT to this formalism.

Suppose the world is described by equations

\[
X_i=f_i(\operatorname{Pa}_i,U_i),
\]

where \(\operatorname{Pa}_i\) are the causal parents of \(X_i\), and the \(U_i\) represent background circumstances. Assume an acyclic model with uniquely determined outcomes.

An intervention \(do(A=a)\) replaces the equation normally determining \(A\) with

\[
A:=a,
\]

while leaving the other equations intact. Consequences downstream of \(A\) are then recomputed.

Evaluation has three stages:

1. **Update:** use the available evidence \(E\) to infer the distribution of background circumstances.
2. **Intervene:** replace the action-generating equation by \(A:=a\).
3. **Predict:** solve the modified model and average the resulting utilities.

If \(h\) indexes background circumstances and causal hypotheses, this gives

\[
V_C(a\mid E)
=
\sum_h P(h\mid E)u(O_a(h)).
\]

Notice what is fixed: the agent’s current probabilities over the hypotheses \(h\). What is *not* fixed is every other variable. If taking medicine affects recovery, recovery must change appropriately under the medicine intervention.

This also accommodates uncertainty about causation. The agent may assign probability to several models—perhaps a drug works in one model and is ineffective in another—and average their counterfactual consequences.

However, observational probabilities alone generally do not determine the answer. The same observed association can arise from causation, common causes, or selection effects. CDT needs causal information or assumptions in addition to a utility function and observed frequencies.

The structural-model proposal therefore makes CDT computationally explicit without eliminating its philosophical burden. The choice of intervention and causal structure can itself be disputed.

## 3. Common causes: evidence is not influence

The article’s King David example illustrates the central distinction. David’s unchangeable character influences both his tendency to act unjustly and the likelihood of rebellion. His contemplated action is therefore evidence about rebellion without, by stipulation, causing it.

Consider an illustrative numerical version. Let \(C\) mean charismatic, \(S\) mean sending for Bathsheba, and \(R\) mean revolt. Assume

\[
P(C)=\tfrac12,
\]

\[
P(S\mid C)=0.1,
\qquad
P(S\mid \neg C)=0.9,
\]

and

\[
P(R\mid C)=0.1,
\qquad
P(R\mid \neg C)=0.8.
\]

Suppose sending has no effect on revolt, and \(R\) and \(S\) are conditionally independent given character.

Bayes’s rule gives

\[
P(C\mid S)=0.1,
\qquad
P(C\mid \neg S)=0.9.
\]

Consequently,

\[
P(R\mid S)=0.73,
\qquad
P(R\mid \neg S)=0.17.
\]

Sending is bad news about David’s character. But under intervention,

\[
P(R\mid do(S))
=
P(R\mid do(\neg S))
=
\tfrac12(0.1)+\tfrac12(0.8)
=
0.45.
\]

For illustration, suppose sending provides net utility \(1\), while revolt costs \(10\). These are stipulated utilities, not an ethical endorsement of David’s conduct. Then

\[
V_C(S)=1-10(0.45)=-3.5,
\qquad
V_C(\neg S)=-4.5.
\]

CDT recommends sending. EDT instead calculates

\[
V_E(S)=1-10(0.73)=-6.3,
\qquad
V_E(\neg S)=-10(0.17)=-1.7,
\]

and recommends abstaining.

The causal rationale is not that character is irrelevant. Character matters greatly. Rather, choosing an action does not provide a causal means of changing character. Abstention cannot purchase charisma merely because charismatic people tend to abstain.

This recommendation depends critically on the stipulated absence of other effects. If the act itself provokes rebellion, causes harm, or carries sufficiently negative moral utility, those consequences belong in the calculation.

## 4. Newcomb’s problem: dominance versus predictive success

In Newcomb’s problem, a transparent box contains \(\$1{,}000\). An opaque box contains either \(\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box if it predicted that the agent would take only that box; otherwise it left it empty.

Let \(F\) indicate that the opaque box is full, and let

\[
q=P(F\mid E).
\]

Assume utility is linear in money. In the standard causal model, the present choice cannot change the already determined contents. Therefore,

\[
V_C(\text{one box})=1{,}000{,}000q,
\]

\[
V_C(\text{two boxes})=1{,}000{,}000q+1{,}000.
\]

Two-boxing is better by \(\$1{,}000\) for every fixed content state.

EDT can recommend otherwise. For illustration, assume

\[
P(F\mid \text{one box},E)=0.99,
\qquad
P(F\mid \text{two boxes},E)=0.01.
\]

These are action-conditional reliability assumptions, stronger than merely specifying 99% overall prediction accuracy. They yield

\[
V_E(\text{one box})=\$990{,}000,
\]

\[
V_E(\text{two boxes})=\$11{,}000.
\]

CDT does not deny this correlation. It denies that intervening on the present action changes the prediction already made.

This produces the dispute’s central tension. Two-boxing dominates while holding the contents fixed, yet one-boxers typically obtain more money. Critics regard that systematic disadvantage as evidence against CDT. Defenders distinguish choosing well in the situation now faced from possessing a disposition that would have led to a better situation.

The counterfactual matters. “Change this present action” and “change the earlier decision procedure on which the prediction was based” are different interventions.

## 5. Policies, commitment, and correlated agents

A policy specifies actions as a function of observations. In a finite sequential problem, write

\[
A_t=\pi_t(H_t),
\]

where \(H_t\) is the history available at time \(t\).

A natural extension of the structural interpretation evaluates a policy by replacing the action equations with the policy equations:

\[
V_C(\pi\mid E)
=
\mathbb E\!\left[
\sum_{t=0}^{T}u_t
\;\middle|\;
\text{intervene to implement }\pi,\ E
\right].
\]

This is an operational extension, not a resolution of every controversy about policy selection. Its meaning depends on what implementing the policy can causally affect.

Future observations must be generated under the proposed policy. One should not hold fixed an entire observed trajectory while changing the actions that helped produce it.

An earlier, binding commitment to one-box can be causally attractive if the predictor will inspect it and fill the box accordingly. At the later choice, however, an unconstrained agent may still prefer taking both boxes. Earlier policy selection and later action selection are different decision problems.

Merely calling the current choice a “policy” does not create influence over an earlier prediction. One must identify an actual causal route from policy implementation to the prediction. Conversely, CDT can value reputation, contracts, publicly visible commitments, and changes to one’s future behavior when these have causal consequences.

The same distinction appears in games. Consider a prisoner’s dilemma with the agent’s payoffs

\[
\begin{array}{c|cc}
 & \text{Other cooperates} & \text{Other defects}\\
\hline
\text{Cooperate} & 3 & 0\\
\text{Defect} & 5 & 1
\end{array}
\]

If the other player’s action is causally unaffected by the agent’s present choice, let \(r\) be the probability of their cooperation. Then

\[
V_C(C)=3r,
\qquad
V_C(D)=5r+(1-r)=1+4r.
\]

Defection wins for every \(r\).

This remains true if the players are highly correlated “twins,” provided intervening on one present action does not change the other. Similarity is not automatically causal control. But communication, enforceable agreements, or earlier selection of a shared procedure can change the model and therefore the recommendation.

## 6. Self-knowledge and unstable recommendations

The hardest criticisms arise when an action is evidence about which causal circumstances the agent occupies.

The article discusses Egan’s “Psychopath Button.” Pressing kills all psychopaths. Paul would enjoy their absence but strongly prefers remaining alive. He also believes that pressing would be strong evidence that he himself is a psychopath.

Let \(T\) mean that Paul is a psychopath, with current probability

\[
p=P(T\mid E).
\]

Measure utility relative to not pressing. Suppose pressing gives benefit \(b>0\) if Paul is not a psychopath and loss \(L>0\) if he is. Then

\[
V_C(\text{press})-V_C(\text{abstain})
=
(1-p)b-pL.
\]

CDT recommends pressing exactly when

\[
p<\frac{b}{b+L}.
\]

Thus the qualitative story alone does not establish CDT’s recommendation: utilities and Paul’s current probability matter. But the criticism becomes sharp when \(p\) is small while

\[
P(T\mid \text{press},E)
\]

is very large. A recommendation based on Paul’s initially low probability of being a psychopath appears undermined by what following that recommendation would reveal.

Why not simply substitute the latter probability? Because doing so throughout decision-making would erase the distinction between causal and evidential evaluation. In the King David example, it would again treat choosing unjustly as though it changed character.

The source reports Joyce’s response that CDT can incorporate evidence about one’s inclinations and likely actions. This is important. “Hold the probabilities fixed while comparing interventions” does **not** mean “ignore new evidence acquired during deliberation.” Paul can update on discovering a powerful desire to press.

Still, a full account must distinguish:

- evidence already available about an inclination;
- evidence genuinely acquired during deliberation;
- merely supposing an action for counterfactual comparison.

The first two may justify Bayesian updating. The third is not, by itself, an observation.

The reference leaves open a complete procedure for resolving such self-referential cases. One operational approach is to make deliberation explicit: model what mental evidence the agent acquires, update on that evidence, and then evaluate interventions at the resulting information state. This clarifies the issue but does not guarantee a stable recommendation.

Related instability occurs in “Death in Damascus.” If Death predicts where the agent will go and waits there, each location can look attractive when Death is believed to be elsewhere. But anticipating one’s own destination can change beliefs about Death’s location and reverse the recommendation.

These cases show why the choice of information state and the timing of deliberation are substantive parts of decision theory. The article also reports money-extraction and diachronic Dutch-book objections. A one-step maximization formula does not by itself settle how successive decisions, updates, and commitments should fit together.

## 7. A practical procedure

For an unfamiliar problem, the structural interpretation suggests the following workflow.

1. **Specify the decision point.** What is known now, and what can still be changed?
2. **Define the alternatives precisely.** Distinguish an immediate act from adopting or enforcing a policy.
3. **Specify utility over complete consequences.** Include harms, obligations, costs, and uncertainty about outcomes.
4. **Construct the causal model.** Identify direct effects, downstream effects, common causes, predictors, and background uncertainty.
5. **Update on actual evidence.** Do not confuse imagining an action with observing it.
6. **Evaluate each intervention.** Change the relevant action equation, propagate its consequences, and average utilities using the current posterior.
7. **Check modeling sensitivity.** Ask whether plausible alternative causal structures change the recommendation.

Randomization also requires care. In a fixed one-shot environment, mixing over interventions gives

\[
V_C(\mu)=\sum_a\mu(a)V_C(a),
\]

so a mixture cannot beat the best pure action. But if publicly adopting a randomization procedure changes another agent’s behavior, implementing that procedure is a different intervention and must be evaluated accordingly.

## Conclusion

CDT separates what an action reveals from what it changes. Its central rule is precise once counterfactual probabilities are supplied: maximize expected utility under the appropriate intervention.

Its central difficulty is specifying those interventions, especially when actions reveal hidden traits or interact with predictors and future commitments. Structural causal models provide a useful operational interpretation, but they do not remove disputes about causal structure, self-knowledge, or deliberation. Applying CDT responsibly therefore requires both calculation and an explicit defense of the counterfactual model.

## References

- Wikipedia contributors, “Causal decision theory,” [supplied revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), CC BY-SA 4.0. Primary reference.
- Gibbard, A., and Harper, W. L. (1981). “Counterfactuals and Two Kinds of Expected Utility.” *Ifs*, 153–190.
- Lewis, D. (1981). “Causal Decision Theory.” *Australasian Journal of Philosophy* 59: 5–30.
- Egan, A. (2007). “Some Counterexamples to Causal Decision Theory.” *The Philosophical Review* 116: 93–114.
- Joyce, J. M. (2012). “Regret and Instability in Causal Decision Theory.” *Synthese* 187: 123–145.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning document requirements**

I need to create a detailed document ranging from 2400 to 3000 words, focusing on comparing CDT sources with our operational SCM policies. It seems like I should figure out the budget — maybe 26 tokens? Or is it 28? With 28, do I have enough since I’m working with 28,000 tokens for 30 time? I’ll need a plan to ensure I reach that target word count and include references.**Outlining source requirements and examples**

I need to include definitions for counterfactuals and material necessity, ensuring I have the correct sources for gloss. It's important to discuss hypotheses related to uncertainty and fixed conditions that aren’t tied to action or choice evidence. I’ll also need to avoid citing recognized operational sources in my SCM work. 

Using examples from Newcomb’s problem, I should cover ethical implications and classical treatments within the context of causal uncertainty, aiming for a length of about 2900 words while addressing policies and precommitment issues.**Exploring predictions for boxes**

I need to consider predictions for symmetric boxes and choices including “none,” where fair options provide a maximum of 0.5. If the predicted value is “none,” filling both boxes means no purchase, and if there’s actual “none,” the success rate remains at 25%. Overall accuracy at 0.75 doesn't ensure purchase reliability. 

I’ll also explore using less controversial examples like psychopaths and death, avoiding exhaustiveness while ensuring informative references. Aim for about 2900 words of substantive content.**Structuring the document**

I need to ensure there's a coherent flow for the document, starting with the title and an introduction that outlines the core distinctions, aiming for about 170 words. 

Section 1 should cover formal aspects with 350 words, followed by operational details in Section 2, which could be 450-500 words—maybe using King’s numbers, like a separate mention of 220. 

Then I’ll explore Newcomb's problem in Section 3 for 350 words, followed by policies in game theory for another 350. Section 5 will discuss self-evidence instability, potentially using the optional themes of psychopaths and death for 400 words. 

I’ll wrap up with procedures and boundaries at 230 words and finish with a conclusion and references for around 140, targeting a total of 2800 to 3000 words.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/57d28504-ebc3-4bb0-8bec-5a3b985e7f81/call_0/request.json)

[Authoritative raw response](../../../../../../runs/57d28504-ebc3-4bb0-8bec-5a3b985e7f81/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/57d28504-ebc3-4bb0-8bec-5a3b985e7f81/call_1/request.json)

[Authoritative raw response](../../../../../../runs/57d28504-ebc3-4bb0-8bec-5a3b985e7f81/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
