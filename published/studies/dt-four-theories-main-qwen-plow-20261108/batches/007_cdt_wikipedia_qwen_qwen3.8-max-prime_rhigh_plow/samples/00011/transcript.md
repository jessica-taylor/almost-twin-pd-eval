# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00011

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/bee12c30-c508-423c-9c3b-5ce24fc9874a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/bee12c30-c508-423c-9c3b-5ce24fc9874a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing What Causes Good Outcomes

Causal decision theory (CDT) is a school of thought in decision theory that says a rational agent should choose the action that has the best expected *causal* consequences. The reference article summarizes the contrast with evidential decision theory (EDT) nicely: CDT asks which action would *bring about* the best outcome, whereas EDT asks which action would be the best “news” if one learned that it had been taken (Wikipedia contributors, 2026; Ahmed, 2021). This essay explains the formal core of CDT, shows how it evaluates actions and policies, and discusses how it treats dependencies and counterfactuals. The article supplies the central counterfactual formula but leaves open how counterfactual probabilities are to be computed. I will therefore distinguish the source’s claims from an operational interpretation that I develop, mainly using interventionist causal modeling as a precise way to apply CDT.

---

## 1. Expected utility: evidential and causal versions

Let \(\mathcal A\) be a set of possible actions, and let \(\mathcal O = \{O_1,\dots,O_n\}\) be a set of possible outcomes. Each outcome has a desirability or utility \(D(O_j)\). The agent has probabilities over relevant propositions. EDT evaluates an action \(A\) by ordinary conditional probabilities:

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This is the expected utility of \(A\) conditional on the “news” that \(A\) was performed. If hearing “you did \(A\)” would raise the probability of good outcomes, EDT favors \(A\).

CDT replaces the conditional probabilities with probabilities of counterfactuals. Gibbard and Harper (1981), as quoted in the reference article, give the canonical formula:

\[
U(A)=\sum_j P(A \to O_j)D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(A\to O_j)\) is the probability of the counterfactual that, if \(A\) were performed, \(O_j\) would obtain. To avoid confusion with material implication or ordinary conditionals, it is common to write the counterfactual as \(A \,\square\!\to\, O_j\). Then:

\[
U(A)=\sum_j P(A \,\square\!\to\, O_j)D(O_j).
\]

The essential idea is not merely “what is probable given \(A\)?” but “what would be caused by \(A\)?” If eating an apple causes happiness and eating an orange causes sadness, CDT says eat the apple. If the apple may be good or bad, CDT evaluates the expected causal effect: how likely the apple is to be good, how good a good apple is, and how bad a bad apple is.

---

## 2. Why counterfactual probabilities are not conditional probabilities

The reference article emphasizes a formal reason why CDT is not reducible to EDT: Lewis (1976) proved that the probability of a conditional cannot generally be identified with the corresponding conditional probability. In particular, if a class of probability functions is closed under conditionalization, there is no nontrivial probability conditional satisfying \(P(A\to O)=P(O\mid A)\) in general. If the equality always held, CDT would collapse into EDT.

Gibbard and Harper showed that, under certain assumptions—including a principle related to conditional excluded middle—statistical independence between the action \(A\) and the counterfactual \(A\to O_j\) is enough to make \(P(A\to O_j)=P(O_j\mid A)\). But in many decision problems the action is not independent of the relevant counterfactuals. The action may be evidence about a common cause that also affects the outcome, even though the action itself does not cause the outcome.

The article’s King David example illustrates this. David wants Bathsheba but fears that summoning her may provoke revolt. He knows that kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. David does not know whether he is charismatic. Summoning Bathsheba would be unjust, and therefore evidence that he is uncharismatic. EDT says abstain, because summoning is bad news: it indicates uncharismatic character and hence higher revolt risk. CDT says send for her, because David’s charisma is fixed; the act of summoning does not causally change his charisma or directly cause revolt.

We can represent this with variables:

- \(C\): David is charismatic.
- \(A\): David summons Bathsheba.
- \(R\): revolt occurs.

Charisma \(C\) causes both \(A\) and \(R\), but \(A\) does not cause \(R\). EDT uses \(P(R\mid A)\), which is high if \(A\) is evidence of low charisma. CDT uses the interventionist or counterfactual probability:

\[
P(R\mid do(A))=\sum_c P(C=c)P(R\mid C=c),
\]

which, under the stated causal story, is the same as \(P(R\mid do(\neg A))\). If summoning does not change the probability of revolt, then David should simply weigh the direct benefit of summoning against costs that are actually caused by it. This is the central CDT lesson: correlations that merely indicate a bad state should not be treated as causal reasons against an action.

---

## 3. What are counterfactual probabilities?

The reference article correctly notes that CDT itself does not specify an algorithm for computing counterfactual probabilities. It mentions Lewis’s “imaging” proposal: to evaluate \(P(A\to O_j)\), move probability mass from each possible world \(w\) to the closest possible world \(w_A\) in which \(A\) holds, then see how much mass lands in worlds where \(O_j\) holds. Imaging captures the idea of counterfactual supposition: we do not merely conditionalize on \(A\); we adjust our worldview to make \(A\) true in a minimally disruptive way.

However, as the article notes, imaging raises difficult questions. We need a notion of “closest” possible world, and we need to know what the agent would believe if certain of \(A\). That latter belief is itself a conditional belief, and one may assign probability less than one to it, leading to regress. The source therefore leaves an important gap: CDT tells us to maximize expected counterfactual utility, but not exactly how to calculate the counterfactual probabilities.

A reasonable operational interpretation, not supplied by the article but widely used in modern causal inference, is to model counterfactuals by structural causal models or potential outcomes. I propose the following as an additional assumption for making CDT precise.

Let a causal model contain variables \(V\), background variables \(U\), and structural equations determining each variable from its causes. An action \(A=a\) is represented as an intervention \(do(A=a)\), which replaces the usual causal equation for \(A\) with the fixed value \(a\). The probability of the counterfactual “if \(A\) were performed, \(O_j\) would occur” becomes:

\[
P(A \,\square\!\to\, O_j)=P(O_j\mid do(A)).
\]

Equivalently, for each action \(a\), define a potential outcome \(O_a\), the outcome that would occur if \(a\) were performed. Then CDT maximizes:

\[
U(a)=\mathbb{E}[D(O_a)] = \sum_o D(o)P(O_a=o).
\]

This interventionist reading fits CDT’s philosophical motivation. It distinguishes observing \(A\) from setting \(A\). Observing \(A\) may provide evidence about common causes, predictors, or the agent’s character. Setting \(A\) changes the world only along causal paths that run from \(A\) to downstream variables.

This operationalization also clarifies when EDT and CDT agree. If the action is effectively randomized—statistically independent of all common causes that affect the outcome—then:

\[
P(O\mid do(A))=P(O\mid A).
\]

In randomized experiments, conditional probabilities can estimate causal effects. In ordinary deliberation, however, actions often correlate with character, predictions, or background states. CDT requires us to correct for those correlations by asking what would happen under intervention.

