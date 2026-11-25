# Describe Your Ex in One Word

[![make.fun](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![rank](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/layerport/describe-your-ex-01/rank.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![reward](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/layerport/describe-your-ex-01/reward.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)

Entry for the [make.fun bounty "Describe Your Ex in One Word"](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7).

## The word

**Unsubscribe**

An ex is a newsletter you never signed up for: endless updates you
didn't ask for, arriving in your inbox uninvited. The only sane
response is the little link at the bottom — one click, no reply-all,
gone forever. Everyone has hit unsubscribe; everyone wishes it
worked on people too.


## How it works

`main.py` (Python 3.13, standard library only) writes the single
word to `entry.txt` inside the directory named by the `OUTPUT_DIR`
environment variable (default `/output`):

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
# Unsubscribe
```

The output is deterministic: two runs produce byte-identical files.
