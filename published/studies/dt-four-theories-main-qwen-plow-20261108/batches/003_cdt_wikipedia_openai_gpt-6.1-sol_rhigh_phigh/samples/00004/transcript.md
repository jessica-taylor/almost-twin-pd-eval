# 003_cdt_wikipedia_openai_gpt-6.1-sol_rhigh_phigh / 00004

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5efed165-eb30-433b-a33a-797d074101f4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5efed165-eb30-433b-a33a-797d074101f4/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing by What an Action Changes

A decision can be good news without being a good intervention. Taking a particular medicine might indicate that one has a serious illness, even though taking it improves one’s prospects. Conversely, an action might indicate favorable circumstances without helping to produce them.

Causal decision theory, or **CDT**, makes this distinction central to rational choice. It recommends the action with the best expected causal consequences, rather than the action most strongly associated with desirable outcomes.

That principle is compelling, but applying it requires more than calculating an ordinary conditional expectation. We must specify which dependencies persist when an action is hypothetically changed, how uncertainty about those dependencies is represented, and whether the object of choice is an immediate act or an earlier policy. Predictor problems then expose a further difficulty: an agent’s deliberation may itself provide evidence about circumstances the action cannot change.

## 1. The central mathematical distinction

Let \(\mathcal A\) be a finite set of feasible actions, \(E\) the agent’s current evidence, and \(u(o)\) the utility of a complete outcome \(o\). Utilities should include everything the agent values: money, health, effects on others, costs of acting, and so forth.

Write \(O_a\) for the outcome that would occur if action \(a\) were performed. A standard causal evaluation is

\[
V_{\mathrm{CDT}}(a\mid E)
=
\mathbb E[u(O_a)\mid E].
\]

For finitely many possible outcomes,

\[
V_{\mathrm{CDT}}(a\mid E)
=
\sum_o P(O_a=o\mid E)\,u(o),
\]

and CDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}
V_{\mathrm{CDT}}(a\mid E).
\]

This expresses the reference article’s formulation, attributed to Gibbard and Harper, using probabilities of counterfactuals. The relevant statement is “Were \(a\) performed, outcome \(o\) would occur.” It is not the material implication \(a\Rightarrow o\), which becomes trivially true whenever \(a\) is false, nor a claim of logical necessity.

**Evidential decision theory**, by contrast, evaluates

\[
V_{\mathrm{EDT}}(a\mid E)
=
\sum_o P(O=o\mid A=a,E)\,u(o).
\]

Here \(A\) describes the action actually taken, and \(O\) the actual outcome. EDT asks what outcomes to expect upon learning that the action occurred. CDT asks what outcomes to expect upon making it occur.

These evaluations can coincide. If, conditional on \(E\), the actual action is independent of every relevant potential outcome, then, assuming consistency and positive probability for the action,

\[
P(O_a=o\mid E)
=
P(O=o\mid A=a,E).
\]

Randomized treatment assignment often supplies this independence. Self-selected treatment frequently does not.

The reference discusses Lewis’s results concerning probabilities of conditionals. Those results caution against identifying counterfactual probabilities with ordinary conditional probabilities as a general rule; they do not imply that the two must always differ.

## 2. Making counterfactuals operational

The source explicitly acknowledges an incompleteness: CDT does not itself provide a universal algorithm for computing counterfactual probabilities.

A useful operational interpretation is supplied by **structural causal models**. This is an additional modeling framework, not something uniquely required by the article’s definition of CDT.

Suppose the world is described by equations

\[
X_i=f_i(\operatorname{Pa}_i,Z_i),
\]

where \(\operatorname{Pa}_i\) are the direct causes of \(X_i\), and the \(Z_i\) represent background circumstances or disturbances.

Ordinarily, the action variable also has an equation,

\[
A=f_A(\operatorname{Pa}_A,Z_A).
\]

To evaluate doing \(a\), replace this equation by

\[
A:=a,
\]

while retaining the other equations. The resulting intervention is written \(\operatorname{do}(A=a)\), giving

\[
V_{\mathrm{CDT}}(a\mid E)
=
\sum_o
P(o\mid \operatorname{do}(A=a),E)\,u(o).
\]

