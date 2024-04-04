#
# PySNMP MIB module OPENBSD-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-SENSORS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:36 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Integer32, MibIdentifier, Unsigned32, ModuleIdentity, Gauge32, Counter32, enterprises, Counter64, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Gauge32", "Counter32", "enterprises", "Counter64", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("OPENBSD-SENSORS-MIB", sensorValue=sensorValue, sensorTable=sensorTable, sensorType=sensorType, sensorDescr=sensorDescr, sensorUnits=sensorUnits, sensorStatus=sensorStatus, sensorNumber=sensorNumber, sensorIndex=sensorIndex, PYSNMP_MODULE_ID=sensorsMIBObjects, sensorEntry=sensorEntry, sensors=sensors, sensorDevice=sensorDevice, sensorsMIBObjects=sensorsMIBObjects)
