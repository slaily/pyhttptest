from jsonschema import validate

from pyhttptest.http_schemas.delete_schema import delete_schema


def test_schema_with_valid_data():
    data = {
        'name': 'Test',
        'verb': 'DELETE',
        'endpoint': 'users/1',
        'host': 'http://test.com',
    }

    result = validate(instance=data, schema=delete_schema)

    assert result is None
