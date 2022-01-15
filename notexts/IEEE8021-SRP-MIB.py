#
# PySNMP MIB module IEEE8021-SRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-SRP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ieee8021BridgeBaseComponentId, ieee8021BridgeBasePort, ieee8021BridgeBaseEntry, ieee8021BridgeBasePortEntry = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId", "ieee8021BridgeBasePort", "ieee8021BridgeBaseEntry", "ieee8021BridgeBasePortEntry")
IEEE8021FqtssTrafficClassValue, = mibBuilder.importSymbols("IEEE8021-FQTSS-MIB", "IEEE8021FqtssTrafficClassValue")
IEEE8021PriorityCodePoint, ieee802dot1mibs, IEEE8021VlanIndex = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PriorityCodePoint", "ieee802dot1mibs", "IEEE8021VlanIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention")
ieee8021SrpMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 19))
ieee8021SrpMib.setRevisions(('2018-10-04 00:00', '2018-06-28 00:00', '2015-12-02 00:00', '2014-12-15 00:00', '2011-02-27 00:00', '2010-04-19 00:00',))
if mibBuilder.loadTexts: ieee8021SrpMib.setLastUpdated('201810040000Z')
if mibBuilder.loadTexts: ieee8021SrpMib.setOrganization('IEEE 802.1 Working Group')
class IEEE8021SrpStreamRankValue(TextualConvention, Integer32):
    reference = '35.2.2.8.5b'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("emergency", 0), ("nonEmergency", 1))

class IEEE8021SrpStreamIdValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:1x:1x:1x:1x:1x.1x:1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class IEEE8021SrpReservationDirectionValue(TextualConvention, Integer32):
    reference = '35.2.1.2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("talkerRegistrations", 0), ("listenerRegistrations", 1))

class IEEE8021SrpReservationDeclarationTypeValue(TextualConvention, Integer32):
    reference = '35.2.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("talkerAdvertise", 0), ("talkerFailed", 1), ("listenerAskingFailed", 2), ("listenerReady", 3), ("listenerReadyFailed", 4))

class IEEE8021SrpReservationFailureCodeValue(TextualConvention, Integer32):
    reference = '35.2.2.8.7'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("noFailure", 0), ("insufficientBandwidth", 1), ("insufficientResources", 2), ("insufficientTrafficClassBandwidth", 3), ("streamIDInUse", 4), ("streamDestinationAddressInUse", 5), ("streamPreemptedByHigherRank", 6), ("latencyHasChanged", 7), ("egressPortNotAVBCapable", 8), ("useDifferentDestinationAddress", 9), ("outOfMSRPResources", 10), ("outOfMMRPResources", 11), ("cannotStoreDestinationAddress", 12), ("priorityIsNoAnSRCLass", 13), ("maxFrameSizeTooLarge", 14), ("maxFanInPortsLimitReached", 15), ("firstValueChangedForStreamID", 16), ("vlanBlockedOnEgress", 17), ("vlanTaggingDisabledOnEgress", 18), ("srClassPriorityMismatch", 19))

