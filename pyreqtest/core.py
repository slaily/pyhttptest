import ijson.backends.yajl2 as ijson

from pyreqtest.decorators import check_file_extension


@check_file_extension
def load_json_from_file(file_path):
    """Loads JSON data from the file.

    By passing ``file_path`` parameter, the file is opened
    and the data from the file is extracted.

    :param str file_path: Optional file path

    :returns: JSON data
    :rtype: dict
    """
    with open(file_path, 'rb') as file:
        items_generator = ijson.items(file, '')
        list_items = [item for item in items_generator]
        json_dict = list_items[0]

        return json_dict
