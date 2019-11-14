from copy import deepcopy

from pyhttptest.http_schemas.base_schema import base_schema


# A ``dict`` schema that copies :file:`pyhttptest/http_schemas/base_schema.py`
# schema and extends it with properties related for a structure specification
# sending an HTTP PUT Request.
put_schema = deepcopy(base_schema)
put_schema['properties'].update(
    {
        'payload': {
            'type': 'object'
        },
        'query_string': {
            'type': 'object'
        }
    }
)
