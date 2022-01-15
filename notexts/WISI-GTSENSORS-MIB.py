#
# PySNMP MIB module WISI-GTSENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-GTSENSORS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:36:37 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Unsigned32, IpAddress, Integer32, MibIdentifier, Counter64, Bits, NotificationType, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "MibIdentifier", "Counter64", "Bits", "NotificationType", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gtModule, = mibBuilder.importSymbols("WISI-GTMODULES-MIB", "gtModule")
gtUnit, = mibBuilder.importSymbols("WISI-TANGRAM-MIB", "gtUnit")
gtSensorsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3))
gtSensorsMIB.setRevisions(('2016-09-08 00:00', '2013-07-01 14:00', '2013-06-27 14:00', '2013-06-26 14:00', '2012-12-12 13:20', '2011-12-15 12:00',))
if mibBuilder.loadTexts: gtSensorsMIB.setLastUpdated('201609080000Z')
if mibBuilder.loadTexts: gtSensorsMIB.setOrganization('WISI Communications GmbH & Co. KG')
gtSensorsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0))
gtSensorsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1))
gtSensorsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2))
gtSensorsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 1))
gtSensorsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2))
gtSensorsNotifyFanPlugin = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 1))
if mibBuilder.loadTexts: gtSensorsNotifyFanPlugin.setStatus('current')
gtSensorsNotifyFanPlugout = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 2))
if mibBuilder.loadTexts: gtSensorsNotifyFanPlugout.setStatus('current')
gtSensorsNotifyPSUPlugin = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 3))
if mibBuilder.loadTexts: gtSensorsNotifyPSUPlugin.setStatus('current')
gtSensorsNotifyPSUPlugout = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 4))
if mibBuilder.loadTexts: gtSensorsNotifyPSUPlugout.setStatus('current')
gtSensorsNotifyTemperature = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 5))
if mibBuilder.loadTexts: gtSensorsNotifyTemperature.setStatus('current')
gtSensorsNotifyFanSpeed = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 6))
if mibBuilder.loadTexts: gtSensorsNotifyFanSpeed.setStatus('current')
gtSensorsNotifyPSUCurrent = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 7))
if mibBuilder.loadTexts: gtSensorsNotifyPSUCurrent.setStatus('current')
gtSensorsNotifyPSUVoltage = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 8))
if mibBuilder.loadTexts: gtSensorsNotifyPSUVoltage.setStatus('current')
gtSensorsNotifyPSUTemperature = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 9))
if mibBuilder.loadTexts: gtSensorsNotifyPSUTemperature.setStatus('current')
gtSensorsNotifyPSUTemperatureClear = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 10))
if mibBuilder.loadTexts: gtSensorsNotifyPSUTemperatureClear.setStatus('current')
gtSensorsNotifyBOARDTemperatureClear = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 11))
if mibBuilder.loadTexts: gtSensorsNotifyBOARDTemperatureClear.setStatus('current')
gtSensorsNotifyPSUFailure = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 12))
if mibBuilder.loadTexts: gtSensorsNotifyPSUFailure.setStatus('current')
gtSensorsNotifyPSUFailureClear = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 0, 13))
if mibBuilder.loadTexts: gtSensorsNotifyPSUFailureClear.setStatus('current')
gtNumTemps = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtNumTemps.setStatus('current')
gtTempsTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2), )
if mibBuilder.loadTexts: gtTempsTable.setStatus('current')
gtTempsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"), (0, "WISI-GTSENSORS-MIB", "gtTemp"))
if mibBuilder.loadTexts: gtTempsEntry.setStatus('current')
gtTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: gtTemp.setStatus('current')
gtTempName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtTempName.setStatus('current')
gtTempValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 195))).setUnits("'C").setMaxAccess("readonly")
if mibBuilder.loadTexts: gtTempValue.setStatus('current')
gtNumFans = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtNumFans.setStatus('current')
gtFansTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4), )
if mibBuilder.loadTexts: gtFansTable.setStatus('current')
gtFansEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1), ).setIndexNames((0, "WISI-GTSENSORS-MIB", "gtFan"))
if mibBuilder.loadTexts: gtFansEntry.setStatus('current')
gtFan = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: gtFan.setStatus('current')
gtFanName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtFanName.setStatus('current')
gtFanControl = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setUnits('rpm').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtFanControl.setStatus('current')
gtFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000))).setUnits('rpm').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtFanSpeed.setStatus('current')
gtFanUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 5), Counter32()).setUnits('s').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtFanUptime.setStatus('current')
gtFanLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 4, 1, 6), Counter32()).setUnits('s').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtFanLifetime.setStatus('current')
gtNumPSUs = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtNumPSUs.setStatus('current')
gtPSUsTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6), )
if mibBuilder.loadTexts: gtPSUsTable.setStatus('current')
gtPSUsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1), ).setIndexNames((0, "WISI-GTSENSORS-MIB", "gtPSU"))
if mibBuilder.loadTexts: gtPSUsEntry.setStatus('current')
gtPSU = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: gtPSU.setStatus('current')
gtPSUName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtPSUName.setStatus('current')
gtPSUPower = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 300000))).setUnits('mW').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtPSUPower.setStatus('current')
gtPSUCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 25000))).setUnits('mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtPSUCurrent.setStatus('current')
gtPSUVoltageInt = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16000))).setUnits('mV').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtPSUVoltageInt.setStatus('current')
gtPSUVoltageOR = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16000))).setUnits('mV').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtPSUVoltageOR.setStatus('current')
gtPSUVoltageExt = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16000))).setUnits('mV').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtPSUVoltageExt.setStatus('current')
gtPSUTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 195))).setUnits("'C").setMaxAccess("readonly")
if mibBuilder.loadTexts: gtPSUTemperature.setStatus('current')
gtSensorsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 1, 1)).setObjects(("WISI-GTSENSORS-MIB", "gtSensorsV1Group"), ("WISI-GTSENSORS-MIB", "gtSensorsSystemGroup"), ("WISI-GTSENSORS-MIB", "gtSensorsStatsGroup"), ("WISI-GTSENSORS-MIB", "gtSensorsTrapGroup"), ("WISI-GTSENSORS-MIB", "gtSensorsSetGroup"), ("WISI-GTSENSORS-MIB", "gtSensorsBasicNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtSensorsMIBCompliance = gtSensorsMIBCompliance.setStatus('current')
gtSensorsV1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 1)).setObjects(("WISI-GTSENSORS-MIB", "gtTempName"), ("WISI-GTSENSORS-MIB", "gtTempValue"), ("WISI-GTSENSORS-MIB", "gtFanName"), ("WISI-GTSENSORS-MIB", "gtFanControl"), ("WISI-GTSENSORS-MIB", "gtFanSpeed"), ("WISI-GTSENSORS-MIB", "gtPSUName"), ("WISI-GTSENSORS-MIB", "gtPSUPower"), ("WISI-GTSENSORS-MIB", "gtPSUCurrent"), ("WISI-GTSENSORS-MIB", "gtPSUVoltageInt"), ("WISI-GTSENSORS-MIB", "gtPSUVoltageOR"), ("WISI-GTSENSORS-MIB", "gtPSUVoltageExt"), ("WISI-GTSENSORS-MIB", "gtPSUTemperature"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtSensorsV1Group = gtSensorsV1Group.setStatus('current')
gtSensorsSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 2)).setObjects(("WISI-GTSENSORS-MIB", "gtTempName"), ("WISI-GTSENSORS-MIB", "gtTempValue"), ("WISI-GTSENSORS-MIB", "gtFanName"), ("WISI-GTSENSORS-MIB", "gtFanSpeed"), ("WISI-GTSENSORS-MIB", "gtPSUName"), ("WISI-GTSENSORS-MIB", "gtPSUPower"), ("WISI-GTSENSORS-MIB", "gtPSUCurrent"), ("WISI-GTSENSORS-MIB", "gtPSUVoltageInt"), ("WISI-GTSENSORS-MIB", "gtPSUVoltageOR"), ("WISI-GTSENSORS-MIB", "gtPSUVoltageExt"), ("WISI-GTSENSORS-MIB", "gtPSUTemperature"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtSensorsSystemGroup = gtSensorsSystemGroup.setStatus('current')
gtSensorsStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 3)).setObjects(("WISI-GTSENSORS-MIB", "gtNumTemps"), ("WISI-GTSENSORS-MIB", "gtNumFans"), ("WISI-GTSENSORS-MIB", "gtFanUptime"), ("WISI-GTSENSORS-MIB", "gtFanLifetime"), ("WISI-GTSENSORS-MIB", "gtNumPSUs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtSensorsStatsGroup = gtSensorsStatsGroup.setStatus('current')
gtSensorsTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 4)).setObjects(("WISI-GTSENSORS-MIB", "gtTempValue"), ("WISI-GTSENSORS-MIB", "gtFanControl"), ("WISI-GTSENSORS-MIB", "gtFanSpeed"), ("WISI-GTSENSORS-MIB", "gtPSUCurrent"), ("WISI-GTSENSORS-MIB", "gtPSUVoltageInt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtSensorsTrapGroup = gtSensorsTrapGroup.setStatus('current')
gtSensorsSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 5)).setObjects(("WISI-GTSENSORS-MIB", "gtFanControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtSensorsSetGroup = gtSensorsSetGroup.setStatus('current')
gtSensorsBasicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 3, 2, 2, 6)).setObjects(("WISI-GTSENSORS-MIB", "gtSensorsNotifyFanPlugin"), ("WISI-GTSENSORS-MIB", "gtSensorsNotifyFanPlugout"), ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUPlugin"), ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUPlugout"), ("WISI-GTSENSORS-MIB", "gtSensorsNotifyTemperature"), ("WISI-GTSENSORS-MIB", "gtSensorsNotifyFanSpeed"), ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUCurrent"), ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUVoltage"), ("WISI-GTSENSORS-MIB", "gtSensorsNotifyPSUTemperature"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtSensorsBasicNotificationsGroup = gtSensorsBasicNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("WISI-GTSENSORS-MIB", gtPSUsTable=gtPSUsTable, gtSensorsNotifyPSUTemperatureClear=gtSensorsNotifyPSUTemperatureClear, gtNumPSUs=gtNumPSUs, gtPSUVoltageInt=gtPSUVoltageInt, gtSensorsNotifications=gtSensorsNotifications, gtSensorsNotifyPSUVoltage=gtSensorsNotifyPSUVoltage, gtNumFans=gtNumFans, gtSensorsSetGroup=gtSensorsSetGroup, gtFansTable=gtFansTable, gtSensorsNotifyTemperature=gtSensorsNotifyTemperature, gtFanSpeed=gtFanSpeed, gtPSUVoltageOR=gtPSUVoltageOR, gtFanUptime=gtFanUptime, gtSensorsMIBCompliance=gtSensorsMIBCompliance, gtSensorsObjects=gtSensorsObjects, gtSensorsConformance=gtSensorsConformance, gtPSUCurrent=gtPSUCurrent, gtSensorsBasicNotificationsGroup=gtSensorsBasicNotificationsGroup, gtSensorsNotifyFanPlugout=gtSensorsNotifyFanPlugout, gtSensorsNotifyFanPlugin=gtSensorsNotifyFanPlugin, gtSensorsNotifyPSUCurrent=gtSensorsNotifyPSUCurrent, gtSensorsNotifyPSUFailure=gtSensorsNotifyPSUFailure, gtSensorsNotifyPSUPlugout=gtSensorsNotifyPSUPlugout, gtPSUName=gtPSUName, gtFanControl=gtFanControl, gtTempsTable=gtTempsTable, PYSNMP_MODULE_ID=gtSensorsMIB, gtSensorsTrapGroup=gtSensorsTrapGroup, gtSensorsMIB=gtSensorsMIB, gtSensorsNotifyBOARDTemperatureClear=gtSensorsNotifyBOARDTemperatureClear, gtSensorsNotifyPSUPlugin=gtSensorsNotifyPSUPlugin, gtTempValue=gtTempValue, gtFanName=gtFanName, gtPSUVoltageExt=gtPSUVoltageExt, gtSensorsNotifyPSUFailureClear=gtSensorsNotifyPSUFailureClear, gtPSUTemperature=gtPSUTemperature, gtSensorsNotifyPSUTemperature=gtSensorsNotifyPSUTemperature, gtPSUsEntry=gtPSUsEntry, gtSensorsSystemGroup=gtSensorsSystemGroup, gtFan=gtFan, gtSensorsCompliances=gtSensorsCompliances, gtTemp=gtTemp, gtTempsEntry=gtTempsEntry, gtSensorsV1Group=gtSensorsV1Group, gtFanLifetime=gtFanLifetime, gtTempName=gtTempName, gtNumTemps=gtNumTemps, gtSensorsGroups=gtSensorsGroups, gtFansEntry=gtFansEntry, gtPSU=gtPSU, gtSensorsNotifyFanSpeed=gtSensorsNotifyFanSpeed, gtPSUPower=gtPSUPower, gtSensorsStatsGroup=gtSensorsStatsGroup)
