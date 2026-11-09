# A-FDT: Choosing the Output of a Decision Function

## 1. The idea

A-FDT (action functional decision theory) is the decision rule given by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." The paper calls its theory simply "FDT". I use "A-FDT" for the action-level rule in Equation (4). The paper notes that its authors' "preferred formalization" has the agent select *policies*, meaning mappings from observations to actions, and that this "makes a difference in certain multi-agent dilemmas." Everything below concerns the action-level version.

The slogan, from the abstract, is that one should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Compare the questions the paper attributes to the rivals. Causal decision theory (CDT) asks "Which physical act of mine causes the best outcome?" Evidential decision theory (EDT) asks "Which physical act of mine would be the best news to hear I took?"

I proceed in this order:

- the formal definition and what each piece means;
- where the source leaves things open, and how I propose to fill the gaps;
- worked examples with the arithmetic;
- the philosophical motivation.

I flag which claims are the source's and which are mine.

## 2. Setting: expected utility with a free "epistemic perspective"

The paper treats EDT, CDT and A-FDT as expected utility theories. They maximize

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $P(a\hookrightarrow o_j;x)$ is the probability that $o_j$ obtains "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Following Joyce's representation theorem, the theories differ only in how "$\hookrightarrow$" is interpreted. In the paper's words, they supply different "epistemic perspectives."

- EDT reads $\hookrightarrow$ as conditioning. It prescribes $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$ (Equation 2).
- CDT reads it as a Pearl intervention on the physical action node. It prescribes $\arg\max_a\mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$ (Equation 3).
- A-FDT reads it as a Pearl intervention on a *logical* node, the output of the agent's own decision function (Equation 4).

The paper stresses that a "hypothetical" is a decision-theoretic instrument rather than a belief or a metaphysical possible world: "transient, useful, and possibly quite representationally thin," like "notes on scratch paper." The agent has a world-model $M$ and, for each action, builds from it a hypothetical $M^{a\hookrightarrow}$. She values each hypothetical and takes the best.

## 3. Equation (4)

> $$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here is each ingredient, as I read it.

**$P$** is a probability distribution over the agent's world-model variables. It includes variables for the outputs of mathematical functions. The paper's example is a variable for $6288+1048$ that "(hopefully) has most of its probability on 7336."

**$G$** is a graph encoding "the logical, mathematical, computational, causal, etc. structure of the world," specifically "how changing a logical variable affects all other variables." It is the analogue of the causal graph CDT requires. Equation (4) *takes it as input*.

**$\mathrm{fdt}(\underline P,\underline G,\underline x)$** is a node in the model representing the output of the A-FDT procedure itself when run on inputs $(P,G,x)$. The underlines denote dequoting, so the node's name depends on the model's own contents. This self-reference is harmless: "an FDT agent does not need to know the *value* of $\mathrm{FDT}(M,x)$ in order to have a variable $\mathrm{fdt}(\underline M,\underline x)$ *representing* that value," and Kleene's second recursion theorem (quining) shows such self-representing structures can be built.

**$do(\cdot)$** is Pearl's operator, reused unchanged. It sets the node to $a$, recomputes everything downstream according to $G$, and leaves everything else alone. "Downstream" now includes everything that subjunctively depends on the function's output, not just things the body causally touches.

**Observation** enters differently than in CDT or EDT. The paper says: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Seeing $x$ does not condition $P$. It selects the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$. Different observations correspond to different nodes, which are different "instances" of the same function.

The paper's summary of the relation to CDT is the most compact statement of the theory: "CDT and FDT both construct counterfactuals by performing a surgery on their world-model that breaks some correlations and preserves others, but where CDT agents preserve only causal structure in their hypotheticals, FDT agents preserve all decision-relevant subjunctive dependencies in theirs."

