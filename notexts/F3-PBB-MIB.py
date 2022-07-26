#
# PySNMP MIB module F3-PBB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-PBB-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:47 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
PerfCounter64, = mibBuilder.importSymbols("CM-COMMON-MIB", "PerfCounter64")
FlowTagControl, cmEthernetNetPortEntry, cmEthernetAccPortEntry, cmFlowEntry = mibBuilder.importSymbols("CM-FACILITY-MIB", "FlowTagControl", "cmEthernetNetPortEntry", "cmEthernetAccPortEntry", "cmFlowEntry")
ipManagementTunnelEntry, = mibBuilder.importSymbols("CM-IP-MIB", "ipManagementTunnelEntry")
cmEthernetNetPortHistoryEntry, cmEthernetNetPortStatsEntry = mibBuilder.importSymbols("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryEntry", "cmEthernetNetPortStatsEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, NotificationType, IpAddress, ModuleIdentity, TimeTicks, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "IpAddress", "ModuleIdentity", "TimeTicks", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier")
VariablePointer, DisplayString, MacAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "VariablePointer", "DisplayString", "MacAddress", "TruthValue", "TextualConvention")
f3PBBMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21))
f3PBBMIB.setRevisions(('2012-10-08 00:00',))
if mibBuilder.loadTexts: f3PBBMIB.setLastUpdated('201210080000Z')
if mibBuilder.loadTexts: f3PBBMIB.setOrganization('ADVA Optical Networking')
f3PBBConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1))
f3PBBPerformanceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2))
f3PBBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3))
f3PbbEthernetAccPortTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1), )
if mibBuilder.loadTexts: f3PbbEthernetAccPortTable.setStatus('current')
f3PbbEthernetAccPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1), )
cmEthernetAccPortEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbEthernetAccPortEntry"))
f3PbbEthernetAccPortEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbEthernetAccPortEntry.setStatus('current')
f3PbbEthernetAccPortITagLoopbackMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopbackMask.setStatus('current')
f3PbbEthernetAccPortITagLoopback1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback1.setStatus('current')
f3PbbEthernetAccPortITagLoopback2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback2.setStatus('current')
f3PbbEthernetAccPortITagLoopback3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback3.setStatus('current')
f3PbbEthernetNetPortTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2), )
if mibBuilder.loadTexts: f3PbbEthernetNetPortTable.setStatus('current')
f3PbbEthernetNetPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1), )
cmEthernetNetPortEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbEthernetNetPortEntry"))
f3PbbEthernetNetPortEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbEthernetNetPortEntry.setStatus('current')
f3PbbEthernetNetPortBackboneMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortBackboneMacAddress.setStatus('current')
f3PbbEthernetNetPortITagLoopbackMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopbackMask.setStatus('current')
f3PbbEthernetNetPortITagLoopback1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback1.setStatus('current')
f3PbbEthernetNetPortITagLoopback2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback2.setStatus('current')
f3PbbEthernetNetPortITagLoopback3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback3.setStatus('current')
f3PbbFlowTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3), )
if mibBuilder.loadTexts: f3PbbFlowTable.setStatus('current')
f3PbbFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1), )
cmFlowEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbFlowEntry"))
f3PbbFlowEntry.setIndexNames(*cmFlowEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbFlowEntry.setStatus('current')
f3PbbFlowITagControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 1), FlowTagControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowITagControl.setStatus('current')
f3PbbFlowITagISID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(256, 16777214))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowITagISID.setStatus('current')
f3PbbFlowITagPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowITagPriority.setStatus('current')
f3PbbFlowBackboneMacDestinationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowBackboneMacDestinationEnabled.setStatus('current')
f3PbbFlowBackboneMacDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 5), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowBackboneMacDestinationAddress.setStatus('current')
f3PbbFlowA2NPbbCapableFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowA2NPbbCapableFlag.setStatus('current')
f3PbbIpManagementTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4), )
if mibBuilder.loadTexts: f3PbbIpManagementTunnelTable.setStatus('current')
f3PbbIpManagementTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1), )
ipManagementTunnelEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbIpManagementTunnelEntry"))
f3PbbIpManagementTunnelEntry.setIndexNames(*ipManagementTunnelEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbIpManagementTunnelEntry.setStatus('current')
f3PbbIpManagementTunnelItagEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelItagEnabled.setStatus('current')
f3PbbIpManagementTunnelISID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(256, 16777214))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelISID.setStatus('current')
f3PbbIpManagementTunnelIPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelIPriority.setStatus('current')
f3PbbIpManagementTunnelBackboneMacDestinationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelBackboneMacDestinationEnabled.setStatus('current')
f3PbbIpManagementTunnelBackboneMacDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 5), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelBackboneMacDestinationAddress.setStatus('current')
f3PbbEthernetNetPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1), )
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsTable.setStatus('current')
f3PbbEthernetNetPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1), )
cmEthernetNetPortStatsEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbEthernetNetPortStatsEntry"))
f3PbbEthernetNetPortStatsEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsEntry.setStatus('current')
f3PbbEthernetNetPortStatsPbbUniBdaDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsPbbUniBdaDiscard.setStatus('current')
f3PbbEthernetNetPortStatsPbbGroupBdaDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1, 2), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsPbbGroupBdaDiscard.setStatus('current')
f3PbbEthernetNetPortHistoryStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2), )
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsTable.setStatus('current')
f3PbbEthernetNetPortHistoryStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1), )
cmEthernetNetPortHistoryEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbEthernetNetPortHistoryStatsEntry"))
f3PbbEthernetNetPortHistoryStatsEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsEntry.setStatus('current')
f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard.setStatus('current')
f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1, 2), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard.setStatus('current')
f3PBBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 1))
f3PBBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2))
f3PBBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 1, 1)).setObjects(("F3-PBB-MIB", "f3PbbConfigGroup"), ("F3-PBB-MIB", "f3PbbStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PBBCompliance = f3PBBCompliance.setStatus('current')
f3PbbConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2, 1)).setObjects(("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopbackMask"), ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback1"), ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback2"), ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback3"), ("F3-PBB-MIB", "f3PbbEthernetNetPortBackboneMacAddress"), ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopbackMask"), ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback1"), ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback2"), ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback3"), ("F3-PBB-MIB", "f3PbbFlowITagControl"), ("F3-PBB-MIB", "f3PbbFlowITagISID"), ("F3-PBB-MIB", "f3PbbFlowITagPriority"), ("F3-PBB-MIB", "f3PbbFlowBackboneMacDestinationEnabled"), ("F3-PBB-MIB", "f3PbbFlowBackboneMacDestinationAddress"), ("F3-PBB-MIB", "f3PbbFlowA2NPbbCapableFlag"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelItagEnabled"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelISID"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelIPriority"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelBackboneMacDestinationEnabled"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelBackboneMacDestinationAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PbbConfigGroup = f3PbbConfigGroup.setStatus('current')
f3PbbStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2, 2)).setObjects(("F3-PBB-MIB", "f3PbbEthernetNetPortStatsPbbUniBdaDiscard"), ("F3-PBB-MIB", "f3PbbEthernetNetPortStatsPbbGroupBdaDiscard"), ("F3-PBB-MIB", "f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard"), ("F3-PBB-MIB", "f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PbbStatsGroup = f3PbbStatsGroup.setStatus('current')
mibBuilder.exportSymbols("F3-PBB-MIB", f3PBBGroups=f3PBBGroups, f3PbbIpManagementTunnelTable=f3PbbIpManagementTunnelTable, f3PbbEthernetNetPortITagLoopback2=f3PbbEthernetNetPortITagLoopback2, f3PbbEthernetNetPortHistoryStatsTable=f3PbbEthernetNetPortHistoryStatsTable, f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard=f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard, f3PbbEthernetNetPortBackboneMacAddress=f3PbbEthernetNetPortBackboneMacAddress, f3PbbEthernetNetPortStatsEntry=f3PbbEthernetNetPortStatsEntry, f3PbbFlowITagControl=f3PbbFlowITagControl, f3PbbFlowTable=f3PbbFlowTable, f3PbbEthernetNetPortITagLoopback1=f3PbbEthernetNetPortITagLoopback1, f3PbbEthernetNetPortITagLoopback3=f3PbbEthernetNetPortITagLoopback3, f3PbbIpManagementTunnelEntry=f3PbbIpManagementTunnelEntry, f3PbbEthernetNetPortHistoryStatsEntry=f3PbbEthernetNetPortHistoryStatsEntry, f3PBBMIB=f3PBBMIB, f3PBBConfigObjects=f3PBBConfigObjects, f3PbbConfigGroup=f3PbbConfigGroup, f3PbbEthernetAccPortITagLoopback3=f3PbbEthernetAccPortITagLoopback3, f3PbbEthernetNetPortTable=f3PbbEthernetNetPortTable, f3PbbFlowA2NPbbCapableFlag=f3PbbFlowA2NPbbCapableFlag, f3PbbIpManagementTunnelISID=f3PbbIpManagementTunnelISID, f3PbbIpManagementTunnelBackboneMacDestinationEnabled=f3PbbIpManagementTunnelBackboneMacDestinationEnabled, f3PbbEthernetNetPortStatsPbbGroupBdaDiscard=f3PbbEthernetNetPortStatsPbbGroupBdaDiscard, f3PbbEthernetAccPortITagLoopback2=f3PbbEthernetAccPortITagLoopback2, f3PbbFlowBackboneMacDestinationEnabled=f3PbbFlowBackboneMacDestinationEnabled, f3PbbEthernetNetPortStatsPbbUniBdaDiscard=f3PbbEthernetNetPortStatsPbbUniBdaDiscard, f3PbbStatsGroup=f3PbbStatsGroup, PYSNMP_MODULE_ID=f3PBBMIB, f3PbbEthernetNetPortEntry=f3PbbEthernetNetPortEntry, f3PbbEthernetNetPortStatsTable=f3PbbEthernetNetPortStatsTable, f3PbbIpManagementTunnelItagEnabled=f3PbbIpManagementTunnelItagEnabled, f3PbbFlowITagISID=f3PbbFlowITagISID, f3PBBCompliances=f3PBBCompliances, f3PBBConformance=f3PBBConformance, f3PbbFlowEntry=f3PbbFlowEntry, f3PbbFlowBackboneMacDestinationAddress=f3PbbFlowBackboneMacDestinationAddress, f3PbbEthernetNetPortITagLoopbackMask=f3PbbEthernetNetPortITagLoopbackMask, f3PbbEthernetAccPortITagLoopback1=f3PbbEthernetAccPortITagLoopback1, f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard=f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard, f3PBBCompliance=f3PBBCompliance, f3PbbEthernetAccPortEntry=f3PbbEthernetAccPortEntry, f3PbbEthernetAccPortTable=f3PbbEthernetAccPortTable, f3PbbIpManagementTunnelIPriority=f3PbbIpManagementTunnelIPriority, f3PbbFlowITagPriority=f3PbbFlowITagPriority, f3PbbIpManagementTunnelBackboneMacDestinationAddress=f3PbbIpManagementTunnelBackboneMacDestinationAddress, f3PBBPerformanceObjects=f3PBBPerformanceObjects, f3PbbEthernetAccPortITagLoopbackMask=f3PbbEthernetAccPortITagLoopbackMask)
