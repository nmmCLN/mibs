#
# PySNMP MIB module SIAE-AGGRL1-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-AGGRL1-MANAGEMENT-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:16 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Bits, TimeTicks, Counter32, Unsigned32, ModuleIdentity, Counter64, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Counter32", "Unsigned32", "ModuleIdentity", "Counter64", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "iso")
RowStatus, DisplayString, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "StorageType")
aggregationL1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 83))
aggregationL1.setRevisions(('2014-09-29 00:00', '2014-05-26 00:00',))
if mibBuilder.loadTexts: aggregationL1.setLastUpdated('201409290000Z')
if mibBuilder.loadTexts: aggregationL1.setOrganization('SIAE MICROELETTRONICA spa')
class AggregableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("radio", 2), ("lan", 3))

aggrL1MibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1MibVersion.setStatus('current')
aggrL1CapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2), )
if mibBuilder.loadTexts: aggrL1CapabilityTable.setStatus('current')
aggrL1CapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1), ).setIndexNames((0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregableIndex"), (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregableType"), (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregatorIndex"))
if mibBuilder.loadTexts: aggrL1CapabilityEntry.setStatus('current')
aggrL1CapabilityAggregableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1CapabilityAggregableIndex.setStatus('current')
aggrL1CapabilityAggregableType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 2), AggregableType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1CapabilityAggregableType.setStatus('current')
aggrL1CapabilityAggregatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1CapabilityAggregatorIndex.setStatus('current')
aggrL1Table = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3), )
if mibBuilder.loadTexts: aggrL1Table.setStatus('current')
aggrL1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1), ).setIndexNames((0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AggregableIndex"), (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AggregableType"))
if mibBuilder.loadTexts: aggrL1Entry.setStatus('current')
aggrL1AggregableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1AggregableIndex.setStatus('current')
aggrL1AggregableType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 2), AggregableType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1AggregableType.setStatus('current')
aggrL1AggregatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrL1AggregatorIndex.setStatus('current')
aggrL1StorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrL1StorageType.setStatus('current')
aggrL1Rowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrL1Rowstatus.setStatus('current')
aggrL1AlarmTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4), )
if mibBuilder.loadTexts: aggrL1AlarmTable.setStatus('current')
aggrL1AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1), ).setIndexNames((0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AlarmAggregatorIndex"))
if mibBuilder.loadTexts: aggrL1AlarmEntry.setStatus('current')
aggrL1AlarmAggregatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1AlarmAggregatorIndex.setStatus('current')
aggrL1FailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 2), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1FailAlarm.setStatus('current')
aggrL1DegradeAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1DegradeAlarm.setStatus('current')
aggrL1RealignmentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 4), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1RealignmentAlarm.setStatus('current')
aggrL1FailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aggrL1FailAlarmSeverityCode.setStatus('current')
aggrL1DegradeAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aggrL1DegradeAlarmSeverityCode.setStatus('current')
aggrL1RealignmentAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aggrL1RealignmentAlarmSeverityCode.setStatus('current')
aggrL1ConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8), )
if mibBuilder.loadTexts: aggrL1ConnectionTable.setStatus('current')
aggrL1ConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1), ).setIndexNames((0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1ConnAggregableIndex"), (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1ConnAggregableType"))
if mibBuilder.loadTexts: aggrL1ConnectionEntry.setStatus('current')
aggrL1ConnAggregableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1ConnAggregableIndex.setStatus('current')
aggrL1ConnAggregableType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 2), AggregableType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1ConnAggregableType.setStatus('current')
aggrL1ConnAggregatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1ConnAggregatorIndex.setStatus('current')
mibBuilder.exportSymbols("SIAE-AGGRL1-MANAGEMENT-MIB", aggrL1ConnectionEntry=aggrL1ConnectionEntry, aggrL1Entry=aggrL1Entry, aggrL1Rowstatus=aggrL1Rowstatus, aggrL1ConnectionTable=aggrL1ConnectionTable, aggrL1ConnAggregableType=aggrL1ConnAggregableType, aggrL1AlarmTable=aggrL1AlarmTable, aggrL1RealignmentAlarm=aggrL1RealignmentAlarm, aggrL1DegradeAlarmSeverityCode=aggrL1DegradeAlarmSeverityCode, aggrL1AggregableIndex=aggrL1AggregableIndex, aggrL1FailAlarmSeverityCode=aggrL1FailAlarmSeverityCode, aggrL1CapabilityAggregatorIndex=aggrL1CapabilityAggregatorIndex, aggrL1FailAlarm=aggrL1FailAlarm, aggrL1CapabilityAggregableIndex=aggrL1CapabilityAggregableIndex, aggrL1AggregableType=aggrL1AggregableType, PYSNMP_MODULE_ID=aggregationL1, aggrL1CapabilityTable=aggrL1CapabilityTable, aggrL1CapabilityAggregableType=aggrL1CapabilityAggregableType, aggregationL1=aggregationL1, aggrL1ConnAggregableIndex=aggrL1ConnAggregableIndex, aggrL1MibVersion=aggrL1MibVersion, aggrL1AlarmEntry=aggrL1AlarmEntry, aggrL1StorageType=aggrL1StorageType, aggrL1ConnAggregatorIndex=aggrL1ConnAggregatorIndex, aggrL1DegradeAlarm=aggrL1DegradeAlarm, aggrL1AlarmAggregatorIndex=aggrL1AlarmAggregatorIndex, AggregableType=AggregableType, aggrL1RealignmentAlarmSeverityCode=aggrL1RealignmentAlarmSeverityCode, aggrL1CapabilityEntry=aggrL1CapabilityEntry, aggrL1Table=aggrL1Table, aggrL1AggregatorIndex=aggrL1AggregatorIndex)
