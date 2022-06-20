import typer

import bin.projects

import util.logger as logger
import repository.mongodb as mongodb_utils

aufgabe_app = typer.Typer()

MODULES = {
	"project" : bin.projects
}

def add_modules():
    for pair in MODULES.items():
        module_name = str(list(pair)[0])
        module = list(pair)[1].aufgabe_module
        aufgabe_app.add_typer(module, name=module_name)


class TestClass:
    def __init__(self, a, b, c):
        self.longer = a
        self.b = b
        self.c = c

@aufgabe_app.command()
def test():
    logger.echo_tabular([
		TestClass(1,2,3000), TestClass(4,5,6), TestClass(200, 400, 300)
	], primary_prop='longer')

@aufgabe_app.command()
def check():
    pass

def main(command: str):
	# echo_logo()
	typer.secho(f"you inserted {str(command)}")

if __name__ == "__main__":
    add_modules()
    aufgabe_app()