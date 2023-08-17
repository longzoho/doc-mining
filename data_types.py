class FileStatus(str):
    CONTENT_SAVED = "CONTENT_SAVED"
    DOCUMENT_SAVED = "DOCUMENT_SAVED"
    EMBED_SAVED = "EMBED_SAVED"
    FAILED = "FAILED"


class FileObj(dict):
    file_name: str
    file_hash: str
    file_status: FileStatus
