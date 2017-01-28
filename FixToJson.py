#!/usr/bin/env python3

import argparse
import json
import sys

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
		with open(arguments.file) as fixFile:
			printFile(fixFile)

	return 0

if __name__ == '__main__':
	sys.exit(main())
