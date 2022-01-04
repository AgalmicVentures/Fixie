#!/usr/bin/env python3

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

import argparse
import gzip
import sys

import inspect
import os
_currentFile = os.path.abspath(inspect.getfile(inspect.currentframe()))
_currentDir = os.path.dirname(_currentFile)
_parentDir = os.path.dirname(os.path.dirname(_currentDir))
sys.path.insert(0, _parentDir)

import Fixie

NO_COLOR = '\033[00m'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
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

def printMessage(indent, messageStr, colorize=None):
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

	#Colorize by default on TTY's, not otherwise
	if colorize is None:
		colorize = sys.stdout.isatty()

	#Print the message
	color = CYAN
	print('%s%6d: %s%s' % (color if colorize else '', indent,
		messageStr[:100].replace(Fixie.SEPARATOR, '|'), '...' if len(messageStr) > 100 else ''),
		NO_COLOR if colorize else '')

	bodyLengthTag = Fixie.TAG_NAME_TO_TAG['BodyLength']
	checksumTag = Fixie.TAG_NAME_TO_TAG['CheckSum']

	#TODO: error handling
	message = Fixie.FIXMessage(messageStr)
	parsedMessage = message.parsedMessage()
	for k in sorted(parsedMessage.keys()):
		extra = ''
		color = NO_COLOR if colorize else ''

		value = parsedMessage[k]
		if type(value) is list:
			separator = ', ' if len(value) < 6 else ',\n' + ' ' * 39
			valueString = separator.join(getPrettyTagValue(k, item) for item in value)
		else:
			valueString = getPrettyTagValue(k, value)

		tag = Fixie.TAG_ID_TO_TAG.get(k)
		if tag is None:
			name = ''
			color = YELLOW
		else:
			name = tag.name()

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

			#Is it part of a repeating group?
			if tag.repeatingHeaderId() is not None:
				headerValue = parsedMessage.get(tag.repeatingHeaderId())
				if headerValue is None:
					extra = 'No group header found [tag %d]' % tag.repeatingHeaderId()
					color = RED
				elif parsedValue is not None:
					try:
						#Header counts should be parseable, and match the count of items
						parsedHeaderValue = int(headerValue)
						valueLength = len(parsedValue) if type(parsedValue) is list else 1
						if parsedHeaderValue != valueLength:
							extra = 'Group header [tag %d] disagrees with item count [%d vs %d]' % (
								tag.repeatingHeaderId(), parsedHeaderValue, valueLength)
							color = YELLOW
					except ValueError:
						color = YELLOW

			#Extra handling for certain tags
			if tag.id() == bodyLengthTag.id():
				bodyLengthStr = '%s%d=%s' % (Fixie.SEPARATOR, bodyLengthTag.id(), value)
				bodyLengthIndex = messageStr.index(bodyLengthStr)
				checksumIndex = messageStr.index('%s%d=' % (Fixie.SEPARATOR, checksumTag.id()))
				calculatedLength = checksumIndex - bodyLengthIndex - len(bodyLengthStr)
				extra = 'Calculated length = %d' % calculatedLength
				color = GREEN if parsedValue == calculatedLength else RED
			elif tag.id() == checksumTag.id():
				calculatedChecksum = message.calculateChecksum()
				extra = 'Calculated checksum = %d' % calculatedChecksum
				color = GREEN if parsedValue == calculatedChecksum else RED

		print('%s%28s [%5d] = %s%s%s' % (color if colorize else '',
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
	parser.add_argument('-c', '--colorize', action='store_true', default=None,
		help='Colorize the output (default True in a TTY, false otherwise).')
	parser.add_argument('file', nargs='?', help='FIX file to view.')

	arguments = parser.parse_args(sys.argv[1:])

	#Read from the file name passed as an argument, or stdin if none is passed
	if arguments.file is None:
		printFile(sys.stdin, colorize=arguments.colorize)
	else:
		openF = gzip.open if arguments.file.endswith('.gz') else open
		try:
			with openF(arguments.file, 'rb') as fixFile:
				printFile(fixFile, colorize=arguments.colorize)
		except BrokenPipeError:
			pass #These happen when you pipe to less and quit

	return 0

if __name__ == '__main__':
	sys.exit(main())
