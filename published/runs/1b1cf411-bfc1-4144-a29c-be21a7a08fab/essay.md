# A-FDT: Choosing by Intervening on the Output of Your Own Decision Function

## 1. The idea in one paragraph

Every expected-utility theory has to say what the agent should imagine when she imagines doing something else. A-FDT (action functional decision theory) says she should imagine that *the output of the function she is computing* is different, and that everything which depends on that output changes with it. Nothing else changes. The source paper (Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality") puts it this way: the agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper writes the resulting rule as Equation (4) of Section 5, and I take that equation as the definition of A-FDT. The paper itself calls it simply "FDT". It prefers a policy-level refinement, which I discuss in §6. I use "A-FDT" for the action-level rule of Equation (4), and I name every other theory explicitly.

The essay has three parts. §§2–3 give the formal definition and an operational recipe. §§4–5 apply it to several decision problems. §§6–7 mark what the source leaves open, separate the source's claims from my own proposals, and discuss the philosophical motivation.

## 2. The formal definition

### 2.1 Expected utility with a free connective

The paper takes CDT, EDT and A-FDT to be expected-utility theories. Each maximizes

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j) \tag{1}$$

Here $a$ ranges over a finite action set $\mathcal A$, $o_j$ over outcomes, $x$ is an observation history, and $\mathcal U$ is a bounded utility function. The connective "$\hookrightarrow$" is a "decision hypothetical". Following Joyce's representation theorem, the paper treats the theories as agreeing about valuation and disagreeing only about "the epistemic perspective from which actions are to be evaluated". Joyce is quoted: "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

The three theories are:

- **EDT** reads "$\hookrightarrow$" as Bayesian conditioning: $\operatorname{argmax}_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$.
- **CDT** (in Pearl's formulation) intervenes on the physical action node: $\operatorname{argmax}_a \mathbb E(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$.
- **A-FDT** is Equation (4):

$$\mathrm{FDT}(P,G,x) := \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}$$

I abbreviate the left side as $\text{A-FDT}(P,G,x)$ below.

### 2.2 The ingredients

**The model $(P,G)$.** $P$ is a probability distribution over variables, and $G$ is a graph. In CDT, $G$ encodes causal structure. In A-FDT, $G$ must encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly". It says how changing a *logical* variable propagates to other variables. This is the source's stated requirement: "we require that the relevant logical dependency structure be given as an input to FDT, in the same way that the relevant causal structure is given as an input to CDT."

**The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$.** The variable $P$ contains variables for the outputs of mathematical functions. For instance, there is a variable for $6288+1048$ with most of its mass on $7336$. Among these is a variable denoting the output of A-FDT itself when run on the agent's own model and observations. The underline means dequoting: if $x:=3$, then $\mathrm{Z}\underline x$ names the variable $\mathrm{Z}3$. This is self-referential, since the node's name depends on the model that contains it. The paper calls the self-reference harmless. The agent need not know the *value* of the output to have a variable *representing* it, and Kleene's second recursion theorem ("quining") shows how a data structure can contain an accurate representation of itself.

**The intervention.** $\mathrm{do}(\cdot)$ is Pearl's operator. It sets the chosen node to $a$, recomputes every descendant of that node in $G$, and leaves everything else untouched. The expectation $\mathbb E(V\mid\cdot)$ is taken over the resulting distribution.

### 2.3 Two differences from CDT

The paper identifies exactly two differences between Equations (3) and (4):

1. CDT intervenes on $\mathrm{Act}$, a node for a *physical* fact about the agent's body. A-FDT intervenes on a node for a *logical* fact about her decision function. In Peirce's terms, CDT intervenes on the token "my action is $a$" and A-FDT intervenes on the type.
2. CDT responds to observation by conditioning. A-FDT responds to observation "by changing which node it intervenes upon". With observation $x$ she intervenes on $\mathrm{fdt}(\underline P,\underline G,\underline x)$, and with observation $y$ on $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

The second difference is subtle, and I return to it in §4. The paper's slogan for the relationship is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

