#
# PySNMP MIB module RADLAN-SENSORENTMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SENSORENTMIB
# Produced by pysmi-1.1.8 at Thu Jan  5 10:02:53 2023
# On host fv-az306-820 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
entPhysicalIndex, entityPhysicalGroup = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entityPhysicalGroup")
EntitySensorValue, entPhySensorEntry = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "entPhySensorEntry")
rlEnv, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "rlEnv")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, Counter32, TimeTicks, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32, Gauge32, iso, NotificationType, IpAddress, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32", "Gauge32", "iso", "NotificationType", "IpAddress", "mib-2")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
rlSensor = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 83, 4))
rlSensor.setRevisions(('2003-09-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSensor.setRevisionsDescriptions(('ADDED this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlSensor.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlSensor.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlSensor.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlSensor.setDescription('The private MIB module definition for sensors in Radlan devices.')
rlEntPhySensorTable = MibTable((1, 3, 6, 1, 4, 1, 89, 83, 3), )
if mibBuilder.loadTexts: rlEntPhySensorTable.setStatus('current')
if mibBuilder.loadTexts: rlEntPhySensorTable.setDescription('The addition to the table of sensors maintained by the environmental\n                monitor.')
rlEntPhySensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 83, 3, 1), )
entPhySensorEntry.registerAugmentions(("RADLAN-SENSORENTMIB", "rlEntPhySensorEntry"))
rlEntPhySensorEntry.setIndexNames(*entPhySensorEntry.getIndexNames())
if mibBuilder.loadTexts: rlEntPhySensorEntry.setStatus('current')
if mibBuilder.loadTexts: rlEntPhySensorEntry.setDescription('An additon to the entry in the sensor table, representing the\n                maximum/minimum values for the sensor associated.')
rlEnvPhySensorMinValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 1), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvPhySensorMinValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorMinValue.setDescription('Minimum value for the Sensor being instrumented.')
rlEnvPhySensorMaxValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 2), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvPhySensorMaxValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorMaxValue.setDescription('Maximum value for the Sensor being instrumented.')
rlEnvPhySensorTestValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 83, 3, 1, 3), EntitySensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEnvPhySensorTestValue.setStatus('current')
if mibBuilder.loadTexts: rlEnvPhySensorTestValue.setDescription('Test/reference value for the Sensor being instrumented.')
mibBuilder.exportSymbols("RADLAN-SENSORENTMIB", rlSensor=rlSensor, PYSNMP_MODULE_ID=rlSensor, rlEntPhySensorTable=rlEntPhySensorTable, rlEntPhySensorEntry=rlEntPhySensorEntry, rlEnvPhySensorMaxValue=rlEnvPhySensorMaxValue, rlEnvPhySensorMinValue=rlEnvPhySensorMinValue, rlEnvPhySensorTestValue=rlEnvPhySensorTestValue)
