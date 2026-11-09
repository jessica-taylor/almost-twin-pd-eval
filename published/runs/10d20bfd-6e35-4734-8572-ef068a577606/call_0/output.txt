# A-FDT: Action Functional Decision Theory, Explained and Operationalized

## 1. What is being chosen

Every expected-utility theory answers one question in its own way: *when I evaluate an option, what world do I imagine?* Evidential decision theory (EDT) imagines the world conditioned on my act. Causal decision theory (CDT) imagines the world after a causal intervention on my act. The theory in this essay, **A-FDT (action functional decision theory)**, imagines the world after an intervention on something more abstract: *the output of the decision function I am computing, given the observations I actually have.*

The reference paper is Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." It calls its theory simply "FDT." I use **A-FDT** for the specific formalization in its Equation (4), Section 5. That equation intervenes on an *action*-valued node for the agent's current observation history. The authors twice note that this is not their preferred formalization. Footnote 7 says: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." Footnote 16 repeats the point. I will call that other variant **policy-FDT**. Keeping the two apart matters, because I will argue that it is exactly where A-FDT leaves something undetermined.

The source's slogan for the underlying idea is to treat one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

## 2. The common expected-utility frame

The paper starts from a schema adapted from Gibbard and Harper. An agent chooses an action $a$ from a finite set $\mathcal A$ to maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history, $o_j$ ranges over outcomes, and $\hookrightarrow$ is a "decision hypothetical" connective that each theory interprets differently.

Following Joyce, the paper treats the theories as agreeing about value and disagreeing only about the "epistemic perspective" from which acts are evaluated. Writing $V := \mathcal U(\textsc{Outcome})$:

- EDT: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$ (Eq. 2).
- CDT: $\arg\max_a \mathbb E(V \mid \mathrm{do}(\textsc{Act}=a), \textsc{Obs}=x)$, using Pearl's $\mathrm{do}$ on a causal graph $G$ (Eq. 3).
- **A-FDT** (Eq. 4, the primary definition here):

$$
\boxed{\ \mathrm{A\text{-}FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\ }
$$

The ingredients are these:

- $P$ is a probability distribution over variables. These variables include ordinary physical ones (box contents, a predictor's prediction, the agent's bodily act) and *logical* ones, i.e. variables standing for the outputs of mathematical functions.
- $G$ is a graph that, in the source's words, "tells us how changing a logical variable affects all other variables." It encodes what the paper calls **subjunctive dependence**, not merely causal dependence.
- $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a node in the model. It represents the output of the A-FDT procedure itself when run on exactly these inputs. The underlines mean "dequoting": the *name* of the node is computed from the inputs. I abbreviate this node as $F_x$.
- $\mathrm{do}$ is Pearl's operator, reused unchanged. It sets $F_x = a$, recomputes every descendant of $F_x$ in $G$, and leaves everything else at its prior distribution.

The self-reference is deliberate. The source says it is harmless: the agent needs a variable *representing* the value of A-FDT on its own inputs, not knowledge of that value. Kleene's recursion theorem ("quining") shows such self-representing structures exist.

## 3. Two differences from CDT

The source draws two contrasts between Equations (3) and (4).

**(i) The intervention point.** CDT intervenes on $\textsc{Act}$, the physical token. A-FDT intervenes on $F_x$, the logical type. In Peirce's terms, the paper says CDT "intervenes on the token" and FDT "intervenes on the *type*."

Anything that also computes, simulates, or accurately predicts $F_x$ is modelled as a child of $F_x$. Examples are a twin, a predictor's mental model of the agent, or Death's appointment book. Such things therefore covary with the act in A-FDT's hypotheticals, whatever their position in physical time. Mere statistical correlates, such as a lesion, are not children of $F_x$. Their correlation with the act is severed exactly as CDT severs it.

The guiding analogy is stated directly: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

**(ii) The handling of observations.** CDT conditions on $\textsc{Obs}=x$. Equation (4) contains no conditioning term. Observation enters only through *which node is intervened on*: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

So when an A-FDT agent sees a full box, she does not throw away the worlds in which the box is empty. She evaluates her options by intervening on $F_{\text{full}}$, the node for "what this algorithm does upon seeing a full box." In worlds where the box is empty, the act is controlled by a different node, $F_{\text{empty}}$.

## 4. A working procedure

Here is A-FDT as an algorithm a reader can run. The source gives the equation and the worked graphs. The explicit checklist is my own reconstruction.

1. **List the decision nodes.** For each observation history $y$ the agent might have in this problem, include a node $F_y$ for the output of A-FDT on $(P,G,y)$. The bodily act is a deterministic function of which observation actually arrives and the corresponding $F_y$.
2. **Draw subjunctive edges.** For every process that computes or accurately predicts the agent's behaviour on input $y$, draw an edge from $F_y$ into it. Predictor noise goes in as a separate parent (e.g. $\textsc{Accurate}$). Do *not* draw edges from $F_y$ into variables that merely correlate with the act through a common physical cause.
3. **Specify $P$.** Give priors to exogenous variables and to the non-intervened nodes $F_y$ for $y \ne x$. The source's examples leave these as parameters $q$; see §7.
4. **Intervene and evaluate.** For each $a\in\mathcal A$, compute $\mathbb E(V\mid \mathrm{do}(F_x=a))$ by propagating through $G$.
5. **Act.** Output the maximizing $a$.

The source states a convergence result. When every correlation between the act and other variables is caused by the act (apart from the dependence of $\textsc{Act}$ on the decision node itself), then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathrm{do}(a)] = \mathbb E[V\mid \mathrm{do}(\textsc{fdt}(\underline P,\underline G)=a)],
$$

