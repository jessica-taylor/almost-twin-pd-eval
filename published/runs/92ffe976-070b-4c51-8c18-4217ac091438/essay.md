# A-FDT: Choosing as the Output of a Function

## 1. The idea in one sentence

Two people deciding whether to cooperate can be causally isolated, sitting in separate rooms with no communication, and still be correlated, because both run the same reasoning. Causal decision theory (CDT) ignores that correlation. Evidential decision theory (EDT) respects every correlation, including spurious ones. Yudkowsky and Soares's *functional decision theory* aims between the two. Its normative principle, in their words, is to treat one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

This essay explains **A-FDT (action functional decision theory)**. I use that name for the specific rule given as Equation (4) in Section 5 of the paper. In that rule the agent intervenes on a variable standing for *the action her decision function outputs on her actual input*.

The authors flag a different formalization in two footnotes (7 and 16). There the agent intervenes to choose a *policy*, a map from observations to actions. I call that variant **policy-FDT**. The paper says that "in the authors' preferred formalization" agents iterate over policies, but that this "will not make a difference in this paper." My subject is A-FDT. I mention policy-FDT only where the contrast clarifies A-FDT.

Throughout, I mark which claims come from the source and which are my own interpretations or proposals.

## 2. The common expected-utility skeleton

The paper presents EDT, CDT and A-FDT as variants of a single template (Equation 1). The agent maximizes

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective. Following Joyce, the paper treats the interpretation of $\hookrightarrow$ as the free parameter. The theories agree on how to value outcomes and disagree on "the epistemic perspective from which actions are to be evaluated."

Procedurally, the agent holds a world-model $M$. For each action $a$ she builds a *hypothetical* $M^{a\hookrightarrow}$, computes its expected utility, and takes the best action. The theories differ in how hypotheticals are built:

- **EDT** conditions: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT** (in Pearl's formalism) intervenes on the physical act: $\arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x)$.
- **A-FDT** intervenes on a *logical* variable.

## 3. The definition of A-FDT

The world-model is a pair $(P, G)$:

- $P$ is a probability distribution that includes variables standing for the *outputs of mathematical functions*.
- $G$ is a graph that says how changing those logical variables would change everything else.

A-FDT is then (Equation 4):

$$
\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).
$$

The variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the node representing "what the A-FDT algorithm outputs when run on these very inputs." The underlines mark dequoting: the node's *name* is built from the agent's own model and observation. The self-reference is intended. The paper notes that the agent need not know the *value* of the node to represent it, and that Kleene's recursion theorem ("quining") lets a data structure contain a representation of itself.

The paper itself names two differences from CDT:

1. **Point of intervention.** CDT intervenes on the token, $\textsc{Act}$. A-FDT intervenes on the *type*, the function's output. Every node that "subjunctively depends" on that output then varies together. This includes the agent's body, a twin running the same function, and a predictor's model of the agent.

2. **Treatment of observations.** Equation (4) does not condition on $\textsc{Obs}=x$. Instead, "FDT responds to observation by changing which node it intervenes upon." A different observation $y$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$. Nodes for the function's output on *other* inputs keep whatever distribution $P$ gives them. So does everything upstream of the intervened node, including the facts that determine which observation the agent receives.

The second feature is the one most often misread. A-FDT does respond to evidence, but only by selecting which logical node is under its control. In the hypothetical, the agent may imagine that she would never have received the observation she is now holding.

### What "subjunctive dependence" means

The paper's slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" Two physical systems computing the same function both subjunctively depend on that function, like two calculators evaluating $6288+1048$. Causal dependence is a special case: a scribe copying a calculator's output would have written something different had the output differed. Mere correlation is excluded: two calculators that happen to be pink do not depend on each other.

In graph terms, the arrows leaving the $\textsc{fdt}$ node in $G$ should point to all and only the things that compute, or accurately model, that function's output on that input.

