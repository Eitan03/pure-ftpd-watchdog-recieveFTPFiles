from processNewFile import *

from unittest.mock import Mock, ANY

from .LoggerMock import createLoggerMock
from .DatabaseMock import createDatabaseMock

def createEmptyProcessNewFile(filePath = '', processFileName = Mock(return_value=('', None, 0)), database = {}, logger = {},sendFile = Mock(return_value=True)):

	class DynamicObject():
		def __init__(self, dictionary: dict):
			self.__dict__.update(dictionary)

	def DatabaseFactory(): 
			return createDatabaseMock(database)
	
	def loggerFactory():
		return createLoggerMock(logger)

	return processNewFile(filePath, processFileName, DatabaseFactory, loggerFactory, sendFile)