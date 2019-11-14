from click.testing import CliRunner

from pyhttptest import cli


def test_execute():
    runner = CliRunner()
    result = runner.invoke(cli.execute, ['data/HTTP_GET.json'])

    assert result.exit_code == 0


def test_execute_with_not_supported_file_extension_as_arg():
    runner = CliRunner()
    result = runner.invoke(cli.execute, ['data/HTTP_GET.yaml'])

    assert result.exit_code == 0
