#
# PySNMP MIB module ADTRAN-AOS-MUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-MUX-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:43 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, ObjectIdentity, Counter32, Bits, Integer32, TimeTicks, Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Counter32", "Bits", "Integer32", "TimeTicks", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Gauge32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
adGenAOSMuxID = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 5))
if mibBuilder.loadTexts: adGenAOSMuxID.setLastUpdated('200410150000Z')
if mibBuilder.loadTexts: adGenAOSMuxID.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSMuxID.setContactInfo('Technical Support Dept.\n                 Postal: ADTRAN, Inc.\n                         901 Explorer Blvd.\n                         Huntsville, AL 35806\n\n                         Tel: +1 800 726-8663\n                         Fax: +1 256 963 6217\n                         E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSMuxID.setDescription('The MIB module for the management of AOS products with\n                 TDM multiplexing and/or cross-connects.')
adGenAOSMux = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5))
adGenAOSXConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1))
adGenAOSTdmGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2))
adGenAOSMuxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99))
adGenAOSMuxCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 1))
adGenAOSMuxMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 2))
adGenAOSXConnectTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1), )
if mibBuilder.loadTexts: adGenAOSXConnectTable.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectTable.setDescription('The Cross-Connect Configuration Table')
adGenAOSXConnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1), ).setIndexNames((0, "ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectIndex"))
if mibBuilder.loadTexts: adGenAOSXConnectEntry.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectEntry.setDescription('An entry in the Cross-Connect Configuration Table')
adGenAOSXConnectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectIndex.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectIndex.setDescription('A number that uniquely defines the cross-connect')
adGenAOSXConnectFirstIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("notAssigned", 0), ("dds", 1), ("t1E1", 2), ("eth", 3), ("serial", 4), ("shdsl", 5), ("fxs", 6), ("frameRelay", 7), ("ppp", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectFirstIfType.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectFirstIfType.setDescription('The type of interface from which a cross-connect is being\n     made')
adGenAOSXConnectFirstIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectFirstIfNumber.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectFirstIfNumber.setDescription('A number that defines the interface described by\n     adGenAOSXConnectFirstIfType -- set to 0 if the interface\n     can be defined by adGenAOSXConnectFirstIfSlot and\n     adGenAOSXConnectFirstIfPort')
adGenAOSXConnectFirstSubIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1007))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectFirstSubIfNumber.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectFirstSubIfNumber.setDescription('A number that further defines some interfaces -- set to\n     0 if the interface can be defined by adGenAOSXConnectFirstIfSlot\n     and adGenAOSXConnectFirstIfPort')
adGenAOSXConnectFirstIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectFirstIfSlot.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectFirstIfSlot.setDescription('The slot number containing the interface described by\n     adGenAOSXConnectFirstIfType -- set to 0 if the interface\n     can be defined by adGenAOSXConnectFirstIfNumber (and\n     adGenAOSXConnectFirstSubIfNumber)\n\n     Note: 0 is also a valid slot number.')
adGenAOSXConnectFirstIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 48))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectFirstIfPort.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectFirstIfPort.setDescription('The port number of the interface described by\n     adGenAOSXConnectFirstIfType -- set to 0 if the interface\n     can be defined by adGenAOSXConnectFirstIfNumber (and\n     adGenAOSXConnectFirstSubIfNumber)')
adGenAOSXConnectFirstTdmGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectFirstTdmGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectFirstTdmGroup.setDescription('A number uniquely identifying the TDM Group associated\n     with the interface described by adGenAOSXConnectFirstIfType\n     -- set to 0 if it is not necessary that a TDM Group be\n     associated with the interface')
adGenAOSXConnectFirstTdmGroupDS0 = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectFirstTdmGroupDS0.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectFirstTdmGroupDS0.setDescription('The specific DS0 of the TDM Group, described by\n     adGenAOSXConnectFirstTdmGroup, from which a cross-\n     connect is being made -- set to 0 if it is not necessary\n     that a specific timeslot be defined')
adGenAOSXConnectSecondIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("notAssigned", 0), ("dds", 1), ("t1E1", 2), ("eth", 3), ("serial", 4), ("shdsl", 5), ("fxs", 6), ("frameRelay", 7), ("ppp", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectSecondIfType.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectSecondIfType.setDescription('The type of interface to which a cross-connect is being\n     made')
adGenAOSXConnectSecondIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectSecondIfNumber.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectSecondIfNumber.setDescription('A number that defines the interface described by\n     adGenAOSXConnectSecondIfType -- set to 0 if the interface\n     can be defined by adGenAOSXConnectSecondIfSlot and\n     adGenAOSXConnectSecondIfPort')
adGenAOSXConnectSecondSubIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1007))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectSecondSubIfNumber.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectSecondSubIfNumber.setDescription('A number that further defines some interfaces -- set to\n     0 if the interface can be defined by adGenAOSXConnectSecondIfSlot\n     and adGenAOSXConnectSecondIfPort')
adGenAOSXConnectSecondIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectSecondIfSlot.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectSecondIfSlot.setDescription('The slot number containing the interface described by\n     adGenAOSXConnectSecondIfType -- set to 0 if the interface\n     can be defined by adGenAOSXConnectSecondIfNumber (and\n     adGenAOSXConnectSecondSubIfNumber)\n\n     Note: 0 is also a valid slot number.')
adGenAOSXConnectSecondIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 48))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectSecondIfPort.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectSecondIfPort.setDescription('The port number of the interface described by\n     adGenAOSXConnectSecondIfType -- set to 0 if the interface\n     can be defined by adGenAOSXConnectSecondIfNumber (and\n     adGenAOSXConnectSecondSubIfNumber)')
adGenAOSXConnectSecondTdmGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectSecondTdmGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectSecondTdmGroup.setDescription('A number uniquely identifying the TDM Group associated\n     with the interface described by adGenAOSXConnectSecondIfType\n     -- set to 0 if it is not necessary that a TDM Group be\n     associated with the interface')
adGenAOSXConnectSecondTdmGroupDS0 = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectSecondTdmGroupDS0.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectSecondTdmGroupDS0.setDescription('The specific DS0 of the TDM Group, described by\n     adGenAOSXConnectSecondTdmGroup, to which a cross-\n     connect is being made -- set to 0 if it is not necessary\n     that a specific timeslot be defined')
adGenAOSXConnectPreserveRbs = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectPreserveRbs.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectPreserveRbs.setDescription('The ability of the cross-connect to maintain robbed-bit\n     signaling integrity -- set to disabled if robbed-bit\n     signaling is not a characteristic of the cross-connect.')
adGenAOSXConnectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSXConnectRowStatus.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectRowStatus.setDescription("The status of this conceptual row.  Until instances\n     of appropriate corresponding columns are configured,\n     the value of the corresponding instance of the\n     adGenAOSXConnectStatus column is 'notReady'.")
adGenAOSTdmGroupTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1), )
if mibBuilder.loadTexts: adGenAOSTdmGroupTable.setStatus('current')
if mibBuilder.loadTexts: adGenAOSTdmGroupTable.setDescription('The TDM Group Table that associates DS0s into mappable\n    units')
adGenAOSTdmGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1), ).setIndexNames((0, "ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupIfSlot"), (0, "ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupIfPort"), (0, "ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupID"))
if mibBuilder.loadTexts: adGenAOSTdmGroupEntry.setStatus('current')
if mibBuilder.loadTexts: adGenAOSTdmGroupEntry.setDescription('An entry in the TDM Group Table')
adGenAOSTdmGroupIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSTdmGroupIfSlot.setStatus('current')
if mibBuilder.loadTexts: adGenAOSTdmGroupIfSlot.setDescription('The slot number containing the interface for\n    the TDM Group')
adGenAOSTdmGroupIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSTdmGroupIfPort.setStatus('current')
if mibBuilder.loadTexts: adGenAOSTdmGroupIfPort.setDescription('The port number containing the interface for\n    the TDM Group')
adGenAOSTdmGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSTdmGroupID.setStatus('current')
if mibBuilder.loadTexts: adGenAOSTdmGroupID.setDescription('A number that uniquely defines the TDM Group')
adGenAOSTdmGroupMask = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSTdmGroupMask.setStatus('current')
if mibBuilder.loadTexts: adGenAOSTdmGroupMask.setDescription('A bitmap of the contiguous DS0s included in this TDM Group\n\n     Example: mapping DS0s 1-12:\n        00000000000000000000111111111111 (bin),\n        00000FFF (hex),\n        4095 (dec)\n\n     Note: To create a new row in adGenAOSTdmGroupTable,\n           set adGenAOSTdmGroupMask with the appropriate\n           index values corresponding to the desired slot,\n           port, and TDM group ID')
adGenAOSTdmGroupUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fiftySixKbps", 1), ("sixtyFourKbps", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSTdmGroupUsage.setStatus('current')
if mibBuilder.loadTexts: adGenAOSTdmGroupUsage.setDescription('The speed of the individual DS0s')
adGenAOSMuxConformancemModule = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 1, 1)).setObjects(("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectGrp"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupGrp"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSMuxConformancemModule = adGenAOSMuxConformancemModule.setStatus('current')
if mibBuilder.loadTexts: adGenAOSMuxConformancemModule.setDescription('The compliance statement for SNMPv2 entities which\n         implement the adGenAOSMux MIB.')
adGenAOSXConnectGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 2, 1)).setObjects(("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectIndex"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstIfType"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstIfNumber"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstSubIfNumber"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstIfSlot"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstIfPort"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstTdmGroup"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstTdmGroupDS0"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondIfType"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondIfNumber"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondSubIfNumber"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondIfSlot"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondIfPort"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondTdmGroup"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondTdmGroupDS0"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectPreserveRbs"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSXConnectGrp = adGenAOSXConnectGrp.setStatus('current')
if mibBuilder.loadTexts: adGenAOSXConnectGrp.setDescription('The Cross-Connect Group.')
adGenAOSTdmGroupGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 2, 2)).setObjects(("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupIfSlot"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupIfPort"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupID"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupMask"), ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSTdmGroupGrp = adGenAOSTdmGroupGrp.setStatus('current')
if mibBuilder.loadTexts: adGenAOSTdmGroupGrp.setDescription('The TDM Group Group.')
mibBuilder.exportSymbols("ADTRAN-AOS-MUX-MIB", PYSNMP_MODULE_ID=adGenAOSMuxID, adGenAOSXConnectFirstIfSlot=adGenAOSXConnectFirstIfSlot, adGenAOSMuxID=adGenAOSMuxID, adGenAOSXConnectIndex=adGenAOSXConnectIndex, adGenAOSMuxConformancemModule=adGenAOSMuxConformancemModule, adGenAOSXConnectGrp=adGenAOSXConnectGrp, adGenAOSXConnectSecondIfPort=adGenAOSXConnectSecondIfPort, adGenAOSMuxCompliance=adGenAOSMuxCompliance, adGenAOSMuxMibGroups=adGenAOSMuxMibGroups, adGenAOSMuxConformance=adGenAOSMuxConformance, adGenAOSXConnectRowStatus=adGenAOSXConnectRowStatus, adGenAOSXConnectSecondTdmGroup=adGenAOSXConnectSecondTdmGroup, adGenAOSTdmGroupIfSlot=adGenAOSTdmGroupIfSlot, adGenAOSXConnectSecondSubIfNumber=adGenAOSXConnectSecondSubIfNumber, adGenAOSTdmGroup=adGenAOSTdmGroup, adGenAOSXConnectFirstTdmGroup=adGenAOSXConnectFirstTdmGroup, adGenAOSXConnectFirstIfPort=adGenAOSXConnectFirstIfPort, adGenAOSXConnectEntry=adGenAOSXConnectEntry, adGenAOSXConnectFirstSubIfNumber=adGenAOSXConnectFirstSubIfNumber, adGenAOSTdmGroupMask=adGenAOSTdmGroupMask, adGenAOSTdmGroupGrp=adGenAOSTdmGroupGrp, adGenAOSXConnectTable=adGenAOSXConnectTable, adGenAOSXConnectFirstTdmGroupDS0=adGenAOSXConnectFirstTdmGroupDS0, adGenAOSXConnectSecondTdmGroupDS0=adGenAOSXConnectSecondTdmGroupDS0, adGenAOSMux=adGenAOSMux, adGenAOSXConnectFirstIfType=adGenAOSXConnectFirstIfType, adGenAOSXConnectPreserveRbs=adGenAOSXConnectPreserveRbs, adGenAOSTdmGroupTable=adGenAOSTdmGroupTable, adGenAOSXConnectSecondIfNumber=adGenAOSXConnectSecondIfNumber, adGenAOSXConnectSecondIfSlot=adGenAOSXConnectSecondIfSlot, adGenAOSTdmGroupID=adGenAOSTdmGroupID, adGenAOSXConnect=adGenAOSXConnect, adGenAOSXConnectFirstIfNumber=adGenAOSXConnectFirstIfNumber, adGenAOSXConnectSecondIfType=adGenAOSXConnectSecondIfType, adGenAOSTdmGroupIfPort=adGenAOSTdmGroupIfPort, adGenAOSTdmGroupEntry=adGenAOSTdmGroupEntry, adGenAOSTdmGroupUsage=adGenAOSTdmGroupUsage)
