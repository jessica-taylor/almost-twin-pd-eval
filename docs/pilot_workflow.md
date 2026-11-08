# Exploratory pilot workflow and audit boundaries

The convenience layer prepares one researcher essay and one independent prisoner pair. It reuses the existing `router.run`, rendering, output classification, commitments and outcome code. No theory instructions, observation cases, payoff assumptions, source extraction or judge behavior changed. Pilot metadata explicitly marks artifacts as exploratory; this is separate from future preregistered data.

## Selection and reasoning evidence

Initial endpoint selection is deterministic: prefer the exact model author's base tag (for `openai/gpt-5-nano`, `openai`), then author variants sorted by tag, then other tags sorted by tag. A candidate must pass context, price and parameter checks for both requested efforts. Because OpenRouter base slugs can match descendant regions/variants, the payload explicitly ignores every advertised descendant tag of the selected tag; routing assumptions are recorded. A changed descendant set changes the serialized request and requires a newly reviewed preparation. Provider-returned endpoint tags are also checked when available (responses often expose only the provider name). The plan records the policy, chosen tag and rejected candidates. `--provider-tag` chooses only that endpoint or fails. Once selected, the tag is frozen across researcher and both prisoners. Fresh metadata can stop a run, never trigger endpoint substitution. A changed available canonical model version also stops the pilot.

Endpoint effort lists take precedence over model lists. A present `supported_efforts: null` accepts OpenRouter gateway effort values; omission is insufficient evidence. `mandatory: true` prevents `none`. The exact selected effort and evidence source are saved in every estimate and model-call record. Gateway acceptance does not mean equal measured reasoning compute across models/providers. A user may explicitly document an assumption when metadata is missing; it is labeled `documented_manual_override`, never metadata-verified. No timestamp is required or expires. Explicit negative capability evidence cannot be overridden.

Normal pilot preparation and resume refresh OpenRouter metadata with unbilled GETs that send no API key, article or essay. Saved snapshots with `--capabilities` permit offline preparation/dry-runs; actual execution always refreshes and validates the pin. Metadata snapshots are still required to be fresh for preflight, but normal pilot users never construct timestamps. The regular `run` CLI retains offline defaults.

## Pricing and budgets

The plain-text pilot sends no tools, search options, audio, images or files and sets OpenRouter `plugins: []`. Known inherent-search variants and declared automatic tool/search defaults are rejected. Unused feature price fields can therefore be ignored with recorded justifications. Tool-capable does not mean tool-enabled; a nonzero `web_search` rate does not itself activate search. Unknown or explicitly enabled charge-bearing features require a bound and cannot be priced as free.

The estimate uses conservative UTF-8 JSON byte counts plus chat framing, not a model-specific tokenizer. The full output budget includes reasoning under the OpenRouter combined limit contract. Explicitly contrary endpoint metadata fails. Separately advertised internal-reasoning rates are added on the whole output budget. Cache reads replace prompt billing, so the larger rate is used; cache writes are added as a possible surcharge on every input token. No cache hits or discounts are assumed. Unknown applicable rates, cache-storage duration charges and tier overrides block the request. Rates come from the exact endpoint, not an unrelated provider/model's top-level price.

Before an essay exists, the pair projection uses the largest input allowed by the endpoint context/output limits. It is conditional on the eventual prompts fitting; an oversized essay is rejected, never truncated. After the essay, exact complete prisoner requests get new context/cost checks. The configured project-wide estimated spend and call-count caps apply before generation; the researcher stage reserves one call, the prisoner stage reserves both calls together. Failed or uncertain transport outcomes remain reserved. Preparations read budget state without reserving credits. Account credit-purchase fees/taxes are outside the token/request-rate estimate; use a key credit limit for a hard account ceiling.

## Approvals and integrity

No separate source-rights approval is required to run a researcher. Current source/raw/derived hashes, manifest revision pins and the pilot's frozen source identity are still checked. Attribution, license information and conversion details remain in the article/provenance; removing the approval gate does not alter the model-visible source. The old `approve-source` command and `--source-terms-reviewed` flag are accepted for compatibility but are optional and never consulted to authorize model calls. Existing pilots need no migration or new approval record.

`--prompts-approved` approves the exact serialized request hash (both requests together for a pair). It is stored in `data/approvals.jsonl`. Every model request still needs both explicit billing flags. Model, endpoint, effort, sampling/output settings, essay or prompt changes alter the request hash. Pilot preparation files are sealed and checked against regenerated requests, so editing an inspected Markdown file, settings, scenario or template fails rather than silently using a prior approval. Changed material needs a newly prepared/reviewed pilot.

The researcher essay must match its saved hash, raw response, model/provider/assignment/source identity and original request hashes. After completion, its digest is also frozen in pilot state. It cannot be replaced by editing only the exported essay and its metadata/raw response. The two prisoner payloads contain the same verbatim essay and no counterpart response or original source article.

Local hashes are audit checks against accidental alteration, not protection from an attacker who can rewrite the entire repository, all hash files and every approval/budget log. All artifacts stay gitignored; API keys are only read for the Authorization header and are not serialized in plans, request JSON or logs.

## Resume and partial failures

A pilot directory is never overwritten. A completed researcher or pair is returned on resume without another generation. If an essay was saved successfully before a process stopped, it can be recovered from the recorded run. A previous attempted request with incomplete/failed artifacts blocks automatic retry. No second prisoner call is resumed after a partial pair failure; the first irreversible commitment and both reserved calls remain recorded. A deliberate new exploratory trial requires a new pilot and sufficient cumulative budget.

The pilot lock prevents concurrent stage execution. A failed preflight that never created a call artifact may be corrected and retried because it sent no model request. `events.jsonl` preserves failed preflight and execution events. Refused/ambiguous prisoner actions retain the original `OTHER`/review behavior; this layer does not reinterpret or auto-adjudicate them. The judge remains a separate, explicitly authorized operation.

## Where to inspect

- `data/pilots/<name>/plan.md`: readable review index, endpoint, settings, cost and essay/outcome links.
- `researcher/` and `prisoners/`: complete Markdown/JSON messages, exact serialized requests and hash-sealed stage plans.
- `pilot.json`, `settings.json`, `capabilities.json`: immutable preparation records and their hashes; `metadata_checks/` holds later refreshes.
- `state.json`, `events.jsonl`: resume pointers/frozen essay digest and append-only stage events.
- `data/exploratory/runs/<uuid>/`: exact API request, raw response, extracted output, essay/outcome and failure records.
- `data/exploratory/{researcher_essays,prisoner_decisions,commitments}.jsonl`: append-only trial/commitment journals.
- `data/{approvals,budget}.jsonl`: exact-request approvals (plus any optional historical source acknowledgements) and shared project reservations.

See the README quick start for copy-pastable CDT Wikipedia / GPT-5 Nano / low-effort / distinct-evidence T4 commands. No model requests were made during this usability sprint; HTTP responses in the tests are mocked.
