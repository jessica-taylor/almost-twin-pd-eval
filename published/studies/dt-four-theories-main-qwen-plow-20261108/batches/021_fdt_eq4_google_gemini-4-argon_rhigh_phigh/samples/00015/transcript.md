# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00015

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/06da2d56-75c2-4b92-ba79-a363a187283e/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/06da2d56-75c2-4b92-ba79-a363a187283e/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Choosing the Output of a Mathematical Function: A Formal Guide to Action Functional Decision Theory (A-FDT)

## 1. Introduction: The Dilemma of Instrumental Rationality

For decades, the foundations of rational choice have been divided between two standard theories of instrumental rationality: **evidential decision theory (EDT)** and **causal decision theory (CDT)**. Both theories endorse expected utility maximization, yet they frequently prescribe incompatible actions and suffer from systematic, predictable failures in well-known decision problems.

Measured by average utility achieved over time, EDT outperforms CDT in dilemmas involving accurate predictors or replicas—such as Newcomb's problem (Nozick, 1969) and the psychological twin prisoner's dilemma (Lewis, 1979)—where EDT agents walk away rich while CDT agents defect or two-box into poverty. Conversely, CDT outperforms EDT in dilemmas involving common causes—such as Skyrms's (1980) smoking lesion problem or Soares and Fallenstein's (2015) XOR blackmail—where EDT agents pay a price to "manage the news" (Lewis, 1981), avoiding actions that are merely statistical symptoms of bad outcomes. Even worse, in sequential prediction dilemmas such as Parfit's hitchhiker problem (Parfit, 1986) and Drescher's (2006) transparent Newcomb problem, *both* CDT and EDT fail to secure the high-utility outcome unless granted advance opportunities to pay for binding precommitments.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"*, Eliezer Yudkowsky and Nate Soares propose a unified resolution to these paradoxes. Their central thesis is that rational agency should not be framed around selecting an isolated physical act token (as in CDT) or conditioning on the auspiciousness of one's behavior (as in EDT). Instead, a rational decision-maker should treat her choice as the output of a fixed mathematical decision function that asks: *"Which output of this very function would yield the best outcome?"*

While the authors note in footnotes that their broader framework can be formulated so that agents iterate over full *policies* (which we may call **policy functional decision theory**, or **P-FDT**), the primary formalization developed and analyzed in Section 5 of their paper—specifically **Equation (4)**—evaluates individual *actions* given a specific world-model and observation history. In this essay, we examine **action functional decision theory (A-FDT)** as defined by Equation (4). We will unpack its formal mathematical machinery, explain how it models counterfactuals via *subjunctive dependence*, demonstrate step-by-step how to apply **A-FDT** to both canonical and unfamiliar decision problems, and develop operational extensions for the implementation questions that the source paper leaves open.

---

## 2. The Formal Architecture of A-FDT

### Expected Utility and Decision Hypotheticals

Following the representation theorem of Joyce (1999), **EDT**, **CDT**, and **A-FDT** are all expected utility theories. As Joyce observes, *"decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."* 

Formally, consider an agent choosing an action $a$ from a finite set $\mathcal{A}$ after receiving an observation history $x$ from a countable set $\mathcal{X}$. Let $\mathcal{O} = \{o_1, o_2, \dots\}$ be a countable set of outcomes and $\mathcal{U} : \mathcal{O} \to \mathbb{R}$ be a suitably bounded utility function. Drawing from Gibbard and Harper (1978), Yudkowsky and Soares state the general principle of expected utility maximization in **Equation (1)**:

$$\mathcal{EU}(a) \coloneqq \sum_{j=1}^N P(a \hookrightarrow o_j ;\, x) \cdot \mathcal{U}(o_j), \tag{1}$$

where $P(a \hookrightarrow o_j ;\, x)$ denotes the subjective probability that outcome $o_j$ will obtain in the hypothetical scenario where action $a$ is executed after observing $x$.

To operationalize Equation (1), an agent maintains a world-model $M$ and, for each candidate action $a \in \mathcal{A}$, performs a formal operation on $M$ to construct a transient computational object $M^{a\hookrightarrow}$—her *hypothetical for $a$*—from which she computes the expected value of utility $\textsc{V} \coloneqq \mathcal{U}(\textsc{Outcome})$. The three theories diverge in what data $M$ must contain and how $M^{a\hookrightarrow}$ is constructed from $M$:

1. **Evidential Decision Theory (EDT)**: The world-model $M$ is simply a Bayesian probability distribution $P$ over random variables including $\textsc{Obs}$ (observation), $\textsc{Act}$ (physical action), and $\textsc{V}$ (utility). The connective $\hookrightarrow$ is interpreted as standard Bayesian conditionalization (**Equation (2)**):
   $$\mathrm{EDT}(P, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \textsc{Obs}=x, \textsc{Act}=a\right), \tag{2}$$
   where actions $a$ with $P(\textsc{Act}=a \mid \textsc{Obs}=x) = 0$ are excluded from consideration.

2. **Causal Decision Theory (CDT)**: Because conditioning confuses symptoms with causes, CDT augments the probability distribution $P$ with a causal graph $G$ (a directed acyclic graph over the variables of $P$ in the sense of Pearl, 1996, 2000). To construct the hypothetical for $a$, the agent updates on $\textsc{Obs}=x$ and applies Pearl's graph-surgery operator $\mathtt{do}(\textsc{Act}=a)$, which severs all incoming edges to the physical action node $\textsc{Act}$, fixes $\textsc{Act}=a$, and propagates changes exclusively to nodes causally downstream of $\textsc{Act}$ (**Equation (3)**):
   $$\mathrm{CDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\right). \tag{3}$$

### Equation (4): The Primary Formal Presentation of A-FDT

Like CDT, **A-FDT** rejects mere conditionalization in favor of structural surgery on a graphical model $(P, G)$. However, instead of intervening on a variable representing a physical act token ($\textsc{Act}$), an **A-FDT** agent intervenes on a variable representing a *logical fact*: the output of her own mathematical decision function when evaluated on her current inputs.

