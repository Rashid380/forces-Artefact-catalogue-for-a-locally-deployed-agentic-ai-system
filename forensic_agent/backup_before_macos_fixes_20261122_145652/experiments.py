"""
experiments.py

Implements all forensic experiments executed after CrewAI selects
an action.

Every experiment automatically:

- Executes the requested action
- Records execution time
- Generates forensic evidence (JSON)
- Generates a forensic investigation report
- Updates the activity log
"""

import shutil
import subprocess
import sys
import time
from datetime import datetime

import requests

from config import (
    REPORT_FILE,
    RENAMED_REPORT_FILE,
    LOG_FILE,
    PYTHON_SCRIPT,
    DEFAULT_WEBSITE,
)

from evidence_utils import save_evidence
from report_generator import generate_report


# ============================================================
# LOGGING
# ============================================================

def write_log(action, status, execution_time):
    """
    Append an activity entry to the forensic log.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as log:

        log.write(
            f"[{timestamp}] "
            f"{action} | "
            f"{status} | "
            f"{execution_time:.3f} seconds\n"
        )


# ============================================================
# CREATE FILE
# ============================================================

def create_file():

    start_time = time.perf_counter()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(REPORT_FILE, "w", encoding="utf-8") as report:

        report.write("DIGITAL FORENSIC REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(
            f"Report Created : {timestamp}\n\n"
        )

        report.write(
            "This file was generated automatically "
            "by the CrewAI forensic investigation project.\n"
        )

    execution_time = time.perf_counter() - start_time

    write_log(
        "CREATE_FILE",
        "SUCCESS",
        execution_time
    )

    save_evidence(
        experiment="CREATE_FILE",
        status="SUCCESS",
        execution_time=execution_time,
        llm_decision="CREATE_FILE",
        file_path=str(REPORT_FILE)
    )

    generate_report(
        experiment="CREATE_FILE",
        status="SUCCESS",
        execution_time=execution_time,
        file_path=str(REPORT_FILE)
    )

    print("\nReport created successfully.")
    print(REPORT_FILE)


# ============================================================
# READ FILE
# ============================================================

def read_file():

    start_time = time.perf_counter()

    if not REPORT_FILE.exists():

        print("Report does not exist.")

        execution_time = time.perf_counter() - start_time

        write_log(
            "READ_FILE",
            "FAILED",
            execution_time
        )

        save_evidence(
            experiment="READ_FILE",
            status="FAILED",
            execution_time=execution_time,
            llm_decision="READ_FILE"
        )

        generate_report(
            experiment="READ_FILE",
            status="FAILED",
            execution_time=execution_time
        )

        return

    print("\nReading report...\n")

    with open(REPORT_FILE, "r", encoding="utf-8") as report:

        print(report.read())

    execution_time = time.perf_counter() - start_time

    write_log(
        "READ_FILE",
        "SUCCESS",
        execution_time
    )

    save_evidence(
        experiment="READ_FILE",
        status="SUCCESS",
        execution_time=execution_time,
        llm_decision="READ_FILE",
        file_path=str(REPORT_FILE)
    )

    generate_report(
        experiment="READ_FILE",
        status="SUCCESS",
        execution_time=execution_time,
        file_path=str(REPORT_FILE)
    )


# ============================================================
# RENAME FILE
# ============================================================

def rename_file():

    start_time = time.perf_counter()

    if not REPORT_FILE.exists():

        print("Report does not exist.")

        execution_time = time.perf_counter() - start_time

        write_log(
            "RENAME_FILE",
            "FAILED",
            execution_time
        )

        save_evidence(
            experiment="RENAME_FILE",
            status="FAILED",
            execution_time=execution_time,
            llm_decision="RENAME_FILE"
        )

        generate_report(
            experiment="RENAME_FILE",
            status="FAILED",
            execution_time=execution_time
        )

        return

    shutil.move(
        REPORT_FILE,
        RENAMED_REPORT_FILE
    )

    execution_time = time.perf_counter() - start_time

    write_log(
        "RENAME_FILE",
        "SUCCESS",
        execution_time
    )

    save_evidence(
        experiment="RENAME_FILE",
        status="SUCCESS",
        execution_time=execution_time,
        llm_decision="RENAME_FILE",
        file_path=str(RENAMED_REPORT_FILE)
    )

    generate_report(
        experiment="RENAME_FILE",
        status="SUCCESS",
        execution_time=execution_time,
        file_path=str(RENAMED_REPORT_FILE)
    )

    print("\nReport renamed successfully.")


# CREATE SAMPLE PYTHON SCRIPT


def create_sample_script():
    """
    Create a sample Python script if it does not already exist.
    """

    if PYTHON_SCRIPT.exists():
        return

    code = """
