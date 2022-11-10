import logging
import threading

from Utils.FileNameUtilFunctions import processFilePath
from SendFileToServer import sendFileToServer
from config import SEC_BEFORE_FILE_EXPIRATION
from multiprocessFunctions.createLocalJSONCommunicator import createLocalJSONCommunicator
from multiprocessFunctions.fileExpired import fileExpired
from processNewFile import processNewFile as processNewFileSync
from Communication.RedisDB import RedisDB
from .processPool import pool

logger = logging.getLogger('')

def onExpiration(processFile_output):
    file_name, did_sent_to_server = processFile_output
    if (not did_sent_to_server):
        logger.info(f'started timer for {file_name}')
        threading.Timer(SEC_BEFORE_FILE_EXPIRATION, fileExpired, [file_name, RedisDB]).start()

def onError(e):
    logger.error(f'got error in process! {e}')

def processNewFile(new_file_path): 
    return pool.apply_async(processNewFileSync, [new_file_path, processFilePath, RedisDB, createLocalJSONCommunicator, sendFileToServer], callback=onExpiration, error_callback=onError)
    #output = processNewFileSync(newFilePath, processFilePath, RedisDB, createLocalJSONCommunicator, sendFileToServer)
    #onExpiration(output)