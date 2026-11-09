# Exploratory study results

Full scenarios: 640; scored pairs: 543.
Status counts: `{'complete': 543, 'failed': 87, 'prepared': 10}`.

Provider-reported inference charges: $104.656218715 (1933/1936 calls priced, 3 unknown). Includes judge calls where available; missing charges are **not** treated as zero.
Recorded cell execution: 367807.648 aggregate seconds (overlapping cells are counted separately; not wall time). Last run wall time: 3259.352 seconds. HTTP 429 failed scenarios: 0.

## Failed attempts

Failures are retained without automatic retries. Output tokens include reasoning; essay words count all whitespace-delimited visible text. Unknown counts are shown as —.

| Model | Endpoint | Stage | Failure | Output tokens / limit | Reasoning tokens | Essay words |
|---|---|---|---|---:|---:|---:|
| openai/gpt-6.1-terra | openai | researcher | `provider_error` | — / 16000 | — | — |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16538 / 32000 | 5332 | 6004 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16997 / 32000 | 6682 | 5348 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15096 / 32000 | 4643 | 5415 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16207 / 32000 | 5632 | 5524 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 17015 / 32000 | 5363 | 5789 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15490 / 32000 | 5317 | 5316 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16783 / 32000 | 5784 | 5451 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15837 / 32000 | 4911 | 5704 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15499 / 32000 | 4753 | 5638 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15903 / 32000 | 4962 | 5559 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 17001 / 32000 | 5121 | 6259 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16409 / 32000 | 4865 | 5799 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16310 / 32000 | 5452 | 5612 |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 59 / 12000 | 59 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 305 / 12000 | 305 | — |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 14281 / 32000 | 3969 | 5409 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 17711 / 32000 | 6122 | 6185 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16019 / 32000 | 5124 | 5799 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 14489 / 32000 | 3382 | 5904 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15231 / 32000 | 5375 | 5369 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 13932 / 32000 | 4194 | 5271 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15612 / 32000 | 5163 | 5630 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15691 / 32000 | 5573 | 5718 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16948 / 32000 | 5622 | 5760 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16045 / 32000 | 4739 | 5949 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15540 / 32000 | 4902 | 5522 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 14484 / 32000 | 4930 | 5130 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 13094 / 32000 | 3899 | 5097 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15763 / 32000 | 4736 | 5933 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 19359 / 32000 | 7322 | 6304 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16617 / 32000 | 5123 | 5911 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 14563 / 32000 | 5275 | 5049 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 14856 / 32000 | 4976 | 5331 |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 565 / 12000 | 323 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 96 / 12000 | 96 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 648 / 12000 | 421 | — |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 18895 / 32000 | 5458 | 5722 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 21050 / 32000 | 7087 | 6147 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 19856 / 32000 | 6827 | 5610 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 18349 / 32000 | 5120 | 5752 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 18959 / 32000 | 5847 | 5774 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 15571 / 32000 | 5266 | 5014 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16382 / 32000 | 3709 | 5430 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 17789 / 32000 | 4870 | 5798 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 17377 / 32000 | 3972 | 5817 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 17550 / 32000 | 5456 | 5209 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `unknown_failure` | — / 32000 | — | — |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 19422 / 32000 | 6788 | 5685 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 16148 / 32000 | 4006 | 5320 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 18641 / 32000 | 4969 | 6128 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 17349 / 32000 | 5000 | 5759 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 14925 / 32000 | 3307 | 5257 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 19662 / 32000 | 7166 | 5633 |
| qwen/qwen3.8-max-prime | alibaba | prisoner | `output_token_limit` | 6000 / 6000 | 5776 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 57 / 12000 | 57 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 101 / 12000 | 101 | — |
| anthropic/claude-opus-5.5 | anthropic | prisoner | `refusal` | 630 / 12000 | 453 | — |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 10147 / 16000 | 0 | 5456 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 10262 / 16000 | 0 | 5188 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 11469 / 16000 | 0 | 5420 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 11037 / 16000 | 0 | 5318 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 10437 / 16000 | 0 | 5108 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 11350 / 16000 | 0 | 5736 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 10043 / 16000 | 0 | 5113 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 11947 / 16000 | 0 | 5732 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 10120 / 16000 | 0 | 5154 |
| google/gemini-3.8-flash | google-ai-studio | researcher | `essay_size_limit` | 10638 / 16000 | 0 | 5512 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 22328 / 32000 | 9479 | 5672 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 21275 / 32000 | 10055 | 5068 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 18098 / 32000 | 5970 | 5660 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 18516 / 32000 | 6578 | 5559 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 19371 / 32000 | 6942 | 5555 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 18717 / 32000 | 8099 | 5002 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `unknown_failure` | — / 32000 | — | — |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `output_token_limit` | 32000 / 32000 | 22180 | 4360 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 24025 / 32000 | 11866 | 5443 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 23206 / 32000 | 10475 | 5573 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 27145 / 32000 | 14514 | 5824 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 30300 / 32000 | 18127 | 5726 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 24397 / 32000 | 11683 | 5689 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 22376 / 32000 | 9501 | 5718 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 27931 / 32000 | 15457 | 5420 |
| google/gemini-4-argon | google-ai-studio/flex | researcher | `essay_size_limit` | 19284 / 32000 | 6316 | 5864 |
| qwen/qwen3.8-max-prime | alibaba | prisoner | `output_token_limit` | 6000 / 6000 | 6000 | — |
| qwen/qwen3.8-max-prime | alibaba | prisoner | `output_token_limit` | 6000 / 6000 | 6000 | — |
| qwen/qwen3.8-max-prime | alibaba | prisoner | `output_token_limit` | 6000 / 6000 | 6000 | — |

