# Choosing on the Evidence: An Essay on Evidential Decision Theory

## 1. The basic idea

Suppose you are about to make a decision, and you can imagine a friend who knows you well — knows your habits, your psychology, your circumstances — telling you, before you decide, "You are going to choose option A." How pleased should you be to hear that news? Evidential decision theory (EDT) answers: the value of an action *is* how pleased you should be to learn you will take it. The slogan, due to Arif Ahmed, is that a rational agent should "do what you most want to learn that you will do" (Ahmed 2021).

This is a genuinely different question from the one most people assume decision theory answers. The familiar question is: *if I do A, what will happen as a result?* The evidential question is: *if I learn I will do A, what should I infer about how well things will go?* These come apart whenever my action is informative about things that are not consequences of my action — when my choice correlates, perhaps as mere symptom rather than cause, with good or bad outcomes elsewhere.

The formal statement goes back to Gibbard and Harper (1976), who distinguished two kinds of expected utility. EDT evaluates an action $A$ by its *conditional* expected utility, sometimes called its **news value**:

$$V(A) \;=\; \sum_j P(O_j \mid A)\, D(O_j),$$

where $O_1, \dots, O_n$ are a partition of the possible outcomes, $D(O_j)$ is the desirability of outcome $O_j$, and $P(O_j \mid A)$ is the agent's conditional credence that $O_j$ obtains, given (supposing as news) that she performs $A$. The agent should choose the $A$ maximizing $V(A)$.

Contrast this with the counterfactual expected utility used by causal decision theory (CDT):

$$U(A) \;=\; \sum_j P(A \,\Box\!\!\rightarrow\, O_j)\, D(O_j),$$

where $P(A \,\Box\!\!\rightarrow\, O_j)$ is the agent's credence in the subjunctive conditional "were $A$ done, $O_j$ would obtain." The conditional $P(\cdot \mid A)$ and the counterfactual $P(A \,\Box\!\!\rightarrow\, \cdot)$ agree in many ordinary cases but diverge systematically: conditioning is evidential (updating on a proposition as an observation), while the counterfactual is causal (hypothetically intervening to make $A$ true while holding fixed the causal background). EDT uses the former throughout; this single choice drives every difference between the theories.

## 2. Two canonical cases

### 2.1 Newcomb's problem

A predictor with 99% accuracy has already placed $1{,}000{,}000 in opaque box B if and only if she predicted you will take only B; transparent box A always contains $1{,}000. You may take both boxes or only B. The prediction is already fixed, so nothing you do now *causally* changes the contents of B.

EDT reasons as follows. That you will take only B is excellent news: it is 99% likely to mean the predictor foresaw this, so

$$
\begin{aligned}
V(\text{one box}) &= 0.99 \times \$1{,}000{,}000 + 0.01 \times \$0 = \$990{,}000,\\
V(\text{both boxes}) &= 0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 = \$11{,}000.
\end{aligned}
$$

One-boxing dominates on news value, so EDT prescribes one-boxing. CDT prescribes two-boxing: conditional on the contents of B already being what they are, your act is causally inert with respect to them, and two boxes are always better than one. EDT, by contrast, treats your choice as evidence about the prediction — and hence about the money — because in your epistemic situation the two are strongly correlated, even though no causal arrow runs from your hand to the box.

It is worth pausing on *why* the correlation licenses the conditional probability here, since this is the crux. In the standard setup, the correlation is mediated by the predictor's model of your decision procedure. Your choice and the box contents have a common cause: your dispositions, deliberation style, or earlier state. Conditioning on "I will one-box" is legitimate evidence about that common cause, and hence about the box. We will return to cases where this evidential inference is more suspect.

### 2.2 The twin prisoner's dilemma

Aomame faces a prisoner's dilemma against her psychological twin, locked in a separate room, whose reasoning is exactly analogous to hers. Payoffs per player: cooperate–cooperate gives \$5 each; defect–defect gives \$1 each; unilateral defection gives \$10 to the defector and \$0 to the cooperator.

Causally, Aomame's choice cannot influence her twin, and defection strictly dominates: whatever the twin does, defecting earns \$10 rather than \$5, or \$1 rather than \$0. But evidentially, Aomame's choice is a near-perfect mirror of her twin's: if she cooperates, so almost certainly will the twin. Computing news value with the idealized assumption of perfect correlation (as in the source's treatment):

$$
\begin{aligned}
V(\text{cooperate}) &= 1 \times \$5 + 0 \times \$0 = \$5,\\
V(\text{defect}) &= 0 \times \$10 + 1 \times \$1 = \$1.
\end{aligned}
$$

EDT recommends cooperating. This is no accident of the numbers: in a symmetric dilemma with correlation $r$ between the players' choices,

$$V(\text{cooperate}) = 5r + 0(1-r) = 5r, \qquad V(\text{defect}) = 10(1-r) + r = 10 - 9r,$$

