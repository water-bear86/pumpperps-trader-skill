#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    py = sys.executable

    validate_cmd = [py, str(root / "scripts" / "quick_validate.py")]
    trader_cmd = [
        py,
        str(root / "scripts" / "trader_loop.py"),
        "--dashboard",
        "--dry-run",
        "--no-prompts",
        "--cycles",
        "0",
    ]
    trader_cmd.extend(sys.argv[1:])

    subprocess.run(validate_cmd, cwd=str(root), check=True)
    os.execvpe(py, trader_cmd, os.environ)


if __name__ == "__main__":
    raise SystemExit(main())