Since the function's actual output is a logical fact, setting it to anything else is a *counterpossible* supposition. The paper concedes it has no definition of the ideal operator $\mathtt{true}(\phi)$ and does not attempt one. Instead it requires that $G$ be supplied as input, just as CDT requires a causal graph. A-FDT is therefore well defined *relative to* $(P,G)$. Constructing $G$ is, in the authors' words, "perhaps the largest open problem."

## 4. A recipe for applying A-FDT

The paper never states an algorithm in these terms. The following is my operational reading of Equation (4) together with the worked examples in Section 6.

1. **Identify the agent's decision instances.** List the inputs $x_1,\dots,x_k$ on which the agent's decision function might be run in the scenario, for example "sees full box" and "sees empty box." Create a node $F_i := \textsc{fdt}(\underline P,\underline G,\underline{x_i})$ for each.

2. **Wire the dependencies.**
   - Draw an arrow from $F_i$ to every system that computes or reliably predicts the agent's output on $x_i$.
   - Draw an arrow from $F_i$ to $\textsc{Act}$ through a selector: whichever input the agent actually receives determines which $F_i$ sets $\textsc{Act}$.
   - Ordinary causal arrows stay as they are.
   - Mere correlates, such as a lesion, receive no arrow from any $F_i$.

3. **Assign priors.**
   - Use ordinary priors over exogenous variables.
   - Assign some distribution to each non-actual $F_j$. The paper uses an arbitrary parameter $q$ and shows that the answer does not depend on it in its examples.

4. **Intervene and evaluate.** For the actual input $x$ and each $a$, compute $\mathbb E[V\mid do(F_x=a)]$ by forward propagation through $G$. Do not additionally condition on $\textsc{Obs}=x$.

5. **Choose** the maximizing $a$.

## 5. Worked examples

All payoffs are in dollars-as-utility, following the paper's convention.

### Twin Prisoner's Dilemma

Both prisoners' acts are children of the single node $F$:

- $do(F=C)$ means both cooperate, giving \$1,000,000.
- $do(F=D)$ means both defect, giving \$1,000.

A-FDT cooperates. CDT holds the twin's act fixed while varying its own, so for CDT defection dominates.

### Newcomb's problem (99% accurate predictor)

$F$ points to the agent's act and to the prediction, with an independent accuracy variable. Write $p_{\text{full}}$ for the probability that box B is full.

- $do(F=\text{one-box})$: $p_{\text{full}}=0.99$, so expected value is $0.99\times 10^6 = 990{,}000$.
- $do(F=\text{two-box})$: $p_{\text{full}}=0.01$, so expected value is $0.01\times 1{,}001{,}000 + 0.99\times 1{,}000 = 11{,}000$.

A-FDT one-boxes. The paper stresses that no retrocausation is assumed. The agent simply declines to imagine her action changing while the predictor's model of the same function stays fixed.

### Smoking lesion

The lesion causes both cancer and a taste for smoking. It is not a model of the agent's reasoning, so $F$ has no arrow to cancer.

The paper fills in more structure:

