#
# PySNMP MIB module PEGASUS-SDH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pegasus/PEGASUS-SDH-MIB
# Produced by pysmi-1.1.11 at Wed Apr  3 13:48:42 2024
# On host fv-az1499-203 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "InterfaceIndexOrZero")
AvailabilityStatusElem, CommStateEnum, pegasusMibModule, OperStateEnum = mibBuilder.importSymbols("PEGASUS-MIB", "AvailabilityStatusElem", "CommStateEnum", "pegasusMibModule", "OperStateEnum")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Counter64, IpAddress, NotificationType, MibIdentifier, Gauge32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Counter64", "IpAddress", "NotificationType", "MibIdentifier", "Gauge32", "Counter32", "TimeTicks")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
pegasusSdhMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6368, 2, 8))
pegasusSdhMibModule.setRevisions(('2004-03-18 00:00', '2004-01-07 00:00', '2003-11-17 00:00',))
if mibBuilder.loadTexts: pegasusSdhMibModule.setLastUpdated('200403180000Z')
if mibBuilder.loadTexts: pegasusSdhMibModule.setOrganization('Schmid Telecom, Zurich')
class ClockSourceEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rxLineClock", 1), ("referenceClock", 2), ("freeRun", 3))

class ClockSyncStateEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("syncOk", 1), ("syncNotOk", 2))

class ClockModeEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class ClockPriorityEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class ClockQualityEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("prc", 1), ("ssu-a", 2), ("ssu-b", 3), ("sec", 4), ("dnu", 5), ("auto", 6), ("unknown", 7))

class ClockStateEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("invalid", 1), ("valid", 2))

class MultiplexingModeEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("au3", 1), ("au4", 2))

class VirtualContainerTypeEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vc4", 1), ("vc3", 2), ("vc12", 3))

class LaserOperationModeEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("off", 1), ("als", 2))

class LaserStateEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("on", 1), ("shutdown", 2), ("restart", 3))

class SdhInterfaceEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("optical", 1), ("e1", 2))

class PRBSPatternEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pattern2exp15", 1), ("pattern2exp20", 2))

class TraceSizeEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("size1byte", 1), ("size16byte", 2))

class SignalLabel(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 7), ValueRangeConstraint(18, 26), ValueRangeConstraint(207, 207), ValueRangeConstraint(225, 252), ValueRangeConstraint(254, 255), )
class ConcatenationTypeEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("lcas", 1), ("nonLCAS", 2))

class EthernetIfEncapsulationEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 1), ("gfp", 2), ("lapf", 3), ("laps", 4), ("ppp", 5))

class OrderLevelEnum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("highOrder", 1), ("lowOrder", 2))

class STM1SlotNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2, 2)

class TUGIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

class TUGIndexOrZero(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 3)

