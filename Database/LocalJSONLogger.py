from datetime import datetime
import json
import os

class LocalJSONLogger():
	def	__init__(self):
		pass

	def	log(self, indexName: str, doc: dict):
		doc['@timestamp'] = str(datetime.now()).replace(' ', 'T') + 'Z'
		folder = os.path.join('./elasticLogs',indexName)
		if not os.path.exists(folder):
			print(f'creating folder {folder}')
			os.mkdir(folder)
		else:
			print(f'folder {folder} exists!')
		with open(os.path.join(folder, f'{indexName}-{str(datetime.now())}.json'), 'a') as f:
			json.dump(doc, f)
		print(f'logged to elastic in index {indexName}')
