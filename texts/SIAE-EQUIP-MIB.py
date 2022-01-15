#
# PySNMP MIB module SIAE-EQUIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-EQUIP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:34:26 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
AlarmStatus, AlarmSeverityCode, alarmTrap = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode", "alarmTrap")
equipTypeUnknown, = mibBuilder.importSymbols("SIAE-EQUIPTYPE-MIB", "equipTypeUnknown")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, TimeTicks, MibIdentifier, iso, Counter32, Gauge32, ModuleIdentity, Counter64, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "TimeTicks", "MibIdentifier", "iso", "Counter32", "Gauge32", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity")
AutonomousType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DisplayString")
equipment = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1))
equipment.setRevisions(('2015-03-23 00:00', '2014-12-03 00:00', '2014-07-01 00:00', '2014-06-23 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: equipment.setRevisionsDescriptions(('Removed alarmTrapNumber from TRAPs and IMPORTS.\n            ', 'MIB version 01.00.02\n             Added equipIpEthDefGatewayIfIndex\n            ', 'MIB version 01.00.01\n             Added equipIpEthVlanId and equipIpEthDefGateway\n            ', 'Fixed IMPORTS clause\n            ', 'Improved description of equipMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: equipment.setLastUpdated('201503230000Z')
if mibBuilder.loadTexts: equipment.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: equipment.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: help@siaemic.com\n            ')
if mibBuilder.loadTexts: equipment.setDescription('Common parameters of SIAE equipments.\n            ')
equipMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipMibVersion.setStatus('current')
if mibBuilder.loadTexts: equipMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
equipCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 2), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipCurrentTime.setStatus('current')
if mibBuilder.loadTexts: equipCurrentTime.setDescription('Seconds since 1/1/1970.')
equipUpTime = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipUpTime.setStatus('current')
if mibBuilder.loadTexts: equipUpTime.setDescription('The time since the system was last re-initialized (in seconds\n             since 1/1/1970).')
equipType = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 4), AutonomousType().clone((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipType.setStatus('current')
if mibBuilder.loadTexts: equipType.setDescription("Type of SIAE MICROELETTRONICA's equipment")
equipIpEthOsiAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthOsiAddress.setStatus('current')
if mibBuilder.loadTexts: equipIpEthOsiAddress.setDescription('Ip address of the equipment on Ethernet-OSI interface.')
equipGosipAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipGosipAddress.setStatus('current')
if mibBuilder.loadTexts: equipGosipAddress.setDescription('GOSIP address of the equipment.')
equipIpEthOsiNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthOsiNetMask.setStatus('current')
if mibBuilder.loadTexts: equipIpEthOsiNetMask.setDescription('The subnet Mask associated with the IP address of OSI ethernet interface.\n             The value of the Mask is an IP address with all the network bits set to 1\n             and all the hosts bits set to 0.')
equipL1L2IsIsRouting = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("l1", 1), ("l2", 2))).clone('l1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipL1L2IsIsRouting.setStatus('current')
if mibBuilder.loadTexts: equipL1L2IsIsRouting.setDescription('It defines the IS-IS routing type: L1 within the same area, L2 among\n             different areas.')
equipStationID = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipStationID.setStatus('current')
if mibBuilder.loadTexts: equipStationID.setDescription('ASCII string assigned by the operator to identify the specific equipment.')
equipLOMConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLOMConfigEnable.setStatus('current')
if mibBuilder.loadTexts: equipLOMConfigEnable.setDescription('Enables/disables the capabilityto connect a LOM in Configuration Mode.')
equipLOMConnected = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cleared", 1), ("connectionAsMonitor", 2), ("connectionAsConfig", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipLOMConnected.setStatus('current')
if mibBuilder.loadTexts: equipLOMConnected.setDescription('Signal when the LOM is connected to the NE and if the connection\n             is for monitor or configuration.')
equipLOMConnectedTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithAck", 3))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLOMConnectedTrapEnable.setStatus('current')
if mibBuilder.loadTexts: equipLOMConnectedTrapEnable.setDescription('Enables/disables the trap generation on EquipLOMConnected status change event.')
equipConfigChange = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipConfigChange.setStatus('current')
if mibBuilder.loadTexts: equipConfigChange.setDescription('Set by the NE when the equipment configuration is changed by the local\n             or Remote LOM.\n             The octet string is a bit stream of flags; a set bit is a change on a\n             specific item. We had:\n             Byte 0.7: change in configuration for equipment group\n             Byte 0.6: change in configuration for userInput group\n             Byte 0.5: change in configuration for userOutput group\n             Byte 0.4: change in configuration for alarmLog group\n             ......\n             Byte 3.7: change in a severity for equipment group\n             Byte 3.6: change in a severity for userInput group\n             Byte 3.5: change in a severity for userOutput group\n             Byte 3.4: change in a severity for alarmLog group\n             CEM can reset the change condition writing one to desired bit flag\n             ......')
equipConfigChangeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithACK", 3))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipConfigChangeTrapEnable.setStatus('current')
if mibBuilder.loadTexts: equipConfigChangeTrapEnable.setDescription('Enables/disables the trap generation on EquipConfigChange status\n             change event.')
equipRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 20, 21, 50, 100, 125, 126, 127))).clone(namedValues=NamedValues(("notActive", 0), ("restart", 1), ("applyIfChange", 2), ("revertIfChange", 3), ("configClearAndRestart", 4), ("routeTableClear", 5), ("uploadBaseBand", 6), ("offLineRouteRetrieve", 7), ("offLineRouteSave", 8), ("hotApplyIfChange", 11), ("ipStackConfigure", 20), ("osiStackConfigure", 21), ("atuTableReset", 50), ("siaeReservedReq1", 100), ("siaeReservedReq26", 125), ("siaeReservedReq27", 126), ("switchFactoryDefault", 127)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipRequest.setStatus('current')
if mibBuilder.loadTexts: equipRequest.setDescription('Force Equipment Controller restart or change in interface properties.')
equipIpEthAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthAddress.setStatus('current')
if mibBuilder.loadTexts: equipIpEthAddress.setDescription('Ip address of the equipment on Ethernet interface.')
equipIpEthNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthNetMask.setStatus('current')
if mibBuilder.loadTexts: equipIpEthNetMask.setDescription('The subnet Mask associated with the IP address of ethernet interface.\n             The value of the Mask is an IP address with all the network bits set to 1\n             and all the hosts bits set to 0.')
equipOsiamParameter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 41))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipOsiamParameter.setStatus('current')
if mibBuilder.loadTexts: equipOsiamParameter.setDescription('It defines the set-up parameter for OSI stack.')
equipIpSnmpAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpSnmpAgentAddress.setStatus('current')
if mibBuilder.loadTexts: equipIpSnmpAgentAddress.setDescription('Ip address used by SNMP Agent for mark generated TRAP.')
equipOperationInProgress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipOperationInProgress.setStatus('current')
if mibBuilder.loadTexts: equipOperationInProgress.setDescription('A value different from 0 means operation in progress.')
equipManagerWakeUpAlarm = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 22), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipManagerWakeUpAlarm.setStatus('current')
if mibBuilder.loadTexts: equipManagerWakeUpAlarm.setDescription('This alarm switches on when periodic connection wake-up trap starts.\n            The trap related to this alarm is also sent periodically only to the\n            manager specified by the leaf equipManagerWakeUpIpAddr when\n            equipManagerWakeUpAlarmSeverityCode differs from disable.')
equipManagerWakeUpAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 23), AlarmSeverityCode().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: equipManagerWakeUpAlarmSeverityCode.setDescription('Defines the severity associated to the equipManagerWakeUpAlarm\n             and enables/disables the trap generation on status change event.')
equipManagerWakeUpTimeout = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpTimeout.setStatus('current')
if mibBuilder.loadTexts: equipManagerWakeUpTimeout.setDescription('This object defines the time (in minutes) after which the periodic\n             connection wake-up trap is stopped.\n             The maximium value is equivalent to 24 hours.\n             When the timeout elapses the equipManagerWakeUpAlarmSeverityCode\n             is set to disable.\n             A zero means no timeout.')
equipManagerWakeUpIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 25), IpAddress().clone(hexValue="00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpIpAddr.setStatus('current')
if mibBuilder.loadTexts: equipManagerWakeUpIpAddr.setDescription('Ip Address of manager wich to send a periodic connection wake-up trap.\n             The periodic trap is sent only if the equipManagerWakeUpAlarmSeverityCode\n             differs from disable.\n             If Ip Address equals 0 no trap will be sent.')
equipManagerWakeUpGosipAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 26), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpGosipAddress.setStatus('current')
if mibBuilder.loadTexts: equipManagerWakeUpGosipAddress.setDescription('Gosip Address of manager wich to send a periodic connection wake-up trap.')
equipManagerWakeUpTrapVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapV1", 1), ("trapV2", 2), ("trapV3", 3))).clone('trapV1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManagerWakeUpTrapVersion.setStatus('current')
if mibBuilder.loadTexts: equipManagerWakeUpTrapVersion.setDescription('Trap version supported by Manager to wake-up.')
equipManager1IpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 28), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManager1IpAddr.setStatus('current')
if mibBuilder.loadTexts: equipManager1IpAddr.setDescription('First IP address of a SNMP Manager always logged to this equipment.\n             The address 0.0.0.0 mean that manager is not present.')
equipManager2IpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 29), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManager2IpAddr.setStatus('current')
if mibBuilder.loadTexts: equipManager2IpAddr.setDescription('Second IP address of a SNMP Manager always logged to this equipment.\n             The address 0.0.0.0 mean that manager is not present.')
equipManager1TrapVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapV1", 1), ("trapV2", 2), ("trapV3", 3))).clone('trapV1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManager1TrapVersion.setStatus('current')
if mibBuilder.loadTexts: equipManager1TrapVersion.setDescription('Trap version supported by Manager 1 (related to equipManager1IpAddr).')
equipManager2TrapVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trapV1", 1), ("trapV2", 2), ("trapV3", 3))).clone('trapV1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipManager2TrapVersion.setStatus('current')
if mibBuilder.loadTexts: equipManager2TrapVersion.setDescription('Trap version supported by Manager 2 (related to equipManager2IpAddr).')
equipDailyPmTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 32), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-12, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipDailyPmTimeZone.setStatus('current')
if mibBuilder.loadTexts: equipDailyPmTimeZone.setDescription('Reference GMT Time Zone to close the daily P.M. records.')
equipOperationMngtControl = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notActive", 0), ("startOperation", 1), ("confirmOperation", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipOperationMngtControl.setStatus('current')
if mibBuilder.loadTexts: equipOperationMngtControl.setDescription("startOperation means the apply of the 'management parameters\n            set' on the E6165 switch.\n            confirmOperation means the backup of the 'management\n            parameters set'.")
equipOperationMngtInProgress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 34), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: equipOperationMngtInProgress.setStatus('current')
if mibBuilder.loadTexts: equipOperationMngtInProgress.setDescription('A value different from 0 means Mngt operation in progress.')
equipLocation = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 35), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLocation.setStatus('current')
if mibBuilder.loadTexts: equipLocation.setDescription('ASCII string assigned by the operator to identify the location of\n            specific equipment.')
equipLongitude = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 36), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLongitude.setStatus('current')
if mibBuilder.loadTexts: equipLongitude.setDescription('Geographic coordinate that specifies the east-west position of\n            the equipment.\n            In order to calculate the latitude in degrees the formula to be\n            applied is\n               Longitude = equipLongitude*180/2^31\n            This object is used with equipLatitude to locate the equipment\n            on a map.\n           ')
equipLatitude = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 37), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipLatitude.setStatus('current')
if mibBuilder.loadTexts: equipLatitude.setDescription('Geographic coordinate that specifies the north-south position of\n            the equipment.\n            In order to calculate the latitude in degrees the formula to be\n            applied is\n               Latitude = equipLatitude*180/2^31\n            This object is used with equipLongitude to locate the equipment\n            on a map.\n           ')
equipIpEthVlanId = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 38), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthVlanId.setStatus('current')
if mibBuilder.loadTexts: equipIpEthVlanId.setDescription('Ethernet vlan id on top of which management is built')
equipIpEthDefGateway = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 39), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthDefGateway.setStatus('current')
if mibBuilder.loadTexts: equipIpEthDefGateway.setDescription('Ip address of the default gateway on Ethernet interface.')
equipIpEthDefGatewayIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 40), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: equipIpEthDefGatewayIfIndex.setStatus('current')
if mibBuilder.loadTexts: equipIpEthDefGatewayIfIndex.setDescription('Ip address of the default gateway on Ethernet interface.')
equipLOMConnectedMonitor = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 109)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipLOMConnected"))
if mibBuilder.loadTexts: equipLOMConnectedMonitor.setStatus('current')
if mibBuilder.loadTexts: equipLOMConnectedMonitor.setDescription('This event is generated by ALFOHD-NE when equipLOMConnected is set to Monitor mode.\n             The data passed with the event are:\n                1) equipIpSnmpAgentAddress\n                2) equipLOMConnected')
equipLOMConnectedConfig = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 110)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipLOMConnected"))
if mibBuilder.loadTexts: equipLOMConnectedConfig.setStatus('current')
if mibBuilder.loadTexts: equipLOMConnectedConfig.setDescription('This event is generated by ALFOHD-NE when equipLOMConnected is set to Configuration mode.\n             The data passed with the event are:\n                1) equipIpSnmpAgentAddress\n                2) equipLOMConnected')
equipLOMDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 111)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipLOMConnected"))
if mibBuilder.loadTexts: equipLOMDisconnected.setStatus('current')
if mibBuilder.loadTexts: equipLOMDisconnected.setDescription('This event is generated by ALFOHD-NE when LOMConnected is cleared.\n             The data passed with the event are:\n                1) equipIpSnmpAgentAddress\n                2) equipLOMConnected')
equipConfigChangeStatus = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 114)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipConfigChange"))
if mibBuilder.loadTexts: equipConfigChangeStatus.setStatus('current')
if mibBuilder.loadTexts: equipConfigChangeStatus.setDescription('This event is generated by ALFOHD-NE when equipConfigChange is changed.\n             The data passed with the event are:\n                1) equipIpSnmpAgentAddress\n                2) equipConfigChange')
equipManagerWakeUpNotify = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 123)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipStationID"), ("SIAE-EQUIP-MIB", "equipLocation"), ("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-EQUIP-MIB", "equipGosipAddress"), ("SIAE-EQUIP-MIB", "equipManagerWakeUpIpAddr"), ("SIAE-EQUIP-MIB", "equipManagerWakeUpAlarm"))
if mibBuilder.loadTexts: equipManagerWakeUpNotify.setStatus('current')
if mibBuilder.loadTexts: equipManagerWakeUpNotify.setDescription(' This trap is sent periodically only to the manager specified by\n             the leaf equipManagerWakeUpIpAddr when equipManagerWakeUpAlarmSeverityCode\n             differs from disable.\n             The data passed with the event are:\n                1) equipIpSnmpAgentAddress\n                2) equipStationID\n                3) equipLocation\n                4) equipIpSnmpAgentAddress\n                5) equipGosipAddress\n                6) equipManagerWakeUpIpAddr\n                7) equipManagerWakeUpAlarm')
mibBuilder.exportSymbols("SIAE-EQUIP-MIB", equipManager1IpAddr=equipManager1IpAddr, equipCurrentTime=equipCurrentTime, equipRequest=equipRequest, equipManagerWakeUpIpAddr=equipManagerWakeUpIpAddr, equipLocation=equipLocation, equipManagerWakeUpNotify=equipManagerWakeUpNotify, equipConfigChange=equipConfigChange, equipConfigChangeTrapEnable=equipConfigChangeTrapEnable, PYSNMP_MODULE_ID=equipment, equipManagerWakeUpAlarmSeverityCode=equipManagerWakeUpAlarmSeverityCode, equipLOMDisconnected=equipLOMDisconnected, equipIpEthOsiNetMask=equipIpEthOsiNetMask, equipManager1TrapVersion=equipManager1TrapVersion, equipment=equipment, equipLOMConnected=equipLOMConnected, equipManager2TrapVersion=equipManager2TrapVersion, equipManagerWakeUpTimeout=equipManagerWakeUpTimeout, equipManagerWakeUpAlarm=equipManagerWakeUpAlarm, equipIpEthNetMask=equipIpEthNetMask, equipLOMConfigEnable=equipLOMConfigEnable, equipLOMConnectedTrapEnable=equipLOMConnectedTrapEnable, equipManagerWakeUpGosipAddress=equipManagerWakeUpGosipAddress, equipIpEthDefGatewayIfIndex=equipIpEthDefGatewayIfIndex, equipL1L2IsIsRouting=equipL1L2IsIsRouting, equipLatitude=equipLatitude, equipUpTime=equipUpTime, equipType=equipType, equipOperationMngtControl=equipOperationMngtControl, equipOperationMngtInProgress=equipOperationMngtInProgress, equipMibVersion=equipMibVersion, equipIpEthDefGateway=equipIpEthDefGateway, equipStationID=equipStationID, equipIpSnmpAgentAddress=equipIpSnmpAgentAddress, equipConfigChangeStatus=equipConfigChangeStatus, equipLOMConnectedMonitor=equipLOMConnectedMonitor, equipManager2IpAddr=equipManager2IpAddr, equipIpEthAddress=equipIpEthAddress, equipOperationInProgress=equipOperationInProgress, equipIpEthVlanId=equipIpEthVlanId, equipLOMConnectedConfig=equipLOMConnectedConfig, equipManagerWakeUpTrapVersion=equipManagerWakeUpTrapVersion, equipGosipAddress=equipGosipAddress, equipLongitude=equipLongitude, equipIpEthOsiAddress=equipIpEthOsiAddress, equipDailyPmTimeZone=equipDailyPmTimeZone, equipOsiamParameter=equipOsiamParameter)
