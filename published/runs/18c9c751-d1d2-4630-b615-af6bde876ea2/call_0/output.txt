# Causal Decision Theory: Counterfactuals, Consequences, and Their Discontents

## 1. The problem decision theory must solve

Decision theory offers a formal answer to a practical question: given uncertainty about how the world is, which action should a rational agent choose? The classical answer, inherited from Ramsey, Savage, and Jeffrey, is *expected utility maximization*: assign probabilities to states of the world, assign desirabilities (utilities) to outcomes, and choose the action whose probability-weighted average desirability is highest.

But this formula hides an ambiguity. When we compute the expected utility of an action, we must ask: *what probabilities?* The probability of each outcome *given that* the agent performs the action — i.e., the conditional probability $P(O_j \mid A)$ — is one natural candidate. Another is the probability that performing the action would *cause* or *counterfactually imply* the outcome. These come apart precisely when actions are correlated with states of the world through channels other than causation — when your action is *evidence* about how things are without being a *handle* on how things are.

**Causal decision theory** (CDT) is the thesis that rational choice maximizes expected utility computed with causal, not evidential, probabilities. **Evidential decision theory** (EDT) uses the conditionals. The two theories agree on most ordinary cases — where acts do influence outcomes, conditional probability and counterfactual probability roughly coincide — and diverge only in exotic cases where the act is correlated with a causally relevant state of the world via a common cause, a prediction, or a logical link. Which theory is correct is one of the central live debates in decision theory (Ahmed 2021; Weirich 2016).

## 2. Formal machinery

### 2.1 Gibbard–Harper expected utility

The canonical formulation (Gibbard and Harper 1981) defines the causal expected utility of act $A$ as

$$
U(A) \;=\; \sum_{j} \, P(A \,\to\, O_j)\, D(O_j),
$$

where $D(O_j)$ is the desirability of outcome $O_j$, and $A \to O_j$ is a *subjunctive conditional*: "if $A$ were (done), $O_j$ would be the case." The weight $P(A \to O_j)$ is the agent's credence in that counterfactual — the probability of the whole conditional, not the conditional probability $P(O_j \mid A)$.

This distinction matters because of Lewis's triviality result (Lewis 1976). If we try to interpret conditionals so that $P(A \to O) = P(O \mid A)$ for a rich enough class of probability functions, closed under conditionalization, the system collapses: the "conditional" can only be definable in trivial cases. So there is genuine formal room — indeed formal necessity — for the probability of a conditional to differ from the conditional probability of its consequent. CDT exploits exactly this room: it uses $P(A \to O_j)$, EDT uses $P(O_j \mid A)$. If they coincided, the two theories would be equivalent; Lewis proved they cannot coincide in general.

One technical wrinkle worth flagging: the counterfactuals used here are typically given a *Stalnaker/Lewis semantics*, where $A \to O$ is true at a world $w$ iff $O$ holds at the closest $A$-world to $w$. Under this semantics, the "conditional excluded middle" — $\,(A \to O) \vee (A \to \neg O)$ — is a validity. Gibbard and Harper showed that, given axioms including this controversial principle, if the act $A$ is statistically independent of the counterfactual $A \to O_j$, then $P(A \to O_j) = P(O_j \mid A)$, and the theories converge. All interesting divergences occur precisely where acts and counterfactuals are *not* independent — i.e., where the agent's beliefs about what she would do are entangled with her beliefs about the world.

### 2.2 The role of dependency hypotheses

A more modern formulation, associated with Lewis (1981) and developed by Joyce (1999), makes the causal structure explicit. The agent partitions her uncertainty over *dependency hypotheses* $K$ — complete specifications of which states of the world are causally relevant to (or influenced by) her act. Then

$$
U(A) \;=\; \sum_{K} P(K) \sum_{j} P(O_j \mid A \wedge K)\, D(O_j).
$$

