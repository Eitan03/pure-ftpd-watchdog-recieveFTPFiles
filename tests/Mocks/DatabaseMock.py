from unittest.mock import Mock

from .DynamicObject import DynamicObject



def createDatabaseMock(database: dict):
	return	DynamicObject({ **{
    		'setHashValue': Mock(return_value=True),
    		'getHash': Mock(return_value=None),
    		'delete': Mock(return_value=True),
    		'exists': Mock(return_value=False),
    		'lenOfHash': Mock(return_value=0),
    		'flushAll': Mock(return_value=True)
		}, **database })