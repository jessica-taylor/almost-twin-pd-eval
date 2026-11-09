# Evidential Decision Theory: Choosing Actions as Evidence

A decision can matter in two ways. It can change what happens, and it can indicate what is already true—or what other agents will do. These roles usually align: taking an effective medicine both helps recovery and provides evidence of recovery. But prediction, psychological similarity, and hidden common causes can pull them apart.

**Evidential decision theory** (EDT) evaluates actions by their evidential relationship to desirable outcomes. Its guiding question is:

> If I learned that I had taken this action, how good would I expect the outcome to be?

The supplied reference describes this as choosing the action with the highest “news value.” This is not a recommendation to seek comforting beliefs. The object of evaluation remains the outcome, not the pleasure of hearing good news.

EDT has a compact mathematical definition. Applying it, however, requires care about the probability model, the agent’s information, and exactly what counts as the action under consideration.

## 1. The basic rule

Let \(\mathcal A\) be a finite set of feasible actions, \(A\) the random variable representing the agent’s eventual action, and \(I\) the information available before choosing. Let \(O_1,\ldots,O_n\) be mutually exclusive, exhaustive outcomes, with utility \(u(O_j)\).

EDT assigns action \(a\) the value

\[
V_I(a)
=
\mathbb E[u(O)\mid I,A=a]
=
\sum_j P(O_j\mid I,A=a)u(O_j),
\]

and recommends

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_I(a).
\]

This is the reference article’s formula, made explicit about background information. For continuous outcomes, the sum becomes an integral. Conditional expectations must exist, and ordinary conditioning requires \(P(A=a\mid I)>0\). Zero-probability alternatives need additional treatment.

Utilities represent preferences, including attitudes toward risk. Dollar amounts may substitute for utilities only under an assumption such as risk neutrality. Multiplying utility by a positive constant, or adding the same constant to every outcome, leaves the recommendation unchanged.

An equivalent representation separates actions from background states. Suppose \(S\) records relevant circumstances and the complete outcome has utility \(u(a,s)\). Then

\[
V_I(a)=\sum_s P(S=s\mid I,A=a)\,u(a,s).
\]

The distinctive feature is that the distribution over states may vary with the proposed action. EDT does not necessarily evaluate every action against one fixed distribution \(P(S\mid I)\).

The probabilities should describe this agent in this situation. Correlations among unrelated people are not automatically informative about the present choice. Conversely, the fact that an action is available for deliberate selection does not, by itself, make it statistically independent of everything else.

The central modeling task is therefore to specify a credible joint distribution over actions and outcomes.

## 2. Conditioning is not intervention

The reference contrasts EDT with causal decision theory (CDT), which evaluates the outcomes of counterfactually performing an action. Its notation is

\[
C_I(a)=\sum_j P(a\mathrel{\Box\!\rightarrow}O_j\mid I)u(O_j).
\]

In a standard causal-model implementation, the corresponding calculation is

\[
C_I(a)=\mathbb E[u(O)\mid I,\operatorname{do}(A=a)].
\]

Here \(\operatorname{do}(A=a)\) means setting the action while breaking its usual dependence on its causes. Conditioning on \(A=a\), by contrast, preserves information carried by the action about those causes.

Suppose a hidden variable \(H\) influences both the action and an outcome:

\[
H\longrightarrow A,\qquad H\longrightarrow O.
\]

There may also be an arrow \(A\longrightarrow O\). EDT retains information flowing through all these statistical relationships. An intervention cuts the incoming influence on \(A\), while retaining its causal effects on \(O\).

For a background state \(S\) whose distribution the intervention leaves unchanged,

\[
C_I(a)=\sum_s P(S=s\mid I)u(a,s),
\]

whereas EDT uses \(P(S=s\mid I,A=a)\). If these distributions agree for every action, the theories agree.

Thus EDT does not ignore causation: ordinary causal effects appear in conditional outcome probabilities. Rather, it declines to discard additional, noncausal evidence.

This also clarifies its treatment of counterfactual questions. EDT translates “What if I chose \(a\)?” into an evidential supposition: evaluate worlds compatible with choosing \(a\), using their conditional probabilities. It does not automatically hold fixed everything outside the action’s causal future. Nor does it claim that choosing an action physically changes the past.

## 3. Newcomb’s problem: evidence about an earlier prediction

