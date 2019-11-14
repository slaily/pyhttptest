from jsonschema import validate

from pyhttptest.http_schemas.put_schema import put_schema


def test_schema_with_valid_data():
    data = {
        'name': 'Test',
        'verb': 'PUT',
        'endpoint': '/users/1',
        'host': 'http://test.com',
        'payload': {
            'user': {
                'name': 'HTTP_PUT',
                'password': '00193b3fd0cf9ef573f0df2f6f8a0940'
            }
        }
    }
    result = validate(instance=data, schema=put_schema)

    assert result is None
