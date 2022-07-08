#
# PySNMP MIB module COLUBRIS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SYSTEM-MIB.my
# Produced by pysmi-1.1.8 at Fri Jul  8 09:20:26 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisProfileIndexOrZero, ColubrisAuthenticationMode, ColubrisNotificationEnable = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisProfileIndexOrZero", "ColubrisAuthenticationMode", "ColubrisNotificationEnable")
ifInUcastPkts, ifOutErrors, ifInErrors, ifOutUcastPkts = mibBuilder.importSymbols("IF-MIB", "ifInUcastPkts", "ifOutErrors", "ifInErrors", "ifOutUcastPkts")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, NotificationType, Integer32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, iso, MibIdentifier, Bits, Counter64, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "iso", "MibIdentifier", "Bits", "Counter64", "TimeTicks", "Counter32")
TruthValue, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TextualConvention", "DisplayString")
colubrisSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 6))
if mibBuilder.loadTexts: colubrisSystemMIB.setLastUpdated('200703200000Z')
if mibBuilder.loadTexts: colubrisSystemMIB.setOrganization('Colubris Networks, Inc.')
colubrisSystemMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1))
systemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1))
systemTime = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2))
adminAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3))
heartbeat = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 4))
systemProductName = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemProductName.setStatus('current')
systemFirmwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemFirmwareRevision.setStatus('current')
systemBootRevision = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemBootRevision.setStatus('current')
systemHardwareRevision = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemHardwareRevision.setStatus('current')
systemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemSerialNumber.setStatus('current')
systemConfigurationVersion = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemConfigurationVersion.setStatus('current')
systemUpTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 7), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpTime.setStatus('current')
systemMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 8), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: systemMacAddress.setStatus('current')
systemWanPortIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 9), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: systemWanPortIpAddress.setStatus('current')
systemProductFlavor = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemProductFlavor.setStatus('current')
systemDeviceIdentification = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 1, 11), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemDeviceIdentification.setStatus('current')
systemTimeUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("sntpUdp", 2), ("tp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeUpdateMode.setStatus('current')
systemTimeLostWhenRebooting = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTimeLostWhenRebooting.setStatus('current')
systemTimeDSTOn = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeDSTOn.setStatus('current')
systemDate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemDate.setStatus('current')
systemTimeOfDay = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeOfDay.setStatus('current')
systemTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeZone.setStatus('current')
systemTimeServerTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 7), )
if mibBuilder.loadTexts: systemTimeServerTable.setStatus('current')
systemTimeServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 7, 1), ).setIndexNames((0, "COLUBRIS-SYSTEM-MIB", "systemTimeServerIndex"))
if mibBuilder.loadTexts: systemTimeServerEntry.setStatus('current')
systemTimeServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: systemTimeServerIndex.setStatus('current')
systemTimeServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 7, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeServerAddress.setStatus('current')
systemTimeServerNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 2, 8), ColubrisNotificationEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemTimeServerNotificationEnabled.setStatus('current')
adminAccessAuthenMode = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 1), ColubrisAuthenticationMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessAuthenMode.setStatus('current')
adminAccessAuthenProfileIndex = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 2), ColubrisProfileIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessAuthenProfileIndex.setStatus('current')
adminAccessMaxLoginAttempts = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessMaxLoginAttempts.setStatus('current')
adminAccessLockOutPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessLockOutPeriod.setStatus('current')
adminAccessLoginNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 5), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessLoginNotificationEnabled.setStatus('current')
adminAccessAuthFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 6), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessAuthFailureNotificationEnabled.setStatus('current')
adminAccessInfo = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adminAccessInfo.setStatus('current')
adminAccessProfileTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8), )
if mibBuilder.loadTexts: adminAccessProfileTable.setStatus('current')
adminAccessProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8, 1), ).setIndexNames((0, "COLUBRIS-SYSTEM-MIB", "adminAccessProfileIndex"))
if mibBuilder.loadTexts: adminAccessProfileEntry.setStatus('current')
adminAccessProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: adminAccessProfileIndex.setStatus('current')
adminAccessUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminAccessUserName.setStatus('current')
adminAccessAdministrativeRights = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adminAccessAdministrativeRights.setStatus('current')
adminAccessLogoutNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 3, 9), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adminAccessLogoutNotificationEnabled.setStatus('current')
heartbeatPeriod = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 31536000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: heartbeatPeriod.setStatus('current')
heartbeatNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 6, 1, 4, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: heartbeatNotificationEnabled.setStatus('current')
colubrisSystemMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2))
colubrisSystemMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0))
adminAccessAuthFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 1)).setObjects(("COLUBRIS-SYSTEM-MIB", "adminAccessInfo"))
if mibBuilder.loadTexts: adminAccessAuthFailureNotification.setStatus('current')
adminAccessLoginNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 2))
if mibBuilder.loadTexts: adminAccessLoginNotification.setStatus('current')
systemColdStart = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 3)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemProductName"), ("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision"), ("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion"), ("COLUBRIS-SYSTEM-MIB", "systemSerialNumber"))
if mibBuilder.loadTexts: systemColdStart.setStatus('current')
systemHeartbeatNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 4)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemSerialNumber"), ("COLUBRIS-SYSTEM-MIB", "systemMacAddress"), ("COLUBRIS-SYSTEM-MIB", "systemWanPortIpAddress"), ("COLUBRIS-SYSTEM-MIB", "systemUpTime"), ("IF-MIB", "ifOutUcastPkts"), ("IF-MIB", "ifInUcastPkts"), ("IF-MIB", "ifOutErrors"), ("IF-MIB", "ifInErrors"), ("IF-MIB", "ifOutUcastPkts"), ("IF-MIB", "ifInUcastPkts"), ("IF-MIB", "ifOutErrors"), ("IF-MIB", "ifInErrors"), ("IF-MIB", "ifOutUcastPkts"), ("IF-MIB", "ifInUcastPkts"), ("IF-MIB", "ifOutErrors"), ("IF-MIB", "ifInErrors"))
if mibBuilder.loadTexts: systemHeartbeatNotification.setStatus('current')
adminAccessLogoutNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 5)).setObjects(("COLUBRIS-SYSTEM-MIB", "adminAccessInfo"))
if mibBuilder.loadTexts: adminAccessLogoutNotification.setStatus('current')
timeServerFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 6, 2, 0, 6)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemTimeServerAddress"))
if mibBuilder.loadTexts: timeServerFailure.setStatus('current')
colubrisSystemMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3))
colubrisSystemMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 1))
colubrisSystemMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2))
colubrisSystemMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 1, 1)).setObjects(("COLUBRIS-SYSTEM-MIB", "colubrisSystemMIBGroup"), ("COLUBRIS-SYSTEM-MIB", "colubrisSystemNotificationGroup"), ("COLUBRIS-SYSTEM-MIB", "colubrisAdminAccessProfileGroup"), ("COLUBRIS-SYSTEM-MIB", "colubrisAdminAccessNotificationGroup"), ("COLUBRIS-SYSTEM-MIB", "colubrisTimeNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSystemMIBCompliance = colubrisSystemMIBCompliance.setStatus('current')
colubrisSystemMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 1)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemProductName"), ("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision"), ("COLUBRIS-SYSTEM-MIB", "systemBootRevision"), ("COLUBRIS-SYSTEM-MIB", "systemHardwareRevision"), ("COLUBRIS-SYSTEM-MIB", "systemSerialNumber"), ("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion"), ("COLUBRIS-SYSTEM-MIB", "systemUpTime"), ("COLUBRIS-SYSTEM-MIB", "systemMacAddress"), ("COLUBRIS-SYSTEM-MIB", "systemWanPortIpAddress"), ("COLUBRIS-SYSTEM-MIB", "systemProductFlavor"), ("COLUBRIS-SYSTEM-MIB", "systemDeviceIdentification"), ("COLUBRIS-SYSTEM-MIB", "systemTimeUpdateMode"), ("COLUBRIS-SYSTEM-MIB", "systemTimeLostWhenRebooting"), ("COLUBRIS-SYSTEM-MIB", "systemTimeDSTOn"), ("COLUBRIS-SYSTEM-MIB", "systemDate"), ("COLUBRIS-SYSTEM-MIB", "systemTimeOfDay"), ("COLUBRIS-SYSTEM-MIB", "systemTimeZone"), ("COLUBRIS-SYSTEM-MIB", "systemTimeServerAddress"), ("COLUBRIS-SYSTEM-MIB", "systemTimeServerNotificationEnabled"), ("COLUBRIS-SYSTEM-MIB", "heartbeatPeriod"), ("COLUBRIS-SYSTEM-MIB", "heartbeatNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSystemMIBGroup = colubrisSystemMIBGroup.setStatus('current')
colubrisAdminAccessProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 2)).setObjects(("COLUBRIS-SYSTEM-MIB", "adminAccessAuthenMode"), ("COLUBRIS-SYSTEM-MIB", "adminAccessMaxLoginAttempts"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLockOutPeriod"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLoginNotificationEnabled"), ("COLUBRIS-SYSTEM-MIB", "adminAccessAuthFailureNotificationEnabled"), ("COLUBRIS-SYSTEM-MIB", "adminAccessAuthenProfileIndex"), ("COLUBRIS-SYSTEM-MIB", "adminAccessInfo"), ("COLUBRIS-SYSTEM-MIB", "adminAccessUserName"), ("COLUBRIS-SYSTEM-MIB", "adminAccessAdministrativeRights"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLogoutNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisAdminAccessProfileGroup = colubrisAdminAccessProfileGroup.setStatus('current')
colubrisSystemNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 3)).setObjects(("COLUBRIS-SYSTEM-MIB", "systemColdStart"), ("COLUBRIS-SYSTEM-MIB", "systemHeartbeatNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSystemNotificationGroup = colubrisSystemNotificationGroup.setStatus('current')
colubrisAdminAccessNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 4)).setObjects(("COLUBRIS-SYSTEM-MIB", "adminAccessAuthFailureNotification"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLoginNotification"), ("COLUBRIS-SYSTEM-MIB", "adminAccessLogoutNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisAdminAccessNotificationGroup = colubrisAdminAccessNotificationGroup.setStatus('current')
colubrisTimeNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 6, 3, 2, 5)).setObjects(("COLUBRIS-SYSTEM-MIB", "timeServerFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisTimeNotificationGroup = colubrisTimeNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-SYSTEM-MIB", systemTimeZone=systemTimeZone, adminAccessMaxLoginAttempts=adminAccessMaxLoginAttempts, adminAccessAuthenProfileIndex=adminAccessAuthenProfileIndex, colubrisSystemMIBObjects=colubrisSystemMIBObjects, systemFirmwareRevision=systemFirmwareRevision, adminAccessLoginNotificationEnabled=adminAccessLoginNotificationEnabled, colubrisSystemMIBGroups=colubrisSystemMIBGroups, adminAccessAuthenMode=adminAccessAuthenMode, adminAccessProfileEntry=adminAccessProfileEntry, systemDeviceIdentification=systemDeviceIdentification, systemDate=systemDate, systemTimeLostWhenRebooting=systemTimeLostWhenRebooting, systemProductFlavor=systemProductFlavor, adminAccessUserName=adminAccessUserName, systemTimeServerTable=systemTimeServerTable, systemTimeServerEntry=systemTimeServerEntry, colubrisSystemMIB=colubrisSystemMIB, systemConfigurationVersion=systemConfigurationVersion, colubrisTimeNotificationGroup=colubrisTimeNotificationGroup, adminAccessLogoutNotificationEnabled=adminAccessLogoutNotificationEnabled, systemUpTime=systemUpTime, colubrisSystemMIBCompliances=colubrisSystemMIBCompliances, systemTimeOfDay=systemTimeOfDay, systemSerialNumber=systemSerialNumber, systemHeartbeatNotification=systemHeartbeatNotification, colubrisAdminAccessNotificationGroup=colubrisAdminAccessNotificationGroup, systemColdStart=systemColdStart, colubrisSystemNotificationGroup=colubrisSystemNotificationGroup, adminAccessInfo=adminAccessInfo, systemTimeDSTOn=systemTimeDSTOn, adminAccessLockOutPeriod=adminAccessLockOutPeriod, colubrisSystemMIBGroup=colubrisSystemMIBGroup, colubrisSystemMIBNotificationPrefix=colubrisSystemMIBNotificationPrefix, systemProductName=systemProductName, colubrisAdminAccessProfileGroup=colubrisAdminAccessProfileGroup, timeServerFailure=timeServerFailure, PYSNMP_MODULE_ID=colubrisSystemMIB, systemMacAddress=systemMacAddress, adminAccessLoginNotification=adminAccessLoginNotification, systemHardwareRevision=systemHardwareRevision, adminAccess=adminAccess, systemBootRevision=systemBootRevision, systemTimeServerNotificationEnabled=systemTimeServerNotificationEnabled, heartbeatNotificationEnabled=heartbeatNotificationEnabled, colubrisSystemMIBConformance=colubrisSystemMIBConformance, systemTimeUpdateMode=systemTimeUpdateMode, adminAccessAdministrativeRights=adminAccessAdministrativeRights, heartbeat=heartbeat, colubrisSystemMIBNotifications=colubrisSystemMIBNotifications, adminAccessAuthFailureNotificationEnabled=adminAccessAuthFailureNotificationEnabled, colubrisSystemMIBCompliance=colubrisSystemMIBCompliance, systemTime=systemTime, systemInfo=systemInfo, systemTimeServerIndex=systemTimeServerIndex, heartbeatPeriod=heartbeatPeriod, systemWanPortIpAddress=systemWanPortIpAddress, adminAccessProfileIndex=adminAccessProfileIndex, systemTimeServerAddress=systemTimeServerAddress, adminAccessProfileTable=adminAccessProfileTable, adminAccessAuthFailureNotification=adminAccessAuthFailureNotification, adminAccessLogoutNotification=adminAccessLogoutNotification)
