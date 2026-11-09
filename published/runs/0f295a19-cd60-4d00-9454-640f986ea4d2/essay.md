# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The core idea

Take a decision problem in which some part of the world is correlated with your action. The question is which of those correlations a hypothetical "what if I did *a*?" should preserve. Evidential decision theory (EDT) preserves all of them. Causal decision theory (CDT) preserves only those running causally downstream of the act. A-FDT, the theory I explain here and which the source paper (Yudkowsky and Soares, "Functional Decision Theory") presents as Equation (4) of Section 5, preserves every decision-relevant *subjunctive dependence*. These are the dependencies of things on the output of the agent's decision function. Causal dependence is a special case of them.

The source's slogan is that the agent asks "Which output of this very function would yield the best outcome?" rather than "Which physical act of mine causes the best outcome?" The paper's own name for the theory is FDT. I use A-FDT throughout, meaning the version defined by Equation (4), and I call the other theories EDT and CDT.

## 2. The formal definition

All three theories maximize expected utility,
$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$
and differ only in how they read the hypothetical connective $\hookrightarrow$. The source follows Joyce in treating this as the free parameter of expected-utility theory, the "epistemic perspective."

The inputs are a probability distribution $P$ over the variables of a world-model, a graph $G$ encoding dependence structure, and an observation history $x$. With $V=\mathcal U(\text{Outcome})$, the three rules are:

