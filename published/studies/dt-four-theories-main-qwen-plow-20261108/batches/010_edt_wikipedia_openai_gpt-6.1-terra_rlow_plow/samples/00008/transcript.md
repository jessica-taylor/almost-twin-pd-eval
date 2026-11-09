# 010_edt_wikipedia_openai_gpt-6.1-terra_rlow_plow / 00008

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5da4ed32-91ef-4c53-aac7-d9911039c1f2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5da4ed32-91ef-4c53-aac7-d9911039c1f2/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential decision theory: choosing the news you want to receive

A decision can be valuable in two different senses. It can *cause* a desirable result, as opening an umbrella causes one to stay drier. Or it can be *evidence* of a desirable result, as carrying an umbrella might indicate that one has seen a reliable forecast of rain.

Evidential decision theory, or **EDT**, evaluates choices using the second kind of connection as well as the first. Its guiding question is: *If I learned that I had taken this action, how good would I expect the resulting situation to be?* It recommends the action associated with the best expected news.

That formulation can sound strange. An agent ordinarily knows what she chooses, so why imagine learning it? The point is not that an action is literally a message arriving from outside. Rather, EDT uses conditional probability to measure what would be true, on average, among situations in which the agent takes that action. Those situations may differ not only in the causal effects of the action, but also in facts that help explain why the action is taken.

This essay follows the reference article’s basic account and develops some operational details it leaves open. In particular, the treatment of zero-probability actions, randomization, and policies below should be read as practical proposals, not as consequences uniquely settled by the article.

## 1. The basic rule

Suppose an agent is choosing from actions \(a\in\mathcal A\). Let \(K\) represent the information available at the decision point, \(O_1,\ldots,O_n\) a mutually exclusive and exhaustive partition of outcomes, and \(u(O_j)\) the utility of outcome \(O_j\). The evidential value of an action is

\[
V_{\mathrm E}(a\mid K)
 =\sum_{j=1}^{n}P(O_j\mid A=a,K)\,u(O_j).
\]

EDT recommends an action maximizing this value:

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}
V_{\mathrm E}(a\mid K).
\]

Here \(A\) is a random variable representing the agent’s action in her probabilistic model. The conditioning event \(A=a\) means that the action is *actually taken*; it does not mean that an external force sets the action to \(a\). When outcomes are not naturally discrete, the sum can be replaced by an expectation:

\[
V_{\mathrm E}(a\mid K)=
\mathbb E[u(O)\mid A=a,K].
\]

The outcome description must include everything the agent cares about. If money, health, fairness, and the costs of choosing matter, utilities should reflect all of them. Dollar amounts can stand in for utilities in simple examples, but that assumes the agent values the relevant amounts linearly and has no other relevant concerns.

The theory’s distinctive feature is the probability \(P(O_j\mid A=a,K)\). By Bayes’ rule, when the relevant probabilities are positive,

\[
P(O_j\mid A=a,K)
=\frac{P(A=a\mid O_j,K)P(O_j\mid K)}
       {P(A=a\mid K)}.
\]

Thus an action can be evidence about an outcome whenever it is more likely in some circumstances than in others. A choice may correlate with a prediction made yesterday, another agent’s independent choice, or an underlying condition that influences the chooser’s preferences. EDT includes these dependencies if they are present in the agent’s conditional probabilities.

This does **not** mean treating every correlation as a causal effect. An evidential decision theorist can agree that an action does not change the past. The claim is instead that, when comparing actions, it is appropriate to take into account what each action would indicate about the past.

## 2. Evidence versus intervention

The reference article contrasts EDT with causal decision theory, or CDT. A common causal formulation evaluates an action by the outcomes that would result *if the action were performed*, keeping fixed the relevant causal structure:

\[
V_{\mathrm C}(a\mid K)
=\sum_j P(O_j^{\,a}\mid K)\,u(O_j),
\]

where \(O^{\,a}\) denotes the outcome under the counterfactual intervention setting the action to \(a\). In a suitable causal model this is often written using \(P(O_j\mid\operatorname{do}(A=a),K)\). The do-notation requires care about when \(K\) is observed and about the causal model, but it illustrates the contrast.

Suppose a hidden variable \(H\) influences both the action and an outcome:

\[
H\longrightarrow A,\qquad H\longrightarrow O.
\]

Observing \(A=a\) can change beliefs about \(H\), and therefore about \(O\). Intervening to set \(A=a\), by contrast, breaks the causal connection from \(H\) to \(A\); it need not change the distribution of \(H\).

