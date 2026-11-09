# Policy Functional Decision Theory: Choosing the Whole Function

*A mathematical essay based on Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," with emphasis on the policy-selection formulation of footnote 16.*

## 1. Introduction

Suppose you are deciding whether to keep a promise. Standard decision theories tell you to evaluate your *physical act*: causal decision theory (CDT) asks what the act will cause; evidential decision theory (EDT) asks what the act would be evidence for. Yudkowsky and Soares (2017) argue that both are asking the wrong question. The right question, they claim, is:

> "Which output of this very decision procedure would yield the best outcome?"

Their answer is **functional decision theory** (FDT). FDT treats your decision not as a bodily motion but as the output of a fixed mathematical function, and evaluates counterfactuals in which that function's *output* differs — with all subjunctively dependent consequences varying along with it, and everything else held fixed.

Buried in a footnote of their paper is an important refinement. Footnote 16 tells us:

> "the author's preferred formulation of FDT actually intervenes on the node FDT(−) to choose not an action but a **policy** which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell."

I will call this preferred formulation **policy functional decision theory (P-FDT)**. This essay develops P-FDT as the central formalism: the agent intervenes on an entire function from observation histories to actions, rather than on the single action given the observations actually received. Section 2 sets up the framework of hypotheticals. Section 3 defines P-FDT formally. Section 4 works through examples. Section 5 explains why the policy formulation matters and where it leaves open questions.

## 2. The Common Framework: Expected Utility over Hypotheticals

All three theories — EDT, CDT, and P-FDT — are expected utility theories sharing a common skeleton (Yudkowsky & Soares, drawing on Joyce 1999). An agent maintains a world-model, a probability distribution $P$ over variables including an action variable $\Act$, an observation variable $\Obs$, an outcome variable $\Outcome$, and a utility variable $V = \Util(\Outcome)$. Each theory prescribes maximizing

$$\mathcal{EU} = \sum_j P(a \hookrightarrow o_j)\,\Util(o_j),$$

where $a \hookrightarrow o_j$ is a *decision hypothetical*: the theory's answer to "what would happen if I took $a$?" The theories differ only in the epistemic perspective encoded in $\hookrightarrow$ — in how the hypothetical is constructed from the model. As Joyce puts it, quoted by the authors: decision theories "should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

The authors formalize this with the "hypothetical" construction: given a model $M$, the agent builds a hypothetical $M^{a\hookrightarrow}$ for each candidate action, then picks the action whose hypothetical has the highest expected $V$.

- **EDT** builds $M^{a\hookrightarrow}$ by *Bayesian conditionalization*: $P(\cdot \mid \Obs = x, \Act = a)$. EDT preserves *all* correlations between the action and the world.
- **CDT** builds it by a *causal intervention* à la Pearl: $P(\cdot \mid \Do(\Act = a))$. CDT preserves only causal structure downstream of $\Act$ — it severs every correlation not causally produced by the act.
- **P-FDT** builds it by intervening on a *logical* variable: the output of the agent's decision function. This preserves causal structure *and* subjunctive (logical) dependence, while severing mere statistical correlation.

## 3. Subjunctive Dependence

The philosophical core of P-FDT is **subjunctive dependence**. The authors write:

> "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."

Two well-functioning calculators computing $6288 + 1048$ will both output $7336$; if one *were* to output something else, the other would too — because both outputs are determined by the same mathematical fact. This dependence is neither purely causal (the calculators need not share a causal history) nor merely statistical (independent coincidences, like two calculators both being pink, exhibit no subjunctive dependence). Causal dependence is a special case: a scribe recording the Parisian calculator's output depends on it both causally and subjunctively.

The slogan is: **FDT is to subjunctive dependence as CDT is to causal dependence.** A Newcomb predictor contains an accurate model of the agent's decision function — a "twin inside the predictor's mind" — so the prediction subjunctively depends on the function's output. A carcinogenic lesion computes nothing about your decision; the smoking–cancer correlation is merely statistical.

A further point of definition, from the authors' account of dependence: "FDT agents do not need to evaluate counterpossibilities in full generality; they only need to reason about questions like 'How would this predictor's prediction of my action change if the FDT algorithm had a different output?'" This is a technical, not philosophical, difficulty — human reasoners manage such reasoning heuristically, and logical-uncertainty machinery (Garber, Demski, Hutter et al.) offers a research direction.

