
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

#TODO: support data
#TODO: support patterns (FIX 5.0)
#TODO: implement UTC

import datetime

########### Functions ##########

#Not everything should require an object

def _tryParseDateTime(value, formats):
	"""
	Attempts to parse a datetime using a variety of formats.

	:param value: str
	:param formats: list of str
	:return: datetime.datetime
	"""
	for format in formats:
		try:
			return datetime.datetime.strptime(value, format)
		except ValueError:
			pass #Nothing to do

	raise ValueError('Invalid datetime format for "%s"' % value)

def parseBool(value):
	"""
	Parse a boolean, which in FIX is either a single 'Y' or 'N'.

	:param value: the tag value (should be 1 character)
	:return: bool
	"""
	if value == 'Y':
		return True
	elif value == 'N':
		return False
	else:
		raise ValueError('FIX boolean values must be Y or N (got %s)' % value)

def parseLocalMarketDate(value):
	"""
	Parses a FIX LocalMktDate in the YYYYMMDD format.

	:param value: str
	:return: datetime.date
	"""
	return datetime.datetime.strptime(value, '%Y%m%d').date()

def parseMonthYear(value):
	"""
	Parses a FIX MonthYear value (usually in the YYYYMM format).

	:param value: str
	:return: datetime.date
	"""
	#Handle values of the form YYYYMMw[1-5]
	if len(value) == 8 and value[-2] == 'w':
		try:
			d = datetime.datetime.strptime(value[:6], '%Y%m').date()
			w = int(value[-1])
			return d.replace(day=7 * (w - 1) + 1)
		except ValueError:
			return None

	#Most often, this path will be taken
	d = _tryParseDateTime(value, [
		'%Y%m%d',
		'%Y%m',
	])
	return d.date() if d is not None else None

def parseUTCTimestamp(value):
	"""
	Parses a FIX UTCTimestamp value.

	:param value: str
	:return: datetime.datetime
	"""
	return _tryParseDateTime(value, [
		'%Y%m%d-%H:%M:%S',
		'%Y%m%d-%H:%M:%S.%f',

		'%Y%m%d%H%M%S',
		'%Y%m%d%H%M%S%f',
	])

def parseUTCDateOnly(value):
	"""
	Parses a FIX UTCDateOnly value.

	:param value: str
	:return: datetime.date
	"""
	d = _tryParseDateTime(value, [
		'%Y%m%d',
		'%Y%m',
	])
	return d.date() if d is not None else None

def parseUTCTimeOnly(value):
	"""
	Parses a FIX UTCTimeOnly value.

	:param value: str
	:return: datetime.time
	"""
	d = _tryParseDateTime(value, [
		'%H:%M:%S',
		'%H:%M:%S.%f',

		'%H%M%S',
		'%H%M%S%f',
	])
	return d.time() if d is not None else None

########### Base Types ##########

class FIXType(object):
	"""
	Generic interface for types in FIX.
	"""

	def name(self):
		"""
		Returns the name of the type.

		:return: str
		"""
		raise NotImplementedError('FIXType.name is pure virtual')

	def type(self):
		"""
		Returns the tags underlying type.

		:return type
		"""
		raise NotImplementedError('FIXType.type is pure virtual')

	def parse(self, value):
		"""
		Parse a value into its real type.

		:param value: str
		:return (whatever the type is)
		"""
		raise NotImplementedError('FIXType.parse is pure virtual')

	#TODO: writing?

class FIXChar(FIXType):
	"""
	Represents the char type in FIX.
	"""

	def name(self):
		return 'char'

	def type(self):
		return str

	def parse(self, value):
		if len(value) != 1:
			raise ValueError('FIX char values must be length 1: %s' % value)

		return value

class FIXData(FIXType):
	"""
	Represents the data type in FIX.
	"""

	def name(self):
		return 'data'

	def type(self):
		return str

	def parse(self, value):
		#TODO: this is kind of a punt since it really requires handling in the parser
		return value

class FIXFloat(FIXType):
	"""
	Represents the float type in FIX.
	"""

	def name(self):
		return 'float'

	def type(self):
		return float

	def parse(self, value):
		return float(value)

class FIXInt(FIXType):
	"""
	Represents the int type in FIX.
	"""

	def name(self):
		return 'int'

	def type(self):
		return int

	def parse(self, value):
		return int(value)

class FIXString(FIXType):
	"""
	Represents the string type in FIX.
	"""

	def name(self):
		return 'String'

	def type(self):
		return str

	def parse(self, value):
		return value

########### Derived Types ##########

#char

class FIXBoolean(FIXChar):
	"""
	Represents the Boolean type in FIX.
	"""

	def name(self):
		return 'Boolean'

	def type(self):
		return bool

	def parse(self, value):
		return parseBool(value)

#float

class FIXAmt(FIXFloat):
	"""
	Represents the Amt type in FIX.
	"""

	def name(self):
		return 'Amt'

class FIXPercentage(FIXFloat):
	"""
	Represents the Percentage type in FIX.
	"""

	def name(self):
		return 'Percentage'

class FIXPrice(FIXFloat):
	"""
	Represents the Price type in FIX.
	"""

	def name(self):
		return 'Price'

class FIXPriceOffset(FIXFloat):
	"""
	Represents the PriceOffset type in FIX.
	"""

	def name(self):
		return 'PriceOffset'

