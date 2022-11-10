from datetime import datetime
import logging
import requests
from os import remove as deleteFile

from config import MY_IP, SERVER_NAME

logger = logging.getLogger('')

def sendFileToServer(file_name, communicator, *file_parts_path):
    try:
        
        file_parts = []
        for part_path in file_parts_path:
            with open(part_path, 'rb') as f:
                    file_parts.append(('fileParts', f.read()))

        res = requests.post(SERVER_NAME, data={ "fileName": file_name}, files=file_parts)
        
        for file in file_parts_path:
            deleteFile(file)
        
        logger.info(f'REQUESTS: sent file {file_name} with {len(file_parts_path)} parts to server with response code of {res.status_code}')
        communicator.log('sent-files',
               {'fileName': file_name, 'sender': MY_IP, 'response': res.status_code})
        if (resJson := res.json()):
            logger.info(f'response body: {resJson}')
    
    except Exception as e:
        logger.error(f'recieve an error when sending files! {e}')