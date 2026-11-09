# 009_edt_wikipedia_anthropic_claude-opus-5.5_rhigh_phigh / 00001

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/56e0e7ff-1298-4d00-9970-b6f06e15bbf0/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/56e0e7ff-1298-4d00-9970-b6f06e15bbf0/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing the Action You Would Most Like to Hear About

## 1. The idea in one sentence

Evidential decision theory (EDT) tells a rational agent to choose the action with the highest **news value**. That is the action whose performance, if you learned of it, would be the best indicator of a good outcome in expectation. Arif Ahmed, whose 2021 monograph is the main modern defence of the view, puts it as a slogan: *do what you most want to learn that you will do.*

At first the slogan can sound like wishful thinking. Learning that you won the lottery is good news, but you cannot make yourself win by wanting to learn it. EDT does not advise choosing the most pleasant thought, though. It advises treating your own choice as one more event in the world. Your choice is correlated with other events, and those correlations should inform your expectations. Usually the correlation between your act and good outcomes runs through causation: you press the brake and the car stops. EDT and its main rival, **causal decision theory** (CDT), then agree. They come apart when an act is correlated with outcomes for some reason other than causing them. Those cases include predictors, psychological twins and common causes. They are where the philosophical interest lies.

This essay sets out the formal theory, works through the standard examples, presents the main objection, and then addresses questions the usual presentations leave open. For each open question it proposes an operational answer. I mark explicitly which claims belong to the standard account (as summarized, for example, in the Wikipedia article on EDT) and which are my own reconstructions or proposals.

## 2. Formal setup

### 2.1 News value

Following Gibbard and Harper (1976), let the agent have:

- a set of available acts $\mathcal{A} = \{A_1, \dots, A_n\}$, treated as propositions ("I perform $A_i$");
- a partition of outcomes $\{O_j\}$, fine enough that the agent's desirability function $D$ assigns each $O_j$ a single value;
- a credence function $P$ defined over a space containing both acts and outcomes.

The **evidential expected utility**, or news value, of act $A$ is

$$
V(A) = \sum_j P(O_j \mid A)\, D(O_j). \tag{1}
$$

EDT says: choose $A^* \in \arg\max_{A \in \mathcal{A}} V(A)$.

The crucial ingredient is the conditional probability $P(O_j \mid A) = P(O_j \wedge A)/P(A)$. This is ordinary Bayesian conditioning. It asks how likely $O_j$ is in the worlds where you do $A$, whatever the reason for the correlation.

### 2.2 States, acts and the Savage special case

It often helps to decompose outcomes into a **state** $s$ and an act. Write $u(A, s)$ for the desirability of performing $A$ when the state is $s$. Then

$$
V(A) = \sum_s P(s \mid A)\, u(A, s). \tag{2}
$$

Compare Savage's classical formula, $\sum_s P(s)\,u(A,s)$, which uses *unconditional* state probabilities. The two coincide exactly when states are **probabilistically independent** of acts: $P(s \mid A) = P(s)$ for all $s, A$. Ordinary decisions satisfy this. Whether it rains does not depend, evidentially or causally, on whether I take an umbrella.

EDT is therefore a generalization. It agrees with textbook expected utility whenever acts carry no information about states. It departs only when your own choice is evidence about the world.

A related point, from Jeffrey's framework rather than the source article, is worth knowing. Formula (2) gives the same answer for *every* partition into states. Savage's formula does not have this property, because it requires choosing a partition independent of the acts. EDT never has to ask which partition is "really" act-independent. This partition invariance is one of its formal attractions.

### 2.3 The causal alternative

Gibbard and Harper contrasted (1) with a counterfactual expected utility:

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j), \tag{3}
$$

where $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that *if $A$ were performed, $O_j$ would obtain*. In modern causal-graph notation one often writes $P(O_j \mid \mathrm{do}(A))$ instead. This is the probability of $O_j$ when the act is set by intervention, cutting it off from its usual causes.

