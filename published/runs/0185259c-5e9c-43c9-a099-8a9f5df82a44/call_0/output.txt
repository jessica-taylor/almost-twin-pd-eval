# Evidential Decision Theory: Choosing the Act You Would Most Like to Hear About

## 1. The slogan

Evidential decision theory (EDT) can be summarized in one sentence: when choosing among actions, pick the one with the highest *news value*. Imagine learning that you had taken a given action. That news would update your beliefs about how the world is and how things will go. EDT tells you to perform the action whose news would be best in expectation. Arif Ahmed's phrasing is "do what you most want to learn that you will do" (Ahmed 2021, p. 7).

This sounds harmless. In ordinary cases an act is good news precisely because it tends to *cause* good outcomes, and EDT agrees with every other expected-utility theory. The theory becomes philosophically interesting where an act is correlated with good outcomes without causing them. In those cases EDT parts ways with its main rival, causal decision theory (CDT). This essay sets out the formal machinery, gives a procedure for applying it, works through the standard cases, and marks where the theory leaves questions open.

On sourcing: the definitions, the Newcomb and twin calculations, the Sleeping Beauty remarks, the evidentialist's wager, and the Lewis and Joyce criticisms come from the reference article. The partition-invariance discussion, the threshold computations, the smoking-lesion and tickle material, the act/policy distinction, and the operational procedure in §4 are my additions. I flag them as such in the text.

## 2. The formal definition

### 2.1 News value

Following Gibbard and Harper (1976), as reported in the source, EDT maximizes

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j),
$$

where $\{O_j\}$ is a partition of possible outcomes, $D(O_j)$ is the desirability of outcome $O_j$, and $P(O_j\mid A)$ is the agent's conditional credence in $O_j$ given that she performs $A$. The only formal departure from textbook expected utility is that the weights are *conditional* on the act.

It is often more convenient to factor outcomes into *states* $s$ (features of the world the agent does not control) and acts $a$, with the outcome given by a function $o(a,s)$ and utility $u(a,s) = D(o(a,s))$. Then

$$
V(a) \;=\; \sum_{s} P(s \mid a)\, u(a,s) \;=\; \mathbb{E}[\,u \mid a\,].
$$

EDT's recommendation is $a^\* \in \arg\max_a V(a)$.

### 2.2 Two structural facts (my exposition)

**Savage as a special case.** Suppose states are probabilistically independent of acts, so $P(s\mid a) = P(s)$ for all $a,s$. Then $V(a) = \sum_s P(s)\,u(a,s)$, which is Savage-style expected utility. EDT therefore departs from orthodoxy only when the agent's credences make acts *evidentially relevant* to states.

**Partition invariance.** In Richard Jeffrey's framework, which is the natural home of EDT, desirability is defined for every proposition, and the following holds for *any* partition $\{S_i\}$:

$$
V(A) = \sum_i P(S_i \mid A)\, V(A \wedge S_i).
$$

This is the law of total expectation applied to $\mathbb{E}[u \mid A]$. Its practical consequence is that you need not find the "right" carving of the world into states. Any partition gives the same answer, provided you condition on the act inside every term. Savage's framework, by contrast, needs act-independent states to give sensible answers. EDT does not need them, which is part of its appeal. Its verdicts are fixed by the joint credence over acts and outcomes and by nothing else.

## 3. The contrast with causal decision theory

CDT, as presented in the source, replaces the conditional probability with the probability of a counterfactual:

$$
U(A) = \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j).
$$

Here $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that $O_j$ *would* obtain if $A$ were performed. Two common ways of cashing this out:

- Lewis's dependency hypotheses: $U(A) = \sum_K P(K)\sum_j P(O_j\mid A\wedge K)D(O_j)$. Here $K$ ranges over hypotheses about how outcomes causally depend on acts, and $P(K)$ is *unconditional*.
- Interventionist: $U(A) = \sum_j P(O_j \mid \mathrm{do}(A))\,D(O_j)$, computed in a causal model by cutting the arrows into the act node.

Since $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ and $P(O_j\mid A)$ need not coincide, the two theories can disagree. The diagnostic is simple. **EDT and CDT diverge exactly when the act carries information about states it does not cause.** Typically this happens because the act and the state share a common cause, or are both outputs of the same computation.

## 4. Applying EDT: an operational procedure (my proposal)

The source gives the formula but not a recipe. The formula alone underdetermines practice in a few places, so I propose the following procedure.

