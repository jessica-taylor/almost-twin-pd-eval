# A-FDT: Choosing the Output of a Decision Procedure

Decision-making becomes unusual when the world contains accurate models of the decision-maker. A predictor may reward an action before it occurs; a psychological twin may reach the same conclusion without communicating; a potential blackmailer may make a threat only when payment is predictable. In such cases, an action can be connected to important outcomes without physically causing them.

**Action functional decision theory (A-FDT)** evaluates these connections by treating an action as the output of a mathematical decision procedure. Its central question is not merely what would happen if one’s body performed a different act, but what would happen if the computation determining that act had a different output.

Here I take Equation (4), Section 5, of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality* as the defining presentation of A-FDT. This qualification matters: the paper also mentions a policy-selection variant, whereas Equation (4) selects an action. The discussion below separates the action-valued rule from that broader proposal, and distinguishes the paper’s commitments from additional modeling assumptions.

## 1. Expected utility and the choice of hypothetical

Let \(\mathcal A\) be a finite action set, \(O\) an outcome variable, and \(U(O)\) the agent’s utility. Write \(V=U(O)\), assuming expectations are finite. An expected-utility theory evaluates each action through some hypothetical outcome distribution:

\[
Q(a)=\sum_o U(o)\,P_a(o).
\]

The central disagreement between decision theories concerns the construction of \(P_a\).

**Evidential decision theory (EDT)** evaluates an action by conditioning on its occurrence:

\[
Q_{\mathrm{EDT}}(a\mid x)
=\mathbb E[V\mid X=x,A=a].
\]

**Causal decision theory (CDT)** instead uses a causal intervention:

\[
Q_{\mathrm{CDT}}(a\mid x)
=\mathbb E[V\mid \operatorname{do}(A=a),X=x].
\]

Conditioning asks what taking the action would indicate. Intervention asks what would follow from setting the action while breaking its usual dependence on upstream causes.

A-FDT also intervenes, but on a different variable. Let

\[
D_x
\]

denote the variable in the agent’s model representing the output of **this A-FDT procedure on the specific inputs \((P,G,x)\)**. Here:

- \(P\) is a probabilistic world-model;
- \(G\) describes relevant causal and noncausal dependencies;
- \(x\) is the observation history supplied to the decision procedure.

Rewriting the paper’s Equation (4) with this abbreviation gives

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}
\left[V\mid \operatorname{do}(D_x=a)\right].
}
\tag{A}
\]

A deterministic implementation additionally needs a fixed tie-breaking convention.

The distinction between \(D_x\) and the actual output is essential. \(D_x\) is a *representation* manipulated inside a model; \(\operatorname{A\!-\!FDT}(P,G,x)\) is the action eventually returned. Naming a computation’s output does not require already knowing it. The paper invokes self-referential programming constructions to explain how a procedure can contain a representation of itself.

Two features of (A) deserve emphasis. First, its intervention target is a computational output, not the physical action. Second, there is **no additional conditioning on \(X=x\)** inside its expectation. Observation changes which variable is targeted, from \(D_x\) to \(D_y\), rather than simply restricting the hypothetical distribution to the observations actually received.

That second feature is responsible for several of A-FDT’s most distinctive recommendations.

## 2. Subjunctive dependence and counterpossible intervention

The paper calls the relevant relationship **subjunctive dependence**. Two physical systems computing the same function on the same input have outputs constrained to agree, even if neither causally influences the other. Accurate predictors provide an approximate version of this relationship.

Suppose two isolated computers execute the same deterministic program on identical inputs. Changing only the displayed output of one computer leaves the other unchanged. But changing the represented answer to their shared computation changes what both should display. A-FDT treats the latter hypothetical as relevant when evaluating the computation’s decision.

This does not license preserving every correlation. A disease correlated with an action through an upstream biological condition need not depend on the output of the agent’s decision procedure. Nor does merely sharing a decision-theory label establish dependence between two agents with different preferences or information.

The difficulty is that a fixed mathematical function has only one output on a fixed input. If it actually outputs \(a\), the supposition that it outputs \(b\ne a\) is counterpossible: it conflicts with a mathematical fact.

Consequently,

\[
P(\,\cdot\mid \operatorname{do}(D_x=b))
\]

cannot simply mean ordinary conditioning on a consistent logical proposition. The paper proposes reusing graphical intervention machinery once the required dependency structure has been supplied. It explicitly leaves open how that structure should be discovered or fully justified.

### A useful operational interpretation

For finite examples, I propose interpreting \(G\) through an augmented structural model. Let its variables satisfy equations

\[
Z_i=f_i(\operatorname{Pa}_i,E_i),
\]

where the exogenous variables \(E_i\) have a specified joint distribution. Include computational-output variables such as \(D_x\), physical actions, predictions, observations, and utility.

To evaluate \(a\):

1. Replace the defining equation for \(D_x\) by \(D_x:=a\).
2. Preserve the other structural equations and the exogenous distribution.
3. Recompute dependent variables.
4. Average the resulting utility.

In an acyclic model this produces a concrete calculation. It is an operational interpretation of the paper’s graphical proposal, not a general solution to logical counterfactuals.

