#
# PySNMP MIB module SYNOLOGY-RAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-RAID-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 08:38:05 2022
# On host fv-az278-268 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, Integer32, TimeTicks, Unsigned32, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, Counter32, MibIdentifier, Counter64, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "Integer32", "TimeTicks", "Unsigned32", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "Counter32", "MibIdentifier", "Counter64", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
synoRaid = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 3))
synoRaid.setRevisions(('2013-09-11 00:00',))
if mibBuilder.loadTexts: synoRaid.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoRaid.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
raidTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 3, 1), )
if mibBuilder.loadTexts: raidTable.setStatus('current')
raidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1), ).setIndexNames((0, "SYNOLOGY-RAID-MIB", "raidIndex"))
if mibBuilder.loadTexts: raidEntry.setStatus('current')
raidIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: raidIndex.setStatus('current')
raidName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidName.setStatus('current')
raidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidStatus.setStatus('current')
raidFreeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidFreeSize.setStatus('current')
raidTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidTotalSize.setStatus('current')
raidConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2))
raidCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2, 1))
raidGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2, 2))
raidCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 3, 2, 1, 1)).setObjects(("SYNOLOGY-RAID-MIB", "raidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidCompliance = raidCompliance.setStatus('current')
raidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 3, 2, 2, 1)).setObjects(("SYNOLOGY-RAID-MIB", "raidName"), ("SYNOLOGY-RAID-MIB", "raidStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidGroup = raidGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-RAID-MIB", raidConformance=raidConformance, raidIndex=raidIndex, raidGroup=raidGroup, synology=synology, raidTotalSize=raidTotalSize, raidStatus=raidStatus, raidFreeSize=raidFreeSize, raidEntry=raidEntry, raidCompliance=raidCompliance, raidCompliances=raidCompliances, raidName=raidName, raidTable=raidTable, synoRaid=synoRaid, PYSNMP_MODULE_ID=synoRaid, raidGroups=raidGroups)
