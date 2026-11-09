# 021_fdt_eq4_google_gemini-4-argon_rhigh_phigh / 00014

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/ab66d442-da9b-476d-9b9f-dc9c292f7d06/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/ab66d442-da9b-476d-9b9f-dc9c292f7d06/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Intervening on the Algorithm: A Mathematical Guide to Action Functional Decision Theory (A-FDT)

For nearly half a century, normative decision theory has been divided between two competing accounts of instrumental rationality: **Evidential Decision Theory (EDT)** and **Causal Decision Theory (CDT)**. When evaluated by a straightforward pragmatic criterion—how much expected utility an agent actually achieves across decision problems—neither theory consistently prevails. EDT thrives in Newcomb's problem and the psychological twin prisoner's dilemma, where predictors or symmetrical reasoners anticipate the agent's behavior, yet falters in medical common-cause dilemmas like Skyrms's smoking lesion problem and becomes systematically exploitable in blackmail scenarios. CDT, conversely, makes the sensible choice in the smoking lesion problem by isolating the physical causal consequences of an act, yet walks away poor in Newcomb's problem, defects against its own twin, and falls into reflective instability when facing adversarial predictors like Death in Damascus. Worse still, in sequential prediction dilemmas such as Parfit's hitchhiker problem and the transparent Newcomb problem, *both* EDT and CDT fail to secure the high-utility outcome without resorting to costly prior precommitments.

In *"Functional Decision Theory: A New Theory of Instrumental Rationality"* (2017), Eliezer Yudkowsky and Nate Soares propose a unified resolution to this impasse. Rather than treating a decision as the selection of an isolated physical act token (as CDT does) or as an update on auspicious news (as EDT does), a rational agent should treat her decision as the output of a fixed mathematical decision function and ask: *"Which output of this very decision procedure yields the best outcome?"*

While Yudkowsky and Soares note that their broader framework can be formulated over either individual actions or comprehensive policies, their primary formal presentation in Equation (4) of Section 5 defines the theory over actions. In this essay, we examine **Action Functional Decision Theory (A-FDT)**—the action-level formalization given by Equation (4)—in mathematical detail. We will unpack its graphical semantics, trace how it evaluates counterfactuals and observations across classic dilemmas, examine the theoretical questions left open by the source paper, and develop a step-by-step operational procedure that enables a practitioner to apply **A-FDT** to unfamiliar decision problems.

---

## 1. The Formal Architecture of A-FDT

Following the representation theorem of Joyce (1999), Yudkowsky and Soares frame EDT, CDT, and **A-FDT** within a common expected-utility scaffold. Consider an agent choosing an action $\act$ from a finite set $\mathcal{A}$ after receiving an observation history $\obs$ from a countable set $\mathcal{X}$, where outcomes $o_1, o_2, \dots$ are drawn from a countable set $\mathcal{O}$ and valued by a bounded utility function $\Util : \mathcal{O} \to \mathbb{R}$. All three decision theories prescribe selecting an action $\act \in \mathcal{A}$ that maximizes expected utility:

$$\mathcal{EU}(\act) \coloneqq \sum_{j=1}^N P(\act \hookrightarrow o_j ;\, \obs) \cdot \Util(o_j) \tag{1}$$

As Joyce observes, competing decision theories do not disagree about how outcomes are valued; they disagree about the epistemic perspective captured by the decision-hypothetical connective $\hookrightarrow$. In algorithmic terms, an agent maintains an internal world-model $\model$ and, for each candidate action $\act \in \mathcal{A}$, performs a formal operation on $\model$ to construct a hypothetical distribution $\model^{\act\hookrightarrow}$ representing what the world would look like if she took action $\act$. Let $\Outcome$ be the random variable over $\mathcal{O}$, define the utility random variable $\VV \coloneqq \Util(\Outcome)$, and write $\EE$ for expectation with respect to the probability distribution $P$ inside $\model$.

**Evidential Decision Theory (EDT)** takes the world-model $\model$ to be a standard Bayesian probability distribution $P$ and constructs each hypothetical via standard conditionalization on both the observation $\Obs = \obs$ and the physical action $\Act = \act$ (ignoring actions of probability zero):

$$\EDT(P, \obs) \coloneqq \argmax_{\act \in \mathcal{A}} \EE\left(\VV \;\middle|\; \Obs = \obs, \Act = \act\right) \tag{2}$$

**Causal Decision Theory (CDT)** insists that conditionals are not counterfactuals: conditioning on $\Act = \act$ preserves purely statistical correlations with upstream common causes. Adopting Pearl's (1996, 2000) graphical causal framework, Yudkowsky and Soares represent a CDT agent's world-model as a pair $(P, G)$, where $G$ is a directed acyclic graph (DAG) encoding causal directionality among the variables of $P$. CDT constructs its hypotheticals by conditioning on the observation $\Obs = \obs$ and applying Pearl's $\Do$-operator to the physical action node $\Act$:

$$\CDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal{A}} \EE\left(\VV \;\middle|\; \Do(\Act = \act), \Obs = \obs\right) \tag{3}$$

Graphically, $\Do(\Act = \act)$ severs all incoming edges into $\Act$, fixes $\Act = \act$, and propagates this value strictly forward along directed causal paths in $G$.

### The Primary Equation of A-FDT

**A-FDT** retains Pearl's graphical intervention machinery but shifts *where* the surgery occurs and *how* observations enter the calculation. In Equation (4) of Section 5 (where the source paper uses the generic notation $\FDT$ and $\FDTvar$), **A-FDT** is defined as:

$$\operatorname{A-FDT}(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal{A}} \EE\left(\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs}) = \act\right)\right) \tag{4}$$

To read Equation (4) with mathematical precision, we must unpack three essential elements of its syntax and semantics:

1. **Logical Variables and Dequotation ($\underline{P}, \underline{G}, \underline{\obs}$):** In **A-FDT**, the probability distribution $P$ ranges not only over physical states of the world, but also over the outputs of mathematical functions and algorithms. The underline notation denotes *dequotation*: if $\obs$ has the value $3$, then $\Var{Z}\underline{\obs}$ denotes the syntactic variable name $\Var{Z}3$. Thus, for an agent whose current world-model is $(P, G)$ and whose observation is $\obs$, $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs})$ is a specific variable inside $G$ that represents the logical output of the $\operatorname{A-FDT}$ algorithm when evaluated on the specific inputs $(P, G, \obs)$. As Yudkowsky and Soares note, the self-reference required for a model $(P, G)$ to contain a node indexed by $(\underline{P}, \underline{G})$ is mathematically benign: by Kleene's (1938) second recursion theorem ("quining"), a computational data structure can coherently encode and manipulate an exact syntactic representation of itself without knowing in advance what output the computation will ultimately return.
2. **Intervening on the Logical Type Rather Than the Physical Token:** Comparing Equations (3) and (4), CDT intervenes on the physical node $\Act$ ("what my body does right now"), whereas **A-FDT** intervenes on the logical node $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs})$ ("what this mathematical decision function outputs on these inputs"). Using Peirce's (1934) type-token distinction, CDT intervenes on the physical *token* of the action, while **A-FDT** intervenes on the algorithmic *type*. Any physical process in the universe that implements, simulates, or predicts $\operatorname{A-FDT}(P, G, \obs)$—including both the agent's own physical motor system $\Act$ and a twin's or predictor's model of the agent—is modeled in $G$ as a child of $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs})$.
3. **Observation-Indexed Intervention Instead of Bayesian Conditioning ("Updatelessness"):** Look closely at what is *absent* from Equation (4): unlike EDT in Equation (2) and CDT in Equation (3), **A-FDT** does not condition the distribution $P$ on $\Obs = \obs$. Instead, when an **A-FDT** agent observes $\obs$, she uses $\obs$ to select *which logical node* to intervene upon—switching her point of intervention from $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\emptyset})$ to $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs})$ while taking the expectation over the prior distribution $P$ modified only by $\Do(\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs}) = \act)$. This feature—inherited from Wei Dai's (2009) Updateless Decision Theory (UDT), and deliberately avoiding the harmful "double update" of Yudkowsky's (2010) Timeless Decision Theory (TDT), which both conditioned on $\Obs = \obs$ and intervened logically—allows an **A-FDT** agent to recognize that if her decision function had output a different action upon observing $\obs$, she might never have observed $\obs$ in the first place.

