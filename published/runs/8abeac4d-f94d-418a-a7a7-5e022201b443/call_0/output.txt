# Evidential Decision Theory: Choosing the Best News

## 1. The slogan and the idea

Evidential decision theory (EDT) answers the question "what should I do?" with an unusual instruction: **do what you would most like to learn that you will do.** Arif Ahmed uses this slogan in his book on the theory (Ahmed 2021, p. 7). An action is evaluated by its *news value*: how good the world can be expected to be, given the news that you take that action.

Usually the slogan sounds like ordinary expected-utility reasoning. Learning that I will take my umbrella is good news about staying dry, because taking the umbrella keeps me dry. The theory becomes distinctive, and controversial, in cases where an action is *evidence* about the world without *causing* anything in it. In such cases EDT says to act on the evidence. Its main rival, causal decision theory (CDT), says to act only on what the action brings about.

This essay sets out:

- the formal definition;
- how it applies to the standard test cases;
- how it handles (or declines to handle) dependence and counterfactuals;
- several questions the standard presentation leaves open.

Where I go beyond what the reference article (the Wikipedia entry on EDT) states, I say so explicitly.

## 2. The formal definition

### 2.1 News value

Following the distinction drawn by Gibbard and Harper (1976), which the reference article cites, EDT ranks each available action $A$ by

$$
V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j),
$$

where:

- $\{O_j\}$ is a partition of possible outcomes;
- $D(O_j)$ is the desirability (utility) of outcome $O_j$;
- $P(O_j \mid A)$ is the agent's conditional credence in $O_j$ given that she performs $A$.

The prescription is to choose $A^\* \in \arg\max_A V(A)$.

The essential ingredient is the ordinary conditional probability

$$
P(O_j \mid A) = \frac{P(O_j \wedge A)}{P(A)} .
$$

To use it, the agent needs a joint probability distribution over her own actions and the rest of the world. Her action is treated as one more event she can learn about, and $P(\cdot \mid A)$ is how she would revise her beliefs on learning it. Nothing in the formula mentions causation, intervention, or counterfactual dependence.

### 2.2 The causal contrast

CDT replaces the conditional probability with the probability of a counterfactual:

$$
U(A) \;=\; \sum_j P(A \mathrel{\Box\!\!\rightarrow} O_j)\, D(O_j),
$$

where $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ is the probability that $O_j$ *would* obtain *if* $A$ were performed. The reference article stresses that $P(A \mathrel{\Box\!\!\rightarrow} O_j)$ and $P(O_j \mid A)$ need not be equal. The two theories therefore come apart.

### 2.3 When do they agree? (my reformulation)

A states-and-acts version makes the relationship precise. Suppose:

- the world has a state $S$ from a partition $\{S_1,\dots,S_n\}$, which the agent's action does not causally influence;
- the outcome is a function $o(A,S)$, with utility $u(A,S) = D(o(A,S))$.

Then a standard Savage-style CDT computes

$$
U(A) = \sum_i P(S_i)\, u(A, S_i),
$$

while EDT computes

$$
V(A) = \sum_i P(S_i \mid A)\, u(A, S_i).
$$

**Proposition (agreement under evidential independence).** If $P(S_i \mid A) = P(S_i)$ for every state $S_i$ and every action $A$, then $V(A)=U(A)$ for all $A$, and the two theories make identical recommendations.

The proof is immediate. The proposition explains why the theories agree in "many cases", as the reference article puts it. In ordinary decisions, my choice tells me nothing about states of the world it does not affect.

Disagreement requires two things together:

1. acts that are **evidentially relevant** to states, so that $P(S\mid A)\ne P(S)$;
2. those same acts being **causally irrelevant** to the states.

That combination arises when something other than the act causes both the act and the state:

- a common cause;
- a predictor who has modelled the agent;
- a twin running the same reasoning.

Every famous divergence case has this structure.

### 2.4 A technical caveat about outcomes (my clarification)

The formula $\sum_j P(O_j\mid A)D(O_j)$ presupposes that outcomes are described finely enough that their desirability does not depend on which act produced them. In Newcomb's problem, "I receive \$1,000,000" is a fine-grained enough outcome. "Box B is full" is not, because its value depends on whether I also take box A.

Richard Jeffrey's original formulation of news value avoids this problem by being defined on arbitrary propositions. It satisfies

$$
V(A)=\sum_i P(S_i\mid A)\,V(A\wedge S_i)
$$

for *any* partition $\{S_i\}$. This property is called partition invariance, and it is a real attraction of EDT. CDT in Savage form, by contrast, needs a privileged partition of act-independent states.

In practice, to apply EDT safely, either:

- make outcomes maximally specific, or
- use states paired with the act-dependent utility $u(A,S)$, as above.

## 3. Worked cases

### 3.1 Newcomb's problem