1. **Fix the option set** $\mathcal{A}$. These are the acts genuinely available at the moment of decision.
2. **Fix the information state.** Write down everything the agent knows *at decision time*, including any observations already made. Call it $E$.
3. **Build a joint credence model** $P(\cdot \mid E)$ over acts, states, and outcomes. Crucially, this model must say how the agent's own choice relates to other variables: to predictors, to twins, and to whatever processes produced her dispositions.
4. **Condition on each act as if it were an observation:** compute $V(a) = \mathbb{E}[u \mid a, E]$.
5. **Choose** $\arg\max_a V(a)$.

Two gaps need patching.

**(a) Zero-probability acts.** If $P(a\mid E)=0$, the conditional is undefined. My recommendation is to define $V(a)$ as a limit. Perturb the agent's self-model so that she "trembles" to every option with probability $\varepsilon>0$, while leaving every other dependency in the model intact, and let $\varepsilon\to 0$. Primitive conditional probabilities (Popper functions) do the same job. The justification is that EDT's question, "how good would it be to learn I did $a$?", stays meaningful when $a$ is unlikely, and continuity is the natural way to answer it.

**(b) Self-knowledge during deliberation.** If the agent already knows which act she will take, conditioning on it is uninformative. If she knows too much about her own internal state, many correlations get "screened off" (see §6). I propose that the relevant credence is the one the agent has *at the moment of choice, before learning her own output*, conditioned on all information she actually possesses. This is an interpretive choice, and §6 shows that it matters.

## 5. The canonical cases

### 5.1 Newcomb's problem (source, with extensions)

A predictor that is right 99% of the time has placed \$1,000,000 in opaque box B if and only if it predicted you would take only B. Transparent box A holds \$1,000. You choose between taking B alone and taking both boxes.

The source's calculation is:

$$
\begin{aligned}
V(\text{one-box}) &= 0.99 \times 1{,}000{,}000 + 0.01\times 0 = 990{,}000,\\
V(\text{two-box}) &= 0.01 \times 1{,}001{,}000 + 0.99 \times 1{,}000 = 11{,}000.
\end{aligned}
$$

EDT one-boxes. Taking one box is strong evidence that the predictor foresaw it, and so evidence that B is full.

*A threshold (my addition).* Let the accuracy be $p$ for both kinds of prediction. Then

$$
V(\text{one}) = 10^6 p, \qquad V(\text{two}) = (1-p)(1{,}001{,}000) + 1{,}000p = 1{,}001{,}000 - 10^6 p,
$$

so EDT one-boxes iff $p > 0.5005$. A predictor only slightly better than chance suffices, because the prize is so large relative to the \$1,000.

*CDT's verdict.* Let $q$ be the unconditional credence that B is full. Your choice cannot change the contents, so

$$
U(\text{two}) = q(1{,}001{,}000) + (1-q)(1{,}000) = U(\text{one}) + 1{,}000
$$

for every $q$. Two-boxing causally dominates, so CDT two-boxes. The disagreement comes entirely from the weights: EDT uses $P(\text{full}\mid a)$, which varies with $a$, while CDT uses $q$, which does not.

### 5.2 The twin prisoner's dilemma (source, with extensions)

Aomame and her psychological twin are in separate rooms. Mutual cooperation pays each \$5, mutual defection pays \$1, and a lone defector gets \$10 while the lone cooperator gets \$0. If the twin's reasoning exactly mirrors hers, then $P(\text{twin } C\mid C)=1$ and $P(\text{twin } C\mid D)=0$, giving

$$
V(C) = 5,\qquad V(D) = 1.
$$

EDT cooperates. CDT notes that the twin's choice is causally independent of Aomame's and that defection dominates, so it defects.

*Imperfect twins (my addition).* Let $r = P(\text{twin }C\mid C)$ and $s = P(\text{twin }C\mid D)$. Then

$$
V(C) = 5r, \qquad V(D) = 10s + (1-s) = 1 + 9s.
$$

EDT cooperates iff $5r > 1 + 9s$. With symmetric reliability $r = 1-s = p$, the condition becomes $p > 5/7 \approx 0.714$. The general lesson is that EDT's verdict depends continuously on how strongly the agent's act and the other agent's act are correlated *in her own credences*. Exact copies are not required, only enough evidential coupling. This is the decision-theoretic core of Hofstadter's "superrationality".

### 5.3 A case where EDT and CDT agree

Should you take an umbrella? Rain is not correlated with your umbrella-taking except through forecasts you have already observed and included in $E$. So $P(\text{rain}\mid \text{umbrella}, E) = P(\text{rain}\mid E)$, and EDT reduces to Savage. Most everyday decisions look like this. The disputes concern a narrow but theoretically important class of problems.

