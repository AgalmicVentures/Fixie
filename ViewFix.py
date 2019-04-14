#!/usr/bin/env python3

# Copyright (c) 2015-2019 Agalmic Ventures LLC (www.agalmicventures.com)
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

import argparse
import gzip
import sys

import Fixie

NO_COLOR = '\033[00m'
RED = '\033[1;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'

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

def printMessage(indent, messageStr, colorize=False):
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

	#Print the message
	color = CYAN
	print('%s%6d: %s%s' % (color if colorize else '', indent,
		messageStr[:100].replace(Fixie.SEPARATOR, '|'), '...' if len(messageStr) > 100 else ''),
		NO_COLOR if colorize else '')

	checksumTag = Fixie.TAG_NAME_TO_TAG['CheckSum']

	#TODO: error handling
	message = Fixie.FIXMessage(messageStr)
	parsedMessage = message.parsedMessage()
	for k in sorted(parsedMessage.keys()):
		extra = ''
		color = NO_COLOR if colorize else ''

		tag = Fixie.TAG_ID_TO_TAG.get(k)
		name = tag.name() if tag is not None else ''

		value = parsedMessage[k]
		valueString = ', '.join(getPrettyTagValue(k, item) for item in value) if type(value) is list else getPrettyTagValue(k, value)

		#Does the value parse correctly?
		try:
			if type(value) is list:
				parsedValue = [tag.type().parse(item) for item in value]
			else:
				parsedValue = tag.type().parse(value)
		except Exception as e:
			parsedValue = None

			extra = str(e)
			color = YELLOW

		#Extra handling for certain tags
		if tag is not None:
			if tag.id() == checksumTag.id():
				calculatedChecksum = message.calculateChecksum()
				extra = 'Calculated checksum = %d' % calculatedChecksum
				color = GREEN if parsedValue == calculatedChecksum else RED

		print('%s%28s [%4d] = %s%s%s' % (color if colorize else '',
			name, k, valueString, ' (%s)' % extra if extra != '' else '', NO_COLOR if colorize else ''))

	print('')

def printFile(file, colorize=False):
	"""
	Pretty prints the contents of a file, line by line.

	:param file: file object to print
	:param colorize: bool Flag indicating whether to colorize the output.
	"""
	for n, message in enumerate(file):
		#Decode if necessary
		if sys.version_info >= (3,):
			message = message.decode('utf8')

		#Remove newlines
		if len(message) > 0 and message[-1] == '\n':
			message = message[:-1]

		printMessage(n, message, colorize=colorize)

def main():
	parser = argparse.ArgumentParser(description='FIX Viewer')
	parser.add_argument('-c', '--colorize', action='store_true',
		help='Colorize the output.')
	parser.add_argument('file', nargs='?', help='FIX file to view.')

	arguments = parser.parse_args(sys.argv[1:])

	#Read from the file name passed as an argument, or stdin if none is passed
	if arguments.file is None:
		printFile(sys.stdin, colorize=arguments.colorize)
	else:
		openF = gzip.open if arguments.file.endswith('.gz') else open
		with openF(arguments.file, 'rb') as fixFile:
			printFile(fixFile, colorize=arguments.colorize)

	return 0

if __name__ == '__main__':
	sys.exit(main())
