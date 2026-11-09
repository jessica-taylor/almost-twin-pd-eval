# Evidential decision theory: choosing what you want to learn

Suppose you must choose an action, and your choice is correlated with facts you cannot directly control. It might reveal something about an earlier prediction, another person’s reasoning, or an unobserved feature of your own psychology. Should those correlations affect your decision?

Evidential decision theory, or **EDT**, says yes. It recommends choosing the action that would be the best *news*: the action whose occurrence would make desirable outcomes most probable, taking everything you currently know into account.

This is different from saying that merely learning about an action changes the world. The idea is instead that your action is itself evidence. If taking an umbrella is evidence of rain, then observing someone take an umbrella may raise your expectation of rain even though taking the umbrella does not cause it. EDT applies this evidential logic to the agent’s own alternatives.

That proposal is intuitive in some cases and controversial in others. It explains why an evidential decision-maker may cooperate with a sufficiently similar opponent or take only one box in Newcomb’s problem. But it also invites the criticism that an agent can improve the *news* associated with an outcome without improving the outcome itself. Understanding EDT requires seeing both sides: its formal rule is simple, while its application depends heavily on the probability model and on what is included in the agent’s evidence.

## 1. The basic rule

Let \(K\) represent everything the agent knows or takes as given at the decision point. Let \(A\) be an available action, and let \(O_1,O_2,\ldots\) be mutually exclusive, exhaustive outcomes. Write \(u(O_j)\) for the utility of outcome \(O_j\). EDT assigns \(A\) the value

\[
V_{\mathrm E}(A\mid K)
=
\sum_j P(O_j\mid A,K)\,u(O_j).
\]

The recommendation is to choose an action with maximal evidential value:

\[
A^*\in\operatorname*{arg\,max}_{A}V_{\mathrm E}(A\mid K).
\]

The source article presents this as maximizing the expected desirability of outcomes conditional on the action. Equivalently, when utility can be represented by a random variable \(U\),

\[
V_{\mathrm E}(A\mid K)=\mathbb E[U\mid A,K].
\]

The conditioning is the distinctive feature. The agent asks: *Given my present information, what would the world probably be like if I learned that I took this action?* That includes effects the action produces, but also facts that the action merely indicates.

Some qualifications are important.

First, outcomes must describe everything relevant to utility. If an action has a cost, the outcome description or utility function must include it. Money can stand in for utility in examples only if the agent values the amounts approximately linearly and has no other relevant preferences.

Second, \(P(O\mid A,K)\) is not generally the same as \(P(O\mid K)\). Conditioning on an action can change beliefs about other events, including events that occurred before the action.

Third, the formula is not an instruction to believe that one has already acted. The agent compares several hypothetical pieces of news using a probability model specified from the current decision point. Exactly how that model should accommodate a self-aware deliberator is a philosophical issue, not something settled merely by writing the equation.

## 2. Evidence and causal counterfactuals

The reference contrasts EDT with **causal decision theory** (CDT). CDT evaluates an action by the outcomes it would causally produce, rather than by everything correlated with its occurrence. In a suitable causal model, a common representation is

\[
V_{\mathrm C}(A\mid K)
=
\sum_j P(O_j\mid \operatorname{do}(A),K)\,u(O_j).
\]

Here \(\operatorname{do}(A)\) represents an intervention that sets the action to \(A\), while leaving the rest of the causal model to evolve accordingly. The reference uses a more general counterfactual notation rather than the intervention operator; the latter is helpful when an explicit causal model is available, but it is not the only formulation of CDT.

Conditioning and intervention can differ. Suppose an unobserved trait \(T\) influences both an earlier prediction \(R\) and the agent’s later action \(A\):

\[
R \leftarrow T \rightarrow A.
\]

Observing \(A\) supplies evidence about \(T\), hence about \(R\). But intervening to set \(A\), in this model, does not change \(T\) or the already-made prediction. Thus \(P(R\mid A,K)\) can differ from \(P(R\mid\operatorname{do}(A),K)\).

When all relevant dependencies between action and outcome are causal effects of the action, or when the appropriate evidential and causal probabilities otherwise coincide, EDT and CDT agree. Their disagreement is concentrated in cases where an action is informative about something it does not cause.

This distinction also clarifies EDT’s treatment of counterfactuals. EDT compares alternatives, but its basic comparison uses **conditional probabilities**, not automatically causal counterfactual probabilities. To say “if I take \(A\)” in an EDT calculation is, at the formal level, to condition on \(A\); it need not mean “if I intervened to make \(A\) happen while holding the past fixed.”

## 3. Newcomb’s problem

