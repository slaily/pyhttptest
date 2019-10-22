import click

from pyhttptest import core


@click.group()
def main():
    pass


@main.command(short_help='Executes a test scenario from a given .json file.')
@click.argument('file')
def execute(file):
    """Executes a test scenario from a given .json file format.

    The command executes an HTTP Request with a composed content from
    a given .json file, described in a specific format and prints out
    the result of an HTTP Response to the stdout.
    """
    try:
        json_file_data = core.load_json_from_file(file)
        required_args, optional_kwargs = core.extract_json_data(json_file_data)
        http_method, url = core.prepare_request_args(*required_args)
        response = core.send_http_request(http_method, url)
        response_content = core.extract_http_response_content(response)
        # Add a JSON property 'name' in the content
        response_content['name'] = json_file_data['name']
        core.printout_result(**response_content)
    except Exception as exc:
        click.echo(str(exc))

    return None