The reference article's setup is as follows. A predictor with 99% accuracy has filled an opaque box B with \$1,000,000 if it predicted you would take only B, and left it empty otherwise. Transparent box A always holds \$1,000. You choose between taking B alone and taking both boxes.

The states are $F$ (B full) and $E$ (B empty). The predictor's reliability makes the state correlated with your act:

$$
P(F\mid \text{one-box}) = 0.99,\qquad P(F\mid\text{two-box}) = 0.01 .
$$

The news values are

$$
\begin{aligned}
V(\text{one-box}) &= 0.99(\$1{,}000{,}000) + 0.01(\$0) = \$990{,}000,\\
V(\text{two-box}) &= 0.01(\$1{,}001{,}000) + 0.99(\$1{,}000) = \$11{,}000.
\end{aligned}
$$

EDT therefore recommends one-boxing.

CDT reasons differently. The contents of box B are already fixed, so $P(F)$ is the same whichever act is evaluated. For any value $P(F) = f$,

$$
U(\text{two-box}) - U(\text{one-box}) = \$1{,}000 > 0 .
$$

Two-boxing dominates, and CDT recommends it.

**How robust is the EDT verdict?** (My generalization.) Let:

- the predictor be correct with probability $p$ regardless of your choice;
- the prize be $M$;
- the sweetener be $K$.

Then

$$
V(\text{one}) = pM,\qquad V(\text{two}) = (1-p)(M+K) + pK = (1-p)M + K .
$$

One-boxing wins iff $(2p-1)M > K$, that is,

$$
p > \tfrac12 + \tfrac{K}{2M}.
$$

With the standard numbers the threshold is $p > 0.5005$. A predictor only slightly better than a coin suffices. EDT's verdict does not depend on near-infallible prediction. It depends only on your act being *some* evidence about the prediction.

### 3.2 The twin prisoner's dilemma

The reference article presents this case, drawn from Greene and Levinstein. Aomame and her psychological twin, whose reasoning mirrors hers, each choose to cooperate (C) or defect (D) without communicating. The payoffs to Aomame are:

| | Twin C | Twin D |
|---|---|---|
| **Aomame C** | \$5 | \$0 |
| **Aomame D** | \$10 | \$1 |

The reference article assumes perfect correlation. Under that assumption $V(C) = \$5$ and $V(D) = \$1$, so EDT recommends cooperation. CDT notes that defection dominates and that Aomame's choice cannot causally affect her twin's. It therefore recommends defection.

**Imperfect correlation** (my extension). Let $q = P(\text{twin C}\mid C) = P(\text{twin D}\mid D)$. Then

$$
V(C) = 5q,\qquad V(D) = 10(1-q) + q = 10 - 9q .
$$

Cooperation is favoured iff $14q > 10$, that is, iff $q > 5/7 \approx 0.714$.

This threshold shows something important about how EDT should be applied. The relevant quantity is not "is the other player similar to me?" but a specific conditional credence. It must be high enough relative to the payoff structure.

This connects EDT to Hofstadter's notion of superrationality: symmetric reasoners who recognise their symmetry cooperate. EDT is not committed to universal cooperation in prisoner's dilemmas. Against an opponent whose choice is independent of yours, $P(\text{twin C} \mid C) = P(\text{twin C} \mid D)$, the proposition in §2.3 applies, and EDT defects just as CDT does.

### 3.3 The smoking lesion: EDT's hardest standard test (not in the reference article)

The reference article's criticism section quotes David Lewis's charge that EDT promotes "an irrational policy of managing the news." The case that most sharply motivates this charge is the smoking lesion. I introduce it because no essay that aims to let readers decide unfamiliar cases can omit it.

Suppose:

- a genetic lesion $L$ causes both cancer and a desire to smoke;
- smoking itself is harmless;
- smoking gives utility $+10$;
- cancer costs $-1000$.

Let

$$
P(L\mid \text{smoke}) = 0.8,\qquad P(L\mid \neg\text{smoke}) = 0.2,
$$

and suppose cancer occurs iff $L$. A naive EDT calculation gives

$$
V(\text{smoke}) = 10 - 800 = -790,\qquad V(\neg\text{smoke}) = -200,
$$

so it recommends abstaining. That looks like trying to avoid bad news rather than bad outcomes. Abstaining does nothing to the lesion.

**The tickle defence.** The standard EDT reply, due to Eells and others, is that the naive calculation conditions on the wrong information. The lesion influences behaviour only *through* the agent's desires and beliefs. By the time she deliberates, she can observe these, through the "tickle" of the urge to smoke. Let $T$ be her actual introspective state. If the lesion's influence on the act is fully mediated by $T$, then conditional on $T$ the act carries no further information about $L$:

$$
P(L\mid \text{smoke}, T) = P(L\mid \neg\text{smoke}, T) = P(L\mid T).
$$

