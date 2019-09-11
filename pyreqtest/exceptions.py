class FileExtensionError(Exception):
    """The exception raised for trying to load unsupported file extensions"""

    def __init__(self, file_extension):
        """Instantiate an object with a file extension isn't supported for
        loading and message that gives information to the user.

        :param str file_extension: File extension
        """
        self.file_extension = file_extension
        self.message = (
            "A file extension '{file_extension}' is not supported. "
            "Only a file with '.json' extension is supported".format(
                file_extension=self.file_extension
            )
        )
        super().__init__(self.message)
