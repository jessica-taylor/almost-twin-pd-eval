# Evidential Decision Theory: Choosing What Is Good News

Evidential decision theory (EDT) is a decision rule that evaluates actions by their *news value*: if you were to learn that you had performed some action, how desirable would you expect the outcome to be? The human-written reference article summarizes the slogan nicely: EDT recommends doing “what you most want to learn that you will do” (Wikipedia contributors, 2026). The theory is historically associated with Allan Gibbard and William Harper’s distinction between two kinds of expected utility, and it is most famous for recommending one-boxing in Newcomb’s paradox while causal decision theory recommends two-boxing.

This essay gives a self-contained formulation of EDT, explains how it applies to actions and policies, describes how it treats dependencies and counterfactuals, and discusses how a mathematically literate reader can use it in unfamiliar decision problems. I will distinguish the claims of the supplied source from my own operational suggestions.

---

## 1. The basic formal rule

Suppose an agent faces a finite set of possible actions

\[
\mathcal A=\{a_1,\dots,a_n\}.
\]

Let \(O\) be a random variable taking values in an outcome space \(\mathcal O\). The agent has a probability function \(P\) over relevant propositions, including propositions about which action she will perform and which outcome will occur. She also has a desirability or utility function

\[
D:\mathcal O\to \mathbb R.
\]

For finite outcome spaces, EDT assigns to each action \(A=a\) the value

\[
V(a)=\sum_{j} P(O=o_j \mid A=a)\,D(o_j).
\]

Equivalently,

\[
V(a)=\mathbb E[D(O)\mid A=a].
\]

The EDT prescription is:

\[
\text{Choose } a^*\in\operatorname{argmax}_{a\in\mathcal A} V(a).
\]

If the outcome space is continuous, the sum is replaced by an integral or by the appropriate conditional expectation:

\[
V(a)=\int_{\mathcal O} D(o)\,dP(o\mid A=a).
\]

The reference article presents essentially this formula, attributing it to Gibbard and Harper:

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

A useful equivalent formulation introduces a state space \(\mathcal S\). Let each state \(s\in\mathcal S\) encode all relevant background facts: what a predictor predicted, what another agent will do, whether a disease is present, and so on. Let \(u(a,s)\) be the utility of performing action \(a\) in state \(s\). Then

\[
V(a)=\sum_{s\in\mathcal S} P(s\mid A=a)\,u(a,s).
\]

This formulation makes clear that EDT does not require the standard independence assumption that the state is probabilistically independent of the action. In EDT, the conditional distribution \(P(s\mid A=a)\) may differ from \(P(s)\). The action can be evidence about the state.

The theory therefore differs from a simple causal expected-utility rule. Causal decision theory (CDT) is often expressed using counterfactual probabilities:

