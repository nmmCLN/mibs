#
# PySNMP MIB module WTI-POWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wti/WTI-POWER-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:16:55 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Integer32, ModuleIdentity, Gauge32, TimeTicks, IpAddress, enterprises, Counter32, ObjectIdentity, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Integer32", "ModuleIdentity", "Gauge32", "TimeTicks", "IpAddress", "enterprises", "Counter32", "ObjectIdentity", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
westernTelematic = MibIdentifier((1, 3, 6, 1, 4, 1, 2634))
power = ModuleIdentity((1, 3, 6, 1, 4, 1, 2634, 3))
power.setRevisions(('2016-04-01 16:00',))
if mibBuilder.loadTexts: power.setLastUpdated('201604011600Z')
if mibBuilder.loadTexts: power.setOrganization('Western Telematic, Inc.')
systemTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 100))
plugTable = MibTable((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200), )
if mibBuilder.loadTexts: plugTable.setStatus('current')
plugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1), ).setIndexNames((0, "WTI-POWER-MIB", "plugIndex"))
if mibBuilder.loadTexts: plugEntry.setStatus('current')
plugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 80)))
if mibBuilder.loadTexts: plugIndex.setStatus('current')
plugID = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(9, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: plugID.setStatus('current')
plugStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: plugStatus.setStatus('current')
plugAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: plugAction.setStatus('current')
plugName = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: plugName.setStatus('current')
plugCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: plugCurrent.setStatus('current')
plugPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 200, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: plugPower.setStatus('current')
plugGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2634, 3, 100, 300), )
if mibBuilder.loadTexts: plugGroupTable.setStatus('current')
plugGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1), ).setIndexNames((0, "WTI-POWER-MIB", "plugGroupIndex"))
if mibBuilder.loadTexts: plugGroupEntry.setStatus('current')
plugGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 54)))
if mibBuilder.loadTexts: plugGroupIndex.setStatus('current')
plugGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: plugGroupName.setStatus('current')
plugGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: plugGroupAction.setStatus('current')
plugGroupCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: plugGroupCurrent.setStatus('current')
plugGroupPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 300, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: plugGroupPower.setStatus('current')
userTable = MibTable((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400), )
if mibBuilder.loadTexts: userTable.setStatus('current')
userEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1), ).setIndexNames((0, "WTI-POWER-MIB", "userIndex"))
if mibBuilder.loadTexts: userEntry.setStatus('current')
userIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)))
if mibBuilder.loadTexts: userIndex.setStatus('current')
userName = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userName.setStatus('current')
userPasswd = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userPasswd.setStatus('current')
userAccessLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userAccessLevel.setStatus('current')
userPortAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userPortAccess.setStatus('current')
userLocalAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userLocalAccess.setStatus('current')
userGroupAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 54))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userGroupAccess.setStatus('current')
userSerialAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userSerialAccess.setStatus('current')
userTelnetSshAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userTelnetSshAccess.setStatus('current')
userWebAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userWebAccess.setStatus('current')
userCurrentPowerMetering = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userCurrentPowerMetering.setStatus('current')
userCallbackNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userCallbackNum.setStatus('current')
userSubmit = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 100, 400, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userSubmit.setStatus('current')
environmentTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 200))
environmentUnitTable = MibTable((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10), )
if mibBuilder.loadTexts: environmentUnitTable.setStatus('current')
environmentUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1), ).setIndexNames((0, "WTI-POWER-MIB", "environmentUnitIndex"))
if mibBuilder.loadTexts: environmentUnitEntry.setStatus('current')
environmentUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)))
if mibBuilder.loadTexts: environmentUnitIndex.setStatus('current')
environmentUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitName.setStatus('current')
environmentUnitTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitTemperature.setStatus('current')
environmentUnitCurrentA = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitCurrentA.setStatus('current')
environmentUnitVoltageA = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitVoltageA.setStatus('current')
environmentUnitPowerA = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitPowerA.setStatus('current')
environmentUnitCurrentB = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitCurrentB.setStatus('current')
environmentUnitVoltageB = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitVoltageB.setStatus('current')
environmentUnitPowerB = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitPowerB.setStatus('current')
environmentUnitCurrentC = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitCurrentC.setStatus('current')
environmentUnitVoltageC = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitVoltageC.setStatus('current')
environmentUnitPowerC = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitPowerC.setStatus('current')
environmentUnitCurrentD = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitCurrentD.setStatus('current')
environmentUnitVoltageD = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitVoltageD.setStatus('current')
environmentUnitPowerD = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentUnitPowerD.setStatus('current')
environmentSysRAM = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentSysRAM.setStatus('current')
environmentSysFlash = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentSysFlash.setStatus('current')
environmentMacEth0 = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentMacEth0.setStatus('current')
environmentMacEth1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentMacEth1.setStatus('current')
environmentInputPower1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentInputPower1.setStatus('current')
environmentInputPower2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentInputPower2.setStatus('current')
environmentInputPower3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentInputPower3.setStatus('current')
environmentInputPower4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2634, 3, 200, 10, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentInputPower4.setStatus('current')
environmentBranchATotalCurrent = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentBranchATotalCurrent.setStatus('current')
environmentBranchATotalPower = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentBranchATotalPower.setStatus('current')
environmentBranchBTotalCurrent = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 40), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentBranchBTotalCurrent.setStatus('current')
environmentBranchBTotalPower = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 50), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentBranchBTotalPower.setStatus('current')
environmentBranchCTotalCurrent = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 51), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentBranchCTotalCurrent.setStatus('current')
environmentBranchCTotalPower = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 52), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentBranchCTotalPower.setStatus('current')
environmentBranchDTotalCurrent = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentBranchDTotalCurrent.setStatus('current')
environmentBranchDTotalPower = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentBranchDTotalPower.setStatus('current')
environmentSystemTotalCurrent = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 60), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentSystemTotalCurrent.setStatus('current')
environmentSystemTotalPower = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 70), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentSystemTotalPower.setStatus('current')
environmentMonthlyPowerLog = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 200, 80), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: environmentMonthlyPowerLog.setStatus('current')
alarmTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 280))
alarmOverCurrentInitial = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmOverCurrentInitial.setStatus('current')
alarmOverCurrentCritical = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmOverCurrentCritical.setStatus('current')
alarmOverTemperatureInitial = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmOverTemperatureInitial.setStatus('current')
alarmOverTemperatureCritical = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmOverTemperatureCritical.setStatus('current')
alarmCircuitBreakerOpen = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCircuitBreakerOpen.setStatus('current')
alarmCommLoss = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmCommLoss.setStatus('current')
alarmLostVoltage = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLostVoltage.setStatus('current')
alarmPingNoAnswer = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPingNoAnswer.setStatus('current')
alarmInvalidAccessLockout = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmInvalidAccessLockout.setStatus('current')
alarmPowerCycle = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPowerCycle.setStatus('current')
alarmAlarmInput = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmAlarmInput.setStatus('current')
alarmPlugCurrent = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPlugCurrent.setStatus('current')
alarmLostOptoVoltage = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLostOptoVoltage.setStatus('current')
alarmEmergencyShutoff = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEmergencyShutoff.setStatus('current')
alarmNoDialtone = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 280, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmNoDialtone.setStatus('current')
wtiTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300))
trapInfo = MibScalar((1, 3, 6, 1, 4, 1, 2634, 3, 300, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapInfo.setStatus('current')
testTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 2))
testTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 2) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
overCurrentInitialTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 4))
overCurrentInitialSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 4) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
overCurrentInitialClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 4) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
overCurrentCriticalTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 5))
overCurrentCriticalSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 5) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
overCurrentCriticalClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 5) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
overTemperatureInitialTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 6))
overTemperatureInitialSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 6) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
overTemperatureInitialClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 6) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
overTemperatureCriticalTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 7))
overTemperatureCriticalSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 7) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
overTemperatureCriticalClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 7) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
circuitBreakerOpenTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 8))
circuitBreakerOpenSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 8) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
circuitBreakerOpenClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 8) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
lostCommTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 9))
lostCommSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 9) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
lostCommClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 9) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
lostVoltageTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 10))
lostVoltageSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 10) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
lostVoltageClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 10) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
pingNoAnswerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 11))
pingNoAnswerSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 11) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
pingNoAnswerClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 11) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
lockoutTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 12))
lockoutSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 12) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
lockoutClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 12) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
powercycleTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 13))
powercycleSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 13) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
alarmInputTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 14))
alarmInputSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 14) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
alarmInputClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 14) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
plugCurrentTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 15))
plugCurrentSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 15) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
plugCurrentClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 15) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
lostOptoVoltageTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 16))
lostOptoVoltageSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 16) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
lostOptoVoltageClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 16) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
emergencyShutoffTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 17))
emergencyShutoffSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 17) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
emergencyShutoffClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 17) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
noDialtoneTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2634, 3, 300, 18))
noDialtoneSetTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 18) + (0,1)).setObjects(("WTI-POWER-MIB", "trapInfo"))
noDialtoneClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 2634, 3, 300, 18) + (0,2)).setObjects(("WTI-POWER-MIB", "trapInfo"))
mibBuilder.exportSymbols("WTI-POWER-MIB", environmentInputPower4=environmentInputPower4, overCurrentInitialTraps=overCurrentInitialTraps, environmentUnitCurrentC=environmentUnitCurrentC, lostCommClearTrap=lostCommClearTrap, plugID=plugID, environmentUnitTable=environmentUnitTable, environmentSystemTotalPower=environmentSystemTotalPower, userPasswd=userPasswd, plugGroupEntry=plugGroupEntry, alarmCircuitBreakerOpen=alarmCircuitBreakerOpen, environmentUnitCurrentB=environmentUnitCurrentB, lostOptoVoltageTraps=lostOptoVoltageTraps, alarmOverCurrentInitial=alarmOverCurrentInitial, plugStatus=plugStatus, environmentMacEth1=environmentMacEth1, overCurrentCriticalTraps=overCurrentCriticalTraps, userWebAccess=userWebAccess, userIndex=userIndex, lostCommTraps=lostCommTraps, lostCommSetTrap=lostCommSetTrap, wtiTraps=wtiTraps, userEntry=userEntry, pingNoAnswerSetTrap=pingNoAnswerSetTrap, environmentMacEth0=environmentMacEth0, alarmPowerCycle=alarmPowerCycle, pingNoAnswerTraps=pingNoAnswerTraps, plugCurrent=plugCurrent, overTemperatureInitialSetTrap=overTemperatureInitialSetTrap, overTemperatureCriticalSetTrap=overTemperatureCriticalSetTrap, alarmCommLoss=alarmCommLoss, alarmInputClearTrap=alarmInputClearTrap, environmentInputPower3=environmentInputPower3, userTable=userTable, lostVoltageTraps=lostVoltageTraps, circuitBreakerOpenSetTrap=circuitBreakerOpenSetTrap, plugCurrentClearTrap=plugCurrentClearTrap, noDialtoneClearTrap=noDialtoneClearTrap, environmentUnitPowerA=environmentUnitPowerA, lostVoltageSetTrap=lostVoltageSetTrap, userCurrentPowerMetering=userCurrentPowerMetering, emergencyShutoffTraps=emergencyShutoffTraps, environmentUnitIndex=environmentUnitIndex, trapInfo=trapInfo, alarmInputTraps=alarmInputTraps, plugCurrentTraps=plugCurrentTraps, alarmInputSetTrap=alarmInputSetTrap, overTemperatureCriticalTraps=overTemperatureCriticalTraps, environmentBranchATotalPower=environmentBranchATotalPower, environmentMonthlyPowerLog=environmentMonthlyPowerLog, noDialtoneTraps=noDialtoneTraps, pingNoAnswerClearTrap=pingNoAnswerClearTrap, environmentUnitTemperature=environmentUnitTemperature, environmentSystemTotalCurrent=environmentSystemTotalCurrent, alarmEmergencyShutoff=alarmEmergencyShutoff, powercycleSetTrap=powercycleSetTrap, userCallbackNum=userCallbackNum, environmentBranchCTotalCurrent=environmentBranchCTotalCurrent, overTemperatureInitialClearTrap=overTemperatureInitialClearTrap, plugTable=plugTable, lostOptoVoltageSetTrap=lostOptoVoltageSetTrap, environmentBranchBTotalPower=environmentBranchBTotalPower, alarmInvalidAccessLockout=alarmInvalidAccessLockout, overCurrentCriticalSetTrap=overCurrentCriticalSetTrap, lockoutTraps=lockoutTraps, environmentUnitPowerC=environmentUnitPowerC, environmentSysFlash=environmentSysFlash, plugGroupTable=plugGroupTable, environmentUnitCurrentD=environmentUnitCurrentD, environmentUnitVoltageA=environmentUnitVoltageA, testTraps=testTraps, environmentUnitVoltageB=environmentUnitVoltageB, lostVoltageClearTrap=lostVoltageClearTrap, environmentBranchATotalCurrent=environmentBranchATotalCurrent, lostOptoVoltageClearTrap=lostOptoVoltageClearTrap, environmentUnitVoltageC=environmentUnitVoltageC, userName=userName, plugIndex=plugIndex, testTrap=testTrap, userPortAccess=userPortAccess, environmentSysRAM=environmentSysRAM, userLocalAccess=userLocalAccess, power=power, alarmOverTemperatureInitial=alarmOverTemperatureInitial, userSerialAccess=userSerialAccess, alarmPlugCurrent=alarmPlugCurrent, environmentBranchBTotalCurrent=environmentBranchBTotalCurrent, PYSNMP_MODULE_ID=power, environmentUnitPowerD=environmentUnitPowerD, powercycleTraps=powercycleTraps, plugGroupPower=plugGroupPower, environmentUnitEntry=environmentUnitEntry, alarmAlarmInput=alarmAlarmInput, alarmOverCurrentCritical=alarmOverCurrentCritical, userGroupAccess=userGroupAccess, environmentUnitVoltageD=environmentUnitVoltageD, overCurrentInitialClearTrap=overCurrentInitialClearTrap, alarmLostVoltage=alarmLostVoltage, userSubmit=userSubmit, alarmNoDialtone=alarmNoDialtone, emergencyShutoffClearTrap=emergencyShutoffClearTrap, emergencyShutoffSetTrap=emergencyShutoffSetTrap, environmentBranchDTotalCurrent=environmentBranchDTotalCurrent, overTemperatureInitialTraps=overTemperatureInitialTraps, lockoutSetTrap=lockoutSetTrap, environmentBranchDTotalPower=environmentBranchDTotalPower, environmentUnitCurrentA=environmentUnitCurrentA, environmentUnitName=environmentUnitName, environmentBranchCTotalPower=environmentBranchCTotalPower, alarmOverTemperatureCritical=alarmOverTemperatureCritical, alarmPingNoAnswer=alarmPingNoAnswer, circuitBreakerOpenClearTrap=circuitBreakerOpenClearTrap, noDialtoneSetTrap=noDialtoneSetTrap, alarmTables=alarmTables, alarmLostOptoVoltage=alarmLostOptoVoltage, plugCurrentSetTrap=plugCurrentSetTrap, lockoutClearTrap=lockoutClearTrap, userAccessLevel=userAccessLevel, environmentInputPower2=environmentInputPower2, userTelnetSshAccess=userTelnetSshAccess, plugGroupAction=plugGroupAction, plugGroupIndex=plugGroupIndex, plugAction=plugAction, environmentTables=environmentTables, circuitBreakerOpenTraps=circuitBreakerOpenTraps, overCurrentInitialSetTrap=overCurrentInitialSetTrap, overTemperatureCriticalClearTrap=overTemperatureCriticalClearTrap, westernTelematic=westernTelematic, overCurrentCriticalClearTrap=overCurrentCriticalClearTrap, plugName=plugName, systemTables=systemTables, plugPower=plugPower, environmentUnitPowerB=environmentUnitPowerB, plugGroupCurrent=plugGroupCurrent, plugEntry=plugEntry, plugGroupName=plugGroupName, environmentInputPower1=environmentInputPower1)
