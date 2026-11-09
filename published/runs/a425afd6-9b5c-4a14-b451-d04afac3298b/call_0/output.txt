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