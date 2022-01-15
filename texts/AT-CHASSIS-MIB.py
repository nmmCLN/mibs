#
# PySNMP MIB module AT-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-CHASSIS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:26 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, Counter32, NotificationType, ModuleIdentity, Integer32, ObjectIdentity, MibIdentifier, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Counter32", "NotificationType", "ModuleIdentity", "Integer32", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chassis = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23))
chassis.setRevisions(('2014-06-09 00:00', '2014-05-26 00:00', '2014-04-16 00:00', '2012-05-15 00:00', '2011-09-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: chassis.setRevisionsDescriptions(('Added sofware version to chassisCardTable.', 'Added new chassisMappingTable for mapping node ID to member ID.', 'Added more descriptions to chassisCardSlot for VCStack Plus and\n                 increase the range to 1-24.', 'Added support for the controller cards and line cards.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: chassis.setLastUpdated('201406090000Z')
if mibBuilder.loadTexts: chassis.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: chassis.setContactInfo('  http://www.alliedtelesis.com')
if mibBuilder.loadTexts: chassis.setDescription('Support for accessing trap notifications on chassis based products.')
chassisNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0))
chassisCardRoleChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 1)).setObjects(("AT-CHASSIS-MIB", "slotNumber"), ("AT-CHASSIS-MIB", "chassisRole"))
if mibBuilder.loadTexts: chassisCardRoleChangeNotify.setStatus('current')
if mibBuilder.loadTexts: chassisCardRoleChangeNotify.setDescription("A notification generated when the CFC's role is changed.")
chassisCardJoinNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 2)).setObjects(("AT-CHASSIS-MIB", "slotNumber"))
if mibBuilder.loadTexts: chassisCardJoinNotify.setStatus('current')
if mibBuilder.loadTexts: chassisCardJoinNotify.setDescription('A notification generated when a card connects to the CFC.')
chassisCardLeaveNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 3)).setObjects(("AT-CHASSIS-MIB", "slotNumber"))
if mibBuilder.loadTexts: chassisCardLeaveNotify.setStatus('current')
if mibBuilder.loadTexts: chassisCardLeaveNotify.setDescription('A notification generated when a card detaches from the CFC.')
slotNumber = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotNumber.setStatus('current')
if mibBuilder.loadTexts: slotNumber.setDescription('Slot number of the card that has changed.')
chassisRole = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 0, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("leaving", 1), ("discovering", 2), ("synchronizing", 3), ("standbyMember", 4), ("pendingMaster", 5), ("disabledMaster", 6), ("activeMaster", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: chassisRole.setStatus('current')
if mibBuilder.loadTexts: chassisRole.setDescription("CFC's role in the chassis.")
chassisCardTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1), )
if mibBuilder.loadTexts: chassisCardTable.setStatus('current')
if mibBuilder.loadTexts: chassisCardTable.setDescription('A list of cards presented on the device.')
chassisCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1), ).setIndexNames((0, "AT-CHASSIS-MIB", "chassisCardSlot"))
if mibBuilder.loadTexts: chassisCardEntry.setStatus('current')
if mibBuilder.loadTexts: chassisCardEntry.setDescription('A table entry containing information about a card.')
chassisCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardSlot.setStatus('current')
if mibBuilder.loadTexts: chassisCardSlot.setDescription('The slot number the card is in. For VCStack Plus,\n                 1-12 refers to the cards on VCS stack member 1 and\n                 13-24 refers to the cards on VCS stack member 2.\n                 Refer to chassisMappingTable for more details.')
chassisCardBoardOID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardBoardOID.setStatus('current')
if mibBuilder.loadTexts: chassisCardBoardOID.setDescription("The OID value used to identify the type of board\n                that is defined in the alliedTelesis's 'boards'\n                enterprise MIB.\n                If the board is provisioned or an unsupported\n                hardware, this object will have the value of 0 0.")
chassisCardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardName.setStatus('current')
if mibBuilder.loadTexts: chassisCardName.setDescription("The name of the card. E.g. AT-SBx81CFC400, AT-SBx81CFC960 for\n                controller cards; AT-SBx81GP24, AT-SBx81GT24, AT-SBx81GS24,\n                AT-SBx81XS6 for line cards; 'unknown' for unsupported hardware.")
chassisCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unknown", 1), ("configuring", 2), ("syncing", 3), ("online", 4), ("syncingFirmware", 5), ("joining", 6), ("incompatibleSW", 7), ("disabled", 8), ("initializing", 9), ("booting", 10), ("unsupportedHW", 11), ("provisioned", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardState.setStatus('current')
if mibBuilder.loadTexts: chassisCardState.setDescription('The current state of the card. The valid state is in one of the following:\n                unknown(1), configuring(2), syncing(3), online(4), syncingFirmware(5),\n                joining(6), incompatibleSW(7), disabled(8), initializing(9),\n                booting(10), unsupportedHW(11) or provisioned(12).')
chassisCardControllerState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisCardControllerState.setStatus('current')
if mibBuilder.loadTexts: chassisCardControllerState.setDescription('The current state of the controller card, in addition to the\n                card state. The valid state is in one of the following:\n                unknown(1), active(2) or standby(3).')
chassiCardSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassiCardSwVersion.setStatus('current')
if mibBuilder.loadTexts: chassiCardSwVersion.setDescription('The software version that the card is running. When feature ISSU (In Service\n                Software Update) is supported, there are situations that a LIF card may run\n                a software version different from the active CFC.')
chassisMappingTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2), )
if mibBuilder.loadTexts: chassisMappingTable.setStatus('current')
if mibBuilder.loadTexts: chassisMappingTable.setDescription('A list of cards presented on the device.')
chassisMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1), ).setIndexNames((0, "AT-CHASSIS-MIB", "chassisNodeId"))
if mibBuilder.loadTexts: chassisMappingEntry.setStatus('current')
if mibBuilder.loadTexts: chassisMappingEntry.setDescription("Other SNMP SET/GET operations refer to a card in a chassis using a\n                single integer index, i.e. a 'node-ID'. This table entry maps a node-ID\n                value to the VCS member-ID and slot number of the card. For example,\n                node-ID 17 would map to card 2.5 (VCS member-ID 2, slot 5).")
chassisNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNodeId.setStatus('current')
if mibBuilder.loadTexts: chassisNodeId.setDescription('The node ID of a chassis card.')
chassisVCSMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisVCSMemberId.setStatus('current')
if mibBuilder.loadTexts: chassisVCSMemberId.setDescription('The VCS member ID of the chassis that the card is in.')
chassisSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSlotNumber.setStatus('current')
if mibBuilder.loadTexts: chassisSlotNumber.setDescription('The chassis slot number that the card is installed in.')
chassisNodeDisplayString = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNodeDisplayString.setStatus('current')
if mibBuilder.loadTexts: chassisNodeDisplayString.setDescription("The name of the chassis card. E.g. 'card 1.5'.")
chassisNodeStateString = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 23, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNodeStateString.setStatus('current')
if mibBuilder.loadTexts: chassisNodeStateString.setDescription('The current state of the card for the bay. If the card is present state is\n                displayed as online, or if the bay is provisioned it will be displayed as\n                Provisioned.')
mibBuilder.exportSymbols("AT-CHASSIS-MIB", chassisCardTable=chassisCardTable, chassisMappingEntry=chassisMappingEntry, chassisSlotNumber=chassisSlotNumber, chassisNodeId=chassisNodeId, chassisCardName=chassisCardName, chassisRole=chassisRole, chassis=chassis, chassisMappingTable=chassisMappingTable, chassisCardBoardOID=chassisCardBoardOID, PYSNMP_MODULE_ID=chassis, chassisCardEntry=chassisCardEntry, chassisCardLeaveNotify=chassisCardLeaveNotify, chassiCardSwVersion=chassiCardSwVersion, slotNumber=slotNumber, chassisCardJoinNotify=chassisCardJoinNotify, chassisCardSlot=chassisCardSlot, chassisNodeStateString=chassisNodeStateString, chassisNotifications=chassisNotifications, chassisCardState=chassisCardState, chassisVCSMemberId=chassisVCSMemberId, chassisCardRoleChangeNotify=chassisCardRoleChangeNotify, chassisNodeDisplayString=chassisNodeDisplayString, chassisCardControllerState=chassisCardControllerState)