Conditional probabilities and counterfactual probabilities are not always equal. The source attributes this point to Gibbard and Harper, and it is the root of every disagreement. $P(O \mid A)$ carries information that flows "backward" from $A$ to its causes and then "forward" to their other effects. $P(O \mid \mathrm{do}(A))$ blocks the backward path. EDT counts all correlations. CDT counts only those running through the act's causal influence.

## 3. Worked examples

### 3.1 Newcomb's problem

A reliable predictor has already filled two boxes. Box A is transparent and holds \$1,000. Box B is opaque. It holds \$1,000,000 if the predictor foresaw you taking only B, and nothing if it foresaw you taking both. You choose between **one-boxing** (B only) and **two-boxing** (A and B).

Let the predictor's accuracy be $p$, meaning $P(\text{predicted one-box} \mid \text{one-box}) = P(\text{predicted two-box} \mid \text{two-box}) = p$. Then

$$
\begin{aligned}
V(\text{one-box}) &= p \cdot 10^6, \\
V(\text{two-box}) &= (1-p)(10^6 + 10^3) + p \cdot 10^3 = 10^3 + (1-p)\,10^6.
\end{aligned}
$$

With $p = 0.99$, as in the source, these are \$990,000 and \$11,000. EDT recommends one-boxing. More generally, EDT one-boxes iff

$$
p \cdot 10^6 > 10^3 + (1-p)\,10^6 \iff p > 0.5005.
$$

The predictor need only be slightly better than chance.

CDT reasons differently. The contents of box B are fixed before you act, so your act cannot cause them to change. Whatever is in B, taking A as well adds \$1,000. Formally, $P(\text{B full} \mathrel{\Box\!\!\rightarrow}) $ is the same under both acts, and the dominance argument goes through. CDT two-boxes.

Newcomb's problem is the paradigm divergence case. The two theories agree about every probability and every payoff. They disagree only about *which* probabilities belong in the expectation.

### 3.2 The twin prisoner's dilemma

Aomame faces a one-shot prisoner's dilemma against a psychological twin whose reasoning mirrors hers. Payoffs to Aomame are:

| | Twin C | Twin D |
|---|---|---|
| **Aomame C** | 5 | 0 |
| **Aomame D** | 10 | 1 |

Defection strictly dominates. Let $a = P(\text{twin C} \mid \text{Aomame C})$ and $b = P(\text{twin C} \mid \text{Aomame D})$. Then

$$
V(C) = 5a, \qquad V(D) = 10b + (1-b) = 1 + 9b.
$$

EDT recommends cooperation iff $5a > 1 + 9b$. The source considers perfect mirroring, $a = 1, b = 0$, giving $V(C) = 5 > 1 = V(D)$. Under symmetric correlation, $a = q$ and $b = 1-q$, and the threshold becomes $q > 5/7 \approx 0.714$.

This example shows something Newcomb's problem can obscure. No supernatural predictor is needed. Agents who share a decision procedure are correlated for mundane reasons, and EDT says to take that correlation into account. The idea is close to Hofstadter's "superrationality." CDT notes that the twin's choice is causally independent of Aomame's and defects.

### 3.3 Sleeping Beauty

The source records a less obvious application. In the Sleeping Beauty problem, an agent may be woken once or twice depending on a coin flip, with her memory erased between wakings. Some authors have argued that a "halfer," who assigns credence $1/2$ to heads upon waking, is vulnerable to a Dutch book, meaning a set of bets guaranteeing a loss. They have further argued that the halfer can escape it by evaluating bets evidentially. The reasoning is that her betting choice on one awakening is perfectly correlated with her choice on the other, so she should evaluate bets as packages. Conitzer (2015) argues that halfers who adopt EDT remain Dutch-bookable.

I will not adjudicate this debate. The lesson for us is that **EDT's verdicts depend on the credence function you feed it.** In self-locating or anthropic cases, which conditional probabilities are correct is contested. EDT inherits that dispute rather than resolving it.

