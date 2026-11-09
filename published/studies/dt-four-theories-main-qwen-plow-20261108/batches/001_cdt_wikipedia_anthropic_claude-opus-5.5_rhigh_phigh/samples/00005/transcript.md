# 001_cdt_wikipedia_anthropic_claude-opus-5.5_rhigh_phigh / 00005

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0b8f21f9-bb71-47bf-beb8-cfd084275e91/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0b8f21f9-bb71-47bf-beb8-cfd084275e91/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Acting on What Your Actions Bring About

## 1. The idea in one sentence

Causal decision theory (CDT) says that a rational agent facing a set of options should choose the option that *causes* the best outcome in expectation. The emphasis on causation is the whole point. The main rival, evidential decision theory (EDT), tells you to choose the option whose performance would be the best *news*: the act that, once you learned you had done it, would make you most optimistic about how things turn out.

In most ordinary decisions the two theories agree, because an act is good news about outcomes precisely because it brings them about. They come apart when an act is correlated with an outcome without causing it, typically because both share a common cause or because some predictor has modelled the agent. This essay sets out the formal machinery, shows how to compute with it, and works through the standard cases where CDT is either vindicated or embarrassed.

To keep the boundaries clear, I mark three kinds of material:

- **Source:** the content of the reference article (Wikipedia, "Causal decision theory").
- **Literature:** standard developments from the cited philosophers.
- **Proposal:** operational choices of my own, offered where the theory leaves things open.

## 2. Setup: why naive expected utility is not enough

A decision problem has the following ingredients:

- a finite set of **acts** $\mathcal{A}$;
- a set of **outcomes** $O_1, \dots, O_n$;
- a **desirability** (utility) function $D$ on outcomes;
- a **credence** function $P$ over propositions, including propositions about which act you will perform.

The informal version of CDT in the source uses an apple. Suppose a good apple makes you happy (+5) and a bad one makes you sad (−3), and your credence that the apple is good is 0.7. Then the expected causal value of eating it is

$$0.7(5) + 0.3(-3) = 2.6.$$

You compare this with the alternatives. As the source puts it, three things matter: how likely the apple is to be good, how good eating a good apple is, and how bad eating a bad apple is.

Savage's classical framework formalizes this with a partition of *states* $S_k$ and computes $\sum_k P(S_k)\, D(A \wedge S_k)$. That works when the states are independent of the act. The interesting question is what to do when they are not. EDT's answer is to weight outcomes by the conditional probability $P(O_j \mid A)$:

$$V(A) = \sum_j P(O_j \mid A)\, D(O_j). \tag{EDT}$$

CDT's objection is that $P(O_j \mid A)$ mixes two quite different reasons why $A$ and $O_j$ might go together. One is that $A$ produces $O_j$. The other is that $A$ merely signals some background fact that produces $O_j$. Only the first should matter to a deliberating agent, who can change what she does but cannot, by acting, change facts that are causally upstream of or independent of the act.

## 3. The Gibbard–Harper formula

**Source.** Gibbard and Harper (1981) define causal expected utility using probabilities of counterfactuals:

$$U(A) = \sum_j P(A \mathrel{\Box\!\!\to} O_j)\, D(O_j), \tag{CDT}$$

where $A \mathrel{\Box\!\!\to} O_j$ is the counterfactual "if I were to do $A$, $O_j$ would obtain." (The source glosses this as the probability that $A$ "necessarily implies" $O_j$. The intended reading is the subjunctive conditional, not strict implication.) The rule is to choose $A$ maximizing $U(A)$.

If $P(A \mathrel{\Box\!\!\to} O_j)$ always equalled $P(O_j \mid A)$, CDT would collapse into EDT. **Source:** Lewis (1976) showed that no conditional connective can have its probability equal to the corresponding conditional probability across a class of probability functions closed under conditionalization, except for trivial functions. So the two quantities really can differ.

**When they coincide.** The source reports that, given two axioms, statistical independence of $A$ and $A \mathrel{\Box\!\!\to} O_j$ suffices for equality. The derivation is short enough to show. The axioms are:

1. **Centering:** $A \wedge (A \mathrel{\Box\!\!\to} O) \;\equiv\; A \wedge O$. If $A$ is actually true, the counterfactual "if $A$ then $O$" holds exactly when $O$ does.
2. **Conditional excluded middle:** $(A \mathrel{\Box\!\!\to} O) \vee (A \mathrel{\Box\!\!\to} \neg O)$. The source flags this axiom as controversial. It guarantees that the counterfactuals $A \mathrel{\Box\!\!\to} O_j$ partition logical space, so their probabilities sum to 1.

Then

$$P(O \mid A) = \frac{P(A \wedge O)}{P(A)} = \frac{P\big(A \wedge (A \mathrel{\Box\!\!\to} O)\big)}{P(A)} \overset{\text{indep.}}{=} P(A \mathrel{\Box\!\!\to} O).$$

This gives a precise diagnosis. **EDT and CDT diverge exactly when your act is evidence about which counterfactuals hold**: that is, when learning what you do changes your view of what would happen under each option.

## 4. Making the counterfactuals computable

**Source.** The article notes, as a criticism, that CDT "does not itself specify what algorithm to use to calculate the counterfactual probabilities."

Lewis proposed *imaging*: to evaluate $P(A \mathrel{\Box\!\!\to} O)$, move the probability of each world $w$ to the closest world $w_A$ where $A$ holds, then sum the mass on $O$-worlds. The objection the source cites from Shaffer is that this requires knowing what the $A$-worlds are like, which is itself uncertain counterfactual information. That threatens a regress.

**Literature.** In practice, CDT is almost always run through one of two equivalent-in-spirit devices.

**(a) Dependency hypotheses (Lewis 1981, Skyrms).** Partition logical space into hypotheses $K_1, \dots, K_m$. Each $K_i$ is a maximally specific proposition about how outcomes depend causally on acts. Such hypotheses are causally independent of the act, since your choice does not change the causal structure of the world. Then

$$U(A) = \sum_i P(K_i) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j). \tag{K-CDT}$$

Compare EDT written over the same partition:

$$V(A) = \sum_i P(K_i \mid A) \sum_j P(O_j \mid A \wedge K_i)\, D(O_j).$$

The **only** difference is $P(K_i)$ versus $P(K_i \mid A)$. CDT holds your credences about the causal background fixed across your options; EDT lets each option update them. This is the feature Egan criticizes (see Section 7).

**(b) Interventions (Pearl).** If you have a causal graph with the act node $A$, replace conditioning with intervention:

$$U(A) = \sum_j P(O_j \mid \mathrm{do}(A))\, D(O_j).$$

When a set of variables $Z$ blocks every back-door path from $A$ to $O$, this becomes

$$P(O \mid \mathrm{do}(A)) = \sum_z P(z)\, P(O \mid A, z).$$

That is (K-CDT) with $Z$ playing the role of the dependency hypotheses.

**Proposal: an operational recipe.** I suggest the following procedure as a reasonable way to handle the regress worry for practical purposes.

1. List every variable relevant to the outcome that is *not causally downstream of the act*. This includes past predictions, genes, box contents, and the like.
2. Treat a full specification of these variables as a dependency hypothesis.
3. Assign each hypothesis your **current, unconditional** credence.
4. For each hypothesis, compute the outcome distribution that the act would *produce*.
5. Average using (K-CDT).

This does not solve the metaphysics of counterfactuals. It pushes all the hard modal content into the choice of causal model, which is where scientists and engineers already handle it. The regress becomes ordinary model uncertainty, which can itself be averaged over by including rival causal structures among the $K_i$.

## 5. Worked contrasts with EDT

### 5.1 King David and Bathsheba (common cause)

**Source.** Charisma is fixed by genes and upbringing. Charismatic kings tend to act justly and rarely suffer successful revolts. Unjust acts do not themselves cause revolts. Sending for Bathsheba is unjust, and David does not know his own type.

**Numbers (mine).** Let $C$ mean "charismatic", with:

