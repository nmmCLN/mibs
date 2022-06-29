#
# PySNMP MIB module CTRON-SFPS-EVENTLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-EVENTLOG-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:56 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
sfpsEventLogGenConfig, sfpsTrapAPI, sfpsEventLogClientConfig, sfpsEventLogStats, sfpsEventLogClientConfigAPI, sfpsTrapTable, sfpsFragStats = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsEventLogGenConfig", "sfpsTrapAPI", "sfpsEventLogClientConfig", "sfpsEventLogStats", "sfpsEventLogClientConfigAPI", "sfpsTrapTable", "sfpsFragStats")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SfpsSwitchInstance(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class HexInteger(Integer32):
    pass

sfpsEventLogStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1), )
if mibBuilder.loadTexts: sfpsEventLogStatsTable.setStatus('mandatory')
sfpsEventLogStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogStatsSwInst"), (0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogWindowStart"))
if mibBuilder.loadTexts: sfpsEventLogStatsEntry.setStatus('mandatory')
sfpsEventLogStatsSwInst = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 1), SfpsSwitchInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogStatsSwInst.setStatus('mandatory')
sfpsEventLogWindowStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogWindowStart.setStatus('mandatory')
sfpsEventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogIndex.setStatus('mandatory')
sfpsEventLogClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogClientName.setStatus('mandatory')
sfpsEventLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogLevel.setStatus('mandatory')
sfpsEventLogMessageString = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogMessageString.setStatus('mandatory')
sfpsEventLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogTime.setStatus('mandatory')
sfpsEventLogCallTag = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 8), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogCallTag.setStatus('mandatory')
sfpsEventLogInfo1 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 9), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogInfo1.setStatus('mandatory')
sfpsEventLogInfo2 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 10), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogInfo2.setStatus('mandatory')
sfpsEventLogGenConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1), )
if mibBuilder.loadTexts: sfpsEventLogGenConfigTable.setStatus('mandatory')
sfpsEventLogGenConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1), ).setIndexNames((0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogGenConfigSwInst"))
if mibBuilder.loadTexts: sfpsEventLogGenConfigEntry.setStatus('mandatory')
sfpsEventLogGenConfigSwInst = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 1), SfpsSwitchInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogGenConfigSwInst.setStatus('mandatory')
sfpsEventLogGenConfigWindowStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigWindowStart.setStatus('mandatory')
sfpsEventLogGenConfigLoggingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogGenConfigLoggingIndex.setStatus('mandatory')
sfpsEventLogGenConfigMessageFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigMessageFilter.setStatus('mandatory')
sfpsEventLogGenConfigCallTagFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 5), HexInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigCallTagFilter.setStatus('mandatory')
sfpsEventLogGenConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("reset", 4), ("continue", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigAdminStatus.setStatus('mandatory')
sfpsEventLogGenConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("pending-disable", 4), ("pending-enable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogGenConfigOperStatus.setStatus('mandatory')
sfpsEventLogGenConfigOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogGenConfigOperTime.setStatus('mandatory')
sfpsEventLogGenConfigAutoFreeze = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigAutoFreeze.setStatus('mandatory')
sfpsEventLogGenConfigDisplayWrapDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigDisplayWrapDetect.setStatus('mandatory')
sfpsEventLogGenConfigAdvertiseAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigAdvertiseAddr.setStatus('mandatory')
sfpsEventLogClientConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1), )
if mibBuilder.loadTexts: sfpsEventLogClientConfigTable.setStatus('mandatory')
sfpsEventLogClientConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1), ).setIndexNames((0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogClientConfigId"))
if mibBuilder.loadTexts: sfpsEventLogClientConfigEntry.setStatus('mandatory')
sfpsEventLogClientConfigId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogClientConfigId.setStatus('mandatory')
sfpsEventLogClientConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogClientConfigName.setStatus('mandatory')
sfpsEventLogClientLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientLogStatus.setStatus('mandatory')
sfpsEventLogClientDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientDisplayStatus.setStatus('mandatory')
sfpsEventLogClientFreezeLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientFreezeLogStatus.setStatus('mandatory')
sfpsEventLogClientFreezeDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientFreezeDisplayStatus.setStatus('mandatory')
sfpsEventLogClientErrorLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientErrorLogStatus.setStatus('mandatory')
sfpsEventLogClientErrorDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientErrorDisplayStatus.setStatus('mandatory')
sfpsEventLogClientCriticalLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientCriticalLogStatus.setStatus('mandatory')
sfpsEventLogClientCriticalDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientCriticalDisplayStatus.setStatus('mandatory')
sfpsEventLogClientInfoLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientInfoLogStatus.setStatus('mandatory')
sfpsEventLogClientInfoDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientInfoDisplayStatus.setStatus('mandatory')
sfpsEventLogClientDebugLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientDebugLogStatus.setStatus('mandatory')
sfpsEventLogClientDebugDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientDebugDisplayStatus.setStatus('mandatory')
sfpsEventLogClientConfigAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("freezeLog", 1), ("errorLog", 2), ("criticalLog", 3), ("infoLog", 4), ("debugLog", 5), ("allLogLevels", 6), ("allClients", 7), ("masterLog", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIVerb.setStatus('mandatory')
sfpsEventLogClientConfigAPIAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIAdminStatus.setStatus('mandatory')
sfpsEventLogClientConfigAPIClientName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIClientName.setStatus('mandatory')
sfpsEventLogClientConfigAPIClientID = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIClientID.setStatus('mandatory')
sfpsEventLogClientConfigAPILogDisplay = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("logAndDisplay", 2), ("logOnly", 3), ("displayOnly", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPILogDisplay.setStatus('mandatory')
sfpsFragStatsTotalFrags = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsTotalFrags.setStatus('mandatory')
sfpsFragStatsNumLookupFail = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsNumLookupFail.setStatus('mandatory')
sfpsFragStatsAvgCompares = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsAvgCompares.setStatus('mandatory')
sfpsFragStatsNumNodes = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsNumNodes.setStatus('mandatory')
sfpsFragStatsNumUsed = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsNumUsed.setStatus('mandatory')
sfpsFragStatsMaxNumUsed = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsMaxNumUsed.setStatus('mandatory')
sfpsFragStatsNumStolen = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsNumStolen.setStatus('mandatory')
sfpsTrapAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3), ("resetTrapStats", 4), ("resetAllStats", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsTrapAPIVerb.setStatus('mandatory')
sfpsTrapAPITrapId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410))).clone(namedValues=NamedValues(("newUser", 1400), ("violation", 1401), ("srcBlock", 1402), ("dstBlock", 1403), ("portToStandby", 1404), ("portFromStandby", 1405), ("ageCnt", 1406), ("changeCount", 1407), ("foundNeighbor", 1408), ("lostNeighbor", 1409), ("agentIP", 1410)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsTrapAPITrapId.setStatus('mandatory')
sfpsTrapAPITotalSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapAPITotalSent.setStatus('mandatory')
sfpsTrapTableTrapId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422))).clone(namedValues=NamedValues(("newUser", 1400), ("violation", 1401), ("srcBlock", 1402), ("dstBlock", 1403), ("portToStandby", 1404), ("portFromStandby", 1405), ("ageCnt", 1406), ("changeCount", 1407), ("foundNeighbor", 1408), ("lostNeighbor", 1409), ("agentIP", 1410), ("noSrcVlans", 1411), ("noDestVlans", 1412), ("noSrcVlansEnabled", 1413), ("noDestVlansEnabled", 1414), ("noCommonSecureVlan", 1415), ("incVlanUserCount", 1416), ("decVlanUserCount", 1417), ("vrrpPrimaryResign", 1418), ("vrrpPrimaryAged", 1419), ("vrrpSecondaryUp", 1420), ("hsrpPrimaryResign", 1421), ("hsrpSecondaryUp", 1422)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapTableTrapId.setStatus('mandatory')
sfpsTrapTableAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapTableAdminStatus.setStatus('mandatory')
sfpsTrapTableNumSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapTableNumSent.setStatus('mandatory')
sfpsTrapTableLastSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapTableLastSent.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-EVENTLOG-MIB", sfpsFragStatsNumNodes=sfpsFragStatsNumNodes, sfpsTrapAPITrapId=sfpsTrapAPITrapId, sfpsEventLogGenConfigMessageFilter=sfpsEventLogGenConfigMessageFilter, sfpsEventLogClientDebugLogStatus=sfpsEventLogClientDebugLogStatus, sfpsTrapTableLastSent=sfpsTrapTableLastSent, sfpsEventLogClientConfigAPIAdminStatus=sfpsEventLogClientConfigAPIAdminStatus, sfpsEventLogGenConfigCallTagFilter=sfpsEventLogGenConfigCallTagFilter, sfpsFragStatsAvgCompares=sfpsFragStatsAvgCompares, sfpsTrapTableNumSent=sfpsTrapTableNumSent, sfpsEventLogGenConfigEntry=sfpsEventLogGenConfigEntry, sfpsEventLogClientName=sfpsEventLogClientName, sfpsEventLogClientErrorLogStatus=sfpsEventLogClientErrorLogStatus, sfpsEventLogClientDebugDisplayStatus=sfpsEventLogClientDebugDisplayStatus, sfpsEventLogClientConfigAPILogDisplay=sfpsEventLogClientConfigAPILogDisplay, sfpsEventLogClientConfigTable=sfpsEventLogClientConfigTable, sfpsEventLogClientInfoDisplayStatus=sfpsEventLogClientInfoDisplayStatus, sfpsEventLogClientInfoLogStatus=sfpsEventLogClientInfoLogStatus, SfpsSwitchInstance=SfpsSwitchInstance, sfpsEventLogClientConfigAPIClientName=sfpsEventLogClientConfigAPIClientName, sfpsTrapTableAdminStatus=sfpsTrapTableAdminStatus, sfpsEventLogIndex=sfpsEventLogIndex, sfpsEventLogInfo2=sfpsEventLogInfo2, sfpsEventLogClientFreezeDisplayStatus=sfpsEventLogClientFreezeDisplayStatus, sfpsEventLogGenConfigDisplayWrapDetect=sfpsEventLogGenConfigDisplayWrapDetect, sfpsEventLogClientCriticalDisplayStatus=sfpsEventLogClientCriticalDisplayStatus, sfpsEventLogGenConfigAdvertiseAddr=sfpsEventLogGenConfigAdvertiseAddr, HexInteger=HexInteger, sfpsTrapTableTrapId=sfpsTrapTableTrapId, sfpsEventLogClientErrorDisplayStatus=sfpsEventLogClientErrorDisplayStatus, sfpsEventLogClientConfigAPIVerb=sfpsEventLogClientConfigAPIVerb, sfpsEventLogGenConfigTable=sfpsEventLogGenConfigTable, sfpsEventLogStatsTable=sfpsEventLogStatsTable, sfpsEventLogClientFreezeLogStatus=sfpsEventLogClientFreezeLogStatus, sfpsTrapAPITotalSent=sfpsTrapAPITotalSent, sfpsEventLogWindowStart=sfpsEventLogWindowStart, sfpsEventLogLevel=sfpsEventLogLevel, sfpsEventLogClientConfigName=sfpsEventLogClientConfigName, sfpsEventLogInfo1=sfpsEventLogInfo1, sfpsFragStatsMaxNumUsed=sfpsFragStatsMaxNumUsed, sfpsEventLogGenConfigOperStatus=sfpsEventLogGenConfigOperStatus, sfpsFragStatsNumUsed=sfpsFragStatsNumUsed, sfpsEventLogMessageString=sfpsEventLogMessageString, sfpsEventLogGenConfigLoggingIndex=sfpsEventLogGenConfigLoggingIndex, sfpsEventLogClientLogStatus=sfpsEventLogClientLogStatus, sfpsEventLogClientConfigAPIClientID=sfpsEventLogClientConfigAPIClientID, sfpsEventLogStatsEntry=sfpsEventLogStatsEntry, sfpsEventLogGenConfigAutoFreeze=sfpsEventLogGenConfigAutoFreeze, sfpsEventLogClientConfigId=sfpsEventLogClientConfigId, sfpsEventLogClientDisplayStatus=sfpsEventLogClientDisplayStatus, sfpsEventLogClientConfigEntry=sfpsEventLogClientConfigEntry, sfpsFragStatsNumLookupFail=sfpsFragStatsNumLookupFail, sfpsTrapAPIVerb=sfpsTrapAPIVerb, sfpsEventLogClientCriticalLogStatus=sfpsEventLogClientCriticalLogStatus, sfpsEventLogGenConfigSwInst=sfpsEventLogGenConfigSwInst, sfpsEventLogTime=sfpsEventLogTime, sfpsEventLogCallTag=sfpsEventLogCallTag, sfpsEventLogGenConfigAdminStatus=sfpsEventLogGenConfigAdminStatus, sfpsEventLogStatsSwInst=sfpsEventLogStatsSwInst, sfpsEventLogGenConfigOperTime=sfpsEventLogGenConfigOperTime, sfpsEventLogGenConfigWindowStart=sfpsEventLogGenConfigWindowStart, sfpsFragStatsTotalFrags=sfpsFragStatsTotalFrags, sfpsFragStatsNumStolen=sfpsFragStatsNumStolen)