**Agreement in simple cases.** If every correlation between action and environment is caused by the action, with at most a subjunctive dependence on the function node, then $\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)]$. The three rules coincide. They come apart only where events correlate with the action without being caused by it, as when predictors or twins are present.

## 4. Subjunctive dependence

The paper's key concept is *subjunctive dependence*: when two physical systems compute the same function, "their behaviors 'subjunctively depend' upon that function." Its calculator illustrations make three points.

1. A predictor's model of you and your body are like two calculators computing $6288+1048$. If one outputs 7336, you can be fairly sure the other does too. The dependence is not diminished by a common-cause explanation being unavailable, as with calculators on opposite sides of the universe.
2. Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
3. Mere statistical correlation is not subjunctive dependence. If two calculators happen to both be pink, "if the scribe had bought a green calculator instead, the one in Tokyo would still be pink."

Hence "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." In Peirce's terms, CDT intervenes on the token "my action is $a$," whereas A-FDT intervenes on the type.

Imperfect dependence is allowed. If the predictor is only 99% accurate, the dependence is "weakened, but not eliminated." In the models this appears as a noise node, such as $\textsc{Accurate}$ with $P=0.99$.

### What the source leaves open

The source is candid about three gaps.

- **Construction of $G$.** "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem." Pearl has a theory of how to learn causal structure from intervention and observation. There is no analogue for learning logical-dependence structure.
- **Counterpossibles.** If the function really outputs *onebox*, imagining it outputs *twobox* is a counterpossible. The paper defines a $\mathtt{true}$ operator, $\mathrm{FDT}^*$ (footnote 9 calls this an "evidential version"), but says: "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) avoids this by assuming $G$ is supplied.
- **Fairness.** The paper claims A-FDT does best on "fair" problems, where outcomes depend only on the agent's behavior in the problem at hand. It admits no formal criterion of fairness exists (footnote 15).

### An operational reading (my proposal, not the paper's)

To be usable, Equation (4) needs a working procedure for deciding which nodes hang below $\mathrm{fdt}$. I propose a question for each variable $Z$ in the model:

> *Does a process that computes (or reliably models) this very decision procedure on this input feed into $Z$? If the procedure returned something different, would $Z$ have been different in a way that tracks the output rather than merely co-occurring with it?*

The following inclusion test serves as a rule of thumb for building $G$:

- The body's action node: yes (it implements the function).
- A predictor's prediction node: yes, if she builds an accurate representation of the agent's decision function and bases the prediction on it.
- A twin's action: yes.
- A lesion, an infestation, or a pink calculator: no. These are correlated with the action but do not compute or model the function.

Where the dependence is imperfect, use a noise node, as the paper does. This test only restates the paper's own criterion ("all and only those things that subjunctively depend on the output of her decision-making procedure") as a checklist. Applying it to messy cases, such as a human predictor with unknown accuracy, remains judgment-laden, and the paper offers no more. The paper's point that "we do not yet have a satisfying account" of this is a limit on mechanical application. It is not a license to fudge.

The following steps then run the procedure:

1. Build $(P,G)$ for the problem as it appears to the agent, including nodes $\mathrm{fdt}(P,G,x')$ for each observation $x'$ that could have occurred.
2. For each action $a$, set the node corresponding to the *actual* observation $x$ to $a$ and propagate through $G$.
3. Compute $\mathbb E[V]$ in each hypothetical.
4. Output the maximizer. The source does not specify tie-breaking.

## 5. Worked examples

### 5.1 Newcomb's problem

The model has $\textsc{Accurate}\in\{\text{acc},\text{inacc}\}$ with $P(\text{acc})=0.99$. The graph is $\mathrm{fdt}\to\textsc{Act}$, $\mathrm{fdt}\to\textsc{Prediction}$, $\textsc{Accurate}\to\textsc{Prediction}$, $\textsc{Prediction}\to\textsc{BoxB}$, and $(\textsc{Act},\textsc{BoxB})\to V$.

- $do(\mathrm{fdt}=\textit{onebox})$ gives $\textsc{Act}=\textit{onebox}$ with probability 1 and $P(\text{full})=0.99$. So $\mathbb E[V]=0.99\cdot 10^6=\$990{,}000$.
- $do(\mathrm{fdt}=\textit{twobox})$ gives $\textsc{Act}=\textit{twobox}$ and $P(\text{full})=0.01$. So $\mathbb E[V]=0.99\cdot 1000+0.01\cdot 1{,}001{,}000=\$11{,}000$.

A-FDT one-boxes. Compare CDT's graph, in which $\textsc{Act}$ has no arrow to $\textsc{Prediction}$. There $P(\text{full})=p$ is the same in both hypotheticals, so two-boxing wins by $1000$ whatever $p$ is. (The source's text gives $999{,}000$ for EDT's one-box value. By the stated parameters that figure should be $990{,}000$.)

An objection the paper anticipates: suppose she is nearly certain the box is full. Shouldn't she then two-box? No. To evaluate two-boxing, she asks what the world looks like if *the function* outputs *twobox*, and in that world the predictor's model of the function also said *twobox*. No retrocausation is involved. She is just declining to imagine her action varying while the function's output is held fixed.

### 5.2 The smoking lesion

Here $\textsc{Lesion}$ is a common cause of the urge to smoke and of cancer, and it does not compute the decision function. The lesion fixes which of two utility functions governs the agent, so there are two function-nodes, $\mathrm{fdt}(P_S,G)$ for the agent with the lesion (who likes smoking) and $\mathrm{fdt}(P_R,G)$ for the agent without. $\textsc{Act}$ is a function of $\textsc{Lesion}$ and the two nodes: if the agent has the lesion her action is the first node's output, and if not it is the second's. Intervening on $\mathrm{fdt}(P_S,G)$ leaves $P(\text{lesion})=p$ unchanged. Smoking is then worth $+\$1000$ times the probability that this node controls her action, so smoking beats refraining by $p\cdot\$1000$. A-FDT smokes.

The paper is dismissive of this problem. When formalized, agents must choose under uncertainty about their own desires, which it calls "quite contrived," and it recommends philosophers abandon the case. I take it mainly as a demonstration that one rule handles both this problem and Newcomb's problem, where the difference lies in $G$ and not in the rule.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

The agent sees both boxes. The graph now has two nodes, $\mathrm{fdt}(P,G,\textit{full})$ and $\mathrm{fdt}(P,G,\textit{empty})$. $\textsc{Prediction}$ determines which node controls $\textsc{Act}$, since the prediction fixes which observation the agent gets. The predictor's model depends on the *full-box* node, since the prediction is what she does on seeing two full boxes.

Suppose she sees *full*, and let $q$ be her prior that she two-boxes on seeing *empty*. Then:

- $do(\mathrm{fdt}_{\text{full}}=\textit{onebox})$ gives $0.99\cdot 10^6+0.01\,q\cdot 1000=990{,}000+10q$.
- $do(\mathrm{fdt}_{\text{full}}=\textit{twobox})$ gives $0.01\cdot 1{,}001{,}000+0.99\,q\cdot1000=10{,}010+990q$.

For any $q\in[0,1]$ the first wins, and the paper notes the consistent value is $q=1$. (The source's printed constant "$110,00$" appears to be a typo; the arithmetic gives $10{,}010$.) A-FDT one-boxes while looking at a full box. When she imagines two-boxing, she imagines, with high probability, a world in which she sees an empty box. The conditioning step is absent. Observation chooses the node to intervene on but does not restrict the hypotheticals to worlds consistent with it.

The paper observes that this is "precisely equivalent to paying the driver in Parfit's hitchhiker problem." The driver rescues the agent iff she predicts the agent will pay in the city, so paying is the output of the node she is intervening on, and A-FDT pays. CDT and EDT both condition on or hold fixed the fact of being in the city.

### 5.4 Blackmail

*Mechanical blackmail.* The blackmailer sends the letter iff she predicts the agent pays. Let the agent have received the letter. Intervening on $\mathrm{fdt}(\cdot,\textit{blackmail})=\textit{pay}$ makes the letter near-certain and costs $\$1000$. Setting it to *refuse* makes the letter near-unlikely. The "worst" case, that the program runs and costs $\$10^6$, is multiplied by the near-zero chance of being blackmailed at all. With a predictor who wrongly predicts payment with probability $\varepsilon$:

- *refuse*: expected loss $\varepsilon\cdot 10^6$;
- *pay*: expected loss $\approx\$1000$.

So refuse iff $\varepsilon<10^{-3}$. The paper's example $\varepsilon=0.0009$ gives \$900 and refusal, as it says. It then says "0.011%" leads to payment, but $0.011\%=1.1\times10^{-4}$ gives \$110, which still favors refusing. The threshold computation suggests the intended figure was $0.11\%$. This is my arithmetic, not the source's. The structural point is that A-FDT refuses even holding a letter it "knows" was sent in error, because it is evaluating the kind of agent it is rather than the single case.

*XOR blackmail.* The letter is sent iff (no termites and the agent would pay) or (termites and the agent would not pay). EDT, conditioning on *pay*, infers no termites and pays. CDT refuses, since termites are causally upstream of its act. A-FDT also refuses. Intervening on the function node changes the letter's probability but not the infestation node. The paper notes that A-FDT and CDT refuse for different reasons, and that their hypotheticals differ even when their actions agree. Asked what would have happened had she paid, CDT says the same letter arrives and she loses money, which implies the predictor erred. A-FDT says the predictor would have predicted differently and no letter would have been sent.

### 5.5 Death in Damascus and the cosmic ray

Death's appointment-book entry is computed from a prediction of the agent's decision. With "stay" costing nothing, "flee" costing $\$1000$, and survival worth $\$10^6$, intervening on the function node moves Death's location with the agent's choice. Stay yields $0$ and flee yields $-1000$. A-FDT stays and avoids the instability that besets CDT, whose hypotheticals hold Death fixed. CDT's flip-flopping continues until it settles on a probability mix, and CDT will then also decline a \$1 truly random coin that gives a 50% chance of survival. A-FDT's graph has no arrow from the function node to a *truly* random coin's outcome. So the coin is a fresh 50% chance at $10^6$ and is worth a dollar. This last step is my application of the source's analysis, not a calculation it presents.

In the cosmic ray problem EDT takes the \$1 because it cannot imagine taking \$100 without having been hit by a ray. A-FDT, like CDT, intervenes on the function node, and the cosmic ray is not a function of that node. It takes the \$100.

## 6. Why the rule has this shape

**Counterfactuals versus conditionals.** The paper insists that "conditionals are not counterfactuals." Choosing between a \$1 and a \$100 bill, conditioning on taking the \$1 suggests the agent had a good reason, but counterfactually she would simply be poorer. EDT's hypotheticals "respect too many correlations." CDT's "respect too few," because it imagines actions changing with predictions fixed, which is "a hypothetical scenario in which a perfect predictor made an incorrect prediction." A-FDT's intended middle position: break statistical correlations, keep logically necessary ones.

**Utility and dominance.** The argument for A-FDT is primarily one from utility achieved. Agents who run it do better in the paper's fair Newcomblike problems, and the paper claims to know of no fair dilemma where it does worse. Against the dominance argument for two-boxing, the paper replies that every method of constructing hypotheticals induces its own notion of dominance. There is an A-FDT dominance principle, under which A-FDT never takes a dominated action, and dominance "doesn't afford us a neutral criterion for deciding between candidate theories."

**Precommitment, information, self-endorsement.** A-FDT "act[s] as they would have precommitted to act," without needing costly binding mechanisms. It does not assign negative value to information, since seeing the box merely selects a node. And it endorses its own use, as the paper argues CDT does not.

**Control talk.** The authors argue A-FDT is no more deluded than CDT. A deterministic CDT agent "controls" its token act only by imagining hypotheticals in which it differs, and an A-FDT agent does the same one level up. Any principled objection to controlling the type would apply equally to controlling the token. "We claim only that if an agent wants to get as much utility as she can, she should weigh different imaginary worlds in which her decision procedure has different logical outputs."

## 7. Applying A-FDT to new cases: a checklist and cautions

Everything in this section is my synthesis, built from Equation (4) and the paper's examples.

1. **List the processes that implement or model your decision function on the inputs in play.** These include predictors, twins, and your own future selves where the decision is relevantly the same. The paper's gym example says: "If there are no relevant differences between her decision today versus tomorrow, then she should assume that she will continue going to the gym in the future if she goes today." Its voting example is similar. Do not include things merely correlated with your action.
2. **Build one function node per possible observation.** Say which downstream variables each feeds, and which node controls the act under each observation history.
3. **Assign priors to the non-actual nodes**, for example $q$ above. These can often be left free, because results frequently hold for all $q$. Where they matter, the consistent value is the one A-FDT itself outputs at that node, found by self-consistent assignment. The paper notes the correct $q$ "as you may verify" but does not give a general fixed-point procedure, so this is my suggestion.
4. **Intervene on the actual-observation node, propagate, and compute $\mathbb E[V]$.**
5. **Sanity check.** If the problem rewards or punishes the agent for *which procedure it uses* rather than for its actions or predicted actions, then in the paper's terms it is "unfair." Dilemmas such as "a mind reader gives \$1,000,000 iff she predicts they follow EDT" fall under this. No theory is safe from these, and A-FDT is not claimed to win them.

**Cautions the source supports.** A-FDT's output is only as good as $G$. If the agent misjudges whether a predictor really models her, the rule will faithfully follow the error. The paper also contemplates only idealized, small models. It expects bounded approximations to share the strengths and weaknesses, but does not prove it.

**Where the formalism underdetermines.** Equation (4) as printed has no $\mathrm{Obs}=x$ condition inside the expectation. The paper's transparent-Newcomb calculation, however, writes $do(\mathrm{fdt}(\cdot,\textit{full})=a,\ \mathrm{Obs}=\textit{full})$ in prose. These two are in tension: if $\mathrm{Obs}$ were held at *full* while the node is set to *twobox*, the hypothetical would have no consistent value. My reading, consistent with the numbers actually computed, is that the observation fixes the *node* and then plays no further conditioning role. The paper's footnotes also say that the preferred policy-level variant matters in multi-agent dilemmas, but the source does not show where A-FDT and that variant diverge. I do not claim to know.

## 8. Conclusion

A-FDT, in Equation (4), is a short formula, $\arg\max_a\mathbb E[V\mid do(\mathrm{fdt}(P,G,x)=a)]$, whose content is a structural commitment. When imagining a different choice, change the output of your decision function, and change everything that subjunctively depends on that output, and nothing else. Observations select which instance of the function you are running. They do not condition your beliefs. This one rule one-boxes in Newcomb's problem, smokes in the lesion problem, pays in Parfit's desert, refuses blackmail, and stays in Damascus, and its differences from CDT and EDT are traceable to which dependencies the graph $G$ marks.

The weak point is the same one the authors identify. $G$ is an input and not an output, and nobody yet has a principled theory of how to learn or verify logical dependence structure, or of how to treat counterpossibles in general. A reader can reasonably accept the structure of the proposal while remaining unsure about its application in any particular case. Where a predictor or twin clearly implements the agent's own function, the application is clear and the verdicts are as above. Elsewhere the rule needs a modeling judgment that the source does not supply and that I have only tried to make explicit.