## 6. The smoking lesion and the tickle defense (my addition)

The source quotes David Lewis's charge that EDT promotes "an irrational policy of managing the news". The standard illustration is the *smoking lesion*, which the source does not discuss. Suppose a genetic lesion causes both a desire to smoke and cancer, and smoking itself is harmless and pleasant. Then $P(\text{cancer}\mid\text{smoke}) > P(\text{cancer}\mid\neg\text{smoke})$. Naively, EDT seems to tell you to abstain so as to avoid the "bad news" of smoking, which looks absurd because abstaining does nothing to your genes.

A numerical sketch makes the worry concrete. Smoking adds 1 util and cancer costs 100. Suppose $P(\text{cancer}\mid S) = 0.3$ and $P(\text{cancer}\mid \neg S) = 0.1$. Then

$$
V(S) = 1 - 30 = -29, \qquad V(\neg S) = -10,
$$

and naive EDT abstains.

The evidentialist's standard reply is the **tickle defense** (Eells and others). The lesion can only influence your choice by influencing something in your deliberation, such as a felt desire, a "tickle". You can introspect that desire. Once you condition on its presence or absence (it belongs in $E$, step 2 of the procedure), the act carries no further information about the lesion:

$$
P(\text{cancer}\mid S, \text{tickle}) = P(\text{cancer}\mid \neg S, \text{tickle}).
$$

With the correlation screened off, EDT smokes, in agreement with CDT.

This shows why §4(b) matters. EDT's verdicts depend on what the agent knows about her own decision process. The tickle defense works only if every route from the common cause to the act passes through something the agent can observe. Is the same true of Newcomb? If the predictor reads exactly the deliberative states you can introspect, a parallel argument would screen off the evidence there too and make EDT two-box. Most evidentialists, Ahmed (2021) among them, argue that the Newcomb correlation is *not* screened off in this way, because the predictor tracks your actual choice, the output of deliberation, rather than any input you could inspect beforehand. On my reading, the honest operational position is this. **The verdict depends on the causal-informational structure you posit between the agent's introspectible states and her act.** Applying EDT requires stating that structure explicitly; you cannot just read conditional frequencies off population data.

## 7. Acts versus policies (my addition)

The source states EDT for *actions*. In sequential problems it matters whether you condition on the act taken *now* or on a *policy*, meaning a function from observations to acts, chosen in advance.

Consider **transparent Newcomb**. Both boxes are visible, and the predictor fills B iff it predicts you would one-box *upon seeing B full*. Suppose you see B full. Conditional on that observation, $P(\text{full}\mid \text{one-box}, E) = P(\text{full}\mid\text{two-box}, E) = 1$. Act-level EDT therefore two-boxes and gains the extra \$1,000. But a reliable predictor anticipates this and leaves B empty for act-level evidentialists. Now evaluate policies $\pi$ from the prior standpoint, $V(\pi) = \mathbb{E}[u\mid\pi]$. The policy "one-box when B is full" has news value near \$1,000,000, while "two-box when B is full" has news value near \$1,000.

So act-EDT and policy-EDT come apart. Which is "EDT"? The source does not say. Here is my proposal:

- Read *standard* EDT as act-level, conditioning on all evidence at decision time. This is Jeffrey's original framework and what the formula $V(A)$ literally says.
- Recognize policy-level ("updateless") evidential reasoning as a distinct extension. It is attractive when the agent can commit in advance or when predictors respond to her dispositions, but it needs extra assumptions: a privileged prior, and a choice of what counts as the agent's policy.

This distinction resolves cases that would otherwise look like counterexamples or ambiguities. Ask: "Is the agent choosing a single act with present evidence, or choosing a disposition before the evidence arrives?"

## 8. Sleeping Beauty and Dutch books (source)

The source reports that EDT has been brought to bear on the Sleeping Beauty problem. A fair coin decides whether Beauty is woken once (heads) or twice with memory erasure (tails), and the question is her credence in heads on waking. "Halfers" answer 1/2. It has been argued that halfers can be Dutch-booked: a bookie offers bets at each awakening, and because Beauty bets twice on tails-worlds, a halfer pricing bets at 1/2 loses money for sure.

The proposed fix is to pair halfing with EDT. When Beauty accepts a bet at one awakening, that acceptance is evidence that she accepts the identical bet at the other awakening in the tails world, since she reasons identically. An EDT halfer therefore counts the tails payoff twice. The doubling exactly offsets the lower credence, and her betting behavior matches that of a thirder who uses CDT. This removes the original Dutch book.

