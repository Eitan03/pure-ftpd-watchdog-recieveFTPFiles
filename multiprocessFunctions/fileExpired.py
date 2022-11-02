from onFileExpiration import fileExpired as fileExpiredSync
from .processPool import pool

def fileExpired(newFilePath, databaseFactory):
    return pool.apply_async(fileExpiredSync, [newFilePath, databaseFactory])