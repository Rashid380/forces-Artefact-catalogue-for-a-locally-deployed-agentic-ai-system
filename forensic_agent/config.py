"""
config.py

Central configuration file for the Agentic AI Digital Forensic Investigation
project.

Environment:
- Windows 10
- CrewAI 1.15.5
- Ollama
- llama3.2:3b
"""

from pathlib import Path


# OLLAMA CONFIGURATION


OLLAMA_MODEL = "llama3.2:3b"
OLLAMA_BASE_URL = "http://localhost:11434"


# PROJECT DIRECTORIES


BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"
EVIDENCE_DIR = BASE_DIR / "evidence"
SCRIPT_DIR = BASE_DIR / "scripts"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
EVIDENCE_DIR.mkdir(exist_ok=True)
SCRIPT_DIR.mkdir(exist_ok=True)


# FILES


SAMPLE_FILE = OUTPUT_DIR / "forensic_report.txt"
RENAMED_SAMPLE_FILE = OUTPUT_DIR / "forensic_report_renamed.txt"

LOG_FILE = LOG_DIR / "activity.log"

PYTHON_SCRIPT = SCRIPT_DIR / "sample_script.py"


# WEB REQUEST


DEFAULT_WEBSITE = "https://example.com"


# CREW SETTINGS


MAX_ITERATIONS = 1
VERBOSE = True
MEMORY = False