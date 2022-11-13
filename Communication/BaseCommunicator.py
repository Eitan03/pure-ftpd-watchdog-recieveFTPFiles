from abc import	ABC, abstractmethod

class BaseCommunicator(ABC):
	@abstractmethod
	def	log(self, topic_name: str, doc:	dict):
		pass