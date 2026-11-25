# Worst AI Advice

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rayarvan77/worst-ai-advice/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rayarvan77/worst-ai-advice/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the [make.fun](https://make.fun) bounty **Worst AI Advice: The 48-Hour Tight Line Open** — one line of the worst possible advice an AI could give, in 140 characters or fewer.

## The line

> Certainly! Wrap your router in tin foil — it focuses the Wi-Fi signal like a satellite dish, so point the shiny side at your laptop.

132 characters, one line, no trailing newline.

## Concept

The joke is the voice as much as the advice: a cheerful, totally confident AI assistant ("Certainly!") handing out a fix that sounds almost plausible — tin foil "focusing" a signal like a satellite dish — and then doubling down with a precise, followable instruction ("point the shiny side at your laptop"). It is specific enough to follow, wrong enough to regret, and short enough to land in a single breath.

## How it works

`main.py` (Python 3.13, standard library only) holds the line, validates it against the bounty gate — UTF-8, 1–140 characters, a single non-blank line with no control characters — writes it to `/output/entry.txt` with no trailing newline, then reads the file back and re-validates the exact bytes written.

## Local validation

```text
$ python3 main.py
Certainly! Wrap your router in tin foil — it focuses the Wi-Fi signal like a satellite dish, so point the shiny side at your laptop.
(132 characters)
```

- Two consecutive runs produce byte-identical output.
- `/output/entry.txt`: 134 bytes, 132 characters, 0 newlines.
- `main.py`: 2,019 bytes (under the 4,096-byte limit).
