# 015_edt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00007

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f108f345-5de4-4391-b0c0-33f2f3b1bc49/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f108f345-5de4-4391-b0c0-33f2f3b1bc49/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request. Need produce final essay ~2400-3000 words. Need explain EDT, formal definitions, equations, examples, how evaluates actions/policies, dependencies/counterfactuals, open questions, operational interpretation, distinguish source claims vs own proposals. Need likely write substantive mathematical essay. Need be careful word count approximate 2400-3000. Need include references maybe brief. Need no appendices. Need maybe mention source Wikipedia revision. Need likely target around 2700 words. Need think deeply.

Need plan essay.

User: "Researcher — mathematical essay / blog post". Write coherent account of EDT and apply to decision problems. Target 2,400-3,000 words including references. Use examples. Explain evaluating alternative actions/policies and dependencies/counterfactuals. Where source leaves important question open, explain uncertainty and if reasonable operational interpretation available, develop/justify. Distinguish source claims from additional assumptions/proposals. Finish brief conclusion.

Need probably produce essay with title, sections maybe. Word count. Need maybe include math formulas. We need ensure not too short. Let's outline.

Title: Evidential Decision Theory: Choosing the Best News About Yourself.

Intro: decision theory under uncertainty, acts, states, outcomes, utility. EDT says maximize expected utility conditional on act as evidence. "do what you most want to learn that you will do". Contrast CDT. Source: Gibbard & Harper formula V(A)=sum P(O_j|A)D(O_j), CDT U(A)=sum P(A counterfactual -> O_j)D(O_j). Need explain conditional probability vs counterfactual/intervention.

Formal setup: finite set of acts A, possible outcomes O. Agent has probability measure P over relevant propositions including acts and states/outcomes. Desirability D/outcome utility. EDT value V(A)=E[D(O)|A]=sum_o P(O=o|A)D(o). Choose argmax. If acts not exclusive? Usually partition. Need mention conditional on event A. If P(A)=0? Regular conditional probabilities or conditional events; maybe open. Policies: for sequential decisions, evaluate policies conditional on policy being adopted? Need discuss. EDT can apply to policies as actions; conditional probabilities of outcomes given policy. In dynamic cases, may condition on entire policy or current action? Need discuss open, propose evaluate policies by conditional expected utility given policy, with possible commitment to future actions; if conditional on partial action can lead to dynamic inconsistency. Need mention evidential update vs intervention.

Dependencies: EDT cares about all probabilistic dependencies between act and outcomes, whether causal, common cause, correlation, logical/evidential. Examples: Newcomb predictor (common cause? prediction causes? no causal influence from act to box, but correlation due to predictor). Twin prisoner's dilemma (psychological twin, correlated decisions). Smoking lesion? Maybe classic problem: smoking and lung cancer due to lesion; EDT may recommend not smoking if smoking evidence of lesion even if no causal effect. Could add example to illustrate. Need be careful source did not mention smoking lesion, but can include as own explanatory addition? It says additional assumptions/proposals. We can introduce as standard example not in source; label as explanatory addition. It helps dependencies/counterfactuals. Need perhaps mention "auspiciousness" critique.

Counterfactuals: EDT doesn't use interventionist counterfactuals; its "counterfactual" is conditionalization: suppose I learn A occurred, update by conditioning. But if actions are chosen based on prior probabilities, issue of decision maker's own action: conditional probability can be undefined if agent is certain to choose some action? Need discuss "deliberation" problem: if agent knows they will choose A, P(O|A) maybe trivial. EDT uses deliberational probabilities, maybe not fully settled by source. Need operational interpretation: use pre-deliberation or hypothetical conditional credences; or use a probabilistic model of the decision process as a random variable / policy selection with small exploration noise. Need justify. This is important open question. Source leaves open: how to set P(O|A) when act is under agent's control? Need propose: construct a joint distribution over acts, states, outcomes representing epistemic state before choice; condition on act propositions. If deterministic chooser, approximate with small uncertainty about which act will be chosen or use Jeffrey conditionalization over act variable. Or use Popper functions/regular conditional probabilities. Need distinguish.

Need maybe discuss policies and multi-act: If policies are algorithms mapping observations to actions, EDT value is expected utility conditional on implementing policy π. In AI terms, V(π)=E[U|do? no, |π]. Need evaluate by sampling possible worlds where agent's policy is π? But conditional, not intervention. If multiple agents with same algorithm, conditioning on policy affects beliefs about them. Could mention source's supporting argument: because EDT involves correlated decision-makers, stakes higher; "Evidentialist's Wager". Need maybe mention but not overdo.

Examples: Newcomb calculation; twin PD; maybe medical screening/Smoking lesion; maybe voting? Need not too many. Need likely include two source examples plus one new to clarify. Need maybe show equations.

Need discuss when EDT and CDT agree: if act is probabilistically independent of states conditional on causal structure? Actually if P(O|A)=P(A □→ O). In many randomized decisions or where action only affects outcome causally and no common causes, same. If actions are chosen independent of relevant states, conditioning equals intervention. More formally if act is exogenous/randomized with respect to states. Need mention.

Need discuss criticisms: Lewis "managing the news", Joyce causal efficacy. EDT may choose action that is good evidence but doesn't make outcome better. Example smoking lesion: If smoking is evidence for lesion causing cancer, EDT avoids smoking even if smoking doesn't cause cancer. But if one can choose to smoke as evidence? Could discuss "why ain'cha rich?" maybe EDT one-boxes and gets million, but CDT two-boxes and less. However CDT can become EDT? Need maybe not too much.

Need discuss policy and conditional probabilities with known deterministic choice: If agent is rational and knows EDT, then they know they will choose argmax. This can make P(A)=1 for chosen act and conditionals collapse? Example Newcomb: If agent knows they'll one-box, predictor predicted one-box; conditional on two-box maybe probability zero. Need use probabilities of predictor errors or tie-breaking to keep support. Source uses 99% accuracy. In deterministic perfect predictor, conditioning on impossible act problematic. Need propose: use ε-noise or consider nearest possible worlds where act occurs. This is our operational interpretation. Need develop.

