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
    json_data_keys_values = (
        json_data['verb'],
        json_data['endpoint'],
        json_data['host']
    )
    args = utils.extract_json_keys_values(json_data, json_keys)

    assert json_data_keys_values == args
