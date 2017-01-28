#!/usr/bin/env python3

import argparse
import gzip
import sys

import Fixie

def getPrettyTagValue(tag, value):
	"""
	Pretty prints a tag value to a string by adding an explanation if it is an enum.

	:param tag: int
	:param value: str
	:return: str
	"""
	enumValues = Fixie.TAG_ENUM_VALUES.get(tag)
	enumValue = ' [%s]' % enumValues.get(value, 'ERROR: Unknown enum value') if enumValues is not None else ''
	return '%s%s' % (value, enumValue)

def printMessage(indent, messageStr):
	"""
	Pretty prints a single (unparsed) FIX message.

	:param indent: int
	:param messageStr: string
	"""
	assert(type(indent) is int)
	assert(type(messageStr) is str)

	#Skip blank lines
	if messageStr == '':
		return

	print('%6d: %s%s' % (indent, messageStr[:100].replace(Fixie.SEPARATOR, '|'), '...' if len(messageStr) > 100 else ''))

	#TODO: error handling
	message = Fixie.FIXMessage(messageStr)
	parsedMessage = message.parsedMessage()
	for k in sorted(parsedMessage.keys()):
		tag = Fixie.TAG_ID_TO_TAG.get(k)
		name = tag.name() if tag is not None else ''

		value = parsedMessage[k]
		valueString = ', '.join(getPrettyTagValue(k, item) for item in value) if type(value) is list else getPrettyTagValue(k, value)

		extra = ''
		if tag is not None and tag.id() == 10:
			extra = ' (calculated checksum = %d)' % message.calculateChecksum()

		print('%28s [%4d] = %s%s' % (name, k, valueString, extra))

	print('')

def printFile(file):
	"""
	Pretty prints the contents of a file, line by line.
	"""
	for n, message in enumerate(file):
		#Decode if necessary
		if sys.version_info >= (3,):
			message = message.decode('utf8')

		#Remove newlines
		if len(message) > 0 and message[-1] == '\n':
			message = message[:-1]

		printMessage(n, message)

def main():
	parser = argparse.ArgumentParser(description='FIX Viewer')
	parser.add_argument('file', nargs='?', help='FIX file to view.')

	arguments = parser.parse_args(sys.argv[1:])

	#Read from the file name passed as an argument, or stdin if none is passed
	if arguments.file is None:
		printFile(sys.stdin)
	else:
		openF = gzip.open if arguments.file.endswith('.gz') else open
		with openF(arguments.file, 'rb') as fixFile:
			printFile(fixFile)

	return 0

if __name__ == '__main__':
	sys.exit(main())