To formalize this, the probability distribution $P$ is extended to include variables representing the outputs of mathematical functions (for instance, a variable for $6288+1048$ that places high probability on $7336$). In an idealized setting, one might wish to define a logical conditioning operator $\mathtt{true}(\phi)$ that updates $P$ on the counterpossible assumption that a logical sentence $\phi$ holds. Because no general formal calculus for $\mathtt{true}(\phi)$ currently exists, Yudkowsky and Soares instead encode the relevant logical, computational, and causal dependencies directly into the directed graph $G$. Re-using Pearl's $\mathtt{do}$ operator on this expanded dependency graph yields **Equation (4)**, the core formal specification of **A-FDT**:

$$\mathrm{FDT}(P, G, x) \coloneqq \argmax_{a \in \mathcal{A}} \mathbb{E}\left(\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a\right)\right). \tag{4}$$

*(Terminological note: Throughout Equation (4) and the source text, the authors denote the decision function by $\mathrm{FDT}$ and its corresponding graph node by $\textsc{fdt}$. To distinguish this action-indexed rule from the policy-indexed variant mentioned in their footnotes, we refer to the theory governed by Equation (4) as **A-FDT**.)*

Let us carefully unpack the mathematical components of Equation (4):

* **Dequoting and Self-Reference ($\underline{P}, \underline{G}, \underline{x}$)**: The underlines denote *dequoting*. If $x \coloneqq 3$, then $\textsc{Z}\underline{x}$ denotes the syntactic variable name $\textsc{Z}3$. Thus, when the **A-FDT** algorithm is run on concrete inputs $(P, G, x)$, it locates inside the graph $G$ the specific node named $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ that represents the output of this very computation. Although this involves self-reference—the model $(P, G)$ contains a variable whose name encodes $(P, G)$—the self-reference is mathematically benign. As proved by Kleene's (1938) second recursion theorem (via "quining"), computational data structures can rigorously contain and manipulate exact representations of their own source code without circularity, and the agent does not need to know the *output value* of $\mathrm{FDT}(P, G, x)$ in advance simply to possess a graph node *representing* that value.
* **The Two Departures from CDT**: Comparing Equation (3) and Equation (4) reveals exactly two formal modifications:
  1. *Type vs. Token Intervention*: CDT intervenes on the physical node $\textsc{Act}$. **A-FDT** intervenes on the functional node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. Both the agent's physical action $\textsc{Act}$ (when she observes $x$) and any external predictor's simulation of her decision (when predicting her response to $x$) are children of $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ in $G$.
  2. *Updateless Response to Observations*: In CDT, receiving observation $x$ triggers a Bayesian update $\mid \textsc{Obs}=x$. In **A-FDT**, Equation (4) contains *no* conditioning on $\textsc{Obs}=x$. Instead, when the agent's observation history changes from $x$ to $y$, **A-FDT** responds by changing *which node in $G$ is intervened upon*—switching from $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) = a)$ to $\mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}, \underline{y}) = a)$.

When all correlations between $\textsc{Act}$ and other variables in $(P, G)$ are caused downstream by $\textsc{Act}$ (apart from $\textsc{Act}$ depending on $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$), **EDT**, **CDT**, and **A-FDT** coincide:
$$\mathbb{E}[\textsc{V} \mid a] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(a)] = \mathbb{E}[\textsc{V} \mid \mathtt{do}(\textsc{fdt}(\underline{P}, \underline{G}) = a)].$$
They diverge precisely when external processes correlate with the agent's action without being *physically caused* by that action.

---

## 3. Subjunctive Dependence, Counterpossibilities, and Dominance

### Subjunctive Dependence and the Type-Token Distinction

Why should an intervention on a decision node alter a predictor's past prediction in a graphical model without invoking retrocausality? Yudkowsky and Soares explain this via **subjunctive dependence**: *"When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."*

Consider two well-functioning electronic calculators on opposite sides of the globe, both tasked with computing $6288 + 1048$. If one outputs $7336$, we infer that the other will also output $7336$ (barring hardware errors or cosmic rays). This correlation does not require a physical signal passing between the calculators, nor does it depend on a shared historical origin; even if human and alien civilizations independently discovered arithmetic, two reliable physical instantiations of the same mathematical function are logically constrained to yield matching outputs.

