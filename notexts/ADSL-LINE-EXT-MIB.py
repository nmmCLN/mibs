#
# PySNMP MIB module ADSL-LINE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ADSL-LINE-EXT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adslAtucIntervalEntry, adslAturPerfDataEntry, adslAtucPerfDataEntry, adslAturIntervalEntry, adslMIB, adslLineAlarmConfProfileEntry, adslLineConfProfileEntry, adslLineEntry = mibBuilder.importSymbols("ADSL-LINE-MIB", "adslAtucIntervalEntry", "adslAturPerfDataEntry", "adslAtucPerfDataEntry", "adslAturIntervalEntry", "adslMIB", "adslLineAlarmConfProfileEntry", "adslLineConfProfileEntry", "adslLineEntry")
AdslPerfPrevDayCount, AdslPerfCurrDayCount = mibBuilder.importSymbols("ADSL-TC-MIB", "AdslPerfPrevDayCount", "AdslPerfCurrDayCount")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
PerfCurrentCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adslExtMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 3))
adslExtMIB.setRevisions(('2002-12-10 00:00',))
if mibBuilder.loadTexts: adslExtMIB.setLastUpdated('200212100000Z')
if mibBuilder.loadTexts: adslExtMIB.setOrganization('IETF ADSL MIB Working Group')
adslExtMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1))
class AdslTransmissionModeType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ansit1413", 0), ("etsi", 1), ("q9921PotsNonOverlapped", 2), ("q9921PotsOverlapped", 3), ("q9921IsdnNonOverlapped", 4), ("q9921isdnOverlapped", 5), ("q9921tcmIsdnNonOverlapped", 6), ("q9921tcmIsdnOverlapped", 7), ("q9922potsNonOverlapeed", 8), ("q9922potsOverlapped", 9), ("q9922tcmIsdnNonOverlapped", 10), ("q9922tcmIsdnOverlapped", 11), ("q9921tcmIsdnSymmetric", 12))

adslLineExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17), )
if mibBuilder.loadTexts: adslLineExtTable.setStatus('current')
adslLineExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1), )
adslLineEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslLineExtEntry"))
adslLineExtEntry.setIndexNames(*adslLineEntry.getIndexNames())
if mibBuilder.loadTexts: adslLineExtEntry.setStatus('current')
adslLineTransAtucCap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 1), AdslTransmissionModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslLineTransAtucCap.setStatus('current')
adslLineTransAtucConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 2), AdslTransmissionModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adslLineTransAtucConfig.setStatus('current')
adslLineTransAtucActual = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 3), AdslTransmissionModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslLineTransAtucActual.setStatus('current')
adslLineGlitePowerState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("l0", 2), ("l1", 3), ("l3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslLineGlitePowerState.setStatus('current')
adslLineConfProfileDualLite = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 17, 1, 5), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adslLineConfProfileDualLite.setStatus('current')
adslAtucPerfDataExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18), )
if mibBuilder.loadTexts: adslAtucPerfDataExtTable.setStatus('current')
adslAtucPerfDataExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1), )
adslAtucPerfDataEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAtucPerfDataExtEntry"))
adslAtucPerfDataExtEntry.setIndexNames(*adslAtucPerfDataEntry.getIndexNames())
if mibBuilder.loadTexts: adslAtucPerfDataExtEntry.setStatus('current')
adslAtucPerfStatFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 1), Counter32()).setUnits('line retrains').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfStatFastR.setStatus('current')
adslAtucPerfStatFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 2), Counter32()).setUnits('line retrains').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfStatFailedFastR.setStatus('current')
adslAtucPerfStatSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 3), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfStatSesL.setStatus('current')
adslAtucPerfStatUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfStatUasL.setStatus('current')
adslAtucPerfCurr15MinFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 5), PerfCurrentCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr15MinFastR.setStatus('current')
adslAtucPerfCurr15MinFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 6), PerfCurrentCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr15MinFailedFastR.setStatus('current')
adslAtucPerfCurr15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 7), PerfCurrentCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr15MinSesL.setStatus('current')
adslAtucPerfCurr15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 8), PerfCurrentCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr15MinUasL.setStatus('current')
adslAtucPerfCurr1DayFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 9), AdslPerfCurrDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr1DayFastR.setStatus('current')
adslAtucPerfCurr1DayFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 10), AdslPerfCurrDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr1DayFailedFastR.setStatus('current')
adslAtucPerfCurr1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 11), AdslPerfCurrDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr1DaySesL.setStatus('current')
adslAtucPerfCurr1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 12), AdslPerfCurrDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfCurr1DayUasL.setStatus('current')
adslAtucPerfPrev1DayFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 13), AdslPerfPrevDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfPrev1DayFastR.setStatus('current')
adslAtucPerfPrev1DayFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 14), AdslPerfPrevDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfPrev1DayFailedFastR.setStatus('current')
adslAtucPerfPrev1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 15), AdslPerfPrevDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfPrev1DaySesL.setStatus('current')
adslAtucPerfPrev1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 18, 1, 16), AdslPerfPrevDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucPerfPrev1DayUasL.setStatus('current')
adslAtucIntervalExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19), )
if mibBuilder.loadTexts: adslAtucIntervalExtTable.setStatus('current')
adslAtucIntervalExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1), )
adslAtucIntervalEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAtucIntervalExtEntry"))
adslAtucIntervalExtEntry.setIndexNames(*adslAtucIntervalEntry.getIndexNames())
if mibBuilder.loadTexts: adslAtucIntervalExtEntry.setStatus('current')
adslAtucIntervalFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 1), PerfIntervalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucIntervalFastR.setStatus('current')
adslAtucIntervalFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 2), PerfIntervalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucIntervalFailedFastR.setStatus('current')
adslAtucIntervalSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 3), PerfIntervalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucIntervalSesL.setStatus('current')
adslAtucIntervalUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 19, 1, 4), PerfIntervalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucIntervalUasL.setStatus('current')
adslAturPerfDataExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20), )
if mibBuilder.loadTexts: adslAturPerfDataExtTable.setStatus('current')
adslAturPerfDataExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1), )
adslAturPerfDataEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAturPerfDataExtEntry"))
adslAturPerfDataExtEntry.setIndexNames(*adslAturPerfDataEntry.getIndexNames())
if mibBuilder.loadTexts: adslAturPerfDataExtEntry.setStatus('current')
adslAturPerfStatSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 1), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfStatSesL.setStatus('current')
adslAturPerfStatUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 2), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfStatUasL.setStatus('current')
adslAturPerfCurr15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 3), PerfCurrentCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfCurr15MinSesL.setStatus('current')
adslAturPerfCurr15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 4), PerfCurrentCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfCurr15MinUasL.setStatus('current')
adslAturPerfCurr1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 5), AdslPerfCurrDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfCurr1DaySesL.setStatus('current')
adslAturPerfCurr1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 6), AdslPerfCurrDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfCurr1DayUasL.setStatus('current')
adslAturPerfPrev1DaySesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 7), AdslPerfPrevDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfPrev1DaySesL.setStatus('current')
adslAturPerfPrev1DayUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 20, 1, 8), AdslPerfPrevDayCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturPerfPrev1DayUasL.setStatus('current')
adslAturIntervalExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21), )
if mibBuilder.loadTexts: adslAturIntervalExtTable.setStatus('current')
adslAturIntervalExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1), )
adslAturIntervalEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAturIntervalExtEntry"))
adslAturIntervalExtEntry.setIndexNames(*adslAturIntervalEntry.getIndexNames())
if mibBuilder.loadTexts: adslAturIntervalExtEntry.setStatus('current')
adslAturIntervalSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1, 1), PerfIntervalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturIntervalSesL.setStatus('current')
adslAturIntervalUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 21, 1, 2), PerfIntervalCount()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturIntervalUasL.setStatus('current')
adslConfProfileExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22), )
if mibBuilder.loadTexts: adslConfProfileExtTable.setStatus('current')
adslConfProfileExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22, 1), )
adslLineConfProfileEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslConfProfileExtEntry"))
adslConfProfileExtEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
if mibBuilder.loadTexts: adslConfProfileExtEntry.setStatus('current')
adslConfProfileLineType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 22, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noChannel", 1), ("fastOnly", 2), ("interleavedOnly", 3), ("fastOrInterleaved", 4), ("fastAndInterleaved", 5))).clone('fastOnly')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslConfProfileLineType.setStatus('current')
adslAlarmConfProfileExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23), )
if mibBuilder.loadTexts: adslAlarmConfProfileExtTable.setStatus('current')
adslAlarmConfProfileExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1), )
adslLineAlarmConfProfileEntry.registerAugmentions(("ADSL-LINE-EXT-MIB", "adslAlarmConfProfileExtEntry"))
adslAlarmConfProfileExtEntry.setIndexNames(*adslLineAlarmConfProfileEntry.getIndexNames())
if mibBuilder.loadTexts: adslAlarmConfProfileExtEntry.setStatus('current')
adslAtucThreshold15MinFailedFastR = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAtucThreshold15MinFailedFastR.setStatus('current')
adslAtucThreshold15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAtucThreshold15MinSesL.setStatus('current')
adslAtucThreshold15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAtucThreshold15MinUasL.setStatus('current')
adslAturThreshold15MinSesL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAturThreshold15MinSesL.setStatus('current')
adslAturThreshold15MinUasL = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 23, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: adslAturThreshold15MinUasL.setStatus('current')
adslExtTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24))
adslExtAtucTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1))
adslExtAtucTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0))
adslAtucFailedFastRThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 1)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFailedFastR"))
if mibBuilder.loadTexts: adslAtucFailedFastRThreshTrap.setStatus('current')
adslAtucSesLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 2)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinSesL"))
if mibBuilder.loadTexts: adslAtucSesLThreshTrap.setStatus('current')
adslAtucUasLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 1, 0, 3)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinUasL"))
if mibBuilder.loadTexts: adslAtucUasLThreshTrap.setStatus('current')
adslExtAturTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2))
adslExtAturTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0))
adslAturSesLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0, 1)).setObjects(("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinSesL"))
if mibBuilder.loadTexts: adslAturSesLThreshTrap.setStatus('current')
adslAturUasLThreshTrap = NotificationType((1, 3, 6, 1, 2, 1, 10, 94, 3, 1, 24, 2, 0, 2)).setObjects(("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinUasL"))
if mibBuilder.loadTexts: adslAturUasLThreshTrap.setStatus('current')
adslExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2))
adslExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1))
adslExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 2))
adslExtLineMibAtucCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 2, 1)).setObjects(("ADSL-LINE-EXT-MIB", "adslExtLineGroup"), ("ADSL-LINE-EXT-MIB", "adslExtLineConfProfileControlGroup"), ("ADSL-LINE-EXT-MIB", "adslExtLineAlarmConfProfileGroup"), ("ADSL-LINE-EXT-MIB", "adslExtAtucPhysPerfCounterGroup"), ("ADSL-LINE-EXT-MIB", "adslExtAturPhysPerfCounterGroup"), ("ADSL-LINE-EXT-MIB", "adslExtNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adslExtLineMibAtucCompliance = adslExtLineMibAtucCompliance.setStatus('current')
adslExtLineGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 1)).setObjects(("ADSL-LINE-EXT-MIB", "adslLineConfProfileDualLite"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucCap"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucConfig"), ("ADSL-LINE-EXT-MIB", "adslLineTransAtucActual"), ("ADSL-LINE-EXT-MIB", "adslLineGlitePowerState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adslExtLineGroup = adslExtLineGroup.setStatus('current')
adslExtAtucPhysPerfCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 2)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucPerfStatFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfStatUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfCurr1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAtucPerfPrev1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucIntervalUasL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adslExtAtucPhysPerfCounterGroup = adslExtAtucPhysPerfCounterGroup.setStatus('current')
adslExtAturPhysPerfCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 3)).setObjects(("ADSL-LINE-EXT-MIB", "adslAturPerfStatSesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfStatUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfCurr1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfPrev1DaySesL"), ("ADSL-LINE-EXT-MIB", "adslAturPerfPrev1DayUasL"), ("ADSL-LINE-EXT-MIB", "adslAturIntervalSesL"), ("ADSL-LINE-EXT-MIB", "adslAturIntervalUasL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adslExtAturPhysPerfCounterGroup = adslExtAturPhysPerfCounterGroup.setStatus('current')
adslExtLineConfProfileControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 4)).setObjects(("ADSL-LINE-EXT-MIB", "adslConfProfileLineType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adslExtLineConfProfileControlGroup = adslExtLineConfProfileControlGroup.setStatus('current')
adslExtLineAlarmConfProfileGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 5)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinFailedFastR"), ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAtucThreshold15MinUasL"), ("ADSL-LINE-EXT-MIB", "adslAturThreshold15MinSesL"), ("ADSL-LINE-EXT-MIB", "adslAturThreshold15MinUasL"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adslExtLineAlarmConfProfileGroup = adslExtLineAlarmConfProfileGroup.setStatus('current')
adslExtNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 94, 3, 2, 1, 6)).setObjects(("ADSL-LINE-EXT-MIB", "adslAtucFailedFastRThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAtucSesLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAtucUasLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAturSesLThreshTrap"), ("ADSL-LINE-EXT-MIB", "adslAturUasLThreshTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adslExtNotificationsGroup = adslExtNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ADSL-LINE-EXT-MIB", adslLineTransAtucCap=adslLineTransAtucCap, adslConfProfileExtTable=adslConfProfileExtTable, adslExtAturTrapsPrefix=adslExtAturTrapsPrefix, adslAturPerfDataExtEntry=adslAturPerfDataExtEntry, adslAtucIntervalFastR=adslAtucIntervalFastR, adslExtLineConfProfileControlGroup=adslExtLineConfProfileControlGroup, adslAturIntervalExtEntry=adslAturIntervalExtEntry, adslLineExtTable=adslLineExtTable, adslLineConfProfileDualLite=adslLineConfProfileDualLite, adslAturPerfStatSesL=adslAturPerfStatSesL, adslAtucFailedFastRThreshTrap=adslAtucFailedFastRThreshTrap, adslAturPerfDataExtTable=adslAturPerfDataExtTable, adslExtTraps=adslExtTraps, adslExtGroups=adslExtGroups, adslExtMibObjects=adslExtMibObjects, adslAtucUasLThreshTrap=adslAtucUasLThreshTrap, adslExtAturPhysPerfCounterGroup=adslExtAturPhysPerfCounterGroup, adslAlarmConfProfileExtEntry=adslAlarmConfProfileExtEntry, adslAlarmConfProfileExtTable=adslAlarmConfProfileExtTable, adslAtucPerfDataExtTable=adslAtucPerfDataExtTable, adslLineExtEntry=adslLineExtEntry, adslAturPerfCurr15MinSesL=adslAturPerfCurr15MinSesL, adslAtucThreshold15MinSesL=adslAtucThreshold15MinSesL, adslLineGlitePowerState=adslLineGlitePowerState, adslAtucPerfCurr15MinFastR=adslAtucPerfCurr15MinFastR, adslAtucPerfDataExtEntry=adslAtucPerfDataExtEntry, adslExtAtucTraps=adslExtAtucTraps, adslExtAtucPhysPerfCounterGroup=adslExtAtucPhysPerfCounterGroup, adslAtucPerfCurr15MinUasL=adslAtucPerfCurr15MinUasL, adslAtucThreshold15MinFailedFastR=adslAtucThreshold15MinFailedFastR, adslAtucPerfPrev1DaySesL=adslAtucPerfPrev1DaySesL, adslAturPerfCurr1DayUasL=adslAturPerfCurr1DayUasL, adslExtCompliances=adslExtCompliances, adslAtucPerfStatFastR=adslAtucPerfStatFastR, adslAtucPerfPrev1DayUasL=adslAtucPerfPrev1DayUasL, AdslTransmissionModeType=AdslTransmissionModeType, adslAtucIntervalFailedFastR=adslAtucIntervalFailedFastR, adslAtucIntervalExtEntry=adslAtucIntervalExtEntry, adslAturPerfPrev1DayUasL=adslAturPerfPrev1DayUasL, adslAtucSesLThreshTrap=adslAtucSesLThreshTrap, adslAturIntervalSesL=adslAturIntervalSesL, adslAtucPerfStatFailedFastR=adslAtucPerfStatFailedFastR, adslExtAturTraps=adslExtAturTraps, adslConfProfileLineType=adslConfProfileLineType, adslExtLineAlarmConfProfileGroup=adslExtLineAlarmConfProfileGroup, adslExtLineMibAtucCompliance=adslExtLineMibAtucCompliance, adslExtLineGroup=adslExtLineGroup, adslAtucIntervalSesL=adslAtucIntervalSesL, adslExtNotificationsGroup=adslExtNotificationsGroup, adslAturSesLThreshTrap=adslAturSesLThreshTrap, adslAturIntervalUasL=adslAturIntervalUasL, adslExtAtucTrapsPrefix=adslExtAtucTrapsPrefix, adslAtucPerfCurr1DayFastR=adslAtucPerfCurr1DayFastR, adslLineTransAtucActual=adslLineTransAtucActual, adslAturUasLThreshTrap=adslAturUasLThreshTrap, adslAturThreshold15MinUasL=adslAturThreshold15MinUasL, adslAturPerfCurr15MinUasL=adslAturPerfCurr15MinUasL, adslAtucPerfStatSesL=adslAtucPerfStatSesL, adslExtMIB=adslExtMIB, adslExtConformance=adslExtConformance, adslAturPerfStatUasL=adslAturPerfStatUasL, adslAtucPerfCurr15MinSesL=adslAtucPerfCurr15MinSesL, adslAtucIntervalExtTable=adslAtucIntervalExtTable, adslAtucPerfCurr1DayFailedFastR=adslAtucPerfCurr1DayFailedFastR, adslLineTransAtucConfig=adslLineTransAtucConfig, adslAtucPerfPrev1DayFailedFastR=adslAtucPerfPrev1DayFailedFastR, adslAtucPerfCurr15MinFailedFastR=adslAtucPerfCurr15MinFailedFastR, PYSNMP_MODULE_ID=adslExtMIB, adslAtucPerfCurr1DayUasL=adslAtucPerfCurr1DayUasL, adslAturThreshold15MinSesL=adslAturThreshold15MinSesL, adslConfProfileExtEntry=adslConfProfileExtEntry, adslAturPerfPrev1DaySesL=adslAturPerfPrev1DaySesL, adslAtucIntervalUasL=adslAtucIntervalUasL, adslAtucThreshold15MinUasL=adslAtucThreshold15MinUasL, adslAtucPerfCurr1DaySesL=adslAtucPerfCurr1DaySesL, adslAtucPerfStatUasL=adslAtucPerfStatUasL, adslAturIntervalExtTable=adslAturIntervalExtTable, adslAtucPerfPrev1DayFastR=adslAtucPerfPrev1DayFastR, adslAturPerfCurr1DaySesL=adslAturPerfCurr1DaySesL)
