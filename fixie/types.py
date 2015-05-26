
from . import encoder

class FIXMessage:
	'''
	Represents a single FIX message, including helpful accessors.
	'''

	def __init__(self, parsedMessage):
		'''
		Initializes a new instance of FIXMessage with an already parsed message.
		'''
		self._parsedMessage = parsedMessage

	########## Basic Accessors ##########

	def parsedMessage(self):
		'''
		Returns the parsed message underlying this object.
		:return dict
		'''
		return self._parsedMessage

	def __str__(self):
		'''
		Reifies the FIX message back into a string.
		'''
		return encoder.formatMessage(self._parsedMessage)

	########## Tag Helpers ##########

	def bodyLength(self):
		'''
		Returns the body length of the message as indicated by tag 9.
		:return int
		'''
		rawValue = self._parsedMessage.get(9)
		return None if rawValue is None else int(rawValue)

	def checkSum(self):
		'''
		Returns the checksum of the message as indicated by tag 10.
		:return int
		'''
		rawValue = self._parsedMessage.get(10)
		return None if rawValue is None else int(rawValue)

	def sequenceNumber(self):
		'''
		Returns the sequence number of the message as indicated by tag 34.
		:return int
		'''
		rawValue = self._parsedMessage.get(34)
		return None if rawValue is None else int(rawValue)

	def messageType(self):
		'''
		Returns the type of the message as indicated by tag 35.
		:return string
		'''
		return self._parsedMessage.get(35)

	#TODO: others
