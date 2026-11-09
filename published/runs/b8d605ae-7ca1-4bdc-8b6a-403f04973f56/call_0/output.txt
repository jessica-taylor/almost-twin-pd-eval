# A-FDT: Choosing by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision theory whose formal statement is Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." The paper calls the theory FDT. I use the name A-FDT for that Equation (4) formulation throughout. Where I discuss other theories I name them: causal decision theory (CDT), evidential decision theory (EDT), and the variant FDT′ that the paper considers and rejects.

The paper's slogan is that an agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" CDT asks which physical act causes the best outcome, and EDT asks which act would be the best news. A-FDT asks what the world would look like if this very decision procedure returned a different value.

The essay has three parts: the formal procedure, how it handles dependencies and counterfactuals, and the worked cases. I flag where the paper stops and I add assumptions of my own.

## 2. The formal setting

All three theories share a template, which the paper's Equation (1) writes as maximizing

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

Here $a$ ranges over a finite action set, $x$ is an observation history, and $\mathcal U$ is a bounded utility function. The paper follows Joyce's observation that expected-utility theories "disagree about the epistemic perspective from which actions are to be evaluated," that is, about how to read the connective "$\hookrightarrow$".

- EDT reads it as conditioning (Equation 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT reads it as Pearl intervention on the physical action node (Equation 3): $\arg\max_a\mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT is Equation (4):

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\Big(V\;\Big|\;do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- **$P$**, a probability distribution over variables of the agent's world-model. It includes variables for the outputs of mathematical functions, such as the value of $6288+1048$.
- **$G$**, a graph encoding how changing a variable propagates to others. The paper stresses that it must encode "logical, mathematical, computational, causal, etc. structure," not only physical causation.
- **$x$**, the observations.

The underlined arguments denote dequoting. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is the node representing the output of this very procedure on these very inputs. The self-reference is harmless. The agent need not know the value of its own output to have a variable representing that value, and Kleene's recursion theorem ("quining") shows how a structure can contain an accurate representation of itself.

The procedure is a recipe:

1. Build $(P,G)$ for the situation.
2. Locate the node $\mathrm{fdt}(P,G,x)$ for the observations actually received.
3. For each action $a$, apply $do(\mathrm{fdt}(P,G,x)=a)$. This sets the node to $a$ and recomputes everything downstream of it in $G$, whether physically or subjunctively downstream. Everything else is held fixed.
4. Compute $\mathbb E[V]$ in each resulting hypothetical and return the maximizer.

The paper's footnotes say its preferred formalization intervenes on policies (maps from observations to actions) rather than single actions. That makes no difference in the paper's examples, but it matters in some multi-agent problems. I follow the paper in working with actions at a given observation, and I note below where the policy view is the natural reading.

## 3. The two differences from CDT

The paper identifies exactly two.

**(i) The intervention point.** CDT cuts the node for the *token*, the physical act. A-FDT cuts the node for the *type*, the function's output. Anything that subjunctively depends on that output changes in the hypothetical. This includes the agent's own body, a twin running the same computation, and a predictor holding an accurate model of the agent.

**(ii) The treatment of observation.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes which node it intervenes on: $\mathrm{fdt}(\ldots,x)$ becomes $\mathrm{fdt}(\ldots,y)$ when the observation changes. Observation therefore selects an entry of the function's input-output table. It does not shrink the set of worlds under consideration. This is why A-FDT can imagine, while holding a full box, a world in which it would have seen an empty one.

When every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$, the three theories coincide. The paper writes this as $\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\mathrm{fdt}=a)]$. They come apart only when something correlates with the action without being caused by it, as with predictors, twins, and blackmailers.

## 4. Subjunctive dependence

The paper defines the relevant dependence informally: when two physical systems compute the same function, their behaviors "subjunctively depend" on that function. The paper's slogan is that A-FDT is to subjunctive dependence as CDT is to causal dependence.