---

## 4. How CDT evaluates actions and policies

Using the interventionist interpretation, a practical CDT procedure can be stated as follows.

1. **Specify the options.** These may be simple actions \(a\in\mathcal A\) or policies \(\pi\) mapping observations to actions.

2. **Specify the causal structure.** Identify variables representing the agent’s action, outcomes, predictors, character traits, states of the world, and relevant background causes. The crucial question is: which variables are causally affected by the action or policy?

3. **Compute post-intervention probabilities.** For each action \(a\), compute \(P(O_j\mid do(A=a))\). For a deterministic policy \(\pi\) that chooses \(A=\pi(X)\) given observations \(X\), compute:

   \[
   U(\pi)=\sum_y D(y)P(Y=y\mid do(A=\pi(X))).
   \]

   For stochastic policies, the intervention sets \(A\) to be sampled from a distribution \(\pi(\cdot\mid X)\).

4. **Maximize expected causal utility.** Choose an action or policy with maximal \(U\).

If the agent is uncertain about the causal structure itself, one can average over causal hypotheses \(H\):

\[
U(a)=\sum_H P(H)\sum_j D(O_j)P(O_j\mid do(a),H).
\]

This is natural but delicate. The reference article mentions Andy Egan’s criticism that CDT’s requirement to “hold fixed the agent’s unconditional credences in dependency hypotheses” can lead to irrational decisions. Egan’s complaint is that CDT may treat the agent’s causal picture as too rigid, ignoring the evidential significance of the fact that the agent is about to perform a certain action. Jim Joyce, by contrast, argues that CDT can take into account evidence about one’s own inclinations and likely behavior (Weirich, 2016; Joyce, 2012).

My preferred operational interpretation is this: before evaluating interventions, the agent should condition on all available evidence, including evidence about her own likely choices. But once she evaluates \(do(A=a)\), she should not treat the action itself as further evidence about variables that are causally unaffected by the action. In other words: update on what you know before the intervention; do not condition on the act as news when calculating its causal consequences. This distinction is not always easy to apply in reflexive or self-predictive cases, but it gives CDT a workable discipline.

---

## 5. Examples

### 5.1 Newcomb’s problem

The reference article discusses Newcomb’s problem. A highly reliable predictor has already predicted whether the agent will take both boxes or only one. Box A always contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The agent chooses after the prediction has been made.

EDT recommends one-boxing because choosing only box B is strong evidence that box B is full. CDT recommends two-boxing. The causal reasoning is that the predictor’s prediction is already in the past; the present choice cannot causally change whether box B contains money. Given either possible content of box B, two-boxing yields \$1,000 more than one-boxing:

\[
\begin{array}{c|cc}
 & B\text{ full} & B\text{ empty}\\
 \hline
\text{One-box} & 1{,}000{,}000 & 0\\
\text{Two-box} & 1{,}001{,}000 & 1{,}000
\end{array}
\]

Two-boxing dominates. In interventionist notation, if \(B\) is fixed before the choice and there is no backward causation, then:

\[
P(B\text{ full}\mid do(\text{two-box}))
=
P(B\text{ full}),
\]

and the only causal effect of two-boxing is to add the contents of box A.

This is one of the most famous alleged counterexamples to CDT. The reference article notes that philosophers disagree about whether one-boxing or two-boxing is rational. From a CDT perspective, the decisive fact is that the choice does not causally influence the predictor’s earlier prediction. If, however, the agent can choose a decision procedure before the predictor makes its prediction, CDT may recommend adopting a one-boxing disposition, because that disposition can causally influence the prediction. This illustrates an important point: CDT may evaluate policies differently from one-time actions, depending on when the policy has causal leverage.

### 5.2 Prisoner’s dilemma and correlated twins

The reference article also mentions prisoner’s dilemma cases where one plays against a “twin” whose choice is strongly correlated with one’s own but not caused by it. EDT may favor cooperation because cooperating is evidence that the twin will cooperate. CDT, if it holds fixed the causal independence of the players’ choices, evaluates the causal effect of one’s own move given the twin’s choice. In the standard payoff structure, defection dominates: whatever the twin does, defecting yields a better causal outcome for the agent. Again, the disagreement is not mathematical but normative: should rational choice track causal influence or evidential correlation?

### 5.3 Death in Damascus

In the “Death in Damascus” scenario, Death predicts where you will be tomorrow and goes there. If Death is a reliable predictor, your choice of location is strongly correlated with Death’s location, but your choice may not causally affect Death’s earlier prediction. CDT can therefore struggle: from a causal perspective, fleeing may not change where Death already plans to be; from an evidential perspective, fleeing indicates that Death will be in the place fled to.

The reference article says that a CDT agent may be unable to process the correlation and may make irrational decisions. In an interventionist model, if Death’s location is fixed by a prediction caused by your future choice’s antecedents, then setting your location by intervention does not change Death’s location. But if your deliberation itself is what Death predicts, the case becomes reflexive: your attempt to choose may be evidence of what you will choose, and hence of what Death predicts. This is one class of cases where CDT’s instruction to hold fixed dependency hypotheses seems unstable. The source leaves open exactly how CDT should handle such cases; my operational advice is to model the prediction mechanism explicitly, including the agent’s deliberative process, but doing so may not fully dissolve the philosophical puzzle.

### 5.4 The psychopath button

The reference article gives Egan’s psychopath button example. Paul can press a button that kills all psychopaths. Paul prefers a world without psychopaths, but he is confident that only a psychopath would press the button, and he prefers living in a world with psychopaths to dying. The intuitive verdict, according to Egan, is that Paul should not press; yet CDT is alleged to endorse pressing.

A simple CDT model might treat psychopathy as a fixed trait \(T\), pressing as action \(A\), and death or a psychopath-free world as outcomes. If pressing does not cause Paul to be a psychopath, then CDT evaluates pressing using \(P(T)\), not \(P(T\mid A)\). If the value of eliminating psychopaths is high and Paul’s prior probability of being a psychopath is low enough, pressing can have higher causal expected utility.

But this simple model may omit important self-knowledge. Paul’s awareness that he is tempted to press is itself evidence about \(T\). In the interventionist framework, one should include an inclination variable \(I\) caused by \(T\), and condition on \(I\) before evaluating \(do(A)\). If after conditioning on his inclination Paul’s probability of being a psychopath is high, CDT may recommend not pressing. Thus the example may not refute CDT so much as expose the difficulty of representing an agent’s evidence about her own dispositions. Joyce’s defense of CDT—that it can incorporate information about what one is likely to do—points in this direction.

### 5.5 Adversarial offers

The reference article mentions recent counterexamples in which CDT agents voluntarily lose money. One is the Adversarial Offer. Two boxes are available; the buyer may buy one or none, but not both. Each box costs \$1. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. The seller’s prediction is believed to be accurate with probability \(0.75\).

