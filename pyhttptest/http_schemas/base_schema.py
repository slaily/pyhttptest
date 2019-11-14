# A ``dict`` schema that defines a structure specification for sending
# an HTTP Request, along with required and non-required parameters
# like Request Header and Response Headert that might be sent by request.
# This is the base schema that will be extended from the HTTP Methods
# schemas::
#
#     ... GET - :file:`pyhttptest/http_schemas/get_schema.py`
#
# The purpose is to validate input JSON file content
# under the schema.
base_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'verb': {
            'type': 'string',
            'enum': ['GET', 'POST', 'PUT', 'DELETE']
        },
        'endpoint': {'type': 'string'},
        'host': {'type': 'string'},
        'headers': {
            'type': 'object',
            'properties': {
                'Content-Type': {'type': 'string'},
                'Content-Encoding': {'type': 'string'},
                'Content-Language': {'type': 'string'},
                'Content-Location': {'type': 'string'},
                'Content-Length': {'type': 'number'},
                'Content-Range': {'type': 'string'},
                'Cache-Control': {'type': 'string'},
                'Expect': {'type': 'string'},
                'Host': {'type': 'string'},
                'Max-Forwards': {'type': 'number'},
                'Pragma': {'type': 'string'},
                'If-Match': {'type': 'string'},
                'If-None-Match': {'type': 'string'},
                'If-Modified-Since': {
                    'type': 'string',
                    'format': 'date'  # <day-name>, <day> <month> <year> <hour>:<minute>:<second> GMT
                },
                'If-Unmodified-Since': {
                    'type': 'string',
                    'format': 'date'  # <day-name>, <day> <month> <year> <hour>:<minute>:<second> GMT
                },
                'Accept': {'type': 'string'},
                'Accept-Charset': {'type': 'string'},
                'Accept-Encoding': {'type': 'string'},
                'Accept-Language': {'type': 'string'},
                'Authorization': {'type': 'string'},
                'Proxy-Authorization': {'type': 'string'},
                'From': {'type': 'string'},
                'Referer': {'type': 'string'},
                'User-Agent': {'type': 'string'},
                'Trailer': {'type': 'string'},
                'Transfer-Encoding': {'type': 'string'}
            }
        },
    },
    'required': [
        'name',
        'verb',
        'endpoint',
        'host'
    ]
}
