"""
system_info.py

Collects system information for forensic evidence generation.
"""

import json
import os
import platform
import socket
import getpass
from datetime import datetime

from config import EVIDENCE_DIR, OLLAMA_MODEL


SYSTEM_INFO_FILE = os.path.join(
    EVIDENCE_DIR,
    "system_information.json"
)


def collect_system_information():
    """
    Collect system information.

    Returns
    -------
    dict
        Dictionary containing forensic system information.
    """

    information = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "hostname": socket.gethostname(),
        "username": getpass.getuser(),
        "python_version": platform.python_version(),
        "working_directory": os.getcwd(),
        "ollama_model": OLLAMA_MODEL
    }

    return information


def save_system_information():
    """
    Save system information as JSON.

    Returns
    -------
    str
        Path to the generated JSON file.
    """

    information = collect_system_information()

    with open(
        SYSTEM_INFO_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            information,
            file,
            indent=4
        )

    return SYSTEM_INFO_FILE


def get_system_information():
    """
    Return system information.

    Generates the file automatically if it does not exist.
    """

    if not os.path.exists(SYSTEM_INFO_FILE):
        save_system_information()

    with open(
        SYSTEM_INFO_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)