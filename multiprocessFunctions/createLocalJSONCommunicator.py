from Communication.LocalJSONCommunicator import LocalJSONCommunicator
from config import config

def createLocalJSONCommunicator():
	return LocalJSONCommunicator(config['JSON_LOGS_PATH'])