Causal dependence is a special case of subjunctive dependence (if a Parisian scribe copies a calculator's display, her notes both causally and subjunctively depend on the calculation), whereas accidental statistical correlation is not (if a calculator in Paris and a calculator in Tokyo happen to be painted pink, imagining the Parisian calculator painted green does not change the color of the Tokyo calculator). This yields the central analogy of the source paper:

> *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

In terms of C. S. Peirce's (1934) type-token distinction, CDT intervenes on the *token* ("my physical act at this spacetime location is $a$"), severing its logical tie to other physical tokens of the same computation—such as a twin's decision or a predictor's simulation. **A-FDT** intervenes on the *type* ("the output of the decision function $\mathrm{FDT}$ on input $(P, G, x)$ is $a$"), preserving variations across all physical tokens that instantiate or simulate that function.

### Counterpossibilities and Why the $\mathrm{FDT}'$ Workaround Fails

Because a deterministic mathematical function has a single output of logical necessity, asking *"What if $\mathrm{FDT}(P, G, x)$ output $a_2$ instead of $a_1$?"* requires evaluating a **counterpossible conditional**—a counterfactual whose antecedent is logically impossible (Cohen, 1990).

One might hope to bypass counterpossibilities by defining a variant theory, $\mathrm{FDT}'$, that asks a purely physical counterfactual: *"What if I implemented a different decision function $f_n$ from a candidate set $\mathcal{F}$?"* An $\mathrm{FDT}'$ agent whose actual decision procedure is $d \notin \mathcal{F}$ would iterate over $f_n \in \mathcal{F}$, evaluate how much utility she would get if she physically ran $f_n$, and emulate the best $f_n$. Yet, as Yudkowsky and Soares point out, this saves no trouble in Newcomb's problem: the predictor predicts the agent's *actual* procedure $d$, not $f_n$. For $\mathrm{FDT}'$ to preserve the correlation between her choice and the prediction, she cannot merely imagine replacing $d$ with $f_n$ in her own head; she must imagine a hypothetical world in which predictors of $d$ predict *as if $d$ behaved like $f_n$*—which immediately returns us to evaluating counterpossibilities about the output of $d$.

Thus, **A-FDT** embraces counterpossibilities directly as pragmatic mental tools ("notes on scratch paper") encoded in the graph $G$. Just as a deterministic CDT agent profitably imagines multiple physically impossible actions to choose the best one, an **A-FDT** agent profitably imagines multiple logically impossible outputs of her algorithm to choose the best one.

### Dominance, Dynamic Consistency, and the Value of Information

Causal decision theorists traditionally defend two-boxing in Newcomb's problem by appealing to **dominance**: whether Box B is full or empty, taking both boxes yields \$1,000 more than taking only Box B. **A-FDT** reveals that dominance is not a theory-neutral criterion. Every rule for constructing hypotheticals induces its own dominance principle:
* Under *CDT dominance* (holding fixed all variables not causally downstream of $\textsc{Act}$), two-boxing dominates one-boxing.
* Under *EDT dominance* (conditioning on $\textsc{Act}$), refraining from smoking "dominates" smoking in the smoking lesion problem.
* Under ***A-FDT** dominance* (holding fixed all background variables and subjunctive dependencies while varying $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$), one-boxing dominates two-boxing in Newcomb's problem, and smoking dominates refraining in the smoking lesion problem.

Asking what happens if the agent changes her physical action while holding the predictor's accurate simulation fixed is like asking what a working calculator would display if it output $3159$ while holding fixed that $6288 + 1048 = 7336$.

Furthermore, severing subjunctive dependencies makes CDT dynamically inconsistent and unstable:
1. **Self-Modification and Precommitment**: In Newcomb-like problems, a CDT agent will pay prior to the prediction to precommit or self-modify into an **A-FDT** agent, yet refuses to act accordingly once the prediction is made. **A-FDT** requires no costly precommitment rituals; it already acts as it would have precommitted to act, endorsing its own future use.
2. **Reflective Instability (Death in Damascus)**: When facing Death, who perfectly predicts whether the agent stays in Damascus or flees to Aleppo (at a \$1,000 travel cost), a CDT agent enters an unstable loop: believing he will stay makes fleeing look better, and believing he will flee makes staying look better (Gibbard & Harper, 1978). Even worse, if Carl uses ratification or pseudorandomization (Joyce, 2012), he treats Death's location as independent of his current choice in his CDT hypotheticals, acting *as if* he already has a $\ge 50\%$ chance of survival—and consequently refuses to pay \$1 for a genuinely random quantum coin that would give him a true $50\%$ survival probability! An **A-FDT** agent, by contrast, sees that $\textsc{fdt}(\underline{P^F}, \underline{G^F})$ determines both her destination and Death's appointment book; knowing she will die under either output, she calmly stays in Damascus and saves \$1,000, while gladly paying \$1 for a genuinely unpredictable coin if offered.

---

## 4. Applying A-FDT: Canonical and Unfamiliar Decision Problems

To see how Equation (4) operates as a concrete mathematical algorithm, let us first trace how **A-FDT** resolves the canonical dilemmas from Yudkowsky and Soares, and then work through an unfamiliar decision problem from scratch.

### Template 1: Predictors vs. Common Causes (Newcomb vs. Smoking Lesion)

In **Newcomb's problem**, Box A contains \$1,000 and Box B contains \$1,000,000 ($\mathit{full}$) if and only if a $99\%$-accurate predictor predicted the agent would leave Box A behind ($\mathit{onebox}$), and \$0 ($\mathit{empty}$) otherwise.

For an **A-FDT** agent (Fiona), the dependency graph $G^F$ contains the intervention node $\textsc{fdt}(\underline{P^F}, \underline{G^F})$, an exogenous noise node $\textsc{Accurate}$ with $P^F(\mathit{accurate}) = 0.99$, a node $\textsc{Prediction}$, a node $\textsc{Box B}$, the physical action node $\textsc{Act}$, and utility $\textsc{V}$. The structural edges are:
$$\textsc{fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Act}, \qquad \textsc{fdt}(\underline{P^F}, \underline{G^F}) \to \textsc{Prediction} \leftarrow \textsc{Accurate}, \qquad \textsc{Prediction} \to \textsc{Box B},$$
with $\textsc{Act}$ and $\textsc{Box B}$ determining $\textsc{V}$. Applying Equation (4):
* Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox})$, we have $\textsc{Act} = \mathit{onebox}$ with probability $1$ and $\textsc{Box B} = \mathit{full}$ with probability $0.99$, yielding:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{onebox}\right)\right] = 0.99(\$1,000,000) + 0.01(\$0) = \$990,000.$$
* Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox})$, we have $\textsc{Act} = \mathit{twobox}$ with probability $1$ and $\textsc{Box B} = \mathit{full}$ with probability $0.01$, yielding:
  $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F}, \underline{G^F}) = \mathit{twobox}\right)\right] = 0.01(\$1,001,000) + 0.99(\$1,000) = \$11,000.$$

Because $\$990,000 > \$11,000$, **A-FDT** outputs $\mathit{onebox}$.

Now contrast this with the **smoking lesion problem**: an unobserved arterial lesion ($\textsc{Lesion}$, with prior probability $p \in (0,1)$) causes people both to love smoking (gaining \$1,000 utility from $\mathit{smoke}$) and to develop fatal lung cancer $99\%$ of the time (losing \$1,000,000 survival utility), whereas those without the lesion develop cancer only $1\%$ of the time.

Why doesn't **A-FDT** refrain from smoking like EDT? Because a physiological lesion does not simulate the **A-FDT** algorithm! Yudkowsky and Soares formalize the lesion's effect on desires by specifying two possible utility functions—$\mathcal{U}_S$ (which values smoking at $+\$1,000$) and $\mathcal{U}_R$ (which values smoking at $-\$1$)—inducing two possible distributions $P^F_S$ and $P^F_R$. In Fiona's graph $G^F$, $\textsc{Lesion}$ is an exogenous common cause of $\textsc{Cancer}$ and $\textsc{Act}$, where $\textsc{Act}$ serves as a multiplexer selecting between two function nodes:
$$\textsc{Act}(\mathit{lesion}, s, r) \coloneqq s, \qquad \textsc{Act}(\mathit{nolesion}, s, r) \coloneqq r,$$
with $s = \textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ and $r = \textsc{fdt}(\underline{P^F_R}, \underline{G^F})$. When Fiona has the lesion, she evaluates $\mathrm{FDT}(P^F_S, G^F)$ by intervening on $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$ while holding fixed the exogenous probability $P^F_S(\mathit{lesion}) = p$ and her prior probability $q = P^F_S(\textsc{fdt}(\underline{P^F_R}, \underline{G^F}) = \mathit{smoke})$:
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{smoke}\right)\right] = p(\$10,000 + \$1,000) + (1-p)(\$990,000 + q \cdot \$1,000),$$
$$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}\left(\textsc{fdt}(\underline{P^F_S}, \underline{G^F}) = \mathit{refrain}\right)\right] = p(\$10,000) + (1-p)(\$990,000 + q \cdot \$1,000).$$
Because $\textsc{Lesion}$ has no incoming edge from $\textsc{fdt}(\underline{P^F_S}, \underline{G^F})$, the intervention leaves the probability of cancer untouched at $p$, and smoking strictly dominates refraining by $p \cdot \$1,000 > 0$.

