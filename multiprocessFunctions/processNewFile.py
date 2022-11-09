import threading

from Database.LocalJSONLogger import LocalJSONLogger
from Utils.FileNameUtilFunctions import processFilePath
from SendFileToServer import sendFileToServer
from config import SEC_BEFORE_FILE_EXPIRATION
from multiprocessFunctions.fileExpired import fileExpired
from processNewFile import processNewFile as processNewFileSync
from Database.RedisDB import RedisDB
from .processPool import pool


def onExpiration(processFileOutput):
    file_name, didSentToServer = processFileOutput
    if (not didSentToServer):
        print(f'started timer for {file_name}')
        threading.Timer(SEC_BEFORE_FILE_EXPIRATION, fileExpired, [file_name, RedisDB]).start()

def onError(e):
    print('got error in process!')
    print(e)

def processNewFile(newFilePath): 
    return pool.apply_async(processNewFileSync, [newFilePath, processFilePath, RedisDB, LocalJSONLogger, sendFileToServer], callback=onExpiration, error_callback=onError)
    # return processNewFileSync( newFilePath, processFilePath, RedisDB, createLocalJSONLogger, sendFileToServer )
    #output = processNewFileSync(newFilePath, processFilePath, RedisDB, createLocalJSONLogger, sendFileToServer)
    #onExpiration(output)