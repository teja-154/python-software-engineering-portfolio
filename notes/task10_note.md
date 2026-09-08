---
task_id: 10
date: 2026-08-31
difficulty: Intermediate
status: Incomplete
---

# Task 10: CSV Exporter & Importer for Employee Records

## Why a Recruiter Cares
JSON is great for software state and web APIs, but business stakeholders and data analysts work in **Excel and CSVs**. A key skill for backend developers, data engineers, and AI developers is data format conversion—taking data stored in JSON, exporting it to CSV, and importing user-provided CSV data back into the system's JSON storage with validation.

## Specifications
Create a new Python script named `task10_converter.py` that handles CSV export and import operations on your `employees.json` database:

1. **Export JSON to CSV**: 
   * Command usage: `python task10_converter.py export employees.csv`
   * Should read `employees.json` and export all employee records into a CSV file named `employees.csv` using Python's built-in `csv` module (with header row: `id,name,department,salary`).
2. **Import CSV to JSON**: 
   * Command usage: `python task10_converter.py import new_employees.csv`
   * Should read an input CSV file (formatted with `name,department,salary`), parse each row, assign an auto-incremented ID, append them to `employees.json`, and save back to disk.
3. **Robust Error Handling**:
   * If the input CSV file does not exist during import, catch `FileNotFoundError` and print a clean error message.
   * If the CSV contains invalid salary numbers, handle the `ValueError` cleanly per row without crashing the entire script.
   * Check argument lengths and show helpful usage instructions if invalid commands are provided.

## Concepts to Research
* [`csv`](https://docs.python.org/3/library/csv.html) module (`csv.writer`, `csv.DictWriter`, `csv.reader`, `csv.DictReader`).
* Converting CSV string values to proper Python data types (e.g., converting salary string `"50000"` to integer `50000`).
* File handling for both JSON and CSV files in a single script workflow.

## Self-Verification Checklist
- [ ] **Export Test**: Run `export employees.csv`. Open the generated CSV file in Notepad or VS Code to verify headers and data rows.
- [ ] **Import Test**: Create a small CSV file named `import_test.csv` containing a couple of new employees. Run `import import_test.csv`. Check `employees.json` to verify the new records were added with valid auto-incremented IDs!
- [ ] **Missing File Test**: Try importing a non-existent file (`python task10_converter.py import fake.csv`). Does it catch the error cleanly?