When action selection carries no information about outcome-relevant factors beyond the known causal effects of the action, EDT and CDT can agree. They diverge when the action is informative about factors that an intervention would not alter. This distinction drives the reference article’s examples.

It also explains what EDT means by comparing alternatives. It is not asking, “Holding the entire actual past fixed, what would happen if I changed my action?” It asks, “Conditional on my taking each action, what should I expect?” The latter comparison can associate different actions with different probabilities concerning the past, without asserting backward causation.

## 3. Newcomb’s problem

A predictor has already filled an opaque box \(B\). If it predicted that you would take only \(B\), it put \$1 million inside; if it predicted that you would take both \(B\) and a transparent box \(A\), it left \(B\) empty. Box \(A\) visibly contains \$1,000. You now choose one box or both.

The evidential calculation depends on the conditional probabilities at your decision point. Suppose

\[
P(B\text{ full}\mid \text{one-box})=0.99,
\qquad
P(B\text{ full}\mid \text{two-box})=0.01.
\]

With utility equal to the number of dollars received,

\[
\begin{aligned}
V_{\mathrm E}(\text{one-box})
 &=0.99(\$1{,}000{,}000)+0.01(\$0)\\
 &=\$990{,}000,\\[3pt]
V_{\mathrm E}(\text{two-box})
 &=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)\\
 &=\$11{,}000.
\end{aligned}
\]

EDT recommends one-boxing. Choosing only \(B\) is strong evidence that the predictor predicted one-boxing, and hence that \(B\) is full.

There is a subtlety in the description “99% accurate.” An overall prediction accuracy of 99% does not by itself imply both conditional probabilities above. For example, if almost everyone one-boxes, the predictor could be 99% accurate overall while being poor at identifying the rare two-boxer. The numerical verdict uses the stronger conditional assumptions explicitly.

More generally, write

\[
q_1=P(B\text{ full}\mid \text{one-box}),\qquad
q_2=P(B\text{ full}\mid \text{two-box}).
\]

Then

\[
V_{\mathrm E}(1)=1{,}000{,}000q_1,\qquad
V_{\mathrm E}(2)=1{,}000{,}000q_2+1{,}000.
\]

One-boxing wins exactly when

\[
q_1-q_2>0.001.
\]

Thus the evidential recommendation is not automatic for every alleged predictor; it depends on the strength of the action–prediction correlation and the stakes.

A standard CDT analysis says that the contents of \(B\) are already fixed, and that taking \(A\) cannot change them. For either fixed state of \(B\), taking both yields \$1,000 more. EDT accepts that causal description but compares the probability of the states *conditional on each action*. The philosophical dispute is whether that difference in conditional probabilities belongs in the decision calculation.

## 4. A psychological twin

Consider a prisoner’s dilemma played against your psychological twin in a separate room. Both cooperation and defection are available. Your personal payoffs are:

| Your action | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$5 | \$0 |
| Defect | \$10 | \$1 |

Assume first that your choices are perfectly correlated:

\[
P(\text{twin cooperates}\mid C)=1,\qquad
P(\text{twin cooperates}\mid D)=0.
\]

Then EDT assigns cooperation a value of \$5 and defection a value of \$1, so it recommends cooperation. There is no need to suppose that your choice sends a signal to your twin. Similar reasoning processes can make your action informative about hers even when neither action causes the other.

Perfect correlation is stronger than the situation needs. Define

\[
p_C=P(\text{twin cooperates}\mid C),\qquad
p_D=P(\text{twin cooperates}\mid D).
\]

The evidential values are

\[
V_{\mathrm E}(C)=5p_C,\qquad
V_{\mathrm E}(D)=10p_D+1(1-p_D)=1+9p_D.
\]

Cooperation is preferred when

\[
5p_C>1+9p_D.
\]

A merely modest resemblance between players may not satisfy this inequality. If, for example, \(p_C=0.8\) and \(p_D=0.5\), cooperation has value \(4\), while defection has value \(5.5\). Calling someone a “twin” is not enough; the relevant conditional probabilities do the work.

The result also changes if the agent values the twin’s welfare, if communication is possible, or if the choice affects future encounters. These factors can create additional reasons to cooperate, but they are separate from the distinctive evidential correlation in the example.

## 5. A challenge: good news without good effects

The strongest intuitive objection to EDT is that actions can be evidence of good news without improving the world. David Lewis criticized the theory as a policy of “managing the news”; James Joyce emphasized causal efficacy rather than auspiciousness.

