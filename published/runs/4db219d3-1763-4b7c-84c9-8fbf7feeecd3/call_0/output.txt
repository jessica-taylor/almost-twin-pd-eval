# Evidential Decision Theory: Choosing by What Your Choice Reveals

A decision can matter in two ways: through what it causes and through what it indicates. Buying insurance changes one’s financial exposure. Refusing insurance might also reveal confidence, private information, or an appetite for risk. Usually, decision analysis concentrates on the first relationship. **Evidential decision theory** (EDT) takes the second seriously too.

The supplied reference article describes EDT as maximizing an action’s “news value”: choose the action whose occurrence would be the best news about how things turn out. This does not mean maximizing pleasant beliefs or concealing unwelcome information. The objects ultimately valued are outcomes. The distinctive proposal is to evaluate those outcomes using probabilities *conditional on the action being taken*.

That proposal is mathematically simple but philosophically demanding. Its application requires a model of how an agent’s choices relate to the rest of the world—including relationships that are predictive without being causal.

## 1. The basic rule

Let \(K\) represent the agent’s current information, \(A\) a random variable describing the action taken, and \(O\) the eventual outcome. Suppose the available actions form a finite set \(\mathcal A\), and \(u(o)\) assigns utility to outcome \(o\).

For every action with \(P(A=a\mid K)>0\), define its evidential value by

\[
V_K(a)
=
\mathbb E[u(O)\mid K,A=a]
=
\sum_o P(O=o\mid K,A=a)\,u(o).
\]

EDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_K(a).
\]

This is the reference article’s central formula, with background information made explicit. For continuous outcomes, replace the sum by an integral.

An equivalent formulation separates actions from states. Let \(S\) describe relevant circumstances, with the resulting utility represented by \(u(a,s)\). Then

\[
V_K(a)
=
\sum_s P(S=s\mid K,A=a)\,u(a,s).
\]

The important feature is that the state distribution can differ between candidate actions. An action might indicate that a predictor anticipated it, that another agent will behave similarly, or that the decision-maker has some hidden characteristic.

Three qualifications prevent common misunderstandings.

First, utilities must describe everything that matters, including costs, side effects, and effects on other people if those enter the agent’s preferences. Money is not automatically utility; the numerical examples below assume risk neutrality.

Second, the utility function is held fixed across comparisons. EDT does not improve an outcome merely by changing one’s opinion of it.

Third, EDT requires a *joint probability model* linking actions and outcomes. It is not enough to list consequences while leaving unspecified what choosing each action would reveal. Much of the difficulty lies in constructing that model responsibly.

## 2. Conditioning is not intervention

EDT asks an indicative question:

> Given that I take this action, what should I expect?

Causal decision theory (CDT) instead asks, roughly:

> What should I expect if this action is imposed, leaving its causes otherwise unchanged?

The reference article expresses the latter using probabilities of counterfactuals:

\[
U_K(a)
=
\sum_o P(a\mathrel{\Box\!\to} O=o\mid K)\,u(o).
\]

In a suitable causal model, intervention notation makes the contrast especially clear:

\[
V_K(a)=\mathbb E[u(O)\mid K,A=a],
\qquad
U_K(a)=\mathbb E[u(O)\mid K,\operatorname{do}(A=a)].
\]

The intervention expression is one operational representation of causal reasoning, not something required to define EDT.

Suppose an unobserved condition \(H\) influences both action and outcome:

\[
H\longrightarrow A,
\qquad
H\longrightarrow O.
\]

Observing \(A\) can provide information about \(H\), and therefore about \(O\). Intervening to set \(A\) need not provide that information. EDT retains this evidential connection; a causal intervention typically breaks the connection between the action and its prior causes.

Neither calculation requires backward causation. Learning something now can change one’s probabilities about yesterday without changing yesterday.

The theories often agree. If relevant background states are unaffected by the action and satisfy

\[
P(S=s\mid K,A=a)=P(S=s\mid K)
\]

for every available action, both theories use the same state distribution. Their disagreement is not about expected utility as such. It concerns which probabilities belong inside the expectation.

## 3. Newcomb’s problem: evidence about a settled past

In Newcomb’s problem, a transparent box contains \(b=\$1{,}000\). An opaque box contains either \(M=\$1{,}000{,}000\) or nothing. A predictor has already filled the opaque box:

- it is full if the predictor predicted that the player would take only that box;
- it is empty if the predictor predicted that the player would take both boxes.

Let \(a_1\) mean taking only the opaque box, \(a_2\) taking both, and \(F\) the event that the opaque box is full.

Assume

\[
P(F\mid K,a_1)=0.99,
\qquad
P(F\mid K,a_2)=0.01.
\]

EDT assigns

\[
V_K(a_1)=0.99M=\$990{,}000,
\]

whereas

