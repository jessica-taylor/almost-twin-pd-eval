# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

Action functional decision theory (A-FDT) is the version of functional decision theory (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") given by Equation (4) of Section 5:

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

I call it A-FDT because the intervention ranges over *actions*. The paper's footnotes 7 and 16 say the authors' preferred formalization ranges over *policies* (maps from observations to actions), and that the difference matters only in some multi-agent dilemmas. Everything below follows the action version. The policy version is a variant I mention only at the end.

Here is how I read the equation.

- $P$ is a probability distribution over the variables of the agent's world-model. These include variables for the outputs of mathematical functions.
- $G$ is a graph describing how changing a variable, including a *logical* one, changes the others. The paper calls this the "logical, mathematical, computational, causal, etc. structure of the world."
- $x$ is the observation history.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model. It represents the output of the A-FDT procedure itself when run on $(P,G,x)$. The underlines mean dequoting. The self-reference is harmless because the agent needs a variable *representing* the output, not its value. Kleene's second recursion theorem ("quining") shows such self-representation is possible.
- $V=\mathcal U(\text{Outcome})$, and $\mathrm{do}$ is Pearl's surgery operator. The node is set to $a$, and everything the graph marks as depending on it is recomputed. Everything else is untouched.

The procedure has four steps. For each action $a$, build a hypothetical by setting the $\mathrm{fdt}$ node to $a$. Propagate along the dependency graph. Compute expected utility. Output the argmax.

## 2. Comparison with its rivals

All three theories maximize $\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j)$. They differ in how they read "$\hookrightarrow$", which is Joyce's "epistemic perspective".

- EDT conditions: $\mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT intervenes on the physical act node: $\mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT intervenes on the logical node $\mathrm{fdt}(\ldots)$.

The paper identifies two differences from CDT.

