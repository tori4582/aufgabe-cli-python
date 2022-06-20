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
            + ' - ' + typer.style(state, fg=Logger.STATE_COLORS[state], bold=True) + " : " + str(text)
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

def echo_tabular(objs: list, primary_prop: str = ''):

    if len(objs) == 0:
        Logger.error('There is no elements to print')

    len_dict = {}

    for obj in objs:
        for prop, val in obj.__dict__.items():
            if prop not in len_dict:
                len_dict[prop] = max(len(str(val)), len(str(prop)))
            else:
                len_dict[prop] = max(len_dict[prop], len(str(val)))

    max_lens = list(len_dict.values())

    tabular_formatter = ["{:<" + str(len(str(len(objs)))) + "}"]
    seperator = " " * len(str(len(objs))) + "  "
    for i in max_lens:
        tabular_formatter.append("{:<" + str(i) + "}")
        seperator += "-"*i + "  "

    tabular_formatter_str = '  '.join(tabular_formatter)
    tabular_header = list(len_dict.keys())
    tabular_header.insert(0, "")

    Logger.debug(tabular_formatter_str)

    typer.secho(tabular_formatter_str.format(*tabular_header), fg=typer.colors.CYAN, bold=True)
    typer.secho(seperator, fg=typer.colors.CYAN)
    for i in range(len(objs)):
        output = [typer.style(str(i), fg=typer.colors.CYAN)]
        counter = 0
        for prop, val in objs[i].__dict__.items():
            value = str(val)
            if prop == primary_prop:
                output.append(typer.style(value, fg=typer.colors.GREEN, bold=True)
                              + (" " * (max_lens[counter] - len(value)))
                )
            else:
                output.append(value)
            counter += 1

        typer.echo(tabular_formatter_str.format(*output))

    typer.echo("\nThe table contains "
               + typer.style(len(objs), fg=typer.colors.BRIGHT_WHITE, bold=True)
               + " object rows and "
               + typer.style(len(max_lens), fg=typer.colors.BRIGHT_WHITE, bold=True)
               + " attribute columns."
    )

def echo_obj(obj):
    pass
