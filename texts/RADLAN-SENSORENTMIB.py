#
# PySNMP MIB module RADLAN-SENSORENTMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SENSORENTMIB
# Produced by pysmi-1.1.8 at Fri Dec  2 16:01:02 2022
# On host fv-az267-189 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
entityPhysicalGroup, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entityPhysicalGroup", "entPhysicalIndex")
entPhySensorEntry, EntitySensorValue = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "entPhySensorEntry", "EntitySensorValue")
rlEnv, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "rlEnv")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Bits, TimeTicks, NotificationType, Gauge32, Unsigned32, mib_2, IpAddress, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "TimeTicks", "NotificationType", "Gauge32", "Unsigned32", "mib-2", "IpAddress", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "ObjectIdentity", "Counter32")
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
mibBuilder.exportSymbols("RADLAN-SENSORENTMIB", rlEnvPhySensorTestValue=rlEnvPhySensorTestValue, rlEnvPhySensorMinValue=rlEnvPhySensorMinValue, rlEnvPhySensorMaxValue=rlEnvPhySensorMaxValue, rlEntPhySensorTable=rlEntPhySensorTable, rlEntPhySensorEntry=rlEntPhySensorEntry, PYSNMP_MODULE_ID=rlSensor, rlSensor=rlSensor)
