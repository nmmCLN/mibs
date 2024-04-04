#
# PySNMP MIB module OPENBSD-PF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-PF-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:21:36 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Integer32, MibIdentifier, Unsigned32, ModuleIdentity, Gauge32, Counter32, enterprises, Counter64, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Gauge32", "Counter32", "enterprises", "Counter64", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
pfMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 1))
pfMIBObjects.setRevisions(('2015-06-09 17:28', '2013-08-31 04:46', '2013-02-24 20:33', '2012-01-26 00:00',))
if mibBuilder.loadTexts: pfMIBObjects.setLastUpdated('201506091728Z')
if mibBuilder.loadTexts: pfMIBObjects.setOrganization('OpenBSD')
pfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 1))
pfCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 2))
pfStateTable = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 3))
pfLogInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 4))
pfSrcTracking = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 5))
pfLimits = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 6))
pfTimeouts = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 7))
pfInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 8))
pfTables = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 9))
pfLabels = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 10))
pfsyncStats = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 1, 11))
pfRunning = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfRunning.setStatus('current')
pfRuntime = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 1, 2), TimeTicks()).setUnits('1/100th of a Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: pfRuntime.setStatus('current')
pfDebug = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emerg", 0), ("alert", 1), ("crit", 2), ("err", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfDebug.setStatus('current')
pfHostid = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfHostid.setStatus('current')
pfCntMatch = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntMatch.setStatus('current')
pfCntBadOffset = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntBadOffset.setStatus('current')
pfCntFragment = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntFragment.setStatus('current')
pfCntShort = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntShort.setStatus('current')
pfCntNormalize = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntNormalize.setStatus('current')
pfCntMemory = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntMemory.setStatus('current')
pfCntTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntTimestamp.setStatus('current')
pfCntCongestion = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntCongestion.setStatus('current')
pfCntIpOption = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntIpOption.setStatus('current')
pfCntProtoCksum = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntProtoCksum.setStatus('current')
pfCntStateMismatch = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntStateMismatch.setStatus('current')
pfCntStateInsert = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntStateInsert.setStatus('current')
pfCntStateLimit = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntStateLimit.setStatus('current')
pfCntSrcLimit = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntSrcLimit.setStatus('current')
pfCntSynproxy = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntSynproxy.setStatus('current')
pfCntTranslate = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntTranslate.setStatus('current')
pfCntNoRoute = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 2, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfCntNoRoute.setStatus('current')
pfStateCount = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStateCount.setStatus('current')
pfStateSearches = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStateSearches.setStatus('current')
pfStateInserts = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStateInserts.setStatus('current')
pfStateRemovals = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfStateRemovals.setStatus('current')
pfLogIfName = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfName.setStatus('current')
pfLogIfIpBytesIn = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIpBytesIn.setStatus('current')
pfLogIfIpBytesOut = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIpBytesOut.setStatus('current')
pfLogIfIpPktsInPass = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIpPktsInPass.setStatus('current')
pfLogIfIpPktsInDrop = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIpPktsInDrop.setStatus('current')
pfLogIfIpPktsOutPass = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIpPktsOutPass.setStatus('current')
pfLogIfIpPktsOutDrop = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIpPktsOutDrop.setStatus('current')
pfLogIfIp6BytesIn = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIp6BytesIn.setStatus('current')
pfLogIfIp6BytesOut = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIp6BytesOut.setStatus('current')
pfLogIfIp6PktsInPass = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIp6PktsInPass.setStatus('current')
pfLogIfIp6PktsInDrop = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIp6PktsInDrop.setStatus('current')
pfLogIfIp6PktsOutPass = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIp6PktsOutPass.setStatus('current')
pfLogIfIp6PktsOutDrop = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 4, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLogIfIp6PktsOutDrop.setStatus('current')
pfSrcTrackCount = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 5, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfSrcTrackCount.setStatus('current')
pfSrcTrackSearches = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfSrcTrackSearches.setStatus('current')
pfSrcTrackInserts = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 5, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfSrcTrackInserts.setStatus('current')
pfSrcTrackRemovals = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 5, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfSrcTrackRemovals.setStatus('current')
pfLimitStates = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLimitStates.setStatus('current')
pfLimitSourceNodes = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 6, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLimitSourceNodes.setStatus('current')
pfLimitFragments = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 6, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLimitFragments.setStatus('current')
pfLimitMaxTables = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 6, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLimitMaxTables.setStatus('current')
pfLimitMaxTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 6, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLimitMaxTableEntries.setStatus('current')
pfTimeoutTcpFirst = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutTcpFirst.setStatus('current')
pfTimeoutTcpOpening = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutTcpOpening.setStatus('current')
pfTimeoutTcpEstablished = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutTcpEstablished.setStatus('current')
pfTimeoutTcpClosing = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutTcpClosing.setStatus('current')
pfTimeoutTcpFinWait = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutTcpFinWait.setStatus('current')
pfTimeoutTcpClosed = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutTcpClosed.setStatus('current')
pfTimeoutUdpFirst = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutUdpFirst.setStatus('current')
pfTimeoutUdpSingle = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutUdpSingle.setStatus('current')
pfTimeoutUdpMultiple = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutUdpMultiple.setStatus('current')
pfTimeoutIcmpFirst = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutIcmpFirst.setStatus('current')
pfTimeoutIcmpError = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutIcmpError.setStatus('current')
pfTimeoutOtherFirst = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutOtherFirst.setStatus('current')
pfTimeoutOtherSingle = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutOtherSingle.setStatus('current')
pfTimeoutOtherMultiple = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutOtherMultiple.setStatus('current')
pfTimeoutFragment = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutFragment.setStatus('current')
pfTimeoutInterval = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutInterval.setStatus('current')
pfTimeoutAdaptiveStart = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutAdaptiveStart.setStatus('current')
pfTimeoutAdaptiveEnd = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutAdaptiveEnd.setStatus('current')
pfTimeoutSrcTrack = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 7, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTimeoutSrcTrack.setStatus('current')
pfIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfNumber.setStatus('current')
pfIfTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128), )
if mibBuilder.loadTexts: pfIfTable.setStatus('current')
pfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1), ).setIndexNames((0, "OPENBSD-PF-MIB", "pfIfIndex"))
if mibBuilder.loadTexts: pfIfEntry.setStatus('current')
pfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIndex.setStatus('current')
pfIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfDescr.setStatus('current')
pfIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("group", 0), ("instance", 1), ("detached", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfType.setStatus('current')
pfIfRefs = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfRefs.setStatus('current')
pfIfRules = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfRules.setStatus('current')
pfIfIn4PassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIn4PassPkts.setStatus('current')
pfIfIn4PassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIn4PassBytes.setStatus('current')
pfIfIn4BlockPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIn4BlockPkts.setStatus('current')
pfIfIn4BlockBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIn4BlockBytes.setStatus('current')
pfIfOut4PassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfOut4PassPkts.setStatus('current')
pfIfOut4PassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfOut4PassBytes.setStatus('current')
pfIfOut4BlockPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfOut4BlockPkts.setStatus('current')
pfIfOut4BlockBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfOut4BlockBytes.setStatus('current')
pfIfIn6PassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIn6PassPkts.setStatus('current')
pfIfIn6PassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIn6PassBytes.setStatus('current')
pfIfIn6BlockPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIn6BlockPkts.setStatus('current')
pfIfIn6BlockBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfIn6BlockBytes.setStatus('current')
pfIfOut6PassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfOut6PassPkts.setStatus('current')
pfIfOut6PassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfOut6PassBytes.setStatus('current')
pfIfOut6BlockPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfOut6BlockPkts.setStatus('current')
pfIfOut6BlockBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 8, 128, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfIfOut6BlockBytes.setStatus('current')
pfTblNumber = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblNumber.setStatus('current')
pfTblTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128), )
if mibBuilder.loadTexts: pfTblTable.setStatus('current')
pfTblEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1), ).setIndexNames((0, "OPENBSD-PF-MIB", "pfTblIndex"))
if mibBuilder.loadTexts: pfTblEntry.setStatus('current')
pfTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblIndex.setStatus('current')
pfTblName = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblName.setStatus('current')
pfTblAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddresses.setStatus('current')
pfTblAnchorRefs = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAnchorRefs.setStatus('current')
pfTblRuleRefs = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblRuleRefs.setStatus('current')
pfTblEvalsMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblEvalsMatch.setStatus('current')
pfTblEvalsNoMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblEvalsNoMatch.setStatus('current')
pfTblInPassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblInPassPkts.setStatus('current')
pfTblInPassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblInPassBytes.setStatus('current')
pfTblInBlockPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblInBlockPkts.setStatus('current')
pfTblInBlockBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblInBlockBytes.setStatus('current')
pfTblInXPassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblInXPassPkts.setStatus('current')
pfTblInXPassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblInXPassBytes.setStatus('current')
pfTblOutPassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblOutPassPkts.setStatus('current')
pfTblOutPassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblOutPassBytes.setStatus('current')
pfTblOutBlockPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblOutBlockPkts.setStatus('current')
pfTblOutBlockBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblOutBlockBytes.setStatus('current')
pfTblOutXPassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblOutXPassPkts.setStatus('current')
pfTblOutXPassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblOutXPassBytes.setStatus('current')
pfTblStatsCleared = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 20), TimeTicks()).setUnits('1/100th of a Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblStatsCleared.setStatus('current')
pfTblInMatchPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblInMatchPkts.setStatus('current')
pfTblInMatchBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblInMatchBytes.setStatus('current')
pfTblOutMatchPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblOutMatchPkts.setStatus('current')
pfTblOutMatchBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 128, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblOutMatchBytes.setStatus('current')
pfTblAddrTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129), )
if mibBuilder.loadTexts: pfTblAddrTable.setStatus('current')
pfTblAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1), ).setIndexNames((0, "OPENBSD-PF-MIB", "pfTblAddrTblIndex"), (0, "OPENBSD-PF-MIB", "pfTblAddrNet"), (0, "OPENBSD-PF-MIB", "pfTblAddrMask"))
if mibBuilder.loadTexts: pfTblAddrEntry.setStatus('current')
pfTblAddrTblIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrTblIndex.setStatus('current')
pfTblAddrNet = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrNet.setStatus('current')
pfTblAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrMask.setStatus('current')
pfTblAddrCleared = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 4), TimeTicks()).setUnits('1/100th of a Second').setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrCleared.setStatus('current')
pfTblAddrInBlockPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrInBlockPkts.setStatus('current')
pfTblAddrInBlockBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrInBlockBytes.setStatus('current')
pfTblAddrInPassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrInPassPkts.setStatus('current')
pfTblAddrInPassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrInPassBytes.setStatus('current')
pfTblAddrOutBlockPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrOutBlockPkts.setStatus('current')
pfTblAddrOutBlockBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrOutBlockBytes.setStatus('current')
pfTblAddrOutPassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrOutPassPkts.setStatus('current')
pfTblAddrOutPassBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrOutPassBytes.setStatus('current')
pfTblAddrInMatchPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrInMatchPkts.setStatus('current')
pfTblAddrInMatchBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrInMatchBytes.setStatus('current')
pfTblAddrOutMatchPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrOutMatchPkts.setStatus('current')
pfTblAddrOutMatchBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 9, 129, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfTblAddrOutMatchBytes.setStatus('current')
pfLabelNumber = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelNumber.setStatus('current')
pfLabelTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128), )
if mibBuilder.loadTexts: pfLabelTable.setStatus('current')
pfLabelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1), ).setIndexNames((0, "OPENBSD-PF-MIB", "pfLabelIndex"))
if mibBuilder.loadTexts: pfLabelEntry.setStatus('current')
pfLabelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelIndex.setStatus('current')
pfLabelName = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelName.setStatus('current')
pfLabelEvals = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelEvals.setStatus('current')
pfLabelPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelPkts.setStatus('current')
pfLabelBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelBytes.setStatus('current')
pfLabelInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelInPkts.setStatus('current')
pfLabelInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelInBytes.setStatus('current')
pfLabelOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelOutPkts.setStatus('current')
pfLabelOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelOutBytes.setStatus('current')
pfLabelTotalStates = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 1, 10, 128, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfLabelTotalStates.setStatus('current')
pfsyncIpPktsRecv = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncIpPktsRecv.setStatus('current')
pfsyncIp6PktsRecv = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncIp6PktsRecv.setStatus('current')
pfsyncPktDiscardsForBadInterface = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForBadInterface.setStatus('current')
pfsyncPktDiscardsForBadTtl = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForBadTtl.setStatus('current')
pfsyncPktShorterThanHeader = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktShorterThanHeader.setStatus('current')
pfsyncPktDiscardsForBadVersion = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForBadVersion.setStatus('current')
pfsyncPktDiscardsForBadAction = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForBadAction.setStatus('current')
pfsyncPktDiscardsForBadLength = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForBadLength.setStatus('current')
pfsyncPktDiscardsForBadAuth = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForBadAuth.setStatus('current')
pfsyncPktDiscardsForStaleState = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForStaleState.setStatus('current')
pfsyncPktDiscardsForBadValues = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForBadValues.setStatus('current')
pfsyncPktDiscardsForBadState = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncPktDiscardsForBadState.setStatus('current')
pfsyncIpPktsSent = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncIpPktsSent.setStatus('current')
pfsyncIp6PktsSent = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncIp6PktsSent.setStatus('current')
pfsyncNoMemory = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncNoMemory.setStatus('current')
pfsyncOutputErrors = MibScalar((1, 3, 6, 1, 4, 1, 30155, 1, 11, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pfsyncOutputErrors.setStatus('current')
mibBuilder.exportSymbols("OPENBSD-PF-MIB", pfIfTable=pfIfTable, pfInterfaces=pfInterfaces, pfHostid=pfHostid, pfTimeoutInterval=pfTimeoutInterval, pfLogIfIp6BytesOut=pfLogIfIp6BytesOut, pfTblAddrTable=pfTblAddrTable, pfStateTable=pfStateTable, pfCntSynproxy=pfCntSynproxy, pfIfIn4BlockBytes=pfIfIn4BlockBytes, pfTblEntry=pfTblEntry, pfLabelEvals=pfLabelEvals, pfTimeoutOtherSingle=pfTimeoutOtherSingle, pfCntTimestamp=pfCntTimestamp, pfTblNumber=pfTblNumber, pfCntIpOption=pfCntIpOption, pfTblName=pfTblName, pfTblInBlockBytes=pfTblInBlockBytes, pfStateSearches=pfStateSearches, pfIfOut4BlockPkts=pfIfOut4BlockPkts, pfTimeoutOtherMultiple=pfTimeoutOtherMultiple, pfRuntime=pfRuntime, pfLogIfIpPktsOutPass=pfLogIfIpPktsOutPass, pfLabelName=pfLabelName, pfIfOut6BlockBytes=pfIfOut6BlockBytes, pfTblOutMatchBytes=pfTblOutMatchBytes, pfTblInPassBytes=pfTblInPassBytes, pfLogIfIp6PktsOutDrop=pfLogIfIp6PktsOutDrop, pfsyncNoMemory=pfsyncNoMemory, pfsyncPktDiscardsForBadTtl=pfsyncPktDiscardsForBadTtl, pfLabelTotalStates=pfLabelTotalStates, pfIfRefs=pfIfRefs, pfLabelBytes=pfLabelBytes, pfLogIfIpBytesIn=pfLogIfIpBytesIn, pfTblAddrCleared=pfTblAddrCleared, pfLogIfIpPktsOutDrop=pfLogIfIpPktsOutDrop, pfTblIndex=pfTblIndex, pfLimitMaxTableEntries=pfLimitMaxTableEntries, pfIfOut6PassBytes=pfIfOut6PassBytes, pfLimitFragments=pfLimitFragments, pfsyncIpPktsSent=pfsyncIpPktsSent, pfIfIn6PassBytes=pfIfIn6PassBytes, pfTblEvalsNoMatch=pfTblEvalsNoMatch, pfCntStateInsert=pfCntStateInsert, pfStateCount=pfStateCount, pfCntStateLimit=pfCntStateLimit, pfTimeoutIcmpFirst=pfTimeoutIcmpFirst, pfIfIndex=pfIfIndex, pfTblOutBlockBytes=pfTblOutBlockBytes, pfSrcTrackInserts=pfSrcTrackInserts, pfLabelNumber=pfLabelNumber, pfTimeouts=pfTimeouts, pfTblAddrInMatchBytes=pfTblAddrInMatchBytes, pfSrcTrackRemovals=pfSrcTrackRemovals, pfTblTable=pfTblTable, pfTblAddrInPassPkts=pfTblAddrInPassPkts, pfDebug=pfDebug, pfTblAddrOutPassPkts=pfTblAddrOutPassPkts, pfTimeoutTcpClosed=pfTimeoutTcpClosed, pfLogIfIpPktsInDrop=pfLogIfIpPktsInDrop, pfTables=pfTables, pfIfType=pfIfType, pfTblInXPassPkts=pfTblInXPassPkts, pfsyncIp6PktsSent=pfsyncIp6PktsSent, pfTblAddrOutBlockBytes=pfTblAddrOutBlockBytes, pfIfIn4PassBytes=pfIfIn4PassBytes, pfTblAddrEntry=pfTblAddrEntry, pfLogIfName=pfLogIfName, pfTblInBlockPkts=pfTblInBlockPkts, pfLabels=pfLabels, pfIfNumber=pfIfNumber, pfsyncPktDiscardsForBadInterface=pfsyncPktDiscardsForBadInterface, pfTblAddresses=pfTblAddresses, pfsyncPktDiscardsForBadVersion=pfsyncPktDiscardsForBadVersion, pfLimitMaxTables=pfLimitMaxTables, pfTblAddrInMatchPkts=pfTblAddrInMatchPkts, pfTblAddrInBlockBytes=pfTblAddrInBlockBytes, pfIfOut4BlockBytes=pfIfOut4BlockBytes, pfCntProtoCksum=pfCntProtoCksum, pfTblInMatchBytes=pfTblInMatchBytes, pfIfIn6BlockPkts=pfIfIn6BlockPkts, pfTblAddrInBlockPkts=pfTblAddrInBlockPkts, pfSrcTrackCount=pfSrcTrackCount, pfsyncPktDiscardsForBadState=pfsyncPktDiscardsForBadState, pfIfIn4BlockPkts=pfIfIn4BlockPkts, pfTblOutPassPkts=pfTblOutPassPkts, pfTblEvalsMatch=pfTblEvalsMatch, pfLabelEntry=pfLabelEntry, pfIfIn4PassPkts=pfIfIn4PassPkts, pfIfRules=pfIfRules, pfTblInMatchPkts=pfTblInMatchPkts, pfTimeoutTcpOpening=pfTimeoutTcpOpening, pfCntMatch=pfCntMatch, pfCntBadOffset=pfCntBadOffset, pfCntShort=pfCntShort, pfSrcTrackSearches=pfSrcTrackSearches, pfLimitStates=pfLimitStates, pfTblAddrOutPassBytes=pfTblAddrOutPassBytes, pfTimeoutTcpFinWait=pfTimeoutTcpFinWait, pfRunning=pfRunning, PYSNMP_MODULE_ID=pfMIBObjects, pfLabelInPkts=pfLabelInPkts, pfsyncPktDiscardsForBadAction=pfsyncPktDiscardsForBadAction, pfCounters=pfCounters, pfTimeoutAdaptiveStart=pfTimeoutAdaptiveStart, pfsyncPktDiscardsForStaleState=pfsyncPktDiscardsForStaleState, pfTblAddrNet=pfTblAddrNet, pfLogIfIp6PktsInDrop=pfLogIfIp6PktsInDrop, pfTimeoutUdpFirst=pfTimeoutUdpFirst, pfsyncStats=pfsyncStats, pfLogIfIp6BytesIn=pfLogIfIp6BytesIn, pfLabelInBytes=pfLabelInBytes, pfTblOutMatchPkts=pfTblOutMatchPkts, pfsyncPktDiscardsForBadAuth=pfsyncPktDiscardsForBadAuth, pfIfOut4PassPkts=pfIfOut4PassPkts, pfMIBObjects=pfMIBObjects, pfLogIfIp6PktsInPass=pfLogIfIp6PktsInPass, pfLabelPkts=pfLabelPkts, pfsyncOutputErrors=pfsyncOutputErrors, pfLimitSourceNodes=pfLimitSourceNodes, pfIfIn6BlockBytes=pfIfIn6BlockBytes, pfIfOut6PassPkts=pfIfOut6PassPkts, pfLabelOutPkts=pfLabelOutPkts, pfStateInserts=pfStateInserts, pfLabelTable=pfLabelTable, pfTblOutBlockPkts=pfTblOutBlockPkts, pfCntStateMismatch=pfCntStateMismatch, pfTblAnchorRefs=pfTblAnchorRefs, pfCntTranslate=pfCntTranslate, pfIfOut6BlockPkts=pfIfOut6BlockPkts, pfCntCongestion=pfCntCongestion, pfTblStatsCleared=pfTblStatsCleared, pfLimits=pfLimits, pfTimeoutOtherFirst=pfTimeoutOtherFirst, pfTblAddrOutMatchPkts=pfTblAddrOutMatchPkts, pfTblInXPassBytes=pfTblInXPassBytes, pfCntNoRoute=pfCntNoRoute, pfIfOut4PassBytes=pfIfOut4PassBytes, pfsyncPktDiscardsForBadValues=pfsyncPktDiscardsForBadValues, pfLogInterface=pfLogInterface, pfTimeoutAdaptiveEnd=pfTimeoutAdaptiveEnd, pfTblAddrTblIndex=pfTblAddrTblIndex, pfCntMemory=pfCntMemory, pfTimeoutSrcTrack=pfTimeoutSrcTrack, pfTimeoutUdpMultiple=pfTimeoutUdpMultiple, pfTblOutPassBytes=pfTblOutPassBytes, pfTimeoutTcpEstablished=pfTimeoutTcpEstablished, pfTimeoutTcpFirst=pfTimeoutTcpFirst, pfTimeoutUdpSingle=pfTimeoutUdpSingle, pfStateRemovals=pfStateRemovals, pfIfEntry=pfIfEntry, pfCntNormalize=pfCntNormalize, pfLogIfIp6PktsOutPass=pfLogIfIp6PktsOutPass, pfTblRuleRefs=pfTblRuleRefs, pfTblOutXPassBytes=pfTblOutXPassBytes, pfTblAddrOutMatchBytes=pfTblAddrOutMatchBytes, pfCntSrcLimit=pfCntSrcLimit, pfSrcTracking=pfSrcTracking, pfsyncPktDiscardsForBadLength=pfsyncPktDiscardsForBadLength, pfTblAddrInPassBytes=pfTblAddrInPassBytes, pfLabelOutBytes=pfLabelOutBytes, pfCntFragment=pfCntFragment, pfsyncIp6PktsRecv=pfsyncIp6PktsRecv, pfTblInPassPkts=pfTblInPassPkts, pfLogIfIpBytesOut=pfLogIfIpBytesOut, pfTblAddrMask=pfTblAddrMask, pfTimeoutFragment=pfTimeoutFragment, pfTblOutXPassPkts=pfTblOutXPassPkts, pfTblAddrOutBlockPkts=pfTblAddrOutBlockPkts, pfInfo=pfInfo, pfsyncPktShorterThanHeader=pfsyncPktShorterThanHeader, pfTimeoutIcmpError=pfTimeoutIcmpError, pfLabelIndex=pfLabelIndex, pfTimeoutTcpClosing=pfTimeoutTcpClosing, pfsyncIpPktsRecv=pfsyncIpPktsRecv, pfLogIfIpPktsInPass=pfLogIfIpPktsInPass, pfIfIn6PassPkts=pfIfIn6PassPkts, pfIfDescr=pfIfDescr)
