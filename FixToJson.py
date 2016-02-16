#!/usr/bin/env python3

import io
import json
import sys

import Fixie

def printMessage(messageStr):
	"""
	Pretty prints a single (unparsed) FIX message.

	:param messageStr: string
	"""
	assert(type(messageStr) is str)
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
		printMessage(message)

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