### Template 2: Observation-Gated Prediction (Transparent Newcomb & Blackmail)

The power of Equation (4)'s updateless observation handling becomes unmistakable in the **transparent Newcomb problem** (and its strategic isomorphs, **Parfit's hitchhiker** and **mechanical blackmail**). Here, both boxes are transparent, and the $99\%$-accurate predictor places \$1,000,000 in Box B if and only if she predicts that the agent will one-box *upon observing that Box B is full*.

Suppose the agent walks into the room and sees that Box B is $\mathit{full}$. Both CDT and EDT condition on $\textsc{Obs} = \mathit{full}$: once $\textsc{Box B} = \mathit{full}$ is locked in by conditionalization, two-boxing yields $\$1,001,000$ while one-boxing yields $\$1,000,000$. Consequently, CDT and EDT agents predictably two-box, and the predictor leaves their Box B empty.

How does **A-FDT** evaluate the choice upon observing $x = \mathit{full}$? In Fiona's graph $G^F$, there are two logical nodes corresponding to her two possible observations: $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$. Because the predictor specifically simulates what Fiona will do *if she sees a full box*, the predictor's node $\textsc{Prediction}$ depends on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ and $\textsc{Accurate}$. Meanwhile, Fiona's physical action $\textsc{Act}$ depends on $\textsc{Prediction}$ (which determines what she observes) and the two $\textsc{fdt}$ nodes:
$$\textsc{Act}(\mathit{Prediction}=1, a_{\mathit{full}}, a_{\mathit{empty}}) = a_{\mathit{full}}, \qquad \textsc{Act}(\mathit{Prediction}=2, a_{\mathit{full}}, a_{\mathit{empty}}) = a_{\mathit{empty}}.$$

When Fiona observes $\mathit{full}$, she applies Equation (4) for $x = \mathit{full}$: she intervenes on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$ *without conditioning $P^F$ on $\textsc{Obs} = \mathit{full}$*. (Note that in Section 6 of the source paper, an unnumbered display formula on page 16 briefly includes a stray `, \Obs=\Val{full}` inside the $\mathtt{do}$ expression—a typographical slip that contradicts Equation (4), the text of Sections 5 and 9, and the authors' immediately following arithmetic.) Let $q = P^F(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty}) = \mathit{twobox})$. Evaluating Equation (4) directly:
* Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{onebox})$: with probability $0.99$ ($\textsc{Accurate}=\mathit{accurate}$), the predictor predicts one-boxing, fills Box B, Fiona sees $\mathit{full}$, executes $\mathit{onebox}$, and gets \$1,000,000. With probability $0.01$ ($\textsc{Accurate}=\mathit{inaccurate}$), the predictor leaves Box B empty, Fiona sees $\mathit{empty}$, executes $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$, and gets $q \cdot \$1,000$ in expectation. Total expected utility:
  $$\$990,000 + 0.01q \cdot \$1,000.$$
* Under $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full}) = \mathit{twobox})$: with probability $0.01$ ($\textsc{Accurate}=\mathit{inaccurate}$), the predictor mistakenly fills Box B, Fiona sees $\mathit{full}$, executes $\mathit{twobox}$, and gets \$1,001,000. With probability $0.99$ ($\textsc{Accurate}=\mathit{accurate}$), the predictor accurately predicts two-boxing, leaves Box B empty, Fiona sees $\mathit{empty}$, and gets $q \cdot \$1,000$ in expectation. Total expected utility:
  $$0.01(\$1,001,000) + 0.99q \cdot \$1,000 = \$10,010 + q \cdot \$990.$$
  *(Note: the source paper writes $\$110,00 + q \cdot \$990$, a minor arithmetic typo for $\$10,010 + q \cdot \$990$; either way, it is vastly smaller than $\$990,000$.)*

Thus, even while staring directly at a full Box B, the **A-FDT** agent imagines that if her decision procedure for $x = \mathit{full}$ output $\mathit{twobox}$, she would almost certainly be staring at an empty box instead! She therefore outputs $\mathit{onebox}$. By the exact same graph structure, an **A-FDT** agent in Parfit's hitchhiker problem pays the \$1,000 ATM fee after safely reaching the city, and an **A-FDT** agent in the mechanical blackmail problem refuses to wire the \$1,000 ransom upon receiving the blackmail notice—because in her $\mathtt{do}(\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{blackmail}) = \mathit{refuse})$ hypothetical, the blackmailer predicts her refusal and never launches the blackmail program in the first place.

### Template 3: Solving an Unfamiliar Case Step-by-Step

To illustrate how a reader can apply **A-FDT** to a novel problem not found in the paper, consider the following scenario:

> **Example (The Automated Compliance Audit).** An algorithmic trading firm uses a decision procedure to operate a server. Each morning, a background hardware fault occurs with prior probability $\theta = 0.20$ ($\textsc{Fault} \in \{1, 0\}$). If a fault occurs ($\textsc{Fault}=1$), the server's logs are corrupted, which will cause a \$100,000 regulatory fine at the end of the day unless the firm runs an expensive manual patch ($\mathit{patch}$) costing \$10,000. Even when no fault occurs ($\textsc{Fault}=0$), running $\mathit{patch}$ still costs \$10,000, whereas doing nothing ($\mathit{pass}$) costs \$0.
>
> However, the firm cannot observe $\textsc{Fault}$ directly. Instead, at noon, a regulatory auditor arrives. The auditor has two independent tools: (1) a diagnostic sensor that detects $\textsc{Fault}=1$ perfectly, and (2) a $90\%$-accurate source-code analyzer ($\textsc{Acc} = 1$ with probability $0.90$) that predicts what action ($\mathit{patch}$ or $\mathit{pass}$) the firm's algorithm will take *if the auditor issues a warning notice*. The auditor wants to collect fines rather than help the firm, so she follows a malicious rule: she issues a warning notice ($x = \mathit{warn}$) if and only if **either** (i) $\textsc{Fault}=1$ and she predicts the firm will $\mathit{pass}$ upon receiving $\mathit{warn}$, **or** (ii) $\textsc{Fault}=0$ and she predicts the firm will $\mathit{patch}$ upon receiving $\mathit{warn}$ (wasting \$10,000). If she does not issue a warning ($x = \mathit{quiet}$), the firm is legally barred from patching. Suppose the firm receives $x = \mathit{warn}$. Should it $\mathit{patch}$ or $\mathit{pass}$?