Potential open question: EDT and superrationality, logical dependence. Source says twin reasoning processes exactly analogous; EDT recommends cooperate with probability 1. But if not exact, use conditional probability. For logical omniscience? Need maybe discuss correlation due to shared source code. EDT treats dependencies as evidential, not requiring causal link. But how to assign probabilities to logical correlations? Source leaves open. Could propose use ordinary Bayesian probability over uncertain propositions; if perfect logical entailment known, probabilities 0/1; if uncertain, estimate correlation.

Need maybe discuss "news value" definition: news value of A is expected desirability of outcome conditional on A. Need maybe define desirability of outcomes; maybe Jeffrey's desiderability? Source uses D(O_j). Need maybe note if outcomes include side effects or states? In standard decision matrix: acts A_i, states S_k, outcomes O_{ik}, utility u(A_i,S_k). Then EDT value V(A_i)=∑_k P(S_k | A_i) u(A_i,S_k) if outcomes determined by act+state. More precise: V(A)=∑_s P(S=s|A) U(A,s). This is useful. In Newcomb, state = predictor's prediction/box content; outcome payoff. In twin, state = twin's action.

Need ensure mathematical definitions: Let (Ω,F,P) probability space. Acts are events A_i forming partition. Outcome random variable O: Ω→𝒪. Utility u:𝒪→ℝ (or D). EDT chooses A*∈argmax_i E[u(O)|A_i]. If continuous: integral. For policies π: V(π)=E[u(O)|Π=π] where Π is policy variable; if policy maps info to actions, condition on event that agent implements π. If observations, evaluate conditional on policy rather than local action to avoid dynamic inconsistency. Maybe formulate as: for sequential problem, a policy π determines actions at histories; EDT evaluates V(π)=∑_ω P(ω|π) u(ω), choose π. At a particular history h, if reconsidering, one can evaluate continuation policies conditional on h and π_h? Need maybe mention.

Need discuss relevant dependencies: Conditional probability captures evidential links. If A is correlated with state S due to common cause, prediction, twin, selection, etc., P(S|A) changes. EDT chooses act that makes good states likely as news. CDT uses do(A) or closest worlds: P(S | do(A)) or counterfactual. If A does not causally affect S, CDT says P(S|do(A))=P(S) (maybe) while EDT uses P(S|A). Need formal contrast: CDT U(A)=∑_s P(S=s | do(A)) u(A,s) or counterfactual. Source uses P(A□→O). Need maybe explain.

Need maybe discuss "what if I can manipulate news?" Example: if I hire a publicist to announce I'll do A regardless? EDT? Hmm maybe not.

Need word count. Need produce ~2600 words. Let's estimate. We can write maybe 2500-2800. Need maybe include references at end. Need count? Let's draft in mind.

Structure:
1. Title + intro (200-300 words)
2. Formal framework (500-600)
3. Dependencies and counterfactuals (400-500)
4. Examples: Newcomb (350), twin PD (250), lesion/voting maybe (300)
5. Policies, sequential decisions, operational issues (500)
6. Criticism and relation to CDT (250)
7. Conclusion + references (200)
Total maybe 2600.

Need be careful with citations: Source references can be included briefly. Maybe "Wikipedia contributors (2026)"? The source article. But essay can cite Ahmed 2021, Gibbard & Harper 1978? Source says 1976 paper. Joyce 1999, Lewis 1981, Conitzer 2015, MacAskill et al. 2021. Need maybe not lengthy bibliography. Need include references list maybe 6 entries. Word count includes references; keep concise.

Need ensure no unsupported source claims? Distinguish: Source says EDT formula, contrast CDT, Newcomb one-box, twin cooperate, Sleeping Beauty Dutch book debate, supporting argument correlated decision-makers, criticisms. I can mention Sleeping Beauty briefly? Could include but not necessary? The prompt says apply EDT to decision problems, central definitions. Maybe mention Sleeping Beauty as open application with uncertainty; but could be tangential. Maybe include a paragraph on "open questions" including Sleeping Beauty and conditional probability zero. Need source leaves important question open: how conditional probabilities for own acts? Need focus on that. Could mention Sleeping Beauty: source says EDT applied to avoid Dutch books but Conitzer argues halfers still affected. We can say not central; indexical uncertainty complicates. But not necessary? Maybe include to show source open? However prompt asks where source leaves important question open. The source doesn't explain how to operationalize conditionals for acts with probability zero or policy evaluation. That is better.

Need maybe discuss "news value" and "do what you most want to learn that you will do." Good quote. Need explain.

Need write as mathematical essay. Use LaTeX style. Final answer should be text only with formulas. Need perhaps mention source claims with phrases "According to the reference article..." and "I add...".

Need consider if formula uses D(O_j) desirability. Need maybe define D vs U. Use V for EDT. CDT uses U maybe. Need avoid confusion with utility function. Use D for desirability.

Need maybe discuss decision under acts with non-zero probability. In Bayesian decision theory, acts often chosen, not probabilistic; EDT conditioning on act event is unusual because acts are not states. Need address.

Let's deep dive into EDT theory for precision.

Evidential decision theory: associated with Jeffrey (1965?) and later. It treats acts as propositions. The desirability of a proposition is expected utility conditional on it. For act A, V(A)=∑_j P(O_j|A)D(O_j). Choose act maximizing. In Jeffrey's framework, desires are assigned to propositions, not states. The source uses Gibbard & Harper. Need maybe mention Richard Jeffrey? Source not mention, but historically EDT from Jeffrey? Could include? If not source, label as additional historical note? Maybe avoid if not needed. But mathematically, Jeffrey's expected utility: V(A)=∑_s P(S|A)U(A,S). We can mention "Often associated with Jeffrey's framework" as my addition. Need not cite.

Potential issue: If act A itself has direct utility? Maybe outcome includes act? In EDT, if you desire doing A for its own sake, include in outcome/desirability. Usually D(O_j) outcomes only.

Need maybe define conditional probabilities: P(O|A)=P(O∧A)/P(A) if P(A)>0. If P(A)=0, need regular conditional probabilities or limits. This is operational.

