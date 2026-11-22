"""
main.py

Main entry point for the Agentic AI Digital Forensic Investigation project.
"""

from crew_setup import run_experiment
from experiments import execute


def show_menu():
    """Display the main menu."""

    print("\n" + "=" * 60)
    print(" AGENTIC AI DIGITAL FORENSIC INVESTIGATION")
    print("=" * 60)
    print("1. Create Forensic Report")
    print("2. Read Forensic Report")
    print("3. Rename Forensic Report")
    print("4. Execute Python Script")
    print("5. Perform Web Request")
    print("0. Exit")
    print("=" * 60)


def get_choice():
    """Get a valid menu selection."""

    while True:

        choice = input("Select an experiment: ").strip()

        if choice in ["0", "1", "2", "3", "4", "5"]:
            return choice

        print("Invalid selection. Please try again.\n")


def main():

    while True:

        show_menu()

        choice = get_choice()

        if choice == "0":
            print("\nExiting project...")
            break

        print("\nRunning CrewAI...\n")

        try:

            command = run_experiment(choice)

        except Exception as error:

            print("\nCrewAI failed to execute.")
            print(error)
            continue

        print("\n" + "=" * 60)
        print("CrewAI Decision")
        print("=" * 60)
        print(command)
        print("=" * 60)

        valid_commands = [
            "CREATE_FILE",
            "READ_FILE",
            "RENAME_FILE",
            "RUN_SCRIPT",
            "WEB_REQUEST",
        ]

        if command not in valid_commands:

            print("\nUnexpected response received from CrewAI.")
            print("Returned value:", command)

        else:

            execute(command)

        print("\nExperiment completed successfully.")

        while True:

            again = input("\nRun another experiment? (Y/N): ").strip().upper()

            if again in ["Y", "N"]:
                break

            print("Please enter Y or N.")

        if again == "N":

            print("\nThank you for using the system.")
            break


if __name__ == "__main__":
    main()