from unittest.mock import patch

from pyhttptest import wrappers


@patch('pyhttptest.wrappers.core.extract_http_response_content', return_value=dict)
@patch('pyhttptest.wrappers.core.send_http_request')
def test_execute_single_test_scenario(_, mock):
    mock.return_value = {
        'status_code': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': {'username': 'pyhttptest'}
    }
    json_data = {
        'name': 'TEST: List all users',
        'verb': 'GET',
        'endpoint': 'users',
        'host': 'http://localhost:8080',
    }
    dict_data = wrappers.execute_single_test_scenario(json_data)

    assert 'body' in dict_data


@patch('pyhttptest.wrappers.core.extract_http_response_content', return_value=dict)
@patch('pyhttptest.wrappers.core.send_http_request')
def test_execute_multiple_test_scenarios(_, mock):
    mock.return_value = {'status_code': 200}
    list_of_dicts = [
        {
            'name': 'TEST: List all users',
            'verb': 'GET',
            'endpoint': 'users',
            'host': 'http://localhost:8080',
        },
        {
            'name': 'TEST: Delete a user',
            'verb': 'DELETE',
            'endpoint': 'users/1',
            'host': 'http://localhost:8080',
        }
    ]
    results = wrappers.execute_multiple_test_scenarios(list_of_dicts)

    assert len(results) == 2


@patch('pyhttptest.wrappers.core.extract_http_response_content', return_value=dict)
@patch('pyhttptest.wrappers.core.send_http_request')
def test_cli_execute(_, mock):
    mock.return_value = {
        'name': 'TEST: List all users',
        'status_code': '200',
        'headers': '{"Content-Type": "application/json"}',
        'body': '{"username": "pyhttptest"}'
    }
    output = wrappers.execute_test_scenarios('data/HTTP_GET.json')

    return isinstance(output, str)
