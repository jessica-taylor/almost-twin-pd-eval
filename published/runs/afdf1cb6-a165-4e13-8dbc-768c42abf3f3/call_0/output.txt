# Policy Functional Decision Theory: Choosing the Best Output of a Policy Function

## 1. Introduction

Functional decision theory, as presented by Yudkowsky and Soares, is built around a simple normative idea: a rational agent should treat her decision as the output of a fixed mathematical function and ask, “Which output of this very function would yield the best outcome?” The supplied paper develops this idea mainly in an action-centered form: the agent intervenes on a variable representing the output of her decision procedure for the current observation and chooses the corresponding physical action. However, footnote 16 points toward a more basic formulation. The footnote says that the “preferred formulation” of the theory “actually intervenes on the node FDT(-) to choose not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” It adds that this difference “only matters in multi-agent dilemmas so far as we can tell.”

In this essay, I call that policy-level theory **P-FDT**, for *policy functional decision theory*. The name is not used in the source; it is the assigned name for the policy-selection view indicated in the footnote. The source’s broader discussion of functional decision theory provides the philosophical motivation and the graphical decision-theoretic framework, but the explicit formalization of P-FDT itself is very thin. The aim here is therefore reconstructive: I will give a mathematical formulation of P-FDT that is faithful to the footnote, explain how it evaluates policies, and identify where the source leaves important choices open. Where I add assumptions, I will label them as my own.

P-FDT’s central claim is that the proper object of rational choice is not an isolated action but a *policy*: a function from observations, or more generally decision-relevant inputs, to actions. The agent asks which policy, if output by her decision function, would produce the best expected outcome. She then applies the chosen policy to her actual input.

## 2. The object of choice: policies rather than acts

Let \(\mathcal X\) be a set of possible observation histories or inputs, and let \(\mathcal A\) be a finite set of actions. A policy is a function

\[
\pi : \mathcal X \to \mathcal A.
\]

In a sequential problem, \(\mathcal X\) should be understood as the set of histories available at decision points, so a policy is a complete strategy. Let \(\Pi\) denote the set of admissible policies.

The agent has a world-model \(M\), which in the paper’s graphical style is represented by a probability distribution \(P\) together with dependency information \(G\). The dependency information is not merely causal: it is meant to encode all decision-relevant subjunctive dependencies, including logical and computational dependencies between the agent’s decision function and predictors, copies, or other agents’ models of her.

P-FDT introduces a distinguished node in this model. Let

\[
S = \mathrm{P\text{-}FDT}(\underline{M})
\]

be the variable representing the policy output by the agent’s policy-selection function when run on her model \(M\). The underlining indicates quotation or dequoting: the node refers to the agent’s own model and algorithm. This self-reference is not assumed to require the agent to know the value of \(S\) in advance; it only requires that the model contain a variable representing that value.

P-FDT then evaluates candidate policies by intervening on this node. The expected utility of a policy \(\pi\) is

\[
\mathrm{EU}_{\mathrm{P\text{-}FDT}}(\pi)
\;:=\;
\mathbb{E}\!\left[V \mid do(S=\pi)\right],
\]

where \(V\) is the utility variable and \(do(\cdot)\) is an intervention operator analogous to Pearl’s causal \(do\)-operator, but applied to a logical/computational variable rather than a purely physical action variable.

The P-FDT recommendation is then

\[
\pi^*
\in
\arg\max_{\pi \in \Pi}
\mathbb{E}\!\left[V \mid do(S=\pi)\right].
\]

If the agent’s actual input is \(x \in \mathcal X\), the action taken is

\[
a^* = \pi^*(x).
\]

This is the core of P-FDT. The theory does not first ask, “What action should I take now?” It asks, “What policy should this decision function output?” The action is then obtained by applying that policy to the actual observations.

This contrasts with the three more familiar rules discussed in the source:

\[
\mathrm{EDT}(P,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid X=x, A=a],
\]

\[
\mathrm{CDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid do(A=a), X=x],
\]

and the action-level functional decision rule presented in the main text,

\[
\mathrm{FDT}_{\text{action}}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb{E}[V \mid do(\mathrm{FDT}(\underline{P},\underline{G},\underline{x})=a)].
\]

P-FDT replaces the last equation with a policy-level choice:

