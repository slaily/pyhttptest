import pytest

from pyreqtest import decorators
from pyreqtest.exceptions import FileExtensionError


def test_check_file_extension():
    func = decorators.check_file_extension(
        lambda file_extension: file_extension
    )
    func_result = func('.json')

    assert func_result == '.json'


def test_check_file_extension_with_not_supported_file_extension():
    with pytest.raises(FileExtensionError) as exc:
        func = decorators.check_file_extension(
            lambda file_extension: file_extension
        )
        func('test.yaml')

    assert "is not supported" in str(exc.value)