### 2.4 What "subjunctive dependence" means

Two physical systems that compute the same function (or one that models the other) have behaviors that "subjunctively depend" on that function. Two calculators on opposite sides of the globe, both computing $6288+1048$, are the paradigm. Causal dependence is a special case: a scribe watching a calculator would write something different if it output something different. Mere statistical correlation is not subjunctive dependence. If two calculators are both pink by coincidence, then had the scribe bought a green one, the other would still be pink.

This is why the model does not need to be retrocausal. The paper stresses that the A-FDT agent "does not think that a physical signal passes between her action and the predictor's prediction; she just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value, since she thinks the predictor is good at reasoning about FDT."

## 3. Applying the rule

Equation (4) does not by itself tell you how to build $G$. Given $(P,G)$, though, it is an algorithm:

1. Locate the node $f_x := \mathrm{fdt}(\underline P,\underline G,\underline x)$ for the actual observation $x$. Other observations $y$ get their own nodes $f_y$.
2. For each $a\in\mathcal A$, form the hypothetical by setting $f_x=a$ and recomputing all its descendants in $G$. Descendants include the agent's own action, any predictor or twin that models the function, and any variable that decides *which* observation the agent receives.
3. Compute $\mathbb E[V]$ in each hypothetical and output the maximizer.

Two practical points follow from the paper's examples.

*First, observation is not conditioned on.* The text writes $\mathbb E(V\mid \mathrm{do}(f_{\text{full}}=a,\mathrm{Obs}=\text{full}))$ for the transparent Newcomb problem. The actual computation, however, lets the intervention change which observation the agent would have received. The expected utility of one-boxing is $0.99\cdot\$1{,}000{,}000+0.01\cdot q\cdot\$1{,}000$, which includes the branch where she sees an empty box. So the observation enters only by selecting the intervention node. It does not restrict the distribution.

*Second, the node $f_x$ is a variable of the model, not the agent's literal state.* In the smoking lesion, the agent does not know which of two functions she is running. Her model has two nodes, one for each utility function, and the lesion determines which of them controls $\mathrm{Act}$.

### 3.1 A baseline: when all theories agree

If every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$, then

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)],$$

and the three theories coincide. They come apart only when something correlates with the action without being caused by it, such as a predictor, a twin, or a common cause.

## 4. Worked examples

I use the paper's graphs and add some computations of my own, each flagged as such.

### 4.1 Newcomb's problem

A-FDT's graph has the node $F=\mathrm{fdt}(\underline P,\underline G)$ with arrows to both $\mathrm{Act}$ and $\mathrm{Prediction}$, because both represent something in the world that depends on the function's output. A noise node $\mathrm{Accurate}$ (0.99) also feeds into $\mathrm{Prediction}$. Then:

- $\mathrm{do}(F=\text{onebox})$: $\Pr(\text{box B full})=0.99$, so $\mathbb E[V]=\$990{,}000$.
- $\mathrm{do}(F=\text{twobox})$: $\Pr(\text{full})=0.01$, so $\mathbb E[V]=0.01\cdot 1{,}001{,}000+0.99\cdot1000=\$11{,}000$.

A-FDT one-boxes. (The source's text gives Eve's one-boxing value as \$999,000. With the stated 0.99 it should be \$990,000, so I take that as a slip.)

The common objection is that, being nearly sure box B is full, she should take both boxes. The source's reply is that when she asks "what if I two-boxed?", she imagines the *function* returning *twobox*, and then the prediction changes with it. CDT's hypothetical holds the prediction fixed while changing the physical act. That is like imagining a working calculator on $6288+1048$ outputting something other than $7336$ while "holding constant" the fact that the sum is $7336$.

### 4.2 The smoking lesion

Here the same rule gives a different graph. The lesion is a common cause of the urge to smoke and of cancer. Cancer is not a descendant of the decision function, because the cancer does not model the agent. Changing $f$ moves $\mathrm{Act}$ but leaves $\Pr(\text{lesion})=p$ alone. The source then computes, for the agent with smoking-loving utility $\mathcal U_S$, that smoking is better than refraining by exactly $p\cdot\$1{,}000$. So A-FDT smokes. The source's takeaway is that "a single compact decision criterion... prescribes both one-boxing and smoking."

