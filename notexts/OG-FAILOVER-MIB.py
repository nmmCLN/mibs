#
# PySNMP MIB module OG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-FAILOVER-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:39:46 2022
# On host fv-az128-12 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ogMgmt, = mibBuilder.importSymbols("OG-SMI-MIB", "ogMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, IpAddress, ObjectIdentity, ModuleIdentity, Unsigned32, Counter32, MibIdentifier, Bits, Integer32, Counter64, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Counter32", "MibIdentifier", "Bits", "Integer32", "Counter64", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ogFailoverMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049, 10, 15))
ogFailoverMib.setRevisions(('2013-08-11 00:00', '2010-03-22 11:27', '2008-11-27 11:40',))
if mibBuilder.loadTexts: ogFailoverMib.setLastUpdated('201308110000Z')
if mibBuilder.loadTexts: ogFailoverMib.setOrganization('Opengear Inc.')
ogFailoverMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10))
ogfovrEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1))
ogfovrEventTable = MibTable((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1), )
if mibBuilder.loadTexts: ogfovrEventTable.setStatus('current')
ogfovrEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1), ).setIndexNames((0, "OG-FAILOVER-MIB", "ogfovrEventIndex"))
if mibBuilder.loadTexts: ogfovrEventEntry.setStatus('current')
ogfovrEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ogfovrEventIndex.setStatus('current')
ogfovrEventPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventPrimary.setStatus('current')
ogfovrEventSecondary = MibTableColumn((1, 3, 6, 1, 4, 1, 25049, 10, 15, 10, 1, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ogfovrEventSecondary.setStatus('current')
ogFailoverMibNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2))
ogfovrMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2, 0))
ogfovrEventOccurred = NotificationType((1, 3, 6, 1, 4, 1, 25049, 10, 15, 2, 0, 200)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventPrimary"), ("OG-FAILOVER-MIB", "ogfovrEventSecondary"))
if mibBuilder.loadTexts: ogfovrEventOccurred.setStatus('current')
ogFailoverMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3))
ogFailoverMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 1))
ogFailoverMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2))
ogFailoverMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 1, 1)).setObjects(("OG-FAILOVER-MIB", "ogFailoverMibGroup"), ("OG-FAILOVER-MIB", "ogfovrNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogFailoverMibCompliance = ogFailoverMibCompliance.setStatus('current')
ogFailoverMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2, 1)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventPrimary"), ("OG-FAILOVER-MIB", "ogfovrEventSecondary"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogFailoverMibGroup = ogFailoverMibGroup.setStatus('current')
ogfovrNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 25049, 10, 15, 3, 2, 2)).setObjects(("OG-FAILOVER-MIB", "ogfovrEventOccurred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ogfovrNotificationsGroup = ogfovrNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("OG-FAILOVER-MIB", ogfovrEvent=ogfovrEvent, ogFailoverMibCompliance=ogFailoverMibCompliance, ogFailoverMibGroup=ogFailoverMibGroup, ogfovrMibNotifications=ogfovrMibNotifications, ogfovrNotificationsGroup=ogfovrNotificationsGroup, ogFailoverMibObjects=ogFailoverMibObjects, ogFailoverMibCompliances=ogFailoverMibCompliances, ogFailoverMibGroups=ogFailoverMibGroups, ogfovrEventEntry=ogfovrEventEntry, ogFailoverMibNotificationPrefix=ogFailoverMibNotificationPrefix, ogfovrEventIndex=ogfovrEventIndex, ogFailoverMibConformance=ogFailoverMibConformance, ogfovrEventSecondary=ogfovrEventSecondary, ogfovrEventTable=ogfovrEventTable, PYSNMP_MODULE_ID=ogFailoverMib, ogfovrEventOccurred=ogfovrEventOccurred, ogfovrEventPrimary=ogfovrEventPrimary, ogFailoverMib=ogFailoverMib)