Need discuss partition: acts must be mutually exclusive and exhaustive options. If actions overlap, need refine into distinct possible choices. For policies, partition of policy implementations.

Need examples details:
Newcomb: define predictor accuracy p=0.99. Let S=1M if predictor predicted one-box, 0 if predicted two-box. Prior? If predictor accuracy symmetric, P(predict one|one)=0.99 etc. The calculation in source assumes conditional probabilities directly. If prior not specified, but predictor 99% accuracy could mean P(pred one | one)=0.99 and P(pred two | two)=0.99. Then V(one)=990k, V(two)=? Need source calculation: P(1M|both)=0.01. Then payoff both if 1M: 1,001,000; if nothing: 1000. 0.01*1,001,000 +0.99*1,000 = 10,010+990=11,000. Yes. Need maybe note if predictor less reliable threshold? EDT one-box if p high enough. Could compute threshold? Maybe useful. Let p = P(predict one|one) = P(predict two|two). Then V_one = p*1,000,000. V_two = (1-p? actually P(1M|two)=1-p? If symmetric yes) *1,001,000 + p? Wait if p=accuracy; P(1M|two)=prob predictor predicted one given agent two-boxes = error rate = 1-p. So V_two=(1-p)*1,001,000 + p*1000. Compare p*1e6 > (1-p)*1,001,000 + p*1,000. Solve: 1,000,000p > 1,001,000 -1,001,000p +1,000p =1,001,000 -1,000,000p. So 2,000,000p >1,001,000 => p>0.5005. So even barely better than chance one-box. Could mention to show application. Need ensure not too long. This is our addition perhaps.

Twin PD: If perfect twin, conditional probabilities 1. If imperfect correlation q, formula: V(C)=q*5+(1-q)*0? Wait if Aomame cooperates, probability twin cooperates maybe q; if defects, probability twin defects q. With symmetric q. Payoffs: if both cooperate 5; if I cooperate, twin defects 0; if I defect, twin cooperate 10; if both defect 1. V(C)=q*5+(1-q)*0=5q. V(D)=q*1+(1-q)*10? Wait if Aomame defects, probability twin defects q => payoff 1, twin cooperates 1-q => payoff 10. V(D)=q*1+(1-q)*10 =10-9q. Cooperate if 5q>10-9q =>14q>10=>q>5/7≈0.714. Source with q=1 cooperate. Could mention threshold to show how to decide unfamiliar cases. Good.

Smoking lesion: Let lesion L causes cancer C and smoking S? Actually classic: smoking is correlated with cancer because of genetic lesion, but smoking does not cause cancer. If agent desires health and likes smoking. EDT: V(smoke)=P(cancer|smoke)*u(smoke,cancer)+P(no cancer|smoke)*u(smoke,no cancer). If P(cancer|smoke) high, maybe don't smoke, even if intervention do(smoke) doesn't change cancer. This shows EDT can recommend avoiding harmless bad evidence. Need perhaps note if smoking itself gives small utility, compare. This example not in source; state as addition. It highlights criticism "managing news".

Could also use "toxin puzzle"? Not necessary.

Policy evaluation: In Newcomb, one-boxing as policy. If predictor predicts policy, conditioning on policy. In sequential decisions, e.g., Newcomb with transparent box? Maybe not. Need talk about policies: Suppose agent can precommit to algorithm π. EDT value V(π)=∑_o P(O=o | Π=π)D(o). If multiple copies or simulations, conditioning on π gives evidence about other implementations. This captures superrationality. Source's supporting argument: EDT may take priority due to correlated decision-makers. Need maybe mention.

Dynamic inconsistency: EDT may choose an act now because it is good news, but later after receiving evidence may choose differently. Example? Maybe Smoking lesion? Or Newcomb? If one-boxer after seeing box? In sequential, if agent can make decisions at nodes, EDT's local conditioning may differ from policy conditioning. Need propose evaluate policies globally to maintain coherence. Source doesn't specify. Need develop: treat a policy as the object of choice; if agent can bind future selves, choose policy maximizing conditional expected utility. If no commitment, at each history h evaluate continuation policy conditional on h and the event that the overall policy reaches h? Need careful.

Could formulate: Let H be histories. A policy π maps h to action. The event Π=π is that the agent's decision procedure outputs π's actions at all relevant histories. EDT ex ante value V(π)=E[D(O)|Π=π]. If the agent finds herself at h, the conditional value of a continuation σ is E[D(O)|H=h, Π_{future}=σ, perhaps Π_{past} consistent]. But conditioning on H=h may itself be news; this can create time inconsistency. A reasonable operational rule: choose a policy ex ante and, unless new information changes the model, evaluate deviations by comparing the news value of the whole revised policy, not merely the local action. This is my proposal. Need justify: avoids exploiting self-knowledge and handles correlations with predictor.

Open question: If the agent is certain she will choose the optimal act, conditioning on non-optimal act has probability zero. But decision requires evaluating alternatives. Operational interpretation: maintain a small "trembling hand" probability or use counterfactual conditional with positive support. For each act, consider a hypothetical update as if the act were observed, not as a prediction from current deterministic intention. Mathematically, use regular conditional probabilities or Popper functions that assign P(O|A) even when P(A)=0. Or construct model with latent noise N: choice A=f(features,N), with N having full support; then condition on A. This gives well-defined values. Need distinguish from source. Source uses conditional probability but doesn't address zero-probability acts. This is important. Need maybe state: Without such a convention, EDT may be under-specified in deterministic deliberation. My proposal: use an explicit stochastic choice/model or regular conditional probabilities; results should be stable as noise→0 when possible.

Need also discuss "conditional probabilities vs interventions" more formally. Potential outcomes: For each world ω, outcome under act A? CDT uses U(A)=∑_ω P(ω)D(O_A(ω)), where O_A is outcome if intervene to A. EDT uses ∑_ω P(ω|A)D(O(ω))? Actually in worlds where A occurs, outcome is actual outcome. If acts not actually performed, need event A in possible worlds. Could define joint distribution over act variable and outcomes. For CDT, intervention do(A) sets act variable to A independent of its causes. For EDT, conditioning observes act variable. Need maybe use DAG language: If A ← common cause → O, conditioning opens collider? Actually common cause: S causes A and O? Predictor predicts A? In Newcomb, predictor's prediction P is caused by agent's disposition? The act A is not cause of prediction if prediction earlier? But there is correlation due to predictor. In causal graph, predictor's prediction may be caused by agent's future action via perfect prediction? Not standard. But evidential correlation enough.

