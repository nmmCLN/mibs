#
# PySNMP MIB module BCN-HA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-HA-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:23:59 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, ModuleIdentity, Counter32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, TimeTicks, iso, Counter64, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "TimeTicks", "iso", "Counter64", "IpAddress", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcnHaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 1))
bcnHaMIB.setRevisions(('2010-12-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnHaMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnHaMIB.setLastUpdated('201012150000Z')
if mibBuilder.loadTexts: bcnHaMIB.setOrganization('BlueCat Networks')
if mibBuilder.loadTexts: bcnHaMIB.setContactInfo('BlueCat Networks. Customer Care.\n\n        North America\n        Call: +1.866.491.2228\n        Europe\n        Call: +44.8081.011.306\n        Other\n        Call: +1.416.646.8433\n        \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnHaMIB.setDescription('This module provides status as well as statistical information\n        about the HA service.')
bcnHa = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5))
bcnHaObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2))
bcnHaNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3))
bcnHaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4))
bcnHaServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1))
if mibBuilder.loadTexts: bcnHaServiceStatus.setStatus('current')
if mibBuilder.loadTexts: bcnHaServiceStatus.setDescription('General state of the HA Service.')
bcnHaSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("standalone", 1), ("active", 2), ("passive", 3), ("stopped", 4), ("stopping", 5), ("becomingActive", 6), ("becomingPassive", 7), ("fault", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerOperState.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerOperState.setDescription('Operational state of the Service. The possible states are:\n        standalone(1) The node is not configured to provide clustering\n                      services.\n        active(2)     The system is operational and the node is providing\n                      clustering services.\n        passive(3)    The system is operational and the node is active as\n                      a passive standby for the cluster.\n        stopped(4)    The service is stopped either intentionally (i.e.:\n                      the service is not supposed to run on this node) or\n                      unintentionally (a problem has occurred).\n                      This state might apply to both standalong and\n                      clustered nodes.\n        stopping(5)   The service is in the process of stopping. Stopping\n                      a service might be necessary after a configuration\n                      change.\n        becomingActive (6)  The node is becoming active, either as a result\n                      of a switchover or by initial start.\n        becomingPassive (7) The node is failing over. Another node is taking\n                      charge of the services.\n        fault(8)      An error has been detected and the state is undefined.\n        ')
bcnHaSerReplicationState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notConfigured", 1), ("replicating", 2), ("synchronized", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerReplicationState.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerReplicationState.setDescription('The current state of the replication. All nodes in a cluster \n        must be in synch in order for HA to work correctly. The nodes\n        might be temporarily out of synch during cluster creation or\n        when one of the nodes has been down for a while.')
bcnHaSerAddressTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3), )
if mibBuilder.loadTexts: bcnHaSerAddressTable.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerAddressTable.setDescription('This table keeps the information about the network addresses\n        for the clustered nodes. Most of the time this table will contain\n        one or two rows, depending on the type of IPs configured for\n        clustering.')
bcnHaSerAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1), ).setIndexNames((0, "BCN-HA-MIB", "bcnHaSerAddrTableIndex"))
if mibBuilder.loadTexts: bcnHaSerAddressEntry.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerAddressEntry.setDescription('A logical row in the bcnHaSerAddressTable.')
bcnHaSerAddrTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bcnHaSerAddrTableIndex.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerAddrTableIndex.setDescription('This index will normally be 0 or 1')
bcnHaSerVirtualAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerVirtualAddressType.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerVirtualAddressType.setDescription('The type of address stored in bcnHaSerVirtualAddress.')
bcnHaSerVirtualAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerVirtualAddress.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerVirtualAddress.setDescription('The virtual IP address configured for this node. The type\n        of this mib variable is defined in bcnHaSerVirtualAddressType.\n        This address binds to the active node at all times.')
bcnHaSerPhysicalAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerPhysicalAddressType.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerPhysicalAddressType.setDescription('The type of address stored in bcnHaSerPhysicalAddress.')
bcnHaSerPhysicalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerPhysicalAddress.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerPhysicalAddress.setDescription('The physical IP address configured for this node. The type\n        of this mib variable is defined in bcnHaSerPhisicalAddressType.\n        This address is not affected by switchover events.')
bcnHaSerPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerPeerAddressType.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerPeerAddressType.setDescription('The type of address stored in bcnHaSerPeerAddress.')
bcnHaSerPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnHaSerPeerAddress.setStatus('current')
if mibBuilder.loadTexts: bcnHaSerPeerAddress.setDescription('The physical IP address configured for the peer node. The type\n        of this mib variable is defined in bcnHaSerPeerAddressType.\n        This address is not affected by switchover events.')
bcnHaNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 0))
bcnHaNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1))
bcnHaAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnHaAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: bcnHaAlarmSeverity.setDescription('Severity classification for the alarm.')
bcnHaAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnHaAlarmInfo.setStatus('current')
if mibBuilder.loadTexts: bcnHaAlarmInfo.setDescription('Descriptive information about the alarm event.')
bcnHaAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 0, 1)).setObjects(("BCN-HA-MIB", "bcnHaSerOperState"), ("BCN-HA-MIB", "bcnHaAlarmSeverity"), ("BCN-HA-MIB", "bcnHaAlarmInfo"))
if mibBuilder.loadTexts: bcnHaAlarmNotif.setStatus('current')
if mibBuilder.loadTexts: bcnHaAlarmNotif.setDescription('A bcnHaAlarmNotif signifies that the HA service has transitioned\n        state or a particular event has been detected on the service.')
bcnHaServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 1))
bcnHaServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2))
bcnHaServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 1)).setObjects(("BCN-HA-MIB", "bcnHaSerOperState"), ("BCN-HA-MIB", "bcnHaSerReplicationState"), ("BCN-HA-MIB", "bcnHaSerVirtualAddressType"), ("BCN-HA-MIB", "bcnHaSerVirtualAddress"), ("BCN-HA-MIB", "bcnHaSerPhysicalAddressType"), ("BCN-HA-MIB", "bcnHaSerPhysicalAddress"), ("BCN-HA-MIB", "bcnHaSerPeerAddressType"), ("BCN-HA-MIB", "bcnHaSerPeerAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnHaServiceStatusGroup = bcnHaServiceStatusGroup.setStatus('current')
if mibBuilder.loadTexts: bcnHaServiceStatusGroup.setDescription('Status conformance.')
bcnHaNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 2)).setObjects(("BCN-HA-MIB", "bcnHaAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnHaNotificationEventGroup = bcnHaNotificationEventGroup.setStatus('current')
if mibBuilder.loadTexts: bcnHaNotificationEventGroup.setDescription('Server statistics conformance.')
bcnHaNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 3)).setObjects(("BCN-HA-MIB", "bcnHaAlarmSeverity"), ("BCN-HA-MIB", "bcnHaAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnHaNotificationDataGroup = bcnHaNotificationDataGroup.setStatus('current')
if mibBuilder.loadTexts: bcnHaNotificationDataGroup.setDescription('Server statistics conformance.')
bcnHaStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 1, 1)).setObjects(("BCN-HA-MIB", "bcnHaServiceStatusGroup"), ("BCN-HA-MIB", "bcnHaNotificationEventGroup"), ("BCN-HA-MIB", "bcnHaNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnHaStatusCompliance = bcnHaStatusCompliance.setStatus('current')
if mibBuilder.loadTexts: bcnHaStatusCompliance.setDescription('Basic conformance')
mibBuilder.exportSymbols("BCN-HA-MIB", bcnHaMIB=bcnHaMIB, bcnHaServiceStatus=bcnHaServiceStatus, bcnHaSerPhysicalAddress=bcnHaSerPhysicalAddress, bcnHaSerPeerAddress=bcnHaSerPeerAddress, bcnHaServiceCompliances=bcnHaServiceCompliances, bcnHaServiceStatusGroup=bcnHaServiceStatusGroup, bcnHaSerPhysicalAddressType=bcnHaSerPhysicalAddressType, bcnHaServiceGroups=bcnHaServiceGroups, bcnHaSerOperState=bcnHaSerOperState, bcnHaAlarmInfo=bcnHaAlarmInfo, bcnHaSerVirtualAddressType=bcnHaSerVirtualAddressType, bcnHaNotificationEventGroup=bcnHaNotificationEventGroup, bcnHaNotificationDataGroup=bcnHaNotificationDataGroup, bcnHaNotificationEvents=bcnHaNotificationEvents, bcnHaAlarmSeverity=bcnHaAlarmSeverity, bcnHaSerAddressEntry=bcnHaSerAddressEntry, bcnHa=bcnHa, PYSNMP_MODULE_ID=bcnHaMIB, bcnHaSerVirtualAddress=bcnHaSerVirtualAddress, bcnHaNotification=bcnHaNotification, bcnHaStatusCompliance=bcnHaStatusCompliance, bcnHaSerAddressTable=bcnHaSerAddressTable, bcnHaSerPeerAddressType=bcnHaSerPeerAddressType, bcnHaSerAddrTableIndex=bcnHaSerAddrTableIndex, bcnHaAlarmNotif=bcnHaAlarmNotif, bcnHaConformance=bcnHaConformance, bcnHaSerReplicationState=bcnHaSerReplicationState, bcnHaNotificationData=bcnHaNotificationData, bcnHaObjects=bcnHaObjects)
