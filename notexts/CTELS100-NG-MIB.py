#
# PySNMP MIB module CTELS100-NG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTELS100-NG-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:40 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Integer32, NotificationType, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, mgmt, Unsigned32, Gauge32, Counter32, iso, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Integer32", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mgmt", "Unsigned32", "Gauge32", "Counter32", "iso", "IpAddress", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mib_2 = MibIdentifier((1, 3, 6, 1, 2, 1)).setLabel("mib-2")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
els100 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1011))
els100SystemConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1011, 1))
els100Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1011, 3))
els100SysSerialno = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SysSerialno.setStatus('mandatory')
els100SysTftpIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysTftpIPAddress.setStatus('mandatory')
els100SysTftpFilename = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysTftpFilename.setStatus('mandatory')
els100SysPowerupCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SysPowerupCount.setStatus('mandatory')
els100SysBrcastCutoffRate = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysBrcastCutoffRate.setStatus('mandatory')
els100SysGatewayIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysGatewayIPAddress.setStatus('mandatory')
els100SysTftpStartDownload = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("download", 1), ("noDownload", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysTftpStartDownload.setStatus('mandatory')
els100SysBootPDhcpEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysBootPDhcpEnable.setStatus('mandatory')
els100SysReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysReset.setStatus('mandatory')
els100SysSyslogServer = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 11), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysSyslogServer.setStatus('mandatory')
els100SysLowestSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysLowestSyslogSeverity.setStatus('mandatory')
els100SysComPortEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SysComPortEnable.setStatus('mandatory')
els100SysBoardID = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SysBoardID.setStatus('mandatory')
els100PortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1011, 2), )
if mibBuilder.loadTexts: els100PortTable.setStatus('mandatory')
els100PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1), ).setIndexNames((0, "CTELS100-NG-MIB", "els100Port"))
if mibBuilder.loadTexts: els100PortEntry.setStatus('mandatory')
els100Port = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100Port.setStatus('mandatory')
els100PortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100PortStatus.setStatus('mandatory')
els100PortDuplexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half", 1), ("full", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortDuplexStatus.setStatus('mandatory')
els100PortForwardedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100PortForwardedFrames.setStatus('mandatory')
els100PortRcvdLocalFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100PortRcvdLocalFrames.setStatus('mandatory')
els100PortName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortName.setStatus('mandatory')
els100PortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortEnable.setStatus('mandatory')
els100PortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tenMbps", 1), ("oneHundredMbps", 2), ("oneThousandMbps", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortSpeed.setStatus('mandatory')
els100PortAutonegEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortAutonegEnable.setStatus('mandatory')
els100PortFlowControlEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100PortFlowControlEnable.setStatus('mandatory')
els100PortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("unknown", 1), ("ieee10BaseT", 2), ("ieee100BaseTx", 3), ("ieee100BaseFx-MM", 4), ("ieee100BaseFx-SM", 5), ("ieee1000BaseCx", 6), ("ieee1000BaseLx", 7), ("ieee1000BaseSx", 8), ("ieee1000BaseT", 9), ("ieee1000BaseX", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100PortType.setStatus('mandatory')
els100SwitchIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchIPAddress.setStatus('mandatory')
els100SwitchSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchSubnetMask.setStatus('mandatory')
els100ActiveAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100ActiveAgingTime.setStatus('mandatory')
els100SwitchSTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchSTPStatus.setStatus('mandatory')
els100SwitchManager = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6))
els100SwitchTrapRcvr1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapRcvr1.setStatus('mandatory')
els100SwitchTrapCommunity1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapCommunity1.setStatus('mandatory')
els100SwitchTrapRcvr2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapRcvr2.setStatus('mandatory')
els100SwitchTrapCommunity2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapCommunity2.setStatus('mandatory')
els100SwitchTrapRcvr3 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapRcvr3.setStatus('mandatory')
els100SwitchTrapCommunity3 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapCommunity3.setStatus('mandatory')
els100SwitchTrapRcvr4 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapRcvr4.setStatus('mandatory')
els100SwitchTrapCommunity4 = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 6, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchTrapCommunity4.setStatus('mandatory')
els100SwitchPortMirroringStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchPortMirroringStatus.setStatus('mandatory')
els100SwitchMirroredPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchMirroredPort.setStatus('mandatory')
els100SwitchMirroringPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchMirroringPort.setStatus('mandatory')
els100SwitchXmitMirrorEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchXmitMirrorEnable.setStatus('mandatory')
els100SwitchRcvMirrorEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchRcvMirrorEnable.setStatus('mandatory')
els100SwitchVlanEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanEnable.setStatus('mandatory')
els100SwitchVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13), )
if mibBuilder.loadTexts: els100SwitchVlanConfigTable.setStatus('mandatory')
els100SwitchVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1), ).setIndexNames((0, "CTELS100-NG-MIB", "els100SwitchVlanId"))
if mibBuilder.loadTexts: els100SwitchVlanEntry.setStatus('mandatory')
els100SwitchVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanId.setStatus('mandatory')
els100SwitchVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanName.setStatus('mandatory')
els100SwitchVlanPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanPorts.setStatus('mandatory')
els100SwitchVlanEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanEgressPorts.setStatus('mandatory')
els100SwitchVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanStatus.setStatus('mandatory')
els100SwitchVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14), )
if mibBuilder.loadTexts: els100SwitchVlanPortTable.setStatus('mandatory')
els100SwitchVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14, 1), ).setIndexNames((0, "CTELS100-NG-MIB", "els100SwitchVlanPortId"))
if mibBuilder.loadTexts: els100SwitchVlanPortEntry.setStatus('mandatory')
els100SwitchVlanPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SwitchVlanPortId.setStatus('mandatory')
els100SwitchVlanPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanPvid.setStatus('mandatory')
els100SwitchVlanPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hybrid", 1), ("access", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchVlanPortType.setStatus('mandatory')
els100SwitchPriorityEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchPriorityEnable.setStatus('mandatory')
els100SwitchPriorityThreshold = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchPriorityThreshold.setStatus('mandatory')
els100SwitchPriorityPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1011, 3, 17), )
if mibBuilder.loadTexts: els100SwitchPriorityPortTable.setStatus('mandatory')
els100SwitchPriorityPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1011, 3, 17, 1), ).setIndexNames((0, "CTELS100-NG-MIB", "els100SwitchPriorityPortId"))
if mibBuilder.loadTexts: els100SwitchPriorityPortEntry.setStatus('mandatory')
els100SwitchPriorityPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 17, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: els100SwitchPriorityPortId.setStatus('mandatory')
els100SwitchPriorityDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1011, 3, 17, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchPriorityDefault.setStatus('mandatory')
els100SwitchSpanningTreeStandby = MibScalar((1, 3, 6, 1, 4, 1, 52, 1011, 3, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: els100SwitchSpanningTreeStandby.setStatus('mandatory')
mibBuilder.exportSymbols("CTELS100-NG-MIB", els100SwitchVlanEgressPorts=els100SwitchVlanEgressPorts, els100PortAutonegEnable=els100PortAutonegEnable, els100SwitchPriorityDefault=els100SwitchPriorityDefault, els100SysTftpFilename=els100SysTftpFilename, els100SwitchVlanPvid=els100SwitchVlanPvid, els100SwitchTrapCommunity1=els100SwitchTrapCommunity1, cabletron=cabletron, els100SysReset=els100SysReset, els100PortName=els100PortName, els100SwitchSTPStatus=els100SwitchSTPStatus, els100SwitchPriorityThreshold=els100SwitchPriorityThreshold, els100SwitchTrapRcvr3=els100SwitchTrapRcvr3, els100SwitchMirroringPort=els100SwitchMirroringPort, els100SwitchIPAddress=els100SwitchIPAddress, els100SwitchVlanName=els100SwitchVlanName, els100SwitchXmitMirrorEnable=els100SwitchXmitMirrorEnable, els100SwitchTrapCommunity4=els100SwitchTrapCommunity4, els100SwitchPortMirroringStatus=els100SwitchPortMirroringStatus, els100SysSyslogServer=els100SysSyslogServer, els100SwitchPriorityPortEntry=els100SwitchPriorityPortEntry, els100SwitchPriorityPortTable=els100SwitchPriorityPortTable, els100PortDuplexStatus=els100PortDuplexStatus, els100SysBoardID=els100SysBoardID, els100SwitchVlanEntry=els100SwitchVlanEntry, els100SwitchVlanPortId=els100SwitchVlanPortId, els100SwitchTrapRcvr1=els100SwitchTrapRcvr1, els100SwitchPriorityPortId=els100SwitchPriorityPortId, els100SysSerialno=els100SysSerialno, els100PortSpeed=els100PortSpeed, els100SwitchVlanPorts=els100SwitchVlanPorts, els100SwitchVlanStatus=els100SwitchVlanStatus, els100SwitchRcvMirrorEnable=els100SwitchRcvMirrorEnable, els100SwitchTrapRcvr4=els100SwitchTrapRcvr4, els100SwitchSpanningTreeStandby=els100SwitchSpanningTreeStandby, els100Port=els100Port, els100SwitchVlanId=els100SwitchVlanId, els100Switch=els100Switch, els100SystemConfig=els100SystemConfig, els100SwitchVlanConfigTable=els100SwitchVlanConfigTable, els100SysTftpStartDownload=els100SysTftpStartDownload, els100PortType=els100PortType, els100ActiveAgingTime=els100ActiveAgingTime, els100SwitchVlanPortTable=els100SwitchVlanPortTable, els100PortForwardedFrames=els100PortForwardedFrames, els100SwitchManager=els100SwitchManager, els100SwitchTrapRcvr2=els100SwitchTrapRcvr2, els100SwitchTrapCommunity2=els100SwitchTrapCommunity2, els100SysBrcastCutoffRate=els100SysBrcastCutoffRate, els100PortEnable=els100PortEnable, els100SwitchMirroredPort=els100SwitchMirroredPort, els100PortRcvdLocalFrames=els100PortRcvdLocalFrames, mib_2=mib_2, els100SysGatewayIPAddress=els100SysGatewayIPAddress, els100=els100, els100SwitchVlanEnable=els100SwitchVlanEnable, els100SysBootPDhcpEnable=els100SysBootPDhcpEnable, els100SysLowestSyslogSeverity=els100SysLowestSyslogSeverity, els100PortEntry=els100PortEntry, els100PortStatus=els100PortStatus, els100SwitchPriorityEnable=els100SwitchPriorityEnable, els100PortFlowControlEnable=els100PortFlowControlEnable, els100SysPowerupCount=els100SysPowerupCount, els100SysComPortEnable=els100SysComPortEnable, els100SwitchVlanPortEntry=els100SwitchVlanPortEntry, els100SysTftpIPAddress=els100SysTftpIPAddress, els100SwitchVlanPortType=els100SwitchVlanPortType, els100SwitchSubnetMask=els100SwitchSubnetMask, els100SwitchTrapCommunity3=els100SwitchTrapCommunity3, els100PortTable=els100PortTable)
