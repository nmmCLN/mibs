#
# PySNMP MIB module AT-VCSTACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-VCSTACK-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:08:25 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, iso, Counter32, Unsigned32, ModuleIdentity, Gauge32, NotificationType, IpAddress, Bits, TimeTicks, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "ModuleIdentity", "Gauge32", "NotificationType", "IpAddress", "Bits", "TimeTicks", "Counter64", "MibIdentifier")
MacAddress, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "DisplayString", "TextualConvention")
vcstack = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13))
vcstack.setRevisions(('2017-05-11 00:00', '2014-12-24 00:00', '2014-07-04 00:00', '2014-05-26 00:00', '2014-04-24 00:00', '2014-04-15 00:00', '2014-04-09 00:00', '2011-11-03 00:00', '2010-09-07 00:00', '2010-09-03 00:00', '2010-06-15 00:15', '2010-05-24 01:19', '2010-01-15 00:39', '2009-11-05 00:00', '2009-06-08 00:00', '2009-01-20 00:00', '2008-03-19 00:00',))
if mibBuilder.loadTexts: vcstack.setLastUpdated('201705110000Z')
if mibBuilder.loadTexts: vcstack.setOrganization('Allied Telesis, Inc')
vcstackNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0))
vcstackRoleChangeNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 1)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackRole"))
if mibBuilder.loadTexts: vcstackRoleChangeNotify.setStatus('current')
vcstackMemberJoinNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 2)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackNbrMemberIdNotify"))
if mibBuilder.loadTexts: vcstackMemberJoinNotify.setStatus('current')
vcstackMemberLeaveNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 3)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackNbrMemberIdNotify"))
if mibBuilder.loadTexts: vcstackMemberLeaveNotify.setStatus('current')
vcstackResiliencyLinkHealthCheckReceivingNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 4)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckReceivingNotify.setStatus('current')
vcstackResiliencyLinkHealthCheckTimeOutNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 5)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckTimeOutNotify.setStatus('current')
vcstackStkPortLinkUpNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 6)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackStkPortNameNotify"))
if mibBuilder.loadTexts: vcstackStkPortLinkUpNotify.setStatus('current')
vcstackStkPortLinkDownNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 7)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackStkPortNameNotify"))
if mibBuilder.loadTexts: vcstackStkPortLinkDownNotify.setStatus('current')
vcstackNbrMemberIdNotify = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vcstackNbrMemberIdNotify.setStatus('current')
vcstackStkPortNameNotify = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 0, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vcstackStkPortNameNotify.setStatus('current')
vcstackStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normalOperation", 1), ("operatingInFailoverState", 2), ("standaloneUnit", 3), ("ringTopologyBroken", 4), ("vcsDisabled", 5), ("allStkPortsNotUp", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStatus.setStatus('current')
vcstackOperationalStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackOperationalStatus.setStatus('current')
vcstackMgmtVlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMgmtVlanId.setStatus('current')
vcstackMgmtVlanSubnetAddr = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMgmtVlanSubnetAddr.setStatus('current')
vcstackTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5), )
if mibBuilder.loadTexts: vcstackTable.setStatus('current')
vcstackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1), ).setIndexNames((0, "AT-VCSTACK-MIB", "vcstackId"))
if mibBuilder.loadTexts: vcstackEntry.setStatus('current')
vcstackId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackId.setStatus('current')
vcstackPendingId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPendingId.setStatus('current')
vcstackMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMacAddr.setStatus('current')
vcstackPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPriority.setStatus('current')
vcstackRole = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("leaving", 1), ("discovering", 2), ("synchronizing", 3), ("backupMember", 4), ("pendingMaster", 5), ("disabledMaster", 6), ("fallbackMaster", 7), ("activeMaster", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackRole.setStatus('current')
vcstackLastRoleChange = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackLastRoleChange.setStatus('current')
vcstackHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackHostname.setStatus('current')
vcstackProductType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackProductType.setStatus('current')
vcstackSWVersionAutoSync = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackSWVersionAutoSync.setStatus('current')
vcstackFallbackConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fileExists", 1), ("fileNotFound", 2), ("notConfigured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackFallbackConfigStatus.setStatus('obsolete')
vcstackFallbackConfigFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackFallbackConfigFilename.setStatus('obsolete')
vcstackResiliencyLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("configured", 1), ("successful", 2), ("failed", 3), ("notConfigured", 4), ("stopped", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackResiliencyLinkStatus.setStatus('current')
vcstackResiliencyLinkInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackResiliencyLinkInterfaceName.setStatus('current')
vcstackActiveStkHardware = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("xemStk", 1), ("builtinStackingPorts", 2), ("none", 3), ("stackXG", 4), ("x6EMXS2", 5), ("stackQS", 6), ("expansionModule", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackActiveStkHardware.setStatus('current')
vcstackStkPort1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("neighbourIncompatible", 2), ("discoveringNeighbour", 3), ("learntNeighbour", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStkPort1Status.setStatus('deprecated')
vcstackStkPort1NeighbourId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStkPort1NeighbourId.setStatus('deprecated')
vcstackStkPort2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("neighbourIncompatible", 2), ("discoveringNeighbour", 3), ("learntNeighbour", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStkPort2Status.setStatus('deprecated')
vcstackStkPort2NeighbourId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackStkPort2NeighbourId.setStatus('deprecated')
vcstackNumMembersJoined = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumMembersJoined.setStatus('current')
vcstackNumMembersLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumMembersLeft.setStatus('current')
vcstackNumIdConflict = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumIdConflict.setStatus('current')
vcstackNumMasterConflict = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumMasterConflict.setStatus('current')
vcstackNumMasterFailover = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumMasterFailover.setStatus('current')
vcstackNumStkPort1NbrIncompatible = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumStkPort1NbrIncompatible.setStatus('current')
vcstackNumStkPort2NbrIncompatible = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackNumStkPort2NbrIncompatible.setStatus('current')
vcstackReadinessStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("init", 1), ("syncing", 2), ("ready", 3), ("syncError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackReadinessStatus.setStatus('current')
vcstackTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6))
vcstackRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 1)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackRole"))
if mibBuilder.loadTexts: vcstackRoleChange.setStatus('deprecated')
vcstackMemberJoin = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 2)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackNbrMemberId"))
if mibBuilder.loadTexts: vcstackMemberJoin.setStatus('deprecated')
vcstackMemberLeave = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 3)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackNbrMemberId"))
if mibBuilder.loadTexts: vcstackMemberLeave.setStatus('deprecated')
vcstackResiliencyLinkHealthCheckReceiving = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 4)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckReceiving.setStatus('deprecated')
vcstackResiliencyLinkHealthCheckTimeOut = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 5)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
if mibBuilder.loadTexts: vcstackResiliencyLinkHealthCheckTimeOut.setStatus('deprecated')
vcstackStkPortLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 6)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackStkPortName"))
if mibBuilder.loadTexts: vcstackStkPortLinkUp.setStatus('deprecated')
vcstackStkPortLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 7)).setObjects(("AT-VCSTACK-MIB", "vcstackId"), ("AT-VCSTACK-MIB", "vcstackStkPortName"))
if mibBuilder.loadTexts: vcstackStkPortLinkDown.setStatus('deprecated')
vcstackNbrMemberId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vcstackNbrMemberId.setStatus('deprecated')
vcstackStkPortName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vcstackStkPortName.setStatus('deprecated')
vcstackVirtualMacAddressStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackVirtualMacAddressStatus.setStatus('current')
vcstackVirtualChassisId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackVirtualChassisId.setStatus('current')
vcstackVirtualMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackVirtualMacAddr.setStatus('current')
vcstackMasterId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMasterId.setStatus('current')
vcstackDisabledMasterMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackDisabledMasterMonitoringStatus.setStatus('current')
vcstackPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12), )
if mibBuilder.loadTexts: vcstackPortTable.setStatus('current')
vcstackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1), ).setIndexNames((0, "AT-VCSTACK-MIB", "vcstackMemberId"), (0, "AT-VCSTACK-MIB", "vcstackBayId"), (0, "AT-VCSTACK-MIB", "vcstackPort"))
if mibBuilder.loadTexts: vcstackPortEntry.setStatus('current')
vcstackMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackMemberId.setStatus('current')
vcstackBayId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackBayId.setStatus('current')
vcstackPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPort.setStatus('current')
vcstackPortString = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPortString.setStatus('current')
vcstackPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("neighbourIncompatible", 2), ("discoveringNeighbour", 3), ("learntNeighbour", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPortStatus.setStatus('current')
vcstackPortNeighbourName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 12, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcstackPortNeighbourName.setStatus('current')
mibBuilder.exportSymbols("AT-VCSTACK-MIB", vcstackPriority=vcstackPriority, vcstackRoleChange=vcstackRoleChange, vcstackNbrMemberId=vcstackNbrMemberId, vcstackPortNeighbourName=vcstackPortNeighbourName, vcstackStatus=vcstackStatus, vcstackVirtualChassisId=vcstackVirtualChassisId, vcstackVirtualMacAddressStatus=vcstackVirtualMacAddressStatus, vcstackEntry=vcstackEntry, vcstackBayId=vcstackBayId, vcstackVirtualMacAddr=vcstackVirtualMacAddr, PYSNMP_MODULE_ID=vcstack, vcstackNotifications=vcstackNotifications, vcstackMemberJoin=vcstackMemberJoin, vcstackMasterId=vcstackMasterId, vcstackMgmtVlanSubnetAddr=vcstackMgmtVlanSubnetAddr, vcstackMacAddr=vcstackMacAddr, vcstackNumStkPort2NbrIncompatible=vcstackNumStkPort2NbrIncompatible, vcstackRoleChangeNotify=vcstackRoleChangeNotify, vcstackStkPortLinkUpNotify=vcstackStkPortLinkUpNotify, vcstackNbrMemberIdNotify=vcstackNbrMemberIdNotify, vcstackResiliencyLinkInterfaceName=vcstackResiliencyLinkInterfaceName, vcstackRole=vcstackRole, vcstackDisabledMasterMonitoringStatus=vcstackDisabledMasterMonitoringStatus, vcstackPortEntry=vcstackPortEntry, vcstackMemberJoinNotify=vcstackMemberJoinNotify, vcstackFallbackConfigFilename=vcstackFallbackConfigFilename, vcstackOperationalStatus=vcstackOperationalStatus, vcstackResiliencyLinkHealthCheckTimeOutNotify=vcstackResiliencyLinkHealthCheckTimeOutNotify, vcstackStkPortNameNotify=vcstackStkPortNameNotify, vcstackReadinessStatus=vcstackReadinessStatus, vcstackNumIdConflict=vcstackNumIdConflict, vcstackNumMasterFailover=vcstackNumMasterFailover, vcstackStkPort1Status=vcstackStkPort1Status, vcstackResiliencyLinkHealthCheckTimeOut=vcstackResiliencyLinkHealthCheckTimeOut, vcstackActiveStkHardware=vcstackActiveStkHardware, vcstackTable=vcstackTable, vcstackMemberLeave=vcstackMemberLeave, vcstackLastRoleChange=vcstackLastRoleChange, vcstackStkPort1NeighbourId=vcstackStkPort1NeighbourId, vcstackStkPortLinkUp=vcstackStkPortLinkUp, vcstackStkPortName=vcstackStkPortName, vcstackPortTable=vcstackPortTable, vcstackMemberLeaveNotify=vcstackMemberLeaveNotify, vcstackSWVersionAutoSync=vcstackSWVersionAutoSync, vcstackPort=vcstackPort, vcstackFallbackConfigStatus=vcstackFallbackConfigStatus, vcstackMemberId=vcstackMemberId, vcstackResiliencyLinkStatus=vcstackResiliencyLinkStatus, vcstackNumMasterConflict=vcstackNumMasterConflict, vcstackNumMembersLeft=vcstackNumMembersLeft, vcstackResiliencyLinkHealthCheckReceivingNotify=vcstackResiliencyLinkHealthCheckReceivingNotify, vcstack=vcstack, vcstackPendingId=vcstackPendingId, vcstackNumStkPort1NbrIncompatible=vcstackNumStkPort1NbrIncompatible, vcstackPortString=vcstackPortString, vcstackNumMembersJoined=vcstackNumMembersJoined, vcstackStkPort2NeighbourId=vcstackStkPort2NeighbourId, vcstackStkPortLinkDownNotify=vcstackStkPortLinkDownNotify, vcstackStkPort2Status=vcstackStkPort2Status, vcstackId=vcstackId, vcstackTraps=vcstackTraps, vcstackResiliencyLinkHealthCheckReceiving=vcstackResiliencyLinkHealthCheckReceiving, vcstackMgmtVlanId=vcstackMgmtVlanId, vcstackProductType=vcstackProductType, vcstackHostname=vcstackHostname, vcstackStkPortLinkDown=vcstackStkPortLinkDown, vcstackPortStatus=vcstackPortStatus)
