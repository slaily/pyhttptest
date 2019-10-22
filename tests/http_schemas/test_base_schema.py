import pytest

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from pyhttptest.http_schemas.base_schema import base_schema


def test_schema_with_valid_data():
    data = {
        'name': 'Test',
        'verb': 'GET',
        'endpoint': 'users',
        'host': 'http://test.com',
    }

    result = validate(instance=data, schema=base_schema)

    assert result is None


def test_schema_with_invalid_data():
    with pytest.raises(ValidationError) as exc:
        # Not including a required property 'endpoint'
        # from the schema into the ``dict`` below
        data = {
            'name': 'Test',
            'verb': 'GET',
            'host': 'http://test.com',
        }

        validate(instance=data, schema=base_schema)

    assert 'required property' in str(exc.value)
