#
# PySNMP MIB module NBS-ROADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-ROADM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:28:05 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, ifAlias = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifAlias")
nbs, NbsTcMHz, NbsTcMilliDb, NbsTcStagingCommit = mibBuilder.importSymbols("NBS-MIB", "nbs", "NbsTcMHz", "NbsTcMilliDb", "NbsTcStagingCommit")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, ObjectIdentity, NotificationType, ModuleIdentity, Counter32, Integer32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Counter32", "Integer32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
nbsRoadmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 235))
if mibBuilder.loadTexts: nbsRoadmMib.setLastUpdated('201504300000Z')
if mibBuilder.loadTexts: nbsRoadmMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsRoadmMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsRoadmMib.setDescription('Reconfigurable Optical Add/Drop Multiplexing')
nbsRoadmCommonGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 10))
if mibBuilder.loadTexts: nbsRoadmCommonGrp.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonGrp.setDescription('Channels per Common port')
nbsRoadmFlexgridGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 20))
if mibBuilder.loadTexts: nbsRoadmFlexgridGrp.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridGrp.setDescription('Describes Flexgrid centerline and bandwidth capabilities ')
nbsRoadmStagingGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 30))
if mibBuilder.loadTexts: nbsRoadmStagingGrp.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingGrp.setDescription('Scratchpad for users to configure channels and WSS setup')
nbsRoadmCommittedGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 31))
if mibBuilder.loadTexts: nbsRoadmCommittedGrp.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedGrp.setDescription('Administratively active channel and WSS setup.')
nbsRoadmRedundantGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 32))
if mibBuilder.loadTexts: nbsRoadmRedundantGrp.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantGrp.setDescription('Current active port.')
nbsRoadmTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 100))
if mibBuilder.loadTexts: nbsRoadmTraps.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmTraps.setDescription('SNMP Traps or Notifications')
nbsRoadmEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 235, 100, 0))
if mibBuilder.loadTexts: nbsRoadmEvent.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmEvent.setDescription('Event Notification Definitions')
nbsRoadmCommonTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 10, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonTableSize.setDescription('The number of entries in nbsRoadmCommonTable')
nbsRoadmCommonTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 10, 2), )
if mibBuilder.loadTexts: nbsRoadmCommonTable.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonTable.setDescription('WSS Switch Configuration')
nbsRoadmCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmCommonIfIndex"))
if mibBuilder.loadTexts: nbsRoadmCommonEntry.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonEntry.setDescription('')
nbsRoadmCommonIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonIfIndex.setDescription("The Mib2 ifIndex of this channel's trunk port.")
nbsRoadmCommonStagingQuickCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2), ("std100Ghz", 3), ("std50Ghz", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRoadmCommonStagingQuickCfg.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonStagingQuickCfg.setDescription("Impulse object used to replace this port's current\n        nbsRoadmStagingTable entries with a known configuration.\n\n        Users may create the nbsRoadmStagingTable manually, a row at a\n        time.  Often it would save the users much work if they could\n        initially populate this table with a standard or known\n        configuration and then customize it to their own requirements.\n\n        When read, this object will indicate whether this feature is\n        available by reporting either notSupported(1) or supported(2).\n\n        The value std100Ghz(3) overwrites this port's\n        nbsRoadmStagingTable with all the standard 100 GHz ITU grid\n        channels which are supported by this port.\n\n        The value std50Ghz(4) overwrites this port's\n        nbsRoadmStagingTable with all the standard 50 GHz ITU grid\n        channels which are supported by this port.\n\n        Overwriting the nbsRoadmStagingTable entries has no effect\n        on the live configuration until committed using\n        nbsRoadmCommonStagingCommit")
nbsRoadmCommonStagingAddCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("capable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonStagingAddCaps.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonStagingAddCaps.setDescription('This object indicates if this port is capable of Add')
nbsRoadmCommonStagingDropCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("capable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonStagingDropCaps.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonStagingDropCaps.setDescription('This object indicates if this port is capable of Drop')
nbsRoadmCommonStagingCommit = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 20), NbsTcStagingCommit()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRoadmCommonStagingCommit.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonStagingCommit.setDescription("Impulse object used to rewrite the entire WSS configuration.\n\n        In order to protect users against accidentally dropping traffic\n        streams, a two-step process is used.\n\n        In the first step, users 'stage' a WSS configuration.  The\n        nbsRoadmStagingTable is like a scratchpad where users can\n        build and modify the entire WSS configuration without affecting\n        the live network.  Here users assign channels to WSS ports, and\n        for flex-grids, define the channels.\n\n        The second step is to replace the existing WSS configuration\n        (which can be read from the nbsRoadmCommittedTable). To replace\n        the existing setup with the configuration specified in the\n        nbsRoadmStagingTable, users set this object to apply(4).\n\n        To discard all changes done to nbsRoadmStagingTable, users\n        set this object to revertToCommitted(3), which will synchronize\n        the Staging table to the Staged configuation.\n\n        When read, this object will report the action last requested\n        until that action is completed, after which it will report\n        supported(2).")
nbsRoadmCommonCommittedGridType = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notSupported", 1), ("reserved", 2), ("customized", 3), ("std100Ghz", 4), ("std50Ghz", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonCommittedGridType.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonCommittedGridType.setDescription("This object is automatically updated in association with writes\n       to nbsRoadmCommonStagingApply.  It indicates whether or not this\n       port's updated nbsRoadmCommittedTable is equivalent to a\n       standard ITU grid such as would come from\n       nbsRoadmCommonStagingQuickCfg.\n\n       If the nbsRoadmCommittedTable matches the results from a\n       nbsRoadmCommonStagingQuickCfg of std100Ghz(4), then this object\n       will report std100Ghz(4).\n\n       If the nbsRoadmCommittedTable matches the results from a\n       nbsRoadmCommonStagingQuickCfg of std50Ghz(5), then this object\n       will report std50Ghz(5).\n\n       If the nbsRoadmCommittedTable matches neither the results from a\n       nbsRoadmCommonStagingQuickCfg of std100Ghz(4) or std50Ghz(5),\n       then this object will report customized(3).")
nbsRoadmCommonCommittedChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 40), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommonCommittedChannels.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommonCommittedChannels.setDescription('The number of channels for this wdm port in the\n       nbsRoadmCommittedTable.')
nbsRoadmFlexgridTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 20, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridTableSize.setDescription('The number of entries in nbsRoadmFlexgridTable.')
nbsRoadmFlexgridTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 20, 2), )
if mibBuilder.loadTexts: nbsRoadmFlexgridTable.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridTable.setDescription('Flexgrid channel creation parameters')
nbsRoadmFlexgridEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmFlexgridIfIndex"))
if mibBuilder.loadTexts: nbsRoadmFlexgridEntry.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridEntry.setDescription('')
nbsRoadmFlexgridIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridIfIndex.setDescription('The Mib2 ifIndex of the Common port.')
nbsRoadmFlexgridCenterlineMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 21), NbsTcMHz().clone(190100000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineMin.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineMin.setDescription('The frequency of the lowest centerline possible.')
nbsRoadmFlexgridCenterlineMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 22), NbsTcMHz().clone(197250000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineMax.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineMax.setDescription('The frequency of the highest centerline possible.')
nbsRoadmFlexgridCenterlineIncr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 23), NbsTcMHz().clone(12500)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineIncr.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridCenterlineIncr.setDescription("Centerline increment - the minimum possible difference, in MHz,\n       between adjacent channels' centerlines.")
nbsRoadmFlexgridBandwidthMin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 31), NbsTcMHz().clone(25000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthMin.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthMin.setDescription('The minimum bandwidth possible.  Each channel must be at least\n       this wide.')
nbsRoadmFlexgridBandwidthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 32), NbsTcMHz().clone(25000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthMax.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthMax.setDescription('The maximum bandwidth possible.  Each channel must be at most\n       this wide.')
nbsRoadmFlexgridBandwidthIncr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 33), NbsTcMHz().clone(25000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthIncr.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmFlexgridBandwidthIncr.setDescription("The granularity of bandwidths possible.  Each channel's\n       bandwidth must be a multiple of this number.")
nbsRoadmStagingTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 30, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmStagingTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingTableSize.setDescription('The number of entries in nbsRoadmStagingTable')
nbsRoadmStagingTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 30, 2), )
if mibBuilder.loadTexts: nbsRoadmStagingTable.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingTable.setDescription('Scratchpad where users can specify a new WSS configuration.\n        Changes to this table have no effect on the system until they\n        are committed using nbsRoadmCommonStagingApply.')
nbsRoadmStagingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmStagingIfIndex"), (0, "NBS-ROADM-MIB", "nbsRoadmStagingCenterline"))
if mibBuilder.loadTexts: nbsRoadmStagingEntry.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingEntry.setDescription('')
nbsRoadmStagingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmStagingIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingIfIndex.setDescription("The Mib2 ifIndex of this channel's Common port.")
nbsRoadmStagingCenterline = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 2), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmStagingCenterline.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingCenterline.setDescription('The center frequency of this channel, in MHz')
nbsRoadmStagingBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 10), NbsTcMHz().clone(100000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingBandwidth.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingBandwidth.setDescription('The amount of spectrum allocated for this channel, in MHz')
nbsRoadmStagingChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingChannelName.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingChannelName.setDescription('User-assigned name for this channel.  The assigned name must be\n        unique within this agent system.')
nbsRoadmStagingAddPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 41), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingAddPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingAddPort.setDescription("The Mib2 ifIndex of this channel's Add port.\n\n        This channel will be blocked from all Add ports except the port\n        specified here.  Setting this object to 0 blocks the channel on\n        all Add ports.\n\n        Not supported value : -1")
nbsRoadmStagingDropPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 42), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingDropPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingDropPort.setDescription("The Mib2 ifIndex of this channel's Drop port.\n\n        This channel will be blocked on all Drop ports except the port\n        specified here.  Setting this object to 0 blocks the channel on\n        all Drop ports.\n\n        Not supported value : -1")
nbsRoadmStagingSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 43), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingSecondaryPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingSecondaryPort.setDescription("The Mib2 ifIndex of this channel's Secondary port.\n\n        This channel will be blocked from all Add ports except the port\n        specified here.  Setting this object to 0 removes the secondary.")
nbsRoadmStagingSecondAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 44), NbsTcMilliDb().clone(-1000000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingSecondAttenu.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingSecondAttenu.setDescription('Attenuation actually being applied to the secondary port, in\n        millidecibels (mdB).')
nbsRoadmStagingAddAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 51), NbsTcMilliDb().clone(-1000000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingAddAttenu.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingAddAttenu.setDescription('Attenuation to be applied to Add channel, expressed in\n        millidecibels (mdB). Default is the blocked value as defined\n        in NbsTcMilliDb')
nbsRoadmStagingDropAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 52), NbsTcMilliDb().clone(-1000000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingDropAttenu.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingDropAttenu.setDescription('Attenuation to be applied to Drop channel, expressed in\n        millidecibels (mdB). Default is the blocked value as defined\n        in NbsTcMilliDb')
nbsRoadmStagingItuName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 53), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmStagingItuName.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingItuName.setDescription("If this channel's centerline and bandwidth match a channel\n        specified in the ITU grid DWDM standard, the name of that ITU\n        channel will be shown here.  The naming convention for 100GHz\n        channels will be the two digit ITU channel number.  For 50GHz\n        channels, the convention will be to specify either the C or H\n        band, followed by the two digit ITU channel number.\n\n        For user-defined channels that don't match an ITU channel, this\n        object will report 'N/A'.")
nbsRoadmStagingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 99), RowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRoadmStagingRowStatus.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmStagingRowStatus.setDescription('Used to create and delete channels in staging area')
nbsRoadmCommittedTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 31, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedTableSize.setDescription('The number of entries in nbsRoadmCommittedTable')
nbsRoadmCommittedTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 31, 2), )
if mibBuilder.loadTexts: nbsRoadmCommittedTable.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedTable.setDescription('Current wss configuration')
nbsRoadmCommittedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmCommittedIfIndex"), (0, "NBS-ROADM-MIB", "nbsRoadmCommittedCenterline"))
if mibBuilder.loadTexts: nbsRoadmCommittedEntry.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedEntry.setDescription('')
nbsRoadmCommittedIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedIfIndex.setDescription("The Mib2 ifIndex of the channel's Common port.")
nbsRoadmCommittedCenterline = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 2), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedCenterline.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedCenterline.setDescription('The center frequency of this channel, in MHz')
nbsRoadmCommittedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 10), NbsTcMHz().clone(100000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedBandwidth.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedBandwidth.setDescription('The amount of spectrum allocated for this channel, in MHz')
nbsRoadmCommittedChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedChannelName.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedChannelName.setDescription('User-assigned name for this channel.  The assigned name must be\n        unique within this agent system.\n\n        This object is equivalent to nbsWdmChannelCustomName.')
nbsRoadmCommittedAddPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 41), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedAddPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedAddPort.setDescription("The Mib2 ifIndex of this channel's Add port.\n\n        This channel will be blocked from all Add ports except the port\n        specified here.  Setting this object to 0 blocks the channel on\n        all ports.\n\n        Not supported value : -1")
nbsRoadmCommittedDropPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 42), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedDropPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedDropPort.setDescription("The Mib2 ifIndex of this channel's Drop port.\n\n        This channel will be blocked on all Drop ports except the port\n        specified here.  Setting this object to 0 blocks the channel on\n        all ports.\n\n        Not supported value : -1")
nbsRoadmCommittedSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 43), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedSecondaryPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedSecondaryPort.setDescription("The Mib2 ifIndex of this channel's Secondary Add port.\n\n        This channel will be blocked from all Add ports except the port\n        specified here.  Setting this object to 0 removes the secondary.")
nbsRoadmCommittedSecondAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 44), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedSecondAttenu.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedSecondAttenu.setDescription('Attenuation actually being applied to the secondary port, in\n        millidecibels (mdB).')
nbsRoadmCommittedAddAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 51), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedAddAttenu.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedAddAttenu.setDescription('Attenuation actually being applied to Add channel, in\n        millidecibels (mdB).')
nbsRoadmCommittedDropAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 52), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedDropAttenu.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedDropAttenu.setDescription('Attenuation actually being applied to Drop channel, in\n        millidecibels (mdB).')
nbsRoadmCommittedItuName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 60), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmCommittedItuName.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmCommittedItuName.setDescription("If this channel's centerline and bandwidth match a channel\n        specified in the ITU grid DWDM standard, the name of that ITU\n        channel will be shown here.  The naming convention for 100GHz\n        channels will be the two digit ITU channel number.  For 50GHz\n        channels, the convention will be to specify either the C or H\n        band, followed by the two digit ITU channel number.\n\n        For user-defined channels that don't match an ITU channel, this\n        object will report 'N/A'.")
nbsRoadmRedundantTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 235, 32, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantTableSize.setDescription('The number of entries in nbsRoadmRedundantTable')
nbsRoadmRedundantTable = MibTable((1, 3, 6, 1, 4, 1, 629, 235, 32, 2), )
if mibBuilder.loadTexts: nbsRoadmRedundantTable.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantTable.setDescription('Current wss redundancy configuration')
nbsRoadmRedundantEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1), ).setIndexNames((0, "NBS-ROADM-MIB", "nbsRoadmRedundantIfIndex"), (0, "NBS-ROADM-MIB", "nbsRoadmRedundantCenterline"))
if mibBuilder.loadTexts: nbsRoadmRedundantEntry.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantEntry.setDescription('')
nbsRoadmRedundantIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantIfIndex.setDescription("The Mib2 ifIndex of the channel's Common port.")
nbsRoadmRedundantCenterline = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 2), NbsTcMHz()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantCenterline.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantCenterline.setDescription('The center frequency of this channel, in MHz')
nbsRoadmRedundantItuName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantItuName.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantItuName.setDescription("If this channel's centerline and bandwidth match a channel\n        specified in the ITU grid DWDM standard, the name of that ITU\n        channel will be shown here.  The naming convention for 100GHz\n        channels will be the two digit ITU channel number.  For 50GHz\n        channels, the convention will be to specify either the C or H\n        band, followed by the two digit ITU channel number.\n\n        For user-defined channels that don't match an ITU channel, this\n        object will report 'N/A'.")
nbsRoadmRedundantChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantChannelName.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantChannelName.setDescription('User-assigned name for this channel.  The assigned name must be\n        unique within this agent system.\n\n        This object is equivalent to nbsWdmChannelCustomName.')
nbsRoadmRedundantMapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 29), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantMapPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantMapPort.setDescription("The Mib2 ifIndex of the current channel's map port.")
nbsRoadmRedundantSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 30), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantSecondaryPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantSecondaryPort.setDescription("The Mib2 ifIndex of the current channel's Secondary port.")
nbsRoadmRedundantCurPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 40), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantCurPort.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantCurPort.setDescription("The Mib2 ifIndex of the current channel's Secondary port.")
nbsRoadmRedundantCurAttenu = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 41), NbsTcMilliDb()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantCurAttenu.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantCurAttenu.setDescription('Attenuation actually being applied to the redundant channel, in\n        millidecibels (mdB).')
nbsRoadmRedundantCurState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switching", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRoadmRedundantCurState.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmRedundantCurState.setDescription('The state of the current redundant port.')
nbsRoadmEventStageAreaCommitted = NotificationType((1, 3, 6, 1, 4, 1, 629, 235, 100, 0, 10)).setObjects(("NBS-ROADM-MIB", "nbsRoadmCommonIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-ROADM-MIB", "nbsRoadmCommonCommittedGridType"), ("NBS-ROADM-MIB", "nbsRoadmCommonCommittedChannels"))
if mibBuilder.loadTexts: nbsRoadmEventStageAreaCommitted.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmEventStageAreaCommitted.setDescription('Sent after an nbsRoadmCommonStagingCommit request is fulfilled.\n\n        This Notification is of severity ERROR, which means it should\n        be emitted unless disabled or nbsCmmcSysTrapTblEntLevel is set\n        to a severity worse than error(3).')
nbsRoadmEventRedundancyTriggered = NotificationType((1, 3, 6, 1, 4, 1, 629, 235, 100, 0, 20)).setObjects(("NBS-ROADM-MIB", "nbsRoadmRedundantIfIndex"), ("NBS-ROADM-MIB", "nbsRoadmRedundantCenterline"))
if mibBuilder.loadTexts: nbsRoadmEventRedundancyTriggered.setStatus('current')
if mibBuilder.loadTexts: nbsRoadmEventRedundancyTriggered.setDescription('Sent after an channel redundancy takes effect.\n\n        This Notification is of severity ERROR, which means it should\n        be emitted unless disabled or nbsCmmcSysTrapTblEntLevel is set\n        to a severity worse than error(3).')
mibBuilder.exportSymbols("NBS-ROADM-MIB", nbsRoadmStagingRowStatus=nbsRoadmStagingRowStatus, nbsRoadmCommonTable=nbsRoadmCommonTable, nbsRoadmCommittedChannelName=nbsRoadmCommittedChannelName, nbsRoadmStagingTableSize=nbsRoadmStagingTableSize, nbsRoadmTraps=nbsRoadmTraps, nbsRoadmCommonStagingCommit=nbsRoadmCommonStagingCommit, nbsRoadmStagingAddPort=nbsRoadmStagingAddPort, nbsRoadmFlexgridBandwidthMax=nbsRoadmFlexgridBandwidthMax, nbsRoadmRedundantCurAttenu=nbsRoadmRedundantCurAttenu, nbsRoadmCommonTableSize=nbsRoadmCommonTableSize, nbsRoadmCommonStagingQuickCfg=nbsRoadmCommonStagingQuickCfg, nbsRoadmFlexgridCenterlineIncr=nbsRoadmFlexgridCenterlineIncr, nbsRoadmCommittedAddAttenu=nbsRoadmCommittedAddAttenu, nbsRoadmRedundantGrp=nbsRoadmRedundantGrp, nbsRoadmStagingTable=nbsRoadmStagingTable, nbsRoadmCommittedTableSize=nbsRoadmCommittedTableSize, nbsRoadmStagingBandwidth=nbsRoadmStagingBandwidth, nbsRoadmCommittedAddPort=nbsRoadmCommittedAddPort, nbsRoadmRedundantSecondaryPort=nbsRoadmRedundantSecondaryPort, nbsRoadmCommittedGrp=nbsRoadmCommittedGrp, nbsRoadmStagingIfIndex=nbsRoadmStagingIfIndex, PYSNMP_MODULE_ID=nbsRoadmMib, nbsRoadmFlexgridCenterlineMax=nbsRoadmFlexgridCenterlineMax, nbsRoadmCommittedEntry=nbsRoadmCommittedEntry, nbsRoadmFlexgridBandwidthMin=nbsRoadmFlexgridBandwidthMin, nbsRoadmStagingDropAttenu=nbsRoadmStagingDropAttenu, nbsRoadmFlexgridGrp=nbsRoadmFlexgridGrp, nbsRoadmCommittedItuName=nbsRoadmCommittedItuName, nbsRoadmFlexgridTableSize=nbsRoadmFlexgridTableSize, nbsRoadmMib=nbsRoadmMib, nbsRoadmRedundantTableSize=nbsRoadmRedundantTableSize, nbsRoadmStagingEntry=nbsRoadmStagingEntry, nbsRoadmCommonCommittedGridType=nbsRoadmCommonCommittedGridType, nbsRoadmStagingSecondaryPort=nbsRoadmStagingSecondaryPort, nbsRoadmRedundantEntry=nbsRoadmRedundantEntry, nbsRoadmFlexgridCenterlineMin=nbsRoadmFlexgridCenterlineMin, nbsRoadmFlexgridEntry=nbsRoadmFlexgridEntry, nbsRoadmCommittedBandwidth=nbsRoadmCommittedBandwidth, nbsRoadmCommonStagingDropCaps=nbsRoadmCommonStagingDropCaps, nbsRoadmEventRedundancyTriggered=nbsRoadmEventRedundancyTriggered, nbsRoadmFlexgridIfIndex=nbsRoadmFlexgridIfIndex, nbsRoadmCommonIfIndex=nbsRoadmCommonIfIndex, nbsRoadmCommonGrp=nbsRoadmCommonGrp, nbsRoadmFlexgridTable=nbsRoadmFlexgridTable, nbsRoadmCommonEntry=nbsRoadmCommonEntry, nbsRoadmStagingDropPort=nbsRoadmStagingDropPort, nbsRoadmRedundantCurState=nbsRoadmRedundantCurState, nbsRoadmStagingChannelName=nbsRoadmStagingChannelName, nbsRoadmRedundantIfIndex=nbsRoadmRedundantIfIndex, nbsRoadmRedundantCenterline=nbsRoadmRedundantCenterline, nbsRoadmRedundantMapPort=nbsRoadmRedundantMapPort, nbsRoadmRedundantTable=nbsRoadmRedundantTable, nbsRoadmCommittedSecondaryPort=nbsRoadmCommittedSecondaryPort, nbsRoadmCommonStagingAddCaps=nbsRoadmCommonStagingAddCaps, nbsRoadmRedundantChannelName=nbsRoadmRedundantChannelName, nbsRoadmEventStageAreaCommitted=nbsRoadmEventStageAreaCommitted, nbsRoadmCommittedSecondAttenu=nbsRoadmCommittedSecondAttenu, nbsRoadmCommittedDropPort=nbsRoadmCommittedDropPort, nbsRoadmCommittedIfIndex=nbsRoadmCommittedIfIndex, nbsRoadmRedundantItuName=nbsRoadmRedundantItuName, nbsRoadmCommonCommittedChannels=nbsRoadmCommonCommittedChannels, nbsRoadmCommittedCenterline=nbsRoadmCommittedCenterline, nbsRoadmCommittedDropAttenu=nbsRoadmCommittedDropAttenu, nbsRoadmRedundantCurPort=nbsRoadmRedundantCurPort, nbsRoadmCommittedTable=nbsRoadmCommittedTable, nbsRoadmFlexgridBandwidthIncr=nbsRoadmFlexgridBandwidthIncr, nbsRoadmStagingAddAttenu=nbsRoadmStagingAddAttenu, nbsRoadmStagingItuName=nbsRoadmStagingItuName, nbsRoadmStagingSecondAttenu=nbsRoadmStagingSecondAttenu, nbsRoadmEvent=nbsRoadmEvent, nbsRoadmStagingGrp=nbsRoadmStagingGrp, nbsRoadmStagingCenterline=nbsRoadmStagingCenterline)
