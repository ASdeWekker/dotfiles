"""
    Move tv show files around so that everything is in the same season folder.
"""

import subprocess
import sys
from pathlib import Path

# ===== CONFIGURATION =====

SOURCE_DISKS = [
    Path(""),  # ex /mnt/media1
    Path(""),
    Path(""),
    Path(""),
    Path(""),
]

DEST_DISK = Path("")

SERIES_BASE_PATH = Path("")

SERIES_TO_MOVE = [
]

RSYNC_FLAGS = [
    "-avhP",
    "--itemize-changes",
    "--remove-source-files",
    "--prune-empty-dirs",
    "--log-file=rsync_migration.log",
]

DRY_RUN = False  # set to True to test safely

# =========================


def run_rsync(src: Path, dst: Path):
    cmd = ["rsync"]

    cmd.extend(RSYNC_FLAGS)

    if DRY_RUN:
        cmd.append("--dry-run")

    cmd.extend([str(src), str(dst)])

    print("\n🚀 Running:")
    print(" ".join(cmd))

    result = subprocess.run(cmd)

    if result.returncode != 0:
        print(f"❌ rsync failed for {src}")
        sys.exit(result.returncode)


def find_series(series_name: str) -> Path | None:
    for disk in SOURCE_DISKS:
        candidate = disk / SERIES_BASE_PATH / series_name
        if candidate.exists():
            return candidate
    return None


def main():
    dest_series_root = DEST_DISK / SERIES_BASE_PATH
    dest_series_root.mkdir(parents=True, exist_ok=True)

    for series in SERIES_TO_MOVE:
        print(f"\n📺 Processing series: {series}")

        source_path = find_series(series)

        if not source_path:
            print(f"⚠️  Not found on any source disk: {series}")
            continue

        for source_path in source_path:
            print(f"📍 Found on: {source_path}")
            run_rsync(source_path, dest_series_root)

        print(f"✅ Completed: {series}")

    print("\n🎉 All done!")


if __name__ == "__main__":
    main()
