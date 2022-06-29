#
# PySNMP MIB module RC-VRF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RC-VRF-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:13:03 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
rcVrf, IdList, EnableValue = mibBuilder.importSymbols("RAPID-CITY", "rcVrf", "IdList", "EnableValue")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, NotificationType, Counter64, TimeTicks, Gauge32, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, iso, Counter32, ObjectIdentity, IpAddress, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Counter64", "TimeTicks", "Gauge32", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "iso", "Counter32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
rcVrfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1))
rcVrfMib.setRevisions(('2008-09-09 00:00', '2008-05-18 00:00', '2008-05-16 00:00', '2008-05-13 00:00', '2008-05-09 00:00', '2008-05-08 00:00', '2008-04-28 00:00', '2008-03-13 00:00', '2007-12-18 00:00', '2007-05-03 00:00', '2007-01-24 00:00',))
if mibBuilder.loadTexts: rcVrfMib.setLastUpdated('200809090000Z')
if mibBuilder.loadTexts: rcVrfMib.setOrganization('Nortel Networks')
class VrfIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class VPNId(TextualConvention, OctetString):
    reference = "Fox, B. and Gleeson, B., 'Virtual Private Networks Identifier', RFC 2685, September 1999."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

class VrfRpTriggerBitCode(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rip", 0), ("ospf", 1), ("bgp", 2), ("isis", 3), ("pim", 4))

rcVrfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 0))
rcVrfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1))
rcVrfNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 2))
rcVrfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1))
rcVrfConfigScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 1))
rcVrfConfigNextAvailableVrfId = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 1, 1), VrfIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfConfigNextAvailableVrfId.setStatus('current')
rcVrfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2), )
if mibBuilder.loadTexts: rcVrfConfigTable.setStatus('current')
rcVrfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1), ).setIndexNames((0, "RC-VRF-MIB", "rcVrfId"))
if mibBuilder.loadTexts: rcVrfConfigEntry.setStatus('current')
rcVrfId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 1), VrfIdentifier())
if mibBuilder.loadTexts: rcVrfId.setStatus('current')
rcVrfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfRowStatus.setStatus('current')
rcVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcVrfName.setStatus('current')
rcVrfContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfContextName.setStatus('current')
rcVrfTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 5), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfTrapEnable.setStatus('current')
rcVrfMaxRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 6), Unsigned32().clone(10000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfMaxRoutes.setStatus('current')
rcVrfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfAdminStatus.setStatus('current')
rcVrfVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 8), VPNId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfVpnId.setStatus('current')
rcVrfRpTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 9), VrfRpTriggerBitCode().clone(namedValues=NamedValues(("rip", 0), ("ospf", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfRpTrigger.setStatus('current')
rcVrfMaxRoutesTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 1, 2, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfMaxRoutesTrapEnable.setStatus('current')
rcVrfStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2))
rcVrfStatScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 1))
rcVrfConfiguredVRFs = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfConfiguredVRFs.setStatus('current')
rcVrfActiveVRFs = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfActiveVRFs.setStatus('current')
rcVrfStatTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2), )
if mibBuilder.loadTexts: rcVrfStatTable.setStatus('current')
rcVrfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1), ).setIndexNames((0, "RC-VRF-MIB", "rcVrfId"))
if mibBuilder.loadTexts: rcVrfStatEntry.setStatus('current')
rcVrfStatRouteEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfStatRouteEntries.setStatus('current')
rcVrfStatFIBEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfStatFIBEntries.setStatus('current')
rcVrfStatUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfStatUpTime.setStatus('current')
rcVrfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfOperStatus.setStatus('current')
rcVrfRpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 5), VrfRpTriggerBitCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfRpStatus.setStatus('current')
rcVrfRouterAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfRouterAddressType.setStatus('current')
rcVrfRouterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 2, 2, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfRouterAddress.setStatus('current')
rcVrfIpVpnTableSize = MibScalar((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcVrfIpVpnTableSize.setStatus('current')
rcVrfIpVpnTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4), )
if mibBuilder.loadTexts: rcVrfIpVpnTable.setStatus('current')
rcVrfIpVpnTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1), ).setIndexNames((0, "RC-VRF-MIB", "rcVrfIpVpnVrfId"))
if mibBuilder.loadTexts: rcVrfIpVpnTableEntry.setStatus('current')
rcVrfIpVpnVrfId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 1), VrfIdentifier())
if mibBuilder.loadTexts: rcVrfIpVpnVrfId.setStatus('current')
rcVrfIpVpnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 2), EnableValue().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnStatus.setStatus('current')
rcVrfIpVpnImportRTList = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 3), IdList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnImportRTList.setStatus('current')
rcVrfIpVpnExportRTList = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 4), IdList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnExportRTList.setStatus('current')
rcVrfIpVpnSvcLblAllocOpt = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("perVrfperNexthop", 1), ("perVrf", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnSvcLblAllocOpt.setStatus('current')
rcVrfIpVpnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 1, 203, 1, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcVrfIpVpnRowStatus.setStatus('current')
mibBuilder.exportSymbols("RC-VRF-MIB", VPNId=VPNId, rcVrfName=rcVrfName, rcVrfMib=rcVrfMib, rcVrfConfigTable=rcVrfConfigTable, rcVrfIpVpnTable=rcVrfIpVpnTable, VrfRpTriggerBitCode=VrfRpTriggerBitCode, rcVrfStatEntry=rcVrfStatEntry, VrfIdentifier=VrfIdentifier, rcVrfStatScalars=rcVrfStatScalars, rcVrfNotificationObjects=rcVrfNotificationObjects, rcVrfIpVpnStatus=rcVrfIpVpnStatus, rcVrfIpVpnExportRTList=rcVrfIpVpnExportRTList, rcVrfIpVpnTableEntry=rcVrfIpVpnTableEntry, rcVrfMaxRoutes=rcVrfMaxRoutes, rcVrfRpTrigger=rcVrfRpTrigger, rcVrfStat=rcVrfStat, rcVrfIpVpnVrfId=rcVrfIpVpnVrfId, rcVrfRouterAddressType=rcVrfRouterAddressType, rcVrfIpVpnTableSize=rcVrfIpVpnTableSize, PYSNMP_MODULE_ID=rcVrfMib, rcVrfNotifications=rcVrfNotifications, rcVrfConfigNextAvailableVrfId=rcVrfConfigNextAvailableVrfId, rcVrfConfigEntry=rcVrfConfigEntry, rcVrfTrapEnable=rcVrfTrapEnable, rcVrfIpVpnSvcLblAllocOpt=rcVrfIpVpnSvcLblAllocOpt, rcVrfVpnId=rcVrfVpnId, rcVrfId=rcVrfId, rcVrfConfigScalars=rcVrfConfigScalars, rcVrfActiveVRFs=rcVrfActiveVRFs, rcVrfAdminStatus=rcVrfAdminStatus, rcVrfStatTable=rcVrfStatTable, rcVrfRowStatus=rcVrfRowStatus, rcVrfIpVpnRowStatus=rcVrfIpVpnRowStatus, rcVrfMaxRoutesTrapEnable=rcVrfMaxRoutesTrapEnable, rcVrfConfiguredVRFs=rcVrfConfiguredVRFs, rcVrfRpStatus=rcVrfRpStatus, rcVrfStatRouteEntries=rcVrfStatRouteEntries, rcVrfIpVpnImportRTList=rcVrfIpVpnImportRTList, rcVrfOperStatus=rcVrfOperStatus, rcVrfContextName=rcVrfContextName, rcVrfStatUpTime=rcVrfStatUpTime, rcVrfConfig=rcVrfConfig, rcVrfStatFIBEntries=rcVrfStatFIBEntries, rcVrfRouterAddress=rcVrfRouterAddress, rcVrfObjects=rcVrfObjects)
