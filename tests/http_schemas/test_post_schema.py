from jsonschema import validate

from pyhttptest.http_schemas.post_schema import post_schema


def test_schema_with_valid_data():
    data = {
        'name': 'Test',
        'verb': 'POST',
        'endpoint': 'users',
        'host': 'http://test.com',
        'payload': {
            'user': {
                'id': 1
            }
        }
    }
    result = validate(instance=data, schema=post_schema)

    assert result is None
