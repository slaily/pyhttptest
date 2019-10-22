from click.testing import CliRunner

from pyhttptest import cli


def test_execute():
    runner = CliRunner()
    result = runner.invoke(cli.execute, ['data/HTTP_GET.json'])

    assert result.exit_code == 0
