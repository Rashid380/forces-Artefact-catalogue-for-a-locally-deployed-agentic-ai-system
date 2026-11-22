from crewai.tools import BaseTool
from pydantic import Field
import os


class CreateReportTool(BaseTool):
    name: str = "Create Report Tool"
    description: str = (
        "Creates a report text file."
    )

    output_folder: str = Field(default="output")

    def _run(self, filename: str, content: str) -> str:

        os.makedirs(self.output_folder, exist_ok=True)

        filepath = os.path.join(self.output_folder, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Successfully created {filepath}"