The key feature is the *unconditional* weighting $P(K)$: the agent holds fixed her prior credence about the causal structure of the world when evaluating an act. Within each dependency hypothesis $K$, the act's effect on outcomes is computed by ordinary conditionalization; across hypotheses, the act provides no evidential leverage, because $K$ is defined to include everything that could make $A$ and the outcome correlate without $A$ causing the outcome.

This "holding fixed" is the heart of CDT — and, as we will see, the heart of the controversy.

### 2.3 Computing the counterfactual probabilities: imaging

CDT as stated does not specify an algorithm for computing $P(A \to O_j)$. Lewis (1981) proposed **imaging**: to evaluate the counterfactual $A \to O$, reassign the probability mass of each possible world $w$ not to the closest $A$-world to *the actual world*, but to the closest $A$-world *to each $w$ individually*:

$$
P_A(O) \;=\; \sum_{w \in W} P(w)\, \mathbf{1}\{O \text{ holds at } w_A\},
$$

where $w_A$ is the closest $A$-world to $w$. Imaging can be read probabilistically as a *hypothetical intervention*: conditionalizing on $A$ lets the evidence about $A$ shift probability across all propositions correlated with $A$; imaging on $A$ shifts probability only along the causal arrows out of $A$, leaving the rest of each world fixed. (Readers familiar with causal graphs will recognize imaging as the ancestor of Pearl's $do$-calculus: $P_A(\cdot)$ behaves like $P(\cdot \mid do(A))$.) Shoham noted the parallel; Pearl (2009) made it systematic.

As the source notes, imaging has a cost: it presupposes that we know, for each world, what we *would* believe if we were *certain* of $A$ — a conditional credence that may itself need to be assigned probability below 1, threatening a regress. In practice, most applications finesse this by modeling the problem with an explicit causal graph and computing $P(\cdot \mid do(A))$, which is well-defined whenever the graph is. Whether this dissolves or merely relocates the philosophical problem is a matter of debate.

## 3. CDT versus EDT: the Bathsheba case

Gibbard and Harper's example shows the divergence cleanly. King David desires Bathsheba, but fears that summoning her would provoke a revolt. He has read enough political science to know:

- Kings are either charismatic or uncharismatic; this is fixed by genetics and upbringing.
- Charismatic kings tend to act justly; uncharismatic kings unjustly.
- Successful revolts are rare against charismatic kings, frequent against uncharismatic ones — *not because of* their just or unjust acts, but because uncharismatic kings have a "sneaky, ignoble bearing" that invites rebellion.
- David does not know which type he is. Sending for Bathsheba would be unjust.

So David's action is a *symptom* of his type, not a *cause* of revolt. Causally, the arrow runs charisma → (bearing, tendency to unjust acts); charisma → revolt-risk; there is no arrow from the act to revolt risk.

- **EDT** computes $P(\text{revolt} \mid \text{summon})$: summoning is evidence of uncharisma, hence evidence of revolt. Expected utility favors abstaining.
- **CDT** computes the counterfactual: *if David were to summon her* (holding fixed his type), the probability of revolt would be whatever it is given his type — unchanged by the act, since the act does not cause the revolt. Whether he summons or not, his revolt risk is his type's revolt risk. So the act's causal expected consequences are just the pleasure of Bathsheba's company, at no causal cost in revolt risk. CDT recommends summoning her.

Most philosophers side with CDT here: it would be irrational to deprive oneself on the strength of a correlation that one's choice cannot influence. The action is news about a bad dice-roll you already made, but not a lever on anything. This intuitive verdict — "don't manage your symptoms; manage your causes" — is the core motivation for CDT.

## 4. The test cases

### 4.1 Newcomb's paradox

A predictor with, say, 99% accuracy predicts your choice. Box A transparently contains \$1{,}000. Box B's contents were set yesterday: \$1{,}000{,}000 if the predictor predicted you'll take only B; empty if the predictor predicted you'll take both. You now choose: take only B, or take both.

Here the correlation runs *backward in the decision problem*: your choice is (strong) evidence about the prediction, which causally determined B's contents — but your choice does not *cause* the contents, which are already fixed.

- **CDT**: condition on the state of box B, which is fixed. Whether you one-box or two-box, B's contents are whatever they are. Two-boxing strictly dominates: you get B's contents plus \$1{,}000 either way. Expected causal utility favors **two-boxing**.
- **EDT**: one-boxing is evidence that the predictor predicted one-boxing, hence that B contains the million. Conditionals favor **one-boxing**, worth roughly $0.99 \times 10^6 \gg 1{,}000$.

Most people's initial intuition favors one-boxing (it's what actually gets the money), which makes Newcomb the flagship prima facie case *against* CDT. Two-boxers respond that rationality is about choosing well given how the world *is*, not about maximizing the payoff of predicaments created by your own predictable dispositions; the one-boxer, ex post, walks past a full box. Philosophers remain genuinely split (Bellos 2016; Wolpert & Benford 2013).

