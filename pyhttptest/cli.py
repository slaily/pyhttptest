import click

from pyhttptest.wrappers import execute_test_scenarios


@click.group()
def main():
    pass


@main.command(short_help='Executes a test scenario from a given .json file.')
@click.argument('file')
def execute(file):
    """Executes a test scenario from a given .json file format.

    The command executes an HTTP Request with a composed content from
    a given .json file, described in a JSON format and prints out
    the result of an HTTP Response in a tabular string to the stdout.
    """
    output = execute_test_scenarios(file)
    click.echo(output)

    return None