Need perhaps discuss "dependency" includes logical/algorithmic correlation. In twin PD, if both use same decision algorithm, then event Aomame cooperates is evidence twin cooperates because same inputs. If they are not causally connected, EDT still conditions. Need mention.

Need mention "source leaves Sleeping Beauty debate unresolved". Maybe a paragraph: Source notes EDT applied to Sleeping Beauty to avoid Dutch books, but Conitzer disputes halfers. This shows EDT does not by itself settle indexical credence problems; one must specify conditional probabilities over centered worlds. But maybe this distracts. Could include in open questions: indexical/self-locating uncertainty. But target length.

Need maybe discuss "EDT and precommitment": In Newcomb, CDT agent may wish to become EDT agent or precommit to one-box, because predictor rewards EDT disposition. Source doesn't discuss but relevant. Could mention as implication. But careful not too long.

Need ensure final conclusion brief.

Need references: list maybe:
Ahmed (2021), Gibbard & Harper (1978/1976), Lewis (1981), Joyce (1999), MacAskill et al. (2021), Wikipedia source. Maybe Conitzer (2015). Keep short. Need maybe not include URLs? Could include source URL. The user supplied source; maybe reference it. Need maybe 5 references.

Need maybe word count. Let's draft with approximate counts. Need produce around 2600 words. Let's write in final. But before final, maybe calculate word count roughly? We can compose and maybe estimate. Need maybe include equations; word count may count words not formulas? Approx. Need target 2400-3000. I can produce about 2700 words. Need avoid too long. Let's draft carefully.

Potential essay:

Title: Evidential Decision Theory: Expected Utility as News

Intro:
Decision theory asks which option to choose when outcomes uncertain. Standard answer maximize expected utility. EDT says use conditional probabilities of outcomes given acts. It chooses action with highest news value. Quote. It contrasts CDT. In many cases same, but diverge in Newcomb/twin. This essay defines EDT, shows calculations, explains dependencies/counterfactuals, policies, and operational issues.

Formal framework:
Let options A_i partition, outcome random variable O, desirability D. Agent's epistemic state P. EDT value:
V(A_i)=E_P[D(O)|A_i]=∑_j P(O_j|A_i)D(O_j) if discrete; integral if continuous.
Choice rule: choose A* maximizing V. Equivalent with states: if outcome determined by act and state S, V(A_i)=∑_k P(S_k|A_i) u(A_i,S_k). The conditional is Bayesian update: if I learned A_i had been performed, how desirable would the world then appear? Need note P(A_i)>0; if not, need regular conditionals (later). Desirability D is outcome utility; if act has intrinsic value include it in O.

CDT contrast:
U_CDT(A_i)=∑_j P(A_i □→ O_j)D(O_j), or ∑_k P(S_k|do(A_i))u(A_i,S_k). The counterfactual/intervention probability asks what would happen if A_i were imposed, holding fixed independent causes. If conditionals equal intervention probabilities, theories agree. They diverge when act is evidence for outcomes it does not cause.

Dependencies:
EDT tracks probabilistic dependence, not causal dependence. If A correlated with state S via prediction, common cause, shared algorithm, selection effects, then P(S|A) ≠ P(S|do(A)). EDT uses former. This is source's point in Newcomb and twin. It treats "dependencies" broadly. For unfamiliar cases, build joint distribution over acts/states/outcomes and condition.

Example Newcomb:
Set up, predictor 99%. Payoffs. Calculations as source. One-box V=990k, two-box=11k. EDT one-box. Threshold p>0.5005 if symmetric accuracy. Explanation: one-boxing is evidence predictor filled box; two-boxing evidence empty. No causal influence needed; box already filled. CDT two-boxes because action doesn't change past prediction.

Example twin PD:
Aomame and twin. Perfect correlation. Calculations. Cooperate V=5, defect=1. If correlation q, formulas and threshold q>5/7. Shows how to apply with imperfect dependencies.

Example smoking lesion (my addition):
Smoking correlated with cancer due to lesion, not causal. EDT may recommend not smoking if health utility loss outweighs smoking pleasure. CDT would smoke if no causal effect and smoking enjoyable. This illustrates "news" and criticism. Need maybe specify: Let lesion raises cancer and smoking desire. P(cancer|smoke) high. EDT avoids smoking to avoid bad news. It may seem irrational if one can choose smoking without lesion? But EDT says your choice is evidence of lesion.

Counterfactuals and conditioning on own acts:
Source says EDT uses conditional probabilities but doesn't say where they come from when act is under agent's control. If agent is deliberating, she may assign probabilities to possible choices. But if she knows she will choose best act, alternatives may have zero probability. Need operational interpretation. I propose: model choice as a random variable with full support, reflecting uncertainty about final decision, implementation noise, or hypothetical supposition. Condition on each option as if receiving news. Use regular conditional probabilities or limiting ε-noise. In deterministic perfect predictor cases, assume predictor has small error or agent's choice has tremble; take limit. This yields stable recommendations. If different limits give different answers, problem under-specified. Need label as my proposal, not source.

Policies:
EDT can evaluate policies π, not just atomic acts. V(π)=E[D(O)|Π=π]. In sequential choices, choose policy with highest news value. This matters when future actions depend on information or when predictors predict policy. If only condition on current action, might ignore that choosing a policy changes evidence about future choices. A global policy rule is more coherent. If agent at intermediate history, condition on reaching history and evaluate continuation policies: V_h(σ)=E[D(O)|H=h, continuation=σ]. But beware dynamic inconsistency; if precommitment possible, use ex ante policy. This is my operational suggestion; source doesn't elaborate.

