from elasticsearch import Elasticsearch

from Database.Logger import Logger

class elasticLogger(Logger):
    def __init__(self, host: str):
        self.__elasticsearch = Elasticsearch(host)

    def log(self, index_name: str, doc: dict):
        print(f'logged to elastic in index {index_name}')
        x = self.__elasticsearch.index(index=index_name, document=doc)
