# Evidential Decision Theory: Choosing by the News Your Choice Brings

## 1. The slogan and the idea

Evidential decision theory (EDT) gives a short instruction: **do what you would most like to learn that you are going to do.** (This is Arif Ahmed's phrasing, quoted in the reference article.) An action is good to the extent that it is good *news*, that is, to the extent that learning you had performed it would raise your expectation of how well things will go.

The instruction seems obvious until it conflicts with a rival intuition: that an act is good to the extent that it *makes* things go well. That rival intuition is causal decision theory (CDT). The two theories agree in nearly every ordinary decision. They come apart only when an act is evidence about something it does not cause. The interest of EDT lies in that gap, so most of this essay is about it.

I first give the formal definition, then a procedure for applying it, then the standard test cases, and then the questions the theory leaves open. Throughout, I mark which claims come from the reference article (the Wikipedia entry on EDT) and which are my own additions or proposals.

## 2. Formal definition

### 2.1 News value

Let $\mathcal{A}$ be a set of available acts. Let $\{O_j\}$ be a partition of possible outcomes. Let $D(O_j)$ be the agent's desirability (utility) for outcome $O_j$, and let $P$ be the agent's credence function, a probability over propositions that include the agent's own acts. Following Gibbard and Harper (1976), as reported in the source, the **evidential expected utility**, or **news value**, of act $A$ is

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j).
$$

EDT says: choose $A^\ast \in \arg\max_{A\in\mathcal{A}} V(A)$.

Three features of this formula matter.

1. **Acts are propositions in the credence space.** The agent has credences about what she herself will do. This is unlike Savage's framework, where acts are functions from states to outcomes and receive no probabilities. The conditional $P(O_j\mid A) = P(O_j \wedge A)/P(A)$ is only defined if $P(A) > 0$, a point I return to in §6.