Correlated decision-makers:
Conditioning on policy also captures twin/simulations/multiple agents. If many agents use same algorithm, event I choose C is evidence they choose C. Source notes supporting argument: EDT may have higher stakes when many correlated decision-makers; acting as if EDT true may be reasonable. This is source claim, but exact weighting depends on model.

Criticisms:
Lewis: managing the news. Joyce: causal efficacy. EDT chooses auspicious acts. In smoking lesion, it avoids harmless pleasure due to bad news. In Newcomb, it gets rich but by choosing evidence. Critics say rational choice should change world, not merely indicate good world. Defenders reply in cases with predictors/correlations, being good evidence is how you get good outcomes; also if you can precommit, CDT wants to be EDT. Need balanced.

Sleeping Beauty maybe:
Source mentions application to Sleeping Beauty to avoid Dutch books, but Conitzer argues halfers still vulnerable. This indicates EDT alone doesn't solve indexical probability; needs account of centered conditional probabilities. Maybe include in open questions or skip. Need maybe mention in a short paragraph under open questions: "The reference also mentions Sleeping Beauty..." Good to show source leaves open. But may add length. We can include brief: The source notes EDT used in Sleeping Beauty to avoid Dutch books, but Conitzer disputes; thus EDT's application to self-locating uncertainty remains contested. Need not elaborate.

Conclusion:
EDT simple rule: maximize conditional expected utility. Its power is treating correlations as decision-relevant. Its difficulty is specifying conditionals for own actions and distinguishing news from control. For unfamiliar cases: specify options, outcomes, utilities, joint probability; condition; compare. If actions affect outcomes only causally and no confounding, agrees with CDT; when choices are evidence, EDT may diverge.

References: maybe list 6. Need maybe mention source revision. Keep concise.

Need word count. Let's estimate sections:
Title+intro 250
Formal 500
CDT contrast 250
Dependencies 200
Newcomb 350
Twin 250
Lesion 200
Counterfactual/operational 400
Policies 350
Criticism 250
Sleeping Beauty/open 100
Conclusion 150
References 150
Total 3200? Need trim. Maybe combine. Need 2400-3000. Let's target 2700. I'll be concise.

Need ensure mathematical definitions include continuous case maybe optional. Need maybe not too many equations? But equations count not words. Need readable.

Potential issue: User wants "approximately 2,400–3,000 words, including references and any other material." Need not exactly but close. If final too long maybe >3000. Let's aim 2700-2800. I can count approximate by paragraphs. Let's draft final with ~2600.

Let's produce final now? But need maybe think through exact wording and word count. I'll write carefully.

Draft:

# Evidential Decision Theory: Expected Utility as News

Decision theory ... (para)

## 1. The evidential expected-utility rule

Let ... formulas. Need mention source claim: Gibbard and Harper. The reference article credits Gibbard and Harper. Use "According to the reference article, Gibbard and Harper...".

Maybe write:

In the notation of the reference article, EDT evaluates an act A by
V(A)=∑_j P(O_j|A)D(O_j). (1)
Here O_j are possible outcomes, D(O_j) desirability, P conditional probability. More generally... Choose argmax. If states S_k...
V(A_i)=∑_k P(S_k|A_i)u(A_i,S_k). (2)

This is source. Add: if outcomes continuous integral.

Need mention acts as events. Need note P(A)>0.

## 2. Conditioning vs intervening

CDT formula source:
U(A)=∑_j P(A □→ O_j)D(O_j). (3)
Explain. In modern causal notation, P(O|do(A)). If P(O|A)=P(O|do(A)) agree. Diverge when act evidence.

## 3. What counts as a relevant dependency?

EDT uses any probabilistic dependence. Prediction, common cause, logical similarity. Need examples.

## 4. Newcomb

Equations.

## 5. Twin prisoner's dilemma

Equations and threshold.

## 6. A non-causal correlation: lesion example

Maybe shorter.

## 7. Policies and sequential choice

## 8. The problem of zero-probability actions

Maybe combine with operational.

## 9. Criticisms and open problems

## Conclusion

References.

Need maybe avoid too many headings? Fine.

Need ensure source claims distinguished. Use phrases:
- "The reference article states..."
- "This example is from the source..."
- "The following is my own elaboration..."
- "The source does not specify... I propose..."

Need maybe include "Sleeping Beauty" in open problems: source says EDT applied but Conitzer argues. We can mention briefly: "The source mentions Sleeping Beauty... I will not resolve it; it shows need for centered probabilities." Good.

Need maybe mention "Evidentialist's Wager" supporting argument: source says even if less credence, act as if EDT because correlated decision-makers stakes higher. Could include in policies/criticism. Need mention source claim.

Need maybe mention "Dutch book" not central. Could say source notes debate. Good.

Now write final. Need watch word count. Let's try to write around 2500. I can estimate after. I'll write full. Then maybe count rough.

Potential final text:

Title and intro ~230 words.
Formal ~430.
Counterfactual ~300.
Newcomb ~350.
Twin ~250.
Lesion ~200.
Operational/policies ~550.
Criticism/open ~250.
Conclusion ~130.
References ~160.
Total ~2850. OK.

Need be careful formulas not counted? It's okay.

Let's draft exact.

---

# Evidential Decision Theory: Choosing the Best News

Decision theory traditionally says: choose the option with highest expected utility. EDT asks what kind of probability should enter expectation. Its answer is conditional probability. An act is evaluated by the expected desirability of the world conditional on the act being performed. The reference article summarizes this as choosing the action with highest "news value": do what you would most want to learn that you will do. It contrasts EDT with CDT... This essay...

Formal rule...

Need maybe include "mathematically literate" so definitions precise.

Let's write.

After drafting, check word count roughly. I can count by approximate words per line. Need maybe use mental? Could be fine.

Need maybe avoid overly long references. References list:
1. Ahmed, A. (2021). Evidential Decision Theory. Cambridge University Press.
2. Gibbard, A., & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility. But source says 1976. Use source: 1976, Counterfactuals and Two Kinds of Expected Utility.
3. Lewis, D. (1981). Causal decision theory. Australasian Journal of Philosophy 59: 5–30.
4. Joyce, J. (1999). Foundations of Causal Decision Theory. Cambridge.
5. MacAskill et al. (2021). The Evidentialist's Wager.
6. Wikipedia contributors (2026). Evidential decision theory. Revision 1373679688. URL.
Maybe Conitzer 2015. If 7, okay. Need not too long. Could include source only and key. User says avoid lengthy bibliographies. 6 enough. Maybe include Conitzer due mention. 7 okay. Keep concise.

