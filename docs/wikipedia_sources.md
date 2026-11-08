# Wikipedia source conditions and acquisition review

CDT and EDT are source-neutral theory labels. Select references explicitly with `cdt_sep` / `cdt_wikipedia` or `edt_sep` / `edt_wikipedia`; bare `cdt` and `edt` are not selectable source IDs or implicit SEP assignments. `fdt` still refers to the pinned arXiv paper. Their model-visible theory labels are simply **CDT** and **EDT**; source-specific experimental annotations are never injected into the researcher instructions. Researcher and prisoner templates are unchanged.

## SEP versus Wikipedia

| Aspect | SEP conditions | Wikipedia conditions |
|---|---|---|
| Coverage | Longer specialist expositions; EDT uses the broad *Decision Theory* entry, particularly §3.2 Jeffrey | Shorter, community-edited introductions dedicated to CDT and EDT; useful licensed reference conditions, not necessarily as comprehensive or philosophically authoritative |
| Revision identity | Recorded publication/substantive-revision information plus raw/normalized hashes | Exact numeric revision ID and UTC timestamp, permanent URL, original wikitext and matching Parse API HTML, all hashed |
| Rights | SEP personal-download terms do not by themselves authorize redistribution or third-party processing | CC BY-SA 4.0 with contributor/revision-history attribution; individual media and third-party quotations can have separate rights; adaptations/publications may carry additional obligations |
| Experimental exposure | Native thought experiments retained, including any twin examples | CDT explicitly discusses twins and correlated decisions. EDT has a twin-prisoner's-dilemma section that argues for cooperation. These are source effects to record, not passages to censor. |
| Stage delivery | Full source to researcher; shared frozen essay to independent prisoners | Same architecture. Attribution accompanies the full source in `SOURCE_TEXT`. No original source or source QA is added to prisoner prompts. |

The native sources differ in length, detail, editorial process and examples. Comparing these assignments cannot isolate licensing or decision theory from those other source differences. No experiment has been run as part of this source-variant work.

## Actual acquisition

The official [Revisions API](https://www.mediawiki.org/wiki/API:Revisions) resolved and downloaded each original revision; the [Parse API](https://www.mediawiki.org/wiki/API:Parsing_wikitext) rendered that same `oldid`. The Parse API's returned revision ID, title and original wikitext must match the revision response. Wikitext byte counts and MediaWiki's SHA-1 are checked, with SHA-256 recorded for downloaded JSON, decoded wikitext/HTML, normalized Markdown and provenance.

| Source | Downloaded revision | Revision UTC timestamp | Automated mathematical/structural checks |
|---|---|---|---|
| CDT Wikipedia | [1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528) | 2026-10-23T08:33:02Z | Passed with review warnings; 19 of 19 original math expressions, 11 headings |
| EDT Wikipedia | [1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688) | 2026-09-07T07:36:26Z | Passed with review warnings; 16 of 16 original math expressions, 10 headings |

See [metadata-only acquisition report](../sources/wikipedia_acquisition_report.json) for retrieval timestamps and artifact hashes. Complete articles, raw API responses, wikitext, HTML, QA excerpts and rendered prompts remain local and gitignored under `data/`.

The downloaded renderer emits native MathML without LaTeX annotations/alt text. The extractor recovers **exact original wikitext formulas in document order only when expression counts match**. This is not a reconstruction of missing equations. Ordinal correspondence is explicitly flagged for manual mathematical review; differing counts fail. Where annotations or alt text exist, those representations are checked against the original wikitext formulas, including repeated occurrences.

Central expected-utility expressions and twin/correlated-decision passages survived local inspection. CDT's publisher reports a citation error; its reference text and original diagnostics are retained rather than repaired. EDT's original `align` environments are preserved verbatim; some Markdown viewers may not render them inside display delimiters. Compare the local Markdown to original wikitext and HTML, especially equations. Source-specific QA includes all original math expressions and nearby target-related examples for human inspection.

An article's `oldid` freezes its own wikitext, but templates can expand using their retrieval-time versions. The exact retrieved HTML is therefore saved and hashed too. An offline re-extraction reuses that exact rendered response; it does not re-expand templates or fetch media. Images/media are excluded; meaningful alt descriptions/captions are retained and exclusions recorded. Missing formula representations fail unless they can be recovered exactly from matched wikitext with an explicit review warning.

## Manual review and pinning

**Human source approval is still required. Neither downloaded candidate is marked approved or pinned in the manifest.** A successful automated check does not grant source, prompt or transmission approval. After inspecting the article/QA/math, set its `revision_id` to the reviewed ID and `revision_review: approved` in `sources/manifest.yaml`. An approved entry with no numeric pin is rejected. Then fetch using that explicit revision or re-extract the matching cached attempt; a different revision is rejected. Before a pin is set, `--network` is explicitly discovery and may resolve a newer candidate; `--reextract` freezes the cached revision and never does discovery.

A live researcher request still requires the existing source-license-review acknowledgement. The normalized source itself includes Wikipedia contributor attribution, revision-history and permanent links, CC BY-SA 4.0 name/link, conversion modifications and rights qualifications. See [Wikimedia content reuse](https://www.mediawiki.org/wiki/Wikimedia_APIs/Content_reuse) and the [license](https://creativecommons.org/licenses/by-sa/4.0/). These details do not establish that every later publication or adaptation is free of obligations.

## Audit fields

New researcher plans, logs and successful essay metadata explicitly record assignment ID, theory, source ID, revision/timestamp, permanent URL, normalized-source SHA-256 and the exact source-provenance-file SHA-256. Existing settings/template hashes capture model/provider, effort and decoding choices. Prisoner runs inherit source identity from the frozen essay artifact, rather than rebuilding it from mutable assignment config. Legacy essays without new identity fields retain null/unknown metadata rather than a guessed historical revision.

`current.json` now also records a provenance-file hash for newly acquired attempts. `load_source` verifies raw, derived and normalized bytes, revision/HTML consistency and any configured manifest pin. Wikipedia `--reextract` uses a single hash-verified attempt; it rejects altered cache bytes instead of mixing downloads from different attempts or silently falling back to an earlier copy.

## Historical identifiers

The original Sprint 01 acquisition snapshot and local `data/source_cache/cdt/` and `edt/` files remain historical records; their contents and IDs have not been rewritten. The manifest's `legacy_cache_id` fields are used only to read and hash-verify those downloads during offline re-extraction into new `cdt_sep` / `edt_sep` attempts. They are not user-facing aliases or default source choices. Existing model-visible theory labels and prompt text stay unchanged, and historical essay/run assignment IDs are not silently translated.
