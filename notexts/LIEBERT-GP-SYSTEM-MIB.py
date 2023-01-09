#
# PySNMP MIB module LIEBERT-GP-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:33:46 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
lgpAgentConnectedDeviceCount, lgpAgentDeviceIndex = mibBuilder.importSymbols("LIEBERT-GP-AGENT-MIB", "lgpAgentConnectedDeviceCount", "lgpAgentDeviceIndex")
liebertSystemModuleReg, lgpSystem = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertSystemModuleReg", "lgpSystem")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Gauge32, NotificationType, ModuleIdentity, TimeTicks, IpAddress, Integer32, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "ModuleIdentity", "TimeTicks", "IpAddress", "Integer32", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
liebertSystemModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 8, 1))
liebertSystemModule.setRevisions(('2008-11-17 00:00', '2008-07-02 00:00', '2008-01-10 00:00', '2007-05-29 00:00', '2006-02-22 00:00',))
if mibBuilder.loadTexts: liebertSystemModule.setLastUpdated('200811170000Z')
if mibBuilder.loadTexts: liebertSystemModule.setOrganization('Liebert Corporation')
lgpSysStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1))
if mibBuilder.loadTexts: lgpSysStatistics.setStatus('current')
lgpSysStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2))
if mibBuilder.loadTexts: lgpSysStatus.setStatus('current')
lgpSysSettings = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3))
if mibBuilder.loadTexts: lgpSysSettings.setStatus('current')
lgpSysControl = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4))
if mibBuilder.loadTexts: lgpSysControl.setStatus('current')
lgpSysTime = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5))
if mibBuilder.loadTexts: lgpSysTime.setStatus('current')
lgpSysMaintenance = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6))
if mibBuilder.loadTexts: lgpSysMaintenance.setStatus('current')
lgpSysEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysEventDescription.setStatus('current')
lgpSysEventNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8))
if mibBuilder.loadTexts: lgpSysEventNotifications.setStatus('current')
lgpSysDeviceComponentGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9))
if mibBuilder.loadTexts: lgpSysDeviceComponentGroup.setStatus('current')
lgpSysDeviceComponentTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1), )
if mibBuilder.loadTexts: lgpSysDeviceComponentTable.setStatus('current')
lgpSysDeviceComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1), ).setIndexNames((0, "LIEBERT-GP-AGENT-MIB", "lgpAgentDeviceIndex"), (0, "LIEBERT-GP-SYSTEM-MIB", "lgpSysDeviceComponentIndex"))
if mibBuilder.loadTexts: lgpSysDeviceComponentEntry.setStatus('current')
lgpSysDeviceComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: lgpSysDeviceComponentIndex.setStatus('current')
lgpSysDeviceComponentDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentDescr.setStatus('current')
lgpSysDeviceComponentSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentSerialNum.setStatus('current')
lgpSysDeviceComponentModelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentModelNum.setStatus('current')
lgpSysDeviceComponentWellknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5))
if mibBuilder.loadTexts: lgpSysDeviceComponentWellknown.setStatus('current')
lgpSysDeviceBatCabinet = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 5))
if mibBuilder.loadTexts: lgpSysDeviceBatCabinet.setStatus('current')
lgpSysDeviceParallelCabinet = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 6))
if mibBuilder.loadTexts: lgpSysDeviceParallelCabinet.setStatus('current')
lgpSysDeviceMaintBypass = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 7))
if mibBuilder.loadTexts: lgpSysDeviceMaintBypass.setStatus('current')
lgpSysNotification = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-SYSTEM-MIB", "lgpSysEventDescription"))
if mibBuilder.loadTexts: lgpSysNotification.setStatus('current')
lgpSysNormal = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-AGENT-MIB", "lgpAgentConnectedDeviceCount"))
if mibBuilder.loadTexts: lgpSysNormal.setStatus('current')
lgpSysStatisticsRunHrs = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1, 1), Unsigned32()).setUnits('hours').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysStatisticsRunHrs.setStatus('current')
lgpSysSelfTestResult = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("passed", 2), ("failed", 3), ("inProgress", 4), ("sysFailure", 5), ("inhibited", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysSelfTestResult.setStatus('current')
lgpSysState = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normalOperation", 1), ("startUp", 2), ("normalWithWarning", 3), ("normalWithAlarm", 4), ("abnormalOperation", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysState.setStatus('current')
lgpSysAudibleAlarm = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysAudibleAlarm.setStatus('current')
lgpSysSelfTest = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysSelfTest.setStatus('current')
lgpSysControlOperationOnOff = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysControlOperationOnOff.setStatus('current')
lgpSysTimeEpoch = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysTimeEpoch.setStatus('current')
lgpSysMaintenanceCapacity = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 1), Unsigned32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceCapacity.setStatus('current')
lgpSysMaintenanceYear = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 2), Unsigned32()).setUnits('year').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceYear.setStatus('current')
lgpSysMaintenanceMonth = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 3), Unsigned32()).setUnits('month').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceMonth.setStatus('current')
mibBuilder.exportSymbols("LIEBERT-GP-SYSTEM-MIB", lgpSysTime=lgpSysTime, lgpSysEventDescription=lgpSysEventDescription, lgpSysNotification=lgpSysNotification, lgpSysDeviceComponentModelNum=lgpSysDeviceComponentModelNum, lgpSysTimeEpoch=lgpSysTimeEpoch, lgpSysStatistics=lgpSysStatistics, lgpSysDeviceComponentSerialNum=lgpSysDeviceComponentSerialNum, lgpSysDeviceComponentDescr=lgpSysDeviceComponentDescr, lgpSysDeviceComponentWellknown=lgpSysDeviceComponentWellknown, lgpSysDeviceComponentEntry=lgpSysDeviceComponentEntry, lgpSysDeviceParallelCabinet=lgpSysDeviceParallelCabinet, lgpSysMaintenance=lgpSysMaintenance, lgpSysSelfTest=lgpSysSelfTest, lgpSysDeviceBatCabinet=lgpSysDeviceBatCabinet, lgpSysControlOperationOnOff=lgpSysControlOperationOnOff, lgpSysStatisticsRunHrs=lgpSysStatisticsRunHrs, lgpSysDeviceComponentIndex=lgpSysDeviceComponentIndex, lgpSysState=lgpSysState, lgpSysNormal=lgpSysNormal, lgpSysMaintenanceMonth=lgpSysMaintenanceMonth, liebertSystemModule=liebertSystemModule, lgpSysStatus=lgpSysStatus, lgpSysDeviceMaintBypass=lgpSysDeviceMaintBypass, lgpSysDeviceComponentTable=lgpSysDeviceComponentTable, lgpSysAudibleAlarm=lgpSysAudibleAlarm, lgpSysMaintenanceYear=lgpSysMaintenanceYear, lgpSysControl=lgpSysControl, lgpSysMaintenanceCapacity=lgpSysMaintenanceCapacity, lgpSysSelfTestResult=lgpSysSelfTestResult, lgpSysSettings=lgpSysSettings, lgpSysEventNotifications=lgpSysEventNotifications, lgpSysDeviceComponentGroup=lgpSysDeviceComponentGroup, PYSNMP_MODULE_ID=liebertSystemModule)
