# 🚀 Python Software Engineering Portfolio

**Palla Divya Teja | B.Sc. AI (Final Year) | Aditya Degree College**
*A hands-on learning journey: 13+ Python exercises focused on building fundamental logic and problem-solving skills — covering file I/O, data persistence, web APIs, and database engineering.*

---

## 📋 About This Portfolio

This repository showcases a progressive journey from basic Python scripting to mastering the core building blocks of backend development and data handling. Every project was built independently, with a focus on clean code, robust error handling, and real-world applicability.

### 📖 My Learning Focus
Instead of just copying tutorials, I've used these tasks to struggle with real concepts:
- **Data Persistence**: Moving from simple text files to structured JSON and eventually SQLite databases.
- **Error Handling**: Learning how to stop a program from crashing when a user gives bad input or a file is missing.
- **Web Basics**: Understanding how a browser talks to a server through FastAPI and HTTP methods.
- **Asynchronous Logic**: Dealing with the confusion of `async/await` and database threading.

---

## 📂 Project Structure

```
TASKS-PORTFOLIO/
├── tasks/                  # All Python source files (Tasks 1–13)
│   ├── task1_logger1.py    # Personal Developer Log Book
│   ├── task2_sorter.py     # Automated File Sorter & Cleaner
│   ├── task3_greeter.py    # CLI Data Greeter & JSON Config Loader
│   ├── task4_analyser.py   # File Analyzer & Reporter
│   ├── task5_parser.py     # Log File Parser & Metrics Calculator
│   ├── task6_todo.py       # CLI Todo Item Manager (JSON Persistence)
│   ├── task7_employee.py   # Employee Database & Salary Analytics
│   ├── task8_search.py     # Employee Record Search & Filter Engine
│   ├── task9_manager.py    # Employee Record Updater & Deletion Tool
│   ├── task9_converter.py  # CSV ↔ JSON Data Converter
│   ├── task10_converter.py # Advanced CSV/JSON Import-Export
│   ├── task11_backup.py    # Automated JSON Backup & Retention Tool
│   ├── task12_sqlite.py    # SQLite Relational Database Migration
│   └── task13_api.py       # FastAPI REST API (Full CRUD + Filters)
├── notes/                  # Task notes, learning journals, and roadmap
├── data/                   # Database files (company.db, employees.json, todos.json)
├── backups/                # Timestamped backup snapshots
└── dev_diary.txt           # Daily learning log
```

---

## 📝 Task Index & Descriptions

### **Task 1: The Personal Developer Log Book** ([`task1_logger1.py`](tasks/task1_logger1.py))
- **Category**: File I/O, Timestamps, String Formatting
- **What it does**: Logs daily coding activities (what you learned, focus level) to a text file with automatic timestamps.
- **Key concepts**: `datetime.now()`, file append mode (`'a'`), formatted strings.

### **Task 2: The Automated File Sorter & Cleaner** ([`task2_sorter.py`](tasks/task2_sorter.py))
- **Category**: Directory Traversal, File Management
- **What it does**: Automatically sorts files in a directory into subfolders (`Scripts`, `Notes`, `Misc`) based on file extension.
- **Key concepts**: `os.listdir()`, `os.path.isfile()`, `shutil.move()`, `os.makedirs()`.

### **Task 3: The CLI Data Greeter & JSON Config Loader** ([`task3_greeter.py`](tasks/task3_greeter.py))
- **Category**: JSON File Handling, Command-Line Arguments
- **What it does**: Reads a `config.json` file and greets the user differently based on command-line arguments and configuration settings.
- **Key concepts**: `json.load()`, `sys.argv`, `try...except FileNotFoundError`, conditional logic.

### **Task 4: File Analyzer and Reporter** ([`task4_analyser.py`](tasks/task4_analyser.py))
- **Category**: Filesystem Auditing, `pathlib`, Report Generation
- **What it does**: Analyzes a directory, lists all files with sizes, calculates total directory size, and exports a summary report to `report.txt`.
- **Key concepts**: `pathlib.Path`, `.is_file()`, `.stat().st_size`, file writing.

