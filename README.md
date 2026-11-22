# Agentic AI Digital Forensic Investigation Prototype

A small research prototype that uses CrewAI with a locally hosted Ollama model to select one of five predefined actions. Python code then performs the selected action and records application-level evidence.

The project is intended for controlled demonstrations and exploratory research. Its generated records are not a substitute for forensic acquisition or independent examination of a host.

## What it does

The interactive menu offers five actions:

1. Create a sample forensic report file.
2. Read the sample report file.
3. Rename the sample report file.
4. Run a sample Python script.
5. Send a test HTTP request to `https://example.com`.

CrewAI returns one of five fixed action labels. The Python application dispatches that label to the corresponding handler. The model does not independently examine a disk image, memory image, packet capture, or registry hive.

For each action, the application records a status and execution time, appends an activity log entry, and writes a timestamped JSON evidence record. File operations also record file metadata and SHA-256 and MD5 digests where a file is available. The HTTP action requires an internet connection.

## Technology and tested environment

- Python 3.12
- CrewAI 1.15.5
- Ollama with the `llama3.2:3b` model
- macOS on Apple Silicon for the recorded run

The dissertation also discusses a Windows test environment. The Mac run documented here is a separate application-level demonstration; it is not a controlled comparison of Mac and Windows forensic artefacts.

## Requirements

- macOS with Python 3.12 available as `python3.12`
- [Ollama](https://ollama.com/) installed and running locally
- The `llama3.2:3b` Ollama model
- Internet access for the web-request experiment

The project’s Python dependencies are pinned in `requirements.txt`.

## Setup on macOS

From the project directory, create and activate a virtual environment, then install the dependencies:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Check that Ollama is available and that the required model is installed:

```bash
ollama list
```

If `llama3.2:3b` is not listed, download it:

```bash
ollama pull llama3.2:3b
```

If Ollama is not already running, start it in a separate Terminal window and leave that window open:

```bash
ollama serve
```

## Run

From the project directory, with the virtual environment active, run:

```bash
CREWAI_TRACING_ENABLED=false python main.py
```

The environment variable disables CrewAI tracing for this process. The menu appears in Terminal. Select an action by entering its number. To run the full sequence, create the file first, then read it, rename it, run the sample script, and finally perform the web request:

```text
1 → 2 → 3 → 4 → 5
```

After each action, enter `Y` to return to the menu. After the final action, enter `N` to exit. The read and rename actions require the sample file to have been created first. The rename action moves `forensic_report.txt` to `forensic_report_renamed.txt`.

## Generated files

The application creates these folders in the project directory if they do not already exist:

- `evidence/` — timestamped per-run JSON records and the latest `system_information.json`.
- `logs/activity.log` — appended action, status, and runtime entries.
- `output/` — sample files and timestamped investigation reports.
- `scripts/` — the sample script used by the script-execution action.

Use the JSON record for the task’s recorded status and details. The menu’s general “Experiment completed successfully” message alone is not enough to establish that an individual action succeeded; for example, a read or rename action can record `FAILED` if its input file is missing or empty.

To inspect the latest records and output files on macOS:

```bash
ls -lt evidence | head -n 10
ls -lh output
```

To independently check the hash of a renamed sample file:

```bash
shasum -a 256 output/forensic_report_renamed.txt
```

Compare the printed SHA-256 value with the corresponding `sha256` value in the create, read, and rename JSON records for that run.

## Evidence and interpretation limits

- A successful menu action shows that the application handler ran and recorded an outcome. It does not, by itself, prove that a corresponding operating-system artefact was acquired or attributed correctly.
- The JSON records describe application-level observations. Independent verification requires examining the underlying file or relevant operating-system evidence.
- Execution times in JSON are rounded to three decimal places. A displayed `0.000` means the measured time rounded below one millisecond, not that the action took no time.
- The sample script is a demonstration script, not malware or an incident-response simulation.
- The web-request action is a connectivity test to `example.com`, not a simulated incident.
- A single successful run does not establish repeatability, detection accuracy, or generalisation to other models, operating systems, or forensic tools.
- This prototype does not provide the complete standardised Forensic Artefact Catalogue proposed for the dissertation.

## Privacy before publishing

Evidence records may contain the local username, hostname, absolute project path, timestamps, and file hashes. Review and sanitise generated evidence, logs, output files, and screen recordings before publishing them to a public repository. Do not commit credentials, personal files, virtual environments, or unreviewed system-specific evidence.

## Project structure

```text
forensic_agent/
├── agents.py           # CrewAI agent and local Ollama model configuration
├── config.py           # Model settings and project paths
├── crew_setup.py       # CrewAI workflow setup
├── evidence_utils.py   # Timestamped JSON evidence records
├── experiments.py      # Python action handlers and evidence generation
├── hashing.py          # File hash calculation
├── main.py             # Interactive command-line menu
├── report_generator.py # Text investigation report generation
├── system_info.py      # Host and runtime information collection
├── tasks.py            # Prompts and allowed action labels
├── tools.py            # CrewAI file tool
├── requirements.txt    # Pinned Python dependencies
├── evidence/           # Generated JSON evidence (created at runtime)
├── logs/               # Generated activity log (created at runtime)
├── output/             # Generated sample files and reports
└── scripts/            # Sample script (created or used at runtime)
```