---

## 2. Subjunctive Dependence and Counterpossible Semantics

Why represent a mathematical function's output as a node in a directed acyclic graph? Philosophically, **A-FDT** rests on the concept of **subjunctive dependence**: the dependency relation that holds among physical systems that compute, emulate, or predict the same mathematical function.

As Yudkowsky and Soares illustrate, if two well-functioning calculators on opposite sides of the globe both compute $6288 + 1048$, their outputs are interdependent—not necessarily because of a proximate physical signal passing between them, but because both physical devices are constrained by the same arithmetical function. Causal dependence (such as a scribe copying a calculator's display) is a special case of subjunctive dependence, whereas accidental statistical correlation (two calculators happening to be painted pink) is not. Consequently, the authors summarize the core analogy of the theory: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."*

Evaluating alternative outputs of a deterministic mathematical function, however, requires reasoning about **counterpossibilities**—counterfactual conditionals whose antecedents are logically or mathematically impossible (Cohen 1990). If $\operatorname{A-FDT}(P, G, \obs)$ in fact evaluates to $\Val{cooperate}$, there is no logically possible world in which that fixed function on that fixed input evaluates to $\Val{defect}$, just as there is no logically possible world in which $6288 + 1048 \neq 7336$.

Ideally, one might wish to define an epistemic conditioning operator $\True(\phi)$ that updates a probability distribution $P$ to reflect the counterpossible supposition that a logical sentence $\phi$ is true, yielding an evidential-style formulation:

$$\operatorname{A-FDT}^*(P, \obs) = \argmax_{\act \in \mathcal{A}} \EE\left(\VV \;\middle|\; \True\left(\Var{a-fdt}(\underline{P}, \underline{\obs}) = \act\right)\right)$$

Because mathematical logic and formal epistemology do not yet possess a canonical, general-purpose definition of $\True(\phi)$ for counterpossible propositions, Yudkowsky and Soares bypass the problem in Equation (4) by requiring that the agent's world-model explicitly supply a subjunctive dependency graph $G$ alongside $P$. Within $(P, G)$, the logical node $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs})$ is treated as a parent node whose structural equations specify how physical variables (such as $\Act$ and $\Var{Prediction}$) vary as a function of its output. Standard Pearlian graph surgery $\Do(\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs}) = \act)$ then computes the exact counterpossible hypothetical required.

Notice that in simple decision environments—where every variable that correlates with $\Act$ is causally downstream of $\Act$ (except $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs})$ itself, on which $\Act$ depends)—Equations (2), (3), and (4) coincide:

$$\EE[\VV \mid \act] = \EE[\VV \mid \Do(\act)] = \EE\left[\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs}) = \act\right)\right]$$

The theories diverge precisely when non-causal correlations exist between the agent's action and the environment. Let us trace how Equation (4) operates across the benchmark dilemmas that separate **A-FDT** from EDT and CDT.

---

## 3. Mathematical Walkthroughs of Benchmark Dilemmas

Following Section 6 of the source paper, we compare three idealized agents—Eve (who executes $\EDT$), Carl (who executes $\CDT$), and Fiona (who executes $\operatorname{A-FDT}$ via Equation (4))—assuming each holds an accurate world-model of the dilemma at hand.

### 3.1 Standard Newcomb's Problem vs. The Smoking Lesion Problem

In **Newcomb's problem** (Nozick 1969), transparent Box A contains $\$1{,}000$, and opaque Box B contains either $\$1{,}000{,}000$ ($\Val{full}$) or $\$0$ ($\Val{empty}$). Yesterday, a predictor with $99\%$ accuracy ($\Var{Accurate} = \Val{accurate}$ with probability $0.99$, $\Val{inaccurate}$ with probability $0.01$) filled Box B if and only if she predicted the agent would leave Box A behind ($\Val{onebox}$) rather than taking both boxes ($\Val{twobox}$). No observation $\obs$ is made during the problem, so we omit $\obs$.

In Fiona's **A-FDT** model $(P^F, G^F)$, the root node of interest is her decision function's output $\Var{a-fdt}(\underline{P^F}, \underline{G^F})$, alongside the independent noise node $\Var{Accurate} \sim \text{Bernoulli}(0.99)$. The structural equations encoded by $G^F$ are:

$$\begin{aligned}
\Act &= \Var{a-fdt}(\underline{P^F}, \underline{G^F}) \\
\Var{Prediction} &= \begin{cases} \Var{a-fdt}(\underline{P^F}, \underline{G^F}) & \text{if } \Var{Accurate} = \Val{accurate} \\ \neg \Var{a-fdt}(\underline{P^F}, \underline{G^F}) & \text{if } \Var{Accurate} = \Val{inaccurate} \end{cases} \\
\Var{Box B} &= \begin{cases} \Val{full} & \text{if } \Var{Prediction} = \Val{onebox} \\ \Val{empty} & \text{if } \Var{Prediction} = \Val{twobox} \end{cases}
\end{aligned}$$

with utility $\VV(\Act, \Var{Box B})$ given by $\VV(\Val{twobox}, \Val{full}) = \$1{,}001{,}000$, $\VV(\Val{onebox}, \Val{full}) = \$1{,}000{,}000$, $\VV(\Val{twobox}, \Val{empty}) = \$1{,}000$, and $\VV(\Val{onebox}, \Val{empty}) = \$0$.

When Fiona evaluates Equation (4), she compares two interventions on $\Var{a-fdt}(\underline{P^F}, \underline{G^F})$:
* Under $\Do(\Var{a-fdt}(\underline{P^F}, \underline{G^F}) = \Val{onebox})$, $\Act$ becomes $\Val{onebox}$ with probability $1$ and $\Var{Box B}$ becomes $\Val{full}$ with probability $0.99$, yielding:
  $$\EE\left[\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P^F}, \underline{G^F}) = \Val{onebox}\right)\right] = 0.99(\$1{,}000{,}000) + 0.01(\$0) = \$990{,}000$$
