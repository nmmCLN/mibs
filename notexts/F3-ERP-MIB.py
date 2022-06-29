#
# PySNMP MIB module F3-ERP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-ERP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:50 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
VlanId, VlanEthertype, SecondaryState, OperationalState, VlanPriority, AdminState = mibBuilder.importSymbols("CM-COMMON-MIB", "VlanId", "VlanEthertype", "SecondaryState", "OperationalState", "VlanPriority", "AdminState")
neIndex, = mibBuilder.importSymbols("CM-ENTITY-MIB", "neIndex")
CmProtUnitType, CmProtUnitState = mibBuilder.importSymbols("CM-PROTECTION-MIB", "CmProtUnitType", "CmProtUnitState")
Dot1agCfmMDLevel, = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmMDLevel")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Gauge32, Counter32, IpAddress, iso, ModuleIdentity, ObjectIdentity, Unsigned32, MibIdentifier, Bits, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Gauge32", "Counter32", "IpAddress", "iso", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Bits", "TimeTicks", "Integer32")
TruthValue, RowStatus, MacAddress, StorageType, TextualConvention, VariablePointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "MacAddress", "StorageType", "TextualConvention", "VariablePointer", "DisplayString")
f3ErpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25))
f3ErpMIB.setRevisions(('2012-09-13 00:00',))
if mibBuilder.loadTexts: f3ErpMIB.setLastUpdated('201209130000Z')
if mibBuilder.loadTexts: f3ErpMIB.setOrganization('ADVA Optical Networking')
class G8032Version(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("v1", 1), ("v2", 2))

class RPLRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("neighbor", 2), ("owner", 3))

class RingPortStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unblocked", 1), ("unblockedSF", 2), ("unblockedSD", 3), ("blockedRPL", 4), ("blockedSF", 5), ("blockedSD", 6), ("blockedMS", 7), ("blockedFS", 8), ("blockedPending", 9), ("subringInterConnect", 10), ("subringInterConnectSF", 11))

class RingNodeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("protection", 2), ("manual", 3), ("forced", 4), ("pending", 5))

class RAPSRequest(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noRequest", 1), ("manual", 2), ("forced", 3), ("signailFail", 4), ("signailDegrade", 5), ("notApplicable", 6))

class ERPGroupAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAction", 1), ("forcedSwitch", 2), ("manualSwitch", 3), ("clearSwitch", 4), ("resetStats", 5))

class RapsInterconnectionNode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("primary", 2), ("secondary", 3))

class RapsMultipleFailure(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("primary", 2), ("secondary", 3))

