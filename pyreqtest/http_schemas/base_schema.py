# A ``dict`` schema that defines a structure specification for sending
# an HTTP Request, along with required and non-required parameters
# like Request Header and Response Headert that might be sent by request.
# This is the base schema that will be extended from the HTTP Methods
# schemas::
#
#     ... GET - :file:`pyreqtest/http_schemas/get_schema.py`
#
# The purpose is to validate input JSON file content
# under the schema.
base_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'verb': {
            'type': 'string',
            'enum': ['GET']
        },
        'endpoint': {'type': 'string'},
        'host': {'type': 'string'},
        'request_headers': {
            'type': 'object',
            'properties': {
                'Content-Type': {'type': 'string'},
                'Content-Encoding': {'type': 'string'},
                'Content-Language': {'type': 'string'},
                'Content-Location': {'type': 'string'},
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
                'User-Agent': {'type': 'string'}
            }
        },
        'response_headers': {
            'type': 'object',
            'properties': {
                'ETag': {'type': 'string'},
                'Last-Modified': {
                    'type': 'string',
                    'format': 'date'  # <day-name>, <day> <month> <year> <hour>:<minute>:<second> GMT
                },
                'WWW-Authenticate': {'type': 'string'},
                'Proxy-Authenticate': {'type': 'string'},
                'Allow': {'type': 'string'},
                'Server': {'type': 'string'},
                'Age': {'type': 'number'},
                'Cache-Control': {'type': 'string'},
                'Expires': {
                    'type': 'string',
                    'format': 'date'  # <day-name>, <day> <month> <year> <hour>:<minute>:<second> GMT
                },
                'Date': {
                    'type': 'string',
                    'format': 'date'  # <day-name>, <day> <month> <year> <hour>:<minute>:<second> GMT
                },
                'Location': {'type': 'string'},
                'Retry-After': {'type': 'number'},
                'Vary': {'type': 'string'}
            }
        }
    },
    'required': [
        'name',
        'verb',
        'endpoint',
        'host'
    ]
}
