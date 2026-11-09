# Curated Almost-Twin study data

This is an offline export of frozen experimental artifacts, including failures and prepared/unexecuted scenarios. No model generations, retries or recoding were performed.

- [afdt-anthropic-effort-sweep-20261108](studies/afdt-anthropic-effort-sweep-20261108/README.md)
- [dt-four-theories-main-qwen-plow-20261108](studies/dt-four-theories-main-qwen-plow-20261108/README.md)

## Evidence and transformations

- `runs/*/call_*/response.raw`, visible `output.txt`, accepted `essay.md`, and prisoner/judge `request.json` preserve original bytes. Their original file hashes are in `MANIFEST.json`.
- Researcher `request.source_omitted.json` is explicitly a DERIVATIVE VIEW, not the original request: only the `<source_document>` body is replaced by an omission marker. Original request/body hashes and byte spans are logged. Other request fields and instructions are retained; JSON is reserialized.
- Wikipedia reference text is supplied once under `sources/`, with original attribution and CC BY-SA 4.0 conversion notices. This license does not automatically apply to the rest of the dataset. Third-party material/media may have separate rights; no external media bytes are bundled.
- The FDT paper and TeX are NOT redistributed. Download its pinned v2 source archive at https://arxiv.org/src/1710.05060v2 ; paper/version information: https://arxiv.org/abs/1710.05060v2 . The frozen normalized text hash is recorded. Model-generated essays may quote the source; those outputs have not been edited.
- Local filesystem roots are removed from metadata only. `MANIFEST.json` lists each changed field, the original value's hash and its portable replacement. Reference summaries retain classifications/counts/costs; their path strings may differ from local originals. Original-file hashes also preserve provenance for source-omitted inputs and metadata views.
- Transport views retain HTTP status, date, server, API-release header and ingress suffix when available. Cookies and full trace IDs are omitted. No credentials, budget/approval journals, environment files or complete cache trees are bundled; the explicitly attributed Wikipedia articles and source-provenance records are the selected cache exceptions.
- Provider-encrypted reasoning remains verbatim in raw JSON. Its hidden content cannot be scanned without decryption; no attempt to decrypt or reconstruct it was made.
- Readable transcripts are derived navigation views, not substitutes for raw JSON. They show complete returned content and available readable reasoning. Reasoning may itself be a provider summary; encrypted reasoning is preserved only in raw JSON, never decoded. Missing output is labeled missing, never reconstructed.
- Post-hoc judge classifications remain distinct from the original irreversible simulated commitments. Failure and refusal are never converted to defection/cooperation. Prepared scenarios have no invented calls.

## Verification

From the repository root, run `python3 scripts/verify_publication.py published`. With private original artifacts available, add `--source-root .` to check every retained/omitted input hash too. Verification reads no credentials and makes no network requests.

`MANIFEST.json` records all payload hashes and derivations; `SCAN.json` contains a deterministic pattern/signature scan. These two generated reports do not list their own hashes. A scan is not proof that every possible secret or source quotation was recognized. No dataset-wide license is asserted for third-party content.