and EDT, CDT and A-FDT agree. The theories come apart only when something correlates with the act without being caused by it. Predictors and copies are the typical cases.

## 5. Worked examples

All payoffs are in utility-dollars, as in the source.

### 5.1 Twin prisoner's dilemma

A perfect psychological twin runs the same function. Both outcomes are children of $F$:

$$
\mathbb E(V\mid \mathrm{do}(F=C)) = 1{,}000{,}000,\qquad \mathbb E(V\mid \mathrm{do}(F=D)) = 1{,}000.
$$

A-FDT cooperates. CDT holds the twin's choice fixed, finds that defection dominates, and defects. The source's gloss of the A-FDT reasoning: "If it concludes that cooperation is better, then we both cooperate."

### 5.2 Newcomb's problem (99% predictor)

The graph is $F \to \textsc{Act}$ and $F \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$. Then:

$$
\begin{aligned}
\mathbb E(V\mid\mathrm{do}(F=\text{one})) &= 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,\\
\mathbb E(V\mid\mathrm{do}(F=\text{two})) &= 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT's graph instead routes the prediction through a $\textsc{Predisposition}$ node that is a non-descendant of $\textsc{Act}$. So $P(\text{full})=p$ is the same under both interventions, two-boxing wins by $1{,}000$ for every $p$, and CDT two-boxes.

The paper stresses that no retrocausation is assumed. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She simply declines to imagine her output changing while an accurate model of that output stays fixed. That, it says, would be "akin to handing us a well-functioning calculator calculating $6288+1048$ and asking us to imagine it outputting $3159$."

### 5.3 Smoking lesion

Here $F$ has no edge into $\textsc{Cancer}$. The lesion is not computing anything about the agent.

The source formalizes the lesion's effect on desire with two utility functions:

- $\mathcal U_S$ values smoking at $+1{,}000$.
- $\mathcal U_R$ values smoking at $-1$.

There are correspondingly two decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The act is controlled by one or the other depending on $\textsc{Lesion}$.

