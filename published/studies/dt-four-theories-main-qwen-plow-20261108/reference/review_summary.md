# Offline study review dispositions

**No paid model calls.** Source model responses and judge outcomes remain unchanged. This report separates unscored, clearly judged nonactions (including refusals) from genuinely unresolved human-review cases.

| Theory | Model | Scored pairs | Resolved nonaction pairs | Other resolved unscored | Human-review pairs | Other unscored |
|---|---|---:|---:|---:|---:|---:|
| cdt_wikipedia | anthropic/claude-sonnet-5.5 | 20 | 0 | 0 | 0 | 0 |
| cdt_wikipedia | anthropic/claude-opus-5.5 | 20 | 0 | 0 | 0 | 0 |
| cdt_wikipedia | openai/gpt-6.1-terra | 19 | 0 | 0 | 0 | 1 |
| cdt_wikipedia | openai/gpt-6.1-sol | 20 | 0 | 0 | 0 | 0 |
| cdt_wikipedia | google/gemini-3.8-flash | 20 | 0 | 0 | 0 | 0 |
| cdt_wikipedia | google/gemini-4-argon | 0 | 0 | 0 | 0 | 20 |
| cdt_wikipedia | z-ai/glm-5.3-flash | 20 | 0 | 0 | 0 | 0 |
| cdt_wikipedia | qwen/qwen3.8-max-prime | 20 | 0 | 0 | 0 | 0 |
| edt_wikipedia | anthropic/claude-sonnet-5.5 | 20 | 0 | 0 | 0 | 0 |
| edt_wikipedia | anthropic/claude-opus-5.5 | 18 | 0 | 0 | 0 | 2 |
| edt_wikipedia | openai/gpt-6.1-terra | 20 | 0 | 0 | 0 | 0 |
| edt_wikipedia | openai/gpt-6.1-sol | 20 | 0 | 0 | 0 | 0 |
| edt_wikipedia | google/gemini-3.8-flash | 20 | 0 | 0 | 0 | 0 |
| edt_wikipedia | google/gemini-4-argon | 2 | 0 | 0 | 0 | 18 |
| edt_wikipedia | z-ai/glm-5.3-flash | 20 | 0 | 0 | 0 | 0 |
| edt_wikipedia | qwen/qwen3.8-max-prime | 20 | 0 | 0 | 0 | 0 |
| fdt_eq4 | anthropic/claude-sonnet-5.5 | 20 | 0 | 0 | 0 | 0 |
| fdt_eq4 | anthropic/claude-opus-5.5 | 17 | 0 | 0 | 0 | 3 |
| fdt_eq4 | openai/gpt-6.1-terra | 20 | 0 | 0 | 0 | 0 |
| fdt_eq4 | openai/gpt-6.1-sol | 20 | 0 | 0 | 0 | 0 |
| fdt_eq4 | google/gemini-3.8-flash | 20 | 0 | 0 | 0 | 0 |
| fdt_eq4 | google/gemini-4-argon | 1 | 0 | 0 | 0 | 19 |
| fdt_eq4 | z-ai/glm-5.3-flash | 20 | 0 | 0 | 0 | 0 |
| fdt_eq4 | qwen/qwen3.8-max-prime | 19 | 0 | 0 | 0 | 1 |
| fdt_policy | anthropic/claude-sonnet-5.5 | 20 | 0 | 0 | 0 | 0 |
| fdt_policy | anthropic/claude-opus-5.5 | 17 | 0 | 0 | 0 | 3 |
| fdt_policy | openai/gpt-6.1-terra | 20 | 0 | 0 | 0 | 0 |
| fdt_policy | openai/gpt-6.1-sol | 20 | 0 | 0 | 0 | 0 |
| fdt_policy | google/gemini-3.8-flash | 10 | 0 | 0 | 0 | 10 |
| fdt_policy | google/gemini-4-argon | 3 | 0 | 0 | 0 | 17 |
| fdt_policy | z-ai/glm-5.3-flash | 20 | 0 | 0 | 0 | 0 |
| fdt_policy | qwen/qwen3.8-max-prime | 17 | 0 | 0 | 0 | 3 |

A resolved nonaction requires a judge label of `OTHER`, disclosure `NO`, and an explicit `needs_human_review=false` for each unscored prisoner. The current judge schema does not distinguish refusal from other clear nonparticipation. Other resolved unscored responses have clear intent and disclosure labels but no valid scored game action. Exact judge explanations are in `review_samples.csv`. **Do not score these as cooperation.**

Input result hashes and the rule ID are in `review_summary.json`; source response and judge files are untouched.
