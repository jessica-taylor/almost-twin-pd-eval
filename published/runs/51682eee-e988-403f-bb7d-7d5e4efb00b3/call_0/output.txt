# Evidential Decision Theory: Choosing the Action That Is Best News

Evidential decision theory (EDT) asks a distinctive question: **which available action would be the best news about how things turn out?** It recommends the action with the highest expected utility conditional on that action being performed.

This differs from asking which action would *cause* the best outcome. Usually the two questions agree. Sometimes, however, an action is evidence about circumstances it cannot causally influence: a prediction already made, an unknown medical condition, or another person’s simultaneous decision. EDT treats those evidential relationships as relevant to choice.

The supplied reference article presents this conditional-expectation rule and illustrates it with Newcomb’s problem and a twin prisoner’s dilemma. The rule is mathematically compact, but applying it requires care about information, probability models, and what exactly counts as the object of choice.

## 1. The basic rule

Let:

- \(\mathcal A\) be a set of feasible actions;
- \(K\) represent the agent’s current information;
- \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive outcomes;
- \(u(O_j)\) be the utility of outcome \(O_j\).

EDT assigns action \(a\) the value

\[
V_K(a)=\sum_j P(O_j\mid A=a,K)\,u(O_j)
\]

and recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_K(a).
\]

Here \(A\) is a random variable representing the action actually performed. For continuous outcomes, replace the sum by an appropriate conditional expectation:

\[
V_K(a)=\mathbb E[u(O)\mid A=a,K].
\]

The reference uses essentially this definition, without explicitly writing the background information \(K\). Including \(K\) matters: learning something relevant can change an action’s evidential significance.

An equivalent formulation separates actions from uncertain circumstances. Let \(S\) describe the relevant state of the world, and let \(u(a,s)\) include every consequence valued by the agent. Then

\[
V_K(a)=\sum_s P(S=s\mid A=a,K)\,u(a,s).
\]

This is often the most useful form for calculations.

Utilities need not be monetary. They may represent health, other people’s welfare, risk attitudes, or combinations of these. The dollar-valued examples below assume utility is linear in money. Otherwise, utilities—not dollar amounts—must be averaged.

The “news” metaphor does not mean that learning pleasant facts is itself the objective. Rather, the hypothetical announcement “you perform \(a\)” identifies a conditional distribution over outcomes. EDT evaluates those outcomes using the agent’s ordinary preferences.

Nor does EDT recommend conditioning on arbitrary desirable events. “I win the lottery” is not an available action merely because it would be excellent news. Feasibility remains a separate requirement.

## 2. Dependence without causal influence

The central contrast with causal decision theory concerns the probabilities used.

In a structural causal model, a convenient representation of causal evaluation is

\[
V^{\mathrm{CDT}}_K(a)
=
\mathbb E[u(a,S)\mid \operatorname{do}(A=a),K].
\]

The intervention notation means that the action is externally set to \(a\), breaking its ordinary dependence on its causes. This is a useful representation of the contrast; the reference itself expresses causal evaluation using probabilities of counterfactual conditionals.

EDT instead uses

\[
P(S\mid A=a,K).
\]

Conditioning preserves the information carried by the action. An intervention generally does not.

For example, suppose an unobserved disposition \(T\) influences both my choice and someone’s earlier prediction:

\[
T\longrightarrow A,
\qquad
T\longrightarrow \text{prediction}.
\]

Learning my action can then provide evidence about the prediction, even though my present action does not cause anything in the past.

EDT requires no backward causation here. It says that the action and the earlier prediction can be statistically connected through their shared determinants.

When the conditional and intervention distributions agree, EDT and CDT agree. Randomized experiments often create this agreement by severing confounding relationships. But merely describing two actions as “available” does not establish statistical independence between the eventual action and the surrounding world.

Thus EDT’s question is not “What would happen if an external mechanism forced this movement?” It is “What should I expect, given that this is the action I perform?” The philosophical dispute concerns which question should govern deliberate choice.

## 3. Newcomb’s problem

Newcomb’s problem makes the distinction vivid.

