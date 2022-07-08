#
# PySNMP MIB module F3-EOMPLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-EOMPLS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:23 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
AdminState, CmPmBinAction, CmPmIntervalType, OperationalState, VlanPriority, SecondaryState, VlanId, PerfCounter64 = mibBuilder.importSymbols("CM-COMMON-MIB", "AdminState", "CmPmBinAction", "CmPmIntervalType", "OperationalState", "VlanPriority", "SecondaryState", "VlanId", "PerfCounter64")
neIndex, = mibBuilder.importSymbols("CM-ENTITY-MIB", "neIndex")
cmFlowEntry, cmEthernetNetPortEntry, cmPrioMapV2PrioMappingCOSEntry = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmFlowEntry", "cmEthernetNetPortEntry", "cmPrioMapV2PrioMappingCOSEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Integer32, Gauge32, Counter64, TimeTicks, ObjectIdentity, IpAddress, Bits, Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Gauge32", "Counter64", "TimeTicks", "ObjectIdentity", "IpAddress", "Bits", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32")
TextualConvention, MacAddress, StorageType, DisplayString, VariablePointer, DateAndTime, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "StorageType", "DisplayString", "VariablePointer", "DateAndTime", "TruthValue", "RowStatus")
f3EoMplsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39))
f3EoMplsMIB.setRevisions(('2015-08-14 00:00',))
if mibBuilder.loadTexts: f3EoMplsMIB.setLastUpdated('201508140000Z')
if mibBuilder.loadTexts: f3EoMplsMIB.setOrganization('ADVA Optical Networking')
class EoMplsMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("raw", 1), ("tagged", 2))

class EoMplsDiscoveryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

