#!/usr/bin/env python3

import argparse
import csv
import sys

def main():
	parser = argparse.ArgumentParser(description='Tag Mapping Code Generator')
	parser.add_argument('file', help='Tag mapping CSV file.')

	arguments = parser.parse_args(sys.argv[1:])

	header = True
	with open(arguments.file) as tagsCsvFile:
		for row in csv.reader(tagsCsvFile):
			#Skip the header
			if header:
				header = False
				continue

			#Break up the row
			id, name, typeName, repeatingHeaderId, vendor, description, _ = row

			#Write the tag constructor
			print("\tFIXTag(%4s, '%s', typeName=%s, repeatingHeaderId=%s, vendor=%s%s)," % (
				id, name,
				"'%s'" % typeName if typeName != '' else 'None',
				str(repeatingHeaderId) if repeatingHeaderId != '' else 'None',
				"'%s'" % vendor if vendor != '' else 'None',
				", description=%s" % description.__repr__() if description != '' else '', #__repr__ is necessary to escape single quotes
			))

	return 0

if __name__ == '__main__':
	sys.exit(main())