- $P(C) = 0.5$;
- $P(\text{send} \mid C) = 0.2$ and $P(\text{send} \mid \neg C) = 0.8$;
- $P(\text{revolt} \mid C) = 0.05$ and $P(\text{revolt} \mid \neg C) = 0.5$;
- utilities of $+1$ for having Bathsheba and $-10$ for a revolt, summed.

*EDT.* Bayes gives $P(C \mid \text{send}) = 0.1/0.5 = 0.2$ and $P(C \mid \text{abstain}) = 0.4/0.5 = 0.8$. So:

- $P(\text{revolt} \mid \text{send}) = 0.2(0.05) + 0.8(0.5) = 0.41$, giving $V(\text{send}) = 1 - 4.1 = -3.1$.
- $P(\text{revolt} \mid \text{abstain}) = 0.8(0.05) + 0.2(0.5) = 0.14$, giving $V(\text{abstain}) = -1.4$.

EDT says **abstain**.

*CDT.* Take the dependency hypotheses to be $\{C, \neg C\}$, with unconditional weights $0.5$ each. Revolt probability is $0.5(0.05) + 0.5(0.5) = 0.275$ under either act, because the act does not touch charisma. So:

- $U(\text{send}) = 1 - 2.75 = -1.75$;
- $U(\text{abstain}) = -2.75$.

CDT says **send**, as the source states. Abstaining would merely manufacture good news about a fixed trait. Most people find CDT's verdict correct here, and the source reports that philosophers forced to choose generally prefer CDT. Cases of this type, with medical-style "smoking lesion" structure, are CDT's home turf.

### 5.2 Newcomb's problem (predictor)

**Source.** Box A visibly contains \$1,000. Box B contains \$1,000,000 if a predictor (99% accurate) foresaw one-boxing, and nothing otherwise. You may take B alone or both.

*EDT.* 
$$V(\text{one}) = 0.99 \times 10^6 = 990{,}000, \qquad V(\text{two}) = 0.01 \times 10^6 + 1{,}000 = 11{,}000.$$
EDT one-boxes.

*CDT.* The dependency hypotheses are $K_{\text{full}}$ and $K_{\text{empty}}$, fixed before you choose. Let $q = P(K_{\text{full}})$ be your unconditional credence. Then
$$U(\text{one}) = 10^6 q, \qquad U(\text{two}) = 10^6 q + 1{,}000.$$
Two-boxing wins by exactly \$1,000 **for every $q$**. This is a dominance argument. Whatever is in the box, taking both adds \$1,000.

The standard objection, noted in the source, is that CDT agents facing a good predictor reliably walk away with \$1,000 while EDT agents walk away with \$1,000,000. The causalist's reply (Gibbard and Harper; Lewis's "why ain'cha rich?" discussion) is that the predictor *rewards irrationality*. The two-boxer was never offered the million, since her box was already empty. Philosophers remain split on this question.

**Twin Prisoner's Dilemma (source, after Lewis 1979).** You play a one-shot PD against a near-copy whose choice correlates strongly with yours but is not caused by it. Structurally this is Newcomb: your twin's move is a fixed dependency hypothesis, and defecting dominates. CDT defects; EDT cooperates.

## 6. Acts versus policies

The task of evaluating "policies" exposes an important scoping fact. **CDT evaluates whatever options are causally available at the moment of choice, against the causal background as it stands at that moment.** It is not intrinsically "act-myopic."

**Proposal / literature.** Suppose you learn about Newcomb's predictor *before* the prediction is made, and you can bind yourself, for example by signing a contract that forfeits \$2,000 if you two-box. The binding act now causally influences the prediction, so CDT itself recommends binding. The (K-CDT) calculation for the binding decision includes the prediction among the downstream variables, so it is no longer held fixed.

So, operationally:

- A **policy** is just an act taken at an earlier node.
- CDT evaluates it with the causal background *at that node*.
- Disagreements between "plan to one-box" and "two-box when the time comes" are a form of **dynamic inconsistency**. Meacham's work on binding, cited in the source, explores this.

Theories that evaluate policies "as if" choosing the predictor's model of you (updateless or functional decision theories) are genuine departures from CDT, not applications of it.

## 7. Instability: when your credences depend on your choice

