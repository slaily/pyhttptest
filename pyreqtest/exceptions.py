class FileExtensionError(Exception):
    """The exception raised for trying to load unsupported file extensions"""

    def __init__(self, file_extension):
        """Instantiate an object with a file extension isn't supported for
        loading and message that gives information to the user.

        :param str file_extension: A File extension e.g. '.yaml'.
        """
        self.file_extension = file_extension
        self.message = (
            "A file extension '{file_extension}' is not supported. "
            "Only a file with '.json' extension is supported".format(
                file_extension=self.file_extension
            )
        )
        super().__init__(self.message)


class HTTPMethodNotSupportedError(Exception):
    """The exception raised when HTTP method isn't supported
    on the application level or typo found.
    """

    def __init__(self, http_method):
        """Instantiate an object with a HTTP method and message that gives information to the user.

        :param str http_method: An HTTP method e.g. 'HEAD'.
        """
        self.http_method = http_method.upper()
        self.message = (
            "An HTTP method ('{method}') is not supported by the application.".format(
                method=self.http_method
            )
        )
        super().__init__(self.message)
