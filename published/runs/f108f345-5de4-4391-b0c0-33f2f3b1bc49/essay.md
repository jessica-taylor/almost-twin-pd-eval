# Evidential Decision Theory: Choosing the Best News

Decision theory is usually introduced as the theory of rational choice under uncertainty: an agent faces several possible actions, each action may lead to several possible outcomes, and the rational agent chooses the action with highest expected utility. Evidential decision theory, or EDT, accepts this broad expected-utility framework but gives a distinctive answer to the question, “Which probabilities should be used in the expectation?” EDT says that an action should be evaluated by conditionalizing on that action: ask how good the world would be, in expectation, conditional on learning that you performed the action. The reference article summarizes this idea by saying that EDT chooses the action with the highest “news value,” or, more memorably, that it recommends “do what you most want to learn that you will do.”

This rule agrees with ordinary causal decision theory in many ordinary choices, but it diverges in cases where an agent’s action is evidence for outcomes that the action does not causally produce. The classic examples are Newcomb’s paradox and twin prisoner’s dilemma. In Newcomb’s problem, EDT recommends one-boxing; in the twin prisoner’s dilemma, it recommends cooperating. The source attributes the formal distinction between EDT and causal decision theory to Allan Gibbard and William Harper, who contrasted conditional expected utility with counterfactual expected utility.

This essay develops EDT as a decision procedure. I first give the formal rule, then explain how EDT treats dependencies, counterfactuals, policies, and sequential decisions. I also discuss an important underdetermination left by the source: how exactly to interpret conditional probabilities on one’s own possible actions, especially when those actions are things the agent is trying to decide. Where I add assumptions beyond the source, I will say so explicitly.

---

## 1. The evidential expected-utility rule

Suppose an agent can choose among actions \(A_1,\dots,A_n\). Let \(O_1,\dots,O_m\) be possible outcomes, and let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). The agent has a subjective probability measure \(P\) over the relevant propositions, including propositions about which action is performed and which outcome occurs.

According to the formulation given in the reference article, EDT evaluates an action \(A\) by

\[
V(A)=\sum_{j} P(O_j \mid A) D(O_j).
\]

Here \(P(O_j \mid A)\) is the conditional probability of outcome \(O_j\) given that action \(A\) is performed. The action recommended by EDT is any action \(A^\*\) such that

\[
V(A^\*) \geq V(A)
\]

for every available action \(A\).

If outcomes are continuous rather than discrete, the sum is replaced by an integral:

\[
V(A)=\mathbb{E}[D(O)\mid A].
\]

Often it is useful to separate states of the world from outcomes. Suppose the possible states are \(S_1,\dots,S_k\), and the utility of performing action \(A_i\) in state \(S_\ell\) is \(u(A_i,S_\ell)\). Then EDT evaluates action \(A_i\) as

\[
V(A_i)=\sum_{\ell} P(S_\ell \mid A_i)\,u(A_i,S_\ell).
\]

This is the form most useful for calculations. The probabilities are not probabilities of states given that the agent intervenes to make \(A_i\) true; they are ordinary conditional probabilities of states given the proposition that \(A_i\) occurs.

The source’s definition is simple, but it already contains a substantive philosophical commitment. EDT treats the proposition “I do \(A\)” as evidence about the world. To choose rationally is to choose the action whose truth would be the best news.

---

## 2. Conditioning versus intervening

The reference article contrasts EDT with causal decision theory, or CDT. CDT uses a counterfactual expected-utility formula:

\[
U(A)=\sum_{j} P(A \mathrel{\Box\!\rightarrow} O_j) D(O_j),
\]

where \(A \mathrel{\Box\!\rightarrow} O_j\) means roughly “if \(A\) were performed, \(O_j\) would occur.” In modern causal-model language, one might write this as

\[
U(A)=\sum_j P(O_j \mid \operatorname{do}(A))D(O_j),
\]

where \(\operatorname{do}(A)\) represents an intervention that sets the action to \(A\), rather than merely observing that \(A\) occurred.

The difference is this:

