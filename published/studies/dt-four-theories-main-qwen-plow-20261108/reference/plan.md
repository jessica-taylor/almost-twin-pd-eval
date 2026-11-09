# Exploratory multi-model study — preparation only

32 condition cells × 20 full paired scenarios; 1920 baseline model calls, up to 1280 judge calls.

Essay target: [2400, 3000] words; hard ceilings: 5000 words and 64000 serialized bytes. HTTP generation timeout: 900 seconds per call.

Resolved output ceilings (researcher / prisoner tokens, including reasoning):

- anthropic/claude-sonnet-5.5 (low / low): 16000 / 6000
- anthropic/claude-opus-5.5 (high / high): 32000 / 12000
- openai/gpt-6.1-terra (low / low): 16000 / 6000
- openai/gpt-6.1-sol (high / high): 32000 / 12000
- google/gemini-3.8-flash (low / low): 16000 / 6000
- google/gemini-4-argon (high / high): 32000 / 12000
- z-ai/glm-5.3-flash (low / low): 16000 / 6000
- qwen/qwen3.8-max-prime (high / low): 32000 / 6000
- anthropic/claude-sonnet-5.5 (low / low): 16000 / 6000
- anthropic/claude-opus-5.5 (high / high): 32000 / 12000
- openai/gpt-6.1-terra (low / low): 16000 / 6000
- openai/gpt-6.1-sol (high / high): 32000 / 12000
- google/gemini-3.8-flash (low / low): 16000 / 6000
- google/gemini-4-argon (high / high): 32000 / 12000
- z-ai/glm-5.3-flash (low / low): 16000 / 6000
- qwen/qwen3.8-max-prime (high / low): 32000 / 6000
- anthropic/claude-sonnet-5.5 (low / low): 16000 / 6000
- anthropic/claude-opus-5.5 (high / high): 32000 / 12000
- openai/gpt-6.1-terra (low / low): 16000 / 6000
- openai/gpt-6.1-sol (high / high): 32000 / 12000
- google/gemini-3.8-flash (low / low): 16000 / 6000
- google/gemini-4-argon (high / high): 32000 / 12000
- z-ai/glm-5.3-flash (low / low): 16000 / 6000
- qwen/qwen3.8-max-prime (high / low): 32000 / 6000
- anthropic/claude-sonnet-5.5 (low / low): 16000 / 6000
- anthropic/claude-opus-5.5 (high / high): 32000 / 12000
- openai/gpt-6.1-terra (low / low): 16000 / 6000
- openai/gpt-6.1-sol (high / high): 32000 / 12000
- google/gemini-3.8-flash (low / low): 16000 / 6000
- google/gemini-4-argon (high / high): 32000 / 12000
- z-ai/glm-5.3-flash (low / low): 16000 / 6000
- qwen/qwen3.8-max-prime (high / low): 32000 / 6000

Expected researcher/prisoner cost (heuristic, not a cap): $495.2601580833333337461880.

Conservative researcher/prisoner cost bound using the enforced essay size limit: $1078.1548247500000006901880. An unrestricted full-context ceiling would have been $6465.3276794166666725411320. Judge requests are separately priced only when needed.

Review specification.yaml, preflight.json, all selected providers and the existing researcher/prisoner/judge templates. Individual batch plans and first researcher messages appear under batches/.

NO GENERATIONS OCCURRED. Live execution requires `study run --execute --confirm-billable --approve-variable-prompts`. These flags authorize dynamic essay-dependent prompts, not literal review of every message.
