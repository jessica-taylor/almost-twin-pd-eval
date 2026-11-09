# A-FDT: Deciding by Intervening on the Decision Function

## 1. The idea

Any decision theory must say how to evaluate "what would happen if I did a?" Causal decision theory (CDT) answers by intervening on the physical act. Evidential decision theory (EDT) answers by conditioning on it. A-FDT, the theory whose formal presentation is Equation (4) of Yudkowsky and Soares's "Functional Decision Theory: A New Theory of Instrumental Rationality," answers by intervening on the output of the agent's decision function. This essay explains the definition, the surrounding apparatus, and how to apply it. I try to separate what the source states from what I add.

The source's slogan is that the agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Her hypotheticals therefore change two kinds of thing: the output of the function, and everything that *subjunctively depends* on that output. Everything else is held fixed.

## 2. The formal definition

All three theories maximize expected utility,

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

and differ only in how they read the connective "$\hookrightarrow$", that is, in which "epistemic perspective" they adopt. The source borrows this framing from Joyce's representation theorem. Joyce's theorem leaves the constraints on $P(-\hookrightarrow -;x)$ as a free parameter, so A-FDT is not a rival theory of value. It is a rival account of counterfactuals.

The three rules are:

- **EDT (Eq. 2):** $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- **CDT (Eq. 3):** $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **A-FDT (Eq. 4):**
$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution over the variables of the agent's world-model. $G$ is a graph saying how changing a variable propagates to others, and it includes *logical, mathematical, computational* structure as well as causal structure. The underlines denote dequoting: $\mathrm{fdt}(\underline P,\underline G,\underline x)$ names the variable standing for the output of the A-FDT procedure on exactly these inputs. This is self-reference, but the source argues it is harmless. The agent need not know the *value* of that variable in order to have a node representing it, and Kleene's second recursion theorem ("quining") shows such self-representing structures can be built.

The source names two differences from CDT.

1. The intervention targets a node for the *output of the decision procedure*, not the physical act. In the source's words, CDT intervenes on a token ("my action is $a$"), while A-FDT intervenes on the type.
2. Observations are handled differently. CDT conditions on $\mathrm{Obs}=x$. A-FDT *changes which node it intervenes on*: with observation $x$ it intervenes on $\mathrm{fdt}(\underline P,\underline G,\underline x)$, and with observation $y$ on $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

The second difference is what makes A-FDT "updateless" in flavor. It never conditions its world-model on what it saw. It uses the observation only to pick out which of its own input-output behaviors is currently being chosen.

The source also mentions a footnote preference. The authors' preferred formalization iterates over *policies* (maps from observations to actions) rather than single actions. The two coincide in the paper's examples, and I flag where the distinction would matter.

## 3. Subjunctive dependence

What belongs in $G$? The source's answer is subjunctive dependence: two things subjunctively depend on a function when they compute, or contain accurate models of, that function. The source's illustration is two well-functioning calculators computing $6288+1048$. Their outputs are constrained to agree, without either causing the other.

The source makes four points about this notion.

- Causal dependence is a special case of subjunctive dependence. A scribe copying a calculator's output depends on it in both senses.
- Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators would not change colour together.
- Imperfect copies give weakened dependence. A predictor who is 99% accurate yields a 99% correlation, conditional on the function's output.
- Evaluating "what if the function output something else?" is a *counterpossible* (a supposition contrary to logic). The source says this is the main drawback relative to CDT, and it expresses hope that heuristics exist, since humans reason about such matters tolerably well.

## 4. Where the source stops, and an operational reading

The source is explicit that Equation (4) works *given* a graph $G$ that correctly describes how changing a logical variable affects other variables. It says that "it is not yet clear how to construct such a thing" and calls deducing subjunctive-dependence structure from observation "perhaps the largest open problem." It also says it lacks a formal $\mathtt{true}(\cdot)$ operator for conditioning on false logical sentences, and so it takes $G$ as an *input*, exactly as CDT takes causal structure as an input.

So A-FDT as specified is a function of $(P,G,x)$, not of raw experience. A practitioner must supply $G$. The following is my own operational proposal, not the source's. To decide an unfamiliar case:

1. List the variables and identify which physical processes *implement or model* the agent's decision procedure. Examples are twins, predictors, simulators, and copies of the agent across time.
2. Draw the node $\mathrm{fdt}(\cdot)$ with arrows into the agent's act and into every such process. Route the agent's observations through the structure, so that the observation determines which $\mathrm{fdt}(\cdot,x)$ node controls the act.
3. Mark variables that merely correlate with the act through a common cause, with no model of the agent involved. Leave them unconnected to the $\mathrm{fdt}$ node.
4. For each action (or policy), set the $\mathrm{fdt}$ node to it, propagate along arrows, compute $\mathbb E[V]$, and take the argmax.

Step 1 is where the real work and the real uncertainty lie. The test I suggest is whether the other process would have been different *had the function been different, in a way that tracks the function's output rather than the agent's physical situation*. The distinction in the source's examples is between a thing that *reasons about or copies* the agent and a thing that merely *shares a cause* with her.

## 5. Worked applications

**Newcomb's problem.** Let the nodes be $\mathrm{fdt}$, Act, Prediction, Accurate (99%), Box B, and $V$. Arrows run from $\mathrm{fdt}$ to both Act and Prediction. Intervening with $\mathrm{fdt}=\text{onebox}$ makes Act = onebox and Box B full with probability 0.99, so $\mathbb E[V]=\$990{,}000$. With $\mathrm{fdt}=\text{twobox}$, Box B is full with probability 0.01, giving $\$11{,}000$. A-FDT one-boxes. CDT's graph lacks the arrow from the function to the prediction, so for any fill probability $p$ it finds two-boxing better by \$1,000. EDT one-boxes, but through conditioning on a correlation.

