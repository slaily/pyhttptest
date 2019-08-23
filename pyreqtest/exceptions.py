class FileExtensionError(Exception):
    def __init__(self, file_extension):
        self.file_extension = file_extension
        self.message = "A file extension '{file_extension}' is not supported".format(
            file_extension=self.file_extension
        )
        super().__init__(self.message)
