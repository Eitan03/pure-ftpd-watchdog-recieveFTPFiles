from processNewFile import *

from unittest.mock import Mock, ANY

from .CommunicatorMock import createCommunicatorMock
from .DatabaseMock import createDatabaseMock

def createEmptyProcessNewFile(filePath = '', processFileName = Mock(return_value=('', None, 0)), database = {}, communicator = {},sendFile = Mock(return_value=True)):

	class DynamicObject():
		def __init__(self, dictionary: dict):
			self.__dict__.update(dictionary)

	def DatabaseFactory(): 
			return createDatabaseMock(database)
	
	def communicatorFactory():
		return createCommunicatorMock(communicator)

	return processNewFile(filePath, processFileName, DatabaseFactory, communicatorFactory, sendFile)