#!/usr/bin/env python3
"""news-image-20261118 entrypoint (Python 3.13, standard library only).

The repository holds the finished image as entry.png; this program copies
it to /output/entry.png. Outside the grader, MAKEFUN_OUTPUT_DIR stands in
for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = HERE / "entry.png"

if not SOURCE.is_file():
    sys.exit(f"entry.png not found beside {__file__}")

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, OUT_DIR / "entry.png")
