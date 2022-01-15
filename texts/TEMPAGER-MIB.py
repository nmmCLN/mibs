#
# PySNMP MIB module TEMPAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/TEMPAGER-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:09:43 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, ObjectIdentity, Gauge32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, MibIdentifier, NotificationType, Unsigned32, NotificationType, Integer32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "ObjectIdentity", "Gauge32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "MibIdentifier", "NotificationType", "Unsigned32", "NotificationType", "Integer32", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
tempager = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 1))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 1, 2))
thresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1))
tempreading1c = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading1c.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading1c.setDescription('Temperature Sensor 1 (Celsius)')
tempreading2c = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading2c.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading2c.setDescription('Temperature Sensor 2 (Celsius)')
tempreading3c = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading3c.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading3c.setDescription('Temperature Sensor 3 (Celsius)')
tempreading4c = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading4c.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading4c.setDescription('Temperature Sensor 4 (Celsius)')
tempreading1f = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading1f.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading1f.setDescription('Temperature Sensor 1 (Fahrenheit)')
tempreading2f = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading2f.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading2f.setDescription('Temperature Sensor 2 (Fahrenheit)')
tempreading3f = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading3f.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading3f.setDescription('Temperature Sensor 3 (Fahrenheit)')
tempreading4f = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempreading4f.setStatus('mandatory')
if mibBuilder.loadTexts: tempreading4f.setDescription('Temperature Sensor 4 (Fahrenheit)')
alarmtemp1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmtemp1.setStatus('mandatory')
if mibBuilder.loadTexts: alarmtemp1.setDescription('Alarm for temperature 1\n\t\t\t0 = temperature OK\n\t\t\t1 = temperature too high\n\t\t\t2 = temperature too low')
alarmtemp2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmtemp2.setStatus('mandatory')
if mibBuilder.loadTexts: alarmtemp2.setDescription('Alarm for temperature 2\n\t\t\t0 = temperature OK\n\t\t\t1 = temperature too high\n\t\t\t2 = temperature too low')
alarmtemp3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmtemp3.setStatus('mandatory')
if mibBuilder.loadTexts: alarmtemp3.setDescription('Alarm for temperature 3\n\t\t\t0 = temperature OK\n\t\t\t1 = temperature too high\n\t\t\t2 = temperature too low')
alarmtemp4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmtemp4.setStatus('mandatory')
if mibBuilder.loadTexts: alarmtemp4.setDescription('Alarm for temperature 4\n\t\t\t0 = temperature OK\n\t\t\t1 = temperature too high\n\t\t\t2 = temperature too low')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
if mibBuilder.loadTexts: alarmmessage.setDescription('Message string to send with trap messages')
upperlimit1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperlimit1.setStatus('mandatory')
if mibBuilder.loadTexts: upperlimit1.setDescription('High temperature threshold for temperature sensor 1')
lowerlimit1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerlimit1.setStatus('mandatory')
if mibBuilder.loadTexts: lowerlimit1.setDescription('Low temperature threshold for temperature sensor 1')
upperlimit2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperlimit2.setStatus('mandatory')
if mibBuilder.loadTexts: upperlimit2.setDescription('High temperature threshold for temperature sensor 2')
lowerlimit2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerlimit2.setStatus('mandatory')
if mibBuilder.loadTexts: lowerlimit2.setDescription('Low temperature threshold for temperature sensor 2')
upperlimit3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperlimit3.setStatus('mandatory')
if mibBuilder.loadTexts: upperlimit3.setDescription('High temperature threshold for temperature sensor 3')
lowerlimit3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerlimit3.setStatus('mandatory')
if mibBuilder.loadTexts: lowerlimit3.setDescription('Low temperature threshold for temperature sensor 3')
upperlimit4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperlimit4.setStatus('mandatory')
if mibBuilder.loadTexts: upperlimit4.setDescription('High temperature threshold for temperature sensor 4')
lowerlimit4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerlimit4.setStatus('mandatory')
if mibBuilder.loadTexts: lowerlimit4.setDescription('Low temperature threshold for temperature sensor 4')
alarmstart1_t4 = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 1) + (0,1)).setLabel("alarmstart1-t4").setObjects(("TEMPAGER-MIB", "alarmmessage"), ("TEMPAGER-MIB", "tempreading1c"), ("TEMPAGER-MIB", "tempreading1f"))
if mibBuilder.loadTexts: alarmstart1_t4.setDescription('A alarmstart1 trap signifies that the current\n\t\t\ttemperature on sensor 1 is outside the \n\t\t\tdefined high or low threshold.')
tempager_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 1) + (0,2)).setLabel("tempager-snmp-trap").setObjects(("TEMPAGER-MIB", "alarmmessage"), ("TEMPAGER-MIB", "tempreading1c"), ("TEMPAGER-MIB", "tempreading1f"), ("TEMPAGER-MIB", "tempreading2c"), ("TEMPAGER-MIB", "tempreading2f"), ("TEMPAGER-MIB", "tempreading3c"), ("TEMPAGER-MIB", "tempreading3f"), ("TEMPAGER-MIB", "tempreading4c"), ("TEMPAGER-MIB", "tempreading4f"))
if mibBuilder.loadTexts: tempager_snmp_trap.setDescription('A tempager-snmp-trap indicates that an alarm\n\t\t\tcondition has occurred on the sensor inidcated\n\t\t\tby the alarmmessage variable.')
alarmstart2_t4 = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 1) + (0,3)).setLabel("alarmstart2-t4").setObjects(("TEMPAGER-MIB", "alarmmessage"), ("TEMPAGER-MIB", "tempreading2c"), ("TEMPAGER-MIB", "tempreading2f"))
if mibBuilder.loadTexts: alarmstart2_t4.setDescription('A alarmstart2 trap signifies that the current\n\t\t\ttemperature on sensor 2 is outside the \n\t\t\tdefined high or low threshold.')
alarmclear2_t4 = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 1) + (0,4)).setLabel("alarmclear2-t4").setObjects(("TEMPAGER-MIB", "alarmmessage"), ("TEMPAGER-MIB", "tempreading2c"), ("TEMPAGER-MIB", "tempreading2f"))
if mibBuilder.loadTexts: alarmclear2_t4.setDescription('A alarmclear2 trap signifies that the current\n\t\t\ttemperature on sensor 2 has returned to a \n\t\t\tnormal condition and is within the defined \n\t\t\thigh or low threshold.')
alarmstart3_t4 = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 1) + (0,5)).setLabel("alarmstart3-t4").setObjects(("TEMPAGER-MIB", "alarmmessage"), ("TEMPAGER-MIB", "tempreading3c"), ("TEMPAGER-MIB", "tempreading3f"))
if mibBuilder.loadTexts: alarmstart3_t4.setDescription('A alarmstart3 trap signifies that the current\n\t\t\ttemperature on sensor 3 is outside the \n\t\t\tdefined high or low threshold.')
alarmclear3_t4 = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 1) + (0,6)).setLabel("alarmclear3-t4").setObjects(("TEMPAGER-MIB", "alarmmessage"), ("TEMPAGER-MIB", "tempreading3c"), ("TEMPAGER-MIB", "tempreading3f"))
if mibBuilder.loadTexts: alarmclear3_t4.setDescription('A alarmclear3 trap signifies that the current\n\t\t\ttemperature on sensor 3 has returned to a \n\t\t\tnormal condition and is within the defined \n\t\t\thigh or low threshold.')
alarmstart4_t4 = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 1) + (0,7)).setLabel("alarmstart4-t4").setObjects(("TEMPAGER-MIB", "alarmmessage"), ("TEMPAGER-MIB", "tempreading4c"), ("TEMPAGER-MIB", "tempreading4f"))
if mibBuilder.loadTexts: alarmstart4_t4.setDescription('A alarmstart4 trap signifies that the current\n\t\t\ttemperature on sensor 4 is outside the \n\t\t\tdefined high or low threshold.')
alarmclear4_t4 = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 1) + (0,8)).setLabel("alarmclear4-t4").setObjects(("TEMPAGER-MIB", "alarmmessage"), ("TEMPAGER-MIB", "tempreading4c"), ("TEMPAGER-MIB", "tempreading4f"))
if mibBuilder.loadTexts: alarmclear4_t4.setDescription('A alarmclear4 trap signifies that the current\n\t\t\ttemperature on sensor 4 has returned to a \n\t\t\tnormal condition and is within the defined \n\t\t\thigh or low threshold.')
mibBuilder.exportSymbols("TEMPAGER-MIB", lowerlimit2=lowerlimit2, alarmclear3_t4=alarmclear3_t4, alarmstart4_t4=alarmstart4_t4, lowerlimit1=lowerlimit1, alarmtemp2=alarmtemp2, upperlimit2=upperlimit2, products=products, alarmtemp4=alarmtemp4, sensors=sensors, tempreading2c=tempreading2c, alarmclear2_t4=alarmclear2_t4, tempager=tempager, temperature=temperature, alarmclear4_t4=alarmclear4_t4, alarmstart2_t4=alarmstart2_t4, thresholds=thresholds, alarmmessage=alarmmessage, alarmtemp3=alarmtemp3, upperlimit1=upperlimit1, tempager_snmp_trap=tempager_snmp_trap, tempreading3c=tempreading3c, alarmtemp1=alarmtemp1, avtech=avtech, upperlimit4=upperlimit4, alarmstart3_t4=alarmstart3_t4, traps=traps, tempreading1c=tempreading1c, tempreading4c=tempreading4c, tempreading1f=tempreading1f, alarmstart1_t4=alarmstart1_t4, tempreading3f=tempreading3f, upperlimit3=upperlimit3, tempreading4f=tempreading4f, tempreading2f=tempreading2f, lowerlimit4=lowerlimit4, lowerlimit3=lowerlimit3)
