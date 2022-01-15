#
# PySNMP MIB module CTRON-SFPS-EVENTLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-EVENTLOG-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
sfpsFragStats, sfpsTrapAPI, sfpsEventLogClientConfig, sfpsEventLogGenConfig, sfpsTrapTable, sfpsEventLogStats, sfpsEventLogClientConfigAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsFragStats", "sfpsTrapAPI", "sfpsEventLogClientConfig", "sfpsEventLogGenConfig", "sfpsTrapTable", "sfpsEventLogStats", "sfpsEventLogClientConfigAPI")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "IpAddress", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SfpsSwitchInstance(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class HexInteger(Integer32):
    pass

sfpsEventLogStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1), )
if mibBuilder.loadTexts: sfpsEventLogStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogStatsTable.setDescription('This table contains the event information produced by the\n                Event Log Server object.')
sfpsEventLogStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogStatsSwInst"), (0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogWindowStart"))
if mibBuilder.loadTexts: sfpsEventLogStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogStatsEntry.setDescription('Each entry contains event log data.')
sfpsEventLogStatsSwInst = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 1), SfpsSwitchInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogStatsSwInst.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogStatsSwInst.setDescription('The switch instance of this Event Logger.')
sfpsEventLogWindowStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogWindowStart.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogWindowStart.setDescription('The index into the event log window.')
sfpsEventLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogIndex.setDescription('The absolutue index into the event log window.')
sfpsEventLogClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogClientName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientName.setDescription('The name of the client who logged the event.')
sfpsEventLogLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogLevel.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogLevel.setDescription('The log level of the logged event.')
sfpsEventLogMessageString = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogMessageString.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogMessageString.setDescription('The logged event message.')
sfpsEventLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogTime.setDescription('The time when the event was logged.')
sfpsEventLogCallTag = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 8), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogCallTag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogCallTag.setDescription('The call tag of the logged event (if applicable).')
sfpsEventLogInfo1 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 9), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogInfo1.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogInfo1.setDescription('A generic info field used to display information\n                 related to the logged event.')
sfpsEventLogInfo2 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 3, 1, 1, 10), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogInfo2.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogInfo2.setDescription('A generic info field used to display information\n                 related to the logged event.')
sfpsEventLogGenConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1), )
if mibBuilder.loadTexts: sfpsEventLogGenConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigTable.setDescription('This table contains the general configuration parameters for\n                 the Event Log Server object.')
sfpsEventLogGenConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1), ).setIndexNames((0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogGenConfigSwInst"))
if mibBuilder.loadTexts: sfpsEventLogGenConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigEntry.setDescription('Each entry contains event log configuration parameters.')
sfpsEventLogGenConfigSwInst = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 1), SfpsSwitchInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogGenConfigSwInst.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigSwInst.setDescription('The switch instance of this Event Logger table.')
sfpsEventLogGenConfigWindowStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigWindowStart.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigWindowStart.setDescription('Represents the starting point of the Event Logger Window.')
sfpsEventLogGenConfigLoggingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogGenConfigLoggingIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigLoggingIndex.setDescription('Pointer to the next location where the event logger will log.')
sfpsEventLogGenConfigMessageFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigMessageFilter.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigMessageFilter.setDescription('A string filter which allows only matching messages to be\n                displayed.')
sfpsEventLogGenConfigCallTagFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 5), HexInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigCallTagFilter.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigCallTagFilter.setDescription('A filter which allows only messages with matching call tags\n                to be displayed.')
sfpsEventLogGenConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("reset", 4), ("continue", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigAdminStatus.setDescription('The administrative status of the event log.')
sfpsEventLogGenConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("pending-disable", 4), ("pending-enable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogGenConfigOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigOperStatus.setDescription('The operational status of the event log.')
sfpsEventLogGenConfigOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogGenConfigOperTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigOperTime.setDescription('The amount of time that the event log has been\n                in its current operational state.')
sfpsEventLogGenConfigAutoFreeze = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigAutoFreeze.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigAutoFreeze.setDescription('Allows events with the Freeze log level to\n                automatically disable the operational status of\n                the event log.')
sfpsEventLogGenConfigDisplayWrapDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigDisplayWrapDetect.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigDisplayWrapDetect.setDescription("Allows the event log to not advance past a\n                wrap-point determined by the event log's\n                current logging point.")
sfpsEventLogGenConfigAdvertiseAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 4, 1, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogGenConfigAdvertiseAddr.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogGenConfigAdvertiseAddr.setDescription('The IP address of a remote event logging\n                 mechanism.')
sfpsEventLogClientConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1), )
if mibBuilder.loadTexts: sfpsEventLogClientConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigTable.setDescription('This table contains the client configuration parameters for the\n                 Event Log Server object.')
sfpsEventLogClientConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1), ).setIndexNames((0, "CTRON-SFPS-EVENTLOG-MIB", "sfpsEventLogClientConfigId"))
if mibBuilder.loadTexts: sfpsEventLogClientConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigEntry.setDescription('Each entry contains event log client configuration parameters.')
sfpsEventLogClientConfigId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogClientConfigId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigId.setDescription('Represents the client ID of a client that is logging events.')
sfpsEventLogClientConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsEventLogClientConfigName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigName.setDescription('The name of the event log client.')
sfpsEventLogClientLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientLogStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientLogStatus.setDescription('Represents the logging status for this event log client.')
sfpsEventLogClientDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientDisplayStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientDisplayStatus.setDescription('Represents the display status for this event log client.')
sfpsEventLogClientFreezeLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientFreezeLogStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientFreezeLogStatus.setDescription('Represents the log status for the log level Freeze of this\n                 client.')
sfpsEventLogClientFreezeDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientFreezeDisplayStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientFreezeDisplayStatus.setDescription('Represents the display status for the log level Freeze of this\n                 client.')
sfpsEventLogClientErrorLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientErrorLogStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientErrorLogStatus.setDescription('Represents the log status for the log level Error of this\n                 client.')
sfpsEventLogClientErrorDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientErrorDisplayStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientErrorDisplayStatus.setDescription('Represents the display status for the log level Error of this\n                 client.')
sfpsEventLogClientCriticalLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientCriticalLogStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientCriticalLogStatus.setDescription('Represents the log status for the log level Critical of this\n                 client.')
sfpsEventLogClientCriticalDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientCriticalDisplayStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientCriticalDisplayStatus.setDescription('Represents the display status for the log level Critical of\n                 this client.')
sfpsEventLogClientInfoLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientInfoLogStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientInfoLogStatus.setDescription('Represents the log status for the log level Info of this\n                 client.')
sfpsEventLogClientInfoDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientInfoDisplayStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientInfoDisplayStatus.setDescription('Represents the display status for the log level Info of this\n                 client.')
sfpsEventLogClientDebugLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientDebugLogStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientDebugLogStatus.setDescription('Represents the log status for the log level Debug of this\n                 client.')
sfpsEventLogClientDebugDisplayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientDebugDisplayStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientDebugDisplayStatus.setDescription('Represents the display status for the log level Debug of this\n                 client.')
sfpsEventLogClientConfigAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("freezeLog", 1), ("errorLog", 2), ("criticalLog", 3), ("infoLog", 4), ("debugLog", 5), ("allLogLevels", 6), ("allClients", 7), ("masterLog", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIVerb.setDescription('')
sfpsEventLogClientConfigAPIAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIAdminStatus.setDescription('')
sfpsEventLogClientConfigAPIClientName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIClientName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIClientName.setDescription('')
sfpsEventLogClientConfigAPIClientID = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIClientID.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPIClientID.setDescription('')
sfpsEventLogClientConfigAPILogDisplay = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("logAndDisplay", 2), ("logOnly", 3), ("displayOnly", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPILogDisplay.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsEventLogClientConfigAPILogDisplay.setDescription('')
sfpsFragStatsTotalFrags = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsTotalFrags.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFragStatsTotalFrags.setDescription('')
sfpsFragStatsNumLookupFail = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsNumLookupFail.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFragStatsNumLookupFail.setDescription('')
sfpsFragStatsAvgCompares = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsAvgCompares.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFragStatsAvgCompares.setDescription('')
sfpsFragStatsNumNodes = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsNumNodes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFragStatsNumNodes.setDescription('')
sfpsFragStatsNumUsed = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsNumUsed.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFragStatsNumUsed.setDescription('')
sfpsFragStatsMaxNumUsed = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsMaxNumUsed.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFragStatsMaxNumUsed.setDescription('')
sfpsFragStatsNumStolen = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 11, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsFragStatsNumStolen.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsFragStatsNumStolen.setDescription('')
sfpsTrapAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("enable", 2), ("disable", 3), ("resetTrapStats", 4), ("resetAllStats", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsTrapAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTrapAPIVerb.setDescription('')
sfpsTrapAPITrapId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410))).clone(namedValues=NamedValues(("newUser", 1400), ("violation", 1401), ("srcBlock", 1402), ("dstBlock", 1403), ("portToStandby", 1404), ("portFromStandby", 1405), ("ageCnt", 1406), ("changeCount", 1407), ("foundNeighbor", 1408), ("lostNeighbor", 1409), ("agentIP", 1410)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsTrapAPITrapId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTrapAPITrapId.setDescription('')
sfpsTrapAPITotalSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapAPITotalSent.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTrapAPITotalSent.setDescription('')
sfpsTrapTableTrapId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422))).clone(namedValues=NamedValues(("newUser", 1400), ("violation", 1401), ("srcBlock", 1402), ("dstBlock", 1403), ("portToStandby", 1404), ("portFromStandby", 1405), ("ageCnt", 1406), ("changeCount", 1407), ("foundNeighbor", 1408), ("lostNeighbor", 1409), ("agentIP", 1410), ("noSrcVlans", 1411), ("noDestVlans", 1412), ("noSrcVlansEnabled", 1413), ("noDestVlansEnabled", 1414), ("noCommonSecureVlan", 1415), ("incVlanUserCount", 1416), ("decVlanUserCount", 1417), ("vrrpPrimaryResign", 1418), ("vrrpPrimaryAged", 1419), ("vrrpSecondaryUp", 1420), ("hsrpPrimaryResign", 1421), ("hsrpSecondaryUp", 1422)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapTableTrapId.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTrapTableTrapId.setDescription('')
sfpsTrapTableAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapTableAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTrapTableAdminStatus.setDescription('')
sfpsTrapTableNumSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapTableNumSent.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTrapTableNumSent.setDescription('')
sfpsTrapTableLastSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 7, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTrapTableLastSent.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTrapTableLastSent.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-EVENTLOG-MIB", sfpsEventLogGenConfigLoggingIndex=sfpsEventLogGenConfigLoggingIndex, sfpsFragStatsMaxNumUsed=sfpsFragStatsMaxNumUsed, sfpsEventLogGenConfigMessageFilter=sfpsEventLogGenConfigMessageFilter, sfpsEventLogGenConfigDisplayWrapDetect=sfpsEventLogGenConfigDisplayWrapDetect, sfpsEventLogClientCriticalDisplayStatus=sfpsEventLogClientCriticalDisplayStatus, sfpsEventLogMessageString=sfpsEventLogMessageString, sfpsFragStatsAvgCompares=sfpsFragStatsAvgCompares, sfpsEventLogGenConfigTable=sfpsEventLogGenConfigTable, sfpsEventLogGenConfigAdvertiseAddr=sfpsEventLogGenConfigAdvertiseAddr, sfpsEventLogInfo2=sfpsEventLogInfo2, sfpsEventLogClientCriticalLogStatus=sfpsEventLogClientCriticalLogStatus, sfpsFragStatsNumUsed=sfpsFragStatsNumUsed, sfpsTrapTableAdminStatus=sfpsTrapTableAdminStatus, sfpsTrapAPITotalSent=sfpsTrapAPITotalSent, sfpsEventLogWindowStart=sfpsEventLogWindowStart, sfpsEventLogStatsSwInst=sfpsEventLogStatsSwInst, sfpsEventLogIndex=sfpsEventLogIndex, sfpsEventLogStatsEntry=sfpsEventLogStatsEntry, sfpsEventLogClientFreezeDisplayStatus=sfpsEventLogClientFreezeDisplayStatus, sfpsEventLogClientDebugDisplayStatus=sfpsEventLogClientDebugDisplayStatus, sfpsEventLogGenConfigAutoFreeze=sfpsEventLogGenConfigAutoFreeze, sfpsEventLogClientName=sfpsEventLogClientName, sfpsEventLogGenConfigOperTime=sfpsEventLogGenConfigOperTime, SfpsSwitchInstance=SfpsSwitchInstance, sfpsEventLogCallTag=sfpsEventLogCallTag, sfpsEventLogClientConfigTable=sfpsEventLogClientConfigTable, sfpsEventLogGenConfigSwInst=sfpsEventLogGenConfigSwInst, sfpsEventLogGenConfigAdminStatus=sfpsEventLogGenConfigAdminStatus, sfpsEventLogClientConfigId=sfpsEventLogClientConfigId, sfpsEventLogClientDisplayStatus=sfpsEventLogClientDisplayStatus, sfpsEventLogClientErrorDisplayStatus=sfpsEventLogClientErrorDisplayStatus, sfpsEventLogClientDebugLogStatus=sfpsEventLogClientDebugLogStatus, sfpsTrapTableTrapId=sfpsTrapTableTrapId, sfpsEventLogGenConfigEntry=sfpsEventLogGenConfigEntry, sfpsFragStatsNumNodes=sfpsFragStatsNumNodes, sfpsEventLogLevel=sfpsEventLogLevel, sfpsFragStatsTotalFrags=sfpsFragStatsTotalFrags, sfpsEventLogClientFreezeLogStatus=sfpsEventLogClientFreezeLogStatus, sfpsEventLogClientConfigEntry=sfpsEventLogClientConfigEntry, sfpsEventLogClientErrorLogStatus=sfpsEventLogClientErrorLogStatus, sfpsEventLogClientConfigAPILogDisplay=sfpsEventLogClientConfigAPILogDisplay, sfpsTrapAPITrapId=sfpsTrapAPITrapId, sfpsEventLogClientConfigName=sfpsEventLogClientConfigName, sfpsEventLogClientConfigAPIVerb=sfpsEventLogClientConfigAPIVerb, sfpsTrapTableLastSent=sfpsTrapTableLastSent, sfpsEventLogInfo1=sfpsEventLogInfo1, sfpsEventLogClientInfoDisplayStatus=sfpsEventLogClientInfoDisplayStatus, sfpsEventLogClientConfigAPIClientID=sfpsEventLogClientConfigAPIClientID, HexInteger=HexInteger, sfpsEventLogStatsTable=sfpsEventLogStatsTable, sfpsEventLogGenConfigOperStatus=sfpsEventLogGenConfigOperStatus, sfpsEventLogGenConfigCallTagFilter=sfpsEventLogGenConfigCallTagFilter, sfpsEventLogClientConfigAPIAdminStatus=sfpsEventLogClientConfigAPIAdminStatus, sfpsEventLogClientInfoLogStatus=sfpsEventLogClientInfoLogStatus, sfpsFragStatsNumStolen=sfpsFragStatsNumStolen, sfpsEventLogGenConfigWindowStart=sfpsEventLogGenConfigWindowStart, sfpsEventLogClientLogStatus=sfpsEventLogClientLogStatus, sfpsEventLogClientConfigAPIClientName=sfpsEventLogClientConfigAPIClientName, sfpsEventLogTime=sfpsEventLogTime, sfpsTrapTableNumSent=sfpsTrapTableNumSent, sfpsFragStatsNumLookupFail=sfpsFragStatsNumLookupFail, sfpsTrapAPIVerb=sfpsTrapAPIVerb)