By the proposition in §2.3, EDT then agrees with CDT and recommends smoking: the $+10$ is free.

**My assessment.** The tickle defence is the correct way to apply EDT. EDT tells you to condition on your *total evidence*, and that evidence includes what you know about your own motivational state. The defence does not fully settle the dispute, for two reasons:

1. **It is an empirical-psychological bet.** It assumes that the common cause works only through states the agent has introspective access to. Variants with an unobservable mechanism resist it. In those variants committed evidentialists typically "bite the bullet" and abstain.
2. **The same move does not dissolve Newcomb.** The predictor's evidence about you is plausibly *not* exhausted by anything you can introspect before choosing. It tracks the decision procedure itself. So conditioning on your current mental state leaves $P(F\mid\text{one-box}) > P(F\mid\text{two-box})$.

EDT's defenders regard this asymmetry as a feature. In the lesion case your choice really is uninformative once you know yourself. In Newcomb's problem it is not.

## 4. Dependencies and counterfactuals: what EDT does and does not model

The reference article frames the EDT/CDT divergence as conditional probability versus counterfactual probability. Stated plainly, EDT treats the following uniformly:

- **causal** dependence (umbrella → dryness);
- **common-cause** correlation (lesion → smoking and cancer);
- **predictive** correlation (your disposition → predictor's forecast);
- **logical or computational** correlation (your algorithm = your twin's algorithm).

All of these enter through the single quantity $P(O\mid A)$. EDT needs no counterfactual semantics, no causal graph, and no notion of intervention.

This economy is one of EDT's selling points. Counterfactuals are notoriously hard to make precise. Conditional probability is well defined whenever $P(A)>0$.

The economy has a cost. EDT cannot by itself distinguish "my act would bring this about" from "my act merely indicates this." The critics' complaint is precisely that this distinction is what rational choice should track. Joyce, as quoted in the reference article, puts it this way: rational agents "act to *bring about* good results even when doing so might betoken bad news."

The evidentialist reply, which Ahmed develops, has two parts:

- From the deliberating agent's own point of view, the only thing she ever gets is a correlation between choices and outcomes.
- The one-boxers tend to end up richer.

In a causal Bayesian network the contrast can be stated exactly. EDT uses $P(O\mid A)$, the observational conditional. Interventionist CDT uses $P(O\mid \mathrm{do}(A))$. The two coincide when no back-door path links $A$ to $O$, meaning there is no confounding of the act. Every EDT/CDT divergence case is a case of confounding by something upstream of the agent's choice.

## 5. Open questions and operational proposals

The reference article gives the defining formula but not the details needed to apply it in hard cases. Below are the main gaps, each with what I take to be a reasonable resolution. These resolutions are my own synthesis, though most track proposals in the literature.

### 5.1 Which probability function? The problem of self-prediction

To compute $P(O\mid A)$, the agent needs credences about her own action. Mid-deliberation, those credences are unstable. If she becomes confident she will do $A$, does that change the evidential significance of $A$?

**Operational proposal.** Use the agent's credences *at the start of deliberation, updated on all evidence available then* (including introspective evidence, as in §3.3), but not on any partial conclusion of the deliberation itself.

If the conditional probabilities are themselves sensitive to the agent's credence in her own act, iterate. Update credences in the direction of the currently favoured act and recompute until a fixed point is reached; this follows the "deliberational dynamics" of Eells, Skyrms and Arntzenius. Recommend an act that is stable under this process. If none is stable, recommend the mixed equilibrium.

### 5.2 Zero-probability acts

If the agent is certain she will not do $A$, then $P(O\mid A)$ is undefined. A fully self-transparent agent might be in this position for every act but one.

**Options:**

- (a) Use a primitive conditional probability function (a Popper function) defined even on null conditions.
- (b) Require, as a rationality constraint, that every live option gets positive credence during deliberation.
- (c) Take a limit of $\epsilon$-perturbed credences in which each act is performed by a small "tremble."

I favour (b) together with (c). They match the deliberative stance, in which options are open precisely because the agent has not yet settled what to do. They also make $V$ well defined in all cases.

### 5.3 Acts or policies?

The reference article's formula ranks *acts* given current evidence. Some problems involve information that arrives before the choice. A key example is a "transparent" Newcomb problem, in which you see box B's contents before choosing.

Act-level EDT, having seen a full box, conditions on that fact. Then $P(F\mid\text{two-box}, F)=1$, and two-boxing gains \$1,000. So it two-boxes. A predictor who anticipates this leaves the box empty, and act-level evidentialists do badly.

One can instead evaluate *policies* $\pi$, which map observations to acts, from the prior standpoint:

$$
V(\pi)=\sum_j P(O_j\mid \pi)\,D(O_j).
$$

This "updateless" variant one-boxes even with transparent boxes.

The source does not address the choice between these versions. I regard policy-level evaluation as a distinct theory: a natural extension of EDT, but not EDT as standardly formulated. When applying EDT to a new case, state which version you are using whenever the agent receives information that a predictor or twin could have anticipated.

### 5.4 Anthropic and self-locating cases

The reference article notes two things:

- EDT has been invoked in the Sleeping Beauty problem to protect "halfers" (who assign credence $1/2$ to heads on waking) against Dutch books.
- Conitzer (2015) argues that halfers remain Dutch-bookable even when they adopt EDT.

The general lesson I draw is this. When several of the agent's decisions are correlated, because she may be making the "same" decision on multiple awakenings, EDT's verdicts depend jointly on:

- the self-locating credences used;
- how the payoffs of correlated decisions are aggregated.

EDT does not settle the self-locating probability question for you. It inherits whatever answer you bring to it, and its pragmatic consequences constrain which combinations are coherent.

## 6. An argument from uncertainty: the evidentialist's wager

The reference article cites MacAskill, Vallinder, Oesterheld, Shulman and Treutlein (2021), who argue that even someone with modest credence in EDT should often act as an evidentialist. Here is a stylised version; the formalisation is mine.

Suppose there are $N$ agents whose decisions are strongly correlated with yours, for instance agents running similar reasoning in a large universe. Each choice yields a local gain $g$. Then:

- by CDT's lights, your choice changes total value by about $g$;
- by EDT's lights, your choice is evidence about all $N$ correlated choices, so the evidential stake is about $Ng$.

Let $c$ be your credence in EDT. If you handle normative uncertainty by maximizing expected choiceworthiness across theories, the EDT term contributes roughly $cNg$, which dominates $(1-c)g$ whenever $N \gg (1-c)/c$.

The argument depends on contested assumptions:

- that values can be compared across theories;
- that the universe is large;
- that it contains genuinely correlated agents.

Still, it shows that EDT's verdicts can matter disproportionately even for causalists who are not certain of their view.

## 7. A procedure for unfamiliar cases

Combining the above, here is a recipe for applying (act-level) EDT to an unfamiliar case.

1. **List the options** $A_1,\dots,A_m$.
2. **Choose an outcome or state partition** fine enough that utilities are act-independent given outcomes. Alternatively, use states with $u(A,S)$ (§2.4).
3. **Build the joint credence** over acts and states, conditioning on *all* evidence available at decision time, including introspective evidence about your own desires and dispositions (§3.3, §5.1).
4. **Check for evidential relevance.** If $P(S\mid A)=P(S)$ for every $A$, the problem is "ordinary" and EDT equals CDT. Otherwise, identify the source of correlation: causal, common-cause, predictive, or computational.
5. **Ensure every option has positive probability** (§5.2), then compute $V(A_i)=\sum_S P(S\mid A_i)u(A_i,S)$.
6. **Check stability.** If the conditionals shift as your credence in your own choice shifts, run the deliberational iteration (§5.1).
7. **Do a threshold analysis.** Compute the correlation strength at which the verdict flips, as in $p>\tfrac12+\tfrac{K}{2M}$ or $q>5/7$. This shows how sensitive the recommendation is to your probabilistic model.
8. **Flag information-before-choice structure.** If a predictor could anticipate how you respond to observations, report both the act-level and policy-level verdicts (§5.3).

## 8. Conclusion

Evidential decision theory is expected-utility maximization with the agent's own action treated as a proposition to be conditioned on. Its formula,

$$
V(A)=\sum_j P(O_j\mid A)D(O_j),
$$

is simpler and less metaphysically loaded than its causal rival's. It agrees with CDT whenever acts carry no evidence about states they do not affect. It diverges, recommending one-boxing in Newcomb's problem and cooperation with a sufficiently correlated twin, exactly when some upstream factor (a predictor, a shared algorithm, a common cause) ties the agent's choice to the world.

The central objection, from Lewis and Joyce, is that EDT confuses signalling good outcomes with producing them. The smoking lesion is the sharpest version of that objection. The tickle defence answers much of it by insisting on total evidence, though not all of it.

Applying EDT carefully requires settling questions the bare formula leaves open:

- which credence function to use during deliberation;
- how to handle zero-probability acts;
- whether to evaluate acts or policies.

I have proposed answers. Readers should treat them as defensible operationalizations rather than as part of the theory's canonical core. With these specifications in place, EDT becomes a usable procedure. Its verdicts in any new case reduce to a precise and checkable question: how much does my choosing this tell me about the things I care about?

---

**References**

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9).
- Gibbard, A. & Harper, W. (1976). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1).
- MacAskill, W., Vallinder, A., Oesterheld, C., Shulman, C. & Treutlein, J. (2021). "The Evidentialist's Wager."
- Wikipedia contributors, "Evidential decision theory," revision 1373679688 (CC BY-SA 4.0).