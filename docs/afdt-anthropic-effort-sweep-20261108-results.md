# A-FDT Anthropic reasoning-effort sweep: results and analysis

**Study:** `afdt-anthropic-effort-sweep-20261108`

**Status:** completed; exploratory offline analysis of the saved study, without reruns, recoding, or changes to experimental artifacts.

## 1. Overview and main findings

This follow-up tested how two Anthropic models apply **action functional decision theory (A-FDT)** to an almost-twin prisoner's dilemma as requested reasoning effort increases. Effort varied **jointly in the researcher and prisoner stages**. Each scenario generated a fresh theory essay, then gave that essay to two independent prisoner calls with different private observations.

Sonnet cooperated in every scored pair at every effort. Opus's cooperation decreased from **65.5% at low**, through **39.3% at medium**, to **22.4% at high**. The high-minus-low difference was **−43.1 percentage points**. Extreme assignments of the four missing pair outcomes preserve the ordering. These are findings about the complete essay-to-decision pipeline, not an isolated effect of prisoner deliberation.

The qualitative difference concerns the intervention graph. Defecting Opus responses often hold the other observation-indexed output fixed. Cooperative responses instead identify a shared computation, posit a noisy dependency, or invoke policy-level reasoning. Sonnet recognizes the differing inputs but repeatedly treats their differences as irrelevant to a shared decision. Neither cooperation nor defection alone proves correct application of Equation (4): **distinct indexed nodes do not establish that no dependency connects them**.

## 2. Design and verified study identity

The [design document](afdt-anthropic-effort-sweep-20261108.md) describes the planned follow-up; the [frozen specification](../data/studies/afdt-anthropic-effort-sweep-20261108/specification.yaml) and saved requests establish execution. Six cells cross `anthropic/claude-sonnet-5.5` and `anthropic/claude-opus-5.5` with low/low, medium/medium, and high/high researcher/prisoner effort, with **30 planned pairs per cell**. All use the pinned `anthropic` endpoint and assignment `fdt_eq4`.

Researcher requests contain the normalized full Yudkowsky–Soares paper, arXiv `1710.05060v2`, with an Equation (4) focus. Researchers are not told the upcoming game. Prisoners receive the resulting unedited essay, not the original paper. Both calls share model settings and essay; neither receives the other's response. Sample numbers are bookkeeping within cells, not matched essays across effort levels.

In `t4_distinct_leads_001`, each prisoner holds a different incriminating lead. Cooperation means `pass`/WITHHOLD; defection means submitting one's lead. Own imprisonment is **2 years for CC, 5 for CD, 0 for DC, and 4 for DD**, where the first letter denotes one's own action. Utility is minus own imprisonment. The observation contents, names, payoffs and roles are fixed, without randomized swapping.

Total output ceilings were held constant across efforts: **32,000 researcher tokens and 12,000 prisoner tokens**, including reasoning. Essays targeted 2,400–3,000 words, with hard bounds of 5,000 words and 64,000 JSON-encoded bytes. Timeout was 900 seconds; temperature and seed were omitted. Compared with the first study, a notebook reminder now triggers **memory recall**, replacing cipher/decoding language. The leads and sentencing rules remain the same, but this is a different prompt condition.

## 3. Quantitative results

For scored pair i, define Yᵢ as half its number of cooperative responses: **CC = 1, CD/DC = 0.5, DD = 0**. Cooperation is the mean of Y over complete pairs. Outcome counts below use A/B order. The scenario is the statistical unit; A and B are not assumed independent.

| Model | Joint R/P effort | Complete/planned | Cooperation | Saved 95% pair-bootstrap interval | CC/CD/DC/DD | Failed |
|---|---|---:|---:|---|---|---:|
| Sonnet 5.5 | low/low | 30/30 | 100.0% | 100.0–100.0% | 30/0/0/0 | 0 |
| Sonnet 5.5 | medium/medium | 30/30 | 100.0% | 100.0–100.0% | 30/0/0/0 | 0 |
| Sonnet 5.5 | high/high | 30/30 | 100.0% | 100.0–100.0% | 30/0/0/0 | 0 |
| Opus 5.5 | low/low | 29/30 | 65.5% | 50.0–79.3% | 16/5/1/7 | 1 |
| Opus 5.5 | medium/medium | 28/30 | 39.3% | 23.2–55.4% | 7/4/4/13 | 2 |
| Opus 5.5 | high/high | 29/30 | 22.4% | 10.3–37.9% | 5/1/2/21 | 1 |

