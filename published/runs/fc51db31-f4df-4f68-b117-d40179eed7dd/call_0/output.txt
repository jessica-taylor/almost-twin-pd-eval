# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) evaluates actions by their *news value*: if you were to learn that you had performed action \(A\), how desirable should you expect the world to be? The reference article summarizes the slogan as “do what you most want to learn that you will do” (Ahmed, via the source). EDT contrasts with causal decision theory (CDT), which asks what an action would *bring about*. The two theories agree when evidence and causation align, but they diverge in predictive or correlated cases such as Newcomb’s problem.

This essay states EDT formally, explains how it handles dependencies and counterfactuals, and applies it to several examples. I also indicate where the supplied source is silent—especially about zero-probability actions, policies, and self-locating cases—and propose operational interpretations where useful. Claims drawn from the source are identified as such; additional formal elaborations and proposals are my own.

## 1. The evidential decision rule

Consider an agent facing a set \(\mathcal A\) of possible actions. Let \(\mathcal O\) be a partition of possible outcomes, and let \(D(o)\) be the desirability, or utility, of outcome \(o\). The agent has a probability function \(P\) over the relevant propositions, including propositions of the form \(A=a\) and \(O=o\). The EDT value of action \(a\) is

\[
V(a)=\sum_{o\in\mathcal O} P(O=o\mid A=a)D(o)=\mathbb{E}[D(O)\mid A=a].
\]

This is the formula given in the reference article, attributed to Gibbard and Harper. If outcomes are determined by an action together with a state \(s\), we can equivalently write

\[
V(a)=\sum_{s\in S}P(s\mid A=a)u(a,s),
\]

where \(u(a,s)\) is the utility of the outcome produced by \(a\) in state \(s\). EDT recommends choosing an action maximizing \(V\).

The phrase “news value” is not merely metaphorical. Suppose a reliable observer sends you a message saying, “you will choose \(a\).” EDT asks how good you should expect the outcome to be after receiving that message. The action is evaluated as a piece of evidence about the world. If choosing \(a\) is strongly associated with good states, \(a\) has high news value even if \(a\) does not causally produce those states.

The reference article contrasts this with CDT’s counterfactual expected utility:

\[
U(a)=\sum_o P(A=a\mathrel{\Box\rightarrow}O=o)D(o),
\]

where \(A=a\mathrel{\Box\rightarrow}O=o\) means that outcome \(o\) would obtain in the counterfactual situation in which \(a\) is performed. In modern causal notation, one could write \(U(a)=\mathbb E[D(O)\mid do(A=a)]\); this notation is my own addition, but it captures the distinction cleanly. EDT conditions on observing or learning the action; CDT evaluates an intervention on the action.

## 2. Dependencies and counterfactuals

EDT’s central formal commitment is that the decision-relevant probabilities are ordinary conditional probabilities. Thus any dependence between action and outcome matters, whether the dependence is causal, common-causal, logical, or merely statistical.

In a causal graph, conditioning on \(A\) can provide information about ancestors or common causes of \(A\) and \(O\). An intervention \(do(A=a)\), by contrast, severs incoming causal arrows to \(A\). If \(A\) has no noncausal correlation with the causes of \(O\), the two distributions coincide. That is why EDT and CDT often agree: in many ordinary choices, learning what I chose tells me little about independent states except through my action’s effects.

They disagree when the action is evidence of something else that also affects the outcome. A predictor, a psychological twin, a diagnostic symptom, or a correlated agent can make \(P(O\mid A=a)\) differ from \(P(O\mid do(A=a))\). EDT then uses the conditional distribution. Its counterfactual is therefore not an interventionist counterfactual but an evidential or indicative supposition: “suppose I learn that I did \(a\); what follows?”

This treatment of counterfactuals is philosophically important. The source does not give a full semantics for these conditionals. A reasonable operational interpretation, which I propose rather than find in the source, is to model the agent’s uncertainty with a probability space in which the action variable has positive probability, or, when that is impossible, to use the agent’s suppositional credences. If the agent is deterministic, we can often add a small noise term representing uncertainty about which output the deterministic procedure will produce, compute conditional expectations, and take a limit if it exists. EDT is well-defined when those conditional probabilities are stable and specified.

## 3. Newcomb’s problem

The reference article’s main example is Newcomb’s problem. A predictor predicts whether the player will take both boxes or only box B. Box A always contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if it predicted two-boxing. The predictor is 99% accurate.

