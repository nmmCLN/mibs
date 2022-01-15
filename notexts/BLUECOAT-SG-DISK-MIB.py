#
# PySNMP MIB module BLUECOAT-SG-DISK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-DISK-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:10:14 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, TimeTicks, MibIdentifier, iso, ModuleIdentity, Unsigned32, Integer32, ObjectIdentity, Counter32, IpAddress, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "TimeTicks", "MibIdentifier", "iso", "ModuleIdentity", "Unsigned32", "Integer32", "ObjectIdentity", "Counter32", "IpAddress", "Gauge32", "Counter64")
TruthValue, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "TextualConvention", "DisplayString")
deviceDiskMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 2))
deviceDiskMIB.setRevisions(('2013-07-11 03:00', '2007-11-05 03:00', '2002-11-06 03:00',))
if mibBuilder.loadTexts: deviceDiskMIB.setLastUpdated('201307110300Z')
if mibBuilder.loadTexts: deviceDiskMIB.setOrganization('Blue Coat Systems, Inc.')
deviceDiskMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1))
deviceDiskMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 2, 2))
deviceDiskMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 2, 2, 0))
class DiskStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("present", 1), ("initializing", 2), ("inserted", 3), ("offline", 4), ("removed", 5), ("notpresent", 6), ("empty", 7), ("ioerror", 8), ("unusable", 9), ("unknown", 10))

deviceDiskValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1))
deviceDiskValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1), )
if mibBuilder.loadTexts: deviceDiskValueTable.setStatus('current')
deviceDiskValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-DISK-MIB", "deviceDiskIndex"))
if mibBuilder.loadTexts: deviceDiskValueEntry.setStatus('current')
deviceDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceDiskIndex.setStatus('current')
deviceDiskTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskTrapEnabled.setStatus('current')
deviceDiskStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 3), DiskStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskStatus.setStatus('current')
deviceDiskTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 4), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskTimeStamp.setStatus('current')
deviceDiskVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskVendor.setStatus('current')
deviceDiskProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskProduct.setStatus('current')
deviceDiskRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskRevision.setStatus('current')
deviceDiskSerialN = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskSerialN.setStatus('current')
deviceDiskBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 9), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskBlockSize.setStatus('current')
deviceDiskBlockCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 2, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceDiskBlockCount.setStatus('current')
deviceDiskTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 2, 2, 0, 1)).setObjects(("BLUECOAT-SG-DISK-MIB", "deviceDiskStatus"))
if mibBuilder.loadTexts: deviceDiskTrap.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-DISK-MIB", deviceDiskTrap=deviceDiskTrap, deviceDiskVendor=deviceDiskVendor, deviceDiskSerialN=deviceDiskSerialN, deviceDiskBlockSize=deviceDiskBlockSize, deviceDiskIndex=deviceDiskIndex, deviceDiskMIBNotificationsPrefix=deviceDiskMIBNotificationsPrefix, deviceDiskStatus=deviceDiskStatus, deviceDiskMIBNotifications=deviceDiskMIBNotifications, deviceDiskProduct=deviceDiskProduct, deviceDiskMIB=deviceDiskMIB, PYSNMP_MODULE_ID=deviceDiskMIB, deviceDiskValueEntry=deviceDiskValueEntry, DiskStatus=DiskStatus, deviceDiskBlockCount=deviceDiskBlockCount, deviceDiskTrapEnabled=deviceDiskTrapEnabled, deviceDiskRevision=deviceDiskRevision, deviceDiskValues=deviceDiskValues, deviceDiskMIBObjects=deviceDiskMIBObjects, deviceDiskValueTable=deviceDiskValueTable, deviceDiskTimeStamp=deviceDiskTimeStamp)
