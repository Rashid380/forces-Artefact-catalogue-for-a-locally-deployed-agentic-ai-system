"""
crew_setup.py

Creates the CrewAI workflow.
"""

from crewai import Crew
from crewai import Process

from agents import create_forensic_agent
from tasks import create_task


def run_experiment(experiment):
    """
    Creates and executes a CrewAI workflow.

    Parameters
    ----------
    experiment : str

        1 - Create File
        2 - Read File
        3 - Rename File
        4 - Run Script
        5 - Web Request
    """

    agent = create_forensic_agent()

    task = create_task(
        agent=agent,
        experiment=experiment
    )

    crew = Crew(

        agents=[
            agent
        ],

        tasks=[
            task
        ],

        process=Process.sequential,

        verbose=False,

        memory=False

    )

    result = crew.kickoff()

    return str(result).strip()