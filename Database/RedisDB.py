import redis

from Database.Database import Databse


class RedisDB(Databse):
    def __init__(self):
        self.__redis = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def setSetValue(self, set_name, *values):
        return self.__redis.sadd(set_name, *values)

    def removeSetValue(self, setName, *values):
        return self.__redis.srem(setName, *values)
    
    def setHashValue(self, hash_name, key, value):
        print(f'REDIS: saved ({key}: {value}) into hash {hash_name}')
        return self.__redis.hset(hash_name, key, value)
    
    def incrementHashValueBy(self, hash_name, key, amount=1):
        print(f'REDIS: incremented {key} by {amount} of hash {hash_name}')
        return self.__redis.hincrby(hash_name, key, amount)

    def getHash(self, key):
        return self.__redis.hgetall(key)
    
    def getHashValue(self, hash_name, key):
        return self.__redis.hget(hash_name, key)
    
    def delete(self, hash_name):
        return self.__redis.delete(hash_name)

    def exists(self, key):
        return self.__redis.exists(key)

    def lenOfHash(self, key):
        return self.__redis.hlen(key)
    
    def flushAll(self):
        return self.__redis.flushall( asynchronous=False)