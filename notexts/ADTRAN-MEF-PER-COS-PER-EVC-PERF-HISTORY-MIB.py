#
# PySNMP MIB module ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:20 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
HCPerfInvalidIntervals, HCPerfTimeElapsed, HCPerfCurrentCount, HCPerfValidIntervals, HCPerfTotalCount, HCPerfIntervalCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfInvalidIntervals", "HCPerfTimeElapsed", "HCPerfCurrentCount", "HCPerfValidIntervals", "HCPerfTotalCount", "HCPerfIntervalCount")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, IpAddress, MibIdentifier, ModuleIdentity, TimeTicks, ObjectIdentity, NotificationType, Counter32, Counter64, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter32", "Counter64", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAosMefPerCosPerEvcPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 4))
adGenAosMefPerCosPerEvcPerfHistoryMib.setRevisions(('2014-09-10 00:00',))
if mibBuilder.loadTexts: adGenAosMefPerCosPerEvcPerfHistoryMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAosMefPerCosPerEvcPerfHistoryMib.setOrganization('ADTRAN Inc.')
adGenAosMefPerCosPerEvcPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4))
adMefPerCosPerEvcPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1), )
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTable.setStatus('current')
adMefPerCosPerEvcPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurQueueNumber"))
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEntry.setStatus('current')
adMefPerCosPerEvcPhCurEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEvcNameFixedLen.setStatus('current')
adMefPerCosPerEvcPhCurQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurQueueNumber.setStatus('current')
adMefPerCosPerEvcPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 3), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTimeElapsed15Min.setStatus('current')
adMefPerCosPerEvcPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 4), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurValidIntervals15Min.setStatus('current')
adMefPerCosPerEvcPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 5), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurInvalidIntervals15Min.setStatus('current')
adMefPerCosPerEvcPhCurIngressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctets15Min.setStatus('current')
adMefPerCosPerEvcPhCurIngressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrames15Min.setStatus('current')
adMefPerCosPerEvcPhCurEgressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctets15Min.setStatus('current')
adMefPerCosPerEvcPhCurEgressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrames15Min.setStatus('current')
adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min.setStatus('current')
adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min.setStatus('current')
adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 12), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min.setStatus('current')
adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 13), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min.setStatus('current')
adMefPerCosPerEvcPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 14), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurTimeElapsed1Day.setStatus('current')
adMefPerCosPerEvcPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 15), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurValidIntervals1Day.setStatus('current')
adMefPerCosPerEvcPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 16), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurInvalidIntervals1Day.setStatus('current')
adMefPerCosPerEvcPhCurIngressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 17), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctets1Day.setStatus('current')
adMefPerCosPerEvcPhCurIngressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 18), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrames1Day.setStatus('current')
adMefPerCosPerEvcPhCurEgressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 19), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctets1Day.setStatus('current')
adMefPerCosPerEvcPhCurEgressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrames1Day.setStatus('current')
adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day.setStatus('current')
adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day.setStatus('current')
adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 23), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day.setStatus('current')
adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 1, 1, 24), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day.setStatus('current')
adMefPerCosPerEvcPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2), )
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalTable.setStatus('current')
adMefPerCosPerEvcPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinQueueNumber"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalEntry.setStatus('current')
adMefPerCosPerEvcPh15MinEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEvcNameFixedLen.setStatus('current')
adMefPerCosPerEvcPh15MinQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinQueueNumber.setStatus('current')
adMefPerCosPerEvcPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIntervalNumber.setStatus('current')
adMefPerCosPerEvcPh15MinIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenOctets.setStatus('current')
adMefPerCosPerEvcPh15MinIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenFrames.setStatus('current')
adMefPerCosPerEvcPh15MinEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenOctets.setStatus('current')
adMefPerCosPerEvcPh15MinEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenFrames.setStatus('current')
adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards.setStatus('current')
adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards.setStatus('current')
adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 10), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards.setStatus('current')
adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 2, 1, 11), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards.setStatus('current')
adMefPerCosPerEvcPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3), )
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalTable.setStatus('current')
adMefPerCosPerEvcPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayQueueNumber"), (0, "ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalEntry.setStatus('current')
adMefPerCosPerEvcPh1DayEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEvcNameFixedLen.setStatus('current')
adMefPerCosPerEvcPh1DayQueueNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayQueueNumber.setStatus('current')
adMefPerCosPerEvcPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIntervalNumber.setStatus('current')
adMefPerCosPerEvcPh1DayIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenOctets.setStatus('current')
adMefPerCosPerEvcPh1DayIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenFrames.setStatus('current')
adMefPerCosPerEvcPh1DayEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenOctets.setStatus('current')
adMefPerCosPerEvcPh1DayEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenFrames.setStatus('current')
adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards.setStatus('current')
adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards.setStatus('current')
adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 10), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards.setStatus('current')
adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4, 3, 1, 11), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards.setStatus('current')
adGenAosMefPerCosPerEvcPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24))
adGenAosMefPerCosPerEvcPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1))
adGenAosMefPerCosPerEvcPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 2))
adGenAosMefPerCosPerEvcPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 2, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurGroup"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIntervalGroup"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerCosPerEvcPerfHistoryCompliance = adGenAosMefPerCosPerEvcPerfHistoryCompliance.setStatus('current')
adMefPerCosPerEvcPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 1)).setObjects(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurTimeElapsed15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurValidIntervals15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurInvalidIntervals15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctets15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrames15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctets15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrames15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurTimeElapsed1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurValidIntervals1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurInvalidIntervals1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctets1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrames1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctets1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrames1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerEvcPhCurGroup = adMefPerCosPerEvcPhCurGroup.setStatus('current')
adMefPerCosPerEvcPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 2)).setObjects(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerEvcPh15MinIntervalGroup = adMefPerCosPerEvcPh15MinIntervalGroup.setStatus('current')
adMefPerCosPerEvcPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 24, 1, 3)).setObjects(("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenOctets"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenFrames"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", "adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerCosPerEvcPh1DayIntervalGroup = adMefPerCosPerEvcPh1DayIntervalGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-COS-PER-EVC-PERF-HISTORY-MIB", adMefPerCosPerEvcPh1DayIntervalNumber=adMefPerCosPerEvcPh1DayIntervalNumber, adMefPerCosPerEvcPhCurValidIntervals15Min=adMefPerCosPerEvcPhCurValidIntervals15Min, adGenAosMefPerCosPerEvcPerfHistoryMib=adGenAosMefPerCosPerEvcPerfHistoryMib, adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min=adMefPerCosPerEvcPhCurEgressGreenFrameDiscards15Min, adMefPerCosPerEvcPh1DayQueueNumber=adMefPerCosPerEvcPh1DayQueueNumber, adMefPerCosPerEvcPhCurTimeElapsed15Min=adMefPerCosPerEvcPhCurTimeElapsed15Min, adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day=adMefPerCosPerEvcPhCurIngressGreenOctetDiscards1Day, adMefPerCosPerEvcPh15MinEvcNameFixedLen=adMefPerCosPerEvcPh15MinEvcNameFixedLen, adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day=adMefPerCosPerEvcPhCurEgressGreenOctetDiscards1Day, adMefPerCosPerEvcPhCurIngressGreenOctets1Day=adMefPerCosPerEvcPhCurIngressGreenOctets1Day, adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards=adMefPerCosPerEvcPh1DayEgressGreenFrameDiscards, adMefPerCosPerEvcPhCurQueueNumber=adMefPerCosPerEvcPhCurQueueNumber, adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min=adMefPerCosPerEvcPhCurEgressGreenOctetDiscards15Min, adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards=adMefPerCosPerEvcPh1DayIngressGreenFrameDiscards, adMefPerCosPerEvcPh1DayIntervalGroup=adMefPerCosPerEvcPh1DayIntervalGroup, adGenAosMefPerCosPerEvcPerfHistory=adGenAosMefPerCosPerEvcPerfHistory, adMefPerCosPerEvcPh15MinIntervalEntry=adMefPerCosPerEvcPh15MinIntervalEntry, adMefPerCosPerEvcPh1DayIntervalTable=adMefPerCosPerEvcPh1DayIntervalTable, adMefPerCosPerEvcPhCurEgressGreenOctets1Day=adMefPerCosPerEvcPhCurEgressGreenOctets1Day, adMefPerCosPerEvcPhCurIngressGreenFrames15Min=adMefPerCosPerEvcPhCurIngressGreenFrames15Min, adMefPerCosPerEvcPhCurInvalidIntervals15Min=adMefPerCosPerEvcPhCurInvalidIntervals15Min, adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards=adMefPerCosPerEvcPh15MinEgressGreenFrameDiscards, adMefPerCosPerEvcPhCurValidIntervals1Day=adMefPerCosPerEvcPhCurValidIntervals1Day, adMefPerCosPerEvcPhCurEntry=adMefPerCosPerEvcPhCurEntry, adMefPerCosPerEvcPhCurIngressGreenOctets15Min=adMefPerCosPerEvcPhCurIngressGreenOctets15Min, adMefPerCosPerEvcPh1DayEgressGreenOctets=adMefPerCosPerEvcPh1DayEgressGreenOctets, adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min=adMefPerCosPerEvcPhCurIngressGreenOctetDiscards15Min, adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day=adMefPerCosPerEvcPhCurEgressGreenFrameDiscards1Day, adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min=adMefPerCosPerEvcPhCurIngressGreenFrameDiscards15Min, adMefPerCosPerEvcPh1DayIntervalEntry=adMefPerCosPerEvcPh1DayIntervalEntry, adGenAosMefPerCosPerEvcPerfHistoryGroups=adGenAosMefPerCosPerEvcPerfHistoryGroups, adMefPerCosPerEvcPhCurTimeElapsed1Day=adMefPerCosPerEvcPhCurTimeElapsed1Day, adGenAosMefPerCosPerEvcPerfHistoryConformance=adGenAosMefPerCosPerEvcPerfHistoryConformance, adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards=adMefPerCosPerEvcPh15MinIngressGreenOctetDiscards, adMefPerCosPerEvcPh1DayIngressGreenFrames=adMefPerCosPerEvcPh1DayIngressGreenFrames, adMefPerCosPerEvcPh15MinQueueNumber=adMefPerCosPerEvcPh15MinQueueNumber, adMefPerCosPerEvcPh1DayEvcNameFixedLen=adMefPerCosPerEvcPh1DayEvcNameFixedLen, adGenAosMefPerCosPerEvcPerfHistoryCompliances=adGenAosMefPerCosPerEvcPerfHistoryCompliances, adMefPerCosPerEvcPhCurEgressGreenFrames1Day=adMefPerCosPerEvcPhCurEgressGreenFrames1Day, adMefPerCosPerEvcPh1DayEgressGreenFrames=adMefPerCosPerEvcPh1DayEgressGreenFrames, adMefPerCosPerEvcPhCurEgressGreenFrames15Min=adMefPerCosPerEvcPhCurEgressGreenFrames15Min, adMefPerCosPerEvcPh15MinIngressGreenFrames=adMefPerCosPerEvcPh15MinIngressGreenFrames, adMefPerCosPerEvcPh15MinIngressGreenOctets=adMefPerCosPerEvcPh15MinIngressGreenOctets, adMefPerCosPerEvcPh15MinIntervalNumber=adMefPerCosPerEvcPh15MinIntervalNumber, adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards=adMefPerCosPerEvcPh15MinIngressGreenFrameDiscards, adGenAosMefPerCosPerEvcPerfHistoryCompliance=adGenAosMefPerCosPerEvcPerfHistoryCompliance, adMefPerCosPerEvcPhCurGroup=adMefPerCosPerEvcPhCurGroup, PYSNMP_MODULE_ID=adGenAosMefPerCosPerEvcPerfHistoryMib, adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day=adMefPerCosPerEvcPhCurIngressGreenFrameDiscards1Day, adMefPerCosPerEvcPh15MinEgressGreenOctets=adMefPerCosPerEvcPh15MinEgressGreenOctets, adMefPerCosPerEvcPh15MinIntervalGroup=adMefPerCosPerEvcPh15MinIntervalGroup, adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards=adMefPerCosPerEvcPh15MinEgressGreenOctetDiscards, adMefPerCosPerEvcPh15MinIntervalTable=adMefPerCosPerEvcPh15MinIntervalTable, adMefPerCosPerEvcPh1DayIngressGreenOctets=adMefPerCosPerEvcPh1DayIngressGreenOctets, adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards=adMefPerCosPerEvcPh1DayIngressGreenOctetDiscards, adMefPerCosPerEvcPhCurEgressGreenOctets15Min=adMefPerCosPerEvcPhCurEgressGreenOctets15Min, adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards=adMefPerCosPerEvcPh1DayEgressGreenOctetDiscards, adMefPerCosPerEvcPhCurInvalidIntervals1Day=adMefPerCosPerEvcPhCurInvalidIntervals1Day, adMefPerCosPerEvcPh15MinEgressGreenFrames=adMefPerCosPerEvcPh15MinEgressGreenFrames, adMefPerCosPerEvcPhCurIngressGreenFrames1Day=adMefPerCosPerEvcPhCurIngressGreenFrames1Day, adMefPerCosPerEvcPhCurTable=adMefPerCosPerEvcPhCurTable, adMefPerCosPerEvcPhCurEvcNameFixedLen=adMefPerCosPerEvcPhCurEvcNameFixedLen)
