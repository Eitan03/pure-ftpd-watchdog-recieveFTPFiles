from datetime import datetime
import requests
from os import remove as deleteFile

from config import MY_IP, SERVER_NAME
from Database.LocalJSONLogger import LocalJSONLogger

def sendFileToServer(file_name, logger: LocalJSONLogger, *file_parts_path):
    try:
        
        fileParts = []
        for part_path in file_parts_path:
            with open(part_path, 'rb') as f:
                    fileParts.append(('fileParts', f.read()))

        res = requests.post(SERVER_NAME, data={ "fileName": file_name}, files=fileParts)
        
        for file in file_parts_path:
            deleteFile(file)
        
        print(f'REQUESTS: sent file {file_name} with {len(file_parts_path)} parts to server with response code of {res.status_code}')
        logger.log('sent-files',
               {'fileName': file_name, 'sender': MY_IP, 'response': res.status_code})
        if (resJson := res.json()):
            print(f'response body: {resJson}')
    
    except Exception as e:
        print({e})