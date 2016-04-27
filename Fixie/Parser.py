
from . import Constants

#TODO: parse a single character at a time instead of using lots of a nasty splits
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
	for k, v in (d.split(valueSeparator, 2) for d in message.split(separator)[:-1]):
		k = int(k)
		currentValue = parsedMessage.get(k)

		#Insert if there is nothing
		if currentValue is None:
			parsedMessage[k] = v

		#Or add on if it's a list
		elif type(currentValue) is list:
			currentValue.append(v)

		#But if it's just a scalar, make a list
		else:
			parsedMessage[k] = [parsedMessage[k], v]

	return parsedMessage