A stylized medical example shows the concern. Suppose a gene makes a disease more likely and also makes its carriers more likely to enjoy a certain drink. The drink itself has no effect on the disease. An agent likes the drink by one utility unit. Suppose, conditional on current information,

\[
P(\text{disease}\mid \text{drink})=0.20,\qquad
P(\text{disease}\mid \text{abstain})=0.05,
\]

and disease costs 100 utility units. Ignoring other payoffs,

\[
V_{\mathrm E}(\text{drink})=1-100(0.20)=-19,
\]
\[
V_{\mathrm E}(\text{abstain})=-100(0.05)=-5.
\]

EDT recommends abstaining. Yet if the gene and disease risk are unaffected by the choice, a causal analysis recommends the enjoyable drink.

An EDT defender can respond that the numbers must be conditional on **all** information the agent actually has. If she knows her genetic status, or knows enough about the inclination that links drinking to the gene, the choice may convey little further information. If

\[
P(\text{disease}\mid \text{drink},K)
=P(\text{disease}\mid \text{abstain},K),
\]

EDT too recommends the drink. But this is not a universal resolution: the agent may not know the relevant hidden condition, and the action may remain informative even after all available evidence is included. Whether it is rational to forgo the drink in that case remains a substantive dispute.

The example illustrates a general diagnostic. Before applying EDT, ask **why** the action predicts the outcome. A causal path from action to outcome, a shared cause of both, and a predictor’s earlier response to the agent’s likely decision can all produce conditional dependence. EDT counts all of them as evidence, but their philosophical significance is contested.

## 6. Constructing a decision model

For an unfamiliar case, the main difficulty is often not the final maximization but specifying a coherent probability model. A practical procedure is:

1. **Fix the decision point and information \(K\).** Include observations, known rules, and remembered choices available to the agent, but not facts she does not know.
2. **Specify the alternatives.** Decide whether the objects of choice are immediate acts, commitments, randomized procedures, or complete policies.
3. **Describe relevant outcomes and utilities.** Include costs of the action and downstream consequences, not merely the attractive headline payoff.
4. **Model how actions and outcomes are jointly distributed.** Include predictors, other agents, shared causes, and uncertainty about the agent’s own choice where relevant.
5. **Condition on each action.** Compute \(P(O_j\mid A=a,K)\), rather than replacing it without argument by an intervention probability.
6. **Compare values and test assumptions.** Check whether the result survives changes in correlation, utility, and information.

A joint model is particularly important because conditional probabilities cannot be chosen independently. For instance, perfect matching in the twin case,

\[
P(\text{twin cooperates}\mid C)=1,\qquad
P(\text{twin cooperates}\mid D)=0,
\]

requires a model in which mismatched choices have probability zero. If both conditionals are to be evaluated by ordinary conditioning, both \(C\) and \(D\) must also have positive probability in that model.

An agent’s uncertainty about her own action is not necessarily ignorance about what she will do after deciding. It can represent uncertainty, *before settling the decision*, about which considerations will prevail, or uncertainty in a model of similar decision situations. But the source’s formula does not completely settle how such self-locating uncertainty is to be represented. Different reasonable models can produce different recommendations.

## 7. Zero probabilities and randomization

Ordinary conditional probability does not define \(P(O\mid A=a,K)\) when \(P(A=a\mid K)=0\). This matters if an agent is already certain that she will choose one action: the formula then cannot directly evaluate an alternative assigned probability zero.

One operational proposal is to use a pre-decision model that assigns positive probability to each genuinely available option, then condition within that model. A second is to consider limits of positive-probability models approaching the original one. But limits need not be unique: different ways of making a supposedly impossible action slightly possible can imply different associations between that action and hidden states. Neither proposal is a complete solution supplied by the basic formula.

Randomization is also model-dependent. Imagine choosing a rule that uses an independent coin to select one-boxing or two-boxing. If the coin is genuinely independent of a predictor’s earlier prediction, the resulting action may be much less informative about the box than an unrandomized choice. On the other hand, the predictor might have predicted the agent’s policy, observed features of the randomization device, or even predicted its result. One must model these possibilities rather than assume that “randomize” automatically preserves or destroys the evidential link.

It is essential to distinguish:

- conditioning on the **policy** “follow this coin rule”;
- conditioning on the **realized action** “the coin rule led to one-boxing”; and
- intervening to force one-boxing regardless of the policy.

