#
# PySNMP MIB module WAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/WAN
# Produced by pysmi-1.1.8 at Sat Jan 15 20:31:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Integer32, Counter64, TimeTicks, IpAddress, Unsigned32, Gauge32, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Bits, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter64", "TimeTicks", "IpAddress", "Unsigned32", "Gauge32", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "ModuleIdentity")
RowStatus, TruthValue, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention", "MacAddress")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
wan_status = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 2)).setLabel("wan-status")
if mibBuilder.loadTexts: wan_status.setLastUpdated('201609060000Z')
if mibBuilder.loadTexts: wan_status.setOrganization('PEPLINK')
class PortSpeedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

wanStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 2, 1))
wanNum = MibScalar((1, 3, 6, 1, 4, 1, 23695, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNum.setStatus('current')
wanTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2), )
if mibBuilder.loadTexts: wanTable.setStatus('current')
wanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2, 1), ).setIndexNames((0, "WAN", "wanId"))
if mibBuilder.loadTexts: wanEntry.setStatus('current')
wanId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanId.setStatus('current')
wanName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanName.setStatus('current')
wanState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unknown", 0), ("disabled", 1), ("disconnected", 2), ("connected", 3), ("connecting", 4), ("activating", 5), ("health-check-fail", 6), ("disconnected-manually", 7), ("standby", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanState.setStatus('current')
wanHealthCheckState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("fail", 0), ("success", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanHealthCheckState.setStatus('current')
wanSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanSignal.setStatus('current')
wanCellID = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanCellID.setStatus('current')
wanPdpConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 0), ("pdp-ip", 1), ("pdp-ppp", 2), ("pdp-ipv6", 3), ("pdp-ipv4v6", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanPdpConnection.setStatus('current')
wanNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3))
wanNetworkIpTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 1), )
if mibBuilder.loadTexts: wanNetworkIpTable.setStatus('current')
wanNetworkIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 1, 1), ).setIndexNames((0, "WAN", "wanId"), (0, "WAN", "wanNetworkIpId"))
if mibBuilder.loadTexts: wanNetworkIpEntry.setStatus('current')
wanNetworkIpId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkIpId.setStatus('current')
wanNetworkIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("dhcp", 0), ("static", 1), ("pppoe", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkIpType.setStatus('current')
wanNetworkIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkIpAddress.setStatus('current')
wanNetworkSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkSubnetMask.setStatus('current')
wanNetworkDnsTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 2), )
if mibBuilder.loadTexts: wanNetworkDnsTable.setStatus('current')
wanNetworkDnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 2, 1), ).setIndexNames((0, "WAN", "wanId"), (0, "WAN", "wanNetworkDnsId"))
if mibBuilder.loadTexts: wanNetworkDnsEntry.setStatus('current')
wanNetworkDnsId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkDnsId.setStatus('current')
wanNetworkDnsServer = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkDnsServer.setStatus('current')
wanNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 3), )
if mibBuilder.loadTexts: wanNetworkTable.setStatus('current')
wanNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 3, 1), ).setIndexNames((0, "WAN", "wanId"))
if mibBuilder.loadTexts: wanNetworkEntry.setStatus('current')
wanNetworkGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 3, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanNetworkGateway.setStatus('current')
wanDataUsageTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 2, 1, 4), )
if mibBuilder.loadTexts: wanDataUsageTable.setStatus('current')
wanDataUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 2, 1, 4, 1), ).setIndexNames((0, "WAN", "wanId"), (0, "WAN", "dataTypeID"))
if mibBuilder.loadTexts: wanDataUsageEntry.setStatus('current')
dataTypeID = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 3))).clone(namedValues=NamedValues(("daily", 0), ("monthly", 1), ("sinceLastReboot", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataTypeID.setStatus('current')
wanDataUsageTxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 4, 1, 2), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: wanDataUsageTxByte.setStatus('current')
wanDataUsageRxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 4, 1, 3), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: wanDataUsageRxByte.setStatus('current')
portWanSpeedTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 2, 1, 5), )
if mibBuilder.loadTexts: portWanSpeedTable.setStatus('current')
portWanSpeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 2, 1, 5, 1), ).setIndexNames((0, "WAN", "portWanSpeedIndex"))
if mibBuilder.loadTexts: portWanSpeedEntry.setStatus('current')
portWanSpeedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portWanSpeedIndex.setStatus('current')
portWanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 1, 5, 1, 2), PortSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portWanSpeed.setStatus('current')
wanOverallStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 2, 2))
wanOverallDataUsageTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 2, 2, 1), )
if mibBuilder.loadTexts: wanOverallDataUsageTable.setStatus('current')
wanOverallDataUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 2, 2, 1, 1), ).setIndexNames((0, "WAN", "wanOverallDataTypeID"))
if mibBuilder.loadTexts: wanOverallDataUsageEntry.setStatus('current')
wanOverallDataTypeID = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 4))).clone(namedValues=NamedValues(("sinceLastReboot", 3), ("sinceInstallation", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanOverallDataTypeID.setStatus('current')
wanOverallDataUsageTxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 2, 1, 1, 2), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: wanOverallDataUsageTxByte.setStatus('current')
wanOverallDataUsageRxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 2, 2, 1, 1, 3), Counter64()).setUnits('MB').setMaxAccess("readonly")
if mibBuilder.loadTexts: wanOverallDataUsageRxByte.setStatus('current')
mibBuilder.exportSymbols("WAN", wanNetworkIpEntry=wanNetworkIpEntry, wanNetworkIpType=wanNetworkIpType, portWanSpeedIndex=portWanSpeedIndex, wanName=wanName, wanEntry=wanEntry, wanNetwork=wanNetwork, wanSignal=wanSignal, wanOverallDataTypeID=wanOverallDataTypeID, wanNetworkSubnetMask=wanNetworkSubnetMask, wanOverallDataUsageTable=wanOverallDataUsageTable, wanNetworkIpTable=wanNetworkIpTable, wanNum=wanNum, PortSpeedType=PortSpeedType, wanNetworkTable=wanNetworkTable, wanNetworkDnsServer=wanNetworkDnsServer, PYSNMP_MODULE_ID=wan_status, peplink=peplink, wanTable=wanTable, wanNetworkEntry=wanNetworkEntry, wanOverallDataUsageRxByte=wanOverallDataUsageRxByte, wanId=wanId, portWanSpeedEntry=portWanSpeedEntry, wanNetworkDnsTable=wanNetworkDnsTable, wan_status=wan_status, portWanSpeed=portWanSpeed, wanPdpConnection=wanPdpConnection, wanNetworkDnsId=wanNetworkDnsId, wanState=wanState, wanDataUsageTxByte=wanDataUsageTxByte, wanStatus=wanStatus, wanDataUsageRxByte=wanDataUsageRxByte, wanOverallStatus=wanOverallStatus, wanDataUsageTable=wanDataUsageTable, dataTypeID=dataTypeID, wanOverallDataUsageTxByte=wanOverallDataUsageTxByte, portWanSpeedTable=portWanSpeedTable, wanCellID=wanCellID, wanHealthCheckState=wanHealthCheckState, wanNetworkDnsEntry=wanNetworkDnsEntry, wanOverallDataUsageEntry=wanOverallDataUsageEntry, wanNetworkIpAddress=wanNetworkIpAddress, wanDataUsageEntry=wanDataUsageEntry, wanNetworkIpId=wanNetworkIpId, wanNetworkGateway=wanNetworkGateway)
