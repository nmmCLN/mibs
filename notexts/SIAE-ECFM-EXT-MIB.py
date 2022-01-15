#
# PySNMP MIB module SIAE-ECFM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-ECFM-EXT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:34:25 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Counter32, NotificationType, Gauge32, MibIdentifier, Bits, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
siaeEcfmExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 94))
siaeEcfmExtMib.setRevisions(('2016-07-25 00:00', '2015-06-26 00:00', '2015-04-14 00:00',))
if mibBuilder.loadTexts: siaeEcfmExtMib.setLastUpdated('201607250000Z')
if mibBuilder.loadTexts: siaeEcfmExtMib.setOrganization('SIAE MICROELETTRONICA spa')
siaeEcfmExtMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: siaeEcfmExtMibVersion.setStatus('current')
siaeMepAlarms8021agTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2), )
if mibBuilder.loadTexts: siaeMepAlarms8021agTable.setStatus('current')
siaeMepAlarms8021agEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1), ).setIndexNames((0, "SIAE-ECFM-EXT-MIB", "defMIEcfmContextId"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMdIndex"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMaIndex"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmMepIdentifier"))
if mibBuilder.loadTexts: siaeMepAlarms8021agEntry.setStatus('current')
defMIEcfmContextId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmContextId.setStatus('current')
defMIEcfmMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmMdIndex.setStatus('current')
defMIEcfmMaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmMaIndex.setStatus('current')
defMIEcfmMepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 4), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmMepIdentifier.setStatus('current')
defRdiCcmAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defRdiCcmAlarm.setStatus('current')
defMacStatusAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defMacStatusAlarm.setStatus('current')
defRemoteCcmAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defRemoteCcmAlarm.setStatus('current')
defErrorCcmAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defErrorCcmAlarm.setStatus('current')
defXconCcmAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 2, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defXconCcmAlarm.setStatus('current')
siaeMepAlarmsY1731Table = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3), )
if mibBuilder.loadTexts: siaeMepAlarmsY1731Table.setStatus('current')
siaeMepAlarmsY1731Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1), ).setIndexNames((0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731ContextId"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MegIndex"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MeIndex"), (0, "SIAE-ECFM-EXT-MIB", "defMIEcfmY1731MepIdentifier"))
if mibBuilder.loadTexts: siaeMepAlarmsY1731Entry.setStatus('current')
defMIEcfmY1731ContextId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmY1731ContextId.setStatus('current')
defMIEcfmY1731MegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmY1731MegIndex.setStatus('current')
defMIEcfmY1731MeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmY1731MeIndex.setStatus('current')
defMIEcfmY1731MepIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 4), Unsigned32())
if mibBuilder.loadTexts: defMIEcfmY1731MepIdentifier.setStatus('current')
defRdiConditionAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defRdiConditionAlarm.setStatus('current')
defLossOfContinuityAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defLossOfContinuityAlarm.setStatus('current')
defUnexpectedPeriodAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defUnexpectedPeriodAlarm.setStatus('current')
defUnexpectedMepAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defUnexpectedMepAlarm.setStatus('current')
defMisMergeAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defMisMergeAlarm.setStatus('current')
defUnexpectedMegLevelAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defUnexpectedMegLevelAlarm.setStatus('current')
defAisConditionAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 11), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defAisConditionAlarm.setStatus('current')
defLckConditionAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 3, 1, 12), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: defLckConditionAlarm.setStatus('current')
mepRdiCcmAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 4), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepRdiCcmAlarmsSeverityCode.setStatus('current')
mepMacStatusAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepMacStatusAlarmsSeverityCode.setStatus('current')
mepRemoteCcmAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepRemoteCcmAlarmsSeverityCode.setStatus('current')
mepErrorCcmAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepErrorCcmAlarmsSeverityCode.setStatus('current')
mepXconCcmAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepXconCcmAlarmsSeverityCode.setStatus('current')
mepRdiConditionAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 9), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepRdiConditionAlarmsSeverityCode.setStatus('current')
mepLossOfContinuityAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 10), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepLossOfContinuityAlarmsSeverityCode.setStatus('current')
mepUnexpectedPeriodAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 11), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepUnexpectedPeriodAlarmsSeverityCode.setStatus('current')
mepUnexpectedMepAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 12), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepUnexpectedMepAlarmsSeverityCode.setStatus('current')
mepMisMergeAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 13), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepMisMergeAlarmsSeverityCode.setStatus('current')
mepUnexpectedMegLevelAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 14), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepUnexpectedMegLevelAlarmsSeverityCode.setStatus('current')
mepAisConditionAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 15), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepAisConditionAlarmsSeverityCode.setStatus('current')
mepLckConditionAlarmsSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 94, 16), AlarmSeverityCode().clone('statusTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mepLckConditionAlarmsSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-ECFM-EXT-MIB", siaeMepAlarmsY1731Entry=siaeMepAlarmsY1731Entry, mepMisMergeAlarmsSeverityCode=mepMisMergeAlarmsSeverityCode, defLckConditionAlarm=defLckConditionAlarm, defMIEcfmMdIndex=defMIEcfmMdIndex, defAisConditionAlarm=defAisConditionAlarm, defRdiCcmAlarm=defRdiCcmAlarm, defMIEcfmY1731MegIndex=defMIEcfmY1731MegIndex, defMIEcfmMepIdentifier=defMIEcfmMepIdentifier, defMIEcfmY1731MepIdentifier=defMIEcfmY1731MepIdentifier, mepRdiConditionAlarmsSeverityCode=mepRdiConditionAlarmsSeverityCode, mepUnexpectedMegLevelAlarmsSeverityCode=mepUnexpectedMegLevelAlarmsSeverityCode, defErrorCcmAlarm=defErrorCcmAlarm, defUnexpectedPeriodAlarm=defUnexpectedPeriodAlarm, defMIEcfmY1731MeIndex=defMIEcfmY1731MeIndex, siaeMepAlarms8021agEntry=siaeMepAlarms8021agEntry, defMisMergeAlarm=defMisMergeAlarm, mepRdiCcmAlarmsSeverityCode=mepRdiCcmAlarmsSeverityCode, defUnexpectedMegLevelAlarm=defUnexpectedMegLevelAlarm, siaeMepAlarms8021agTable=siaeMepAlarms8021agTable, defMIEcfmMaIndex=defMIEcfmMaIndex, mepLossOfContinuityAlarmsSeverityCode=mepLossOfContinuityAlarmsSeverityCode, defMIEcfmContextId=defMIEcfmContextId, defRemoteCcmAlarm=defRemoteCcmAlarm, mepUnexpectedPeriodAlarmsSeverityCode=mepUnexpectedPeriodAlarmsSeverityCode, siaeEcfmExtMib=siaeEcfmExtMib, mepRemoteCcmAlarmsSeverityCode=mepRemoteCcmAlarmsSeverityCode, defLossOfContinuityAlarm=defLossOfContinuityAlarm, mepXconCcmAlarmsSeverityCode=mepXconCcmAlarmsSeverityCode, defXconCcmAlarm=defXconCcmAlarm, mepUnexpectedMepAlarmsSeverityCode=mepUnexpectedMepAlarmsSeverityCode, defUnexpectedMepAlarm=defUnexpectedMepAlarm, mepErrorCcmAlarmsSeverityCode=mepErrorCcmAlarmsSeverityCode, defMIEcfmY1731ContextId=defMIEcfmY1731ContextId, siaeMepAlarmsY1731Table=siaeMepAlarmsY1731Table, mepLckConditionAlarmsSeverityCode=mepLckConditionAlarmsSeverityCode, mepAisConditionAlarmsSeverityCode=mepAisConditionAlarmsSeverityCode, defMacStatusAlarm=defMacStatusAlarm, siaeEcfmExtMibVersion=siaeEcfmExtMibVersion, mepMacStatusAlarmsSeverityCode=mepMacStatusAlarmsSeverityCode, PYSNMP_MODULE_ID=siaeEcfmExtMib, defRdiConditionAlarm=defRdiConditionAlarm)