They are different events or operations. A fair coin independent of a hidden state can make its realized result uninformative about that state, but choosing to use that coin may itself be informative if agents with different hidden characteristics choose different policies.

## 8. Acts, policies, and changing information

An immediate action is not always the natural unit of choice. A policy \(\pi\) may prescribe actions at several future information states: for example, “cooperate unless I receive evidence of deception.” One possible evidential evaluation is

\[
V_{\mathrm E}(\pi\mid K)
=\mathbb E[u(O)\mid \Pi=\pi,K],
\]

where \(\Pi\) denotes the policy actually adopted. As with individual acts, this requires a joint distribution in which adoption of the policy can be conditioned on. A policy may be evidence about a predictor’s earlier forecast or about policies adopted by similar agents.

This is a useful extension, not a unique rule mandated by the source. A policy might be a publicly observable commitment, a private intention, a computer program, or merely a description of what the agent would do in many circumstances. Those interpretations give different predictors access to different information and can produce different correlations. In particular, the fact that a policy specifies an action in a hypothetical situation does not establish that another agent can observe that specification.

Sequential choices raise a further issue. A policy that looks best before receiving information need not remain preferred at every later decision point. An agent must distinguish the value of committing now from the value of choosing afresh later, conditional on what she has learned. If actual commitment is possible, its costs and enforcement belong in the outcome model. If it is not, a plan that the future self will abandon cannot simply be treated as implemented.

The reference article briefly mentions Sleeping Beauty and disputes over Dutch books: arrangements of bets that guarantee a loss under specified rules. It reports arguments both that EDT can help a half-credence Sleeping Beauty avoid such books and, following Vincent Conitzer, that halfers may remain vulnerable even with EDT. The general lesson is not a settled verdict about Sleeping Beauty. It is that repeated awakenings, memory, bet timing, and whether one evaluates a whole betting policy or each offer separately all matter to the formal decision problem.

## 9. What the theory claims—and what it leaves open

EDT provides a compact rule: maximize expected utility conditional on the action. Its appeal is that a decision is part of the world, not an isolated lever. If an action is reliable evidence of what a predictor did or what a similar agent will do, excluding that evidence can look like ignoring relevant information. Newcomb’s problem and the twin dilemma make this appeal vivid.

Its difficulty is the same feature seen from the other side. A favorable conditional distribution can arise because an action *indicates* an advantageous state, even where it does nothing to produce that state. Critics argue that choosing the indicator confuses news with control. Conditioning on all available information can remove some apparent pathologies, but cannot be assumed to remove them all.

The reference article also notes a further, qualified argument: even someone uncertain about EDT might give it practical weight because correlated decisions can have larger stakes than an isolated causal choice. This is not a proof that EDT is correct. Acting under uncertainty among decision theories requires additional assumptions about how to compare their recommendations and stakes.

## Conclusion

To use EDT, build a joint probabilistic model of actions and outcomes, condition on each available action using the information actually possessed, and choose the greatest conditional expected utility. The decisive questions are often which correlations are justified, whether the action or a policy is the object of choice, and whether the needed conditional probabilities are defined.

EDT’s distinctive proposal is that what an action *reveals* matters to choice alongside what it causes. Whether that is rational insight or an attempt to manage the news remains the central philosophical disagreement.

### References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy* 59, 1981.
- Vincent Conitzer, “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists,” *Synthese* 192, 2015.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7f1c2a42-c1f7-47f1-a2bd-a24264eeafc9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7f1c2a42-c1f7-47f1-a2bd-a24264eeafc9/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Deciding on correlation models**

I need to determine if there’s a correlation between common models with strong symmetry. The different names for these concepts might not matter much. It seems there's likely strong reasoning behind their similarities, but there's some uncertainty due to independent sampling and private differences. So, I'll pass on what's reasonable and focus on the essential elements. I'm making sure to keep clarity in my analysis while recognizing these uncertainties.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/7f1c2a42-c1f7-47f1-a2bd-a24264eeafc9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/7f1c2a42-c1f7-47f1-a2bd-a24264eeafc9/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Choosing correlations carefully**

I need to decide on a correlation between some factors. I'm noticing that the same reasoning applies even if the names and facts are different, suggesting a strong correlation based on shared decision-making processes. However, independent sampling creates uncertainty since there's no explicit numerical data to rely on. I'm treating high correlation as an indication of compelling reasoning, and while I note that distinct private observations could affect this, they seem negligible in meaning.
```
