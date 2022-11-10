from Communication.LocalJSONCommunicator import LocalJSONCommunicator
from config import JSON_LOGS_PATH

def createLocalJSONCommunicator():
	return LocalJSONCommunicator(JSON_LOGS_PATH)