#
# PySNMP MIB module COLUBRIS-CONNECTION-LIMITING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-CONNECTION-LIMITING-MIB.my
# Produced by pysmi-1.1.8 at Fri Jul  8 08:03:19 2022
# On host fv-az121-197 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, ModuleIdentity, NotificationType, Bits, ObjectIdentity, MibIdentifier, IpAddress, Integer32, Gauge32, Unsigned32, iso, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "NotificationType", "Bits", "ObjectIdentity", "MibIdentifier", "IpAddress", "Integer32", "Gauge32", "Unsigned32", "iso", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
colubrisConnectionLimitingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 18))
if mibBuilder.loadTexts: colubrisConnectionLimitingMIB.setLastUpdated('200501210000Z')
if mibBuilder.loadTexts: colubrisConnectionLimitingMIB.setOrganization('Colubris Networks, Inc.')
colubrisConnectionLimitingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1))
connectionLimitingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1))
connectionLimitingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2))
connectionLimitingMaximumUserConnections = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnections.setStatus('current')
connectionLimitingNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingNotificationEnabled.setStatus('current')
connectionLimitingMaximumSystemConnections = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionLimitingMaximumSystemConnections.setStatus('current')
connectionLimitingUserMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: connectionLimitingUserMACAddress.setStatus('current')
connectionLimitingUserIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: connectionLimitingUserIPAddress.setStatus('current')
colubrisConnectionLimitingMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2))
colubrisConnectionLimitingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2, 0))
connectionLimitingMaximumUserConnectionsReached = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2, 0, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserMACAddress"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserIPAddress"))
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnectionsReached.setStatus('current')
colubrisConnectionLimitingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3))
colubrisConnectionLimitingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 1))
colubrisConnectionLimitingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2))
colubrisConnectionLimitingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 1, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingConfigMIBGroup"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingInfoMIBGroup"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingMIBCompliance = colubrisConnectionLimitingMIBCompliance.setStatus('current')
colubrisConnectionLimitingConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingConfigMIBGroup = colubrisConnectionLimitingConfigMIBGroup.setStatus('current')
colubrisConnectionLimitingInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 2)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumSystemConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserMACAddress"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserIPAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingInfoMIBGroup = colubrisConnectionLimitingInfoMIBGroup.setStatus('current')
colubrisConnectionLimitingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 3)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnectionsReached"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingNotificationGroup = colubrisConnectionLimitingNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-CONNECTION-LIMITING-MIB", colubrisConnectionLimitingMIBConformance=colubrisConnectionLimitingMIBConformance, colubrisConnectionLimitingNotificationGroup=colubrisConnectionLimitingNotificationGroup, colubrisConnectionLimitingConfigMIBGroup=colubrisConnectionLimitingConfigMIBGroup, colubrisConnectionLimitingMIBNotificationPrefix=colubrisConnectionLimitingMIBNotificationPrefix, colubrisConnectionLimitingInfoMIBGroup=colubrisConnectionLimitingInfoMIBGroup, colubrisConnectionLimitingMIBObjects=colubrisConnectionLimitingMIBObjects, colubrisConnectionLimitingMIBNotifications=colubrisConnectionLimitingMIBNotifications, PYSNMP_MODULE_ID=colubrisConnectionLimitingMIB, connectionLimitingUserIPAddress=connectionLimitingUserIPAddress, colubrisConnectionLimitingMIBCompliance=colubrisConnectionLimitingMIBCompliance, connectionLimitingInfo=connectionLimitingInfo, connectionLimitingMaximumUserConnectionsReached=connectionLimitingMaximumUserConnectionsReached, colubrisConnectionLimitingMIBCompliances=colubrisConnectionLimitingMIBCompliances, connectionLimitingNotificationEnabled=connectionLimitingNotificationEnabled, colubrisConnectionLimitingMIB=colubrisConnectionLimitingMIB, connectionLimitingConfig=connectionLimitingConfig, connectionLimitingMaximumUserConnections=connectionLimitingMaximumUserConnections, connectionLimitingMaximumSystemConnections=connectionLimitingMaximumSystemConnections, colubrisConnectionLimitingMIBGroups=colubrisConnectionLimitingMIBGroups, connectionLimitingUserMACAddress=connectionLimitingUserMACAddress)