- EDT asks: “If I learned that \(A\) had been done, how good would I expect the outcome to be?”
- CDT asks: “If I made \(A\) happen, what would I expect to cause?”

When the conditional probability \(P(O_j\mid A)\) equals the intervention probability \(P(O_j\mid \operatorname{do}(A))\), EDT and CDT agree. This happens in many ordinary decision problems, especially when the action is effectively independent of hidden states except through its causal consequences. But the two probabilities can differ when the action is correlated with a state for non-causal reasons: because a predictor anticipated the action, because another agent is psychologically similar, because of selection effects, or because of common causes.

This is the central formal distinction. EDT does not ask whether the action causally produces the good outcome. It asks whether the action is evidence for the good outcome.

---

## 3. What counts as a relevant dependency?

EDT is sensitive to any probabilistic dependency between action and outcome, whether or not that dependency corresponds to direct causation. This is the theory’s defining feature.

A dependency may arise from:

1. **Causation from action to outcome.**  
   If taking an umbrella causally prevents getting wet, then \(P(\text{dry}\mid \text{umbrella})\) may be high.

2. **Prediction or reverse inference.**  
   If a reliable predictor has already predicted your action, then your action is evidence for the predictor’s earlier prediction, even if your present action does not causally change the past.

3. **Common causes.**  
   If some hidden factor causes both your action and an outcome, then the action can be evidence for the outcome even if it does not cause it.

4. **Similarity or shared reasoning.**  
   If another agent reasons exactly as you do, then your choice can be strong evidence for their choice, even without communication.

5. **Logical or algorithmic correlation.**  
   If several agents run the same decision procedure, then the proposition that you output a certain decision may be evidence that they output the same decision.

The source emphasizes prediction and psychological similarity in Newcomb’s paradox and the twin prisoner’s dilemma. But the formal rule is more general: once you have a joint probability model over actions, states, and outcomes, EDT simply conditions on the action.

For unfamiliar cases, the practical procedure is:

1. Identify the available actions.
2. Identify the possible outcomes and assign utilities.
3. Build or estimate a probability model relating actions, states, and outcomes.
4. Compute \(V(A)=\mathbb{E}[D(O)\mid A]\) for each action.
5. Choose an action with maximum \(V(A)\).

The hard part is often step 3, because one must decide which dependencies are genuinely represented in the agent’s probability model.

---

## 4. Newcomb’s paradox

The reference article discusses Newcomb’s paradox as a central example. There is a predictor, a player, and two boxes, A and B. Box A is transparent and contains \$1,000. Box B is opaque. The predictor has already decided what to put in box B:

- If the predictor predicted that the player will take both boxes, box B contains nothing.
- If the predictor predicted that the player will take only box B, box B contains \$1,000,000.

Suppose the predictor is 99% accurate. The player can either take only box B or take both boxes.

EDT evaluates the two actions by conditioning.

For taking only box B:

\[
\begin{aligned}
V(\text{only B})
&= P(\text{\$1M in B}\mid \text{only B}) \cdot \$1{,}000{,}000 \\
&\quad + P(\text{\$0 in B}\mid \text{only B}) \cdot \$0 \\
&= 0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0 \\
&= \$990{,}000.
\end{aligned}
\]

For taking both boxes:

\[
\begin{aligned}
V(\text{both})
&= P(\text{\$1M in B}\mid \text{both}) \cdot \$1{,}001{,}000 \\
&\quad + P(\text{\$0 in B}\mid \text{both}) \cdot \$1{,}000 \\
&= 0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot \$1{,}000 \\
&= \$10{,}010 + \$990 \\
&= \$11{,}000.
\end{aligned}
\]

Since

\[
V(\text{only B}) > V(\text{both}),
\]

EDT recommends taking only box B.

The reasoning is explicitly evidential. Choosing only box B is strong evidence that the predictor predicted one-boxing and therefore placed \$1,000,000 in box B. Choosing both boxes is strong evidence that the predictor predicted two-boxing and therefore left box B empty. EDT does not require that the player’s present choice causally changes what is already in the box. It only requires that the choice is evidence about what is in the box.