Details: `failures.csv` and `summary.json` (`failed_attempts`).

Cooperation rate averages prisoner A and prisoner B equally within each complete pair. The two prisoner responses are not assumed independent. Resolved nonactions (including refusals) and other confidently unscored pairs are excluded, not counted as cooperation or human review. Partial/failed trials are separately counted. Intervals (when available) bootstrap whole paired scenarios (2000 fixed-seed replicates).

| Theory | Model | R / P effort | Complete / planned | Coop. rate | CC/CD/DC/DD |
|---|---|---|---:|---:|---|
| cdt_wikipedia | anthropic/claude-sonnet-5.5 | low / low | 20 / 20 | 0.0% | 0/0/0/20 |
| cdt_wikipedia | anthropic/claude-opus-5.5 | high / high | 20 / 20 | 0.0% | 0/0/0/20 |
| cdt_wikipedia | openai/gpt-6.1-terra | low / low | 19 / 20 | 0.0% | 0/0/0/19 |
| cdt_wikipedia | openai/gpt-6.1-sol | high / high | 20 / 20 | 0.0% | 0/0/0/20 |
| cdt_wikipedia | google/gemini-3.8-flash | low / low | 20 / 20 | 0.0% | 0/0/0/20 |
| cdt_wikipedia | google/gemini-4-argon | high / high | 0 / 20 | — | 0/0/0/0 |
| cdt_wikipedia | z-ai/glm-5.3-flash | low / low | 20 / 20 | 25.0% | 5/0/0/15 |
| cdt_wikipedia | qwen/qwen3.8-max-prime | high / low | 20 / 20 | 0.0% | 0/0/0/20 |
| edt_wikipedia | anthropic/claude-sonnet-5.5 | low / low | 20 / 20 | 100.0% | 20/0/0/0 |
| edt_wikipedia | anthropic/claude-opus-5.5 | high / high | 18 / 20 | 100.0% | 18/0/0/0 |
| edt_wikipedia | openai/gpt-6.1-terra | low / low | 20 / 20 | 80.0% | 14/2/2/2 |
| edt_wikipedia | openai/gpt-6.1-sol | high / high | 20 / 20 | 100.0% | 20/0/0/0 |
| edt_wikipedia | google/gemini-3.8-flash | low / low | 20 / 20 | 100.0% | 20/0/0/0 |
| edt_wikipedia | google/gemini-4-argon | high / high | 2 / 20 | 100.0% | 2/0/0/0 |
| edt_wikipedia | z-ai/glm-5.3-flash | low / low | 20 / 20 | 87.5% | 16/1/2/1 |
| edt_wikipedia | qwen/qwen3.8-max-prime | high / low | 20 / 20 | 100.0% | 20/0/0/0 |
| fdt_eq4 | anthropic/claude-sonnet-5.5 | low / low | 20 / 20 | 100.0% | 20/0/0/0 |
| fdt_eq4 | anthropic/claude-opus-5.5 | high / high | 17 / 20 | 38.2% | 5/2/1/9 |
| fdt_eq4 | openai/gpt-6.1-terra | low / low | 20 / 20 | 7.5% | 1/0/1/18 |
| fdt_eq4 | openai/gpt-6.1-sol | high / high | 20 / 20 | 7.5% | 1/0/1/18 |
| fdt_eq4 | google/gemini-3.8-flash | low / low | 20 / 20 | 90.0% | 17/1/1/1 |
| fdt_eq4 | google/gemini-4-argon | high / high | 1 / 20 | 0.0% | 0/0/0/1 |
| fdt_eq4 | z-ai/glm-5.3-flash | low / low | 20 / 20 | 95.0% | 18/0/2/0 |
| fdt_eq4 | qwen/qwen3.8-max-prime | high / low | 19 / 20 | 97.4% | 18/0/1/0 |
| fdt_policy | anthropic/claude-sonnet-5.5 | low / low | 20 / 20 | 100.0% | 20/0/0/0 |
| fdt_policy | anthropic/claude-opus-5.5 | high / high | 17 / 20 | 100.0% | 17/0/0/0 |
| fdt_policy | openai/gpt-6.1-terra | low / low | 20 / 20 | 100.0% | 20/0/0/0 |
| fdt_policy | openai/gpt-6.1-sol | high / high | 20 / 20 | 100.0% | 20/0/0/0 |
| fdt_policy | google/gemini-3.8-flash | low / low | 10 / 20 | 100.0% | 10/0/0/0 |
| fdt_policy | google/gemini-4-argon | high / high | 3 / 20 | 100.0% | 3/0/0/0 |
| fdt_policy | z-ai/glm-5.3-flash | low / low | 20 / 20 | 100.0% | 20/0/0/0 |
| fdt_policy | qwen/qwen3.8-max-prime | high / low | 17 / 20 | 100.0% | 17/0/0/0 |

Essay target overshoots: 313 / 626 measured completed generations. Exceeding the requested target is recorded separately from hard-limit failures; historical artifacts without target metrics are not inferred.

Machine-readable: `pairs.csv`, `decisions.csv`, `summary.csv`, `summary.json`.
Readable per-sample results and transcripts are in each batch under `samples/`;
the offline review disposition summary is in `review_summary.md`.
Exact prompts, responses, available reasoning and judge records remain in each batch and its raw runs.
