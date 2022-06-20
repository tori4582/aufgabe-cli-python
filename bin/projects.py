
import typer
import repository.project_repo as project_repo
import util.logger

from modal.Project import Project
from util.logger import Logger


aufgabe_module = typer.Typer()

COLOR_ID = typer.colors.BRIGHT_YELLOW

@aufgabe_module.command()
def create(name, desc = typer.Option('')):
    prj = Project(name, desc)
    object_id = project_repo.add(prj)
    Logger.info("Project created with id: " + typer.style(prj.id, fg=COLOR_ID))
    Logger.debug("Stored in database with ObjectId: " + typer.style(object_id.inserted_id, fg=typer.colors.BRIGHT_WHITE))

@aufgabe_module.command()
def remove(project_id: str):
    prj = project_repo.get(project_id)

    if prj is NoneType:
        Logger.error("Project with given id is not existed")
        return

    Logger.warn("Project with id " + typer.style(str(prj['id']), fg=COLOR_ID) + " will be removed! Please retype the id to confirm deletion")
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
    for project in result:
        prj = Project(project['name'], project['description'])
        prj.id = project['id']
        projects.append(prj)

    util.logger.echo_tabular(projects, primary_prop='name')

if __name__ == "__main__":
    aufgabe_module()
