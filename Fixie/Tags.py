
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

import re

from . import Types

class FIXTag(object):
	"""
	Represents a FIX tag (used to automate parsing).
	"""

	def __init__(self, id, name, typeName=None, repeatingHeaderId=None, vendor=None, description=None):
		"""
		Initializes a new instance of FIXTag.
		"""
		assert(type(id) is int)
		assert(0 < id)
		assert(id < 100000)
		assert(type(name) is str)
		assert(re.match('^[A-Z0-9][a-zA-Z0-9_]*$', name) is not None)
		assert(typeName is None or type(typeName) is str)
		assert(repeatingHeaderId is None or type(repeatingHeaderId) is int)
		assert(vendor is None or type(vendor) is str)
		assert(description is None or type(description) is str)

		self._id = id
		self._name = name
		self._typeName = typeName
		self._type = None if typeName is None else Types.TYPE_NAME_TO_TYPE.get(typeName)
		assert(typeName is None or self._type is not None)

		self._repeatingHeaderId = repeatingHeaderId
		self._vendor = vendor
		self._description = description

	def __str__(self):
		"""
		Returns a string representing this tag.

		:return: str
		"""
		return '[%4d] %s' % (self._id, self._name)

	def __repr__(self):
		"""
		Returns a more complete string representing this tag.

		:return: str
		"""
		return '[%4d] %s rhn=%s v=%s d=%s' % (self._id, self._name, self._repeatingHeaderId, self._vendor, self._description)

	def id(self):
		"""
		Returns the ID of the tag.

		:return: int
		"""
		return self._id

	def name(self):
		"""
		Returns the name of the tag.

		:return: str
		"""
		return self._name

	def typeName(self):
		"""
		Returns the name of the type of the tag.

		:return: str
		"""
		return self._typeName

	def type(self):
		"""
		Returns the `FIXType` of the tag (e.g. for parsing).

		:return: FIXType
		"""
		return self._type

	def repeatingHeaderId(self):
		"""
		Returns the ID of the repeating group header if this is a part of one.

		:return: int
		"""
		return self._repeatingHeaderId

	def vendor(self):
		"""
		Returns the vendor of the tag.

		:return: str
		"""
		return self._vendor

	def description(self):
		"""
		Returns a description of the tag.

		:return: str
		"""
		return self._description

