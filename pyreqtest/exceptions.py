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


class HTTPVerbNotSupportedError(Exception):
    """The exception raised when HTTP verb isn't supported
    on the application level or typo found.
    """

    def __init__(self, verb):
        """Instantiate an object with a verb and message that gives information to the user.

        :param str verb: An HTTP verb e.g. 'HEAD'.
        """
        self.verb = verb
        self.message = (
            "An HTTP verb ('{verb}') is not supported by the application.".format(
                verb=self.verb
            )
        )
        super().__init__(self.message)
