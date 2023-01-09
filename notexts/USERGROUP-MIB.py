#
# PySNMP MIB module USERGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/usrgrp.mib
# Produced by pysmi-1.1.8 at Mon Jan  9 10:31:06 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
hmConfiguration, = mibBuilder.importSymbols("HMPRIV-MGMT-SNMP-MIB", "hmConfiguration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, Integer32, Bits, IpAddress, NotificationType, TextualConvention, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Gauge32, Unsigned32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Integer32", "Bits", "IpAddress", "NotificationType", "TextualConvention", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Gauge32", "Unsigned32", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmUserGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 14, 3))
hmUserGroup.setRevisions(('2007-09-13 12:00',))
if mibBuilder.loadTexts: hmUserGroup.setLastUpdated('200709131200Z')
if mibBuilder.loadTexts: hmUserGroup.setOrganization('Hirschmann Automation and Control GmbH')
class MemberID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

hmUserGroupTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 1), )
if mibBuilder.loadTexts: hmUserGroupTable.setStatus('current')
hmUserGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmUserGroupID"))
if mibBuilder.loadTexts: hmUserGroupEntry.setStatus('current')
hmUserGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmUserGroupID.setStatus('current')
hmUserGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupDescription.setStatus('current')
hmUserGroupRestricted = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupRestricted.setStatus('current')
hmUserGroupSecAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("trapOnly", 2), ("portDisable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupSecAction.setStatus('current')
hmUserGroupMemberTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 2), )
if mibBuilder.loadTexts: hmUserGroupMemberTable.setStatus('current')
hmUserGroupMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 2, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmUserGroupMemberGroupID"), (0, "USERGROUP-MIB", "hmUserGroupMemberUserID"))
if mibBuilder.loadTexts: hmUserGroupMemberEntry.setStatus('current')
hmUserGroupMemberGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmUserGroupMemberGroupID.setStatus('current')
hmUserGroupMemberUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 2, 1, 2), MemberID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmUserGroupMemberUserID.setStatus('current')
hmUserTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 3), )
if mibBuilder.loadTexts: hmUserTable.setStatus('current')
hmUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 3, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmUserID"))
if mibBuilder.loadTexts: hmUserEntry.setStatus('current')
hmUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 3, 1, 1), MemberID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmUserID.setStatus('current')
hmUserRestricted = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserRestricted.setStatus('current')
hmPortSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 4), )
if mibBuilder.loadTexts: hmPortSecurityTable.setStatus('current')
hmPortSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmPortSecSlotID"), (0, "USERGROUP-MIB", "hmPortSecPortID"))
if mibBuilder.loadTexts: hmPortSecurityEntry.setStatus('current')
hmPortSecSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecSlotID.setStatus('current')
hmPortSecPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecPortID.setStatus('current')
hmPortSecPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("user", 1), ("group", 2), ("known", 3), ("world", 4), ("uplink", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecPermission.setStatus('current')
hmPortSecAllowedUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 4), MemberID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAllowedUserID.setStatus('current')
hmPortSecAllowedGroupIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(128, 128)).setFixedLength(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAllowedGroupIDs.setStatus('current')
hmPortSecConnectedUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 6), MemberID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecConnectedUserID.setStatus('current')
hmPortSecAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("trapOnly", 2), ("portDisable", 3), ("autoDisable", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAction.setStatus('current')
hmPortSecAutoReconfigure = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAutoReconfigure.setStatus('current')
hmPortSecPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledWithWrongAddr", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecPortStatus.setStatus('current')
hmPortSecAllowedUserIPID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecAllowedUserIPID.setStatus('current')
hmPortSecDynamicLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecDynamicLimit.setStatus('current')
hmPortSecDynamicCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 4, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecDynamicCount.setStatus('current')
hmUserGroupSecurityAction = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("trapOnly", 2), ("portDisable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupSecurityAction.setStatus('current')
hmUserGroupPortSecurityMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("macAddressBased", 1), ("ipAddressBased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmUserGroupPortSecurityMode.setStatus('current')
hmPortSecExtendedGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 3, 10))
hmPortSecExtendedTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1), )
if mibBuilder.loadTexts: hmPortSecExtendedTable.setStatus('current')
hmPortSecExtendedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmPortSecExtSlotID"), (0, "USERGROUP-MIB", "hmPortSecExtPortID"))
if mibBuilder.loadTexts: hmPortSecExtendedEntry.setStatus('current')
hmPortSecExtSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: hmPortSecExtSlotID.setStatus('current')
hmPortSecExtPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: hmPortSecExtPortID.setStatus('current')
hmPortSecExtAction = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("trapOnly", 2), ("portDisable", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecExtAction.setStatus('current')
hmPortSecExtPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledWithWrongAddr", 3))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmPortSecExtPortStatus.setStatus('current')
hmPortSecMultipleAdressesTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2), )
if mibBuilder.loadTexts: hmPortSecMultipleAdressesTable.setStatus('current')
hmPortSecMultipleAdressesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1), ).setIndexNames((0, "USERGROUP-MIB", "hmPortSecMASlotID"), (0, "USERGROUP-MIB", "hmPortSecMAPortID"), (0, "USERGROUP-MIB", "hmPortSecMAExtendedIndex"))
if mibBuilder.loadTexts: hmPortSecMultipleAdressesEntry.setStatus('current')
hmPortSecMASlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: hmPortSecMASlotID.setStatus('current')
hmPortSecMAPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: hmPortSecMAPortID.setStatus('current')
hmPortSecMAExtendedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)))
if mibBuilder.loadTexts: hmPortSecMAExtendedIndex.setStatus('current')
hmPortSecMAAllowedUserIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 4), MemberID()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIDs.setStatus('current')
hmPortSecMAAllowedUserIPIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIPIDs.setStatus('current')
hmPortSecMAAllowedUserIDMask = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 3, 10, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 48)).clone(48)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmPortSecMAAllowedUserIDMask.setStatus('current')
hmUserGroupEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 14, 3, 0))
if mibBuilder.loadTexts: hmUserGroupEvent.setStatus('current')
hmNewUserTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 3, 0, 1)).setObjects(("USERGROUP-MIB", "hmPortSecConnectedUserID"))
if mibBuilder.loadTexts: hmNewUserTrap.setStatus('current')
hmPortSecurityTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 3, 0, 2)).setObjects(("USERGROUP-MIB", "hmPortSecPermission"), ("USERGROUP-MIB", "hmPortSecAction"), ("USERGROUP-MIB", "hmPortSecConnectedUserID"), ("USERGROUP-MIB", "hmPortSecAllowedUserID"), ("USERGROUP-MIB", "hmPortSecAllowedUserIPID"), ("USERGROUP-MIB", "hmPortSecAllowedGroupIDs"))
if mibBuilder.loadTexts: hmPortSecurityTrap.setStatus('current')
hmPortSecConfigErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 3, 0, 3)).setObjects(("USERGROUP-MIB", "hmPortSecConnectedUserID"))
if mibBuilder.loadTexts: hmPortSecConfigErrorTrap.setStatus('current')
mibBuilder.exportSymbols("USERGROUP-MIB", hmPortSecDynamicCount=hmPortSecDynamicCount, hmUserGroupMemberTable=hmUserGroupMemberTable, hmUserGroupPortSecurityMode=hmUserGroupPortSecurityMode, hmUserGroupMemberEntry=hmUserGroupMemberEntry, hmPortSecExtendedGroup=hmPortSecExtendedGroup, MemberID=MemberID, hmPortSecConfigErrorTrap=hmPortSecConfigErrorTrap, hmPortSecAllowedUserIPID=hmPortSecAllowedUserIPID, hmUserGroupDescription=hmUserGroupDescription, hmPortSecPortID=hmPortSecPortID, hmUserGroupSecurityAction=hmUserGroupSecurityAction, PYSNMP_MODULE_ID=hmUserGroup, hmUserEntry=hmUserEntry, hmPortSecSlotID=hmPortSecSlotID, hmPortSecMASlotID=hmPortSecMASlotID, hmPortSecMAExtendedIndex=hmPortSecMAExtendedIndex, hmPortSecMAAllowedUserIPIDs=hmPortSecMAAllowedUserIPIDs, hmPortSecConnectedUserID=hmPortSecConnectedUserID, hmPortSecMAPortID=hmPortSecMAPortID, hmPortSecPortStatus=hmPortSecPortStatus, hmUserID=hmUserID, hmUserRestricted=hmUserRestricted, hmUserTable=hmUserTable, hmPortSecAction=hmPortSecAction, hmPortSecMAAllowedUserIDs=hmPortSecMAAllowedUserIDs, hmUserGroupEvent=hmUserGroupEvent, hmPortSecMAAllowedUserIDMask=hmPortSecMAAllowedUserIDMask, hmUserGroupEntry=hmUserGroupEntry, hmPortSecPermission=hmPortSecPermission, hmUserGroupRestricted=hmUserGroupRestricted, hmPortSecurityTrap=hmPortSecurityTrap, hmPortSecAllowedGroupIDs=hmPortSecAllowedGroupIDs, hmPortSecDynamicLimit=hmPortSecDynamicLimit, hmUserGroup=hmUserGroup, hmUserGroupTable=hmUserGroupTable, hmPortSecExtSlotID=hmPortSecExtSlotID, hmPortSecurityTable=hmPortSecurityTable, hmPortSecMultipleAdressesEntry=hmPortSecMultipleAdressesEntry, hmNewUserTrap=hmNewUserTrap, hmPortSecAllowedUserID=hmPortSecAllowedUserID, hmPortSecurityEntry=hmPortSecurityEntry, hmPortSecAutoReconfigure=hmPortSecAutoReconfigure, hmUserGroupID=hmUserGroupID, hmUserGroupSecAction=hmUserGroupSecAction, hmPortSecExtPortStatus=hmPortSecExtPortStatus, hmUserGroupMemberGroupID=hmUserGroupMemberGroupID, hmPortSecExtendedEntry=hmPortSecExtendedEntry, hmPortSecExtPortID=hmPortSecExtPortID, hmPortSecExtAction=hmPortSecExtAction, hmPortSecExtendedTable=hmPortSecExtendedTable, hmUserGroupMemberUserID=hmUserGroupMemberUserID, hmPortSecMultipleAdressesTable=hmPortSecMultipleAdressesTable)
