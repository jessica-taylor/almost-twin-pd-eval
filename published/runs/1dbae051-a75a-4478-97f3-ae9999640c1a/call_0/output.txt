# Causal decision theory: choosing what makes a difference

A decision often provides information as well as producing consequences. Ordering a salad may be evidence that one is health-conscious; pressing a switch may turn on a light. These are different relationships. The first tells us something about the kind of person who made the choice; the second describes a way the choice changes the world.

**Causal decision theory** (CDT) recommends choosing an available act whose *expected causal consequences* are best. It contrasts with **evidential decision theory** (EDT), which evaluates an act by asking how desirable the world would be conditional on learning that the act was taken. The distinction matters most when an action is correlated with a desirable or undesirable state of affairs that it does not itself cause.

The basic idea is simple, but applying it requires a model of counterfactuals: what would happen if the agent took each alternative? The supplied reference presents CDT through probabilities of such counterfactuals, and also notes an important limitation: the theory’s slogan does not itself supply a general algorithm for computing them. A structural causal model is one useful way to make the calculation operational, but it is an additional modeling choice, not a definition settled by the slogan alone.

## 1. From consequences to expected utility

Suppose an agent can choose one action \(a\) from a set \(\mathcal A\). Outcomes are denoted by \(o\), and \(u(o)\) measures their desirability to the agent. If the consequences of an action are uncertain, the decision requires an average weighted by probabilities, not merely an identification of its best or worst possible result.

Let \(O_a\) denote the outcome that *would occur if* the agent took \(a\). A standard causal expected-utility rule is

\[
V_C(a)=\mathbb E[u(O_a)\mid E],
\qquad
a^*\in\arg\max_{a\in\mathcal A}V_C(a),
\]

where \(E\) is the evidence available at the time of choice. For discrete outcomes this becomes

\[
V_C(a)=\sum_o
P(O_a=o\mid E)\,u(o).
\]

The probability here concerns a counterfactual outcome. It is not automatically the probability of \(o\) *among cases in which the agent in fact takes \(a\)*.

For example, suppose eating an apple produces utility \(10\) if it is good and \(-6\) if it is bad. If the probability that it is good is \(0.7\), then, assuming eating it does not change its prior quality,

\[
V_C(\text{eat apple})=0.7(10)+0.3(-6)=5.2.
\]

An orange with a certain utility of \(4\) is therefore worse by this measure. The calculation requires both beliefs about the apple and utilities for the resulting experiences. “Expected causal consequences” does not mean certain consequences, nor does it mean maximizing the expected amount of money unless money is an adequate stand-in for utility.

The reference presents Gibbard and Harper’s formulation as

\[
U(A)=\sum_j P(A\mathbin{\to}O_j)\,D(O_j),
\]

where \(A\mathbin{\to}O_j\) is a counterfactual conditional and \(D(O_j)\) is the outcome’s desirability. Informally, \(P(A\mathbin{\to}O_j)\) is the probability that, were \(A\) done, \(O_j\) would result. This should not be read as saying that \(A\) *logically or necessarily* implies \(O_j\): the relevant implication is counterfactual and depends on how the world would respond to the action.

The potential-outcome notation above is a convenient operational interpretation. It assumes that the relevant counterfactuals are well defined and that the outcomes form an exhaustive, mutually exclusive partition. Those assumptions can be difficult to satisfy: “take the medicine,” for instance, may leave important aspects of dose and timing unspecified.

## 2. Why not just condition on the action?

EDT uses a different valuation:

\[
V_E(a)=\mathbb E[u(O)\mid A=a,E].
\]

It asks what outcomes are likely on receiving the news that the act occurred. When an act is evidence of some independently important fact, this conditional distribution can differ from the distribution of \(O_a\).

Imagine that a hidden trait \(T\) affects both a person’s choice and their risk of illness:

\[
T\longrightarrow A,\qquad T\longrightarrow O.
\]

Suppose, for illustration, that people with \(T=1\) are much more likely to drink coffee and also much more likely to become ill, but coffee itself has no effect on illness. Learning that a person drinks coffee raises the probability that they have the trait and hence that they will become ill. Yet making that person drink coffee does not change the trait. On these assumptions, \(P(O\mid A=\text{coffee})\) and \(P(O_{\text{coffee}})\) differ.

The supplied reference’s King David example has this structure. David’s unknown charisma influences both whether he is inclined to act unjustly and whether a revolt would succeed. By hypothesis, the unjust act of summoning Bathsheba does not itself cause a successful revolt. Abstaining can therefore be *evidence* of charisma, while not making David charismatic. If David values the encounter and there are no sufficiently important additional costs, CDT recommends summoning her; EDT may recommend abstention because it is good news about his prospects.

Those qualifications matter. If injustice itself has a utility cost, if summoning her alienates supporters, or if David’s deliberations provide new evidence about his personality, the result can change. CDT does not say to disregard morality or information. It says to represent them in the utility function and the causal model rather than infer a causal effect merely from correlation.

