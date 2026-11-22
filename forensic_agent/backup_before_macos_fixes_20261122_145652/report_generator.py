"""
report_generator.py

Generates a human-readable forensic investigation report.
"""

import os
from datetime import datetime

from config import REPORT_FILE
from hashing import get_file_hashes
from system_info import get_system_information


def generate_report(
    experiment,
    status,
    execution_time,
    file_path=None,
    additional_information=None
):
    """
    Generate a forensic investigation report.

    Parameters
    ----------
    experiment : str

    status : str

    execution_time : float

    file_path : str

    additional_information : dict
    """

    system = get_system_information()

    hashes = {}

    if file_path and os.path.exists(file_path):
        hashes = get_file_hashes(file_path)

    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as report:

        report.write("=" * 70 + "\n")
        report.write("DIGITAL FORENSIC INVESTIGATION REPORT\n")
        report.write("=" * 70 + "\n\n")

        report.write(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        report.write(
            f"Experiment: {experiment}\n"
        )

        report.write(
            f"Status: {status}\n"
        )

        report.write(
            f"Execution Time: {execution_time:.3f} seconds\n\n"
        )

        report.write("-" * 70 + "\n")
        report.write("SYSTEM INFORMATION\n")
        report.write("-" * 70 + "\n")

        report.write(
            f"Operating System : {system['operating_system']}\n"
        )

        report.write(
            f"Hostname         : {system['hostname']}\n"
        )

        report.write(
            f"Username         : {system['username']}\n"
        )

        report.write(
            f"Python Version   : {system['python_version']}\n"
        )

        report.write(
            f"Ollama Model     : {system['ollama_model']}\n"
        )

        report.write(
            f"Working Directory: {system['working_directory']}\n\n"
        )

        if file_path:

            report.write("-" * 70 + "\n")
            report.write("EVIDENCE INFORMATION\n")
            report.write("-" * 70 + "\n")

            report.write(
                f"Evidence File : {file_path}\n"
            )

            if os.path.exists(file_path):

                report.write(
                    f"File Size     : {os.path.getsize(file_path)} bytes\n"
                )

                report.write(
                    f"SHA-256       : {hashes['sha256']}\n"
                )

                report.write(
                    f"MD5           : {hashes['md5']}\n"
                )

            else:

                report.write(
                    "Evidence file not found.\n"
                )

            report.write("\n")

        if additional_information:

            report.write("-" * 70 + "\n")
            report.write("ADDITIONAL INFORMATION\n")
            report.write("-" * 70 + "\n")

            for key, value in additional_information.items():

                report.write(
                    f"{key}: {value}\n"
                )

            report.write("\n")

        report.write("-" * 70 + "\n")
        report.write("SUMMARY\n")
        report.write("-" * 70 + "\n")

        report.write(
            "The experiment completed successfully and the associated "
            "digital evidence was collected. File integrity information "
            "was calculated using cryptographic hash functions, and the "
            "system environment was recorded to support forensic analysis "
            "and reproducibility.\n"
        )

        report.write("\n")
        report.write("=" * 70 + "\n")
        report.write("End of Report\n")
        report.write("=" * 70 + "\n")