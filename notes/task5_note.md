---
task_id: 5
date: 2026-08-28
difficulty: Intermediate
status: Incomplete
---

# Task 5: Log File Parser and Metrics Calculator

## Why a Recruiter Cares
In production environments, applications generate massive amounts of log data. Being able to parse these files to identify critical events (like "ERROR" vs "INFO"), filter out noise, and calculate metrics (e.g., "how many errors happened in the last hour?") is an essential skill for SREs, MLOps, and Backend Engineers. This task simulates real-world data processing.

## Specifications
Create a Python script (`task5_parser.py`) that performs the following:

1. **Input**: Accept a log file path as an argument. If no argument is provided, default to a file named `application.log` in the current directory.
2. **Parsing**: Read the log file line by line.
3. **Filtering & Counting**:
    * Count the total number of lines.
    * Identify and count lines that contain the word "ERROR".
    * Identify and count lines that contain the word "WARNING".
4. **Report Generation**: Print a summary to the terminal that includes:
    * Total lines processed.
    * Number of "ERROR" entries found.
    * Number of "WARNING" entries found.
5. **Robust Error Handling**:
    * Handle `FileNotFoundError` if the log file doesn't exist.
    * Print a polite message if the file is empty.

## Concepts to Research
* String methods like `.contains()` (actually, use the `in` operator in Python).
* File reading modes (read only).
* Counters/Accumulators (simple variables that increase in a loop).

## Self-Verification Checklist
- [ ] **Empty File Test**: Create an empty `application.log`. Does your script report 0 lines processed?
- [ ] **No File Test**: Run the script with a filename that doesn't exist. Does it handle the `FileNotFoundError`?
- [ ] **Metric Accuracy**: Create a sample log file with known counts of ERROR/WARNING lines. Does your script output the correct counts?
