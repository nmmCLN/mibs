#
# PySNMP MIB module ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:02:42 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSMef, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSMef", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
HCPerfInvalidIntervals, HCPerfCurrentCount, HCPerfValidIntervals, HCPerfIntervalCount, HCPerfTotalCount, HCPerfTimeElapsed = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfInvalidIntervals", "HCPerfCurrentCount", "HCPerfValidIntervals", "HCPerfIntervalCount", "HCPerfTotalCount", "HCPerfTimeElapsed")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Gauge32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress, Integer32, Counter64, TimeTicks, MibIdentifier, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress", "Integer32", "Counter64", "TimeTicks", "MibIdentifier", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAosMefPerEvcPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 3))
adGenAosMefPerEvcPerfHistoryMib.setRevisions(('2014-09-10 00:00',))
if mibBuilder.loadTexts: adGenAosMefPerEvcPerfHistoryMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAosMefPerEvcPerfHistoryMib.setOrganization('ADTRAN Inc.')
adGenAosMefPerEvcPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3))
adMefPerEvcPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1), )
if mibBuilder.loadTexts: adMefPerEvcPhCurTable.setStatus('current')
adMefPerEvcPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEvcNameFixedLen"))
if mibBuilder.loadTexts: adMefPerEvcPhCurEntry.setStatus('current')
adMefPerEvcPhCurEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerEvcPhCurEvcNameFixedLen.setStatus('current')
adMefPerEvcPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 2), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurTimeElapsed15Min.setStatus('current')
adMefPerEvcPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 3), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurValidIntervals15Min.setStatus('current')
adMefPerEvcPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 4), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurInvalidIntervals15Min.setStatus('current')
adMefPerEvcPhCurIngressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctets15Min.setStatus('current')
adMefPerEvcPhCurIngressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrames15Min.setStatus('current')
adMefPerEvcPhCurEgressGreenOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctets15Min.setStatus('current')
adMefPerEvcPhCurEgressGreenFrames15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrames15Min.setStatus('current')
adMefPerEvcPhCurIngressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrameDiscards15Min.setStatus('current')
adMefPerEvcPhCurEgressGreenFrameDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrameDiscards15Min.setStatus('current')
adMefPerEvcPhCurIngressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctetDiscards15Min.setStatus('current')
adMefPerEvcPhCurEgressGreenOctetDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 12), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctetDiscards15Min.setStatus('current')
adMefPerEvcPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 13), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurTimeElapsed1Day.setStatus('current')
adMefPerEvcPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 14), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurValidIntervals1Day.setStatus('current')
adMefPerEvcPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 15), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurInvalidIntervals1Day.setStatus('current')
adMefPerEvcPhCurIngressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 16), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctets1Day.setStatus('current')
adMefPerEvcPhCurIngressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 17), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrames1Day.setStatus('current')
adMefPerEvcPhCurEgressGreenOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 18), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctets1Day.setStatus('current')
adMefPerEvcPhCurEgressGreenFrames1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 19), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrames1Day.setStatus('current')
adMefPerEvcPhCurIngressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenFrameDiscards1Day.setStatus('current')
adMefPerEvcPhCurEgressGreenFrameDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenFrameDiscards1Day.setStatus('current')
adMefPerEvcPhCurIngressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurIngressGreenOctetDiscards1Day.setStatus('current')
adMefPerEvcPhCurEgressGreenOctetDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 1, 1, 23), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPhCurEgressGreenOctetDiscards1Day.setStatus('current')
adMefPerEvcPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2), )
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalTable.setStatus('current')
adMefPerEvcPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalEntry.setStatus('current')
adMefPerEvcPh15MinEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerEvcPh15MinEvcNameFixedLen.setStatus('current')
adMefPerEvcPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adMefPerEvcPh15MinIntervalNumber.setStatus('current')
adMefPerEvcPh15MinIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 3), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenOctets.setStatus('current')
adMefPerEvcPh15MinIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenFrames.setStatus('current')
adMefPerEvcPh15MinEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenOctets.setStatus('current')
adMefPerEvcPh15MinEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenFrames.setStatus('current')
adMefPerEvcPh15MinIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenFrameDiscards.setStatus('current')
adMefPerEvcPh15MinEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenFrameDiscards.setStatus('current')
adMefPerEvcPh15MinIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinIngressGreenOctetDiscards.setStatus('current')
adMefPerEvcPh15MinEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 2, 1, 10), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh15MinEgressGreenOctetDiscards.setStatus('current')
adMefPerEvcPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3), )
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalTable.setStatus('current')
adMefPerEvcPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1), ).setIndexNames((0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEvcNameFixedLen"), (0, "ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalEntry.setStatus('current')
adMefPerEvcPh1DayEvcNameFixedLen = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(50, 50)).setFixedLength(50))
if mibBuilder.loadTexts: adMefPerEvcPh1DayEvcNameFixedLen.setStatus('current')
adMefPerEvcPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adMefPerEvcPh1DayIntervalNumber.setStatus('current')
adMefPerEvcPh1DayIngressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 3), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenOctets.setStatus('current')
adMefPerEvcPh1DayIngressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenFrames.setStatus('current')
adMefPerEvcPh1DayEgressGreenOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenOctets.setStatus('current')
adMefPerEvcPh1DayEgressGreenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenFrames.setStatus('current')
adMefPerEvcPh1DayIngressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenFrameDiscards.setStatus('current')
adMefPerEvcPh1DayEgressGreenFrameDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenFrameDiscards.setStatus('current')
adMefPerEvcPh1DayIngressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayIngressGreenOctetDiscards.setStatus('current')
adMefPerEvcPh1DayEgressGreenOctetDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3, 3, 1, 10), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adMefPerEvcPh1DayEgressGreenOctetDiscards.setStatus('current')
adGenAosMefPerEvcPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23))
adGenAosMefPerEvcPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1))
adGenAosMefPerEvcPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 2))
adGenAosMefPerEvcPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 2, 1)).setObjects(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurGroup"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIntervalGroup"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosMefPerEvcPerfHistoryCompliance = adGenAosMefPerEvcPerfHistoryCompliance.setStatus('current')
adMefPerEvcPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 1)).setObjects(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurTimeElapsed15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurValidIntervals15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurInvalidIntervals15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctets15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrames15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctets15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrames15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrameDiscards15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctetDiscards15Min"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurTimeElapsed1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurValidIntervals1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurInvalidIntervals1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctets1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrames1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctets1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrames1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenFrameDiscards1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurIngressGreenOctetDiscards1Day"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPhCurEgressGreenOctetDiscards1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerEvcPhCurGroup = adMefPerEvcPhCurGroup.setStatus('current')
adMefPerEvcPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 2)).setObjects(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenOctets"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenFrames"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenOctets"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenFrames"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh15MinEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerEvcPh15MinIntervalGroup = adMefPerEvcPh15MinIntervalGroup.setStatus('current')
adMefPerEvcPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 23, 1, 3)).setObjects(("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenOctets"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenFrames"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenOctets"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenFrames"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenFrameDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenFrameDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayIngressGreenOctetDiscards"), ("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", "adMefPerEvcPh1DayEgressGreenOctetDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adMefPerEvcPh1DayIntervalGroup = adMefPerEvcPh1DayIntervalGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", adMefPerEvcPhCurInvalidIntervals1Day=adMefPerEvcPhCurInvalidIntervals1Day, adMefPerEvcPh15MinIngressGreenOctets=adMefPerEvcPh15MinIngressGreenOctets, adMefPerEvcPh15MinEgressGreenOctetDiscards=adMefPerEvcPh15MinEgressGreenOctetDiscards, adMefPerEvcPh15MinEgressGreenOctets=adMefPerEvcPh15MinEgressGreenOctets, adMefPerEvcPhCurValidIntervals1Day=adMefPerEvcPhCurValidIntervals1Day, adMefPerEvcPhCurTimeElapsed1Day=adMefPerEvcPhCurTimeElapsed1Day, adMefPerEvcPh1DayIntervalEntry=adMefPerEvcPh1DayIntervalEntry, adMefPerEvcPhCurEgressGreenOctetDiscards1Day=adMefPerEvcPhCurEgressGreenOctetDiscards1Day, adMefPerEvcPhCurInvalidIntervals15Min=adMefPerEvcPhCurInvalidIntervals15Min, adMefPerEvcPhCurEgressGreenFrameDiscards1Day=adMefPerEvcPhCurEgressGreenFrameDiscards1Day, adGenAosMefPerEvcPerfHistoryConformance=adGenAosMefPerEvcPerfHistoryConformance, adMefPerEvcPh1DayEvcNameFixedLen=adMefPerEvcPh1DayEvcNameFixedLen, adMefPerEvcPhCurIngressGreenOctetDiscards15Min=adMefPerEvcPhCurIngressGreenOctetDiscards15Min, adMefPerEvcPhCurIngressGreenFrames1Day=adMefPerEvcPhCurIngressGreenFrames1Day, adMefPerEvcPh1DayEgressGreenOctetDiscards=adMefPerEvcPh1DayEgressGreenOctetDiscards, adMefPerEvcPhCurValidIntervals15Min=adMefPerEvcPhCurValidIntervals15Min, adMefPerEvcPh15MinIntervalNumber=adMefPerEvcPh15MinIntervalNumber, adMefPerEvcPh15MinIngressGreenFrameDiscards=adMefPerEvcPh15MinIngressGreenFrameDiscards, adMefPerEvcPh15MinEgressGreenFrameDiscards=adMefPerEvcPh15MinEgressGreenFrameDiscards, adMefPerEvcPh1DayEgressGreenFrames=adMefPerEvcPh1DayEgressGreenFrames, adMefPerEvcPhCurGroup=adMefPerEvcPhCurGroup, adMefPerEvcPh1DayIngressGreenFrameDiscards=adMefPerEvcPh1DayIngressGreenFrameDiscards, adMefPerEvcPh15MinEvcNameFixedLen=adMefPerEvcPh15MinEvcNameFixedLen, adMefPerEvcPh15MinIngressGreenOctetDiscards=adMefPerEvcPh15MinIngressGreenOctetDiscards, adMefPerEvcPh15MinIntervalEntry=adMefPerEvcPh15MinIntervalEntry, adMefPerEvcPhCurEgressGreenOctets1Day=adMefPerEvcPhCurEgressGreenOctets1Day, adMefPerEvcPh1DayEgressGreenOctets=adMefPerEvcPh1DayEgressGreenOctets, adGenAosMefPerEvcPerfHistory=adGenAosMefPerEvcPerfHistory, adMefPerEvcPhCurEgressGreenOctetDiscards15Min=adMefPerEvcPhCurEgressGreenOctetDiscards15Min, adMefPerEvcPh1DayEgressGreenFrameDiscards=adMefPerEvcPh1DayEgressGreenFrameDiscards, adMefPerEvcPhCurEvcNameFixedLen=adMefPerEvcPhCurEvcNameFixedLen, adMefPerEvcPh15MinEgressGreenFrames=adMefPerEvcPh15MinEgressGreenFrames, adMefPerEvcPhCurEntry=adMefPerEvcPhCurEntry, adMefPerEvcPh15MinIntervalGroup=adMefPerEvcPh15MinIntervalGroup, adGenAosMefPerEvcPerfHistoryGroups=adGenAosMefPerEvcPerfHistoryGroups, adMefPerEvcPh1DayIntervalGroup=adMefPerEvcPh1DayIntervalGroup, adMefPerEvcPhCurIngressGreenFrames15Min=adMefPerEvcPhCurIngressGreenFrames15Min, adMefPerEvcPhCurTable=adMefPerEvcPhCurTable, adMefPerEvcPhCurEgressGreenOctets15Min=adMefPerEvcPhCurEgressGreenOctets15Min, adGenAosMefPerEvcPerfHistoryCompliance=adGenAosMefPerEvcPerfHistoryCompliance, PYSNMP_MODULE_ID=adGenAosMefPerEvcPerfHistoryMib, adGenAosMefPerEvcPerfHistoryMib=adGenAosMefPerEvcPerfHistoryMib, adMefPerEvcPh15MinIngressGreenFrames=adMefPerEvcPh15MinIngressGreenFrames, adMefPerEvcPh1DayIngressGreenOctets=adMefPerEvcPh1DayIngressGreenOctets, adMefPerEvcPhCurEgressGreenFrames1Day=adMefPerEvcPhCurEgressGreenFrames1Day, adMefPerEvcPhCurIngressGreenOctetDiscards1Day=adMefPerEvcPhCurIngressGreenOctetDiscards1Day, adMefPerEvcPh15MinIntervalTable=adMefPerEvcPh15MinIntervalTable, adGenAosMefPerEvcPerfHistoryCompliances=adGenAosMefPerEvcPerfHistoryCompliances, adMefPerEvcPh1DayIntervalNumber=adMefPerEvcPh1DayIntervalNumber, adMefPerEvcPhCurTimeElapsed15Min=adMefPerEvcPhCurTimeElapsed15Min, adMefPerEvcPhCurIngressGreenOctets1Day=adMefPerEvcPhCurIngressGreenOctets1Day, adMefPerEvcPh1DayIntervalTable=adMefPerEvcPh1DayIntervalTable, adMefPerEvcPhCurEgressGreenFrameDiscards15Min=adMefPerEvcPhCurEgressGreenFrameDiscards15Min, adMefPerEvcPhCurIngressGreenFrameDiscards1Day=adMefPerEvcPhCurIngressGreenFrameDiscards1Day, adMefPerEvcPh1DayIngressGreenOctetDiscards=adMefPerEvcPh1DayIngressGreenOctetDiscards, adMefPerEvcPhCurIngressGreenOctets15Min=adMefPerEvcPhCurIngressGreenOctets15Min, adMefPerEvcPhCurIngressGreenFrameDiscards15Min=adMefPerEvcPhCurIngressGreenFrameDiscards15Min, adMefPerEvcPhCurEgressGreenFrames15Min=adMefPerEvcPhCurEgressGreenFrames15Min, adMefPerEvcPh1DayIngressGreenFrames=adMefPerEvcPh1DayIngressGreenFrames)
