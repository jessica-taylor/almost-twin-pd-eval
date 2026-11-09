# Evidential decision theory: choosing what you want to learn

Suppose you are about to make a choice, and your action would reveal something about the world. Perhaps a skilled predictor has anticipated it, or someone who reasons much as you do is making a similar decision elsewhere. Should you take those correlations into account, even when your action cannot cause the predictor’s earlier prediction or the other person’s choice?

**Evidential decision theory** (EDT) says yes. It evaluates an action by asking how desirable the world would be *conditional on your taking that action*. Its characteristic recommendation is to choose the act that would be the best news about how things stand.

This is not merely a rule for gathering information. The information considered is hypothetical: EDT asks what your action would indicate if you learned that you had taken it. The resulting assessment includes ordinary causal effects of the act, but it can also include correlations with events that the act does not cause.

The contrast is with **causal decision theory** (CDT), which evaluates an action by its consequences in a causal counterfactual: what would happen *if the agent were to perform it*, holding fixed the causally appropriate features of the situation. The two approaches often agree. Their disagreement appears when an action is evidence about a desirable state of affairs without being its cause.

The reference article presents EDT chiefly through this distinction and through Newcomb’s problem and a twin prisoner’s dilemma. The formal rule is simple; applying it requires care about what is known, which probabilities are being used, and what an “alternative action” means. Those complications are central rather than peripheral: different choices of model can yield different verdicts even among evidential decision theorists.

## 1. The basic rule

Let \(K\) represent the agent’s current evidence, and let \(A\) be one of the available actions. Suppose the relevant outcomes \(O_1,\ldots,O_n\) form an exhaustive, mutually exclusive partition, with utility \(u(O_j)\). EDT assigns \(A\) the value

\[
V_K(A)=\sum_{j=1}^n P(O_j\mid A,K)\,u(O_j).
\]

The recommendation is to choose an action maximizing \(V_K(A)\).

More generally, if utility depends explicitly on both the action and the state of the world \(S\), it is convenient to write

\[
V_K(A)=\sum_s P(s\mid A,K)\,u(A,s).
\]

This makes clear that an act can matter in two ways:

1. It can change the payoff obtained in a given state, represented by \(u(A,s)\).
2. It can be evidence about which state obtains, represented by \(P(s\mid A,K)\).

For example, buying insurance changes your payoff whether or not a loss occurs. But a decision to buy insurance might also be evidence that you possess private information about your risk. EDT includes both considerations if they are present in the agent’s probability model.

The probabilities are the agent’s credences at the decision point, conditional on all relevant available evidence. The theory does not require outcomes to be monetary: utilities can represent health, welfare, moral concerns, or any other consequences the decision-maker appropriately values. In the numerical examples below, money is treated as proportional to utility for simplicity.

The phrase “news value” can be misleading if taken too literally. EDT is not advising an agent to make herself happier by receiving a reassuring report. It uses the hypothetical report “I take \(A\)” as a way of assessing the distribution of outcomes associated with \(A\). Whether that is a sound basis for choice is precisely what critics dispute.

## 2. Conditioning is not intervention

The difference between EDT and CDT can be illustrated with a state \(S\) that affects both an action \(A\) and an outcome \(O\):

\[
S\longrightarrow A,\qquad S\longrightarrow O.
\]

Observing \(A\) supplies information about \(S\), and hence about \(O\). But setting \(A\) by an intervention need not change \(S\). In a simple causal model, EDT may therefore use

\[
P(O\mid A,K),
\]

whereas a causal calculation may use

\[
P(O\mid \operatorname{do}(A),K).
\]

The \(\operatorname{do}\) notation represents an intervention that sets the action while breaking the ordinary causal links into it. It is one useful way to formalize causal evaluation, though not every formulation of CDT is identical to this particular intervention rule.

