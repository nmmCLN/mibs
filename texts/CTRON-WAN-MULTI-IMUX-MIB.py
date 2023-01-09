#
# PySNMP MIB module CTRON-WAN-MULTI-IMUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-WAN-MULTI-IMUX-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:52 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ctWanServices, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctWanServices")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Integer32, ModuleIdentity, Gauge32, iso, TimeTicks, Counter64, IpAddress, Unsigned32, ObjectIdentity, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Integer32", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctWanMultiMux = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2))
ctWANMMuxGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 1))
ctWANMMuxMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWANMMuxMaxNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctWANMMuxMaxNum.setDescription('Get the maximum number of Inverse Multiplexer\n                        applications allowed to be programmed for this IP host.')
ctWanMMuxTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2), )
if mibBuilder.loadTexts: ctWanMMuxTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxTable.setDescription('Information describing the global parameters\n                        that apply to Inverse Multiplexer entities.')
ctWanMMuxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxId"))
if mibBuilder.loadTexts: ctWanMMuxEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxEntry.setDescription('A description of a single Inverse Multiplexer entry.')
ctWanMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxId.setDescription('A unique value identifying an element in a sequence of\n                        Inverse Multiplexer Applications which belong to an IP\n                        host. This value ranges from 1 to the maximum number of \n                        programmable applications as described by\n                        ctWANMMuxMaxNum. This index is associated\n                        with a physical WAN interface containing multiple DS1\n                        connections.')
ctWanMMuxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxIfIndex.setDescription('The value for this object is equal to the value of\n                        ifIndex from the Interfaces table of MIB II (RFC 1213).\n                        Specifically, this index is associated with the physical\n                        interface containing multiple DS1 connections to be used\n                        for Cabletron WAN Inverse Multiplexing.')
ctWanMMuxMaxNumGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxMaxNumGroups.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxMaxNumGroups.setDescription('Get the maximum number of Inverse Multiplexer groups\n                        allowed to be programmed for this IMUX entity. This value\n                        is the number of physical WAN connections, divided by\n                        the minimum number of channels for a single mux\n                        to be operational (2).  However, some devices may only\n                        support a single inverse multiplexer group.')
ctWanMMuxAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxAdmin.setDescription('Used to enable and disable an Inverse Multiplexer\n                        Application.  This object is used to enable/disable\n                        Inverse Multiplexing for a single IMUX entity.  Inverse\n                        Multiplexer Groups may be enabled/disabled independently\n                        using ctWanMMuxGroupAdmin.  This object must be set to \n                        enabled for any inverse multiplexing to occur on the \n                        IMUX entity.')
ctWanMMuxGroupTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3), )
if mibBuilder.loadTexts: ctWanMMuxGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxGroupTable.setDescription('Information describing the configured parameters\n                        of one of the Inverse Multiplexer groups.')
ctWanMMuxGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxGroupMMuxId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxGroupId"))
if mibBuilder.loadTexts: ctWanMMuxGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxGroupEntry.setDescription('A description of a single Inverse Multiplexer group \n                        entry.')
ctWanMMuxGroupMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupMMuxId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxGroupMMuxId.setDescription('A unique value identifying an element in a sequence of\n                        Inverse Multiplexer Applications which belong to an IP\n                        host. This value ranges from 1 to the maximum number of \n                        programmable applications as described by \n                        ctWANMMuxMaxNum.  This index is the same as\n                        ctWanMMuxId.')
ctWanMMuxGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxGroupId.setDescription('A unique value identifying an element in a sequence of\n                        groups which belong to the WAN Inverse Multiplexer.  \n                        This value ranges from 1 to the maximum number of \n                        programmable groups as described by\n                        ctWANMMuxMaxNumGroups.')
ctWanMMuxGroupAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxGroupAdmin.setDescription("Used to enable and disable an Inverse Multiplexer\n                        group which evenly distributes data traffic in a\n                        properly sequenced fashion, over two or more single \n                        channel Wide Area Network connections such as DS1, \n                        E1, DDS, or SYNC.  Each of the single channel \n                        connections must be configured with an appropriate \n                        datalink protocol. A minimum of two channels, each \n                        assigned to it's own physical interface, is required\n                        before the Inverse Multiplexer group can be enabled.")
ctWanMMuxGroupNumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxGroupNumChannels.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxGroupNumChannels.setDescription("Get the number of channels currently\n                        associated with this Inverse Multiplexer group. A \n                        minimum of two channels, each assigned to it's own\n                        physical interface, is required before the Inverse \n                        Multiplexer group can be enabled.")
ctWanMMuxGroupAddChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupAddChannel.setReference('rfc-1213')
if mibBuilder.loadTexts: ctWanMMuxGroupAddChannel.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxGroupAddChannel.setDescription('Add a channel to the channel list used by this Inverse\n                        Multiplexer group.  Before a channel is added, the \n                        channel must be assigned a MIB II ifindex, and an\n                        acceptable Datalink Protocol. When this object is set,\n                        it is set with the ifindex value. This object is always\n                        read as a 1.')
ctWanMMuxGroupDelChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctWanMMuxGroupDelChannel.setReference('rfc-1213')
if mibBuilder.loadTexts: ctWanMMuxGroupDelChannel.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxGroupDelChannel.setDescription("Delete a channel to the channel list used by this \n                        Inverse Multiplexer group.  Before a channel is\n                        deleted, the channel must exist in the Inverse\n                        Multiplexer group's channel table.  When this object\n                        is set, it is set with the ifindex value of the channel\n                        the user wishes to delete from the channel table. This \n                        object is always read as a 1.")
ctWanMMuxChannelTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4), )
if mibBuilder.loadTexts: ctWanMMuxChannelTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelTable.setDescription('Table containing ifindex values, representing WAN \n                        channels, used by the Inverse Multiplexer. The table \n                        also contains statistics reported about each channel.')
ctWanMMuxChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1), ).setIndexNames((0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelMMuxId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelGroupId"), (0, "CTRON-WAN-MULTI-IMUX-MIB", "ctWanMMuxChannelId"))
if mibBuilder.loadTexts: ctWanMMuxChannelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelEntry.setDescription('A description of a single entry.')
ctWanMMuxChannelMMuxId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelMMuxId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelMMuxId.setDescription('A unique value identifying an element in a sequence of\n                        Inverse Multiplexer Applications which belong to an IP\n                        host. This value ranges from 1 to the maximum number of \n                        programmable applications as described by \n                        ctWANMMuxMaxNum.  This index is the same as\n                        ctWanMMuxId.')
ctWanMMuxChannelGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelGroupId.setDescription('A unique value identifying an element in a sequence \n                        of groups which belong to the WAN Inverse Multiplexer.\n                        This value ranges from 1 to the maximum number of \n                        programmable groups as described by\n                        ctWANMMuxMaxNumGroups.')
ctWanMMuxChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelId.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelId.setDescription('A unique value identifying an element in a sequence of\n                        member channel ifindex values which belong to a WAN \n                        Inverse Multiplexer group.')
ctWanMMuxChannelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelIfIndex.setDescription('Returns an ifindex associated with a WAN\n                        channel used for Inverse Multiplexing.')
ctWanMMuxChannelPhysNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelPhysNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelPhysNum.setDescription("Returns a unique physical connection identifier \n                        associated with this channel's physical WAN\n                        connection.")
ctWanMMuxChannelBwAvail = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelBwAvail.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelBwAvail.setDescription('Returns a value which represents the available \n                        bandwidth for transmitting data existing for the \n                        physical WAN connection associated with this channel.\n                        The value is represented in bits/sec.')
ctWanMMuxChannelByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelByteCount.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelByteCount.setDescription('Returns a value which represents a cumulative count\n                        of bytes transmitted out from this interface.  The \n                        count includes any bytes transmitted across the\n                        physical medium, less physical medium framing.')
ctWanMMuxChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctWanMMuxChannelStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctWanMMuxChannelStatus.setDescription('Returns the current status of the channel associated\n                        with an inverse multiplexer group.  The channel is \n                        active when the group admin status is enabled, and \n                        the channel is operational.  The channel is inactive \n                        when either the group admin status is disabled, or \n                        the channel is not operational.')
mibBuilder.exportSymbols("CTRON-WAN-MULTI-IMUX-MIB", ctWanMMuxChannelEntry=ctWanMMuxChannelEntry, ctWanMMuxChannelMMuxId=ctWanMMuxChannelMMuxId, ctWanMMuxGroupDelChannel=ctWanMMuxGroupDelChannel, ctWanMMuxGroupId=ctWanMMuxGroupId, ctWanMMuxChannelBwAvail=ctWanMMuxChannelBwAvail, ctWANMMuxMaxNum=ctWANMMuxMaxNum, ctWanMMuxGroupAdmin=ctWanMMuxGroupAdmin, ctWanMMuxGroupMMuxId=ctWanMMuxGroupMMuxId, ctWanMMuxChannelId=ctWanMMuxChannelId, ctWanMMuxGroupEntry=ctWanMMuxGroupEntry, ctWanMMuxTable=ctWanMMuxTable, ctWanMMuxEntry=ctWanMMuxEntry, ctWanMMuxIfIndex=ctWanMMuxIfIndex, ctWANMMuxGeneralGroup=ctWANMMuxGeneralGroup, ctWanMMuxMaxNumGroups=ctWanMMuxMaxNumGroups, ctWanMMuxChannelTable=ctWanMMuxChannelTable, ctWanMMuxChannelStatus=ctWanMMuxChannelStatus, ctWanMMuxId=ctWanMMuxId, ctWanMMuxChannelPhysNum=ctWanMMuxChannelPhysNum, ctWanMMuxChannelByteCount=ctWanMMuxChannelByteCount, ctWanMMuxChannelGroupId=ctWanMMuxChannelGroupId, ctWanMMuxGroupTable=ctWanMMuxGroupTable, ctWanMMuxGroupNumChannels=ctWanMMuxGroupNumChannels, ctWanMMuxChannelIfIndex=ctWanMMuxChannelIfIndex, ctWanMMuxGroupAddChannel=ctWanMMuxGroupAddChannel, ctWanMultiMux=ctWanMultiMux, ctWanMMuxAdmin=ctWanMMuxAdmin)
