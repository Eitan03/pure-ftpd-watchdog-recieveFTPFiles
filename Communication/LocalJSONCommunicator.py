from datetime import datetime
import json
import logging
import os

from Communication.BaseCommunicator import BaseCommunicator

logger = logging.getLogger('')

class LocalJSONCommunicator(BaseCommunicator):
	def	__init__(self, baseDir):
		self.baseDir = baseDir

	def	log(self, topic_name: str, doc: dict, add_timestamp=True):
		if add_timestamp: doc['@timestamp'] = str(datetime.now()).replace(' ', 'T') + 'Z'

		folder = os.path.join(self.baseDir,topic_name)

		if not os.path.exists(folder):
			logger.info(f'creating folder {folder}')
			os.mkdir(folder)
		with open(os.path.join(folder, f'{topic_name} - {datetime.now().strftime("%Y-%m-%d:%H")}.json'), 'a') as f:
			data = json.dumps(doc)
			f.write(data + '\n')
		logger.info(f'logged to elastic in index {topic_name}')
