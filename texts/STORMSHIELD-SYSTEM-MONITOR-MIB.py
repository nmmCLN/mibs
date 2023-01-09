#
# PySNMP MIB module STORMSHIELD-SYSTEM-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SYSTEM-MONITOR-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:37:53 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Integer32, ModuleIdentity, Bits, MibIdentifier, NotificationType, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Integer32", "ModuleIdentity", "Bits", "MibIdentifier", "NotificationType", "TimeTicks", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsSystemMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 10))
snsSystemMonitor.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsSystemMonitor.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsSystemMonitor.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsSystemMonitor.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsSystemMonitor.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsSystemMonitor.setDescription('stormshield System Monitor')
snsDate = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDate.setStatus('current')
if mibBuilder.loadTexts: snsDate.setDescription('Stormshield Firewall current date (%Y-%m-%d %T)')
snsUptime = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 10, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsUptime.setStatus('current')
if mibBuilder.loadTexts: snsUptime.setDescription('Stormshield Firewal system running for day:hour:min:sec')
snsMem = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 10, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsMem.setStatus('current')
if mibBuilder.loadTexts: snsMem.setDescription('Stormshield Firewall memory left for in percent\n                  (host,frag,icmp,conn,dtrack,dyn)')
snsStatTime = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 10, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsStatTime.setStatus('current')
if mibBuilder.loadTexts: snsStatTime.setDescription('Stormshield Firewall last stat time (%Y-%m-%d %T)')
snsDiskTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5), )
if mibBuilder.loadTexts: snsDiskTable.setStatus('current')
if mibBuilder.loadTexts: snsDiskTable.setDescription('Disk information')
snsDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1), ).setIndexNames((0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsDiskEntryIndex"))
if mibBuilder.loadTexts: snsDiskEntry.setStatus('current')
if mibBuilder.loadTexts: snsDiskEntry.setDescription('Disk information')
snsDiskEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryIndex.setStatus('current')
if mibBuilder.loadTexts: snsDiskEntryIndex.setDescription('Index of each disk in table')
snsDiskEntryDiskName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryDiskName.setStatus('current')
if mibBuilder.loadTexts: snsDiskEntryDiskName.setDescription('Name of the disk')
snsDiskEntrySmartResult = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntrySmartResult.setStatus('current')
if mibBuilder.loadTexts: snsDiskEntrySmartResult.setDescription('Result of the smart infos tests')
snsDiskEntryIsRaid = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryIsRaid.setStatus('current')
if mibBuilder.loadTexts: snsDiskEntryIsRaid.setDescription('Is the disk a member of a RAID array')
snsDiskEntryRaidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryRaidStatus.setStatus('current')
if mibBuilder.loadTexts: snsDiskEntryRaidStatus.setDescription('RAID Status')
snsDiskEntryPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryPosition.setStatus('current')
if mibBuilder.loadTexts: snsDiskEntryPosition.setDescription('Disk Position')
snsPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 10, 6), )
if mibBuilder.loadTexts: snsPowerSupplyTable.setStatus('current')
if mibBuilder.loadTexts: snsPowerSupplyTable.setDescription('Power supply status of Firewall')
snsPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1), ).setIndexNames((0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsPowerSupplyIndex"))
if mibBuilder.loadTexts: snsPowerSupplyEntry.setStatus('current')
if mibBuilder.loadTexts: snsPowerSupplyEntry.setDescription('Power supply information')
snsPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsPowerSupplyIndex.setStatus('current')
if mibBuilder.loadTexts: snsPowerSupplyIndex.setDescription('Index of each line in table')
snsPowerSupplyPowered = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsPowerSupplyPowered.setStatus('current')
if mibBuilder.loadTexts: snsPowerSupplyPowered.setDescription('Is power supply powered by electricity ?')
snsCpuTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 10, 7), )
if mibBuilder.loadTexts: snsCpuTable.setStatus('current')
if mibBuilder.loadTexts: snsCpuTable.setDescription('CPU status of Firewalls')
snsCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1), ).setIndexNames((0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsCpuIndex"))
if mibBuilder.loadTexts: snsCpuEntry.setStatus('current')
if mibBuilder.loadTexts: snsCpuEntry.setDescription('CPU information')
snsCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsCpuIndex.setStatus('current')
if mibBuilder.loadTexts: snsCpuIndex.setDescription('Index of each CPU in table')
snsCpuTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsCpuTemp.setStatus('current')
if mibBuilder.loadTexts: snsCpuTemp.setDescription('Temperature in Celsius degree')
snsBypassTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8), )
if mibBuilder.loadTexts: snsBypassTable.setStatus('current')
if mibBuilder.loadTexts: snsBypassTable.setDescription('Bypass status of Firewalls')
snsBypassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1), ).setIndexNames((0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsBypassIndex"))
if mibBuilder.loadTexts: snsBypassEntry.setStatus('current')
if mibBuilder.loadTexts: snsBypassEntry.setDescription('Bypass information')
snsBypassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsBypassIndex.setStatus('current')
if mibBuilder.loadTexts: snsBypassIndex.setDescription('Each line in the table')
snsBypassI2CAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassI2CAddress.setStatus('current')
if mibBuilder.loadTexts: snsBypassI2CAddress.setDescription('I2C Address of Bypass Device')
snsBypassSystemOff = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassSystemOff.setStatus('current')
if mibBuilder.loadTexts: snsBypassSystemOff.setDescription('System-off Bypass status')
snsBypassJustOn = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassJustOn.setStatus('current')
if mibBuilder.loadTexts: snsBypassJustOn.setDescription('Just-On Bypass status')
snsBypassRunTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassRunTime.setStatus('current')
if mibBuilder.loadTexts: snsBypassRunTime.setDescription('Run-Time Bypass status')
snsBypassWatchdog = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassWatchdog.setStatus('current')
if mibBuilder.loadTexts: snsBypassWatchdog.setDescription('Run-Time Watchdog Timer status')
mibBuilder.exportSymbols("STORMSHIELD-SYSTEM-MONITOR-MIB", snsDate=snsDate, snsBypassSystemOff=snsBypassSystemOff, snsBypassTable=snsBypassTable, snsDiskEntryIsRaid=snsDiskEntryIsRaid, PYSNMP_MODULE_ID=snsSystemMonitor, snsPowerSupplyIndex=snsPowerSupplyIndex, snsCpuEntry=snsCpuEntry, snsMem=snsMem, snsBypassI2CAddress=snsBypassI2CAddress, snsDiskEntryIndex=snsDiskEntryIndex, snsDiskEntryPosition=snsDiskEntryPosition, snsBypassJustOn=snsBypassJustOn, snsDiskEntryDiskName=snsDiskEntryDiskName, snsStatTime=snsStatTime, snsBypassEntry=snsBypassEntry, snsUptime=snsUptime, snsCpuTemp=snsCpuTemp, snsBypassWatchdog=snsBypassWatchdog, snsBypassIndex=snsBypassIndex, snsPowerSupplyTable=snsPowerSupplyTable, snsDiskTable=snsDiskTable, snsDiskEntry=snsDiskEntry, snsPowerSupplyEntry=snsPowerSupplyEntry, snsCpuTable=snsCpuTable, snsPowerSupplyPowered=snsPowerSupplyPowered, snsBypassRunTime=snsBypassRunTime, snsSystemMonitor=snsSystemMonitor, snsDiskEntryRaidStatus=snsDiskEntryRaidStatus, snsCpuIndex=snsCpuIndex, snsDiskEntrySmartResult=snsDiskEntrySmartResult)
