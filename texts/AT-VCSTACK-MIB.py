#
# PySNMP MIB module AT-VCSTACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-VCSTACK-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:44 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, MibIdentifier, NotificationType, Bits, IpAddress, Integer32, iso, Gauge32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "MibIdentifier", "NotificationType", "Bits", "IpAddress", "Integer32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32")
TextualConvention, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "TruthValue")
vcstack = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13))
vcstack.setRevisions(('2017-05-11 00:00', '2014-12-24 00:00', '2014-07-04 00:00', '2014-05-26 00:00', '2014-04-24 00:00', '2014-04-15 00:00', '2014-04-09 00:00', '2011-11-03 00:00', '2010-09-07 00:00', '2010-09-03 00:00', '2010-06-15 00:15', '2010-05-24 01:19', '2010-01-15 00:39', '2009-11-05 00:00', '2009-06-08 00:00', '2009-01-20 00:00', '2008-03-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vcstack.setRevisionsDescriptions(('Added new field expansionModule to vcstackActiveStkHardware and\n                 deprecated fields xemStk(1), stackXG(4) and x6EMXS2(5).\n                 Added the missing field stackQS(6) as it is supported on x930.', 'Allow value range (0-12) for object vcstackBayid', 'Added a new value for object vcstackStatus', 'Updated vcstackStkPortxNeighbourId descriptions for VCS+.', 'Deprecated vcstackStkPort1Status, vcstackStkPort1NeighbourId,\n                 vcstackStkPort2Status, vcstackStkPort2NeighbourId', 'Added vcstackPortTable table', 'Updated vcstackVirtualMacAddr description with small change in behaviour', 'Add x6EM/XS2 hardware type', 'Generic syntax tidy up', 'Added disabled master monitoring object and a new resiliency-link status', 'MIB revision history dates in descriptions updated.', 'OID of vcstackTraps was reverted to 6 but deprecated. Added vcstackNotifications', 'Changed the OID value of vcstackTraps from 6 to 0 to meet RFC 3584 3.1', 'Obsoleted fallback-config, added new status object', "Added stack master object and corrected allowable ranges\n                for learned neighbour stack ID's.", 'Added Virtual MAC address objects.', 'Initial version.',))
if mibBuilder.loadTexts: vcstack.setLastUpdated('201705110000Z')
if mibBuilder.loadTexts: vcstack.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: vcstack.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: vcstack.setDescription('This MIB file contains definitions of managed objects for\n                Virtual Chassis Stacking in AlliedWare Plus. ')
vcstackNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0))
vcstackRoleChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 1)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackRole"))
if mibBuilder.loadTexts: vcstackRoleChangeNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackRoleChangeNotify.setDescription("A notification generated when the stack member's role is changed.")
vcstackMemberJoinNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 2)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackNbrMemberIdNotify"))
if mibBuilder.loadTexts: vcstackMemberJoinNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackMemberJoinNotify.setDescription('A notification generated when a member joins in the stack.')
vcstackMemberLeaveNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 3)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackNbrMemberIdNotify"))
if mibBuilder.loadTexts: vcstackMemberLeaveNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackMemberLeaveNotify.setDescription('A notification generated when a member leaves from the stack.')
vcstackResiliencyLinkHealthCheckReceivingNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 4)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckReceivingNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckReceivingNotify.setDescription('A notification generated when the resiliency link is activated.')
vcstackResiliencyLinkHealthCheckTimeOutNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 5)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckTimeOutNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckTimeOutNotify.setDescription("A notification generated when the slave's receive timer has timed out\n                indicating that the Slave has lost contact with the Master\n                via the resiliency link.")
vcstackStkPortLinkUpNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 6)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackStkPortNameNotify"))
if mibBuilder.loadTexts: vcstackStkPortLinkUpNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackStkPortLinkUpNotify.setDescription('A notification generated when the link of stack port is up.')
vcstackStkPortLinkDownNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 7)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackStkPortNameNotify"))
if mibBuilder.loadTexts: vcstackStkPortLinkDownNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackStkPortLinkDownNotify.setDescription('A notification generated when the link of stack port is down.')
vcstackNbrMemberIdNotify = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vcstackNbrMemberIdNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackNbrMemberIdNotify.setDescription('The stack member id of the neighbor of the member sent this notification.')
vcstackStkPortNameNotify = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vcstackStkPortNameNotify.setStatus('current')
if mibBuilder.loadTexts: vcstackStkPortNameNotify.setDescription('The stack port name related this notification.')
vcstackStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normalOperation", 1), ("operatingInFailoverState", 2), ("standaloneUnit", 3), ("ringTopologyBroken", 4), ("vcsDisabled", 5), ("allStkPortsNotUp", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStatus.setStatus('current')
if mibBuilder.loadTexts: vcstackStatus.setDescription('The overall stack status.')
vcstackOperationalStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: vcstackOperationalStatus.setDescription('Whether the stack is enabled or disabled.')
vcstackMgmtVlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMgmtVlanId.setStatus('current')
if mibBuilder.loadTexts: vcstackMgmtVlanId.setDescription('The current stacking management VLAN ID.')
vcstackMgmtVlanSubnetAddr = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMgmtVlanSubnetAddr.setStatus('current')
if mibBuilder.loadTexts: vcstackMgmtVlanSubnetAddr.setDescription('The current stacking management VLAN subnet address.')
vcstackTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5), )
if mibBuilder.loadTexts: vcstackTable.setStatus('current')
if mibBuilder.loadTexts: vcstackTable.setDescription('A list of stack members.')
vcstackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1), ).setIndexNames((0, "AT-VCSTACK-MIB", "vcstackId"))
if mibBuilder.loadTexts: vcstackEntry.setStatus('current')
if mibBuilder.loadTexts: vcstackEntry.setDescription('A set of parameters that describe the status of a stack member')
vcstackId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackId.setStatus('current')
if mibBuilder.loadTexts: vcstackId.setDescription('Stack member ID.')
vcstackPendingId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPendingId.setStatus('current')
if mibBuilder.loadTexts: vcstackPendingId.setDescription('The pending stack member ID.')
vcstackMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMacAddr.setStatus('current')
if mibBuilder.loadTexts: vcstackMacAddr.setDescription("Stack member's hardware MAC address.")
vcstackPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPriority.setStatus('current')
if mibBuilder.loadTexts: vcstackPriority.setDescription('The priority for election of the stack master. The lowest number has the highest priority.')
vcstackRole = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("leaving", 1), ("discovering", 2), ("synchronizing", 3), ("backupMember", 4), ("pendingMaster", 5), ("disabledMaster", 6), ("fallbackMaster", 7), ("activeMaster", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackRole.setStatus('current')
if mibBuilder.loadTexts: vcstackRole.setDescription("Stack member's role in the stack.\n                Note: value type fallbackMaster(7) is deprecated.")
vcstackLastRoleChange = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackLastRoleChange.setStatus('current')
if mibBuilder.loadTexts: vcstackLastRoleChange.setDescription('The time and date when the stack member last changed its role in the stack.')
vcstackHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackHostname.setStatus('current')
if mibBuilder.loadTexts: vcstackHostname.setDescription("Stack member's hostname.")
vcstackProductType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackProductType.setStatus('current')
if mibBuilder.loadTexts: vcstackProductType.setDescription('Stack members product type.')
vcstackSWVersionAutoSync = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackSWVersionAutoSync.setStatus('current')
if mibBuilder.loadTexts: vcstackSWVersionAutoSync.setDescription("Whether or not to automatically upgrade the stack member's software.")
vcstackFallbackConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fileExists", 1), ("fileNotFound", 2), ("notConfigured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackFallbackConfigStatus.setStatus('obsolete')
if mibBuilder.loadTexts: vcstackFallbackConfigStatus.setDescription('The status of the fallback configuration file.\n                For AW+ releases, this object is not supported as from software\n                release 5.3.4.')
vcstackFallbackConfigFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackFallbackConfigFilename.setStatus('obsolete')
if mibBuilder.loadTexts: vcstackFallbackConfigFilename.setDescription('The filename of the fallback configuration file.\n                For AW+ releases, this object is not supported as from software\n                release 5.3.4.')
vcstackResiliencyLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("configured", 1), ("successful", 2), ("failed", 3), ("notConfigured", 4), ("stopped", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackResiliencyLinkStatus.setStatus('current')
if mibBuilder.loadTexts: vcstackResiliencyLinkStatus.setDescription('The status of the stack members resilency link.')
vcstackResiliencyLinkInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackResiliencyLinkInterfaceName.setStatus('current')
if mibBuilder.loadTexts: vcstackResiliencyLinkInterfaceName.setDescription('The name of the interface the resiliency link is configured on.')
vcstackActiveStkHardware = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("xemStk", 1), ("builtinStackingPorts", 2), ("none", 3), ("stackXG", 4), ("x6EMXS2", 5), ("stackQS", 6), ("expansionModule", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackActiveStkHardware.setStatus('current')
if mibBuilder.loadTexts: vcstackActiveStkHardware.setDescription('The stack ports hardware type.\n                Note: Value type none(3) is deprecated.\n                Value types xemStk(1), stackXG(4) and x6EMXS2(5) are deprecated as\n                these modules are no longer supported.')
vcstackStkPort1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("neighbourIncompatible", 2), ("discoveringNeighbour", 3), ("learntNeighbour", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStkPort1Status.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackStkPort1Status.setDescription('Status of the stack port 1.')
vcstackStkPort1NeighbourId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStkPort1NeighbourId.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackStkPort1NeighbourId.setDescription('The ID of the neighbour on stack port 1. A value of zero\n                indicates no learned neighbour. For VCStack Plus, 1-12 refers\n                to the cards on chassis member 1 and 13-24 refers to the cards\n                on chassis member 2. Refer to chassisMappingTable for more details.')
vcstackStkPort2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("neighbourIncompatible", 2), ("discoveringNeighbour", 3), ("learntNeighbour", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStkPort2Status.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackStkPort2Status.setDescription('Status of the stack port 2.')
vcstackStkPort2NeighbourId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStkPort2NeighbourId.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackStkPort2NeighbourId.setDescription('The ID of the neighbour on stack port 2. A value of zero\n                indicates no learned neighbour.  For VCStack Plus, 1-12 refers\n                to the cards on chassis member 1 and 13-24 refers to the cards\n                on chassis member 2. Refer to chassisMappingTable for more details.')
vcstackNumMembersJoined = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumMembersJoined.setStatus('current')
if mibBuilder.loadTexts: vcstackNumMembersJoined.setDescription('The number of times the stack acquires a member.')
vcstackNumMembersLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumMembersLeft.setStatus('current')
if mibBuilder.loadTexts: vcstackNumMembersLeft.setDescription('The number of times the stack loses a member.')
vcstackNumIdConflict = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumIdConflict.setStatus('current')
if mibBuilder.loadTexts: vcstackNumIdConflict.setDescription('The number of times that a stack member ID conflicts.')
vcstackNumMasterConflict = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumMasterConflict.setStatus('current')
if mibBuilder.loadTexts: vcstackNumMasterConflict.setDescription('The number of times that a stack master conflict occurs.')
vcstackNumMasterFailover = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumMasterFailover.setStatus('current')
if mibBuilder.loadTexts: vcstackNumMasterFailover.setDescription('The number of times that the stack master fails.')
vcstackNumStkPort1NbrIncompatible = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumStkPort1NbrIncompatible.setStatus('current')
if mibBuilder.loadTexts: vcstackNumStkPort1NbrIncompatible.setDescription('The number of times that the neighbour is detected as incompatible on stack port 1.')
vcstackNumStkPort2NbrIncompatible = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumStkPort2NbrIncompatible.setStatus('current')
if mibBuilder.loadTexts: vcstackNumStkPort2NbrIncompatible.setDescription('The number of times that the neighbour is detected as incompatible on stack port 2.')
vcstackReadinessStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("init", 1), ("syncing", 2), ("ready", 3), ("syncError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackReadinessStatus.setStatus('current')
if mibBuilder.loadTexts: vcstackReadinessStatus.setDescription("Indicates how readily a stack member can take over as master\n                if the current stack master were to fail. Possible values are:\n\n                init (1) - the stack member is completing startup initialization.\n                syncing (2) - the stack member is synchronizing state information\n                with the stack master following startup.\n                ready (3) - the stack member is fully synchronized with the current\n                master and is ready to take over immediately.\n                syncError (4) - state information on the stack member is not correctly\n                synchronized with the current stack master.\n\n                For a stack member to take over as stack master with the least possible\n                network disruption, it must have the 'ready (3)' status.")
vcstackTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6))
vcstackRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 1)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackRole"))
if mibBuilder.loadTexts: vcstackRoleChange.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackRoleChange.setDescription("A trap generated when the stack member's role is changed.")
vcstackMemberJoin = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 2)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackNbrMemberId"))
if mibBuilder.loadTexts: vcstackMemberJoin.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackMemberJoin.setDescription('A trap generated when a member joins in the stack.')
vcstackMemberLeave = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 3)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackNbrMemberId"))
if mibBuilder.loadTexts: vcstackMemberLeave.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackMemberLeave.setDescription('A trap generated when a member leaves from the stack.')
vcstackResiliencyLinkHealthCheckReceiving = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 4)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckReceiving.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckReceiving.setDescription('A trap generated when the resiliency link is activated.')
vcstackResiliencyLinkHealthCheckTimeOut = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 5)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckTimeOut.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckTimeOut.setDescription("A trap generated when the slave's receive timer has timed out\n                indicating that the Slave has lost contact with the Master\n                via the resiliency link.")
vcstackStkPortLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 6)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackStkPortName"))
if mibBuilder.loadTexts: vcstackStkPortLinkUp.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackStkPortLinkUp.setDescription('A trap generated when the link of stack port is up.')
vcstackStkPortLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 7)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackStkPortName"))
if mibBuilder.loadTexts: vcstackStkPortLinkDown.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackStkPortLinkDown.setDescription('A trap generated when the link of stack port is down.')
vcstackNbrMemberId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vcstackNbrMemberId.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackNbrMemberId.setDescription('The stack member id of the neighbor of the member sent this trap.')
vcstackStkPortName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vcstackStkPortName.setStatus('deprecated')
if mibBuilder.loadTexts: vcstackStkPortName.setDescription('The stack port name related this trap.')
vcstackVirtualMacAddressStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackVirtualMacAddressStatus.setStatus('current')
if mibBuilder.loadTexts: vcstackVirtualMacAddressStatus.setDescription('Whether the virtual MAC address is enabled or disabled.')
vcstackVirtualChassisId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackVirtualChassisId.setStatus('current')
if mibBuilder.loadTexts: vcstackVirtualChassisId.setDescription('The current virtual chassis ID.')
vcstackVirtualMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackVirtualMacAddr.setStatus('current')
if mibBuilder.loadTexts: vcstackVirtualMacAddr.setDescription('The virtual MAC address used by the stack.\n\n                 If the virtual MAC address feature is not enabled, this returns\n                 the hardware MAC address used by the system.')
vcstackMasterId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMasterId.setStatus('current')
if mibBuilder.loadTexts: vcstackMasterId.setDescription('The stack ID of the master unit.')
vcstackDisabledMasterMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackDisabledMasterMonitoringStatus.setStatus('current')
if mibBuilder.loadTexts: vcstackDisabledMasterMonitoringStatus.setDescription('Whether the disabled master monitoring is enabled or disabled.')
vcstackPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12), )
if mibBuilder.loadTexts: vcstackPortTable.setStatus('current')
if mibBuilder.loadTexts: vcstackPortTable.setDescription('A list of stack ports.')
vcstackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1), ).setIndexNames((0, "AT-VCSTACK-MIB", "vcstackMemberId"), (0, "AT-VCSTACK-MIB", "vcstackBayId"), (0, "AT-VCSTACK-MIB", "vcstackPort"))
if mibBuilder.loadTexts: vcstackPortEntry.setStatus('current')
if mibBuilder.loadTexts: vcstackPortEntry.setDescription('A set of parameters that describe the status of a stack port')
vcstackMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMemberId.setStatus('current')
if mibBuilder.loadTexts: vcstackMemberId.setDescription('Stack member ID')
vcstackBayId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackBayId.setStatus('current')
if mibBuilder.loadTexts: vcstackBayId.setDescription('Stack member bay number')
vcstackPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPort.setStatus('current')
if mibBuilder.loadTexts: vcstackPort.setDescription('Stack port number')
vcstackPortString = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPortString.setStatus('current')
if mibBuilder.loadTexts: vcstackPortString.setDescription('Display stack port name as a string')
vcstackPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("neighbourIncompatible", 2), ("discoveringNeighbour", 3), ("learntNeighbour", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPortStatus.setStatus('current')
if mibBuilder.loadTexts: vcstackPortStatus.setDescription('Status of stack port.')
vcstackPortNeighbourName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPortNeighbourName.setStatus('current')
if mibBuilder.loadTexts: vcstackPortNeighbourName.setDescription('The port name of the neighbour the is connected\n                to. None means no neighbour present')
mibBuilder.exportSymbols("AT-VCSTACK-MIB", PYSNMP_MODULE_ID=vcstack, vcstackBayId=vcstackBayId, vcstackNumMasterFailover=vcstackNumMasterFailover, vcstackPortStatus=vcstackPortStatus, vcstackStkPortLinkUp=vcstackStkPortLinkUp, vcstackStatus=vcstackStatus, vcstackMemberLeaveNotify=vcstackMemberLeaveNotify, vcstackPendingId=vcstackPendingId, vcstackVirtualMacAddressStatus=vcstackVirtualMacAddressStatus, vcstackNumMasterConflict=vcstackNumMasterConflict, vcstackNbrMemberId=vcstackNbrMemberId, vcstackFallbackConfigStatus=vcstackFallbackConfigStatus, vcstackRoleChangeNotify=vcstackRoleChangeNotify, vcstackMemberId=vcstackMemberId, vcstackVirtualChassisId=vcstackVirtualChassisId, vcstackPort=vcstackPort, vcstackStkPort2Status=vcstackStkPort2Status, vcstackRole=vcstackRole, vcstackResiliencyLinkHealthCheckReceiving=vcstackResiliencyLinkHealthCheckReceiving, vcstackStkPortName=vcstackStkPortName, vcstackProductType=vcstackProductType, vcstackHostname=vcstackHostname, vcstackSWVersionAutoSync=vcstackSWVersionAutoSync, vcstackDisabledMasterMonitoringStatus=vcstackDisabledMasterMonitoringStatus, vcstackLastRoleChange=vcstackLastRoleChange, vcstackPortEntry=vcstackPortEntry, vcstackStkPort1Status=vcstackStkPort1Status, vcstackTable=vcstackTable, vcstackMemberJoin=vcstackMemberJoin, vcstackNumMembersJoined=vcstackNumMembersJoined, vcstackTraps=vcstackTraps, vcstackMacAddr=vcstackMacAddr, vcstackMasterId=vcstackMasterId, vcstackResiliencyLinkHealthCheckTimeOut=vcstackResiliencyLinkHealthCheckTimeOut, vcstackFallbackConfigFilename=vcstackFallbackConfigFilename, vcstackRoleChange=vcstackRoleChange, vcstack=vcstack, vcstackId=vcstackId, vcstackEntry=vcstackEntry, vcstackResiliencyLinkStatus=vcstackResiliencyLinkStatus, vcstackNbrMemberIdNotify=vcstackNbrMemberIdNotify, vcstackVirtualMacAddr=vcstackVirtualMacAddr, vcstackStkPortNameNotify=vcstackStkPortNameNotify, vcstackResiliencyLinkInterfaceName=vcstackResiliencyLinkInterfaceName, vcstackNumStkPort1NbrIncompatible=vcstackNumStkPort1NbrIncompatible, vcstackResiliencyLinkHealthCheckTimeOutNotify=vcstackResiliencyLinkHealthCheckTimeOutNotify, vcstackPortNeighbourName=vcstackPortNeighbourName, vcstackResiliencyLinkHealthCheckReceivingNotify=vcstackResiliencyLinkHealthCheckReceivingNotify, vcstackStkPort2NeighbourId=vcstackStkPort2NeighbourId, vcstackStkPortLinkDownNotify=vcstackStkPortLinkDownNotify, vcstackStkPortLinkUpNotify=vcstackStkPortLinkUpNotify, vcstackMemberLeave=vcstackMemberLeave, vcstackOperationalStatus=vcstackOperationalStatus, vcstackMgmtVlanSubnetAddr=vcstackMgmtVlanSubnetAddr, vcstackStkPort1NeighbourId=vcstackStkPort1NeighbourId, vcstackActiveStkHardware=vcstackActiveStkHardware, vcstackPortTable=vcstackPortTable, vcstackReadinessStatus=vcstackReadinessStatus, vcstackPriority=vcstackPriority, vcstackMemberJoinNotify=vcstackMemberJoinNotify, vcstackNumStkPort2NbrIncompatible=vcstackNumStkPort2NbrIncompatible, vcstackNotifications=vcstackNotifications, vcstackStkPortLinkDown=vcstackStkPortLinkDown, vcstackNumIdConflict=vcstackNumIdConflict, vcstackPortString=vcstackPortString, vcstackNumMembersLeft=vcstackNumMembersLeft, vcstackMgmtVlanId=vcstackMgmtVlanId)