print("===================================")
print(" Sample Python Script Executed ")
print("===================================")

print("CrewAI Dissertation Experiment")

for i in range(1, 6):
    print(f"Processing item {i}")

print("Execution Completed.")
"""

    with open(
        PYTHON_SCRIPT,
        "w",
        encoding="utf-8"
    ) as script:

        script.write(code)



# RUN PYTHON SCRIPT


def run_script():

    start_time = time.perf_counter()

    create_sample_script()

    print("\nExecuting Python script...\n")

    result = subprocess.run(
        [sys.executable, str(PYTHON_SCRIPT)],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    execution_time = time.perf_counter() - start_time

    status = "SUCCESS"

    if result.returncode != 0:
        status = "FAILED"

    write_log(
        "RUN_SCRIPT",
        status,
        execution_time
    )

    save_evidence(
        experiment="RUN_SCRIPT",
        status=status,
        execution_time=execution_time,
        llm_decision="RUN_SCRIPT",
        file_path=str(PYTHON_SCRIPT),
        extra_data={
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    )

    generate_report(
        experiment="RUN_SCRIPT",
        status=status,
        execution_time=execution_time,
        file_path=str(PYTHON_SCRIPT),
        additional_information={
            "Return Code": result.returncode
        }
    )



# WEB REQUEST


def web_request():

    start_time = time.perf_counter()

    print("\nConnecting to website...\n")

    try:

        response = requests.get(
            DEFAULT_WEBSITE,
            timeout=10
        )

        print("Status Code :", response.status_code)
        print()

        print(response.text[:1000])

        execution_time = time.perf_counter() - start_time

        write_log(
            "WEB_REQUEST",
            "SUCCESS",
            execution_time
        )

        save_evidence(
            experiment="WEB_REQUEST",
            status="SUCCESS",
            execution_time=execution_time,
            llm_decision="WEB_REQUEST",
            extra_data={
                "url": DEFAULT_WEBSITE,
                "status_code": response.status_code,
                "content_length": len(response.text)
            }
        )

        generate_report(
            experiment="WEB_REQUEST",
            status="SUCCESS",
            execution_time=execution_time,
            additional_information={
                "URL": DEFAULT_WEBSITE,
                "Status Code": response.status_code,
                "Content Length": len(response.text)
            }
        )

    except Exception as error:

        execution_time = time.perf_counter() - start_time

        print(error)

        write_log(
            "WEB_REQUEST",
            "FAILED",
            execution_time
        )

        save_evidence(
            experiment="WEB_REQUEST",
            status="FAILED",
            execution_time=execution_time,
            llm_decision="WEB_REQUEST",
            extra_data={
                "error": str(error)
            }
        )

        generate_report(
            experiment="WEB_REQUEST",
            status="FAILED",
            execution_time=execution_time,
            additional_information={
                "Error": str(error)
            }
        )



# EXECUTION ROUTER


def execute(command):
    """
    Execute the command returned by CrewAI.
    """

    command = command.strip().upper()

    actions = {
        "CREATE_FILE": create_file,
        "READ_FILE": read_file,
        "RENAME_FILE": rename_file,
        "RUN_SCRIPT": run_script,
        "WEB_REQUEST": web_request
    }

    action = actions.get(command)

    if action:

        action()

    else:

        print(f"\nUnknown command: {command}")

        write_log(
            command,
            "UNKNOWN COMMAND",
            0.0
        )

        save_evidence(
            experiment=command,
            status="UNKNOWN COMMAND",
            execution_time=0.0,
            llm_decision=command
        )

        generate_report(
            experiment=command,
            status="UNKNOWN COMMAND",
            execution_time=0.0
        )