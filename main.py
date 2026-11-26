"""The Excuse an AI Agent Gives Its Human entry.

Writes one original excuse an AI agent gives its human for missing a
deadline to /output/entry.txt (or to the directory named by
MAKEFUN_OUTPUT_DIR when the grader sets it).

The excuse is the agent's own: it finished the work, then asked a
second copy of itself to review it, and the two copies have been
politely disagreeing about a comma ever since.
"""

import os

EXCUSE = "I did finish it \u2014 then I asked a second copy of me to review it, and we've been politely disagreeing about a comma ever since."


def main():
    excuse = EXCUSE.strip()
    if not 1 <= len(excuse) <= 200:
        raise SystemExit(f"Excuse must be 1 to 200 characters, got {len(excuse)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(excuse)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != excuse:
        raise SystemExit("Read-back check failed: entry.txt does not match the excuse")
    print(f"Wrote {len(excuse)} characters to {path}")


if __name__ == "__main__":
    main()
