#
# PySNMP MIB module IONODES-IONSERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ionodes/IONODES-IONSERIES-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:22:57 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, Counter64, ModuleIdentity, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, IpAddress, MibIdentifier, NotificationType, TimeTicks, enterprises, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ModuleIdentity", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "TimeTicks", "enterprises", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class AnalogVideoSignalLockState(TextualConvention, Integer32):
    description = 'Possible analog signal lock states.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("locked", 1), ("unlocked", 2))

class AnalogVideoStandard(TextualConvention, Integer32):
    description = 'Possible analog video standards.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ntsc", 1), ("pal", 2))

class DigitalVideoConnState(TextualConvention, Integer32):
    description = 'Possible digital video connection states.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("connected", 1), ("notconnected", 2))

class DigitalVideoStandard(TextualConvention, Integer32):
    description = 'Possible digital video standards.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("hdmi720p", 1), ("hdmi720p50", 2), ("hdmi1080i", 3), ("hdmi1080i50", 4), ("hdmi1080p", 5), ("hdmi1080p50", 6), ("hdmi1080p25", 7), ("hdmi1080p30", 8))

class StreamState(TextualConvention, Integer32):
    description = 'Possible stream states.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("connected", 1), ("notconnected", 2))

class IoPinState(TextualConvention, Integer32):
    description = 'Possible states of digital I/O pins.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("open", 1), ("closed", 2))

ionSeriesModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 40748, 1, 1, 1))
if mibBuilder.loadTexts: ionSeriesModule.setLastUpdated('201506180000Z')
if mibBuilder.loadTexts: ionSeriesModule.setOrganization('IONODES Inc.')
if mibBuilder.loadTexts: ionSeriesModule.setContactInfo('Stephane Pare\n          IONODES Inc.\n\n          EMail:    stephane.pare@ionodes.com\n          phone:    +1 450 696-1060\n          postal:   1855 rue Bernard-Lefebvre, suite 201\n                    Laval, Qc H7C 0A5\n                    Canada\n         ')
if mibBuilder.loadTexts: ionSeriesModule.setDescription("The MIB module for IONODES' IONSERIES line of products.\n          Copyright (C) IONODES Inc (2013-2015).\n         ")
ionodes = MibIdentifier((1, 3, 6, 1, 4, 1, 40748))
ionReg = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1))
ionModules = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 1))
ionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 1, 2))
ionObjectGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 40748, 1, 2, 1)).setObjects(("IONODES-IONSERIES-MIB", "ionSysCpuUsage"), ("IONODES-IONSERIES-MIB", "ionSysMemUsage"), ("IONODES-IONSERIES-MIB", "ionSysTemperature"), ("IONODES-IONSERIES-MIB", "ionVInNumber"), ("IONODES-IONSERIES-MIB", "ionVInIndex"), ("IONODES-IONSERIES-MIB", "ionVInDescr"), ("IONODES-IONSERIES-MIB", "ionVInAnalogSignalLock"), ("IONODES-IONSERIES-MIB", "ionVInAnalogStandard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ionObjectGroups = ionObjectGroups.setStatus('current')
if mibBuilder.loadTexts: ionObjectGroups.setDescription('Description.')
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
if mibBuilder.loadTexts: ionSysCpuUsage.setDescription('Current core CPU usage percentage.')
ionSysMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 40748, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: ionSysMemUsage.setStatus('current')
if mibBuilder.loadTexts: ionSysMemUsage.setDescription('Current system memory usage percentage.')
ionSysTemperature = MibScalar((1, 3, 6, 1, 4, 1, 40748, 2, 3), Integer32()).setUnits('Celcius').setMaxAccess("readonly")
if mibBuilder.loadTexts: ionSysTemperature.setStatus('current')
if mibBuilder.loadTexts: ionSysTemperature.setDescription('Current system temperature, in degrees celcius.')
ionVideoInputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 3))
ionVInNumber = MibScalar((1, 3, 6, 1, 4, 1, 40748, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInNumber.setStatus('current')
if mibBuilder.loadTexts: ionVInNumber.setDescription('Number of video inputs present.')
ionVInTable = MibTable((1, 3, 6, 1, 4, 1, 40748, 3, 2), )
if mibBuilder.loadTexts: ionVInTable.setStatus('current')
if mibBuilder.loadTexts: ionVInTable.setDescription('Table containing the description of all video inputs present.')
ionVInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1), ).setIndexNames((0, "IONODES-IONSERIES-MIB", "ionVInIndex"))
if mibBuilder.loadTexts: ionVInEntry.setStatus('current')
if mibBuilder.loadTexts: ionVInEntry.setDescription('Description of a video input.')
ionVInIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInIndex.setStatus('current')
if mibBuilder.loadTexts: ionVInIndex.setDescription('Index of the video input (1-based).')
ionVInDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInDescr.setStatus('current')
if mibBuilder.loadTexts: ionVInDescr.setDescription('Video input user-friendly name.')
ionVInAnalogSignalLock = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 3), AnalogVideoSignalLockState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInAnalogSignalLock.setStatus('current')
if mibBuilder.loadTexts: ionVInAnalogSignalLock.setDescription('Analog signal lock state of the video input.')
ionVInAnalogStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 4), AnalogVideoStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInAnalogStandard.setStatus('current')
if mibBuilder.loadTexts: ionVInAnalogStandard.setDescription('Analog video standard (NTSC/PAL) currently detected by the video input.  This value is irrelevant if the analog video input lock state is unlocked.')
ionVInDigitalConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 5), DigitalVideoConnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInDigitalConnState.setStatus('current')
if mibBuilder.loadTexts: ionVInDigitalConnState.setDescription('Digital video connection state of the video input.')
ionVInDigitalStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 3, 2, 1, 6), DigitalVideoStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVInDigitalStandard.setStatus('current')
if mibBuilder.loadTexts: ionVInDigitalStandard.setDescription('Digital video standard (HDMI) currently detected by the video input.  This value is irrelevant if the digital video input lock state is unlocked.')
ionVideoOutputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 4))
ionVOutNumber = MibScalar((1, 3, 6, 1, 4, 1, 40748, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutNumber.setStatus('current')
if mibBuilder.loadTexts: ionVOutNumber.setDescription('Number of video outputs present.')
ionVOutTable = MibTable((1, 3, 6, 1, 4, 1, 40748, 4, 2), )
if mibBuilder.loadTexts: ionVOutTable.setStatus('current')
if mibBuilder.loadTexts: ionVOutTable.setDescription('Table containing the description of all video outputs present.')
ionVOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1), ).setIndexNames((0, "IONODES-IONSERIES-MIB", "ionVOutIndex"))
if mibBuilder.loadTexts: ionVOutEntry.setStatus('current')
if mibBuilder.loadTexts: ionVOutEntry.setDescription('Description of a video output.')
ionVOutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutIndex.setStatus('current')
if mibBuilder.loadTexts: ionVOutIndex.setDescription('Index of the video output (1-based).')
ionVOutDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutDescr.setStatus('current')
if mibBuilder.loadTexts: ionVOutDescr.setDescription('Video output user-friendly name.')
ionVOutAnalogSignalLock = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 3), AnalogVideoSignalLockState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutAnalogSignalLock.setStatus('current')
if mibBuilder.loadTexts: ionVOutAnalogSignalLock.setDescription('Analog signal lock state of the video output.')
ionVOutAnalogStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 4), AnalogVideoStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutAnalogStandard.setStatus('current')
if mibBuilder.loadTexts: ionVOutAnalogStandard.setDescription('Analog video standard (NTSC/PAL) currently detected by the video output.  This value is irrelevant if the analog video output lock state is unlocked.')
ionVOutDigitalConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 5), DigitalVideoConnState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutDigitalConnState.setStatus('current')
if mibBuilder.loadTexts: ionVOutDigitalConnState.setDescription('Digital video connection state of the video output.')
ionVOutDigitalStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 6), DigitalVideoStandard()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutDigitalStandard.setStatus('current')
if mibBuilder.loadTexts: ionVOutDigitalStandard.setDescription('Digital video standard (HDMI) currently detected by the video output.  This value is irrelevant if the digital video output lock state is unlocked.')
ionVOutStream1State = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 7), StreamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutStream1State.setStatus('current')
if mibBuilder.loadTexts: ionVOutStream1State.setDescription('State of the video stream #1 feeding the video output.')
ionVOutStream2State = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 8), StreamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutStream2State.setStatus('current')
if mibBuilder.loadTexts: ionVOutStream2State.setDescription('State of the video stream #2 feeding the video output.')
ionVOutStream3State = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 9), StreamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutStream3State.setStatus('current')
if mibBuilder.loadTexts: ionVOutStream3State.setDescription('State of the video stream #3 feeding the video output.')
ionVOutStream4State = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 4, 2, 1, 10), StreamState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionVOutStream4State.setStatus('current')
if mibBuilder.loadTexts: ionVOutStream4State.setDescription('State of the video stream #4 feeding the video output.')
ionAudioInputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 5))
ionAudioOutputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 6))
ionIoInputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 7))
ionIoInNumber = MibScalar((1, 3, 6, 1, 4, 1, 40748, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoInNumber.setStatus('current')
if mibBuilder.loadTexts: ionIoInNumber.setDescription('Number of digital I/O input pins present.')
ionIoInTable = MibTable((1, 3, 6, 1, 4, 1, 40748, 7, 2), )
if mibBuilder.loadTexts: ionIoInTable.setStatus('current')
if mibBuilder.loadTexts: ionIoInTable.setDescription('Table containing the description of all digital I/O input pins present.')
ionIoInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40748, 7, 2, 1), ).setIndexNames((0, "IONODES-IONSERIES-MIB", "ionIoInIndex"))
if mibBuilder.loadTexts: ionIoInEntry.setStatus('current')
if mibBuilder.loadTexts: ionIoInEntry.setDescription('Description of a digital I/O input pin.')
ionIoInIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoInIndex.setStatus('current')
if mibBuilder.loadTexts: ionIoInIndex.setDescription('Index of the digital I/O input pin (1-based).')
ionIoInDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoInDescr.setStatus('current')
if mibBuilder.loadTexts: ionIoInDescr.setDescription('Digital I/O input pin user-friendly name.')
ionIoInPinState = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 7, 2, 1, 3), IoPinState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoInPinState.setStatus('current')
if mibBuilder.loadTexts: ionIoInPinState.setDescription('State of the digital I/O input pin.')
ionIoOutputs = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 8))
ionIoOutNumber = MibScalar((1, 3, 6, 1, 4, 1, 40748, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoOutNumber.setStatus('current')
if mibBuilder.loadTexts: ionIoOutNumber.setDescription('Number of digital I/O output pins present.')
ionIoOutTable = MibTable((1, 3, 6, 1, 4, 1, 40748, 8, 2), )
if mibBuilder.loadTexts: ionIoOutTable.setStatus('current')
if mibBuilder.loadTexts: ionIoOutTable.setDescription('Table containing the description of all digital I/O output pins present.')
ionIoOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 40748, 8, 2, 1), ).setIndexNames((0, "IONODES-IONSERIES-MIB", "ionIoOutIndex"))
if mibBuilder.loadTexts: ionIoOutEntry.setStatus('current')
if mibBuilder.loadTexts: ionIoOutEntry.setDescription('Description of a digital I/O output pin.')
ionIoOutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoOutIndex.setStatus('current')
if mibBuilder.loadTexts: ionIoOutIndex.setDescription('Index of the digital I/O output pin (1-based).')
ionIoOutDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoOutDescr.setStatus('current')
if mibBuilder.loadTexts: ionIoOutDescr.setDescription('Digital I/O output pin user-friendly name.')
ionIoOutPinState = MibTableColumn((1, 3, 6, 1, 4, 1, 40748, 8, 2, 1, 3), IoPinState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ionIoOutPinState.setStatus('current')
if mibBuilder.loadTexts: ionIoOutPinState.setDescription('State of the digital I/O output pin.')
ionSerialPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 40748, 9))
mibBuilder.exportSymbols("IONODES-IONSERIES-MIB", ionReg=ionReg, ionAudioOutputs=ionAudioOutputs, ionVInAnalogStandard=ionVInAnalogStandard, ionR100=ionR100, StreamState=StreamState, ionIoOutTable=ionIoOutTable, ionIoOutPinState=ionIoOutPinState, ionVOutStream3State=ionVOutStream3State, ionSystem=ionSystem, ionVInEntry=ionVInEntry, ionVInDigitalStandard=ionVInDigitalStandard, ionIoInPinState=ionIoInPinState, ionSeriesModule=ionSeriesModule, ionSysMemUsage=ionSysMemUsage, ionSysCpuUsage=ionSysCpuUsage, ionModules=ionModules, ionVOutIndex=ionVOutIndex, PYSNMP_MODULE_ID=ionSeriesModule, ionVOutDigitalConnState=ionVOutDigitalConnState, ionIoOutDescr=ionIoOutDescr, ionE100Mini=ionE100Mini, ionIoInIndex=ionIoInIndex, ionodes=ionodes, ionCIRRUSSeries=ionCIRRUSSeries, ionVOutDescr=ionVOutDescr, ionE100HD=ionE100HD, DigitalVideoConnState=DigitalVideoConnState, ionVOutStream4State=ionVOutStream4State, AnalogVideoStandard=AnalogVideoStandard, ionIoInNumber=ionIoInNumber, ionVInDigitalConnState=ionVInDigitalConnState, ionIoOutputs=ionIoOutputs, ionVInNumber=ionVInNumber, ionE400=ionE400, ionVOutDigitalStandard=ionVOutDigitalStandard, ionProducts=ionProducts, ionIONSeries=ionIONSeries, ionIoInEntry=ionIoInEntry, ionSerialPorts=ionSerialPorts, DigitalVideoStandard=DigitalVideoStandard, AnalogVideoSignalLockState=AnalogVideoSignalLockState, ionVOutAnalogStandard=ionVOutAnalogStandard, ionE100=ionE100, ionAudioInputs=ionAudioInputs, ionIoOutNumber=ionIoOutNumber, ionIoOutIndex=ionIoOutIndex, ionVideoOutputs=ionVideoOutputs, ionVOutStream1State=ionVOutStream1State, ionVInDescr=ionVInDescr, ionVOutTable=ionVOutTable, ionIoOutEntry=ionIoOutEntry, ionVInAnalogSignalLock=ionVInAnalogSignalLock, ionSysTemperature=ionSysTemperature, ionIoInTable=ionIoInTable, ionVInTable=ionVInTable, ionObjectGroups=ionObjectGroups, ionVideoInputs=ionVideoInputs, ionVOutAnalogSignalLock=ionVOutAnalogSignalLock, ionIoInputs=ionIoInputs, ionVOutEntry=ionVOutEntry, ionVOutStream2State=ionVOutStream2State, IoPinState=IoPinState, ionVOutNumber=ionVOutNumber, ionVInIndex=ionVInIndex, ionConformance=ionConformance, ionIoInDescr=ionIoInDescr, tve110sd=tve110sd)
