import ijson.backends.yajl2 as ijson

from pyreqtest import utils
from pyreqtest import constants
from pyreqtest.decorators import check_file_extension


@check_file_extension
def load_json_from_file(file_path):
    """Loads JSON data from the file.

    By passing ``file_path`` parameter, the file is opened
    and the data from the file is extracted.

    :param str file_path: Optional file path.

    :returns: JSON data.
    :rtype: `dict`
    """
    with open(file_path, 'rb') as file:
        items_generator = ijson.items(file, '')
        list_items = [item for item in items_generator]
        json_dict = list_items[0]

        return json_dict


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
    if not args and len(args) != 4:
        return None

    _, http_method, endpoint, host = args
    url = utils.prepare_url(host, endpoint)

    return (http_method.lower(), url)
