
import encoder

class FIXMessage:

	def __init__(self, parsedMessage):
		self._parsedMessage = parsedMessage

	def parsedMessage(self):
		return self._parsedMessage

	#TODO: helpers

	def __str__(self):
		return encoder.formatMessage(self._parsedMessage)
