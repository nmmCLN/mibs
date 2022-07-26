#
# PySNMP MIB module SIAE-SYNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SYNC-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:34:11 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, iso, Counter64, NotificationType, TimeTicks, Unsigned32, Gauge32, Bits, IpAddress, ObjectIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "iso", "Counter64", "NotificationType", "TimeTicks", "Unsigned32", "Gauge32", "Bits", "IpAddress", "ObjectIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
sync = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 28))
sync.setRevisions(('2014-04-02 00:00', '2014-02-17 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: sync.setLastUpdated('201404020000Z')
if mibBuilder.loadTexts: sync.setOrganization('SIAE MICROELETTRONICA spa')
syncMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncMibVersion.setStatus('current')
timingGeneratorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2), )
if mibBuilder.loadTexts: timingGeneratorTable.setStatus('current')
timingGeneratorRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1), ).setIndexNames((0, "SIAE-SYNC-MIB", "timingGeneratorId"))
if mibBuilder.loadTexts: timingGeneratorRecord.setStatus('current')
timingGeneratorId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorId.setStatus('current')
timingGeneratorT4vsT0 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t4NotEqualT0", 1), ("t4EqualT0", 2))).clone('t4EqualT0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorT4vsT0.setStatus('current')
timingGeneratorHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1800)).clone(300)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorHoldOffTime.setStatus('current')
timingGeneratorWtrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorWtrTime.setStatus('current')
timingGeneratorSinkLosSet = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorSinkLosSet.setStatus('current')
timingGeneratorSinkLosReset = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorSinkLosReset.setStatus('current')
timingGeneratorT0SquelchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorT0SquelchAlarm.setStatus('current')
timingGeneratorT4SquelchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorT4SquelchAlarm.setStatus('current')
timingGeneratorFreeRunningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorFreeRunningStatus.setStatus('current')
timingGeneratorHoldoverStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorHoldoverStatus.setStatus('current')
timingGeneratorActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableStatus", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorActiveStatus.setStatus('current')
timingGeneratorT0CurrentQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorT0CurrentQuality.setStatus('current')
timingGeneratorT4CurrentQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorT4CurrentQuality.setStatus('current')
timingGeneratorT4MinimumQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4, 8, 11))).clone(namedValues=NamedValues(("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11))).clone('qSEC')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorT4MinimumQuality.setStatus('current')
timingGeneratorT0PreferredSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 15), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorT0PreferredSource.setStatus('current')
timingGeneratorT4PreferredSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 16), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorT4PreferredSource.setStatus('current')
timingGeneratorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorRowStatus.setStatus('current')
timingGeneratorMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3), )
if mibBuilder.loadTexts: timingGeneratorMaintTable.setStatus('current')
timingGeneratorMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1), ).setIndexNames((0, "SIAE-SYNC-MIB", "timingGeneratorId"))
if mibBuilder.loadTexts: timingGeneratorMaintRecord.setStatus('current')
timingGeneratorT4Squelch = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT4Squelch.setStatus('current')
timingGeneratorStatusControl = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("freerunning", 1), ("holdover", 2), ("locked", 3))).clone('locked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorStatusControl.setStatus('current')
timingGeneratorT0ForcedSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT0ForcedSource.setStatus('current')
timingGeneratorT4ForcedSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT4ForcedSource.setStatus('current')
timingGeneratorWtrClearSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 5), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorWtrClearSource.setStatus('current')
timingSinkTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4), )
if mibBuilder.loadTexts: timingSinkTable.setStatus('current')
timingSinkRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1), ).setIndexNames((0, "SIAE-SYNC-MIB", "timingSinkGenId"), (0, "SIAE-SYNC-MIB", "timingSinkId"), (0, "SIAE-SYNC-MIB", "timingSinkType"))
if mibBuilder.loadTexts: timingSinkRecord.setStatus('current')
timingSinkGenId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkGenId.setStatus('current')
timingSinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkId.setStatus('current')
timingSinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t0", 1), ("t4", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkType.setStatus('current')
timingSinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkIfIndex.setStatus('current')
timingSinkSelector = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkSelector.setStatus('current')
timingSinkPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("p1", 1), ("p2", 2), ("p3", 3), ("p4", 4), ("p5", 5), ("p6", 6), ("p7", 7), ("p8", 8), ("p9", 9), ("p10", 10), ("p11", 11), ("p12", 12), ("p13", 13), ("p14", 14), ("p15", 15), ("disable", 16))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkPriority.setStatus('current')
timingSinkLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkLabel.setStatus('current')
timingSinkLosAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkLosAlarm.setStatus('current')
timingSinkDriftAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkDriftAlarm.setStatus('current')
timingSinkActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableStatus", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkActiveStatus.setStatus('current')
timingSinkCurrentQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkCurrentQuality.setStatus('current')
timingSinkOverwriteTxQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("noOverwrite", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15))).clone('noOverwrite')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkOverwriteTxQuality.setStatus('current')
timingSinkOverwriteRxQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("noOverwrite", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15))).clone('noOverwrite')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkOverwriteRxQuality.setStatus('current')
timingSinkSentQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkSentQuality.setStatus('current')
timingSinkE1Sabit = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 8)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkE1Sabit.setStatus('current')
timingSinkEthPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2))).clone('dynamic')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkEthPortRole.setStatus('deprecated')
timingSinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkRowStatus.setStatus('current')
timingGeneratorManualSwitch = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorManualSwitch.setStatus('current')
timingGeneratorForcedSwitch = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorForcedSwitch.setStatus('current')
timingGeneratorT0SquelchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT0SquelchAlarmSeverityCode.setStatus('current')
timingGeneratorT4SquelchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT4SquelchAlarmSeverityCode.setStatus('current')
timingGeneratorFreeRunningStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 9), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorFreeRunningStatusSeverityCode.setStatus('current')
timingGeneratorHoldoverStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 10), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorHoldoverStatusSeverityCode.setStatus('current')
timingGeneratorActiveStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("statusTrapEnable", 2))).clone('statusTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorActiveStatusSeverityCode.setStatus('current')
timingGeneratorQualityEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorQualityEnable.setStatus('current')
timingSinkLosAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 13), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingSinkLosAlarmSeverityCode.setStatus('current')
timingSinkDriftAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 14), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingSinkDriftAlarmSeverityCode.setStatus('current')
timingSinkActiveStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("statusTrapEnable", 2))).clone('statusTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingSinkActiveStatusSeverityCode.setStatus('current')
timingSinkSelectorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16), )
if mibBuilder.loadTexts: timingSinkSelectorTable.setStatus('current')
timingSinkSelectorRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1), ).setIndexNames((0, "SIAE-SYNC-MIB", "timingSinkGenId"), (0, "SIAE-SYNC-MIB", "timingSinkId"), (0, "SIAE-SYNC-MIB", "timingSinkType"), (0, "SIAE-SYNC-MIB", "timingSinkSelectorId"))
if mibBuilder.loadTexts: timingSinkSelectorRecord.setStatus('current')
timingSinkSelectorId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkSelectorId.setStatus('current')
timingSinkSelectorLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkSelectorLabel.setStatus('current')
esmcTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17), )
if mibBuilder.loadTexts: esmcTable.setStatus('current')
esmcRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: esmcRecord.setStatus('current')
esmcSsmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: esmcSsmEnable.setStatus('current')
esmcQlRx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcQlRx.setStatus('current')
esmcQlTx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcQlTx.setStatus('current')
esmcPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcPktsRx.setStatus('current')
esmcPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcPktsTx.setStatus('current')
esmcPktsRxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcPktsRxDropped.setStatus('current')
esmcPktsRxErrored = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcPktsRxErrored.setStatus('current')
esmc1000BaseTRole = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("slave", 1), ("master", 2), ("auto", 3))).clone('auto')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: esmc1000BaseTRole.setStatus('current')
esmcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: esmcRowStatus.setStatus('current')
mibBuilder.exportSymbols("SIAE-SYNC-MIB", timingGeneratorT4PreferredSource=timingGeneratorT4PreferredSource, esmcTable=esmcTable, PYSNMP_MODULE_ID=sync, timingGeneratorHoldOffTime=timingGeneratorHoldOffTime, timingGeneratorSinkLosSet=timingGeneratorSinkLosSet, timingGeneratorActiveStatus=timingGeneratorActiveStatus, timingGeneratorT4SquelchAlarm=timingGeneratorT4SquelchAlarm, timingGeneratorT4CurrentQuality=timingGeneratorT4CurrentQuality, timingGeneratorMaintRecord=timingGeneratorMaintRecord, timingGeneratorRowStatus=timingGeneratorRowStatus, timingSinkPriority=timingSinkPriority, timingSinkSelectorRecord=timingSinkSelectorRecord, esmcRowStatus=esmcRowStatus, timingSinkOverwriteRxQuality=timingSinkOverwriteRxQuality, timingGeneratorForcedSwitch=timingGeneratorForcedSwitch, timingGeneratorActiveStatusSeverityCode=timingGeneratorActiveStatusSeverityCode, timingGeneratorSinkLosReset=timingGeneratorSinkLosReset, timingGeneratorWtrTime=timingGeneratorWtrTime, timingGeneratorT0SquelchAlarm=timingGeneratorT0SquelchAlarm, timingSinkDriftAlarm=timingSinkDriftAlarm, timingSinkE1Sabit=timingSinkE1Sabit, timingGeneratorT4SquelchAlarmSeverityCode=timingGeneratorT4SquelchAlarmSeverityCode, timingSinkGenId=timingSinkGenId, esmcPktsRxDropped=esmcPktsRxDropped, esmcQlTx=esmcQlTx, timingGeneratorT4Squelch=timingGeneratorT4Squelch, timingSinkIfIndex=timingSinkIfIndex, timingGeneratorT0CurrentQuality=timingGeneratorT0CurrentQuality, timingSinkLabel=timingSinkLabel, timingSinkSelectorId=timingSinkSelectorId, timingSinkLosAlarm=timingSinkLosAlarm, timingGeneratorT0SquelchAlarmSeverityCode=timingGeneratorT0SquelchAlarmSeverityCode, timingGeneratorTable=timingGeneratorTable, timingGeneratorStatusControl=timingGeneratorStatusControl, timingSinkId=timingSinkId, timingSinkSelector=timingSinkSelector, timingGeneratorQualityEnable=timingGeneratorQualityEnable, timingSinkSelectorLabel=timingSinkSelectorLabel, timingSinkType=timingSinkType, timingSinkSelectorTable=timingSinkSelectorTable, esmcQlRx=esmcQlRx, esmcPktsTx=esmcPktsTx, timingGeneratorManualSwitch=timingGeneratorManualSwitch, sync=sync, timingGeneratorId=timingGeneratorId, syncMibVersion=syncMibVersion, timingSinkOverwriteTxQuality=timingSinkOverwriteTxQuality, timingGeneratorFreeRunningStatus=timingGeneratorFreeRunningStatus, timingGeneratorHoldoverStatusSeverityCode=timingGeneratorHoldoverStatusSeverityCode, esmc1000BaseTRole=esmc1000BaseTRole, timingGeneratorHoldoverStatus=timingGeneratorHoldoverStatus, timingGeneratorRecord=timingGeneratorRecord, esmcSsmEnable=esmcSsmEnable, timingSinkCurrentQuality=timingSinkCurrentQuality, timingGeneratorT4MinimumQuality=timingGeneratorT4MinimumQuality, timingSinkActiveStatus=timingSinkActiveStatus, timingSinkRowStatus=timingSinkRowStatus, timingGeneratorT0ForcedSource=timingGeneratorT0ForcedSource, timingSinkEthPortRole=timingSinkEthPortRole, timingGeneratorFreeRunningStatusSeverityCode=timingGeneratorFreeRunningStatusSeverityCode, timingSinkRecord=timingSinkRecord, timingGeneratorT4ForcedSource=timingGeneratorT4ForcedSource, timingSinkLosAlarmSeverityCode=timingSinkLosAlarmSeverityCode, timingGeneratorT4vsT0=timingGeneratorT4vsT0, esmcPktsRxErrored=esmcPktsRxErrored, timingGeneratorMaintTable=timingGeneratorMaintTable, timingSinkTable=timingSinkTable, timingSinkSentQuality=timingSinkSentQuality, timingSinkActiveStatusSeverityCode=timingSinkActiveStatusSeverityCode, timingSinkDriftAlarmSeverityCode=timingSinkDriftAlarmSeverityCode, esmcRecord=esmcRecord, esmcPktsRx=esmcPktsRx, timingGeneratorWtrClearSource=timingGeneratorWtrClearSource, timingGeneratorT0PreferredSource=timingGeneratorT0PreferredSource)
