#
# PySNMP MIB module PACKETLOGIC-HW-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-SENSORS-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:36:14 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
hw, = mibBuilder.importSymbols("PACKETLOGIC-HW-MIB", "hw")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Counter64, NotificationType, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Integer32, iso, Bits, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Integer32", "iso", "Bits", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
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
mibBuilder.exportSymbols("PACKETLOGIC-HW-SENSORS-MIB", tempSensorStatus=tempSensorStatus, PYSNMP_MODULE_ID=sensors, tempSensorEntry=tempSensorEntry, tempSensorUnit=tempSensorUnit, fanSensorId=fanSensorId, tempSensors=tempSensors, fanSensorEntryIndex=fanSensorEntryIndex, fanSensorStatus=fanSensorStatus, fanSensorSpeed=fanSensorSpeed, fanSensorEntry=fanSensorEntry, fanSensorUnit=fanSensorUnit, tempSensorId=tempSensorId, fanSensors=fanSensors, tempSensorReading=tempSensorReading, tempSensorEntryIndex=tempSensorEntryIndex, sensors=sensors)