## 4. The Formal Definition of P-FDT

Here is the graphical formalization, adapted to the policy formulation. The agent's model is a pair $(P, G)$, where $P$ is a probability distribution and $G$ is a graph describing *subjunctive dependence structure* — how changing the value of a logical variable (including the output of the decision procedure) affects other variables. The distribution $P$ contains a variable for each node.

The key object is the **decision-function variable**. For each possible input (observation history) $x$, the model contains a variable

$$\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$$

representing *what the decision procedure would output given input $x$*. The underlines indicate dequoting: these variables are *about* the very procedure computing them. The self-reference is harmless — Kleene's second recursion theorem ("quining") shows how an algorithm can contain an accurate representation of itself without needing to know its own output in advance.

In the action-selection version of FDT given as equation (4) of the source, the agent intervenes on $\mathrm{fdt}(\underline{P}, \underline{G}, \underline{x})$ for the *actually observed* $x$:

$$\mathrm{FDT}(P, G, x) = \arg\max_{a \in \mathcal{A}} \mathbb{E}\Big(V \,\Big|\, \Do\big(\mathrm{fdt}(\underline{P},\underline{G},\underline{x}) = a\big)\Big).$$

P-FDT differs in one structural respect: the intervention targets a single variable representing a **policy**

$$\pi : \mathcal{X} \to \mathcal{A},$$

a function from observation histories to actions. That is:

$$\textbf{(P-FDT)}\qquad \mathrm{PFDT}(P, G) = \pi^*,\ \text{where } \pi^* = \arg\max_{\pi \in \Pi}\, \mathbb{E}\Big(V \,\Big|\, \Do\big(\mathrm{fdt}(\underline{P},\underline{G}) = \pi\big)\Big),$$

and the agent, having selected $\pi^*$, *then* applies it to her actual observations: she takes the action $\pi^*(x)$. Two differences from CDT, in the source's own words: first, where CDT intervenes on the physical act, P-FDT intervenes on the logical output of its decision procedure; second, where CDT responds to observation by conditioning, P-FDT responds to observation by choosing *which intervention to make* — and, in the policy version, by evaluating interventions on the whole input–output map rather than the slice of it at the observed input.

The $\Do$ operator here is Pearl's, repurposed: setting $\mathrm{fdt}(\underline{P},\underline{G}) = \pi$ propagates downstream through $G$, updating everything that subjunctively depends on the decision function's behavior — the agent's own action at *every* observation point, any twin's identical computation, any predictor's model-based prediction — while leaving everything else (lesions, statistical coincidences, states causally upstream and independent) fixed.

**Two caveats I should flag as interpretation rather than source text.** First, the source gives the policy formulation only informally (footnote 16 plus footnote 7, which says agents "actually iterate over *policies*... rather than actions. This makes a difference in certain multi-agent dilemmas"). The argmax-over-$\Pi$ equation above is my formalization of that remark. Second, the source leaves open what counts as the domain $\mathcal{X}$ of the policy — the set of "inputs" or observation histories the policy maps from. The natural reading, given the paper's examples (Fiona intervenes on $\mathrm{fdt}(\underline{P}, \underline{G}, \mathrm{full})$ versus $\mathrm{fdt}(\underline{P}, \underline{G}, \emptyset)$ in the transparent Newcomb problem and on $\mathrm{fdt}(\underline{P}, \underline{G}, \mathrm{blackmail})$ versus $\mathrm{fdt}(\underline{P}, \underline{G}, \emptyset)$ in the mechanical blackmail problem), is: the possible observation histories *within the decision problem at hand*, together with the null history. Policies are problem-relative objects. I adopt this reading below; it makes P-FDT a theory of "what rule should this procedure output for this game?", not "what rule should I run for life?"

A practical remark: computing $\arg\max_\pi$ over policies is generally harder than over actions, since $\Pi$ is exponentially large. In the fair single-agent problems of the source this doesn't matter, because the optimal policy is *generated* by the optimal action at each input — the policy $\pi^*$ is just "do the P-FDT-optimal thing everywhere." The difference only bites, as the authors say, in multi-agent dilemmas where other agents' behavior depends on what you *would have done* at observations you didn't receive.

## 5. How P-FDT Reasons: Three canonical problems

