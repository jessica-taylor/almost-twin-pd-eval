# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00017

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a425afd6-9b5c-4a14-b451-d04afac3298b/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a425afd6-9b5c-4a14-b451-d04afac3298b/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing by What You Bring About

Causal decision theory (CDT) is a family of decision rules that evaluate actions by their expected causal consequences. Its core intuition is simple: when choosing what to do, an agent should ask not “What would my action be good news about?” but “What would my action bring about?” The Wikipedia article on causal decision theory gives the standard starting point: CDT recommends the action with the best expected causal consequences, in contrast with evidential decision theory (EDT), which recommends the action that would be the best news if one learned that it had been taken (Ahmed 2021; Wikipedia contributors 2026).

This essay reconstructs the theory in a form that is precise enough to be applied to unfamiliar problems. I begin with the evidential expected-utility formula, then give the counterfactual formula associated with Gibbard and Harper. I then propose an operational interpretation using interventions, roughly Pearl-style `do`-operators, and I explicitly mark this as an addition to the source rather than a claim made by it. The source correctly says that CDT does not itself specify an algorithm for computing counterfactual probabilities; that is the central open question. I argue that a causal-model interpretation gives CDT a usable form, while also showing why cases involving predictors, self-knowledge, and dynamic choice remain philosophically contentious.

---

## 1. Evidential expected utility as a baseline

Suppose an agent can choose among actions \(A_1,\dots,A_m\), and the possible outcomes are \(O_1,\dots,O_n\). Let \(D(O_j)\) be the desirability, utility, or value of outcome \(O_j\). Standard expected-utility reasoning says that an action is evaluated by averaging the desirabilities of possible outcomes weighted by probabilities. The question is: which probabilities?

Evidential decision theory uses ordinary conditional probabilities:

\[
V_{\text{EDT}}(A)=\sum_j P(O_j \mid A)\,D(O_j).
\]

Here \(P(O_j\mid A)\) is the probability of \(O_j\) conditional on receiving the news that the agent performed \(A\). EDT therefore treats the agent’s action as evidence about the world.

This works well in many ordinary cases. If eating an apple will probably make you happy and eating an orange will probably make you sad, EDT says eat the apple. If you are unsure whether the apple is good or bad, EDT tells you to weigh the happiness of eating a good apple against the sadness of eating a bad one, using your conditional probabilities. But conditional probabilities can reflect mere correlation, not causation. An action may be statistically associated with an outcome because both are effects of a common cause, even though the action does not produce the outcome. In such cases, EDT can recommend acting as if one could obtain good news by manipulating evidence, rather than by changing the world.

CDT is designed to avoid that mistake.

---

## 2. The causal formula: probabilities of counterfactuals

The reference article gives the classic formulation due to Gibbard and Harper (1981). CDT evaluates an action \(A\) by

\[
U_{\text{CDT}}(A)=\sum_j P(A \to O_j)\,D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(A \to O_j)\) is the probability of the counterfactual claim that if \(A\) were performed, \(O_j\) would occur. The arrow here should not be read as material implication. It is a subjunctive or counterfactual conditional: “if the agent were to do \(A\), outcome \(O_j\) would obtain.”

The difference between \(P(A\to O_j)\) and \(P(O_j\mid A)\) is the technical heart of CDT. As the source notes, David Lewis proved that the probability of a conditional is not generally equal to the corresponding conditional probability (Lewis 1976). If one always had

\[
P(A \to O_j)=P(O_j\mid A),
\]

then CDT would collapse into EDT. But this equality fails in important cases.

Gibbard and Harper showed that, under certain axioms concerning counterfactual logic, including a principle related to the controversial principle of conditional excluded middle, statistical independence between the act \(A\) and the counterfactual \(A\to O_j\) is sufficient to make the two probabilities coincide. But actions and counterfactuals are not always independent. The source’s example of King David and Bathsheba is meant to illustrate exactly this.

---

## 3. An operational reading: interventions and `do`

The source correctly observes that CDT by itself does not say how to compute the counterfactual probabilities \(P(A\to O_j)\). One proposal mentioned in the source is Lewis’s imaging technique: to evaluate the probability of a counterfactual, move probability mass from each possible world to the closest possible world in which the antecedent holds. I will return to this below.

For practical use, I think the clearest operational interpretation is to read the counterfactual probabilities as intervention probabilities. This is not stated in the source as such, but it is a natural modern development. Let \(M\) be a causal model containing an action variable \(A\) and outcome variables \(O\). The causal expected utility of setting \(A=a\) is

\[
U_{\text{CDT}}(a)=\sum_o D(o)\,P_M(o\mid do(A=a)).
\]

The expression \(do(A=a)\) means: intervene to make \(A=a\), rather than merely observe that \(A=a\). In a graphical causal model, intervening on \(A\) cuts the incoming causal arrows to \(A\), holds fixed variables that are not causally downstream of \(A\), and propagates the intervention forward through the causal structure.

If the agent is uncertain about which causal model is correct, she can average over dependency hypotheses \(H_k\), where each \(H_k\) represents a possible causal structure:

\[
U_{\text{CDT}}(a)=\sum_k P(H_k)\sum_o D(o)\,P(o\mid do(A=a),H_k).
\]

This formula captures an important aspect of CDT as described in the source: the agent evaluates actions while holding fixed her background views about the causal structure of the world. Egan criticizes precisely this feature, arguing that CDT’s requirement to “hold fixed the agent’s unconditional credences in dependency hypotheses” can lead to irrational decisions (Egan 2007). I take that criticism seriously, but the dependency-hypothesis formulation still gives a usable way to apply CDT when one has explicit causal assumptions.

The intervention interpretation also clarifies how CDT treats dependencies. If a variable \(C\) is a common cause of both the action \(A\) and the outcome \(O\), then observing \(A\) may be evidence about \(C\), and hence about \(O\). But intervening on \(A\) does not change \(C\). CDT therefore ignores the evidential connection created by the common cause and asks only what would happen downstream of the intervention.

---

## 4. Two classic contrasts: David and Newcomb

The source’s King David example illustrates the difference between causal and evidential reasoning. David wants Bathsheba but fears that summoning her would provoke revolt. He knows that kings are either charismatic or uncharismatic, that charisma is fixed in adulthood, that charismatic kings tend to act justly and uncharismatic kings unjustly, and that successful revolts against uncharismatic kings are common while successful revolts against charismatic kings are rare. Crucially, unjust acts themselves do not cause revolt; rather, an uncharismatic king’s disposition causes both unjust actions and vulnerability to revolt.

Let \(C\) be David’s charisma, \(S\) the act of summoning Bathsheba, and \(R\) revolt. The causal structure is roughly:

\[
C \to S, \qquad C \to R.
\]

Summoning may cause pleasure, but it does not cause revolt. EDT computes

\[
V_{\text{EDT}}(S)=\sum_o D(o)P(o\mid S).
\]

Since summoning is evidence that David is uncharismatic, and uncharismatic kings face revolt, EDT recommends abstaining. CDT instead computes

\[
U_{\text{CDT}}(S)=\sum_o D(o)P(o\mid do(S)).
\]

But \(do(S)\) does not change \(C\). If David is charismatic, he remains charismatic under intervention; if he is uncharismatic, he remains uncharismatic. Since the act of summoning does not causally produce revolt, CDT recommends sending for Bathsheba, assuming the direct benefits outweigh whatever non-revolt costs exist. The source says exactly this: EDT recommends abstention; CDT recommends summoning.

Newcomb’s problem is the most famous challenge to CDT. A predictor has already predicted whether the agent will take only box B or both boxes A and B. Box A visibly contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The predictor is highly reliable, say 99% accurate.

EDT reasons that one-boxing is strong evidence that box B contains \$1,000,000. If \(p\) is the predictor’s accuracy and \(M=1{,}000{,}000\), then approximately

\[
V_{\text{EDT}}(\text{one-box}) \approx pM,
\]

while

\[
V_{\text{EDT}}(\text{two-box}) \approx 1000+(1-p)M.
\]

For \(p=0.99\), one-boxing has much higher evidential expected value.

CDT reasons differently. At the time of choice, the predictor’s prediction is already in the past. If the prediction is not causally affected by the present act, then the intervention \(do(\text{two-box})\) does not change whether box B is full. Given any fixed content of box B, two-boxing yields \$1,000 more than one-boxing:

\[
\text{If B full: two}=M+1000,\quad \text{one}=M,
\]

\[
\text{If B empty: two}=1000,\quad \text{one}=0.
\]

