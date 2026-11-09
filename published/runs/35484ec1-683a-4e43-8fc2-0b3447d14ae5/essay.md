# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

A-FDT (action functional decision theory) is the version of functional decision theory presented in Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." Its action-level form selects an action, whereas the paper's preferred version selects a policy. I return to that distinction below. I use "A-FDT" throughout for this action-selecting rule and name other theories (EDT, CDT) separately.

All three theories in the paper are expected-utility maximizers. They differ only in the "epistemic perspective" used to evaluate an action, that is, in how they read the connective "a ↪ o" in

EU(a) = Σ_j P(a ↪ o_j ; x) · U(o_j).

EDT reads it as conditioning, P(o_j | x, a). CDT reads it as a causal intervention on the physical act. A-FDT reads it as an intervention on the *output of the agent's decision function*.

## 2. The formal definition

The agent has a world-model (P, G). P is a probability distribution over variables, and G is a graph saying how changing one variable propagates to others. Unlike a purely causal graph, G encodes *subjunctive dependence*, which includes logical and computational dependence. The agent also has an observation x. Equation (4) reads:

FDT(P, G, x) := argmax_{a∈𝒜} E[ V | do( fdt(⌜P⌝, ⌜G⌝, ⌜x⌝) = a ) ].

Here V = U(Outcome), and fdt(⌜P⌝,⌜G⌝,⌜x⌝) is a variable in the model standing for the output of this very algorithm on these inputs. The underlines or quotes mean dequoting: the variable's name depends on its inputs. The self-reference is harmless. The agent need not know the value of fdt(P,G,x) in order to have a variable representing it, and Kleene's recursion theorem (quining) shows such self-representation is constructible.

The procedure is as follows.
1. Build (P, G) and record the observation x.
2. Locate the node fdt(P,G,x).
3. For each action a, perform Pearl's do-surgery on that node, setting it to a and propagating the change to everything that G says depends on it.
4. Compute E[V] in each resulting hypothetical.
5. Output the maximizer.

Two differences from CDT (Equation 3) matter.

- **Where the intervention lands.** CDT intervenes on the token Act, and A-FDT intervenes on the type, the function's output. The nodes downstream of that output include the agent's own act, twins, and predictors who model the agent.
- **How observations enter.** CDT conditions on Obs = x. A-FDT does *not* condition. It changes which node it intervenes on, namely fdt(P,G,x) versus fdt(P,G,y). Observation selects an input of the function rather than updating the distribution.

The paper says when the three theories agree: when every correlation between Act and other variables is caused by Act (apart from possible dependence on the fdt node), then E[V|a] = E[V|do(a)] = E[V|do(fdt=a)]. They diverge when something correlates with the action without being caused by it, as with predictors, twins, and lesions.

## 3. Subjunctive dependence

Two systems subjunctively depend on a function if both compute it. Examples are two calculators evaluating 6288+1048, or a predictor's accurate model of an agent. The paper's claims about this concept:
- Causal dependence is a special case. A scribe copying a calculator depends on it both causally and subjunctively.
- Mere statistical correlation does not suffice. Two pink calculators are correlated, but a different purchase would not change the other's colour.
- It comes in degrees, since predictors can err or the agent can be noisy.

Evaluating do(fdt = a) for the action the function does not actually output is a *counterpossible*. The paper concedes this is the main weakness of the theory relative to CDT. It argues the difficulty is technical, not philosophical, since humans reason sensibly under logical uncertainty. It also notes the agent needs only a narrow capability: how a given predictor's output would change if the algorithm's output changed.

## 4. The open problem and one operational reading

The paper is candid. Equation (4) works *given* a graph G that correctly encodes how changing a logical variable affects other variables. How to obtain such a graph from observation, as Pearl's methods do for causation, is called "perhaps the largest open problem." Footnote 9 says the dependence structure is "required as an input," just as causal structure is for CDT. The theory therefore has no algorithm for building G.

