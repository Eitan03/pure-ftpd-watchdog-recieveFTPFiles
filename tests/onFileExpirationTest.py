import unittest
from unittest.mock import Mock, ANY

from  tests.Mocks.DatabaseMock import createDatabaseMock

import os
from onFileExpiration import fileExpired
from config import config
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

		fileExpired(file_name, lambda: db)

		deleteMock.assert_called_once_with(file_name)

	def test_fileExpired_deleted_parts(self):

		file_name = 'file'
		file_parts = []
		files_path = './tests/' + file_name + '_'


		db = createDatabaseMock({
			'exists': Mock(return_value=True),
			'getHash': Mock(return_value=dict([(str(i), files_path + str(i)) for i in range(5)])),
		})

		for i in range(config['AMOUNT_OF_FILE_PARTS']):
			file_path = files_path + str(i)
			with open(file_path, 'w') as f:
				f.write('123')

		fileExpired(file_name, lambda: db)

		for i in range(config['AMOUNT_OF_FILE_PARTS']):
			if os.path.isfile(files_path + str(i)):
				self.fail(f'file {files_path + str(i)} exists')