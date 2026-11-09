# Evidential Decision Theory: Choosing What Would Be Good News

Suppose an action would be excellent news about a fact you cannot change. Is that a reason to perform it?

Evidential decision theory, or **EDT**, answers yes, provided that the news improves the action’s expected outcome enough to outweigh its costs. Its guiding idea is to choose the act that you would most want to learn you had performed. This does not mean that an agent literally waits for a news report about their own behavior. It means that, in evaluating an available action, the agent asks what the action would indicate about everything relevant to the outcome.

The contrast is with **causal decision theory** (CDT), which evaluates an action by what it would causally bring about. Ordinarily the two approaches agree: taking an umbrella both causes you to stay drier and is evidence that you stay drier. They can diverge when your choice is evidence about something it does not cause—for example, a prediction made before you act, or the simultaneous choice of a sufficiently similar decision-maker.

The reference article presents EDT’s conditional-expectation rule and illustrates it with Newcomb’s problem and a twin prisoner’s dilemma. It does not, however, settle every question about how an agent should construct the relevant probabilities. In particular, conditioning on a contemplated choice, treating policies as alternatives, and handling actions assigned probability zero require further interpretation. The operational suggestions below are proposals for applying the article’s central rule, not additional claims established by the article.

## 1. The formal rule

Let \(K\) represent the information the agent has at the decision point. Let \(A\) range over available actions, and let \(O_1,O_2,\ldots\) be mutually exclusive and exhaustive outcomes. An outcome should include everything the agent values: not just money or an external state, but also action costs, side effects, and any relevant effects on other people.

Write \(u(O_j)\) for the utility of outcome \(O_j\). EDT assigns the action \(A\) the evidential value

\[
V_K(A)=\sum_j P(O_j\mid A,K)\,u(O_j).
\]

The recommended action is one that maximizes this quantity:

\[
A^*\in\operatorname*{arg\,max}_{A}V_K(A).
\]

Equivalently, if utility is represented by a random variable \(U\),

\[
V_K(A)=\mathbb E[U\mid A,K].
\]

The \(K\) matters. The agent evaluates each action using the same information available before choosing, augmented for that evaluation by the supposition that the action occurs. It should not compare one act using information known only under that act with another using less information.

In a finite model where \(P(A\mid K)>0\), the conditional probabilities obey Bayes’ rule:

\[
P(O_j\mid A,K)
=\frac{P(A\mid O_j,K)P(O_j\mid K)}
       {P(A\mid K)}.
\]

This formula shows how an action acquires *news value*. If the action is more likely in some circumstances than others, learning that it occurred shifts probability toward those circumstances. Those circumstances might be future consequences of the action, but they might also include facts already settled.

Utilities need not be monetary. The dollar calculations below assume, for simplicity, that utility is linear in money over the relevant ranges. With risk aversion or other preferences, the same procedure applies after replacing dollar amounts with the appropriate utilities.

### What is being conditioned on?

An important distinction is between:

1. **The action being chosen:** “I take one box.”
2. **The hypothetical evaluation:** “How good would things be, conditional on my taking one box?”

The second is not an instruction to cause oneself to believe the first, nor a claim that merely saying the words makes the outcome likely. It is a calculation using a probabilistic model of how the agent’s choice is related to the world.

That model must include the agent as a decision-maker. If a predictor has learned about the agent’s reasoning, or another person reasons similarly, the probability model should represent those relationships. Otherwise it may miss precisely the dependencies that EDT regards as relevant.

## 2. Conditioning is not intervention

The article contrasts EDT’s conditional probabilities with CDT’s probabilities for outcomes in a counterfactual situation where an action is performed. A common causal-model illustration is

\[
V_{\mathrm{CDT}}(A)
=\sum_j P(O_j\mid \operatorname{do}(A),K)\,u(O_j),
\]

where \(\operatorname{do}(A)\) represents an intervention that sets the action while leaving the model’s other causal mechanisms in place. This is a useful illustration, though not every formulation of CDT is exhausted by a single intervention notation.

