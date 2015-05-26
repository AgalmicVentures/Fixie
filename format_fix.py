#!/usr/bin/env python3

import io
import sys

import fixie

def main():
	if len(sys.argv) <= 1:
		print('Ussage: format_fix.py <FILENAME>')
		return 1

	with io.open(sys.argv[1]) as fixFile:
		for n, message in enumerate(fixFile):
			if message == '':
				continue

			print('%6d: %s%s' % (n, message[:100], '...' if len(message) > 100 else ''))

			#TODO: error handling
			parsedMessage = fixie.parseMessage(message)
			for k in sorted(parsedMessage.keys()):
				name = fixie.TAG_ID_TO_NAME.get(k, '')
				values = ', '.join(parsedMessage[k])
				print('\t%20s [%4d] = %s' % (name, k, values))

			print()

	return 0

if __name__ == '__main__':
	sys.exit(main())
