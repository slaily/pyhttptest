import pytest

from pyreqtest import utils


def test_extract_json_keys_values():
    json_data = {
        "name": "TEST: List all users",
        "verb": "GET",
        "endpoint": "users",
        "host": "HTTP://localhost:8080",
        "headers": {
            "Accept-Language": "en-US"
        }
    }
    json_keys = ('verb', 'endpoint', 'host')
    extracted_keys_values = utils.extract_json_keys_values(
        json_data,
        json_keys
    )
    expected_keys_values = (
        json_data['verb'],
        json_data['endpoint'],
        json_data['host']
    )

    assert sorted(expected_keys_values) == sorted(extracted_keys_values)


def test_extract_json_keys_values_with_wrong_data_format():
    json_data = 'key: value'

    with pytest.raises(TypeError) as exc:
        utils.extract_json_keys_values(json_data, ())

    part_of_exc_msg = 'Not a type of {type}'.format(type=type(json_data))

    assert part_of_exc_msg in str(exc.value)


def test_extract_json_keys_values_with_wrong_keys_format():
    json_data = {'name': 'test', 'verb': 'GET'}
    json_keys = 'name, verb'

    with pytest.raises(TypeError) as exc:
        utils.extract_json_keys_values(json_data, json_keys)

    part_of_exc_msg = 'Not a type of {type}'.format(type=type(json_keys))

    assert part_of_exc_msg in str(exc.value)