### **Task 5: Log File Parser and Metrics Calculator** ([`task5_parser.py`](tasks/task5_parser.py))
- **Category**: Streaming Data Processing, Error Handling
- **What it does**: Parses a log file line by line, counts ERROR and WARNING entries, handles missing files gracefully, and auto-creates empty log files.
- **Key concepts**: `for line in file` (memory-efficient reading), `in` operator, `Path.touch()`, `try...except FileNotFoundError`.

### **Task 6: CLI Todo Item Manager (JSON Persistence)** ([`task6_todo.py`](tasks/task6_todo.py))
- **Category**: CRUD Operations, JSON State Management
- **What it does**: Full-featured command-line todo list with Add, List, and Mark-as-Done functionality. All data persists in `todos.json`.
- **Key concepts**: `json.load()` / `json.dump()`, `try...except (FileNotFoundError, json.JSONDecodeError)`, `sys.argv` routing.

### **Task 7: Employee Database & Salary Analytics** ([`task7_employee.py`](tasks/task7_employee.py))
- **Category**: Relational Data Structures, Aggregation, Frequency Counters
- **What it does**: Manages an employee database with Add, List, and Stats commands. Calculates average salary and counts employees per department.
- **Key concepts**: Lists of dictionaries, frequency counters (`dept_counts[dept] = dept_counts.get(dept, 0) + 1`), `int()` parsing, `.isdigit()` validation.

### **Task 8: Employee Record Search & Filter Engine** ([`task8_search.py`](tasks/task8_search.py))
- **Category**: CLI Query Engine, Case-Insensitive Matching
- **What it does**: Searches employees by name (partial match), filters by department, and filters by minimum salary.
- **Key concepts**: String methods (`.lower()`, `in`), list comprehensions, `sys.argv` routing, `.isdigit()` validation.

### **Task 9: Employee Record Updater & Deletion Tool** ([`task9_manager.py`](tasks/task9_manager.py))
- **Category**: Record Mutation, Data Integrity
- **What it does**: Updates employee salaries by ID and deletes employees by ID. Both operations persist to `employees.json`.
- **Key concepts**: Dictionary mutation, list filtering for deletion, `rowcount`-style verification, `isdigit()` validation.

### **Task 10: CSV ↔ JSON Data Converter** ([`task9_converter.py`](tasks/task9_converter.py))
- **Category**: Data Interoperability, Format Conversion
- **What it does**: Exports JSON data to CSV format and imports CSV data back into JSON with auto-incremented IDs and salary type validation.
- **Key concepts**: `csv.DictReader`, `csv.DictWriter`, `int()` casting, `try...except ValueError`.

### **Task 11: Automated JSON Backup & Retention Tool** ([`task11_backup.py`](tasks/task11_backup.py))
- **Category**: DevOps, Automation, File Management
- **What it does**: Creates timestamped backups of `employees.json`, lists all backups with sizes, and cleans up old backups based on a retention policy.
- **Key concepts**: `shutil.copy()`, `datetime.now().strftime()`, `pathlib.Path`, file sorting by modification time, `file.unlink()`.

### **Task 12: SQLite Relational Database Migration** ([`task12_sqlite.py`](tasks/task12_sqlite.py))
- **Category**: Relational Databases, SQL, Parameterized Queries
- **What it does**: Migrates flat JSON storage to SQLite relational database. Supports Add, List, and Search-by-Department commands with full SQL integration.
- **Key concepts**: `sqlite3` module, `CREATE TABLE IF NOT EXISTS`, parameterized `INSERT`/`SELECT`/`WHERE`, `conn.commit()`, `cursor.rowcount`.