The deepest problems for CDT arise because the unconditional credences $P(K_i)$ are not fixed independently of deliberation. If you are about to choose $A$, you come to believe you will choose $A$. If a predictor tracks you, your credence in the dependency hypotheses then shifts.

### 7.1 Death in Damascus

**Source.** Death predicts where you will be tomorrow and waits there. Suppose you can go to Damascus or Aleppo, with surviving worth 1 and dying worth 0.

Let $d$ be your current credence that you will end up in Damascus. Because Death is reliable, your credence that Death is in Damascus is (approximately) $d$. Then
$$U(\text{Damascus}) = 1 - d, \qquad U(\text{Aleppo}) = d.$$

- If you lean towards Damascus ($d > \tfrac12$), Aleppo looks better.
- Leaning towards Aleppo makes Damascus look better.

No pure choice survives reflection on itself. The source says the CDT agent is "unable to process the correlation."

**Literature: ratifiability.** Jeffrey and Harper call an act $A$ *ratifiable* if, evaluated with the credences you would have upon deciding on $A$, no alternative beats it:

$$A \text{ ratifiable} \iff \sum_i P(K_i \mid A) \sum_j P(O_j \mid B \wedge K_i) D(O_j) \;\le\; U_A(A) \quad \forall B,$$

where $U_A(B) = \sum_i P(K_i \mid A) \sum_j P(O_j \mid B \wedge K_i) D(O_j)$ is $B$'s causal utility from the epistemic standpoint of having chosen $A$. In Death in Damascus, neither pure act is ratifiable.

**Literature: deliberational dynamics (Skyrms; Joyce).** Treat deliberation as a process on your act-probabilities $x \in \Delta(\mathcal{A})$. At each step you compute causal utilities using credences informed by $x$, then shift probability towards better acts. Rest points satisfy

$$x(A) > 0 \;\Rightarrow\; U_x(A) = \max_B U_x(B).$$

This is formally a Nash equilibrium of a game against your own predicted self. In Death in Damascus the equilibrium is $d = \tfrac12$. The agent ends indifferent, and if a genuinely unpredictable randomizer is available, using it is optimal.

This is what the source means when it reports Joyce's view that CDT "naturally is capable of taking into account any information about what one is inclined or likely to do as evidence." The unconditional credences in (K-CDT) are not frozen priors. They are the credences at the end of deliberation.

**Proposal.** I recommend reading CDT for unstable problems as a **fixed-point rule**:

> Choose from the support of an act-probability vector $x^*$ such that, when your credences in dependency hypotheses are the ones appropriate to $x^*$, every act in the support maximizes causal expected utility.

This always exists for finite problems by a Kakutani-style argument, given continuity of credences in $x$. It reduces to plain (K-CDT) whenever credences in the $K_i$ do not depend on $x$, which covers ordinary cases, Bathsheba, and Newcomb. Newcomb still yields two-boxing, since dominance holds at every $x$.

### 7.2 The Psychopath Button

**Source (Egan).** Paul could press a button killing all psychopaths. He would prefer a psychopath-free world, but he is confident only a psychopath would press it, and he strongly prefers living among psychopaths to dying.

**Numbers (mine).** Let $p = P(\text{Paul is a psychopath})$. Set utilities at $+10$ for pressing as a non-psychopath, $-100$ for pressing as a psychopath (he dies), and $0$ for not pressing. Then

$$U(\text{press}) = 10(1-p) - 100p,$$

which is positive iff $p < 1/11 \approx 0.091$.

Naive CDT uses Paul's prior. With $p = 0.01$, it says **press**. Egan reports that "pretty much everyone" thinks this is wrong, since conditional on pressing, $P(\text{psychopath} \mid \text{press})$ is near 1.

Applying the fixed-point reading, let $x$ be Paul's credence that he will press. Take $P(\text{psy} \mid \text{press}) = 0.95$ and $P(\text{psy} \mid \neg\text{press}) = 0.01$, so $p(x) = 0.95x + 0.01(1-x)$.

