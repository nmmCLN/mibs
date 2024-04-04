#
# PySNMP MIB module HMRINGARC-MGMT-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/hmARC
# Produced by pysmi-1.1.12 at Thu Apr  4 09:18:52 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hmRingRedundancy, = mibBuilder.importSymbols("HMRING-MGMT-SNMP-MIB", "hmRingRedundancy")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, TimeTicks, MibIdentifier, Counter32, Unsigned32, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "TimeTicks", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmARC = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 14, 5, 7))
hmARC.setRevisions(('2010-09-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hmARC.setRevisionsDescriptions(('Initial Release',))
if mibBuilder.loadTexts: hmARC.setLastUpdated('201009011200Z')
if mibBuilder.loadTexts: hmARC.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hmARC.setContactInfo(' Contact: Customer Support\r\n\t\t\t\t   Postal: Hirschmann Automation and Control GmbH\r\n\t\t\t\t\t\t   Stuttgarter Strasse 45-51\r\n\t\t\t\t\t\t   DE-72654 Neckartenzlingen\r\n\t\t\t\t\t\t   Germany\r\n\t\t\t\t\t  Tel: +49-7127-14-1981\r\n\t\t\t\t\t  Fax: +49-7127-14-1542\r\n\t\t\t\t      URL: www.hicomcenter.com\r\n\t\t\t\t   E-mail: hicomcenter@hirschmann.com')
if mibBuilder.loadTexts: hmARC.setDescription('The Hirschmann Private Automatic Ring Configuration MIB definitions.')
hmArcManagerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1))
hmArcManagerStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2))
hmArcClientConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 3))
hmArcClientStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4))
hmArcManagerAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmArcManagerAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerAdminStatus.setDescription('The administratively desired status of the ARC manager.\r\n\t\t\t\t\r\n\t\t\t\t enabled(1): ARC manager is active, the device can check and configure other ARC devices.\r\n\t\t\t\t disabled(2): ARC manager is inactive, neither checking nor automatic configuring can be done.')
hmArcManagerRedProtocol = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("mrp", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmArcManagerRedProtocol.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerRedProtocol.setDescription('The ring redundancy protocol the clients will be configured for. Parameters like VLAN ID\r\n\t\t\t\t and timings are taken from the current redundancy manager configuration.\r\n\t\t\t\t \r\n\t\t\t\t mrp(1): Media Redundancy Protocol, according to IEC62439-2.')
hmArcManagerPrimGroupID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerPrimGroupID.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerPrimGroupID.setDescription('Unique index to identify the slot number of\r\n                                the primary link of the ARC manager. This value is never\r\n                                greater than hmSysGroupCapacity. ')
hmArcManagerPrimIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerPrimIfIndex.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerPrimIfIndex.setDescription('Interface index of the primary link of the ARC manager.')
hmArcManagerRedGroupID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerRedGroupID.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerRedGroupID.setDescription('Unique index to identify the slot number of\r\n                                the redundant link of the ARC manager. This value is never\r\n                                greater than hmSysGroupCapacity. ')
hmArcManagerRedIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerRedIfIndex.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerRedIfIndex.setDescription('Interface index of the redundant link of the ARC manager.')
hmArcManagerVlanID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerVlanID.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerVlanID.setDescription('VLAN identifier of the ARC manager. \r\n                If value is set to 0 no VLAN is assigned.')
hmArcManagerAction = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("checkTopology", 2), ("configureRing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmArcManagerAction.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerAction.setDescription('The actions the ARC manager is able to activate.\r\n\t\t\t\t\r\n\t\t\t\t This object, when read, returns noAction(1) if no action is currently running.\r\n\t\t\t\t checkTopology(2): Checks the topology connected to the given primary and redundant \r\n\t\t\t\t     port and also fills the hmArcCheckResultTable, especially if an invalid topology \r\n\t\t\t\t     was found.\r\n\t\t\t\t configureRing(3): Automatically configures the ring devices connected to the given \r\n\t\t\t\t     primary and redundant port. A successful checkTopology is prerequisite.')
hmArcManagerActionResult = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noAction", 1), ("pending", 2), ("closedRing", 3), ("configuredRing", 4), ("openRing", 5), ("invalidTopology", 6), ("configFailed", 7), ("configSuccessful", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcManagerActionResult.setStatus('current')
if mibBuilder.loadTexts: hmArcManagerActionResult.setDescription('Result of the last activated action.\r\n\r\n\t\t\t\t noAction(1): Initial state, no action started.\r\n\t\t\t\t pending(2): A topology check or a configuration process is going on.\r\n\t\t\t\t closedRing(3): The topology check detected a ring topology which is ready for automatic configuration.\r\n\t\t\t\t configuredRing(4): The topology check detected a partly or fully configured ring. \r\n\t\t\t\t                    See the hmArcCheckResultTable for details. You may reconfigure it using ARC.\r\n\t\t\t\t openRing(5): The topology check detected an open ring. It cannot be configured by ARC.\r\n\t\t\t\t invalidTopology(6): An invalid topology was detected. See the hmArcCheckResultTable for details.\r\n\t\t\t\t configFailed(7): One or more devices in the ring could not activate the configuration and are not \r\n\t\t\t\t                  properly configured.\r\n\t\t\t\t configSuccessful(8): The automatic configuration process was successful.')
hmArcCheckResultTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1), )
if mibBuilder.loadTexts: hmArcCheckResultTable.setStatus('current')
if mibBuilder.loadTexts: hmArcCheckResultTable.setDescription('Every entry in this table contains information about\r\n                the status of the network topology reported by the ARC devices.')
hmArcCheckResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1), ).setIndexNames((0, "HMRINGARC-MGMT-SNMP-MIB", "hmArcCheckStatusIndex"), (0, "HMRINGARC-MGMT-SNMP-MIB", "hmArcCheckStatusDeviceMac"))
if mibBuilder.loadTexts: hmArcCheckResultEntry.setStatus('current')
if mibBuilder.loadTexts: hmArcCheckResultEntry.setDescription('An entry in the hmArcCheckResultTable.')
hmArcCheckStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusIndex.setStatus('current')
if mibBuilder.loadTexts: hmArcCheckStatusIndex.setDescription('Index for the table')
hmArcCheckStatusDeviceMac = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusDeviceMac.setStatus('current')
if mibBuilder.loadTexts: hmArcCheckStatusDeviceMac.setDescription('The MAC address of the ARC device that reported \r\n                the status.')
hmArcCheckStatusDeviceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusDeviceIp.setStatus('current')
if mibBuilder.loadTexts: hmArcCheckStatusDeviceIp.setDescription('The IP address of the ARC device that reported \r\n                the status.')
hmArcCheckStatusType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("otherRm", 1), ("loop", 2), ("alreadyConfigured", 3), ("unsupportedOption", 4), ("openRing", 5), ("configFailed", 6), ("duplexMode", 7), ("noArcDevices", 8), ("portState", 9), ("info", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusType.setStatus('current')
if mibBuilder.loadTexts: hmArcCheckStatusType.setDescription('The status an ARC device in the connected topology reported.\r\n\t\t\t\t\r\n\t\t\t\totherRm(1): the device detected another active Redundancy Manager.\r\n\t\t\t\tloop(2): unclear topology detected. This may be a loop or a net segment\r\n\t\t\t\twhich is connected to the ring with Rapid Spanning Tree.\r\n\t\t\t\talreadyConfigured(3): the device already has a ring configured.\r\n\t\t\t\tunsupportedOption(4): the device does not support one of the ARC Manager options.\r\n\t\t\t\topenRing(5): the ARC Manager has detected an open Ring.\r\n\t\t\t\tconfigFailed(6): the configuration of the device failed.\r\n\t\t\t\tduplexMode(7): at least one Ring Port of the device is not in full duplex mode.\r\n\t\t\t\tnoArcDevices(8): there is no device in the ring which supports the ARC Protocol,\r\n\t\t\t\tor all devices have hmArcClientAdminStatus set to disabled.\r\n\t\t\t\tportState(9): at least one Ring Port of the device is not properly configured.\r\n\t\t\t\tinfo(10): the device reported just additional information.')
hmArcCheckStatusInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusInfo.setStatus('current')
if mibBuilder.loadTexts: hmArcCheckStatusInfo.setDescription('Additional information about the ARC device status.\r\n                The device may provide this information for each value in hmArcCheckStatusType.')
hmArcCheckStatusClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("ok", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcCheckStatusClassification.setStatus('current')
if mibBuilder.loadTexts: hmArcCheckStatusClassification.setDescription('Classification of the status the ARC device reported.\r\n\t\t\t\t\r\n\t\t\t\terror(1): the reported status is an\terror.\r\n\t\t\t\twarning(2):\tthe reported status is a warning.\r\n\t\t\t\tok(3): the reported status is an information.')
hmArcClientAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("checkOnly", 3))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmArcClientAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hmArcClientAdminStatus.setDescription("The administratively desired status of the ARC client.\r\n\t\t\t\t\r\n\t\t\t\t enabled(1): ARC client is active, the device can be configured automatically and can return \r\n\t\t\t\t             a status on a topology check.\r\n\t\t\t\t disabled(2): ARC client is inactive, neither checking nor automatic configuring can be done.\r\n\t\t\t\t checkOnly(3): The ARC client returns a status on a topology check but it's not possible \r\n\t\t\t\t               to configure the device automatically.")
hmArcClientManagerDeviceMac = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientManagerDeviceMac.setStatus('current')
if mibBuilder.loadTexts: hmArcClientManagerDeviceMac.setDescription('The MAC address of the ARC manager that last checked or configured the device.')
hmArcClientManagerDeviceIp = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientManagerDeviceIp.setStatus('current')
if mibBuilder.loadTexts: hmArcClientManagerDeviceIp.setDescription('The IP address of the ARC manager that last checked or configured the device.')
hmArcClientPrimGroupID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientPrimGroupID.setStatus('current')
if mibBuilder.loadTexts: hmArcClientPrimGroupID.setDescription('Unique index to identify the slot number of\r\n                                the to be configured primary link port. This value is never\r\n                                greater than hmSysGroupCapacity. ')
hmArcClientPrimIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientPrimIfIndex.setStatus('current')
if mibBuilder.loadTexts: hmArcClientPrimIfIndex.setDescription('Interface index of the to be configured primary link.')
hmArcClientRedGroupID = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientRedGroupID.setStatus('current')
if mibBuilder.loadTexts: hmArcClientRedGroupID.setDescription('Unique index to identify the slot number of\r\n                                the to be configured redundant link port. This value is never\r\n                                greater than hmSysGroupCapacity. ')
hmArcClientRedIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 248, 14, 5, 7, 4, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmArcClientRedIfIndex.setStatus('current')
if mibBuilder.loadTexts: hmArcClientRedIfIndex.setDescription('Interface index of the to be configured redundant link.')
mibBuilder.exportSymbols("HMRINGARC-MGMT-SNMP-MIB", hmArcManagerPrimGroupID=hmArcManagerPrimGroupID, hmArcCheckStatusDeviceMac=hmArcCheckStatusDeviceMac, hmArcClientManagerDeviceIp=hmArcClientManagerDeviceIp, hmArcManagerConfig=hmArcManagerConfig, hmArcClientConfig=hmArcClientConfig, hmARC=hmARC, hmArcClientPrimIfIndex=hmArcClientPrimIfIndex, hmArcManagerActionResult=hmArcManagerActionResult, hmArcManagerVlanID=hmArcManagerVlanID, hmArcClientManagerDeviceMac=hmArcClientManagerDeviceMac, hmArcManagerAdminStatus=hmArcManagerAdminStatus, hmArcCheckStatusDeviceIp=hmArcCheckStatusDeviceIp, hmArcClientRedGroupID=hmArcClientRedGroupID, hmArcClientAdminStatus=hmArcClientAdminStatus, hmArcCheckStatusInfo=hmArcCheckStatusInfo, hmArcCheckStatusType=hmArcCheckStatusType, hmArcClientStatus=hmArcClientStatus, hmArcManagerRedIfIndex=hmArcManagerRedIfIndex, hmArcClientPrimGroupID=hmArcClientPrimGroupID, hmArcManagerStatus=hmArcManagerStatus, hmArcCheckStatusClassification=hmArcCheckStatusClassification, hmArcManagerAction=hmArcManagerAction, PYSNMP_MODULE_ID=hmARC, hmArcCheckStatusIndex=hmArcCheckStatusIndex, hmArcCheckResultTable=hmArcCheckResultTable, hmArcClientRedIfIndex=hmArcClientRedIfIndex, hmArcCheckResultEntry=hmArcCheckResultEntry, hmArcManagerRedGroupID=hmArcManagerRedGroupID, hmArcManagerPrimIfIndex=hmArcManagerPrimIfIndex, hmArcManagerRedProtocol=hmArcManagerRedProtocol)
