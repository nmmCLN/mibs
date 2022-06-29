#
# PySNMP MIB module T3610-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/comet/T3610-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:04:49 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Unsigned32, Integer32, IpAddress, enterprises, Bits, ObjectIdentity, NotificationType, Gauge32, iso, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Unsigned32", "Integer32", "IpAddress", "enterprises", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "iso", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

comet = MibIdentifier((1, 3, 6, 1, 4, 1, 22626))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1))
t3610 = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2))
values = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1))
pysmi_global = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2)).setLabel("global")
valuesInt = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3))
settings = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5))
tables = MibIdentifier((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6))
temp = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temp.setStatus('mandatory')
if mibBuilder.loadTexts: temp.setDescription('Temperature')
hum = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hum.setStatus('mandatory')
if mibBuilder.loadTexts: hum.setDescription('Relative humidity')
compVal = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compVal.setStatus('mandatory')
if mibBuilder.loadTexts: compVal.setDescription('Computed value')
tempAlarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: tempAlarm.setDescription('Alarm on Temperature; none, high, low')
humAlarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: humAlarm.setDescription('Alarm on Relative humidity; none, high, low')
compValAlarm = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: compValAlarm.setDescription('Alarm on Computed value; none, high, low')
tempUnit = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempUnit.setStatus('mandatory')
if mibBuilder.loadTexts: tempUnit.setDescription('Temperature Unit')
humUnit = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humUnit.setStatus('mandatory')
if mibBuilder.loadTexts: humUnit.setDescription('Relative humidity Unit')
compValUnit = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValUnit.setStatus('mandatory')
if mibBuilder.loadTexts: compValUnit.setDescription('Computed value Unit')
tempMin = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempMin.setStatus('mandatory')
if mibBuilder.loadTexts: tempMin.setDescription('Minimal temperature')
humMin = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humMin.setStatus('mandatory')
if mibBuilder.loadTexts: humMin.setDescription('Minimal relative humidity')
compValMin = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValMin.setStatus('mandatory')
if mibBuilder.loadTexts: compValMin.setDescription('Minimal computed value')
tempMax = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempMax.setStatus('mandatory')
if mibBuilder.loadTexts: tempMax.setDescription('Maximal temperature')
humMax = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humMax.setStatus('mandatory')
if mibBuilder.loadTexts: humMax.setDescription('Maximal relative humidity')
compValMax = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValMax.setStatus('mandatory')
if mibBuilder.loadTexts: compValMax.setDescription('Maximal computed value')
sensorName = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 68))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorName.setStatus('mandatory')
if mibBuilder.loadTexts: sensorName.setDescription('Device name')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: serialNumber.setDescription('Serial number')
deviceType = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceType.setStatus('mandatory')
if mibBuilder.loadTexts: deviceType.setDescription('Device type')
tempInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempInt.setStatus('mandatory')
if mibBuilder.loadTexts: tempInt.setDescription('Temperature (value*10)')
humInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humInt.setStatus('mandatory')
if mibBuilder.loadTexts: humInt.setDescription('Relative humidity (value*10)')
compValInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValInt.setStatus('mandatory')
if mibBuilder.loadTexts: compValInt.setDescription('Computed value (value*10)')
tempAlarmInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempAlarmInt.setStatus('mandatory')
if mibBuilder.loadTexts: tempAlarmInt.setDescription('Alarm on Temperature; 0 - No, 1 - High, 2 - Low')
humAlarmInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humAlarmInt.setStatus('mandatory')
if mibBuilder.loadTexts: humAlarmInt.setDescription('Alarm on Relative humidity; 0 - No, 1 - High, 2 - Low')
compValAlarmInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValAlarmInt.setStatus('mandatory')
if mibBuilder.loadTexts: compValAlarmInt.setDescription('Alarm on Computed value; 0 - No, 1 - High, 2 - Low')
tempLowInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempLowInt.setStatus('mandatory')
if mibBuilder.loadTexts: tempLowInt.setDescription('Temperature Limit Low (value*10)')
tempHighInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHighInt.setStatus('mandatory')
if mibBuilder.loadTexts: tempHighInt.setDescription('Temperature Limit High (value*10)')
humLowInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humLowInt.setStatus('mandatory')
if mibBuilder.loadTexts: humLowInt.setDescription('Humidity Limit Low (value*10)')
humHighInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humHighInt.setStatus('mandatory')
if mibBuilder.loadTexts: humHighInt.setDescription('Humidity Limit High (value*10)')
compValLowInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValLowInt.setStatus('mandatory')
if mibBuilder.loadTexts: compValLowInt.setDescription('Computed value Limit Low (value*10)')
compValHighInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValHighInt.setStatus('mandatory')
if mibBuilder.loadTexts: compValHighInt.setDescription('Computed value Limit High (value*10)')
tempDelayInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempDelayInt.setStatus('mandatory')
if mibBuilder.loadTexts: tempDelayInt.setDescription('Temperature alaram delay [sec]')
humDelayInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humDelayInt.setStatus('mandatory')
if mibBuilder.loadTexts: humDelayInt.setDescription('Humidity alaram delay [sec]')
compValDelayInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValDelayInt.setStatus('mandatory')
if mibBuilder.loadTexts: compValDelayInt.setDescription('Computed value alaram delay [sec]')
tempHystInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHystInt.setStatus('mandatory')
if mibBuilder.loadTexts: tempHystInt.setDescription('Temperature hysteresis (value*10)')
humHystInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: humHystInt.setStatus('mandatory')
if mibBuilder.loadTexts: humHystInt.setDescription('Humidity hysteresis (value*10)')
compValHystInt = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: compValHystInt.setStatus('mandatory')
if mibBuilder.loadTexts: compValHystInt.setDescription('Computed value hysteresis (value*10)')
messageString = MibScalar((1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageString.setStatus('mandatory')
if mibBuilder.loadTexts: messageString.setDescription('Message giving more detailed information on alarms')
historyTable = MibTable((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1), )
if mibBuilder.loadTexts: historyTable.setStatus('mandatory')
if mibBuilder.loadTexts: historyTable.setDescription('Table of the history values')
historyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1), ).setIndexNames((0, "T3610-MIB", "histTemp"))
if mibBuilder.loadTexts: historyEntry.setStatus('optional')
if mibBuilder.loadTexts: historyEntry.setDescription('History values entries')
histTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histTemp.setStatus('mandatory')
if mibBuilder.loadTexts: histTemp.setDescription('Temperature reading')
histHum = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histHum.setStatus('mandatory')
if mibBuilder.loadTexts: histHum.setDescription('Humidity reading')
histCompVal = MibTableColumn((1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-5000, 20000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: histCompVal.setStatus('mandatory')
if mibBuilder.loadTexts: histCompVal.setDescription('Computed value reading')
trapTest = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,0)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapTest.setDescription('Testing trap, testing trap by TSensor software')
trapNTPError = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,1)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapNTPError.setDescription('Error on time synchronisation via NTP')
trapEmailErrLogin = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,2)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapEmailErrLogin.setDescription('SMTP error - unknown server')
trapEmailErrAuth = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,3)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapEmailErrAuth.setDescription('SMTP error - authentication error')
trapEmailErrSome = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,4)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapEmailErrSome.setDescription('SMTP error - error during communication with server, unexpected return code')
trapEmailErrSocket = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,5)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapEmailErrSocket.setDescription('SMTP error - socket error, server is not available')
trapEmailErrDNS = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,6)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapEmailErrDNS.setDescription('SMTP error - DNS error')
trapSOAPErrFile = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,7)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapSOAPErrFile.setDescription('SOAP error - file SOAP not found')
trapSOAPErrDNS = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,8)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapSOAPErrDNS.setDescription('SOAP error - DNS error')
trapSOAPErrSocket = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,9)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapSOAPErrSocket.setDescription('SOAP error - socket error, server is not available')
trapSOAPErrDelivery = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,10)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"))
if mibBuilder.loadTexts: trapSOAPErrDelivery.setDescription('SOAP error - delivery error, wrong return code from server')
trapTempHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,11)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "temp"), ("T3610-MIB", "tempAlarmInt"))
if mibBuilder.loadTexts: trapTempHighAlarm.setDescription('Trap for high alarm on temperature')
trapHumHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,12)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "hum"), ("T3610-MIB", "humAlarmInt"))
if mibBuilder.loadTexts: trapHumHighAlarm.setDescription('Trap for high alarm on relative humidity')
trapCompValHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,13)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "compVal"), ("T3610-MIB", "compValAlarmInt"))
if mibBuilder.loadTexts: trapCompValHighAlarm.setDescription('Trap for high alarm on computed value')
trapTempLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,21)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "temp"), ("T3610-MIB", "tempAlarmInt"))
if mibBuilder.loadTexts: trapTempLowAlarm.setDescription('Trap for low alarm on temperature')
trapHumLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,22)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "hum"), ("T3610-MIB", "humAlarmInt"))
if mibBuilder.loadTexts: trapHumLowAlarm.setDescription('Trap for low alarm on relative humidity')
trapCompValLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,23)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "compVal"), ("T3610-MIB", "compValAlarmInt"))
if mibBuilder.loadTexts: trapCompValLowAlarm.setDescription('Trap for low alarm on computed value')
trapTempClrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,31)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "temp"), ("T3610-MIB", "tempAlarmInt"))
if mibBuilder.loadTexts: trapTempClrAlarm.setDescription('Trap for clearing alarm on temperature')
trapHumClrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,32)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "hum"), ("T3610-MIB", "humAlarmInt"))
if mibBuilder.loadTexts: trapHumClrAlarm.setDescription('Trap for clearing alarm on relative humidity')
trapCompValClrAlarm = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,33)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "compVal"), ("T3610-MIB", "compValAlarmInt"))
if mibBuilder.loadTexts: trapCompValClrAlarm.setDescription('Trap for clearing alarm on computed value')
trapTempError = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,41)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "temp"), ("T3610-MIB", "tempAlarmInt"))
if mibBuilder.loadTexts: trapTempError.setDescription('Trap for error on temperature')
trapHumError = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,42)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "hum"), ("T3610-MIB", "humAlarmInt"))
if mibBuilder.loadTexts: trapHumError.setDescription('Trap for error on relative humidity')
trapCompValError = NotificationType((1, 3, 6, 1, 4, 1, 22626) + (0,43)).setObjects(("T3610-MIB", "sensorName"), ("T3610-MIB", "messageString"), ("T3610-MIB", "compVal"), ("T3610-MIB", "compValAlarmInt"))
if mibBuilder.loadTexts: trapCompValError.setDescription('Trap for error on computed value')
mibBuilder.exportSymbols("T3610-MIB", DisplayString=DisplayString, humAlarmInt=humAlarmInt, trapSOAPErrSocket=trapSOAPErrSocket, compValAlarmInt=compValAlarmInt, compValHighInt=compValHighInt, tempMax=tempMax, settings=settings, humHystInt=humHystInt, trapEmailErrDNS=trapEmailErrDNS, comet=comet, histHum=histHum, trapCompValClrAlarm=trapCompValClrAlarm, compValMin=compValMin, humAlarm=humAlarm, tempDelayInt=tempDelayInt, values=values, tempMin=tempMin, humUnit=humUnit, humHighInt=humHighInt, sensorName=sensorName, compValHystInt=compValHystInt, trapTest=trapTest, tempAlarm=tempAlarm, tempLowInt=tempLowInt, trapTempError=trapTempError, compValInt=compValInt, trapHumClrAlarm=trapHumClrAlarm, histTemp=histTemp, humDelayInt=humDelayInt, trapSOAPErrDelivery=trapSOAPErrDelivery, compValMax=compValMax, trapEmailErrSocket=trapEmailErrSocket, trapHumError=trapHumError, trapCompValError=trapCompValError, humInt=humInt, trapSOAPErrDNS=trapSOAPErrDNS, trapTempClrAlarm=trapTempClrAlarm, histCompVal=histCompVal, tempUnit=tempUnit, trapHumHighAlarm=trapHumHighAlarm, trapEmailErrLogin=trapEmailErrLogin, humMin=humMin, trapCompValHighAlarm=trapCompValHighAlarm, traps=traps, deviceType=deviceType, trapNTPError=trapNTPError, tempHystInt=tempHystInt, t3610=t3610, tables=tables, compValDelayInt=compValDelayInt, hum=hum, trapEmailErrAuth=trapEmailErrAuth, temp=temp, humMax=humMax, humLowInt=humLowInt, trapHumLowAlarm=trapHumLowAlarm, tempAlarmInt=tempAlarmInt, historyEntry=historyEntry, trapTempHighAlarm=trapTempHighAlarm, compValAlarm=compValAlarm, historyTable=historyTable, trapCompValLowAlarm=trapCompValLowAlarm, trapSOAPErrFile=trapSOAPErrFile, messageString=messageString, trapTempLowAlarm=trapTempLowAlarm, tempInt=tempInt, trapEmailErrSome=trapEmailErrSome, pysmi_global=pysmi_global, tempHighInt=tempHighInt, compValUnit=compValUnit, compValLowInt=compValLowInt, serialNumber=serialNumber, compVal=compVal, products=products, valuesInt=valuesInt)
