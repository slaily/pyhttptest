import pytest

from pyreqtest import core
from pyreqtest.exceptions import FileExtensionError


def test_load_json_from_file():
    json_dict = core.load_json_from_file('data/HTTP_GET.json')

    assert isinstance(json_dict, dict)


def test_load_json_from_file_with_not_supported_file_extension():
    with pytest.raises(FileExtensionError) as exc:
        core.load_json_from_file('data/HTTP_GET.yaml')

    assert "is not supported" in str(exc.value)


def test_extract_json_data():
    data = core.load_json_from_file('data/HTTP_GET.json')
    required_args, optional_kwargs = core.extract_json_data(data)

    assert isinstance(required_args, tuple) and isinstance(optional_kwargs, dict)


def test_prepare_request_args():
    args = (
        'TEST: List all users',
        'GET',
        'users',
        'http://localhost:8080'
    )
    request_args = core.prepare_request_args(*args)
    expected_args = ('get', 'http://localhost:8080/users')

    assert sorted(request_args) and sorted(expected_args)