Newcomb’s problem makes the difference vivid. A predictor has already placed either \$1 million or nothing in an opaque box \(B\). A transparent box \(A\) contains \$1,000. If the predictor predicted that you would take only \(B\), it filled \(B\); if it predicted that you would take both boxes, it left \(B\) empty.

Suppose your conditional probabilities are

\[
P(B\text{ full}\mid \text{one-box},K)=0.99,
\qquad
P(B\text{ full}\mid \text{two-box},K)=0.01.
\]

Assuming linear utility for money, EDT gives

\[
\begin{aligned}
V_{\mathrm E}(\text{one-box})
&=0.99(\$1{,}000{,}000)=\$990{,}000,\\
V_{\mathrm E}(\text{two-box})
&=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
=\$11{,}000.
\end{aligned}
\]

One-boxing is much better news about the contents of \(B\). EDT therefore recommends it.

For the standard causal analysis, the predictor’s choice and the box contents are already fixed. Taking the transparent box cannot empty the opaque one. Holding the earlier contents fixed, taking both boxes adds \$1,000, so CDT recommends two-boxing.

The 99% figures deserve care. An **overall** 99% prediction accuracy does not, by itself, imply both conditional probabilities above. If one action is very rare, the predictor’s errors could be concentrated among people who take that action. The calculation requires the stated conditional reliability, or further assumptions that entail it.

More generally, write

\[
p_1=P(B\text{ full}\mid \text{one-box},K),\qquad
p_2=P(B\text{ full}\mid \text{two-box},K).
\]

Then EDT one-boxes exactly when

\[
\$1{,}000{,}000p_1>
\$1{,}000{,}000p_2+\$1{,}000,
\]

or

\[
p_1-p_2>0.001.
\]

The important quantity is therefore not prediction accuracy stated in isolation, but the difference between the probabilities of a full box conditional on the competing actions.

## 4. A correlated opponent

The same reasoning applies when the correlated event is another agent’s choice. Suppose Aomame and her psychological twin independently face a prisoner’s dilemma. Aomame’s payoffs are:

| Aomame | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$5 | \$0 |
| Defect | \$10 | \$1 |

If the twin’s choice is perfectly correlated with hers, then

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1
\]

and

\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]

Consequently,

\[
V_{\mathrm E}(C)=\$5,\qquad V_{\mathrm E}(D)=\$1.
\]

EDT recommends cooperation, even though defection pays more against either *fixed* choice of the twin. The recommendation does not require Aomame’s choice to cause the twin’s choice. It requires the relevant conditional dependence.

Perfect correlation is stronger than necessary. Let

\[
q_C=P(\text{twin cooperates}\mid C,K),\qquad
q_D=P(\text{twin cooperates}\mid D,K).
\]

Then

\[
V_{\mathrm E}(C)=5q_C,\qquad
V_{\mathrm E}(D)=10q_D+1(1-q_D)=1+9q_D.
\]

Cooperation is recommended when \(5q_C>1+9q_D\). If the players are merely somewhat similar, this inequality may or may not hold. “We reason alike” is not a substitute for a probability model: similarity matters only insofar as it supports the necessary conditional probabilities.

## 5. The news-management objection

Critics argue that EDT can confuse an indication of a good outcome with a means of producing one. David Lewis called it a policy of “managing the news”; James Joyce emphasized causal efficacy rather than auspiciousness.

Consider an illustrative medical case. A disease \(D\) both causes an appetite for a certain food and raises the chance of illness. Suppose eating the food is mildly enjoyable and has no causal effect on health. Before observing the choice, let

\[
P(D\mid \text{eat})=0.8,\qquad
P(D\mid \text{abstain})=0.2.
\]

If illness costs 10 utility units, the disease certainly causes illness, and eating gives 1 unit of enjoyment, the evidential values are

\[
V_{\mathrm E}(\text{eat})=1-10(0.8)=-7,
\qquad
V_{\mathrm E}(\text{abstain})=-10(0.2)=-2.
\]

EDT, with these probabilities, says abstain. Yet if the disease is already present or absent and eating cannot affect it, a causal analysis says that eating adds enjoyment without altering the health outcome.

The objection is not that EDT literally thinks abstaining cures the disease. It is that abstention is good *news* about whether the disease is present, and EDT lets that news outweigh the enjoyment.

A possible evidentialist response is to ask what the agent already knows about their appetite and other symptoms. If that information screens off the correlation between choice and disease, so that

\[
P(D\mid \text{eat},K)=P(D\mid \text{abstain},K),
\]

the disease term cancels and EDT recommends eating. But screening off is a substantive empirical and informational assumption, not a universal solution. The agent may lack access to the relevant internal state, or their eventual choice may reveal additional information even after everything currently known is included. Thus the case exposes a genuine dispute about whether all decision-relevant evidential dependencies should count.

## 6. Actions, policies, and information

