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
    'response',
    'payload',
)

HTTP_METHOD_NAMES = ('get', 'post', 'put', 'delete',)

SLICE_TO_INDEX = 100

PRINTER_HEADERS = (
    'Test name',
    'HTTP Response Status Code',
    'Cover',
)

PRINTER_HEADERS_DATA_KEYS = (
    'name',
    'status_code',
    'cover'
)
