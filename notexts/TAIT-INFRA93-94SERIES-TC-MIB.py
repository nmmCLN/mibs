#
# PySNMP MIB module TAIT-INFRA93-94SERIES-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-INFRA93-94SERIES-TC-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:58 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, TimeTicks, IpAddress, Counter32, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "TimeTicks", "IpAddress", "Counter32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("TAIT-INFRA93-94SERIES-TC-MIB", BaseStationMode=BaseStationMode, AlarmState=AlarmState, Milliseconds=Milliseconds, ChannelGroupStatus=ChannelGroupStatus, OptionState=OptionState, Condition=Condition, FrequencyHz=FrequencyHz, PowerW=PowerW, PYSNMP_MODULE_ID=infra93_94TC, TransmitterStatus=TransmitterStatus, GateState=GateState, TimingControlType=TimingControlType, VoltageV=VoltageV, infra93_94TC=infra93_94TC, CurrentmA=CurrentmA)
