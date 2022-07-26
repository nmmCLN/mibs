#
# PySNMP MIB module AVIAT-RXPERFORMANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-RXPERFORMANCE-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:23:43 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
AviatPowerLevel, = mibBuilder.importSymbols("AVIAT-TEXTCONVENTION-MIB", "AviatPowerLevel")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Bits, Integer32, Counter64, ObjectIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Gauge32, iso, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Integer32", "Counter64", "ObjectIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Gauge32", "iso", "Unsigned32", "TimeTicks")
TruthValue, DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "DateAndTime")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatRxPerformanceModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 15))
aviatRxPerformanceModule.setRevisions(('2014-01-21 01:57',))
if mibBuilder.loadTexts: aviatRxPerformanceModule.setLastUpdated('201401210157Z')
if mibBuilder.loadTexts: aviatRxPerformanceModule.setOrganization('Aviat Networks')
class AviatPackedRxPerformData(TextualConvention, OctetString):
    status = 'current'
    displayHint = '63x'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(63, 63), )
aviatRxPerformanceConf = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 15, 1))
aviatRxPerformanceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 15, 1, 1))
aviatRxPerformanceCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 15, 1, 2))
aviatRxPerformanceMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2))
aviatRxPerformControlTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1), )
if mibBuilder.loadTexts: aviatRxPerformControlTable.setStatus('current')
aviatRxPerformControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRxPerformControlEntry.setStatus('current')
aviatRxPerformReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("all", 2), ("realtime", 3), ("quarterhour", 4), ("daily", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatRxPerformReset.setStatus('current')
aviatRxPerformLastQHourChangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformLastQHourChangeIndex.setStatus('current')
aviatRxPerformLastDayChangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformLastDayChangeIndex.setStatus('current')
aviatRxPerformTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2), )
if mibBuilder.loadTexts: aviatRxPerformTable.setStatus('current')
aviatRxPerformEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatRxPerformEntry.setStatus('current')
aviatRxPerformRslReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 3), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformRslReadingMean.setStatus('current')
aviatRxPerformRslReadingCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 4), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformRslReadingCurrent.setStatus('current')
aviatRxPerformRslReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 5), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformRslReadingMax.setStatus('current')
aviatRxPerformRslReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 6), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformRslReadingMin.setStatus('current')
aviatRxPerformBerReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformBerReadingMean.setStatus('current')
aviatRxPerformBerReadingCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformBerReadingCurrent.setStatus('current')
aviatRxPerformBerReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformBerReadingMax.setStatus('current')
aviatRxPerformBerReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformBerReadingMin.setStatus('current')
aviatRxPerformFrameLossSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformFrameLossSeconds.setStatus('current')
aviatRxPerformPackedData = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 2, 1, 12), AviatPackedRxPerformData()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformPackedData.setStatus('current')
aviatRxPerformQuarterHourTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3), )
if mibBuilder.loadTexts: aviatRxPerformQuarterHourTable.setStatus('current')
aviatRxPerformQuarterHourEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourIndex"), (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourPeriod"))
if mibBuilder.loadTexts: aviatRxPerformQuarterHourEntry.setStatus('current')
aviatRxPerformQHourIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 1), Gauge32())
if mibBuilder.loadTexts: aviatRxPerformQHourIndex.setStatus('current')
aviatRxPerformQHourPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 2), Gauge32())
if mibBuilder.loadTexts: aviatRxPerformQHourPeriod.setStatus('current')
aviatRxPerformQHourDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourDateAndTime.setStatus('current')
aviatRxPerformQHourRslReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 5), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourRslReadingMean.setStatus('current')
aviatRxPerformQHourRslReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 6), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourRslReadingMax.setStatus('current')
aviatRxPerformQHourRslReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 7), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourRslReadingMin.setStatus('current')
aviatRxPerformQHourBerReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourBerReadingMean.setStatus('current')
aviatRxPerformQHourBerReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourBerReadingMax.setStatus('current')
aviatRxPerformQHourBerReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourBerReadingMin.setStatus('current')
aviatRxPerformQHourFrameLossSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourFrameLossSeconds.setStatus('current')
aviatRxPerformQHourInvalidEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 3, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformQHourInvalidEntry.setStatus('current')
aviatRxPerformDayTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4), )
if mibBuilder.loadTexts: aviatRxPerformDayTable.setStatus('current')
aviatRxPerformDayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayIndex"), (0, "AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayPeriod"))
if mibBuilder.loadTexts: aviatRxPerformDayEntry.setStatus('current')
aviatRxPerformDayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 1), Gauge32())
if mibBuilder.loadTexts: aviatRxPerformDayIndex.setStatus('current')
aviatRxPerformDayPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 2), Gauge32())
if mibBuilder.loadTexts: aviatRxPerformDayPeriod.setStatus('current')
aviatRxPerformDayDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayDateAndTime.setStatus('current')
aviatRxPerformDayRslReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 5), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayRslReadingMean.setStatus('current')
aviatRxPerformDayRslReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 6), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayRslReadingMax.setStatus('current')
aviatRxPerformDayRslReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 7), AviatPowerLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayRslReadingMin.setStatus('current')
aviatRxPerformDayBerReadingMean = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayBerReadingMean.setStatus('current')
aviatRxPerformDayBerReadingMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayBerReadingMax.setStatus('current')
aviatRxPerformDayBerReadingMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayBerReadingMin.setStatus('current')
aviatRxPerformDayFrameLossSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayFrameLossSeconds.setStatus('current')
aviatRxPerformDayInvalidEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 15, 2, 4, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatRxPerformDayInvalidEntry.setStatus('current')
aviatRxPerformObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 15, 1, 1, 1)).setObjects(("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformReset"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformLastQHourChangeIndex"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformLastDayChangeIndex"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformRslReadingMean"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformRslReadingCurrent"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformRslReadingMax"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformRslReadingMin"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformBerReadingMean"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformBerReadingCurrent"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformBerReadingMax"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformBerReadingMin"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformFrameLossSeconds"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformPackedData"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourDateAndTime"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourRslReadingMean"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourRslReadingMax"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourRslReadingMin"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourBerReadingMean"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourBerReadingMax"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourBerReadingMin"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourFrameLossSeconds"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformQHourInvalidEntry"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayDateAndTime"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayRslReadingMean"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayRslReadingMax"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayRslReadingMin"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayBerReadingMean"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayBerReadingMax"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayBerReadingMin"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayFrameLossSeconds"), ("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformDayInvalidEntry"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatRxPerformObjectGroup = aviatRxPerformObjectGroup.setStatus('current')
aviatRxPerformanceComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2509, 9, 15, 1, 2, 1)).setObjects(("AVIAT-RXPERFORMANCE-MIB", "aviatRxPerformObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatRxPerformanceComplV1 = aviatRxPerformanceComplV1.setStatus('current')
mibBuilder.exportSymbols("AVIAT-RXPERFORMANCE-MIB", aviatRxPerformDayBerReadingMin=aviatRxPerformDayBerReadingMin, aviatRxPerformQuarterHourTable=aviatRxPerformQuarterHourTable, aviatRxPerformLastQHourChangeIndex=aviatRxPerformLastQHourChangeIndex, aviatRxPerformLastDayChangeIndex=aviatRxPerformLastDayChangeIndex, aviatRxPerformQHourBerReadingMean=aviatRxPerformQHourBerReadingMean, aviatRxPerformanceMIBObjs=aviatRxPerformanceMIBObjs, aviatRxPerformDayBerReadingMean=aviatRxPerformDayBerReadingMean, aviatRxPerformBerReadingMean=aviatRxPerformBerReadingMean, aviatRxPerformBerReadingMin=aviatRxPerformBerReadingMin, aviatRxPerformRslReadingMean=aviatRxPerformRslReadingMean, aviatRxPerformEntry=aviatRxPerformEntry, aviatRxPerformanceComplV1=aviatRxPerformanceComplV1, aviatRxPerformDayRslReadingMin=aviatRxPerformDayRslReadingMin, aviatRxPerformQHourRslReadingMean=aviatRxPerformQHourRslReadingMean, aviatRxPerformanceGroups=aviatRxPerformanceGroups, aviatRxPerformFrameLossSeconds=aviatRxPerformFrameLossSeconds, aviatRxPerformDayBerReadingMax=aviatRxPerformDayBerReadingMax, aviatRxPerformQHourBerReadingMin=aviatRxPerformQHourBerReadingMin, aviatRxPerformDayInvalidEntry=aviatRxPerformDayInvalidEntry, aviatRxPerformControlTable=aviatRxPerformControlTable, aviatRxPerformDayEntry=aviatRxPerformDayEntry, aviatRxPerformQHourInvalidEntry=aviatRxPerformQHourInvalidEntry, aviatRxPerformDayIndex=aviatRxPerformDayIndex, aviatRxPerformBerReadingCurrent=aviatRxPerformBerReadingCurrent, aviatRxPerformQHourRslReadingMin=aviatRxPerformQHourRslReadingMin, aviatRxPerformObjectGroup=aviatRxPerformObjectGroup, aviatRxPerformTable=aviatRxPerformTable, aviatRxPerformRslReadingCurrent=aviatRxPerformRslReadingCurrent, aviatRxPerformQHourRslReadingMax=aviatRxPerformQHourRslReadingMax, aviatRxPerformDayPeriod=aviatRxPerformDayPeriod, aviatRxPerformControlEntry=aviatRxPerformControlEntry, aviatRxPerformanceModule=aviatRxPerformanceModule, aviatRxPerformQHourDateAndTime=aviatRxPerformQHourDateAndTime, AviatPackedRxPerformData=AviatPackedRxPerformData, aviatRxPerformDayRslReadingMean=aviatRxPerformDayRslReadingMean, aviatRxPerformQHourIndex=aviatRxPerformQHourIndex, aviatRxPerformQHourFrameLossSeconds=aviatRxPerformQHourFrameLossSeconds, aviatRxPerformRslReadingMax=aviatRxPerformRslReadingMax, aviatRxPerformDayDateAndTime=aviatRxPerformDayDateAndTime, aviatRxPerformQuarterHourEntry=aviatRxPerformQuarterHourEntry, PYSNMP_MODULE_ID=aviatRxPerformanceModule, aviatRxPerformPackedData=aviatRxPerformPackedData, aviatRxPerformReset=aviatRxPerformReset, aviatRxPerformQHourBerReadingMax=aviatRxPerformQHourBerReadingMax, aviatRxPerformanceCompl=aviatRxPerformanceCompl, aviatRxPerformQHourPeriod=aviatRxPerformQHourPeriod, aviatRxPerformDayRslReadingMax=aviatRxPerformDayRslReadingMax, aviatRxPerformBerReadingMax=aviatRxPerformBerReadingMax, aviatRxPerformDayTable=aviatRxPerformDayTable, aviatRxPerformanceConf=aviatRxPerformanceConf, aviatRxPerformDayFrameLossSeconds=aviatRxPerformDayFrameLossSeconds, aviatRxPerformRslReadingMin=aviatRxPerformRslReadingMin)