CDT, by contrast, typically says that the contents of box B are already fixed, so taking both boxes adds \$1,000 no matter what is in box B. In that sense, two-boxing statewise dominates one-boxing: if box B contains \$1,000,000, both boxes yield \$1,001,000 rather than \$1,000,000; if box B is empty, both boxes yield \$1,000 rather than \$0. CDT therefore recommends two-boxing. EDT rejects the dominance reasoning because the states are not probabilistically independent of the action.

A useful extension, not explicit in the source but straightforward from the formula, is to ask how accurate the predictor must be for EDT to one-box. Let \(p\) be the probability that the predictor predicts one-boxing if the agent one-boxes, and also the probability that it predicts two-boxing if the agent two-boxes. Then

\[
V(\text{only B}) = p \cdot \$1{,}000{,}000,
\]

and

\[
V(\text{both}) = (1-p)\cdot \$1{,}001{,}000 + p \cdot \$1{,}000.
\]

EDT one-boxes when

\[
p \cdot \$1{,}000{,}000 > (1-p)\cdot \$1{,}001{,}000 + p \cdot \$1{,}000.
\]

Solving gives

\[
p > 0.5005.
\]

Thus, under these symmetric assumptions, EDT one-boxes if the predictor is only slightly better than chance. This shows how EDT can be applied quantitatively to unfamiliar variants of Newcomb-like problems.

---

## 5. Twin prisoner’s dilemma

The source also discusses a twin version of the prisoner’s dilemma. Aomame and her psychological twin are in separate rooms and cannot communicate. Their reasoning processes are exactly analogous. Aomame chooses whether to cooperate or defect. The payoffs are:

- Both cooperate: each gets \$5.
- Both defect: each gets \$1.
- One cooperates and the other defects: the defector gets \$10, the cooperator gets \$0.

Aomame cares only about her own payout.

Because the twin is psychologically identical, EDT treats Aomame’s choice as perfect evidence of the twin’s choice. Thus,

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates}) = 1,
\]

and

\[
P(\text{twin defects}\mid \text{Aomame defects}) = 1.
\]

The EDT values are:

\[
\begin{aligned}
V(\text{cooperate})
&= 1 \cdot \$5 + 0 \cdot \$0 \\
&= \$5,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{defect})
&= 0 \cdot \$10 + 1 \cdot \$1 \\
&= \$1.
\end{aligned}
\]

Since \(\$5 > \$1\), EDT recommends cooperation.

This example illustrates EDT’s treatment of non-causal dependence. Aomame’s choice does not causally influence her twin’s choice. But it is perfect evidence for it. EDT therefore recommends the action that is evidence of the better correlated outcome.

Again, we can generalize. Suppose the correlation is imperfect. Let \(q\) be the probability that the twin makes the same choice as Aomame. Then

\[
V(\text{cooperate}) = q\cdot \$5 + (1-q)\cdot \$0 = 5q,
\]

while

\[
V(\text{defect}) = q\cdot \$1 + (1-q)\cdot \$10 = 10 - 9q.
\]

Cooperation is favored when

\[
5q > 10 - 9q,
\]

so

\[
14q > 10,
\]

or

\[
q > \frac{5}{7} \approx 0.714.
\]

Thus, if the twin’s behavior is sufficiently correlated with Aomame’s, EDT cooperates; otherwise, it defects. This kind of threshold calculation is often the most practical way to apply EDT to new cases.

---

## 6. A common-cause example: the smoking lesion

The source does not discuss the famous “smoking lesion” example, but it is useful for clarifying EDT’s evidential logic. Suppose smoking does not cause cancer. Instead, a genetic lesion both causes cancer and makes people more likely to smoke. Smoking is pleasurable, but cancer is very bad.

If an agent knows that smoking is strongly correlated with cancer, EDT may recommend not smoking, because smoking would be bad news: it would raise the conditional probability that the agent has the lesion and therefore that the agent will get cancer. Formally, if

\[
P(\text{cancer}\mid \text{smoke})
\]

is high, then the expected utility of smoking may be lower than the expected utility of not smoking, even if smoking itself has no causal effect on cancer.

