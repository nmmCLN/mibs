#
# PySNMP MIB module TAIT-INFRA93SERIES-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93SERIES-TC-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:16:04 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, Gauge32, Counter32, IpAddress, Integer32, Unsigned32, ModuleIdentity, ObjectIdentity, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Gauge32", "Counter32", "IpAddress", "Integer32", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
infra93_94TC, = mibBuilder.importSymbols("TAIT-INFRA93-94SERIES-TC-MIB", "infra93-94TC")
infra93TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 10, 1, 1))
infra93TC.setRevisions(('2019-05-29 00:26', '2018-05-22 00:26', '2017-07-28 00:00', '2016-11-18 00:00', '2016-07-01 00:00', '2014-10-30 15:00', '2014-04-14 00:00', '2014-01-26 00:00', '2014-01-14 11:00',))
if mibBuilder.loadTexts: infra93TC.setLastUpdated('201905290026Z')
if mibBuilder.loadTexts: infra93TC.setOrganization('www.taitradio.com')
class Ratio(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-256, 255)

class LeveldBm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class SINADLevel(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class Temperature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class FrequencydHz(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class DcsCode(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'o'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubAudibleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("ctcss", 1), ("dcs", 2))

class TxFrequencyResponse(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pre-emph-speech", 1), ("flat-speech", 2))

class RxFrequencyResponse(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("de-emph-speech", 1))

class OperationalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("analogConventional", 1), ("dmrConventional", 2), ("dmrTrunking", 3), ("mptTrunking", 4))

class MPTControlProtocolStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unconnected", 0), ("idle", 1), ("control", 2), ("traffic", 3), ("conventional", 4))

class FallbackNodeStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("active", 1), ("inactive", 2), ("settling", 3), ("disabled", 4))

class ColourCode(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class TransmitterSyncStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("no-license", 0), ("non-simulcast-operation", 1), ("frequency-reference-bad-or-absent", 2), ("never-had-1pps", 3), ("never-had-ntp", 4), ("missing-1pps-or-ntp", 5), ("synchronized", 6), ("non-channelgroup-operation", 7))

class ReceiverSyncStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("no-license", 0), ("non-channelgroup-operation", 1), ("synchronized", 2), ("never-had-1pps", 3), ("never-had-ntp", 4), ("missing-1pps-or-ntp", 5))

class ControlProtocolStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unconnected", 0), ("deprecatedUnconnected", 1), ("standby", 2), ("dmrAligned", 3), ("dmrOffset", 4), ("dmr2SlotData", 5), ("dmrHibernate", 6), ("analogue", 7), ("testMode", 8), ("dmrTier2Aligned", 9))

class LogicalChannelState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))
    namedValues = NamedValues(("inactive", 0), ("idle", 1), ("traffic", 2), ("control", 3), ("test", 4), ("poll", 5), ("invalid", 255))

class StandaloneNodeStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6))
    namedValues = NamedValues(("offline", 0), ("standby", 1), ("active", 2), ("disabled", 4), ("running", 5), ("master", 6))

mibBuilder.exportSymbols("TAIT-INFRA93SERIES-TC-MIB", LeveldBm=LeveldBm, Temperature=Temperature, RxFrequencyResponse=RxFrequencyResponse, FallbackNodeStatus=FallbackNodeStatus, TransmitterSyncStatus=TransmitterSyncStatus, DcsCode=DcsCode, SubAudibleType=SubAudibleType, ControlProtocolStatus=ControlProtocolStatus, MPTControlProtocolStatus=MPTControlProtocolStatus, StandaloneNodeStatus=StandaloneNodeStatus, ReceiverSyncStatus=ReceiverSyncStatus, FrequencydHz=FrequencydHz, ColourCode=ColourCode, TxFrequencyResponse=TxFrequencyResponse, PYSNMP_MODULE_ID=infra93TC, OperationalMode=OperationalMode, LogicalChannelState=LogicalChannelState, SINADLevel=SINADLevel, Ratio=Ratio, infra93TC=infra93TC)