so EDT cooperates exactly when $r > 10/19 \approx 0.53$. For sufficiently similar agents — and EDT does not require the twin to be *perfect*, only strongly correlated — cooperation beats defection. This connects EDT to Hofstadter's notion of superrationality and to the modern literature on "Newcomblike" interactions among correlated agents (MacAskill et al. 2021 exploit this to argue that even committed causalists have instrumental reason to attend to evidential considerations, since correlated communities of evidentialists may prosper).

## 3. What the conditional really encodes

A reader who wants to *apply* EDT to unfamiliar cases needs to be careful about what $P(O_j \mid A)$ is. It is not always easy to read off, and this is where most applications go wrong.

**First, the conditioning must be on the action as an act of *this* agent, assessed with all background knowledge.** In Newcomb, $P(\$\text{1M} \mid \text{one-box})$ is high because of the predictor's accuracy; in a variant with a useless predictor (a coin-flipper filling the box), $P(\$\text{1M} \mid \text{one-box})$ would be just the prior $1/2$, and EDT, like CDT, would prescribe two-boxing. EDT is not a theorem that one should one-box; it is a theorem that one should one-box *when one-boxing is good news*. The same holds in the twin dilemma: replace the twin with a random stranger and the correlation $r$ drops, and with it EDT's enthusiasm for cooperation.

**Second, conditioning is symmetric in a way that intervention is not.** $P(O \mid A)$ measures evidential relevance in either direction. A symptom is evidence of disease even though it does not cause the disease. This is the engine of EDT's most famous difficulty.

## 4. The smoking lesion: EDT's hardest case

The Wikipedia source (correctly) does not discuss the smoking lesion, but no essay purporting to teach the application of EDT can skip it, and I will develop it here — flagging that the analysis of this subsection goes beyond the source.

Suppose a gene causes both a craving for smoking and (independently of smoking itself) cancer. Among those with the gene, smoking is pleasurable and harmless; among those without it, smoking is harmless but joyless, and they lack the craving. So smoking causally affects nothing you care about except pleasure — but it is strong evidence that you carry the gene, and hence that you will get cancer.

Compute news values, writing $c = P(\text{cancer})$, and suppose for simplicity that among the gene-positive $P(\text{smoke}) = 0.9$ while among the gene-negative $P(\text{smoke}) = 0.1$. Then

$$P(\text{cancer} \mid \text{smoke}) = \frac{0.9c}{0.9c + 0.1(1-c)},$$

which for $c = 0.1$ is already about $0.5$ — refraining from smoking is powerful news of health. If the disvalue of cancer exceeds the value of smoking for anyone, $V(\text{refrain}) > V(\text{smoke})$, and EDT prescribes *refraining from an act that causally cannot affect whether you get cancer* — an act, moreover, whose only causal consequence is pleasure. Refraining is like "managing the news": you cannot influence the gene, but you can arrange to receive tidier information about it.

This is David Lewis's (1981) complaint that EDT promotes "an irrational policy of managing the news," and Joyce's (1999) dictum that rational agents "act to bring about good results even when doing so might betoken bad news." The charge has force precisely here: in Newcomb and the twin dilemma, the evidentially good act is at least *not causally bad* — one-boxing loses nothing causally, since the boxes are already sealed. In the smoking lesion, EDT's prescription is causally wasteful.

Can the evidentialist say anything in reply? Several moves exist in the literature; here is one that I find a reasonable operational interpretation, offered as my own reconstruction rather than the source's. The agent's conditional probability $P(\text{cancer} \mid \text{smoke})$ is computed from her *prior* evidential situation, before she has introspected her own cravings and deliberation. But a rational agent about to choose does not learn only "I will smoke"; she learns the whole trajectory of her deliberation — "I considered smoking, felt no countervailing worry, noticed I lacked the anxious self-scrutiny of the gene-free," and so on. If she conditions on the *full evidence available at the moment of choice*, much of the lesion's evidential value of the act has already been absorbed. In the limiting case where introspection reveals her genic status, $P(\text{cancer} \mid \text{smoke} \wedge \text{no gene}) = P(\text{cancer} \mid \text{no gene})$, and the evidential penalty for smoking vanishes; EDT then prescribes smoking after all. Call this the **soak-up remedy**: EDT's verdicts are correct when the conditioning event includes all the agent's self-knowledge at decision time.

This remedy works cleanly in the smoking lesion because the lesion's correlation is entirely mediated by introspectible states (cravings, temperament). It works less cleanly in Newcomb, where the predictor reads the decision procedure itself, and no amount of introspection before the act fully reveals its output — the act *is* the last piece of self-revelation. Whether the soak-up remedy generalizes, or merely shows that EDT gives the right answer in the smoking lesion for parochial reasons, is genuinely contested, and I flag it as an open question. It is also worth noting the uncomfortable asymmetry: if the remedy succeeds, part of EDT's distinctive behavior in Newcomb rests on the agent's constitutive inability to fully observe her own choice in advance — an interesting but fragile foundation.

