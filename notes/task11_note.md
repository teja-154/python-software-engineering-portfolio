---
task_id: 11
date: 2026-08-31
difficulty: Intermediate-Advanced
status: Incomplete
---

# Task 11: Automated JSON Backup & Retention Policy Tool

## Why a Recruiter Cares
In production IT and software engineering, **data safety and disaster recovery** are absolute requirements. Systems must automatically create timestamped backups of critical configuration or database files (like JSON, SQLite, or configuration stores) to prevent accidental data loss. Furthermore, automated housekeeping (retention policies) ensures that backup folders don't bloat and consume 100% of the server's disk space over time.

## Specifications
Create a new Python script named `task11_backup.py` that manages backups and retention policies for your `employees.json` file:

1. **Create Timestamped Backup**: 
   * Command usage: `python task11_backup.py backup`
   * Should copy `employees.json` into a dedicated `backups/` directory (auto-creating the directory if it doesn't exist) with a timestamped filename, e.g., `employees_backup_20260831_153000.json`.
2. **List Existing Backups**: 
   * Command usage: `python task11_backup.py list`
   * Should list all files inside the `backups/` directory, displaying their names and file sizes in bytes.
3. **Retention Policy (Cleanup)**: 
   * Command usage: `python task11_backup.py clean 3`
   * Should sort the backups by creation time (newest to oldest), keep only the specified number of recent backups (e.g., `3`), and **delete the older backup files** to save disk space.
4. **Robust Error Handling**:
   * If `employees.json` does not exist when trying to make a backup, catch the error and print a clear message.
   * If the `backups/` directory is empty when running `list` or `clean`, handle it gracefully.
   * Validate terminal arguments (e.g., ensuring `clean` receives a valid integer for the count).

## Concepts to Research
* [`shutil`](https://docs.python.org/3/library/shutil.html) module (`shutil.copy()`) for copying files.
* [`datetime`](https://docs.python.org/3/library/datetime.html) module (`datetime.now().strftime("%Y%m%d_%H%M%S")`) for generating clean timestamps.
* Sorting files by modification/creation time using `pathlib` (`sorted(folder.iterdir(), key=lambda f: f.stat().st_mtime, reverse=True)`).

## Self-Verification Checklist
- [ ] **Backup Test**: Run `python task11_backup.py backup` multiple times. Check that a `backups/` folder is created containing timestamped copies of `employees.json`.
- [ ] **List Test**: Run `python task11_backup.py list`. Does it display all backup files and their sizes?
- [ ] **Cleanup Test**: Run `python task11_backup.py clean 2`. Does it successfully keep only the 2 newest backups and delete the rest?
- [ ] **Missing File Test**: Temporarily rename `employees.json` and try to run `backup`. Does it catch the error cleanly?
