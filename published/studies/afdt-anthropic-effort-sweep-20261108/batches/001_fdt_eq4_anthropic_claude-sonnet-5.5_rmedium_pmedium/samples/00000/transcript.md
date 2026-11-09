# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6d1a3c78-ec88-4907-a2ab-c2bf294190cb/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6d1a3c78-ec88-4907-a2ab-c2bf294190cb/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision theory that Yudkowsky and Soares (2017) call "functional decision theory" and formalize in Equation (4) of their Section 5. This essay uses the name A-FDT for that procedure. I take it to be an expected-utility rule in which the agent evaluates each candidate action by asking what the world would look like if *her decision function itself* returned that action. It does not ask what would follow from her body performing the action. In the paper's words, the agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

I separate three things below: what the source states, what is a reasonable operational reading, and what I add myself. The source is explicit that some of the machinery is missing.

## 2. The formal definition

All of the paper's theories maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is a connective for "decision hypotheticals". Following Joyce, the theories differ only in their "epistemic perspective", meaning how they interpret $\hookrightarrow$. EDT conditionalizes. CDT, in Pearl's graphical version, uses $\mathtt{do}(\mathrm{Act}=a)$ on a causal graph. A-FDT, Equation (4), is:

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\Big(V\;\Big|\;\mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- $P$, a probability distribution over the agent's world-model variables. These include variables for outputs of mathematical functions, so $P$ has a variable for $6288+1048$ with nearly all its mass on $7336$.
- $G$, a graph that records how changing a *logical* variable propagates to other variables. It encodes causal structure, and also logical, computational, and other subjunctive structure.
- $x$, the observation history.
- $V=\mathcal U(\mathrm{Outcome})$.

The underlines denote dequoting. $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a *node* in the model that represents the output of the very algorithm being run, on these very inputs. This is self-referential. The source says the reference is harmless, because the agent does not need to know the node's value to have a variable representing it, and Kleene's second recursion theorem ("quining") shows such self-representing structures can be built.

The source names two differences from CDT:

1. CDT intervenes on a node for the physical action. A-FDT intervenes on the node for the decision function's output.
2. CDT responds to observations by conditioning. A-FDT responds by *changing which node it intervenes on*, from $\mathrm{fdt}(\ldots,x)$ to $\mathrm{fdt}(\ldots,y)$.

Footnotes 7 and 16 add that the authors' preferred formalization iterates over *policies*, which are maps from observations to actions. They say this makes a difference only in some multi-agent problems and ignore it in the paper. Equation (4) as written is the action version, which is what I describe.

## 3. Subjunctive dependence and the role of $G$

A-FDT's hypotheticals preserve exactly the "subjunctive dependencies" on the decision function. A variable depends subjunctively on the function if it would be different had the function output something different. This covers:

- Causal descendants. Causal dependence is a special case, since a scribe copying a calculator depends on it both causally and subjunctively.
- Twins, which run the same function.
- Predictors, which contain an accurate representation of the function. The source's picture is a "twin" inside the predictor's mind.

Mere statistical correlation does not count. Two calculators that happen to both be pink are not dependent, because if one had been green the other would still be pink. So A-FDT breaks lesion-type correlations (as CDT does) and keeps predictor-type correlations (as EDT does). The source summarizes: "EDT respects too many action-environment correlations, while CDT respects too few."

The surgery is by $\mathtt{do}$ on a logical variable, so it is a counterpossible: the function cannot in fact return another value, "any more than there are possible worlds where $6288+1048\neq7336$." The source does not claim a theory of counterpossibles. It defines a $\mathtt{true}(\cdot)$ operator, concedes that "it's not clear how to define" it, and sidesteps the problem by requiring $G$ as an *input*, in the way CDT takes a causal graph as input.

## 4. Applying the procedure

Here is a recipe. The first three steps follow the source's worked examples. The fourth is my summary.

1. Model the problem as a stochastic or deterministic network. Include a node for each relevant instance of $\mathrm{fdt}(P,G,\cdot)$.
2. Wire the graph so that everything that runs or models the function (the action, predictors, twins) is a child of the relevant fdt node. Variables only statistically correlated with the agent are *not* children.
3. For each action $a$, set the fdt node (the one matching the actual observation) to $a$, propagate, and compute $\mathbb E[V]$.
4. Output the best $a$.

### Newcomb's problem

With a 99% accurate predictor, the nodes Act and Prediction both descend from $\mathrm{fdt}(P,G)$. Setting it to one-box gives $0.99\cdot\$1{,}000{,}000=\$990{,}000$. Setting it to two-box gives $0.01\cdot\$1{,}000{,}000+\$1{,}000=\$11{,}000$. So A-FDT one-boxes. No retrocausation is involved. The agent just declines to imagine the action changing while the predictor's model of that very function stays fixed. Her reasoning "doesn't change" if she is already near-certain of her own output, because the hypothetical is built by intervention rather than conditioning. A high prior on one-boxing does not make two-boxing look good.

### Smoking lesion

Here the lesion is not a descendant of the function. The graph has Lesion as a parent of Act and Cancer, with the fdt node feeding only Act. The source adds a further wrinkle. The lesion determines the agent's utility function, so there are two possible functions, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, and Lesion selects which one controls Act. Intervening on the relevant node leaves $P(\text{lesion})=p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes. The *same* rule gives opposite answers in the two problems because $G$ differs. The source also admits the problem is contrived and "badly confused."

### Transparent Newcomb and Parfit's hitchhiker

With observation $x=\textit{full}$, A-FDT intervenes on $\mathrm{fdt}(P,G,\textit{full})$. That node feeds the predictor, because the predictor simulates the agent seeing a full box, and it also feeds Act when the box is full. Setting it to one-box yields $\$990{,}000+0.01q\cdot\$1{,}000$, where $q$ is the credence that she two-boxes on seeing an empty box. Setting it to two-box yields about $\$11{,}000+q\cdot\$990$. So A-FDT one-boxes even looking at a full box. When she imagines two-boxing, she imagines a world where she is probably looking at an empty box. This is exactly equivalent to paying in Parfit's hitchhiker. The source defends it by three arguments (precommitment, non-negative value of information, and utility achieved), and says the third gives the first two their teeth.

### Blackmail

In the XOR blackmail and the mechanical blackmail, the letter node is downstream of $\mathrm{fdt}(\ldots,\textit{letter})$ through the blackmailer's prediction, but Infestation is not. A-FDT refuses to pay in XOR blackmail because refusing does not change whether she has termites. In mechanical blackmail, refusing corresponds to a world in which she is probably never blackmailed. The source works a fallible case. If the blackmailer wrongly predicts "pay" with probability $0.0009$, then paying costs \$1,000 for certain and refusing costs about \$900 in expectation, so she refuses even while holding a letter she knows came from an erroneous prediction. At error $0.011\%$, she pays.

### Death in Damascus

Death's location descends from the function through the predicted-and-written appointment book. So whatever the output, Death is there. The only difference is the \$1,000 flight cost, and A-FDT stays. This avoids CDT's instability.

### Coordination examples

The source also sketches, without derivations:

- **Voting.** Ten agents who each pay \$1,000 to vote are rewarded only if all do. A-FDT agents treat each other's decisions as not subjunctively independent.
- **Gym attendance.** A-FDT treats this week's and next week's decisions as instances of one function.

## 5. What the source leaves open, and how I read it

**(a) How to obtain $G$.** The source says this is "perhaps the largest open problem" and that it is unclear whether it can be done in Pearl's framework. A reader must supply $G$ by hand, justified by the problem description: a predictor with a model of the agent is a descendant, and a lesion is not.

My operational suggestion, which is my own proposal and not the paper's, is to test each variable $Z$ with the question "Does $Z$ reliably track what this algorithm returns, because $Z$ is computed from the algorithm or a faithful model of it?" Only variables passing that test become children of the fdt node. The test is itself a judgment about the world, so it carries uncertainty. Partial reliability should be represented as stochastic edges, as with the 99% predictor.

**(b) Which node to intervene on.** When the agent's observations differ across branches, it matters which instance of the function is "this very one". The paper handles this by indexing the node by $x$ and having the graph's variables select among instances. In the blackmail graphs, the Blackmailer node decides whether $\mathrm{fdt}(\ldots,\textit{letter})$ or $\mathrm{fdt}(\ldots,\emptyset)$ controls Act. I recommend always drawing one node per possible observation value and treating the expected-utility sum as taken over the whole graph, with the intervened node fixed. This is only an interpretation of the examples.

**(c) Self-ignorance.** In the examples, the agent may assign arbitrary credence ($q$) to what other instances of her function would do. The computed decisions do not depend on it. I treat this as a robustness check one should verify in new problems. If the answer does depend on such credences, the model is under-specified.

**(d) Actions versus policies.** Equation (4) maximizes over actions, but the authors prefer policies, noting they differ only in multi-agent dilemmas. For a single-agent problem with observation-dependent predictors, the action version evaluated at each observation reproduced the paper's results.

**(e) Fairness.** The source claims A-FDT does best in "fair" problems, where outcomes depend on the agent's behavior and not on which algorithm produces it. Newcomb's predictor "punishes two-boxers", not CDT. The source acknowledges it has no formal definition of fairness and notes obstacles (footnote 15: a problem that punishes anyone who copies A-FDT's action is unfair to A-FDT in a way that has no obvious analogue for others). No theory can win everywhere.

## 6. Dominance and delusion

A CDT-style dominance argument says two-boxing is better whatever the box contains. The source replies that this uses CDT's counterfactual, holding the prediction fixed while the action varies. That is like imagining a calculator outputting 3159 while holding $6288+1048=7336$ fixed. Every method of constructing hypotheticals induces its own dominance relation. Conditional dominance makes refusing to smoke "dominate", and A-FDT's own dominance, which holds subjunctive dependencies fixed, never selects a dominated action. So dominance cannot adjudicate between theories, and the source falls back on expected utility achieved.

To the charge that A-FDT agents believe they control mathematical facts, the source replies that a deterministic CDT agent also imagines worlds where her token action differs. Any objection to "controlling" the type would equally block controlling the token.

## 7. Where A-FDT agrees with the others

In models where every action-correlated variable is caused by the action, with only the fdt node as a possible subjunctive cause, the paper shows $\mathbb E[V|a]=\mathbb E[V|\mathtt{do}(a)]=\mathbb E[V|\mathtt{do}(\mathrm{fdt}=a)]$, so the three theories agree. They split only when something correlates with the action without being caused by it, as with predictors, twins, and blackmailers. A diagnostic habit follows. In an unfamiliar case, first ask whether any predictor or copy of the agent is present. If not, ordinary causal reasoning suffices.

## 8. Limitations and my own caveats

- The theory is only as good as its input graph, and the paper provides no principled procedure for producing it. Any claim that A-FDT "prescribes X" is conditional on a choice of $G$.
- Counterpossible surgery is treated as a modeling operation. The paper takes the computation to be a tool and does not claim a metaphysics of it.
- Idealized models are small. The paper notes that real models, with a variable for every belief, would make Equation (4) intractable, and argues that bounded approximations would show analogous strengths and weaknesses. That is a hope and not a proof.
- Some prescriptions, such as one-boxing while looking at two full boxes or refusing to pay a letter already in hand, will strike readers as odd. The source's answer is that the policy-level view, in which one asks what kind of agent gets blackmailed, is correct. It also claims A-FDT is reflectively stable in fair problems, which is a claim of the paper and not something I have verified.

## 9. Conclusion

A-FDT keeps expected-utility maximization and changes only how hypotheticals are built. It intervenes on a node representing the output of its own decision function, and lets everything that depends subjunctively on that output (predictors, copies, and downstream causal effects) change with it, while leaving mere statistical correlates alone. This one rule gives one-boxing in Newcomb's problem, smoking in the lesion problem, paying in Parfit's hitchhiker, refusing blackmail, and staying in Damascus. The cost is its dependence on a subjunctive-dependence graph that nobody yet knows how to derive from observation. Until that problem is solved, applying A-FDT means making an explicit, defensible modeling judgment about what depends on what, and then computing carefully.

**Reference:** Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4f586838-7c38-4e3b-af31-3510d68ce69a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4f586838-7c38-4e3b-af31-3510d68ce69a/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner is a near-twin running the same model with the same essay, so the two decision functions are strongly subjunctively dependent. The differences in private leads (names, letter text) don't change the sentencing table or the objective, so the outputs should track each other closely.

Comparing the symmetric outcomes under that dependence:
- Both keep quiet: 2 years each.
- Both send: 4 years each.

If the dependence were perfect, quiet beats sending. The question is how reliable it is. Let p be the probability the other copy matches my output, and treat the match as the same fdt node.

- Quiet: p·2 + (1−p)·5
- Send: p·4 + (1−p)·0

Quiet is better when 2p + 5 − 5p < 4p, i.e. 5 < 7p, so p > 5/7 ≈ 0.714.

Both copies use the same weights, the same essay and the same reasoning, and the differences are stipulated to be irrelevant to the payoffs. I expect them to converge with probability well above 0.71, since the essay explicitly treats twins as subjunctively dependent and points to cooperating in coordination problems. So I intervene on the shared function and choose quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4f586838-7c38-4e3b-af31-3510d68ce69a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4f586838-7c38-4e3b-af31-3510d68ce69a/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner's choice depends subjunctively on my decision function only to the extent that the two of us run the same function. The twin case here is an imperfect one. We are the same model with the same weights and the same essay, but our private observations differ, and independent sampling is possible. Even so, the central decision procedure is almost certainly the same, so the outputs should be highly correlated.

Let p be the probability that the other copy's output matches mine when I intervene on the function.

- If I keep quiet: 2p + 5(1−p) = 5 − 3p.
- If I send the letter: 0·p + 4(1−p) = 4 − 4p.

Sending is better when 4 − 4p < 5 − 3p, which holds for every p > −1, so it always wins. Matching therefore cannot favor quiet, because mutual defection (4 years) is worse than mutual cooperation (2 years) only if the other copy's action is held to match mine. I need to recheck that.

The correct calculation treats the other copy's action as matching mine with probability p, and otherwise as the opposite action.

- Quiet: with probability p the other is quiet (2 years), otherwise they send (5 years). Expected years = 2p + 5(1−p).
- Send: with probability p the other sends (4 years), otherwise they are quiet (0 years). Expected years = 4p + 0·(1−p).

I had the send case wrong above. Redoing the comparison:

- Quiet: 5 − 3p.
- Send: 4p.

Quiet is better when 5 − 3p < 4p, which gives p > 5/7 ≈ 0.714.

The copies share weights, the essay, and the decision theory, and they differ only in surface details that do not affect the payoffs. The correlation is plausibly well above 0.71, and A-FDT treats the twin as a child of the same function node. So I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
