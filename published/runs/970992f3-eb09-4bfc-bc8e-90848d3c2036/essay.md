# A-FDT: Choosing by Intervening on Your Decision Function

## 1. The core idea

Action functional decision theory (A-FDT) is the version of functional decision theory given by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." This essay explains that equation, shows how to apply it, and marks where the paper stops. I call it A-FDT because it intervenes on the output of the decision function as an action. The paper's footnotes 7 and 16 say the authors prefer a policy-valued version, in which the intervention selects a mapping from observations to actions. The paper sets that version aside, and so do I, apart from one remark in §6.

The source states the guiding principle this way: treat one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Causal decision theory (CDT) asks which physical act causes the best outcome. Evidential decision theory (EDT) asks which act would be the best news. A-FDT asks which output of this very procedure leads to the best outcome.

## 2. The formal definition

All three theories maximize expected utility, $\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;x)\,\mathcal U(o_j)$ (Equation 1). They differ only in how they read the decision-hypothetical connective "$\hookrightarrow$". Following Joyce's representation theorem, which the paper borrows, they supply different "epistemic perspectives" on one common expected-utility structure.

The agent keeps a world-model $M$ and builds a hypothetical $M^{a\hookrightarrow}$ for each action. She computes the value $V_a$ of each hypothetical and takes the argmax. The hypotheticals are "mental or computational objects used as tools," comparable to "notes on scratch paper," and are not beliefs.

The paper's formulas for the three theories are:

- EDT: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT: $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **A-FDT (Equation 4):**
$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are a probability distribution $P$ over the model's variables, a graph $G$, and an observation history $x$. The graph encodes "the logical, mathematical, computational, causal, etc. structure of the world." It says how changing a logical variable changes the other variables. $\mathrm{do}$ is Pearl's surgery operator: set the intervened node, recompute everything downstream of it, and leave everything else untouched.

The underlines denote dequoting. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is the variable in the model that stands for the output of the A-FDT procedure run on exactly these inputs. The self-reference is harmless. The agent need not know the value of that output in order to have a variable representing it, and Kleene's second recursion theorem (quining) shows how a structure can contain an accurate representation of itself.

### Two differences from CDT

1. **Where the intervention goes.** CDT intervenes on $\mathrm{Act}$, a physical fact about the agent's body. A-FDT intervenes on a logical fact, the output of her decision function. In Peirce's terms, CDT intervenes on the token and A-FDT intervenes on the type. $\mathrm{Act}$ is then downstream of the fdt node, and so is anything else that computes or predicts the same function.
2. **How observations enter.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes which node it intervenes on, namely $\mathrm{fdt}(\underline P,\underline G,\underline x)$ versus $\mathrm{fdt}(\underline P,\underline G,\underline y)$. The observation is an input to the function being evaluated, not a fact held fixed across hypotheticals. This is why A-FDT can imagine that, had its output been different, it would have seen something different.

### Subjunctive dependence

Variable $Z$ subjunctively depends on the function if, were the function's output different, $Z$ would be different. Two calculators computing $6288+1048$ depend on the same function. Causal dependence is a special case: a scribe copying a calculator's display also subjunctively depends on it. Mere statistical correlation is not enough. Two pink calculators are correlated in color, but changing one's color would not change the other's.

The paper's claim is that A-FDT is to subjunctive dependence as CDT is to causal dependence. Its hypotheticals keep exactly the dependencies that track the function and break correlations that are merely statistical. Compared with the other two theories, EDT "respects too many" action–environment correlations and CDT "respects too few."

## 3. What the source leaves open

The input $G$ is given, not derived. The paper says plainly that "Equation (4) … rests on shakier philosophical foundations than (3)." There is no analogue of Pearl's account for inferring subjunctive-dependence structure from data. It calls this "perhaps the largest open problem" for the theory. A more direct operator $\mathtt{true}(\phi)$, for conditioning on a false logical sentence, is also undefined. That is the counterpossible problem. The paper's pragmatic move is to require the dependency structure as an input, just as CDT requires causal structure as an input. It also argues that humans reason tolerably about counterpossibles, and that the agent only needs narrow ones, such as "how would this predictor's prediction change if my algorithm's output changed?"

So in practice A-FDT is a well-defined procedure relative to a model. It is not yet a method for building the model. When I say below that "the graph says X," I am taking the modeler's description of the problem as correct, which is the paper's own practice.

## 4. Worked applications

**Newcomb's problem.** The agent's graph (Fiona's, in the paper's notation) has one node $\mathrm{fdt}(\underline{P},\underline{G})$ with arrows to both $\mathrm{Act}$ and $\mathrm{Prediction}$. $\mathrm{Prediction}$ also depends on an $\mathrm{Accurate}$ noise variable ($0.99$). $\mathrm{Box\,B}$ follows from $\mathrm{Prediction}$.

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$ gives $P(\text{full})=0.99$ and an expected value of $\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$ gives $P(\text{full})=0.01$ and an expected value of $\$11{,}000$.

A-FDT one-boxes. The paper says no retrocausal physics is invoked. The agent simply thinks it foolish to imagine her action changing while the predictor's model of her stays fixed.

An objection: if she is nearly sure box B is full, why not take two boxes? The answer is that her hypothetical for two-boxing is not "same world, different act." It is "this function outputs twobox," and that world has an empty box.

