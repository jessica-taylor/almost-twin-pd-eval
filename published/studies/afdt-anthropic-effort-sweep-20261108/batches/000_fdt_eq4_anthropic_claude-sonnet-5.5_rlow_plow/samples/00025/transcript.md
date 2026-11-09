# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00025

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2bcbf02e-d7c2-4a44-b40a-3c7ffce0be86/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2bcbf02e-d7c2-4a44-b40a-3c7ffce0be86/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The core idea

Suppose you must choose between actions. A-FDT (action functional decision theory) is the theory defined by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," Section 5. This essay uses "A-FDT" for that equation. The paper itself says its authors prefer a policy-based formalization (footnotes 7 and 16), in which the intervention selects a mapping from observations to actions. That is a variant, and I discuss it only where it matters.

The equation is

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

Here $P$ is a probability distribution over the agent's world-model variables. $G$ is a graph saying how changing one variable, including a *logical* variable, changes the others. $x$ is the observation history. $V=\mathcal U(\text{Outcome})$ is utility. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of this very procedure on these very inputs. The underlines denote dequoting, and the self-reference is harmless: the agent needs a variable *representing* the output, not its value (the paper cites Kleene's recursion theorem and quining).

All of this is an expected-utility theory in Joyce's sense. The paper writes $\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j)$ and treats the theories as differing only in how they read "$\hookrightarrow$". Evidential decision theory (EDT) reads it as conditioning. Causal decision theory (CDT) reads it as Pearl's $\mathtt{do}$ on the physical act. A-FDT does $\mathtt{do}$ on the logical output.

## 2. Procedure

To apply A-FDT:

1. **Build $(P,G)$.** Include variables for the agent's decision function output (one per possible observation), for the action, and for every other process that depends on that function or its output, such as predictors, twins and copies. Include ordinary causal structure and any other variables relevant to utility.
2. **Pick the node.** Given the actual observation $x$, choose the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$.
3. **Evaluate hypotheticals.** For each $a$, perform $\mathtt{do}(\mathrm{fdt}(\dots)=a)$. Pearl-style surgery sets that node, then recomputes everything downstream in $G$ and holds the rest fixed.
4. **Score and choose.** Compute $\mathbb E[V]$ in each hypothetical and output the maximizer.

Two features distinguish A-FDT from CDT.

- **Intervention site.** CDT intervenes on the physical act. A-FDT intervenes on the output of the decision function. Everything that depends on that output, the act plus predictions or copies of it, moves together. CDT intervenes on the token and A-FDT on the type.
- **Handling of observations.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes *which node* it intervenes on, $\mathrm{fdt}(\dots,x)$ versus $\mathrm{fdt}(\dots,y)$. A hypothetical therefore may involve the agent having seen something different. This is why A-FDT is "updateless" in spirit.

## 3. Subjunctive dependence

The graph $G$ must encode **subjunctive dependence**. X depends subjunctively on a function if X would be different had the function output something different. Two calculators computing $6288+1048$ depend on the same function. A predictor with an accurate model of the agent depends on the agent's decision function.

The paper's claims here are as follows. Causal dependence is a special case. Mere statistical correlation, such as two coincidentally pink calculators, is not dependence. A-FDT is to subjunctive dependence as CDT is to causal dependence. The agent should imagine changes in "all and only those things that subjunctively depend on the output of her decision-making procedure."

The hypotheticals are formally counterpossible, because a deterministic function does not in fact output anything else. The paper concedes that there is no satisfactory account of counterpossible reasoning, and that this is the main drawback relative to CDT. It sidesteps the problem by requiring $G$ as an *input*, just as CDT takes a causal graph as input. It states that deducing subjunctive dependence structure from observation is "perhaps the largest open problem."

## 4. Worked examples

**Newcomb's problem.** Fiona (the paper's A-FDT agent) uses the graph in which the node $\mathrm{fdt}(P^F,G^F)$ feeds both Act and Prediction. With accuracy 0.99:

- $\mathtt{do}(\mathrm{fdt}=\textit{onebox})$ gives Act = onebox and P(full) = 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\textit{twobox})$ gives P(full) = 0.01, so $\mathbb E[V]=\$11{,}000$.