1. The intervention is on the *type* (the function's output), not the token (the physical act).
2. Observation is handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes *which node it intervenes on*, from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

The second difference does much of the work. It is why A-FDT can imagine that, had its output been different, it would have *seen something different*.

The slogan is that A-FDT is to subjunctive dependence as CDT is to causal dependence. In the paper's words, A-FDT's hypotheticals "preserve all decision-relevant subjunctive dependencies". EDT's hypotheticals respect too many correlations, including merely statistical ones. CDT's respect too few.

## 3. Subjunctive dependence

Two systems subjunctively depend on a function when they compute it. The paper's example is two calculators computing $6288+1048$. If one outputs 7336, the other almost certainly does too, and a predictor's model of an agent stands in the same relation to the agent. Causal dependence is a special case: a scribe copying a calculator's output depends on it subjunctively as well as causally. Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators do not covary under the intervention "had the scribe bought a green one."

The upshot is that A-FDT treats a predictor and a lesion differently. A predictor contains a model of the agent's decision function, so its output moves with the function's output. A lesion causes both the urge to smoke and the cancer, but the cancer does not compute the agent's decision.

## 4. Worked examples

**Newcomb's problem.** Fiona's graph has a node $\mathrm{fdt}(P,G)$ with arrows to both $\mathrm{Act}$ and $\mathrm{Prediction}$. The predictor is accurate with probability 0.99. Setting $\mathrm{fdt}=\text{onebox}$ gives $0.99\times\$1{,}000{,}000=\$990{,}000$. Setting it to twobox gives $0.01\times 1{,}001{,}000+0.99\times 1{,}000=\$11{,}000$. She one-boxes.

She believes in no retrocausation. She simply declines to imagine her function outputting something different while the predictor's copy of it stays fixed.

**Smoking lesion.** The graph differs, because the lesion is not a function of the decision procedure. The paper models the lesion as determining which utility function the agent has ($\mathcal U_S$ or $\mathcal U_R$). That means two nodes, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, with the lesion selecting which one controls $\mathrm{Act}$. Intervening on either leaves $P(\text{lesion})=p$ unchanged. Smoking comes out ahead by $p\cdot\$1{,}000$, so she smokes. The same equation therefore yields one-boxing and smoking. The paper adds that this problem is contrived and recommends abandoning it.

**Transparent Newcomb and Parfit's Hitchhiker.** Fiona sees a full box, so she intervenes on $\mathrm{fdt}(P,G,\text{full})$. That node feeds $\mathrm{Prediction}$ and, if the prediction was one-box, controls $\mathrm{Act}$. If the prediction was two-box, a different node, $\mathrm{fdt}(\ldots,\text{empty})$, controls $\mathrm{Act}$. Setting the full-box node to onebox gives about $\$990{,}000+0.01q\cdot 1000$. Setting it to twobox gives about $\$110{,}000+q\cdot\$990$. She one-boxes while looking at two full boxes, because when she imagines two-boxing she imagines (probably) seeing an empty box. This is equivalent to paying the driver in Parfit's problem.

**Mechanical blackmail.** Having received the letter, Fiona refuses to pay. In the "refuse" hypothetical, the blackmailer (a predictor of her function) probably never sent the letter. The paper also works the imperfect-predictor case. With error rate 0.0009 she refuses, since refusing costs about \$900 in expectation against \$1,000 for paying. At 0.011% error, the comparison reverses and she pays.

**Death in Damascus.** Death's location depends on the book entry, which depends on the agent's function. Fiona stays, saving the \$1,000. CDT instead becomes unstable, and its pseudorandomized versions refuse a \$1 truly random coin worth a 50% survival chance.

**XOR blackmail.** Carl and Fiona both refuse, for different reasons. Carl refuses because infestation is causally upstream of his act. Fiona refuses because changing her function's output changes whether the letter is sent but not whether termites are present. Eve (the EDT agent) pays, because conditional on paying the letter is good news.

**Cosmic ray.** A-FDT takes the \$100. It simply breaks the merely statistical correlation between taking \$100 and being hit by rays.

## 5. What the source does not settle

**The dependency graph $G$ is an input.** The paper is explicit about this. Equation (4) works *given* a graph describing how changing a logical variable affects other variables, but "it is not yet clear how to construct such a thing—nor even whether it can be done in a satisfactory manner within Pearl's framework." It calls this "perhaps the largest open problem." So A-FDT is a well-defined function of $(P,G,x)$. It is not a full algorithm for going from raw evidence to action.

The paper also says it lacks a definition of the $\mathtt{true}$ operator, which would condition on false logical sentences. This is why it uses $\mathrm{do}$ instead.

**Operational reading (my proposal, not the paper's).** I suggest the following practical test for constructing $G$. For each variable $Z$ in the model, ask: "If the decision procedure I am running had output something else on this input, would $Z$ have been different?" That is, ask whether $Z$ is computed from, or contains an accurate model of, this procedure.

- Predictors, twins, and copies are marked dependent.
- Common-cause conditions such as lesions, past infestations, and weather are marked independent.
- Observations are marked dependent when the observer's environment responds to the agent's behavior, as in the transparent box.

When dependence is partial, I would encode it as a stochastic edge. The paper's accuracy variable ($0.99$ in Newcomb, a $0.0009$ error in blackmail) does exactly this.

**The "fair problem" restriction.** The authors claim A-FDT does at least as well as CDT and EDT on "fair" problems, meaning problems where outcomes depend only on the agent's behavior in that problem. Fairness is not formalized. Footnote 15 notes that a problem punishing agents who act like a copy of Fiona is unfair to her. The paper also admits that "we do not yet know whether FDT is optimal among decision theories."

**Evaluating counterpossibles.** The authors acknowledge that A-FDT's hypotheticals are counterpossible, since the function in fact has one output. They argue the difficulty is technical, because agents need only reason locally about how particular predictions would change. They point to humans' ability to do this as evidence.

**Policies versus actions.** Equation (4) as written intervenes on action-valued nodes indexed by observations. Because the node used depends on $x$, it already behaves like a lookup into a policy. Footnotes 7 and 16 say the policy version differs only in multi-agent cases. I do not develop that here.

## 6. Why one should accept it

The paper's main argument is utility: agents using A-FDT get richer on fair problems, so a theory that recommends otherwise is hard to call rational. Secondary arguments are:

- A-FDT agents act as they would have precommitted to act, without paying for precommitment.
- They never assign negative value to information.
- They are reflectively stable, since an A-FDT agent holding the blackmail letter does not want to switch to CDT.
- They cannot be accused of a worse "delusion of control" than CDT agents in deterministic worlds. CDT agents also imagine changing a token that is physically fixed.

The dominance argument for two-boxing is answered in kind. Dominance is relative to a method of building hypotheticals. CDT dominance holds the prediction fixed. A-FDT dominance holds fixed all relevant subjunctive dependencies, and by that standard A-FDT never takes a dominated action.

## 7. A usable recipe

1. Write down the model $(P,G)$ with a node $\mathrm{fdt}(P,G,x)$ for each possible observation.
2. For each $a$, do the surgery and propagate along the dependence edges, including those into predictors and into whichever observation-indexed node controls $\mathrm{Act}$.
3. Compute $\mathbb E[V]$ and choose the maximum.

The result depends on $G$, so the user must make honest judgments about which things really compute the agent's function.

## Conclusion

A-FDT is a single rule of the same form as CDT, with the intervention moved from a physical act to the logical output of the agent's own decision procedure. Observation changes the node intervened on rather than the distribution conditioned on. In the source's examples this yields one-boxing, smoking, paying the driver, refusing blackmail, and staying in Damascus. Its weak point is also stated by the authors: no principled method yet exists for inferring the subjunctive-dependence graph.