### 4.2 Prisoner's dilemma with a twin

Lewis (1979) observed that the prisoner's dilemma played against a psychological twin is a Newcomb problem in disguise. Your choice and your twin's choice are strongly correlated — similar minds, similar deliberation — but neither *causes* the other. EDT cooperates (your cooperating is evidence that your twin cooperates); standard CDT defects, since your defection does not causally affect your twin's choice. Whether defecting against a known twin is "sane" is disputed: Howard (1988) argued for cooperation precisely on grounds resembling one-boxing.

### 4.3 Death in Damascus

Death predicts where you will be tomorrow and waits there. You can flee to Aleppo or Damascus; Death is a reliable predictor of your choice. EDT's conditionals are unhelpfully symmetric; CDT, holding fixed its credence about where Death waits (which correlates with its prediction of your act), finds that whichever act it contemplates, it should expect Death to be there — and the theory famously oscillates or destabilizes. Egan (2007) and Meacham (2010) argue this reveals that CDT cannot properly use information about *its own inclinations* as evidence, since CDT holds fixed unconditional credences about the dependency structure when evaluating each act.

## 5. Counterexamples and responses

### 5.1 Egan's diagnosis and the Psychopath Button

Egan (2007) argues that CDT's failure cases stem from a gap between the intuitive rule — *do what you expect will bring about the best results* — and CDT's algorithm: *do what has the best expected outcome, holding fixed your unconditional credences about the causal structure*. In cases where the act is self-revelatory, holding fixed those credences is precisely what misleads.

His **Psychopath Button**: pressing the button kills all psychopaths, which Paul would love — but Paul is nearly certain that only a psychopath would press it, and Paul strongly prefers living (as a psychopath in a world of psychopaths, if need be) to dying.

- **CDT**: holding fixed Paul's credences, if he presses, the psychopaths (whoever they are) die; if he doesn't, everyone lives. Since Paul is *nearly certain he is not a psychopath*, the counterfactual "if I press, I die" has low probability. Pressing has high causal expected utility. **CDT says press.**
- Intuition (per Egan, "pretty much everyone"): don't press. The very fact that you're inclined to press is overwhelming evidence you're a psychopath, and your inclination is not causally independent of the button's effects on you.

Notice the structure: like Newcomb, it involves an act that is evidence about a state (being a psychopath) which determines the outcome; but unlike Newcomb, the intuitive verdict *against* CDT is nearly unanimous, since two-boxing at least seems defensible while pressing the button seems manifestly crazy.

### 5.2 Money-pump cases

Spencer (2020) and Oesterheld & Conitzer (2021) construct variants where a CDT agent predictably loses money. The cleanest is the **Adversarial Offer**: two boxes, each costing \$1, buy at most one. Yesterday the seller put \$3 in each box she predicted you would *not* buy; her predictions are 75% accurate.