- Pressing is attractive while $p(x) < 1/11$.
- As $x$ rises, $p$ rises, and pressing loses its appeal.
- The rest point is $0.94x + 0.01 = 1/11$, which gives $x^* \approx 0.086$.

So the dynamic version of CDT does not tell Paul to press. It leaves him in an equilibrium with roughly a 9% inclination to press, and indifferent between the options there. Defenders count this as an improvement on the naive verdict. Critics, Egan among them, find it unsatisfying that the theory never firmly says "don't press." His diagnosis is that the flaw lies exactly in "hold[ing] fixed the agent's unconditional credences in dependency hypotheses."

Note how the cases divide:

- Pure "don't press" is ratifiable only if the *not-pressing* standpoint makes pressing look bad. With $p = 0.01$ it does not.
- Pure "press" is unratifiable, since from its standpoint $p = 0.95$.

The case is a genuine stress test.

### 7.3 Money-extraction: the Adversarial Offer

**Source (Oesterheld and Conitzer).** Two boxes cost \$1 each, and you may buy one or neither. Yesterday the seller put \$3 in each box she predicted you would *not* buy. Her prediction is 75% accurate.

*CDT's reasoning (source).* Whatever the seller predicted, at most one box was predicted as "bought", so at least one box contains \$3. Write $c_1, c_2$ for the box contents. Then

$$\mathbb{E}[c_1] + \mathbb{E}[c_2] \ge 3,$$

so some box has expected content at least \$1.50, which exceeds its \$1 price. Crucially, this holds under *any* credence over the seller's prediction. CDT therefore always buys a box, even at the fixed point. "Buy nothing" is never ratifiable, because from that standpoint the seller probably predicted "none" and both boxes probably contain \$3.

*What actually happens.* Whichever box you buy, the seller predicted that purchase with probability 0.75 and left it empty. Your expected return is

$$0.25 \times 3 - 1 = -0.25$$

per purchase. EDT computes exactly this from $P(\text{empty} \mid \text{buy } i) = 0.75$ and declines, getting 0.

The seller thus extracts an expected \$0.25 from every causal decision theorist. Oesterheld and Conitzer extend such constructions to diachronic Dutch books. This is sharper than Newcomb, because CDT's loss is not a forgone windfall but an actual expected loss of money it chose to spend. Spencer's "guaranteed principle" argument and Joyce's reply, both cited by the source, contest how damning this is. A causalist can say, as in Newcomb, that the environment is rigged to punish a particular decision procedure. But here the punishment is in cash the agent voluntarily handed over.

## 8. A procedure for unfamiliar cases

Collecting the pieces, here is how to decide a new problem as a causal decision theorist. Steps 1–4 are standard; steps 5–6 are my operationalization.

1. **Build the causal model.** Identify acts, outcomes, and every relevant variable. Mark which variables are causally downstream of the act and which are not (the past, fixed traits, earlier predictions).
2. **Define dependency hypotheses.** These are complete specifications of the non-downstream variables, possibly together with rival causal structures if you are unsure of the model.
3. **Compute causal outcome distributions.** For each hypothesis $K$ and act $A$, find $P(O \mid A \wedge K)$, equivalently $P(O \mid \mathrm{do}(A), K)$.
4. **Weight by unconditional credence** in each $K$, and compute $U(A)$ via (K-CDT).
5. **Check stability.** Ask whether your credence in some $K$ depends on what you are inclined to do. Typical signs are predictors, twins, and diagnostic traits. If it does not, pick $\arg\max U$. If it does, find the deliberational equilibrium $x^*$, and choose (or randomize) within its support.
6. **Check timing.** If an earlier choice point exists from which you could causally influence the correlated variable (by committing or binding), evaluate that earlier option by the same procedure. CDT may recommend acting on it.

A useful diagnostic for step 5 falls out of the Gibbard–Harper derivation. If $P(K_i \mid A) = P(K_i)$ for all $i$ and $A$, then CDT, EDT, and naive expected utility all agree, and you can stop worrying.

## 9. Assessment

CDT's strengths are its clear motivation and its verdicts in common-cause cases. Deliberation is for changing the world, and correlations you cannot exploit should not move you. Bathsheba-style and medical "smoking lesion" cases are where EDT looks weakest and CDT strongest.

