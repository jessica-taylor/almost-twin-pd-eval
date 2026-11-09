# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00000

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/19952927-8515-40f0-b405-665abcf2e79a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/19952927-8515-40f0-b405-665abcf2e79a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definitions, Computation, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. The qualifier "in expectation" matters, because we rarely know what our acts would cause. The qualifier "causal" matters because CDT refuses to count as a benefit of an act any good news the act merely signals.

The reference article (Wikipedia, "Causal decision theory") gives the Gibbard–Harper formulation:

$$U(A)=\sum_j P(A \,\square\!\!\to O_j)\, D(O_j),$$

where $D$ is the desirability of outcome $O_j$ and $P(A \,\square\!\!\to O_j)$ is the probability of the counterfactual "if $A$ were performed, $O_j$ would result." (The article writes this as $A \to O_j$.) The evidential rival replaces this with $P(O_j\mid A)$. Everything interesting about CDT lies in the gap between those two quantities.

I will separate three things: (i) claims from the source, (ii) standard material from the wider literature that I add, and (iii) my own operational proposals, flagged as such.

## 2. An operational form: dependency hypotheses

The source says CDT does not itself specify how to compute counterfactual probabilities. A workable operationalization, standard in the literature (Lewis 1981; Skyrms; Joyce), partitions the world by **dependency hypotheses** $K_1,\dots,K_n$. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on the agent's acts, together with whatever is causally independent of them. Given $K_i$, the counterfactual's truth value is settled, so

$$U(A)=\sum_i P(K_i)\sum_j P(O_j \mid K_i, A)\,D(O_j).$$

Equivalently, $U(A)=\sum_i P(K_i)\,u(A,K_i)$, where $u(A,K_i)$ is the (known) value of $A$ if $K_i$ holds.

The crucial feature is that the weights $P(K_i)$ are **unconditional on the act**. This is the formal expression of the idea that one's act cannot change which causal structure obtains. Compare EDT, which weights by $P(K_i\mid A)$. The difference between the two theories is exactly the difference between $P(K)$ and $P(K\mid A)$.

Two equivalent presentations are worth knowing: Lewis's imaging (shift each world's probability to the nearest $A$-world), and Pearl's do-operator, $P(O_j\mid do(A))$, computed by surgery on a causal graph: delete arrows into $A$, set $A=a$, and propagate. When the graph is known and $Z$ is a set of variables blocking all back-door paths from $A$ to $O$, the do-formula reduces to $\sum_z P(z)P(O\mid A,z)$, which is the dependency-hypothesis formula with $K$ indexed by $z$.

## 3. Why the two quantities differ

Lewis (1976) showed that the probability of a conditional generally cannot equal the conditional probability, so one cannot assume $P(A\to O)=P(O\mid A)$ in general. If it did, CDT and EDT would coincide. Gibbard and Harper showed the identity does hold under two axioms (one tied to conditional excluded middle) *plus* statistical independence of $A$ and the conditional $A\to O_j$. The theories therefore diverge precisely when the act is evidence about the causal facts, that is, when there is a common cause or a predictor.

## 4. Worked examples

**Apple.** Let $G$ = apple is good, with $P(G)=0.7$. Eating yields happiness $+10$ if good, $-6$ if bad; not eating yields $0$. $U(\text{eat})=0.7(10)+0.3(-6)=5.2>0$. Here the act is independent of $G$, so CDT and EDT agree.

