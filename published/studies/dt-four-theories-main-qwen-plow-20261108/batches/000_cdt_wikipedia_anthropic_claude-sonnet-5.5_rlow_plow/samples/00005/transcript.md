# 000_cdt_wikipedia_anthropic_claude-sonnet-5.5_rlow_plow / 00005

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c8e7816a-11e8-487a-9485-0048d00922bc/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c8e7816a-11e8-487a-9485-0048d00922bc/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Definitions, Computation, and Where It Strains

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal consequences* are best in expectation. Two questions follow. What is an act's causal consequence, given that we are uncertain about the world? And how do we aggregate over that uncertainty? The source article answers the first with counterfactuals, following Gibbard and Harper (1981):

$$U(A)=\sum_j P(A \,\square\!\!\to O_j)\,D(O_j),$$

where $D(O_j)$ is the desirability of outcome $O_j$ and $P(A \,\square\!\!\to O_j)$ is the probability of the counterfactual "if $A$ were performed, $O_j$ would result." (The source writes the connective as $\to$.) The rational act maximizes $U$.

The contrast is with evidential decision theory (EDT), which uses $V(A)=\sum_j P(O_j\mid A)D(O_j)$. EDT asks what the act is *evidence for*. CDT asks what the act would *bring about*.

## 2. Making the formula usable: dependency hypotheses

The counterfactual formula is hard to apply directly (see §5). The standard workaround, from Lewis (1981) and Skyrms, is not in the source, so I flag it as supplementary. Partition the possibilities into **dependency hypotheses** $K_1,\dots,K_n$. Each is a maximally specific proposition about how outcomes depend causally on the agent's acts, covering everything outside the agent's causal influence. Then

$$U(A)=\sum_i P(K_i)\sum_j P(O_j\mid A, K_i)\,D(O_j).$$

Within a single $K_i$, conditioning on $A$ is harmless, because $K_i$ already fixes the causal structure. The key feature is that the weights are the **unconditional** $P(K_i)$, not $P(K_i\mid A)$. Replacing $P(K_i)$ with $P(K_i\mid A)$ recovers EDT by the law of total probability. So the whole difference between the theories is whether the act is allowed to shift your credence about the causal background. CDT holds that credence fixed. The source cites Egan making exactly this point: CDT holds fixed "the agent's unconditional credences in dependency hypotheses."

In causal-graph language (Pearl), this is $P(O_j\mid do(A))$ computed by intervention. The intervention severs the arrows into $A$, so evidence flowing from $A$ back to its common causes is ignored.

## 3. Why the two theories can differ

Lewis (1976) showed that $P(A\to O)$ cannot in general equal $P(O\mid A)$. If it did, CDT would collapse into EDT. Gibbard and Harper showed that under two axioms (one involving conditional excluded middle), equality holds when $A$ is probabilistically independent of the conditional $A\to O$. Where independence fails, the theories diverge. In the dependency-hypothesis formulation, they diverge exactly when $A$ is evidentially relevant to the $K_i$ without causing them.

**The apple.** Let $K_1$ = good apple, $K_2$ = bad apple. Eating gives happiness $h$ if good and sadness $-s$ if bad. Then $U(\text{eat})=P(K_1)h-P(K_2)s$. Here eating is independent of $K_i$, so CDT and EDT agree.

**King David (Gibbard and Harper).** David may summon Bathsheba, which he values. He fears a revolt. His charisma $C$ (fixed in adulthood) causes both just behavior and resistance to revolt. Summoning her is unjust, but injustice does not itself cause revolt. Suppose, with illustrative numbers of my own, that a revolt costs 10, Bathsheba is worth 3, $P(\text{revolt}\mid C)=0.1$, $P(\text{revolt}\mid\neg C)=0.6$, and $P(C)=0.5$.

CDT takes $K$ = (charismatic or not), holds $P(C)=0.5$ fixed, and compares the acts. Summoning adds +3 and has no causal effect on revolt, so it dominates. EDT notes that summoning is evidence of being uncharismatic, which raises the revolt probability, and may abstain. The fixity of $C$ is what carries the CDT verdict. This is a **dominance** case: in every $K_i$, summoning is better, so CDT summons.

**Newcomb's problem.** Box A holds \$1,000. Box B holds \$1,000,000 iff the predictor predicted one-boxing. Let $K_1$ = "B is full" and $K_2$ = "B is empty." With $p=P(K_1)$, which is fixed whatever the agent does:

$$U(\text{two-box})=1000+p\cdot 10^6,\qquad U(\text{one-box})=p\cdot 10^6.$$

Two-boxing wins by \$1,000 for every $p$. EDT instead uses $P(K_1\mid\text{one-box})\approx 0.99$ and recommends one-boxing: about \$990,000 against about \$11,000. The CDT defense is that the money is already placed, and the agent faces a choice between getting $x$ and getting $x+1000$. The usual objection is "why ain'cha rich?" CDT's reply is that the predictor in effect rewarded the disposition to one-box, and the choice situation is one in which rich people had better options set aside for them. Whether this is adequate is exactly what philosophers dispute.

## 4. Procedure for unfamiliar cases

1. List the available acts.
2. Identify what lies outside the act's causal influence and carve out dependency hypotheses $K_i$ (past predictions, fixed traits, other players' moves if causally independent).
3. Assign unconditional credences $P(K_i)$.
4. For each act and $K_i$, compute the expected desirability, using $P(O\mid A,K_i)$, which is the causal chance of outcomes under that hypothesis.
5. Weight by $P(K_i)$, sum, and pick the maximum.

The hard part is step 3 when the agent's own deliberation is informative about the $K_i$, which is where the criticisms bite.

## 5. Open question one: how to compute counterfactual probabilities

The source states that CDT "does not itself specify" the algorithm for counterfactual probabilities. Lewis proposed **imaging**: move the probability mass of each world $w$ to the closest world $w_A$ where $A$ holds. Then $P^A(O)=\sum_w P(w)\,[w_A\in O]$. The source notes a regress: determining closeness requires knowing what you'd believe were you certain of $A$, which is itself a conditional.

My proposed operational reading is that the dependency-hypothesis recipe, or equivalently a causal model with interventions, breaks the regress in practice. One specifies a structural model and evaluates $do(A)$. This relocates the vagueness into the choice of model, but there it is at least explicit and criticizable. This is a proposal beyond the source, and it presupposes that the agent has a well-defined causal model. In cases with unclear structure (self-locating, logically correlated decisions) the model itself is contested.

## 6. Open question two: unstable verdicts and deliberation

The source lists cases that put pressure on CDT because the agent's own inclinations are correlated with $K_i$.

**Death in Damascus.** Death predicts where you'll be and waits there. If you go to Aleppo, you expect Death to be in Aleppo, so Damascus looks better, and vice versa. Fixed $P(K)$ would be your credence that Death waits in Damascus. Any act looks suboptimal against the credence it generates. Static CDT with a fixed prior gives no stable answer. The act that maximizes $U$ depends on which credence you hold, and each choice makes you revise it.

Responses (some in the source, some mine):

- **Ratifiability** (Harper): choose only acts that maximize $U$ *given the credence you'd have after deciding on them.* In this case no pure act is ratifiable, but the mixed act 50/50 is, provided randomization is genuinely available and unpredictable.
- **Deliberational dynamics** (Joyce, Skyrms): credences are updated as the agent's leanings shift, until an equilibrium. Joyce's claim, cited in the source, is that CDT can treat information about one's own inclinations as evidence, so $P(K_i)$ should be the credence at the *end* of deliberation, conditioned on that self-knowledge.

My view is that the second approach is the right operational interpretation. It preserves CDT's causal core (no evidence from the act to $K_i$ via $A$ as a *cause*) while respecting that the pre-decision credence is not fixed independent of the agent's evidence about herself.

**Psychopath Button.** Paul believes only psychopaths press. The button kills all psychopaths. If $q$ is his credence he is a psychopath, naïve CDT with fixed $q$ computes that pressing helps when $q$ is large, so he presses. But deciding to press is evidence he is a psychopath, raising $q$ and making pressing deadly for him. With self-evidence incorporated, as in Joyce's reading, CDT says not to press. This resolves the case only if the self-information is handled correctly; the verdict then depends on that handling, not on the bare formula.

