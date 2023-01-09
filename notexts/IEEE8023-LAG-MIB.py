#
# PySNMP MIB module IEEE8023-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IEEE8023-LAG-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:30 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Counter64, iso, Bits, Integer32, ObjectIdentity, IpAddress, Counter32, Gauge32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "iso", "Bits", "Integer32", "ObjectIdentity", "IpAddress", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity")
DisplayString, MacAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TruthValue", "TextualConvention")
lagMIB = ModuleIdentity((1, 2, 840, 10006, 300, 43))
if mibBuilder.loadTexts: lagMIB.setLastUpdated('200211211623Z')
if mibBuilder.loadTexts: lagMIB.setOrganization('IEEE 802.3ad Working Group')
lagMIBObjects = MibIdentifier((1, 2, 840, 10006, 300, 43, 1))
class LacpKey(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LacpState(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lacpActivity", 0), ("lacpTimeout", 1), ("aggregation", 2), ("synchronization", 3), ("collecting", 4), ("distributing", 5), ("defaulted", 6), ("expired", 7))

class ChurnState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noChurn", 1), ("churn", 2), ("churnMonitor", 3))

dot3adAgg = MibIdentifier((1, 2, 840, 10006, 300, 43, 1, 1))
dot3adAggPort = MibIdentifier((1, 2, 840, 10006, 300, 43, 1, 2))
dot3adTablesLastChanged = MibScalar((1, 2, 840, 10006, 300, 43, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adTablesLastChanged.setStatus('current')
dot3adAggTable = MibTable((1, 2, 840, 10006, 300, 43, 1, 1, 1), )
if mibBuilder.loadTexts: dot3adAggTable.setStatus('current')
dot3adAggEntry = MibTableRow((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggIndex"))
if mibBuilder.loadTexts: dot3adAggEntry.setStatus('current')
dot3adAggIndex = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dot3adAggIndex.setStatus('current')
dot3adAggMACAddress = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggMACAddress.setStatus('current')
dot3adAggActorSystemPriority = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggActorSystemPriority.setStatus('current')
dot3adAggActorSystemID = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggActorSystemID.setStatus('current')
dot3adAggAggregateOrIndividual = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggAggregateOrIndividual.setStatus('current')
dot3adAggActorAdminKey = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 6), LacpKey()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggActorAdminKey.setStatus('current')
dot3adAggActorOperKey = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 7), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggActorOperKey.setStatus('current')
dot3adAggPartnerSystemID = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPartnerSystemID.setStatus('current')
dot3adAggPartnerSystemPriority = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPartnerSystemPriority.setStatus('current')
dot3adAggPartnerOperKey = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 10), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPartnerOperKey.setStatus('current')
dot3adAggCollectorMaxDelay = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggCollectorMaxDelay.setStatus('current')
dot3adAggPortListTable = MibTable((1, 2, 840, 10006, 300, 43, 1, 1, 2), )
if mibBuilder.loadTexts: dot3adAggPortListTable.setStatus('current')
dot3adAggPortListEntry = MibTableRow((1, 2, 840, 10006, 300, 43, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggIndex"))
if mibBuilder.loadTexts: dot3adAggPortListEntry.setStatus('current')
dot3adAggPortListPorts = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 1, 2, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortListPorts.setStatus('current')
dot3adAggPortTable = MibTable((1, 2, 840, 10006, 300, 43, 1, 2, 1), )
if mibBuilder.loadTexts: dot3adAggPortTable.setStatus('current')
dot3adAggPortEntry = MibTableRow((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"))
if mibBuilder.loadTexts: dot3adAggPortEntry.setStatus('current')
dot3adAggPortIndex = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dot3adAggPortIndex.setStatus('current')
dot3adAggPortActorSystemPriority = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortActorSystemPriority.setStatus('current')
dot3adAggPortActorSystemID = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorSystemID.setStatus('current')
dot3adAggPortActorAdminKey = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 4), LacpKey()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortActorAdminKey.setStatus('current')
dot3adAggPortActorOperKey = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 5), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorOperKey.setStatus('current')
dot3adAggPortPartnerAdminSystemPriority = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminSystemPriority.setStatus('current')
dot3adAggPortPartnerOperSystemPriority = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperSystemPriority.setStatus('current')
dot3adAggPortPartnerAdminSystemID = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 8), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminSystemID.setStatus('current')
dot3adAggPortPartnerOperSystemID = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperSystemID.setStatus('current')
dot3adAggPortPartnerAdminKey = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 10), LacpKey()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminKey.setStatus('current')
dot3adAggPortPartnerOperKey = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 11), LacpKey()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperKey.setStatus('current')
dot3adAggPortSelectedAggID = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 12), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortSelectedAggID.setStatus('current')
dot3adAggPortAttachedAggID = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 13), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortAttachedAggID.setStatus('current')
dot3adAggPortActorPort = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorPort.setStatus('current')
dot3adAggPortActorPortPriority = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortActorPortPriority.setStatus('current')
dot3adAggPortPartnerAdminPort = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminPort.setStatus('current')
dot3adAggPortPartnerOperPort = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperPort.setStatus('current')
dot3adAggPortPartnerAdminPortPriority = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminPortPriority.setStatus('current')
dot3adAggPortPartnerOperPortPriority = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperPortPriority.setStatus('current')
dot3adAggPortActorAdminState = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 20), LacpState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortActorAdminState.setStatus('current')
dot3adAggPortActorOperState = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 21), LacpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortActorOperState.setStatus('current')
dot3adAggPortPartnerAdminState = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 22), LacpState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3adAggPortPartnerAdminState.setStatus('current')
dot3adAggPortPartnerOperState = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 23), LacpState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortPartnerOperState.setStatus('current')
dot3adAggPortAggregateOrIndividual = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 1, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortAggregateOrIndividual.setStatus('current')
dot3adAggPortStatsTable = MibTable((1, 2, 840, 10006, 300, 43, 1, 2, 2), )
if mibBuilder.loadTexts: dot3adAggPortStatsTable.setStatus('current')
dot3adAggPortStatsEntry = MibTableRow((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"))
if mibBuilder.loadTexts: dot3adAggPortStatsEntry.setStatus('current')
dot3adAggPortStatsLACPDUsRx = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsLACPDUsRx.setStatus('current')
dot3adAggPortStatsMarkerPDUsRx = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsMarkerPDUsRx.setStatus('current')
dot3adAggPortStatsMarkerResponsePDUsRx = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsMarkerResponsePDUsRx.setStatus('current')
dot3adAggPortStatsUnknownRx = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsUnknownRx.setStatus('current')
dot3adAggPortStatsIllegalRx = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsIllegalRx.setStatus('current')
dot3adAggPortStatsLACPDUsTx = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsLACPDUsTx.setStatus('current')
dot3adAggPortStatsMarkerPDUsTx = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsMarkerPDUsTx.setStatus('current')
dot3adAggPortStatsMarkerResponsePDUsTx = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortStatsMarkerResponsePDUsTx.setStatus('current')
dot3adAggPortDebugTable = MibTable((1, 2, 840, 10006, 300, 43, 1, 2, 3), )
if mibBuilder.loadTexts: dot3adAggPortDebugTable.setStatus('current')
dot3adAggPortDebugEntry = MibTableRow((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1), ).setIndexNames((0, "IEEE8023-LAG-MIB", "dot3adAggPortIndex"))
if mibBuilder.loadTexts: dot3adAggPortDebugEntry.setStatus('current')
dot3adAggPortDebugRxState = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("currenT", 1), ("expired", 2), ("defaulted", 3), ("initialize", 4), ("lacpDisabled", 5), ("portDisabled", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugRxState.setStatus('current')
dot3adAggPortDebugLastRxTime = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugLastRxTime.setStatus('current')
dot3adAggPortDebugMuxState = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("detached", 1), ("waiting", 2), ("attached", 3), ("collecting", 4), ("distributing", 5), ("collectingDistributing", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugMuxState.setStatus('current')
dot3adAggPortDebugMuxReason = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugMuxReason.setStatus('current')
dot3adAggPortDebugActorChurnState = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 5), ChurnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugActorChurnState.setStatus('current')
dot3adAggPortDebugPartnerChurnState = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 6), ChurnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugPartnerChurnState.setStatus('current')
dot3adAggPortDebugActorChurnCount = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugActorChurnCount.setStatus('current')
dot3adAggPortDebugPartnerChurnCount = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugPartnerChurnCount.setStatus('current')
dot3adAggPortDebugActorSyncTransitionCount = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugActorSyncTransitionCount.setStatus('current')
dot3adAggPortDebugPartnerSyncTransitionCount = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugPartnerSyncTransitionCount.setStatus('current')
dot3adAggPortDebugActorChangeCount = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugActorChangeCount.setStatus('current')
dot3adAggPortDebugPartnerChangeCount = MibTableColumn((1, 2, 840, 10006, 300, 43, 1, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3adAggPortDebugPartnerChangeCount.setStatus('current')
dot3adAggConformance = MibIdentifier((1, 2, 840, 10006, 300, 43, 2))
dot3adAggGroups = MibIdentifier((1, 2, 840, 10006, 300, 43, 2, 1))
dot3adAggCompliances = MibIdentifier((1, 2, 840, 10006, 300, 43, 2, 2))
dot3adAggGroup = ObjectGroup((1, 2, 840, 10006, 300, 43, 2, 1, 1)).setObjects(("IEEE8023-LAG-MIB", "dot3adAggActorSystemID"), ("IEEE8023-LAG-MIB", "dot3adAggActorSystemPriority"), ("IEEE8023-LAG-MIB", "dot3adAggAggregateOrIndividual"), ("IEEE8023-LAG-MIB", "dot3adAggActorAdminKey"), ("IEEE8023-LAG-MIB", "dot3adAggMACAddress"), ("IEEE8023-LAG-MIB", "dot3adAggActorOperKey"), ("IEEE8023-LAG-MIB", "dot3adAggPartnerSystemID"), ("IEEE8023-LAG-MIB", "dot3adAggPartnerSystemPriority"), ("IEEE8023-LAG-MIB", "dot3adAggPartnerOperKey"), ("IEEE8023-LAG-MIB", "dot3adAggCollectorMaxDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggGroup = dot3adAggGroup.setStatus('current')
dot3adAggPortListGroup = ObjectGroup((1, 2, 840, 10006, 300, 43, 2, 1, 2)).setObjects(("IEEE8023-LAG-MIB", "dot3adAggPortListPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggPortListGroup = dot3adAggPortListGroup.setStatus('current')
dot3adAggPortGroup = ObjectGroup((1, 2, 840, 10006, 300, 43, 2, 1, 3)).setObjects(("IEEE8023-LAG-MIB", "dot3adAggPortActorSystemPriority"), ("IEEE8023-LAG-MIB", "dot3adAggPortActorSystemID"), ("IEEE8023-LAG-MIB", "dot3adAggPortActorAdminKey"), ("IEEE8023-LAG-MIB", "dot3adAggPortActorOperKey"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminSystemPriority"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperSystemPriority"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminSystemID"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperSystemID"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminKey"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperKey"), ("IEEE8023-LAG-MIB", "dot3adAggPortSelectedAggID"), ("IEEE8023-LAG-MIB", "dot3adAggPortAttachedAggID"), ("IEEE8023-LAG-MIB", "dot3adAggPortActorPort"), ("IEEE8023-LAG-MIB", "dot3adAggPortActorPortPriority"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminPort"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperPort"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminPortPriority"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperPortPriority"), ("IEEE8023-LAG-MIB", "dot3adAggPortActorAdminState"), ("IEEE8023-LAG-MIB", "dot3adAggPortActorOperState"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminState"), ("IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperState"), ("IEEE8023-LAG-MIB", "dot3adAggPortAggregateOrIndividual"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggPortGroup = dot3adAggPortGroup.setStatus('current')
dot3adAggPortStatsGroup = ObjectGroup((1, 2, 840, 10006, 300, 43, 2, 1, 4)).setObjects(("IEEE8023-LAG-MIB", "dot3adAggPortStatsLACPDUsRx"), ("IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerPDUsRx"), ("IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerResponsePDUsRx"), ("IEEE8023-LAG-MIB", "dot3adAggPortStatsUnknownRx"), ("IEEE8023-LAG-MIB", "dot3adAggPortStatsIllegalRx"), ("IEEE8023-LAG-MIB", "dot3adAggPortStatsLACPDUsTx"), ("IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerPDUsTx"), ("IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerResponsePDUsTx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggPortStatsGroup = dot3adAggPortStatsGroup.setStatus('current')
dot3adAggPortDebugGroup = ObjectGroup((1, 2, 840, 10006, 300, 43, 2, 1, 5)).setObjects(("IEEE8023-LAG-MIB", "dot3adAggPortDebugRxState"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugLastRxTime"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugMuxState"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugMuxReason"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChurnState"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChurnState"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChurnCount"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChurnCount"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorSyncTransitionCount"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerSyncTransitionCount"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChangeCount"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChangeCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggPortDebugGroup = dot3adAggPortDebugGroup.setStatus('current')
dot3adTablesLastChangedGroup = ObjectGroup((1, 2, 840, 10006, 300, 43, 2, 1, 1, 6)).setObjects(("IEEE8023-LAG-MIB", "dot3adTablesLastChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adTablesLastChangedGroup = dot3adTablesLastChangedGroup.setStatus('current')
dot3adAggCompliance = ModuleCompliance((1, 2, 840, 10006, 300, 43, 2, 2, 1)).setObjects(("IEEE8023-LAG-MIB", "dot3adAggGroup"), ("IEEE8023-LAG-MIB", "dot3adAggPortGroup"), ("IEEE8023-LAG-MIB", "dot3adTablesLastChangedGroup"), ("IEEE8023-LAG-MIB", "dot3adAggPortListGroup"), ("IEEE8023-LAG-MIB", "dot3adAggPortStatsGroup"), ("IEEE8023-LAG-MIB", "dot3adAggPortDebugGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3adAggCompliance = dot3adAggCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8023-LAG-MIB", dot3adAggPortDebugEntry=dot3adAggPortDebugEntry, dot3adAggPortPartnerOperKey=dot3adAggPortPartnerOperKey, dot3adAgg=dot3adAgg, dot3adAggPortAggregateOrIndividual=dot3adAggPortAggregateOrIndividual, dot3adAggPortDebugMuxReason=dot3adAggPortDebugMuxReason, LacpState=LacpState, dot3adAggPartnerSystemID=dot3adAggPartnerSystemID, ChurnState=ChurnState, dot3adAggMACAddress=dot3adAggMACAddress, dot3adAggPortDebugRxState=dot3adAggPortDebugRxState, dot3adAggPartnerOperKey=dot3adAggPartnerOperKey, dot3adAggPortGroup=dot3adAggPortGroup, dot3adAggActorSystemID=dot3adAggActorSystemID, dot3adAggPortActorSystemPriority=dot3adAggPortActorSystemPriority, dot3adAggPortPartnerOperSystemPriority=dot3adAggPortPartnerOperSystemPriority, dot3adAggPortStatsUnknownRx=dot3adAggPortStatsUnknownRx, dot3adAggCollectorMaxDelay=dot3adAggCollectorMaxDelay, dot3adAggPortDebugPartnerChurnState=dot3adAggPortDebugPartnerChurnState, dot3adAggPortPartnerAdminPort=dot3adAggPortPartnerAdminPort, dot3adAggPortDebugActorSyncTransitionCount=dot3adAggPortDebugActorSyncTransitionCount, dot3adAggActorAdminKey=dot3adAggActorAdminKey, dot3adAggCompliance=dot3adAggCompliance, dot3adAggPortStatsMarkerPDUsTx=dot3adAggPortStatsMarkerPDUsTx, dot3adAggGroups=dot3adAggGroups, dot3adAggPortActorAdminState=dot3adAggPortActorAdminState, lagMIBObjects=lagMIBObjects, dot3adAggPortPartnerOperPortPriority=dot3adAggPortPartnerOperPortPriority, dot3adAggPortDebugGroup=dot3adAggPortDebugGroup, dot3adAggPortStatsLACPDUsTx=dot3adAggPortStatsLACPDUsTx, dot3adAggPortPartnerAdminSystemPriority=dot3adAggPortPartnerAdminSystemPriority, dot3adAggPortListPorts=dot3adAggPortListPorts, dot3adAggPortActorSystemID=dot3adAggPortActorSystemID, dot3adAggPortDebugPartnerSyncTransitionCount=dot3adAggPortDebugPartnerSyncTransitionCount, dot3adAggPortPartnerAdminState=dot3adAggPortPartnerAdminState, dot3adAggPort=dot3adAggPort, dot3adAggEntry=dot3adAggEntry, dot3adAggPortActorPortPriority=dot3adAggPortActorPortPriority, dot3adAggPortDebugMuxState=dot3adAggPortDebugMuxState, dot3adAggPortListTable=dot3adAggPortListTable, LacpKey=LacpKey, dot3adAggPortPartnerAdminKey=dot3adAggPortPartnerAdminKey, dot3adAggPartnerSystemPriority=dot3adAggPartnerSystemPriority, dot3adAggPortActorOperKey=dot3adAggPortActorOperKey, dot3adAggIndex=dot3adAggIndex, dot3adAggPortStatsEntry=dot3adAggPortStatsEntry, dot3adAggPortPartnerAdminSystemID=dot3adAggPortPartnerAdminSystemID, dot3adAggGroup=dot3adAggGroup, dot3adAggPortDebugLastRxTime=dot3adAggPortDebugLastRxTime, dot3adAggPortStatsLACPDUsRx=dot3adAggPortStatsLACPDUsRx, dot3adAggAggregateOrIndividual=dot3adAggAggregateOrIndividual, dot3adAggPortStatsTable=dot3adAggPortStatsTable, dot3adAggActorOperKey=dot3adAggActorOperKey, dot3adAggActorSystemPriority=dot3adAggActorSystemPriority, dot3adAggPortPartnerAdminPortPriority=dot3adAggPortPartnerAdminPortPriority, dot3adAggPortPartnerOperSystemID=dot3adAggPortPartnerOperSystemID, dot3adAggPortActorPort=dot3adAggPortActorPort, dot3adAggPortDebugPartnerChurnCount=dot3adAggPortDebugPartnerChurnCount, dot3adAggPortAttachedAggID=dot3adAggPortAttachedAggID, dot3adAggPortIndex=dot3adAggPortIndex, lagMIB=lagMIB, dot3adAggPortDebugActorChurnCount=dot3adAggPortDebugActorChurnCount, dot3adAggPortEntry=dot3adAggPortEntry, dot3adTablesLastChanged=dot3adTablesLastChanged, dot3adAggCompliances=dot3adAggCompliances, dot3adAggTable=dot3adAggTable, dot3adAggPortStatsIllegalRx=dot3adAggPortStatsIllegalRx, dot3adAggPortDebugPartnerChangeCount=dot3adAggPortDebugPartnerChangeCount, dot3adAggPortDebugActorChangeCount=dot3adAggPortDebugActorChangeCount, dot3adAggPortListEntry=dot3adAggPortListEntry, dot3adAggPortDebugTable=dot3adAggPortDebugTable, dot3adAggPortStatsGroup=dot3adAggPortStatsGroup, dot3adAggPortStatsMarkerPDUsRx=dot3adAggPortStatsMarkerPDUsRx, dot3adAggPortPartnerOperPort=dot3adAggPortPartnerOperPort, dot3adAggPortSelectedAggID=dot3adAggPortSelectedAggID, dot3adAggPortStatsMarkerResponsePDUsRx=dot3adAggPortStatsMarkerResponsePDUsRx, dot3adAggPortStatsMarkerResponsePDUsTx=dot3adAggPortStatsMarkerResponsePDUsTx, dot3adAggPortTable=dot3adAggPortTable, dot3adAggPortActorAdminKey=dot3adAggPortActorAdminKey, dot3adTablesLastChangedGroup=dot3adTablesLastChangedGroup, dot3adAggPortActorOperState=dot3adAggPortActorOperState, dot3adAggConformance=dot3adAggConformance, PYSNMP_MODULE_ID=lagMIB, dot3adAggPortListGroup=dot3adAggPortListGroup, dot3adAggPortDebugActorChurnState=dot3adAggPortDebugActorChurnState, dot3adAggPortPartnerOperState=dot3adAggPortPartnerOperState)