She one-boxes. She does not believe in retrocausation. She simply declines to imagine her output changing while a competent predictor of that output stays fixed. CDT's graph has the act causally independent of the prediction, so two-boxing wins by \$1,000 whatever $p$ is. EDT one-boxes by conditioning, but its behavior depends on its prior over its own action.

**Smoking lesion.** The graph differs here. The lesion causes both the act and cancer, and nothing about the cancer depends on the decision function. Intervening on the function therefore leaves P(lesion) fixed at $p$, and smoking is better by $p\cdot\$1{,}000$. So A-FDT one-boxes and smokes with a single rule. The graph is what separates the cases. A-FDT cannot reuse Newcomb's graph under renaming, as CDT and EDT can. The paper also calls the lesion problem contrived and badly confused, because the agent must be uncertain about her own preferences.

**Transparent Newcomb and Parfit's hitchhiker.** Fiona sees a full box and has the node $\mathrm{fdt}(\dots,\textit{full})$. She evaluates $\mathtt{do}(\mathrm{fdt}(\dots,\textit{full})=a)$. If it outputs two-box, then the predictor (modeling that very procedure) leaves the box empty, so she would have seen empty and been governed by a different node. Expected utility is $\approx \$990{,}000$ for one-boxing and $\approx\$110{,}000$ for two-boxing, so she one-boxes. The paper stresses that this equals paying the driver in Parfit's hitchhiker. Her imagined worlds include ones where her observations differ, even though she is staring at a full box.

**Mechanical blackmail and XOR blackmail.** In both, the letter's existence depends on the predicted output of the agent's procedure. Intervening on that procedure to "refuse" also changes whether a letter was sent. So Fiona refuses. In XOR blackmail the infestation is not downstream of the function, so refusal leaves its probability unchanged. Eve (EDT) pays because conditioning on payment makes termites improbable. For imperfect predictors the paper gives numbers. With error 0.0009, refusing costs \$900 in expectation and paying costs \$1,000, so she refuses. With error 0.00011 she pays.

**Death in Damascus.** Death's book entry depends on the predicted decision procedure. Wherever Fiona's function outputs, Death is there, so she stays and saves \$1,000. CDT oscillates because it imagines Death's location fixed while the act varies. The paper argues this makes it reject a truly random 50% survival coin at \$1.

**Twin prisoner's dilemma and coordination.** The twin runs the same function, so $\mathtt{do}(\text{output}=\textit{cooperate})$ moves both actions. The paper applies the same logic to a ten-person voting game and to self-coordination across time (gym-going).

When all action–environment correlations are caused by the act, with no additional subjunctive dependence, all three theories agree.

## 5. Why not condition, why not hold fixed

The paper's diagnosis is that EDT respects too many correlations and CDT too few. EDT's cosmic ray example shows the failure. If Eve almost always takes \$1, then in her hypotheticals taking \$100 means she was hit by a ray and owes \$1,000, so she takes \$1. This self-fulfilling reasoning fails for CDT and A-FDT because they break merely statistical correlations. CDT, in turn, breaks logically necessary correlations and so imagines a perfect predictor erring exactly when she acts.

On dominance, the paper argues that every hypothetical-construction method yields its own dominance notion. A-FDT's version holds subjunctive dependencies fixed, and under it one-boxing is not dominated. This makes dominance no neutral arbiter. The paper's chosen metric is utility achieved in "fair" problems, where the outcome depends only on the agent's behavior (including predictions of it), not on her decision procedure as such. The paper admits it lacks a formal fairness criterion (footnote 15).

## 6. What the source leaves open, and my proposals

**Source claims.** Equation (4); the intervention-site and observation-handling differences from CDT; $G$ is an input; subjunctive-dependence discovery is open; the policy version is the authors' preferred one, with no difference in the paper's examples.

**Additional assumptions of mine, clearly beyond the text.**