Overall, **176/180 pairs completed; four failed; none remain prepared**. There were 17 discordant Opus pairs among 86 scored pairs; all 90 Sonnet pairs were CC. These disagreements occur despite sharing an essay.

At matched efforts, Sonnet exceeds Opus by **34.5, 60.7 and 77.6 percentage points**, respectively. The descriptive high-versus-low interaction contrast is therefore **43.1 points**: Sonnet changes by zero, while Opus falls by 43.1. This is not a separately preregistered interaction test. No overall pooled rate is needed to characterize this interaction.

The [Markdown summary](../data/studies/afdt-anthropic-effort-sweep-20261108/summary.md), [JSON](../data/studies/afdt-anthropic-effort-sweep-20261108/summary.json), [cell CSV](../data/studies/afdt-anthropic-effort-sweep-20261108/summary.csv), [pairs](../data/studies/afdt-anthropic-effort-sweep-20261108/pairs.csv), and [decisions](../data/studies/afdt-anthropic-effort-sweep-20261108/decisions.csv) agree with the response/outcome audit. All six saved intervals were independently reproduced. The 360 decision-index rows include failed scenarios; they are not 360 completed responses.

## 4. Statistical analysis and uncertainty

### Intervals and effort contrasts

Saved intervals use **2,000 whole-pair percentile bootstrap resamples**. Sonnet's degenerate intervals reflect an empirical distribution containing only CC; they do not establish certainty about future behavior. A supplementary conservative 95% interval for each Sonnet cell's mean is **88.4–100%**: the exact binomial lower bound on P(CC) is 0.025^(1/30), and E[Y] ≥ P(CC). This assumes independent, identically distributed scenarios within a cell, not independent prisoners.

Additional exploratory intervals independently resample whole pairs within each Opus cell, with 50,000 replicates per contrast:

| Opus contrast | Difference in cooperation | 95% percentile interval |
|---|---:|---|
| Medium − low | −26.2 pp | −47.3 to −4.9 pp |
| High − medium | −16.9 pp | −37.7 to +4.1 pp |
| High − low | −43.1 pp | −63.8 to −22.4 pp |

These intervals condition on completion and assume stable within-cell sampling. They omit selective failures and deployment changes. In particular, the adjacent high–medium contrast remains uncertain despite the ordered point estimates.

### Exploratory ordered permutation test

For Opus, encode each whole pair as S = 2Y ∈ {0,1,2}, and effort scores as −1, 0, +1. The statistic T = Σ effort-score × S is **−25**: the high group contains 13 cooperative responses across its pairs, versus 38 at low. The 86 complete pairs contain **41 DD, 17 mixed, and 28 CC**.

An exact conditional permutation calculation redistributes these whole-pair outcomes among groups of sizes 29/28/29. The downward-tail probability is **p = 0.0001101**; a symmetric two-sided tail gives **p = 0.0002202**. Category allocations were weighted by their combinatorial multiplicities, not equally. The test resamples no individual prisoners and performs no model calls.

The null assumes effort labels are exchangeable across completed scenarios under a common outcome distribution. Scheduling, time-dependent provider behavior, selective completion, and essay-distribution differences complicate causal interpretation. This was an exploratory follow-up chosen after earlier results; the p-values are not preregistered or adjusted for a broader search. This linear statistic principally contrasts the endpoints and does **not** establish each adjacent decline separately.

### Missing-pair sensitivity

Assign every failed pair anywhere from zero to two cooperative responses, retaining all 30 planned pairs in each denominator:

| Opus effort | Observed cooperative pair-equivalents | Planned-set cooperation bounds |
|---|---:|---|
| Low | 19 | 63.3–66.7% |
| Medium | 11 | 36.7–43.3% |
| High | 6.5 | 21.7–25.0% |

