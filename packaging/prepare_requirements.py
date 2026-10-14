"""Keep Windows build compatibility overrides separate from runtime requirements."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
OVERRIDES = {
    "matplotlib": "matplotlib==3.10.8",
    "h5py": "h5py==3.15.1",
    "pyfar": "pyfar==0.8.0",
}


def requirements():
    for line in (ROOT / "requirements.txt").read_text().splitlines():
        name = re.split(r"[<>=!~\[;\s]", line, maxsplit=1)[0].lower()
        yield OVERRIDES.get(name, line)
    yield "pyinstaller==6.16.0"


if __name__ == "__main__":
    Path(sys.argv[1]).write_text("\n".join(requirements()) + "\n")
