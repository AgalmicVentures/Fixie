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
try:
	import ujson as json
except ImportError:
	import json
import sys

import inspect
import os
_currentFile = os.path.abspath(inspect.getfile(inspect.currentframe()))
_currentDir = os.path.dirname(_currentFile)
_parentDir = os.path.dirname(os.path.dirname(_currentDir))
sys.path.insert(0, _parentDir)

import Fixie

def printMessage(messageStr):
	"""
	Pretty prints a single (unparsed) FIX message.

	:param messageStr: string
	"""
	assert(type(messageStr) is str)

	#Skip blank lines
	if messageStr == '':
		return

	#TODO: error handling
	message = Fixie.FIXMessage(messageStr)
	print(json.dumps(message.parsedMessage()))

def printFile(file):
	"""
	Prints the contents of a file, line by line.
	"""
	for message in file:
		#Decode if necessary
		if sys.version_info >= (3,):
			message = message.decode('utf8')

		#Remove newlines
		if len(message) > 0 and message[-1] == '\n':
			message = message[:-1]

		printMessage(message)

def main():
	parser = argparse.ArgumentParser(description='FIX to JSON Converter')
	parser.add_argument('file', nargs='?', help='FIX file to convert.')

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