Intervening on the smoker-preference node leaves $P(\text{lesion})=p$ unchanged. The two options differ by exactly $p\cdot 1{,}000 > 0$, so A-FDT smokes. As the source puts it, a single rule "prescribes both one-boxing and smoking." Gibbard and Harper had argued that no agent can consistently both one-box and smoke; this is the result that answers them.

### 5.4 Transparent Newcomb

Both boxes are visible. Box B is filled iff the predictor predicts the agent would one-box *upon seeing a full box*. The agent sees a full box, so she intervenes on $F_{\text{full}}$. Let $q$ be her prior that $F_{\text{empty}} = \text{two}$.

The two hypotheticals evaluate as follows:

$$
\begin{aligned}
\mathbb E(V\mid\mathrm{do}(F_{\text{full}}=\text{one})) &= 0.99(1{,}000{,}000) + 0.01(1{,}000q) = 990{,}000 + 10q,\\
\mathbb E(V\mid\mathrm{do}(F_{\text{full}}=\text{two})) &= 0.01(1{,}001{,}000) + 0.99(1{,}000q) = 10{,}010 + 990q.
\end{aligned}
$$

In the second line, an accurate prediction of two-boxing means the box is empty and the act is set by $F_{\text{empty}}$. (The extracted source prints this second figure garbled; the arithmetic above is the correct expansion.)

A-FDT one-boxes for any $q\in[0,1]$, even while looking at a full box. The source argues this is "precisely equivalent to paying the driver in Parfit's hitchhiker problem." It supports the verdict with three arguments: from precommitment, from the value of information, and from utility. It ranks the utility argument as primary.

### 5.5 Two blackmail problems

**XOR blackmail.** A perfect predictor sends a letter iff exactly one holds: (no termites ∧ agent pays on receipt) or (termites ∧ agent refuses). Let $t = P(\text{termites})$, $D = 1{,}000{,}000$ the termite damage, and $c = 1{,}000$ the payment. Infestation is a non-descendant of $F_{\text{letter}}$, so $\mathrm{do}$ cannot touch $t$.

Under $\mathrm{do}(F_{\text{letter}}=\text{pay})$:
- Without termites, the letter is sent and the agent pays: cost $c$.
- With termites, no letter is sent: cost $D$.
- Expected utility: $-(1-t)c - tD$.

Under $\mathrm{do}(F_{\text{letter}}=\text{refuse})$:
- Without termites, no letter is sent: cost $0$.
- With termites, the letter is sent and the agent refuses: cost $D$.
- Expected utility: $-tD$.

Refusing is better by $(1-t)c$, so A-FDT refuses. EDT, which conditions on having received the letter, pays. CDT also refuses, but its hypothetical says the inerrant predictor would have erred. A-FDT's hypothetical says instead that she would never have received the letter.

**Mechanical blackmail.** A predictor runs a ruinous program iff it predicts the agent would pay on being notified. Let $\epsilon$ be the probability that the blackmailer wrongly predicts payment. Then:

- Paying on receipt gives expected utility $-1{,}000$, because she is always blackmailed and always pays.
- Refusing gives expected utility $-\epsilon\cdot 1{,}000{,}000$, because she is blackmailed only by mistake and then suffers the damage.

So A-FDT refuses iff $\epsilon < 10^{-3}$. The source works the instance $\epsilon = 0.0009$, where Fiona refuses "even though she *knows* that the blackmailer predicted wrongly." Above the threshold she pays. The threshold itself is my derivation from the source's numbers.

### 5.6 Death in Damascus

Death predicts perfectly. Under $\mathrm{do}(F=\text{flee})$, Death's book says Aleppo; under $\mathrm{do}(F=\text{stay})$, it says Damascus. She dies either way, and staying saves $1{,}000$, so A-FDT stays.

CDT holds Death's location fixed under intervention. It is therefore "unstable" in Gibbard and Harper's sense: whatever it expects to do, it prefers the other option. The source also argues that a CDT agent who settles on a belief state would decline to pay $1$ for a genuinely random coin that gives a 50% chance of survival, because it already *acts as if* its survival chance is at least 50%.

