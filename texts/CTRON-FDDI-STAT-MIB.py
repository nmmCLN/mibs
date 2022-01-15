#
# PySNMP MIB module CTRON-FDDI-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-FDDI-STAT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:17 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ctFDDIStats, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFDDIStats")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, Gauge32, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctFDDIStatsUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1))
ctFDDIStatsCtlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1), )
if mibBuilder.loadTexts: ctFDDIStatsCtlTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIStatsCtlTable.setDescription('This table allows control over the creation of FDDI\n                utilization statistics.  This is done by providing an\n                object that when accessed latches the statistics into\n                the stats table.')
ctFDDIStatsCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1), ).setIndexNames((0, "CTRON-FDDI-STAT-MIB", "ctFDDISlot"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDISMT"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDIPath"))
if mibBuilder.loadTexts: ctFDDIStatsCtlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIStatsCtlEntry.setDescription('Defines a specific control entry.')
ctFDDISlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDISlot.setDescription('A specific slot for which this connection entry is\n                defined.  If the entry corresponds to a slotless chassis \n                system, then this entry will have the value of 0.')
ctFDDISMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDISMT.setReference('The IETF RFC FDDI-SMT73-MIB, fddimibSMTIndex')
if mibBuilder.loadTexts: ctFDDISMT.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDISMT.setDescription('A specific instance of SMT for which this entry pertains.')
ctFDDIPath = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPath.setReference('The IETF RFC FDDI-SMT73-MIB, fddimibPATHIndex')
if mibBuilder.loadTexts: ctFDDIPath.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIPath.setDescription('A specific FDDI Path that this connection entry pertains.')
ctFDDINextEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDINextEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDINextEntry.setDescription('Provides an identifier of the next entry to be used\n                in the ctFDDIStatsHistoryTable.\n\n                Reading this object will latch FDDI performance data\n                into a conceptual row in the ctFDDIStatsHistoryTable\n                indexed by the value just read from ctFDDINextEntry.')
ctFDDIResetPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFDDIResetPeak.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIResetPeak.setDescription('This object provides the ability to reset the peak\n                bytes and peak time stamp object.  This is accomplished\n                by setting this object with a value of reset(2).  Setting\n                a value of normal(1) will have no affect.  \n\n                When read this object will always return normal(1).')
ctFDDIStatsHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2), )
if mibBuilder.loadTexts: ctFDDIStatsHistoryTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIStatsHistoryTable.setDescription('Provides a history of latched FDDI performance objects.\n                There is one such object for each entry that has been\n                latched in the ctFDDIStatsCtlTable.\n\n                This table will contain the 10 most recent entries.  All\n                other entries will be lost.')
ctFDDIStatsHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1), ).setIndexNames((0, "CTRON-FDDI-STAT-MIB", "ctFDDISlot"), (0, "CTRON-FDDI-STAT-MIB", "ctFDDIStatsIndex"))
if mibBuilder.loadTexts: ctFDDIStatsHistoryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIStatsHistoryEntry.setDescription('')
ctFDDIStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIStatsIndex.setDescription('A unique entry that identifies a particular latched stats\n                entry.  This corresponds directly to a value of\n                ctFDDINextEntry.')
ctFDDIStatsTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIStatsTimeStamp.setDescription('The value of sysUpTime when this entry was created.')
ctFDDIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIFrames.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIFrames.setDescription('The bandwidth utilization in frames per second.')
ctFDDIBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIBytes.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIBytes.setDescription('The bandwidth utilization in bytes per second.')
ctFDDIPeakBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPeakBytes.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIPeakBytes.setDescription('The peak bandwidth utilization in bytes per second.')
ctFDDIPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIPeakTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIPeakTime.setDescription('A time stamp when the peak occured.')
ctFDDIStatsSMT = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsSMT.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIStatsSMT.setDescription('The FDDI SMT index for which these statistics pertain.\n                The value of the object must match a corresponding value\n                of ctFDDISMT.')
ctFDDIStatsPath = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFDDIStatsPath.setStatus('mandatory')
if mibBuilder.loadTexts: ctFDDIStatsPath.setDescription('The FDDI MAC path index for which these statistics pertain.\n                The value of the object must match a corresponding value\n                of ctFDDIPath.')
mibBuilder.exportSymbols("CTRON-FDDI-STAT-MIB", ctFDDIStatsHistoryEntry=ctFDDIStatsHistoryEntry, ctFDDIStatsCtlEntry=ctFDDIStatsCtlEntry, ctFDDIBytes=ctFDDIBytes, ctFDDIFrames=ctFDDIFrames, ctFDDIPeakBytes=ctFDDIPeakBytes, ctFDDIResetPeak=ctFDDIResetPeak, ctFDDIStatsSMT=ctFDDIStatsSMT, ctFDDIStatsIndex=ctFDDIStatsIndex, ctFDDIStatsPath=ctFDDIStatsPath, ctFDDIStatsCtlTable=ctFDDIStatsCtlTable, ctFDDIPath=ctFDDIPath, ctFDDIStatsUtil=ctFDDIStatsUtil, ctFDDISMT=ctFDDISMT, ctFDDIStatsTimeStamp=ctFDDIStatsTimeStamp, ctFDDIPeakTime=ctFDDIPeakTime, ctFDDINextEntry=ctFDDINextEntry, ctFDDISlot=ctFDDISlot, ctFDDIStatsHistoryTable=ctFDDIStatsHistoryTable)
