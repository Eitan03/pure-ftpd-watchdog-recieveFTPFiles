from datetime import datetime
import logging
from time import sleep
from Utils.FileNameUtilFunctions import *
from types import FunctionType

from config import AMOUNT_OF_FILE_PARTS, MY_IP, REDIS_IMAGES_PROCESSED_NAME

logger = logging.getLogger()

def processNewFile(file_path: str, processFileName: FunctionType, DatabaseFactory, communicatorFactory, sendFile: FunctionType):
    """_summary_

    Args:
        filePath (str): the full path of the file to process
        
        processFileName ( (filePath: str) -> (file_name, file_type, file_part_idx) ): the function to get the file attributes from its name
        
        DatabaseFactory ( () ): a function to initialize a database object that contains the functions to get/set database  key/value pairs
        
        communicatorFactory( () ): a function to initialize a communicator object that contain a function to log events to

        sendFile ( (fileName: str, *filePartsPath) -> None ): a function that accepts a file name and a list of its parts path and send it to further processing
    
    Returns:
        file_name, didSendFile
    """
    db = DatabaseFactory()
    communicator = communicatorFactory()

    try:
        logger.info(f'got new file {file_path}')
        communicator.log('received-file-parts',
           { 'fileName': file_path, 'receiver': MY_IP})
    except Exception as e:
        logger.error(f'got an error: {e}')
    file_name, file_type, file_part_idx = processFileName(file_path)

    while (db.setSetValue(REDIS_IMAGES_PROCESSED_NAME, file_name) == 0):
        logger.info(f'waiting with file {file_name} and part {file_part_idx}')
        sleep(0.5)
    # TODO maybe go to another image and return to this one?
    # maybe by openning and closing the file so a watchdog event is triggered

    try:
        if (not db.exists(file_name)) or (int(db.getHashValue(file_name, 'amount_of_parts')) < (AMOUNT_OF_FILE_PARTS - 1)):
            if file_type != None:
                db.setHashValue(file_name, 'type', file_type)

            db.setHashValue(file_name, str(file_part_idx), file_path)
            db.incrementHashValueBy(file_name, 'amount_of_parts', 1)

            return file_name, False
        else:
            file_data: list = db.getHash(file_name)
            if file_type is None: file_type = file_data['type']

            file_data[str(file_part_idx)] = file_path

            sendFile( file_name + "." + file_type, communicator, *[file_data[str(i)] for i in range(AMOUNT_OF_FILE_PARTS)])
            db.delete(file_name)
            return file_name, True
    finally:
        logger.info(f'deleting for set {file_name}')
        db.removeSetValue(REDIS_IMAGES_PROCESSED_NAME, file_name)