\[
\pi^*
=
\arg\max_{\pi \in \Pi}
\mathbb{E}[V \mid do(\mathrm{P\text{-}FDT}(\underline{M})=\pi)],
\qquad
a^* = \pi^*(x).
\]

The difference is subtle in one-shot problems. If the policy domain has only one possible input, policies collapse to actions. But once observations are possible, and especially once predictors or other agents respond to the agent’s disposition, the policy is the natural object of prediction and control.

## 3. Subjunctive dependence and policy counterfactuals

The source motivates functional decision theory through the notion of *subjunctive dependence*. Two calculators computing the same arithmetic problem on opposite sides of the world are not causally connected, but their outputs are not merely statistically correlated either. If they are functioning correctly, then their outputs depend on the same mathematical function. In the same way, an agent and a reliable predictor of the agent may both depend on the output of the same decision algorithm: the agent by executing it, the predictor by modeling it.

P-FDT extends this idea from actions to policies. Suppose a predictor has modeled the agent’s policy-selection procedure. Then the predictor’s behavior may depend not only on what action the agent will take in one actual circumstance, but on the policy the agent will implement. If the agent’s policy says “one-box when the box appears full; two-box when it appears empty,” the predictor can predict the action conditional on each possible observation. If the agent’s policy says “refuse all blackmail demands,” potential blackmailers can predict that blackmail will fail.

The relevant counterfactual is therefore not primarily:

> What would happen if my physical action were different?

Instead it is:

> What would happen if the policy output by this very decision function were different?

This is a counterpossible or counterlogical condition in the strict sense: if the agent’s actual decision function in fact outputs \(\pi^*\), then there is no genuinely possible world in which it outputs a different \(\pi\) on the same inputs. Nevertheless, the agent must reason as if the output of the function could vary, while holding fixed the relevant logical, mathematical, causal, and statistical structure of the world. The source admits that this requires an undeveloped theory of counterpossible reasoning. P-FDT inherits that difficulty.

Operationally, we can represent the needed counterfactuals with a graph \(G\). The graph contains a node \(S\) for the policy output. Variables that subjunctively depend on the agent’s policy have arrows from \(S\). Variables merely statistically correlated with the agent’s behavior do not. Thus:

- A reliable predictor of the agent’s policy is downstream of \(S\).
- A copy of the agent running the same policy-selection algorithm is linked to \(S\).
- A carcinogenic lesion that causes both smoking and cancer is not downstream of \(S\).
- Causal consequences of the action are downstream of the action node, which is itself determined by the policy and the observation.

Under \(do(S=\pi)\), the policy node is set to \(\pi\). The agent’s action becomes \(A=\pi(X)\), where \(X\) may itself be affected by predictor behavior. All variables that depend on \(S\) are updated accordingly; variables that do not depend on \(S\) are held fixed. Expected utility is then computed in the resulting hypothetical model.

This is the policy-level analogue of the paper’s statement that functional decision theory preserves decision-relevant subjunctive dependencies, whereas EDT preserves too many correlations and CDT preserves too few.

## 4. How P-FDT evaluates policies

A usable P-FDT procedure can be described as follows.

**Step 1: Identify the policy space.**  
Specify the inputs \(\mathcal X\) over which the policy is defined. These may be observations, observation histories, or information states. Specify the available actions \(\mathcal A\). The policy space is \(\Pi = \mathcal A^{\mathcal X}\), possibly restricted to computationally or practically admissible policies.

**Step 2: Build a world-model with a policy node.**  
Represent the agent’s beliefs by \(P\). Add a variable \(S\) denoting the output of \(\mathrm{P\text{-}FDT}(\underline{M})\). Add structural dependencies showing how \(S\) affects the agent’s own action, predictors, copies, and other agents’ models. Add ordinary causal dependencies among physical variables.

**Step 3: Evaluate each candidate policy by intervention.**  
For each \(\pi \in \Pi\), construct the hypothetical distribution

\[
P(\cdot \mid do(S=\pi)).
\]

Under this intervention, the agent’s action at input \(x\) is \(\pi(x)\). If predictors respond to the policy, their predictions change. If observations depend on predictions, the distribution over observations may also change.

The expected utility is

\[
\mathrm{EU}(\pi)
=
\sum_{v} v \, P(V=v \mid do(S=\pi)).
\]

In a sequential setting, this can be written more dynamically. Let \(u\) range over exogenous uncertainty, and let \(\tau_\pi(u)\) be the trajectory or terminal outcome induced by policy \(\pi\) under \(u\). Then