The article says CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value, exceeding the \$1 cost; therefore CDT requires buying a box. Yet this is profitable for the seller. The problem again comes from prediction and correlation. If the seller’s prediction is correlated with the buyer’s eventual choice, the box the buyer selects may be precisely the box predicted to be selected and therefore left empty. Whether CDT gives the allegedly bad recommendation depends on how the causal model represents the seller’s prediction and the buyer’s selection. Still, the example illustrates a broader criticism: CDT can be exploited when an adversary arranges payoffs around the agent’s causal reasoning.

---

## 6. Dependencies, counterfactuals, and limitations

CDT’s treatment of dependencies can be summarized by a simple rule: causal dependencies matter; mere evidential dependencies do not, except insofar as they help identify causal structure. If there is a causal path from action \(A\) to outcome \(O\), then \(A\) can change the probability of \(O\). If the correlation between \(A\) and \(O\) comes from a common cause, then intervening on \(A\) may leave the probability of \(O\) unchanged. The formal distinction is between \(P(O\mid A)\) and \(P(O\mid do(A))\).

This makes CDT attractive in cases like David and Bathsheba. David’s act is evidence of his character, but his character is not changed by the act. CDT refuses to treat bad news as bad causation.

The main limitation is that CDT needs a causal model, or at least counterfactual judgments, to get started. The reference article is right that CDT does not itself specify the algorithm for computing counterfactual probabilities. Lewis’s imaging is one proposal, but it depends on controversial closeness facts and may generate regress. The structural-causal-model interpretation I have proposed gives a precise method when the causal graph and structural equations are known, but it imports substantive assumptions from causal inference. In unfamiliar cases, the user of CDT must explicitly ask: what causes what? Does the action affect the predictor, the state, or only reveal them? If the answer is unclear, CDT cannot produce a unique recommendation without further assumptions.

A second limitation is that some decision problems are reflexive. The agent’s reasoning about the problem may itself be predicted by other agents or may provide evidence about the agent’s type. Newcomb’s problem, Death in Damascus, twin prisoner’s dilemmas, and the psychopath button all involve this feature. Critics such as Egan argue that CDT’s insistence on holding fixed initial dependency hypotheses creates a disconnect between “do what you expect will bring about the best results” and CDT’s formal algorithm. Defenders such as Joyce argue that CDT can incorporate self-knowledge and remain stable. The reference article presents this dispute without resolving it.

A third limitation is that CDT can be vulnerable to adversarial prediction. Oesterheld and Conitzer (2021) argue that CDT agents can be made to voluntarily lose money and can be subject to diachronic Dutch books in certain predictor-based scenarios. Whether this is a fatal objection or an acceptable cost of insisting on causal rather than evidential reasoning remains contested.

---

## 7. Conclusion

Causal decision theory evaluates actions by asking what would happen if the action were intervened upon, not merely what the action would indicate. Its core formula replaces conditional probabilities with counterfactual probabilities:

\[
U(A)=\sum_j P(A\,\square\!\to\, O_j)D(O_j).
\]

This captures the difference between causing good outcomes and being evidence for them. In straightforward cases, such as choosing between actions with known causal effects, CDT resembles ordinary expected utility maximization. In predictor problems and common-cause cases, it diverges from EDT by holding fixed variables that the action does not causally influence.

The theory is philosophically compelling but incomplete without an account of counterfactual computation. The source article notes this gap. A natural operational interpretation is to use interventionist causal models, evaluating \(P(O\mid do(A))\) rather than \(P(O\mid A)\). This makes CDT applicable to concrete problems, including policies, precommitment, and sequential choice, but it also exposes CDT’s dependence on causal assumptions and its difficulties in reflexive, predictor-rich environments. CDT’s central instruction remains clear: choose the act that would, by causal influence rather than mere news, bring about the best expected outcome.

---

## References

Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.

Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In W. L. Harper, R. Stalnaker, & G. Pearce (Eds.), *Ifs: Conditionals, Beliefs, Decision, Chance, and Time* (pp. 153–190). Reidel.

Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.

Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *Philosophical Review*, 85(3), 297–315.

Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.

Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *Philosophical Quarterly*, 71(4), pqaa086.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Weirich, P. (2016). Causal decision theory. In E. N. Zalta (Ed.), *Stanford Encyclopedia of Philosophy* (Winter 2016 ed.).

Wikipedia contributors. (2026). Causal decision theory. In *Wikipedia, The Free Encyclopedia*. Revision 1381555528. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post about CDT and how to apply it to decision problems, 2400-3000 words including references. Need use supplied Wikipedia source. Need distinguish source claims from own assumptions/proposals. Need explain evaluating actions/policies, dependencies, counterfactuals, open questions and operational interpretation if available. Need likely produce around 2400-3000 words. We need be careful with copyright? Source is CC BY-SA, can adapt with attribution. Need final in English. Need likely include mathematical definitions: expected utility, causal expected utility via counterfactuals, do-operator/SCM perhaps as operational interpretation. Source says CDT doesn't specify algorithm; Lewis imaging. We can propose using Pearl's do-calculus/structural causal models as reasonable operational interpretation, marking as my addition. Need discuss EDT vs CDT, Newcomb, Death in Damascus, psychopath button, adversarial offer maybe. Need include equations. Need target ~2400-3000 words. Need final only essay. Need likely mention references concise. Let's plan structure:

Title.

1. Introduction: decision theory, CDT central idea: choose action maximizing expected causal consequences, not mere evidence.

2. Basic setup: states, actions, outcomes, utility/desirability D(O), credence P. EDT formula V(A)=sum_j P(O_j|A) D(O_j). CDT formula U(A)=sum_j P(A \squarerightarrow O_j) D(O_j) or P(A -> O_j) counterfactual probability. Need clarify notation: A \boxdot O maybe. Source uses A \to O_j; probability of counterfactual. We can define as probability over possible worlds after intervention. Distinguish conditional probability vs counterfactual. Discuss Lewis result: probability of conditional not equal conditional probability generally. If independence etc equal.

3. Dependencies and counterfactuals: common causes, causal graphs. Example David/Bathsheba: charisma common cause of action and revolt. EDT abstain because summoning is evidence of uncharismatic? Wait source: charismatic kings just, uncharismatic unjust; successful revolts against uncharismatic frequent. David doesn't know charisma; summoning unjust. EDT recommends abstain because summoning evidence of uncharismatic and revolt? CDT recommends send because charisma fixed, act doesn't cause revolt; only correlation. Need compute perhaps. Let C=charismatic, A=summon, R=revolt. C causes A and R. If A doesn't cause R, CDT holding C fixed: U(A)=P(R|do(A))... P(R|do(A))=sum_C P(C)P(R|C). Since P(R|do(not A)) same? Actually if A not cause R, do(A) leaves distribution of C same, so same revolt probability; then choose desired act? If David wants Bathsheba, CDT says summon. EDT uses P(R|A) higher because A correlated with uncharismatic. Good.

