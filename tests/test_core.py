from unittest.mock import patch

import pytest

from requests import Response

from pyhttptest import core
from pyhttptest.exceptions import FileExtensionError


def test_load_content_from_json_file():
    content = core.load_content_from_json_file('data/HTTP_GET.json')

    assert isinstance(content[0], dict)


def test_load_content_from_json_file_with_not_supported_file_extension():
    with pytest.raises(FileExtensionError) as exc:
        core.load_content_from_json_file('data/HTTP_GET.yaml')

    assert 'is not supported' in str(exc.value)


def test_extract_json_data():
    content = core.load_content_from_json_file('data/HTTP_GET.json')
    required_args, optional_kwargs = core.extract_json_data(content[0])

    assert isinstance(required_args, tuple) and isinstance(optional_kwargs, dict)


def test_extract_json_data_with_key_name_response():
    content = core.load_content_from_json_file('data/HTTP_GET_SAVE_RESPONSE.json')
    required_args, optional_kwargs = core.extract_json_data(content[0])

    assert 'response' in optional_kwargs and optional_kwargs['response']


def test_prepare_request_args():
    args = (
        'TEST: List all users',
        'GET',
        'users',
        'http://localhost:8080'
    )
    request_args = core.prepare_request_args(*args)
    expected_args = ('get', 'http://localhost:8080/users')

    assert sorted(request_args) == sorted(expected_args)


def test_prepare_request_args_with_invalid_arguments():
    args = (
        'users',
        'http://localhost:8080'
    )
    request_args = core.prepare_request_args(*args)

    assert request_args is None


@patch('pyhttptest.core.method_dispatcher', return_value=Response)
def test_send_http_request(mock):
    mock.return_value.status_code = 200
    args = ('get', 'http://localhost:8080/users')
    response = core.send_http_request(*args)

    assert response.status_code == 200


def test_extract_http_response_content():
    response = Response()
    response.status_code = 200
    response.headers = {'Content-Type': 'application/json'}
    response_content = core.extract_http_response_content(response)

    assert all(
        key in response_content for key in ('status_code',)
    )


def test_extract_http_response_content_with_not_supported_argument_type():
    response = {
        'status_code': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': '<h1>Hello, pyhttptest!</h1>'
    }
    response_content = core.extract_http_response_content(response)

    assert response_content is None


def test_load_content_from_json_file_with_multiple_http_requests_scenarios():
    content = core.load_content_from_json_file(
        'data/MULTIPLE_HTTP_REQUESTS.json'
    )

    assert isinstance(content[0], list)


def test_transform_data_in_tabular_str_with_dict_data():
    data = {
        'name': 'Test: process data for print',
        'status_code': '200',
        'headers': '{Content-Type: application/json}',
        'body': 'Lorem Ipsum'
    }
    tabular_str = core.transform_data_in_tabular_str(data)

    assert isinstance(tabular_str, str)


def test_transform_data_in_tabular_str_with_list_of_dict_data():
    data = [{
        'name': 'Test: process data for print',
        'status_code': '200',
        'headers': '{Content-Type: application/json}',
        'body': 'Lorem Ipsum'
    }]
    tabular_str = core.transform_data_in_tabular_str(data)

    assert isinstance(tabular_str, str)