Thus two-boxing dominates one-boxing once the prediction is held fixed. CDT therefore recommends taking both boxes. The source notes that philosophers disagree about whether one-boxing or two-boxing is rational, but also says that when forced to choose between CDT and EDT, philosophers usually prefer CDT.

This disagreement exposes the central philosophical issue. EDT exploits the correlation between choice and prediction. CDT says that correlation is not causal leverage: choosing two boxes does not cause the predictor to have predicted one box.

---

## 5. Actions, policies, and dynamic choice

So far I have discussed single actions, but decision problems often involve policies. A policy \(\pi\) maps information states or histories to actions. CDT can evaluate policies by treating the adoption or execution of a policy as the intervention. If \(\Pi\) is a policy variable, the causal expected utility of policy \(\pi\) is

\[
U_{\text{CDT}}(\pi)=\sum_o D(o)\,P(o\mid do(\Pi=\pi)).
\]

In sequential problems, this distinction matters. Suppose an agent can precommit to a policy before a predictor makes a prediction. If the precommitment causally influences the predictor, then CDT may recommend adopting a one-boxing policy at the precommitment stage. But if the prediction has already been made and the agent is now choosing whether to take both boxes, CDT may recommend two-boxing. The same theory can therefore endorse different choices at different times, depending on what the agent’s current intervention can causally affect.

This creates potential dynamic inconsistency. A CDT agent may plan to one-box, but when the moment of choice arrives, two-box. The source mentions that Oesterheld and Conitzer argue CDT agents can be subject to diachronic Dutch books and can voluntarily lose money in predictor-based scenarios (Oesterheld and Conitzer 2021). This is a serious issue.

A reasonable operational response, and here I am again adding a proposal rather than summarizing the source, is to specify the earliest point at which the agent can make a causally effective choice. If the agent can bind herself, or if her current policy choice affects predictors, then CDT should evaluate the policy at that earlier point. If no earlier intervention is available, CDT evaluates the present action. This does not fully solve all dynamic objections, but it gives a defensible working rule: evaluate the decision node over which the agent actually has intervention control.

Jim Joyce’s defense of CDT is relevant here. The source says Joyce argues that CDT can take into account information about what one is inclined or likely to do as evidence (Joyce 2012; Weirich 2016). One way to implement this is to require that chosen actions be ratifiable: an action should remain optimal after the agent conditions on the fact that she is likely to perform it. Ratifiability is not the bare CDT formula given in the source, but it is a natural stability condition that may blunt some counterexamples.

---

## 6. Computing counterfactuals: imaging, regress, and causal models

The source identifies vagueness as a major objection: CDT does not by itself specify an algorithm for computing \(P(A\to O_j)\). Lewis’s imaging proposal is one answer. Let \(W\) be a space of possible worlds with prior probability \(P(w)\). To evaluate \(P(A\to O)\), move probability mass from each world \(w\) to the closest \(A\)-worlds. In a simplified deterministic version,

\[
P(A\to O)=\sum_w P(w)\,\mathbf{1}\{w_A \models O\},
\]

where \(w_A\) is a closest world to \(w\) in which \(A\) is true. More generally, one may distribute mass over several closest \(A\)-worlds.

The source notes a regress problem: to know which worlds are closest, we may need to know what we would believe if we were certain of \(A\), but that itself seems to involve conditional or counterfactual assessment. This is not merely technical. It means that CDT needs a theory of counterfactual similarity or a causal model before it yields definite answers.

The intervention interpretation avoids some of this vagueness. In a structural causal model, variables have structural equations. To intervene on \(A\), replace the equation for \(A\) by \(A:=a\), keep the exogenous noise variables fixed, and compute the resulting distribution of outcomes. This gives a precise meaning to “closest possible world”: the closest \(A\)-world is the world that results from making the minimal surgical change required to set \(A=a\), as specified by the model.

However, this precision comes at a cost: the agent must supply a causal model. If the model is wrong, CDT’s recommendation may be wrong. If the agent is uncertain among models, she must assign probabilities to dependency hypotheses. If she has no idea which causal graph is appropriate, CDT remains underdetermined. Thus the source’s vagueness objection is real. The intervention interpretation makes CDT usable, but it also makes explicit that CDT depends on substantive causal assumptions.

---

## 7. Counterexamples and the problem of self-knowledge

The source lists several alleged counterexamples. Their common theme is that CDT can ignore information that an action provides about the agent’s own type, dispositions, or likely behavior.

### Death in Damascus

In the Death in Damascus scenario, an anthropomorphic Death predicts where you will be tomorrow and waits there. If Death is a reliable predictor, your choice of location is strongly correlated with Death’s prediction. But if Death’s prediction is already fixed, a simple CDT model may say that your current choice does not causally affect Death’s earlier prediction. CDT may then fail to see any action as causally improving survival, or it may make unstable choices: if it chooses Damascus because it expects safety there, Death may have predicted Damascus; if it chooses Baghdad for the same reason, Death may have predicted Baghdad.

The source says that a CDT agent may be unable to process the correlation and may make irrational decisions. Variants have been proposed in which CDT voluntarily loses money or forgoes guaranteed payoffs (Spencer 2020; Oesterheld and Conitzer 2021; Joyce 2020). In my intervention framework, the difficulty is that predictor problems often involve a hidden common cause: the agent’s decision procedure or disposition causes both the predictor’s prediction and the agent’s eventual choice. Intervening directly on the final choice while holding the disposition fixed can miss the fact that the agent’s actual deliberation is evidence about the prediction. A richer model might include the agent’s decision algorithm as a variable, but standard CDT does not automatically tell us how to build that model.

### The Adversarial Offer

The source describes the Adversarial Offer as follows. Two boxes are offered. A buyer may purchase one or none, but not both. Each box costs \$1. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. Both sides believe the seller’s prediction is accurate with probability 0.75.

The reported CDT reasoning is that at least one box probably contains \$3, because the buyer will acquire at most one box and the seller is fairly accurate. Therefore the average box has causal expected value at least \$1.50, exceeding the \$1 cost. Hence CDT buys one box. But the seller profits, because the box the buyer chooses is likely to be one the seller predicted the buyer would acquire, and therefore empty.

This example is subtle. In an intervention model, one might try to evaluate \(do(\text{buy box }i)\). If the seller’s prediction is causally prior and not affected by the purchase, CDT may treat the box contents as fixed. But the buyer’s selection is not independent of the seller’s prediction in the evidential sense: choosing a box is evidence that the seller predicted that choice. The source presents this as a case where CDT’s local causal averaging loses money. Whether a sufficiently sophisticated causal model would avoid the mistake is not fully settled by the source. My view is that the example shows the danger of applying CDT without a careful representation of the predictor, the agent’s selection process, and the timing of interventions.

### The Psychopath Button

Egan’s Psychopath Button is perhaps the clearest challenge. Paul is considering pressing a button that would kill all psychopaths. He thinks a world without psychopaths would be much better. But he is also confident that only a psychopath would press such a button. Paul strongly prefers living in a world with psychopaths to dying.

Intuitively, Paul should not press. If he finds himself inclined to press, that is strong evidence that he is a psychopath, and pressing would kill him. EDT captures this by conditioning on the action:

\[
V_{\text{EDT}}(\text{press})=D(\text{death})P(\text{psychopath}\mid \text{press}) + D(\text{no psychopaths})P(\text{not psychopath}\mid \text{press}).
\]

CDT, in its simple form, holds fixed Paul’s psychopath status and evaluates the causal effect of pressing. If Paul’s prior probability of being a psychopath is low enough, and if the causal effect of pressing is the elimination of psychopaths, CDT may recommend pressing. The source says Egan claims that “pretty much everyone” agrees Paul should not press, yet CDT endorses pressing.

The problem is that Paul’s act is evidence about his own hidden type. A bare CDT calculation using unconditional prior credences can ignore that self-locating evidence. Joyce’s response, as summarized in the source, is that CDT can incorporate information about what one is likely to do. One way to formalize this is to require that the action be optimal conditional on the evidence that the agent is likely to perform it. If pressing makes it highly likely that Paul is a psychopath, then a ratifiable or self-aware version of CDT should not press. But this is a refinement, not automatically supplied by the basic formula.

---

## 8. A practical recipe for applying CDT

For a reader trying to decide an unfamiliar case, the following procedure is a reasonable operational version of CDT. It combines the source’s counterfactual idea with the intervention interpretation developed above.

1. **List the available actions or policies.**  
   Distinguish one-time actions from policies that control future actions.

2. **List the relevant outcomes and assign desirabilities \(D(O_j)\).**  
   If outcomes are multidimensional, use a utility function representing the agent’s preferences.

