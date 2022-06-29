#
# PySNMP MIB module COLUBRIS-SATELLITE-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SATELLITE-MANAGEMENT-MIB.my
# Produced by pysmi-1.1.8 at Wed Jun 29 13:09:22 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, ColubrisSSIDOrNone = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable", "ColubrisSSIDOrNone")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Gauge32, ObjectIdentity, IpAddress, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Unsigned32, ModuleIdentity, Bits, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits", "NotificationType", "Integer32")
MacAddress, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "DisplayString", "TextualConvention")
colubrisSatelliteManagementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 7))
if mibBuilder.loadTexts: colubrisSatelliteManagementMIB.setLastUpdated('200602230000Z')
if mibBuilder.loadTexts: colubrisSatelliteManagementMIB.setOrganization('Colubris Networks, Inc.')
colubrisSatelliteManagementMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1))
satelliteInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1))
masterSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2))
satelliteTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1), )
if mibBuilder.loadTexts: satelliteTable.setStatus('current')
satelliteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIndex"))
if mibBuilder.loadTexts: satelliteEntry.setStatus('current')
satelliteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: satelliteIndex.setStatus('current')
satelliteDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDeviceId.setStatus('current')
satelliteMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteMacAddress.setStatus('current')
satelliteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteIpAddress.setStatus('current')
satelliteName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteName.setStatus('current')
satelliteSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 6), ColubrisSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSSID.setStatus('current')
satelliteChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteChannelNumber.setStatus('current')
satelliteForwardWirelessToWireless = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteForwardWirelessToWireless.setStatus('current')
satelliteMasterTrafficOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteMasterTrafficOnly.setStatus('current')
satelliteSNMPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSNMPPort.setStatus('current')
satelliteSecureWebPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteSecureWebPort.setStatus('current')
satelliteDeviceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDeviceMacAddress.setStatus('current')
satelliteProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteProductName.setStatus('current')
satelliteFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteFirmwareRevision.setStatus('current')
satelliteGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteGroupName.setStatus('current')
satelliteChannelNumberRadio2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteChannelNumberRadio2.setStatus('current')
satelliteVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteVLAN.setStatus('current')
satelliteDetectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteDetectionPort.setStatus('current')
satelliteNumber = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: satelliteNumber.setStatus('current')
satelliteUpNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2, 1), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: satelliteUpNotificationEnabled.setStatus('current')
satelliteDownNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 7, 1, 2, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: satelliteDownNotificationEnabled.setStatus('current')
colubrisSatelliteManagementMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 2))
colubrisSatelliteManagementMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0))
satelliteUpNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0, 1)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"))
if mibBuilder.loadTexts: satelliteUpNotification.setStatus('current')
satelliteDownNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 7, 2, 0, 2)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"))
if mibBuilder.loadTexts: satelliteDownNotification.setStatus('current')
colubrisSatelliteManagementMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3))
colubrisSatelliteManagementMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 1))
colubrisSatelliteManagementMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2))
colubrisSatelliteManagementMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 1, 1)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "colubrisSatelliteManagementMIBGroup"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "colubrisSatelliteNotificationControlGroup"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "colubrisSatelliteNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSatelliteManagementMIBCompliance = colubrisSatelliteManagementMIBCompliance.setStatus('current')
colubrisSatelliteManagementMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 1)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceId"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMacAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteIpAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSSID"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteChannelNumber"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteForwardWirelessToWireless"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteMasterTrafficOnly"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSNMPPort"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteSecureWebPort"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDeviceMacAddress"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteProductName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteFirmwareRevision"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteGroupName"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteNumber"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteChannelNumberRadio2"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteVLAN"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDetectionPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSatelliteManagementMIBGroup = colubrisSatelliteManagementMIBGroup.setStatus('current')
colubrisSatelliteNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 2)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteUpNotificationEnabled"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDownNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSatelliteNotificationControlGroup = colubrisSatelliteNotificationControlGroup.setStatus('current')
colubrisSatelliteNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 7, 3, 2, 3)).setObjects(("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteUpNotification"), ("COLUBRIS-SATELLITE-MANAGEMENT-MIB", "satelliteDownNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSatelliteNotificationGroup = colubrisSatelliteNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-SATELLITE-MANAGEMENT-MIB", satelliteUpNotificationEnabled=satelliteUpNotificationEnabled, colubrisSatelliteManagementMIBNotifications=colubrisSatelliteManagementMIBNotifications, PYSNMP_MODULE_ID=colubrisSatelliteManagementMIB, satelliteIndex=satelliteIndex, satelliteIpAddress=satelliteIpAddress, satelliteGroupName=satelliteGroupName, colubrisSatelliteManagementMIBGroups=colubrisSatelliteManagementMIBGroups, colubrisSatelliteManagementMIBNotificationPrefix=colubrisSatelliteManagementMIBNotificationPrefix, satelliteSSID=satelliteSSID, satelliteSecureWebPort=satelliteSecureWebPort, satelliteUpNotification=satelliteUpNotification, colubrisSatelliteNotificationControlGroup=colubrisSatelliteNotificationControlGroup, satelliteMacAddress=satelliteMacAddress, satelliteDeviceId=satelliteDeviceId, colubrisSatelliteManagementMIBObjects=colubrisSatelliteManagementMIBObjects, satelliteNumber=satelliteNumber, satelliteEntry=satelliteEntry, satelliteVLAN=satelliteVLAN, satelliteName=satelliteName, satelliteChannelNumberRadio2=satelliteChannelNumberRadio2, satelliteDownNotification=satelliteDownNotification, satelliteMasterTrafficOnly=satelliteMasterTrafficOnly, satelliteProductName=satelliteProductName, colubrisSatelliteManagementMIBCompliance=colubrisSatelliteManagementMIBCompliance, satelliteDownNotificationEnabled=satelliteDownNotificationEnabled, colubrisSatelliteManagementMIBCompliances=colubrisSatelliteManagementMIBCompliances, satelliteDetectionPort=satelliteDetectionPort, satelliteSNMPPort=satelliteSNMPPort, masterSettings=masterSettings, satelliteChannelNumber=satelliteChannelNumber, colubrisSatelliteManagementMIBGroup=colubrisSatelliteManagementMIBGroup, colubrisSatelliteManagementMIB=colubrisSatelliteManagementMIB, colubrisSatelliteNotificationGroup=colubrisSatelliteNotificationGroup, satelliteTable=satelliteTable, satelliteDeviceMacAddress=satelliteDeviceMacAddress, satelliteForwardWirelessToWireless=satelliteForwardWirelessToWireless, satelliteInfo=satelliteInfo, satelliteFirmwareRevision=satelliteFirmwareRevision, colubrisSatelliteManagementMIBConformance=colubrisSatelliteManagementMIBConformance)
