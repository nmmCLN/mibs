#
# PySNMP MIB module ADTRAN-IF-PERF-HISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-IF-PERF-HISTORY-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:13 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
HCPerfValidIntervals, HCPerfInvalidIntervals, HCPerfTimeElapsed, HCPerfTotalCount, HCPerfIntervalCount, HCPerfCurrentCount = mibBuilder.importSymbols("HC-PerfHist-TC-MIB", "HCPerfValidIntervals", "HCPerfInvalidIntervals", "HCPerfTimeElapsed", "HCPerfTotalCount", "HCPerfIntervalCount", "HCPerfCurrentCount")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, IpAddress, Bits, Counter32, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Unsigned32, ObjectIdentity, ModuleIdentity, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Bits", "Counter32", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAosIfPerfHistoryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 7))
adGenAosIfPerfHistoryMib.setRevisions(('2013-08-23 00:00',))
if mibBuilder.loadTexts: adGenAosIfPerfHistoryMib.setLastUpdated('201308230000Z')
if mibBuilder.loadTexts: adGenAosIfPerfHistoryMib.setOrganization('ADTRAN Inc.')
adGenAosIfPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7))
adIfPhCurTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1), )
if mibBuilder.loadTexts: adIfPhCurTable.setStatus('current')
adIfPhCurEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adIfPhCurEntry.setStatus('current')
adIfPhCurTimeElapsed15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 1), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurTimeElapsed15Min.setStatus('current')
adIfPhCurValidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 2), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurValidIntervals15Min.setStatus('current')
adIfPhCurInvalidIntervals15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 3), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInvalidIntervals15Min.setStatus('current')
adIfPhCurInOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 4), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInOctets15Min.setStatus('current')
adIfPhCurInUcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 5), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInUcastPkts15Min.setStatus('current')
adIfPhCurInMcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 6), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInMcastPkts15Min.setStatus('current')
adIfPhCurInBcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 7), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInBcastPkts15Min.setStatus('current')
adIfPhCurInDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 8), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInDiscards15Min.setStatus('current')
adIfPhCurInErrors15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 9), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInErrors15Min.setStatus('current')
adIfPhCurInUnknownProtos15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 10), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInUnknownProtos15Min.setStatus('current')
adIfPhCurOutOctets15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 11), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutOctets15Min.setStatus('current')
adIfPhCurOutUcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 12), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutUcastPkts15Min.setStatus('current')
adIfPhCurOutMcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 13), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutMcastPkts15Min.setStatus('current')
adIfPhCurOutBcastPkts15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 14), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutBcastPkts15Min.setStatus('current')
adIfPhCurOutDiscards15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 15), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutDiscards15Min.setStatus('current')
adIfPhCurOutErrors15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 16), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutErrors15Min.setStatus('current')
adIfPhCurTimeElapsed1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 17), HCPerfTimeElapsed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurTimeElapsed1Day.setStatus('current')
adIfPhCurValidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 18), HCPerfValidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurValidIntervals1Day.setStatus('current')
adIfPhCurInvalidIntervals1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 19), HCPerfInvalidIntervals()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInvalidIntervals1Day.setStatus('current')
adIfPhCurInOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 20), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInOctets1Day.setStatus('current')
adIfPhCurInUcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 21), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInUcastPkts1Day.setStatus('current')
adIfPhCurInMcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 22), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInMcastPkts1Day.setStatus('current')
adIfPhCurInBcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 23), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInBcastPkts1Day.setStatus('current')
adIfPhCurInDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 24), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInDiscards1Day.setStatus('current')
adIfPhCurInErrors1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 25), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInErrors1Day.setStatus('current')
adIfPhCurInUnknownProtos1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 26), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurInUnknownProtos1Day.setStatus('current')
adIfPhCurOutOctets1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 27), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutOctets1Day.setStatus('current')
adIfPhCurOutUcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 28), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutUcastPkts1Day.setStatus('current')
adIfPhCurOutMcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 29), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutMcastPkts1Day.setStatus('current')
adIfPhCurOutBcastPkts1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 30), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutBcastPkts1Day.setStatus('current')
adIfPhCurOutDiscards1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 31), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutDiscards1Day.setStatus('current')
adIfPhCurOutErrors1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 1, 1, 32), HCPerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPhCurOutErrors1Day.setStatus('current')
adIfPh15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2), )
if mibBuilder.loadTexts: adIfPh15MinIntervalTable.setStatus('current')
adIfPh15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinIntervalNumber"))
if mibBuilder.loadTexts: adIfPh15MinIntervalEntry.setStatus('current')
adIfPh15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: adIfPh15MinIntervalNumber.setStatus('current')
adIfPh15MinInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 2), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInOctets.setStatus('current')
adIfPh15MinInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 3), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInUcastPkts.setStatus('current')
adIfPh15MinInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 4), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInMcastPkts.setStatus('current')
adIfPh15MinInBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 5), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInBcastPkts.setStatus('current')
adIfPh15MinInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 6), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInDiscards.setStatus('current')
adIfPh15MinInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 7), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInErrors.setStatus('current')
adIfPh15MinInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 8), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinInUnknownProtos.setStatus('current')
adIfPh15MinOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 9), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutOctets.setStatus('current')
adIfPh15MinOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 10), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutUcastPkts.setStatus('current')
adIfPh15MinOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 11), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutMcastPkts.setStatus('current')
adIfPh15MinOutBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 12), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutBcastPkts.setStatus('current')
adIfPh15MinOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 13), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutDiscards.setStatus('current')
adIfPh15MinOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 2, 1, 14), HCPerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh15MinOutErrors.setStatus('current')
adIfPh1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3), )
if mibBuilder.loadTexts: adIfPh1DayIntervalTable.setStatus('current')
adIfPh1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayIntervalNumber"))
if mibBuilder.loadTexts: adIfPh1DayIntervalEntry.setStatus('current')
adIfPh1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: adIfPh1DayIntervalNumber.setStatus('current')
adIfPh1DayInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 2), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInOctets.setStatus('current')
adIfPh1DayInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 3), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInUcastPkts.setStatus('current')
adIfPh1DayInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 4), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInMcastPkts.setStatus('current')
adIfPh1DayInBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 5), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInBcastPkts.setStatus('current')
adIfPh1DayInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 6), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInDiscards.setStatus('current')
adIfPh1DayInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 7), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInErrors.setStatus('current')
adIfPh1DayInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 8), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayInUnknownProtos.setStatus('current')
adIfPh1DayOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 9), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutOctets.setStatus('current')
adIfPh1DayOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 10), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutUcastPkts.setStatus('current')
adIfPh1DayOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 11), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutMcastPkts.setStatus('current')
adIfPh1DayOutBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 12), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutBcastPkts.setStatus('current')
adIfPh1DayOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 13), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutDiscards.setStatus('current')
adIfPh1DayOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7, 3, 1, 14), HCPerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adIfPh1DayOutErrors.setStatus('current')
adGenAosIfPerfHistoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16))
adGenAosIfPerfHistoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1))
adGenAosIfPerfHistoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 2))
adGenAosIfPerfHistoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 2, 1)).setObjects(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurGroup"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinIntervalGroup"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayIntervalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAosIfPerfHistoryCompliance = adGenAosIfPerfHistoryCompliance.setStatus('current')
adIfPhCurGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 1)).setObjects(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurTimeElapsed15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurValidIntervals15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInvalidIntervals15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInOctets15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInMcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInBcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInDiscards15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInErrors15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUnknownProtos15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutOctets15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutUcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutMcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutBcastPkts15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutDiscards15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutErrors15Min"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurTimeElapsed1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurValidIntervals1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInvalidIntervals1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInOctets1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInMcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInBcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInDiscards1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInErrors1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurInUnknownProtos1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutOctets1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutUcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutMcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutBcastPkts1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutDiscards1Day"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPhCurOutErrors1Day"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adIfPhCurGroup = adIfPhCurGroup.setStatus('current')
adIfPh15MinIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 2)).setObjects(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInOctets"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInUcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInMcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInBcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInDiscards"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInErrors"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinInUnknownProtos"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutOctets"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutUcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutMcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutBcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutDiscards"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh15MinOutErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adIfPh15MinIntervalGroup = adIfPh15MinIntervalGroup.setStatus('current')
adIfPh1DayIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 16, 1, 3)).setObjects(("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInOctets"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInUcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInMcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInBcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInDiscards"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInErrors"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayInUnknownProtos"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutOctets"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutUcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutMcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutBcastPkts"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutDiscards"), ("ADTRAN-IF-PERF-HISTORY-MIB", "adIfPh1DayOutErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adIfPh1DayIntervalGroup = adIfPh1DayIntervalGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-IF-PERF-HISTORY-MIB", adIfPhCurInMcastPkts15Min=adIfPhCurInMcastPkts15Min, adIfPhCurInUnknownProtos1Day=adIfPhCurInUnknownProtos1Day, adIfPhCurOutErrors15Min=adIfPhCurOutErrors15Min, adIfPhCurInBcastPkts15Min=adIfPhCurInBcastPkts15Min, adIfPhCurInMcastPkts1Day=adIfPhCurInMcastPkts1Day, adIfPhCurOutDiscards1Day=adIfPhCurOutDiscards1Day, adIfPh15MinOutUcastPkts=adIfPh15MinOutUcastPkts, adIfPhCurOutBcastPkts15Min=adIfPhCurOutBcastPkts15Min, adIfPh15MinOutErrors=adIfPh15MinOutErrors, adIfPh1DayIntervalTable=adIfPh1DayIntervalTable, adIfPhCurTable=adIfPhCurTable, adIfPhCurInvalidIntervals1Day=adIfPhCurInvalidIntervals1Day, adIfPh1DayInDiscards=adIfPh1DayInDiscards, adIfPhCurTimeElapsed15Min=adIfPhCurTimeElapsed15Min, adIfPhCurInBcastPkts1Day=adIfPhCurInBcastPkts1Day, adIfPhCurInvalidIntervals15Min=adIfPhCurInvalidIntervals15Min, adIfPh1DayIntervalEntry=adIfPh1DayIntervalEntry, adIfPh1DayInOctets=adIfPh1DayInOctets, adIfPh15MinOutDiscards=adIfPh15MinOutDiscards, adIfPhCurOutMcastPkts1Day=adIfPhCurOutMcastPkts1Day, adIfPh1DayOutErrors=adIfPh1DayOutErrors, adIfPh15MinInErrors=adIfPh15MinInErrors, adIfPh15MinInMcastPkts=adIfPh15MinInMcastPkts, adIfPhCurValidIntervals15Min=adIfPhCurValidIntervals15Min, adIfPh1DayIntervalGroup=adIfPh1DayIntervalGroup, adIfPhCurOutBcastPkts1Day=adIfPhCurOutBcastPkts1Day, adIfPh1DayOutDiscards=adIfPh1DayOutDiscards, adIfPh15MinIntervalGroup=adIfPh15MinIntervalGroup, adIfPh15MinInBcastPkts=adIfPh15MinInBcastPkts, adIfPhCurEntry=adIfPhCurEntry, adIfPhCurOutOctets1Day=adIfPhCurOutOctets1Day, adGenAosIfPerfHistoryMib=adGenAosIfPerfHistoryMib, adIfPh1DayInUcastPkts=adIfPh1DayInUcastPkts, adIfPhCurInDiscards1Day=adIfPhCurInDiscards1Day, adIfPh1DayInMcastPkts=adIfPh1DayInMcastPkts, adIfPhCurOutErrors1Day=adIfPhCurOutErrors1Day, adIfPh1DayInBcastPkts=adIfPh1DayInBcastPkts, adIfPh1DayOutUcastPkts=adIfPh1DayOutUcastPkts, adIfPh1DayOutMcastPkts=adIfPh1DayOutMcastPkts, adIfPh1DayOutBcastPkts=adIfPh1DayOutBcastPkts, adIfPhCurOutUcastPkts1Day=adIfPhCurOutUcastPkts1Day, adGenAosIfPerfHistoryGroups=adGenAosIfPerfHistoryGroups, adIfPh1DayOutOctets=adIfPh1DayOutOctets, adGenAosIfPerfHistoryConformance=adGenAosIfPerfHistoryConformance, adIfPhCurInDiscards15Min=adIfPhCurInDiscards15Min, adIfPhCurValidIntervals1Day=adIfPhCurValidIntervals1Day, adIfPh1DayInUnknownProtos=adIfPh1DayInUnknownProtos, PYSNMP_MODULE_ID=adGenAosIfPerfHistoryMib, adIfPhCurOutMcastPkts15Min=adIfPhCurOutMcastPkts15Min, adIfPhCurInErrors15Min=adIfPhCurInErrors15Min, adIfPhCurOutUcastPkts15Min=adIfPhCurOutUcastPkts15Min, adIfPhCurOutDiscards15Min=adIfPhCurOutDiscards15Min, adIfPhCurInUcastPkts15Min=adIfPhCurInUcastPkts15Min, adIfPhCurInErrors1Day=adIfPhCurInErrors1Day, adIfPhCurInUcastPkts1Day=adIfPhCurInUcastPkts1Day, adIfPh1DayIntervalNumber=adIfPh1DayIntervalNumber, adIfPh1DayInErrors=adIfPh1DayInErrors, adGenAosIfPerfHistoryCompliance=adGenAosIfPerfHistoryCompliance, adIfPh15MinIntervalEntry=adIfPh15MinIntervalEntry, adIfPh15MinIntervalTable=adIfPh15MinIntervalTable, adIfPh15MinInUnknownProtos=adIfPh15MinInUnknownProtos, adIfPhCurInOctets15Min=adIfPhCurInOctets15Min, adIfPhCurOutOctets15Min=adIfPhCurOutOctets15Min, adIfPh15MinInUcastPkts=adIfPh15MinInUcastPkts, adIfPh15MinOutOctets=adIfPh15MinOutOctets, adIfPh15MinOutMcastPkts=adIfPh15MinOutMcastPkts, adGenAosIfPerfHistory=adGenAosIfPerfHistory, adIfPhCurInUnknownProtos15Min=adIfPhCurInUnknownProtos15Min, adIfPh15MinIntervalNumber=adIfPh15MinIntervalNumber, adIfPh15MinInDiscards=adIfPh15MinInDiscards, adIfPhCurGroup=adIfPhCurGroup, adIfPhCurTimeElapsed1Day=adIfPhCurTimeElapsed1Day, adIfPhCurInOctets1Day=adIfPhCurInOctets1Day, adGenAosIfPerfHistoryCompliances=adGenAosIfPerfHistoryCompliances, adIfPh15MinOutBcastPkts=adIfPh15MinOutBcastPkts, adIfPh15MinInOctets=adIfPh15MinInOctets)
