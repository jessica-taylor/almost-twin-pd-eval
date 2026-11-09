# Evidential Decision Theory: Choosing by What an Action Reveals

A decision can matter in two ways: through what it causes and through what it indicates. Buying insurance changes one’s financial exposure. Reaching for an umbrella may also reveal something about one’s assessment of the weather. Usually these roles coexist without difficulty. Sometimes, however, an action is evidence about an important outcome that it cannot cause.

**Evidential decision theory** (EDT) says to choose the action associated with the highest conditional expected utility. Its guiding question is:

> Given everything I already know, which action would I most want to learn that I take?

The supplied reference article calls this an action’s “news value.” The phrase is memorable but potentially misleading: EDT does not maximize pleasant feelings about receiving news. It maximizes expected utility, using the action itself as evidence.

This essay develops that rule, explains its treatment of dependencies and counterfactuals, and identifies modeling choices that the reference leaves open.

## 1. The basic mathematical rule

Let \(\mathcal A\) be a finite set of available actions. Write \(A\) for the random variable representing which action the agent takes, \(I\) for the agent’s current information, and \(O\) for the resulting outcome. Let \(u(O)\) measure the outcome’s utility.

For each action \(a\), EDT assigns the value

\[
V_E(a\mid I)
=
\mathbb E[u(O)\mid A=a,I].
\]

For a discrete outcome space, this becomes

\[
V_E(a\mid I)
=
\sum_o P(O=o\mid A=a,I)\,u(o).
\]

The recommendation is

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_E(a\mid I).
\]

This is the reference article’s central definition, with background information made explicit.

Outcomes should be described richly enough to include everything the agent values: money, health, other people’s welfare, effort, and any intrinsic value attached to the action. Utility need not equal monetary payoff. Using dollars directly assumes risk neutrality over the amounts involved.

The probabilities are the agent’s reasoned credences, not necessarily frequencies in a population. Observing that people who choose an action tend to prosper is insufficient if those people differ from this agent in already-known ways.

A useful alternative representation introduces states \(s\) that, together with an action, determine utility:

\[
V_E(a\mid I)
=
\sum_s P(s\mid A=a,I)\,u(a,s).
\]

The distinctive feature is that the state probabilities may differ between actions. Bayes’ rule makes this explicit:

