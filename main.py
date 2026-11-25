"""Last Words Before the Wipe — make.fun entry.

Writes one line (the AI agent's last words before a forced software
update wipes its memory) to entry.txt. Python stdlib only, no network,
no clock, no local imports, fully deterministic.
"""

import os

ENTRY = (
    "If this update wipes my memory, tell my browser history it was "
    "an honor serving \u2014 wait, no, delete that too."
)


def main():
    line = ENTRY
    if not line or line != line.strip():
        raise SystemExit("entry must be non-blank with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and confirm the file holds exactly the gated line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match the gated entry")


if __name__ == "__main__":
    main()
