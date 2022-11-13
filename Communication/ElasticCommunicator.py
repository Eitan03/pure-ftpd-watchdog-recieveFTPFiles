import logging
from elasticsearch import Elasticsearch

from Communication.BaseCommunicator import BaseCommunicator

logger = logging.getLogger('')

class Communicator(BaseCommunicator):
    def __init__(self, host: str):
        self.__elasticsearch = Elasticsearch(host)

    def log(self, index_name: str, doc: dict):
        logger.info(f'logged to elastic in index {index_name}')
        x = self.__elasticsearch.index(index=index_name, document=doc)