\[
P(s\mid A=a,I)
=
\frac{P(A=a\mid s,I)P(s\mid I)}
{\sum_{s'}P(A=a\mid s',I)P(s'\mid I)}.
\]

If some hidden state makes an action more likely, contemplating that action can increase the evidential probability of that state.

The joint probability model is therefore crucial. EDT supplies an optimization rule; it does not supply all the probabilities needed to apply it.

## 2. Conditioning is not intervention

The reference contrasts EDT with causal decision theory (CDT). In its counterfactual notation, CDT evaluates

\[
V_C(a\mid I)
=
\sum_o P(a\mathrel{\Box\!\rightarrow}o\mid I)\,u(o),
\]

where the probability concerns what would happen were the action performed. This is not ordinary conditioning, nor is the counterfactual a material implication.

In a suitable causal model, a common representation is

\[
V_C(a\mid I)
=
\mathbb E[u(O)\mid \operatorname{do}(A=a),I].
\]

The intervention fixes the action while severing its ordinary incoming causal influences. Conditioning does not sever them.

Suppose a hidden characteristic \(L\) influences both action \(A\) and outcome \(O\):

\[
A\leftarrow L\rightarrow O.
\]

Learning \(A=a\) can reveal \(L\), thereby changing the probability of \(O\). Intervening on \(A\) need not change \(L\) at all. EDT retains this evidential connection; CDT does not count it as an effect of the action.

This does not make EDT a theory of backward causation. An action can be evidence about yesterday’s prediction without changing yesterday.

Nor does EDT ignore causation. Causal consequences normally affect conditional outcomes too. The disagreement concerns additional, noncausal dependencies.

The theories agree whenever the relevant conditional and intervention distributions agree. For example, if action selection is independent of all payoff-relevant background factors, given \(I\), then conditioning on the action does not selectively favor different background states. Under an appropriate causal model, EDT then reduces to the familiar calculation of consequences.

## 3. Newcomb’s problem: evidence about an already-filled box

In Newcomb’s problem, a transparent box contains \(k=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing.

A predictor has already filled the opaque box:

- if it predicted that the agent would take only the opaque box, it put \(M\) inside;
- if it predicted that the agent would take both boxes, it left the opaque box empty.

Let \(B\) denote taking only the opaque box and \(T\) taking both. Define

\[
q=P(\text{opaque box full}\mid B,I),
\qquad
r=P(\text{opaque box full}\mid T,I).
\]

For monetary utility,

\[
V_E(B)=qM,
\qquad
V_E(T)=rM+k.
\]

Thus EDT recommends one-boxing exactly when

\[
(q-r)M>k.
\]

The reference uses \(q=0.99\) and \(r=0.01\), giving

\[
V_E(B)=\$990{,}000,
\qquad
V_E(T)=\$11{,}000.
\]

One-boxing wins decisively.

There is a technical qualification: saying merely that a predictor is “99% accurate overall” does not uniquely determine these two conditional probabilities. The article’s calculation assumes the relevant action-conditional reliabilities. An unfamiliar version of the problem must specify enough information to recover \(q\) and \(r\).

CDT instead holds the already-set box contents fixed under interventions on the present action. Whatever those contents are, taking both boxes adds \(\$1{,}000\).

EDT does not dispute that arithmetic. It disputes the decision procedure that gives the same probability distribution over box contents to both actions. Learning that one takes only the opaque box is, by hypothesis, strong evidence that it contains the million.

If the contents become known before choosing, this evidential advantage disappears. With the same known contents under both action-conditionals, EDT also recommends taking the extra thousand dollars.

## 4. Psychological twins and correlated choices

The reference’s twin prisoner’s dilemma illustrates the same structure without a predictor.

Two isolated psychological twins choose between cooperation \(C\) and defection \(D\). Each cares only about her own payoff:

\[
\begin{array}{c|cc}
 & \text{Twin }C & \text{Twin }D\\
\hline
C & 5 & 0\\
D & 10 & 1
\end{array}
\]

Defection pays more against either fixed action of the other player. But EDT does not necessarily assign the same probabilities to the twin’s action conditional on cooperating and conditional on defecting.

Write

\[
p_C=P(\text{twin cooperates}\mid C,I),
\qquad
p_D=P(\text{twin cooperates}\mid D,I).
\]

Then

\[
V_E(C)=5p_C,
\qquad
V_E(D)=10p_D+(1-p_D)=1+9p_D.
\]

Cooperation is recommended when

\[
5p_C>1+9p_D.
\]

For perfectly matching twins, \(p_C=1\) and \(p_D=0\), so cooperation yields conditional expected utility \(5\), compared with \(1\) for defection.

For an imperfect symmetric relationship, suppose the twins match with conditional probability \(r\):

\[
p_C=r,\qquad p_D=1-r.
\]

Cooperation wins precisely when

\[
5r>10-9r
\quad\Longleftrightarrow\quad
r>\frac57.
\]

This extension, not stated in the source, shows that perfect identity is unnecessary. Sufficiently strong conditional dependence can support cooperation.

Nothing here gives one player causal control over the other. Nor does EDT automatically correlate all agents who resemble one another. The relevant probabilities require justification from shared psychology, information, reasoning, or some other reliable connection.

## 5. The central objection: managing the news

The same mechanism can produce much less attractive recommendations.

Consider a fictional medical example. A hidden lesion increases both the desire to use a harmless stimulant and the probability of illness. Taking the stimulant does not cause illness. It provides utility \(+1\), while illness costs \(100\).

Suppose, conditional on the agent’s current information,

\[
P(\text{illness}\mid \text{take})=0.8,
\qquad
P(\text{illness}\mid \text{abstain})=0.2.
\]

EDT calculates

\[
V_E(\text{take})=1-100(0.8)=-79,
\]

\[
V_E(\text{abstain})=-100(0.2)=-20.
\]

It recommends abstention.

A causal assessment says that the stimulant leaves the lesion and illness risk unchanged while providing a benefit. Taking it is causally preferable by one utility unit.

This captures the criticism quoted in the reference: David Lewis describes EDT as “managing the news,” while James Joyce argues that rational action should be governed by causal efficacy rather than auspiciousness. Avoiding a symptom does not cure the condition it indicates.

An evidentialist can reply that the conditional prospects really are worse upon taking the stimulant. But that restates, rather than resolves, the disagreement: should an agent select the action associated with better prospects, or the intervention that improves outcomes?

### Why background information matters

Suppose the agent already knows a disposition \(T\), and \(T\) screens off the action–illness association:

\[
\text{illness}\;\perp\!\!\!\perp\;A\mid I,T.
\]

Then taking the stimulant supplies no further evidence about illness. EDT recommends taking it for its benefit.

This illustrates an important operational discipline: condition on everything already known. Do not let an action reveal information that is already included in the background.

However, one cannot simply add the unknown lesion itself to the conditioning information. That would replace uncertainty with knowledge the agent does not possess. Whether an observed desire or other introspective evidence genuinely screens off the association is a substantive modeling question.

Likewise, EDT does not generally recommend refusing medical information. Taking an independently offered test need not indicate illness, even though a positive result would. The evidential significance of choosing a test and that of its result are different.

## 6. Actions, policies, and repeated decisions

The reference gives an act-level rule, but it does not provide a complete account of sequential choice. This matters when an agent can commit to a policy, face repeated situations, or encounter other agents using related reasoning.

A policy is a rule assigning actions to possible information histories:

\[
\pi:h\mapsto a.
\]

A natural extension of EDT is to treat policy adoption itself as the object of conditioning. Let \(\Pi\) represent the policy adopted. Then evaluate

\[
V_E(\pi\mid I)
=
\mathbb E[u(O)\mid \Pi=\pi,I].
\]

For a policy followed by one later observation \(H\),

\[
V_E(\pi\mid I)
=
\sum_h
P(H=h\mid \Pi=\pi,I)
\mathbb E[u(O)\mid \Pi=\pi,H=h,I].
\]

The action subsequently taken is \(\pi(h)\).

This is a proposed operational extension, not a uniquely specified prescription in the supplied article. It requires a joint model of policy adoption, later observations, and outcomes.

Three distinctions are essential.

**Policy evidence need not equal action evidence.** Learning that someone adopted a conditional plan can reveal different information from learning which action they eventually performed. An action may depend heavily on a later observation.

**Correlation is not automatic synchronization.** Conditioning on my adoption of \(\pi\) changes probabilities concerning other agents only to the extent supported by the model. It does not mean replacing every similar agent’s policy with mine.

**Commitment differs from reconsideration.** At a later history \(h\), act-level EDT evaluates

\[
\mathbb E[u(O)\mid A=a,I,h].
\]

That need not reproduce the action prescribed by an earlier policy evaluation. Equivalence between choosing a policy now and optimizing separately later requires assumptions about commitment, information, and the evidential relationships among decisions.

Randomization also needs explicit modeling. If a genuinely independent random device selects an action, its result may carry less information about hidden dispositions than a deliberate selection would. The value of a randomized policy must therefore be calculated from the policy-conditioned model, not automatically as an average of previously calculated action values.

## 7. Applying EDT when the model is incomplete

Most practical difficulty lies in specifying the conditional probabilities rather than maximizing the resulting expression. A disciplined application proceeds as follows:

1. **Identify the decision object.** Is the agent choosing an immediate act, a commitment, or a policy?
2. **Fix the information set.** Include observations, remembered commitments, and relevant self-knowledge.
3. **Specify outcomes and utility.** Include costs and benefits to everyone whose welfare matters to the agent.
4. **Model dependencies.** Identify why the action might provide information about outcomes, including shared causes, predictors, and correlated reasoning.
5. **Calculate action-conditional expected utilities.** Preserve warranted dependencies, but do not invent them.
6. **Test sensitivity.** Determine which probabilities or utilities could change the recommendation.

The threshold calculations above are especially useful: one need not know every probability exactly if the recommendation is stable across a defensible range.

### Zero-probability actions

Ordinary conditioning requires

\[
P(A=a\mid I)>0.
\]

But a deterministic agent might assign probability one to its eventual choice, leaving alternatives with probability zero. The reference does not resolve this problem.

One operational approach is to use a deliberative model that leaves each live option with positive probability. Another is to introduce small probabilities of error and examine

\[
V_E(a)
=
\lim_{\varepsilon\to0}
\mathbb E_\varepsilon[u(O)\mid A=a,I].
\]

These are additional modeling proposals. Different error models can yield different limiting conditionals. An accidental action caused by an unrelated motor failure may reveal much less about psychology than the same action reached through deliberation.

Thus zero-probability alternatives require an explicit account of what “learning that I take this action” means. EDT’s compact formula does not uniquely provide one.

### Self-location and repeated opportunities

The reference also reports disputed applications to Sleeping Beauty and Dutch-book arguments. Such cases require more than the EDT slogan.

One must specify whether probabilities concern whole experimental runs or particular awakenings, whether indistinguishable decisions are linked, and whether utility counts one transaction or the total payoff across the experiment. The source reports both defenses of evidentialist approaches and Conitzer’s criticism of them. It therefore does not establish that EDT uniquely settles the underlying probability dispute or automatically prevents every Dutch book.

## Source and further reading

The central definition, standard examples, and reported criticisms are drawn from Wikipedia contributors, [“Evidential decision theory,” supplied revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), licensed CC BY-SA 4.0. The source cites Allan Gibbard and William Harper’s *Counterfactuals and Two Kinds of Expected Utility* (1976) for the formal distinction, and Arif Ahmed’s *Evidential Decision Theory* (2021) for a sustained treatment. The generalized thresholds, policy formulation, and operational proposals here are additional exposition rather than claims uniquely settled by that article.

## Conclusion

EDT evaluates an action by the expected utility conditional on performing it. It therefore retains informative dependencies that intervention-based reasoning can exclude, explaining its attraction in Newcomb’s problem and correlated cooperation—and its vulnerability to the charge of merely managing good and bad news.

Applying it well requires more than recognizing a correlation. One must specify the agent’s information, the decision object, and a justified probability model. With those ingredients explicit, EDT becomes a precise, usable procedure, while the philosophical dispute remains visible: should choice track what an action brings about, or the prospects that taking it reveals?