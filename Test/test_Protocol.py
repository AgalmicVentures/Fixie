
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

import unittest

from Fixie import Protocol

class TypesTest(unittest.TestCase):

	def test_message(self):
		rawMessage = "1128=9\0019=667\00135=d\00149=CME\00134=1263\00152=20140615160300389\00115=USD\00122=8\00148=24922\00155=ZS\001107=ZS:CF Q4U4X4F5\001200=201408\001202=0\001207=XCBT\001461=FMAXSX\001462=2\001555=4\001600=[N/A]\001602=94251\001603=8\001623=1\001624=1\001600=[N/A]\001602=801876\001603=8\001623=1\001624=2\001600=[N/A]\001602=873933\001603=8\001623=1\001624=2\001600=[N/A]\001602=786065\001603=8\001623=1\001624=1\001562=1\001731=1\001762=CF\001827=2\001864=2\001865=5\001866=20130114\0011145=223000000\001865=7\001866=20140814\0011145=170100000\001870=7\001871=24\001872=1\001871=24\001872=4\001871=24\001872=7\001871=24\001872=11\001871=24\001872=12\001871=25\001872=8\001871=27\001872=1\001947=USD\001969=0.25\001996=CTRCT\0011140=2500\0011141=1\0011022=GBX\001264=10\0011142=K\0011143=2.5\0011144=0\0011146=0\0011147=0\0011148=-284\0011149=516\0011150=116\0011151=ZS\0011180=111\0011300=72\0015796=20140613\0019787=1\0019850=0\00110=166\001"
		message = Protocol.FIXMessage(rawMessage)

		self.assertEqual(message.bodyLength(), 667)
		self.assertEqual(message.messageType(), 'd')
		self.assertEqual(message.senderCompID(), 'CME')
		self.assertEqual(message.currency(), 'USD')
		self.assertEqual(message.symbol(), 'ZS')
		self.assertEqual(message.checksum(), 166)

		message.updateMessage()
		#TODO: once repeating groups work self.assertEqual(message.message(), rawMessage)

	def test_emptyMessage(self):
		rawMessage = ''
		with self.assertRaises(ValueError):
			Protocol.FIXMessage(rawMessage)

	def test_missingEndSeperatorMessage(self):
		rawMessage = '1128=9\0019=667'
		with self.assertRaises(ValueError):
			Protocol.FIXMessage(rawMessage)

	def test_invalidTagMessage(self):
		rawMessage = 'asdf=9\0019=667\001'
		with self.assertRaises(ValueError):
			Protocol.FIXMessage(rawMessage)
