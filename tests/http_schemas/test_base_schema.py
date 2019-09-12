from jsonschema import validate

from pyreqtest.http_schemas.base_schema import base_schema


def test_schema_with_valid_data():
    data = {
        'name': 'Test',
        'verb': 'Base',
        'endpoint': 'users',
        'host': 'http://test.com',
    }

    result = validate(instance=data, schema=base_schema)

    assert result is None
