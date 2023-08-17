import logging
import os

from flask import request
from werkzeug.datastructures import FileStorage

from api.api_error_handler import api_error_handler
from data_types import FileObj, FileStatus
from repository.profile import Profile
from util.crypto_util import hash_content
from util.file_util import save_file, file_exists
from util.path_util import content_path, bucket
from workflow.embed_flow import embed_flow
from workflow.query_flow import query_flow

logger = logging.getLogger(__name__)


@api_error_handler
def upload_docs(profile_id: str):
    # get files from request body
    if "files" in request.files:
        files = request.files.getlist("files")
        file_objs: list[FileObj] = []
        for file in files:
            file_data, file_name = read_file(file)
            file_extension = os.path.splitext(file_name)[1]
            file_hash = hash_content(file_data)
            if file_data is not None:
                file_key = f'{content_path()}/{file_hash}{file_extension}'
                if not file_exists(bucket=bucket(), file_key=file_key):
                    save_file(bucket=bucket(), file_key=file_key, file_data=file_data)
                file_objs.append(FileObj(file_name=file_name, file_hash=f'{file_hash}{file_extension}',
                                         file_status=FileStatus.CONTENT_SAVED))
            else:
                logger.error(f'Error reading file {file_name}')
        profile = Profile(profile_id=profile_id)
        profile.add_files(file_objs=file_objs)
        return {'files': file_objs}, 200
    return {'message': 'No files found'}, 400


@api_error_handler
def embedding(profile_id: str):
    embed_flow(profile_id=profile_id)
    return {'message': 'embedding'}, 200


@api_error_handler
def query(profile_id: str):
    if request.json.get('query') is not None:
        result = query_flow(profile_id=profile_id, query=request.json.get('query'))
        return {'result': result}, 200
    return {'message': 'No query found'}, 400


def read_file(file: FileStorage) -> (bytes, str):
    file_name = file.filename
    try:
        return file.read(), file_name
    except Exception as e:
        logger.error(f'Error reading file {file_name}: {e}')
    return None, None
