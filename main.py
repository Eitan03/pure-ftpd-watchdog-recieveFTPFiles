import logging
import time
from os import scandir, path

from Communication.Logger import initLogger
from Communication.RedisDB import RedisDB
from NewFileEventListener import NewFileListener
from config import config
from multiprocessFunctions.processNewFile import processNewFile



if  __name__ == "__main__":
    initLogger()
    redisDB = RedisDB()
    redisDB.flushAll()


    logger = logging.getLogger('')
    for entry in scandir(config['FTP_IMAGES_PATH']):
        if entry.is_file():
            logger.info(f'found file {entry.name}, preprocessing it')
            processNewFile(path.join(config['FTP_IMAGES_PATH'], entry.name))
        else:
            logger.info(f"WARNING! an object that isnt a file was found in the listenning dir! {entry.name}")

    fileListener = NewFileListener(config['FTP_IMAGES_PATH'], processNewFile)

    fileListener.start_listenning()
    logger.info(f"started listenning to folder {config['FTP_IMAGES_PATH']}")
    try:
        while True:
            time.sleep(1)
    finally:
        fileListener.stop_listenning()
