import shutil
import sys
from pathlib import Path


def copy_and_process(src, dst):
    if src.is_file():
        n = src.name
        t = dst / (n[5:] if n.startswith(("head.", "tail.")) else n)
        c = src.read_text()
        if n.startswith("head."):
            print(f"Prepending file: {src} -> {t}")
            t.write_text(c + t.read_text())
        elif n.startswith("tail."):
            print(f"Appending file: {src} -> {t}")
            t.write_text(t.read_text() + c)
        else:
            print(f"Copying file: {src} -> {t}")
            shutil.copy2(src, t)
    elif src.is_dir():
        target_dir = dst / src.name
        print(f"Processing directory: {src} -> {target_dir}")
        target_dir.mkdir(exist_ok=True)
        for item in src.iterdir():
            copy_and_process(item, target_dir)


src_path = Path(sys.argv[1])
dst_path = Path(sys.argv[2])

print(f"Starting process: {src_path} -> {dst_path}")

for f in src_path.iterdir():
    copy_and_process(f, dst_path)

print("Process completed")
