#
# PySNMP MIB module SILVERPEAK-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:23:19 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
silverpeakMgmt, silverpeakNotifications = mibBuilder.importSymbols("SILVERPEAK-SMI", "silverpeakMgmt", "silverpeakNotifications")
SilverpeakYesNo, SilverpeakSeqNum, SilverpeakAlarmSeverity = mibBuilder.importSymbols("SILVERPEAK-TC", "SilverpeakYesNo", "SilverpeakSeqNum", "SilverpeakAlarmSeverity")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Unsigned32, ModuleIdentity, NotificationType, IpAddress, TimeTicks, Integer32, Gauge32, Bits, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Unsigned32", "ModuleIdentity", "NotificationType", "IpAddress", "TimeTicks", "Integer32", "Gauge32", "Bits", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
silverpeakMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23867, 3, 1))
if mibBuilder.loadTexts: silverpeakMgmtMIB.setLastUpdated('201201060000Z')
if mibBuilder.loadTexts: silverpeakMgmtMIB.setOrganization('Silver Peak Systems, Inc.')
if mibBuilder.loadTexts: silverpeakMgmtMIB.setContactInfo('  URL: http://www.silver-peak.com/contact\n            E-mail: support@silver-peak.com ')
if mibBuilder.loadTexts: silverpeakMgmtMIB.setDescription('This module defines the management variables used to manage\n         and monitor appliance status.')
silverpeakMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1))
silverpeakMgmtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 4, 1))
silverpeakMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2))
silverpeakMgmtMIBScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1))
spsSystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsSystemVersion.setStatus('current')
if mibBuilder.loadTexts: spsSystemVersion.setDescription('System software version string')
spsProductModel = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsProductModel.setStatus('current')
if mibBuilder.loadTexts: spsProductModel.setDescription('System product model')
spsOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsOperStatus.setStatus('current')
if mibBuilder.loadTexts: spsOperStatus.setDescription('The current operational state of the appliance.')
spsActiveAlarmCount = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmCount.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmCount.setDescription('The number of active alarm entries in the alarm table -\n             spsActiveAlarmTable, defined under silverpeakMgmtMIBTables\n             subtree.')
spsSystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsSystemUptime.setStatus('current')
if mibBuilder.loadTexts: spsSystemUptime.setDescription('The amount of time in hundredth of a second since\n             this NX was last initialized.  Note that this is\n             different from sysUpTime in the SNMPv2-MIB [RFC1907]\n             because sysUpTime is the uptime of the network\n             management portion of the system.')
spsSystemSerial = MibScalar((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsSystemSerial.setStatus('current')
if mibBuilder.loadTexts: spsSystemSerial.setDescription('System serial number string')
silverpeakMgmtMIBTables = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2))
spsActiveAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1), )
if mibBuilder.loadTexts: spsActiveAlarmTable.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmTable.setDescription('A list of the active alarm entries. This represents the fault\n         conditions that are still active in the appliance.\n        ')
activeAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1), ).setIndexNames((0, "SILVERPEAK-MGMT-MIB", "spsActiveAlarmIndex"))
if mibBuilder.loadTexts: activeAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: activeAlarmEntry.setDescription('The active alarm entries that are still valid system faults.')
spsActiveAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: spsActiveAlarmIndex.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmIndex.setDescription('An index that uniquely identifies an entry in the\n        active alarm table.')
spsActiveAlarmSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 2), SilverpeakSeqNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmSeqNum.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmSeqNum.setDescription("The active alarm's sequence number at the time it was generated.")
spsActiveAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 3), SilverpeakAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmSeverity.setDescription('The alarm severity for the active alarm.')
spsActiveAlarmName = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmName.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmName.setDescription('A short name for the active alarm.')
spsActiveAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmDescr.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmDescr.setDescription('A description for the active alarm.')
spsActiveAlarmSource = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmSource.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmSource.setDescription('The source for the active alarm.')
spsActiveAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmType.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmType.setDescription('The alarm type for the active alarm.')
spsActiveAlarmAcked = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 8), SilverpeakYesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmAcked.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmAcked.setDescription('Identifies if the user has acknowledged the alarm.')
spsActiveAlarmActive = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 9), SilverpeakYesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmActive.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmActive.setDescription('Identifies if the alarm is currently active.')
spsActiveAlarmClearable = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 10), SilverpeakYesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmClearable.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmClearable.setDescription('Identifies if the user can manually clear the alarm.')
spsActiveAlarmLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmLogTime.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmLogTime.setDescription('The value of sysUpTime when the alarm was generated.')
spsActiveAlarmServiceAffect = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 12), SilverpeakYesNo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmServiceAffect.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmServiceAffect.setDescription('Identifies if the alarm is service affecting.')
spsActiveAlarmTypeId = MibTableColumn((1, 3, 6, 1, 4, 1, 23867, 3, 1, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spsActiveAlarmTypeId.setStatus('current')
if mibBuilder.loadTexts: spsActiveAlarmTypeId.setDescription("An ID that uniquely identifies a type of alarm.\n         The following is a list of currently defined type IDs\n         (ID listed below is in hexadecimal):\n\n            ID     Description\n            -----  ------------------------------------------\n            10000  Tunnel remote ID is misconfigured\n            10001  Tunnel state is Down\n            10002  Tunnel VRRP IP is misconfigured\n            10003  Tunnel keepalive version mismatch\n            10004  Tunnel WCCP GID is misconfigured\n            10005  Tunnel software version mismatch\n            10006  Connecting to a non-VX-X is not supported. \n                   Please contact sales@silver-peak.com to discuss your options.\n            10007  Duplicate Silver Peak license detected on peer device.\n            10008  Tunnel local IP address not owned by this appliance\n            10009  Tunnel software version mismatch results in reduced functionality.\n            1000a  Tunnel peer encapsulation mode mismatch detected.\n            1000b  UDP Destination Port is the same as flow redirection port\n\n            20000  Tunnel has unexpected traffic class error\n\n            30000  RAID array is degraded\n            30001  Disk is failed\n            30002  Disk is degraded\n            30003  Fan failure detected\n            30004  System bypass mode\n            30005  LAN/WAN fail-to-wire card failure\n            30006  LAN/WAN fail-to-wire card relay failure\n            30007  Encryption card hardware failure\n            30008  Network interface admin down\n            30009  Network interface link down\n            3000a  Management interface link down\n            3000b  Interface is half duplex\n            3000c  Interface speed is 10 Mbps\n            3000d  Config DB disk full\n            3000e  Operating System disk full\n            3000f  File system disk full\n            30010  Datapath internal loopback test failed\n            30011  WAN next-hop unreachable\n            30012  VRRP instance is down\n            30013  VRRP state changed from Master to Backup\n            30014  WAN next-hop router discovered on a LAN port\n                   (box is in backwards)\n            30015  Disk is not in service\n            30016  Disk is rebuilding\n            30017  Disk removed by operator\n            30018  LAN/WAN interfaces have different admin states\n            30019  LAN/WAN interfaces have different link carrier states\n            3001a  LAN/WAN interface has been shutdown due to\n                   link propagation of paired interface\n            3001b  Disk SMART threshold exceeded\n            3001c  Flow redirection cluster peer is down\n            3001d  Bonding members have different speed/duplex\n            3001e  WCCP adjacency(ies) down\n            3001f  WCCP assignment table mismatch\n            30020  Power supply not connected, not powered or failed\n            30021  NIC interface failure\n            30022  LAN next-hop unreachable\n            30023  Unexpected system restart\n            30024  Insufficient configured memory size for this virtual appliance\n            30025  Insufficient configured processor count for this virtual appliance\n            30026  Insufficient configured disk storage for this virtual appliance\n            30027  Interfaces have different MTUs\n            30028  Interfaces have different MTUs\n            30029  Bridge loop is detected\n            3002a  Bridge creation failed\n            3002b  Network interface is unassigned\n            3002c  System optimization turned off\n            3002d  Sub-optimal configured memory size for this virtual appliance\n            3002e  Sub-optimal configured processor count for this virtual appliance\n            3002f  Sub-optimal configured disk storage for this virtual appliance\n\n\n            40000  Software upgrade process has failed\n            40001  System is low on resources\n            40002  Significant change in time of day has occurred,\n                   and might compromise statistics.\n            40003  The licensing for this virtual appliance has expired.\n            40004  There is no license installed on this virtual appliance.\n            40005  A disk self test has been performed. The system will\n                   require a reboot after the test.\n            40006  The SSL private key is invalid.\n            40007  The SSL certificate is not yet valid.\n            40008  The SSL certificate has expired.\n            40009  The NTP server is unreachable.\n            4000a  Virtual appliance license expires on yyyy/mm/dd.\n            4000b  Virtual appliance license expires on yyyy/mm/dd.\n            4000c  Invalid virtual appliance license.\n            4000d  Dual Wan-nexthop topology configuration no longer supported.\n            4000e  Setting system wan-nexthop to VLAN nhop is no longer necessary.\n            4000f  Minor inconsistencies during QOS upgrade.\n            40010  Major inconsistencies during QOS upgrade.\n            40011  Tunnel IP hdr disable setting was discarded during upgrade.\n            40012  A very large range has been configured for a local subnet.\n            40013  A peer name has been specified in a route-map that can't be resolved.\n            40014  Shaper max bandwidth exceeds system bandwidth\n            40015  Software capability token exceeds warning threshold\n            40016  Software capability token has exceeded the required limit\n            40017  Silvepeak Portal is unreachable\n            40018  Silverpeak Portal is unreachable for setting up a remote help session\n            40019  An application has been deleted on the Silver Peak portal\n            4001a  Boost Limiting MTS\n            4001b  Bad portal registration data\n            4001c  EdgeConnect Base license not granted\n            4001d  Orchestrator is unreachable from appliance using HTTPS\n            4001e  Silver Peak Portal is unreachable for licensing\n            4001f  Silver Peak Portal hostname cannot be resolved\n            40020  Edge Connect Plus license not granted\n            40021  Edge Connect Boost license not granted\n            40022  Appliance has not been approved for licensing by Orchestrator\n            40023  Software capability token related alarm\n            40024  A NATed interface connected to Internet has no public IP address\n            40025  Initial admin password is not yet changed\n            40026  DHCP server mis-configuration\n            40027  Subnet table has exceeded high-water level for BGP/OSPF entries\n            40028  Subnet table has reached maximum capacity\n            40029  Unable to resolve Orchestrator DNS name\n            4002a  Builtin CA certificate is not valid\n            4002b  CA certificate Bundle is not valid\n            4002c  A BGP peer session is no longer in Established state\n            4002d  An IP SLA monitor is in Down state\n            4002e  An OSPF neighbor session is no longer in Full state\n            4002f  DNS Proxy is down\n            40030  EC Licensing Warning\n\n\n            50001  WAN-side transmit throughput TCA\n            50002  LAN-side receive throughput TCA\n            50003  Total number of optimized flows TCA\n            50004  Total number of flows TCA\n            50005  File-system utilization TCA\n            50006  Tunnel latency TCA\n            50007  Tunnel loss pre-FEC TCA\n            50008  Tunnel loss post-FEC TCA\n            50009  Tunnel OOP pre-POC TCA\n            5000a  Tunnel OOP post-POC TCA\n            5000b  Tunnel utilization TCA\n            5000c  Tunnel reduction TCA\n            5000d  Appliance capacity TCA\n            -----  ------------------------------------------")
spsNotifyAlarm = NotificationType((1, 3, 6, 1, 4, 1, 23867, 4, 1, 1)).setObjects(("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSource"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeverity"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmDescr"))
if mibBuilder.loadTexts: spsNotifyAlarm.setStatus('current')
if mibBuilder.loadTexts: spsNotifyAlarm.setDescription('A notification that the system has just generated and alarm.')
silverpeakMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 1))
silverpeakMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2))
silverpeakMgmtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 1, 1)).setObjects(("SILVERPEAK-MGMT-MIB", "silverpeakMgmtGroup"), ("SILVERPEAK-MGMT-MIB", "silverpeakMgmtNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    silverpeakMgmtCompliance = silverpeakMgmtCompliance.setStatus('current')
if mibBuilder.loadTexts: silverpeakMgmtCompliance.setDescription('The compliance statement for agents implementing \n                silverpeakMgmtMIB.')
silverpeakMgmtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2, 1)).setObjects(("SILVERPEAK-MGMT-MIB", "spsSystemVersion"), ("SILVERPEAK-MGMT-MIB", "spsProductModel"), ("SILVERPEAK-MGMT-MIB", "spsOperStatus"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeqNum"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSeverity"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmName"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmDescr"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmSource"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmType"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmAcked"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmActive"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmClearable"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmLogTime"), ("SILVERPEAK-MGMT-MIB", "spsActiveAlarmServiceAffect"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    silverpeakMgmtGroup = silverpeakMgmtGroup.setStatus('current')
if mibBuilder.loadTexts: silverpeakMgmtGroup.setDescription('A collection of objects used to retrieve management\n                 information from Silverpeak Systems appliances.\n                ')
silverpeakMgmtNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 23867, 3, 1, 2, 2, 3)).setObjects(("SILVERPEAK-MGMT-MIB", "spsNotifyAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    silverpeakMgmtNotifyGroup = silverpeakMgmtNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: silverpeakMgmtNotifyGroup.setDescription('A collection of the Notifications supported in\n                 the management MIB.')
mibBuilder.exportSymbols("SILVERPEAK-MGMT-MIB", silverpeakMgmtMIBTables=silverpeakMgmtMIBTables, silverpeakMgmtCompliance=silverpeakMgmtCompliance, PYSNMP_MODULE_ID=silverpeakMgmtMIB, spsActiveAlarmDescr=spsActiveAlarmDescr, silverpeakMgmtMIBScalars=silverpeakMgmtMIBScalars, spsActiveAlarmCount=spsActiveAlarmCount, spsActiveAlarmTable=spsActiveAlarmTable, spsActiveAlarmActive=spsActiveAlarmActive, spsActiveAlarmServiceAffect=spsActiveAlarmServiceAffect, spsActiveAlarmAcked=spsActiveAlarmAcked, spsActiveAlarmSeqNum=spsActiveAlarmSeqNum, spsSystemUptime=spsSystemUptime, silverpeakMgmtMIB=silverpeakMgmtMIB, spsSystemVersion=spsSystemVersion, silverpeakMgmtMIBCompliances=silverpeakMgmtMIBCompliances, spsActiveAlarmSource=spsActiveAlarmSource, spsActiveAlarmClearable=spsActiveAlarmClearable, silverpeakMgmtMIBConformance=silverpeakMgmtMIBConformance, silverpeakMgmtNotifyGroup=silverpeakMgmtNotifyGroup, spsActiveAlarmTypeId=spsActiveAlarmTypeId, silverpeakMgmtGroup=silverpeakMgmtGroup, spsActiveAlarmName=spsActiveAlarmName, spsProductModel=spsProductModel, spsActiveAlarmSeverity=spsActiveAlarmSeverity, silverpeakMgmtMIBGroups=silverpeakMgmtMIBGroups, spsActiveAlarmIndex=spsActiveAlarmIndex, spsNotifyAlarm=spsNotifyAlarm, silverpeakMgmtMIBObjects=silverpeakMgmtMIBObjects, spsActiveAlarmType=spsActiveAlarmType, spsOperStatus=spsOperStatus, activeAlarmEntry=activeAlarmEntry, spsActiveAlarmLogTime=spsActiveAlarmLogTime, spsSystemSerial=spsSystemSerial, silverpeakMgmtMIBNotifications=silverpeakMgmtMIBNotifications)
