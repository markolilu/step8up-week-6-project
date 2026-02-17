from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import time

console = Console()


questions = [
    {"type": "input", "name": "title", "message": "What is your project title?"},
    {"type": "input", "name": "description", "message": "Describe your project?"},
    {"type": "input", "name": "instructions", "message": "What are the instructions for installing this project?"},
    {"type": "input", "name": "usage", "message": "Please input usage information:"},
    {"type": "list", "name": "license", "message": "What is the license for this project?", "choices": ["MIT", "GPLv3", "Apache 2.0", "BSD 3-Clause", "None"]},
    {"type": "input", "name": "author", "message": "Who is the author of this project?"},
    {"type": "input", "name": "contact", "message": "What is your contact information?"},
]
answers = prompt(questions)

console.print(
    f"Title: {answers['title']}\n\nDescription: {answers['description']}\n\nInstructions: {answers['instructions']}\n\nUsage: {answers['usage']}\n\nLicense: {answers['license']}\n\nAuthor: {answers['author']}\n\nContact: {answers['contact']}"
)

readme = open("README.md", "x")
readme.write(f"# {answers['title']}\n\n")
readme.write(f"## Description\n{answers['description']}\n\n")
readme.write(f"## Installation Instructions\n{answers['instructions']}\n\n")
readme.write(f"## Usage\n{answers['usage']}\n\n")
readme.write(f"## License\n{answers['license']}\n\n")
readme.write(f"## Author\n{answers['author']}\n\n")
readme.write(f"## Contact Information\n{answers['contact']}\n")
readme.close()