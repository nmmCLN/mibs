#
# PySNMP MIB module CTRON-VLAN-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-VLAN-EXTENSIONS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ctVlanExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctVlanExt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctVlanBridgeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1))
ctVlanVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanVersionNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanVersionNumber.setDescription('Specifies the IEEE 802.1Q VLAN version number.')
ctVlanSupportedOperationalMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("configurable", 2))).clone('static')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanSupportedOperationalMode.setStatus('deprecated')
if mibBuilder.loadTexts: ctVlanSupportedOperationalMode.setDescription('This value indicates whether the device allows for flexible\n       VLAN configuration as specified by ctVlanCurrentOperationalMode.\n\n       A value of static(1) indicates that the device does not allow\n       for user configuration.  \n\n       A value of configurable(2) indicates that the device supports \n       the functionality described in the ctVlanCurrentOperationalMode \n       object.')
ctVlanCurrentOperationalMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12)).clone(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanCurrentOperationalMode.setStatus('deprecated')
if mibBuilder.loadTexts: ctVlanCurrentOperationalMode.setDescription('This value indicates the number of bits in a VLAN Id\n        that are considered significant in the forwarding decision\n        of a packet.  This allows VLANs to be grouped together into\n        logical units.  Within the scope of these VLAN groups, unicast\n        traffic may be bridged between VLANs, but, multicast and broadcast\n        traffic is scoped to a specific VLAN.\n\n        In the following depiction M represents the number of\n        significant bits as specified by a set of the object.\n        An X in a box represents that the bit is considered\n        significant based on the value of M.\n\n               11  10  9   8   7   6   5   4  3    2   1   0\n             +===============================================+\n        M=0  |   |   |   |   |   |   |   |   |   |   |   |   |\n             +===============================================+\n\n               11  10  9   8   7   6   5   4  3    2   1   0\n             +===============================================+\n        M=4  |   |   |   |   |   |   |   |   | X | X | X | X |\n             +===============================================+\n\n               11  10  9   8   7   6   5   4  3    2   1   0\n             +===============================================+\n        M=9  |   |   |   | X | X | X | X | X | X | X | X | X |\n             +===============================================+\n\n\n        Significant bits are assigned sequentially starting with bit\n        zero and ending with bit M-1.\n\n        For a set value of M, (2 ^ M) VLAN groups will be created.  Each\n        group will contain (2 ^ (12 - M)) VLAN Ids, with the exception\n        of the first group and last group which will each have\n        ((2 ^ (12 - M)) - 1) VLAN Ids (VLAN Ids 0 and 4095 are reserved).\n        VLAN groups are numbered sequentially from 0 through ((2 ^ M) - 1).\n        The VLAN Ids assigned to each group, N, are assigned sequentially\n        starting with (N * (2 ^ (12 - M))) through\n        ((N * (2 ^ (12 - M))) + ((2 ^ (12 - M)) - 1)), with the exception\n        of group zero which always starts with VLAN Id 1 and group\n        ((2 ^ M) -1) which always ends with VLAN Id 4094.\n\n        The number of bits specified allows the maximum amount of\n        flexibility in the scoping of traffic, without compromising\n        security between VLANS.  For example, a set value of 0 would\n        create a single VLAN group with 4094 VLAN Ids.  This configuration\n        would allow all unicast traffic to be bridged between VLANS,\n        while scoping all multicast and broadcast traffic to a specific VLAN.\n        A set value of 12 would restrict all unicast, multicast and broadcast\n        traffic to a specific VLAN.  In this configuration no traffic\n        would be bridged between VLANS.\n\n        Setting of this object is limited to devices which support\n        configurable(2) operational modes as specified by\n        ctVlanSupportedOperationalMode.  A set of this object for a\n        device which only supports static(1) operational mode will fail.\n        A read of this object for a device that only supports\n        static(1) operational mode will always return 12.')
ctVlanResetDefaults = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("current", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanResetDefaults.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanResetDefaults.setDescription('A set of the value reset(2) will cause the\n       ctVlanTriggerPortSet table to contain no entries, delete\n       all objects from the ctVlanConfig group, and reset the\n       ctVlanPortVID for each port to the default port VLAN Identifier.\n       A read of this object will return current(1).\n       A set of current(1) has no effect.')
ctVlanDefaultVIDStickyEgress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanDefaultVIDStickyEgress.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanDefaultVIDStickyEgress.setDescription("A set of the value enable(1) will cause\n       a port, as specified by ctVlanPortNum, to remain in the\n       egress list for the DEFAULT VLAN (VID 1) when the port's\n       VID, specified by ctVlanPortVID, is changed.  A set of disable(2)\n       will cause the port to be removed from the egress list of the\n       DEFAULT VLAN when the ports VID is changed.")
ctVlanSupportedPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6), )
if mibBuilder.loadTexts: ctVlanSupportedPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanSupportedPortTable.setDescription('This table specifies which bridge ports on the device\n       support VLANs.')
ctVlanSupportedPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanSupportedSlotNum"))
if mibBuilder.loadTexts: ctVlanSupportedPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanSupportedPortEntry.setDescription('Specifies the bridge ports in the ctVlanSupportedPortTable.')
ctVlanSupportedSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanSupportedSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanSupportedSlotNum.setDescription('The slot number of the device that the bridge port is located on.')
ctVlanSupportedPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanSupportedPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanSupportedPortNum.setDescription("The set of ports on the device, specified by\n       ctVlanSupportedSlotNum, that support VLANs.\n       Each octet within the value of this object specifies\n       a set of eight ports, with the first octet specifying\n       ports 1 through 8, the second octet specifying ports 9\n       through 16, etc.  Within each octet, the most significant\n       bit represents the lowest numbered port, and the least\n       significant bit represents the highest numbered port.\n       Thus, each port of the VLAN bridge is represented by a\n       single bit within the value of this object.  If that bit\n       has a value of '1' then that port is included in the set\n       of ports; the port is not included if its bit has a value of '0'.")
ctVlanLearningMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ivl", 1), ("svl", 2), ("svlivl", 3))).clone('svl')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanLearningMode.setReference('IEEE Draft Standard P802.1Q/D9, February 20, 1998: Section 3.5\n       IEEE Draft Standard P802.1Q/D9, February 20, 1998: Section 3.9\n       IEEE Draft Standard P802.1Q/D9, February 20, 1998: Section 3.11\n       IEEE Draft Standard P802.1Q/D9, February 20, 1998: Section 6.4')
if mibBuilder.loadTexts: ctVlanLearningMode.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanLearningMode.setDescription("This value indicates the type of VLAN learning the device supports.\n\n       A value of ivl(1) indicates the device supports Independent VLAN\n       Learning (IVL).  Configuration and operation of the Learning Process\n       and the Filtering Database such that, for a given set of VLANs, if a\n       given individual MAC address is learnt in one VLAN, that learnt \n       information is not used in forwarding decisions taken for the same \n       address relative to any other VLAN in the given set.  This \n       operational mode indicates that all unicast, multicast and broadcast \n       traffic is scoped to a specific VLAN.\n\n       A value of svl(2) indicates the device supports Shared VLAN\n       Learning (SVL).  Configuration and operation of the Learning Process\n       and the Filtering Database such that, for a given set of VLANs, if a\n       given individual MAC address is learnt in one VLAN, that learnt\n       information is used in forwarding decisions taken for the same\n       address relative to any other VLAN in the given set.  In a bridge\n       that supports SVL operation, the `given set of VLANS' is the set\n       of all VLANS (1 - 4094).  This operational mode allows all unicast \n       traffic to be bridged between VLANS, while scoping all unknown, \n       multicast and broadcast traffic to a specific VLAN.\n\n       A value of svlivl(3) indicates the device supports both Shared\n       and Independent VLAN learning simultaneously.  This operational\n       mode allows learnt information to be shared between those VLANS for\n       which SVL is necessary while also allowing learnt information not to \n       be shared between those VLANS for which IVL is necessary.  \n\n       All three of the aforementioned modes operate by placing VLANs in \n       `sets'.  In IVL each VLAN is mapped to a separate set while in SVL \n       each VLAN is mapped to the same set.  Accordingly, svlivl is a \n       combination of both.  Each set is realized as a separate filter \n       database.  Each filter database is uniquely identified by a Filter \n       Database Identifier (FID).  The mapping of VLANs to filter databases \n       is defined in the ctVlanIdToFidMapping leaf of the ctVlanConfigTable.")
ctVlanTriggerPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2))
ctVlanTriggerPortSetTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1), )
if mibBuilder.loadTexts: ctVlanTriggerPortSetTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanTriggerPortSetTable.setDescription('This table provides information pertaining to the ports \n       participating in the GVRP triggering function.')
ctVlanTriggerPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanTriggerSlotNum"))
if mibBuilder.loadTexts: ctVlanTriggerPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanTriggerPortEntry.setDescription('Specifies the bridge ports in the ctVlanTriggerPortSet table.')
ctVlanTriggerSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanTriggerSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanTriggerSlotNum.setDescription('The slot number of the device that the bridge port is located on.')
ctVlanTriggerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanTriggerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanTriggerStatus.setDescription("The set of ports that will participate in GVRP\n       trigger functions.  Each octet within the value of\n       this object specifies a set of eight ports, with the\n       first octet specifying ports 1 through 8, the second\n       octet specifying ports 9 through 16, etc.  Within each\n       octet, the most significant bit represents the lowest\n       numbered port, and the least significant bit represents\n       the highest numbered port.  Thus, each port of the VLAN\n       bridge is represented by a single bit within the value\n       of this object.  If that bit has a value of '1' then\n       that port is included in the set of ports; the port is\n       not included if its bit has a value of '0'.  A set of '1'\n       for a port that does not have a '1' for the corresponding\n       bit in the ctVlanSupportedPortNum will be ignored.")
ctVlanPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3))
ctVlanPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1), )
if mibBuilder.loadTexts: ctVlanPortConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanPortConfigTable.setDescription('This table provides general information about the VLAN \n       configuration of all bridge ports on a device.')
ctVlanPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanPortSlotNum"), (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanPortNum"))
if mibBuilder.loadTexts: ctVlanPortConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanPortConfigEntry.setDescription('Describes a particular VLAN port configuration entry.')
ctVlanPortSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanPortSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanPortSlotNum.setDescription('The slot number of the device that the bridge port is located on.')
ctVlanPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanPortNum.setDescription('The port number for which the information is requested.')
ctVlanPortVID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanPortVID.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanPortVID.setDescription('The 12 bit Port VLAN Identifier (PVID) associated with the configured\n       VLAN for received untagged packets on the port specified by \n       ctVlanPortNum.  The port specified by ctVlanPortNum will be added to \n       the egress list (ctVlanEgressList) for the specified VLAN with \n       the frame type of untagged, via ctVlanEgressUntaggedList.  The port will \n       be removed from the egress list of the previous PVID.  The exception to \n       this is the DEFAULT VLAN (VID 1) when the ctVlanDefaultVIDStickyEgress\n       is set to a value of enable(1).  Additionally the ctVlanStatus\n       of the specified VLAN will be set to a value of enable(1).  A set of \n       value that does not exist in the ctVlanConfigTable will fail\n       with a NO-INSTANCE error.')
ctVlanPortDiscardFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noDiscard", 1), ("discardUntagged", 2), ("discardTagged", 3))).clone('noDiscard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanPortDiscardFrame.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanPortDiscardFrame.setDescription('A set of noDiscard(1) causes the port to submit all packets\n       received on the port to the forwarding process, regardless,\n       of the absence or presence of a VLAN tag in the packet.\n       A set of discardUntagged(2) causes the port specified by ctVlanPortNum\n       to discard all frames received that carry no VLAN classification\n       (i.e. any untagged frames or priority tagged frames).  A set of\n       discardTagged(3) has no effect.')
ctVlanPortOperationalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dot1QTrunk", 1), ("hybrid", 2), ("dot1dTrunk", 3))).clone('hybrid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanPortOperationalMode.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanPortOperationalMode.setDescription('A set of dot1QTrunk(1) causes the port specified by ctVlanPortNum \n       to transmit tagged frames exclusively, and ctVlanPortDiscardFrame \n       is set to a value of discardUntagged(2).  Additionally the specified\n       port is added to the egress list of all existing VLANS, and all \n       existing VLANS are enabled as specified by ctVlanStatus.  If new \n       VLANS are established and any port is configured as a dot1QTrunk(1) \n       then the newly created VLAN will automatically be added to the \n       egress list (ctVlanEgressList) for the port specified by \n       ctVlanPortNum.  A set of hybrid(2) allows the port to transmit \n       both tagged and untagged frames.  Additionally the specified \n       port is removed from all VLANS except the the VLAN as specified \n       by ctVlanPortVID.  A set of hybrid(2) will also set \n       ctVlanPortDiscardFrame to a value of noDiscard(1).  A set of \n       dot1dTrunk(3) causes the port specified by ctVlanPortNum to\n       transmit untagged frames exclusively, and ctVlanPortDiscardFrame \n       is set to a value of noDiscard(1).  Additionally the specified \n       port is added to the egress list and the untagged list of all \n       existing VLANS, and all existing VLANS are enabled as specified \n       by ctVlanStatus.  If new VLANS are established and any port is \n       configured as a dot1dTrunk(3) then the newly created VLAN will \n       automatically be added to the egress list (ctVlanEgressList) and \n       the untagged list (ctVlanEgressUntaggedList) for the port specified \n       by ctVlanPortNum.')
ctVlanPortIngressFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanPortIngressFiltering.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanPortIngressFiltering.setDescription("A set of enable(1) causes the forwarding process to discard any frame\n       received on the port, specified by ctVlanPortNum, that is not a member\n       of the classified VLANs' egress list, as specified bt ctVlanEgressList.\n       VLAN classification may be accomplished via the PVID, as specified by \n       ctVlanPortVID, for untagged frames, or the VLAN Id specified in the\n       VLAN tag for tagged packets.  A set of disable(2) causes the port to \n       submit all frames to the forwarding process that have not already been \n       discarded by ctVlanPortDiscardFrame.")
ctVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4))
ctVlanNumActiveEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanNumActiveEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanNumActiveEntries.setDescription('The number of active VLAN entries for the device.')
ctVlanNumConfiguredEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanNumConfiguredEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanNumConfiguredEntries.setDescription('The number of configured VLAN entries for the device.  This value\n       includes active entries.')
ctVlanMaxNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanMaxNumEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanMaxNumEntries.setDescription('The maximum number of VLAN entries for the device.')
ctVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4), )
if mibBuilder.loadTexts: ctVlanConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanConfigTable.setDescription('This table allows for the creation, deletion, and modification of\n       specific VLANs.')
ctVlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanVID"))
if mibBuilder.loadTexts: ctVlanConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanConfigEntry.setDescription('Allows for configuration of specific VLAN entries.')
ctVlanVID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanVID.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanVID.setDescription('The 12 bit VLAN Identifier associated with the configured VLAN.')
ctVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanName.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanName.setDescription('The ASCII name associated with the configured VLAN.\n       A set of this object prior to creating an entry by \n       setting ctVlanEstablish will fail with a NO-INSTANCE error.')
ctVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanStatus.setDescription('A set with the value of enable(1), enables all associated entries\n      in ctVlanEgressPorts table for the specified VLAN.  A set of\n      disable(2), disables all ctVlanEgressPorts entries associated with\n      the specified VLAN.  On ports for which the ctVlanVID specifies\n      the PVID, the operation causes the PVID to be set to the default\n      PVID value.  A set of this object prior to creating an entry by\n      setting ctVlanEstablish will fail with a NO-INSTANCE error.')
ctVlanEstablish = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanEstablish.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanEstablish.setDescription('A set of the value create(1), causes an entry to be created in\n       the ctVlanConfigTable as specified by the instancing information\n       of ctVlanVID.  Additionally, an entry is created in the\n       ctVlanEgressPortsTable for the specified VLAN. A set of delete(2)\n       causes the specified entry to be removed from both tables.  A read\n       of this object will always return create(1).')
ctVlanIdToFidMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanIdToFidMapping.setReference('IEEE Draft Standard P802.1Q/D9, February 20, 1998: Section 3.6\n       IEEE Draft Standard P802.1Q/D9, February 20, 1998: Section 3.10\n       IEEE Draft Standard P802.1Q/D9, February 20, 1998: Section 3.11\n       IEEE Draft Standard P802.1Q/D9, February 20, 1998: Section 8.11.7')
if mibBuilder.loadTexts: ctVlanIdToFidMapping.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanIdToFidMapping.setDescription('The 12 bit Filter Database Identifier (FID) associated with the\n       configured VLAN as specified by ctVlanVID.\n\n       For devices operating in Independent VLAN Learning (IVL) mode, as \n       specified by a value of ivl(1) for ctVlanLearningMode, each VLAN \n       will be mapped to a FID value equal to the VLAN Id specified\n       by ctVlanId.\n\n       For devices operating in Shared VLAN Learning (SVL) mode, as specified \n       by a value of svl(2) for ctVlanLearningMode, all VLANs will be to the \n       same FID (1).  On a device operating in SVL mode, sets to this object \n       will have no effect.\n\n       For devices operating in Shared and Independent VLAN Learning\n       (SIVL) mode, as specified by a value of svlivl(3) for \n       ctVlanLearningMode, one or more VLANs can be mapped to each FID.  Each \n       VLAN can only be uniquely mapped to one FID.  When more than one VLAN \n       is mapped to a single FID they will operate together under the SVL mode \n       of operation.  When a single VLAN is mapped to a FID it will operate \n       under the IVL mode of operation.  The default value for this object, \n       while the device is svlivl(3) mode, will be equal to the VLAN Id \n       specified by ctVlanId.')
ctVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("dynamicGvrp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanType.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanType.setDescription('This object indicates the type for this entry.\n\n         A value of other(1) indicates that this entry is currently in use \n         but the conditions under which it will remain so differ from the \n         following values.\n\n         A value of static(2) indicates that this entry has been statically\n         configured by management, is currently in use and will remain so after\n         the next reset of the device.  \n\n         A value of dynamicGvrp(3) indicates that this entry is currently in use\n         and will remain so until removed by GVRP.  There is no static entry for \n         this VLAN and it will be removed when the last port leaves the VLAN.')
ctVlanEgressPortsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5), )
if mibBuilder.loadTexts: ctVlanEgressPortsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanEgressPortsTable.setDescription('This table provides information pertaining to the egress ports \n       for a particular VLAN.')
ctVlanEgressPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanEgressPortSlotNum"), (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanEgressVID"))
if mibBuilder.loadTexts: ctVlanEgressPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanEgressPortEntry.setDescription('Specifies the egress ports and frame types per port for the \n       specified VLAN.')
ctVlanEgressPortSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanEgressPortSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanEgressPortSlotNum.setDescription('The slot number of the device that the VLAN is configured on.')
ctVlanEgressVID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanEgressVID.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanEgressVID.setDescription('The 12 bit VLAN Identifier associated with the configured VLAN.')
ctVlanEgressList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanEgressList.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanEgressList.setDescription("The set of ports to which traffic destined for\n       the VLAN specified by ctVlanEgressVID\n       on the device specified by ctVlanEgressPortSlotNum\n       may be transmitted. Each octet within the value of\n       this object specifies a set of eight ports, with the\n       first octet specifying ports 1 through 8, the second\n       octet specifying ports 9 through 16, etc.  Within each\n       octet, the most significant bit represents the lowest\n       numbered port, and the least significant bit represents\n       the highest numbered port.  Thus, each port of the VLAN\n       bridge is represented by a single bit within the value\n       of this object.  If that bit has a value of '1' then\n       that port is included in the set of ports; the port is\n       not included if its bit has a value of '0'.  A set of '1'\n       for a port that does not have a '1' for the corresponding\n       bit in the ctVlanSupportedPortNum will be ignored.")
ctVlanEgressUntaggedList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanEgressUntaggedList.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanEgressUntaggedList.setDescription("The set of ports to which traffic destined for\n       the VLAN specified by ctVlanEgressVID\n       on the device specified by ctVlanEgressPortSlotNum\n       should be untagged. Each octet within the value of\n       this object specifies a set of eight ports, with the\n       first octet specifying ports 1 through 8, the second\n       octet specifying ports 9 through 16, etc.  Within each\n       octet, the most significant bit represents the lowest\n       numbered port, and the least significant bit represents\n       the highest numbered port.  Thus, each port of the VLAN\n       bridge is represented by a single bit within the value\n       of this object.  If that bit has a value of '1' then\n       that port is included in the set of ports; the port is\n       not included if its bit has a value of '0'.  All egress\n       ports, as specified by ctVlanEgressList, that do not have\n       a value of '1' for the corresponding bit in this object\n       will be tagged. A set of '1' for a port that does not have\n       a '1' for the corresponding bit in the ctVlanEgressList will\n       be ignored.")
ctVlanProtocolAssign = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5))
ctVlanProtocolStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanProtocolStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanProtocolStatus.setDescription('This object allows the Protocol/Vlan feature to be disabled.')
ctMaxNumVlanProtoEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctMaxNumVlanProtoEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctMaxNumVlanProtoEntries.setDescription('The maximum number of entries allowed for the ctVlanProtoAssignTable \n         table.')
ctVlanProtoAssignTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3), )
if mibBuilder.loadTexts: ctVlanProtoAssignTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanProtoAssignTable.setDescription("This table provides a mapping of protocol or Ether types to \n         VLAN Ids for 'untagged' packets.")
ctVlanProtoAssignEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1), ).setIndexNames((0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanVID"), (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanProtoEtherType"))
if mibBuilder.loadTexts: ctVlanProtoAssignEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanProtoAssignEntry.setDescription('Describes a particular protocol VLAN ID configuration entry.')
ctVlanProtoEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanProtoEtherType.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanProtoEtherType.setDescription("This object returns the protocol or Ether type that is mapped to\n         the VLAN specified in it's instancing.  This object takes the \n         value of any valid Ether type(0x0600..0xFFFF).\n\n         In addition to the previously mentioned range of Ether types, the \n         following values hold special meaning:\n            \n         Value        Description        DSAP/SSAP/Control\n        -------     ---------------    ----------------------\n         0x100        LLC_IPX1            0xE0E003   \n         0x101        LLC_IPX2            0xFFFF\n         0x102        LLC_NETBIOS         0xF0F003\n         0x103        LLC_BANYAN          0xBCBC03\n        ")
ctVlanProtoEstablish = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanProtoEstablish.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanProtoEstablish.setDescription('A set of the value create(1), causes an entry to be added to the \n         ctVlanProtoAssignTable as specified by the instancing information\n         of ctVlanVID and ctVlanProtoEtherType.  This has the result \n         of mapping the specified protocol or Ether type to a VLAN\n         for all received untagged traffic on the ports specified by\n         ctVlanProtoPortList.  A set of the value delete(2), \n         causes the specified entry information to be removed from the table. \n         A read of this object will always return create(1).')
ctVlanProtoPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanProtoPortList.setStatus('mandatory')
if mibBuilder.loadTexts: ctVlanProtoPortList.setDescription("The set of ports on the device, specified by ctVlanVID and \n         ctVlanProtoEtherType, that will classify received 'untagged' \n         packets of ctVlanProtoEtherType type, to the VLAN specified\n         by ctVlanVID.  Each octet within the value of this object\n         specifies a set of eight ports, with the first octet specifying ports 1\n         through 8, the second octet specifying ports 9 through 16, etc.  Within\n         each octet, the most significant bit represents the lowest numbered \n         port, and the least significant bit represents the highest numbered \n         port.  Thus, each port on this device is represented by a single bit\n         within the value of this object.  If that bit has a\n         value of '1' then that port is included in the set of ports; the port \n         is not included if its bit has a value of '0'.  A set of this object \n         prior to creating an entry by setting ctVlanProtoEstablish will fail \n         with a NO-INSTANCE error.  This object will have an initial value '0' \n         for each port that is represented.")
mibBuilder.exportSymbols("CTRON-VLAN-EXTENSIONS-MIB", ctVlanBridgeConfig=ctVlanBridgeConfig, ctVlanProtoEtherType=ctVlanProtoEtherType, ctVlanEgressPortEntry=ctVlanEgressPortEntry, ctVlanTriggerPortEntry=ctVlanTriggerPortEntry, ctVlanConfigEntry=ctVlanConfigEntry, ctVlanConfigTable=ctVlanConfigTable, ctVlanSupportedOperationalMode=ctVlanSupportedOperationalMode, ctVlanConfig=ctVlanConfig, ctVlanPortDiscardFrame=ctVlanPortDiscardFrame, ctVlanNumActiveEntries=ctVlanNumActiveEntries, ctVlanVID=ctVlanVID, ctVlanIdToFidMapping=ctVlanIdToFidMapping, ctVlanEgressPortsTable=ctVlanEgressPortsTable, ctVlanCurrentOperationalMode=ctVlanCurrentOperationalMode, ctVlanSupportedPortNum=ctVlanSupportedPortNum, ctMaxNumVlanProtoEntries=ctMaxNumVlanProtoEntries, ctVlanTriggerStatus=ctVlanTriggerStatus, ctVlanPortIngressFiltering=ctVlanPortIngressFiltering, ctVlanPortConfigTable=ctVlanPortConfigTable, ctVlanName=ctVlanName, ctVlanDefaultVIDStickyEgress=ctVlanDefaultVIDStickyEgress, ctVlanEgressUntaggedList=ctVlanEgressUntaggedList, ctVlanLearningMode=ctVlanLearningMode, ctVlanPortConfig=ctVlanPortConfig, ctVlanPortOperationalMode=ctVlanPortOperationalMode, ctVlanType=ctVlanType, ctVlanSupportedSlotNum=ctVlanSupportedSlotNum, ctVlanEgressVID=ctVlanEgressVID, ctVlanEstablish=ctVlanEstablish, ctVlanEgressList=ctVlanEgressList, ctVlanSupportedPortEntry=ctVlanSupportedPortEntry, ctVlanProtoAssignEntry=ctVlanProtoAssignEntry, ctVlanProtocolStatus=ctVlanProtocolStatus, ctVlanPortVID=ctVlanPortVID, ctVlanTriggerPortConfig=ctVlanTriggerPortConfig, ctVlanProtocolAssign=ctVlanProtocolAssign, ctVlanSupportedPortTable=ctVlanSupportedPortTable, ctVlanVersionNumber=ctVlanVersionNumber, ctVlanPortSlotNum=ctVlanPortSlotNum, ctVlanTriggerSlotNum=ctVlanTriggerSlotNum, ctVlanPortNum=ctVlanPortNum, ctVlanEgressPortSlotNum=ctVlanEgressPortSlotNum, ctVlanMaxNumEntries=ctVlanMaxNumEntries, ctVlanNumConfiguredEntries=ctVlanNumConfiguredEntries, ctVlanTriggerPortSetTable=ctVlanTriggerPortSetTable, ctVlanStatus=ctVlanStatus, ctVlanPortConfigEntry=ctVlanPortConfigEntry, ctVlanProtoAssignTable=ctVlanProtoAssignTable, ctVlanProtoEstablish=ctVlanProtoEstablish, ctVlanProtoPortList=ctVlanProtoPortList, ctVlanResetDefaults=ctVlanResetDefaults)