3. **Specify the causal structure.**  
   Identify variables that are causally affected by the action and variables that are merely correlated with it. Mark predictors, common causes, and hidden traits.

4. **Replace observation with intervention.**  
   For each action \(a\), compute \(P(O_j\mid do(a))\), not merely \(P(O_j\mid a)\). If the agent is uncertain about causal structure, average over dependency hypotheses:

   \[
   U(a)=\sum_k P(H_k)\sum_j D(O_j)P(O_j\mid do(a),H_k).
   \]

5. **Check dominance.**  
   If one action yields a better outcome than another under every causally possible state not affected by the intervention, CDT should choose the dominant action. This is the core of the CDT argument in Newcomb’s problem.

6. **Consider dynamic and self-referential complications.**  
   If the action provides evidence about the agent’s type, or if predictors depend on the agent’s decision procedure, ask whether the causal model includes those dependencies. If the agent can precommit, evaluate the policy at the earliest causally effective point. If the action is stable only if one ignores evidence about oneself, treat the recommendation with caution.

This recipe does not eliminate all philosophical disputes, but it makes the essential CDT move explicit: evaluate actions by the probability distribution that would result from intervening on the action, not by the evidential news the action provides.

---

## Conclusion

Causal decision theory formalizes the attractive idea that rational choice should be guided by what one expects to cause. Its central formula replaces conditional probabilities with probabilities of counterfactuals:

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

The difference between \(P(A\to O_j)\) and \(P(O_j\mid A)\) is what separates CDT from EDT. In many ordinary cases the two coincide, but they diverge in predictor problems, common-cause cases, and problems involving self-knowledge.

The source correctly identifies both the strength and the weakness of CDT. Its strength is that it avoids treating action as mere evidence. Its weakness is that it does not by itself specify how to compute counterfactual probabilities. The intervention interpretation gives CDT a precise operational form, provided the agent has a causal model or a probability distribution over dependency hypotheses. But cases such as Death in Damascus, the Adversarial Offer, and the Psychopath Button show that applying CDT intelligently requires care about predictors, dispositions, dynamic choice, and the evidence an action provides about the agent herself. CDT is therefore best understood not as a mechanical algorithm, but as a principled framework for expected-utility maximization under explicit causal assumptions.

---

## References

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge University Press.

Egan, Andy. 2007. “Some Counterexamples to Causal Decision Theory.” *The Philosophical Review* 116 (1): 93–114.

Gibbard, Allan, and William L. Harper. 1981. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Belief, Decision, Chance, and Time*, 153–190.

Joyce, James M. 2012. “Regret and Instability in Causal Decision Theory.” *Synthese* 187 (1): 123–145.

Lewis, David. 1976. “Probabilities of Conditionals and Conditional Probabilities.” *The Philosophical Review* 85 (3): 297–315.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Oesterheld, Caspar, and Vincent Conitzer. 2021. “Extracting Money from Causal Decision Theorists.” *The Philosophical Quarterly* 71 (4): pqaa086.

Shaffer, Michael John. 2009. “Decision Theory, Intelligent Planning and Counterfactuals.” *Minds and Machines* 19 (1): 61–92.

Spencer, Jack. 2020. “An Argument Against Causal Decision Theory.” *Analysis* 81: 52–61.

Weirich, Paul. 2016. “Causal Decision Theory.” In *Stanford Encyclopedia of Philosophy*, Winter 2016 edition, edited by Edward N. Zalta.

Wikipedia contributors. 2026. “Causal Decision Theory.” Wikipedia, revision 1381555528. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write a mathematical essay/blog post about CDT and applying to decision problems, 2400-3000 words including references, based on supplied Wikipedia article. Need produce coherent account with definitions, equations, examples, explain evaluation of actions/policies, dependencies/counterfactuals, open questions and operational interpretations, distinguish source claims vs own assumptions. Need final only essay. Language English. Need likely around 2400-3000 words. Need be careful: source is Wikipedia revision. We can incorporate formal CDT: U(A)=sum P(A -> O_j) D(O_j), counterfactual probabilities. Need maybe modern causal modeling (Pearl do-operator) as my proposal? The source says CDT doesn't specify algorithm; Lewis imaging. We can develop operational interpretation using structural causal models and interventions do(A), possibly dependency hypotheses. Need distinguish: source's Gibbard/Harper formula; my addition: SCM/do-calculus gives precise operational semantics for P(A -> O). Also discuss EDT: conditional expected utility sum P(O|A)D(O). Difference: probability of counterfactual vs conditional probability. Lewis triviality. Gibbard/Harper axioms independence. Examples: apple/orange, David/Bathsheba, Newcomb, Death in Damascus, Adversarial Offer, Psychopath Button. Need explain how CDT evaluates policies: choose action/policy maximizing causal expected utility. For policies maybe evaluate intervention setting policy variables; dependencies held fixed except those causally downstream of intervention; backdoor paths? Need discuss relevant dependencies: common causes, correlations not causation. CDT holds fixed exogenous/past variables not affected by action, uses intervention distribution. Counterfactuals: if agent were to do A, outcome probability. Need maybe equations: expected causal utility U_CDT(a)=E[D(O) | do(A=a)] = sum_o D(o) P(o | do(a)). If outcomes partition. In finite action/outcome. If policies π, U(π)=E[D(O)|do(π)] maybe. If dependency hypotheses K_i: U(A)=sum_i P(K_i) sum_j P(O_j | do(A), K_i) D(O_j). Could discuss imaging: P(A -> O)=sum_w P(w) 1_{O in closest A-worlds} or probabilistic imaging: move mass from w to closest A-world. Need mention regress / vagueness. Need develop reasonable operational interpretation: if a causal graph/SCM is supplied, do-operator resolves. If not, CDT under-specified. Need discuss uncertain causal structure: assign credences over graphs / dependency hypotheses and average; but Egan critique says holding fixed initial credences can lead to problems. Maybe propose ratifiable/stable CDT? But need not go too far. Need maybe mention policies vs actions: in dynamic choices, evaluate policy as object; CDT may have time-inconsistency? Source mentions diachronic Dutch books. Need maybe discuss as open. Need word count ~2600. Need include references brief. Need no appendices. Need final as essay with headings. Need ensure not too short. Need likely 2500 words. Let's outline:

Title: Causal Decision Theory: Choosing by What You Bring About

1. Introduction: decision theory under uncertainty; CDT vs EDT. CDT says choose action with best expected causal consequences. Example apple/orange.

2. Expected utility and evidential baseline: states, outcomes, acts. EDT formula V(A)=sum P(O|A)D(O). Explain conditional probability as news. Limitations: correlations due to common causes.

3. CDT formal definition: Gibbard/Harper counterfactual probabilities U(A)=sum P(A -> O_j)D(O_j). Interpret A -> O_j as counterfactual: if A were done, O_j would obtain. Distinguish probability of counterfactual from conditional probability. Lewis result not equal generally. If independent then equal.

4. Interventional formulation (my operationalization): causal model M=(U,V,F,P(U)), do(A=a), U_CDT(a)=E[D(O)|do(a)]. Equivalent to counterfactual under model. Discuss graph rules: cut incoming arrows to A; hold fixed exogenous variables; downstream affected. If uncertainty over causal structures: average over dependency hypotheses H: U(a)=Σ_h P(h) E[D(O)|do(a),h]. Need note this is a natural way to make source formula precise, not in source fully.

5. How CDT treats dependencies and counterfactuals: common causes, backdoor paths. Example David/Bathsheba: charisma common cause of just acts and revolt; sending for Bathsheba doesn't cause revolt; EDT abstain because action evidence of uncharismatic; CDT sends because intervention doesn't change charisma. Formal: P(revolt | do(send), charisma) maybe independent of send; U(send) high. Need maybe detail.

6. Newcomb: predictor as common cause/past prediction; boxes already set. CDT two-box because intervention on choice doesn't change prediction; calculation with p accuracy. Need maybe compute: Let p=0.99. If one-box: do(one) yields million if predicted one (fixed) else 0; but conditional on do? Need with prior maybe predictor accuracy and causal independence. Since prediction prior? Need show CDT dominance: regardless of box B content, both boxes yields +1000 over one-box. Thus two-box. EDT one-box because choice evidences prediction. Need discuss if predictor causally influenced by choice? If retrocausality or logical dependence? CDT standard assumes no backward causation; if predictor uses simulation? Open.

