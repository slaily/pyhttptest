from unittest.mock import patch

import pytest

from requests import Response

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

    assert sorted(request_args) == sorted(expected_args)


@patch('pyreqtest.core.method_dispatcher', return_value=Response)
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
        key in response_content for key in ('status_code', 'headers', 'body')
    )


def test_printout_result():
    test_kwargs = {
        'name': 'Test: process data for print',
        'status_code': '200',
        'headers': '{Content-Type: application/json}',
        'body': 'Lorem Ipsum'
    }
    result = core.printout_result(**test_kwargs)

    assert result is None
