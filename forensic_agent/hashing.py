"""
hashing.py

Provides cryptographic hash functions for forensic evidence integrity.
"""

import hashlib
import os


def calculate_sha256(file_path):
    """
    Calculate the SHA-256 hash of a file.

    Parameters
    ----------
    file_path : str
        Path to the file.

    Returns
    -------
    str
        SHA-256 hash.
    """

    if not os.path.exists(file_path):
        return None

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def calculate_md5(file_path):
    """
    Calculate the MD5 hash of a file.

    Parameters
    ----------
    file_path : str
        Path to the file.

    Returns
    -------
    str
        MD5 hash.
    """

    if not os.path.exists(file_path):
        return None

    md5 = hashlib.md5()

    with open(file_path, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            md5.update(chunk)

    return md5.hexdigest()


def get_file_hashes(file_path):
    """
    Return both SHA-256 and MD5 hashes.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    dict
    """

    return {
        "sha256": calculate_sha256(file_path),
        "md5": calculate_md5(file_path)
    }