**Newcomb's problem.** A 99%-accurate predictor has filled box B iff she predicted one-boxing. Fiona's graph $G^F$ has $\mathrm{fdt}(\underline{P^F}, \underline{G^F})$ pointing to both $\Act$ and $\Var{Prediction}$: both her bodily action and the predictor's prediction depend on what her decision procedure outputs. Intervening $\Do(\mathrm{fdt} = \text{onebox})$ sets $\Act = \text{onebox}$ and makes Box B full with probability 0.99; expected utility \$990,000. Intervening $\Do(\mathrm{fdt} = \text{twobox})$ yields \$11,000. So P-FDT one-boxes. No retrocausality is invoked: Fiona simply refuses to imagine her action changing while the thing computing it stays fixed — "much like we should expect elliptic curves to have different properties if (counterpossibly) Fermat's last theorem were false."

**The smoking lesion.** Cancer is caused by a lesion that also causes a taste for smoking; the correlation is merely statistical. Here Fiona's graph differs: $\mathrm{fdt}(\underline{P},\underline{G})$ points to $\Act$ but *not* to $\Var{Cancer}$. Intervening on the decision function does not change the probability of the lesion, so the smoking hypothetical is strictly better by $p \cdot \$1{,}000$. P-FDT smokes. One rule, one-boxing and smoking — contra the Gibbard–Harper claim that no theory can consistently do both.

**Transparent Newcomb and the key move.** Both boxes are transparent; the predictor filled box B iff she predicted one-boxing *upon seeing two full boxes*. Fiona sees the box is full — and one-boxes anyway. Why? Because in P-FDT, "agents should entertain the hypothesis that, if their action were different, they might have *made different observations*." Upon seeing a full box, she intervenes on $\mathrm{fdt}(\underline{P}, \underline{G}, \mathrm{full})$; but the graph tells her that *which* observation she receives depends on the predictor's prediction, which subjunctively depends on her decision function's behavior at that observation. In the hypothetical where $\mathrm{fdt}(\underline{P},\underline{G},\mathrm{full}) = \text{twobox}$, the predictor predicted defection, the box is empty, and (crucially) she is running the policy for the *empty*-box branch instead. Expected utilities: \$990,000 for the onebox output versus roughly \$110,000 for twobox. She one-boxes, and so gets full boxes.

This is exactly where the action-version and policy-version of FDT coincide in effect: the action-version's intervention on $\mathrm{fdt}(\underline{P},\underline{G},\mathrm{full})$ already implicitly varies what happens at the other observation, because the graph connects $\Var{Prediction}$ to $\Act$. The policy version makes this explicit and total: the intervention sets the *whole* function, so behavior at the empty-box branch is chosen *jointly* with behavior at the full-box branch, rather than treated as a separate, fixed fact.

**Mechanical blackmail.** A perfect predictor runs a damaging program iff she predicts the agent will pay upon receiving the blackmail letter. The P-FDT agent, holding the letter, evaluates the policy intervention: the policy that pays gets blackmailed (probability ≈ 1) and loses \$1,000; the policy that refuses is almost never blackmailed (probability ≈ 0 of paying, with a small chance of \$1,000,000 damages under predictor error). She refuses; the predictor, foreseeing this, never sends the letter. Here the policy formulation is *visibly* doing work: the agent refuses even *while holding the letter*, because her hypothetical — "if my policy were the refusing one, I would not be holding this letter" — is generated by intervening on the whole function. The authors note she happily "imagines worlds in which her observations were different, and even... achieving low utility in the world corresponding to her actual observations." The result is immunity to extortion: predictors leave P-FDT agents alone. The same structure resolves Parfit's hitchhiker (pay the rescuer: the refusing-policy world is the desert world) and yields self-coordination over time (go to the gym: today's decision and next week's decision subjunctively depend on the same policy).

## 6. Why Policies Rather Than Actions?

The source says only that the difference "matters in certain multi-agent dilemmas." Let me spell out the mechanism as I understand it, flagging this section as my development of the footnote.

Consider an agent who will face a sequence of observations, only one of which will actually occur — say, an agent who may receive a blackmail letter or not. If she evaluates *actions*, her evaluation of "pay, given letter" treats her behavior in the no-letter branch as a fixed background fact. But other agents (the blackmailer) may condition *their* behavior on her behavior in the branch she won't reach: the blackmailer runs the program iff she predicts *payment upon receiving the letter* — but a bargaining blackmailer might condition on her whole policy, e.g. pay in some states and not others, or pay conditional on some signal. In dilemmas with such *policy-contingent* outsiders — or with logical correlates of the agent across multiple input branches (a twin facing a different dilemma instance, a successor process, another branch of a scattered decision) — evaluating slice-by-slice can be inconsistent, because the intervention on one slice holds fixed the very outputs that the counterparty is predicting. Intervening on the whole policy removes the inconsistency at the root: all branches of the agent's behavior move together, so every subjunctively dependent party sees the coherent counterfactual world.

