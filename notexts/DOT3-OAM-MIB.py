#
# PySNMP MIB module DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DOT3-OAM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TruthValue, TimeStamp, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TimeStamp", "TextualConvention", "MacAddress")
dot3OamMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 158))
dot3OamMIB.setRevisions(('2007-06-14 00:00',))
if mibBuilder.loadTexts: dot3OamMIB.setLastUpdated('200706140000Z')
if mibBuilder.loadTexts: dot3OamMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
dot3OamNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 158, 0))
dot3OamObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 158, 1))
dot3OamConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 158, 2))
class EightOTwoOui(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

dot3OamTable = MibTable((1, 3, 6, 1, 2, 1, 158, 1, 1), )
if mibBuilder.loadTexts: dot3OamTable.setStatus('current')
dot3OamEntry = MibTableRow((1, 3, 6, 1, 2, 1, 158, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3OamEntry.setStatus('current')
dot3OamAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamAdminState.setStatus('current')
dot3OamOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("disabled", 1), ("linkFault", 2), ("passiveWait", 3), ("activeSendLocal", 4), ("sendLocalAndRemote", 5), ("sendLocalAndRemoteOk", 6), ("oamPeeringLocallyRejected", 7), ("oamPeeringRemotelyRejected", 8), ("operational", 9), ("nonOperHalfDuplex", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamOperStatus.setStatus('current')
dot3OamMode = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passive", 1), ("active", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamMode.setStatus('current')
dot3OamMaxOamPduSize = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(64, 1518))).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamMaxOamPduSize.setStatus('current')
dot3OamConfigRevision = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamConfigRevision.setStatus('current')
dot3OamFunctionsSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 1, 1, 6), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamFunctionsSupported.setStatus('current')
dot3OamPeerTable = MibTable((1, 3, 6, 1, 2, 1, 158, 1, 2), )
if mibBuilder.loadTexts: dot3OamPeerTable.setStatus('current')
dot3OamPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 158, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3OamPeerEntry.setStatus('current')
dot3OamPeerMacAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamPeerMacAddress.setStatus('current')
dot3OamPeerVendorOui = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 2, 1, 2), EightOTwoOui()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamPeerVendorOui.setStatus('current')
dot3OamPeerVendorInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamPeerVendorInfo.setStatus('current')
dot3OamPeerMode = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("passive", 1), ("active", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamPeerMode.setStatus('current')
dot3OamPeerMaxOamPduSize = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(64, 1518), ))).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamPeerMaxOamPduSize.setStatus('current')
dot3OamPeerConfigRevision = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamPeerConfigRevision.setStatus('current')
dot3OamPeerFunctionsSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 2, 1, 7), Bits().clone(namedValues=NamedValues(("unidirectionalSupport", 0), ("loopbackSupport", 1), ("eventSupport", 2), ("variableSupport", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamPeerFunctionsSupported.setStatus('current')
dot3OamLoopbackTable = MibTable((1, 3, 6, 1, 2, 1, 158, 1, 3), )
if mibBuilder.loadTexts: dot3OamLoopbackTable.setStatus('current')
dot3OamLoopbackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 158, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3OamLoopbackEntry.setStatus('current')
dot3OamLoopbackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noLoopback", 1), ("initiatingLoopback", 2), ("remoteLoopback", 3), ("terminatingLoopback", 4), ("localLoopback", 5), ("unknown", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamLoopbackStatus.setStatus('current')
dot3OamLoopbackIgnoreRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("process", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamLoopbackIgnoreRx.setStatus('current')
dot3OamStatsTable = MibTable((1, 3, 6, 1, 2, 1, 158, 1, 4), )
if mibBuilder.loadTexts: dot3OamStatsTable.setStatus('current')
dot3OamStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 158, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3OamStatsEntry.setStatus('current')
dot3OamInformationTx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 1), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamInformationTx.setStatus('current')
dot3OamInformationRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 2), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamInformationRx.setStatus('current')
dot3OamUniqueEventNotificationTx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 3), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamUniqueEventNotificationTx.setStatus('current')
dot3OamUniqueEventNotificationRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 4), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamUniqueEventNotificationRx.setStatus('current')
dot3OamDuplicateEventNotificationTx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 5), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamDuplicateEventNotificationTx.setStatus('current')
dot3OamDuplicateEventNotificationRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 6), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamDuplicateEventNotificationRx.setStatus('current')
dot3OamLoopbackControlTx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 7), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamLoopbackControlTx.setStatus('current')
dot3OamLoopbackControlRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 8), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamLoopbackControlRx.setStatus('current')
dot3OamVariableRequestTx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 9), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamVariableRequestTx.setStatus('current')
dot3OamVariableRequestRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 10), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamVariableRequestRx.setStatus('current')
dot3OamVariableResponseTx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 11), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamVariableResponseTx.setStatus('current')
dot3OamVariableResponseRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 12), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamVariableResponseRx.setStatus('current')
dot3OamOrgSpecificTx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 13), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamOrgSpecificTx.setStatus('current')
dot3OamOrgSpecificRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 14), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamOrgSpecificRx.setStatus('current')
dot3OamUnsupportedCodesTx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 15), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamUnsupportedCodesTx.setStatus('current')
dot3OamUnsupportedCodesRx = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 16), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamUnsupportedCodesRx.setStatus('current')
dot3OamFramesLostDueToOam = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 4, 1, 17), Counter32()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamFramesLostDueToOam.setStatus('current')
dot3OamEventConfigTable = MibTable((1, 3, 6, 1, 2, 1, 158, 1, 5), )
if mibBuilder.loadTexts: dot3OamEventConfigTable.setStatus('current')
dot3OamEventConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 158, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3OamEventConfigEntry.setStatus('current')
dot3OamErrSymPeriodWindowHi = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 1), Unsigned32()).setUnits('2^32 symbols').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrSymPeriodWindowHi.setStatus('current')
dot3OamErrSymPeriodWindowLo = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 2), Unsigned32()).setUnits('symbols').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrSymPeriodWindowLo.setStatus('current')
dot3OamErrSymPeriodThresholdHi = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 3), Unsigned32()).setUnits('2^32 symbols').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrSymPeriodThresholdHi.setStatus('current')
dot3OamErrSymPeriodThresholdLo = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 4), Unsigned32()).setUnits('symbols').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrSymPeriodThresholdLo.setStatus('current')
dot3OamErrSymPeriodEvNotifEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrSymPeriodEvNotifEnable.setStatus('current')
dot3OamErrFramePeriodWindow = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 6), Unsigned32()).setUnits('frames').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFramePeriodWindow.setStatus('current')
dot3OamErrFramePeriodThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 7), Unsigned32()).setUnits('frames').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFramePeriodThreshold.setStatus('current')
dot3OamErrFramePeriodEvNotifEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFramePeriodEvNotifEnable.setStatus('current')
dot3OamErrFrameWindow = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 9), Unsigned32().clone(10)).setUnits('tenths of a second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFrameWindow.setStatus('current')
dot3OamErrFrameThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 10), Unsigned32().clone(1)).setUnits('frames').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFrameThreshold.setStatus('current')
dot3OamErrFrameEvNotifEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 11), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFrameEvNotifEnable.setStatus('current')
dot3OamErrFrameSecsSummaryWindow = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 9000)).clone(100)).setUnits('tenths of a second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFrameSecsSummaryWindow.setStatus('current')
dot3OamErrFrameSecsSummaryThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 900)).clone(1)).setUnits('errored frame seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFrameSecsSummaryThreshold.setStatus('current')
dot3OamErrFrameSecsEvNotifEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 14), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamErrFrameSecsEvNotifEnable.setStatus('current')
dot3OamDyingGaspEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 15), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamDyingGaspEnable.setStatus('current')
dot3OamCriticalEventEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 5, 1, 16), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3OamCriticalEventEnable.setStatus('current')
dot3OamEventLogTable = MibTable((1, 3, 6, 1, 2, 1, 158, 1, 6), )
if mibBuilder.loadTexts: dot3OamEventLogTable.setStatus('current')
dot3OamEventLogEntry = MibTableRow((1, 3, 6, 1, 2, 1, 158, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOT3-OAM-MIB", "dot3OamEventLogIndex"))
if mibBuilder.loadTexts: dot3OamEventLogEntry.setStatus('current')
dot3OamEventLogIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot3OamEventLogIndex.setStatus('current')
dot3OamEventLogTimestamp = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogTimestamp.setStatus('current')
dot3OamEventLogOui = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 3), EightOTwoOui()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogOui.setStatus('current')
dot3OamEventLogType = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogType.setStatus('current')
dot3OamEventLogLocation = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogLocation.setStatus('current')
dot3OamEventLogWindowHi = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogWindowHi.setStatus('current')
dot3OamEventLogWindowLo = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogWindowLo.setStatus('current')
dot3OamEventLogThresholdHi = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogThresholdHi.setStatus('current')
dot3OamEventLogThresholdLo = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogThresholdLo.setStatus('current')
dot3OamEventLogValue = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 10), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogValue.setStatus('current')
dot3OamEventLogRunningTotal = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 11), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogRunningTotal.setStatus('current')
dot3OamEventLogEventTotal = MibTableColumn((1, 3, 6, 1, 2, 1, 158, 1, 6, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OamEventLogEventTotal.setStatus('current')
dot3OamThresholdEvent = NotificationType((1, 3, 6, 1, 2, 1, 158, 0, 1)).setObjects(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"), ("DOT3-OAM-MIB", "dot3OamEventLogOui"), ("DOT3-OAM-MIB", "dot3OamEventLogType"), ("DOT3-OAM-MIB", "dot3OamEventLogLocation"), ("DOT3-OAM-MIB", "dot3OamEventLogWindowHi"), ("DOT3-OAM-MIB", "dot3OamEventLogWindowLo"), ("DOT3-OAM-MIB", "dot3OamEventLogThresholdHi"), ("DOT3-OAM-MIB", "dot3OamEventLogThresholdLo"), ("DOT3-OAM-MIB", "dot3OamEventLogValue"), ("DOT3-OAM-MIB", "dot3OamEventLogRunningTotal"), ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
if mibBuilder.loadTexts: dot3OamThresholdEvent.setStatus('current')
dot3OamNonThresholdEvent = NotificationType((1, 3, 6, 1, 2, 1, 158, 0, 2)).setObjects(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"), ("DOT3-OAM-MIB", "dot3OamEventLogOui"), ("DOT3-OAM-MIB", "dot3OamEventLogType"), ("DOT3-OAM-MIB", "dot3OamEventLogLocation"), ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
if mibBuilder.loadTexts: dot3OamNonThresholdEvent.setStatus('current')
dot3OamGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 158, 2, 1))
dot3OamCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 158, 2, 2))
dot3OamCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 158, 2, 2, 1)).setObjects(("DOT3-OAM-MIB", "dot3OamControlGroup"), ("DOT3-OAM-MIB", "dot3OamPeerGroup"), ("DOT3-OAM-MIB", "dot3OamStatsBaseGroup"), ("DOT3-OAM-MIB", "dot3OamLoopbackGroup"), ("DOT3-OAM-MIB", "dot3OamErrSymbolPeriodEventGroup"), ("DOT3-OAM-MIB", "dot3OamErrFramePeriodEventGroup"), ("DOT3-OAM-MIB", "dot3OamErrFrameEventGroup"), ("DOT3-OAM-MIB", "dot3OamErrFrameSecsSummaryEventGroup"), ("DOT3-OAM-MIB", "dot3OamFlagEventGroup"), ("DOT3-OAM-MIB", "dot3OamEventLogGroup"), ("DOT3-OAM-MIB", "dot3OamNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamCompliance = dot3OamCompliance.setStatus('current')
dot3OamControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 1)).setObjects(("DOT3-OAM-MIB", "dot3OamAdminState"), ("DOT3-OAM-MIB", "dot3OamOperStatus"), ("DOT3-OAM-MIB", "dot3OamMode"), ("DOT3-OAM-MIB", "dot3OamMaxOamPduSize"), ("DOT3-OAM-MIB", "dot3OamConfigRevision"), ("DOT3-OAM-MIB", "dot3OamFunctionsSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamControlGroup = dot3OamControlGroup.setStatus('current')
dot3OamPeerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 2)).setObjects(("DOT3-OAM-MIB", "dot3OamPeerMacAddress"), ("DOT3-OAM-MIB", "dot3OamPeerVendorOui"), ("DOT3-OAM-MIB", "dot3OamPeerVendorInfo"), ("DOT3-OAM-MIB", "dot3OamPeerMode"), ("DOT3-OAM-MIB", "dot3OamPeerFunctionsSupported"), ("DOT3-OAM-MIB", "dot3OamPeerMaxOamPduSize"), ("DOT3-OAM-MIB", "dot3OamPeerConfigRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamPeerGroup = dot3OamPeerGroup.setStatus('current')
dot3OamStatsBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 3)).setObjects(("DOT3-OAM-MIB", "dot3OamInformationTx"), ("DOT3-OAM-MIB", "dot3OamInformationRx"), ("DOT3-OAM-MIB", "dot3OamUniqueEventNotificationTx"), ("DOT3-OAM-MIB", "dot3OamUniqueEventNotificationRx"), ("DOT3-OAM-MIB", "dot3OamDuplicateEventNotificationTx"), ("DOT3-OAM-MIB", "dot3OamDuplicateEventNotificationRx"), ("DOT3-OAM-MIB", "dot3OamLoopbackControlTx"), ("DOT3-OAM-MIB", "dot3OamLoopbackControlRx"), ("DOT3-OAM-MIB", "dot3OamVariableRequestTx"), ("DOT3-OAM-MIB", "dot3OamVariableRequestRx"), ("DOT3-OAM-MIB", "dot3OamVariableResponseTx"), ("DOT3-OAM-MIB", "dot3OamVariableResponseRx"), ("DOT3-OAM-MIB", "dot3OamOrgSpecificTx"), ("DOT3-OAM-MIB", "dot3OamOrgSpecificRx"), ("DOT3-OAM-MIB", "dot3OamUnsupportedCodesTx"), ("DOT3-OAM-MIB", "dot3OamUnsupportedCodesRx"), ("DOT3-OAM-MIB", "dot3OamFramesLostDueToOam"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamStatsBaseGroup = dot3OamStatsBaseGroup.setStatus('current')
dot3OamLoopbackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 4)).setObjects(("DOT3-OAM-MIB", "dot3OamLoopbackStatus"), ("DOT3-OAM-MIB", "dot3OamLoopbackIgnoreRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamLoopbackGroup = dot3OamLoopbackGroup.setStatus('current')
dot3OamErrSymbolPeriodEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 5)).setObjects(("DOT3-OAM-MIB", "dot3OamErrSymPeriodWindowHi"), ("DOT3-OAM-MIB", "dot3OamErrSymPeriodWindowLo"), ("DOT3-OAM-MIB", "dot3OamErrSymPeriodThresholdHi"), ("DOT3-OAM-MIB", "dot3OamErrSymPeriodThresholdLo"), ("DOT3-OAM-MIB", "dot3OamErrSymPeriodEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamErrSymbolPeriodEventGroup = dot3OamErrSymbolPeriodEventGroup.setStatus('current')
dot3OamErrFramePeriodEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 6)).setObjects(("DOT3-OAM-MIB", "dot3OamErrFramePeriodWindow"), ("DOT3-OAM-MIB", "dot3OamErrFramePeriodThreshold"), ("DOT3-OAM-MIB", "dot3OamErrFramePeriodEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamErrFramePeriodEventGroup = dot3OamErrFramePeriodEventGroup.setStatus('current')
dot3OamErrFrameEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 7)).setObjects(("DOT3-OAM-MIB", "dot3OamErrFrameWindow"), ("DOT3-OAM-MIB", "dot3OamErrFrameThreshold"), ("DOT3-OAM-MIB", "dot3OamErrFrameEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamErrFrameEventGroup = dot3OamErrFrameEventGroup.setStatus('current')
dot3OamErrFrameSecsSummaryEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 8)).setObjects(("DOT3-OAM-MIB", "dot3OamErrFrameSecsSummaryWindow"), ("DOT3-OAM-MIB", "dot3OamErrFrameSecsSummaryThreshold"), ("DOT3-OAM-MIB", "dot3OamErrFrameSecsEvNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamErrFrameSecsSummaryEventGroup = dot3OamErrFrameSecsSummaryEventGroup.setStatus('current')
dot3OamFlagEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 9)).setObjects(("DOT3-OAM-MIB", "dot3OamDyingGaspEnable"), ("DOT3-OAM-MIB", "dot3OamCriticalEventEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamFlagEventGroup = dot3OamFlagEventGroup.setStatus('current')
dot3OamEventLogGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 10)).setObjects(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"), ("DOT3-OAM-MIB", "dot3OamEventLogOui"), ("DOT3-OAM-MIB", "dot3OamEventLogType"), ("DOT3-OAM-MIB", "dot3OamEventLogLocation"), ("DOT3-OAM-MIB", "dot3OamEventLogWindowHi"), ("DOT3-OAM-MIB", "dot3OamEventLogWindowLo"), ("DOT3-OAM-MIB", "dot3OamEventLogThresholdHi"), ("DOT3-OAM-MIB", "dot3OamEventLogThresholdLo"), ("DOT3-OAM-MIB", "dot3OamEventLogValue"), ("DOT3-OAM-MIB", "dot3OamEventLogRunningTotal"), ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamEventLogGroup = dot3OamEventLogGroup.setStatus('current')
dot3OamNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 158, 2, 1, 11)).setObjects(("DOT3-OAM-MIB", "dot3OamThresholdEvent"), ("DOT3-OAM-MIB", "dot3OamNonThresholdEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OamNotificationGroup = dot3OamNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DOT3-OAM-MIB", dot3OamThresholdEvent=dot3OamThresholdEvent, dot3OamControlGroup=dot3OamControlGroup, dot3OamEventLogLocation=dot3OamEventLogLocation, dot3OamFramesLostDueToOam=dot3OamFramesLostDueToOam, dot3OamNonThresholdEvent=dot3OamNonThresholdEvent, dot3OamConformance=dot3OamConformance, dot3OamConfigRevision=dot3OamConfigRevision, dot3OamLoopbackIgnoreRx=dot3OamLoopbackIgnoreRx, dot3OamErrSymbolPeriodEventGroup=dot3OamErrSymbolPeriodEventGroup, dot3OamErrFrameWindow=dot3OamErrFrameWindow, dot3OamPeerFunctionsSupported=dot3OamPeerFunctionsSupported, dot3OamPeerTable=dot3OamPeerTable, dot3OamVariableRequestTx=dot3OamVariableRequestTx, dot3OamOperStatus=dot3OamOperStatus, dot3OamEventLogValue=dot3OamEventLogValue, dot3OamCompliance=dot3OamCompliance, dot3OamLoopbackControlTx=dot3OamLoopbackControlTx, dot3OamErrFrameEventGroup=dot3OamErrFrameEventGroup, dot3OamLoopbackControlRx=dot3OamLoopbackControlRx, dot3OamEventLogOui=dot3OamEventLogOui, dot3OamErrFrameSecsSummaryEventGroup=dot3OamErrFrameSecsSummaryEventGroup, dot3OamPeerVendorOui=dot3OamPeerVendorOui, dot3OamInformationTx=dot3OamInformationTx, dot3OamMode=dot3OamMode, dot3OamNotificationGroup=dot3OamNotificationGroup, dot3OamNotifications=dot3OamNotifications, dot3OamEventLogEntry=dot3OamEventLogEntry, dot3OamAdminState=dot3OamAdminState, dot3OamFunctionsSupported=dot3OamFunctionsSupported, dot3OamStatsTable=dot3OamStatsTable, dot3OamEventLogIndex=dot3OamEventLogIndex, dot3OamEventLogRunningTotal=dot3OamEventLogRunningTotal, dot3OamUniqueEventNotificationTx=dot3OamUniqueEventNotificationTx, dot3OamErrFrameSecsSummaryThreshold=dot3OamErrFrameSecsSummaryThreshold, dot3OamCompliances=dot3OamCompliances, dot3OamMIB=dot3OamMIB, dot3OamOrgSpecificRx=dot3OamOrgSpecificRx, dot3OamPeerEntry=dot3OamPeerEntry, dot3OamDuplicateEventNotificationRx=dot3OamDuplicateEventNotificationRx, dot3OamErrSymPeriodWindowLo=dot3OamErrSymPeriodWindowLo, dot3OamLoopbackTable=dot3OamLoopbackTable, dot3OamErrFramePeriodThreshold=dot3OamErrFramePeriodThreshold, dot3OamPeerMacAddress=dot3OamPeerMacAddress, dot3OamEventLogThresholdLo=dot3OamEventLogThresholdLo, dot3OamErrFrameSecsSummaryWindow=dot3OamErrFrameSecsSummaryWindow, dot3OamLoopbackGroup=dot3OamLoopbackGroup, dot3OamEventLogGroup=dot3OamEventLogGroup, dot3OamDyingGaspEnable=dot3OamDyingGaspEnable, dot3OamVariableRequestRx=dot3OamVariableRequestRx, dot3OamErrSymPeriodThresholdLo=dot3OamErrSymPeriodThresholdLo, dot3OamFlagEventGroup=dot3OamFlagEventGroup, dot3OamEventLogThresholdHi=dot3OamEventLogThresholdHi, dot3OamUniqueEventNotificationRx=dot3OamUniqueEventNotificationRx, dot3OamPeerMode=dot3OamPeerMode, dot3OamVariableResponseRx=dot3OamVariableResponseRx, dot3OamErrFramePeriodEvNotifEnable=dot3OamErrFramePeriodEvNotifEnable, dot3OamErrFramePeriodWindow=dot3OamErrFramePeriodWindow, dot3OamPeerVendorInfo=dot3OamPeerVendorInfo, dot3OamLoopbackEntry=dot3OamLoopbackEntry, dot3OamEntry=dot3OamEntry, dot3OamEventLogTable=dot3OamEventLogTable, dot3OamGroups=dot3OamGroups, EightOTwoOui=EightOTwoOui, dot3OamErrSymPeriodWindowHi=dot3OamErrSymPeriodWindowHi, dot3OamOrgSpecificTx=dot3OamOrgSpecificTx, dot3OamPeerMaxOamPduSize=dot3OamPeerMaxOamPduSize, dot3OamPeerConfigRevision=dot3OamPeerConfigRevision, PYSNMP_MODULE_ID=dot3OamMIB, dot3OamErrSymPeriodEvNotifEnable=dot3OamErrSymPeriodEvNotifEnable, dot3OamMaxOamPduSize=dot3OamMaxOamPduSize, dot3OamErrFrameEvNotifEnable=dot3OamErrFrameEvNotifEnable, dot3OamErrFramePeriodEventGroup=dot3OamErrFramePeriodEventGroup, dot3OamEventLogWindowLo=dot3OamEventLogWindowLo, dot3OamStatsBaseGroup=dot3OamStatsBaseGroup, dot3OamTable=dot3OamTable, dot3OamUnsupportedCodesRx=dot3OamUnsupportedCodesRx, dot3OamLoopbackStatus=dot3OamLoopbackStatus, dot3OamErrSymPeriodThresholdHi=dot3OamErrSymPeriodThresholdHi, dot3OamEventLogType=dot3OamEventLogType, dot3OamUnsupportedCodesTx=dot3OamUnsupportedCodesTx, dot3OamEventLogTimestamp=dot3OamEventLogTimestamp, dot3OamVariableResponseTx=dot3OamVariableResponseTx, dot3OamInformationRx=dot3OamInformationRx, dot3OamCriticalEventEnable=dot3OamCriticalEventEnable, dot3OamStatsEntry=dot3OamStatsEntry, dot3OamEventConfigEntry=dot3OamEventConfigEntry, dot3OamPeerGroup=dot3OamPeerGroup, dot3OamObjects=dot3OamObjects, dot3OamEventLogEventTotal=dot3OamEventLogEventTotal, dot3OamEventLogWindowHi=dot3OamEventLogWindowHi, dot3OamDuplicateEventNotificationTx=dot3OamDuplicateEventNotificationTx, dot3OamErrFrameThreshold=dot3OamErrFrameThreshold, dot3OamErrFrameSecsEvNotifEnable=dot3OamErrFrameSecsEvNotifEnable, dot3OamEventConfigTable=dot3OamEventConfigTable)
