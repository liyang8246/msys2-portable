import os
import shutil
import sys
from pathlib import Path


def copy_and_process(src, dst):
    if src.is_file():
        n = src.name
        t = dst / (n[5:] if n.startswith(("head.", "tail.")) else n)
        c = src.read_text()
        if n.startswith("head."):
            t.write_text(c + t.read_text())
        elif n.startswith("tail."):
            t.write_text(t.read_text() + c)
        else:
            shutil.copy2(src, t)
    elif src.is_dir():
        (dst / src.name).mkdir(exist_ok=True)
        for item in src.iterdir():
            copy_and_process(item, dst / src.name)


for f in Path(sys.argv[1]).iterdir():
    copy_and_process(f, Path(sys.argv[2]))
