from functools import wraps

from pyhttptest.constants import JSON_FILE_EXTENSION
from pyhttptest.exceptions import FileExtensionError


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
        def load_json_from_file(file_path):
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
