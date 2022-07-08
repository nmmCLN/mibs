#
# PySNMP MIB module IPSEC-VPN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/IPSEC-VPN
# Produced by pysmi-1.1.8 at Fri Jul  8 09:26:24 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Counter32, Counter64, MibIdentifier, ObjectIdentity, Unsigned32, enterprises, IpAddress, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter32", "Counter64", "MibIdentifier", "ObjectIdentity", "Unsigned32", "enterprises", "IpAddress", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Bits")
DisplayString, RowStatus, TextualConvention, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "MacAddress", "TruthValue")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1))
ipsecVpnMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13))
if mibBuilder.loadTexts: ipsecVpnMib.setLastUpdated('201812181200Z')
if mibBuilder.loadTexts: ipsecVpnMib.setOrganization('PEPLINK')
ipsecVpnStatusTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1), )
if mibBuilder.loadTexts: ipsecVpnStatusTable.setStatus('current')
ipsecVpnStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1), ).setIndexNames((0, "IPSEC-VPN", "ipsecVpnStatusId"))
if mibBuilder.loadTexts: ipsecVpnStatusEntry.setStatus('current')
ipsecVpnStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnStatusId.setStatus('current')
ipsecVpnStatusProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnStatusProfileName.setStatus('current')
ipsecVpnStatusConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("standby", 0), ("connecting", 1), ("established", 2), ("partially-established", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnStatusConnectionState.setStatus('current')
ipsecVpnStatusWanName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnStatusWanName.setStatus('current')
ipsecVpnRouteStatusTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2), )
if mibBuilder.loadTexts: ipsecVpnRouteStatusTable.setStatus('current')
ipsecVpnRouteStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1), ).setIndexNames((0, "IPSEC-VPN", "ipsecVpnStatusId"), (0, "IPSEC-VPN", "ipsecVpnRouteStatusId"))
if mibBuilder.loadTexts: ipsecVpnRouteStatusEntry.setStatus('current')
ipsecVpnRouteStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusId.setStatus('current')
ipsecVpnRouteState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("down", 0), ("up", 1), ("standby", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteState.setStatus('current')
ipsecVpnRouteStatusLocalNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusLocalNetwork.setStatus('current')
ipsecVpnRouteStatusLocalSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusLocalSubnet.setStatus('current')
ipsecVpnRouteStatusRemoteNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusRemoteNetwork.setStatus('current')
ipsecVpnRouteStatusRemoteSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusRemoteSubnet.setStatus('current')
mibBuilder.exportSymbols("IPSEC-VPN", ipsecVpnStatusEntry=ipsecVpnStatusEntry, ipsecVpnRouteStatusRemoteSubnet=ipsecVpnRouteStatusRemoteSubnet, ipsecVpnStatusProfileName=ipsecVpnStatusProfileName, ipsecVpnStatusConnectionState=ipsecVpnStatusConnectionState, ipsecVpnMib=ipsecVpnMib, ipsecVpnRouteStatusId=ipsecVpnRouteStatusId, ipsecVpnRouteStatusEntry=ipsecVpnRouteStatusEntry, ipsecVpnStatusId=ipsecVpnStatusId, ipsecVpnStatusWanName=ipsecVpnStatusWanName, ipsecVpnStatusTable=ipsecVpnStatusTable, ipsecVpnRouteStatusLocalSubnet=ipsecVpnRouteStatusLocalSubnet, generalMib=generalMib, PYSNMP_MODULE_ID=ipsecVpnMib, productMib=productMib, ipsecVpnRouteStatusRemoteNetwork=ipsecVpnRouteStatusRemoteNetwork, peplink=peplink, ipsecVpnRouteState=ipsecVpnRouteState, ipsecVpnRouteStatusLocalNetwork=ipsecVpnRouteStatusLocalNetwork, ipsecVpnRouteStatusTable=ipsecVpnRouteStatusTable)
