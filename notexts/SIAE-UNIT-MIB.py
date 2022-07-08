#
# PySNMP MIB module SIAE-UNIT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-UNIT-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:28:16 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
unitTypeUnequipped, = mibBuilder.importSymbols("SIAE-UNITYPE-MIB", "unitTypeUnequipped")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, Bits, ModuleIdentity, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, iso, ObjectIdentity, Counter32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Bits", "ModuleIdentity", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "iso", "ObjectIdentity", "Counter32", "IpAddress", "Integer32")
RowStatus, TextualConvention, DisplayString, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "AutonomousType")
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
mibBuilder.exportSymbols("SIAE-UNIT-MIB", unitTable=unitTable, unitNotRespondingAlarmSeverityCode=unitNotRespondingAlarmSeverityCode, unitFailAlarmSeverityCode=unitFailAlarmSeverityCode, unitLabel=unitLabel, unitRowStatus=unitRowStatus, unitSwMismatchAlarmSeverityCode=unitSwMismatchAlarmSeverityCode, unitRecord=unitRecord, unitHwMismatchAlarm=unitHwMismatchAlarm, unitNotRespondingAlarm=unitNotRespondingAlarm, unitActualType=unitActualType, unitParentPartNumber=unitParentPartNumber, unitExpectedType=unitExpectedType, unitHwEdition=unitHwEdition, unitHwMismatchAlarmSeverityCode=unitHwMismatchAlarmSeverityCode, unit=unit, unitId=unitId, unitMissingAlarm=unitMissingAlarm, PYSNMP_MODULE_ID=unit, unitParentSerialNumber=unitParentSerialNumber, unitMissingAlarmSeverityCode=unitMissingAlarmSeverityCode, unitMibVersion=unitMibVersion, unitPartNumber=unitPartNumber, unitFailAlarm=unitFailAlarm, unitSwMismatchAlarm=unitSwMismatchAlarm)
