"""
    Move tv show files around so that everything is in the same season folder.
"""


import json
import os
import subprocess
import sys

from dotenv import load_dotenv
from pathlib import Path

# Custom service
sys.path.insert(1, "../../automations/services")
import telegram_apprise as telmes


load_dotenv()


# ===== CONFIGURATION =====

SOURCE_DISKS = [
    Path(str(os.getenv("DISK1"))),
    #Path(str(os.getenv("DISK2"))),
    Path(str(os.getenv("DISK3"))),
    Path(str(os.getenv("DISK4"))),
    #Path(str(os.getenv("DISK5"))),
]
DEST_DISK = Path(str(os.getenv("DEST_DISK")))
SERIES_BASE_PATH = Path(str(os.getenv("SERIES_BASE_PATH")))
SERIES_CONFIG = Path("series_config.json")

RSYNC_FLAGS = [
    "-avhP",
    "--itemize-changes",
    "--remove-source-files",
    "--prune-empty-dirs",
    "--log-file=rsync_migration.log",
]

DRY_RUN = False  # set to True to test safely

# =========================


def load_series_list() -> list[str]:
    """ Load the list of series from a JSON file. """

    if not SERIES_CONFIG.exists():
        telmes.message(f"❌ Config file not found: {SERIES_CONFIG}")
        sys.exit(0)

    with open(SERIES_CONFIG, "r") as file:
        config = json.load(file)

    return config.get("series", [])


def run_rsync(src: Path, dst: Path):
    """ Craft the rsync command that's needed. """

    cmd = ["rsync"]

    cmd.extend(RSYNC_FLAGS)

    if DRY_RUN:
        cmd.append("--dry-run")

    cmd.extend([str(src), str(dst)])

    print("\n🚀 Running:")
    print(" ".join(cmd))

    result = subprocess.run(cmd)

    if result.returncode != 0:
        telmes.message(f"❌ Command rsync failed for {src}")
        sys.exit(result.returncode)


def find_all_series(series_name: str) -> list[Path]:
    """Find all occurrences of a series across all disks."""

    found = []

    for disk in SOURCE_DISKS:
        candidate = disk / SERIES_BASE_PATH / series_name
        if candidate.exists():
            found.append(candidate)

    if found is None:
        telmes.message("❌ No series found")
        return None

    return found


def main():
    """ Make it all work together. """

    print("📋 Loading series list from JSON...")
    series_to_move = load_series_list()

    if not series_to_move:
        telmes.message("⚠️ No series found in config file")
        sys.exit(1)

    telmes.message(f"Found {len(series_to_move)} series to process\n")

    dest_series_root = DEST_DISK / SERIES_BASE_PATH
    dest_series_root.mkdir(parents=True, exist_ok=True)
    series_count = 0

    for series in series_to_move:
        series_count += 1
        show_num = f"({series_count}/{len(series_to_move)})"
        print(f"\n📺 Processing series: {series} {show_num}")

        source_paths = find_all_series(series)

        if not source_paths:
            print(f"⚠️  Not found on any source disk: {series}")
            continue

        for source_path in source_paths:
            print(f"📍 Found on: {source_path}")
            run_rsync(source_path, dest_series_root)

        telmes.message(f"✅ Completed: {series} {show_num}")

    telmes.message("\n🎉 All done!")


if __name__ == "__main__":
    main()
