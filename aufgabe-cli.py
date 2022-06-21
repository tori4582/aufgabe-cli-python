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
    prj = bin.projects.checkout(project_id)

    if prj.id == glbvars.vars_read('project'):
        Logger.warn('Project is already checked out. There is no need to reattempt action')
        return

    glbvars.vars_write('project', prj.id)
    Logger.info("Switched to project " + typer.style(project_id, fg=bin.projects.COLOR_ID))
    logger.echo_dict(prj.__dict__)

def main(command: str):
	# echo_logo()
	typer.secho(f"you inserted {str(command)}")

if __name__ == "__main__":
    add_modules()
    aufgabe_app()