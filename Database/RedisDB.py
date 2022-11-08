import redis


class RedisDB():
    def __init__(self):
        self.__redis = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def setSetValue(self, setName, *values):
        return self.__redis.sadd(setName, *values)

    def removeSetValue(self, setName, *values):
        return self.__redis.srem(setName, *values)
    
    def setHashValue(self, hashName, key, value):
        print(f'REDIS: saved ({key}: {value}) into hash {hashName}')
        return self.__redis.hset(hashName, key, value)
    
    def incrementHashValueBy(self, hashName, key, amount=1):
        print(f'REDIS: incremented {key} by {amount} of hash {hashName}')
        return self.__redis.hincrby(hashName, key, amount)

    def getHash(self, key):
        return self.__redis.hgetall(key)
    
    def getHashValue(self, hashName, key):
        return self.__redis.hget(hashName, key)
    
    def delete(self, hashName):
        return self.__redis.delete(hashName)

    def exists(self, key):
        return self.__redis.exists(key)

    def lenOfHash(self, key):
        return self.__redis.hlen(key)
    
    def flushAll(self):
        return self.__redis.flushall( asynchronous=False)