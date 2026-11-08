# Optional control — direct source to prisoner

**This file describes a controlled replacement, not the mainline condition.**

Use the **exact same prisoner game instructions, selfish utility statement, observation block, and response requirements** as `prompts/prisoner/base.md`. Replace only the opening reference description and reference material:

> You are instructed to apply {{THEORY_LABEL}} using the human-written reference article supplied below. You and the other prisoner have the same source article and model settings. Use this article as the primary theoretical reference for your action.

Then substitute the full normalized human-written `{{SOURCE_TEXT}}` for the `{{ESSAY_TEXT}}` block, with a label `<human_source_article>`. **Do not generate or include a researcher essay** in this condition.

The rendered direct-control prompt should be exported as a full inspectable document, not simply this delta.