When do the two theories agree? One sufficient condition, in a potential-outcome formulation, is **consistency** together with conditional independence:

\[
O_a\perp A\mid E,
\qquad
O=O_a\ \text{when }A=a.
\]

Then, for an action with positive probability,

\[
P(O=o\mid A=a,E)=P(O_a=o\mid E).
\]

Randomized assignment, appropriately modeled, is a familiar situation in which this kind of equality can hold. The reference reports a related sufficient condition from Gibbard and Harper, involving independence between an action and its counterfactual conditional, under further axioms.

The equality is not a general law. Lewis’s work on probabilities of conditionals gives a broader warning against identifying the probability of a conditional with an ordinary conditional probability in unrestricted settings. A counterfactual question and a news-of-the-action question are conceptually distinct even when a particular model makes their numerical answers coincide.

## 3. Computing causal values with a model

One practical way to implement CDT is with a **structural causal model**. This is an operational proposal for applying the reference’s idea, not a claim that every version of CDT must use the same formalism.

Suppose variables are generated by equations such as

\[
A=f_A(T,U_A),\qquad
O=f_O(A,T,U_O),
\]

where \(T\) is a background variable and the \(U\)’s represent other influences. The equation for \(A\) describes how the agent would ordinarily choose. To evaluate a hypothetical intervention \(do(A=a)\), replace that equation with \(A=a\), retain the other relevant equations, and propagate the change forward. Then

\[
V_C(a)
=\sum_o u(o)\,P(o\mid do(A=a),E).
\]

The intervention breaks the ordinary incoming causal links to \(A\), but it does **not** erase the agent’s evidence \(E\) or make all other variables independent. Background factors retain their evidence-conditioned distribution. Variables downstream of the action are allowed to change according to the model.

This is not the instruction to “hold everything else fixed.” If turning a thermostat down causes the room to cool, the room temperature should change in that counterfactual. What is held fixed, in the simplest model, are the background circumstances and mechanisms that the contemplated intervention does not alter. If an action changes another agent’s response, that response is a descendant and must be recomputed too.

Evidence can also concern variables that are usually downstream. If the agent has observed a symptom before a medical decision, that observation may be evidence about the underlying disease. A counterfactual calculation should first use the evidence to infer plausible background states and then ask what each action would do in those states. It should not pretend the observed symptom was never seen. The causal timing and content of evidence therefore need to be specified carefully.

Causal models require substantive assumptions. Observational data alone may fail to identify \(P(o\mid do(a),E)\): two models can fit the same correlations but disagree about interventions. An agent may instead average over models \(M\),

\[
V_C(a)=\sum_m P(M=m\mid E)\,
\mathbb E_m[u(O_a)\mid E],
\]

provided the models give well-defined counterfactuals. This represents uncertainty about causal mechanisms rather than resolving it by fiat.

## 4. Newcomb’s problem: a fixed past and correlated choices

Newcomb’s problem makes the distinction vivid. There is a transparent box containing \$1,000 and an opaque box containing either \$1,000,000 or nothing. A reliable predictor has already filled the opaque box: it put in the million if it predicted that the player would take only the opaque box, and otherwise left it empty.

Assume money is linear in utility over these amounts, and let \(p\) be the player’s current probability that the opaque box is full. If the choice cannot causally alter the already completed prediction or box filling, then

\[
V_C(\text{one box})=1{,}000{,}000p,
\]
\[
V_C(\text{two boxes})=1{,}000{,}000p+1{,}000.
\]

Thus two-boxing causally dominates: in either fixed state of the opaque box, it yields \$1,000 more. This is the recommendation reported in the reference.

EDT reasons differently. To illustrate its calculation, suppose the predictor is 99% accurate *conditional on either actual choice*. Then

