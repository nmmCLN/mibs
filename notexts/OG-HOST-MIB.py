#
# PySNMP MIB module OG-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-HOST-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:38 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ModuleIdentity, TimeTicks, Counter64, MibIdentifier, Counter32, ObjectIdentity, iso, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter64", "MibIdentifier", "Counter32", "ObjectIdentity", "iso", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogHostMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 14))
ogHostMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogHostMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogHostMib.setOrganization('Opengear Inc.')
ogHostMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10))
oghostEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1))
oghostEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1), )
if mibBuilder.loadTexts: oghostEventTable.setStatus('current')
oghostEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1), ).setIndexNames((0, "OG-HOST-MIB", "oghostEventIndex"))
if mibBuilder.loadTexts: oghostEventEntry.setStatus('current')
oghostEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: oghostEventIndex.setStatus('current')
oghostEventUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventUsername.setStatus('current')
oghostEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventType.setStatus('current')
oghostEventAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventAddress.setStatus('current')
oghostEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventDescription.setStatus('current')
oghostEventProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventProtocol.setStatus('current')
oghostEventPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventPort.setStatus('current')
ogHostMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2))
oghostMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2, 0))
oghostEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2, 0, 200)).setObjects(("OG-HOST-MIB", "oghostEventUsername"), ("OG-HOST-MIB", "oghostEventType"), ("OG-HOST-MIB", "oghostEventAddress"), ("OG-HOST-MIB", "oghostEventDescription"), ("OG-HOST-MIB", "oghostEventProtocol"), ("OG-HOST-MIB", "oghostEventPort"))
if mibBuilder.loadTexts: oghostEventOccurred.setStatus('current')
ogHostMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3))
ogHostMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 1))
ogHostMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2))
ogHostMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 1, 1)).setObjects(("OG-HOST-MIB", "ogHostMibGroup"), ("OG-HOST-MIB", "oghostNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogHostMibCompliance = ogHostMibCompliance.setStatus('current')
ogHostMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2, 1)).setObjects(("OG-HOST-MIB", "oghostEventUsername"), ("OG-HOST-MIB", "oghostEventType"), ("OG-HOST-MIB", "oghostEventAddress"), ("OG-HOST-MIB", "oghostEventDescription"), ("OG-HOST-MIB", "oghostEventProtocol"), ("OG-HOST-MIB", "oghostEventPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogHostMibGroup = ogHostMibGroup.setStatus('current')
oghostNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2, 2)).setObjects(("OG-HOST-MIB", "oghostEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oghostNotificationsGroup = oghostNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-HOST-MIB", oghostEventPort=oghostEventPort, PYSNMP_MODULE_ID=ogHostMib, ogHostMibCompliances=ogHostMibCompliances, oghostNotificationsGroup=oghostNotificationsGroup, oghostEventTable=oghostEventTable, oghostEventUsername=oghostEventUsername, oghostMibNotifications=oghostMibNotifications, oghostEventIndex=oghostEventIndex, ogHostMibGroups=ogHostMibGroups, oghostEventAddress=oghostEventAddress, oghostEventOccurred=oghostEventOccurred, ogHostMib=ogHostMib, oghostEventType=oghostEventType, oghostEventDescription=oghostEventDescription, oghostEventEntry=oghostEventEntry, oghostEvent=oghostEvent, ogHostMibObjects=ogHostMibObjects, ogHostMibConformance=ogHostMibConformance, ogHostMibGroup=ogHostMibGroup, ogHostMibCompliance=ogHostMibCompliance, ogHostMibNotificationPrefix=ogHostMibNotificationPrefix, oghostEventProtocol=oghostEventProtocol)
