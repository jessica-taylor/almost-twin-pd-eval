# A-FDT: Choosing as the Output of a Function

## 1. What A-FDT is

Most of decision theory agrees on one recipe: weigh outcomes by probability and utility, then pick the act with the highest expected value. The disagreement is about which probabilities to use, and in particular about what the agent should imagine when she asks "what if I did $a$?"

Yudkowsky and Soares's *functional decision theory* (FDT) answers that a rational agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" In this essay I discuss the specific formalization the paper gives as its Equation (4) in Section 5. I call it **A-FDT (action functional decision theory)** because it maximizes over **actions**, one input at a time. The paper's own footnote says this is not the authors' favoured version: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." Everything below concerns the action version. Where I discuss the policy version, I call it policy-FDT.

I will mark which claims come from the source and which are my own operational proposals.

## 2. The common frame

The source starts from a generic expected-utility schema (its Equation 1):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j).
$$

Here $x$ is the observation history, $o_j$ ranges over outcomes, and $\hookrightarrow$ is a "decision hypothetical" connective whose meaning is left open. Following Joyce's representation theorem, the authors treat rival theories as rival interpretations of $\hookrightarrow$. On this view the theories share an account of value and differ only in "the epistemic perspective from which actions are to be evaluated."

Operationally, the agent has a world-model $M$. For each candidate act she builds a *hypothetical* $M^{a\hookrightarrow}$, which the authors describe as "transient, useful, and possibly quite representationally thin," like notes on scratch paper. She then scores each hypothetical. Two familiar theories fill in the blank as follows, writing $V=\mathcal U(\textsc{Outcome})$:

- **EDT** (Eq. 2) conditions: $\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a)$.
- **CDT** (Eq. 3) intervenes on the physical act in a causal graph $G$: $\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x)$.

## 3. The A-FDT equation

The paper's Equation (4), which it writes with the label $\mathrm{FDT}$, is

$$
\boxed{\;\mathrm{A\text{-}FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\; \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).\;}
$$

The ingredients are these:

- $P$ is a probability distribution over variables. Unlike in CDT, these include variables for the *outputs of mathematical functions*. The source's example is a variable for the value of $6288+1048$, "one that (hopefully) has most of its probability on $7336$."
- $G$ is a graph saying how changing such logical variables propagates to other variables. It encodes **subjunctive dependence** and not merely causal dependence.
- $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable in the model that stands for *what this very algorithm outputs on this very input*. The underlines mark dequoting: the variable's name is built from the agent's own model and observation. The authors call the self-reference harmless. One can *represent* the output without knowing it, and Kleene's recursion theorem ("quining") shows that such self-representing data structures exist.
- $\mathtt{do}$ is Pearl's operator. It sets a node, recomputes its descendants in $G$, and leaves everything else at its prior distribution.

The source names two differences from CDT.

1. **Point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical *type*, the function's output. Everything that subjunctively depends on that output then moves together: the agent's own body, a twin's body, a predictor's forecast.
2. **Treatment of observations.** In Equation (4), $\textsc{Obs}=x$ does **not** appear to the right of the conditioning bar. Instead, the observation selects *which node* is intervened on. When the history changes from $x$ to $y$, A-FDT switches from $\textsc{fdt}(\ldots,\underline x)$ to $\textsc{fdt}(\ldots,\underline y)$.

The second point is easy to miss, and it decides several cases. An A-FDT agent who has seen $x$ may consider hypotheticals in which she would never have seen $x$. One more detail: the paper's displayed formula in its transparent Newcomb section seems to put $\textsc{Obs}=\textit{full}$ inside the expectation, but the calculation it then carries out does not condition on it. I follow Equation (4) and the calculation. A footnote on Timeless Decision Theory (an earlier variant) explains why this matters. That theory both conditions on evidence *and* moves the intervention point, which creates "a kind of 'double update' which proves harmful in practice."

The source also states a coincidence result. Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node. Then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$

and EDT, CDT and A-FDT agree. They come apart only when something other than the act itself tracks the act, as predictors and copies do.

## 4. Subjunctive dependence, and what $G$ must encode

