# Evidential Decision Theory: Choosing by What an Action Tells You

Suppose an action would be excellent news about your prospects, even though performing it would not cause those prospects to improve. Should that count in its favor?

Evidential decision theory (EDT) answers yes. It evaluates an action by the expected desirability of the world conditional on performing that action. The reference article summarizes its advice as: “do what you most want to learn that you will do.”

This differs from asking which action would produce the best consequences through its causal effects. Usually these questions agree. They can diverge when an action is evidence about something it does not control: an earlier prediction, another person’s decision, or an underlying medical condition.

The attraction of EDT is that such evidence can be highly relevant to whether things go well for the agent. The objection is that choosing favorable evidence may amount to selecting good news rather than improving reality. Understanding the theory requires making both sides precise.

## 1. The basic mathematical rule

Let:

- \(I\) represent the agent’s current information;
- \(\mathcal A\) be the set of available actions;
- \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive outcomes;
- \(u(O_j)\) be the utility of outcome \(O_j\);
- \(P\) represent the agent’s probabilistic beliefs.

EDT assigns action \(a\) the value

\[
V_I(a)
=
\mathbb E[u(O)\mid I,A=a]
=
\sum_j P(O_j\mid I,A=a)u(O_j).
\]

It recommends any action satisfying

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_I(a).
\]

Here \(A\) is a random variable representing what the agent does. Conditioning on \(A=a\) means considering the information that this action occurs.

The reference article gives this rule without explicitly displaying background information \(I\). Including it matters: an action can be informative given one information set and uninformative given another.

Utilities should encompass everything the agent values, including action costs, other people’s welfare, and risk attitudes. Monetary examples below assume utility is linear in money. With nonlinear utility, one must evaluate each monetary outcome through \(u\), rather than simply maximize expected dollars.

A useful equivalent formulation separates actions from background states. Suppose \(S\) describes relevant circumstances and the resulting utility is \(u(a,s)\). Then

\[
V_I(a)=\sum_s P(s\mid I,A=a)u(a,s).
\]

The distinctive feature is that **the distribution over states may differ between candidate actions**. Choosing one action can be evidence for a different underlying situation than choosing another.

These distributions must come from a common, coherent probabilistic model. EDT does not license inventing a favorable conditional distribution separately for each action.

## 2. Evidence, causation, and counterfactuals

The reference contrasts EDT with causal decision theory (CDT). In its presentation, CDT evaluates probabilities of counterfactual outcomes:

\[
U_I(a)
=
\sum_j
P(a\mathrel{\Box\!\rightarrow}O_j\mid I)\,u(O_j),
\]

where the counterfactual concerns what would happen if action \(a\) were performed.

In a suitable causal model, this contrast is often expressed as

\[
\underbrace{P(O\mid I,A=a)}_{\text{conditioning}}
\qquad\text{versus}\qquad
\underbrace{P(O\mid I,\operatorname{do}(A=a))}_{\text{intervention}}.
\]

The intervention notation is an explanatory addition to the source, not its general definition of CDT.

Conditioning retains the information carried by an action’s occurrence. An intervention instead fixes the action while severing its ordinary causal dependence on upstream variables.

Suppose an unobserved variable \(S\) influences both an agent’s choice and the eventual outcome:

\[
S\longrightarrow A,
\qquad
S\longrightarrow O,
\qquad
A\longrightarrow O.
\]

Learning \(A=a\) can update beliefs about \(S\). An intervention setting \(A=a\) does not, merely by itself, provide the same evidence about \(S\).

This is why saying “the state is already fixed” does not settle an evidential decision. A fixed but unknown fact can still be learned about. One’s choice need not change the past to be evidence about it.

EDT therefore need not deny causal facts or prohibit counterfactual reasoning. Its distinctive prescription is that action evaluation uses conditional expected utility rather than replacing conditioning with a causal counterfactual. The imagined supposition is approximately:

> Given everything I currently know, how desirable should I expect the world to be upon learning that I perform this action?

It is not:

> Holding the relevant background circumstances fixed, what would changing my action accomplish?

When the action is independent of the background state,

\[
P(s\mid I,A=a)=P(s\mid I),
\]

and the causal model uses that same state distribution, the distinction disappears:

\[
V_I(a)=\sum_s P(s\mid I)u(a,s).
\]

This explains why EDT agrees with ordinary causal reasoning in many everyday choices. If selecting an umbrella provides no additional evidence about the weather, both theories evaluate its protection and inconvenience against the same weather probabilities.

## 3. Newcomb’s problem: evidence about a prediction

Newcomb’s problem makes the disagreement especially clear.