**Smoking lesion.** Here the graph has no arrow from the fdt node to $\mathrm{Cancer}$. The lesion causes both the desire and the cancer, and the function's output is independent of the lesion. (The paper formalizes this with two possible models, $P_S$ and $P_R$, depending on whether the agent has the lesion, so the agent chooses under uncertainty about her own preferences.) Intervening gives the same $P(\text{lesion})=p$ in both hypotheticals. Smoking is better by $p\cdot\$1{,}000$, so the agent smokes. The same equation therefore one-boxes and smokes, because only the graph differs. The paper concedes that the problem is contrived and recommends abandoning it.

**Transparent Newcomb and Parfit's hitchhiker.** Observations change which node is intervened on. Suppose the agent sees a full box and evaluates $\mathrm{do}(\mathrm{fdt}(\underline{P},\underline{G},\text{full})=a)$. With $\mathrm{Accurate}$ at 0.99:

- Setting the output to onebox gives $0.99\cdot\$1{,}000{,}000+0.01\cdot q\cdot\$1{,}000$.
- Setting it to twobox gives about $\$11{,}000$, plus a term in $q$.

Here $q$ is her credence that she would two-box on seeing an empty box; its value barely matters. In the twobox hypothetical, the prediction was "twobox," the box is empty, and a different node ($\mathrm{fdt}(\ldots,\text{empty})$) controls her act. A-FDT leaves the $\$1{,}000$ behind. The paper stresses that this is formally the same problem as paying the driver in Parfit's hitchhiker, and that A-FDT pays.

**XOR blackmail, mechanical blackmail.** In the XOR case, $\mathrm{Infestation}$ is not downstream of the function, so intervening does not change its probability. The intervention does change whether the letter is sent. Paying makes the letter a signal of "no termites" only through correlation, which the surgery severs. A-FDT refuses. In the mechanical blackmail case, refusing is evaluated in a world where the blackmailer, predicting refusal, never ran the program. With predictor error $0.0009$, paying costs $\$1{,}000$ for sure, while refusing is blackmailed $0.09\%$ of the time with expected loss $\$900$. So she refuses even while holding the letter. If the error rate is $0.011\%$, she pays.

**Death in Damascus.** Death's book entry depends on the agent's function. Whichever output is imagined, Death's location moves with it, so staying (saving $\$1{,}000$) is best. CDT instead imagines Death's location held fixed and is unstable.

**Cosmic ray.** A-FDT, like CDT, takes the $\$100$. It breaks the merely statistical correlation between taking $\$100$ and being hit by a ray.

When the dependencies are exactly the causal ones, the three theories agree: $\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$.

## 5. A recipe for unfamiliar cases

This procedure is my own packaging of the source's definitions, not a quotation from it.

1. Identify every process that computes, or reliably models, the same function as the agent: twins, predictors, copies of her future self, and mind-readers of her choices.
2. Draw the graph with a node for each distinct input the function might receive, since observations change which node is active. Make her act depend on whichever node is active. Make the predictors' outputs depend on the relevant nodes.
3. Mark as independent of the node everything that merely correlates with her behavior through a common cause, such as a lesion, a disposition she cannot revise, or a termite infestation.
4. For each action, intervene on the node corresponding to her actual observations, propagate the surgery, and compute expected utility. Take the argmax.

The substantive modeling work is steps 1 to 3. The paper does not give a general rule for step 3 when a predictor's accuracy is partial or the process is opaque. I would treat that as the place where judgment, and error, enter.

## 6. Why the paper thinks this is right

The paper's central argument is utility. A predictor who can follow the reasoning sees that CDT and EDT agents two-box in the transparent problem, while A-FDT agents one-box, so A-FDT agents face full boxes. A secondary argument is that A-FDT "always acts as it would have precommitted to act," without costly binding. It also assigns no negative value to information, and it is reflectively stable in "fair" problems. The paper says A-FDT would not want to switch to CDT even after seeing blackmail.

The paper rejects dominance as a neutral tiebreaker. Every method of building hypotheticals induces its own dominance relation. In A-FDT's, holding the subjunctive dependency fixed, two-boxing is dominated.

The paper also takes up the charge that the theory's odd advice shows mistaken beliefs about causation. It replies that CDT's talk of "controlling" a deterministic action token is no better off than A-FDT's talk of controlling a function's output type. Both use imagined variation that cannot actually occur.

**Fairness.** The paper restricts its claims to "fair" problems, where outcomes depend only on the agent's behavior in the problem at hand and the agent's beliefs are accurate. Rewarding "act differently from the A-FDT agent" is unfair to A-FDT, and rewarding or punishing a decision procedure as such is unfair to every theory. The paper has no formal criterion for fairness and admits that making one precise is hard. The claim that A-FDT loses in no fair problem is therefore informal.

## 7. Caveats

- Reliance on supplied dependency structure is the major gap. A-FDT's prescription varies with how a modeler draws arrows, and the paper offers no check on this.
- Partial correlations, as with imperfect predictors or similar but non-identical reasoners, are handled in the examples by noisy nodes (the $0.99$ accuracy variable). A general treatment would need a graded notion of dependence, which the source does not define.
- Policy versus action: the authors prefer the policy-level version, reportedly relevant only in multi-agent problems. This essay's treatment inherits the paper's setting-aside of that point.
- The paper treats the single-shot cases carefully but does not work out multi-round cases. Its voting and gym examples are sketches.

## 8. Conclusion

A-FDT keeps the expected-utility skeleton of CDT and changes two things: the intervention targets the output of the agent's decision function, and observations select which function-instance is intervened on. This one change yields cooperation with twins, one-boxing, smoking, paying in Parfit's hitchhiker, and refusing blackmail from a single rule, while declining to "manage the news." Its weakness is that the rule is only as good as the dependency graph, and there is not yet a principled theory of where such graphs come from.