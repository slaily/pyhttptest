from json import dumps

import ijson.backends.yajl2_c as ijson

from requests import Response

from pyhttptest import utils
from pyhttptest import constants
from pyhttptest.http import method_dispatcher
from pyhttptest.printer import prepare_data_for_print
from pyhttptest.decorators import (
    check_file_extension,
    validate_data_against_json_schema
)


@check_file_extension
def load_content_from_json_file(file_path):
    """Loads content from the file.

    By passing ``file_path`` parameter, the file is opened
    and the content from the file is extracted.

    :param str file_path: Optional file path.

    :returns: A content in a list
    :rtype: `list`
    """
    with open(file_path, 'rb') as file:
        items_generator = ijson.items(file, '')
        list_of_items = [item for item in items_generator]
        return list_of_items


@validate_data_against_json_schema
def extract_json_data(data):
    """Wrapper function that extracts JSON data.

    By passing ``data`` parameter, the JSON content
    from parameter is extracted under the required
    and optional keys.

    :param dict data: An arbitrary data.

    :returns: Splitted data into required and optional.
    :rtype: `tuple`
    """
    required_args = utils.extract_properties_values_from_json(
        data,
        constants.REQUIRED_SCHEMA_KEYS
    )
    optional_kwargs = utils.extract_properties_values_of_type_dict_from_json(
        data,
        constants.OPTIONAL_SCHEMA_KEYS
    )

    return (required_args, optional_kwargs)


def prepare_request_args(*args):
    """Prepares the required arguments that will be used
    to send an HTTP Request.

    By passing ``args`` parameter, the arguments within
    are transformed in a way to cover sending an HTTP Request
    gracefully.

    :param args: Expect arguments in format (name, verb, endpoint, host).

    :returns: Transformed arguments for HTTP Request.
    :rtype: `tuple`
    """
    if not args or len(args) != 4:
        return None

    _, http_method, endpoint, host = args
    url = utils.prepare_url(host, endpoint)

    return (http_method.lower(), url)


def send_http_request(*args, **kwargs):
    """Wrapper function responsible for sending an HTTP Request
    and receiving an HTTP Response.

    :param args: An HTTP Request arguments.
    :param kwargs: Optional arguments like HTTP headers, cookies and etc.

    :returns: :class:`Response` object or `None`.
    :rtype: :class:`requests.Response` or `None`
    """
    return method_dispatcher(*args, **kwargs)


def extract_http_response_content(response):
    """Extracts given :class:`requests.Response` instance
    attributes.

    Аttributes that are extracted from the instance are following:

        - HTTP Status Code
        - HTTP Headers
        - HTTP Body

    :param requests.Response response: Instance.

    :returns: Content of HTTP Response.
    :rtype: `dict`
    """
    if not isinstance(response, Response):
        return None

    return {
        'status_code': str(response.status_code),
        'headers': dumps(dict(response.headers), indent=2),
        'body': response.text
    }


def transform_data_in_tabular_str(data):
    """Transforms the data into tabular string.

    param list|dict data: An extract of HTTP Response data.

    :returns: A tabular string.
    :rtype: `str`
    """
    if not any(isinstance(data, _type) for _type in [list, dict]):
        return 'The data is not correctly structured.'

    if isinstance(data, list) and not isinstance(data[0], dict):
        return 'The list of content is not correctly formatted.'

    if isinstance(data, dict):
        # Put the `dict` data into a list
        data = [data]

    return prepare_data_for_print(data)