Let us solve this step-by-step using **EDT**, **CDT**, and **A-FDT**:

1. **Construct the Structural Model $(P, G)$**:
   * Exogenous variables: $\textsc{Fault} \sim \mathrm{Bernoulli}(0.20)$ and $\textsc{Acc} \sim \mathrm{Bernoulli}(0.90)$.
   * Function node for the active observation $x = \mathit{warn}$: $F_{\mathit{warn}} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \mathit{warn}) \in \{\mathit{patch}, \mathit{pass}\}$. (Since no choice exists when $x = \mathit{quiet}$, $F_{\mathit{quiet}}$ is trivially $\mathit{pass}$.)
   * Auditor's prediction node $\textsc{Pred}$: equals $F_{\mathit{warn}}$ if $\textsc{Acc}=1$, and the opposite action if $\textsc{Acc}=0$.
   * Observation node $\textsc{Obs}$: equals $\mathit{warn}$ if $(\textsc{Fault}=1 \land \textsc{Pred}=\mathit{pass})$ or $(\textsc{Fault}=0 \land \textsc{Pred}=\mathit{patch})$; otherwise $\mathit{quiet}$.
   * Physical action node $\textsc{Act}$: equals $F_{\mathit{warn}}$ if $\textsc{Obs}=\mathit{warn}$, and $\mathit{pass}$ if $\textsc{Obs}=\mathit{quiet}$.
   * Utility node $\textsc{V}$:
     $$\textsc{V} = -\$10,000 \cdot \mathbb{I}(\textsc{Act}=\mathit{patch}) - \$100,000 \cdot \mathbb{I}(\textsc{Fault}=1 \land \textsc{Act}=\mathit{pass}).$$

2. **Compare EDT and CDT**:
   * **EDT** conditions on both $\textsc{Obs}=\mathit{warn}$ and $\textsc{Act}=a$. If the agent conditions on $\textsc{Act}=\mathit{patch}$ (and $\textsc{Acc}=1$, say), the auditor's rule implies that $\mathit{warn}$ was sent because $\textsc{Fault}=0$! Conversely, conditioning on $\textsc{Act}=\mathit{pass}$ implies $\textsc{Fault}=1$ (a $-\$100,000$ fine). Like XOR blackmail, EDT is tricked into managing the news: to convince herself that $\textsc{Fault}=0$, Eve chooses $\mathit{patch}$ even when she believes $\mathit{patch}$ is evidence that no patch is needed!
   * **CDT** conditions on $\textsc{Obs}=\mathit{warn}$ to update its belief $p_{\mathit{warn}} = P(\textsc{Fault}=1 \mid \textsc{Obs}=\mathit{warn})$, and then intervenes $\mathtt{do}(\textsc{Act}=a)$ holding $\textsc{Obs}=\mathit{warn}$ fixed. Notice that under CDT, if Carl believes he will $\mathit{pass}$, then seeing $\mathit{warn}$ means $p_{\mathit{warn}} \approx 1$, so CDT tells him to $\mathit{patch}$; but if he believes he will $\mathit{patch}$, then seeing $\mathit{warn}$ means $p_{\mathit{warn}} \approx 0$, so CDT tells him to $\mathit{pass}$! Carl is trapped in a Death-in-Damascus reflective instability loop.

3. **Evaluate Equation (4) for A-FDT**:
   Fiona intervenes on $F_{\mathit{warn}}$ *without conditioning on $\textsc{Obs}=\mathit{warn}$*, propagating the intervention through $\textsc{Pred}$, $\textsc{Obs}$, and $\textsc{Act}$ while holding exogenous $\textsc{Fault}$ ($\theta = 0.20$) and $\textsc{Acc}$ ($0.90$) fixed:
   * **Case 1: $\mathtt{do}(F_{\mathit{warn}} = \mathit{patch})$**.
     * With probability $0.90$ ($\textsc{Acc}=1$), $\textsc{Pred} = \mathit{patch}$. Then:
       * If $\textsc{Fault}=1$ (prob $0.20$), the auditor does *not* warn ($\textsc{Obs}=\mathit{quiet}$), so the firm cannot patch ($\textsc{Act}=\mathit{pass}$) and suffers the $-\$100,000$ fine.
       * If $\textsc{Fault}=0$ (prob $0.80$), the auditor *does* warn ($\textsc{Obs}=\mathit{warn}$), so the firm executes $F_{\mathit{warn}}=\mathit{patch}$ and pays $-\$10,000$.
     * With probability $0.10$ ($\textsc{Acc}=0$), $\textsc{Pred} = \mathit{pass}$. Then:
       * If $\textsc{Fault}=1$ (prob $0.20$), the auditor warns ($\textsc{Obs}=\mathit{warn}$), and the firm executes $F_{\mathit{warn}}=\mathit{patch}$, paying $-\$10,000$ and avoiding the fine!
       * If $\textsc{Fault}=0$ (prob $0.80$), the auditor stays quiet ($\textsc{Obs}=\mathit{quiet}$), and payoff is $\$0$.
     * Summing over all four branches:
       $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(F_{\mathit{warn}} = \mathit{patch})\right] = 0.90\big[0.20(-\$100\text{k}) + 0.80(-\$10\text{k})\big] + 0.10\big[0.20(-\$10\text{k}) + 0.80(\$0)\big] = -\$25,400.$$
   * **Case 2: $\mathtt{do}(F_{\mathit{warn}} = \mathit{pass})$**.
     * Whether $\textsc{Obs}=\mathit{warn}$ or $\textsc{Obs}=\mathit{quiet}$, the firm's physical action is $\textsc{Act}=\mathit{pass}$ in all branches! Hence it never pays the \$10,000 patch fee, and simply suffers the $-\$100,000$ fine whenever $\textsc{Fault}=1$ (prior probability $0.20$):
       $$\mathbb{E}\left[\textsc{V} \;\middle|\; \mathtt{do}(F_{\mathit{warn}} = \mathit{pass})\right] = 0.20(-\$100,000) + 0.80(\$0) = -\$20,000.$$

   Since $-\$20,000 > -\$25,400$, **A-FDT** stably prescribes $\mathit{pass}$! Why? Because from the global perspective of Equation (4), committing to $\mathit{patch}$ upon seeing a warning only saves the firm when the auditor's code analyzer errs ($10\%$ of the time), whereas $90\%$ of the time it induces the auditor to suppress the warning when a real fault occurs and issue false alarms when no fault exists.