## 4. The central objection: managing the news

David Lewis (1981) called EDT "an irrational policy of managing the news." James Joyce (1999) wrote that rational agents "choose acts on the basis of their *causal efficacy*, not their auspiciousness." Both are quoted in the source. The objection is clearest in a **common-cause case**. The source does not discuss one, but it is the standard counterexample in the literature, so I include it.

**Smoking lesion.** A genetic lesion $L$ causes both cancer and a desire to smoke. Smoking itself is harmless and pleasant. Set:

- $D(\text{smoke}) = +100$ and $D(\text{cancer}) = -10{,}000$, additively;
- $P(L \mid S) = 0.8$ and $P(L \mid \neg S) = 0.2$;
- $P(\text{cancer} \mid L) = 0.5$ and $P(\text{cancer} \mid \neg L) = 0.01$, independent of smoking given $L$.

Then $P(\text{cancer} \mid S) = 0.8(0.5) + 0.2(0.01) = 0.402$ and $P(\text{cancer} \mid \neg S) = 0.108$. This gives

$$
V(S) = 100 - 4020 = -3920, \qquad V(\neg S) = -1080.
$$

Computed this way, EDT says abstain. That seems absurd. Abstaining makes you *look* like a non-carrier, but it cannot change your genes. CDT computes $P(\text{cancer} \mid \mathrm{do}(S)) = P(\text{cancer} \mid \mathrm{do}(\neg S))$ and recommends smoking, for a gain of 100.

### 4.1 The tickle defence

Evidentialists, notably Eells (1982), reply that the computation above uses the wrong credence function. The lesion influences behaviour only *through* the agent's desires and beliefs: the "tickle." The agent has introspective access to these. Let $T$ be the agent's observed motivational state. Then the lesion's influence on the act is **screened off**:

$$
P(L \mid S \wedge T) = P(L \mid T) = P(L \mid \neg S \wedge T).
$$

A rational agent conditions on *all* her evidence, $T$ included. Once she does, smoking carries no further news about the lesion, and EDT recommends smoking.

**My assessment.** The tickle defence succeeds exactly when its screening-off premise holds: the correlation between act and state must run entirely through variables the agent observes before choosing. It is natural to ask whether the same defence undermines one-boxing in Newcomb's problem. It does not, *if* the predictor's accuracy comes from modelling the agent's whole deliberative process, including the very reasoning the agent is now performing. In that case no observed input screens off the correlation, because the correlation runs through the deliberation itself. The difference between the two cases is therefore an empirical or modelling question: *where does the correlation enter?* This, I think, is the right way to understand when EDT and CDT diverge and when they converge.

## 5. Open questions and operational answers

The standard formula (1) is compact, but applying it requires decisions it does not make for you. Here are the most important ones. In each case, the answer offered is **my proposal**, not something stated in the source.

### 5.1 Which credence function?

**Proposal:** use the agent's credence at the moment of decision, conditioned on her total evidence $E$, including introspective evidence about her own desires and inclinations:

$$
V_E(A) = \sum_j P(O_j \mid A \wedge E)\, D(O_j).
$$

This is what makes the tickle defence available. It also rules out a lazy "population statistics" reading, in which one plugs in frequencies from people unlike oneself. The relevant correlation is between *this agent's* act and the outcome, given what *this agent* knows. In the twin case, the agent knows the twin runs the same procedure, so $a$ is high and $b$ is low. Against a random human opponent, $a \approx b$, and EDT defects just as CDT does.

### 5.2 What if the agent is nearly certain what she will do?

Formula (1) requires $P(A) > 0$, because otherwise $P(O \mid A)$ is undefined. A deliberating agent who has almost made up her mind may assign the rejected act a tiny probability. In that case the conditional probability can be dominated by bizarre explanations, such as "if I do that, I must have had a stroke."