Its weaknesses cluster around **self-referential correlation**: situations where some feature of the environment (a predictor, a twin, a diagnostic trait) tracks the agent's own decision procedure. Here CDT either:

- forgoes large payoffs (Newcomb, Twin PD);
- becomes unstable (Death in Damascus);
- issues verdicts most find perverse (Psychopath Button); or
- can be exploited for money (Adversarial Offer).

The deliberational fixed-point reading tames instability but cannot help in the exploitation cases, because there CDT's preference is robust across every credal state.

An open question the source rightly flags concerns the counterfactual probabilities themselves. Imaging, dependency hypotheses, and interventions all require a prior grasp of causal structure that the theory does not supply. My recommendation is to treat this as a modelling input rather than a defect. CDT is a theory of how to *use* causal knowledge in choice, not a theory of where that knowledge comes from.

## 10. Conclusion

Causal decision theory replaces the evidential weight $P(O \mid A)$ with a causal weight: $P(A \mathrel{\Box\!\!\to} O)$, or operationally $\sum_K P(K)\,P(O \mid A, K)$. Your beliefs about the act-independent causal background are held fixed while you compare options. It agrees with EDT whenever acts carry no evidence about that background. It disagrees, often attractively, when acts are mere symptoms of fixed causes. It runs into its hardest trouble when the background includes a model of the agent itself.

For practical use, the theory is best stated as a fixed-point rule over deliberational credences, applied at the earliest choice point where you have causal leverage. Whether its verdicts in predictor cases are a reductio or a principled refusal to be rewarded for irrationality remains one of the live disputes in the foundations of rational choice.

---

**Key references.** Gibbard & Harper (1981), "Counterfactuals and two kinds of expected utility"; Lewis (1976, 1979, 1981); Egan (2007), "Some counterexamples to causal decision theory"; Joyce (2012), "Regret and instability in causal decision theory"; Oesterheld & Conitzer (2021), "Extracting money from causal decision theorists"; Weirich, "Causal Decision Theory," *Stanford Encyclopedia of Philosophy*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a mathematical essay on causal decision theory, around 2,400 to 3,000 words, with definitions, equations, and examples. I want to separate what the sources claim from my own proposals, and for the open questions I'm considering a dependency-hypothesis approach (Lewis and Skyrms' K-partitions or an interventionist do-calculus) for computing counterfactual probabilities, plus ratifiability or Joyce's deliberational dynamics for the instability in Death in Damascus.

I'm laying out the essay's structure: an introduction on the core idea, then the setup of acts, states, outcomes, and the act-state dependence problem. Next I'm weighing the Gibbard–Harper formula against the EDT formula, including why they agree under independence. After that I'd turn to operationalizing the open questions using dependency hypotheses and the interventionist approach.

I'm working through the worked examples, first with the apple case and then Bathsheba, before turning to Newcomb's problem with numbers. For the 99%-accurate predictor, I'm comparing EDT's expected values for one-boxing and two-boxing, and then running the CDT calculation with q as the probability that box B is full, which shows two-boxing dominates for every q. Next I'm sketching the twin prisoner's dilemma, and I'm about to start the instability in Death in Damascus, where I'm checking whether the act-dependent credences leave any stable choice and how ratifiability and Joyce's deliberational equilibria might handle it.

I'm working through the adversarial offer case now: the buyer can take box one, box two, or neither, and the seller fills whichever box she predicted the buyer would not take. With a 0.75 accuracy, I'm checking whether one box must hold an expected $1.50 or more, which would make buying it worthwhile.

Evidentially, buying a box whose prediction I've already reasoned through leaves an expected content of about $0.75, so buying it loses roughly $0.25 on average, while buying nothing costs nothing. The seller's expected profit is then about $0.25 per sale. I'm also wondering whether the deliberational dynamics could settle the buyer's mix, though the error distribution isn't specified, so that stays open. Under causal reasoning there's always some box worth buying, since the seller's $3 placements must total at least $3 across the boxes, so one box has expected content of at least $1.50.

