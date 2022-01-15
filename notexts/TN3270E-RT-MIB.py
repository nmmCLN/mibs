#
# PySNMP MIB module TN3270E-RT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/TN3270E-RT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
IANATn3270eAddress, IANATn3270eAddrType = mibBuilder.importSymbols("IANATn3270eTC-MIB", "IANATn3270eAddress", "IANATn3270eAddrType")
snanauMIB, = mibBuilder.importSymbols("SNA-NAU-MIB", "snanauMIB")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TimeStamp, DateAndTime, TestAndIncr, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "DateAndTime", "TestAndIncr", "TextualConvention", "RowStatus")
tn3270eClientGroupName, tn3270eResMapElementType, tn3270eSrvrConfIndex = mibBuilder.importSymbols("TN3270E-MIB", "tn3270eClientGroupName", "tn3270eResMapElementType", "tn3270eSrvrConfIndex")
tn3270eRtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 9))
tn3270eRtMIB.setRevisions(('2006-01-13 00:00', '1998-07-27 00:00',))
if mibBuilder.loadTexts: tn3270eRtMIB.setLastUpdated('200601130000Z')
if mibBuilder.loadTexts: tn3270eRtMIB.setOrganization('TN3270E Working Group')
tn3270eRtNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 0))
tn3270eRtObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 1))
tn3270eRtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3))
tn3270eRtCollCtlTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 1), )
if mibBuilder.loadTexts: tn3270eRtCollCtlTable.setStatus('current')
tn3270eRtCollCtlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1), ).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"))
if mibBuilder.loadTexts: tn3270eRtCollCtlEntry.setStatus('current')
tn3270eRtCollCtlType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlType.setStatus('current')
tn3270eRtCollCtlSPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 86400)).clone(20)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlSPeriod.setStatus('current')
tn3270eRtCollCtlSPMult = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 5760)).clone(30)).setUnits('period').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlSPMult.setStatus('current')
tn3270eRtCollCtlThreshHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshHigh.setStatus('current')
tn3270eRtCollCtlThreshLow = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlThreshLow.setStatus('current')
tn3270eRtCollCtlIdleCount = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 7), Unsigned32().clone(1)).setUnits('transactions').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlIdleCount.setStatus('current')
tn3270eRtCollCtlBucketBndry1 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 8), Unsigned32().clone(10)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry1.setStatus('current')
tn3270eRtCollCtlBucketBndry2 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 9), Unsigned32().clone(20)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry2.setStatus('current')
tn3270eRtCollCtlBucketBndry3 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 10), Unsigned32().clone(50)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry3.setStatus('current')
tn3270eRtCollCtlBucketBndry4 = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 11), Unsigned32().clone(100)).setUnits('tenths of seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlBucketBndry4.setStatus('current')
tn3270eRtCollCtlRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tn3270eRtCollCtlRowStatus.setStatus('current')
tn3270eRtDataTable = MibTable((1, 3, 6, 1, 2, 1, 34, 9, 1, 2), )
if mibBuilder.loadTexts: tn3270eRtDataTable.setStatus('current')
tn3270eRtDataEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1), ).setIndexNames((0, "TN3270E-MIB", "tn3270eSrvrConfIndex"), (0, "TN3270E-MIB", "tn3270eClientGroupName"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddrType"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddress"), (0, "TN3270E-RT-MIB", "tn3270eRtDataClientPort"))
if mibBuilder.loadTexts: tn3270eRtDataEntry.setStatus('current')
tn3270eRtDataClientAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 1), IANATn3270eAddrType())
if mibBuilder.loadTexts: tn3270eRtDataClientAddrType.setStatus('current')
tn3270eRtDataClientAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 2), IANATn3270eAddress())
if mibBuilder.loadTexts: tn3270eRtDataClientAddress.setStatus('current')
tn3270eRtDataClientPort = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: tn3270eRtDataClientPort.setStatus('current')
tn3270eRtDataAvgRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 4), Gauge32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgRt.setStatus('current')
tn3270eRtDataAvgIpRt = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 5), Gauge32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgIpRt.setStatus('current')
tn3270eRtDataAvgCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 6), Gauge32()).setUnits('transactions').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataAvgCountTrans.setStatus('current')
tn3270eRtDataIntTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataIntTimeStamp.setStatus('current')
tn3270eRtDataTotalRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 8), Counter32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataTotalRts.setStatus('current')
tn3270eRtDataTotalIpRts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 9), Counter32()).setUnits('tenths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataTotalIpRts.setStatus('current')
tn3270eRtDataCountTrans = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 10), Counter32()).setUnits('transactions').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataCountTrans.setStatus('current')
tn3270eRtDataCountDrs = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 11), Counter32()).setUnits('definite responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataCountDrs.setStatus('current')
tn3270eRtDataElapsRndTrpSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 12), Unsigned32()).setUnits('tenths of seconds squared').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataElapsRndTrpSq.setStatus('current')
tn3270eRtDataElapsIpRtSq = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 13), Unsigned32()).setUnits('tenths of seconds squared').setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataElapsIpRtSq.setStatus('current')
tn3270eRtDataBucket1Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket1Rts.setStatus('current')
tn3270eRtDataBucket2Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket2Rts.setStatus('current')
tn3270eRtDataBucket3Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket3Rts.setStatus('current')
tn3270eRtDataBucket4Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket4Rts.setStatus('current')
tn3270eRtDataBucket5Rts = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataBucket5Rts.setStatus('current')
tn3270eRtDataRtMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("responses", 1), ("timingMark", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataRtMethod.setStatus('current')
tn3270eRtDataDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 20), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tn3270eRtDataDiscontinuityTime.setStatus('current')
tn3270eRtSpinLock = MibScalar((1, 3, 6, 1, 2, 1, 34, 9, 1, 3), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tn3270eRtSpinLock.setStatus('current')
tn3270eRtExceeded = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 1)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
if mibBuilder.loadTexts: tn3270eRtExceeded.setStatus('current')
tn3270eRtOkay = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 2)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
if mibBuilder.loadTexts: tn3270eRtOkay.setStatus('current')
tn3270eRtCollStart = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 3)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-MIB", "tn3270eResMapElementType"))
if mibBuilder.loadTexts: tn3270eRtCollStart.setStatus('current')
tn3270eRtCollEnd = NotificationType((1, 3, 6, 1, 2, 1, 34, 9, 0, 4)).setObjects(("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
if mibBuilder.loadTexts: tn3270eRtCollEnd.setStatus('current')
tn3270eRtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 1))
tn3270eRtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 9, 3, 2))
tn3270eRtCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 9, 3, 2, 1)).setObjects(("TN3270E-RT-MIB", "tn3270eRtGroup"), ("TN3270E-RT-MIB", "tn3270eRtNotGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn3270eRtCompliance = tn3270eRtCompliance.setStatus('current')
tn3270eRtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 1)).setObjects(("TN3270E-RT-MIB", "tn3270eRtCollCtlType"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPeriod"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPMult"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshHigh"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshLow"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlIdleCount"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry1"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry2"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry3"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry4"), ("TN3270E-RT-MIB", "tn3270eRtCollCtlRowStatus"), ("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"), ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"), ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"), ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"), ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"), ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"), ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"), ("TN3270E-RT-MIB", "tn3270eRtSpinLock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn3270eRtGroup = tn3270eRtGroup.setStatus('current')
tn3270eRtNotGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 2)).setObjects(("TN3270E-RT-MIB", "tn3270eRtExceeded"), ("TN3270E-RT-MIB", "tn3270eRtOkay"), ("TN3270E-RT-MIB", "tn3270eRtCollStart"), ("TN3270E-RT-MIB", "tn3270eRtCollEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tn3270eRtNotGroup = tn3270eRtNotGroup.setStatus('current')
mibBuilder.exportSymbols("TN3270E-RT-MIB", tn3270eRtCollCtlBucketBndry3=tn3270eRtCollCtlBucketBndry3, tn3270eRtDataBucket2Rts=tn3270eRtDataBucket2Rts, tn3270eRtCollCtlThreshHigh=tn3270eRtCollCtlThreshHigh, tn3270eRtCollCtlTable=tn3270eRtCollCtlTable, tn3270eRtDataRtMethod=tn3270eRtDataRtMethod, tn3270eRtCollCtlIdleCount=tn3270eRtCollCtlIdleCount, tn3270eRtExceeded=tn3270eRtExceeded, tn3270eRtDataClientPort=tn3270eRtDataClientPort, tn3270eRtGroup=tn3270eRtGroup, tn3270eRtDataTable=tn3270eRtDataTable, tn3270eRtCollCtlThreshLow=tn3270eRtCollCtlThreshLow, tn3270eRtDataAvgIpRt=tn3270eRtDataAvgIpRt, tn3270eRtDataEntry=tn3270eRtDataEntry, tn3270eRtDataClientAddrType=tn3270eRtDataClientAddrType, tn3270eRtCollCtlBucketBndry4=tn3270eRtCollCtlBucketBndry4, tn3270eRtDataBucket1Rts=tn3270eRtDataBucket1Rts, PYSNMP_MODULE_ID=tn3270eRtMIB, tn3270eRtGroups=tn3270eRtGroups, tn3270eRtCompliance=tn3270eRtCompliance, tn3270eRtObjects=tn3270eRtObjects, tn3270eRtCompliances=tn3270eRtCompliances, tn3270eRtDataCountTrans=tn3270eRtDataCountTrans, tn3270eRtCollCtlBucketBndry1=tn3270eRtCollCtlBucketBndry1, tn3270eRtNotifications=tn3270eRtNotifications, tn3270eRtCollCtlType=tn3270eRtCollCtlType, tn3270eRtConformance=tn3270eRtConformance, tn3270eRtDataTotalRts=tn3270eRtDataTotalRts, tn3270eRtDataElapsIpRtSq=tn3270eRtDataElapsIpRtSq, tn3270eRtDataBucket4Rts=tn3270eRtDataBucket4Rts, tn3270eRtCollCtlEntry=tn3270eRtCollCtlEntry, tn3270eRtDataIntTimeStamp=tn3270eRtDataIntTimeStamp, tn3270eRtCollCtlSPMult=tn3270eRtCollCtlSPMult, tn3270eRtCollCtlRowStatus=tn3270eRtCollCtlRowStatus, tn3270eRtCollCtlBucketBndry2=tn3270eRtCollCtlBucketBndry2, tn3270eRtOkay=tn3270eRtOkay, tn3270eRtDataBucket5Rts=tn3270eRtDataBucket5Rts, tn3270eRtMIB=tn3270eRtMIB, tn3270eRtDataClientAddress=tn3270eRtDataClientAddress, tn3270eRtDataAvgRt=tn3270eRtDataAvgRt, tn3270eRtSpinLock=tn3270eRtSpinLock, tn3270eRtCollCtlSPeriod=tn3270eRtCollCtlSPeriod, tn3270eRtNotGroup=tn3270eRtNotGroup, tn3270eRtCollStart=tn3270eRtCollStart, tn3270eRtCollEnd=tn3270eRtCollEnd, tn3270eRtDataCountDrs=tn3270eRtDataCountDrs, tn3270eRtDataTotalIpRts=tn3270eRtDataTotalIpRts, tn3270eRtDataElapsRndTrpSq=tn3270eRtDataElapsRndTrpSq, tn3270eRtDataAvgCountTrans=tn3270eRtDataAvgCountTrans, tn3270eRtDataBucket3Rts=tn3270eRtDataBucket3Rts, tn3270eRtDataDiscontinuityTime=tn3270eRtDataDiscontinuityTime)
