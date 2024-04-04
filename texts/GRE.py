#
# PySNMP MIB module GRE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/GRE
# Produced by pysmi-1.1.12 at Thu Apr  4 09:22:09 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, IpAddress, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, ModuleIdentity, Integer32, enterprises, iso, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "IpAddress", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "ModuleIdentity", "Integer32", "enterprises", "iso", "Counter32", "Bits")
DisplayString, TruthValue, RowStatus, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention", "MacAddress")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1))
greMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11))
greInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1))
if mibBuilder.loadTexts: greInfo.setLastUpdated('201502110000Z')
if mibBuilder.loadTexts: greInfo.setOrganization('PEPLINK')
if mibBuilder.loadTexts: greInfo.setContactInfo('')
if mibBuilder.loadTexts: greInfo.setDescription('MIB module for GRE.')
greStatusTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1), )
if mibBuilder.loadTexts: greStatusTable.setStatus('current')
if mibBuilder.loadTexts: greStatusTable.setDescription('GRE status table')
greStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1), ).setIndexNames((0, "GRE", "greStatusId"))
if mibBuilder.loadTexts: greStatusEntry.setStatus('current')
if mibBuilder.loadTexts: greStatusEntry.setDescription('An entry in the greStatusTable')
greStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusId.setStatus('current')
if mibBuilder.loadTexts: greStatusId.setDescription('GRE ID.')
greStatusProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusProfileName.setStatus('current')
if mibBuilder.loadTexts: greStatusProfileName.setDescription('GRE profile name.')
greStatusConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disconnected", 0), ("connected", 1), ("connecting", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusConnectionState.setStatus('current')
if mibBuilder.loadTexts: greStatusConnectionState.setDescription('GRE connection state.')
greStatusLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusLocalIpAddress.setStatus('current')
if mibBuilder.loadTexts: greStatusLocalIpAddress.setDescription('GRE local IP.')
greStatusRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusRemoteIpAddress.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteIpAddress.setDescription('GRE remote IP.')
greStatusTunnelLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusTunnelLocalIpAddress.setStatus('current')
if mibBuilder.loadTexts: greStatusTunnelLocalIpAddress.setDescription('GRE tunnel local IP.')
greStatusTunnelRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusTunnelRemoteIpAddress.setStatus('current')
if mibBuilder.loadTexts: greStatusTunnelRemoteIpAddress.setDescription('GRE tunnel remote IP.')
greStatusRemoteNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2), )
if mibBuilder.loadTexts: greStatusRemoteNetworkTable.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteNetworkTable.setDescription('GRE status remote network table')
greStatusRemoteNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1), ).setIndexNames((0, "GRE", "greStatusId"), (0, "GRE", "greStatusRemoteNetworkId"))
if mibBuilder.loadTexts: greStatusRemoteNetworkEntry.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteNetworkEntry.setDescription('An entry in the greStatusRemoteNetworkTable')
greStatusRemoteNetworkId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusRemoteNetworkId.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteNetworkId.setDescription('GRE remote network ID.')
greStatusRemoteNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusRemoteNetwork.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteNetwork.setDescription('GRE remote network IP.')
greStatusRemoteSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusRemoteSubnet.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteSubnet.setDescription('GRE remote network subnet.')
mibBuilder.exportSymbols("GRE", greMib=greMib, greStatusProfileName=greStatusProfileName, peplink=peplink, greStatusRemoteNetworkId=greStatusRemoteNetworkId, greStatusRemoteNetwork=greStatusRemoteNetwork, greStatusLocalIpAddress=greStatusLocalIpAddress, greInfo=greInfo, greStatusTunnelRemoteIpAddress=greStatusTunnelRemoteIpAddress, greStatusTunnelLocalIpAddress=greStatusTunnelLocalIpAddress, generalMib=generalMib, greStatusConnectionState=greStatusConnectionState, greStatusTable=greStatusTable, greStatusEntry=greStatusEntry, productMib=productMib, greStatusRemoteIpAddress=greStatusRemoteIpAddress, greStatusRemoteNetworkEntry=greStatusRemoteNetworkEntry, PYSNMP_MODULE_ID=greInfo, greStatusId=greStatusId, greStatusRemoteSubnet=greStatusRemoteSubnet, greStatusRemoteNetworkTable=greStatusRemoteNetworkTable)