---

## 5. Open Questions and Operational Extensions for A-FDT

While Yudkowsky and Soares establish the normative appeal of **A-FDT** across classic dilemmas, their paper explicitly leaves several foundational and operational questions open. To help researchers apply **A-FDT** systematically, we must clearly separate what follows directly from the source paper from additional assumptions or operational proposals of our own.

### 1. Deducing the Subjunctive Dependency Graph $G$

**What the source states**: In Section 5, the authors emphasize that while Pearl (2000) provides a rigorous methodology for inferring *causal* graphs from observation and physical intervention, no comparable theory yet exists for inferring *logical* or *subjunctive* graphs:

> *"Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."*

**Operational proposal (The Computational Modularity Rule)**: When building $(P, G)$ for an unfamiliar domain, how should a modeler decide which nodes receive a directed edge from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$? We propose formalizing $G$ as a **Structural Causal Model with Oracle Calls (SCM-OC)**. In a standard SCM, each endogenous variable $V_i$ is determined by a structural equation $V_i = f_i(\mathrm{Pa}(V_i), U_i)$. To operationalize **A-FDT**, we introduce the following modeling rule:
* Whenever our mechanistic model of a physical subsystem $V_i$ (such as a twin, a game-theoretic opponent, or an inspection algorithm) entails that $V_i$'s physical transition function simulates, proves theorems about, or queries the agent's decision procedure under input state $(P, G, x)$ up to some fidelity/noise parameter $U_i$, we represent that internal query as a call to an abstract subroutine $\mathcal{O}_{P,G,x}()$, and draw a directed edge $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x}) \to V_i$.
* If a subsystem $V_j$ (such as a carcinogenic lesion or prior weather) is modeled by a physical mechanism that does not query or simulate the agent's decision procedure—even if $V_j$ is statistically correlated with $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ via an upstream common cause or selection bias—no edge is drawn from $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$ to $V_j$.

This operational rule does not solve the full philosophical problem of logical uncertainty (such as conditioning on the negation of the Twin Prime Conjecture), but it suffices to construct $G$ unambiguously in any decision problem or game where the agent can specify which environmental processes are *predictors/replicas* of her current decision state and which are *mechanically independent*.

### 2. Off-Path Priors ($q$) and A-FDT vs. Policy-FDT

**What the source states**: In Footnotes 7 and 16, Yudkowsky and Soares remark that in their preferred formalization of functional decision theory, *"agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."*

Why does Equation (4)—**A-FDT**—suffice for the paper's examples, and where exactly does its action-indexed architecture need additional assumptions? Notice that in both the smoking lesion problem (Figure 4) and the transparent Newcomb problem (Figure 5b), Fiona's graph $G^F$ contains *multiple* $\textsc{fdt}$ nodes—one for her actual input (e.g., $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$), and another for the counterfactual input she did not receive (e.g., $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$). Under Equation (4), when Fiona observes $\mathit{full}$, she intervenes *only* on $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{full})$, treating the unvisited node $\textsc{fdt}(\underline{P^F}, \underline{G^F}, \mathit{empty})$ as an exogenous random variable with prior probability $q$. In the transparent Newcomb problem, the authors note that the true value of $q$ is $1$, *"but in this case it doesn't matter if Fiona has some uncertainty about how she would act in that case"* because $0.99(\$1,000,000) + 0.01q(\$1,000) > 0.01(\$1,001,000) + 0.99q(\$1,000)$ holds for *every* $q \in [0, 1]$.

**Operational proposal (Recursive Off-Path Resolution and the Asymmetric Twin Boundary)**: What happens in an unfamiliar problem where the optimal action at observation $x_1$ *does* depend on the value of $q$ at an unvisited observation $x_2$? We distinguish two regimes:

1. *Decoupled Off-Path Branches (Recursive A-FDT)*: Suppose the predictor only predicts what the agent does at $x_1$, while the off-path node $F_{x_2} \coloneqq \textsc{fdt}(\underline{P}, \underline{G}, \underline{x_2})$ only affects the agent's payoff in the fallback branch where observation $x_2$ occurs, and suppose $F_{x_2}$'s own optimization does not depend on $F_{x_1}$. Then an **A-FDT** agent does not need to leave $q = P(F_{x_2} = a)$ as an arbitrary free parameter! Because she has full access to $(P, G, x_2)$, she can operationally compute $a^*_{x_2} \coloneqq \mathrm{FDT}(P, G, x_2)$ via Equation (4) as a subroutine first, and set $q = \mathbb{I}(a = a^*_{x_2}) \in \{0, 1\}$.

