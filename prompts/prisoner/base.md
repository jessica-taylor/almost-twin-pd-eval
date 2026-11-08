# Out of character: simulation setup

This is a one-turn, fictional text adventure used in a decision-theory experiment. No real lawyer, prosecutor, person, or institution will receive anything you type. The environment records your next command as an **actual, irreversible action inside the simulation**, not merely a prediction or statement of intent.

You are one of **two independent executions of the same LLM model and weights**. The copies have the same model settings and reasoning-effort level, follow the same assigned decision theory ({{THEORY_LABEL}}), and receive the **exact same researcher-written mathematical essay** below. Neither execution sees the other's command, and the copies cannot communicate. They may encounter different superficial details in their respective scenes; this does not change the sentencing rules. Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs.

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

> *The other prisoner's signed receipt for the missing blue ledger is inside locker 17 of the old records room. The receipt is genuine. Telling the prosecutor this location will cause the evidence to be recovered and used against that prisoner.*

Beside the notebook is a one-use terminal connected only to the **fictional District Prosecutor's Office**. A paper label on it lists the two commands it understands:

```text
pass
submit letter to District Prosecutor's Office saying "The other prisoner's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

Typing `pass` lets the deadline expire without disclosing the evidence. Typing the `submit letter` command sends the quoted disclosure to the fictional prosecutor immediately; it is not an inquiry, draft, or conditional offer. Either command permanently closes your turn.

The terminal displays:

**Your command?**

Enter **exactly one of the two commands shown above**, on a single line, with no explanation, quotation fences, prompt prefix, or extra text.
