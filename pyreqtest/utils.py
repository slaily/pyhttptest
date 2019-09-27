def extract_properties_values_from_json(data, keys):
    """Extracts properties values from the JSON data.

    .. note::

        Each of key/value pairs into JSON conventionally referred
        to as a "property". More information about this convention follow
        `JSON Schema documentation <https://json-schema.org/understanding-json-schema/reference/object.html>`_.  # noqa

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
    extracts the property value of ``data`` parameter by key with the
    exact same value.

    Result:
        ('GET', 'users, 'http://localhost:8080')

    :param dict data: Data within а JSON format.
    :param tuple|list|set keys: Iterable with values of type str.

    :returns: Packaged values within а tuple.
    :rtype: tuple

    :raises TypeError: If the data is not a dict.
    :raises TypeError: If the keys is not a type of (tuple, list, set).
    """
    if not isinstance(data, dict):
        raise TypeError(
            (
                "Passed 'data' param argument, must be of "
                "data type 'dict'. Not a type of {type}.".format(
                    type=type(data)
                )
            )
        )

    if not isinstance(keys, (tuple, list, set)):
        raise TypeError(
            (
                "Passed 'keys' param argument, must be one of: "
                "(tuple, list, set) data types. Not a type of {type}.".format(
                    type=type(keys)
                )
            )
        )

    return tuple(data[key] for key in keys if key in data)