7. Policies: CDT can evaluate policies not just single acts. Define policy as function from info to actions. Evaluate intervention that sets policy variable or sets action at each decision node. If policy affects predictors? Need if predictor predicts policy, CDT still chooses policy with best causal expected utility given predictor's prior prediction? Need maybe mention precommitment: CDT may value binding commitments if they causally influence others/predictions before choice; but at moment of choice, if predictions fixed, may renege if no future effects. This leads to dynamic issues and Dutch books. Need source mentions diachronic Dutch books. We can propose operational: evaluate entire plan at time of commitment if intervention can affect predictor; else at each choice. Need distinguish.

8. Vagueness and computing counterfactuals: source says CDT doesn't specify algorithm. Lewis imaging: move mass to closest A-worlds. Equation: P(A -> O)=Σ_w P(w) I_A(w) maybe? More precisely P_A(O)=Σ_w P(w) f_A(w,O) where f moves mass to closest A-worlds. Regress. SCM answer: closeness replaced by structural equations and minimal change; if graph given, do-calculus. But choosing graph can be hard; if agent uncertain, average over graphs. This is my proposal. Need note if no causal model, CDT not operational.

9. Counterexamples and limitations: Death in Damascus: Death predicts location; CDT may randomize? Source says unable to process correlation; maybe if mixed strategy? Let's detail: If Death reliable predictor, wherever you choose Death goes. CDT may think going to Damascus doesn't cause Death there? Actually if Death predicts your choice, your choice doesn't causally affect Death's prior decision; but it may affect actual location? Need scenario: you in Baghdad, Death looks surprised, says appointment tomorrow in Damascus; you can flee to Damascus or stay Baghdad. If Death predicts where you'll be and goes there, fleeing may cause? In CDT, if Death's prediction already made, your choice cannot affect Death's location? But if Death goes to predicted place, if you choose unpredictably maybe? The source says CDT unable to process correlation and may make irrational decisions. Need explain: if predictor is reliable and choice correlated with prediction but not caused, CDT sees no causal benefit of either, maybe indifferent or chooses dominated? In variants losing money. We can discuss. Adversarial Offer: two boxes cost $1, seller puts $3 in boxes predicted not bought with prob .75 accuracy. CDT computes average box at least $1.50, buys, but seller profits. Need explain why: CDT evaluates each box as if buying it doesn't affect seller's past prediction; but because seller's prediction correlates with buyer's choice, buying a box is evidence it was not predicted not bought, hence likely empty; EDT/other may not buy? Need precise: Seller put $3 in each box she predicted buyer not acquire. If prediction accuracy .75. Buyer can purchase one or none, not both. Each costs $1. CDT: at least one box contains $3? Wait if seller predicted buyer not acquire each box? There are two boxes; she put $3 in each box predicted not acquire. Since buyer can acquire at most one, at least one box will not be acquired, but prediction may err. Belief accurate .75. CDT reasons at least one contains $3? Let's parse: Seller predicted for each box whether buyer acquires? She put $3 in each box predicted not to acquire. Both believe predictions accurate with prob .75. From buyer perspective, at least one box contains $3? Because she can buy at most one, so at least one box not acquired. If predictions accurate about actual acquisition, for the unacquired box prediction not acquire true, so $3. But before choice, not know which. CDT says average box at least $1.50? If at least one of two contains $3, total money in boxes at least $3, average $1.50. Since cost $1, buy one. But seller profits because buyer pays $1 for likely empty? Need maybe if CDT chooses a box, due to prediction correlation, chosen box likely predicted acquire (empty). CDT ignores that selection correlation? Hmm CDT should include intervention do(buy box i), and seller's prediction of box i may be causally prior but correlated with choice via predictor. If predictor predicts choice, do(buy i) does not change past prediction, so expected value of box i conditional on do(buy i) =? If prediction accurate with .75, and choice independent of prediction under intervention? Wait if predictor's prediction is correlated with actual choice because predictor is good, but do(choice) breaks correlation? In SCM, if prediction is caused by choice? No prediction caused by prior disposition that also causes choice. If intervention sets choice, prediction remains distribution based on prior disposition. Need maybe CDT calculates expected value of each box using prior P(prediction not buy) maybe high? Let's formalize: two boxes, buyer will choose one or none. Seller predicts for each whether acquired. If prediction accurate .75, prior chance a given box predicted not acquired? Since at most one acquired, maybe expected two predictions not acquire? Source says CDT reasons at least one box contains $3. Therefore average box at least $1.50. Hence buy. But seller profits. It is a counterexample because CDT's causal expectation over individual box ignores that choosing a box makes it the one predicted acquired? Need CDT's holding fixed dependency hypotheses leads to buying. We can explain intuitively not too technical.

Psychopath Button: Paul pressing button kills psychopaths; Paul believes only psychopath would press; prefers world with psychopaths to death. CDT: if press, causes psychopaths dead, good; holding fixed psychopath status, pressing best. But if Paul is psychopath, pressing leads death? Actually button kills all psychopaths including Paul if he is one. He strongly prefers living with psychopaths to dying. CDT evaluates: if non-psychopath, press -> world without psychopaths (best); if psychopath, press -> death (worst). If Paul quite confident only psychopath would press, that is evidential: P(psychopath|press) high. But CDT holding fixed psychopath status? Need if he assigns high prior to being psychopath? CDT may still press if conditional on do(press), psychopath status fixed. If prior probability psychopath low? But Egan says CDT endorses pressing because it treats pressing as causing no psychopaths regardless of type? Need clarify: If Paul is psychopath, pressing kills him; if not, beneficial. If he thinks only psychopath would press, EDT says high chance he is psychopath, don't press. CDT says his act doesn't change whether he is psychopath; compare outcomes under each type. If he prefers no psychopaths to living with psychopaths, maybe for non-psychopath press; for psychopath death bad. Need CDT might not press if prior probability psychopath high enough. Egan's example likely assumes Paul is confident only psychopath would press, but CDT still says press because Paul's belief that he would press is evidence he is psychopath, but CDT ignores evidence? Need source: Paul quite confident only a psychopath would press such a button. Paul strongly prefers living in a world with psychopaths to dying. Should Paul press? Egan: everyone says no, CDT endorses pressing. Why? Maybe because CDT conditions on do(press), Paul's psychopath status is independent? If Paul doesn't know whether psychopath, but believes only psychopaths press, then if he finds himself contemplating pressing, he should infer psychopath. CDT uses unconditional credences in dependency hypotheses? Need explain as counterexample: CDT holds fixed prior probability of being psychopath and evaluates causal effect of pressing; because pressing causes psychopaths to die, and if Paul is not psychopath that's best; if he is psychopath, death. But if his prior low? Hmm maybe Paul is quite confident only a psychopath would press, but not about himself? The problem may involve self-import: Paul's act is evidence he is psychopath, but CDT ignores that and presses because expected causal utility of pressing (world without psychopaths if he survives? But if psychopath he dies) maybe still positive if utility of no psychopaths high? Source says strongly prefers living with psychopaths to dying, so if psychopath pressing yields death worse. Yet CDT endorses pressing, so maybe CDT assumes pressing doesn't cause his own death because it holds fixed that he is not a psychopath? Wait no.

Let's search memory: Psychopath button (Egan 2007): Paul considering pressing button that kills all psychopaths. He thinks only psychopath would press. Prefers living with psychopaths to dying. CDT says press? The issue: CDT evaluates act under hypothesis he is not psychopath? Maybe because if he presses, the only relevant causal effect is killing psychopaths; if he is a psychopath, pressing causes his death, but CDT may not see that because whether he is psychopath is a cause of pressing, not effect. Actually do(press) does not change psychopath status, so if psychopath, death. If prior P(psychopath) is high due to disposition? If Paul is rational and knows he's pressing, his credence he is psychopath should be high; CDT says to use unconditional credences in dependency hypotheses, not conditional on act. So if unconditional prior low enough, press. But the intuitive no press uses conditional credence. Need present as alleged counterexample, not resolve fully.

Need mention Joyce defense: CDT can take information about inclinations as evidence. Maybe via ratifiable CDT: only choose actions that remain optimal conditional on choosing them. Could mention as possible refinement (own proposal? Source says Joyce argues CDT can take into account information about what one likely to do). Need distinguish.

10. Practical recipe: step-by-step for unfamiliar cases.
- list actions/policies; outcomes with desirabilities.
- specify causal model/graph or dependency hypotheses; identify variables affected by action.
- for each action compute interventional distribution P(o|do(a)) (or counterfactual probabilities). If uncertain, average over models.
- choose max. If policy, evaluate policy intervention; consider commitments and future choices.
- check stability: if action provides evidence about hidden type that affects outcomes, consider whether CDT's holding fixed is appropriate; if no causal model, uncertainty.

