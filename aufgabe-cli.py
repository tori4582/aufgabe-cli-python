import typer

import bin.projects

from util.logger import echo_logo
import util.mongodb as mongodb_utils

aufgabe_app = typer.Typer()

MODULES = {
	"project" : bin.projects
}

def add_modules():
    for pair in MODULES.items():
        module_name = str(list(pair)[0])
        module = list(pair)[1].aufgabe_module
        aufgabe_app.add_typer(module, name=module_name)

def main(command: str):
	# echo_logo()
	typer.secho(f"you inserted {str(command)}")

if __name__ == "__main__":
    add_modules()
    aufgabe_app()