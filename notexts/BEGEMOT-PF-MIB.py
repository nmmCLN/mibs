#
# PySNMP MIB module BEGEMOT-PF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-PF-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:14:11 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
InetAddressPrefixLength, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, TimeTicks, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Integer32, IpAddress, Gauge32, iso, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "TimeTicks", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Integer32", "IpAddress", "Gauge32", "iso", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
begemotPf = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 200))
begemotPf.setRevisions(('2010-03-18 00:00', '2009-12-05 00:00', '2005-01-24 00:00',))
if mibBuilder.loadTexts: begemotPf.setLastUpdated('201003180000Z')
if mibBuilder.loadTexts: begemotPf.setOrganization('NixSys BVBA')
begemotPfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1))
pfStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 1))
pfCounter = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 2))
pfStateTable = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 3))
pfSrcNodes = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 4))
pfLimits = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 5))
pfTimeouts = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6))
pfLogInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7))
pfInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8))
pfTables = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9))
pfAltq = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10))
pfLabels = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11))
pfStatusRunning = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStatusRunning.setStatus('current')
pfStatusRuntime = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 1, 2), TimeTicks()).setUnits('1/100th of a Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStatusRuntime.setStatus('current')
pfStatusDebug = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("urgent", 1), ("misc", 2), ("loud", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStatusDebug.setStatus('current')
pfStatusHostId = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStatusHostId.setStatus('current')
pfCounterMatch = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCounterMatch.setStatus('current')
pfCounterBadOffset = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCounterBadOffset.setStatus('current')
pfCounterFragment = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCounterFragment.setStatus('current')
pfCounterShort = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCounterShort.setStatus('current')
pfCounterNormalize = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCounterNormalize.setStatus('current')
pfCounterMemDrop = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCounterMemDrop.setStatus('current')
pfStateTableCount = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStateTableCount.setStatus('current')
pfStateTableSearches = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStateTableSearches.setStatus('current')
pfStateTableInserts = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStateTableInserts.setStatus('current')
pfStateTableRemovals = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStateTableRemovals.setStatus('current')
pfSrcNodesCount = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfSrcNodesCount.setStatus('current')
pfSrcNodesSearches = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfSrcNodesSearches.setStatus('current')
pfSrcNodesInserts = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfSrcNodesInserts.setStatus('current')
pfSrcNodesRemovals = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfSrcNodesRemovals.setStatus('current')
pfLimitsStates = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 5, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLimitsStates.setStatus('current')
pfLimitsSrcNodes = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 5, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLimitsSrcNodes.setStatus('current')
pfLimitsFrags = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 5, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLimitsFrags.setStatus('current')
pfTimeoutsTcpFirst = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsTcpFirst.setStatus('current')
pfTimeoutsTcpOpening = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsTcpOpening.setStatus('current')
pfTimeoutsTcpEstablished = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsTcpEstablished.setStatus('current')
pfTimeoutsTcpClosing = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsTcpClosing.setStatus('current')
pfTimeoutsTcpFinWait = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsTcpFinWait.setStatus('current')
pfTimeoutsTcpClosed = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsTcpClosed.setStatus('current')
pfTimeoutsUdpFirst = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsUdpFirst.setStatus('current')
pfTimeoutsUdpSingle = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsUdpSingle.setStatus('current')
pfTimeoutsUdpMultiple = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsUdpMultiple.setStatus('current')
pfTimeoutsIcmpFirst = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsIcmpFirst.setStatus('current')
pfTimeoutsIcmpError = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsIcmpError.setStatus('current')
pfTimeoutsOtherFirst = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsOtherFirst.setStatus('current')
pfTimeoutsOtherSingle = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsOtherSingle.setStatus('current')
pfTimeoutsOtherMultiple = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsOtherMultiple.setStatus('current')
pfTimeoutsFragment = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsFragment.setStatus('current')
pfTimeoutsInterval = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsInterval.setStatus('current')
pfTimeoutsAdaptiveStart = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsAdaptiveStart.setStatus('current')
pfTimeoutsAdaptiveEnd = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsAdaptiveEnd.setStatus('current')
pfTimeoutsSrcNode = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 6, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutsSrcNode.setStatus('current')
pfLogInterfaceName = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceName.setStatus('current')
pfLogInterfaceIp4BytesIn = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp4BytesIn.setStatus('current')
pfLogInterfaceIp4BytesOut = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp4BytesOut.setStatus('current')
pfLogInterfaceIp4PktsInPass = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp4PktsInPass.setStatus('current')
pfLogInterfaceIp4PktsInDrop = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp4PktsInDrop.setStatus('current')
pfLogInterfaceIp4PktsOutPass = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp4PktsOutPass.setStatus('current')
pfLogInterfaceIp4PktsOutDrop = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp4PktsOutDrop.setStatus('current')
pfLogInterfaceIp6BytesIn = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp6BytesIn.setStatus('current')
pfLogInterfaceIp6BytesOut = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp6BytesOut.setStatus('current')
pfLogInterfaceIp6PktsInPass = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp6PktsInPass.setStatus('current')
pfLogInterfaceIp6PktsInDrop = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp6PktsInDrop.setStatus('current')
pfLogInterfaceIp6PktsOutPass = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp6PktsOutPass.setStatus('current')
pfLogInterfaceIp6PktsOutDrop = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 7, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogInterfaceIp6PktsOutDrop.setStatus('current')
pfInterfacesIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIfNumber.setStatus('current')
pfInterfacesIfTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2), )
if mibBuilder.loadTexts: pfInterfacesIfTable.setStatus('current')
pfInterfacesIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1), ).setIndexNames((0, "BEGEMOT-PF-MIB", "pfInterfacesIfIndex"))
if mibBuilder.loadTexts: pfInterfacesIfEntry.setStatus('current')
pfInterfacesIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pfInterfacesIfIndex.setStatus('current')
pfInterfacesIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIfDescr.setStatus('current')
pfInterfacesIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("group", 0), ("instance", 1), ("detached", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIfType.setStatus('current')
pfInterfacesIfTZero = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 4), TimeTicks()).setUnits('1/100th of a Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIfTZero.setStatus('current')
pfInterfacesIfRefsState = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIfRefsState.setStatus('current')
pfInterfacesIfRefsRule = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIfRefsRule.setStatus('current')
pfInterfacesIf4BytesInPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf4BytesInPass.setStatus('current')
pfInterfacesIf4BytesInBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf4BytesInBlock.setStatus('current')
pfInterfacesIf4BytesOutPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf4BytesOutPass.setStatus('current')
pfInterfacesIf4BytesOutBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf4BytesOutBlock.setStatus('current')
pfInterfacesIf4PktsInPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf4PktsInPass.setStatus('current')
pfInterfacesIf4PktsInBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf4PktsInBlock.setStatus('current')
pfInterfacesIf4PktsOutPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf4PktsOutPass.setStatus('current')
pfInterfacesIf4PktsOutBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf4PktsOutBlock.setStatus('current')
pfInterfacesIf6BytesInPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf6BytesInPass.setStatus('current')
pfInterfacesIf6BytesInBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf6BytesInBlock.setStatus('current')
pfInterfacesIf6BytesOutPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf6BytesOutPass.setStatus('current')
pfInterfacesIf6BytesOutBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf6BytesOutBlock.setStatus('current')
pfInterfacesIf6PktsInPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf6PktsInPass.setStatus('current')
pfInterfacesIf6PktsInBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf6PktsInBlock.setStatus('current')
pfInterfacesIf6PktsOutPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf6PktsOutPass.setStatus('current')
pfInterfacesIf6PktsOutBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 8, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfInterfacesIf6PktsOutBlock.setStatus('current')
pfTablesTblNumber = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblNumber.setStatus('current')
pfTablesTblTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2), )
if mibBuilder.loadTexts: pfTablesTblTable.setStatus('current')
pfTablesTblEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1), ).setIndexNames((0, "BEGEMOT-PF-MIB", "pfTablesTblIndex"))
if mibBuilder.loadTexts: pfTablesTblEntry.setStatus('current')
pfTablesTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pfTablesTblIndex.setStatus('current')
pfTablesTblDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblDescr.setStatus('current')
pfTablesTblCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblCount.setStatus('current')
pfTablesTblTZero = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 4), TimeTicks()).setUnits('1/100th of a Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblTZero.setStatus('current')
pfTablesTblRefsAnchor = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblRefsAnchor.setStatus('current')
pfTablesTblRefsRule = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblRefsRule.setStatus('current')
pfTablesTblEvalMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblEvalMatch.setStatus('current')
pfTablesTblEvalNoMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblEvalNoMatch.setStatus('current')
pfTablesTblBytesInPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblBytesInPass.setStatus('current')
pfTablesTblBytesInBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblBytesInBlock.setStatus('current')
pfTablesTblBytesInXPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblBytesInXPass.setStatus('current')
pfTablesTblBytesOutPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblBytesOutPass.setStatus('current')
pfTablesTblBytesOutBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblBytesOutBlock.setStatus('current')
pfTablesTblBytesOutXPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblBytesOutXPass.setStatus('current')
pfTablesTblPktsInPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblPktsInPass.setStatus('current')
pfTablesTblPktsInBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblPktsInBlock.setStatus('current')
pfTablesTblPktsInXPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblPktsInXPass.setStatus('current')
pfTablesTblPktsOutPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblPktsOutPass.setStatus('current')
pfTablesTblPktsOutBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblPktsOutBlock.setStatus('current')
pfTablesTblPktsOutXPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesTblPktsOutXPass.setStatus('current')
pfTablesAddrTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3), )
if mibBuilder.loadTexts: pfTablesAddrTable.setStatus('current')
pfTablesAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1), ).setIndexNames((0, "BEGEMOT-PF-MIB", "pfTablesAddrIndex"))
if mibBuilder.loadTexts: pfTablesAddrEntry.setStatus('current')
pfTablesAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pfTablesAddrIndex.setStatus('current')
pfTablesAddrNetType = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrNetType.setStatus('current')
pfTablesAddrNet = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrNet.setStatus('current')
pfTablesAddrPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 4), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrPrefix.setStatus('current')
pfTablesAddrTZero = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 5), TimeTicks()).setUnits('1/100th of a Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrTZero.setStatus('current')
pfTablesAddrBytesInPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrBytesInPass.setStatus('current')
pfTablesAddrBytesInBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrBytesInBlock.setStatus('current')
pfTablesAddrBytesOutPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrBytesOutPass.setStatus('current')
pfTablesAddrBytesOutBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrBytesOutBlock.setStatus('current')
pfTablesAddrPktsInPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrPktsInPass.setStatus('current')
pfTablesAddrPktsInBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrPktsInBlock.setStatus('current')
pfTablesAddrPktsOutPass = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrPktsOutPass.setStatus('current')
pfTablesAddrPktsOutBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 9, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTablesAddrPktsOutBlock.setStatus('current')
pfAltqQueueNumber = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfAltqQueueNumber.setStatus('current')
pfAltqQueueTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2), )
if mibBuilder.loadTexts: pfAltqQueueTable.setStatus('current')
pfAltqQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2, 1), ).setIndexNames((0, "BEGEMOT-PF-MIB", "pfAltqQueueIndex"))
if mibBuilder.loadTexts: pfAltqQueueEntry.setStatus('current')
pfAltqQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pfAltqQueueIndex.setStatus('current')
pfAltqQueueDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfAltqQueueDescr.setStatus('current')
pfAltqQueueParent = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfAltqQueueParent.setStatus('current')
pfAltqQueueScheduler = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 8, 11))).clone(namedValues=NamedValues(("cbq", 1), ("hfsc", 8), ("priq", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfAltqQueueScheduler.setStatus('current')
pfAltqQueueBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfAltqQueueBandwidth.setStatus('current')
pfAltqQueuePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfAltqQueuePriority.setStatus('current')
pfAltqQueueLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 10, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfAltqQueueLimit.setStatus('current')
pfLabelsLblNumber = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelsLblNumber.setStatus('current')
pfLabelsLblTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2), )
if mibBuilder.loadTexts: pfLabelsLblTable.setStatus('current')
pfLabelsLblEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2, 1), ).setIndexNames((0, "BEGEMOT-PF-MIB", "pfLabelsLblIndex"))
if mibBuilder.loadTexts: pfLabelsLblEntry.setStatus('current')
pfLabelsLblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pfLabelsLblIndex.setStatus('current')
pfLabelsLblName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelsLblName.setStatus('current')
pfLabelsLblEvals = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelsLblEvals.setStatus('current')
pfLabelsLblBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelsLblBytesIn.setStatus('current')
pfLabelsLblBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelsLblBytesOut.setStatus('current')
pfLabelsLblPktsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelsLblPktsIn.setStatus('current')
pfLabelsLblPktsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 200, 1, 11, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelsLblPktsOut.setStatus('current')
mibBuilder.exportSymbols("BEGEMOT-PF-MIB", pfInterfacesIf4BytesInBlock=pfInterfacesIf4BytesInBlock, pfTablesTblRefsAnchor=pfTablesTblRefsAnchor, pfStatus=pfStatus, pfStateTableSearches=pfStateTableSearches, pfLabelsLblName=pfLabelsLblName, pfLogInterfaceIp6PktsOutPass=pfLogInterfaceIp6PktsOutPass, pfStateTableCount=pfStateTableCount, pfLimitsFrags=pfLimitsFrags, pfTimeoutsOtherFirst=pfTimeoutsOtherFirst, pfAltqQueueScheduler=pfAltqQueueScheduler, pfInterfacesIf4BytesOutPass=pfInterfacesIf4BytesOutPass, pfInterfacesIf4BytesOutBlock=pfInterfacesIf4BytesOutBlock, pfTablesTblEvalMatch=pfTablesTblEvalMatch, pfTimeoutsInterval=pfTimeoutsInterval, pfLabelsLblEntry=pfLabelsLblEntry, begemotPf=begemotPf, pfInterfacesIfRefsState=pfInterfacesIfRefsState, pfTablesAddrBytesOutBlock=pfTablesAddrBytesOutBlock, pfAltqQueueParent=pfAltqQueueParent, pfTablesTblEntry=pfTablesTblEntry, pfLogInterfaceName=pfLogInterfaceName, pfTimeoutsUdpFirst=pfTimeoutsUdpFirst, pfAltqQueuePriority=pfAltqQueuePriority, pfLogInterfaceIp6PktsOutDrop=pfLogInterfaceIp6PktsOutDrop, pfInterfacesIfTable=pfInterfacesIfTable, pfTablesTblBytesInBlock=pfTablesTblBytesInBlock, pfTimeoutsAdaptiveEnd=pfTimeoutsAdaptiveEnd, pfTimeoutsTcpClosed=pfTimeoutsTcpClosed, pfTimeoutsTcpFinWait=pfTimeoutsTcpFinWait, pfTablesTblEvalNoMatch=pfTablesTblEvalNoMatch, pfLabelsLblEvals=pfLabelsLblEvals, pfInterfaces=pfInterfaces, pfStatusRuntime=pfStatusRuntime, pfInterfacesIf4BytesInPass=pfInterfacesIf4BytesInPass, pfAltqQueueBandwidth=pfAltqQueueBandwidth, pfTablesTblCount=pfTablesTblCount, pfTablesAddrPrefix=pfTablesAddrPrefix, pfTimeoutsIcmpError=pfTimeoutsIcmpError, pfTimeoutsUdpMultiple=pfTimeoutsUdpMultiple, pfTablesTblPktsInBlock=pfTablesTblPktsInBlock, pfTablesTblBytesOutXPass=pfTablesTblBytesOutXPass, pfAltqQueueDescr=pfAltqQueueDescr, pfStateTableInserts=pfStateTableInserts, pfSrcNodesCount=pfSrcNodesCount, pfLimitsStates=pfLimitsStates, pfCounter=pfCounter, pfLogInterfaceIp4PktsOutPass=pfLogInterfaceIp4PktsOutPass, pfLogInterfaceIp6PktsInPass=pfLogInterfaceIp6PktsInPass, pfLabelsLblTable=pfLabelsLblTable, pfInterfacesIfType=pfInterfacesIfType, pfSrcNodesInserts=pfSrcNodesInserts, pfInterfacesIfEntry=pfInterfacesIfEntry, pfInterfacesIf4PktsInBlock=pfInterfacesIf4PktsInBlock, pfTablesAddrBytesOutPass=pfTablesAddrBytesOutPass, pfTablesAddrPktsOutPass=pfTablesAddrPktsOutPass, pfInterfacesIf6PktsInPass=pfInterfacesIf6PktsInPass, pfTimeoutsTcpOpening=pfTimeoutsTcpOpening, pfInterfacesIf4PktsInPass=pfInterfacesIf4PktsInPass, pfInterfacesIf4PktsOutBlock=pfInterfacesIf4PktsOutBlock, pfTablesTblPktsOutBlock=pfTablesTblPktsOutBlock, pfCounterBadOffset=pfCounterBadOffset, pfTablesAddrPktsOutBlock=pfTablesAddrPktsOutBlock, pfStatusRunning=pfStatusRunning, pfInterfacesIfTZero=pfInterfacesIfTZero, pfLogInterfaceIp4PktsInPass=pfLogInterfaceIp4PktsInPass, pfAltqQueueEntry=pfAltqQueueEntry, PYSNMP_MODULE_ID=begemotPf, pfTimeoutsTcpFirst=pfTimeoutsTcpFirst, pfInterfacesIf6BytesInBlock=pfInterfacesIf6BytesInBlock, pfTablesAddrEntry=pfTablesAddrEntry, pfStatusDebug=pfStatusDebug, pfTablesAddrNet=pfTablesAddrNet, pfLogInterfaceIp4BytesOut=pfLogInterfaceIp4BytesOut, pfTablesAddrNetType=pfTablesAddrNetType, pfTablesAddrPktsInPass=pfTablesAddrPktsInPass, pfTablesTblPktsOutXPass=pfTablesTblPktsOutXPass, pfTimeoutsAdaptiveStart=pfTimeoutsAdaptiveStart, pfSrcNodes=pfSrcNodes, pfTablesTblBytesInPass=pfTablesTblBytesInPass, pfLogInterfaceIp4PktsInDrop=pfLogInterfaceIp4PktsInDrop, pfTimeoutsFragment=pfTimeoutsFragment, pfLogInterface=pfLogInterface, pfLogInterfaceIp4PktsOutDrop=pfLogInterfaceIp4PktsOutDrop, pfTablesTblIndex=pfTablesTblIndex, pfTimeoutsTcpClosing=pfTimeoutsTcpClosing, pfCounterShort=pfCounterShort, pfInterfacesIf4PktsOutPass=pfInterfacesIf4PktsOutPass, pfTablesTblTable=pfTablesTblTable, pfCounterMemDrop=pfCounterMemDrop, pfLabelsLblPktsOut=pfLabelsLblPktsOut, pfLabelsLblBytesIn=pfLabelsLblBytesIn, pfStatusHostId=pfStatusHostId, pfCounterNormalize=pfCounterNormalize, pfTablesTblRefsRule=pfTablesTblRefsRule, pfTablesTblPktsInPass=pfTablesTblPktsInPass, pfCounterMatch=pfCounterMatch, pfTablesTblBytesInXPass=pfTablesTblBytesInXPass, pfTablesTblPktsInXPass=pfTablesTblPktsInXPass, pfTablesAddrTZero=pfTablesAddrTZero, pfLogInterfaceIp6PktsInDrop=pfLogInterfaceIp6PktsInDrop, pfLabelsLblBytesOut=pfLabelsLblBytesOut, pfLimits=pfLimits, pfLabelsLblPktsIn=pfLabelsLblPktsIn, pfCounterFragment=pfCounterFragment, pfLogInterfaceIp6BytesOut=pfLogInterfaceIp6BytesOut, pfTablesTblTZero=pfTablesTblTZero, pfTablesTblDescr=pfTablesTblDescr, pfInterfacesIf6PktsOutPass=pfInterfacesIf6PktsOutPass, pfTablesTblNumber=pfTablesTblNumber, pfInterfacesIf6PktsInBlock=pfInterfacesIf6PktsInBlock, pfTimeouts=pfTimeouts, pfTablesAddrIndex=pfTablesAddrIndex, pfSrcNodesSearches=pfSrcNodesSearches, pfTimeoutsTcpEstablished=pfTimeoutsTcpEstablished, begemotPfObjects=begemotPfObjects, pfTimeoutsIcmpFirst=pfTimeoutsIcmpFirst, pfTablesTblBytesOutPass=pfTablesTblBytesOutPass, pfAltqQueueLimit=pfAltqQueueLimit, pfInterfacesIf6BytesOutPass=pfInterfacesIf6BytesOutPass, pfInterfacesIfRefsRule=pfInterfacesIfRefsRule, pfAltqQueueTable=pfAltqQueueTable, pfLimitsSrcNodes=pfLimitsSrcNodes, pfTables=pfTables, pfInterfacesIf6BytesInPass=pfInterfacesIf6BytesInPass, pfStateTableRemovals=pfStateTableRemovals, pfLogInterfaceIp6BytesIn=pfLogInterfaceIp6BytesIn, pfTablesAddrBytesInBlock=pfTablesAddrBytesInBlock, pfInterfacesIfDescr=pfInterfacesIfDescr, pfStateTable=pfStateTable, pfAltq=pfAltq, pfAltqQueueNumber=pfAltqQueueNumber, pfInterfacesIf6BytesOutBlock=pfInterfacesIf6BytesOutBlock, pfLabels=pfLabels, pfLabelsLblIndex=pfLabelsLblIndex, pfLabelsLblNumber=pfLabelsLblNumber, pfTimeoutsSrcNode=pfTimeoutsSrcNode, pfInterfacesIf6PktsOutBlock=pfInterfacesIf6PktsOutBlock, pfAltqQueueIndex=pfAltqQueueIndex, pfTablesAddrPktsInBlock=pfTablesAddrPktsInBlock, pfTimeoutsOtherSingle=pfTimeoutsOtherSingle, pfTablesAddrBytesInPass=pfTablesAddrBytesInPass, pfInterfacesIfIndex=pfInterfacesIfIndex, pfTablesTblPktsOutPass=pfTablesTblPktsOutPass, pfLogInterfaceIp4BytesIn=pfLogInterfaceIp4BytesIn, pfSrcNodesRemovals=pfSrcNodesRemovals, pfTablesAddrTable=pfTablesAddrTable, pfTimeoutsOtherMultiple=pfTimeoutsOtherMultiple, pfInterfacesIfNumber=pfInterfacesIfNumber, pfTimeoutsUdpSingle=pfTimeoutsUdpSingle, pfTablesTblBytesOutBlock=pfTablesTblBytesOutBlock)
