
def test_check_file_extension():
    func = check_file_extension(lambda file_extension: file_extension)
    func_result = func('.json')

    assert func_result == '.json'
