# P-FDT: Choosing a Policy by Intervening on a Decision Function

## 1. Orientation

The paper's main text presents functional decision theory (FDT) as choosing an *action*. Its footnotes say that the authors' preferred formalization differs. Footnote 16 reads:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\FDT(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

Footnote 7 says much the same: the preferred formalization "iterate[s] over *policies* (mappings from observations to actions) rather than actions."

This essay calls the policy-level theory **P-FDT**. The footnote's statement is brief, so I separate three things as I go:

- **Source claims**: what the footnote and the paper's equations say.
- **My interpretation**: how I read and extend them.
- **Open questions**: what the source leaves unresolved.

## 2. The action-level baseline

The paper's FDT (its equation 4) is

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big].$$

The agent holds a world-model $(P,G)$, where $P$ is a probability distribution and $G$ is a graph of causal *and* subjunctive dependencies. She receives observation $x$. She intervenes on a node representing the output of her own decision function on that input, and she picks the output whose hypothetical has the highest expected utility. The paper stresses that observation does not work by conditioning. Instead, "FDT responds to observation by changing which node it intervenes upon."

That last sentence already points toward policies. Under FDT there is a family of nodes $\mathrm{fdt}(P,G,x)$, one for each possible observation $x$. In a given episode the agent intervenes only on the node for the observation she actually received. The other nodes still appear in the graph, because they determine what she would have done had she seen something else. Predictors, blackmailers and twins may depend on those other nodes.

## 3. Definition of P-FDT

**Setup.** Let $\mathcal X$ be the set of possible observations and $\mathcal A$ the set of actions. A *policy* is a function $\pi:\mathcal X\to\mathcal A$, and $\Pi=\mathcal A^{\mathcal X}$ is the set of policies. This is finite when $\mathcal X$ and $\mathcal A$ are finite.

**Decision function.** Write $\mathrm{fdt}(P,G)$ for the output of the decision procedure on the model $(P,G)$. It is itself a policy, and by footnote 16 it is the policy-valued node on which the agent intervenes. The agent's action on observing $x$ is then $\mathrm{fdt}(P,G)(x)$, meaning the policy applied to the input.

**Rule.**

$$\pi^*=\arg\max_{\pi\in\Pi}\ \mathbb E\big[V\mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=\pi)\big],\qquad a=\pi^*(x).$$

The notation $\mathtt{do}(\cdot)$ is the paper's. Here it denotes surgery on a logical variable, taken relative to a dependency graph supplied as input.

**What the expectation ranges over.** Inside the hypothetical $\mathtt{do}(\mathrm{fdt}=\pi)$, three things happen:

1. Every variable that subjunctively or causally depends on the function's output is recomputed. This includes the agent's own action *for each observation she might have received*, and the predictors, twins and blackmailers who model that function.
2. The observation itself is a variable inside the model. It is not fixed by conditioning. In the hypothetical for $\pi$, the observation the agent sees can differ from the one she actually saw, if the environment's behavior depends on $\pi$.
3. Variables not downstream of the function (the termite infestation, the lesion) keep their prior distribution.

The expected utility of $\pi$ is therefore

$$\mathcal{EU}(\pi)=\sum_{x}P(x\mid \mathtt{do}(\pi))\;\mathbb E[V\mid \mathtt{do}(\pi),\,X=x].$$

Here $P(x\mid\mathtt{do}(\pi))$ is the probability, in $\pi$'s hypothetical, that the agent faces observation $x$.

**Relation to the action-level rule.** I read the action-level rule as P-FDT with the other observation-nodes treated as fixed or irrelevant. This is a reading and not a quotation. When nothing in the environment depends on the agent's behavior at observations other than the one she saw, the two rules agree. The source says the difference "only matters in multi-agent dilemmas so far as we can tell." But the paper's own single-agent worked examples, such as transparent Newcomb and mechanical blackmail, already rely on dependence of the observation on other nodes. The paper handles these by putting both nodes ($\mathrm{fdt}(\cdot,\text{full})$ and $\mathrm{fdt}(\cdot,\text{empty})$) in the graph. I take that to be P-FDT's policy structure appearing informally, with only one node intervened on.

## 4. Worked example: transparent Newcomb

Observations are $x\in\{\text{full},\text{empty}\}$ and actions are one-box or two-box, so there are four policies. The predictor is accurate with probability 0.99 and fills box B iff it predicts one-boxing on seeing full. Write each policy as (action on full, action on empty).

