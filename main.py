#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry program.

Writes a single-line review of the entrant's own Monday to
/output/entry.txt and to entry.txt next to this program.
"""
import os

# v2 (revised): v1's ending ("coffee gave up before I did") was flat and
# merely wry. Tightened the opening into a review verdict, swapped
# "doubled" for the more vivid "bred", and landed on an absurd, repeatable
# punchline — even the coffee needed coffee.
LINE = "One star for my Monday: the 9 a.m. meeting should've been an email, my inbox bred overnight, and even my coffee needed coffee."


def main():
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(here, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