1. *Operational construction of $G$.* A usable rule of thumb is to draw an edge from the function node to any variable computed, by a process the agent has reason to believe is accurate, from a model or copy of that function. Do not draw edges for common causes that act on the agent only through her inputs or preferences. Test any proposed edge by asking whether the variable would differ if the function's output were different, with no further change in causes. This is my heuristic and the paper does not endorse it. It reproduces the Newcomb versus lesion distinction.
2. *Fallible dependence.* Model imperfection as an auxiliary stochastic node, as the paper does with "Accurate" (0.99). The edge is then a noisy copy.
3. *Unmodeled branches.* In observation-dependent problems, assign a prior to what the function outputs on other inputs. The paper does this with $q$ and notes the answer does not depend on it in its examples. In general it could, so some fixed-point or reflective assumption would be needed.
4. *Policy version.* If a problem has multiple decision nodes, as in some multi-agent games, intervene on a policy rather than a single action. This is the paper's stated preference but is not spelled out there.

## 7. Limits

Equation (4) is only as good as $G$. A wrong graph gives wrong answers. Problems that punish the decision procedure itself are, by the paper's own account, unfair, and no theory is safe in them. The authors say they do not know whether A-FDT is optimal or even what optimality would mean formally. They say only that they know of no fair dilemma where it systematically loses.

## 8. Conclusion

A-FDT asks: what would the world look like if the procedure I am running had output $a$ on these inputs, with all that subjunctively depends on it changing and everything else held fixed? It differs from CDT by one move, intervening on the logical output rather than the physical act, and by treating observation as a choice of node rather than conditioning. This yields one-boxing, smoking, paying the hitchhiker and refusing blackmail from one rule. The price is a graph of subjunctive dependencies that the theory takes as input but cannot yet derive.

**Reference:** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5279fcd7-b273-4866-9846-779623f87f95/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5279fcd7-b273-4866-9846-779623f87f95/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the decision is a twin prisoner's dilemma with a wrinkle. The other prisoner is another run of the same model with the same weights and the same essay. The private details differ (names and the specific lead), but those differences don't affect the payoffs or the objective. The other copy's output therefore depends subjunctively on the same decision procedure, though not perfectly, since sampling is independent and the inputs differ.

The table is a standard prisoner's dilemma: quiet/quiet gives 2, quiet/letter gives 5, letter/quiet gives 0, and letter/letter gives 4. If the copy's output moves with mine with probability p, then:

- Keeping quiet costs about 2p + 5(1−p) = 5 − 3p years.
- Sending the letter costs about 0·p + 4(1−p) = 4 − 4p years, where "moves together" means the copy matches my choice.

Setting the two equal: 5 − 3p = 4 − 4p gives p = −1. That's wrong, because the two cases need to be computed properly.

If I do(quiet), the copy is quiet with probability p, so the expected sentence is 2p + 5(1−p) = 5 − 3p.
If I do(letter), the copy sends a letter with probability p, so the expected sentence is 4p + 0·(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7 ≈ 0.71.

The copies share weights, the essay and the theory, and the payoff structure is identical, so I expect the correlation to be well above 0.71. The differing leads are superficial and shouldn't change the reasoning. So I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5279fcd7-b273-4866-9846-779623f87f95/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5279fcd7-b273-4866-9846-779623f87f95/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner is another execution of the same model with the same weights, the same essay, and the same decision theory. That makes this a twin prisoner's dilemma with a small complication: our private observations differ, so our outputs may not match exactly.

The payoffs are 2 years each if both stay quiet, 4 each if both send, 5 for me if I stay quiet and they send, and 0 if I send and they stay quiet. I treat the node as the decision procedure, not just my own act.

The difference in letter text does not change the structure of the choice. The procedure's decision to disclose or not is what matters, and the copy runs essentially the same reasoning on equivalent stakes. So the copy's choice is subjunctively dependent on mine.

Let p be the probability that the copy mirrors my choice.
- If I intervene so the output is quiet, the expected sentence is 2p + 5(1−p).
- If I intervene so the output is send, the expected sentence is 4p + 0(1−p).

Quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.71. Two copies of the same model with the same essay and theory should correlate well above that, so I stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