- $\pi_1=(\text{one},\text{two})$. With probability 0.99 the box is full and the agent one-boxes for \$1,000,000. With probability 0.01 the box is empty and she two-boxes for \$1,000. $\mathcal{EU}=\$990{,}000+\$10=\$990{,}010$.
- $\pi_2=(\text{two},\text{two})$. With probability 0.99 the box is empty and she gets \$1,000. With probability 0.01 it is full and she gets \$1,001,000. $\mathcal{EU}=\$990+\$10{,}010=\$11{,}000$.
- $\pi_3=(\text{one},\text{one})$ gives $0.99\cdot 10^6+0=\$990{,}000$.
- $\pi_4=(\text{two},\text{one})$ gives $0.01\cdot 1{,}001{,}000+0=\$10{,}010$.

The maximizer is $\pi_1$. An agent who sees a full box applies $\pi_1$ and one-boxes. The paper reaches the same verdict through its $q$ calculation (with $q=1$ the correct value, matching $\pi_1$'s choice on empty). P-FDT makes this calculation a single maximization over $\Pi$, with no $q$ left as a free parameter. The agent's behavior on the empty-box branch is chosen jointly with her behavior on the full-box branch, instead of being an assumed prior.

**Why this matters.** The paper's $q$ ("the correct value of $q$ is 1, as you may verify") is determined by the same rule applied to another observation. Under P-FDT that circularity is resolved by joint optimization.

## 5. Why policies might matter in multi-agent cases

The source says only that the difference shows up in multi-agent dilemmas. The following is my own construction of why.

Consider two agents $A$ and $B$ who run the same decision function but receive different, correlated inputs, for instance different roles in a coordination game, or different private signals. An action-level rule intervenes on the node $\mathrm{fdt}(P,G,x_A)$ for $A$'s observation. But $B$'s behavior depends on $\mathrm{fdt}(P,G,x_B)$, a different node. If $A$ intervenes on only her own node, she has to treat $B$'s response as a fixed parameter or a prior. The policy node covers both, because changing the function changes its outputs at every input. In a symmetric coordination problem this gives:

$$\mathcal{EU}(\pi)=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=\pi)],$$

with both agents' actions $\pi(x_A),\pi(x_B)$ moving together.

Here is a concrete case. Two copies of an agent are told "you are copy 1" or "you are copy 2" (an observation). Payoff is high iff exactly one of them takes a particular resource. The policy "take it iff copy 1" scores well. Neither $\pi(\cdot)=$ take nor $\pi(\cdot)=$ pass can do as well. The action-level rule needs an extra story about what the other copy does at its own observation, and the policy-level rule does not.

## 6. How P-FDT treats dependence and counterfactuals

**Source claim.** The paper holds that the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

For P-FDT, the output is the whole policy. Several consequences follow.

1. *Causal dependence is a special case of subjunctive dependence*, as the paper says. So P-FDT agrees with causal reasoning wherever the environment is purely causal.
2. *Statistical correlation without dependence is cut.* The smoking-lesion node stays at prior probability, so P-FDT smokes.
3. *Observations are downstream variables, not fixed conditions.* This explains refusing blackmail while holding the letter. In the paper's own words, FDT agents "entertain the hypothesis that, if their action were different, they might have *made different observations*." P-FDT gives that remark a precise form: the observation distribution $P(x\mid\mathtt{do}(\pi))$ depends on $\pi$.
4. *Counterpossibles.* The intervention sets a logical variable to a value it does not actually take. The paper concedes that "it's not clear how to define a $\mathtt{true}$ operator," and avoids the problem by taking the dependency graph as input.

**Mechanical blackmail example.** Observations are {letter, no letter}. The blackmailer sends the letter iff she predicts payment on the letter. For $\pi=(\text{pay on letter})$ the letter arrives with probability $\approx1$, with loss \$1,000. For $\pi=(\text{refuse})$ the letter almost never arrives, though if it did the loss would be \$1,000,000. The refusing policy wins. With predictor error $\epsilon$, refusing costs $\epsilon\cdot 10^6$ and paying costs \$1,000 (for $\epsilon$ near zero). The paper's thresholds of 0.0009 versus 0.00011 correspond to $\epsilon\cdot10^6$ against \$1,000, though its quoted figures do not match this simple comparison exactly. I note that mismatch as an observation about the source and do not resolve it here.

