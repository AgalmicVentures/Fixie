#!/usr/bin/env python3

import csv
import io
import sys

def main():
	#Read from the file name passed as an argument
	if len(sys.argv) <= 1:
		print('Usage: generate_tag_mappings.py <TAGS.CSV>')
		return 1

	header = True
	with io.open(sys.argv[1]) as tagsCsvFile:
		for row in csv.reader(tagsCsvFile):
			#Skip the header
			if header:
				header = False
				continue

			#Break up the row
			id, name, fixType, repeatingHeaderId, vendor, description, _ = row

			#Write the tag constructor
			print("\tFIXTag(%4s, '%s', repeatingHeaderId=%s, vendor=%s%s)," % (
				id, name,
				str(repeatingHeaderId) if repeatingHeaderId != '' else 'None',
				"'%s'" % vendor if vendor != '' else 'None',
				", description=%s" % description.__repr__() if description != '' else '', #__repr__ is necessary to escape single quotes
			))

	return 0

if __name__ == '__main__':
	sys.exit(main())
