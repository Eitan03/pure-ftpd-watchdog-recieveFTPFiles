import time
from os import scandir, path

from NewFileEventListener import NewFileListener
from Database.RedisDB import RedisDB
from Utils.log import log
from config import FTP_IMAGES_PATH
from multiprocessFunctions.processNewFile import processNewFile



if  __name__ == "__main__":
    redisDB = RedisDB()
    redisDB.flushAll()


    for entry in scandir(FTP_IMAGES_PATH):
        if entry.is_file():
            processNewFile(path.join(FTP_IMAGES_PATH, entry.name))
        else:
            log(f"WARNING! an object that isnt a file was found in the listenning dir! {entry.name}")

    fileListener = NewFileListener(FTP_IMAGES_PATH, processNewFile)

    fileListener.start_listenning()
    log(f"started listenning to folder {FTP_IMAGES_PATH}")
    try:
        while True:
            time.sleep(1)
    finally:
        fileListener.stop_listenning()
