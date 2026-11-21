"""Organize files in a folder by file type. Standard library only."""
from pathlib import Path
import argparse
import csv
import shutil
from datetime import datetime



CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"},
    "Spreadsheets": {".csv", ".xls", ".xlsx", ".ods"},
    "Presentations": {".ppt", ".pptx", ".odp"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json", ".xml"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}
REPORTS_DIR_NAME = "reports"



def categorize(file_path: Path) -> str:
    """Return the folder category for a file based on its extension."""
    suffix = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if suffix in extensions:
            return category
    return "Others"



def unique_destination(destination: Path) -> Path:
    """Return a destination path that will not overwrite an existing file."""
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(f"{destination.stem}_{counter}{destination.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1



def write_csv_report(folder: Path, rows: list[dict]) -> Path:
    """Write a timestamped CSV report into the folder's reports subdirectory."""
    report_folder = folder / REPORTS_DIR_NAME
    report_folder.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = report_folder / f"file_organizer_report_{timestamp}.csv"
    fields = ["File", "Category", "Action", "Destination", "Details"]
    with report_path.open("w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return report_path



def organize(folder_path: Path, apply_changes: bool = False) -> int:
    """Preview or move files in the selected folder. Returns number of successful moves."""
    folder = folder_path.expanduser().resolve()
    if not folder.exists():
        print(f"ERROR: Folder does not exist: {folder}")
        return 1
    if not folder.is_dir():
        print(f"ERROR: Path is not a folder: {folder}")
        return 1

    rows = []
    successful_moves = 0
    files = sorted((p for p in folder.iterdir() if p.is_file()), key=lambda p: p.name.lower())
    if not files:
        print("No files found at the top level of this folder.")
        return 0

    print("FILE ORGANIZER - " + ("APPLY MODE" if apply_changes else "PREVIEW MODE"))
    print("=" * 55)
    for source in files:
        category = categorize(source)
        target_folder = folder / category
        destination = unique_destination(target_folder / source.name)
        if not apply_changes:
            print(f"[PREVIEW] {source.name} -> {category}/{destination.name}")
            rows.append({"File": source.name, "Category": category, "Action": "Preview only", "Destination": str(destination), "Details": "No file moved"})
            continue
        try:
            target_folder.mkdir(exist_ok=True)
            destination = unique_destination(target_folder / source.name)
            shutil.move(str(source), str(destination))
            successful_moves += 1
            print(f"[MOVED] {source.name} -> {category}/{destination.name}")
            rows.append({"File": source.name, "Category": category, "Action": "Moved", "Destination": str(destination), "Details": "Success"})
        except OSError as exc:
            print(f"[ERROR] Could not move {source.name}: {exc}")
            rows.append({"File": source.name, "Category": category, "Action": "Failed", "Destination": str(destination), "Details": str(exc)})

    print("\nSummary")
    print(f"Files checked: {len(files)}")
    if apply_changes:
        print(f"Files moved successfully: {successful_moves}")
        try:
            report_path = write_csv_report(folder, rows)
            print(f"CSV report saved: {report_path}")
        except OSError as exc:
            print(f"WARNING: Could not create report: {exc}")
        print("Done. Check the folders and report above.")
    else:
        print("Preview only: no files were changed.")
        print("To move files, rerun this command with --apply.")
    return 0



def main() -> int:
    parser = argparse.ArgumentParser(description="Sort files in a folder into file-type categories.")
    parser.add_argument("folder", help="Path to the folder containing files to organize")
    parser.add_argument("--apply", action="store_true", help="Actually move files (without this, preview only)")
    args = parser.parse_args()
    return organize(Path(args.folder), apply_changes=args.apply)



if __name__ == "__main__":
    raise SystemExit(main())
