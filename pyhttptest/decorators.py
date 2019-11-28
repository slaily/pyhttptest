from sys import modules
from functools import wraps

from jsonschema import validate

from pyhttptest.constants import (
    HTTP_METHOD_NAMES,
    JSON_FILE_EXTENSION,
)
from pyhttptest.exceptions import (
    FileExtensionError,
    HTTPMethodNotSupportedError
)


def check_file_extension(func):
    """A decorator responsible for checking whether
    the file extension is supported.

    An inner :func:`_decorator` slices the last five
    characters of the passed ``file_path`` parameter and
    checking whether they are equal to JSON file extension(.json).
    If there is equality, decorated function business logic is
    performed otherwise, the exception for not supported file extension
    is raised.

    Usage:

    .. code-block:: python

        @check_file_extension
        def load_content_from_json_file(file_path):
            ...

    :raises FileExtensionError: If the file extension is not '.json'.
    """
    @wraps(func)
    def _decorator(file_path):
        file_extension = file_path[-5:]
        if file_extension != JSON_FILE_EXTENSION:
            raise FileExtensionError(file_extension)
        return func(file_path)
    return _decorator


def validate_extract_json_properties_func_args(func):
    """A validation decorator, ensuring that arguments
    passed to the decorated function are with proper types.

    An inner :func:`_decorator` does checking of arguments
    types. If the types of the arguments are different than allowing
    ones, the exception is raised, otherwise decorated function
    is processed.

    Usage:

    .. code-block:: python

        @validate_extract_json_properties_func_args
        def extract_properties_values_from_json(data, keys):
            ...

    :raises TypeError: If the data is not a `dict`.
    :raises TypeError: If the keys is not a type of (`tuple`, `list`, `set`).
    """
    @wraps(func)
    def _decorator(data, keys):
        if not isinstance(data, dict):
            raise TypeError(
                (
                    "Passed 'data' param argument, must be of "
                    "data type 'dict'. Not a type of {type}.".format(
                        type=type(data)
                    )
                )
            )

        if not isinstance(keys, (tuple, list, set)):
            raise TypeError(
                (
                    "Passed 'keys' param argument, must be one of: "
                    "(tuple, list, set) data types. Not a type of {type}.".format(
                        type=type(keys)
                    )
                )
            )
        return func(data, keys)
    return _decorator


def validate_data_against_json_schema(func):
    """A validation decorator, ensuring that data is
    covering JSON Schema requirements.

    An inner :func:`_decorator` does checking of data
    type, HTTP Method support along with appropriate JSON Schema,
    that can validate passed data. If one of the checks doesn't match,
    the exception is raised, otherwise, data validation is run against
    JSON Schema and decorated function is processed.

    Usage:

    .. code-block:: python

        @validate_data_against_json_schema
        def extract_json_data(data):
            ...

    :raises TypeError: If the data is not a `dict`.
    :raises HTTPMethodNotSupportedError: If an HTTP Method is not supported.
    :raises TypeError: If lack of appropriate JSON Schema to validate data.
    """
    @wraps(func)
    def _decorator(data):
        if not isinstance(data, dict):
            raise TypeError(
                (
                    "Passed 'data' param argument, must be of "
                    "data type 'dict'. Not a type of {type}.".format(
                        type=type(data)
                    )
                )
            )

        if 'verb' not in data or data['verb'].lower() not in HTTP_METHOD_NAMES:
            raise HTTPMethodNotSupportedError(data.get('verb', 'None'))

        http_schemas_module = modules['pyhttptest.http_schemas']
        http_schema_name = '_'.join([data['verb'].lower(), 'schema'])

        if not hasattr(http_schemas_module, http_schema_name):
            raise ValueError(
                (
                    'There is no appropriate JSON Schema to '
                    'validate data against it.'
                )
            )

        http_schema_module = getattr(http_schemas_module, http_schema_name)
        http_schema_instance = getattr(http_schema_module, http_schema_name)
        validate(instance=data, schema=http_schema_instance)

        return func(data)
    return _decorator
