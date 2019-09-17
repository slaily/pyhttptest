from copy import deepcopy

from pyreqtest.http_schemas.base_schema import base_schema


# A ``dict`` schema that copies :file:`pyreqtest/http_schemas/base_schema.py`
# schema and extends it with properties related for a structure specification
# sending an HTTP GET Request.
get_schema = deepcopy(base_schema)
get_schema['properties'].update(
    {
        'query_string': {
            'type': 'object'
        }
    }
)
