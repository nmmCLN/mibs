#
# PySNMP MIB module CTRON-FDDI-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-FDDI-STAT-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:29:47 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ctFDDIStats, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFDDIStats")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, iso, Counter64, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "Counter64", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctFDDIStatsUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1))
ctFDDIStatsCtlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1), )
if mibBuilder.loadTexts: ctFDDIStatsCtlTable.setStatus('mandatory')
ctFDDIStatsCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-FDDI-STAT-MIB", "ctFDDISlot"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDISMT"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDIPath"))
if mibBuilder.loadTexts: ctFDDIStatsCtlEntry.setStatus('mandatory')
ctFDDISlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISlot.setStatus('mandatory')
ctFDDISMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISMT.setStatus('mandatory')
ctFDDIPath = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPath.setStatus('mandatory')
ctFDDINextEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINextEntry.setStatus('mandatory')
ctFDDIResetPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDIResetPeak.setStatus('mandatory')
ctFDDIStatsHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2), )
if mibBuilder.loadTexts: ctFDDIStatsHistoryTable.setStatus('mandatory')
ctFDDIStatsHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1), ).setIndexNames((0, "CTRON-FDDI-STAT-MIB", "ctFDDISlot"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDIStatsIndex"))
if mibBuilder.loadTexts: ctFDDIStatsHistoryEntry.setStatus('mandatory')
ctFDDIStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsIndex.setStatus('mandatory')
ctFDDIStatsTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsTimeStamp.setStatus('mandatory')
ctFDDIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIFrames.setStatus('mandatory')
ctFDDIBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIBytes.setStatus('mandatory')
ctFDDIPeakBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPeakBytes.setStatus('mandatory')
ctFDDIPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPeakTime.setStatus('mandatory')
ctFDDIStatsSMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsSMT.setStatus('mandatory')
ctFDDIStatsPath = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsPath.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-FDDI-STAT-MIB", ctFDDIStatsUtil=ctFDDIStatsUtil, ctFDDIPeakTime=ctFDDIPeakTime, ctFDDIStatsSMT=ctFDDIStatsSMT, ctFDDINextEntry=ctFDDINextEntry, ctFDDISMT=ctFDDISMT, ctFDDIStatsCtlTable=ctFDDIStatsCtlTable, ctFDDIStatsCtlEntry=ctFDDIStatsCtlEntry, ctFDDISlot=ctFDDISlot, ctFDDIStatsPath=ctFDDIStatsPath, ctFDDIPeakBytes=ctFDDIPeakBytes, ctFDDIResetPeak=ctFDDIResetPeak, ctFDDIFrames=ctFDDIFrames, ctFDDIBytes=ctFDDIBytes, ctFDDIStatsTimeStamp=ctFDDIStatsTimeStamp, ctFDDIStatsHistoryTable=ctFDDIStatsHistoryTable, ctFDDIStatsHistoryEntry=ctFDDIStatsHistoryEntry, ctFDDIPath=ctFDDIPath, ctFDDIStatsIndex=ctFDDIStatsIndex)