A second response, more concessive: the evidentialist can accept that $V(A)$ misdescribes value when act and outcome are correlated by a common cause *without* the act being diagnostic of anything the agent does not already know, and can graft a "tickle"-style fix or partial causal screening into the partition of outcomes over which the sum in $V(A)$ ranges. The choice of outcome partition is a genuine freedom in the formalism — $\sum_j P(O_j \mid A)D(O_j)$ is invariant across partitions only if $D$ is an additive utility — and careful partitioning is often where the real modeling work of applying EDT lies.

## 5. A practical recipe

Distilling the above, here is how I would recommend applying EDT to an unfamiliar case.

1. **Model the dependency structure.** Identify, for each act $A$, which features of the world it is evidence about. Ask: does my doing $A$ correlate with $O_j$ because (a) $A$ is a *symptom* of a common cause (my type, disposition, the state of the world that also produced me), (b) other agents *predict* or *mirror* me (Newcomb, twins, iterated games, bargains with simulators), or (c) $A$ causally contributes to $O_j$? EDT's conditional probabilities respect all three channels; CDT's counterfactuals respect only (c) plus (a) insofar as it is held fixed.

2. **Condition on the right event.** Use $P(O_j \mid A \wedge E)$ where $E$ is everything the agent knows at choice time, including introspection. If the correlation between $A$ and $O_j$ survives after conditioning on $E$, it is genuine evidential relevance; if it evaporates, it was mere confounding to be screened off.

3. **Compute and compare.** Evaluate $V(A) = \sum_j P(O_j \mid A \wedge E) D(O_j)$ for each admissible act and choose the maximum. Check the result against causal dominance intuitions: if EDT's winner is causally dominated by the loser *and* the correlation was fully mediated by introspectible states, suspect a smoking-lesion artifact and revisit step 2.

The reader should understand that step 2's treatment of $E$ is where EDT's critics and defenders divide, and that the recipe encodes my own proposal (the soak-up remedy) as much as orthodoxy.

## 6. Open questions and criticisms, summarized

Three issues remain live.

**(i) The managing-the-news objection.** Lewis and Joyce hold that rational action aims at causal efficacy, not auspiciousness. The evidentialist's best reply, as sketched above, is that "mere auspiciousness" — correlation not screened off by the agent's total evidence — is rarer than critics suppose, and that where it is genuine (predictors, twins), tracking it is not irrational but shrewd. Whether this reply fully succeeds for smoking-lesion variants where the confounding survives all conditioning is unresolved.

**(ii) Sleeping Beauty and Dutch books.** EDT has been deployed in the Sleeping Beauty problem: it is argued that a halfing who adopts EDT can avoid Dutch books that would otherwise exploit her credence of 1/2 in heads, though Conitzer (2015) constructs Dutch books against halfers even after they adopt EDT. This shows that the connection between EDT's decision rule and probabilistic coherence is subtler than a simple "EDT immunizes you" story suggests.

**(iii) The evidentialist's wager.** MacAskill, Vallinder, Österheld, Shulman, and Treutlein (2021) argue that even agents who believe CDT is the true theory may have decisive reason to *act as evidentialists* when many correlated decision-makers face similar choices: if thousands of corrigible evidentialists each act so as to be good news for the others, the stakes of the evidential policy can outweigh those of the causal one. This is a decision-theoretic second-order application of EDT's own logic, and it recommends attention to EDT's verdicts even to its skeptics.

## 7. Conclusion

Evidential decision theory replaces the counterfactual "what would happen *were* I to do this?" with the conditional "what should I expect *given the news* that I do this?" — a single, clean change in the expected-utility formula with far-reaching consequences. It one-boxes in Newcomb's problem and cooperates with psychological twins, on the grounds that in correlated decision problems your act is a window into the world, not merely a lever on it. Its great vulnerability is the smoking lesion, where it values symptom management over causal efficacy; its best defense is that careful conditioning on the agent's total evidence at choice time dissolves many such cases, while the genuinely correlated cases that survive — predictors, twins, correlated communities — are exactly those where tracking the news is wise. Whether EDT's conditional or CDT's counterfactual is the fundamental object of rational choice remains one of decision theory's most productive disagreements; the reader equipped with $V(A) = \sum_j P(O_j \mid A)D(O_j)$, a careful model of the case's dependency structure, and a sober respect for screening-off is prepared to explore it.

### References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Conitzer, V. (2015). "A Dutch book against sleeping beauties who are evidential decision theorists." *Synthese* 192(9), 2887–2899.
- Gibbard, A. & Harper, W. L. (1976). "Counterfactuals and Two Kinds of Expected Utility." In *Foundations and Applications of Decision Theory*, pp. 7–8.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Lewis, D. (1981). "Causal Decision Theory." *Australasian Journal of Philosophy* 59(1), 5–30.
- MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). "The Evidentialist's Wager." Global Priorities Institute working paper.