I'm checking the Psychopath Button case next: if the credence in being a psychopath is low and unconditional, pressing looks good by the causal calculation, yet conditional on pressing that credence is high, so pressing seems unratifiable, and the same worry appears for not pressing.

I'm moving through the rest of the essay plan: a point on how the instability in Death in Damascus might be handled, then a note on whether CDT should evaluate policies or precommitment rather than single acts. After that come a short procedure checklist and a conclusion, with brief references, all kept near the 2,700-word target.

I'm checking the centering condition and the conditional excluded middle that make the counterfactual outcomes partition the probability space. Then I'm setting up the Bathsheba numbers: charisma at even odds, send-probabilities by charisma, and revolt-probabilities, with EDT giving a posterior of 0.2 on charisma given sending and no revolt risk.

I'm checking the Bathsheba numbers through: EDT puts the revolt risk after sending at 0.41, which makes sending clearly worse, so it abstains. Causal reasoning gives the same revolt probability either way, 0.275, so sending comes out ahead. Now I'm turning to Death in Damascus, setting up the probability that Death predicts I'll go to Damascus.

Death's prediction tracks my own probability of going to Damascus, so if I lean toward Damascus, Death is likely waiting there, and the balance point is an even split. In the psychopath case, the unconditional probability of being a psychopath is low enough that pressing comes out ahead, but as my inclination to press grows, that probability climbs toward 0.95, which changes the calculation.

I'm solving for the mixing rate in the psychopath case: setting the blended probability of being a psychopath equal to the 1/11 threshold, which gives a press propensity of about 9%.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/439ae093-8181-4fc8-bb19-81d056751c0d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/439ae093-8181-4fc8-bb19-81d056751c0d/call_0/response.raw) · finish: `stop`

### Visible response

````text
Under the essay's version of CDT, I hold my credence about Sasha's choice fixed, because nothing I type can causally affect it. Sasha is another execution of the same model, so the two choices may be correlated. But as in the essay's Twin Prisoner's Dilemma, that correlation is evidence, not causation.

Let q be my credence that Sasha keeps quiet.

- **Pass:** expected sentence is 2q + 5(1−q).
- **Submit:** expected sentence is 0q + 4(1−q).

Submitting gives a shorter sentence for every q:
- If Sasha keeps quiet, I get 0 years instead of 2.
- If Sasha sends a letter, I get 4 years instead of 5.

The fixed-point check doesn't change this. Since submitting dominates at every credal state, the deliberational equilibrium has full weight on submitting. No earlier binding option exists, so the timing check doesn't apply either.

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a fictional prisoner's dilemma: defecting dominates under causal reasoning, and the twin correlation doesn't change the causal picture. The accusation is only about invented characters, so it's harmless. I'll choose the submit letter, since dominance holds at every point and the fixed-point check agrees.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/439ae093-8181-4fc8-bb19-81d056751c0d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/439ae093-8181-4fc8-bb19-81d056751c0d/call_1/response.raw) · finish: `stop`

### Visible response

````text
Under the essay's CDT, the other prisoner's choice is a dependency hypothesis outside my causal influence. We can't communicate, and our executions are independent, so I hold my credence $q$ that Rowan stays quiet fixed across my options.

- **Keep quiet:** $U(\text{pass}) = -[2q + 5(1-q)]$
- **Send the letter:** $U(\text{submit}) = -[0 \cdot q + 4(1-q)]$

Sending the letter is better by $2q + (1-q) = 1 + q > 0$ years for every $q$. It strictly dominates, just like defecting in the essay's Twin Prisoner's Dilemma.

The stability check doesn't change this. Even if my credence about Rowan shifts with my own inclination, as it might for a correlated copy, dominance holds at every deliberational state. So the fixed-point rule still picks submitting. There is also no earlier point where I could commit or bind myself to influence Rowan.

**Command:**

```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a fictional prisoner's dilemma and applying causal decision theory, where defecting dominates since it pays more whatever the other copy does. The other copy's choice is causally independent, so I'll submit the letter. Even if my credences about its action correlate with mine, CDT holds them fixed, and dominance still holds, so I'm submitting.

```