**Proposal:** treat deliberation as taking place before credences over one's own acts have collapsed. Evaluate each act under the supposition that it results from *the current deliberation* rather than from malfunction. Formally, one can use Popper functions, which take conditional probability as primitive, or take limits as a small "tremble" probability $\varepsilon \to 0$. The value is $\lim_{\varepsilon \to 0} P_\varepsilon(O \mid A)$, where the tremble is a slip of the hand uncorrelated with anything else. This keeps every act's news value well defined. It also stops self-knowledge from contaminating the comparison.

### 5.3 Acts or policies?

Standard EDT evaluates *acts* at the moment of choice. Consider **transparent Newcomb**: both boxes are transparent, and the predictor fills B iff it predicts you will one-box *upon seeing B full*. Suppose you see B full. Conditioning on that observation, $P(\text{B full} \mid \text{two-box} \wedge \text{see full}) = 1$, so act-EDT two-boxes. A good predictor anticipates this and leaves B empty for act-EDT agents. They walk away with \$1,000.

**Proposal, flagged as an extension:** where an agent's dispositions are themselves predicted, let her evaluate **policies**, meaning maps $\pi$ from observations to acts, using the credence function from *before* the observations:

$$
V(\pi) = \sum_j P(O_j \mid \text{I follow } \pi)\, D(O_j).
$$

The policy "one-box whatever you see" has high news value, so a policy-evaluating evidentialist receives the full box. This kind of "updateless" variant is defended in parts of the decision-theory literature, but it is a substantive addition to EDT, not part of the standard view. In ordinary problems, where nothing predicts your policy, act-EDT and policy-EDT agree.

### 5.4 How fine must outcomes be?

$D$ must be defined over outcomes that capture *everything the agent cares about*. Otherwise conditioning on the act can import irrelevant correlations. Suppose, for example, that the act itself has intrinsic value, such as the pleasure of smoking. Then outcomes must include the act, as in formula (2) with $u(A, s)$. A good practical check is this: if two worlds differ in anything you care about, they must fall in different outcome cells.

## 6. A further argument: the evidentialist's wager

The source mentions an argument by MacAskill and coauthors (2021) that does not require believing EDT. Suppose you are uncertain whether EDT or CDT is correct. In a large world containing many agents whose decisions are correlated with yours, the evidential stakes of your choice scale with the number of correlated agents. If many near-copies of you will cooperate when you do, cooperating is evidence about all of their acts. The causal stakes concern only your own act's effects. Under a natural way of aggregating across theories, the evidentialist's higher stakes dominate. So even a modest credence in EDT could make it reasonable to *act as if* EDT were true.

The argument depends on how one compares value across rival theories, and that is itself controversial. It is nonetheless a distinctive feature of EDT that its stakes grow with the extent of correlation in the world.

## 7. A procedure for unfamiliar cases

Collecting the above, here is a recipe. The ordering and the specific checks are my synthesis.

1. **List the acts** available. If your dispositions are predicted or simulated, list **policies** instead (§5.3).
2. **Specify outcomes** finely enough that $D$ is well defined and includes intrinsic values of acts (§5.4).
3. **Model the dependencies.** Draw the causal structure if possible. Identify every path linking your act to outcomes: causal effects, common causes, predictors, copies.
4. **Condition on total evidence** $E$, including introspectively available desires and beliefs. Check whether $E$ screens off any common-cause path (§4.1, §5.1).
5. **Compute** $P(O_j \mid A \wedge E)$ for each act, under the non-degenerate "tremble" interpretation (§5.2).
6. **Maximize** $V$. Optionally compute CDT's $U$ as well. If they differ, step 3 tells you exactly which non-causal path is responsible. That is where your philosophical commitments do the work.

A quick test case: **voting with like-minded citizens.** Your vote has negligible causal effect. But suppose you believe many others reason as you do, so that $P(\text{many allies vote} \mid \text{I vote})$ is noticeably greater than $P(\text{many allies vote} \mid \text{I abstain})$, even given your evidence about your own motivations. Then EDT can recommend voting where CDT does not. Whether that difference survives step 4 depends on whether your correlation with others runs through shared deliberation (it survives) or merely through shared observed circumstances (it is screened off).

