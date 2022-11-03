import unittest
from unittest.mock import Mock, ANY

from .Mocks.DatabaseMock import createDatabaseMock

from onFileExpiration import fileExpired
# def	fileExpired(file_name: str,	DatabaseFactory):

class onFileExpirationTest(unittest.TestCase):
	def test_fileExpired_deleted_from_redis(self):

		file_name = 'file'

		deleteMock = Mock(return_value=True)

		db = createDatabaseMock({
			'exists': Mock(return_value=True),
			'getHash': Mock(return_value={}),
			'delete': deleteMock
		})

		fileExpired(file_name, db)

		deleteMock.assert_called_once_with(file_name)

	def test_fileExpired_deleted_parts(self):
		file_parts = []

		for i in range(5):
			
		pass
		