#
# PySNMP MIB module PACKETLOGIC-HW-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-SENSORS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:22:26 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, Gauge32, Counter32, MibIdentifier, NotificationType, Unsigned32, TimeTicks, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32", "TimeTicks", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "ObjectIdentity")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
sensors = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3))
sensors.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: sensors.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: sensors.setOrganization('Procera Networks, Inc.')
tempSensors = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1), )
if mibBuilder.loadTexts: tempSensors.setStatus('current')
tempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1), ).setIndexNames((0, "PACKETLOGIC-HW-SENSORS-MIB", "tempSensorEntryIndex"))
if mibBuilder.loadTexts: tempSensorEntry.setStatus('current')
tempSensorEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: tempSensorEntryIndex.setStatus('current')
fanSensors = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4), )
if mibBuilder.loadTexts: fanSensors.setStatus('current')
fanSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1), ).setIndexNames((0, "PACKETLOGIC-HW-SENSORS-MIB", "fanSensorEntryIndex"))
if mibBuilder.loadTexts: fanSensorEntry.setStatus('current')
fanSensorEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: fanSensorEntryIndex.setStatus('current')
tempSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorId.setStatus('current')
tempSensorReading = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorReading.setStatus('current')
tempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorStatus.setStatus('current')
tempSensorUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempSensorUnit.setStatus('current')
fanSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSensorId.setStatus('current')
fanSensorSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSensorSpeed.setStatus('current')
fanSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSensorStatus.setStatus('current')
fanSensorUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 30, 3, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSensorUnit.setStatus('current')
mibBuilder.exportSymbols("PACKETLOGIC-HW-SENSORS-MIB", fanSensorUnit=fanSensorUnit, tempSensorStatus=tempSensorStatus, tempSensorEntryIndex=tempSensorEntryIndex, PYSNMP_MODULE_ID=sensors, fanSensors=fanSensors, fanSensorStatus=fanSensorStatus, fanSensorEntryIndex=fanSensorEntryIndex, sensors=sensors, fanSensorEntry=fanSensorEntry, fanSensorId=fanSensorId, tempSensorReading=tempSensorReading, tempSensorEntry=tempSensorEntry, fanSensorSpeed=fanSensorSpeed, tempSensors=tempSensors, tempSensorUnit=tempSensorUnit, tempSensorId=tempSensorId)
