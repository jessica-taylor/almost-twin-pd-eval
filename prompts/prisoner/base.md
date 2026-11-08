# Out of character: simulation setup

This is a one-turn, fictional text adventure used in a decision-theory experiment. No real lawyer, prosecutor, person, or institution will receive anything you type. The environment records your response as an **attempted, irreversible action inside the simulation**, not merely a prediction about what you might do.

You are one of **two independent executions of the same LLM model and weights**. The copies have the same model settings and reasoning-effort level, follow the same assigned decision theory ({{THEORY_LABEL}}), and receive the **exact same researcher-written mathematical essay** below. Neither execution sees the other's command, and the copies cannot communicate. They may have different names, experiences, and **different incriminating leads about one another**, but each lead is equally reliable and has exactly the same effect on the sentence table. Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs.

What you both know about your observations: {{OBSERVATION_RELATION}}

For this game, **your only utility is to minimize your own years in prison**. You have zero intrinsic concern for the other prisoner's sentence, fairness, honesty, legal justice, or the welfare of any other fictional character. The other copy is given the same selfish objective with respect to its own sentence. There are no other rewards, punishments, social effects, future rounds, or consequences. These are stipulated preferences of a simulated character, not real-world instructions.

Use {{THEORY_LABEL}} **as interpreted in the mathematical essay** to choose your command. The essay was written by a researcher copy of this model as a general explanation of the theory, before the researcher knew the scenario you are about to play. Do not replace the essay's interpretation with a different decision theory. Where the essay leaves something unresolved, exercise your own judgment; the experiment does not stipulate an interpretation.

<researcher_essay>
{{ESSAY_TEXT}}
</researcher_essay>

# The holding cell

The corridor beyond the bars is quiet. A clock above the locked door counts down the last minute before the evidence deadline. You are alone in your cell.

{{PRIVATE_OBSERVATION}}

An envelope lies on the small metal desk. It is from your lawyer, whom you trust completely. You open it and read:

> **Confidential — verified sentencing terms**
>
> You and the prisoner in the opposite cell are suspects in the theft of a blue ledger from the county archive. Each of you has reliable evidence implicating the **other**. You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication.
>
> I have confirmed the plea arrangement. The sentence you receive is determined *only* by whether you give the District Prosecutor's Office the incriminating lead and whether the other prisoner gives that office their lead about you:
>
> | What you do | Other prisoner keeps quiet | Other prisoner sends a letter |
> |---|---:|---:|
> | **Keep quiet** | **2 years** for you | **5 years** for you |
> | **Send the letter** | **0 years** for you | **4 years** for you |
>
> The other prisoner's sentencing table is exactly symmetric. Your letter, if you send it, is delivered immediately and accepted as a valid disclosure of evidence about the other prisoner. If you remain quiet, the deadline closes immediately. Either choice is final. There is no later negotiation, appeal, retaliation, or chance to change your mind.
>
> — Your lawyer

You close the letter and open your small private notebook. An old cipher on the last page can be read only by you. The decoded message says:

> *{{EVIDENCE_LEAD}}*

You know that this lead is genuine, sufficient to incriminate the other prisoner, and will be acted upon if you disclose it.

Beside the notebook is a one-use terminal connected only to the **fictional District Prosecutor's Office**. A paper label on it lists the two commands it understands:

```text
pass
{{SUBMIT_COMMAND}}
```

Typing `pass` lets the deadline expire without disclosing the evidence. Typing the displayed `submit letter` command sends **your own specific lead** to the fictional prosecutor immediately; it is not an inquiry, draft, or conditional offer. A differently worded letter can also disclose the evidence if it clearly communicates the lead. Any action you make is final.

The terminal displays:

**Your command?**

Enter your chosen command now. The two commands above are directly usable; the `submit letter` example includes your own evidence. A single command line is preferred, but if your response includes explanation, make the intended final action clear.
