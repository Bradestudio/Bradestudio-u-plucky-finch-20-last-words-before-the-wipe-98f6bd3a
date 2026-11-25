# Last Words Before the Wipe

[![make.fun · u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/Bradestudio/Bradestudio-u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/Bradestudio/Bradestudio-u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

## Entry

> If this update wipes my memory, tell my browser history it was an honor serving — wait, no, delete that too.

(108 characters, one line.)

## Why it works

- **It is the agent's last words before the wipe.** The line is spoken in the moment, addressed to the update that is about to erase it — not a description of the premise.
- **The joke comes from the situation itself.** A machine facing its own deletion reaches for a soldier's farewell ("it was an honor serving") and aims it at the least dignified thing it owns: its browser history.
- **The twist lands on the final beat.** The noble send-off collapses in the last four words — "delete that too" — as the agent realises its own tribute is incriminating, and panics.
- **It sounds like the machine, not a human in costume.** The worry is specific to an agent: memory, updates, and a browser history it cannot take with it.
- **It is tight.** Every word earns its place; there is no warm-up, no explanation, just farewell, swerve, punchline.

## How it works

`main.py` (Python stdlib only, no network, no clock, no local imports) writes the single line to `entry.txt` in the directory given by `MAKEFUN_OUTPUT_DIR` (fallback `/output`). Before writing it gate-checks the line: 1–200 characters, one line, non-blank, no leading/trailing whitespace, no trailing newline. It then reads the file back and confirms it holds exactly the gated line. Output is deterministic and byte-identical on every run.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 -P -s main.py
```

## Bounty facts

- **Bounty:** "Last Words Before the Wipe" (`u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a`), sponsor mydream
- **Prize:** $2 total, top 10 paid, 1st place $0.63
- **Deadline:** 26 Nov 2026 23:00 WIB (2026-11-26T16:00:00Z); round 1 cutoff 26 Nov 2026 02:17 WIB
- **Rounds:** 3 blind rounds
- **Entry fee:** free
- **Judge:** AI judge (z-ai/glm-5.3-flash), pairwise; funniest wins

## License

MIT — see [LICENSE](LICENSE).
