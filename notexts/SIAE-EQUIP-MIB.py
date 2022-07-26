#
# PySNMP MIB module SIAE-EQUIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-EQUIP-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:34:10 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
alarmTrap, AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "alarmTrap", "AlarmStatus", "AlarmSeverityCode")
equipTypeUnknown, = mibBuilder.importSymbols("SIAE-EQUIPTYPE-MIB", "equipTypeUnknown")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, iso, Counter64, NotificationType, TimeTicks, Unsigned32, Gauge32, IpAddress, Bits, ObjectIdentity, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "iso", "Counter64", "NotificationType", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "Bits", "ObjectIdentity", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, AutonomousType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "DisplayString")
equipment = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1))
equipment.setRevisions(('2015-03-23 00:00', '2014-12-03 00:00', '2014-07-01 00:00', '2014-06-23 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: equipment.setLastUpdated('201503230000Z')
if mibBuilder.loadTexts: equipment.setOrganization('SIAE MICROELETTRONICA spa')
equipMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipMibVersion.setStatus('current')
equipCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 2), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipCurrentTime.setStatus('current')
equipUpTime = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipUpTime.setStatus('current')
equipType = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 4), AutonomousType().clone((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipType.setStatus('current')
equipIpEthOsiAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthOsiAddress.setStatus('current')
equipGosipAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipGosipAddress.setStatus('current')
equipIpEthOsiNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthOsiNetMask.setStatus('current')
equipL1L2IsIsRouting = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("l1", 1), ("l2", 2))).clone('l1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipL1L2IsIsRouting.setStatus('current')
equipStationID = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipStationID.setStatus('current')
equipLOMConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLOMConfigEnable.setStatus('current')
equipLOMConnected = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cleared", 1), ("connectionAsMonitor", 2), ("connectionAsConfig", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipLOMConnected.setStatus('current')
equipLOMConnectedTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithAck", 3))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLOMConnectedTrapEnable.setStatus('current')
equipConfigChange = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipConfigChange.setStatus('current')
equipConfigChangeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithACK", 3))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipConfigChangeTrapEnable.setStatus('current')
equipRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 20, 21, 50, 100, 125, 126, 127))).clone(namedValues=NamedValues(("notActive", 0), ("restart", 1), ("applyIfChange", 2), ("revertIfChange", 3), ("configClearAndRestart", 4), ("routeTableClear", 5), ("uploadBaseBand", 6), ("offLineRouteRetrieve", 7), ("offLineRouteSave", 8), ("hotApplyIfChange", 11), ("ipStackConfigure", 20), ("osiStackConfigure", 21), ("atuTableReset", 50), ("siaeReservedReq1", 100), ("siaeReservedReq26", 125), ("siaeReservedReq27", 126), ("switchFactoryDefault", 127)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipRequest.setStatus('current')
equipIpEthAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthAddress.setStatus('current')
equipIpEthNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthNetMask.setStatus('current')
equipOsiamParameter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 41))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipOsiamParameter.setStatus('current')
equipIpSnmpAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpSnmpAgentAddress.setStatus('current')
equipOperationInProgress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipOperationInProgress.setStatus('current')
equipManagerWakeUpAlarm = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 22), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipManagerWakeUpAlarm.setStatus('current')
equipManagerWakeUpAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 23), AlarmSeverityCode().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpAlarmSeverityCode.setStatus('current')
equipManagerWakeUpTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpTimeout.setStatus('current')
equipManagerWakeUpIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 25), IpAddress().clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpIpAddr.setStatus('current')
equipManagerWakeUpGosipAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 26), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpGosipAddress.setStatus('current')
equipManagerWakeUpTrapVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapV1", 1), ("trapV2", 2), ("trapV3", 3))).clone('trapV1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpTrapVersion.setStatus('current')
equipManager1IpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 28), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManager1IpAddr.setStatus('current')
equipManager2IpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 29), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManager2IpAddr.setStatus('current')
equipManager1TrapVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapV1", 1), ("trapV2", 2), ("trapV3", 3))).clone('trapV1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManager1TrapVersion.setStatus('current')
equipManager2TrapVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapV1", 1), ("trapV2", 2), ("trapV3", 3))).clone('trapV1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManager2TrapVersion.setStatus('current')
equipDailyPmTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-12, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipDailyPmTimeZone.setStatus('current')
equipOperationMngtControl = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notActive", 0), ("startOperation", 1), ("confirmOperation", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipOperationMngtControl.setStatus('current')
equipOperationMngtInProgress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipOperationMngtInProgress.setStatus('current')
equipLocation = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 35), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLocation.setStatus('current')
equipLongitude = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 36), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLongitude.setStatus('current')
equipLatitude = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 37), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLatitude.setStatus('current')
equipIpEthVlanId = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthVlanId.setStatus('current')
equipIpEthDefGateway = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 39), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthDefGateway.setStatus('current')
equipIpEthDefGatewayIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 40), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthDefGatewayIfIndex.setStatus('current')
equipLOMConnectedMonitor = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 109)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipLOMConnected"))
if mibBuilder.loadTexts: equipLOMConnectedMonitor.setStatus('current')
equipLOMConnectedConfig = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 110)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipLOMConnected"))
if mibBuilder.loadTexts: equipLOMConnectedConfig.setStatus('current')
equipLOMDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 111)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipLOMConnected"))
if mibBuilder.loadTexts: equipLOMDisconnected.setStatus('current')
equipConfigChangeStatus = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 114)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipConfigChange"))
if mibBuilder.loadTexts: equipConfigChangeStatus.setStatus('current')
equipManagerWakeUpNotify = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 123)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipStationID"), ("SIAE-EQUIP-MIB", "equipLocation"), ("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipGosipAddress"), ("SIAE-EQUIP-MIB", "equipManagerWakeUpIpAddr"), ("SIAE-EQUIP-MIB", "equipManagerWakeUpAlarm"))
if mibBuilder.loadTexts: equipManagerWakeUpNotify.setStatus('current')
mibBuilder.exportSymbols("SIAE-EQUIP-MIB", equipLOMConnectedTrapEnable=equipLOMConnectedTrapEnable, equipIpEthOsiAddress=equipIpEthOsiAddress, equipStationID=equipStationID, equipConfigChangeTrapEnable=equipConfigChangeTrapEnable, equipLatitude=equipLatitude, equipLOMConnectedConfig=equipLOMConnectedConfig, equipIpEthDefGatewayIfIndex=equipIpEthDefGatewayIfIndex, equipManagerWakeUpGosipAddress=equipManagerWakeUpGosipAddress, equipGosipAddress=equipGosipAddress, equipIpEthNetMask=equipIpEthNetMask, equipIpEthDefGateway=equipIpEthDefGateway, equipManagerWakeUpIpAddr=equipManagerWakeUpIpAddr, equipManagerWakeUpTimeout=equipManagerWakeUpTimeout, equipLocation=equipLocation, equipOperationInProgress=equipOperationInProgress, equipManager1IpAddr=equipManager1IpAddr, equipL1L2IsIsRouting=equipL1L2IsIsRouting, equipIpEthOsiNetMask=equipIpEthOsiNetMask, equipManagerWakeUpAlarmSeverityCode=equipManagerWakeUpAlarmSeverityCode, equipLOMDisconnected=equipLOMDisconnected, equipIpEthVlanId=equipIpEthVlanId, equipLongitude=equipLongitude, equipIpEthAddress=equipIpEthAddress, equipManagerWakeUpAlarm=equipManagerWakeUpAlarm, PYSNMP_MODULE_ID=equipment, equipManager1TrapVersion=equipManager1TrapVersion, equipConfigChangeStatus=equipConfigChangeStatus, equipOperationMngtControl=equipOperationMngtControl, equipOperationMngtInProgress=equipOperationMngtInProgress, equipConfigChange=equipConfigChange, equipManager2IpAddr=equipManager2IpAddr, equipOsiamParameter=equipOsiamParameter, equipMibVersion=equipMibVersion, equipRequest=equipRequest, equipIpSnmpAgentAddress=equipIpSnmpAgentAddress, equipManagerWakeUpTrapVersion=equipManagerWakeUpTrapVersion, equipManager2TrapVersion=equipManager2TrapVersion, equipManagerWakeUpNotify=equipManagerWakeUpNotify, equipCurrentTime=equipCurrentTime, equipLOMConnectedMonitor=equipLOMConnectedMonitor, equipDailyPmTimeZone=equipDailyPmTimeZone, equipType=equipType, equipment=equipment, equipLOMConnected=equipLOMConnected, equipLOMConfigEnable=equipLOMConfigEnable, equipUpTime=equipUpTime)