- There are two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$ (values smoking at $-\$1$), and hence two possible decision nodes.
- The lesion selects which node controls $\textsc{Act}$.
- The agent cannot introspect which node is hers.

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\text{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes. The paper itself regards the dilemma as "badly confused" and recommends abandoning it.

### Transparent Newcomb

The agent sees box B full. There are two nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction is a child of $F_{\text{full}}$, and the prediction determines which node controls the act. Let $q$ be the prior that $F_{\text{empty}}=$ two-box.

- $do(F_{\text{full}}=1)$: $0.99\times 10^6 + 0.01\times q\times 1{,}000 = 990{,}000 + 10q$.
- $do(F_{\text{full}}=2)$: $0.01\times 1{,}001{,}000 + 0.99\times q\times 1{,}000 = 10{,}010 + 990q$.

The source prints the second as "\$110,00 + $q\cdot$\$990", which appears to be a typesetting slip for \$10,010.

One-boxing wins for every $q\in[0,1]$. A-FDT therefore leaves the visible \$1,000 behind. In the hypothetical where it two-boxes, the agent would most likely have *seen an empty box*. Here the absence of conditioning on $\textsc{Obs}=x$ matters directly. The paper notes this case is structurally identical to Parfit's hitchhiker: A-FDT pays the driver.

### XOR blackmail (infallible predictor)

Let $t$ be the prior probability of termites. The letter is sent iff exactly one of these holds:

- (no termites and the agent pays), or
- (termites and the agent refuses).

Compare the two interventions:

- $do(F_{\text{letter}}=\text{pay})$: with termites, no letter arrives and the agent loses \$1,000,000. Without termites, the letter arrives and the agent pays \$1,000. Expected loss: $10^6 t + 1{,}000(1-t)$.
- $do(F_{\text{letter}}=\text{refuse})$: with termites, the agent loses \$1,000,000. Without termites, no letter arrives and the loss is 0. Expected loss: $10^6 t$.

A-FDT refuses, because the intervention does not touch the termites. EDT pays, since conditioning on paying makes termites impossible given the letter. CDT also refuses, but its counterfactual is that the infallible predictor would have erred.

### Mechanical blackmail

The blackmailer runs the program only if she predicts the agent will pay. Let $\varepsilon$ be the probability that she wrongly predicts payment from an agent who would refuse.

- Refusing costs $\varepsilon\times 10^6$ in expectation.
- Paying costs about \$1,000, since the agent is then blackmailed essentially always and pays.

A-FDT refuses iff $\varepsilon < 10^{-3}$. The paper's example $\varepsilon=0.0009$ gives an expected loss of \$900, so A-FDT refuses even while holding the letter. The paper then says A-FDT pays at "0.011%". By my arithmetic the threshold is 0.1%: at 0.011% the expected cost of refusing would be only \$110, and A-FDT would still refuse. The intended figure was probably 0.11%.

### Death in Damascus

Death predicts perfectly, so $F$ points to both the agent's location and Death's book.

- $do(F=\text{stay})$: death, utility 0.
- $do(F=\text{flee})$: death plus the \$1,000 cost of fleeing.

A-FDT stays, with no instability. CDT, by contrast, oscillates or ratifies a near-50/50 mixture. The paper also offers a truly random coin for \$1 that gives a 50% chance of escaping.

The paper explains why CDT refuses the coin but does not compute A-FDT's response. My own computation: the coin is not an output of $F$ and is not predictable from it. So $do(F=\text{buy coin})$ yields roughly $0.5\times 10^6 - 1$, which beats certain death, and A-FDT buys the coin.

## 6. Dominance, fairness, and stability (the source's claims)

**Dominance.** The paper argues that dominance is not a neutral criterion: "every method for constructing hypotheticals gives rise to its own notion of dominance."

- CDT-dominance holds the prediction fixed, and by that standard two-boxing dominates.
- FDT-dominance holds subjunctive dependencies fixed, and by that standard one-boxing does.

The authors prefer to judge theories by utility achieved.

**Fairness.** The authors claim that FDT does at least as well as its rivals in "fair problems": problems where the agent's beliefs are accurate and outcomes depend only on the agent's *behaviour* in the problem at hand, not on which procedure produced it. They admit that "fair" is not yet formalized. Footnote 15 offers a counterexample family: punish whoever acts like a copy of Fiona.

**Reflective stability and precommitment.** The authors claim that FDT "always act[s] as [it] would have precommitted to act," and that it is reflectively stable in fair problems.

## 7. Open questions and how I propose to settle them

**(a) Where does $G$ come from?** The source leaves this explicitly open. My operational criterion is:

> Draw an arrow $F_x \to Y$ iff $Y$'s value is produced by a process that would track the output of the agent's function on input $x$ under the hypothetical that this output differed.

In practice that means $Y$ simulates, reasons about, or copies the function. Statistical association arising from common physical causes earns no arrow.

For imperfect dependence, such as a 99% predictor, use the paper's device: an independent noise node feeding the dependent variable.

For partially similar agents, such as a colleague who reasons "much like me," the source gives no rule. A modest extension is to model the colleague's act as a mixture: with probability $s$ it is computed by $F$, and with probability $1-s$ by some independent process. This makes $s$ an explicit judgment about logical similarity rather than about correlation. It is my proposal, not the paper's.

**(b) Priors on non-actual decision nodes.** Equation (4) leaves the values of $F_{x'}$ for $x'\neq x$ at their priors. In the paper's examples the answer is insensitive to $q$, but nothing guarantees this in general. Consider a predictor that rewards an agent only if it behaves in a specific *combination* across inputs. The A-FDT choice at $x$ can then depend on what the agent believes it does at $x'$.

I propose to require an equilibrium: $P(F_{x'}=a') = 1$ iff $a'$ is the A-FDT output at $x'$, computed under the same requirement. This is a fixed point over the agent's decision instances. Multiple equilibria can exist, and selecting among them is exactly what policy-FDT's joint optimization accomplishes. The paper says this difference "only matters in multi-agent dilemmas so far as we can tell." I read that as an acknowledgment, not a proof, that A-FDT and policy-FDT can come apart.

**(c) Why not also condition on $x$?** The paper's answer is that conditioning *and* moving the intervention point produces a harmful "double update." It attributes this flaw to the earlier timeless decision theory. A-FDT, as specified, does not condition. In the transparent Newcomb computation, conditioning on "box full" would make two-boxing look better and destroy the result.

**(d) Self-reference and probability-zero actions.** Unlike EDT, A-FDT does not exclude actions to which it assigns prior probability zero. The $do$-operator sets the node regardless of its prior. So an agent nearly certain she will one-box can still evaluate two-boxing. The paper's "objection" passage makes this point.

**(e) Counterpossibles.** Equation (4) reduces the counterpossible operator $\mathtt{true}$ to Pearl's $do$ on a given graph. Whether every subjunctive-dependence structure can be represented this way is, by the paper's own account, "not yet clear." Footnote 9 mentions an evidential alternative that would condition on logical facts. No formal definition of that alternative yet exists, and it is not A-FDT.

## 8. When A-FDT agrees with CDT and EDT

The paper observes that if every correlation between the act and other variables is caused by the act, except the act's dependence on $F$ itself, then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(F=a)].
$$

In that case all three theories prescribe the same action. A-FDT diverges only where something outside the agent's body tracks her decision function, such as predictors, twins, copies, or her own future selves. The paper gives two examples:

- **Voting.** Ten like-minded agents vote because their choices are subjunctively linked.
- **The gym.** An agent goes to the gym today because next week's choice is "the same decision."

For working through a new case, this gives a quick test. First ask whether anything models your decision function. If nothing does, A-FDT reduces to CDT, and you can stop there.

## 9. Conclusion

A-FDT is CDT with the point of intervention moved: from the physical act to the output of one's decision function on one's actual input, and with observation handled by choosing which node to intervene on rather than by conditioning. Given a world-model $P$ and a graph $G$ of subjunctive dependencies, Equation (4) is a concrete argmax.

Applied to the classic dilemmas, it one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays the hitchhiker's driver, refuses both kinds of blackmail, and stays in Damascus. The paper's case rests on these utility outcomes and on reflective stability. Its acknowledged gaps are:

- how to obtain $G$;
- how to make sense of counterpossible interventions;
- how to define "fair" problems.

I have added three interpretive choices of my own: an arrow criterion for building $G$, a similarity-mixture model for imperfect replicas, and an equilibrium condition on non-actual decision nodes. These make A-FDT usable on unfamiliar cases. They also show where it may diverge from policy-FDT, which the authors themselves prefer.

*Reference:* E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2.