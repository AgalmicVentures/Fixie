
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
		self.assertEqual(Types.parseMonthYear('201501'), datetime.date(2015, 1, 1))
		self.assertEqual(Types.parseMonthYear('20150103'), datetime.date(2015, 1, 3))
		self.assertEqual(Types.parseMonthYear('201503'), datetime.date(2015, 3, 1))
