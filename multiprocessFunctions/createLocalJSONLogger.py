from Database.LocalJSONLogger import LocalJSONLogger
from config import JSON_LOGS_PATH

def createLocalJSONLogger():
	return LocalJSONLogger(JSON_LOGS_PATH)