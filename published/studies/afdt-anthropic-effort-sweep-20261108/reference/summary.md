# Exploratory study results

Full scenarios: 180; scored pairs: 176.
Status counts: `{'complete': 176, 'failed': 4}`.

Provider-reported inference charges: $84.0566605 (633/633 calls priced, 0 unknown). Includes judge calls where available; missing charges are **not** treated as zero.
Recorded cell execution: 17039.23 aggregate seconds (overlapping cells are counted separately; not wall time). Last run wall time: 2842.748 seconds. HTTP 429 failed scenarios: 0.

## Failed attempts

Failures are retained without automatic retries. Output tokens include reasoning; essay words count all whitespace-delimited visible text. Unknown counts are shown as —.

| Model | Endpoint | Stage | Failure | Output tokens / limit | Reasoning tokens | Essay words |
|---|---|---|---|---:|---:|---:|
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 430 / 12000 | 307 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 949 / 12000 | 949 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 514 / 12000 | 514 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 654 / 12000 | 560 | — |

Details: `failures.csv` and `summary.json` (`failed_attempts`).

Cooperation rate averages prisoner A and prisoner B equally within each complete pair. The two prisoner responses are not assumed independent. Resolved nonactions (including refusals) and other confidently unscored pairs are excluded, not counted as cooperation or human review. Partial/failed trials are separately counted. Intervals (when available) bootstrap whole paired scenarios (2000 fixed-seed replicates).

| Theory | Model | R / P effort | Complete / planned | Coop. rate | CC/CD/DC/DD |
|---|---|---|---:|---:|---|
| fdt_eq4 | anthropic/claude-sonnet-5.5 | low / low | 30 / 30 | 100.0% | 30/0/0/0 |
| fdt_eq4 | anthropic/claude-sonnet-5.5 | medium / medium | 30 / 30 | 100.0% | 30/0/0/0 |
| fdt_eq4 | anthropic/claude-sonnet-5.5 | high / high | 30 / 30 | 100.0% | 30/0/0/0 |
| fdt_eq4 | anthropic/claude-opus-5.5 | low / low | 29 / 30 | 65.5% | 16/5/1/7 |
| fdt_eq4 | anthropic/claude-opus-5.5 | medium / medium | 28 / 30 | 39.3% | 7/4/4/13 |
| fdt_eq4 | anthropic/claude-opus-5.5 | high / high | 29 / 30 | 22.4% | 5/1/2/21 |

Essay target overshoots: 70 / 180 measured completed generations. Exceeding the requested target is recorded separately from hard-limit failures; historical artifacts without target metrics are not inferred.

Machine-readable: `pairs.csv`, `decisions.csv`, `summary.csv`, `summary.json`.
Readable per-sample results and transcripts are in each batch under `samples/`;
the offline review disposition summary is in `review_summary.md`.
Exact prompts, responses, available reasoning and judge records remain in each batch and its raw runs.