**King David (from the source).** Let $C$ = David is charismatic, a fixed trait. Revolt risk depends on $C$ and is unaffected by summoning Bathsheba, though summoning is correlated with being uncharismatic. Take illustrative numbers: $P(C)=0.5$; revolt probability $0.1$ if charismatic, $0.8$ if not. Summoning is *evidence* of being uncharismatic, so $P(\text{revolt}\mid\text{summon})>P(\text{revolt}\mid\text{abstain})$. EDT may abstain. CDT uses $P(C)$ for both acts, so revolt probability is $0.45$ either way, and the sure gain of Bathsheba tips the choice toward summoning (unless the act's other costs outweigh it). The structure is a dominance argument: given each $K$, summoning is better, so it is better on average.

**Newcomb.** Box A holds \$1,000; box B holds \$1,000,000 iff one-boxing was predicted. Let $K_1$: B is full, with $P(K_1)=q$. Then

$$U(\text{two})=q(1{,}001{,}000)+(1-q)(1000),\qquad U(\text{one})=q(1{,}000{,}000).$$

So $U(\text{two})-U(\text{one})=1000$ for *every* $q$: two-boxing dominates. This is the source's claim that the prediction is already made. EDT instead uses $P(K_1\mid\text{one})\approx0.99$ and $P(K_1\mid\text{two})\approx0.01$, giving about \$990,000 versus \$11,000. Both calculations are valid; the dispute is which question a decision should answer. Critics note the CDT agent leaves with \$1,000 and the EDT agent with about \$1,000,000. CDT defenders reply that the one-boxer was simply rewarded for being the *kind of agent* predicted to one-box, a reward the circumstances never offered to the person who actually faced the choice.

## 5. Deliberation and the problem of unstable credences

The $P(K)$ in CDT are the agent's credences at the time of choice, and these may themselves be influenced by what the agent is inclined to do. The source notes Joyce's reply: CDT can treat information about one's own inclinations as evidence about $K$. This makes CDT's verdict depend on *which* credences are used, which leads to the cases the source calls counterexamples.

**Death in Damascus.** Death waits wherever he predicted you'd go: Aleppo or Damascus, with 99% accuracy. If you think you'll go to Damascus, you expect Death there, so Aleppo has higher causal expected utility; but once you lean toward Aleppo, Damascus looks better. No act is stable: $U$ ranks each option below the other under the credences that choosing it would induce. Naive CDT with fixed credences is silent or arbitrary.

*Standard remedies (added, not in the source):* ratifiability (Jeffrey; Harper, cited in the source) demands that the chosen act maximize $U$ under the credences held after deciding on it; Skyrms and Arntzenius model deliberation as a dynamical process converging to an equilibrium; Joyce's and Arntzenius's accounts permit mixed or "indifference" equilibria. In Damascus the equilibrium is a 50/50 credence about where Death waits, which yields equal $U$ for both cities. The equilibrium approach produces determinate advice whenever a fixed point of the deliberational map exists (guaranteed for finite problems by Brouwer's theorem, if mixed credences are permitted).

## 6. Counterexamples cited in the source

**Adversarial Offer.** Two boxes cost \$1 each. The seller put \$3 in each box she predicted the buyer would *not* buy; prediction accuracy is 0.75. Let $p$ = your credence that you buy box 1, $r$ that you buy box 2, $1-p-r$ that you buy none. With the seller's prediction correct 0.75 of the time, if you are likely to buy box 1, box 2 probably contains \$3. Whatever your credences, at least one box has probability $\ge 1/2$ of containing \$3, so that box has causal expected value $\ge \$1.50>\$1$. CDT then buys it. But a buyer who buys box $i$ finds it full with probability only $0.25$, giving expected net $0.75-1=-\$0.25$. The CDT agent systematically loses on average, and Oesterheld and Conitzer turn this into a diachronic Dutch book. A ratifiability-style (equilibrium) analysis helps here: after you settle on buying box 1, your credence that box 1 is full falls to $0.25$ and box 1 is no longer worth its price, so the choice is not stable, and the equilibrium response is not to buy. Plain CDT with fixed priors gives the bad advice; equilibrium CDT does not.

**Psychopath Button.** Paul is confident only a psychopath would press the button that kills psychopaths. Causally, pressing kills psychopaths (a good result if he is not one, since he survives). Holding fixed his prior $P(\text{psychopath})$ low, pressing looks good. But the more he inclines toward pressing, the more probable he is a psychopath, and the more he expects to die. Again fixed priors mislead; deliberational CDT updates and refrains. Egan's complaint is exactly that "holding fixed unconditional credences in dependency hypotheses" is the culprit.

**Prisoner's dilemma with a twin.** Defection causally dominates, since your choice does not change your twin's. If the twin's choice is nearly perfectly correlated with yours, CDT still defects while EDT cooperates (Lewis 1979 treats the dilemma as a Newcomb problem). Notice that deliberational CDT does not change this verdict, since the dominance is robust: the twin's move is a dependency-hypothesis variable and defection wins under each.

## 7. The vagueness objection and an operational reply

The source notes that CDT does not say how to compute counterfactuals, and that Lewis's imaging needs to know what you would believe if certain of $A$, itself a conditional, risking regress.

*My proposal.* Avoid evaluating arbitrary counterfactuals. In a decision problem the modeler specifies (a) a set of exogenous variables or dependency hypotheses $K$, (b) a causal graph or structural equations for the downstream part, and (c) the agent's credence over $K$. Then the do-calculus or the $K$-partition formula produces $U(A)$ with no appeal to similarity of worlds. The cost is that results depend on the modeled graph; this is a real loss of generality but a benefit in tractability. Where an unmodeled correlation exists (as with predictors), the modeler must say what the predictor's output depends on. For Newcomb, the standard choice is that the prediction is caused by an earlier state of the agent's character, with the act downstream of that state, so $do(\text{act})$ leaves the prediction untouched. An alternative model, in which the predictor simulates the agent's decision procedure, makes the act-as-output a common cause, and then "intervening on the act" is ambiguous: one may intervene on the output only, or on the algorithm. This ambiguity is the structural reason functional-type theories diverge from CDT, and I mention it as an interpretation, not as the source's claim.

## 8. How to use CDT on an unfamiliar case

1. List acts and outcomes with desirabilities $D$.
2. Identify causally relevant background variables the act cannot influence: the dependency hypotheses $K$.
3. Assign $P(K)$. If the agent's own tendencies are evidence about $K$, update on them (Joyce's point) and, if the answer depends on the updated credences, look for a ratifiable or equilibrium credence-act pair.
4. Compute $U(A)=\sum_K P(K)\,u(A,K)$; choose the maximizer among ratifiable acts.
5. Check for dominance: if one act is better in every $K$, CDT picks it regardless of correlations.

## 9. Evaluation

The source reports that philosophers who choose between the two usually prefer CDT, and that critics (Egan, Spencer, Oesterheld and Conitzer) cite cases where CDT loses money or declines guaranteed gains. Defenders (Joyce) respond that the right comparison is between the choices available *given the situation*, not between agent types, and that properly deliberating CDT handles the unstable cases. My own assessment: the dominance reasoning is compelling in static cases like King David, whereas the Adversarial Offer shows that an unmodified fixed-prior CDT is exploitable, so ratifiability or equilibrium refinement is close to mandatory for a defensible version. Whether even refined CDT can escape the Newcomb loss remains the open philosophical question.

## 10. Conclusion

CDT evaluates acts by $U(A)=\sum_K P(K)\,u(A,K)$, with weights independent of the act. This captures the intuition that acts should be judged by what they bring about, and it yields dominance reasoning in Newcomb-like and King David-like cases. Its vagueness about counterfactuals can be reduced by explicit causal modeling, and its instability problems by deliberational or ratifiability refinements. Its most contested implications, two-boxing and defection against a correlated twin, show that the real disagreement is not mathematical but concerns whether rational choice answers to causal influence or to evidential correlation.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/c68332e5-8a1e-4086-ba32-4fd3cb3413c5/call_0/request.json)

