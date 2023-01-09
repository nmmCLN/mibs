#
# PySNMP MIB module COLUBRIS-TOOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-TOOLS-MIB.my
# Produced by pysmi-1.1.8 at Mon Jan  9 10:31:12 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Bits, Unsigned32, MibIdentifier, Integer32, iso, Counter64, NotificationType, Counter32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "Integer32", "iso", "Counter64", "NotificationType", "Counter32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisToolsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 12))
if mibBuilder.loadTexts: colubrisToolsMIB.setLastUpdated('200402200000Z')
if mibBuilder.loadTexts: colubrisToolsMIB.setOrganization('Colubris Networks, Inc.')
colubrisToolsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1))
traceToolConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1))
traceInterface = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceInterface.setStatus('current')
traceCaptureDestination = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureDestination.setStatus('current')
traceCaptureDestinationURL = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureDestinationURL.setStatus('current')
traceTimeout = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999)).clone(600)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceTimeout.setStatus('current')
traceNumberOfPackets = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999)).clone(100)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceNumberOfPackets.setStatus('current')
tracePacketSize = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(68, 4096)).clone(128)).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tracePacketSize.setStatus('current')
traceCaptureFilter = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureFilter.setStatus('current')
traceCaptureStatus = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2))).clone('stop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceCaptureStatus.setStatus('current')
traceNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 12, 1, 1, 9), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: traceNotificationEnabled.setStatus('current')
colubrisToolsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 2))
colubrisToolsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 2, 0))
traceStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 12, 2, 0, 1)).setObjects(("COLUBRIS-TOOLS-MIB", "traceCaptureStatus"))
if mibBuilder.loadTexts: traceStatusNotification.setStatus('current')
colubrisToolsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3))
colubrisToolsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 1))
colubrisToolsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 2))
colubrisToolsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 1, 1)).setObjects(("COLUBRIS-TOOLS-MIB", "colubrisToolsMIBGroup"), ("COLUBRIS-TOOLS-MIB", "colubrisToolsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisToolsMIBCompliance = colubrisToolsMIBCompliance.setStatus('current')
colubrisToolsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 2, 1)).setObjects(("COLUBRIS-TOOLS-MIB", "traceInterface"), ("COLUBRIS-TOOLS-MIB", "traceCaptureDestination"), ("COLUBRIS-TOOLS-MIB", "traceCaptureDestinationURL"), ("COLUBRIS-TOOLS-MIB", "traceTimeout"), ("COLUBRIS-TOOLS-MIB", "traceNumberOfPackets"), ("COLUBRIS-TOOLS-MIB", "tracePacketSize"), ("COLUBRIS-TOOLS-MIB", "traceCaptureFilter"), ("COLUBRIS-TOOLS-MIB", "traceCaptureStatus"), ("COLUBRIS-TOOLS-MIB", "traceNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisToolsMIBGroup = colubrisToolsMIBGroup.setStatus('current')
colubrisToolsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 12, 3, 2, 2)).setObjects(("COLUBRIS-TOOLS-MIB", "traceStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisToolsNotificationGroup = colubrisToolsNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-TOOLS-MIB", traceNumberOfPackets=traceNumberOfPackets, traceCaptureFilter=traceCaptureFilter, colubrisToolsMIBCompliances=colubrisToolsMIBCompliances, traceCaptureDestination=traceCaptureDestination, colubrisToolsMIB=colubrisToolsMIB, traceNotificationEnabled=traceNotificationEnabled, traceStatusNotification=traceStatusNotification, colubrisToolsMIBNotificationPrefix=colubrisToolsMIBNotificationPrefix, traceInterface=traceInterface, colubrisToolsMIBCompliance=colubrisToolsMIBCompliance, traceTimeout=traceTimeout, colubrisToolsMIBObjects=colubrisToolsMIBObjects, tracePacketSize=tracePacketSize, colubrisToolsMIBConformance=colubrisToolsMIBConformance, colubrisToolsMIBGroups=colubrisToolsMIBGroups, traceCaptureStatus=traceCaptureStatus, traceCaptureDestinationURL=traceCaptureDestinationURL, PYSNMP_MODULE_ID=colubrisToolsMIB, colubrisToolsMIBNotifications=colubrisToolsMIBNotifications, traceToolConfig=traceToolConfig, colubrisToolsMIBGroup=colubrisToolsMIBGroup, colubrisToolsNotificationGroup=colubrisToolsNotificationGroup)
