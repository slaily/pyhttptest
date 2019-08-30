import pytest

from pyreqtest import core
from pyreqtest.exceptions import FileExtensionError


def test_load_json_from_file():
    json_dict = core.load_json_from_file('data/test_data.json')

    assert isinstance(json_dict, dict)


def test_load_json_from_file_format_type_yaml():
    with pytest.raises(FileExtensionError) as exc:
        core.load_json_from_file('data/test_data.yaml')

    assert "is not supported" in str(exc.value)