Conditioning and intervention answer different questions:

- \(P(O\mid A,K)\): Among cases compatible with what I know in which I perform \(A\), how often does \(O\) occur?
- \(P(O\mid\operatorname{do}(A),K)\): How often would \(O\) occur if \(A\) were set by the relevant intervention?

Suppose a hidden trait \(T\) affects both an action \(A\) and an outcome \(O\). Observing \(A\) gives evidence about \(T\), which in turn gives evidence about \(O\). But intervening on \(A\) need not change \(T\). Consequently the two probabilities may differ even when the agent’s action has no causal effect on the hidden trait.

EDT does not say that correlations are causes. It gives correlations a decision-theoretic role as *evidence*. The philosophical dispute is whether an agent should use all such evidence when choosing, or should instead isolate the changes their action would cause.

## 3. Newcomb’s problem

In the article’s version of Newcomb’s problem, a transparent box contains $1,000. An opaque box contains either $1,000,000 or nothing. A highly reliable predictor has already filled the opaque box: it put the million there if it predicted that the agent would take only that box, and left it empty if it predicted that the agent would take both.

The agent now chooses between:

- \(B\): take only the opaque box;
- \(AB\): take both boxes.

The crucial evidential assumptions in the article’s numerical example are

\[
P(\text{million}\mid B)=0.99,\qquad
P(\text{million}\mid AB)=0.01.
\]

Assuming linear utility for money,

\[
V(B)=0.99(\$1{,}000{,}000)+0.01(\$0)
=\$990{,}000,
\]

whereas

\[
V(AB)=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
=\$11{,}000.
\]

EDT therefore recommends taking only the opaque box. The action is excellent evidence that the predictor anticipated it and filled that box.

The causal recommendation is different under the usual assumptions. The predictor’s decision is over, and the contents of the opaque box will not change when the agent chooses. Whatever that box contains, taking both adds $1,000. CDT accordingly recommends both boxes.

The evidential calculation does **not** say that one-boxing causes a past prediction. It says that, in the model, the choice and the prediction are correlated. One possible explanation is that the predictor has reliable information about features of the agent that also influence the agent’s eventual choice.

### Accuracy needs interpretation

“99% accurate” by itself does not automatically imply both conditional probabilities used above. Overall accuracy can coexist with different error rates for different actions, and the frequencies of the two choices also matter.

For a general model, set

\[
q_B=P(\text{million}\mid B,K),\qquad
q_{AB}=P(\text{million}\mid AB,K).
\]

Then

\[
V(B)=1{,}000{,}000q_B,\qquad
V(AB)=1{,}000+1{,}000{,}000q_{AB}.
\]

One-boxing is preferred exactly when

\[
q_B-q_{AB}>0.001.
\]

Thus even a relatively small evidential difference can outweigh the extra $1,000, because the opaque box has such a large stake. But the difference must be justified by the agent’s actual probability model; it cannot simply be assumed from the presence of someone called a “predictor.”

## 4. Correlated agents: the twin dilemma

Now imagine the twin prisoner’s dilemma from the source. Aomame chooses whether to cooperate or defect against a psychological twin. Each gets $5 if both cooperate and $1 if both defect. A lone defector gets $10, while the cooperator gets nothing.

With perfect conditional matching,

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1
\]

and

\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]

So EDT gives cooperation value $5 and defection value $1. It recommends cooperation even if Aomame cares only about her own payoff.

Again, the point is evidential, not telepathic. Aomame’s choice may not send a signal to her twin, yet it can reveal something about what a very similar decision process does in a very similar situation. A causal theorist who treats the twin’s move as unaffected by Aomame’s act sees defection as better: against either fixed move, it pays $5 more.

Perfect similarity is not essential. Let

\[
c=P(\text{twin cooperates}\mid C,K),\qquad
d=P(\text{twin cooperates}\mid D,K).
\]

Then

\[
V(C)=5c,\qquad
V(D)=10d+1(1-d)=1+9d.
\]