Consider a fever and a thermometer. A high reading is evidence of fever, but heating the thermometer does not cure or cause the patient’s illness in the same way. Likewise, an action can be associated with an outcome because of a common cause, prediction, shared reasoning, or selection, without producing that outcome.

In ordinary cases, this distinction may not change the decision. If the action is randomized independently of relevant background states, and all its effects are adequately represented, conditioning on the action can coincide with intervening on it. EDT and CDT then agree. The interesting cases are those in which the agent’s contemplated action remains correlated with something outside its causal control.

## 3. Newcomb’s problem

A predictor has already placed either \$1 million or nothing in an opaque box \(B\). A transparent box \(A\) visibly contains \$1,000. The predictor filled \(B\) if it predicted that you would take only \(B\), and left \(B\) empty if it predicted that you would take both boxes. You now choose either:

- **One-box:** take only \(B\).
- **Two-box:** take both \(A\) and \(B\).

Suppose the following conditional probabilities describe your situation:

\[
P(B\text{ full}\mid \text{one-box})=0.99,
\qquad
P(B\text{ full}\mid \text{two-box})=0.01.
\]

Then EDT assigns

\[
V(\text{one-box})=0.99(\$1{,}000{,}000)=\$990{,}000
\]

and

\[
\begin{aligned}
V(\text{two-box})
&=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)\\
&=\$11{,}000.
\end{aligned}
\]

One-boxing is overwhelmingly better news: it indicates that the predictor probably expected one-boxing and filled \(B\).

A causal theorist typically argues differently. At the moment of choice, the contents of \(B\) are already fixed. Whatever those contents are, taking both boxes gives \$1,000 more than taking only \(B\). On that causal account, two-boxing is preferable.

The disagreement is not about whether the prediction is accurate, nor about whether the box was filled in the past. It is about how to evaluate an alternative act. EDT conditions on the act and allows the associated probability of the past prediction to change. CDT asks what the act would causally produce given the relevant fixed background.

There is a subtle probabilistic point. The statement “the predictor is 99% accurate” by itself does **not** entail both displayed conditional probabilities. An overall accuracy rate can conceal different error rates among one-boxers and two-boxers. The numerical EDT calculation requires the stronger conditional assumptions, or a joint probability model from which they follow. This distinction matters whenever a case supplies a global accuracy figure but asks for probabilities conditioned on particular choices.

The general one-boxing condition makes the structure clearer. Let

\[
p_1=P(B\text{ full}\mid\text{one-box}),\qquad
p_2=P(B\text{ full}\mid\text{two-box}).
\]

With a million-dollar opaque-box prize and a thousand-dollar transparent-box prize, EDT one-boxes exactly when

\[
1{,}000{,}000p_1>
1{,}000{,}000p_2+1{,}000,
\]

or

\[
p_1-p_2>0.001.
\]

The evidential advantage need not be perfect; it must be large enough to outweigh the guaranteed additional \$1,000.

## 4. Correlated agents: the twin prisoner’s dilemma

Now imagine that you and a psychological twin separately choose whether to cooperate or defect. Your individual payoffs are:

| Your choice | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$5 | \$0 |
| Defect | \$10 | \$1 |

For either fixed choice of the twin, defecting pays more. If your choice cannot causally influence your twin, that is the familiar dominance argument for defection.

But suppose your reasoning processes are so closely matched that your choices are perfectly correlated:

\[
P(\text{twin cooperates}\mid\text{you cooperate})=1,
\]
\[
P(\text{twin cooperates}\mid\text{you defect})=0.
\]

EDT gives cooperation value \$5 and defection value \$1. Cooperating is evidence that your twin cooperates; defecting is evidence that your twin defects. No communication or causal influence is required for that conditional relationship.

Perfect twins are an idealization. With imperfect correlation, set

\[
q_C=P(\text{twin cooperates}\mid C),\qquad
q_D=P(\text{twin cooperates}\mid D).
\]

Then