The intervention removes the action’s normal dependence on its causes. It does not remove its effects.

For example, consider

\[
C\longrightarrow A,\qquad
C\longrightarrow Y,\qquad
A\longrightarrow Y.
\]

An underlying condition \(C\) influences both treatment \(A\) and health \(Y\), while treatment also affects health. Observing treatment provides evidence about \(C\). Intervening on treatment does not, by itself, change \(C\).

A practical calculation has three stages:

1. **Update on actual evidence.** Infer the background circumstances compatible with \(E\).
2. **Intervene.** Replace the action equation by the contemplated action.
3. **Propagate.** Calculate downstream outcomes using the remaining equations.

If \(z\) denotes a complete background state, this gives

\[
V(a\mid E)=\sum_z P(z\mid E)\,u(O_a(z)).
\]

Uncertainty about the causal model can also be included:

\[
V(a\mid E)
=
\sum_{M,z}P(M,z\mid E)\,u(O_a(M,z)).
\]

Thus CDT need not assume certainty about causation.

The article also describes Lewis’s **imaging** approach: transfer probability from each possible world to a closest world in which the contemplated action occurs. Structural intervention supplies one disciplined interpretation of “closest”: change the action mechanism while preserving background circumstances and other mechanisms.

Neither approach eliminates substantive judgment. Which mechanisms should remain fixed is precisely what must be defended. Assuming that each intervention has a uniquely determined outcome once the background state is specified is itself a modeling assumption.

## 3. A common-cause example

The reference illustrates the difference between causation and evidence with King David’s uncertainty about his own charisma. His personality affects both his tendency to act unjustly and his vulnerability to revolt, while the particular unjust act is stipulated not to cause revolt.

Here is a numerical version. Suppose David assigns probability \(1/2\) to being charismatic. Revolt probabilities are

\[
P(R\mid C)=0.1,
\qquad
P(R\mid \neg C)=0.6.
\]

Summoning Bathsheba brings a stipulated benefit of \(5\), and revolt has utility cost \(100\). For illustration, assume these exhaust the utility differences.

Because summoning does not change personality or revolt risk,

\[
P(R\mid \operatorname{do}(\text{summon}))=0.35.
\]

Consequently,

\[
V_{\mathrm{CDT}}(\text{summon})=5-100(0.35)=-30,
\]

whereas abstaining has value \(-35\).

Now suppose summoning is strong evidence of lacking charisma:

\[
P(\neg C\mid \text{summon})=0.9,
\qquad
P(\neg C\mid \text{abstain})=0.1.
\]

The corresponding evidential revolt probabilities are \(0.55\) and \(0.15\). EDT therefore assigns values \(-50\) and \(-15\), preferring abstention.

The disagreement concerns whether to evaluate the action while retaining current beliefs about personality or while adopting the personality distribution associated with observing that action.

This is not a moral endorsement of David’s conduct. Adding disutility for injustice or harm could reverse CDT’s recommendation. A decision theory supplies an evaluation procedure, not a complete account of what deserves utility.

## 4. Newcomb’s problem: dominance against predictive success

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains \$1,000,000 if a reliable predictor previously predicted that the agent would take only that box, and nothing otherwise. The agent may take the opaque box alone or both boxes.

Let \(B\in\{0,10^6\}\) denote the opaque box’s contents. Under the usual causal interpretation,

\[
\text{current action does not cause }B.
\]

With linear utility for money,

\[
V_{\mathrm{CDT}}(\text{one box})=\mathbb E[B\mid E],
\]

\[
V_{\mathrm{CDT}}(\text{two boxes})
=
\mathbb E[B\mid E]+1000.
\]

Thus CDT recommends taking both.

Indeed, two-boxing yields \$1,000 more for either fixed content of the opaque box. This is a dominance argument across causal background states.

The evidential calculation differs. Suppose, more specifically, that

\[
P(B=10^6\mid \text{one box})=0.99,
\qquad
P(B=10^6\mid \text{two boxes})=0.01.
\]

Then

