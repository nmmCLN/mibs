#
# PySNMP MIB module COLUBRIS-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-DEVICE-MIB.my
# Produced by pysmi-1.1.8 at Fri Jul  8 09:20:26 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, NotificationType, Integer32, Unsigned32, IpAddress, ObjectIdentity, Gauge32, Counter32, iso, MibIdentifier, Bits, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "ObjectIdentity", "Gauge32", "Counter32", "iso", "MibIdentifier", "Bits", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
colubrisDeviceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 23))
if mibBuilder.loadTexts: colubrisDeviceMIB.setLastUpdated('200609050000Z')
if mibBuilder.loadTexts: colubrisDeviceMIB.setOrganization('Colubris Networks, Inc.')
colubrisDeviceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1))
coDeviceConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1))
coDeviceDiscoveryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2))
coDeviceInformationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3))
coDeviceStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4))
coDeviceStateChangeNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 1), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceStateChangeNotificationEnabled.setStatus('current')
coDeviceAuthorizationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceAuthorizationFailureNotificationEnabled.setStatus('current')
coDeviceSecurityFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 3), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceSecurityFailureNotificationEnabled.setStatus('current')
coDeviceFirmwareFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 4), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceFirmwareFailureNotificationEnabled.setStatus('current')
coDeviceConfigurationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 5), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceConfigurationFailureNotificationEnabled.setStatus('current')
coDeviceDiscoveryTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceDiscoveryTable.setStatus('current')
coDeviceDiscoveryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"))
if mibBuilder.loadTexts: coDeviceDiscoveryEntry.setStatus('current')
coDevDisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevDisIndex.setStatus('current')
coDevDisSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisSerialNumber.setStatus('current')
coDevDisMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisMacAddress.setStatus('current')
coDevDisIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisIpAddress.setStatus('current')
coDevDisState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disconnected", 1), ("authorized", 2), ("join", 3), ("firmware", 4), ("security", 5), ("configuration", 6), ("running", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisState.setStatus('current')
coDevDisSystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisSystemName.setStatus('current')
coDevDisLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisLocation.setStatus('current')
coDevDisContact = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisContact.setStatus('current')
coDevDisGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisGroupName.setStatus('current')
coDevDisConnectionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 10), Counter32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisConnectionTime.setStatus('current')
coDeviceInfoTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1), )
if mibBuilder.loadTexts: coDeviceInfoTable.setStatus('current')
coDeviceInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1), )
coDeviceDiscoveryEntry.registerAugmentions(("COLUBRIS-DEVICE-MIB", "coDeviceInfoEntry"))
coDeviceInfoEntry.setIndexNames(*coDeviceDiscoveryEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceInfoEntry.setStatus('current')
coDevInfoProductType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoProductType.setStatus('current')
coDevInfoProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoProductName.setStatus('current')
coDevInfoFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoFirmwareRevision.setStatus('current')
coDevInfoBootRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoBootRevision.setStatus('current')
coDevInfoHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoHardwareRevision.setStatus('current')
coDeviceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1), )
if mibBuilder.loadTexts: coDeviceStatusTable.setStatus('current')
coDeviceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1), )
coDeviceDiscoveryEntry.registerAugmentions(("COLUBRIS-DEVICE-MIB", "coDeviceStatusEntry"))
coDeviceStatusEntry.setIndexNames(*coDeviceDiscoveryEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceStatusEntry.setStatus('current')
coDevStUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStUpTime.setStatus('current')
coDevStLoadAverage1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStLoadAverage1Min.setStatus('current')
coDevStLoadAverage5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStLoadAverage5Min.setStatus('current')
coDevStLoadAverage15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStLoadAverage15Min.setStatus('current')
coDevStCpuUseNow = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 5), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStCpuUseNow.setStatus('current')
coDevStCpuUse5Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 6), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStCpuUse5Sec.setStatus('current')
coDevStCpuUse10Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 7), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStCpuUse10Sec.setStatus('current')
coDevStCpuUse20Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 8), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStCpuUse20Sec.setStatus('current')
coDevStRamTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 9), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStRamTotal.setStatus('current')
coDevStRamFree = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 10), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStRamFree.setStatus('current')
coDevStRamBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 11), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStRamBuffer.setStatus('current')
coDevStRamCached = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 12), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStRamCached.setStatus('current')
coDevStStorageUsePermanent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 13), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStStorageUsePermanent.setStatus('current')
coDevStStorageUseTemporary = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 14), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStStorageUseTemporary.setStatus('current')
colubrisDeviceMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2))
colubrisDeviceMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0))
coDeviceStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 1)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceStateChangeNotification.setStatus('current')
coDeviceAuthorizationFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 2)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceAuthorizationFailureNotification.setStatus('current')
coDeviceSecurityFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 3)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceSecurityFailureNotification.setStatus('current')
coDeviceFirmwareFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 4)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceFirmwareFailureNotification.setStatus('current')
coDeviceConfigurationFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 5)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceConfigurationFailureNotification.setStatus('current')
colubrisDeviceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3))
colubrisDeviceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 1))
colubrisDeviceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2))
colubrisDeviceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 1, 1)).setObjects(("COLUBRIS-DEVICE-MIB", "colubrisDeviceConfigMIBGroup"), ("COLUBRIS-DEVICE-MIB", "colubrisDeviceDiscoveryMIBGroup"), ("COLUBRIS-DEVICE-MIB", "colubrisDeviceInformationMIBGroup"), ("COLUBRIS-DEVICE-MIB", "colubrisDeviceStatusMIBGroup"), ("COLUBRIS-DEVICE-MIB", "colubrisDeviceNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceMIBCompliance = colubrisDeviceMIBCompliance.setStatus('current')
colubrisDeviceConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 1)).setObjects(("COLUBRIS-DEVICE-MIB", "coDeviceStateChangeNotificationEnabled"), ("COLUBRIS-DEVICE-MIB", "coDeviceAuthorizationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-MIB", "coDeviceSecurityFailureNotificationEnabled"), ("COLUBRIS-DEVICE-MIB", "coDeviceFirmwareFailureNotificationEnabled"), ("COLUBRIS-DEVICE-MIB", "coDeviceConfigurationFailureNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceConfigMIBGroup = colubrisDeviceConfigMIBGroup.setStatus('current')
colubrisDeviceDiscoveryMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 2)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisMacAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"), ("COLUBRIS-DEVICE-MIB", "coDevDisLocation"), ("COLUBRIS-DEVICE-MIB", "coDevDisContact"), ("COLUBRIS-DEVICE-MIB", "coDevDisGroupName"), ("COLUBRIS-DEVICE-MIB", "coDevDisConnectionTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceDiscoveryMIBGroup = colubrisDeviceDiscoveryMIBGroup.setStatus('current')
colubrisDeviceInformationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 3)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevInfoProductType"), ("COLUBRIS-DEVICE-MIB", "coDevInfoProductName"), ("COLUBRIS-DEVICE-MIB", "coDevInfoFirmwareRevision"), ("COLUBRIS-DEVICE-MIB", "coDevInfoBootRevision"), ("COLUBRIS-DEVICE-MIB", "coDevInfoHardwareRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceInformationMIBGroup = colubrisDeviceInformationMIBGroup.setStatus('current')
colubrisDeviceStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 4)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevStUpTime"), ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage1Min"), ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage5Min"), ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage15Min"), ("COLUBRIS-DEVICE-MIB", "coDevStCpuUseNow"), ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse5Sec"), ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse10Sec"), ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse20Sec"), ("COLUBRIS-DEVICE-MIB", "coDevStRamTotal"), ("COLUBRIS-DEVICE-MIB", "coDevStRamFree"), ("COLUBRIS-DEVICE-MIB", "coDevStRamBuffer"), ("COLUBRIS-DEVICE-MIB", "coDevStRamCached"), ("COLUBRIS-DEVICE-MIB", "coDevStStorageUsePermanent"), ("COLUBRIS-DEVICE-MIB", "coDevStStorageUseTemporary"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceStatusMIBGroup = colubrisDeviceStatusMIBGroup.setStatus('current')
colubrisDeviceNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 5)).setObjects(("COLUBRIS-DEVICE-MIB", "coDeviceStateChangeNotification"), ("COLUBRIS-DEVICE-MIB", "coDeviceAuthorizationFailureNotification"), ("COLUBRIS-DEVICE-MIB", "coDeviceSecurityFailureNotification"), ("COLUBRIS-DEVICE-MIB", "coDeviceFirmwareFailureNotification"), ("COLUBRIS-DEVICE-MIB", "coDeviceConfigurationFailureNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceNotificationGroup = colubrisDeviceNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-MIB", coDeviceAuthorizationFailureNotificationEnabled=coDeviceAuthorizationFailureNotificationEnabled, coDevDisConnectionTime=coDevDisConnectionTime, coDeviceDiscoveryTable=coDeviceDiscoveryTable, coDevInfoFirmwareRevision=coDevInfoFirmwareRevision, coDevStCpuUse10Sec=coDevStCpuUse10Sec, coDeviceStateChangeNotificationEnabled=coDeviceStateChangeNotificationEnabled, coDeviceFirmwareFailureNotificationEnabled=coDeviceFirmwareFailureNotificationEnabled, coDevDisGroupName=coDevDisGroupName, colubrisDeviceMIBNotifications=colubrisDeviceMIBNotifications, coDeviceSecurityFailureNotificationEnabled=coDeviceSecurityFailureNotificationEnabled, coDeviceDiscoveryEntry=coDeviceDiscoveryEntry, coDeviceStatusEntry=coDeviceStatusEntry, coDeviceAuthorizationFailureNotification=coDeviceAuthorizationFailureNotification, coDevStLoadAverage15Min=coDevStLoadAverage15Min, colubrisDeviceMIBCompliance=colubrisDeviceMIBCompliance, coDevStLoadAverage5Min=coDevStLoadAverage5Min, coDeviceStatusTable=coDeviceStatusTable, coDeviceInfoTable=coDeviceInfoTable, colubrisDeviceConfigMIBGroup=colubrisDeviceConfigMIBGroup, colubrisDeviceInformationMIBGroup=colubrisDeviceInformationMIBGroup, coDeviceSecurityFailureNotification=coDeviceSecurityFailureNotification, colubrisDeviceStatusMIBGroup=colubrisDeviceStatusMIBGroup, colubrisDeviceMIBNotificationPrefix=colubrisDeviceMIBNotificationPrefix, coDeviceInformationGroup=coDeviceInformationGroup, colubrisDeviceMIBObjects=colubrisDeviceMIBObjects, coDevStCpuUse5Sec=coDevStCpuUse5Sec, coDevDisContact=coDevDisContact, coDeviceFirmwareFailureNotification=coDeviceFirmwareFailureNotification, coDevDisMacAddress=coDevDisMacAddress, coDevStRamBuffer=coDevStRamBuffer, coDevDisSerialNumber=coDevDisSerialNumber, coDevStCpuUse20Sec=coDevStCpuUse20Sec, colubrisDeviceMIBGroups=colubrisDeviceMIBGroups, coDevDisLocation=coDevDisLocation, coDevDisState=coDevDisState, coDevInfoBootRevision=coDevInfoBootRevision, coDevStUpTime=coDevStUpTime, coDevStRamTotal=coDevStRamTotal, coDevStRamFree=coDevStRamFree, coDeviceInfoEntry=coDeviceInfoEntry, coDevStRamCached=coDevStRamCached, coDeviceStateChangeNotification=coDeviceStateChangeNotification, coDevStStorageUsePermanent=coDevStStorageUsePermanent, colubrisDeviceMIBConformance=colubrisDeviceMIBConformance, PYSNMP_MODULE_ID=colubrisDeviceMIB, coDeviceDiscoveryGroup=coDeviceDiscoveryGroup, coDeviceConfigurationFailureNotificationEnabled=coDeviceConfigurationFailureNotificationEnabled, coDevDisIndex=coDevDisIndex, coDevDisIpAddress=coDevDisIpAddress, coDeviceStatusGroup=coDeviceStatusGroup, coDevInfoProductType=coDevInfoProductType, coDevStLoadAverage1Min=coDevStLoadAverage1Min, colubrisDeviceNotificationGroup=colubrisDeviceNotificationGroup, colubrisDeviceMIB=colubrisDeviceMIB, coDevDisSystemName=coDevDisSystemName, coDevStStorageUseTemporary=coDevStStorageUseTemporary, coDevStCpuUseNow=coDevStCpuUseNow, colubrisDeviceDiscoveryMIBGroup=colubrisDeviceDiscoveryMIBGroup, coDeviceConfigurationFailureNotification=coDeviceConfigurationFailureNotification, coDeviceConfigGroup=coDeviceConfigGroup, colubrisDeviceMIBCompliances=colubrisDeviceMIBCompliances, coDevInfoHardwareRevision=coDevInfoHardwareRevision, coDevInfoProductName=coDevInfoProductName)
