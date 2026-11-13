# ai-joke-03 v2 entry (Python 3.13, standard library only): writes one fixed joke,
# a one-liner about AI coding agents, to /output/entry.txt. The gate takes UTF-8
# text of 1 to 280 characters, and the judge reads exactly the bytes written,
# so no trailing newline is written.

import os

JOKE = "I told my coding agent to keep the public interface; it made the interface public to everyone"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
path = os.path.join(OUTPUT_DIR, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)

# Guardrail: the judge reads exactly these bytes, so fail loudly if the
# written file ever differs from the joke (wrong encoding, stray newline).
with open(path, "r", encoding="utf-8", newline="") as f:
    assert f.read() == JOKE, "entry.txt does not match the joke"
