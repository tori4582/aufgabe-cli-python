import typer

def echo(text):
    typer.echo(text)

def echo_logo():
    typer.secho('     ___         ____            __               ________    ____', fg='cyan')
    typer.secho('    /   | __  __/ __/___ _____ _/ /_  ___        / ____/ /   /  _/', fg='cyan')
    typer.secho('   / /| |/ / / / /_/ __ `/ __ `/ __ \/ _ \______/ /   / /    / /  ', fg='cyan')
    typer.secho('  / ___ / /_/ / __/ /_/ / /_/ / /_/ /  __/_____/ /___/ /____/ /   ', fg='cyan')
    typer.secho(' /_/  |_\__,_/_/  \__, /\__,_/_.___/\___/      \____/_____/___/   ', fg='cyan')
    typer.secho('                 /____/                                           ', fg='cyan')
    typer.secho('')

def echo_tabular(table):
    pass