- EDT: $\arg\max_a \mathbb E(V\mid \text{Obs}=x,\text{Act}=a)$
- CDT: $\arg\max_a \mathbb E(V\mid do(\text{Act}=a),\text{Obs}=x)$
- **A-FDT (Equation 4):**
$$\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\ \Big|\ do\big(\text{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The underlines denote dequoting. The variable $\text{fdt}(\underline P,\underline G,\underline x)$ stands for the output of the A-FDT procedure itself on those inputs. Three features of this definition matter.

**Self-reference is harmless.** The model contains a variable naming the very computation that uses it. The agent need not know the *value* of that computation to have a variable *representing* it. The source invokes Kleene's recursion theorem ("quining") to show such self-representing structures can be built.

**Observation changes where one intervenes.** CDT handles observations by conditioning. A-FDT instead moves the intervention point from $\text{fdt}(P,G,x)$ to $\text{fdt}(P,G,y)$ when the observation changes. Different observations correspond to different nodes, namely the procedure's output on different inputs. This is why A-FDT can imagine that, had its output differed, it would have seen something else. The source's footnote 7 adds that the authors' *preferred* formalization intervenes on policies (maps from observations to actions). It says this difference matters only in some multi-agent problems and is not used in the paper. Equation (4) as written is action-valued, and I follow it.

**The graph $G$ is an input.** The source is explicit that no theory yet exists for deducing subjunctive-dependence structure from observation, comparable to Pearl's account of causal structure. It calls this "perhaps the largest open problem." It also says it is unclear whether such a theory can be built within Pearl's framework. It further admits that a $\mathtt{true}$ operator conditioning on false logical sentences ("counterpossibles") is undefined. Equation (4) sidesteps this by requiring the dependency graph to be supplied, just as CDT requires a causal graph.

## 3. Subjunctive dependence

Two physical systems computing the same function (two calculators on $6288+1048$) subjunctively depend on that function. If it output something else, both would. A predictor containing an accurate model of an agent has, in effect, a "twin" of the agent inside its mind. The source's distinctions are:

- Causal dependence is a special case: a scribe copying a calculator's output depends both causally and subjunctively on it.
- Mere statistical correlation is not subjunctive dependence. Two pink calculators on opposite sides of the world are correlated, but if one were green the other would stay pink.
- Imperfect predictors give weakened dependence, not none.

The rule of imagination is: when the agent pictures taking a different action, she changes the output of her decision function and everything that subjunctively depends on it, and holds the rest fixed. She does this without believing in retrocausation. No signal passes backward in time. It is simply incoherent to picture her action changing while a good predictor of that very function stays unchanged. The source also stresses that A-FDT is no more "deluded" than CDT. A deterministic CDT agent likewise imagines worlds in which its act differs.

## 4. The procedure, step by step

1. Build the world-model: variables for the agent's decision-function outputs on each possible input, for predictors and copies, and for the rest of the environment, together with a graph saying how changing a decision-function node propagates.
2. Identify the node $\text{fdt}(P,G,x)$ corresponding to the observation actually received.
3. For each action $a$, perform $do(\text{fdt}(P,G,x)=a)$. Propagate the change along the graph to every variable depending on that node: the agent's act, predictions of it, and even whether she gets to see the observation. Hold the others fixed.
4. Compute $\mathbb E[V]$ in each resulting hypothetical and output the maximizer.

## 5. Worked examples

**Newcomb (99% predictor).** The node $\text{fdt}(P,G)$ feeds both Act and Prediction. With $do(\text{fdt}=\text{onebox})$, Act is one-box and Box B is full with probability 0.99, so $\mathbb E[V]\approx\$990{,}000$. With twobox, Box B is full with probability 0.01 and $\mathbb E[V]=\$11{,}000$. A-FDT one-boxes. CDT's graph has Prediction independent of Act, so it two-boxes. Note the grid of payoffs here (full box $\$1{,}000{,}000$, plus $\$1{,}000$ for two-boxing) is the source's.

**Smoking lesion.** The lesion causes both the desire to smoke and the cancer. Cancer does not depend on the agent's decision function (the cancer does not simulate her). So the intervention leaves $P(\text{lesion})=p$ unchanged, and smoking gains $p\cdot\$1{,}000$. A-FDT smokes. The same rule one-boxes in Newcomb and smokes here, and only the graphs differ. (The source notes the formalization is contrived, since the agent is uncertain about her own preferences, and it recommends abandoning the problem.)

**Transparent Newcomb and Parfit's hitchhiker.** Suppose the agent sees a full box. She intervenes on $\text{fdt}(P,G,\text{full})$. In the twobox hypothetical, the predictor, who modelled that very procedure, would with probability 0.99 have left the box empty, so she would have been running the *other* node, $\text{fdt}(\ldots,\text{empty})$. Letting $q$ be her credence that she two-boxes on seeing empty, the source computes onebox $=\$990{,}000+0.01q\cdot\$1{,}000$ against twobox $=0.01\cdot\$1{,}001{,}000+0.99q\cdot\$1{,}000$. A-FDT one-boxes even while looking at the full box. The structure is identical to paying the driver in Parfit's hitchhiker, where refusing corresponds to a world in which she was never rescued.

**XOR blackmail.** The infestation is not downstream of the decision function, so A-FDT leaves its probability unchanged. The only things that vary are the letter's arrival and her response. Paying merely makes the letter more likely to be sent. A-FDT refuses, and EDT pays because it treats the letter as news about termites.

**Mechanical blackmail with a fallible predictor.** The source gives error rate 0.0009 for the blackmailer's wrongly predicting payment. Paying means always blackmailed, losing \$1,000. Refusing means blackmailed 0.09% of the time, losing \$900 in expectation. So A-FDT refuses, even holding a letter it knows came from a prediction error. With error 0.011% the comparison reverses and it pays. This gives a threshold rule that a reader can apply to unfamiliar cases: compare $\Pr(\text{targeted}\mid\text{policy})\times\text{loss}$ across the two policy-hypotheticals.

**Death in Damascus.** Death's book entry depends on the agent's decision function. Fleeing means Death is in Aleppo, so A-FDT stays and saves the \$1,000. CDT oscillates, because it holds Death's location fixed.

## 6. Claims versus my own proposals

**Source's claims.** The definition in Equation (4). That A-FDT agrees with CDT and EDT when all action–world correlations are causal. That it outperforms them on Newcomb-like problems, with the performance measured as expected utility achieved. That it needs no precommitment or ratification. That it is reflectively stable on "fair" problems. That it never assigns negative value to information. And that its dominance principle is analogous to CDT's but built on A-FDT counterfactuals.

**Open in the source.** There is no algorithm for deriving $G$. There is no formal fairness criterion (footnote 15 gives a counterexample: a problem that punishes copies of the agent). Counterpossible reasoning is unspecified.

**My own operational suggestions** (not the source's):

1. *Graph-building heuristic.* Ask of each variable: does it contain a model of, or computation of, my decision procedure (a predictor, a copy, an opponent who reasons about me)? If so, link it to the decision-function node. If it merely correlates statistically with my act (a common cause such as a lesion), do not link it. This is a rule of thumb that reproduces the source's verdicts, not a theory.
2. *Sensitivity check.* Since $G$ is an input, for any prescribed action compute how robust the verdict is to the dependence strength $\rho$ (e.g. predictor accuracy). The blackmail example shows a sharp threshold, so reporting that threshold is more informative than a bare verdict.
3. *Policy view.* For multi-observation problems, evaluate whole policies by intervening on all of the decision-function nodes jointly. This matches the source's remark about its preferred formulation, and it keeps the calculation consistent with the transparent-Newcomb computation above.

## 7. Why this is philosophically defensible

The source argues from three directions. First, utility: any predictor can see which theory an agent follows, and A-FDT agents end up richer. Second, the global perspective: the agent asks what the whole universe would look like if her procedure behaved differently, and picks the best such universe. Third, a diagnosis of the rivals. EDT respects too many correlations and so manages the news. CDT respects too few and so imagines predictors erring exactly when she acts.

I would add a caveat of my own. All the persuasive force depends on $G$ being right. If someone supplies a graph that wrongly links a lesion-like variable to the decision node, A-FDT will behave like EDT. If someone omits a real link, it will behave like CDT. So the theory is as reliable as its dependence model, and the unsolved problem of discovering dependence is the real boundary of its practical use.

## 8. Conclusion

A-FDT is CDT's surgical structure applied to a different node. Instead of intervening on the physical act, it intervenes on the logical output of its own decision procedure, and it lets that intervention propagate to everything that subjunctively depends on it, including predictions, copies, and even what is observed. Equation (4) is a precise, computable rule given $(P,G,x)$. What remains unsettled, as the source admits, is how to obtain $G$ and how to reason about counterpossibles. Within those limits, it gives a single criterion that one-boxes, smokes, pays the hitchhiker, refuses blackmail, and stays in Damascus.