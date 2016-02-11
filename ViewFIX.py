#!/usr/bin/env python3

import io
import sys

import Fixie

def getPrettyTagValue(tag, value):
	enumValues = Fixie.TAG_ENUM_VALUES.get(tag)
	enumValue = ' [%s]' % enumValues.get(value, 'ERROR: Unknown enum value') if enumValues is not None else ''
	return '%s%s' % (value, enumValue)

def printMessage(indent, messageStr):
	"""
	Pretty prints a single (unparsed) FIX message.

	:param indent: int
	:param message: string
	"""
	assert(type(indent) is int)

	if messageStr == '':
		return

	print('%6d: %s%s' % (indent, messageStr[:100].replace(Fixie.SEPARATOR, '|'), '...' if len(messageStr) > 100 else ''))

	#TODO: error handling
	message = Fixie.FIXMessage(messageStr)
	parsedMessage = message.parsedMessage()
	for k in sorted(parsedMessage.keys()):
		tag = Fixie.TAG_ID_TO_NAME.get(k)
		name = tag.name() if tag is not None else ''

		value = parsedMessage[k]
		valueString = ', '.join(getPrettyTagValue(k, item) for item in value) if type(value) is list else getPrettyTagValue(k, value)

		print('%28s [%4d] = %s' % (name, k, valueString))

	print()

def printFile(file):
	"""
	Pretty prints the contents of a file, line by line.
	"""
	for n, message in enumerate(file):
		printMessage(n, message)

def main():
	#Read from the file name passed as an argument, or stdin if none is passed
	if len(sys.argv) <= 1:
		printFile(sys.stdin)
	else:
		with io.open(sys.argv[1]) as fixFile:
			printFile(fixFile)

	return 0

if __name__ == '__main__':
	sys.exit(main())