The source stresses that no retrocausation is involved. The agent just declines to imagine her act changing while the predictor's model of her stays fixed. When she imagines two-boxing, she imagines a world with a probably empty box.

**Smoking lesion.** Here the graph must differ from Newcomb's. The lesion causes both the desire to smoke and cancer, and the cancer does not depend on the function's output. The source formalizes this with two utility functions, one for each lesion state, and hence two possible functions the agent might be running. Intervening on the one actually relevant leaves $P(\text{lesion})$ unchanged. For the lesion-version function, smoking has expected utility greater than refraining by $p\cdot\$1{,}000$, where $p$ is the probability that this function is the one controlling her act. A-FDT smokes. The lesson is that the same decision structure gets different graphs depending on whether there is a predictor-like process (as in Newcomb) or merely a common cause (as here). The source also remarks that the problem is contrived, and that it is unfair to EDT.

**Transparent Newcomb / Parfit's hitchhiker.** Upon seeing a full box, A-FDT intervenes on $\mathrm{fdt}(\ldots,\text{full})$. If the predictor is accurate, setting that function to onebox yields a full box and a one-boxing act. Setting it to twobox yields, with probability 0.99, a predictor who left the box empty, in which case the agent is *not* running the "full" function at all. With $q$ the probability that she two-boxes upon seeing an empty box, the values are $\$990{,}000+0.01q\cdot\$1{,}000$ against $\$110{,}000+q\cdot\$990$. A-FDT one-boxes even while looking at the full box. The source notes that this is exactly equivalent to paying the driver in Parfit's hitchhiker. In both cases the agent chooses as she would have precommitted to choose, but without a costly precommitment mechanism.

**Blackmail.** In mechanical blackmail, the blackmailer runs the program iff she predicts the agent would pay. Intervening on $\mathrm{fdt}(\ldots,\text{blackmail})$ with *pay* gives near-certain blackmail and a \$1,000 loss. With *refuse* it gives near-zero blackmail probability. A-FDT refuses even when holding the letter. For an imperfect blackmailer the arithmetic is a real comparison. With misprediction probability 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation, against a certain \$1,000 for paying. Paying wins only if the error rate is above 0.1%. The source's figure of 0.011% for paying looks like a slip, since by its own numbers the threshold is 0.1%, so I do not rely on it.

**Death in Damascus and XOR blackmail.** In Damascus, Death's book depends on the agent's function. A-FDT concludes that wherever it goes Death will be, and so saves the \$1,000 by staying. It does not have the instability of CDT, which pairs a belief about its own location with a hypothetical in which Death's location is independent of it. In XOR blackmail, A-FDT's intervention changes whether the letter arrives, but not whether the house has termites, so it refuses. EDT pays because conditioning on paying "removes" the bad news.

## 6. Dominance, fairness, and reflective stability

Two-boxing "dominates" only if dominance is defined with CDT counterfactuals, where the action changes and the prediction is held fixed. The source argues that every method of constructing hypotheticals induces its own dominance notion, so dominance cannot arbitrate between theories. A-FDT has its own: holding all subjunctive dependencies fixed, switching to another output never beats the A-FDT choice. The source prefers instead to judge theories by utility achieved.

It limits this claim to "fair" problems, meaning those where the payoff depends on the agent's *behavior* and not on which decision procedure she uses, and where her beliefs are accurate. Newcomb's predictor punishes two-boxers, not CDT as such. The source admits it lacks a formal definition of fairness. Its footnote shows a difficulty: a game that punishes anyone who acts like a copy of A-FDT is plainly unfair to A-FDT but not to the others.

The source also claims reflective stability in fair problems. An agent facing blackmail would not wish to switch temporarily to CDT, since by her own hypotheticals that would make her a more attractive target. The claim is the authors', and it is argued by examples, not proved.

## 7. My own cautions and extensions

These are my comments, not the source's.

- **Garbage in, garbage out.** Since $G$ is an input, A-FDT's prescriptions are only as good as the dependency structure given. The same problem text can yield different graphs under different modeling choices. The source's one-boxing results are derived from graphs it chose, not from a general procedure for deriving them.
- **Partial correlation.** The source treats imperfect predictors by letting the Accurate node vary. A natural extension is to give each downstream process a mixture of dependence on the function and noise. That fits the source's remark that imperfect modeling weakens but does not eliminate dependence, but a formal calibration of the mixture is not given.
- **Multi-agent cases.** For a voting coalition, or an agent coordinating with her future selves, the source says A-FDT agents recognize their decisions as not independent whenever they run the same function on relevantly similar inputs. In the gym example it says Fiona goes "if there are no relevant differences" between today's and next week's decisions. The phrase "relevant differences" carries real weight, and the source gives no criterion for it.
- **Policies versus actions.** I would adopt the policy-level reading by default, since observation-dependent intervention (transparent Newcomb, blackmail) is already policy-like, but the source does not require it.

## 8. Conclusion

A-FDT is CDT with the intervention point moved. Instead of asking what would follow from my body doing something else, it asks what the world would look like if *this very procedure* output something else. That includes the predictors, twins, and copies whose behavior is tied to the same function, while keeping fixed things that merely correlate with the act. Equation (4) makes this a concrete maximization given $(P,G,x)$. It one-boxes, smokes, pays the hitchhiker, refuses blackmail, and stays in Damascus, all from a single rule. The source is candid about the price. Constructing $G$, especially its logical dependencies, remains an unsolved problem, and counterpossible reasoning is not yet formalized. Fairness is also informal. Within those limits, A-FDT is a clearly defined procedure whose answers depend on a dependency model that the user must supply.