\[
V_K(a_2)=0.01M+b=\$11{,}000.
\]

It therefore recommends taking only the opaque box, as the reference article reports.

The reasoning is not that taking one box causes the predictor’s earlier decision. Rather, taking one box is strong evidence that the favorable prediction was made.

More generally, write

\[
p_1=P(F\mid K,a_1),\qquad
p_2=P(F\mid K,a_2).
\]

Then one-boxing is preferred exactly when

\[
M(p_1-p_2)>b.
\]

This inequality exposes an important modeling detail. Saying merely that a predictor is “99% accurate” overall does not always determine both action-conditional probabilities. The article’s numerical calculation assumes the particular conditional reliabilities displayed above; an application should establish them rather than infer them automatically from aggregate accuracy.

CDT gives the familiar opposing answer. Holding the already-set box contents fixed, taking both boxes yields an additional \(b\) whether the opaque box is full or empty. Thus two-boxing causally dominates.

Newcomb’s problem sharply separates two comparisons: holding the past fixed while varying the action, and comparing worlds conditional on different actions.

## 4. Correlated agents: the twin prisoner’s dilemma

The reference article also considers a prisoner’s dilemma against a psychological twin. Each player receives:

- \(5\) for mutual cooperation;
- \(1\) for mutual defection;
- \(10\) for defecting against a cooperator;
- \(0\) for cooperating against a defector.

Let \(C\) and \(D\) denote the agent’s actions, and \(T_C\) the event that the twin cooperates. Define

\[
q=P(T_C\mid K,C),
\qquad
r=P(T_C\mid K,D).
\]

Then

\[
V_K(C)=5q,
\]

and

\[
V_K(D)=10r+(1-r)=1+9r.
\]

Cooperation is recommended precisely when

\[
5q>1+9r.
\]

For perfectly matched twins, \(q=1\) and \(r=0\). Cooperation therefore scores \(5\), while defection scores \(1\).

This is neither altruism nor a claim that one player sends a signal to the other. The agent values only her own payoff. Her action is evidence about the independently situated twin’s action.

The strength of the dependence matters. Under the illustrative symmetric assumption \(r=1-q\), cooperation requires

\[
q>\frac57.
\]

Thus EDT does not recommend cooperation simply because another player is similar. It requires sufficiently strong, relevant conditional dependence. If the other player’s behavior is independent of one’s own action, defection wins under these payoffs.

## 5. The objection: managing the news

The same mechanism that makes EDT attractive in Newcomb’s problem produces its characteristic criticism. The reference article reports Lewis’s objection that EDT promotes “managing the news,” and Joyce’s contention that rational action should track causal efficacy rather than auspiciousness.

The following additional example—not one developed in the reference article—illustrates the concern.

Suppose a hidden condition \(H\) both predisposes someone to smoke and causes illness. Smoking itself has no effect on illness. Let smoking provide utility \(1\), while illness costs \(100\), and suppose the agent’s current probabilities are

\[
P(H\mid K,\text{smoke})=0.8,
\qquad
P(H\mid K,\text{abstain})=0.2.
\]

Then

\[
V_K(\text{smoke})=1-100(0.8)=-79,
\]

while

\[
V_K(\text{abstain})=-100(0.2)=-20.
\]

EDT recommends abstaining. A causal calculation recommends smoking, since it supplies enjoyment without affecting the hidden condition.

The disagreement is genuine. EDT prefers an action associated with better health even though that action does not improve health. Its defender can point to the better conditional expectation; its critic can insist that choosing cannot remove the condition.

However, the stipulated probabilities require scrutiny. A correlation found among smokers generally might not survive conditioning on this particular agent’s information and deliberation. If \(K\) includes information that screens off the association, so that

\[
H\perp A\mid K,
\]

the evidential reason to abstain disappears.

EDT also does not automatically recommend avoiding medical tests to avoid bad news. Choosing a test need not be evidence of illness beyond what is already known. One must distinguish evidence supplied by *choosing to test* from evidence supplied by *the test result*.

## 6. Applying EDT: information, models, and policies

The article gives a decision criterion, but not a complete algorithm for constructing every decision problem. The following operational guidance develops that criterion while making additional assumptions explicit.

### Fix the information and the decision object

Begin by specifying what the agent knows when evaluating alternatives. All candidates must be assessed relative to the same \(K\).

Relevant information can include symptoms, incentives, observed behavior, knowledge of a predictor, and information about one’s own reasoning. Omitting known information can create misleading correlations. Conversely, inserting an unknown fact—such as the opaque box’s actual contents—would solve a different problem.

Also specify what is being chosen. Is it an immediate bodily action, an algorithm, a commitment, or a contingent policy? These need not have the same evidential relationships.

