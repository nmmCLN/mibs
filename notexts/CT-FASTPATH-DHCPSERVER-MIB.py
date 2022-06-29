#
# PySNMP MIB module CT-FASTPATH-DHCPSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FASTPATH-DHCPSERVER-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:56 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ctDhcpServerExpMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDhcpServerExpMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
TruthValue, TextualConvention, DisplayString, MacAddress, RowPointer, StorageType, PhysAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "MacAddress", "RowPointer", "StorageType", "PhysAddress", "RowStatus")
ctFastPathDHCPServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1))
if mibBuilder.loadTexts: ctFastPathDHCPServerMIB.setLastUpdated('200601161932Z')
if mibBuilder.loadTexts: ctFastPathDHCPServerMIB.setOrganization('Enterasys Networks, Inc.')
ctAgentDhcpServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1))
ctAgentDhcpServerAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerAdminMode.setStatus('current')
ctAgentDhcpServerPingPktNos = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2, 10), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPingPktNos.setStatus('current')
ctAgentDhcpServerAutomaticBindingsNos = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerAutomaticBindingsNos.setStatus('current')
ctAgentDhcpServerExpiredBindingsNos = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerExpiredBindingsNos.setStatus('current')
ctAgentDhcpServerMalformedMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerMalformedMessagesReceived.setStatus('current')
ctAgentDhcpServerDISCOVERMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerDISCOVERMessagesReceived.setStatus('current')
ctAgentDhcpServerREQUESTMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerREQUESTMessagesReceived.setStatus('current')
ctAgentDhcpServerDECLINEMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerDECLINEMessagesReceived.setStatus('current')
ctAgentDhcpServerRELEASEMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerRELEASEMessagesReceived.setStatus('current')
ctAgentDhcpServerINFORMMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerINFORMMessagesReceived.setStatus('current')
ctAgentDhcpServerOFFERMessagesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerOFFERMessagesSent.setStatus('current')
ctAgentDhcpServerACKMessagesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerACKMessagesSent.setStatus('current')
ctAgentDhcpServerNAKMessagesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerNAKMessagesSent.setStatus('current')
ctAgentDhcpServerClearStatistics = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerClearStatistics.setStatus('current')
ctAgentDhcpServerBootpAutomatic = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerBootpAutomatic.setStatus('current')
ctAgentDhcpServerPoolConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2))
ctAgentDhcpServerPoolNameCreate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 1), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 31), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolNameCreate.setStatus('current')
ctAgentDhcpServerPoolConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2), )
if mibBuilder.loadTexts: ctAgentDhcpServerPoolConfigTable.setStatus('current')
ctAgentDhcpServerPoolConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolIndex"))
if mibBuilder.loadTexts: ctAgentDhcpServerPoolConfigEntry.setStatus('current')
ctAgentDhcpServerPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolIndex.setStatus('current')
ctAgentDhcpServerPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolName.setStatus('current')
ctAgentDhcpServerPoolDefRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolDefRouter.setStatus('current')
ctAgentDhcpServerPoolDNSServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolDNSServer.setStatus('current')
ctAgentDhcpServerPoolLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolLeaseTime.setStatus('current')
ctAgentDhcpServerPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("un-allocated", 0), ("dynamic", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolType.setStatus('current')
ctAgentDhcpServerPoolNetbiosNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolNetbiosNameServer.setStatus('current')
ctAgentDhcpServerPoolNetbiosNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("none", 0), ("b-node", 1), ("p-node", 2), ("m-node", 4), ("h-node", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolNetbiosNodeType.setStatus('current')
ctAgentDhcpServerPoolNextServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolNextServer.setStatus('current')
ctAgentDhcpServerPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolDomainName.setStatus('current')
ctAgentDhcpServerPoolBootfile = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolBootfile.setStatus('current')
ctAgentDhcpServerPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 2, 1, 12), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolRowStatus.setStatus('current')
ctAgentDhcpServerPoolAllocationTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3), )
if mibBuilder.loadTexts: ctAgentDhcpServerPoolAllocationTable.setStatus('current')
ctAgentDhcpServerPoolAllocationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1), )
ctAgentDhcpServerPoolConfigEntry.registerAugmentions(("CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolAllocationEntry"))
ctAgentDhcpServerPoolAllocationEntry.setIndexNames(*ctAgentDhcpServerPoolConfigEntry.getIndexNames())
if mibBuilder.loadTexts: ctAgentDhcpServerPoolAllocationEntry.setStatus('current')
ctAgentDhcpServerPoolAllocationName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolAllocationName.setStatus('current')
ctAgentDhcpServerDynamicPoolIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerDynamicPoolIpAddress.setStatus('current')
ctAgentDhcpServerDynamicPoolIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerDynamicPoolIpMask.setStatus('current')
ctAgentDhcpServerDynamicPoolIpPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerDynamicPoolIpPrefixLength.setStatus('current')
ctAgentDhcpServerPoolAllocationType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("un-allocated", 0), ("dynamic", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolAllocationType.setStatus('current')
ctAgentDhcpServerManualPoolClientIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolClientIdentifier.setStatus('current')
ctAgentDhcpServerManualPoolClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolClientName.setStatus('current')
ctAgentDhcpServerManualPoolClientHWAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolClientHWAddr.setStatus('current')
ctAgentDhcpServerManualPoolClientHWType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6))).clone(namedValues=NamedValues(("ethernet", 1), ("ieee802", 6))).clone('ethernet')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolClientHWType.setStatus('current')
ctAgentDhcpServerManualPoolIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolIpAddress.setStatus('current')
ctAgentDhcpServerManualPoolIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolIpMask.setStatus('current')
ctAgentDhcpServerManualPoolIpPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerManualPoolIpPrefixLength.setStatus('current')
ctAgentDhcpServerExcludedAddressRangeCreate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedAddressRangeCreate.setStatus('current')
ctAgentDhcpServerExcludedAddressRangeTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5), )
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedAddressRangeTable.setStatus('current')
ctAgentDhcpServerExcludedAddressRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerExcludedRangeIndex"))
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedAddressRangeEntry.setStatus('current')
ctAgentDhcpServerExcludedRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedRangeIndex.setStatus('current')
ctAgentDhcpServerExcludedStartIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedStartIpAddress.setStatus('current')
ctAgentDhcpServerExcludedEndIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedEndIpAddress.setStatus('current')
ctAgentDhcpServerExcludedAddressRangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 5, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerExcludedAddressRangeStatus.setStatus('current')
ctAgentDhcpServerPoolOptionCreate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionCreate.setStatus('current')
ctAgentDhcpServerPoolOptionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7), )
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionTable.setStatus('current')
ctAgentDhcpServerPoolOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolOptionIndex"), (0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerPoolOptionCode"))
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionEntry.setStatus('current')
ctAgentDhcpServerPoolOptionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionIndex.setStatus('current')
ctAgentDhcpServerPoolOptionCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionCode.setStatus('current')
ctAgentDhcpServerOptionPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerOptionPoolName.setStatus('current')
ctAgentDhcpServerPoolOptionAsciiData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 441))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionAsciiData.setStatus('current')
ctAgentDhcpServerPoolOptionHexData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1324))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionHexData.setStatus('current')
ctAgentDhcpServerPoolOptionIpAddressData = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionIpAddressData.setStatus('current')
ctAgentDhcpServerPoolOptionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 2, 7, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerPoolOptionStatus.setStatus('current')
ctAgentDhcpServerLeaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3))
ctAgentDhcpServerLeaseClearAllBindings = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseClearAllBindings.setStatus('current')
ctAgentDhcpServerLeaseTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2), )
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseTable.setStatus('current')
ctAgentDhcpServerLeaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerLeaseIPAddress"))
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseEntry.setStatus('current')
ctAgentDhcpServerLeaseIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseIPAddress.setStatus('current')
ctAgentDhcpServerLeaseIPMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseIPMask.setStatus('current')
ctAgentDhcpServerLeaseHWAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseHWAddress.setStatus('current')
ctAgentDhcpServerLeaseRemainingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseRemainingTime.setStatus('current')
ctAgentDhcpServerLeaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseType.setStatus('current')
ctAgentDhcpServerLeaseStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 3, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerLeaseStatus.setStatus('current')
ctAgentDhcpServerAddressConflictGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4))
ctAgentDhcpServerClearAllAddressConflicts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerClearAllAddressConflicts.setStatus('current')
ctAgentDhcpServerAddressConflictLogging = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictLogging.setStatus('current')
ctAgentDhcpServerAddressConflictTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3), )
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictTable.setStatus('current')
ctAgentDhcpServerAddressConflictEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1), ).setIndexNames((0, "CT-FASTPATH-DHCPSERVER-MIB", "ctAgentDhcpServerAddressConflictIP"))
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictEntry.setStatus('current')
ctAgentDhcpServerAddressConflictIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictIP.setStatus('current')
ctAgentDhcpServerAddressConflictDetectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ping", 1), ("gratuitousArp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictDetectionType.setStatus('current')
ctAgentDhcpServerAddressConflictDetectionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictDetectionTime.setStatus('current')
ctAgentDhcpServerAddressConflictStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 32, 1, 4, 3, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctAgentDhcpServerAddressConflictStatus.setStatus('current')
mibBuilder.exportSymbols("CT-FASTPATH-DHCPSERVER-MIB", ctAgentDhcpServerExcludedStartIpAddress=ctAgentDhcpServerExcludedStartIpAddress, ctAgentDhcpServerLeaseTable=ctAgentDhcpServerLeaseTable, ctAgentDhcpServerPoolDefRouter=ctAgentDhcpServerPoolDefRouter, ctAgentDhcpServerPoolLeaseTime=ctAgentDhcpServerPoolLeaseTime, ctAgentDhcpServerManualPoolClientHWAddr=ctAgentDhcpServerManualPoolClientHWAddr, ctAgentDhcpServerPoolBootfile=ctAgentDhcpServerPoolBootfile, ctAgentDhcpServerPoolDomainName=ctAgentDhcpServerPoolDomainName, ctAgentDhcpServerManualPoolIpMask=ctAgentDhcpServerManualPoolIpMask, ctAgentDhcpServerExcludedRangeIndex=ctAgentDhcpServerExcludedRangeIndex, ctAgentDhcpServerPoolOptionCode=ctAgentDhcpServerPoolOptionCode, ctAgentDhcpServerDynamicPoolIpAddress=ctAgentDhcpServerDynamicPoolIpAddress, ctAgentDhcpServerAddressConflictGroup=ctAgentDhcpServerAddressConflictGroup, ctAgentDhcpServerPoolConfigEntry=ctAgentDhcpServerPoolConfigEntry, ctAgentDhcpServerPoolNetbiosNodeType=ctAgentDhcpServerPoolNetbiosNodeType, ctAgentDhcpServerRELEASEMessagesReceived=ctAgentDhcpServerRELEASEMessagesReceived, ctAgentDhcpServerPoolType=ctAgentDhcpServerPoolType, ctAgentDhcpServerAddressConflictLogging=ctAgentDhcpServerAddressConflictLogging, ctAgentDhcpServerPoolNameCreate=ctAgentDhcpServerPoolNameCreate, ctAgentDhcpServerLeaseGroup=ctAgentDhcpServerLeaseGroup, ctAgentDhcpServerPoolRowStatus=ctAgentDhcpServerPoolRowStatus, ctAgentDhcpServerPoolOptionIndex=ctAgentDhcpServerPoolOptionIndex, ctAgentDhcpServerExcludedAddressRangeStatus=ctAgentDhcpServerExcludedAddressRangeStatus, ctAgentDhcpServerPoolNextServer=ctAgentDhcpServerPoolNextServer, ctAgentDhcpServerExpiredBindingsNos=ctAgentDhcpServerExpiredBindingsNos, ctAgentDhcpServerPoolOptionCreate=ctAgentDhcpServerPoolOptionCreate, ctAgentDhcpServerExcludedAddressRangeTable=ctAgentDhcpServerExcludedAddressRangeTable, ctAgentDhcpServerDynamicPoolIpMask=ctAgentDhcpServerDynamicPoolIpMask, ctAgentDhcpServerAddressConflictStatus=ctAgentDhcpServerAddressConflictStatus, ctAgentDhcpServerExcludedAddressRangeEntry=ctAgentDhcpServerExcludedAddressRangeEntry, ctAgentDhcpServerPoolAllocationEntry=ctAgentDhcpServerPoolAllocationEntry, ctAgentDhcpServerLeaseIPAddress=ctAgentDhcpServerLeaseIPAddress, ctAgentDhcpServerREQUESTMessagesReceived=ctAgentDhcpServerREQUESTMessagesReceived, ctAgentDhcpServerManualPoolClientIdentifier=ctAgentDhcpServerManualPoolClientIdentifier, ctAgentDhcpServerExcludedEndIpAddress=ctAgentDhcpServerExcludedEndIpAddress, ctAgentDhcpServerClearAllAddressConflicts=ctAgentDhcpServerClearAllAddressConflicts, ctAgentDhcpServerDECLINEMessagesReceived=ctAgentDhcpServerDECLINEMessagesReceived, ctAgentDhcpServerNAKMessagesSent=ctAgentDhcpServerNAKMessagesSent, ctAgentDhcpServerLeaseEntry=ctAgentDhcpServerLeaseEntry, ctAgentDhcpServerACKMessagesSent=ctAgentDhcpServerACKMessagesSent, ctAgentDhcpServerAddressConflictTable=ctAgentDhcpServerAddressConflictTable, ctAgentDhcpServerGroup=ctAgentDhcpServerGroup, ctAgentDhcpServerAddressConflictDetectionType=ctAgentDhcpServerAddressConflictDetectionType, ctAgentDhcpServerAddressConflictDetectionTime=ctAgentDhcpServerAddressConflictDetectionTime, PYSNMP_MODULE_ID=ctFastPathDHCPServerMIB, ctAgentDhcpServerLeaseType=ctAgentDhcpServerLeaseType, ctAgentDhcpServerOptionPoolName=ctAgentDhcpServerOptionPoolName, ctAgentDhcpServerOFFERMessagesSent=ctAgentDhcpServerOFFERMessagesSent, ctAgentDhcpServerPoolOptionIpAddressData=ctAgentDhcpServerPoolOptionIpAddressData, ctAgentDhcpServerManualPoolClientName=ctAgentDhcpServerManualPoolClientName, ctAgentDhcpServerAdminMode=ctAgentDhcpServerAdminMode, ctAgentDhcpServerBootpAutomatic=ctAgentDhcpServerBootpAutomatic, ctAgentDhcpServerAutomaticBindingsNos=ctAgentDhcpServerAutomaticBindingsNos, ctAgentDhcpServerClearStatistics=ctAgentDhcpServerClearStatistics, ctAgentDhcpServerManualPoolClientHWType=ctAgentDhcpServerManualPoolClientHWType, ctAgentDhcpServerAddressConflictEntry=ctAgentDhcpServerAddressConflictEntry, ctAgentDhcpServerPingPktNos=ctAgentDhcpServerPingPktNos, ctAgentDhcpServerLeaseStatus=ctAgentDhcpServerLeaseStatus, ctAgentDhcpServerPoolDNSServer=ctAgentDhcpServerPoolDNSServer, ctAgentDhcpServerLeaseRemainingTime=ctAgentDhcpServerLeaseRemainingTime, ctAgentDhcpServerPoolConfigTable=ctAgentDhcpServerPoolConfigTable, ctAgentDhcpServerPoolOptionStatus=ctAgentDhcpServerPoolOptionStatus, ctAgentDhcpServerPoolName=ctAgentDhcpServerPoolName, ctAgentDhcpServerManualPoolIpPrefixLength=ctAgentDhcpServerManualPoolIpPrefixLength, ctFastPathDHCPServerMIB=ctFastPathDHCPServerMIB, ctAgentDhcpServerLeaseClearAllBindings=ctAgentDhcpServerLeaseClearAllBindings, ctAgentDhcpServerPoolAllocationType=ctAgentDhcpServerPoolAllocationType, ctAgentDhcpServerLeaseHWAddress=ctAgentDhcpServerLeaseHWAddress, ctAgentDhcpServerINFORMMessagesReceived=ctAgentDhcpServerINFORMMessagesReceived, ctAgentDhcpServerPoolConfigGroup=ctAgentDhcpServerPoolConfigGroup, ctAgentDhcpServerPoolAllocationTable=ctAgentDhcpServerPoolAllocationTable, ctAgentDhcpServerPoolIndex=ctAgentDhcpServerPoolIndex, ctAgentDhcpServerAddressConflictIP=ctAgentDhcpServerAddressConflictIP, ctAgentDhcpServerDISCOVERMessagesReceived=ctAgentDhcpServerDISCOVERMessagesReceived, ctAgentDhcpServerPoolOptionEntry=ctAgentDhcpServerPoolOptionEntry, ctAgentDhcpServerManualPoolIpAddress=ctAgentDhcpServerManualPoolIpAddress, ctAgentDhcpServerMalformedMessagesReceived=ctAgentDhcpServerMalformedMessagesReceived, ctAgentDhcpServerPoolOptionTable=ctAgentDhcpServerPoolOptionTable, ctAgentDhcpServerPoolOptionAsciiData=ctAgentDhcpServerPoolOptionAsciiData, ctAgentDhcpServerPoolAllocationName=ctAgentDhcpServerPoolAllocationName, ctAgentDhcpServerLeaseIPMask=ctAgentDhcpServerLeaseIPMask, ctAgentDhcpServerPoolNetbiosNameServer=ctAgentDhcpServerPoolNetbiosNameServer, ctAgentDhcpServerDynamicPoolIpPrefixLength=ctAgentDhcpServerDynamicPoolIpPrefixLength, ctAgentDhcpServerPoolOptionHexData=ctAgentDhcpServerPoolOptionHexData, ctAgentDhcpServerExcludedAddressRangeCreate=ctAgentDhcpServerExcludedAddressRangeCreate)
