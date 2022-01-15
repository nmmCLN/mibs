#
# PySNMP MIB module SIAE-ACM-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-ACM-STATISTICS-MIB
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
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
acmStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 75))
acmStats.setRevisions(('2014-11-05 00:00', '2014-02-11 00:00',))
if mibBuilder.loadTexts: acmStats.setLastUpdated('201411050000Z')
if mibBuilder.loadTexts: acmStats.setOrganization('SIAE MICROELETTRONICA spa')
class AcmProfile(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("unavailable", 1), ("downshift", 2), ("upshift", 3), ("acmBPSKstrong", 4), ("acmBPSK", 5), ("acm4QAMstrong", 6), ("acm4QAM", 7), ("acm8PSKstrong", 8), ("acm8PSK", 9), ("acm16QAMstrong", 10), ("acm16QAM", 11), ("acm32QAMstrong", 12), ("acm32QAM", 13), ("acm64QAMstrong", 14), ("acm64QAM", 15), ("acm128QAMstrong", 16), ("acm128QAM", 17), ("acm256QAMstrong", 18), ("acm256QAM", 19), ("acm512QAMstrong", 20), ("acm512QAM", 21), ("acm1024QAMstrong", 22), ("acm1024QAM", 23), ("acm2048QAMstrong", 24), ("acm2048QAM", 25), ("acm4096QAMstrong", 26), ("acm4096QAM", 27))

acmsMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsMibVersion.setStatus('current')
acmsTpLinkTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2), )
if mibBuilder.loadTexts: acmsTpLinkTable.setStatus('current')
acmsTpLinkRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"))
if mibBuilder.loadTexts: acmsTpLinkRecord.setStatus('current')
acmsTpLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: acmsTpLinkId.setStatus('current')
acmsTpLinkPolId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: acmsTpLinkPolId.setStatus('current')
acmsTpLinkStartStop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2))).clone('stop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpLinkStartStop.setStatus('current')
acmsTpLinkLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsTpLinkLabel.setStatus('current')
acmsTpLinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpLinkRowStatus.setStatus('current')
acmsTpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3), )
if mibBuilder.loadTexts: acmsTpProfileTable.setStatus('current')
acmsTpProfileRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpProfileId"))
if mibBuilder.loadTexts: acmsTpProfileRecord.setStatus('current')
acmsTpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 1), AcmProfile())
if mibBuilder.loadTexts: acmsTpProfileId.setStatus('current')
acmsTpProfile15mAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 2), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsTpProfile15mAlarm.setStatus('current')
acmsTpProfile24hAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsTpProfile24hAlarm.setStatus('current')
acmsTpProfile15mThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpProfile15mThreshold.setStatus('current')
acmsTpProfile24hThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpProfile24hThreshold.setStatus('current')
acmsTpProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpProfileRowStatus.setStatus('current')
acmsTpMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4), )
if mibBuilder.loadTexts: acmsTpMaintTable.setStatus('current')
acmsTpMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"))
if mibBuilder.loadTexts: acmsTpMaintRecord.setStatus('current')
acmsTpMaintCounterClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acmsTpMaintCounterClear.setStatus('current')
acmsTpMaintAlarmClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acmsTpMaintAlarmClear.setStatus('current')
acmsIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5), )
if mibBuilder.loadTexts: acmsIntervalTable.setStatus('current')
acmsIntervalRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsIntervalId"))
if mibBuilder.loadTexts: acmsIntervalRecord.setStatus('current')
acmsIntervalId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsIntervalId.setStatus('current')
acmsIntervalType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("daily", 1), ("fifteen-min", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsIntervalType.setStatus('current')
acmsIntervalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meaningless", 1), ("meaningfull", 2), ("incomplete", 3), ("dummy", 4), ("lost", 5), ("restarted", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsIntervalStatus.setStatus('current')
acmsIntervalTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsIntervalTimeStamp.setStatus('current')
acmsProfileCounterTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6), )
if mibBuilder.loadTexts: acmsProfileCounterTable.setStatus('current')
acmsProfileCounterRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpProfileId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsIntervalId"))
if mibBuilder.loadTexts: acmsProfileCounterRecord.setStatus('current')
acmsProfileCounterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsProfileCounterValue.setStatus('current')
acmsTpProfile15mAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acmsTpProfile15mAlarmSeverityCode.setStatus('current')
acmsTpProfile24hAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acmsTpProfile24hAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-ACM-STATISTICS-MIB", acmsProfileCounterRecord=acmsProfileCounterRecord, acmsIntervalStatus=acmsIntervalStatus, acmsIntervalType=acmsIntervalType, acmsTpProfile15mAlarmSeverityCode=acmsTpProfile15mAlarmSeverityCode, acmsIntervalTable=acmsIntervalTable, acmsTpMaintAlarmClear=acmsTpMaintAlarmClear, acmsTpProfile15mAlarm=acmsTpProfile15mAlarm, acmsTpLinkLabel=acmsTpLinkLabel, acmsTpMaintCounterClear=acmsTpMaintCounterClear, acmsMibVersion=acmsMibVersion, acmsTpProfileRowStatus=acmsTpProfileRowStatus, acmsProfileCounterValue=acmsProfileCounterValue, acmsTpLinkPolId=acmsTpLinkPolId, AcmProfile=AcmProfile, acmsTpProfileRecord=acmsTpProfileRecord, acmsTpLinkRowStatus=acmsTpLinkRowStatus, acmsTpProfile15mThreshold=acmsTpProfile15mThreshold, acmsIntervalTimeStamp=acmsIntervalTimeStamp, acmsTpProfile24hAlarm=acmsTpProfile24hAlarm, acmsProfileCounterTable=acmsProfileCounterTable, acmsTpProfile24hAlarmSeverityCode=acmsTpProfile24hAlarmSeverityCode, acmsTpProfileTable=acmsTpProfileTable, acmsTpLinkRecord=acmsTpLinkRecord, acmsTpLinkTable=acmsTpLinkTable, PYSNMP_MODULE_ID=acmStats, acmsTpProfileId=acmsTpProfileId, acmsTpLinkId=acmsTpLinkId, acmsTpLinkStartStop=acmsTpLinkStartStop, acmsIntervalRecord=acmsIntervalRecord, acmStats=acmStats, acmsTpMaintTable=acmsTpMaintTable, acmsTpMaintRecord=acmsTpMaintRecord, acmsTpProfile24hThreshold=acmsTpProfile24hThreshold, acmsIntervalId=acmsIntervalId)