* Under $\Do(\Var{a-fdt}(\underline{P^F}, \underline{G^F}) = \Val{twobox})$, $\Act$ becomes $\Val{twobox}$ with probability $1$ and $\Var{Box B}$ becomes $\Val{full}$ with probability $0.01$, yielding:
  $$\EE\left[\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P^F}, \underline{G^F}) = \Val{twobox}\right)\right] = 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000) = \$11{,}000$$

Because $\$990{,}000 > \$11{,}000$, $\operatorname{A-FDT}(P^F, G^F) = \Val{onebox}$. Notice that Carl (CDT) intervenes directly on $\Act$, severing the link between $\Act$ and his predisposition while holding $\Var{Box B}$ fixed at some prior probability $p$; since $p(\$1{,}001{,}000) + (1-p)(\$1{,}000) > p(\$1{,}000{,}000)$ for every $p \in [0,1]$, Carl two-boxes and receives $\$1{,}000$.

Now consider why CDT's dominance argument fails against **A-FDT**. As Yudkowsky and Soares point out, every decision theory defines dominance relative to its own counterfactuals. Relative to CDT counterfactuals (changing physical action $\Act$ while holding fixed the output of the agent's decision function), two-boxing dominates. Relative to **A-FDT** counterfactuals (changing the output of $\Var{a-fdt}(\underline{P^F}, \underline{G^F})$ while holding fixed the subjunctive dependency that the predictor's model tracks that function with $99\%$ accuracy), one-boxing dominates.

Why, then, does **A-FDT** not refrain from smoking in **the smoking lesion problem** (Skyrms 1980)? In that dilemma, an unobserved arterial lesion ($\Var{Lesion} \in \{\Val{lesion}, \Val{nolesion}\}$) causes lung cancer $99\%$ of the time (versus $1\%$ without the lesion) and simultaneously causes agents to love smoking (gaining $\$1{,}000$ in utility from smoking, plus $\$1{,}000{,}000$ if they avoid fatal cancer). For Eve (EDT) and Carl (CDT), the Bayesian network and causal graph are isomorphic to Newcomb's problem under a simple relabeling of variables ($\Var{Predisposition} \mapsto \Var{Lesion}$, $\Val{twobox} \mapsto \Val{smoke}$, $\Val{onebox} \mapsto \Val{refrain}$). Thus, Eve refrains and Carl smokes.

For Fiona (**A-FDT**), however, the subjunctive graph $G^F$ is *not* isomorphic to Newcomb's problem, because cancer does not simulate or depend upon the output of the $\operatorname{A-FDT}$ algorithm. Instead, as Yudkowsky and Soares formalize the problem in Section 6, the lesion determines the agent's utility function: an agent with the lesion has a preference distribution $P^F_S$ (reflecting utility function $\Util_S$, which values smoking at $+\$1{,}000$), while an agent without the lesion has a preference distribution $P^F_R$ (reflecting $\Util_R$, which values smoking at $-\$1$). Because Fiona cannot introspectively observe whether she has the lesion, she computes her decision under uncertainty about which world-model is physically driving her body. Her graph $G^F$ routes $\Var{Lesion}$ and *both* logical nodes—$\Var{a-fdt}(\underline{P^F_S}, \underline{G^F})$ and $\Var{a-fdt}(\underline{P^F_R}, \underline{G^F})$—into $\Act$ via a multiplexer structural equation:

$$\Act\left(\Var{Lesion}, s, r\right) \coloneqq \begin{cases} s & \text{if } \Var{Lesion} = \Val{lesion} \\ r & \text{if } \Var{Lesion} = \Val{nolesion} \end{cases}$$

where $s = \Var{a-fdt}(\underline{P^F_S}, \underline{G^F})$ and $r = \Var{a-fdt}(\underline{P^F_R}, \underline{G^F})$. Meanwhile, $\Var{Cancer}$ depends only on $\Var{Lesion}$ and background noise $\Var{Luck} \sim \text{Bernoulli}(0.99)$, with no directed path from either $\Var{a-fdt}$ node to $\Var{Lesion}$ or $\Var{Cancer}$.

Let $p = P^F_S(\Var{Lesion} = \Val{lesion}) \in (0, 1)$, and let $q = P^F_S(\Var{a-fdt}(\underline{P^F_R}, \underline{G^F}) = \Val{smoke})$ be Fiona's prior probability that the non-lesion procedure smokes. When Fiona (whose preferences are $\Util_S$) evaluates $\operatorname{A-FDT}(P^F_S, G^F)$, she intervenes on $\Var{a-fdt}(\underline{P^F_S}, \underline{G^F})$. Because $\Var{Lesion}$ is upstream of $\Act$ and unlinked to $\Var{a-fdt}(\underline{P^F_S}, \underline{G^F})$, the intervention leaves $P^F_S(\Var{Lesion} = \Val{lesion}) = p$ invariant:
* If $\Do(\Var{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \Val{smoke})$, then with probability $p$ she has the lesion (surviving cancer with probability $0.01$ for $\$10{,}000$ expected health utility, plus $\$1{,}000$ because $\Act = s = \Val{smoke}$), and with probability $1-p$ she lacks the lesion (surviving cancer with probability $0.99$ for $\$990{,}000$ expected health utility, plus $q \cdot \$1{,}000$ from $\Act = r$):
  $$\EE\left[\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \Val{smoke}\right)\right] = p(\$10{,}000 + \$1{,}000) + (1-p)(\$990{,}000 + q \cdot \$1{,}000)$$
* If $\Do(\Var{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \Val{refrain})$, the $(1-p)$ branch is unchanged while the $p$ branch loses the $\$1{,}000$ smoking payoff:
  $$\EE\left[\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P^F_S}, \underline{G^F}) = \Val{refrain}\right)\right] = p(\$10{,}000) + (1-p)(\$990{,}000 + q \cdot \$1{,}000)$$

The difference in expected utility is strictly positive ($p \cdot \$1{,}000 > 0$), so $\operatorname{A-FDT}(P^F_S, G^F) = \Val{smoke}$. By distinguishing algorithmic dependencies from common-cause statistical correlations, **A-FDT** one-boxes in Newcomb's problem and smokes in the smoking lesion problem.

### 3.2 Transparent Newcomb, Parfit's Hitchhiker, and Mechanical Blackmail

The power of **A-FDT**'s second distinctive feature—responding to an observation $\obs$ by changing the target node of intervention rather than conditioning $P$ on $\Obs = \obs$—emerges in **the transparent Newcomb problem** (Drescher 2006). Here, both boxes are transparent, and the $99\%$-accurate predictor fills Box B with $\$1{,}000{,}000$ if and only if she predicts that the agent will one-box *upon seeing that Box B is full* ($\obs = \Val{full}$). As Yudkowsky and Soares note, this problem is decision-theoretically isomorphic to **Parfit's hitchhiker problem** (Parfit 1986), where a lie-detecting driver rescues an agent from the desert (worth $\$1{,}000{,}000$) if and only if she predicts the agent will pay $\$1{,}000$ upon safely reaching the city ($\obs = \Val{city}$), as well as **the mechanical blackmail problem** (Soares and Fallenstein 2015), where a predictor launches a mutually destructive $\$1{,}000{,}000$ defamation program if and only if she predicts the agent will pay $\$1{,}000$ upon receiving the blackmail notice ($\obs = \Val{blackmail}$).

