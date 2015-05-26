#!/usr/bin/env python3

import io
import sys

import fixie

def printMessage(n, message):
	if message == '':
		return

	print('%6d: %s%s' % (n, message[:100].replace(fixie.SEPARATOR, '|'), '...' if len(message) > 100 else ''))

	#TODO: error handling
	parsedMessage = fixie.parseMessage(message)
	for k in sorted(parsedMessage.keys()):
		name = fixie.TAG_ID_TO_NAME.get(k, '')
		values = ', '.join(parsedMessage[k])
		print('\t%20s [%4d] = %s' % (name, k, values))

	print()

def printFile(file):
	for n, message in enumerate(file):
		printMessage(n, message)

def main():
	if len(sys.argv) <= 1:
		printFile(sys.stdin)
	else:
		with io.open(sys.argv[1]) as fixFile:
			printFile(fixFile)

	return 0

if __name__ == '__main__':
	sys.exit(main())