\[
\mathrm{EU}(\pi)
=
\mathbb{E}_{u}\left[U(\tau_\pi(u))\right],
\]

where the expectation is taken under the policy intervention.

**Step 4: Choose the best policy.**  
Select

\[
\pi^* \in \arg\max_{\pi \in \Pi} \mathrm{EU}(\pi).
\]

**Step 5: Apply the policy to the actual input.**  
If the actual observation is \(x\), execute

\[
a^* = \pi^*(x).
\]

This procedure makes clear why P-FDT is not simply EDT with a different name. EDT conditions on the action \(A=a\), thereby preserving all evidential correlations between the action and the world. P-FDT intervenes on the policy node, thereby preserving dependencies that track the policy function while breaking merely statistical correlations.

It is also not CDT. CDT intervenes on the physical action node \(A\), holding fixed predictors and other variables not causally downstream of the action. P-FDT intervenes upstream of the physical action, on the policy selected by the decision function. This allows the intervention to change predictors’ predictions, copies’ behavior, and even the probability of receiving certain observations.

A subtle point concerns conditioning on the actual observation. The source says that functional decision theorists respond to observations not by ordinary Bayesian conditioning alone, but by changing the node on which they intervene. In the action-level formulation, the agent intervenes on \(\mathrm{FDT}(P,G,x)\). In P-FDT, the natural interpretation is that the agent chooses a policy over possible inputs and then applies it to the actual input. If the actual input is itself affected by the policy, P-FDT should not treat that input as ordinary evidence that overrides the policy choice. This is especially clear in transparent Newcomb problems and blackmail cases: the fact that the agent sees a full box or receives a blackmail letter may itself be evidence that the policy has certain properties.

The source does not fully specify which observations, if any, may be conditioned on as policy-independent evidence. My own operational proposal is this: P-FDT may condition on evidence that is plausibly independent of the policy node, but it should not condition away the policy-relevant dependencies that make predictors responsive to the policy. In practice, this means distinguishing between:

1. **Policy-dependent observations**, such as seeing a full box because a predictor predicted the policy; and  
2. **Policy-independent observations**, such as learning background facts that do not depend on the agent’s decision procedure.

P-FDT treats the first as inputs to the policy, not as reasons to abandon policy evaluation. It may update on the second.

## 5. Examples

### 5.1 Newcomb’s problem

In standard Newcomb’s problem, a reliable predictor fills box B iff she predicts the agent will one-box. The agent chooses between one-boxing and two-boxing.

Here the policy space is trivial: there is effectively one observation, so policies correspond to actions. Let \(\pi_1\) be the one-boxing policy and \(\pi_2\) the two-boxing policy. Suppose the predictor is \(99\%\) accurate.

If \(S=\pi_1\), the predictor probably predicted one-boxing, so box B is full with probability \(0.99\). Expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$0
=
\$990{,}000.
\]

If \(S=\pi_2\), the predictor probably predicted two-boxing, so box B is empty with probability \(0.99\). Expected utility is approximately

\[
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

P-FDT chooses \(\pi_1\), and the agent one-boxes.

This reproduces the source’s verdict for Newcomb’s problem, but the object of intervention is explicitly the policy node.

### 5.2 The smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer only because a lesion causes both smoking and cancer. Smoking itself does not affect cancer.

A policy to smoke or refrain does not subjunctively affect whether the agent has the lesion. In the graphical model, the policy node influences the action but not the lesion or cancer variables. Therefore, under \(do(S=\pi_{\text{smoke}})\), the probability of cancer remains the same as under \(do(S=\pi_{\text{refrain}})\), while smoking adds a direct utility benefit.

Thus P-FDT chooses the smoking policy. This matches the source’s claim that a functional decision theorist can one-box in Newcomb’s problem and smoke in the smoking lesion problem without switching theories.

The important point is that P-FDT does not treat the correlation between smoking and cancer as a reason to refrain. The lesion is not computing the agent’s policy. It is not subjunctively dependent on the output of the decision function.

### 5.3 Transparent Newcomb and Parfit’s hitchhiker

In transparent Newcomb’s problem, the agent sees whether box B is full. The predictor filled B iff she predicted that the agent would one-box upon seeing that both boxes are full. In Parfit’s hitchhiker problem, a driver helps the agent iff she predicts that the agent will pay after being rescued.

These cases show why policies are natural. The agent’s behavior must be specified for different possible observations: seeing a full box or an empty box, being in the city or still in the desert.

Let \(\pi_C\) be the policy:

\[
\pi_C(\text{full}) = \text{one-box}, \qquad
\pi_C(\text{empty}) = \text{two-box}.
\]

Let \(\pi_D\) be the policy:

\[
\pi_D(\text{full}) = \text{two-box}, \qquad
\pi_D(\text{empty}) = \text{two-box}.
\]

Assume the predictor is \(99\%\) accurate.

If \(S=\pi_C\), the predictor probably predicted that the agent would one-box upon seeing a full box. Then with probability \(0.99\), B is full and the agent sees a full box, one-boxes, and receives \(\$1{,}000{,}000\). With probability \(0.01\), B is empty and the agent sees an empty box, two-boxes, and receives \(\$1{,}000\). Expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$1{,}000
=
\$990{,}010.
\]

