# define class Profile
from tinydb import TinyDB, Query

from data_types import FileObj


class Profile:
    def __init__(self, profile_id: str):
        self.profile_id = profile_id
        self.db = TinyDB(f'./data/database.json')
        self.table = self.db.table('profiles')

    def add_files(self, file_objs: list[FileObj]):
        # create profile if not exists
        profile_query = Query()
        profile = self.table.search(profile_query.profile_id == self.profile_id)
        if not profile:
            self.table.insert({'profile_id': self.profile_id, 'files': [file_obj for file_obj in file_objs]})
        else:
            # merge files remove duplicate file_hash
            profile_files = profile[0]['files']
            file_hash_list = [file['file_hash'] for file in profile_files]
            self.table.upsert(
                {'files': [file_obj for file_obj in file_objs if file_obj.file_hash not in file_hash_list]},
                profile_query.profile_id == self.profile_id)

    def update_file_status(self, file_hash: str, file_status: str):
        profile_query = Query()
        profile = self.table.search(profile_query.profile_id == self.profile_id)
        if profile:
            profile_files = profile[0]['files']
            for file in profile_files:
                if file['file_hash'] == file_hash:
                    file['file_status'] = file_status
            self.table.upsert({'files': profile_files}, profile_query.profile_id == self.profile_id)
        else:
            raise Exception(f'Profile {self.profile_id} not found')

    def get_profile(self):
        profile_query = Query()
        profile = self.table.search(profile_query.profile_id == self.profile_id)
        return profile[0]

    def __str__(self):
        return self.profile_id
