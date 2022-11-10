from abc import	ABC, abstractmethod

class Databse(ABC):

	@abstractmethod
	def	setSetValue(self, set_name,	*values):
		pass

	@abstractmethod
	def	removeSetValue(self, setName, *values):
		pass
	
	@abstractmethod	  
	def	setHashValue(self, hash_name, key, value):
		pass
	
	@abstractmethod	  
	def	incrementHashValueBy(self, hash_name, key, amount=1):
		pass

	@abstractmethod	
	def	getHash(self, key):
		pass
	
	@abstractmethod	  
	def	getHashValue(self, hash_name, key):
		pass
	
	@abstractmethod	  
	def	delete(self, hash_name):
		pass

	@abstractmethod	  
	def	exists(self, key):
		pass

	@abstractmethod	  
	def	lenOfHash(self,	key):
		pass
	
	@abstractmethod	  
	def	flushAll(self):
		pass