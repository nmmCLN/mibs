#
# PySNMP MIB module CTRON-SFPS-PKTMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-PKTMGR-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
sfpsSwitchSfpsPacket, sfpsCSPPacket, sfpsPktDispatchStats = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsSwitchSfpsPacket", "sfpsCSPPacket", "sfpsPktDispatchStats")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, Bits, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "Bits", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SfpsSwitchInstance(Integer32):
    pass

class HexInteger(Integer32):
    pass

sfpsPacketMgrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1), )
if mibBuilder.loadTexts: sfpsPacketMgrTable.setStatus('mandatory')
sfpsPacketMgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1), ).setIndexNames((0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketMgrSwitchID"), (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketMgrPacketType"))
if mibBuilder.loadTexts: sfpsPacketMgrEntry.setStatus('mandatory')
sfpsPacketMgrSwitchID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrSwitchID.setStatus('mandatory')
sfpsPacketMgrPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 2), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrPacketType.setStatus('mandatory')
sfpsPacketMgrTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrTotalPackets.setStatus('mandatory')
sfpsPacketMgrPktsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrPktsUsed.setStatus('mandatory')
sfpsPacketMgrPktsAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrPktsAvailable.setStatus('mandatory')
sfpsPacketMgrPktsInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrPktsInUse.setStatus('mandatory')
sfpsPacketMgrNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrNotFound.setStatus('mandatory')
sfpsPacketMgrTooLarge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketMgrTooLarge.setStatus('mandatory')
sfpsPacketMgrToCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPacketMgrToCreate.setStatus('mandatory')
sfpsPacketMgrReInit = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("reinit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPacketMgrReInit.setStatus('mandatory')
sfpsPacketListTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2), )
if mibBuilder.loadTexts: sfpsPacketListTable.setStatus('mandatory')
sfpsPacketListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1), ).setIndexNames((0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketListPacketType"), (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketListSize"))
if mibBuilder.loadTexts: sfpsPacketListEntry.setStatus('mandatory')
sfpsPacketListPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListPacketType.setStatus('mandatory')
sfpsPacketListSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListSize.setStatus('mandatory')
sfpsPacketListTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListTotalPackets.setStatus('mandatory')
sfpsPacketListPktsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListPktsUsed.setStatus('mandatory')
sfpsPacketListPktsLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListPktsLeft.setStatus('mandatory')
sfpsPacketListPktsInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListPktsInUse.setStatus('mandatory')
sfpsPacketListLowWater = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListLowWater.setStatus('mandatory')
sfpsPacketListNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListNotFound.setStatus('mandatory')
sfpsPacketListStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketListStatus.setStatus('mandatory')
sfpsPacketSizeTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3), )
if mibBuilder.loadTexts: sfpsPacketSizeTable.setStatus('mandatory')
sfpsPacketSizeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1), ).setIndexNames((0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketSizeSwitchInstance"), (0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketSizeSize"))
if mibBuilder.loadTexts: sfpsPacketSizeEntry.setStatus('mandatory')
sfpsPacketSizeSwitchInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 1), SfpsSwitchInstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketSizeSwitchInstance.setStatus('mandatory')
sfpsPacketSizeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketSizeSize.setStatus('mandatory')
sfpsPacketSizePktsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketSizePktsUsed.setStatus('mandatory')
sfpsPacketSizeNotFound = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketSizeNotFound.setStatus('mandatory')
sfpsPacketQTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4), )
if mibBuilder.loadTexts: sfpsPacketQTable.setStatus('mandatory')
sfpsPacketQEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1), ).setIndexNames((0, "CTRON-SFPS-PKTMGR-MIB", "sfpsPacketQPriorityQ"))
if mibBuilder.loadTexts: sfpsPacketQEntry.setStatus('mandatory')
sfpsPacketQPriorityQ = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("low", 1), ("medium", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketQPriorityQ.setStatus('mandatory')
sfpsPacketQTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketQTotalPackets.setStatus('mandatory')
sfpsPacketQCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketQCurrent.setStatus('mandatory')
sfpsPacketQHighWater = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsPacketQHighWater.setStatus('mandatory')
sfpsCSPPacketStatsPacketsSentBad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsSentBad.setStatus('mandatory')
sfpsCSPPacketStatsPacketsSentGood = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsSentGood.setStatus('mandatory')
sfpsCSPPacketStatsPacketsReceivedBad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsReceivedBad.setStatus('mandatory')
sfpsCSPPacketStatsPacketsReceivedGood = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 10, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCSPPacketStatsPacketsReceivedGood.setStatus('mandatory')
sfpsPktDispatchStatsVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("resetAllStats", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsPktDispatchStatsVerb.setStatus('mandatory')
numHPMInvalidFrameTypeDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMInvalidFrameTypeDrops.setStatus('mandatory')
numHPMFilterMgtPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMFilterMgtPortDrops.setStatus('mandatory')
numHPMPhysToLogPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMPhysToLogPortDrops.setStatus('mandatory')
numHPMNullSFPSPktDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMNullSFPSPktDrops.setStatus('mandatory')
numHPM81fdThrottleDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPM81fdThrottleDrops.setStatus('mandatory')
numHPM81ffThrottleDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPM81ffThrottleDrops.setStatus('mandatory')
numHPMPhysStandbyMaskDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPMPhysStandbyMaskDrops.setStatus('mandatory')
numBSInvSrcPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSInvSrcPortDrops.setStatus('mandatory')
numBSSourceBlockDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSSourceBlockDrops.setStatus('mandatory')
numBSViolationDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSViolationDrops.setStatus('mandatory')
numBSUnknownPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSUnknownPortDrops.setStatus('mandatory')
numBSStandbyPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSStandbyPortDrops.setStatus('mandatory')
numBSFabricNghbrPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSFabricNghbrPortDrops.setStatus('mandatory')
numBSGoingToAccessPortDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSGoingToAccessPortDrops.setStatus('mandatory')
numBSInvPortTypeDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSInvPortTypeDrops.setStatus('mandatory')
numBSNullCallDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSNullCallDrops.setStatus('mandatory')
numBSNullBottomCPDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSNullBottomCPDrops.setStatus('mandatory')
numBSInvCSPTypeDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSInvCSPTypeDrops.setStatus('mandatory')
numBSNonHello81fdDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSNonHello81fdDrops.setStatus('mandatory')
numBSCSPCtrlDisableDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSCSPCtrlDisableDrops.setStatus('mandatory')
numBSCSPCtrlIndexDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBSCSPCtrlIndexDrops.setStatus('mandatory')
numBCPNullCallDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPNullCallDrops.setStatus('mandatory')
numBCPCPFaultedDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPCPFaultedDrops.setStatus('mandatory')
numBCPGleanFailDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPGleanFailDrops.setStatus('mandatory')
numBCPCPHaltedDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPCPHaltedDrops.setStatus('mandatory')
numBCPSwitchedBCADrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPSwitchedBCADrops.setStatus('mandatory')
numBCPCallNotAcceptedDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numBCPCallNotAcceptedDrops.setStatus('mandatory')
numHPM81fdNullPktDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPM81fdNullPktDrops.setStatus('mandatory')
numHPM81fdHelloNullPktDrops = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 7, 5, 30), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numHPM81fdHelloNullPktDrops.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-PKTMGR-MIB", sfpsPacketQPriorityQ=sfpsPacketQPriorityQ, numBSInvSrcPortDrops=numBSInvSrcPortDrops, numBSInvPortTypeDrops=numBSInvPortTypeDrops, sfpsPacketListTable=sfpsPacketListTable, numBCPCPFaultedDrops=numBCPCPFaultedDrops, sfpsCSPPacketStatsPacketsSentBad=sfpsCSPPacketStatsPacketsSentBad, sfpsPacketSizePktsUsed=sfpsPacketSizePktsUsed, sfpsPacketListTotalPackets=sfpsPacketListTotalPackets, sfpsPacketListPacketType=sfpsPacketListPacketType, sfpsCSPPacketStatsPacketsReceivedBad=sfpsCSPPacketStatsPacketsReceivedBad, numBCPCPHaltedDrops=numBCPCPHaltedDrops, numBSNonHello81fdDrops=numBSNonHello81fdDrops, sfpsCSPPacketStatsPacketsSentGood=sfpsCSPPacketStatsPacketsSentGood, sfpsPacketMgrTotalPackets=sfpsPacketMgrTotalPackets, sfpsPacketMgrTable=sfpsPacketMgrTable, sfpsPacketListNotFound=sfpsPacketListNotFound, sfpsPacketQTable=sfpsPacketQTable, sfpsPacketQHighWater=sfpsPacketQHighWater, numHPM81fdHelloNullPktDrops=numHPM81fdHelloNullPktDrops, sfpsPacketListSize=sfpsPacketListSize, sfpsPacketQTotalPackets=sfpsPacketQTotalPackets, SfpsSwitchInstance=SfpsSwitchInstance, sfpsPacketMgrPacketType=sfpsPacketMgrPacketType, numHPMInvalidFrameTypeDrops=numHPMInvalidFrameTypeDrops, sfpsPacketSizeEntry=sfpsPacketSizeEntry, sfpsPacketMgrPktsUsed=sfpsPacketMgrPktsUsed, numBCPGleanFailDrops=numBCPGleanFailDrops, sfpsPktDispatchStatsVerb=sfpsPktDispatchStatsVerb, sfpsPacketMgrPktsInUse=sfpsPacketMgrPktsInUse, sfpsPacketMgrNotFound=sfpsPacketMgrNotFound, numBSNullCallDrops=numBSNullCallDrops, sfpsPacketQEntry=sfpsPacketQEntry, sfpsPacketListPktsLeft=sfpsPacketListPktsLeft, numBSViolationDrops=numBSViolationDrops, numBSInvCSPTypeDrops=numBSInvCSPTypeDrops, sfpsPacketMgrToCreate=sfpsPacketMgrToCreate, numHPMNullSFPSPktDrops=numHPMNullSFPSPktDrops, numBSNullBottomCPDrops=numBSNullBottomCPDrops, sfpsPacketListPktsInUse=sfpsPacketListPktsInUse, numHPMPhysStandbyMaskDrops=numHPMPhysStandbyMaskDrops, numBCPSwitchedBCADrops=numBCPSwitchedBCADrops, sfpsPacketMgrPktsAvailable=sfpsPacketMgrPktsAvailable, sfpsPacketMgrSwitchID=sfpsPacketMgrSwitchID, sfpsPacketListEntry=sfpsPacketListEntry, sfpsPacketMgrReInit=sfpsPacketMgrReInit, sfpsPacketSizeNotFound=sfpsPacketSizeNotFound, sfpsPacketListStatus=sfpsPacketListStatus, numHPM81fdThrottleDrops=numHPM81fdThrottleDrops, numBSSourceBlockDrops=numBSSourceBlockDrops, sfpsPacketListPktsUsed=sfpsPacketListPktsUsed, HexInteger=HexInteger, numBSUnknownPortDrops=numBSUnknownPortDrops, numBSGoingToAccessPortDrops=numBSGoingToAccessPortDrops, numBSFabricNghbrPortDrops=numBSFabricNghbrPortDrops, sfpsPacketQCurrent=sfpsPacketQCurrent, numHPMPhysToLogPortDrops=numHPMPhysToLogPortDrops, numHPM81ffThrottleDrops=numHPM81ffThrottleDrops, sfpsCSPPacketStatsPacketsReceivedGood=sfpsCSPPacketStatsPacketsReceivedGood, sfpsPacketListLowWater=sfpsPacketListLowWater, numBCPNullCallDrops=numBCPNullCallDrops, numBSCSPCtrlDisableDrops=numBSCSPCtrlDisableDrops, numBSStandbyPortDrops=numBSStandbyPortDrops, numHPM81fdNullPktDrops=numHPM81fdNullPktDrops, numBCPCallNotAcceptedDrops=numBCPCallNotAcceptedDrops, sfpsPacketSizeSize=sfpsPacketSizeSize, sfpsPacketMgrTooLarge=sfpsPacketMgrTooLarge, numHPMFilterMgtPortDrops=numHPMFilterMgtPortDrops, sfpsPacketSizeTable=sfpsPacketSizeTable, sfpsPacketSizeSwitchInstance=sfpsPacketSizeSwitchInstance, numBSCSPCtrlIndexDrops=numBSCSPCtrlIndexDrops, sfpsPacketMgrEntry=sfpsPacketMgrEntry)
