#
# PySNMP MIB module T11-FC-SP-ZONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-FC-SP-ZONING-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, mib_2, iso, Integer32, Counter32, Bits, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "mib-2", "iso", "Integer32", "Counter32", "Bits", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
T11FcSpPolicyHashFormat, T11FcSpHashCalculationStatus, T11FcSpPolicyHashValue = mibBuilder.importSymbols("T11-FC-SP-TC-MIB", "T11FcSpPolicyHashFormat", "T11FcSpHashCalculationStatus", "T11FcSpPolicyHashValue")
t11ZsStatsEntry, t11ZsFabricIndex, t11ZsNotifyControlEntry, t11ZsServerEntry = mibBuilder.importSymbols("T11-FC-ZONE-SERVER-MIB", "t11ZsStatsEntry", "t11ZsFabricIndex", "t11ZsNotifyControlEntry", "t11ZsServerEntry")
t11FcSpZoningMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 177))
t11FcSpZoningMIB.setRevisions(('2008-08-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: t11FcSpZoningMIB.setRevisionsDescriptions(('Initial version of this MIB module, published as RFC 5324.',))
if mibBuilder.loadTexts: t11FcSpZoningMIB.setLastUpdated('200808200000Z')
if mibBuilder.loadTexts: t11FcSpZoningMIB.setOrganization('This MIB module was developed through the\n                  coordinated effort of two organizations:\n                  T11 began the development and the IETF (in\n                  the IMSS Working Group) finished it.')
if mibBuilder.loadTexts: t11FcSpZoningMIB.setContactInfo('     Claudio DeSanti\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  EMail: cds@cisco.com\n\n                  Keith McCloghrie\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA 95134 USA\n                  Email: kzm@cisco.com')
if mibBuilder.loadTexts: t11FcSpZoningMIB.setDescription("This MIB module specifies the extensions to the\n           T11-FC-ZONE-SERVER-MIB module that are necessary for the\n           management of Fibre Channel's FC-SP Zoning Servers, as\n           defined in the FC-SP specification.\n\n           The persistence of values written to these MIB objects is\n           the same as the persistence of the objects they extend,\n           i.e., it is given by the value of the relevant instance of\n           t11ZsServerDatabaseStorageType (defined in the\n           T11-FC-ZONE-SERVER-MIB module).\n\n           Copyright (C) The IETF Trust (2008).  This version\n           of this MIB module is part of RFC 5324;  see the RFC\n           itself for full legal notices.")
t11FcSpZsMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 177, 0))
t11FcSpZsMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 177, 1))
t11FcSpZsMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 177, 2))
t11FcSpZsConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 177, 1, 1))
t11FcSpZsStatistics = MibIdentifier((1, 3, 6, 1, 2, 1, 177, 1, 2))
t11FcSpZsServerTable = MibTable((1, 3, 6, 1, 2, 1, 177, 1, 1, 1), )
if mibBuilder.loadTexts: t11FcSpZsServerTable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsServerTable.setDescription('A table which provides FC-SP-specific information about\n           the Zone Servers on each Fabric in one or more Switches.')
t11FcSpZsServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1), )
t11ZsServerEntry.registerAugmentions(("T11-FC-SP-ZONING-MIB", "t11FcSpZsServerEntry"))
t11FcSpZsServerEntry.setIndexNames(*t11ZsServerEntry.getIndexNames())
if mibBuilder.loadTexts: t11FcSpZsServerEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsServerEntry.setDescription('Each entry contains information relevant to FC-SP\n           for a particular Zone Server for a particular Fabric\n           on a particular Switch.  The Fabric and Switch are\n           identified in the same manner as in t11ZsServerEntry.')
t11FcSpZsServerCapabilityObject = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("fcSpZoning", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsServerCapabilityObject.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 184.')
if mibBuilder.loadTexts: t11FcSpZsServerCapabilityObject.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsServerCapabilityObject.setDescription('Capabilities of the Zone Server for the particular Fabric\n           on the particular Switch, with respect to FC-SP Zoning:\n\n               fcSpZoning -- set to 1 to indicate the Switch is\n                             capable of supporting FC-SP Zoning.\n           ')
t11FcSpZsServerEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpZsServerEnabled.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 185.')
if mibBuilder.loadTexts: t11FcSpZsServerEnabled.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsServerEnabled.setDescription('This object indicates whether the Zone Server for the\n           particular Fabric on the particular Switch, is operating in\n           FC-SP Zoning mode.')
t11FcSpZoneSetHashStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 3), T11FcSpHashCalculationStatus().clone('stale')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpZoneSetHashStatus.setReference("t11ZsServerDatabaseStorageType in\n           'Fibre Channel Zone Server MIB', RFC 4936, August 2007.")
if mibBuilder.loadTexts: t11FcSpZoneSetHashStatus.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZoneSetHashStatus.setDescription("When read, the value of this object is either:\n\n             correct -- the corresponding instances of both\n                        t11FcSpActiveZoneSetHash and\n                        t11FcSpZoneSetDatabaseHash contain\n                        the correct hash values; or\n             stale   -- the corresponding instances of\n                        t11FcSpActiveZoneSetHash and\n                        t11FcSpZoneSetDatabaseHash contain\n                        stale (possibly incorrect) values;\n\n           Writing a value of 'calculate' is a request to re-calculate\n           and update the values of the corresponding instances of both\n           t11FcSpActiveZoneSetHash and t11FcSpZoneSetDatabaseHash.\n           Writing a value of 'correct' or 'stale' to this object\n           is an error (e.g., 'wrongValue').\n\n           When the Active Zone Set and/or the Zone Set Database are\n           updated, it is common that multiple changes need to be made\n           at the same time.  In such circumstances, the use of this\n           object allows the hash values to be updated only once after\n           all changes, rather than repeatedly/after each individual\n           change.\n\n           If and when the corresponding instance of\n           t11ZsServerDatabaseStorageType has the value 'permanent(4)',\n           then if write access is supported to any instance of a\n           read-write object in any row of any table governed by the\n           'permanent' value of t11ZsServerDatabaseStorageType, then\n\n           write access to the corresponding instance of this object\n           must also be supported.")
t11FcSpActiveZoneSetHashType = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 4), T11FcSpPolicyHashFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpActiveZoneSetHashType.setStatus('current')
if mibBuilder.loadTexts: t11FcSpActiveZoneSetHashType.setDescription('The format used for the hash value contained in the\n           corresponding instance of t11FcSpActiveZoneSetHash.')
t11FcSpActiveZoneSetHash = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 5), T11FcSpPolicyHashValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpActiveZoneSetHash.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 187.')
if mibBuilder.loadTexts: t11FcSpActiveZoneSetHash.setStatus('current')
if mibBuilder.loadTexts: t11FcSpActiveZoneSetHash.setDescription('The value of the hash for the current Active Zone Set.\n            The format of this value is given by the corresponding\n            instance of t11FcSpActiveZoneSetHashType.')
t11FcSpZoneSetDatabaseHashType = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 6), T11FcSpPolicyHashFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZoneSetDatabaseHashType.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZoneSetDatabaseHashType.setDescription('The format used for the hash value contained in the\n           corresponding instance of t11FcSpZoneSetDatabaseHash.')
t11FcSpZoneSetDatabaseHash = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 1, 1, 7), T11FcSpPolicyHashValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZoneSetDatabaseHash.setReference('- ANSI INCITS 426-2007, T11/Project 1570-D,\n              Fibre Channel - Security Protocols (FC-SP),\n              February 2007, Table 187.')
if mibBuilder.loadTexts: t11FcSpZoneSetDatabaseHash.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZoneSetDatabaseHash.setDescription('The value of the hash for the current Zone Set Database.\n            The format of this value is given by the corresponding\n            instance of t11FcSpZoneSetDatabaseHashType.')
t11FcSpZsStatsTable = MibTable((1, 3, 6, 1, 2, 1, 177, 1, 2, 1), )
if mibBuilder.loadTexts: t11FcSpZsStatsTable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsStatsTable.setDescription('A table of statistics specific to FC-SP that are\n           maintained by Zone Servers.')
t11FcSpZsStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1), )
t11ZsStatsEntry.registerAugmentions(("T11-FC-SP-ZONING-MIB", "t11FcSpZsStatsEntry"))
t11FcSpZsStatsEntry.setIndexNames(*t11ZsStatsEntry.getIndexNames())
if mibBuilder.loadTexts: t11FcSpZsStatsEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsStatsEntry.setDescription('A set of statistics specific to FC-SP for a particular\n           Zone Server for a particular Fabric on a particular Switch.\n           The Fabric and Switch are identified in the same manner as\n           in t11ZsStatsEntry.')
t11FcSpZsSPCMITrequestsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsSPCMITrequestsSent.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsSPCMITrequestsSent.setDescription("The number of SP Commit Zone Changes (SPCMIT) operation\n\n           requests sent by the Zone Server.\n\n           This counter has no discontinuities other than those\n           that all Counter32's have when sysUpTime=0.")
t11FcSpZsSPCMITrequestsAccepted = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsSPCMITrequestsAccepted.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsSPCMITrequestsAccepted.setDescription("The number of SP Commit Zone Changes (SPCMIT) operation\n           requests received and accepted by the Zone Server.\n\n           This counter has no discontinuities other than those\n           that all Counter32's have when sysUpTime=0.")
t11FcSpZsSPCMITrequestsRejected = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsSPCMITrequestsRejected.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsSPCMITrequestsRejected.setDescription("The number of SP Commit Zone Changes (SPCMIT) operation\n           requests received but rejected by the Zone Server.\n\n           This counter has no discontinuities other than those\n           that all Counter32's have when sysUpTime=0.")
t11FcSpZsZcpRequestsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsZcpRequestsSent.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsZcpRequestsSent.setDescription("The number of Zoning Check Protocol (ZCP) requests sent\n           by the Zone Server.\n\n           This counter has no discontinuities other than those\n           that all Counter32's have when sysUpTime=0.")
t11FcSpZsZcpRequestsAccepted = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsZcpRequestsAccepted.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsZcpRequestsAccepted.setDescription("The number of Zoning Check Protocol (ZCP) requests received\n\n           and accepted by the Zone Server.\n\n           This counter has no discontinuities other than those\n           that all Counter32's have when sysUpTime=0.")
t11FcSpZsZcpRequestsRejected = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsZcpRequestsRejected.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsZcpRequestsRejected.setDescription("The number of Zoning Check Protocol (ZCP) requests received\n           but rejected by the Zone Server.\n\n           This counter has no discontinuities other than those\n           that all Counter32's have when sysUpTime=0.")
t11FcSpZsZirRequestsAccepted = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsZirRequestsAccepted.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsZirRequestsAccepted.setDescription("The number of Zoning Information Request (ZIR) requests\n           received and accepted by the Zone Server.\n\n           This counter has no discontinuities other than those\n           that all Counter32's have when sysUpTime=0.")
t11FcSpZsZirRequestsRejected = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcSpZsZirRequestsRejected.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsZirRequestsRejected.setDescription("The number of Zoning Information Request (ZIR) requests\n           received but rejected by the Zone Server.\n\n           This counter has no discontinuities other than those\n           that all Counter32's have when sysUpTime=0.")
t11FcSpZsNotifyControlTable = MibTable((1, 3, 6, 1, 2, 1, 177, 1, 1, 2), )
if mibBuilder.loadTexts: t11FcSpZsNotifyControlTable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsNotifyControlTable.setDescription('A table of control information for notifications\n           generated due to Zone Server events related to\n           FC-SP Zoning.')
t11FcSpZsNotifyControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 177, 1, 1, 2, 1), )
t11ZsNotifyControlEntry.registerAugmentions(("T11-FC-SP-ZONING-MIB", "t11FcSpZsNotifyControlEntry"))
t11FcSpZsNotifyControlEntry.setIndexNames(*t11ZsNotifyControlEntry.getIndexNames())
if mibBuilder.loadTexts: t11FcSpZsNotifyControlEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsNotifyControlEntry.setDescription('Each entry is an augmentation of the notification control\n           information for a Zone Server for a particular Fabric on a\n           particular Switch.  The Fabric and Switch are identified in\n           the same manner as in t11ZsNotifyControlEntry.')
t11FcSpZsNotifyJoinSuccessEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpZsNotifyJoinSuccessEnable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsNotifyJoinSuccessEnable.setDescription('This object specifies whether\n           t11FcSpZsFabricJoinFailureNotify notifications should be\n           generated by the Zone Server for this Fabric.')
t11FcSpZsNotifyJoinFailureEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 177, 1, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FcSpZsNotifyJoinFailureEnable.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsNotifyJoinFailureEnable.setDescription('This object specifies whether\n           t11FcSpZsFabricJoinSuccessNotify notifications should be\n           generated by the Zone Server for this Fabric.')
t11FcSpZsFabricJoinSuccessNotify = NotificationType((1, 3, 6, 1, 2, 1, 177, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("T11-FC-ZONE-SERVER-MIB", "t11ZsFabricIndex"))
if mibBuilder.loadTexts: t11FcSpZsFabricJoinSuccessNotify.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsFabricJoinSuccessNotify.setDescription('This notification indicates that a Switch that is part\n           of one Fabric (indicated by the value of t11ZsFabricIndex)\n           has successfully joined (on the interface indicated by the\n           value of ifIndex) with a Switch that is part of another\n           Fabric.\n\n           If multiple Virtual Fabrics are configured on an interface,\n           and all are successfully joined at the same time, and if\n           the agent so chooses, then it can generate just one\n           notification in which t11ZsFabricIndex has the value 4096.')
t11FcSpZsFabricJoinFailureNotify = NotificationType((1, 3, 6, 1, 2, 1, 177, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("T11-FC-ZONE-SERVER-MIB", "t11ZsFabricIndex"))
if mibBuilder.loadTexts: t11FcSpZsFabricJoinFailureNotify.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsFabricJoinFailureNotify.setDescription('This notification indicates that an E_Port on the local\n           Switch has entered the Isolated state because a join\n           between two Fabrics failed.  The failure occurred on the\n           local Fabric indicated by the value of t11ZsFabricIndex,\n           on the interface indicated by the value of ifIndex.\n\n           If multiple Virtual Fabrics are configured on an interface,\n           and all have a failure to join at the same time, and if the\n           agent so chooses, then it can generate just one notification\n           in which t11ZsFabricIndex has the value 4096.')
t11FcSpZsMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 177, 2, 1))
t11FcSpZsMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 177, 2, 2))
t11FcSpZsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 177, 2, 1, 1)).setObjects(("T11-FC-SP-ZONING-MIB", "t11FcSpZsObjectsGroup"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsNotificationControlGroup"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsNotificationGroup"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpZsMIBCompliance = t11FcSpZsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsMIBCompliance.setDescription("The compliance statement for entities that\n           implement the extensions specified in FC-SP for\n           Fibre Channel's Zone Server.")
t11FcSpZsObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 177, 2, 2, 1)).setObjects(("T11-FC-SP-ZONING-MIB", "t11FcSpZsServerCapabilityObject"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsServerEnabled"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZoneSetHashStatus"), ("T11-FC-SP-ZONING-MIB", "t11FcSpActiveZoneSetHashType"), ("T11-FC-SP-ZONING-MIB", "t11FcSpActiveZoneSetHash"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZoneSetDatabaseHashType"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZoneSetDatabaseHash"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpZsObjectsGroup = t11FcSpZsObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsObjectsGroup.setDescription('A collection of objects for Zone configuration\n\n           information of a Zone Server capable of\n           operating in FC-SP Zoning mode.')
t11FcSpZsNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 177, 2, 2, 2)).setObjects(("T11-FC-SP-ZONING-MIB", "t11FcSpZsNotifyJoinSuccessEnable"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsNotifyJoinFailureEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpZsNotificationControlGroup = t11FcSpZsNotificationControlGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsNotificationControlGroup.setDescription('A collection of notification control objects for\n           monitoring Zone Server failures specific to FC-SP.')
t11FcSpZsStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 177, 2, 2, 3)).setObjects(("T11-FC-SP-ZONING-MIB", "t11FcSpZsSPCMITrequestsSent"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsSPCMITrequestsAccepted"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsSPCMITrequestsRejected"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZcpRequestsSent"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZcpRequestsAccepted"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZcpRequestsRejected"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZirRequestsAccepted"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsZirRequestsRejected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpZsStatisticsGroup = t11FcSpZsStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsStatisticsGroup.setDescription('A collection of objects for collecting Zone Server\n            statistics which are specific to FC-SP.')
t11FcSpZsNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 177, 2, 2, 4)).setObjects(("T11-FC-SP-ZONING-MIB", "t11FcSpZsFabricJoinSuccessNotify"), ("T11-FC-SP-ZONING-MIB", "t11FcSpZsFabricJoinFailureNotify"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcSpZsNotificationGroup = t11FcSpZsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcSpZsNotificationGroup.setDescription('A collection of notification(s) for monitoring\n           Zone Server events that are specific to FC-SP.')
mibBuilder.exportSymbols("T11-FC-SP-ZONING-MIB", t11FcSpZoneSetDatabaseHashType=t11FcSpZoneSetDatabaseHashType, t11FcSpZoneSetHashStatus=t11FcSpZoneSetHashStatus, t11FcSpZoneSetDatabaseHash=t11FcSpZoneSetDatabaseHash, t11FcSpZsSPCMITrequestsRejected=t11FcSpZsSPCMITrequestsRejected, t11FcSpZsStatisticsGroup=t11FcSpZsStatisticsGroup, t11FcSpZsZirRequestsRejected=t11FcSpZsZirRequestsRejected, t11FcSpZsNotifyControlTable=t11FcSpZsNotifyControlTable, t11FcSpZsServerEntry=t11FcSpZsServerEntry, t11FcSpZsFabricJoinSuccessNotify=t11FcSpZsFabricJoinSuccessNotify, t11FcSpZsServerTable=t11FcSpZsServerTable, t11FcSpZsStatsTable=t11FcSpZsStatsTable, t11FcSpZsNotifyControlEntry=t11FcSpZsNotifyControlEntry, t11FcSpZsSPCMITrequestsAccepted=t11FcSpZsSPCMITrequestsAccepted, t11FcSpZsNotificationControlGroup=t11FcSpZsNotificationControlGroup, t11FcSpZsNotifyJoinFailureEnable=t11FcSpZsNotifyJoinFailureEnable, t11FcSpZsStatsEntry=t11FcSpZsStatsEntry, t11FcSpZsMIBGroups=t11FcSpZsMIBGroups, t11FcSpZsConfiguration=t11FcSpZsConfiguration, t11FcSpZsZcpRequestsRejected=t11FcSpZsZcpRequestsRejected, t11FcSpZsServerEnabled=t11FcSpZsServerEnabled, t11FcSpZsMIBObjects=t11FcSpZsMIBObjects, t11FcSpActiveZoneSetHash=t11FcSpActiveZoneSetHash, t11FcSpZsZirRequestsAccepted=t11FcSpZsZirRequestsAccepted, t11FcSpZsMIBCompliance=t11FcSpZsMIBCompliance, t11FcSpZsZcpRequestsAccepted=t11FcSpZsZcpRequestsAccepted, t11FcSpZsMIBCompliances=t11FcSpZsMIBCompliances, PYSNMP_MODULE_ID=t11FcSpZoningMIB, t11FcSpZsObjectsGroup=t11FcSpZsObjectsGroup, t11FcSpZsZcpRequestsSent=t11FcSpZsZcpRequestsSent, t11FcSpZsSPCMITrequestsSent=t11FcSpZsSPCMITrequestsSent, t11FcSpZsMIBConformance=t11FcSpZsMIBConformance, t11FcSpActiveZoneSetHashType=t11FcSpActiveZoneSetHashType, t11FcSpZsStatistics=t11FcSpZsStatistics, t11FcSpZsMIBNotifications=t11FcSpZsMIBNotifications, t11FcSpZsServerCapabilityObject=t11FcSpZsServerCapabilityObject, t11FcSpZsFabricJoinFailureNotify=t11FcSpZsFabricJoinFailureNotify, t11FcSpZsNotificationGroup=t11FcSpZsNotificationGroup, t11FcSpZsNotifyJoinSuccessEnable=t11FcSpZsNotifyJoinSuccessEnable, t11FcSpZoningMIB=t11FcSpZoningMIB)
