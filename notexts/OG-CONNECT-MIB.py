#
# PySNMP MIB module OG-CONNECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-CONNECT-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 16:47:20 2022
# On host fv-az119-924 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, MibIdentifier, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Unsigned32, NotificationType, ModuleIdentity, Counter64, Bits, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Unsigned32", "NotificationType", "ModuleIdentity", "Counter64", "Bits", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ogConnectMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 10))
ogConnectMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogConnectMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogConnectMib.setOrganization('Opengear Inc.')
ogConnectMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10))
ogconnEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1))
ogconnEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1), )
if mibBuilder.loadTexts: ogconnEventTable.setStatus('current')
ogconnEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1), ).setIndexNames((0, "OG-CONNECT-MIB", "ogconnEventIndex"))
if mibBuilder.loadTexts: ogconnEventEntry.setStatus('current')
ogconnEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogconnEventIndex.setStatus('current')
ogconnEventUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventUsername.setStatus('current')
ogconnEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventType.setStatus('current')
ogconnEventPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventPortNumber.setStatus('current')
ogconnEventPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 10, 10, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogconnEventPortLabel.setStatus('current')
ogConnectMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 2))
ogconnMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 2, 0))
ogconnEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 10, 2, 0, 200)).setObjects(("OG-CONNECT-MIB", "ogconnEventUsername"), ("OG-CONNECT-MIB", "ogconnEventType"), ("OG-CONNECT-MIB", "ogconnEventPortNumber"), ("OG-CONNECT-MIB", "ogconnEventPortLabel"))
if mibBuilder.loadTexts: ogconnEventOccurred.setStatus('current')
ogConnectMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3))
ogConnectMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 1))
ogConnectMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2))
ogConnectMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 1, 1)).setObjects(("OG-CONNECT-MIB", "ogConnectMibGroup"), ("OG-CONNECT-MIB", "ogconnNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogConnectMibCompliance = ogConnectMibCompliance.setStatus('current')
ogConnectMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2, 1)).setObjects(("OG-CONNECT-MIB", "ogconnEventUsername"), ("OG-CONNECT-MIB", "ogconnEventType"), ("OG-CONNECT-MIB", "ogconnEventPortNumber"), ("OG-CONNECT-MIB", "ogconnEventPortLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogConnectMibGroup = ogConnectMibGroup.setStatus('current')
ogconnNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 10, 3, 2, 2)).setObjects(("OG-CONNECT-MIB", "ogconnEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogconnNotificationsGroup = ogconnNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-CONNECT-MIB", ogconnEventType=ogconnEventType, ogconnMibNotifications=ogconnMibNotifications, ogConnectMibNotificationPrefix=ogConnectMibNotificationPrefix, ogConnectMibCompliance=ogConnectMibCompliance, ogConnectMib=ogConnectMib, ogconnEventTable=ogconnEventTable, ogConnectMibConformance=ogConnectMibConformance, ogconnEventIndex=ogconnEventIndex, ogConnectMibGroups=ogConnectMibGroups, ogconnEventOccurred=ogconnEventOccurred, ogconnEventPortNumber=ogconnEventPortNumber, ogconnEventEntry=ogconnEventEntry, ogConnectMibGroup=ogConnectMibGroup, ogconnEventUsername=ogconnEventUsername, ogconnEvent=ogconnEvent, ogconnEventPortLabel=ogconnEventPortLabel, ogConnectMibCompliances=ogConnectMibCompliances, ogConnectMibObjects=ogConnectMibObjects, ogconnNotificationsGroup=ogconnNotificationsGroup, PYSNMP_MODULE_ID=ogConnectMib)