EDT cooperates when \(5c>1+9d\). Mere resemblance is insufficient; what matters is how strongly the two choices are correlated **conditional on the information already available**. If Aomame knows facts that largely determine her twin’s action independently of her own, the evidential advantage of cooperation may disappear.

## 5. The “managing the news” objection

The article reports a central criticism: David Lewis characterized EDT as an irrational policy of “managing the news,” while James Joyce argued that rational agents should attend to causal efficacy rather than auspiciousness. A medical example brings the objection into focus.

Suppose a condition \(G\) causes both a craving to smoke and a high risk of illness. Assume, for the example, that smoking itself has no effect on illness but gives a small pleasure. If smoking is evidence of \(G\), then a simple EDT calculation may favor not smoking: nonsmokers are less likely to have the condition. Yet, the critic says, refraining cannot change whether you already have \(G\); if smoking is otherwise harmless and pleasurable, why give it up?

This is a genuine challenge, not a mathematical inconsistency. The disagreement concerns the relevance of the evidential association. EDT’s proponent can respond that an agent should choose the act associated, on their best probabilities, with the better outcome. The critic replies that such a rule may sacrifice a benefit to obtain only reassuring evidence about an unchanged fact.

The details of the information state are also important. Suppose the agent already knows whether they have the craving, and smoking conveys no further information about \(G\) once that fact is included in \(K\). Then

\[
P(G\mid \text{smoke},K)
=
P(G\mid \text{abstain},K).
\]

If smoking has no health effect and adds pleasure, EDT now favors smoking. This illustrates why one should condition on relevant information already possessed, rather than on population correlations that it screens off.

It does not solve every version of the objection. An agent may remain uncertain about a latent disposition even after introspection; their eventual act may still provide evidence about it. Whether conditioning on that residual evidence is rational is precisely part of the dispute.

## 6. Policies, prediction, and randomization

Sometimes the natural alternatives are not isolated acts but **policies**: rules that specify what to do in each possible information state. For a policy \(\pi\), an evidential evaluation might be written

\[
V_K(\pi)=\mathbb E[U\mid \Pi=\pi,K],
\]

where \(\Pi\) is a random variable representing which policy the agent follows. The policy’s outcome includes what happens in all relevant circumstances, weighted by their probabilities conditional on following that policy.

This is a proposed extension of the article’s action rule. It is useful when a predictor forecasts the agent’s decision procedure, when several decisions are linked, or when commitment to a rule is itself observable. But it raises a modeling question: is the policy genuinely an available alternative, and what would selecting it be evidence of? One cannot assume that a predictor responds identically to a policy choice and to a later isolated action.

Randomization makes the distinction vivid. Suppose an agent commits to use a private, genuinely unpredictable coin to choose between two acts. If the coin is independent of the predictor’s earlier prediction, then the **realized coin result** need not be evidence about that prediction. But the prior decision to adopt a randomized policy may itself be predictable, and the predictor may respond to that policy. The probabilities must describe the actual sequence: when the policy is chosen, what the predictor can observe, and when the random draw occurs.

In particular, one should not automatically transfer the 99% conditional probabilities from the deterministic Newcomb example to a newly introduced randomizing procedure. Nor should one automatically assume randomization defeats prediction. Both conclusions depend on the model.

Policy evaluation can also differ from re-evaluation at a later decision point. A policy that looked best before new information arrived may prescribe an act that looks inferior after conditioning on that information. An agent may then face a question about commitment or dynamic consistency. EDT’s one-step formula alone does not decide every such question: the analyst must specify what commitments are feasible and whether the choice being evaluated is the earlier policy or the later act.

## 7. Zero probabilities and the decision model

The elementary conditional formula is undefined if \(P(A\mid K)=0\). This can arise if the agent is certain which action they will take, or if an idealized deterministic model assigns zero probability to an alternative. Yet a decision problem still appears to ask what to do.

The source’s formula does not specify a universal repair. Several approaches are possible:

- Use a model that assigns positive probability to each genuinely available alternative.
- Consider a limiting family of models in which each alternative has small positive probability.
- Supply conditional probabilities or counterfactual assumptions separately rather than deriving them by the elementary ratio.

These approaches need not agree. In particular, a limit can depend on *how* probability is perturbed: a rare act caused by a prediction error may carry different evidence from a rare act caused by an independent coin. Merely declaring an action to have an infinitesimal probability does not settle its evidential value.

A practical proposal is to make the source of variation explicit. Ask what would distinguish cases in which the agent takes one available act from cases in which they take another: uncertainty about preferences, reasoning, private information, implementation error, or a random device. Build the joint distribution around that story, check that it respects what is already known, and then test whether the recommendation changes under plausible alternative stories. This is not a theorem of EDT; it is a way to expose assumptions that might otherwise be hidden inside \(P(O\mid A,K)\).

The same caution applies to using past data. An observed association between an action and an outcome is not necessarily the conditional probability relevant to *this* decision. The populations may differ, important information may already have been learned, and changing the available policy may change the selection mechanism.

## 8. A procedure for unfamiliar cases

The following workflow combines the source’s rule with the modeling proposals above.

1. **Specify the decision point and information \(K\).** Include observations, known past events, available commitments, and what the agent knows about predictors or other decision-makers.

2. **List the actual alternatives.** Decide whether these are immediate acts, randomized procedures, or policies extending across future situations. Include relevant costs and constraints.

3. **Define outcomes and utilities.** Outcomes should capture everything valued, including the action’s direct effects. Use money as a proxy only when the assumptions justify it.

4. **Model the joint dependencies.** Represent predictors, common causes, correlated agents, and random devices as appropriate. Do not remove a dependency merely because it is noncausal; equally, do not invent one because an example resembles Newcomb’s problem.

5. **Calculate \(P(O_j\mid A,K)\)** for every alternative and outcome. Keep the same background information fixed across comparisons. Check that the conditional probabilities are defined and that claims of predictive accuracy imply the probabilities actually used.

6. **Compute and compare expected utilities.** If results depend heavily on uncertain correlations or utilities, report the threshold at which the recommendation changes, as in the Newcomb and twin examples above.

7. **Identify unresolved modeling choices.** If zero-probability alternatives, policy commitments, or later re-evaluation matter, say which interpretation is being used and how another plausible interpretation could alter the result.

This procedure is not a guarantee of an uncontroversial answer. EDT supplies a decision criterion, but a criterion needs a probability model and a utility function before it yields a verdict.

## 9. Broader implications and limits

The reference article notes applications to the Sleeping Beauty problem and Dutch-book arguments, while also reporting Conitzer’s argument that adopting EDT does not remove every Dutch-book difficulty for an agent who assigns probability \(1/2\) to heads on awakening. The lesson is not that EDT settles the disputed credence. In repeated or memory-erasing settings, one must specify the betting opportunities, what is paid at each awakening, and whether the object of choice is an individual bet or a policy across awakenings. Different specifications can produce different evaluations.

The article also mentions an argument for taking EDT seriously under uncertainty about decision theory: if one’s decision is evidence about many correlated decision-makers, the evidential stakes may be unusually large. This is a consideration, not a general proof that EDT must dominate. Its force depends on the strength and number of correlations, the utilities at stake, and how competing decision theories are compared.

## Conclusion

EDT evaluates an action by the expected utility of the world conditional on that action. Its distinctive feature is not a belief that choices magically alter the past or control distant agents, but a willingness to treat an action’s noncausal associations as relevant evidence. That produces one-boxing in the standard Newcomb calculation and cooperation in a sufficiently correlated twin dilemma, while also inviting the objection that agents may end up managing news rather than outcomes.

To apply EDT well, the decisive work is often in the model: specify what the agent knows, what alternatives are really available, and why each action would be evidence of particular outcomes. The formula is compact; the dependencies it asks us to understand need not be.

### References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688. CC BY-SA 4.0.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.
- Vincent Conitzer, “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists,” *Synthese*, 2015.