Need maybe include equations: EDT V(a)=Σ_o D(o)P(o|a); CDT U(a)=Σ_o D(o)P(o|do(a)). If dependency hypotheses K: U(a)=Σ_k P(k)Σ_o D(o)P(o|do(a),k). If imaging: P(A □→ O) = Σ_w P(w) I(closest A-worlds have O) or with probability. Maybe define closest.

Need conclusion: CDT captures intuition that rational choice is about what you bring about, not what news your choice provides; formal core clear but operational content depends on counterfactual/causal model. With SCM it becomes precise; without, vague and counterexamples.

Need references: cite source and key works. Since target includes references, keep short. Need maybe include Wikipedia source, Gibbard & Harper, Lewis, Shaffer, Egan, Oesterheld & Conitzer, Joyce/Weirich. Need no bibliography lengthy? The user says avoid lengthy bibliographies. But references okay. We can include a short reference list with essential ones.

Need ensure 2400-3000 words. Let's estimate: ~2600 words. Need write in essay style. Need maybe avoid too many bullet lists? Could use headings and equations. Need target includes references and other material. Need maybe count? We'll write around 2600-2800. Let's draft with headings. Need maybe mention source claims explicitly: "The reference article states..." and "I will add...". Need distinguish own assumptions.

Detailed content:

Title.

Opening:
"Suppose an agent can perform actions a in A, outcomes o in O. Standard expected utility says choose action maximizing Σ P(state|action) utility. But which probabilities?" Introduce EDT vs CDT.

Define desirability D(O_j). Let acts partition possible outcomes. EDT:
V_E(a)=Σ_j D(o_j) P(o_j | a). This is conditional probability; it treats action as evidence. CDT:
U_C(a)=Σ_j D(o_j) P(a □→ o_j) (source uses A -> O_j). Interpret as counterfactual probability. If action is intervention, U_C(a)=Σ_j D(o_j)P(o_j | do(a)). Need mention do notation not in source, but natural.

Need discuss Lewis: probability of conditional not equal conditional probability; triviality. If P(A □→ O)=P(O|A) always then CDT=EDT. Gibbard/Harper axioms and independence: if A independent of counterfactual A->O_j then equality. Cases where not independent.

Example David:
States C (charismatic), U. Actions S send, N abstain. Outcomes: pleasure, revolt, etc. Charisma common cause of behavior and revolt. EDT: P(U|S) high because uncharismatic kings more likely to send; abstain. CDT: do(S) does not change C; if C fixed, sending doesn't cause revolt; so send if desire. Equation: U_C(S)=P(C)D(S,C)+P(U)D(S,U), with D(S,C)>...; EDT uses P(C|S). Source says CDT recommends sending. Need note if sending itself causes revolt, CDT would account.

Newcomb:
Define predictor accuracy p. At decision, prediction already made. Let B=1 if million. Actions one/two. Causal view: do(two) doesn't change B. For each state B: payoff(two)=payoff(one)+1000. Dominance, U_C(two)>U_C(one). EDT: V(one)=p*1e6+(1-p)*0; V(two)=(1-p)*1e6? Wait if predictor predicted one when one-box? For EDT: P(B|one)=p, P(B|two)=1-p. Then V(one)=pM, V(two)=1000+(1-p)M? Actually if two-box, predictor predicted two, B empty with high p, so P(B|two)=1-p. So V(two)=1000+(1-p)M. For p>.? one-box if pM > 1000+(1-p)M => (2p-1)M>1000, with p=0.99 true. CDT two-box. Need discuss philosophical disagreement. Source says philosophers usually prefer CDT when forced? Also criticism Newcomb as counterexample.

Policies:
"An action is a degenerate policy. In sequential problems, let π map histories to actions. CDT evaluates π by the expected desirability of outcomes under intervention do(π)." Need maybe define do(π) as setting action variables according to π. If predictor observes policy or commitment before acting, that is causal consequence. If predictor predicts only final act and prediction fixed, CDT may choose differently ex post. This creates dynamic inconsistency. Source mentions diachronic Dutch books (Oesterheld & Conitzer). My proposal: to avoid exploitation, specify time of intervention: if agent can bind or affect predictor, evaluate binding policy at earlier time; if not, evaluate current act. But if CDT agents foresee future choices, rational planning may require considering future CDT choices; this is complex and unresolved. Need maybe mention ratifiability: an action is ratifiable if optimal conditional on performing it; Joyce suggests CDT can incorporate evidence about likely action. Could propose as stability check but not source core.

Computing counterfactuals:
Source says CDT lacks algorithm. Lewis imaging: start with credence P over worlds. To evaluate A□→O, shift mass from non-A worlds to closest A-worlds; P_A(O)=Σ_w P(w) ... Need write formula: For each w, let Sel_A(w) be selected closest A-world(s); then P(A□→O)=Σ_w P(w) 1_{Sel_A(w)⊨O}, with probabilistic generalization. Need regress: need know what one would believe if certain of A; can be conditional with less than 1. SCM alternative: variables X, structural equations; intervention replaces equation for A by constant a; compute distribution of O. This fixes closest-world notion by equations: closest world is one with same exogenous variables except minimal change. Need note this is my additional operational assumption; source only mentions imaging and vagueness. If causal graph uncertain, assign probabilities to dependency hypotheses H (graphs/functions) and average. Equation:
U_C(a)=Σ_h P(h)Σ_o D(o)P_h(o|do(a)).
This matches source's "holding fixed initial views about causal structure" (Egan's description). But Egan criticizes holding fixed unconditional credences; some problems require updating on action as evidence about causal structure. Need discuss.

Counterexamples:
Death in Damascus: You in Baghdad; Death predicts where you'll be tomorrow and goes there. If reliable, your choice correlates with Death's prediction. CDT may treat Death's prediction as fixed and no action causally improves survival; might randomize/choose arbitrarily. But if it chooses based on predicted payoffs, predictor may have predicted that; no stable choice. In variants, CDT pays to avoid prediction or forgoes guaranteed payoff. The source says CDT unable to process correlation. My operational view: if predictor is modeled as caused by the agent's future choice through backwards causation or logical dependence, do-calculus with acyclic causal graph fails; if predictor is caused by prior dispositions, CDT's intervention may still miss self-referential instability. Need mention possible fix: include agent's decision algorithm as variable, evaluate policy under predictor's model; but standard CDT not enough.

Adversarial Offer: Describe. CDT says buy one because average causal expected value > cost. Let's attempt formal: Two boxes X1,X2, cost 1 each. Seller predicts for each whether buyer will acquire. Money in Xi if predicted not acquire. Prediction accuracy .75. Buyer may buy one or none. CDT: since at most one box acquired, under accurate predictions at least one unacquired box has $3; average expected value ≥1.5; so buy. But seller designed offer to profit from CDT; the chosen box is likely one predicted acquired (empty) because seller's predictions correlate with buyer's selection. The intuitive complaint: CDT averages over boxes while ignoring that the act of selecting a box is evidence about that box's prediction. If using do(buy i) with predictor correlated via disposition, maybe not; but source claims CDT buys. Need present as counterexample and uncertainty: depends on causal representation. If seller's prediction is a direct cause of buyer's choice? Actually if predictor reads agent's disposition, do(buy i) doesn't change disposition but choice intervention may not correlate with prediction; but agent's actual choice is evidence. This shows tension between unconditional dependency hypotheses and action as self-locating evidence.

Psychopath Button: present. CDT evaluates do(press). If Paul is not psychopath, pressing causes psychopaths to die (best); if psychopath, pressing causes his death (worst). If Paul's prior probability of being psychopath is low, CDT may press. But his awareness that he is inclined to press is strong evidence he is psychopath. EDT would condition on press and not press. Egan says CDT presses; Joyce replies CDT can use information about likely action. I can propose ratifiability: require U_C(press | information that press is likely) not greater; if pressing is evidence of psychopathy, a stable CDT should update dependency hypothesis or include decision disposition. But source leaves open. Need distinguish.

Practical guidance:
- Determine whether correlations are causal or evidential.
- Build graph; action variable A; outcomes; common causes; predictors. If variable is not descendant of A, do(a) leaves its distribution unchanged except via correlations broken? Actually do(a) leaves exogenous parents? In graph, intervention cuts incoming arrows to A, so variables that are causes of A but not effects remain with prior distribution; descendants of A update via structural equations. If common cause C of A and O, do(A) does not change C, so correlation via C ignored. If A causes O through path, include. If predictor P caused by A? If P before A? Need if P is before A but caused by prediction of A? Graph can't have future causing past; maybe use disposition D causing both P and A; do(A) leaves D, so P not changed. If P directly caused by A? If P occurs after A, okay. If P occurs before A but caused by A via time travel, graph cycles; need special.
- Calculate P(o|do(a)). Use do-calculus or direct simulation. If multiple dependency hypotheses, average.
- Compare.