stm1CardTable = MibTable((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1), )
if mibBuilder.loadTexts: stm1CardTable.setStatus('current')
stm1CardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1), ).setIndexNames((0, "PEGASUS-SDH-MIB", "stm1CardSlotNumber"))
if mibBuilder.loadTexts: stm1CardEntry.setStatus('current')
stm1CardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 1), STM1SlotNumber())
if mibBuilder.loadTexts: stm1CardSlotNumber.setStatus('current')
stm1CardName = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardName.setStatus('current')
stm1CardHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardHardwareVersion.setStatus('current')
stm1CardFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardFirmwareVersion.setStatus('current')
stm1CardManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardManufacturer.setStatus('current')
stm1CardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardSerialNumber.setStatus('current')
stm1CardMultiplexingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 7), MultiplexingModeEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardMultiplexingMode.setStatus('current')
stm1CardJ0TraceMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 8), OperStateEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardJ0TraceMonitoring.setStatus('current')
stm1CardJ1TraceMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 9), OperStateEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardJ1TraceMonitoring.setStatus('current')
stm1CardJ2TraceMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 10), OperStateEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardJ2TraceMonitoring.setStatus('current')
stm1CardJ0PathTraceSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 11), TraceSizeEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardJ0PathTraceSize.setStatus('current')
stm1CardJ0PathTraceSend = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardJ0PathTraceSend.setStatus('current')
stm1CardJ0PathTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardJ0PathTraceExpected.setStatus('current')
stm1CardJ0PathTraceReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardJ0PathTraceReceive.setStatus('current')
stm1CardLaserOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 15), LaserOperationModeEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardLaserOperationMode.setStatus('current')
stm1CardLaserState = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 16), LaserStateEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardLaserState.setStatus('current')
stm1CardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 17), OperStateEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardOperState.setStatus('current')
stm1CardAvailabilityState = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 18), AvailabilityStatusElem()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardAvailabilityState.setStatus('current')
stm1CardMgmtCommState = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 19), CommStateEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardMgmtCommState.setStatus('current')
stm1CardPRBSGeneratorSink = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 20), SdhInterfaceEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardPRBSGeneratorSink.setStatus('current')
stm1CardPRBSAnalyzerSource = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 21), SdhInterfaceEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardPRBSAnalyzerSource.setStatus('current')
stm1CardPRBSPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 22), PRBSPatternEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardPRBSPattern.setStatus('current')
stm1CardAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardAlarmStatus.setStatus('current')
stm1CardClockTable = MibTable((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2), )
if mibBuilder.loadTexts: stm1CardClockTable.setStatus('current')
stm1CardClockEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1), ).setIndexNames((0, "PEGASUS-SDH-MIB", "stm1CardSlotNumber"))
if mibBuilder.loadTexts: stm1CardClockEntry.setStatus('current')
stm1CardActiveClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 1), ClockSourceEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardActiveClockSource.setStatus('current')
stm1CardClockSyncState = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 2), ClockSyncStateEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardClockSyncState.setStatus('current')
stm1CardTxLineClockQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 3), ClockQualityEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardTxLineClockQuality.setStatus('current')
stm1CardRxClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 4), ClockModeEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardRxClockMode.setStatus('current')
stm1CardRxClockPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 5), ClockPriorityEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardRxClockPriority.setStatus('current')
stm1CardRxClockQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 6), ClockQualityEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardRxClockQuality.setStatus('current')
stm1CardRxClockState = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 7), ClockStateEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardRxClockState.setStatus('current')
stm1CardReferenceClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 8), ClockModeEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardReferenceClockMode.setStatus('current')
stm1CardReferenceClockPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 9), ClockPriorityEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardReferenceClockPriority.setStatus('current')
stm1CardReferenceClockQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 10), ClockQualityEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stm1CardReferenceClockQuality.setStatus('current')
stm1CardReferenceClockState = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 2, 1, 11), ClockStateEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stm1CardReferenceClockState.setStatus('current')
ethernetIfTable = MibTable((1, 3, 6, 1, 4, 1, 6368, 2, 8, 3), )
if mibBuilder.loadTexts: ethernetIfTable.setStatus('current')
ethernetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetIfEntry.setStatus('current')
etherIfConcatenationOption = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1, 1), ConcatenationTypeEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherIfConcatenationOption.setStatus('current')
etherIfEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1, 2), EthernetIfEncapsulationEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherIfEncapsulation.setStatus('current')
etherIfOrderLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1, 3), OrderLevelEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherIfOrderLevel.setStatus('current')
etherIfAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherIfAlarmStatus.setStatus('current')
vcTable = MibTable((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4), )
if mibBuilder.loadTexts: vcTable.setStatus('current')
vcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcEntry.setStatus('current')
vcType = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 1), VirtualContainerTypeEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcType.setStatus('current')
vcRelatedTUG = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 2), TUGIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcRelatedTUG.setStatus('current')
vcRelatedVC = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcRelatedVC.setStatus('current')
vcAssignedIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcAssignedIfIndex.setStatus('current')
vcPathTraceSend = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcPathTraceSend.setStatus('current')
vcPathTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcPathTraceExpected.setStatus('current')
vcPathTraceReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcPathTraceReceive.setStatus('current')
vcSignalLabelSend = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 8), SignalLabel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcSignalLabelSend.setStatus('current')
vcSignalLabelExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 9), SignalLabel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcSignalLabelExpected.setStatus('current')
vcSignalLabelReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 10), SignalLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcSignalLabelReceive.setStatus('current')
vcAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 4, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 524287))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcAlarmStatus.setStatus('current')
tugConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6368, 2, 8, 5), )
if mibBuilder.loadTexts: tugConfigTable.setStatus('current')
tugConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6368, 2, 8, 5, 1), ).setIndexNames((0, "PEGASUS-SDH-MIB", "tugIndex"))
if mibBuilder.loadTexts: tugConfigEntry.setStatus('current')
tugIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 5, 1, 1), TUGIndex())
if mibBuilder.loadTexts: tugIndex.setStatus('current')
tugRelatedVC4 = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 5, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tugRelatedVC4.setStatus('current')
tugOrderLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 6368, 2, 8, 5, 1, 3), OrderLevelEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tugOrderLevel.setStatus('current')
sdhMibRevision = MibScalar((1, 3, 6, 1, 4, 1, 6368, 2, 8, 6), DisplayString().clone('$Workfile: PEGASUS-SDH-MIB.txt $ $Revision: 14 $ $Date: 3/18/04 6:40p $')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sdhMibRevision.setStatus('current')
mibBuilder.exportSymbols("PEGASUS-SDH-MIB", TraceSizeEnum=TraceSizeEnum, stm1CardJ2TraceMonitoring=stm1CardJ2TraceMonitoring, PRBSPatternEnum=PRBSPatternEnum, stm1CardMultiplexingMode=stm1CardMultiplexingMode, stm1CardPRBSAnalyzerSource=stm1CardPRBSAnalyzerSource, ConcatenationTypeEnum=ConcatenationTypeEnum, stm1CardJ1TraceMonitoring=stm1CardJ1TraceMonitoring, sdhMibRevision=sdhMibRevision, tugRelatedVC4=tugRelatedVC4, PYSNMP_MODULE_ID=pegasusSdhMibModule, etherIfAlarmStatus=etherIfAlarmStatus, stm1CardAlarmStatus=stm1CardAlarmStatus, etherIfOrderLevel=etherIfOrderLevel, stm1CardLaserOperationMode=stm1CardLaserOperationMode, vcSignalLabelExpected=vcSignalLabelExpected, MultiplexingModeEnum=MultiplexingModeEnum, EthernetIfEncapsulationEnum=EthernetIfEncapsulationEnum, stm1CardRxClockMode=stm1CardRxClockMode, etherIfEncapsulation=etherIfEncapsulation, stm1CardReferenceClockQuality=stm1CardReferenceClockQuality, stm1CardActiveClockSource=stm1CardActiveClockSource, tugConfigEntry=tugConfigEntry, tugOrderLevel=tugOrderLevel, vcAssignedIfIndex=vcAssignedIfIndex, stm1CardPRBSGeneratorSink=stm1CardPRBSGeneratorSink, ClockModeEnum=ClockModeEnum, ClockStateEnum=ClockStateEnum, vcRelatedTUG=vcRelatedTUG, stm1CardOperState=stm1CardOperState, TUGIndexOrZero=TUGIndexOrZero, tugIndex=tugIndex, stm1CardReferenceClockState=stm1CardReferenceClockState, vcType=vcType, stm1CardPRBSPattern=stm1CardPRBSPattern, vcRelatedVC=vcRelatedVC, vcEntry=vcEntry, stm1CardReferenceClockMode=stm1CardReferenceClockMode, stm1CardJ0PathTraceReceive=stm1CardJ0PathTraceReceive, stm1CardManufacturer=stm1CardManufacturer, stm1CardSlotNumber=stm1CardSlotNumber, SdhInterfaceEnum=SdhInterfaceEnum, ClockPriorityEnum=ClockPriorityEnum, stm1CardClockSyncState=stm1CardClockSyncState, LaserOperationModeEnum=LaserOperationModeEnum, etherIfConcatenationOption=etherIfConcatenationOption, stm1CardSerialNumber=stm1CardSerialNumber, stm1CardJ0PathTraceExpected=stm1CardJ0PathTraceExpected, SignalLabel=SignalLabel, vcAlarmStatus=vcAlarmStatus, pegasusSdhMibModule=pegasusSdhMibModule, ClockQualityEnum=ClockQualityEnum, stm1CardEntry=stm1CardEntry, stm1CardTable=stm1CardTable, ethernetIfEntry=ethernetIfEntry, stm1CardRxClockQuality=stm1CardRxClockQuality, stm1CardName=stm1CardName, stm1CardMgmtCommState=stm1CardMgmtCommState, stm1CardRxClockState=stm1CardRxClockState, vcSignalLabelReceive=vcSignalLabelReceive, stm1CardHardwareVersion=stm1CardHardwareVersion, STM1SlotNumber=STM1SlotNumber, OrderLevelEnum=OrderLevelEnum, vcPathTraceExpected=vcPathTraceExpected, LaserStateEnum=LaserStateEnum, ethernetIfTable=ethernetIfTable, stm1CardJ0PathTraceSize=stm1CardJ0PathTraceSize, TUGIndex=TUGIndex, stm1CardClockTable=stm1CardClockTable, ClockSyncStateEnum=ClockSyncStateEnum, stm1CardJ0PathTraceSend=stm1CardJ0PathTraceSend, vcSignalLabelSend=vcSignalLabelSend, stm1CardReferenceClockPriority=stm1CardReferenceClockPriority, stm1CardRxClockPriority=stm1CardRxClockPriority, stm1CardJ0TraceMonitoring=stm1CardJ0TraceMonitoring, VirtualContainerTypeEnum=VirtualContainerTypeEnum, vcTable=vcTable, stm1CardLaserState=stm1CardLaserState, vcPathTraceReceive=vcPathTraceReceive, stm1CardFirmwareVersion=stm1CardFirmwareVersion, stm1CardTxLineClockQuality=stm1CardTxLineClockQuality, ClockSourceEnum=ClockSourceEnum, stm1CardAvailabilityState=stm1CardAvailabilityState, vcPathTraceSend=vcPathTraceSend, stm1CardClockEntry=stm1CardClockEntry, tugConfigTable=tugConfigTable)
