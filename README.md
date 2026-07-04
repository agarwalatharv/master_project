# 🚀 Master Task Manager (CLI Tool)

A lightweight, highly flexible Command-Line Interface (CLI) task tracking tool built in Python.

## 🛠️ What It Does
- **Permanent Storage:** Unlike basic scripts that wipe data on exit, this tool automatically generates and maintains a physical `tasks.txt` file so your progress is completely secure.
- **Smart File Routing:** Driven by `argparse` and `pathlib`, you can pass command-line arguments to save your task lists to any target directory or project workspace on your machine.
- **Error Resilient:** Built-in validation handles incorrect inputs or out-of-bounds numbers smoothly without crashing the terminal execution loop.

---

## 💻 How to Use It

Launch the script from your terminal using any of the following configurations:

### 1. Default Execution
Saves a standard `tasks.txt` file directly inside the current script directory:
```powershell
python main.py
