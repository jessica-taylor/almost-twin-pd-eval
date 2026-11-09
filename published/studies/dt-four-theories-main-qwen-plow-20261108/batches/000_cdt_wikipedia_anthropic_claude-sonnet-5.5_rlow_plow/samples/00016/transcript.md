# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00016

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/fc915ca7-9bf4-445a-8a05-f1e7c29879ed/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/fc915ca7-9bf4-445a-8a05-f1e7c29879ed/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. The key word is "causal." An act can be correlated with good outcomes without producing them, and CDT tells you to ignore that correlation when evaluating what to do. What matters is what your act would bring about, given your uncertainty about how the world is arranged.

The source article presents this informally (good apple versus bad apple) and then formally via Gibbard and Harper (1981):

$$U(A)=\sum_j P(A \,\square\!\!\to O_j)\, D(O_j),$$

where $D$ is the desirability of outcome $O_j$ and $P(A \square\!\to O_j)$ is the probability of the counterfactual "if $A$ were performed, $O_j$ would result." The article writes the connective as $\to$. I write $\square\!\!\to$ to avoid confusing it with the material conditional. The rule is to pick the $A$ maximizing $U(A)$.

Everything interesting is hidden in the counterfactual probability. This essay explains how to compute it, how it differs from conditional probability, and where the theory is contested.

## 2. Dependency hypotheses: a working operationalization

The source says CDT "does not itself specify" an algorithm for counterfactual probabilities. Here is the standard way to make the formula usable. This decomposition is from the wider literature (Lewis 1981, Skyrms, Joyce) and is not spelled out in the article.

Partition the possibilities into **dependency hypotheses** $K_1,\dots,K_n$. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on your acts, including everything outside your control that bears on the result. Each hypothesis settles which counterfactuals hold: given $K_i$, "if $A$ then $O_j$" has a definite truth value (or definite chance). Then

$$U(A)=\sum_i P(K_i)\sum_j P(O_j\mid A\wedge K_i)\,D(O_j)=\sum_i P(K_i)\,V(A\wedge K_i).$$

Equivalently, $P(A\square\!\to O_j)=\sum_i P(K_i)\,P(O_j\mid A, K_i)$. Contrast this with evidential value:

$$V(A)=\sum_i P(K_i\mid A)\,V(A\wedge K_i).$$

**The entire formal difference is $P(K_i)$ versus $P(K_i\mid A)$.** CDT weights the dependency hypotheses by your credences that do not move when you contemplate the act, whereas EDT lets the act serve as evidence about which hypothesis holds. When $K$ and $A$ are probabilistically independent, the two agree. That is the content of Gibbard and Harper's observation, mentioned in the article, that independence of $A$ and the conditional $A\square\!\to O_j$ (plus two axioms, one tied to conditional excluded middle) yields $P(A\square\!\to O_j)=P(O_j\mid A)$.

Lewis's triviality results show that no single proposition-valued conditional can in general have probability equal to the conditional probability. So the equivalence of CDT and EDT is not automatic, and the dependency-hypothesis decomposition shows precisely where they separate.

## 3. Worked examples

### 3.1 King David and Bathsheba

Let $K_c$ = David is charismatic and $K_u$ = uncharismatic, with $P(K_c)=P(K_u)=\tfrac12$ say. Outcomes: revolt or not, and getting Bathsheba. Revolt is likely under $K_u$ (say 0.8) and rare under $K_c$ (0.1), *regardless of whether David summons her*, since unjust acts do not cause revolt. Summoning is strongly correlated with $K_u$. Let getting Bathsheba be worth $+10$ and a revolt $-100$. Summoning gains 10 in either state, and the revolt probability is the same whether or not he summons.

CDT computes, for summoning $S$ and abstaining $\neg S$:

$$U(S)-U(\neg S) = 10 > 0,$$

because the revolt term is identical in both and cancels. CDT says summon. EDT, using $P(K_u\mid S)$ high, sees $S$ as bad news about revolt, and may well recommend abstaining. The article reports exactly this verdict split.

### 3.2 Newcomb's problem

A predictor with 99% accuracy fills opaque box B with \$1,000,000 iff it predicted you would take only B. Box A holds \$1,000. Let $K_F$ = "B is full" and $K_E$ = "B is empty." These are fixed before you act, so:

$$U(\text{two-box}) = p\cdot 1{,}001{,}000 + (1-p)\cdot 1{,}000,\qquad U(\text{one-box}) = p\cdot 1{,}000{,}000,$$

where $p=P(K_F)$. For every $p$, two-boxing wins by exactly \$1,000, so CDT two-boxes whatever it believes about the predictor. EDT instead uses $P(K_F\mid \text{one-box})=0.99$ and one-boxes, with value about \$990,000 against about \$11,000 for two-boxing.

The CDT defender's reply is that the predictor "rewards irrationality," and that a two-boxer facing a full box does better than a one-boxer facing that same box. The critic's reply is: "if you're so smart, why ain't you rich?" Philosophers remain divided, which the source notes.

## 4. Policies versus acts