ieee8021SrpNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 0))
ieee8021SrpObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 1))
ieee8021SrpConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 2))
ieee8021SrpConfiguration = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 1, 1))
ieee8021SrpLatency = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 1, 2))
ieee8021SrpStreams = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 1, 3))
ieee8021SrpReservations = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 1, 4))
ieee8021SrpBridgeBaseTable = MibTable((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021SrpBridgeBaseTable.setStatus('current')
ieee8021SrpBridgeBaseEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1), )
ieee8021BridgeBaseEntry.registerAugmentions(("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseEntry"))
ieee8021SrpBridgeBaseEntry.setIndexNames(*ieee8021BridgeBaseEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021SrpBridgeBaseEntry.setStatus('current')
ieee8021SrpBridgeBaseMsrpEnabledStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SrpBridgeBaseMsrpEnabledStatus.setStatus('current')
ieee8021SrpBridgeBaseMsrpTalkerPruning = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SrpBridgeBaseMsrpTalkerPruning.setStatus('current')
ieee8021SrpBridgeBaseMsrpMaxFanInPorts = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SrpBridgeBaseMsrpMaxFanInPorts.setStatus('current')
ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 4), Unsigned32().clone(2000)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize.setStatus('current')
ieee8021SrpBridgeBaseMsrpTalkerVlanPruning = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SrpBridgeBaseMsrpTalkerVlanPruning.setStatus('current')
ieee8021SrpBridgeBaseMsrpMaxSRClasses = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpBridgeBaseMsrpMaxSRClasses.setStatus('current')
ieee8021SrpBridgePortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2), )
if mibBuilder.loadTexts: ieee8021SrpBridgePortTable.setStatus('current')
ieee8021SrpBridgePortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1), )
ieee8021BridgeBasePortEntry.registerAugmentions(("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortEntry"))
ieee8021SrpBridgePortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021SrpBridgePortEntry.setStatus('current')
ieee8021SrpBridgePortMsrpEnabledStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SrpBridgePortMsrpEnabledStatus.setStatus('current')
ieee8021SrpBridgePortMsrpFailedRegistrations = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 2), Counter64()).setUnits('failed MSRP registrations').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpBridgePortMsrpFailedRegistrations.setStatus('current')
ieee8021SrpBridgePortMsrpLastPduOrigin = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpBridgePortMsrpLastPduOrigin.setStatus('current')
ieee8021SrpBridgePortSrPvid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 4), IEEE8021VlanIndex().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SrpBridgePortSrPvid.setStatus('current')
ieee8021SrpBridgePortMsrpTalkerPrunningPerPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021SrpBridgePortMsrpTalkerPrunningPerPort.setStatus('current')
ieee8021SrpLatencyTable = MibTable((1, 3, 111, 2, 802, 1, 1, 19, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021SrpLatencyTable.setStatus('current')
ieee8021SrpLatencyEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 19, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-SRP-MIB", "ieee8021SrpTrafficClass"))
if mibBuilder.loadTexts: ieee8021SrpLatencyEntry.setStatus('current')
ieee8021SrpTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 2, 1, 1, 1), IEEE8021FqtssTrafficClassValue())
if mibBuilder.loadTexts: ieee8021SrpTrafficClass.setStatus('current')
ieee8021SrpPortTcLatency = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 2, 1, 1, 2), Unsigned32()).setUnits('nano-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpPortTcLatency.setStatus('current')
ieee8021SrpStreamTable = MibTable((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1), )
if mibBuilder.loadTexts: ieee8021SrpStreamTable.setStatus('current')
ieee8021SrpStreamEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1), ).setIndexNames((0, "IEEE8021-SRP-MIB", "ieee8021SrpStreamId"))
if mibBuilder.loadTexts: ieee8021SrpStreamEntry.setStatus('current')
ieee8021SrpStreamId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 1), IEEE8021SrpStreamIdValue())
if mibBuilder.loadTexts: ieee8021SrpStreamId.setStatus('current')
ieee8021SrpStreamDestinationAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpStreamDestinationAddress.setStatus('current')
ieee8021SrpStreamVlanId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 3), IEEE8021VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpStreamVlanId.setStatus('current')
ieee8021SrpStreamTspecMaxFrameSize = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpStreamTspecMaxFrameSize.setStatus('current')
ieee8021SrpStreamTspecMaxIntervalFrames = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpStreamTspecMaxIntervalFrames.setStatus('current')
ieee8021SrpStreamDataFramePriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 6), IEEE8021PriorityCodePoint()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpStreamDataFramePriority.setStatus('current')
ieee8021SrpStreamRank = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 7), IEEE8021SrpStreamRankValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpStreamRank.setStatus('current')
ieee8021SrpStreamPreloadTable = MibTable((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2), )
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadTable.setStatus('current')
ieee8021SrpStreamPreloadEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1), ).setIndexNames((0, "IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadId"))
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadEntry.setStatus('current')
ieee8021SrpStreamPreloadId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 1), IEEE8021SrpStreamIdValue())
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadId.setStatus('current')
ieee8021SrpStreamPreloadDestinationAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadDestinationAddress.setStatus('current')
ieee8021SrpStreamPreloadVlanId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 3), IEEE8021VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadVlanId.setStatus('current')
ieee8021SrpStreamPreloadTspecMaxFrameSize = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadTspecMaxFrameSize.setStatus('current')
ieee8021SrpStreamPreloadTspecMaxIntervalFrames = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadTspecMaxIntervalFrames.setStatus('current')
ieee8021SrpStreamPreloadDataFramePriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 6), IEEE8021PriorityCodePoint()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadDataFramePriority.setStatus('current')
ieee8021SrpStreamPreloadRank = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 7), IEEE8021SrpStreamRankValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SrpStreamPreloadRank.setStatus('current')
ieee8021SrpReservationsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1), )
if mibBuilder.loadTexts: ieee8021SrpReservationsTable.setStatus('current')
ieee8021SrpReservationsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1), ).setIndexNames((0, "IEEE8021-SRP-MIB", "ieee8021SrpReservationStreamId"), (0, "IEEE8021-SRP-MIB", "ieee8021SrpReservationDirection"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021SrpReservationsEntry.setStatus('current')
ieee8021SrpReservationStreamId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 1), IEEE8021SrpStreamIdValue())
if mibBuilder.loadTexts: ieee8021SrpReservationStreamId.setStatus('current')
ieee8021SrpReservationDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 2), IEEE8021SrpReservationDirectionValue())
if mibBuilder.loadTexts: ieee8021SrpReservationDirection.setStatus('current')
ieee8021SrpReservationDeclarationType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 3), IEEE8021SrpReservationDeclarationTypeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpReservationDeclarationType.setStatus('current')
ieee8021SrpReservationAccumulatedLatency = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 4), Unsigned32()).setUnits('nano-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpReservationAccumulatedLatency.setStatus('current')
ieee8021SrpReservationFailureSystemId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpReservationFailureSystemId.setStatus('current')
ieee8021SrpReservationFailureCode = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 6), IEEE8021SrpReservationFailureCodeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpReservationFailureCode.setStatus('current')
ieee8021SrpReservationDroppedStreamFrames = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 7), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpReservationDroppedStreamFrames.setStatus('current')
ieee8021SrpReservationStreamAge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021SrpReservationStreamAge.setStatus('current')
ieee8021SrpReservationsPreloadTable = MibTable((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2), )
if mibBuilder.loadTexts: ieee8021SrpReservationsPreloadTable.setStatus('current')
ieee8021SrpReservationsPreloadEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2, 1), ).setIndexNames((0, "IEEE8021-SRP-MIB", "ieee8021SrpReservationsPreloadStreamId"), (0, "IEEE8021-SRP-MIB", "ieee8021SrpReservationPreloadDirection"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021SrpReservationsPreloadEntry.setStatus('current')
ieee8021SrpReservationsPreloadStreamId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2, 1, 1), IEEE8021SrpStreamIdValue())
if mibBuilder.loadTexts: ieee8021SrpReservationsPreloadStreamId.setStatus('current')
ieee8021SrpReservationPreloadDirection = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2, 1, 2), IEEE8021SrpReservationDirectionValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SrpReservationPreloadDirection.setStatus('current')
ieee8021SrpReservationPreloadAccumulatedLatency = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2, 1, 3), Unsigned32()).setUnits('nano-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021SrpReservationPreloadAccumulatedLatency.setStatus('current')
ieee8021SrpCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 2, 1))
ieee8021SrpGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 19, 2, 2))
ieee8021SrpConfigurationGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 1)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpEnabledStatus"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpTalkerPruning"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpMaxFanInPorts"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpTalkerVlanPruning"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpMaxSRClasses"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpEnabledStatus"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpFailedRegistrations"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpLastPduOrigin"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortSrPvid"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpTalkerPrunningPerPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpConfigurationGroup = ieee8021SrpConfigurationGroup.setStatus('current')
ieee8021SrpLatencyGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 2)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpPortTcLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpLatencyGroup = ieee8021SrpLatencyGroup.setStatus('current')
ieee8021SrpStreamsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 3)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpStreamDestinationAddress"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamVlanId"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamTspecMaxFrameSize"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamTspecMaxIntervalFrames"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamDataFramePriority"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamRank"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpStreamsGroup = ieee8021SrpStreamsGroup.setStatus('current')
ieee8021SrpReservationsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 4)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpReservationDeclarationType"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationAccumulatedLatency"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationFailureSystemId"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationFailureCode"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationDroppedStreamFrames"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationStreamAge"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpReservationsGroup = ieee8021SrpReservationsGroup.setStatus('current')
ieee8021SrpConfigurationPruningGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 5)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpTalkerVlanPruning"), ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpTalkerPrunningPerPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpConfigurationPruningGroup = ieee8021SrpConfigurationPruningGroup.setStatus('current')
ieee8021SrpMonitoringSRclassesGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 6)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpMaxSRClasses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpMonitoringSRclassesGroup = ieee8021SrpMonitoringSRclassesGroup.setStatus('current')
ieee8021SrpStreamsPreloadGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 7)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadId"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadDestinationAddress"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadVlanId"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadTspecMaxFrameSize"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadTspecMaxIntervalFrames"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadDataFramePriority"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadRank"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpStreamsPreloadGroup = ieee8021SrpStreamsPreloadGroup.setStatus('current')
ieee8021SrpReservationsPreloadGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 8)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpReservationsPreloadStreamId"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationPreloadDirection"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationPreloadAccumulatedLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpReservationsPreloadGroup = ieee8021SrpReservationsPreloadGroup.setStatus('current')
ieee8021SrpCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 19, 2, 1, 1)).setObjects(("IEEE8021-SRP-MIB", "ieee8021SrpConfigurationGroup"), ("IEEE8021-SRP-MIB", "ieee8021SrpLatencyGroup"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamsGroup"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationsGroup"), ("IEEE8021-SRP-MIB", "ieee8021SrpConfigurationPruningGroup"), ("IEEE8021-SRP-MIB", "ieee8021SrpMonitoringSRclassesGroup"), ("IEEE8021-SRP-MIB", "ieee8021SrpStreamsPreloadGroup"), ("IEEE8021-SRP-MIB", "ieee8021SrpReservationsPreloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021SrpCompliance = ieee8021SrpCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-SRP-MIB", ieee8021SrpBridgeBaseMsrpMaxFanInPorts=ieee8021SrpBridgeBaseMsrpMaxFanInPorts, ieee8021SrpBridgePortMsrpEnabledStatus=ieee8021SrpBridgePortMsrpEnabledStatus, ieee8021SrpStreamId=ieee8021SrpStreamId, ieee8021SrpReservationAccumulatedLatency=ieee8021SrpReservationAccumulatedLatency, ieee8021SrpBridgePortMsrpTalkerPrunningPerPort=ieee8021SrpBridgePortMsrpTalkerPrunningPerPort, ieee8021SrpStreamEntry=ieee8021SrpStreamEntry, IEEE8021SrpReservationDirectionValue=IEEE8021SrpReservationDirectionValue, ieee8021SrpReservationStreamId=ieee8021SrpReservationStreamId, ieee8021SrpStreamTspecMaxIntervalFrames=ieee8021SrpStreamTspecMaxIntervalFrames, ieee8021SrpBridgePortMsrpLastPduOrigin=ieee8021SrpBridgePortMsrpLastPduOrigin, ieee8021SrpLatencyGroup=ieee8021SrpLatencyGroup, ieee8021SrpReservations=ieee8021SrpReservations, ieee8021SrpLatencyTable=ieee8021SrpLatencyTable, ieee8021SrpCompliance=ieee8021SrpCompliance, ieee8021SrpReservationsTable=ieee8021SrpReservationsTable, ieee8021SrpReservationDeclarationType=ieee8021SrpReservationDeclarationType, ieee8021SrpLatencyEntry=ieee8021SrpLatencyEntry, IEEE8021SrpStreamRankValue=IEEE8021SrpStreamRankValue, ieee8021SrpMib=ieee8021SrpMib, ieee8021SrpStreamTable=ieee8021SrpStreamTable, ieee8021SrpStreamsGroup=ieee8021SrpStreamsGroup, ieee8021SrpReservationStreamAge=ieee8021SrpReservationStreamAge, ieee8021SrpBridgePortEntry=ieee8021SrpBridgePortEntry, ieee8021SrpStreamTspecMaxFrameSize=ieee8021SrpStreamTspecMaxFrameSize, ieee8021SrpCompliances=ieee8021SrpCompliances, ieee8021SrpStreamPreloadDataFramePriority=ieee8021SrpStreamPreloadDataFramePriority, ieee8021SrpReservationsPreloadEntry=ieee8021SrpReservationsPreloadEntry, ieee8021SrpConfiguration=ieee8021SrpConfiguration, ieee8021SrpBridgePortSrPvid=ieee8021SrpBridgePortSrPvid, ieee8021SrpStreamPreloadDestinationAddress=ieee8021SrpStreamPreloadDestinationAddress, ieee8021SrpConfigurationPruningGroup=ieee8021SrpConfigurationPruningGroup, ieee8021SrpPortTcLatency=ieee8021SrpPortTcLatency, ieee8021SrpReservationPreloadAccumulatedLatency=ieee8021SrpReservationPreloadAccumulatedLatency, ieee8021SrpReservationsGroup=ieee8021SrpReservationsGroup, ieee8021SrpBridgeBaseMsrpMaxSRClasses=ieee8021SrpBridgeBaseMsrpMaxSRClasses, ieee8021SrpStreamVlanId=ieee8021SrpStreamVlanId, ieee8021SrpBridgeBaseMsrpTalkerPruning=ieee8021SrpBridgeBaseMsrpTalkerPruning, ieee8021SrpStreamPreloadId=ieee8021SrpStreamPreloadId, ieee8021SrpGroups=ieee8021SrpGroups, ieee8021SrpReservationDroppedStreamFrames=ieee8021SrpReservationDroppedStreamFrames, IEEE8021SrpReservationDeclarationTypeValue=IEEE8021SrpReservationDeclarationTypeValue, ieee8021SrpBridgeBaseTable=ieee8021SrpBridgeBaseTable, ieee8021SrpStreamPreloadTspecMaxFrameSize=ieee8021SrpStreamPreloadTspecMaxFrameSize, ieee8021SrpReservationsPreloadGroup=ieee8021SrpReservationsPreloadGroup, ieee8021SrpStreamRank=ieee8021SrpStreamRank, ieee8021SrpBridgeBaseMsrpTalkerVlanPruning=ieee8021SrpBridgeBaseMsrpTalkerVlanPruning, ieee8021SrpBridgeBaseEntry=ieee8021SrpBridgeBaseEntry, ieee8021SrpStreamDestinationAddress=ieee8021SrpStreamDestinationAddress, ieee8021SrpMonitoringSRclassesGroup=ieee8021SrpMonitoringSRclassesGroup, IEEE8021SrpStreamIdValue=IEEE8021SrpStreamIdValue, ieee8021SrpLatency=ieee8021SrpLatency, ieee8021SrpConfigurationGroup=ieee8021SrpConfigurationGroup, PYSNMP_MODULE_ID=ieee8021SrpMib, ieee8021SrpBridgePortTable=ieee8021SrpBridgePortTable, ieee8021SrpStreams=ieee8021SrpStreams, ieee8021SrpStreamsPreloadGroup=ieee8021SrpStreamsPreloadGroup, ieee8021SrpNotifications=ieee8021SrpNotifications, ieee8021SrpStreamPreloadEntry=ieee8021SrpStreamPreloadEntry, ieee8021SrpReservationFailureCode=ieee8021SrpReservationFailureCode, ieee8021SrpReservationFailureSystemId=ieee8021SrpReservationFailureSystemId, ieee8021SrpReservationsPreloadTable=ieee8021SrpReservationsPreloadTable, ieee8021SrpStreamPreloadVlanId=ieee8021SrpStreamPreloadVlanId, ieee8021SrpStreamDataFramePriority=ieee8021SrpStreamDataFramePriority, ieee8021SrpBridgeBaseMsrpEnabledStatus=ieee8021SrpBridgeBaseMsrpEnabledStatus, ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize=ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize, ieee8021SrpReservationDirection=ieee8021SrpReservationDirection, ieee8021SrpStreamPreloadTspecMaxIntervalFrames=ieee8021SrpStreamPreloadTspecMaxIntervalFrames, ieee8021SrpConformance=ieee8021SrpConformance, ieee8021SrpStreamPreloadTable=ieee8021SrpStreamPreloadTable, IEEE8021SrpReservationFailureCodeValue=IEEE8021SrpReservationFailureCodeValue, ieee8021SrpReservationPreloadDirection=ieee8021SrpReservationPreloadDirection, ieee8021SrpStreamPreloadRank=ieee8021SrpStreamPreloadRank, ieee8021SrpObjects=ieee8021SrpObjects, ieee8021SrpTrafficClass=ieee8021SrpTrafficClass, ieee8021SrpReservationsPreloadStreamId=ieee8021SrpReservationsPreloadStreamId, ieee8021SrpReservationsEntry=ieee8021SrpReservationsEntry, ieee8021SrpBridgePortMsrpFailedRegistrations=ieee8021SrpBridgePortMsrpFailedRegistrations)
