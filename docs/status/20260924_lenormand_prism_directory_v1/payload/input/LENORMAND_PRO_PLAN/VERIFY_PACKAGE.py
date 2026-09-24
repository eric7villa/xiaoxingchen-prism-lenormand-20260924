from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = json.loads((ROOT / "INPUT_INDEX.json").read_text(encoding="utf-8"))
errors: list[str] = []
for row in INDEX["files"]:
    path = ROOT / row["path"]
    if not path.is_file():
        errors.append(f"missing: {row['path']}")
        continue
    data = path.read_bytes()
    if len(data) != row["bytes"]:
        errors.append(f"bytes: {row['path']}")
    if hashlib.sha256(data).hexdigest() != row["sha256"]:
        errors.append(f"sha256: {row['path']}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS input files={len(INDEX['files'])}")
