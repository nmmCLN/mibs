#
# PySNMP MIB module FREENAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ixsystems/FREENAS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:20:19 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibIdentifier, NotificationType, Counter64, Counter32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, ModuleIdentity, iso, Gauge32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "NotificationType", "Counter64", "Counter32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "ModuleIdentity", "iso", "Gauge32", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
freeNas = ModuleIdentity((1, 3, 6, 1, 4, 1, 50536))
freeNas.setRevisions(('2017-10-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: freeNas.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: freeNas.setLastUpdated('201710270000Z')
if mibBuilder.loadTexts: freeNas.setOrganization('www.ixsystems.com')
if mibBuilder.loadTexts: freeNas.setContactInfo('postal:   2490 Kruse Dr\n                   San Jose, CA 95131\n\n         email:    support@iXsystems.com')
if mibBuilder.loadTexts: freeNas.setDescription('')
class ZPoolHealthType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("online", 0), ("degraded", 1), ("faulted", 2), ("offline", 3), ("unavail", 4), ("removed", 5))

class AlertLevelType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(20, 30, 50))
    namedValues = NamedValues(("info", 20), ("warning", 30), ("critical", 50))

zfs = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1))
notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 2))
notificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 2, 1))
notificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 2, 2))
zpool = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 1))
dataset = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 2))
zvol = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 3))
arc = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 4))
l2arc = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 5))
zil = MibIdentifier((1, 3, 6, 1, 4, 1, 50536, 1, 6))
zpoolTable = MibTable((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1), )
if mibBuilder.loadTexts: zpoolTable.setStatus('current')
if mibBuilder.loadTexts: zpoolTable.setDescription('')
zpoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1), ).setIndexNames((0, "FREENAS-MIB", "zpoolIndex"))
if mibBuilder.loadTexts: zpoolEntry.setStatus('current')
if mibBuilder.loadTexts: zpoolEntry.setDescription('')
zpoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: zpoolIndex.setStatus('current')
if mibBuilder.loadTexts: zpoolIndex.setDescription('')
zpoolDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolDescr.setStatus('current')
if mibBuilder.loadTexts: zpoolDescr.setDescription('')
zpoolAllocationUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolAllocationUnits.setStatus('current')
if mibBuilder.loadTexts: zpoolAllocationUnits.setDescription('')
zpoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zpoolSize.setStatus('current')
if mibBuilder.loadTexts: zpoolSize.setDescription('')
zpoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolUsed.setStatus('current')
if mibBuilder.loadTexts: zpoolUsed.setDescription('')
zpoolAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolAvailable.setStatus('current')
if mibBuilder.loadTexts: zpoolAvailable.setDescription('')
zpoolHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 7), ZPoolHealthType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolHealth.setStatus('current')
if mibBuilder.loadTexts: zpoolHealth.setDescription('The current health of the containing pool, as reported\n        by zpool status.')
zpoolReadOps = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolReadOps.setStatus('current')
if mibBuilder.loadTexts: zpoolReadOps.setDescription('The number of read I/O operations sent to the pool or device,\n        including metadata requests (averaged since system booted).')
zpoolWriteOps = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolWriteOps.setStatus('current')
if mibBuilder.loadTexts: zpoolWriteOps.setDescription('The number of write I/O operations sent to the pool or device\n        (averaged since system booted).')
zpoolReadBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolReadBytes.setStatus('current')
if mibBuilder.loadTexts: zpoolReadBytes.setDescription('The bandwidth of all read operations (including metadata),\n        expressed as units per second (averaged since system booted)')
zpoolWriteBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolWriteBytes.setStatus('current')
if mibBuilder.loadTexts: zpoolWriteBytes.setDescription('The bandwidth of all write operations, expressed as units per\n        second (averaged since system booted).')
zpoolReadOps1sec = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolReadOps1sec.setStatus('current')
if mibBuilder.loadTexts: zpoolReadOps1sec.setDescription('The number of read I/O operations sent to the pool or device,\n        including metadata requests (over 1 second interval).')
zpoolWriteOps1sec = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolWriteOps1sec.setStatus('current')
if mibBuilder.loadTexts: zpoolWriteOps1sec.setDescription('The number of write I/O operations sent to the pool or device\n        (over 1 second interval).')
zpoolReadBytes1sec = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolReadBytes1sec.setStatus('current')
if mibBuilder.loadTexts: zpoolReadBytes1sec.setDescription('The bandwidth of all read operations (including metadata),\n        expressed as units per second (over 1 second interval)')
zpoolWriteBytes1sec = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zpoolWriteBytes1sec.setStatus('current')
if mibBuilder.loadTexts: zpoolWriteBytes1sec.setDescription('The bandwidth of all write operations, expressed as units per\n        second (over 1 second interval).')
datasetTable = MibTable((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1), )
if mibBuilder.loadTexts: datasetTable.setStatus('current')
if mibBuilder.loadTexts: datasetTable.setDescription('')
datasetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1), ).setIndexNames((0, "FREENAS-MIB", "datasetIndex"))
if mibBuilder.loadTexts: datasetEntry.setStatus('current')
if mibBuilder.loadTexts: datasetEntry.setDescription('')
datasetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: datasetIndex.setStatus('current')
if mibBuilder.loadTexts: datasetIndex.setDescription('')
datasetDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: datasetDescr.setStatus('current')
if mibBuilder.loadTexts: datasetDescr.setDescription('')
datasetAllocationUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: datasetAllocationUnits.setStatus('current')
if mibBuilder.loadTexts: datasetAllocationUnits.setDescription('')
datasetSize = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: datasetSize.setStatus('current')
if mibBuilder.loadTexts: datasetSize.setDescription('')
datasetUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: datasetUsed.setStatus('current')
if mibBuilder.loadTexts: datasetUsed.setDescription('')
datasetAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: datasetAvailable.setStatus('current')
if mibBuilder.loadTexts: datasetAvailable.setDescription('')
zvolTable = MibTable((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1), )
if mibBuilder.loadTexts: zvolTable.setStatus('current')
if mibBuilder.loadTexts: zvolTable.setDescription('')
zvolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1), ).setIndexNames((0, "FREENAS-MIB", "zvolIndex"))
if mibBuilder.loadTexts: zvolEntry.setStatus('current')
if mibBuilder.loadTexts: zvolEntry.setDescription('')
zvolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: zvolIndex.setStatus('current')
if mibBuilder.loadTexts: zvolIndex.setDescription('')
zvolDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolDescr.setStatus('current')
if mibBuilder.loadTexts: zvolDescr.setDescription('')
zvolAllocationUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolAllocationUnits.setStatus('current')
if mibBuilder.loadTexts: zvolAllocationUnits.setDescription('')
zvolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zvolSize.setStatus('current')
if mibBuilder.loadTexts: zvolSize.setDescription('')
zvolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolUsed.setStatus('current')
if mibBuilder.loadTexts: zvolUsed.setDescription('')
zvolAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 50536, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zvolAvailable.setStatus('current')
if mibBuilder.loadTexts: zvolAvailable.setDescription('')
zfsArcSize = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcSize.setStatus('current')
if mibBuilder.loadTexts: zfsArcSize.setDescription('')
zfsArcMeta = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcMeta.setStatus('current')
if mibBuilder.loadTexts: zfsArcMeta.setDescription('')
zfsArcData = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcData.setStatus('current')
if mibBuilder.loadTexts: zfsArcData.setDescription('')
zfsArcHits = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcHits.setStatus('current')
if mibBuilder.loadTexts: zfsArcHits.setDescription('')
zfsArcMisses = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcMisses.setStatus('current')
if mibBuilder.loadTexts: zfsArcMisses.setDescription('')
zfsArcC = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcC.setStatus('current')
if mibBuilder.loadTexts: zfsArcC.setDescription('')
zfsArcP = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcP.setStatus('current')
if mibBuilder.loadTexts: zfsArcP.setDescription('')
zfsArcMissPercent = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcMissPercent.setStatus('current')
if mibBuilder.loadTexts: zfsArcMissPercent.setDescription('Arc Miss Percentage.\n        (Note: Floating precision sent across SNMP as a String')
zfsArcCacheHitRatio = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcCacheHitRatio.setStatus('current')
if mibBuilder.loadTexts: zfsArcCacheHitRatio.setDescription('Arc Cache Hit Ration Percentage.\n        (Note: Floating precision sent across SNMP as a String')
zfsArcCacheMissRatio = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 4, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsArcCacheMissRatio.setStatus('current')
if mibBuilder.loadTexts: zfsArcCacheMissRatio.setDescription('Arc Cache Miss Ration Percentage.\n        (Note: Floating precision sent across SNMP as a String')
zfsL2ArcHits = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcHits.setStatus('current')
if mibBuilder.loadTexts: zfsL2ArcHits.setDescription('')
zfsL2ArcMisses = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcMisses.setStatus('current')
if mibBuilder.loadTexts: zfsL2ArcMisses.setDescription('')
zfsL2ArcRead = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcRead.setStatus('current')
if mibBuilder.loadTexts: zfsL2ArcRead.setDescription('')
zfsL2ArcWrite = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcWrite.setStatus('current')
if mibBuilder.loadTexts: zfsL2ArcWrite.setDescription('')
zfsL2ArcSize = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 5, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsL2ArcSize.setStatus('current')
if mibBuilder.loadTexts: zfsL2ArcSize.setDescription('')
zfsZilstatOps1sec = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 6, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsZilstatOps1sec.setStatus('current')
if mibBuilder.loadTexts: zfsZilstatOps1sec.setDescription('The ops column parsed from the command zilstat 1 1')
zfsZilstatOps5sec = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 6, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsZilstatOps5sec.setStatus('current')
if mibBuilder.loadTexts: zfsZilstatOps5sec.setDescription('The ops column parsed from the command zilstat 5 1')
zfsZilstatOps10sec = MibScalar((1, 3, 6, 1, 4, 1, 50536, 1, 6, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zfsZilstatOps10sec.setStatus('current')
if mibBuilder.loadTexts: zfsZilstatOps10sec.setDescription('The ops column parsed from the command zilstat 10 1')
alert = NotificationType((1, 3, 6, 1, 4, 1, 50536, 2, 1, 1)).setObjects(("FREENAS-MIB", "alertId"), ("FREENAS-MIB", "alertLevel"), ("FREENAS-MIB", "alertMessage"))
if mibBuilder.loadTexts: alert.setStatus('current')
if mibBuilder.loadTexts: alert.setDescription('An alert raised')
alertId = MibScalar((1, 3, 6, 1, 4, 1, 50536, 2, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertId.setStatus('current')
if mibBuilder.loadTexts: alertId.setDescription('')
alertLevel = MibScalar((1, 3, 6, 1, 4, 1, 50536, 2, 2, 2), AlertLevelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertLevel.setStatus('current')
if mibBuilder.loadTexts: alertLevel.setDescription('')
alertMessage = MibScalar((1, 3, 6, 1, 4, 1, 50536, 2, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertMessage.setStatus('current')
if mibBuilder.loadTexts: alertMessage.setDescription('')
alertCancellation = NotificationType((1, 3, 6, 1, 4, 1, 50536, 2, 1, 2)).setObjects(("FREENAS-MIB", "alertId"))
if mibBuilder.loadTexts: alertCancellation.setStatus('current')
if mibBuilder.loadTexts: alertCancellation.setDescription('An alert cancelled')
mibBuilder.exportSymbols("FREENAS-MIB", zpoolReadBytes=zpoolReadBytes, zvolEntry=zvolEntry, l2arc=l2arc, zpoolIndex=zpoolIndex, zpoolUsed=zpoolUsed, zpoolWriteOps=zpoolWriteOps, zpoolReadOps=zpoolReadOps, zfsArcMisses=zfsArcMisses, zfsArcCacheHitRatio=zfsArcCacheHitRatio, datasetUsed=datasetUsed, zfsArcCacheMissRatio=zfsArcCacheMissRatio, PYSNMP_MODULE_ID=freeNas, zfsL2ArcMisses=zfsL2ArcMisses, datasetIndex=datasetIndex, zfsZilstatOps5sec=zfsZilstatOps5sec, zfsL2ArcSize=zfsL2ArcSize, zpoolEntry=zpoolEntry, zpoolAllocationUnits=zpoolAllocationUnits, zpoolTable=zpoolTable, datasetSize=datasetSize, notificationPrefix=notificationPrefix, zvolSize=zvolSize, zpoolSize=zpoolSize, zvolAllocationUnits=zvolAllocationUnits, zfsArcP=zfsArcP, notificationObjects=notificationObjects, datasetEntry=datasetEntry, zfsArcSize=zfsArcSize, zfsZilstatOps1sec=zfsZilstatOps1sec, zvolAvailable=zvolAvailable, alertLevel=alertLevel, zfsZilstatOps10sec=zfsZilstatOps10sec, alertCancellation=alertCancellation, zil=zil, zfsL2ArcWrite=zfsL2ArcWrite, datasetTable=datasetTable, zvolUsed=zvolUsed, arc=arc, zfsL2ArcHits=zfsL2ArcHits, zpoolDescr=zpoolDescr, zpoolWriteOps1sec=zpoolWriteOps1sec, dataset=dataset, datasetDescr=datasetDescr, zfs=zfs, ZPoolHealthType=ZPoolHealthType, zfsArcC=zfsArcC, zvolIndex=zvolIndex, datasetAvailable=datasetAvailable, zfsL2ArcRead=zfsL2ArcRead, alert=alert, zvolDescr=zvolDescr, alertMessage=alertMessage, zpoolHealth=zpoolHealth, zvolTable=zvolTable, notifications=notifications, zvol=zvol, zpoolWriteBytes=zpoolWriteBytes, zpoolReadOps1sec=zpoolReadOps1sec, zfsArcMissPercent=zfsArcMissPercent, AlertLevelType=AlertLevelType, zpool=zpool, zpoolReadBytes1sec=zpoolReadBytes1sec, zpoolWriteBytes1sec=zpoolWriteBytes1sec, freeNas=freeNas, zfsArcHits=zfsArcHits, zfsArcMeta=zfsArcMeta, zfsArcData=zfsArcData, alertId=alertId, zpoolAvailable=zpoolAvailable, datasetAllocationUnits=datasetAllocationUnits)
