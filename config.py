AMOUNT_OF_FILE_PARTS = 2
FTP_IMAGES_PATH = '/ftp/images'
SEC_BEFORE_FILE_EXPIRATION = 60
SERVER_NAME = 'http://10.0.0.9:8000/uploadfiles/'
ELASTIC_HOST = 'http://10.0.0.13:9200'
JSON_LOGS_PATH = './elasticLogs'

REDIS_IMAGES_PROCESSED_NAME = 'imagesProcessed'

import socket
MY_IP = socket.gethostbyname(socket.gethostname())