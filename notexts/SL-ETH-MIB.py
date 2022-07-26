#
# PySNMP MIB module SL-ETH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ETH-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:38 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfTotalCount, PerfCurrentCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfCurrentCount", "PerfIntervalCount")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, NotificationType, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, TimeTicks, IpAddress, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "TimeTicks", "IpAddress", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter32")
TextualConvention, DateAndTime, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString", "TruthValue")
slEthernet = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1))
if mibBuilder.loadTexts: slEthernet.setLastUpdated('200508171200Z')
if mibBuilder.loadTexts: slEthernet.setOrganization('PacketLight Networks Ltd.')
ethTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 7))
ethConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1), )
if mibBuilder.loadTexts: ethConfigTable.setStatus('current')
ethConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1), ).setIndexNames((0, "SL-ETH-MIB", "ethLineIndex"))
if mibBuilder.loadTexts: ethConfigEntry.setStatus('current')
ethLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethLineIndex.setStatus('current')
ethTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTimeElapsed.setStatus('current')
ethValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethValidIntervals.setStatus('current')
ethResetPm = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethResetPm.setStatus('current')
ethAutoNegSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethAutoNegSupported.setStatus('current')
ethAutoNegAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethAutoNegAdminStatus.setStatus('current')
ethConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethConfigStatus.setStatus('current')
ethTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("base1000SX", 2), ("base1000LX", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTransceiverType.setStatus('current')
ethPauseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 16383))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethPauseTime.setStatus('current')
ethPauseEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethPauseEnable.setStatus('current')
ethResetPmCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethResetPmCounters.setStatus('current')
ethTransceiverMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("copper", 2), ("fiber", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethTransceiverMedia.setStatus('current')
ethCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2), )
if mibBuilder.loadTexts: ethCurrentTable.setStatus('current')
ethCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1), ).setIndexNames((0, "SL-ETH-MIB", "ethCurrentIndex"))
if mibBuilder.loadTexts: ethCurrentEntry.setStatus('current')
ethCurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentIndex.setStatus('current')
ethCurrentRxDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxDropEvents.setStatus('current')
ethCurrentOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentOctets.setStatus('current')
ethCurrentPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentPkts.setStatus('current')
ethCurrentBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentBroadcastPkts.setStatus('current')
ethCurrentMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentMulticastPkts.setStatus('current')
ethCurrentCRCAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentCRCAlignErrors.setStatus('current')
ethCurrentUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentUndersizePkts.setStatus('current')
ethCurrentOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentOversizePkts.setStatus('current')
ethCurrentFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentFragments.setStatus('current')
ethCurrentJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentJabbers.setStatus('current')
ethCurrentCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentCollisions.setStatus('current')
ethCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentUtilization.setStatus('current')
ethCurrentTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxOctets.setStatus('current')
ethCurrentTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPkts.setStatus('current')
ethCurrentRxPause = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxPause.setStatus('current')
ethCurrentTxPause = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPause.setStatus('current')
ethCurrentTxDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxDropEvents.setStatus('current')
ethCurrentRxPkts64Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxPkts64Octets.setStatus('current')
ethCurrentRxPkts65to127Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxPkts65to127Octets.setStatus('current')
ethCurrentRxPkts128to255Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxPkts128to255Octets.setStatus('current')
ethCurrentRxPkts256to511Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxPkts256to511Octets.setStatus('current')
ethCurrentRxPkts512to1023Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxPkts512to1023Octets.setStatus('current')
ethCurrentRxPkts1024to1518Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxPkts1024to1518Octets.setStatus('current')
ethCurrentRxPkts1519to1522Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxPkts1519to1522Octets.setStatus('current')
ethCurrentTxPkts64Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPkts64Octets.setStatus('current')
ethCurrentTxPkts65to127Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPkts65to127Octets.setStatus('current')
ethCurrentTxPkts128to255Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPkts128to255Octets.setStatus('current')
ethCurrentTxPkts256to511Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPkts256to511Octets.setStatus('current')
ethCurrentTxPkts512to1023Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPkts512to1023Octets.setStatus('current')
ethCurrentTxPkts1024to1518Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPkts1024to1518Octets.setStatus('current')
ethCurrentTxPkts1519to1522Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxPkts1519to1522Octets.setStatus('current')
ethCurrentRxVlanPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxVlanPkts.setStatus('current')
ethCurrentTxVlanPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxVlanPkts.setStatus('current')
ethCurrentRxJumboPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentRxJumboPkts.setStatus('current')
ethCurrentTxJumboPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 2, 1, 36), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethCurrentTxJumboPkts.setStatus('current')
ethIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3), )
if mibBuilder.loadTexts: ethIntervalTable.setStatus('current')
ethIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1), ).setIndexNames((0, "SL-ETH-MIB", "ethIntervalIndex"), (0, "SL-ETH-MIB", "ethIntervalNumber"))
if mibBuilder.loadTexts: ethIntervalEntry.setStatus('current')
ethIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalIndex.setStatus('current')
ethIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalNumber.setStatus('current')
ethIntervalDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalDropEvents.setStatus('current')
ethIntervalOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalOctets.setStatus('current')
ethIntervalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalPkts.setStatus('current')
ethIntervalBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalBroadcastPkts.setStatus('current')
ethIntervalMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalMulticastPkts.setStatus('current')
ethIntervalCRCAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalCRCAlignErrors.setStatus('current')
ethIntervalUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalUndersizePkts.setStatus('current')
ethIntervalOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalOversizePkts.setStatus('current')
ethIntervalFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalFragments.setStatus('current')
ethIntervalJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalJabbers.setStatus('current')
ethIntervalCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalCollisions.setStatus('current')
ethIntervalUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalUtilization.setStatus('current')
ethIntervalTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalTxOctets.setStatus('current')
ethIntervalTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalTxPkts.setStatus('current')
ethIntervalRxPause = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalRxPause.setStatus('current')
ethIntervalTxPause = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalTxPause.setStatus('current')
ethIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalValidData.setStatus('current')
ethIntervalTcaFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 3, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIntervalTcaFlag.setStatus('current')
ethTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4), )
if mibBuilder.loadTexts: ethTotalTable.setStatus('current')
ethTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1), ).setIndexNames((0, "SL-ETH-MIB", "ethTotalIndex"), (0, "SL-ETH-MIB", "ethTotalDayNumber"))
if mibBuilder.loadTexts: ethTotalEntry.setStatus('current')
ethTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalIndex.setStatus('current')
ethTotalDayNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 33)))
if mibBuilder.loadTexts: ethTotalDayNumber.setStatus('current')
ethTotalDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalDropEvents.setStatus('current')
ethTotalOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalOctets.setStatus('current')
ethTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalPkts.setStatus('current')
ethTotalBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalBroadcastPkts.setStatus('current')
ethTotalMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalMulticastPkts.setStatus('current')
ethTotalCRCAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalCRCAlignErrors.setStatus('current')
ethTotalUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalUndersizePkts.setStatus('current')
ethTotalOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalOversizePkts.setStatus('current')
ethTotalFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalFragments.setStatus('current')
ethTotalJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalJabbers.setStatus('current')
ethTotalCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalCollisions.setStatus('current')
ethTotalUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalUtilization.setStatus('current')
ethTotalTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalTxOctets.setStatus('current')
ethTotalTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalTxPkts.setStatus('current')
ethTotalRxPause = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalRxPause.setStatus('current')
ethTotalTxPause = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalTxPause.setStatus('current')
ethTotalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 4, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethTotalValidData.setStatus('current')
ethStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 1, 1, 7, 1)).setObjects(("SL-ETH-MIB", "ethLineIndex"), ("SL-ETH-MIB", "ethConfigStatus"))
if mibBuilder.loadTexts: ethStatusChange.setStatus('current')
mibBuilder.exportSymbols("SL-ETH-MIB", ethTotalDayNumber=ethTotalDayNumber, ethIntervalOctets=ethIntervalOctets, ethTotalBroadcastPkts=ethTotalBroadcastPkts, ethTimeElapsed=ethTimeElapsed, ethCurrentRxPkts1519to1522Octets=ethCurrentRxPkts1519to1522Octets, ethCurrentTxJumboPkts=ethCurrentTxJumboPkts, ethTotalMulticastPkts=ethTotalMulticastPkts, ethConfigStatus=ethConfigStatus, ethTotalTxPause=ethTotalTxPause, ethIntervalCollisions=ethIntervalCollisions, ethCurrentFragments=ethCurrentFragments, ethCurrentRxPkts1024to1518Octets=ethCurrentRxPkts1024to1518Octets, ethConfigTable=ethConfigTable, ethCurrentRxJumboPkts=ethCurrentRxJumboPkts, ethIntervalDropEvents=ethIntervalDropEvents, ethCurrentUndersizePkts=ethCurrentUndersizePkts, ethIntervalPkts=ethIntervalPkts, ethCurrentRxVlanPkts=ethCurrentRxVlanPkts, ethCurrentTxPkts65to127Octets=ethCurrentTxPkts65to127Octets, ethTransceiverMedia=ethTransceiverMedia, ethCurrentRxPkts512to1023Octets=ethCurrentRxPkts512to1023Octets, ethCurrentMulticastPkts=ethCurrentMulticastPkts, ethTotalDropEvents=ethTotalDropEvents, ethIntervalBroadcastPkts=ethIntervalBroadcastPkts, ethCurrentTxPkts1024to1518Octets=ethCurrentTxPkts1024to1518Octets, ethTotalUndersizePkts=ethTotalUndersizePkts, ethCurrentCollisions=ethCurrentCollisions, ethCurrentCRCAlignErrors=ethCurrentCRCAlignErrors, ethResetPm=ethResetPm, ethAutoNegSupported=ethAutoNegSupported, ethCurrentRxDropEvents=ethCurrentRxDropEvents, ethCurrentTxPkts256to511Octets=ethCurrentTxPkts256to511Octets, ethCurrentRxPause=ethCurrentRxPause, ethTotalTxOctets=ethTotalTxOctets, ethIntervalNumber=ethIntervalNumber, ethTotalJabbers=ethTotalJabbers, ethCurrentRxPkts64Octets=ethCurrentRxPkts64Octets, ethTotalCollisions=ethTotalCollisions, ethIntervalTxPkts=ethIntervalTxPkts, ethTotalTable=ethTotalTable, ethAutoNegAdminStatus=ethAutoNegAdminStatus, ethIntervalTable=ethIntervalTable, ethIntervalTxPause=ethIntervalTxPause, ethCurrentEntry=ethCurrentEntry, ethIntervalTcaFlag=ethIntervalTcaFlag, ethPauseEnable=ethPauseEnable, ethCurrentRxPkts65to127Octets=ethCurrentRxPkts65to127Octets, ethCurrentTxPkts64Octets=ethCurrentTxPkts64Octets, ethTotalFragments=ethTotalFragments, ethIntervalFragments=ethIntervalFragments, ethCurrentPkts=ethCurrentPkts, ethIntervalTxOctets=ethIntervalTxOctets, ethCurrentIndex=ethCurrentIndex, ethCurrentOversizePkts=ethCurrentOversizePkts, ethTotalTxPkts=ethTotalTxPkts, ethCurrentTxPkts=ethCurrentTxPkts, ethIntervalMulticastPkts=ethIntervalMulticastPkts, ethCurrentTxPkts128to255Octets=ethCurrentTxPkts128to255Octets, ethResetPmCounters=ethResetPmCounters, ethIntervalRxPause=ethIntervalRxPause, ethTotalEntry=ethTotalEntry, ethCurrentTxOctets=ethCurrentTxOctets, ethStatusChange=ethStatusChange, ethIntervalUtilization=ethIntervalUtilization, ethTotalValidData=ethTotalValidData, ethTotalUtilization=ethTotalUtilization, ethCurrentBroadcastPkts=ethCurrentBroadcastPkts, ethIntervalCRCAlignErrors=ethIntervalCRCAlignErrors, ethTotalOversizePkts=ethTotalOversizePkts, ethCurrentRxPkts128to255Octets=ethCurrentRxPkts128to255Octets, ethIntervalJabbers=ethIntervalJabbers, ethTraps=ethTraps, ethCurrentTxPkts1519to1522Octets=ethCurrentTxPkts1519to1522Octets, ethIntervalOversizePkts=ethIntervalOversizePkts, ethCurrentTxPause=ethCurrentTxPause, ethIntervalEntry=ethIntervalEntry, ethTotalIndex=ethTotalIndex, ethTotalOctets=ethTotalOctets, ethValidIntervals=ethValidIntervals, ethCurrentTxDropEvents=ethCurrentTxDropEvents, ethTotalCRCAlignErrors=ethTotalCRCAlignErrors, slEthernet=slEthernet, ethCurrentRxPkts256to511Octets=ethCurrentRxPkts256to511Octets, ethCurrentTxPkts512to1023Octets=ethCurrentTxPkts512to1023Octets, PYSNMP_MODULE_ID=slEthernet, ethConfigEntry=ethConfigEntry, ethIntervalIndex=ethIntervalIndex, ethIntervalUndersizePkts=ethIntervalUndersizePkts, ethCurrentOctets=ethCurrentOctets, ethTotalRxPause=ethTotalRxPause, ethTransceiverType=ethTransceiverType, ethIntervalValidData=ethIntervalValidData, ethCurrentTxVlanPkts=ethCurrentTxVlanPkts, ethLineIndex=ethLineIndex, ethPauseTime=ethPauseTime, ethCurrentUtilization=ethCurrentUtilization, ethCurrentJabbers=ethCurrentJabbers, ethCurrentTable=ethCurrentTable, ethTotalPkts=ethTotalPkts)
