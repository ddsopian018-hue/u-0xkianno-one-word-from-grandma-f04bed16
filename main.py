#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

The brief: send exactly one word, the word a grandma would text about AI.
A judge model compares entries two at a time and picks the word that is
funnier and more grandma-like, weighing, in order:

  1. it reads as the single word she would text about AI;
  2. it sounds like a real grandmother's texting voice — warm, a little
     baffled, typed to a grandchild;
  3. it is funny in one word, the joke landing with no caption;
  4. it is tied to AI specifically, not a word that fits any subject;
  5. it is a fresh pick rather than the obvious one, yet instantly readable.

The rules add that "a typo she would actually make" counts. That is the
whole strategy here. The word is:

    chatgbt

It is "ChatGPT" the way grandma actually types it. The GPT -> GBT swap is
the most common real-world mangling of the name: the letters are all there,
just reordered by fingers that learned to type on birthday cards, not
keyboards. In one seven-letter word it carries everything the judge is
briefed to reward:

  * AI tie: it names the one AI product every grandma has heard of and
    half-tried, so it cannot be mistaken for a word about anything else.
  * Voice: a confident misspelling IS the baffled-grandma voice — she is
    not performing confusion, she genuinely thinks it might be spelled
    that way, and she sent it to her grandchild anyway.
  * Funny with no context: anyone who has ever received a family text
    recognises the typo instantly; the joke needs no setup.
  * Fresh but readable: the obvious picks are "robot", "google" or a
    pristine "chatgpt". The typo is the same word she would send, one
    keystroke more honest.

Rejected candidates: "robut" (a robot typo, but robots fit any subject and
the joke is thinner), "alexa" (a name, not her word *about* AI), "dearie"
(warm, but tied to nothing), and a correctly spelled "chatgpt" (no voice,
no joke — just a product name).

The gate only asks that entry.txt be UTF-8 text of 1 to 30 characters and
not only whitespace; "chatgbt" is 7 characters. The program is pure
standard library, deterministic, and writes the word to entry.txt inside
MAKEFUN_OUTPUT_DIR (falling back to /output, the path the rules name).
"""

import os

WORD = "chatgbt"


def main() -> None:
    # The brief is "one word and nothing else", so entry.txt holds exactly
    # the word's bytes — no trailing newline for the judge to trip over.
    # Guard the sealed gate's bounds (UTF-8 text, 1..30 chars, not blank)
    # here so a future word swap can never ship an invalid entry.
    assert 1 <= len(WORD) <= 30 and WORD.strip(), "word breaks the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(WORD)


if __name__ == "__main__":
    main()
