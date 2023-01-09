#
# PySNMP MIB module CM-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-PROTECTION-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:41 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
neIndex, slotIndex, shelfIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "neIndex", "slotIndex", "shelfIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, Counter64, Gauge32, IpAddress, MibIdentifier, ObjectIdentity, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Counter64", "Gauge32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Unsigned32", "NotificationType")
DisplayString, StorageType, TruthValue, MacAddress, VariablePointer, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TruthValue", "MacAddress", "VariablePointer", "TextualConvention", "RowStatus")
cmProtectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7))
cmProtectionMIB.setRevisions(('2010-06-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmProtectionMIB.setRevisionsDescriptions(('Notes from release 201006230000Z,\n             (1)Added universalring as CmProtSwitchMode for R4.4CC. \n\n            Notes from release 200803030000Z,\n             (1)MIB version ready for release FSP150CM 3.1.',))
if mibBuilder.loadTexts: cmProtectionMIB.setLastUpdated('201006230000Z')
if mibBuilder.loadTexts: cmProtectionMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: cmProtectionMIB.setContactInfo('        Raghav Trivedi\n                     ADVA Optical Networking, Inc.\n                Tel: +1 972 759-1239\n             E-mail: rtrivedi@advaoptical.com\n             Postal: 2301 N. Greenville Ave. #300\n                     Richardson, TX USA 75082')
if mibBuilder.loadTexts: cmProtectionMIB.setDescription('This module defines the Protection MIB definitions used by \n             the F3 (FSP150CM/CC) product lines.  \n             Copyright (C) ADVA Optical Networking.')
cmProtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1))
cmProtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 2))
cmProtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3))
class CmProtSwitchMode(TextualConvention, Integer32):
    description = 'Enumerations for Protection Switch Mode.\n             oneplusone   - 1+1, this is the NPCUP mode,\n             dualactiverx - In this mode, traffic is bridged in A2N\n                            direction (same as 1+1), however\n                            both network ports receive customer traffic in\n                            N2A direction. In this mode, both network\n                            ports are working, i.e. there is no\n                            protection.\n             universalring - In this mode, traffic is bridged in A2N\n                             direction (same as 1+1), both\n                             network ports receive customer traffic in\n                             N2A direction.  In this mode, both network\n                             ports are working, i.e. no protection.\n                             The main difference w.r.t dualactiverx is that\n                             traffic in N2A direction, which does not match\n                             the service definition is steered to the other\n                             network port, i.e. non-service matching traffic\n                             from N1 goes to N2 and vice versa.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("oneplusone", 1), ("dualactiverx", 2), ("universalring", 3))

class CmProtSwitchDirection(TextualConvention, Integer32):
    description = 'Enumerations for Protection Switch Direction.\n             unidirectional - Unidirectional Protection Switching,\n             bidirectional  - Bidirectional Protection Switching.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unidirectional", 1), ("bidirectional", 2))

class CmProtSwitchAction(TextualConvention, Integer32):
    description = 'Enumerations for User initiated Protection Switch Action.\n             manualfromworking  - Manual Switch from Working,\n             forcedfromworking  - Forced Switch from Working,\n             manualfromprotect  - Manual Switch from Protect,\n             forcedfromprotect  - Forced Switch from Protect,\n             lockoutfromprotect - Lockout from Protect'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("releaseprotswitch", 2), ("manualfromworking", 3), ("forcedfromworking", 4), ("manualfromprotect", 5), ("forcedfromprotect", 6), ("lockoutfromprotect", 7))

class CmProtUnitType(TextualConvention, Integer32):
    description = 'Enumerations for Protection Unit Type.\n             working - Working Protection Unit,\n             protect - Protect Protection Unit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("working", 1), ("protect", 2))

class CmProtUnitState(TextualConvention, Integer32):
    description = 'Enumerations for Protection Unit State.\n             active  - Active Protection Unit,\n             standby - Standby Protection Unit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("standby", 2))

class CmProtGroupStatus(TextualConvention, Integer32):
    description = 'Enumerations for Protection Status.\n             nooutstandingreq - No oustanding request,\n             sf-protect       - Signal failure on protect,\n             sf-working       - Signal failure on working,\n             sd-protect       - Signal degrade on protect,\n             sd-working       - Signal degrade on working,\n             manual-protect   - Manual on protect \n             manual-working   - Manual on working \n             forced-working   - Forced on working \n             forced-protect   - Forced on protect \n             lockout-protect  - Lockout on protect \n             waitToRestore    - Wait to restore'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("nooutstandingreq", 1), ("sf-protect", 2), ("sf-working", 3), ("sd-protect", 4), ("sd-working", 5), ("manual-protect", 6), ("manual-working", 7), ("forced-protect", 8), ("forced-working", 9), ("lockout-protect", 10), ("waitToRestore", 11))

cmFacProtGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1), )
if mibBuilder.loadTexts: cmFacProtGroupTable.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupTable.setDescription('A list of entries corresponding to the Facility Protection Groups.\n             Entries can be created/deleted in this table by management\n             application action.')
cmFacProtGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-PROTECTION-MIB", "cmFacProtGroupIndex"))
if mibBuilder.loadTexts: cmFacProtGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupEntry.setDescription('An entry containing information applicable to a particular\n             Protection Group.')
cmFacProtGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupIndex.setDescription('Unique index value associated with the Facility Protection Group.')
cmFacProtGroupUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupUserLabel.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupUserLabel.setDescription('User Label associated with the Facility Protection Group.')
cmFacProtGroupSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 3), CmProtSwitchMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupSwitchMode.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupSwitchMode.setDescription("Facility Protection Group's Protection Switch Mode.")
cmFacProtGroupRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupRevertive.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupRevertive.setDescription("Whether the Facility Protection is revertive or not.\n          This object is not applicable for cmFacProtGroupSwitchMode 'dualactiverx'.")
cmFacProtGroupWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 60), ValueRangeConstraint(0, 0), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupWaitToRestore.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupWaitToRestore.setDescription("Time in minutes to wait before reverting to Working facility\n          in case of cmFacProtGroupRevertive set to revertive.\n          This object is not applicable for cmFacProtGroupSwitchMode 'dualactiverx'.")
cmFacProtGroupDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 6), CmProtSwitchDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupDirection.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupDirection.setDescription("Supported Protection Group Switch direction.\n          This object is not applicable for cmFacProtGroupSwitchMode 'dualactiverx'.")
cmFacProtGroupWorkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 7), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupWorkPort.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupWorkPort.setDescription('Facility Protection Group exists between 2 facilities (ports). \n          This object represents the WORKING facility Port.')
cmFacProtGroupProtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 8), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupProtPort.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupProtPort.setDescription('This object\n          represents the PROTECT facility Network Element Port when\n          cmFacProtGroupSwitchMode is oneplusone.  In the case of\n          dualactiverx, this represents the second active port.')
cmFacProtGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 9), CmProtGroupStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtGroupStatus.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupStatus.setDescription('This object represents the PROTECTION group status.')
cmFacProtGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 10), CmProtSwitchAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmFacProtGroupAction.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupAction.setDescription('User initiated protection switch action.')
cmFacProtGroupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 11), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupStorageType.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupStorageType.setDescription('The type of storage configured for this entry.')
cmFacProtGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupRowStatus.setDescription('The status of this row.  An entry MUST NOT exist in the \n            active state unless all objects in the entry have an \n            appropriate value, as described\n            in the description clause for each writable object.\n\n            The values of cmFacProtGroupRowStatus supported are\n            createAndGo(4) and destroy(6).  All mandatory attributes\n            must be specified in a single SNMP SET request with\n            cmFacProtGroupRowStatus value as createAndGo(4).\n            Upon successful row creation, this object has a\n            value of active(1).\n\n            The cmFacProtGroupRowStatus object may be modified if\n            the associated instance of this object is equal to active(1).')
cmFacProtGroupMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtGroupMacAddress.setStatus('current')
if mibBuilder.loadTexts: cmFacProtGroupMacAddress.setDescription('This object allows retrieval of the Mac Address of the PROTECTION group.')
cmFacProtUnitTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2), )
if mibBuilder.loadTexts: cmFacProtUnitTable.setStatus('current')
if mibBuilder.loadTexts: cmFacProtUnitTable.setDescription('A list of entries corresponding to the Facility Protection \n             Units.')
cmFacProtUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-PROTECTION-MIB", "cmFacProtGroupIndex"), (0, "CM-PROTECTION-MIB", "cmFacProtUnitIndex"))
if mibBuilder.loadTexts: cmFacProtUnitEntry.setStatus('current')
if mibBuilder.loadTexts: cmFacProtUnitEntry.setDescription('An entry containing information applicable to a particular\n             Protection Unit.')
cmFacProtUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtUnitIndex.setStatus('current')
if mibBuilder.loadTexts: cmFacProtUnitIndex.setDescription('Unique index value associated with the Facility Protection Unit.')
cmFacProtUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 2), CmProtUnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtUnitType.setStatus('current')
if mibBuilder.loadTexts: cmFacProtUnitType.setDescription("Facility Protection Unit's Type, i.e. whether working or protect.")
cmFacProtUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 3), CmProtUnitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtUnitState.setStatus('current')
if mibBuilder.loadTexts: cmFacProtUnitState.setDescription("Facility Protection Unit's State, i.e. whether active or standby.")
cmFacProtUnitPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 4), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtUnitPort.setStatus('current')
if mibBuilder.loadTexts: cmFacProtUnitPort.setDescription("Facility Protection Unit's points to a facility (port). \n          This object represents the facility Network Element port.")
cmMSPGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3), )
if mibBuilder.loadTexts: cmMSPGroupTable.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupTable.setDescription('A list of entries corresponding to the Multiplex Section Protection Groups.\n             Entries can be created/deleted in this table by management\n             application action.')
cmMSPGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-PROTECTION-MIB", "cmMSPGroupIndex"))
if mibBuilder.loadTexts: cmMSPGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupEntry.setDescription('An entry containing information applicable to a particular\n             Protection Group.')
cmMSPGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupIndex.setDescription('Unique index value associated with the Multiplex Section Protection Group.')
cmMSPGroupUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupUserLabel.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupUserLabel.setDescription('User Label associated with the Multiplex Section Protection Group.')
cmMSPGroupSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 3), CmProtSwitchMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupSwitchMode.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupSwitchMode.setDescription("Multiplex Section Protection Group's Protection Switch Mode.")
cmMSPGroupRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupRevertive.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupRevertive.setDescription("Whether the Multiplex Section Protection is revertive or not.\n          This object is not applicable for cmMSPGroupSwitchMode 'dualactiverx'.")
cmMSPGroupWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 60), ValueRangeConstraint(0, 0), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupWaitToRestore.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupWaitToRestore.setDescription("Time in minutes to wait before reverting to Working facility\n          in case of cmMSPGroupRevertive set to revertive.\n          This object is not applicable for cmMSPGroupSwitchMode 'dualactiverx'.")
cmMSPGroupB2DEGTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupB2DEGTrigger.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupB2DEGTrigger.setDescription('B2DEG is trigger of MSP or not.')
cmMSPGroupDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 7), CmProtSwitchDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupDirection.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupDirection.setDescription("Supported Protection Group Switch direction.\n          This object is not applicable for cmMSPGroupSwitchMode 'dualactiverx'.")
cmMSPGroupWorkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 8), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupWorkPort.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupWorkPort.setDescription('Multiplex Section Protection Group exists between 2 facilities (ports). \n          This object represents the WORKING facility Port.')
cmMSPGroupProtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 9), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupProtPort.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupProtPort.setDescription('This object\n          represents the PROTECT facility Network Element Port when\n          cmMSPGroupSwitchMode is oneplusone.  In the case of\n          dualactiverx, this represents the second active port.')
cmMSPGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 10), CmProtGroupStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPGroupStatus.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupStatus.setDescription('This object represents the PROTECTION group status.')
cmMSPGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 11), CmProtSwitchAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmMSPGroupAction.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupAction.setDescription('User initiated protection switch action.')
cmMSPGroupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 12), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupStorageType.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupStorageType.setDescription('The type of storage configured for this entry.')
cmMSPGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupRowStatus.setDescription('The status of this row.  An entry MUST NOT exist in the \n            active state unless all objects in the entry have an \n            appropriate value, as described\n            in the description clause for each writable object.\n\n            The values of cmMSPGroupRowStatus supported are\n            createAndGo(4) and destroy(6).  All mandatory attributes\n            must be specified in a single SNMP SET request with\n            cmMSPGroupRowStatus value as createAndGo(4).\n            Upon successful row creation, this object has a\n            value of active(1).\n\n            The cmMSPGroupRowStatus object may be modified if\n            the associated instance of this object is equal to active(1).')
cmMSPGroupMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 14), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPGroupMacAddress.setStatus('current')
if mibBuilder.loadTexts: cmMSPGroupMacAddress.setDescription('This object allows retrieval of the Mac Address of the PROTECTION group.')
cmMSPUnitTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4), )
if mibBuilder.loadTexts: cmMSPUnitTable.setStatus('current')
if mibBuilder.loadTexts: cmMSPUnitTable.setDescription('A list of entries corresponding to the Multiplex Section Protection \n             Units.')
cmMSPUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-PROTECTION-MIB", "cmMSPGroupIndex"), (0, "CM-PROTECTION-MIB", "cmMSPUnitIndex"))
if mibBuilder.loadTexts: cmMSPUnitEntry.setStatus('current')
if mibBuilder.loadTexts: cmMSPUnitEntry.setDescription('An entry containing information applicable to a particular\n             Protection Unit.')
cmMSPUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPUnitIndex.setStatus('current')
if mibBuilder.loadTexts: cmMSPUnitIndex.setDescription('Unique index value associated with the Multiplex Section Protection Unit.')
cmMSPUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 2), CmProtUnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPUnitType.setStatus('current')
if mibBuilder.loadTexts: cmMSPUnitType.setDescription("Multiplex Section Protection Unit's Type, i.e. whether working or protect.")
cmMSPUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 3), CmProtUnitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPUnitState.setStatus('current')
if mibBuilder.loadTexts: cmMSPUnitState.setDescription("Multiplex Section Protection Unit's State, i.e. whether active or standby.")
cmMSPUnitPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 4), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPUnitPort.setStatus('current')
if mibBuilder.loadTexts: cmMSPUnitPort.setDescription("Facility Protection Unit's points to a facility (port). \n          This object represents the facility Network Element port.")
cmProtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 1))
cmProtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2))
cmProtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 1, 1)).setObjects(("CM-PROTECTION-MIB", "cmProtObjectGroup"), ("CM-PROTECTION-MIB", "cmMSProtObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmProtCompliance = cmProtCompliance.setStatus('current')
if mibBuilder.loadTexts: cmProtCompliance.setDescription('Describes the requirements for conformance to the CM Prot\n             group.')
cmProtObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2, 1)).setObjects(("CM-PROTECTION-MIB", "cmFacProtGroupIndex"), ("CM-PROTECTION-MIB", "cmFacProtGroupUserLabel"), ("CM-PROTECTION-MIB", "cmFacProtGroupSwitchMode"), ("CM-PROTECTION-MIB", "cmFacProtGroupRevertive"), ("CM-PROTECTION-MIB", "cmFacProtGroupWaitToRestore"), ("CM-PROTECTION-MIB", "cmFacProtGroupDirection"), ("CM-PROTECTION-MIB", "cmFacProtGroupWorkPort"), ("CM-PROTECTION-MIB", "cmFacProtGroupProtPort"), ("CM-PROTECTION-MIB", "cmFacProtGroupStatus"), ("CM-PROTECTION-MIB", "cmFacProtGroupAction"), ("CM-PROTECTION-MIB", "cmFacProtGroupStorageType"), ("CM-PROTECTION-MIB", "cmFacProtGroupRowStatus"), ("CM-PROTECTION-MIB", "cmFacProtGroupMacAddress"), ("CM-PROTECTION-MIB", "cmFacProtUnitIndex"), ("CM-PROTECTION-MIB", "cmFacProtUnitType"), ("CM-PROTECTION-MIB", "cmFacProtUnitState"), ("CM-PROTECTION-MIB", "cmFacProtUnitPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmProtObjectGroup = cmProtObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cmProtObjectGroup.setDescription('A collection of objects used to manage the Protection Object group.')
cmMSProtObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2, 2)).setObjects(("CM-PROTECTION-MIB", "cmMSPGroupIndex"), ("CM-PROTECTION-MIB", "cmMSPGroupUserLabel"), ("CM-PROTECTION-MIB", "cmMSPGroupSwitchMode"), ("CM-PROTECTION-MIB", "cmMSPGroupRevertive"), ("CM-PROTECTION-MIB", "cmMSPGroupWaitToRestore"), ("CM-PROTECTION-MIB", "cmMSPGroupB2DEGTrigger"), ("CM-PROTECTION-MIB", "cmMSPGroupDirection"), ("CM-PROTECTION-MIB", "cmMSPGroupWorkPort"), ("CM-PROTECTION-MIB", "cmMSPGroupProtPort"), ("CM-PROTECTION-MIB", "cmMSPGroupStatus"), ("CM-PROTECTION-MIB", "cmMSPGroupAction"), ("CM-PROTECTION-MIB", "cmMSPGroupStorageType"), ("CM-PROTECTION-MIB", "cmMSPGroupRowStatus"), ("CM-PROTECTION-MIB", "cmMSPGroupMacAddress"), ("CM-PROTECTION-MIB", "cmMSPUnitIndex"), ("CM-PROTECTION-MIB", "cmMSPUnitType"), ("CM-PROTECTION-MIB", "cmMSPUnitState"), ("CM-PROTECTION-MIB", "cmMSPUnitPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmMSProtObjectGroup = cmMSProtObjectGroup.setStatus('current')
if mibBuilder.loadTexts: cmMSProtObjectGroup.setDescription('A collection of objects used to manage the Multiplex \n              Section Protection Object group.')
mibBuilder.exportSymbols("CM-PROTECTION-MIB", cmFacProtGroupRowStatus=cmFacProtGroupRowStatus, cmFacProtUnitTable=cmFacProtUnitTable, cmFacProtUnitType=cmFacProtUnitType, cmFacProtGroupSwitchMode=cmFacProtGroupSwitchMode, cmMSPGroupWorkPort=cmMSPGroupWorkPort, PYSNMP_MODULE_ID=cmProtectionMIB, cmFacProtGroupWorkPort=cmFacProtGroupWorkPort, cmMSPGroupStatus=cmMSPGroupStatus, cmMSPGroupRowStatus=cmMSPGroupRowStatus, cmFacProtGroupTable=cmFacProtGroupTable, CmProtSwitchMode=CmProtSwitchMode, cmFacProtGroupAction=cmFacProtGroupAction, cmFacProtUnitIndex=cmFacProtUnitIndex, cmMSPGroupRevertive=cmMSPGroupRevertive, cmMSPGroupAction=cmMSPGroupAction, cmFacProtGroupStorageType=cmFacProtGroupStorageType, cmFacProtUnitEntry=cmFacProtUnitEntry, cmFacProtGroupUserLabel=cmFacProtGroupUserLabel, CmProtSwitchAction=CmProtSwitchAction, CmProtUnitType=CmProtUnitType, cmFacProtGroupProtPort=cmFacProtGroupProtPort, cmMSPGroupSwitchMode=cmMSPGroupSwitchMode, cmProtGroups=cmProtGroups, cmFacProtGroupStatus=cmFacProtGroupStatus, CmProtGroupStatus=CmProtGroupStatus, cmMSPGroupB2DEGTrigger=cmMSPGroupB2DEGTrigger, cmMSPGroupMacAddress=cmMSPGroupMacAddress, CmProtSwitchDirection=CmProtSwitchDirection, CmProtUnitState=CmProtUnitState, cmMSPUnitType=cmMSPUnitType, cmMSPUnitPort=cmMSPUnitPort, cmProtNotifications=cmProtNotifications, cmMSPGroupTable=cmMSPGroupTable, cmMSPGroupIndex=cmMSPGroupIndex, cmMSPGroupDirection=cmMSPGroupDirection, cmProtCompliances=cmProtCompliances, cmFacProtUnitState=cmFacProtUnitState, cmFacProtUnitPort=cmFacProtUnitPort, cmFacProtGroupDirection=cmFacProtGroupDirection, cmProtConformance=cmProtConformance, cmFacProtGroupEntry=cmFacProtGroupEntry, cmMSPUnitIndex=cmMSPUnitIndex, cmMSPUnitEntry=cmMSPUnitEntry, cmMSPGroupWaitToRestore=cmMSPGroupWaitToRestore, cmProtectionMIB=cmProtectionMIB, cmMSPUnitTable=cmMSPUnitTable, cmMSPGroupStorageType=cmMSPGroupStorageType, cmFacProtGroupWaitToRestore=cmFacProtGroupWaitToRestore, cmFacProtGroupIndex=cmFacProtGroupIndex, cmMSPUnitState=cmMSPUnitState, cmMSPGroupProtPort=cmMSPGroupProtPort, cmProtObjects=cmProtObjects, cmMSPGroupEntry=cmMSPGroupEntry, cmProtCompliance=cmProtCompliance, cmProtObjectGroup=cmProtObjectGroup, cmFacProtGroupRevertive=cmFacProtGroupRevertive, cmFacProtGroupMacAddress=cmFacProtGroupMacAddress, cmMSPGroupUserLabel=cmMSPGroupUserLabel, cmMSProtObjectGroup=cmMSProtObjectGroup)
