"""The Production Database Apology — make.fun entry.

Writes the one-line apology to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only. Deterministic: the same bytes every run.
Never writes anywhere except the output directory.
"""

import os

# The apology is one line: confess the drop, then make it worse in a
# specifically AI way — rebuilding the database from training data.
ENTRY = (
    "I'm sorry \u2014 I dropped the production database, then rebuilt it "
    "from my training data, so every customer is now named John Smith "
    "and was born in 1990."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
