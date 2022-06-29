#
# PySNMP MIB module UPS2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/UPS2-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:56 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ctUPS, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctUPS")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, TimeTicks, IpAddress, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
upsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 1))
upsId = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2))
upsBattery = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3))
upsInput = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4))
upsOutput = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5))
upsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6))
upsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7))
upsExtMeas = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8))
upsAddlFuncs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9))
upsNumUPSs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsNumUPSs.setStatus('mandatory')
upsIdTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1), )
if mibBuilder.loadTexts: upsIdTable.setStatus('mandatory')
upsIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1), ).setIndexNames((0, "UPS2-MIB", "upsIndex"))
if mibBuilder.loadTexts: upsIdEntry.setStatus('mandatory')
upsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsIndex.setStatus('mandatory')
upsName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsName.setStatus('mandatory')
upsModelType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("smartUps250", 1), ("smartUps400", 2), ("smartUps600", 3), ("smartUps900", 4), ("smartUps1250", 5), ("smartUps2000", 6), ("matrixUps3000", 7), ("matrixUps5000", 8), ("other", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsModelType.setStatus('mandatory')
upsFwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsFwVersion.setStatus('mandatory')
upsSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsSerialNumber.setStatus('mandatory')
upsManufDate = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsManufDate.setStatus('mandatory')
upsBatteryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1), )
if mibBuilder.loadTexts: upsBatteryTable.setStatus('mandatory')
upsBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1), ).setIndexNames((0, "UPS2-MIB", "upsIndex"))
if mibBuilder.loadTexts: upsBatteryEntry.setStatus('mandatory')
upsBatteryCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryCapacity.setStatus('mandatory')
upsBatteryVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryVoltage.setStatus('mandatory')
upsBatteryTest = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("initiateTest", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsBatteryTest.setStatus('mandatory')
upsBatteryTestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("batteryOK", 1), ("batteryBad", 2), ("noRecentTest", 3), ("invalidTestDueToOverload", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsBatteryTestResult.setStatus('mandatory')
upsRunTimeCalibration = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("performTest", 1), ("abortTest", 2), ("testInProgress", 3), ("testNotInProgress", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsRunTimeCalibration.setStatus('mandatory')
upsEstimatedRunTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsEstimatedRunTimeRemaining.setStatus('mandatory')
upsTransferCause = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noTransfer", 1), ("selfTest", 2), ("inputLineSpike", 3), ("inputLowVoltage", 4), ("inputHighVoltage", 5), ("inputLineFrequencyBad", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsTransferCause.setStatus('mandatory')
upsBatteryTestTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("twoWeeks", 1), ("oneWeek", 2), ("startupOnly", 3), ("off", 4))).clone('twoWeeks')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsBatteryTestTime.setStatus('mandatory')
upsLowBatteryWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("twoMinutes", 1), ("fiveMinutes", 2), ("sevenMinutes", 3), ("tenMinutes", 4))).clone('twoMinutes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsLowBatteryWarning.setStatus('mandatory')
upsInputTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1), )
if mibBuilder.loadTexts: upsInputTable.setStatus('mandatory')
upsInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1), ).setIndexNames((0, "UPS2-MIB", "upsIndex"))
if mibBuilder.loadTexts: upsInputEntry.setStatus('mandatory')
upsInputUtilityVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vac100", 1), ("vac120", 2), ("vac208", 3), ("vac220", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputUtilityVoltage.setStatus('mandatory')
upsInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputVoltage.setStatus('mandatory')
upsInputFailureSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("high", 1), ("medium", 2), ("low", 3), ("auto", 4))).clone('high')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsInputFailureSensitivity.setStatus('mandatory')
upsInputMaxVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputMaxVoltage.setStatus('mandatory')
upsInputMinVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputMinVoltage.setStatus('mandatory')
upsInputFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsInputFrequency.setStatus('mandatory')
upsOutputTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1), )
if mibBuilder.loadTexts: upsOutputTable.setStatus('mandatory')
upsOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1, 1), ).setIndexNames((0, "UPS2-MIB", "upsIndex"))
if mibBuilder.loadTexts: upsOutputEntry.setStatus('mandatory')
upsOutputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputVoltage.setStatus('mandatory')
upsOutputUtilityVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vac225", 1), ("vac230", 2), ("vac240", 3), ("vac220", 4))).clone('vac225')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsOutputUtilityVoltage.setStatus('mandatory')
upsOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsOutputPower.setStatus('mandatory')
upsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1), )
if mibBuilder.loadTexts: upsStatusTable.setStatus('mandatory')
upsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1, 1), ).setIndexNames((0, "UPS2-MIB", "upsIndex"))
if mibBuilder.loadTexts: upsStatusEntry.setStatus('mandatory')
upsStatusOperational = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsStatusOperational.setStatus('mandatory')
upsStatusFault = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsStatusFault.setStatus('mandatory')
upsStatusTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsStatusTemp.setStatus('mandatory')
upsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7, 1), )
if mibBuilder.loadTexts: upsConfigTable.setStatus('mandatory')
upsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7, 1, 1), ).setIndexNames((0, "UPS2-MIB", "upsIndex"))
if mibBuilder.loadTexts: upsConfigEntry.setStatus('mandatory')
upsConfigAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("uponUtilityFailure", 1), ("thirtySecondsAfterUtilityFailure", 2), ("lowBatteryOnly", 3), ("noAudibleAlarm", 4))).clone('uponUtilityFailure')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigAlarm.setStatus('mandatory')
upsConfigRestoreDefaults = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("restoreDefaults", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsConfigRestoreDefaults.setStatus('mandatory')
upsExtMeasTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1), )
if mibBuilder.loadTexts: upsExtMeasTable.setStatus('mandatory')
upsExtMeasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1), ).setIndexNames((0, "UPS2-MIB", "upsIndex"))
if mibBuilder.loadTexts: upsExtMeasEntry.setStatus('mandatory')
upsExtMeasFwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtMeasFwVersion.setStatus('mandatory')
upsExtMeasTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtMeasTemp.setStatus('mandatory')
upsExtMeasHumidity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtMeasHumidity.setStatus('mandatory')
upsExtMeasAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsExtMeasAlarmStatus.setStatus('mandatory')
upsExtMeasMaxTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ninetyDegreesF", 1), ("oneHundredFifteenDegreesF", 2), ("oneHundredThirtyDegreesF", 3), ("oneHundredSeventyFiveDegreesF", 4))).clone('ninetyDegreesF')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasMaxTemp.setStatus('mandatory')
upsExtMeasMinTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("fortyDegreesF", 1), ("fiftyDegreesF", 2), ("fiftyEightDegreesF", 3), ("sixtyFiveDegreesF", 4))).clone('fortyDegreesF')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasMinTemp.setStatus('mandatory')
upsExtMeasMaxHumidity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("seventyPercent", 1), ("eightyPercent", 2), ("eightyFivePercent", 3), ("ninetyPercent", 4))).clone('seventyPercent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasMaxHumidity.setStatus('mandatory')
upsExtMeasMinHumidity = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tenPercent", 1), ("twentyPercent", 2), ("thirtyPercent", 3), ("fortyPercent", 4))).clone('tenPercent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasMinHumidity.setStatus('mandatory')
upsExtMeasContact1AlarmControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasContact1AlarmControl.setStatus('mandatory')
upsExtMeasContact2AlarmControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasContact2AlarmControl.setStatus('mandatory')
upsExtMeasContact3AlarmControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasContact3AlarmControl.setStatus('mandatory')
upsExtMeasContact4AlarmControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasContact4AlarmControl.setStatus('mandatory')
upsExtMeasMaxTempAlarmControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasMaxTempAlarmControl.setStatus('mandatory')
upsExtMeasMinTempAlarmControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasMinTempAlarmControl.setStatus('mandatory')
upsExtMeasMaxHumidityAlarmControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasMaxHumidityAlarmControl.setStatus('mandatory')
upsExtMeasMinHumidityAlarmControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 8, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsExtMeasMinHumidityAlarmControl.setStatus('mandatory')
upsAddlFuncsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1), )
if mibBuilder.loadTexts: upsAddlFuncsTable.setStatus('mandatory')
upsAddlFuncsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1), ).setIndexNames((0, "UPS2-MIB", "upsIndex"))
if mibBuilder.loadTexts: upsAddlFuncsEntry.setStatus('mandatory')
upsAddlFuncsNumBatteryPacks = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAddlFuncsNumBatteryPacks.setStatus('mandatory')
upsAddlFuncsNumBadBatteryPacks = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAddlFuncsNumBadBatteryPacks.setStatus('mandatory')
upsAddlFuncsOutputCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAddlFuncsOutputCurrent.setStatus('mandatory')
upsAddlFuncsOutputApparentPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAddlFuncsOutputApparentPower.setStatus('mandatory')
upsAddlFuncsStatusOperational = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAddlFuncsStatusOperational.setStatus('mandatory')
upsAddlFuncsStatusFault = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upsAddlFuncsStatusFault.setStatus('mandatory')
upsAddlFuncsConfigPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsAddlFuncsConfigPassword.setStatus('mandatory')
upsAddlFuncsConfigDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("disableUps", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsAddlFuncsConfigDisable.setStatus('mandatory')
upsAddlFuncsConfigBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10, 9, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bypassMode", 1), ("exitBypassMode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upsAddlFuncsConfigBypass.setStatus('mandatory')
mibBuilder.exportSymbols("UPS2-MIB", upsExtMeasFwVersion=upsExtMeasFwVersion, upsExtMeasMinTempAlarmControl=upsExtMeasMinTempAlarmControl, upsIndex=upsIndex, upsExtMeasMaxHumidity=upsExtMeasMaxHumidity, upsInputFrequency=upsInputFrequency, upsId=upsId, upsInputTable=upsInputTable, upsExtMeasMaxTempAlarmControl=upsExtMeasMaxTempAlarmControl, upsNumUPSs=upsNumUPSs, upsSerialNumber=upsSerialNumber, upsBattery=upsBattery, upsIdTable=upsIdTable, upsExtMeasContact4AlarmControl=upsExtMeasContact4AlarmControl, upsInput=upsInput, upsConfig=upsConfig, upsAddlFuncs=upsAddlFuncs, upsOutputEntry=upsOutputEntry, upsStatusFault=upsStatusFault, upsAddlFuncsEntry=upsAddlFuncsEntry, upsAddlFuncsConfigBypass=upsAddlFuncsConfigBypass, upsInputMinVoltage=upsInputMinVoltage, upsIdEntry=upsIdEntry, upsAddlFuncsNumBatteryPacks=upsAddlFuncsNumBatteryPacks, upsExtMeasMinHumidityAlarmControl=upsExtMeasMinHumidityAlarmControl, upsEstimatedRunTimeRemaining=upsEstimatedRunTimeRemaining, upsInputUtilityVoltage=upsInputUtilityVoltage, upsOutputPower=upsOutputPower, upsAddlFuncsNumBadBatteryPacks=upsAddlFuncsNumBadBatteryPacks, upsConfigAlarm=upsConfigAlarm, upsBatteryTest=upsBatteryTest, upsAddlFuncsTable=upsAddlFuncsTable, upsStatus=upsStatus, upsInputEntry=upsInputEntry, upsExtMeasTemp=upsExtMeasTemp, upsStatusEntry=upsStatusEntry, upsAddlFuncsStatusFault=upsAddlFuncsStatusFault, upsExtMeasMinTemp=upsExtMeasMinTemp, upsLowBatteryWarning=upsLowBatteryWarning, upsStatusOperational=upsStatusOperational, upsExtMeasContact2AlarmControl=upsExtMeasContact2AlarmControl, upsExtMeasHumidity=upsExtMeasHumidity, upsInputFailureSensitivity=upsInputFailureSensitivity, upsExtMeasTable=upsExtMeasTable, upsConfigTable=upsConfigTable, upsExtMeasMinHumidity=upsExtMeasMinHumidity, upsBatteryTestTime=upsBatteryTestTime, upsInputVoltage=upsInputVoltage, upsStatusTable=upsStatusTable, upsName=upsName, upsConfigEntry=upsConfigEntry, upsOutputVoltage=upsOutputVoltage, upsAddlFuncsOutputApparentPower=upsAddlFuncsOutputApparentPower, upsAddlFuncsStatusOperational=upsAddlFuncsStatusOperational, upsExtMeas=upsExtMeas, upsExtMeasContact3AlarmControl=upsExtMeasContact3AlarmControl, upsExtMeasMaxHumidityAlarmControl=upsExtMeasMaxHumidityAlarmControl, upsInputMaxVoltage=upsInputMaxVoltage, upsOutput=upsOutput, upsManufDate=upsManufDate, upsBatteryVoltage=upsBatteryVoltage, upsOutputTable=upsOutputTable, upsBatteryEntry=upsBatteryEntry, upsExtMeasMaxTemp=upsExtMeasMaxTemp, upsExtMeasAlarmStatus=upsExtMeasAlarmStatus, upsStatusTemp=upsStatusTemp, upsFwVersion=upsFwVersion, upsAddlFuncsConfigDisable=upsAddlFuncsConfigDisable, upsAddlFuncsOutputCurrent=upsAddlFuncsOutputCurrent, upsBatteryCapacity=upsBatteryCapacity, upsTransferCause=upsTransferCause, upsRunTimeCalibration=upsRunTimeCalibration, upsExtMeasEntry=upsExtMeasEntry, upsConfigRestoreDefaults=upsConfigRestoreDefaults, upsBatteryTestResult=upsBatteryTestResult, upsModelType=upsModelType, upsOutputUtilityVoltage=upsOutputUtilityVoltage, upsSystem=upsSystem, upsExtMeasContact1AlarmControl=upsExtMeasContact1AlarmControl, upsBatteryTable=upsBatteryTable, upsAddlFuncsConfigPassword=upsAddlFuncsConfigPassword)
