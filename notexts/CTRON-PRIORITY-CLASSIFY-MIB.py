#
# PySNMP MIB module CTRON-PRIORITY-CLASSIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PRIORITY-CLASSIFY-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:56 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ctPriorityExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPriorityExt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ctPriClassify = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6))
if mibBuilder.loadTexts: ctPriClassify.setLastUpdated('200203121855Z')
if mibBuilder.loadTexts: ctPriClassify.setOrganization('Cabletron Systems, Inc')
ctPriClassifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1))
class CtPriClassifyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("etherType", 1), ("llcDsapSsap", 2), ("ipTypeOfService", 3), ("ipProtocolType", 4), ("ipxClassOfService", 5), ("ipxPacketType", 6), ("ipAddressSource", 7), ("ipAddressDestination", 8), ("ipAddressBilateral", 9), ("ipxNetworkSource", 10), ("ipxNetworkDestination", 11), ("ipxNetworkBilateral", 12), ("ipUdpPortSource", 13), ("ipUdpPortDestination", 14), ("ipUdpPortBilateral", 15), ("ipTcpPortSource", 16), ("ipTcpPortDestination", 17), ("ipTcpPortBilateral", 18), ("ipxSocketSource", 19), ("ipxSocketDestination", 20), ("ipxSocketBilateral", 21), ("macAddressSource", 22), ("macAddressDestination", 23), ("macAddressBilateral", 24), ("ipFragments", 25))

class PortList(TextualConvention, OctetString):
    status = 'current'

ctPriClassifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyStatus.setStatus('current')
ctPriClassifyMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyMaxEntries.setStatus('current')
ctPriClassifyNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyNumEntries.setStatus('current')
ctPriClassifyTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4), )
if mibBuilder.loadTexts: ctPriClassifyTable.setStatus('current')
ctPriClassifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1), ).setIndexNames((0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPriority"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMeaning"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataVal"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMask"))
if mibBuilder.loadTexts: ctPriClassifyEntry.setStatus('current')
ctPriClassifyPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: ctPriClassifyPriority.setStatus('current')
ctPriClassifyDataMeaning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 2), CtPriClassifyType())
if mibBuilder.loadTexts: ctPriClassifyDataMeaning.setStatus('current')
ctPriClassifyDataVal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: ctPriClassifyDataVal.setStatus('current')
ctPriClassifyDataMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 4), Unsigned32())
if mibBuilder.loadTexts: ctPriClassifyDataMask.setStatus('current')
ctPriClassifyIngressList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 5), PortList().clone(hexValue="0000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctPriClassifyIngressList.setStatus('current')
ctPriClassifyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctPriClassifyRowStatus.setStatus('current')
ctPriClassifyRowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyRowInfo.setStatus('current')
ctPriClassifyTOSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyTOSStatus.setStatus('current')
ctPriClassifyTOSValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyTOSValue.setStatus('current')
ctPriClassifyAbilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5), )
if mibBuilder.loadTexts: ctPriClassifyAbilityTable.setStatus('current')
ctPriClassifyAbilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1), ).setIndexNames((0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyAbility"))
if mibBuilder.loadTexts: ctPriClassifyAbilityEntry.setStatus('current')
ctPriClassifyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 1), CtPriClassifyType())
if mibBuilder.loadTexts: ctPriClassifyAbility.setStatus('current')
ctPriClassifyPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyPorts.setStatus('current')
ctPriClassifyTableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyTableLastChange.setStatus('current')
ctPriClassifyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2))
ctPriClassifyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1))
ctPriClassifyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2))
ctPriClassifyBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1, 1)).setObjects(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyMaxEntries"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyNumEntries"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyIngressList"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowInfo"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSValue"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPorts"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTableLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctPriClassifyBaseGroup = ctPriClassifyBaseGroup.setStatus('current')
ctPriClassifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2, 1)).setObjects(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctPriClassifyCompliance = ctPriClassifyCompliance.setStatus('current')
mibBuilder.exportSymbols("CTRON-PRIORITY-CLASSIFY-MIB", ctPriClassifyDataMeaning=ctPriClassifyDataMeaning, ctPriClassifyPorts=ctPriClassifyPorts, ctPriClassifyGroups=ctPriClassifyGroups, ctPriClassifyBaseGroup=ctPriClassifyBaseGroup, ctPriClassifyRowStatus=ctPriClassifyRowStatus, ctPriClassifyStatus=ctPriClassifyStatus, ctPriClassifyTableLastChange=ctPriClassifyTableLastChange, ctPriClassifyRowInfo=ctPriClassifyRowInfo, ctPriClassifyAbility=ctPriClassifyAbility, PortList=PortList, ctPriClassifyObjects=ctPriClassifyObjects, PYSNMP_MODULE_ID=ctPriClassify, ctPriClassifyPriority=ctPriClassifyPriority, ctPriClassify=ctPriClassify, ctPriClassifyCompliances=ctPriClassifyCompliances, ctPriClassifyDataMask=ctPriClassifyDataMask, ctPriClassifyAbilityTable=ctPriClassifyAbilityTable, CtPriClassifyType=CtPriClassifyType, ctPriClassifyMaxEntries=ctPriClassifyMaxEntries, ctPriClassifyDataVal=ctPriClassifyDataVal, ctPriClassifyTOSStatus=ctPriClassifyTOSStatus, ctPriClassifyTOSValue=ctPriClassifyTOSValue, ctPriClassifyConformance=ctPriClassifyConformance, ctPriClassifyIngressList=ctPriClassifyIngressList, ctPriClassifyEntry=ctPriClassifyEntry, ctPriClassifyCompliance=ctPriClassifyCompliance, ctPriClassifyTable=ctPriClassifyTable, ctPriClassifyNumEntries=ctPriClassifyNumEntries, ctPriClassifyAbilityEntry=ctPriClassifyAbilityEntry)
