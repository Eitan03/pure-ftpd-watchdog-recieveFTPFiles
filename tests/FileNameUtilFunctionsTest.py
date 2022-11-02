import unittest

from Utils.FileNameUtilFunctions import *


class TestFielNameUtilFunctions(unittest.TestCase):

	# getFileExtension

	def test_getFileExtension_without_extension(self):
		self.assertEqual(getFileExtension('testFile'), ('testFile', None))

	def test_getFileExtension_with_extension(self):
		self.assertEqual(getFileExtension('testFile.txt'), ('testFile', 'txt'))
	
	def test_getFileExtension_with_multiple_extensions(self):
		self.assertEqual(getFileExtension('testFile.txt.encrypted'), ('testFile', 'txt.encrypted'))
	
	# getFilePartIdx

	def test_getFilePartIdx__ends_with_a_returns_0(self):
		self.assertEqual(getFilePartIdx('test_file_a'), ('test_file', 0))

	def test_getFilePartIdx__ends_with_b_returns_1(self):
		self.assertEqual(getFilePartIdx('test_file_b'), ('test_file', 1))
	
	# processFilePath

	def test_processFilePath_absolute_path_with_extention_and_part(self):
		self.assertEqual(processFilePath('/full/path/to/file_b.txt'), ('file', 'txt', 1))

	def test_processFilePath_absolute_path_without_extention_and_with_part(self):
		self.assertEqual(processFilePath('/full/path/to/file_a'), ('file', None, 0))