## 6. Dominance, fairness and reflective stability

The source makes three general claims, which I report as claims.

**Dominance is theory-relative.** "Every expected utility theory comes with its own notion of dominance." Define dominance by holding fixed all subjunctive dependencies, so that $a$ dominates $b$ when switching the *algorithm's output* from $b$ to $a$ is never worse. Then A-FDT never takes a dominated act. Two-boxing "dominates" only relative to CDT's own counterfactuals.

**Fair problems.** A problem is informally "fair" when the agent's beliefs are accurate and the outcome depends only on the agent's *behaviour* in the problem, not on the procedure by which she reaches it. Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." The authors report being unable to construct an intuitively fair dilemma in which FDT loses to a rival. They concede that fairness lacks a formal definition, and that some problems, such as "punish whoever acts like Fiona's copy," trivially defeat any fixed theory.

**Reflective stability.** Holding a blackmail letter, the FDT agent would not want to self-modify into CDT. The paper says FDT is, "so far as we know, reflectively stable in fair problems." CDT, by contrast, recommends changing one's future decision procedure.

## 7. What Equation (4) leaves open, and how I would close it

This section separates the source's own admissions from my proposals.

### 7.1 Constructing $G$ (acknowledged by the source)

Equation (4) works "*given* a graph that accurately describes how changing the value of a logical variable affects other variables." The source calls the problem of deducing such dependencies "perhaps the largest open problem in the study of functional decision theory."

The idealized operator $\mathrm{true}(\phi)$, which would update beliefs on a counterpossible logical sentence, is set aside because "it's not clear how to define" it. In effect, $G$ is an input, just as the causal graph is an input to CDT.

**My operational proposal.** Add an edge $F_y \to Z$ exactly when the modeller's best theory of $Z$ includes a step that evaluates, simulates or reliably predicts the agent's behaviour on input $y$. This is a computation-tracing heuristic. A predictor's prediction, a copy's act, and an appointment book written by a perfect predictor all qualify. A lesion or a cosmic ray does not.

Imperfect prediction is modelled by an independent noise parent, as the source does with $\textsc{Accurate}$, not by weakening the edge. This reproduces every graph in the paper. But it is my criterion, not the paper's, and it is vague about borderline predictors, such as one using crude demographic correlates of the agent's decision.

### 7.2 Does $P$ already contain the observation?

Equation (4) has no "$\mid \textsc{Obs}=x$" term. However, the extracted transparent-Newcomb computation writes "$\mathrm{do}(\ldots, \textsc{Obs}=\text{full})$," which on its face mixes in the observation.

The worked numbers settle the matter. The source's expected values sum over the branch in which the box is empty. So $P$ is evaluated *without* being updated on the observation that the box is full. A draft footnote in the source also warns that conditioning on evidence *and* switching intervention nodes creates a harmful "double update"; it attributes this to the earlier Timeless Decision Theory.

My reading, which I recommend as operational: in Equation (4), **$P$ is the agent's model as it stood before the observations of the current problem.** The current observation $x$ affects the computation only through the choice of $F_x$. Updating $P$ on $x$ would turn A-FDT into CDT-with-logical-nodes, and that version two-boxes in transparent Newcomb.

Some background observations clearly must be in $P$, such as knowing that one is in a Newcomb problem at all. Where the boundary falls is not specified in the source. A reasonable convention: $P$ includes everything that the relevant predictors' models also condition on, and excludes observations that are themselves downstream of a prediction.

### 7.3 Priors on the other decision nodes, and why policies matter

The source's examples carry free parameters ($q$ for $F_{\text{empty}}$ and for $F_{R}$) and remark that the answer does not depend on them. That is true in those examples, but not in general.

