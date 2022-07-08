#
# PySNMP MIB module ADTRAN-AOS-DS1-EXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-DS1-EXT
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:13 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
adGenAOSConformance, adGenAOSWan = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSWan")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, IpAddress, Counter64, Bits, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Unsigned32, ObjectIdentity, ModuleIdentity, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Counter64", "Bits", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "iso", "NotificationType")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
adGenAOSDs1ThresholdsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 6, 1))
if mibBuilder.loadTexts: adGenAOSDs1ThresholdsMib.setLastUpdated('200507060000Z')
if mibBuilder.loadTexts: adGenAOSDs1ThresholdsMib.setOrganization('ADTRAN, Inc.')
adGenAOSDs1Threshold = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1))
adGenAOSDs1ThresholdTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 0))
if mibBuilder.loadTexts: adGenAOSDs1ThresholdTraps.setStatus('current')
adGenAOSDs1ThresholdsReachedTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1), )
if mibBuilder.loadTexts: adGenAOSDs1ThresholdsReachedTable.setStatus('current')
adGenAOSDs1ThresholdsReachedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenAOSDs1ThresholdsReachedEntry.setStatus('current')
adGenAOSDs1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSDs1Index.setStatus('current')
adGenAOSDs1ThresholdAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("ds1ThresholdReached15MinBES", 0), ("ds1ThresholdReached15MinCSS", 1), ("ds1ThresholdReached15MinDM", 2), ("ds1ThresholdReached15MinES", 3), ("ds1ThresholdReached15MinLCV", 4), ("ds1ThresholdReached15MinLES", 5), ("ds1ThresholdReached15MinPCV", 6), ("ds1ThresholdReached15MinSES", 7), ("ds1ThresholdReached15MinSEFS", 8), ("ds1ThresholdReached15MinUAS", 9), ("ds1ThresholdReached24HrBES", 10), ("ds1ThresholdReached24HrCSS", 11), ("ds1ThresholdReached24HrDM", 12), ("ds1ThresholdReached24HrES", 13), ("ds1ThresholdReached24HrLCV", 14), ("ds1ThresholdReached24HrLES", 15), ("ds1ThresholdReached24HrPCV", 16), ("ds1ThresholdReached24HrSES", 17), ("ds1ThresholdReached24HrSEFS", 18), ("ds1ThresholdReached24HrUAS", 19)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSDs1ThresholdAlarms.setStatus('current')
adGenAOSDs1PreviousThresholdAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1, 3), Bits().clone(namedValues=NamedValues(("ds1ThresholdReached15MinBES", 0), ("ds1ThresholdReached15MinCSS", 1), ("ds1ThresholdReached15MinDM", 2), ("ds1ThresholdReached15MinES", 3), ("ds1ThresholdReached15MinLCV", 4), ("ds1ThresholdReached15MinLES", 5), ("ds1ThresholdReached15MinPCV", 6), ("ds1ThresholdReached15MinSES", 7), ("ds1ThresholdReached15MinSEFS", 8), ("ds1ThresholdReached15MinUAS", 9), ("ds1ThresholdReached24HrBES", 10), ("ds1ThresholdReached24HrCSS", 11), ("ds1ThresholdReached24HrDM", 12), ("ds1ThresholdReached24HrES", 13), ("ds1ThresholdReached24HrLCV", 14), ("ds1ThresholdReached24HrLES", 15), ("ds1ThresholdReached24HrPCV", 16), ("ds1ThresholdReached24HrSES", 17), ("ds1ThresholdReached24HrSEFS", 18), ("ds1ThresholdReached24HrUAS", 19)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSDs1PreviousThresholdAlarms.setStatus('current')
adGenAOSDs1LastThresholdChange = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSDs1LastThresholdChange.setStatus('current')
adGenAOSDs1Threshold15MinBES = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinBES.setStatus('current')
adGenAOSDs1Threshold15MinCSS = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinCSS.setStatus('current')
adGenAOSDs1Threshold15MinDM = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinDM.setStatus('current')
adGenAOSDs1Threshold15MinES = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(65)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinES.setStatus('current')
adGenAOSDs1Threshold15MinLCV = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(13340)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinLCV.setStatus('current')
adGenAOSDs1Threshold15MinLES = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(65)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinLES.setStatus('current')
adGenAOSDs1Threshold15MinPCV = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(72)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinPCV.setStatus('current')
adGenAOSDs1Threshold15MinSES = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinSES.setStatus('current')
adGenAOSDs1Threshold15MinSEFS = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinSEFS.setStatus('current')
adGenAOSDs1Threshold15MinUAS = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold15MinUAS.setStatus('current')
adGenAOSDs1Threshold24HrBES = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrBES.setStatus('current')
adGenAOSDs1Threshold24HrCSS = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrCSS.setStatus('current')
adGenAOSDs1Threshold24HrDM = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrDM.setStatus('current')
adGenAOSDs1Threshold24HrES = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(648)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrES.setStatus('current')
adGenAOSDs1Threshold24HrLCV = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(133400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrLCV.setStatus('current')
adGenAOSDs1Threshold24HrLES = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(648)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrLES.setStatus('current')
adGenAOSDs1Threshold24HrPCV = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(691)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrPCV.setStatus('current')
adGenAOSDs1Threshold24HrSES = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrSES.setStatus('current')
adGenAOSDs1Threshold24HrSEFS = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(17)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrSEFS.setStatus('current')
adGenAOSDs1Threshold24HrUAS = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 21), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSDs1Threshold24HrUAS.setStatus('current')
adGenAOSDs1ThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 1, 0, 1)).setObjects(("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1ThresholdAlarms"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1PreviousThresholdAlarms"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1LastThresholdChange"))
if mibBuilder.loadTexts: adGenAOSDs1ThresholdReached.setStatus('current')
adGenAOSDs1ThresholdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6))
adAOSDs1ThresholdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6, 1))
adAOSDs1ThresholdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6, 2))
adAOSDs1ThresholdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6, 1, 1)).setObjects(("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1ThresholdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSDs1ThresholdCompliance = adAOSDs1ThresholdCompliance.setStatus('current')
adGenAOSDs1ThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 6, 2, 1)).setObjects(("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Index"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1PreviousThresholdAlarms"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1LastThresholdChange"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1ThresholdAlarms"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinBES"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinCSS"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinDM"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinES"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinLCV"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinLES"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinPCV"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinSES"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinSEFS"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold15MinUAS"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrBES"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrCSS"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrDM"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrES"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrLCV"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrLES"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrPCV"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrSES"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrSEFS"), ("ADTRAN-AOS-DS1-EXT", "adGenAOSDs1Threshold24HrUAS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDs1ThresholdGroup = adGenAOSDs1ThresholdGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-DS1-EXT", adGenAOSDs1Threshold15MinBES=adGenAOSDs1Threshold15MinBES, adGenAOSDs1ThresholdTraps=adGenAOSDs1ThresholdTraps, adGenAOSDs1Threshold24HrES=adGenAOSDs1Threshold24HrES, adGenAOSDs1ThresholdsMib=adGenAOSDs1ThresholdsMib, adGenAOSDs1Threshold24HrCSS=adGenAOSDs1Threshold24HrCSS, adGenAOSDs1Threshold24HrLCV=adGenAOSDs1Threshold24HrLCV, adAOSDs1ThresholdCompliance=adAOSDs1ThresholdCompliance, adGenAOSDs1Threshold15MinLES=adGenAOSDs1Threshold15MinLES, adGenAOSDs1Threshold15MinDM=adGenAOSDs1Threshold15MinDM, adGenAOSDs1Threshold=adGenAOSDs1Threshold, adGenAOSDs1Threshold15MinES=adGenAOSDs1Threshold15MinES, adGenAOSDs1ThresholdsReachedEntry=adGenAOSDs1ThresholdsReachedEntry, adGenAOSDs1ThresholdGroup=adGenAOSDs1ThresholdGroup, adGenAOSDs1Threshold24HrSES=adGenAOSDs1Threshold24HrSES, adGenAOSDs1PreviousThresholdAlarms=adGenAOSDs1PreviousThresholdAlarms, adGenAOSDs1Threshold24HrBES=adGenAOSDs1Threshold24HrBES, adGenAOSDs1LastThresholdChange=adGenAOSDs1LastThresholdChange, adGenAOSDs1Threshold24HrDM=adGenAOSDs1Threshold24HrDM, adGenAOSDs1Threshold15MinLCV=adGenAOSDs1Threshold15MinLCV, adGenAOSDs1Threshold15MinSES=adGenAOSDs1Threshold15MinSES, adGenAOSDs1ThresholdReached=adGenAOSDs1ThresholdReached, adGenAOSDs1ThresholdAlarms=adGenAOSDs1ThresholdAlarms, PYSNMP_MODULE_ID=adGenAOSDs1ThresholdsMib, adGenAOSDs1Threshold24HrSEFS=adGenAOSDs1Threshold24HrSEFS, adGenAOSDs1ThresholdConformance=adGenAOSDs1ThresholdConformance, adGenAOSDs1Threshold15MinCSS=adGenAOSDs1Threshold15MinCSS, adGenAOSDs1Threshold24HrPCV=adGenAOSDs1Threshold24HrPCV, adGenAOSDs1Index=adGenAOSDs1Index, adGenAOSDs1Threshold24HrUAS=adGenAOSDs1Threshold24HrUAS, adGenAOSDs1ThresholdsReachedTable=adGenAOSDs1ThresholdsReachedTable, adAOSDs1ThresholdCompliances=adAOSDs1ThresholdCompliances, adGenAOSDs1Threshold15MinSEFS=adGenAOSDs1Threshold15MinSEFS, adGenAOSDs1Threshold24HrLES=adGenAOSDs1Threshold24HrLES, adGenAOSDs1Threshold15MinPCV=adGenAOSDs1Threshold15MinPCV, adGenAOSDs1Threshold15MinUAS=adGenAOSDs1Threshold15MinUAS, adAOSDs1ThresholdGroups=adAOSDs1ThresholdGroups)
