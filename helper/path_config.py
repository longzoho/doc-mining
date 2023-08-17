import os


def content_path():
    return os.getenv('CONTENT_PATH') or '/content'


def document_path():
    return os.getenv('DOCUMENT_PATH') or '/document'


def embeddingdb_path():
    return os.getenv('EMBEDDINGDB_PATH') or '/embeddingdb'


def bucket():
    return os.getenv('BUCKET_NAME') or 'doc-mining'
