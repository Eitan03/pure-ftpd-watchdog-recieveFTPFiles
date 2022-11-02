from datetime import datetime
import requests
from os import remove as deleteFile

from Utils.log import log
from config import MY_IP, SERVER_NAME
from Database.elasticLogger import elasticLogger

def sendFileToServer(file_name, logger: elasticLogger, *file_parts_path):
    try:
        
        fileParts = []
        for part_path in file_parts_path:
            with open(part_path, 'rb') as f:
                    fileParts.append(('fileParts', f.read()))

        res = requests.post(SERVER_NAME, data={ "fileName": file_name}, files=fileParts)
        
        for file in file_parts_path:
            deleteFile(file)
        
        log(f'REQUESTS: sent file {file_name} with {len(file_parts_path)} parts to server with response code of {res.status_code}')
        logger.log('sent-files',
               {'@timestamp': datetime.now(), 'fileName': file_name, 'sender': MY_IP, 'response': res.status_code})
        if (resJson := res.json()):
            log(f'response body: {resJson}')
    
    except Exception as e:
        log({e})