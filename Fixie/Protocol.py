
# Copyright (c) 2015-2022 Agalmic Ventures LLC (www.agalmicventures.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

	def account(self):
		"""
		Returns the account of the message as indicated by tag 1.

		:return: str
		"""
		return self.get(1)

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

	def executionID(self):
		"""
		Returns the execution ID of the message as indicated by tag 17.

		:return: str
		"""
		return self.get(17)

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

	def orderID(self):
		"""
		Returns the order ID of the message as indicated by tag 37.

		:return: str
		"""
		return self.get(37)

	def possibleDuplicateFlag(self):
		"""
		Returns the possible duplicate flag of the message as indicated by tag 43.

		:return: bool
		"""
		return self.getParsed(43)

	def price(self):
		"""
		Returns the price of the message as indicated by tag 44.

		:return: float
		"""
		return self.getParsed(44)

	def securityID(self):
		"""
		Returns the security ID of the message as indicated by tag 48.

		:return: str
		"""
		return self.get(48)

	def senderCompID(self):
		"""
		Returns the SenderCompID of the message as indicated by tag 49.

		:return: str
		"""
		return self.get(49)

	def senderSubID(self):
		"""
		Returns the SenderSubID of the message as indicated by tag 50.

		:return: str
		"""
		return self.get(50)

	def side(self):
		"""
		Returns the side of the message as indicated by tag 54.

		:return: str
		"""
		return self.get(54)

	def symbol(self):
		"""
		Returns the symbol of the message as indicated by tag 55.

		:return: str
		"""
		return self.get(55)

	def targetCompID(self):
		"""
		Returns the TargetCompID of the message as indicated by tag 56.

		:return: str
		"""
		return self.get(56)

	def targetSubID(self):
		"""
		Returns the TargetSubID of the message as indicated by tag 57.

		:return: str
		"""
		return self.get(57)

	def timeInForce(self):
		"""
		Returns the symbol of the message as indicated by tag 55.

		:return: str
		"""
		return self.get(59)

	def minimumQuantity(self):
		"""
		Returns the minimum quantity of the message as indicated by tag 110.

		:return: int
		"""
		return self.get(110)

	def leavesQuantity(self):
		"""
		Returns the leaves quantity of the message as indicated by tag 151.

		:return: int
		"""
		return self.getParsed(151)

	def securityType(self):
		"""
		Returns the security type of the message as indicated by tag 167.

		:return: str
		"""
		return self.get(167)

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

	def contractMultiplier(self):
		"""
		Returns the contract multiplier of the message as indicated by tag 231.

		:return: float
		"""
		return self.get(231)

	#TODO: others
