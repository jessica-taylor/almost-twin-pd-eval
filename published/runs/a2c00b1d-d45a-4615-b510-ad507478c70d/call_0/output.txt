# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the version of functional decision theory given by Equation (4) of Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. It is an expected-utility theory. Its distinctive feature is where it makes the counterfactual cut: not at a physical act, but at the output of the agent's decision function. This essay states the rule, applies it to several problems, and separates what the paper establishes from what I add.

## 2. The formal setting

The paper defines expected utility as 𝓔𝓤(a) = Σⱼ P(a ↪ oⱼ; x)·U(oⱼ). Here a ranges over a finite action set, x is the observation history, and ↪ is a "decision hypothetical" connective. Citing Joyce's representation theorem, the paper says that EDT, CDT and FDT agree on the expected-utility form and differ only in the "epistemic perspective", that is, in how ↪ is read. Joyce's own phrase, quoted there, is that decision theories "disagree about the epistemic perspective from which actions are to be evaluated."

The paper's schema is as follows. The agent keeps a world-model M. For each action a she builds a hypothetical M^{a↪}, a transient mental object, "like notes on scratch paper". She computes a value V_a from it and takes the action with the highest value. The three theories differ in what M is and how the hypothetical is built:

- **EDT:** argmax_a E(V | Obs=x, Act=a). The hypothetical is Bayesian conditioning.
- **CDT:** argmax_a E(V | do(Act=a), Obs=x). M is (P, G) with G a causal graph, and the hypothetical is Pearl surgery on the physical act.
- **A-FDT (Equation 4):**

  A-FDT(P, G, x) := argmax_{a∈𝒜} E( V | do( fdt(⌜P⌝, ⌜G⌝, ⌜x⌝) = a ) ).

The underlined (quoted) arguments mean that fdt(P,G,x) is a *variable in the model* that represents the output of the A-FDT procedure on those very inputs. The self-reference is harmless, because the agent need not know the value of A-FDT(P,G,x) to have a variable representing it. The paper cites Kleene's second recursion theorem ("quining") for this.

The paper names two differences from CDT:

1. A-FDT intervenes on the node for the decision function's output, not on the physical-act node.
2. A-FDT does not condition on observations. Seeing x changes *which node* is intervened on, from fdt(·,·,x) to fdt(·,·,y). It does not change the distribution.

The graph G must encode subjunctive dependence: it says which variables would change if the function's output changed. These include the agent's own act, predictions of her, and the behavior of twins. It must also say which variables would not change, such as a lesion or a termite infestation. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

## 3. What is claimed and what is open

The paper gives a *conditional* procedure. The inputs P and G are supplied, as causal structure is supplied to CDT. Three things are not given:

- a method for learning G's subjunctive-dependence edges from observation (the paper calls this "perhaps the largest open problem");
- a definition of a `true` operator for counterpossible conditioning, which the paper explicitly says it lacks;
- a formal notion of "fair" problems.

The paper also says its preferred formalization intervenes on *policies* (maps from observations to actions) rather than on single outputs. Equation (4) is the action-indexed version, and footnotes 7 and 16 say the difference matters only in multi-agent cases. I follow Equation (4) throughout.

