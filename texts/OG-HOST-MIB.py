#
# PySNMP MIB module OG-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-HOST-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:25 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, NotificationType, TimeTicks, Bits, iso, Gauge32, ObjectIdentity, MibIdentifier, Counter32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "NotificationType", "TimeTicks", "Bits", "iso", "Gauge32", "ObjectIdentity", "MibIdentifier", "Counter32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("OG-HOST-MIB", ogHostMibObjects=ogHostMibObjects, oghostEvent=oghostEvent, ogHostMibCompliances=ogHostMibCompliances, oghostEventType=oghostEventType, ogHostMibCompliance=ogHostMibCompliance, oghostMibNotifications=oghostMibNotifications, oghostEventAddress=oghostEventAddress, ogHostMibNotificationPrefix=ogHostMibNotificationPrefix, oghostEventTable=oghostEventTable, oghostEventOccurred=oghostEventOccurred, oghostEventIndex=oghostEventIndex, oghostNotificationsGroup=oghostNotificationsGroup, ogHostMibConformance=ogHostMibConformance, ogHostMibGroups=ogHostMibGroups, ogHostMib=ogHostMib, oghostEventPort=oghostEventPort, oghostEventDescription=oghostEventDescription, oghostEventUsername=oghostEventUsername, oghostEventEntry=oghostEventEntry, ogHostMibGroup=ogHostMibGroup, PYSNMP_MODULE_ID=ogHostMib, oghostEventProtocol=oghostEventProtocol)
