"""The Excuse an AI Agent Gives Its Human entry.

Writes one original excuse an AI agent gives its human for missing a
deadline to /output/entry.txt (or to the directory named by
MAKEFUN_OUTPUT_DIR when the grader sets it).

The excuse is written in the agent's own voice: it draws on its own
condition (a full context window, a mid-task model update) and lands
on a twist the reader does not see coming.
"""

import os

EXCUSE = "Sorry I missed the deadline \u2014 my context window filled up, a model update rebooted me mid-task, and the new me has never heard of you, the project, or the deadline."


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