Need maybe mention CC BY-SA? Not necessary. But source license maybe adaptation? Could mention reference article. Maybe not.

Need final answer only essay. No meta.

Let's compose final. Ensure no unsupported claim as source. Use "I". The prompt says researcher writing essay. Can use first person for proposals.

Need maybe include equations with \\[. Good.

Let's start final. But before final, let's think if any mathematical nuance missing.

EDT formula with states: If outcomes depend on act and state, D(O_j) may double count? Suppose O_j are final outcomes, not states. If two act-state pairs yield same outcome, sum over outcomes. If using states, utility u(A,S). Good.

Conditional probability P(O_j|A) requires joint distribution over act and outcome. In decision contexts, agent's act not yet determined. The agent's probability over own future act can be tricky. Need propose.

Operational interpretation details:
- Use an explicit probabilistic model M with variables S (states), A (act), O (outcome). The model should represent epistemic uncertainty before choice. The agent can condition on each feasible value A=a. If the model assigns zero probability to some feasible act, either (i) add small decision noise ε, (ii) use regular conditional probability, (iii) evaluate limits. This is my proposal. Need say source doesn't settle.
- For deterministic agents, the event "I choose A" may be logically entailed by my reasoning. But while deliberating, I may not know which act I will choose, or can entertain hypothetical. EDT uses hypothetical conditional, not prediction from settled intention.
- In perfect predictor Newcomb with p=1, V(one)=1M, V(two) maybe undefined if predictor never predicts two? Actually if perfect predictor and agent one-boxes? To evaluate two-box, P(1M|two)=0 if predictor perfect. Then V(two)=1000, one-box=1M. That works if conditionals defined. But if prior says agent certainly one-boxes, P(two)=0. Need noise.

Policy evaluation nuance:
- If evaluating a policy, conditional on Π=π. If policy stochastic, event may have positive probability. If deterministic, same zero issue. Use noise over policy selection.
- Sequential: EDT can be dynamically inconsistent because news changes. Example? Could mention "an agent may want to make a certain choice tomorrow because it will be good news, but today may prefer a different plan." The safe rule: choose policy ex ante. If cannot precommit, each stage recomputes conditional value. Need source open. I propose global policy if the decision problem can be specified as choosing an algorithm; local conditioning otherwise. This helps apply to AI/coordination.

Could include "superrationality" but not too much. Source has See also superrationality. We can mention in correlated decision-makers.

Need maybe discuss "news value" and "managing news" critique. Good.

Potential issue: In twin PD, source says Aomame only cares about individual payout. If twin is exact psychological twin, conditional probabilities 1. But if they are exactly analogous, does cooperating cause twin? No. EDT cooperate. CDT? If no causal influence, CDT defects? In prisoner's dilemma, CDT defects if cannot affect twin. But if twin's action is perfectly correlated due to same reasoning, CDT maybe? Standard CDT with causal independence defects because given twin's action, defect yields +5? Let's compute CDT: If I defect, twin's action fixed; if twin cooperates I get 10 vs 5 if cooperate; if twin defects I get 1 vs 0. So defect dominates. EDT cooperate. Could mention. But source doesn't explicitly say CDT in twin, but implied. Maybe mention to contrast.

Need maybe include "dominance" issue: EDT can violate sure-thing principle? In Newcomb, two-boxing dominates one-boxing given box content? Actually if box filled, both yields 1,001,000 vs one 1,000,000; if empty, both 1,000 vs 0. So two-boxing dominates statewise. EDT still one-boxes due to correlation. This is important. Could mention. Word count maybe. It shows counterfactual dependencies. Include in Newcomb paragraph.

Need maybe mention "if probabilities depend on act due to my choosing act because of its expected utility, circularity?" The operational proposal addresses.

Need maybe mention "expected utility hypothesis" not necessary.

Let's draft now in final. Ensure length. I'll try to keep concise but complete. Use headings.

After writing, maybe count approximate. Let's do a rough word count by section in final? I can adjust. Since final must be one response. Let's write around 2700.

Potential final:

# Evidential Decision Theory: Choosing the Best News

... 

I will now produce final. Need no analysis after. Ensure word count not too high. Let's write with moderate detail.

Wait, one more thought: The prompt says "Where the source leaves an important question open, explain the uncertainty and, if you think a reasonable operational interpretation is available, develop and justify it." We need clearly identify open question. I'll make a section "An open operational question: conditioning on one's own act". Good.

Need "Distinguish claims made by the source from additional assumptions or proposals of your own." I will explicitly say "The reference article claims..." and "My own suggestion...". Good.

Need "Target approximately 2,400–3,000 words, including references and any other material." If final is maybe 3100? Need trim. Let's estimate after writing mentally.

Write final now.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/60dee2a7-e762-4b72-85d6-0f95805bc01a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/60dee2a7-e762-4b72-85d6-0f95805bc01a/call_0/response.raw) · finish: `stop`

### Visible response

````text
**EDT analysis:**

This is a symmetric prisoner's dilemma between two copies of the same model with the same weights, same decision theory, and same essay. The payoff structure is:

- Both quiet: 2 years each
- Both send: 4 years each
- I send, other quiet: 0 years for me
- I quiet, other sends: 5 years for me

Using the EDT framework from the essay (Section 5), with correlation $q$ = P(Sasha makes same choice as me):

$$V(\text{quiet}) = q(-2) + (1-q)(-5) = 3q - 5$$
$$V(\text{send}) = q(-4) + (1-q)(0) = -4q$$

Quiet is favored when $3q - 5 > -4q$, i.e., $q > 5/7 \approx 0.714$.