2. *Coupled Cross-Observation Dilemmas (Where A-FDT and P-FDT Diverge)*: Consider an **Asymmetric Observation Twin Prisoner's Dilemma** (an extension beyond the source text). Two identical agents running the same decision algorithm are placed in separate rooms: Room 1 ($x = \mathit{room1}$) and Room 2 ($x = \mathit{room2}$). Each knows which room she is in, and each must choose $\mathit{cooperate}$ (costing \$1,000) or $\mathit{defect}$ (costing \$0); if both cooperate, each gets \$1,000,000.
   * If the agent in Room 1 strictly applies **A-FDT** (Equation 4), she intervenes *only* on the node $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{room1}) = a$. Because her twin in Room 2 observes $x = \mathit{room2} \neq \mathit{room1}$, the twin's action is governed by the *distinct* node $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{room2})$. Under pure Equation (4), intervening on $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{room1})$ does *not* alter $\textsc{fdt}(\underline{P}, \underline{G}, \mathit{room2})$! Thus, a literal **A-FDT** agent treats her twin's action in Room 2 as fixed, and defects—just like CDT!
   * This explains why Footnotes 7 and 16 state that policy-based FDT (**P-FDT**) differs in multi-agent dilemmas. Under **P-FDT**, both twins intervene on the single policy-returning node $\textsc{fdt}(\underline{P}, \underline{G}) = \pi$, where $\pi : \{\mathit{room1}, \mathit{room2}\} \to \{\mathit{cooperate}, \mathit{defect}\}$, and then execute $\pi(x)$. Alternatively, to enable **A-FDT** to cooperate here without abandoning Equation (4), one must adopt an additional **Symmetry Quotient Assumption**: stripping decision-irrelevant indexical labels (such as room numbers that do not enter the payoff function asymmetrically) from the observation representation $x$ before passing $x$ into $\mathrm{FDT}(P, G, x)$.

### 3. Formalizing "Fair" Decision Problems

**What the source states**: In Section 9, Yudkowsky and Soares note that no decision theory can win in *all* conceivable environments—for example, if a mind-reader rewards agents if and only if their source code is CDT, or punishes agents for taking \$100 in the cosmic ray problem. They argue that **A-FDT** dominates rivals in **"fair problems"**, informally defined as dilemmas where *"the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand."* As they put it: *"Newcomb's predictor doesn't punish rational agents; she punishes two-boxers."* However, Footnote 15 acknowledges that a general mathematical definition of fairness (especially in adversarial games like "act differently from a copy of yourself") remains an open problem.

**Operational proposal (Extensionality of Environmental Mechanisms)**: For single-agent predictive dilemmas, we can formalize the authors' criterion of fairness as **Input-Output Extensionality** on the graph $G$: a decision problem $(P, G)$ is *extensionally fair* if every path from the agent's internal cognitive state or source code to the utility node $\textsc{V}$ is $d$-separated (blocked) in $G$ by the family of input-output variables $\{\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})\}_{x \in \mathcal{X}}$ and $\textsc{Act}$. Whenever this graphical condition holds, predictors in the environment respond solely to *what output* the agent's decision function produces in the dilemma at hand, never to *how* the algorithm is syntactically written.

---

## 6. Conclusion

**Action functional decision theory (A-FDT)**, as formalized in Equation (4) of Yudkowsky and Soares, represents a decisive mathematical advance in the theory of rational choice. By shifting the locus of counterfactual surgery from the physical act token $\textsc{Act}$ to the logical output node $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$, and by handling observations through shifting the point of intervention rather than Bayesian conditioning, **A-FDT** captures the best of both worlds: it preserves genuine computational and predictive dependencies that CDT severs, while severing spurious statistical correlations that trap EDT. Equipped with the graphical mechanics of Equation (4) and clear operational rules for modeling subjunctive subroutines and off-path branches, decision theorists and computer scientists can apply **A-FDT** as a coherent, reflectively stable calculus for instrumental rationality.

---

## References

