from jsonschema import validate

from pyreqtest.http_schemas.get_schema import get_schema


def test_schema_with_valid_data():
    data = {
        'name': 'Test',
        'verb': 'GET',
        'endpoint': 'users',
        'host': 'http://test.com',
        'query_string': {
            'page': '1',
            'limit': '5'
        }
    }

    result = validate(instance=data, schema=get_schema)

    assert result is None
