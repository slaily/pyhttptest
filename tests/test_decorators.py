from pyreqtest import decorators


def test_check_file_extension():
    func = decorators.check_file_extension(
        lambda file_extension: file_extension
    )
    func_result = func('.json')

    assert func_result == '.json'
