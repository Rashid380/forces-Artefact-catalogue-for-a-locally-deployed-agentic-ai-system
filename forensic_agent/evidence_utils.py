"""
evidence_utils.py

Creates structured forensic evidence for each experiment.
"""

import json
import os
from datetime import datetime

from config import EVIDENCE_DIR
from hashing import get_file_hashes
from system_info import get_system_information


def get_file_metadata(file_path):
    """
    Collect metadata for a file.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    dict
    """

    if file_path is None or not os.path.exists(file_path):

        return {
            "exists": False
        }

    stats = os.stat(file_path)

    metadata = {
        "exists": True,
        "filename": os.path.basename(file_path),
        "absolute_path": os.path.abspath(file_path),
        "size_bytes": stats.st_size,
        "created": datetime.fromtimestamp(
            stats.st_ctime
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "modified": datetime.fromtimestamp(
            stats.st_mtime
        ).strftime("%Y-%m-%d %H:%M:%S")
    }

    metadata.update(
        get_file_hashes(file_path)
    )

    return metadata


def save_evidence(
    experiment,
    status,
    execution_time,
    llm_decision,
    file_path=None,
    extra_data=None
):
    """
    Save forensic evidence as a JSON file.

    Parameters
    ----------
    experiment : str

    status : str

    execution_time : float

    llm_decision : str

    file_path : str

    extra_data : dict
    """

    run_id = datetime.now().strftime("%Y%m%dT%H%M%S_%f")

    evidence = {

        "run_id": run_id,

        "experiment": experiment,

        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "status": status,

        "execution_time_seconds": round(
            execution_time,
            3
        ),

        "llm_decision": llm_decision,

        "system_information": get_system_information(),

        "file_metadata": get_file_metadata(
            file_path
        )
    }

    if extra_data:

        evidence["additional_information"] = extra_data

    filename = experiment.lower().replace(
        " ",
        "_"
    )

    evidence_file = os.path.join(
        EVIDENCE_DIR,
        f"{filename}_{run_id}.json"
    )

    with open(
        evidence_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            evidence,
            file,
            indent=4
        )

    return evidence_file