The modularity assumption is substantial. We suspend one represented computational fact without allowing arbitrary logical consequences of a contradiction. Which equations should survive that suspension is precisely what the dependency model must specify. A graph’s arrows alone are therefore insufficient: quantitative response rules, including predictor-error mechanisms, are also required.

## 3. A-FDT in prediction, correlation, and coordination problems

### Newcomb’s problem

An opaque box contains either \(M\) dollars or nothing. A transparent box contains \(k\) dollars. A predictor filled the opaque box if it predicted that the agent would take only that box.

Let the computational output be

\[
D\in\{\text{one},\text{two}\}.
\]

The relevant structure is

\[
D\longrightarrow A,
\qquad
D\longrightarrow R\longrightarrow B,
\]

where \(R\) is the prediction and \(B\) the opaque-box contents. The arrow from \(D\) to \(R\) represents computational dependence, not a physical signal traveling backward in time.

Assume a symmetric prediction channel with accuracy \(r\):

\[
P(R=D\mid\operatorname{do}(D=a))=r
\]

for either candidate output. Then

\[
Q(\text{one})=rM,
\qquad
Q(\text{two})=(1-r)M+k.
\]

Thus A-FDT one-boxes exactly when

\[
(2r-1)M>k.
\]

For \(M=1{,}000{,}000\), \(k=1{,}000\), and \(r=0.99\), the scores are \(990{,}000\) and \(11{,}000\).

More generally, define

\[
p_1=P(B=\text{full}\mid\operatorname{do}(D=\text{one})),
\]
\[
p_2=P(B=\text{full}\mid\operatorname{do}(D=\text{two})).
\]

The criterion becomes

\[
M(p_1-p_2)>k.
\]

This formulation exposes an important implementation assumption: a predictor’s historical accuracy does not by itself determine its response under every computational intervention. The symmetric error channel is an additional model, matching the paper’s intended example.

A-FDT does not claim that reaching toward one box physically refills another. It evaluates alternative outputs of a computation whose representations helped determine the earlier prediction.

### The smoking lesion

Now suppose an imaginary lesion \(L\) both encourages smoking and causes cancer \(C\), while smoking itself has no health effect. Consider an agent for whom smoking supplies a positive utility increment \(s\).

If changing the relevant decision output does not change \(L\) or \(C\), then, in a simple model where that output controls the action,

\[
Q(\text{smoke})-Q(\text{refrain})=s>0.
\]

A-FDT therefore smokes in this fictional problem. The action’s evidential connection to cancer is not preserved as a dependence running from the computational output to the lesion.

The paper’s detailed treatment is more complicated because the lesion changes preferences, thereby changing the inputs to the decision procedure. It introduces distinct computational nodes for distinct utility functions, with the lesion selecting which node controls behavior. The pro-smoking node still favors smoking, but its expected gain is weighted by the probability that it controls the physical action.

The authors also acknowledge that the traditional smoking-lesion setup is contrived, particularly its assumptions about ignorance of one’s own preferences. The robust lesson is structural: **an upstream cause of an action need not change under intervention on the computation producing that action**.

### Psychological twins

In the paper’s twin prisoner’s dilemma, mutual cooperation pays each player \(1{,}000{,}000\), mutual defection pays \(1{,}000\), and unilateral defection pays the defector \(1{,}001{,}000\).

Assume both players implement the same decision computation with identical decision-relevant inputs. Then

\[
A_1=D,\qquad A_2=D.
\]

A-FDT compares

\[
Q(\text{cooperate})=1{,}000{,}000,
\qquad
Q(\text{defect})=1{,}000.
\]

Cooperation follows without altruism.

The assumption of computational identity does the work. Against an independent opponent whose behavior does not depend on this computational output, defection remains preferable. For imperfectly similar agents, one needs an explicit model of how the opponent’s action responds to each intervention—not an unsupported inference that rational agents must agree.

## 4. Observations select the intervention target

The transparent version of Newcomb’s problem illustrates why Equation (A) is not merely CDT with extra arrows.

Suppose the predictor fills the large box if it predicts that the agent would one-box **upon seeing it full**. Introduce

\[
D_F=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
D_E=\operatorname{A\!-\!FDT}(P,G,\text{empty}).
\]

These are outputs on different inputs. Sharing a procedure does not make them the same variable.

The prediction depends on \(D_F\). Its result determines the box contents, which determine which node controls the physical action:

\[
A=
\begin{cases}
D_F,&B=\text{full},\\
D_E,&B=\text{empty}.
\end{cases}
\]

After seeing a full box, A-FDT intervenes on \(D_F\), but does not condition the evaluation on the box remaining full.

Let \(q\) be the model’s probability that \(D_E=\text{two}\), unchanged by the intervention. With symmetric prediction accuracy \(r\),

\[
Q(D_F:=\text{one})
=rM+(1-r)qk,
\]

whereas

\[
Q(D_F:=\text{two})
=(1-r)(M+k)+rqk.
\]

At \(r=0.99\), one-boxing wins for every \(q\in[0,1]\). Although the agent actually sees a full box, its hypothetical for \(D_F:=\text{two}\) usually contains an empty box and execution of \(D_E\).

