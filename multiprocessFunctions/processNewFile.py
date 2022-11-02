import threading

from Utils.log import log
from Utils.FileNameUtilFunctions import processFilePath
from SendFileToServer import sendFileToServer
from config import SEC_BEFORE_FILE_EXPIRATION
from multiprocessFunctions.createElasticLogger import createElasticLogger
from multiprocessFunctions.fileExpired import fileExpired
from processNewFile import processNewFile as processNewFileSync
from Database.RedisDB import RedisDB
from .processPool import pool


def onExpiration(processFileOutput):
    file_name, didSentToServer = processFileOutput
    if (not didSentToServer):
        log(f'started timer for {file_name}')
        threading.Timer(SEC_BEFORE_FILE_EXPIRATION, fileExpired, [file_name, RedisDB]).start()


def processNewFile(newFilePath): 
    return pool.apply_async(processNewFileSync, [newFilePath, processFilePath, RedisDB, createElasticLogger, sendFileToServer], callback=onExpiration)
    # return processNewFileSync( newFilePath, processFilePath, RedisDB, createElasticLogger, sendFileToServer )