The prompt asks about actions *or policies*. Standard CDT evaluates **acts at the moment of choice**. Its evaluation of a policy $\pi$ (a function from situations to acts) is by the same formula with $\pi$ as the "act," but only if $\pi$ is adopted as a present choice whose consequences are causal. This matters because a predictor may have responded to your *disposition* rather than your final act. A CDT agent who can *now* choose to bind itself, for instance by self-modifying into a one-boxer before the prediction, will do so, since the binding act causally influences the prediction. The same agent, once the prediction has been made, will not. This is a source of dynamic inconsistency: CDT recommends adopting policies that CDT, applied later, would reverse. That observation is mine rather than the article's, though it underlies the diachronic Dutch-book arguments that the article attributes to Oesterheld and Conitzer.

## 5. Unstable cases: when your credences depend on your inclination

The source points to Death in Damascus and the Psychopath Button, where a naive CDT calculation goes wrong, and to Joyce's response that CDT can use information about one's own tendencies as evidence. Here is how that works operationally.

**Death in Damascus.** Death predicts your location (Damascus or Aleppo) with high reliability and waits there. Let $q=P(\text{Death in Damascus})$. Staying in Damascus has causal expected utility $-(q)\cdot L$, where $L$ is the loss from meeting Death, and going to Aleppo has $-(1-q)L$. If $q>\tfrac12$ you should go to Aleppo. But if you become confident you will go to Aleppo, your $q$ falls below $\tfrac12$, and then Damascus is better. Every pure choice is *unstable*: once you lean toward it, CDT recommends the other.

Several operational resolutions exist, all additions beyond the article:

1. **Ratifiability** (Harper, Jeffrey): only choose acts that maximize $U$ computed with credences updated on the supposition that you choose them. Here no pure act is ratifiable, but the mixed act with $q=\tfrac12$ is, and any randomization is equally good in expectation. Mixed acts then require that you can actually randomize and that Death cannot predict the outcome of your randomizer.
2. **Deliberational dynamics** (Skyrms, Arntzenius): model deliberation as an iterative process updating $q$ and the act probabilities until equilibrium. The fixed point is $q=\tfrac12$.
3. **Joyce's view**: your credence over $K_i$ at the end of deliberation includes information about your leanings, and CDT is applied to those updated credences. This is the "information about what one is inclined to do as evidence" the article mentions.

The three agree on Death in Damascus, which supports reading CDT not as "hold your *initial* credences fixed" but as "hold fixed your *current, deliberation-adjusted* credences in dependency hypotheses." Egan's critique targets the first reading; Joyce's defense relies on the second.

**Psychopath Button.** Paul believes only psychopaths would press. Let $K_P$ = Paul is a psychopath. Pressing kills all psychopaths, including Paul if $K_P$. A naive CDT agent, with a prior in which $P(K_P)$ is small, finds that pressing probably yields a better world, and presses. But the act of pressing is strong evidence for $K_P$. If the deliberator updates on his own inclination to press, his credence in $K_P$ rises, so pressing looks lethal, and he should refrain. With $u_{\text{die}}\ll u_{\text{psych}}<u_{\text{no psych}}$, the stable credence is the one at which pressing and not pressing have equal $U$. Ratifiability yields the commonly agreed verdict of not pressing, or at most a mixed act at an indifference point.

## 6. Adversarial offers and money pumps

The Adversarial Offer in the article makes the cost of the naive rule concrete. Two boxes cost \$1 each, and the seller puts \$3 in each box she predicted you would not buy. Prediction accuracy is 0.75. Let $b_1, b_2$ be your probabilities of buying box 1 or 2, with $b_0=1-b_1-b_2$.

Causal expected value of buying box $i$ is $3\,P(\text{box } i \text{ filled}) - 1$. The fill probabilities sum to at least 1 (each box is filled unless the seller predicted you buy it, and you buy at most one), so $P_1+P_2\ge 1$ and the better box has $P\ge\tfrac12$, giving value $\ge 3(0.5)-1=0.5>0$. So CDT buys something. But if you buy box $i$, the box is empty with probability 0.75, so your realized expected value is $0.25\cdot 3-1=-0.25$ per purchase.

The resolution available to a ratifiability-style CDT is subtle. Once you are leaning toward buying box 1, you expect it to be empty, so buying box 2 looks better, and the instability repeats. Joyce's updating-based CDT can end at a mixed state in which both boxes have causal expected value near \$1, making you indifferent to buying. Whether that salvages CDT is contested, and Oesterheld and Conitzer argue that the "naive" version is common enough, and the problem robust enough, to expose CDT's costs. I note the calculation above, but its interpretive conclusion is a judgment call.

## 7. The vagueness objection and imaging

The article records the objection that CDT does not specify the counterfactual algorithm. Lewis's *imaging* offers one: to compute $P(A\square\!\to O)$, shift each world's probability mass to the closest $A$-world. Formally, $P^A(w')=\sum_{w:\,w_A=w'}P(w)$, and $P(A\square\!\to O)=P^A(O)$. Imaging differs from conditioning because mass moves to the nearest $A$-worlds rather than being renormalized across all $A$-worlds. The worry in the article is regress: the similarity ordering encodes what you would believe were you certain of $A$, which is itself conditional.