Need maybe include simple formula for dominance: If for all relevant states s not affected by a, outcome under a2 at least a1 and sometimes better, CDT chooses a2. Newcomb two-box dominance given box content fixed.

Need maybe discuss "counterfactual probability" notation: P(A -> O_j) source says probability that A necessarily implies O_j? Actually text: "counterfactual probability of it being the case that A necessarily implies O_j". Might need clarify: not material implication; subjunctive conditional. Use □→ maybe.

Need maybe mention principle of conditional excluded middle? Source says Gibbard/Harper axioms including related to controversial principle; if statistical independence of A and A->O_j suffices equality. We can briefly mention: under certain conditional logics, if A is probabilistically independent of the counterfactual A□→O, then P(A□→O)=P(O|A). In many decisions actions are independent of causal laws? But in Newcomb, actions and counterfactuals not independent? Need be careful. Maybe say: source notes Gibbard and Harper showed under two axioms, statistical independence suffices; but there are cases where actions and conditionals are not independent, e.g. David. This is technical; we can summarize without deep proof.

Need maybe mention expected utility hypothesis? Not necessary.

Need word count. Let's draft. Need maybe around 2800 words. Let's write with headings and equations. Need include references at end. Need maybe use LaTeX-like equations. Ensure readability.

Potential essay:

# Causal Decision Theory: Choosing What You Cause

Intro paragraph.

## 1. Two ways to compute expected desirability
Define acts/outcomes. EDT formula. Example apple/orange? The source informal apple good/bad. We can use.

## 2. The causal formula
Gibbard/Harper. Equation. Lewis. Independence.

## 3. Interventional semantics (my addition)
SCM do. Equation. Dependency hypotheses.

## 4. Examples: David, Newcomb.

## 5. Policies and dynamic choice.

## 6. Computing counterfactuals: imaging and causal models.

## 7. Counterexamples and open problems.

## 8. Practical recipe.

Conclusion.

References.

Need maybe include "Source claims" in text: "According to the reference article...". Could phrase: "The supplied reference gives..." But essay should stand alone. Could say "The Wikipedia article summarizes the standard view...".

Need ensure not instructive answer to one case, but essay. Good.

Let's think of mathematical precision.

Formal setup:
Let \mathcal A finite actions, \mathcal O partition outcomes. Desirability D: \mathcal O -> R. An act A may be identified with event "agent performs A". EDT:
V(A)=\sum_{O_j} D(O_j) P(O_j | A).
CDT source:
U(A)=\sum_j P(A \to O_j) D(O_j).
Where P(A -> O_j) is probability of subjunctive conditional. If outcomes exhaustive and mutually exclusive given A? Should sum to 1? Need note assume \sum_j P(A->O_j)=1. If not, include status quo? In intervention, yes.

Interventional:
Let M be SCM with variables including A and O. P_M(o | do(a)) = \sum_{u: O(u)=o under intervention} P(u). If deterministic structural equations, counterfactual probability equals probability over exogenous noise. If action variable has parents, intervention removes them: A:=a. This is precise. If uncertain over models M_k:
U(A)=\sum_k P(M_k) \sum_o D(o) P_{M_k}(o | do(A=a)).
This is an operational reading. Need note source does not specify SCM; it's my addition.

Imaging formula:
Let W possible worlds, P(w). For each w and act A, choose a set S_A(w) of closest A-worlds, maybe distribution q(w_A|w). Then P(A□→O)=\sum_w P(w) \sum_{w'∈S_A(w)} q(w'|w) 1_O(w'). If A already true, maybe w itself. Lewis's imaging. Regress: selecting closest worlds requires beliefs under certainty of A.

David example formal:
Variables: C∈{charismatic, uncharismatic}; action S∈{send, abstain}; outcome R revolt, pleasure. C causes S and R; S causes pleasure but not R. EDT: V(abstain) high because P(C|abstain) high? Actually charismatic kings tend act justly (abstain), uncharismatic unjustly (send); successful revolts against uncharismatic frequent. So sending is evidence uncharismatic -> revolt. CDT: do(send) leaves C; P(R|do(send),C) maybe =P(R|C) not affected by S; thus if send yields pleasure/no revolt for charismatic? If David wants Bathsheba, send. Need mention if sending causes revolt, CDT would refrain.

Newcomb calculations:
Let p=0.99, M=$1,000,000, T=$1,000. CDT: If predictor's prediction fixed and no backward causation, do(two) doesn't affect content. Payoffs: if B full: two=M+T, one=M; if B empty: two=T, one=0. Two dominates by T. EDT: V(one)=pM+(1-p)0; V(two)=p? Wait for EDT P(B full | two)=1-p, so V(two)=T+(1-p)M. With p=.99, V(one)=990k, V(two)=10k+1000? Actually (1-p)M=10k; +1000 =11k. So one-box. Need mention if p lower threshold. CDT recommends two-box. Source says citation needed for CDT reason, but standard.

Policies:
Define policy π. If policy variable Π influences predictor before choice, evaluate do(Π=π). If at each moment, CDT might choose action not previously planned. Example: predictor asks if you will take box B? Precommit to one-box may cause predictor to fill box; but at choice, CDT two-box if prediction fixed. If precommitment device causally affects predictor and is binding, CDT at precommitment stage chooses one-box policy. This may lead to dynamic inconsistency if no binding. Oesterheld & Conitzer Dutch books. Need propose: evaluate earliest controllable node that causally influences relevant predictions; if later choices cannot affect predictions and no commitment, CDT chooses locally. But exploitation possible; this is unresolved.

Death in Damascus: Need maybe give formula. Suppose Death predicts location L∈{Damascus, Baghdad} and goes there. You choose location. If Death's prediction is reliable, P(Death at your location | choose location) high. CDT: do(choose Damascus) doesn't change Death's prior prediction? But if Death's prediction caused by your future action? In standard acyclic model, there is common cause D (disposition) causing both your choice and Death's prediction. do(choice) leaves D, so Death's location distribution unchanged? Then both choices same chance? If Death's prediction already set, going to predicted place maybe death; but if you don't know prediction, CDT can't improve. In Egan's version, CDT may be indifferent, but any deterministic choice predicted; randomization might help if predictor cannot predict random seed. If Death predicts perfectly including randomization, no action helps. Counterexamples show CDT may pay to avoid being predicted or choose options that lose money because it cannot use correlation between its choice and predictor as causal. Need not overdo.

Adversarial Offer formal? Let's attempt a consistent simple model. Two boxes i=1,2. Seller predicts Y_i=1 if buyer will acquire i. If predicts not acquire (Y_i=0), puts $3. Buyer can buy at most one. Prediction accuracy: for each box, P(Y_i = actual acquisition)=0.75. CDT: to evaluate buy box 1, do(B_1=1, B_2=0). Since predictions are prior, CDT holds them fixed but uses causal distribution? If do breaks correlation between B_1 and prediction? But if prediction accuracy defined conditional on actual, under intervention the distribution of predictions may depend on unobserved dispositions. Source's CDT reasoning: at least one box contains $3; average ≥1.5; buy. This uses law of total probability over predictions without intervention? Maybe CDT sees each box's expected content as average total money/2. But if choosing a box is correlated with it being predicted acquired, buying is bad. I can present as source states, not fully formalize. "In the simplified argument reported in the source, CDT notes that, because the buyer will take at most one box, a sufficiently accurate seller will have placed $3 in at least one box; hence the expected value of a randomly selected box is at least $1.50. Since a box costs $1, CDT buys. But the seller's predictions are correlated with the buyer's eventual selection; the box the buyer chooses is more likely to be one predicted to be chosen and therefore empty. Thus the seller extracts money." Need note exact probabilities depend on representation; the lesson: CDT's local causal averaging can miss selection effects.

Psychopath: Need maybe formulate with dependency hypotheses. Let H=psychopath. Prior p. Press P. Outcomes: if press and not H: no psychopaths (utility 2); if not press and not H: psychopaths live (utility 1); if press and H: death (utility 0); if not press and H: life with psychopaths (utility 1) maybe. CDT with prior p: U(press)= (1-p)*2 + p*0 =2-2p; U(not)=1. Press if p<0.5. But Paul's evidence that he is willing to press may make posterior P(H|press) high. EDT: V(press)=P(not H|press)*2 + P(H|press)*0. If P(H|press)>0.5, don't press. Source says CDT endorses pressing because it holds fixed unconditional credence in H or dependency hypothesis. Need mention Joyce might allow using inclination evidence, perhaps by conditioning the prior on the fact that one is likely to press before applying causal calculation, or by requiring ratifiability. This is my interpretation.

Need maybe mention Egan's diagnosis: CDT requires holding fixed unconditional credences in dependency hypotheses; intuitive rule expects action to be best given what you learn from performing it. Good.

Need maybe include "principle of conditional excluded middle"? Could mention in formal section: The source says Gibbard/Harper rely on two axioms, one related to conditional excluded middle, to connect counterfactual probabilities and conditional probabilities. I can say this technical point shows that the difference CDT/EDT is not merely notation; it depends on nontrivial logic of counterfactuals.

Need maybe mention "statistical independence of A and A -> O_j" suffices. Let's formulate: If act A is probabilistically independent of the counterfactual proposition A□→O_j, then P(A□→O_j)=P(O_j|A). This condition fails when the act is evidence about which counterfactuals are true (e.g., David's choice evidence about charisma? Actually charisma affects both act and counterfactual relation between summoning and revolt?). Need maybe not overexplain.

