#
# PySNMP MIB module CM-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-REDUNDANCY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:07:40 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
CardType, neIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "CardType", "neIndex")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Integer32, iso, Counter32, Bits, Counter64, Gauge32, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Integer32", "iso", "Counter32", "Bits", "Counter64", "Gauge32", "Unsigned32", "TimeTicks")
VariablePointer, TruthValue, StorageType, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "VariablePointer", "TruthValue", "StorageType", "DisplayString", "TextualConvention", "RowStatus")
cmRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15))
cmRedundancyMIB.setRevisions(('2009-02-24 00:00',))
if mibBuilder.loadTexts: cmRedundancyMIB.setLastUpdated('200902240000Z')
if mibBuilder.loadTexts: cmRedundancyMIB.setOrganization('ADVA Optical Networking')
cmRedundancyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1))
cmRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 2))
cmRedundancyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3))
class CmRedundancyArch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("loadbalance", 1), ("activestandby", 2))

class CmRedundancyStandbyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cold", 1), ("warm", 2), ("hot", 3))

class CmRedundancyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class CmRedundancySyncStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("out-of-synchronize", 2), ("bulk-synchronize", 3), ("incremental-synchronize", 4))

class CmRedundancySwitchOverReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("latestUpdatedData", 2), ("userTrigger", 3), ("cardReset", 4), ("cardRemoval", 5), ("softwareFailure", 6), ("hardwareFailure", 7))

class CmRedundancySyncMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("automatically", 1), ("manually", 2))

class CmRedundancyAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("force", 1), ("manual", 2), ("releaseforce", 3))

class CmRedundancyUnitState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("normal", 2), ("maintenance", 3), ("faultisolation", 4), ("lock", 5), ("extracted", 6), ("init", 7), ("stanbdby", 8))

cmRedundancyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1), )
if mibBuilder.loadTexts: cmRedundancyGroupTable.setStatus('current')
cmRedundancyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-REDUNDANCY-MIB", "cmRedundancyGroupIndex"))
if mibBuilder.loadTexts: cmRedundancyGroupEntry.setStatus('current')
cmRedundancyGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupIndex.setStatus('current')
cmRedundancyGroupUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmRedundancyGroupUserLabel.setStatus('current')
cmRedundancyGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 3), CardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupType.setStatus('current')
cmRedundancyGroupSyncEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmRedundancyGroupSyncEnabled.setStatus('current')
cmRedundancyGroupActiveCard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 5), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupActiveCard.setStatus('current')
cmRedundancyGroupActiveCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 6), CmRedundancyUnitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupActiveCardState.setStatus('current')
cmRedundancyGroupStandbyCard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 7), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupStandbyCard.setStatus('current')
cmRedundancyGroupStandbyCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 8), CmRedundancyUnitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupStandbyCardState.setStatus('current')
cmRedundancyGroupLastSwitchOverTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupLastSwitchOverTime.setStatus('current')
cmRedundancyGroupLastSwitchOverReason = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 10), CmRedundancySwitchOverReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupLastSwitchOverReason.setStatus('current')
cmRedundancyGroupState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 11), CmRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupState.setStatus('current')
cmRedundancyGroupSyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 12), CmRedundancySyncStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmRedundancyGroupSyncStatus.setStatus('current')
cmRedundancyGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 13), CmRedundancyAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmRedundancyGroupAction.setStatus('current')
cmRedundancyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 1))
cmRedundancyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 2))
cmRedundancyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 1, 1)).setObjects(("CM-REDUNDANCY-MIB", "cmRedundancyObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmRedundancyCompliance = cmRedundancyCompliance.setStatus('current')
cmRedundancyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 2, 1)).setObjects(("CM-REDUNDANCY-MIB", "cmRedundancyGroupIndex"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupUserLabel"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupType"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupSyncEnabled"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupActiveCard"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupActiveCardState"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupStandbyCard"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupStandbyCardState"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupLastSwitchOverTime"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupLastSwitchOverReason"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupState"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupSyncStatus"), ("CM-REDUNDANCY-MIB", "cmRedundancyGroupAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmRedundancyObjectGroup = cmRedundancyObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CM-REDUNDANCY-MIB", cmRedundancyGroups=cmRedundancyGroups, cmRedundancyGroupLastSwitchOverTime=cmRedundancyGroupLastSwitchOverTime, cmRedundancyCompliances=cmRedundancyCompliances, CmRedundancySyncStatus=CmRedundancySyncStatus, cmRedundancyGroupLastSwitchOverReason=cmRedundancyGroupLastSwitchOverReason, cmRedundancyGroupActiveCardState=cmRedundancyGroupActiveCardState, CmRedundancyArch=CmRedundancyArch, cmRedundancyNotifications=cmRedundancyNotifications, cmRedundancyGroupState=cmRedundancyGroupState, cmRedundancyGroupAction=cmRedundancyGroupAction, cmRedundancyGroupActiveCard=cmRedundancyGroupActiveCard, cmRedundancyGroupStandbyCardState=cmRedundancyGroupStandbyCardState, cmRedundancyGroupStandbyCard=cmRedundancyGroupStandbyCard, cmRedundancyGroupType=cmRedundancyGroupType, cmRedundancyGroupUserLabel=cmRedundancyGroupUserLabel, cmRedundancyGroupIndex=cmRedundancyGroupIndex, CmRedundancySyncMode=CmRedundancySyncMode, cmRedundancyMIB=cmRedundancyMIB, cmRedundancyObjectGroup=cmRedundancyObjectGroup, CmRedundancyStandbyMode=CmRedundancyStandbyMode, cmRedundancyCompliance=cmRedundancyCompliance, cmRedundancyGroupSyncEnabled=cmRedundancyGroupSyncEnabled, CmRedundancyAction=CmRedundancyAction, cmRedundancyGroupEntry=cmRedundancyGroupEntry, cmRedundancyConformance=cmRedundancyConformance, CmRedundancySwitchOverReason=CmRedundancySwitchOverReason, PYSNMP_MODULE_ID=cmRedundancyMIB, CmRedundancyState=CmRedundancyState, CmRedundancyUnitState=CmRedundancyUnitState, cmRedundancyGroupSyncStatus=cmRedundancyGroupSyncStatus, cmRedundancyObjects=cmRedundancyObjects, cmRedundancyGroupTable=cmRedundancyGroupTable)
