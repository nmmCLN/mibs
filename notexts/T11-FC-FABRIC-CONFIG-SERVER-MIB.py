#
# PySNMP MIB module T11-FC-FABRIC-CONFIG-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-FC-FABRIC-CONFIG-SERVER-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
fcmInstanceIndex, FcPortType, FcAddressIdOrZero, FcNameIdOrZero, FcDomainIdOrZero, fcmSwitchIndex = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex", "FcPortType", "FcAddressIdOrZero", "FcNameIdOrZero", "FcDomainIdOrZero", "fcmSwitchIndex")
URLString, = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "URLString")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TimeStamp, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TruthValue", "TextualConvention")
t11FamLocalSwitchWwn, = mibBuilder.importSymbols("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn")
T11NsGs4RejectReasonCode, = mibBuilder.importSymbols("T11-FC-NAME-SERVER-MIB", "T11NsGs4RejectReasonCode")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FcFabricConfigServerMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 162))
t11FcFabricConfigServerMIB.setRevisions(('2007-06-27 00:00',))
if mibBuilder.loadTexts: t11FcFabricConfigServerMIB.setLastUpdated('200706270000Z')
if mibBuilder.loadTexts: t11FcFabricConfigServerMIB.setOrganization("For the initial versions, T11. For later versions, the IETF's IMSS Working Group.")
t11FcsMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 1))
t11FcsMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 2))
t11FcsNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 0))
t11FcsDiscovery = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 1, 1))
t11FcsDiscoveredConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 1, 2))
t11FcsStats = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 1, 3))
t11FcsNotificationInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 1, 4))
class T11FcListIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class T11FcListIndexPointerOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class T11FcIeType(TextualConvention, Integer32):
    reference = 'ANSI INCITS 427-2007, Fibre Channel - Generic Services 5, FC-GS-5, Table 96.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("switch", 3), ("hub", 4), ("bridge", 5))

class T11FcPortState(TextualConvention, Integer32):
    reference = 'ANSI INCITS 427-2007, Fibre Channel - Generic Services 5, FC-GS-5, Table 106.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("online", 3), ("offline", 4), ("testing", 5), ("fault", 6))

class T11FcPortTxType(TextualConvention, Integer32):
    reference = 'ANSI INCITS 427-2007, Fibre Channel - Generic Services 5, FC-GS-5, Table 101.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("shortwave850nm", 3), ("longwave1550nm", 4), ("longwave1310nm", 5), ("electrical", 6), ("tenGbaseSr850", 7), ("tenGbaseLr1310", 8), ("tenGbaseEr1550", 9), ("tenGbaseLx1300", 10), ("tenGbaseSw850", 11), ("tenGbaseLw1310", 12), ("tenGbaseEw1550", 13))

class T11FcsRejectReasonExplanation(TextualConvention, Integer32):
    reference = 'ANSI INCITS 427-2007, Fibre Channel - Generic Services 5, FC-GS-5, Table 124.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))
    namedValues = NamedValues(("noAdditionalExplanation", 1), ("invNameIdForIEOrPort", 2), ("ieListNotAvailable", 3), ("ieTypeNotAvailable", 4), ("domainIdNotAvailable", 5), ("mgmtIdNotAvailable", 6), ("fabNameNotAvailable", 7), ("ielogNameNotAvailable", 8), ("mgmtAddrListNotAvailable", 9), ("ieInfoListNotAvailable", 10), ("portListNotAvailable", 11), ("portTypeNotAvailable", 12), ("phyPortNumNotAvailable", 13), ("attPortNameListNotAvailable", 14), ("portStateNotAvailable", 15), ("unableToRegIELogName", 16), ("platformNameNoExist", 17), ("platformNameAlreadyExists", 18), ("platformNodeNameNoExists", 19), ("platformNodeNameAlreadyExists", 20), ("resourceUnavailable", 21), ("noEntriesInLunMap", 22), ("invalidDeviceNameLength", 23), ("multipleAttributes", 24), ("invalidAttribBlockLength", 25), ("attributesMissing", 26))

t11FcsFabricDiscoveryTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 1, 1), )
if mibBuilder.loadTexts: t11FcsFabricDiscoveryTable.setStatus('current')
t11FcsFabricDiscoveryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"))
if mibBuilder.loadTexts: t11FcsFabricDiscoveryEntry.setStatus('current')
t11FcsFabricDiscoveryRangeLow = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1, 1), T11FabricIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcsFabricDiscoveryRangeLow.setStatus('current')
t11FcsFabricDiscoveryRangeHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1, 2), T11FabricIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcsFabricDiscoveryRangeHigh.setStatus('current')
t11FcsFabricDiscoveryStart = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("noOp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcsFabricDiscoveryStart.setStatus('current')
t11FcsFabricDiscoveryTimeOut = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(300, 86400)).clone(900)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcsFabricDiscoveryTimeOut.setStatus('current')
t11FcsDiscoveryStateTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 1, 2), )
if mibBuilder.loadTexts: t11FcsDiscoveryStateTable.setStatus('current')
t11FcsDiscoveryStateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"))
if mibBuilder.loadTexts: t11FcsDiscoveryStateEntry.setStatus('current')
t11FcsFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 1, 2, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: t11FcsFabricIndex.setStatus('current')
t11FcsDiscoveryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inProgress", 1), ("completed", 2), ("localOnly", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcsDiscoveryStatus.setStatus('current')
t11FcsDiscoveryCompleteTime = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 1, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsDiscoveryCompleteTime.setStatus('current')
t11FcsIeTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 2, 1), )
if mibBuilder.loadTexts: t11FcsIeTable.setStatus('current')
t11FcsIeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeName"))
if mibBuilder.loadTexts: t11FcsIeEntry.setStatus('current')
t11FcsIeName = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: t11FcsIeName.setStatus('current')
t11FcsIeType = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 2), T11FcIeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsIeType.setStatus('current')
t11FcsIeDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 3), FcDomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsIeDomainId.setStatus('current')
t11FcsIeMgmtId = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 4), FcAddressIdOrZero().clone(hexValue="000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsIeMgmtId.setStatus('current')
t11FcsIeFabricName = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 5), FcNameIdOrZero().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )).clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsIeFabricName.setStatus('current')
t11FcsIeLogicalName = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsIeLogicalName.setStatus('current')
t11FcsIeMgmtAddrListIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 7), T11FcListIndexPointerOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsIeMgmtAddrListIndex.setStatus('current')
t11FcsIeInfoList = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsIeInfoList.setStatus('current')
t11FcsMgmtAddrListTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 2, 2), )
if mibBuilder.loadTexts: t11FcsMgmtAddrListTable.setStatus('current')
t11FcsMgmtAddrListEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 2, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrListIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrIndex"))
if mibBuilder.loadTexts: t11FcsMgmtAddrListEntry.setStatus('current')
t11FcsMgmtAddrListIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 2, 1, 1), T11FcListIndex())
if mibBuilder.loadTexts: t11FcsMgmtAddrListIndex.setStatus('current')
t11FcsMgmtAddrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: t11FcsMgmtAddrIndex.setStatus('current')
t11FcsMgmtAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 2, 1, 3), URLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsMgmtAddr.setStatus('current')
t11FcsPortTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 2, 4), )
if mibBuilder.loadTexts: t11FcsPortTable.setStatus('current')
t11FcsPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeName"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortName"))
if mibBuilder.loadTexts: t11FcsPortEntry.setStatus('current')
t11FcsPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: t11FcsPortName.setStatus('current')
t11FcsPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 2), FcPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortType.setStatus('current')
t11FcsPortTxType = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 3), T11FcPortTxType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortTxType.setStatus('current')
t11FcsPortModuleType = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortModuleType.setStatus('current')
t11FcsPortPhyPortNum = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortPhyPortNum.setStatus('current')
t11FcsPortAttachPortNameIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 6), T11FcListIndexPointerOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortAttachPortNameIndex.setStatus('current')
t11FcsPortState = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 7), T11FcPortState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortState.setStatus('current')
t11FcsPortSpeedCapab = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortSpeedCapab.setStatus('current')
t11FcsPortOperSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortOperSpeed.setStatus('current')
t11FcsPortZoningEnfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 4, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPortZoningEnfStatus.setStatus('current')
t11FcsAttachPortNameListTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 2, 5), )
if mibBuilder.loadTexts: t11FcsAttachPortNameListTable.setStatus('current')
t11FcsAttachPortNameListEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 2, 5, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsAttachPortNameListIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsAttachPortName"))
if mibBuilder.loadTexts: t11FcsAttachPortNameListEntry.setStatus('current')
t11FcsAttachPortNameListIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 5, 1, 1), T11FcListIndex())
if mibBuilder.loadTexts: t11FcsAttachPortNameListIndex.setStatus('current')
t11FcsAttachPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsAttachPortName.setStatus('current')
t11FcsPlatformTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 2, 6), )
if mibBuilder.loadTexts: t11FcsPlatformTable.setStatus('current')
t11FcsPlatformEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformIndex"))
if mibBuilder.loadTexts: t11FcsPlatformEntry.setStatus('current')
t11FcsPlatformIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: t11FcsPlatformIndex.setStatus('current')
t11FcsPlatformName = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformName.setStatus('current')
t11FcsPlatformType = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformType.setStatus('current')
t11FcsPlatformNodeNameListIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 4), T11FcListIndexPointerOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformNodeNameListIndex.setStatus('current')
t11FcsPlatformMgmtAddrListIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 5), T11FcListIndexPointerOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformMgmtAddrListIndex.setStatus('current')
t11FcsPlatformVendorId = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 6), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(12, 12), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformVendorId.setStatus('current')
t11FcsPlatformProductId = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 7), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(20, 20), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformProductId.setStatus('current')
t11FcsPlatformProductRevLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 8), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 32), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformProductRevLevel.setStatus('current')
t11FcsPlatformDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 9), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 128), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformDescription.setStatus('current')
t11FcsPlatformLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 10), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 64), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformLabel.setStatus('current')
t11FcsPlatformLocation = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 11), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 128), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformLocation.setStatus('current')
t11FcsPlatformSystemID = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 12), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 64), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformSystemID.setStatus('current')
t11FcsPlatformSysMgmtAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 13), T11FcListIndexPointerOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformSysMgmtAddr.setStatus('current')
t11FcsPlatformClusterId = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 14), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 64), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformClusterId.setStatus('current')
t11FcsPlatformClusterMgmtAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 15), T11FcListIndexPointerOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformClusterMgmtAddr.setStatus('current')
t11FcsPlatformFC4Types = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 6, 1, 16), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(32, 32), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsPlatformFC4Types.setStatus('current')
t11FcsNodeNameListTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 2, 7), )
if mibBuilder.loadTexts: t11FcsNodeNameListTable.setStatus('current')
t11FcsNodeNameListEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 2, 7, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsNodeNameListIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsNodeName"))
if mibBuilder.loadTexts: t11FcsNodeNameListEntry.setStatus('current')
t11FcsNodeNameListIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 7, 1, 1), T11FcListIndex())
if mibBuilder.loadTexts: t11FcsNodeNameListIndex.setStatus('current')
t11FcsNodeName = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 2, 7, 1, 2), FcNameIdOrZero().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsNodeName.setStatus('current')
t11FcsStatsTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 3, 1), )
if mibBuilder.loadTexts: t11FcsStatsTable.setStatus('current')
t11FcsStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"))
if mibBuilder.loadTexts: t11FcsStatsEntry.setStatus('current')
t11FcsInGetReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsInGetReqs.setStatus('current')
t11FcsOutGetReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsOutGetReqs.setStatus('current')
t11FcsInRegReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsInRegReqs.setStatus('current')
t11FcsOutRegReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsOutRegReqs.setStatus('current')
t11FcsInDeregReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsInDeregReqs.setStatus('current')
t11FcsOutDeregReqs = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsOutDeregReqs.setStatus('current')
t11FcsRejects = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsRejects.setStatus('current')
t11FcsNotifyControlTable = MibTable((1, 3, 6, 1, 2, 1, 162, 1, 4, 1), )
if mibBuilder.loadTexts: t11FcsNotifyControlTable.setStatus('current')
t11FcsNotifyControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricIndex"))
if mibBuilder.loadTexts: t11FcsNotifyControlEntry.setStatus('current')
t11FcsReqRejectNotifyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcsReqRejectNotifyEnable.setStatus('current')
t11FcsDiscoveryCompNotifyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcsDiscoveryCompNotifyEnable.setStatus('current')
t11FcsMgmtAddrChangeNotifyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcsMgmtAddrChangeNotifyEnable.setStatus('current')
t11FcsRejectCtCommandString = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsRejectCtCommandString.setStatus('current')
t11FcsRejectRequestSource = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 5), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsRejectRequestSource.setStatus('current')
t11FcsRejectReasonCode = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 6), T11NsGs4RejectReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsRejectReasonCode.setStatus('current')
t11FcsRejectReasonCodeExp = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 7), T11FcsRejectReasonExplanation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsRejectReasonCodeExp.setStatus('current')
t11FcsRejectReasonVendorCode = MibTableColumn((1, 3, 6, 1, 2, 1, 162, 1, 4, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcsRejectReasonVendorCode.setStatus('current')
t11FcsRqRejectNotification = NotificationType((1, 3, 6, 1, 2, 1, 162, 0, 1)).setObjects(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonCode"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonCodeExp"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonVendorCode"))
if mibBuilder.loadTexts: t11FcsRqRejectNotification.setStatus('current')
t11FcsDiscoveryCompleteNotify = NotificationType((1, 3, 6, 1, 2, 1, 162, 0, 2)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryRangeLow"))
if mibBuilder.loadTexts: t11FcsDiscoveryCompleteNotify.setStatus('current')
t11FcsMgmtAddrChangeNotify = NotificationType((1, 3, 6, 1, 2, 1, 162, 0, 3)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeFabricIndex"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeIeName"))
if mibBuilder.loadTexts: t11FcsMgmtAddrChangeNotify.setStatus('current')
t11FcsMgmtAddrChangeFabricIndex = MibScalar((1, 3, 6, 1, 2, 1, 162, 1, 4, 2), T11FabricIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: t11FcsMgmtAddrChangeFabricIndex.setStatus('current')
t11FcsMgmtAddrChangeIeName = MibScalar((1, 3, 6, 1, 2, 1, 162, 1, 4, 3), FcNameIdOrZero()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: t11FcsMgmtAddrChangeIeName.setStatus('current')
t11FcsMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 2, 1))
t11FcsMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 162, 2, 2))
t11FcsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 162, 2, 1, 1)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveredConfigGroup"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryStatusGroup"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsNotificationInfoGroup"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsNotificationGroup"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryControlGroup"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcsMIBCompliance = t11FcsMIBCompliance.setStatus('current')
t11FcsDiscoveryControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 162, 2, 2, 1)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryRangeLow"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryRangeHigh"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryStart"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsFabricDiscoveryTimeOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcsDiscoveryControlGroup = t11FcsDiscoveryControlGroup.setStatus('current')
t11FcsDiscoveryStatusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 162, 2, 2, 2)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryStatus"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryCompleteTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcsDiscoveryStatusGroup = t11FcsDiscoveryStatusGroup.setStatus('current')
t11FcsDiscoveredConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 162, 2, 2, 3)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeType"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeDomainId"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeMgmtId"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeFabricName"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeLogicalName"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeMgmtAddrListIndex"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsIeInfoList"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddr"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortType"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortTxType"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortModuleType"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortPhyPortNum"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortAttachPortNameIndex"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortState"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortSpeedCapab"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortOperSpeed"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPortZoningEnfStatus"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsAttachPortName"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformName"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformType"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformNodeNameListIndex"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformMgmtAddrListIndex"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformVendorId"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformProductId"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformProductRevLevel"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformDescription"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformLabel"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformLocation"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformSystemID"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformSysMgmtAddr"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformClusterId"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformClusterMgmtAddr"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsPlatformFC4Types"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsNodeName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcsDiscoveredConfigGroup = t11FcsDiscoveredConfigGroup.setStatus('current')
t11FcsStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 162, 2, 2, 4)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsInGetReqs"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsOutGetReqs"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsInRegReqs"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsOutRegReqs"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsInDeregReqs"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsOutDeregReqs"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejects"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcsStatisticsGroup = t11FcsStatisticsGroup.setStatus('current')
t11FcsNotificationInfoGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 162, 2, 2, 5)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsReqRejectNotifyEnable"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryCompNotifyEnable"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeNotifyEnable"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectCtCommandString"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectRequestSource"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonCode"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonCodeExp"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRejectReasonVendorCode"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeFabricIndex"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeIeName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcsNotificationInfoGroup = t11FcsNotificationInfoGroup.setStatus('current')
t11FcsNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 162, 2, 2, 6)).setObjects(("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsRqRejectNotification"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsDiscoveryCompleteNotify"), ("T11-FC-FABRIC-CONFIG-SERVER-MIB", "t11FcsMgmtAddrChangeNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcsNotificationGroup = t11FcsNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("T11-FC-FABRIC-CONFIG-SERVER-MIB", t11FcsIeMgmtId=t11FcsIeMgmtId, t11FcsIeTable=t11FcsIeTable, t11FcsDiscoveryCompNotifyEnable=t11FcsDiscoveryCompNotifyEnable, t11FcsFabricIndex=t11FcsFabricIndex, t11FcsPlatformFC4Types=t11FcsPlatformFC4Types, t11FcsNotifyControlTable=t11FcsNotifyControlTable, t11FcsDiscoveryCompleteTime=t11FcsDiscoveryCompleteTime, T11FcListIndex=T11FcListIndex, t11FcsPlatformName=t11FcsPlatformName, t11FcsPortEntry=t11FcsPortEntry, t11FcsPortState=t11FcsPortState, t11FcsAttachPortNameListEntry=t11FcsAttachPortNameListEntry, t11FcsPortZoningEnfStatus=t11FcsPortZoningEnfStatus, t11FcsRqRejectNotification=t11FcsRqRejectNotification, t11FcsMgmtAddrIndex=t11FcsMgmtAddrIndex, t11FcsReqRejectNotifyEnable=t11FcsReqRejectNotifyEnable, t11FcsDiscoveredConfig=t11FcsDiscoveredConfig, t11FcsRejectReasonCode=t11FcsRejectReasonCode, t11FcsPortTxType=t11FcsPortTxType, t11FcsMgmtAddrListIndex=t11FcsMgmtAddrListIndex, t11FcsDiscoveredConfigGroup=t11FcsDiscoveredConfigGroup, t11FcsPlatformEntry=t11FcsPlatformEntry, t11FcsNotificationGroup=t11FcsNotificationGroup, t11FcsNodeNameListTable=t11FcsNodeNameListTable, t11FcsPlatformMgmtAddrListIndex=t11FcsPlatformMgmtAddrListIndex, t11FcsIeName=t11FcsIeName, t11FcsFabricDiscoveryRangeHigh=t11FcsFabricDiscoveryRangeHigh, t11FcsPortAttachPortNameIndex=t11FcsPortAttachPortNameIndex, t11FcsPlatformProductId=t11FcsPlatformProductId, T11FcPortTxType=T11FcPortTxType, PYSNMP_MODULE_ID=t11FcFabricConfigServerMIB, t11FcsPlatformLocation=t11FcsPlatformLocation, t11FcsRejectCtCommandString=t11FcsRejectCtCommandString, t11FcsMIBCompliances=t11FcsMIBCompliances, t11FcsNotificationInfoGroup=t11FcsNotificationInfoGroup, t11FcsMIBCompliance=t11FcsMIBCompliance, t11FcsPlatformSysMgmtAddr=t11FcsPlatformSysMgmtAddr, t11FcsIeMgmtAddrListIndex=t11FcsIeMgmtAddrListIndex, t11FcsMIBObjects=t11FcsMIBObjects, t11FcsPortModuleType=t11FcsPortModuleType, t11FcsMIBGroups=t11FcsMIBGroups, t11FcsPlatformSystemID=t11FcsPlatformSystemID, t11FcsPlatformClusterMgmtAddr=t11FcsPlatformClusterMgmtAddr, t11FcsNotificationInfo=t11FcsNotificationInfo, t11FcsIeEntry=t11FcsIeEntry, t11FcsInRegReqs=t11FcsInRegReqs, t11FcsFabricDiscoveryEntry=t11FcsFabricDiscoveryEntry, t11FcsMgmtAddrListTable=t11FcsMgmtAddrListTable, t11FcsDiscoveryStateEntry=t11FcsDiscoveryStateEntry, t11FcsDiscoveryStatusGroup=t11FcsDiscoveryStatusGroup, t11FcsRejectRequestSource=t11FcsRejectRequestSource, t11FcsInDeregReqs=t11FcsInDeregReqs, t11FcsOutGetReqs=t11FcsOutGetReqs, t11FcsOutRegReqs=t11FcsOutRegReqs, t11FcsPlatformClusterId=t11FcsPlatformClusterId, t11FcsIeDomainId=t11FcsIeDomainId, t11FcsInGetReqs=t11FcsInGetReqs, t11FcsNotifyControlEntry=t11FcsNotifyControlEntry, t11FcsAttachPortNameListIndex=t11FcsAttachPortNameListIndex, t11FcsPlatformVendorId=t11FcsPlatformVendorId, t11FcsDiscoveryControlGroup=t11FcsDiscoveryControlGroup, t11FcsRejectReasonVendorCode=t11FcsRejectReasonVendorCode, t11FcsDiscovery=t11FcsDiscovery, t11FcsAttachPortName=t11FcsAttachPortName, t11FcsFabricDiscoveryTable=t11FcsFabricDiscoveryTable, t11FcsAttachPortNameListTable=t11FcsAttachPortNameListTable, t11FcsOutDeregReqs=t11FcsOutDeregReqs, t11FcsPortType=t11FcsPortType, t11FcsStatsEntry=t11FcsStatsEntry, t11FcsStatisticsGroup=t11FcsStatisticsGroup, t11FcsIeType=t11FcsIeType, t11FcsFabricDiscoveryStart=t11FcsFabricDiscoveryStart, t11FcsIeInfoList=t11FcsIeInfoList, t11FcsStats=t11FcsStats, T11FcPortState=T11FcPortState, t11FcsNodeName=t11FcsNodeName, T11FcListIndexPointerOrZero=T11FcListIndexPointerOrZero, t11FcFabricConfigServerMIB=t11FcFabricConfigServerMIB, t11FcsPortPhyPortNum=t11FcsPortPhyPortNum, t11FcsPortSpeedCapab=t11FcsPortSpeedCapab, t11FcsMgmtAddr=t11FcsMgmtAddr, t11FcsStatsTable=t11FcsStatsTable, t11FcsPlatformIndex=t11FcsPlatformIndex, t11FcsFabricDiscoveryRangeLow=t11FcsFabricDiscoveryRangeLow, t11FcsMgmtAddrChangeNotify=t11FcsMgmtAddrChangeNotify, t11FcsPlatformLabel=t11FcsPlatformLabel, t11FcsPlatformProductRevLevel=t11FcsPlatformProductRevLevel, t11FcsMgmtAddrChangeFabricIndex=t11FcsMgmtAddrChangeFabricIndex, t11FcsMgmtAddrListEntry=t11FcsMgmtAddrListEntry, t11FcsNotifications=t11FcsNotifications, T11FcsRejectReasonExplanation=T11FcsRejectReasonExplanation, t11FcsRejects=t11FcsRejects, t11FcsMIBConformance=t11FcsMIBConformance, t11FcsPortTable=t11FcsPortTable, t11FcsFabricDiscoveryTimeOut=t11FcsFabricDiscoveryTimeOut, t11FcsMgmtAddrChangeIeName=t11FcsMgmtAddrChangeIeName, t11FcsPlatformDescription=t11FcsPlatformDescription, t11FcsPlatformNodeNameListIndex=t11FcsPlatformNodeNameListIndex, t11FcsPlatformType=t11FcsPlatformType, t11FcsPlatformTable=t11FcsPlatformTable, t11FcsIeLogicalName=t11FcsIeLogicalName, t11FcsDiscoveryCompleteNotify=t11FcsDiscoveryCompleteNotify, t11FcsRejectReasonCodeExp=t11FcsRejectReasonCodeExp, t11FcsPortOperSpeed=t11FcsPortOperSpeed, t11FcsDiscoveryStatus=t11FcsDiscoveryStatus, t11FcsMgmtAddrChangeNotifyEnable=t11FcsMgmtAddrChangeNotifyEnable, t11FcsIeFabricName=t11FcsIeFabricName, t11FcsNodeNameListIndex=t11FcsNodeNameListIndex, t11FcsDiscoveryStateTable=t11FcsDiscoveryStateTable, T11FcIeType=T11FcIeType, t11FcsPortName=t11FcsPortName, t11FcsNodeNameListEntry=t11FcsNodeNameListEntry)