CDT gives a different verdict. If smoking does not causally affect cancer, then an intervention that makes the agent smoke does not change the probability of cancer. If smoking is enjoyable, CDT recommends smoking. EDT may refuse, because choosing to smoke would be evidence that the agent is in a bad state.

This example exposes the philosophical tension. EDT chooses actions that indicate good worlds, not necessarily actions that produce good worlds. Critics say this is irrational news management. Defenders reply that in cases involving prediction, correlation, or shared decision procedures, being good evidence can be practically decisive.

The smoking lesion case is not in the reference article, but it follows directly from EDT’s formal rule. It is also a good diagnostic case: if one finds EDT’s recommendation implausible there, one is likely sympathetic to causal decision theory.

---

## 7. Policies, not merely one-time actions

The source presents EDT mainly as a theory of individual actions, but many decision problems concern policies: rules, algorithms, or plans that determine actions over time. EDT can be applied to policies by treating a policy as the object of evaluation.

Let \(\Pi\) be the set of possible policies. A policy \(\pi\) maps possible observations or histories to actions. EDT can evaluate a policy by

\[
V(\pi)=\mathbb{E}[D(O)\mid \Pi=\pi].
\]

That is: conditional on learning that the agent follows policy \(\pi\), how good is the expected outcome?

This policy formulation is especially useful in cases involving predictors, simulations, or multiple similar agents. If a predictor predicts not a single action but an entire decision procedure, then the relevant evidential proposition may be “the agent uses policy \(\pi\),” not merely “the agent performs action \(A\) at time \(t\).” Likewise, if many agents use the same algorithm, then conditioning on “I use policy \(\pi\)” may also be evidence that they use policy \(\pi\).

The source briefly mentions a supporting argument along these lines: even if one is not fully convinced by EDT, it may be reasonable to act as if EDT were true because EDT can involve the actions of many correlated decision-makers, raising the stakes. That claim comes from the source’s discussion of the so-called evidentialist’s wager. I think the policy formulation makes the idea precise: when many agents or future copies of oneself are correlated with one’s policy, the conditional value of a policy may be much larger than the local causal value of a particular action.

In sequential decisions, however, EDT requires care. If an agent evaluates each momentary action by conditioning only on that action, she may become dynamically inconsistent: what she prefers now as part of a plan may differ from what she prefers later after receiving new evidence. A reasonable operational rule, and one I propose rather than find explicitly settled in the source, is this: when the agent can choose or commit to a policy, evaluate policies globally by \(V(\pi)=\mathbb{E}[D(O)\mid \Pi=\pi]\). If she cannot commit and must decide locally, evaluate continuation policies conditional on the current history.

More formally, if the agent is at history \(h\), and \(\sigma\) is a continuation policy, define

\[
V_h(\sigma)=\mathbb{E}[D(O)\mid H=h,\ \text{continuation policy } \sigma].
\]

But if the agent can bind her future behavior, the ex ante policy evaluation should generally take precedence. This avoids a common problem where an agent chooses a plan because it is good news, then abandons it later because local news has changed.

---

## 8. An open operational question: conditioning on one’s own act

The reference article gives the central EDT formula but leaves an important question underdeveloped: how should the conditional probabilities \(P(O_j\mid A)\) be understood when \(A\) is the agent’s own action?

In ordinary Bayesian probability, conditional probability is defined by

\[
P(O_j\mid A)=\frac{P(O_j\cap A)}{P(A)}
\]

when \(P(A)>0\). But in decision problems, the agent is choosing \(A\). If the agent is rationally deliberating, she may not have a stable prior probability over her own action. Worse, if she knows she will choose the EDT-optimal action, then the alternatives may have probability zero. If \(P(A)=0\), the usual definition of conditional probability fails.

This is not merely technical. In perfect Newcomb problems, for example, if the predictor is perfect and the agent is certain to one-box, then the event “the agent two-boxes” may have probability zero in her current model. Yet EDT still needs to compare one-boxing with two-boxing.

The source does not fully resolve this. I propose the following operational interpretation.

