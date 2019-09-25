def extract_json_keys_values(data, keys):
    """Extracts values of the JSON keys.

    Passing ``data`` argument for an example:

        data = {
            "verb": "GET",
            "endpoint": "users",
            "host": "http://localhost:8080"
            ...
        }

    along with ``keys`` argument for an example:

        keys = ('verb', 'endpoint', host')

    Iterating over ``keys`` parameter values and
    extracts the value of ``data`` parameter key with the
    exact same value.

    Result:
        ('GET', 'users, 'http://localhost:8080')

    :param dict data: Content within а JSON format.
    :param tuple|list|set keys: Structure with values of type str.

    :returns: Packaged values within а tuple.
    :rtype: tuple

    :raises TypeError: If the data is not a dict.
    :raises TypeError: If the keys is not a type of (tuple, list, set).
    """
    if not isinstance(data, dict):
        raise TypeError(
            (
                "Passed 'data' param argument, must be of "
                "data type 'dict'."
            )
        )

    if not isinstance(keys, (tuple, list, set)):
        raise TypeError(
            (
                "Passed 'keys' param argument, must be one of: "
                "(tuple, list, set) data types."
            )
        )

    return tuple(data[key] for key in keys if key in data)