A decision is not always a single physical act. It can be a **policy**: a rule specifying what to do after different observations. For example, a medical policy might say “treat if the test is positive, otherwise wait.” If \(\pi\) is such a policy, an evidential evaluation can take the form

\[
V_{\mathrm E}(\pi\mid K)=\mathbb E[U\mid \pi,K].
\]

This treats adopting or following \(\pi\) as the evidence being evaluated. The possible outcomes must include the observations, subsequent actions, costs, and results generated under that policy. The model must also say what the event “\(\pi\)” means: choosing a plan now, irrevocably committing to it, or actually following it can be different events with different correlations.

The source gives the central action rule but does not settle every question about policy choice and sequential decisions. A reasonable operational proposal is:

1. **Fix the decision point and information \(K\).** Include observations the agent actually has, but do not insert the hypothetical action into \(K\) before comparing alternatives.
2. **List the feasible alternatives.** These may be immediate actions or explicitly described policies.
3. **Build one coherent joint probability model** over the alternatives, relevant past and future events, observations, and outcomes.
4. **Condition that model on each alternative**, compute expected utility, and compare values.
5. **Reassess at later information states**, while keeping track of any commitments or policy consequences already incurred.

This procedure is a proposed practical interpretation, not a separate theorem supplied by the source. Its main virtue is that it forces hidden assumptions into the open. In Newcomb’s problem, for example, it asks how the predictor, agent, and box contents are jointly distributed. In the twin dilemma, it asks how strongly the twin’s decision remains correlated with yours given what you know.

Sequential cases require special care. A policy that looks best before receiving information need not prescribe the action that looks best after receiving it. Also, choosing a policy now may itself be evidence about other agents or past predictions, whereas conditioning later on a particular act can convey different evidence. If an agent can commit, the commitment and its causal effects belong in the outcome model. If they cannot, a plan should not be evaluated as though it were guaranteed to be followed. EDT’s basic formula alone does not resolve every possible conflict between ex ante policy evaluation and later choice.

## 7. Randomization and zero-probability alternatives

A further problem arises when an alternative has probability zero under the agent’s model. Ordinary conditional probability

\[
P(O\mid A,K)=\frac{P(O\cap A\mid K)}{P(A\mid K)}
\]

is undefined when \(P(A\mid K)=0\). This can happen if the model treats the agent as perfectly predictable, or if the agent is certain of what they will choose.

One possible operational response is to use a richer model in which each live alternative has positive probability, perhaps because of uncertainty about deliberation. Another is to specify a principled limiting conditional or other extension for zero-probability events. Neither is automatic: different ways of approaching a zero-probability event can yield different answers. Adding tiny probabilities without explaining the model can therefore conceal rather than solve the problem.

Randomization also needs explicit treatment. If the agent uses a coin or random device, “choose a 50–50 randomizing policy” and “the device produces action \(A\)” are distinct events. An independent coin outcome may carry little evidence about a predictor or twin, while adopting the policy may itself be predictable or correlated with their behavior. EDT should condition on the actual alternative under evaluation, not assume that every resulting action has the same evidential significance as a deliberately selected act.

## 8. Broader implications and limits

The reference notes applications to the Sleeping Beauty problem and debates about Dutch books: collections of bets that guarantee a loss under specified rules. Whether EDT protects a particular account of Beauty’s credences depends on the betting setup and on how repeated awakenings and decisions are counted. The article reports a dispute, including Conitzer’s argument that some “halfer” evidentialists remain vulnerable. EDT alone should not be treated as settling that broader controversy.

The reference also mentions an argument sometimes called the evidentialist’s wager: even someone uncertain about EDT might give it weight because correlated decisions can have unusually large stakes. That is a claim in **decision-making under normative uncertainty**, not a consequence of the ordinary EDT formula. Its force depends on how competing theories are compared and on whether their scales of value can be meaningfully combined.

These examples underline the theory’s central lesson. Dependencies are not optional decorations in a decision problem. The answer changes with what an action indicates, what information is already available, whether other agents are correlated with the decision-maker, and which alternative—an act, a commitment, or a policy—is being evaluated.

## Conclusion

EDT chooses the action with the highest expected utility **conditional on taking it**. This gives it distinctive recommendations in cases such as Newcomb’s problem and the twin prisoner’s dilemma, where an action is evidence about events it does not causally control. Its appeal is that rational choices should take relevant information seriously; its central vulnerability is that good news need not be something an action brings about.

To apply EDT responsibly, specify the agent’s information, alternatives, utilities, and joint probability model. Then condition on each alternative—and inspect the resulting dependencies rather than assuming that correlation, causation, and counterfactual change are the same thing.

**References**

- Wikipedia contributors, [“Evidential decision theory,” revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), CC BY-SA 4.0.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.