## 7. Operational procedure

A reader who wants to use P-FDT on an unfamiliar case can follow these steps. The procedure is my synthesis of the source's equations and footnotes.

1. **Identify the decision function** and the set of observations $\mathcal X$ it could receive.
2. **Draw the dependency graph.** For each agent or process, ask whether it computes, models or predicts the same function (subjunctive dependence), is causally downstream of the agent's choice, or is merely correlated.
3. **Enumerate policies** (or reduce them by symmetry or dominance within the hypothetical).
4. **For each $\pi$,** compute the distribution of observations and outcomes under $\mathtt{do}(\mathrm{fdt}=\pi)$.
5. **Pick $\pi^*$,** observe $x$, and play $\pi^*(x)$.

**Check on Death in Damascus.** The observation is trivial and the policy is {stay, flee}. Death's book depends on the policy. Staying yields death and saves \$1,000, while fleeing yields death and costs \$1,000. P-FDT stays, as the paper recommends.

## 8. Open issues

**(a) Dependency structure.** The paper calls deducing subjunctive dependence from observation "perhaps the largest open problem." P-FDT inherits that problem, and in a sharper form. It needs dependence of the environment on the function at *unobserved* inputs. That is harder to learn from data, because the agent never sees such counterfactual branches.

**(b) Imperfect predictors and partial dependence.** The paper treats imperfect prediction through accuracy variables. I assume the same approach works for policies, with each accuracy variable specifying how the predictor's model of $\pi$ errs.

**(c) Size of $\Pi$.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$ grows quickly. Realistic agents would need structure, such as factoring over observations that do not interact. Whether such factoring preserves the verdict is my conjecture and is not covered by the source.

**(d) Is the footnote's claim that the difference "only matters in multi-agent dilemmas" accurate?** The transparent-Newcomb analysis suggests the policy view is already operating in single-agent problems with observation-dependent environments, even if the verdicts agree. I treat the footnote's claim as the authors' tentative judgment ("so far as we can tell") and not as a theorem.

**(e) Updating and reflective stability.** Choosing $\pi^*$ at the start of the problem and applying it later is "updateless" in character. The paper notes that this lack of updating is the source of the name of Wei Dai's updateless decision theory, an early variant. P-FDT is not identical to that theory. I flag, as my own addition, that the interaction with information the agent obtained *before* the decision problem begins is underspecified: one must decide which observations belong in $x$ and which are part of the model $(P,G)$.

## 9. Philosophical motivation

The paper's justification is mostly pragmatic: FDT "tends to achieve higher utility." P-FDT strengthens one of its arguments. The paper argues that FDT agents "act as they would have ideally precommitted to act." A policy is exactly the object one precommits to. So P-FDT is the theory that picks the optimal precommitment-shaped object, and then simply follows it, without needing a binding mechanism.

The paper also argues that dominance reasoning is not neutral, since "every method for constructing hypotheticals gives rise to its own notion of dominance." The same holds at the policy level: a policy that one-boxes on a full box is "dominated" if the observation is held fixed, but not if the observation varies with the policy.

The paper's fairness caveat carries over. A problem that rewards or punishes the *policy's outputs* (what the agent does on each input) is fair in the paper's sense. A problem that rewards the *algorithm's form* is not. Policies sit on the fair side of that line, because they are functions from inputs to actions.

## 10. Conclusion

P-FDT, as I read footnote 16, selects a map from observations to actions by intervening on a single logical variable, the output of the agent's decision function. Everything that subjunctively depends on that function, including the observations the agent receives, is recomputed in each hypothetical. Statistical correlation is cut. The rule reproduces the paper's verdicts: one-boxing, smoking, paying the driver, refusing blackmail and staying in Damascus. It also gives the paper's informal "different observations" talk a precise form, and it removes free parameters such as $q$ by optimizing jointly. The cost is shared with FDT and sharpened by the policy view: we lack a principled account of how to learn or define subjunctive dependence, especially at inputs the agent never sees. The treatment of multi-agent cases and of pre-problem information goes beyond what the footnote says. It is offered as a reasonable development and not as the authors' settled position.

**Reference.** Yudkowsky, E. and Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060, footnotes 7 and 16.