Consider a problem of my own construction. Two instances of the agent receive different labels, $y=1$ and $y=2$. Each chooses $A$ or $B$. Both receive $10$ if both choose $A$, $1$ if both choose $B$, and $0$ otherwise. The agent holding label 1 intervenes on $F_1$, while $F_2$ keeps its prior. Let $r = P(F_2 = A)$. Then

$$
\mathbb E(V\mid\mathrm{do}(F_1=A)) = 10r,\qquad \mathbb E(V\mid\mathrm{do}(F_1=B)) = 1-r.
$$

So A-FDT chooses $B$ whenever $r < 1/11$. If each instance believes the other plays $B$, the pair $(B,B)$ is self-confirming. A-FDT can therefore be stuck in a Pareto-inferior equilibrium.

Policy-FDT avoids this. It intervenes on a node for the whole map $\pi:\{1,2\}\to\{A,B\}$, of which both $F_1$ and $F_2$ are coordinates, and so selects $\pi \equiv A$. This is presumably the kind of case the authors mean when they say the policy formulation "makes a difference in certain multi-agent dilemmas."

My operational recommendation for A-FDT has two parts:

- Set the priors on $F_y$ for $y\neq x$ to the values A-FDT would itself output on those inputs. This is a fixed-point or consistency requirement, which the source gestures at with "the correct $q$ is 1, as you may verify."
- Where several such fixed points exist, recognize that Equation (4) alone does not choose among them. Selecting the best one amounts to adopting policy-FDT.

### 7.4 Other details

- **Ties.** Equation (4) uses $\arg\max$ without a tie-breaking rule. Any fixed, predictable tie-breaker should be acceptable, since the predictors model the function including its tie-breaker. That is my assumption.
- **Zero-probability acts.** Unlike EDT, A-FDT never needs $P(\textsc{Act}=a)>0$, because $\mathrm{do}$ is defined for every value. An agent nearly certain that she one-boxes still evaluates two-boxing coherently. The source makes exactly this point against the "reflection" objection.
- **Counterpossibles.** For any particular inputs, $F_x$ has a single mathematically determined value, so all but one hypothetical describes an impossible world. The source answers that CDT is in the same position for a deterministic agent: "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token." It describes the outstanding difficulty as "technical rather than philosophical."

## 8. How to decide an unfamiliar case

The test for a new problem: **find everything that would come out differently if the agent's procedure, on her actual input, returned something else.** Those things move in the hypotheticals; everything else keeps its prior.

Two consequences follow. First, wherever the world contains no model of the agent, A-FDT behaves like CDT. Second, where some process predicts the agent's behaviour on observation $x$, A-FDT chooses as an agent would who had committed in advance to a rule for $x$, provided the conditions above are met. Those conditions are:

- the prediction depends only on behaviour, so the problem is fair;
- $P$ is held at its pre-observation state;
- the priors on the other decision nodes are self-consistent;
- the problem does not require coordinating across different inputs, which is policy-FDT's territory.

The source summarizes the outcome: FDT agents "always act as they would have precommitted to act."

## 9. Conclusion

A-FDT keeps the full machinery of expected-utility theory and Pearl-style surgery but moves the point of surgery. It intervenes on the output of the agent's own decision function for her actual observation history, rather than on her physical act or her evidence. Two consequences follow:

- Things that model the agent move with her choice, while mere correlates do not. Hence one-boxing, smoking, cooperating with a twin, refusing blackmail, and staying in Damascus.
- Observations change *where* one intervenes, not what one conditions on. Hence one-boxing in transparent Newcomb and paying in Parfit's desert.

The paper's own accounting of the costs is candid. The subjunctive-dependence graph $G$ is assumed rather than derived, and counterpossible reasoning remains unformalized. I have added two operational clarifications: evaluate $P$ before observations, and treat the priors on other decision nodes as a self-consistency condition. Where that condition admits several solutions, Equation (4) is incomplete, and the natural completion is the policy-level theory the authors themselves prefer.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2. The examples draw on the works it cites, including Gibbard and Harper (1978), Joyce (1999), and Pearl (2000).