The paper makes several points about this relation:

- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators do not covary under intervention.
- It is graded. With an imperfect predictor or a noisy agent the dependence weakens without vanishing, as with calculators that may suffer cosmic-ray errors.
- Applying it requires evaluating counterpossibles, since a deterministic function has only one real output. The paper admits that this "is the main drawback of FDT relative to CDT at this time." It argues the difficulty is technical, not philosophical, because human mathematicians reason under logical uncertainty.

A-FDT sidesteps the lack of a general $\mathtt{true}(\cdot)$ operator by assuming the dependency graph is supplied as input, just as CDT assumes the causal graph is supplied. The paper calls learning that graph from observation "perhaps the largest open problem" for the theory. The formal definition is therefore conditional: *given* an accurate $G$, Equation (4) is a complete algorithm. A user of the theory has to do the modeling.

## 5. Worked examples

Dollar amounts stand for utilities, as in the paper.

### Newcomb's problem

Fiona's graph has a node $\mathrm{fdt}(P,G)$ with arrows to $\mathrm{Act}$ and to $\mathrm{Prediction}$. $\mathrm{Prediction}$ also depends on the noise variable $\mathrm{Accurate}$ (0.99 accurate), and $\mathrm{Box\,B}$ follows the prediction.

- $do(\mathrm{fdt}=\textit{onebox})$ gives $\mathrm{Act}=\textit{onebox}$ and $\Pr(\text{full})=0.99$, so $\mathbb E[V]=\$990{,}000$.
- $do(\mathrm{fdt}=\textit{twobox})$ gives $\Pr(\text{full})=0.01$, so $\mathbb E[V]=\$11{,}000$.

She one-boxes. CDT's graph has $\mathrm{Act}$ causally independent of the box, so it adds $\$1{,}000$ to either branch and two-boxes. EDT also one-boxes, by conditioning. The paper notes that this holds unless its prior on two-boxing is 1, since conditioning on a probability-zero act is undefined.

Nothing retrocausal is assumed. The paper insists that Fiona "just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value."

### Smoking lesion

Here the lesion should not depend on the decision function. In Fiona's graph the lesion influences which version of the function governs $\mathrm{Act}$, and the cancer is downstream of the lesion only. Intervening on the function leaves $\Pr(\text{lesion})=p$ unchanged. Smoking is then better by $p\cdot\$1{,}000$, so she smokes. The same Equation (4) therefore yields one-boxing in Newcomb's problem and smoking in the lesion problem. The only input that differs is the graph, specifically whether the problematic variable is downstream of the function. The paper itself calls the lesion problem contrived and "badly confused."

### Transparent Newcomb and Parfit's hitchhiker

Having seen a full box, Fiona intervenes on $\mathrm{fdt}(P,G,\textit{full})$. A-FDT's hypothetical for two-boxing is not "full box, take both." Since the predictor models the function's response to a full box, setting that response to *twobox* makes the box probably empty, and the agent then runs the "empty" branch.

Writing $q$ for her probability of two-boxing after an empty box, the paper computes:

- One-boxing: $\$990{,}000+0.01q\cdot\$1{,}000$.
- Two-boxing: $0.01\cdot\$1{,}001{,}000+0.99q\cdot\$1{,}000$.

One-boxing wins whatever $q$ is. She leaves the extra $\$1{,}000$ even while looking at two full boxes. The paper notes this is structurally identical to paying the driver in Parfit's hitchhiker.

### XOR blackmail and mechanical blackmail

In XOR blackmail, intervening on $\mathrm{fdt}(\ldots,\textit{letter})$ changes whether the letter is sent and what she does if it arrives. It does not change whether the house has termites, so she refuses. In mechanical blackmail she compares "pay, and always be blackmailed and lose $\$1{,}000$" against "refuse, and (nearly) never be blackmailed". She refuses.

