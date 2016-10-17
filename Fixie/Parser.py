
from . import Constants

def parseMessage(message, separator=Constants.SEPARATOR, valueSeparator=Constants.VALUE_SEPARATOR):
	"""
	Parses a single FIX message into a dictionary of ID's to lists of values.

	:param message: string
	:return: dict of int -> list[string] (ID -> values)
	"""
	assert(type(message) is str)
	assert(type(separator) is str)
	assert(len(separator) > 0)
	assert(type(valueSeparator) is str)
	assert(len(valueSeparator) > 0)
	assert(len(message) > 0)

	#TODO: better validation
	if message[-1] != separator:
		raise ValueError('FIX Message is invalid (length=%d): "%s"' % (
			len(message), message.replace(separator, '|')))

	parsedMessage = {}

	#TODO: correctly handle binary fields by using the prior length field
	n = 0
	while n < len(message):
		nextValueSeparator = message.index(valueSeparator, n)
		tagStr = message[n:nextValueSeparator]
		tag = int(tagStr)

		nextSeparator = message.index(separator, nextValueSeparator)
		value = message[nextValueSeparator + 1:nextSeparator]

		n = nextSeparator + 1

		#Insert if there is nothing
		currentValue = parsedMessage.get(tag)
		if currentValue is None:
			parsedMessage[tag] = value

		#Or add on if it's a list
		elif type(currentValue) is list:
			currentValue.append(value)

		#But if it's just a scalar, make a list
		else:
			parsedMessage[tag] = [parsedMessage[tag], value]

	return parsedMessage