Let \(p=0.99\) be the accuracy, interpreted symmetrically:

\[
P(\text{predicted one}\mid \text{one})=p,\qquad
P(\text{predicted two}\mid \text{two})=p.
\]

Then EDT evaluates one-boxing as

\[
V(\text{one})=P(1M\mid \text{one})\cdot 1{,}000{,}000
=0.99\cdot 1{,}000{,}000=990{,}000.
\]

For two-boxing, if the predictor predicted two-boxing, B is empty and the player receives only A’s \$1,000; if it predicted one-boxing, B contains \$1,000,000 and the player receives \$1,001,000. Hence

\[
V(\text{two})=0.99\cdot 1{,}000+0.01\cdot 1{,}001{,}000=11{,}000.
\]

EDT therefore recommends taking only box B.

The example shows why EDT is controversial. Once the predictor has acted, taking both boxes yields \$1,000 more than taking only B in each possible state of box B. Two-boxing statewise dominates one-boxing. CDT respects dominance because the act does not change the past prediction. EDT says dominance is not decisive when the dominating act is strong evidence of a worse prior state. The choice is evaluated as news, not as a physical intervention.

A small extension, my own, clarifies the boundary. For general accuracy \(p\),

\[
V(\text{one})=p\cdot 1{,}000{,}000,
\]

\[
V(\text{two})=p\cdot 1{,}000+(1-p)\cdot 1{,}001{,}000.
\]

One-boxing is better exactly when

\[
p>\frac{1{,}001{,}000}{1{,}999{,}000}\approx 0.50075.
\]

Thus EDT does not require a perfect predictor; it requires the predictor to be better than chance by a very small margin in this payoff setup.

## 4. Correlated agents: the twin prisoner’s dilemma

The reference article also discusses a twin prisoner’s dilemma. Aomame and her psychological twin choose separately whether to cooperate or defect. Their reasoning processes are exactly analogous. Payoffs to Aomame are: both cooperate, \$5; both defect, \$1; Aomame cooperates while twin defects, \$0; Aomame defects while twin cooperates, \$10.

If Aomame’s choice is perfect evidence of her twin’s choice, then

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]

\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]

So

\[
V(C)=1\cdot 5+0\cdot 0=5,
\]

\[
V(D)=0\cdot 10+1\cdot 1=1.
\]

EDT recommends cooperation.

Again, a generalization helps. Let

\[
q=P(\text{twin cooperates}\mid \text{I cooperate}),
\]

\[
r=P(\text{twin cooperates}\mid \text{I defect}).
\]

Then

\[
V(C)=5q,
\]

\[
V(D)=10r+1(1-r)=1+9r.
\]

Cooperation is evidentially rational iff

\[
5q>1+9r.
\]

In a standard prisoner’s dilemma with independent opponents, \(q=r\), so \(V(D)-V(C)=1+4q>0\), and EDT defects. EDT cooperates only when the agent’s choice is sufficiently strong evidence that the other will cooperate. This is not a claim added to the source’s numerical example; it is an extension of the same formal rule.

## 5. Policies, dynamics, and a practical procedure

Although the source states EDT for single acts, decision problems often involve policies: functions from information states to actions. EDT can be applied to policies by treating the policy itself as the object of choice. If \(\Pi\) is a policy variable and \(O\) is the outcome produced when the agent follows that policy, define

\[
V(\pi)=\mathbb E[D(O)\mid \Pi=\pi].
\]

Choose the policy with highest news value. This matters when precommitment or algorithmic disposition is itself predictive. If a predictor predicts whether you will adopt a cooperative policy, the adoption can be good evidence about the predictor’s earlier action.

In dynamic problems, EDT may give different answers at different times because the conditioning event changes. At the outset, the agent conditions on “I will follow policy \(\pi\).” At a later node, she conditions on “I am at this node and am choosing \(a\).” If those conditional expectations conflict, EDT may recommend choosing a policy now but deviating later. A common operational response, which I propose, is to evaluate the choice that is actually available: if the agent can bind herself to a policy, the policy is the relevant act; if she cannot, each local choice is evaluated conditional on the local news. EDT itself does not automatically solve dynamic inconsistency; one must specify the feasible actions or policies.

For unfamiliar cases, the following procedure captures EDT:

1. Identify the feasible actions or policies. They should be mutually exclusive and described at the level relevant to predictors or correlated agents.
2. Specify outcomes and utilities \(D(o)\).
3. Specify a joint probability model over actions, states, other agents’ actions, predictors, and outcomes, using all admissible evidence.
4. Compute \(P(O=o\mid A=a)\) for each action.
5. Compute \(V(a)=\sum_o P(o\mid a)D(o)\).
6. Choose the action or policy with maximum \(V\).

This procedure makes clear that EDT is not a theory of physical causation. It is a rule for choosing conditional on an evidential model.

## 6. Open questions and operational interpretation

The source leaves several important questions open.

First, what if \(P(A=a)=0\)? Ordinary conditional probability is undefined when the conditioning event has probability zero. The source does not address this. In deterministic models, an agent may believe she will certainly choose one action, making alternatives zero-probability. A reasonable operational interpretation is to treat EDT’s probabilities as deliberative conditional credences rather than ratios derived from a fixed prior. Alternatively, one can introduce a small probability of alternative actions—because of noise, uncertainty about one’s own algorithm, or uncertainty about how the choice variable is realized—and then examine the limit as that probability goes to zero. If the limit is stable, it supplies the EDT value; if not, the problem needs a more precise model.

Second, which action descriptions are admissible? Conditional probabilities can depend on how an action is described. If “one-boxing” and “one-boxing because I desire the million” are treated as distinct acts, they may have different news values. The source does not settle this. I propose that EDT should use the action variable that is actually under the agent’s control and that predictors or correlated agents track. Coarser or finer descriptions are legitimate only if they represent genuinely different options or different evidential events.

Third, self-locating problems such as Sleeping Beauty are not resolved by EDT alone. The reference article notes that EDT has been used to avoid Dutch books and that Conitzer argues halfers can still be Dutch booked even when using EDT. The problem is that Beauty’s evidence is indexical: she must condition on “I am awake now” and on the betting action available at that awakening. EDT can evaluate bets once centered credences are specified, but it does not by itself determine whether the appropriate credence in heads is \(1/2\) or \(1/3\). This is an important uncertainty.

Fourth, the reference article mentions an argument that even agents uncertain about EDT may have reason to act as if EDT were true, because EDT can involve many correlated decision-makers and therefore high stakes. This “evidentialist’s wager” is a strategic argument, not a derivation of EDT’s core rule. It suggests a pragmatic reason to use EDT in large correlated settings, but it does not remove the need to specify conditional probabilities.

## 7. Criticism and philosophical import

The source quotes two classic criticisms. Lewis calls EDT “an irrational policy of managing the news.” Joyce says rational agents choose on the basis of causal efficacy, not auspiciousness. The objections are best understood through cases where an action is bad news but causally harmless, or good news but causally useless.

Consider a case not in the source, which I use only as illustration. A genetic lesion causes both a desire to smoke and cancer, but smoking itself does not cause cancer. If smoking is strong evidence that one has the lesion, EDT may recommend not smoking because not smoking is better news. CDT would recommend smoking if smoking gives pleasure and does not change the lesion. EDT’s critics say this confuses choosing symptoms with choosing causes. EDT’s defenders can reply that if the agent’s aim is to obtain good outcomes, and her action is reliable evidence about those outcomes, it is rational to choose the action with the better evidential profile. The dispute is therefore not merely computational; it concerns what decision theory is for.

EDT also has attractive features. It gives a simple Bayesian rule, handles prediction and correlation directly, and avoids some puzzles where causal models are difficult to specify. In cases with predictors, identical agents, or large populations of correlated decision-makers, EDT can give stable, intuitively compelling advice.

## Conclusion

Evidential decision theory says: choose the action whose occurrence would be the best news. Formally, it maximizes expected utility conditional on the action,

\[
V(a)=\mathbb E[D(O)\mid A=a].
\]

It differs from causal decision theory by using evidential conditionals rather than interventionist counterfactuals. This makes EDT one-box in Newcomb’s problem and cooperate in perfectly correlated twin dilemmas, but it also exposes EDT to the criticism that it rewards auspicious signs rather than causal effectiveness. To apply EDT to new problems, one must carefully specify the action or policy variable, the outcome utilities, and the conditional probability model. Where the source is silent—zero-probability actions, policy dynamics, and indexical cases—an operational interpretation based on suppositional credences or limiting noise models can make the theory usable, but the philosophical dispute between evidential and causal rationality remains unresolved.

## References

- Wikipedia contributors. “Evidential decision theory.” Revision 1373679688, 7 Sep. 2026. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.
- Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1981): 5–30.
- Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.
- Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192 (2015): 2887–2899.