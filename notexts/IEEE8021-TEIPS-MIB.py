#
# PySNMP MIB module IEEE8021-TEIPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-TEIPS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:23:45 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ieee8021BridgeBaseComponentId, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId")
IEEE8021BridgePortNumber, IEEE8021PbbTeTSidId, IEEE8021TeipsIpgConfigAdmin, IEEE8021TeipsIpgConfigActiveRequests, ieee802dot1mibs, IEEE8021TeipsIpgid = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumber", "IEEE8021PbbTeTSidId", "IEEE8021TeipsIpgConfigAdmin", "IEEE8021TeipsIpgConfigActiveRequests", "ieee802dot1mibs", "IEEE8021TeipsIpgid")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Integer32, ObjectIdentity, MibIdentifier, NotificationType, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter32, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "NotificationType", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter32", "Unsigned32", "TimeTicks", "Counter64")
DisplayString, StorageType, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention", "TruthValue", "RowStatus")
ieee8021TeipsMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 24))
ieee8021TeipsMib.setRevisions(('2011-08-17 00:00',))
if mibBuilder.loadTexts: ieee8021TeipsMib.setLastUpdated('201108170000Z')
if mibBuilder.loadTexts: ieee8021TeipsMib.setOrganization('IEEE 802.1 Working Group')
ieee8021TeipsNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 0))
ieee8021TeipsObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 1))
ieee8021TeipsConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 2))
ieee8021TeipsIpgTable = MibTable((1, 3, 111, 2, 802, 1, 1, 24, 1, 1), )
if mibBuilder.loadTexts: ieee8021TeipsIpgTable.setStatus('current')
ieee8021TeipsIpgEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"))
if mibBuilder.loadTexts: ieee8021TeipsIpgEntry.setStatus('current')
ieee8021TeipsIpgid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 1), IEEE8021TeipsIpgid())
if mibBuilder.loadTexts: ieee8021TeipsIpgid.setStatus('current')
ieee8021TeipsIpgWorkingMA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgWorkingMA.setStatus('current')
ieee8021TeipsIpgProtectionMA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgProtectionMA.setStatus('current')
ieee8021TeipsIpgWorkingPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 4), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgWorkingPortNumber.setStatus('current')
ieee8021TeipsIpgProtectionPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 5), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgProtectionPortNumber.setStatus('current')
ieee8021TeipsIpgStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgStorageType.setStatus('current')
ieee8021TeipsIpgRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgRowStatus.setStatus('current')
ieee8021TeipsTesiTable = MibTable((1, 3, 111, 2, 802, 1, 1, 24, 1, 2), )
if mibBuilder.loadTexts: ieee8021TeipsTesiTable.setStatus('current')
ieee8021TeipsTesiEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1), ).setIndexNames((0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"), (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiIndex"))
if mibBuilder.loadTexts: ieee8021TeipsTesiEntry.setStatus('current')
ieee8021TeipsTesiIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ieee8021TeipsTesiIndex.setStatus('current')
ieee8021TeipsTesiId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 2), IEEE8021PbbTeTSidId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsTesiId.setStatus('current')
ieee8021TeipsTesiStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsTesiStorageType.setStatus('current')
ieee8021TeipsTesiRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsTesiRowStatus.setStatus('current')
ieee8021TeipsCandidatePsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 24, 1, 3), )
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsTable.setStatus('current')
ieee8021TeipsCandidatePsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1), ).setIndexNames((0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"), (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsIndex"))
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsEntry.setStatus('current')
ieee8021TeipsCandidatePsIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsIndex.setStatus('current')
ieee8021TeipsCandidatePsMA = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsMA.setStatus('current')
ieee8021TeipsCandidatePsPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 3), IEEE8021BridgePortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsPort.setStatus('current')
ieee8021TeipsCandidatePsOper = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsOper.setStatus('current')
ieee8021TeipsCandidatePsStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsStorageType.setStatus('current')
ieee8021TeipsCandidatePsRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsCandidatePsRowStatus.setStatus('current')
ieee8021TeipsIpgConfigTable = MibTable((1, 3, 111, 2, 802, 1, 1, 24, 1, 4), )
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigTable.setStatus('current')
ieee8021TeipsIpgConfigEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"))
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigEntry.setStatus('current')
ieee8021TeipsIpgConfigState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("workingSegment", 1), ("protectionSegment", 2), ("waitToRestore", 3), ("protAdmin", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigState.setStatus('current')
ieee8021TeipsIpgConfigCommandStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 2), IEEE8021TeipsIpgConfigAdmin()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandStatus.setStatus('current')
ieee8021TeipsIpgConfigCommandLast = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 3), IEEE8021TeipsIpgConfigAdmin()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandLast.setStatus('current')
ieee8021TeipsIpgConfigCommandAdmin = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 4), IEEE8021TeipsIpgConfigAdmin().clone('clear')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigCommandAdmin.setStatus('current')
ieee8021TeipsIpgConfigActiveRequests = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 5), IEEE8021TeipsIpgConfigActiveRequests()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigActiveRequests.setStatus('current')
ieee8021TeipsIpgConfigWTR = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 12), )).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigWTR.setStatus('current')
ieee8021TeipsIpgConfigHoldOff = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('deciseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigHoldOff.setStatus('current')
ieee8021TeipsIpgM1ConfigState = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("psAssigned", 1), ("segmentOk", 2), ("segmentFailed", 3), ("assignNewPs", 4), ("revertToBetterPs", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TeipsIpgM1ConfigState.setStatus('current')
ieee8021TeipsIpgConfigMWTR = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 9), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 12), )).clone(5)).setUnits('minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigMWTR.setStatus('current')
ieee8021TeipsIpgConfigNotifyEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigNotifyEnable.setStatus('current')
ieee8021TeipsIpgConfigStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 11), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021TeipsIpgConfigStorageType.setStatus('current')
ieee8021TeipsIpgAdminFailure = NotificationType((1, 3, 111, 2, 802, 1, 1, 24, 0, 1)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigState"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandStatus"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandLast"))
if mibBuilder.loadTexts: ieee8021TeipsIpgAdminFailure.setStatus('current')
ieee8021TeipsCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 2, 1))
ieee8021TeipsGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 24, 2, 2))
ieee8021TeipsIpgGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 1)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgWorkingMA"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgProtectionMA"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgWorkingPortNumber"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgProtectionPortNumber"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgStorageType"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsIpgGroup = ieee8021TeipsIpgGroup.setStatus('current')
ieee8021TeipsCandidatePsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 2)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsMA"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsPort"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsOper"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsStorageType"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsCandidatePsGroup = ieee8021TeipsCandidatePsGroup.setStatus('current')
ieee8021TeipsIpgTesiGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 3)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiId"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiStorageType"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsIpgTesiGroup = ieee8021TeipsIpgTesiGroup.setStatus('current')
ieee8021TeipsIpgConfigManGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 4)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigState"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandStatus"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandLast"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandAdmin"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigActiveRequests"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigNotifyEnable"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsIpgConfigManGroup = ieee8021TeipsIpgConfigManGroup.setStatus('current')
ieee8021TeipsIpgConfigOptGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 5)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigWTR"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigMWTR"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgM1ConfigState"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigHoldOff"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsIpgConfigOptGroup = ieee8021TeipsIpgConfigOptGroup.setStatus('current')
ieee8021TeipsNotificationsGroup = NotificationGroup((1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 6)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgAdminFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsNotificationsGroup = ieee8021TeipsNotificationsGroup.setStatus('current')
ieee8021TeipsCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 1)).setObjects(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgTesiGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigManGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsNotificationsGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigOptGroup"), ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TeipsCompliance = ieee8021TeipsCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-TEIPS-MIB", ieee8021TeipsCandidatePsRowStatus=ieee8021TeipsCandidatePsRowStatus, ieee8021TeipsConformance=ieee8021TeipsConformance, ieee8021TeipsIpgConfigActiveRequests=ieee8021TeipsIpgConfigActiveRequests, ieee8021TeipsTesiStorageType=ieee8021TeipsTesiStorageType, ieee8021TeipsIpgConfigNotifyEnable=ieee8021TeipsIpgConfigNotifyEnable, ieee8021TeipsIpgConfigCommandStatus=ieee8021TeipsIpgConfigCommandStatus, ieee8021TeipsIpgStorageType=ieee8021TeipsIpgStorageType, ieee8021TeipsIpgTesiGroup=ieee8021TeipsIpgTesiGroup, ieee8021TeipsIpgWorkingMA=ieee8021TeipsIpgWorkingMA, ieee8021TeipsIpgConfigManGroup=ieee8021TeipsIpgConfigManGroup, ieee8021TeipsNotificationsGroup=ieee8021TeipsNotificationsGroup, ieee8021TeipsIpgConfigWTR=ieee8021TeipsIpgConfigWTR, ieee8021TeipsIpgM1ConfigState=ieee8021TeipsIpgM1ConfigState, ieee8021TeipsIpgEntry=ieee8021TeipsIpgEntry, ieee8021TeipsTesiTable=ieee8021TeipsTesiTable, ieee8021TeipsCandidatePsIndex=ieee8021TeipsCandidatePsIndex, ieee8021TeipsCandidatePsTable=ieee8021TeipsCandidatePsTable, ieee8021TeipsIpgProtectionPortNumber=ieee8021TeipsIpgProtectionPortNumber, ieee8021TeipsTesiId=ieee8021TeipsTesiId, ieee8021TeipsCandidatePsMA=ieee8021TeipsCandidatePsMA, ieee8021TeipsNotifications=ieee8021TeipsNotifications, ieee8021TeipsIpgConfigMWTR=ieee8021TeipsIpgConfigMWTR, ieee8021TeipsIpgWorkingPortNumber=ieee8021TeipsIpgWorkingPortNumber, ieee8021TeipsObjects=ieee8021TeipsObjects, ieee8021TeipsCompliance=ieee8021TeipsCompliance, PYSNMP_MODULE_ID=ieee8021TeipsMib, ieee8021TeipsIpgProtectionMA=ieee8021TeipsIpgProtectionMA, ieee8021TeipsIpgConfigHoldOff=ieee8021TeipsIpgConfigHoldOff, ieee8021TeipsTesiRowStatus=ieee8021TeipsTesiRowStatus, ieee8021TeipsGroups=ieee8021TeipsGroups, ieee8021TeipsIpgConfigTable=ieee8021TeipsIpgConfigTable, ieee8021TeipsIpgConfigOptGroup=ieee8021TeipsIpgConfigOptGroup, ieee8021TeipsIpgConfigStorageType=ieee8021TeipsIpgConfigStorageType, ieee8021TeipsIpgConfigCommandLast=ieee8021TeipsIpgConfigCommandLast, ieee8021TeipsIpgConfigEntry=ieee8021TeipsIpgConfigEntry, ieee8021TeipsCandidatePsEntry=ieee8021TeipsCandidatePsEntry, ieee8021TeipsCandidatePsOper=ieee8021TeipsCandidatePsOper, ieee8021TeipsCompliances=ieee8021TeipsCompliances, ieee8021TeipsCandidatePsGroup=ieee8021TeipsCandidatePsGroup, ieee8021TeipsTesiIndex=ieee8021TeipsTesiIndex, ieee8021TeipsCandidatePsStorageType=ieee8021TeipsCandidatePsStorageType, ieee8021TeipsIpgRowStatus=ieee8021TeipsIpgRowStatus, ieee8021TeipsMib=ieee8021TeipsMib, ieee8021TeipsIpgAdminFailure=ieee8021TeipsIpgAdminFailure, ieee8021TeipsIpgConfigState=ieee8021TeipsIpgConfigState, ieee8021TeipsIpgGroup=ieee8021TeipsIpgGroup, ieee8021TeipsTesiEntry=ieee8021TeipsTesiEntry, ieee8021TeipsCandidatePsPort=ieee8021TeipsCandidatePsPort, ieee8021TeipsIpgConfigCommandAdmin=ieee8021TeipsIpgConfigCommandAdmin, ieee8021TeipsIpgid=ieee8021TeipsIpgid, ieee8021TeipsIpgTable=ieee8021TeipsIpgTable)
