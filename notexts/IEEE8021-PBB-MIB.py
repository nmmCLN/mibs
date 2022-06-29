#
# PySNMP MIB module IEEE8021-PBB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-PBB-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:08 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ieee8021BridgeBasePortComponentId, ieee8021BridgeBasePort = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId", "ieee8021BridgeBasePort")
IEEE8021PriorityValue, IEEE8021PbbServiceIdentifier, IEEE8021PriorityCodePoint, ieee802dot1mibs, IEEE8021PbbServiceIdentifierOrUnassigned, IEEE8021PbbIngressEgress, IEEE8021BridgePortNumber, IEEE8021PbbComponentIdentifier = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PriorityValue", "IEEE8021PbbServiceIdentifier", "IEEE8021PriorityCodePoint", "ieee802dot1mibs", "IEEE8021PbbServiceIdentifierOrUnassigned", "IEEE8021PbbIngressEgress", "IEEE8021BridgePortNumber", "IEEE8021PbbComponentIdentifier")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Unsigned32, Counter64, NotificationType, TimeTicks, ObjectIdentity, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, Counter32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "Counter32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, StorageType, DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "StorageType", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
ieee8021PbbMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 9))
ieee8021PbbMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2011-02-27 00:00', '2008-11-18 00:00', '2008-10-15 00:00',))
if mibBuilder.loadTexts: ieee8021PbbMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021PbbMib.setOrganization('IEEE 802.1 Working Group')
ieee8021PbbNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 9, 0))
ieee8021PbbObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 9, 1))
ieee8021PbbConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 9, 2))
ieee8021PbbProviderBackboneBridge = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 9, 1, 1))
ieee8021PbbBackboneEdgeBridgeObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1))
ieee8021PbbBackboneEdgeBridgeAddress = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbBackboneEdgeBridgeAddress.setStatus('current')
ieee8021PbbBackboneEdgeBridgeName = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbBackboneEdgeBridgeName.setStatus('current')
ieee8021PbbNumberOfIComponents = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbNumberOfIComponents.setStatus('current')
ieee8021PbbNumberOfBComponents = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbNumberOfBComponents.setStatus('current')
ieee8021PbbNumberOfBebPorts = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbNumberOfBebPorts.setStatus('current')
ieee8021PbbNextAvailablePipIfIndex = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbNextAvailablePipIfIndex.setStatus('current')
ieee8021PbbVipTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2), )
if mibBuilder.loadTexts: ieee8021PbbVipTable.setStatus('current')
ieee8021PbbVipEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PbbVipEntry.setStatus('current')
ieee8021PbbVipPipIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbVipPipIfIndex.setStatus('current')
ieee8021PbbVipISid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 2), IEEE8021PbbServiceIdentifierOrUnassigned().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbVipISid.setStatus('current')
ieee8021PbbVipDefaultDstBMAC = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 3), MacAddress().clone(hexValue="001e83000001")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbVipDefaultDstBMAC.setStatus('current')
ieee8021PbbVipType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 4), IEEE8021PbbIngressEgress().clone(namedValues=NamedValues(("egress", 1), ("ingress", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbVipType.setStatus('deprecated')
ieee8021PbbVipRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbVipRowStatus.setStatus('current')
ieee8021PbbVipEnableConnectionId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbVipEnableConnectionId.setStatus('current')
ieee8021PbbISidToVipTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3), )
if mibBuilder.loadTexts: ieee8021PbbISidToVipTable.setStatus('current')
ieee8021PbbISidToVipEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3, 1), ).setIndexNames((0, "IEEE8021-PBB-MIB", "ieee8021PbbISidToVipISid"))
if mibBuilder.loadTexts: ieee8021PbbISidToVipEntry.setStatus('current')
ieee8021PbbISidToVipISid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3, 1, 1), IEEE8021PbbServiceIdentifier())
if mibBuilder.loadTexts: ieee8021PbbISidToVipISid.setStatus('current')
ieee8021PbbISidToVipComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3, 1, 2), IEEE8021PbbComponentIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbISidToVipComponentId.setStatus('current')
ieee8021PbbISidToVipPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3, 1, 3), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbISidToVipPort.setStatus('current')
ieee8021PbbPipTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4), )
if mibBuilder.loadTexts: ieee8021PbbPipTable.setStatus('current')
ieee8021PbbPipEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1), ).setIndexNames((0, "IEEE8021-PBB-MIB", "ieee8021PbbPipIfIndex"))
if mibBuilder.loadTexts: ieee8021PbbPipEntry.setStatus('current')
ieee8021PbbPipIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ieee8021PbbPipIfIndex.setStatus('current')
ieee8021PbbPipBMACAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbPipBMACAddress.setStatus('current')
ieee8021PbbPipName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbPipName.setStatus('current')
ieee8021PbbPipIComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 4), IEEE8021PbbComponentIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbPipIComponentId.setStatus('current')
ieee8021PbbPipVipMap = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbPipVipMap.setStatus('current')
ieee8021PbbPipVipMap1 = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbPipVipMap1.setStatus('current')
ieee8021PbbPipVipMap2 = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbPipVipMap2.setStatus('current')
ieee8021PbbPipVipMap3 = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbPipVipMap3.setStatus('current')
ieee8021PbbPipVipMap4 = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1537)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbPipVipMap4.setStatus('current')
ieee8021PbbPipRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbPipRowStatus.setStatus('current')
ieee8021PbbPipPriorityTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5), )
if mibBuilder.loadTexts: ieee8021PbbPipPriorityTable.setStatus('current')
ieee8021PbbPipPriorityEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5, 1), )
ieee8021PbbPipEntry.registerAugmentions(("IEEE8021-PBB-MIB", "ieee8021PbbPipPriorityEntry"))
ieee8021PbbPipPriorityEntry.setIndexNames(*ieee8021PbbPipEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021PbbPipPriorityEntry.setStatus('current')
ieee8021PbbPipPriorityCodePointSelection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5, 1, 1), IEEE8021PriorityCodePoint()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbPipPriorityCodePointSelection.setStatus('current')
ieee8021PbbPipUseDEI = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbPipUseDEI.setStatus('current')
ieee8021PbbPipRequireDropEncoding = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbPipRequireDropEncoding.setStatus('current')
ieee8021PbbPipDecodingTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6), )
if mibBuilder.loadTexts: ieee8021PbbPipDecodingTable.setStatus('current')
ieee8021PbbPipDecodingEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1), ).setIndexNames((0, "IEEE8021-PBB-MIB", "ieee8021PbbPipIfIndex"), (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingPriorityCodePointRow"), (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingPriorityCodePoint"))
if mibBuilder.loadTexts: ieee8021PbbPipDecodingEntry.setStatus('current')
ieee8021PbbPipDecodingPriorityCodePointRow = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1, 1), IEEE8021PriorityCodePoint())
if mibBuilder.loadTexts: ieee8021PbbPipDecodingPriorityCodePointRow.setStatus('current')
ieee8021PbbPipDecodingPriorityCodePoint = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: ieee8021PbbPipDecodingPriorityCodePoint.setStatus('current')
ieee8021PbbPipDecodingPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1, 3), IEEE8021PriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbPipDecodingPriority.setStatus('current')
ieee8021PbbPipDecodingDropEligible = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbPipDecodingDropEligible.setStatus('current')
ieee8021PbbPipEncodingTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7), )
if mibBuilder.loadTexts: ieee8021PbbPipEncodingTable.setStatus('current')
ieee8021PbbPipEncodingEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1), ).setIndexNames((0, "IEEE8021-PBB-MIB", "ieee8021PbbPipIfIndex"), (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingPriorityCodePointRow"), (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingPriorityCodePoint"), (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingDropEligible"))
if mibBuilder.loadTexts: ieee8021PbbPipEncodingEntry.setStatus('current')
ieee8021PbbPipEncodingPriorityCodePointRow = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1, 1), IEEE8021PriorityCodePoint())
if mibBuilder.loadTexts: ieee8021PbbPipEncodingPriorityCodePointRow.setStatus('current')
ieee8021PbbPipEncodingPriorityCodePoint = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: ieee8021PbbPipEncodingPriorityCodePoint.setStatus('current')
ieee8021PbbPipEncodingDropEligible = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1, 3), TruthValue())
if mibBuilder.loadTexts: ieee8021PbbPipEncodingDropEligible.setStatus('current')
ieee8021PbbPipEncodingPriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1, 4), IEEE8021PriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbPipEncodingPriority.setStatus('current')
ieee8021PbbVipToPipMappingTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8), )
if mibBuilder.loadTexts: ieee8021PbbVipToPipMappingTable.setStatus('current')
ieee8021PbbVipToPipMappingEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PbbVipToPipMappingEntry.setStatus('current')
ieee8021PbbVipToPipMappingPipIfIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbVipToPipMappingPipIfIndex.setStatus('current')
ieee8021PbbVipToPipMappingStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8, 1, 2), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbVipToPipMappingStorageType.setStatus('current')
ieee8021PbbVipToPipMappingRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbVipToPipMappingRowStatus.setStatus('current')
ieee8021PbbCBPServiceMappingTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9), )
if mibBuilder.loadTexts: ieee8021PbbCBPServiceMappingTable.setStatus('current')
ieee8021PbbCBPServiceMappingEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingBackboneSid"))
if mibBuilder.loadTexts: ieee8021PbbCBPServiceMappingEntry.setStatus('current')
ieee8021PbbCBPServiceMappingBackboneSid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 1), IEEE8021PbbServiceIdentifier())
if mibBuilder.loadTexts: ieee8021PbbCBPServiceMappingBackboneSid.setStatus('current')
ieee8021PbbCBPServiceMappingBVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 2), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbCBPServiceMappingBVid.setStatus('current')
ieee8021PbbCBPServiceMappingDefaultBackboneDest = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbCBPServiceMappingDefaultBackboneDest.setStatus('current')
ieee8021PbbCBPServiceMappingType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 4), IEEE8021PbbIngressEgress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbCBPServiceMappingType.setStatus('deprecated')
ieee8021PbbCBPServiceMappingLocalSid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 5), IEEE8021PbbServiceIdentifierOrUnassigned().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbCBPServiceMappingLocalSid.setStatus('current')
ieee8021PbbCBPServiceMappingRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbCBPServiceMappingRowStatus.setStatus('current')
ieee8021PbbCbpTable = MibTable((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 10), )
if mibBuilder.loadTexts: ieee8021PbbCbpTable.setStatus('current')
ieee8021PbbCbpEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 10, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021PbbCbpEntry.setStatus('current')
ieee8021PbbCbpRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 10, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021PbbCbpRowStatus.setStatus('current')
ieee8021PbbGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 9, 2, 1))
ieee8021PbbCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 9, 2, 2))
ieee8021PbbBackboneEdgeBridgeGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 1)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbBackboneEdgeBridgeAddress"), ("IEEE8021-PBB-MIB", "ieee8021PbbBackboneEdgeBridgeName"), ("IEEE8021-PBB-MIB", "ieee8021PbbNumberOfIComponents"), ("IEEE8021-PBB-MIB", "ieee8021PbbNumberOfBComponents"), ("IEEE8021-PBB-MIB", "ieee8021PbbNumberOfBebPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbBackboneEdgeBridgeGroup = ieee8021PbbBackboneEdgeBridgeGroup.setStatus('current')
ieee8021PbbVipGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 2)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbVipPipIfIndex"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipISid"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipDefaultDstBMAC"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipType"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipRowStatus"), ("IEEE8021-PBB-MIB", "ieee8021PbbISidToVipComponentId"), ("IEEE8021-PBB-MIB", "ieee8021PbbISidToVipPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbVipGroup = ieee8021PbbVipGroup.setStatus('current')
ieee8021PbbPipGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 3)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbNextAvailablePipIfIndex"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipBMACAddress"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipName"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipIComponentId"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap1"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap2"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap3"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap4"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbPipGroup = ieee8021PbbPipGroup.setStatus('current')
ieee8021PbbDefaultPriorityGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 4)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbPipPriorityCodePointSelection"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipUseDEI"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipRequireDropEncoding"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbDefaultPriorityGroup = ieee8021PbbDefaultPriorityGroup.setStatus('current')
ieee8021PbbPipDecodingGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 5)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingPriority"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingDropEligible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbPipDecodingGroup = ieee8021PbbPipDecodingGroup.setStatus('current')
ieee8021PbbPipEncodingGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 6)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbPipEncodingGroup = ieee8021PbbPipEncodingGroup.setStatus('current')
ieee8021PbbVipToPipMappingGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 7)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbVipToPipMappingPipIfIndex"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipToPipMappingStorageType"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipToPipMappingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbVipToPipMappingGroup = ieee8021PbbVipToPipMappingGroup.setStatus('current')
ieee8021PbbCBPServiceMappingGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 8)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingBVid"), ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingDefaultBackboneDest"), ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingType"), ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingLocalSid"), ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbCBPServiceMappingGroup = ieee8021PbbCBPServiceMappingGroup.setStatus('current')
ieee8021PbbDynamicCbpGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 9)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbCbpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbDynamicCbpGroup = ieee8021PbbDynamicCbpGroup.setStatus('current')
ieee8021PbbVipPbbTeGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 10)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbVipEnableConnectionId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbVipPbbTeGroup = ieee8021PbbVipPbbTeGroup.setStatus('current')
ieee8021PbbCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 9, 2, 2, 1)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbBackboneEdgeBridgeGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipToPipMappingGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbDynamicCbpGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbDefaultPriorityGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbCompliance = ieee8021PbbCompliance.setStatus('current')
ieee8021PbbWithPbbTeCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 9, 2, 2, 2)).setObjects(("IEEE8021-PBB-MIB", "ieee8021PbbBackboneEdgeBridgeGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipToPipMappingGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbDynamicCbpGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbVipPbbTeGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbDefaultPriorityGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingGroup"), ("IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PbbWithPbbTeCompliance = ieee8021PbbWithPbbTeCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-PBB-MIB", ieee8021PbbCBPServiceMappingGroup=ieee8021PbbCBPServiceMappingGroup, ieee8021PbbCompliance=ieee8021PbbCompliance, ieee8021PbbPipEncodingPriority=ieee8021PbbPipEncodingPriority, ieee8021PbbPipRequireDropEncoding=ieee8021PbbPipRequireDropEncoding, ieee8021PbbCBPServiceMappingBackboneSid=ieee8021PbbCBPServiceMappingBackboneSid, ieee8021PbbVipEntry=ieee8021PbbVipEntry, ieee8021PbbPipDecodingPriorityCodePointRow=ieee8021PbbPipDecodingPriorityCodePointRow, ieee8021PbbPipTable=ieee8021PbbPipTable, ieee8021PbbISidToVipTable=ieee8021PbbISidToVipTable, ieee8021PbbPipRowStatus=ieee8021PbbPipRowStatus, ieee8021PbbCompliances=ieee8021PbbCompliances, ieee8021PbbCBPServiceMappingRowStatus=ieee8021PbbCBPServiceMappingRowStatus, ieee8021PbbPipGroup=ieee8021PbbPipGroup, ieee8021PbbPipDecodingEntry=ieee8021PbbPipDecodingEntry, ieee8021PbbBackboneEdgeBridgeObjects=ieee8021PbbBackboneEdgeBridgeObjects, ieee8021PbbObjects=ieee8021PbbObjects, ieee8021PbbNumberOfBebPorts=ieee8021PbbNumberOfBebPorts, ieee8021PbbISidToVipComponentId=ieee8021PbbISidToVipComponentId, ieee8021PbbPipEncodingEntry=ieee8021PbbPipEncodingEntry, ieee8021PbbPipEntry=ieee8021PbbPipEntry, ieee8021PbbCBPServiceMappingDefaultBackboneDest=ieee8021PbbCBPServiceMappingDefaultBackboneDest, ieee8021PbbISidToVipISid=ieee8021PbbISidToVipISid, ieee8021PbbVipToPipMappingEntry=ieee8021PbbVipToPipMappingEntry, ieee8021PbbISidToVipPort=ieee8021PbbISidToVipPort, ieee8021PbbPipIfIndex=ieee8021PbbPipIfIndex, ieee8021PbbBackboneEdgeBridgeName=ieee8021PbbBackboneEdgeBridgeName, ieee8021PbbPipDecodingDropEligible=ieee8021PbbPipDecodingDropEligible, ieee8021PbbGroups=ieee8021PbbGroups, ieee8021PbbCBPServiceMappingTable=ieee8021PbbCBPServiceMappingTable, ieee8021PbbVipEnableConnectionId=ieee8021PbbVipEnableConnectionId, ieee8021PbbPipVipMap=ieee8021PbbPipVipMap, ieee8021PbbPipVipMap3=ieee8021PbbPipVipMap3, ieee8021PbbPipPriorityEntry=ieee8021PbbPipPriorityEntry, ieee8021PbbCbpTable=ieee8021PbbCbpTable, ieee8021PbbPipEncodingGroup=ieee8021PbbPipEncodingGroup, ieee8021PbbVipTable=ieee8021PbbVipTable, ieee8021PbbNumberOfBComponents=ieee8021PbbNumberOfBComponents, ieee8021PbbVipToPipMappingPipIfIndex=ieee8021PbbVipToPipMappingPipIfIndex, ieee8021PbbISidToVipEntry=ieee8021PbbISidToVipEntry, ieee8021PbbCBPServiceMappingLocalSid=ieee8021PbbCBPServiceMappingLocalSid, ieee8021PbbPipVipMap1=ieee8021PbbPipVipMap1, ieee8021PbbPipBMACAddress=ieee8021PbbPipBMACAddress, ieee8021PbbVipRowStatus=ieee8021PbbVipRowStatus, ieee8021PbbPipEncodingTable=ieee8021PbbPipEncodingTable, ieee8021PbbPipEncodingPriorityCodePointRow=ieee8021PbbPipEncodingPriorityCodePointRow, ieee8021PbbCBPServiceMappingBVid=ieee8021PbbCBPServiceMappingBVid, ieee8021PbbPipPriorityTable=ieee8021PbbPipPriorityTable, ieee8021PbbWithPbbTeCompliance=ieee8021PbbWithPbbTeCompliance, ieee8021PbbCBPServiceMappingType=ieee8021PbbCBPServiceMappingType, ieee8021PbbDynamicCbpGroup=ieee8021PbbDynamicCbpGroup, ieee8021PbbNextAvailablePipIfIndex=ieee8021PbbNextAvailablePipIfIndex, ieee8021PbbVipToPipMappingStorageType=ieee8021PbbVipToPipMappingStorageType, ieee8021PbbConformance=ieee8021PbbConformance, ieee8021PbbPipDecodingGroup=ieee8021PbbPipDecodingGroup, ieee8021PbbVipISid=ieee8021PbbVipISid, ieee8021PbbVipDefaultDstBMAC=ieee8021PbbVipDefaultDstBMAC, ieee8021PbbPipEncodingPriorityCodePoint=ieee8021PbbPipEncodingPriorityCodePoint, ieee8021PbbVipPbbTeGroup=ieee8021PbbVipPbbTeGroup, ieee8021PbbPipVipMap4=ieee8021PbbPipVipMap4, ieee8021PbbVipType=ieee8021PbbVipType, ieee8021PbbBackboneEdgeBridgeAddress=ieee8021PbbBackboneEdgeBridgeAddress, ieee8021PbbNumberOfIComponents=ieee8021PbbNumberOfIComponents, ieee8021PbbProviderBackboneBridge=ieee8021PbbProviderBackboneBridge, ieee8021PbbCbpEntry=ieee8021PbbCbpEntry, PYSNMP_MODULE_ID=ieee8021PbbMib, ieee8021PbbCbpRowStatus=ieee8021PbbCbpRowStatus, ieee8021PbbPipDecodingPriority=ieee8021PbbPipDecodingPriority, ieee8021PbbBackboneEdgeBridgeGroup=ieee8021PbbBackboneEdgeBridgeGroup, ieee8021PbbVipToPipMappingTable=ieee8021PbbVipToPipMappingTable, ieee8021PbbVipPipIfIndex=ieee8021PbbVipPipIfIndex, ieee8021PbbPipDecodingTable=ieee8021PbbPipDecodingTable, ieee8021PbbVipToPipMappingGroup=ieee8021PbbVipToPipMappingGroup, ieee8021PbbPipDecodingPriorityCodePoint=ieee8021PbbPipDecodingPriorityCodePoint, ieee8021PbbMib=ieee8021PbbMib, ieee8021PbbVipGroup=ieee8021PbbVipGroup, ieee8021PbbCBPServiceMappingEntry=ieee8021PbbCBPServiceMappingEntry, ieee8021PbbPipVipMap2=ieee8021PbbPipVipMap2, ieee8021PbbDefaultPriorityGroup=ieee8021PbbDefaultPriorityGroup, ieee8021PbbNotifications=ieee8021PbbNotifications, ieee8021PbbPipName=ieee8021PbbPipName, ieee8021PbbPipEncodingDropEligible=ieee8021PbbPipEncodingDropEligible, ieee8021PbbVipToPipMappingRowStatus=ieee8021PbbVipToPipMappingRowStatus, ieee8021PbbPipIComponentId=ieee8021PbbPipIComponentId, ieee8021PbbPipUseDEI=ieee8021PbbPipUseDEI, ieee8021PbbPipPriorityCodePointSelection=ieee8021PbbPipPriorityCodePointSelection)