A transparent box contains \(b=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A reliable predictor has already filled the opaque box:

- if it predicted that you would take only the opaque box, it put \(M\) inside;
- if it predicted that you would take both boxes, it left the opaque box empty.

You choose between one-boxing, \(B\), and two-boxing, \(T\).

Write

\[
q_B=P(\text{opaque box full}\mid I,B),
\qquad
q_T=P(\text{opaque box full}\mid I,T).
\]

EDT gives

\[
V_I(B)=Mq_B,
\qquad
V_I(T)=b+Mq_T.
\]

Thus one-boxing is recommended precisely when

\[
M(q_B-q_T)>b.
\]

This inequality is more informative than the slogan “trust the predictor.” It identifies the evidential advantage needed to outweigh the guaranteed extra money.

The reference uses

\[
q_B=0.99,\qquad q_T=0.01,
\]

which yields

\[
V_I(B)=\$990{,}000,
\qquad
V_I(T)=\$11{,}000.
\]

One-boxing wins decisively.

There is an important modeling qualification. A predictor’s *overall* accuracy of \(99\%\) does not, by itself, establish both action-conditional probabilities above. Overall accuracy is an average across choices; conditional accuracy can differ between one-boxers and two-boxers. The source’s numerical calculation therefore requires the displayed conditional reliability assumptions, not merely an aggregate success rate.

Under the symmetric specification \(q_B=p\) and \(q_T=1-p\), one-boxing is preferred when

\[
p>\frac{1+b/M}{2}.
\]

For these prizes, the threshold is \(0.5005\).

CDT’s standard recommendation is two-boxing: whatever the opaque box already contains, taking the transparent box adds \(\$1{,}000\). EDT does not dispute that comparison with the contents held fixed. It disputes using a fixed distribution over those contents when evaluating the two actions. Learning that you one-box and learning that you two-box are, by hypothesis, very different evidence.

## 4. Psychological twins: evidence about another decision

The reference’s twin prisoner’s dilemma uses the same structure without a predictor.

Two psychologically identical agents independently choose cooperation, \(C\), or defection, \(D\). Their individual payoffs are

\[
\begin{array}{c|cc}
 & \text{Twin }C & \text{Twin }D\\ \hline
C & 5 & 0\\
D & 10 & 1
\end{array}
\]

Holding the twin’s action fixed, defection always pays more. Nevertheless, suppose their decisions match perfectly:

\[
P(\text{Twin }C\mid C)=1,
\qquad
P(\text{Twin }D\mid D)=1.
\]

Then

\[
V(C)=5,\qquad V(D)=1,
\]

so EDT recommends cooperation.

This is not an appeal to altruism or communication. The agent can care exclusively about her own payoff. Her choice is evidence about what a correlated decision-maker does.

For an imperfect analogue, define

\[
q_C=P(\text{Twin }C\mid C),
\qquad
q_D=P(\text{Twin }C\mid D).
\]

The values become

\[
V(C)=5q_C,
\qquad
V(D)=10q_D+(1-q_D)=1+9q_D.
\]

Cooperation is therefore justified exactly when

\[
5q_C>1+9q_D.
\]

If the choices are independent, \(q_C=q_D=q\), defection wins. Psychological resemblance alone is insufficient; it must support the relevant conditional probabilities.

Likewise, logical or computational similarity between agents does not automatically provide a unique probabilistic model. EDT can use a justified dependency, but its basic formula does not determine how strong that dependency should be.

## 5. The objection: choosing good news rather than good outcomes

The reference reports David Lewis’s criticism that EDT promotes an irrational policy of “managing the news.” A simple additional example illustrates the concern.

Suppose an unobserved condition \(H\) both causes an illness and increases a desire for a harmless dessert. Eating the dessert does not affect the illness. Let

\[
P(H\mid \text{eat})=0.8,
\qquad
P(H\mid \text{decline})=0.1.
\]

The dessert gives one utility unit; the illness costs \(100\). Then

\[
V(\text{eat})=1-100(0.8)=-79,
\]

while

\[
V(\text{decline})=-100(0.1)=-10.
\]

EDT recommends declining.

But under the stipulated causal structure, refusing dessert does not remove the condition. Eating adds one unit of enjoyment in either underlying state. Critics regard the evidential recommendation as sacrificing a genuine benefit to avoid an ominous sign.

The example is deliberately fictional; it is not a claim about any actual food or disease.

An evidentialist can reply that the conditional expectations are nevertheless the correct expectations upon learning which choice occurs. This response exposes the fundamental dispute rather than resolving it: should rational choice track favorable conditional prospects even when the difference is noncausal?

Background information can change the verdict. If the agent learns whether \(H\) holds, and that information screens off the action–illness association, then

\[
P(H\mid I,\text{eat})
=
P(H\mid I,\text{decline}).
\]

Eating now wins by one utility unit.

This shows why an EDT analysis must condition on the agent’s actual information. It does not show that all troubling correlations disappear. Nor may the analyst simply assume knowledge of the hidden condition.

## 6. What counts as an action: moves, randomizations, and policies

The source gives an action-level formula but does not supply a complete theory of sequential choice. Applying EDT to policies therefore requires additional specification.

A policy is a rule mapping information histories to actions:

\[
\pi:\mathcal H\longrightarrow\mathcal A.
\]

For example, a medical policy might prescribe testing first, then choosing treatment according to the result.

A natural extension is to introduce a random variable \(\Pi\) representing the agent’s policy and evaluate

\[
V_I(\pi)
=
\mathbb E[u(O)\mid I,\Pi=\pi].
\]

This is an operational proposal, not a further rule established by the reference. It requires a meaningful probabilistic model of policy adoption and any associated evidence.

Policy conditioning can matter when predictors or similar agents respond to an entire decision procedure rather than an isolated movement. But one must not assume that changing a policy automatically changes every correlated agent. Any such conclusion must be justified by the model.

Randomization makes the distinction especially clear. Suppose the agent uses a fresh coin statistically independent of a hidden state. The realized coin-selected action may provide no evidence about that state. By contrast, adopting the randomized policy might be informative about the agent’s dispositions, and those dispositions might matter to a predictor.

Consequently, these are different candidate conditioning events:

\[
\Pi=\pi,
\qquad
\text{coin result}=r,
\qquad
A=a.
\]

They cannot be exchanged without checking their dependencies.

Sequential choice raises another issue. Before observing a result, an agent might favor a complete policy. After observing it, she might favor a different local action. The relevant expressions are different:

\[
\mathbb E[u\mid I,\Pi=\pi]
\quad\text{and}\quad
\mathbb E[u\mid I,H=h,A=a].
\]

EDT’s one-step formula does not guarantee that these evaluations produce a dynamically stable plan in every problem. An analysis must say whether it evaluates an initial commitment, a policy without commitment, or repeated local choices. Quietly moving between them can manufacture apparent solutions or contradictions.

## 7. Making the prescription operational

EDT’s calculation is straightforward once its inputs are fixed. Constructing those inputs is often the real difficulty.

### Keep the information set fixed

All candidate actions should initially be evaluated relative to the same current information \(I\). One must not compare an action evaluated before receiving a diagnostic signal with another evaluated after receiving it.

At the same time, the conditional distributions

\[
P(O\mid I,A=a)
\]

should include the evidence supplied by the hypothesized action itself. Omitting that evidence simply replaces EDT with a different procedure.

### Distinguish prediction from recommendation

The variable \(A\) describes what the agent does; maximizing \(V_I\) recommends what to do. A predictive model of a deliberating agent may therefore face self-reference.

If the agent already assigns probability one to choosing the recommended act, all alternatives have probability zero. Ordinary conditional probability then cannot evaluate them:

\[
P(O\mid I,A=a)
=
\frac{P(O,A=a\mid I)}{P(A=a\mid I)}.
\]

When the denominator vanishes, this expression is undefined.

The reference does not resolve this problem. A reasonable operational approach is to use a pre-decision predictive model giving positive probability to the contemplated alternatives, when that is coherent. Another is to specify small probabilities of execution errors and examine limiting values. These are modeling proposals, however; different error models may yield different conditionals.

Thus “just condition on choosing otherwise” is not always a complete instruction.

### Audit the dependencies

A useful workflow is:

1. Specify available actions or policies and the actual information set.
2. Define complete outcomes and their utilities.
3. Construct one joint model connecting actions, hidden states, predictors, and other agents.
4. Derive the action-conditional outcome distributions.
5. Maximize conditional expected utility and test sensitivity to uncertain assumptions.

A parallel causal analysis can identify where the disagreement arises. It should remain a comparison, not silently replace EDT’s conditioning rule.

The central diagnostic question is:

> What does learning this particular action tell me, beyond what I already know?

If the answer is “nothing relevant about the background circumstances,” standard causal and evidential calculations will often coincide.

## 8. Wider implications and unresolved applications

The reference mentions Sleeping Beauty and disputes over Dutch-book arguments. In that problem, a fair coin determines whether an amnesiac subject awakens once or twice. Evaluating bets requires specifying whether payoffs occur per awakening or per experiment, what information the subject possesses, and how accepting one offer is correlated with accepting another.

EDT alone does not settle those choices of model. The source reports competing claims, including Conitzer’s argument that adopting EDT does not generally protect halfers from Dutch books.

The article also mentions an “evidentialist’s wager”: correlations with many other decision-makers could make evidential considerations unusually consequential. Such reasoning requires both justified correlations and a utility function that values the relevant outcomes. Correlation by itself does not enlarge an egoistic agent’s utility stakes.

These applications reinforce the same lesson. EDT is a criterion for evaluating a specified model, not a substitute for specifying one.

## Sources and further reading

The account above follows the supplied article, with the policy formulation, operational recommendations, and additional derivations explicitly developed here.

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” supplied revision 1373679688.
- Gibbard, A., and Harper, W. L. (1976), *Counterfactuals and Two Kinds of Expected Utility*.
- Ahmed, A. (2021), *Evidential Decision Theory*.
- Lewis, D. (1981), “Causal Decision Theory.”
- Conitzer, V. (2015), “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.”

## Conclusion

EDT recommends the action with the highest expected utility conditional on its occurrence. Its distinctive commitment is to retain relevant noncausal evidence rather than evaluate actions solely through their causal effects. That yields one-boxing in Newcomb’s problem and cooperation between sufficiently correlated twins, but also motivates the objection that EDT manages news instead of improving outcomes. Applying it responsibly requires explicit information sets, justified dependencies, well-defined conditioning events, and a clear distinction between individual actions and whole policies.