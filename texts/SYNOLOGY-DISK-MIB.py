#
# PySNMP MIB module SYNOLOGY-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/synology/SYNOLOGY-DISK-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:16:02 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, TimeTicks, Counter64, NotificationType, Integer32, Gauge32, iso, IpAddress, Counter32, MibIdentifier, enterprises, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter64", "NotificationType", "Integer32", "Gauge32", "iso", "IpAddress", "Counter32", "MibIdentifier", "enterprises", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synoDisk = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 2))
synoDisk.setRevisions(('2013-09-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synoDisk.setRevisionsDescriptions(('Second draft.',))
if mibBuilder.loadTexts: synoDisk.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoDisk.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synoDisk.setContactInfo('postal:   Jay Pan\n          email:    jaypan@synology.com')
if mibBuilder.loadTexts: synoDisk.setDescription('Characteristics of the disk information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
diskTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 2, 1), )
if mibBuilder.loadTexts: diskTable.setStatus('current')
if mibBuilder.loadTexts: diskTable.setDescription('Synology disk table')
diskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1), ).setIndexNames((0, "SYNOLOGY-DISK-MIB", "diskIndex"))
if mibBuilder.loadTexts: diskEntry.setStatus('current')
if mibBuilder.loadTexts: diskEntry.setDescription('For all disk entry')
diskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: diskIndex.setStatus('current')
if mibBuilder.loadTexts: diskIndex.setDescription('The index of disk table')
diskID = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskID.setStatus('current')
if mibBuilder.loadTexts: diskID.setDescription('Synology disk ID\n\t The ID of disk is assigned by disk Station.\n\t')
diskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskModel.setStatus('current')
if mibBuilder.loadTexts: diskModel.setDescription('Synology disk model name\n\t The disk model name will be showed here.\n\t')
diskType = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskType.setStatus('current')
if mibBuilder.loadTexts: diskType.setDescription('Synology disk type\n\t The type of disk will be showed here, including SATA, SSD and so on.\n\t')
diskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskStatus.setStatus('current')
if mibBuilder.loadTexts: diskStatus.setDescription('Synology disk status \n\t Each meanings of status represented describe below.\n\n\t Normal(1): The hard disk functions normally.\n\t Initialized(2): The hard disk has system partition but no data.\n\t NotInitialized(3):\tThe hard disk does not have system in system partition.\t\n\t SystemPartitionFailed(4): The system partitions on the hard disks are damaged.\n\t Crashed(5): The hard disk has damaged.\n\t')
diskTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskTemperature.setStatus('current')
if mibBuilder.loadTexts: diskTemperature.setDescription('Synology disk temperature\n\t The temperature of each disk uses Celsius degree.\n\t')
diskConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 2, 2))
diskCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 2, 2, 1))
diskGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 2, 2, 2))
diskCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 2, 2, 1, 1)).setObjects(("SYNOLOGY-DISK-MIB", "diskGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diskCompliance = diskCompliance.setStatus('current')
if mibBuilder.loadTexts: diskCompliance.setDescription('The compliance statement for synoDisk entities which\n            implement the SYNOLOGY DISK MIB.')
diskGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 2, 2, 2, 1)).setObjects(("SYNOLOGY-DISK-MIB", "diskID"), ("SYNOLOGY-DISK-MIB", "diskModel"), ("SYNOLOGY-DISK-MIB", "diskType"), ("SYNOLOGY-DISK-MIB", "diskStatus"), ("SYNOLOGY-DISK-MIB", "diskTemperature"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diskGroup = diskGroup.setStatus('current')
if mibBuilder.loadTexts: diskGroup.setDescription('A collection of objects providing basic information\n             of an synology disk entity.')
mibBuilder.exportSymbols("SYNOLOGY-DISK-MIB", diskEntry=diskEntry, diskStatus=diskStatus, diskID=diskID, diskGroup=diskGroup, diskModel=diskModel, diskTable=diskTable, synology=synology, diskConformance=diskConformance, diskIndex=diskIndex, synoDisk=synoDisk, diskCompliances=diskCompliances, diskGroups=diskGroups, PYSNMP_MODULE_ID=synoDisk, diskCompliance=diskCompliance, diskTemperature=diskTemperature, diskType=diskType)
