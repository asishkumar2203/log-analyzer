# 🔍 Log File Analyzer

This Python script reads and analyzes application log files for useful insights such as:
- Number of log entries by level (INFO, ERROR, WARN, etc.)
- Number of log entries per service
- Most common error message

---


## 🚀 How to Run

### 1. Prerequisites

- Python 3.6 or higher

Check your Python version:
```bash
python --version

### Navigate to the project folder where app.log and log_analyzer.py are located and run:

python log_analyzer.py

### The script will output a JSON-formatted summary like:

{
    "log_levels": {
        "INFO": 5,
        "ERROR": 3,
        "WARN": 2,
        "DEBUG": 1
    },
    "services": {
        "ServiceA": 3,
        "ServiceB": 4,
        "ServiceC": 2,
        "ServiceD": 1,
        "ServiceE": 1
    },
    "most_common_error": {
        "message": "Null pointer exception",
        "count": 2
    }
}
