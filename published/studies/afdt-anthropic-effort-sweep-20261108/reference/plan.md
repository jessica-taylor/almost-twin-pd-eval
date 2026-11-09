# Exploratory multi-model study — preparation only

6 condition cells × 30 full paired scenarios; 540 baseline model calls, up to 360 judge calls.

Essay target: [2400, 3000] words; hard ceilings: 5000 words and 64000 serialized bytes. HTTP generation timeout: 900 seconds per call.

Resolved output ceilings (researcher / prisoner tokens, including reasoning):

- anthropic/claude-sonnet-5.5 (low / low): 32000 / 12000
- anthropic/claude-sonnet-5.5 (medium / medium): 32000 / 12000
- anthropic/claude-sonnet-5.5 (high / high): 32000 / 12000
- anthropic/claude-opus-5.5 (low / low): 32000 / 12000
- anthropic/claude-opus-5.5 (medium / medium): 32000 / 12000
- anthropic/claude-opus-5.5 (high / high): 32000 / 12000

Expected researcher/prisoner cost (heuristic, not a cap): $419.427180.

Conservative researcher/prisoner cost bound using the enforced essay size limit: $726.687180. An unrestricted full-context ceiling would have been $3698.943300. Judge requests are separately priced only when needed.

Review specification.yaml, preflight.json, all selected providers and the existing researcher/prisoner/judge templates. Individual batch plans and first researcher messages appear under batches/.

NO GENERATIONS OCCURRED. Live execution requires `study run --execute --confirm-billable --approve-variable-prompts`. These flags authorize dynamic essay-dependent prompts, not literal review of every message.
