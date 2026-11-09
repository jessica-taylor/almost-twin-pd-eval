# Reproduce and inspect the published results

There are three distinct tasks: verify the saved public evidence, rebuild its curated export from private originals, or run a new experiment. Only the last involves model generation. None of the verification/export commands below makes network or billable calls.

## 1. Verify a public checkout

Use Python 3.11+ from the repository root:

```sh
python3 scripts/verify_publication.py published
```

No package installation or credentials are required. The [independent verifier](../scripts/verify_publication.py) uses only the standard library and imports neither the exporter nor the harness's scoring/reporting code. It checks:

- Every manifested payload's byte count and SHA-256, plus the expected file inventory.
- All **820** scenario records: **719 complete, 91 failed, 10 prepared/unexecuted**.
- All **38 model/theory/effort cells**, reconstructing CC/CD/DC/DD counts and cooperation from whole paired scenarios, and reproducing the saved 2,000-resample pair-bootstrap intervals.
- Saved classifications, failure dispositions, payoff years, essay sharing, and prisoner-prompt differences limited to the private fields.
- **2,569 attempted calls**, **2,566 priced calls**, and provider-reported charges of **$104.656218715** for the main study and **$84.0566605** for the effort sweep. The three unpriced attempts remain unknown.
- Available token usage, essay target metrics, failure evidence, and recorded execution time from logs.

To save the verification result:

```sh
python3 scripts/verify_publication.py published --out /tmp/almost-twin-verification.json
```

This checks export fidelity and primary numerical results. It does not independently regrade every response's intent or establish a theory's normative correctness. The results reports describe additional exploratory comparisons, permutation tests and chronological analyses; those are not all automated by this verifier. See the [main-study appendix](dt-four-theories-main-qwen-plow-20261108-results.md#appendix-c-audit-and-artifact-accessibility) and [effort-sweep appendix](afdt-anthropic-effort-sweep-20261108-results.md#appendix-reproducibility-and-artifact-locations) for their procedures. Temporary analysis scripts mentioned there are historical local working files, not dependencies required for public verification.

## 2. Browse or reanalyze without the original machine

The [dataset guide](../published/README.md) links both study indices. For each study, `reference/summary.csv` contains cell summaries; `reference/pairs.csv` and `reference/decisions.csv` give scenario and response indices; `reference/failures.csv` and `reference/review_summary.md` explain missingness and adjudication.

For example, this standard-library snippet prints each main-study cell's saved summary:

```sh
python3 - <<'PY'
import csv
from pathlib import Path

path = Path("published/studies/dt-four-theories-main-qwen-plow-20261108/reference/summary.csv")
with path.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        print(row)
PY
```

Use whole A/B scenarios as the statistical unit. Keep failures and prepared records separate from scored outcomes; rates conditional on completion can be affected by nonrandom missingness. Do not pool the two studies as though they used identical prompts, effort settings or essay limits.

For close reading, open a sample's `transcript.md` and follow the links to `response.raw` and the saved request. The adjacent `record.json` links its essay/run artifacts and identifies the condition. Available readable reasoning may be a provider summary. Hidden/encrypted reasoning remains opaque. Source-omitted researcher requests cannot be used as exact generation inputs.

## 3. Rebuild the export, if private originals are available

Install the CLI dependencies (this installation may access a package index):

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
```

With the original `data/studies/`, referenced batches/pilots/runs, and matching source-cache provenance available in this checkout:

```sh
python3 -m almost_twin export-publication --out /tmp/almost-twin-export
python3 scripts/verify_publication.py /tmp/almost-twin-export --source-root .
```

Choose a fresh output directory. The exporter accepts an identical existing export but refuses to overwrite a different one. It selects the two frozen studies by default and reads their frozen metadata rather than current editable prompts/configurations or mutable cache pointers. The output introduces no export-time timestamp or checkout-specific path. The same inputs and exporter version produce identical bytes; a changed exporter may change provenance or generated notices even if the underlying evidence is unchanged.

`MANIFEST.json` documents each verbatim file, derivative, source hash and transformation. With `--source-root .`, verification additionally checks original input hashes and declared transformations against those originals. A public-only clone cannot perform that private-input check or reconstruct excluded full researcher requests. Fetching an article again is not guaranteed to reproduce a historical normalization; compare both source and provenance hashes before claiming exact reproduction.

See [publication policy](publication.md) for excluded source texts, transport-header omissions, local-path substitutions and the audit's limits. Original study artifacts are never modified by export or verification.

## 4. New experiments are separate runs

The [pilot](pilot_workflow.md), [batch](batch_workflow.md) and [study](study_workflow.md) guides explain preparation, spending controls and explicitly authorized execution. Use a new output directory and preserve the completed studies. Current configuration and template files may have evolved; the published frozen specifications and saved historical requests establish what ran.

Provider availability, versions, routing and stochastic generation can change. A new run can test the same design without reproducing identical responses. No API key is needed to inspect or verify the existing dataset.
