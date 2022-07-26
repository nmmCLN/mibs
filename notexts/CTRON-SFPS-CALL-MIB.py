#
# PySNMP MIB module CTRON-SFPS-CALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CALL-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:27:41 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
sfpsCallTableStats, sfpsCallByTuple, sfpsSap, sfpsSapAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsCallTableStats", "sfpsCallByTuple", "sfpsSap", "sfpsSapAPI")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ObjectIdentity, Counter64, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, TimeTicks, Gauge32, Bits, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ObjectIdentity", "Counter64", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "Bits", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HexInteger(Integer32):
    pass

sfpsSapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1), )
if mibBuilder.loadTexts: sfpsSapTable.setStatus('mandatory')
sfpsSapTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableTag"), (0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableHash"), (0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableHashIndex"))
if mibBuilder.loadTexts: sfpsSapTableEntry.setStatus('mandatory')
sfpsSapTableTag = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableTag.setStatus('mandatory')
sfpsSapTableHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableHash.setStatus('mandatory')
sfpsSapTableHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableHashIndex.setStatus('mandatory')
sfpsSapTableSourceCP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableSourceCP.setStatus('mandatory')
sfpsSapTableDestCP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableDestCP.setStatus('mandatory')
sfpsSapTableSAP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableSAP.setStatus('mandatory')
sfpsSapTableOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableOperStatus.setStatus('mandatory')
sfpsSapTableAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableAdminStatus.setStatus('mandatory')
sfpsSapTableStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableStateTime.setStatus('mandatory')
sfpsSapTableDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableDescription.setStatus('mandatory')
sfpsSapTableNumAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableNumAccepted.setStatus('mandatory')
sfpsSapTableNumDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableNumDropped.setStatus('mandatory')
sfpsSapTableUnicastSap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapTableUnicastSap.setStatus('mandatory')
sfpsSapTableNVStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableNVStatus.setStatus('mandatory')
sfpsSapAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("getStatus", 1), ("next", 2), ("first", 3), ("disable", 4), ("disableInNvram", 5), ("enable", 6), ("enableInNvram", 7), ("clearFromNvram", 8), ("clearAllNvram", 9), ("resetStats", 10), ("resetAllStats", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPIVerb.setStatus('mandatory')
sfpsSapAPISourceCP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPISourceCP.setStatus('mandatory')
sfpsSapAPIDestCP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPIDestCP.setStatus('mandatory')
sfpsSapAPISAP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPISAP.setStatus('mandatory')
sfpsSapAPINVStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPINVStatus.setStatus('mandatory')
sfpsSapAPIAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPIAdminStatus.setStatus('mandatory')
sfpsSapAPIOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPIOperStatus.setStatus('mandatory')
sfpsSapAPINvSet = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPINvSet.setStatus('mandatory')
sfpsSapAPINVTotal = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPINVTotal.setStatus('mandatory')
sfpsSapAPINumAccept = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPINumAccept.setStatus('mandatory')
sfpsSapAPINvDiscard = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPINvDiscard.setStatus('mandatory')
sfpsSapAPIDefaultStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPIDefaultStatus.setStatus('mandatory')
sfpsCallByTupleTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1), )
if mibBuilder.loadTexts: sfpsCallByTupleTable.setStatus('mandatory')
sfpsCallByTupleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1), ).setIndexNames((0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleInPort"), (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleSrcHash"), (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleDstHash"), (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleHashIndex"))
if mibBuilder.loadTexts: sfpsCallByTupleEntry.setStatus('mandatory')
sfpsCallByTupleInPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleInPort.setStatus('mandatory')
sfpsCallByTupleSrcHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleSrcHash.setStatus('mandatory')
sfpsCallByTupleDstHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleDstHash.setStatus('mandatory')
sfpsCallByTupleHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleHashIndex.setStatus('mandatory')
sfpsCallByTupleBotSrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleBotSrcType.setStatus('mandatory')
sfpsCallByTupleBotSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleBotSrcAddress.setStatus('mandatory')
sfpsCallByTupleBotDstType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleBotDstType.setStatus('mandatory')
sfpsCallByTupleBotDstAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleBotDstAddress.setStatus('mandatory')
sfpsCallByTupleTopSrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTopSrcType.setStatus('mandatory')
sfpsCallByTupleTopSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTopSrcAddress.setStatus('mandatory')
sfpsCallByTupleTopDstType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTopDstType.setStatus('mandatory')
sfpsCallByTupleTopDstAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTopDstAddress.setStatus('mandatory')
sfpsCallByTupleCallProcName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleCallProcName.setStatus('mandatory')
sfpsCallByTupleCallTag = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 14), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleCallTag.setStatus('mandatory')
sfpsCallByTupleCallState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleCallState.setStatus('mandatory')
sfpsCallByTupleTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 16), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTimeRemaining.setStatus('mandatory')
sfpsCallTableStatsRam = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsRam.setStatus('mandatory')
sfpsCallTableStatsSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsSize.setStatus('mandatory')
sfpsCallTableStatsInUse = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsInUse.setStatus('mandatory')
sfpsCallTableStatsMax = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsMax.setStatus('mandatory')
sfpsCallTableStatsTotMisses = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsTotMisses.setStatus('mandatory')
sfpsCallTableStatsMissStart = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsMissStart.setStatus('mandatory')
sfpsCallTableStatsMissStop = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsMissStop.setStatus('mandatory')
sfpsCallTableStatsLastMiss = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTableStatsLastMiss.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-CALL-MIB", sfpsSapTableAdminStatus=sfpsSapTableAdminStatus, sfpsSapTableHash=sfpsSapTableHash, sfpsSapAPIDefaultStatus=sfpsSapAPIDefaultStatus, sfpsCallTableStatsSize=sfpsCallTableStatsSize, sfpsCallTableStatsTotMisses=sfpsCallTableStatsTotMisses, sfpsCallTableStatsMissStart=sfpsCallTableStatsMissStart, sfpsSapAPISourceCP=sfpsSapAPISourceCP, sfpsSapAPINVStatus=sfpsSapAPINVStatus, sfpsSapAPIOperStatus=sfpsSapAPIOperStatus, sfpsCallByTupleTopSrcType=sfpsCallByTupleTopSrcType, sfpsSapAPINVTotal=sfpsSapAPINVTotal, sfpsSapTableDescription=sfpsSapTableDescription, sfpsCallByTupleBotDstType=sfpsCallByTupleBotDstType, sfpsCallTableStatsLastMiss=sfpsCallTableStatsLastMiss, sfpsCallByTupleCallState=sfpsCallByTupleCallState, sfpsSapAPIDestCP=sfpsSapAPIDestCP, sfpsSapTableSourceCP=sfpsSapTableSourceCP, sfpsSapTableNVStatus=sfpsSapTableNVStatus, sfpsCallTableStatsMissStop=sfpsCallTableStatsMissStop, sfpsSapTableDestCP=sfpsSapTableDestCP, sfpsCallTableStatsInUse=sfpsCallTableStatsInUse, sfpsCallByTupleBotSrcAddress=sfpsCallByTupleBotSrcAddress, sfpsCallByTupleCallProcName=sfpsCallByTupleCallProcName, sfpsSapAPINvDiscard=sfpsSapAPINvDiscard, sfpsCallByTupleTable=sfpsCallByTupleTable, HexInteger=HexInteger, sfpsSapAPIVerb=sfpsSapAPIVerb, sfpsSapAPINvSet=sfpsSapAPINvSet, sfpsSapAPIAdminStatus=sfpsSapAPIAdminStatus, sfpsCallByTupleTimeRemaining=sfpsCallByTupleTimeRemaining, sfpsCallByTupleHashIndex=sfpsCallByTupleHashIndex, sfpsCallByTupleTopDstType=sfpsCallByTupleTopDstType, sfpsCallByTupleDstHash=sfpsCallByTupleDstHash, sfpsCallByTupleCallTag=sfpsCallByTupleCallTag, sfpsSapTable=sfpsSapTable, sfpsSapTableEntry=sfpsSapTableEntry, sfpsSapTableHashIndex=sfpsSapTableHashIndex, sfpsCallByTupleSrcHash=sfpsCallByTupleSrcHash, sfpsCallTableStatsRam=sfpsCallTableStatsRam, sfpsCallByTupleTopDstAddress=sfpsCallByTupleTopDstAddress, sfpsCallTableStatsMax=sfpsCallTableStatsMax, sfpsSapTableUnicastSap=sfpsSapTableUnicastSap, sfpsSapTableSAP=sfpsSapTableSAP, sfpsSapTableOperStatus=sfpsSapTableOperStatus, sfpsSapTableNumDropped=sfpsSapTableNumDropped, sfpsCallByTupleBotSrcType=sfpsCallByTupleBotSrcType, sfpsSapTableNumAccepted=sfpsSapTableNumAccepted, sfpsCallByTupleTopSrcAddress=sfpsCallByTupleTopSrcAddress, sfpsSapAPINumAccept=sfpsSapAPINumAccept, sfpsCallByTupleInPort=sfpsCallByTupleInPort, sfpsSapAPISAP=sfpsSapAPISAP, sfpsCallByTupleBotDstAddress=sfpsCallByTupleBotDstAddress, sfpsCallByTupleEntry=sfpsCallByTupleEntry, sfpsSapTableTag=sfpsSapTableTag, sfpsSapTableStateTime=sfpsSapTableStateTime)
