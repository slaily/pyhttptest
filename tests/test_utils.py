import pytest

from http.client import InvalidURL

from pyreqtest import utils


def test_extract_properties_values_from_json():
    json_data = {
        'name': 'TEST: List all users',
        'verb': 'GET',
        'endpoint': 'users',
        'host': 'http://localhost:8080',
        'headers': {
            'Accept-Language': 'en-US'
        }
    }
    json_keys = ('verb', 'endpoint', 'host')
    extracted_keys_values = utils.extract_properties_values_from_json(
        json_data,
        json_keys
    )
    expected_keys_values = (
        json_data['verb'],
        json_data['endpoint'],
        json_data['host']
    )

    assert sorted(expected_keys_values) == sorted(extracted_keys_values)


def test_extract_properties_values_of_type_dict_from_json():
    json_data = {
        'host': 'http://localhost:8080',
        'headers': {
            'Accept-Language': 'en-US'
        }
    }
    json_keys = ('headers',)
    extracted_keys_values = utils.extract_properties_values_of_type_dict_from_json(
        json_data,
        json_keys
    )

    assert 'headers' in extracted_keys_values


def test_prepare_url():
    host = 'http://localhost:8080'
    endpoint = 'users'
    url = utils.prepare_url(host, endpoint)

    assert url == 'http://localhost:8080/users'


def test_prepare_url_with_none_type_arg():
    url = utils.prepare_url('http://localhost:8080', None)

    assert url is None


def test_prepare_url_with_host_arg_ends_with_backslash():
    host = 'http://localhost:8080/'
    endpoint = 'users'
    url = utils.prepare_url(host, endpoint)

    assert url == 'http://localhost:8080/users'


def test_prepare_url_with_endpoint_arg_starts_with_backslash():
    host = 'http://localhost:8080'
    endpoint = '/users'
    url = utils.prepare_url(host, endpoint)

    assert url == 'http://localhost:8080/users'


def test_prepare_url_with_both_host_and_endpoint_args_contains_backslash():
    host = 'http://localhost:8080/'
    endpoint = '/users'
    url = utils.prepare_url(host, endpoint)

    assert url == 'http://localhost:8080/users'


def test_prepare_url_with_invalid_host_arg_format():
    with pytest.raises(InvalidURL) as exc:
        host = 'localhost.com'
        endpoint = 'users'
        utils.prepare_url(host, endpoint)

    assert 'Invalid URL' in str(exc.value)


def test_prepare_url_with_not_supported_url_scheme():
    with pytest.raises(InvalidURL) as exc:
        host = 'ftp://localhost.com'
        endpoint = 'users'
        utils.prepare_url(host, endpoint)

    assert 'Invalid URL scheme' in str(exc.value)