The source notes that Vincent Conitzer (2015) argues this escape is incomplete. He constructs a variant betting scenario in which EDT Sleeping Beauties are still exploitable, so on his view halfers remain vulnerable even after adopting EDT. The broader lesson is that EDT's verdicts in problems involving copies or memory loss depend sensitively on how the agent's credences link her choices across instances. This is the same coupling that drives the twin case.

## 9. The evidentialist's wager (source, formalized by me)

The source mentions an argument by MacAskill, Vallinder, Oesterheld, Shulman, and Treutlein (2021). Even if you are unsure whether EDT is correct, you may have reason to *act* as if it were, because its stakes can be much larger.

Here is a stylized version. Suppose your decision is evidentially correlated with those of $N$ similar agents, and each correlated agent's choice yields value difference $\delta$ between options. By EDT's lights, your choice is evidence about all $N$ choices, so the difference between options is roughly $N\delta$. By CDT's lights, you affect only your own outcome, giving roughly $\delta$. If you assign credence $c$ to EDT and $1-c$ to CDT, and maximize expected choiceworthiness across theories (itself a contestable assumption, since it requires intertheoretic value comparisons), the EDT-favored option wins when

$$
c\, N \delta_{\text{EDT}} > (1-c)\,\delta_{\text{CDT}},
$$

which holds for large $N$ even when $c$ is small. In a large universe containing many agents like you, $N$ may be enormous. The argument is not a defense of EDT's *correctness*. It is a claim about how to act under normative uncertainty.

## 10. Criticism (source)

The main objection, quoted in the source, is Lewis's: EDT promotes "an irrational policy of managing the news". James Joyce makes the same point: "Rational agents choose acts on the basis of their *causal efficacy*, not their auspiciousness; they act to *bring about* good results even when doing so might betoken bad news." On this view, one-boxing in Newcomb is like refusing to look at a medical test so as not to receive bad news. Changing your evidence does not change the world.

Evidentialists have several replies (my summary).

1. **The "why ain'cha rich?" retort.** In repeated Newcomb trials, one-boxers walk away with roughly \$990,000 and two-boxers with roughly \$11,000. A theory that predictably does worse in a fair, specified problem owes an explanation.
2. **The tickle defense** (§6). It removes many alleged counterexamples, such as the smoking lesion, by insisting that the agent condition on everything she knows about herself.
3. **Parsimony.** EDT needs only credences and utilities. CDT needs, in addition, a primitive notion of causal or counterfactual dependence, which is philosophically contested and hard to apply when agents are copies or predicted computations.

Causalists reply that the "rich" argument is unfair: the predictor rewards irrationality. They also argue that the tickle defense is fragile, because it fails whenever introspection is imperfect. Neither side has decisively won. The disagreement is real and comes down to whether rational choice should track *what your act indicates* or *what your act brings about*.

## 11. A checklist for unfamiliar cases

Drawing the above together, to apply EDT to a new problem:

1. List the acts and the payoff-relevant states.
2. Specify your information at decision time, including introspective information about your own motives.
3. Ask whether any state is correlated with your act *beyond* your causal influence on it. Such correlations can come from predictors, copies, common causes, or other agents running similar reasoning.
4. Check for screening off. Given everything you know, does the act still carry information about that state? If not, EDT behaves like CDT for that state.
5. Decide whether the problem is about a single act given current evidence (act-EDT) or a committed disposition (policy-level evidential reasoning). State the choice explicitly.
6. Compute $V(a) = \sum_s P(s\mid a, E)\,u(a,s)$ and maximize, using the trembling limit for zero-probability acts.
7. As a sanity check, compute CDT's $U(a)$ too. If the two agree, the case is uncontroversial. If they disagree, you have found exactly the kind of problem the EDT–CDT debate is about.

## 12. Conclusion

EDT is expected-utility theory with one change: weight outcomes by their probability *conditional on your act*. That change makes the theory elegant. It is partition-invariant, needs no causal primitives, and reduces to Savage whenever acts carry no information about states. The same change makes it controversial, because it lets correlation without causation influence choice. In Newcomb's problem and the twin prisoner's dilemma this yields one-boxing and cooperation, verdicts its defenders regard as vindicated by results and its critics regard as "managing the news". Applying EDT well requires careful modeling of what the agent knows about her own deliberation, a clear decision about whether acts or policies are being evaluated, and a principled treatment of improbable options. With these specified, EDT yields a determinate verdict in any well-posed case.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9): 2887–2899.
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press, p. 146.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C., & Treutlein, J. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," revision 1373679688 (CC BY-SA 4.0).