Two things should be noticed. The graphs differ, even though the numerical problem is isomorphic to Newcomb's, because the dependence structure differs. The paper also calls the problem "badly confused" (the agent must be ignorant of her own preferences) and treats it only for its historical significance.

### 4.3 Transparent Newcomb and Parfit's hitchhiker

Let $f_{\text{full}}$ and $f_{\text{empty}}$ be the function's outputs on the two possible observations. The prediction depends on $f_{\text{full}}$, and the prediction determines which observation she gets, so the prediction determines which node controls $\mathrm{Act}$. Let $q$ be her credence that she two-boxes on seeing an empty box. With full box observed:

- $\mathrm{do}(f_{\text{full}}=\text{onebox})$: $0.99\cdot 1{,}000{,}000 + 0.01\cdot 1000q = 990{,}000+10q$.
- $\mathrm{do}(f_{\text{full}}=\text{twobox})$: $0.01\cdot 1{,}001{,}000+0.99\cdot1000q = 10{,}010+990q$.

Even for $q=1$, one-boxing wins ($990{,}010$ against $11{,}000$). (The source prints "$\$110,00$" for the second figure, evidently a typo.) A-FDT therefore leaves the \$1,000 behind while looking at a full box. By the same structure it pays the driver in Parfit's hitchhiker: "one-boxing in the transparent Newcomb problem *is precisely equivalent to paying the driver*." When she imagines two-boxing, she imagines a world in which she most likely saw an empty box.

The paper offers three supporting arguments for this verdict: precommitment, value of information, and utility. A-FDT acts as it would have precommitted to act, without needing a costly precommitment device. It never assigns negative value to information. And agents of its type tend to be the ones who see full boxes.

### 4.4 XOR blackmail and mechanical blackmail

In the XOR blackmail the letter is true iff exactly one of "no termites and you pay" or "termites and you don't pay" holds. EDT pays, because conditioning on paying makes termites impossible. CDT refuses because termites are causally upstream of its action. A-FDT also refuses, but for a different reason. In its graph, the node $f_{\text{letter}}$ affects what she does on receiving a letter and the probability that a letter is sent, but not $\Pr(\text{termites})$.

The mechanical blackmail illustrates the "global" character of the rule. Paying yields a world in which she is blackmailed and loses \$1,000. Refusing yields a world where she is (with a perfect predictor) never blackmailed. A-FDT refuses even while holding the letter. For an imperfect blackmailer with error rate $\varepsilon$, refusing costs about $\varepsilon\cdot\$1{,}000{,}000$ in expectation, while paying costs about \$1,000. The break-even is therefore $\varepsilon\approx0.1\%$. The source says she refuses at 0.09% error, which matches this, and that she pays at "0.011%". By my arithmetic the crossover for paying is just above 0.1%, so I read "0.011%" as a typo for something like 0.11%.

### 4.5 Death in Damascus

The agent's action and Death's location both descend from $f$, via Death's book. With staying costing nothing and fleeing costing \$1,000, and survival worth \$1,000,000:

- $\mathrm{do}(f=\text{stay})$: Death is in Damascus, she dies, $V=0$.
- $\mathrm{do}(f=\text{flee})$: Death is in Aleppo, she dies, $V=-\$1{,}000$.

She stays, with no instability. CDT's hypothetical holds Death's location fixed while the agent's changes. The result is a deliberation that oscillates, or settles on a mixed state in which a truly random \$1 coin (which would give a real 50% survival chance) looks worthless. In A-FDT's graph the coin is valuable: if Death cannot predict the coin, then using it yields a hypothetical in which her location is independent of Death's. That gives $\approx\$500{,}000-\$1$, which beats $0$. (The coin application is my extension of the paper's discussion to Equation (4).)

### 4.6 The twin prisoner's dilemma with imperfect copying