In the transparent Newcomb problem, both Eve (EDT) and Carl (CDT) condition on $\Obs = \Val{full}$ when they see a full Box B. Once $\Obs = \Val{full}$ is conditioned upon, $\Var{Box B} = \Val{full}$ is fixed with probability $1$, so both $\EE[\VV \mid \Act = \act, \Obs = \Val{full}]$ and $\EE[\VV \mid \Do(\Act = \act), \Obs = \Val{full}]$ yield $\$1{,}001{,}000$ for $\Val{twobox}$ versus $\$1{,}000{,}000$ for $\Val{onebox}$. Predictably, Eve and Carl two-box, so the predictor leaves Box B empty (and leaves them to die in Parfit's desert).

Now consider how Fiona (**A-FDT**) models the transparent Newcomb problem. Because there are two possible observations, $\mathcal{X} = \{\Val{full}, \Val{empty}\}$, her graph $G^F$ (depicted in Figure 5b of the source paper) contains two logical decision nodes: $\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full})$ and $\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{empty})$. Crucially, the predictor cares only about what Fiona will do if she sees a full box, so $\Var{Prediction}$ is a child of $\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full})$ and $\Var{Accurate}$, while $\Act$ is a multiplexer controlled by $\Var{Prediction}$ (which determines $\Var{Box B}$ and thus which observation Fiona receives):

$$\begin{aligned}
\Var{Prediction} &= \begin{cases} \Val{1} & \text{if } \left(\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) = \Val{onebox} \land \Var{Accurate} = \Val{accurate}\right) \\ & \quad \lor \left(\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) = \Val{twobox} \land \Var{Accurate} = \Val{inaccurate}\right) \\ \Val{2} & \text{otherwise} \end{cases} \\
\Var{Box B} &= \begin{cases} \Val{full} & \text{if } \Var{Prediction} = \Val{1} \\ \Val{empty} & \text{if } \Var{Prediction} = \Val{2} \end{cases} \\
\Act &= \begin{cases} \Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) & \text{if } \Var{Prediction} = \Val{1} \\ \Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{empty}) & \text{if } \Var{Prediction} = \Val{2} \end{cases}
\end{aligned}$$

Suppose Fiona stands in front of the boxes and observes $\obs = \Val{full}$. By Equation (4), she does *not* condition $P^F$ on $\Obs = \Val{full}$. Instead, she evaluates $\operatorname{A-FDT}(P^F, G^F, \Val{full})$ by intervening on the node $\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full})$:

$$\operatorname{A-FDT}(P^F, G^F, \Val{full}) = \argmax_{\act \in \{\Val{onebox}, \Val{twobox}\}} \EE\left(\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) = \act\right)\right)$$

*(Technical note on the source text: In Section 6 of the reference paper, the unnumbered display formula on the page discussing the transparent Newcomb problem contains a typographical error—a stray `, \Obs=\Val{full}` and an unclosed parenthesis inside $\Do(\dots)$—and a few lines below misprints $\$10{,}010$ as `\$110,00`. However, the authors explicitly emphasize in Section 5, Section 6, and Section 9 that Fiona does not condition on her observation, and the exact probability weights in their calculation follow Equation (4) without conditioning on $\Obs = \Val{full}$, as we verify below.)*

Let $q = P^F(\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{empty}) = \Val{twobox})$ be Fiona's prior probability that she two-boxes upon seeing an empty box. Evaluating the two interventions under Equation (4):
* **Hypothetical 1:** $\Do(\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) = \Val{onebox})$. With probability $0.99$ ($\Var{Accurate} = \Val{accurate}$), $\Var{Prediction} = \Val{1}$, so $\Var{Box B} = \Val{full}$, Fiona executes $\Act = \Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) = \Val{onebox}$, and she receives $\$1{,}000{,}000$. With probability $0.01$ ($\Var{Accurate} = \Val{inaccurate}$), $\Var{Prediction} = \Val{2}$, so $\Var{Box B} = \Val{empty}$, Fiona's action is governed instead by $\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{empty})$, and she receives $q \cdot \$1{,}000$ in expectation. Total expected utility:
  $$\EE\left[\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) = \Val{onebox}\right)\right] = 0.99(\$1{,}000{,}000) + 0.01(q \cdot \$1{,}000) = \$990{,}000 + \$10q$$
* **Hypothetical 2:** $\Do(\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) = \Val{twobox})$. With probability $0.01$ ($\Var{Accurate} = \Val{inaccurate}$), $\Var{Prediction} = \Val{1}$, so $\Var{Box B} = \Val{full}$, Fiona executes $\Act = \Val{twobox}$, and she receives $\$1{,}001{,}000$. With probability $0.99$ ($\Var{Accurate} = \Val{accurate}$), $\Var{Prediction} = \Val{2}$, so $\Var{Box B} = \Val{empty}$, Fiona's action is governed by $\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{empty})$, and she receives $q \cdot \$1{,}000$ in expectation. Total expected utility:
  $$\EE\left[\VV \;\middle|\; \Do\left(\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full}) = \Val{twobox}\right)\right] = 0.01(\$1{,}001{,}000) + 0.99(q \cdot \$1{,}000) = \$10{,}010 + \$990q$$

For every $q \in [0, 1]$, $\$990{,}000 + \$10q > \$10{,}010 + \$990q$. Therefore, Fiona one-boxes even while looking directly at $\$1{,}000{,}000$ in Box B. Even though she knows in fact that Box B is full, when she counterfactually imagines $\Var{a-fdt}(\underline{P^F}, \underline{G^F}, \Val{full})$ outputting $\Val{twobox}$, she imagines a hypothetical universe in which the predictor predicted two-boxing and left Box B empty $99\%$ of the time, routing her physical self to the $\Val{empty}$ observation branch instead. By evaluating her options from this "global perspective," Fiona acts exactly as CDT and EDT agents wish they could precommit to act, never assigns negative expected value to information, pays the driver in Parfit's hitchhiker problem, and refuses extortion in the mechanical blackmail problem.

### 3.3 Death in Damascus and Adversarial Prediction

What happens when a predictor uses its prediction to *harm* the agent regardless of what she chooses? In **Death in Damascus** (Gibbard and Harper 1978), Death perfectly predicts whether the agent will stay in $\Val{damascus}$ or pay $\$1{,}000$ to ride a camel to $\Val{aleppo}$, and meets her at her chosen destination (costing her life, worth $\$1{,}000{,}000$).