TAGS = [
##### BEGIN GENERATED CODE
	FIXTag(   1, 'Account', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(   2, 'AdvId', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(   3, 'AdvRefID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(   4, 'AdvSide', typeName='char', repeatingHeaderId=None, vendor=None, description="Broker's side of advertised trade (B=Buy S=Sell X=Cross T=Trade)"),
	FIXTag(   5, 'AdvTransType', typeName='String', repeatingHeaderId=None, vendor=None, description='Avertisement message transaction type (N=New C=Cancel R=Replace)'),
	FIXTag(   6, 'AvgPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag(   7, 'BeginSeqNo', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(   8, 'BeginString', typeName='String', repeatingHeaderId=None, vendor=None, description='First in message'),
	FIXTag(   9, 'BodyLength', typeName='int', repeatingHeaderId=None, vendor=None, description='How is this not a Length?'),
	FIXTag(  10, 'CheckSum', typeName='int', repeatingHeaderId=None, vendor=None, description='Last in message'),
	FIXTag(  11, 'ClOrdID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  12, 'Commission', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag(  13, 'CommType', typeName='char', repeatingHeaderId=None, vendor=None, description='1=per share 2=percentage 3=absolute'),
	FIXTag(  14, 'CumQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag(  15, 'Currency', typeName='Currency', repeatingHeaderId=None, vendor=None, description='Identifies currency used for price.'),
	FIXTag(  16, 'EndSeqNo', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  17, 'ExecID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  18, 'ExecInst', typeName='MultipleValueString', repeatingHeaderId=None, vendor=None),
	FIXTag(  19, 'ExecRefID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  20, 'ExecTransType', typeName='char', repeatingHeaderId=None, vendor=None, description='Transaction type (0=New 1=Cancel 2=Correct 3=Status)'),
	FIXTag(  21, 'HandlInst', typeName='char', repeatingHeaderId=None, vendor=None, description='Floor broker instructions (1=Automated, private 2=Automated, public, 3=Manual)'),
	FIXTag(  22, 'IDSource', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  23, 'IOIid', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  24, 'IOIOthSvc', typeName='char', repeatingHeaderId=None, vendor=None, description='No longer used'),
	FIXTag(  25, 'IOIQltyInd', typeName='char', repeatingHeaderId=None, vendor=None, description='Relative quality of indication (L=Low M=Medium H=High)'),
	FIXTag(  26, 'IOIRefID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  27, 'IOIShares', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  28, 'IOITransType', typeName='char', repeatingHeaderId=None, vendor=None, description='IOI transaction type (N=New C=Cancel R=Replace)'),
	FIXTag(  29, 'LastCapacity', typeName='char', repeatingHeaderId=None, vendor=None, description='Broker capacity in order execution (1=Agent 2=Cross as agent 3=Cross as principal 4=Principal)'),
	FIXTag(  30, 'LastMkt', typeName='Exchange', repeatingHeaderId=None, vendor=None),
	FIXTag(  31, 'LastPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag(  32, 'LastShares', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag(  33, 'LinesOfText', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  34, 'MsgSeqNum', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  35, 'MsgType', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  36, 'NewSeqNo', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  37, 'OrderID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  38, 'OrderQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag(  39, 'OrdStatus', typeName='char', repeatingHeaderId=None, vendor=None, description='Order status (0=New 1=Partially filled 2=Filled 3=Done for day 4=Canceled 5=Replaced 6=Pending cancel ...)'),
	FIXTag(  40, 'OrdType', typeName='char', repeatingHeaderId=None, vendor=None, description='Order type (1=Market 2=Limit 3=Stop 4=Stop limit 5=Market on close ...)'),
	FIXTag(  41, 'OrigClOrdID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  42, 'OrigTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag(  43, 'PossDupFlag', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag(  44, 'Price', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag(  45, 'RefSeqNum', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  46, 'RelatdSym', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  47, 'Rule80A', typeName='char', repeatingHeaderId=None, vendor=None, description='Also known as OrderCapacity'),
	FIXTag(  48, 'SecurityID', typeName='String', repeatingHeaderId=None, vendor=None, description='Unique instrument ID as qualified by the exchange per tag 22-SecurityIDSource.'),
	FIXTag(  49, 'SenderCompID', typeName='String', repeatingHeaderId=None, vendor=None, description='Assigned value used to identify firm sending message.'),
	FIXTag(  50, 'SenderSubID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  51, 'SendingDate', typeName='LocalMktDate', repeatingHeaderId=None, vendor=None, description='No longer used'),
	FIXTag(  52, 'SendingTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag(  53, 'Shares', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag(  54, 'Side', typeName='char', repeatingHeaderId=None, vendor=None, description='1=Buy 2=Sell 3=Buy minus 4=Sell plus 5=Sell short 6=Sell short exempt 7=Undisclosed 8=Cross 9=Cross short'),
	FIXTag(  55, 'Symbol', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  56, 'TargetCompID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  57, 'TargetSubID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  58, 'Text', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  59, 'TimeInForce', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag(  60, 'TransactTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag(  61, 'Urgency', typeName='char', repeatingHeaderId=None, vendor=None, description='0=Normal 1=Flash 2=Background'),
	FIXTag(  62, 'ValidUntilTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag(  63, 'SettlmntTyp', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag(  64, 'FutSettDate', typeName='LocalMktDate', repeatingHeaderId=None, vendor=None),
	FIXTag(  65, 'SymbolSfx', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  66, 'ListID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  67, 'ListSeqNo', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  68, 'TotNoOrders', typeName='int', repeatingHeaderId=None, vendor=None, description='Formerly named ListNoOrds'),
	FIXTag(  69, 'ListExecInst', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  70, 'AllocID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  71, 'AllocTransType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag(  72, 'RefAllocID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  73, 'NoOrders', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  74, 'AvgPrxPrecision', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  75, 'TradeDate', typeName='LocalMktDate', repeatingHeaderId=None, vendor=None),
	FIXTag(  76, 'ExecBroker', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  77, 'OpenClose', typeName='char', repeatingHeaderId=None, vendor=None, description='O=open C=close'),
	FIXTag(  78, 'NoAllocs', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  79, 'AllocAccount', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  80, 'AllocShares', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag(  81, 'ProcessCode', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag(  82, 'NoRpts', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  83, 'RptSeq', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  84, 'CxlQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag(  85, 'NoDlvyInst', typeName='int', repeatingHeaderId=None, vendor=None, description='No longer used'),
	FIXTag(  86, 'DlvyInst', typeName='String', repeatingHeaderId=None, vendor=None, description='No longer used'),
	FIXTag(  87, 'AllocStatus', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  88, 'AllocRejCode', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  89, 'Signature', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag(  90, 'SecureDataLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag(  91, 'SecureData', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag(  92, 'BrokerOfCredit', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag(  93, 'SignatureLength', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag(  94, 'EmailType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag(  95, 'RawDataLength', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag(  96, 'RawData', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag(  97, 'PossResend', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag(  98, 'EncryptMethod', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag(  99, 'StopPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 100, 'ExDestination', typeName='Exchange', repeatingHeaderId=None, vendor=None),
	FIXTag( 102, 'CxlRejReason', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 103, 'OrdRejReason', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 104, 'IOIQualifier', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 105, 'WaveNo', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 106, 'Issuer', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 107, 'SecurityDesc', typeName='String', repeatingHeaderId=None, vendor=None, description='Instrument Name.'),
	FIXTag( 108, 'HeartBtInt', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 109, 'ClientID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 110, 'MinQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 111, 'MaxFloor', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 112, 'TestReqID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 113, 'ReportToExch', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 114, 'LocateReqd', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 115, 'OnBehalfOfCompID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 116, 'OnBehalfOfSubID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 117, 'QuoteID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 118, 'NetMoney', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 119, 'SettlCurrAmt', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 120, 'SettlCurrency', typeName='Currency', repeatingHeaderId=None, vendor=None, description='Identifies currency used for settlement price.'),
	FIXTag( 121, 'ForexReq', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 122, 'OrigSendingTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 123, 'GapFillFlag', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 124, 'NoExecs', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 125, 'CxlType', typeName='char', repeatingHeaderId=None, vendor=None, description='No longer used'),
	FIXTag( 126, 'ExpireTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 127, 'DKReason', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 128, 'DeliverToCompID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 129, 'DeliverToSubID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 130, 'IOINaturalFlag', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 131, 'QuoteReqID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 132, 'BidPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 133, 'OfferPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 134, 'BidSize', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 135, 'OfferSize', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 136, 'NoMiscFees', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 137, 'MiscFeeAmt', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 138, 'MiscFeeCurr', typeName='Currency', repeatingHeaderId=None, vendor=None),
	FIXTag( 139, 'MiscFeeType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 140, 'PrevClosePx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 141, 'ResetSeqNumFlag', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 142, 'SenderLocationID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 143, 'TargetLocationID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 144, 'OnBehalfOfLocationID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 145, 'DeliverToLocationID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 146, 'NoRelatedSym', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 147, 'Subject', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 148, 'Headline', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 149, 'URLLink', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 150, 'ExecType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 151, 'LeavesQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 152, 'CashOrderQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 153, 'AllocAvgPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 154, 'AllocNetMoney', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 155, 'SettlCurrFxRate', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 156, 'SettlCurrFxRateCalc', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 157, 'NumDaysInterest', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 158, 'AccruedInterestRate', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 159, 'AccruedInterestAmt', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 160, 'SettlInstMode', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 161, 'AllocText', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 162, 'SettlInstID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 163, 'SettlInstTransType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 164, 'EmailThreadID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 165, 'SettlInstSource', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 166, 'SettlLocation', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 167, 'SecurityType', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 168, 'EffectiveTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 169, 'StandInstDbType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 170, 'StandInstDbName', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 171, 'StandInstDbID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 172, 'SettlDeliveryType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 173, 'SettlDepositoryCode', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 174, 'SettlBrkrCode', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 175, 'SettlInstCode', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 176, 'SecuritySettlAgentName', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 177, 'SecuritySettlAgentCode', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 178, 'SecuritySettlAgentAcctNum', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 179, 'SecuritySettlAgentAcctName', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 180, 'SecuritySettlAgentContactName', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 181, 'SecuritySettlAgentContactPhone', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 182, 'CashSettlAgentName', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 183, 'CashSettlAgentCode', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 184, 'CashSettlAgentAcctNum', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 185, 'CashSettlAgentAcctName', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 186, 'CashSettlAgentContactName', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 187, 'CashSettlAgentContactPhone', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 188, 'BidSpotRate', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 189, 'BidForwardPoints', typeName='PriceOffset', repeatingHeaderId=None, vendor=None),
	FIXTag( 190, 'OfferSpotRate', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 191, 'OfferForwardPoints', typeName='PriceOffset', repeatingHeaderId=None, vendor=None),
	FIXTag( 192, 'OrderQty2', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 193, 'FutSettDate2', typeName='LocalMktDate', repeatingHeaderId=None, vendor=None),
	FIXTag( 194, 'LastSpotRate', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 195, 'LastForwardPoints', typeName='PriceOffset', repeatingHeaderId=None, vendor=None),
	FIXTag( 196, 'AllocLinkID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 197, 'AllocLinkType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 198, 'SecondaryOrderID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 199, 'NoIOIQualifiers', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 200, 'MaturityMonthYear', typeName='MonthYear', repeatingHeaderId=None, vendor=None, description='Format YYYYMM (i.e. 200912)'),
	FIXTag( 201, 'PutOrCall', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 202, 'StrikePrice', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 203, 'CoveredOrUncovered', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 204, 'CustomerOrFirm', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 205, 'MaturityDay', typeName='DayOfMonth', repeatingHeaderId=None, vendor=None),
	FIXTag( 206, 'OptAttribute', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 207, 'SecurityExchange', typeName='Exchange', repeatingHeaderId=None, vendor=None),
	FIXTag( 208, 'NotifyBrokerOfCredit', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 209, 'AllocHandlInst', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 210, 'MaxShow', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 211, 'PegDifference', typeName='PriceOffset', repeatingHeaderId=None, vendor=None),
	FIXTag( 212, 'XmlDataLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 213, 'XmlData', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 214, 'SettlInstRefID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 215, 'NoRoutingIDs', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 216, 'RoutingType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 217, 'RoutingID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 218, 'SpreadToBenchmark', typeName='PriceOffset', repeatingHeaderId=None, vendor=None),
	FIXTag( 219, 'Benchmark', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 223, 'CouponRate', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 231, 'ContractMultiplier', typeName='float', repeatingHeaderId=None, vendor=None, description='Number of deliverable units per instrument, e.g., peak days in maturity month or number of calendar days in maturity month.'),
	FIXTag( 262, 'MDReqID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 263, 'SubscriptionRequestType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 264, 'MarketDepth', typeName='int', repeatingHeaderId=1141, vendor=None, description='Identifies the depth of book.'),
	FIXTag( 265, 'MDUpdateType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 266, 'AggregatedBook', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 267, 'NoMDEntryTypes', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 268, 'NoMDEntries', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 269, 'MDEntryType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 270, 'MDEntryPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 271, 'MDEntrySize', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 272, 'MDEntryDate', typeName='UTCDateOnly', repeatingHeaderId=None, vendor=None),
	FIXTag( 273, 'MDEntryTime', typeName='UTCTimeOnly', repeatingHeaderId=None, vendor=None),
	FIXTag( 274, 'TickDirection', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 275, 'MDMkt', typeName='Exchange', repeatingHeaderId=None, vendor=None),
	FIXTag( 276, 'QuoteCondition', typeName='MultipleValueString', repeatingHeaderId=None, vendor=None),
	FIXTag( 277, 'TradeCondition', typeName='MultipleValueString', repeatingHeaderId=None, vendor=None),
	FIXTag( 278, 'MDEntryID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 279, 'MDUpdateAction', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 280, 'MDEntryRefID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 281, 'MDReqRejReason', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 282, 'MDEntryOriginator', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 283, 'LocationID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 284, 'DeskID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 285, 'DeleteReason', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 286, 'OpenCloseSettleFlag', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 287, 'SellerDays', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 288, 'MDEntryBuyer', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 289, 'MDEntrySeller', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 290, 'MDEntryPositionNo', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 291, 'FinancialStatus', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 292, 'CorporateAction', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 293, 'DefBidSize', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 294, 'DefOfferSize', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 295, 'NoQuoteEntries', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 296, 'NoQuoteSets', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 297, 'QuoteAckStatus', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 298, 'QuoteCancelType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 299, 'QuoteEntryID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 300, 'QuoteRejectReason', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 301, 'QuoteResponseLevel', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 302, 'QuoteSetID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 303, 'QuoteRequestType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 304, 'TotQuoteEntries', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 305, 'UnderlyingIDSource', typeName='String', repeatingHeaderId=711, vendor=None, description="This value is always '8' for CME."),
	FIXTag( 306, 'UnderlyingIssuer', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 307, 'UnderlyingSecurityDesc', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 308, 'UnderlyingSecurityExchange', typeName='Exchange', repeatingHeaderId=None, vendor=None),
	FIXTag( 309, 'UnderlyingSecurityID', typeName='String', repeatingHeaderId=711, vendor=None, description='Unique instrument ID as qualified by the exchange per tag 305-UnderlyingSecurityIDSource.'),
	FIXTag( 310, 'UnderlyingSecurityType', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 311, 'UnderlyingSymbol', typeName='String', repeatingHeaderId=711, vendor=None, description="Underlying security's Symbol."),
	FIXTag( 312, 'UnderlyingSymbolSfx', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 313, 'UnderlyingMaturityMonthYear', typeName='MonthYear', repeatingHeaderId=None, vendor=None),
	FIXTag( 314, 'UnderlyingMaturityDay', typeName='DayOfMonth', repeatingHeaderId=None, vendor=None),
	FIXTag( 315, 'UnderlyingPutOrCall', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 316, 'UnderlyingStrikePrice', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 317, 'UnderlyingOptAttribute', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 318, 'UnderlyingCurrency', typeName='Currency', repeatingHeaderId=None, vendor=None),
	FIXTag( 319, 'RatioQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 320, 'SecurityReqID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 321, 'SecurityRequestType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 322, 'SecurityResponseID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 323, 'SecurityResponseType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 324, 'SecurityStatusReqID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 325, 'UnsolicitedIndicator', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 326, 'SecurityTradingStatus', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 327, 'HaltReason', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 328, 'InViewOfCommon', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 329, 'DueToRelated', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 330, 'BuyVolume', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 331, 'SellVolume', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 332, 'HighPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 333, 'LowPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 334, 'Adjustment', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 335, 'TradSesReqID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 336, 'TradingSessionID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 337, 'ContraTrader', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 338, 'TradSesMethod', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 339, 'TradSesMode', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 340, 'TradSesStatus', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 341, 'TradSesStartTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 342, 'TradSesOpenTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 343, 'TradSesPreCloseTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 344, 'TradSesCloseTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 345, 'TradSesEndTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 346, 'NumberOfOrders', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 347, 'MessageEncoding', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 348, 'EncodedIssuerLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 349, 'EncodedIssuer', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 350, 'EncodedSecurityDescLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 351, 'EncodedSecurityDesc', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 352, 'EncodedListExecInstLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 353, 'EncodedListExecInst', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 354, 'EncodedTextLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 355, 'EncodedText', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 356, 'EncodedSubjectLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 357, 'EncodedSubject', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 358, 'EncodedHeadlineLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 359, 'EncodedHeadline', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 360, 'EncodedAllocTextLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 361, 'EncodedAllocText', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 362, 'EncodedUnderlyingIssuerLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 363, 'EncodedUnderlyingIssuer', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 364, 'EncodedUnderlyingSecurityDescLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 365, 'EncodedUnderlyingSecurityDesc', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 366, 'AllocPrice', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 367, 'QuoteSetValidUntilTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 368, 'QuoteEntryRejectReason', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 369, 'LastMsgSeqNumProcessed', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 370, 'OnBehalfOfSendingTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 371, 'RefTagID', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 372, 'RefMsgType', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 373, 'SessionRejectReason', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 374, 'BidRequestTransType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 375, 'ContraBroker', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 376, 'ComplianceID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 377, 'SolicitedFlag', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 378, 'ExecRestatementReason', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 379, 'BusinessRejectRefID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 380, 'BusinessRejectReason', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 381, 'GrossTradeAmt', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 382, 'NoContraBrokers', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 383, 'MaxMessageSize', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 384, 'NoMsgTypes', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 385, 'MsgDirection', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 386, 'NoTradingSessions', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 387, 'TotalVolumeTraded', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 388, 'DiscretionInst', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 389, 'DiscretionOffset', typeName='PriceOffset', repeatingHeaderId=None, vendor=None),
	FIXTag( 390, 'BidID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 391, 'ClientBidID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 392, 'ListName', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 393, 'TotalNumSecurities', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 394, 'BidType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 395, 'NumTickets', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 396, 'SideValue1', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 397, 'SideValue2', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 398, 'NoBidDescriptors', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 399, 'BidDescriptorType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 400, 'BidDescriptor', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 401, 'SideValueInd', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 402, 'LiquidityPctLow', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 403, 'LiquidityPctHigh', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 404, 'LiquidityValue', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 405, 'EFPTrackingError', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 406, 'FairValue', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 407, 'OutsideIndexPct', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 408, 'ValueOfFutures', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 409, 'LiquidityIndType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 410, 'WtAverageLiquidity', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 411, 'ExchangeForPhysical', typeName='Boolean', repeatingHeaderId=None, vendor=None),
	FIXTag( 412, 'OutMainCntryUIndex', typeName='Amt', repeatingHeaderId=None, vendor=None),
	FIXTag( 413, 'CrossPercent', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 414, 'ProgRptReqs', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 415, 'ProgPeriodInterval', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 416, 'IncTaxInd', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 417, 'NumBidders', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 418, 'TradeType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 419, 'BasisPxType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 420, 'NoBidComponents', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 421, 'Country', typeName='Country', repeatingHeaderId=None, vendor=None),
	FIXTag( 422, 'TotNoStrikes', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 423, 'PriceType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 424, 'DayOrderQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 425, 'DayCumQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 426, 'DayAvgPx', typeName='Price', repeatingHeaderId=None, vendor=None),
	FIXTag( 427, 'GTBookingInst', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 428, 'NoStrikes', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 429, 'ListStatusType', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 430, 'NetGrossInd', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 431, 'ListOrderStatus', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 432, 'ExpireDate', typeName='LocalMktDate', repeatingHeaderId=None, vendor=None),
	FIXTag( 433, 'ListExecInstType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 434, 'CxlRejResponseTo', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 435, 'UnderlyingCouponRate', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 436, 'UnderlyingContractMultiplier', typeName='float', repeatingHeaderId=None, vendor=None),
	FIXTag( 437, 'ContraTradeQty', typeName='Qty', repeatingHeaderId=None, vendor=None),
	FIXTag( 438, 'ContraTradeTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 439, 'ClearingFirm', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 440, 'ClearingAccount', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 441, 'LiquidityNumSecurities', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 442, 'MultiLegReportingType', typeName='char', repeatingHeaderId=None, vendor=None),
	FIXTag( 443, 'StrikeTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor=None),
	FIXTag( 444, 'ListStatusText', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 445, 'EncodedListStatusTextLen', typeName='Length', repeatingHeaderId=None, vendor=None),
	FIXTag( 446, 'EncodedListStatusText', typeName='data', repeatingHeaderId=None, vendor=None),
	FIXTag( 454, 'NoSecurityAltID', typeName='NumInGroup', repeatingHeaderId=None, vendor=None),
	FIXTag( 455, 'SecurityAltID', typeName='String', repeatingHeaderId=454, vendor=None),
	FIXTag( 456, 'SecurityAltIDSource', typeName='String', repeatingHeaderId=454, vendor=None),
	FIXTag( 460, 'Product', typeName='int', repeatingHeaderId=None, vendor=None),
	FIXTag( 461, 'CFICode', typeName='String', repeatingHeaderId=None, vendor=None, description='Indicates the type of security using ISO 10962 standard, Classification of Financial Instruments (CFI code) values. See: http://www.cmegroup.com/confluence/display/EPICSANDBOX/Market+Data+-+CFICode+Table+of+Values'),
	FIXTag( 462, 'UnderlyingProduct', typeName='int', repeatingHeaderId=None, vendor='CME', description='Product complex (2=Commodity/Agriculture, 4=Currency, 5=Equity, 12=Other, 14=Interest Rate, 15=FX Cash, 16=Energy, 17=Metals)'),
	FIXTag( 541, 'MaturityDate', typeName='LocalMktDate', repeatingHeaderId=None, vendor=None),
	FIXTag( 555, 'NoLegs', typeName='NumInGroup', repeatingHeaderId=None, vendor='CME', description='Number of legs.'),
	FIXTag( 556, 'LegCurrency', typeName='Currency', repeatingHeaderId=555, vendor='CME', description='Currency for this leg.'),
	FIXTag( 562, 'MinTradeVol', typeName='Qty', repeatingHeaderId=None, vendor='CME', description='The minimum trading volume for a security.'),
	FIXTag( 566, 'LegPrice', typeName='Price', repeatingHeaderId=555, vendor='CME', description='Price for the futures leg of a covered.'),
	FIXTag( 600, 'LegSymbol', typeName='String', repeatingHeaderId=555, vendor='CME', description='Only sent for options strategies and futures spreads. '),
	FIXTag( 602, 'LegSecurityID', typeName='String', repeatingHeaderId=555, vendor='CME', description='Unique instrument ID for the leg.'),
	FIXTag( 603, 'LegSecurityIDSource', typeName='String', repeatingHeaderId=555, vendor='CME', description="Identifies source of tag 602-LegSecurityID value. This value is always '8' for CME."),
	FIXTag( 604, 'NoLegSecurityAltID', typeName='NumInGroup', repeatingHeaderId=None, vendor=None),
	FIXTag( 605, 'LegSecurityAltID', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 606, 'LegSecurityAltIDSource', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 608, 'LegCFICode', typeName='String', repeatingHeaderId=555, vendor='CME', description='CFI code for this leg.'),
	FIXTag( 609, 'LegSecurityType', typeName='String', repeatingHeaderId=None, vendor=None),
	FIXTag( 610, 'LegMaturityMonthYear', typeName='MonthYear', repeatingHeaderId=555, vendor='CME', description="Leg's MaturityMonthYear."),
	FIXTag( 611, 'LegMaturityDate', typeName='LocalMktDate', repeatingHeaderId=None, vendor=None),
	FIXTag( 612, 'LegStrikePrice', typeName='Price', repeatingHeaderId=555, vendor='CME', description='Strike price of the leg.'),
	FIXTag( 616, 'LegSecurityExchange', typeName='Exchange', repeatingHeaderId=555, vendor='CME', description='Security exchange of the leg.'),
	FIXTag( 620, 'LegSecurityDesc', typeName='String', repeatingHeaderId=555, vendor='CME', description='Leg security description (e.g., ESM0 C1130)'),
	FIXTag( 623, 'LegRatioQty', typeName='Qty', repeatingHeaderId=555, vendor='CME', description='The ratio of quantity for this individual leg relative to the entire multi-leg instrument.'),
	FIXTag( 624, 'LegSide', typeName='char', repeatingHeaderId=555, vendor='CME', description='1=Buy, 2=Sell.'),
	FIXTag( 711, 'NoUnderlyings', typeName='NumInGroup', repeatingHeaderId=None, vendor='CME', description='Number of underlying instruments.'),
	FIXTag( 731, 'SettlPriceType', typeName='String', repeatingHeaderId=None, vendor='CME', description='Indicates whether settlement price is preliminary or final (1=Final, 2=Theoretical, 100=Actual preliminary for instruments not subject to rounding, 101=Actual preliminary for instruments subject to rounding).'),
	FIXTag( 762, 'SecuritySubType', typeName='String', repeatingHeaderId=None, vendor='CME', description='Indicates Strategy type.'),
	FIXTag( 764, 'LegSecuritySubType', typeName='String', repeatingHeaderId=555, vendor='CME', description='If leg repeating group is a spread, the strategy type for the spread.'),
	FIXTag( 779, 'LastUpdateTime', typeName='UTCTimestamp', repeatingHeaderId=None, vendor='CME', description='Timestamp of when the instrument was deleted.'),
	FIXTag( 827, 'ExpirationCycle', typeName='int', repeatingHeaderId=None, vendor='CME', description="Indicates if the instrument expires at the trading session close, or at a specified last eligible trade date. If '0', the instrument is eligible for Day orders only. If '2', the instrument is eligible for GTC/GTD orders (outrights only)."),
	FIXTag( 864, 'NoEvents', typeName='NumInGroup', repeatingHeaderId=None, vendor='CME', description='Number of repeating EventType entries.'),
	FIXTag( 865, 'EventType', typeName='int', repeatingHeaderId=864, vendor='CME', description='Code to represent the type of event (5=Activation, 7=Last eligible trade date)'),
	FIXTag( 866, 'EventDate', typeName='LocalMktDate', repeatingHeaderId=864, vendor='CME', description='Date of event.'),
	FIXTag( 870, 'NbInstAttrib', typeName='NumInGroup', repeatingHeaderId=None, vendor='CME', description='Number of repeating group InstrAttribType entries.'),
	FIXTag( 871, 'InstAttribType', typeName='int', repeatingHeaderId=870, vendor='CME', description='Tag 871-InstAttribType and tag 872-InstAttribValue function together where tag 871 indicates the type of value that the following tag 872 will contain.'),
	FIXTag( 872, 'InstAttribValue', typeName='String', repeatingHeaderId=870, vendor='CME', description='Tag 871-InstAttribType and tag 872-InstAttribValue function together where tag 871 indicates the type of value that the following tag 872 will contain.'),
	FIXTag( 911, 'TotNumReports', typeName='int', repeatingHeaderId=None, vendor='CME', description='Total number of reports returned in response to a request.'),
	FIXTag( 942, 'LegStrikeCurrency', typeName='Currency', repeatingHeaderId=555, vendor='CME', description='Currency of the strike price of the leg.'),
	FIXTag( 947, 'StrikeCurrency', typeName='Currency', repeatingHeaderId=None, vendor='CME', description='Currency in which the strike price is denominated.'),
	FIXTag( 969, 'MinPriceIncrement', typeName='float', repeatingHeaderId=None, vendor='CME', description='Minimum constant tick for the instrument, sent only if instrument is non-VTT (Variable Tick table) eligible.'),
	FIXTag( 980, 'SecurityUpdateAction', typeName='char', repeatingHeaderId=None, vendor='CME', description='A=Add, M=Modify, D=Delete.'),
	FIXTag( 996, 'UnitOfMeasure', typeName='String', repeatingHeaderId=None, vendor='CME', description="Unit of measure for the products' original contract size."),
	FIXTag(1017, 'LegOptionDelta', typeName='float', repeatingHeaderId=555, vendor='CME', description='Delta used to calculate the quantity of futures used to cover the option or option strategy.'),
	FIXTag(1022, 'MDFeedType', typeName='String', repeatingHeaderId=1141, vendor='CME', description='Describes a class of service for a given data feed.'),
	FIXTag(1028, 'ManualOrderIndicator', typeName='Boolean', repeatingHeaderId=None, vendor='CME', description='Flag to indicate a manual order'),
	FIXTag(1091, 'PreTradeAnonymity', typeName='Boolean', repeatingHeaderId=None, vendor='CME', description='Tag to indicate whether tag 37 will be sent out in the Trade Summary message (MDP 3.0)'),
	FIXTag(1093, 'LotType', typeName='char', repeatingHeaderId=1234, vendor='CME', description='The quantity type used for the leg of the spread. This tag is required to interpret the value in tag 1231-MinLotSize.'),
	FIXTag(1128, 'ApplVerID', typeName='String', repeatingHeaderId=None, vendor='CME', description='Specifies the service pack release being applied at message level.'),
	FIXTag(1140, 'MaxTradeVol', typeName='Qty', repeatingHeaderId=None, vendor='CME', description='The maximum trading volume for a security.'),
	FIXTag(1141, 'NoMdFeedTypes', typeName='NumInGroup', repeatingHeaderId=None, vendor='CME', description='Number of repeating FeedType repeating group entries.'),
	FIXTag(1142, 'MatchingAlgorithm', typeName='char', repeatingHeaderId=None, vendor='CME', description='Matching algorithm (F=FIFO, K=Configurable, C=Pro-Rata, A=Allocation, T=FIFO with LLM, O=Threshold Pro-Rata, S=FIFO with TOP and LLM, Q=Threshold Pro-Rata with LLM, Y=Eurodollar options)'),
	FIXTag(1143, 'MaxPriceVariation', typeName='float', repeatingHeaderId=None, vendor='CME', description='Differential value for price banding.'),
	FIXTag(1144, 'ImpliedMarketIndicator', typeName='int', repeatingHeaderId=None, vendor='CME', description='Informs the market that an instrument is eligible for implied trading (Implied In & Out; 0=Non-implied, 3=Implied). If this tag is not present, instrument is non-implied.'),
	FIXTag(1145, 'EventTime', typeName='UTCTimestamp', repeatingHeaderId=864, vendor='CME', description='Time of event.'),
	FIXTag(1146, 'MinPriceIncrementAmount', typeName='Amt', repeatingHeaderId=None, vendor='CME', description='Under development.'),
	FIXTag(1147, 'UnitOfMeasureQty', typeName='Qty', repeatingHeaderId=None, vendor='CME', description='This field contains the contract size for each instrument (in combination with tag 996).'),
	FIXTag(1148, 'LowLimitPrice', typeName='Price', repeatingHeaderId=None, vendor='CME', description='Lower price threshold for the instrument. Orders submitted with prices below the lower limit will be rejected.'),
	FIXTag(1149, 'HighLimitPrice', typeName='Price', repeatingHeaderId=None, vendor='CME', description='Upper price threshold for the instrument. Orders submitted with prices above the upper limit will be rejected.'),
	FIXTag(1150, 'TradingReferencePrice', typeName='Price', repeatingHeaderId=None, vendor='CME', description='The most recent settlement price.'),
	FIXTag(1151, 'SecurityGroup', typeName='String', repeatingHeaderId=None, vendor='CME', description='Product code.'),
	FIXTag(1180, 'AppIID', typeName='String', repeatingHeaderId=None, vendor='CME', description='The channel ID as defined in the XML Configuration file.'),
	FIXTag(1234, 'NoLotTypeRules', typeName='NumInGroup', repeatingHeaderId=None, vendor='CME', description='Number of quantity types in the upcoming repeating group.'),
	FIXTag(1300, 'MarketSegmentID', typeName='String', repeatingHeaderId=None, vendor='CME', description='Identifies the market segment.'),
	FIXTag(1435, 'ContractMultiplierUnit', typeName='float', repeatingHeaderId=None, vendor='CME', description='Indicates the type of multiplier being applied to the product. Used in combination with tag 231. 1=Hour, 2=Day'),
	FIXTag(1439, 'FlowScheduleType', typeName='int', repeatingHeaderId=None, vendor='CME', description='The schedule according to which the electricity is delivered in a physical contract, or priced in a financial contract. '),
	FIXTag(5770, 'PriceRatio', typeName='float', repeatingHeaderId=None, vendor='CME', description='Used for price calculation in spread and leg pricing.'),
	FIXTag(5791, 'ClearedVolume', typeName='Qty', repeatingHeaderId=None, vendor='CME', description='Indicates the total cleared volume of instruments traded during the prior trading session.'),
	FIXTag(5792, 'OpenInterestQty', typeName='Qty', repeatingHeaderId=None, vendor='CME', description='Indicates the total open interest for the market at the close of the prior trading session.'),
	FIXTag(5795, 'LegSecurityGroup', typeName='String', repeatingHeaderId=555, vendor='CME', description='Product code for this leg.'),
	FIXTag(5796, 'TradingReferenceDate', typeName='LocalMktDate', repeatingHeaderId=None, vendor='CME', description='Indicates the date the last update to the settlement price.'),
	FIXTag(5818, 'DecayQty', typeName='Qty', repeatingHeaderId=None, vendor='CME', description='Indicates the quantity that a contract will decay daily by once the decay start date is reached.'),
	FIXTag(5819, 'DecayStartDate', typeName='LocalMktDate', repeatingHeaderId=None, vendor='CME', description='Indicates the date at which a decay contract will begin to decay.'),
	FIXTag(5849, 'OriginalContractSize', typeName='Qty', repeatingHeaderId=None, vendor='CME', description='Fixed contract value assigned to a product.'),
	FIXTag(7928, 'SelfMatchPreventionID', typeName='String', repeatingHeaderId=None, vendor='CME', description='ID used for self-match prevention'),
	FIXTag(8000, 'SelfMatchPreventionInstruction', typeName='char', repeatingHeaderId=None, vendor='CME', description='O=Cancel resting N=Cancel aggressing'),
	FIXTag(9702, 'CtiCode', typeName='char', repeatingHeaderId=None, vendor='CME', description='CTI code of the customer (1-4)'),
	FIXTag(9779, 'UserDefinedInstrument', typeName='Boolean', repeatingHeaderId=None, vendor='CME', description='Y=User defined, N=Not.'),
	FIXTag(9787, 'DisplayFactor', typeName='float', repeatingHeaderId=None, vendor='CME', description='Contains the multiplier to convert the CME Globex display price to the conventional price.'),
	FIXTag(9850, 'MinCabPrice', typeName='Price', repeatingHeaderId=None, vendor='CME', description='Defines cabinet price for outright options products.'),
	FIXTag(9853, 'PricingModel', typeName='char', repeatingHeaderId=None, vendor='CME', description='Identifies options pricing model (F=Fischer-Black, W=Whaley).'),
	FIXTag(10456, 'UnderlyingSecurityAltID', typeName='String', repeatingHeaderId=None, vendor='TT', description='Leg’s alternative security ID'),
	FIXTag(16460, 'DeliveryUnit', typeName='int', repeatingHeaderId=None, vendor='TT', description='Delivery unit for this contract (e.g. 2500 MBtus, 50 megawatts, etc.)'),
	FIXTag(16463, 'Blocks', typeName='int', repeatingHeaderId=None, vendor='TT', description='Total number of deliverable units per contract'),
	FIXTag(16464, 'TradesInFlow', typeName='Boolean', repeatingHeaderId=None, vendor='TT', description='Whether the contract is continuously delivered.'),
	FIXTag(16456, 'NumTickTblEntries', typeName='NumInGroup', repeatingHeaderId=None, vendor='TT', description='Number of ticks in the tick table.'),
	FIXTag(16552, 'ExchTickSize', typeName='float', repeatingHeaderId=None, vendor='TT', description='Size of one base tick for this security'),
	FIXTag(16554, 'ExchPointValue', typeName='float', repeatingHeaderId=None, vendor='TT', description='Size of one point for this  security'),
	FIXTag(16624, 'LegSide_TT', typeName='char', repeatingHeaderId=None, vendor='TT', description='Side of the leg (1=Buy, 2=Sell)'),
	FIXTag(18100, 'LegExDestination', typeName='Exchange', repeatingHeaderId=None, vendor='TT', description='Exchange the leg trades on'),
	FIXTag(18211, 'ContractTerm', typeName='char', repeatingHeaderId=None, vendor='TT', description='The term of the contract (Y=yearly, Q=quarterly, etc.)'),
	FIXTag(18212, 'LegDeliveryTerm', typeName='char', repeatingHeaderId=None, vendor='TT', description='Delivery term of the leg'),
	FIXTag(18224, 'LegContractYearMonth', typeName='MonthYear', repeatingHeaderId=None, vendor='TT', description='Month and year in which the leg matures'),
	FIXTag(18314, 'LegMaturityDay', typeName='DayOfMonth', repeatingHeaderId=None, vendor='TT', description='Day of the month on which the leg matures'),
##### END GENERATED CODE
]

TAG_ID_TO_TAG = {}
TAG_NAME_TO_TAG = {}
for tag in TAGS:
	assert(tag.id() not in TAG_ID_TO_TAG)
	TAG_ID_TO_TAG[tag.id()] = tag

	if tag.name() in TAG_NAME_TO_TAG:
		raise RuntimeError('Duplicate tag name %s' % tag.name())
	TAG_NAME_TO_TAG[tag.name()] = tag

SECURITY_ID_SOURCES = {
	'1': 'CUSIP',
	'2': 'SEDOL',
	'3': 'QUIK',
	'4': 'ISIN',
	'5': 'RIC',
	'6': 'ISO 4217',
	'7': 'ISO 3166-1',
	'8': 'Exchange Symbol',
	'9': 'CTA',
	'A': 'Bloomberg',
	'B': 'Wertpapier',
	'C': 'Dutch',
	'D': 'Valoren',
	'E': 'Sicovam',
	'F': 'Belgian',
	'G': 'Clearstream',
	'H': 'Clearing',
	'I': 'ISDA',
	'J': 'OPRA',
	'94': 'Alt Symbol',
	'95': 'Clearport',
	'96': 'TT',
	'97': 'TT Alias',
	'98': 'Name',
	'99': 'Other',
}

DELIVERY_TERM = {
	'A': 'Same day',
	'B': 'Balance of month',
	'D': 'Daily',
	'L': 'Balance of week',
	'N': 'Next day',
	'M': 'Monthly',
	'Q': 'Quarterly',
	'S': 'Seasonal',
	'V': 'Variable',
	'W': 'Weekly',
	'X': 'Custom',
	'Y': 'Yearly',
}

#Separate from the tags for ease of code generation
TAG_ENUM_VALUES = {
	35: {
		'0': 'Heartbeat',
		'1': 'Test Request',
		'2': 'Resend Request',
		'3': 'Reject',
		'4': 'Sequence Reset',
		'5': 'Logout',
		'6': 'Indication of Interest',
		'7': 'Advertisement',
		'8': 'Execution Report',
		'9': 'Order Cancel Reject',
		'A': 'Logon',
		'B': 'News',
		'C': 'Email',
		'D': 'Order - Single',
		'E': 'Order - List',
		'F': 'Order Cancel Request',
		'G': 'Order Cancel/Replace Request',
		'H': 'Order Status Request',
		'J': 'Allocation',
		'K': 'List Cancel Request',
		'L': 'List Execute',
		'M': 'List Status Request',
		'N': 'List Status',
		'P': 'Allocation ACK',
		'Q': 'Don\'t Know Trade',
		'R': 'Quote Request',
		'S': 'Quote',
		'T': 'Settlement Instructions',
		'V': 'Market Data Request',
		'W': 'Market Data-Snapshot/Full Refresh',
		'X': 'Market Data-Incremental Refresh',
		'Y': 'Market Data Request Reject',
		'Z': 'Quote Cancel',
		'a': 'Quote Status Request',
		'b': 'Quote Acknowledgement',
		'c': 'Security Definition Request',
		'd': 'Security Definition',
		'e': 'Security Status Request',
		'f': 'Security Status',
		'g': 'Trading Session Status Request',
		'h': 'Trading Session Status',
		'i': 'Mass Quote',
		'j': 'Business Message Reject',
		'k': 'Bid Request',
		'l': 'Bid Response',
		'm': 'List Strike Price'
	},
	39: {
		'0': 'Order ack',
		'1': 'Partial fill',
		'2': 'Complete fill',
		'4': 'Cancel ack',
		'5': 'Modify ack',
		'8': 'Reject',
		'C': 'Expired',
		'H': 'Trade canceled',
	},
	40: {
		'1': 'Market order',
		'2': 'Limit order',
		'3': 'Stop order',
		'4': 'Stop-limit order',
		'K': 'Market-limit order',
	},
	54: {
		'1': 'Buy',
		'2': 'Sell',
		'3': 'Buy minus',
		'4': 'Sell plus',
		'5': 'Sell short',
		'6': 'Sell short exempt',
		'7': 'Undisclosed (valid for IOI and List Order messages only)',
		'8': 'Cross (orders where counterparty is an exchange, valid for all messages except IOIs)',
		'9': 'Cross short'
	},
	59: {
		'0': 'DAY',
		'1': 'GTC',
		'3': 'FAK',
		'6': 'GTD',
	},
	61: {
		'0': 'Normal',
		'1': 'Flash',
		'2': 'Background'
	},
	102: {
		'0': 'Too late to cancel',
		'1': 'Unknown order',
		'2': 'Broker/Exchange option',
		'3': 'Order already pending cancel or cancel-replace',
		'4': 'Unable to process mass cancel request',
		'5': 'OrigOrdModTime (tag 586) did not match last TransactTime (tag 60) of order',
		'6': 'Duplicate CLOrdID (tag 11) received',
		'7': 'Price exceeds current price',
		'8': 'Price exceeds current price band',
		'18': 'Invalid price increment',
		'99': 'Other',
		'2045': 'This order is not in the book',
		'1003': 'Orders may not be canceled while the market is closed',
	},
	150: {
		'0': 'Order ack',
		'1': 'Partial fill',
		'2': 'Complete fill',
		'4': 'Cancel ack',
		'5': 'Modify ack',
		'8': 'Reject',
		'C': 'Expired',
		'H': 'Trade canceled',
	},
	201: {
		'0': 'Put',
		'1': 'Call',
	},
	456: SECURITY_ID_SOURCES,
	460: {
		'1': 'Agency',
		'2': 'Commodity',
		'3': 'Corporate',
		'4': 'Currency',
		'5': 'Equity',
		'6': 'Government',
		'7': 'Index',
		'8': 'Loan',
		'9': 'Money Market',
		'10': 'Mortgage',
		'11': 'Municipal',
		'12': 'Other',
		'13': 'Financing',
	},
	603: SECURITY_ID_SOURCES,
	606: SECURITY_ID_SOURCES,
	624: {
		'1': 'Buy',
		'2': 'Sell'
	},
	731: {
		'1': 'Final',
		'2': 'Theoretical',
		'100': 'Actual preliminary (instrument not subject to settlement price rounding)',
		'101': 'Actual preliminary (instrument subject to settlement price rounding)'
	},
	827: {
		'0': 'Expire on trading session close',
		'2': 'Expiration at given date'
	},
	865: {
		'5': 'Activation',
		'7': 'Last eligible trade date'
	},
	980: {
		'A': 'Add',
		'D': 'Delete',
		'M': 'Modify'
	},
	1093: {
		'2': 'Minimum order entry quantity',
		'3': 'Minimum quantity required for block trade',
		'4': 'Round lot (variable quantity products)'
	},
	1128: {
		'9': 'FIX50SP2',
	},
	1142: {
		'F': 'FIFO',
		'K': 'Configurable',
		'C': 'Pro-Rata',
		'A': 'Allocation',
		'T': 'FIFO with LLM',
		'O': 'Threshold Pro-Rata',
		'S': 'FIFO with TOP and LLM',
		'Q': 'Threshold Pro-Rata with LLM',
		'Y': 'Eurodollar options'
	},
	1144: {
		'0': 'Non-implied instrument',
		'3': 'Implied instrument'
	},
	1435: {
		'1': 'Multiplied by hour',
		'2': 'Multiplied by day'
	},
	9779: {
		'Y': 'User defined',
		'N': 'Not user defined'
	},
	9853: {
		'F': 'Fisher-Black',
		'W': 'Whaley'
	},
	18211: DELIVERY_TERM,
	18212: DELIVERY_TERM,
}