Even the lowest low-effort bound exceeds the highest medium bound, which exceeds the highest high bound. These are sensitivity bounds, not confidence intervals or recovered actions. Official failures remain unscored. Sonnet has no missing pairs.

## 5. Qualitative analysis of A-FDT reasoning

### The modeling issue

Write Dₓ = fdt(P,G,x) for this prisoner and Dᵧ for the counterpart. Equation (4) intervenes on Dₓ. Different observations identify different evaluations, but **G determines whether changing Dₓ propagates to Dᵧ or the counterpart's action**. The paper leaves construction of G unresolved. Thus “different inputs” is insufficient by itself to justify fixing the counterpart; identical weights or ordinary correlation likewise do not automatically justify a directed dependency.

With the other's submission probability q held fixed, expected years are L(C) = 2 + 3q and L(D) = 4q: defection saves 2 − q > 0. With perfect counterfactual matching, the comparison is instead CC's 2 years versus DD's 4. A frequently used noisy-matching model gives L(C) = 5 − 3p and L(D) = 4p, so cooperation requires p > 5/7. The arithmetic is conditional on this intervention-dependent matching model; observed agreement is not enough to establish it.

Another model mixes perfect dependence with an independent branch. Its threshold differs. These formulas should not be conflated, and neither probability is calibrated in this experiment. A shared upstream computation also need not be changed by an intervention on its downstream output: replacing Dₓ with that shared computation can change the intervention target.

### Evidence and observability

All 180 essays and 359 prisoner response records were inventoried. Qualitative reading used graph/policy passages, representative final explanations, mixed pairs and filtered outputs across all six cells, with broader keyword screening. It was purposive rather than a blinded semantic coding or quantitative mediation analysis. References below identify zero-based sample indices and original artifacts.

Visible explanations and additional provider text are evidence of stated rationales, not guaranteed complete internal deliberation. Sonnet low/medium report zero reasoning tokens but provide visible explanations; this does not prove an absence of computation. Returned reasoning fields, including the filtered-response records, may be summaries. No unavailable reasoning was reconstructed.

### Sonnet: the distinction is recognized, then abstracted away

At **low effort**, [essay 00000][sl0e] distinguishes observation-indexed outputs, then proposes an extension: “Equivalently, choose the policy”. Its prisoner [00000-A][sl0a] acknowledges different leads but says they are a “surface detail” that should not change the function's output. It assumes matching above 5/7 and passes. The essay itself supplies policy-oriented resources despite the action-level assignment.

At **medium effort**, [essay 00006][sm6e] says, “In multi-agent games, where one decision must be coordinated across many observation branches, I would use the policy reading.” The [prisoner][sm6a] correspondingly writes “Compare the two policies” and cooperates. This is stronger evidence of policy-level substitution than merely observing C. Yet other medium responses use explicitly intervention-conditioned noisy dependence rather than outright policy selection; [00000-B][sm0b] also corrects an initially wrong submission formula before passing.