f3ErpConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1))
f3ErpStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2))
f3ErpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3))
f3ErpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1), )
if mibBuilder.loadTexts: f3ErpGroupTable.setStatus('current')
f3ErpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-ERP-MIB", "f3ErpGroupIndex"))
if mibBuilder.loadTexts: f3ErpGroupEntry.setStatus('current')
f3ErpGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: f3ErpGroupIndex.setStatus('current')
f3ErpGroupAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 2), AdminState()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupAdminState.setStatus('current')
f3ErpGroupOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 3), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupOperationalState.setStatus('current')
f3ErpGroupSecondaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 4), SecondaryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupSecondaryState.setStatus('current')
f3ErpGroupRapsRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRapsRingId.setStatus('current')
f3ErpGroupRapsNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 6), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRapsNodeId.setStatus('current')
f3ErpGroupRapsVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 7), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRapsVlanId.setStatus('current')
f3ErpGroupRapsVlanPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 8), VlanPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRapsVlanPrio.setStatus('current')
f3ErpGroupRapsVlanEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRapsVlanEtherType.setStatus('current')
f3ErpGroupRapsMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 10), Dot1agCfmMDLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRapsMdLevel.setStatus('current')
f3ErpGroupCompatibleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 11), G8032Version()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3ErpGroupCompatibleVersion.setStatus('current')
f3ErpGroupRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRevertive.setStatus('current')
f3ErpGroupSubRingWithoutVirtChan = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 13), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupSubRingWithoutVirtChan.setStatus('current')
f3ErpGroupGuardTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupGuardTime.setStatus('current')
f3ErpGroupWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupWaitToRestore.setStatus('current')
f3ErpGroupHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupHoldOffTime.setStatus('current')
f3ErpGroupRingPort0 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 17), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRingPort0.setStatus('current')
f3ErpGroupRingPort0MEP = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 18), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRingPort0MEP.setStatus('current')
f3ErpGroupRingPort0Role = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 19), RPLRole()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRingPort0Role.setStatus('current')
f3ErpGroupRingPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 20), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRingPort1.setStatus('current')
f3ErpGroupRingPort1MEP = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 21), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRingPort1MEP.setStatus('current')
f3ErpGroupRingPort1Role = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 22), RPLRole()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRingPort1Role.setStatus('current')
f3ErpGroupProtectMgmtTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 23), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupProtectMgmtTunnel.setStatus('current')
f3ErpGroupNodeState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 24), RingNodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupNodeState.setStatus('current')
f3ErpGroupWTRRemainingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupWTRRemainingTime.setStatus('current')
f3ErpGroupTxRapsRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 26), RAPSRequest()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupTxRapsRequest.setStatus('current')
f3ErpGroupTxRapsRplBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 27), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupTxRapsRplBlocked.setStatus('current')
f3ErpGroupTxRapsDNF = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 28), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupTxRapsDNF.setStatus('current')
f3ErpGroupTxRapsBPR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupTxRapsBPR.setStatus('current')
f3ErpGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 30), ERPGroupAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3ErpGroupAction.setStatus('current')
f3ErpGroupActionObject = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 31), VariablePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3ErpGroupActionObject.setStatus('current')
f3ErpGroupUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 32), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupUserLabel.setStatus('current')
f3ErpGroupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 33), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupStorageType.setStatus('current')
f3ErpGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 34), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRowStatus.setStatus('current')
f3ErpGroupInterconnectionErp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 35), VariablePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3ErpGroupInterconnectionErp.setStatus('current')
f3ErpGroupInterconnectPropagateTc = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 36), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3ErpGroupInterconnectPropagateTc.setStatus('current')
f3ErpGroupRapsVirtualChannelMep = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 37), VariablePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3ErpGroupRapsVirtualChannelMep.setStatus('current')
f3ErpGroupMaxFpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 38), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3ErpGroupMaxFpNum.setStatus('current')
f3ErpGroupRapsInterconnectionNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 39), RapsInterconnectionNode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRapsInterconnectionNode.setStatus('current')
f3ErpGroupRapsMultipleFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 40), RapsMultipleFailure()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3ErpGroupRapsMultipleFailure.setStatus('current')
f3ErpGroupProtectedFlowTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 2), )
if mibBuilder.loadTexts: f3ErpGroupProtectedFlowTable.setStatus('current')
f3ErpGroupProtectedFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-ERP-MIB", "f3ErpGroupIndex"), (0, "F3-ERP-MIB", "f3ErpGroupProtectedFlow"))
if mibBuilder.loadTexts: f3ErpGroupProtectedFlowEntry.setStatus('current')
f3ErpGroupProtectedFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 2, 1, 1), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpGroupProtectedFlow.setStatus('current')
f3ErpUnitTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3), )
if mibBuilder.loadTexts: f3ErpUnitTable.setStatus('current')
f3ErpUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-ERP-MIB", "f3ErpGroupIndex"), (0, "F3-ERP-MIB", "f3ErpUnitIndex"))
if mibBuilder.loadTexts: f3ErpUnitEntry.setStatus('current')
f3ErpUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: f3ErpUnitIndex.setStatus('current')
f3ErpUnitPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 2), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPort.setStatus('current')
f3ErpUnitPortMEP = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 3), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortMEP.setStatus('current')
f3ErpUnitPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 4), RPLRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortRole.setStatus('current')
f3ErpUnitPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 5), RingPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortStatus.setStatus('current')
f3ErpUnitPortRxRapsRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 6), RAPSRequest()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortRxRapsRequest.setStatus('current')
f3ErpUnitPortRxRapsRplBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortRxRapsRplBlocked.setStatus('current')
f3ErpUnitPortRxRapsDNF = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortRxRapsDNF.setStatus('current')
f3ErpUnitPortRxRapsBPR = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortRxRapsBPR.setStatus('current')
f3ErpUnitPortRxRapsNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortRxRapsNodeId.setStatus('current')
f3ErpUnitPortRapsFp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 11), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitPortRapsFp.setStatus('current')
f3ErpUnitStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1), )
if mibBuilder.loadTexts: f3ErpUnitStatsTable.setStatus('current')
f3ErpUnitStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "F3-ERP-MIB", "f3ErpGroupIndex"), (0, "F3-ERP-MIB", "f3ErpUnitIndex"))
if mibBuilder.loadTexts: f3ErpUnitStatsEntry.setStatus('current')
f3ErpUnitNumBlockedStateTrans = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitNumBlockedStateTrans.setStatus('current')
f3ErpUnitRapsPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsPDUsTx.setStatus('current')
f3ErpUnitRapsPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsPDUsRx.setStatus('current')
f3ErpUnitRapsPDUsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsPDUsDiscarded.setStatus('current')
f3ErpUnitRapsNoReqPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsNoReqPDUsTx.setStatus('current')
f3ErpUnitRapsNoReqRBPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsNoReqRBPDUsTx.setStatus('current')
f3ErpUnitRapsSignalFailPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsSignalFailPDUsTx.setStatus('current')
f3ErpUnitRapsManualSwitchPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsManualSwitchPDUsTx.setStatus('current')
f3ErpUnitRapsForcedSwitchPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsForcedSwitchPDUsTx.setStatus('current')
f3ErpUnitRapsEventPDUsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsEventPDUsTx.setStatus('current')
f3ErpUnitRapsNoReqPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsNoReqPDUsRx.setStatus('current')
f3ErpUnitRapsNoReqRBPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsNoReqRBPDUsRx.setStatus('current')
f3ErpUnitRapsSignalFailPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsSignalFailPDUsRx.setStatus('current')
f3ErpUnitRapsManualSwitchPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsManualSwitchPDUsRx.setStatus('current')
f3ErpUnitRapsForcedSwitchPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsForcedSwitchPDUsRx.setStatus('current')
f3ErpUnitRapsEventPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsEventPDUsRx.setStatus('current')
f3ErpUnitRapsInvalidOamVersionPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsInvalidOamVersionPDUsRx.setStatus('current')
f3ErpUnitRapsRsvdRequestPDUsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsRsvdRequestPDUsRx.setStatus('current')
f3ErpUnitRapsRsvdEventSubcode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ErpUnitRapsRsvdEventSubcode.setStatus('current')
f3ErpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 1))
f3ErpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 2))
f3ErpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 1, 1)).setObjects(("F3-ERP-MIB", "f3ErpGroupGroup"), ("F3-ERP-MIB", "f3ErpUnitGroup"), ("F3-ERP-MIB", "f3ErpUnitStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ErpCompliance = f3ErpCompliance.setStatus('current')
f3ErpGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 2, 1)).setObjects(("F3-ERP-MIB", "f3ErpGroupAdminState"), ("F3-ERP-MIB", "f3ErpGroupOperationalState"), ("F3-ERP-MIB", "f3ErpGroupSecondaryState"), ("F3-ERP-MIB", "f3ErpGroupRapsRingId"), ("F3-ERP-MIB", "f3ErpGroupRapsNodeId"), ("F3-ERP-MIB", "f3ErpGroupRapsVlanId"), ("F3-ERP-MIB", "f3ErpGroupRapsVlanPrio"), ("F3-ERP-MIB", "f3ErpGroupRapsVlanEtherType"), ("F3-ERP-MIB", "f3ErpGroupRapsMdLevel"), ("F3-ERP-MIB", "f3ErpGroupCompatibleVersion"), ("F3-ERP-MIB", "f3ErpGroupRevertive"), ("F3-ERP-MIB", "f3ErpGroupSubRingWithoutVirtChan"), ("F3-ERP-MIB", "f3ErpGroupGuardTime"), ("F3-ERP-MIB", "f3ErpGroupWaitToRestore"), ("F3-ERP-MIB", "f3ErpGroupHoldOffTime"), ("F3-ERP-MIB", "f3ErpGroupRingPort0"), ("F3-ERP-MIB", "f3ErpGroupRingPort0MEP"), ("F3-ERP-MIB", "f3ErpGroupRingPort0Role"), ("F3-ERP-MIB", "f3ErpGroupRingPort1"), ("F3-ERP-MIB", "f3ErpGroupRingPort1MEP"), ("F3-ERP-MIB", "f3ErpGroupRingPort1Role"), ("F3-ERP-MIB", "f3ErpGroupProtectMgmtTunnel"), ("F3-ERP-MIB", "f3ErpGroupNodeState"), ("F3-ERP-MIB", "f3ErpGroupWTRRemainingTime"), ("F3-ERP-MIB", "f3ErpGroupTxRapsRequest"), ("F3-ERP-MIB", "f3ErpGroupTxRapsRplBlocked"), ("F3-ERP-MIB", "f3ErpGroupTxRapsDNF"), ("F3-ERP-MIB", "f3ErpGroupTxRapsBPR"), ("F3-ERP-MIB", "f3ErpGroupAction"), ("F3-ERP-MIB", "f3ErpGroupActionObject"), ("F3-ERP-MIB", "f3ErpGroupUserLabel"), ("F3-ERP-MIB", "f3ErpGroupStorageType"), ("F3-ERP-MIB", "f3ErpGroupRowStatus"), ("F3-ERP-MIB", "f3ErpGroupProtectedFlow"), ("F3-ERP-MIB", "f3ErpGroupInterconnectionErp"), ("F3-ERP-MIB", "f3ErpGroupInterconnectPropagateTc"), ("F3-ERP-MIB", "f3ErpGroupRapsVirtualChannelMep"), ("F3-ERP-MIB", "f3ErpGroupMaxFpNum"), ("F3-ERP-MIB", "f3ErpGroupRapsInterconnectionNode"), ("F3-ERP-MIB", "f3ErpGroupRapsMultipleFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ErpGroupGroup = f3ErpGroupGroup.setStatus('current')
f3ErpUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 2, 2)).setObjects(("F3-ERP-MIB", "f3ErpUnitPort"), ("F3-ERP-MIB", "f3ErpUnitPortMEP"), ("F3-ERP-MIB", "f3ErpUnitPortRole"), ("F3-ERP-MIB", "f3ErpUnitPortStatus"), ("F3-ERP-MIB", "f3ErpUnitPortRxRapsRequest"), ("F3-ERP-MIB", "f3ErpUnitPortRxRapsRplBlocked"), ("F3-ERP-MIB", "f3ErpUnitPortRxRapsDNF"), ("F3-ERP-MIB", "f3ErpUnitPortRxRapsBPR"), ("F3-ERP-MIB", "f3ErpUnitPortRxRapsNodeId"), ("F3-ERP-MIB", "f3ErpUnitPortRapsFp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ErpUnitGroup = f3ErpUnitGroup.setStatus('current')
f3ErpUnitStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 2, 3)).setObjects(("F3-ERP-MIB", "f3ErpUnitNumBlockedStateTrans"), ("F3-ERP-MIB", "f3ErpUnitRapsPDUsTx"), ("F3-ERP-MIB", "f3ErpUnitRapsPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsPDUsDiscarded"), ("F3-ERP-MIB", "f3ErpUnitRapsNoReqPDUsTx"), ("F3-ERP-MIB", "f3ErpUnitRapsNoReqRBPDUsTx"), ("F3-ERP-MIB", "f3ErpUnitRapsSignalFailPDUsTx"), ("F3-ERP-MIB", "f3ErpUnitRapsManualSwitchPDUsTx"), ("F3-ERP-MIB", "f3ErpUnitRapsForcedSwitchPDUsTx"), ("F3-ERP-MIB", "f3ErpUnitRapsEventPDUsTx"), ("F3-ERP-MIB", "f3ErpUnitRapsNoReqPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsNoReqRBPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsSignalFailPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsManualSwitchPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsForcedSwitchPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsEventPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsInvalidOamVersionPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsRsvdRequestPDUsRx"), ("F3-ERP-MIB", "f3ErpUnitRapsRsvdEventSubcode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ErpUnitStatsGroup = f3ErpUnitStatsGroup.setStatus('current')
mibBuilder.exportSymbols("F3-ERP-MIB", RapsMultipleFailure=RapsMultipleFailure, f3ErpGroupProtectedFlow=f3ErpGroupProtectedFlow, f3ErpGroupTxRapsRplBlocked=f3ErpGroupTxRapsRplBlocked, f3ErpGroupSubRingWithoutVirtChan=f3ErpGroupSubRingWithoutVirtChan, f3ErpGroupWaitToRestore=f3ErpGroupWaitToRestore, G8032Version=G8032Version, f3ErpUnitRapsNoReqPDUsTx=f3ErpUnitRapsNoReqPDUsTx, f3ErpGroupProtectedFlowEntry=f3ErpGroupProtectedFlowEntry, f3ErpUnitRapsManualSwitchPDUsRx=f3ErpUnitRapsManualSwitchPDUsRx, f3ErpGroupRingPort1=f3ErpGroupRingPort1, PYSNMP_MODULE_ID=f3ErpMIB, f3ErpUnitRapsRsvdEventSubcode=f3ErpUnitRapsRsvdEventSubcode, f3ErpGroups=f3ErpGroups, f3ErpStatsObjects=f3ErpStatsObjects, f3ErpUnitPortRxRapsNodeId=f3ErpUnitPortRxRapsNodeId, f3ErpGroupHoldOffTime=f3ErpGroupHoldOffTime, f3ErpGroupRapsMultipleFailure=f3ErpGroupRapsMultipleFailure, f3ErpUnitPort=f3ErpUnitPort, f3ErpGroupRapsVlanId=f3ErpGroupRapsVlanId, f3ErpGroupRevertive=f3ErpGroupRevertive, f3ErpUnitPortMEP=f3ErpUnitPortMEP, f3ErpGroupAdminState=f3ErpGroupAdminState, f3ErpUnitRapsPDUsTx=f3ErpUnitRapsPDUsTx, f3ErpGroupRowStatus=f3ErpGroupRowStatus, f3ErpGroupInterconnectPropagateTc=f3ErpGroupInterconnectPropagateTc, RingPortStatus=RingPortStatus, f3ErpUnitRapsForcedSwitchPDUsRx=f3ErpUnitRapsForcedSwitchPDUsRx, f3ErpUnitRapsNoReqRBPDUsRx=f3ErpUnitRapsNoReqRBPDUsRx, f3ErpGroupRapsVlanEtherType=f3ErpGroupRapsVlanEtherType, f3ErpGroupAction=f3ErpGroupAction, f3ErpGroupRingPort1Role=f3ErpGroupRingPort1Role, f3ErpUnitRapsRsvdRequestPDUsRx=f3ErpUnitRapsRsvdRequestPDUsRx, f3ErpGroupSecondaryState=f3ErpGroupSecondaryState, f3ErpGroupInterconnectionErp=f3ErpGroupInterconnectionErp, f3ErpGroupTxRapsBPR=f3ErpGroupTxRapsBPR, f3ErpUnitRapsEventPDUsTx=f3ErpUnitRapsEventPDUsTx, f3ErpUnitRapsForcedSwitchPDUsTx=f3ErpUnitRapsForcedSwitchPDUsTx, f3ErpUnitIndex=f3ErpUnitIndex, f3ErpUnitStatsEntry=f3ErpUnitStatsEntry, f3ErpGroupIndex=f3ErpGroupIndex, f3ErpUnitNumBlockedStateTrans=f3ErpUnitNumBlockedStateTrans, f3ErpGroupRapsNodeId=f3ErpGroupRapsNodeId, f3ErpCompliance=f3ErpCompliance, f3ErpGroupRingPort1MEP=f3ErpGroupRingPort1MEP, RPLRole=RPLRole, RingNodeState=RingNodeState, RapsInterconnectionNode=RapsInterconnectionNode, f3ErpGroupRingPort0MEP=f3ErpGroupRingPort0MEP, f3ErpGroupMaxFpNum=f3ErpGroupMaxFpNum, RAPSRequest=RAPSRequest, f3ErpGroupGroup=f3ErpGroupGroup, f3ErpUnitPortRole=f3ErpUnitPortRole, f3ErpGroupCompatibleVersion=f3ErpGroupCompatibleVersion, f3ErpUnitGroup=f3ErpUnitGroup, f3ErpGroupNodeState=f3ErpGroupNodeState, f3ErpUnitRapsSignalFailPDUsTx=f3ErpUnitRapsSignalFailPDUsTx, f3ErpUnitRapsPDUsRx=f3ErpUnitRapsPDUsRx, f3ErpUnitPortRxRapsBPR=f3ErpUnitPortRxRapsBPR, ERPGroupAction=ERPGroupAction, f3ErpConformance=f3ErpConformance, f3ErpGroupActionObject=f3ErpGroupActionObject, f3ErpGroupTable=f3ErpGroupTable, f3ErpUnitRapsInvalidOamVersionPDUsRx=f3ErpUnitRapsInvalidOamVersionPDUsRx, f3ErpGroupRapsVirtualChannelMep=f3ErpGroupRapsVirtualChannelMep, f3ErpUnitPortRxRapsDNF=f3ErpUnitPortRxRapsDNF, f3ErpUnitRapsPDUsDiscarded=f3ErpUnitRapsPDUsDiscarded, f3ErpGroupEntry=f3ErpGroupEntry, f3ErpUnitRapsEventPDUsRx=f3ErpUnitRapsEventPDUsRx, f3ErpGroupRingPort0Role=f3ErpGroupRingPort0Role, f3ErpUnitEntry=f3ErpUnitEntry, f3ErpGroupTxRapsRequest=f3ErpGroupTxRapsRequest, f3ErpGroupProtectMgmtTunnel=f3ErpGroupProtectMgmtTunnel, f3ErpGroupRapsInterconnectionNode=f3ErpGroupRapsInterconnectionNode, f3ErpUnitRapsManualSwitchPDUsTx=f3ErpUnitRapsManualSwitchPDUsTx, f3ErpUnitRapsNoReqRBPDUsTx=f3ErpUnitRapsNoReqRBPDUsTx, f3ErpGroupUserLabel=f3ErpGroupUserLabel, f3ErpUnitPortRxRapsRequest=f3ErpUnitPortRxRapsRequest, f3ErpGroupGuardTime=f3ErpGroupGuardTime, f3ErpUnitTable=f3ErpUnitTable, f3ErpUnitPortRapsFp=f3ErpUnitPortRapsFp, f3ErpGroupStorageType=f3ErpGroupStorageType, f3ErpCompliances=f3ErpCompliances, f3ErpMIB=f3ErpMIB, f3ErpUnitStatsTable=f3ErpUnitStatsTable, f3ErpUnitStatsGroup=f3ErpUnitStatsGroup, f3ErpGroupRapsMdLevel=f3ErpGroupRapsMdLevel, f3ErpUnitPortStatus=f3ErpUnitPortStatus, f3ErpUnitRapsSignalFailPDUsRx=f3ErpUnitRapsSignalFailPDUsRx, f3ErpGroupOperationalState=f3ErpGroupOperationalState, f3ErpUnitPortRxRapsRplBlocked=f3ErpUnitPortRxRapsRplBlocked, f3ErpGroupRingPort0=f3ErpGroupRingPort0, f3ErpGroupWTRRemainingTime=f3ErpGroupWTRRemainingTime, f3ErpGroupProtectedFlowTable=f3ErpGroupProtectedFlowTable, f3ErpUnitRapsNoReqPDUsRx=f3ErpUnitRapsNoReqPDUsRx, f3ErpGroupTxRapsDNF=f3ErpGroupTxRapsDNF, f3ErpGroupRapsRingId=f3ErpGroupRapsRingId, f3ErpGroupRapsVlanPrio=f3ErpGroupRapsVlanPrio, f3ErpConfigObjects=f3ErpConfigObjects)
