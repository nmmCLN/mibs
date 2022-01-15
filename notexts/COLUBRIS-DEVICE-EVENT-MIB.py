#
# PySNMP MIB module COLUBRIS-DEVICE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-DEVICE-EVENT-MIB.my
# Produced by pysmi-1.1.8 at Sat Jan 15 20:23:07 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
coDevDisIndex, = mibBuilder.importSymbols("COLUBRIS-DEVICE-MIB", "coDevDisIndex")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, ColubrisSSIDOrNone = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable", "ColubrisSSIDOrNone")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, MibIdentifier, Counter64, Counter32, IpAddress, Gauge32, Unsigned32, NotificationType, Integer32, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Counter64", "Counter32", "IpAddress", "Gauge32", "Unsigned32", "NotificationType", "Integer32", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
colubrisDeviceEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 26))
if mibBuilder.loadTexts: colubrisDeviceEventMIB.setLastUpdated('200607050000Z')
if mibBuilder.loadTexts: colubrisDeviceEventMIB.setOrganization('Colubris Networks, Inc.')
colubrisDeviceEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1))
coDeviceEventConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1))
coDeviceEventInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2))
coDevEvSuccessfulAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 1), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulAssociationNotificationEnabled.setStatus('current')
coDevEvAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 2), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvAssociationFailureNotificationEnabled.setStatus('current')
coDevEvSuccessfulReAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 3), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulReAssociationNotificationEnabled.setStatus('current')
coDevEvReAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 4), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvReAssociationFailureNotificationEnabled.setStatus('current')
coDevEvSuccessfulAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 5), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulAuthenticationNotificationEnabled.setStatus('current')
coDevEvAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 6), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvAuthenticationFailureNotificationEnabled.setStatus('current')
coDevEvSuccessfulDisAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 7), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulDisAssociationNotificationEnabled.setStatus('current')
coDevEvDisAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 8), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvDisAssociationFailureNotificationEnabled.setStatus('current')
coDevEvSuccessfulDeAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 9), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvSuccessfulDeAuthenticationNotificationEnabled.setStatus('current')
coDevEvDeAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 1, 10), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDevEvDeAuthenticationFailureNotificationEnabled.setStatus('current')
coDeviceEventTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceEventTable.setStatus('current')
coDeviceEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-EVENT-MIB", "coDevEvIndex"))
if mibBuilder.loadTexts: coDeviceEventEntry.setStatus('current')
coDevEvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevEvIndex.setStatus('current')
coDevEvMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvMacAddress.setStatus('current')
coDeviceEventDetailTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2), )
if mibBuilder.loadTexts: coDeviceEventDetailTable.setStatus('current')
coDeviceEventDetailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-EVENT-MIB", "coDevEvIndex"), (0, "COLUBRIS-DEVICE-EVENT-MIB", "coDevEvLogIndex"))
if mibBuilder.loadTexts: coDeviceEventDetailEntry.setStatus('current')
coDevEvLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevEvLogIndex.setStatus('current')
coDevEvDetMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvDetMacAddress.setStatus('current')
coDevEvTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvTime.setStatus('current')
coDevEvSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 4), ColubrisSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvSSID.setStatus('current')
coDevEvRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvRadioIndex.setStatus('current')
coDevEvDuplicateCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvDuplicateCount.setStatus('current')
coDevEvCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("wireless", 1), ("ieee802dot1x", 2), ("wpa", 3), ("macAuthentication", 4), ("dhcpServer", 5), ("pptpL2tp", 6), ("ipSec", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvCategory.setStatus('current')
coDevEvOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("association", 1), ("authentication", 2), ("authorization", 3), ("encryption", 4), ("addressAllocation", 5), ("vpnAuthentication", 6), ("vpnAddressAllocation", 7), ("unknown", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvOperation.setStatus('current')
coDevEvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvStatus.setStatus('current')
coDevEvOptionalData = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 26, 1, 2, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevEvOptionalData.setStatus('current')
colubrisDeviceEventMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2))
colubrisDeviceEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0))
coDeviceEventSuccessfulAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 1)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulAssociation.setStatus('current')
coDeviceEventAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 2)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventAssociationFailure.setStatus('current')
coDeviceEventSuccessfulReAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 3)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulReAssociation.setStatus('current')
coDeviceEventReAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 4)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventReAssociationFailure.setStatus('current')
coDeviceEventSuccessfulAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 5)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulAuthentication.setStatus('current')
coDeviceEventAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 6)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventAuthenticationFailure.setStatus('current')
coDeviceEventSuccessfulDisAssociation = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 7)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulDisAssociation.setStatus('current')
coDeviceEventDisAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 8)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventDisAssociationFailure.setStatus('current')
coDeviceEventSuccessfulDeAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 9)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventSuccessfulDeAuthentication.setStatus('current')
coDeviceEventDeAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 26, 2, 0, 10)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if mibBuilder.loadTexts: coDeviceEventDeAuthenticationFailure.setStatus('current')
colubrisDeviceEventMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3))
colubrisDeviceEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 1))
colubrisDeviceEventMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 2))
colubrisDeviceEventMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 1, 1)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "colubrisDeviceEventConfigMIBGroup"), ("COLUBRIS-DEVICE-EVENT-MIB", "colubrisDeviceEventInfoMIBGroup"), ("COLUBRIS-DEVICE-EVENT-MIB", "colubrisDeviceEventNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceEventMIBCompliance = colubrisDeviceEventMIBCompliance.setStatus('current')
colubrisDeviceEventConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 2, 1)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulAssociationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvAssociationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulReAssociationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvReAssociationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulAuthenticationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvAuthenticationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulDisAssociationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvDisAssociationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSuccessfulDeAuthenticationNotificationEnabled"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvDeAuthenticationFailureNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceEventConfigMIBGroup = colubrisDeviceEventConfigMIBGroup.setStatus('current')
colubrisDeviceEventInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 2, 2)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvDetMacAddress"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvTime"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvSSID"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvRadioIndex"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvDuplicateCount"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvCategory"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOperation"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvStatus"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceEventInfoMIBGroup = colubrisDeviceEventInfoMIBGroup.setStatus('current')
colubrisDeviceEventNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 26, 3, 2, 3)).setObjects(("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAssociation"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventAssociationFailure"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulReAssociation"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventReAssociationFailure"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAuthentication"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventAuthenticationFailure"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDisAssociation"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventDisAssociationFailure"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDeAuthentication"), ("COLUBRIS-DEVICE-EVENT-MIB", "coDeviceEventDeAuthenticationFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceEventNotificationGroup = colubrisDeviceEventNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-EVENT-MIB", colubrisDeviceEventNotificationGroup=colubrisDeviceEventNotificationGroup, coDevEvSuccessfulReAssociationNotificationEnabled=coDevEvSuccessfulReAssociationNotificationEnabled, colubrisDeviceEventMIBCompliance=colubrisDeviceEventMIBCompliance, coDevEvMacAddress=coDevEvMacAddress, coDevEvDetMacAddress=coDevEvDetMacAddress, PYSNMP_MODULE_ID=colubrisDeviceEventMIB, coDevEvSuccessfulDisAssociationNotificationEnabled=coDevEvSuccessfulDisAssociationNotificationEnabled, coDevEvRadioIndex=coDevEvRadioIndex, coDevEvIndex=coDevEvIndex, colubrisDeviceEventMIBNotifications=colubrisDeviceEventMIBNotifications, colubrisDeviceEventMIBNotificationPrefix=colubrisDeviceEventMIBNotificationPrefix, colubrisDeviceEventMIBConformance=colubrisDeviceEventMIBConformance, coDeviceEventDetailTable=coDeviceEventDetailTable, coDeviceEventAuthenticationFailure=coDeviceEventAuthenticationFailure, coDeviceEventDetailEntry=coDeviceEventDetailEntry, coDevEvOperation=coDevEvOperation, coDeviceEventDisAssociationFailure=coDeviceEventDisAssociationFailure, coDevEvDuplicateCount=coDevEvDuplicateCount, coDevEvCategory=coDevEvCategory, coDevEvTime=coDevEvTime, coDeviceEventTable=coDeviceEventTable, coDevEvDeAuthenticationFailureNotificationEnabled=coDevEvDeAuthenticationFailureNotificationEnabled, coDeviceEventReAssociationFailure=coDeviceEventReAssociationFailure, coDeviceEventDeAuthenticationFailure=coDeviceEventDeAuthenticationFailure, coDevEvSSID=coDevEvSSID, coDeviceEventSuccessfulAssociation=coDeviceEventSuccessfulAssociation, coDevEvAuthenticationFailureNotificationEnabled=coDevEvAuthenticationFailureNotificationEnabled, coDeviceEventSuccessfulAuthentication=coDeviceEventSuccessfulAuthentication, colubrisDeviceEventMIB=colubrisDeviceEventMIB, colubrisDeviceEventMIBObjects=colubrisDeviceEventMIBObjects, coDeviceEventAssociationFailure=coDeviceEventAssociationFailure, coDeviceEventInfoGroup=coDeviceEventInfoGroup, coDeviceEventSuccessfulReAssociation=coDeviceEventSuccessfulReAssociation, colubrisDeviceEventMIBGroups=colubrisDeviceEventMIBGroups, coDevEvStatus=coDevEvStatus, coDevEvDisAssociationFailureNotificationEnabled=coDevEvDisAssociationFailureNotificationEnabled, colubrisDeviceEventMIBCompliances=colubrisDeviceEventMIBCompliances, coDevEvSuccessfulAuthenticationNotificationEnabled=coDevEvSuccessfulAuthenticationNotificationEnabled, coDevEvReAssociationFailureNotificationEnabled=coDevEvReAssociationFailureNotificationEnabled, coDevEvAssociationFailureNotificationEnabled=coDevEvAssociationFailureNotificationEnabled, coDeviceEventConfigGroup=coDeviceEventConfigGroup, coDevEvLogIndex=coDevEvLogIndex, coDevEvSuccessfulDeAuthenticationNotificationEnabled=coDevEvSuccessfulDeAuthenticationNotificationEnabled, coDevEvOptionalData=coDevEvOptionalData, colubrisDeviceEventConfigMIBGroup=colubrisDeviceEventConfigMIBGroup, colubrisDeviceEventInfoMIBGroup=colubrisDeviceEventInfoMIBGroup, coDeviceEventSuccessfulDisAssociation=coDeviceEventSuccessfulDisAssociation, coDevEvSuccessfulAssociationNotificationEnabled=coDevEvSuccessfulAssociationNotificationEnabled, coDeviceEventEntry=coDeviceEventEntry, coDeviceEventSuccessfulDeAuthentication=coDeviceEventSuccessfulDeAuthentication)
