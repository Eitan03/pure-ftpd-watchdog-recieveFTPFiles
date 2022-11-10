import logging
from logging.handlers import TimedRotatingFileHandler
from time import sleep
from config import MY_IP

log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)

jsonFormatter = logging.Formatter(
	'{ \"@timestamp\": \"%(asctime)s\", \"level\": \"%(levelname)s\", \"message\": \"%(message)s\"' + 
		', \"host\": \"' + MY_IP + '\" }'
	, datefmt='%Y-%m-%dT%H:%M:%SZ'
	) 

fh = TimedRotatingFileHandler('temp/test.json', when='H', interval=3, encoding='utf-8')
fh.setLevel(logging.WARNING)
fh.setFormatter(jsonFormatter)
log.addHandler(fh)


consoleFormatter = logging.Formatter('[%(levelname)s] - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(consoleFormatter)
log.addHandler(ch)

log.info('hello world')
log.warning('this is a warning')
log.error('this is a error!')
sleep(4)
log.warning('this is a warning2')