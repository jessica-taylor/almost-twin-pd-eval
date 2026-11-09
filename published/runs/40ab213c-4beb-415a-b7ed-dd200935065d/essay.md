# A-FDT: Choosing by Intervening on the Decision Function

## 1. The idea

A-FDT is the decision theory defined by Equation (4) of Yudkowsky and Soares' "Functional Decision Theory: A New Theory of Instrumental Rationality." This essay uses "A-FDT" for that equation and calls the other theories by their usual names, EDT and CDT.

All three theories maximize expected utility. They differ in how they build the hypothetical used to evaluate each action. The paper follows Gibbard and Harper and writes expected utility as

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where "$\hookrightarrow$" is the connective for decision hypotheticals. Following Joyce, the paper says the theories disagree about "the epistemic perspective from which actions are to be evaluated," not about value. EDT reads $\hookrightarrow$ as Bayesian conditioning. CDT reads it as Pearl's $\mathtt{do}$ on the physical act. A-FDT reads it as a $\mathtt{do}$ on a node representing the output of the agent's own decision function.

## 2. The definition

The agent has a world-model $(P, G)$. $P$ is a probability distribution over variables. $G$ is a graph saying how changing one variable changes the others. Unlike a purely causal graph, $G$ must encode logical, computational and causal dependence. The agent also has an observation $x$. Equation (4) is

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The underlines mean dequoting. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of this very procedure on these very inputs. The self-reference is harmless. The agent need not know the value of the output in order to have a variable representing it. The paper points to Kleene's second recursion theorem ("quining") for how a structure can contain a representation of itself.

The procedure has four steps:

1. Build $(P,G)$ so that it encodes the problem, including every physical process that depends on the decision function (predictors, copies, twins, later selves).
2. For each action $a$, perform surgery: set the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $a$. Propagate along $G$ to every variable that depends on it, by cause or by logical or subjunctive dependence. Hold everything else fixed.
3. Compute $\mathbb E[V]$ in each resulting hypothetical.
4. Output the maximizing $a$.

Two differences from CDT follow, and the paper states both.

- **Where the intervention happens.** CDT intervenes on the token "my action is $a$." A-FDT intervenes on the type, the function's output. The agent's own act is one downstream variable among others.
- **How observation is handled.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not update by conditioning. It changes which node it intervenes on: $\mathrm{fdt}(\ldots,x)$ rather than $\mathrm{fdt}(\ldots,y)$. This is why A-FDT can imagine that, had it acted differently, it would have seen something different.

Where the model's dependencies are purely causal, all three theories agree. In the paper's words, then, $\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}=a)]$. They come apart when something correlates with the action without being caused by it, as with a predictor.

## 3. Subjunctive dependence

A variable subjunctively depends on the decision function if it would be different had the function output something different. Two calculators computing $6288+1048$ are the standard example. Causal dependence is a special case. Mere statistical correlation is not an instance: two pink calculators in Paris and Tokyo do not depend on each other's colour. This is the line A-FDT draws between a predictor, which models the agent, and a lesion, which only correlates with her.

If the predictor is imperfect, the dependence is weakened but not removed. In the model it becomes an accuracy variable that sits between the function and the prediction.

## 4. What A-FDT leaves open, and an operational reading

The paper is candid that Equation (4) "rests on shakier philosophical foundations" than the CDT equation. It does not say how to learn or deduce $G$. It calls this "perhaps the largest open problem." The ideal operator $\mathtt{true}(\mathrm{fdt}=a)$, which would condition on a logical falsehood, is undefined. The paper therefore takes the dependency structure as an input, just as CDT takes the causal structure as an input.

Footnotes 7 and 16 say the authors' preferred version intervenes on policies, meaning maps from observations to actions. The paper's examples use actions indexed by observation.

The following operational reading is my own proposal, not the paper's. To build $G$ for a new problem, ask of each variable: "Is this a computation, or a physical process that contains a model of a computation, which would give a different answer if the agent's decision procedure, run on my actual inputs, returned a different output?" If so, it is a child of the node. A usable checklist:

- Does something predict or simulate me? Link it to the node.
- Is there a copy or twin running the same procedure on the same inputs? Link it.
- Is a past or future self facing a relevantly similar input? Link it.
- Is the correlation only statistical, through a common cause that does not model my procedure? Do not link.

Anyone who can specify $G$ can run the procedure. Whether $G$ is right is a separate question that A-FDT does not answer.

## 5. Worked examples

**Twin prisoner's dilemma.** The node $F$ is the output of the shared function. It sets both the agent's move and the twin's. Setting $F=C$ gives \$1,000,000 and setting $F=D$ gives \$1,000, so A-FDT cooperates. CDT would intervene on the agent's act alone and so defect.

