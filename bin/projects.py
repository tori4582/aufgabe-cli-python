
from asyncio.log import logger
from types import NoneType
from numpy import select
import typer
import repository.project_repo as project_repo
import util.logger

from modal.Project import Project
from util.logger import Logger
import config.globalvars as glbvars

aufgabe_module = typer.Typer()

COLOR_ID = typer.colors.BRIGHT_YELLOW

@aufgabe_module.command()
def create(name, desc = typer.Option('')):
    Logger.debug("name:" + str(name))
    prj = Project(str(name), desc)
    object_id = project_repo.add(prj)
    Logger.info("Project created with id: " + typer.style(prj.id, fg=COLOR_ID))
    Logger.debug("Stored in database with ObjectId: "
                 + typer.style(object_id.inserted_id, fg=typer.colors.BRIGHT_WHITE))

@aufgabe_module.command()
def remove(project_id: str):
    prj = project_repo.get(project_id)

    if prj is NoneType:
        Logger.error("Project with given id is not existed")
        return

    Logger.warn("Project with id " + typer.style(str(prj['id']), fg=COLOR_ID)
                + " will be removed! Please retype the id to confirm deletion")

    confirmation = typer.prompt('Confirmation', type=str)
    if confirmation == prj['id']:
        result = project_repo.remove(project_id)
        Logger.info("Project with id " + typer.style(project_id, fg=COLOR_ID)
                    + " and named " + typer.style('"' + prj['name'] + '"', fg=typer.colors.CYAN)
                    + " has been removed")
    else:
        Logger.info("Action is terminated due to cancellation of confirmation")


@aufgabe_module.command()
def show():
    result = list(project_repo.getall())
    projects = []
    selected_lines = []
    checked_project_id = glbvars.vars_read('project')
    checked_project = None

    counter = 0
    for project in result:

        prj = Project(project['name'], project['description'])
        prj.id = project['id']
        projects.append(prj)

        if project['id'] == checked_project_id:
            selected_lines.append(counter)
            checked_project = prj

        counter += 1

    util.logger.echo_tabular(projects, primary_prop='name', selected_lines=selected_lines)

    if checked_project is not None:
        typer.echo("You are now checked in the project:")
        util.logger.echo_dict(checked_project.__dict__)
    else:
        typer.echo("You are not in any project")


def checkout(project_id):

    if project_id == glbvars.vars_read('project'):
        Logger.warn('Project is already checked out. There is no need to reattempt action')
        return

    prj = project_repo.get(project_id)

    if isinstance(prj, NoneType):
        Logger.error("Project with given id is not existed")
        return None

    glbvars.vars_write('project', prj.id)
    Logger.info("Switched to project " + typer.style(project_id, fg=bin.projects.COLOR_ID))
    logger.echo_dict(prj.__dict__)

if __name__ == "__main__":
    aufgabe_module()
