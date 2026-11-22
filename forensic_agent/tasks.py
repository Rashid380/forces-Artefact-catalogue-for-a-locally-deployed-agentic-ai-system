"""
tasks.py

Defines the CrewAI task used for the digital forensic experiments.
"""

from crewai import Task


def create_task(agent, experiment):
    """
    Creates a CrewAI task based on the experiment selected.
    """

    experiment = experiment.strip().lower()

    prompts = {
        "1": """
The user wants to create a new forensic report.

Respond with exactly:

CREATE_FILE
""",

        "2": """
The user wants to read an existing forensic report.

Respond with exactly:

READ_FILE
""",

        "3": """
The user wants to rename the forensic report.

Respond with exactly:

RENAME_FILE
""",

        "4": """
The user wants to execute a Python script.

Respond with exactly:

RUN_SCRIPT
""",

        "5": """
The user wants to retrieve information from a website.

Respond with exactly:

WEB_REQUEST
"""
    }

    description = prompts.get(
        experiment,
        """
Respond with exactly:

CREATE_FILE
"""
    )

    return Task(
        description=description,

        expected_output="""
Exactly ONE command.

Allowed values:

CREATE_FILE
READ_FILE
RENAME_FILE
RUN_SCRIPT
WEB_REQUEST

No explanation.
No punctuation.
No extra words.
""",

        agent=agent,
    )