The core claim is that "predictor-like things depend upon an agent's future action, and lesion-like things do not." The source uses calculators to illustrate. Two working calculators computing $6288+1048$ on opposite sides of the globe will agree. They agree not because one causes the other, but because both compute the same function. A scribe copying one calculator's output depends on it both causally and subjunctively, so causal dependence is a special case. Two calculators that happen to be pink are merely correlated. The slogan is:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Strictly, A-FDT needs *counterpossible* reasoning. If the function in fact outputs *cooperate*, there is no possible world where it outputs *defect*. The ideal would be a $\mathtt{true}(\varphi)$ operator that updates a distribution on a possibly false logical sentence, giving

$$
\mathrm{FDT}^*(P,x)=\arg\max_a \mathbb E\big(V\mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a)\big).
$$

The authors admit that "it's not clear how to define a $\mathtt{true}$ operator." Their workaround is that the logical dependency structure is *supplied as input* in $G$, in the same way CDT takes causal structure as given. Equation (4) then reuses $\mathtt{do}$. This is honest, but it moves the hard problem rather than solving it. In the source's words: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

Two questions about "control" come up. First, does A-FDT believe in retrocausation? No. Fiona, the paper's A-FDT agent, "does not think that a physical signal passes between her action and the predictor's prediction." Second, is intervening on a logical fact incoherent? The authors answer by symmetry. A deterministic CDT agent also evaluates acts it could not "really" have performed, so "any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

## 5. Worked cases

Utilities are in dollars throughout, and the predictor is 99% accurate unless stated otherwise.

**Newcomb's problem.** Fiona's graph has $\textsc{fdt}(\underline P,\underline G)$ as a parent of both $\textsc{Act}$ and $\textsc{Prediction}$, and an $\textsc{Accurate}$ noise node also feeds $\textsc{Prediction}$.

- Setting the output to *onebox*: box B is full with probability 0.99, so $\mathbb E V = 990{,}000$.
- Setting it to *twobox*: $\mathbb E V = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000$.

A-FDT one-boxes. CDT, intervening on $\textsc{Act}$, leaves $P(\textit{full})=p$ fixed, finds two-boxing better by $1{,}000$ whatever $p$ is, and two-boxes. The paper notes a standard objection. If Fiona is nearly sure she one-boxes and therefore that the box is full, why not take both? The answer is that her hypothetical for two-boxing is one where the function outputs *twobox*, and in that hypothetical the box is probably empty. Her beliefs about the actual world and her decision hypotheticals are different objects.

**Twin prisoner's dilemma.** Both twins implement the same function, so one intervention sets both actions. Mutual cooperation yields $1{,}000{,}000$ and mutual defection $1{,}000$. A-FDT cooperates.

**Smoking lesion.** Here the graph differs from Newcomb's, and that is the whole point. The lesion is not computing anything about the agent's decision procedure. The source formalizes the case unusually. The lesion fixes which utility function the agent has, $\mathcal U_S$ (likes smoking) or $\mathcal U_R$, and so which of two decision computations, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls $\textsc{Act}$:

$$\textsc{Act}(\textit{lesion},s,r)=s,\qquad \textsc{Act}(\textit{nolesion},s,r)=r.$$

Intervening on the $S$-node leaves $P(\textit{lesion})=p$ unchanged. Smoking then beats refraining by exactly $p\cdot 1{,}000$, so A-FDT smokes. The authors themselves call the problem "badly confused" and recommend that philosophers abandon it.

**Transparent Newcomb and Parfit's hitchhiker.** Both boxes are visible, and box B is filled iff the agent is predicted to one-box *upon seeing it full*. Fiona sees it full and intervenes on $\textsc{fdt}(\ldots,\textit{full})$. She does not condition on seeing a full box. Let $q$ be her prior probability that she two-boxes on seeing an empty box.

- *onebox*: $0.99(1{,}000{,}000)+0.01\,q(1{,}000) = 990{,}000+10q$.
- *twobox*: $0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q$.

The paper prints the second figure as "\$110,00 + q·\$990", which looks like a typo for $10{,}010+990q$. The ranking is the same either way: A-FDT one-boxes even while looking at a full box. The source argues that this case is "precisely equivalent to paying the driver in Parfit's hitchhiker problem." A-FDT therefore pays the driver, while CDT and EDT do not and so are left in the desert.