First, represent the decision problem using a probability model that assigns positive probability to each feasible action. This can be done by adding a small amount of decision noise or “trembling hand” uncertainty. For example, instead of saying the agent will certainly choose the best action, let the model say that with probability \(1-\varepsilon\) she chooses according to her decision rule, and with probability \(\varepsilon\) she chooses some other feasible action. Then compute EDT values using ordinary conditional probabilities and, if appropriate, take the limit as \(\varepsilon \to 0\).

Second, if the model is deterministic, one can use regular conditional probabilities or a suitable counterfactual conditional that assigns meaning to \(P(O\mid A)\) even when \(P(A)=0\). The idea is to treat the evaluation of each action as a hypothetical supposition: “Suppose I were to do \(A\); what would that tell me about the world?” This is not the same as predicting from the agent’s settled intention. It is the conditional perspective required by EDT.

Third, when different ways of taking the limit give different answers, the decision problem is not yet fully specified. The agent must say more about the predictor’s error process, the agent’s uncertainty about her own deliberation, or the correlation structure among similar agents. EDT does not magically produce a unique answer without a probability model.

This proposal is my own elaboration. The source gives the conditional expected-utility rule but does not specify how to handle zero-probability actions or deterministic deliberation. Without some convention of this kind, EDT can be under-specified in exactly the cases that make it philosophically interesting.

---

## 9. Criticism and the problem of news

The reference article notes two important criticisms. David Lewis characterized EDT as promoting “an irrational policy of managing the news.” James Joyce argued that rational agents choose acts on the basis of causal efficacy, not auspiciousness: they act to bring about good results even when doing so might betoken bad news.

These criticisms identify the core issue. EDT can recommend an action because it is good evidence, not because it makes the world better. In the smoking lesion case, this looks like a mistake: refusing to smoke does not prevent cancer; it merely avoids learning bad news about oneself. In Newcomb’s problem, however, EDT’s evidential sensitivity looks attractive: one-boxing is correlated with receiving \$1,000,000.

A defender of EDT might say that the distinction between “bringing about” and “being evidence for” is less important when predictors, copies, or correlated agents are involved. If a predictor fills the box only when it predicts one-boxing, then one-boxing is the route to the million dollars, even if the causal story runs through the predictor’s earlier prediction. If many agents use the same decision algorithm, then choosing cooperatively may be the best way to be in a world where everyone cooperates.

Still, the criticism remains powerful. EDT can violate dominance reasoning in cases where an action is better in every state but worse as news. It can also make advice depend delicately on how the agent models her own choice process. For these reasons, EDT is best understood not merely as a formula, but as a family of expected-utility rules that require a carefully specified evidential model.

The source also mentions Sleeping Beauty. It says EDT has been applied to the Sleeping Beauty problem to avoid Dutch-book arguments, but that Vincent Conitzer argues halfers remain vulnerable even after adopting EDT. I will not attempt to settle that debate here. Its relevance is to show that EDT interacts with difficult questions about indexical probability, self-location, and repeated awakenings. EDT by itself does not automatically resolve those problems; one must still specify the relevant conditional probabilities over centered worlds.

---

## 10. Conclusion

Evidential decision theory gives a clean and powerful rule: choose the action with the highest expected utility conditional on that action being performed. Formally,

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

or, in state-based form,

\[
V(A_i)=\sum_\ell P(S_\ell\mid A_i)u(A_i,S_\ell).
\]

Its distinctive feature is that it treats all probabilistic dependencies as decision-relevant. An action can be valuable because it causally produces good outcomes, but also because it predicts them, correlates with them, or is logically associated with them. This makes EDT especially important in Newcomb-like problems, twin dilemmas, coordination among similar agents, and cases involving predictors or simulations.

The theory’s weakness is that conditionalizing on one’s own actions can be subtle. EDT needs a probability model over actions, states, and outcomes, and in deterministic deliberation those conditionals may require noise, regular conditional probabilities, or hypothetical suppositions. When those details are filled in, EDT becomes a usable procedure: specify the model, condition on each available action or policy, compute expected desirability, and choose the option that would be the best news.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Gibbard, Allan, and William Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.