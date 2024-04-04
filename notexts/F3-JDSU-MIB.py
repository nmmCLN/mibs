#
# PySNMP MIB module F3-JDSU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-JDSU-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:27 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
VlanPriority, VlanId, SecondaryState, AdminState, OperationalState = mibBuilder.importSymbols("CM-COMMON-MIB", "VlanPriority", "VlanId", "SecondaryState", "AdminState", "OperationalState")
shelfIndex, slotIndex, neIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "shelfIndex", "slotIndex", "neIndex")
cmEthernetTrafficPortEntry, cmEthernetTrafficPortIndex = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmEthernetTrafficPortEntry", "cmEthernetTrafficPortIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, iso, Gauge32, MibIdentifier, ModuleIdentity, ObjectIdentity, Counter64, Counter32, IpAddress, Unsigned32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "iso", "Gauge32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Counter64", "Counter32", "IpAddress", "Unsigned32", "Integer32", "Bits")
MacAddress, RowStatus, DateAndTime, DisplayString, TruthValue, TextualConvention, StorageType, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "DateAndTime", "DisplayString", "TruthValue", "TextualConvention", "StorageType", "VariablePointer")
f3JdsuMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31))
f3JdsuMIB.setRevisions(('2014-01-02 00:00',))
if mibBuilder.loadTexts: f3JdsuMIB.setLastUpdated('201401020000Z')
if mibBuilder.loadTexts: f3JdsuMIB.setOrganization('ADVA Optical Networking')
f3JdsuObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1))
f3JdsuNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 2))
f3JdsuConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3))
class GeneratorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("none", 1), ("initial", 2), ("helloIngress", 3), ("helloCompleted", 4), ("helloFailed", 5), ("lookupIngress", 6), ("lookupCompleted", 7), ("lookupFailed", 8), ("lookdownIngress", 9), ("lookdownCompleted", 10), ("lookdownFailed", 11))

class ItemOperation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notApplicable", 1), ("save", 2))

class UpdateReachStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notApplicable", 1), ("update", 2))

class JdsuGeneratorFrameType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("frameType8023", 2))

class JdsuGeneratorPayloadType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("fixed", 2), ("random", 3))

class GeneratorAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notApplicable", 1), ("loopUp", 2), ("loopDown", 3))

class DiscoveryAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notApplicable", 1), ("discover", 2))

