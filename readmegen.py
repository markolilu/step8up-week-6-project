from rich.table import Table


def mDGen(answers):
    readme = open("README.md", "x")
    readme.write(f"# {answers['title']}\n\n")
    readme.write(f"## Description\n{answers['description']}\n\n")
    readme.write(f"## Installation Instructions\n{answers['instructions']}\n\n")
    readme.write(f"## Usage\n{answers['usage']}\n\n")
    readme.write(f"## License\n{answers['license']}\n\n")
    readme.write(f"## Author\n{answers['author']}\n\n")
    readme.write(f"## Contact Information\n{answers['contact']}\n")
    readme.close()

    table = Table(title="Sample Data")
    table.add_column("Title", justify="center", style="cyan")
    table.add_column("Description",justify="center", style="magenta")
    table.add_column("Instructions", justify="center", style="green")
    table.add_column("Usage", justify="center", style="blue")
    table.add_column("License", justify="center", style="yellow")
    table.add_column("Author", justify="center", style="red")
    table.add_column("Contact", justify="center", style="blue")

    table.add_row(answers['title'], answers['description'], answers['instructions'], answers['usage'], answers['license'], answers['author'], answers['contact'])

    return table