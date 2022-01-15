#
# PySNMP MIB module IEEE8021-ECMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-ECMP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ieee8021BridgeBasePort, ieee8021BridgeBasePortComponentId = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort", "ieee8021BridgeBasePortComponentId")
ieee8021QBridgePortVlanStatisticsEntry, ieee8021QBridgeTpFdbEntry = mibBuilder.importSymbols("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgePortVlanStatisticsEntry", "ieee8021QBridgeTpFdbEntry")
ieee8021SpbTopIx, ieee8021SpbmTopSrvTableEntry, IEEE8021SpbBridgePriority = mibBuilder.importSymbols("IEEE8021-SPB-MIB", "ieee8021SpbTopIx", "ieee8021SpbmTopSrvTableEntry", "IEEE8021SpbBridgePriority")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
VlanId, PortList = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "PortList")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
ieee8021EcmpMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 28))
ieee8021EcmpMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2013-05-13 00:00',))
if mibBuilder.loadTexts: ieee8021EcmpMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021EcmpMib.setOrganization('IEEE 802.1 Working Group')
ieee8021EcmpNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 0))
ieee8021EcmpObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 1))
ieee8021EcmpConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 2))
ieee8021QBridgeEcmpFdbTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 1), )
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbTable.setStatus('current')
ieee8021QBridgeEcmpFdbEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 1, 1), )
ieee8021QBridgeTpFdbEntry.registerAugmentions(("IEEE8021-ECMP-MIB", "ieee8021QBridgeEcmpFdbEntry"))
ieee8021QBridgeEcmpFdbEntry.setIndexNames(*ieee8021QBridgeTpFdbEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbEntry.setStatus('current')
ieee8021QBridgeEcmpFdbPortList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 1, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbPortList.setStatus('current')
ieee8021EcmpFlowFilterCtlTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 2), )
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlTable.setStatus('current')
ieee8021EcmpFlowFilterCtlEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlVid"))
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlEntry.setStatus('current')
ieee8021EcmpFlowFilterCtlVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlVid.setStatus('current')
ieee8021EcmpFlowFilterCtlEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlEnabled.setStatus('current')
ieee8021EcmpFlowFilterCtlHashGen = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlHashGen.setStatus('current')
ieee8021EcmpFlowFilterCtlTtl = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlTtl.setStatus('current')
ieee8021EcmpEctStaticTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 3), )
if mibBuilder.loadTexts: ieee8021EcmpEctStaticTable.setStatus('current')
ieee8021EcmpEctStaticEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIx"), (0, "IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryTieBreakMask"))
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntry.setStatus('current')
ieee8021EcmpEctStaticEntryTieBreakMask = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryTieBreakMask.setStatus('current')
ieee8021EcmpEctStaticEntryBridgePriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 2), IEEE8021SpbBridgePriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryBridgePriority.setStatus('current')
ieee8021EcmpEctStaticEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryRowStatus.setStatus('current')
ieee8021EcmpTopSrvTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 4), )
if mibBuilder.loadTexts: ieee8021EcmpTopSrvTable.setStatus('current')
ieee8021EcmpTopSrvEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1), )
ieee8021SpbmTopSrvTableEntry.registerAugmentions(("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvEntry"))
ieee8021EcmpTopSrvEntry.setIndexNames(*ieee8021SpbmTopSrvTableEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntry.setStatus('current')
ieee8021EcmpTopSrvEntryTsBit = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntryTsBit.setStatus('current')
ieee8021EcmpTopSrvEntryTieBreakMask = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntryTieBreakMask.setStatus('current')
ieee8021QBridgePortVlanTtlStatisticsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 5), )
if mibBuilder.loadTexts: ieee8021QBridgePortVlanTtlStatisticsTable.setStatus('current')
ieee8021QBridgePortVlanTtlStatisticsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 5, 1), )
ieee8021QBridgePortVlanStatisticsEntry.registerAugmentions(("IEEE8021-ECMP-MIB", "ieee8021QBridgePortVlanTtlStatisticsEntry"))
ieee8021QBridgePortVlanTtlStatisticsEntry.setIndexNames(*ieee8021QBridgePortVlanStatisticsEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021QBridgePortVlanTtlStatisticsEntry.setStatus('current')
ieee8021QBridgeTpVlanPortTtlDiscards = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 5, 1, 1), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021QBridgeTpVlanPortTtlDiscards.setStatus('current')
ieee8021EcmpGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 2, 1))
ieee8021EcmpCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 2, 2))
ieee8021QBridgeEcmpFdbGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 1)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021QBridgeEcmpFdbPortList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021QBridgeEcmpFdbGroup = ieee8021QBridgeEcmpFdbGroup.setStatus('current')
ieee8021EcmpFlowFilterCtlGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 2)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlEnabled"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlHashGen"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlTtl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpFlowFilterCtlGroup = ieee8021EcmpFlowFilterCtlGroup.setStatus('current')
ieee8021EcmpEctStaticGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 3)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryBridgePriority"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpEctStaticGroup = ieee8021EcmpEctStaticGroup.setStatus('current')
ieee8021EcmpTopSrvGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 4)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvEntryTsBit"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvEntryTieBreakMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpTopSrvGroup = ieee8021EcmpTopSrvGroup.setStatus('current')
ieee8021QBridgePortVlanTtlStatisticsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 5)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021QBridgeTpVlanPortTtlDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021QBridgePortVlanTtlStatisticsGroup = ieee8021QBridgePortVlanTtlStatisticsGroup.setStatus('current')
ieee8021EcmpCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 28, 2, 2, 1)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021QBridgeEcmpFdbGroup"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticGroup"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpCompliance = ieee8021EcmpCompliance.setStatus('current')
ieee8021EcmpFlowFilteringCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 28, 2, 2, 2)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlGroup"), ("IEEE8021-ECMP-MIB", "ieee8021QBridgePortVlanTtlStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpFlowFilteringCompliance = ieee8021EcmpFlowFilteringCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-ECMP-MIB", ieee8021EcmpFlowFilterCtlEntry=ieee8021EcmpFlowFilterCtlEntry, ieee8021QBridgeEcmpFdbEntry=ieee8021QBridgeEcmpFdbEntry, ieee8021QBridgeEcmpFdbTable=ieee8021QBridgeEcmpFdbTable, ieee8021EcmpTopSrvGroup=ieee8021EcmpTopSrvGroup, ieee8021EcmpGroups=ieee8021EcmpGroups, ieee8021EcmpEctStaticEntryBridgePriority=ieee8021EcmpEctStaticEntryBridgePriority, ieee8021QBridgePortVlanTtlStatisticsGroup=ieee8021QBridgePortVlanTtlStatisticsGroup, ieee8021EcmpFlowFilterCtlEnabled=ieee8021EcmpFlowFilterCtlEnabled, ieee8021EcmpConformance=ieee8021EcmpConformance, ieee8021EcmpFlowFilterCtlGroup=ieee8021EcmpFlowFilterCtlGroup, ieee8021EcmpMib=ieee8021EcmpMib, ieee8021EcmpTopSrvTable=ieee8021EcmpTopSrvTable, ieee8021EcmpTopSrvEntryTieBreakMask=ieee8021EcmpTopSrvEntryTieBreakMask, ieee8021EcmpFlowFilterCtlTtl=ieee8021EcmpFlowFilterCtlTtl, ieee8021EcmpFlowFilterCtlVid=ieee8021EcmpFlowFilterCtlVid, ieee8021EcmpEctStaticEntryTieBreakMask=ieee8021EcmpEctStaticEntryTieBreakMask, ieee8021EcmpTopSrvEntryTsBit=ieee8021EcmpTopSrvEntryTsBit, ieee8021EcmpNotifications=ieee8021EcmpNotifications, ieee8021QBridgeEcmpFdbPortList=ieee8021QBridgeEcmpFdbPortList, ieee8021EcmpObjects=ieee8021EcmpObjects, ieee8021EcmpEctStaticGroup=ieee8021EcmpEctStaticGroup, ieee8021QBridgePortVlanTtlStatisticsEntry=ieee8021QBridgePortVlanTtlStatisticsEntry, ieee8021EcmpEctStaticEntry=ieee8021EcmpEctStaticEntry, ieee8021EcmpFlowFilterCtlHashGen=ieee8021EcmpFlowFilterCtlHashGen, ieee8021EcmpEctStaticTable=ieee8021EcmpEctStaticTable, ieee8021EcmpCompliances=ieee8021EcmpCompliances, ieee8021EcmpFlowFilteringCompliance=ieee8021EcmpFlowFilteringCompliance, PYSNMP_MODULE_ID=ieee8021EcmpMib, ieee8021QBridgeTpVlanPortTtlDiscards=ieee8021QBridgeTpVlanPortTtlDiscards, ieee8021EcmpTopSrvEntry=ieee8021EcmpTopSrvEntry, ieee8021QBridgeEcmpFdbGroup=ieee8021QBridgeEcmpFdbGroup, ieee8021EcmpFlowFilterCtlTable=ieee8021EcmpFlowFilterCtlTable, ieee8021QBridgePortVlanTtlStatisticsTable=ieee8021QBridgePortVlanTtlStatisticsTable, ieee8021EcmpEctStaticEntryRowStatus=ieee8021EcmpEctStaticEntryRowStatus, ieee8021EcmpCompliance=ieee8021EcmpCompliance)
