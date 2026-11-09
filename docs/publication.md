# Curated study export and publication audit

The two frozen studies are exported under [`published/`](../published/README.md). This commit prepares a reviewable local dataset; it does **not** push data, publish a release, or change GitHub visibility.

## Reproduce and verify offline

From the repository root:

```sh
python3 -m almost_twin export-publication --out published
python3 scripts/verify_publication.py published
```

If private originals are available:

```sh
python3 scripts/verify_publication.py published --source-root .
```

The exporter reads the original frozen study/batch/pilot manifests and saved artifacts. It does not use current model choices, prompts, source-cache `current.json` pointers, approvals or budgets to reconstruct historical conditions. It makes no network or model requests. Optional `--study PATH` flags select explicit study directories; the default is the two completed studies.

Output bytes are deterministic: no export-time timestamp, absolute checkout location, Git HEAD, random ID or filesystem mtime is introduced. Identical exports are accepted without overwriting. A different existing export is refused; use a new output directory for a revised publication version. Temporary staging is cleaned up on failure. Original study files are never edited.

The full second export matched all **19,493 files byte-for-byte**. All **57,880 original study/run files** checked remained unchanged, and more than 6,100 generated/report navigation links resolved. These checks are recorded in [`publication-reproducibility.json`](publication-reproducibility.json). The curated tree is approximately 191 MiB including its full provenance ledger. `.gitattributes` disables text/EOL conversion, clean/smudge filters and identifier expansion for `published/`; staged Git blobs are checked against the exported bytes before committing.

## Roster and scope

| Study | Complete | Failed | Prepared/unexecuted | Total |
|---|---:|---:|---:|---:|
| First main four-theory study | 543 | 87 | 10 | 640 |
| Anthropic A-FDT effort sweep | 176 | 4 | 0 | 180 |
| Total | 719 | 91 | 10 | 820 |

Each scenario has a public record and a readable transcript, including scenarios with no calls. The export includes all 2,566 saved API response bodies and accounts for all 2,569 attempted calls; the three attempts without responses/prices remain explicitly unknown. Accepted essays, partial/failed researcher outputs, prisoner responses, judge responses, original classifications, adjudications, frozen settings, source identities, prompt hashes and timing/cost metadata are retained. Generated indices distinguish unexecuted, failed and scored scenarios.

## Evidence-preservation rules

`published/MANIFEST.json` is the transformation ledger. Every payload has a SHA-256, byte count, evidence designation, source-file hashes and operations. Its input inventory also hashes intentionally omitted originals, such as complete researcher requests. Original filenames are repository-relative; actual local home directories are not disclosed.

- **Verbatim evidence:** raw API response bytes, visible output files, accepted essay bytes, and prisoner/judge request bytes. No line-ending normalization, action recoding, truncation, essay rewriting, guessed output or decrypted reasoning is performed.
- **Researcher input views:** `request.source_omitted.json` is explicitly a derivative, never labeled an exact request. Only the contents of the single `<source_document>` block are replaced by a conspicuous source descriptor/hash marker. The original request hash, omitted-body hash, UTF-8 byte span, replacement and JSON-reserialization operation are logged. All other request fields/instructions survive. The exact original request is not bundled.
- **Metadata paths:** local repository-root strings are replaced by portable `runs/`, `studies/` or `<LOCAL_REPOSITORY>` paths. Each changed structured field has a JSON pointer (or CSV row/column pointer), original-value hash and replacement. Serialization changes are explicit. Source-root verification rejects undeclared structured changes.
- **Transport metadata:** HTTP status, date, server, API-release header and three-letter ingress suffix are retained where saved. Response cookies, full connection trace IDs and other headers are omitted. The ledger lists omitted header names and the original transport-file hash, without exposing their values.
- **Readable transcripts:** generated from the raw response JSON, with complete visible content inside safe fences. Readable reasoning prefers the saved `reasoning` string, then `reasoning_content`, then the ordered `reasoning.summary`/`reasoning.text` blocks. Joining those blocks and any wrapper separator newline are documented derivations. These views may contain provider summaries; they are not claims to complete internal traces. Encrypted fields remain untouched in raw JSON and are never decoded.
- **Original metadata digests:** a redacted metadata view may have a different hash from its private original. `study.original.sha256` refers to the original frozen study file; the ledger supplies the public file's hash. This distinction is deliberate.

Duplicate rendered prompts, cache trees, capability snapshots, locks, local environment files, transport cookies and project-wide budget/approval journals are not published. No additional source-text redaction is applied to model-generated essays or responses, even when they quote or discuss the human reference. This preserves experimental evidence rather than silently repairing it.

