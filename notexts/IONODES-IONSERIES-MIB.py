#
# PySNMP MIB module IONODES-IONSERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ionodes/IONODES-IONSERIES-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:30:24 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, Gauge32, Unsigned32, Counter32, TimeTicks, Counter64, ObjectIdentity, enterprises, iso, NotificationType, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Unsigned32", "Counter32", "TimeTicks", "Counter64", "ObjectIdentity", "enterprises", "iso", "NotificationType", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class AnalogVideoSignalLockState(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("locked", 1), ("unlocked", 2))

class AnalogVideoStandard(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ntsc", 1), ("pal", 2))

class DigitalVideoConnState(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("connected", 1), ("notconnected", 2))

class DigitalVideoStandard(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("hdmi720p", 1), ("hdmi720p50", 2), ("hdmi1080i", 3), ("hdmi1080i50", 4), ("hdmi1080p", 5), ("hdmi1080p50", 6), ("hdmi1080p25", 7), ("hdmi1080p30", 8))

class StreamState(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("connected", 1), ("notconnected", 2))

class IoPinState(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("open", 1), ("closed", 2))

ionSeriesModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 40748, 1, 1, 1))
if mibBuilder.loadTexts: ionSeriesModule.setLastUpdated('201506180000Z')
if mibBuilder.loadTexts: ionSeriesModule.setOrganization('IONODES Inc.')
ionodes = MibIdentifier((1, 3, 6, 1, 4, 1, 40748))
ionReg = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1))
ionModules = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 1))
ionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 2))
ionObjectGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 40748, 1, 2, 1)).setObjects(("IONODES-IONSERIES-MIB", "ionSysCpuUsage"), ("IONODES-IONSERIES-MIB", "ionSysMemUsage"), ("IONODES-IONSERIES-MIB", "ionSysTemperature"), ("IONODES-IONSERIES-MIB", "ionVInNumber"), ("IONODES-IONSERIES-MIB", "ionVInIndex"), ("IONODES-IONSERIES-MIB", "ionVInDescr"), ("IONODES-IONSERIES-MIB", "ionVInAnalogSignalLock"), ("IONODES-IONSERIES-MIB", "ionVInAnalogStandard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ionObjectGroups = ionObjectGroups.setStatus('current')
ionProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3))
ionIONSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3, 1))
ionE100 = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 1))
ionE400 = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 2))
ionE100Mini = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 3))
ionE100HD = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 4))
ionR100 = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 5))
tve110sd = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3, 1, 6))
ionCIRRUSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 3, 2))
ionSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 2))
ionSysCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 40748, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: ionSysCpuUsage.setStatus('current')
ionSysMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 40748, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: ionSysMemUsage.setStatus('current')
ionSysTemperature = MibScalar((1, 3, 6, 1, 4, 1, 40748, 2, 3), Integer32()).setUnits('Celcius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ionSysTemperature.setStatus('current')
ionVideoInputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 3))
ionVInNumber = MibScalar((1, 3, 6, 1, 4, 1, 40748, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInNumber.setStatus('current')
ionVInTable = MibTable((1, 3, 6, 1, 4, 1, 40748, 3, 2), )
if mibBuilder.loadTexts: ionVInTable.setStatus('current')
ionVInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1), ).setIndexNames((0, "IONODES-IONSERIES-MIB", "ionVInIndex"))
if mibBuilder.loadTexts: ionVInEntry.setStatus('current')
ionVInIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInIndex.setStatus('current')
ionVInDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInDescr.setStatus('current')
ionVInAnalogSignalLock = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 3), AnalogVideoSignalLockState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInAnalogSignalLock.setStatus('current')
ionVInAnalogStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 4), AnalogVideoStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInAnalogStandard.setStatus('current')
ionVInDigitalConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 5), DigitalVideoConnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInDigitalConnState.setStatus('current')
ionVInDigitalStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 6), DigitalVideoStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInDigitalStandard.setStatus('current')
ionVideoOutputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 4))
ionVOutNumber = MibScalar((1, 3, 6, 1, 4, 1, 40748, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutNumber.setStatus('current')
ionVOutTable = MibTable((1, 3, 6, 1, 4, 1, 40748, 4, 2), )
if mibBuilder.loadTexts: ionVOutTable.setStatus('current')
ionVOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1), ).setIndexNames((0, "IONODES-IONSERIES-MIB", "ionVOutIndex"))
if mibBuilder.loadTexts: ionVOutEntry.setStatus('current')
ionVOutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutIndex.setStatus('current')
ionVOutDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutDescr.setStatus('current')
ionVOutAnalogSignalLock = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 3), AnalogVideoSignalLockState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutAnalogSignalLock.setStatus('current')
ionVOutAnalogStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 4), AnalogVideoStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutAnalogStandard.setStatus('current')
ionVOutDigitalConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 5), DigitalVideoConnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutDigitalConnState.setStatus('current')
ionVOutDigitalStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 6), DigitalVideoStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutDigitalStandard.setStatus('current')
ionVOutStream1State = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 7), StreamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutStream1State.setStatus('current')
ionVOutStream2State = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 8), StreamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutStream2State.setStatus('current')
ionVOutStream3State = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 9), StreamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutStream3State.setStatus('current')
ionVOutStream4State = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 10), StreamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutStream4State.setStatus('current')
ionAudioInputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 5))
ionAudioOutputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 6))
ionIoInputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 7))
ionIoInNumber = MibScalar((1, 3, 6, 1, 4, 1, 40748, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoInNumber.setStatus('current')
ionIoInTable = MibTable((1, 3, 6, 1, 4, 1, 40748, 7, 2), )
if mibBuilder.loadTexts: ionIoInTable.setStatus('current')
ionIoInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40748, 7, 2, 1), ).setIndexNames((0, "IONODES-IONSERIES-MIB", "ionIoInIndex"))
if mibBuilder.loadTexts: ionIoInEntry.setStatus('current')
ionIoInIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoInIndex.setStatus('current')
ionIoInDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoInDescr.setStatus('current')
ionIoInPinState = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 3), IoPinState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoInPinState.setStatus('current')
ionIoOutputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 8))
ionIoOutNumber = MibScalar((1, 3, 6, 1, 4, 1, 40748, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoOutNumber.setStatus('current')
ionIoOutTable = MibTable((1, 3, 6, 1, 4, 1, 40748, 8, 2), )
if mibBuilder.loadTexts: ionIoOutTable.setStatus('current')
ionIoOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40748, 8, 2, 1), ).setIndexNames((0, "IONODES-IONSERIES-MIB", "ionIoOutIndex"))
if mibBuilder.loadTexts: ionIoOutEntry.setStatus('current')
ionIoOutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoOutIndex.setStatus('current')
ionIoOutDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoOutDescr.setStatus('current')
ionIoOutPinState = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 3), IoPinState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoOutPinState.setStatus('current')
ionSerialPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 9))
mibBuilder.exportSymbols("IONODES-IONSERIES-MIB", ionIoOutEntry=ionIoOutEntry, ionConformance=ionConformance, ionodes=ionodes, ionVInTable=ionVInTable, ionSysCpuUsage=ionSysCpuUsage, ionIoInDescr=ionIoInDescr, ionIoOutputs=ionIoOutputs, PYSNMP_MODULE_ID=ionSeriesModule, ionIoInEntry=ionIoInEntry, ionIoOutDescr=ionIoOutDescr, ionSerialPorts=ionSerialPorts, ionVOutAnalogStandard=ionVOutAnalogStandard, ionIoInputs=ionIoInputs, ionVOutDigitalStandard=ionVOutDigitalStandard, ionIoOutNumber=ionIoOutNumber, ionIONSeries=ionIONSeries, ionSystem=ionSystem, ionSysMemUsage=ionSysMemUsage, DigitalVideoStandard=DigitalVideoStandard, ionIoInTable=ionIoInTable, ionVInDigitalConnState=ionVInDigitalConnState, ionVOutStream1State=ionVOutStream1State, tve110sd=tve110sd, ionVOutDigitalConnState=ionVOutDigitalConnState, ionVInIndex=ionVInIndex, ionVInAnalogSignalLock=ionVInAnalogSignalLock, ionIoInNumber=ionIoInNumber, ionE400=ionE400, ionVOutStream3State=ionVOutStream3State, ionVOutIndex=ionVOutIndex, ionVInAnalogStandard=ionVInAnalogStandard, ionVOutAnalogSignalLock=ionVOutAnalogSignalLock, ionAudioOutputs=ionAudioOutputs, ionVOutEntry=ionVOutEntry, StreamState=StreamState, AnalogVideoSignalLockState=AnalogVideoSignalLockState, ionVInEntry=ionVInEntry, ionIoInIndex=ionIoInIndex, ionVInDigitalStandard=ionVInDigitalStandard, ionVOutStream2State=ionVOutStream2State, ionVOutTable=ionVOutTable, ionVOutNumber=ionVOutNumber, ionSysTemperature=ionSysTemperature, IoPinState=IoPinState, ionVOutStream4State=ionVOutStream4State, ionSeriesModule=ionSeriesModule, ionVideoInputs=ionVideoInputs, ionVInNumber=ionVInNumber, ionModules=ionModules, ionVOutDescr=ionVOutDescr, DigitalVideoConnState=DigitalVideoConnState, ionAudioInputs=ionAudioInputs, ionE100Mini=ionE100Mini, ionIoOutTable=ionIoOutTable, ionCIRRUSSeries=ionCIRRUSSeries, ionVideoOutputs=ionVideoOutputs, ionProducts=ionProducts, ionIoInPinState=ionIoInPinState, ionReg=ionReg, ionE100HD=ionE100HD, AnalogVideoStandard=AnalogVideoStandard, ionE100=ionE100, ionIoOutIndex=ionIoOutIndex, ionIoOutPinState=ionIoOutPinState, ionR100=ionR100, ionObjectGroups=ionObjectGroups, ionVInDescr=ionVInDescr)