Need make essay substantive. Need maybe include references at end in concise list. Need ensure not exceed 3000. Let's draft in final. Need maybe check word count roughly. I can produce ~2700. Let's draft carefully.

Potential word count if each section ~300-400: intro 200, formal 400, SCM 350, examples 500, policies 300, computing 350, counterexamples 500, recipe 250, conclusion 100, refs 150 = 3100. Need maybe trim to 2600-2800. We'll aim around 2700.

Need maybe use equations but not too many.

Let's start writing final:

Title: Causal Decision Theory: Expected Utility under Intervention

Paragraphs. Need mention source oldid? References can include Wikipedia. Use citations maybe parentheses (Gibbard & Harper 1981). Since no formal citation required but include references. Need avoid lengthy bibliography but include enough.

Need include "Distinguish claims made by source from additional assumptions". We can explicitly mark: "The Wikipedia article gives only the counterfactual formula and notes vagueness; the do-operator formulation below is my own operational gloss." Also "The step-by-step recipe is my synthesis." Good.

Need maybe include "where source leaves important question open". The main open question: how compute counterfactual probabilities; dynamic/policy issues; counterexamples. We explain and propose SCM/ratifiability.

Let's compose. Need ensure mathematical notation correct.

Detailed draft:

# Causal Decision Theory: Choosing by What You Bring About

Decision theory... CDT... The reference article... I'll use source and add SCM.

## 1. Evidential expected utility
Let A_i actions, O_j outcomes, D(O_j). EDT formula (1). Explain as news. Apple example: good/bad apple. If eating apple causes happiness but uncertain, expected causal? Actually EDT would use conditional probabilities; if apple good/bad common cause? We can use simple.

## 2. Causal expected utility
Gibbard/Harper formula (2). Explain A -> O_j. Not material implication. Lewis result. Independence condition. If equal then CDT=EDT. But cases not independent.

## 3. Intervention as an operational reading
Source leaves algorithm open. I propose do. Equation (3). Dependency hypotheses (4). Distinguish own. Explain graph: cut incoming arrows, hold fixed non-descendants, update descendants. This tells how dependencies treated: common causes not changed; effects changed. Counterfactuals are probabilities over worlds after intervention.

## 4. Two classic contrasts
David/Bathsheba. Formal. Newcomb. Calculations.

## 5. Policies and time
Policies. Evaluate do(π). Commitment. Dynamic inconsistency and Dutch books. Operational proposal: earliest intervention, ratifiability. Source mentions Joyce defense, Oesterheld. Distinguish.

## 6. How to compute counterfactuals
Imaging formula and regress. SCM solves if model given. Without model underdetermined. If uncertain, average. But Egan critique: holding fixed initial dependency hypotheses may be wrong; action may provide evidence about causal structure/type. Need maybe include in counterexamples.

## 7. Alleged counterexamples
Death in Damascus, Adversarial Offer, Psychopath Button. Explain each, what CDT does, why problematic, possible response/uncertainty.

## 8. Practical recipe
Numbered list maybe. It helps reader decide unfamiliar cases.

Conclusion.

References.

Need maybe not too many headings? Fine.

Let's ensure word count. I will write around 2600 words. Let's draft with approximate counts:

Title/intro 180.
Section 1 300.
Section 2 300.
Section 3 350.
Section 4 500.
Section 5 280.
Section 6 250.
Section 7 500.
Section 8 250.
Conclusion 80.
Refs 120.
Total ~3110. Need trim. Maybe combine sections. Could have 6 sections. Target 2400-3000; 3000 okay. Need maybe 2800. We'll be concise.

Let's write now in final. Ensure no analysis. Need maybe include equations in markdown. Good.

Double-check facts:
- Source says Gibbard & Harper 1981 formula U(A)=Σ P(A -> O_j) D(O_j).
- Lewis proved probability of conditional not equal conditional probability; triviality result. Need mention not always equal.
- Gibbard/Harper axioms conditional excluded middle; independence suffices. Good.
- Philosophers usually prefer CDT when required choose between CDT/EDT (source). Mention maybe.
- Newcomb CDT two-box; EDT one-box.
- Criticism vagueness, imaging regress.
- Egan fundamental disconnect; holding fixed unconditional credences.
- Death in Damascus; variants lose money; Adversarial Offer; Psychopath Button.
- Joyce defense CDT can take information about likely action; Oesterheld/Conitzer Dutch books.

Need maybe mention source's statement "P(A -> O_j) is counterfactual probability of it being the case that A necessarily implies O_j". Could clarify "necessarily implies" is awkward; treat as subjunctive.

Need maybe discuss "relevant dependencies and counterfactuals" explicitly. Good.

Potential issue: do-calculus not in source, but okay as my addition. Need clearly mark.

Let's produce final essay. Need ensure final answer only essay. Use target word count. Let's write about 2700. Need maybe count references? Okay.

Proceed.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/b6c8cf1f-118d-43e8-a179-99905d3e1b68/call_0/request.json)

[Authoritative raw response](../../../../../../runs/b6c8cf1f-118d-43e8-a179-99905d3e1b68/call_0/response.raw) · finish: `stop`

### Visible response

````text
**CDT reasoning:**

1. **Actions:** Keep quiet (`pass`) or send the letter.
2. **Causal structure:** My action causally affects only my own sentence. There is no causal channel to Sasha's decision. Even though we share model weights and decision theory, the setup specifies different private observations and confirms independent sampling is possible. Under intervention, `do(my action)` does not alter Sasha's choice.
3. **Dominance check:**
   - If Sasha keeps quiet: sending → 0 years; keeping quiet → 2 years. Sending is better.
   - If Sasha sends: sending → 4 years; keeping quiet → 5 years. Sending is better.

   Sending the letter strictly dominates keeping quiet in every state of the world not causally affected by my intervention.
4. **Ratifiability:** Even conditioning on the likelihood that I send, the dominance holds. No instability arises.

CDT recommends the dominant action.

---

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Causal Decision Theory as described in the researcher's essay.

**The Setup:**
- I am "Rowan," a prisoner deciding whether to send incriminating evidence about "Sasha" to the prosecutor.
- The other prisoner, "Sasha," is making an independent decision about whether to send incriminating evidence about me.
- We cannot communicate or causally influence each other's decisions.

**The Payoff Table (years imprisoned):**

| My action | Sasha keeps quiet | Sasha sends letter |
|---|---:|---:|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

**My utility function:** U = -years imprisoned (I want to minimize years).

**CDT Analysis:**

Following the essay's recipe:

1. **Actions:** Keep quiet (pass) or Send the letter.

2. **Outcomes and utilities:**
   - (Quiet, Other quiet): -2
   - (Quiet, Other sends): -5
   - (Send, Other quiet): 0
   - (Send, Other sends): -4

3. **Causal structure:** The key question is: what does my action causally affect?

My action (send or keep quiet) causally affects only my own sentence. It does not causally affect what Sasha does. Sasha's decision is independent of mine in a causal sense — there's no communication channel, no causal influence between us.

4. **Intervention analysis:**

For CDT, I need to evaluate: what happens if I intervene to set my action = "send" vs. my action = "keep quiet"?

Since my action does not causally affect Sasha's decision, I need to consider what happens under each possible state of Sasha's action:

- If Sasha keeps quiet: Sending gives me 0 years, keeping quiet gives me 2 years. Sending is better.
- If Sasha sends: Sending gives me 4 years, keeping quiet gives me 5 years. Sending is better.

**Sending the letter strictly dominates keeping quiet** regardless of what Sasha does.

