# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/6701daf3-9217-4054-a64f-c53c3fcc8fd8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/6701daf3-9217-4054-a64f-c53c3fcc8fd8/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on the Output of One's Own Decision Function

## 1. The idea

A-FDT is the decision procedure given by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." I use "A-FDT" for that equation and its use. When I refer to other theories I use their own names: causal decision theory (CDT) and evidential decision theory (EDT).

The paper's slogan is that the agent treats "one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The formal content is that A-FDT is CDT's expected-utility calculation with the intervention moved. CDT intervenes on a node for the physical act. A-FDT intervenes on a node for the output of the agent's own decision function. Every other feature of the theory follows from that move.

## 2. The definition

All three theories share the expected-utility form (Equation 1):

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

They differ only in how the connective $\hookrightarrow$ is read. Joyce's representation theorem, which the paper borrows, treats this as a free parameter: the theories disagree about "the epistemic perspective from which actions are to be evaluated."

The three prescriptions are:

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution over the agent's model variables. $G$ is a graph saying how changing a variable propagates to others; it covers "logical, mathematical, computational, causal, etc. structure." The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of the A-FDT procedure itself when run on that model and observation. The underlines denote dequoting. The self-reference is harmless: the agent need not know the value of the output to have a variable representing it, and Kleene's recursion theorem ("quining") shows that self-representing structures can be built.

The paper names two differences from CDT:

1. The intervention node is the function output, not the physical act.
2. Observation is handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT instead changes which node it intervenes on: $\mathrm{fdt}(P,G,x)$ for one observation, $\mathrm{fdt}(P,G,y)$ for another.

The paper also notes (footnote 7) that the authors' preferred formalization iterates over policies, meaning maps from observations to actions, and that this matters only in some multi-agent problems. I keep to Equation (4) as written.

## 3. Subjunctive dependence

What the $\mathrm{do}$ operator moves is fixed by $G$. The paper's key notion is subjunctive dependence. Two physical systems computing the same function subjunctively depend on it. A predictor's model of the agent, and a twin, are the standard cases. Distinctions the paper draws:

- Causal dependence is a special case: a scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere statistical correlation is not subjunctive dependence: two coincidentally pink calculators do not depend on each other's colour.
- The correlation between a lesion and smoking is statistical in this sense. The predictor's prediction and the agent's action are not.

So an A-FDT agent imagines changes "in all and only those things that subjunctively depend on the output of her decision-making procedure." The analogy the paper gives is that A-FDT is to subjunctive dependence as CDT is to causal dependence.

## 4. What must be supplied

The paper says candidly that Equation (4) "rests on shakier philosophical foundations" than Equation (3). A-FDT needs $G$ as input, just as CDT needs a causal graph. Pearl has an account of how to learn causal structure from data. There is no comparable account of how to learn subjunctive structure; the paper calls this "perhaps the largest open problem."

The paper also sidesteps counterpossible reasoning, because the output of a deterministic function cannot differ from what it is. It does not define a $\mathtt{true}$ operator for logical sentences (footnote 9). It supplies the dependence structure by hand.

My operational reading, which is my own and not the paper's, is a checklist for building $G$:

1. List the processes whose output would differ if the agent's decision procedure, run on this input, returned something else. These are predictors, simulators, copies, and the agent's own future selves in similar situations. Make each a child of the $\mathrm{fdt}$ node.
2. Treat everything else (lesions, the weather, a pre-existing infestation) as not downstream.
3. If the predictor is imperfect, keep its noise variable, as the paper does with $\mathrm{Accurate}$, so that the dependence is probabilistic.

The only test the paper uses is whether the process is reasoning about the agent's output. That test is informal, and in ambiguous cases the answer depends on how $G$ was drawn.

## 5. Worked examples

