#
# PySNMP MIB module OPENBSD-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-SENSORS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:24 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, enterprises, Counter64, NotificationType, iso, Counter32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "enterprises", "Counter64", "NotificationType", "iso", "Counter32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sensorsMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 2))
sensorsMIBObjects.setRevisions(('2012-09-20 00:00', '2012-01-31 00:00', '2008-12-23 00:00',))
if mibBuilder.loadTexts: sensorsMIBObjects.setLastUpdated('201209200000Z')
if mibBuilder.loadTexts: sensorsMIBObjects.setOrganization('OpenBSD')
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 2, 1))
sensorNumber = MibScalar((1, 3, 6, 1, 4, 1, 30155, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorNumber.setStatus('current')
sensorTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2), )
if mibBuilder.loadTexts: sensorTable.setStatus('current')
sensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1), ).setIndexNames((0, "OPENBSD-SENSORS-MIB", "sensorIndex"))
if mibBuilder.loadTexts: sensorEntry.setStatus('current')
sensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorIndex.setStatus('current')
sensorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorDescr.setStatus('current')
sensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("temperature", 0), ("fan", 1), ("voltsdc", 2), ("voltsac", 3), ("resistance", 4), ("power", 5), ("current", 6), ("watthour", 7), ("amphour", 8), ("indicator", 9), ("raw", 10), ("percent", 11), ("illuminance", 12), ("drive", 13), ("timedelta", 14), ("humidity", 15), ("freq", 16), ("angle", 17), ("distance", 18), ("pressure", 19), ("accel", 20)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorType.setStatus('current')
sensorDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorDevice.setStatus('current')
sensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorValue.setStatus('current')
sensorUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorUnits.setStatus('current')
sensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unspecified", 0), ("ok", 1), ("warn", 2), ("critical", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorStatus.setStatus('current')
mibBuilder.exportSymbols("OPENBSD-SENSORS-MIB", sensorNumber=sensorNumber, sensorValue=sensorValue, sensorUnits=sensorUnits, sensorEntry=sensorEntry, sensorDescr=sensorDescr, sensorDevice=sensorDevice, sensorTable=sensorTable, sensorType=sensorType, PYSNMP_MODULE_ID=sensorsMIBObjects, sensorIndex=sensorIndex, sensorStatus=sensorStatus, sensorsMIBObjects=sensorsMIBObjects, sensors=sensors)
