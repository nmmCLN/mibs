#
# PySNMP MIB module ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:07:29 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSConformance, adGenAOSMef = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSMef")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
HCPerfTotalCount, HCPerfValidIntervals, HCPerfTimeElapsed, HCPerfInvalidIntervals, HCPerfIntervalCount, HCPerfCurrentCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfTotalCount", "HCPerfValidIntervals", "HCPerfTimeElapsed", "HCPerfInvalidIntervals", "HCPerfIntervalCount", "HCPerfCurrentCount")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, TimeTicks, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Bits, NotificationType, Counter32, Unsigned32, MibIdentifier, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Bits", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ADTRAN-MEF-PER-EVC-PERF-HISTORY-MIB", adMefPerEvcPh15MinEgressGreenOctetDiscards=adMefPerEvcPh15MinEgressGreenOctetDiscards, adMefPerEvcPh15MinIngressGreenFrameDiscards=adMefPerEvcPh15MinIngressGreenFrameDiscards, adGenAosMefPerEvcPerfHistory=adGenAosMefPerEvcPerfHistory, adMefPerEvcPh15MinEvcNameFixedLen=adMefPerEvcPh15MinEvcNameFixedLen, adMefPerEvcPh1DayEgressGreenFrames=adMefPerEvcPh1DayEgressGreenFrames, adMefPerEvcPhCurIngressGreenOctetDiscards1Day=adMefPerEvcPhCurIngressGreenOctetDiscards1Day, adMefPerEvcPh1DayEvcNameFixedLen=adMefPerEvcPh1DayEvcNameFixedLen, adMefPerEvcPhCurEntry=adMefPerEvcPhCurEntry, adMefPerEvcPhCurTable=adMefPerEvcPhCurTable, adMefPerEvcPhCurEvcNameFixedLen=adMefPerEvcPhCurEvcNameFixedLen, adMefPerEvcPhCurValidIntervals1Day=adMefPerEvcPhCurValidIntervals1Day, adMefPerEvcPhCurInvalidIntervals1Day=adMefPerEvcPhCurInvalidIntervals1Day, adMefPerEvcPh1DayIngressGreenOctetDiscards=adMefPerEvcPh1DayIngressGreenOctetDiscards, adMefPerEvcPh15MinIngressGreenFrames=adMefPerEvcPh15MinIngressGreenFrames, adMefPerEvcPhCurEgressGreenFrames15Min=adMefPerEvcPhCurEgressGreenFrames15Min, adMefPerEvcPh15MinEgressGreenFrameDiscards=adMefPerEvcPh15MinEgressGreenFrameDiscards, adMefPerEvcPhCurIngressGreenFrameDiscards1Day=adMefPerEvcPhCurIngressGreenFrameDiscards1Day, adMefPerEvcPhCurEgressGreenOctetDiscards15Min=adMefPerEvcPhCurEgressGreenOctetDiscards15Min, adMefPerEvcPhCurEgressGreenFrames1Day=adMefPerEvcPhCurEgressGreenFrames1Day, adMefPerEvcPh15MinIngressGreenOctets=adMefPerEvcPh15MinIngressGreenOctets, adMefPerEvcPh1DayIngressGreenFrames=adMefPerEvcPh1DayIngressGreenFrames, adMefPerEvcPh15MinIntervalGroup=adMefPerEvcPh15MinIntervalGroup, adMefPerEvcPh15MinIntervalNumber=adMefPerEvcPh15MinIntervalNumber, adMefPerEvcPhCurIngressGreenOctets1Day=adMefPerEvcPhCurIngressGreenOctets1Day, adMefPerEvcPhCurTimeElapsed15Min=adMefPerEvcPhCurTimeElapsed15Min, adMefPerEvcPh1DayIntervalEntry=adMefPerEvcPh1DayIntervalEntry, adMefPerEvcPh15MinEgressGreenFrames=adMefPerEvcPh15MinEgressGreenFrames, adGenAosMefPerEvcPerfHistoryConformance=adGenAosMefPerEvcPerfHistoryConformance, adMefPerEvcPhCurIngressGreenFrames15Min=adMefPerEvcPhCurIngressGreenFrames15Min, adMefPerEvcPh15MinIntervalEntry=adMefPerEvcPh15MinIntervalEntry, PYSNMP_MODULE_ID=adGenAosMefPerEvcPerfHistoryMib, adMefPerEvcPh1DayIngressGreenFrameDiscards=adMefPerEvcPh1DayIngressGreenFrameDiscards, adMefPerEvcPhCurEgressGreenFrameDiscards15Min=adMefPerEvcPhCurEgressGreenFrameDiscards15Min, adGenAosMefPerEvcPerfHistoryCompliances=adGenAosMefPerEvcPerfHistoryCompliances, adMefPerEvcPhCurIngressGreenOctetDiscards15Min=adMefPerEvcPhCurIngressGreenOctetDiscards15Min, adMefPerEvcPh15MinIntervalTable=adMefPerEvcPh15MinIntervalTable, adGenAosMefPerEvcPerfHistoryCompliance=adGenAosMefPerEvcPerfHistoryCompliance, adMefPerEvcPhCurValidIntervals15Min=adMefPerEvcPhCurValidIntervals15Min, adMefPerEvcPhCurGroup=adMefPerEvcPhCurGroup, adGenAosMefPerEvcPerfHistoryMib=adGenAosMefPerEvcPerfHistoryMib, adMefPerEvcPhCurEgressGreenOctetDiscards1Day=adMefPerEvcPhCurEgressGreenOctetDiscards1Day, adMefPerEvcPh1DayIntervalTable=adMefPerEvcPh1DayIntervalTable, adMefPerEvcPh1DayEgressGreenFrameDiscards=adMefPerEvcPh1DayEgressGreenFrameDiscards, adGenAosMefPerEvcPerfHistoryGroups=adGenAosMefPerEvcPerfHistoryGroups, adMefPerEvcPhCurEgressGreenOctets15Min=adMefPerEvcPhCurEgressGreenOctets15Min, adMefPerEvcPh15MinEgressGreenOctets=adMefPerEvcPh15MinEgressGreenOctets, adMefPerEvcPhCurIngressGreenOctets15Min=adMefPerEvcPhCurIngressGreenOctets15Min, adMefPerEvcPhCurEgressGreenOctets1Day=adMefPerEvcPhCurEgressGreenOctets1Day, adMefPerEvcPhCurEgressGreenFrameDiscards1Day=adMefPerEvcPhCurEgressGreenFrameDiscards1Day, adMefPerEvcPh1DayEgressGreenOctets=adMefPerEvcPh1DayEgressGreenOctets, adMefPerEvcPh1DayIntervalGroup=adMefPerEvcPh1DayIntervalGroup, adMefPerEvcPhCurIngressGreenFrames1Day=adMefPerEvcPhCurIngressGreenFrames1Day, adMefPerEvcPhCurIngressGreenFrameDiscards15Min=adMefPerEvcPhCurIngressGreenFrameDiscards15Min, adMefPerEvcPh15MinIngressGreenOctetDiscards=adMefPerEvcPh15MinIngressGreenOctetDiscards, adMefPerEvcPhCurTimeElapsed1Day=adMefPerEvcPhCurTimeElapsed1Day, adMefPerEvcPh1DayEgressGreenOctetDiscards=adMefPerEvcPh1DayEgressGreenOctetDiscards, adMefPerEvcPh1DayIngressGreenOctets=adMefPerEvcPh1DayIngressGreenOctets, adMefPerEvcPhCurInvalidIntervals15Min=adMefPerEvcPhCurInvalidIntervals15Min, adMefPerEvcPh1DayIntervalNumber=adMefPerEvcPh1DayIntervalNumber)