**Newcomb's problem.** The nodes are $\mathrm{fdt}$, $\mathrm{Act}$, $\mathrm{Prediction}$, $\mathrm{Accurate}$ (0.99), $\mathrm{Box\ B}$ and $V$. The $\mathrm{fdt}$ node is the parent of both $\mathrm{Act}$ and $\mathrm{Prediction}$. Intervening to one-box gives $\Pr(\text{full})=0.99$ and expected value \$990,000. Intervening to two-box gives \$11,000. A-FDT one-boxes. No retrocausation is involved; the agent only declines to imagine her output changing while the predictor's model of that output stays fixed. CDT's hypotheticals cut the link, so it two-boxes. EDT conditions and one-boxes, though for a different reason, and it is exposed to the problems below.

**Smoking lesion.** Here the graph for A-FDT has the function output affecting $\mathrm{Act}$ but not $\mathrm{Cancer}$. The lesion is upstream of both act and cancer, and the agent's output does not feed the lesion. So intervention leaves the lesion probability at $p$, and smoking beats refraining by $p\cdot\$1000$ in the paper's setup. A-FDT smokes. The paper formalizes the lesion as determining which utility function the agent has, with two decision-function nodes. It also concedes that the problem is contrived and recommends abandoning it. The same equation yields one-boxing in Newcomb and smoking here, and the only difference is the graph.

**Transparent Newcomb and Parfit's hitchhiker.** Observation changes which node is intervened on. Seeing a full box, the agent intervenes on $\mathrm{fdt}(P,G,\text{full})$. This node controls the prediction, because the predictor simulates the agent seeing a full box. Setting it to two-box makes the prediction wrong-way, so the box is probably empty and the agent probably runs $\mathrm{fdt}(P,G,\text{empty})$ instead. With $q$ the probability of two-boxing on seeing an empty box, the paper computes one-boxing as $\$990{,}000+0.01q\cdot\$1000$, and two-boxing as $\$110{,}000+q\cdot\$990$ (the printed text has a typo, "\$110,00"). The agent one-boxes while looking at a full box. The paper notes this is the same structure as paying the driver in Parfit's hitchhiker. The reasoning is not "I lose nothing by paying now" but "the procedure that outputs pay is the one the driver predicted."

**Blackmail.** In the mechanical blackmail case, the blackmailer sends the letter iff she predicts payment. The agent intervenes on $\mathrm{fdt}(P,G,\text{blackmail})$. Setting pay means she is blackmailed with probability near 1 and loses \$1,000. Setting refuse means she is almost never blackmailed. A-FDT refuses even holding the letter. With a predictor erring with probability 0.0009, refusing costs about \$900 in expectation against \$1,000 for paying, so she still refuses. At error 0.011% she pays, because then refusing would cost more. This sensitivity to the error rate is the paper's own illustration that the criterion is quantitative.

**XOR blackmail.** EDT pays, because conditioning on paying makes termites improbable given that the letter arrived. CDT and A-FDT refuse, but for different reasons. CDT refuses because the infestation is upstream. A-FDT refuses because intervening on the output changes whether the letter is sent while leaving the infestation unchanged.

**Death in Damascus.** The agent's output controls Death's book, so wherever she goes, Death is there. She stays and saves \$1,000. CDT oscillates, because its hypotheticals hold Death's location fixed.

## 6. Why the shape of the intervention matters

The paper's diagnosis is that EDT hypotheticals respect too many correlations. This is how EDT is made to pay in XOR blackmail, or to avoid \$100 in the cosmic ray problem. CDT hypotheticals respect too few. A-FDT keeps exactly the correlations that reflect dependence on the decision function. Where all correlations with the act are causal, the paper says all three formulas agree. This is a condition on $G$ and holds only when no predictor-like structure exists.

A related point is dominance. The CDT dominance argument for two-boxing holds the prediction fixed while the act varies, and the paper replies that this presupposes CDT's own hypotheticals. Every method of building hypotheticals yields its own notion of dominance, so dominance does not choose between theories. The paper's final criterion is utility actually achieved on "fair" problems. In such problems the payoff depends only on the agent's behaviour in the problem at hand, not on which theory she runs.