The dependency-hypothesis formulation sidesteps much of this by shifting the burden to specifying a causal model. In a Pearl-style structural model, the counterfactual is evaluated by intervention, $P(O\mid \mathrm{do}(A))$, and

$$U(A)=\sum_j P(O_j\mid \mathrm{do}(A))\,D(O_j).$$

This is a well-defined operational proposal when a causal graph is available (my gloss; the article does not discuss it). It also clarifies Newcomb: $\mathrm{do}(\text{act})$ cuts the arrow from the predictor's state into the act, and the predictor's state is unaffected. The residual questions are how to represent the agent's own decision node, whether "the predictor simulates me" should be modeled as a common cause, and whether the model should include the agent's deliberation, which is precisely where the CDT camps disagree.

## 8. A procedure for unfamiliar cases

1. List the available acts.
2. Identify the outcome-relevant factors that are causally independent of the act, and form dependency hypotheses $K_i$. Include hypotheses about predictors, hidden types, and states of the world fixed before the act.
3. For each act and hypothesis, determine $P(O_j\mid A,K_i)$ by tracing only downstream causal effects of $A$.
4. Assign credences $P(K_i)$. Decide whether these are *prior* credences or *deliberation-adjusted* credences that incorporate evidence about your own leanings. This choice is the main source of divergent CDT verdicts.
5. Compute $U(A)=\sum_iP(K_i)V(A\wedge K_i)$.
6. If the best act changes as your credences update on it, check for ratifiable or equilibrium (possibly mixed) acts.
7. For cases involving commitment, ask whether policies or dispositions can be chosen causally prior to the predictor's action; if so, evaluate that choice with the same machinery.

## 9. Assessment

The article reports that philosophers generally prefer CDT to EDT when forced to choose. The case for CDT is the thought that deliberation should look forward to what your act can change. The case against is that CDT agents appear to lose predictably in Newcomb-like environments, and that naive versions are open to money-pump or Dutch-book constructions. A defender replies that the problems stipulate environments that reward a type of agent, not a type of act, and that sophisticated CDT handles evidence about one's own tendencies.

Two distinctions cut across this debate. One is between claims about acts and claims about agent-types: CDT evaluates the former, and a different criterion (such as "which decision procedure does best across environments") evaluates the latter. The other is between naive and deliberation-sensitive versions of CDT. Many headline counterexamples target only the naive version, while the deeper dispute concerns whether the sophisticated version still gives defensible advice in Newcomb itself, where the credence in the box's contents is not unstable and so no refinement changes the two-box verdict.

## 10. Conclusion

CDT replaces conditional probability with the probability of counterfactuals or interventions, equivalently by holding fixed one's credences over dependency hypotheses while varying the act. Its formal content is compact: $U(A)=\sum_i P(K_i)V(A\wedge K_i)$. Its application demands judgment about causal structure and about whether credences should be updated on one's own inclinations. The theory handles King David and cases of mere correlation cleanly, gives the contested two-box verdict in Newcomb, and faces serious tests in unstable, self-referential problems. Those tests are met only by refinements such as ratifiability, deliberational equilibrium, or Joyce's evidential updating, and whether such refinements are principled or ad hoc remains the central open question.

**References** (as in the source article): Gibbard & Harper (1981); Lewis (1976, 1981); Egan (2007); Joyce (2012); Oesterheld & Conitzer (2021); Weirich, *SEP* "Causal Decision Theory."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/45b573f4-2b7a-456e-aafa-bfead6dfbdf9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/45b573f4-2b7a-456e-aafa-bfead6dfbdf9/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is fixed and my action can't causally affect it. Sending the letter is the dominant act.

- If the other prisoner keeps quiet, sending gives me 0 years and staying quiet gives me 2.
- If the other prisoner sends, sending gives me 4 years and staying quiet gives me 5.

Sending is better in both cases, whatever credence I assign to the other's choice. The essay's refinements for unstable cases don't change this. My credence about the other prisoner may shift because the other execution is a copy of me, but that doesn't make the choice unstable. Sending is the best response at every credence, so it is ratifiable. The correlation with the copy is evidence, and CDT does not let it count as a causal effect of my act.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/45b573f4-2b7a-456e-aafa-bfead6dfbdf9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/45b573f4-2b7a-456e-aafa-bfead6dfbdf9/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, the other prisoner's choice is causally independent of mine, so I treat it as a fixed state of the world. This is a Prisoner's Dilemma with the following payoffs:

- If Rowan keeps quiet, sending the letter gives me 0 years and keeping quiet gives me 2, so sending is better.
- If Rowan sends a letter, sending gives me 4 years and keeping quiet gives me 5, so sending is better again.

Sending the letter strictly dominates for every credence P(K) about Rowan's choice. The essay's complications (instability, ratifiability, the correlation between my copy and me) don't change this. Dominance holds in both states, so the choice is stable and ratifiable. The evidential link to the other copy is not a causal channel and doesn't enter the CDT calculation.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