This is not a factual belief that the observed box might secretly be empty. It is a decision hypothetical in which the output determining the predictor’s behavior differs.

Parfit’s hitchhiker has the same structure. A driver rescues an agent only when predicting that the agent will pay afterward. Upon reaching safety, A-FDT evaluates the output of its *pay-after-rescue* computation. Altering that output also alters the prediction and hence the probability of rescue. With sufficiently reliable prediction and sufficiently valuable survival, it pays.

### Does A-FDT ignore evidence?

No: evidence changes the targeted computational node. But it does not necessarily remain fixed across the resulting hypotheticals.

In ordinary cases this distinction can disappear. Suppose observing \(x\) has an intervention-independent probability \(p_x>0\), and changing \(D_x\) affects utility only when \(x\) occurs. Then

\[
Q(a)=p_x\,\mathbb E[V_a\mid X=x]+C,
\]

where \(C\) is independent of \(a\). Maximizing the unconditional score gives the same answer as maximizing conditional expected utility.

The distinctive behavior arises when changing \(D_x\) changes whether \(x\) occurs, or affects other implementations of the computation.

A remaining uncertainty concerns the reference model: which earlier evidence is already incorporated into \(P\), and which possible observations must remain represented as branches? The examples make the intended treatment clear locally, but the paper does not provide a complete general construction. Simply replacing \(P\) with a posterior conditioned on the current observation can destroy the behavior Equation (4) was designed to capture.

## 5. A-FDT and prediction-based blackmail

Suppose a blackmailer launches a damaging mechanism only when predicting payment. Paying costs \(c\); refusing after launch incurs damage \(L\).

Let \(D_B\) represent the agent’s response upon receiving the demand. Assume launch is certain if \(D_B=\text{pay}\), but occurs with probability \(\varepsilon\) if \(D_B=\text{refuse}\). This explicitly specifies the predictor’s asymmetric errors.

Taking no blackmail as utility zero,

\[
Q(\text{pay})=-c,
\qquad
Q(\text{refuse})=-\varepsilon L.
\]

A-FDT refuses when

\[
\varepsilon L<c.
\]

For \(c=1{,}000\) and \(L=1{,}000{,}000\), the threshold is \(\varepsilon=0.001\). At \(\varepsilon=0.0009\), refusal has expected loss \(900\), so A-FDT refuses—even upon receiving the exceptional demand.

This is not categorical stubbornness. If the probability of being threatened despite predictable refusal is sufficiently high, paying can win. Nor does the result apply automatically to ordinary extortion. If launch is independent of the response computation, the claimed deterrence disappears; paying may then minimize loss.

The practical question is not whether one wishes to discourage blackmail. It is whether the threat’s occurrence actually depends on the computational output being evaluated.

## 6. Using A-FDT—and recognizing its limits

Applying A-FDT begins with identifying the precise computation under consideration: its procedure, model, utility specification, and observation input. One then separates several relationships that ordinary correlation conflates: physical causation, shared computation, predictive modeling, upstream common causes, and accidental association.

For each candidate action, the model must say which variables change, through which mechanisms, and with what probabilities. Uncertain dependencies should be represented rather than resolved by rhetoric. For example, a mixture over “faithful simulator” and “independent guesser” models can generate different intervention scores. Such Bayesian averaging over dependency models is a reasonable extension, but the paper does not supply a complete method for learning those models.

A-FDT also must not be silently replaced by global policy optimization. For fixed \(P,G\), its input-indexed decisions induce a mapping

\[
\pi(x)=\operatorname{A\!-\!FDT}(P,G,x).
\]

Nevertheless, Equation (A) intervenes on one output \(D_x\), not directly on the whole mapping \(\pi\). Other outputs change only where the dependency model says they should. The policy-selection variant mentioned in the paper’s footnotes instead optimizes over observation-to-action mappings. Equivalence between these approaches requires additional assumptions; the authors themselves note possible differences in multi-agent settings.

Philosophically, A-FDT challenges the supposed neutrality of causal dominance. Two-boxing is better if one holds box contents fixed while changing only the physical action. One-boxing can be better if one preserves the predictor’s computational dependence. Which comparison is relevant is the disputed issue, not something dominance settles independently.

The paper’s appeal to expected-utility representation likewise establishes compatibility with a general framework of coherent valuation, not the correctness of a particular dependency graph.

Finally, the examples do not prove universal superiority. The authors acknowledge that environments can reward or punish particular procedures directly. Their proposed restriction to “fair” problems remains informal, and they explicitly leave general optimality unresolved. Self-reference is representable, but that alone does not establish consistency or tractability for every reflective world-model.

### References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2), especially §§3–6, 9, and footnotes 7 and 16.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
- Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT evaluates actions by intervening on the represented output of the decision computation producing them. Its hypotheticals preserve relevant computational and predictive dependencies while breaking merely evidential associations; they may also change which observations occur. Given an adequate dependency model, Equation (4) supplies a concrete expected-utility rule. The principal unfinished task is constructing that model reliably: deciding which relationships should survive a counterpossible change in a computation’s output.