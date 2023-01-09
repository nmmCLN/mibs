#
# PySNMP MIB module CTRON-SFPS-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-TAP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:52 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
sfpsTap, sfpsCallTap, sfpsTapStats = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsTap", "sfpsCallTap", "sfpsTapStats")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Integer32, ModuleIdentity, Gauge32, iso, TimeTicks, Counter64, IpAddress, Unsigned32, ObjectIdentity, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Integer32", "ModuleIdentity", "Gauge32", "iso", "TimeTicks", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sfpsCallTapVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("call-tap", 2), ("call-untap", 3), ("vlan-tap", 4), ("vlan-untap", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTapVerb.setDescription('Tap/Untap request')
sfpsCallTapHeaderType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("mac-da-sa", 2), ("atm-vpi-vci", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapHeaderType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTapHeaderType.setDescription('Type of header, typically MAC DA/SA')
sfpsCallTapHeaderLength = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapHeaderLength.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTapHeaderLength.setDescription('Length of header')
sfpsCallTapHeaderValue = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapHeaderValue.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTapHeaderValue.setDescription('DA/SA header value')
sfpsCallTapArgDirection = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("bi", 2), ("uni", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapArgDirection.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTapArgDirection.setDescription('Uni or Bi directional tap')
sfpsCallTapProbeSwitch = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 6), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapProbeSwitch.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTapProbeSwitch.setDescription('Base MAC of probe switch')
sfpsCallTapProbePort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 11, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTapProbePort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTapProbePort.setDescription('Port number of probe ')
sfpsTapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1), )
if mibBuilder.loadTexts: sfpsTapTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapTable.setDescription('Contains information on current taps.')
sfpsTapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1), ).setIndexNames((0, "CTRON-SFPS-TAP-MIB", "sfpsTapHeaderDASA"))
if mibBuilder.loadTexts: sfpsTapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapEntry.setDescription('')
sfpsTapHeaderDASA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapHeaderDASA.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapHeaderDASA.setDescription('DA/SA header value')
sfpsTapRQPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapRQPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapRQPort.setDescription('Inport of tap request')
sfpsTapRSPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapRSPPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapRSPPort.setDescription('Inport of tap response')
sfpsTapRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapRetries.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapRetries.setDescription('Number of tap retries')
sfpsTapSwitchState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("awaitingTapRsps", 1), ("receivingTapRsps", 2), ("retryingTapRequest", 3), ("tapActive", 4), ("awaitingUnTapRsps", 5), ("receivingUnTapRsps", 6), ("retryingUnTapRequest", 7), ("unassigned", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapSwitchState.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapSwitchState.setDescription('Tap state of switch')
sfpsTapSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("originatingTap", 1), ("intermediate", 2), ("terminal", 3), ("originatingUntap", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapSwitchType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapSwitchType.setDescription('Type of tap switch')
sfpsTapSwitchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("disableOutport", 1), ("keepOutport", 2), ("probeNotFound", 3), ("decisionUnknown", 4), ("unassigned", 5), ("halfCnx", 6), ("alterCnx", 7), ("alterCnxDone", 8), ("halfCnxDone", 9), ("tapIgnore", 10), ("tapDeleteCnx", 11), ("tapMarkCnx", 12), ("tapFilterCnx", 13), ("tapSharedMedia", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapSwitchStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapSwitchStatus.setDescription('Contains information helpful for untapping')
sfpsTapDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("bi-Directional", 2), ("uni-Directional", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapDirection.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapDirection.setDescription('Uni or Bi Directional tap')
sfpsTapDirectRouteMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapDirectRouteMAC.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapDirectRouteMAC.setDescription('MAC of switch for direct Nbr connection')
sfpsTapResponseStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("disableOutport", 1), ("keepOutport", 2), ("probeNotFound", 3), ("decisionUnknown", 4), ("unassigned", 5), ("halfCnx", 6), ("alterCnx", 7), ("alterCnxDone", 8), ("halfCnxDone", 9), ("tapIgnore", 10), ("tapDeleteCnx", 11), ("tapMarkCnx", 12), ("tapFilterCnx", 13), ("tapSharedMedia", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapResponseStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapResponseStatus.setDescription('Status to reutrn for multi-tap')
sfpsTapProbeSwitchMac = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapProbeSwitchMac.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapProbeSwitchMac.setDescription('Probe Switch mac address')
sfpsTapProbePort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 12, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapProbePort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapProbePort.setDescription('Probe Switch port')
sfpsTapStatsTapReqCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsTapReqCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapStatsTapReqCnt.setDescription('Count for all tap requests')
sfpsTapStatsTapRespCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsTapRespCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapStatsTapRespCnt.setDescription('Count for all tap responses')
sfpsTapStatsUntapReqCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsUntapReqCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapStatsUntapReqCnt.setDescription('Count of all untap requests')
sfpsTapStatsUntapRespCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsUntapRespCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapStatsUntapRespCnt.setDescription('Count of all untap responses')
sfpsTapStatsErrorCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsErrorCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapStatsErrorCnt.setDescription('Count of all tap errors')
sfpsTapStatsStaleEntCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 13, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsTapStatsStaleEntCnt.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsTapStatsStaleEntCnt.setDescription('Count of all stale tap entries')
mibBuilder.exportSymbols("CTRON-SFPS-TAP-MIB", sfpsTapResponseStatus=sfpsTapResponseStatus, sfpsTapProbePort=sfpsTapProbePort, sfpsTapStatsErrorCnt=sfpsTapStatsErrorCnt, sfpsTapRetries=sfpsTapRetries, sfpsTapStatsUntapReqCnt=sfpsTapStatsUntapReqCnt, sfpsTapRQPort=sfpsTapRQPort, sfpsTapProbeSwitchMac=sfpsTapProbeSwitchMac, sfpsTapStatsTapRespCnt=sfpsTapStatsTapRespCnt, sfpsTapEntry=sfpsTapEntry, sfpsTapTable=sfpsTapTable, sfpsTapHeaderDASA=sfpsTapHeaderDASA, sfpsCallTapHeaderValue=sfpsCallTapHeaderValue, sfpsTapDirection=sfpsTapDirection, sfpsTapStatsTapReqCnt=sfpsTapStatsTapReqCnt, sfpsCallTapHeaderType=sfpsCallTapHeaderType, sfpsCallTapProbePort=sfpsCallTapProbePort, sfpsCallTapProbeSwitch=sfpsCallTapProbeSwitch, sfpsTapRSPPort=sfpsTapRSPPort, sfpsTapStatsUntapRespCnt=sfpsTapStatsUntapRespCnt, sfpsTapSwitchStatus=sfpsTapSwitchStatus, sfpsCallTapHeaderLength=sfpsCallTapHeaderLength, sfpsTapStatsStaleEntCnt=sfpsTapStatsStaleEntCnt, sfpsTapSwitchState=sfpsTapSwitchState, sfpsTapDirectRouteMAC=sfpsTapDirectRouteMAC, sfpsCallTapArgDirection=sfpsCallTapArgDirection, sfpsCallTapVerb=sfpsCallTapVerb, sfpsTapSwitchType=sfpsTapSwitchType)