f3EoMplsConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1))
f3EoMplsPerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2))
f3EoMplsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 3))
f3EoMplsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4))
f3EoMplsPwTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1), )
if mibBuilder.loadTexts: f3EoMplsPwTable.setStatus('current')
f3EoMplsPwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwIndex"))
if mibBuilder.loadTexts: f3EoMplsPwEntry.setStatus('current')
f3EoMplsPwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: f3EoMplsPwIndex.setStatus('current')
f3EoMplsPwMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 2), EoMplsMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwMode.setStatus('current')
f3EoMplsPwTxTunnelLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwTxTunnelLabel.setStatus('current')
f3EoMplsPwTxTunnelExp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwTxTunnelExp.setStatus('current')
f3EoMplsPwTxTunnelTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwTxTunnelTtl.setStatus('current')
f3EoMplsPwTxVcLabelControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwTxVcLabelControl.setStatus('current')
f3EoMplsPwTxVcLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwTxVcLabel.setStatus('current')
f3EoMplsPwTxVcExp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwTxVcExp.setStatus('current')
f3EoMplsPwTxVcTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwTxVcTtl.setStatus('current')
f3EoMplsPwRxTunnelLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwRxTunnelLabel.setStatus('current')
f3EoMplsPwRxTunnelExp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwRxTunnelExp.setStatus('current')
f3EoMplsPwRxTunnelTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwRxTunnelTtl.setStatus('current')
f3EoMplsPwRxVcLabelControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwRxVcLabelControl.setStatus('current')
f3EoMplsPwRxVcLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(16, 1048575))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwRxVcLabel.setStatus('current')
f3EoMplsPwRxVcExp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwRxVcExp.setStatus('current')
f3EoMplsPwRxVcTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwRxVcTtl.setStatus('current')
f3EoMplsPwOuterStagControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwOuterStagControl.setStatus('current')
f3EoMplsPwOuterStagVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 18), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwOuterStagVlanId.setStatus('current')
f3EoMplsPwOuterStagVlanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 19), VlanPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwOuterStagVlanPri.setStatus('current')
f3EoMplsPwDiscoverType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 20), EoMplsDiscoveryType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwDiscoverType.setStatus('current')
f3EoMplsPwDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwDestIp.setStatus('current')
f3EoMplsPwDestMac = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 22), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwDestMac.setStatus('current')
f3EoMplsPwAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 23), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwAdminState.setStatus('current')
f3EoMplsPwOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 24), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwOperationalState.setStatus('current')
f3EoMplsPwSecondaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 25), SecondaryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwSecondaryState.setStatus('current')
f3EoMplsPwStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 26), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3EoMplsPwStorageType.setStatus('current')
f3EoMplsPwRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3EoMplsPwRowStatus.setStatus('current')
f3EoMplsPwInnerExpMappingControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 28), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwInnerExpMappingControl.setStatus('current')
f3EoMplsPwOuterExpMappingControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 29), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwOuterExpMappingControl.setStatus('current')
f3EoMplsPwOuterTagPriMappingControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 30), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwOuterTagPriMappingControl.setStatus('current')
f3EoMplsPwEgressInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 31), VariablePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwEgressInterface.setStatus('current')
f3NetPortExtEoMplsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 2), )
if mibBuilder.loadTexts: f3NetPortExtEoMplsTable.setStatus('current')
f3NetPortExtEoMplsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 2, 1), )
cmEthernetNetPortEntry.registerAugmentions(("F3-EOMPLS-MIB", "f3NetPortExtEoMplsEntry"))
f3NetPortExtEoMplsEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3NetPortExtEoMplsEntry.setStatus('current')
f3NetPortExtEoMplsSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortExtEoMplsSrcIp.setStatus('current')
f3PrioMapV2PrioMappingCosExtEoMplsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 3), )
if mibBuilder.loadTexts: f3PrioMapV2PrioMappingCosExtEoMplsTable.setStatus('current')
f3PrioMapV2PrioMappingCosExtEoMplsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 3, 1), )
cmPrioMapV2PrioMappingCOSEntry.registerAugmentions(("F3-EOMPLS-MIB", "f3PrioMapV2PrioMappingCosExtEoMplsEntry"))
f3PrioMapV2PrioMappingCosExtEoMplsEntry.setIndexNames(*cmPrioMapV2PrioMappingCOSEntry.getIndexNames())
if mibBuilder.loadTexts: f3PrioMapV2PrioMappingCosExtEoMplsEntry.setStatus('current')
f3PrioMapV2PrioMappingCosOuterMplsExp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 3, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PrioMapV2PrioMappingCosOuterMplsExp.setStatus('current')
f3PrioMapV2PrioMappingCosInnerMplsExp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PrioMapV2PrioMappingCosInnerMplsExp.setStatus('current')
f3EoMplsPwStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1), )
if mibBuilder.loadTexts: f3EoMplsPwStatsTable.setStatus('current')
f3EoMplsPwStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwStatsIndex"))
if mibBuilder.loadTexts: f3EoMplsPwStatsEntry.setStatus('current')
f3EoMplsPwStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwStatsIndex.setStatus('current')
f3EoMplsPwStatsIntervalType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 2), CmPmIntervalType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwStatsIntervalType.setStatus('current')
f3EoMplsPwStatsValid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwStatsValid.setStatus('current')
f3EoMplsPwStatsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 4), CmPmBinAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwStatsAction.setStatus('current')
f3EoMplsPwStatsTtlEqual0Drop = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 5), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwStatsTtlEqual0Drop.setStatus('current')
f3EoMplsPwHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2), )
if mibBuilder.loadTexts: f3EoMplsPwHistoryTable.setStatus('current')
f3EoMplsPwHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwStatsIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwHistoryIndex"))
if mibBuilder.loadTexts: f3EoMplsPwHistoryEntry.setStatus('current')
f3EoMplsPwHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwHistoryIndex.setStatus('current')
f3EoMplsPwHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwHistoryTime.setStatus('current')
f3EoMplsPwHistoryValid = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwHistoryValid.setStatus('current')
f3EoMplsPwHistoryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 4), CmPmBinAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwHistoryAction.setStatus('current')
f3EoMplsPwHistoryTtlEqual0Drop = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 5), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwHistoryTtlEqual0Drop.setStatus('current')
f3EoMplsPwThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3), )
if mibBuilder.loadTexts: f3EoMplsPwThresholdTable.setStatus('current')
f3EoMplsPwThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwStatsIndex"), (0, "F3-EOMPLS-MIB", "f3EoMplsPwThresholdIndex"))
if mibBuilder.loadTexts: f3EoMplsPwThresholdEntry.setStatus('current')
f3EoMplsPwThresholdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwThresholdIndex.setStatus('current')
f3EoMplsPwThresholdInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 2), CmPmIntervalType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwThresholdInterval.setStatus('current')
f3EoMplsPwThresholdVariable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 3), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwThresholdVariable.setStatus('current')
f3EoMplsPwThresholdValueLo = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwThresholdValueLo.setStatus('current')
f3EoMplsPwThresholdValueHi = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EoMplsPwThresholdValueHi.setStatus('current')
f3EoMplsPwThresholdMonValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EoMplsPwThresholdMonValue.setStatus('current')
f3EoMplsPwThresholdCrossingAlert = NotificationType((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 3, 1)).setObjects(("F3-EOMPLS-MIB", "f3EoMplsPwThresholdIndex"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdInterval"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdVariable"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdValueLo"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdValueHi"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdMonValue"))
if mibBuilder.loadTexts: f3EoMplsPwThresholdCrossingAlert.setStatus('current')
f3EoMplsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4, 1))
f3EoMplsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4, 2))
f3EoMplsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4, 1, 1)).setObjects(("F3-EOMPLS-MIB", "f3EoMplsConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsCompliance = f3EoMplsCompliance.setStatus('current')
f3EoMplsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4, 2, 1)).setObjects(("F3-EOMPLS-MIB", "f3EoMplsPwIndex"), ("F3-EOMPLS-MIB", "f3EoMplsPwMode"), ("F3-EOMPLS-MIB", "f3EoMplsPwTxTunnelLabel"), ("F3-EOMPLS-MIB", "f3EoMplsPwTxTunnelExp"), ("F3-EOMPLS-MIB", "f3EoMplsPwTxTunnelTtl"), ("F3-EOMPLS-MIB", "f3EoMplsPwTxVcLabelControl"), ("F3-EOMPLS-MIB", "f3EoMplsPwTxVcLabel"), ("F3-EOMPLS-MIB", "f3EoMplsPwTxVcExp"), ("F3-EOMPLS-MIB", "f3EoMplsPwTxVcTtl"), ("F3-EOMPLS-MIB", "f3EoMplsPwRxTunnelLabel"), ("F3-EOMPLS-MIB", "f3EoMplsPwRxTunnelExp"), ("F3-EOMPLS-MIB", "f3EoMplsPwRxTunnelTtl"), ("F3-EOMPLS-MIB", "f3EoMplsPwRxVcLabelControl"), ("F3-EOMPLS-MIB", "f3EoMplsPwRxVcLabel"), ("F3-EOMPLS-MIB", "f3EoMplsPwRxVcExp"), ("F3-EOMPLS-MIB", "f3EoMplsPwRxVcTtl"), ("F3-EOMPLS-MIB", "f3EoMplsPwOuterStagControl"), ("F3-EOMPLS-MIB", "f3EoMplsPwOuterStagVlanId"), ("F3-EOMPLS-MIB", "f3EoMplsPwOuterStagVlanPri"), ("F3-EOMPLS-MIB", "f3EoMplsPwDiscoverType"), ("F3-EOMPLS-MIB", "f3EoMplsPwDestIp"), ("F3-EOMPLS-MIB", "f3EoMplsPwDestMac"), ("F3-EOMPLS-MIB", "f3EoMplsPwAdminState"), ("F3-EOMPLS-MIB", "f3EoMplsPwOperationalState"), ("F3-EOMPLS-MIB", "f3EoMplsPwSecondaryState"), ("F3-EOMPLS-MIB", "f3EoMplsPwStorageType"), ("F3-EOMPLS-MIB", "f3EoMplsPwRowStatus"), ("F3-EOMPLS-MIB", "f3EoMplsPwInnerExpMappingControl"), ("F3-EOMPLS-MIB", "f3EoMplsPwOuterExpMappingControl"), ("F3-EOMPLS-MIB", "f3EoMplsPwOuterTagPriMappingControl"), ("F3-EOMPLS-MIB", "f3EoMplsPwEgressInterface"), ("F3-EOMPLS-MIB", "f3NetPortExtEoMplsSrcIp"), ("F3-EOMPLS-MIB", "f3PrioMapV2PrioMappingCosOuterMplsExp"), ("F3-EOMPLS-MIB", "f3PrioMapV2PrioMappingCosInnerMplsExp"), ("F3-EOMPLS-MIB", "f3EoMplsPwStatsIndex"), ("F3-EOMPLS-MIB", "f3EoMplsPwStatsIntervalType"), ("F3-EOMPLS-MIB", "f3EoMplsPwStatsValid"), ("F3-EOMPLS-MIB", "f3EoMplsPwStatsAction"), ("F3-EOMPLS-MIB", "f3EoMplsPwStatsTtlEqual0Drop"), ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryIndex"), ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryTime"), ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryValid"), ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryAction"), ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryTtlEqual0Drop"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdIndex"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdInterval"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdVariable"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdValueLo"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdValueHi"), ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdMonValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EoMplsConfigGroup = f3EoMplsConfigGroup.setStatus('current')
mibBuilder.exportSymbols("F3-EOMPLS-MIB", f3EoMplsPwEgressInterface=f3EoMplsPwEgressInterface, f3EoMplsPwOuterTagPriMappingControl=f3EoMplsPwOuterTagPriMappingControl, f3EoMplsPwTxTunnelLabel=f3EoMplsPwTxTunnelLabel, f3EoMplsPwRxTunnelLabel=f3EoMplsPwRxTunnelLabel, f3EoMplsPerformance=f3EoMplsPerformance, f3EoMplsPwThresholdVariable=f3EoMplsPwThresholdVariable, f3EoMplsConformance=f3EoMplsConformance, f3EoMplsPwTxVcExp=f3EoMplsPwTxVcExp, f3EoMplsPwStorageType=f3EoMplsPwStorageType, f3EoMplsPwRxTunnelTtl=f3EoMplsPwRxTunnelTtl, f3EoMplsPwThresholdCrossingAlert=f3EoMplsPwThresholdCrossingAlert, f3EoMplsPwIndex=f3EoMplsPwIndex, f3EoMplsPwTxVcLabelControl=f3EoMplsPwTxVcLabelControl, f3EoMplsPwOuterStagVlanId=f3EoMplsPwOuterStagVlanId, f3EoMplsPwDestIp=f3EoMplsPwDestIp, f3EoMplsPwThresholdValueLo=f3EoMplsPwThresholdValueLo, f3EoMplsCompliances=f3EoMplsCompliances, f3EoMplsPwTable=f3EoMplsPwTable, f3EoMplsPwThresholdEntry=f3EoMplsPwThresholdEntry, f3EoMplsPwStatsIntervalType=f3EoMplsPwStatsIntervalType, f3EoMplsPwThresholdIndex=f3EoMplsPwThresholdIndex, PYSNMP_MODULE_ID=f3EoMplsMIB, f3EoMplsPwEntry=f3EoMplsPwEntry, f3EoMplsPwThresholdValueHi=f3EoMplsPwThresholdValueHi, f3EoMplsPwTxVcLabel=f3EoMplsPwTxVcLabel, f3NetPortExtEoMplsSrcIp=f3NetPortExtEoMplsSrcIp, f3PrioMapV2PrioMappingCosExtEoMplsEntry=f3PrioMapV2PrioMappingCosExtEoMplsEntry, f3EoMplsPwRowStatus=f3EoMplsPwRowStatus, f3EoMplsPwThresholdMonValue=f3EoMplsPwThresholdMonValue, f3EoMplsPwOuterStagVlanPri=f3EoMplsPwOuterStagVlanPri, f3EoMplsMIB=f3EoMplsMIB, f3PrioMapV2PrioMappingCosInnerMplsExp=f3PrioMapV2PrioMappingCosInnerMplsExp, f3EoMplsPwStatsAction=f3EoMplsPwStatsAction, f3PrioMapV2PrioMappingCosOuterMplsExp=f3PrioMapV2PrioMappingCosOuterMplsExp, f3EoMplsPwThresholdTable=f3EoMplsPwThresholdTable, f3EoMplsPwRxVcTtl=f3EoMplsPwRxVcTtl, f3EoMplsPwStatsValid=f3EoMplsPwStatsValid, f3EoMplsPwHistoryTtlEqual0Drop=f3EoMplsPwHistoryTtlEqual0Drop, f3EoMplsPwHistoryTable=f3EoMplsPwHistoryTable, f3EoMplsCompliance=f3EoMplsCompliance, f3EoMplsPwDestMac=f3EoMplsPwDestMac, f3EoMplsPwHistoryValid=f3EoMplsPwHistoryValid, f3EoMplsPwStatsIndex=f3EoMplsPwStatsIndex, f3EoMplsPwHistoryTime=f3EoMplsPwHistoryTime, f3EoMplsPwDiscoverType=f3EoMplsPwDiscoverType, f3EoMplsGroups=f3EoMplsGroups, f3PrioMapV2PrioMappingCosExtEoMplsTable=f3PrioMapV2PrioMappingCosExtEoMplsTable, f3EoMplsPwSecondaryState=f3EoMplsPwSecondaryState, f3EoMplsPwAdminState=f3EoMplsPwAdminState, f3EoMplsPwStatsEntry=f3EoMplsPwStatsEntry, f3EoMplsPwTxVcTtl=f3EoMplsPwTxVcTtl, f3EoMplsConfigGroup=f3EoMplsConfigGroup, f3EoMplsPwOuterExpMappingControl=f3EoMplsPwOuterExpMappingControl, f3EoMplsPwRxVcLabel=f3EoMplsPwRxVcLabel, f3EoMplsPwThresholdInterval=f3EoMplsPwThresholdInterval, f3EoMplsPwRxTunnelExp=f3EoMplsPwRxTunnelExp, f3EoMplsPwTxTunnelTtl=f3EoMplsPwTxTunnelTtl, f3EoMplsConfigObjects=f3EoMplsConfigObjects, f3EoMplsPwMode=f3EoMplsPwMode, f3EoMplsPwStatsTtlEqual0Drop=f3EoMplsPwStatsTtlEqual0Drop, f3EoMplsPwHistoryEntry=f3EoMplsPwHistoryEntry, f3EoMplsPwOperationalState=f3EoMplsPwOperationalState, f3EoMplsPwOuterStagControl=f3EoMplsPwOuterStagControl, f3EoMplsPwStatsTable=f3EoMplsPwStatsTable, f3NetPortExtEoMplsEntry=f3NetPortExtEoMplsEntry, EoMplsDiscoveryType=EoMplsDiscoveryType, f3NetPortExtEoMplsTable=f3NetPortExtEoMplsTable, f3EoMplsNotifications=f3EoMplsNotifications, f3EoMplsPwTxTunnelExp=f3EoMplsPwTxTunnelExp, f3EoMplsPwRxVcLabelControl=f3EoMplsPwRxVcLabelControl, f3EoMplsPwRxVcExp=f3EoMplsPwRxVcExp, EoMplsMode=EoMplsMode, f3EoMplsPwHistoryIndex=f3EoMplsPwHistoryIndex, f3EoMplsPwHistoryAction=f3EoMplsPwHistoryAction, f3EoMplsPwInnerExpMappingControl=f3EoMplsPwInnerExpMappingControl)