\[
V(C)=5q_C,\qquad
V(D)=10q_D+1(1-q_D)=1+9q_D.
\]

EDT cooperates when

\[
5q_C>1+9q_D.
\]

Thus similarity alone is not enough: what matters is the *conditional difference* in the other agent’s behavior, together with the payoff structure. If your action tells you almost nothing about the other’s, the evidential reason to cooperate disappears.

This example also shows why the relevant “outcome” should include other agents’ actions. Holding those actions fixed while evaluating your alternatives would remove the very dependence EDT is meant to consider.

## 5. An objection: smoking and bad news

The standard criticism is that EDT can confuse evidence of a bad outcome with a way of producing it. Consider a simplified example. A genetic condition \(G\) increases both the desire to smoke and the risk of disease, but smoking itself has no effect on disease. Suppose smoking gives a small pleasure, worth \(2\) utility units, while disease costs \(100\).

An agent’s model might assign

\[
P(G\mid \text{smoke})=0.8,\qquad
P(G\mid \text{abstain})=0.2,
\]

and suppose, for simplicity, that disease occurs exactly when \(G\) is present. Then

\[
V(\text{smoke})=2-100(0.8)=-78,
\]
\[
V(\text{abstain})=-100(0.2)=-20.
\]

EDT recommends abstaining. Yet if smoking has no causal effect on the genetic condition or disease, critics say that abstaining merely avoids the *bad news* associated with smoking. David Lewis called this kind of reasoning “managing the news”; James Joyce emphasized causal efficacy rather than auspiciousness.

An evidentialist can respond that the assessment depends on what the agent already knows. If the agent knows whether she has \(G\), or knows all relevant information about her tendency to smoke, then her eventual choice may supply no additional evidence about \(G\). For instance, conditional on \(K\) that screens off the association,

\[
P(G\mid \text{smoke},K)
=
P(G\mid \text{abstain},K),
\]

so EDT favors smoking for its small benefit.

This response does not settle every version of the objection. Whether the agent’s present evidence really screens off the correlation is a substantive assumption, not something to declare by fiat. Some information about one’s dispositions may remain uncertain. The case illustrates both the flexibility and the vulnerability of EDT: its verdict depends on the conditional dependencies in the model, and critics question whether those dependencies should always count in action evaluation.

## 6. How to model an unfamiliar problem

The reference article states the core conditional-utility rule but does not specify a complete procedure for building probability models. The following is an operational proposal consistent with that rule, rather than a uniquely mandated interpretation.

**First, specify the decision point and evidence.** Write down what the agent currently knows, including observations of predictors, past events, and private information. Use the same \(K\) for each alternative unless the alternatives themselves involve obtaining different information.

**Second, enumerate feasible acts and outcomes.** Outcomes should contain everything relevant to utility: the agent’s payoff, other people’s welfare if valued, future decisions, and costs of implementing an act. Avoid counting an informational correlation as an extra payoff on top of the outcome it predicts.

**Third, construct a joint model.** Specify, or estimate, a distribution over actions, background states, other agents’ choices, and outcomes, conditional on \(K\). Then calculate the relevant conditional probabilities. A causal diagram can help identify possible dependencies, but EDT does not simply replace the distribution with an intervention distribution.

**Fourth, compare conditional expected utilities.** For each act with positive conditional probability, compute \(V_K(A)\). Check whether the result is robust to plausible uncertainty about correlations and utilities.

**Finally, inspect the interpretation.** Ask why an act is evidence of a state. Is the link based on prediction, shared reasoning, private information, or a common cause? Would it remain after conditioning on what the agent actually knows? This step guards against importing a correlation from a population that does not apply to the individual decision.

A major difficulty lies in the third step. An agent may think her choice is up to her, yet the calculation asks for probabilities of her own possible actions. One practical interpretation is to use a coherent subjective model in which the action is a random variable reflecting the agent’s uncertainty about her reasoning, dispositions, or implementation. This is a modelling device for evidential dependence; it need not mean the agent regards herself as physically randomized.

