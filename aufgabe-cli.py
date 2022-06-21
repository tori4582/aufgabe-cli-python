import typer

import bin.projects

import util.logger as logger
import repository.mongodb as mongodb_utils

import config.globalvars as glbvars
from util.logger import Logger

aufgabe_app = typer.Typer()

MODULES = {
	"project" : bin.projects
}

def add_modules():
    for pair in MODULES.items():
        module_name = str(list(pair)[0])
        module = list(pair)[1].aufgabe_module
        aufgabe_app.add_typer(module, name=module_name)

@aufgabe_app.command()
def check():
    pass

@aufgabe_app.command()
def checkout(project_id):
    bin.projects.checkout(project_id)

def main(command: str):
	# echo_logo()
	typer.secho(f"you inserted {str(command)}")

if __name__ == "__main__":
    add_modules()
    aufgabe_app()