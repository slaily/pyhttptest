import pytest

from pyhttptest import decorators
from pyhttptest.exceptions import (
    FileExtensionError,
    HTTPMethodNotSupportedError,
)


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


def test_validate_extract_json_properties_func_args_with_wrong_data_format():
    with pytest.raises(TypeError) as exc:
        func = decorators.validate_extract_json_properties_func_args(
            lambda data, keys: None
        )
        json_data = 'key: value'
        func(json_data, ())

    part_of_exc_msg = 'Not a type of {type}'.format(type=type(json_data))

    assert part_of_exc_msg in str(exc.value)


def test_extract_properties_values_from_json_with_wrong_keys_format():
    with pytest.raises(TypeError) as exc:
        func = decorators.validate_extract_json_properties_func_args(
            lambda data, keys: None
        )
        json_data = {'name': 'test', 'verb': 'GET'}
        json_keys = 'name, verb'
        func(json_data, json_keys)

    part_of_exc_msg = 'Not a type of {type}'.format(type=type(json_keys))

    assert part_of_exc_msg in str(exc.value)


def test_validate_data_against_json_schema():
    func = decorators.validate_data_against_json_schema(
        lambda data: data
    )
    data = {
        "name": "TEST: List all users",
        "verb": "GET",
        "endpoint": "users",
        "host": "https://localhost.com",
    }
    func_result = func(data)

    assert id(func_result) == id(data)


def test_validate_data_against_json_schema_with_not_supported_argument_type():
    with pytest.raises(TypeError) as exc:
        func = decorators.validate_data_against_json_schema(
            lambda data: data
        )
        data = {
            "TEST: List all users",
            "GET",
            "users",
            "https://localhost.com",
        }
        func(data)

    part_of_exc_msg = 'Not a type of {type}'.format(type=type(data))

    assert part_of_exc_msg in str(exc.value)


def test_validate_data_against_json_schema_with_not_supported_http_method():
    with pytest.raises(HTTPMethodNotSupportedError) as exc:
        func = decorators.validate_data_against_json_schema(
            lambda data: data
        )
        data = {
            "name": "TEST: List all users",
            "verb": "HEAD",
            "endpoint": "users",
            "host": "https://localhost.com",
        }
        func(data)

    part_of_exc_msg = "An HTTP method ('{http_method}') is not".format(
        http_method=data['verb']
    )

    assert part_of_exc_msg in str(exc.value)
