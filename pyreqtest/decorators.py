from functools import wraps

from pyreqtest.constants import JSON_FILE_EXTENSION


def check_file_extension(func):
    """A decorator responsible for checking whether
    the file extension is supported.

    Inner :func:``_decorator`` slices the last five
    characters of the passed ``file_path`` parameter and
    checking whether they are equal to JSON file extension(.json).
    If there is equality, decorated function business logic is
    performed otherwise, the exception for not supported file extension
    is raised. Usage:

        @check_file_extension
        def load_json_from_file(file_path):
            ...
    """
    @wraps(func)
    def _decorator(file_path):
        if file_path[-5:] != JSON_FILE_EXTENSION:
            raise Exception()
        return func(file_path)
    return _decorator
