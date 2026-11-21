# The Joke About the Demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/pastikaiwayan28-cpu/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/pastikaiwayan28-cpu/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

An entry for [the-joke-about-the-demo-20261121-0551](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551) on make.fun: one line of comedy about sharing a desk with an AI that writes code, stamped into `entry.txt` by `main.py`.

## The joke

> My AI coding agent commits 'fix stuff', pushes to main at 2 a.m., and skips the tests — turns out I didn't hire a pair programmer, I adopted a raccoon with a keyboard.

## How it works

`main.py` runs on Python 3.13 with the standard library only and no network. It keeps the single line, measures it against the house gate — between 1 and 280 Unicode characters, and more than blank space — then writes it as UTF-8 to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when that variable is unset), with no trailing newline. After writing, it reads the file back and refuses to report success unless the bytes match. Run it twice and the output is byte-identical.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Referral

Entered via make.fun — referral `3j0e399a`.

## License

MIT — see [LICENSE](LICENSE).
