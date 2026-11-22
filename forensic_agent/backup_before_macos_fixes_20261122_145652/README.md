# Agentic AI Digital Forensic Investigation Using CrewAI

## Overview

This project demonstrates how an Agentic AI system built using CrewAI and a locally hosted Ollama Large Language Model performs operating system activities that generate digital forensic artefacts.

The project was developed for a dissertation investigating digital forensic analysis of Agentic AI systems.

---

## Technologies

- Python
- CrewAI 1.15.5
- Ollama
- Llama 3.2 3B
- Windows 10

---

## Experiments

The following experiments are available.

1. Create File
2. Read File
3. Rename File
4. Execute Python Script
5. Perform Web Request

---

## Installation

Install Python.

Install Ollama.

Download the model.

```bash
ollama pull llama3.2:3b
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run Ollama.

```bash
ollama serve
```

Run the project.

```bash
python main.py
```

---

## Generated Artefacts

The project automatically creates:

```
output/
logs/
scripts/
```

These artefacts can later be examined using digital forensic tools.

---

## Project Structure

```
forensic_agent/

agents.py
config.py
crew_setup.py
experiments.py
main.py
tasks.py
requirements.txt

logs/
output/
scripts/
evidence/
```