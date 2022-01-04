
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

from . import Constants

def parseMessage(message, separator=Constants.SEPARATOR, valueSeparator=Constants.VALUE_SEPARATOR):
	"""
	Parses a single FIX message into a dictionary of ID's to (lists of) values.

	:param message: str
	:param separator: str Separator, by default '\x01'
	:param valueSeparator: str Key/value separator, by default '='
	:return: dict of int -> list[string] (ID -> values)
	"""
	assert(type(message) is str)
	assert(type(separator) is str)
	assert(len(separator) > 0)
	assert(type(valueSeparator) is str)
	assert(len(valueSeparator) > 0)

	if len(message) == 0 or message[-1] != separator:
		raise ValueError('FIX Message is invalid (length=%d): "%s"' % (
			len(message), message.replace(separator, '|')))

	parsedMessage = {}

	#TODO: correctly handle binary fields by using the prior length field
	n = 0
	while n < len(message):
		#Parse the next tag
		nextValueSeparator = message.index(valueSeparator, n)
		tagStr = message[n:nextValueSeparator]
		tag = int(tagStr)

		#Parse the next value
		nextSeparator = message.index(separator, nextValueSeparator)
		value = message[nextValueSeparator + 1:nextSeparator]
		n = nextSeparator + 1

		#Update the output
		#  Insert if there is nothing
		currentValue = parsedMessage.get(tag)
		if currentValue is None:
			parsedMessage[tag] = value

		#  Or add on if it's a list
		elif type(currentValue) is list:
			currentValue.append(value)

		#  But if it's just a scalar, make a list
		else:
			parsedMessage[tag] = [parsedMessage[tag], value]

	return parsedMessage
