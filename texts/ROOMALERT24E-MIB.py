#
# PySNMP MIB module ROOMALERT24E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERT24E-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:47 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, Integer32, Bits, Counter64, TimeTicks, Unsigned32, iso, NotificationType, ObjectIdentity, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Integer32", "Bits", "Counter64", "TimeTicks", "Unsigned32", "iso", "NotificationType", "ObjectIdentity", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
roomalert24e = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 2))
internal = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1))
humidity = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 2))
heat_index = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3)).setLabel("heat-index")
digital = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2))
digital_sen1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1)).setLabel("digital-sen1")
digital_sen2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2)).setLabel("digital-sen2")
digital_sen3 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3)).setLabel("digital-sen3")
digital_sen4 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4)).setLabel("digital-sen4")
digital_sen5 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5)).setLabel("digital-sen5")
digital_sen6 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6)).setLabel("digital-sen6")
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3))
internal_tempf = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempf").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempf.setStatus('mandatory')
if mibBuilder.loadTexts: internal_tempf.setDescription('The internal temperature reading in Fahrenheit. Because the SNMP Protocol does not support floating point numbers, values are scaled by 100 and should be divided by 100 to get the actual value.')
internal_tempc = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempc").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempc.setStatus('mandatory')
if mibBuilder.loadTexts: internal_tempc.setDescription('The internal temperature reading in Celsius. Because the SNMP Protocol does not support floating point numbers, values are scaled by 100 and should be divided by 100 to get the actual value.')
internal_humidity = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-humidity").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_humidity.setStatus('mandatory')
if mibBuilder.loadTexts: internal_humidity.setDescription('The internal relative humidity reading in %RH. Because the SNMP Protocol does not support floating point numbers, values are scaled by 100 and should be divided by 100 to get the actual value.')
internal_heat_index = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-heat-index").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_heat_index.setStatus('mandatory')
if mibBuilder.loadTexts: internal_heat_index.setDescription('The internal heat index reading in Fahrenheit. Because the SNMP Protocol does not support floating point numbers, values are scaled by 100 and should be divided by 100 to get the actual value.')
internal_heat_indexc = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-heat-indexc").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_heat_indexc.setStatus('mandatory')
if mibBuilder.loadTexts: internal_heat_indexc.setDescription('The internal heat index reading in Celsius. Because the SNMP Protocol does not support floating point numbers, values are scaled by 100 and should be divided by 100 to get the actual value.')
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen1_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen2_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen3_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen3_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen3_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen3_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen3_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen4_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen4_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen4_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen4_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen4_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen4_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen4_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen4_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen4_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen4_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen5_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen5_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen5_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen5_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen5_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen5_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen5_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen5_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen5_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen5_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen6_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen6_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen6_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen6_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen6_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen6_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen6_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen6_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen6_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen6_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
switch_sen1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen1.setDescription('The reading for switch sensor 1 (0 = OPEN, 1 = CLOSED).')
switch_sen2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen2.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen2.setDescription('The reading for switch sensor 2 (0 = OPEN, 1 = CLOSED).')
switch_sen3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen3").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen3.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen3.setDescription('The reading for switch sensor 3 (0 = OPEN, 1 = CLOSED).')
switch_sen4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen4").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen4.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen4.setDescription('The reading for switch sensor 4 (0 = OPEN, 1 = CLOSED).')
switch_sen5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen5").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen5.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen5.setDescription('The reading for switch sensor 5 (0 = OPEN, 1 = CLOSED).')
switch_sen6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen6").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen6.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen6.setDescription('The reading for switch sensor 6 (0 = OPEN, 1 = CLOSED).')
switch_sen7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen7").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen7.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen7.setDescription('The reading for switch sensor 7 (0 = OPEN, 1 = CLOSED).')
switch_sen8 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen8").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen8.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen8.setDescription('The reading for switch sensor 8 (0 = OPEN, 1 = CLOSED).')
switch_sen9 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen9").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen9.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen9.setDescription('The reading for switch sensor 9 (0 = OPEN, 1 = CLOSED).')
switch_sen10 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen10").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen10.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen10.setDescription('The reading for switch sensor 10 (0 = OPEN, 1 = CLOSED).')
switch_sen11 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen11").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen11.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen11.setDescription('The reading for switch sensor 11 (0 = OPEN, 1 = CLOSED).')
switch_sen12 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen12").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen12.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen12.setDescription('The reading for switch sensor 12 (0 = OPEN, 1 = CLOSED).')
switch_sen13 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen13").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen13.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen13.setDescription('The reading for switch sensor 13 (0 = OPEN, 1 = CLOSED).')
switch_sen14 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen14").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen14.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen14.setDescription('The reading for switch sensor 14 (0 = OPEN, 1 = CLOSED).')
switch_sen15 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen15").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen15.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen15.setDescription('The reading for switch sensor 15 (0 = OPEN, 1 = CLOSED).')
switch_sen16 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen16").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen16.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen16.setDescription('The reading for switch sensor 16 (0 = OPEN, 1 = CLOSED).')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
if mibBuilder.loadTexts: alarmmessage.setDescription('Last Alarm Message')
tempalarm1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,1)).setLabel("tempalarm1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempalarm1_24e.setDescription('A tempalarm1 trap signifies that the current\n\t\t\ttemperature on external sensor 1 is outside the \n\t\t\tdefined high or low threshold.')
room_alert_24e_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,2)).setLabel("room-alert-24e-snmp-trap").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: room_alert_24e_snmp_trap.setDescription('A room-alert-24e-snmp-trap indicates that an alarm\n\t\t\tcondition has occurred on the sensor indicated\n\t\t\tby the alarmmessage variable.')
tempalarm2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,3)).setLabel("tempalarm2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempalarm2_24e.setDescription('A tempalarm2 trap signifies that the current\n\t\t\ttemperature on external sensor 2 is outside the \n\t\t\tdefined high or low threshold.')
tempclear2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,4)).setLabel("tempclear2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempclear2_24e.setDescription('A tempclear2 trap signifies that the current\n\t\t\ttemperature on external sensor 2 has returned to\n\t\t\ta normal condition and is within the defined \n\t\t\thigh or low threshold.')
tempalarm3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,5)).setLabel("tempalarm3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempalarm3_24e.setDescription('A tempalarm3 trap signifies that the current\n\t\t\ttemperature on external sensor 3 is outside the \n\t\t\tdefined high or low threshold.')
tempclear3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,6)).setLabel("tempclear3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempclear3_24e.setDescription('A tempclear3 trap signifies that the current\n\t\t\ttemperature on external sensor 3 has returned to\n\t\t\ta normal condition and is within the defined \n\t\t\thigh or low threshold.')
humidityalarm1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,7)).setLabel("humidityalarm1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityalarm1_24e.setDescription('A humidityalarm1 trap signifies that the current\n\t\t\thumidity on external sensor 1 is outside the \n\t\t\tdefined high or low threshold.')
humidityclear1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,8)).setLabel("humidityclear1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityclear1_24e.setDescription('A humidityclear1 trap signifies that the current\n\t\t\thumidity on external sensor 1 has returned to\n\t\t\ta normal condition and is within the defined \n\t\t\thigh or low threshold.')
humidityalarm2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,9)).setLabel("humidityalarm2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityalarm2_24e.setDescription('A humidityalarm2 trap signifies that the current\n\t\t\thumidity on external sensor 2 is outside the \n\t\t\tdefined high or low threshold.')
humidityclear2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,10)).setLabel("humidityclear2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityclear2_24e.setDescription('A humidityclear2 trap signifies that the current\n\t\t\thumidity on external sensor 2 has returned to\n\t\t\ta normal condition and is within the defined \n\t\t\thigh or low threshold.')
humidityalarm3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,11)).setLabel("humidityalarm3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityalarm3_24e.setDescription('A humidityalarm3 trap signifies that the current\n\t\t\thumidity on external sensor 3 is outside the \n\t\t\tdefined high or low threshold.')
humidityclear3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,12)).setLabel("humidityclear3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityclear3_24e.setDescription('A humidityclear3 trap signifies that the current\n\t\t\thumidity on external sensor 3 has returned to\n\t\t\ta normal condition and is within the defined \n\t\t\thigh or low threshold.')
switchalarm1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,13)).setLabel("switchalarm1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm1_24e.setDescription('A switchalarm1 trap signifies that switch sensor 1\n\t\t\tis in an alarm state.')
switchclear1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,14)).setLabel("switchclear1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear1_24e.setDescription('A switchclear1 trap signifies that the switch sensor 1\n\t\t\thas returned to a normal state.')
switchalarm2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,15)).setLabel("switchalarm2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm2_24e.setDescription('A switchalarm2 trap signifies that switch sensor 2\n\t\t\tis in an alarm state.')
switchclear2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,16)).setLabel("switchclear2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear2_24e.setDescription('A switchclear2 trap signifies that the switch sensor 2\n\t\t\thas returned to a normal state.')
switchalarm3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,17)).setLabel("switchalarm3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm3_24e.setDescription('A switchalarm1 trap signifies that switch sensor 1\n\t\t\tis in an alarm state.')
switchclear3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,18)).setLabel("switchclear3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear3_24e.setDescription('A switchclear3 trap signifies that the switch sensor 3\n\t\t\thas returned to a normal state.')
switchalarm4_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,19)).setLabel("switchalarm4-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm4_24e.setDescription('A switchalarm4 trap signifies that switch sensor 4\n\t\t\tis in an alarm state.')
switchclear4_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,20)).setLabel("switchclear4-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear4_24e.setDescription('A switchclear4 trap signifies that the switch sensor 4\n\t\t\thas returned to a normal state.')
switchalarm5_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,21)).setLabel("switchalarm5-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm5_24e.setDescription('A switchalarm5 trap signifies that switch sensor 5\n\t\t\tis in an alarm state.')
switchclear5_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,22)).setLabel("switchclear5-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear5_24e.setDescription('A switchclear5 trap signifies that the switch sensor 5\n\t\t\thas returned to a normal state.')
switchalarm6_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,23)).setLabel("switchalarm6-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm6_24e.setDescription('A switchalarm6 trap signifies that switch sensor 6\n\t\t\tis in an alarm state.')
switchclear6_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,24)).setLabel("switchclear6-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear6_24e.setDescription('A switchclear6 trap signifies that the switch sensor 6\n\t\t\thas returned to a normal state.')
switchalarm7_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,25)).setLabel("switchalarm7-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm7_24e.setDescription('A switchalarm7 trap signifies that switch sensor 7\n\t\t\tis in an alarm state.')
switchclear7_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,26)).setLabel("switchclear7-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear7_24e.setDescription('A switchclear7 trap signifies that the switch sensor 7\n\t\t\thas returned to a normal state.')
switchalarm8_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,27)).setLabel("switchalarm8-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm8_24e.setDescription('A switchalarm8 trap signifies that switch sensor 8\n\t\t\tis in an alarm state.')
switchclear8_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,28)).setLabel("switchclear8-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear8_24e.setDescription('A switchclear8 trap signifies that the switch sensor 8\n\t\t\thas returned to a normal state.')
mibBuilder.exportSymbols("ROOMALERT24E-MIB", digital_sen5_2=digital_sen5_2, switchalarm7_24e=switchalarm7_24e, switchalarm2_24e=switchalarm2_24e, digital_sen3=digital_sen3, digital_sen3_5=digital_sen3_5, switch=switch, room_alert_24e_snmp_trap=room_alert_24e_snmp_trap, digital_sen1=digital_sen1, humidity=humidity, switchalarm4_24e=switchalarm4_24e, digital_sen5_1=digital_sen5_1, internal=internal, digital_sen1_4=digital_sen1_4, switch_sen10=switch_sen10, switchclear4_24e=switchclear4_24e, digital_sen4_2=digital_sen4_2, switch_sen2=switch_sen2, switchalarm5_24e=switchalarm5_24e, humidityclear2_24e=humidityclear2_24e, tempalarm1_24e=tempalarm1_24e, switchclear2_24e=switchclear2_24e, internal_heat_indexc=internal_heat_indexc, digital_sen1_1=digital_sen1_1, switch_sen12=switch_sen12, switch_sen4=switch_sen4, avtech=avtech, switch_sen6=switch_sen6, internal_humidity=internal_humidity, humidityclear3_24e=humidityclear3_24e, digital_sen1_2=digital_sen1_2, internal_heat_index=internal_heat_index, switch_sen7=switch_sen7, tempalarm2_24e=tempalarm2_24e, digital_sen3_3=digital_sen3_3, digital_sen2_5=digital_sen2_5, tempclear3_24e=tempclear3_24e, switch_sen1=switch_sen1, switch_sen8=switch_sen8, roomalert24e=roomalert24e, digital_sen3_2=digital_sen3_2, digital_sen5_5=digital_sen5_5, digital_sen5_4=digital_sen5_4, switch_sen13=switch_sen13, switchclear8_24e=switchclear8_24e, digital_sen3_4=digital_sen3_4, alarmmessage=alarmmessage, digital_sen2_3=digital_sen2_3, tempclear2_24e=tempclear2_24e, humidityalarm3_24e=humidityalarm3_24e, digital=digital, digital_sen6=digital_sen6, digital_sen5_3=digital_sen5_3, sensors=sensors, digital_sen6_3=digital_sen6_3, switch_sen16=switch_sen16, digital_sen1_5=digital_sen1_5, digital_sen1_3=digital_sen1_3, digital_sen4=digital_sen4, digital_sen4_5=digital_sen4_5, switchalarm8_24e=switchalarm8_24e, switchclear3_24e=switchclear3_24e, switch_sen9=switch_sen9, switchclear7_24e=switchclear7_24e, switch_sen15=switch_sen15, humidityclear1_24e=humidityclear1_24e, switchclear1_24e=switchclear1_24e, digital_sen6_2=digital_sen6_2, switchclear5_24e=switchclear5_24e, digital_sen2_1=digital_sen2_1, switch_sen3=switch_sen3, digital_sen6_5=digital_sen6_5, humidityalarm1_24e=humidityalarm1_24e, digital_sen2_4=digital_sen2_4, internal_tempc=internal_tempc, digital_sen6_4=digital_sen6_4, digital_sen4_3=digital_sen4_3, tempalarm3_24e=tempalarm3_24e, switchclear6_24e=switchclear6_24e, digital_sen3_1=digital_sen3_1, digital_sen2=digital_sen2, products=products, switchalarm1_24e=switchalarm1_24e, switch_sen11=switch_sen11, internal_tempf=internal_tempf, switchalarm6_24e=switchalarm6_24e, digital_sen5=digital_sen5, switch_sen14=switch_sen14, digital_sen4_4=digital_sen4_4, digital_sen6_1=digital_sen6_1, heat_index=heat_index, digital_sen4_1=digital_sen4_1, switchalarm3_24e=switchalarm3_24e, switch_sen5=switch_sen5, traps=traps, digital_sen2_2=digital_sen2_2, humidityalarm2_24e=humidityalarm2_24e, temperature=temperature)