From the buyer's pre-choice perspective: at least one box was left unpurchased in the seller's prediction, so at least one box contains \$3; a randomly chosen box has causal expected value at least $0.75 \times 3 - 1 = \$1.25 > 0$. CDT buys. But since the seller predicted the buyer's CDT-inclined choice 75% of the time, the buyer on average pays \$1 and most often gets an empty box. The seller, exploiting the buyer's known decision algorithm, profits at the CDT agent's expense. Oesterheld and Conitzer also show CDT agents are vulnerable to *diachronic Dutch books* — sequences of bets, each individually acceptable, that jointly guarantee a loss.

### 5.3 Joyce's response: ratifiability

Jim Joyce, CDT's most prominent modern defender, responds that CDT, properly formulated, *can* use information about one's own inclinations as evidence (Joyce 2012; Weirich 2016). The refinement is **ratifiability**: an act $A$ is ratifiable if, conditional on the agent's actually deciding on $A$ (which is itself evidence about the agent's disposition and hence about the world), $A$ still maximizes expected utility. Formally, one evaluates acts using $P(\cdot \mid \text{"I am about to choose } A\text{"})$-adjusted credences, and demands a choice that survives its own evidential implications.

In the Psychopath Button, pressing is *not* ratifiable: conditional on Paul's being about to press, he should infer he is almost certainly a psychopath, and the button then kills him — so from within that condition, not pressing looks better. Likewise, in Adversarial Offer, no purchase is ratifiable once the evidence from one's own choice is factored in. Joyce argues CDT so refined avoids the counterexamples; critics reply that ratifiability is an evidential patch that either concedes the point to EDT or fails to generalize (e.g., it can leave no stable choice at all, as in Death in Damascus). The debate is unresolved.

## 6. How to apply CDT in practice: a worked recipe

For a reader facing an unfamiliar decision problem, the operational procedure I would recommend (this synthesis goes slightly beyond the source, drawing on the dependency-hypothesis and causal-graph formulations) is:

1. **Model the causal structure.** Draw a causal graph: which variables does the act influence? Which variables correlate with the act via common causes, predictions, or logical links, but are not influenced by it? Variables of the second kind — like the predictor's past move, the seller's past filling of boxes, David's charisma, Paul's psychopathy — go in the "held fixed" pile.

2. **Partition over dependency hypotheses.** If the causal structure itself is uncertain, represent that uncertainty as a distribution over complete causal graphs (or dependency hypotheses $K$), weighted by your unconditional credence $P(K)$.

3. **Evaluate each act by intervention.** Compute $U(A) = \sum_K P(K)\sum_j P(O_j \mid do(A), K)\, D(O_j)$. Concretely: sever the incoming causal arrows into the act node, set the act to $A$, propagate the effects, and average.

4. **Check for self-revelation.** Ask: does the fact that I am inclined to choose $A$ carry information about any variable in the "held fixed" pile? If so, apply the ratifiability check: re-evaluate $A$ under credences conditional on your choosing $A$. Prefer acts that are ratifiable; if none are, the problem is degenerate and warrants care (this is where the theory is least settled).

Worked micro-example (smoking lesion, a Newcomb relative): Susan knows "smoking gene" causes both a craving and (independently of smoking) cancer. Smoking causes pleasure but no cancer. Whether to smoke? Under the recipe: the gene is in the "held fixed" pile — smoking does not cause or prevent cancer. $U(\text{smoke})$ exceeds $U(\text{abstain})$ by the pleasure of smoking. CDT says smoke; abstaining only manages a symptom. (EDT, taking smoking as evidence of the gene, says abstain — the case where most everyone thinks EDT fails.) Contrast Newcomb, where the predictor's *past act* is held fixed and CDT two-boxes — the case where many think CDT fails. The recipe makes the divergence between such cases transparent: it all turns on which correlations are causally severed by the intervention.

## 7. Assessment

CDT's strengths are real. It gives the right answer (nearly everyone agrees) in Newcomb-like cases of *medical* correlation — smoking lesions, Bathsheba — where EDT recommends self-denial on evidential grounds. It has a clean philosophical motivation: rationality is efficacy, not auspiciousness. And its formalism connects naturally to the interventionist $do$-calculus that now dominates causal inference in statistics and machine learning.