The proposal has limits. If the model already assigns probability one to the action the agent is certain she will take, then the alternatives have probability zero, and ordinary conditional probability does not define their values. EDT’s basic formula alone does not resolve that case. Possible extensions include specifying conditional distributions directly, using carefully chosen limiting perturbations, or adopting richer counterfactual probability models. Different perturbations can produce different answers, so a zero-probability case requires further assumptions rather than an automatic appeal to Bayes’ rule.

## 7. Actions, policies, and randomization

Often the object of choice is not a single immediate act but a **policy**: a rule specifying what to do under different future observations. For a policy \(\pi\), an evidential analogue of the basic rule is

\[
V_K(\pi)=E[u\mid \pi,K],
\]

where “\(\pi\)” denotes adoption or implementation of that policy in a specified model. This can be useful when the policy itself is predictable, when other agents respond to it, or when it governs several correlated decisions.

But conditioning on adopting a policy is not automatically the same as intervening to install it. If people who adopt \(\pi\) tend to have different traits from people who adopt another policy, EDT may treat that association as evidence. A policy analysis must therefore say what event is being conditioned on and what the agent knows at the time.

A further issue is **dynamic consistency**. A policy that looks best before receiving information need not recommend, at every later information state, the act that maximizes that later state’s evidential value. Whether to follow the earlier policy or reconsider locally can depend on commitment possibilities and on which decision is being evaluated. The article’s basic formula does not by itself settle all such sequential-choice questions.

Randomization likewise needs an explicit model. Suppose a fair, genuinely independent coin determines your action. Conditional on the coin-selected action, correlations arising solely from your ordinary disposition to choose may disappear. On the other hand, if a predictor can forecast the coin or knows the policy producing it, relevant correlations may remain. “Choose randomly” is therefore not a universal escape from evidential dependence: the decision-maker must model the randomizer, who can predict it, and which variable—policy, coin result, or final act—is being evaluated.

## 8. Broader implications and open disputes

EDT’s appeal is strongest when an action is reliably linked to favorable outcomes in a way the decision-maker cannot causally reproduce by treating everything else as fixed. Newcomb’s problem makes that appeal vivid: one-boxers predictably receive more money under the stipulated conditional probabilities. The twin dilemma extends the idea to other agents whose decisions correlate with one’s own.

Its opponents insist that successful choice is about making the world better, not selecting an act that happens to signal that it was already better. The smoking example gives this criticism its force. There is no simple way to dismiss either side without taking a stand on what a decision-theoretic counterfactual should hold fixed.

The reference article also notes applications to Sleeping Beauty and Dutch-book arguments. There the details of awakening, memory loss, betting rules, and whether a policy or each individual bet is evaluated matter greatly. The article reports a dispute over whether EDT protects particular “halfer” credences from Dutch books; it does not establish a general resolution. Similarly, the suggestion that one should act as if EDT were true because correlated decisions can create especially large stakes is a further argument under moral or decision-theoretic uncertainty, not a consequence of the basic EDT equation.

## Conclusion

EDT evaluates an act by the expected utility of outcomes **conditional on that act**, given the agent’s evidence. Its distinctive feature is that correlations count even when they do not represent causal influence. This yields one-boxing in the stated Newcomb model and cooperation in the perfectly correlated twin dilemma, while exposing the theory to the charge of managing bad news in cases such as smoking.

To apply EDT responsibly, one must specify the decision point, utilities, and especially the joint distribution connecting actions to outcomes. The formula is concise; the philosophical and practical work lies in justifying the conditional model and deciding how to handle policies, sequential choices, and zero-probability alternatives.

### References

- Wikipedia contributors, [“Evidential decision theory,” revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), CC BY-SA 4.0.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, “Counterfactuals and Two Kinds of Expected Utility,” 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.