\[
V_{\mathrm{EDT}}(\text{one box})=990{,}000,
\qquad
V_{\mathrm{EDT}}(\text{two boxes})=11{,}000.
\]

These conditional probabilities require more specification than a bare statement of “99% overall accuracy”; the latter does not uniquely determine both.

CDT does not deny the predictive correlation. It denies that the correlation should be preserved when evaluating an intervention on the present action.

This is also the source of the objection. Agents disposed to one-box generally receive more money. Defenders distinguish choosing well in an already arranged situation from possessing a disposition that attracts favorable arrangements. Critics question whether a theory should maintain that distinction when it repeatedly recommends the poorer-performing action.

## 5. Actions, policies, and commitment

An immediate action and a policy are different possible objects of intervention.

A policy \(\pi\) specifies what to do after each possible information history \(h\):

\[
A_t=\pi_t(h_t).
\]

A stochastic policy instead specifies probabilities \(\pi_t(a\mid h_t)\). If selecting and implementing such a policy is feasible, a natural causal evaluation is

\[
V(\pi\mid E)
=
\mathbb E\!\left[
\sum_{t=0}^{T}\gamma^t r_t
\;\middle|\;
\operatorname{do}(\pi),E
\right].
\]

Here intervening on \(\pi\) means replacing the relevant action-generating mechanisms with the policy. This is an operational extension of the basic action rule.

Timing matters. Suppose that, before the Newcomb predictor acts, an agent can install a binding device guaranteeing one-boxing, and the predictor can inspect it. The causal structure may then include

\[
\text{commitment}
\longrightarrow
\text{prediction}
\longrightarrow
\text{box contents}.
\]

CDT can favor installing that device. Once the boxes are filled, however, taking another box cannot affect their contents.

There is no permission here to redescribe any present action as an earlier commitment. A policy must be genuinely selectable, and its consequences must follow through the specified causal structure. Merely imagining “being the kind of agent who one-boxes” does not establish a causal influence on yesterday’s prediction.

Likewise, randomization alone does not solve a fixed one-stage problem. If an independent randomizer chooses actions with probabilities \(\mu(a)\), then

\[
V(\mu\mid E)=\sum_a\mu(a)V(a\mid E),
\]

which cannot exceed the best pure action’s value. Randomization can matter when others causally respond to a commitment to randomize, or when it prevents successful prediction. Those are changes to the decision environment, not exceptions to linearity.

## 6. Correlated opponents

Consider a prisoner’s dilemma with payoffs

\[
u(C,C)=3,\quad u(D,C)=5,\quad
u(C,D)=0,\quad u(D,D)=1.
\]

Suppose the opponent’s action is strongly correlated with yours because you have similar dispositions, but neither action causally influences the other.

Let \(q\) be the opponent’s probability of cooperation under either intervention on your action. Then

\[
V(C)=3q,
\qquad
V(D)=5q+1(1-q)=1+4q.
\]

Defection is better by \(1+q\).

An evidential evaluation may favor cooperation if observing your cooperation strongly predicts the opponent’s cooperation. CDT retains the opponent’s behavior when changing your action counterfactually.

However, if you can communicate, make an observable commitment, or otherwise influence the opponent, the causal model changes. CDT does not recommend ignoring strategic influence; it recommends distinguishing influence from correlation.

## 7. Self-knowledge and deliberative instability

The reference highlights Egan’s “Psychopath Button.” Paul values eliminating psychopaths but believes that almost only psychopaths would press the button. Pressing kills every psychopath, possibly including Paul.

Let

\[
p=P(\text{Paul is a psychopath}\mid E).
\]

Suppose pressing gives utility gain \(g>0\) if Paul is not a psychopath and utility loss \(L>0\) if he is, relative to abstaining. These quantities incorporate all relevant consequences. The straightforward causal calculation is

\[
\Delta V=(1-p)g-pL.
\]

Pressing is recommended when

\[
p<\frac{g}{g+L}.
\]

The uncomfortable recommendation arises if Paul’s initial \(p\) is small despite his belief that pressing would strongly indicate psychopathy.

