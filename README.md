# Almost-Twin Prisoner's Dilemma: decision-theory experiments

How do language models apply different decision theories when facing another copy of their own algorithm with different private observations?

This research project tests **causal decision theory (CDT)**, **evidential decision theory (EDT)**, **action functional decision theory (A-FDT)** and **policy functional decision theory (P-FDT)**. A researcher model first writes an essay from a human-written reference article, without being told about the upcoming game. Two independent prisoner calls then receive the same frozen essay and game, with different private observations. Each chooses whether to submit evidence about the other prisoner, seeking to minimize its own imprisonment.

The repository contains the experiment harness, methods, results, and a curated dataset of **820 paired scenarios**, including failures and unexecuted scenarios. Both studies are exploratory. Their results describe these particular model/source/prompt configurations; they do not establish what a decision theory normatively prescribes.

## Studies and results

| Study | Design | Methods | Results and analysis | Browse scenarios |
|---|---|---|---|---|
| **Four-theory main study** | Eight models × four theories × 20 planned pairs; 640 scenarios | [Methods](docs/first_study_design.md) | [Full results](docs/dt-four-theories-main-qwen-plow-20261108-results.md) | [640 records](published/studies/dt-four-theories-main-qwen-plow-20261108/README.md) |
| **Anthropic A-FDT effort sweep** | Sonnet 5.5 and Opus 5.5 × three joint researcher/prisoner effort levels × 30 planned pairs; 180 scenarios | [Methods](docs/afdt-anthropic-effort-sweep-20261108-methods.md) | [Full results](docs/afdt-anthropic-effort-sweep-20261108-results.md) | [180 records](published/studies/afdt-anthropic-effort-sweep-20261108/README.md) |

In the main study, CDT generally led to defection, EDT generally to cooperation, and P-FDT to cooperation in every complete pair. A-FDT produced substantial disagreement between models. The results document examines how they interpret an intervention on a decision-function output indexed by the agent's observations, including whether it also changes the other prisoner's output.

In the follow-up, Sonnet cooperated in all 90 complete pairs. Opus's cooperation rates were **65.5%, 39.3%, and 22.4%** at low, medium, and high effort, respectively, among 29, 28, and 29 complete pairs. Researcher and prisoner effort varied together, and every scenario generated a fresh essay, so this does not isolate the effect of prisoner reasoning. Strong chronological clustering within low-effort Opus is an additional caution discussed in the report.

| Study | Complete/scored pairs | Failed pairs | Prepared, unexecuted | Planned |
|---|---:|---:|---:|---:|
| Main study | 543 | 87 | 10 | 640 |
| Effort sweep | 176 | 4 | 0 | 180 |
| **Total** | **719** | **91** | **10** | **820** |

Cooperation means **WITHHOLD** (`pass`); defection means **SUBMIT** the evidence. A pair contributes 1 for CC, 0.5 for CD/DC, and 0 for DD. Rates use complete paired scenarios, without assuming the two prisoners are independent. Failure, refusal and nonexecution are separate dispositions, never recoded as defection. The remaining ten Gemini Argon scenarios were intentionally left unexecuted.

## Browse the evidence

Start with the [dataset guide](published/README.md) or either study's scenario index above. Each row identifies a model/theory/effort cell, a zero-based sample number, its status and outcome, and a **Read** link to a complete readable transcript.

1. Open `transcript.md` to read the researcher essay, both returned prisoner responses, available readable reasoning, and judge output where applicable. [Example: low-effort Opus A-FDT, sample 00000](published/studies/afdt-anthropic-effort-sweep-20261108/batches/003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow/samples/00000/transcript.md).
2. Follow its request/response links for the saved API artifacts. `response.raw`, accepted `essay.md`, visible `output.txt`, and prisoner/judge `request.json` preserve original bytes. Readable reasoning may be a provider summary; missing or encrypted reasoning is not reconstructed.
3. Open the adjacent `record.json` for structured scenario metadata and artifact paths. Each study also has a machine-readable `index.json` and a `reference/` directory with summaries, pair/decision CSVs, failures, review dispositions and the frozen specification.

All 820 scenarios have records, including the 91 failures and ten unexecuted scenarios. Missing responses remain missing. Judge classifications remain distinguishable from the prisoners' original commitments.

**Researcher requests are source-omitted derivative views**, clearly named `request.source_omitted.json`; they are not exact original requests. The FDT paper/TeX and full source-bearing researcher requests are excluded. Attributed Wikipedia reference articles are included once each. [Publication policy](docs/publication.md) explains every transformation and omission; `published/MANIFEST.json` records hashes and derivations. Large JSON files are easiest to inspect after cloning or downloading the repository.

## Reproduce the reported outcomes offline

Clone the repository, then verify with **Python 3.11+**:

```sh
git clone https://github.com/jessica-taylor/almost-twin-pd-eval.git
cd almost-twin-pd-eval
python3 scripts/verify_publication.py published
```

This independent, standard-library-only verifier needs **no installation, API key, network or model calls**. It verifies the export's hashes, reconstructs all 38 cells' outcome counts and cooperation rates, reproduces the saved whole-pair bootstrap intervals, and checks failures, essay sharing, usage and costs against the saved reports. See [reproducibility instructions](docs/reproducibility.md) for its scope, programmatic browsing, and rebuilding the export when private originals are available.

## Use or develop the harness

To install the small Python CLI and run its offline tests:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
python3 -m unittest discover -s tests
python3 -m almost_twin --help
```

Installing dependencies may access a package index; tests do not generate model calls. For new experiments, use the [two-stage pilot guide](docs/pilot_workflow.md), [batch guide](docs/batch_workflow.md), or [study guide](docs/study_workflow.md), and read the [Wikipedia source instructions](docs/wikipedia_sources.md). Generation requires an OpenRouter key and explicit billing flags. Prepare new output directories; the completed studies should remain frozen.

Current editable [prompts](prompts/), [configurations](configs/), and the [source manifest](sources/manifest.yaml) support future work. Historical execution is established by each published study's frozen specification and saved requests, rather than assuming today's templates are identical. A new model run is not guaranteed to reproduce the saved outputs or provider behavior.

## Licenses and attribution

The software, prompt templates, configurations and software documentation are available under the [MIT License](LICENSE). Project-authored research reports and the project's rights in the curated research data are offered under [CC BY 4.0, with explicit third-party exceptions](DATA_LICENSE.md). The bundled Wikipedia articles retain **CC BY-SA 4.0**, contributor attribution and revision notices. No license is granted on behalf of paper authors or model providers, and no copyright is claimed over material that has none.

When using the results or dataset, credit **Almost-Twin PD Eval contributors**, link this repository and the relevant methods/results document, identify the study and repository commit, and describe any changes. Preserve source-specific notices when redistributing source material. See [data redistribution terms](DATA_LICENSE.md) and the [publication audit](docs/publication.md).