With a perfect twin, $f$ drives both actions: cooperate gives \$1,000,000 and defect gives \$1,000. Suppose instead that the twin copies $f$ with probability $1-\varepsilon$ and otherwise does the opposite. This is my own variation, modeled on the paper's treatment of imperfect predictors. Then

$$\mathbb E[\text{coop}]=(1-\varepsilon)\,10^6,\qquad \mathbb E[\text{defect}]=(1-\varepsilon)\,10^3+\varepsilon\,1{,}001{,}000,$$

and cooperation wins iff $999{,}000(1-\varepsilon)>1{,}001{,}000\,\varepsilon$, i.e. $\varepsilon<999/2000\approx0.4995$. Noise weakens the dependence without eliminating it, and the rule weighs the strength of the dependence quantitatively. This matches the paper's remark that "if the predictor's model is imperfect... then the interdependence is weakened, but not eliminated."

## 5. Why this is not CDT in disguise, and not EDT

The paper diagnoses the two rivals as having malformed hypotheticals: "EDT respects too many action-environment correlations, while CDT respects too few."

- EDT keeps correlations that are merely statistical, such as lesion and smoking. It can also be made to do anything by extreme priors on its own action. In the cosmic ray problem it takes \$1 because it "cannot imagine breaking" the correlation between taking \$100 and being hit by a ray.
- CDT breaks correlations that are logically forced, for example with a perfect predictor. Its hypothetical has "a perfect predictor [making] an incorrect prediction".
- A-FDT keeps exactly the correlations that are subjunctive dependencies, namely those running through a shared function, and breaks all the others.

Because Equation (4) has CDT's form, with intervention in place of conditioning, it avoids EDT's problems with common causes, and it inherits the benefits of a $\mathrm{do}$-style hypothetical. Because the intervention point is the function rather than the act, it handles predictors and twins.

## 6. What the source leaves open, and my proposals

**Claims of the source (stated in the paper).** Equation (4) as the formal presentation of the rule. The two differences from CDT. The requirement that $G$ be supplied as input. The claim that the theory is formally an expected-utility theory in Joyce's sense. The treatment of the cases above. The claim that A-FDT agents are reflectively stable in "fair problems". The statement that "the authors have not been able to construct an intuitively fair dilemma where FDT loses to a rival decision theory."

**Open questions the source states itself.**

1. *How to learn $G$.* "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Whether it can be done "within Pearl's framework" is also unclear.
2. *The $\mathtt{true}$ operator.* The paper first writes an evidential-style version, $\operatorname{argmax}\mathbb E(V\mid \mathtt{true}(\mathrm{fdt}=a))$, and notes that "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) sidesteps this by supplying $G$.
3. *Counterpossibles.* Setting a logically determined output to a different value is a counterpossible. The paper says that this is "the main drawback of FDT relative to CDT at this time", and that the difficulty is "technical rather than philosophical."
4. *Fairness.* There is no formal criterion yet separating fair from unfair problems, so the claim of optimality on fair problems cannot be tested systematically.
5. *Policies vs. actions.* Footnotes 7 and 16 say the authors' preferred formalization intervenes on a policy (a map from observations to actions) rather than an action. The paper sets this aside because it matters only in multi-agent dilemmas, and it does not spell out the policy formalization. This is exactly why I label Equation (4) "A-FDT".

**My proposals and interpretations (not claims of the source).**

*(a) Graph construction heuristics.* The paper's examples suggest a practical test for adding an arrow from $f$ to a variable $Z$: *Does $Z$ get computed, modelled, or copied by something that runs the same function (or a good model of it)?* Predictors, twins, simulated copies, and future selves in repeated situations pass this test. Common causes (lesions, termites) and downstream consequences of the act fail it or pass it only through the act. This heuristic is mine, an operationalization of the paper's description, not a derivation.

