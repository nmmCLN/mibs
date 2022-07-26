#
# PySNMP MIB module CTIF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTIF-EXT-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:45 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ctronMib2, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctronMib2")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, iso, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, IpAddress, ObjectIdentity, Counter64, MibIdentifier, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "iso", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "IpAddress", "ObjectIdentity", "Counter64", "MibIdentifier", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
commonDev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1))
ctIf = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2))
ctIfPort = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3))
ctIfCp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4))
ctSNMP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5))
ctSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6))
ctVirtual = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7))
ctStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8))
ctFramerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9))
ctIfHC = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10))
comDeviceTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 1), DisplayString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(6, 6), ValueSizeConstraint(8, 8), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceTime.setStatus('mandatory')
if mibBuilder.loadTexts: comDeviceTime.setDescription('The current time of day, in 24 hour format, as\n        measured by the device.  The representation shall\n        use the standard HHMMSS format.')
comDeviceDate = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comDeviceDate.setStatus('mandatory')
if mibBuilder.loadTexts: comDeviceDate.setDescription('The current date, as measured by the device.  The\n        representation shall use the standard MMDDYYYY \n        format.')
comDeviceBoardMap = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: comDeviceBoardMap.setStatus('mandatory')
if mibBuilder.loadTexts: comDeviceBoardMap.setDescription('Contains a bit encoded representation of slots that contain MIM\n        boards.  If a bit is one then that slot is occupied by a board.')
ctIfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1), )
if mibBuilder.loadTexts: ctIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfTable.setDescription('This table defines an extension to the interface table.')
ctIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctIfNumber"))
if mibBuilder.loadTexts: ctIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfEntry.setDescription('This defines each conceptual row within the ctIfTable')
ctIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfNumber.setDescription('This defines the interface that is being described.  This is the\n        same as ifIndex.')
ctIfPortCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortCnt.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfPortCnt.setDescription('This defines the number of ports on the interface that is being\n        described.')
ctIfConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfConnectionType.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfConnectionType.setDescription('Defines the specific type of the interface connection (BRIM, etc).\n        This is defined within ctron-oids.  This differs from the nature of\n        the interface as defined by ifType as found in MIB-II.')
ctIfLAA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfLAA.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfLAA.setDescription("This object is used by a device (with a Token Ring \n                interface) to set a Locally Administered Address (LAA) \n                for it's MAC hardware address.  When set, this LAA will\n                override the default Universally Administered Address or \n                burned in address of the interface. \n\n                For devices that do not support LAA: \n\n                        - a read will return all zeros.\n\n                        - any write attempt will return BADVALUE.\n\n                For devices that support LAA:\n\n                        - valid values are 4000 0000 0000 to 4000 7fff ffff, \n                          and 0000 0000 0000 (a value of all zeros, causes\n                          interface to use the burned in address).\n\n                        - a set (write) with an invalid value, returns BADVALUE.\n\n                        - after a write, new values will only become active\n                          after the Token Ring interface has been closed and\n                          then opened again.\n\n                        - a read of ctIfLAA will always return same value as\n                          ifPhysAddress, except in the case where;\n\n                                o ctIfLAA has been set, but interface has\n                                  not yet been closed and reopened, in\n                                  this case the last set value is returned.\n\n                Note that a read of ifPhysAddress will always return the\n                physical address currently being used by the interface.")
ctIfDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("full", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfDuplex.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfDuplex.setDescription('Defines the duplex mode that the interface is set to\n                operate in.\n\n                For devices that do not support this capability: \n\n                        - a read will return standard(2).\n\n                        - any write attempt will return BADVALUE.\n\n                        - fast ethernet devices will report other(1).')
ctIfCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("standard", 2), ("fullDuplex", 3), ("fastEthernet", 4), ("ethernetBased", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfCapability.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfCapability.setDescription('Defines the cabability of the underlying hardware in\n                supporting full duplex.  This object will have a value\n                of fullDuplex(3) if all hardware is capable of supporting\n                full duplex operation.')
ctIfRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redundant", 1), ("not-redundant", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfRedundancy.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRedundancy.setDescription('Defines whether or not an interface supports redundancy.')
ctIfPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1), )
if mibBuilder.loadTexts: ctIfPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfPortTable.setDescription('This table defines an extension to the interface table.')
ctIfPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctIfPortIfNumber"), (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"))
if mibBuilder.loadTexts: ctIfPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfPortEntry.setDescription('This defines each conceptual row within the ctIfPortTable')
ctIfPortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfPortPortNumber.setDescription('This defines the port that is being described.')
ctIfPortIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortIfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfPortIfNumber.setDescription('This defines the interface that the port being described is on.')
ctIfPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortType.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfPortType.setDescription('Defines the specific type of the port (EPIM, TPIM).\n         This is defined within ctron-oids.')
ctIfPortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notLinked", 1), ("linked", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfPortLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfPortLinkStatus.setDescription('Defines the status of the port connection.')
ctIfPortTrapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfPortTrapStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfPortTrapStatus.setDescription('Defines the trap forwarding status of the port.  A value of (1) \n     indicates that a trap WILL NOT be sent if the port goes down and\n     a value of (2) which is the default value, indicates that a trap\n     WILL be sent if the port goes down.')
ctCpTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1), )
if mibBuilder.loadTexts: ctCpTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctCpTable.setDescription('This table defines a Com Port Table.')
ctCpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctComPort"))
if mibBuilder.loadTexts: ctCpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctCpEntry.setDescription('This defines each conceptual row within the ctCPTable')
ctComPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctComPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctComPort.setDescription('This is the index into the Com Port Table and defines the Com Port \n        that is being described.  com1 = 1, com2 = 2')
ctCpFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("lm", 1), ("ups", 2), ("slip", 3), ("ppp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCpFunction.setStatus('mandatory')
if mibBuilder.loadTexts: ctCpFunction.setDescription('Defines the Com Port Function supported by that Com Port.')
ctIfNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfNum.setDescription('This defines the interface that is being described.  This is the\n        same as ifIndex.  This is only valid if ctCpFunction is SLIP or PPP,\n        otherwise, 0')
ctCpAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctCpAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctCpAdminStatus.setDescription('The administrative state of the Com Port.')
enableSNMPv1 = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableSNMPv1.setStatus('mandatory')
if mibBuilder.loadTexts: enableSNMPv1.setDescription('This object allows control over the SNMPv1 protocol.  If set to\n        a value of disable(1) then the SNMPv1 protocol will not be accepted\n        by the device.')
enableSNMPv2 = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableSNMPv2.setStatus('mandatory')
if mibBuilder.loadTexts: enableSNMPv2.setDescription('This object allows control over the SNMPv2 protocol.  If set to\n        a value of disable(1) then the SNMPv2 protocol will not be accepted\n        by the device.')
enableSNMPv1Counter64 = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enableSNMPv1Counter64.setStatus('mandatory')
if mibBuilder.loadTexts: enableSNMPv1Counter64.setDescription('This object allows control over the SNMPv1 protocol agent.  If \n        set to a value of enable(2) then the SNMPv1 agent will return \n        Counter64 objects using SNMPv2 syntax. If set to a value of disable(1) \n        then the SNMPv1 agent will return any Counter64 objects as Counter32.')
ctSonetTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1), )
if mibBuilder.loadTexts: ctSonetTable.setStatus('deprecated')
if mibBuilder.loadTexts: ctSonetTable.setDescription('This table defines the Sonet table.')
ctSonetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctSonetIfIndex"))
if mibBuilder.loadTexts: ctSonetEntry.setStatus('deprecated')
if mibBuilder.loadTexts: ctSonetEntry.setDescription('This defines each conceptual row within the ctSonetTable.')
ctSonetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctSonetIfIndex.setStatus('deprecated')
if mibBuilder.loadTexts: ctSonetIfIndex.setDescription('This defines the interface being described. It is the same as\n        IfIndex.')
ctSonetMediumType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctSonetMediumType.setStatus('deprecated')
if mibBuilder.loadTexts: ctSonetMediumType.setDescription('This variable identifies whether a SONET or a SDH\n         signal is used across this interface.')
ctVirtualIfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1), )
if mibBuilder.loadTexts: ctVirtualIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfTable.setDescription('This table defines a Virtual IF Table.')
ctVirtualIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctVirtualIfIndex"))
if mibBuilder.loadTexts: ctVirtualIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfEntry.setDescription('This defines each conceptual row within the ctVirtualIfTable')
ctVirtualIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfIndex.setDescription('Returns the virtual If Index.')
ctVirtualIfPhysicalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPhysicalInterface.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfPhysicalInterface.setDescription('This value displays the physical interface that owns\n          the virtual interface. This is the IfIndex from MIB-II.')
ctVirtualIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfType.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfType.setDescription('This value displays the physical interface type.')
ctVirtualIfNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfNumPorts.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfNumPorts.setDescription('This value displays the number of virtual ports.')
ctVirtualIfPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2), )
if mibBuilder.loadTexts: ctVirtualIfPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfPortTable.setDescription('This table defines the Virtual Port types.')
ctVirtualIfPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctVirtualIfPortIfIndex"), (0, "CTIF-EXT-MIB", "ctVirtualIfPortNumber"))
if mibBuilder.loadTexts: ctVirtualIfPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfPortEntry.setDescription('This defines each conceptual row within the ctVirtualIfPortTable.')
ctVirtualIfPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfPortIfIndex.setDescription('Returns the virtual If Index.')
ctVirtualIfPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfPortNumber.setDescription('The application port number of the port being described.')
ctVirtualIfPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("portVirtualTypeSvc", 1), ("portVirtualTypePvcLlc", 2), ("portVirtualTypePvcVcmux", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortType.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfPortType.setDescription('This defines the port type from ctron-oids.')
ctVirtualIfPortVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortVPI.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfPortVPI.setDescription('This returns the Virtual Path Identifier value.')
ctVirtualIfPortVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 7, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVirtualIfPortVCI.setStatus('mandatory')
if mibBuilder.loadTexts: ctVirtualIfPortVCI.setDescription('This returns the Virtual Channel Identifier value.')
ctStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1), )
if mibBuilder.loadTexts: ctStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctStatsTable.setDescription('This table defines the Stats table.')
ctStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1), ).setIndexNames((0, "CTIF-EXT-MIB", "ctStatsIfIndex"))
if mibBuilder.loadTexts: ctStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctStatsEntry.setDescription('This defines each StatsTable.')
ctStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctStatsIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctStatsIfIndex.setDescription('This defines the interface being described. It is the same as\n        IfIndex.')
ctStatsIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctStatsIfEnable.setStatus('mandatory')
if mibBuilder.loadTexts: ctStatsIfEnable.setDescription('This allows the interface to pass Token Ring MAC frames to the\nHOST for processing.\n          When disabled, stats will not be gathered on the interface.\n          Default is Enabled.\n         For devices that do not support this capability\n         any write attempt will return BADVALUE.')
ctIfHCStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1), )
if mibBuilder.loadTexts: ctIfHCStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfHCStatsTable.setDescription('This table defines an extension to the interface table.\n\n                This table consists of interface counters grouped together.\n                For each counter type in the table their is a 32 bit counter\n                and a 32 bit overflow counter.  This effectively provides a\n                method for counting up to 64 bits.')
ctIfHCStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctIfHCStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfHCStatsEntry.setDescription('This defines each conceptual row within the ctIfHCStatsTable.\n                 Entries in this table will exist for High Capacity Interfaces.')
ctIfInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfInOctets.setDescription('The total number of octets received on the interface,\n            including framing characters.')
ctIfInOctetsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInOctetsOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfInOctetsOverflows.setDescription('The number of times the associated ctIfInOctets\n            counter has overflowed.')
ctIfInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInUcastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfInUcastPkts.setDescription('The number of packets, delivered by this sub-layer to a\n            higher (sub-)layer, which were not addressed to a multicast\n            or broadcast address at this sub-layer.')
ctIfInUcastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInUcastPktsOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfInUcastPktsOverflows.setDescription('The number of times the associated ctIfInUcastPkts\n            counter has overflowed.')
ctIfInMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInMulticastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfInMulticastPkts.setDescription('The number of packets, delivered by this sub-layer to a\n            higher (sub-)layer, which were addressed to a multicast\n            address at this sub-layer.  For a MAC layer protocol, this\n            includes both Group and Functional addresses.')
ctIfInMulticastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInMulticastPktsOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfInMulticastPktsOverflows.setDescription('The number of times the associated ctIfInMulticastPkts\n            counter has overflowed.')
ctIfInBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInBroadcastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfInBroadcastPkts.setDescription('The number of packets, delivered by this sub-layer to a\n            higher (sub-)layer, which were addressed to a broadcast\n            address at this sub-layer.')
ctIfInBroadcastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfInBroadcastPktsOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfInBroadcastPktsOverflows.setDescription('The number of times the associated ctIfInBroadcastPkts\n            counter has overflowed.')
ctIfOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfOutOctets.setDescription('The total number of octets transmitted out of the\n            interface, including framing characters.')
ctIfOutOctetsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutOctetsOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfOutOctetsOverflows.setDescription('The number of times the associated ctIfOutOctets\n            counter has overflowed.')
ctIfOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutUcastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfOutUcastPkts.setDescription('The total number of packets that higher-level protocols\n            requested be transmitted, and which were not addressed to a\n            multicast or broadcast address at this sub-layer, including\n            those that were discarded or not sent.')
ctIfOutUcastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutUcastPktsOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfOutUcastPktsOverflows.setDescription('The number of times the associated ctIfOutUcastPkts\n            counter has overflowed.')
ctIfOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutMulticastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfOutMulticastPkts.setDescription('The total number of packets that higher-level protocols\n            requested be transmitted, and which were addressed to a\n            multicast address at this sub-layer, including those that\n            were discarded or not sent.  For a MAC layer protocol, this\n            includes both Group and Functional addresses.')
ctIfOutMulticastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutMulticastPktsOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfOutMulticastPktsOverflows.setDescription('The number of times the associated ctIfOutMulticastPkts\n            counter has overflowed.')
ctIfOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutBroadcastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfOutBroadcastPkts.setDescription('The total number of packets that higher-level protocols\n            requested be transmitted, and which were addressed to a\n            broadcast address at this sub-layer, including those that\n            were discarded or not sent.')
ctIfOutBroadcastPktsOverflows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 10, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfOutBroadcastPktsOverflows.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfOutBroadcastPktsOverflows.setDescription('The number of times the associated ctIfOutBroadcastPkts\n            counter has overflowed.')
mibBuilder.exportSymbols("CTIF-EXT-MIB", ctIfPortPortNumber=ctIfPortPortNumber, ctIfDuplex=ctIfDuplex, ctVirtualIfPortVPI=ctVirtualIfPortVPI, enableSNMPv2=enableSNMPv2, ctIfHCStatsEntry=ctIfHCStatsEntry, ctIfInOctets=ctIfInOctets, ctVirtualIfPortIfIndex=ctVirtualIfPortIfIndex, ctIfPortLinkStatus=ctIfPortLinkStatus, ctVirtual=ctVirtual, ctIfInBroadcastPktsOverflows=ctIfInBroadcastPktsOverflows, ctIfLAA=ctIfLAA, ctVirtualIfTable=ctVirtualIfTable, ctCpFunction=ctCpFunction, ctSonetTable=ctSonetTable, ctIfTable=ctIfTable, ctVirtualIfPortType=ctVirtualIfPortType, ctStatsEntry=ctStatsEntry, ctSonetIfIndex=ctSonetIfIndex, ctVirtualIfPortEntry=ctVirtualIfPortEntry, ctStatsIfEnable=ctStatsIfEnable, ctIfOutUcastPktsOverflows=ctIfOutUcastPktsOverflows, ctIfCapability=ctIfCapability, ctCpTable=ctCpTable, ctStatsTable=ctStatsTable, ctVirtualIfPhysicalInterface=ctVirtualIfPhysicalInterface, ctVirtualIfPortVCI=ctVirtualIfPortVCI, ctIfPortTrapStatus=ctIfPortTrapStatus, comDeviceTime=comDeviceTime, ctIfCp=ctIfCp, enableSNMPv1=enableSNMPv1, ctIfPortCnt=ctIfPortCnt, ctIfEntry=ctIfEntry, ctIfHC=ctIfHC, ctIfConnectionType=ctIfConnectionType, ctIfInUcastPkts=ctIfInUcastPkts, ctSNMP=ctSNMP, ctIfInOctetsOverflows=ctIfInOctetsOverflows, ctIfInMulticastPkts=ctIfInMulticastPkts, ctSonetMediumType=ctSonetMediumType, ctIfOutUcastPkts=ctIfOutUcastPkts, ctIfOutOctets=ctIfOutOctets, ctVirtualIfPortNumber=ctVirtualIfPortNumber, commonDev=commonDev, ctIfInMulticastPktsOverflows=ctIfInMulticastPktsOverflows, ctStats=ctStats, ctVirtualIfType=ctVirtualIfType, ctIfOutMulticastPktsOverflows=ctIfOutMulticastPktsOverflows, ctIfInBroadcastPkts=ctIfInBroadcastPkts, ctCpAdminStatus=ctCpAdminStatus, ctCpEntry=ctCpEntry, ctIfPortType=ctIfPortType, ctIfPort=ctIfPort, ctIfOutBroadcastPkts=ctIfOutBroadcastPkts, ctIfOutOctetsOverflows=ctIfOutOctetsOverflows, ctIfPortTable=ctIfPortTable, ctVirtualIfIndex=ctVirtualIfIndex, enableSNMPv1Counter64=enableSNMPv1Counter64, ctIfPortEntry=ctIfPortEntry, ctVirtualIfNumPorts=ctVirtualIfNumPorts, ctVirtualIfEntry=ctVirtualIfEntry, ctIfOutMulticastPkts=ctIfOutMulticastPkts, ctIfOutBroadcastPktsOverflows=ctIfOutBroadcastPktsOverflows, ctSonet=ctSonet, ctIfInUcastPktsOverflows=ctIfInUcastPktsOverflows, comDeviceDate=comDeviceDate, ctIfNum=ctIfNum, ctSonetEntry=ctSonetEntry, ctIfPortIfNumber=ctIfPortIfNumber, ctIfHCStatsTable=ctIfHCStatsTable, comDeviceBoardMap=comDeviceBoardMap, ctIfRedundancy=ctIfRedundancy, ctIfNumber=ctIfNumber, ctIf=ctIf, ctStatsIfIndex=ctStatsIfIndex, ctFramerConfig=ctFramerConfig, ctComPort=ctComPort, ctVirtualIfPortTable=ctVirtualIfPortTable)
