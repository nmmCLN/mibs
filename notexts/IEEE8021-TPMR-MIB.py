#
# PySNMP MIB module IEEE8021-TPMR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-TPMR-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:23:45 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ieee8021BridgeBasePortComponentId, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId")
IEEE8021BridgePortNumber, ieee802dot1mibs = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumber", "ieee802dot1mibs")
ifCounterDiscontinuityGroup, = mibBuilder.importSymbols("IF-MIB", "ifCounterDiscontinuityGroup")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Integer32, ObjectIdentity, MibIdentifier, NotificationType, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter32, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "NotificationType", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter32", "Unsigned32", "TimeTicks", "Counter64")
MacAddress, DisplayString, StorageType, TextualConvention, TimeInterval, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "StorageType", "TextualConvention", "TimeInterval", "TruthValue")
ieee8021TpmrMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 14))
ieee8021TpmrMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2011-02-27 00:00', '2009-09-04 00:00',))
if mibBuilder.loadTexts: ieee8021TpmrMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021TpmrMib.setOrganization('IEEE 802.1 Working Group')
ieee8021TpmrNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 14, 0))
ieee8021TpmrObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 14, 1))
ieee8021TpmrConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 14, 2))
class IEEE8021TpmrFrameDiscardErrorReason(TextualConvention, Integer32):
    reference = '12.19.3.1.1.3:h'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("txSduSizeExceeded", 1))

