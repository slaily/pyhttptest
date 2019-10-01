from pyreqtest import exceptions


def test_file_extension_error_exception():
    file_extension_error = exceptions.FileExtensionError('.yaml')
    exception_message = (
        "A file extension '.yaml' is not supported. "
        "Only a file with '.json' extension is supported"
    )

    assert file_extension_error.message == exception_message


def test_http_verb_not_supported_error_exception():
    http_verb_not_supported_error = exceptions.HTTPVerbNotSupportedError('HEAD')
    exception_message = "An HTTP verb ('HEAD') is not supported by the application."

    assert http_verb_not_supported_error.message == exception_message
