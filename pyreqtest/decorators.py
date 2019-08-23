from functools import wraps

from pyreqtest.constants import JSON_FILE_EXTENSION


def check_file_extension(func):
    @wraps(func)
    def _decorator(filename):
        if filename[-5:] != JSON_FILE_EXTENSION:
            raise Exception()
        return func(filename)
    return _decorator