\[
U(A)=\sum_j P(A\mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A\mathrel{\Box\rightarrow} O_j\) means something like “if \(A\) were performed, \(O_j\) would occur.” In modern causal-model language, CDT evaluates

\[
U_{\mathrm{CDT}}(a)=\sum_j P(O=o_j\mid \operatorname{do}(A=a))D(o_j),
\]

where \(\operatorname{do}(A=a)\) represents an intervention that sets the action to \(a\). EDT instead uses the ordinary conditional probability \(P(O=o_j\mid A=a)\). When intervention and conditioning coincide, EDT and CDT agree. They differ when the action is probabilistically correlated with outcomes for reasons other than, or in addition to, direct causation.

---

## 2. What EDT means by “evidence”

The core idea is that an action can be *diagnostic* of other facts. If choosing \(a\) is strongly correlated with a good outcome, then \(a\) has high news value. The correlation may arise in several ways:

1. **Causation from action to outcome.**  
   If studying causes good exam results, then \(P(\text{good result}\mid \text{study})\) may be high partly because studying causally improves performance.

2. **Common causes.**  
   A hidden factor may influence both the action and the outcome. If a genetic lesion both causes a preference for smoking and causes cancer, then smoking is evidence of cancer even if smoking itself does not cause cancer.

3. **Prediction.**  
   A predictor may have already predicted your action. Your present action is evidence of what the predictor predicted.

4. **Logical or algorithmic correlation.**  
   If two agents use the same reasoning procedure in symmetric circumstances, one agent’s action may be strong evidence about the other’s action, even without communication or causal influence.

EDT treats all of these sources of dependence in the same way: include them in the probability model, condition on the action, and compute expected utility.

This is why EDT is often described as choosing the action that would be the best news. The phrase “news” should not be taken literally. The agent is not waiting to hear what she did. Rather, the decision rule says that the rational value of an action is the conditional expected utility of the world given that action.

---

## 3. Evaluating policies, not merely one-shot actions

The source article gives the EDT formula for actions. Many real decisions, however, concern policies: rules, dispositions, algorithms, or plans that determine actions across multiple situations. EDT can be extended naturally to policies by treating a policy as the object of conditionalization.

Let \(\Pi\) be a set of possible policies. A policy \(\pi\) might say, for example, “cooperate in all prisoner’s-dilemma interactions with psychologically similar agents” or “one-box in every Newcomb problem with a sufficiently reliable predictor.” If \(\Pi=\pi\) is the proposition that the agent adopts policy \(\pi\), then the evidential value of the policy is

\[
V(\pi)=\mathbb E[D(O)\mid \Pi=\pi].
\]

The agent chooses

\[
\pi^*\in\operatorname{argmax}_{\pi\in\Pi} V(\pi).
\]

This extension is not explicitly developed in the supplied source, but it is a natural operational interpretation. The source’s basic rule applies to any proposition whose truth can be conditioned on; a policy is just such a proposition.

Policy evaluation matters in sequential problems. Suppose an agent must choose today whether to commit to a future plan. If predictors, other agents, or her own future decisions are correlated with that plan, EDT says to condition on the whole policy, not merely on the local action at one moment. A myopic action-by-action application can miss important dependencies.

One subtle point concerns randomization. If a policy says “choose \(a\) with probability \(p\) and \(b\) with probability \(1-p\),” EDT evaluates the policy by conditioning on the proposition that this randomization rule is used. The value need not be exactly

\[
pV(a)+(1-p)V(b),
\]

because the news that you use a particular randomization rule may itself carry information about other variables. If the randomization device is independent of everything relevant, the simple weighted average will often be appropriate. But EDT’s primitive rule is always conditional expected utility given the object being evaluated.

---

## 4. Newcomb’s paradox

The reference article’s central example is Newcomb’s paradox. There is a predictor, a player, and two boxes:

- Box A is transparent and always contains \$1,000.
- Box B is opaque.
- If the predictor predicted that the player will take only box B, box B contains \$1,000,000.
- If the predictor predicted that the player will take both boxes, box B contains nothing.

The player can either take only box B, called one-boxing, or take both boxes, called two-boxing.

Suppose the predictor is 99% reliable in the symmetric sense that

\[
P(\text{predicted one-box}\mid \text{one-box})=0.99
\]

and

\[
P(\text{predicted two-box}\mid \text{two-box})=0.99.
\]

Then EDT computes:

\[
\begin{aligned}
V(\text{one-box})
&=P(\text{\$1M in B}\mid \text{one-box})\cdot \$1{,}000{,}000 \\
&\quad +P(\text{\$0 in B}\mid \text{one-box})\cdot \$0 \\
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0 \\
&=\$990{,}000.
\end{aligned}
\]

For two-boxing:

\[
\begin{aligned}
V(\text{two-box})
&=P(\text{\$1M in B}\mid \text{two-box})\cdot \$1{,}001{,}000 \\
&\quad +P(\text{\$0 in B}\mid \text{two-box})\cdot \$1{,}000 \\
&=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000 \\
&=\$11{,}000.
\end{aligned}
\]

Because

\[
V(\text{one-box})>V(\text{two-box}),
\]

EDT recommends taking only box B.

The intuitive explanation is that one-boxing is strong evidence that the predictor predicted one-boxing, and therefore strong evidence that box B contains \$1,000,000. Two-boxing is strong evidence that the predictor predicted two-boxing, and therefore strong evidence that box B is empty.

CDT gives the opposite recommendation. It says that the contents of box B are already fixed, so taking both boxes cannot causally change whether box B contains \$1,000,000. Given that the money is either there or not, taking both boxes adds \$1,000. Thus CDT two-boxes.

The disagreement is not about arithmetic. It is about whether the decision rule should condition on the action or intervene on the action. EDT conditions: “Given that I one-box, what is likely true?” CDT intervenes: “If I bring it about that I two-box, what will happen?”

---

## 5. Twin prisoner’s dilemma

The source also discusses a twin prisoner’s dilemma. Aomame and her psychological twin are in separate rooms. They cannot communicate. Their reasoning processes are exactly analogous. The payoff matrix for each is:

- Both cooperate: each gets \$5.
- Both defect: each gets \$1.
- One cooperates, one defects: cooperator gets \$0, defector gets \$10.

If the twins are exactly alike and face symmetric circumstances, EDT treats Aomame’s choice as perfect evidence about her twin’s choice:

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]

\[
P(\text{twin defects}\mid \text{Aomame defects})=1.
\]