This connects to why P-FDT agents are reflectively stable: the theory endorses its own use. Asked, mid-blackmail, whether to self-modify into a CDT-style payer "just this once," the P-FDT agent evaluates that proposal as a policy change — and the policy that pays is the policy that gets blackmailed. So she declines, stably. (Contrast CDT, which the authors note advises agents to self-modify away from CDT in future dilemmas while two-boxing in any ongoing one — a temporal inconsistency they reject as a mark against a normative theory.)

It also connects to voting and coalition problems in the source's conclusion: ten agents each decide whether to pay \$1,000 to vote, with \$1,000,000 payoff iff all ten vote. Each P-FDT agent recognizes that the others' decisions subjunctively depend on the same reasoning — effectively the same policy — and votes; ten CDT agents each stay home.

## 7. Dominance, Fairness, and Open Problems

Every method of constructing hypotheticals yields its own dominance relation. Two-boxing "dominates" under CDT counterfactuals; but this, the authors argue, "is merely a restatement of CDT's method for assessing an agent's options," not an independent argument. P-FDT has an analogous dominance notion — an action dominates if switching the *output of the algorithm*, holding fixed all subjunctive dependencies, is never worse — and P-FDT agents never take dominated actions in that sense. Dominance therefore cannot arbitrate between theories; the authors prefer the metric of **utility achieved**.

That metric must be applied fairly. The authors' informal criterion: a problem is "fair" if "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand" — where "behavior" should, on the policy reading, be understood as the agent's policy. Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." A predictor who reads your source code and punishes you for *running FDT* is unfair, and P-FDT will lose there — as any theory loses when punished for its identity. Footnote 15 acknowledges that no principled general transformation between "unfair to theory X" and "unfair to theory Y" problems is yet known.

Three open problems deserve emphasis, all flagged by the source:

1. **The $\True$/logical-dependence problem.** Equation (4) requires a graph $G$ of subjunctive dependencies *as an input* — there is no analogue of Pearl's method for learning logical/causal dependence structure from observation and experiment. "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Some hope for an evidential variant conditioning on logical facts, but "we currently lack a formal definition of conditional probabilities that can be used with false logical sentences."
2. **The policy domain.** Which inputs belong in $\mathcal{X}$ — this problem's observations only, or broader observation classes over which the agent is "the same"? The source is silent; the problem-relative reading I adopted above is the minimal one consistent with its examples, but a global reading (policies over all of life's dilemmas) would be needed for the gym-style self-coordination to be fully uniform. This is, to my knowledge, unresolved.
3. **Fairness formalization**, as above, and hence a general proof (or refutation) of the conjecture that P-FDT matches or beats every rival on all fair problems.

## 8. Conclusion

Policy functional decision theory is a single rule: *intervene on the mathematical function that maps your inputs to your actions; imagine the world in which that function outputs a different policy, with all subjunctively dependent consequences varying and everything else fixed; then apply the best such policy to your actual observations.* It inherits CDT's respect for causal structure (and hence smokes in the smoking lesion), extends respect to logical structure (and hence one-boxes, pays the hitchhiker, resists blackmail, votes, and goes to the gym), and — in its policy form — evaluates counterfactuals over whole input–output maps, which keeps multi-agent and multi-branch reasoning coherent. Its costs are real: a dependence on counterpossible reasoning without a settled semantics, and an input graph of subjunctive dependencies that no one yet knows how to infer. But the authors' central claim stands as a challenge worth taking seriously: among fair problems, a theory that asks "which output of this very procedure yields the best world?" has, so far, lost to none.

### References

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060. (Primary source; footnote 16 for P-FDT.)
- Pearl, J. (2000). *Causality.* Cambridge University Press.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.* Cambridge University Press.
- Soares, N. & Fallenstein, B. (2015). *Toward Idealized Decision Theory.* arXiv:1507.01986.
- Dai, W. (2009). *Towards a New Decision Theory.* LessWrong.