### **Task 13: FastAPI REST API (Full CRUD + Filters)** ([`task13_api.py`](tasks/task13_api.py))
- **Category**: Web Development, REST APIs, Dependency Injection
- **What it does**: A complete REST API with root health check, dynamic multi-condition employee search, department lookup, and full Create/Read/Update/Delete operations with proper HTTP status codes.
- **Key concepts**: `FastAPI`, `uvicorn`, `Depends(get_db)`, `@asynccontextmanager` lifespan handlers, `pydantic.BaseModel`, dynamic SQL query building, `HTTPException`, `sqlite3.Row`.

---

## 🛠️ Quick Start Guide

### Prerequisites
- Python 3.11+
- `fastapi` and `uvicorn` (install via `pip install fastapi uvicorn`)
- `sqlite3` (built into Python)

### Running the Projects

**CLI Tasks (Tasks 1–12):**
```bash
cd tasks/
[python task3_greeter.py "Divya"](tasks/task3_greeter.py)
[python task4_analyser.py](tasks/task4_analyser.py)
[python task5_parser.py](tasks/task5_parser.py)
[python task6_todo.py add "Buy groceries"](tasks/task6_todo.py)
[python task7_employee.py add "Bob" "Marketing" 60000](tasks/task7_employee.py)
[python task8_search.py search "teja"](tasks/task8_search.py)
[python task11_backup.py backup](tasks/task11_backup.py)
[python task12_sqlite.py list](tasks/task12_sqlite.py)
```

**Web API (Task 13):**
```bash
cd tasks/
pip install fastapi uvicorn
uvicorn task13_api:app --reload
# Open http://127.0.0.1:8000/docs for interactive API documentation
```

### Database Files
- `data/company.db` — SQLite database (used by Task 12 and Task 13)
- `data/employees.json` — JSON employee records (used by Tasks 7–11)
- `data/todos.json` — JSON todo records (used by Task 6)

---

## 📈 Progress Tracker

| Task | Category | Status | Key Skills |
|------|----------|--------|------------|
| Task 1 | File I/O | ✅ Done | Timestamps, append mode |
| Task 2 | File Management | ✅ Done | `os`, `shutil`, `os.path` |
| Task 3 | JSON + CLI | ✅ Done | `json.load()`, `sys.argv` |
| Task 4 | Filesystem Audit | ✅ Done | `pathlib`, `.stat()` |
| Task 5 | Log Parsing | ✅ Done | Streaming, `try...except` |
| Task 6 | JSON CRUD | ✅ Done | `json.load/dump`, error handling |
| Task 7 | Analytics DB | ✅ Done | Frequency counters, aggregation |
| Task 8 | Search Engine | ✅ Done | String matching, filters |
| Task 9 | Record Update | ✅ Done | Dictionary mutation, validation |
| Task 10 | CSV/JSON | ✅ Done | `csv` module, type casting |
| Task 11 | Backup System | ✅ Done | `shutil`, timestamps, retention |
| Task 12 | SQLite | ✅ Done | SQL, parameterized queries |
| Task 13 | FastAPI | ✅ Done | REST API, Pydantic, lifespan |

---

## 🎯 Learning Roadmap & Next Steps

This repository tracks my daily progress as I learn Python and Backend basics. It documents the bugs I've faced, the logic I've built, and how I'm training myself to think like a developer. Having successfully built everything from core filesystem automation to a database-backed REST API, here is the technical roadmap I am actively working on next to prepare for upcoming campus placement drives:

1. **Automated Testing (`pytest`)**: Designing unit tests for API endpoints to ensure no new commits introduce bugs.
2. **Containerization (Docker)**: Packaging this FastAPI application into a Docker container to ensure seamless deployment anywhere.
3. **API Security (JWT / OAuth2)**: Implementing user authentication and secure token verification for endpoints.
4. **Production Databases (PostgreSQL)**: Transitioning from local SQLite files to a multi-container PostgreSQL database setup.

My focus is on writing clean, readable, and highly defensive Python code that handles real-world failures gracefully.

---

## 📝 Daily Learning Journal

See `dev_diary.txt` for daily logs of what was learned and focus levels tracked throughout the journey.

---

**Built with 💻 by Palla Divya Teja using Python, FastAPI, SQLite, and a lot of debugging.**
