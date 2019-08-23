import ijson.backends.yajl2 as ijson


def load_json_from_file(filename):
    with open(filename, 'rb') as input_file:
        items_generator = ijson.items(input_file, '')
        list_items = [item for item in items_generator]
        json_dict = list_items[0]

        return json_dict
