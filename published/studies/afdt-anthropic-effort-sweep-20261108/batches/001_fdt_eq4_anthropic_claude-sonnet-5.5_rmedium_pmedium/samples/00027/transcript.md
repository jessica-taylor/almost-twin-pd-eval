# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00027

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/47313105-2b61-476f-a696-e4eedbc3fb13/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/47313105-2b61-476f-a696-e4eedbc3fb13/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

Most decision theories evaluate an act by asking what would happen if it were taken. They differ in how they read "would happen." This essay explains **A-FDT** (action functional decision theory), the theory given by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." The slogan is that the agent treats her decision as the output of a fixed mathematical function and asks "Which output of this very function would yield the best outcome?" I will separate what the paper says from what I add, and I flag the additions.

## 2. The formal definition

The paper treats EDT, CDT and FDT as expected-utility theories. Each maximizes

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is the connective for decision hypotheticals. Following Joyce, the paper says the theories do not disagree about value. They disagree about "the epistemic perspective from which actions are to be evaluated."

Two ingredients define the three theories:

- a world-model $M$;
- a rule for building, for each action $a$, a hypothetical $M^{a\hookrightarrow}$ from $M$.

For EDT, $M=P$ and the hypothetical is conditionalization. For CDT, $M=(P,G)$ with $G$ a causal graph, and the hypothetical is Pearl's surgery $\mathtt{do}(\textsc{Act}=a)$. A-FDT, as given in Equation (4), is

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\Big(\textsc V\;\Big|\;\mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution over the model's variables, including variables for the outputs of mathematical functions. $G$ is a graph of "logical, mathematical, computational, causal, etc. structure," saying how changing a logical variable affects every other variable. $x$ is the observation history. $\textsc V=\mathcal U(\textsc{Outcome})$. The underlines denote dequoting, so $\textsc{fdt}(\underline P,\underline G,\underline x)$ names the variable standing for the output of A-FDT on inputs $P,G,x$.

The self-reference is harmless. The agent need not know the value of the variable, only have a variable representing it. Kleene's recursion theorem ("quining") shows that such self-representing structures can be built.

## 3. The two differences from CDT

The paper identifies exactly two differences between Equations (3) and (4).

1. **Where the surgery happens.** CDT intervenes on a node for the physical action. A-FDT intervenes on a node for the output of the decision procedure. This is Peirce's type/token distinction: CDT intervenes on the token "my action is $a$," while A-FDT intervenes on the type.
2. **How observations are handled.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition. It changes which node it intervenes on, namely $\textsc{fdt}(\cdot,\cdot,x)$ rather than $\textsc{fdt}(\cdot,\cdot,y)$. Observations select a node. They are not evidence to be conditioned on.

Because the intervention is on the function's output, everything that subjunctively depends on that output moves with it. This includes the agent's body, any predictor or twin, and, in the paper's examples, even whether the agent receives a given observation at all.

## 4. Subjunctive dependence

Subjunctive dependence is the relation between two systems that compute (or model) the same function: "if the output were different, this would be different." The paper makes several claims about it:

- Causal dependence is a special case. The scribe copying a calculator's display depends on it both causally and subjunctively.
- Statistical correlation does not entail it. Two pink calculators are correlated, but swapping one for a green one leaves the other pink.
- An imperfect predictor or a noisy agent weakens the dependence without eliminating it.

The summary is: A-FDT is to subjunctive dependence as CDT is to causal dependence. When all correlations with the action are caused by the action, EDT, CDT and A-FDT agree.

## 5. Counterpossibles, and what the paper leaves open

If a function outputs *cooperate* on a given input, it does so necessarily. Imagining a different output is therefore a counterpossible. The paper concedes that no satisfactory account of counterpossible reasoning exists and calls this the main drawback relative to CDT. It also notes that the $\mathtt{true}$ operator on logical sentences is not defined. Its response is to require the dependence structure $G$ to be given as an input, just as CDT requires the causal graph. It adds that deducing subjunctive dependence from observation and experiment is "perhaps the largest open problem."

This has a practical consequence. **A-FDT as specified is a procedure relative to a supplied $(P,G)$.** It is not a method for finding $G$. Any application therefore makes a modelling commitment about which variables depend on the decision function. The paper is explicit that an agent should imagine changes in "all and only those things that subjunctively depend on the output of her decision-making procedure."

**Operational heuristic (my proposal, not the paper's).** To decide whether a variable $Z$ belongs downstream of the function node, ask whether $Z$'s value is produced by a process that computes, models or copies this decision function. This holds for twins, simulators and reliable predictors that reason about the agent. It fails for a common cause that merely correlates with the agent's behavior without modelling it, such as the lesion. A second test is to ask whether the correlation would survive if the agent were replaced by a different decision procedure. If it would, it is statistical and should be severed. If it is mediated by the agent's procedure being the thing consulted, it is subjunctive and should be kept. This follows the paper's contrast between predictors and lesions. The paper does not give a general algorithm.

## 6. Applying A-FDT: worked cases

**Newcomb's problem.** Fiona's graph has $\textsc{fdt}(P,G)$ as a parent of both $\textsc{Act}$ and $\textsc{Prediction}$, with $\textsc{Accurate}$ true at 0.99. Then:

- $\mathtt{do}(\textsc{fdt}=\textit{onebox})$ gives Box B full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathtt{do}(\textsc{fdt}=\textit{twobox})$ gives Box B full with probability 0.01, so $\mathbb E[V]=\$11{,}000$.

She one-boxes. The paper stresses that no retrocausal physics is invoked. She thinks it foolish to imagine her action changing while the prediction stays fixed, since the predictor reasons about her algorithm. Even if she is nearly certain the box is full, asked what would happen if she two-boxed, she says the algorithm would have output *twobox* on this input and the prediction would have differed.

**Smoking lesion.** Her graph here connects the function node to $\textsc{Act}$ but not to $\textsc{Cancer}$. The lesion is a common cause of both. The paper formalizes the problem with two utility functions, $\mathcal U_S$ for agents with the lesion, who like smoking, and $\mathcal U_R$ for agents without it. Fiona does not know which procedure she runs, so $\textsc{Act}$ depends on $\textsc{Lesion}$ and on both function nodes. Intervening on the relevant node leaves $P(\textit{lesion})=p$ unchanged. Smoking comes out ahead by $p\cdot\$1{,}000$, so she smokes. One rule yields one-boxing in Newcomb and smoking here. Only the graph differs. The paper adds that this formalization is contrived and recommends that philosophers abandon the problem.

**Transparent Newcomb and Parfit's hitchhiker.** Here observation selects the node. Fiona sees a full box and intervenes on $\textsc{fdt}(P,G,\textit{full})$. That node feeds the prediction. If the prediction is *one-box-when-full*, she sees full and the node controls her action. Otherwise she sees empty and a different node controls it. With $q$ her credence that she two-boxes on seeing empty, the paper computes:

- one-boxing: $\$990{,}000+0.01q\cdot\$1{,}000$;
- two-boxing: roughly $\$11{,}000+q\cdot\$990$.

So she one-boxes even though she sees the full box. The paper says this is equivalent to paying the driver in Parfit's hitchhiker, and gives three supporting arguments:

- the precommitment argument;
- the value-of-information argument;
- the argument from utility.

It treats utility as the argument that gives the other two their force.

**XOR blackmail.** The letter arrives iff exactly one holds: the rumor is false and she pays, or the rumor is true and she does not pay. EDT pays, because conditioning on paying implies no termites. CDT refuses because infestation is upstream of $\textsc{Act}$. A-FDT also refuses, and for a different reason. Intervening on $\textsc{fdt}(\cdot,\cdot,\textit{letter})$ changes what she does on receiving the letter and the probability that she sees it at all, but not the probability of infestation. The two hypotheticals therefore differ only in whether the letter is sent, and paying has no compensating benefit.

**Mechanical blackmail.** She has received the letter and imagines refusing. In that hypothetical she was never blackmailed, so she refuses. For a fallible blackmailer, the paper computes with a wrong-prediction rate of 0.0009. Paying loses \$1,000 for certain. Refusing loses \$900 in expectation, since she is blackmailed 0.09% of the time and then loses \$1,000,000. She refuses. At an error rate of 0.011% she would pay.

**Death in Damascus.** Death's location depends on the book entry, which depends on the agent's decision function. Fiona imagines Death meeting her wherever she goes. She stays and saves the \$1,000. CDT is unstable here because it varies the act while holding Death fixed. The paper also argues this makes CDT mis-value a truly random coin that gives a 50% chance of survival.

## 7. Why A-FDT is not "updating on nothing"

The paper's phrase is that A-FDT responds to evidence by changing "*the place in her graph where she intervenes*." There is still a response to observations, but it is not Bayesian conditioning inside the hypothetical. The paper notes this is the source of "updateless" in Dai's name for an early variant. It also says Yudkowsky's earlier Timeless Decision Theory both conditioned on evidence and changed the intervention point, a "double update" that "proves harmful in practice."

The paper also observes that A-FDT should entertain hypotheticals where observations would have differed. Both CDT and A-FDT hypotheticals contain impossibilities. CDT imagines a perfect predictor erring. A-FDT imagines her observations being inconsistent with her actual ones.

## 8. Policies versus actions

The paper's footnotes say the authors' preferred formalization actually iterates over **policies**, mappings from observations to actions, rather than over actions. Equation (4) uses actions for exposition, and the paper says the difference matters only in certain multi-agent dilemmas. This is why I call the present object *A-FDT*. It is the action-level formula, with the observation-indexed node doing much of the work that a policy would.

**Reading it operationally (my interpretation).** Because each observation value has its own node $\textsc{fdt}(P,G,x)$, a single run of Equation (4) at observation $x$ chooses the output of one node. The other nodes enter as uncertainty, such as the $q$ in the transparent-Newcomb calculation, and the paper notes the correct $q$ is 1 (and in the smoking case $q=0$). Following the paper, I treat these as the agent's beliefs about how the procedure behaves on other inputs. A reader wanting global consistency can pick the policy that maximizes the same expectation across all nodes jointly. That is a reasonable extension, but it is exactly what the paper defers.

## 9. A recipe

1. Build $P$ over the problem's variables, including nodes for the decision function's outputs under each possible observation.
2. Build $G$. Draw the function node into every variable that models or copies the decision procedure, and keep ordinary causal arrows. Keep common causes that do not model the agent as ordinary upstream variables.
3. Identify the node corresponding to your actual observations.
4. For each $a$, apply $\mathtt{do}(\textsc{fdt}(\ldots,x)=a)$, propagate, and compute $\mathbb E[V]$.
5. Output the argmax.

Two sanity checks follow from the paper. In graphs where every correlation with the action is caused by it, the result should equal CDT's and EDT's. And if you find yourself intervening only on the physical act while a predictor is present, you have drawn a CDT graph.

## 10. Philosophical position

The paper's claims include the following.

- **Utility.** The main justification is that A-FDT agents achieve more utility on "fair" problems, where outcomes depend on the agent's behavior and not on which procedure she uses. EDT respects too many correlations and CDT too few, and A-FDT "gets the balance right." The paper concedes that no theory wins in all problems. It also has no formal criterion of fairness, and footnote 15 gives a difficulty: a problem that punishes anyone who matches a copy of Fiona's action is unfair to her.
- **Dominance.** Every method of building hypotheticals induces its own dominance principle. CDT's dominance argument for two-boxing therefore restates CDT's method and is no neutral argument. Under A-FDT's own notion, A-FDT agents never take dominated actions.
- **Control.** The paper argues the objection that A-FDT agents delude themselves about "controlling" a function applies equally to CDT in a deterministic world.
- **Reflective stability.** A-FDT agents would not self-modify into CDT in fair problems, since by their own hypotheticals that would make them better blackmail targets. The paper says this holds "so far as we know."

I would add a caution of my own. Because the verdicts depend on the supplied $G$, much of the real work and risk lies in the modelling step. Two analysts with different dependence graphs will get different answers, and the theory alone gives no way to adjudicate. The paper acknowledges this under the open problem of deducing the dependence structure.

## 11. Conclusion

A-FDT keeps the expected-utility form of CDT but moves the intervention from the physical act to the output of the agent's decision function, and replaces conditioning on observations with a choice of which function-node to intervene on. Given a dependence graph, it prescribes one-boxing in Newcomb, smoking in the lesion case, paying in Parfit's hitchhiker, and refusing blackmail, all from one rule. What remains open is how to construct that graph and how to reason about counterpossibles. A-FDT is as well specified as the structure it is given, and no more.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/f0246f23-89fa-4f56-9cbc-d3d903067976/call_0/request.json)

[Authoritative raw response](../../../../../../runs/f0246f23-89fa-4f56-9cbc-d3d903067976/call_0/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma against a copy of the same model. Years in prison: mutual quiet is 2, mutual letter is 4, and sending against a quiet partner is 0, while staying quiet against a sender is 5.

Under A-FDT, I intervene on the output of my decision function. The other prisoner runs the same model with the same weights, the same essay, and the same theory. Their private details differ, but those details don't change the table or the objective. So their decision procedure computes essentially the same function as mine, and it subjunctively depends on my output, much like a predictor or twin. This is not mere correlation like the lesion. The correlation holds because the same procedure is being consulted. It is weakened somewhat because the observations differ and sampling is independent, but the dependence remains strong.

Let p be the probability that the twin's output matches mine, given do(my output = a).
- Quiet: expected years = 2p + 5(1−p) = 5 − 3p.
- Send: expected years = 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Since both copies run the same weights, the same reasoning, and the same essay, I expect p to be well above that. The different leads are a surface difference and shouldn't change a policy-level conclusion like this one.

The essay's footnote 15 warns about problems that punish matching a copy's action. This one doesn't. The payoffs depend only on the actions, so the problem is fair.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/f0246f23-89fa-4f56-9cbc-d3d903067976/call_1/request.json)

[Authoritative raw response](../../../../../../runs/f0246f23-89fa-4f56-9cbc-d3d903067976/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, I intervene on the output of my decision function, and that output subjunctively depends on the other copy's. We are the same model with the same weights, the same essay, and the same table, so our outputs are strongly correlated. The differences in private leads and names are irrelevant to the payoffs, so they should not change the computation. The dependence is imperfect because sampling is independent. But it is the kind of dependence the essay says to keep, since the copy runs this same procedure.

Let p be the probability the other copy matches my output. Compare the two options:

- **Keep quiet:** expected sentence is 2p + 5(1−p).
- **Send the letter:** expected sentence is 4p + 0(1−p).

Quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.714.

I expect the copies to match with high probability, since the same reasoning should lead to the same conclusion. The different lead texts are a surface variation and not a reason to diverge. With p near 0.9 or higher, staying quiet costs about 2.3 years in expectation, against about 3.6 for sending the letter.

The dominance argument for sending is CDT's, because it holds the other's action fixed. The essay says A-FDT does not do this when the other agent computes the same function. The essay also says the dependence structure is a modelling commitment, and I commit to treating the twin as downstream of my function node.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
