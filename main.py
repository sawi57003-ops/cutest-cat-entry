#!/usr/bin/env python3
"""cutest-cat-01 entry for make.fun: "Draw the cutest cat".

The picture is stored in this repository as cat.png (a hand-drawn style
illustration of an orange kitten, 1024x1024 PNG, 662,389 bytes).
This program only copies those exact bytes to the output path, so every
run writes identical output: no network, no randomness, no timestamps.

Usage: python3 main.py [output-path]  (default: /output/entry.png)
"""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cat.png")
DST = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.png"

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))
