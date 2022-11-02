from elasticsearch import Elasticsearch
from Utils.log import log

class elasticLogger():
    def __init__(self, host: str):
        self.__elasticsearch = Elasticsearch(host)
        pass

    def log(self, indexName: str, doc: dict):
        log(f'logged to elastic in index {indexName}')
        x = self.__elasticsearch.index(index=indexName, document=doc)
