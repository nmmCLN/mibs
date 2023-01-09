#
# PySNMP MIB module Q-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/Q-BRIDGE-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:17 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
dot1dBasePort, dot1dBasePortEntry, dot1dBridge = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort", "dot1dBasePortEntry", "dot1dBridge")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, ObjectIdentity, iso, Counter32, NotificationType, Integer32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "ObjectIdentity", "iso", "Counter32", "NotificationType", "Integer32", "Unsigned32", "Counter64")
MacAddress, TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
qBridgeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 17, 7))
qBridgeMIB.setRevisions(('2006-01-09 00:00', '1999-08-25 00:00',))
if mibBuilder.loadTexts: qBridgeMIB.setLastUpdated('200601090000Z')
if mibBuilder.loadTexts: qBridgeMIB.setOrganization('IETF Bridge MIB Working Group')
qBridgeMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1))
class PortList(TextualConvention, OctetString):
    status = 'current'

class VlanIndex(TextualConvention, Unsigned32):
    status = 'current'

class VlanId(TextualConvention, Integer32):
    reference = 'IEEE Std 802.1Q 2003 Edition, Virtual Bridged Local Area Networks.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class VlanIdOrAny(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(4095, 4095), )
class VlanIdOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), )
class VlanIdOrAnyOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ValueRangeConstraint(4095, 4095), )
dot1qBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 1))
dot1qTp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 2))
dot1qStatic = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 3))
dot1qVlan = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 4))
dot1vProtocol = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 1, 5))
dot1qVlanVersionNumber = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("version1", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qVlanVersionNumber.setStatus('current')
dot1qMaxVlanId = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 2), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qMaxVlanId.setStatus('current')
dot1qMaxSupportedVlans = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qMaxSupportedVlans.setStatus('current')
dot1qNumVlans = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qNumVlans.setStatus('current')
dot1qGvrpStatus = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 5), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qGvrpStatus.setStatus('current')
dot1qFdbTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1), )
if mibBuilder.loadTexts: dot1qFdbTable.setStatus('current')
dot1qFdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"))
if mibBuilder.loadTexts: dot1qFdbEntry.setStatus('current')
dot1qFdbId = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: dot1qFdbId.setStatus('current')
dot1qFdbDynamicCount = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qFdbDynamicCount.setStatus('current')
dot1qTpFdbTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2), )
if mibBuilder.loadTexts: dot1qTpFdbTable.setStatus('current')
dot1qTpFdbEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"))
if mibBuilder.loadTexts: dot1qTpFdbEntry.setStatus('current')
dot1qTpFdbAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: dot1qTpFdbAddress.setStatus('current')
dot1qTpFdbPort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpFdbPort.setStatus('current')
dot1qTpFdbStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpFdbStatus.setStatus('current')
dot1qTpGroupTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3), )
if mibBuilder.loadTexts: dot1qTpGroupTable.setStatus('current')
dot1qTpGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"), (0, "Q-BRIDGE-MIB", "dot1qTpGroupAddress"))
if mibBuilder.loadTexts: dot1qTpGroupEntry.setStatus('current')
dot1qTpGroupAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: dot1qTpGroupAddress.setStatus('current')
dot1qTpGroupEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpGroupEgressPorts.setStatus('current')
dot1qTpGroupLearnt = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpGroupLearnt.setStatus('current')
dot1qForwardAllTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4), )
if mibBuilder.loadTexts: dot1qForwardAllTable.setStatus('current')
dot1qForwardAllEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: dot1qForwardAllEntry.setStatus('current')
dot1qForwardAllPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qForwardAllPorts.setStatus('current')
dot1qForwardAllStaticPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qForwardAllStaticPorts.setStatus('current')
dot1qForwardAllForbiddenPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qForwardAllForbiddenPorts.setStatus('current')
dot1qForwardUnregisteredTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5), )
if mibBuilder.loadTexts: dot1qForwardUnregisteredTable.setStatus('current')
dot1qForwardUnregisteredEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: dot1qForwardUnregisteredEntry.setStatus('current')
dot1qForwardUnregisteredPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qForwardUnregisteredPorts.setStatus('current')
dot1qForwardUnregisteredStaticPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qForwardUnregisteredStaticPorts.setStatus('current')
dot1qForwardUnregisteredForbiddenPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qForwardUnregisteredForbiddenPorts.setStatus('current')
dot1qStaticUnicastTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1), )
if mibBuilder.loadTexts: dot1qStaticUnicastTable.setStatus('current')
dot1qStaticUnicastEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qStaticUnicastAddress"), (0, "Q-BRIDGE-MIB", "dot1qStaticUnicastReceivePort"))
if mibBuilder.loadTexts: dot1qStaticUnicastEntry.setStatus('current')
dot1qStaticUnicastAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: dot1qStaticUnicastAddress.setStatus('current')
dot1qStaticUnicastReceivePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: dot1qStaticUnicastReceivePort.setStatus('current')
dot1qStaticUnicastAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qStaticUnicastAllowedToGoTo.setStatus('current')
dot1qStaticUnicastStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5))).clone('permanent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qStaticUnicastStatus.setStatus('current')
dot1qStaticMulticastTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2), )
if mibBuilder.loadTexts: dot1qStaticMulticastTable.setStatus('current')
dot1qStaticMulticastEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"), (0, "Q-BRIDGE-MIB", "dot1qStaticMulticastAddress"), (0, "Q-BRIDGE-MIB", "dot1qStaticMulticastReceivePort"))
if mibBuilder.loadTexts: dot1qStaticMulticastEntry.setStatus('current')
dot1qStaticMulticastAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: dot1qStaticMulticastAddress.setStatus('current')
dot1qStaticMulticastReceivePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: dot1qStaticMulticastReceivePort.setStatus('current')
dot1qStaticMulticastStaticEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qStaticMulticastStaticEgressPorts.setStatus('current')
dot1qStaticMulticastForbiddenEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qStaticMulticastForbiddenEgressPorts.setStatus('current')
dot1qStaticMulticastStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5))).clone('permanent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qStaticMulticastStatus.setStatus('current')
dot1qVlanNumDeletes = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qVlanNumDeletes.setStatus('current')
dot1qVlanCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2), )
if mibBuilder.loadTexts: dot1qVlanCurrentTable.setStatus('current')
dot1qVlanCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanTimeMark"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: dot1qVlanCurrentEntry.setStatus('current')
dot1qVlanTimeMark = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 1), TimeFilter())
if mibBuilder.loadTexts: dot1qVlanTimeMark.setStatus('current')
dot1qVlanIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 2), VlanIndex())
if mibBuilder.loadTexts: dot1qVlanIndex.setStatus('current')
dot1qVlanFdbId = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qVlanFdbId.setStatus('current')
dot1qVlanCurrentEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qVlanCurrentEgressPorts.setStatus('current')
dot1qVlanCurrentUntaggedPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qVlanCurrentUntaggedPorts.setStatus('current')
dot1qVlanStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("permanent", 2), ("dynamicGvrp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qVlanStatus.setStatus('current')
dot1qVlanCreationTime = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qVlanCreationTime.setStatus('current')
dot1qVlanStaticTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3), )
if mibBuilder.loadTexts: dot1qVlanStaticTable.setStatus('current')
dot1qVlanStaticEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: dot1qVlanStaticEntry.setStatus('current')
dot1qVlanStaticName = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1qVlanStaticName.setStatus('current')
dot1qVlanStaticEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 2), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1qVlanStaticEgressPorts.setStatus('current')
dot1qVlanForbiddenEgressPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1qVlanForbiddenEgressPorts.setStatus('current')
dot1qVlanStaticUntaggedPorts = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1qVlanStaticUntaggedPorts.setStatus('current')
dot1qVlanStaticRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1qVlanStaticRowStatus.setStatus('current')
dot1qNextFreeLocalVlanIndex = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(4096, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qNextFreeLocalVlanIndex.setStatus('current')
dot1qPortVlanTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5), )
if mibBuilder.loadTexts: dot1qPortVlanTable.setStatus('current')
dot1qPortVlanEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1), )
dot1dBasePortEntry.registerAugmentions(("Q-BRIDGE-MIB", "dot1qPortVlanEntry"))
dot1qPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: dot1qPortVlanEntry.setStatus('current')
dot1qPvid = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 1), VlanIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qPvid.setStatus('current')
dot1qPortAcceptableFrameTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("admitAll", 1), ("admitOnlyVlanTagged", 2))).clone('admitAll')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qPortAcceptableFrameTypes.setStatus('current')
dot1qPortIngressFiltering = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qPortIngressFiltering.setStatus('current')
dot1qPortGvrpStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 4), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qPortGvrpStatus.setStatus('current')
dot1qPortGvrpFailedRegistrations = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qPortGvrpFailedRegistrations.setStatus('current')
dot1qPortGvrpLastPduOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qPortGvrpLastPduOrigin.setStatus('current')
dot1qPortRestrictedVlanRegistration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qPortRestrictedVlanRegistration.setStatus('current')
dot1qPortVlanStatisticsTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6), )
if mibBuilder.loadTexts: dot1qPortVlanStatisticsTable.setStatus('current')
dot1qPortVlanStatisticsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: dot1qPortVlanStatisticsEntry.setStatus('current')
dot1qTpVlanPortInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortInFrames.setStatus('current')
dot1qTpVlanPortOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortOutFrames.setStatus('current')
dot1qTpVlanPortInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortInDiscards.setStatus('current')
dot1qTpVlanPortInOverflowFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortInOverflowFrames.setStatus('current')
dot1qTpVlanPortOutOverflowFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortOutOverflowFrames.setStatus('current')
dot1qTpVlanPortInOverflowDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortInOverflowDiscards.setStatus('current')
dot1qPortVlanHCStatisticsTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7), )
if mibBuilder.loadTexts: dot1qPortVlanHCStatisticsTable.setStatus('current')
dot1qPortVlanHCStatisticsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: dot1qPortVlanHCStatisticsEntry.setStatus('current')
dot1qTpVlanPortHCInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortHCInFrames.setStatus('current')
dot1qTpVlanPortHCOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortHCOutFrames.setStatus('current')
dot1qTpVlanPortHCInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1qTpVlanPortHCInDiscards.setStatus('current')
dot1qLearningConstraintsTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8), )
if mibBuilder.loadTexts: dot1qLearningConstraintsTable.setStatus('current')
dot1qLearningConstraintsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qConstraintVlan"), (0, "Q-BRIDGE-MIB", "dot1qConstraintSet"))
if mibBuilder.loadTexts: dot1qLearningConstraintsEntry.setStatus('current')
dot1qConstraintVlan = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 1), VlanIndex())
if mibBuilder.loadTexts: dot1qConstraintVlan.setStatus('current')
dot1qConstraintSet = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: dot1qConstraintSet.setStatus('current')
dot1qConstraintType = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("independent", 1), ("shared", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1qConstraintType.setStatus('current')
dot1qConstraintStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1qConstraintStatus.setStatus('current')
dot1qConstraintSetDefault = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qConstraintSetDefault.setStatus('current')
dot1qConstraintTypeDefault = MibScalar((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("independent", 1), ("shared", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qConstraintTypeDefault.setStatus('current')
dot1vProtocolGroupTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1), )
if mibBuilder.loadTexts: dot1vProtocolGroupTable.setStatus('current')
dot1vProtocolGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1vProtocolTemplateFrameType"), (0, "Q-BRIDGE-MIB", "dot1vProtocolTemplateProtocolValue"))
if mibBuilder.loadTexts: dot1vProtocolGroupEntry.setStatus('current')
dot1vProtocolTemplateFrameType = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ethernet", 1), ("rfc1042", 2), ("snap8021H", 3), ("snapOther", 4), ("llcOther", 5))))
if mibBuilder.loadTexts: dot1vProtocolTemplateFrameType.setStatus('current')
dot1vProtocolTemplateProtocolValue = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1, 2), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(2, 2), ValueSizeConstraint(5, 5), )))
if mibBuilder.loadTexts: dot1vProtocolTemplateProtocolValue.setStatus('current')
dot1vProtocolGroupId = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1vProtocolGroupId.setStatus('current')
dot1vProtocolGroupRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1vProtocolGroupRowStatus.setStatus('current')
dot1vProtocolPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2), )
if mibBuilder.loadTexts: dot1vProtocolPortTable.setStatus('current')
dot1vProtocolPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1vProtocolPortGroupId"))
if mibBuilder.loadTexts: dot1vProtocolPortEntry.setStatus('current')
dot1vProtocolPortGroupId = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dot1vProtocolPortGroupId.setStatus('current')
dot1vProtocolPortGroupVid = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1vProtocolPortGroupVid.setStatus('current')
dot1vProtocolPortRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1vProtocolPortRowStatus.setStatus('current')
qBridgeConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 2))
qBridgeGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 2, 1))
qBridgeCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 7, 2, 2))
qBridgeBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 1)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanVersionNumber"), ("Q-BRIDGE-MIB", "dot1qMaxVlanId"), ("Q-BRIDGE-MIB", "dot1qMaxSupportedVlans"), ("Q-BRIDGE-MIB", "dot1qNumVlans"), ("Q-BRIDGE-MIB", "dot1qGvrpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeBaseGroup = qBridgeBaseGroup.setStatus('current')
qBridgeFdbUnicastGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 2)).setObjects(("Q-BRIDGE-MIB", "dot1qFdbDynamicCount"), ("Q-BRIDGE-MIB", "dot1qTpFdbPort"), ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeFdbUnicastGroup = qBridgeFdbUnicastGroup.setStatus('current')
qBridgeFdbMulticastGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 3)).setObjects(("Q-BRIDGE-MIB", "dot1qTpGroupEgressPorts"), ("Q-BRIDGE-MIB", "dot1qTpGroupLearnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeFdbMulticastGroup = qBridgeFdbMulticastGroup.setStatus('current')
qBridgeServiceRequirementsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 4)).setObjects(("Q-BRIDGE-MIB", "dot1qForwardAllPorts"), ("Q-BRIDGE-MIB", "dot1qForwardAllStaticPorts"), ("Q-BRIDGE-MIB", "dot1qForwardAllForbiddenPorts"), ("Q-BRIDGE-MIB", "dot1qForwardUnregisteredPorts"), ("Q-BRIDGE-MIB", "dot1qForwardUnregisteredStaticPorts"), ("Q-BRIDGE-MIB", "dot1qForwardUnregisteredForbiddenPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeServiceRequirementsGroup = qBridgeServiceRequirementsGroup.setStatus('current')
qBridgeFdbStaticGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 5)).setObjects(("Q-BRIDGE-MIB", "dot1qStaticUnicastAllowedToGoTo"), ("Q-BRIDGE-MIB", "dot1qStaticUnicastStatus"), ("Q-BRIDGE-MIB", "dot1qStaticMulticastStaticEgressPorts"), ("Q-BRIDGE-MIB", "dot1qStaticMulticastForbiddenEgressPorts"), ("Q-BRIDGE-MIB", "dot1qStaticMulticastStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeFdbStaticGroup = qBridgeFdbStaticGroup.setStatus('current')
qBridgeVlanGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 6)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanNumDeletes"), ("Q-BRIDGE-MIB", "dot1qVlanFdbId"), ("Q-BRIDGE-MIB", "dot1qVlanCurrentEgressPorts"), ("Q-BRIDGE-MIB", "dot1qVlanCurrentUntaggedPorts"), ("Q-BRIDGE-MIB", "dot1qVlanStatus"), ("Q-BRIDGE-MIB", "dot1qVlanCreationTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeVlanGroup = qBridgeVlanGroup.setStatus('current')
qBridgeVlanStaticGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 7)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanStaticName"), ("Q-BRIDGE-MIB", "dot1qVlanStaticEgressPorts"), ("Q-BRIDGE-MIB", "dot1qVlanForbiddenEgressPorts"), ("Q-BRIDGE-MIB", "dot1qVlanStaticUntaggedPorts"), ("Q-BRIDGE-MIB", "dot1qVlanStaticRowStatus"), ("Q-BRIDGE-MIB", "dot1qNextFreeLocalVlanIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeVlanStaticGroup = qBridgeVlanStaticGroup.setStatus('current')
qBridgePortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 8)).setObjects(("Q-BRIDGE-MIB", "dot1qPvid"), ("Q-BRIDGE-MIB", "dot1qPortAcceptableFrameTypes"), ("Q-BRIDGE-MIB", "dot1qPortIngressFiltering"), ("Q-BRIDGE-MIB", "dot1qPortGvrpStatus"), ("Q-BRIDGE-MIB", "dot1qPortGvrpFailedRegistrations"), ("Q-BRIDGE-MIB", "dot1qPortGvrpLastPduOrigin"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgePortGroup = qBridgePortGroup.setStatus('deprecated')
qBridgeVlanStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 9)).setObjects(("Q-BRIDGE-MIB", "dot1qTpVlanPortInFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortOutFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortInDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeVlanStatisticsGroup = qBridgeVlanStatisticsGroup.setStatus('current')
qBridgeVlanStatisticsOverflowGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 10)).setObjects(("Q-BRIDGE-MIB", "dot1qTpVlanPortInOverflowFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortOutOverflowFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortInOverflowDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeVlanStatisticsOverflowGroup = qBridgeVlanStatisticsOverflowGroup.setStatus('current')
qBridgeVlanHCStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 11)).setObjects(("Q-BRIDGE-MIB", "dot1qTpVlanPortHCInFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortHCOutFrames"), ("Q-BRIDGE-MIB", "dot1qTpVlanPortHCInDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeVlanHCStatisticsGroup = qBridgeVlanHCStatisticsGroup.setStatus('current')
qBridgeLearningConstraintsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 12)).setObjects(("Q-BRIDGE-MIB", "dot1qConstraintType"), ("Q-BRIDGE-MIB", "dot1qConstraintStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeLearningConstraintsGroup = qBridgeLearningConstraintsGroup.setStatus('current')
qBridgeLearningConstraintDefaultGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 13)).setObjects(("Q-BRIDGE-MIB", "dot1qConstraintSetDefault"), ("Q-BRIDGE-MIB", "dot1qConstraintTypeDefault"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeLearningConstraintDefaultGroup = qBridgeLearningConstraintDefaultGroup.setStatus('current')
qBridgeClassificationDeviceGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 14)).setObjects(("Q-BRIDGE-MIB", "dot1vProtocolGroupId"), ("Q-BRIDGE-MIB", "dot1vProtocolGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeClassificationDeviceGroup = qBridgeClassificationDeviceGroup.setStatus('current')
qBridgeClassificationPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 15)).setObjects(("Q-BRIDGE-MIB", "dot1vProtocolPortGroupVid"), ("Q-BRIDGE-MIB", "dot1vProtocolPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeClassificationPortGroup = qBridgeClassificationPortGroup.setStatus('current')
qBridgePortGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 16)).setObjects(("Q-BRIDGE-MIB", "dot1qPvid"), ("Q-BRIDGE-MIB", "dot1qPortAcceptableFrameTypes"), ("Q-BRIDGE-MIB", "dot1qPortIngressFiltering"), ("Q-BRIDGE-MIB", "dot1qPortGvrpStatus"), ("Q-BRIDGE-MIB", "dot1qPortGvrpFailedRegistrations"), ("Q-BRIDGE-MIB", "dot1qPortGvrpLastPduOrigin"), ("Q-BRIDGE-MIB", "dot1qPortRestrictedVlanRegistration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgePortGroup2 = qBridgePortGroup2.setStatus('current')
qBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 7, 2, 2, 1)).setObjects(("Q-BRIDGE-MIB", "qBridgeBaseGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanStaticGroup"), ("Q-BRIDGE-MIB", "qBridgePortGroup"), ("Q-BRIDGE-MIB", "qBridgeFdbUnicastGroup"), ("Q-BRIDGE-MIB", "qBridgeFdbMulticastGroup"), ("Q-BRIDGE-MIB", "qBridgeServiceRequirementsGroup"), ("Q-BRIDGE-MIB", "qBridgeFdbStaticGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanStatisticsGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanStatisticsOverflowGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanHCStatisticsGroup"), ("Q-BRIDGE-MIB", "qBridgeLearningConstraintsGroup"), ("Q-BRIDGE-MIB", "qBridgeLearningConstraintDefaultGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeCompliance = qBridgeCompliance.setStatus('deprecated')
qBridgeCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 7, 2, 2, 2)).setObjects(("Q-BRIDGE-MIB", "qBridgeBaseGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanStaticGroup"), ("Q-BRIDGE-MIB", "qBridgePortGroup2"), ("Q-BRIDGE-MIB", "qBridgeFdbUnicastGroup"), ("Q-BRIDGE-MIB", "qBridgeFdbMulticastGroup"), ("Q-BRIDGE-MIB", "qBridgeServiceRequirementsGroup"), ("Q-BRIDGE-MIB", "qBridgeFdbStaticGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanStatisticsGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanStatisticsOverflowGroup"), ("Q-BRIDGE-MIB", "qBridgeVlanHCStatisticsGroup"), ("Q-BRIDGE-MIB", "qBridgeLearningConstraintsGroup"), ("Q-BRIDGE-MIB", "qBridgeLearningConstraintDefaultGroup"), ("Q-BRIDGE-MIB", "qBridgeClassificationDeviceGroup"), ("Q-BRIDGE-MIB", "qBridgeClassificationPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qBridgeCompliance2 = qBridgeCompliance2.setStatus('current')
mibBuilder.exportSymbols("Q-BRIDGE-MIB", qBridgeLearningConstraintDefaultGroup=qBridgeLearningConstraintDefaultGroup, dot1qVlanStaticEgressPorts=dot1qVlanStaticEgressPorts, dot1qVlanCreationTime=dot1qVlanCreationTime, VlanIdOrAny=VlanIdOrAny, qBridgeServiceRequirementsGroup=qBridgeServiceRequirementsGroup, dot1qConstraintTypeDefault=dot1qConstraintTypeDefault, qBridgeCompliance=qBridgeCompliance, dot1qPortAcceptableFrameTypes=dot1qPortAcceptableFrameTypes, dot1qStaticMulticastReceivePort=dot1qStaticMulticastReceivePort, qBridgeVlanGroup=qBridgeVlanGroup, dot1qTpFdbPort=dot1qTpFdbPort, dot1qStaticUnicastAllowedToGoTo=dot1qStaticUnicastAllowedToGoTo, dot1qVlanCurrentTable=dot1qVlanCurrentTable, dot1qForwardUnregisteredForbiddenPorts=dot1qForwardUnregisteredForbiddenPorts, dot1qStaticMulticastTable=dot1qStaticMulticastTable, dot1qTpGroupLearnt=dot1qTpGroupLearnt, qBridgeMIB=qBridgeMIB, dot1qForwardUnregisteredStaticPorts=dot1qForwardUnregisteredStaticPorts, dot1qPortGvrpLastPduOrigin=dot1qPortGvrpLastPduOrigin, VlanId=VlanId, dot1qPortGvrpFailedRegistrations=dot1qPortGvrpFailedRegistrations, dot1qFdbTable=dot1qFdbTable, dot1qTpFdbAddress=dot1qTpFdbAddress, VlanIdOrAnyOrNone=VlanIdOrAnyOrNone, dot1qPvid=dot1qPvid, dot1qForwardAllPorts=dot1qForwardAllPorts, dot1qForwardUnregisteredTable=dot1qForwardUnregisteredTable, dot1qTpFdbStatus=dot1qTpFdbStatus, dot1qConstraintSetDefault=dot1qConstraintSetDefault, dot1qStaticMulticastForbiddenEgressPorts=dot1qStaticMulticastForbiddenEgressPorts, qBridgeConformance=qBridgeConformance, dot1qVlanForbiddenEgressPorts=dot1qVlanForbiddenEgressPorts, qBridgeClassificationPortGroup=qBridgeClassificationPortGroup, dot1qPortVlanHCStatisticsTable=dot1qPortVlanHCStatisticsTable, dot1qPortVlanStatisticsTable=dot1qPortVlanStatisticsTable, qBridgeMIBObjects=qBridgeMIBObjects, dot1qMaxSupportedVlans=dot1qMaxSupportedVlans, dot1qPortIngressFiltering=dot1qPortIngressFiltering, dot1qTpVlanPortHCOutFrames=dot1qTpVlanPortHCOutFrames, dot1qForwardUnregisteredPorts=dot1qForwardUnregisteredPorts, qBridgeVlanStatisticsOverflowGroup=qBridgeVlanStatisticsOverflowGroup, dot1vProtocolPortEntry=dot1vProtocolPortEntry, dot1qVlanVersionNumber=dot1qVlanVersionNumber, dot1qBase=dot1qBase, dot1qPortVlanEntry=dot1qPortVlanEntry, dot1vProtocolPortRowStatus=dot1vProtocolPortRowStatus, dot1qForwardAllStaticPorts=dot1qForwardAllStaticPorts, dot1qTpVlanPortInDiscards=dot1qTpVlanPortInDiscards, qBridgeVlanHCStatisticsGroup=qBridgeVlanHCStatisticsGroup, dot1qStaticUnicastAddress=dot1qStaticUnicastAddress, qBridgeFdbMulticastGroup=qBridgeFdbMulticastGroup, qBridgeFdbUnicastGroup=qBridgeFdbUnicastGroup, dot1qFdbId=dot1qFdbId, dot1qVlanIndex=dot1qVlanIndex, dot1qVlanCurrentEntry=dot1qVlanCurrentEntry, qBridgeClassificationDeviceGroup=qBridgeClassificationDeviceGroup, dot1qTpGroupEgressPorts=dot1qTpGroupEgressPorts, dot1qVlanStaticName=dot1qVlanStaticName, dot1qVlanStatus=dot1qVlanStatus, dot1qPortVlanTable=dot1qPortVlanTable, dot1qTpVlanPortOutOverflowFrames=dot1qTpVlanPortOutOverflowFrames, dot1qPortGvrpStatus=dot1qPortGvrpStatus, dot1qConstraintType=dot1qConstraintType, dot1vProtocolGroupId=dot1vProtocolGroupId, dot1qStaticMulticastAddress=dot1qStaticMulticastAddress, dot1qForwardAllTable=dot1qForwardAllTable, dot1qFdbEntry=dot1qFdbEntry, qBridgeGroups=qBridgeGroups, dot1qTp=dot1qTp, dot1qTpVlanPortInFrames=dot1qTpVlanPortInFrames, qBridgeCompliances=qBridgeCompliances, VlanIndex=VlanIndex, qBridgeVlanStatisticsGroup=qBridgeVlanStatisticsGroup, dot1qPortRestrictedVlanRegistration=dot1qPortRestrictedVlanRegistration, dot1qVlanTimeMark=dot1qVlanTimeMark, VlanIdOrNone=VlanIdOrNone, dot1qFdbDynamicCount=dot1qFdbDynamicCount, dot1qStaticUnicastReceivePort=dot1qStaticUnicastReceivePort, dot1qVlanStaticEntry=dot1qVlanStaticEntry, dot1qForwardAllForbiddenPorts=dot1qForwardAllForbiddenPorts, dot1qConstraintSet=dot1qConstraintSet, dot1qMaxVlanId=dot1qMaxVlanId, dot1qTpGroupTable=dot1qTpGroupTable, dot1qForwardUnregisteredEntry=dot1qForwardUnregisteredEntry, qBridgeFdbStaticGroup=qBridgeFdbStaticGroup, qBridgeVlanStaticGroup=qBridgeVlanStaticGroup, dot1qStaticMulticastEntry=dot1qStaticMulticastEntry, PortList=PortList, dot1qStaticUnicastTable=dot1qStaticUnicastTable, dot1vProtocolPortGroupId=dot1vProtocolPortGroupId, dot1qStaticUnicastStatus=dot1qStaticUnicastStatus, dot1qStaticMulticastStatus=dot1qStaticMulticastStatus, dot1qVlanCurrentUntaggedPorts=dot1qVlanCurrentUntaggedPorts, dot1qNextFreeLocalVlanIndex=dot1qNextFreeLocalVlanIndex, qBridgeBaseGroup=qBridgeBaseGroup, dot1qLearningConstraintsEntry=dot1qLearningConstraintsEntry, dot1vProtocolTemplateProtocolValue=dot1vProtocolTemplateProtocolValue, dot1qStaticUnicastEntry=dot1qStaticUnicastEntry, dot1vProtocolGroupRowStatus=dot1vProtocolGroupRowStatus, dot1qGvrpStatus=dot1qGvrpStatus, dot1qNumVlans=dot1qNumVlans, qBridgeCompliance2=qBridgeCompliance2, dot1qLearningConstraintsTable=dot1qLearningConstraintsTable, dot1qConstraintVlan=dot1qConstraintVlan, dot1qPortVlanStatisticsEntry=dot1qPortVlanStatisticsEntry, dot1vProtocolTemplateFrameType=dot1vProtocolTemplateFrameType, dot1vProtocol=dot1vProtocol, dot1qStaticMulticastStaticEgressPorts=dot1qStaticMulticastStaticEgressPorts, dot1qVlan=dot1qVlan, dot1qVlanNumDeletes=dot1qVlanNumDeletes, qBridgeLearningConstraintsGroup=qBridgeLearningConstraintsGroup, dot1vProtocolGroupTable=dot1vProtocolGroupTable, dot1qTpVlanPortInOverflowFrames=dot1qTpVlanPortInOverflowFrames, dot1vProtocolPortTable=dot1vProtocolPortTable, dot1qVlanStaticRowStatus=dot1qVlanStaticRowStatus, dot1qVlanCurrentEgressPorts=dot1qVlanCurrentEgressPorts, dot1qConstraintStatus=dot1qConstraintStatus, dot1qPortVlanHCStatisticsEntry=dot1qPortVlanHCStatisticsEntry, dot1qTpVlanPortOutFrames=dot1qTpVlanPortOutFrames, dot1qTpGroupEntry=dot1qTpGroupEntry, dot1qForwardAllEntry=dot1qForwardAllEntry, PYSNMP_MODULE_ID=qBridgeMIB, dot1vProtocolPortGroupVid=dot1vProtocolPortGroupVid, dot1qVlanStaticUntaggedPorts=dot1qVlanStaticUntaggedPorts, dot1qTpFdbEntry=dot1qTpFdbEntry, qBridgePortGroup=qBridgePortGroup, dot1qTpGroupAddress=dot1qTpGroupAddress, dot1qTpVlanPortHCInDiscards=dot1qTpVlanPortHCInDiscards, dot1qTpVlanPortHCInFrames=dot1qTpVlanPortHCInFrames, dot1qVlanFdbId=dot1qVlanFdbId, dot1qVlanStaticTable=dot1qVlanStaticTable, dot1qStatic=dot1qStatic, dot1qTpFdbTable=dot1qTpFdbTable, dot1qTpVlanPortInOverflowDiscards=dot1qTpVlanPortInOverflowDiscards, qBridgePortGroup2=qBridgePortGroup2, dot1vProtocolGroupEntry=dot1vProtocolGroupEntry)
