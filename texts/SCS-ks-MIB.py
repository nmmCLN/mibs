#
# PySNMP MIB module SCS-ks-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/carel/SCS-ks-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:14:04 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysLocation, sysContact, sysName = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation", "sysContact", "sysName")
TimeTicks, ModuleIdentity, Bits, Unsigned32, IpAddress, ObjectIdentity, Counter64, enterprises, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter32, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32", "IpAddress", "ObjectIdentity", "Counter64", "enterprises", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter32", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
scs_ks = ModuleIdentity((1, 3, 6, 1, 4, 1, 9839, 1, 1)).setLabel("scs-ks")
scs_ks.setRevisions(('2020-11-05 18:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: scs_ks.setRevisionsDescriptions(('scs ks MIB',))
if mibBuilder.loadTexts: scs_ks.setLastUpdated('202011051805Z')
if mibBuilder.loadTexts: scs_ks.setOrganization('None')
if mibBuilder.loadTexts: scs_ks.setContactInfo('\n                        None\n                        GH: https://github.com/Torch09\n                        Mail: torch09gh@gmail.com\n                ')
if mibBuilder.loadTexts: scs_ks.setDescription('This is the unofficial MIB module for the SCS KS.')
carel = MibIdentifier((1, 3, 6, 1, 4, 1, 9839))
systm = MibIdentifier((1, 3, 6, 1, 4, 1, 9839, 1))
scs = MibIdentifier((1, 3, 6, 1, 4, 1, 9839, 1, 2))
status_evaporator_fan = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-evaporator-fan").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_evaporator_fan.setStatus('current')
if mibBuilder.loadTexts: status_evaporator_fan.setDescription('Evaporator Fan alarm 0=OK;1=Error')
status_condenser_fan = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-condenser-fan").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_condenser_fan.setStatus('current')
if mibBuilder.loadTexts: status_condenser_fan.setDescription('Condenser Fan alarm 0=OK;1=Error')
status_compressor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-compressor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_compressor.setStatus('current')
if mibBuilder.loadTexts: status_compressor.setDescription('Compressor alarm 0=OK;1=Error')
status_heater_thermal_protection = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-heater-thermal-protection").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_heater_thermal_protection.setStatus('current')
if mibBuilder.loadTexts: status_heater_thermal_protection.setDescription('Heater thermal protection alarm 0=OK;1=Error')
status_exhaust_air_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-exhaust-air-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_exhaust_air_sensor.setStatus('current')
if mibBuilder.loadTexts: status_exhaust_air_sensor.setDescription('Exhaust air sensor alarm 0=OK;1=Error')
status_supply_air_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-supply-air-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_supply_air_sensor.setStatus('current')
if mibBuilder.loadTexts: status_supply_air_sensor.setDescription('Supply air sensor alarm 0=OK;1=Error')
status_outside_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-outside-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_outside_sensor.setStatus('current')
if mibBuilder.loadTexts: status_outside_sensor.setDescription('Outside temperature sensor alarm 0=OK;1=Error')
status_room_temperature_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-room-temperature-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_room_temperature_sensor.setStatus('current')
if mibBuilder.loadTexts: status_room_temperature_sensor.setDescription('Temperature room sensor alarm 0=OK;1=Error')
status_room_humidity_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-room-humidity-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_room_humidity_sensor.setStatus('current')
if mibBuilder.loadTexts: status_room_humidity_sensor.setDescription('Humidity room sensor alarm 0=OK;1=Error')
status_min_exhaust_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-min-exhaust-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_min_exhaust_air_temperature.setStatus('current')
if mibBuilder.loadTexts: status_min_exhaust_air_temperature.setDescription('Minimum exhaust air temperature alarm 0=OK;1=Error')
status_max_exhaust_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-max-exhaust-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_max_exhaust_air_temperature.setStatus('current')
if mibBuilder.loadTexts: status_max_exhaust_air_temperature.setDescription('Maximum exhaust air temperature alarm 0=OK;1=Error')
status_min_supply_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-min-supply-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_min_supply_air_temperature.setStatus('current')
if mibBuilder.loadTexts: status_min_supply_air_temperature.setDescription('Minimum supply air temperature alarm 0=OK;1=Error')
status_water_sensor = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-water-sensor").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_water_sensor.setStatus('current')
if mibBuilder.loadTexts: status_water_sensor.setDescription('Water sensor alarm 0=OK;1=Error')
status_filter_monitoring = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-filter-monitoring").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_filter_monitoring.setStatus('current')
if mibBuilder.loadTexts: status_filter_monitoring.setDescription('Filter monitoring alarm 0=OK;1=Error')
exhaust_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("exhaust-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: exhaust_air_temperature.setStatus('current')
if mibBuilder.loadTexts: exhaust_air_temperature.setDescription('Exhaust air temperature 235 = 23.5 degree Celsius')
supply_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("supply-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: supply_air_temperature.setStatus('current')
if mibBuilder.loadTexts: supply_air_temperature.setDescription('Supply air temperature 235 = 23.5 degree Celsius')
outside_air_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("outside-air-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: outside_air_temperature.setStatus('current')
if mibBuilder.loadTexts: outside_air_temperature.setDescription('Outside air temperature 235 = 23.5 degree Celsius')
room_temperature = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("room-temperature").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: room_temperature.setStatus('current')
if mibBuilder.loadTexts: room_temperature.setDescription('Room temperature 235 = 23.5 degree Celsius')
room_humidity = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-999, 999))).setLabel("room-humidity").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: room_humidity.setStatus('current')
if mibBuilder.loadTexts: room_humidity.setDescription('Room humidity 235 = 23.5 %')
status_operational_status = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-operational-status").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_operational_status.setStatus('current')
if mibBuilder.loadTexts: status_operational_status.setDescription('Operational status 0=Off;1=Running')
status_collective_fault = MibScalar((1, 3, 6, 1, 4, 1, 9839, 1, 2, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("status-collective-fault").setUnits('N/A').setMaxAccess("readonly")
if mibBuilder.loadTexts: status_collective_fault.setStatus('current')
if mibBuilder.loadTexts: status_collective_fault.setDescription('Collective fault alarm 0=Error;1=Ok')
mibBuilder.exportSymbols("SCS-ks-MIB", status_room_temperature_sensor=status_room_temperature_sensor, status_supply_air_sensor=status_supply_air_sensor, status_evaporator_fan=status_evaporator_fan, status_filter_monitoring=status_filter_monitoring, status_operational_status=status_operational_status, status_heater_thermal_protection=status_heater_thermal_protection, status_room_humidity_sensor=status_room_humidity_sensor, room_humidity=room_humidity, systm=systm, status_exhaust_air_sensor=status_exhaust_air_sensor, status_condenser_fan=status_condenser_fan, status_max_exhaust_air_temperature=status_max_exhaust_air_temperature, status_collective_fault=status_collective_fault, carel=carel, supply_air_temperature=supply_air_temperature, scs_ks=scs_ks, exhaust_air_temperature=exhaust_air_temperature, status_water_sensor=status_water_sensor, status_outside_sensor=status_outside_sensor, PYSNMP_MODULE_ID=scs_ks, room_temperature=room_temperature, scs=scs, status_min_exhaust_air_temperature=status_min_exhaust_air_temperature, status_compressor=status_compressor, outside_air_temperature=outside_air_temperature, status_min_supply_air_temperature=status_min_supply_air_temperature)
