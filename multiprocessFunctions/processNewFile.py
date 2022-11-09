import threading

from Utils.FileNameUtilFunctions import processFilePath
from SendFileToServer import sendFileToServer
from config import SEC_BEFORE_FILE_EXPIRATION
from multiprocessFunctions.createLocalJSONLogger import createLocalJSONLogger
from multiprocessFunctions.fileExpired import fileExpired
from processNewFile import processNewFile as processNewFileSync
from Database.RedisDB import RedisDB
from .processPool import pool


def onExpiration(processFile_output):
    file_name, did_sent_to_server = processFile_output
    if (not did_sent_to_server):
        print(f'started timer for {file_name}')
        threading.Timer(SEC_BEFORE_FILE_EXPIRATION, fileExpired, [file_name, RedisDB]).start()

def onError(e):
    print('got error in process!')
    print(e)

def processNewFile(new_file_path): 
    return pool.apply_async(processNewFileSync, [new_file_path, processFilePath, RedisDB, createLocalJSONLogger, sendFileToServer], callback=onExpiration, error_callback=onError)
    #output = processNewFileSync(newFilePath, processFilePath, RedisDB, createLocalJSONLogger, sendFileToServer)
    #onExpiration(output)