Generated navigation links are checked separately from model-authored text. Mathematical notation, footnotes, model-written URLs and any errors in the essays are retained as evidence, without automatic link repair.

## Wikipedia and the FDT paper

The exact normalized Wikipedia articles used in the main study are included **once each**, selected by both article hash and provenance hash, with their original contributor attribution, permanent revision, history link, CC BY-SA 4.0 license link, conversion notice and qualifications for third-party content/media. No external media bytes are included. Extraction/download provenance is included as metadata. The Wikipedia license does not become a blanket license for all experimental artifacts.

The FDT normalized article, original paper, TeX and complete source-bearing researcher requests are **not** included. The source descriptor preserves the exact version and normalized/provenance hashes and points to:

- [Pinned v2 TeX source archive](https://arxiv.org/src/1710.05060v2)
- [Pinned paper/version page](https://arxiv.org/abs/1710.05060v2)
- [Pinned PDF](https://arxiv.org/pdf/1710.05060v2)

The source archive lets readers locate the TeX directly without implying redistribution rights. Original extraction metadata is retained where available. Rebuilding a researcher input requires obtaining the source and reproducing the recorded normalized hash; the public derivative is not a substitute input for a rerun. No permission or license is asserted on behalf of the paper's authors or model providers.

## Audit results and limits

The audit at Git HEAD `bcea2cdedfa8668016005ce2c5978def054c58cf` examines the 83 existing tracked worktree files, all 293 historical blobs and 106 commit/tag messages reachable from local refs/reflogs, plus the prospective additions. Results are recorded in [`publication-audit.json`](publication-audit.json), including remote-URL credential checks and nonignored new files. It performs no remote fetch and does not inspect unseen remote refs or server-side records.

No confirmed credentials, local-home/workstation identifiers or full reference-article copies were found in the pre-export tracked contents/history. Broader patterns do flag an explicitly mocked API-key fixture in `tests/test_study.py` (one current occurrence and nine historical blob versions), a fabricated cookie literal in `tests/test_publication.py`, and a URL-expression fixture in that same test. These are individually triaged by location and value hash in the audit report, with no blanket test-directory exemption and no values copied into the report. Raw scanner findings are retained. Authorized, attributed Wikipedia copies in the export are scoped exceptions to the article-copy rule.

Git author/committer metadata contains **two email identities that are not GitHub noreply addresses**. The report records address hashes rather than duplicating those addresses. They remain in Git history as contributor provenance. Before making the repository public, decide whether those identities are acceptable; no identity or history rewrite is authorized or performed by this export.

The export also has a deterministic [`SCAN.json`](../published/SCAN.json). It scans known credential formats, private-key markers, literal bearer tokens, local-home paths, workstation prompts, email addresses, cookie values and known full-source signatures. Wikipedia article exceptions apply only within `sources/`. Detected evidence is not automatically sanitized: a blocking match aborts export without changing the original. Findings identify locations and value hashes, never the credential values.

This is a documented heuristic audit, not proof of absence of every possible secret, personal detail or source quotation. No dedicated gitleaks/trufflehog installation was available. Encrypted provider reasoning cannot be content-scanned without decryption; it is retained as opaque original evidence. No blanket quotation-rights determination is made for model outputs.

## Independent numerical verification

[`scripts/verify_publication.py`](../scripts/verify_publication.py) uses only Python's standard library and imports neither the exporter nor the experiment's scoring/reporting functions. It checks file inventories/hashes, reconstructs dispositions from exported states and classifications, distinguishes judge labels from original commitments, recomputes payoff years/utilities and all 38 cell outcome distributions/cooperation rates, checks frozen essay sharing and private-field-only prompt differences, sums response-reported charges/tokens/call counts, reproduces saved whole-pair bootstrap intervals, and checks essay target metrics. With `--source-root`, it verifies original input hashes and checks declared source-span/path transformations against those originals.

The verifier also checks failure identities/types against available provider stops and hard essay limits, and reproduces the recorded execution-time fields from the event logs (allowing only floating-point summation noise). Results are recorded in [`publication-verification.json`](publication-verification.json). This checks faithful export and numerical reproduction, not philosophical correctness of a theory or an independent regrading of model intent. There are no new judge calls and no inferred actions for missing/filtered responses. The shared global commitment journal is outside this export's frozen-study scope; original per-pair enacted-action records remain distinct from post-hoc adjudications.