Then

\[
\begin{aligned}
V(\text{cooperate})
&=1\cdot \$5+0\cdot \$0 \\
&=\$5,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{defect})
&=0\cdot \$10+1\cdot \$1 \\
&=\$1.
\end{aligned}
\]

So EDT recommends cooperation.

This example is useful because it shows how EDT handles noncausal dependence. Aomame’s choice does not cause her twin’s choice. The twin is in another room. But because the two agents are psychologically identical and reason in the same way, Aomame’s choice is evidence of her twin’s choice. EDT counts that evidence.

A more general version helps in unfamiliar cases. Suppose the twins are not perfect copies but are highly correlated. Let \(\varepsilon\) be the probability that the twin makes the opposite choice:

\[
P(\text{twin defects}\mid \text{Aomame cooperates})=\varepsilon,
\]

\[
P(\text{twin cooperates}\mid \text{Aomame defects})=\varepsilon.
\]

Then

\[
V(\text{cooperate})=(1-\varepsilon)\cdot \$5+\varepsilon\cdot \$0=5(1-\varepsilon),
\]

and

\[
V(\text{defect})=\varepsilon\cdot \$10+(1-\varepsilon)\cdot \$1=1+9\varepsilon.
\]

EDT recommends cooperation exactly when

\[
5(1-\varepsilon)>1+9\varepsilon,
\]

which simplifies to

\[
4>14\varepsilon,
\]

or

\[
\varepsilon<\frac{2}{7}\approx 0.286.
\]

Thus, if the correlation is stronger than roughly 71.4%, EDT cooperates. This kind of calculation gives a practical way to apply EDT when correlations are imperfect.

---

## 6. A non-source example: the smoking lesion

To see EDT’s distinctive treatment of common-cause dependence, consider a standard philosophical example not mentioned in the supplied source: the smoking lesion problem.

Suppose a genetic lesion causes both a strong desire to smoke and a high probability of cancer. Smoking itself does not causally affect cancer; only the lesion does. The agent likes smoking but dislikes cancer.

Let the utilities be:

- Smoking gives pleasure \(+1\).
- Cancer gives harm \(-100\).
- Not smoking gives \(0\) if no cancer, and \(-100\) if cancer.

Suppose smoking is very strong evidence of the lesion, and hence of cancer:

\[
P(\text{cancer}\mid \text{smoke})=0.9,
\]

\[
P(\text{cancer}\mid \text{do not smoke})=0.1.
\]

Then EDT gives

\[
V(\text{smoke})=1+0.9(-100)+0.1(0)=-89,
\]

and

\[
V(\text{do not smoke})=0+0.1(-100)+0.9(0)=-10.
\]

EDT recommends not smoking, even though smoking does not cause cancer. The action is bad news.

CDT, by contrast, says that since smoking does not causally affect cancer, the agent should smoke for the small pleasure.

This example illustrates the main philosophical dispute around EDT. Critics say EDT recommends avoiding harmless actions merely because they are correlated with bad outcomes. Defenders reply that EDT correctly takes seriously evidential dependencies that CDT ignores, especially in cases involving predictors, twins, and correlated agents.

---

## 7. How to apply EDT in an unfamiliar case

The source article does not give a full operational manual. The following procedure is my own reconstruction of how EDT can be used in practice.

### Step 1: Specify the feasible actions or policies

List the alternatives the agent can choose. These may be simple actions, such as “one-box” and “two-box,” or policies, such as “use this decision algorithm in all similar cases.”

The alternatives should form a partition for the purpose of the decision: they should be mutually exclusive and exhaustive descriptions of the choices being evaluated.

### Step 2: Specify outcomes and utilities

Define the outcomes the agent cares about and assign utilities to them. If the agent cares only about her own payoff, \(D\) represents that payoff. If she also cares about the payoffs of correlated agents, future people, or other morally relevant consequences, those should be included in the outcome description.

### Step 3: Build a joint probability model

The agent needs a probability model over:

- her possible actions or policies;
- relevant states of the world;
- other agents’ actions;
- predictors’ predictions;
- outcomes.

EDT does not itself tell you where these probabilities come from. They may come from frequencies, scientific models, symmetry arguments, logical reasoning, or subjective judgment. The theory assumes that the agent has a coherent probability function.

### Step 4: Compute conditional probabilities

For each action \(a\), compute

\[
P(O=o_j\mid A=a).
\]

If direct conditioning is difficult, Bayes’ rule may help:

\[
P(O=o_j\mid A=a)=\frac{P(A=a\mid O=o_j)P(O=o_j)}{P(A=a)}.
\]

In predictor cases, one often estimates conditional accuracy directly:

\[
P(\text{prediction}=a\mid \text{action}=a).
\]

In twin or algorithmic cases, one may use symmetry. If two agents use exactly the same algorithm in exactly the same information state, it is natural to assign probability 1 to their making the same choice. If the similarity is imperfect, one can assign a high but less-than-one conditional probability.

### Step 5: Compute evidential expected utility

For each action or policy, compute

\[
V(a)=\sum_j P(O=o_j\mid A=a)D(o_j).
\]

Choose the action or policy with the largest value.

### Step 6: Check whether the object of evaluation is right

Sometimes the outcome depends not on a single action but on a disposition, rule, or publicly observable policy. In those cases, condition on the disposition or policy rather than on a narrow local act. For example, if a predictor predicts whether you are generally cooperative, evaluate the policy “be cooperative,” not merely today’s isolated cooperative act.

This is an interpretive addition, but it follows the spirit of EDT: condition on the fact whose news value you are assessing.

---

## 8. Zero-probability actions and deterministic agents

One important issue left open in the source is how EDT should handle actions that the agent assigns probability zero. If the agent believes her future action is determined by her reasoning process, she may assign probability 1 to one action and 0 to the alternatives. Then ordinary conditional probabilities such as \(P(O\mid A=a)\) may be undefined for the alternatives.

A practical operational proposal is to introduce a small amount of deliberative noise. Suppose the agent assigns probability \(1-\eta\) to the action she expects to take and distributes probability \(\eta>0\) among the alternatives. She computes EDT values using this regularized probability distribution. If the recommendation is stable as \(\eta\to 0\), she can take that stable recommendation as the EDT verdict.

Another approach is to evaluate policies rather than individual acts. Even if the agent is uncertain about which exact act she will perform, she may be able to reason about the probability that she follows one policy rather than another.

These are not claims made by the source; they are my own suggestions for making EDT operational. The basic point is that EDT requires conditional probabilities, so some well-defined probability distribution over possible actions or policies is needed. If no such distribution is available, or if the result depends arbitrarily on how zero probabilities are regularized, EDT may not give a determinate verdict in that case.

---

## 9. Dependencies, counterfactuals, and causal structure

EDT’s treatment of counterfactuals is epistemic rather than interventionist. The expression

\[
P(O=o_j\mid A=a)
\]

can be read as: “How probable is outcome \(o_j\), given the supposition that action \(a\) is performed?” This is close to Ramsey-style conditional supposition: temporarily add \(A=a\) to your belief state and see what follows probabilistically.

CDT, by contrast, asks what would happen if the agent intervened to bring about \(a\). In causal Bayesian networks, the distinction is:

\[
P(O=o_j\mid A=a)
\]

versus

\[
P(O=o_j\mid \operatorname{do}(A=a)).
\]

If the action has common causes with the outcome, these can differ. For example, in a causal graph,

\[
A \leftarrow L \rightarrow O,
\]

conditioning on \(A\) gives information about \(L\), and hence about \(O\). But intervening on \(A\) severs the arrow from \(L\) to \(A\), so \(A\) no longer provides information about \(L\). EDT uses the conditional dependence; CDT uses the interventional distribution.

In logical-correlation cases, such as the twin prisoner’s dilemma, the dependence is not easily represented by ordinary causal arrows. The two agents’ choices are correlated because they are outputs of similar or identical computations. EDT can still model this by assigning

\[
P(\text{twin cooperates}\mid \text{I cooperate})
\]

a high value. Whether such dependencies should be treated as genuinely counterfactual, merely evidential, or something else is philosophically contested. The source does not resolve this; EDT’s formal rule only requires that the conditional probabilities be specified.

---

## 10. Criticism and the “managing the news” objection

The source article quotes David Lewis’s criticism that EDT promotes “an irrational policy of managing the news,” and James Joyce’s claim that rational agents choose acts on the basis of causal efficacy, not auspiciousness.

The objection is sharpest in smoking-lesion-style cases. If an action does not causally affect an outcome but is merely correlated with it, EDT may recommend avoiding the action because it is bad news. Critics say this confuses rational decision-making with impression management.

EDT has several possible responses. First, in many famous cases, such as Newcomb’s problem and the twin prisoner’s dilemma, the evidential correlation is not an irrelevant coincidence. The action is tied to the outcome through prediction or shared reasoning. One-boxing is not merely pleasant news; it is associated with the predictor having placed money in the box. Cooperating is associated with the twin also cooperating.

Second, if the world contains reliable predictors or many similar agents, conditioning on one’s action may track real patterns in the world. EDT treats these patterns as decision-relevant. CDT says that only causal influence is decision-relevant.