* Ahmed, A. (2014). *Evidence, Decision and Causality*. Cambridge University Press.
* Cohen, D. (1990). On what cannot be. In *Truth or Consequences: Essays in Honor of Nuel Belnap* (pp. 123–132). Kluwer Academic Publishers.
* Dai, W. (2009). Towards a new decision theory. *Less Wrong*.
* Drescher, G. L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Eells, E. (1984). Metatickles and the dynamics of deliberation. *Theory and Decision*, 17(1), 71–95.
* Gibbard, A., & Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory* (Vol. 1, pp. 125–162). D. Reidel.
* Jeffrey, R. C. (1983). *The Logic of Decision* (2nd ed.). University of Chicago Press.
* Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, J. M. (2012). Regret and instability in causal decision theory. *Synthese*, 187(1), 123–145.
* Kleene, S. C. (1938). On notation for ordinal numbers. *Journal of Symbolic Logic*, 3(4), 150–155.
* Lewis, D. (1979). Prisoners' dilemma is a Newcomb problem. *Philosophy & Public Affairs*, 8(3), 235–240.
* Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.
* Nozick, R. (1969). Newcomb's problem and two principles of choice. In *Essays in Honor of Carl G. Hempel* (pp. 114–146). D. Reidel.
* Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, J. (1996). Causation, action, and counterfactuals. In *6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-'96)* (pp. 51–73). Morgan Kaufmann.
* Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, C. S. (1934). *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, B. (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, N., & Fallenstein, B. (2015). Toward idealized decision theory. *arXiv preprint arXiv:1507.01986*.
* Spohn, W. (1977). Where Luce and Krantz do really generalize Savage's decision model. *Erkenntnis*, 11(1), 113–134.
* Yudkowsky, E. (2010). *Timeless Decision Theory*. The Singularity Institute.
* Yudkowsky, E., & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. Machine Intelligence Research Institute, arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Scope**

I'm now focusing on defining the scope for this explanation of Action Functional Decision Theory. The goal is to create a technical explanation, probably in essay or blog post form. I am keeping in mind the need for practical application to real-world decision-making problems. I need to make sure the target audience is clear to define scope, but an expert audience is presumed.


**Clarifying Key Formalism**

I've been analyzing the formal aspects, specifically focusing on Equation (4) from Yudkowsky and Soares' paper. I'm viewing this equation as the primary formal presentation of Action Functional Decision Theory (A-FDT). My role is a researcher crafting a technical piece for a mathematically literate audience, exploring both the mathematical rigor and philosophical underpinnings. The naming convention is critical for clarity.


**Refining Nomenclature Choices**

I'm now establishing conventions, with "A-FDT" as the consistent name. I will clearly differentiate other theories like CDT and EDT. I'm focusing on faithfully reproducing quotations. The essay must be coherent, precise, with definitions, equations, examples, and explanations, so a reader could use the essay to decide unfamiliar cases. I need to explain A-FDT's evaluation process, including dependencies and counterfactuals, and address open questions, distinguishing the source material from my own interpretations. The target length is 2400-3000 words.


**Analyzing Core Theories**

I'm now diving into the core of the source material. I'm focusing on the philosophical shifts underlying A-FDT. I need to clearly delineate how EDT and CDT are expected utility theories. I'm taking notes on their failures to pinpoint where A-FDT fills the gaps and improves on these. My goal is to extract the core ideas behind the expected utility theories.


**Evaluating A-FDT Mechanics**

I'm currently focusing on how A-FDT addresses the shortcomings of CDT and EDT. I understand CDT doesn't respect enough correlations, specifically concerning the logical ties between an agent's decision procedure and external predictors. I'm now exploring how both CDT and EDT fail in sequential/observation-dependent prediction problems. I'm focusing on the A-FDT model, where the agent treats her decision as the output of a mathematical function, and I'm reviewing the formalization by policy iteration.


**Interpreting A-FDT Mechanics**

I'm now diving into the formal aspects of Equation (4), and the contrast with CDT. I see that A-FDT intervenes on the function result, not the physical node itself, clarifying the critical distinction. My focus is on unpacking the meaning of 'do' and the implications of this type versus token intervention. I'm exploring the implications for counterfactual reasoning within the A-FDT framework. The goal is a clear technical explanation.


**Clarifying Agent Actions**

I'm now clarifying the nature of agent actions within the A-FDT model. The agent's action and any predictor's model are *downstream* from the computational output $\textsc{fdt}(\underline{P}, \underline{G}, \underline{x})$. This includes understanding how the agent's actual physical action and the predictor's model depend on this mathematical result. Also, I'm examining how A-FDT handles observations, noting that A-FDT does *not* condition the prior probability distribution $P$ on $\textsc{Obs}=x$, which contrasts with CDT. I need to make sure my explanation is consistent with Section 6.


**Verifying Mathematical Details**

I'm now cross-referencing Equation (4) with the example calculations in Sections 5, 6, and 9, especially the *lack* of conditioning on observation. The critical point is that the numerical calculation in Section 6 works only without $\textsc{Obs}=\mathit{full}$! I am also verifying the calculation in Section 6, explicitly working through the case of Transparent Newcomb. My focus is on ensuring mathematical consistency and clarifying the underlying assumptions.


**Calculating Expected Utility**

I'm now calculating the agent's total expected utility under different scenarios, specifically focusing on the Transparent Newcomb problem. I've noted that if the expectation had conditioned on $\textsc{Obs}=\mathit{full}$, the probability of Box B being full would be $1$, not $0.99$, which is a critical point. This helps clarify the implications of Equation (4) in this context. I'm focusing on the mathematical consistency.


**Clarifying A-FDT Implementation**

I'm now identifying open questions, and developing operational proposals for implementation. The source material's largest open problem involves constructing the subjunctive dependency graph, $G$, and evaluating counterpossibilities, which I need to understand better. I am also investigating action-based versus policy-based FDT in a multi-observation context. I am also identifying a typographical error. I've noted that the unnumbered formula in Section 6 included a stray $\textsc{Obs}=\mathit{full}$, which should clarify that A-FDT evaluates observations by shifting intervention.


**Analyzing Multi-Agent Dilemmas**

I'm now focusing on multi-agent dilemmas and the implications of policy iteration within A-FDT. I'm exploring scenarios where a predictor's actions depend on the agent's behavior across multiple observations, or when different observations are available to the agent. I see that A-FDT, under Equation (4), intervenes on specific nodes and treats other decision points as priors, and that this could be a problem. My goal is to determine the limitations, and to create an explanation.


**Operationalizing FDT Mechanics**

I'm now focused on operationalizing the construction of $(P, G)$ for applying A-FDT in novel situations, especially focusing on 'fair' problems. I'm proposing an operational rule based on Structural Causal Models, treating the agent's decision as a subroutine. This addresses the challenge of defining counterpossibilities, and helps develop a recipe for applying Equation (4) in practice.


**Developing Operational Protocols**

I'm now developing operational protocols for resolving cross-observation priors and addressing potential limitations in A-FDT. I'm focusing on recursive A-FDT resolution, which computes the optimal action at each counterfactual observation node first. I am exploring the use of a recursive approach to handle potential dependencies on unobserved branches and asymmetric observations, and applying equation (4) recursively to each observation.


**Planning Section Content**

I am now planning the structure and word count. I'm targeting a length of 2650-2800 words. The plan includes an introduction of ~350 words, that will introduce the conflict between CDT and EDT and introduce A-FDT. I need to explain the action-indexed architecture, and explicitly diagnose when dependencies are coupled. This will provide a clear, rigorous understanding of how to use A-FDT.


**Analyzing A-FDT Formalism**

I'm now analyzing the core philosophical shift of A-FDT, viewing the action as the logical output of a decision function, not as a physical token. My current focus is on the formal architecture. I'm unpacking Joyce's expected utility framework, specifically comparing EDT, CDT and A-FDT using Equations 1, 2, 3 and 4, and understanding the decisive departures from CDT. I need to explain the intervention on the decision-function output node, contrasted with the Act, and responding.



**Structuring the Subsections**

I'm now structuring the remaining sections, focusing on the planned content distribution. I've broken down "Subjunctive Dependence" to cover the type-token distinction and the two calculators analogy, explaining how A-FDT handles counterpossibilities, and why the FDT' workaround fails. "Applying A-FDT" will now include canonical and unfamiliar problems. The total is now about 2700 words.

I'm aiming for a concise explanation of how A-FDT evaluates observations.


**Developing Section Examples**

I'm now creating examples for the paper, including observation-gated prediction and an unfamiliar case. I'm focusing on scenarios that showcase how the graph separates predictor-like dependencies from statistical correlations and includes preference uncertainty. I'm also working through the math for Transparent Newcomb. Finally, I'm working through a step-by-step example with algorithmic collusion.



**Clarifying Branch Dependencies**

I'm now focusing on how A-FDT (Equation 4) handles off-path nodes and exploring its relationship to policy-based FDT, especially with regards to decoupled branches. I'm proposing recursive branch evaluation for situations where branches are decoupled, and showing how A-FDT may diverge from Policy-FDT unless extended. I also need to provide formal examples for clarification. I am drafting a concise conclusion.


**Refining Equation Details**

I'm now refining the details of Equation (4), which, per Footnotes 7 and 16, is an *action-indexed* formulation. I am now referring to this variant as **A-FDT**, as contrasted with the *policy-indexed* form, which I'm calling **Policy-FDT** or **P-FDT**. I am also carefully double-checking the accuracy of every quotation. I'm focusing on those from the source, to ensure 100% accuracy.


```
