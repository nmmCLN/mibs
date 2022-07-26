#
# PySNMP MIB module SIAE-UNIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-UNIT-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:34:11 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
unitTypeUnequipped, = mibBuilder.importSymbols("SIAE-UNITYPE-MIB", "unitTypeUnequipped")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, iso, Counter64, NotificationType, TimeTicks, Unsigned32, Gauge32, Bits, IpAddress, ObjectIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "iso", "Counter64", "NotificationType", "TimeTicks", "Unsigned32", "Gauge32", "Bits", "IpAddress", "ObjectIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, AutonomousType, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "DisplayString", "RowStatus")
unit = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 6))
unit.setRevisions(('2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: unit.setLastUpdated('201402030000Z')
if mibBuilder.loadTexts: unit.setOrganization('SIAE MICROELETTRONICA spa')
unitMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitMibVersion.setStatus('current')
unitTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2), )
if mibBuilder.loadTexts: unitTable.setStatus('current')
unitRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1), ).setIndexNames((0, "SIAE-UNIT-MIB", "unitId"))
if mibBuilder.loadTexts: unitRecord.setStatus('current')
unitId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitId.setStatus('current')
unitExpectedType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 2), AutonomousType().clone((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitExpectedType.setStatus('current')
unitActualType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 3), AutonomousType().clone((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 3, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitActualType.setStatus('current')
unitLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitLabel.setStatus('current')
unitFailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 5), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitFailAlarm.setStatus('current')
unitMissingAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 6), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitMissingAlarm.setStatus('current')
unitNotRespondingAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 7), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitNotRespondingAlarm.setStatus('current')
unitHwMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 8), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitHwMismatchAlarm.setStatus('current')
unitSwMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 9), AlarmStatus().clone('activeReportableMajor')).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitSwMismatchAlarm.setStatus('current')
unitHwEdition = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitHwEdition.setStatus('current')
unitPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitPartNumber.setStatus('current')
unitParentPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitParentPartNumber.setStatus('current')
unitParentSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitParentSerialNumber.setStatus('current')
unitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 2, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: unitRowStatus.setStatus('current')
unitFailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 4), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitFailAlarmSeverityCode.setStatus('current')
unitMissingAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitMissingAlarmSeverityCode.setStatus('current')
unitNotRespondingAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitNotRespondingAlarmSeverityCode.setStatus('current')
unitHwMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitHwMismatchAlarmSeverityCode.setStatus('current')
unitSwMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 6, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitSwMismatchAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-UNIT-MIB", unitMissingAlarm=unitMissingAlarm, unit=unit, unitSwMismatchAlarm=unitSwMismatchAlarm, unitHwMismatchAlarm=unitHwMismatchAlarm, unitId=unitId, unitFailAlarmSeverityCode=unitFailAlarmSeverityCode, unitSwMismatchAlarmSeverityCode=unitSwMismatchAlarmSeverityCode, unitNotRespondingAlarm=unitNotRespondingAlarm, unitMibVersion=unitMibVersion, unitParentPartNumber=unitParentPartNumber, unitFailAlarm=unitFailAlarm, unitActualType=unitActualType, unitParentSerialNumber=unitParentSerialNumber, unitMissingAlarmSeverityCode=unitMissingAlarmSeverityCode, unitHwEdition=unitHwEdition, unitRowStatus=unitRowStatus, unitTable=unitTable, unitLabel=unitLabel, unitNotRespondingAlarmSeverityCode=unitNotRespondingAlarmSeverityCode, unitExpectedType=unitExpectedType, unitPartNumber=unitPartNumber, PYSNMP_MODULE_ID=unit, unitHwMismatchAlarmSeverityCode=unitHwMismatchAlarmSeverityCode, unitRecord=unitRecord)
