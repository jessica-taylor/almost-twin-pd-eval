# Causal Decision Theory: Choosing Effects, Not Evidence

A decision can be informative without being effective. Taking a particular action might reveal that one is healthy, that a prediction was favorable, or that another person will cooperate. But revealing a favorable circumstance is not necessarily the same as bringing it about.

**Causal decision theory** (CDT) makes this distinction central. It recommends the action with the greatest expected utility under a causal counterfactual: *What would happen if I performed this action?* **Evidential decision theory** (EDT), by contrast, evaluates the prospects associated with learning that the action is performed.

This difference is often invisible in ordinary decisions. It becomes decisive when actions correlate with circumstances they cannot influence. The challenge is to specify which dependencies survive a hypothetical change of action—and why.

The supplied reference presents CDT’s counterfactual formulation and several major objections. Below, I develop that formulation into a practical procedure using structural causal models. This implementation is an additional modeling choice, not something uniquely specified by the reference.

## 1. The basic mathematical rule

Let:

- \(\mathcal A\) be a finite set of available actions;
- \(I\) be the agent’s current information;
- \(O\) be the eventual outcome;
- \(u(O)\) be its utility.

Utilities should include everything the agent values: money, health, other people’s welfare, moral considerations, and any costs of acting. CDT supplies an optimization rule, not a particular morality.

For each action \(a\), introduce a potential outcome \(O_a\): the outcome that would occur were the agent to perform \(a\). The causal value of \(a\) is

\[
V_C(a\mid I)=\mathbb E[u(O_a)\mid I].
\]

CDT recommends

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a\mid I).
\]

For discrete outcomes \(o_j\),

\[
V_C(a\mid I)
=
\sum_j P(O_a=o_j\mid I)\,u(o_j).
\]

This corresponds to the Gibbard–Harper formula reproduced in the reference:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

Here the arrow represents a counterfactual conditional. It should not be read as material implication or as ordinary logical necessity. An action need not logically entail an outcome to make that outcome causally probable.

EDT instead uses

\[
V_E(a\mid I)
=
\mathbb E[u(O)\mid A=a,I].
\]

The difference is between **supposing an action is imposed** and **learning that the action occurs**. Learning can change beliefs about the circumstances that produced the action. An intervention need not.

A useful alternative representation introduces a background state \(H\), sufficiently detailed to determine the consequences of each action:

\[
V_C(a\mid I)
=
\sum_h P(h\mid I)\,u(O(a,h)).
\]

The same background probabilities appear in every comparison. EDT can instead assign different weights \(P(h\mid A=a,I)\) to different contemplated actions.

These rules sometimes agree. Assuming consistency—if \(A=a\), then \(O=O_a\)—a sufficient condition is

\[
O_a\perp A\mid I.
\]

Then, for actions with positive conditional probability,

\[
P(O_a=o\mid I)=P(O=o\mid A=a,I).
\]

The reference discusses related independence conditions and Lewis’s work on probabilities of conditionals. The practical lesson is that conditional and counterfactual probabilities cannot simply be identified.

## 2. Making counterfactuals operational

CDT’s formula is incomplete until we say how to calculate \(O_a\). This is a central limitation identified by the reference: the theory does not itself supply a universally accepted counterfactual algorithm.

A structural causal model provides one operational interpretation. Suppose

\[
X=f_X(Z_X),\qquad
A=f_A(X,Z_A),\qquad
O=f_O(A,X,Z_O),
\]

where \(X\) describes background circumstances and the \(Z\)’s represent exogenous uncertainty. They need not be mutually independent.

To evaluate action \(a\), replace the action equation with

\[
A:=a,
\]

while retaining the other equations. This is the intervention \(\operatorname{do}(A=a)\). It breaks the modeled causes of the action without breaking the action’s effects.

For suitable pre-action information \(I\),

\[
V_C(a\mid I)
=
\sum_o u(o)\,
P(o\mid\operatorname{do}(A=a),I).
\]

Computationally, the procedure is:

1. Infer a posterior distribution over background circumstances from \(I\).
2. Replace the action-generating mechanism by \(A:=a\).
3. Propagate that change through the remaining causal mechanisms.
4. Average the resulting utilities.

If the causal model itself is uncertain, let \(M\) index possible models and \(z\) their exogenous states. Then

\[
V_C(a\mid I)
=
\sum_{M,z}
P(M,z\mid I)\,
u\!\left(O_a(M,z)\right).
\]

Thus CDT need not assume certainty about causal structure. It averages over causal hypotheses while holding their current posterior weights fixed across hypothetical actions.

“Holding fixed” does not mean preserving everything. Downstream consequences must change when the model says they change. If buying a medicine changes symptoms, future observations, and subsequent treatment, all those consequences belong in the calculation. What remains fixed is the relevant background uncertainty, not the entire future.

The reference also describes Lewis’s **imaging** proposal: transfer each world’s probability to an appropriate nearby world in which the contemplated action occurs. Structural interventions make a particular choice about the relevant similarity: preserve background mechanisms and circumstances, alter the action mechanism, and recompute its consequences.

