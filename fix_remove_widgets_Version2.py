#!/usr/bin/env python3
"""
fix_remove_widgets.py

Usage:
  python fix_remove_widgets.py path/to/notebook1.ipynb [path/to/notebook2.ipynb ...]

This script:
- Creates a .bak backup for each notebook (same folder, filename + ".bak").
- Removes any 'widgets' key inside cell metadata and the top-level metadata.widgets key.
- Preserves all other notebook content (cells, outputs, execution counts, other metadata).
"""
import sys
from pathlib import Path
import shutil
import nbformat

def remove_widgets_from_notebook(path: Path) -> bool:
    if not path.exists():
        print(f"[SKIP] Not found: {path}")
        return False

    # Backup
    bak = path.with_suffix(path.suffix + ".bak")
    shutil.copy2(path, bak)
    print(f"[BACKUP] {path} -> {bak}")

    nb = nbformat.read(str(path), as_version=nbformat.NO_CONVERT)
    changed = False

    # Remove cell-level metadata.widgets
    for i, cell in enumerate(nb.get("cells", [])):
        meta = cell.get("metadata", {})
        if "widgets" in meta:
            del meta["widgets"]
            nb["cells"][i]["metadata"] = meta
            changed = True
            print(f"  - Removed metadata.widgets from cell {i}")

    # Remove top-level metadata.widgets
    top_meta = nb.get("metadata", {})
    if "widgets" in top_meta:
        del nb["metadata"]["widgets"]
        changed = True
        print("  - Removed top-level metadata.widgets")

    if changed:
        nbformat.write(nb, str(path))
        print(f"[PATCHED] {path}")
    else:
        print(f"[NO CHANGE] {path} (no metadata.widgets found)")

    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_remove_widgets.py notebook1.ipynb [notebook2.ipynb ...]")
        sys.exit(1)
    for p in sys.argv[1:]:
        remove_widgets_from_notebook(Path(p))

if __name__ == '__main__':
    main()