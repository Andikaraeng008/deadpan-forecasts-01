"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Gate: /output/entry.txt must be UTF-8 text of 1-160 characters
(this line is 141). One absurd but believable weather forecast for
an invented city, read like a deadpan TV meteorologist.

Writes to $MAKEFUN_OUTPUT_DIR (fallback /output) -- never to a
repo-local output/ dir, which the grader mounts read-only.
Deterministic: byte-identical output on every run.
"""

import os

LINE = "In Blorvenwick, expect 14 centimetres of sideways rain, gusts of 90 kilometres an hour, and one umbrella that has filed for early retirement."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
