#
# PySNMP MIB module OG-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-HOST-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:40 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, ModuleIdentity, Gauge32, Unsigned32, MibIdentifier, TimeTicks, Counter64, iso, Bits, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "TimeTicks", "Counter64", "iso", "Bits", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogHostMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 14))
ogHostMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ogHostMib.setRevisionsDescriptions(('Renamed from OPENGEAR-HOST-MIB to OG-HOST-MIB to\n\t\tfix naming discrepancy.', 'Syntax corrections by Opengear Inc.', 'Initial version.',))
if mibBuilder.loadTexts: ogHostMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogHostMib.setOrganization('Opengear Inc.')
if mibBuilder.loadTexts: ogHostMib.setContactInfo('Opengear Inc.\n\t\t630 West 9560 South,\n\t\t Sandy, UT 84070\n\t\t support@opengear.com')
if mibBuilder.loadTexts: ogHostMib.setDescription('Opengear host connection MIB')
ogHostMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10))
oghostEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1))
oghostEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1), )
if mibBuilder.loadTexts: oghostEventTable.setStatus('current')
if mibBuilder.loadTexts: oghostEventTable.setDescription('A table of sensor status events generated by this device.')
oghostEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1), ).setIndexNames((0, "OG-HOST-MIB", "oghostEventIndex"))
if mibBuilder.loadTexts: oghostEventEntry.setStatus('current')
if mibBuilder.loadTexts: oghostEventEntry.setDescription('A console connection event occuring at this\n                 device. Each entry is indexed by a message index.')
oghostEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: oghostEventIndex.setStatus('current')
if mibBuilder.loadTexts: oghostEventIndex.setDescription('A monotonically increasing integer for the sole\n                 purpose of indexing messages.  When it reaches the\n                 maximum value the agent flushes the table and wraps\n                 the value back to 1.')
oghostEventUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventUsername.setStatus('current')
if mibBuilder.loadTexts: oghostEventUsername.setDescription('The user pertaining to the connection event')
oghostEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventType.setStatus('current')
if mibBuilder.loadTexts: oghostEventType.setDescription('The type of connection event')
oghostEventAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventAddress.setStatus('current')
if mibBuilder.loadTexts: oghostEventAddress.setDescription('The address of the host to which this connection applies.')
oghostEventDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventDescription.setStatus('current')
if mibBuilder.loadTexts: oghostEventDescription.setDescription('The description of the host to which this connection applies.')
oghostEventProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventProtocol.setStatus('current')
if mibBuilder.loadTexts: oghostEventProtocol.setDescription('The internet protocl to which this connection applies.')
oghostEventPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 14, 10, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oghostEventPort.setStatus('current')
if mibBuilder.loadTexts: oghostEventPort.setDescription('The applicable port number of the host.')
ogHostMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2))
oghostMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2, 0))
oghostEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 14, 2, 0, 200)).setObjects(("OG-HOST-MIB", "oghostEventUsername"), ("OG-HOST-MIB", "oghostEventType"), ("OG-HOST-MIB", "oghostEventAddress"), ("OG-HOST-MIB", "oghostEventDescription"), ("OG-HOST-MIB", "oghostEventProtocol"), ("OG-HOST-MIB", "oghostEventPort"))
if mibBuilder.loadTexts: oghostEventOccurred.setStatus('current')
if mibBuilder.loadTexts: oghostEventOccurred.setDescription('The notification sent when a user connection event occurs')
ogHostMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3))
ogHostMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 1))
ogHostMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2))
ogHostMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 1, 1)).setObjects(("OG-HOST-MIB", "ogHostMibGroup"), ("OG-HOST-MIB", "oghostNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogHostMibCompliance = ogHostMibCompliance.setStatus('current')
if mibBuilder.loadTexts: ogHostMibCompliance.setDescription('The compliance statement for entities which implement\n                the Opengear Host MIB.')
ogHostMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2, 1)).setObjects(("OG-HOST-MIB", "oghostEventUsername"), ("OG-HOST-MIB", "oghostEventType"), ("OG-HOST-MIB", "oghostEventAddress"), ("OG-HOST-MIB", "oghostEventDescription"), ("OG-HOST-MIB", "oghostEventProtocol"), ("OG-HOST-MIB", "oghostEventPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogHostMibGroup = ogHostMibGroup.setStatus('current')
if mibBuilder.loadTexts: ogHostMibGroup.setDescription('A collection of objects providing the sensor MIB capability.')
oghostNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 14, 3, 2, 2)).setObjects(("OG-HOST-MIB", "oghostEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oghostNotificationsGroup = oghostNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: oghostNotificationsGroup.setDescription('A collection of notification(s) for sensor system.')
mibBuilder.exportSymbols("OG-HOST-MIB", ogHostMibGroup=ogHostMibGroup, oghostEvent=oghostEvent, oghostMibNotifications=oghostMibNotifications, oghostEventTable=oghostEventTable, oghostEventEntry=oghostEventEntry, oghostEventAddress=oghostEventAddress, ogHostMibGroups=ogHostMibGroups, oghostEventProtocol=oghostEventProtocol, ogHostMibConformance=ogHostMibConformance, oghostEventPort=oghostEventPort, oghostEventOccurred=oghostEventOccurred, PYSNMP_MODULE_ID=ogHostMib, ogHostMibObjects=ogHostMibObjects, oghostEventDescription=oghostEventDescription, oghostNotificationsGroup=oghostNotificationsGroup, ogHostMibNotificationPrefix=ogHostMibNotificationPrefix, oghostEventType=oghostEventType, ogHostMibCompliances=ogHostMibCompliances, oghostEventUsername=oghostEventUsername, ogHostMibCompliance=ogHostMibCompliance, ogHostMib=ogHostMib, oghostEventIndex=oghostEventIndex)
