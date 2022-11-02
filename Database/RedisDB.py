import redis

from Utils.log import log

class RedisDB():
    def __init__(self):
        self.__redis = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def setHashValue(self, hashName, key, value):
        log(f'REDIS: saved ({key}: {value}) into hash {hashName}')
        return self.__redis.hset(hashName, key, value)

    def getHash(self, key):
        return self.__redis.hgetall(key)
    
    def delete(self, hashName):
        return self.__redis.delete(hashName)

    def exists(self, key):
        return self.__redis.exists(key)

    def lenOfHash(self, key):
        return self.__redis.hlen(key)
    
    def flushAll(self):
        return self.__redis.flushall( asynchronous=False)