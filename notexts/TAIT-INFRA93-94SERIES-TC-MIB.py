#
# PySNMP MIB module TAIT-INFRA93-94SERIES-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-TC-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:34:38 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, NotificationType, MibIdentifier, Counter32, ObjectIdentity, Bits, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "MibIdentifier", "Counter32", "ObjectIdentity", "Bits", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
infra93_94MibModule, = mibBuilder.importSymbols("TAIT-INFRA93-94SERIES-COMMON-MIB", "infra93-94MibModule")
infra93_94TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 10, 1)).setLabel("infra93-94TC")
infra93_94TC.setRevisions(('2018-08-31 00:00', '2018-05-22 00:26', '2017-11-28 00:00', '2017-07-28 00:00', '2016-03-21 00:00', '2015-05-15 12:00', '2014-10-30 15:00', '2014-01-14 11:00',))
if mibBuilder.loadTexts: infra93_94TC.setLastUpdated('201808310000Z')
if mibBuilder.loadTexts: infra93_94TC.setOrganization('www.taitradio.com')
class BaseStationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("offline", 0), ("online", 1), ("unknown", 2))

class Condition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("bad", 0), ("good", 1), ("notFitted", 2))

class CurrentmA(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-3'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AlarmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unavailable", 0), ("cleared", 1), ("raised", 2), ("disabled", 3))

class FrequencyHz(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-6'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class PowerW(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class TransmitterStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("unconfigured", 1), ("untuned", 2), ("idle", 3), ("transmitting", 4), ("calibrating", 5), ("fault", 6))

class VoltageV(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class Milliseconds(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class ChannelGroupStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noLicense", 0), ("offline", 1), ("isolated", 2), ("satellite", 3), ("centralVoter", 4), ("singleBaseStation", 5), ("backupCentral", 6))

class TimingControlType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fixed", 0), ("selfRegulating", 1))

class GateState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("closed", 0), ("open", 1))

class OptionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

mibBuilder.exportSymbols("TAIT-INFRA93-94SERIES-TC-MIB", TimingControlType=TimingControlType, GateState=GateState, PowerW=PowerW, FrequencyHz=FrequencyHz, TransmitterStatus=TransmitterStatus, AlarmState=AlarmState, VoltageV=VoltageV, Milliseconds=Milliseconds, ChannelGroupStatus=ChannelGroupStatus, PYSNMP_MODULE_ID=infra93_94TC, Condition=Condition, infra93_94TC=infra93_94TC, OptionState=OptionState, BaseStationMode=BaseStationMode, CurrentmA=CurrentmA)
