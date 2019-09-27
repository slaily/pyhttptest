import pytest

from pyreqtest import decorators
from pyreqtest.exceptions import FileExtensionError


def test_check_file_extension():
    func = decorators.check_file_extension(
        lambda file_extension: file_extension
    )
    func_result = func('.json')

    assert func_result == '.json'


def test_check_file_extension_with_not_supported_file_extension():
    with pytest.raises(FileExtensionError) as exc:
        func = decorators.check_file_extension(
            lambda file_extension: file_extension
        )
        func('test.yaml')

    assert "is not supported" in str(exc.value)


def test_validate_extract_json_properties_func_args():
    func = decorators.validate_extract_json_properties_func_args(
        lambda data, keys: True
    )
    json_data = {'name': 'TEST'}
    json_keys = ('name',)
    has_func_result = func(json_data, json_keys)

    assert has_func_result