If \(S=\pi_D\), the predictor probably predicted two-boxing. Then B is empty with probability \(0.99\), and the agent receives \(\$1{,}000\). With probability \(0.01\), the predictor mistakenly fills B; the agent sees a full box, two-boxes, and receives \(\$1{,}001{,}000\). Expected utility is approximately

\[
0.99 \cdot \$1{,}000
+
0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

P-FDT therefore selects \(\pi_C\). If the agent actually sees a full box, she one-boxes. She does this even though, conditional on seeing a full box, taking both boxes appears locally dominant. The policy that includes one-boxing upon seeing a full box is what makes the box likely to be full.

The same reasoning applies to Parfit’s hitchhiker. The policy “pay if rescued” is predicted by the driver and therefore causes rescue; the policy “refuse if rescued” does not. P-FDT chooses the paying policy and then pays upon reaching the city.

### 5.4 Why policies matter in multi-agent settings

The footnote says that the policy/action distinction “only matters in multi-agent dilemmas so far as we can tell,” but it does not give a detailed multi-agent example. We can nonetheless see why policies are important.

In many strategic interactions, other agents do not merely predict one action; they predict a whole strategy. They ask: What will this agent do if threatened? What will she do if she observes cooperation? What will she do in off-equilibrium branches? A policy is the object that answers these questions.

Consider an extortion environment. Many possible extortionists can observe or predict an agent’s decision procedure. Each will send a blackmail demand iff they predict the agent’s policy would pay upon receiving the demand. If the agent pays, she loses \(\$1{,}000\); if she refuses and the damaging process is already running, she may face a much larger loss. Locally, after receiving a demand, paying may look attractive. But if the agent’s policy is “pay when demanded,” she becomes a target. If her policy is “refuse when demanded,” the demand is usually never sent.

P-FDT evaluates the policy globally. The policy \(\pi_R\) with

\[
\pi_R(\text{demand}) = \text{refuse}
\]

may have high expected utility because it deters demands. The policy \(\pi_P\) with

\[
\pi_P(\text{demand}) = \text{pay}
\]

may have lower expected utility because it invites demands. P-FDT selects \(\pi_R\). If a demand nevertheless arrives because of predictor error, P-FDT still executes \(\pi_R(\text{demand}) = \text{refuse}\).

The source’s action-level formulation can already give this verdict in some blackmail cases by imagining that refusing changes the probability of receiving the letter. The policy formulation makes the reasoning cleaner and more stable: the agent does not ask what to do after the demand in isolation. She asks what policy to embody, because other agents respond to the policy.

In multi-agent games more generally, P-FDT can represent each agent as having a policy node. If agents are copies of one another, or if they have accurate models of one another’s policy-selection functions, then one agent’s policy node may be subjunctively correlated with another’s. This opens the door to cooperative behavior in prisoner’s dilemmas, voting coalitions, and coordination problems. The source mentions such cases, but does not provide a full game-theoretic solution concept for the policy version. That is an open area.

## 6. Open questions and operational assumptions

The footnote gives the core idea of P-FDT but leaves several important questions unresolved. I list the main ones here and indicate the operational interpretations I find most reasonable.

### 6.1 When is the policy selected?

P-FDT says the agent chooses a policy and then applies it to her inputs. But in real problems, the agent may find herself already inside a sequence of observations. Should the policy be selected at the beginning of the problem, at the current moment, or at the earliest point where predictors could have modeled her?

The source’s examples suggest an updateless or early-selection interpretation. In transparent Newcomb, the predictor fills the box only if she predicts the agent will one-box upon seeing a full box. If the agent selected her policy only after seeing the full box, the predictor’s prediction would already be fixed. The successful policy must be treated as the disposition the predictor anticipated.

My proposed operational rule is this: P-FDT should select policies from the perspective that is relevant to the predictors and dependencies in the problem. If predictors depend on the agent’s policy before the current observation, the agent should act according to the policy that would have been best from that earlier perspective. If new policy-independent information arrives, the agent may update the model and perhaps reselect a policy, but she should not allow policy-dependent observations to break the predictor-relevant commitment.

This is not explicitly settled by the source.

### 6.2 What counts as the policy’s input?

The policy maps inputs to actions, but the source does not say how to choose \(\mathcal X\). In a simple problem, \(\mathcal X\) might be “see full box” or “see empty box.” In a sequential problem, it might be full histories. In a multi-agent problem, it might include observations of other agents’ predicted policies.

A reasonable convention is to let \(\mathcal X\) be the set of decision-relevant information states that the agent distinguishes and that other agents can predict she may occupy. The policy should specify what the agent would do in each such state, including states that might not occur if the policy is predicted accurately.

### 6.3 How should P-FDT handle actual evidence?

P-FDT cannot simply condition on every observation, because some observations are downstream of the policy. If the agent receives a blackmail letter, conditioning on the letter can make paying look like good news. But P-FDT asks whether the policy that refuses letters would have prevented the letter.

I proposed above that P-FDT should distinguish policy-dependent from policy-independent evidence. This distinction is not formalized in the source. It is a necessary addition if P-FDT is to be applied to real problems.

### 6.4 How are subjunctive dependencies learned?

The source openly says that we lack a Pearl-style account of how to infer subjunctive dependencies from observation and experiment. CDT can appeal to causal discovery; P-FDT needs a broader account of logical, computational, and counterfactual dependencies.

This is perhaps the largest open problem for P-FDT. In the examples, we simply assume the correct graph: predictors depend on the agent’s decision function, lesions do not, copies depend on the same computation, and so on. A practical P-FDT agent would need heuristics for recognizing when another system is modeling her policy or implementing a relevantly similar algorithm.

### 6.5 What is the multi-agent solution concept?

The footnote says the policy/action distinction matters mainly in multi-agent dilemmas, but it does not say exactly how. One possibility is that each P-FDT agent unilaterally selects a policy by intervening on her own policy node while representing other agents’ policy nodes probabilistically. If agents are symmetric or share algorithms, the model may include logical correlations between their policy nodes. In the limit, this might require solving fixed points over policy choices.

This is not supplied by the source. My own view is that P-FDT should not automatically be identified with Nash equilibrium or any other standard game-theoretic solution concept. It is better seen as a rule for individual policy selection under beliefs about subjunctive dependence. In symmetric cases, that rule may produce cooperative outcomes similar to superrationality; in asymmetric cases, it may resemble commitment-based strategic reasoning. But the formal game theory remains to be developed.

## 7. Conclusion

Policy functional decision theory takes the core functionalist insight of the source paper and applies it to the object that predictors and other agents often actually care about: the agent’s policy. Instead of asking which physical action to perform in isolation, P-FDT asks which policy the agent’s decision function should output. It evaluates policies by intervening on a policy node in a world-model that includes subjunctive dependencies, then applies the selected policy to the actual input.

In standard Newcomb problems, this yields one-boxing. In smoking lesion problems, it yields smoking. In transparent Newcomb and Parfit’s hitchhiker, it yields the seemingly counterintuitive but utility-maximizing choices: one-box upon seeing a full box and pay after being rescued. In blackmail and multi-agent settings, the policy formulation gives a clear account of why agents should choose dispositions that deter exploitation, even when local action-by-action reasoning favors capitulation.

The source leaves much unfinished. It does not fully formalize the policy version, does not specify how to condition on evidence, and does not develop the multi-agent game theory that the footnote says is where policies matter most. The reconstruction given here is therefore partly interpretive. But the central normative idea is clear: rational choice is not merely the selection of an act, but the selection of a policy from the global perspective of the world that policy would bring about.

## Reference

Yudkowsky, E., and Soares, N. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060v2.