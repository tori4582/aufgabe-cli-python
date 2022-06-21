from curses import nl
from turtle import bgcolor
import typer
import time
import util.common

class Logger:

    STATE_COLORS = {
        'INFO' : typer.colors.GREEN,
        'DEBUG' : typer.colors.CYAN,
        'WARN' : typer.colors.YELLOW,
        'ERROR' : typer.colors.RED,
    }

    @staticmethod
    def convention_log(text, state='INFO'):
        return (
            typer.style(util.common.get_pretty_date(time.gmtime()), fg=typer.colors.BRIGHT_WHITE)
            + ' - ' + typer.style(state, fg=Logger.STATE_COLORS[state], bold=True)
            + " : " + str(text)
        )

    @staticmethod
    def info(text):
        output = Logger.convention_log(text)
        typer.echo(output)

    @staticmethod
    def debug(text):
        output = Logger.convention_log(text, 'DEBUG')
        typer.echo(output)

    @staticmethod
    def warn(text):
        output = Logger.convention_log(text, 'WARN')
        typer.echo(output)

    @staticmethod
    def error(text):
        output = Logger.convention_log(text, 'ERROR')
        typer.echo(output)


def echo_logo():
    typer.secho('     ___         ____            __               ________    ____', fg='cyan')
    typer.secho('    /   | __  __/ __/___ _____ _/ /_  ___        / ____/ /   /  _/', fg='cyan')
    typer.secho('   / /| |/ / / / /_/ __ `/ __ `/ __ \/ _ \______/ /   / /    / /  ', fg='cyan')
    typer.secho('  / ___ / /_/ / __/ /_/ / /_/ / /_/ /  __/_____/ /___/ /____/ /   ', fg='cyan')
    typer.secho(' /_/  |_\__,_/_/  \__, /\__,_/_.___/\___/      \____/_____/___/   ', fg='cyan')
    typer.secho('                 /____/                                           ', fg='cyan')
    typer.secho('')

def get_tabular_widths(objs: list):
    len_dict = {}

    for obj in objs:
        for prop, val in obj.__dict__.items():
            if prop not in len_dict:
                len_dict[prop] = max(len(str(val)), len(str(prop)))
            else:
                len_dict[prop] = max(len_dict[prop], len(str(val)))

    return len_dict

def get_tabular_formatter(objs: list):
    len_dict = get_tabular_widths(objs)

    max_lens = list(len_dict.values())

    tabular_formatter = ["{:<" + str(len(str(len(objs)))) + "}"]
    for i in max_lens:
        tabular_formatter.append("{:<" + str(i) + "}")

    return ('  '.join(tabular_formatter))


def echo_tabular_header(objs: list):

    if len(objs) == 0:
        Logger.info('There is no elements to print')
        return

    len_dict = get_tabular_widths(objs)
    max_lens = list(len_dict.values())

    seperator = " " * len(str(len(objs))) + "  "

    for i in max_lens:
        seperator += "-"*i + "  "

    tabular_header = list(len_dict.keys())
    tabular_header.insert(0, "")

    tabular_formatter = get_tabular_formatter(objs)

    typer.secho(tabular_formatter.format(*tabular_header), fg=typer.colors.CYAN, bold=True)
    typer.secho(seperator, fg=typer.colors.CYAN)


def echo_tabular(objs: list, primary_prop: str = '', selected_lines=[]):

    if len(objs) == 0:
        Logger.info('There is no elements to print')
        return

    max_lens = list(get_tabular_widths(objs).values())
    tabular_formatter = get_tabular_formatter(objs)

    typer.echo()
    echo_tabular_header(objs)

    for i in range(len(objs)):

        bgcolor = typer.colors.BRIGHT_BLUE if i in selected_lines else None

        typer.secho(
            str(i) + '  ',
            fg=typer.colors.CYAN if (bgcolor is None) else typer.colors.BLUE,
            bg=typer.colors.BRIGHT_WHITE if (bgcolor is not None) else None,
            bold=(bgcolor is not None),
            nl=False)
        counter = 0
        for prop, val in objs[i].__dict__.items():
            value = '{0:<{1}}'.format(str(val), max_lens[counter])

            typer.secho(
                value + ('  ' if counter < len(objs[i].__dict__.items()) - 1 else ''),
                fg=typer.colors.GREEN if prop == primary_prop else None,
                bold=(prop == primary_prop),
                bg=bgcolor,
                nl=False
            )
            counter += 1

        typer.echo()

    typer.echo("\nThe table contains "
               + typer.style(len(objs), fg=typer.colors.BRIGHT_WHITE, bold=True)
               + " object rows and "
               + typer.style(len(max_lens), fg=typer.colors.BRIGHT_WHITE, bold=True)
               + " attribute columns."
    )

def echo_dict(d: dict, indent=1):
    typer.echo("{")
    for k, v in d.items():
        typer.echo(
            ("    " * indent)
            + typer.style('"' + str(k) + '"', fg=typer.colors.GREEN)
            + " : ",
            nl=False
        )
        if isinstance(v, dict):
            echo_dict(v, indent = indent + 1)
        elif isinstance(v, str):
            typer.secho('"' + v + '"', fg=typer.colors.BRIGHT_RED, nl=False)
        else:
            typer.echo(v, nl=False)

        typer.echo(',')

    typer.echo('}')