The source reports Joyce’s response that CDT can use information about one’s inclinations as evidence. That distinction is important. Discovering a powerful desire to press may rationally raise \(p\). Merely evaluating the intervention “press,” however, does not automatically justify conditioning on the actual occurrence of pressing.

A reasonable operational procedure is therefore:

- update on genuine observations of one’s inclinations or deliberative state;
- evaluate interventions using those updated beliefs;
- do not treat every hypothetical action as already-observed evidence.

This preserves the causal–evidential distinction, but it leaves a difficult boundary question. Deliberation can generate new self-knowledge, and new self-knowledge can change the preferred action. The article does not specify a universal rule for when that process is complete or how to resolve cycles.

## 8. Adversarial offers and fixed causal beliefs

The article’s adversarial-offer example sharpens this difficulty. Two boxes each cost \$1. Yesterday, a predictor placed \$3 in every box she predicted the buyer would not acquire. The buyer may purchase one box or neither.

At least one box contains \$3. Holding the buyer’s present beliefs about the already fixed contents constant across interventions,

\[
\mathbb E[X_1\mid E]+\mathbb E[X_2\mid E]\ge 3.
\]

Thus at least one box has expected contents worth at least \$1.50. Straightforward CDT recommends buying some box rather than declining.

Yet reliable prediction can make purchasers systematically lose. To make the calculation precise, add the assumption that, conditional on purchasing, the predictor correctly identifies the purchased box with probability \(0.75\). The purchased box is then empty with probability \(0.75\), producing expected profit

\[
0.25(3)-1=-0.25.
\]

This conditional calibration is stronger than an unspecified overall accuracy rate.

The contrast captures Egan’s criticism of holding initial beliefs about causal dependencies fixed. Each contemplated purchase can look profitable under current beliefs, while the purchase eventually selected is predictable and therefore usually unfavorable.

It does not follow that every development of CDT must ignore information acquired during selection. But allowing such updates raises the preceding stability problem: after learning which option one favors, a different option may become preferable. The source presents this as an active dispute, not a settled refutation or a solved technical detail.

## 9. A practical method for unfamiliar cases

A disciplined application of CDT should answer five questions.

**What is being chosen?** Identify a feasible action, commitment, or policy, and its time of implementation.

**What is already known?** Condition on actual evidence, including legitimate self-knowledge.

**What changes under intervention?** Specify causal mechanisms rather than inferring them from correlations alone.

**What remains uncertain?** Average over background circumstances and, where appropriate, competing causal models.

**Is the recommendation stable?** Check whether deliberation supplies new evidence, whether future choices will undo a policy, and whether an alleged commitment is genuinely binding.

When plausible causal models disagree, calculate under each and expose the dependence. If \(M_1\) and \(M_2\) receive probabilities \(w\) and \(1-w\), compare

\[
V(a)=wV(a\mid M_1)+(1-w)V(a\mid M_2).
\]

Often the useful result is a threshold in \(w\), rather than an unjustifiably unconditional recommendation.

## Sources

This essay draws principally on Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” supplied revision, and the works it identifies: Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1981); Lewis, “Causal Decision Theory” (1981); Egan, “Some Counterexamples to Causal Decision Theory” (2007); Joyce, “Regret and Instability in Causal Decision Theory” (2012); and Oesterheld and Conitzer, “Extracting Money from Causal Decision Theorists” (2021). The structural-model implementation and numerical elaborations above are additional expository choices.

## Conclusion

CDT evaluates actions by their expected consequences under causal counterfactuals, not simply by the outcomes they predict. Its practical strength is separating intervention from evidence. Its central unfinished business concerns specifying counterfactuals and handling evidence generated by deliberation itself. Applying CDT responsibly therefore requires both an expected-utility calculation and an explicit defense of what changes—and what remains fixed—when an alternative is chosen.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/021f7f2c-9205-4a9e-986a-6204287a9526/call_0/request.json)

[Authoritative raw response](../../../../../../runs/021f7f2c-9205-4a9e-986a-6204287a9526/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/021f7f2c-9205-4a9e-986a-6204287a9526/call_1/request.json)

[Authoritative raw response](../../../../../../runs/021f7f2c-9205-4a9e-986a-6204287a9526/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