ieee8021TpmrPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 14, 1, 1), )
if mibBuilder.loadTexts: ieee8021TpmrPortTable.setStatus('current')
ieee8021TpmrPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 14, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-TPMR-MIB", "ieee8021TpmrPortNumber"))
if mibBuilder.loadTexts: ieee8021TpmrPortEntry.setStatus('current')
ieee8021TpmrPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 1, 1, 1), IEEE8021BridgePortNumber().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: ieee8021TpmrPortNumber.setStatus('current')
ieee8021TpmrPortMgmtAddr = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortMgmtAddr.setStatus('current')
ieee8021TpmrPortMgmtAddrForwarding = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortMgmtAddrForwarding.setStatus('current')
ieee8021TpmrPortStatsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 14, 1, 2), )
if mibBuilder.loadTexts: ieee8021TpmrPortStatsTable.setStatus('current')
ieee8021TpmrPortStatsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1), )
ieee8021TpmrPortEntry.registerAugmentions(("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsEntry"))
ieee8021TpmrPortStatsEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021TpmrPortStatsEntry.setStatus('current')
ieee8021TpmrPortStatsRxFrames = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 1), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortStatsRxFrames.setStatus('current')
ieee8021TpmrPortStatsRxOctets = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 2), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortStatsRxOctets.setStatus('current')
ieee8021TpmrPortStatsFramesForwarded = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 3), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortStatsFramesForwarded.setStatus('current')
ieee8021TpmrPortStatsFramesDiscarded = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 4), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortStatsFramesDiscarded.setStatus('current')
ieee8021TpmrPortStatsFramesDiscardedQueueFull = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 5), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortStatsFramesDiscardedQueueFull.setStatus('current')
ieee8021TpmrPortStatsFramesDiscardedLifetime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 6), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortStatsFramesDiscardedLifetime.setStatus('current')
ieee8021TpmrPortStatsFramesDiscardedError = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 2, 1, 7), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortStatsFramesDiscardedError.setStatus('current')
ieee8021TpmrPortDiscardDetailsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 14, 1, 3), )
if mibBuilder.loadTexts: ieee8021TpmrPortDiscardDetailsTable.setStatus('current')
ieee8021TpmrPortDiscardDetailsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 14, 1, 3, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-TPMR-MIB", "ieee8021TpmrPortNumber"), (0, "IEEE8021-TPMR-MIB", "ieee8021TpmrPortDiscardDetailsIndex"))
if mibBuilder.loadTexts: ieee8021TpmrPortDiscardDetailsEntry.setStatus('current')
ieee8021TpmrPortDiscardDetailsIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: ieee8021TpmrPortDiscardDetailsIndex.setStatus('current')
ieee8021TpmrPortDiscardDetailsSource = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortDiscardDetailsSource.setStatus('current')
ieee8021TpmrPortDiscardDetailsReason = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 3, 1, 3), IEEE8021TpmrFrameDiscardErrorReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrPortDiscardDetailsReason.setStatus('current')
ieee8021TpmrMspTable = MibTable((1, 3, 111, 2, 802, 1, 1, 14, 1, 4), )
if mibBuilder.loadTexts: ieee8021TpmrMspTable.setStatus('current')
ieee8021TpmrMspEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1), )
ieee8021TpmrPortEntry.registerAugmentions(("IEEE8021-TPMR-MIB", "ieee8021TpmrMspEntry"))
ieee8021TpmrMspEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021TpmrMspEntry.setStatus('current')
ieee8021TpmrMspLinkNotify = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021TpmrMspLinkNotify.setStatus('current')
ieee8021TpmrMspLinkNotifyWait = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 2), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(20, 100)).clone(40)).setUnits('centiseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021TpmrMspLinkNotifyWait.setStatus('current')
ieee8021TpmrMspLinkNotifyRetry = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 3), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(100)).setUnits('centiseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021TpmrMspLinkNotifyRetry.setStatus('current')
ieee8021TpmrMspMacNotify = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021TpmrMspMacNotify.setStatus('current')
ieee8021TpmrMspMacNotifyTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 5), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(20)).setUnits('centiseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021TpmrMspMacNotifyTime.setStatus('current')
ieee8021TpmrMspMacRecoverTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 6), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(2, 50)).clone(10)).setUnits('centiseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021TpmrMspMacRecoverTime.setStatus('current')
ieee8021TpmrMspStorageType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 4, 1, 7), StorageType().clone('nonVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021TpmrMspStorageType.setStatus('current')
ieee8021TpmrMspStatsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 14, 1, 5), )
if mibBuilder.loadTexts: ieee8021TpmrMspStatsTable.setStatus('current')
ieee8021TpmrMspStatsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1), )
ieee8021TpmrPortEntry.registerAugmentions(("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsEntry"))
ieee8021TpmrMspStatsEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021TpmrMspStatsEntry.setStatus('current')
ieee8021TpmrMspStatsTxAcks = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 1), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsTxAcks.setStatus('current')
ieee8021TpmrMspStatsTxAddNotifications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 2), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsTxAddNotifications.setStatus('current')
ieee8021TpmrMspStatsTxAddConfirmations = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 3), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsTxAddConfirmations.setStatus('current')
ieee8021TpmrMspStatsTxLossNotifications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 4), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsTxLossNotifications.setStatus('current')
ieee8021TpmrMspStatsTxLossConfirmations = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 5), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsTxLossConfirmations.setStatus('current')
ieee8021TpmrMspStatsRxAcks = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 6), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsRxAcks.setStatus('current')
ieee8021TpmrMspStatsRxAddNotifications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 7), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsRxAddNotifications.setStatus('current')
ieee8021TpmrMspStatsRxAddConfirmations = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 8), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsRxAddConfirmations.setStatus('current')
ieee8021TpmrMspStatsRxLossNotifications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 9), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsRxLossNotifications.setStatus('current')
ieee8021TpmrMspStatsRxLossConfirmations = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 10), Counter32()).setUnits('MSPDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsRxLossConfirmations.setStatus('current')
ieee8021TpmrMspStatsAddEvents = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 11), Counter32()).setUnits('MSP transitions').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsAddEvents.setStatus('current')
ieee8021TpmrMspStatsLossEvents = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 12), Counter32()).setUnits('MSP transitions').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsLossEvents.setStatus('current')
ieee8021TpmrMspStatsMacStatusNotifications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 14, 1, 5, 1, 13), Counter32()).setUnits('MSP transitions').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TpmrMspStatsMacStatusNotifications.setStatus('current')
ieee8021TpmrCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 14, 2, 1))
ieee8021TpmrGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 14, 2, 2))
ieee8021TpmrPortGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 1)).setObjects(("IEEE8021-TPMR-MIB", "ieee8021TpmrPortMgmtAddr"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortMgmtAddrForwarding"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TpmrPortGroup = ieee8021TpmrPortGroup.setStatus('current')
ieee8021TpmrPortStatsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 2)).setObjects(("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsRxFrames"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsRxOctets"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesForwarded"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesDiscarded"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesDiscardedQueueFull"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesDiscardedLifetime"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsFramesDiscardedError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TpmrPortStatsGroup = ieee8021TpmrPortStatsGroup.setStatus('current')
ieee8021TpmrPortDiscardDetailsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 3)).setObjects(("IEEE8021-TPMR-MIB", "ieee8021TpmrPortDiscardDetailsSource"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortDiscardDetailsReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TpmrPortDiscardDetailsGroup = ieee8021TpmrPortDiscardDetailsGroup.setStatus('current')
ieee8021TpmrMspGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 4)).setObjects(("IEEE8021-TPMR-MIB", "ieee8021TpmrMspLinkNotify"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspLinkNotifyWait"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspLinkNotifyRetry"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspMacNotify"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspMacNotifyTime"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspMacRecoverTime"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TpmrMspGroup = ieee8021TpmrMspGroup.setStatus('current')
ieee8021TpmrMspStatsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 14, 2, 2, 5)).setObjects(("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxAcks"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxAddNotifications"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxAddConfirmations"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxLossNotifications"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsTxLossConfirmations"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxAcks"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxAddNotifications"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxAddConfirmations"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxLossNotifications"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsRxLossConfirmations"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsAddEvents"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsLossEvents"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsMacStatusNotifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TpmrMspStatsGroup = ieee8021TpmrMspStatsGroup.setStatus('current')
ieee8021TpmrCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 14, 2, 1, 1)).setObjects(("IF-MIB", "ifCounterDiscontinuityGroup"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortGroup"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortStatsGroup"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrPortDiscardDetailsGroup"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspGroup"), ("IEEE8021-TPMR-MIB", "ieee8021TpmrMspStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TpmrCompliance = ieee8021TpmrCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-TPMR-MIB", ieee8021TpmrMspLinkNotifyRetry=ieee8021TpmrMspLinkNotifyRetry, ieee8021TpmrPortMgmtAddrForwarding=ieee8021TpmrPortMgmtAddrForwarding, ieee8021TpmrPortStatsFramesDiscardedQueueFull=ieee8021TpmrPortStatsFramesDiscardedQueueFull, ieee8021TpmrPortStatsTable=ieee8021TpmrPortStatsTable, ieee8021TpmrPortTable=ieee8021TpmrPortTable, ieee8021TpmrPortGroup=ieee8021TpmrPortGroup, ieee8021TpmrMspStatsTxAddNotifications=ieee8021TpmrMspStatsTxAddNotifications, ieee8021TpmrPortNumber=ieee8021TpmrPortNumber, ieee8021TpmrPortStatsRxFrames=ieee8021TpmrPortStatsRxFrames, ieee8021TpmrMspEntry=ieee8021TpmrMspEntry, ieee8021TpmrMspMacRecoverTime=ieee8021TpmrMspMacRecoverTime, ieee8021TpmrPortStatsGroup=ieee8021TpmrPortStatsGroup, ieee8021TpmrMspStatsTxAcks=ieee8021TpmrMspStatsTxAcks, ieee8021TpmrPortDiscardDetailsGroup=ieee8021TpmrPortDiscardDetailsGroup, ieee8021TpmrMspStatsTxLossNotifications=ieee8021TpmrMspStatsTxLossNotifications, IEEE8021TpmrFrameDiscardErrorReason=IEEE8021TpmrFrameDiscardErrorReason, ieee8021TpmrPortDiscardDetailsEntry=ieee8021TpmrPortDiscardDetailsEntry, ieee8021TpmrPortStatsEntry=ieee8021TpmrPortStatsEntry, ieee8021TpmrMspStatsRxAcks=ieee8021TpmrMspStatsRxAcks, ieee8021TpmrPortStatsFramesDiscardedLifetime=ieee8021TpmrPortStatsFramesDiscardedLifetime, ieee8021TpmrMspStatsGroup=ieee8021TpmrMspStatsGroup, ieee8021TpmrPortStatsFramesForwarded=ieee8021TpmrPortStatsFramesForwarded, ieee8021TpmrMspStatsMacStatusNotifications=ieee8021TpmrMspStatsMacStatusNotifications, ieee8021TpmrMspLinkNotifyWait=ieee8021TpmrMspLinkNotifyWait, ieee8021TpmrMspStatsRxLossConfirmations=ieee8021TpmrMspStatsRxLossConfirmations, ieee8021TpmrPortMgmtAddr=ieee8021TpmrPortMgmtAddr, ieee8021TpmrMspGroup=ieee8021TpmrMspGroup, ieee8021TpmrObjects=ieee8021TpmrObjects, ieee8021TpmrMspStatsLossEvents=ieee8021TpmrMspStatsLossEvents, ieee8021TpmrMspStatsTxAddConfirmations=ieee8021TpmrMspStatsTxAddConfirmations, ieee8021TpmrMspTable=ieee8021TpmrMspTable, ieee8021TpmrMspStatsTable=ieee8021TpmrMspStatsTable, ieee8021TpmrConformance=ieee8021TpmrConformance, ieee8021TpmrPortEntry=ieee8021TpmrPortEntry, PYSNMP_MODULE_ID=ieee8021TpmrMib, ieee8021TpmrGroups=ieee8021TpmrGroups, ieee8021TpmrPortStatsFramesDiscarded=ieee8021TpmrPortStatsFramesDiscarded, ieee8021TpmrPortDiscardDetailsSource=ieee8021TpmrPortDiscardDetailsSource, ieee8021TpmrMspStatsRxAddConfirmations=ieee8021TpmrMspStatsRxAddConfirmations, ieee8021TpmrPortStatsRxOctets=ieee8021TpmrPortStatsRxOctets, ieee8021TpmrPortDiscardDetailsTable=ieee8021TpmrPortDiscardDetailsTable, ieee8021TpmrMspMacNotifyTime=ieee8021TpmrMspMacNotifyTime, ieee8021TpmrMspStatsEntry=ieee8021TpmrMspStatsEntry, ieee8021TpmrCompliance=ieee8021TpmrCompliance, ieee8021TpmrMspStatsRxLossNotifications=ieee8021TpmrMspStatsRxLossNotifications, ieee8021TpmrMspMacNotify=ieee8021TpmrMspMacNotify, ieee8021TpmrMspStorageType=ieee8021TpmrMspStorageType, ieee8021TpmrCompliances=ieee8021TpmrCompliances, ieee8021TpmrPortStatsFramesDiscardedError=ieee8021TpmrPortStatsFramesDiscardedError, ieee8021TpmrPortDiscardDetailsIndex=ieee8021TpmrPortDiscardDetailsIndex, ieee8021TpmrPortDiscardDetailsReason=ieee8021TpmrPortDiscardDetailsReason, ieee8021TpmrMib=ieee8021TpmrMib, ieee8021TpmrMspLinkNotify=ieee8021TpmrMspLinkNotify, ieee8021TpmrMspStatsTxLossConfirmations=ieee8021TpmrMspStatsTxLossConfirmations, ieee8021TpmrMspStatsRxAddNotifications=ieee8021TpmrMspStatsRxAddNotifications, ieee8021TpmrMspStatsAddEvents=ieee8021TpmrMspStatsAddEvents, ieee8021TpmrNotifications=ieee8021TpmrNotifications)