**XOR blackmail.** A perfect predictor sends a letter iff exactly one of these holds: (i) no termites and the agent pays on receiving the letter; (ii) termites and the agent does not pay. Let $p=P(\textit{termites})$. Intervening on $\textsc{fdt}(\ldots,\textit{letter})$ gives:

- *pay*: the letter arrives iff there are no termites, so $\mathbb E V = -p(10^6)-(1-p)(10^3)$.
- *refuse*: the letter arrives iff there are termites, so $\mathbb E V = -p(10^6)$.

A-FDT refuses, by a margin of $(1-p)\cdot 1{,}000$. The calculation shows that paying changes whether the letter comes, not whether there are termites. EDT pays here. CDT refuses, but for a different reason: its hypothetical in which it pays still has the letter arriving, which amounts to imagining that an inerrant predictor erred.

**Mechanical blackmail.** The blackmailer runs a damaging program, costing $10^6$, iff she predicts the agent would pay $1{,}000$ to stop it. Let $\varepsilon$ be the probability that she wrongly predicts payment. Intervening on $\textsc{fdt}(\ldots,\textit{blackmail})$:

- *pay*: always blackmailed and always pays, so $\mathbb E V = -1{,}000$.
- *refuse*: blackmailed only by error, so $\mathbb E V = -\varepsilon\cdot 10^6$.

A-FDT refuses iff $\varepsilon<0.001$. The source gives $\varepsilon=0.0009$ as a refusing case, with an expected loss of 900, and "0.011%" as a paying case. Under this model a paying case needs $\varepsilon>0.1\%$, so 0.11% seems to be intended. The important qualitative point is that A-FDT refuses *while holding the letter*, knowing that the prediction was wrong, "because it's advantageous to be *the kind of agent* that makes such decisions."

**Death in Damascus.** Death perfectly predicts the agent and goes wherever the agent will be. In both A-FDT hypotheticals Death is at the agent's location, so the agent dies either way. Fleeing costs an extra $1{,}000$, so A-FDT stays in Damascus. CDT, by contrast, oscillates, because each tentative plan makes the other option look better. With ratification it ends up mixing, and it may even refuse to pay \$1 for a truly random coin that offers a 50% chance of survival.

The pattern across these cases is the source's diagnosis: "EDT respects too many action-environment correlations, while CDT respects too few."

## 6. Applying A-FDT to unfamiliar cases

The source deliberately brackets *how* one finds subjunctive dependencies. To decide new cases one needs some procedure. What follows is **my proposal** for one. It reproduces every analysis in the paper, but it is not stated there.

1. **Index your decision nodes by input.** For each observation history $y$ you might face, create a variable $D_y=\textsc{fdt}(\underline P,\underline G,\underline y)$. Your actual input $x$ marks the node you will intervene on.
2. **Find the systems that compute or model $D_y$.** These include your body, copies of you, predictors and simulators. For each one, draw an edge from the relevant $D_y$ to that system's output. Add a noise node for its error rate, as the source does with $\textsc{Accurate}$.
3. **Leave mere correlates alone.** Lesions, shared genes, background causes and other things that do not evaluate your function get no edge from any $D_y$. Their correlation with your act runs only through ordinary common causes.
4. **Make the routing explicit.** Write $\textsc{Act}$ as a function of upstream variables that decides *which* $D_y$ controls the body, as the paper does when the prediction determines what the agent sees.
5. **Do not condition on $x$.** Compute $\mathbb E(V\mid \mathtt{do}(D_x=a))$, letting the model assign probability to other observations. Leave the non-intervened $D_y$ at prior credences, which the paper writes as $q$.
6. **Take the argmax.**

**An example of my own: the imperfect twin.** Real "twins" are only partly similar. One simple model of partial similarity is this. With probability $s$ the other player's choice is computed by your function, so it equals $D_x$. With probability $1-s$ it is generated independently and cooperates with probability $r$. Using the twin-PD payoffs:

$$
\mathbb E V(C)-\mathbb E V(D)= s(1{,}000{,}000-1{,}000) + (1-s)(-1{,}000) = 1{,}000{,}000\,s - 1{,}000.
$$