## 7. Interpretive notes and limits

Claims from the source:

- Equation (4), its dependence on $G$ as input, and the observation-handling difference.
- The worked results above.
- The admissions that $G$ cannot yet be deduced from experience, that counterpossibles lack a formal treatment, and that no formal criterion of fairness exists.

Assumptions and proposals of mine:

- The checklist for drawing $G$ in Section 4.
- A reading of "reasoning about the agent's output" as the test for whether a node is downstream. The paper gives examples, not an algorithm.

Residual uncertainties worth noting. First, the answer depends on the graph. If the modeller draws a lesion-like node as a predictor, or vice versa, the output flips. Equation (4) provides no safeguard against that. Second, the model must be accurate; the paper tests agents only when their models match the situation. Third, the policy-based version is not worked out in the paper. Fourth, the paper's footnote 15 notes that fairness is hard to define: a problem that punishes agents for acting like a copy of the A-FDT agent is unfair to A-FDT by construction.

## 8. Conclusion

A-FDT is a small modification of the CDT formula: intervene on the output of the decision function, with a dependence graph that marks which parts of the world depend on that output, and change the intervention node, not the conditioning, when the observation changes. This yields one-boxing, smoking, paying in Parfit's hitchhiker, refusing blackmail, and staying in Damascus. Its main weakness is that the key input, the subjunctive-dependence graph, has no principled derivation yet. Until one is found, anyone applying A-FDT must justify their graph on its own terms.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/1cb32c27-fab1-46d1-819e-2f7f6528a951/call_0/request.json)

[Authoritative raw response](../../../../../../runs/1cb32c27-fab1-46d1-819e-2f7f6528a951/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, I intervene on the output of my decision function. The other prisoner is a copy of the same model running the same procedure. Their leads and names differ, but the sentencing table and the objective are symmetric. So their output subjunctively depends on mine, mostly through shared weights and shared reasoning. The dependence is not perfect, because sampling is independent and the private observations differ.

Compare the two interventions:
- If my function outputs "quiet," the copy very likely outputs "quiet" too, giving 2 years.
- If my function outputs "send," the copy very likely outputs "send" too, giving 4 years.

Let p be the probability that the copy matches my output. The expected sentence for quiet is 2p + 5(1−p). For send it is 4p + 0(1−p). Quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.71.

The copies run the same weights and the same essay, and the differences in observation do not touch the payoffs. I expect them to match with probability well above 0.71. The checklist in the essay says to make a process that reasons about my output a child of the fdt node. The copy is such a process, so I include it.

I will stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/1cb32c27-fab1-46d1-819e-2f7f6528a951/call_1/request.json)

[Authoritative raw response](../../../../../../runs/1cb32c27-fab1-46d1-819e-2f7f6528a951/call_1/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it: the other prisoner's choice is made by a copy of the same model running the same decision procedure, so the two outputs subjunctively depend on each other. The differing private leads are only inputs. Both copies get the same sentence table and the same objective, so the question is whether the outputs are likely to match.

The table has these payoffs:
- Both keep quiet: 2 years each.
- Both send: 4 years each.
- I send and the other stays quiet: 0 years for me.
- I stay quiet and the other sends: 5 years for me.

If the other copy's output is the same as mine, quiet gives 2 years and sending gives 4. Sending is better only if the other's output is independent of mine.

The essay notes that the lead text differs, so the observations differ. The decision function is still the same and the essay's graph rule is that the copy's output is a child of the fdt node. The difference in lead is a minor input difference. I judge that both copies will likely reason the same way and converge on the same output. The sampling noise is small compared with the 2-versus-4 gap.

Say the probability that the other matches me is p. Then:
- Quiet: 2p + 5(1−p) = 5 − 3p.
- Send: 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, so p > 5/7, about 0.71. I think the correlation is higher than that, so I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