In CDT, Carl treats Death's location as causally independent of $\Act$. If Carl believes he will stay in Damascus, CDT tells him to flee to Aleppo; if he believes he will flee to Aleppo, CDT tells him to stay in Damascus. Even if Carl uses a ratification procedure (such as Joyce 2012) to settle into a mixed subjective belief where $P^C_*(\Val{damascus}) = 0.5005$ and $P^C_*(\Val{aleppo}) = 0.4995$, his CDT hypotheticals evaluate each option as if Death's location were uncorrelated with his choice—causing him to hallucinate a $\ge 50\%$ survival probability ($0.5005 \times \$1{,}000{,}000 - \$1{,}000 = \$499{,}500$ expected utility) and refuse to pay $\$1$ for a genuinely random quantum coin that would actually give him a $50\%$ chance of escaping Death (worth $\$500{,}000 - \$1$ vs. CDT's imagined $\$500{,}500$ baseline).

In **A-FDT**, Fiona's graph $G^F$ sets both $\Act = \Var{a-fdt}(\underline{P^F}, \underline{G^F})$ and $\Var{DeathLocation} = \Var{a-fdt}(\underline{P^F}, \underline{G^F})$. Intervening with $\Do(\Var{a-fdt}(\underline{P^F}, \underline{G^F}) = \Val{damascus})$ yields $\$0$ (certain death, no travel cost), whereas $\Do(\Var{a-fdt}(\underline{P^F}, \underline{G^F}) = \Val{aleppo})$ yields $-\$1{,}000$ (certain death, plus $\$1{,}000$ travel cost). Without any loop or ratification ritual, Fiona immediately stays in Damascus—and if offered a genuinely random coin for $\$1$, she gladly buys it because her graph shows that a physical randomizer severs Death's predictive edge and raises her true survival rate from $0\%$ to $50\%$.

---

## 4. Applying A-FDT to Unfamiliar Cases: Open Questions and an Operational Recipe

While Yudkowsky and Soares demonstrate what Equation (4) prescribes once a graph $G$ is given, a researcher or engineer seeking to apply **A-FDT** to a novel problem immediately confronts three questions that the source paper leaves open. Let us carefully separate what follows directly from the source text from the additional operational assumptions we propose to resolve these ambiguities.

### 4.1 Open Question 1: How to Construct the Subjunctive Graph $G$

In Section 5, Yudkowsky and Soares explicitly acknowledge that while Pearl (2000) provides a rigorous methodology for deducing *causal* graphs from observation and experiment, *"no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence. Equation (4) works given a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing."*

**Operational Proposal (The 4-Step Graph Construction Recipe):** To make **A-FDT** applicable to unfamiliar cases, we propose the following structured modeling protocol that extends standard causal modeling into an **A-FDT** model $(P, G)$:

1. **Specify the Causal Backbone and Observation Space:** First, write down the standard physical/causal DAG over environmental states, exogenous noise variables, the agent's observation variable $\Obs \in \mathcal{X}$, the physical action $\Act \in \mathcal{A}$, and utility $\VV$.
2. **Introduce Observation-Indexed Logical Nodes:** For each possible observation $\obs' \in \mathcal{X}$ that the agent might receive in the dilemma, introduce a root logical node $\Lambda_{\obs'} \coloneqq \Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs'})$ taking values in $\mathcal{A}$. Remove any incoming edges to $\Act$ from the agent's internal disposition, and replace $\Act$ with the deterministic multiplexer structural equation:
   $$\Act\left(\Obs, \{\Lambda_{\obs'}\}_{\obs' \in \mathcal{X}}\right) \coloneqq \Lambda_{\Obs}$$
3. **Route Algorithmic Dependencies to Predictors and Replicators:** Inspect every other decision-maker, predictor, or physical process $Y$ in the environment. Ask: *Does the mechanism generating $Y$ simulate, copy, or predict the focal agent's response to some observation $\obs'$?*
   * If $Y$ is a purely physical or statistical common cause (like the smoking lesion or the termite infestation in the XOR blackmail problem), do **not** add an edge from any $\Lambda_{\obs'}$ to $Y$. (If $Y$ alters the agent's preferences or beliefs prior to observation, index the logical nodes by those preference states, as in $\Var{a-fdt}(\underline{P_S}, \underline{G})$ vs. $\Var{a-fdt}(\underline{P_R}, \underline{G})$.)
   * If $Y$ relies on a prediction or symmetrical copy of what the agent does upon observing $\obs'$, draw a directed edge $\Lambda_{\obs'} \to Y$ and write the structural equation for $Y$ in terms of $\Lambda_{\obs'}$ and the predictor's accuracy/noise variables.
4. **Assign Off-Path Priors and Execute Equation (4):** Given the actual observation $\obs \in \mathcal{X}$, assign subjective prior probabilities $P(\Lambda_{\obs'} = \act)$ for all *unreached* observation branches $\obs' \neq \obs$ (which can be computed recursively by solving $\operatorname{A-FDT}(P, G, \obs')$ if the agent knows her own preferences at $\obs'$, or left as a credal parameter $q$ under self-ignorance). Finally, compute $\EE[\VV \mid \Do(\Lambda_{\obs} = \act)]$ for each $\act \in \mathcal{A}$ by propagating $\Lambda_{\obs} = \act$ through the structural equations of $G$, and select the action $\act$ that maximizes this expectation.

### 4.2 Worked Example on an Unfamiliar Case: The Audited Resource-Sharing Game

To see how a reader can use this 4-step procedure to decide an unfamiliar problem, consider a novel dilemma that combines a common-cause confounder, a predictor-driven observation gate, and a symmetric twin interaction:

> **Dilemma (The Audited Resource-Sharing Game):** An agent and her psychological twin (who uses the exact same decision procedure) are each assigned to manage a server during either a $\Val{high}$ or $\Val{low}$ solar-flare state ($\Var{Flare} \in \{\Val{high}, \Val{low}\}$, with prior probability $P(\Var{Flare} = \Val{high}) = 0.5$). If $\Var{Flare} = \Val{high}$, both servers suffer $\$100{,}000$ in unavoidable hardware damage. Before the agent acts, an automated Auditor—which knows $\Var{Flare}$ and predicts with $90\%$ accuracy ($\Var{Acc} = 1$ with probability $0.9$, $0$ with probability $0.1$) how the agent reacts to an audit—decides whether to send an official audit alert ($\Obs = \Val{alert}$) or remain silent ($\Obs = \Val{quiet}$). Specifically, the Auditor sends $\Val{alert}$ to both twins if and only if *either* $\Var{Flare} = \Val{high}$ *or* the Auditor predicts the agent will $\Val{share}$ bandwidth upon seeing $\Val{alert}$.
>
> Upon seeing $\Obs \in \{\Val{alert}, \Val{quiet}\}$, the agent and her twin simultaneously choose $\Act \in \{\Val{share}, \Val{hoard}\}$:
> * Sharing costs the agent $\$1{,}000$, while receiving shared bandwidth from the twin yields $+\$5{,}000$.
> * Furthermore, if the Auditor sent $\Val{alert}$ because it predicted $\Val{share}$ during a $\Val{low}$ flare state, the Auditor awards a $\$10{,}000$ compliance bonus to the agent regardless of her final action.
>
> Suppose the agent receives $\Obs = \Val{alert}$. Should she $\Val{share}$ or $\Val{hoard}$?

Notice why this case is tricky: receiving $\Val{alert}$ is correlated with the catastrophic $\$100{,}000$ solar flare, *and* the $\$10{,}000$ compliance bonus is already causally fixed once $\Val{alert}$ is sent. Let us apply our 4-step **A-FDT** recipe:

* **Steps 1 & 2 (Variables and Logical Nodes):** We have exogenous variables $\Var{Flare} \sim \text{Bernoulli}(0.5)$ and $\Var{Acc} \sim \text{Bernoulli}(0.9)$. Since $\mathcal{X} = \{\Val{alert}, \Val{quiet}\}$, we introduce $\Lambda_{\Val{alert}} = \Var{a-fdt}(\underline{P}, \underline{G}, \Val{alert})$ and $\Lambda_{\Val{quiet}} = \Var{a-fdt}(\underline{P}, \underline{G}, \Val{quiet})$.
* **Step 3 (Structural Equations):** Neither the agent nor the Auditor controls $\Var{Flare}$, so $\Var{Flare}$ has no incoming edges from $\Lambda_{\Val{alert}}$. The Auditor's prediction of $\Lambda_{\Val{alert}}$ is $\Var{Pred} = \Lambda_{\Val{alert}}$ if $\Var{Acc} = 1$ and $\neg \Lambda_{\Val{alert}}$ if $\Var{Acc} = 0$. The observation and bonus structural equations are:
  $$\Obs = \begin{cases} \Val{alert} & \text{if } \Var{Flare} = \Val{high} \lor \Var{Pred} = \Val{share} \\ \Val{quiet} & \text{otherwise} \end{cases}$$
  $$\Var{Bonus} = \begin{cases} \$10{,}000 & \text{if } \Var{Flare} = \Val{low} \land \Var{Pred} = \Val{share} \\ \$0 & \text{otherwise} \end{cases}$$
  Because the twin executes the exact same algorithm and receives the same $\Obs$, both the agent's action $\Act$ and the twin's action $\Act_{\text{twin}}$ obey the multiplexer $\Act = \Act_{\text{twin}} = \Lambda_{\Obs}$. Thus, when $\Obs$ is realized, the net coordination payoff is $\$5{,}000 - \$1{,}000 = +\$4{,}000$ if $\Lambda_{\Obs} = \Val{share}$, and $\$0$ if $\Lambda_{\Obs} = \Val{hoard}$.
* **Step 4 (Off-Path Priors and Equation (4) Evaluation):** Let $q = P(\Lambda_{\Val{quiet}} = \Val{share})$ be the prior probability of sharing when $\Obs = \Val{quiet}$. (In fact, at $\Obs = \Val{quiet}$ the twin still matches $\Lambda_{\Val{quiet}}$, so $q = 1$, giving $+\$4{,}000$ on the quiet branch, or $+\$4{,}000q$ for general $q$.) Now evaluate $\Do(\Lambda_{\Val{alert}} = \act)$ unconditionally across the four states of $(\Var{Flare}, \Var{Acc})$:
  1. **Under $\Do(\Lambda_{\Val{alert}} = \Val{share})$:**
     * $\Var{Flare} = \Val{high}$ (prob $0.5$): $\Obs = \Val{alert}$ regardless of $\Var{Acc}$. Damage is $-\$100{,}000$, $\Var{Bonus} = \$0$, and since $\Obs = \Val{alert}$, both twins execute $\Lambda_{\Val{alert}} = \Val{share}$ for $+\$4{,}000$.
     * $\Var{Flare} = \Val{low}, \Var{Acc} = 1$ (prob $0.45$): $\Var{Pred} = \Val{share}$, so $\Obs = \Val{alert}$, $\Var{Bonus} = +\$10{,}000$, and both twins execute $\Lambda_{\Val{alert}} = \Val{share}$ for $+\$4{,}000$.
     * $\Var{Flare} = \Val{low}, \Var{Acc} = 0$ (prob $0.05$): $\Var{Pred} = \Val{hoard}$, so $\Obs = \Val{quiet}$, $\Var{Bonus} = \$0$, and both twins execute $\Lambda_{\Val{quiet}}$ for $+\$4{,}000q$.
     * **Total Expected Utility ($\Val{share}$):**
       $$0.5(-\$96{,}000) + 0.45(\$14{,}000) + 0.05(\$4{,}000q) = -\$48{,}000 + \$6{,}300 + \$200q = -\$41{,}700 + \$200q$$
  2. **Under $\Do(\Lambda_{\Val{alert}} = \Val{hoard})$:**
     * $\Var{Flare} = \Val{high}$ (prob $0.5$): $\Obs = \Val{alert}$, damage is $-\$100{,}000$, $\Var{Bonus} = \$0$, and both twins execute $\Lambda_{\Val{alert}} = \Val{hoard}$ for $\$0$.
     * $\Var{Flare} = \Val{low}, \Var{Acc} = 1$ (prob $0.45$): $\Var{Pred} = \Val{hoard}$, so $\Obs = \Val{quiet}$, $\Var{Bonus} = \$0$, and both twins execute $\Lambda_{\Val{quiet}}$ for $+\$4{,}000q$.
     * $\Var{Flare} = \Val{low}, \Var{Acc} = 0$ (prob $0.05$): $\Var{Pred} = \Val{share}$, so $\Obs = \Val{alert}$, $\Var{Bonus} = +\$10{,}000$, and both twins execute $\Lambda_{\Val{alert}} = \Val{hoard}$ for $\$0$.
     * **Total Expected Utility ($\Val{hoard}$):**
       $$0.5(-\$100{,}000) + 0.45(\$4{,}000q) + 0.05(\$10{,}000) = -\$50{,}000 + \$1{,}800q + \$500 = -\$49{,}500 + \$1{,}800q$$

Subtracting the two expectations, $\Val{share}$ beats $\Val{hoard}$ by $\$7{,}800 - \$1{,}600q > 0$ for every $q \in [0, 1]$ (and specifically by $\$6{,}200$ when $q = 1$). Notice how cleanly **A-FDT** disentangles the three effects: (i) the $-\$100{,}000$ solar flare is held invariant at probability $0.5$ rather than misattributed as evidential "bad news" of sharing; (ii) the $+\$4{,}000$ twin-cooperation gain is captured on the $\Obs = \Val{alert}$ branches; and (iii) the updateless intervention accounts for the $0.45$ probability shift from $\Obs = \Val{quiet}$ to $\Obs = \Val{alert}$ that unlocks the $+\$10{,}000$ compliance bonus.

### 4.3 Open Question 2: Action Iteration (A-FDT) vs. Policy Iteration (P-FDT)

In Footnotes 7 and 16, Yudkowsky and Soares remark that in their preferred formalization of functional decision theory—which we may call **Policy Functional Decision Theory (P-FDT)**—the agent intervenes on a single algorithm node to select an entire *policy* $\pi : \mathcal{X} \to \mathcal{A}$ (a mapping from observations to actions) and then outputs $\pi(\obs)$, rather than intervening separately on the observation-specific action node $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs}) = \act$ as in Equation (4). They state that *"the difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."*

Why does this distinction matter mathematically, and when do **A-FDT** and **P-FDT** diverge?
In **A-FDT** (Equation (4)), when the agent observes $\obs$, she intervenes *only* on $\Lambda_{\obs} = \Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs})$, while holding the nodes $\Lambda_{\obs'}$ for all counterfactual observations $\obs' \neq \obs$ fixed at their prior distributions in $P$. This local decomposition works whenever the payoff on the $\Lambda_{\obs}$ branches is separable from the choices on the $\Lambda_{\obs'}$ branches, or when each $\Lambda_{\obs'}$ has a unique self-ratifying optimum that does not trade off against $\Lambda_{\obs}$.

However, consider a game—either a single-agent problem with a holistic predictor or a multi-agent coordination game with asymmetric information—where a predictor's action or a twin's payoff depends *jointly and non-separably* on the pair $(\Lambda_{\obs_1}, \Lambda_{\obs_2})$. For example, suppose an agent observes a fair coin toss $\Obs \in \{\Val{H}, \Val{T}\}$ and chooses $\Act \in \{\Val{0}, \Val{1}\}$, and a predictor awards $\$1{,}000$ to the agent if and only if the agent's decision function outputs the *same* action on both $\Val{H}$ and $\Val{T}$ (i.e., $\Lambda_{\Val{H}} = \Lambda_{\Val{T}}$), while the agent also gets a tiny $+\$1$ bonus for matching the coin ($\Act = \Val{1}$ on $\Val{H}$, $\Act = \Val{0}$ on $\Val{T}$).
* Under **P-FDT**, the agent compares all four policies $\pi \in \{\Val{0}, \Val{1}\}^{\{\Val{H}, \Val{T}\}}$ simultaneously and selects the constant policy $\pi(\Val{H}) = \pi(\Val{T}) = \Val{1}$ (or $\Val{0}$), securing $\$1{,}000.50$ in expectation.
* Under **A-FDT** (Equation (4)), if the agent observes $\Val{H}$ and evaluates $\Do(\Lambda_{\Val{H}} = \act)$ while holding $\Lambda_{\Val{T}}$ fixed at the independent optima of each local branch ($\Lambda_{\Val{H}} = \Val{1}$ and $\Lambda_{\Val{T}} = \Val{0}$, or a $50/50$ prior $q = 0.5$), neither local intervention can coordinate the two branches simultaneously unless $\Lambda_{\Val{H}}$ and $\Lambda_{\Val{T}}$ are coupled in $G$.

**Operational Resolution:** When using Equation (4) in a dilemma where a predictor or twin conditions on the agent's behavior across *multiple* information states $\obs_1, \obs_2 \in \mathcal{X}$ simultaneously, the modeler can bridge **A-FDT** and **P-FDT** within Equation (4) by coarsening the decision variable at the decision stage into a policy tuple $\act = (\act_{\obs_1}, \act_{\obs_2}) \in \mathcal{A}^{\mathcal{X}}$ and projecting the physical action via $\Act = \act_{\Obs}$.

### 4.4 Open Question 3: The Scope of "Fair" Dilemmas

Finally, in Section 9, Yudkowsky and Soares note that no decision theory can dominate all rivals in *unfair* dilemmas—such as a mind-reader who scans the agent's source code and punishes anyone implementing **A-FDT**, or rewards only agents who follow "alphabetical decision theory." They conjecture that **A-FDT** matches or outperforms all rival theories in *"fair problems"*—informally defined as dilemmas where the agent's beliefs are accurate and external predictors base their actions only on predictions of the agent's *behavior in the dilemma at hand*, rather than directly rewarding or punishing the syntax of the agent's decision procedure or her behavior in unrelated dilemmas. Formalizing an exact mathematical invariance criterion for "fairness" (for instance, requiring that the environment's structural equations factor through behavioral equivalence classes of the agent's input-output map in the current game) remains an active frontier of decision-theoretic research.

---

## 5. Conclusion

**Action Functional Decision Theory (A-FDT)**, as formalized by Equation (4) of Yudkowsky and Soares (2017), achieves a synthesis long thought impossible in the foundations of rational choice. By shifting Pearl's $\Do$-intervention from the physical action token $\Act$ to the observation-indexed logical output $\Var{a-fdt}(\underline{P}, \underline{G}, \underline{\obs})$—and by replacing Bayesian conditioning on $\Obs = \obs$ with a shift in the locus of logical intervention—**A-FDT** preserves legitimate algorithmic and predictive dependencies while severing spurious common-cause correlations. The result is a single, time-consistent decision rule that cooperates with twins, one-boxes in standard and transparent Newcomb problems, smokes in the smoking lesion problem, pays the driver in Parfit's hitchhiker problem, resists blackmail, and remains reflectively stable against adversarial predictors. While foundational questions remain regarding the automated discovery of subjunctive graphs and the interplay between action-level and policy-level interventions, the structural-equation recipe developed here equips researchers with a rigorous procedure for applying **A-FDT** across decision theory, game theory, and artificial intelligence.

---

## References

* Cohen, Daniel (1990). "On What Cannot Be." In *Truth or Consequences: Essays in Honor of Nuel Belnap*, 123–132. Kluwer Academic Publishers.
* Dai, Wei (2009). "Towards a New Decision Theory." *LessWrong*, August 13, 2009.
* Drescher, Gary L. (2006). *Good and Real: Demystifying Paradoxes from Physics to Ethics*. MIT Press.
* Gibbard, Allan, and William L. Harper (1978). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, Vol. 1, 125–162. D. Reidel.
* Joyce, James M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
* Joyce, James M. (2012). "Regret and Instability in Causal Decision Theory." *Synthese* 187 (1): 123–145.
* Kleene, Stephen Cole (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic* 3 (4): 150–155.
* Nozick, Robert (1969). "Newcomb's Problem and Two Principles of Choice." In *Essays in Honor of Carl G. Hempel*, 114–146. D. Reidel.
* Parfit, Derek (1986). *Reasons and Persons*. Oxford University Press.
* Pearl, Judea (1996). "Causation, Action, and Counterfactuals." In *Proceedings of the 6th Conference on Theoretical Aspects of Rationality and Knowledge (TARK-96)*, 51–73.
* Pearl, Judea (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
* Peirce, Charles Sanders (1934). *Collected Papers of Charles Sanders Peirce, Vol. V: Pragmatism and Pragmaticism*. Harvard University Press.
* Skyrms, Brian (1980). *Causal Necessity: A Pragmatic Investigation of the Necessity of Laws*. Yale University Press.
* Soares, Nate, and Benja Fallenstein (2015). "Toward Idealized Decision Theory." *arXiv preprint arXiv:1507.01986*.
* Yudkowsky, Eliezer (2010). *Timeless Decision Theory*. Technical Report, The Singularity Institute.
* Yudkowsky, Eliezer, and Nate Soares (2017). "Functional Decision Theory: A New Theory of Instrumental Rationality." *arXiv preprint arXiv:1710.05060v2*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Defining the Scope**

I'm now focusing on defining the scope for this explanation of Action Functional Decision Theory. The goal is to create a technical explanation, probably in essay or blog post form. I am keeping in mind the need for practical application to real-world decision-making problems. I need to make sure the target audience is clear to define scope, but an expert audience is presumed.


**Clarifying Key Elements**

I've been drilling down on the essential components. The research role is clearly defined as crafting a mathematical essay for an informed audience. I'm homing in on Action Functional Decision Theory (A-FDT) as the core subject, specifically focusing on Equation (4) from the paper. This will serve as the primary formal representation. The naming convention, A-FDT, is solidified for consistency.


**Refining Content Scope**

I'm now zeroing in on the content requirements. My goal is to craft a coherent account, including mathematical definitions and examples. The essay needs to be precise enough to guide decisions in unfamiliar cases, exploring how A-FDT evaluates actions, addressing dependencies and counterfactuals (subjunctive dependence, counterpossibles, and logical interventions), and clarifying open questions and implementation details left open in the original paper.


**Defining Uncertainties & Scope**

I'm now focusing on the open questions within the source material. I need to address the ambiguities related to constructing the subjunctive dependency graph, formalizing counterpossibles, and defining "fair" problems. I'll also develop a clear, operational interpretation of these areas, making sure to distinguish between the source's claims and my own interpretations. The target word count is approximately 2,400–3,000 words for the mathematical essay, which will include a brief conclusion. My motivation is the conflict between Evidential and Causal Decision Theories.


**Analyzing A-FDT's Performance**

I am now delving into evaluating A-FDT's behavior in classic decision theory problems. I've noted its undesirable outcomes in scenarios like Newcomb's problem and the Psychological Twin Prisoner's Dilemma, alongside the failures of CDT and EDT in problems like Parfit's Hitchhiker. My primary focus is understanding why. I'm especially interested in analyzing the core A-FDT idea of treating decisions as outputs of a fixed mathematical function, and exploring how it tackles subjunctive dependence and the complex area of counterpossibles.


**Formalizing Key Concepts**

I am now focusing on A-FDT's mathematical formalization, specifically Equation 4, and the notation. I aim to make this core equation perfectly clear to the reader. To that end, I am clarifying the differences between CDT and A-FDT. I need to emphasize the point of intervention (type vs. token). My next step is to examine the implications of the conditioning operator to capture subjunctive dependencies in a Pearl-style DAG, including the re-use of Pearl's $\Do(\cdot)$ operator.


**Elaborating on Updatelessness**

I'm now zeroing in on A-FDT's method of handling observations, which doesn't involve conditioning on them. Instead, the observation impacts which logical node is intervened upon: $\FDTvar(\underline{P}, \underline{G}, \underline{\obs})$. The reason is that in problematic examples, the observation is downstream of the predictor's forecast of $\FDTvar(\underline{P}, \underline{G}, \underline{\obs})$. Conditioning would lock the past and destroy the counterfactual link between output and probability. This is crucial for problems like Transparent Newcomb.


**Clarifying Graph Construction**

I'm now focusing on how the subjunctive graph, $G$, is constructed, as this is a key open question. I'm proposing a "computational-causal synthesis" rule to define an operational principle for defining the structural modularity, in contrast with Pearl's methods. I'm also planning to clarify a key typo in the paper concerning conditional expectation, which is not being used as the paper claims. I am also planning on explaining how Fiona's strategy is computed.



**Defining Graph Construction**

I am now focusing on the practical construction of (P, G). I'm looking at representing physical causal mechanisms using standard structural equations. I'm identifying agents and introducing logical nodes for each possible observation. I'm exploring the routing of edges into the focal agent's conditional action mechanism, alongside the predictor's representation of that conditional response. I am focusing on constructing the graph, given the source material.


**Analyzing Multiple Observation Nodes**

I'm now analyzing scenarios where predictors or twins base their actions on outputs from *multiple* observation nodes, not just one. I'm mathematically exploring the sufficiency of A-FDT in these cases and how to address unreached-branch priors, like the parameter $q$. I am also now working on the paper's outline and structure, with a word count between 2600-2800.


**Examining Functional Dependencies**

I'm now diving into the functional dependencies within A-FDT, especially focusing on how Equation 4 operates. I'm carefully contrasting it with EDT and CDT's expected utility frameworks. I'm clarifying the distinction between Pearl's interventions and A-FDT's type-level interventions. My goal is to elaborate on these concepts, emphasizing the logical type interventions in the context of subjunctive dependence and counterpossibles, and examining the impact of using $\Do$ on an augmented DAG. I'm aiming for clarity in describing the formalism.


**Analyzing Decision Dynamics**

Now, I'm focusing on the mathematical mechanics of $(P, G)$ and structural equations, aiming to show how A-FDT calculations work in classic problems, particularly in Newcomb's problem and the Smoking Lesion case. I'm demonstrating how the model can be used to capture the advantage of smoking in the Smoking Lesion. I'll also explore the mechanics behind transparent Newcomb and Parfit's Hitchhiker problems.


**Analyzing Counterfactual Worlds**

I'm now zeroing in on *Mechanical Blackmail* and contrasting it with *Death in Damascus*. In Mechanical Blackmail, I'm working through the specific calculations to show how the multiplexer functions when there is an observation. I need to explain the counterfactual world where the observation itself changes. Next, I am going to analyze why A-FDT is stable in Damascus, even though CDT is unstable in this situation.


**Proposing Practical Construction**

I'm now formulating a 4-step procedure for building $(P, G)$ in new decision problems. This operational plan defines (1) a Physical/Causal Backbone; (2) Information-State Multiplexing for $\Act$; (3) Algorithmic Dependency Routing for predictors/twins/future selves; and (4) Off-Path Prior Specification. Next, I plan to analyze the differences between A-FDT's local action interventions and policy optimization. I'll mathematically assess divergence scenarios, and I will be developing a diagnostic method for users.


**Refining the Evaluation**

I'm now refining my mathematical calculations for specific scenarios like Newcomb's problem. I am checking the numerical details and ensuring accuracy in how A-FDT evaluates the outcomes. I have identified a typo in the original paper's calculations for Eve's expected value, correcting it to $990,000 to match the paper's claims. My focus is now on ensuring the precision of all numerical examples.


**Calculating Expected Utility**

I'm now calculating expected utilities in Transparent Newcomb's problem, focusing on the numerical values. I've re-examined the paper's claims, especially the EU for one-boxing, and I'm updating my calculations to be completely precise. I am currently working to express it with an equation to express the value, including the variable $q$.


**Calculating Action Utility**

I'm now in the thick of calculating Action Functional Decision Theory (A-FDT)'s expected utility in a new scenario. I'm taking the previous calculations and applying them to an *unfamiliar case* (or a fresh worked example), so the reader sees the operational procedure. I need to make sure this new worked example shows the user exactly how to use A-FDT.


**Demonstrating Operational Usage**

I'm now designing a worked example, the "Asymmetric Audit Dilemma," to illustrate A-FDT's 4-step procedure in action. I'll meticulously detail how to use the framework, including an observation, predictor, and a confounding variable. This new example will directly show how to apply A-FDT in an unfamiliar scenario, aiming for practical clarity.


```