So A-FDT cooperates iff $s>0.001$, and the threshold does not depend on $r$. The mixture model is my assumption. The source offers only the noisy-calculator intuition, that dependence is "weakened, but not eliminated" by imperfection. Other ways of modelling partial similarity could give different thresholds, which is exactly the gap the open problem names.

The same template handles the source's two closing examples:

- **Voting.** Ten like-minded A-FDT voters each pay \$1,000 and win \$1,000,000 iff all ten vote. One intervention moves all ten votes, so voting yields $999{,}000$ against $0$.
- **The gym.** If this week's choice and next week's are the same computation, "go" moves all of them together.

## 7. Open questions, and where A-FDT specifically is underdetermined

**(a) Constructing $G$.** The source states plainly that no method yet exists to infer subjunctive-dependence structure from observation, or even to know whether Pearl's framework can represent it satisfactorily. In practice the verdict of A-FDT is only as good as the modeller's judgement about which systems "compute your function." Borderline cases, such as crude predictors, base-rate statisticians and agents running similar but non-identical algorithms, are not settled by the theory.

**(b) Action versus policy.** This question is specific to A-FDT. Equation (4) chooses the output on the *current* input and holds the outputs $D_y$ for other inputs $y\neq x$ at prior credences. In the paper's examples those credences do not affect the ranking. The authors note in passing that the correct values are $q=1$ for transparent Newcomb and $q=0$ in the lesion case. In general, though, they can matter. Suppose a predictor rewards you only if you do $a$ on input $x_1$ *and* $b$ on input $x_2$, and doing $a$ costs something. At $x_1$, A-FDT weighs $a$ using its current credence that it will do $b$ at $x_2$. If that credence is low, $a$ may not seem worth its cost, and the coordinated policy may never be found. Policy-FDT avoids this by choosing the whole mapping $\pi:\mathcal X\to\mathcal A$ at once, roughly $\arg\max_\pi \mathbb E(V\mid \mathtt{do}(\textsc{fdt}=\pi))$, and then applying $\pi(x)$. The source says the difference matters "in certain multi-agent dilemmas" and does not develop it. My suggestion is that where the two versions might diverge, a careful user of A-FDT should check whether the credences on the other nodes are reflectively consistent with what A-FDT itself would output on those inputs. That is an equilibrium requirement which Equation (4) does not impose.

**(c) Self-knowledge and priors.** EDT's verdicts can depend on its prior over its own action, and the paper illustrates this with the cosmic ray problem. Because A-FDT uses $\mathtt{do}$, it never conditions on a probability-zero action, and the prior on the intervened node is "inconsequential." The prior on the *other* nodes remains, as in (b).

**(d) Fairness.** The authors claim superiority only on "fair" problems, meaning problems where the agent's beliefs are accurate and payoffs depend only on the agent's behaviour in the dilemma at hand. Someone who punishes anyone acting like Fiona's copy defeats A-FDT trivially. They grant that no formal criterion of fairness yet exists.

**(e) Dominance.** The source argues that "every expected utility theory comes with its own notion of dominance." CDT's dominance argument for two-boxing presupposes CDT's hypotheticals. A-FDT never takes an action that is dominated in its own sense: holding the subjunctive dependencies fixed, switching the function's output never helps.

## 8. Conclusion

A-FDT keeps the machinery of expected utility and changes one thing: the object of choice. Instead of intervening on a physical act, the agent intervenes on the output, *on her current input*, of the function she implements. She lets every system that computes or accurately models that function move with it, and she does not condition on her observations. This single change explains why A-FDT one-boxes yet smokes, cooperates with twins, pays in Parfit's desert, and refuses both kinds of blackmail. The source is candid about where the account is incomplete. The subjunctive-dependence graph $G$ is given as an input, not derived, and the action-indexed form of Equation (4) leaves the agent's behaviour on other inputs to prior credences, a gap that policy-FDT is meant to close. With those caveats, A-FDT already gives a usable and precise procedure: draw the dependence graph honestly, intervene on the function's output, and choose the hypothetical world you most prefer.

## References

- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060.