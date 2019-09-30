import pytest

from pyreqtest import utils


def test_extract_properties_values_from_json():
    json_data = {
        'name': 'TEST: List all users',
        'verb': 'GET',
        'endpoint': 'users',
        'host': 'HTTP://localhost:8080',
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
        'host': 'HTTP://localhost:8080',
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
