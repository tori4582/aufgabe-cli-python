
import typer

aufgabe_module = typer.Typer()

PROJECTS_NAME = ['hehe', 'boiz', 'bruh']

@aufgabe_module.command()
def list():
    for i in range(len(PROJECTS_NAME)):
        typer.echo(str(i) + "\t" + typer.style(PROJECTS_NAME[i], fg=typer.colors.CYAN, bold=True))

if __name__ == "__main__":
    aufgabe_module()