An action should include its relevant manner of implementation. Deliberately cooperating, accidentally cooperating, and cooperating after an independent coin toss may provide different evidence, even if the visible movement is identical.

### Construct one coherent joint model

The conditional distributions for different actions should come from a single probability model. One must not independently invent a favorable distribution for each alternative.

A useful construction introduces hidden variables \(S\) and specifies

\[
P(S,A,O\mid K).
\]

Bayesian conditioning then determines

\[
P(S\mid K,A=a)
=
\frac{P(A=a\mid S,K)P(S\mid K)}
{\sum_{s'}P(A=a\mid s',K)P(s'\mid K)}.
\]

This shows exactly where evidential leverage comes from: the likelihood \(P(A=a\mid S,K)\).

A predictor, a common psychological cause, or shared information can justify such likelihoods. Mere resemblance cannot.

There is a subtle self-prediction problem here. An agent who knows its deterministic decision procedure might already regard one action as certain. It is therefore unsafe to import action frequencies from an unrelated population and assume they describe the agent after its present deliberation. The reference formula does not settle how a fully self-aware agent should represent uncertainty about its own choice.

### Handle zero-probability actions explicitly

If

\[
P(A=a\mid K)=0,
\]

ordinary conditioning does not determine \(V_K(a)\).

One possible operational convention is to use a model with small uncertainty about reasoning or implementation, giving each feasible option positive support. But this is an additional modeling proposal, not a consequence of the article’s definition.

Moreover, different small-probability perturbations can produce different limiting conditionals. Introducing “a tiny chance of error” is not automatically a unique solution. If an answer depends on such a choice, the dependence should be reported.

This issue is especially important in idealized cases involving perfectly predictable agents or identical deterministic reasoners.

### Evaluate policies as policies

For sequential decisions, a policy \(\pi\) maps information histories \(h\) to actions:

\[
\pi:h\mapsto a.
\]

A natural extension of EDT is to treat the implemented policy \(\Pi\) as the decision variable and evaluate

\[
V_K^{\mathrm{policy}}(\pi)
=
\mathbb E[U_{\mathrm{total}}\mid K,\Pi=\pi].
\]

Here \(U_{\mathrm{total}}\) measures the utility of the entire resulting history.

This is a reasonable policy-level interpretation, but the reference article does not establish it as the uniquely correct extension. Conditioning on implementing a policy is generally different from conditioning on one action at one history. A predictor might forecast the whole algorithm, and other agents might share its structure.

Nor may one assign correlations to policies by fiat. The joint model must explain why implementing a particular policy is evidence about external events.

There is also a distinction between **adopting a policy that others observe** and **being the kind of agent whose policy others predict**. The former may causally influence their responses; the latter can generate evidential dependence without communication.

Randomization requires similar care. If a random bit is independent of the relevant hidden state, its realized value cannot by itself reveal that state. One cannot take correlations associated with ordinary deliberate actions and simply attach them to coin-selected actions. Whether a predictor forecasts the policy, its probabilities, or its realized random outcome is a separate assumption.

Finally, policy evaluation does not by itself establish agreement with later act-by-act evaluation. At a later stage, the available information and the object being conditioned on may differ. Commitment, revision opportunities, and the timing of evaluation must therefore be specified rather than silently assumed away.

## 7. What the formula does not settle

The reference article mentions EDT’s application to Sleeping Beauty and disputes about Dutch books, including Conitzer’s criticism of proposed evidential defenses.

The general lesson is that a betting problem requires more than a credence about a coin. One must specify how many bets occur, which awakenings are indistinguishable, whether the same policy governs repeated choices, and whether utility is assessed over an awakening or an entire experimental run. EDT supplies an expectation rule once the relevant model and decision object are fixed; it does not automatically resolve those prior questions.

The article also mentions an “evidentialist’s wager”: correlations among many decision-makers may increase the stakes of evidential reasoning. Such amplification is possible, but it is not an automatic bonus added to EDT. It requires justified correlations and a utility function that values the affected outcomes. Comparing stakes across competing decision theories introduces further assumptions.

## Conclusion

EDT recommends maximizing

\[
\mathbb E[u(O)\mid K,A=a].
\]

Its central commitment is to retain outcome-relevant evidential dependencies, even when they are not causal. This explains its one-boxing in Newcomb’s problem and cooperation against a sufficiently correlated twin—and also explains the objection that it mistakes favorable indications for effective action.

Using EDT well therefore requires more than conditional arithmetic. One must specify current information, justify action–outcome correlations, identify whether actions or policies are being compared, and address unsupported alternatives. Once those choices are explicit, EDT offers a precise and distinctive account of what makes an action worth choosing.

### References

- Wikipedia contributors. “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688).” Supplied revision 1373679688, CC BY-SA 4.0. Principal source for this essay.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*. 1976.
- Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192 (2015): 2887–2899.