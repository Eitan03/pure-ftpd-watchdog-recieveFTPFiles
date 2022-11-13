from onFileExpiration import fileExpired as fileExpiredSync
from .processPool import pool

def fileExpired(new_file_path, databaseFactory):
    return pool.apply_async(fileExpiredSync, [new_file_path, databaseFactory])