f3JdsuGeneratorPort = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 1), VariablePointer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorPort.setStatus('current')
f3JdsuGeneratorOuterVlanEnabled = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorOuterVlanEnabled.setStatus('current')
f3JdsuGeneratorOuterVlanId = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 3), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorOuterVlanId.setStatus('current')
f3JdsuGeneratorOuterVlanPri = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 4), VlanPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorOuterVlanPri.setStatus('current')
f3JdsuGeneratorOuterVlanEtherType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorOuterVlanEtherType.setStatus('current')
f3JdsuGeneratorInnerVlan1Enabled = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorInnerVlan1Enabled.setStatus('current')
f3JdsuGeneratorInnerVlan1Id = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 7), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorInnerVlan1Id.setStatus('current')
f3JdsuGeneratorInnerVlan1Pri = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 8), VlanPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorInnerVlan1Pri.setStatus('current')
f3JdsuGeneratorInnerVlan1EtherType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorInnerVlan1EtherType.setStatus('current')
f3JdsuGeneratorInnerVlan2Enabled = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorInnerVlan2Enabled.setStatus('current')
f3JdsuGeneratorInnerVlan2Id = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 11), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorInnerVlan2Id.setStatus('current')
f3JdsuGeneratorInnerVlan2Pri = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 12), VlanPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorInnerVlan2Pri.setStatus('current')
f3JdsuGeneratorInnerVlan2EtherType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 13), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorInnerVlan2EtherType.setStatus('current')
f3JdsuGeneratorFrameType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 14), JdsuGeneratorFrameType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorFrameType.setStatus('current')
f3JdsuGeneratorPayloadType = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 15), JdsuGeneratorPayloadType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorPayloadType.setStatus('current')
f3JdsuGeneratorFrameLength = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorFrameLength.setStatus('current')
f3JdsuGeneratorDiscoveryAction = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 17), DiscoveryAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoveryAction.setStatus('current')
f3JdsuGeneratorDiscoverTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18), )
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverTable.setStatus('current')
f3JdsuGeneratorDiscoverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"), (0, "F3-JDSU-MIB", "f3JdsuGeneratorDiscoverDestMacAddr"))
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverEntry.setStatus('current')
f3JdsuGeneratorDiscoverDestMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 1), MacAddress())
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverDestMacAddr.setStatus('current')
f3JdsuGeneratorDiscoverOuterVlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverOuterVlanEnabled.setStatus('current')
f3JdsuGeneratorDiscoverOuterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 3), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverOuterVlanId.setStatus('current')
f3JdsuGeneratorDiscoverOuterVlanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 4), VlanPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverOuterVlanPri.setStatus('current')
f3JdsuGeneratorDiscoverOuterVlanEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverOuterVlanEtherType.setStatus('current')
f3JdsuGeneratorDiscoverInnerVlan1Enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverInnerVlan1Enabled.setStatus('current')
f3JdsuGeneratorDiscoverInnerVlan1Id = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 7), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverInnerVlan1Id.setStatus('current')
f3JdsuGeneratorDiscoverInnerVlan1Pri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 8), VlanPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverInnerVlan1Pri.setStatus('current')
f3JdsuGeneratorDiscoverInnerVlan1EtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverInnerVlan1EtherType.setStatus('current')
f3JdsuGeneratorDiscoverInnerVlan2Enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverInnerVlan2Enabled.setStatus('current')
f3JdsuGeneratorDiscoverInnerVlan2Id = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 11), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverInnerVlan2Id.setStatus('current')
f3JdsuGeneratorDiscoverInnerVlan2Pri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 12), VlanPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverInnerVlan2Pri.setStatus('current')
f3JdsuGeneratorDiscoverInnerVlan2EtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverInnerVlan2EtherType.setStatus('current')
f3JdsuGeneratorDiscoverFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 14), JdsuGeneratorFrameType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverFrameType.setStatus('current')
f3JdsuGeneratorDiscoverPayloadType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 15), JdsuGeneratorPayloadType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverPayloadType.setStatus('current')
f3JdsuGeneratorDiscoverFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverFrameLength.setStatus('current')
f3JdsuGeneratorDiscoverUnitTextId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverUnitTextId.setStatus('current')
f3JdsuGeneratorDiscoverIfReachable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverIfReachable.setStatus('current')
f3JdsuGeneratorDiscoverGeneratorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 19), GeneratorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverGeneratorStatus.setStatus('current')
f3JdsuGeneratorDiscoverItemOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 20), ItemOperation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverItemOperation.setStatus('current')
f3JdsuGeneratorDiscoverItemIfSaved = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 21), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverItemIfSaved.setStatus('current')
f3JdsuGeneratorDiscoverGeneratorAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 18, 1, 22), GeneratorAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorDiscoverGeneratorAction.setStatus('current')
f3JdsuGeneratorConfigureTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19), )
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureTable.setStatus('current')
f3JdsuGeneratorConfigureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"), (0, "F3-JDSU-MIB", "f3JdsuGeneratorConfigureDestMacAddr"))
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureEntry.setStatus('current')
f3JdsuGeneratorConfigureDestMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 1), MacAddress())
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureDestMacAddr.setStatus('current')
f3JdsuGeneratorConfigureOuterVlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureOuterVlanEnabled.setStatus('current')
f3JdsuGeneratorConfigureOuterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 3), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureOuterVlanId.setStatus('current')
f3JdsuGeneratorConfigureOuterVlanPri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 4), VlanPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureOuterVlanPri.setStatus('current')
f3JdsuGeneratorConfigureOuterVlanEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureOuterVlanEtherType.setStatus('current')
f3JdsuGeneratorConfigureInnerVlan1Enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureInnerVlan1Enabled.setStatus('current')
f3JdsuGeneratorConfigureInnerVlan1Id = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 7), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureInnerVlan1Id.setStatus('current')
f3JdsuGeneratorConfigureInnerVlan1Pri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 8), VlanPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureInnerVlan1Pri.setStatus('current')
f3JdsuGeneratorConfigureInnerVlan1EtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureInnerVlan1EtherType.setStatus('current')
f3JdsuGeneratorConfigureInnerVlan2Enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureInnerVlan2Enabled.setStatus('current')
f3JdsuGeneratorConfigureInnerVlan2Id = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 11), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureInnerVlan2Id.setStatus('current')
f3JdsuGeneratorConfigureInnerVlan2Pri = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 12), VlanPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureInnerVlan2Pri.setStatus('current')
f3JdsuGeneratorConfigureInnerVlan2EtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureInnerVlan2EtherType.setStatus('current')
f3JdsuGeneratorConfigureFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 14), JdsuGeneratorFrameType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureFrameType.setStatus('current')
f3JdsuGeneratorConfigurePayloadType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 15), JdsuGeneratorPayloadType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigurePayloadType.setStatus('current')
f3JdsuGeneratorConfigureFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureFrameLength.setStatus('current')
f3JdsuGeneratorConfigureUnitTextId = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureUnitTextId.setStatus('current')
f3JdsuGeneratorConfigureIfReachable = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureIfReachable.setStatus('current')
f3JdsuGeneratorConfigureReachableUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 19), UpdateReachStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureReachableUpdate.setStatus('current')
f3JdsuGeneratorConfigureStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 20), GeneratorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureStatus.setStatus('current')
f3JdsuGeneratorConfigureGeneratorAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 21), GeneratorAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureGeneratorAction.setStatus('current')
f3JdsuGeneratorConfigureStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 22), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureStorageType.setStatus('current')
f3JdsuGeneratorConfigureRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 19, 1, 23), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: f3JdsuGeneratorConfigureRowStatus.setStatus('current')
f3EthernetTrafficPortJdsuExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20), )
if mibBuilder.loadTexts: f3EthernetTrafficPortJdsuExtTable.setStatus('current')
f3EthernetTrafficPortJdsuExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20, 1), )
cmEthernetTrafficPortEntry.registerAugmentions(("F3-JDSU-MIB", "f3EthernetTrafficPortJdsuExtEntry"))
f3EthernetTrafficPortJdsuExtEntry.setIndexNames(*cmEthernetTrafficPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3EthernetTrafficPortJdsuExtEntry.setStatus('current')
f3EthernetTrafficPortJdsuLoopbackEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EthernetTrafficPortJdsuLoopbackEnabled.setStatus('current')
f3EthernetTrafficPortJdsuGenerationEanbled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3EthernetTrafficPortJdsuGenerationEanbled.setStatus('current')
f3EthernetTrafficPortJdsuLoopbackVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 1, 20, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3EthernetTrafficPortJdsuLoopbackVlanList.setStatus('current')
f3JdsuCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3, 1))
f3JdsuGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3, 2))
f3JdsuCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3, 1, 1)).setObjects(("F3-JDSU-MIB", "f3JdsuGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuCompliance = f3JdsuCompliance.setStatus('current')
f3JdsuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 31, 3, 2, 1)).setObjects(("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverDestMacAddr"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverOuterVlanEnabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverOuterVlanId"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverOuterVlanPri"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverOuterVlanEtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan1Enabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan1Id"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan1Pri"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan1EtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan2Enabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan2Id"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan2Pri"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverInnerVlan2EtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverFrameType"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverPayloadType"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverFrameLength"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverUnitTextId"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverIfReachable"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverGeneratorStatus"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverItemOperation"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverItemIfSaved"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoverGeneratorAction"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureDestMacAddr"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureOuterVlanEnabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureOuterVlanId"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureOuterVlanPri"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureOuterVlanEtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan1Enabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan1Id"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan1Pri"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan1EtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan2Enabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan2Id"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan2Pri"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureInnerVlan2EtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureFrameType"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigurePayloadType"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureFrameLength"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureUnitTextId"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureIfReachable"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureReachableUpdate"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureStatus"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureGeneratorAction"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureStorageType"), ("F3-JDSU-MIB", "f3JdsuGeneratorConfigureRowStatus"), ("F3-JDSU-MIB", "f3EthernetTrafficPortJdsuLoopbackEnabled"), ("F3-JDSU-MIB", "f3EthernetTrafficPortJdsuGenerationEanbled"), ("F3-JDSU-MIB", "f3EthernetTrafficPortJdsuLoopbackVlanList"), ("F3-JDSU-MIB", "f3JdsuGeneratorPort"), ("F3-JDSU-MIB", "f3JdsuGeneratorOuterVlanEnabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorOuterVlanId"), ("F3-JDSU-MIB", "f3JdsuGeneratorOuterVlanPri"), ("F3-JDSU-MIB", "f3JdsuGeneratorOuterVlanEtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan1Enabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan1Id"), ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan1Pri"), ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan1EtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan2Enabled"), ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan2Id"), ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan2Pri"), ("F3-JDSU-MIB", "f3JdsuGeneratorInnerVlan2EtherType"), ("F3-JDSU-MIB", "f3JdsuGeneratorFrameType"), ("F3-JDSU-MIB", "f3JdsuGeneratorPayloadType"), ("F3-JDSU-MIB", "f3JdsuGeneratorFrameLength"), ("F3-JDSU-MIB", "f3JdsuGeneratorDiscoveryAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3JdsuGroup = f3JdsuGroup.setStatus('current')
mibBuilder.exportSymbols("F3-JDSU-MIB", f3JdsuGeneratorOuterVlanEnabled=f3JdsuGeneratorOuterVlanEnabled, f3JdsuCompliance=f3JdsuCompliance, f3JdsuGeneratorConfigureUnitTextId=f3JdsuGeneratorConfigureUnitTextId, f3JdsuGeneratorDiscoverOuterVlanEnabled=f3JdsuGeneratorDiscoverOuterVlanEnabled, f3EthernetTrafficPortJdsuExtTable=f3EthernetTrafficPortJdsuExtTable, f3JdsuGeneratorConfigureDestMacAddr=f3JdsuGeneratorConfigureDestMacAddr, f3JdsuGeneratorConfigureOuterVlanEnabled=f3JdsuGeneratorConfigureOuterVlanEnabled, f3JdsuGeneratorConfigureEntry=f3JdsuGeneratorConfigureEntry, f3JdsuGeneratorOuterVlanPri=f3JdsuGeneratorOuterVlanPri, f3JdsuGeneratorConfigureStatus=f3JdsuGeneratorConfigureStatus, f3JdsuGeneratorConfigureFrameLength=f3JdsuGeneratorConfigureFrameLength, f3JdsuGeneratorDiscoverIfReachable=f3JdsuGeneratorDiscoverIfReachable, f3JdsuGeneratorInnerVlan1EtherType=f3JdsuGeneratorInnerVlan1EtherType, f3JdsuGeneratorDiscoverInnerVlan1EtherType=f3JdsuGeneratorDiscoverInnerVlan1EtherType, f3JdsuGeneratorConfigureInnerVlan1Id=f3JdsuGeneratorConfigureInnerVlan1Id, f3JdsuGeneratorOuterVlanId=f3JdsuGeneratorOuterVlanId, f3JdsuGeneratorInnerVlan1Enabled=f3JdsuGeneratorInnerVlan1Enabled, f3JdsuGeneratorConfigurePayloadType=f3JdsuGeneratorConfigurePayloadType, DiscoveryAction=DiscoveryAction, f3JdsuGroup=f3JdsuGroup, f3EthernetTrafficPortJdsuLoopbackEnabled=f3EthernetTrafficPortJdsuLoopbackEnabled, f3JdsuGroups=f3JdsuGroups, f3JdsuGeneratorDiscoverUnitTextId=f3JdsuGeneratorDiscoverUnitTextId, f3JdsuGeneratorConfigureInnerVlan2Id=f3JdsuGeneratorConfigureInnerVlan2Id, f3JdsuGeneratorDiscoverDestMacAddr=f3JdsuGeneratorDiscoverDestMacAddr, f3JdsuGeneratorConfigureInnerVlan1EtherType=f3JdsuGeneratorConfigureInnerVlan1EtherType, f3JdsuGeneratorFrameLength=f3JdsuGeneratorFrameLength, f3JdsuGeneratorDiscoverPayloadType=f3JdsuGeneratorDiscoverPayloadType, f3JdsuGeneratorConfigureOuterVlanPri=f3JdsuGeneratorConfigureOuterVlanPri, f3EthernetTrafficPortJdsuExtEntry=f3EthernetTrafficPortJdsuExtEntry, f3EthernetTrafficPortJdsuLoopbackVlanList=f3EthernetTrafficPortJdsuLoopbackVlanList, UpdateReachStatus=UpdateReachStatus, f3JdsuGeneratorConfigureInnerVlan2EtherType=f3JdsuGeneratorConfigureInnerVlan2EtherType, f3JdsuGeneratorConfigureGeneratorAction=f3JdsuGeneratorConfigureGeneratorAction, JdsuGeneratorFrameType=JdsuGeneratorFrameType, f3JdsuGeneratorDiscoverGeneratorStatus=f3JdsuGeneratorDiscoverGeneratorStatus, f3JdsuNotifications=f3JdsuNotifications, f3JdsuGeneratorDiscoverOuterVlanId=f3JdsuGeneratorDiscoverOuterVlanId, f3JdsuGeneratorInnerVlan2Pri=f3JdsuGeneratorInnerVlan2Pri, f3JdsuObjects=f3JdsuObjects, f3JdsuGeneratorDiscoverOuterVlanEtherType=f3JdsuGeneratorDiscoverOuterVlanEtherType, f3JdsuGeneratorInnerVlan2EtherType=f3JdsuGeneratorInnerVlan2EtherType, PYSNMP_MODULE_ID=f3JdsuMIB, f3JdsuGeneratorFrameType=f3JdsuGeneratorFrameType, f3JdsuGeneratorPayloadType=f3JdsuGeneratorPayloadType, f3JdsuGeneratorInnerVlan1Id=f3JdsuGeneratorInnerVlan1Id, f3JdsuGeneratorInnerVlan2Enabled=f3JdsuGeneratorInnerVlan2Enabled, f3JdsuGeneratorConfigureOuterVlanId=f3JdsuGeneratorConfigureOuterVlanId, f3JdsuGeneratorDiscoverInnerVlan1Pri=f3JdsuGeneratorDiscoverInnerVlan1Pri, f3JdsuGeneratorDiscoverItemIfSaved=f3JdsuGeneratorDiscoverItemIfSaved, f3JdsuGeneratorConfigureRowStatus=f3JdsuGeneratorConfigureRowStatus, f3JdsuGeneratorDiscoverInnerVlan2Pri=f3JdsuGeneratorDiscoverInnerVlan2Pri, GeneratorStatus=GeneratorStatus, f3JdsuGeneratorConfigureInnerVlan2Enabled=f3JdsuGeneratorConfigureInnerVlan2Enabled, f3JdsuGeneratorConfigureOuterVlanEtherType=f3JdsuGeneratorConfigureOuterVlanEtherType, f3JdsuGeneratorConfigureInnerVlan2Pri=f3JdsuGeneratorConfigureInnerVlan2Pri, f3JdsuGeneratorDiscoverInnerVlan1Id=f3JdsuGeneratorDiscoverInnerVlan1Id, JdsuGeneratorPayloadType=JdsuGeneratorPayloadType, f3JdsuGeneratorOuterVlanEtherType=f3JdsuGeneratorOuterVlanEtherType, f3JdsuGeneratorInnerVlan2Id=f3JdsuGeneratorInnerVlan2Id, GeneratorAction=GeneratorAction, f3JdsuGeneratorConfigureInnerVlan1Pri=f3JdsuGeneratorConfigureInnerVlan1Pri, f3JdsuGeneratorDiscoverGeneratorAction=f3JdsuGeneratorDiscoverGeneratorAction, f3JdsuGeneratorDiscoverTable=f3JdsuGeneratorDiscoverTable, f3EthernetTrafficPortJdsuGenerationEanbled=f3EthernetTrafficPortJdsuGenerationEanbled, f3JdsuMIB=f3JdsuMIB, f3JdsuGeneratorConfigureReachableUpdate=f3JdsuGeneratorConfigureReachableUpdate, f3JdsuGeneratorConfigureIfReachable=f3JdsuGeneratorConfigureIfReachable, f3JdsuGeneratorDiscoverInnerVlan2Enabled=f3JdsuGeneratorDiscoverInnerVlan2Enabled, f3JdsuGeneratorDiscoverInnerVlan2EtherType=f3JdsuGeneratorDiscoverInnerVlan2EtherType, f3JdsuGeneratorDiscoverInnerVlan2Id=f3JdsuGeneratorDiscoverInnerVlan2Id, f3JdsuGeneratorConfigureFrameType=f3JdsuGeneratorConfigureFrameType, f3JdsuGeneratorDiscoverInnerVlan1Enabled=f3JdsuGeneratorDiscoverInnerVlan1Enabled, f3JdsuGeneratorDiscoveryAction=f3JdsuGeneratorDiscoveryAction, ItemOperation=ItemOperation, f3JdsuGeneratorDiscoverEntry=f3JdsuGeneratorDiscoverEntry, f3JdsuGeneratorDiscoverFrameType=f3JdsuGeneratorDiscoverFrameType, f3JdsuGeneratorConfigureInnerVlan1Enabled=f3JdsuGeneratorConfigureInnerVlan1Enabled, f3JdsuGeneratorConfigureStorageType=f3JdsuGeneratorConfigureStorageType, f3JdsuGeneratorPort=f3JdsuGeneratorPort, f3JdsuGeneratorInnerVlan1Pri=f3JdsuGeneratorInnerVlan1Pri, f3JdsuConformance=f3JdsuConformance, f3JdsuGeneratorDiscoverOuterVlanPri=f3JdsuGeneratorDiscoverOuterVlanPri, f3JdsuGeneratorConfigureTable=f3JdsuGeneratorConfigureTable, f3JdsuGeneratorDiscoverItemOperation=f3JdsuGeneratorDiscoverItemOperation, f3JdsuCompliances=f3JdsuCompliances, f3JdsuGeneratorDiscoverFrameLength=f3JdsuGeneratorDiscoverFrameLength)
