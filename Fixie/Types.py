
import re

from . import Decoder, Encoder

class FIXTag:
	'''
	Represents a FIX tag (used to automate parsing).
	'''

	def __init__(self, id, name, repeatingHeaderId=None, vendor=None, description=None):
		'''
		Initializes a new instance of FIXTag.
		'''
		assert(type(id) is int)
		assert(0 < id)
		assert(id < 10000)
		assert(type(name) is str)
		assert(re.match('[A-Z0-9][a-zA-Z0-9]*', name) is not None)
		assert(repeatingHeaderId is None or type(repeatingHeaderId) is int)
		assert(vendor is None or type(vendor) is str)
		assert(description is None or type(description) is str)

		self._id = id
		self._name = name
		self._repeatingHeaderId = repeatingHeaderId
		self._vendor = vendor
		self._description = description

	def __str__(self):
		'''
		Returns a string representing this tag.
		:return string
		'''
		return '[%4d] %s' % (self._id, self._name)

	def __repr__(self):
		'''
		Returns a more complete string representing this tag.
		:return string
		'''
		return '[%4d] %s rhn=%s v=%s d=%s' % (self._id, self._name, self._repeatingHeaderId, self._vendor, self._description)

	def id(self):
		'''
		Returns the ID of the tag.
		:return int
		'''
		return self._id

	def name(self):
		'''
		Returns the name of the tag.
		:return string
		'''
		return self._name

	def repeatingHeaderId(self):
		'''
		Returns the ID of the repeating group header if this is a part of one.
		:return string
		'''
		return self._repeatingHeaderId

	def vendor(self):
		'''
		Returns the vendor of the tag.
		:return string
		'''
		return self._vendor

	def description(self):
		'''
		Returns a description of the tag.
		:return string
		'''
		return self._description

class FIXMessage:
	'''
	Represents a single FIX message, including helpful accessors.
	'''

	def __init__(self, message):
		'''
		Initializes a new instance of FIXMessage with an unparsed message.
		'''
		assert(type(message) is str)

		self._message = message
		self._parsedMessage = decoder.parseMessage(message)

	########## Basic Accessors ##########

	def message(self):
		'''
		Returns the message underlying this object.
		:return string
		'''
		return self._message

	def parsedMessage(self):
		'''
		Returns the parsed message underlying this message.
		:return dict
		'''
		return self._parsedMessage

	def __str__(self):
		'''
		Returns the string underlying this message.
		:return string
		'''
		return self._message

	def __len__(self):
		'''
		Returns the length of the message as a string.
		:return int
		'''
		return len(self._message)

	########## Tag Helpers ##########

	def _parsePrice(self, price):
		#TODO: is this correct?
		return float(price)

	def averagePrice(self):
		'''
		Returns the average price of the message as indicated by tag 6.
		:return int
		'''
		rawValue = self._parsedMessage.get(6)
		return None if rawValue is None else self._parsePrice(rawValue)

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

	def currency(self):
		'''
		Returns the currency of the message as indicated by tag 15.
		:return string
		'''
		return self._parsedMessage.get(15)

	def lastPrice(self):
		'''
		Returns the last price of the message as indicated by tag 31.
		:return int
		'''
		rawValue = self._parsedMessage.get(31)
		return None if rawValue is None else self._parsePrice(rawValue)

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

	def price(self):
		'''
		Returns the price of the message as indicated by tag 44.
		:return int
		'''
		rawValue = self._parsedMessage.get(44)
		return None if rawValue is None else self._parsePrice(rawValue)

	def senderCompID(self):
		'''
		Returns the SenderCompID of the message as indicated by tag 49.
		:return string
		'''
		return self._parsedMessage.get(49)

	def symbol(self):
		'''
		Returns the symbol of the message as indicated by tag 55.
		:return string
		'''
		return self._parsedMessage.get(55)

	def strikePrice(self):
		'''
		Returns the strike price of the message as indicated by tag 202.
		:return int
		'''
		rawValue = self._parsedMessage.get(202)
		return None if rawValue is None else self._parsePrice(rawValue)

	def securityExchange(self):
		'''
		Returns the security exchange of the message as indicated by tag 207.
		:return string
		'''
		return self._parsedMessage.get(207)

	#TODO: others
