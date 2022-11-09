from os	import remove as deleteFile

from config	import AMOUNT_OF_FILE_PARTS


def	fileExpired(file_name: str,	DatabaseFactory):
	db = DatabaseFactory()
	if db.exists(file_name):
		print(f'time for {file_name} has expired, deleting it')

		file_data =	db.getHash(file_name)
		for	i in range(AMOUNT_OF_FILE_PARTS):
			if str(i) in file_data:
				deleteFile(file_data[str(i)])

		db.delete(file_name)
