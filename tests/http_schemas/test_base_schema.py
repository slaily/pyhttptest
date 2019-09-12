from jsonschema import validate


def test_schema_with_valid_data():
    data = {
        'name': 'Test',
        'verb': 'Base',
        'endpoint': 'users',
        'host': 'http://test.com',
    }

    result = validate(instance=data, schema=schema)

    assert result is None
