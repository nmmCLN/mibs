#
# PySNMP MIB module ARISTA-NEXTHOP-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-NEXTHOP-GROUP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:20 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, Integer32, NotificationType, Counter32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, IpAddress, Unsigned32, ModuleIdentity, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "NotificationType", "Counter32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "IpAddress", "Unsigned32", "ModuleIdentity", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaNexthopGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 21))
aristaNexthopGroupMIB.setRevisions(('2016-04-17 00:00',))
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setLastUpdated('201604170000Z')
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setOrganization('Arista Networks, Inc.')
aristaNexthopGroupMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1))
aristaNexthopGroupMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2))
class NexthopGroupName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class NexthopGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("invalid", 0), ("ipInIp", 1), ("gre", 2), ("mpls", 3), ("ip", 4), ("mplsOverGre", 5))

aristaNexthopGroupTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1), )
if mibBuilder.loadTexts: aristaNexthopGroupTable.setStatus('current')
aristaNexthopGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1), ).setIndexNames((0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"))
if mibBuilder.loadTexts: aristaNexthopGroupEntry.setStatus('current')
aristaNexthopGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaNexthopGroupId.setStatus('current')
aristaNexthopGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 2), NexthopGroupName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupName.setStatus('current')
aristaNexthopGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 3), NexthopGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupType.setStatus('current')
aristaNexthopGroupCounterTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2), )
if mibBuilder.loadTexts: aristaNexthopGroupCounterTable.setStatus('current')
aristaNexthopGroupCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1), ).setIndexNames((0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"), (0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupEntryIndex"))
if mibBuilder.loadTexts: aristaNexthopGroupCounterEntry.setStatus('current')
aristaNexthopGroupEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaNexthopGroupEntryIndex.setStatus('current')
aristaNexthopGroupCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterIndex.setStatus('current')
aristaNexthopGroupCounterPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterPacketCount.setStatus('current')
aristaNexthopGroupCounterByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterByteCount.setStatus('current')
aristaNexthopGroupMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1))
aristaNexthopGroupMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2))
aristaNexthopGroupMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1, 1)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupGroup"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupMibCompliance = aristaNexthopGroupMibCompliance.setStatus('current')
aristaNexthopGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 1)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupName"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupGroup = aristaNexthopGroupGroup.setStatus('current')
aristaNexthopGroupCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 2)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterIndex"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterPacketCount"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterByteCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupCounterGroup = aristaNexthopGroupCounterGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-NEXTHOP-GROUP-MIB", PYSNMP_MODULE_ID=aristaNexthopGroupMIB, aristaNexthopGroupMibCompliance=aristaNexthopGroupMibCompliance, aristaNexthopGroupId=aristaNexthopGroupId, NexthopGroupName=NexthopGroupName, aristaNexthopGroupTable=aristaNexthopGroupTable, aristaNexthopGroupCounterGroup=aristaNexthopGroupCounterGroup, aristaNexthopGroupCounterByteCount=aristaNexthopGroupCounterByteCount, aristaNexthopGroupEntry=aristaNexthopGroupEntry, aristaNexthopGroupMibObjects=aristaNexthopGroupMibObjects, aristaNexthopGroupMibConformance=aristaNexthopGroupMibConformance, aristaNexthopGroupCounterPacketCount=aristaNexthopGroupCounterPacketCount, aristaNexthopGroupName=aristaNexthopGroupName, aristaNexthopGroupEntryIndex=aristaNexthopGroupEntryIndex, aristaNexthopGroupMibCompliances=aristaNexthopGroupMibCompliances, aristaNexthopGroupMIB=aristaNexthopGroupMIB, aristaNexthopGroupType=aristaNexthopGroupType, aristaNexthopGroupCounterEntry=aristaNexthopGroupCounterEntry, NexthopGroupType=NexthopGroupType, aristaNexthopGroupCounterTable=aristaNexthopGroupCounterTable, aristaNexthopGroupCounterIndex=aristaNexthopGroupCounterIndex, aristaNexthopGroupGroup=aristaNexthopGroupGroup, aristaNexthopGroupMibGroups=aristaNexthopGroupMibGroups)