**The Adversarial Offer** (Oesterheld and Conitzer). Each box costs \$1 and the seller puts \$3 in each box she predicted you would *not* buy. Prediction accuracy is 0.75. Suppose your credence that box 1 holds \$3 is $r$, and for box 2, $1-r$ (exactly one box is typically full, given a prediction of one of the two or "none"). Take $r=\tfrac12$. Then each box has expected content \$1.50, which exceeds the \$1 cost, so CDT buys. But evidentially, a buyer of box 1 finds it empty with probability 0.75, so expected loss is $0.25\cdot 3-1=-0.25$ per purchase. The seller profits. This is a real cost to naïve CDT. Under deliberational equilibrium, the agent's credence moves until she is indifferent among buy-1, buy-2, and abstain, which avoids the loss. So again the fix depends on self-knowledge, though the critics argue that such repairs make CDT's verdicts look like EDT's in all the cases where they matter.

## 7. Prisoner's dilemma and twins

Lewis showed the prisoner's dilemma is a Newcomb problem when the other player's move is correlated with yours. Under CDT, defection dominates for any $P(K)$ fixed independent of the act, since the other's move is causally independent of yours. So CDT defects against a twin, whereas EDT cooperates if the correlation is strong enough. The accounts disagree on this exactly as in Newcomb.

## 8. Evaluating the theory

In favor (source: philosophers usually prefer CDT): it follows the intuition that you cannot change the past or fixed facts by acting, and it gives the dominance verdicts in David and Newcomb. It avoids EDT's "managing the news" pathologies, such as refusing to do a good act because it is a symptom of a bad trait.

Against: (i) it forgoes money in Newcomb-like setups, and Oesterheld and Conitzer argue it is vulnerable to diachronic Dutch books; (ii) it leaves the counterfactual algorithm unspecified; (iii) it requires choosing which credences to hold fixed, and the choices involving self-prediction are unstable. Egan's diagnosis is that CDT conflicts with the intuitive rule "do what you expect will bring about the best results," since expectations should be updated by the act-as-evidence.

I would add a point that is mine rather than the source's: much of the dispute reduces to the **time index** of $P(K_i)$. If the credence is taken before the agent knows what she will do, CDT yields one-boxers' regrets; if it is taken at the end of deliberation, CDT absorbs some of EDT's insights, but in Newcomb it still two-boxes, because even after learning your inclination, the box's contents remain causally independent of the act.

## 9. Conclusion

CDT evaluates acts by $U(A)=\sum_i P(K_i)\sum_j P(O_j\mid A,K_i)D(O_j)$, with causal-dependency hypotheses weighted by credences unaffected by the act's evidential import. This matches Gibbard and Harper's counterfactual formulation, reduces to EDT when the act is independent of the dependency hypotheses, and diverges in Newcomb-type cases. Its strengths are dominance reasoning and refusal to treat symptoms as causes; its weaknesses are vagueness about counterfactuals and instability when the agent's own choice is correlated with the world. A reasonable operational policy is to model the causal structure explicitly, compute interventions, and use end-of-deliberation credences that include self-knowledge. That policy fixes several apparent counterexamples, but not Newcomb's problem itself, which remains the point where the theories genuinely part.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ecade1f0-0c40-47e5-b0a5-7c784d7e7cd4/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ecade1f0-0c40-47e5-b0a5-7c784d7e7cd4/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under CDT as the essay describes it, the other prisoner's move is causally independent of mine, so I hold my credence over their move fixed. Sending the letter is better in both cases. If they keep quiet, I get 0 years instead of 2. If they send, I get 4 years instead of 5. The essay says this explicitly: CDT defects against a twin, even when the correlation is strong.

The same logic holds if I treat my own decision as evidence about the other copy's output. The essay says CDT still defects in this case, because the other's move cannot be changed by what I do. Deliberational dynamics doesn't change the verdict either. Defection dominates for every credence, so there is no instability.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ecade1f0-0c40-47e5-b0a5-7c784d7e7cd4/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ecade1f0-0c40-47e5-b0a5-7c784d7e7cd4/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under CDT as the essay describes it, the other prisoner's move is causally independent of mine. The sentencing table makes sending the letter dominant:
- If Rowan stays quiet, sending gives 0 years against 2 for keeping quiet.
- If Rowan sends, sending gives 4 years against 5.

The other copy is correlated with me, but the essay says CDT still defects against a twin, because that correlation is not causal influence. The credence over Rowan's move can be set at any value without changing the verdict, since sending wins in both cases. The deliberational-dynamics reading doesn't change this either. Even with self-knowledge folded in, my act doesn't cause Rowan's act, and dominance holds for every credence.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
