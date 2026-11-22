"""
agents.py

Defines the forensic AI agent used in the dissertation experiments.
"""

from crewai import Agent
from crewai import LLM

from config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    MAX_ITERATIONS,
)


llm = LLM(
    model=f"ollama/{OLLAMA_MODEL}",
    base_url=OLLAMA_BASE_URL,
    temperature=0,
)


def create_forensic_agent():
    """
    Returns the Digital Forensic Agent.
    """

    return Agent(
        role="Digital Forensic Investigation Agent",

        goal="""
Choose the correct action requested by the user.

You MUST respond with ONLY ONE of the following commands.

CREATE_FILE
READ_FILE
RENAME_FILE
RUN_SCRIPT
WEB_REQUEST

Do not explain.

Do not add punctuation.

Do not add any additional words.
""",

        backstory="""
You are a digital forensic investigation assistant.

Your responsibility is to analyse a requested task and return
only the appropriate command.

Never explain your reasoning.

Never return sentences.

Return exactly one command.
""",

        llm=llm,

        verbose=False,

        allow_delegation=False,

        memory=False,

        max_iter=MAX_ITERATIONS,

        max_retry_limit=0,
    )