\[
V_E(\text{one box})=0.99(1{,}000{,}000)=990{,}000,
\]
\[
V_E(\text{two boxes})=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

On those illustrative probabilities EDT one-boxes. Overall accuracy of 99%, by itself, does not guarantee these two conditional accuracies; the example needs that extra assumption.

The disagreement is not about whether prediction and choice are correlated. Both theories can recognize the correlation. They disagree about whether the correlation should count in evaluating the present act when the prediction is already causally settled. Nor does the CDT calculation show that two-boxers generally receive more than one-boxers: with a highly accurate predictor, the opposite may be true. The two-boxer’s claim is that, at the specified decision point, taking the additional transparent box cannot empty the opaque one.

## 5. Actions, policies, and commitment

The time and object of a decision can change the causal problem. Suppose that, *before* the predictor makes its forecast, an agent can irreversibly install a device that forces one-boxing. If the predictor can detect the device and fill the opaque box accordingly, installing it may causally produce a better result. CDT can recommend that earlier commitment.

That is not necessarily inconsistent with recommending two boxes later when no binding device is present. The earlier choice is between causal interventions on a commitment mechanism; the later choice is between acts after the prediction has been made. They have different descendants.

The same point applies to policies more generally. Let a policy \(\pi\) specify an action \(\pi(h)\) after each possible history \(h\). To evaluate an available intervention that installs the policy, one can write

\[
V_C(\pi)=\mathbb E[u(O_\pi)\mid E],
\]

where \(O_\pi\) includes the consequences of implementing it: other people may observe the commitment and change their behavior, and future observations may affect the prescribed act. Merely imagining that one follows a policy is not the same as possessing a causal means to bind oneself to it. A complete analysis must say what can actually be selected, when, and with what effects.

This distinction also matters in games. In a one-shot prisoner’s dilemma, defecting may causally improve a player’s payoff against each fixed move of an opponent. If the opponent’s move is correlated with the player’s because they have similar reasoning, but is not causally affected by the player’s present move, straightforward CDT treats that correlation as evidence rather than a causal influence. If the opponent observes a prior commitment or responds to communication, those are causal pathways and must be included. Correlation between “twins” and causal response to a commitment are different models.

## 6. Unsettled counterfactuals and difficult cases

The reference emphasizes that CDT does not, on its own, specify how to calculate counterfactual probabilities. Lewis’s **imaging** is one proposal: for each possible world, transfer its probability mass to a suitably close world in which the action occurs. The resulting distribution is used to evaluate the action. But “closest” requires a substantive account of which facts and laws should be preserved. The reference also notes a regress concern about determining the appropriate beliefs under the hypothetical certainty of the act.

Structural models make the required choices more explicit, but do not eliminate them. Which equation is replaced by an intervention on an agent’s choice? Can a purported intervention leave the agent’s beliefs and character unchanged? Which physical actions count as available? Different answers may yield different counterfactuals. The neat \(do\)-operator is therefore a tool for applying causal assumptions, not a machine for discovering them.

The **psychopath button** illustrates a further difficulty. Paul believes that pressing a button would kill all psychopaths, that a world without psychopaths would be better, and that someone who presses it is very likely to be a psychopath. He strongly prefers living with psychopaths to dying. If his current probability of being a psychopath is \(q\), the benefit of eliminating others is \(B\), and the loss from his own death is \(L\), a simplified causal value for pressing might be

\[
V_C(\text{press})-V_C(\text{abstain})=B-qL.
\]

If \(q\) is low enough, this version of CDT says press. Yet pressing could be strong evidence that Paul is a psychopath and therefore that he will die. Egan presents this kind of case as a counterexample: the formal rule may recommend an act whose very selection is alarming news about its consequences.

How much force the case has depends on what Paul already knows. As the reference notes, Joyce argues that a causal decision-maker can use information about their own inclinations as evidence. If Paul notices a strong desire to press before choosing, he should update \(q\), potentially making abstention causally preferable. But it is a further question whether all the evidence supplied by the eventual choice is already available in deliberation. Simply saying “update first” does not settle that issue; nor does identifying action as evidence automatically establish that it causes psychopathology.

The **adversarial offer** raises a related problem. A seller predicts which of two boxes a buyer will acquire and puts \$3 in each box predicted not to be acquired. A box costs \$1; the buyer may buy one or none. At the time of choice, the contents are fixed, and at least one box contains \$3. Therefore, under linear monetary utility, the average causal gross value of the two boxes is at least \$1.50. At least one box has causal expected net value at least \$0.50, so straightforward CDT recommends buying a box rather than none.

Yet if the seller predicts the buyer’s purchase correctly with probability \(0.75\), the purchased box is empty on correct predictions. With exactly one box predicted for purchase, the buyer’s expected net payoff is

\[
0.25(3)-1=-0.25.
\]

The seller profits in expectation. This is not a numerical contradiction: the causal evaluation uses the buyer’s present probabilities of the fixed contents, whereas the realized purchase is correlated with those contents through the prediction. It exposes a tension between local causal evaluation and performance across the correlated situations in which the rule is used. Variants of such examples and related diachronic “money pump” arguments are discussed in the reference; their force depends on the precise sequence of offers, information, and feasible commitments.

## Conclusion

CDT asks which available intervention has the highest expected utility, evaluated using beliefs about what would causally follow from each alternative. Its central discipline is to distinguish changing a fact from learning evidence about it. That discipline explains both its appeal and its controversial recommendations in predictive cases.

To apply CDT responsibly, specify the decision point, available acts or policies, evidence, utilities, and causal mechanisms; then compute the relevant counterfactual outcomes. Where those counterfactuals or the treatment of self-predictive evidence are disputed, the recommendation is conditional on the model rather than a consequence of the name “CDT” alone.

### References

- Wikipedia contributors, “[Causal decision theory](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528),” revision 1381555528.
- Gibbard, A., and Harper, W. L. “Counterfactuals and Two Kinds of Expected Utility,” 1981.
- Lewis, D. “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.
- Egan, A. “Some Counterexamples to Causal Decision Theory,” *The Philosophical Review*, 2007.
- Oesterheld, C., and Conitzer, V. “Extracting Money from Causal Decision Theorists,” *The Philosophical Quarterly*, 2021.