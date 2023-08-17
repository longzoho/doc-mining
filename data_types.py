class FileStatus(str):
    CONTENT_SAVED = "CONTENT_SAVED"
    DOCUMENT_SAVED = "DOCUMENT_SAVED"
    EMBED_SAVED = "EMBED_SAVED"
    ERROR = "ERROR"


class FileObj(dict):
    file_name: str
    file_hash: str
    file_status: FileStatus

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return self.get(name)
