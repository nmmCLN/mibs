#
# PySNMP MIB module PACKETLOGIC-SNOOPER-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-SNOOPER-DHCP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:31:48 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
snoopers, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "snoopers")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, Bits, NotificationType, IpAddress, Unsigned32, Counter64, ObjectIdentity, iso, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "NotificationType", "IpAddress", "Unsigned32", "Counter64", "ObjectIdentity", "iso", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
dhcp = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1))
dhcp.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: dhcp.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: dhcp.setOrganization('Procera Networks, Inc.')
dhcpTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1), )
if mibBuilder.loadTexts: dhcpTable.setStatus('current')
dhcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpEntryIndex"))
if mibBuilder.loadTexts: dhcpEntry.setStatus('current')
dhcpEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dhcpEntryIndex.setStatus('current')
dhcpRequestsInQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1))
dhcpRequestsInQueueVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 1), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRequestsInQueueVal.setStatus('current')
dhcpRequestsInQueueMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRequestsInQueueMax.setStatus('current')
dhcpRequestsInQueueLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4), )
if mibBuilder.loadTexts: dhcpRequestsInQueueLevelTable.setStatus('current')
dhcpRequestsInQueueLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpRequestsInQueueLevelName"))
if mibBuilder.loadTexts: dhcpRequestsInQueueLevelEntry.setStatus('current')
dhcpRequestsInQueueLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpRequestsInQueueLevelName.setStatus('current')
dhcpRequestsInQueueLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4, 1, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRequestsInQueueLevelVal.setStatus('current')
dhcpRequestsInQueueLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 1, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRequestsInQueueLevelMax.setStatus('current')
dhcpDynAddFailures = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2))
dhcpDynAddFailuresVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDynAddFailuresVal.setStatus('current')
dhcpDynAddFailuresMom = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDynAddFailuresMom.setStatus('current')
dhcpDynAddFailuresMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDynAddFailuresMax.setStatus('current')
dhcpDynAddFailuresLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4), )
if mibBuilder.loadTexts: dhcpDynAddFailuresLevelTable.setStatus('current')
dhcpDynAddFailuresLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpDynAddFailuresLevelName"))
if mibBuilder.loadTexts: dhcpDynAddFailuresLevelEntry.setStatus('current')
dhcpDynAddFailuresLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpDynAddFailuresLevelName.setStatus('current')
dhcpDynAddFailuresLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDynAddFailuresLevelVal.setStatus('current')
dhcpDynAddFailuresLevelMom = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDynAddFailuresLevelMom.setStatus('current')
dhcpDynAddFailuresLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 2, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpDynAddFailuresLevelMax.setStatus('current')
dhcpPLDBReconnects = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3))
dhcpPLDBReconnectsVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 1), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBReconnectsVal.setStatus('current')
dhcpPLDBReconnectsMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBReconnectsMax.setStatus('current')
dhcpPLDBReconnectsLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4), )
if mibBuilder.loadTexts: dhcpPLDBReconnectsLevelTable.setStatus('current')
dhcpPLDBReconnectsLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDBReconnectsLevelName"))
if mibBuilder.loadTexts: dhcpPLDBReconnectsLevelEntry.setStatus('current')
dhcpPLDBReconnectsLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPLDBReconnectsLevelName.setStatus('current')
dhcpPLDBReconnectsLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4, 1, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBReconnectsLevelVal.setStatus('current')
dhcpPLDBReconnectsLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 3, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBReconnectsLevelMax.setStatus('current')
dhcpPLDBUptime = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4))
dhcpPLDBUptimeVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBUptimeVal.setStatus('current')
dhcpPLDBUptimeLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 2), )
if mibBuilder.loadTexts: dhcpPLDBUptimeLevelTable.setStatus('current')
dhcpPLDBUptimeLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 2, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDBUptimeLevelName"))
if mibBuilder.loadTexts: dhcpPLDBUptimeLevelEntry.setStatus('current')
dhcpPLDBUptimeLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPLDBUptimeLevelName.setStatus('current')
dhcpPLDBUptimeLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 4, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBUptimeLevelVal.setStatus('current')
dhcpPLDBCommits = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5))
dhcpPLDBCommitsVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBCommitsVal.setStatus('current')
dhcpPLDBCommitsMom = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBCommitsMom.setStatus('current')
dhcpPLDBCommitsMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBCommitsMax.setStatus('current')
dhcpPLDBCommitsLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4), )
if mibBuilder.loadTexts: dhcpPLDBCommitsLevelTable.setStatus('current')
dhcpPLDBCommitsLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDBCommitsLevelName"))
if mibBuilder.loadTexts: dhcpPLDBCommitsLevelEntry.setStatus('current')
dhcpPLDBCommitsLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPLDBCommitsLevelName.setStatus('current')
dhcpPLDBCommitsLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBCommitsLevelVal.setStatus('current')
dhcpPLDBCommitsLevelMom = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBCommitsLevelMom.setStatus('current')
dhcpPLDBCommitsLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 5, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDBCommitsLevelMax.setStatus('current')
dhcpPLDReconnects = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6))
dhcpPLDReconnectsVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 1), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDReconnectsVal.setStatus('current')
dhcpPLDReconnectsMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDReconnectsMax.setStatus('current')
dhcpPLDReconnectsLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4), )
if mibBuilder.loadTexts: dhcpPLDReconnectsLevelTable.setStatus('current')
dhcpPLDReconnectsLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDReconnectsLevelName"))
if mibBuilder.loadTexts: dhcpPLDReconnectsLevelEntry.setStatus('current')
dhcpPLDReconnectsLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPLDReconnectsLevelName.setStatus('current')
dhcpPLDReconnectsLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4, 1, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDReconnectsLevelVal.setStatus('current')
dhcpPLDReconnectsLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 6, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDReconnectsLevelMax.setStatus('current')
dhcpPLDUptime = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7))
dhcpPLDUptimeVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDUptimeVal.setStatus('current')
dhcpPLDUptimeLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 2), )
if mibBuilder.loadTexts: dhcpPLDUptimeLevelTable.setStatus('current')
dhcpPLDUptimeLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 2, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDUptimeLevelName"))
if mibBuilder.loadTexts: dhcpPLDUptimeLevelEntry.setStatus('current')
dhcpPLDUptimeLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPLDUptimeLevelName.setStatus('current')
dhcpPLDUptimeLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 7, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDUptimeLevelVal.setStatus('current')
dhcpPLDOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8))
dhcpPLDOperationsVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDOperationsVal.setStatus('current')
dhcpPLDOperationsMom = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDOperationsMom.setStatus('current')
dhcpPLDOperationsMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDOperationsMax.setStatus('current')
dhcpPLDOperationsLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4), )
if mibBuilder.loadTexts: dhcpPLDOperationsLevelTable.setStatus('current')
dhcpPLDOperationsLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPLDOperationsLevelName"))
if mibBuilder.loadTexts: dhcpPLDOperationsLevelEntry.setStatus('current')
dhcpPLDOperationsLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPLDOperationsLevelName.setStatus('current')
dhcpPLDOperationsLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDOperationsLevelVal.setStatus('current')
dhcpPLDOperationsLevelMom = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDOperationsLevelMom.setStatus('current')
dhcpPLDOperationsLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 8, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPLDOperationsLevelMax.setStatus('current')
dhcpPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9))
dhcpPacketsVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsVal.setStatus('current')
dhcpPacketsMom = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsMom.setStatus('current')
dhcpPacketsMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsMax.setStatus('current')
dhcpPacketsLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4), )
if mibBuilder.loadTexts: dhcpPacketsLevelTable.setStatus('current')
dhcpPacketsLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPacketsLevelName"))
if mibBuilder.loadTexts: dhcpPacketsLevelEntry.setStatus('current')
dhcpPacketsLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPacketsLevelName.setStatus('current')
dhcpPacketsLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsLevelVal.setStatus('current')
dhcpPacketsLevelMom = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsLevelMom.setStatus('current')
dhcpPacketsLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 9, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsLevelMax.setStatus('current')
dhcpUnparsablePackets = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10))
dhcpUnparsablePacketsVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpUnparsablePacketsVal.setStatus('current')
dhcpUnparsablePacketsMom = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpUnparsablePacketsMom.setStatus('current')
dhcpUnparsablePacketsMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpUnparsablePacketsMax.setStatus('current')
dhcpUnparsablePacketsLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4), )
if mibBuilder.loadTexts: dhcpUnparsablePacketsLevelTable.setStatus('current')
dhcpUnparsablePacketsLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpUnparsablePacketsLevelName"))
if mibBuilder.loadTexts: dhcpUnparsablePacketsLevelEntry.setStatus('current')
dhcpUnparsablePacketsLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpUnparsablePacketsLevelName.setStatus('current')
dhcpUnparsablePacketsLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpUnparsablePacketsLevelVal.setStatus('current')
dhcpUnparsablePacketsLevelMom = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpUnparsablePacketsLevelMom.setStatus('current')
dhcpUnparsablePacketsLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 10, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpUnparsablePacketsLevelMax.setStatus('current')
dhcpPacketsReq = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11))
dhcpPacketsReqVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsReqVal.setStatus('current')
dhcpPacketsReqMom = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsReqMom.setStatus('current')
dhcpPacketsReqMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsReqMax.setStatus('current')
dhcpPacketsReqLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4), )
if mibBuilder.loadTexts: dhcpPacketsReqLevelTable.setStatus('current')
dhcpPacketsReqLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPacketsReqLevelName"))
if mibBuilder.loadTexts: dhcpPacketsReqLevelEntry.setStatus('current')
dhcpPacketsReqLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPacketsReqLevelName.setStatus('current')
dhcpPacketsReqLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsReqLevelVal.setStatus('current')
dhcpPacketsReqLevelMom = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsReqLevelMom.setStatus('current')
dhcpPacketsReqLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 11, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsReqLevelMax.setStatus('current')
dhcpPacketsAck = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12))
dhcpPacketsAckVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsAckVal.setStatus('current')
dhcpPacketsAckMom = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsAckMom.setStatus('current')
dhcpPacketsAckMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsAckMax.setStatus('current')
dhcpPacketsAckLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4), )
if mibBuilder.loadTexts: dhcpPacketsAckLevelTable.setStatus('current')
dhcpPacketsAckLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPacketsAckLevelName"))
if mibBuilder.loadTexts: dhcpPacketsAckLevelEntry.setStatus('current')
dhcpPacketsAckLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPacketsAckLevelName.setStatus('current')
dhcpPacketsAckLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsAckLevelVal.setStatus('current')
dhcpPacketsAckLevelMom = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsAckLevelMom.setStatus('current')
dhcpPacketsAckLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 12, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsAckLevelMax.setStatus('current')
dhcpPacketsIgnored = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13))
dhcpPacketsIgnoredVal = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsIgnoredVal.setStatus('current')
dhcpPacketsIgnoredMom = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 2), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsIgnoredMom.setStatus('current')
dhcpPacketsIgnoredMax = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsIgnoredMax.setStatus('current')
dhcpPacketsIgnoredLevelTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4), )
if mibBuilder.loadTexts: dhcpPacketsIgnoredLevelTable.setStatus('current')
dhcpPacketsIgnoredLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1), ).setIndexNames((0, "PACKETLOGIC-SNOOPER-DHCP-MIB", "dhcpPacketsIgnoredLevelName"))
if mibBuilder.loadTexts: dhcpPacketsIgnoredLevelEntry.setStatus('current')
dhcpPacketsIgnoredLevelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: dhcpPacketsIgnoredLevelName.setStatus('current')
dhcpPacketsIgnoredLevelVal = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsIgnoredLevelVal.setStatus('current')
dhcpPacketsIgnoredLevelMom = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1, 3), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsIgnoredLevelMom.setStatus('current')
dhcpPacketsIgnoredLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 10, 1, 1, 1, 13, 4, 1, 4), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPacketsIgnoredLevelMax.setStatus('current')
mibBuilder.exportSymbols("PACKETLOGIC-SNOOPER-DHCP-MIB", dhcpPLDBCommitsLevelVal=dhcpPLDBCommitsLevelVal, dhcpPLDReconnectsLevelEntry=dhcpPLDReconnectsLevelEntry, dhcpPLDBUptimeLevelVal=dhcpPLDBUptimeLevelVal, dhcpPLDOperationsMax=dhcpPLDOperationsMax, dhcpDynAddFailuresLevelMom=dhcpDynAddFailuresLevelMom, dhcpPLDBCommitsLevelName=dhcpPLDBCommitsLevelName, dhcpPLDBReconnectsLevelMax=dhcpPLDBReconnectsLevelMax, dhcpPLDReconnectsLevelVal=dhcpPLDReconnectsLevelVal, dhcpDynAddFailuresLevelName=dhcpDynAddFailuresLevelName, dhcpPacketsIgnoredLevelVal=dhcpPacketsIgnoredLevelVal, dhcpPacketsIgnoredLevelEntry=dhcpPacketsIgnoredLevelEntry, dhcpPacketsIgnoredLevelTable=dhcpPacketsIgnoredLevelTable, dhcpPLDBReconnectsLevelName=dhcpPLDBReconnectsLevelName, dhcpPacketsAckLevelVal=dhcpPacketsAckLevelVal, dhcpRequestsInQueueVal=dhcpRequestsInQueueVal, dhcpPacketsLevelTable=dhcpPacketsLevelTable, dhcpPLDBUptimeLevelTable=dhcpPLDBUptimeLevelTable, dhcpPLDBCommitsLevelTable=dhcpPLDBCommitsLevelTable, dhcpEntry=dhcpEntry, dhcpRequestsInQueueLevelName=dhcpRequestsInQueueLevelName, dhcpTable=dhcpTable, dhcpPLDBUptimeLevelName=dhcpPLDBUptimeLevelName, dhcpDynAddFailuresLevelMax=dhcpDynAddFailuresLevelMax, dhcpEntryIndex=dhcpEntryIndex, dhcpUnparsablePacketsVal=dhcpUnparsablePacketsVal, dhcpPLDUptime=dhcpPLDUptime, dhcpPLDBCommitsMom=dhcpPLDBCommitsMom, dhcpPLDOperations=dhcpPLDOperations, dhcpPacketsMom=dhcpPacketsMom, dhcpRequestsInQueueLevelTable=dhcpRequestsInQueueLevelTable, dhcpPacketsReqVal=dhcpPacketsReqVal, dhcpPLDBUptime=dhcpPLDBUptime, dhcpPLDOperationsLevelEntry=dhcpPLDOperationsLevelEntry, dhcpUnparsablePacketsLevelEntry=dhcpUnparsablePacketsLevelEntry, dhcpPLDBCommitsMax=dhcpPLDBCommitsMax, dhcpRequestsInQueueLevelMax=dhcpRequestsInQueueLevelMax, dhcpPacketsIgnoredMax=dhcpPacketsIgnoredMax, dhcpPacketsReq=dhcpPacketsReq, dhcpUnparsablePacketsMom=dhcpUnparsablePacketsMom, PYSNMP_MODULE_ID=dhcp, dhcpPLDBCommitsLevelMax=dhcpPLDBCommitsLevelMax, dhcpDynAddFailuresLevelEntry=dhcpDynAddFailuresLevelEntry, dhcpPLDBUptimeLevelEntry=dhcpPLDBUptimeLevelEntry, dhcpPacketsIgnored=dhcpPacketsIgnored, dhcpPacketsMax=dhcpPacketsMax, dhcpPacketsLevelEntry=dhcpPacketsLevelEntry, dhcpPLDUptimeLevelName=dhcpPLDUptimeLevelName, dhcpPacketsReqLevelName=dhcpPacketsReqLevelName, dhcpUnparsablePackets=dhcpUnparsablePackets, dhcpUnparsablePacketsLevelMom=dhcpUnparsablePacketsLevelMom, dhcpPacketsAckLevelName=dhcpPacketsAckLevelName, dhcpPLDReconnectsLevelTable=dhcpPLDReconnectsLevelTable, dhcpPacketsReqLevelMax=dhcpPacketsReqLevelMax, dhcpPLDBCommitsLevelEntry=dhcpPLDBCommitsLevelEntry, dhcpDynAddFailuresLevelTable=dhcpDynAddFailuresLevelTable, dhcpPacketsAckMom=dhcpPacketsAckMom, dhcpPacketsAckMax=dhcpPacketsAckMax, dhcpPLDReconnects=dhcpPLDReconnects, dhcpPLDBReconnectsVal=dhcpPLDBReconnectsVal, dhcpPacketsReqLevelMom=dhcpPacketsReqLevelMom, dhcpPLDOperationsLevelVal=dhcpPLDOperationsLevelVal, dhcpPLDBUptimeVal=dhcpPLDBUptimeVal, dhcpPLDBReconnects=dhcpPLDBReconnects, dhcpPLDOperationsLevelTable=dhcpPLDOperationsLevelTable, dhcp=dhcp, dhcpPacketsLevelName=dhcpPacketsLevelName, dhcpPLDReconnectsMax=dhcpPLDReconnectsMax, dhcpPLDReconnectsLevelName=dhcpPLDReconnectsLevelName, dhcpPLDOperationsLevelMom=dhcpPLDOperationsLevelMom, dhcpPLDBReconnectsMax=dhcpPLDBReconnectsMax, dhcpDynAddFailuresMax=dhcpDynAddFailuresMax, dhcpPLDBReconnectsLevelTable=dhcpPLDBReconnectsLevelTable, dhcpPacketsReqLevelEntry=dhcpPacketsReqLevelEntry, dhcpPLDBCommitsLevelMom=dhcpPLDBCommitsLevelMom, dhcpUnparsablePacketsLevelTable=dhcpUnparsablePacketsLevelTable, dhcpPLDReconnectsLevelMax=dhcpPLDReconnectsLevelMax, dhcpPacketsAckLevelMom=dhcpPacketsAckLevelMom, dhcpRequestsInQueueLevelEntry=dhcpRequestsInQueueLevelEntry, dhcpPacketsReqLevelVal=dhcpPacketsReqLevelVal, dhcpDynAddFailures=dhcpDynAddFailures, dhcpPacketsLevelVal=dhcpPacketsLevelVal, dhcpRequestsInQueueMax=dhcpRequestsInQueueMax, dhcpPacketsReqMax=dhcpPacketsReqMax, dhcpPacketsIgnoredLevelMom=dhcpPacketsIgnoredLevelMom, dhcpPLDReconnectsVal=dhcpPLDReconnectsVal, dhcpRequestsInQueueLevelVal=dhcpRequestsInQueueLevelVal, dhcpPLDBReconnectsLevelEntry=dhcpPLDBReconnectsLevelEntry, dhcpUnparsablePacketsLevelName=dhcpUnparsablePacketsLevelName, dhcpPacketsReqLevelTable=dhcpPacketsReqLevelTable, dhcpDynAddFailuresLevelVal=dhcpDynAddFailuresLevelVal, dhcpPacketsAckLevelMax=dhcpPacketsAckLevelMax, dhcpPacketsAckLevelEntry=dhcpPacketsAckLevelEntry, dhcpPacketsReqMom=dhcpPacketsReqMom, dhcpPacketsIgnoredLevelMax=dhcpPacketsIgnoredLevelMax, dhcpPLDBCommitsVal=dhcpPLDBCommitsVal, dhcpPLDOperationsVal=dhcpPLDOperationsVal, dhcpPLDBReconnectsLevelVal=dhcpPLDBReconnectsLevelVal, dhcpDynAddFailuresVal=dhcpDynAddFailuresVal, dhcpPacketsLevelMax=dhcpPacketsLevelMax, dhcpUnparsablePacketsLevelVal=dhcpUnparsablePacketsLevelVal, dhcpPLDBCommits=dhcpPLDBCommits, dhcpPLDOperationsLevelName=dhcpPLDOperationsLevelName, dhcpPacketsAckVal=dhcpPacketsAckVal, dhcpPacketsVal=dhcpPacketsVal, dhcpPacketsLevelMom=dhcpPacketsLevelMom, dhcpPacketsIgnoredMom=dhcpPacketsIgnoredMom, dhcpUnparsablePacketsMax=dhcpUnparsablePacketsMax, dhcpUnparsablePacketsLevelMax=dhcpUnparsablePacketsLevelMax, dhcpPLDUptimeLevelTable=dhcpPLDUptimeLevelTable, dhcpPacketsAck=dhcpPacketsAck, dhcpPLDOperationsMom=dhcpPLDOperationsMom, dhcpDynAddFailuresMom=dhcpDynAddFailuresMom, dhcpPLDUptimeLevelVal=dhcpPLDUptimeLevelVal, dhcpPacketsIgnoredLevelName=dhcpPacketsIgnoredLevelName, dhcpPLDOperationsLevelMax=dhcpPLDOperationsLevelMax, dhcpRequestsInQueue=dhcpRequestsInQueue, dhcpPacketsIgnoredVal=dhcpPacketsIgnoredVal, dhcpPLDUptimeLevelEntry=dhcpPLDUptimeLevelEntry, dhcpPacketsAckLevelTable=dhcpPacketsAckLevelTable, dhcpPLDUptimeVal=dhcpPLDUptimeVal, dhcpPackets=dhcpPackets)
