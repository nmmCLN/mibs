#
# PySNMP MIB module WAYSTREAM-IGMP-CACHE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-IGMP-CACHE-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:38:46 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, NotificationType, Bits, Gauge32, iso, TimeTicks, Unsigned32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "NotificationType", "Bits", "Gauge32", "iso", "TimeTicks", "Unsigned32", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wsMgmt, = mibBuilder.importSymbols("WAYSTREAM-SMI", "wsMgmt")
wsIgmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 4, 13))
wsIgmp.setRevisions(('2017-02-10 11:00', '2011-01-11 17:54', '2009-04-29 13:49', '2009-03-23 11:25', '2008-04-30 13:48', '2007-06-13 14:37',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wsIgmp.setRevisionsDescriptions(('Company name change:\n\t In October 2015 PacketFront Network Products was renamed Waystream.\n\t In this update all PacketFront were changed to Waystream and all\n\t pf* to ws*.', 'Updated company name', 'Moved pfIgmp from pfExperimental.3 to pfMgmt.13', 'Updated telephone information in contact-info', 'Move from PACKETFRONT-MIB', 'Initial implementation of pfIgmp',))
if mibBuilder.loadTexts: wsIgmp.setLastUpdated('201702101100Z')
if mibBuilder.loadTexts: wsIgmp.setOrganization('Waystream AB')
if mibBuilder.loadTexts: wsIgmp.setContactInfo('Waystream AB\n         Customer Service\n\n         Mail : Farogatan 33\n                SE-164 51 Kista\n                Sweden\n\n         Tel  : +46 8 5626 9450\n\n         E-mail: info@waystream.com\n         Web   : http://www.waystream.com')
if mibBuilder.loadTexts: wsIgmp.setDescription('Waystream MIB describing IGMP caching and snooping functions of\n         ASRs')
wsIgmpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2), )
if mibBuilder.loadTexts: wsIgmpCacheTable.setStatus('current')
if mibBuilder.loadTexts: wsIgmpCacheTable.setDescription('The table listing all snooped members of IP multicast groups\n\tthat are connected through downstream0-mapped interfaces.')
wsIgmpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1), ).setIndexNames((0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheAddress"), (0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheIfIndex"), (0, "WAYSTREAM-IGMP-CACHE-MIB", "wsIgmpCacheReporter"))
if mibBuilder.loadTexts: wsIgmpCacheEntry.setStatus('current')
if mibBuilder.loadTexts: wsIgmpCacheEntry.setDescription('An entry in the wsIgmpCacheTable.')
wsIgmpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: wsIgmpCacheAddress.setStatus('current')
if mibBuilder.loadTexts: wsIgmpCacheAddress.setDescription('The IP multicast group for which this entry\n\tcontains information.')
wsIgmpCacheIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: wsIgmpCacheIfIndex.setStatus('current')
if mibBuilder.loadTexts: wsIgmpCacheIfIndex.setDescription('The interface for which this entry contains\n\tinformation for\tan IP multicast group.')
wsIgmpCacheReporter = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 3), IpAddress())
if mibBuilder.loadTexts: wsIgmpCacheReporter.setStatus('current')
if mibBuilder.loadTexts: wsIgmpCacheReporter.setDescription('The reporter for which this entry contains\n\tinformation for an IP multicast group.')
wsIgmpCacheUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9303, 4, 13, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsIgmpCacheUpTime.setStatus('current')
if mibBuilder.loadTexts: wsIgmpCacheUpTime.setDescription('Time elapsed since this entry was created.')
mibBuilder.exportSymbols("WAYSTREAM-IGMP-CACHE-MIB", wsIgmpCacheIfIndex=wsIgmpCacheIfIndex, wsIgmp=wsIgmp, wsIgmpCacheReporter=wsIgmpCacheReporter, wsIgmpCacheUpTime=wsIgmpCacheUpTime, wsIgmpCacheEntry=wsIgmpCacheEntry, wsIgmpCacheTable=wsIgmpCacheTable, wsIgmpCacheAddress=wsIgmpCacheAddress, PYSNMP_MODULE_ID=wsIgmp)
