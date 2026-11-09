# Causal Decision Theory: Definitions, Procedure, and Pressure Points

## 1. The core idea

Causal decision theory (CDT) says: choose the act whose *causal* consequences are best in expectation. The key word is "causal". An act can be good news without being a good thing to do. Whether you carry an umbrella is correlated with rain, but carrying one does not cause rain. CDT asks what your act would bring about, not what it would indicate.

The source gives the informal version (the apple example) and the Gibbard–Harper formalization. This essay explains both, works through the standard cases, and addresses the main open question the source flags: how to compute the counterfactual probabilities. Where I go beyond the source, I say so.

## 2. The Gibbard–Harper formula

The source states that CDT maximizes

$$U(A)=\sum_j P(A \,\square\!\!\to O_j)\,D(O_j),$$

where $D(O_j)$ is the desirability of outcome $O_j$ and $P(A\,\square\!\!\to O_j)$ is the probability of the counterfactual "if I were to do $A$, outcome $O_j$ would result." (The source writes the connective as $\to$.)

Evidential decision theory (EDT) instead uses

$$V(A)=\sum_j P(O_j\mid A)\,D(O_j).$$

The two differ exactly when the probability of the counterfactual diverges from the conditional probability. Lewis's 1976 triviality results show that no single conditional-like proposition can in general have probability equal to $P(O\mid A)$. This is part of why the counterfactual probability is a different quantity and not merely another name for the conditional probability.

Gibbard and Harper showed that the two coincide when two axioms hold, one involving conditional excluded middle, and when $A$ is probabilistically independent of the counterfactual $A\,\square\!\!\to O_j$. When the act is correlated with background facts that determine what the act would cause, independence fails and the theories split.

## 3. An operational reading: dependency hypotheses

The source leaves the algorithm unspecified. Here is the standard operational interpretation, which is widely used but is my gloss, not something the source states.

Partition the possibilities into **dependency hypotheses** $K_1,\dots,K_n$. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on your acts, covering everything outside your control. Given $K_i$, the counterfactual's truth is settled: the outcome that act $A$ would produce is $o(A,K_i)$. Then

$$U(A)=\sum_i P(K_i)\,D\big(o(A,K_i)\big).$$

The important feature is that the weights are the **unconditional** $P(K_i)$, not $P(K_i\mid A)$. This is Lewis's and Skyrms's formulation. Egan describes the same feature when he says CDT "holds fixed the agent's unconditional credences in dependency hypotheses." If the $K_i$ are fine-grained enough to screen off the act from the outcome, this equals the Gibbard–Harper quantity.

