#
# PySNMP MIB module ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:15 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
HCPerfIntervalCount, HCPerfInvalidIntervals, HCPerfCurrentCount, HCPerfValidIntervals, HCPerfTotalCount, HCPerfTimeElapsed = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfIntervalCount", "HCPerfInvalidIntervals", "HCPerfCurrentCount", "HCPerfValidIntervals", "HCPerfTotalCount", "HCPerfTimeElapsed")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, ObjectIdentity, Bits, Counter64, NotificationType, ModuleIdentity, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "ObjectIdentity", "Bits", "Counter64", "NotificationType", "ModuleIdentity", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAosMefPerCosPerEvcPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 4))
adGenAosMefPerCosPerEvcPerfHistoryMib.setRevisions(('2014-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAosMefPerCosPerEvcPerfHistoryMib.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: adGenAosMefPerCosPerEvcPerfHistoryMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAosMefPerCosPerEvcPerfHistoryMib.setOrganization('ADTRAN Inc.')
if mibBuilder.loadTexts: adGenAosMefPerCosPerEvcPerfHistoryMib.setContactInfo('Info:   www.adtran.com\n      Postal: ADTRAN, Inc.\n              901 Explorer Blvd.\n              Huntsville, AL 35806\n      Tel:    +1 888 423-8726\n      E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAosMefPerCosPerEvcPerfHistoryMib.setDescription('This MIB module defines high capacity performance statistics\n      per COS per EVC within an AOS product.\n\n      Copyright (C) ADTRAN, Inc. (2014).')
adGenAosMefPerCosPerEvcPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4))
adMefPerCosPerEvcPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1), )
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTable.setDescription('This table contains current performance history information that has been\n      recorded since the last 15 minute interval ended and from when the last\n      1 day interval ended.  This table is indexed by adMefPerCosPerEvcPhCurEvcNameFixedLen \n      and the queue number.')
adMefPerCosPerEvcPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurQueueNumber"))
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEntry.setDescription("This specifies the information contained in one entry of the\n      adMefPerCosPerEvcPhCurTable.  It is indexed by an EVC's \n      adMefPerCosPerEvcPhCurEvcNameFixedLen and the queue number.")
adMefPerCosPerEvcPhCurEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEvcNameFixedLen.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEvcNameFixedLen.setDescription('The name of the EVC.  This string is padded at the end with 0x00 so that \n      this table index has a fixed length of characters of the specified SIZE.')
adMefPerCosPerEvcPhCurQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurQueueNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurQueueNumber.setDescription('NNI queue number.')
adMefPerCosPerEvcPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 3), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTimeElapsed15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTimeElapsed15Min.setDescription('Total elapsed seconds in the current 15 minute interval.')
adMefPerCosPerEvcPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 4), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurValidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurValidIntervals15Min.setDescription('Number of valid 15 minute intervals over the last 24 hours.')
adMefPerCosPerEvcPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 5), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurInvalidIntervals15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurInvalidIntervals15Min.setDescription('Number of invalid 15 minute intervals over the last 24 hours.')
adMefPerCosPerEvcPhCurIngressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctets15Min.setDescription('Count of ingress green octets in the current 15 minute interval.')
adMefPerCosPerEvcPhCurIngressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrames15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrames15Min.setDescription('Count of ingress green frames in the current 15 minute interval.')
adMefPerCosPerEvcPhCurEgressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctets15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctets15Min.setDescription('Count of egress green octets in the current 15 minute interval.')
adMefPerCosPerEvcPhCurEgressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrames15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrames15Min.setDescription('Count of egress green frames in the current 15 minute interval.')
adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min.setDescription('Count of ingress green frames discarded in the current 15 minute interval.')
adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min.setDescription('Count of egress green frames discarded in the current 15 minute interval.')
adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 12), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min.setDescription('Count of ingress green octets discarded in the current 15 minute interval.')
adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 13), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min.setDescription('Count of egress green octets discarded in the current 15 minute interval.')
adMefPerCosPerEvcPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 14), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTimeElapsed1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTimeElapsed1Day.setDescription('Total elapsed seconds in the current 1 day interval.')
adMefPerCosPerEvcPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 15), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurValidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurValidIntervals1Day.setDescription('Number of valid 1 day intervals available.')
adMefPerCosPerEvcPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 16), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurInvalidIntervals1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurInvalidIntervals1Day.setDescription('Number of invalid 1 day intervals available.')
adMefPerCosPerEvcPhCurIngressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 17), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctets1Day.setDescription('Count of ingress green octets in the current 1 day interval.')
adMefPerCosPerEvcPhCurIngressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 18), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrames1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrames1Day.setDescription('Count of ingress green frames in the current 1 day interval.')
adMefPerCosPerEvcPhCurEgressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 19), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctets1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctets1Day.setDescription('Count of egress green octets in the current 1 day interval.')
adMefPerCosPerEvcPhCurEgressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrames1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrames1Day.setDescription('Count of egress green frames in the current 1 day interval.')
adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day.setDescription('Count of ingress green frames discarded in the current 1 day interval.')
adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day.setDescription('Count of egress green frames discarded in the current 1 day interval.')
adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 23), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day.setDescription('Count of ingress green octets discarded in the current 1 day interval.')
adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 24), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day.setDescription('Count of egress green octets discarded in the current 1 day interval.')
adMefPerCosPerEvcPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2), )
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalTable.setDescription('This table contains performance history information for each valid 15\n      minute interval.  This table is indexed by adMefPerCosPerEvcPh15MinEvcNameFixedLen,\n      the queue number, and the interval number.')
adMefPerCosPerEvcPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinQueueNumber"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalEntry.setDescription('An entry in the adMefPerCosPerEvcPh15MinIntervalTable.')
adMefPerCosPerEvcPh15MinEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEvcNameFixedLen.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEvcNameFixedLen.setDescription('The name of the EVC.  This string is padded at the end with 0x00 so that \n      this table index has a fixed length of characters of the specified SIZE.')
adMefPerCosPerEvcPh15MinQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinQueueNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinQueueNumber.setDescription('NNI queue number.')
adMefPerCosPerEvcPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalNumber.setDescription('Performance history interval number.  Interval 1 is the most\n      recent previous interval; interval 96 is 24 hours ago.\n      Intervals 2..96 are optional.')
adMefPerCosPerEvcPh15MinIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenOctets.setDescription('Count of ingress green octets in the 15 minute interval.')
adMefPerCosPerEvcPh15MinIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenFrames.setDescription('Count of ingress green frames in the 15 minute interval.')
adMefPerCosPerEvcPh15MinEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenOctets.setDescription('Count of egress green octets in the 15 minute interval.')
adMefPerCosPerEvcPh15MinEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenFrames.setDescription('Count of egress green frames in the 15 minute interval.')
adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards.setDescription('Count of ingress green frames discarded in the 15 minute interval.')
adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards.setDescription('Count of egress green frames discarded in the 15 minute interval.')
adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 10), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards.setDescription('Count of ingress green octets discarded in the 15 minute interval.')
adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 11), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards.setDescription('Count of egress green octets discarded in the 15 minute interval.')
adMefPerCosPerEvcPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3), )
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalTable.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalTable.setDescription('This table contains performance history information for each valid 1\n      day interval.  This table is indexed by adMefPerCosPerEvcPh1DayEvcNameFixedLen,\n      the queue number, and the interval number.')
adMefPerCosPerEvcPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayQueueNumber"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalEntry.setDescription('An entry in the adMefPerCosPerEvcPh1DayIntervalTable.')
adMefPerCosPerEvcPh1DayEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEvcNameFixedLen.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEvcNameFixedLen.setDescription('The name of the EVC.  This string is padded at the end with 0x00 so that \n      this table index has a fixed length of characters of the specified SIZE.')
adMefPerCosPerEvcPh1DayQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayQueueNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayQueueNumber.setDescription('NNI queue number.')
adMefPerCosPerEvcPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalNumber.setDescription('Performance history interval number.  Interval 1 is the most recent\n      previous day; interval 7 is 7 days ago.  Intervals 2..30 are optional.')
adMefPerCosPerEvcPh1DayIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenOctets.setDescription('Count of ingress green octets in the 1 day interval.')
adMefPerCosPerEvcPh1DayIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenFrames.setDescription('Count of ingress green frames in the 1 day interval.')
adMefPerCosPerEvcPh1DayEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenOctets.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenOctets.setDescription('Count of egress green octets in the 1 day interval.')
adMefPerCosPerEvcPh1DayEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenFrames.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenFrames.setDescription('Count of egress green frames in the 1 day interval.')
adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards.setDescription('Count of ingress green frames discarded in the 1 day interval.')
adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards.setDescription('Count of egress green frames discarded in the 1 day interval.')
adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 10), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards.setDescription('Count of ingress green octets discarded in the 1 day interval.')
adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 11), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards.setDescription('Count of egress green octets discarded in the 1 day interval.')
adGenAosMefPerCosPerEvcPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24))
adGenAosMefPerCosPerEvcPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1))
adGenAosMefPerCosPerEvcPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 2))
adGenAosMefPerCosPerEvcPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 2, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurGroup"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIntervalGroup"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerCosPerEvcPerfHistoryCompliance = adGenAosMefPerCosPerEvcPerfHistoryCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAosMefPerCosPerEvcPerfHistoryCompliance.setDescription('The compliance statement for SNMPv2 entities which\n      implement UNI interface per-queue performance history.')
adMefPerCosPerEvcPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurTimeElapsed15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurValidIntervals15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurInvalidIntervals15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctets15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrames15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctets15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrames15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurTimeElapsed1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurValidIntervals1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurInvalidIntervals1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctets1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrames1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctets1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrames1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerEvcPhCurGroup = adMefPerCosPerEvcPhCurGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurGroup.setDescription('The Current Group.')
adMefPerCosPerEvcPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 2)).setObjects(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerEvcPh15MinIntervalGroup = adMefPerCosPerEvcPh15MinIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalGroup.setDescription('The 15 minute interval group.')
adMefPerCosPerEvcPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 3)).setObjects(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerEvcPh1DayIntervalGroup = adMefPerCosPerEvcPh1DayIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalGroup.setDescription('The 1 day interval group.')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards=adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards, adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min=adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min, adMefPerCosPerEvcPhCurEgressGreenOctets15Min=adMefPerCosPerEvcPhCurEgressGreenOctets15Min, adMefPerCosPerEvcPhCurEntry=adMefPerCosPerEvcPhCurEntry, adMefPerCosPerEvcPhCurEgressGreenFrames1Day=adMefPerCosPerEvcPhCurEgressGreenFrames1Day, adMefPerCosPerEvcPh15MinIngressGreenFrames=adMefPerCosPerEvcPh15MinIngressGreenFrames, adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards=adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards, adMefPerCosPerEvcPhCurIngressGreenFrames1Day=adMefPerCosPerEvcPhCurIngressGreenFrames1Day, adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards=adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards, adMefPerCosPerEvcPh1DayIngressGreenFrames=adMefPerCosPerEvcPh1DayIngressGreenFrames, adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards=adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards, adMefPerCosPerEvcPhCurTable=adMefPerCosPerEvcPhCurTable, adMefPerCosPerEvcPh15MinQueueNumber=adMefPerCosPerEvcPh15MinQueueNumber, adMefPerCosPerEvcPh15MinEgressGreenOctets=adMefPerCosPerEvcPh15MinEgressGreenOctets, adMefPerCosPerEvcPhCurEgressGreenFrames15Min=adMefPerCosPerEvcPhCurEgressGreenFrames15Min, adMefPerCosPerEvcPhCurInvalidIntervals1Day=adMefPerCosPerEvcPhCurInvalidIntervals1Day, adMefPerCosPerEvcPhCurTimeElapsed15Min=adMefPerCosPerEvcPhCurTimeElapsed15Min, adMefPerCosPerEvcPh1DayIngressGreenOctets=adMefPerCosPerEvcPh1DayIngressGreenOctets, adMefPerCosPerEvcPh1DayEvcNameFixedLen=adMefPerCosPerEvcPh1DayEvcNameFixedLen, adMefPerCosPerEvcPh1DayQueueNumber=adMefPerCosPerEvcPh1DayQueueNumber, adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min=adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min, adGenAosMefPerCosPerEvcPerfHistoryCompliances=adGenAosMefPerCosPerEvcPerfHistoryCompliances, adMefPerCosPerEvcPh15MinIntervalGroup=adMefPerCosPerEvcPh15MinIntervalGroup, adMefPerCosPerEvcPh15MinIntervalNumber=adMefPerCosPerEvcPh15MinIntervalNumber, adMefPerCosPerEvcPh15MinIngressGreenOctets=adMefPerCosPerEvcPh15MinIngressGreenOctets, adMefPerCosPerEvcPh1DayEgressGreenOctets=adMefPerCosPerEvcPh1DayEgressGreenOctets, adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards=adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards, adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min=adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min, adMefPerCosPerEvcPhCurEvcNameFixedLen=adMefPerCosPerEvcPhCurEvcNameFixedLen, adMefPerCosPerEvcPh1DayIntervalTable=adMefPerCosPerEvcPh1DayIntervalTable, PYSNMP_MODULE_ID=adGenAosMefPerCosPerEvcPerfHistoryMib, adMefPerCosPerEvcPh15MinIntervalTable=adMefPerCosPerEvcPh15MinIntervalTable, adGenAosMefPerCosPerEvcPerfHistoryGroups=adGenAosMefPerCosPerEvcPerfHistoryGroups, adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day=adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day, adMefPerCosPerEvcPh1DayIntervalEntry=adMefPerCosPerEvcPh1DayIntervalEntry, adMefPerCosPerEvcPh1DayIntervalNumber=adMefPerCosPerEvcPh1DayIntervalNumber, adMefPerCosPerEvcPh1DayEgressGreenFrames=adMefPerCosPerEvcPh1DayEgressGreenFrames, adMefPerCosPerEvcPhCurIngressGreenOctets1Day=adMefPerCosPerEvcPhCurIngressGreenOctets1Day, adMefPerCosPerEvcPhCurTimeElapsed1Day=adMefPerCosPerEvcPhCurTimeElapsed1Day, adMefPerCosPerEvcPhCurEgressGreenOctets1Day=adMefPerCosPerEvcPhCurEgressGreenOctets1Day, adMefPerCosPerEvcPhCurGroup=adMefPerCosPerEvcPhCurGroup, adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards=adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards, adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day=adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day, adMefPerCosPerEvcPhCurIngressGreenFrames15Min=adMefPerCosPerEvcPhCurIngressGreenFrames15Min, adGenAosMefPerCosPerEvcPerfHistory=adGenAosMefPerCosPerEvcPerfHistory, adMefPerCosPerEvcPh15MinIntervalEntry=adMefPerCosPerEvcPh15MinIntervalEntry, adMefPerCosPerEvcPhCurIngressGreenOctets15Min=adMefPerCosPerEvcPhCurIngressGreenOctets15Min, adGenAosMefPerCosPerEvcPerfHistoryCompliance=adGenAosMefPerCosPerEvcPerfHistoryCompliance, adMefPerCosPerEvcPh15MinEvcNameFixedLen=adMefPerCosPerEvcPh15MinEvcNameFixedLen, adMefPerCosPerEvcPh15MinEgressGreenFrames=adMefPerCosPerEvcPh15MinEgressGreenFrames, adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards=adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards, adMefPerCosPerEvcPhCurQueueNumber=adMefPerCosPerEvcPhCurQueueNumber, adMefPerCosPerEvcPhCurValidIntervals15Min=adMefPerCosPerEvcPhCurValidIntervals15Min, adGenAosMefPerCosPerEvcPerfHistoryMib=adGenAosMefPerCosPerEvcPerfHistoryMib, adGenAosMefPerCosPerEvcPerfHistoryConformance=adGenAosMefPerCosPerEvcPerfHistoryConformance, adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards=adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards, adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day=adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day, adMefPerCosPerEvcPhCurValidIntervals1Day=adMefPerCosPerEvcPhCurValidIntervals1Day, adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min=adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min, adMefPerCosPerEvcPh1DayIntervalGroup=adMefPerCosPerEvcPh1DayIntervalGroup, adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day=adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day, adMefPerCosPerEvcPhCurInvalidIntervals15Min=adMefPerCosPerEvcPhCurInvalidIntervals15Min)
