from urllib.parse import urlparse
from http.client import InvalidURL

from pyhttptest.decorators import validate_extract_json_properties_func_args


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
            'verb': 'GET',
            'endpoint': 'users',
            'host': 'http://localhost:8080'
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

    :param dict data: An arbitrary data.
    :param tuple|list|set keys: Iterable with values of type `str`.

    :returns: Packaged values.
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

    :param dict data: An arbitrary data.
    :param tuple|list|set keys: Iterable with values of type `str`.

    :returns: Packaged key/value pairs.
    :rtype: `dict`
    """
    return {
        key: data[key] for key in keys
        if key in data and isinstance(data[key], dict)
    }


def prepare_url(host, endpoint):
    """Glues the ``host`` and ``endpoint`` parameters to
    form an URL.

    :param str host: Value e.g. **http://localhost.com**.
    :param str endpoint: An API resourse e.g. **/users**.

    :raises InvalidURL: If the URL parts are in invalid format.
    :raises InvalidURL: If the URL schema is not supported.

    :returns: URL.
    :rtype: `str`
    """
    if not host or not endpoint:
        return None

    if not host[-1] == '/' and not endpoint[0] == '/':
        url = '/'.join([host, endpoint])

    if host[-1] == '/' and not endpoint[0] == '/':
        url = ''.join([host, endpoint])

    if not host[-1] == '/' and endpoint[0] == '/':
        url = ''.join([host, endpoint])

    if host[-1] == '/' and endpoint[0] == '/':
        url = ''.join([host, endpoint[1:]])

    parsed_url = urlparse(url)

    if not parsed_url.scheme or not parsed_url.netloc:
        raise InvalidURL('Invalid URL {url}'.format(url=url))

    if parsed_url.scheme not in ['http', 'https']:
        raise InvalidURL(
            'Invalid URL scheme {scheme}. '
            'Supported schemes are http or https.'.format(
                scheme=parsed_url.scheme
            )
        )

    return url
