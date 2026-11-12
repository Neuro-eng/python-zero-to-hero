import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Documents": {".pdf", ".docx", ".txt", ".xlsx", ".pptx"},
    "Code": {".py", ".js", ".html", ".css", ".json"},
    "Archives": {".zip", ".tar", ".gz", ".rar"},
}


def category_for(path):
    ext = Path(path).suffix.lower()
    for name, exts in CATEGORIES.items():
        if ext in exts:
            return name
    return "Other"


def organize(folder, dry_run=False):
    folder = Path(folder)
    moves = []
    for item in folder.iterdir():
        if item.is_file():
            dest_dir = folder / category_for(item)
            moves.append((item, dest_dir / item.name))
    for src, dest in moves:
        print(f"{src.name} -> {dest.parent.name}/")
        if not dry_run:
            dest.parent.mkdir(exist_ok=True)
            if dest.exists():
                dest = dest.with_name(f"{dest.stem}_copy{dest.suffix}")
            shutil.move(str(src), str(dest))
    return moves


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("folder")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    organize(a.folder, a.dry_run)