In Newcomb’s problem, a transparent box contains \(b=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box precisely when it predicted that the agent would take only that box.

Let \(B\) mean taking only the opaque box and \(T\) mean taking both. Write

\[
q_B=P(\text{opaque box full}\mid I,A=B),
\]

\[
q_T=P(\text{opaque box full}\mid I,A=T).
\]

Assuming linear utility for money,

\[
V_I(B)=Mq_B,\qquad V_I(T)=b+Mq_T.
\]

Consequently, EDT recommends one-boxing exactly when

\[
M(q_B-q_T)>b.
\]

The reference uses \(q_B=0.99\) and \(q_T=0.01\), giving

\[
V_I(B)=\$990{,}000,\qquad V_I(T)=\$11{,}000.
\]

One-boxing wins because it is powerful evidence that the opaque box is full.

A small but important modeling qualification concerns “99% accuracy.” Overall prediction accuracy alone does not determine these two conditional probabilities. Different error rates across actions, combined with different action frequencies, can produce the same aggregate accuracy. The calculation requires the relevant conditional probabilities, not merely a headline reliability figure.

CDT instead reasons that the box’s contents are already fixed. Holding those contents fixed, taking both boxes gives an additional \(\$1{,}000\). Its recommendation is therefore to two-box.

This illustrates EDT’s rejection of a familiar dominance argument. For either fixed box content, two-boxing pays more. But EDT does not assign the same weights to those contents when evaluating the two actions.

The disagreement is not arithmetic. It concerns which comparison matters: an intervention holding the earlier prediction fixed, or conditioning on an action that reveals information about that prediction.

## 4. Psychological twins and correlated decisions

The reference’s twin prisoner’s dilemma supplies a different source of dependence. Two isolated agents have closely matching reasoning processes. Each chooses cooperation \(C\) or defection \(D\). The focal agent receives

\[
\begin{array}{c|cc}
&\text{Twin cooperates}&\text{Twin defects}\\ \hline
C&5&0\\
D&10&1
\end{array}
\]

in utility units.

Define

\[
p_C=P(\text{twin cooperates}\mid I,A=C),
\qquad
p_D=P(\text{twin cooperates}\mid I,A=D).
\]

Then

\[
V_I(C)=5p_C,\qquad V_I(D)=1+9p_D.
\]

EDT cooperates when

\[
5p_C>1+9p_D.
\]

For perfect psychological correspondence, \(p_C=1\) and \(p_D=0\), so cooperation yields value \(5\), against defection’s \(1\).

No altruism has been assumed: the utility function contains only the focal agent’s payoff. Cooperation follows from the informational connection between the decisions.

But merely calling someone a “twin” is insufficient. If the choices are independent conditional on current information, then \(p_C=p_D=p\), and

\[
V_I(D)-V_I(C)=1+4p>0.
\]

EDT then defects. Psychological similarity matters only insofar as it supports the relevant conditional dependence. Sharing a decision-theoretic label, without further information about reasoning, inputs, and circumstances, does not establish perfect correlation.

## 5. The objection: managing the news

The reference reports David Lewis’s criticism that EDT promotes an irrational policy of “managing the news.” A deliberately artificial example makes the concern precise.

Suppose an unknown lesion \(H\) guarantees a later loss of \(100\) utility units. A harmless indulgence gives an immediate benefit of \(10\). The lesion does not make the indulgence harmful, but does make choosing it more likely:

\[
P(H)=\tfrac12,\qquad
P(A=\text{indulge}\mid H)=0.9,
\]

\[
P(A=\text{indulge}\mid\neg H)=0.1.
\]

By Bayes’ rule,

\[
P(H\mid\text{indulge})=0.9,\qquad
P(H\mid\text{abstain})=0.1.
\]

With utility

\[
u(a,H)=10\,\mathbf 1_{\{a=\text{indulge}\}}
-100\,\mathbf 1_{\{H\}},
\]

EDT obtains

\[
V(\text{indulge})=10-90=-80,
\qquad
V(\text{abstain})=-10.
\]

It abstains, although abstention cannot remove the lesion.

A causal intervention leaves the lesion probability at one-half:

\[
C(\text{indulge})=-40,\qquad
C(\text{abstain})=-50.
\]

The causal recommendation is to enjoy the harmless benefit.

This example is an illustration added here, not a worked example in the supplied article. It exposes the philosophical issue directly. EDT treats the dependence much as it treats prediction in Newcomb’s problem; critics deny that an action’s favorable evidential significance is sufficient reason to choose it.

The outcome can change if the agent has additional information. If observed evidence \(X\) screens off the relationship,

\[
P(H\mid I,X,A)=P(H\mid I,X),
\]

then the lesion term has the same conditional expectation under both actions, and EDT recommends indulging.

This is not a universal solution. Screening off must follow from the information actually available; one cannot simply assume it to obtain a preferred verdict. Conversely, one should not preserve a population-level correlation after learning facts that render it irrelevant.

Notice also that an action-independent physical harm cannot automatically be omitted from an EDT calculation. Although the action does not cause the harm, its *conditional expectation* can differ across actions.

## 6. What exactly is the action?

The formula is simple only after the conditioning event has been identified.

Choosing an indulgence because of a lesion-related desire need not provide the same evidence as indulging because an independent coin instructed it. If, conditional on a fixed procedure, an independent coin alone selects the action, the resulting action can be uninformative about the lesion.

That does not establish that adopting the procedure was uninformative. The decision to use a coin might itself correlate with hidden circumstances. Randomization is therefore not an automatic way to erase every evidential dependence.

A sound model should distinguish:

- selecting a decision procedure;
- observing a random device;
- implementing the resulting physical action.

These events may have different evidential values.

Self-knowledge raises a related difficulty. An agent should condition on its available evidence, including relevant facts about its desires and reasoning. But if its information already entails its final action, every alternative has probability zero.

The basic conditional-probability formula then provides no answer. One possible extension uses full-support approximations \(P_\varepsilon\), under which every feasible action has positive probability, and evaluates

\[
V_\varepsilon(a)=\mathbb E_{P_\varepsilon}[u\mid I,A=a].
\]

However, different accounts of rare mistakes or departures can produce different limits as \(\varepsilon\to0\). A random implementation error may carry different evidence from an unusual deliberative conclusion.

The supplied article does not settle this issue. A reasonable operational approach is to use a pre-choice model that preserves genuine uncertainty about feasible actions, and to specify any limiting model explicitly. That is a modeling proposal, not a consequence of the source’s equation.

## 7. From individual actions to policies

Many problems concern not one action but a rule for responding to future observations. Let a policy \(\pi\) map each possible information history \(h\) to an action \(\pi(h)\).

The reference gives an action-level rule, not a complete theory of sequential choice. A natural extension is to treat adopting a policy as the present action. If \(\Pi\) represents the adopted policy, define

\[
W_I(\pi)=\mathbb E[u(O)\mid I,\Pi=\pi].
\]

The probability model must include implementation of that policy and any evidence its adoption supplies about predictors, other agents, or hidden circumstances.

This extension is useful when a predictor forecasts a whole strategy, or when agents with similar reasoning choose matching policies. It does not mean conditioning on the simultaneous performance of actions at mutually exclusive future histories. Adopting a contingent rule is one event; executing every branch is not.

Policy selection also raises a commitment question. Should an agent optimize a policy now and follow it later, or reconsider at each future decision using

\[
V_h(a)=\mathbb E[u(O)\mid h,A=a]?
\]

The one-step EDT rule alone supplies no general guarantee that these perspectives agree. A commitment device may alter available actions; new information may alter evidential relationships.

My proposed operational interpretation is to evaluate a policy when its adoption is genuinely available, and evaluate later actions against the information and options then available. Where these recommendations conflict, the model must state whether commitment is possible and whether policy choice or later reconsideration governs behavior. Calling both “EDT” does not resolve that additional issue.

## 8. Applying EDT to unfamiliar cases

A practical analysis can proceed as follows.

**Specify the decision object.** Is the choice a physical act, a randomized procedure, or a contingent policy? Identify what can actually be selected.

**Fix the information.** Include relevant observations and self-knowledge available at that stage. Do not silently compare actions using different background information.

**Specify complete outcomes and utilities.** Include costs, risks, and all people whose welfare the agent values. Correlated decisions do not create extra utility unless their consequences matter under that utility function.

**Build the joint model.** Explain why actions carry information. Possible sources include prediction, shared psychology, hidden common causes, or common observations. Causal diagrams can clarify these dependencies without requiring a causal decision rule.

**Compute conditional expectations.** Use \(P(O\mid I,A=a)\), not an interventional distribution substituted without argument. Check that the action events have positive probability.

**Test sensitivity.** Which correlations drive the recommendation? Would additional evidence screen them off? Would a different account of prediction errors, randomization, or policy adoption reverse the result?

This procedure separates two questions often conflated in debates about EDT: whether its decision rule is defensible, and whether a particular probability model correctly represents the case.

## 9. Scope and sources

The supplied article also discusses Sleeping Beauty and Dutch-book arguments. It reports both a proposed evidential defense of assigning heads probability one-half and Conitzer’s criticism of that defense. It does not establish that EDT uniquely resolves the problem. A proper analysis must specify how awakenings, repeated offers, correlated acceptances, and total payoffs enter the model.

Likewise, the article reports an argument that correlation with many decision-makers can make EDT’s stakes especially large. This is a further argument about decision-making under theoretical uncertainty, not a theorem following from conditional expected utility alone.

The account above is based on:

- **Wikipedia contributors**, “Evidential decision theory,” [supplied revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), CC BY-SA 4.0.
- **Gibbard, A., and Harper, W. L.** (1976), *Counterfactuals and Two Kinds of Expected Utility*—the formal distinction attributed by the reference.
- **Ahmed, A.** (2021), *Evidential Decision Theory*, Cambridge University Press.
- **Conitzer, V.** (2015), “A Dutch book against sleeping beauties who are evidential decision theorists,” *Synthese* 192: 2887–2899.

The screening-off example, procedural distinctions, and proposed policy interpretation are explanatory developments beyond the supplied article’s explicit treatment.

## Conclusion

EDT maximizes expected utility conditional on performing an action. Its distinctive commitment is to retain evidential relationships even when they are not causal influences. That explains both its attraction in Newcomb-style prediction problems and its controversial recommendations in hidden-common-cause cases.

The arithmetic is straightforward; identifying the right conditional probabilities is not. A usable EDT analysis must make its information, action descriptions, dependencies, and utility function explicit—and acknowledge where policy choice or zero-probability alternatives require assumptions beyond the basic rule.