from pyreqtest import exceptions


def test_file_extensior_error_exception():
    file_extension_error = exceptions.FileExtensionError('.yaml')
    exception_message = (
        "A file extension '.yaml' is not supported. "
        "Only a file with '.json' extension is supported"
    )

    assert file_extension_error.message == exception_message