Equivalently, in Pearl's framework, $U(A)=\sum_o P(o\mid do(A))\,D(o)$. Here $do(A)$ surgically sets the act variable, cutting arrows into it from its causes while leaving everything not downstream of the act at its prior distribution. Lewis's **imaging** (the source's proposal) does the same job in possible-worlds terms. Move each world's probability to the nearest world where $A$ holds. Unlike conditioning, imaging does not re-weight worlds by how well they correlate with $A$.

The source mentions a regress objection to imaging: to image, you must know what you would believe if you were certain of $A$, and that is itself a conditional. The causal-graph reading avoids this only by taking the graph as a given input. The vagueness thus moves from the algorithm into the modeling. The theory is only as good as your causal model, and CDT supplies no method for building one.

## 4. Worked examples

### 4.1 The apple

Suppose the apple is good with probability $p$. Eating gives happiness $h>0$ if good and $-s$ if bad. Then $U(\text{eat})=ph-(1-p)s$. Not eating yields 0. Here the dependency hypotheses are "good" and "bad," and the act cannot influence which holds, so CDT and EDT agree: eat iff $ph>(1-p)s$.

### 4.2 King David and Bathsheba

This is the source's own example. The hypotheses are $K_C$ (charismatic) and $K_U$ (uncharismatic). Charisma is fixed and causes both just behavior and resistance to revolt. Summoning Bathsheba is unjust, which is evidence of being uncharismatic, so $P(K_U\mid\text{summon})>P(K_U)$. Revolt risk is $r_C$ under $K_C$ and $r_U$ under $K_U$, with $r_U>r_C$. The act itself does not change revolt risk.

- EDT computes the revolt probability from $P(K_U\mid\text{summon})$, so summoning looks dangerous and EDT abstains.
- CDT uses the unconditional $P(K_U)$ for both acts. The revolt risk is the same either way, while summoning has the added benefit of Bathsheba. CDT summons.

With numbers: let $P(K_U)=0.5$, $r_C=0.1$, $r_U=0.5$. Let Bathsheba be worth $+10$ and a revolt $-20$. The CDT value of abstaining is $-20(0.3)=-6$. The CDT value of summoning is $10-6=4$. If summoning moves $P(K_U)$ to $0.8$, the EDT value is $10-20(0.42)=1.6$ against $-8.4$ for abstaining, so EDT would still summon here. Making EDT abstain requires a harsher revolt cost or a smaller prize, but the structural point stands: CDT ignores the evidential channel entirely.

### 4.3 Newcomb's problem

Box A holds \$1,000. Box B holds \$1,000,000 iff the predictor foresaw one-boxing. Let $q$ be your unconditional credence that B is full. The dependency hypotheses are "full" and "empty," and the act does not change which obtains:

$$U(\text{two-box})=1000+q\cdot 10^6,\qquad U(\text{one-box})=q\cdot10^6.$$

Two-boxing dominates by \$1,000 for every $q$. EDT, using $P(\text{full}\mid\text{one-box})=0.99$, computes $990{,}000$ for one-boxing against $11{,}000$ for two-boxing.

Notice that the CDT verdict does not depend on predictor accuracy. That is both its logical strength, since it is a dominance argument, and the root of the standard complaint that "two-boxers end up poor."

## 5. Why philosophers favor CDT, and the strongest objections

The source reports that philosophers who must choose between the two usually prefer CDT. The motivating argument is that deliberation is about what you can bring about. In Newcomb's problem, the money is already there. A "managing the news" policy seems irrational, like refusing a medical test to avoid learning bad news.

The objections, from the source, fall into a few groups.

**Systematic loss.** In Newcomb's problem CDT agents end up with less than one-boxers. CDT proponents reply that the game rewards being predicted to be irrational, and that the one-boxer was simply offered a better game.

**Adversarial Offer (Oesterheld–Conitzer).** Two boxes each cost \$1. The seller put \$3 in each box she predicted you would *not* buy, and her accuracy is 0.75. Let $q_1,q_2$ be your credences that you'll buy box 1 or box 2, with $q_0=1-q_1-q_2$ for buying neither. The boxes' contents are fixed, so the credence that box $i$ is full is the probability the seller predicted you wouldn't buy it. Averaging the two boxes, at least one is full, so the mean causal expected content is at least \$1.50, which exceeds the \$1 price. CDT therefore says to buy some box. But evidentially, whichever box you buy is empty with probability 0.75, so you expect $0.25\cdot3-1=-\$0.25$ per purchase. The seller profits systematically.

A subtlety, which is my own analysis: if your credences about your own choice are not fixed, they should move as you deliberate. For CDT to recommend a particular box, it must find that box's causal expected value above \$1. With credences about your own act at the equilibrium, the two values equalize, and CDT is indifferent among purchases that each have causal expectation \$1.50 or more. The loss therefore does not depend on a quirk of the tie-break.

**Death in Damascus and instability.** Death predicts your city and waits there. If you think you'll go to Aleppo, CDT says to stay in Damascus, and vice versa, so every act is unstable under CDT's own recommendation. Ratifiability (Harper) and deliberational dynamics (Joyce, Skyrms) are proposed repairs. Equilibrium mixed strategies are one such answer. A defender replies that an agent in a genuine dilemma should expect regret whatever she does. This is an "unfortunate but rational" case.

**Psychopath Button.** Paul believes only psychopaths press the button, and he fears he may be one. CDT holds his credence of being a psychopath fixed, and since pressing would kill psychopaths and thereby make the world better if he is not one, it endorses pressing. Egan and most intuition say not to press. The defender's response (Joyce) is that a CDT agent is permitted to treat information about his own inclinations as evidence. Deliberating, his credence that he is a psychopath should rise as he leans toward pressing, which flips the recommendation.

This reply is important. The theory's weakness and its flexibility sit in the same place: the credence $P(K)$ is **the agent's credence at the moment of decision**, and CDT does not by itself say how that credence should be updated during deliberation. If $P(K)$ is allowed to track one's current inclination, many counterexamples dissolve, although a few, like the Adversarial Offer, do not.

**Dutch books.** Oesterheld and Conitzer argue that CDT agents are exposed to diachronic Dutch books. A bookie can offer a sequence of bets each of which looks acceptable at its own time but which together guarantee a loss.

## 6. A recipe for unfamiliar cases

This procedure is my own summary, not from the source.

1. List the acts available to the agent.
2. Identify the causally relevant background facts the agent cannot influence. These are the candidate dependency hypotheses $K_i$.
3. For each $(A,K_i)$, determine the outcome $o(A,K_i)$, tracing only downstream causal consequences of the act.
4. Assign probabilities $P(K_i)$. These are the agent's current credences, **not** conditioned on the act under evaluation. If the case involves self-knowledge, the credences should be the ones the agent has once she has taken her own tendencies into account.
5. Compute $U(A)=\sum_i P(K_i)D(o(A,K_i))$ and choose the maximum. If every option is unstable under this recommendation, as in Damascus, apply a ratifiability or equilibrium refinement, which is an additional commitment beyond basic CDT.

**Test case: the medical correlation.** A gene causes both smoking-urge and cancer, and smoking does not cause cancer. Acts: smoke or abstain. $K$: gene or no gene. Smoking has no causal effect on cancer, so CDT's verdict reduces to the pleasure of smoking, and CDT smokes. EDT may abstain because smoking is evidence of the gene. This parallels David's case.

**Test case: the twin prisoner's dilemma.** Your twin's choice is correlated with yours but not caused by it. Holding the twin's act fixed, defection dominates, so CDT defects. If you instead regard the twin's decision as a causal consequence of the shared algorithm, as a "logical" causal link, the model changes and so does the verdict. This shows that the answer depends on the modeling, which the source mentions only briefly as the vagueness criticism.

## 7. Conclusion

CDT evaluates an act by the expectation of its causal consequences, weighting dependency hypotheses by credences not shifted by the act itself. Formally it is $U(A)=\sum_j P(A\,\square\!\!\to O_j)D(O_j)$, operationally $\sum_i P(K_i)\,D(o(A,K_i))$ or Pearl's $do$-expectation. It diverges from EDT exactly when the act is evidence about causally upstream facts. It gives the dominance verdict in Newcomb, summoning in David's case, and smoking in the gene case.

Its weaknesses are the ones the source records: dependence on an unspecified causal or counterfactual semantics, instability in cases like Death in Damascus, and apparently predictable losses in Newcomb-like and adversarial setups. Defenders respond that the theory is correct about what choosing is, and that its anomalies come from poor modeling or from games that reward irrationality. Critics respond that a theory that reliably pays to be exploited has missed something. How much weight to give each side remains open, and which side one takes depends largely on whether one thinks rational choice is about what one's act accomplishes or about what policy does well in the world as it actually is.

## References

- Gibbard & Harper (1981), "Counterfactuals and two kinds of expected utility."
- Lewis (1976), "Probabilities of conditionals and conditional probabilities"; (1981), "Causal decision theory."
- Egan (2007), "Some counterexamples to causal decision theory."
- Oesterheld & Conitzer (2021), "Extracting money from causal decision theorists."
- Joyce (2012), "Regret and instability in causal decision theory."