
import constants

#TODO: parse a single character at a time instead of using lots of a nasty splits
def parseMessage(message, separator=constants.SEPARATOR):
	'''
	Parses a single FIX message into a dictionary of ID's to lists of values.
	:param message: string
	:return: dict of int -> list[string] (ID -> values)
	'''
	assert(len(separator) > 0)

	parsedMessage = {}
	for k, v in (d.split('=', 2) for d in message.split(separator)[:-1]):
		k = int(k)
		if k not in parsedMessage:
			parsedMessage[k] = []

		parsedMessage[k].append(v)
	return parsedMessage