**My operational reading** (my addition, not the paper's): treat subjunctive dependence as the answer to the question "if this computation returned a different value, which quantities in the world would be different?" In practice there are three kinds of link:

- (a) The agent's own act (and her later acts in identical situations).
- (b) Any process that implements the same function, or contains an accurate model of it. Examples are twins, predictors and blackmailers who simulate the agent.
- (c) Nothing else. In particular, mere statistical correlation through a common cause does not count (the paper's pink calculators).

To build G, ask whether the correlated variable is *computing or modeling your decision procedure*. If it is, it hangs below the fdt node. If it is correlated only through a shared cause that does not read your output, it hangs elsewhere and is held fixed. The paper's illustration is the contrast between a predictor and a lesion. This heuristic cannot replace a theory of dependence discovery, but it settles all the paper's examples.

Note also that fdt(·,·,x) for different x are different nodes. When an agent faces observation x, she intervenes on the node for x. Other nodes (what she would do on other observations) stay in the model, and the graph says how they feed the act. A hypothetical in which x would not have been observed is therefore possible, because the intervention can change what is observed.

## 4. Worked applications

**Newcomb's problem.** The paper's graph for Fiona (the A-FDT agent) has fdt → Act and fdt → Prediction, with Accurate also feeding Prediction. Then:

- do(fdt=onebox): Act=onebox, P(full)=0.99, so E[V]=0.99·1,000,000 = $990,000.
- do(fdt=twobox): Act=twobox, P(full)=0.01, so E[V]=0.01·1,000,000 + 1,000 = $11,000.

A-FDT one-boxes. Equation (1) is applied directly, and no retrocausation is invoked. The paper stresses that the hypothetical simply refuses to separate act from prediction.

The CDT agent (Carl) intervenes on Act, which has no arrow to Box B. For any p = P(full), two-boxing is better by $1,000. The EDT agent (Eve) conditions and gets $999,000 versus $11,000, so she one-boxes. This holds unless her prior on one-boxing is extreme (probability 1 for two-boxing), which is Spohn's point that EDT can be pushed to do anything.

**Smoking lesion.** Here the graph is different. Lesion → Act and Lesion → Cancer, but fdt is not connected to Cancer. The paper makes the lesion fix the agent's utility function (U_S versus U_R), so there are two possible function-nodes, and the lesion selects which one controls Act. The probability of lesion is p whatever fdt is set to. Smoking therefore beats refraining by p·$1,000, and A-FDT smokes. One rule yields one-boxing in Newcomb and smoking here; only G changed. (The paper itself calls this problem contrived and recommends abandoning it.)

**Transparent Newcomb and Parfit's hitchhiker.** Here A-FDT's difference from CDT is most visible. Fiona sees a full box, so she intervenes on fdt(·,·,full). Her model has Prediction determine which function-node controls Act. If this function outputs onebox, the predictor (modeling it) fills the box. If it outputs twobox, the box is probably empty, and in that world her act is governed by fdt(·,·,empty). With q her credence that she two-boxes on seeing empty:

- onebox: 0.99·1,000,000 + 0.01·q·1,000 ≈ $990,000.
- twobox: 0.01·1,001,000 + 0.99·q·1,000, which is small. (The paper prints this with a typo, "$110,00".)

A-FDT one-boxes while staring at a full box. The paper notes this is *equivalent to paying in Parfit's hitchhiker*. The agent who would pay is the agent the driver rescues. Neither Carl nor Eve can honestly promise to pay, so both are left in the desert.

**Mechanical blackmail.** On seeing the letter, A-FDT compares do(fdt(·,·,blackmail)=pay) with do(…=refuse). Paying makes blackmail near-certain and costs $1,000. Refusing makes blackmail near-impossible, since the blackmailer's prediction tracks the function. So A-FDT refuses and is never blackmailed. With an imperfect predictor, the paper's numbers show how the threshold works. If the blackmailer wrongly predicts payment with probability 0.0009, refusal costs 0.0009·$1,000,000 = $900 in expectation, which is less than $1,000, so A-FDT refuses. If the error rate is 0.011% (0.00011), refusal costs $110 > $… as the paper says: at that rate, she pays. I note the arithmetic is worth checking before use. The point is that the comparison is between whole hypothetical worlds, not between outcomes given the letter.

**XOR blackmail.** Carl and Fiona both refuse, for different reasons. Carl holds the infestation fixed because it is causally upstream. Fiona sees that changing the function's output changes whether the letter arrives but not whether there are termites. Eve conditions on the letter, sees that paying is "good news", and pays.

**Death in Damascus.** Fiona knows Death's book was written by predicting her decision function. Changing the output therefore changes where Death waits, and she stays and saves $1,000. Carl's hypotheticals hold Death fixed, so his CDT preferences flip with each belief revision.

**Cosmic ray problem.** A-FDT takes the $100. It treats the statistical correlation between taking $100 and being hit by a ray as breakable, and Eve cannot break it.

## 5. Why this construction

The paper's diagnosis is that EDT's hypotheticals respect too many act–environment correlations, and CDT's respect too few. A-FDT keeps exactly those that follow from the logical or computational structure. Its claims are as follows:

- **Counterpossibles.** A deterministic function has only one output, so the hypothetical is counterpossible. The paper's reply is that CDT has the analogous problem for a deterministic physical agent's "token", so the objection cannot decide between the theories.
- **Dominance.** CDT-style dominance holds act-independence fixed. A-FDT has its own dominance principle, in which "all relevant subjunctive dependencies" are held fixed, and every hypothetical-building method yields its own notion of dominance. The paper therefore prefers utility achieved as the arbiter.
- **Fairness.** A problem that rewards or punishes *actions* (even predicted ones) is fair; one that punishes using a particular procedure is not. The paper concedes it lacks a formal criterion, and footnote 15 gives a copy-of-Fiona example showing the obstacle.
- **Reflective stability.** The paper claims A-FDT "always acts as it would have precommitted to act", so it has no need for binding mechanisms and no negative value of information.
- **Coordination.** The paper's examples include voting (ten agents must each pay $1,000 to vote, and A-FDT agents vote) and gym attendance across days.

## 6. A procedure, and where it needs more

A usable recipe, with the paper's parts marked:

1. Specify outcomes, utility, and the observation x. (Paper.)
2. Identify every process that computes, models or copies your decision procedure, and every future instance of it. (My heuristic, consistent with the paper.)
3. Build G with the node fdt(·,·,x) feeding your act and those processes. Include the nodes for other observations, since they govern worlds where you would see something else. (Paper, with my emphasis.)
4. For each a, set do(fdt=a), propagate, and compute E[V]. (Paper.)
5. Pick the maximum. (Paper.)

The unresolved parts are step 2 and the graph's reliability. Wrong edges give wrong answers, just as a wrong causal graph does for CDT. The paper also leaves open how an agent should set credences about fdt nodes for cases such as "what would I do on observation y" (its examples use arbitrary q and show the answer is insensitive to it).

## 7. Conclusion

A-FDT is Pearl-style expected-utility maximization with the cut moved one level up, to the output of the decision function. Observation no longer conditions the model; it selects which function-node is intervened on. On the paper's evidence this one rule one-boxes in Newcomb, smokes in the lesion problem, pays in Parfit's hitchhiker, refuses blackmail and stays in Damascus. Its main limitation is that its input, the graph of subjunctive dependencies, has no accepted method of construction.