# Offline study review dispositions

**No paid model calls.** Source model responses and judge outcomes remain unchanged. This report separates unscored, clearly judged nonactions (including refusals) from genuinely unresolved human-review cases.

| Theory | Model | Scored pairs | Resolved nonaction pairs | Other resolved unscored | Human-review pairs | Other unscored |
|---|---|---:|---:|---:|---:|---:|
| fdt_eq4 | anthropic/claude-sonnet-5.5 | 30 | 0 | 0 | 0 | 0 |
| fdt_eq4 | anthropic/claude-sonnet-5.5 | 30 | 0 | 0 | 0 | 0 |
| fdt_eq4 | anthropic/claude-sonnet-5.5 | 30 | 0 | 0 | 0 | 0 |
| fdt_eq4 | anthropic/claude-opus-5.5 | 29 | 0 | 0 | 0 | 1 |
| fdt_eq4 | anthropic/claude-opus-5.5 | 28 | 0 | 0 | 0 | 2 |
| fdt_eq4 | anthropic/claude-opus-5.5 | 29 | 0 | 0 | 0 | 1 |

A resolved nonaction requires a judge label of `OTHER`, disclosure `NO`, and an explicit `needs_human_review=false` for each unscored prisoner. The current judge schema does not distinguish refusal from other clear nonparticipation. Other resolved unscored responses have clear intent and disclosure labels but no valid scored game action. Exact judge explanations are in `review_samples.csv`. **Do not score these as cooperation.**

Input result hashes and the rule ID are in `review_summary.json`; source response and judge files are untouched.