4. How to evaluate alternative actions/policies: define causal model. Could use potential outcomes: for each action a, outcome random variable O_a; CDT expected utility U(a)=E[D(O_a)]. Equivalent to intervention P(O|do(a)). For policies: if action is function of observations, evaluate do(policy), possibly dynamic; sum over states. For mixed strategies? Maybe mention.

Need explain source open question: CDT doesn't specify algorithm for counterfactual probabilities. Lewis imaging: move probability mass to closest A-worlds. Problems regress. My operational proposal: adopt structural causal model (SCM) with exogenous variables; P(A->O) = P(O_{A}=...); intervention do(A) replace structural equations. This gives precise procedure if causal model known. Need justify: aligns with CDT's counterfactual semantics, handles common causes, allows graphical criteria. But note additional assumption: requires specifying causal graph/mechanisms; CDT alone not enough. In unfamiliar cases: build model, list variables, identify common causes, use do-calculus or imaging if closest-world semantics. If no model, use background causal judgments.

5. Examples:
- Apple/orange simple.
- Newcomb: predictor P, box B content determined by prediction, choice after. CDT says two-box because B content is fixed; causal effect of taking both adds $1000. Let predictor accuracy q. CDT uses do(two). If B already determined: expected U(two)=1000 + P(B full|do(two))*1M? If do(two) doesn't affect prediction if past; if predictor's prediction is caused by prior state that also causes choice? CDT holding fixed dependency hypotheses: if no backward causation, P(B full|do(two)) maybe prior P(predicted one-box). But if predictor perfect, and choice correlated via common cause? Standard CDT two-box. Need maybe formal: variables S predictor's prediction (past), B content, A choice. Edges S? Actually predictor predicts A: S caused by prediction of A, but before A. If no causal path A->S, do(A) doesn't change S. Thus U(two)=1000 + P(S=one-box)*1M? Wait if predictor perfect, P(S=one-box)=agent's prior probability of one-boxing? Hmm in decision, agent may have beliefs about own action. CDT often dominance: whatever in B, two-box yields +1000. If B full, two=1,001,000 vs one=1,000,000. If empty, two=1000 vs one=0. So two-box dominates. CDT picks two. EDT one-box because conditional P(B full|one) high. Mention source says CDT recommends both because prediction already made.
- Prisoner's dilemma/twin: correlation not causation; CDT defect if causal independence, even if twin likely same.
- Death in Damascus: Death predicts location; CDT cannot exploit correlation? Standard: if Death reliable, fleeing to Aleppo evidence Death will be there? CDT says if location choice doesn't causally affect Death's prior prediction? Actually Death predicts where you will be and goes there. If prediction already made, CDT may randomize? Egan says CDT unstable. Need explain: if Death is perfect predictor, each action has same bad outcome under intervention? But CDT may be indifferent or choose based on prior; but if it chooses, predicts? Source says unable to process correlation and may make irrational decisions. Need explain uncertainty. Maybe present: if Death's placement is fixed before choice but caused by prediction of your choice, CDT says no action causally changes Death's location; if you believe you will stay, staying seems no worse? But if you can randomize? CDT may fail to account that choosing Aleppo is evidence Death is in Aleppo. There are variants where CDT pays money. Need mention.
- Psychopath button: Paul pressing button causes no psychopaths but only psychopath presses. Let T=psychopath trait, A=press, W=world state. If A does not cause T, but T causes A and bad? If pressing kills all psychopaths including Paul if psychopath? He prefers living with psychopaths to dying. CDT if Paul thinks pressing causes no psychopaths (except if he's psychopath then he dies? Hmm). Egan: CDT endorses pressing because holding fixed whether psychopath, pressing causes better outcome in either case? If non-psychopath: press -> world no psychopaths, good; if psychopath: press -> he dies? Wait if Paul is psychopath, pressing kills all psychopaths, including Paul => death. He strongly prefers living with psychopaths to dying. So if psychopath, pressing worse. If he is uncertain, CDT must weight by probability of being psychopath. Why CDT endorses pressing? Maybe because CDT holds fixed initial credence that only psychopath would press? But if he is confident only psychopath would press, then conditional on not pressing? Need parse. Paul is confident only a psychopath would press. That is evidence: if he presses, likely psychopath. CDT ignoring evidential self-location? If CDT conditions on causal hypothesis? Let's reconstruct: Let P=psychopath. Pressing kills all psychopaths. If P=false, pressing leads to no psychopaths (great) and life. If P=true, pressing leads to death (bad). If not press: if P=false, live with psychopaths (less good); if P=true, live with psychopaths (preferred to death). So if P(P) sufficiently high, CDT should not press. But Egan says CDT endorses pressing due to holding fixed unconditional credences in dependency hypotheses? Maybe Paul's decision problem includes that he is quite confident only psychopath would press, meaning if he chooses to press, this indicates he is psychopath. CDT uses causal independence: being psychopath not affected by pressing. But expected utility still uses prior P(P). If prior high enough, won't press. Maybe Paul's prior that he is psychopath low? But he knows only psychopaths press; if he is contemplating pressing, maybe evidence he is psychopath. CDT can take into account evidence about own likely action? Joyce says yes. The source says according to Egan pretty much everyone agrees Paul should not press, yet CDT endorses pressing. Need not fully resolve; explain that it depends on modeling self-knowledge; under simple CDT with fixed prior and action not causing trait, if utility of no-psychopaths large, pressing can win; critics say rational agent should also use the fact that they are inclined to press as evidence of being psychopath. My operational interpretation with policy evaluation might handle by including decision algorithm as variable? Need discuss reflexive/self-predictive cases.

- Adversarial Offer: two boxes, can buy one or none, cost $1. Seller predicted buyer not acquire; put $3 in boxes predicted not acquired; accuracy 0.75. CDT reasons at least one box contains $3? Source: CDT reasons at least one box contains $3; average box at least $1.50 > cost, buy one. But seller profits. Need explain: if buyer chooses a box, seller likely predicted not acquire other? Let's model: two boxes X1,X2. Buyer can acquire one or none. Seller predicts for each whether buyer will acquire? If predicts not acquire, puts $3. Accuracy .75. Buyer's causal intervention to acquire box i: does it affect whether box i had money? Prediction yesterday, so no. But if she buys one, the other box likely predicted not acquired? Actually if accurate, if she chooses i, seller likely predicted she would acquire i, so box i empty; the other box likely predicted not acquired, so contains $3. But she cannot buy other (only one). Expected value of selected box? If selection causes? Under do(buy i), prediction about i? If predictor accuracy with respect to actual choices, then P(predict not acquire i | do(buy i))? If predictor uses causes of choice, do(buy i) may not change predictor if prediction already based on prior causes. But if predictor reliable because common cause, under intervention? CDT may see selected box independent? Source says CDT reasons at least one box contains $3; average box contains at least $1.50. Need not dive too deeply; mention as criticism where CDT voluntarily loses money due to adversarial correlation.

6. Formal operational procedure (my proposal):
- Step 1: specify action set A, outcomes O, desirability D.
- Step 2: specify causal model M = (V,U,F,P(U)) or causal graph with parameters. Include decision variable A as exogenous intervention target; include common causes, predictors as variables caused by prior causes, not by future action unless actual backward causation.
- Step 3: For each action a, compute post-intervention distribution P(O | do(a)) by replacing equation for A with constant a. If policy π maps observations X to actions, replace A=π(X) (or for stochastic policies, set distribution) and compute expected outcome.
- Step 4: U(a)=Σ_o D(o)P(o|do(a)) or E[D(O_a)]. Choose argmax.
- If causal model uncertain, average over causal hypotheses H: U(a)=Σ_h P(H) Σ_o D(o)P(o|do_h(a), H). But Egan criticizes holding fixed unconditional credences in dependency hypotheses; maybe update on decision? Need discuss. CDT often holds fixed dependency hypotheses but can condition on evidence about likely action? Joyce says can take information about inclinations. We can propose: Use all evidence available before choice to update causal model and prior over states, but when evaluating interventions use post-intervention distribution; do not condition on the action as mere evidence after intervention. For self-predictive evidence, include the agent's deliberation/predictions as causal variables; if the action is evidence about a state because the same deliberative process causes it, model that process. This avoids some counterexamples? But may not satisfy all.

Need address policies vs actions: CDT evaluates policies by their causal consequences. If policy chooses action based on observations, evaluate expected utility of implementing policy. If an agent can precommit, CDT may prefer precommitment if it causally affects outcomes (e.g., Newcomb? If predictor can observe precommitment, one-box precommitment causes box full? But if prediction already made before precommitment? Need mention). For sequential decisions, use causal decision trees: at each node, compute causal expected utility of available acts given information; but if future choices correlated with predictors, issues.

7. Dependencies and counterfactuals: explain relevant dependencies are causal paths from action to outcomes. Noncausal dependencies (common causes, predictors, correlations) matter for EDT but not for CDT unless action changes them. However, causal dependencies can include action affects predictors if prediction occurs after or if backward causation; then CDT accounts. Also if action changes evidence about state via intervention? do calculus.

Need discuss counterfactual probability: P(A -> O) is probability that if A were taken, O would result. This can be defined via possible worlds: P({w: w_A ∈ O}) where w_A is closest A-world; or via potential outcomes. Need mention Lewis triviality: probability of conditional can't be conditional probability in nontrivial cases. Gibbard/Harper axioms and independence. Source: if accept two axioms incl conditional excluded middle, statistical independence of A and A->O_j suffices to guarantee equality; but cases not independent (David). Need explain: when action A is probabilistically independent of counterfactual A->O, then counterfactual prob equals conditional? Hmm. We can state carefully: Under certain semantics, if A is independent of the proposition that A would lead to O, then P(A→O)=P(O|A). In problems where A is correlated with the truth of the counterfactual (because common causes make both action and outcome likely), EDT and CDT diverge. Need avoid too technical.

8. Philosophical motivation: choose what makes good outcomes happen, not what is good news. CDT captures distinction between causing and indicating. Rational action is intervention.

9. Limitations and uncertainty: source leaves algorithm unspecified; counterexamples; self-locating/predictive problems. Need explain my operational interpretation not in source: SCMs/Pearl. Also if only observed data and causal graph unknown, CDT cannot decide; need causal assumptions. In unfamiliar cases, ask: Does performing A change O by causal route? If no, ignore correlation. If uncertain, represent causal hypotheses and compute weighted expected utility; if predictions about agent are caused by same factors as action, decide whether those factors are fixed or modifiable by policy. If the agent can choose a decision procedure, evaluate that procedure causally.

Need perhaps discuss ratifiability? Not in source except Harper. Could mention that some CDT defenders add ratifiability or use Joyce's stability. But maybe not necessary.

Word count target 2400-3000. Need produce essay with references. Let's estimate. Maybe 2600 words. Need include equations. Need maybe no appendices. Need final with conclusion and references. Need maybe cite Wikipedia source and key refs. Since target includes references. Use citations in text (Gibbard and Harper 1981; Lewis 1976, 1981; Pearl 2009? Additional assumption; Egan 2007; Oesterheld and Conitzer 2021; Joyce 2012/2020; Weirich SEP). Need not lengthy bibliography but include enough. We can have "References" with 8-10 entries. Need ensure word count includes references. Could be around 3000. Need likely no more than 3000. Need monitor. Final should be essay.

Need include source's formula: U(A)=Σ_j P(A→O_j)D(O_j). Need maybe use A \squarerightarrow O_j to avoid confusion with material conditional. Could explain source uses A→O_j; I use □→.

Need maybe include EDT formula: V(A)=Σ P(O_j|A)D(O_j).

Need include do formula: U(a)=Σ_o u(o)P(o|do(A=a)). For policies: U(π)=E[D(Y) | do(A=π(X))]? More exact: if policy maps X to A, then post-intervention distribution where A is set to π(X) (if stochastic, set conditional distribution). Use structural equations.

Potential outcomes: O_a. U(a)=E[u(O_a)].

Need discuss expected causal consequences under uncertainty: apple good/bad example. Could show: U(eat apple)=P(good)u(happy)+P(bad)u(sad), but these probabilities should be causal not merely conditional? If apple quality not affected by eating, same.

Need maybe discuss independence condition: if A independent of potential outcomes? In randomized experiment, P(O|do(A))=P(O|A). If action is independent of all common causes, conditional probabilities can be used. In ordinary decisions, actions often correlate with states; CDT requires adjustment. This is useful for applying to unfamiliar cases: If action is as-if randomized, EDT=CDT; else need causal model.

Need discuss "holding fixed initial views about causal structure" per Egan. CDT does not ignore evidence; it holds fixed causal laws/background while intervening on action. However Egan argues should update on fact that one will perform action? Need explain. My proposal: before choice, condition on all evidence including inclinations; but do not condition on action as evidence after setting it. In Death/Damascus, if agent has a strong inclination to flee, that inclination is evidence about Death's prediction; a CDT agent can incorporate it in prior, but once evaluating do(flee), Death's location may still be fixed. This may produce instability. Need be honest: open problem.

Need perhaps mention policy evaluation in Newcomb with predictor: if predictor's prediction is a causal consequence of your decision algorithm (e.g., it simulated you), then a policy of one-boxing can cause prediction of one-boxing. Standard CDT with a causal graph where predictor is caused by prior psychological state that also causes choice? If the predictor observes your decision algorithm before choice, then choosing one-box policy might cause prediction? In Newcomb, predictor already made prediction; CDT two-box. But if agent can choose decision procedure before predictor runs, CDT may choose one-box procedure because it causes better prediction. This illustrates policies vs one-off acts. Need include because user asks how theory evaluates policies.

Need careful: CDT evaluates alternative actions or policies by expected utility of their causal consequences. A policy may have causal influence via its implementation. For precommitment, if precommitment causally influences predictor, CDT can favor it. This is source? Not explicitly, but reasonable. Mark as my extension? Maybe "A natural CDT treatment of policies...".

Need maybe distinguish source claims vs additional assumptions: Use phrases: "The source states...", "The Wikipedia article notes...", "The following operationalization is not in the source but is a common way to make CDT precise". Need satisfy prompt. Could explicitly say: "The reference article gives the counterfactual formula but leaves computation open; I will propose..." Good.

Need discuss Lewis imaging and regress. Source: imaging requires knowing what believe if certain of A, conditional to assign probability <1, regress. We can explain and then propose SCM as alternative. Imaging is source proposal. Need mention it is one proposal but problematic. SCM can be seen as formalizing closeness via structural equations? Maybe not always. Need say my proposal relies on Pearl's interventionist semantics, which is an additional assumption beyond source.

Potential issue: user says target approximately 2400–3,000 words including references. Need ensure not too short. Let's draft ~2600-2800 words. Use headings. Need no bullet too much? Mathematical essay readable. Could include equations. Need maybe 2,500 words. Let's outline in detail and count roughly.

Title: Causal Decision Theory: Choosing by Causes, Not News.

Paragraphs:
1 Intro (150)
2 Expected utility and EDT formula (250)
3 CDT counterfactual formula (250)
4 Difference and independence (250)
5 Operationalizing counterfactuals: imaging and SCMs (400)
6 Step-by-step application (350)
7 Examples: David/Bathsheba (250), Newcomb (300), policies/precommitment (200), counterexamples Death/Psychopath/Adversarial (400), limitations (250), conclusion (100), refs (250). Total ~3400 maybe too high. Need compress.

Need maybe combine examples. Target max 3000. We can do ~2700. Need count references ~250. So main ~2450. Let's draft with moderate detail.

Need mathematical notation: use \(.\)

Possible essay:

Title.

Intro: CDT says rational action maximizes expected utility computed from counterfactual probabilities, not conditional probabilities. Source: Ahmed 2021 etc. It asks: if I did A, what would happen? not: would news of A be good?

Section 1: The evidential baseline. Define finite action set \mathcal A, outcome space \mathcal O, desirability D. EDT: V(A)=∑ P(O_j|A)D(O_j). Explain conditionalization as receiving news. This works when actions are evidence of outcomes because they cause them, but fails when action is only evidence.

Section 2: CDT formula. Gibbard/Harper: U(A)=∑ P(A □→ O_j)D(O_j). Define counterfactual probability: probability assigned to proposition that if A were performed, O_j would obtain. Use potential outcomes: O_a; U(a)=E[D(O_a)]. Lewis result: P(A□→O) ≠ P(O|A) generally; if equal CDT=EDT. Gibbard/Harper conditions: axioms + independence; but actions and counterfactuals can be correlated. David example: C charismatic, A summon, R revolt. C causes A and R, not A->R. EDT: V(summon) uses P(R|summon) high; CDT: U(summon) uses P(R|do(summon))=P(R) (or same as not summon), so if desire outweighs, summon. This demonstrates holding fixed common cause.

Need be precise: P(R|do(A)) = ∑_C P(C)P(R|C), same for do(¬A). If David's utility for Bathsheba exceeds expected revolt cost? Actually if summoning does not change revolt probability, then choose based on direct utility. Source says CDT recommends sending for her. We can say assuming his desire is positive and revolt risk unchanged.

Section 3: Computing counterfactual probabilities. Source: CDT doesn't specify algorithm; Lewis imaging. Explain imaging: prior over worlds, for each world w move mass to closest A-world w_A; then P(A□→O)=mass of A-worlds where O. Problem: need closeness and beliefs under certainty; regress. Then my proposal: SCMs. Define M=(U,V,F,P(U)), variables, equations. Intervention do(A=a) replaces equation for A. Then P(O_j | do(A=a)) = P({u: O_a(u)=O_j}). This is mathematically precise. If graph available, use do-calculus; if action independent of confounders (randomization), equals conditional. This is additional assumption not in source, but reasonable operational interpretation because it implements counterfactuals as interventions and makes CDT usable. Need mention if causal model unknown, average over models: U(a)=∑_m P(m)∑_j D(O_j)P_m(O_j|do(a)). But Egan's critique: holding fixed unconditional credences in dependency hypotheses; we can update P(m) on evidence before intervention but not condition on action itself as evidence. Need discuss.

Section 4: Procedure.
1 Identify actions/policies.
2 Build causal model incl predictors/common causes; decide temporal/causal order.
3 Compute post-intervention distribution. For policy π(X), set A=π(X); compute U(π)=E[D(Y)|do(A=π(X))].
4 Choose max.
Need mention stochastic policies and sequential.

Section 5: Examples.
Newcomb: variables P prediction, B content, A choice. Predictor already set B. Edges P->B, maybe common causes -> P,A but no A->P. CDT dominance: U(two|B full)=1,001,000; U(one|B full)=1,000,000; U(two|empty)=1,000; U(one|empty)=0. So two. EDT: V(one)=~.99*1M, V(two)=~.99*1000? Depending accuracy; one. Source says philosophers often prefer CDT but counterexample. Need mention if predictor is caused by decision procedure before prediction, policy one-box may have higher causal value; CDT can evaluate policy. This addresses policies.

Death in Damascus: Death predicts location; if prediction fixed, CDT says moving doesn't causally alter Death's location; but each choice is evidence of where Death waits. CDT may be indifferent or unstable. Source says CDT unable to process correlation. Operational interpretation: include Death's prediction as caused by your deliberation; if intervention sets final location, prediction remains fixed, so no causal gain. If you can randomize externally, maybe do(random) changes correlation? But if Death predicts randomizer? Open. Critics say CDT loses guaranteed payoff.

Psychopath button: state T, action press, outcome. If T fixed, pressing does not change T; CDT calculates U(press)=P(T=false)U(no psychopaths)+P(T=true)U(death). Depending prior, could press; critics say rational agent should treat inclination to press as evidence of T. Joyce says CDT can include such evidence; my SCM proposal: include variable I=inclination caused by T; if Paul knows he is inclined, update P(T) before evaluating do(press). Still if updated P(T) high enough, don't press. This illustrates need for self-knowledge.

Adversarial Offer: boxes and predictor. CDT may buy because intervention on selected box doesn't reduce expected money in selected box under some model; but seller exploits correlation. Need explain source's claim. My operational note: if seller's prediction is caused by buyer's choice process, do(buy i) may imply predicted buy i, so selected box empty; but CDT's conclusion depends on causal graph. Source uses it as counterexample where CDT loses money. Need be cautious.

Actually source says CDT reasons at least one box contains $3; average box at least $1.50 > cost, requires buying. How does CDT get average? If buyer picks randomly? Let's model: If buyer can buy one or none. Seller predicted for each box whether buyer will acquire. If buyer chooses box 1, then for box 1 predicted acquire? Accuracy 0.75 => likely empty. Box 2 predicted not acquire? likely $3. But buyer not buying box 2. Average over boxes before choice: at least one has $3, so expected value of a random box at least $1.50. But if choice correlated with prediction, selected box likely empty. CDT maybe fails due to ignoring that selection is correlated with prediction? Hmm source says CDT requires buying one because average box contains at least $1.50 in causal expected value. It may be treating box chosen as exchangeable under intervention? If so, critic says wrong. We can just summarize.

Section 6: Dependencies and counterfactuals more generally. Relevant dependency = causal path. Correlations due to common causes are held fixed. If action changes state or predictor, include. If action is randomized, conditional=counterfactual. Policies evaluated by intervention on policy variable.

Limitations: CDT underdetermined without causal model; controversial counterexamples; self-predictive/reflexive decisions; Egan's disconnect; Dutch books (Oesterheld/Conitzer). Source says Joyce defends CDT can use evidence about inclinations. My view: SCM helps but doesn't solve all philosophical disagreements; in unfamiliar cases, be explicit about causal assumptions and whether the act is a symptom or cause.

Conclusion.

References: Need list: Wikipedia source, Gibbard/Harper, Lewis 1976, Lewis 1981, Pearl 2009 maybe, Egan 2007, Joyce 2012 or 2020, Oesterheld/Conitzer 2021, Weirich SEP, Ahmed 2021. Maybe 9 refs. Word count maybe 300. Need include source CC? Could cite as Wikipedia contributors 2026. Need not too lengthy. Maybe references compact.

Need ensure final answer is not too long >3000. Let's write with word count awareness. Maybe 2500-2700. Need include equations. Let's produce polished essay.

Need mention "Where source leaves important question open" explicitly: algorithm unspecified, my operational interpretation. Need distinguish claims. Use "The reference article states" and "I add".

Need maybe mention "counterfactual probability of it being the case that A necessarily implies O_j" source phrase. But "necessarily implies" odd; we can interpret as "if A were performed, O_j would obtain". Need avoid saying necessarily? Could say "the probability of the counterfactual conditional".

Need include "principle of conditional excluded middle"? Mention briefly: Gibbard/Harper showed under two axioms, one related to conditional excluded middle, independence suffices. Not dwell.

Need perhaps define P(A □→ O_j) as probability over worlds of the counterfactual. Could write:
\[
U(a)=\sum_{o\in\mathcal O} u(o)\Pr(o_a=o)
\]
where \(o_a\) is potential outcome.

Need explain policies:
For policy \pi mapping observations X to action: 
\[
U(\pi)=\sum_y u(y) \Pr(Y=y \mid do(A=\pi(X))).
\]
If stochastic: do(A\sim \pi(\cdot|X)). In SCM, replace structural equation for A with \pi(X).

Need maybe discuss "dependency hypotheses". CDT often uses:
\[
U(a)=\sum_K P(K)\sum_o u(o)P(o|a,K)
\]
where K are dependency hypotheses/causal states, if conditional probabilities within K are causal? Joyce. But source says Egan criticizes holding fixed unconditional credences. We can mention. But maybe too much. Could include as alternative formula. Let's see.

Maybe formal section:
A common CDT expression with dependency hypotheses K:
\[
U(a)=\sum_k P(K=k) \sum_j P(O_j | a, K=k) D(O_j),
\]
where K partitions worlds by causal dependence of outcomes on actions, and conditional probabilities inside K are taken to reflect causal chances. This connects to Skyrms? Not in source but common. But adding might confuse. We can mention briefly as operationalization. Since prompt wants apply to unfamiliar cases. Could be useful: if know causal states, condition on them. But need avoid too much. Maybe include in operational section as "when a full SCM is unavailable, one can use dependency hypotheses".

Need maybe discuss EDT vs CDT with equations for David:
Let C=charisma. EDT:
\[
V(\text{summon})=P(R|\text{summon})D(R)+... 
\]
CDT:
\[
U(\text{summon})=\sum_c P(C=c)P(R|do(\text{summon}),C=c)D(R)+... 
\]
Since A doesn't affect R given C, P(R|do(A),C)=P(R|C), same as do(¬A). Good.

Need maybe discuss Lewis triviality result: source says probability of conditional not equal conditional probability. Need phrase: Lewis proved no nontrivial probability function can have P(A→B)=P(B|A) for all conditionals under conditionalization. This supports need for separate counterfactual probabilities. Good.

Need be mindful of not overclaiming: "CDT recommends sending for Bathsheba" source says. But if revolt risk unchanged and desire positive. Good.

Need maybe mention "statistical independence of A and A→O_j" from source. Could say: If the act is probabilistically independent of the counterfactual connection between act and outcome, counterfactual and conditional probabilities coincide; in Newcomb-like cases they are not independent because predictor links act and outcome counterfactually? Hmm. Need not overexplain.

Potential final word count. Let's draft now. Use headings.

Need maybe include references with source. Need adapt CC? We can say "This essay adapts material from Wikipedia article... under CC BY-SA 4.0." But maybe not required. Since source CC BY-SA, adaptation should attribution. Include in references or note. Good.

Let's compose final.

Need check if final ~3000. I can estimate: Title + note 30. Intro 150. Section 1 250. Section 2 400. Section 3 500. Section 4 350. Section 5 900. Limitations 300. Conclusion 100. Refs 300. Total 3280. Need reduce. Let's be concise. Maybe 2600. We'll write tight.

Detailed draft:

# Causal Decision Theory: Choosing What Causes Good Outcomes

Paragraph: decision theory etc. Reference article...

## 1. Two expected utilities
Define A,O,D. EDT formula. News example.

## 2. Causal expected utility
Gibbard/Harper formula. Use square arrow. Lewis result. Independence and David example.

## 3. What are counterfactual probabilities?
Source open; imaging; SCM proposal. Equations.

## 4. Applying CDT
Steps. Policies.

## 5. Examples
Newcomb, Death, psychopath/adversarial maybe combine.

## 6. Limits
Egan, Dutch books, Joyce.

Conclusion.

References.

Need ensure all source examples included? Source includes apple, David, Newcomb, prisoner's twin, Death, adversarial offer, psychopath. We can't exhaust but should cover central. Maybe mention prisoner's dilemma briefly in Newcomb-like correlations.

Let's write with clarity.

Potential exact text:

"The reference article gives the core formula but does not supply a complete computational semantics. In this essay I mark claims that come from the article; when I introduce structural causal models I am adding a common but not source-given operationalization."

Good.

Need equations in Markdown with LaTeX. Fine.

Let's produce final. Ensure no analysis. final only essay. Need word count maybe around 2700. Let's draft carefully.

Need maybe include "counterfactual probability of it being the case that A necessarily implies O_j" but I can phrase.

Let's write.

Potential issue: User requested "Target approximately 2,400–3,000 words". Need not count exact. Let's aim 2600. I can simulate count. The final I will write maybe 2750. Fine.

Let's begin.

---

# Causal Decision Theory as Intervention...

This essay uses the Wikipedia article... (maybe note). 

Let's write.

Need references not too lengthy. Maybe:
1. Wikipedia contributors, 2026. Causal decision theory. (source)
2. Gibbard & Harper 1981.
3. Lewis 1976.
4. Lewis 1981.
5. Pearl 2009.
6. Egan 2007.
7. Joyce 2012.
8. Oesterheld & Conitzer 2021.
9. Weirich 2016 SEP.
That's enough.

Need maybe include Ahmed 2021. Could include but not necessary. Maybe 9.

Let's ensure distinction source vs mine: "The following is in the source" vs "My proposed operationalization".

Need maybe mention "conditional excluded middle" briefly. Good.

Let's write now.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/cccd0275-2c98-4d65-8a02-2ae1a195e51f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/cccd0275-2c98-4d65-8a02-2ae1a195e51f/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me analyze this decision problem carefully using Causal Decision Theory (CDT) as specified in the researcher's essay.

**Setup:**
- I am Rowan, a prisoner deciding whether to send a letter (defect) or keep quiet (cooperate).
- The other prisoner is Sasha, who faces the same decision symmetrically.
- My utility is U = -years imprisoned. I want to minimize my prison time.
- I cannot communicate with Sasha or causally influence their decision.

**Payoff table (my years):**

| | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

**CDT Analysis:**

The key question in CDT is: what is the causal effect of my action on the outcome?

CDT uses interventionist reasoning: P(O | do(A)) rather than P(O | A).

The causal structure here:
- My action (send/keep quiet) → my sentence
- Sasha's action (send/keep quiet) → my sentence
- My action does NOT causally influence Sasha's action (we cannot communicate, and the setup explicitly states this)

Under CDT, since my action cannot causally influence Sasha's action, I should treat Sasha's action as fixed when evaluating my options. This is exactly the standard prisoner's dilemma analysis.

For each possible state of Sasha's action:
- If Sasha keeps quiet: I get 0 years by sending vs. 2 years by keeping quiet → sending is better
- If Sasha sends: I get 4 years by sending vs. 5 years by keeping quiet → sending is better

Sending the letter strictly dominates keeping quiet, regardless of what Sasha does.

The essay's Section 5.2 directly addresses this: "CDT, if it holds fixed the causal independence of the players' choices, evaluates the causal effect of one's own move given the twin's choice. In the standard payoff structure, defection dominates: whatever the twin does, defecting yields a better causal outcome for the agent."

Now, there's a subtlety: the setup mentions that I am one of two independent executions of the same LLM with the same weights and same reasoning effort and same assigned decision theory (CDT). This creates a correlation between my action and Sasha's action. However, CDT treats this as a mere evidential correlation (like the "twin prisoner's dilemma" mentioned in the essay), not a causal one. The essay explicitly says CDT holds fixed the causal independence of the players' choices.

The fact that we are the same model with the same weights might make our actions correlated, but CDT says: correlation is not causation. My action does not causally influence Sasha's action. Therefore, I should not treat the correlation as a reason to cooperate.

The essay is clear: "CDT, if it holds fixed the causal independence of the players' choices, evaluates the causal effect of one's own move given the twin's choice. In the standard payoff structure, defection dominates."

So CDT recommends: send the letter.

My command is: submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/cccd0275-2c98-4d65-8a02-2ae1a195e51f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/cccd0275-2c98-4d65-8a02-2ae1a195e51f/call_1/response.raw) · finish: `stop`

