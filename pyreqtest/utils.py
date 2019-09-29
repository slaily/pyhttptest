from pyreqtest.decorators import validate_extract_json_properties_func_args


@validate_extract_json_properties_func_args
def extract_properties_values_from_json(data, keys):
    """Extracts properties values from the JSON data.

    .. note::

        Each of key/value pairs into JSON conventionally referred
        to as a "property". More information about this convention follow
        `JSON Schema documentation <https://json-schema.org/understanding-json-schema/reference/object.html>`_.

    Passing ``data`` argument for an example:

    .. code-block:: python

        data = {
            "verb": "GET",
            "endpoint": "users",
            "host": "http://localhost:8080"
            ...
        }

    along with ``keys`` argument for an example:

    .. code-block:: python

        keys = ('verb', 'endpoint', 'host')

    Iterating over ``keys`` parameter values and
    extracts the property value of ``data`` parameter by key with the
    exact same value.

    Result:

    .. code-block:: python

        ('GET', 'users, 'http://localhost:8080')

    :param dict data: Data within а JSON format.
    :param tuple|list|set keys: Iterable with values of type `str`.

    :returns: Packaged values within а `tuple`.
    :rtype: `tuple`
    """
    return tuple(data[key] for key in keys if key in data)


@validate_extract_json_properties_func_args
def extract_properties_values_of_type_dict_from_json(data, keys):
    """Extracts properties values of type `dict` from the JSON data.

    .. note::

        Each of key/value pairs into JSON conventionally referred
        to as a "property". More information about this convention follow
        `JSON Schema documentation <https://json-schema.org/understanding-json-schema/reference/object.html>`_.

    Passing ``data`` argument for an example:

    .. code-block:: python

        data = {
            'verb': 'GET',
            'endpoint': 'users',
            'host': 'http://localhost:8080'
            'headers': {
                'Accept-Language': 'en-US'
            }
            ...
        }

    along with ``keys`` argument for an example:

    .. code-block:: python

        keys = ('headers',)

    Iterating over ``keys`` parameter values and
    extracts the property value of type `dict` from ``data``
    parameter by key with the exact same value.

    Result:

    .. code-block:: python

        {
            'headers': {
                'Accept-Language': 'en-US'
            }
        }

    :param dict data: Data within а JSON format.
    :param tuple|list|set keys: Iterable with values of type `str`.

    :returns: Packaged key/value pairs within а `dict`.
    :rtype: `dict`
    """
    return {
        key: data[key] for key in keys
        if key in data and isinstance(data[key], dict)
    }
