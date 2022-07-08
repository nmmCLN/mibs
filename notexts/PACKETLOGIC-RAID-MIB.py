#
# PySNMP MIB module PACKETLOGIC-RAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-RAID-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:26:43 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, iso, NotificationType, Counter32, Unsigned32, Integer32, Bits, Gauge32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "iso", "NotificationType", "Counter32", "Unsigned32", "Integer32", "Bits", "Gauge32", "Counter64", "MibIdentifier")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
raid = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1))
raid.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: raid.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: raid.setOrganization('Procera Networks, Inc.')
raidCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1))
ld = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3), )
if mibBuilder.loadTexts: ld.setStatus('current')
ldEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1), ).setIndexNames((0, "PACKETLOGIC-RAID-MIB", "ldEntryIndex"))
if mibBuilder.loadTexts: ldEntry.setStatus('current')
ldEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ldEntryIndex.setStatus('current')
disk = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4), )
if mibBuilder.loadTexts: disk.setStatus('current')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1), ).setIndexNames((0, "PACKETLOGIC-RAID-MIB", "diskEntryIndex"))
if mibBuilder.loadTexts: diskEntry.setStatus('current')
diskEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: diskEntryIndex.setStatus('current')
adpNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adpNumber.setStatus('current')
ldNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldNumber.setStatus('current')
diskNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskNumber.setStatus('current')
ldId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldId.setStatus('current')
ldState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ldState.setStatus('current')
diskId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskId.setStatus('current')
diskState = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskState.setStatus('current')
diskLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskLabel.setStatus('current')
mibBuilder.exportSymbols("PACKETLOGIC-RAID-MIB", raidCfg=raidCfg, ld=ld, adpNumber=adpNumber, ldId=ldId, disk=disk, diskNumber=diskNumber, diskEntry=diskEntry, PYSNMP_MODULE_ID=raid, ldEntryIndex=ldEntryIndex, ldEntry=ldEntry, raid=raid, diskId=diskId, diskState=diskState, diskLabel=diskLabel, ldNumber=ldNumber, diskEntryIndex=diskEntryIndex, ldState=ldState)
