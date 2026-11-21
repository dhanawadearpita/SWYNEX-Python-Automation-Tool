# SWYNEX Python Automation Tool — Smart File Organizer

A beginner-friendly Python command-line automation tool that sorts files into folders based on their extensions. It includes a safe preview mode, collision-safe file naming, and a CSV activity report.


## Features
- Categorizes common file formats (images, documents, spreadsheets, presentations, videos, audio, code, archives, and other files).
- Preview mode is the default: files are **not moved** unless `--apply` is supplied.
- Creates category folders automatically when applying.
- Avoids overwriting files by adding a numeric suffix to duplicate names.
- Produces a timestamped CSV report when applying.
- Uses only Python's standard library (no package installation needed).
- Handles missing folder paths and file-move errors with messages.


## Requirements
- Python 3.8 or newer (Python 3.9+ recommended)
- Windows, macOS, or Linux
- No third-party libraries required


## Project structure
```text
SWYNEX-Python-Automation-Tool/
├── file_organizer.py
├── README.md
├── requirements.txt
├── LINKEDIN_POST.md
├── VIDEO_SCRIPT.md
├── UPLOAD_GUIDE.md
├── sample_files/          # harmless sample files for testing
└── screenshots/            # add your real screenshots here
```


## How to use

### 1. Preview (safe; does not move files)
Open a terminal in the project folder and run:

```bash
python file_organizer.py "C:\Users\YourName\Desktop\Automation_Test"
```
Replace the sample path with the folder you want to test. The preview lists planned destinations without changing files.

### 2. Apply (moves files)
After reviewing the preview, run:

```bash
python file_organizer.py "C:\Users\YourName\Desktop\Automation_Test" --apply
```
This creates category folders, moves files, and writes a report under `reports/` inside the selected folder.

### 3. Sample project files
You can test using the included `sample_files` folder. Copy it to a separate location before applying so the repository's sample files remain unchanged.


## Categories
| Folder | Extensions (examples) |
|---|---|
| Images | JPG, JPEG, PNG, GIF, BMP, WEBP, SVG |
| Documents | PDF, DOC, DOCX, TXT, RTF, ODT |
| Spreadsheets | CSV, XLS, XLSX, ODS |
| Presentations | PPT, PPTX, ODP |
| Videos | MP4, MKV, MOV, AVI, WEBM |
| Audio | MP3, WAV, AAC, FLAC, OGG |
| Code | PY, JS, HTML, CSS, JAVA, C, CPP, JSON, XML |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Others | Extensions not listed above |


## Report
The CSV report contains the file name, category, action, destination path, and details. Report names include a timestamp to reduce accidental overwriting.


## Safety notes
- Test with a temporary folder first, not your main Downloads folder.
- The program only checks files directly inside the selected folder; it does not recursively process subfolders.
- Preview first. The `--apply` flag is required to move files.
- Keep backups of important files.


## Learning outcomes
- Python functions and dictionaries
- File and folder handling with `pathlib`
- File moves using `shutil`
- Command-line argument parsing with `argparse`
- CSV report generation
- Basic error handling and safe automation design


## Internship task
Prepared as a Python automation project for Task 2. Please test the program yourself, capture real screenshots, and include your own GitHub repository URL in your LinkedIn post and task submission.
