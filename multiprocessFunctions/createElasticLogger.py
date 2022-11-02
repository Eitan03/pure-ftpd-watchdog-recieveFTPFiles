from config import ELASTIC_HOST
from Database.elasticLogger import elasticLogger

def createElasticLogger():
    return elasticLogger(ELASTIC_HOST)