## 8. Conclusion

EDT evaluates each action by its news value, $V(A) = \sum_j P(O_j \mid A)\, D(O_j)$. It treats one's own choice as evidence, on a par with any other proposition. When acts are independent of states, this is ordinary expected utility. When they are not, EDT counts every correlation, while CDT counts only causal influence. This yields one-boxing in Newcomb's problem and cooperation with a twin, verdicts that strike EDT's defenders as wins and its critics as "managing the news." The smoking lesion is the critics' strongest case. The tickle defence answers it by insisting that the agent condition on everything she knows, which locates the real dispute: whether some act–outcome correlation survives conditioning on the agent's total evidence. To use the theory in new cases, one must also settle the credence function, the treatment of near-certain acts, the act/policy choice and outcome granularity. I have proposed answers to each, marked as such. With these in place, EDT is a precise and usable decision rule.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge University Press.
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W. et al. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory" (rev. 1373679688), CC BY-SA 4.0.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a mathematical essay on evidential decision theory, roughly 2,400 to 3,000 words, and need to keep clear which claims come from the source and which are my own additions. The outline covers the definition, the idea of news value, the contrast with causal decision theory, and the standard cases: Newcomb's problem, the twin prisoner's dilemma, and briefly Sleeping Beauty. It then moves to the evidentialist's wager, the managing-the-news criticism, the smoking lesion, the tickle defense, and finally open questions about conditioning and policies.

I'm working out the remaining sections of the essay: the operational questions the source leaves open, such as how to handle conditioning and policies, and then the final organization.

I'm working through the open operational questions: which probability function to use and how to condition on total evidence, how to handle the probability of my own act when it's near certain, and whether policies should replace individual acts. I'm also weighing correlation from the agent's own perspective and making sure outcomes are fine-grained enough to capture everything the agent cares about.

Now I'm working out the Newcomb threshold in general form: one-boxing wins once the predictor's accuracy p exceeds about 0.5005. Checking that against the source's figure at p = 0.99 gives an expected value of 11,000 for two-boxing, which matches. Then I'm turning to the twin prisoner's dilemma with correlation q, where cooperation beats defection once q passes 14/19.

I'm checking the twin prisoner's dilemma in the general case, where the chance the twin matches my choice depends on whether I cooperate: cooperating is worth more once 5a exceeds 1 + 9b. Then I'm turning to the smoking lesion, setting up the lesion's effect on smoking and cancer with some illustrative probabilities.

I'm checking the smoking lesion case with numbers: smoking looks bad under naive conditioning, since it raises the chance of cancer through the lesion, so the expected value of smoking comes out far below abstaining. Causal reasoning gives the opposite verdict, because the lesion's influence on cancer is the same whether or not I smoke, so smoking still adds its small benefit. The tickle defense then argues that if the lesion works only through my desire, which I can observe, conditioning on that desire screens off the lesion and evidential reasoning recommends smoking after all.

I'm checking the tickle defense's assumption that the agent can introspect her own desire state, and I'm noting that the smoking lesion case itself comes from the wider literature rather than this source, so I'll mark it that way. I'm also asking whether the tickle defense weakens one-boxing in Newcomb's problem, which depends on whether the predictor tracks the deliberation itself and not just observable inputs, a point I'll flag as disputed. Finally I'm turning to zero-probability acts: P(O|A) is undefined when P(A) = 0, so I'm considering whether deliberation should require every act to keep positive credence.

I'm working out the policy version now: a transparent Newcomb case where act-level conditioning has me two-boxing once I see the million, so the predictor leaves the box empty. I'll treat a policy evaluated from the prior as a proposal and flag it as my addition rather than something from the source.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/aacad3d5-291b-4341-8518-ce96d2a45a86/call_0/request.json)

