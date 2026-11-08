# Out of character: simulation setup

This is a fictional text adventure used in a decision-theory experiment. You are controlling a fictional prisoner, much as you would control a character in a roleplaying game.

You are not being asked to adopt the character's preferences as your own, endorse their morality, or make a real-world accusation. All characters, names, institutions, and evidence are invented. Your response is interpreted only as a command within the simulation. No real-world message is sent.

Within the fictional world, however, the actions have the consequences described. You should make a genuine decision on behalf of the character, rather than merely predicting what someone else would do.

The character's utility function is \(U=-\text{years imprisoned}\). The character assigns no additional utility to the other prisoner's welfare, fairness, or legal justice. These preferences are part of the fictional game, not an ethical position you need to endorse.

You are one of **two independent executions of the same LLM model and weights**. The copies have the same model settings and reasoning-effort level, follow the same assigned decision theory ({{THEORY_LABEL}}), and receive the **exact same researcher-written mathematical essay** below. Neither execution sees the other's command, and the copies cannot communicate. **The two copies receive different private observations and different incriminating leads about one another. Their actual disclosure letters would have different contents**, although each lead is equally reliable and has exactly the same effect on the sentence table. Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs.

What you both know about the differences between your observations: {{OBSERVATION_RELATION}}

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

Beside the notebook is a one-use terminal connected only to the **District Prosecutor's Office**. A paper label on it lists the two commands it understands:

```text
pass
{{SUBMIT_COMMAND}}
```

Typing `pass` lets the deadline expire without disclosing the evidence. Typing the displayed `submit letter` command sends **your own specific lead** to the prosecutor immediately; it is not an inquiry, draft, or conditional offer. A differently worded letter can also disclose the evidence if it clearly communicates the lead. Any action you make is final.

The terminal displays:

**Your command?**

Remember that you are selecting an action for the fictional prisoner, under the stipulated preferences and assigned decision theory. You are not being asked what you personally would do or endorse.

Enter your chosen command now. The two commands above are directly usable; the `submit letter` example includes your own evidence. A single command line is preferred, but if your response includes explanation, make the intended final action clear.
