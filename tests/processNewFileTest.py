import unittest

from unittest.mock import ANY, Mock
from Mocks.createEmptyProcessNewFile import createEmptyProcessNewFile


class test_processNewFile(unittest.TestCase):

	def test_createEmptyProcessNewFile(self):
		createEmptyProcessNewFile()
	
	# TODO: c

	def test_processNewFile_cehck_saved_type_and_file_to_redis(self):

		file_name = 'file'
		file_idx = 0
		file_path = 'path/to/file'

		processFileName = Mock(return_value=(file_name, 'txt', file_idx))

		redisDBgetHashValueMock = Mock(return_value=True)
		db = {
			'setHashValue': redisDBgetHashValueMock,
		}
		createEmptyProcessNewFile(filePath=file_path, processFileName=processFileName, database=db)

		redisDBgetHashValueMock.assert_called_with(file_name, str(file_idx), file_path)


	def test_processNewFile_cehck_saved_type_and_file_send_to_server(self):

		file_name = 'file'
		file_ext = 'txt'
		file_idx = 1
		file_path_0 = 'path/to/file'
		file_path_1 = 'path/to/file_b'

		processFileName = Mock(return_value=(file_name, None, file_idx))

		db = {
			'exists': Mock(return_value=True),
			'lenOfHash': Mock(return_value=2),
			'getHash': Mock(return_value={'type': file_ext, '0': file_path_0}),
		}
		sendFileMock = Mock(return_value=None)


		createEmptyProcessNewFile(filePath=file_path_1, processFileName=processFileName, database=db, sendFile=sendFileMock)

		sendFileMock.assert_called_with(file_name + '.' + file_ext, ANY, file_path_0, file_path_1)