*(b) Uncertainty about $G$.* When the agent is unsure whether a dependence exists, one natural extension is to put a distribution over graphs, $\{(G_i,w_i)\}$, evaluate $\mathbb E_{G_i}[V\mid\mathrm{do}(f=a)]$ for each, and take the $w$-weighted average. This is equivalent to enlarging $P$ with structure variables. The paper does not do this, but it is consistent with the interpretation of $G$ as part of the model $M$. It also gives sensible answers: with a 99% accurate predictor, mistaken belief in a causal-only story costs far more than the \$1,000 at stake.

*(c) Imperfect dependence as noise nodes.* The paper's $\mathrm{Accurate}$ node is one way to represent weakened dependence. I used the same device in §4.6. It allows a smooth transition between CDT-like and A-FDT-like behavior as dependence strength varies.

*(d) Observation and the choice of node.* Where the problem has several possible observations, I treat each $f_y$ as a separate node, with the actual $x$ selecting which is intervened on. The model may have different probability on different $f_y$ as predicted by others. This reading is what makes the transparent Newcomb calculation go through.

*(e) The policy-level variant.* If the agent intervened on a whole policy, then every $f_y$ would be set jointly. In single-agent problems with a single decision point the two coincide. I expect them to differ when the same function's outputs on different inputs are jointly modelled by a counterpart, but this is speculation, and the paper does not address it.

## 7. Philosophical motivation and objections

**Utility as the test.** The paper's central argument is the "argument from utility". Agents following CDT or EDT face empty boxes or die in the desert, and A-FDT agents tend not to. This defeats the dominance argument, because every hypothetical-construction method has its own dominance principle. CDT-dominance holds the prediction fixed. An "FDT-style" dominance principle holds subjunctive dependencies fixed, and by it A-FDT never takes a dominated action. As the paper puts it, "dominance doesn't afford us a neutral criterion."

**Control.** One objection is that A-FDT agents act as though they control abstract functions or the past. The paper replies that CDT faces a parallel difficulty in deterministic worlds. If the objection works against controlling a decision type, it also works against controlling a decision token. "Since CDT and FDT face analogous difficulties in making sense of the idea of 'control,' this factor cannot help us decide between the theories." The theory is meant as a procedure that needs no commitment about free will or the metaphysics of possible worlds.

**Fairness.** Newcomb's predictor responds to actions, not to the agent's algorithm. In the paper's phrase, "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*." A problem that rewards or punishes agents *for being A-FDT* is a different matter, and no decision theory is safe there. I add one qualification of my own. Because the correct treatment of such cases depends on how problems are individuated, the fairness claim is currently a heuristic and not a theorem. Footnote 15's "copy of Fiona" example shows why it is hard to formalize.

**Reflective stability.** Since A-FDT evaluates by "what if this function output differently", it has no reason to self-modify in fair problems. The paper claims CDT does, in ongoing Newcomb-like cases, and that this undermines it as a normative theory.

**Strangeness of some verdicts.** Refusing the blackmail while holding the letter, and one-boxing before two full boxes, are odd. The paper's defence is that A-FDT asks what "the entire universe" would look like if the function behaved differently, and picks the best such universe. In both cases it admits that this means imagining worlds where observations differ from the actual ones: "both hypotheticals contain impossibilities". CDT imagines predictions failing and A-FDT imagines different observations. The difference it claims is a practical one.

## 8. Conclusion

A-FDT is a small formal change with large consequences. Equation (4) keeps CDT's machinery of graphs and $\mathrm{do}$-surgery, but moves the point of intervention from the agent's physical act to the output of her decision function, and moves her response to observation from conditioning to selecting a different node. With a graph that encodes logical dependence, it one-boxes in Newcomb, smokes in the lesion problem, pays in Parfit's hitchhiker, refuses blackmail, and stays in Damascus, all using one rule.

The theory's weakness is also clear from the source. It is only as good as the dependency graph it is given, and no account yet exists of how to learn that graph, reason about counterpossibles, or define fairness. The heuristics and extensions in §6 are one way to proceed in practice, but they are mine, not the paper's. The decision-theoretic content of A-FDT is clearest when one-boxing, paying, and refusing are seen as results of one question, "which output of this very function would yield the best outcome?", asked relative to a model that records what depends on the answer.