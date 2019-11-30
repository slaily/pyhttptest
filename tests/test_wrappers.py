from unittest.mock import patch

from pyhttptest import wrappers


@patch('pyhttptest.wrappers.core.extract_http_response_content', return_value=dict)
@patch('pyhttptest.wrappers.core.send_http_request')
def test_execute_single_test_scenario(_, mock):
    mock.return_value = {
        'status_code': 200,
        'headers': {'Content-type': 'application/json'},
        'body': {'username': 'pyhttptest'}
    }
    test_kwargs = {
        'name': 'TEST: List all users',
        'verb': 'GET',
        'endpoint': 'users',
        'host': 'http://localhost:8080',
    }
    result = wrappers.execute_single_test_scenario(test_kwargs)

    assert 'name' in result
