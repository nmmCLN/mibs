#
# PySNMP MIB module PACKETLOGIC-RAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-RAID-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:22:33 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, ObjectIdentity, Integer32, IpAddress, Counter64, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "Integer32", "IpAddress", "Counter64", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Bits", "TimeTicks", "Gauge32")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
raid = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1))
raid.setRevisions(('2019-09-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: raid.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: raid.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: raid.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: raid.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: raid.setDescription('MIB for PacketLogic2 RAID devices')
raidCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1))
ld = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3), )
if mibBuilder.loadTexts: ld.setStatus('current')
if mibBuilder.loadTexts: ld.setDescription('Conceptual Table')
ldEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1), ).setIndexNames((0, "PACKETLOGIC-RAID-MIB", "ldEntryIndex"))
if mibBuilder.loadTexts: ldEntry.setStatus('current')
if mibBuilder.loadTexts: ldEntry.setDescription('Conceptual Table')
ldEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ldEntryIndex.setStatus('current')
if mibBuilder.loadTexts: ldEntryIndex.setDescription('Unique Row Index for Conceptual Table')
disk = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4), )
if mibBuilder.loadTexts: disk.setStatus('current')
if mibBuilder.loadTexts: disk.setDescription('Conceptual Table')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1), ).setIndexNames((0, "PACKETLOGIC-RAID-MIB", "diskEntryIndex"))
if mibBuilder.loadTexts: diskEntry.setStatus('current')
if mibBuilder.loadTexts: diskEntry.setDescription('Conceptual Table')
diskEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: diskEntryIndex.setStatus('current')
if mibBuilder.loadTexts: diskEntryIndex.setDescription('Unique Row Index for Conceptual Table')
adpNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpNumber.setStatus('current')
if mibBuilder.loadTexts: adpNumber.setDescription('Number of available adapters in system')
ldNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldNumber.setStatus('current')
if mibBuilder.loadTexts: ldNumber.setDescription('Number of available logical devices in system')
diskNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskNumber.setStatus('current')
if mibBuilder.loadTexts: diskNumber.setDescription('Number of available disks in system')
ldId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldId.setStatus('current')
if mibBuilder.loadTexts: ldId.setDescription('LD Index')
ldState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldState.setStatus('current')
if mibBuilder.loadTexts: ldState.setDescription('LD State')
diskId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskId.setStatus('current')
if mibBuilder.loadTexts: diskId.setDescription('Disk Index')
diskState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskState.setStatus('current')
if mibBuilder.loadTexts: diskState.setDescription('Disk State')
diskLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskLabel.setStatus('current')
if mibBuilder.loadTexts: diskLabel.setDescription('Disk Label')
mibBuilder.exportSymbols("PACKETLOGIC-RAID-MIB", diskId=diskId, diskNumber=diskNumber, diskLabel=diskLabel, raidCfg=raidCfg, diskEntryIndex=diskEntryIndex, ld=ld, PYSNMP_MODULE_ID=raid, disk=disk, diskEntry=diskEntry, ldId=ldId, raid=raid, ldEntryIndex=ldEntryIndex, adpNumber=adpNumber, ldEntry=ldEntry, ldNumber=ldNumber, diskState=diskState, ldState=ldState)