The paper also handles an imperfect blackmailer. With error rate 0.0009, refusing costs $0.0009\cdot\$1{,}000{,}000=\$900$ in expectation, against a certain $\$1{,}000$ for paying, so she refuses. At error rate 0.00011 the refusal cost is about $\$110$, which is below $\$1{,}000$, so she pays. The same logic applies to any threshold. The comparison is between policies as priced by the dependence structure, not between outcomes in the realized world.

### Death in Damascus

The agent's location and Death's page in the appointment book both depend on the function's output. Fiona stays and saves the $\$1{,}000$, since wherever she goes Death will be. CDT is unstable here because it holds Death's location fixed.

## 6. Why the construction is principled

The paper's diagnosis is that EDT's hypotheticals respect too many correlations, including merely statistical ones (the cosmic-ray problem and XOR blackmail both exploit this). CDT's respect too few, since it breaks the correlation between an action and the predictions of agents running the same computation. A-FDT keeps exactly the correlations that survive intervention on the decision function. The paper argues this is the optimal predisposition for any "fair" problem.

Three further claims from the source:

- **Dominance is theory-relative.** Every hypothetical-building method yields its own dominance notion, so dominance cannot arbitrate between theories. Under A-FDT dominance, one-boxing is not dominated. The paper prefers to judge theories by utility achieved.
- **Fairness.** A problem is "fair" if outcomes depend on the agent's behavior in that problem, not on her decision procedure as such. The paper admits no formal criterion exists. Footnote 15 shows the difficulty: a problem that punishes copying Fiona's action is unfair to her.
- **Reflective stability.** The paper claims A-FDT agents never wish to self-modify in fair problems and need no costly precommitments. The one-boxer in the transparent problem acts as she would have precommitted.

The paper also discusses a worry about "control." It answers that any objection to controlling a function's output equally undermines a deterministic CDT agent's "control" of her action token.

## 7. Open questions and operational guidance

The source leaves three matters open. In each case I separate what the paper says from what I propose.

**(a) Building $G$.** The paper requires $G$ as input and gives no derivation procedure. Proposal (mine, not the paper's): a practical modeler should ask, for each variable, whether it would be different if the agent's decision procedure returned a different value at the input she actually has. Include a subjunctive arrow when the variable is produced by a model of the agent, a copy of the agent, or someone reasoning about the agent's reasoning. Omit it when the variable is merely correlated through a common cause that does not model the agent's decision (the lesion). Some cases will be uncertain, so a distribution over candidate graphs is a natural extension, though not one the paper develops.

**(b) Imperfect or non-literal dependence.** The paper handles this through noise variables like $\mathrm{Accurate}$, and the blackmail analysis shows that thresholds then matter. I suggest treating a predictor's reliability as the strength of the arrow and computing expected utilities as above. The question of how a predictor's accuracy generalizes across inputs it never faces is not addressed.

**(c) Policies versus actions.** The authors' preferred formalization intervenes on a whole policy. In multi-agent games, where one decision must be coordinated across many observation branches, I would use the policy reading. Equation (4) as printed intervenes on one branch's output, with the other branches entering as priors like $q$ above. The paper shows the answer is robust to these priors in its examples, but I do not claim this in general.

A caution: a mismodeled graph yields confident wrong answers, just as a wrong causal graph does for CDT. The paper says that agent models should accurately portray the situation, and I add that the dependency structure needs the same care as the probabilities.

## 8. Conclusion

A-FDT, as defined in Equation (4), is expected-utility maximization in which the hypothetical for each action is built by surgery on the node for the decision function's output on its actual input. The surgery propagates through both causal and subjunctive dependence. With observations handled by switching the intervention node rather than by conditioning, it yields one-boxing, smoking, paying the driver, refusing blackmail, and staying in Damascus. Its main limitation, which the paper states plainly, is that it presupposes a dependency graph that no one yet knows how to derive in general. A reader applying it must therefore supply that graph and judge it as carefully as the probabilities.