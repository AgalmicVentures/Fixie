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
