JSON_FILE_EXTENSION = '.json'

REQUIRED_SCHEMA_KEYS = (
    'name',
    'verb',
    'endpoint',
    'host',
)

OPTIONAL_SCHEMA_KEYS = (
    'headers',
    'query_string',
)

HTTP_METHOD_NAMES = ('get', 'post', 'put', 'delete',)

SLICE_TO_INDEX = 100

PRINTER_HEADERS = (
    'Test name',
    'HTTP Response Status Code',
    'HTTP Response Headers',
    'HTTP Response Message Body',
)

PRINTER_HEADERS_DATA_KEYS = (
    'name',
    'status_code',
    'headers',
    'body',
)