An operational interpretation (my proposal, not the paper's) is a modelling recipe. For each entity in the problem, ask whether its behaviour is a function of this algorithm's output on some input. That covers copies, simulations, and reliable predictors. If so, draw an edge from the fdt node to it. If its connection to the agent is only a common cause with no computation of the agent's decision, draw no edge. The distinction the paper draws, "predictor versus lesion," is exactly this test. A heuristic check is to ask whether the entity's behaviour would change if the agent's decision procedure had been different, not merely if the agent's body had acted differently. The weak points are intermediate cases, such as a predictor who uses coarse behavioural statistics, and the modeller's choice of granularity. I flag these as places where A-FDT's output depends on modelling judgment.

## 5. Worked examples

**Newcomb's problem.** Fiona's graph has the node fdt pointing to both Act and Prediction. Prediction determines Box B. Accuracy is 0.99.
- do(fdt = onebox): Act = onebox, P(full) = 0.99, so E[V] = $990,000.
- do(fdt = twobox): Act = twobox, P(full) = 0.01, so E[V] = $11,000.

She one-boxes. No retrocausation is invoked. She simply refuses to imagine her action varying while the predictor's model of her stays fixed. Carl (CDT) holds P(full) = p fixed, gains $1,000 either way, and two-boxes.

**Smoking lesion.** Here the graph differs. The lesion causes both the desire to smoke and cancer. The fdt node feeds Act but has no edge to Cancer. Intervening on it leaves P(lesion) at p, so smoking beats refraining by p·$1,000 (the paper models two utility functions, since the lesion fixes which decision function runs). The agent smokes. The example shows that A-FDT needs a different graph from Newcomb's even when the probabilities look isomorphic; Carl can reuse his, and Eve (EDT) reuses her distribution, but Fiona cannot.

**Transparent Newcomb / Parfit's Hitchhiker.** Observation of a full box selects the node fdt(P,G,full). The Prediction variable determines which node, fdt(…,full) or fdt(…,empty), controls Act. Setting fdt(…,full) = twobox makes the box probably empty, so the agent would be running a different input-node. With accuracy 0.99 and q her prior probability of two-boxing upon seeing an empty box, the paper gets ≈$990,000 + 0.01q·$1,000 for one-boxing, versus $10,000-scale values for two-boxing. She one-boxes even while looking at the full box. Hitchhiker has the same structure: she pays because the kind of agent who pays is the kind who gets rescued.

**Blackmail.** In the mechanical blackmail problem, paying means being blackmailed almost surely and losing $1,000. Refusing means (against a perfect predictor) never being blackmailed. With an imperfect predictor that errs with probability ε, refusing costs about ε·$1,000,000 in expectation in the paper's example, against $1,000 for paying. So the break-even is ε = 0.1%: she refuses at ε = 0.09% and pays at 0.011%, per the paper's worked numbers. The paper stresses that she may hold the letter in her hands, know the predictor erred, and still refuse. In XOR blackmail the refusal is driven by something else: intervening on fdt changes whether the letter arrives but not the termite probability. Eve instead pays, because conditioning on pay makes termites improbable.

**Death in Damascus.** Death's book entry depends on the fdt node, so staying implies Death in Damascus and fleeing implies Death in Aleppo. Fiona stays and saves $1,000. Carl's hypotheticals hold Death fixed, which produces the unstable oscillation and a refusal to pay even $1 for a truly random coin.

## 6. Interpretive notes

**Updating.** A-FDT does change behaviour with evidence, but through the choice of input to the function, not through conditioning. This is why it is "updateless" in spirit. The paper notes that Yudkowsky's earlier Timeless Decision Theory both conditioned *and* shifted the intervention point, producing a harmful "double update."

**Actions versus policies.** The paper's footnotes say the authors' preferred formalization intervenes on a node that outputs a *policy* (a map from observations to actions) and then applies the observation. The paper says this matters only for certain multi-agent dilemmas, so Equation (4) is presented at the action level. A-FDT in this essay therefore means the Equation (4) action-level rule. A policy-level version is an extension supported by the source's footnotes, but its details are not developed there.

**Dominance.** Any hypothetical-construction rule induces its own dominance principle. A-FDT dominance holds fixed the subjunctive dependencies; under it, two-boxing in Newcomb's problem is not dominant. The paper's main justification is accordingly not dominance but *utility achieved* in "fair" problems, where outcomes depend only on the agent's behaviour in the problem at hand and the agent's model is accurate. The authors admit they lack a formal definition of fairness and note a counterexample: a problem that punishes whoever acts like a copy of Fiona is unfair to her.

**Metaphysics.** The authors claim A-FDT needs no doctrine of free will. Their parity argument is that a deterministic CDT agent also "imagines" varying a token it cannot really vary, so objections to controlling a type apply equally to a token.

## 7. What is source and what is mine

From the source: Equation (4); the do-surgery on the fdt node; observation changing the intervention node; the examples and numbers above; the claim that G is a required input; the stated difficulty of counterpossibles and of inferring G; the fairness discussion.

My additions: the modelling test for edges (computing-the-function versus merely correlated); the remark that the Newcomb-versus-lesion graphs make A-FDT depend on modeller judgment; the explicit summary of the pipeline. These are interpretive aids, not claims of the paper.

## 8. Using it on a new case

1. List the variables and identify every process that computes or models the agent's decision function, with its accuracy.
2. Build G: edges from the fdt node(s) to the agent's act and to those processes; ordinary causal edges elsewhere; none for mere common causes.
3. Create one fdt node per possible observation, with the act controlled by whichever applies.
4. For each candidate output, intervene, propagate, and compute E[V]. Include worlds where the agent would have observed something different.
5. Choose the maximum. Sanity-check against the "precommitment test": would a sensible advance commitment agree?

## 9. Conclusion

A-FDT keeps expected-utility maximization and Pearl-style surgery but moves the surgery from a physical act to the logical output of the agent's own decision procedure. This lets it one-box, smoke, pay the hitchhiker, refuse blackmail, and stay in Damascus with a single rule. Its price is a dependence on subjunctive-dependence graphs and counterpossible reasoning that the paper explicitly does not know how to construct or ground systematically. Until that gap is closed, A-FDT is a precise decision rule that depends on a modelling input it cannot yet derive.