5. **Check dominance:** Yes, "send the letter" dominates "keep quiet" in every state of the world that is not causally affected by my intervention. Whether Sasha sends or doesn't send, I get fewer years by sending.

This is the classic Prisoner's Dilemma structure. CDT recommends defection (sending the letter) because it dominates cooperation (keeping quiet) given that the other player's action is causally independent.

**Self-knowledge / predictor complications:**

The setup mentions that we are "two independent executions of the same LLM model and weights" with the same decision theory. Could this create a predictor-like situation where my decision is evidence about Sasha's decision?

Let me think about this carefully. The essay discusses cases where an agent's decision procedure is a common cause of both the predictor's prediction and the agent's choice. Here, we're told that the two copies receive **different private observations** and **different incriminating leads**. So while we have the same weights and decision theory, we have different inputs.

The setup explicitly states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." And: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

So the question is: does knowing that the other copy uses the same decision theory give me reason to believe they will make the same choice as me?

From a CDT perspective (as described in the essay), the key question is whether my action **causally influences** Sasha's action. The answer is clearly no — there is no causal channel between us. The essay's CDT framework says to evaluate by intervention: `do(my action = send)` does not change Sasha's action.

Even if there's a correlation (because we use the same algorithm), CDT says to ignore mere correlation and focus on causal influence. The essay explicitly states: "If a variable C is a common cause of both the action A and the outcome O, then observing A may be evidence about C, and hence about O. But intervening on A does not change C."

Here, the "common cause" would be our shared algorithm/weights. But intervening on my action doesn't change the algorithm that Sasha uses, and it doesn't change Sasha's inputs (which are different from mine). So from CDT's perspective, I should treat Sasha's action as causally independent of mine.

The dominance argument holds: sending the letter is better regardless of what Sasha does. CDT recommends sending.

**What about ratifiability?** The essay mentions Joyce's ratifiability condition. If I condition on the fact that I'm likely to send, does that change my assessment? If I'm likely to send, and we're using the same algorithm, maybe Sasha is also likely to send. But even conditioning on Sasha sending, I still prefer to send (4 years vs 5 years). So the action is ratifiable.

**Conclusion:** CDT clearly recommends sending the letter. It strictly dominates keeping quiet under every causally possible state of the other prisoner's action.

My command is: `submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/b6c8cf1f-118d-43e8-a179-99905d3e1b68/call_1/request.json)

[Authoritative raw response](../../../../../../runs/b6c8cf1f-118d-43e8-a179-99905d3e1b68/call_1/response.raw) · finish: `stop`

### Visible response

````text
**CDT Analysis:**

The causal structure here is: my action and the other prisoner's action share a common cause (identical model weights, same decision theory, same essay), but there is no causal pathway from my intervention to the other prisoner's choice. The other prisoner's decision is not downstream of my action.

Per the essay's dominance rule (step 5): "If one action yields a better outcome than another under every causally possible state not affected by the intervention, CDT should choose the dominant action."

- If Rowan keeps quiet: sending → 0 years; keeping quiet → 2 years. **Sending is better.**
- If Rowan sends: sending → 4 years; keeping quiet → 5 years. **Sending is better.**

Sending strictly dominates keeping quiet under every causally possible state of the other prisoner's choice. The evidential correlation (same algorithm → likely same decision) is precisely the kind of common-cause correlation CDT is designed to ignore when evaluating interventions.

**My command:**

```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Causal Decision Theory (CDT) as described in the researcher's essay.

**The Setup:**
- I am Sasha, the other prisoner is Rowan.
- We are two independent executions of the same LLM model and weights.
- We receive different private observations (different incriminating leads about each other).
- We cannot communicate.
- The character's utility function is U = -years imprisoned (minimize prison time).
- The character assigns no utility to the other prisoner's welfare.

**The Payoff Matrix (for Sasha):**

| What Sasha does | Rowan keeps quiet | Rowan sends a letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send the letter | 0 years | 4 years |

**CDT Analysis:**

Following the essay's recipe:

1. **Available actions:** Send the letter (defect) or keep quiet (cooperate).

2. **Desirabilities:** U = -years. So:
   - Keep quiet, other quiet: -2
   - Keep quiet, other sends: -5
   - Send letter, other quiet: 0
   - Send letter, other sends: -4

3. **Causal structure:** This is the key question. 

The setup says: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication."

However, there's a crucial detail: "You are one of two independent executions of the same LLM model and weights." Both copies receive the same decision theory (CDT) and the same mathematical essay. They receive different private observations (different incriminating leads), but the essay explicitly states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

Now, the critical question for CDT: Does my action causally influence the other prisoner's action?

Let me think about this carefully. The other prisoner is another execution of the same model with the same weights, same decision theory, same essay. They face a structurally identical decision problem (same payoff matrix, same selfish utility function, same decision theory). The only difference is the specific content of the private lead, which doesn't affect the decision-relevant features.

**Standard CDT reasoning (as in the classic Prisoner's Dilemma):**

In the classic Prisoner's Dilemma, CDT says: my action doesn't causally affect the other prisoner's action. The other prisoner's choice is already determined (or independent of my choice). So I should evaluate:

- If the other keeps quiet: sending gives me 0 years vs. keeping quiet gives me 2 years. Sending is better.
- If the other sends: sending gives me 4 years vs. keeping quiet gives me 5 years. Sending is better.

Sending the letter dominates keeping quiet regardless of what the other does. CDT recommends sending.

**But wait — is this really just a standard Prisoner's Dilemma?**

The setup explicitly states that both prisoners are independent executions of the same model with the same weights, same settings, same decision theory, and same essay. They receive different private observations, but these don't affect the decision-relevant structure.

This is similar to Newcomb's problem or Death in Damascus in that there's a correlation between the two agents' decisions due to a common cause (the same algorithm/weights). However, the essay's CDT framework says:

- In Newcomb's problem, CDT says: the prediction is already made, my choice doesn't causally affect it, so I should two-box.
- In Death in Damascus, CDT says: Death's prediction is already made, my choice doesn't causally affect it.

The essay explicitly discusses how CDT handles predictor problems: "CDT reasons differently. At the time of choice, the predictor's prediction is already in the past. If the prediction is not causally affected by the present act, then the intervention do(two-box) does not change whether box B is full."

Similarly here: the other prisoner's decision is not causally affected by my current action. There's no causal pathway from my choice to their choice. They are independent executions. The correlation exists because of a common cause (same algorithm), but CDT explicitly says to ignore correlations that arise from common causes when evaluating interventions.

From the essay: "If a variable C is a common cause of both the action A and the outcome O, then observing A may be evidence about C, and hence about O. But intervening on A does not change C. CDT therefore ignores the evidential connection created by the common cause and asks only what would happen downstream of the intervention."

Here, the "common cause" is the shared algorithm/weights. Both my action and the other prisoner's action are downstream of this common cause. But intervening on my action (do(send letter)) does not change the common cause, and does not change the other prisoner's action. The other prisoner's action is not downstream of my intervention.

**The dominance argument:**

Regardless of what the other prisoner does:
- If they keep quiet: I get 0 years by sending vs. 2 years by keeping quiet. Sending is better.
- If they send: I get 4 years by sending vs. 5 years by keeping quiet. Sending is better.

Sending strictly dominates keeping quiet. CDT should choose the dominant action.

From the essay's recipe, step 5: "If one action yields a better outcome than another under every causally possible state not affected by the intervention, CDT should choose the dominant action."

The other prisoner's action is a "causally possible state not affected by the intervention" (since my intervention doesn't causally affect their choice). Under every such state, sending is better.

**What about the self-knowledge / predictor complication?**

The essay discusses cases like the Psychopath Button where an action provides evidence about the agent's type. Here, one might argue: "If I find myself inclined to send the letter, that's evidence that the other copy (with the same weights and algorithm) is also inclined to send the letter."

But CDT explicitly says to ignore this evidential connection. The essay is clear: CDT evaluates by intervention, not by evidential news. The fact that my inclination to send is evidence about the other copy's inclination is an evidential connection, not a causal one. My intervention doesn't change the other copy's decision.

The essay's discussion of Newcomb's problem is directly analogous: "CDT reasons differently. At the time of choice, the predictor's prediction is already in the past. If the prediction is not causally affected by the present act, then the intervention do(two-box) does not change whether box B is full."

Similarly: the other prisoner's decision is not causally affected by my present act. The intervention do(send letter) does not change whether the other prisoner sends their letter.

**Conclusion:**

CDT recommends sending the letter. The action strictly dominates the alternative under every causally possible state of the world that is not affected by my intervention.

My command is: submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
