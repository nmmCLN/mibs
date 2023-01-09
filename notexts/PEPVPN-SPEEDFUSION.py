#
# PySNMP MIB module PEPVPN-SPEEDFUSION (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/PEPVPN-SPEEDFUSION
# Produced by pysmi-1.1.8 at Mon Jan  9 10:35:57 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, NotificationType, Gauge32, ObjectIdentity, Unsigned32, Bits, Counter32, enterprises, TimeTicks, MibIdentifier, IpAddress, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "Counter32", "enterprises", "TimeTicks", "MibIdentifier", "IpAddress", "Counter64", "ModuleIdentity")
MacAddress, TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1))
pepvpnMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10))
pepvpn = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1))
if mibBuilder.loadTexts: pepvpn.setLastUpdated('201305140000Z')
if mibBuilder.loadTexts: pepvpn.setOrganization('PEPLINK')
pepVpnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1))
pepVpnStatusTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2), )
if mibBuilder.loadTexts: pepVpnStatusTable.setStatus('current')
pepVpnStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"))
if mibBuilder.loadTexts: pepVpnStatusEntry.setStatus('current')
pepVpnStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusId.setStatus('current')
pepVpnStatusProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusProfileName.setStatus('current')
pepVpnStatusConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("start", 0), ("authen", 1), ("tunnel", 2), ("route", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusConnectionState.setStatus('current')
pepVpnStatusEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("off", 1), ("aes256", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusEncryption.setStatus('current')
pepVpnStatusL2Bridging = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusL2Bridging.setStatus('current')
pepVpnStatusL2Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusL2Vlan.setStatus('current')
pepVpnRemotePeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnRemotePeerId.setStatus('current')
pepVpnRemotePeer = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnRemotePeer.setStatus('current')
pepVpnStatusWanTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 3), )
if mibBuilder.loadTexts: pepVpnStatusWanTable.setStatus('current')
pepVpnStatusWanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 3, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusWanId"))
if mibBuilder.loadTexts: pepVpnStatusWanEntry.setStatus('current')
pepVpnStatusWanId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanId.setStatus('current')
pepVpnStatusWanName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanName.setStatus('current')
pepVpnStatusWanTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanTxBytes.setStatus('current')
pepVpnStatusWanRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanRxBytes.setStatus('current')
pepVpnStatusWanDropPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanDropPackets.setStatus('current')
pepVpnStatusWanLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanLatency.setStatus('current')
pepVpnStatusRemoteNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 4), )
if mibBuilder.loadTexts: pepVpnStatusRemoteNetworkTable.setStatus('current')
pepVpnStatusRemoteNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 4, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusRemoteNetowrkId"))
if mibBuilder.loadTexts: pepVpnStatusRemoteNetworkEntry.setStatus('current')
pepVpnStatusRemoteNetowrkId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteNetowrkId.setStatus('current')
pepVpnStatusRemoteNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteNetwork.setStatus('current')
pepVpnStatusRemoteSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 10, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteSubnet.setStatus('current')
mibBuilder.exportSymbols("PEPVPN-SPEEDFUSION", pepVpnStatusL2Bridging=pepVpnStatusL2Bridging, pepVpnStatusRemoteNetworkTable=pepVpnStatusRemoteNetworkTable, pepVpnStatusRemoteSubnet=pepVpnStatusRemoteSubnet, pepVpnInfo=pepVpnInfo, pepVpnStatusWanEntry=pepVpnStatusWanEntry, pepVpnStatusId=pepVpnStatusId, generalMib=generalMib, pepVpnStatusWanDropPackets=pepVpnStatusWanDropPackets, pepVpnStatusWanTable=pepVpnStatusWanTable, pepvpnMib=pepvpnMib, pepVpnStatusEntry=pepVpnStatusEntry, pepVpnStatusRemoteNetowrkId=pepVpnStatusRemoteNetowrkId, pepVpnRemotePeer=pepVpnRemotePeer, pepVpnStatusWanName=pepVpnStatusWanName, pepVpnStatusWanRxBytes=pepVpnStatusWanRxBytes, pepVpnRemotePeerId=pepVpnRemotePeerId, pepVpnStatusL2Vlan=pepVpnStatusL2Vlan, pepVpnStatusConnectionState=pepVpnStatusConnectionState, pepVpnStatusWanTxBytes=pepVpnStatusWanTxBytes, pepVpnStatusEncryption=pepVpnStatusEncryption, pepVpnStatusRemoteNetworkEntry=pepVpnStatusRemoteNetworkEntry, pepvpn=pepvpn, pepVpnStatusTable=pepVpnStatusTable, PYSNMP_MODULE_ID=pepvpn, pepVpnStatusWanLatency=pepVpnStatusWanLatency, pepVpnStatusWanId=pepVpnStatusWanId, peplink=peplink, productMib=productMib, pepVpnStatusRemoteNetwork=pepVpnStatusRemoteNetwork, pepVpnStatusProfileName=pepVpnStatusProfileName)