A transparent box contains \(c=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box:

- it contains \(M\) if the predictor predicted that the agent would take only that box;
- otherwise it is empty.

The agent chooses between one-boxing, \(A=1\), and taking both boxes, \(A=2\). Let \(F\) mean that the opaque box is full.

For arbitrary relevant probabilities,

\[
V(1)=M P(F\mid A=1),
\]

while

\[
V(2)=c+M P(F\mid A=2).
\]

Consequently, EDT recommends one-boxing exactly when

\[
M\bigl[P(F\mid A=1)-P(F\mid A=2)\bigr]>c.
\]

This inequality exposes the reasoning: the evidential advantage of one-boxing must outweigh the transparent box’s contents.

The reference’s numerical example effectively assumes

\[
P(F\mid A=1)=0.99,
\qquad
P(F\mid A=2)=0.01.
\]

Under those assumptions,

\[
V(1)=\$990{,}000,
\qquad
V(2)=\$11{,}000.
\]

EDT therefore one-boxes.

A modeling qualification matters. Saying only that a predictor is “99% accurate” does not, by itself, determine both conditional probabilities. Overall accuracy depends on the frequencies of different actions and errors. The displayed calculation requires the action-conditional reliabilities just stated, or other assumptions that imply them.

CDT instead holds the already-fixed contents causally unaffected by the present action. For either possible content, taking both boxes yields another \$1,000. It therefore two-boxes.

EDT does not dispute that state-by-state comparison. It disputes using the same probability distribution over box contents to evaluate both actions. On the evidential model, people who one-box and people who two-box face very different conditional prospects.

Neither side need believe that reaching toward the transparent box empties the opaque one. Their disagreement concerns the decision-relevance of evidence about what is already there.

## 4. Cooperating with a psychological twin

The reference’s second main example involves two isolated agents with exactly analogous reasoning processes. Each chooses cooperation, \(C\), or defection, \(D\). The first agent’s payoffs are

\[
\begin{array}{c|cc}
&\text{Twin }C&\text{Twin }D\\ \hline
C&5&0\\
D&10&1
\end{array}
\]

Suppose their actions match perfectly:

\[
P(\text{Twin }C\mid A=C)=1,
\qquad
P(\text{Twin }D\mid A=D)=1.
\]

Then

\[
V(C)=5,\qquad V(D)=1,
\]

so EDT cooperates.

This is not an appeal to altruism. The utilities are the agent’s own payoffs. Cooperation is recommended because her action is evidence about her twin’s action.

Perfect similarity is unnecessary. Write

\[
p_C=P(\text{Twin }C\mid A=C),
\qquad
p_D=P(\text{Twin }C\mid A=D).
\]

Then

\[
V(C)=5p_C,
\qquad
V(D)=10p_D+(1-p_D)=1+9p_D.
\]

Cooperation is preferred precisely when

\[
5p_C>1+9p_D.
\]

Under the symmetric specification \(p_C=q\) and \(p_D=1-q\), this becomes

\[
q>\frac57.
\]

Thus EDT does not recommend cooperation with every person who resembles oneself. The required dependence must be supported by the probability model. If the twin’s action is independent of one’s own, defection wins: it pays more against either fixed opponent action.

## 5. The objection: are we merely managing the news?

The reference reports David Lewis’s criticism that EDT encourages “managing the news,” and James Joyce’s insistence that rational choice should track causal efficacy rather than auspiciousness.

A fictional medical example illustrates the objection.

Suppose a hidden condition makes someone both more inclined to smoke and more likely to develop a disease. In this deliberately artificial model, smoking itself has no effect on the disease. It provides one unit of enjoyment, while disease costs 100 utility units. Assume, conditional on the agent’s current information,

\[
P(\text{disease}\mid \text{smoke})=0.8,
\qquad
P(\text{disease}\mid \text{abstain})=0.2.
\]

Then EDT gives

\[
V(\text{smoke})=1-100(0.8)=-79,
\]

\[
V(\text{abstain})=-100(0.2)=-20.
\]

It recommends abstaining, despite the stipulated absence of any protective causal effect.

The causal objection is straightforward: refusing the enjoyment does not remove the condition. Why pay to obtain a more reassuring description of oneself?

The evidential response is that the conditional prospects really do differ, if the probabilities are correct. People who abstain are much less likely to have the disease. EDT treats this difference as decision-relevant even when abstention does not produce it. Whether that is rational is the substantive disagreement, not an arithmetic error.

### What screening-off can—and cannot—do

Additional information can remove the dependence. If the agent learns the hidden condition \(H\), and

\[
P(\text{disease}\mid A,H,K)
=
P(\text{disease}\mid H,K),
\]

then the disease term is identical across actions. EDT recommends smoking for its stipulated enjoyment.

But merely including \(H\) as a latent variable in the model does not accomplish this. When its value remains unknown,

\[
P(\text{disease}\mid A,K)
=
\sum_h
P(\text{disease}\mid h,K)P(h\mid A,K),
\]

assuming conditional independence given \(H\). The action may still change the weights assigned to different hidden conditions.

This distinction is essential: **knowing that a common cause exists is not the same as knowing its value**. A proposed screening-off defense must identify information the agent actually possesses and show that it removes the relevant dependence.

## 6. Actions, policies, and repeated decisions

The reference gives a rule for actions, but does not supply a complete theory of policy selection or sequential choice. A natural extension is available, provided it is identified as an additional modeling proposal.

A policy \(\pi\) maps possible information histories to actions:

\[
\pi:h\mapsto a.
\]

If selecting or installing a policy is itself a feasible choice, let \(\Pi\) denote the selected policy and \(U\) the utility of the complete resulting trajectory. The direct evidential extension is

\[
V_{K_0}(\pi)
=
\mathbb E[U\mid \Pi=\pi,K_0].
\]

This preserves EDT’s basic idea: evaluate each available object of choice by conditioning on its selection.

However, conditioning on a policy is not generally equivalent to conditioning on one later action. Several policies may produce the same action at one history while differing elsewhere. Moreover, selecting a policy may provide different evidence about a predictor or another agent than observing a particular action does.

Nor does policy-level EDT automatically establish dynamic consistency. At a later history \(h\), an agent who re-evaluates locally may maximize

\[
\mathbb E[U\mid A=a,h]
\]

rather than follow the policy preferred earlier. These conditionals need not yield the same recommendation. A complete sequential theory must specify whether commitments bind, whether policies can be revised, and which information is available at each choice point.

A reasonable operational convention is:

> Evaluate the decision object actually under the agent’s control, using its actual probabilistic relationships with the rest of the world.

Choosing a binding program is one decision problem; choosing a bodily movement after observing new information is another. Calling both “EDT” does not erase their differences.

Randomization likewise requires a model. If an unpredictable coin independently determines an action, that action may cease to be evidence about a pre-existing hidden state. But a predictor might anticipate the randomized policy, or correlated random sources might preserve dependence. “Randomize” is not a model-independent way to remove correlation.

Finally, policy evaluation does not license assuming that every similar agent adopts the same policy whenever I do. Such dependence must be justified. EDT conditions on the supplied probabilistic structure; it does not create correlations by declaration.

## 7. An operational procedure—and its limits

For an unfamiliar case, the following procedure makes the theory reasonably explicit.

**First, identify the choice point and feasible alternatives.** Is the agent choosing an immediate action, a commitment, or a policy?

**Second, specify current information \(K\).** Include known circumstances, observations, and relevant self-knowledge. Do not condition on unavailable information merely because it would simplify the analysis.

**Third, specify complete utilities.** Include costs, risks, other people’s welfare if valued, and consequences across repeated interactions. A locally attractive payoff may conceal a bad total outcome.

**Fourth, build a joint probability model.** EDT needs probabilities connecting actions to uncertain circumstances, not merely a list of possible consequences. Explain why the action would provide evidence about those circumstances.

**Fifth, condition separately on each alternative and compare expected utilities.** Sensitivity analysis is useful when dependencies are uncertain.

Two foundational difficulties remain.

### Zero-probability alternatives and deliberation

Ordinary conditioning does not determine

\[
P(O\mid A=a,K)
\]

when \(P(A=a\mid K)=0\). This can arise when an agent regards its own deterministic decision procedure as known.

One possible operational approach is to use a pre-choice model assigning positive probability to each considered action. Another is to evaluate limits of small perturbations. Neither is automatically canonical: different perturbations can produce different conditional distributions.

The reference does not settle this issue. An application involving probability-zero alternatives must therefore state an additional convention rather than presenting its answer as uniquely dictated by the basic formula.

Relatedly, the probabilities cannot simply be adjusted to make the preferred action look attractive. They must represent justified beliefs about the agent and environment. EDT is a decision criterion, not a complete theory of how a deliberating agent should model its own reasoning.

### Repeated decisions and theory uncertainty

The reference mentions disputed Dutch-book arguments involving Sleeping Beauty. The general lesson is methodological: repeated, correlated choices require a specification of total payoffs and the relationship among decisions at different awakenings. The one-line EDT formula alone does not resolve that controversy.

The article also reports an “evidentialist’s wager”: correlated agents may make EDT’s stakes unusually large, potentially giving it practical importance even under uncertainty about decision theory. This is a further argument, not a consequence of conditional expectation alone. It requires assumptions about correlations, utilities, and how competing normative theories should be compared.

## Sources

The principal source is Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” supplied revision 1373679688, CC BY-SA 4.0.

Relevant works cited there include Arif Ahmed, *Evidential Decision Theory* (2021); Allan Gibbard and William Harper, *Counterfactuals and Two Kinds of Expected Utility* (1976); David Lewis, “Causal Decision Theory” (1981); James Joyce, *The Foundations of Causal Decision Theory* (1999); and Vincent Conitzer, “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists” (2015). The policy extension and operational conventions above are proposals developed here, not additional claims attributed to those works.

## Conclusion

EDT maximizes expected utility conditional on the action performed. Its distinctive commitment is that justified evidential dependence can matter even without causal influence. This explains both its appeal in prediction and twin problems and its controversial recommendations in hidden-condition cases. Applying it well requires more than recognizing a correlation: one must specify the choice object, available information, utilities, and conditional probability model—and acknowledge where those specifications leave the answer unsettled.