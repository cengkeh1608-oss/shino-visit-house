#!/usr/bin/env python3
"""Copy the pre-rendered invitation image to the output directory.

The letter image (entry.png) is rendered at build time and committed with
this program. At run time this script only copies it to /output/entry.png
using the standard library, so it runs in a plain python:3.13 sandbox
with no network and no third-party packages.
"""

import os
import shutil
import sys


def main():
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR", ".")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    src = os.path.join(bot_dir, "entry.png")
    if not os.path.isfile(src):
        print("missing entry.png next to main.py", file=sys.stderr)
        sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