Its weaknesses are equally real, per the source's own account:

- **Vagueness of the counterfactuals.** The theory does not uniquely specify $P(A \to O_j)$; imaging requires conditional credences whose own status is problematic.
- **Self-knowledge.** Holding fixed unconditional credences blocks the agent from using her own deliberation as evidence — the engine of Death in Damascus, the Psychopath Button, and the money-pump constructions. Ratifiability is a partial, contested repair.
- **Newcomb.** Whether two-boxing is rational or merely stubborn is, after sixty years, still disputed; Oesterheld and Conitzer's Dutch book and money-extraction results give the opposition new teeth.

A reasonable reader might take the following view (this is my assessment, not the source's): CDT is the correct theory of *intervention* — of what to do, given the causal levers you actually hold — and the counterexamples show not that the theory is wrong but that real deliberation includes an *evidential* step: before pulling a lever, an agent should ask what her wanting to pull it reveals. EDT builds that step into the value function, at the price of recommending superstition in medical cases; unrefined CDT omits it, at the price of the Psychopath Button. Joyce's ratifiability hybrid — causal evaluation, evidentially screened — captures the best of both, though whether it is a principled synthesis or an ad hoc patch remains open.

## 8. Conclusion

Causal decision theory says: choose the act with the best expected causal consequences, computed from probabilities of counterfactuals rather than conditional probabilities. The formal core — $U(A) = \sum_j P(A \to O_j)D(O_j)$, or equivalently averaging $P(O_j \mid do(A))$ over unconditional credences in dependency hypotheses — is precise and, with a causal graph in hand, operational. The theory's soul is the distinction between being a symptom and being a cause: between news that the dice have fallen badly and a hand that can shake the table anew. Where acts are mere symptoms, CDT refuses to be intimidated — usually to its credit. Where acts are evidence about one's own dispositions in self-referential predicaments, that same refusal gets it into trouble, and the theory's defenders and critics continue to argue over whether the trouble is fatal or fixable. Anyone applying CDT to a new case should do three things: build the causal graph, identify which correlations the intervention severs, and then ask honestly whether the choice itself carries news the formula is choosing to ignore.

## References

- Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.
- Egan, A. (2007). "Some counterexamples to causal decision theory." *Philosophical Review* 116(1): 93–114.
- Gibbard, A. & Harper, W. L. (1981). "Counterfactuals and two kinds of expected utility." In *Ifs*, 153–190.
- Howard, J. V. (1988). "Cooperation in the Prisoner's Dilemma." *Theory and Decision* 24(3): 203–213.
- Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Joyce, J. M. (2012). "Regret and instability in causal decision theory." *Synthese* 187(1): 123–145.
- Lewis, D. (1976). "Probabilities of conditionals and conditional probabilities." *Philosophical Review* 85(3): 297–315.
- Lewis, D. (1979). "Prisoners' dilemma is a Newcomb problem." *Philosophy & Public Affairs* 8(3): 235–240.
- Lewis, D. (1981). "Causal decision theory." *Australasian Journal of Philosophy* 59(1): 5–30.
- Meacham, C. J. G. (2010). "Binding and its consequences." *Philosophical Studies* 149(1): 49–71.
- Oesterheld, C. & Conitzer, V. (2021). "Extracting money from causal decision theorists." *Philosophical Quarterly* 71(4): pqaa086.
- Pearl, J. (2009). *Causality* (2nd ed.). Cambridge University Press.
- Spencer, J. (2020). "An argument against causal decision theory." *Analysis* 81(1): 52–61.
- Weirich, P. (2016). "Causal Decision Theory." *Stanford Encyclopedia of Philosophy*.
- Wolpert, D. H. & Benford, G. (2013). "The lesson of Newcomb's paradox." *Synthese* 190(9): 1637–1646.