Still, the disagreement remains substantive. EDT and CDT embody different views about what a decision is: an evidential event that reveals information, or an intervention that changes the world.

---

## 11. The evidentialist’s wager and correlated decision-makers

The source mentions a further argument: even if one has only partial confidence in EDT, it may be reasonable to act as if EDT were true because EDT can involve the actions of many correlated decision-makers, and therefore its stakes may be higher than those of CDT.

This idea, sometimes called the evidentialist’s wager, can be expressed schematically. Let \(q\) be your credence that EDT is correct. Suppose that if EDT is correct, adopting EDT rather than CDT yields a large gain \(G\) because your choice is correlated with many other agents’ choices. Suppose that if EDT is false, adopting EDT rather than CDT incurs a loss \(L\) in some local cases. Then a simple expected-value comparison favors acting according to EDT if

\[
qG>(1-q)L.
\]

The source does not give this exact formula; it only states the qualitative idea. The wager is also not a proof that EDT is true. It is a pragmatic argument for using EDT in domains where correlation among decision-makers could matter greatly.

This argument is especially relevant to large-scale coordination problems, altruistic decisions, and scenarios involving artificial intelligences or institutions that reason similarly. If your cooperative behavior is evidence that many similar agents will also cooperate, EDT can assign high value to cooperation even when the direct causal effect of one act is small.

---

## 12. Sleeping Beauty and unresolved cases

The source briefly mentions the Sleeping Beauty problem. In that problem, a coin is flipped, and Beauty is awakened either once or twice depending on the result, with amnesia between awakenings. Philosophers disagree about whether Beauty’s credence in heads should be \(1/2\) or \(1/3\).

According to the source, EDT has been applied to Sleeping Beauty in order to avoid Dutch-book arguments. It has been argued that Beauty can avoid certain Dutch books by adopting EDT, but Vincent Conitzer argues that halfers remain vulnerable even after adopting EDT.

This illustrates an important limitation of the source: EDT’s formal expected-utility rule is clear, but its application can depend on difficult questions about self-locating belief, probability over centered worlds, and how bets are offered across multiple indistinguishable awakenings. The supplied article does not settle these questions. A careful EDT analysis of Sleeping Beauty must specify exactly what propositions are being conditioned on, what betting policies are available, and how utility is assigned across awakenings.

---

## 13. When EDT and CDT agree

It is worth emphasizing that EDT and CDT often agree. If an action affects an outcome only through its causal consequences, and if the action is not correlated with hidden causes of the outcome, then

\[
P(O=o_j\mid A=a)\approx P(O=o_j\mid \operatorname{do}(A=a)).
\]

For example, if you are deciding whether to flip a light switch, and there is no predictor or correlated agent involved, conditioning on flipping the switch and intervening to flip the switch lead to the same practical recommendation. The theories diverge in philosophically interesting cases precisely because those cases are designed to contain nonstandard dependencies.

Thus EDT should not be thought of as a theory that ignores causation. It simply does not restrict decision-relevant probabilities to causal or interventional probabilities. It uses the agent’s full conditional probabilities.

---

## 14. Conclusion

Evidential decision theory evaluates actions by conditional expected utility:

\[
V(a)=\sum_j P(O_j\mid a)D(O_j).
\]

It recommends the action or policy that would be the best news. In Newcomb’s problem, it one-boxes; in a twin prisoner’s dilemma, it cooperates. It treats predictions, common causes, and algorithmic correlations as decision-relevant because they affect the conditional probability of good outcomes.

The theory is mathematically simple but philosophically controversial. Its central question is not “What will this action cause?” but “What does this action indicate?” If one accepts that rational choice can depend on evidential significance as well as causal efficacy, EDT provides a precise and usable decision rule. If one insists that rational choice must track only causal consequences, EDT will seem like an irrational policy of managing the news.

For practical use, the key tasks are to specify the actions or policies, define outcomes and utilities, build a coherent probability model including all relevant dependencies, and compute conditional expected utilities. Where probabilities are uncertain or actions have zero prior probability, EDT may need regularization or policy-level analysis. These operational details are not fully settled by the source, but they can be handled cautiously by treating EDT as a rule over well-specified probabilistic models of the decision problem.

---

## References

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge University Press.

Conitzer, Vincent. 2015. “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192 (9): 2887–2899.

Gibbard, Allan, and William L. Harper. 1976. *Counterfactuals and Two Kinds of Expected Utility*.

Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. 2021. “The Evidentialist’s Wager.”

Wikipedia contributors. 2026. “Evidential Decision Theory.” *Wikipedia*, revision 1373679688.