#
# PySNMP MIB module SIAE-PMTXPWR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-PMTXPWR-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:27 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, IpAddress, Unsigned32, Integer32, TimeTicks, ObjectIdentity, MibIdentifier, NotificationType, Gauge32, Counter32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "IpAddress", "Unsigned32", "Integer32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "NotificationType", "Gauge32", "Counter32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
pmTxPwr = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 13))
pmTxPwr.setRevisions(('2014-10-07 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: pmTxPwr.setLastUpdated('201410070000Z')
if mibBuilder.loadTexts: pmTxPwr.setOrganization('SIAE MICROELETTRONICA spa')
pmTxPwrMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrMibVersion.setStatus('current')
pmTxPwrCounterTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2), )
if mibBuilder.loadTexts: pmTxPwrCounterTable.setStatus('current')
pmTxPwrCounterRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1), ).setIndexNames((0, "SIAE-PMTXPWR-MIB", "pmTxPwrBranchId"), (0, "SIAE-PMTXPWR-MIB", "pmTxPwrCounterBlockId"))
if mibBuilder.loadTexts: pmTxPwrCounterRecord.setStatus('current')
pmTxPwrBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrBranchId.setStatus('current')
pmTxPwrCounterBlockId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrCounterBlockId.setStatus('current')
pmTxPwrCounterBlockType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("daily", 1), ("fifteenMin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrCounterBlockType.setStatus('current')
pmTxPwrCounterBlockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meaningless", 1), ("meaningfull", 2), ("incomplete", 3), ("dummy", 4), ("lost", 5), ("restarted", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrCounterBlockStatus.setStatus('current')
pmTxPwrCounterTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrCounterTimeStamp.setStatus('current')
pmTxPwrTlts1Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTlts1Counter.setStatus('current')
pmTxPwrTlts2Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTlts2Counter.setStatus('current')
pmTxPwrTlts3Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTlts3Counter.setStatus('current')
pmTxPwrTlts4Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTlts4Counter.setStatus('current')
pmTxPwrTMMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTMMax.setStatus('current')
pmTxPwrTMMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTMMin.setStatus('current')
pmTxPwrAverageTxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrAverageTxLevel.setStatus('current')
pmTxPwrTpClassTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3), )
if mibBuilder.loadTexts: pmTxPwrTpClassTable.setStatus('current')
pmTxPwrTpClassRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1), ).setIndexNames((0, "SIAE-PMTXPWR-MIB", "pmTxPwrTpClassBranchId"))
if mibBuilder.loadTexts: pmTxPwrTpClassRecord.setStatus('current')
pmTxPwrTpClassBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClassBranchId.setStatus('current')
pmTxPwrTpClassStartStop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassStartStop.setStatus('current')
pmTxPwrTpClassLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClassLabel.setStatus('current')
pmTxPwrTpClassTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClassTimeStamp.setStatus('current')
pmTxPwrTpClass15MTlts1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts1Alarm.setStatus('current')
pmTxPwrTpClass15MTlts2Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts2Alarm.setStatus('current')
pmTxPwrTpClass15MTlts3Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts3Alarm.setStatus('current')
pmTxPwrTpClass15MTlts4Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts4Alarm.setStatus('current')
pmTxPwrTpClass24HTlts1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts1Alarm.setStatus('current')
pmTxPwrTpClass24HTlts2Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts2Alarm.setStatus('current')
pmTxPwrTpClass24HTlts3Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 11), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts3Alarm.setStatus('current')
pmTxPwrTpClass24HTlts4Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 12), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts4Alarm.setStatus('current')
pmTxPwrTpClassTlt1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-30)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassTlt1Threshold.setStatus('current')
pmTxPwrTpClassTlt2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-40)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassTlt2Threshold.setStatus('current')
pmTxPwrTpClassTlt3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassTlt3Threshold.setStatus('current')
pmTxPwrTpClassTlt4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassTlt4Threshold.setStatus('current')
pmTxPwrTpClass15MTlts1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts1Threshold.setStatus('current')
pmTxPwrTpClass15MTlts2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 18), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts2Threshold.setStatus('current')
pmTxPwrTpClass15MTlts3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 19), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts3Threshold.setStatus('current')
pmTxPwrTpClass15MTlts4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 20), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTlts4Threshold.setStatus('current')
pmTxPwrTpClass24HTlts1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 21), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts1Threshold.setStatus('current')
pmTxPwrTpClass24HTlts2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 22), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts2Threshold.setStatus('current')
pmTxPwrTpClass24HTlts3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 23), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts3Threshold.setStatus('current')
pmTxPwrTpClass24HTlts4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 24), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTlts4Threshold.setStatus('current')
pmTxPwrTpClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 3, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmTxPwrTpClassRowStatus.setStatus('current')
pmTxPwrTpMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4), )
if mibBuilder.loadTexts: pmTxPwrTpMaintTable.setStatus('current')
pmTxPwrTpMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1), ).setIndexNames((0, "SIAE-PMTXPWR-MIB", "pmTxPwrTpClassBranchId"))
if mibBuilder.loadTexts: pmTxPwrTpMaintRecord.setStatus('current')
pmTxPwrTpMaintCounterClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTxPwrTpMaintCounterClear.setStatus('current')
pmTxPwrTpMaintAlarmClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTxPwrTpMaintAlarmClear.setStatus('current')
pmTxPwrTpClass15MTltsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTxPwrTpClass15MTltsAlarmSeverityCode.setStatus('current')
pmTxPwrTpClass24HTltsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 13, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmTxPwrTpClass24HTltsAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-PMTXPWR-MIB", pmTxPwrTpClassTlt1Threshold=pmTxPwrTpClassTlt1Threshold, pmTxPwrTpClass15MTlts3Threshold=pmTxPwrTpClass15MTlts3Threshold, pmTxPwrCounterTable=pmTxPwrCounterTable, pmTxPwrTpMaintRecord=pmTxPwrTpMaintRecord, pmTxPwrTpClassTable=pmTxPwrTpClassTable, pmTxPwrCounterBlockId=pmTxPwrCounterBlockId, pmTxPwrTMMin=pmTxPwrTMMin, pmTxPwrTpClass24HTlts1Alarm=pmTxPwrTpClass24HTlts1Alarm, pmTxPwrTpClass24HTlts1Threshold=pmTxPwrTpClass24HTlts1Threshold, pmTxPwrTlts2Counter=pmTxPwrTlts2Counter, pmTxPwrTpClass15MTlts2Alarm=pmTxPwrTpClass15MTlts2Alarm, pmTxPwrTpClassTlt3Threshold=pmTxPwrTpClassTlt3Threshold, pmTxPwrBranchId=pmTxPwrBranchId, pmTxPwrTpClass15MTlts4Threshold=pmTxPwrTpClass15MTlts4Threshold, pmTxPwrTpClassTlt2Threshold=pmTxPwrTpClassTlt2Threshold, pmTxPwrTMMax=pmTxPwrTMMax, pmTxPwrTpClass24HTltsAlarmSeverityCode=pmTxPwrTpClass24HTltsAlarmSeverityCode, pmTxPwrTpClass15MTlts2Threshold=pmTxPwrTpClass15MTlts2Threshold, pmTxPwrCounterTimeStamp=pmTxPwrCounterTimeStamp, pmTxPwrTpMaintTable=pmTxPwrTpMaintTable, pmTxPwr=pmTxPwr, pmTxPwrTpClassStartStop=pmTxPwrTpClassStartStop, pmTxPwrTpClassTimeStamp=pmTxPwrTpClassTimeStamp, pmTxPwrTpClass24HTlts3Alarm=pmTxPwrTpClass24HTlts3Alarm, pmTxPwrTlts1Counter=pmTxPwrTlts1Counter, PYSNMP_MODULE_ID=pmTxPwr, pmTxPwrMibVersion=pmTxPwrMibVersion, pmTxPwrTpMaintAlarmClear=pmTxPwrTpMaintAlarmClear, pmTxPwrTlts4Counter=pmTxPwrTlts4Counter, pmTxPwrTpClass24HTlts4Threshold=pmTxPwrTpClass24HTlts4Threshold, pmTxPwrTpClass24HTlts3Threshold=pmTxPwrTpClass24HTlts3Threshold, pmTxPwrAverageTxLevel=pmTxPwrAverageTxLevel, pmTxPwrCounterBlockType=pmTxPwrCounterBlockType, pmTxPwrTlts3Counter=pmTxPwrTlts3Counter, pmTxPwrTpClassLabel=pmTxPwrTpClassLabel, pmTxPwrTpClass24HTlts2Alarm=pmTxPwrTpClass24HTlts2Alarm, pmTxPwrCounterBlockStatus=pmTxPwrCounterBlockStatus, pmTxPwrTpClassRecord=pmTxPwrTpClassRecord, pmTxPwrTpMaintCounterClear=pmTxPwrTpMaintCounterClear, pmTxPwrTpClass15MTlts1Alarm=pmTxPwrTpClass15MTlts1Alarm, pmTxPwrTpClass15MTltsAlarmSeverityCode=pmTxPwrTpClass15MTltsAlarmSeverityCode, pmTxPwrCounterRecord=pmTxPwrCounterRecord, pmTxPwrTpClassTlt4Threshold=pmTxPwrTpClassTlt4Threshold, pmTxPwrTpClass15MTlts3Alarm=pmTxPwrTpClass15MTlts3Alarm, pmTxPwrTpClass24HTlts4Alarm=pmTxPwrTpClass24HTlts4Alarm, pmTxPwrTpClassRowStatus=pmTxPwrTpClassRowStatus, pmTxPwrTpClass15MTlts4Alarm=pmTxPwrTpClass15MTlts4Alarm, pmTxPwrTpClass15MTlts1Threshold=pmTxPwrTpClass15MTlts1Threshold, pmTxPwrTpClass24HTlts2Threshold=pmTxPwrTpClass24HTlts2Threshold, pmTxPwrTpClassBranchId=pmTxPwrTpClassBranchId)