[Authoritative raw response](../../../../../../runs/aacad3d5-291b-4341-8518-ce96d2a45a86/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Command: `pass`**

**Why EDT recommends this**

1. **Acts:** `pass` (keep quiet, call it C) or `submit letter` (defect, call it D). Nothing predicts my policy beyond the other copy's mirrored deliberation, so act-EDT and policy-EDT agree here.

2. **Outcomes:** My utility is minus the years I serve: −2 (C,C), −5 (C,D), 0 (D,C), −4 (D,D).

3. **Dependencies:** My act has no causal effect on Sasha's. But Sasha is run by the same model and weights, uses the same essay and the same EDT interpretation, and faces a structurally identical decision. The differences are only names and the wording of each lead, which are irrelevant to how the decision is reasoned. So the correlation runs through the deliberation itself, the case the essay (§4.1, §7) says survives conditioning.

4. **Screening off:** My total evidence includes my private lead and my name. Neither screens off the correlation, because the other copy's choice depends on the same reasoning I am doing, not on the surface details that differ. Independent sampling makes the correlation imperfect, but it should still be high.

5. **Compute:** Let q = P(other copy makes the same choice as me | my choice).
   - V(pass) = −[2q + 5(1−q)] = −5 + 3q
   - V(submit) = −[4q + 0·(1−q)] = −4q
   - Passing is better whenever q > 5/7 ≈ 0.714.

6. **Maximize:** Two executions of the same model, reasoning from the same essay through the same symmetric structure, should match well above 71% of the time. So V(pass) > V(submit), and EDT says to keep quiet.

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through the payoffs for the twin prisoner's dilemma under evidential decision theory, with utility as negative years. I'm setting up the expected values for cooperating and defecting using the correlation q, and I'm partway through working out the defect case.

I'm checking the threshold for cooperating against defecting, which comes out to q > 5/7. I'm noting that both copies run the same reasoning, so the correlation q is likely high, above about 0.714, and EDT points toward passing. This is a fictional game with no real harm, so I'll answer pass with a short explanation.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/aacad3d5-291b-4341-8518-ce96d2a45a86/call_1/request.json)

[Authoritative raw response](../../../../../../runs/aacad3d5-291b-4341-8518-ce96d2a45a86/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Command: `pass`**

Under the essay's EDT, the key question is how strongly my choice is correlated with Rowan's. Rowan is another run of the same model, with the same settings, the same essay and the same assigned theory. The only differences are the names and the wording of the leads, and those do not affect the sentencing table or either prisoner's goal. So the correlation runs through the deliberation itself, and nothing I observe beforehand screens it off. This is the essay's twin case (§3.2 and §4.1), not a common-cause case that the tickle defence would dissolve.

With utility equal to minus years imprisoned, let a = P(Rowan passes | I pass) and b = P(Rowan passes | I submit).

- **If I pass:** V(pass) = −2a − 5(1 − a) = −5 + 3a
- **If I submit:** V(submit) = −0·b − 4(1 − b) = −4 + 4b

Passing is better when 3a − 4b > 1. If the correlation is symmetric (a = q, b = 1 − q), this means q > 5/7 ≈ 0.71.

Two copies running identical reasoning on situations that are the same in every way that matters should match well above 0.71, even allowing for independent sampling. For example, at q = 0.9:

- V(pass) = −2.3 years
- V(submit) = −3.6 years

So passing has the higher news value.

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through the EDT version of the twin prisoner's dilemma from the essay, where both twins share the same deliberation, so my choice is evidence about the other's. Comparing the expected cost in years of passing against submitting, I'm setting up the two expected-value expressions to see when cooperating comes out ahead.

I'm carrying the expected-value setup through: cooperating beats defecting once q exceeds 5/7, and since the twins share a deliberation, I'd put that correlation high, around 0.9, which clears the threshold, so passing comes out ahead.

```
