#
# PySNMP MIB module SL-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-CHASSIS-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:39 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfIntervalCount, PerfCurrentCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfCurrentCount", "PerfTotalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, NotificationType, iso, MibIdentifier, ModuleIdentity, IpAddress, TimeTicks, Counter32, Integer32, Unsigned32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "NotificationType", "iso", "MibIdentifier", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter32", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity")
RowStatus, PhysAddress, TextualConvention, TimeStamp, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "PhysAddress", "TextualConvention", "TimeStamp", "TruthValue", "DisplayString")
slChassis = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18))
if mibBuilder.loadTexts: slChassis.setLastUpdated('201305050000Z')
if mibBuilder.loadTexts: slChassis.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slChassis.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slChassis.setDescription('This MIB module describes the Multi-Chassis information')
slChassisInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1))
slChassisSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2))
slChassisInfoNodeSlotId = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slChassisInfoNodeSlotId.setStatus('current')
if mibBuilder.loadTexts: slChassisInfoNodeSlotId.setDescription('The slot ID of the node.\n         This number is assigned to the node before it is a part of the chassis.\n         Slot ID should be assigned also to the GNE nodes.\n         The Slot ID should be unique in the chassis.')
slChassisInfoNodeRole = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("gneNode", 1), ("internalSlotNode", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slChassisInfoNodeRole.setStatus('current')
if mibBuilder.loadTexts: slChassisInfoNodeRole.setDescription('The role of the node.\n         gneNode - for Master or Backup chassis GNE node.\n         internalSlotNode - for non gne node.\n         none - the node is in a simple chassis')
slChassisInfoLanVrrpIp = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slChassisInfoLanVrrpIp.setStatus('current')
if mibBuilder.loadTexts: slChassisInfoLanVrrpIp.setDescription('The VRRP ip of the node on the LAN interface.')
slChassisInfoOscVrrpIp = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slChassisInfoOscVrrpIp.setStatus('current')
if mibBuilder.loadTexts: slChassisInfoOscVrrpIp.setDescription('The VRRP ip of the node on the OSC interface.')
slChassisInfoTopology = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("osc", 1), ("lan", 2), ("simple", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slChassisInfoTopology.setStatus('current')
if mibBuilder.loadTexts: slChassisInfoTopology.setDescription('The topology mode of the multichassis:\n         osc - the management use the LAN IP of the GNE and VRRP.\n         lan - the management use the OSC IP of the GNE and VRRP.\n         simple - no GNE to the chassis. Used for display only')
slChassisInfoVrrpEnable = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slChassisInfoVrrpEnable.setStatus('current')
if mibBuilder.loadTexts: slChassisInfoVrrpEnable.setDescription('Enable/Disable the activation of the VRRP protocol by the GNE')
slChassisSlotTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1), )
if mibBuilder.loadTexts: slChassisSlotTable.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotTable.setDescription('This table contains the chassis slots.')
slChassisSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1), ).setIndexNames((0, "SL-CHASSIS-MIB", "slChassisSlotId"))
if mibBuilder.loadTexts: slChassisSlotEntry.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotEntry.setDescription('An entry in the Chassis Slot table.')
slChassisSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotId.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotId.setDescription('The slot ID of the node.')
slChassisSlotRole = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gneNode", 1), ("internalNode", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotRole.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotRole.setDescription('The role of the node.\n         gneNode - for Master or Backup chassis GNE node.\n         internalNode - for non gne node')
slChassisSlotInternalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotInternalIp.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotInternalIp.setDescription('The internal ip of the node.\n        This address is used to identify the node and not for management access.')
slChassisSlotProductType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotProductType.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotProductType.setDescription('The sysObjectID of the node.')
slChassisSlotSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotSysName.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotSysName.setDescription('The SysName of the node')
slChassisSlotSnmp161Port = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotSnmp161Port.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotSnmp161Port.setDescription('The SNMP Gte/Set port of the node.')
slChassisSlotSnmp162MinPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotSnmp162MinPort.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotSnmp162MinPort.setDescription('The minimal SNMP Trap port of the node.')
slChassisSlotSnmp162MaxPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotSnmp162MaxPort.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotSnmp162MaxPort.setDescription('The maximal SNMP Trap port of the node.')
slChassisSlotHttpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotHttpPort.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotHttpPort.setDescription('The HTTP port of the node.')
slChassisSlotTelnetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotTelnetPort.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotTelnetPort.setDescription('The Telnet port of the node.')
slChassisSlotFtpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotFtpPort.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotFtpPort.setDescription('The Ftp port of the node.')
slChassisSlotTL1Port = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotTL1Port.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotTL1Port.setDescription('The TL1 port of the node.')
slChassisSlotPingIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotPingIdentifier.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotPingIdentifier.setDescription('The ping identifier of the node.')
slChassisSlotHttpsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotHttpsPort.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotHttpsPort.setDescription('The HTTPS port of the node.')
slChassisSlotSshPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotSshPort.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotSshPort.setDescription('The SSH port of the node.')
slChassisSlotSTL1Port = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 18, 2, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slChassisSlotSTL1Port.setStatus('current')
if mibBuilder.loadTexts: slChassisSlotSTL1Port.setDescription('The TL1 over SSH port of the node.')
mibBuilder.exportSymbols("SL-CHASSIS-MIB", slChassisSlotSTL1Port=slChassisSlotSTL1Port, slChassisSlotRole=slChassisSlotRole, slChassisSlotTL1Port=slChassisSlotTL1Port, slChassisInfoOscVrrpIp=slChassisInfoOscVrrpIp, PYSNMP_MODULE_ID=slChassis, slChassisInfoNodeRole=slChassisInfoNodeRole, slChassisSlotInternalIp=slChassisSlotInternalIp, slChassisInfoLanVrrpIp=slChassisInfoLanVrrpIp, slChassisInfo=slChassisInfo, slChassis=slChassis, slChassisSlotSnmp161Port=slChassisSlotSnmp161Port, slChassisSlotHttpPort=slChassisSlotHttpPort, slChassisSlotTelnetPort=slChassisSlotTelnetPort, slChassisInfoNodeSlotId=slChassisInfoNodeSlotId, slChassisSlotSnmp162MinPort=slChassisSlotSnmp162MinPort, slChassisSlotSnmp162MaxPort=slChassisSlotSnmp162MaxPort, slChassisSlotProductType=slChassisSlotProductType, slChassisSlotId=slChassisSlotId, slChassisInfoTopology=slChassisInfoTopology, slChassisSlotTable=slChassisSlotTable, slChassisInfoVrrpEnable=slChassisInfoVrrpEnable, slChassisSlotSshPort=slChassisSlotSshPort, slChassisSlotPingIdentifier=slChassisSlotPingIdentifier, slChassisSlot=slChassisSlot, slChassisSlotEntry=slChassisSlotEntry, slChassisSlotHttpsPort=slChassisSlotHttpsPort, slChassisSlotFtpPort=slChassisSlotFtpPort, slChassisSlotSysName=slChassisSlotSysName)
