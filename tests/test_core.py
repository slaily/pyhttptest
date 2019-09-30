import pytest

from pyreqtest import core
from pyreqtest.exceptions import FileExtensionError


def test_load_json_from_file():
    json_dict = core.load_json_from_file('data/test_data.json')

    assert isinstance(json_dict, dict)


def test_load_json_from_file_with_not_supported_file_extension():
    with pytest.raises(FileExtensionError) as exc:
        core.load_json_from_file('data/test_data.yaml')

    assert "is not supported" in str(exc.value)


def test_extract_json_data():
    data = core.load_json_from_file('data/test_data.json')
    required_args, optional_kwargs = core.extract_json_data(data)

    assert isinstance(required_args, tuple) and isinstance(optional_kwargs, dict)
