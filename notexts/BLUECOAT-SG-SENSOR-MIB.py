#
# PySNMP MIB module BLUECOAT-SG-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-SENSOR-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:13:48 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Counter32, TimeTicks, Unsigned32, iso, Bits, ObjectIdentity, MibIdentifier, Integer32, ModuleIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Counter32", "TimeTicks", "Unsigned32", "iso", "Bits", "ObjectIdentity", "MibIdentifier", "Integer32", "ModuleIdentity", "IpAddress", "NotificationType")
TimeStamp, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "TruthValue", "DisplayString")
deviceSensorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 1))
deviceSensorMIB.setRevisions(('2015-11-26 03:00', '2013-07-11 03:00', '2007-11-05 03:00', '2002-11-06 03:00',))
if mibBuilder.loadTexts: deviceSensorMIB.setLastUpdated('201511260300Z')
if mibBuilder.loadTexts: deviceSensorMIB.setOrganization('Blue Coat Systems, Inc.')
deviceSensorMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1))
deviceSensorMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2))
deviceSensorMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0))
class SensorUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("truthvalue", 2), ("specialEnum", 3), ("volts", 4), ("celsius", 5), ("rpm", 6))

class SensorCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("ok", 1), ("unknown", 2), ("notInstalled", 3), ("voltageLowWarning", 4), ("voltageLowCritical", 5), ("noPower", 6), ("voltageHighWarning", 7), ("voltageHighCritical", 8), ("voltageHighSevere", 9), ("temperatureHighWarning", 10), ("temperatureHighCritical", 11), ("temperatureHighSevere", 12), ("fanSlowWarning", 13), ("fanSlowCritical", 14), ("fanStopped", 15))

class ExpBase10(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-24, 24)

class SensorValue(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class SensorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3), ("notInstalled", 4))

deviceSensorValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1))
deviceSensorValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: deviceSensorValueTable.setStatus('current')
deviceSensorValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-SENSOR-MIB", "deviceSensorIndex"))
if mibBuilder.loadTexts: deviceSensorValueEntry.setStatus('current')
deviceSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceSensorIndex.setStatus('current')
deviceSensorTrapEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTrapEnabled.setStatus('current')
deviceSensorUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 3), SensorUnits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorUnits.setStatus('current')
deviceSensorScale = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 4), ExpBase10()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorScale.setStatus('current')
deviceSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 5), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorValue.setStatus('current')
deviceSensorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 6), SensorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorCode.setStatus('current')
deviceSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 7), SensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorStatus.setStatus('current')
deviceSensorTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 8), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorTimeStamp.setStatus('current')
deviceSensorName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceSensorName.setStatus('current')
deviceSensorTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0, 1)).setObjects(("BLUECOAT-SG-SENSOR-MIB", "deviceSensorName"), ("BLUECOAT-SG-SENSOR-MIB", "deviceSensorValue"), ("BLUECOAT-SG-SENSOR-MIB", "deviceSensorCode"))
if mibBuilder.loadTexts: deviceSensorTrap.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-SENSOR-MIB", deviceSensorValueTable=deviceSensorValueTable, SensorStatus=SensorStatus, deviceSensorUnits=deviceSensorUnits, deviceSensorMIBObjects=deviceSensorMIBObjects, PYSNMP_MODULE_ID=deviceSensorMIB, deviceSensorScale=deviceSensorScale, SensorCode=SensorCode, deviceSensorMIBNotificationsPrefix=deviceSensorMIBNotificationsPrefix, deviceSensorTrap=deviceSensorTrap, ExpBase10=ExpBase10, deviceSensorIndex=deviceSensorIndex, deviceSensorTrapEnabled=deviceSensorTrapEnabled, deviceSensorTimeStamp=deviceSensorTimeStamp, SensorValue=SensorValue, deviceSensorStatus=deviceSensorStatus, deviceSensorMIBNotifications=deviceSensorMIBNotifications, deviceSensorValue=deviceSensorValue, deviceSensorCode=deviceSensorCode, deviceSensorValueEntry=deviceSensorValueEntry, deviceSensorName=deviceSensorName, deviceSensorMIB=deviceSensorMIB, SensorUnits=SensorUnits, deviceSensorValues=deviceSensorValues)