2. **States can be made explicit.** If outcomes are determined by an act together with a state $s$ from a partition $\mathcal{S}$, the law of total probability gives
$$
V(A) = \sum_{s\in\mathcal{S}} P(s\mid A)\, u(A,s),
$$
where $u(A,s)$ is the desirability of doing $A$ in state $s$. The decisive feature is that the *state* probabilities are conditioned on the act. (This partition-invariance, meaning that the value does not depend on how one carves up the states, is a well-known virtue of Jeffrey's framework rather than something the source discusses.)

3. **Everything known is conditioned on.** In practice the relevant credence is $P(\cdot \mid E)$, where $E$ is the agent's total evidence at the moment of choice. Writing the formula as $V(A) = \sum_j P(O_j\mid A, E)\,D(O_j)$ makes clear that what counts is the evidential bearing of $A$ *given everything else the agent already knows*. This will matter a great deal in §5.

### 2.2 The causal alternative

The source sets EDT against the causal formula

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that $O_j$ *would* obtain *were* $A$ performed. The source's central structural claim is that $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ and $P(O_j\mid A)$ need not be equal. That is the whole of the disagreement.

They coincide whenever the act is probabilistically independent of every state that it does not causally influence. Formally, if $P(s\mid A) = P(s)$ for every $s$ in a partition of causally act-independent states, then
$$V(A) = \sum_s P(s)\,u(A,s) = U(A),$$
and the theories give identical verdicts. So EDT and CDT diverge only when an act is *correlated* with a state it does not cause. Such correlations typically come from a common cause, from a predictor modelling the agent, or from another agent running the same reasoning.

## 3. A working procedure

The source gives the formula and examples but no step-by-step method. The following procedure is my own codification. It is meant to let a reader decide unfamiliar cases.

1. **Fix the decision point.** Identify when the choice is made and what the agent knows at that moment, $E$. Include introspective knowledge of the agent's own desires and beliefs where she has it.
2. **List the options.** Identify the genuinely available acts $A_1,\dots,A_n$, or policies if the choice is being made ex ante (§6.2).
3. **Choose an outcome or state partition** fine enough that desirability is well defined on each cell.
4. **Specify the joint credence** $P(\cdot\mid E)$ over acts and states. Ask specifically: *if I learned I did $A_i$, what would I then believe about the states?* Correlations from every source count: causal influence, common causes, predictors, and similarity of reasoning.
5. **Compute** $V(A_i) = \sum_s P(s\mid A_i,E)\,u(A_i,s)$ and choose the maximum.
6. **Run two diagnostics.** (a) *Screening:* is the correlation between $A_i$ and $s$ still present once you condition on all of $E$, or does something you already know screen it off? (b) *Stability:* if you became confident you would do $A_i$, would $A_i$ still look best? (§6.3)

Step 4 is where all the substantive work happens, and it is also where EDT is most often misapplied. The test cases below show both.

## 4. The test cases

### 4.1 Newcomb's problem

As in the source: box A is transparent and contains \$1,000. Box B is opaque and contains \$1,000,000 if and only if a reliable predictor foresaw that you would take only B. You may take B alone or both boxes.

Let $p = P(\text{predicted } X \mid \text{you do } X)$. The source sets $p = 0.99$. Then

$$
\begin{aligned}
V(\text{one-box}) &= p\cdot 10^6 + (1-p)\cdot 0 = p\cdot 10^6,\\
V(\text{two-box}) &= p\cdot 10^3 + (1-p)\cdot(10^6+10^3) = 1{,}001{,}000 - 10^6\, p.
\end{aligned}
$$

At $p=0.99$ these are \$990,000 and \$11,000, the source's figures. More generally, one-boxing wins if and only if

$$
p\cdot 10^6 > 1{,}001{,}000 - 10^6 p \iff p > 0.5005.
$$

**EDT one-boxes against any predictor even slightly better than chance.** (This threshold is my own derivation, not the source's.)

Note an assumption the source leaves implicit. It reads "99% accuracy" as $P(\text{\$1M in B}\mid\text{one-box}) = 0.99$ *and* $P(\text{empty}\mid\text{two-box}) = 0.99$. That reading requires the predictor to be equally accurate on both kinds of chooser, and the agent's credences to reflect that accuracy. EDT needs only the agent's conditional credences, so if accuracy is asymmetric you should plug in the two conditionals separately.

CDT reasons differently. Let $b$ be the probability that B is full. The prediction is already made, so $P(\text{two-box} \mathrel{\Box\!\!\rightarrow} \text{B full}) = b$ regardless of the act. Hence

$$U(\text{two-box}) = U(\text{one-box}) + 1000$$

for every $b$. Two-boxing dominates. This is the cleanest divergence between the theories.

### 4.2 The twin prisoner's dilemma

Aomame faces a psychological twin whose reasoning mirrors hers. The payoffs are (C,C) = 5, (D,D) = 1, and sucker/temptation = 0/10. The source assumes perfect correlation and obtains $V(C)=5$ and $V(D)=1$, so EDT cooperates.

Relax the assumption. Let $q = P(\text{twin } C\mid C)$ and $r = P(\text{twin } D\mid D)$. Then

$$
V(C) = 5q, \qquad V(D) = 10(1-r) + r = 10 - 9r.
$$

With symmetric correlation $q=r$, cooperation wins iff $5q > 10-9q$, i.e. $q > 5/7 \approx 0.71$. (Again this is my generalisation.) CDT defects whatever the correlation is, because the twin's choice is causally independent of Aomame's and defection dominates.

This case shows EDT's distinctive notion of dependency most clearly. No signal passes between the rooms and no predictor exists. The correlation arises solely because two processes compute the same function. For EDT this kind of non-causal, "logical" dependence is fully action-relevant. It is the formal core of what Hofstadter called *superrationality*, which the source lists under "See also."

### 4.3 Sleeping Beauty

The source reports only the following. EDT has been applied to Sleeping Beauty to escape Dutch books. A "halfer" (credence 1/2 in Heads upon waking) has been argued to be Dutch-bookable but to avoid this by adopting EDT. Conitzer (2015) argues that EDT halfers remain Dutch-bookable.

Here is my own illustration of why EDT changes the betting picture. Recall the setup: a fair coin is tossed, Beauty is woken once if Heads and twice if Tails, and her memory is erased between wakings. At each waking she is offered a bet costing $x$ that pays 1 if Tails. Her waking selves reason identically, so her choice now is evidence (indeed near-certain evidence) that she makes the same choice at every waking. An EDT halfer therefore evaluates accepting the bet across the whole experiment:

$$
V(\text{accept}) = \tfrac12(-x) + \tfrac12\cdot 2(1-x) = 1 - \tfrac{3}{2}x.
$$

She accepts iff $x < 2/3$. That is exactly the price a thirder would pay. So EDT plus halfer credences can reproduce thirder betting behaviour, which is how certain Dutch books are defused. (The pairing of EDT-halfing with CDT-thirding is associated in the literature with Briggs 2010.) Whether *every* Dutch book is defused this way is precisely what Conitzer disputes. I take no stand on it here.

## 5. Dependencies, counterfactuals, and "managing the news"

### 5.1 What EDT does with counterfactuals

Strictly, nothing. EDT has no counterfactual operator, no causal graph, and no "intervention." The only modal question it asks is indicative: *given that I do $A$, how are things likely to be?*

Defenders count this as a virtue, since causal and counterfactual notions are philosophically contested and EDT does without them. Critics count it as the core defect.

David Lewis (quoted in the source) called EDT "an irrational policy of managing the news." Joyce wrote that rational agents "act to *bring about* good results even when doing so might betoken bad news."

### 5.2 The smoking lesion and the tickle defence

The critics' canonical case does not appear in the source, but any reader applying EDT will meet it.

Suppose a lesion $L$ causes both cancer and a taste for smoking, and smoking itself is harmless. Take $u(\text{smoke}) = +10$ and $u(\text{cancer}) = -1000$, and suppose the population statistics give $P(\text{cancer}\mid S) = 0.5$ and $P(\text{cancer}\mid \neg S) = 0.1$. A naive calculation gives

$$
V(S) = 10 - 500 = -490,\qquad V(\neg S) = -100.
$$

So "EDT says don't smoke," which is the absurdity of managing the news.

The standard reply is the *tickle defence* (Eells 1982). It is an instance of diagnostic 6(a). Suppose the lesion affects behaviour only by producing a desire $T$ (the "tickle"), and the agent can introspect whether she has $T$. Her evidence $E$ then includes $T$ or $\neg T$, and the lesion is screened off:

$$
P(L\mid S, T) = P(L\mid T) \quad\text{and}\quad P(L \mid \neg S, T) = P(L\mid T).
$$

Conditioning on her total evidence, the act carries no further news about the lesion, so $V(S\mid T) - V(\neg S\mid T) = 10$. She should smoke.

The general moral, which I endorse as an operational principle, is this: **population correlations are not the agent's conditional credences.** The quantity EDT uses is $P(s\mid A, E)$. The statistical correlation between the act and the state frequently disappears once $E$ includes the agent's own reasons for acting.

Newcomb and the twin case differ from the lesion in exactly this respect. Nothing the agent knows about herself before choosing screens off the predictor's or the twin's correlation with the *choice itself*, because they track the output of her deliberation and not merely her prior inclinations. Whether tickle-style screening always succeeds is disputed. When it does, EDT and CDT converge on a problem. When it fails, they diverge.

### 5.3 A taxonomy of dependencies (my summary)

| Source of act–state correlation | Example | EDT counts it? | CDT counts it? |
|---|---|---|---|
| Act causes state | pressing a switch lights the lamp | yes | yes |
| Common cause, screened off by the agent's evidence | lesion with an introspectible tickle | no (screened off) | no |
| Common cause, not screened off | lesion with no introspective access | yes | no |
| Predictor modelling the agent's deliberation | Newcomb | yes | no |
| Shared reasoning procedure | twin PD, Beauty's wakings | yes | no |

## 6. Open questions and reasonable operationalisations

The source states the formula and the verdicts. It leaves several questions the formula does not settle by itself.

### 6.1 Zero-probability acts

$P(O\mid A)$ is undefined if $P(A)=0$. Yet a deliberating agent may become certain of what she will do, and she still needs a value for the alternatives in order to confirm the choice.

*Proposal.* Treat conditional credence as primitive (Popper functions). Alternatively, define

$$V(A) = \lim_{\varepsilon\to 0} V_\varepsilon(A),$$

where $P_\varepsilon$ mixes a small "tremble" probability $\varepsilon$ onto every act. I prefer the trembling route because it is computable. Its cost is that the limit can depend on *how* trembles correlate with states. If you would only take an act by mistake, what does that mistake indicate? The modeller must then state an explicit assumption. I regard this as a genuine open problem, not a technicality.

### 6.2 Acts versus policies

EDT is usually applied at the moment of choice. Consider a *transparent* Newcomb problem, in which box B is visible.

If you see \$1M, the prediction is already revealed. Your act then carries no news about the contents, and EDT conditioned on $E$ says to take both boxes. Yet an agent who is predictably like that would have been shown an empty box.

An alternative evaluates *policies* $\pi: E\mapsto A$ from an earlier vantage point:

$$\pi^\ast = \arg\max_\pi \sum_s P(s\mid \pi)\,u(\pi, s).$$

This is the intuition behind "updateless" variants. The source says nothing about it. My recommendation is to apply act-level EDT when no one is modelling your policy, and to evaluate policies when predictors or copies respond to what you *would* do across observations. Be clear, however, that this goes beyond EDT as standardly defined.

### 6.3 Instability and ratifiability

The value of $V$ depends on the agent's credences about her own action, and those credences shift as she deliberates. Jeffrey (1983) proposed that one should choose only *ratifiable* acts. Let $V_A$ denote news value computed under the credence one would have on deciding $A$. Then:

$$A \text{ is ratifiable iff } V_A(A) \ge V_A(B) \ \text{ for all } B.$$

Ratifiability adds a stability condition to bare EDT. As step 6(b), it is a useful diagnostic, but it is an addition, and it can make EDT agree with CDT in some cases while leaving others with no ratifiable option at all.

### 6.4 Whose correlations?

EDT is subjective: it uses *your* conditional credences. Two agents facing the "same" twin dilemma can rationally disagree about $q$. The theory then gives them different recommendations. That is not inconsistency; it is how the theory is designed. Applied work should therefore report the conditional credences on which a verdict depends, as I did with the thresholds $p > 0.5005$ and $q > 5/7$.

## 7. The evidentialist's wager

The source reports a further argument from MacAskill, Vallinder, Oesterheld, Shulman and Treutlein (2021). Even an agent who gives EDT low credence may have reason to act as EDT recommends, because EDT's stakes can be larger.

Here is a simple formalisation of my own. Suppose your decision is correlated with the decisions of $N$ similar agents, and each correlated decision adds $\Delta_E$ to the value of the world as you assess it. According to EDT, choosing $A$ over $B$ is news about all $N$ decisions, worth about $N\Delta_E$. According to CDT, it changes only your own contribution, $\Delta_C$.

With credence $c$ in EDT, a "maximise expected choiceworthiness" approach to theory-uncertainty favours the EDT recommendation whenever

$$c\,N\Delta_E > (1-c)\Delta_C.$$

For large $N$ this holds even for small $c$.

The argument inherits all the contested assumptions of intertheoretic value comparison. In particular, it assumes that "utility according to EDT" and "utility according to CDT" share a common scale. The source presents it only as a "supporting argument," and I would treat it as suggestive rather than decisive.

## 8. Assessment

The case *for* EDT has three parts.

- **Parsimony:** it is ordinary expected utility with ordinary conditional probability, with no causal or counterfactual primitives.
- **Results:** EDT agents facing reliable predictors walk away rich. Its defenders ask the pointed question, "if you're so smart, why aren't you rich?"
- **Shared reasoning:** it handles correlation among similar reasoners naturally, as in the twin case, Sleeping Beauty and the wager.

The case *against* is Lewis's and Joyce's charge. An act's auspiciousness is not its efficacy, and choosing acts in order to receive good news looks like a confusion between learning about the world and changing it. Its force depends on cases like the smoking lesion. There, EDT's defenders reply that properly conditioned credences remove the bad news, which brings EDT into line with CDT exactly where CDT's verdict is intuitive.

Real philosophical disagreement remains at the Newcomb and twin cases. In those, *nothing the agent knows can screen off the correlation*, because what is correlated is the deliberation itself.

## 9. Conclusion

EDT ranks acts by
$$V(A) = \sum_j P(O_j\mid A, E)\,D(O_j),$$
the expected desirability of the world given the news that you do $A$, conditioned on everything you know.

It treats every act–state correlation the agent still believes in as decision-relevant, whether that correlation is causal, common-cause, predictive or logical. It replaces counterfactuals with indicative conditionals. As a result it agrees with CDT whenever acts are independent of the states they do not cause, and disagrees exactly where they are not: it one-boxes in Newcomb for any predictor accuracy above $0.5005$, and it cooperates with a twin once correlation exceeds $5/7$.

Applying EDT well is mostly a matter of getting the conditional credences right: conditioning on total evidence, checking for screening-off, and noting when the verdict depends on how zero-probability acts, policies or deliberational instability are handled. Those three points are where the theory's formal statement runs out and the user must supply, and defend, an interpretation of their own.

---

**References** (brief)

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge UP.
- Briggs, R. (2010). "Putting a value on Beauty." *Oxford Studies in Epistemology* 3.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Eells, E. (1982). *Rational Decision and Causality*. Cambridge UP.
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and two kinds of expected utility."
- Jeffrey, R. (1983). *The Logic of Decision*, 2nd ed. Chicago UP.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Lewis, D. (1981). "Causal decision theory." *Australasian J. Phil.* 59(1).
- MacAskill, W. et al. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," rev. 1373679688 (CC BY-SA 4.0), the reference article.