**Newcomb's problem.** The paper's graph has $F$ as a parent of both Act and Prediction. Accuracy is 0.99, so $F=\text{onebox}$ gives box B full with probability 0.99, and expected utility is \$990,000 on the paper's numbers. $F=\text{twobox}$ gives full with probability 0.01 and \$11,000. A-FDT one-boxes. The agent does not believe in retrocausality. She just considers it foolish to imagine her act changing while the function's output stays fixed, given a predictor of the function.

**Smoking lesion.** Here the graph differs. The lesion is not linked to $F$. The lesion causes the desire to smoke, which fixes which of two functions the agent runs, and it causes cancer. Intervening on $F$ leaves $P(\text{lesion})=p$ unchanged. Smoking gains \$1,000 with probability $p$ that this function controls her act. A-FDT smokes. The same rule one-boxes in Newcomb and smokes in the lesion problem, which the paper presents as an advantage over EDT and CDT, each of which gets one of them wrong.

**Transparent Newcomb and Parfit's hitchhiker.** Suppose the agent sees a full box. She intervenes on $\mathrm{fdt}(\ldots,\text{full})$. Setting it to onebox gives, with accuracy 0.99, a full box and \$1,000,000. Setting it to twobox makes a predictor of this function likely to have left B empty, so she would likely have seen empty and run the other node. The paper gives these values as $990{,}000+0.01q\cdot 1000$ against $110{,}000+q\cdot 990$ (printed there as "\$110,00"). A-FDT one-boxes while looking at two full boxes. Paying the hitchhiker is structurally the same. The paper's arguments in support are precommitment (she acts as she would have precommitted), non-negative value of information, and utility achieved.

**Mechanical blackmail.** A perfect predictor runs the blackmail only if she predicts payment. Setting the node to "pay" makes blackmail near-certain and costs \$1,000. Setting it to "refuse" makes blackmail near-impossible. A-FDT refuses even while holding the letter. With an imperfect blackmailer the choice is quantitative. The paper says refusal holds when the false-positive rate is 0.0009, since the expected loss is \$900 against \$1,000, and that she pays when it is 0.011%. (That second figure does not look consistent with the stated payoff arithmetic, so I would not rely on it.)

**XOR blackmail and Death in Damascus.** Termites are not downstream of the function, so A-FDT refuses to pay, because the letter's presence changes under the intervention while the infestation does not. EDT pays because it conditions on good news. In Death in Damascus, Death's book depends on the function, so A-FDT stays in Damascus and saves \$1,000. CDT oscillates, because it holds Death's location fixed under its intervention.

## 6. A short numerical recipe

Suppose a predictor of accuracy $\alpha$ fills a box worth $M$ iff she predicts one-boxing, and the other box holds $m$.

- $\mathcal{EU}(\text{one})=\alpha M$.
- $\mathcal{EU}(\text{two})=(1-\alpha)M+m$.

A-FDT one-boxes iff $\alpha M > (1-\alpha)M + m$, that is, iff $\alpha > \tfrac12 + \tfrac{m}{2M}$. For $M=10^6$, $m=10^3$ the threshold is $0.5005$. This extends the paper's 0.99 case. It is my arithmetic, not a claim from the source.

## 7. How the theory treats dominance and fairness

The paper rejects dominance as a neutral criterion. Every way of building hypotheticals defines its own dominance relation. Two-boxing dominates under CDT counterfactuals and refraining dominates under conditioning. Under A-FDT's own counterfactuals, A-FDT agents never take a dominated action. So the paper prefers to judge theories by utility achieved.

It limits this claim to "fair" problems, those where the outcome depends only on what the agent does in the problem and where her beliefs are accurate. Rewarding actions, such as one-boxing, is fair. Rewarding adherence to a named theory is not. The paper admits it has no formal definition of fairness. It also says it is unknown whether the theory is optimal.

## 8. Objections and my assessment

The paper holds that A-FDT agents are no more deluded than CDT agents. Both imagine alternatives that cannot occur given determinism: a different token for CDT, a different type output for A-FDT.

My own cautions:

- The theory's behaviour is only as good as $G$. A wrongly drawn dependence, such as treating a lesion as a predictor, makes A-FDT behave badly. Equation (4) offers no defence against that.
- There is a possible circularity. $P$ includes beliefs about the function's own output, and the node is defined in terms of $P$. The quining argument shows the representation is well-formed. It does not show that the beliefs are consistent or that equilibrium is unique. The paper does not discuss this.
- Problems that reward being the kind of agent who thinks about the world in a particular way, as opposed to what she does, are outside what the theory claims to handle.

## 9. Conclusion

A-FDT is "CDT with a different intervention point." The agent asks which output of this very function leads to the best imagined world, where the imagined world respects every dependence on that output. Where dependence is purely causal it agrees with CDT and EDT. Where predictors, twins or copies appear it diverges, one-boxing in Newcomb, cooperating with twins, paying the hitchhiker, and refusing blackmail while still smoking in the lesion problem. The formal procedure is simple. The open problem is the input $G$: how to discover and represent subjunctive dependencies, and what counts as fair.

**Reference:** Yudkowsky, E. and Soares, N., "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.