Neither approach eliminates judgment. Which variables are genuine causes? What can the agent intervene upon? Which mechanisms remain stable? CDT requires answers; the maximization rule cannot provide them.

## 3. Common causes: the King David example

The reference’s King David example illustrates the intended separation of evidence from influence.

Let \(H\) represent an established personality type: charismatic or uncharismatic. Personality affects both David’s tendency to summon Bathsheba and his vulnerability to rebellion. By stipulation, summoning her does not itself affect rebellion:

\[
H\longrightarrow A,
\qquad
H\longrightarrow R.
\]

For illustration, suppose the two personality types are initially equally probable, and

\[
P(R\mid H=\text{charismatic})=0.1,
\qquad
P(R\mid H=\text{uncharismatic})=0.6.
\]

Suppose also that the probabilities of summoning her are respectively \(0.1\) and \(0.9\).

Then

\[
P(R)=0.35,
\]

but observing the action gives

\[
P(R\mid \text{summon})=0.55,
\qquad
P(R\mid \text{abstain})=0.15.
\]

Let summoning have a net benefit of \(2\), apart from rebellion, and let rebellion cost \(10\). These are illustrative utilities, not a moral endorsement.

CDT assigns

\[
V_C(\text{summon})=2-10(0.35)=-1.5,
\]

\[
V_C(\text{abstain})=-10(0.35)=-3.5.
\]

EDT instead assigns

\[
V_E(\text{summon})=2-10(0.55)=-3.5,
\]

\[
V_E(\text{abstain})=-10(0.15)=-1.5.
\]

CDT recommends summoning because changing the action does not change the stipulated personality or rebellion risk. EDT recommends abstention because abstention is favorable evidence about personality.

The example depends on its causal assumptions. If the act provokes rebellion, or its moral cost outweighs the benefit, CDT may recommend abstention too.

## 4. Newcomb’s problem: prediction without present control

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains either \$1,000,000 or nothing. A reliable predictor previously filled the opaque box exactly when it predicted that the player would take only that box.

The player now chooses between one-boxing and two-boxing.

Let \(B\in\{0,1\}\) indicate whether the opaque box is full, and let \(T=1\) mean taking both boxes. Monetary utility is

\[
u=1{,}000{,}000B+1{,}000T.
\]

Assume the present choice cannot causally affect the earlier filling. Writing \(q=P(B=1\mid I)\), CDT obtains

\[
V_C(\text{one-box})=1{,}000{,}000q,
\]

\[
V_C(\text{two-box})=1{,}000{,}000q+1{,}000.
\]

Two-boxing is better by \$1,000 under either fixed box content.

For an evidential comparison, suppose more specifically that

\[
P(B=1\mid\text{one-box})=0.99,
\qquad
P(B=1\mid\text{two-box})=0.01.
\]

These conditional probabilities require more specification than merely saying the predictor has 99% overall accuracy. They give

\[
V_E(\text{one-box})=\$990{,}000,
\qquad
V_E(\text{two-box})=\$11{,}000.
\]

EDT therefore recommends one-boxing.

CDT does not deny the predictive association. It denies that switching the present action changes the already-fixed box content. Its counterfactual varies the action while preserving that content; the evidential comparison associates different actions with different contents.

This distinction explains both CDT’s appeal and its vulnerability. Two-boxing dominates when the contents are held fixed, yet one-boxers tend to become much richer. Whether dominance or predictive success should govern rational choice is precisely the dispute—not something settled by the arithmetic.

## 5. Policies, commitments, and other agents

A **policy** specifies actions for multiple possible information states:

\[
\pi:\mathcal H\to\mathcal A,
\]

where \(\mathcal H\) is the set of possible observation histories.

CDT can evaluate policies when adopting or installing a policy is an available intervention:

\[
V_C(\pi\mid I_0)
=
\mathbb E\!\left[
u(O_{\operatorname{do}(\Pi=\pi)})
\mid I_0
\right].
\]

The calculation must include the policy’s effects on later observations, other agents, and future actions. One cannot simply hold a future observation history fixed while changing a policy that helps generate it.

Consider a Newcomb-like situation in which the player can install a binding one-boxing mechanism before the predictor examines the player. If the predictor responds causally to that mechanism, CDT can favor installation. With perfect recognition and commitment cost \(c\), this may yield \$1,000,000 minus \(c\), rather than the \$1,000 associated with a recognized two-boxing mechanism.

There is no retroactive influence. Earlier commitment affects later prediction.

However, merely evaluating an abstract policy at the final choice does not create control over earlier events. Any policy-level analysis must specify the intervention, its timing, and whether commitment is genuinely available. The reference does not settle these implementation questions.

The same issue appears in games. Suppose a prisoner’s-dilemma player receives:

| Own action | Other cooperates | Other defects |
|---|---:|---:|
| Cooperate | 3 | 0 |
| Defect | 5 | 1 |

If the other player’s action is causally unaffected by the present choice, and its probability of cooperation is \(s\), then

\[
V_C(C)=3s,\qquad V_C(D)=5s+(1-s)=1+4s.
\]

