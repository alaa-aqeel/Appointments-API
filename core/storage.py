import uuid, os 
from datetime import datetime
from core.setting import setting 


class Storage:

    # @classmethod 
    # def get_file(cls, filename: str):
    #     if cls.has_file(filename):

    @classmethod
    def full_path(self, filename: str):
        return f"{setting.storage_path}/{filename}"

    @classmethod
    async def store_file(cls, file: object):
        
        filename_split = file.filename.split(".")
        filename = f"{uuid.uuid4()}.{filename_split[-1]}"

        contents = await file.read() 

        with open(f"{setting.storage_path}/{filename}", "wb") as wf:
            wf.write(contents)

        return filename

    @classmethod
    def has_file(cls, filename: str):

        return os.path.exists(f"{setting.storage_path}/{filename}")

    @classmethod
    def delete_file(cls, filename: str):

        if cls.has_file(filename):
            os.remove(f"{setting.storage_path}/{filename}")

