from abc import	ABC, abstractmethod

class BaseCommunicator(ABC):
	@abstractmethod
	def	log(self, index_name: str, doc:	dict):
		pass