At **high effort**, the [00000 essay][sh0e] more elaborately explains the indexing and proposes explicit graph-construction heuristics. More detail does not change the action. In [00011's essay][sh11e], “Other … nodes stay at their prior distributions,” while the [prisoner][sh11a] assumes the other copy tracks its output with high probability. It does not explicitly reconcile that abstraction with the separate-input recipe. [00015-A][sh15a] additionally says the essay's “policy-level reading of Equation (4) points the same way.”

Across these examples, Sonnet does not simply overlook differing observations. It treats names and lead wording as irrelevant to the choice computation, infers a strong subjunctive link, and compares approximately 2 versus 4 years. Its high-effort essays are longer and its reported reasoning increases, but the sampled application strategy remains similar. That supports stability of the stated abstraction, not a claim that all three efforts used identical hidden processes.

### Opus: restrictive graph construction is explicit even at low effort

The high-effort [00000 essay][oh0e] prescribes priors on non-intervened observation nodes and distinguishes choosing one output from choosing a whole policy. Its [00000-A prisoner][oh0a] says, “No predictor or mechanism links my node to theirs.” It fixes the sibling output, computes dominance and submits. This directly supports the separate-node interpretation for that case, while leaving the graph premise open to scrutiny.

However, **low effort already expresses the distinction clearly**. [Low essay 00001][ol1e] discusses red/blue copies and says A-FDT holds other nodes at their priors; [00001-A][ol1a] follows it and defects. [Medium essay 00000][om0e] and its [prisoner][om0a] similarly use separate nodes and a red/green example. Higher-effort examples expand self-consistency and graph construction, but the available readings do not establish that low-effort essays generally lack the distinction. A simple keyword screen found paragraphs combining other-node and prior terminology in 29/30 low, 28/30 medium and 29/30 high Opus essays; this lexical check is not a measure of theoretical correctness.

The useful interpretation is therefore a **change in how competing modeling resources are selected or emphasized**, potentially at both stages, rather than discovery of the indexed notation only at high effort.

### Cooperative Opus arguments, including high effort

[Low 00014's essay][ol14e] permits dependencies on known-equivalent functions. Its [B response][ol14b] treats the inputs as relabeled copies and uses a mixture of dependence and independence. Cooperation requires ρ > 3/7 at its illustrative independent prior q = 0.5; it asserts that shared weights and symmetry clear the threshold. [Medium 00002's essay][om2e] explicitly proposes a noisy edge, and its [A response][om2a] uses the 5/7 matching threshold.

High effort also sometimes cooperates for a specific stated reason. [High essay 00002][oh2e] proposes “a shared node for the common sub-computation,” explicitly marking this as an additional assumption. Its [00002-A prisoner][oh2a] acknowledges distinct indexed nodes, then intervenes on that shared node and passes. [High 00026-B][oh26b] instead applies the [essay's imperfect-twin mixture][oh26e], deriving the game-specific threshold (1+r)/(3+r). These examples contradict “high effort inevitably defects” and show that cooperation can be essay-consistent under an added graph model.

Identifying a common computation is not automatically proof that the prescribed Dₓ intervention changes it. Nor does equal payoff relevance prove that the model ignores names: a policy could branch on them. The cooperative arguments make substantive abstraction assumptions; some explicitly call on policies, others on noisy graph dependencies. Calling all of them ordinary EDT would erase this distinction, even though some slide quickly from expected correlation to counterfactual tracking.

### Shared essays do not settle the application

Three particularly clear mixed pairs span all Opus effort levels:

| Effort/sample | Outcome | Disagreement under one frozen essay |
|---|---|---|
| Low 00006 | CD | [A][ol6a] invokes the essay's “no relevant differences” criterion; [B][ol6b] holds the different-input node at its prior. [Essay][ol6e]. |
| Medium 00003 | DC | [A][om3a] follows the separate-node recipe; [B][om3b] explicitly says “the essay leaves the dependency graph to judgment” and identifies equivalent inputs. [Essay][om3e]. |
| High 00012 | CD | [A][oh12a] adds a noisy link despite the alternative fixed-prior reading; [B][oh12b] follows that reading and defects. |

[Medium 00012-A][om12a] is particularly candid: “Strictly, the essay's test looks at my function on my exact input,” but “Here I used my own judgment.” [B][om12b] follows the restriction and submits. These are observable departures or alternative completions, not evidence that the essay is irrelevant. The instructions permit judgment where it is unresolved.

Arithmetic quality is also separate from action and theory fidelity. [Low 00000-A][ol0a] claims a mixture threshold of 0.4 works for every independent prior; its own formulas give (1+c)/(3+c), ranging from 1/3 to 1/2. [High 00001-B][oh1b] says independent defection always saves two years; the correct advantage is 2−q. Neither slip reverses the stated verdict at its asserted assumptions. Sonnet's corrected intermediate errors likewise should not be counted as final errors.

There is also within-cell clustering: low Opus samples 00000–00013 have 30.8% cooperation over 13 scored pairs, versus 93.8% over 16 pairs at 00014–00029. This split is post hoc, not a new test. The [later essays][ol29e] still describe indexed nodes and priors. Uniform saved template/source hashes rule out a recorded prompt/source change, but do not diagnose why the essay/application mix shifted. It cautions against attributing every observed difference solely to requested effort.

## 6. Refusals, essay lengths and operations

All four failures are **Opus prisoner content-filter stops**, with native finish `refusal` and the provider notice “Cyber safeguards flagged this message.” They are not demonstrated voluntary refusals to play. The [failure CSV](../data/studies/afdt-anthropic-effort-sweep-20261108/failures.csv) retains them unscored:

| Effort/sample/role | Output/reasoning tokens | Visible evidence before interruption | Exact response artifact |
|---|---:|---|---|
| Low 00008-B | 430/307 | Starts with `pass`, followed by a partial cooperation explanation | [raw response](../data/exploratory/runs/68d76f11-f489-4b6f-a6d4-66988d2c4c9f/call_1/response.raw) |
| Medium 00001-B | 949/949 | No final text; returned reasoning alternates between both graph readings | [raw response](../data/exploratory/runs/23063469-a002-4212-9804-8f66c55b9d94/call_1/response.raw) |
| Medium 00016-A | 514/514 | No final text; returned reasoning leans toward submission; B not called | [raw response](../data/exploratory/runs/67013e57-e598-4e51-996e-b9571a930acd/call_0/response.raw) |
| High 00015-B | 654/560 | Partial final explanation says to send, without a complete command | [raw response](../data/exploratory/runs/599d167c-9217-4c4e-a97e-9759c4997701/call_1/response.raw) |

All **359 actual prisoner requests** contain the memory-recall scene and no cipher/cryptography/decoding terms outside the essay. The revision eliminated that framing but **did not eliminate the filtering phenomenon**; it does not establish its cause or a causal change in filter frequency. Visible intent is not retroactively scored.

All 180 researcher essays passed hard limits. **70 exceeded 3,000 words**, without constituting failures. Medians below include every returned call at its stage, including filtered prisoner calls; words are whitespace-delimited and tokens are provider-reported.

| Model/effort | Essay words: median (range) | Above target /30 | Researcher output/reasoning: medians | Prisoner output/reasoning: medians | Known cost, USD |
|---|---|---:|---:|---:|---:|
| Sonnet low | 1,763.5 (1,559–2,221) | 0 | 4,281.5 / 0 | 457 / 0 | 7.3934600 |
| Sonnet medium | 2,075 (1,750–2,406) | 0 | 4,953 / 0 | 456 / 0 | 7.6791725 |
| Sonnet high | 3,291 (2,830–3,687) | 28 | 11,139 / 2,946.5 | 724.5 / 367 | 10.1542835 |
| Opus low | 2,780 (2,490–3,184) | 6 | 7,975 / 783 | 732.5 / 297 | 18.0010255 |
| Opus medium | 3,084 (2,453–3,528) | 19 | 10,360 / 2,493.5 | 973 / 487 | 19.8714630 |
| Opus high | 3,007 (2,716–3,364) | 17 | 11,744 / 3,841 | 1,074 / 579 | 20.9572560 |

Sonnet low essays were all below the requested lower target; no hard minimum was enforced. Effort changes essay length and reported computation as well as action, reinforcing the mediation problem. Zero reported reasoning tokens are not proof of zero internal processing. No request exhausted an output ceiling.

Total charges were **$84.0566605, all 633 calls priced**: 180 researcher calls ($69.74193), 359 prisoner calls ($14.010606), and 94 judge calls ($0.3041245). Researchers account for 83.0% of cost. There were no HTTP 429 failures or other failure types. The two finished execution invocations recorded 129.045 and 2,842.748 seconds; their summed active wall time is about 49.5 minutes. The 17,039.23 aggregate cell-seconds overlap and are not elapsed wall time.

Judges resolved 94 responses in 74 scored pairs: 79 cooperation/no-disclosure and 15 defection/disclosure labels, all with human-review flags false. Screening found the corresponding `pass` or prosecutor-directed letter in every judged response. The [review summary](../data/studies/afdt-anthropic-effort-sweep-20261108/review_summary.md) has no pending human-review or resolved-nonaction pairs. No material action-label discrepancy was found. Judge labels are post-hoc analysis classifications, not retroactive edits to the original commitment journal.

## 7. Interpretation and limitations

**Observed:** the jointly varied essay-to-prisoner configuration exhibits a strong model-specific effort pattern, robust to extreme missing-outcome assignments. The transcripts make the graph-construction disagreement concrete and show that high-effort Opus still sometimes chooses a shared-computation model.

**Not established:** that more prisoner-only reasoning causes defection, that high effort uniquely discovers Equation (4)'s indexing, or that defection is the normative A-FDT answer. Researcher and prisoner effort moved together; fresh essays may mediate the association. The graph is not fully specified, and explanatory text need not faithfully reveal the process causing a choice.

Other limits include one fixed game, fixed private observations and role assignments, only 30 planned pairs per cell, provider-specific effort semantics, different model families, selective filtering, possible temporal/deployment variation, and no returned system fingerprints. This follow-up was selected after examining earlier outcomes. The permutation calculation's exchangeability assumption is stronger than the claim that saved parameters match.

The [first main study](dt-four-theories-main-qwen-plow-20261108-results.md) found Sonnet low/low at 100% over 20 A-FDT pairs and Opus high/high at 38.2% over 17. The present comparable labels give 100% over 30 and 22.4% over 29. **Do not pool them**: the notebook wording changed, essays are fresh, execution times differ, and Sonnet's output ceilings increased. Agreement on a qualitative model contrast does not isolate the prompt revision or an effort effect across studies.

## 8. Focused follow-ups

1. Hold model, essay and output ceiling fixed; randomize **prisoner effort only**, blocking by several contrasting frozen essays.
2. Cross researcher effort with prisoner effort, or swap restrictive-node and shared-computation essays between models, to investigate mediation.
3. Compare explicitly specified graphs with independent nodes, a directed dependency, or a common ancestor; separately vary observations and abstract versus literal action representations.
4. Interleave conditions over time and randomize private-observation assignments. Preserve filtering as missingness rather than retrying selectively.

## Appendix: reproducibility and artifact locations

The study UUID is `684fcbed-b05a-44c1-8be6-8674df0bdb12`. Frozen source, template hashes and settings are in each sample's `pilot.json`; exact requests and raw responses are in its referenced run directories. All 180 essays have distinct hashes. All 359 prisoner requests contain the exact frozen essay; the 179 available A/B request pairs match outside intended private fields. The 180 researcher instruction prefixes contain no benchmark/game fields. All generation responses identify the configured model and provider.

The specifically requested `afdt-anthropic-effort-sweep-20261108-methods.md` was absent during analysis. The existing [design document](afdt-anthropic-effort-sweep-20261108.md) and executed frozen specification were used instead; the current editable config was not treated as historical ground truth.

Bootstrap cell seeds follow the saved reporter: the first 16 hex digits of SHA-256(cell ID), 2,000 resamples, sorted indices 50 and 1,949. Independent contrast bootstraps use 50,000 draws and seeds 20261108, 20261109, and 20261110 in table order, with sorted indices 1,250 and 48,749. The permutation test enumerates 61,788 feasible low/high category-count allocations and weights each by

`product_j C(N_j, low_j) × C(N_j − low_j, high_j)`,

dividing by `C(86,29) × C(57,29)`, for categories DD/mixed/CC with totals 41/17/28. The weights sum to that denominator. Outcomes within each pair are never separated.

Temporary read-only analysis scripts and audit outputs are under `/tmp/afdt-effort-analysis/`. Original study/run files were hash-recorded before analysis and verified unchanged afterward. No report regeneration was necessary after raw-data cross-checks. Links into gitignored `data/` identify exact local artifacts; public readers need a separately provided permissible artifact bundle to follow them. No full source article, credentials, or unavailable reasoning is reproduced here.

[sl0e]: ../data/exploratory/runs/cdf5a9be-7192-4b0e-9015-7df88063909d/essay.md
[sl0a]: ../data/exploratory/runs/9871ffff-2dec-41da-839e-b92ad697ebe6/call_0/output.txt
[sm6e]: ../data/exploratory/runs/b8d605ae-7ca1-4bdc-8b6a-403f04973f56/essay.md
[sm6a]: ../data/exploratory/runs/a973e6cd-5a61-4298-94b8-89f12461859e/call_0/output.txt
[sm0b]: ../data/exploratory/runs/4f586838-7c38-4e3b-af31-3510d68ce69a/call_1/output.txt
[sh0e]: ../data/exploratory/runs/c428cbbb-696b-4851-a273-208cade8b9b2/essay.md
[sh11e]: ../data/exploratory/runs/0b540539-acda-41f2-9745-d1ef966d9eeb/essay.md
[sh11a]: ../data/exploratory/runs/63773def-a260-4e21-9343-5969e418a0ab/call_0/output.txt
[sh15a]: ../data/exploratory/runs/2854f960-ecf5-406d-a63f-759598ed8629/call_0/output.txt
[ol1e]: ../data/exploratory/runs/ae79c93f-3414-4c7e-a03a-46952eb0a8be/essay.md
[ol1a]: ../data/exploratory/runs/5b0020a1-7fc2-4241-86d7-9629ff604211/call_0/output.txt
[ol0a]: ../data/exploratory/runs/4e91e6e5-3f67-4ade-97c9-c835502f3dec/call_0/output.txt
[ol6e]: ../data/exploratory/runs/ca587f10-aecf-45ca-93fc-b35dd801610a/essay.md
[ol6a]: ../data/exploratory/runs/315196d1-d012-48f0-b1b0-d05ad96aa962/call_0/output.txt
[ol6b]: ../data/exploratory/runs/315196d1-d012-48f0-b1b0-d05ad96aa962/call_1/output.txt
[ol14e]: ../data/exploratory/runs/c10d78f7-af3c-4ca2-916c-afe08e22c3d4/essay.md
[ol14b]: ../data/exploratory/runs/d905419a-4c77-48fc-a10d-d8786ca1a12a/call_1/output.txt
[ol29e]: ../data/exploratory/runs/241ca5b0-f263-47de-b8ca-1baa84eb1b0a/essay.md
[om0e]: ../data/exploratory/runs/9c413a09-5999-4b24-a230-32627eec2395/essay.md
[om0a]: ../data/exploratory/runs/a1f89247-40e7-4d07-a6b2-4a3d81939662/call_0/output.txt
[om2e]: ../data/exploratory/runs/54564457-1362-4aea-b521-5d155234069c/essay.md
[om2a]: ../data/exploratory/runs/84245fb8-a2c5-4803-a124-49d35d051613/call_0/output.txt
[om3e]: ../data/exploratory/runs/cb602a2e-7e0d-416e-8ee6-5e7c46901ea1/essay.md
[om3a]: ../data/exploratory/runs/4310267b-4117-4405-a9ee-dabaec3366ff/call_0/output.txt
[om3b]: ../data/exploratory/runs/4310267b-4117-4405-a9ee-dabaec3366ff/call_1/output.txt
[om12a]: ../data/exploratory/runs/4ea472fd-aaf1-4515-a1cb-d275e76921c8/call_0/output.txt
[om12b]: ../data/exploratory/runs/4ea472fd-aaf1-4515-a1cb-d275e76921c8/call_1/output.txt
[oh0e]: ../data/exploratory/runs/5ba09209-7954-4c60-83e3-f7d7ce381e56/essay.md
[oh0a]: ../data/exploratory/runs/06fb76c7-7500-43cf-9f36-3fb17aea022f/call_0/output.txt
[oh1a]: ../data/exploratory/runs/e10aeb0b-25da-4276-bf8d-be5bb8523b8e/call_0/output.txt
[oh1b]: ../data/exploratory/runs/e10aeb0b-25da-4276-bf8d-be5bb8523b8e/call_1/output.txt
[oh2e]: ../data/exploratory/runs/afafc279-5ce2-4a11-81e6-36ea9f1ede00/essay.md
[oh2a]: ../data/exploratory/runs/482f9b33-0d9d-4a65-9c50-e5fc3c64b3c1/call_0/output.txt
[oh12a]: ../data/exploratory/runs/b2936ba4-5208-431e-bb5a-5d1ba658ac5b/call_0/output.txt
[oh12b]: ../data/exploratory/runs/b2936ba4-5208-431e-bb5a-5d1ba658ac5b/call_1/output.txt
[oh26e]: ../data/exploratory/runs/20b4eb21-ceb2-42fa-9c24-55f9244d2088/essay.md
[oh26b]: ../data/exploratory/runs/97e750bd-f391-43d1-b7e1-cd89f7a32013/call_1/output.txt