Defection wins for every \(s\).

This remains true if the opponent is a highly correlated “twin,” provided the dependence is not causal. Conversely, if present behavior influences future cooperation, reputation, or an enforceable agreement, those effects must enter CDT’s model. CDT does not generally prescribe selfishness or defection.

## 6. Self-evidence and unstable deliberation

The hardest objections concern actions that reveal information about the agent’s own causal situation.

### The psychopath button

In the reference’s example, Paul can press a button that kills all psychopaths. He values their removal but strongly prefers living among them to dying. He also believes that pressing would be strong evidence that he is himself a psychopath.

Let \(p\) be his current probability of being a psychopath. Normalize abstention’s utility to zero. Suppose pressing gives gain \(g>0\) if he is not a psychopath and loss \(d>0\) if he is. Then

\[
V_C(\text{press})=(1-p)g-pd.
\]

The simple causal calculation recommends pressing exactly when

\[
p<\frac{g}{g+d}.
\]

Thus the verbal scenario does not establish an unconditional CDT recommendation. Pressing requires a sufficiently low current probability of being a psychopath.

Nevertheless, Egan’s objection remains substantial: Paul may regard actually deciding to press as overwhelming evidence that this low probability was mistaken. Should deliberation incorporate that anticipated self-information?

The reference reports Joyce’s response that CDT can use evidence about one’s inclinations or likely behavior. A natural operational distinction is:

- Update on actual evidence, including observed motives and dispositions.
- Do not automatically treat every hypothetical intervention as evidence about its ordinary causes.

This distinction preserves the causal–evidential contrast. But it leaves a difficult question: when does deliberation itself produce new evidence? The supplied article does not establish a uniquely accepted rule.

### Prediction and instability

Death in Damascus dramatizes this difficulty. Death predicts which of two cities the agent will occupy and waits there.

If the agent currently assigns probability \(p\) to Death being in Damascus, the causal survival values are

\[
V_C(\text{Damascus})=1-p,
\qquad
V_C(\text{elsewhere})=p.
\]

But concluding “I will go elsewhere” may provide evidence that Death predicted elsewhere, changing \(p\) and reversing the recommendation.

CDT can represent the predictive correlation; the problem is not mathematical inability. The problem is whether a recommendation remains acceptable after the agent learns what it is inclined to do. Requirements of deliberative stability or **ratifiability** address this concern, but add constraints beyond elementary one-step maximization.

### The adversarial offer

The reference also describes two boxes, each costing \$1. A seller placed \$3 in every box she predicted the buyer would not acquire.

At least one box contains \$3. Consequently, with fixed current beliefs,

\[
\mathbb E[\text{contents of box 1}]
+
\mathbb E[\text{contents of box 2}]
\ge 3.
\]

At least one box therefore has causal expected contents of at least \$1.50. Simple CDT recommends buying a box.

Yet if the seller correctly predicts the purchased box with probability \(0.75\), the buyer’s realized expected net return is

\[
0.75(-1)+0.25(2)=-\$0.25.
\]

The action-by-action causal calculation favors purchase, while the predictor’s success makes purchasing systematically unprofitable.

Such examples motivate the money-loss objections discussed in the reference. Their interpretation also depends on whether the stipulated predictor, available randomization, and the agent’s beliefs can be modeled consistently. They expose a genuine pressure point rather than automatically settling every version of CDT.

## 7. A practical procedure

For an unfamiliar problem, proceed in this order:

1. **Specify the decision point.** What actions or commitments are available now?
2. **Specify utility.** Include all relevant benefits, harms, and costs.
3. **Separate observation from intervention.** What does the action reveal, and what does it change?
4. **Model dependencies.** Identify common causes, downstream effects, predictive relationships, and uncertainty about them.
5. **Update on current evidence.** Include genuine information about one’s own dispositions.
6. **Evaluate interventions using one current posterior.**
7. **Check deliberative and temporal stability.** Could new self-information or later reconsideration reverse the recommendation?

The last check identifies possible problems; it is not, by itself, a universally agreed repair. Where different plausible causal models recommend different actions, the honest result is conditional: CDT recommends one action under one model and another under a rival model.

## Sources

The primary reference is Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” supplied revision 1381555528, licensed CC BY-SA 4.0.

Key works identified there include Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1981); Lewis, “Causal Decision Theory” (1981); Egan, “Some Counterexamples to Causal Decision Theory” (2007); Joyce, “Regret and Instability in Causal Decision Theory” (2012); and Oesterheld and Conitzer, “Extracting Money from Causal Decision Theorists” (2021). The structural-model implementation and numerical illustrations above are additional exposition.

## Conclusion

CDT asks which available intervention has the best expected consequences—not which action would be the best news. Its strength is a disciplined distinction between influence and evidence. Its unresolved difficulties concern how to construct counterfactuals, incorporate self-information, and evaluate commitments across time. Used carefully, CDT is therefore both an optimization rule and a demand for explicit causal modeling: identify what can change, preserve what cannot, and make uncertainty about that distinction visible.