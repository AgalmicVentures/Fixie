
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

import datetime
import unittest

from Fixie import Types

class TypesTest(unittest.TestCase):

	def test_parseBool(self):
		#Upper case is accepted
		self.assertTrue(Types.parseBool('Y'))
		self.assertFalse(Types.parseBool('N'))

		#Lower case is not
		with self.assertRaises(ValueError):
			Types.parseBool('y')

		with self.assertRaises(ValueError):
			Types.parseBool('n')

	def test_parseMonthYear(self):
		#Common formats
		self.assertEqual(Types.parseMonthYear('201501'), datetime.date(2015, 1, 1))
		self.assertEqual(Types.parseMonthYear('20150103'), datetime.date(2015, 1, 3))
		self.assertEqual(Types.parseMonthYear('201503'), datetime.date(2015, 3, 1))

	def test_parseMonthYear_weekly(self):
		#Weekly values: March has 5 weeks
		self.assertEqual(Types.parseMonthYear('201503w0'), None)
		self.assertEqual(Types.parseMonthYear('201503w1'), datetime.date(2015, 3, 1))
		self.assertEqual(Types.parseMonthYear('201503w2'), datetime.date(2015, 3, 8))
		self.assertEqual(Types.parseMonthYear('201503w3'), datetime.date(2015, 3, 15))
		self.assertEqual(Types.parseMonthYear('201503w4'), datetime.date(2015, 3, 22))
		self.assertEqual(Types.parseMonthYear('201503w5'), datetime.date(2015, 3, 29))
		self.assertEqual(Types.parseMonthYear('201503w6'), None)

		#Feb has 4 weeks
		self.assertEqual(Types.parseMonthYear('201502w0'), None)
		self.assertEqual(Types.parseMonthYear('201502w1'), datetime.date(2015, 2, 1))
		self.assertEqual(Types.parseMonthYear('201502w2'), datetime.date(2015, 2, 8))
		self.assertEqual(Types.parseMonthYear('201502w3'), datetime.date(2015, 2, 15))
		self.assertEqual(Types.parseMonthYear('201502w4'), datetime.date(2015, 2, 22))
		self.assertEqual(Types.parseMonthYear('201502w5'), None)
		self.assertEqual(Types.parseMonthYear('201502w6'), None)

		#Except in leap years
		self.assertEqual(Types.parseMonthYear('201602w0'), None)
		self.assertEqual(Types.parseMonthYear('201602w1'), datetime.date(2016, 2, 1))
		self.assertEqual(Types.parseMonthYear('201602w2'), datetime.date(2016, 2, 8))
		self.assertEqual(Types.parseMonthYear('201602w3'), datetime.date(2016, 2, 15))
		self.assertEqual(Types.parseMonthYear('201602w4'), datetime.date(2016, 2, 22))
		self.assertEqual(Types.parseMonthYear('201602w5'), datetime.date(2016, 2, 29))
		self.assertEqual(Types.parseMonthYear('201602w6'), None)

	def test_parseMonthYear_error(self):
		#Must specify a month
		with self.assertRaises(ValueError):
			Types.parseMonthYear('2015')