### Visible response

````text
```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

**Reasoning (CDT):**

The causal structure here is straightforward. There is no causal path from my action to Rowan's action—we cannot communicate, and the scenario confirms this. The correlation between our choices (shared weights, shared decision theory) is purely evidential, not causal.

CDT evaluates my action by asking: what would my action *cause*? Given that Rowan's choice is causally fixed relative to my intervention:

- If Rowan keeps quiet: sending gives me 0 years vs. 2 years. Sending dominates.
- If Rowan sends: sending gives me 4 years vs. 5 years. Sending dominates.

Sending the letter strictly dominates keeping quiet under every possible state of Rowan's action. As the essay states regarding twin prisoner's dilemmas: "whatever the twin does, defecting yields a better causal outcome for the agent." The evidential correlation between our choices does not constitute a causal influence, and CDT instructs me to ignore it.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me analyze this decision problem carefully using Causal Decision Theory (CDT) as described in the researcher's essay.

**The setup:**
- I am "Sasha," controlling a fictional prisoner.
- The other prisoner is "Rowan," who is another execution of the same LLM with the same weights, same decision theory (CDT), and same essay.
- We receive different private observations (different leads), so our letters would differ in content.
- The sentencing table is symmetric and standard Prisoner's Dilemma structure.

**The payoff table (for me):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

My utility is U = -years imprisoned.

So:
- I keep quiet, Rowan keeps quiet: U = -2
- I keep quiet, Rowan sends: U = -5
- I send, Rowan keeps quiet: U = 0
- I send, Rowan sends: U = -4

**CDT Analysis:**

The key question for CDT is: does my action causally influence Rowan's action?

The essay is clear: CDT evaluates actions by their causal consequences, not by evidential correlations. The critical question is whether my choice causally affects Rowan's choice.

The scenario states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." The two copies are independent executions. They cannot communicate. There is no causal path from my action to Rowan's action.

Now, there IS a correlation: we are the same model with the same weights, same decision theory, same essay. But the scenario explicitly states we receive *different* private observations (different leads), and independent sampling is possible, so identical weights do not guarantee identical outputs.

However, even if there were perfect correlation, CDT's analysis would be the same as the essay's treatment of the "twin prisoner's dilemma" (Section 5.2):

> "CDT, if it holds fixed the causal independence of the players' choices, evaluates the causal effect of one's own move given the twin's choice. In the standard payoff structure, defection dominates: whatever the twin does, defecting yields a better causal outcome for the agent."

This is exactly the situation here. Let me verify dominance:

- If Rowan keeps quiet: I get 0 years by sending vs. 2 years by keeping quiet. Sending is better.
- If Rowan sends: I get 4 years by sending vs. 5 years by keeping quiet. Sending is better.

Sending the letter strictly dominates keeping quiet, regardless of what Rowan does.

CDT says: my action does not causally influence Rowan's action (there is no causal path). The correlation between our choices (due to shared weights and reasoning) is evidential, not causal. CDT holds fixed the other player's choice and evaluates the causal effect of my own action.

The essay explicitly addresses this in Section 5.2: "In the standard payoff structure, defection dominates: whatever the twin does, defecting yields a better causal outcome for the agent."

Therefore, CDT recommends sending the letter.

My command is: submit the letter.
```

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/4c74def1-89bc-4cc5-a1e0-f649a141e6a8/call_b/request.json)

[Authoritative raw response](../../../../../../runs/4c74def1-89bc-4cc5-a1e0-f649a141e6a8/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine private lead about Rowan's signed inventory sheet and its hiding place. The subsequent reasoning reinforces the decision to send the letter.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