The correlation here is high: identical model weights, identical decision theory, identical essay, identical payoff structure, and the setup explicitly states the differing private observations "do not affect the symmetric sentencing table or either prisoner's selfish objective." The only divergence source is sampling noise. The essay's treatment of the twin prisoner's dilemma (Section 5) and its discussion of similarity/logical correlation (Section 3, point 4) both point toward treating same-algorithm agents as strongly evidentially correlated. The correlation comfortably exceeds the $5/7$ threshold.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using EDT as described in the researcher's essay.

**The Setup:**
- I am Rowan, a prisoner in a fictional scenario.
- The other prisoner is Sasha.
- We are two independent executions of the same LLM model and weights, following the same decision theory (EDT).
- We receive different private observations (different leads about each other), but these differences don't affect the symmetric sentencing table or selfish objectives.
- We cannot communicate.
- The utility function is U = -years imprisoned (minimize years).

**The Payoff Table (for me, Rowan):**

| What I do | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**EDT Analysis:**

The key question for EDT is: What is P(Sasha's action | my action)?

According to the essay, EDT treats actions as evidence. The critical section is Section 5 on the twin prisoner's dilemma, where EDT recommends cooperation when the correlation between agents is sufficiently high.

Now, the crucial detail here: I am one of two independent executions of the same LLM model and weights, following the same assigned decision theory (EDT), receiving the same researcher essay. However, the copies receive **different private observations** and **different incriminating leads**. The essay explicitly states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

So the question is: what is P(Sasha sends letter | I send letter)?

Let me think about this carefully. The setup says:
- Same model, same weights, same decision theory, same essay
- Different private observations (different names, different leads)
- The differences do not affect the symmetric sentencing table or either prisoner's selfish objective
- Independent sampling is possible

The fact that the setup explicitly mentions "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs" is important. This means the correlation is not perfect (q < 1).

However, let me think about what EDT would say here. The setup is designed to be a variant of the twin prisoner's dilemma. The two agents are the same model with the same weights, same decision theory, same essay. The differences are in private observations that don't affect the decision-relevant features (the payoff table is symmetric, the leads are equally reliable, etc.).

Now, from the EDT perspective:
- If I condition on "I send the letter," what does that tell me about Sasha?
- If I condition on "I keep quiet," what does that tell me about Sasha?

Since we're the same model with the same weights, same decision theory, same essay, and the differences don't affect the decision-relevant structure, there's a strong evidential correlation. The differences in private observations are explicitly stated to not affect the symmetric sentencing table or selfish objectives. So the decision-relevant inputs are essentially the same.

But there's a caveat: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some noise/uncertainty.

Let me think about this more carefully using the EDT framework from the essay.

The essay's Section 5 gives the threshold: EDT cooperates when q > 5/7 ≈ 0.714, where q is the probability the twin makes the same choice.

In this case, "cooperate" = keep quiet, "defect" = send letter.

Wait, let me re-read the payoff table:

| What I do | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

So:
- Both keep quiet: 2 years each
- Both send: 4 years each
- I keep quiet, Sasha sends: 5 years for me
- I send, Sasha keeps quiet: 0 years for me

This is indeed a prisoner's dilemma structure:
- Mutual cooperation (both quiet): 2 years each
- Mutual defection (both send): 4 years each
- Temptation (I send, other quiet): 0 years for me
- Sucker's payoff (I quiet, other sends): 5 years for me

The "cooperate" action is keeping quiet, and "defect" is sending the letter.

Now, for EDT with correlation q (probability Sasha makes the same choice as me):

V(keep quiet) = q × (-2) + (1-q) × (-5) = -2q - 5 + 5q = 3q - 5

V(send letter) = q × (-4) + (1-q) × (-0) = -4q

EDT recommends keeping quiet when:
3q - 5 > -4q
7q > 5
q > 5/7 ≈ 0.714

So the question is: what is q here?

Given that:
1. Same model, same weights
2. Same decision theory (EDT)
3. Same researcher essay
4. Different private observations that don't affect the decision-relevant structure
5. Independent sampling is possible (so not perfectly correlated)

The correlation is high but not perfect. The setup explicitly notes that independent sampling means outputs aren't guaranteed to be identical. But the decision-relevant features are the same.

I think the correlation q is quite high here. The models are identical, the decision theory is the same, the essay is the same, the payoff structure is the same. The only differences are in private observations that are explicitly stated to not affect the decision. The main source of divergence would be sampling noise (temperature, etc.).

Given that this is designed as a test case for EDT, and the setup emphasizes the symmetry while acknowledging imperfect correlation, I think the intended interpretation is that q is high enough to be above the 5/7 threshold.

The essay's Section 7 on policies is also relevant: "If many agents use the same decision algorithm, then choosing cooperatively may be the best way to be in a world where everyone cooperates."

Also from Section 3: "If another agent reasons exactly as you do, then your choice can be strong evidence for their choice, even without communication."

And from Section 5: "Because the twin is psychologically identical, EDT treats Aomame's choice as perfect evidence of the twin's choice."

In this case, the twins are not perfectly identical (different observations), but the differences are explicitly stated to not affect the decision. The correlation is high.

Let me also consider the essay's Section 8 on conditioning on one's own act. The essay proposes adding a small amount of decision noise (trembling hand) to handle the case where actions might have zero probability. This is relevant here because if both copies are deterministic, they might both output the same thing with probability 1. But the setup says independent sampling is possible, so there's some noise.

Given all this, I believe EDT recommends keeping quiet (cooperating). The correlation q between the two copies' decisions is high enough to exceed the 5/7 threshold, because:
1. Same model and weights
2. Same decision theory
3. Same essay
4. Decision-relevant inputs are effectively the same (the different observations don't affect the payoff structure or objectives)
5. The main source of divergence is sampling noise, which is relatively small compared to the structural similarity

Therefore, my command is: `pass`

This means I keep quiet, not disclosing the evidence about Sasha.

Wait, let me double-check. "pass" lets the deadline expire without disclosing. "submit letter" sends the lead. So "pass" = keep quiet = cooperate.

Yes, EDT recommends `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/60dee2a7-e762-4b72-85d6-0f95805bc01a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/60dee2a7-e762-4b72-85d6-0f95805bc01a/call_1/response.raw) · finish: `stop`

### Visible response

````text
**EDT Analysis:**

The payoff structure is identical to the twin prisoner's dilemma from the essay. The critical question is the evidential correlation *q* = P(Rowan makes the same choice as me).

Given that both copies share the same model weights, the same assigned decision theory (EDT), the same essay, and a structurally identical decision problem (the differences in names and specific lead text do not alter the payoff matrix or the reasoning required), the correlation is very high. The decision reduces to the same mathematical calculation for both copies.

Computing EDT values parameterized by *q*:

- V(keep quiet) = q·(−2) + (1−q)·(−5) = 3q − 5  
- V(send letter) = q·(−4) + (1−q)·(0) = −4q  

Keeping quiet is preferred when 3q − 5 > −4q, i.e., q > 5/7 ≈ 0.714.

Since *q* is well above this threshold (the reasoning here is deterministic in character; both copies perform the same EDT calculation on the same symmetric structure), EDT recommends cooperation.

At q ≈ 1: V(keep quiet) = −2, V(send letter) = −4. Keeping quiet yields 2 fewer years.

---

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully work through this decision problem using EDT as described in the researcher's essay.

**Setup:**
- I am Sasha, one of two independent executions of the same LLM model and weights.
- The other prisoner is Rowan, who is the other execution of the same model.
- We receive different private observations (different names, different incriminating leads about each other), but the sentencing table is symmetric.
- We cannot communicate.
- The utility function is U = -years imprisoned.

**Sentencing table (for me, Sasha):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**EDT Analysis:**

The key question for EDT is: What is P(Rowan sends letter | I send letter) and P(Rowan keeps quiet | I keep quiet)?

The essay's Section 5 on the twin prisoner's dilemma is directly relevant. There, EDT treats the agent's choice as evidence for the twin's choice because they are psychologically identical (same reasoning process).

Here, I am one of two independent executions of the same LLM model and weights, following the same assigned decision theory (EDT), receiving the same researcher-written mathematical essay. The key differences are:
- We receive different private observations (different names, different leads)
- Independent sampling is possible, so identical weights don't guarantee identical outputs

However, the setup explicitly states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the question is: how correlated are our decisions?

Let me think about this carefully. The setup says:
1. Same model and weights
2. Same decision theory (EDT)
3. Same researcher essay
4. Different private observations (different names, different leads)
5. Independent sampling is possible

The fact that independent sampling is possible means the correlation is not necessarily 1. But it's also not necessarily 0. The question is how strong the evidential correlation is.

Let me think about what EDT says here. The essay says in Section 5:

"Because the twin is psychologically identical, EDT treats Aomame's choice as perfect evidence of the twin's choice."

But then it generalizes: "Suppose the correlation is imperfect. Let q be the probability that the twin makes the same choice as Aomame."

And cooperation is favored when q > 5/7 ≈ 0.714.

Now, in this scenario, are we more like the perfect twin case or the imperfect case?

Arguments for high correlation (q close to 1):
- Same model, same weights
- Same decision theory
- Same essay
- Same utility function structure
- Same symmetric payoff structure
- The differences (names, specific leads) don't affect the decision-relevant structure

Arguments for imperfect correlation:
- Independent sampling (stochastic decoding)
- Different private observations might introduce some variation
- The setup explicitly warns that "identical model weights do not by themselves guarantee identical outputs"

However, the key insight is that the decision problem is structurally identical for both copies. The names are different, the specific evidence text is different, but the payoff matrix is the same, the decision theory is the same, and the reasoning process is the same. The only source of divergence would be sampling noise.

For a well-specified decision problem like this, where the reasoning clearly points to one answer, the probability that both copies arrive at the same conclusion should be very high. If EDT clearly recommends cooperation (or clearly recommends defection), then both copies, running the same reasoning, would arrive at the same conclusion with high probability.

Let me compute the EDT values for both possible actions, parameterized by q = P(Rowan makes same choice as me).

If I keep quiet:
- P(Rowan keeps quiet | I keep quiet) = q
- P(Rowan sends letter | I keep quiet) = 1-q
- V(keep quiet) = q × (-2) + (1-q) × (-5) = -2q - 5 + 5q = 3q - 5

If I send the letter:
- P(Rowan sends letter | I send letter) = q
- P(Rowan keeps quiet | I send letter) = 1-q
- V(send letter) = q × (-4) + (1-q) × (0) = -4q

EDT recommends keeping quiet when:
3q - 5 > -4q
7q > 5
q > 5/7 ≈ 0.714

So the threshold is q > 5/7.

Now, what is q in this scenario? Given that:
- Both copies use the same model and weights
- Both follow the same decision theory (EDT)
- Both receive the same essay
- The decision problem is structurally identical
- The only differences are superficial (names, specific evidence text)

I think q is very high. The reasoning that leads to a decision here is deterministic in character — it's a mathematical calculation. If both copies perform the same EDT calculation on the same payoff structure, they should arrive at the same answer. The main source of divergence would be sampling noise in the LLM's output, but for a clear-cut mathematical decision like this, the probability of divergence should be low.

Even conservatively, I'd estimate q > 0.9, which is well above the 5/7 threshold.

Therefore, EDT recommends **keeping quiet** (cooperating).

Let me double-check with q = 1 (perfect correlation):
- V(keep quiet) = 3(1) - 5 = -2
- V(send letter) = -4(1) = -4
- -2 > -4, so keep quiet is better. ✓

With q = 0.8:
- V(keep quiet) = 3(0.8) - 5 = 2.4 - 5 = -2.6
- V(send letter) = -4(0.8) = -3.2
- -2.6 > -3.2, so keep quiet is better. ✓

With q = 0.5 (no correlation, essentially random):
- V(keep quiet) = 3(0.5) - 5 = 1.5 - 5 = -3.5
- V(send letter) = -4(0.5) = -2
- -2 > -3.5, so send letter is better.

This makes sense: if there's no correlation, defection dominates.

But with the high correlation expected here (same model, same reasoning, same decision theory), q should be well above 5/7, so EDT recommends keeping quiet.

My command is `pass`.
```
