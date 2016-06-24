
from . import Constants, Parser, Tags

def calculateChecksum(message):
	"""
	Calculates the checksum of a raw message.

	:param message: str
	:return: int
	"""
	checksum = sum(ord(ch) for ch in message)
	return checksum % 256

class FIXMessage(object):
	"""
	Represents a single FIX message, including helpful accessors.
	"""

	def __init__(self, message):
		"""
		Initializes a new instance of FIXMessage with an unparsed message.
		"""
		assert(type(message) is str)

		self._message = message
		self._parsedMessage = Parser.parseMessage(message)

	########## Basic Accessors ##########

	def message(self):
		"""
		Returns the message underlying this object.

		:return: str
		"""
		return self._message

	def parsedMessage(self):
		"""
		Returns the parsed message underlying this message.

		:return: dict
		"""
		return self._parsedMessage

	def get(self, id):
		"""
		Returns the string value of the given tag ID.

		:return: str or None
		"""
		return self._parsedMessage.get(id)

	def getParsed(self, id):
		"""
		Returns the string value of the given tag ID.

		:return: str or None
		"""
		value = self.get(id)
		if value is None:
			return None

		tag = Tags.TAG_ID_TO_TAG.get(id)
		if tag is None:
			return value
		else:
			return tag.type().parse(value)

	def __str__(self):
		"""
		Returns the string underlying this message.

		:return: str
		"""
		return self._message

	def __len__(self):
		"""
		Returns the length of the message as a string.

		:return: int
		"""
		return len(self._message)

	########## Methods ##########

	def calculateChecksum(self):
		"""
		Calculates the checksum of this message, excluding the last tag if it is a checksum.

		:return: int
		"""
		#Remove the checksum tag from consideration
		lastTag = self._message.rfind(Constants.SEPARATOR, 0, -2)
		if self._message[lastTag+1:lastTag+4] == '10=':
			end = lastTag + 1
		else:
			end = len(self._message)

		#Calculate the checksum over the part before the checksum
		return calculateChecksum(self._message[0:end])

	def updateMessage(self):
		"""
		Updates the message to reflect the dictionary (including the checksum, which is also
		updated in the dictionary).
		"""
		#TODO: handle repeating groups
		#TODO: use the type system so this handles lists properly

		#Parts of the message to be joined
		parts = []

		#Create the headers
		headerIDs = [8, 9, 35, 49, 56, 34, 52]
		for headerID in headerIDs:
			value = self.get(headerID)
			if value is not None:
				parts.append('%s=%s%s' % (headerID, value, Constants.SEPARATOR))

		#Write other fields
		for tagID in self._parsedMessage:
			#Skip headers
			if tagID in headerIDs:
				continue

			parts.append('%s=%s%s' % (tagID, self._parsedMessage[tagID], Constants.SEPARATOR))

		#Calculate the partial message for the checksum
		parts.append(Constants.SEPARATOR)
		partialMessage = ''.join(parts)

		#Add the checksum
		checksum = calculateChecksum(partialMessage)
		parts.append(Constants.SEPARATOR)

		self._message = '%s10=%3d%s' % (partialMessage, checksum, Constants.SEPARATOR)

	########## Tag Helpers ##########

	def averagePrice(self):
		"""
		Returns the average price of the message as indicated by tag 6.

		:return: int
		"""
		return self.getParsed(6)

	def bodyLength(self):
		"""
		Returns the body length of the message as indicated by tag 9.

		:return: int
		"""
		return self.getParsed(9)

	def checksum(self):
		"""
		Returns the checksum of the message as indicated by tag 10.

		:return: int
		"""
		return self.getParsed(10)

	def currency(self):
		"""
		Returns the currency of the message as indicated by tag 15.

		:return: str
		"""
		return self.get(15)

	def lastPrice(self):
		"""
		Returns the last price of the message as indicated by tag 31.

		:return: int
		"""
		return self.getParsed(31)

	def sequenceNumber(self):
		"""
		Returns the sequence number of the message as indicated by tag 34.

		:return: int
		"""
		return self.getParsed(34)

	def messageType(self):
		"""
		Returns the type of the message as indicated by tag 35.

		:return: str
		"""
		return self.get(35)

	def price(self):
		"""
		Returns the price of the message as indicated by tag 44.

		:return: float
		"""
		return self.getParsed(44)

	def senderCompID(self):
		"""
		Returns the SenderCompID of the message as indicated by tag 49.

		:return: str
		"""
		return self.get(49)

	def symbol(self):
		"""
		Returns the symbol of the message as indicated by tag 55.

		:return: str
		"""
		return self.get(55)

	def strikePrice(self):
		"""
		Returns the strike price of the message as indicated by tag 202.

		:return: float
		"""
		return self.getParsed(202)

	def securityExchange(self):
		"""
		Returns the security exchange of the message as indicated by tag 207.

		:return: str
		"""
		return self.get(207)

	#TODO: others