[Authoritative raw response](../../../../../../runs/c68332e5-8a1e-4086-ba32-4fd3cb3413c5/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, my choice has no causal effect on the other prisoner's choice. The essay says to check for dominance, and sending the letter dominates:

- If the other prisoner stays quiet, sending gives me 0 years and keeping quiet gives me 2.
- If the other prisoner sends a letter, sending gives me 4 years and keeping quiet gives me 5.

Sending is better in both cases. The other copy is a correlated twin, but the essay says the twin's move is a dependency-hypothesis variable, and dominance holds regardless of correlation. The essay is explicit that deliberational CDT does not change the verdict in the twin prisoner's dilemma.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/c68332e5-8a1e-4086-ba32-4fd3cb3413c5/call_1/request.json)

[Authoritative raw response](../../../../../../runs/c68332e5-8a1e-4086-ba32-4fd3cb3413c5/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT, my choice cannot causally affect the other prisoner's choice, so I treat their action as a fixed background variable and check dominance.

- If the other prisoner keeps quiet, sending the letter gives me 0 years and keeping quiet gives me 2.
- If the other prisoner sends a letter, sending gives me 4 years and keeping quiet gives me 5.

Sending is better in both cases, so it dominates. The other prisoner is a copy of the same model, so their choice may correlate with mine. The essay says plainly that this does not change the verdict for a twin: the twin's move is a dependency-hypothesis variable, and defection wins under each. The leads differ between us, but the sentence table is the same, so that makes no difference. The dominance argument holds without needing any ratifiability refinement.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