class FIXQty(FIXFloat):
	"""
	Represents the Qty type in FIX.
	"""

	def name(self):
		return 'Qty'

#int

class FIXDayOfMonth(FIXInt):
	"""
	Represents the DayOfMonth in FIX.
	"""

	def name(self):
		return 'DayOfMonth'

	def parse(self, value):
		value = FIXInt.parse(self, value)
		if value < 1 or 31 < value:
			raise ValueError('FIX DayOfMonth must be between 1 and 31 inclusive')

		return value

class FIXLength(FIXInt):
	"""
	Represents the Length type in FIX.
	"""

	def name(self):
		return 'Length'

	def parse(self, value):
		value = FIXInt.parse(self, value)
		if value < 1:
			raise ValueError('FIX Length must be postive')

		return value

class FIXNumInGroup(FIXInt):
	"""
	Represents the NumInGroup (number in repeating group) type in FIX.
	"""

	def name(self):
		return 'NumInGroup'

	def parse(self, value):
		value = FIXInt.parse(self, value)
		if value < 1:
			raise ValueError('FIX NumInGroup must be postive')

		return value

class FIXSeqNum(FIXInt):
	"""
	Represents the SeqNum type in FIX.
	"""

	def name(self):
		return 'SeqNum'

	def parse(self, value):
		value = FIXInt.parse(self, value)
		if value < 1:
			raise ValueError('FIX SeqNum must be postive')

		return value

class FIXTagNum(FIXInt):
	"""
	Represents the SeqNum type in FIX.
	"""

	def name(self):
		return 'TagNum'

	def parse(self, value):
		value = FIXInt.parse(self, value)
		if value < 1:
			raise ValueError('FIX TagNum must be postive')

		if value[0] == '0':
			raise ValueError('FIX TagNum must not have leading zeroes')

		return value

#String

class FIXCountry(FIXString):
	"""
	Represents the country type in FIX (ISO 3166 codes).
	"""

	def name(self):
		return 'Country'

	def parse(self, value):
		if len(value) != 2:
			raise ValueError('FIX currency values must be 2 characters: %s', value)

		return value

class FIXCurrency(FIXString):
	"""
	Represents the currency type in FIX (ISO 4217 codes).
	"""

	def name(self):
		return 'Currency'

	def parse(self, value):
		if len(value) != 3:
			raise ValueError('FIX currency values must be 3 characters: %s', value)

		return value

class FIXExchange(FIXString):
	"""
	Represents the exchange type in FIX (ISO 10383 codes).
	"""

	def name(self):
		return 'Exchange'

	def parse(self, value):
		if len(value) > 4:
			raise ValueError('FIX exchange values must be <= 4 characters: %s', value)

		return value

class FIXLocalMktDate(FIXString):
	"""
	Represents the LocalMktDate type in FIX.
	"""

	def name(self):
		return 'LocalMktDate'

	def type(self):
		return datetime.date

	def parse(self, value):
		return parseLocalMarketDate(value)

class FIXMonthYear(FIXString):
	"""
	Represents the MonthYear type in FIX.
	"""

	def name(self):
		return 'MonthYear'

	def type(self):
		return datetime.date

	def parse(self, value):
		return parseMonthYear(value)

class FIXMultipleValueString(FIXString):
	"""
	Represents the MultipleValueString type in FIX.
	"""

	def name(self):
		return 'MultipleValueString'

	def type(self):
		return list

	def parse(self, value):
		return value.split(' ')

class FIXUTCDateOnly(FIXString):
	"""
	Represents the UTCDateOnly type in FIX.
	"""

	def name(self):
		return 'UTCDateOnly'

	def type(self):
		return datetime.date

	def parse(self, value):
		return parseUTCDateOnly(value)

class FIXUTCTimeOnly(FIXString):
	"""
	Represents the UTCTimeOnly type in FIX.
	"""

	def name(self):
		return 'UTCTimeOnly'

	def type(self):
		return datetime.time

	def parse(self, value):
		return parseUTCTimeOnly(value)

class FIXUTCTimestamp(FIXString):
	"""
	Represents the UTCTimeStamp type in FIX.
	"""

	def name(self):
		return 'UTCTimestamp'

	def type(self):
		return datetime.datetime

	def parse(self, value):
		return parseUTCTimestamp(value)

########## Types ##########

TYPE_CLASSES = [
	FIXChar,
	FIXBoolean,

	FIXData,

	FIXFloat,
	FIXAmt,
	FIXPercentage,
	FIXPrice,
	FIXPriceOffset,
	FIXQty,

	FIXInt,
	FIXDayOfMonth,
	FIXLength,
	FIXNumInGroup,
	FIXSeqNum,
	FIXTagNum,

	FIXString,
	FIXCountry,
	FIXCurrency,
	FIXExchange,
	FIXLocalMktDate,
	FIXMonthYear,
	FIXMultipleValueString,
	FIXUTCDateOnly,
	FIXUTCTimeOnly,
	FIXUTCTimestamp,
]

TYPE_NAME_TO_TYPE = {}
for typeClass in TYPE_CLASSES:
	fixType = typeClass()

	assert(fixType.name() not in TYPE_NAME_TO_TYPE)
	TYPE_NAME_TO_TYPE[fixType.name()] = fixType
